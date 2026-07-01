---
name: video-generation-playbook
description: "Pick the right video workflow — launch, Remotion, or HyperFrames. Use when: make a video, promo, explainer, launch clip, render MP4, motion graphic."
---

# Video generation playbook

**Goal:** route to the best video skill — not generative AI footage (Sora/Runway), but **code-rendered** MP4s.

Read first: `playbook-common/references/video-skills-leaderboard.md`

## 0. Quick route

| User intent | Playbook / skill |
|-------------|------------------|
| Brag / launch video for **this repo** | `video-launch-playbook` → **`brag`** |
| Product promo from URL, brief, or script | `video-launch-playbook` → `product-launch-video` |
| PR / changelog / release notes video | `video-launch-playbook` → `pr-to-video` |
| Website tour / portfolio clip | `video-launch-playbook` → `website-to-video` |
| Topic explainer (no product) | `video-launch-playbook` → `faceless-explainer` |
| React video project, data-driven, scale | `video-remotion-playbook` → `remotion-best-practices` |
| Edit custom HyperFrames HTML composition | `hyperframes` entry skill |
| Captions on existing talking-head MP4 | `embedded-captions` |
| Short kinetic type, no narration | `motion-graphics` |

When intent is clear, **read only that playbook or child skill** — do not load Remotion and HyperFrames in parallel.

## 1. Clarify input (max 2 questions)

If unclear, ask:

1. **Input** — current project, product URL, PR link, topic text, existing footage, or Remotion repo?
2. **Output** — shareable launch clip (~15–25s), promo (30–90s), or maintained video codebase?

Defaults unless user says otherwise: **16:9 landscape**, English narration/captions.

## 2. Stack choice

### HyperFrames path (HTML → MP4)

Best for: agent-authored promos, brag, crawled sites, PR explainers.

1. Install if missing: `npx skills add heygen-com/hyperframes -g --all -y --copy`
2. For **this project** launch → `brag` first (narrower, faster than generic PLV)
3. Else read `hyperframes` entry skill — follow its intent router
4. Domain skills on demand: `hyperframes-core`, `hyperframes-animation`, `hyperframes-media`, `hyperframes-cli`

Prereqs: Node 22+, FFmpeg, `npx hyperframes doctor`

### Remotion path (React → MP4)

Best for: parametrized templates, Spotify Wrapped-style, CI renders, existing Remotion repos.

→ `video-remotion-playbook`

### Do not use for

- Browser screen recording → `agent-browser` / manual capture
- UI motion in a web app (not exported video) → `frontend-motion-playbook`
- Marketing copy only (no video) → `marketing-seo-playbook`

## 3. After render

- Share copy / SEO → `marketing-seo-playbook` (`copywriting`, `ai-seo`)
- Ship landing page with video → `frontend-feature-playbook`
- Deploy Remotion Lambda / API → `deploy-playbook` + Remotion deploy rules

## Anti-patterns

- Loading `remotion-best-practices` and `hyperframes` for the same one-off launch clip
- Using `remotion-video-toolkit` when `remotion-best-practices` is installed (official skill wins)
- Picking Sora/Runway when user wants editable, version-controlled video code
