# routr-test boundaries

| Situation | Use instead |
|-----------|-------------|
| Click through the running app, screenshot, smoke test | `routr-qa` |
| Test already exists and fails — find out why | `routr-debug` |
| Test passes, ready to commit | `routr-ship` |
| Reviewing someone else's test PR | `routr-review` |

## routr-test vs routr-qa

Same surface (E2E, Playwright), different job: `routr-test` **writes** the test file that runs in CI on every push. `routr-qa` **drives** the app once — exploratory or post-deploy — and doesn't necessarily leave a test file behind. A Playwright spec being authored is `routr-test`; an agent clicking through a preview URL is `routr-qa`.

If the task is "write a Playwright test AND verify it now" — `routr-test` writes it, then a short `routr-qa` pass confirms the running app matches, not the other way around.
