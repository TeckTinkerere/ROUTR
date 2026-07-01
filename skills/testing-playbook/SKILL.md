---
name: testing-playbook
description: "Write and run tests (TDD, unit, E2E, Playwright). Use when: add tests, TDD, coverage, failing test suite."
---

# Testing playbook

**Goal:** tests that prove behavior — written in the right order, at the right level.

## 0. Bootstrap

Read if present (see `playbook-common/references/skill-catalog.md`):

| Order | Skill | Role |
|-------|-------|------|
| 1 | `test-driven-development` | Obra: red-green-refactor before implementation |
| 2 | `tdd` | Matt Pocock: slice work into testable issues |
| 3 | `webapp-testing` | Anthropic: local web app test patterns |
| 4 | `playwright-best-practices` | E2E structure, selectors, stability |
| 5 | `playwright-cli` | Microsoft Playwright CLI workflows |

For debugging failing tests → switch to `debugging-playbook` after loading `systematic-debugging`.

## 1. Choose test level

| Level | When |
|-------|------|
| Unit | Pure logic, utils, hooks with mocked deps |
| Integration | API routes, DB queries, service boundaries |
| E2E | Critical user journeys, auth flows, checkout |

## 2. TDD loop (feature or bugfix)

1. Read `test-driven-development` — write failing test first
2. Minimal implementation to pass
3. Refactor with tests green
4. Do not skip tests to "save time"

## 3. Web / React

- `webapp-testing` for component and app-level testing setup
- `vercel-react-best-practices` if tests touch data-fetching or RSC boundaries
- Frontend UI under test? Skim `frontend-feature-playbook` for a11y targets

## 4. E2E

1. `playwright-best-practices` for test design
2. Prefer stable selectors (`data-testid`, role-based)
3. For live browser dogfooding → `e2e-qa-playbook` (`agent-browser`)

## 5. Verify

- [ ] Tests fail before fix (when doing TDD)
- [ ] No flaky retries without fixing root cause
- [ ] CI-relevant command documented (`npm test`, `npx playwright test`)

## Handoff

- Ship after tests green → `fix-and-ship-playbook`
- Review test quality on PR → `code-review-playbook`
