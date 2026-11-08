# Session Handoff: Obsidian Kohra colour-review fixes, shown in Paper

**Date:** 2026-11-08
**Project:** /Users/sudakshsoti/dev/kohra (this repo). The work targets the Obsidian port at /Users/sudakshsoti/dev/obsidian-kohra-theme.

## Current State

**Task:** An adversarial colour review of the Obsidian port's `theme.css` produced fixes. Show them as "· fixed" frames in Paper beside the current frames, with every change marked. If the user approves the frames, apply the values to `obsidian-kohra-theme/theme.css`.
**Phase:** Review. The frames are built. No theme file has been changed in either repo.
**Progress:**
- Night · fixed is built and checked visually.
- Daybreak · fixed is built. Its sample pins were placed automatically and have not been checked visually.

## What Changed and Where

- **Paper file** `01M6VVHS31B3BBZ1ZY4ZSFBYFS`, page `p-1-0` ("Nimble olive"). Artboards are in one row at top −2580:

| Artboard | id | left |
|---|---|---|
| Kohra — Palette | `1-0` | −347 |
| Kohra — Night (current, untouched) | `CG-0` | 1133 |
| Kohra — Night · fixed | `3FZ-0` | 3293 |
| Kohra — Daybreak (current; only moved) | `1RJ-0` | 5453 |
| Kohra — Daybreak · fixed | `DMP-0` | 7613 |

- **Each fixed frame:** header → "What changed" (Δ1–Δ16 list plus before/after contrast tiles) → neutral ramp → hue buckets → system tokens and values table → samples (Obsidian note, code block, terminal) → "Changes in these samples" legend.
- **Change markers are magenta canvas layers**, because the Paper MCP can't create comments: `#ff4fa3` on Night, `#c4136f` on Daybreak. Each marker is a "Δn" pill, a dashed "was #hex" strip, a ring, and one pinned example per Δ in the samples.
- **`handoff/2026-11-08-obsidian-kohra-fixed-values.json`** (this repo) is the single source for applying the fixes. For each mode it holds `raw` (token → value), `helpers` (`--color-*-hover`), `src`, and `changes` (token → [Δ, old hex]). It also holds the Δ text. It was exported from a Python kernel that no longer exists.
- Identical copies of the handoff and JSON are in `obsidian-kohra-theme/handoff/`, untracked.
- **Uncommitted in this repo:** this file and the JSON. Nothing is committed.
- **Uncommitted in obsidian-kohra-theme:** `design/` and `handoff/` are untracked. `theme.css` is unmodified.

## Decisions Made

- **Full fix only.** The user dropped the "Night · minimal fix" variant and its artboard was deleted.
- **OKLCH is the source.** Obsidian ships hex, but every swatch label shows the authored OKLCH, which converts back to exactly the shipped hex.
  - Night hue buckets are all L 0.720, C 0.075.
  - New Night cyan: `#6bb4ab` = oklch(0.72 0.075 185). It moves cyan from the 0.62 tier to bucket lightness.
  - Daybreak buckets are all L 0.520, with their existing C/H.
  - The Night ramp uses L `[0.180,0.207,0.236,0.277,0.356,0.400,0.480,0.586,0.670,0.762,0.815,0.870,0.935]` at C 0.006 (0.005 for bright), H 240.
  - Earlier readings like 0.720/0.721/0.722 were artefacts of measuring OKLCH back from 8-bit hex.
- **Error keeps its exemption** from bucket lightness and from Lc 60. This matches this repo's rule that error is the only token allowed out of its bucket.
  - It only has to clear WCAG 4.5:1 on the editor, the panel, and the 12% rest wash. The 20% hover wash is not required (user decision).
  - Night error: `#e07878`, oklch(0.69 0.13 21). Worst case is 4.59:1.
  - Daybreak error: `#9a3e3c`, oklch(0.49 0.124 24). Worst case is 4.68:1.
- **The Night text ramp gets the full lift:** body Lc 80, muted Lc 60, faint 4.5:1. Inactive tabs use text-muted.
- **Headings h1–h4 use `--heading-cool`.** Titlebar and ribbon move to base-10.
- **Washes stay `rgba()`, not `color-mix`.** The `-rgb` triplets stay literal numbers.
- **No new variables.** Accent HSL follows the blue bucket.
- **Audit result:** all 42 audited pairs pass in both modes. 56 values change in Night and 81 in Daybreak.

## Open Questions

- [ ] Does the user approve the frames? Applying the changes to `obsidian-kohra-theme/theme.css` (and its README line 31) waits on that.
- [ ] Should any fix carry over to this repo's ports? Two candidates: cyan/`type` at the 0.62 tier, and the Night text ramp. This repo forbids speculative hex changes and treats Figma as the source, so ask first.
- [ ] Residual to tell the user about: accent HSL renders 1 bit off blue because of HSL rounding.

## Context to Remember

- Style: British spelling, no em dashes in prose, colour in OKLCH, APCA as a supplement to WCAG, terse.
- Never add the agent as co-author on commits.
- Paper MCP:
  - `find_nodes` has no name filter; use `textValue`.
  - `set_text_content` takes `textContent` or `html`.
  - Screenshots of tall nodes get downscaled, so screenshot child groups.
  - PIL isn't installed; use `sips`.

## Next Steps

1. [ ] **Next action:** in Paper, screenshot Daybreak · fixed (`DMP-0`) one section at a time. Check the pins and that the "was" strips are readable. Confirm every token in the JSON `changes["Daybreak · fixed"]` has a Δ marker and that no unchanged token has one. Fix marker problems on the canvas only.
2. [ ] Show both fixed frames to the user and ask for approval.
3. [ ] If approved, apply `raw` and `helpers` from the JSON to `obsidian-kohra-theme/theme.css`. Correct its README line 31. Commit in that repo.

## Files to Review on Resume

- `handoff/2026-11-08-obsidian-kohra-fixed-values.json`: the values.
- `/Users/sudakshsoti/dev/obsidian-kohra-theme/theme.css`: the target. Night hues are around line 54; Daybreak hues around line 198.
- `/Users/sudakshsoti/dev/obsidian-kohra-theme/design/decisions.md`: the frame decisions.
- `AGENTS.md` (this repo): the bucket system and the error exemption.
