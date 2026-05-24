# Kohra

A personal cool fog-grey monochrome dark theme. Single variant, not packaged for distribution. The name is Hindi for fog, which is the surface.

## Concept

Every token in Kohra belongs to a bucket. Inside each bucket, lightness and chroma are locked in OKLCH; only hue varies. Keywords don’t shout over types, strings don’t dominate functions, comments recede uniformly. Tokens of the same role read as siblings because they are siblings in perceptual coordinates. Diagnostics break the rule on purpose — they have to interrupt.

The chromatic identity is cold and still — a winter morning under fog, not a stylistic substitution. No system accent.

For the long-form version — why OKLCH, the full bucket table, cross-editor parity notes, and what would change in a second run — see the case study at [sudaksh.io/projects/kohra](https://www.sudaksh.io/projects/kohra). Full coordinate reference for every variable lives in [`CLAUDE.md`](./CLAUDE.md).

## Implementations

Five implementations track the same Figma source of truth.

| Editor       | File                                                                          |
| ------------ | ----------------------------------------------------------------------------- |
| VS Code      | `themes/kohra-color-theme.json`                                               |
| Cursor       | `themes/kohra-cursor-color-theme.json` (byte-identical to VS Code today)      |
| Zed          | `themes/kohra.zed-theme.json`                                                 |
| Ghostty      | `themes/kohra-ghostty`                                                        |
| Sublime Text | `themes/kohra.sublime-color-scheme` + `themes/kohra.sublime-theme` (+ assets) |

## Install

VS Code: symlink the repo into `~/.vscode/extensions/`, reload the window, switch theme via Cmd+K Cmd+T, pick **Kohra**.

Cursor: symlink the repo into `~/.cursor/extensions/`, reload the window, pick **Kohra (Cursor)**.

Zed: symlink `themes/kohra.zed-theme.json` into `~/.config/zed/themes/`, then pick Kohra from the theme picker.

Ghostty: symlink `themes/kohra-ghostty` into `~/.config/ghostty/themes/`, set `theme = kohra-ghostty` in your config, and reload.

Sublime Text: symlink the `themes/` folder as a package at `Packages/Kohra` (the chrome theme references its icon assets by relative path), then pick **Kohra** from both `UI: Select Color Scheme` and `UI: Select Theme`.

## What this is not

Not a marketplace product. Not a fully balanced system across multiple modes; there is no light variant and one is not planned. Not WCAG or APCA certified; contrast was tuned by eye against the editor surface and held above Lc 60 for body syntax, Lc 45 for muted tokens, but every grader will have a token they want to push.

## Provenance

Scaffolded from Tokyo Night by Enkia, MIT licensed. The VS Code extension manifest and full scope coverage are inherited; every colour value has been replaced. The Sublime Text chrome theme and its icon assets are scaffolded separately from ayu-mirage by Ike Ku, also MIT. License remains MIT (see `LICENSE.txt`); third-party attribution is in `NOTICE`.
