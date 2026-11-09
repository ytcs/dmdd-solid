# R16 verification brief VER-CW7 (hostile, isolated; one referee, changed items only)

## Role
You are a hostile referee. Find errors and overclaims. Do not be helpful beyond stating the corrections.

## Under review
/home/user/dmdd-solid/returns/R16/CW7.md, with its checks in /home/user/dmdd-solid/code/CW7/ (rerun them). It closes loose-ends rows listed in /home/user/dmdd-solid/state/LOOSE-ENDS.md.

## Scope (verify these, in this order)
0. Also under review: returns/R16/WP8-U-v2.md (+ WP8-U-table-v3.csv) and returns/R16/WP8-F-v2.md. Check that each closing-table row really resolves its R14 referee item (you may read referees/R14/REF-WP8-U-*.md and REF-WP8-F-*.md for this), and trace ≥ 20 random v3 CSV rows (state the seed) to their sources. Exclude CW7 §12 (the WP8-S synthesis, refereed separately).
1. Every item where the return changes refereed text: its "Owed corrections" (each target and exact replacement text) and every status upgrade ([C] or [D, sketch] → [D], "observed" → DERIVED, UNRESOLVED → CONFIRMED/REFUTED). Re-derive each one independently, with sympy where it is algebraic.
2. Every claim that a published paper is wrong or misprinted. Fetch the full text and rate it CONFIRMED / REFUTED / UNRESOLVED.
3. Every new derived result, checked for hypotheses, steps and limits.
4. Every CLOSED-AS-EXACT-GAP row: is the stated missing step really the single missing step, and is the computation specification sufficient? It must say what is computed, the approximation level, the method and convergence, and the pitfalls.
5. Proposed LIMITS rows: is the source quoted correctly from full text, and are the validity and leading correction right?

## Read only
The return and its code. The files it cites (returns/R8/*-v3.md, returns/R12/*, returns/R13/*, returns/R14/*, LIMITS.md, state/LOOSE-ENDS.md). /home/user/dmdd-solid/CONVENTIONS.md, NOTATION.md, CONTROLS.md, DONE.md, STATEMENT.md.
Do NOT read referees/R16/, other returns/R16 files, briefs/ or log/LAUNCHES.

## Output
Write /home/user/dmdd-solid/referees/R16/VER-CW7.md (≤ 220 lines). Start with a verdict table, one row per item in scope 1–3: STANDS / STANDS WITH CORRECTION / FALLS, with a reason.
Fetch literature with /home/user/dmdd-solid/skills/breakthrough-maths/scripts/lit.py fetch <id> -o /home/user/dmdd-solid/literature/papers-r16-VER-CW7/ and delete the PDFs afterwards.
Run no heavy numerics; sympy/numpy checks of ≤ 2 min are fine. Write only your report and the papers folder. Do not commit.

Final message: ≤ 12 lines.
