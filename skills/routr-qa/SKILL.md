---
name: routr-qa
description: "Test the app in a real browser (click, screenshot, smoke test). Use when: QA, E2E, 'open the site and check', preview verification, smoke test. Not for: writing test files (→ routr-test); fixing a bug you find (→ routr-debug)."
---

# routr-qa

**Goal:** prove the app works in a real browser — not guess from reading the code.

## When to activate

- "Open the site and check", exploratory QA, smoke test
- Post-deploy preview verification
- Confirming a fix actually works in the running app

## Do not activate

- Authoring a Playwright spec file that lives in the repo → `routr-test`
- A bug was found — now fix it → `routr-debug`
- No running app / preview URL available → can't verify; say so

## Iron law

**Claim nothing works until you've actually driven the browser and seen it — reading the code is not verification.**

## 0. Bootstrap

See `routr-catalog/references/skill-registry.md`:

| Order | Skill | Tier |
|-------|-------|------|
| 1 | `agent-browser` | recommended — exploratory QA, screenshots |
| 2 | `webapp-testing` | recommended — local web patterns |
| 3 | `playwright-best-practices` | optional — durable E2E design |
| 4 | `playwright-cli` | optional — Playwright automation |

If both `agent-browser` and `webapp-testing` are missing → [references/fallback.md](./references/fallback.md).

## 1. Mode (medium freedom)

| Mode | When |
|------|------|
| Exploratory | `agent-browser` journey through the app |
| Repeatable E2E | Playwright spec already in repo |
| Post-deploy | `agent-browser` on the preview URL |

## 2. Exploratory (medium freedom)

Define checklist; screenshot on failure; report bugs → `routr-debug`.

## 3. Automated E2E (medium freedom)

`playwright-best-practices`; run in CI — see `routr-test`.

## 4. Frontend quality (medium freedom)

Visual → `routr-frontend` / `routr-motion`. a11y → `web-design-guidelines`.

## 5. Verify (low freedom)

- [ ] Actually navigated the app — not inferred from source
- [ ] Screenshot or console log captured for any failure
- [ ] Checklist items each have a pass/fail, not "looks fine"

## Output format

```markdown
## QA report
**Mode:** exploratory / E2E / post-deploy
**Checklist:** item — pass/fail — evidence
**Bugs found:** … (hand off to routr-debug)
**Verified:** yes/no
```

## Handoff

| Need | Router |
|------|--------|
| Bug found | `routr-debug` |
| Deploy then verify | `routr-deploy` → this skill |
| New test file for CI | `routr-test` |

## References

- [fallback](./references/fallback.md) — when no browser-automation skill is installed
- [gotchas](./references/gotchas.md)
- [examples](./references/examples.md)
- [boundaries](./references/boundaries.md)

## Anti-patterns

- Reporting "works" from reading code instead of driving the browser
- Writing a permanent Playwright spec when the task was a one-off check
- Fixing a bug found during QA instead of handing off to `routr-debug`
