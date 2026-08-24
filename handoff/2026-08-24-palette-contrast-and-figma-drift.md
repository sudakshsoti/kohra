# Handoff — palette contrast pass and Figma drift

**Date:** 2026-08-24
**Branch:** `main` (pushed, clean)
**Commits:** `bd79a0c`, `3c05e5d`, plus this handoff

## Why this session happened

The shipped theme had drifted away from Figma over months of direct JSON
edits. The task was to reconcile Figma to the theme and recompute every
contrast ratio. Along the way `syntax/comment` turned out to be failing
WCAG outright, and the fix pulled in the background ramp.

## What changed and where

### Figma — palette board (`m3bq5i16KVFgk8BF9xiAMD`, node `7:2195`)

Brought fully current against the shipped JSONs. All 25 Kohra swatches
carry live hexes, fresh OKLCH captions and recomputed WCAG badges. The
board's own chrome was warm leftovers (`#0e0d0c` ground, warm-grey text)
and is now on the cool ramp. Primary-syntax rows were reordered by hue
because the section header claims hue order. Section headers corrected.
The Flexoki Dark comparison column was deliberately left untouched.

### Theme files (`bd79a0c`)

Eight files: both VS Code and Cursor themes, Zed, both Sublime files,
Superset, and the hex maps in `.scripts/apply_kohra.py` and
`.scripts/apply_kohra_theme.py`.

| Token | Before | After | Ratio |
|---|---|---|---|
| `bg-editor` | `#0f1214` | `#0b0e10` | base |
| `bg-input` | `#0a0d0f` | `#070a0c` | — |
| `bg-deep` | `#06080a` | `#040608` | — |
| `bg-deepest` | `#030506` | `#020405` | — |
| `syntax/comment` | `#4c5b65` (2.68 fail) | `#54636d` | 3.12 |
| `syntax/comment-doc` | `#5c6c77` | `#64747f` | 4.01 |
| `syntax/comment-em` | `#6d7274` | `#768691` | 5.15 |
| `syntax/operator` + `escape` | `#79736d` | `#6e757a` | 4.14 |

Ghostty was correctly left untouched — it is a terminal and never sat on
the editor plane.

### `AGENTS.md` (`3c05e5d`)

Rewrote the Figma section, fixed four bucket-table rows, added a
"Contrast floor" section and a note on the neutral ramp's bottom, and
documented the cmux port, `assets/` and `sample/`.

## Decisions and why

**Comments are held to WCAG 3.0, not 4.5.** Reaching 4.5 needs L 0.586,
which is brighter than `syntax/operator` at L 0.558 and would invert the
theme's own stated hierarchy of comments as the quietest token. 3.0 is
the large-text floor and the right bar here.

**Darkening the base does not fix contrast.** At these luminances the
WCAG formula is dominated by its `+0.05` floor. Dropping the base from
L 0.180 to L 0.130, nearly black, lifts the comment only from 2.68 to
2.86. The base change was taste; the ramp rebuild was the fix.

**The base landed at L 0.160, not the L 0.150 first recommended.** Four
planes sit below the editor within 0.06 of L. At L 0.150 the editor
would have gone *under* `bg-input`, making input fields lighter than the
editor containing them. Shifting the lower three to compensate produced
rgb(1,2,3) and rgb(3,4,5), which are dead values. L 0.160 with the
bottom re-spaced at even 0.020 steps keeps every plane alive.

**All four bottom planes moved together.** Consequence: `bg-deep` is
Sublime's chrome window background, so Sublime's frame darkened by 0.013.
Accepted as the price of a coherent ramp.

**`#6d7274` was edited surgically, not globally.** It meant both
`comment-em` and `fg_subtle`. Only the `comment.block.documentation` rule
moved; ghost text, inlay hints, `predictive` and `terminal.ansi.dim_white`
still hold the old value deliberately.

**Zed's `editor.line_number` shared the comment hex and followed it up**
to `#54636d`. It was failing at 2.68 too, so this is an improvement, but
it was not explicitly requested — flag it if unwanted.

## Current state

Working tree clean, `main` pushed. No half-done edits. All theme JSONs
parse. `python3 .scripts/apply_kohra.py` re-runs idempotently, replacing
0 hexes; its "unmapped" list is now every Kohra colour, which is expected
after a complete conversion and not a failure.

### Open items, none blocking

1. **The Figma variable collection is stale.** File
   `dtReQGh5lb7Q80BnnPabe0` holds a `Kohra` collection of 89 variables,
   every one still the pre-drift warm palette (`neutral/bg-editor` is
   `#14110e`, `syntax/comment` is `#605749`). `AGENTS.md` now marks it
   stale and says the JSONs win, so nothing will silently revert, but
   Figma is not the source of truth until this is resynced.
2. **`themes/kohra-cmux.jsonc`** still has an install line reading
   `cp themes/kohra-cmux.json`, missing the `c` from the rename in
   `189af7f`. One-character fix.
3. **`sample/showcase.ts`** header prose says lightness and chroma are
   locked with only hue free. That is now imprecise: `syntax-primary`
   holds two locked tiers, L 0.620 and L 0.720.
4. **`herdr` worktrees** came up and were never resolved.
   `herdr worktree create` wraps `git worktree add`, so it only carries
   committed state. Moot now that everything is committed.

## Next action

Resync the 89 variables in the `Kohra` collection of Figma file
`dtReQGh5lb7Q80BnnPabe0` to the shipped palette, reading current values
from `themes/kohra-color-theme.json` and `themes/kohra.zed-theme.json`,
then update the `AGENTS.md` Figma section to drop the stale warning.
