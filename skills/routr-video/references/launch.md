# Video launch workflow

Launch-video workflow for `routr-video`.

## Bootstrap

| Priority | Skill | When |
|----------|-------|------|
| **1** | `brag` | Launch clip for **this workspace** |
| 2 | `product-launch-video` | External product URL or script |
| 3 | `pr-to-video` | GitHub PR |
| 4 | `website-to-video` | Site tour |
| 5 | `faceless-explainer` | Topic only |
| 6 | `motion-graphics` | Short kinetic (&lt;10s) |
| 7 | `embedded-captions` | Caption existing footage |

```bash
npx skills add latent-spaces/brag@brag heygen-com/hyperframes -g -y --copy
```

Prereqs: Node 22+, FFmpeg, `npx hyperframes doctor`

## Route tree

```
Input?
├─ Current repo / "brag" / just shipped     → brag
├─ Product URL / brief / script             → product-launch-video
├─ GitHub PR                                → pr-to-video
├─ Website tour                             → website-to-video
├─ Topic text                               → faceless-explainer
├─ Existing MP4 → captions                  → embedded-captions
└─ Motion-only graphic                      → motion-graphics
```

**brag vs product-launch-video:** Same workspace → `brag`. External product URL → `product-launch-video`.

## brag pass

1. Read `brag/SKILL.md`
2. Parse tone, format, duration
3. Output → `brag-output/` (plan, brief, `brag.mp4`, share copy)

## HyperFrames pass

Read `hyperframes/SKILL.md`; follow matched workflow skill only.

## Share and ship

1. Share copy from output
2. Landing → `routr-frontend`
3. SEO → `routr-marketing`
