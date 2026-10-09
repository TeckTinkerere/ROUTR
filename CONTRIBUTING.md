# Contributing to ROUTR

Thanks for helping. ROUTR is a set of `routr-*` router skills, and its quality comes down to one thing: **does the agent pick the right router from a ~200-character description?** Most contributions are about protecting that.

By taking part you agree to the [Code of Conduct](CODE_OF_CONDUCT.md). Security problems go through [SECURITY.md](SECURITY.md), not public issues.

## Pick your path

| I want to... | Go to |
|--------------|-------|
| Report an agent picking the wrong router | [Report a misroute](#report-a-misroute) |
| Add a new router | [Add a router](#add-a-router) |
| Improve a router's description | [Improve a description](#improve-a-description) |
| Fix a script, the validator or CI | [Local setup](#local-setup), then open a PR |
| Ask a question or float an idea | [Discussions](https://github.com/TeckTinkerere/ROUTR/discussions) |

## Report a misroute

This is the most valuable contribution, and it takes two minutes.

1. Open a [misroute report](https://github.com/TeckTinkerere/ROUTR/issues/new?template=misroute.yml).
2. Give the exact prompt, the router chosen, the router expected, your agent and model, and why.
3. A maintainer (or you) turns it into an eval prompt in `evals/`, then fixes the description or the resolution rules until it passes without breaking neighbours.

Prompts that legitimately have several right answers get `acceptable_routers` (or `acceptable_chains` for route plans) instead of a forced single label.

## Add a router

Read [docs/authoring.md](docs/authoring.md) first. A router owns a **situation**, not a tool. If an existing router almost fits, improve its description instead.

Checklist:

1. Create `skills/routr-{domain}/SKILL.md` and `references/` per the authoring guide. The description needs `Use when:` and `Not for:`, and must be 320 characters or fewer (aim for 280).
2. Register it in `routr-router`'s decision tree, `skills/routr-catalog/references/resolution.md` and `skill-registry.md`.
3. Add an entry to `skills/routr-catalog/references/routes.json`: its `handoff` targets, any `companions`, and whether it `owns_domain_failures`.
4. Add `evals/routr-{domain}.eval.json` with at least 3 prompts, including one adversarial boundary pair (a prompt that looks like yours but belongs to a neighbour).
5. Run the validator and evals (below) and fix anything red.
6. Add a line to `CHANGELOG.md` under the unreleased section.

## Improve a description

Descriptions decide routing, so every change needs evidence that it did not make things worse.

```bash
# 1. Baseline before you edit (offline, free, deterministic lexical smoke test)
python scripts/run-evals.py

# 2. Edit the description, then re-run and compare
python scripts/run-evals.py
bash scripts/validate-skills.sh
```

The static mode is only a lexical check of `Use when:` and `Not for:` overlap. For a real signal use a model.

**Blind model eval (works without the `claude` CLI).** The exporter writes the router menu and prompts with no expected answers, so a model cannot cheat:

```bash
python scripts/run-evals.py --export-prompts prompts.json
# Give prompts.json to any model that sees ONLY that file.
# Ask it to answer {"<id>": "routr-xxx", ...} for every prompt, saved as preds.json
python scripts/run-evals.py --mode predictions --predictions preds.json
```

**With the Claude CLI signed in:**

```bash
python scripts/run-evals.py --mode claude --model claude-haiku-4-5-20251001
```

Rules of thumb:

- A single model run varies by about 3 points. Compare averages across two or more runs, not one.
- Zero `must_not_load` violations is the bar, not a nice-to-have.
- Never tune a description around one contested prompt. Add `acceptable_routers` / `acceptable_chains` or open a discussion.
- Paste before and after numbers in your PR.

## Local setup

You need **Git**, **Python 3** (standard library only, no `pip install`) and **Bash** (for the validator). Node.js 18+ is only needed to test installs with `npx skills`.

**macOS / Linux**

```bash
git clone https://github.com/TeckTinkerere/ROUTR.git
cd ROUTR
bash scripts/validate-skills.sh
python3 scripts/run-evals.py
```

**Windows**

Use Git for Windows (it provides Bash) or WSL:

```powershell
git clone https://github.com/TeckTinkerere/ROUTR.git
cd ROUTR
bash scripts/validate-skills.sh
python scripts/run-evals.py
```

The repo is LF-only through `.gitattributes`, except `*.ps1` files, which stay CRLF. Your editor should honour `.editorconfig`. If Git warns about line endings, do not run `git add --renormalize` as part of a feature PR.

To try your changes in a real agent, copy them into your skills folder with the sync script (dry run first):

```bash
bash scripts/sync-installed.sh            # report only
bash scripts/sync-installed.sh --apply    # copy repo routers over installed copies
```

On Windows PowerShell: `scripts\sync-installed.ps1 -Apply`.

## Commit style

We use [Conventional Commits](https://www.conventionalcommits.org/), as the history does:

```
feat(routing): sharpen router selection and add loop-engineering depth
feat: fast validator, blind model evals, sharper router boundaries
docs(discussions): add ROUTR welcome discussion template
chore(v2)!: remove deprecated *-playbook redirect stubs
```

Types: `feat`, `fix`, `docs`, `chore`, `refactor`, `test`, `ci`. Use `!` or a `BREAKING CHANGE:` footer for renames and removals. Keep the subject under about 72 characters.

## Pull request checklist

The PR template repeats this. Before you open one:

- [ ] `bash scripts/validate-skills.sh` passes with no new FAIL or WARN
- [ ] `python scripts/run-evals.py` before and after, with no regression in router accuracy
- [ ] New behaviour has eval prompts, and misroute fixes include the reported prompt
- [ ] `routes.json` updated if handoffs, companions or chains changed
- [ ] New router registered in `routr-router`, `resolution.md` and `skill-registry.md`
- [ ] `CHANGELOG.md` updated
- [ ] Conventional Commit messages
- [ ] One concern per PR

Small, focused PRs get reviewed fastest.

## Releases (maintainers)

Move the `[2.x.y] - Unreleased` heading in `CHANGELOG.md` to a dated heading, bump `.plugin/plugin.json`, then push a `vX.Y.Z` tag. The release workflow validates the repo and publishes the matching changelog section as the GitHub Release.
