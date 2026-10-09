# Perf workflow (per symptom)

## Core Web Vitals (LCP / INP / CLS)

1. Measure with Lighthouse or Chrome DevTools Performance/Web Vitals panel (`webapp-testing`) — lab data; cross-check field data (CrUX/RUM) if available
2. LCP: find the largest contentful element — image, hero text, web font. Check preload, format, server response time
3. INP: find the long task blocking the main thread on interaction — heavy event handler, synchronous layout, unbatched state updates
4. CLS: find the element shifting layout — missing image dimensions, late-injected content, web font swap

## Bundle size

1. Run the framework's build analyzer (`next build`, webpack-bundle-analyzer, `vite build --report`, etc.) — get actual KB, not a guess
2. Identify the largest chunks: duplicate deps, unnecessary polyfills, a library imported whole instead of tree-shaken
3. Fix: code-split, lazy-load below-the-fold, replace a heavy dependency, dedupe

## React re-render profiling

1. React DevTools Profiler — record an interaction, read which components rendered and why (props changed, context changed, parent re-rendered)
2. `vercel-react-best-practices` for memoization, key stability, context-splitting patterns
3. Fix the actual re-render cause — do not wrap everything in memoization helpers speculatively

## Slow API endpoints / N+1 / app-level slow queries

1. Server timing / APM trace for the endpoint's p50/p95
2. Count queries per request — N+1 shows up as "1 query becomes N" in the trace or query log
3. `supabase-postgres-best-practices` for index/query-shape fixes once the N+1 site is found
4. Connection-pool exhaustion: check pool size vs concurrent request count, not just query speed

## Memory leaks

1. Take a heap snapshot, repeat the suspected action N times, take another snapshot, diff
2. Growing count of a specific object type across repeats = the leak signature
3. Common causes: uncleaned event listeners/subscriptions, growing closures in intervals, detached DOM nodes held by JS references

## Caching

1. Confirm what's actually happening without cache first (baseline)
2. Pick the right layer: HTTP cache headers, CDN/edge cache, data cache (server), memoization (client)
3. State the invalidation rule before shipping — a cache with no invalidation plan is a bug waiting to happen

## Tool order (all symptoms)

1. SymDex/lean-ctx to find the hot path — never start with a full-repo read
2. Measure baseline with the right tool for the symptom (above)
3. Fix smallest change
4. Re-measure same way
