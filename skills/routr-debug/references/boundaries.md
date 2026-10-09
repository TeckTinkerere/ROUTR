# routr-debug boundaries

## Precedence (more specific wins)

| Situation | Use instead |
|-----------|-------------|
| Known fix, tests pass, need commit | `routr-ship` |
| "How does auth work?" | `routr-explore` |
| Security vulnerability report | `routr-security` |
| Layout looks wrong, no error | `routr-frontend` (visual) or `routr-debug` (logic) |
| Animation jank | `routr-motion` |
| Slow, not wrong (Core Web Vitals, bundle, N+1, leak) | `routr-perf` |
| A domain's own machinery failing (agent loop, AI SDK stream, video render, EAS build, migration runner) | the domain router (`routr-agents` / `routr-ai` / `routr-video` / `routr-mobile` / `routr-database`); back here only if the cause is outside the domain |

## vs routr-ship

- **routr-debug**: root cause unknown or reproduction failing
- **routr-ship**: fix is understood, impact scoped, ready to verify + commit

## vs routr-test

- **routr-debug**: existing test fails or behavior wrong
- **routr-test**: writing new tests or TDD for a feature
