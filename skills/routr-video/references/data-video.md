# Data-driven video

Content whose subject is the data: metrics recaps, year-in-review, per-customer summaries, changelog stats, benchmark results, dashboards in motion. Two distinct shapes — decide which before choosing a stack.

| Shape | Meaning | Stack |
|-------|---------|-------|
| **One video, real numbers** | A single piece whose content happens to be data | HyperFrames — see [hyperframes.md](./hyperframes.md) |
| **N videos, one template** | The same composition rendered per row, user, or account | Remotion — see [remotion.md](./remotion.md) |

The dividing line is not the amount of data, it is whether the *render* repeats. Ten metrics in one clip is the first shape. One metric across ten thousand users is the second.

## Iron law

**No number reaches the screen without a source.** Every figure traces to a file, query, or API response you actually read. If a beat needs a number nobody has, cut the beat — do not estimate, round up, or invent a plausible one.

## Data prep — before any composition work

1. **Pull the real data first.** Query, export, or fetch it, and write it to a file the composition reads. A hardcoded number in the markup drifts the moment the data does.
2. **Freeze and date it.** Snapshot the dataset used for this render and put the as-of date on screen or in the description. A recap with a live query behind it is unreproducible.
3. **Decide the shape once.** One record per scene, or one metric per scene? Mixing them mid-video reads as chaos.
4. **Check the ugly rows.** Zero, negative, null, a single-item list, a name three times longer than the layout allows, a 7-digit number where the design assumed 3. These break batch renders at row 4,000 — the happy path never does.
5. **Pick honest scales.** Truncated axes, uneven time buckets, and percentage-of-percentage framing are the three ways a data video misleads without a single false statement.

## Per-record renders — the Remotion path

This is what Remotion is uniquely good at, and it is why "thousands of variants" always routes here.

- Type the props with a schema so a bad row fails at validation, not at frame 900.
- Compute duration, dimensions, and derived props from the data rather than hardcoding — a metadata function can fetch and return duration, size, and props together. A recap whose length does not follow its content will either cut off or pad with dead air.
- Test with the extremes from step 4 before the batch, not the median row.
- Render the batch in the cloud, not on a laptop: `routr-deploy` owns the pipeline once it is more than a one-off.
- Cache the fetch. Thousands of renders each hitting your API is a self-inflicted outage.

## Single data video — the HyperFrames path

- Parametrize with the composition-variables mechanism and render with the variables flag; add the strict-variables flag so an undeclared key fails the render instead of silently rendering blank.
- `hyperframes-registry` ships chart blocks — install one rather than hand-rolling an SVG chart.
- `hyperframes-animation` has a count-up blueprint for numbers; `hyperframes-creative` has a stats-and-infographic reference for how dense a data frame should be.

## Motion rules for numbers

- Count-ups earn attention once, maybe twice per video. Every stat counting up is noise.
- Hold a number long enough to read it: roughly one second per stat, plus reading time for the label. Viewers cannot scrub.
- Animate one dimension at a time — a bar that grows while the frame also pans reads as neither.
- Label the unit and the period on the same frame as the number. A viewer who reads "412" and has to infer the unit has lost the sentence.
- Round consistently across the video. Mixed precision looks like sloppiness, which reads as untrustworthy data.

## Verify

- [ ] Every on-screen figure traced back to the source data
- [ ] As-of date present, dataset snapshot saved
- [ ] Edge-case rows rendered and eyeballed, not just the median
- [ ] Axis scales and time buckets are honest
- [ ] Batch path: a sample of the actual output checked, not just an exit code

## Handoff

| Next | Router |
|------|--------|
| The query or export feeding the video | `routr-database` |
| Batch render pipeline, cloud deploy | `routr-deploy` |
| Positioning and distribution of the recap | `routr-marketing` |
| A dashboard instead of a video | `routr-frontend` |
