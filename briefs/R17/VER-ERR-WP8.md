# R17 verification brief VER-ERR-WP8 (hostile, isolated; one referee, changed items only)

## Role
You are a hostile referee. Find errors and overclaims. Do not be helpful beyond stating the corrections.

## Under review
/home/user/dmdd-solid/returns/R17/WP8-errata.md with its code (code/REV-WP8-S/, code/CW7/cascade_gf.py), with its checks in /home/user/dmdd-solid/code/REV-WP8-S/ and code/CW7/ (rerun both). It answers referees/R17/VER-ERR-CW7.md and referees/R16/VER-WP8-S-v2.md (you may read both), and builds on returns/R16/WP8-S-v2.md, WP8-F-v3.md, WP8-U-v3.md, table v4 and state/DATA-ADDENDA.csv.

## Scope (verify these, in this order)
0. The new content of the errata: the pairwise heavy-mediator window (re-derive the 4.2 × m_min onset); the light-mediator 1 − (1+κ_η)m_min/m_χ factor (sympy); the CaWO₄ measured-C_ij substitution and its source chain (2508.08858 quoting Farley & Saunders 1972); the CsI bulk-modulus-floor model and whether the CsI lead survives a fully independent check; the S2 array-rule promotion (only diamond?); the next-target guide §16.4 (is each 'missing demonstration' correct?); the r_mat variants; the cascade grid fix (rerun against your own Monte Carlo).
1. Every item where the return changes refereed text: its "Owed corrections" (each target and exact replacement text) and every status upgrade ([C] or [D, sketch] → [D], "observed" → DERIVED, UNRESOLVED → CONFIRMED/REFUTED). Re-derive each one independently, with sympy where it is algebraic.
2. Every claim that a published paper is wrong or misprinted. Fetch the full text and rate it CONFIRMED / REFUTED / UNRESOLVED.
3. Every new derived result, checked for hypotheses, steps and limits.
4. Every CLOSED-AS-EXACT-GAP row: is the stated missing step really the single missing step, and is the computation specification sufficient? It must say what is computed, the approximation level, the method and convergence, and the pitfalls.
5. Proposed LIMITS rows: is the source quoted correctly from full text, and are the validity and leading correction right?

## Read only
The return and its code. The files it cites (returns/R8/*-v3.md, returns/R12/*, returns/R13/*, returns/R14/*, LIMITS.md, state/LOOSE-ENDS.md). /home/user/dmdd-solid/CONVENTIONS.md, NOTATION.md, CONTROLS.md, DONE.md, STATEMENT.md.
Do NOT read other referee reports, other returns/R16 files except those listed and WP8-S-v2.md, briefs/ or log/LAUNCHES.

## Output
Write /home/user/dmdd-solid/referees/R17/VER-ERR-WP8.md (≤ 220 lines). Start with a verdict table, one row per item in scope 1–3: STANDS / STANDS WITH CORRECTION / FALLS, with a reason.
Fetch literature with /home/user/dmdd-solid/skills/breakthrough-maths/scripts/lit.py fetch <id> -o /home/user/dmdd-solid/literature/papers-r17-VER-ERR-WP8/ and delete the PDFs afterwards.
Run no heavy numerics; sympy/numpy checks of ≤ 2 min are fine. Write only your report and the papers folder. Do not commit.

Final message: ≤ 12 lines.
