# ROUTR naming taxonomy

Authoritative naming rules for all skills in this repository.

## ROUTR-owned skills

| Rule | Pattern | Example |
|------|---------|---------|
| Situational routers | `routr-{domain}` | `routr-debug` |
| Meta router | `routr-router` | Pick workflow when unclear |
| Dependency catalog | `routr-catalog` | Install commands, registry |
| Native depth fallbacks | `routr-depth-{domain}` | When child skill not installed |
| Folder name | **Must equal** `name` in YAML frontmatter | Agent Skills spec |

All ROUTR skills use the `routr-` prefix. No `*-playbook` suffix on new skills.

## Child skills (external)

Upstream skills keep their published names. ROUTR maps them in [`skill-registry.md`](../skills/routr-catalog/references/skill-registry.md):

- **canonical** — the name routers reference in bootstrap tables
- **aliases** — alternate names agents may encounter (e.g. `grilling` → `grill-me`)
- **tier** — `required` | `recommended` | `optional`
- **namespace** — logical grouping (`obra`, `vercel`, `anthropic`, `hyperframes`)

Do not rename upstream skills (`brag`, `caveman`, `frontend-design`).

## Namespace prefixes (catalog grouping)

| Namespace | Examples | Source |
|-----------|----------|--------|
| `obra` | `systematic-debugging`, `brainstorming` | obra/superpowers |
| `vercel` | `vercel-react-best-practices`, `ai-sdk` | vercel-labs, vercel/ai |
| `anthropic` | `frontend-design`, `webapp-testing` | anthropics/skills |
| `hyperframes` | `hyperframes-core`, `brag` | heygen-com/hyperframes, latent-spaces |
| `routr` | all `routr-*` skills | this repo |

## Rename map (v2)

| Deprecated name | Current name |
|-----------------|--------------|
| `playbook-router` | `routr-router` |
| `playbook-common` | `routr-catalog` |
| `planning-playbook` | `routr-plan` |
| `debugging-playbook` | `routr-debug` |
| `fix-and-ship-playbook` | `routr-ship` |
| `testing-playbook` | `routr-test` |
| `code-review-playbook` | `routr-review` |
| `security-review-playbook` | `routr-security` |
| `refactor-playbook` | `routr-refactor` |
| `deploy-playbook` | `routr-deploy` |
| `database-playbook` | `routr-database` |
| `e2e-qa-playbook` | `routr-qa` |
| `explore-codebase-playbook` | `routr-explore` |
| `library-integration-playbook` | `routr-integrate` |
| `agent-design-playbook` | `routr-agents` |
| `frontend-feature-playbook` | `routr-frontend` |
| `frontend-motion-playbook` | `routr-motion` |
| `mobile-expo-playbook` | `routr-mobile` |
| `marketing-seo-playbook` | `routr-marketing` |
| `ai-llm-app-playbook` | `routr-ai` |
| `video-generation-playbook` | `routr-video` |
| `video-launch-playbook` | `routr-video` (see `references/launch.md`) |
| `video-remotion-playbook` | `routr-video` (see `references/remotion.md`) |

Old `*-playbook` folders were removed in v2. The map above is kept for migration reference.

## Description format

Third person. **WHAT** + **Use when:** triggers. Pushy — include phrases users say without naming the skill.

```yaml
description: "Find and fix bugs step by step. Use when: errors, crashes, test failures, 'debug this', 'why is this broken', root cause."
```

## Adding a new router

1. Name: `routr-{domain}` (check this table for collisions)
2. Register in `routr-router` decision tree
3. Add row to `skill-registry.md`
4. Add `references/boundaries.md` if overlap with siblings is likely
5. See [authoring.md](authoring.md)
