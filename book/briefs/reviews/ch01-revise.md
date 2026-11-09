# Chapter 1 revision (one reviser for the chapter)

Revise /home/user/dmdd-solid/book/tex/ch01/s1-1.tex … s1-5.tex, ch01.tex, /home/user/dmdd-solid/book/tex/appC/C-9.tex and /home/user/dmdd-solid/book/tex/appD/D-1.tex. The revision must address **every** item in the four review reports: /home/user/dmdd-solid/book/ledgers/REVIEWS/ch01/{derivation,prose,reader-a,reader-b}.md.

Follow /home/user/dmdd-solid/book/briefs/sections/COMMON.md, STYLE.md, NOTATION.md and READER.md. Keep each section's voice and length: within ±10% of its current length, except where a review asks for added material.

## Editor rulings (apply these; they settle the open questions in the reports)
1. **v_min.** Use the absolute-value form throughout. Replace the signed-form sentence in D-1.tex (line 50).
2. **Aluminium gap.** Quote the physical bulk value 2Δ ≈ 0.36 meV (from T_c via BCS, cited), with m_min ≈ 0.10 keV. Present the 0.6 meV used in some projections as a film value, labelled and attributed.
3. **Silicon constants.**
   - Low-temperature indirect gap E_g(0) = 1.1692 eV, citing Ramanathan & Kurinsky, Eq. (11).
   - Room-temperature gap 1.12 eV, with a fetched public source; otherwise drop it.
   - a = 5.431 Å, citing the CODATA/NIST lattice spacing of silicon (add the bib entry).
   - Remove "1.2 eV".
   - Use one consistent gap per context throughout the chapter.
4. **Folding scale for fcc Si.** Use the shortest reciprocal vector, |G₁₁₁| = √3·2π/a ≈ 4 keV, where the text gives a momentum scale.
5. **Terms used before §3.1 defines them** (Brillouin zone, crystal momentum, reciprocal lattice, folding). In §1.3, give each a one-sentence working definition and point to \cref{sec:3.1}.
6. **§1.2 coordinates.** Define RA, declination and sidereal time. Print the 3×3 rotation that produces the lab-frame direction, so the reader can reproduce the 20.9 h result.
7. **§1.4 QFT notation.** State the absorption couplings as cited results, with equation numbers. Point to App. C.9 and to Chap. 2 for the derivations. Write no QFT derivation here.
8. **Exclusion figure (§1.5).** Name the cutoff function in the caption and the script. Make the quoted minima match the code (verify by rerunning the script).
9. **Citations.**
   - Essig et al. 2016: use one equation scheme everywhere (the η branches are (B.4)/(B.5)).
   - Credit Lee–Weinberg to Lee & Weinberg, not to Lin.
   - Steigman's section is II C.
   - Narrow or drop the Kahn–Lin Table I overreach.
   - Use one citation style throughout.
10. **Chapter structure.**
    - Add the chapter opening outline paragraph in ch01.tex.
    - Remove "thread" wording and hard-coded part numbers (use \cref{part:...}, or write in words).
    - Remove duplicated explanations: say each once and point back.
    - Remove the repeated η equation (keep D.1, point to it).
    - Use curly quotes.
    - Give g_deg its definition.
    - Make every caption stand alone.
    - Strengthen the join from §1.3 to §1.4.
    - Revise the summary.
11. **Numbers.** Apply every WRONG number in derivation.md (|v_⊙|, the yearly m_min swing, edge ratios, the 5% point, x_fo ≈ 22, the 560 km/s statement, and so on). Fix the toy-rate normalisation, which is per ln E_e.

## Deliverables
- The revised tex files, rebuilt.
  - **Lint:** 0 real hits. The banned list now also catches thread, ledger and internal file names.
  - **Build:** no errors and no undefined citations.
- /home/user/dmdd-solid/book/ledgers/REVIEWS/ch01/revision.md: one row per review item → fix → location. Any item you decline must carry a reason.
- Update each ledgers/SEAMS/1.N.md "proposed rows" block with symbols added or renamed.
- Do not commit. Final message ≤ 10 lines.
