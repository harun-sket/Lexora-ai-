import { Clerk } from "@clerk/clerk-js";

const publishableKey =
  import.meta.env.VITE_CLERK_PUBLISHABLE_KEY;

if (!publishableKey) {
  throw new Error(
    "VITE_CLERK_PUBLISHABLE_KEY is missing"
  );
}

export const clerk = new Clerk(
  publishableKey
);

export async function initClerk() {
  await clerk.load();
  return clerk;
}
