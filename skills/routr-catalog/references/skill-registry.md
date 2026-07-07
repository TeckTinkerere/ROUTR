# Skill registry — dependencies for routr-* routers

Install globally:

```bash
npx skills add <source> -g -y --copy
```

Install ROUTR routers:

```bash
npx skills add TeckTinkerere/ROUTR -g --all -y --copy
```

## Install bundles

ROUTR routers are indexes — install child bundles for depth.

### routr-bundle-core (daily coding)

```bash
npx skills add obra/superpowers -g --skill systematic-debugging --skill test-driven-development --skill brainstorming --skill requesting-code-review -y --copy
npx skills add husnainpk/SymDex -g -y --copy
npx skills add yvgude/lean-ctx -g -y --copy
npx skills add JuliusBrussee/caveman -g --skill caveman-commit -y --copy
```

Covers: `routr-debug`, `routr-ship`, `routr-explore`, `routr-plan`, `routr-review`

### routr-bundle-frontend (UI work)

```bash
npx skills add anthropics/skills@frontend-design anthropics/skills@web-design-guidelines -g -y --copy
npx skills add vercel-labs/agent-skills -g --skill vercel-react-best-practices --skill web-design-guidelines -y --copy
npx skills add shadcn/ui -g --skill shadcn -y --copy
npx skills add patricio0312rev/skills -g --skill framer-motion-animator -y --copy
```

Covers: `routr-frontend`, `routr-motion`

### routr-bundle-full (power users)

```bash
# Discovery & docs
npx skills add vercel-labs/skills@find-skills upstash/context7 -g -y --copy
# Vercel engineering
npx skills add vercel-labs/agent-skills -g --skill vercel-react-best-practices --skill web-design-guidelines --skill deploy-to-vercel --skill vercel-composition-patterns -y --copy
npx skills add vercel-labs/agent-browser -g -y --copy
# Anthropic
npx skills add anthropics/skills@frontend-design anthropics/skills@webapp-testing -g -y --copy
# Obra Superpowers
npx skills add obra/superpowers -g --skill systematic-debugging --skill test-driven-development --skill brainstorming --skill requesting-code-review --skill receiving-code-review -y --copy
# Matt Pocock
npx skills add mattpocock/skills -g --skill tdd --skill to-prd --skill grill-me --skill improve-codebase-architecture --skill diagnosing-bugs -y --copy
# Database
npx skills add supabase/agent-skills -g --all -y --copy
# Playwright
npx skills add microsoft/playwright-cli@playwright-cli currents-dev/playwright-best-practices-skill -g -y --copy
# Code intelligence
npx skills add husnainpk/SymDex yvgude/lean-ctx -g -y --copy
```

---

## Registry format

| Column | Meaning |
|--------|---------|
| **canonical** | Name routers use in bootstrap tables |
| **aliases** | Alternate names — do not use in router bodies |
| **namespace** | Logical group |
| **tier** | required / recommended / optional |
| **routers** | Which `routr-*` skills reference this |

---

## Code intelligence & context

| canonical | aliases | namespace | tier | routers | source |
|-----------|---------|-----------|------|---------|--------|
| `find-skills` | — | vercel | optional | routr-plan | vercel-labs/skills |
| `symdex-code-search` | symdex | routr | recommended | routr-debug, routr-ship, routr-explore, routr-frontend, routr-database, routr-refactor | husnainpk/SymDex |
| `lean-ctx` | — | routr | recommended | all code routers | yvgude/lean-ctx |
| `find-docs` | context7 | vercel | recommended | routr-integrate, routr-frontend | upstash/context7 |
| `caveman` | — | routr | optional | routr-debug | JuliusBrussee/caveman |
| `caveman-commit` | — | routr | optional | routr-ship | JuliusBrussee/caveman |
| `caveman-review` | — | routr | optional | routr-review | JuliusBrussee/caveman |

## Debugging & quality

| canonical | aliases | namespace | tier | routers | source |
|-----------|---------|-----------|------|---------|--------|
| `systematic-debugging` | debug-core, obra-debugging | obra | required | routr-debug | obra/superpowers |
| `test-driven-development` | tdd-obra | obra | recommended | routr-test, routr-ship | obra/superpowers |
| `diagnosing-bugs` | — | mattpocock | recommended | routr-debug | mattpocock/skills |
| `finishing-a-development-branch` | — | obra | optional | routr-ship, routr-deploy | obra/superpowers |
| `executing-plans` | — | obra | optional | routr-plan | obra/superpowers |

**ROUTR fallback:** `routr-depth-debug` when `systematic-debugging` missing. Agent-loop skills (`subagent-driven-development` et al.) live in [Agent & loop engineering](#agent--loop-engineering).

## Planning & specs

| canonical | aliases | namespace | tier | routers | source |
|-----------|---------|-----------|------|---------|--------|
| `brainstorming` | — | obra | required | routr-plan | obra/superpowers |
| `to-prd` | — | mattpocock | recommended | routr-plan | mattpocock/skills |
| `grill-me` | grilling, grill | mattpocock | recommended | routr-plan | mattpocock/skills |
| `grill-with-docs` | — | mattpocock | optional | routr-plan | mattpocock/skills |
| `improve-codebase-architecture` | — | mattpocock | optional | routr-plan, routr-refactor | mattpocock/skills |

**ROUTR fallback:** `routr-depth-plan` when `brainstorming` missing.

## Testing & E2E

| canonical | aliases | namespace | tier | routers | source |
|-----------|---------|-----------|------|---------|--------|
| `webapp-testing` | — | anthropic | recommended | routr-test, routr-qa | anthropics/skills |
| `tdd` | — | mattpocock | recommended | routr-test | mattpocock/skills |
| `playwright-cli` | — | microsoft | optional | routr-test, routr-qa | microsoft/playwright-cli |
| `playwright-best-practices` | — | currents | optional | routr-test, routr-qa | currents-dev/playwright-best-practices-skill |
| `agent-browser` | — | vercel | recommended | routr-qa | vercel-labs/agent-browser |

**ROUTR fallback:** `routr-depth-test` when `webapp-testing` missing.

## Code review

| canonical | aliases | namespace | tier | routers | source |
|-----------|---------|-----------|------|---------|--------|
| `requesting-code-review` | — | obra | recommended | routr-review, routr-ship | obra/superpowers |
| `receiving-code-review` | — | obra | optional | routr-review | obra/superpowers |
| `code-review-excellence` | — | wshobson | optional | routr-review | wshobson/agents |
| `review-since` | — | mattpocock | optional | routr-review | mattpocock/skills |
| `vercel-react-best-practices` | — | vercel | recommended | routr-review, routr-refactor, routr-frontend | vercel-labs/agent-skills |
| `vercel-composition-patterns` | — | vercel | optional | routr-refactor, routr-frontend | vercel-labs/agent-skills |

## Deploy

| canonical | aliases | namespace | tier | routers | source |
|-----------|---------|-----------|------|---------|--------|
| `deploy-to-vercel` | — | vercel | required | routr-deploy | vercel-labs/agent-skills |
| `vercel-cli-with-tokens` | — | vercel | optional | routr-deploy | vercel-labs/agent-skills |
| `vercel-optimize` | — | vercel | optional | routr-deploy | vercel-labs/agent-skills |
| `expo-deployment` | — | expo | optional | routr-deploy, routr-mobile | expo/skills |

## Frontend — visual

| canonical | aliases | namespace | tier | routers | source |
|-----------|---------|-----------|------|---------|--------|
| `frontend-design` | — | anthropic | required | routr-frontend | anthropics/skills |
| `web-design-guidelines` | — | vercel | recommended | routr-frontend, routr-qa, routr-review | vercel-labs/agent-skills |
| `ui-ux-pro-max` | — | nextlevelbuilder | recommended | routr-frontend | nextlevelbuilder/ui-ux-pro-max-skill |
| `tailwind-design-system` | — | wshobson | optional | routr-frontend | wshobson/agents |
| `shadcn` | — | shadcn | optional | routr-frontend | shadcn/ui |

**ROUTR fallback:** `routr-depth-frontend` when `frontend-design` missing.

## Frontend — motion

| canonical | aliases | namespace | tier | routers | source |
|-----------|---------|-----------|------|---------|--------|
| `framer-motion-animator` | — | patricio | recommended | routr-motion, routr-frontend | patricio0312rev/skills |
| `review-animations` | — | emilkowalski | recommended | routr-motion, routr-review | emilkowalski/skills |
| `motion-design` | — | lottie | optional | routr-motion | lottiefiles/motion-design-skill |
| `ui-animation` | — | mblode | optional | routr-motion | mblode/agent-skills |
| `remotion-best-practices` | — | remotion | optional | routr-video | remotion-dev/skills |

## Database

| canonical | aliases | namespace | tier | routers | source |
|-----------|---------|-----------|------|---------|--------|
| `supabase-postgres-best-practices` | — | supabase | required | routr-database | supabase/agent-skills |
| `supabase` | — | supabase | recommended | routr-database | supabase/agent-skills |

## Security

| canonical | aliases | namespace | tier | routers | source |
|-----------|---------|-----------|------|---------|--------|
| `semgrep` | — | trailofbits | recommended | routr-security | trailofbits/skills |
| `firebase-security-rules-auditor` | — | firebase | optional | routr-security | firebase/agent-skills |

## Mobile

| canonical | aliases | namespace | tier | routers | source |
|-----------|---------|-----------|------|---------|--------|
| `building-native-ui` | — | expo | required | routr-mobile | expo/skills |
| `vercel-react-native-skills` | — | vercel | recommended | routr-mobile | vercel-labs/agent-skills |
| `native-data-fetching` | — | expo | recommended | routr-mobile | expo/skills |

## Marketing

| canonical | aliases | namespace | tier | routers | source |
|-----------|---------|-----------|------|---------|--------|
| `seo-audit` | — | marketing | recommended | routr-marketing | coreyhaines31/marketingskills |
| `copywriting` | — | marketing | recommended | routr-marketing | coreyhaines31/marketingskills |
| `ai-seo` | — | marketing | optional | routr-marketing | coreyhaines31/marketingskills |
| `aso` | — | marketing | optional | routr-marketing, routr-mobile | coreyhaines31/marketingskills |

## AI / LLM

| canonical | aliases | namespace | tier | routers | source |
|-----------|---------|-----------|------|---------|--------|
| `ai-sdk` | vercel-ai-sdk | vercel | required | routr-ai | vercel/ai |
| `migrate-ai-sdk-v6-to-v7` | — | vercel | optional | routr-ai | vercel/ai |
| `chat-sdk` | — | vercel | optional | routr-ai | vercel/chat |

## Video

Leaderboard: [video-skills-leaderboard.md](video-skills-leaderboard.md)

| canonical | aliases | namespace | tier | routers | source |
|-----------|---------|-----------|------|---------|--------|
| `brag` | — | hyperframes | required | routr-video | latent-spaces/brag |
| `remotion-best-practices` | — | remotion | required | routr-video | remotion-dev/skills |
| `hyperframes` | — | hyperframes | recommended | routr-video | heygen-com/hyperframes |
| `product-launch-video` | plv | hyperframes | optional | routr-video | heygen-com/hyperframes |
| `pr-to-video` | — | hyperframes | optional | routr-video | heygen-com/hyperframes |

## Agent & loop engineering

The **operating loop** (research loops, self-correction, eval gates, trace debugging) is a fast-growing skill area. All ship in one collection — install once, route per symptom via `routr-agents`.

### Context engineering

| canonical | aliases | namespace | tier | routers | source |
|-----------|---------|-----------|------|---------|--------|
| `context-fundamentals` | — | context-eng | optional | routr-agents | muratcankoylan/Agent-Skills-for-Context-Engineering |
| `context-degradation` | — | context-eng | optional | routr-debug, routr-agents | same |
| `context-optimization` | — | context-eng | optional | routr-agents | same |
| `context-compression` | — | context-eng | optional | routr-agents | same |
| `filesystem-context` | — | context-eng | optional | routr-agents | same |
| `memory-systems` | — | context-eng | optional | routr-agents | same |
| `tool-design` | — | context-eng | optional | routr-agents | same |

### Loop engineering

| canonical | aliases | namespace | tier | routers | source |
|-----------|---------|-----------|------|---------|--------|
| `harness-engineering` | — | context-eng | recommended | routr-agents | muratcankoylan/Agent-Skills-for-Context-Engineering |
| `comprehensive-research-agent` | — | context-eng | recommended | routr-agents | same |
| `reasoning-trace-optimizer` | — | context-eng | recommended | routr-agents, routr-debug | same |
| `multi-agent-patterns` | — | context-eng | recommended | routr-agents | same |
| `subagent-driven-development` | — | obra | optional | routr-agents | obra/superpowers |
| `evaluation` | — | context-eng | optional | routr-agents | same as harness-engineering |
| `advanced-evaluation` | — | context-eng | optional | routr-agents | same |
| `hosted-agents` | — | context-eng | optional | routr-agents | same |
| `latent-briefing` | — | context-eng | optional | routr-agents | same |

```bash
# Context + loop engineering (one collection, all skills)
npx skills add muratcankoylan/Agent-Skills-for-Context-Engineering -g --all --full-depth -y --copy
# Subagent delegation loop (Obra)
npx skills add obra/superpowers -g --skill subagent-driven-development -y --copy
```

**Route:** `routr-agents` bootstrap loads exactly one row per active symptom — never the whole cluster.

---

## Router → child quick map

| Router | Top children |
|--------|--------------|
| `routr-debug` | systematic-debugging, diagnosing-bugs, symdex, lean-ctx |
| `routr-ship` | symdex, lean-ctx, test-driven-development, caveman-commit |
| `routr-test` | test-driven-development, tdd, webapp-testing |
| `routr-review` | requesting-code-review, vercel-react-best-practices |
| `routr-plan` | brainstorming, grill-me, to-prd |
| `routr-deploy` | deploy-to-vercel |
| `routr-database` | supabase-postgres-best-practices |
| `routr-refactor` | improve-codebase-architecture, vercel-composition-patterns |
| `routr-qa` | agent-browser, playwright-best-practices |
| `routr-security` | semgrep |
| `routr-frontend` | frontend-design, web-design-guidelines, shadcn |
| `routr-motion` | framer-motion-animator, review-animations |
| `routr-mobile` | building-native-ui, vercel-react-native-skills |
| `routr-marketing` | seo-audit, copywriting, ai-seo |
| `routr-ai` | ai-sdk, find-docs |
| `routr-video` | brag, remotion-best-practices, hyperframes |
| `routr-explore` | symdex, lean-ctx |
| `routr-integrate` | find-docs, symdex |
| `routr-agents` | harness-engineering, comprehensive-research-agent, reasoning-trace-optimizer, multi-agent-patterns |

## Legacy catalog

Deprecated filename `skill-catalog.md` — use this file (`skill-registry.md`).
