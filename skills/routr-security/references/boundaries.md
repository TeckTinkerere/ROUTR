# routr-security boundaries

| Situation | Use instead |
|-----------|-------------|
| Bug or crash with no security angle | `routr-debug` |
| General PR review (style, correctness) | `routr-review` |
| RLS/schema design with no audit request | `routr-database` |
| Fixing the findings once identified | `routr-ship` |

## routr-security vs routr-review

`routr-review` covers correctness, spec adherence, standards, security, performance, UX/a11y in one pass and escalates to `routr-security` when it hits something security-shaped. `routr-security` is the deep pass on that one axis — run it directly when the request is explicitly a security audit, or when `routr-review` escalates mid-review.
