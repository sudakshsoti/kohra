# Repository instructions

## Kohra

Personal dark colour theme. Single variant, not for marketplace distribution. Targets VS Code (primary), Cursor (parallel theme file in the same extension manifest — Cursor is a VS Code fork and reads the manifest natively), Zed (parallel port), Ghostty (terminal port), Sublime Text (parallel port) and cmux (parallel port). A separate repo, `obsidian-kohra-theme`, ports the same Night palette plus a light Daybreak variant.

Scaffolded from Tokyo Night by Enkia (MIT) — VS Code scope coverage and the extension manifest are inherited. The Sublime Text `.sublime-theme` (chrome — tabs, sidebar, status bar, popups) is scaffolded separately from ayu-mirage by Ike Ku (MIT) and uses ayu's PNG icon assets verbatim. All colour values have been replaced. See `NOTICE` for license texts.

## Design intent

Cool fog-grey monochrome surface with a small set of deliberate syntax colours. The neutral ramp is achromatic with a very slight blue tint (OKLCH H ≈ 240°, C ≈ 0.007) — no warmth. Evokes a winter morning under fog: still, cold, desaturated. Goal is "pleasant over long sessions," not philosophical coherence. No system accent. Comments are the lowest-luminance syntax token.

## Source of truth: Paper → JSON

Since 2026-11-08 the design source is the Paper file `01M6VVHS31B3BBZ1ZY4ZSFBYFS`. Make colour decisions there, then apply them to the theme files. If Paper and the theme files ever disagree, that is drift: reconcile rather than picking a winner.

- **`Kohra · final` page** holds the shipped editor palette: neutral ramp, hue buckets, chrome and state tokens, terminal, each swatch with hex, OKLCH and a WCAG ratio against `neutral/bg-editor`. This is the page to read for the editor ports.
- **Page 1** holds the Obsidian working frames: the current Night and Daybreak artboards, untouched, and the approved `Night · fixed` / `Daybreak · fixed` artboards with their Δ1–Δ16 change markers. `handoff/2026-11-08-obsidian-*.md/.json` record those fixes.
- **Workflow:** colour decisions are made in OKLCH. Never change a hex value speculatively, only when explicitly told the new value, or when conforming a token to its bucket below.
- **MCP access:** the Paper MCP server (`get_basic_info`, `get_children`, `get_jsx` for reads; `write_html`, `update_styles` for writes).
- **Figma is retired.** The `Kohra` palette board (`m3bq5i16KVFgk8BF9xiAMD`) and `Kohra — Color System Tokens` (`dtReQGh5lb7Q80BnnPabe0`) were last reconciled on 2026-08-24 and are stale. Do not read them as authoritative.

## OKLCH bucket system

Every Kohra token belongs to one bucket. Within a bucket, lightness (L) and chroma (C) are locked and only hue varies. This is what makes colours in the same category feel like siblings. `syntax-primary` and `accent-primary` are the exception: they hold two locked tiers rather than one.

Values below are measured from the shipped theme files.

| Bucket | Tokens | L | C |
|---|---|---|---|
| neutral ramp | `neutral/bg-*`, `neutral/fg-*`, `term/black\|white\|bright-black\|bright-white` | per step, 0.103–0.935 (see below) | 0.006 @ H 240 |
| syntax-muted | `syntax/comment`, `comment-doc`, `comment-em` | 0.491 / 0.550 / 0.611, even 0.060 steps | 0.025 @ H≈238° |
| syntax-neutral | `syntax/variable`, `class` | 0.799 | 0.006, held below body text (0.871) so identifiers never outshine the 0.720 hues |
| syntax-faint | `syntax/operator`, `escape` | 0.558 | 0.011 @ H≈239° |
| syntax-primary, dim | `syntax/invalid`, `regex`, `tag-punct` | 0.620 | 0.075 |
| syntax-primary, bright | all other `syntax/*`, including `type` (cyan `#6bb4ab`) | 0.720 | 0.075 |
| accent-primary | `accent/*` base hues and `accent/*-bright` | 0.620 or 0.720 | 0.075 — the same two tiers as syntax-primary |
| accent-dim | `accent/*-muted`, `*-dark` | 0.550 | 0.060 |
| brand | `brand/blue` / `brand/blue-dim` | 0.450 / 0.300 | 0.100 / 0.061 |
| diag | `diag/*` (fg), except error | 0.650 | 0.130 |
| vcs-fg | `vcs/*-fg` | 0.600 | 0.070 |
| vcs-bg | `vcs/*-bg` | 0.249 (matched) | 0.040 |
| term-normal | `term/{red,green,yellow,blue,magenta,cyan}` | 0.600 | 0.100 |
| term-bright | `term/bright-{colour}` | 0.750 | 0.090 |

Neutral ramp steps (chrome and body text): editor `#0b0e10` (0.161), panels `#1c1f21` (0.236), hover and raised `#26292b` (0.277), borders `#393d3f` (0.356), border hover and gutter `#45484b` (0.400), ANSI bright black `#5b5e61` (0.480), faint `#797d7f` (0.586), subtle (ghost text, inlay hints) `#929699` (0.670), muted chrome text `#aeb2b5` (0.762), body `#d1d5d8` (0.871), bright `#e7eaec` (0.935). The four planes below the editor (`#020405`, `#040608`, `#070a0c`) are unchanged.

There is one cyan. The old teal `#70b4a2` (links, preproc, object keys) was merged into `#6bb4ab` on 2026-11-08 because the two sat 10° apart in the same tier. `#4c958c` survives only as the accent dim tier in UI tints (diff inserted, `charts.green`, bracket pair 4), not as a syntax colour.

States: hover is `#26292b`; active and focused selections are `#78accf` at 20% alpha (`#78accf33`), inactive selection 12% (`#78accf1f`), so active always reads stronger than hover. The focus ring is `#78accf` (6.8:1 on panels).

Warning is `#bf801e` in every port. `#c29e70` is the yellow syntax hue, not a warning colour.

There is no live chart bucket. `chart/*` existed only in the retired Figma collection.

Error is the only token allowed out of its bucket. Its foreground `#e07878` sits at L 0.690 / C 0.130, above the diag lightness, so it clears 4.5:1 on its own 10–12% wash over a panel (5.1:1 at worst). `diag/error-bg` `#3f191a` sits at L 0.271 / C 0.060, above the `vcs-bg` plane it would otherwise join, so the error background reads hotter than the VCS tints. Do not conform either.

When extending or rebalancing the palette, classify the new token first, then conform to its bucket's (L, C).

## Contrast floor

Comments are deliberately the quietest tokens and are held to WCAG 2.2 large-text (3.0), not body text (4.5). Pushing `syntax/comment` to 4.5 would put it above `syntax/operator` in lightness and invert the theme's own hierarchy. Measured against `neutral/bg-editor` `#0b0e10`, the three lowest syntax ratios are `syntax/comment` 3.12, `syntax/comment-doc` 4.01 and `syntax/operator` 4.14. Nothing falls below 3.0. Keep it that way.

Two chrome tokens sit under body-text contrast, both known: faint text `#797d7f` is 4.66:1 on the editor but 3.99:1 on panels, and ANSI bright black `#5b5e61` (shell autosuggestions) is 2.97:1 on the VS Code terminal and 2.76:1 on the Ghostty background `#141719`. Both were lifted on 2026-11-08 from roughly 2.6 and 2.0.

## Repo layout

```
themes/kohra-color-theme.json         VS Code theme (JSONC; trailing commas stripped)
themes/kohra-cursor-color-theme.json  Cursor theme — parallel target, byte-identical to the VS Code file today; carved out so Cursor-specific surfaces (ghost text, inline AI diff, composer chrome) can diverge without touching the VS Code variant
themes/kohra.zed-theme.json            Zed theme (v0.2.0 schema)
themes/kohra-ghostty                   Ghostty terminal theme (flat key=value config; 16-colour ANSI palette + bg/fg/cursor/selection). Derived from the Zed terminal palette
themes/kohra.sublime-color-scheme      Sublime Text colour scheme (relaxed JSON; // comments + trailing commas allowed). variables → globals (editor UI) → rules (scope-based syntax). Hexes mirror the VS Code / Zed palette
themes/kohra.sublime-theme             Sublime Text UI theme (chrome — tabs, sidebar, status bar, popups). Scaffolded from ayu-mirage; references PNG icons under kohra-assets/. Texture paths resolve via the `Packages/Kohra/` install symlink
themes/kohra-cmux.jsonc                cmux port (JSONC). Keeps the full cmux template scaffold with only the colour-relevant keys active — app.appearance, workspaceColors, sidebarAppearance, browser.theme — and every other section left commented so it falls back to what is saved in cmux Settings. Colours mirror the Ghostty terminal palette. Install: `cp themes/kohra-cmux.jsonc ~/.config/cmux/cmux.json`
themes/kohra-assets/                   PNG icon set used by kohra.sublime-theme (arrows, close glyph, dirty dot, folder, fold). Lifted verbatim from ayu (MIT, see NOTICE)
assets/kohra-zed.png                   Screenshot of the Zed port, used by README.md
sample/showcase.ts                     Sample file for eyeballing syntax coverage
.scripts/apply_kohra.py                TN→Kohra hex substitution for the VS Code / Cursor JSONC themes; idempotent
.scripts/apply_kohra_theme.py          ayu-mirage→Kohra hex substitution for kohra.sublime-theme; idempotent
package.json                           VS Code / Cursor extension manifest — registers both themes under labels "Kohra" and "Kohra (Cursor)"
NOTICE                                 MIT attribution for Tokyo Night (VS Code scope coverage) and ayu (Sublime theme chrome + icon assets)
```

There is no `reference/`, `token-map.csv`, or `tokens.json` in this repo — those were planned scaffolding from Tokyo Night that didn't survive the rewrite. Don't recreate them unless asked.

## Working with the JSONs

- `themes/kohra-color-theme.json` is JSONC. VS Code's loader accepts comments. Trailing commas have been stripped to satisfy strict linters — keep it that way; if you add a property at the end of an object, do not introduce a trailing comma.
- `themes/kohra.zed-theme.json` is strict JSON (Zed enforces it).
- `.scripts/apply_kohra.py` holds the Tokyo Night → Kohra hex map and applies it to the VS Code theme: `python3 .scripts/apply_kohra.py`. Now that the conversion is complete a clean run replaces 0 hexes and lists every Kohra colour as "unmapped" — that is expected, not a failure. Keep the `M` dict updated when a Kohra value changes so the map stays a usable record of the substitution.

## Rules

- Never change colour values speculatively. Only update a token when explicitly told the new value, or when re-running `.scripts/apply_kohra.py` with an explicit mapping change.
- All colour values go into the JSON as hex. Convert from OKLCH only when explicitly asked.
- Do not add new token entries to the VS Code theme — Tokyo Night's scope coverage is sufficient. Adding tokens to the Paper palette is fine when the design requires it.
- Do not modify `package.json` publisher, name, or version unless asked.

## Testing locally

VS Code / Cursor:

- Symlink or copy this folder into `~/.vscode/extensions/` (or `~/.cursor/extensions/` for Cursor).
- Reload window: `Cmd+Shift+P → Developer: Reload Window`.
- Switch theme: `Cmd+K Cmd+T → Kohra`.

Zed:

- Symlink `themes/kohra.zed-theme.json` into `~/.config/zed/themes/` (e.g. `ln -sf $(pwd)/themes/kohra.zed-theme.json ~/.config/zed/themes/kohra.json`).
- Zed hot-reloads themes; pick **Kohra** from the theme picker.

Ghostty:

- Symlink `themes/kohra-ghostty` into `~/.config/ghostty/themes/` (e.g. `ln -sf $(pwd)/themes/kohra-ghostty ~/.config/ghostty/themes/kohra-ghostty`).
- Set `theme = kohra-ghostty` in `~/.config/ghostty/config`, then reload (`Cmd+Shift+,`).

Sublime Text:

- Symlink the entire `themes/` folder as a Sublime package (texture paths in the theme reference `Kohra/kohra-assets/…`, so the folder must mount at `Packages/Kohra/`):
  `ln -sf $(pwd)/themes ~/Library/Application\ Support/Sublime\ Text/Packages/Kohra`
- Pick the colour scheme: `Cmd+Shift+P → UI: Select Color Scheme → Kohra`.
- Pick the chrome theme: `Cmd+Shift+P → UI: Select Theme → Kohra` (both hot-reload on save).

## Implementation priority

When applying a palette pass: surfaces (backgrounds, UI chrome) → primary text → syntax colours → diagnostics → VCS → terminal. The script handles this implicitly via the hex map, but keep the order in mind when normalising buckets manually.

Surfaces come first because the whole contrast table is measured against `neutral/bg-editor`. Move it and every ratio below it changes. Note that the four planes at the bottom of the neutral ramp (`bg-deepest`, `bg-deep`, `bg-input`, `bg-editor`) sit within 0.06 of L of each other, so the editor background cannot be darkened on its own — the three below it have to move with it or the stack inverts.
