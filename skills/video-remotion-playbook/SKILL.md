---
name: video-remotion-playbook
description: "React/Remotion programmatic video — animations, captions, Lambda. Use when: Remotion, create-video, MP4 from React, parametrized video, Wrapped-style."
---

# Video Remotion playbook

**Goal:** correct **Remotion** (React + TypeScript) video code — not HyperFrames HTML compositions.

Leaderboard: `playbook-common/references/video-skills-leaderboard.md` (#1: `remotion-best-practices` at 401K+ installs)

## 0. Bootstrap

| Priority | Skill | When |
|----------|-------|------|
| **1** | `remotion-best-practices` | Always — official Remotion agent skill |
| 2 | `remotion-video-toolkit` | Only if official skill missing (671 installs, alternate rules) |
| 3 | `find-docs` | Remotion API edge cases via Context7 |

```bash
npx skills add remotion-dev/skills@remotion-best-practices -g -y --copy
```

Optional fallback:

```bash
npx skills add shreefentsar/remotion-video-toolkit@remotion-video-toolkit -g -y --copy
```

## 1. When Remotion (not HyperFrames / brag)

| Signal | Remotion |
|--------|----------|
| Existing `remotion` / `video` package in repo | Yes |
| Thousands of personalized renders from JSON props | Yes |
| Spotify Wrapped / GitHub Unwrapped pattern | Yes |
| User says "Remotion" or "create-video" | Yes |
| One-shot launch clip from current app | No → `video-launch-playbook` → `brag` |
| Crawl product URL for promo | No → `product-launch-video` |

## 2. New project

Empty folder — scaffold per child skill:

```bash
npx create-video@latest --yes --blank --no-tailwind my-video
```

Then read `remotion-best-practices` rules **progressively** (captions, audio, layout, etc.) — do not load all 30+ rule files at once.

**Layout first:** load `rules/video-layout.md` before designing scenes.

**Animation default:** `useCurrentFrame()` + `interpolate()`; use `spring()` only for physics-like motion.

## 3. Build pass

1. `remotion-best-practices/SKILL.md` — load rules matching current task only
2. Composition structure, props, `calculateMetadata` if duration is dynamic
3. Captions → captions rules; 3D → Three.js rules; charts → chart rules
4. Preview: `npm run dev` (Remotion Studio)
5. Render: `npx remotion render` or Lambda per project setup

## 4. Port to HyperFrames

User wants to **migrate** Remotion → HyperFrames (not new work):

→ `remotion-to-hyperframes` skill (one-way port)

## 5. Ship

- Deploy render pipeline → `deploy-playbook` + Remotion Lambda / Vercel docs
- Marketing page with embedded video → `frontend-feature-playbook`
- Launch clip from product site (not Remotion codebase) → `video-launch-playbook`

## Anti-patterns

- Using Remotion for a 15s "brag" when `brag` + HyperFrames is faster
- Installing `remotion-video-toolkit` alongside official skill (pick one)
- `spring()` everywhere — prefer `interpolate()` + `Easing.bezier()`
