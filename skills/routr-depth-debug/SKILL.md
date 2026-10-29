---
name: routr-depth-debug
description: "Structured debugging when systematic-debugging is not installed. Use when: routr-debug bootstrap fails, child debug skill missing, or agent about to guess fixes."
---

# routr-depth-debug

Fallback depth for `routr-debug`. Load only when `systematic-debugging` is not installed.

## Iron law

```
NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST
```

## Four phases (complete each before next)

### Phase 1: Root cause investigation

1. Read error messages and stack traces completely
2. Reproduce — document exact steps; if not reproducible, gather data
3. Check recent changes (git diff, deps, env)
4. Multi-component: log at each boundary, run once, localize failure layer

### Phase 2: Hypothesis

1. One-sentence root cause theory
2. Minimal experiment to confirm/deny
3. Max 3 parallel hypotheses

### Phase 3: Fix

1. Smallest diff for confirmed root cause
2. No drive-by refactors

### Phase 4: Verify

1. Re-run reproduction
2. Check callers for blast radius

## Tool discipline

1. Search/narrow before whole-file reads
2. Read only hot paths (signatures → lines range)
3. Do not load unrelated skills

## Install full skill

```bash
npx skills@1.7.4 add obra/superpowers -g --skill systematic-debugging -y --copy
```

Then follow `systematic-debugging/SKILL.md` exclusively.
