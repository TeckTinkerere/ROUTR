# Living specification artifact contract (version 1)

This is an interchange contract for documents and JSON, not a new application or runtime. Use an existing specification directory when appropriate, recording the mapping in manifest.json; otherwise use `.product-spec/`. Keep machine fields in English for deterministic updates; prose may follow the product's language.

## File roles

| Default file | Required content |
|--------------|------------------|
| BASELINE.md | Immutable original-intent snapshot(s), selected baseline ID, candidate provenance/authority, coverage and conflicts. Preserve excerpts/summaries plus revision/digest and original locator. Add a new version for an explicitly authorized baseline change; retain previous versions. |
| CURRENT.md | As-built product specification: target/scope, actors, capabilities, rules, permissions, workflows/states, integrations and relevant constraints; stable requirement IDs and evidence references. Mark source-established vs runtime-observed behavior and unknowns. |
| DRIFT.md | Baseline ID and target, then Requirement / Baseline / Current / Status / Evidence, with separate intent confidence and unresolved gaps. Include carried-forward scope. |
| PRODUCT_CHANGELOG.md | Product-evolution events grouped under Added, Changed, Removed, Behavioral Drift, Documentation Drift and Unknown / unresolved intent where useful. Stable event ID, requirement IDs, before/after, known occurrence commit/date or unknown, discovery date and evidence. Never substitute the repository release changelog. |
| ledger.json | Durable requirement records, evidence catalog and product-event identities. Human-readable files are views of these records. |
| manifest.json | Format/baseline/target identities, checkpoints, file roles, area dependencies, changed inputs and pending scope. Persist last after validating the other artifacts. |

Don't copy implementation trivia into CURRENT. A path belongs in an evidence citation, not in a user requirement unless it is itself an external contract (such as a public API route).

## Status rules

Use exactly one behavior status per record. Reason/intent confidence is a separate axis: UNKNOWN_INTENT is represented by reason.classification = UNKNOWN, never as a competing behavior status.

Apply these rules in order. Scope every comparison to the selected baseline and current target:

| Status | Deterministic condition |
|--------|-------------------------|
| UNVERIFIED | Either side, coverage or conflicting evidence prevents a supported comparison. No authoritative baseline, an unexplored runtime requirement, or unestablished absence belongs here. |
| DORMANT | Implementation exists but evidence proves it unreachable/disabled in the specified scope. Record activation conditions; do not count it as available. |
| ADDED | Current available contract exists and baseline evidence establishes its absence/exclusion within a sufficiently complete baseline scope. Mere silence in partial docs is insufficient. |
| REMOVED | Historical evidence establishes prior implementation of the baseline contract, and evidence establishes current absence across the relevant scope. A requirement written in a PRD alone does not establish that a feature was removed. |
| MISSING | Baseline requires a contract that is demonstrably absent now, but prior implementation is not established (including never-built work). Record historical uncertainty; do not claim removal. |
| MATCH | Supported current contract meets the baseline with no meaningful difference in the compared behavior. |
| PARTIAL | A supported, available subset of a baseline contract exists; remaining obligations are demonstrably unmet. |
| MODIFIED | Both sides are established but rules, workflow or outcome differ beyond a missing subset, including replacement by another contract. |

If the baseline explicitly excluded a now dormant implementation, DORMANT takes precedence over ADDED. Split independent subcontracts with related IDs when one status would conceal distinct outcomes. Nothing requires inventing a baseline absence to classify a discovered feature; CURRENT remains useful with UNVERIFIED comparisons.

## Ledger schema

Required root fields: schema_version (1), baseline_id (selected baseline or null), records (array), evidence (array) and events (array). IDs are unique within each array. Retain IDs across moves and updates; never recycle removed requirement IDs. All evidence_ids resolve to this catalog. Include records for significant unresolved contracts as well as confirmed ones.

Each record has:

| Field | Contract |
|-------|----------|
| id, area | Stable requirement ID and product area key, matching manifest areas |
| related_ids | Existing requirement IDs for splits, merges or related contracts; empty array if none |
| baseline, current | State objects described below; never ambiguous bare nulls |
| status | One status from the table above |
| reason | value (text or null), classification (OBSERVED_FACT / INFERRED_INTENT / UNKNOWN), evidence_ids, limitations (array). Confirmed rationale requires an explicit intent source; UNKNOWN uses value null and lists missing evidence. An inferred rationale must name its basis and remain labeled a hypothesis. |
| introduced_commit, changed_commit | Full verified commit IDs or null. Distinguish original introduction from the compared transition; use null when history cannot establish them. |
| user_visible | Boolean; false may still describe an important permission/integration contract |
| verification | checked_commit (full hash or null), target_id, checked_at (ISO 8601), method (source / runtime / artifact / mixed), coverage (text), carried_forward (boolean) |

A state object has value (text or null), presence (present / absent / unknown), classification (OBSERVED_FACT / INFERRED_INTENT / UNKNOWN), evidence_ids (array) and scope (text). Proven absence uses presence absent, value null, OBSERVED_FACT and negative evidence. Unknown uses presence unknown, value null, UNKNOWN and a gap explanation in scope; evidence_ids may be empty. A baseline document's stated requirement is an observed documentary fact, not proof it was ever implemented. Inferred intent must not be promoted to an established baseline/current contract for classification.

Evidence entries require id, kind (source / baseline / test / git / pr / issue / adr / runtime / artifact), locator (path/URL/tool evidence reference with section/symbol/range), revision (commit/doc revision/build ID or null), digest (content/artifact SHA-256 or null), target_id (or null for baseline intent), observed_at (ISO 8601), supports (what this evidence actually establishes) and limitations (array). Record a revision or digest for reproducibility where practical; otherwise explain why unavailable. Runtime/artifact evidence retains build/environment/scenario identity and retained or inline REA evidence as applicable. Do not copy secrets or sensitive runtime data into specification artifacts.

Events require id, requirement_ids, baseline_id (or null), target_id, category (Added / Changed / Removed / Behavioral Drift / Documentation Drift / Unknown), before, after, reason (same shape as the record), occurred_commit (or null), occurred_at (ISO 8601 or null), discovered_at, evidence_ids and supersedes (prior event ID or null). Retain the event's original intent/provenance even when the current record changes again. Use a deterministic event identity derived from requirement IDs + before/after contract + evidence transition identity (commit pair or target/input digests), excluding reconciliation timestamps and line-number-only movement. Maintain the same ID when an uncommitted overlay is later committed without changing the contract; enrich its provenance. Append a linked correction for a retracted conclusion rather than erasing earlier history. A discovered feature with unknown origin must not receive today's date as occurred_at.

### Example: no evidence for why authentication changed

This illustrative record refers to catalog entries E-PRD, E-AUTH and E-TEST; replace them with real locators before writing a product ledger. No hashes are invented here.

```json
{
  "id": "AUTH-03",
  "area": "authentication",
  "related_ids": [],
  "baseline": {
    "value": "Password login",
    "presence": "present",
    "classification": "OBSERVED_FACT",
    "evidence_ids": ["E-PRD"],
    "scope": "Original PRD's customer login requirement"
  },
  "current": {
    "value": "Magic-link login replaces password login",
    "presence": "present",
    "classification": "OBSERVED_FACT",
    "evidence_ids": ["E-AUTH", "E-TEST"],
    "scope": "Reachable customer login in the captured source snapshot; production unobserved"
  },
  "status": "MODIFIED",
  "reason": {
    "value": null,
    "classification": "UNKNOWN",
    "evidence_ids": [],
    "limitations": ["No explicit rationale found in accessible history; PR/issue metadata unavailable"]
  },
  "introduced_commit": null,
  "changed_commit": null,
  "user_visible": true,
  "verification": {
    "checked_commit": null,
    "target_id": "source-snapshot-1",
    "checked_at": "2026-10-16T00:00:00Z",
    "method": "source",
    "coverage": "Customer login; source snapshot digests retained in evidence catalog",
    "carried_forward": false
  }
}
```

## Manifest schema

Required fields and null semantics:

| Field | Contract |
|-------|----------|
| schema_version, spec_format_version | Integers, both 1 for this contract; detect unsupported versions before incremental updates |
| artifacts | Role-to-relative-path map for baseline/current/drift/product_changelog/ledger/manifest; preserve existing directory conventions |
| baseline | id (or null), selected_sources (array), candidates (array), versions (array). Each source stores locator, revision, digest, authority, coverage, snapshot_path and section. Each version retains its ID and source identities. Missing baseline uses null id and explicit candidate/authority gaps. |
| target | id, kind (source / runtime / artifact / mixed), captured_at, head_commit (or null), build (or null), environment (text), input_digests (path/reference → digest). Never call a source target a deployed observation. |
| last_reconciled_commit | Full Git hash or null; successful coverage checkpoint, not simply latest seen HEAD |
| last_reconciled_target | Last completed target identity/digests, or null; enables non-Git and runtime comparisons |
| scope | Included areas, roles/flags/environments and exclusions; this bounds what the checkpoint claims |
| areas | Array: id, paths (patterns), depends_on (other area IDs), requirement_ids, checked_inputs (commit/build/baseline/overlay identities), disposition (revalidated / carried_forward / pending). Include shared policy/config areas so changes propagate. |
| working_tree | dirty (boolean), inputs (array of path, layer: index / working_tree / untracked, state: present / deleted, digest). A path can have separate index and working_tree entries when both differ. Store no secret content. A deleted input has digest null. Keep overlay separate from committed evidence. |
| pending_areas | Array of area ID, blocker and needed evidence; empty only when declared affected scope was assessed |
| history_gaps | Array of old/new checkpoint identities, reason and known coverage; retain discontinuities across rebuilds |
| last_run | mode (initial / incremental / full / recovery), compared_from, compared_to, changed_areas, unaffected_areas, completed (boolean), limitations |

Record external baseline/runtime inputs even when unchanged Git commits permit a no-op. The manifest describes the most recent attempt; last_reconciled_commit and last_reconciled_target remain at the previous completed checkpoint when the attempt is blocked. Per-area checked_inputs permit reuse of completed evidence during retries.

## Integrity and updates

- Evidence is scoped, not a universal truth: source, packaged source and runtime may disagree without either observation being fabricated. Keep distinct target IDs and mark unresolved aggregate comparisons UNVERIFIED.
- Persist the ledger and Markdown views consistently before the manifest. Preserve existing files if interrupted; a manifest referencing an incomplete set is not a valid checkpoint.
- Validate all IDs, references, enumerations and status conditions; evidence-less confirmed reasons or unsupported ADDED/REMOVED claims fail the contract. Never silently convert nulls into confident prose.
- Unknown rationale is displayed beside a confirmed behavior status, including in the product changelog. Unknown date/commit stays null. Baseline changes require preserved versions and explicit authority.
- If existing artifacts use another schema, document a compatible role/field mapping or an explicit migration; do not casually overwrite the user's structure.
