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

## 0. Quick route

Read [references/launch.md](./references/launch.md) or [references/remotion.md](./references/remotion.md) based on intent.

| User intent | Path |
|-------------|------|
| Brag / launch for **this repo** | launch → `brag` |
| Product promo from URL/brief | launch → `product-launch-video` |
| PR / changelog video | launch → `pr-to-video` |
| React/parametric video codebase | remotion → `remotion-best-practices` |
| HyperFrames HTML composition | launch → `hyperframes` |

Leaderboard: `routr-catalog/references/video-skills-leaderboard.md`

## 1. Clarify (max 2 questions)

If unclear:

1. **Input** — repo, URL, PR, topic text, footage, or Remotion project?
2. **Output** — launch clip (~15–25s), promo (30–90s), or maintained video codebase?

Defaults: **16:9**, English narration/captions.

## 2. Execute

Follow the matched reference file only — do not load both stacks.

## 3. After render

- Share copy → `routr-marketing`
- Landing with video → `routr-frontend`
- Remotion Lambda deploy → `routr-deploy`

## References

- [launch](./references/launch.md) — brag, HyperFrames promos
- [remotion](./references/remotion.md) — React programmatic video
- [gotchas](./references/gotchas.md)
- [examples](./references/examples.md)
- [boundaries](./references/boundaries.md)

## Anti-patterns

- `remotion-best-practices` + `hyperframes` for same one-off launch
- Sora/Runway when user wants version-controlled video code
- Skip `npx hyperframes doctor` before first HyperFrames render
