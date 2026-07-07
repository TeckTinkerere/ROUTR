---
name: routr-router
description: "Pick the right ROUTR workflow when the task is unclear. Use when: not sure which skill, 'what approach', multiple tasks apply, 'help me with this', starting a new task, or user didn't name a specific router."
---

# routr-router

Pick **one** `routr-*` skill, announce it in one line, then read and follow that skill's `SKILL.md` exclusively.

> Most tasks route from the slash-menu `description` alone — each router now carries `Use when:` **and** `Not for:` boundaries. Only load this file when genuinely ambiguous.

## When to activate

- User intent spans multiple domains
- No clear match to a single router
- User asks "what should we do first?"

## Do not activate

- Intent already clear — load the specific `routr-*` directly (its `description` already disambiguates)

## Iron law

**One router at a time — never load unrelated `routr-*` skills in parallel.**

## Decision tree

```
User intent?
├─ Plan / spec / PRD / grill idea              → routr-plan
├─ Bug / error / crash / root cause            → routr-debug
├─ Fix + verify + commit (known change)        → routr-ship
├─ Write tests / TDD / Playwright              → routr-test
├─ Review PR / code review                     → routr-review
├─ Security audit / vuln                       → routr-security
├─ Refactor / tech debt                        → routr-refactor
├─ Deploy / Vercel / go live                   → routr-deploy
├─ SQL / Supabase / migrations                 → routr-database
├─ Browser QA / smoke test                     → routr-qa
├─ How does X work? / onboard                  → routr-explore
├─ Library API / SDK setup                     → routr-integrate
├─ Build agent / multi-agent / context / loop  → routr-agents
├─ AI chatbot / LLM / RAG / AI SDK             → routr-ai
├─ Expo / React Native                         → routr-mobile
├─ Marketing / SEO / landing copy              → routr-marketing
├─ Video / promo / /brag / Remotion            → routr-video
├─ New UI / page / component / redesign        → routr-frontend
└─ Animate / motion / scroll (UI exists)       → routr-motion
```

Tie-break by **most specific wins** — single source of truth in [routr-catalog/references/resolution.md](../routr-catalog/references/resolution.md#router-precedence). Overlap edge cases (fix-the-UI, ship-the-feature, video-vs-frontend, AI-feature): [references/decision-tree.md](./references/decision-tree.md).

## Frontend detection

Touches `.tsx`/`.jsx`/`.vue`/`.svelte`, CSS/Tailwind, layout, components, pages: build/redesign → `routr-frontend`; motion only → `routr-motion`; visual bug → `routr-debug`; post-deploy check → `routr-qa`.

## Multi-router chains

Run **sequentially** — finish one, then re-route for the next (see each router's Handoff):

| User goal | Chain |
|-----------|-------|
| New feature end-to-end | `routr-plan` → `routr-frontend` → `routr-ship` |
| AI chat product | `routr-plan` → `routr-ai` → `routr-frontend` → `routr-ship` |
| Ship + brag video | `routr-ship` → `routr-video` → `routr-marketing` |
| Expo app + store listing | `routr-mobile` → `routr-marketing` → `routr-deploy` |
| Fix bug in production | `routr-debug` → `routr-ship` → `routr-deploy` |
| Deploy + verify | `routr-deploy` → `routr-qa` |

## After routing

1. Load the chosen `routr-*` skill only.
2. If a child skill is missing → its `routr-depth-*` or `routr-catalog/references/resolution.md`.
3. Install child bundles from `skill-registry.md` if output feels weak.
