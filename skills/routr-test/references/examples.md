# Test examples

## Example 1: TDD for a new utility function

**Input:** "Add a function that formats currency, with tests."

**Expected:** Write the failing test first (assert formatted output for a few cases), confirm it fails, implement the minimal function, confirm green. Unit level — no Playwright.

## Example 2: Failing suite, unclear cause

**Input:** "The test suite is red on CI and I don't know why."

**Expected:** Route to `routr-debug` first — root cause is unknown. `routr-test` is for writing/extending tests, not diagnosing an existing failure.

## Example 3: Critical journey needs E2E coverage

**Input:** "We don't have any test coverage on the checkout flow."

**Expected:** E2E level, `playwright-best-practices` loaded, stable selectors (`data-testid` / role-based), documented run command.

## Example 4: "Check the site works" (boundary case)

**Input:** "Open the preview URL and check it works."

**Expected:** Hand off to `routr-qa` — this is exploratory verification, not test authoring, even though both skills touch a browser.
