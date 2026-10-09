# How ROUTR routes

ROUTR keeps one rule fixed: **one router is active at a time.** What varies is how much of the route the agent plans before it starts.

- [Single route](#single-route)
- [Route plans](#route-plans)
- [Companions](#companions)
- [Tie-breaks](#tie-breaks)
- [Worked examples](#worked-examples)
- [Where this is defined](#where-this-is-defined)

## Single route

Most requests match one router from the skill's `description` alone ("fix this typo and open a PR" → `routr-ship`). The agent announces the router in one line and follows its `SKILL.md`. When it is unclear which router fits, `routr-router` decides using a decision tree and the precedence list in [resolution.md](../skills/routr-catalog/references/resolution.md#router-precedence).

## Route plans

Some requests span several routers: "fix the 500 and ship it to prod" needs debug, then ship, then deploy. The agent plans the whole route upfront and announces it:

```
ROUTR plan: routr-debug → routr-ship → routr-deploy
Now: routr-debug — 500 on checkout, root cause unknown
Next: routr-ship once root cause is fixed and verified
```

Rules:

- **One router active.** The plan is a sequence, not parallel loading.
- **At most 3 steps.** Anything longer starts with `routr-plan`, then re-plans.
- **Each step has an exit condition**, the point where the agent stops and hands off.
- **Re-route at every handoff.** The agent re-checks the next step and drops it if it no longer applies.
- **You can override at any time.** Say "skip", "stop after debug" or "just ship"; the agent restates the plan in one line.

Common plans (`prod-bugfix`, `perf-fix`, `ship-and-brag`, ...) are listed in [routes.json](../skills/routr-catalog/references/routes.json). The agent may also compose a plan from each router's `handoff` list.

### Composing a plan

The `step_signals` list in `routes.json` maps each job in a request to a router. The agent then orders the steps by how the work actually happens:

```
plan → diagnose or build → fix + commit (routr-ship) → release (routr-deploy) → verify live (routr-qa) / promote (routr-video, routr-marketing)
```

The `composition_rules` in `routes.json` add six more rules:

1. **One step per job the request asks for.** "Find the cause, fix it, get it live" is debug → ship → deploy.
2. **Fixes reach production through `routr-ship`.** Never go straight from debug, perf or security to deploy.
3. **Diagnose before you polish.** perf comes before motion, review before ship, test before qa, and plan before building.
4. **Add an unstated step only when the deliverable can't exist without it.** Example: AI chat in an app that has no chat UI yet.
5. **Deferred work is not a step.** "We'll deploy later" means no deploy step.
6. **A companion is never a step.**

Adding these rules raised chain exact-match on a held-out set from 75% to 92% (see [Measured routing quality](../README.md#measured-routing-quality)).

## Companions

A **companion** is a second router that contributes one checklist to the active router without taking over. Rules: at most one companion per step, started only by a named signal, and it reads only the section `routes.json` points at (no bootstrap, no child skills).

| Active | Companion | Signal |
|--------|-----------|--------|
| `routr-ship` | `routr-security` | diff touches auth, sessions, RLS, secrets, payments |
| `routr-frontend` | `routr-perf` | stated perf budget, LCP/INP complaint, heavy media |
| `routr-ai` | `routr-agents` | output-quality scoring or an eval harness |
| `routr-database` | `routr-security` | RLS policies, grants, multi-tenant data |
| `routr-deploy` | `routr-qa` | the user asks to verify the deployed preview |
| `routr-mobile` | `routr-perf` | jank, slow startup, list performance |

Each target skill has a short "Companion checklist" section for this purpose.

## Tie-breaks

Two rules decide most contested cases:

1. **Most specific wins** ([precedence list](../skills/routr-catalog/references/resolution.md#router-precedence)).
2. **A domain's own machinery beats generic debug.** If the thing failing is the domain itself (a render pipeline, an agent loop, an AI SDK stream, an EAS build, a migration runner), the domain router owns it and uses its own gotchas. It hands to `routr-debug` only if the root cause turns out to be outside the domain. If the failure is application logic that merely uses the domain (a query returning the wrong rows), it goes to `routr-debug`.

Some prompts legitimately start at more than one router ("build a whole new onboarding flow" can begin at `routr-plan` or `routr-frontend`). Evals record these with `acceptable_routers`, and alternative route plans with `acceptable_chains`.

## Worked examples

**1. Prompt:** "The checkout page throws a 500 in production. Find the cause, fix it, and get it live."

```
ROUTR plan: routr-debug → routr-ship → routr-deploy
Now: routr-debug — root cause unknown
Next: routr-ship once the cause is fixed and verified
```

**2. Prompt:** "Add a Supabase migration for the orders table with row level security, then ship it."

```
ROUTR plan: routr-database → routr-ship
Now: routr-database — migration + RLS (companion: routr-security checklist for the RLS policies)
Next: routr-ship once the migration is written and tested
```

**3. Prompt:** "Build a launch landing page with a hero demo video, and keep LCP under 2.5 seconds."

```
ROUTR plan: routr-frontend → routr-video
Now: routr-frontend — page build (companion: routr-perf checklist for the LCP budget)
Next: routr-video once the page needs the demo asset
```

**4. Prompt:** "My agent loop keeps drifting off task after a few tool calls."

```
ROUTR: routr-agents
```

One step. The agent loop is the domain's own machinery, so `routr-agents` owns it rather than `routr-debug`.

**5. Prompt:** "Build the Expo onboarding screens, write the App Store listing, and submit with EAS." Then, mid-task: "Skip the listing for now."

```
ROUTR plan: routr-mobile → routr-marketing → routr-deploy
Now: routr-mobile — onboarding screens

(user: "skip the listing")
ROUTR plan: routr-mobile → routr-deploy
Now: routr-mobile — onboarding screens
```

## Where this is defined

| What | File |
|------|------|
| Plan protocol, decision tree | [routr-router/SKILL.md](../skills/routr-router/SKILL.md) |
| Chains, companions, handoffs (machine-readable) | [routes.json](../skills/routr-catalog/references/routes.json) |
| Precedence and tie-break rules | [resolution.md](../skills/routr-catalog/references/resolution.md) |
| Eval format (`expected_chain`, `acceptable_routers`, `acceptable_chains`) | [evals/](../evals/) and `scripts/run-evals.py` |
| Consistency checks | `scripts/validate-skills.sh`, check 12 |
