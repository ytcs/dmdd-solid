# Chapter 3 revision (one reviser for the chapter and its appendices)

Revise tex/ch03/ch03.tex and s3-1.tex … s3-6.tex (the Summary sits at the end of s3-6), tex/appC/C-1.tex … C-8.tex, and tex/appD/D-4.tex, D-5.tex. Touch D-6.tex only for the H_D → H_Dar rename, and appE E-7.tex and C-15.tex only for the (Zα)² clause. All paths are under /home/user/dmdd-solid/book.

Address **every** item of the reports in ledgers/REVIEWS/ch03/: derivation.md, prose.md, reader-a.md, reader-b.md and figures.md, plus ledgers/REVIEWS/ch03/editor-notes.md, which binds you. Follow COMMON.md (including the compute policy: run no QE), STYLE.md, REGISTER.md, NOTATION.md and READER.md.

## Editor rulings
1. **(200) versus (222).** Bond charge supplies (222) only; (200) vanishes exactly by the glide symmetry (\cref{app:C.17}). Fix 3.2 and 3.4. Define "glide" in one clause where it is first used.
2. **Gap values.** Use 1.17 eV at low T and 1.12 eV at 300 K. Use 1.11 eV only as the projection threshold, and say so. WE 3-scales uses 1.17.
3. **Lattice constants.** Use room temperature throughout: Si 5.431, Ge 5.658, GaAs 5.653 Å (Vurgaftman), in both prose and tables. Remove the "zero-temperature" labels.
4. **Figures.** Figs 3.6–3.8 now come from QE (figures.md lists every number). Make all text consistent with them: k_c 0.843 everywhere (no 0.840 or 0.85), Ge semimetallic in PBE with spin–orbit, and the LDA caveat. Remove the claim at 3.3 l.44 that a figure is DFT where it is a model, and keep the description of each figure accurate. The k·p sum-rule check stays as the empirical model: state its inputs (Cohen–Bergstresser form factors) in one sentence and fix the degenerate-pair accounting (the pair contributes 4.53 of 5.43).
5. **Wannier (3.6).** The away-from-bond result is confirmed. Correct the description of the wannier90 tutorial outcome to what figures.md and derivation.md report, and say plainly that the more localized set points away from the bonds. Replace the claim that minimizers "must be" real with what is actually known. Define or drop "Chern invariant".
6. **Notation.**
   - Use δk for k − k₀ (not bold κ).
   - Atomic orbitals are φ^{at}_j, and trial orbitals φ^tr_n.
   - No hat on the velocity operator (as in App. A.5).
   - E_qp for the quasiparticle energy.
   - Rename H_D → H_Dar in D.6.
   - Propose NOTATION rows in SEAMS for the new 3.x symbols.
7. **Duplicates.** Cut C.2's lattice-sum derivation to a pointer to 3.1, keeping the infinite-crystal form.
8. **Attribution.** 3.5: the norm-conservation condition is Hamann–Schlüter–Chiang's, and Vanderbilt's ultrasoft scheme relaxes it.
9. **The (Zα)² clause.** E.7 and C.15 state that (Zα)² is the size of each term and that the net 1s shift is about a quarter of it (0.26 % for Si, 1.46 % for Ge).
10. **Process artifacts and register.**
    - Remove "keyresult" in prose, "We will…" runs and "representative calculation".
    - Fix every WRONG and GAP item in derivation.md: the C.4 sign, 0.26 %, 4.7 meV, and normalization over one cell in eq:3.5-rhoAE.
    - Add the reader-a items: Δ_xc motivated from piecewise-linear E(N); the unreachable q point stated; and q_min versus q at threshold separated in 3.5 (38 vs 76 keV).
    - Define "semilocal", "Wigner–Seitz cell" and the other undefined terms. Change "rank eight" to "8×8".
11. **Summary.** Re-check it against the revised sections.

## Deliverables
- The revised files.
- A build in /tmp/build-ch03rev with 0 LaTeX errors and no undefined citations; undefined references only to unwritten targets.
- Lint clean (real hits only).
- ledgers/REVIEWS/ch03/revision.md: one row per item → fix → location, with a reason for any declined item. Do not announce fixes in the text.
- Updated SEAMS rows.
- Other agents edit tex/ch05, ch06, ch07 and appE E.14+. Stay out of those.
- Do not commit. Final message ≤ 10 lines.
