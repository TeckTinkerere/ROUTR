# Skill catalog — dependencies for playbooks

Install globally (recommended):

```bash
npx skills add <source> -g -y --copy
```

Install this router pack:

```bash
npx skills add TeckTinkerere/agent-skill-routers -g --all -y --copy
```

---

## Code intelligence & context

| Skill | Source | Playbooks |
|-------|--------|-----------|
| `symdex-code-search` | `husnainpk/SymDex` | debug, fix, explore, frontend |
| `lean-ctx` | `yvgude/lean-ctx` | debug, fix, explore, frontend |
| `find-docs` | `upstash/context7` | library, frontend |
| `caveman` | `JuliusBrussee/caveman` | debug (lite), fix-ship |
| `caveman-commit` | `JuliusBrussee/caveman` | fix-ship |
| `caveman-review` | `JuliusBrussee/caveman` | fix-ship |

## Frontend — visual design

| Skill | Source | Playbooks |
|-------|--------|-----------|
| `frontend-design` | `anthropics/skills@frontend-design` | frontend-feature |
| `ui-ux-pro-max` | `nextlevelbuilder/ui-ux-pro-max-skill` | frontend-feature |
| `tailwind-design-system` | `wshobson/agents@tailwind-design-system` | frontend-feature |
| `shadcn` | `shadcn/ui@shadcn` | frontend-feature |

## Frontend — motion & animation

| Skill | Source | Playbooks |
|-------|--------|-----------|
| `framer-motion-animator` | `patricio0312rev/skills` | frontend-feature, frontend-motion |
| `review-animations` | `emilkowalski/skills` | frontend-motion |
| `motion-design` | `lottiefiles/motion-design-skill` | frontend-motion |
| `ui-animation` | `mblode/agent-skills` | frontend-motion |
| `gsap-framer-scroll-animation` | `github/awesome-copilot` | frontend-motion (scroll-heavy) |

> **Motion.dev / Framer Motion:** use `framer-motion-animator` for React `motion` components; pair with `review-animations` before shipping.

## Agent architecture

| Skill | Source | Playbooks |
|-------|--------|-----------|
| `context-fundamentals` | `muratcankoylan/Agent-Skills-for-Context-Engineering` | agent-design |
| `context-degradation` | same repo | debug, agent-design |
| `context-compression` | same repo | agent-design |
| `multi-agent-patterns` | same repo | agent-design |
| `harness-engineering` | same repo | agent-design |
| `evaluation` | same repo | agent-design |
| `tool-design` | same repo | agent-design |

Install full context-engineering set:

```bash
npx skills add muratcankoylan/Agent-Skills-for-Context-Engineering -g --all --full-depth -y --copy
```

## Optional quality gates

| Skill | Source | When |
|-------|--------|------|
| `react-best-practices` | `vercel-labs/agent-skills` | React / Next.js frontend |
| `webapp-testing` | `anthropics/skills` or project skill | fix-ship verification |
