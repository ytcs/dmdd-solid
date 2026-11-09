# Chapter 4 revision (one reviser for the chapter and its appendices)

Revise /home/user/dmdd-solid/book/tex/ch04/ch04.tex and s4-1.tex … s4-9.tex, and tex/appD/D-6.tex … D-12.tex. Touch tex/appC/C-5.tex … C-7.tex and tex/appA/A-7.tex only where a report names them. Address **every** item of the five reports in ledgers/REVIEWS/ch04/: derivation-1.md, derivation-2.md, prose.md, reader-a.md and reader-b.md, plus ledgers/REVIEWS/ch04/editor-notes.md. The editor notes bind you.

Follow COMMON.md, STYLE.md, REGISTER.md (bring 4.6 and 4.9 toward the model's "however" and "we" frequencies), NOTATION.md and READER.md.

## Editor rulings
1. **K^x relabel.** D.12 must call the exchange kernel without its G = 0 term K^x, and the full one K^x_full; drop K̄^x everywhere. Then make 4.9's claim of equality with D.12 true. Fix the direct-kernel index order in D.12 eq:D.12-crystal and 4.9 eq:4.9-kernels to the general (non-inversion-symmetric) form that derivation-2 gives. Put the conjugate into the exciton oscillator strength in App. E.6, as |Σ A ρ*|².
2. **4.7 eq:4.7-ImSigma.** Im Σ^R = −π𝖠/|𝖦^R|². Add the +i/V prefactor rule for the time-ordered response to the 4.8 key result and to D.11.
3. **Bruus–Flensberg.** Cite it without chapter numbers in 4.7, 4.8 and D.11, unless you verify the table of contents.
4. **Mermin causality.** Add the short no-growing-mode proof from derivation-1 to D.9, and a one-line pointer to it in 4.5.
5. **Renames.** In WE 4.1 use λ_osc, Δ_tl and the oscillator mass per NOTATION. Use \SpecA for 𝖠. Write g_deg = 2 throughout Ch4. Fix the notation drifts the reports list, and propose NOTATION rows in ledgers/SEAMS/4.*.md for the symbols that have none.
6. **Process artifacts.** Cut the "numerical check confirms to 10⁻ⁿ" sentences the prose report marks for cutting, and keep at most one per section where it teaches. Remove "In this section we" and the list opening of 4.8. Replace the 4.6 title "RPA, local fields and TDDFT kernels" with a short noun phrase without undefined abbreviations. Strengthen the join from 4.6 into 4.7.
7. **Figures 4.7 and 4.11 (empirical-pseudopotential models).** A figure-pass agent is regenerating Fig. 4.7 from Quantum ESPRESSO, and it will edit the Fig. 4.7 caption and WE 4.11 in s4-6.tex. Do not change those two passages; re-read s4-6.tex before every edit there. Fig. 4.11 stays a labelled model. Move into the text (not only the caption) the explanation that its bands already contain the exciton shift. Add published first-principles BSE spectra and ε∞ values for comparison with a citation (e.g. Albrecht et al. 1998, Onida–Reining–Rubio 2002), and fix the "17 % → 11.9" arithmetic. The silicon ε∞ model values appear six times; keep them in WE 4.11 and Fig. 4.7 only, and point to those elsewhere.
8. **A.7** "first term" → "resonant term" (the old editor note).
9. **Exciton summary.** State that μ_x is inferred from the measured 14.7 meV, not predicted.
10. Fix every WRONG and GAP item in the derivation reports, including the plasmon limit-box caption (below 3×10⁻⁴ only for q < 0.30 k_F), the GaAs WE numbers (3.74 meV, 14.9 nm), 6.26 keV, and the unit and wording gaps.

## Deliverables
- The revised files.
- A build in /tmp/build-ch04rev with 0 LaTeX errors and no undefined citations; undefined references only to unwritten targets.
- Lint clean (real hits only).
- ledgers/REVIEWS/ch04/revision.md: one row per item → fix → location, with a reason for any item you decline. Do not announce fixes in the text itself.
- Updated SEAMS proposed rows.
- Other agents edit tex/ch03, ch05 and the Fig. 4.7 parts of s4-6.tex. Stay out of them.
- Do not commit. Final message ≤ 10 lines.
