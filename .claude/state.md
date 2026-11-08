# State: Obsidian colour-review fixes → all Kohra themes

## Goal
Verify the approved Obsidian fixes (handoff/2026-11-08-obsidian-*.md/.json, live in /Users/sudakshsoti/dev/kohra/handoff, untracked) and plan applying them to obsidian-kohra-theme/theme.css and to this repo's 7 ports.

## Decisions
- User approved the Paper "· fixed" frames (2026-11-08).
- Numeric verification passed: 108/108 vars, every recorded old hex matches theme.css, no changed-but-unmarked or marked-but-unchanged token.
- Residuals: Night text-faint 3.99:1 on base-10; Daybreak green/cyan/blue 4.33–4.42 on base-10; accent HSL 1 bit off blue.
- Kohra ports share Obsidian Night's ramp exactly (except editor #0b0e10 vs #0f1214). Daybreak-only fixes don't apply (no light variant).
- SOURCE OF TRUTH IS NOW PAPER (file 01M6VVHS31B3BBZ1ZY4ZSFBYFS), not Figma. AGENTS.md needs updating.
- Ports kept: VS Code, Cursor, Zed, Sublime (scheme+UI), Ghostty, cmux. RETIRE Superset.
- Port all finalised fixes: Δ2 ramp lift (variables/class HOLD #babec1), Δ4 cyan #6bb4ab + teal #70b4a2 merged into it (regex stays dim), Δ7 error #e07878, warning unified on #bf801e (VS Code #c29e70 → #bf801e), ANSI 0/7/8/15 follow ramp. Chrome/state (Δ8 active>hover, Δ9 focus blue, Δ15 borders) follow Paper.
- Keep editor bold orange and Markdown titles blue (no Δ5/Δ13 in ports).
- Paper frame check passed; only defect: Δ12 pin wraps on Daybreak · fixed.

## Rejected
- Carrying Obsidian-only consumer changes (headings, accent HSL, inactive-tab CSS rule) into ports verbatim.

## Done
- Phase 2: commit d8a345f (6 ports, Superset retired, AGENTS/README/M dict, handoff copied).
- Paper page "Kohra · final": ramp, hues, quiet syntax, state/diag, ANSI 16, in-use editor mock.
- Phase 0: Δ12 pin fixed in Paper (nowrap, moved to margin).
- Phase 1: obsidian-kohra-theme commit 100f8cc (theme.css 0 mismatches vs JSON, 110 vars/mode; README/AGENTS/kitchen-sink docs updated). Not pushed. No in-app visual pass done.

## Next
- User: in-app visual pass (VS Code, Zed, Sublime, Ghostty, cmux; Obsidian kitchen-sink). Push both repos when happy.

## Warm text pass (2026-11-08, uncommitted)
- User chose B: neutral text OKLCH H 75 C 0.012 at same L; all neutral text; everywhere incl. Daybreak.
- Map (scratchpad warm_map.json): e7eaec→eee9e1, d3d8da→dcd6cf, d1d5d8→d9d3cc, bfc3c6→c7c1ba, babec1→c2bdb5, aeb2b5→b6b1a9, 9a9ea1→a29d95, 929699→9a958e, 797d7f→817c75 (L 0.588 so Obsidian faint ≥4.5 on #0f1214). Day: 6b7175→746f68, 545a5f→5d5852, 444a4e→4d4842, 31363a→39352f, 202427→27231d.
- Opaque + glyph uses warm; translucent fills/borders stay cool. Comments, operators, Obsidian base-50 and --color-base-rgb stay cool.
- Done: 6 ports, T3 theme (installed, defaultTheme=kohra), Obsidian theme.css, docs both repos, apply_kohra.py M dict. Paper: fork agent running.
- Next: report; ask to commit + push both repos (and add themes/kohra-t3code.json).
