---
name: routr-deploy
description: "Deploy to Vercel or preview environments. Use when: deploy, go live, preview URL, production release, push to Vercel. Not for: writing the code (→ routr-ship); post-deploy browser QA (→ routr-qa)."
---

# routr-deploy

**Goal:** safe deploy with working preview/production URL.

## When to activate

- Deploy, go live, preview URL, production release, push to Vercel
- Mobile EAS build/submit

## Do not activate

- Writing the code or fix itself → `routr-ship`
- Post-deploy browser QA → `routr-qa`

## Iron law

**Never deploy without the pre-deploy gate passing — tests, build, env vars, migrations.**

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

## Output format

```markdown
## Deploy report
**Target:** preview / production
**URL:** …
**Pre-deploy gate:** tests / build / env vars / migrations — pass/fail
**Verified:** smoke-tested yes/no
```

## Handoff

- Deploy broke prod → `routr-debug`
- Browser verification → `routr-qa`

## References

- [boundaries](./references/boundaries.md)

## Anti-patterns

- Deploy without build check
- Force-push main to fix deploy
- Skipping env var parity preview ↔ production
