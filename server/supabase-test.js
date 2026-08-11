console.log("================================");
console.log("LEXORA SUPABASE TEST STARTED");
console.log("================================");

console.log(
  "SUPABASE_URL:",
  process.env.SUPABASE_URL
    ? "SET"
    : "MISSING"
);

console.log(
  "SUPABASE_SERVICE_ROLE_KEY:",
  process.env.SUPABASE_SERVICE_ROLE_KEY
    ? "SET"
    : "MISSING"
);

if (!process.env.SUPABASE_URL) {
  console.error("❌ SUPABASE_URL IS MISSING");
  process.exit(1);
}

if (!process.env.SUPABASE_SERVICE_ROLE_KEY) {
  console.error(
    "❌ SUPABASE_SERVICE_ROLE_KEY IS MISSING"
  );
  process.exit(1);
}

console.log("✓ Environment variables found.");

const {
  createClient
} = await import("@supabase/supabase-js");

console.log("✓ Supabase package loaded.");

const supabase = createClient(
  process.env.SUPABASE_URL,
  process.env.SUPABASE_SERVICE_ROLE_KEY,
  {
    auth: {
      autoRefreshToken: false,
      persistSession: false
    }
  }
);

console.log("✓ Supabase client created.");
console.log("Testing database...");

try {

  const {
    data,
    error
  } = await supabase
    .from("profiles")
    .select("id")
    .limit(1);

  if (error) {

    console.error("");
    console.error("❌ SUPABASE DATABASE ERROR");
    console.error("message:", error.message);
    console.error("code:", error.code);
    console.error("details:", error.details);
    console.error("hint:", error.hint);
    console.error("");

    process.exit(1);
  }

  console.log("");
  console.log("🔥🔥🔥 SUPABASE CONNECTED 🔥🔥🔥");
  console.log(
    "profiles rows:",
    data?.length ?? 0
  );
  console.log("");

} catch (error) {

  console.error("");
  console.error("❌ SUPABASE REQUEST FAILED");
  console.error(error);
  console.error("");

  process.exit(1);
}
