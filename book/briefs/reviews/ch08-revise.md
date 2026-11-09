# Chapter 8 revision (one reviser)
Revise tex/ch08/ch08.tex, s8-1.tex … s8-8.tex (the Summary is at the end of s8-8) and tex/appD/D-24.tex … D-28.tex. All paths are under /home/user/dmdd-solid/book.
Address every item of the five reports in ledgers/REVIEWS/ch08/ (derivation-1.md, derivation-2.md, prose.md, reader-a.md, reader-b.md) and of ledgers/REVIEWS/ch08/editor-notes.md, which binds you.
Follow COMMON.md (compute policy: Python model scripts under 10 min are fine; no QE), STYLE.md, REGISTER.md, NOTATION.md and READER.md.

## Editor rulings
1. **8.7 worked example (we:8-pairs).** Rerun figscripts/ch08/we8_pairs.py with narrower broadening, or a broadening-converged scheme, until the photon's mean electron and hole energies add to the shared pair energy (≈ 9.2 eV at 10 eV). Then correct every number and the "a volt" comparison in 8.7 and in the Summary; drop the claim if it does not survive. Cache the script outputs (< 5 MB npz/json) so the numbers can be checked. Do the same caching for the 8.3 PySCF contact-density run.
2. **8.7 symmetry condition.** The in/out equality needs a real symmetric kernel (RPA, ALDA), not merely a Hermitian one, and R_GG′ = R_G′G with the origin at an inversion centre. State both.
3. **8.6.**
   - The Fano coefficients: only their deviations from the mean average to zero, and only when ν runs over all decay channels. Fix 8.6 and D.28.
   - The velocity ratio is taken at equal kinetic energy.
   - Write the remainder in Eq. 8.6-decomp relative to the binned value.
   - Say that the Dirac width comes from dimensional analysis.
   - Explain or fix the 8 % toy-model mismatch.
4. **8.4.**
   - GaAs ionic term −9.2×10⁻⁴.
   - The theorem needs ω ≠ 0 in the clamped case; name the long-wavelength acoustic phonon in its statement.
   - In WE 8.6, "same weight" means the f-sum weight; the peak weight changes by ω_T/ω_L.
   - Define Π_em and "improper response" at their first use.
   - Use one pointer instead of four repetitions.
   - ε_e: keep it as the electron dielectric function in 8.4, and rename 8.7's carrier kinetic energies (e.g. E_e, E_h). Check A.7.
5. **8.3.**
   - The interference sign: say where the positive part sits.
   - The O(q/G) correction without inversion is purely imaginary.
   - The Campbell-Deem wording.
   - D.26: centre-of-mass term at order q⁶.
6. **8.2 and 8.5.**
   - 8.2 states that no standard model produces O₇ at leading order.
   - Give n_B one consistent step size, or explain why it differs by context.
   - Assign the many-body level of DFPT phonons and Born charges explicitly in 8.5.
   - 𝔗 symbols are used in 8.2–8.4 before 8.5 defines them: add a forward clause at first use, or reorder.
7. **8.1.**
   - Say that the operator list is complete for spin-½ dark matter only, and state what changes for other spins.
   - Cite the ²⁹Si abundance (4.685 %, IUPAC/Meija 2016, already in book.bib as meija2016isotopic) and J = 1/2.
   - Remove the Coulomb-energy row, which has no later user, or point it to the section that uses it.
8. **Notation.**
   - The NOTATION 𝓜^k unit is eV^{k+3}.
   - Rates Γ_A/Γ_B/Γ_AB are \varGamma.
   - Rename the projector 𝒬_{n,m} (it clashes with 10.9 and C.20).
   - Resolve the clashes in S⁰, 𝒜, g, 𝖫 (8.8 vs 4.9) and the spin current vs C.20 𝒥.
   - Propose rows in SEAMS.
9. **Citations.** knapen2021dark Eqs. (6), (13); kahn2022searches Eqs. (90)–(92); Ramanathan's distribution is "fitted"; the two citations lacking eq./sect. numbers get them.
10. **Prose.**
    - Rewrite the second paragraph of the chapter opening as argument, not a section list.
    - Cut the repetitions the prose report lists, and 8.6 per its proposed cuts.
    - Remove the production note from the Fig. 8.3 caption.
    - Cite Tab. 8.6 before it appears.
    - Use one percent style.
    - "a volt" → eV.
    - Avoid "We call".
    - Fix the wording slips ("v_F" for Si, "gapless" magnons, k "not a good label").
    - Bring "however" up and "only"/"of order" down, toward REGISTER.

## Deliverables
- Revised files.
- A build in /tmp/build-ch08rev with 0 LaTeX errors and no undefined citations; undefined references only to unwritten targets.
- Lint clean.
- ledgers/REVIEWS/ch08/revision.md, with one row per item → fix → location and a reason for each decline.
- Updated SEAMS rows.
- Other agents are writing tex/ch10 and ch11 and editing appF/F-rows.tex and book.bib. Edit shared files only with exact small insertions.
- Do not commit. Final message ≤ 12 lines.
