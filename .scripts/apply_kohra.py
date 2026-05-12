#!/usr/bin/env python3
import re
from pathlib import Path

# TN hex -> Kohra hex (both lowercase, 6 chars, no '#')
M = {
    # --- Surfaces ---
    "0d0f17": "060403",  # window borders -> bg-deepest
    "0f0f14": "060403",  # input.border, chat.requestBorder -> bg-deepest
    "101014": "090705",  # many borders, peekView -> bg-deep
    "111117": "090705",  # foldBackground base -> bg-deep
    "14141b": "100c0a",  # input.bg, dropdown -> bg-base
    "13131a": "100c0a",  # list.hoverBackground -> bg-base
    "16161e": "1e1a17",  # sideBar, statusBar, terminal, panel -> bg-surface
    "1a1b26": "14110e",  # editor.background -> bg-editor
    "1b1e2e": "272320",  # menubar selBorder, scmGraph -> bg-elevated
    "1c1d29": "272320",  # list focus/inactive -> bg-elevated
    "1e202e": "272320",  # sideBar/list dropBg, menu selBg -> bg-elevated
    "1f202e": "272320",  # tab modified/active border -> bg-elevated
    "222333": "272320",  # tab.lastPinnedBorder -> bg-elevated
    "232433": "272320",  # editorIndentGuide.bg1 -> bg-elevated
    "202330": "272320",  # toolbar, list activeSel -> bg-elevated
    "20222c": "272320",  # statusBar hover, suggest selected -> bg-elevated
    "282a3b": "272320",  # diff unchanged -> bg-elevated
    "292e42": "272320",  # diff diagonal fill -> bg-elevated
    "29355a": "0a3149",  # sash.hover, notebook focus -> brand/blue-dim

    # --- Text / chrome greys ---
    "a9b1d6": "c1bdb8",  # editor fg, sidebar header, peek sel fg -> fg-normal
    "acb0d0": "c1bdb8",  # badge fg, link active, term bright white -> fg-normal
    "bbc2e0": "c1bdb8",  # validation fg -> fg-normal
    "c0caf5": "c1bdb8",  # cursor, variables, semantic -> fg-normal
    "c0cefc": "dbd6d2",  # markup.table -> fg-bright
    "d9d4cd": "c1bdb8",  # semantic parameter -> fg-normal
    "9aa5ce": "a19d99",  # charts fg, html text, heading 5 -> fg-secondary
    "9abdf5": "a19d99",  # block punctuation, list_item -> fg-secondary
    "9699a8": "a19d99",  # textPreformat -> fg-secondary
    "747ca1": "75706d",  # heading 6 -> fg-subtle
    "868bc4": "8a8581",  # scrollbar slider -> fg-muted
    "7e83b2": "8a8581",  # badge bg -> fg-muted
    "787c99": "8a8581",  # foreground, icon, sidebar -> fg-muted
    "646e9c": "75706d",  # ghostText, inlayHint, gitlens trailing -> fg-subtle
    "545c7e": "615c59",  # disabledForeground, focusBorder -> fg-dim
    "515670": "615c59",  # descriptionForeground, ignoredResource -> fg-dim
    "515c7e": "45413e",  # selection bg (tinted overlay) -> fg-ghost
    "3b3e52": "45413e",  # activityBar inactive, button secondary -> fg-ghost
    "42465d": "45413e",  # panelTitle inactive, bracketMatch border -> fg-ghost
    "363b54": "45413e",  # linenumber, indent guide, whitespace -> fg-ghost
    "414761": "45413e",  # breakpoint disabled -> fg-ghost
    "51597d": "605749",  # codeLens, comment, separator -> syntax/comment
    "4e5579": "716859",  # blockquote, raw inline punct -> syntax/comment-doc
    "5a638c": "716859",  # comment doc -> syntax/comment-doc

    # --- Brand blues ---
    "3d59a1": "085b87",  # button bg, focus, find match -> brand/blue
    "506fca": "085b87",  # scmGraph historyItem ref -> brand/blue
    "6183bb": "4f7791",  # settings hdr, link, list highlight, modified -> blue-muted
    "668ac4": "4f7791",  # list highlight -> blue-muted

    # --- Accent palette ---
    "7aa2f7": "78accf",  # blue, function, method, decorator, ansiBlue -> accent/blue
    "698cd6": "78accf",  # bracket 1 -> accent/blue
    "7dcfff": "6bb4aa",  # cyan-bright, interpolation, link active -> accent/cyan-bright
    "68b3de": "6bb4aa",  # bracket 2 -> accent/cyan-bright
    "2ac3de": "6bb4aa",  # semantic defaultLibrary -> accent/cyan-bright
    "73daca": "70b4a2",  # object-key, link, preprocessor, ansi green -> accent/teal-bright
    "41a6b5": "4c958c",  # chart green, gutter add, merge -> accent/teal
    "25aac2": "4c958c",  # bracket 4 -> accent/teal
    "0db9d7": "4c958c",  # html entity, info-token, json key, support -> accent/cyan
    "1abc9c": "2a99d4",  # info ruler -> diag/info
    "0da0ba": "2a99d4",  # info/hint icons, notif info -> diag/info
    "bb9af7": "a89ccf",  # purple keyword variable-decl -> accent/purple
    "9a7ecc": "a89ccf",  # bracket 3 -> accent/purple
    "b267e6": "a89ccf",  # token debug -> accent/purple
    "9d7cd8": "746b91",  # purple-dark, storage-mod, charts purple -> accent/purple-dark
    "9ece6a": "9cad77",  # string, ansi green, debug string -> accent/green
    "80a856": "9cad77",  # bracket 5 -> accent/green
    "e0af68": "c29e70",  # yellow params globals warning -> accent/yellow
    "e2bd3a": "c29e70",  # stack frame highlight base -> accent/yellow
    "ff9e64": "cc977b",  # orange numbers scmGraph -> accent/orange
    "c49a5a": "bf801e",  # list/debug warning -> diag/warning
    "bba461": "bf801e",  # notification warning icon -> diag/warning
    "ffdb69": "bf801e",  # token warn -> diag/warning
    "c97018": "cc977b",  # list invalid -> accent/orange

    # --- Reds / errors ---
    "f7768e": "d09292",  # red/pink, language var, ansi red, tag, spread -> accent/red
    "fc7b7b": "d09292",  # CSS ID -> accent/red
    "de5971": "d09292",  # custom tag -> accent/red
    "ba3c97": "a57495",  # tag punctuation -> accent/magenta
    "ff5370": "af7473",  # invalid -> accent/red-error
    "db4b4b": "d36c6d",  # error -> diag/error
    "bb616b": "d36c6d",  # debug/list/notif error -> diag/error
    "c24242": "d36c6d",  # breakpoint unverified -> diag/error
    "85353e": "321919",  # validation error bg -> vcs/deleted-bg
    "963c47": "af7473",  # validation error border, exception border -> red-error
    "a6333f": "af7473",  # filter no matches -> red-error

    # --- VCS / diff ---
    "914c54": "a66f6f",  # markup deleted, git deleted resource -> vcs/deleted-fg
    "944449": "321919",  # minimap deleted -> vcs/deleted-bg
    "703438": "321919",  # overview ruler deleted -> vcs/deleted-bg
    "823c41": "321919",  # gutter deleted -> vcs/deleted-bg
    "449dab": "6a8b63",  # added/renamed/untracked, markup inserted, merge handled -> vcs/added-fg
    "164846": "172614",  # gutter added -> vcs/added-bg
    "1c5957": "172614",  # minimap added -> vcs/added-bg
    "394b70": "0e2433",  # gutter modified, overview modified -> vcs/modified-bg
    "425882": "0e2433",  # minimap modified -> vcs/modified-bg

    # --- Syntax-faint (operator/escape) ---
    "89ddff": "79736d",  # punctuation, operator, escape, regex quantifier -> syntax/operator

    # --- Regex ---
    "b4f9f8": "519584",  # regex strings -> syntax/regex

    # --- Markdown headings (use varied dims for hierarchy) ---
    "61bdf2": "4f7791",  # heading 2 -> blue-muted
    "6d91de": "4f7791",  # heading 4 -> blue-muted

    # --- Stragglers ---
    "c2985b": "c29e70",  # inputValidation warning bg -> accent/yellow
    "2b2b3b": "272320",  # tree indent guides -> bg-elevated
    "007a75": "172614",  # merge current content bg base -> vcs/added-bg
}

# Lowercase, sanity check
M = {k.lower(): v.lower() for k, v in M.items()}

PRESERVE = {"ffffff", "000000"}

HEX_RE = re.compile(r"#([0-9a-fA-F]{6})([0-9a-fA-F]{2})?\b")

def main():
    target = Path("/Users/sudakshsoti/dev/kohra/themes/kohra-color-theme.jsonc")
    text = target.read_text()

    unmapped = {}
    counts = {}

    def repl(m):
        base = m.group(1).lower()
        suffix = m.group(2) or ""
        if base in PRESERVE:
            return m.group(0)
        if base in M:
            counts[base] = counts.get(base, 0) + 1
            return "#" + M[base] + suffix
        unmapped[base] = unmapped.get(base, 0) + 1
        return m.group(0)

    new_text = HEX_RE.sub(repl, text)

    target.write_text(new_text)

    print(f"Replaced {sum(counts.values())} hex codes across {len(counts)} unique colours.")
    if unmapped:
        print("\nUNMAPPED hexes still in file:")
        for h, n in sorted(unmapped.items(), key=lambda x: -x[1]):
            print(f"  #{h}  x{n}")
    else:
        print("All hexes mapped.")

if __name__ == "__main__":
    main()
