# Chapter 6 revision (2026-11-02)

Files: tex/ch06/ch06.tex (one nit), s6-1 … s6-5 (Summary in s6-5), tex/appD/D-16, D-17, D-18, tex/appA/A-6 (one sentence), tex/bib/book.bib
(calandra2010adiabatic eprint). No QE. The Al model (figscripts/ch06/fig6_6.py) was re-run from a scratch copy with the output redirected, to
read off the fitted force constants: λ_ep = 0.436, ω_log = 250 K, unchanged. Build: /tmp/build-ch06rev, 0 LaTeX errors, no undefined
citations; undefined references from Chap. 6 only to unwritten targets (chap:8, chap:12, chap:13, sec:11.6, sec:12.1, sec:12.2, sec:13.1).
Lint: 0 blocking in all ten files (EQ-PUNCT hits are the known \end{aligned}/\end{gathered} false positives; remaining LONG-SENT hits are
environment-opening artifacts). Format: item → fix → location. "Declined" gives the reason.

## Editor rulings (brief)
| # | Item | Fix | Location |
|---|---|---|---|
| 1 | Fan sign | "lowers the energy" → the translation Fan term ℓ²Σ(ε_n − ε_m)\|ê·p\|² written, "either sign: bands above push down, below push up"; AH "shifts it back by exactly as much" | s6-3 after eq:6.3-cancel |
| 1 | Degenerate Si VBM | Degenerate level: self-energy is a matrix in the partners; partner terms with vanishing denominators left out (Poncé Sect. III A); summed over the zone it commutes with the little group, so on an irreducible level it is ∝ 1 and each partner shifts by the average of the diagonal elements; "this is how the shifts of degenerate band edges below are defined". D.16 one clause | s6-3 after keyresult; D-16 before eq:D.16-FMmats |
| 2 | ZPR reconciliation | New paragraph after Fig. 6.4: −52/−58 (WE inversions, depend on ω_Ein and on where the slope is read; slope still grows toward a = 0.49 meV/K; a consistency test), −62/−64 (Cardona: isotope and linear extrapolation, need no ω_Ein, include +9 meV zero-point expansion), −71/−73 (e–ph part). −56.2 compared with the e–ph part, ≈20 % short (also ZG −57). Earlier ZPR paragraph reduced to the extracted values | s6-3 §ZPR ¶2, new ¶ after fig:6-gapT |
| 2 | Summary | Same three-scale comparison | s6-5 Summary ¶3 |
| 2 | Overscreening | "consistent with the overscreening … a calculation of the same kind on GW bands gives 66 meV [Zacharias Sect. VII B]" (verified in sources/review-ch06/1912.10929.txt l.1127–1138) | s6-3 new ¶ |
| 2 | −59 → −58 | done | s6-3 WE 6.3 |
| 3 | Al potential units | −3e²/(4πr), w = −3e²cos(qr_c)/[Ωq²ε_Lin(q,0)] | s6-4 model ¶ |
| 3 | Al inputs | a, M; spring tensors 0.648 (xx=yy), −0.187 (zz), 0.574 (xy) for (a/2)(1,1,0) and 0.038 (xx), −0.052 (yy=zz) for a(1,0,0), eV Å⁻², entering as Σ_R K_R[1 − cos Q·R]/M; fitted to X_L 9.69, X_T 5.78, L_L 9.69, L_T 4.19 THz (Savrasov Table I) and C11 106.8, C12 60.7, C44 28.2 GPa, ρ 2.70 g cm⁻³ (Kittel); model paragraph split | s6-4 model ¶¶ |
| 3 | WE 6.4 percentages | "9 % below the full model's 0.436 and 6 to 8 % below the measured 0.42–0.43" | s6-4 WE 6.4 |
| 4 | Bardeen 1937 | Giustino Eqs. (3)–(5) cited as Bardeen's static screening; Bardeen–Pines cited directly (bardeen1955electron) for the dynamical vertex | s6-2 §screened vertex |
| 4 | Spin factor | 6.4: Eq. (146) sentence moved to D.17 and corrected ("spin factor 2 written explicitly; its 1/τ equals γ^ep"); D.18: Giustino Eq. (200) spin implicit, Noffsinger Eq. (1) explicit; 6.5 the same in one clause | s6-4 §linewidth; D-17 §linewidth; D-18 §ε₂^PA; s6-5 after keyresult |
| 4 | Li 10.45 eV/Å | "the mean of two such combinations [Eq. (12) and the text below it]" | s6-2 §optical DP |
| 4 | Li Fig. 5 range | "linear over the whole computed range, up to 0.1 Å⁻¹"; caption: "the end of the range over which … were computed and found linear" | s6-2 acoustic ¶; fig:6-gQ caption |
| 4 | "Up to 30 %" | Stated as Calandra, Profeta and Mauri's ("note corrections of up to 30 % of the phonon frequency there"). Their source is their ref. 12, Saitta, Lazzeri, Calandra, Mauri, PRL 100, 226401 (2008); not added to the bib (arXiv id not verified this round) | s6-4 §adiabatic/nonadiabatic |
| 4 | calandra2010 arXiv | eprint = 1007.2098, archivePrefix arXiv (checked in the fetched text) | tex/bib/book.bib |
| 5 | Si quadrupole tail | g^W "still has a quadrupole … R_p⁻³, no finite range, Q⁰ direction-dependent term; small in Si and subtractable like the dipole"; GaAs sentence: quadrupoles "present in silicon as in GaAs" | s6-2 §Wannier ¶3–4 |
| 5 | Piezo origin | two terms: dynamical quadrupoles (defined in one clause: next term after Z* in the long-wavelength expansion of the induced charge of a displaced atom) and the Born charges of the strain-induced sublattice displacement | s6-2 piezo ¶ |
| 5 | Adiabatic parameter | Rule stated: response functions even in ω below the gap → (ω/E_g)²; excitation amplitudes → ω/E_g. 6.2 screening and 6.3 (insulator Migdal, closing ¶) now (ω_ph/E_g)²; 6.1 (amplitude) and 6.4 (Π) unchanged | s6-2 §screened vertex; s6-3 §Migdal |
| 5 | Local fields → Z* | Two sentences: comoving bond-charge cloud = induced density at Q+G, G ≠ 0; its dipole −e(Z − Z*) per unit displacement, ion + cloud = eZ* | s6-2 ¶ "How much is left" |
| 5 | 1/Q² vs 1/q⁴ | "Coulomb propagator 1/Q² acting on a dipole source ∝ Q … a light mediator weights more steeply, 1/q⁴, the squared propagator on a point charge" | s6-2 after Fröhlich keyresult |
| 6 | D.18 √α | "each component is a straight line …, while their sum bends at every threshold" | D-18 last-but-one ¶ |
| 6 | D.18 machine precision | Sentence (seven-orbital check) cut | D-18 after eq:D.18-M |
| 6 | D.18 m_e, ê, W_ab | m_e → m*_d (defined at first use); ê → ê_γ (with "unit polarization vector"); W_ab dropped, ê_γ·v_ab written out (6 terms) | D-18 throughout |
| 7 | Density operator | \op{n}(r) → \op{\nd}_e(r) (3×) | s6-1 §H_ep |
| 7 | Bold d clash | Rigid translation renamed 𝐭, T̂_𝐭 (6.2, 6.3, D.16); 𝐝 stays the derivative coupling; Al neighbor vector written R, not d; NOTATION rows proposed | s6-2 §acoustic; s6-3 §translation; D-16 §translation; SEAMS 6.1, 6.2 |
| 7 | Bare μ | μ_ep, a_ep (hydrogen); μ_χH (WE 6.1) | s6-1 hydrogen ¶; WE 6.1 |
| 7 | D.17 W | → E_band (E_cut is taken: plane-wave cutoff) | D-17 §mass enhancement |
| 7 | First-use definitions | ω_opt glossed ("zone-center optical phonon of silicon, 64.1 meV"); m_l/m_t → m*_d = (m*_∥m*_⊥²)^{1/3}; v_F "the Fermi velocity"; E_dir named at the 6.5 opener; w → u_rel = u₁ − u₂ (D.14) | s6-1 l.107; s6-3 lifetimes, Migdal; s6-5 opener; s6-2 Fröhlich ¶ |
| 7 | ω_Ein row | Widening proposed (Einstein energy ⟨ω⁻¹⟩⁻¹ of a spectrum, 6.3) | SEAMS 6.3 |
| 7 | A_ν vs A_TA/A_LA | WE 6.4 weights renamed I_TA, I_LA; A_ν, A_TA = A_TO = A stay 6.5's | s6-4 WE 6.4 |
| 7 | n_r first use | Already defined at eq:6.5-alpha; NOTATION first-use move proposed | SEAMS 6.5 |
| 7 | ω_D/E_F | "10⁻³ to 10⁻²" in 6.3 and 6.1 | s6-1 l.40; s6-3 after Migdal keyresult |
| 8 | A.6 | Replaced by what 5.6 and 6.3 show: shared B_κ; the first-moment double commutator fixes the mean recoil energy of which e^{−2W} is the elastic share (5.6), and, for a rigid translation, makes Σ^AH cancel the Fan term (6.3) | A-6 §Second order |
| 9 | q_min | ω ≤ qv − q²/2m_χ; threshold mass → q = 2E_g/v_max = 0.88 keV; heavy DM → E_g/v_max = 0.44 keV; both ≪ k_c = 0.85(2π/a) = 1.9 keV | s6-5 last subsection |
| 10 | Migdal counting once | Full statement: 6.3 keyresult. 6.1 keeps the estimate; 6.1 closing ¶ one sentence; 6.4 one sentence pointing to 6.3; D.17 one sentence pointing to 6.3 (prose review wanted D.17 full; ruling wins) | s6-1; s6-4 §adiabatic; D-17 §vertex corrections |
| 10 | 10 mK gap once | Stated in 6.3's closing paragraph (with the do-not-add-twice pointer to we:E-zpr); 6.3 l.139 lesson cut; WE ends "therefore sees E_g(0)"; 6.5 keeps its emission-threshold point (a different fact) | s6-3 |
| 10 | Notes to a reviewer | Cut: s6-2 Li units sentence, Verdi map sentence (one clause left), "in the notation of this book" (6.3, D.16); s6-4 Eq. (140)/(146)/(185)/(205) reconciliations (one half-width clause left); D.16 numerical-check ¶ (66 % non-rigid failure kept as one sentence); D.17 quadrature/tight-binding sentences (finite-band fraction kept as one clause); D.18 seven-orbital sentence | as listed |
| 10 | Modelling / spelling | "modelling choice" → "an approximation" (6.3 WE); Fig. 6.8 caption rewritten; core radius "a choice of the model"; "non-adiabatic" → "nonadiabatic" in Chap. 6 (ch05, D.13, E.8, E.11, E.18, E.23 still hyphenated: editor sweep); "translational" → "translation invariance" (6.3, D.16, Summary; E.8 l.59 remains); spelled percents → \SI{}{\percent} | 6.1–6.5, D.16 |
| 10 | Summary | Kohn anomaly attributed to the static bubble (own sentence); "overlap of the boosted ground state with the original one", sentence split; "restored the rest" and WORDY "in terms of" fixed | s6-5 Summary |
| 11 | Register 6.4/6.5 | Calibration rewrites applied: 6.4 l.26 ("Note that we have put the screened vertex …"), l.63 ("However, … still broadened"), "corresponds to 0.951"; 6.5 "Typical optical-phonon vertices", Noffsinger one clause, "∼10⁻²". "only"/"gives" cut in 6.4 (9→6, 11→5) and 6.5 (15→11, 10→8); "for example", "we can", "note that", "however" added where they carry the sentence | s6-4, s6-5 |

## Derivation report (derivation.md)
| # | Item | Fix | Location |
|---|---|---|---|
| 1 | Al Gaussian units | ruling 3 | s6-4 |
| 2 | Bardeen–Pines cite | ruling 4 | s6-2 |
| 3 | Eq. (146) spin | ruling 4 | D-17; s6-4 sentence cut |
| 4 | D.18 spin attribution | ruling 4; s6-5 "with the spin sum implicit" | D-18; s6-5 |
| 5 | −59 | −58 | s6-3 WE |
| 6 | Li 10.45 | ruling 4 | s6-2 |
| 7 | Li Fig. 5 | ruling 4 | s6-2 text and caption |
| 8 | Zacharias 20 % | ruling 2 (GW 66 meV wording as suggested). Zacharias' +8 meV non-adiabatic sentence not imported | s6-3 |
| 9 | WE 6.4 % | ruling 3 | s6-4 |
| 10 | Bare μ | ruling 7 | s6-1 |
| 11 | D.17 W | E_band | D-17 |
| — | κ_BO² "10⁻²" at 6.1 l.40 | "between 10⁻³ and 10⁻²" | s6-1 |
| — | D.17 l.91 machine precision | cut | D-17 |

## Reader (a)
| Item | Fix | Location |
|---|---|---|
| Kicked-then-trapped trajectory missing | X(t), Ẍ and the Fourier integral written | s6-1 |
| Derivative coupling as velocity is heuristic | "heuristically at first" | s6-1 |
| Local fields → Z* asserted | ruling 5 | s6-2 |
| Dynamical quadrupoles undefined | defined in one clause | s6-2 |
| Degenerate VBM | ruling 1 | s6-3 |
| Three ZPR scales | ruling 2 | s6-3 |
| Ξ² average "relative to k" | "averaged over the angle between Q and the valley axis, as for valleys of random orientation" | s6-3 lifetimes |
| −59 vs −58 | −58 | s6-3 |
| ~Q² remainder on trust | linear term drops out of the angular sum, stated | s6-3 |
| Al units; λ not reproducible | ruling 3 (inputs printed) | s6-4 |
| Static subtraction "too fast" | Declined beyond the 6.4 l.26 rewrite: the adiabatic subsection already states that the DFPT first-order density is the ω = 0 response that turns the bare end into the screened one | s6-4 |
| Fig. 6.6 caption garbled | reordered | s6-4 |
| Al-model paragraph too dense | split into phonon and electron paragraphs | s6-4 |
| Vertex-correction ¶ repeats 6.3 | one sentence | s6-4 |
| 6.5 vs D.18 normalization | cross-note ⟨⟨…⟩⟩ = N⁻²Σ, V = NΩ in D.18 | D-18 |
| Closing Migdal ¶ repeats | trimmed | s6-1 |

## Reader (b) / (c)
| Item | Fix | Location |
|---|---|---|
| Berry connection | one clause | s6-1 |
| Contact-interaction crossing time | "a heuristic only" | s6-1 |
| Local fields → Z* | ruling 5 | s6-2 |
| 1/Q² vs 1/q⁴ | ruling 5 | s6-2 |
| Rainbow/seagull remark | added (Rayleigh cancellation analogue) | s6-3 |
| ω_log before definition in caption | glossed in caption | s6-4 |
| Z graphs | one clause | s6-5 |
| (c) q_max = 2μv_max | shown at 6.1 opener | s6-1 |
| (c) DM–electron coupling in the same event | "a separate process, which we leave aside" | s6-1 |
| (c) Si quadrupole tail | ruling 5 | s6-2 |
| (c) piezo = quadrupoles only | ruling 5 | s6-2 |
| (c) ω/E_g vs (ω/E_g)² | ruling 5 | s6-2, s6-3 |
| (c) "converged to 14 meV" | "with an energy resolution of 14 meV" | s6-2 |
| (c) 0.048 vs 0.024 Å | reconciled in one sentence | s6-2 |
| (c) Fan sign | ruling 1 | s6-3 |
| (c) q_min kinematics | ruling 9 | s6-5 |

## Prose report (prose.md) not covered above
| Item | Fix | Location |
|---|---|---|
| 6.1 #9–11 long sentences | rewritten/split as suggested | s6-1 |
| 6.1 #12 "recoil-induced ionization" | cut | s6-1 |
| 6.1 calibration l.36 | Lin version applied | s6-1 |
| 6.2 #6 count-teaser | cut | s6-2 |
| 6.2 #7 "almost ten times" | applied | s6-2 |
| 6.2 #8 pitfalls triad | kept (content) | — |
| 6.2 calibration l.28 | Lin version applied | s6-2 |
| 6.3 #2, #3 closing paragraph | "this section leaves three facts"; "joined the other way into an electron loop" | s6-3 |
| 6.3 #6 λ_ep definition | applied | s6-3 |
| 6.3 #11 naming note | "to which we reserve the name" | s6-3 |
| 6.3 #12 narration | rewritten | s6-3 |
| 6.3 #13 passive | Poncé et al. named | s6-3 |
| 6.3 calibration l.112 | Lin version applied | s6-3 |
| 6.4 #8 long colon sentence | split | s6-4 |
| 6.4 #11 opener | names the double-counting point | s6-4 |
| 6.4 #12 text/appendix duplicates | D.17 copies cut, 6.4 keeps the physical sentences | D-17 |
| 6.5 #5 long sentence | rewritten | s6-5 |
| 6.5 #6 "first composite process of the book" | "the simplest composite process" | s6-5 |
| 6.5 #9 long paragraph | split after "instead of two" | s6-5 |
| 6.5 #10 photon momentum | rewritten | s6-5 |
| 6.5 l.49 sign-convention clause (Giustino/Noffsinger denominators) | Kept: one clause that carries the content (\|M\|² unchanged) | s6-5 |
| D.16 l.119 hedge | "usually taken to be small" | D-16 |
| D.18 "two branches" | "two components of a branch" | D-18 |
| D.18 local potential | added | D-18 |
| Opener nit | "the coupling decides" | ch06.tex |
| Summary 20 % trim | Declined in part: fixes applied; the ruling-2 sentence adds length, net length about unchanged | s6-5 |
| No limitbox (structural note) | Declined: editor-level decision, not in the brief | — |

## Editor notes not in the brief's list
| Item | Status |
|---|---|
| ω_e upright vs italic 12.1 clash note | proposed in SEAMS 6.1 |
| α_F vertex-correction claim | marked as an estimate ("we estimate … by the same counting … ∼α_F") | s6-3 |
| Optional 6.3 self-energy diagram figure | Declined (optional; Fig. 6.5(a) already draws the diagram) |
| Born–Huang App. VIII, Yu–Cardona Chap. 6, Cardona 2005, Alex 1996 | audit items, unchanged |

## Out of scope, for the editor
- E.8 l.92 attributes the ≈20 % shortfall to Zacharias directly ("attributes the underestimate to the overscreening"); 6.3 now says
  "consistent with … GW-based 66 meV". E.8 l.59 "translational"; "non-adiabatic" in ch05, D.13, E.8, E.11, E.18, E.23.
- NOTATION rows are proposed in SEAMS 6.1–6.5 (not edited in NOTATION.md). check_notation.py on ch06 + D.16–18 lists 27 gaps, all
  Chap. 6 symbols awaiting the ledger merge; the new ones (𝐭/T̂_𝐭, μ_ep, a_ep, μ_χH, I_TA/I_LA, E_band, m*_d) have rows proposed.
