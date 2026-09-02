# Video fallback (no child skills installed)

Use when neither `brag` nor `hyperframes` is installed and there's no time to run the install command first (e.g. offline, sandboxed, or mid-deadline).

## Iron law

```
NEVER LOAD REMOTION + HYPERFRAMES IN PARALLEL FOR A ONE-OFF CLIP
```

## Minimum process

1. **Confirm the toolchain exists** — Node 22+, FFmpeg on `PATH`. Without both, there is no code-rendered path; say so and stop rather than guessing at a workaround.
2. **Pick the simplest stack that fits:**
   - Current repo, no React video project → hand-authored HTML/CSS composition, captured with headless Chromium + `ffmpeg` frame-stitching (the same primitive `brag`/HyperFrames build on).
   - Existing `remotion` package in the repo → use its own `npm run dev` / `npx remotion render` directly; do not scaffold a new toolchain.
3. **Smoke render first** — 3–5s of the real composition, full pipeline (render → encode → play back). Confirms the toolchain before spending time on content.
4. **Keep scope small** — one scene, one duration target, no dynamic props system. This is a stopgap, not a maintained video codebase.
5. **Verify** — play back the rendered file; check duration and aspect ratio against the target.

## When stuck

- Render fails silently → check FFmpeg exit code directly, not just the wrapping tool's output
- No FFmpeg available and can't install → captions-only or stills fallback (see `references/gotchas.md`)
- Ask the user for deadline and destination (Devpost, YouTube, social) — these set aspect ratio and duration harder than any default

## Escalate to install

```bash
npx skills add latent-spaces/brag@brag heygen-com/hyperframes -g -y --copy
npx skills add remotion-dev/skills@remotion-best-practices -g -y --copy
```
