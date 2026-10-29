# Frontend fallback (no frontend-design installed)

Use when `frontend-design` and `routr-depth-frontend` unavailable.

## Minimum design rules

1. **Subject first** — name audience and page job before picking colors
2. **Avoid default AI clusters** unless brief requires them:
   - Warm cream + terracotta accent + serif display
   - Near-black + single acid-green accent
   - Newspaper columns + hairline rules everywhere
3. **Typography** — pair display + body deliberately; set explicit scale
4. **One signature** — one bold element; keep rest disciplined
5. **Responsive** — mobile layout required
6. **a11y** — focus visible, reduced motion respected

## Token starter (adapt to subject)

Pick 4–6 named colors with roles (bg, surface, text, accent, muted) — do not copy defaults above without justification.

## Install full skill

```bash
npx skills@1.7.4 add anthropics/skills@frontend-design -g -y --copy
```
