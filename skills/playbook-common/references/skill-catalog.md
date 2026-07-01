# Skill catalog — dependencies for playbooks

Install globally (recommended):

```bash
npx skills add <source> -g -y --copy
```

Install this router pack:

```bash
npx skills add TeckTinkerere/ROUTR -g --all -y --copy
```

## Famous skills starter pack (curated from skills.sh top installs)

One-shot install of the most adopted vendor skills (2M–100K+ installs each):

```bash
# Discovery & docs
npx skills add vercel-labs/skills@find-skills upstash/context7 -g -y --copy

# Vercel engineering (515K+ react, 428K+ web design, 499K+ browser)
npx skills add vercel-labs/agent-skills -g --skill vercel-react-best-practices -g --skill web-design-guidelines -g --skill deploy-to-vercel -g --skill vercel-composition-patterns -y --copy
npx skills add vercel-labs/agent-browser -g -y --copy

# Anthropic (610K+ frontend, 107K+ webapp testing)
npx skills add anthropics/skills@frontend-design anthropics/skills@webapp-testing -g -y --copy

# Obra Superpowers (166K+ debugging, 149K+ code review)
npx skills add obra/superpowers -g --skill systematic-debugging --skill test-driven-development --skill brainstorming --skill requesting-code-review --skill receiving-code-review -y --copy

# Matt Pocock (330K+ tdd, 350K+ architecture, 425K+ grill)
npx skills add mattpocock/skills -g --skill tdd --skill to-prd --skill grill-me --skill improve-codebase-architecture --skill diagnosing-bugs -y --copy

# Database (260K+ postgres practices)
npx skills add supabase/agent-skills -g --all -y --copy

# Playwright E2E (72K+ / 56K+)
npx skills add microsoft/playwright-cli@playwright-cli currents-dev/playwright-best-practices-skill -g -y --copy
```

---

## Code intelligence & context

| Skill | Source | Installs | Playbooks |
|-------|--------|----------|-----------|
| `find-skills` | `vercel-labs/skills` | 2.3M+ | planning |
| `symdex-code-search` | `husnainpk/SymDex` | — | debug, fix, explore, frontend, database, refactor |
| `lean-ctx` | `yvgude/lean-ctx` | — | all code playbooks |
| `find-docs` | `upstash/context7` | 8K+ | library, frontend |
| `caveman` | `JuliusBrussee/caveman` | 78K+ stars | debug (lite), fix-ship |
| `caveman-commit` | `JuliusBrussee/caveman` | — | fix-ship |
| `caveman-review` | `JuliusBrussee/caveman` | — | code-review |

## Debugging & quality (Obra Superpowers + Matt Pocock)

| Skill | Source | Installs | Playbooks |
|-------|--------|----------|-----------|
| `systematic-debugging` | `obra/superpowers` | 166K+ | debugging |
| `test-driven-development` | `obra/superpowers` | — | testing, fix-ship |
| `diagnosing-bugs` | `mattpocock/skills` | — | debugging |
| `finishing-a-development-branch` | `obra/superpowers` | — | fix-ship, deploy |
| `executing-plans` | `obra/superpowers` | — | planning (execute phase) |
| `subagent-driven-development` | `obra/superpowers` | — | agent-design |

## Planning & specs

| Skill | Source | Installs | Playbooks |
|-------|--------|----------|-----------|
| `brainstorming` | `obra/superpowers` | — | planning |
| `to-prd` | `mattpocock/skills` | 310K+ | planning |
| `grill-me` | `mattpocock/skills` | 425K+ | planning |
| `grill-with-docs` | `mattpocock/skills` | 350K+ | planning |
| `improve-codebase-architecture` | `mattpocock/skills` | 350K+ | planning, refactor |

## Testing & E2E

| Skill | Source | Installs | Playbooks |
|-------|--------|----------|-----------|
| `webapp-testing` | `anthropics/skills` | 107K+ | testing, e2e-qa |
| `tdd` | `mattpocock/skills` | 330K+ | testing |
| `playwright-cli` | `microsoft/playwright-cli` | 72K+ | testing, e2e-qa |
| `playwright-best-practices` | `currents-dev/playwright-best-practices-skill` | 56K+ | testing, e2e-qa |
| `agent-browser` | `vercel-labs/agent-browser` | 499K+ | e2e-qa |

## Code review

| Skill | Source | Installs | Playbooks |
|-------|--------|----------|-----------|
| `requesting-code-review` | `obra/superpowers` | 149K+ | code-review, fix-ship |
| `receiving-code-review` | `obra/superpowers` | 122K+ | code-review |
| `code-review-excellence` | `wshobson/agents` | 24K+ | code-review |
| `review-since` | `mattpocock/skills` | — | code-review |
| `vercel-react-best-practices` | `vercel-labs/agent-skills` | 515K+ | code-review, refactor, frontend |

## Deploy & optimize

| Skill | Source | Installs | Playbooks |
|-------|--------|----------|-----------|
| `deploy-to-vercel` | `vercel-labs/agent-skills` | 82K+ | deploy |
| `vercel-cli-with-tokens` | `vercel-labs/agent-skills` | — | deploy |
| `vercel-optimize` | `vercel-labs/agent-skills` | — | deploy |
| `expo-deployment` | `expo/skills` | 39K+ | deploy (mobile) |

## Frontend — visual design

| Skill | Source | Installs | Playbooks |
|-------|--------|----------|-----------|
| `frontend-design` | `anthropics/skills` | 610K+ | frontend-feature |
| `web-design-guidelines` | `vercel-labs/agent-skills` | 428K+ | frontend-feature, e2e-qa, code-review |
| `ui-ux-pro-max` | `nextlevelbuilder/ui-ux-pro-max-skill` | 243K+ | frontend-feature |
| `tailwind-design-system` | `wshobson/agents` | 52K+ | frontend-feature |
| `shadcn` | `shadcn/ui` | 214K+ | frontend-feature |
| `vercel-react-view-transitions` | `vercel-labs/agent-skills` | — | frontend-motion |
| `design-taste-frontend` | `leonxlnx/taste-skill` | 202K+ | frontend-feature (alt aesthetic) |

## Frontend — motion & animation

| Skill | Source | Installs | Playbooks |
|-------|--------|----------|-----------|
| `framer-motion-animator` | `patricio0312rev/skills` | 7K+ | frontend-feature, frontend-motion |
| `review-animations` | `emilkowalski/skills` | 12K+ | frontend-motion, code-review |
| `motion-design` | `lottiefiles/motion-design-skill` | 3.6K+ | frontend-motion |
| `ui-animation` | `mblode/agent-skills` | 6.6K+ | frontend-motion |
| `remotion-best-practices` | `remotion-dev/skills` | 401K+ | frontend-motion (video) |

## Refactor & architecture

| Skill | Source | Installs | Playbooks |
|-------|--------|----------|-----------|
| `vercel-composition-patterns` | `vercel-labs/agent-skills` | — | refactor |
| `codebase-design` | `mattpocock/skills` | — | refactor |
| `nextjs-app-router-patterns` | `wshobson/agents` | 23K+ | frontend-feature, library |

## Database

| Skill | Source | Installs | Playbooks |
|-------|--------|----------|-----------|
| `supabase-postgres-best-practices` | `supabase/agent-skills` | 260K+ | database |
| `supabase` | `supabase/agent-skills` | 146K+ | database |

## Security

| Skill | Source | Installs | Playbooks |
|-------|--------|----------|-----------|
| `semgrep` | `trailofbits/skills` | 5.6K+ | security-review |
| `firebase-security-rules-auditor` | `firebase/agent-skills` | 59K+ | security-review |

## Mobile — Expo & React Native

| Skill | Source | Installs | Playbooks |
|-------|--------|----------|-----------|
| `building-native-ui` | `expo/skills` | 57K+ | mobile-expo |
| `vercel-react-native-skills` | `vercel-labs/agent-skills` | 155K+ | mobile-expo |
| `native-data-fetching` | `expo/skills` | 45K+ | mobile-expo |
| `expo-tailwind-setup` | `expo/skills` | 40K+ | mobile-expo |
| `expo-deployment` | `expo/skills` | 39K+ | mobile-expo, deploy |
| `react-native-best-practices` | `callstackincubator/agent-skills` | 19K+ | mobile-expo |
| `react-native-design` | `wshobson/agents` | 11K+ | mobile-expo |

```bash
npx skills add expo/skills -g --skill building-native-ui --skill native-data-fetching --skill expo-deployment -y --copy
npx skills add vercel-labs/agent-skills@vercel-react-native-skills callstackincubator/agent-skills@react-native-best-practices -g -y --copy
```

## Marketing & SEO

| Skill | Source | Installs | Playbooks |
|-------|--------|----------|-----------|
| `seo-audit` | `coreyhaines31/marketingskills` | 150K+ | marketing-seo |
| `copywriting` | `coreyhaines31/marketingskills` | 140K+ | marketing-seo |
| `marketing-psychology` | `coreyhaines31/marketingskills` | 103K+ | marketing-seo |
| `programmatic-seo` | `coreyhaines31/marketingskills` | 95K+ | marketing-seo |
| `ai-seo` | `coreyhaines31/marketingskills` | 82K+ | marketing-seo |
| `aso` | `coreyhaines31/marketingskills` | — | marketing-seo, mobile-expo |
| `ad-creative` | `coreyhaines31/marketingskills` | — | marketing-seo |
| `analytics` | `coreyhaines31/marketingskills` | — | marketing-seo |

```bash
npx skills add coreyhaines31/marketingskills -g --all -y --copy
```

## AI / LLM applications

| Skill | Source | Installs | Playbooks |
|-------|--------|----------|-----------|
| `ai-sdk` | `vercel/ai` | 37K+ | ai-llm-app |
| `migrate-ai-sdk-v6-to-v7` | `vercel/ai` | — | ai-llm-app |
| `chat-sdk` | `vercel/chat` | 4K+ | ai-llm-app (chat UI) |

```bash
npx skills add vercel/ai -g --all -y --copy
```

## Video generation

Leaderboard and routing notes: [video-skills-leaderboard.md](video-skills-leaderboard.md)

| Skill | Source | Installs | Playbooks |
|-------|--------|----------|-----------|
| `remotion-best-practices` | `remotion-dev/skills` | 401K+ | video-remotion |
| `brag` | `latent-spaces/brag` | 61+ · 716★ | video-launch |
| `hyperframes` | `heygen-com/hyperframes` | bundle | video-generation, video-launch |
| `product-launch-video` | `heygen-com/hyperframes` | bundle | video-launch |
| `pr-to-video` | `heygen-com/hyperframes` | bundle | video-launch |
| `website-to-video` | `heygen-com/hyperframes` | bundle | video-launch |
| `faceless-explainer` | `heygen-com/hyperframes` | bundle | video-launch |
| `motion-graphics` | `heygen-com/hyperframes` | bundle | video-launch |
| `embedded-captions` | `heygen-com/hyperframes` | bundle | video-launch |
| `remotion-video-toolkit` | `shreefentsar/remotion-video-toolkit` | 671 | video-remotion (fallback) |

```bash
npx skills add remotion-dev/skills@remotion-best-practices latent-spaces/brag@brag -g -y --copy
npx skills add heygen-com/hyperframes -g --all -y --copy
```

## Agent architecture

| Skill | Source | Playbooks |
|-------|--------|-----------|
| `context-fundamentals` | `muratcankoylan/Agent-Skills-for-Context-Engineering` | agent-design |
| `context-degradation` | same repo | debug, agent-design |
| `harness-engineering` | same repo | agent-design |
| `multi-agent-patterns` | same repo | agent-design |

```bash
npx skills add muratcankoylan/Agent-Skills-for-Context-Engineering -g --all --full-depth -y --copy
```

---

## Playbook → skill quick map

| Playbook | Top child skills |
|----------|------------------|
| `debugging-playbook` | systematic-debugging, diagnosing-bugs, symdex, lean-ctx |
| `fix-and-ship-playbook` | symdex, lean-ctx, test-driven-development, caveman-commit |
| `testing-playbook` | test-driven-development, tdd, webapp-testing, playwright-* |
| `code-review-playbook` | requesting-code-review, vercel-react-best-practices |
| `planning-playbook` | brainstorming, grill-me, to-prd |
| `deploy-playbook` | deploy-to-vercel, vercel-optimize |
| `database-playbook` | supabase-postgres-best-practices, supabase |
| `refactor-playbook` | improve-codebase-architecture, vercel-composition-patterns |
| `e2e-qa-playbook` | agent-browser, playwright-best-practices |
| `security-review-playbook` | semgrep, firebase-security-rules-auditor |
| `frontend-feature-playbook` | frontend-design, web-design-guidelines, shadcn |
| `frontend-motion-playbook` | framer-motion-animator, review-animations |
| `mobile-expo-playbook` | building-native-ui, vercel-react-native-skills |
| `marketing-seo-playbook` | seo-audit, copywriting, ai-seo |
| `ai-llm-app-playbook` | ai-sdk, find-docs, agent-design |
| `video-generation-playbook` | hyperframes, brag, remotion-best-practices |
| `video-launch-playbook` | brag, product-launch-video, pr-to-video |
| `video-remotion-playbook` | remotion-best-practices |
