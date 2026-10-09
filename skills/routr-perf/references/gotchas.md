# Perf gotchas

1. **No baseline, no claim**: "I optimized the render path" with no before/after number is not a finding — measure first, always.
2. **Dev-mode numbers**: React dev builds and unminified bundles are much slower/larger than production — always measure against a production build.
3. **Cold vs warm cache**: first load and repeat load differ hugely (CDN cache, browser cache, DB connection pool warm-up) — state which one was measured.
4. **Memoizing everything**: wrapping every component in memoization helpers (`useMemo`, `useCallback`, and friends) without profiling first often adds overhead without fixing the actual re-render cause.
5. **N+1 hidden by an ORM**: a single line of ORM code can silently issue one query per row — check the query log/trace count, not the source line count.
6. **Caching over a bug**: adding a cache in front of a slow, broken, or wrong result hides the bug and complicates the eventual fix — fix first, cache second.
7. **Throttling mismatch**: testing on a fast dev machine/network hides real-world mobile/3G LCP and INP — use DevTools throttling presets or real device testing.
8. **Single-run measurements**: one Lighthouse run has variance — run 3+ times and use the median, especially before/after comparisons.
9. **Bundle analyzer blind spots**: a bundle analyzer shows shipped size, not parse/execute cost — a small but synchronous script can still block the main thread.
