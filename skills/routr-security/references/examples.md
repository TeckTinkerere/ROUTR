# Security examples

## Example 1: Pre-launch audit

**Input:** "We're launching publicly next week — is this secure?"

**Expected:** Full scope pass (authN/authZ, injection, secrets, dependency CVEs), `semgrep` run, RLS check via `routr-database`, severity-ranked report with exploit scenarios.

## Example 2: Scoped PR check

**Input:** "Any security issues in this PR?"

**Expected:** `semgrep` on changed paths only, not the whole repo. Findings only for what changed.

## Example 3: RLS policy review

**Input:** "Check our Supabase RLS policies are correct for multi-tenant data."

**Expected:** Hand off the schema/policy read to `routr-database`, apply the security lens (can tenant A read tenant B's rows under any policy gap) on top.

## Example 4: Non-security bug (boundary case)

**Input:** "This form silently fails to submit."

**Expected:** Route to `routr-debug` — no security angle stated or apparent; don't force a security framing onto an ordinary bug.
