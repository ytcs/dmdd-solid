# R16 verification brief VER-CW6 (hostile, isolated; one referee, changed items only)

## Role
You are a hostile referee. Find errors and overclaims. Do not be helpful beyond stating the corrections.

## Under review
/home/user/dmdd-solid/returns/R16/CW6.md, with its checks in /home/user/dmdd-solid/code/CW6/ (rerun them). It closes loose-ends rows listed in /home/user/dmdd-solid/state/LOOSE-ENDS.md.

## Scope (verify these, in this order)
0. Also under review: returns/R16/WP8-R-v2.md. Check that each closing-table row resolves its R14 referee item (you may read referees/R14/REF-WP8-R-A.md and -B.md), and that the verdicts per route follow from the derivations. Re-derive the isotropic P–SV acoustic-mismatch solver and its reciprocity theorem; check the r_coll = 0.87–0.98 estimate and its consequence for LIMITS L36 / WP7-E (r ≥ 1 condition).
1. Every item where the return changes refereed text: its "Owed corrections" (each target and exact replacement text) and every status upgrade ([C] or [D, sketch] → [D], "observed" → DERIVED, UNRESOLVED → CONFIRMED/REFUTED). Re-derive each one independently, with sympy where it is algebraic.
2. Every claim that a published paper is wrong or misprinted. Fetch the full text and rate it CONFIRMED / REFUTED / UNRESOLVED.
3. Every new derived result, checked for hypotheses, steps and limits.
4. Every CLOSED-AS-EXACT-GAP row: is the stated missing step really the single missing step, and is the computation specification sufficient? It must say what is computed, the approximation level, the method and convergence, and the pitfalls.
5. Proposed LIMITS rows: is the source quoted correctly from full text, and are the validity and leading correction right?

## Read only
The return and its code. The files it cites (returns/R8/*-v3.md, returns/R12/*, returns/R13/*, returns/R14/*, LIMITS.md, state/LOOSE-ENDS.md). /home/user/dmdd-solid/CONVENTIONS.md, NOTATION.md, CONTROLS.md, DONE.md, STATEMENT.md.
Do NOT read referees/R16/, other returns/R16 files, briefs/ or log/LAUNCHES.

## Output
Write /home/user/dmdd-solid/referees/R16/VER-CW6.md (≤ 220 lines). Start with a verdict table, one row per item in scope 1–3: STANDS / STANDS WITH CORRECTION / FALLS, with a reason.
Fetch literature with /home/user/dmdd-solid/skills/breakthrough-maths/scripts/lit.py fetch <id> -o /home/user/dmdd-solid/literature/papers-r16-VER-CW6/ and delete the PDFs afterwards.
Run no heavy numerics; sympy/numpy checks of ≤ 2 min are fine. Write only your report and the papers folder. Do not commit.

Final message: ≤ 12 lines.
