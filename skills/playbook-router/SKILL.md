---
name: playbook-router
description: "Pick the right workflow when the task is unclear. Use when: not sure which playbook, 'what approach', or multiple tasks could apply."
---

# Playbook router

Pick **one** playbook, announce it in one line, then read and follow that playbook's `SKILL.md` exclusively.

## Decision tree

```
User intent?
├─ Plan / spec / PRD / "grill my idea"        → planning-playbook
├─ Bug / error / crash / root cause           → debugging-playbook
├─ Fix + verify + commit (scoped)             → fix-and-ship-playbook
├─ Write tests / TDD / Playwright             → testing-playbook
├─ Review PR / code review                    → code-review-playbook
├─ Security audit / vuln check                  → security-review-playbook
├─ Refactor / tech debt / architecture        → refactor-playbook
├─ Deploy / Vercel / go live                  → deploy-playbook
├─ SQL / Supabase / migrations                → database-playbook
├─ Browser QA / smoke test deployed app       → e2e-qa-playbook
├─ How does X work? / onboard                 → explore-codebase-playbook
├─ Library API / "how do I use Next…"         → library-integration-playbook
├─ Build agent / multi-agent / context        → agent-design-playbook
├─ New UI / page / component / redesign       → frontend-feature-playbook
└─ Animate / motion / scroll / transitions    → frontend-motion-playbook
```

## Frontend detection

Treat as **frontend** when the work touches: `.tsx`, `.jsx`, `.vue`, `.svelte`, CSS/Tailwind, design tokens, layout, components, pages, or the user mentions UI/UX/design.

- Building or redesigning UI → `frontend-feature-playbook`
- UI exists; motion only → `frontend-motion-playbook`
- Visual bug → `debugging-playbook`
- Post-deploy UI check → `e2e-qa-playbook`

## After routing

1. Read `playbook-common/references/resolution.md` if child skills may be missing.
2. Load the chosen playbook skill from skills root.
3. Do not load unrelated playbooks in parallel.

## Quick reference

| Playbook | Trigger words |
|----------|----------------|
| `planning-playbook` | plan, spec, PRD, brainstorm, grill |
| `debugging-playbook` | debug, trace, error, failing, broken |
| `fix-and-ship-playbook` | fix, patch, ship, commit, PR |
| `testing-playbook` | test, TDD, Playwright, coverage |
| `code-review-playbook` | review, PR feedback, diff |
| `security-review-playbook` | security, audit, vuln, RLS |
| `refactor-playbook` | refactor, clean up, tech debt |
| `deploy-playbook` | deploy, Vercel, production, preview URL |
| `database-playbook` | SQL, Postgres, Supabase, migration |
| `e2e-qa-playbook` | browser test, QA, screenshot, smoke test |
| `explore-codebase-playbook` | how does, architecture, where is |
| `library-integration-playbook` | library docs, API, configure SDK |
| `agent-design-playbook` | agent system, harness, eval |
| `frontend-feature-playbook` | build UI, landing, component |
| `frontend-motion-playbook` | animate, Framer, motion, scroll |
