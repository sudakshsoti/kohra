# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Kohra

Personal dark colour theme. Single variant, not for marketplace distribution. Targets VS Code (primary), Cursor (parallel theme file in the same extension manifest — Cursor is a VS Code fork and reads the manifest natively), Zed (parallel port), Ghostty (terminal port), and eventually Sublime Text.

Scaffolded from Tokyo Night by Enkia (MIT) — scope coverage and the VS Code extension manifest are inherited. All colour values have been replaced.

## Design intent

Cool fog-grey monochrome surface with a small set of deliberate syntax colours. The neutral ramp is achromatic with a very slight blue tint (OKLCH H ≈ 240°, C ≈ 0.005) — no warmth. Evokes a winter morning under fog: still, cold, desaturated. Goal is "pleasant over long sessions," not philosophical coherence. No system accent. Comments are the lowest-luminance syntax token.

## Source of truth: Figma → JSON

The Figma file is the design source; the theme JSONs are the implementation target.

- **Figma file:** `Kohra — Color System Tokens` (key `dtReQGh5lb7Q80BnnPabe0`) holds three variable collections — `Tokyo Night`, `Flexoki Dark`, and `Kohra` — all under a single "Dark" mode. The `Kohra` collection (89 colour variables) is the live palette and was last normalised on 2026-05-13.
- **Workflow:** colour decisions are made in Figma in OKLCH. Hex values are exported into the theme JSONs only after a change is approved visually. Never change a hex value speculatively — only when explicitly told the new value.
- **MCP access:** the Figma file is reachable via the Figma MCP server (`mcp__claude_ai_Figma__use_figma` for writes, `get_variable_defs` for reads). Use these tools to inspect or update the Kohra collection rather than editing JSON directly when a hue change is in play.

## OKLCH bucket system

Every Kohra variable belongs to one bucket. Within a bucket, lightness (L) and chroma (C) are locked; only hue varies. This is what makes colours in the same category feel like siblings.

| Bucket | Tokens | L | C |
|---|---|---|---|
| neutral ramps | `neutral/bg-*`, `neutral/fg-*`, `term/black\|white\|bright-*` | preserved per step | 0.007 @ H≈240° |
| syntax-muted | `syntax/comment*` | preserved per step | 0.025 |
| syntax-neutral | `syntax/variable`, `class` | 0.78 | 0.012 |
| syntax-faint | `syntax/operator`, `escape` | 0.56 | 0.012 |
| syntax-primary | other `syntax/*` | 0.62 | 0.075 |
| accent-primary | `accent/*` base hues | 0.62 | 0.075 |
| accent-dim | `accent/*-muted`, `*-dark` | 0.55 | 0.06 |
| accent-bright | `accent/*-bright` | 0.72 | 0.075 |
| brand | `brand/blue` / `brand/blue-dim` | 0.45 / 0.30 | 0.10 / 0.06 |
| diag | `diag/*` (fg) | 0.65 | 0.13 |
| vcs-fg | `vcs/*-fg` | 0.60 | 0.07 |
| vcs-bg | `vcs/*-bg` | 0.25 (matched) | 0.04 |
| term-normal | `term/{red,green,yellow,blue,magenta,cyan}` | 0.60 | 0.10 |
| term-bright | `term/bright-{color}` | 0.75 | 0.09 |
| chart | `chart/*` | 0.65 | 0.11 |

When extending or rebalancing the palette, classify the new token first, then conform to its bucket's (L, C).

## Repo layout

```
themes/kohra-color-theme.json         VS Code theme (JSONC; trailing commas stripped)
themes/kohra-cursor-color-theme.json  Cursor theme — parallel target, byte-identical to the VS Code file today; carved out so Cursor-specific surfaces (ghost text, inline AI diff, composer chrome) can diverge without touching the VS Code variant
themes/kohra.zed-theme.json            Zed theme (v0.2.0 schema)
themes/kohra-ghostty                   Ghostty terminal theme (flat key=value config; 16-colour ANSI palette + bg/fg/cursor/selection). Derived from the Zed terminal palette
.scripts/apply_kohra.py                TN→Kohra hex substitution; idempotent; rewrites both JSONC files in one pass
package.json                           VS Code / Cursor extension manifest — registers both themes under labels "Kohra" and "Kohra (Cursor)"
```

There is no `reference/`, `token-map.csv`, or `tokens.json` in this repo — those were planned scaffolding from Tokyo Night that didn't survive the rewrite. Don't recreate them unless asked.

## Working with the JSONs

- `themes/kohra-color-theme.json` is JSONC. VS Code's loader accepts comments. Trailing commas have been stripped to satisfy strict linters — keep it that way; if you add a property at the end of an object, do not introduce a trailing comma.
- `themes/kohra.zed-theme.json` is strict JSON (Zed enforces it).
- `.scripts/apply_kohra.py` holds the Tokyo Night → Kohra hex map and applies it to the VS Code theme. Re-run after any palette change in the Kohra Figma collection: `python3 .scripts/apply_kohra.py`. The script reports unmapped hexes — add them to the `M` dict and re-run.

## Rules

- Never change colour values speculatively. Only update a token when explicitly told the new value, or when re-running `.scripts/apply_kohra.py` with an explicit mapping change.
- All colour values go into the JSON as hex. Convert from OKLCH only when explicitly asked.
- Do not add new token entries to the VS Code theme — Tokyo Night's scope coverage is sufficient. Adding rows to the Kohra Figma collection is fine when the design requires it.
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

## Implementation priority

When applying a palette pass: surfaces (backgrounds, UI chrome) → primary text → syntax colours → diagnostics → VCS → terminal → charts. The script handles this implicitly via the hex map, but keep the order in mind when normalising buckets manually in Figma.
