# Product reconciliation examples

## Source-only as-built PRD

**Input:** "Reverse engineer my current app into a PRD and compare it against the original. All source and tests are here."

**Result:** `routr-spec`. Snapshot the authoritative original with revision/hash, map reachable product contracts with source/test evidence, write CURRENT and DRIFT. Skip REA and its readiness/provider commands. A PRD-shaped output does not require a future-planning child.

## Authentication changed, reason unknown

Baseline AUTH-03 requires password login; current reachable handlers and tests establish magic links instead. A parent diff identifies the replacement commit, whose message says only "update auth". PR/issue metadata is unavailable.

| Requirement | Baseline | Current | Status | Evidence |
|-------------|----------|---------|--------|----------|
| AUTH-03 | Password login | Magic-link login | MODIFIED | Baseline section + current handler/test + parent diff, all at recorded revisions |

**Observed fact:** authentication changed. **Reason:** UNKNOWN; no commit explanation, PR, issue or ADR establishing why was available. Record the missing sources. Do not invent a conversion/security rationale or downgrade the confirmed MODIFIED status because intent is unknown.

## Incremental billing update

The manifest checkpoints commit A; HEAD is B. A..B changes billing limits and a shared entitlement check. Revalidate billing plus dependent export permissions, follow a renamed policy file and classify new routes. Carry unrelated search evidence forward at A. Append one product event per evidenced transition, update CURRENT/DRIFT, validate, and write the new checkpoint last. Rerunning at B with identical inputs appends nothing.

## Shipped Electron app

**Input:** "We inherited this shipped Electron app and need an evidence-backed current spec. There is no source checkout."

`routr-spec` establishes target and baseline candidates, then loads optional `reverse-engineer-anything` for artifact/runtime evidence. Preserve its Evidence identifiers, artifact digest/version and scope. Static package findings and executed scenarios remain distinct. Missing MCP/provider access follows REA's own recovery contract; unaffected documentary work continues and blocked claims stay UNVERIFIED. Installing the skill alone does not solve tool registration.

## Partial intent and dormant code

An old PRD explicitly excludes guest export but mentions nothing about admin export. Current admin export works; guest export exists behind a proven disabled flag. Guest export is DORMANT with flag/reachability evidence. Admin comparison is UNVERIFIED if the baseline's coverage cannot establish whether it was intended; do not call it ADDED solely because the PRD omitted it.

## Missing functionality is recorded, not implemented

The baseline requires three account roles; two are reachable and tested. Record PARTIAL with the missing role. Stop after reconciliation. "Now decide which roles we should support" hands to `routr-plan`; "implement the already specified third role" hands to `routr-ship` when suitable. No implementation follows merely from discovering the gap.

If the promised roles are entirely absent and prior implementation cannot be established, use MISSING, not REMOVED. REMOVED requires evidence of an actual earlier implementation.

## Source and production diverge

Source at commit C permits export; the observed build R denies it for a specified role. Record both scoped claims and an UNVERIFIED combined comparison until the target mapping/config discrepancy is resolved. Use REA when necessary for shipped/runtime evidence. Neither the source commit date nor the observation date establishes when build R changed behavior.

## Rewritten history or changed baseline

The saved Git commit is no longer an ancestor. Preserve it and the old evidence, record a history gap and reconcile affected areas as a new snapshot before establishing a checkpoint. If the user supplies a newly approved PRD, preserve baseline v1 and add v2 with explicit authority and provenance; describe which baseline each drift report compares. A full rebuild never erases earlier intent.

## Wider scope at unchanged HEAD

The prior run covered billing only. The user now wants the whole product at the same commit. Inventory the previously excluded product areas and their dependencies, reuse still-valid billing evidence, and update the declared scope only after the new areas have been assessed. An empty Git range does not establish coverage.
