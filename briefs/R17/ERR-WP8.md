# R17 errata brief ERR-WP8: final corrections to the WP8 chain (U-v3, F-v3, table v4, S-v2)

## Target
Write /home/user/dmdd-solid/returns/R17/WP8-errata.md. Read together with returns/R16/WP8-U-v3.md, WP8-F-v3.md, WP8-U-table-v4.csv, CW7-errata.md and WP8-S-v2.md, it must make every item verified. It applies:
- referees/R17/VER-ERR-CW7.md: RC1–RC9 and every non-STANDS row;
- referees/R16/VER-WP8-S-v2.md: every non-STANDS row.

Do not edit those returns.

## Required
1. **One section per correction**, each containing:
   - the corrected statement;
   - its derivation, checked with sympy where algebraic;
   - full replacement text for every passage it changes.
2. **Key items:**
   - **cascade_gf.py:** the grid step h must divide ω₀ and E_g; fix the code and rerun.
   - **Heavy-mediator single-phonon window:** recompute it pairwise per material. VER-WP8-S-v2 gives ≈ 0.065–0.34 MeV for survivors; VER-ERR-CW7 gives (2.3b) = 6.5 keV for Si and ≈ 0.2–0.4 MeV for CsI/Si. Reconcile the two and state the window with its derivation.
   - **The light-mediator O(m_min/m_χ) correction.**
   - **The ε-route polar bound:** it requires mode data. Use the (8.1) interval where only ε data exist.
   - **r^M is an [E] lower estimate.**
   - **Ge EC L-lines inside the sub-keV window.**
   - **G-F6:** add ⁴³Ca and the direction-resolved DOS.
   - **Statement (ii):** add "excluding Migdal".
   - **L-S3:** the (n′/n)^(−3/2) factor multiplies the whole FOM.
   - **CsI and CaWO₄:** justify or widen their uncertainty widths. Use measured elastic constants [FT] if you can fetch them. The CsI value may sit below the bulk-modulus floor; check this.
   - **Smaller fixes:**
     - the tier count;
     - the Si ε_eh width (text vs code);
     - the sapphire width;
     - the Ge vs Si cosmogenics sum;
     - the wording of the PE shear shift;
     - the identity of the dropped rows.
   - **The L(k,ω) gap:** write its computation spec, in the book-explainable form: what is computed, the approximation level, the method, convergence and pitfalls.
3. **Ranking.** Update code/REV-WP8-S/rank.py with every input change and rerun it.
   - Report the r_mat = 0, 0.5, 0.9 and 1 variants (CONVENTIONS §13 row 29).
   - Write data/ranking_v3.json.
   - Give a final readings table with probabilities.
   - Extend checks.py to cover each correction; it must pass.
4. **Owed corrections** to LIMITS, NOTATION and CORRECTIONS, as exact text.
5. **Closing table:** verifier item → resolution → location.

## Rules
- Run no heavy numerics; a Monte Carlo of ≤ 2 min is fine.
- Follow CONVENTIONS and NOTATION.
- Literature via skills/breakthrough-maths/scripts/lit.py into literature/papers-ERR-WP8/; delete the PDFs.
- Write only the errata file, code/REV-WP8-S/ and code/CW7/cascade_gf.py with its checks. Do not commit.
- Final message ≤ 12 lines.
