# R16 errata brief ERR-CW7: apply the verification corrections to CW7

## Target
Write /home/user/dmdd-solid/returns/R16/CW7-errata.md. It is an addendum that, read together with returns/R16/CW7.md, makes every item verified. Do not edit CW7.md: returns are the record.

## Required
0. **Also produce the WP8 v3 returns.** Write returns/R16/WP8-U-v3.md (+ WP8-U-table-v4.csv) and returns/R16/WP8-F-v3.md as standalone versions. They absorb:
   - VER-CW7's items on WP8-U-v2 and WP8-F-v2: the 55 screen_S rows that use [E] as evidence, the 13 keys with contradictory verdicts, and the partly applied A-G8 / B-(e)(ii) / B-(e)(v) and A-§E(c);
   - the FOM-level findings of referees/R16/REF-WP8-S-A.md and REF-WP8-S-B.md: the light-mediator single-phonon NR rate is independent of c (1910.10716 Eq. (35)), with 1/c holding only for the heavy mediator at ≈ 0.1–0.43 MeV; the polar 'upper bound' is not a bound; the compound Migdal factor 𝓠_Mig with plasmon-pole size; the uniaxial elastic-tensor symmetry breaking; the GAP-input dropouts (Li₂MoO₄); and the ²¹⁰Pb condition on the Pb salts.
   Also fix code/CW7/cascade_gf.py for θ_ii > 1 (ΣP must be 1). The WP8-S ranking itself is revised afterwards by a separate agent; do not rewrite CW7 §12.
1. For every row of /home/user/dmdd-solid/referees/R16/VER-CW7.md that is not plain STANDS:
   - FALLS: re-derive, give the correct statement, or withdraw the item and replace it with an exact remaining gap.
   - STANDS WITH CORRECTION: apply the correction.
   - Thin specification: complete it with what is computed, the approximation level, the method and convergence, and the pitfalls.
   - Doubtful "single missing step": state all missing steps.
2. Re-issue every owed correction of CW7.md that the verifier changed, as complete replacement text, so the merger uses only the errata version. Mark the others "unchanged".
3. Where the verifier's own claim looks wrong, rebut it with a derivation (sympy) in a "Rebuttals" section. Do not concede silently.
4. Fix /home/user/dmdd-solid/code/CW7/checks.py: tighten tolerances, remove circular checks, add checks for each correction. It must pass in ≤ 2 min.
5. Closing table: verifier item → resolution → location.

## Rules
Read CW7.md, VER-CW7.md, and the sources they cite. Follow CONVENTIONS and NOTATION. Literature via /home/user/dmdd-solid/skills/breakthrough-maths/scripts/lit.py into literature/papers-ERR-CW7/, PDFs deleted. Run no heavy numerics. Write only the errata file, the WP8 v3 files and code/CW7/. Do not commit. Final message ≤ 12 lines.
