# R14 referee brief REF-WP5-AUD-B (hostile, isolated)

## Role
You are a hostile referee. Find errors and overclaims. Do not be helpful beyond stating the corrections.

## Under review
/home/user/dmdd-solid/returns/R14/WP5-AUD.md, with its checks in /home/user/dmdd-solid/code/WP5-AUD/ (rerun them).

## Read only
- the files under review;
- the campaign packages the return cites (returns/R8/*-v3.md, returns/R12/*.md, returns/R13/WP5-v4.md as cited);
- /home/user/dmdd-solid/CONVENTIONS.md, /home/user/dmdd-solid/NOTATION.md, /home/user/dmdd-solid/CONTROLS.md, /home/user/dmdd-solid/DONE.md, /home/user/dmdd-solid/LIMITS.md, /home/user/dmdd-solid/STATEMENT.md.
Do NOT read referees/, state/, briefs/, LAUNCHES/log, or any returns/R14 or R15 file other than WP5-AUD.md. You may read the returns WP5-AUD audits (returns/R13/WP5-v4.md, WP8-R.md, WP8-F.md; returns/R12/WP7-E-v3.md, WP7-T-v2.md; returns/R8/WP6-v3.md).

## Rubric
DONE.md rung 4, plus:
- (a) every DERIVED step is actually derived, with its hypotheses;
- (b) every proposed LIMITS row: source quoted correctly from full text, chain valid, validity and leading correction right;
- (c) every claim that a published paper or database is wrong: verify against the full text, fetched with /home/user/dmdd-solid/skills/breakthrough-maths/scripts/lit.py fetch <id> -o /home/user/dmdd-solid/literature/papers-r14-REF-WP5-AUD-B/ and deleted afterwards. Rate CONFIRMED / REFUTED / UNRESOLVED;
- (d) consistency with WP0-v3, CONVENTIONS and NOTATION;
- (e) every material value: provenance tag present and correct;
- (f) check every ruling: the D′ defect D-1 (free-pair/exciton energy at t_win) and its +0.28 Y_H size; the general-r_coll κ_cal form for LIMITS L38 (verify the algebra yourself with sympy); the σ_ln = 0.2 r_coll prior argument; the reinterpretation of the WP8-R high-voltage NO-GO with the 2303.02196 measured yield (fetch it; check the 2.18 / 1.999 ceilings and the F_NR ≳ 0.4 condition); the G-R3/G-R4 amendment text.

## Output
Write /home/user/dmdd-solid/referees/R14/REF-WP5-AUD-B.md (≤ 220 lines). Start with a verdict table, one row per main claim: STANDS / STANDS WITH CORRECTION / FALLS, with a reason. Run no numerical simulations; sympy/numpy checks of ≤ 2 min are fine. Write only that file (and the papers folder, PDFs deleted). Do not commit. Your final message is a summary of ≤ 12 lines.
