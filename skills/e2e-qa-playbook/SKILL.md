---
name: e2e-qa-playbook
description: >
  Browser-based QA, smoke tests, form filling, screenshots, scraping, and live
  app verification. Use when testing in a real browser, E2E QA, "open the site
  and check", dogfooding, visual regression, automating login flows, or verifying
  a deployed preview. Routes to vercel-labs agent-browser (500K+ installs),
  anthropics webapp-testing, and Playwright skills. Prefer over ad-hoc curl for
  UI flows.
---

# E2E & QA playbook

**Goal:** prove the app works in a real browser — not just unit tests.

## 0. Bootstrap

| Skill | Role |
|-------|------|
| `agent-browser` | Vercel browser CLI — navigate, click, screenshot, scrape (499K+ installs) |
| `webapp-testing` | Anthropic local web testing patterns |
| `playwright-best-practices` | Durable E2E test design |
| `playwright-cli` | Microsoft Playwright automation |

## 1. Choose mode

| Mode | When |
|------|------|
| Exploratory QA | `agent-browser` — manual journey, screenshots |
| Repeatable E2E | Playwright tests in repo |
| Post-deploy smoke | `agent-browser` on preview URL |

## 2. Exploratory (agent-browser)

1. Read `agent-browser` skill fully
2. Define checklist: login → core flow → edge case
3. Capture screenshots on failure
4. Report repro steps for bugs → `debugging-playbook`

## 3. Automated E2E

1. `playwright-best-practices` for selectors and waits
2. Add tests under project test dir
3. Run in CI — see `testing-playbook`

## 4. Frontend quality bar

Visual polish issues → `frontend-feature-playbook` or `frontend-motion-playbook`

Accessibility spot-check → `web-design-guidelines`, `ui-ux-pro-max`

## Handoff

- Bug found → `debugging-playbook`
- Deploy then verify → `deploy-playbook` then this playbook
