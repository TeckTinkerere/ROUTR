# Video Remotion workflow

Remotion workflow for `routr-video`.

## Bootstrap

| Priority | Skill | When |
|----------|-------|------|
| **1** | `remotion-best-practices` | Always |
| 2 | `remotion-video-toolkit` | Only if official missing |
| 3 | `find-docs` | API edge cases |

```bash
npx skills add remotion-dev/skills@remotion-best-practices -g -y --copy
```

## When Remotion (not launch/HyperFrames)

| Signal | Remotion |
|--------|----------|
| `remotion` package in repo | Yes |
| Thousands of renders from JSON props | Yes |
| Wrapped/Unwrapped data viz pattern | Yes |
| User says Remotion / create-video | Yes |
| One-shot launch from current app | No → launch.md → `brag` |

## New project

```bash
npx create-video@latest --yes --blank --no-tailwind my-video
```

Load `remotion-best-practices` rules progressively — not all 30+ at once.

**Layout first:** `rules/video-layout.md` before scenes.

**Animation default:** `useCurrentFrame()` + `interpolate()`; `spring()` only for physics-like motion.

## Build pass

1. Rules matching current task only
2. Composition, props, `calculateMetadata` if dynamic duration
3. Preview: `npm run dev`
4. Render: `npx remotion render` or Lambda

## Port to HyperFrames

Migration only → `remotion-to-hyperframes`

## Ship

- Pipeline deploy → `routr-deploy`
- Marketing page → `routr-frontend`
- Launch clip from product site → launch.md
