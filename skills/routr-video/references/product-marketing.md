# Product marketing video

A promo sells the product's value. A tour shows the site. **This file is the promo path** — the default for any commercial URL, even when the user only names the site. For a portfolio, blog, docs, or event site shown as-is, go back to [launch.md](./launch.md) and use `website-to-video`.

## Iron law

**Positioning before pixels.** Who is this for, what do they currently do instead, what changes for them? A video without an answer becomes a feature list set to music. If the user cannot answer, route the positioning question to `routr-marketing` first — a two-minute detour that saves a re-render.

## Input modes

`product-launch-video` accepts three, and they change what you must supply:

| Mode | Input | What happens |
|------|-------|--------------|
| Crawl | Product URL | Headless Chrome pulls real screenshots, brand tokens, palette, and type |
| Resolve-and-crawl | Script or brief that *names* the site without linking it | The site is resolved and crawled unless the user opts out |
| No-capture | Script only, or "don't scrape" | No crawl — pick a style preset that supplies palette and design system |

When a script is supplied, ask one thing: is it the **verbatim** voice-over, or a brief to restructure per scene? Getting this wrong wastes the whole render.

## Beat structure

Sweet spot is 30–90s. Under 20s, cut to hook, one proof, CTA.

| Beat | Seconds | Job |
|------|---------|-----|
| Hook | 0–3 | The problem in the viewer's words. No logo yet |
| Stakes | 3–8 | What the current workaround costs them |
| Reveal | 8–15 | The product, named, doing the thing |
| Proof | 15–45 | Two or three concrete capabilities, each with a real screen or number |
| Differentiator | 45–60 | Why this and not the obvious alternative |
| CTA | last 5 | One action, one URL, held long enough to read and type |

The first three seconds carry the whole video on social. If the hook needs the logo to make sense, it is not a hook.

## Channel spec

| Destination | Aspect | Length | Captions | Notes |
|-------------|--------|--------|----------|-------|
| Landing page hero | 16:9 | 30–60s | optional | Often autoplays muted and looped — must read with no audio |
| YouTube / docs | 16:9 | 60–90s | recommended | Room for the differentiator beat |
| LinkedIn / X | 1:1 or 16:9 | 20–45s | **burned in** | Muted autoplay is the norm |
| TikTok / Reels / Shorts | 9:16 | 15–30s | **burned in** | Hook in the first second; safe margins for platform UI |
| Demo day / judging | 16:9 | 60–120s | **burned in** | Judges frequently watch with sound off |

Vertical is not a crop of the horizontal cut. If both are needed, plan the composition for the tighter frame and let the wide version breathe — or budget a second pass.

## Truth gate (low freedom)

Marketing video is outward-facing and hard to retract once posted. Before render:

- [ ] Every metric on screen traces to a real source, with the measurement window stated if it is a rate or a growth number
- [ ] Customer names, logos, and quotes are ones the user confirms they may use
- [ ] Comparison claims against a named competitor are ones the user is willing to defend publicly
- [ ] Pricing, availability, and "coming soon" language matches what actually ships
- [ ] Music and stock imagery are licensed for commercial use — see [media.md](./media.md)

Do not invent a customer quote, a logo wall, or a statistic to fill a beat. Cut the beat instead.

## Publishing

Rendering is not publishing. Posting the video to a public channel is the user's call, every time — hand them the file and the copy, and let them press the button.

## Handoff

| Next | Router |
|------|--------|
| Headline, description, share copy, distribution plan | `routr-marketing` |
| Embed on the landing page | `routr-frontend` |
| App store preview video | `routr-marketing` for the listing, `routr-mobile` for the build |
| Variants per segment, region, or account | [data-video.md](./data-video.md) |
