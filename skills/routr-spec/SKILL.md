---
name: routr-spec
description: "Reconcile existing products. Use when: compare current app vs original PRD, as-built spec, stale docs, product drift/evolution, incremental reconciliation. Not for: unbuilt features (→ routr-plan); code walkthroughs (→ routr-explore); implement fixes (→ routr-ship)."
---

# routr-spec

**Goal:** an evidence-backed current product specification, reconciled with original intent and a traceable product-evolution history.

## When to activate

- Reconstruct an existing app into an as-built PRD, including when called "reverse engineering"
- Compare current product behavior with original requirements; explain drift without inventing intent
- Update a living specification and product changelog since the previous reconciliation
- Reconstruct a shipped product's specification when source alone cannot establish behavior

## Do not activate

- Decide what to build next → `routr-plan`
- Explain code or architecture only → `routr-explore`
- Judge a PR or diff's quality → `routr-review`
- Implement missing requirements → `routr-ship` (or plan first if scope is unresolved)
- Restructure code without behavior changes → `routr-refactor`
- Low-level artifact inspection/decompilation alone → use `reverse-engineer-anything` directly; no product-spec router needed

## Iron law

**Distinguish OBSERVED FACT, INFERRED INTENT, and UNKNOWN. Never manufacture why a product changed.**

Code may establish WHAT; Git may establish WHEN; a commit explanation, PR, issue or ADR may establish WHY. Runtime evidence establishes only the observed shipped target and scenario. Missing rationale stays unknown, even when the behavior change is certain.

Edit only requested specification artifacts. Never change application code, tests, flags, the original PRD or the repository release changelog to make drift disappear.

## 0. Bootstrap (low freedom)

Resolve only needed children through [resolution.md](../routr-catalog/references/resolution.md). This workflow does not silently install skills, engines or tools or change the environment; use [fallback.md](./references/fallback.md) when helpers are missing.

| Order | Skill | Tier / gate |
|-------|-------|-------------|
| 1 | `symdex-code-search` | recommended — locate source contracts and affected callers |
| 2 | `lean-ctx` | recommended — read mapped signatures and focused ranges |
| 3 | `reverse-engineer-anything` | optional — only claims needing shipped/runtime evidence unavailable or unreliable in source |

**Budget gate:** a sufficient source repository needs only the source path. "Reverse engineer my app" is not an REA trigger by itself. No REA readiness/provider calls on that path. Do not load planning children merely because the deliverable is called a PRD.

REA applies to shipped binaries/packages, Electron/JS, APK/native/.NET, browser/application runtime, source-versus-production discrepancies, or absent/incomplete/contradictory source when those affect the question. Read the child's real skill for execution and its connection/recovery guide if tools are absent or blocked. Skill installation does not register MCP or install engines. Continue independently supported source work; mark only dependent claims unverified.

## 1. Establish baseline (medium freedom)

- Locate the existing specification directory; default to `.product-spec/` only if none fits.
- Identify authoritative PRD/requirements/ADRs/docs with provenance. A README is a candidate, not automatically the original PRD.
- Preserve original snapshots and competing candidates; record unresolved authority instead of inventing a baseline.
- Record target commit/build/environment and coverage. Read [workflow.md](./references/workflow.md) before collecting evidence.

## 2. Establish current reality (medium freedom)

Map product capabilities, business rules, permissions, workflows, state transitions, integrations, relevant persistence and constraints. Use source → focused tests/history; add runtime/REA only for claims that require it. Describe observable contracts, not a file-by-file implementation tour.

## 3. Reconcile and explain evolution (low freedom)

- Use stable requirement IDs and the deterministic status rules in [artifacts.md](./references/artifacts.md).
- Keep behavior status separate from intent confidence. Unknown intent does not hide a confirmed modification.
- Trace claims to versioned source/docs/tests/history or scoped runtime evidence. Record contradictions and coverage gaps.
- Investigate relevant Git/PR/issue/ADR history for when and why; unavailable metadata stays missing evidence.

## 4. Maintain artifacts (low freedom)

When creation/update is requested, maintain BASELINE.md, CURRENT.md, DRIFT.md, PRODUCT_CHANGELOG.md, ledger.json and manifest.json using the [artifact contract](./references/artifacts.md). Writing these artifacts is part of this router, not a ship or planning handoff. Preserve original intent; product evolution is distinct from the repository release changelog. For an answer-only request, report findings and proposed artifact locations without writing them.

Subsequent runs use the saved last-reconciled commit through the captured HEAD, plus relevant baseline/runtime changes and working-tree overlays. Revalidate affected product areas and shared dependencies; carry unaffected evidence forward with its original verification scope. Explicit full rebuilds and invalid checkpoints use the recovery rules in [workflow.md](./references/workflow.md#incremental-reconciliation).

## 5. Verify and finish

- Check evidence links, IDs, status rules, unknown rationale, scope and artifact agreement.
- Preserve baseline versions and existing product history; avoid duplicate evolution events on reruns.
- Advance the checkpoint only after the covered reconciliation is persisted and validated.
- Report changed/unaffected/unverified areas, evidence limitations and the next checkpoint.

## Handoff

**Reconciliation recorded → STOP.** Missing functionality is drift, not permission to implement. Only continue when the user requests the next job:

| Next | Skill |
|------|-------|
| Decide desired behavior or scope unresolved requirements | `routr-plan` |
| Implement a specified, understood missing requirement | `routr-ship` |

One router active at a time; maximum three steps. A requested intent → implementation → reconciliation can use plan → ship → spec. Reconciliation is never an automatic step on every implementation request.

## References

- [workflow](./references/workflow.md) — evidence collection and incremental checkpoints
- [artifacts](./references/artifacts.md) — format version, statuses, ledger and manifest
- [fallback](./references/fallback.md) — source-only operation and blocked evidence
- [gotchas](./references/gotchas.md) — provenance and scope failures
- [examples](./references/examples.md) — concrete reconciliations
- [boundaries](./references/boundaries.md) — neighboring routers and direct REA work
