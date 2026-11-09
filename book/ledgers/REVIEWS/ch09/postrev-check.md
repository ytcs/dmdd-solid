# Ch09 post-revision check (2026-11-07)

Isolated verifier. Inputs: editor-notes.md (rulings R1–R8), the five reviews, revision.md; tex/ch09/*.tex, figscripts/ch09/*, tex/ch22/s22-2.tex, s22-summary.tex, figscripts/ch22/gaps22_2.py, tex/appF/F-rows.tex, NOTATION.md.
Method: all scripts were rerun on a scratch copy of tex/ and figscripts/. atlas9_1.log, fig9_1.log and gaps22_2.log came out byte-identical. fig9_2.log differs only in its output path. fig9_3.py regenerated tab9-3.tex identically, also when pointed at the new build's main.aux. Key numbers were recomputed by hand, and the tex was parsed independently. Nothing outside this file was edited.

## 1. Rulings

| Item | Verdict | Evidence / fix |
|---|---|---|
| R1 three filled cells | CONFIRMED | core × vector abs. → 10.7 (10.7 runs absorption "through the L and K edges"); chiral × vector abs. → 14.5 (single-molecule magnets, dark-photon B field and E-field dipoles); body acoustic × vector abs. → 11.8 (sec:11.8-bar, piezoelectric plate). |
| R1 mobile defects → 19.6 | CONFIRMED | 19.6 has sec:19.6-defecton and sec:19.6-crowdion, so keeping "defectons" in the gloss is justified. The row is empty by construction, and its own paragraph in 9.1-empty says why. |
| R1 single phonon × n_e | CONFIRMED | stays 11.2; the caption points to the 10.2 acoustic peak. |
| R1 eight ○ cells | CONFIRMED | My own parse of the tabular gives 24 rows: 57 filled, 8 ○, 79 "—" (= 144). Columns are 14/6/8/14/10/5. The ○ cells sit at core, Migdal, phonon-assisted, superconductors, Dirac, Frenkel and dopants × spin, plus free recoil × n_e, exactly the derivation-1 list. ○ is defined in the caption. |
| R1 counts | CONFIRMED | 57/8/79 are identical in 9.1 (l.14, l.90), WE 9.1 and the summary. Dark photon: 14 + 6 + 14 + 3 = 37 of 57, matching atlas9_1.log. |
| R2 Ch22 row | CONFIRMED | One grouped row under a new "Chap. 9" group, class unsized, section sec:9.1. A parse of the longtable gives 74 data rows: unsized 39, estimate 17, bounded 10, test 5, proof 3. gaps22_2.log: calc 56, meas 11, theory 7, Ch8–9 4 rows. |
| R2 Ch22 consistency | CONFIRMED | s22-2: 74 (×2), 71, 10/17/39/5, 56/11/7. s22-summary: 74 (×2), 71, 39, 56/11/7, 16 of 19, 14 of 17. No stale 73/70/38/55 anywhere in tex/ch22. s22-1 prints no count of tab:22-gaps. |
| R3 Al edge | CONFIRMED | ρc² = (C11 + 2C12 + 4C44)/3 with 114.3/61.9/31.6 GPa (s20-3) and 2.73 g/cm³ gives 6.671 km/s. 2C44/(C11 − C12) = 1.21 > 1, so [111] is the fastest direction. Edge at 1 meV = 8.550 keV → 8.6 keV. Both captions say 6.67 km/s along [111]. |
| R3 ZrTe₅ | CONFIRMED | Velocities 1.1e-3, 4.5e-4, 1.0e-3 (16.1 l.64) give 9.58, 7.12 and 8.99 keV. The slow axis gives 7.1 keV. 16.1 prints "9.6, 7.1 and 9.0" and isotropic 8.0. Equivalent Si threshold 1.16 meV. |
| R3 46.8 MeV | CONFIRMED | μ = (M E_g/2)^½ / v_max = 46.68 MeV, so m_χ = 46.76 MeV (M = 26.161 GeV). Same value in the 9.2 opener, 9.3 l.18 and the summary. |
| R3 plasmon | CONFIRMED | ω_p = 16.6 eV, k_F = 3.57 keV, ω² = ω_p² + (3/5)q²v_F² meets qv_F + q²/2m at 2.24 keV and 20.55 eV. Phase speed 9.18e-3 = 3.46 v_max, printed "9.2e-3, 3.5 v_max". The same dispersion is used in 9.2, 9.3, the Fig. 9.2 caption and WE 9.3. 10.3 l.72 prints 2.24 keV; q_c = 2.60 keV is named once as the Lindhard zero. |
| R3 halo shift 3.1 % | CONFIRMED | δln v = 25/794.5 = 0.03147. The free-nucleus exponent 1.0005 gives 3.148 %, which rounds to 3.1 % (the acoustic edge is 3.18 → 3.2 %). |
| R3 Ge 0.420 | CONFIRMED | 1898²/[2(1898·v_max − 0.744)] eV = 0.4203 MeV; fig9_1.py uses q = 1898 eV. |
| R3 Si 2p 28.6 MeV | CONFIRMED (the rounding change is right) | 2(99.4 + 1.17 eV)/v_max² = 201.14 eV / 7.0234e-6 = 28.64 MeV. The old 28.7 came from the rounded 38 keV: 2·38/v_max = 28.68. The one-line explanation is present. |
| R3 random / two-magnon | CONFIRMED | Both are placed on the floor: 0.285 keV at 1 meV, 21.5× below the Si acoustic edge and 5.13× below NiO one-magnon at 1 meV. The reason is stated. |
| R3 halo exponent | CONFIRMED | The stationary condition q̄v = 2E − q̄E′ is stated, and the linear branch is named as a constrained minimum. Exponents −2.37 and −2.12/−2.74 match the log. |
| R4 80/75 | CONFIRMED | "test 80 of them in 75 boxes" (9.4 opener), "Eighty belong to the 75" (9.4-appF), "80 are tested in the 75 boxes" (summary). fig9_3.log: 90 rows, 10 no-box, 80 boxed, 75 distinct boxes, 6 unsized. |
| R4 reclassification | CONFIRMED | Rerun fig9_3.py: nB 12.4b; TM includes 10.3a and 11.5c. Label 25 = 1+0+2+11+1+6+2+2; qualifiers 50 = 5+9+5+31. Ch10 7/15, Ch11 6/20, Ch12 7/9, Ch14 0/8, Ch16 2/17. 9.4 text and summary match. 9.4 states why 10.3a and 11.5c are target-model steps. |
| R4 App F column 1 | CONFIRMED | My own parse of F-rows.tex: all 23 rows of Ch10 (16) and 11.1–11.2 (7) carry "(\cref{lim:…})" in column 1. fig9_3.py asserts that all 80 boxed rows name a box. |
| R4 summary definition / Migdal | CONFIRMED | The definition covers "a parameter that the label records in words". "Every Migdal scattering formula sits at n_B = 2". 2.9e-3 is in 12.4. |
| R4 follow-on | CONCERN (tracked) | 12.4 l.137 and the App F rows of lim:12.4b, 10.3a and 11.5c still give the old placement, so Ch12 and App F disagree with 9.4 until the Ch12 light pass and the App F completion. Revision.md already lists these; keep them on the cross-chapter list. |
| R5 WE 9.1 | CONFIRMED | "three of the last" (10.9 + 17.3 plasmons + 17.3 phonons). The nuclear column is complete: phonons and multiphonons, free recoil with Z_κ², color centers, solid helium and Migdal = 6. Tally 14/6/14/3 = 37. |
| R6 GaAs Fano, NiO, WE 9.3 | CONFIRMED | 13.6 states "a few percent at most of the first emissions". tab:9-supports says 4.54 meV is "measured". "inside the window by 11 meV" matches fig9_2.log. |
| R6 Si direct gap | CONFIRMED | 3.4 eV everywhere (3.3, 10.7, 13.8). 3.17 eV is explained as the scissor-shifted E_min(q → 0). |
| R6 tables, phonon passage, criteria | CONFIRMED | knapen2021dark is cited and "published tables" is gone. q̄ = 0.882 keV, k_c − q̄ = 1.058 keV, TA 14.8 meV, and 18.3 meV at k_c (13.1). The 2.3 / 4 / 9 phonon-energy criteria are each named with their use. |
| R6 free-nucleus absorption | CONFIRMED | (E + M)² − p² = M² ⇔ m_φ² + 2E_φM = 0, which is correct. The energy fraction m_φv²/2M is right. |
| R6 closed channels, dark Compton, NiO | CONFIRMED | Two closed channels (Si bulk plasmon, narrow-gap III–V pairs), both in populated cells. φe → γe matches 10.8. |
| R7 opening, artifacts, symbols, \cref | CONFIRMED | Paragraph 2 is motivation. No "Status:" line, misprint assurance or bookkeeping clause remains. g₃₃, g_c, ⟨ω⟩, ⟨ω_e⟩, δM_κ/M_κ and q₀ are defined. No bare c. \cref{app:F} is used in the text and the summary; the 9.4-appF title avoids naming the appendix, which is acceptable. |
| R7 repetitions | CONCERN (minor) | WE 9.1 still says silicon closes the single phonon twice ("in silicon, with Z*_κ = 0, the cell is empty" and "A material can still close a lattice cell, as silicon closes the single phonon"), besides "nothing in silicon" for absorption. Fix: delete the sentence "A material can still close a lattice cell, as silicon closes the single phonon." in the WE's last paragraph. |
| R7 register | CONFIRMED | "therefore" ×4 (ch09, s9-2, s9-3, s9-4 once each); "only" 8 in s9-2 and 6 in s9-3. |
| R8 NOTATION | CONFIRMED | Rows m_min^ch, E_ch(q), q̄, ○ (NOTATION l.773–778); entry 95. check_notation.py: GAPS 0. The one bare m_min in 9.2 is the threshold mass of eq:1.3-mmin, as the row allows. |

## 2. Cross-chapter numbers (31 sampled; each checked in the cited section's tex)

CONFIRMED, with the section where each was found:
- 14.1: c_M 1.36e-4; 7.3 keV at 5 meV; 4.54 and ~0.6 meV; top 118 meV. 14.2: 236 meV. 14.3: MnF₂ 1.1 meV; 116 µeV/T.
- 16.1: Δ_D 11.8 meV; 2Δ_D 23.6 meV; 8.0 keV (isotropic); 9.6/7.1/9.0 keV; axis velocities. 7.3: 15.6 meV (relaxed cell).
- 13.1: 0.3332/0.3374; 0.2119–0.2141; 0.433–0.436; 0.517–0.560; Ge 0.32; 14.8 meV; 1057 eV; 18.27 meV. 13.9: 0.405–0.408. 13.8: 1.1728 eV; 14.7 meV.
- 11.4: E_R 164 meV at 92.5 keV; 17.5 MeV; x_R ≥ 2.3 at q ≥ 70 keV; ⟨u_x²⟩ 2.45e-3 Å². 17.1: Ge 21.3 MeV; Ge edge 10.2 keV.
- 17.6: GaAs 10.3–12.3 keV. 17.5: diamond 3.1 keV. 11.1: 44 × edge. 17.3: 12–28 % and 1 %; Si optical 18.3 keV.
- 10.6: Ge 3d 29.2 and 29.8 eV. 12.1: 2.7e-4 and ~6 eV. 12.4: 2.9e-3. 17.4: 5.47e-4.
- 14.6: 26.8 mT, 241.8 kHz. 14.5: q g₃₃ = 7e-5 at 2.1 eV. 16.2: 3.4–6.9 v_max. 16.3: PbS 1.2 eV, graphene 4.3 eV. 16.4: anthracene 3.1 eV. 16.5: 45.59 meV. 16.6: 4.75 eV. 16.7: 1e20 eV⁻¹cm⁻³.
- 10.1: 0.05 / 0.22 / 0.47. 10.2: > 10⁴. 13.6: 1.184–1.467 eV at 1 keV, closes 1.27 keV, reopens 3.30 keV. 11.5: below 3 meV. 20.3: Al 0 K constants and density. 5.2: 9.35 and 5.84 km/s.
- 10.3: 18.9 eV at 0.5 keV → 22.3 eV at 2.45 keV. **CONCERN (wording):** 9.3 l.22 appends "\SI{2.5}{eV} above the measured value" right after 22.3 eV, so it reads as 22.3 − 2.5. 10.3 says the *small-q* peak (18.9 eV) is 2.5 eV above the measured 16.4 eV. Fix: "…to 22.3 eV at 2.45 keV; their small-q peak lies 2.5 eV above the measured 16.4 eV because of the shift that sets their gap".
- 5.2 (Part I) via 9.1 l.94: **CONCERN (small factual):** "c_ν between 2×10⁻⁵ and 3.1×10⁻⁵ in silicon" is wrong at the lower end. 5.2 gives the slow TA branch along [110] as 4.67 km/s = 1.56×10⁻⁵. Fix: "between 1.6×10⁻⁵ and 3.1×10⁻⁵". The conclusion "some 10⁻⁸ of the boson mass" is unchanged.

## 3. Reader rule

CONFIRMED (spot-check). Forward pointers carry glosses, for example "(\cref{sec:11.6}, which treats such random couplings)", "(\cref{sec:14.1}, which computes the one-magnon rate of NiO)", "(\cref{sec:17.6}, which ranks the targets…)", "\cref{sec:22.2}, which collects the open items" and "\cref{sec:19.6}" with "defect kinetics".
Part II formulas that Ch9 uses are restated inline: E^PA_min = E_g + ω_TA(k_c − q), the Migdal moment estimate and Lewin–Smith with Helm. WE 9.4 limits itself to the assumptions of the three rates.
"Conserving" and the 𝔗 components are glossed at first use. A bare citation such as "(\cref{sec:16.1})" for the ZrTe₅ velocities is a source pointer, not a result used without explanation.

## 4. Regressions

- Process words: CONFIRMED. No SPINE/SEAM/ruling/draft/LE- strings in tex/ch09. The only comment is the generator header of tab9-3.tex.
- Lint (lint.py --banned BANNED-TERMS.txt, ch09.tex + s9-*.tex): CONFIRMED, 20 hits and 0 blocking. All are LONG-SENT in captions, table rows and enumerations, plus one DASH hit on a tabular preamble.
- Overfull boxes in Ch9: CONFIRMED none. Only underfull boxes in table cells. The 13 pt overfull just before Ch9 belongs to the Ch8 bibliography (Commun. Math. Phys. DOI). The float that is 34.6 pt too large is in ch10/s10-10.tex l.55. Neither is in scope.

## 5. Build

CONFIRMED. `latexmk -pdf -interaction=nonstopmode -outdir=/tmp/claude-0/build-ch09post main.tex` exited 0 with all targets up to date and no extra pass needed. The result is 1836 pages, 0 LaTeX errors, 0 undefined citations or references, and 0 biber warnings.
Numbering: tab:9-atlas 9.1, tab:9-edges 9.2, tab:9-overlaps 9.3, tab:9-supports 9.4, tab:9-limitchecks 9.5; fig:9-kinmap 9.1, fig:9-qomega 9.2, fig:9-axes 9.3.

## Verdict

ACCEPT once three small text fixes are made. None of them changes a count, a table or a script:
1. s9-1 l.94: "between $2\times10^{-5}$" → "between $1.6\times10^{-5}$".
2. s9-3 l.22: reattach "2.5 eV above the measured value" to the small-q peak (wording above).
3. s9-1 WE 9.1, last paragraph: delete "A material can still close a lattice cell, as silicon closes the single phonon." (R7 repetition).
Tracked, not blocking: the 12.4 / App F placements of lim:12.4b, 10.3a and 11.5c (Ch12 light pass and App F completion).
