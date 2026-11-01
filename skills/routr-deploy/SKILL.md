---
name: routr-deploy
description: "Deploy to Vercel, preview environments, or app stores. Use when: deploy, go live, preview URL, production release, EAS submit, TestFlight; deploy-then-verify requests start here. Not for: writing the code (→ routr-ship); QA of an already-live site (→ routr-qa)."
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

| Order | Skill | Tier |
|-------|-------|------|
| 1 | `deploy-to-vercel` | required — web target (Vercel, default Next.js) |
| 2 | `expo-deployment` | required — mobile target (EAS) |
| 3 | `vercel-cli-with-tokens` | optional — CI token auth |
| 4 | `vercel-optimize` | optional — post-deploy tuning |
| 5 | `finishing-a-development-branch` | optional — merge vs PR |

**Budget gate:** read only the one target skill (row 1 or 2) for the deploy at hand. Pull `vercel-cli-with-tokens` only for CI or token auth, `vercel-optimize` only after a Vercel deploy, and `finishing-a-development-branch` only when the user asks merge vs PR.

**Skip:** `agent-browser`, `webapp-testing` (post-deploy browser QA → `routr-qa`), `systematic-debugging` (production broke → `routr-debug`), `supabase` (writing the migration → `routr-database`), `caveman-commit` (commit prep → `routr-ship`).

## 1. Pre-deploy gate

- [ ] Tests pass (`routr-test`)
- [ ] `npm run build` succeeds
- [ ] Env vars documented
- [ ] Migrations if needed (`routr-database`)

## 2. Deploy

Read `deploy-to-vercel`; capture preview URL; smoke-test.

Preview is the default target. Production deploys, alias promotion and store submission (EAS submit, TestFlight) go out only after the user approves that release in this conversation: name the target, project and commit before asking.

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
- Promoting to production because the preview looked fine, without the user's go-ahead
- Skipping env var parity preview ↔ production
