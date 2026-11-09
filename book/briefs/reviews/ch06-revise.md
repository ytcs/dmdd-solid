# Chapter 6 revision (one reviser)
Revise tex/ch06/ch06.tex and s6-1.tex … s6-5.tex (the Summary is at the end of s6-5) and tex/appD/D-16.tex … D-18.tex. Touch tex/appA/A-6.tex only for the sum-rule sentence. All paths are under /home/user/dmdd-solid/book.
Address every item of the four reports in ledgers/REVIEWS/ch06/: derivation.md, prose.md, reader-a.md and reader-b.md. Also apply ledgers/REVIEWS/ch06/editor-notes.md, which binds you.
Follow COMMON.md (compute policy: run no QE; the cached data are in figscripts/ch05 and ch06), STYLE.md, REGISTER.md, NOTATION.md and READER.md.

## Editor rulings
1. **Physics.** 6.3: the Fan term can have either sign. Fix the sentence that says it "lowers the energy", and state how the threefold-degenerate silicon valence top is handled: a degenerate-perturbation average, as in E.8, or the formula restricted to the nondegenerate conduction minimum, saying so.
2. **ZPR reconciliation.** Give one paragraph in 6.3, and the Summary, that separates the three silicon scales:
   - −52/−59 meV, the Einstein-model inversions of WE 6.3;
   - −62/−64 meV, from experiment including the 9 meV lattice expansion;
   - −71/−73 meV, the electron–phonon part only.
   Compare the computed −56.2 meV with the right one: it is about 20 % short of the e–ph part. Cite the source or drop the "overscreening" attribution to Zacharias. Fix −59 → −58.
3. **Units.** 6.4's Al empty-core potential must be in the book's Heaviside–Lorentz convention: −3e²/(4πr) and w = −3e²cos(qr_c)/(Ωq²ε). Give the Al force-constant inputs, or point to the script and the measured data that fix them, so that a reader can check λ = 0.436. WE 6.4: 0.396 is 6–8 % below the measured value.
4. **Attributions.**
   - Giustino Eq. (5) is Bardeen 1937 static screening.
   - The spin factor 2: Giustino Eq. (146) has it explicit, Noffsinger explicit, Giustino Eq. (200) implicit. Fix 6.4, D.17 and D.18 accordingly.
   - Li's 10.45 eV/Å is the mean of two combinations.
   - Li's Fig. 5 reaches only 0.1 Å⁻¹.
   - Cite the origin of the "up to 30 %" nonadiabatic correction, or state it as Calandra et al.'s.
   - Add the arXiv number 1007.2098 to the calandra2010 bib entry.
5. **6.2 consistency.**
   - Silicon's interpolated vertex has a quadrupole R⁻³ tail: say so, consistently with GaAs.
   - Piezoelectric coupling comes from dynamical quadrupoles and the piezoelectric tensor; define "dynamical quadrupoles" in one clause.
   - The adiabatic small parameter must agree between 6.2 and 6.4 (ω/E_g vs (ω/E_g)²; derive or reconcile).
   - Show in two lines, or point to, how local fields produce Z*.
   - Tighten the 1/Q² vs 1/q⁴ analogy.
6. **D.18** (per editor-notes):
   - √α is straight per component only.
   - Cut the "confirms to machine precision" sentence.
   - m_e → m*_d, ê → ê_γ, and resolve the W_ab clash.
7. **Notation.**
   - The density operator is 𝓃̂ (\hat{\nd}); change 6.1's \op{n}.
   - Resolve the bold d clash (derivative coupling vs rigid translation) and add a NOTATION row proposal.
   - Bare μ (two reduced masses in 6.1): rename one.
   - D.17's band-width W: rename it.
   - Define ω_opt, m_l/m_t, v_F, E_dir and w at their first use.
   - ω_Ein row: widen it.
   - Resolve the A_ν vs A_TA/A_LA repeat.
   - n_r first use moves to 6.5.
   - 6.3 says ω_D/E_F is "10⁻³ to 10⁻²".
8. **A.6.** Reword "enter sum rules with opposite effects (5.6, 6.3)" to what 5.6 and 6.3 actually show.
9. **6.5.** Add the one-line q_min estimate for the dark-matter threshold window.
10. **Repetition and process.**
    - State the Migdal counting once and point back to it.
    - State the 10 mK gap point once.
    - Cut the reconciliation and numerical-check paragraphs that read as notes to a reviewer.
    - Replace "Modelling" wording; use American spelling.
    - Fix the Summary's Kohn-anomaly attribution and "overlap … with itself".
11. **Register.** Bring 6.4 and 6.5 toward REGISTER.md's frequencies, using the prose report's calibration rewrites.

## Deliverables
- The revised files.
- A build in /tmp/build-ch06rev with 0 LaTeX errors and no undefined citations; undefined references only to unwritten targets.
- Lint clean.
- ledgers/REVIEWS/ch06/revision.md, one row per item → fix → location, with the reason for any decline.
- Updated SEAMS rows.
- Other agents edit tex/ch07, appE E.14+ and the ledgers. Stay out of them.
- Do not commit. Final message ≤ 10 lines.
