---
name: routr-test
description: "Write and run tests (TDD, unit, E2E, Playwright). Use when: add tests, TDD, coverage, failing test suite, 'write tests for this'. Not for: browser smoke test (→ routr-qa); diagnosing why a test fails (→ routr-debug)."
---

# routr-test

**Goal:** tests that prove behavior — right order, right level.

## When to activate

- Adding test coverage, TDD, "write tests for this"
- Failing suite that needs new/updated tests (not root-cause debugging)
- Setting up or extending Playwright/E2E

## Do not activate

- Click through the running app / smoke test → `routr-qa`
- Diagnosing *why* an existing test fails → `routr-debug`
- Fixing the code so a test passes and shipping the diff → `routr-ship`

## Iron law

**Failing test before implementation when doing TDD — never write the pass first.**

## 0. Bootstrap

See `routr-catalog/references/skill-registry.md`:

| Order | Skill | Tier |
|-------|-------|------|
| 1 | `test-driven-development` | required |
| 2 | `tdd` | recommended |
| 3 | `webapp-testing` | recommended |
| 4 | `playwright-best-practices` | optional |
| 5 | `playwright-cli` | optional |

**Budget gate:** `test-driven-development` + the test level's own docs for a routine test. Add Playwright rows only for E2E work.

If `webapp-testing` missing → read `routr-depth-test` OR [references/fallback.md](./references/fallback.md).

Failing tests debug → `routr-debug` + `systematic-debugging`.

## 1. Choose test level (medium freedom)

| Level | When |
|-------|------|
| Unit | Pure logic, utils, mocked deps |
| Integration | API routes, DB, services |
| E2E | Critical user journeys |

## 2. TDD loop (low freedom)

1. Failing test first
2. Minimal pass
3. Refactor green

## 3. Verify (low freedom)

- [ ] Tests fail before fix (TDD)
- [ ] No flaky retries without root cause fix
- [ ] CI command documented

## Output format

```markdown
## Test report
**Level:** unit / integration / E2E
**Coverage added:** files / behaviors
**Run command:** …
**Verified:** yes/no — failing-first confirmed, now green
```

## Handoff

| Need | Router |
|------|--------|
| Ship the change | `routr-ship` |
| Review test PR | `routr-review` |
| Test fails for unknown reason | `routr-debug` |
| Browser smoke test / preview check | `routr-qa` |

## References

- [fallback](./references/fallback.md) — when `webapp-testing` is missing
- [gotchas](./references/gotchas.md)
- [examples](./references/examples.md)
- [boundaries](./references/boundaries.md)

## Anti-patterns

- Writing the implementation before a failing test in a TDD flow
- Testing implementation details instead of behavior
- Retrying a flaky test instead of fixing its root cause
- Loading Playwright rules for a pure-unit-test task
