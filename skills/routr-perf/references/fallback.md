# Perf fallback (no child skills installed)

Use when none of the bootstrap skills in `SKILL.md` are available.

## Iron law

```
MEASURE BEFORE AND AFTER — NO OPTIMIZATION WITHOUT A BASELINE NUMBER
```

## Minimum process

1. **Name the metric** — LCP ms, INP ms, bundle KB, render count, endpoint p95 ms, or heap MB. "Feels slow" is not a metric; get a number first.
2. **Measure baseline** — browser DevTools Performance/Network/Memory panels are available with no extra skill installed. Use them:
   - Web Vitals: Chrome DevTools → Performance panel → record page load or interaction
   - Bundle: the framework's own build output usually prints chunk sizes; otherwise `du -sh` on the build output directory as a rough proxy
   - Renders: React DevTools (browser extension) Profiler tab
   - API: add a timestamp log at request start/end if no APM exists
   - Memory: DevTools → Memory panel → heap snapshot, repeat action, diff
3. **Locate the bottleneck** — narrow with search (grep/SymDex-equivalent) to the hot path before reading whole files
4. **One fix at a time** — smallest change, re-measure between each
5. **Verify** — same metric, same method, report before → after with numbers

## When stuck

- Can't tell what's slow → add coarse timing logs around suspected boundaries (request in/out, render start/end) before guessing
- No production data → lab-test locally with throttled CPU/network (DevTools has built-in throttling presets)

## Escalate to install

```bash
npx skills add vercel-labs/agent-skills -g --skill vercel-react-best-practices --skill vercel-optimize -y --copy
npx skills add anthropics/skills@webapp-testing -g -y --copy
npx skills add supabase/agent-skills -g --skill supabase-postgres-best-practices -y --copy
```
