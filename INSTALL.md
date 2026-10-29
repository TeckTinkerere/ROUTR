# Install — ROUTR v2

> **Breaking rename (v2):** `*-playbook` → `routr-*`. Old names were removed in v2. See [docs/naming.md](docs/naming.md).

The **slash-command hover text** comes from each skill’s `description` in `SKILL.md`.

## Requirements

- **Node.js 18+** · **Git** (optional) · Internet for first install

---

## Install routers

### Interactive (recommended)

```powershell
npx skills@1.7.4 add TeckTinkerere/ROUTR -g --copy
```

```bash
npx skills@1.7.4 add TeckTinkerere/ROUTR -g --copy
```

Use **Space** to toggle, **Enter** to confirm. On Windows use `--copy`.

### Bundle picker

```powershell
.\scripts\install-routr.ps1
```

```bash
./scripts/install-routr.sh
```

### Install all routr-* skills (no prompts)

```powershell
npx skills@1.7.4 add TeckTinkerere/ROUTR -g --all -y --copy
```

| Flag | Meaning |
|------|---------|
| `-g` | Global — all projects |
| `--all` | Every routr-* skill |
| `-y` | Skip confirmations |
| `--copy` | Copy files (Windows-safe) |
| `--skill <name>` | Specific skills only |

**Restart your agent** after install.

### Preset router bundles

| Bundle | Command |
|--------|---------|
| **Meta** | `npx skills@1.7.4 add TeckTinkerere/ROUTR -g --copy -y --skill routr-router --skill routr-catalog` |
| **Core** | `… --skill routr-debug --skill routr-ship --skill routr-plan --skill routr-spec --skill routr-explore` |
| **Frontend** | `… --skill routr-frontend --skill routr-motion` |
| **Video** | `… --skill routr-video` |
| **Stacks** | `… --skill routr-mobile --skill routr-marketing --skill routr-ai` |

For existing-product specification reconciliation, install `routr-spec` individually or use the all-skills command above:

```bash
npx skills@1.7.4 add TeckTinkerere/ROUTR -g --copy -y --skill routr-spec
```

`routr-spec` supports source-based reconciliation without REA. Its optional `reverse-engineer-anything` child is for claims that require shipped/runtime evidence; installing that child does not register or connect the REA MCP server. Consult the [skill registry](skills/routr-catalog/references/skill-registry.md) and REA's own connection contract when that evidence is needed.

---

## Install child skill bundles (required for depth)

Routers are indexes — install children for Anthropic-grade output:

| Bundle | See |
|--------|-----|
| `routr-bundle-core` | Daily coding — debug, ship, symdex, lean-ctx |
| `routr-bundle-frontend` | `frontend-design`, Vercel UI, shadcn |
| `routr-bundle-full` | Power-user starter pack |

Commands in [`skills/routr-catalog/references/skill-registry.md`](skills/routr-catalog/references/skill-registry.md).

Quick core install:

```bash
npx skills@1.7.4 add obra/superpowers -g --skill systematic-debugging --skill brainstorming -y --copy
npx skills@1.7.4 add anthropics/skills@frontend-design -g -y --copy
npx skills@1.7.4 add husnainpk/SymDex yvgude/lean-ctx -g -y --copy
```

---

## Slash menu

Search `routr-` in `/` picker:

| Router | Hover |
|--------|-------|
| `routr-router` | Pick workflow when unclear |
| `routr-debug` | Find and fix bugs step by step |
| `routr-ship` | Fix, verify, commit or PR |
| `routr-frontend` | Build or redesign UI |
| `routr-plan` | Plan future work, new-feature PRD, grill ideas |
| `routr-spec` | Reconstruct current product, reconcile specs, document drift |
| `routr-video` | Video — launch, Remotion, HyperFrames |
| `routr-ai` | AI SDK chat, agents, RAG |
| `routr-mobile` | Expo / React Native |
| `routr-marketing` | SEO, copy, growth |
| … | Full list in [README](README.md) |

Old `debugging-playbook` etc. were removed — use `routr-*`.

---

## Verify

```bash
npx skills@1.7.4 ls -g | grep routr
```

In Cursor: `/` → search `routr-debug`.

---

## Update / uninstall

```bash
npx skills@1.7.4 update TeckTinkerere/ROUTR -g -y
```

Remove all v2 routers:

```bash
npx skills@1.7.4 remove routr-router routr-catalog routr-debug routr-ship routr-plan routr-spec routr-test routr-review routr-refactor routr-deploy routr-database routr-qa routr-security routr-perf routr-explore routr-integrate routr-agents routr-frontend routr-motion routr-mobile routr-marketing routr-ai routr-video routr-depth-debug routr-depth-frontend routr-depth-plan routr-depth-ship routr-depth-test routr-depth-security -g -y
```

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Weak output | Install child bundles from skill-registry.md |
| Old playbook names | Use `routr-*` (old names removed in v2) |
| Skill not in menu | Restart agent; `-g --copy` |
| Child missing | `routr-catalog/references/skill-registry.md` |

---

## Keep installed copies in sync

Installed skill folders (`~/.claude/skills`, `~/.agents/skills`, etc.) can drift from this repo after you pull updates. Check and fix drift:

```bash
# Dry run — report what's out of date, no changes made
bash scripts/sync-installed.sh

# Apply — copy the repo's routr-* skills over the installed copies
bash scripts/sync-installed.sh --apply

# Apply + prune legacy *-playbook stubs (moved to a dated backup, never deleted)
bash scripts/sync-installed.sh --apply --prune-legacy
```

PowerShell equivalent:

```powershell
scripts\sync-installed.ps1 -Apply -PruneLegacy
```

Run this after `npx skills@1.7.4 update` or after pulling repo changes, before trusting a router's behavior matches what's in this repo.

The sync scripts only touch `routr-*` folders in the skill roots they find. Repo-only files such as `.gitattributes`, `.editorconfig`, `.github/` and `CHANGELOG.md` are for contributors and are never copied to your machine, so you can ignore them.

---

## Per-agent paths

| Agent | Typical path |
|-------|--------------|
| Cursor | `~/.agents/skills/` |
| Claude Code | `~/.claude/skills/` |
| Codex | `~/.codex/skills/` |

```bash
npx skills@1.7.4 ls -g -a cursor
```
