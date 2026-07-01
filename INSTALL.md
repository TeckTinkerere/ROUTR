# Install — Agent Skill Routers

The **slash-command hover text** in Cursor, Claude Code, Codex, and other agents comes from each skill’s `description` field in `SKILL.md`. This repo keeps those descriptions short and plain.

## Requirements

- **Node.js 18+** ([nodejs.org](https://nodejs.org))
- **Git** (optional; `npx skills` clones from GitHub)
- Internet access for first install

Check Node:

```powershell
node -v
```

```bash
node -v
```

---

## Install playbooks (all platforms)

### Windows — PowerShell

```powershell
npx skills add TeckTinkerere/agent-skill-routers -g --all -y --copy
```

### macOS / Linux — Bash or Zsh

```bash
npx skills add TeckTinkerere/agent-skill-routers -g --all -y --copy
```

| Flag | Meaning |
|------|---------|
| `-g` / `--global` | Install for your user (all projects) |
| `--all` | Install every playbook in this repo |
| `-y` | No confirmation prompts |
| `--copy` | Copy files (recommended on Windows; avoids symlink issues) |

**Restart your agent app** after install so the slash menu refreshes.

---

## Install famous child skills (optional)

Playbooks **route** to other skills; they do not bundle them. Install the starter pack once:

### Windows (PowerShell)

```powershell
npx skills add vercel-labs/agent-browser anthropics/skills@webapp-testing obra/superpowers -g --all -y --copy
npx skills add vercel-labs/agent-skills supabase/agent-skills mattpocock/skills -g --all -y --copy
npx skills add husnainpk/SymDex yvgude/lean-ctx upstash/context7 JuliusBrussee/caveman -g --all -y --copy
npx skills add anthropics/skills@frontend-design shadcn/ui@shadcn -g -y --copy
```

### macOS / Linux

```bash
npx skills add vercel-labs/agent-browser anthropics/skills@webapp-testing obra/superpowers -g --all -y --copy
npx skills add vercel-labs/agent-skills supabase/agent-skills mattpocock/skills -g --all -y --copy
npx skills add husnainpk/SymDex yvgude/lean-ctx upstash/context7 JuliusBrussee/caveman -g --all -y --copy
npx skills add anthropics/skills@frontend-design shadcn/ui@shadcn -g -y --copy
```

Full list with install counts: [`skills/playbook-common/references/skill-catalog.md`](skills/playbook-common/references/skill-catalog.md)

---

## Per-agent notes

Skills install to agent-specific folders via the [skills CLI](https://skills.sh). Global install (`-g`) targets **all supported agents** on your machine.

| Agent | Skill location (typical) | After install |
|-------|--------------------------|---------------|
| **Cursor** | `%USERPROFILE%\.agents\skills\` (Windows) or `~/.agents/skills/` | Restart Cursor. Type `/` and search playbook name. |
| **Claude Code** | `~/.claude/skills/` | Restart Claude Code. Use skill picker or `/` if enabled. |
| **Codex** | `~/.codex/skills/` or `~/.agents/skills/` | Restart Codex CLI / IDE integration. |
| **Kiro** | `~/.kiro/skills/` | Restart Kiro. |
| **OpenCode** | `~/.config/opencode/` (skills mirrored) | Restart OpenCode. |
| **Windsurf** | `~/.codeium/windsurf/skills/` | Restart Windsurf. |
| **Copilot** | VS Code user skills paths | Reload VS Code window. |

List what is installed for one agent:

```powershell
npx skills ls -g -a cursor
```

```bash
npx skills ls -g -a claude-code
```

---

## Verify install

```powershell
# Windows — should list debugging-playbook, frontend-feature-playbook, etc.
npx skills ls -g | Select-String playbook
```

```bash
# macOS / Linux
npx skills ls -g | grep playbook
```

In **Cursor**: open chat → type `/` → search `debugging-playbook`. Hover should show the one-line description from `SKILL.md`.

---

## Update playbooks

```powershell
npx skills update TeckTinkerere/agent-skill-routers -g -y
```

Or reinstall:

```powershell
npx skills add TeckTinkerere/agent-skill-routers -g --all -y --copy
```

---

## Uninstall

```powershell
npx skills remove debugging-playbook frontend-feature-playbook -g -y
```

Remove all playbooks from this repo:

```powershell
npx skills remove playbook-router debugging-playbook fix-and-ship-playbook explore-codebase-playbook library-integration-playbook agent-design-playbook frontend-feature-playbook frontend-motion-playbook planning-playbook testing-playbook code-review-playbook refactor-playbook deploy-playbook database-playbook e2e-qa-playbook security-review-playbook playbook-common -g -y
```

---

## Slash menu: what you configure

Each playbook’s hover text is the YAML `description` at the top of `skills/<name>/SKILL.md`:

```yaml
---
name: debugging-playbook
description: >
  Find and fix bugs step by step. Use when: errors, crashes, test failures, "debug this".
---
```

Edit `description` → reinstall or push to GitHub → `npx skills update` to refresh what users see on hover.

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Skill not in `/` menu | Restart agent; run install with `-g --copy` |
| Old hover text | `npx skills update <skill-name> -g` |
| `npx` not found | Install Node.js 18+; reopen terminal |
| Windows symlink errors | Always use `--copy` |
| Child skill missing at runtime | Install from [skill-catalog.md](skills/playbook-common/references/skill-catalog.md) |

---

## Project-only install (team repo)

Omit `-g` inside a project that has `skills` configured:

```bash
cd your-project
npx skills add TeckTinkerere/agent-skill-routers --all -y --copy
```

Commits `skills-lock.json` if your team uses lockfile workflow.
