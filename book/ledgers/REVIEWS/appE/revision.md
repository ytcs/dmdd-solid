# Appendix E revision log (2026-11-02)

Scope: tex/appE/appE.tex, E-1 … E-13; tex/bib/book.bib (4 new entries, kim2020quickstart → journal version); NOTATION.md row 16.8 (α_ohm, K_b; ruling);
ledgers/SEAMS/E.1-E.3, E.4, E.5, E.6, E.7-E.10, E.11, E.12, E.13. Sources fetched to sources/review-appE/ (xdb-sec1-1.txt, xdb-table1-1.txt; rev/1404.3101, 1912.04893, 2302.06325; PDFs deleted).
Build: /tmp/build-appErev, 0 LaTeX errors. Undefined citations: none from App. E (five keys cited by the concurrently written tex/appD/D-17.tex — allen1972neutron, allen1976theory, allen1981temperature, calandra2010adiabatic, migdal1958interaction — not touched). Undefined refs only to unwritten sections (Chaps. 8, 10, 12–21, sec:3.4–3.6, 4.4–4.9, 5.x, 6.x, 7.x, App. B.2, C.18, D.7, D.15, D.23, app:E.14, app:E.27).
Lint: 0 blocking; remaining EQ-PUNCT (E.4:98, E.9:12/63, E.10:57, E.13:45) are the displays that run into the next clause, already identified as false positives; LONG-SENT hits are table/equation merges.

Key: B = brief ruling, N = editor-notes ruling, D1/D2 = derivation reports, P = prose, R = reader-bc (N1–N8 its numbered items), C = coordinator message.

## Brief and editor rulings
| item | fix | location |
|---|---|---|
| B1 opening | adapted 143-word opening: what the numbers are, methods (\crefrange E.1–E.13) and specifications (E.14–E.27, no titles), 𝔗 components n_B, n_g, n_A, n_T, 𝒳 and 𝔗₀ with \cref{sec:8.5} | appE.tex |
| B1 comment line | no comment line was present in appE.tex; nothing to delete | appE.tex |
| B1 summary | `\section*{Summary}` after E.13 (base calculation, converge on the quantity, three bookkeeping rules, Si uncertainties) | appE.tex |
| B2 Poncé | Poncé rescales to the measured value it adopts, 11.94; book value 11.7 called the low-temperature measurement | E-4 Born-charge subsection |
| B3 Garza | 0.38 eV over 41 compounds, 0.18 eV for typical semiconductors at low T; doubled phrase removed | E-1 Functionals |
| B3 PseudoDojo | mean ≈ 0.7 meV/atom (excl. Cr, Mn, Fe) vs 1.4 meV for earlier NC tables | E-2 Testing |
| B3 SG15 | parameters presented as inputs of the book's calculation as listed in the files; paper cited only for the library and its construction | E-2 Construction |
| B3 Noffsinger | "norm-conserving" → "plane-wave pseudopotentials" | E-4 we:E-dfpt-si |
| B4 v_C | v_{\mathrm{C}} everywhere (E.1, E.3) | E-1, E-3 |
| B4 𝔗 components | NOTATION row gives no upright form → italic n_B, n_A, n_T, n_g in all sections (E.4, E.6 changed); each n_T use glossed with the 8.5 meaning (zeroth thermal order; n_T = 1 first order in n_Qν) | E-1, E-4, E-5, E-6, E-7 |
| B4 atom count | N_at everywhere (E.1, E.3 n_at → N_at); row proposed | E-1 Cost, E-3 Cost; SEAMS E.1-E.3 |
| B4 N_f | → N_fine, defined at first use; row proposed | E-5; SEAMS E.5, E.1-E.3 |
| B4 broadening | bare η → η_b (E.6 eq:E.6-R0 and k-grid paragraph; E.4 finite-frequency Sternheimer); row proposed | E-4, E-6 |
| B5 Si core | X-Ray Data Booklet Table 1-1 (relative to VBM for semiconductors, Sect. 1.1): 2p 99.4/99.8, 2s 150, 1s 1839 eV; Ge 3d 29 eV; 2p opens at 29 MeV, q ≥ 38 keV; 2s 43 MeV, 57 keV; Ge 8.5 MeV, 11 keV; E.2 "hundreds of eV" → "about 100 eV" | E-2 opening, Construction; E-7 Core states, we:E-siff close; bib williams2009electron |
| B6 tab:E-gw | Si core-polarization entries 1.29/1.16 (Γ→0.85X) from Table II; Ge measured Γ 0.89 in caption; GaAs LDA cell removed (see N below) | E-3 table |
| B7 spelling | aluminum, tunneling, labeled | E-7, E-8, E-9, E-10, E-11 |
| B7 rates | \varGamma for Γ_w, TST Γ, Γ_0, Γ_iso, Γ_anh, Γ_L, Γ_ii, Γ_ph, Γ_tot, Γ_max; zone-center Γ upright | E-5, E-11, E-12, E-13 |
| N order | E.6 before E.7 kept; E.7 close "…; \cref{app:E.6} treated them"; E.8 close rewritten | E-7, E-8 |
| N duplicates | PAW reconstruction derived only in E.2; E.7 points to eq:E.2-PAW/rhoPAW/onecentre in E.2 symbols (φ, p̃), keeps eq:E.7-radial; eq:E.7-paw, E.7-pawO removed. Displacement-threshold protocol only in E.11; E.10 keeps definition, range and pointer | E-7, E-10 |
| N E.9 factor 2 | ω = |S|[J(Q)−J(0)]; frozen magnon ω = 2ΔE/(|S|sin²θ) | E-9 Spin spirals |
| N E.8 ZPR | +9 meV lattice term applied: −47/−48 meV vs −62/−64; e–ph part −71/−73, calculations ≈20 % low | E-8 we:E-zpr |
| N E.13 A_AB | A_AB tuned to ε_eh in the original model, injection data confirm to 5 eV; 1 % agreement now consistent | E-13 single-parameter model |
| N GaAs LDA gap | one value, 0.43 eV (Lucero, tab:E-functionals); tab:E-gw cell "--" with caption pointer | E-3 table |
| N Si 2p | see B5; reference level stated | E-7 |
| N E.3 GW update | paragraph on current practice: 1/N_PW extrapolation and empty-state-free schemes, Si G0W0@LDA 1.10 eV (Klimeš Sect. IV C); contour deformation; vertex corrections QSGŴ, Si 1.08 eV (Cunningham Table 1); Golze review; opener and we:E-si-gap qualified ("older calculations overshoot") | E-3 opening, Self-consistency, WE; bib klimes2014predictive, cunningham2023qsgw, golze2019gw |
| N E.6 ε∞ | 11.7; μ_x 0.10 m_e, a_x ≈ 6 nm, 1/a_x 0.016 Å⁻¹ | E-6 BSE |
| N z_qp | \cite[Sect. II]{kotani2010impact}, pointer to eq:E.3-qp | E-13 |
| N α_ohm | half-difference V_d (configurations at ±V_d), eigenvalues e^{2iδ̃} of S_RS_L†, α = 4K_b kept; NOTATION 16.8 row updated | E-10; NOTATION.md l.468 |
| N Heisenberg convention | E.9 already pairs once, J > 0 AFM (matches NOTATION editor ruling); flagged for 7.1/WE 7.2 in SEAMS | SEAMS E.7-E.10 |
| N Grüneisen | γ^G already in E.8; E.4 words only (now one sentence pointing to E.8) | E-4 |
| N 𝔗 macro | \mathfrak{T} kept (no \Trunc adopted) | — |
| N E.5 enumerate | six-item list → prose paragraph | E-5 recoil calculation |
| N E.11 title | full title "Recoil molecular dynamics" (no optional short title needed) | E-11 |
| N arXiv-only bib | kim2020quickstart → J. Phys. Energy 2, 036001 (Crossref-checked); komsa2009comparison: no journal version of that paper found, kept arXiv-only | book.bib |
| C Δ_SO, m_Γ | Ge Δ_SO 0.296 eV (E.1 Pitfalls, E.3 WE: Δ/3 = 99 meV); GaAs measured Γ mass 0.067 m_e (E.3, \cref{sec:3.3}) | E-1, E-3; SEAMS E.1-E.3 |

## Derivation reports
| item | fix | location |
|---|---|---|
| D1-1 Garza | B3 | E-1 |
| D1-2 PseudoDojo | B3 | E-2 |
| D1-3 Poncé | B2 | E-4 |
| D1-4 / R-N1 E.5 time | 10¹⁶ op: 10³ s ≈ quarter hour at 10¹³/s; 2–3 days at 5×10¹⁰/s | E-5 cost |
| D1-5 rounding | 270.3 bohr³; 1.88 Å; v_max = 2.65×10⁻³ | E-1, E-2 |
| D1-6 / R-N4 DFPT cost | 3N_at⁴R⁹ vs 3N_at⁴R³, factor R⁶ | E-4 force-constant interpolation |
| D1-7 window count, R_p stage | three valence bands (HH, LH, SO) → 3×10⁷ pairs; R_p stage stated (≈7×10⁶ MAC per distinct Q, subdominant to 10⁵ Q) | E-5 cost |
| D1-8 Si CPP | B6 | E-3 |
| D1-9 notation | B4 | — |
| D1 E.1 ε^T | ε^T = 1 − R⁰v_C acts on densities, same eigenvalues; eq:E.1-mixing written with ε^T | E-1 Self-consistency |
| D1 E.6 "At T = 0" | removed | E-6 |
| D1 E.6 η | B4 | E-6 |
| D1 0.32 m_e | stated as per-valley DOS mass (0.92·0.19²)^{1/3} | E-5 we:E-counts |
| D1 SEAMS 0.37/1.4 | corrected | SEAMS E.1-E.3 |
| D2-1 / R-N2 | N E.9 | E-9 |
| D2-2 / R-N3 | 0.60/1.53 | E-9 we:E-al |
| D2-3 α_ohm | N α_ohm | E-10 |
| D2-4 ⟨c³⟩ | B_iso = 4π³gΩ_at⟨c⁻³⟩, ⟨c⁻³⟩ = (1/3)Σc_s⁻³ = 1/(2.13×10¹¹) s³m⁻³, arithmetic rewritten | E-12 eq:E.12-iso |
| D2-5 lowest band | "lowest band left out" | E-7 convergence |
| D2-6 / R-N5 bins | q_0 → 0.02 αm_e = 75 eV; ≈500×400 to 30 keV (published 500×900 to 67 keV) | E-7 we:E-siff |
| D2-7 E.7 KS gap | "about 0.6 eV in the representative PBE calculation (we:E-si-bands)", Poncé cite dropped | E-7 we:E-siff |
| D2-8 NiO range | "DFT-based values 11–27 meV (UHF 4.6 meV)"; opener qualified | E-9 opening, mapping |
| D2-9 core depths | B5 | E-7 |
| D2-10 A_AB dimension | "A_AB = 5.2 in the units of the source (quoted eV², leaving eV⁻¹)", energies in eV; fits "in the same units" | E-13 |
| D2-11 z_qp | N | E-13 |
| D2-12 conventions | J^ex convention exists in NOTATION; Γ (B7); LKAG conversion J^ex = −2J_ij/|S|² stated | E-9 Green's functions |
| D2 E.7 Zacharias factor | half sentence: their inverse factor multiplies the oscillator-strength form | E-7 scissor |
| D2 E.7 45 vs 50 keV | 45 keV in both places | E-7 core states |
| D2 E.8 occupations | "of order e^{−ω/T}" | E-8 WE |
| D2 E.10 10 vs 20 ps | protocol only in E.11 (20 ps) | E-10 |
| D2 E.11 4×10⁷ | 5×10⁷ core-h (two places) | E-11 |
| D2 E.11 Bartók "Sect. V" | location kept; not re-checked (source section numbering not in the extract) | — |
| D2 citation audit | N arXiv-only bib | book.bib |

## Prose report
| item | fix | location |
|---|---|---|
| S1 Pitfalls | cut to items stated nowhere earlier: E.1 (Ge band order, Ge ε failure, smearing hides a metal, seam close to E.2/E.3); E.2 (frozen-core polarization); E.3 removed (closing sentence kept); E.4 removed (closing pointer kept); E.5 (grid/resolution warning); E.6 (head-element/G_q, broadening); E.7 (Umklapp, cut window, normalizations, Ge order); E.8 moved after WE, two artifacts + edge pointer; E.11 (validation, two omissions); E.12 (conversion, Debye start, transferred fits); E.13 (gap T, two double countings split, interpretive). Cross-cutting lessons in the Summary | all |
| S2/S3 outline openers | replaced by one sentence of what is computed or trusted, varied wording | E-1, E-2, E-4, E-5, E-6, E-7, E-8, E-9, E-10, E-11, E-12 |
| S4 hierarchy heading | "Place on the hierarchy" in all sections except E.2 (no hierarchy paragraph) | E-1, E-3 … E-13 |
| S5 clause titles | "Computed quantities", "The frozen core", "Outputs of a linear-response run", "The density vertex" | E-1, E-2, E-3, E-4, E-5, E-6, E-7, E-11, E-12, E-13 |
| S6 register | "gives" in E.9 cut from 10 to 5; "must" reduced where sentences were rewritten; remaining counts not swept mechanically (declined as a global rewrite: the sentences carry content and the brief limits changes to listed items) | E-9 and rewritten passages |
| S7 Γ | B7 | — |
| S8 units | ħΓ → Γ "in natural units" (E.13); "with ħ restored" dropped (E.4); k_B dropped (E.11, T in energy units) | E-4, E-11, E-13 |
| S9 spelling | B7; label eq:E.2-onecentre kept (referenced; rename optional) | — |
| S10 style | \cite\cite → comma; f-sum → $f$-sum; booktabs in E.11–E.13; labels tab:E-md-si, tab:E-phrates, tab:E-transport-si, tab:E-cascade-si; "abstract" cites → section numbers (E.8, E.10) | E-3, E-5, E-6, E-7, E-8, E-10 … E-13 |
| S11 imperatives | E.4 Fix/Replace/Take, E.5 compute/compare, Take; E.7 Fold/form; E.12 Take; E.2 recipe | E-2, E-4, E-5, E-7, E-12 |
| E.1 items | assurance cut; outline; appositives; percent form (\SI…\percent); "In this book"; verbatim block → sentence; insulator sentence cut; seam to E.2 | E-1 |
| E.2 items | opener; "noticeably" cut; "rest of this section" cut; recipe; "considerably" → differential vs integrated statement | E-2 |
| E.2 vague factor (Griffin Fig. 5) | declined: the factor cannot be read from the text extract; the source's own words ("much higher", "significantly enhanced") are paraphrased | — |
| E.3 items | opener with new number, recaps merged; parentheses; restating sentence deleted; recipe sequencing; WE ordinals | E-3 |
| E.4 items | opener; "One perturbation is labeled…"; outputs; checks sentence; "direction follows"; "catch is the zone center"; split space; strains; duplicate lattice-constant sentence merged; 10 %/11 % | E-4 |
| E.5 items | opener; mandatory test; setup; enumerate; ordinals | E-5 |
| E.6 items | opener; N defined; named parameters; false contrast; count teasers named; ε∞ 11.7; $GW$ | E-6 |
| E.7 items | title; opener; fold/form; KB symbols → E.2's p̃, D; R1–R3 consolidation; 50 → 45 keV; close | E-7 |
| E.8 items | opener; "method of choice"; Pitfalls moved; detector tic; close | E-8 |
| E.9 items | opener; Jacobsson #20 → two-sublattice LSWT stated (eq:E.9-afm); LKAG conversion; tic | E-9 |
| E.10 items | opener; passive recipe; R9 cut; Holmström #20 removed with the duplicate | E-10 |
| E.11 items | title; rhetorical question; in-text table folded into tab:E-md-si (all six energies); splice rule; caption bookkeeping cut; miscount | E-11 |
| E.11 "far more … than intuition" | rewritten without the comparison; census numbers not given (none in sources) | E-11 |
| E.12 items | #20 Leman Eq. 9 (L→L′+T′ distribution and angle stated) and G4CMP Eq. 9 (P(θ) stated); "For a carrier"; checks named | E-12 |
| E.13 items | three ingredients; Ω 40.05; z_qp; Im χ → Im W^scr; 0.75 wording; double-counting split; closing contrast | E-13 |
| Redundancy R1–R10 | R1, R3, R9 as above; R2 E.2 one clause + eq:E.7-vNL (E.4 already one clause); R4 E.2 and E.7 cross-referenced, E.5 one clause; R5 E.7 one clause; R6 E.3 one clause + we:E-zpr, E.8 keeps; R7 E.1 shortened; R8 E.4 one sentence; R10 Summary | — |
| Seams | E.1→E.2, E.6→E.7, E.8 close fixed | — |

## Reader report (b)/(c)
| item | fix | location |
|---|---|---|
| 𝔗 friction | appendix opening states the components; each n_T use glossed | appE.tex; sections |
| N6, N7, N1–N5 | as above | — |
| N8 FFT counts | E.1: indices −17…17 → 35 points, 36³; E.7: cube estimate labeled, fcc factor √2, 22 N_pw ≈ 36³ at 60 Ry; we:E-siff N_FFT 6×10⁴, 1×10¹⁵ flop, ≈3 h | E-1, E-7 |
| E.1 two measured a | WE states 5.431 room-T vs 5.416 table value | E-1 WE |
| E.1 Ewald/grid sentence | rewritten with superlattice vectors R | E-1 BZ sampling |
| E.1 derivative discontinuity | one sentence | E-1 |
| E.1 cutoff error estimate | softened with the Ge 1.3 vs 3.1 meV numbers | E-1 |
| E.2 κ sum | atoms of one cell, cell normalization stated | E-2 |
| E.2 f-sum test "which n" | declined: band and k-point choice of the representative run not recorded beyond "states at k = 0" | — |
| E.2 Gaunt | glossed | E-2 |
| E.3 COHSEX, head and wings | glossed | E-3 |
| E.3 Ge measured Γ | 0.89 eV in caption | E-3 |
| E.3 ZPR source | van Schilfgaarde ZPR sentence replaced by pointer to we:E-zpr (≈60 meV) | E-3 |
| E.3 scissor ε∞ "closer" | "not guaranteed to be closer" | E-3 |
| E.4 δ_off | defined | E-4 |
| E.4 frequency noise | rewritten (linear error in force constants; small or imaginary frequencies) | E-4 |
| E.4 forces vanish by symmetry | stress, not forces, sets the reason | E-4 |
| E.5 Ω_W gloss | declined: defined in Sect. 3.6 (pointer present) | — |
| E.6 α material dependence | "a fit for silicon rather than a universal constant"; newer kernels (bootstrap, JGM) declined: no fetched source | E-6 |
| E.7/E.2 Griffin 15 vs 10 eV | reconciled: differential rate above 15 eV, integrated rate above thresholds ≈10 eV; E.7 points to E.2 | E-2, E-7 |
| E.7 f-sum cross-reference | E.2 and E.7 refer to each other | E-2, E-7 |
| E.10 Makov–Payne overcorrection | sentence with Komsa Sect. III B; WE says production uses Gaussian-charge schemes | E-10 |
| E.11 ACE/MACE cost | declined: no source fetched for the speed-up | — |
| E.12 Luke TA emission | clause added (longitudinal only in eq:E.12-luke) | E-12 |
| E.13 0.75 ambiguity, double counting | as P | E-13 |

## Notation changes not requested by the reports
| item | fix | location |
|---|---|---|
| E.12 E_ph (reserved by NOTATION for the Luke-amplified energy of 1.5) | → E_ath (NOTATION 20.2) | E-12, SEAMS E.12 |
| E.12 V_b (renamed in clash 71) | → V_bias | E-12, SEAMS E.12 |
| E.6 N_b | → N_{\mathrm{b}} as in E.1 | E-6 |
