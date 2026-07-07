---
name: routr-deploy
description: "Deploy to Vercel or preview environments. Use when: deploy, go live, preview URL, production release, push to Vercel. Not for: writing the code (→ routr-ship); post-deploy browser QA (→ routr-qa)."
---

# routr-deploy

**Goal:** safe deploy with working preview/production URL.

## 0. Bootstrap

| Skill | When |
|-------|------|
| `deploy-to-vercel` | Vercel (default Next.js) |
| `vercel-cli-with-tokens` | CI token auth |
| `vercel-optimize` | Post-deploy tuning |
| `finishing-a-development-branch` | Merge vs PR |
| `expo-deployment` | Mobile EAS |

## 1. Pre-deploy gate

- [ ] Tests pass (`routr-test`)
- [ ] `npm run build` succeeds
- [ ] Env vars documented
- [ ] Migrations if needed (`routr-database`)

## 2. Deploy

Read `deploy-to-vercel`; capture preview URL; smoke-test.

## 3. Post-deploy

- `vercel-optimize` for cost/CWV
- Frontend regression → `routr-qa` on preview URL

## Handoff

- Deploy broke prod → `routr-debug`
- Browser verification → `routr-qa`

## Anti-patterns

- Deploy without build check
- Force-push main to fix deploy
- Skipping env var parity preview ↔ production
