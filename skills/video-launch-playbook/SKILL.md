---
name: video-launch-playbook
description: "Shareable launch and promo videos via brag and HyperFrames. Use when: /brag, launch video, product promo, PR video, site tour, explainer."
---

# Video launch playbook

**Goal:** a polished **shareable MP4** — launch clips, promos, PR videos, site tours.

Leaderboard: `playbook-common/references/video-skills-leaderboard.md`

## 0. Bootstrap

| Priority | Skill | When |
|----------|-------|------|
| **1** | `brag` | User built **this project** and wants a launch / brag clip |
| 2 | `product-launch-video` | Product URL, brief, or script — marketed product |
| 3 | `pr-to-video` | GitHub PR URL or `owner/repo#N` |
| 4 | `website-to-video` | General site tour (not product launch framing) |
| 5 | `faceless-explainer` | Topic / article — no product, no URL capture |
| 6 | `motion-graphics` | Short unnarrated kinetic hit (&lt;10s) |
| 7 | `embedded-captions` | Caption existing talking-head footage |

```bash
npx skills add latent-spaces/brag@brag -g -y --copy
npx skills add heygen-com/hyperframes -g --all -y --copy
```

Prereqs: Node 22+, FFmpeg, `npx hyperframes doctor` (and `npx hyperframes auth login` if needed).

## 1. Route (most specific wins)

```
Input?
├─ Current repo / "brag about this" / just shipped     → brag
├─ Product being marketed (URL, brief, script)       → product-launch-video
├─ GitHub PR                                         → pr-to-video
├─ General website → video (tour, portfolio)         → website-to-video
├─ Explain topic from text                           → faceless-explainer
├─ Existing MP4 → captions                           → embedded-captions
└─ Short motion-only graphic                         → motion-graphics
```

**brag vs product-launch-video:** If the video is about **the codebase in this workspace**, use `brag`. If it's about an **external product URL** or a **script-first** promo, use `product-launch-video`.

## 2. brag pass (default for "make a launch video")

1. Read `brag/SKILL.md` in full
2. Parse tone (`--tone`), format (`vertical` / `landscape`), duration
3. Output → `brag-output/` with plan, brief, `brag.mp4`, share copy
4. brag owns story; HyperFrames renders — do not hand-author composition unless brag delegates

**Triggers:** `/brag`, "let's brag", "launch video for what we built", "turn this into a share clip"

## 3. HyperFrames workflow pass

When not brag, read `hyperframes/SKILL.md` and follow the matched workflow skill only:

| Workflow | Trigger examples |
|----------|------------------|
| `product-launch-video` | "promo for our SaaS", "60s launch from this URL" |
| `pr-to-video` | "video for this PR", changelog, release notes |
| `website-to-video` | "turn homepage into a clip" |
| `faceless-explainer` | "explain DNS in a video" |
| `embedded-captions` | "add subtitles to interview.mp4" |
| `motion-graphics` | "5s stat animation", logo sting |

Install single workflow: `npx skills add heygen-com/hyperframes --skill pr-to-video -g -y --copy`

## 4. Share and ship

1. Use share copy from brag or workflow output
2. Landing page / meta → `marketing-seo-playbook`
3. Embed on marketing site → `frontend-feature-playbook`

## Handoff

- Parametric React video at scale → `video-remotion-playbook`
- Custom multi-scene HyperFrames edit → `hyperframes` + `general-video`
- Unclear video type → `video-generation-playbook`

## Anti-patterns

- `product-launch-video` when `brag` fits (same repo, no external URL needed)
- Scraping a site when user only has notes → `faceless-explainer`
- Skipping `npx hyperframes doctor` before first render
