import { Clerk } from "@clerk/clerk-js";

const key =
  import.meta.env.VITE_CLERK_PUBLISHABLE_KEY;

const app =
  document.getElementById("app");

try {

  if (!key) {
    throw new Error(
      "VITE_CLERK_PUBLISHABLE_KEY is missing"
    );
  }

  app.innerHTML = `
    <h1>LEXORA CLERK</h1>
    <p>Publishable key found.</p>
    <p>Loading Clerk...</p>
  `;

  const clerk = new Clerk(key);

  await clerk.load();

  app.innerHTML = `
    <h1>🔥 CLERK LOADED</h1>

    <p>
      Clerk initialized successfully.
    </p>

    <p>
      Signed in:
      <strong>${clerk.isSignedIn}</strong>
    </p>
  `;

} catch (error) {

  app.innerHTML = `
    <h1>❌ CLERK FAILED</h1>

    <pre style="
      white-space:pre-wrap;
      word-break:break-word;
      color:#ff8080;
    ">${error?.message || error}</pre>
  `;

  console.error(error);

}
