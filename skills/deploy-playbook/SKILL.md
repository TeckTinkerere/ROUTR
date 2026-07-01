---
name: deploy-playbook
description: "Deploy to Vercel or preview environments. Use when: deploy, go live, preview URL, production release."
---

# Deploy playbook

**Goal:** safe deploy with working preview/production URL.

## 0. Bootstrap

| Skill | When |
|-------|------|
| `deploy-to-vercel` | Vercel deploy (default for Next.js/React on Vercel) |
| `vercel-cli-with-tokens` | CI/non-interactive token auth |
| `vercel-optimize` | Post-deploy cost, CWV, caching tuning |
| `finishing-a-development-branch` | Merge vs PR vs cleanup after deploy-ready |

Non-Vercel: check catalog for `expo-deployment` (mobile).

## 1. Pre-deploy gate

- [ ] Tests pass (`testing-playbook`)
- [ ] Build succeeds locally (`npm run build`)
- [ ] Env vars documented (no secrets in git)
- [ ] Migrations run if applicable (`database-playbook`)

## 2. Deploy

1. Read `deploy-to-vercel` for project-specific steps
2. Token/CI: `vercel-cli-with-tokens`
3. Capture preview URL; smoke-test critical path

## 3. Post-deploy

- `vercel-optimize` if user cares about bill, slow routes, or Core Web Vitals
- Frontend regression? → `e2e-qa-playbook` on preview URL

## Handoff

- Deploy broke prod → `debugging-playbook`
- Need browser verification → `e2e-qa-playbook`

## Anti-patterns

- Deploy without build check
- Force-push to main to "fix" deploy
- Skipping env var parity preview ↔ production
