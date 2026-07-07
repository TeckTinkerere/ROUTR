# Skill resolution (all routr-* routers)

## Skills root

Resolve the directory that contains installed skills (first match):

| OS | Path |
|----|------|
| Windows | `%USERPROFILE%\.agents\skills` |
| macOS / Linux | `~/.agents/skills` |

Some agents mirror skills under `~/.cursor/skills`, `~/.claude/skills`, or `~/.codex/skills`. Prefer `.agents/skills` when present.

## How to load a child skill

1. Read `{skills-root}/{canonical-name}/SKILL.md` in full.
2. Follow that skill's instructions for the current step only.
3. Progressive disclosure — do not paste entire child skills into conversation.

## If a child skill is missing

1. Open [skill-registry.md](skill-registry.md)
2. Run install command for that skill or a bundle
3. If still missing → router's `routr-depth-*` or `references/fallback.md`

## Router precedence

When multiple `routr-*` skills could apply, use the **most specific** match:

1. `routr-motion` — motion / animation polish only
2. `routr-frontend` — new UI, pages, components
3. `routr-debug` — bugs, errors, failures
4. `routr-ship` — fix + verify + commit
5. `routr-integrate` — third-party library API
6. `routr-explore` — understand architecture
7. `routr-agents` — agent systems
8. `routr-plan` — specs and PRDs
9. `routr-test` — TDD and Playwright
10. `routr-review` — PR review
11. `routr-deploy` — Vercel and shipping
12. `routr-database` — Postgres / Supabase
13. `routr-refactor` — structure without behavior change
14. `routr-qa` — browser QA
15. `routr-security` — security pass
16. `routr-mobile` — Expo / React Native
17. `routr-marketing` — SEO, copy
18. `routr-ai` — AI SDK apps
19. `routr-video` — all video workflows

When unsure, read `routr-router/SKILL.md` first.

## Removed playbook names

Old `*-playbook` folders were removed in v2 — use the `routr-*` equivalent. Mapping: [docs/naming.md](../../../docs/naming.md).
