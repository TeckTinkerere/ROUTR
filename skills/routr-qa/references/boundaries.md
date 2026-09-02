# routr-qa boundaries

| Situation | Use instead |
|-----------|-------------|
| Writing a Playwright spec that lives in the repo and runs in CI | `routr-test` |
| Found a real bug — now diagnose and fix it | `routr-debug` |
| Visual redesign or a11y implementation | `routr-frontend` |
| Animation feels off | `routr-motion` |
| No running app or preview URL exists yet | `routr-deploy` first, then this skill |

## routr-qa vs routr-test

See [routr-test boundaries](../../routr-test/references/boundaries.md#routr-test-vs-routr-qa) for the canonical statement of this split — `routr-qa` drives the app once, `routr-test` writes the spec file that runs every time.
