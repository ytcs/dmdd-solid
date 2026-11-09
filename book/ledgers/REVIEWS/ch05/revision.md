# Chapter 5 revision (2026-11-02)

Files: tex/ch05/s5-1 … s5-7 (Summary in s5-7), tex/appD/D-13, D-14, D-15, tex/appC/C-18. ch05.tex unchanged (prose: PASS).
Numbers recomputed from the caches only (no QE): fig5_1_data.npz (frozen phonon), fig5_2_data.npz (48³ DOS), the stated elastic
constants. Scripts: scratchpad ch05rev/q4.py (quartic fits), nums.py (C.18 / Debye), dos.py (DOS ratio, ⟨u_x²⟩).
Format: item → fix → location. "Declined" items give the reason.

## Editor rulings (brief)
| # | Item | Fix | Location |
|---|---|---|---|
| 1 | 5.1 repeats D.13 | 5.1 states eq:5.1-coupled/N after one sentence with pointer; non-adiabatic counting cut to its conclusion. D.13 rewritten to derive and point back to eq:5.1-H, -adiabatic, -BO, -HF, -dcoup, -scales (no re-displays); D.13 κ numbers replaced by a pointer to WE 5.1; D.13 opener one sentence | s5-1 §Adiabatic states, §Small parameter; D-13 throughout |
| 1 | 5.5 repeats D.14; D.14 works the two-atom crystal | 5.5 keeps definitions (U, F/P, Z*, neutrality), physical paragraphs and stated results (na, LOTO, eps, LST); constraint display, two-atom e.o.m. (eq:5.5-w deleted) and ε(ω) derivation now only in D.14. D.14 points to eq:5.5-U/FP/neutral and ends its derivations on eq:5.5-LOTO/eps/LST (D.14-U, -FP, -neutral, -LOTO, -eps, -LST labels removed; none cited elsewhere). Opener now says the derivations, two-atom and general, are in D.14. Name-of-nonanalytic paragraph only in 5.5; polariton paragraph only in 5.5 | s5-5 l.3, §Born charges, §LO–TO, §LST; D-14 §Energy, §na, §LO–TO, §LST |
| 2 | Quartic constant | Refit: energies deg 4–8 and forces deg 3–5 over \|u\| ≤ 0.1–0.3 Å give Φ⁽⁴⁾ = 35–42 eV Å⁻⁴ → "about 40"; correction Φ⁽⁴⁾u²/12 = 0.003 eV Å⁻² (0.02 %) at 0.03 Å | s5-4 WE 5.6 |
| 2 | 5.7 consequences | quartic ≈ 40 eV Å⁻⁴ (l.23); ratio Φ⁽⁴⁾ℓ²/12Φ⁽²⁾ = 0.6×10⁻³ = 0.25η²; coefficients "close to one, between a quarter and two" | s5-7 §Cubic and quartic, §Small parameter |
| 2 | WE 5.3 low-energy DOS | "agree below 7 meV" → computed/Debye 1.3–1.4 at 5–7 meV (cache: 1.31, 1.34, 1.40 at 5, 6, 7 meV; 1.25 at 4 meV), ω² coefficient 1.28 = (5.89/5.42)³, PBE sound speeds softer | s5-2 WE 5.3, last ¶ |
| 2 | C.18 single named isotropic model | "isotropic [100] model": [100] speeds 8.43/5.84 km s⁻¹ in every direction, c̄ = 6.35 km s⁻¹ (3/c̄³ = c_LA⁻³ + 2c_TA⁻³), Θ_D = 696 K (+8 %); same name and numbers in WE 5.3. The transport-code Lamé set (λ = 52.4, μ = 68.0 GPa → 9.0/5.4 km s⁻¹, used by App. E.12 via Leman) is kept as a "parameter set of the codes", not a model of silicon | C-18 isotropy ¶ and after eq:C.18-cubic; s5-2 WE 5.3 |
| 2 | m_e/2M | ω² shifts by m_e/M, ω by m_e/2M | s5-1 after keyresult; D-13 last ¶ |
| 2 | κ_BO of a₀ | "fraction κ_BO of the Bohr radius" | D-13 §Power counting |
| 2 | Γ optical 0.6–0.7 % | 0.6 % in both places (63.69 vs 64.1) | s5-2 §Phonons of Si; s5-4 WE 5.6 |
| 2 | Table 5.3 Si DFPT | caption: 48³ DOS at 0 and 300 K; text adds 0.0807 Å at 300 K (0.0495/0.0799/0.0807 Å at 0/293/300 K from the cache). Table values 0.049/0.081 unchanged (now consistent) | s5-3 table caption, ¶ before WE 5.4 |
| 2 | 17/18 meV | 17 meV in 5.2 opener and Summary | s5-2 l.3; s5-7 Summary |
| 2 | 22 % | "off by up to 22 %" | s5-2 WE 5.2 |
| 2 | "2.6 %" | 5.2 now states the mean absolute difference over the eight frequencies, 2.6 %; 5.4 pointer unchanged | s5-2 §Phonons of Si |
| 2 | Supercell cost scaling | One rule (cost ∝ N_at³ × N_k, N_k ∝ 1/N_at while > 1) in the opener → 216² ≈ 5×10⁴; range L: L⁶ while k points can be thinned, L⁹ at Γ only (Baroni IV.B) | s5-4 opener; §Frozen phonons |
| 3 | Dark-photon peak at ω_L | One clause: for m = ω the mixing is screened by 1/ε, rate = ω Im ε/\|ε\|² ∝ Im(−1/ε), peak at ω_L (Knapen Eqs. (2)–(3), checked in sources/5.5/1712.06598.txt) | s5-5 §Coupling to a uniform field |
| 3 | Summary 5.5 paragraph | adds: PBE Z* right to 1 %, ε∞ 26 % high, so use the measured splitting (or computed Z* with measured ε∞), not PBE ε∞ | s5-7 Summary |
| 4 | Flensburg "measured" | "a lattice-dynamical fit to neutron data gives" | s5-1 WE 5.1 |
| 4 | Soft-TA PBE trend | TA-specific trend dropped; 8 % stated as this calculation's result; general PBE underestimate of Si/Ge phonons cited to Haxhijaj 2026 Sect. V (verified in sources/review-ch05/2601.11177.txt; its Table IV shows only 2–3 % TA softness at the PBE a, so no TA claim is attributed) | s5-2 §Phonons of Si |
| 4 | Ge has no DFPT column | one caption sentence. Note: App. E.1 l.147 says PBE at the measured a leaves a 0.047 eV gap with the wrong band order and is metallic at the PBE a; the sentence follows E.1 ("nearly metallic at the measured a … metallic at its own") rather than the ruling's shorthand "metallic at the measured a" | s5-3 table caption |
| 4 | D.15 normalization | per atom, g_ph/n_at normalized to three (eq:5.3-u2); "one atom per cell" dropped | D-15 §Debye model |
| 4 | 52.33 GeV | done | s5-3 §Zero-point length |
| 4 | Fig. 5.1 at 50 Ry | caption kept (settings already stated); no rerun | s5-1 fig caption |
| 4 | 5.7 crystal-momentum sentence | "merging with Q₁ν₁ into −Q₂ν₂" | s5-7 keyresult |
| 5 | E_R, ω_D | D.15: E_{\mathrm{R}} → E_R, \omega_D → \omega_{\mathrm{D}} throughout | D-15 |
| 5 | p_n clash | Poisson weight → p^ph_n; p_n stays the Gibbs weight (2.5), with a pointer | s5-6 eq:5.6-poisson, A(E) |
| 5 | Λ clash | Λ → Λ^ac (Λ^{ac,αβ}, Λ^ac_ν) | s5-2 §Sound speeds |
| 5 | w clash | 𝐰 → 𝐮_rel (5.5, D.14); w_p kept with a proposed row | s5-5, D-14 |
| 5 | n_A before 8.5 | kept, defined in passing (counts powers of the anharmonic expansion parameter in the response) | s5-7 §Small parameter |
| 5 | NOTATION rows | proposed in SEAMS 5.1–5.7 "Revision" sections (E^ad(u), ℓ_zp, Λ^ac, γ^G and μ_red first uses → 5.2, ∂_{κα,Q}V_KS, n_at/N_at, 𝐮_rel, p^ph_n, w_p, missing rows of derivation.md). NOTATION.md itself not edited (ledgers belong to other agents) | ledgers/SEAMS/5.*.md |
| 6 | "We will" runs | one roadmap sentence per opener (5.2, 5.3, 5.4, 5.5, 5.7) | openers |
| 6 | "In practice" | removed in 5.1, 5.2, 5.5, 5.6; kept in 5.3 and 5.7 | — |
| 6 | "gives" | 5.4: 15 → 2 (yields / finds / is / leads to) | s5-4 |
| 6 | "which is Ref." | 5× removed (as in / the form of / attached to the clause) | s5-4 |
| 6 | Seams 5.3→5.4, 5.6→5.7 | 5.3 closes on "All of this needs ω, e on fine grids …; 5.4 shows how DFT supplies them"; 5.6 closing sentence rewritten | s5-3 end; s5-6 end |
| 6 | "representative calculation", "The book writes", 8³ narration | removed / "We write" / one sentence | s5-4 WE 5.6; s5-3; s5-5 |

## derivation.md
| Item | Fix | Location |
|---|---|---|
| 1 Φ⁽⁴⁾ and 0.02 eV Å⁻² | see ruling 2 | s5-4, s5-7 |
| 2 WE 5.3 "agree below 7 meV" | see ruling 2 | s5-2 |
| 3 C.18 isotropic model | see ruling 2 | C-18, s5-2 |
| 4 D.13 bond length → Bohr radius | done | D-13 |
| 5 m_e/2M | done | s5-1, D-13 |
| 6 notation (p_n, Λ, w, ω_D, missing rows) | ruling 5 | as above |
| 5.2 "20 %" → 22 % | done | s5-2 |
| 5.2 18 → 17 meV | done | s5-2, s5-7 |
| 5.3 Giustino Eqs. (16)–(18) → (16)–(21) | done (A.6 outside scope, not touched) | s5-3 |
| 5.3 "20–30 %" → "20 to 35 %" | done | s5-3 WE 5.4 |
| 5.4 "DFPT … (Sect. 5.1)" | points to the 4³ DFPT of Fig. 5.1(b) | s5-4 WE 5.6 |
| 5.5 tab:E-functionals pointer | the 0.57 eV is attributed to "this calculation"; the table supports the measured 1.52 eV | s5-5 |
| D.13 5.0e-5 → 5.1e-5 | done (with a clause on the m_e³/M³ term) | D-13 |
| C.18 Voigt eigenvalues | "The Voigt matrix C_IJ then has three distinct eigenvalues" | C-18 |
| 5.7 keyresult merging wording | ruling 4 | s5-7 |

## prose.md
| Item | Fix | Location |
|---|---|---|
| 5.1 overlap with D.13 | ruling 1 | s5-1, D-13 |
| 5.1 l.41 comma splice | parenthesis | s5-1 |
| 5.1 l.48 N_at | "3n_at N coordinates of the nuclei of a crystal of N cells" | s5-1 |
| 5.1 l.61 count-teaser | folded into one statement | s5-1 |
| 5.1 l.129 inverted pointer | "\cref{we:5-kappa} checks its size" | s5-1 |
| 5.1 l.134 caption duplicate | deleted | s5-1 |
| 5.1 l.147 measured | ruling 4 | s5-1 |
| 5.1 l.50 trivial citation | first giustino citation dropped | s5-1 |
| 5.1 l.79 "of order" chain | rewritten with "∼" as suggested | s5-1 |
| 5.2 l.3 roadmap | one sentence; attribution moved to the dynamical-matrix citation | s5-2 |
| 5.2 17 meV, "The rest" | done | s5-2 |
| 5.2 l.109 filler | deleted | s5-2 |
| 5.2 l.119 TA trend | ruling 4 | s5-2 |
| 5.2 l.183 ħ, k_B | removed | s5-2 |
| 5.2 l.47 "In practice" | removed | s5-2 |
| 5.2 l.96 T paragraph | first sentence "Rotational invariance kills it; here is why"; index chain moved to a display | s5-2 |
| 5.3 "The book writes" | "We write" | s5-3 |
| 5.3 "convention of the whole book" ×3 | once ("the convention used throughout") in 5.3; dropped in 5.2; Summary "used throughout" | s5-2, s5-3, s5-7 |
| 5.3 l.167 mass comparison | dropped | s5-3 |
| 5.3 52.33 GeV | done | s5-3 |
| 5.3 table caption Ge / length | Ge sentence added; caption now separate sentences (DFPT grid/temperature stated) | s5-3 |
| 5.3 l.182 repeated Debye % | first percentage dropped | s5-3 |
| 5.4 l.3 roadmap | one sentence | s5-4 |
| 5.4 "gives", "which is Ref." | ruling 6 | s5-4 |
| 5.4 "representative" | removed | s5-4 |
| 5.4 0.7 vs 0.8 % | 0.6 % both | s5-2, s5-4 |
| 5.4 l.129 vague pointer | "\cref{eq:5.4-alias} read backward" | s5-4 |
| 5.4 l.143 however/but | rewritten as suggested | s5-4 |
| 5.4 2.6 % | ruling 2 | s5-2 |
| 5.4 "The picture is simple" | deleted | s5-4 |
| 5.5 overlap with D.14 | ruling 1 | s5-5, D-14 |
| 5.5 l.38 convergence log | one sentence | s5-5 |
| 5.5 l.78 semicolons | split | s5-5 |
| 5.5 l.82 signpost | "…uniform in space, the case of the coupling below" | s5-5 |
| 5.5 l.138 count-teaser | ordinals removed | s5-5 |
| 5.6 l.31 Debye restatement | one clause with pointer to WE 5.4 | s5-6 |
| 5.6 l.59 \cite\cite | separated | s5-6 |
| 5.6 l.73 "Its normalization" | "The prefactor is 2W_κ, since at t = 0 …" | s5-6 |
| 5.6 l.62 "Two cautions apply" | deleted (and "In practice" opener) | s5-6 |
| 5.6 l.109 "previous subsection" | "The momentum kick of eq:5.6-poisson" | s5-6 |
| 5.6 l.174 seam | rewritten as suggested | s5-6 |
| 5.7 l.114 n_A | ruling 5 (kept, defined in passing; the ruling overrides the prose report's "drop n_A") | s5-7 |
| 5.7 l.23 bond sentence | "its force constant falls as it lengthens" | s5-7 |
| 5.7 l.129 zero-point pressure ×3 | kept in 5.7 (pointer to E.8 added); cut to pointers in 5.1 and 5.3 | s5-1, s5-3, s5-7 |
| 5.7 "of order" ×7 | 7 → 2 (Summary scaling list rewritten with ∼) | s5-7 |
| 5.7 "the last part of this section" | "the effective harmonic theories at the end of this section" | s5-7 |
| Summary 18 meV, 5.5 conclusion, "whole book" | done | s5-7 |
| D.13 l.3 outline | one sentence | D-13 |
| D.14 comma splice + duplicate polariton ¶ | paragraph deleted (lives in 5.5) | D-14 |
| D.14 numerical-check sentence | deleted | D-14 |
| D.14 "these four results" | named | D-14 |
| D.15 title | "The Debye--Waller factor" | D-15 |
| D.15 normalization, ω_D, E_R, "quadruples" | rulings 4, 5 | D-15 |
| C.18 km/s | km.s^{-1} throughout | C-18 |
| C.18 "which is the form E.12 writes it", "one diagonalizes" | deleted / "we diagonalize" | C-18 |
| §4 Debye-error redundancy (iv), zero-point pressure (iii), polariton (iv) | as above | — |
| Optional "typical", raise "we will/can/see" | declined: the brief asks to thin "We will" runs; no other change | — |

## reader-a.md
| Item | Fix | Location |
|---|---|---|
| 5.1 caption "(gray dashed)" | done | s5-1 |
| 5.1 "DOS", "4³ grid" before 5.2 | declined: caption/WE forward uses with pointers to the figure, acceptable for a caption (no change of order without restructuring) | — |
| 5.2 C.18 isotropic mismatch | ruling 2 | s5-2, C-18 |
| 5.2 "relaxed" Christoffel | declined: the internal-relaxation remark is two sentences earlier in the same subsection | — |
| 5.2 second-order sound speed pace | declined: the D₁ acoustic block vanishing is the rotational-invariance argument just above | — |
| 5.3 Table grid/temperature | ruling 2 | s5-3 |
| 5.3 three zero-point lengths | ℓ_zp row proposed (SEAMS 5.1); 5.3 already reconciles the factor 2 | SEAMS |
| 5.4 cost scaling, 2.6 %, f_Hxc | rulings 2 and f_Hxc = v_C + f_xc defined | s5-4 |
| 5.4 WE quartic | ruling 2 | s5-4 |
| 5.4 PCM from eq:5.4-hess | one line inserting ∂n = R∂V_ext | s5-4 |
| 5.4 2n+1 orthonormality | declined: the text names the Lagrange-multiplier route and credits Gonze; a full proof is beyond the chapter's scope | — |
| 5.6 P₁ normalization | done | s5-6 |
| 5.7 merging sentence, n_A | rulings 4, 5 | s5-7 |
| 5.7 SCHA/TDEP pace | declined: reader marks them acceptable on trust | — |
| D.13 "bond length", repeated numbers | done (numbers replaced by pointer) | D-13 |
| D.14 typo | paragraph removed | D-14 |
| D.15 "quadruples" | done | D-15 |
| 17/18 meV | done | — |

## reader-b.md
| Item | Fix | Location |
|---|---|---|
| (b) 5.1 Ewald / SG15 bare in caption | declined: captions keep the settings; no section defines the Ewald sum to point to | — |
| (b) 5.2 rotational invariance under BvK | one parenthesis | s5-2 |
| (b) 5.2 0.8 vs 0.7 % | 0.6 % | s5-2, s5-4 |
| (b) 5.3 p_Q vs π_{−k} | one sentence | s5-3 |
| (b) 5.3 Table 0.081 | ruling 2 | s5-3 |
| (b) 5.3 three zero-point lengths | as reader-a | — |
| (b) 5.4 quartic, cost scaling, however/but | done | s5-4 |
| (b) 5.5 dark-photon Im(−1/ε) | ruling 3 | s5-5 |
| (b) 5.6 P₁ wording | done | s5-6 |
| (b) D.15 quadruples | done | D-15 |
| (b) C.18 9.0/5.4 vs 8.43/5.84 | ruling 2 | C-18 |
| (c) D.13 bond length | done | D-13 |
| (c) 5.3 B_Qν "displacement field" vs 𝐃 | declined: both names are book notation (NOTATION rows B_Qν, 𝐃); flagged, no rename at chapter level | — |
| (c) 5.4 ASR "chiefly" | done (5.4 and 5.2) | s5-2, s5-4 |
| (c) 5.5 in-medium mixing gloss | ruling 3 | s5-5 |
| (c) 5.7 Π normalization | "defined there in units of a squared frequency" (checked against D.17 eq. for γ^ep = −Im Π/ω) | s5-7 |

## editor-notes.md
| Note | Status |
|---|---|
| 5.1 E^ad(u) row; Born–Huang App. VIII; Flensburg one component | row proposed (SEAMS 5.1); "measured" fixed; citation-audit items left to the audit |
| 5.1 60 Ry rerun | superseded by the compute-policy note: 50 Ry kept and stated in the caption |
| 5.2 Dolling title, Kittel Θ_D | citation audit (not touched) |
| 5.2 D.15 normalization | done (per atom, to three) |
| 5.2 WE 5.2/5.3 vs C.18 | done (isotropic [100] model) |
| 5.2 15.5/15.53 THz | kept, as ruled |
| 5.2 γ^G first use | row proposed (SEAMS 5.2) |
| 5.2 TA 8 % with source | general trend cited (Haxhijaj Sect. V); TA-specific claim not made (no source supports 8 %) |
| 5.4 SPINE figure list | not in scope (SPINE is an editor file); noted |
| 5.4 2n+1 cites both PRA 52 papers | already so (gonze1995perturbation, gonze1995adiabatic) |
| 5.4 ∂_{κα,Q}V_KS, n_at/N_at | rows proposed (SEAMS 5.4) |
| App. E notation items | outside scope |
| 5.3 GaAs row; Ge DFPT column | GaAs row present; Ge sentence added |
| 5.3 Flensburg wording; 52.33 GeV; D.15 per atom | done |
| 5.6 Lovesey/AM audit; E_ZPL first use; E_R alignment; Bloch uncited | audit left; E_ZPL already first used in 5.6 (row proposed); E_R aligned; Bloch left uncited |
| 5.7 keys; 300 K Raman width | keys fine; 300 K width: declined in this pass (Menéndez–Cardona not fetched; WE 5.8 keeps the measured low-T width and the Klemens prediction) |
| 5.7 summary paragraphs for 5.5, 5.6 | 5.5 paragraph completed; 5.6 checked |
| 5.5 converged ε∞, Z*; 8³ superseded | used; 8³ narration removed |
| 5.5 Γ acoustic 5.8 meV before ASR | not in the text; nothing to change |
| 5.5 D.14 comma splice | paragraph removed |
| 5.5 Strauch–Dorner/Lockwood temperatures | citation audit |
| "representative calculation" | removed |

## Register counts after revision (grep)
"gives": s5-1 1, s5-2 3, s5-3 2, s5-4 2 (was 15), s5-5 1, s5-6 5, s5-7 6. "In practice": s5-3 1, s5-7 1, others 0.
"which is Ref.": 0. "of order": s5-7 2 (was 7). "We will": one per opener (5.5 and 5.6 have one more in the body).

## Build and lint
Lint (lint.py --banned BANNED-TERMS.txt): 0 blocking hits in every file; remaining non-blocking hits are EQ-PUNCT false positives
(gathered/split/aligned) and LONG-SENT on captions or sentences carrying a display.
Build: full main.tex into /tmp/build-ch05rev (latexmk): 0 LaTeX errors, 0 undefined citations. Undefined references from the revised files: chap:11, sec:11.1–11.6, sec:17.5, sec:20.2, sec:20.3, sec:6.3, sec:6.4, sec:8.5, sec:9.2, all unwritten. Not ours: sec:6.5 is undefined in this build although ch06/s6-5.tex carries the label (Chap. 6 agent).
WE 5.6 also says in one clause that the two symmetric estimates differ by 0.02 eV Å⁻², within the precision of the energies, so Φ⁽⁴⁾ comes from fits (both mock readers had derived 89 from them).
Optional reader-b item p_Q vs π_{−k}: written in words, no new symbols.
