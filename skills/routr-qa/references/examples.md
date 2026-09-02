# QA examples

## Example 1: Post-deploy smoke test

**Input:** "Deployed to preview — check it works."

**Expected:** `agent-browser` on the preview URL, checklist of critical paths (load, primary action, one form submit), evidence per item, bugs handed to `routr-debug`.

## Example 2: "Write a test for the login flow"

**Input:** "Write a test for the login flow."

**Expected:** Route to `routr-test` — this is spec authoring, not a one-off browser check, even though it's the same surface.

## Example 3: Exploratory bug hunt

**Input:** "Click around the checkout flow and see if anything's broken."

**Expected:** Exploratory mode, screenshot on any failure, report as a bug list — do not attempt fixes from within `routr-qa`.

## Example 4: No preview exists

**Input:** "Check the new feature works" (feature branch not deployed, no local server running)

**Expected:** State that there's nothing to drive yet; hand off to `routr-deploy` or ask the user to start the dev server before QA can run.
