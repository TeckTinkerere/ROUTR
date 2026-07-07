# Install — ROUTR v2

> **Breaking rename (v2):** `*-playbook` → `routr-*`. Old names were removed in v2. See [docs/naming.md](docs/naming.md).

The **slash-command hover text** comes from each skill’s `description` in `SKILL.md`.

## Requirements

- **Node.js 18+** · **Git** (optional) · Internet for first install

---

## Install routers

### Interactive (recommended)

```powershell
npx skills add TeckTinkerere/ROUTR -g --copy
```

```bash
npx skills add TeckTinkerere/ROUTR -g --copy
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
npx skills add TeckTinkerere/ROUTR -g --all -y --copy
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
| **Meta** | `npx skills add TeckTinkerere/ROUTR -g --copy -y --skill routr-router --skill routr-catalog` |
| **Core** | `… --skill routr-debug --skill routr-ship --skill routr-plan --skill routr-explore` |
| **Frontend** | `… --skill routr-frontend --skill routr-motion` |
| **Video** | `… --skill routr-video` |
| **Stacks** | `… --skill routr-mobile --skill routr-marketing --skill routr-ai` |

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
npx skills add obra/superpowers -g --skill systematic-debugging --skill brainstorming -y --copy
npx skills add anthropics/skills@frontend-design -g -y --copy
npx skills add husnainpk/SymDex yvgude/lean-ctx -g -y --copy
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
| `routr-plan` | Plan, PRD, grill ideas |
| `routr-video` | Video — launch, Remotion, HyperFrames |
| `routr-ai` | AI SDK chat, agents, RAG |
| `routr-mobile` | Expo / React Native |
| `routr-marketing` | SEO, copy, growth |
| … | Full list in [README](README.md) |

Old `debugging-playbook` etc. were removed — use `routr-*`.

---

## Verify

```bash
npx skills ls -g | grep routr
```

In Cursor: `/` → search `routr-debug`.

---

## Update / uninstall

```bash
npx skills update TeckTinkerere/ROUTR -g -y
```

Remove all v2 routers:

```bash
npx skills remove routr-router routr-catalog routr-debug routr-ship routr-plan routr-test routr-review routr-refactor routr-deploy routr-database routr-qa routr-security routr-explore routr-integrate routr-agents routr-frontend routr-motion routr-mobile routr-marketing routr-ai routr-video routr-depth-debug routr-depth-frontend routr-depth-plan routr-depth-ship routr-depth-test -g -y
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

## Per-agent paths

| Agent | Typical path |
|-------|--------------|
| Cursor | `~/.agents/skills/` |
| Claude Code | `~/.claude/skills/` |
| Codex | `~/.codex/skills/` |

```bash
npx skills ls -g -a cursor
```
