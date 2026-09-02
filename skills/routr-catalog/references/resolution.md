# Skill resolution (all routr-* routers)

## Skills root

Resolve the directory that contains installed skills (first match):

| OS | Path |
|----|------|
| Windows | `%USERPROFILE%\.agents\skills` |
| macOS / Linux | `~/.agents/skills` |

Some agents mirror skills under `~/.cursor/skills`, `~/.claude/skills`, or `~/.codex/skills`. Prefer `.agents/skills` when present.

## How to load a child skill

Many hosts (Claude Code, Claude.ai, plugin marketplaces) install skills as **namespaced plugins** rather than bare folders — e.g. `vercel:shadcn`, `supabase:supabase`, `figma:figma-use`, `anthropic-skills:pptx`. A registry `canonical` name is the skill's identity, not necessarily its on-disk or invocable name. Resolve in this order, stopping at the first hit:

1. **Host invocation by canonical name** — if the current agent host exposes a skill/slash-command mechanism (e.g. a `Skill` tool or `/name`), check whether `{canonical-name}` is already listed as available. If so, invoke it directly — do not also read it off disk.
2. **Host invocation by namespaced name** — check for `{namespace}:{canonical-name}` (registry `namespace` column) in the same listing, e.g. `vercel:ai-sdk`, `supabase:supabase`. Namespace prefixes are a hint, not a guarantee — some sources publish under a different namespace than the registry's grouping label, so also scan the listing for any entry whose suffix matches `{canonical-name}`.
3. **Filesystem path** — read `{skills-root}/{canonical-name}/SKILL.md` in full (see Skills root above).
4. **Not found** — only now treat the skill as missing; proceed to "If a child skill is missing" below.

Once loaded (by any method): follow that skill's instructions for the current step only. Progressive disclosure — do not paste entire child skills into conversation.

**Do not conclude "missing" from step 3 alone.** A skill installed as a namespaced plugin will never appear at the bare filesystem path — checking only step 3 produces a false negative on an installed skill, which triggers an unnecessary reinstall or a degraded fallback the user didn't need.

## If a child skill is missing

Missing means: not found by host invocation (bare or namespaced) **and** not found on the filesystem path.

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

## Stack entry points vs workflow selectors

Some installed child skills declare themselves the default for a whole domain in their own `description` (e.g. a video or database skill claiming "read this first for any request to X"). That claim covers **which stack to use once inside the domain** — it does not cover **which `routr-*` domain applies**, and does not override the router.

- A `routr-*` router owns the **workflow selection**: which domain, which child skill, in what order, with what handoff.
- A self-declared entry-point child skill owns the **execution details** once selected: how to use that stack correctly.

Route with `routr-*` first, then hand off to the entry-point child skill for stack-specific execution. Never let a child skill's own activation language skip the router.

## Removed playbook names

Old `*-playbook` folders were removed in v2 — use the `routr-*` equivalent. Mapping: [docs/naming.md](../../../docs/naming.md).
