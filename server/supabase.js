import { createClient } from "@supabase/supabase-js";

const supabaseUrl =
  process.env.SUPABASE_URL;

const supabaseServiceRoleKey =
  process.env.SUPABASE_SERVICE_ROLE_KEY;

if (!supabaseUrl) {
  throw new Error(
    "SUPABASE_URL is missing."
  );
}

if (!supabaseServiceRoleKey) {
  throw new Error(
    "SUPABASE_SERVICE_ROLE_KEY is missing."
  );
}

export const supabase =
  createClient(
    supabaseUrl,
    supabaseServiceRoleKey,
    {
      auth: {
        autoRefreshToken: false,
        persistSession: false
      }
    }
  );

export async function testSupabase() {

  const {
    data,
    error
  } = await supabase
    .from("profiles")
    .select("id")
    .limit(1);

  if (error) {

    console.error(
      "SUPABASE CONNECTION FAILED"
    );

    console.error(
      error.message
    );

    throw error;
  }

  console.log(
    "SUPABASE CONNECTION SUCCESSFUL"
  );

  console.log(
    `profiles table accessible: ${data.length >= 0}`
  );

  return true;
}
