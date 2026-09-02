# Test fallback (no child skills installed)

Use when `webapp-testing` and `routr-depth-test` are both unavailable.

## Iron law

```
FAILING TEST BEFORE IMPLEMENTATION WHEN DOING TDD
```

## Minimum process

1. **Pick the level** — unit (pure logic), integration (API/DB boundary), or E2E (critical journey). Default to the cheapest level that actually proves the behavior.
2. **Write the failing test first** — run it, confirm it fails for the right reason (not a syntax error).
3. **Minimal implementation** — just enough to pass.
4. **Refactor with tests green.**
5. **Document the run command** — `npm test`, `npx playwright test`, whatever the project uses. A test nobody can re-run isn't done.

## E2E discipline (if no Playwright skill available)

- Stable selectors: `data-testid` or role-based, never CSS classes that change with styling
- No flaky retries without fixing the root cause
- One critical journey per test, not a mega-test covering the whole app

## Escalate to install

```bash
npx skills add anthropics/skills@webapp-testing -g -y --copy
npx skills add obra/superpowers -g --skill test-driven-development -y --copy
```
