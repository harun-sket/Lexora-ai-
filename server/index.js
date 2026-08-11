import express from "express";
import cors from "cors";
import crypto from "crypto";
import { createClient } from "@supabase/supabase-js";

const app = express();

const PORT = process.env.API_PORT || 5051;

const SUPABASE_URL =
  process.env.SUPABASE_URL ||
  "https://whoeifvapwtqnferbrtd.supabase.co";

const SUPABASE_SERVICE_ROLE_KEY =
  process.env.SUPABASE_SERVICE_ROLE_KEY;

if (!SUPABASE_SERVICE_ROLE_KEY) {
  console.error("");
  console.error("ERROR: SUPABASE_SERVICE_ROLE_KEY is missing.");
  console.error("");
  console.error(
    "Set it before starting the API:"
  );
  console.error(
    'export SUPABASE_SERVICE_ROLE_KEY="YOUR_SERVICE_ROLE_KEY"'
  );
  console.error("");
  process.exit(1);
}

const supabase = createClient(
  SUPABASE_URL,
  SUPABASE_SERVICE_ROLE_KEY,
  {
    auth: {
      autoRefreshToken: false,
      persistSession: false
    }
  }
);


app.use(cors());

app.use(
  express.json({
    limit: "2mb"
  })
);


/* ============================================================
   HELPERS
   ============================================================ */

function createRequestId() {
  return `lxr_${crypto
    .randomBytes(8)
    .toString("hex")}`;
}


function hashApiKey(key) {
  return crypto
    .createHash("sha256")
    .update(key)
    .digest("hex");
}


function sendError(
  res,
  statusCode,
  code,
  message
) {
  return res.status(statusCode).json({
    error: {
      code,
      message
    },
    request_id: createRequestId()
  });
}


function sendSuccess(
  res,
  results,
  statusCode = 200
) {
  return res.status(statusCode).json({
    status: "success",
    request_id: createRequestId(),
    results
  });
}


/* ============================================================
   API KEY AUTHENTICATION
   ============================================================ */

async function authenticateApiKey(
  req,
  res,
  next
) {

  const authorization =
    req.headers.authorization || "";

  if (
    !authorization.startsWith("Bearer ")
  ) {

    return sendError(
      res,
      401,
      "missing_api_key",
      "Authorization Bearer token is required."
    );

  }


  const apiKey =
    authorization
      .slice(7)
      .trim();


  if (!apiKey) {

    return sendError(
      res,
      401,
      "missing_api_key",
      "API key is required."
    );

  }


  const keyHash =
    hashApiKey(apiKey);


  const {
    data: apiKeyRecord,
    error
  } = await supabase
    .from("api_keys")
    .select(
      "id,user_id,name,key_prefix,key_hash,last_used_at,created_at,revoked_at"
    )
    .eq(
      "key_hash",
      keyHash
    )
    .maybeSingle();


  if (error) {

    console.error(
      "API key lookup failed:",
      error
    );

    return sendError(
      res,
      500,
      "authentication_error",
      "Unable to validate API key."
    );

  }


  if (!apiKeyRecord) {

    return sendError(
      res,
      401,
      "invalid_api_key",
      "API key is invalid."
    );

  }


  if (
    apiKeyRecord.revoked_at
  ) {

    return sendError(
      res,
      401,
      "revoked_api_key",
      "API key has been revoked."
    );

  }


  req.apiKey = apiKeyRecord;

  req.userId =
    apiKeyRecord.user_id;


  next();

}


/* ============================================================
   USAGE LOGGING
   ============================================================ */

async function logUsage({
  userId,
  apiKeyId,
  tokens = 0,
  processingMs = null,
  status = "success",
  statusCode = 200
}) {

  try {

    await supabase
      .from("usage_events")
      .insert({
        user_id: userId,
        api_key_id: apiKeyId,
        tokens,
        processing_ms:
          processingMs,
        status,
        status_code: statusCode
      });

  } catch (err) {

    console.error(
      "Usage logging failed:",
      err
    );

  }

}


/* ============================================================
   UPDATE LAST USED
   ============================================================ */

async function updateLastUsed(
  apiKeyId
) {

  try {

    await supabase
      .from("api_keys")
      .update({
        last_used_at:
          new Date().toISOString()
      })
      .eq(
        "id",
        apiKeyId
      );

  } catch (err) {

    console.error(
      "last_used_at update failed:",
      err
    );

  }

}


/* ============================================================
   HEALTH
   ============================================================ */

app.get(
  "/v1/health",
  async (req, res) => {

    return res.json({

      status: "ok",

      service:
        "lexora-api",

      version:
        "1.0.0",

      engine:
        "online"

    });

  }
);


/* ============================================================
   API ROOT
   ============================================================ */

app.get(
  "/",
  (req, res) => {

    return res.json({

      name:
        "Lexora API",

      version:
        "1.0.0",

      status:
        "online",

      endpoints: [

        "GET /v1/health",

        "POST /v1/intelligence",

        "POST /v1/datasets/process"

      ]

    });

  }
);


/* ============================================================
   INTELLIGENCE
   ============================================================ */

app.post(
  "/v1/intelligence",
  authenticateApiKey,
  async (req, res) => {

    const started =
      Date.now();

    const {
      text,
      language = "en",
      tasks = []
    } = req.body || {};


    if (
      typeof text !== "string" ||
      !text.trim()
    ) {

      const processingMs =
        Date.now() - started;

      await logUsage({
        userId:
          req.userId,

        apiKeyId:
          req.apiKey.id,

        tokens: 0,

        processingMs,

        status:
          "rejected",

        statusCode:
          400
      });

      return sendError(
        res,
        400,
        "invalid_text",
        "The 'text' field is required."
      );

    }


    if (
      !Array.isArray(tasks)
    ) {

      const processingMs =
        Date.now() - started;

      await logUsage({
        userId:
          req.userId,

        apiKeyId:
          req.apiKey.id,

        tokens: 0,

        processingMs,

        status:
          "rejected",

        statusCode:
          400
      });

      return sendError(
        res,
        400,
        "invalid_tasks",
        "The 'tasks' field must be an array."
      );

    }


    /*
     * ========================================================
     * LEXORA ENGINE
     * ========================================================
     *
     * THIS IS WHERE YOUR FINISHED ENGINE GOES.
     *
     * For now this returns a safe API-shaped result.
     *
     * Replace this object with your actual engine call.
     */

    const results = {

      language,

      confidence:
        0.98,

      text_length:
        text.length,

      tasks,

      classification:
        tasks.includes(
          "classification"
        )
          ? {
              label:
                "general",

              confidence:
                0.98
            }
          : undefined,

      entities:
        tasks.includes(
          "entities"
        )
          ? []
          : undefined,

      summary:
        tasks.includes(
          "summary"
        )
          ? (
              text.length > 180
                ? `${text.slice(0, 177)}...`
                : text
            )
          : undefined

    };


    const processingMs =
      Date.now() - started;


    const tokens =
      Math.max(
        1,
        Math.ceil(
          text.length / 4
        )
      );


    await logUsage({

      userId:
        req.userId,

      apiKeyId:
        req.apiKey.id,

      tokens,

      processingMs,

      status:
        "success",

      statusCode:
        200

    });


    await updateLastUsed(
      req.apiKey.id
    );


    return sendSuccess(
      res,
      results
    );

  }
);


/* ============================================================
   DATASET PROCESSING
   ============================================================ */

app.post(
  "/v1/datasets/process",
  authenticateApiKey,
  async (req, res) => {

    const started =
      Date.now();

    const {
      data,
      language = "en"
    } = req.body || {};


    if (
      data === undefined ||
      data === null
    ) {

      const processingMs =
        Date.now() - started;

      await logUsage({

        userId:
          req.userId,

        apiKeyId:
          req.apiKey.id,

        tokens: 0,

        processingMs,

        status:
          "rejected",

        statusCode:
          400

      });

      return sendError(
        res,
        400,
        "invalid_dataset",
        "The 'data' field is required."
      );

    }


    /*
     * DATASET ENGINE INTEGRATION POINT
     */

    const records =
      Array.isArray(data)
        ? data.length
        : 1;


    const processingMs =
      Date.now() - started;


    await logUsage({

      userId:
        req.userId,

      apiKeyId:
        req.apiKey.id,

      tokens:
        records,

      processingMs,

      status:
        "success",

      statusCode:
        200

    });


    await updateLastUsed(
      req.apiKey.id
    );


    return sendSuccess(
      res,
      {

        language,

        processed:
          true,

        records

      }
    );

  }
);


/* ============================================================
   404
   ============================================================ */

app.use(
  (req, res) => {

    return sendError(
      res,
      404,
      "not_found",
      "The requested endpoint does not exist."
    );

  }
);


/* ============================================================
   SERVER
   ============================================================ */

app.listen(
  PORT,
  "0.0.0.0",
  () => {

    console.log("");
    console.log(
      "========================================"
    );
    console.log(
      "          LEXORA API V1"
    );
    console.log(
      "========================================"
    );
    console.log("");

    console.log(
      `PORT: ${PORT}`
    );

    console.log(
      `URL: http://localhost:${PORT}`
    );

    console.log("");

    console.log(
      "GET  /v1/health"
    );

    console.log(
      "POST /v1/intelligence"
    );

    console.log(
      "POST /v1/datasets/process"
    );

    console.log("");

    console.log(
      "SUPABASE: CONNECTED"
    );

    console.log(
      "API KEY AUTH: ENABLED"
    );

    console.log(
      "USAGE LOGGING: ENABLED"
    );

    console.log("");

  }
);

