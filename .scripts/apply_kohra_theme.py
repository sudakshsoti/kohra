#!/usr/bin/env python3
"""Ayu-mirage → Kohra hex substitution for themes/kohra.sublime-theme.

Mirrors apply_kohra.py: idempotent, reports unmapped hexes, preserves white/black.
Run after any palette change in the Kohra Figma collection that affects chrome.
"""
import re
from pathlib import Path

# ayu-mirage hex -> Kohra hex (lowercase, no '#', RGB or RGBA)
M = {
    # --- Surfaces / chrome ---
    "161921":   "030506",   # sidebar separator inner (texture tint) -> bg_deepest
    "1f2430":   "06080a",   # sidebar separator outer, title bar separator -> bg_deep
    "242936":   "181b1d",   # chrome bg: sidebar, title bar, inactive tab, status bar -> bg_chrome
    "282e3b":   "212527",   # raised: panels, command palette, popup, scroll track -> bg_raised
    "282e3b00": "21252700", # transparent raised overlay

    # --- Text greys ---
    "cccac2":   "d3d8da",   # main fg (title bar text, kind labels) -> fg_bright
    "707a8c":   "828689",   # muted text -> fg_muted
    "707a8c4d": "8286894d", # muted @ 30% alpha
    "707a8c80": "82868980", # muted @ 50%
    "707a8cb3": "828689b3", # muted @ 70%
    "707a8cbf": "828689bf", # muted @ 75%

    # --- Tree row highlights (cool blue-grey tints) ---
    "63759900": "30353800", # tree highlight base, transparent
    "63759926": "30353826", # tree hover @ ~15%
    "69758c1f": "3a3e411f", # tree selected @ ~12%

    # --- Accents (the signature gold for active tab indicator + folder open glyph) ---
    "ffcc66":   "c29e70",   # ayu's signature accent -> Kohra gold
    "ffd173":   "c29e70",   # near-duplicate accent -> gold
    "ffad66":   "cc977b",   # orange -> Kohra orange
    "ffdfb3":   "d3d8da",   # pale cream (rare) -> fg_bright

    # --- Other accents (kind containers, syntax glyphs in command palette) ---
    "5ccfe6":   "6bb4aa",   # cyan widget accent -> teal_bright
    "73d0ff":   "78accf",   # blue -> Kohra blue
    "f28779":   "d09292",   # red/coral -> Kohra red
    "f29e74":   "cc977b",   # peach -> orange
    "dfbfff":   "a89ccf",   # purple -> Kohra purple
    "d5ff80":   "9cad77",   # lime -> Kohra green
    "95e6cb":   "70b4a2",   # mint -> green_teal

    # --- Translucent overlays (find highlight, diagnostics underline backgrounds) ---
    "80bfff66": "78accf66", # translucent blue -> Kohra blue @ alpha
    "87d96c66": "9cad7766", # translucent green
    "f2798366": "d0929266", # translucent red
    "b8cfe680": "babec180", # translucent cool blue -> Kohra fg @ alpha

    # --- Dim warning state ---
    "805500":   "3a2d18",   # dim warning bg -> very dim gold-brown

    # --- Shadow ---
    "0000004d": "0000004d", # keep
}

M = {k.lower(): v.lower() for k, v in M.items()}

PRESERVE = {"ffffff", "000000", "0000004d"}

HEX_RE = re.compile(r"#([0-9a-fA-F]{6})([0-9a-fA-F]{2})?\b")

def main():
    target = Path(__file__).resolve().parent.parent / "themes" / "kohra.sublime-theme"

    unmapped = {}
    counts = {}

    def repl(m):
        base = m.group(1).lower()
        suffix = (m.group(2) or "").lower()
        full = base + suffix
        if full in M:
            counts[full] = counts.get(full, 0) + 1
            return "#" + M[full]
        if base in PRESERVE:
            return m.group(0)
        if base in M:
            counts[base] = counts.get(base, 0) + 1
            return "#" + M[base] + suffix
        unmapped[full] = unmapped.get(full, 0) + 1
        return m.group(0)

    text = target.read_text()
    new_text = HEX_RE.sub(repl, text)
    target.write_text(new_text)
    print(f"Wrote {target.name}")
    print(f"Replaced {sum(counts.values())} hex codes across {len(counts)} unique colours.")
    if unmapped:
        print("\nUNMAPPED hexes still in file:")
        for h, n in sorted(unmapped.items(), key=lambda x: -x[1]):
            print(f"  #{h}  x{n}")
    else:
        print("All hexes mapped.")

if __name__ == "__main__":
    main()
