---
name: routr-perf
description: "Performance: Core Web Vitals, bundle size, re-renders, slow APIs, N+1 queries, memory leaks, caching. Use when: slow page, high INP, big bundle, leak growing. Not for: wrong output (routr-debug), one query (routr-database), redesign (routr-frontend), animating (routr-motion)."
---

# routr-perf

**Goal:** make it measurably faster — never optimize on vibes.

## When to activate

- Core Web Vitals regressions: LCP, INP, CLS
- Bundle size growth, slow initial load
- React re-render storms, unnecessary renders
- Slow API endpoints, N+1 or slow queries at the app/request level
- Memory leaks, growing heap over time
- Missing or wrong caching (HTTP, data, memoization)

## Do not activate

- Output is wrong, not slow → `routr-debug`
- One slow SQL query, index, or schema design → `routr-database` (N+1, connection-pool exhaustion, or latency spread across many queries stays here)
- Visual redesign with no perf complaint → `routr-frontend`
- Browser smoke test only, no perf claim → `routr-qa`
- Authoring or polishing an animation → `routr-motion` (janky/dropped-frame diagnosis is `routr-perf`; the fix once located is `routr-motion`)
- Structural cleanup with no measured slowness → `routr-refactor`

## Iron law

**Measure before and after — no optimization without a baseline number.**

## 0. Bootstrap

Install missing from `routr-catalog/references/skill-registry.md`.

| Order | Skill | Tier |
|-------|-------|------|
| 1 | `vercel-react-best-practices` | recommended — render profiling, memoization, RSC boundaries |
| 2 | `webapp-testing` | recommended — Lighthouse/CWV measurement in a real browser |
| 3 | `supabase-postgres-best-practices` | recommended — N+1 / slow query diagnosis when Supabase/Postgres |
| 4 | `symdex-code-search` | recommended — locate hot paths, callers |
| 5 | `lean-ctx` | recommended — narrow reads on large files/bundles |
| 6 | `vercel-optimize` | optional — Vercel edge caching, build/runtime tuning |

**Budget gate:** read `required`/`recommended` only for the symptom at hand — a bundle-size task does not need `supabase-postgres-best-practices`. Pull `vercel-optimize` only on Vercel deployments.

No dedicated `routr-depth-perf` fallback exists — if every child skill above is missing, use [references/fallback.md](./references/fallback.md) directly.

## 1. Baseline (low freedom)

- [ ] Capture the metric that's actually complained about (LCP ms, INP ms, bundle KB, render count, endpoint p95 ms, heap MB) — before any change
- [ ] Record how it was measured (tool, device/throttle profile, environment)
- [ ] State the target (a number, not "faster")

## 2. Locate the bottleneck (medium freedom)

1. SymDex/lean-ctx: find the hot path, not the whole app
2. Web Vitals: Lighthouse/Chrome DevTools Performance panel via `webapp-testing`
3. Bundle: build analyzer output (webpack-bundle-analyzer, `next build` output, etc.)
4. React renders: React DevTools Profiler — which component, how many renders, why
5. API/DB: server timing, slow query log, N+1 detection (count of queries per request)
6. Memory: heap snapshot diff over repeated action, not a single snapshot

## 3. Fix discipline (medium freedom)

- Smallest change that moves the measured number
- One change at a time — re-measure between changes, don't batch fixes
- Prefer removing work (fewer renders, fewer queries, smaller payload) over adding infra (caching layer) when both close the gap
- Caching only after the uncached path is understood — caching over a bug hides it

## 4. Verify (low freedom)

- [ ] Re-measure the same metric, same method as the baseline
- [ ] State before → after with numbers, not "should be faster"
- [ ] Check for regressions in adjacent metrics (e.g. bundle split shouldn't blow up request count)

## Output format

```markdown
## Perf report
**Metric:** … (e.g. LCP, bundle KB, endpoint p95, heap growth)
**Baseline:** … (number, method)
**Bottleneck:** … (root cause, not symptom)
**Fix:** …
**After:** … (number, same method) — delta
```

## Handoff

| Need | Router |
|------|--------|
| Fix is understood, ready to commit | `routr-ship` |
| Root cause of slowness is actually a bug (wrong query, infinite loop) | `routr-debug` |
| Single query needs an index/rewrite | `routr-database` |
| Deploy the fix | `routr-deploy` |

## References

- [workflow](./references/workflow.md) — phased perf process per symptom
- [fallback](./references/fallback.md) — when no child skills installed
- [gotchas](./references/gotchas.md)
- [examples](./references/examples.md)
- [boundaries](./references/boundaries.md)

## Anti-patterns

- "This should be faster now" with no before/after number
- Changing five things then measuring once
- Adding a cache in front of a bug instead of fixing the bug
- Full bundle rewrite for a single slow component
