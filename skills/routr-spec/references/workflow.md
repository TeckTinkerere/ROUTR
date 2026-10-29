# Product specification reconciliation

## Establish scope and baseline

1. Identify the product, requested areas, source checkout and any supplied runtime/build. Do not select an unrelated installed app. Record a captured HEAD (if Git-backed), dirty state, environment and investigation date. Local source is not automatically production.
2. Find an existing product-spec/requirements structure and prior manifest. Reuse it with an explicit file-role mapping; otherwise use `.product-spec/`. Read existing artifacts before updates.
3. Find baseline candidates: original PRD, requirements, ADRs, product docs, roadmap/issues, README or a prior approved specification. Record path/URL, revision or content digest, date and authority for each. Prefer explicit user/project authority over filename or recency. Preserve disagreements and identify which candidate governs each area; ask only where unresolved authority prevents comparison.
4. Snapshot selected intent into BASELINE.md with source excerpts or faithful summaries and immutable references. Preserve a local snapshot if a mutable external document cannot be revisited by revision. Never overwrite the original PRD to match code. If no baseline exists, record that fact and still reconstruct CURRENT.md; absence of a document is not proof a feature was unplanned.
5. Establish coverage boundaries: roles, flags, environments, product versions and excluded areas. For a partial baseline, record the areas it actually covers.

## Evidence by claim, not one universal ranking

For ordinary repositories start with current source, baseline intent, tests, Git history, available PRs/issues/ADRs, then runtime and REA when necessary. These answer different questions:

| Claim | Preferred evidence | Limit |
|-------|--------------------|-------|
| Implemented behavior | Reachable source paths, config and relevant tests at a captured revision | Presence of code does not prove deployed or enabled behavior |
| Original requirement | Versioned authoritative baseline, with candidate provenance | README/roadmap aspirations are not automatically approved requirements |
| Tested contract | Assertions and actual test results, including environment | Test existence is not a passing run; mocks do not prove live integration |
| Introduction/change | Focused Git history, parent diff, release/build mapping if known | Blame identifies last line change, not necessarily behavior introduction or deployment date |
| Reason | Explicit commit/PR/issue/ADR explanation tied to the change | Implementation alone cannot confirm intent; author date is not a release date |
| Shipped behavior | Versioned artifact or observed runtime scenario | Scope to that build, role, flags and environment; static artifact analysis is not execution |

Use OBSERVED_FACT for directly supported statements (including that a document explicitly states an intention), INFERRED_INTENT for clearly labeled hypotheses, and UNKNOWN for missing/conflicting support. A high-confidence WHAT never upgrades an unsupported WHY. Omit speculative rationale by default; if useful, label its basis and alternatives.

When source and runtime disagree, preserve both claims with their distinct targets. Do not silently let either overwrite the other. Load optional `reverse-engineer-anything` only if the unresolved product claim needs shipped/package/runtime investigation. Follow its evidence and connection/recovery contracts; retain evidence identifiers, target identity and limitations, including inline evidence if retained references are unavailable. No copied engine/setup procedures belong here.

## Map and reconcile

1. Use `symdex-code-search` to narrow entry points and dependencies; use `lean-ctx` for mapped ranges. With neither available, use the [source fallback](./fallback.md).
2. Inventory capabilities and contracts by product area: actors/permissions, happy and denied paths, state transitions, defaults/limits, flags, integrations and user-relevant data retention/persistence. Connect each meaningful claim to evidence; identify reachability and scope before declaring a capability present or absent.
3. Assign stable IDs, reusing baseline IDs where possible. Split broad requirements only with recorded parent/child relationships; never renumber existing IDs because headings moved.
4. Compare baseline and current contract using [status rules](./artifacts.md#status-rules). Missing evidence becomes UNVERIFIED, not REMOVED. Confirmed enabled subsets are PARTIAL; proven disabled implementations are DORMANT. Separate baseline gaps from product additions.
5. For actual changes, inspect targeted history: `git log --follow -- <path>`, relevant `git log -S`/`-G` searches, `git show <commit> -- <path>` and parent diffs. Follow renames. Use blame as a lead, then verify the transition. Capture commit IDs, dates and explicit rationale; do not manufacture PR/issue metadata that is inaccessible.
6. Produce/update the six artifact roles. CURRENT describes the product at the recorded target; DRIFT compares against the preserved baseline; PRODUCT_CHANGELOG records evidenced product transitions, including documentation drift and unresolved intent. An initial discovery without a known introduction date is recorded as discovered, not as newly shipped today.

## Incremental reconciliation

First run or explicit full rebuild: build the scoped inventory and area/dependency map. A rebuild refreshes evidence, not the original baseline, stable IDs or evolution history. Record why a wider scan was needed.

For subsequent runs:

Compare requested scope with the saved manifest scope before checking file deltas. Newly included product areas, roles, flags, environments or versions are affected even at identical HEAD. Run the initial inventory only for that widened scope and its dependencies; never carry forward a checkpoint as evidence for previously excluded contracts. Retain exclusions when scope narrows and do not claim they were refreshed.

1. Read manifest and ledger; capture HEAD once. Confirm the saved commit exists and is an ancestor using `git cat-file -e <saved>^{commit}` and `git merge-base --is-ancestor <saved> <head>`. Use captured full hashes in commands. Never reset, clean, rebase, fetch or deepen history implicitly.
2. Inspect `git diff --name-status --find-renames <saved>..<head>` plus the corresponding log. Include tracked staged/unstaged changes and relevant untracked files in a separately identified working-tree overlay. Do not attribute uncommitted behavior to HEAD. Retain overlay content digests so edits/disappearances are detectable even when HEAD is unchanged.
3. Check baseline source revisions/digests and runtime build/environment identities independently of Git. Updated intent becomes a new baseline version only with explicit authority; preserve the old snapshot and record the baseline transition. A changed external spec or production build can require reconciliation even with no code diff.
4. Map changed paths/symbols to ledger IDs via the manifest's area paths and shared dependencies. For renames/deletions, inspect both old and new paths. New/unmapped files get a focused classification pass so entirely new capabilities are not missed. Ignore generated spec output changes as product input unless they change the selected baseline. Config, auth, shared policy, schema or integration changes may invalidate several areas; expand transitively and explain why.
5. Revalidate affected contracts only. Carry other records forward with their original checked commit/build, explicitly marked unaffected by this delta; do not pretend to have retested them. Changed assumptions or unmapped broad changes justify wider revalidation. Unresolved claims stay visible and retry when relevant evidence becomes available.
6. Update CURRENT/DRIFT and append only new product events with stable event IDs. A docs-only clarification is documentation drift, not a behavioral release. Same inputs and evidence produce no duplicate changelog events. Changes in a runtime observation need new target/scenario provenance even if the source commit is unchanged.
7. Validate artifacts as a consistent set, then write manifest last. Advance last_reconciled_commit only when all affected areas, including widened scope, were assessed and their results saved. Evidence-limited UNVERIFIED results may be recorded, but blocked affected areas stay in pending_areas and prevent checkpoint advancement. Keep per-area checked inputs so retries can reuse completed work. Recheck HEAD/overlay before finishing; if inputs moved, retain the old checkpoint and record the new pending delta.

### Recovery and non-Git products

- **Missing, shallow or rewritten history / branch switch with no ancestor:** preserve old checkpoint and artifacts; use accessible evidence to select a new scoped snapshot comparison, recording the discontinuity. Do not claim the full interval or introduction commit is known. After that reconciliation completes, establish a new checkpoint with the gap retained in history_gaps.
- **No Git:** use source content digests, artifact digests/version and baseline revisions to compare inputs. If no reliable inventory exists, do a scoped rescan and state why. Commit fields stay null.
- **Format mismatch/corrupt manifest:** preserve the old files, report the mismatch and migrate explicitly or rebuild a checkpoint from readable evidence; do not discard history or claim incremental continuity.
- **Uncommitted overlay:** successful reconciliation may checkpoint the committed range while retaining the overlay manifest and its evidence as uncommitted. Subsequent runs compare both the committed range and old/new overlay, including when those edits are later committed or reverted.

## Validation before reporting

Parse both JSON files; check format version, unique stable IDs, allowed statuses, evidence-reference resolution and required null/unknown fields. Confirm each non-UNVERIFIED comparison has evidence on both sides (or justified absence), and every confirmed reason has an explicit rationale source. Check Markdown tables and links agree with ledger, target scope and manifest. Never use wall-clock observation time as an invented introduction/release date. Report verified scope, carried-forward areas, pending areas and history limitations.
