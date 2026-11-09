# R16 verification brief VER-CW1 (hostile, isolated; one referee, changed items only)

## Role
You are a hostile referee. Find errors and overclaims. Do not be helpful beyond stating the corrections.

## Under review
/home/user/dmdd-solid/returns/R16/CW1.md, with its checks in /home/user/dmdd-solid/code/CW1/ (rerun them). It closes loose-ends rows listed in /home/user/dmdd-solid/state/LOOSE-ENDS.md.

## Scope (verify these, in this order)
0. The [CALC] numbers (code/CW1/: inputs, scripts, out/): rerun the cheap ones, check convergence and the off-axis minimum search for the Si zero-phonon threshold (0.400–0.405 MeV), M_x = 1.19 m_e, the (2̄00) vertex Σ|ρ|² = 0.150 and the mirror selection rule, the ZPL/PAER ratios, and the SOC-lifted vertex. Check the reconciliation with returns/R15/COMP-PH.md and COMP-PAER.md (you may read both).
1. Every item where the return changes refereed text: its "Owed corrections" (each target and exact replacement text) and every status upgrade ([C] or [D, sketch] → [D], "observed" → DERIVED, UNRESOLVED → CONFIRMED/REFUTED). Re-derive each one independently, with sympy where it is algebraic.
2. Every claim that a published paper is wrong or misprinted. Fetch the full text and rate it CONFIRMED / REFUTED / UNRESOLVED.
3. Every new derived result, checked for hypotheses, steps and limits.
4. Every CLOSED-AS-EXACT-GAP row: is the stated missing step really the single missing step, and is the computation specification sufficient? It must say what is computed, the approximation level, the method and convergence, and the pitfalls.
5. Proposed LIMITS rows: is the source quoted correctly from full text, and are the validity and leading correction right?

## Read only
The return and its code. The files it cites (returns/R8/*-v3.md, returns/R12/*, returns/R13/*, returns/R14/*, LIMITS.md, state/LOOSE-ENDS.md). /home/user/dmdd-solid/CONVENTIONS.md, NOTATION.md, CONTROLS.md, DONE.md, STATEMENT.md.
Do NOT read referees/R16/, other returns/R16 files, briefs/ or log/LAUNCHES.

## Output
Write /home/user/dmdd-solid/referees/R16/VER-CW1.md (≤ 220 lines). Start with a verdict table, one row per item in scope 1–3: STANDS / STANDS WITH CORRECTION / FALLS, with a reason.
Fetch literature with /home/user/dmdd-solid/skills/breakthrough-maths/scripts/lit.py fetch <id> -o /home/user/dmdd-solid/literature/papers-r16-VER-CW1/ and delete the PDFs afterwards.
Run no heavy numerics; sympy/numpy checks of ≤ 2 min are fine. Write only your report and the papers folder. Do not commit.

Final message: ≤ 12 lines.
