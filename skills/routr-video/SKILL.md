---
name: routr-video
description: "Pick and run the right video workflow — launch, Remotion, or HyperFrames. Use when: make a video, promo, explainer, launch clip, /brag, render MP4, motion graphic, Remotion, product video. Not for: in-app UI animation (→ routr-motion)."
---

# routr-video

**Goal:** route to the best **code-rendered** MP4 workflow — not Sora/Runway generative footage.

## When to activate

- User wants a video, promo, launch clip, explainer
- `/brag`, Remotion, HyperFrames, MP4 export
- PR video, site tour, product promo

## Do not activate

- In-app UI animation (not exported video) → `routr-motion`
- Marketing copy only → `routr-marketing`
- Screen recording → `agent-browser` / manual capture

## Iron law

**Load only one video stack per task — never Remotion + HyperFrames in parallel for a one-off clip.**

## 0. Bootstrap

Install missing from `routr-catalog/references/skill-registry.md` (Video table).

| Order | Skill | Tier |
|-------|-------|------|
| 1 | `brag` | required — same-workspace launch clip |
| 2 | `remotion-best-practices` | required — React/parametric video |
| 3 | `hyperframes` | recommended — entry point once a HyperFrames workflow is chosen |
| 4 | `product-launch-video` | optional — external product URL/brief |
| 5 | `pr-to-video` | optional — GitHub PR / changelog |

If `brag` and `hyperframes` are both missing → read [references/fallback.md](./references/fallback.md).

`hyperframes` may describe itself as the default for any video request. That claim covers stack execution once selected, not workflow selection — see [references/boundaries.md](./references/boundaries.md#precedence-over-self-declared-entry-points). Route from this file first.

**Pre-flight gate (low freedom) — before any render:**

- [ ] Node 22+, FFmpeg on `PATH`
- [ ] `npx hyperframes doctor` clean (HyperFrames path only)
- [ ] A 3–5s smoke render succeeds before the full-length render

Skipping this is the most common way a video task fails late instead of early.

## 1. Quick route

Read [references/launch.md](./references/launch.md) or [references/remotion.md](./references/remotion.md) based on intent.

| User intent | Path |
|-------------|------|
| Brag / launch for **this repo** | launch → `brag` |
| Product promo from URL/brief | launch → `product-launch-video` |
| PR / changelog video | launch → `pr-to-video` |
| React/parametric video codebase | remotion → `remotion-best-practices` |
| HyperFrames HTML composition | launch → `hyperframes` |

Leaderboard: `routr-catalog/references/video-skills-leaderboard.md`

## 2. Clarify (max 2 questions)

If unclear:

1. **Input** — repo, URL, PR, topic text, footage, or Remotion project?
2. **Output** — launch clip (~15–25s), promo (30–90s), or maintained video codebase?

Defaults: **16:9**, English narration/captions, burned-in captions if the audience may watch muted (demo/social).

If there's a hard deadline (demo day, hackathon judging, live event), ask it as a third question and let it override defaults — see [references/gotchas.md](./references/gotchas.md) for the low-time path.

## 3. Execute

Follow the matched reference file only — do not load both stacks.

## 4. Verify (low freedom)

- [ ] Duration matches the target (share clip vs promo vs maintained codebase)
- [ ] Captions present if audience may be muted
- [ ] Aspect ratio matches the destination (16:9 default; 9:16 for social if requested)

## Output format

```markdown
## Video report
**Workflow:** brag / product-launch-video / pr-to-video / hyperframes / remotion-best-practices
**Output:** path to rendered file(s)
**Duration / aspect:** …
**Verified:** yes/no — smoke render + full render both succeeded
```

## Handoff

| Need | Router |
|------|--------|
| Share copy | `routr-marketing` |
| Landing page with embedded video | `routr-frontend` |
| Remotion Lambda deploy | `routr-deploy` |
| Render kept failing | `routr-debug` |

## References

- [launch](./references/launch.md) — brag, HyperFrames promos
- [remotion](./references/remotion.md) — React programmatic video
- [fallback](./references/fallback.md) — when `brag`/`hyperframes` are both missing
- [gotchas](./references/gotchas.md)
- [examples](./references/examples.md)
- [boundaries](./references/boundaries.md)

## Anti-patterns

- `remotion-best-practices` + `hyperframes` for same one-off launch
- Sora/Runway when user wants version-controlled video code
- Skip `npx hyperframes doctor` before first HyperFrames render
- Full-length render before a smoke render confirms the pipeline works
