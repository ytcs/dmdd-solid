# Language audit: appendices (reviser log)

Brief: briefs/reviews/language-audit.md, reviser role. Ledger: ledgers/REVIEWS/language/appendices.md. Edits only in tex/app* (B-1 and B-3 untouched) and one check script (figscripts/appD/check_D_b.py). Every replacement was an exact string match that occurred once in the file it was applied to.

## Global
- G1 (MUST) done: "This appendix" → "This section" at line 3 of the 28 listed D files. The same fault also appeared twice in D bodies, so those were changed as well: D-19:13 "every lattice of this appendix" and D-40:38 "the model of this appendix" now say "this section". No "this appendix" is left in tex/appD.
- G2 (OPTIONAL) done: "momentum transfer" now replaces bare "transfer" at A-3:69, in the A-4 subsection title, and at A-6:65, A-7:10, B-2:72, C-17:95 and E-13:81. E-13:40 is left as it was, as the ledger advises.
- G3: no mechanical sweep was made, as instructed. The rewrites below avoid adding "so"/"therefore".
- G4 (editor's call): not applied. appA, appC and appD still have no opening paragraph.

## App. A
- A1 (MUST) A-2:17 done. Checked against eq:A.2-SL: the form with e² has no 4π.
- A2 (MUST) A-3:74: the sentence is deleted.
- A3 A-1:7: now reads "Four constants suffice; their values follow …".
- A4 A-4:12, A5 A-5:10 and A6 A-8:13 done as the ledger proposed.

## App. B
- B1 B-2:64: the count-teaser is replaced by the four conventions, named. appB.tex has no items.

## App. C
- C1 (MUST) C-1:24 and C2 (MUST) C-5:3 done.
- C3 C-3:3, C4 C-8:3 and C5 (C-10:3, plus D-46:17 "is supported on") done.
- P3 (editor ruling) C-20:3: now reads "a hopping rate that, for weak coupling ($\alpha_{\mathrm{ohm}} < \tfrac12$ in \cref{eq:C.20-ohmrate}), grows as the temperature falls".
- P2 (editor ruling) C-6:67 now uses $M = \SI{26.16}{GeV}$, the mean atomic mass of natural silicon, and cites \cref{sec:5.3} instead of we:1-nuclear, which uses ²⁸Si. The quoted value is unchanged: $q = (2M\omega_0)^{1/2}$ is 56 keV with either mass.

## App. D (besides G1)
- D1 (MUST) D-24:3 and D2 (MUST) D-36:3 done.
- D3 D-12:3, D4 D-29:3 and D5 D-47:3 done. Both D-29 and D-47 do end with the subsections that the new sentences name.
- D6 D-1:3 and D-1:89 now say "the values/parameters of \cref{app:A.8}". D7 D-39:3 and D-39:24 done.
- P1 (editor ruling) D-13:3 now reads: "A silicon nucleus is $5.12\times10^4$ times heavier than an electron, with $M = \SI{28.0855}{u} = \SI{26.16}{GeV}$ for the natural isotope mixture, as in \cref{sec:5.3,app:C.6}. Held by force constants of the same electronic order, it vibrates $(M/m_e)^{1/2} \approx 226$ times more slowly than the electrons move, …".
- P2: the mass in D-13 changed from 26.06 to 26.16 GeV, which changes M/mₑ from 5.10 to 5.12 × 10⁴. figscripts/appD/check_D_b.py now also computes the natural-abundance mass and asserts the values the text quotes: M = 26.16 GeV, M/mₑ = 5.12×10⁴ and √(M/mₑ) = 226.3. Its κ_BO assertions stay at ²⁸Si because they check the Sect. 5.1 values, which D-13 does not quote. Rerun: "all checks passed".

## App. E
- E0 (MUST) appE.tex:35 done: the sentence now reads "The specifications of \crefrange{app:E.14}{app:E.27} share one rule: …".
- E1–E12 (MUST) done: E-19 "parts" (×3), E-24 "stages", E-5, E-16, E-25:3, E-8:85, E-12:20, E-12:99 (the following sentences shortened as well: "that sound speed", "the subject of the memory-loss arguments", "The surface parameters are fits …"), E-6:92, E-8:97, E-13:85 and E-22:57 (both "pitfall" labels removed).
- E13–E25 (OPTIONAL) all done:
  - E13: the remaining "pitfall" sentences in E-22, E-24, E-4 and E-1.
  - E14: "machinery" replaced in E-4 and E-21.
  - E15: in E-10:64 the restated controls are deleted and the next sentence reads "\Cref{app:E.11} extends …".
  - E16: "engine" (×2) and "recipe" replaced.
  - E17 to E25: E-9:103, E-1:3, E-3:3 (split and recast), the E-3 caption, E-19:3, E-14:3, E-17:11, E-1:153 (deleted) and appE.tex:3.
- P2 (editor ruling) E-18:3: the mass is now stated: "$\delta M/M = 2.73\times10^{-4}$ for natural silicon ($M = \SI{26.16}{GeV}$, \cref{sec:5.3})". No number changes; the ratios already implied 26.16 GeV.
- Note: ch01 (s1-3, s1-4) and ch08 (s8-5) still use 26.06 GeV for ²⁸Si. Those files are outside this scope and belong to the chapter revisers.

## App. F
- F1 (MUST) appF.tex:2 and F2 (MUST) F-rows.tex:2 ("set in landscape" deleted) done.
- F3: the Leading-correction sentence is moved unchanged to the end of the appF.tex opening paragraph. \Fsize is defined in macros.tex, so it works there. F-rows.tex now starts with its comment line, then \begin{landscape}.

## appD.tex:29 `\setcounter{section}{27}`
Removed. Before the edit, a baseline build (/tmp/claude-0/build-langA-base) recorded the D numbering. After removing the line, the main build reproduced it exactly: all 47 \newlabel{app:D.n} entries match, and so do all 316 labels numbered D.* (sections, subsections, equations), with the same numbers before and after.

## Checks
- Lint (lint.py --banned BANNED-TERMS.txt, all files in scope): 557 hits, 0 blocking. The only language hits are the known ones: the A-1:45 PERIPHRASIS false positive and the D-11 MONOTONY. The rest are EQ-PUNCT, LONG-SENT in table cells, and "landscape" (the environment name) in F-rows.
- Build: `latexmk -pdf -outdir=/tmp/claude-0/build-langA main.tex` finished with exit 0 and stable files, giving 1840 pages, 0 LaTeX errors, 0 undefined references and 0 undefined citations. The baseline also had 0 undefined references.
