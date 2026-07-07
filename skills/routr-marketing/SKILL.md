---
name: routr-marketing
description: "Marketing copy, SEO audits, and growth content. Use when: landing copy, SEO, meta tags, ads, CRO, App Store listing, blog post, growth. Not for: building the landing page UI (→ routr-frontend)."
---

# routr-marketing

**Goal:** copy and SEO that converts.

## 0. Bootstrap

See `routr-catalog/references/skill-registry.md`:

| Skill | When |
|-------|------|
| `seo-audit` | Technical + programmatic SEO (templated pages at scale) |
| `copywriting` | Headlines, CTAs, paid-ad creative |
| `ai-seo` | AI search visibility |
| `aso` | App store listings |

```bash
npx skills add coreyhaines31/marketingskills -g --all -y --copy
```

## 1. Goal routing

| Goal | Lead skill |
|------|------------|
| Rankings | `seo-audit` |
| Landing copy | `copywriting` + `routr-frontend` |
| App store | `aso` |
| LLM citations | `ai-seo` |

## 2. Ship with product

Page UI → `routr-frontend` after copy approved. Mobile store → `routr-mobile` + `aso`.

## Handoff

- Implement site → `routr-frontend`
- Deploy/optimize → `routr-deploy`
- Tracking bug → `routr-debug`

## Anti-patterns

- Keyword stuffing without user value
- Copy before audience and positioning context is defined
