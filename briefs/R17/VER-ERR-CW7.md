# R17 verification brief VER-ERR-CW7 (hostile, isolated; one referee, changed items only)

## Role
You are a hostile referee. Find errors and overclaims. Do not be helpful beyond stating the corrections.

## Under review
/home/user/dmdd-solid/returns/R16/CW7-errata.md, returns/R16/WP8-U-v3.md, WP8-U-table-v4.csv and WP8-F-v3.md, with its checks in /home/user/dmdd-solid/code/CW7/ (rerun them). They are the CW7 errata and the WP8 v3 returns (you may read referees/R16/VER-CW7.md, REF-WP8-S-A.md and REF-WP8-S-B.md, which they answer).

## Scope (verify these, in this order)
0. The new content: (a) the JARVIS shear-order claim (C₄₄/C₆₆ swapped in every non-cubic tensor R14–R16): check it against the JARVIS documentation/source and ≥ 3 materials with measured C_ij [FT], and check that build_v4.py re-indexes correctly; (b) the 55 retagged/dropped screening rows and 13 resolved keys (sample ≥ 15); (c) CW7-154′ and the cascade_gf.py θ_ii > 1 fix (rerun); (d) the WP8-F-v3 FOM changes (light-mediator independence, the 9.52 polar bound and its conditions, 𝓠_Mig, ²¹⁰Pb condition).
1. Every item where the return changes refereed text: its "Owed corrections" (each target and exact replacement text) and every status upgrade ([C] or [D, sketch] → [D], "observed" → DERIVED, UNRESOLVED → CONFIRMED/REFUTED). Re-derive each one independently, with sympy where it is algebraic.
2. Every claim that a published paper is wrong or misprinted. Fetch the full text and rate it CONFIRMED / REFUTED / UNRESOLVED.
3. Every new derived result, checked for hypotheses, steps and limits.
4. Every CLOSED-AS-EXACT-GAP row: is the stated missing step really the single missing step, and is the computation specification sufficient? It must say what is computed, the approximation level, the method and convergence, and the pitfalls.
5. Proposed LIMITS rows: is the source quoted correctly from full text, and are the validity and leading correction right?

## Read only
The return and its code. The files it cites (returns/R8/*-v3.md, returns/R12/*, returns/R13/*, returns/R14/*, LIMITS.md, state/LOOSE-ENDS.md). /home/user/dmdd-solid/CONVENTIONS.md, NOTATION.md, CONTROLS.md, DONE.md, STATEMENT.md.
Do NOT read other referee reports, other returns/R16 files except those listed and WP8-S-v2.md, briefs/ or log/LAUNCHES.

## Output
Write /home/user/dmdd-solid/referees/R17/VER-ERR-CW7.md (≤ 220 lines). Start with a verdict table, one row per item in scope 1–3: STANDS / STANDS WITH CORRECTION / FALLS, with a reason.
Fetch literature with /home/user/dmdd-solid/skills/breakthrough-maths/scripts/lit.py fetch <id> -o /home/user/dmdd-solid/literature/papers-r17-VER-ERR-CW7/ and delete the PDFs afterwards.
Run no heavy numerics; sympy/numpy checks of ≤ 2 min are fine. Write only your report and the papers folder. Do not commit.

Final message: ≤ 12 lines.
