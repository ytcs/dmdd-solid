# Chapter 1 revision log

One row per review item: report (D = derivation, P = prose, A = reader-a, B = reader-b persona b, C = reader-b persona c), item, fix, location.
Locations are section / paragraph (line numbers moved). Editor rulings are cited as R1–R11.
Build: latexmk clean, 0 LaTeX errors, 0 undefined citations; undefined references only to unwritten targets (app:A.*, B.2, C.8, E.*,
sec:2.x–7.x, chap:8/10/18/20/21). Lint: 0 real hits; the 4 remaining LONG-SENT hits are the known table artifacts (detex merges
tab:1-shm, tab:1-kinematics, tab:1-interactions, tab:1-quanta captions with their cells).
Word counts (detex, before → after): s1-1 1314 → ~1500 (definitions and clauses requested by A/B/C/D); s1-2 4067 → ~4330 (+6%);
s1-3 4145 → ~4380 (+6%); s1-4 2703 → ~2800 (+4%); s1-5 3831 → ~4030 (+5%); C-9, D-1 ±1%.
Figures rerun: fig1_5.py (|G_111| line, CODATA a) and fig1_9.py (minima 9.69 / 1.98 MeV, ratios 46.1 / 1.42 printed by the script).

## Editor rulings
| R | fix | location |
|---|---|---|
| R1 v_min | D.1 signed sentence replaced by "By Eq. (1.3-vmin), v_min ≥ 0, so η is never needed at a negative argument"; absolute value kept in 1.3; NOTATION v_min row change proposed | D-1 branch list; SEAMS/1.3 |
| R2 Al gap | Bulk T_c = 1.2 K [Yeh 2023], Δ_BCS ≈ 1.76 k_BT_c [Snowmass Sect. 3.3] → 2Δ ≈ 0.36 meV, m_min ≈ 0.10 keV; 0.6 meV labelled film value, attributed to Hochberg 2016 / Mitridate Table II (m_min 0.17 keV); table and summary updated | 1.5 Quasiparticles ¶, tab:1-quanta, Summary; bib yeh2023doubling |
| R3 Si constants | E_g(0) = 1.1692 eV [Ramanathan Eq. (11)]; 1.12 eV at 300 K [Ramanathan Table I, fetched]; 1.11 eV stated as the literature value [Essig Eq. (5.2)] used for every Ch. 1 threshold mass (no temperature claim); m_min = 0.333 MeV at 1.1692; a = 5.431 Å [CODATA 2022, bib mohr2025codata, NIST value fetched]; "1.2 eV" removed (photon ¶ now "1.17 eV at low temperature"); 1.11 contexts (step model, fig 1.5/1.9 captions, summary) point to we:1-mmin as "literature gap" | 1.3 WE we:1-mmin, scales ¶, fig:1-kinematics; 1.5 Charge, Photons ¶, fig:1-exclusion; Summary |
| R4 folding scale | |G_111| = √3·2π/a = 3.95 keV ≈ 1.06 q₀ is the interatomic scale; 2π/a = 2.28 keV = 0.61 q₀ kept as cubic-cell unit; "above 0.4 MeV" → 0.75 MeV; 23 eV "below a hundredth of |G_111|"; fig1_5.py redrawn with |G_111| | 1.3 scales ¶, folding ¶, phonon ¶; fig:1-kinematics |
| R5 terms before 3.1 | Working definitions of reciprocal-lattice vector, crystal momentum, first Brillouin zone, folding at first appearance, pointing to Sect. 3.1 | 1.3 first ¶ |
| R6 coordinates | Equatorial axes, declination, right ascension, sidereal day, meridian, local sidereal time, hour angle defined; 3×3 equatorial→galactic matrix printed (eq:1.2-rotation), verified: third column (−0.4838, 0.7470, 0.4560), Galactic center RA 266.40°, Dec −28.94°, transpose on v̂_⊙ → (0.4657, −0.4887, 0.7378), RA 20.91 h | 1.2 Daily modulation |
| R7 QFT notation | Absorption couplings stated as cited results with equation numbers (Mitridate Eq. (3), (18); Graham Eqs. (2),(3); Hochberg 2017 Eq. (7)); explicit pointer to App. C.9 and Chap. 2 (and Chap. 8); no derivation; NR currents said in words | 1.4 opening ¶, Absorption |
| R8 exclusion figure | Caption names the Gaussian cutoff exp[−q²/2(2q₀)²]; script comment names it and prints the minima; rerun gives 9.69 MeV / 46.1 (heavy), 1.98 MeV / 1.42 (light); text 9.7, 46, 2.0, "within 1.4" | fig:1-exclusion, 1.5 "two curves" ¶, fig1_9.py |
| R9 citations | Essig 2016 in (x.y) scheme everywhere: (A.12)–(A.15), (A.14), (B.4)/(B.5) in 1.3 and D.1; Lee–Weinberg 2 GeV → lee1977 only, Lin Eq. (44) for the scaling; Steigman Sect. II C; Kahn–Lin Table I cited only for eV gap and optical phonons; all concatenated \cite\cite → \cites; equation numbers inside cite options | 1.1, 1.3, 1.4, 1.5, D-1 |
| R10 structure | Outline paragraph added, process comment removed (ch01.tex); "thread" removed (1.3 last ¶, 1.5 inputs); Part I/III → words + \crefrange{chap:2}{chap:7}; duplicates removed (see P chapter rows); η display removed from 1.3, D.1 equations cited; curly quotes; g_deg defined; captions made standalone; 1.3→1.4 join rewritten; Summary revised | ch01.tex; all sections |
| R11 numbers | All WRONG numbers applied (rows D below); toy rate integrated over ln ω (×ln(30/1.11) = 3.30): r = 7.39×10⁴¹, N_sig = 74, σ̄_lim = 3.1×10⁻⁴², 3.1×10⁻⁴³ | 1.5 we:1-limit |

## Derivation report (D)
| item | fix | location |
|---|---|---|
| A1 v_min | R1 | D-1; SEAMS/1.3 |
| A2 σ̄_e vs Lin's 10⁻³⁷ | Clause added: Lin quotes ≈10⁻³⁷ for both benchmarks; its Eq. (74) gives 3.0×10⁻³⁹ here | 1.4 we:1-darkphoton |
| A3 Al gap | R2 | 1.5 |
| A3 toy rate per ln E_e | R11 | 1.5 we:1-limit |
| A3 Essig "29 events" | Not quoted (never was) | — |
| A4 Steigman section | III C → II C | 1.1 freeze-out |
| A4 Majorana / Ωh² = 0.11 | Clause added: Dirac doubles; Planck value lowers 2.2 → ≈2.0×10⁻²⁶; estimate "order of magnitude" (omits post-freeze-out annihilation) | 1.1 freeze-out |
| A4 x_fo at 1 GeV, ⟨σv⟩ inserted | Iterated with ⟨σv⟩ = 2.3×10⁻²⁶ (self-consistent), g_deg = 2: 25 at 100 GeV (g_* ≈ 80), 22 at 1 GeV (g_* = 10.75, T_fo ≈ 45 MeV) | 1.1 freeze-out |
| A5 Si numbers, "1.2 eV" | R3 | 1.3, 1.5 |
| B Lin I A/I C prose unverified | No change: not wrong; Lin Sect. I cites retained (reviewer verified section topics) | — |
| B Lee–Weinberg cite | R9 | 1.1 |
| B Kahn–Lin Table I overreach | Narrowed to gap ≈ eV and optical phonons tens of meV; acoustic/superconducting scales pointed to 1.3/1.5 instead | 1.1 window ¶ |
| C |v_⊙| = 250.55 rounding | Magnitude printed as 250.55 km/s; 250.5 km/s stated as the adopted reference value with which all later numbers are computed (relative difference 2×10⁻⁴; no final result changes at its quoted precision); tab:1-shm row and v_E^ref definition reworded; NOTATION rows proposed. Chosen over 250.6 so that scripts, figures and worked-example digits (1.0525, 0.86338, 0.6498) stay consistent | 1.2 after eq:1.2-vsun, v_max ¶, tab:1-shm; SEAMS/1.2 |
| C Baxter Eq. (10) for boosted f | Text now: "the galactic one of Ref. [Eq. (10)] evaluated at the boosted velocity" | 1.2 lab frame |
| D m_min yearly swing | −3.9 % (June) / +3.4 % (December) | 1.3 threshold mass |
| D 26.06 GeV atomic mass | "atomic mass of ²⁸Si" in 1.3 (WE, table caption, figure caption), 1.4, fig1_5.py comment | 1.3, 1.4 |
| D Essig (43)–(46), (45), (67)/(68) vs (66)/(68) | R9: (A.12)–(A.15), (A.14), (B.4)/(B.5) | 1.3 speed integral; D-1 checks |
| D η(0)/η(200) 1.41 | "factor of 1.41" | 1.3 fig:1-eta ¶ |
| D η(760) Dec 0.38 | 0.37 | 1.3 |
| D edge with correction 0.98/0.99 | 0.98 and 1.00 | 1.3 edge |
| D "within 5 % above 740" | "above 745 km/s" | fig:1-eta caption |
| E Graham Eqs. lack g_aee term | g_aee term now cited to Mitridate Eq. (3); Graham kept for the photon coupling | 1.4 ALP ¶ |
| E Mitridate Table I claims unverified | No change; claims stay attributed to Table I (not wrong, unverified) | — |
| E "≲ 5 MeV" | "≈ 5 MeV at m_χ = 1 GeV" | 1.4 nuclei |
| E S(q,ω) 2π/V normalization (Knapen Eq. (4)) | Out of scope (Sect. 4.2 unwritten); convention note for the editor: §4.2 must define S with Knapen's 2π/V so that Eq. (1.5-rate) holds; 1.5 now says "with the normalization of Sect. 4.2" | 1.5 dimension check |
| F Ramanathan "TABLE I" | Table~1 → Table~I (×3) | 1.5, fig:1-chain |
| F "well above 20 eV" | Located in Ramanathan abstract; cite changed to "abstract and Eq. (1)" | 1.5 Charge ¶ |
| F exclusion figure | R8 | 1.5 |
| G D.1 line 50 and cite | R1, R9 | D-1 |
| H NOTATION first-use drift and missing rows | Proposed in SEAMS: Δ_BCS, T_c → 1.5; ρ_T, σ₁ → 1.4; v_min, a, G_111, G → 1.3; g_deg clash (1.1); rotation components (1.2). F_χ, ζ_eff, g_φee, x_fo, g_*, s_0, N_90, M_det, t_exp, ω_yr, ω_sid, θ_E were already in the SEAMS proposed rows | SEAMS/1.1–1.5 |
| I Not verified list | No action possible; recorded | — |

## Prose report (P)
| item | fix | location |
|---|---|---|
| Lint: thread, NOTATION comment | Both removed | s1-1 l.2, 1.3 last ¶, 1.5 inputs ¶ |
| 1.1 g_deg | Defined (internal spin states of χ) | 1.1 freeze-out |
| 1.1 Ω_c first use | Defined in words before use | 1.1 cosmological density |
| 1.1 vs 1.2 density ranges | 1.1 now "a few tenths of a GeV cm⁻³" and points to 1.2, which gives the one range (0.2–0.6) | 1.1 WE |
| 1.1 "These masses point to solids" restating | Paragraph removed; excitation scales folded into the window ¶; section ends on a bridge to 1.2 | 1.1 |
| 1.1 optional freeze-out trim | Declined: readers A and B asked for more here (g_*, iteration, entropy clause), not less | — |
| 1.2 density range | as above | 1.2 |
| 1.2 v₀ arithmetic twice | First mention now points to the derivation below eq:1.2-vsun | 1.2 v₀ ¶ |
| 1.2 252.1 / reference convention ×3 | Reason kept once (v_max ¶); annual ¶ keeps only the η consequences; 1.3 keeps only the edge consequences with \cref | 1.2, 1.3 |
| 1.2 0.47 km/s twice | Second mention points back to the daily-modulation ¶ | 1.2 last-but-one ¶ |
| 1.2 overloaded ¶ (lab frame) | Split after "cut or no cut."; relativistic remark moved next to eq:1.2-galilean | 1.2 lab frame |
| 1.2 310-word daily ¶ | Split at "The simplest anisotropy" and "Polar crystals"; Griffin cited once | 1.2 daily |
| 1.2 v_min undefined at η mention | "with v_min the minimum speed of Eq. (1.3-vmin)" | 1.2 after we:1-nesc |
| 1.2 "signature" tone | Reviewer: no change | — |
| 1.3 thread | "The edge recurs throughout the book" | 1.3 last ¶ |
| 1.3 "a few eV" vs 0.5 eV | "at most 3.5 eV … about a seventh of that at a typical speed (Sect. 1.1)" | 1.3 opener |
| 1.3 vs D.1 Essig cite | R9 | 1.3, D-1 |
| 1.3 η display duplicates D.1 | Display removed; text cites eq:D.1-eta1/eta2; edge derivation cites eq:D.1-eta2 | 1.3 speed integral, edge |
| 1.3 ASCII quotes | `` '' | 1.3 v_min ¶ |
| 1.3 "every reader has met" | Deleted | 1.3 first ¶ |
| 1.3 Brillouin zone before definition | R5 | 1.3 first ¶ |
| 1.3 "as stated in Sect. 1.4" | "the case of the exothermic models of Sect. 1.4" | 1.3 v_min ¶ |
| 1.3 \cite\cite | \cites (R9) | 1.3 |
| 1.3 gap given twice | Second mention is "E_g (we:1-mmin; Sect. 3.3)" | 1.3 energy scales |
| 1.3 0.70 MeV not a row; "exactly" | "interpolating Table"; "exactly" cut | 1.3 |
| 1.3 "each defined here in one sentence" | Deleted | 1.3 energy scales |
| 1.3 table caption "third column" | Columns named; "The ½m v_max² column is …" | tab:1-kinematics |
| 1.3 subsection labels sec:1.3-eta etc. | Declined: no visible effect; needs a STYLE rule by the editor (accept `sec:N.M-short`) or a book-wide rename | — |
| 1.3 long ¶s | Split at "To keep the models of" and at "The recovery above the edge is slow." | 1.3 |
| 1.4 opener echoes 1.1 | Rewritten as the 1.3→1.4 join (kinematics opens transfers, interaction sets how often) | 1.4 opener |
| 1.4 sentences opening with a symbol | Reworded (×4) | 1.4 σ̄_e ¶, in-medium ¶ |
| 1.4 / 1.5 ω_q | ω_{\vect q} | 1.4 inelastic; Summary |
| 1.4 endo/exothermic repeated | Replaced by "(endothermic and exothermic cases, Sect. 1.3)" | 1.4 inelastic |
| 1.4 citation style | \cites; Knapen numbers inside the cite | 1.4 |
| 1.4 270-word nuclei ¶ | Split twice | 1.4 nuclei |
| 1.4 table caption | Names Chaps. 4, 8, 5 | tab:1-interactions |
| 1.4 blank line before keyresult | Removed; sentence runs into the box | 1.4 Yukawa |
| 1.4 "differently from in vacuum" | "the medium modifies the mixing" | 1.4 in-medium |
| 1.5 threads / Part I, III | R10 | 1.5 inputs ¶ |
| 1.5 1.2 eV | R3 | 1.5 Photons |
| 1.5 "In words" | "Well above threshold, therefore," | 1.5 rate |
| 1.5 "(precise in" | "(made precise in" ×2 | 1.5 |
| 1.5 percent style | All \SI{..}{\percent} | 1.5 |
| 1.5 ρ_T / ℛ double definition | 1.4 says "the normalization of the event rate ℛ of Sect. 1.5"; 1.5 cites ρ_T to Eq. (1.4-dp-abs) | 1.4 absorption, 1.5 rate |
| 1.5 "The factors are:" list | Declined: reviewer marks it acceptable inside a worked example | — |
| 1.5 gerund title | "Exclusion plots" | 1.5 |
| 1.5 Summary inside s1-5.tex | Declined: STYLE does not require a separate file; moving it changes chapter structure for no visible effect | — |
| C-9 "exact for every purpose" | "accurate to better than a part in 10⁵" | C-9 static limit |
| C-9 long kinetic-mixing ¶ | Split before "For m_V = 0" | C-9 |
| D-1 inconsistent Essig cite | R9 | D-1 |
| D-1 gather numbering | Both lines labelled (eq:D.1-erf, eq:D.1-gauss); branch (i) cites the erf line | D-1 |
| Chapter outline missing | Added (R10) | ch01.tex |
| Summary (a) η for absorption | "every scattering rate"; η named "mean inverse speed above v_min" | Summary |
| Summary (b) ω_q | fixed | Summary |
| Summary (c) "many decades" | "about 90 decades" | Summary |
| Summary (d) theory uncertainty | Sentence added | Summary |
| Summary (e) next six chapters | \crefrange{chap:2}{chap:7} | Summary |
| Redundancy (4) KE vs solids | Kept in 1.1 only; 1.3 opener refers back | 1.1, 1.3 |
| Redundancy (5) q₀ recall | Reviewer: acceptable; unchanged | — |
| Seam 1.1|1.2 | 1.1 ends on a bridge to 1.2 | 1.1 |
| Seam 1.3|1.4 | R10 | 1.4 opener |

## Reader a (A)
| item | fix | location |
|---|---|---|
| Unresolved ?? refs | Expected: targets unwritten (list in header) | — |
| App. C.9 prints as C.1 | Note only: appendix counter is an editor setting (STYLE "Appendix numbering") | — |
| Rounding slips 0.6498 / 0.38 / 0.009 / 94 % | 0.38 → 0.37 (D); 0.6498 kept: correct at the adopted v_E^ref = 250.5 (reader used 250.55); 0.009 (0.0085) and 94 % (93.5 %) correct at stated precision | 1.3 |
| 1.1 x_fo circular, g_* at 1 GeV | D-A4 row | 1.1 |
| 1.1 n/s constant | Comoving volume defined; adiabatic expansion conserves entropy | 1.1 |
| 1.1 Lee–Weinberg scaling asserted | Half-line argument (mediator propagator like G_F, dimensions) | 1.1 |
| 1.1 Pauli limit, g_deg | Glossed; defined | 1.1 |
| 1.2 RA/Dec/sidereal/meridian; matrix | R6 | 1.2 |
| 1.2 uniaxial, optic axis | Glossed | 1.2 |
| 1.2 Jeans equilibrium | One sentence: velocity variance acts as pressure (Jeans equation, first moment of collisionless Boltzmann) | 1.2 |
| 1.2 annual ¶ repetition | P rows (252.1) | 1.2, 1.3 |
| 1.3 ½μv² ambiguity | "the most energy that can go into an internal excitation of a free target" | 1.3 consequences ¶ |
| 1.3 bound-electron estimates | q set by electron momentum; ω ≈ qv; sign check m_χα(v − α/2) < 0 since α/2 = 3.6×10⁻³ > v | 1.3 bound electrons |
| 1.3 600 km/s at the mass edge | "faster than about 560 km/s, the most favorable speed at 2m_min, which are 7 % of the halo" (computed 7.3 %) | 1.3 edge |
| 1.3 table caption, 0.70 MeV | P rows | 1.3 |
| 1.3 fig caption acoustic line | "for the lightest mass" in text; caption no longer claims it | 1.3 |
| 1.3 terms before 3.1 | R5 | 1.3 |
| 1.4 QFT language | R7; currents in words | 1.4 |
| 1.4 1/m_e ordering unargued | Argued: second term trades v ≈ 10⁻³ for electron velocity ≈ α [Mitridate Sect. II] | 1.4 ALP |
| 1.4 Dirac → Majorana opaque | Said in plain words first, field-theory phrase second | 1.4 inelastic |
| 1.5 S has eV² on trust | "with the normalization of Sect. 4.2" | 1.5 |
| 1.5 α as a speed | "α c in conventional units" in text and factor list | 1.5 WE |
| 1.5 KID, Fermi level, impact ionization | Glossed | 1.5 |
| 1.5 fig numbers not recomputable | R8 | 1.5 |
| D.1 gather / cite clash | P rows | D-1 |

## Reader b, persona b (B)
| item | fix | location |
|---|---|---|
| g_* at 1 GeV | D-A4 row | 1.1 |
| Xenon thresholds | Says which analysis: Kahn–Lin Sect. I few-hundred-eV scale; analyses with both signals nearer a keV | 1.1 window ¶ |
| uniaxial / optic axis / polar crystals | Glossed | 1.2 |
| Astronomy terms | R6 | 1.2 |
| Orthonormality ¶ too slow | Trimmed to one clause | 1.2 annual |
| Second-order term discussion | Kept: two sentences, needed for the exact 266.4/237.4 extremes | — |
| Brillouin zone at l.7 | R5 | 1.3 |
| m_min swing, table column, Essig clash | D and P rows | 1.3, D-1 |
| Fig exclusion cutoff | R8 | 1.5 |

## Reader b, persona c (C)
| item | fix | location |
|---|---|---|
| Comoving volume | Defined | 1.1 |
| RA/Dec glossary | R6 | 1.2 |
| 2π/a vs |G_111| | R4 | 1.3 |
| Phonon range 100 vs 150 meV | 1.1 now "optical phonons of tens of meV"; 1.3 "zero to about 100 meV" stands | 1.1 |
| Limit-box validity | "E_R well above the phonon energies, tens of meV (impulse approximation)"; lattice binding removed | 1.3 limitbox |
| Optical phonon q range | "between ω/v_max and the upper root of Eq. (1.3-region), close to 2m_χv_max", flat branch stated | 1.3 |
| Al gap | R2 | 1.5 |
| Phonon cascade | "through several anharmonic decays they eventually become acoustic phonons" | 1.5 Phonons |
| Si gap 1.11 vs 1.2 | R3 | 1.3, 1.5 |
| CsI 6.4 eV | "band gaps of about 6 eV" for NaI and CsI (cited source gives 5.9/6.4; the rounded statement is true for both) | 1.5 Photons |
| TES / QET fins | Reviewer: fine at this level; unchanged | — |
| DFT Kohn–Sham | "as Kohn–Sham states rather than true quasiparticle states" | 1.5 rate |

## Bibliography and sources added
- mohr2025codata (Rev. Mod. Phys. 97, 025002 (2025), arXiv:2409.03787; checked against arXiv API and Crossref); NIST value page saved to
  sources/review-ch01/nist/asil.txt (a = 5.431 020 511 × 10⁻¹⁰ m, 2022 CODATA).
- yeh2023doubling (Phys. Rev. Mater. 7, 114801 (2023), arXiv:2305.06084; checked against arXiv API); text extract in
  sources/review-ch01/d2305.06084/ (bulk Al T_c = 1.2 K; films up to 2.4 K).
