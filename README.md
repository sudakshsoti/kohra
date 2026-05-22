# Kohra

A personal cool fog-grey monochrome dark theme. Single variant, not packaged for distribution. The name is Hindi for fog, which is the surface.

## Concept

The discipline is perceptual uniformity within categories. Every token in Kohra belongs to a bucket, and inside each bucket lightness and chroma are locked in OKLCH; only hue varies. Keywords don't shout over types, strings don't dominate functions, comments recede uniformly. Tokens of the same role read as siblings because they are siblings in perceptual coordinates.

The surface ramp runs six steps from L 0.11 to 0.26, hue locked around 230 to 240 degrees, chroma at 0.006. Text runs eight steps from L 0.38 to 0.88 on the same low-chroma cool axis. The neutral ramp is achromatic with only a faint blue tint — no warmth anywhere in the chrome. Syntax primary (keyword, string, function, type, tag, number, parameter) sits at L 0.62 chroma 0.075. Comments at chroma 0.025, graded by lightness, and held as the lowest-luminance syntax token so they sink into the surface. Variables and classes read as near-neutral grey at L 0.78 chroma 0.012. Operators fade further. Diagnostics break the rule on purpose: error, warning, info, and hint sit at chroma 0.13 because they have to interrupt.

The chromatic identity is cold and still — a winter morning under fog, not a stylistic substitution. Where Tokyo Night runs saturated blue-purple, Kohra runs muted dusk-blue, teal, cyan, faded purple, and a desaturated green and amber held back toward grey. Hues were picked for visual comfort over long reading sessions, not strict colour-wheel logic. There is no system accent, nothing shouts to remind you it is the brand colour.

Five implementations track the same Figma source of truth: a VS Code theme at `themes/kohra-color-theme.json`, a Cursor-targeted parallel at `themes/kohra-cursor-color-theme.json` (currently byte-identical; carved out so Cursor-specific surfaces can diverge), a Zed v0.2.0 theme at `themes/kohra.zed-theme.json`, a Ghostty terminal theme at `themes/kohra-ghostty`, and a Sublime Text colour scheme and chrome theme at `themes/kohra.sublime-color-scheme` and `themes/kohra.sublime-theme`.

## Install

VS Code: symlink the repo into `~/.vscode/extensions/`, reload the window, switch theme via Cmd+K Cmd+T, pick **Kohra**.

Cursor: symlink the repo into `~/.cursor/extensions/`, reload the window, pick **Kohra (Cursor)**. Cursor is a VS Code fork and reads the same manifest, so the plain **Kohra** label also works — the Cursor-labelled variant exists so the file can drift independently if Cursor-specific tokens (ghost text, inline AI diff, composer chrome) need separate tuning.

Zed: symlink `themes/kohra.zed-theme.json` into `~/.config/zed/themes/`, then pick Kohra from the theme picker.

Ghostty: symlink `themes/kohra-ghostty` into `~/.config/ghostty/themes/`, set `theme = kohra-ghostty` in your config, and reload.

Sublime Text: symlink the `themes/` folder as a package at `Packages/Kohra` (the chrome theme references its icon assets by relative path), then pick **Kohra** from both `UI: Select Color Scheme` and `UI: Select Theme`.

## What this is not

Not a marketplace product. Not a fully balanced system across multiple modes; there is no light variant and one is not planned. Not WCAG or APCA certified; contrast was tuned by eye against the editor surface and held above Lc 60 for body syntax, Lc 45 for muted tokens, but every grader will have a token they want to push.

## Provenance

Scaffolded from Tokyo Night by Enkia, MIT licensed. The VS Code extension manifest and full scope coverage are inherited; every colour value has been replaced. The Sublime Text chrome theme and its icon assets are scaffolded separately from ayu-mirage by Ike Ku, also MIT. The OKLCH bucket system that drives every value is documented in `CLAUDE.md`. License remains MIT (see `LICENSE.txt`); third-party attribution is in `NOTICE`.
