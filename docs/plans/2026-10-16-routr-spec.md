# Evidence-backed product specification reconciliation

## Design and scope

`routr-spec` owns current product reality, baseline drift and a living product specification. Future intent stays with `routr-plan`; code understanding stays with `routr-explore`; code quality review and implementation stay with their existing routers. The name fits ROUTR's situational router convention without creating a new runtime or depth skill.

The router uses `symdex-code-search` and `lean-ctx` when available, with a focused source-search fallback. `to-prd` remains a planning child: as-built output has its own evidence-aware artifact contract. Optional `reverse-engineer-anything` supplies shipped/runtime investigation only when source cannot establish the claim. A sufficient source repository skips REA and its readiness checks, even when the user says "reverse engineer". Direct low-level REA tasks remain outside product-spec routing.

REA's actual skill and installation contract were inspected at upstream commit `1bd5c5c87e81b27bfb16140f71ffa03563e58477` (skill metadata version 42): [SKILL.md](https://github.com/morluto/rea/blob/1bd5c5c87e81b27bfb16140f71ffa03563e58477/.agents/skills/reverse-engineer-anything/SKILL.md), [connection/recovery](https://github.com/morluto/rea/blob/1bd5c5c87e81b27bfb16140f71ffa03563e58477/.agents/skills/reverse-engineer-anything/references/connection-and-recovery.md). Installing the skill does not register MCP or install engines; ROUTR delegates recovery to the child and does not copy setup procedures.

## Artifacts and incremental behavior

The [artifact contract](../../skills/routr-spec/references/artifacts.md) specifies six roles in an existing suitable spec directory, defaulting to `.product-spec/`: BASELINE.md, CURRENT.md, DRIFT.md, PRODUCT_CHANGELOG.md, ledger.json and manifest.json. Stable requirement/evidence/event identities connect prose to versioned evidence. A separate reason classification distinguishes OBSERVED_FACT, INFERRED_INTENT and UNKNOWN; confirmed behavior can have unknown intent.

Behavior statuses are UNVERIFIED, DORMANT, ADDED, REMOVED, MISSING, MATCH, PARTIAL and MODIFIED. MISSING avoids implying historical removal when an original requirement was never shown to have been implemented. Unknown baseline coverage prevents unsupported ADDED claims. Baseline versions and event provenance survive rebuilds; product evolution is separate from release history.

The [workflow](../../skills/routr-spec/references/workflow.md) compares the saved Git checkpoint with captured HEAD, plus baseline revisions, runtime identities, dirty overlays and requested scope. It revalidates affected areas and shared dependencies, carrying other evidence forward with its original verification scope. Widening a billing-only reconciliation to the whole product requires new coverage even at unchanged HEAD. Blocked areas retain the last completed checkpoint. Non-Git snapshots and rewritten history have explicit recovery paths.

Outgoing handoffs are deliberately limited to requested planning or implementation. Ship may hand to spec when reconciliation is explicitly requested. The opt-in plan → ship → spec chain respects the existing maximum of three steps and one active router. REA is neither a router nor a chain step.

## File inventory

| Concern | Files |
|---------|-------|
| New router | `skills/routr-spec/SKILL.md`; references: workflow, artifacts, fallback, boundaries, gotchas and examples |
| Coverage | `evals/routr-spec.eval.json`; this design/validation record |
| Routing registration | `skills/routr-router/SKILL.md`, its decision-tree reference; catalog resolution, skill registry and routes.json |
| Neighbor boundaries | plan, explore and ship descriptions; plan/explore/review/ship activation and boundary documentation; explicit ship → spec handoff |
| Discovery/install | README, INSTALL, plugin description and both router-install pickers; no release version change or REA bundle addition |
| Contributor documentation | architecture/routing docs and the unreleased CHANGELOG entry |

## Validation record

Baseline: repository commit `101192f549bb87318939c33b0dd19f0293c513e0`, clean `master`, before changing descriptions. Work is on `codex/routr-spec`. No release version bump, publication or installed-skill synchronization is part of this feature.

The suite now contains **245 prompts in 23 files: 231 routing cases and 14 behavior-only cases**. The new file contributes 32 prompts: 31 routing cases, including 3 multi-step chains and 20 explicit single-step chains, and one direct-REA case that intentionally has no `expected_router`. No acceptable alternatives were added to hide failures.

| Evaluation | Before | After | Violations before / after |
|------------|--------|-------|---------------------------|
| Static, full applicable suite | 123/200 (61.5%) | 150/231 (64.9%) | 10 / 10 |
| Static, unchanged original cases | 123/200 | 123/200 | 10 / 10 |
| Static, new spec file | — | 27/31 (87.1%) | — / 0 |
| Blind Codex subagent, full applicable suite | 195/200 (97.5%) | 226/231 (97.8%) | 0 / 0 |
| Blind, unchanged original cases | 195/200 | 195/200 | 0 / 0 |
| Blind, new spec file | — | 31/31 (100%) | — / 0 |
| Blind original multi-step chain set, exact / prefix | 46/52 / 49/52 | 49/55 / 52/55 | — |

The blind before/after runs used separate isolated subagents with only the frozen exported menu, route guide and unlabeled prompts; they did not see expected answers or repository content. They used the inherited Codex session model, not the historical Haiku benchmark. Predictions were scored through the repository runner; baseline scoring excluded the new eval file. These are single-run comparisons, not statistical proof of improvement.

Priority neighbor files:

| File | Static before → after | Blind before → after |
|------|------------------------|----------------------|
| routr-plan | 6/7 → 6/7 | 7/7 → 7/7 |
| routr-explore | 2/7 → 2/7 | 7/7 → 7/7 |
| routr-review | 5/7 → 5/7 | 7/7 → 7/7 |
| routr-ship | 5/7 → 5/7 | 7/7 → 7/7 |

Static mode's four new misses concern missing helpers, dirty-source reconciliation, colloquial reverse engineering of code flow, and the three-step intent/build/reconcile request. The two multi-step chains beginning with ship/plan also expose its documented first-handoff chain heuristic. The descriptions were clarified around existing-vs-future intent and known implementation, without changing the lexical scorer or relabeling contested cases.

Blind residual misses all concern existing cases: Expo store copy/release, stuck AI streaming, a broken build before deferred deployment, EAS/native work and a pitch deck. None routes to `routr-spec`; no existing passing case regressed. These labels/descriptions were left outside this feature's scope.

An authenticated **Claude CLI / Haiku 4.5** run (`claude-haiku-4-5-20251001`, repository defaults) completed the full suite: **219/231 (94.8%)**, chains **46/55 exact and 51/55 prefix**, **zero first-router violations and zero failed calls**. The new spec file scored **31/31**, its three multi-step chains all matched, and plan/explore/review/ship each scored **7/7**. Its 12 routing misses are existing cases outside those five files. The difference from the Codex blind run is model/method variation, not a measured before/after regression. A separate inspection of single-job chains found an unjustified spec → ship step for an authentication-spec/product-changelog request; the first-router score did not catch it. This prompted an explicit artifact-ownership composition rule and single-step chain assertions for all 20 spec-only jobs, preserving the original prompts and expected routers. The offending case also forbids ship explicitly. Initial full-run chain numbers above predate those added assertions.

The final suite scores **75 chain cases** (52 original, 3 new multi-step and 20 new single-step). Final static results remain 150/231 and the same 10 pre-existing violations; chain exact/prefix are 31/75 and 35/75. A pre-fix focused Claude repeat also passed 31/31 spec routing cases without any extra single-job steps, demonstrating sample variation; the explicit rule and chain assertions were retained to protect artifact ownership.

A fresh isolated blind run of the final menu/guide on the spec file passed **31/31 routers and 23/23 chains**, with zero first-router or whole-chain forbidden-router violations. It saw only the exported menu, guide and prompts, not the new chain assertions or expected answers.

The focused Claude repeat across spec/plan/explore/review/ship scored **57/59 (96.6%)**: spec 31/31, plan 6/7, explore/review 7/7 and ship 6/7. The plan miss (UI sketch → plan) was identical to the separately captured pre-change Claude plan sample (also 6/7); the ship miss had no parsed prediction. This repeat's spec calls preceded the composition-rule correction. Rescoring its predictions against the strengthened labels gives **23/23 spec chains**, versus **22/23** for full-run A; neither rescoring is a fresh run of the corrected guide.

A fresh final-guide Claude attempt failed at preflight with **"Credit balance is too low"** (exit 2 from the eval runner), before any prompts were scored. No retry, credit purchase or account changes were made. The corrected guide is validated by the fresh isolated blind run above, plus final static/validator checks; do not claim a successful final-guide Claude run or average this unavailable sample into the results.

The validator passes with **zero warnings**. All changed Markdown links and anchors resolve; SKILL.md has fewer than 150 lines and its description is 266 characters. Registry canonical names, exact spec/ship handoff agreement, installer syntax and whitespace checks pass. There are 29 skills: 21 situational routers, 2 meta skills and 6 depth fallbacks. REA is not added to child install bundles; `routr-spec` is added to both router-install pickers.

### Source-only behavior fixture

A temporary Git repository exercised the fallback without helper skills or REA. Its original PRD requires passwords and a 20-row export limit; the initial implementation already uses magic links, and a later commit raises export to 50. Actual source/history inspection, focused unit tests and generation of all six artifacts were performed. A temporary writer serialized manually reviewed claims; this was workflow execution with assertions, not an independent blind behavioral evaluator or a new ROUTR runtime.

The final replay passed **22/22 checks**, including schema fields, evidence references, baseline preservation, application-input hashes, checkpoints and idempotency:

| Phase | Revalidated | Carried forward | Requirements / events |
|-------|-------------|-----------------|-----------------------|
| Initial | Authentication, export | — | 2 / 1 |
| Export-only commit | Export | Authentication at its original checked commit | 2 / 2 |
| Same-input rerun | — | Authentication, export | 2 / 2 |
| Wider scope, unchanged HEAD | Retention | Authentication, export | 3 / 3 |

BASELINE remained byte-identical through all four phases. The no-op rerun left PRODUCT_CHANGELOG byte-identical. Reconciliation changed no tracked application inputs. Auth's introduction in the first accessible commit was recorded, but no earlier implemented password flow was invented: its transition date/commit and rationale remain unknown. Newly included retention has an observed current contract but unknown original intent, so its comparison is UNVERIFIED rather than ADDED.

The fixture also exposed ambiguous source-locator wording; the final contract and replay require separate snapshot_path and section fields. The required-APK/unavailable-tools case was reviewed as a **simulation only**, with UNVERIFIED claims, a pending area, unchanged checkpoint and delegated REA recovery. No APK, REA MCP integration or engine installation was exercised.

### Reproduction and limits

```bash
python scripts/run-evals.py
bash scripts/validate-skills.sh
python scripts/run-evals.py --export-prompts prompts.json
# Give only prompts.json to an isolated model; collect predictions.json.
python scripts/run-evals.py --mode predictions --predictions predictions.json
python scripts/run-evals.py --mode claude --model claude-haiku-4-5-20251001
```

On this Windows host, bare Bash selects WSL and Git Bash finds a nonfunctional Store python3 shim before Python. The real validator was run through Git Bash with a process-local function selecting the working Python interpreter:

```powershell
& 'C:\Program Files\Git\bin\bash.exe' -c 'python3() { python "$@"; }; export -f python3; bash scripts/validate-skills.sh'
```

No persistent environment changes were needed. An initial shim-only "pass" was discarded. The link checker run over the entire repository also sees a placeholder link inside docs/authoring.md's fenced template; it is pre-existing sample text, not a broken feature link. Actual changed Markdown links were checked outside code fences, including anchors.

The routing runner scores the first router and declared chains. It does **not** execute children or grade `expected_behaviors`; REA gating, artifact correctness and checkpoint behavior require workflow review or fixture execution. The native-artifact direct-child boundary is therefore intentionally behavior-only, not a fake `routr-*` expectation.
