# R16 referee brief REF-WP8-S-B (hostile, isolated)

## Role
You are a hostile referee. Find errors and overclaims. Do not be helpful beyond stating the corrections.

## Under review
/home/user/dmdd-solid/returns/R16/CW7.md §12 only (the WP8-S ranking synthesis: optimal substrate per channel within the pickable universe), built on returns/R16/WP8-U-v2.md, WP8-U-table-v3.csv and WP8-F-v2.md, with its checks in /home/user/dmdd-solid/code/CW7/ (rank.py) (rerun them).

## Read only
- the files under review;
- the campaign packages the return cites (returns/R8/*-v3.md, returns/R12/*.md, returns/R13/WP5-v4.md as cited);
- /home/user/dmdd-solid/CONVENTIONS.md, /home/user/dmdd-solid/NOTATION.md, /home/user/dmdd-solid/CONTROLS.md, /home/user/dmdd-solid/DONE.md, /home/user/dmdd-solid/LIMITS.md, /home/user/dmdd-solid/STATEMENT.md.
Do NOT read referees/, state/, briefs/, LAUNCHES/log, or returns/R16 files other than CW7.md, WP8-U-v2.md, WP8-F-v2.md and WP8-U-table-v3.csv.

## Rubric
DONE.md rung 4, plus:
- (a) every DERIVED step is actually derived, with its hypotheses;
- (b) every proposed LIMITS row: source quoted correctly from full text, chain valid, validity and leading correction right;
- (c) every claim that a published paper or database is wrong: verify against the full text, fetched with /home/user/dmdd-solid/skills/breakthrough-maths/scripts/lit.py fetch <id> -o /home/user/dmdd-solid/literature/papers-r16-REF-WP8-S-B/ and deleted afterwards. Rate CONFIRMED / REFUTED / UNRESOLVED;
- (d) consistency with WP0-v3, CONVENTIONS and NOTATION;
- (e) every material value: provenance tag present and correct;
- (f) the ranking itself: is each per-channel ranking the correct consequence of the WP8-F-v2 FOM (rate vs reach, background-free vs background-limited) evaluated on the v3 table values with their provenance; are excluded/conditional materials handled per the WP8-U-v2 screening (incl. S4 radioactivity); are uncertainties propagated (could the top-ranked material change within its error band?); are any rankings driven by [E] or GAP values, and is that stated; is the FOMs' theory uncertainty (WP6 nuisance types) reflected.

## Output
Write /home/user/dmdd-solid/referees/R16/REF-WP8-S-B.md (≤ 220 lines). Start with a verdict table, one row per main claim: STANDS / STANDS WITH CORRECTION / FALLS, with a reason. Run no numerical simulations; sympy/numpy checks of ≤ 2 min are fine. Write only that file (and the papers folder, PDFs deleted). Do not commit. Your final message is a summary of ≤ 12 lines.
