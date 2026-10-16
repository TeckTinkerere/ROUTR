# Reconciliation without helper skills

Resolve children using the host's bare/namespaced listing and filesystem fallback in [resolution.md](../../routr-catalog/references/resolution.md). Missing helpers do not authorize installation. Offer the registry command only if needed; do not silently change the environment.

## Source repository is sufficient

1. Find authoritative baseline candidates and preserve provenance.
2. Use `rg --files`, focused `rg` searches, entry points and relevant tests to map product areas. Read narrow source ranges; follow reachable calls/config, not every file.
3. Inspect Git history for changed contracts and recorded rationale. No Git or remote metadata means explicit gaps, not guessed dates or reasons.
4. Use the same [workflow](./workflow.md) and [artifact contract](./artifacts.md), including incremental checkpoints and source-only scope labels.

No REA dependency exists on this path. Absence of REA must not reduce confidence in a contract adequately established by source; it does limit any claim about a particular deployed product that was not observed.

## Shipped/runtime evidence is necessary

Load `reverse-engineer-anything` only for those claims. If its tools/provider are missing or blocked, follow the installed child's connection/recovery guide, using supported work and any authorized fallback it provides. Do not copy setup commands here or imply installing its skill registered MCP. If the skill itself is absent, point to the [registry](../../routr-catalog/references/skill-registry.md#shipped-and-runtime-evidence) and upstream skill; record the missing capability.

Continue source-based areas independently. Mark artifact-dependent claims UNVERIFIED with the missing evidence, target and next action. Pending affected areas prevent falsely advancing the complete reconciliation checkpoint. Do not present source expectations as observed production behavior, silently install engines, repair MCP configuration or execute a target without authorization.

## No authoritative baseline

Produce a scoped current specification and an explicit missing-baseline record. Candidate docs can be cited as candidates; comparison remains UNVERIFIED where original intent is unknown. Do not invent requirements or label every discovered feature ADDED. Keep useful evidence and questions so a later supplied baseline can be reconciled without repeating the current-state scan.
