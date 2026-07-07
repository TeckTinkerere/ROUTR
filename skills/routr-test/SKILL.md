---
name: routr-test
description: "Write and run tests (TDD, unit, E2E, Playwright). Use when: add tests, TDD, coverage, failing test suite, 'write tests for this'. Not for: browser smoke test (→ routr-qa); diagnosing why a test fails (→ routr-debug)."
---

# routr-test

**Goal:** tests that prove behavior — right order, right level.

## 0. Bootstrap

See `routr-catalog/references/skill-registry.md`:

| Order | Skill | Tier |
|-------|-------|------|
| 1 | `test-driven-development` | required |
| 2 | `tdd` | recommended |
| 3 | `webapp-testing` | recommended |
| 4 | `playwright-best-practices` | optional |
| 5 | `playwright-cli` | optional |

If `webapp-testing` missing → `routr-depth-test`.

Failing tests debug → `routr-debug` + `systematic-debugging`.

## 1. Choose test level

| Level | When |
|-------|------|
| Unit | Pure logic, utils, mocked deps |
| Integration | API routes, DB, services |
| E2E | Critical user journeys |

## 2. TDD loop

1. Failing test first
2. Minimal pass
3. Refactor green

## 3. Verify

- [ ] Tests fail before fix (TDD)
- [ ] No flaky retries without root cause fix
- [ ] CI command documented

## Handoff

- Ship → `routr-ship`
- Review test PR → `routr-review`
