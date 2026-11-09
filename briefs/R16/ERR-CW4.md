# R16 errata brief ERR-CW4: apply the verification corrections to CW4

## Target
Write /home/user/dmdd-solid/returns/R16/CW4-errata.md. It is an addendum that, read together with returns/R16/CW4.md, makes every item verified. Do not edit CW4.md: returns are the record.

## Required
1. For every row of /home/user/dmdd-solid/referees/R16/VER-CW4.md that is not plain STANDS:
   - FALLS: re-derive, give the correct statement, or withdraw the item and replace it with an exact remaining gap.
   - STANDS WITH CORRECTION: apply the correction.
   - Thin specification: complete it with what is computed, the approximation level, the method and convergence, and the pitfalls.
   - Doubtful "single missing step": state all missing steps.
2. Re-issue every owed correction of CW4.md that the verifier changed, as complete replacement text, so the merger uses only the errata version. Mark the others "unchanged".
3. Where the verifier's own claim looks wrong, rebut it with a derivation (sympy) in a "Rebuttals" section. Do not concede silently.
4. Fix /home/user/dmdd-solid/code/CW4/checks.py: tighten tolerances, remove circular checks, add checks for each correction. It must pass in ≤ 2 min.
5. Closing table: verifier item → resolution → location.

## Rules
Read CW4.md, VER-CW4.md, and the sources they cite. Follow CONVENTIONS and NOTATION. Literature via /home/user/dmdd-solid/skills/breakthrough-maths/scripts/lit.py into literature/papers-ERR-CW4/, PDFs deleted. Run no heavy numerics. Write only the errata file and code/CW4/. Do not commit. Final message ≤ 12 lines.
