import "dotenv/config";
import express from "express";
import cors from "cors";
import { clerkMiddleware, getAuth } from "@clerk/express";
import { createClient } from "@supabase/supabase-js";

const app = express();

const PORT =
  process.env.AUTH_SYNC_PORT || 5052;

const supabaseUrl =
  process.env.SUPABASE_URL;

const supabaseServiceKey =
  process.env.SUPABASE_SERVICE_ROLE_KEY;

const clerkSecretKey =
  process.env.CLERK_SECRET_KEY;

const clerkPublishableKey =
  process.env.CLERK_PUBLISHABLE_KEY;

if (!supabaseUrl) {
  console.error(
    "❌ SUPABASE_URL is missing"
  );
  process.exit(1);
}

if (!supabaseServiceKey) {
  console.error(
    "❌ SUPABASE_SERVICE_ROLE_KEY is missing"
  );
  process.exit(1);
}

if (!clerkSecretKey) {
  console.error(
    "❌ CLERK_SECRET_KEY is missing"
  );
  process.exit(1);
}

if (!clerkPublishableKey) {
  console.error(
    "❌ CLERK_PUBLISHABLE_KEY is missing"
  );
  process.exit(1);
}


const supabase =
  createClient(
    supabaseUrl,
    supabaseServiceKey,
    {
      auth: {
        autoRefreshToken: false,
        persistSession: false
      }
    }
  );


app.use(cors());

app.use(express.json());

app.use(
  clerkMiddleware({
    secretKey:
      clerkSecretKey,

    publishableKey:
      clerkPublishableKey
  })
);


/*
============================================================
HEALTH
============================================================
*/

app.get(
  "/health",
  (req, res) => {

    res.json({
      status: "online",
      service: "lexora-auth-sync"
    });

  }
);


/*
============================================================
SYNC CLERK USER
============================================================

IMPORTANT:

This endpoint assumes your Clerk user is already
authenticated.

The Clerk user ID is NOT inserted directly into
profiles.id because your database currently requires:

profiles.id -> auth.users.id

Therefore this endpoint expects a Supabase Auth user
to already exist for the user.

If you have not configured Clerk <-> Supabase Auth
synchronization yet, this endpoint will tell you that
instead of creating a broken profile.
*/

app.post(
  "/auth/sync",
  async (req, res) => {

    try {

      const auth =
        getAuth(req);

      if (!auth.userId) {

        return res.status(401).json({
          error: {
            code: "not_authenticated",
            message:
              "You must be signed in with Clerk."
          }
        });

      }


      const clerkUserId =
        auth.userId;


      /*
      --------------------------------------------------------
      Find an existing Supabase Auth user.

      Your current schema requires profiles.id to equal
      an auth.users.id.
      --------------------------------------------------------
      */

      const {
        data: users,
        error: usersError
      } =
        await supabase.auth.admin.listUsers({
          page: 1,
          perPage: 100
        });


      if (usersError) {

        console.error(
          "Supabase Auth lookup failed:",
          usersError
        );

        return res.status(500).json({
          error: {
            code:
              "supabase_auth_lookup_failed",
            message:
              usersError.message
          }
        });

      }


      /*
      --------------------------------------------------------
      Look for a user whose metadata contains the Clerk ID.
      --------------------------------------------------------
      */

      const supabaseUser =
        users.users.find(
          user =>
            user.user_metadata
              ?.clerk_user_id ===
            clerkUserId
        );


      if (!supabaseUser) {

        return res.status(409).json({

          error: {

            code:
              "supabase_user_not_synced",

            message:
              "The Clerk user is authenticated, but no matching Supabase Auth user exists yet."

          },

          clerk_user_id:
            clerkUserId,

          next_step:
            "Configure Clerk to synchronize users with Supabase Auth before creating the profile."

        });

      }


      /*
      --------------------------------------------------------
      Get email from Supabase Auth.
      --------------------------------------------------------
      */

      const email =
        supabaseUser
          .email_addresses?.[0]
          ?.email_address ||
        null;


      /*
      --------------------------------------------------------
      Create/update Lexora profile.
      --------------------------------------------------------
      */

      const {
        data: profile,
        error: profileError
      } =
        await supabase
          .from("profiles")
          .upsert(
            {
              id:
                supabaseUser.id,

              email,

              display_name:
                req.body?.display_name ||
                null,

              plan:
                "free",

              updated_at:
                new Date().toISOString()

            },
            {
              onConflict: "id"
            }
          )
          .select()
          .single();


      if (profileError) {

        console.error(
          "Profile sync failed:",
          profileError
        );

        return res.status(500).json({

          error: {

            code:
              "profile_sync_failed",

            message:
              profileError.message

          }

        });

      }


      /*
      --------------------------------------------------------
      Ensure subscription exists.
      --------------------------------------------------------
      */

      const {
        error:
          subscriptionError
      } =
        await supabase
          .from("subscriptions")
          .upsert(
            {
              user_id:
                profile.id,

              plan:
                "free",

              status:
                "active",

              updated_at:
                new Date().toISOString()

            },
            {
              onConflict:
                "user_id"
            }
          );


      if (subscriptionError) {

        console.error(
          "Subscription sync failed:",
          subscriptionError
        );

      }


      return res.json({

        status:
          "success",

        message:
          "Clerk user synchronized with Lexora.",

        clerk_user_id:
          clerkUserId,

        supabase_user_id:
          profile.id,

        profile

      });

    } catch (error) {

      console.error(
        "AUTH SYNC ERROR:",
        error
      );

      return res.status(500).json({

        error: {

          code:
            "auth_sync_error",

          message:
            error.message

        }

      });

    }

  }
);


/*
============================================================
DATABASE CONNECTION TEST
============================================================
*/

app.get(
  "/database-test",
  async (req, res) => {

    try {

      const {
        data,
        error
      } =
        await supabase
          .from("profiles")
          .select("id")
          .limit(1);


      if (error) {

        return res.status(500).json({

          status:
            "error",

          message:
            error.message

        });

      }


      return res.json({

        status:
          "connected",

        database:
          "supabase",

        table:
          "profiles",

        rows:
          data.length

      });

    } catch (error) {

      return res.status(500).json({

        status:
          "error",

        message:
          error.message

      });

    }

  }
);


/*
============================================================
START
============================================================
*/

app.listen(
  PORT,
  "0.0.0.0",
  () => {

    console.log("");
    console.log(
      "========================================"
    );
    console.log(
      "       LEXORA AUTH SYNC"
    );
    console.log(
      "========================================"
    );
    console.log("");

    console.log(
      `Server: http://localhost:${PORT}`
    );

    console.log(
      "Clerk: configured"
    );

    console.log(
      "Supabase: configured"
    );

    console.log(
      "Profile sync: enabled"
    );

    console.log("");

  }
);

