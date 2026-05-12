# TODO

## Sync Figma `Kohra` collection to the L 0.72 syntax-primary lift

The JSON themes were bumped from L 0.62 → L 0.72 in commit `68d3f59`, but the Figma file (`Kohra — Color System Tokens`, key `dtReQGh5lb7Q80BnnPabe0`) still holds the old L 0.62 values for the syntax-primary bucket. Update so Figma remains the source of truth.

Variables to update in the `Kohra` collection (Dark mode), all at **L 0.72, C 0.075**, hue preserved:

| Variable (hue) | Old hex | New hex |
|---|---|---|
| purple — h ≈ 295° | `#897daf` | `#a89ccf` |
| red — h ≈ 19° | `#af7474` | `#d09292` |
| orange-yellow — h ≈ 72° | `#a27f52` | `#c29e70` |
| blue — h ≈ 239° | `#598dae` | `#78accf` |
| green — h ≈ 122° | `#7f8e5a` | `#9cad77` |
| warm-orange — h ≈ 48° | `#ab795c` | `#cc977b` |

Also update the bucket spec line in `CLAUDE.md` once Figma is normalised: the `syntax-primary` row in the OKLCH bucket table should read `L 0.72, C 0.075` (currently `0.62`). Same for `accent-primary` if it's promoted in lockstep — decide after a few days of using the new values.

## Maybe lift lightness further after testing

L 0.72 is the conservative jump that gets WCAG to ~7.5:1 and APCA to body-reading band. After living with it for a session or two, evaluate whether to push higher:

- **L 0.75** — closer to `accent-bright` ceiling. Higher contrast, but syntax may start to compete with body text (`#c1bdb8` at L ≈ 0.78).
- **L 0.78** — would essentially merge syntax-primary into the neutral-fg luminance band. Probably too bright; syntax would lose its visual subordination to identifiers.

Things to look for during testing:
- Does purple still feel like the dim one next to teal property keys?
- Does the orange numerics token (`#cc977b`) overpower string green / blue function names? If yes, the bucket lift worked but warm hues now dominate — consider rebalancing chroma down to 0.06 instead of raising L.
- Long-session fatigue: is the editor *too bright* now? Warm-grey background is forgiving but L 0.72 across six tokens is a meaningful aggregate increase in screen luminance.

If unchanged after a week, close this TODO. If purple still reads dim, try splitting JSX attribute names into a brighter L 0.75 sub-bucket (Option B from `~/.claude/plans/image-1-i-feel-sequential-owl.md`).
