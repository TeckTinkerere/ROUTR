# Changelog

All notable changes to ROUTR are documented here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html). For ROUTR, a "breaking" change is one that renames or removes a skill, or changes a router's documented contract.

## [2.1.0] - Unreleased

### Added

- **Multi-route plans.** An agent now announces the full route upfront (at most 3 steps, each with an exit condition) and re-checks it at every handoff. One router is still active at a time. See `docs/plans/2026-10-09-multi-route.md`.
- **Companions.** A second router can contribute one checklist section to the active router on a named signal, without taking over (for example `routr-security` alongside `routr-ship` when a diff touches auth).
- **`skills/routr-catalog/references/routes.json`**, the machine-readable source of truth for handoffs, companions and chains.
- **Tie-break rule.** When the domain's own machinery is failing (render pipeline, agent loop, AI SDK stream, EAS build), the domain router owns it. Application logic that merely uses the domain still goes to `routr-debug`.
- **`routr-perf`**: Core Web Vitals, bundle size, re-renders, slow APIs, N+1 queries, memory leaks, caching.
- **`routr-depth-security`**: an OWASP-style fallback (authz, injection, secrets, RLS, SSRF, dependencies), wired into the `routr-security` bootstrap.
- **Validator checks 6 to 11**: description length budget (FAIL over 320, WARN over 280), `Not for:` presence, SKILL.md line caps, broken relative links, eval JSON validity with router-name resolution, and eval coverage for every situational router.
- **`scripts/run-evals.py`** (stdlib only) with four modes: `static` (offline lexical baseline), `claude` (shells out to `claude -p`), `predictions` (score routing decisions made elsewhere) and `--export-prompts` (write the menu and prompts for a blind model run). Reports per-file accuracy, boundary failures and `must_not_load` violations, with `--json` and `--min-accuracy`.
- **Chain scoring in evals**: `acceptable_routers` and `acceptable_chains` for prompts with more than one right answer; model-facing eval menus include each router's `next` handoffs and `companions` from `routes.json`; plus chain exact-match and chain prefix-match metrics. New `evals/multi-route.eval.json`.
- **`scripts/sync-installed.sh` and `.ps1`**: report drift between this repo and installed skill folders; `--apply` copies; `--prune-legacy` moves removed `*-playbook` stubs to a dated backup folder and never deletes.
- **Evals for every router**: 153 prompts across 20 eval files, each situational router with at least 3 prompts including an adversarial boundary pair.
- **Open-source files**: `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md` (Contributor Covenant 2.1), `SECURITY.md`, issue forms (misroute, new router, bug), a pull request template, a release workflow, `.gitattributes` and `.editorconfig`.
- README: CI badge, Mermaid routing diagram, multi-route section, measured routing quality and roadmap.

### Changed

- **Validator is much faster** on Windows (about 6 seconds, down from 1m45s to 4m) by moving checks 1, 2 and 5 to 8 into `scripts/_validate_helpers.py`. Output is identical.
- Sharper router boundaries from blind-eval misses: database vs debug for wrong query results, plan vs frontend for UI sketches and multi-screen features, video vs debug for failed renders, and deploy vs mobile vs qa for EAS submit and "deploy then smoke test".
- `routr-debug` and `routr-video` descriptions trimmed under the 280-character soft budget.
- CI runs the validator and a static eval smoke test.
- `.plugin/plugin.json` bumped to 2.1.0 with corrected counts.

### Fixed

- Stale counts and version in plugin metadata and README badge.
- Installed copies silently drifting from the repo (now detectable with `sync-installed`).

### Measured

Blind Haiku 4.5 runs (a subagent that could only read the exported prompts file) scored 148/153, 144/153 and then 152/153 and 149/153 after the description fixes: **97.4 to 99.3% router accuracy and 0 `must_not_load` violations** on the final two runs. Single runs vary by about 3 points. See `docs/plans/2026-09-25-routr-v2.1.md`.

## [2.0.1] - 2026-09-05

### Added

- All 19 situational `routr-*` routers brought to the authoring spec, with a registry validator (`scripts/validate-skills.sh`).
- `routr-video` gained HeyGen, Remotion, product-marketing and data-driven configuration.

## [2.0.0] - 2026-07-03

### Changed

- **Breaking:** `*-playbook` skills renamed to `routr-*`. See `docs/naming.md`.
- Skill registry and depth fallbacks (`routr-depth-debug`, `-frontend`, `-plan`, `-ship`, `-test`) introduced for when child skills are missing.
- Router selection sharpened and `routr-router` slimmed to a decision tree (2026-07-07).

### Removed

- **Breaking:** deprecated `*-playbook` redirect stubs (2026-07-07).

### Added

- GitHub Discussions welcome template (2026-07-07).

## [1.3.0] - 2026-07-01

### Added

- Video generation playbooks (video generation, launch, Remotion) and a video skills leaderboard.
- Install path rebranded to ROUTR.
- Interactive install picker and bundle scripts.

## [1.2.0] - 2026-07-01

### Added

- Mobile (Expo / React Native), marketing and SEO, and AI / LLM app playbooks.
- README redesign with ASCII banner and stack-focused layout.

## [1.1.0] - 2026-07-01

### Added

- Seven playbooks: testing, code review, planning, deploy, database, refactor, e2e QA, plus security review.
- Skill catalog expanded with Vercel, Anthropic, Obra Superpowers, Matt Pocock, Supabase and Playwright leaderboard skills.
- `INSTALL.md` with Windows, macOS, Linux and per-agent instructions; plain-language slash-menu descriptions.

## [1.0.0] - 2026-07-01

### Added

- Initial release: situational agent skill playbooks.

[2.1.0]: https://github.com/TeckTinkerere/ROUTR/compare/v2.0.1...v2.1.0
[2.0.1]: https://github.com/TeckTinkerere/ROUTR/compare/v2.0.0...v2.0.1
[2.0.0]: https://github.com/TeckTinkerere/ROUTR/compare/v1.3.0...v2.0.0
[1.3.0]: https://github.com/TeckTinkerere/ROUTR/compare/v1.2.0...v1.3.0
[1.2.0]: https://github.com/TeckTinkerere/ROUTR/compare/v1.1.0...v1.2.0
[1.1.0]: https://github.com/TeckTinkerere/ROUTR/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/TeckTinkerere/ROUTR/releases/tag/v1.0.0
