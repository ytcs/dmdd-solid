# Chapter 10 revision (2026-11-02)

Files: tex/ch10/ch10.tex, s10-1 … s10-10 (Summary at the end of s10-10), tex/appD/D-29.tex, D-30.tex; tex/ch08/s8-4.tex (Table 8.3 and the
l.54 sentence that restates its last row, only). Outside these: NOTATION.md (one row, 𝒢_rel), tex/bib/book.bib (three entries:
fermi1940ionization and allison1980relativistic, checked against Crossref; bahcall2001solar, arXiv astro-ph/0010346 checked against the
arXiv API: ApJ 555, 990, doi 10.1086/321493), ledgers/SEAMS/10.1–10.10 (a "Revision after the Chapter 10 review" block each; 10.2's
𝒢_GS → 𝒢_rel). Sources fetched: sources/review-ch10rev/ (2507.14345 text, astro-ph/0010346 text; PDFs deleted).
Compute: no QE, no new scripts. we10_2.py rerun (RPA+LF 16.75 at 1 MeV → 16.7, as the 10.3 table). |ε(3 eV)|² recomputed with
abs10_7.eps_si (Franta 300 K): 761.3. Other numbers from the existing logs (nuis10_10.log, inel10_9.log, limit10_*.log).
Format: item → fix → location. "Declined" gives the reason. User rules received mid-task (patterns 0, 21–23) are applied throughout.

## Editor rulings (brief)
| # | Item | Fix | Location |
|---|---|---|---|
| 1 | Table 8.3 last row | split in three: j_T "only through local fields (G ≠ 0) on symmetry axes; at G = 0 only through L–T mixing" (O5, O8); spin current 𝒥 "none without SOC or magnetic order, as the spin density" (O3, O7, O12–O15; ALP absorption); 𝒯_e "head and local fields; head term O(q²) at small q in crystals without a polar axis" (O2 v⊥² part; scalar absorption); l.54 prose split to match | s8-4 tab:8-screening, l.54 |
| 2 | ALP dark Compton | "Their differential rate [Eq. (16)], integrated over the photon angle at v → 0, gives eq:10.8-alpC exactly. The factor appears only in their integrated rate [Eqs. (3) and (17)], so the error enters in the step from the differential to the integrated form." | s10-8 |
| 2 | fermionic absorption | free vertex underestimates by at least 1/r (r = 0.59 → ×1.7, Xe 1s at 56.5 keV); transverse term a sum of squares, can only add; only (Zα)² ≈ 0.13 of unknown sign. ("at least r" in the brief written as 1/r, since r = free/continuity in eq:10.9-ratio.) | s10-9 fermionic ¶, lim:10.9c closing, sec:10.9-open, sec:10.10-open |
| 2 | Cherenkov term | "contains the Cherenkov term of Fermi's formula, standard for fast charged particles in matter and in the PAI model of energy loss in silicon [fermi1940, allison1980]; what is new here is only its size in a boosted-DM rate in silicon with a massless mediator"; "holds a surprise" removed; Fermi cited at eq:10.9-fermi | s10-9 |
| 2 | W̄5, Im W̄2 | 10.4: both vanish exactly in Si/Ge under PT (D.30); "the small nonzero W̄5 and Im W̄2 of the published calculation, which its authors attribute to departures from axial symmetry, are therefore numerical". D.30: Im W̄2 = 0 added | s10-4 ¶ after tab; D-30 |
| 3 | 2.5×10⁻³ | text 2.4 → 2.5×10⁻³ (caption keeps 2.4×10⁻³, its own criterion (√r+1)² ≤ 1.1) | s10-4 |
| 3 | Fermi factor | 2.6 → 2.3 at 10 E_x^b (WE's 2.6 at 1.27 eV kept) | s10-5 |
| 3 | 16.2 | (5.03 − 1)² = 16.2 | WE 10-band |
| 3 | 0.525 q₀ | "The kinematic edge at that energy lies at 0.525 q₀ …; just above it, at q = 0.55 q₀, …" | s10-1 after box |
| 3 | 7.09 keV | "flat between about 1.7 q₀ and 1.9 q₀ (6.5 to 7.09 keV)" (raw argmax 1.74 q₀, flat integrand) | WE 10-rate |
| 3 | |ε(3 eV)|² | recomputed 761.3 → 761 in 10.4 (now \cref{sec:10.7-darkphoton}), 10.7, Summary. **Open:** s8-4 l.149 still says 770 (rounded ε₂/L); outside the permitted s8-4 edit — editor to change to 761 | s10-4, s10-7, s10-10 |
| 3 | NaI vs GaAs | "lowest optical exciton about 0.3 eV below the gap (absorption peak 5.6 eV against gap 5.9 eV [taufertshofer]), some seventy times deeper than the 4.2 meV of GaAs (4.9)" | s10-5 |
| 3 | 10.2 gap | 1.11 → 1.17 eV, seventeen → eighteen; WE threshold now "1.11 eV, the gap of the tables" (ω_th); caption "the scissor gap of the tables" | s10-2 |
| 3 | 77 K gap | "1.165 eV against 1.169 eV at millikelvin temperatures, from the measured temperature dependence [alex1996temperature] (6.3)" (fit of 6.3: 1.1692 − 4.9e-4·77²/732) | s10-7 edge |
| 3 | solar core | "1.57×10⁷ K at the center [bahcall2001solar, Table 5]" | s10-9 boosted |
| 3 | Baryakhtar | Eqs. (2.1), (2.2); σ^{μν}F_{μν} → −2σ·B gives μ_M ≃ 2/Λ_d, rate 4Δ³/πΛ_d² (same scaling) | s10-9 decay text and lim:10.9d |
| 3 | lim:10.9a | cites Eqs. (10), (11), (15), (16), (20) "with the factor q⁻² of [essig2016direct, Eq. (3.13)] restored and the absolute value written out"; text after eq:10.9-inel says the same; "absolute value included" → "taken in absolute value" | s10-9 |
| 3 | WE 10-exo | "half-maximum edges between about 4 and 8.5 eV (up to 11.8 eV at 3 MeV)"; 41 → 40 % (inel10_9.log 0.40) | s10-9 |
| 4 | 10.2 pointer | IP 1.36×10⁵ "from the independent-particle head of these tables and not from the form-factor table of 10.1, which gives 1.60×10⁵ (10.10-rungs traces the difference)"; Fig. 10.2 caption "from a different tabulation"; Summary "(two tabulations differ by 18 %, 10.10-rungs)" | s10-2, s10-10 |
| 4 | 10.1 f-sum | scissor "accounts for about ten percent; the rest of the excess has no identified cause (10.10-rungs)"; Summary sentence added | s10-1, Summary |
| 4 | 10.10 spread | justified as a bound: the discrepancy sits at small q, where screening is strongest; with ε₂ and ε₁ − 1 too large by 1 + δ and ε₁ ≫ 1, L ≃ ε₂/ε₁² moves by ≈ 1/(1 + δ), opposite and no larger; the IP ratio is an upper bound on the screened spread and is carried as such (table row, WE label "(bound)") | s10-10 rungs, table, WE 10-band3 |
| 5 | 𝒢_GS | → 𝒢_rel in 10.2 (eq:10.2-relaxed, text), NOTATION row added, SEAMS 10.2. **Pass 2 (App. E):** tex/appE/E-16.tex l.46, 47, 50, 52 and tex/appF/F-rows.tex l.76 still print \mathrm{GS} | s10-2, NOTATION |
| 5 | χ for responses | χ⁰(0), χ(0), χ^TD → R⁰(0), R(0), R^TD(0) | s10-5 |
| 5 | clashes | bare Λ → Λ_NP (10.8), E_cut (10.7 box caption; its ⟨f|T|0⟩ → ⟨f|p²/2m_e|0⟩, T being the temperature); K̄, K → K̄_pair, K_pair (10.8 text, box caption); bare ξ removed (10.8 Bauer normalization compressed); script 𝒯^{(2)}, 𝒯^C → T^{(2)}, T^C (T-matrix family); n_g → n_grp (10.9; NOTATION C.16 row); \varOmega pole → E_cp (10.5); 𝒢_a (pair coefficient) → g^{φφ}_a (clashed with 𝒢_rel/𝒢_VH) | s10-5, 7, 8, 9 |
| 5 | SEAMS rows | appended to SEAMS 10.1–10.10 (~35 symbols: Ω_{P,e}, K_n, η_n^max, ω_p^val first use, Z_L, ω_pl, q_c, v_th, B⁺_pl, ε₂⁺, r, r_med, δ^j_LF, j_T, 𝒥_T, E_cp, R^TD, w_λ, C, N^acc, S^at, δ_mv, δ_oo, H_oo, T_ij, E_ee, q_3d, E_cut, ε″, 𝐉_a, T^{(2)}, T^C, K_pair, p_K, Λ_NP, G_S…G_A, g^{φφ}_a, g_eff, ω_γ, ω_C, σ_Th, H_sg, Γ_pair, k_*, ω_line, q_line, D_eff, Λ_d) | ledgers/SEAMS |
| 6 | opening | middle four sentences → "The band structure alone gives the crystal form factor on which most published limits rest. The answer, however, turns on what the band structure leaves out: …" | ch10.tex |
| 6 | titles (and user rule 21: every title) | 10.1 "The crystal form factor"; 10.4 "Spin and current couplings"; 10.9 "Inelastic and relativistic dark matter"; 10.10 "Nuisance parameters of the electronic rate"; subsections: "The independent-particle structure factor", "Convergence parameters and omitted physics", "Rung ratios of the silicon rate", "Sum-rule bounds on the rate", "Static step of a relaxing lattice" (numbered, sec:10.2-lattice), "The Lindhard loss-function rate", "Plasmon pole and residue", "Plasmon threshold speed", "Plasmon decay into pairs and phonons", "Screening of non-density rows", "Interference bound on a mixed block", "Elliott onset and bound exciton lines", "Triplet excitons", Open problems numbered (sec:10.5-open), "Core shells within kinematic reach", "Separation of core and valence responses", "Relativistic shifts of the $f$-sum rule", "Dark-photon absorption and in-medium mixing", "Optical data near the silicon edge", "Axion-like-particle absorption", "Scalar absorption and the kinetic-energy row", "Second-order transition operator", "In-medium decay of an excited state", "Many-body rung spread", "Gap and threshold nuisances", "Nuisance table of the electronic sector"; D.30 "Response functions W̄1–W̄5", "Interference band on a mixed block"; WE titles "Dark-photon absorption at 10 eV", "Exothermic lines in silicon", "The germanium $3d$ onset in $q$" | all |
| 6 | truncation-label ¶s | 10.1 (chain ¶ → one pointer to D.29), 10.2 (𝒦 bookkeeping folded), 10.3 (calibration rewrite), 10.9 ×4 (l.79, 142, 195, 228 folded into physics sentences) | s10-1, 2, 3, 9 |
| 6 | count-teasers | 10.1 "Three properties"/"Three parameters…A fourth", 10.2 "three things"/"a fourth number", 10.6 "Two approximations"/"four places", 10.10 "Four calculations"/"Three open items": members named | s10-1, 2, 6, 10 |
| 6 | project-plan wording | "acceptance test" ×3, "core-hours", "Until that library exists", "response library" ×2, "library of E.16" removed | s10-4, 6, 8, 10, D-30 |
| 6 | 10.8 cuts | real-field pair ¶ cut; detector-geometry sentence cut | s10-8 |
| 6 | "momentum transfer" | 10.1 l.74, 76; 10.6 l.14, 54 | s10-1, s10-6 |
| 6 | polar group, pyroelectric | "a polar group, one that leaves some direction fixed under every operation. Crystals with a polar group are pyroelectric: they carry a spontaneous electric polarization along that direction." | s10-7 scalar |
| 6 | normalization triple | 10.1 conversions ¶ → one sentence listing them and a pointer to D.29; chain ¶ after the box cut; D.29 keeps the conversions | s10-1 |
| 6 | connectives | "however" 6 → 9 occurrences, "we can" 1 → 3, "typical(ly)" 0 → 3, "of order" 35 → 28 where not an expansion order (calibration rewrites of prose.md for 10.2 l.81, 10.3 l.38, 10.4 l.3 used) | s10-1…10 |

## User rules received during the task
| Rule | Fix |
|---|---|
| titles name content (pattern 21) | every section/subsection title reviewed (list above); lint TITLE/TITLE-GESTURE: 0 hits |
| no provenance/self-narration (pattern 22) | "This section derives/answers/gives" openers → content statements (10.2, 10.3, 10.6, 10.10); "their Eq. (14) in the book's normalization" → "which is [Eq. (14)] in the book's normalization"; Dror "That paper's general Eq. (7)…its Eq. (8)" → \cite forms; Bauer normalization paragraph compressed; no "without derivation" sentences found |
| underbraces (pattern 23) | eq:10.1-rate (halo, coupling, target, kinematics, with one sentence naming each); eq:10.4-O8 (electron at rest, electron motion) |
| deletion test (pattern 0) | low-content sentences cut: 10.2 closing restatement, 10.6 561.3 eV aside, 10.9 closing four-case recap, 10.4 duplicated triplet ¶, 10.3 repeated third-body sentence; lint with the new BANNED-TERMS: 0 blocking |

## Review items
| Report | Item | Fix / decline | Location |
|---|---|---|---|
| deriv-1 A1, deriv-2 P6, reader-b | Table 8.3 | ruling 1 | s8-4 |
| deriv-1 A2 | D.30 W̄1 citation | "[Eq. (D2)]" (checked in sources/review-ch10/2105.02233.txt) | D-30 |
| deriv-1 C | 4.9 eV shares; empty bins; "quarter of its value at q₀" | "at most 4.9 eV"; "window means… bins counted as zero"; done | s10-1 |
| deriv-1 D | 16.8 vs 16.7; f-sum bound q ≤ 22.5 keV | 16.7 both; "evaluated, like the rate, for q ≤ 22.5 keV, valid because the bound holds at each q" | s10-2 WE |
| deriv-1 E | Z_L form; Maxwell tails | "with Z_L expanded to 1 − (3/5)q²v_F²/ω_p² as in the limit box"; "about 10⁻⁴⁹ / 10⁻⁵³" | s10-3 |
| deriv-1 G | "grows by 2.2 from the onset" | "The weight below 3 eV grows by 2.2" | s10-5 |
| deriv-1 H3, H4 | Ω pole; Ω_{P,e}; ω_p^val | E_cp; Ω_{P,e} row in SEAMS 10.2; ω_p^val in 10.2 WE, 10.5, 10.6 (Ge), 10.9 caption and box sentence; the gas ω_p of 10.3 stays (stated as the gas at the valence density) | s10-2, 5, 6, 9 |
| deriv-1 H6 | \varGamma as Euler gamma (10.5 l.64) | **Flagged, not changed**: STYLE assigns no glyph to the gamma function (\varGamma = rates, upright Γ = zone centre); editor to rule | SEAMS 10.5 |
| deriv-2 | Bauer g_DM | "written per degree of freedom" | s10-8 |
| deriv-2, reader-a | "particle by particle" | "The pair rate per unit volume equals the rate of a scalar of mass 2m_φ at the number density ρ_χ/2m_φ when" | s10-8 |
| reader-a | 10.1 daily modulation 11.7 vs 1.2 | 10.2 → \cref{sec:11.7} (SPINE home) | s10-2 |
| reader-a, reader-b | 10.3 closest approach | "for the exact zero of the Lindhard function (the quadratic dispersion gives 14.5 eV at 1.72 keV)" | WE 10-plasmon |
| reader-a | D.29 cancellation | both facts stated (reverse transitions; S⁰(q) = S⁰(−q)) | D-29 |
| reader-a, reader-b | "coupling carried by a unit volume" | rewritten as the coefficient of iq·U in the density row, c₁^(e)𝓃_e, cancelling for the charge | s10-2 |
| reader-b (b) | Ge–Sheng–Xing terse | "free-electron squared amplitude, evaluated at the kinematics of a bound electron" | s10-6 |
| reader-b (c) | H_int of derivative couplings | "To first order in the couplings the interaction Hamiltonian is minus the interaction Lagrangian, derivative terms included." | s10-8 |
| reader-b (c) | 1.11 "room-temperature value" vs 1.12 | "close to the room-temperature gap of 1.12 eV (10.7-edge)" | s10-1 |
| prose B | redundant IP=−2Im R⁰ in 10.2 | one-line pointer | s10-2 |
| prose B | 10.4→10.5 and 10.6→10.7 seams | clause in 10.5 opener; closing sentences of 10.6 | s10-5, s10-6 |
| prose D | 10.4 table vs text on j_T | one phrase: "unscreened at the head …, local fields only (about 10 %)" in table and text | s10-4 |
| prose D | 10.4 330-word ¶; 10.5 open problems | split in three; split at "So is the response" | s10-4, s10-5 |
| prose D | 10.5 comma, \cites, caption dash-dotted | fixed | s10-5 |
| prose D | 10.6 𝓜¹_ee; 561.3 aside | "first moment 𝓜¹_ee of eq:4.3-fsum"; aside deleted | s10-6 |
| prose D | 10.7 caption tautology; s state; box in source notation | fixed; box now Γ = −(g²/m_φm_e²) Im R_𝒯𝒯 in book symbols | s10-7 |
| prose D | 10.8 "factor between 2 and 1" | "falls from 2 at small mass to 1 well above m_e" | lim:10.8b |
| prose D | 10.9 Dror hard-coded Eqs. | \cite[Eq.~(7)], \cite[Eq.~(8)] | s10-9 |
| prose D | 10.10 "Home" | "Section" | tab:10-nuisances |
| prose D | 10.2 l.110 c₁^(e) undefined | covered by the rewrite (coefficient of the density row, 8.4) | s10-2 |
| PARTII | lim: labels | added lim:10.1a, 10.2a, 10.2b, 10.3a, 10.3b, 10.4a, 10.5a, 10.7a, 10.7b | boxes |
| prose D | `lim:` label not in STYLE | **Declined**: PARTII.md prescribes `lim:N.Mx` labels | — |
| prose E | one EPM anchor (we:8-rung + Cohen–Bergstresser there) | **Declined in part**: citing Cohen–Bergstresser at we:8-rung needs a ch08 edit outside the permitted scope; captions keep \cite{cohen1966band} because captions stand alone | — |
| reader-b (b) | O₁…O₁₅ cited by number only | **Declined**: tab:8-operators is cited with the table; restating 15 operators would repeat 8.1 | — |
| reader-b (b) | fermion trace sign convention before the trace | **Declined**: the next sentence gives the reason for dropping the term; moving it changes nothing | — |
| reader-a | relaxing-lattice step too fast; published-treatments ¶ dense | the latter split; the former keeps its pointers to Ch. 5 and 8.4 (no new material) | s10-2, s10-4 |
| deriv-1 F | limit10_4a.log prints 2.38e-3 for both criteria | **Not changed**: log print bug only; text and caption now carry the right numbers; script not rerun | — |
| deriv-2 GAPs | script-only numbers (Ge crystal valence, EPM scalar, 1.6e-12) | no text change (verification gaps, not errors) | — |

## Not touched
- Every derivation marked CHECKED; figures (no figure depends on a renamed symbol in its PDF, apart from axis labels without the renamed symbols).
- s8-4 beyond Table 8.3 and l.54; E-16, F-rows (pass 2); s8-4 l.149 (770 → 761 for the editor).

## Build and lint
/tmp/build-ch10rev, full main.tex with latexmk -f (biber): 0 LaTeX errors, 0 undefined citations, 0 multiply defined labels, 1014 pages.
Undefined references from the edited files, all to unwritten targets: app:D.36, chap:12, chap:18, sec:13.1, 13.3, 13.4, 13.5, 13.9,
14.3, 16.2, 16.4, 17.3, 18.1, 21.4, 22.3 (the book-wide list also has app:B.2, app:D.47, sec:9.2, 9.4 and chap/sec 12–22 from other files).
Lint (lint.py --banned BANNED-TERMS.txt, current list) on the 14 edited tex files: 66 hits, 0 blocking; all are LONG-SENT merges of
captions, tables and displays and EQ-PUNCT false positives inside aligned/gathered; TITLE and TITLE-GESTURE: 0.
