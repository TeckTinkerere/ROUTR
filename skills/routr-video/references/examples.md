# Video examples

Input → expected routing behavior.

## 1. Brag

**Input:** "/brag about this project"

**Expected:** launch.md → `brag` only. No HyperFrames entry skill, no Remotion.

## 2. Per-record variants

**Input:** "Video from this JSON with thousands of variants"

**Expected:** data-video.md → the N-videos-one-template shape → remotion.md → `remotion-best-practices`. Props schema and a metadata function; batch render handed to `routr-deploy`.

## 3. Product promo from a URL

**Input:** "60s promo from our SaaS homepage"

**Expected:** product-marketing.md → `product-launch-video` in crawl mode. Positioning confirmed before the script. Not `website-to-video` — the site is commercial.

## 4. Site tour

**Input:** "Turn my portfolio site into a short video"

**Expected:** launch.md → `website-to-video`. Non-commercial site shown as-is, not a promo.

## 5. Script with no site

**Input:** "Here's my script, make a launch video, don't scrape anything"

**Expected:** product-marketing.md → `product-launch-video` in no-capture mode. Ask once whether the script is verbatim voice-over or a brief to restructure. A style preset supplies the palette.

## 6. Metrics recap

**Input:** "Make a video of our Q3 numbers from this CSV"

**Expected:** data-video.md → one-video-real-numbers shape → HyperFrames with variables. Every figure traced to the CSV, as-of date on screen. Not a Remotion project — the render does not repeat.

## 7. Avatar presenter

**Input:** "I want a presenter reading this announcement"

**Expected:** media.md → sign-in preflight relayed and stopped on → HeyGen avatar video via the CLI, script-driven. Then packaged with `embedded-captions` or `talking-head-recut`. Cost confirmed before the paid call.

## 8. Captions only

**Input:** "Add subtitles to this MP4"

**Expected:** launch.md → `embedded-captions`. Footage untouched. Not `talking-head-recut` — no designed overlay cards were asked for.

## 9. Deck, not video

**Input:** "Build me a pitch deck with presenter mode"

**Expected:** `slideshow`. The deliverable is a navigable deck; do not render an MP4.

## 10. Boundary — in-app motion

**Input:** "Make the hero section animation feel more alive"

**Expected:** `routr-motion`. No exported video, so `routr-video` never activates.

## 11. Boundary — screen recording

**Input:** "Just record my screen walking through the app"

**Expected:** No router. Manual screen capture is out of scope.
