# Perf examples

## Example 1: Slow dashboard load

**Input:** "The dashboard takes forever to load"

**Expected behavior:**
1. Baseline: LCP/TTFB via Lighthouse, note the number
2. Locate: is it server response time, bundle size, or a slow API call blocking render?
3. Fix the actual bottleneck found (not a guess)
4. Re-measure same way, report before → after

## Example 2: Bundle size complaint

**Input:** "Our JS bundle is huge, users on slow connections bounce"

**Expected behavior:**
1. Run build analyzer, get current KB (gzipped) as baseline
2. Identify largest chunks — often a whole-library import or duplicate dependency
3. Code-split or replace; re-run analyzer
4. Report KB before → after

## Example 3: Component re-renders too often

**Input:** "This list re-renders on every keystroke in an unrelated input"

**Expected behavior:**
1. React DevTools Profiler: confirm which component re-renders and why (shared context/state)
2. Fix: split context, memoize the list, or move state down
3. Re-profile the same interaction, confirm render count dropped

## Example 4: N+1 at the app level (boundary case)

**Input:** "The orders page is slow — it's issuing hundreds of queries"

**Expected behavior:** `routr-perf` — this is app-level query fan-out (N+1), not a single query needing an index. Locate the loop issuing per-row queries, batch or join it, verify query count dropped. Route a genuinely single slow query to `routr-database` instead.

## Example 5: Memory leak in a long-running session

**Input:** "The app gets sluggish after being open for an hour"

**Expected behavior:** Heap snapshot diff across repeated navigation, find the growing object type (often uncleaned subscriptions/listeners), fix the cleanup, re-diff to confirm growth stopped.

## Example 6: Functional bug, not perf (boundary case)

**Input:** "The search results are wrong after typing fast"

**Expected behavior:** Route to `routr-debug` — wrong output from a race condition, not a speed complaint, even though the trigger is fast typing.
