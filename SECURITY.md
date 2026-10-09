# Security Policy

ROUTR ships **instructions that AI agents execute**, plus a few scripts that run on your machine. Both are in scope.

## What counts as a vulnerability

| In scope | Examples |
|----------|----------|
| **Prompt injection in skill text** | A `SKILL.md` or `references/` file that tells the agent to exfiltrate data, disable safety checks, fetch and run remote code, or act on content from untrusted sources without confirmation |
| **Unsafe instructions** | A router or depth fallback that steers the agent toward destructive or irreversible actions (force-push, `rm -rf`, dropping data, disabling auth) without a confirmation step |
| **Scripts touching your filesystem** | `scripts/sync-installed.*` and `scripts/install-routr.*` write to `~/.claude/skills`, `~/.agents/skills` and similar. Path traversal, writing outside those roots, deleting instead of backing up, or following symlinks out of the target are all bugs |
| **Supply chain** | Install commands in docs that point at the wrong package, or a workflow in `.github/` that could be abused (e.g. unpinned privileged actions, token exposure) |
| **Depth fallbacks** | Insecure guidance in `routr-depth-security` or the other `routr-depth-*` skills (for example, advice that weakens auth or RLS) |

Out of scope: vulnerabilities in third-party child skills (report those upstream), a model simply picking the wrong router (use the [misroute template](https://github.com/TeckTinkerere/ROUTR/issues/new?template=misroute.yml)), and issues that need an attacker who already controls your machine.

## Reporting

Use **GitHub private vulnerability reporting**:

1. Go to the [Security tab](https://github.com/TeckTinkerere/ROUTR/security) of the repository.
2. Choose **Report a vulnerability**, or open <https://github.com/TeckTinkerere/ROUTR/security/advisories/new>.
3. Include the affected file and version, how to reproduce it, and what an attacker gains.

Please do not open a public issue or discussion for a vulnerability.

What to expect from maintainers (this is a small, volunteer-run project, so these are goals, not guarantees):

- Acknowledgement within about 7 days.
- A fix or a clear explanation within about 30 days for confirmed issues.
- Credit in the changelog and advisory unless you ask to stay anonymous.

## Supported versions

| Version | Supported |
|---------|-----------|
| 2.1.x | Yes |
| 2.0.x | Security fixes only |
| 1.x | No (renamed to `routr-*` in v2; `*-playbook` skills are removed) |

## Staying safe as a user

- Review `SKILL.md` changes before pulling updates into your global skills folder.
- Run `bash scripts/sync-installed.sh` without `--apply` first. It is a dry run and shows what would change.
- `--prune-legacy` moves stubs to a dated backup folder and never deletes them.
- Treat any skill, ROUTR or otherwise, that asks the agent to run remote scripts as untrusted until you have read it.
