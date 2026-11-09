# Chapter 7 revision (one reviser)
Revise tex/ch07/ch07.tex, s7-1.tex … s7-4.tex (the Summary is at the end of s7-4) and tex/appD/D-19.tex … D-23.tex. All paths are under /home/user/dmdd-solid/book.
Address every item of the four reports in ledgers/REVIEWS/ch07/ (derivation.md, prose.md, reader-a.md, reader-b.md) and of ledgers/REVIEWS/ch07/editor-notes.md, which binds you.
Follow COMMON.md (compute policy: run no QE), STYLE.md, REGISTER.md, NOTATION.md and READER.md.

## Editor rulings
1. **Physics and number errors.**
   - D.19 Bogoliubov coefficients: (|S|A₀/2ω^M)^{1/2}.
   - 7.3: the continuum edge lies above v_D q, not "the slope never falls below v_D". Call the bands slow, not "steep"; the threshold is 10.5 keV; the edge is not "a pair at rest".
   - 7.2: threshold numerator Δ²±Δ² (jump π/2); "the ratio falls as the mass grows" applies to the typical ratio, not the maximum.
   - D.23: the orbit is oblate; the p levels agree to 0.4 %.
   - 7.4: the T-center hole binding is 34.78(15) meV (the cited paper's measurement), with the older 22–32 meV estimates identified as such.
   - WE 7.3: the expansion parameter must use the definition the text gives (0.93), or the text must define it with 2Δ_D.
   - WE 7.4: 7.7×10⁻⁴.
   - The dos Santos 14 % refers to the maximum magnon energy.
   - Summary: use 31.3 meV, consistent with the text.
   - t/U range: 0.05–0.06.
2. **Notation.**
   - Dirac matrices α_D, β_D everywhere (bare β is inverse temperature).
   - Doublet Pauli matrices σ^{d}_i, consistent with 7.2's remark about σ.
   - Dressed vertices \mathsf{V} in 7.2 and D.21, not \varGamma or upright Γ.
   - Use δk for k − k₀ in 7.3, not bold κ.
   - Resolve the clashes in E₀ (7.1), ω₀ and E_d (7.4), 𝒩_s (vs E.11), the γ symbols, and a (lattice constant vs orbit radius).
   - D.19's Fourier sign must agree with 7.1.
   - D.23: Coulomb term in Heaviside–Lorentz, ε for the dielectric constant (not ε₀, which reads as vacuum permittivity).
   - Propose NOTATION rows in SEAMS 7.*.md.
3. **Gaps.** Add one-sentence explanations:
   - Goldstone counting;
   - the Anderson–Higgs name;
   - what A₁/E/T₂ label;
   - NiO as a charge-transfer insulator.
   Slow down the k·p→Dirac reduction and the Ward-identity paragraph for the first-year reader. D.20 "as one checks": show the step.
4. **Prose.**
   - Remove the roadmap endings of the four section openers.
   - State repeated facts once (e.g. 0.36 meV / 0.1 keV) and point to them afterwards.
   - Cut the numerical-precision reassurances ("to machine precision", "to 10⁻¹²").
   - Bring "gives" toward REGISTER's rate.
   - Fix the comma after eq:7.1-dirac and "the 1s triplet".
5. **Silicon ε.** Keep 11.7 book-wide. The 11.4 note in 7.4 stays as written.
6. **ZrTe₅.** Use α̃ ≈ 0.19–0.20 with g_deg = 2, consistent with E.20.

## Deliverables
- Revised files.
- A build in /tmp/build-ch07rev with 0 LaTeX errors and no undefined citations; undefined references only to unwritten targets.
- Lint clean.
- ledgers/REVIEWS/ch07/revision.md: one row per item → fix → location, with a reason for each decline.
- Updated SEAMS rows.
- Other agents edit the ledgers and some ch05/appD/appE spellings (a sweep of "nonadiabatic" and "translation invariance"). Stay out of those files.
- Do not commit. Final message ≤ 10 lines.
