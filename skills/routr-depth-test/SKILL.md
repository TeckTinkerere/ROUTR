---
name: routr-depth-test
description: "Test writing patterns when webapp-testing is not installed. Use when: routr-test bootstrap fails, adding tests without Anthropic webapp-testing skill."
---

# routr-depth-test

Fallback depth for `routr-test`. Load only when `webapp-testing` is not installed.

## Iron law

**Red-green-refactor — failing test before implementation when doing TDD.**

## Choose level

| Level | When |
|-------|------|
| Unit | Pure logic, utils, mocked hooks |
| Integration | API routes, DB, service boundaries |
| E2E | Critical user journeys |

## TDD loop

1. Write failing test
2. Minimal code to pass
3. Refactor with tests green

## E2E discipline

- Stable selectors: `data-testid`, role-based
- No flaky retries without fixing root cause
- Document run command: `npm test`, `npx playwright test`

## Web/React

- Test behavior, not implementation details
- a11y: keyboard path for critical flows

## Install full skills

```bash
npx skills@1.7.4 add anthropics/skills@webapp-testing -g -y --copy
npx skills@1.7.4 add obra/superpowers -g --skill test-driven-development -y --copy
```
