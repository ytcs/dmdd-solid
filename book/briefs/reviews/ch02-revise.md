# Chapter 2 revision (one reviser for the chapter and its appendices)

Revise /home/user/dmdd-solid/book/tex/ch02/ch02.tex and s2-1.tex … s2-5.tex, /home/user/dmdd-solid/book/tex/appA/A-1.tex … A-9.tex and /home/user/dmdd-solid/book/tex/appD/D-2.tex, D-3.tex. Address **every** item of the four reports /home/user/dmdd-solid/book/ledgers/REVIEWS/ch02/{derivation,prose,reader-a,reader-b}.md, plus /home/user/dmdd-solid/book/ledgers/REVIEWS/ch02/editor-notes.md.

Follow COMMON.md, STYLE.md, REGISTER.md (apply rewrites R9 and R10 in §2.1, and bring §§2.1 and 2.3 to the model's word frequencies), NOTATION.md and READER.md.

## Editor rulings
1. **Si optical phonon at Γ: 64 meV book-wide.** Recompute the §2.5 numbers (n_B(300 K) = 0.092, the ratio 11.9, 10⁻⁸¹ at 4 K) by rerunning fig2_6.py. Grep Chapter 1 and Appendix A for the Si optical phonon and align them. Leave the stated toy-model ω₀ in the §1.3 limit box alone, because it is a labelled model.
2. **The Si gap.** Use one value per context, following the Chapter 1 convention: 1.11 eV as the projection threshold, 1.12 eV at 300 K, 1.1692 eV at low temperature. Remove bare "1.1 eV".
3. **α against v.** "α is about ten times the dark-matter speed", not a hundred. Fix it in Chapters 1 and 2 (the reader found it on three pages).
4. **The §2.4 sign.** The inner time-integral numerator is +i. Fix that display only.
5. **Symbols.**
   - Target states are |i_T⟩ and |f_T⟩, not a/b.
   - Resolve the clashes: s species vs spin s, z_κ vs Z_κ, Z for the residue in D.3, and V, β, ξ, Ω each carrying two meanings. Name each one per NOTATION, and propose rows.
   - A.9 uses σ_T and μ_χe.
   - v_C has an upright C (A.2, §2.3).
6. **Nuclear levels.** Correct the sentence: ⁷³Ge has its first excited state at 13.3 keV. State the actual range with a source.
7. **Textbook pointers** (Sakurai–Napolitano, Cohen-Tannoudji, Peskin–Schroeder, Fetter–Walecka, Landau–Lifshitz, Jackson). Cite them at chapter level only. Never cite a section number that has not been checked. Bernreuther's DOI is 10.1088/1475-7516/2024/03/047.
8. **The §2.2 limit box.**
   - The hydrogen result does not contradict Essig et al., whose 30% applies to xenon and argon outer shells. Say this in one plain clause.
   - Fix or remove the unconfirmed "quarter at 10 E_B" (the checker finds 0.29–0.34).
   - Fix the Duda citation: it is Sect. V.
9. **Process artifacts.**
   - Remove every pattern-19 sentence the prose report lists, including "These numbers are printed by the script of …" (§2.2) and the A.2, A.4, A.6, A.7 and A.8 items.
   - Delete the process comments (the LaTeX comment lines "% Sections are \\input here as they are accepted" and "% Appendix sections are \\input here in order as they are accepted") in ch02.tex, appA.tex and appD.tex, and in ch01.tex and appC.tex if they are present there.
10. **Chapter level.**
    - The opening stays motivational and stops walking through the sections in order.
    - The summary gives §2.4 its due: time orderings, Wigner–Weisskopf decay, and the cascade plus the finite part.
    - Fix all the small numbers and steps: 2.3e-8, 950/953, v_max vs v, j₁ named, and the one-line steps for the rotating frame, the f_ion Jacobian, the factor ½, and dω = E_ej d ln E_ej.
    - Fix the cross-reference pointers (A.8 → sec:2.5).
    - Make Worked example 2.6 match its equation.
11. **Stale SEAM.** Update SEAMS/1.5.md: 74 events. Fix §1.4's radius: use silicon's Helm radius of 3.47 fm, or name germanium.

## Deliverables
- The revised files.
- Build in /tmp/build-ch02rev: no errors and no undefined citations.
- Lint clean (real hits only).
- /home/user/dmdd-solid/book/ledgers/REVIEWS/ch02/revision.md: one row per item → fix → location, and a reason for any item you decline. Do not announce fixes in the text itself.
- Updated SEAMS proposed rows.
- Do not commit. Final message ≤ 10 lines.
