---
name: routr-qa
description: "Test the app in a real browser (click, screenshot, smoke test). Use when: QA, E2E, 'open the site and check', preview verification, smoke test. Not for: writing test files (→ routr-test); fixing a bug you find (→ routr-debug)."
---

# routr-qa

**Goal:** prove the app works in a real browser.

## 0. Bootstrap

| Skill | Role |
|-------|------|
| `agent-browser` | Exploratory QA, screenshots |
| `webapp-testing` | Local web patterns |
| `playwright-best-practices` | Durable E2E design |
| `playwright-cli` | Playwright automation |

## 1. Mode

| Mode | When |
|------|------|
| Exploratory | `agent-browser` journey |
| Repeatable E2E | Playwright in repo |
| Post-deploy | `agent-browser` on preview URL |

## 2. Exploratory

Define checklist; screenshots on failure; report bugs → `routr-debug`

## 3. Automated E2E

`playwright-best-practices`; run in CI — see `routr-test`

## 4. Frontend quality

Visual → `routr-frontend` / `routr-motion`. a11y → `web-design-guidelines`

## Handoff

- Bug found → `routr-debug`
- Deploy then verify → `routr-deploy` → this skill
