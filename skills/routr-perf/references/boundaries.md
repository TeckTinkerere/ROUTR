# routr-perf boundaries

| Situation | Use instead |
|-----------|-------------|
| Output is wrong, not slow | `routr-debug` |
| One slow SQL query, index, or schema design | `routr-database` |
| Visual redesign with no perf complaint | `routr-frontend` |
| Post-deploy smoke test with no perf claim | `routr-qa` |
| Authoring or polishing an animation | `routr-motion` |
| Structural cleanup with no measured slowness | `routr-refactor` |

## vs routr-database

- **routr-perf**: N+1 query fan-out, connection-pool exhaustion, or latency spread across many queries at the app/request level
- **routr-database**: one specific slow query, missing index, or schema/migration design

## vs routr-motion

- **routr-perf**: diagnose *why* an animation is janky or dropping frames (profiling, main-thread blocking, layout thrash)
- **routr-motion**: author or polish the animation itself once the cause is known

Chain: `routr-perf` locates the cause → `routr-motion` implements the fix if it's an animation-authoring change.

## vs routr-refactor

- **routr-perf**: goal is speed, backed by a measured baseline number
- **routr-refactor**: goal is structure/readability, behavior and performance unchanged

## vs routr-debug

- **routr-perf**: behavior is correct, just slow or resource-heavy
- **routr-debug**: behavior is wrong (crash, wrong output, exception) — fix that first, perf second
