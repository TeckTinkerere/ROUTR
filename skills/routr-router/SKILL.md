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
├─ Slow page / bundle size / high INP / leak   → routr-perf
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

Domain machinery beats generic debug: if the thing failing is a domain's *own machinery* (render pipeline, agent loop, AI SDK stream, EAS build, migration runner), that domain router owns it. Wrong *application* logic that merely uses the domain → `routr-debug`.

Tie-break by **most specific wins** — single source of truth in [routr-catalog/references/resolution.md](../routr-catalog/references/resolution.md#router-precedence). Overlap edge cases (fix-the-UI, ship-the-feature, video-vs-frontend, AI-feature): [references/decision-tree.md](./references/decision-tree.md).

## Frontend detection

Touches `.tsx`/`.jsx`/`.vue`/`.svelte`, CSS/Tailwind, layout, components, pages: build/redesign → `routr-frontend`; motion only → `routr-motion`; visual bug → `routr-debug`; post-deploy check → `routr-qa`.

## Route plans

Real requests often span routers. Plan the whole route upfront, then run it **one router at a time**. Known chains and their exit conditions live in [routes.json](../routr-catalog/references/routes.json) (source of truth) — use a matching chain entry or compose your own from each router's handoff list.

Announce before starting:

```
ROUTR plan: routr-debug → routr-ship → routr-deploy
Now: routr-debug — 500 on checkout, root cause unknown
Next: routr-ship once root cause is fixed and verified
```

- **At most 3 steps.** Anything longer: make `routr-plan` the first step, then re-plan after it.
- **Exit condition per step:** the point where you stop and hand off (e.g. "root cause fixed + verified"). A single-router task announces one line, as before.
- **Re-route at each handoff.** Re-read the plan; if the next step no longer applies, drop it. Never skip ahead or load the next router early.
- **User overrides win.** "Skip", "stop after debug", "just ship" edit the plan immediately; restate it in one line.
- Run `Next:` only after the current router's own Handoff says it is done.

### Composing a plan

Map each job the request asks for to a router (step_signals in routes.json), then order them by how the work happens:

```
plan → diagnose or build → fix + commit (routr-ship) → release (routr-deploy) → verify live (routr-qa) / promote (routr-video, routr-marketing)
```

1. **One step per distinct job asked for.** "Find the cause, fix it, get it live" is three jobs: debug → ship → deploy.
2. **Fixes go live through ship.** Never go straight from routr-debug, routr-perf or routr-security to routr-deploy.
3. **Diagnose before you polish.** perf before motion, review before ship, test before qa, plan before building.
4. **Add an unstated step only if the deliverable can't exist without it.** For example, AI chat in an app with no chat UI needs routr-frontend.
5. **Deferred work is not a step.** "We'll deploy later" means no deploy step.
6. **Companions are never steps.**

## Companions

A **companion** lends one checklist to the active router without taking the task. At most one per step, only on its named signal (pairings in routes.json, e.g. `routr-ship` + `routr-security` when the diff touches auth, RLS, secrets, or payments). Read only the section the entry names; never run its bootstrap or load its children.

## After routing

1. Load the chosen `routr-*` skill only.
2. If a child skill is missing → its `routr-depth-*` or `routr-catalog/references/resolution.md`.
3. Install child bundles from `skill-registry.md` if output feels weak.
