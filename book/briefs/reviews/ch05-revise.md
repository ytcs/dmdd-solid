# Chapter 5 revision (one reviser)
Revise tex/ch05/ch05.tex, s5-1.tex … s5-7.tex (the Summary sits at the end of s5-7), tex/appD/D-13.tex … D-15.tex and tex/appC/C-18.tex (all under /home/user/dmdd-solid/book). Address **every** item of the four reports in ledgers/REVIEWS/ch05/ (derivation.md, prose.md, reader-a.md, reader-b.md), plus ledgers/REVIEWS/ch05/editor-notes.md, which binds you. Follow COMMON.md (including the compute policy: run no QE; recompute from the caches in figscripts/ch05), STYLE.md, REGISTER.md, NOTATION.md and READER.md.

## Editor rulings
1. Duplicates. 5.1 must not repeat D.13 and 5.5 must not repeat D.14. Cut to pointers as the prose report specifies: each fact lives in one place. D.14 works the two-atom crystal; correct 5.5's description of it.
2. Numbers. Refit the quartic constant from the cached frozen-phonon data (≈ 35–42 eV Å⁻⁴, per derivation.md) and fix WE 5.6, 5.4 and 5.7 consistently (the correction at 0.03 Å; the quartic/harmonic ratio). Fix the WE 5.3 low-energy DOS claim (computed/Debye = 1.3–1.4 because the PBE sound speed is softer). Give C.18 a single, named isotropic model used consistently in 5.2 and C.18, and recompute its speeds (8.43/5.84 km/s from the stated constants) and Θ_D. Correct m_e/2M in 5.1 and D.13, and "a fraction κ_BO of a₀" in D.13. The Γ optical error is 0.6–0.7 % everywhere. Table 5.3's Si DFPT entry must match the text (grid and temperature). Fix 17/18 meV, 22 %, the "2.6 %" and the supercell cost scaling (state one rule and derive the power).
3. 5.5. Add the one clause explaining why dark-photon absorption peaks at ω_L: the screened rate ∝ Im(−1/ε). Say plainly that the Summary's 5.5 paragraph recommends the measured splitting over PBE's ε∞.
4. Wording. Change "measured" to "a lattice-dynamical fit to neutron data" for Flensburg–Stewart. Cite a source for the soft-TA PBE trend, or drop the claim. Explain in one sentence why Ge has no DFPT column (PBE is metallic at the measured a). D.15 normalization: per atom, normalized to 3. Use 52.33 GeV. Keep the Fig. 5.1 settings caption at 50 Ry (no rerun). Fix the 5.7 crystal-momentum sentence ("merging with −Q₁ν₁…").
5. Notation. E_R (as in NOTATION) in D.15; ω_D upright or italic per NOTATION; resolve the p_n, Λ and w clashes. n_A appears before 8.5 defines it: add one clause that defines it in passing. Propose NOTATION rows in SEAMS/5.*.md.
6. Register. Thin the "We will…" runs, "In practice" openers, "gives" and "which is Ref. [n]"; strengthen the 5.3→5.4 and 5.6→5.7 seams; remove "representative calculation", "The book writes" and the 8³ convergence narration in 5.5.
## Deliverables
- The revised files.
- A build in /tmp/build-ch05rev with 0 LaTeX errors, no undefined citations, and undefined references only to unwritten targets.
- Lint clean.
- ledgers/REVIEWS/ch05/revision.md with item → fix → location, and the reason for any item you decline.
- Updated SEAMS rows.
- Other agents edit tex/ch03, ch04, ch06, ch07, appE E.14+ and the ledgers. Stay out of them.
- Do not commit. Final message ≤ 10 lines.
