# Skill resolution (all playbooks)

## Skills root

Resolve the directory that contains installed skills (first match):

| OS | Path |
|----|------|
| Windows | `%USERPROFILE%\.agents\skills` |
| macOS / Linux | `~/.agents/skills` |

Some agents mirror skills under `~/.cursor/skills`, `~/.claude/skills`, or `~/.codex/skills`. Prefer `.agents/skills` when present.

## How to load a child skill

1. Read `{skills-root}/{skill-name}/SKILL.md` in full.
2. Follow that skill's instructions for the current step only.
3. Do not paste entire child skills into the conversation — progressive disclosure.

## If a child skill is missing

1. Open [skill-catalog.md](skill-catalog.md) in this folder.
2. Run the listed `npx skills add …` command for that skill.
3. Re-read the child `SKILL.md`, then continue the playbook.

## Playbook precedence

When multiple playbooks could apply, use the **most specific** match:

1. `frontend-motion-playbook` — motion / animation polish only
2. `frontend-feature-playbook` — new UI, pages, components, design systems
3. `debugging-playbook` — bugs, errors, failures
4. `fix-and-ship-playbook` — implement fix + verify + commit (not open-ended debug)
5. `library-integration-playbook` — third-party library API / docs
6. `explore-codebase-playbook` — understand architecture, no bug yet
7. `agent-design-playbook` — build or optimize agent systems
8. `planning-playbook` — specs and PRDs before coding
9. `testing-playbook` — TDD and Playwright
10. `code-review-playbook` — PR and diff review
11. `deploy-playbook` — Vercel and shipping
12. `database-playbook` — Postgres / Supabase
13. `refactor-playbook` — structure without behavior change
14. `e2e-qa-playbook` — browser QA and smoke tests
15. `security-review-playbook` — security pass
16. `mobile-expo-playbook` — Expo / React Native
17. `marketing-seo-playbook` — SEO, copy, growth
18. `ai-llm-app-playbook` — Vercel AI SDK apps
19. `video-remotion-playbook` — Remotion / React programmatic video
20. `video-launch-playbook` — brag, launch promo, PR video, HyperFrames workflows
21. `video-generation-playbook` — general video intent (routes to launch or Remotion)

When unsure, read `playbook-router/SKILL.md` first.
