# Reconciliation gotchas

1. **Plausible rationale is not evidence.** Password auth became magic links; "to reduce friction" is unknown unless a source establishes it. A design hypothesis stays INFERRED_INTENT.
2. **Code presence is not availability.** Disabled flags, disconnected routes, environment gates and dead implementations require reachability evidence; use DORMANT only when inactivity is established.
3. **Silence is not removal.** Search scope and negative evidence matter. Missing source/runtime evidence is UNVERIFIED; incomplete baseline coverage cannot establish ADDED.
4. **Source is not production.** Preserve both targets when package version, runtime settings or observed behavior differ. A static REA finding still does not prove execution.
5. **Latest docs are not original intent.** Preserve the original snapshot and authority. Updating CURRENT does not authorize rebasing BASELINE or editing the original PRD.
6. **Blame is not origin or motive.** Formatting/refactors move lines. Verify behavior transitions using parents/history; recorded intent needs a directly relevant explanation.
7. **Clean Git diff is not unchanged product.** External docs, flags, runtime builds and working-tree/untracked inputs can change without HEAD moving.
8. **A shared policy can affect many areas.** Revalidate dependents when auth, schema or integration assumptions change; do not mechanically restrict to changed filenames.
9. **Reruns can duplicate history.** Stable requirement/event identities and source fingerprints distinguish new evolution from repeated discovery. Correct a mistaken event with a linked correction rather than silently rewriting history.
10. **The product changelog is not a release log.** Record observable capabilities/rules and documentation drift; avoid dependency bumps or refactors unless product behavior changed. Never edit ROUTR's own CHANGELOG as the user's product history.
11. **Helpers are optional infrastructure.** Missing REA is irrelevant to sufficient source work. Missing runtime evidence blocks only dependent claims; preserve pending areas and checkpoint integrity.
12. **Same HEAD is not the same scope.** A billing-only checkpoint cannot validate a later whole-product request. Inventory newly requested areas/roles/environments even when no files changed.
13. **Unbuilt is not removed.** A promised but absent capability is MISSING unless history establishes it once existed. A PRD alone cannot prove prior implementation.
