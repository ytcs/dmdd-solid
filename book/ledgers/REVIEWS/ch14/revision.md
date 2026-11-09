# Chapter 14 revision (2026-11-06)

Scope: tex/ch14/ch14.tex, s14-1 … s14-6, new s14-summary.tex; tex/appD/D-38.tex; Ch14 rows of tex/appF/F-rows.tex; narrow edits in appE/E-26 (t_coh), appE/E-20 (𝒢_OA), ch11/s11-8 (t_coh), ch08/s8-2 (golden-rule condition). Scripts: we14_1, we14_3, we14_4, limit14_6c (log regenerated, complete), limit14_4a (axis label), new lph14_5.py (+log), map14.py rerun. Build: private, `-outdir=/tmp/claude-0/build-ch14rev`: 0 LaTeX errors, 0 undefined citations, no undefined reference from Ch14/D.38 (51 book-wide forward references to unwritten chapters remain), no overfull box in Ch14. Lint: 0 blocking hits (EQ-PUNCT false positives on gathered/aligned; LONG-SENT warnings, mostly environment artifacts). Not committed.

Word counts (detex): 14.1 3,100; 14.2 3,400 (was 3,830); 14.3 3,880; 14.4 2,990; 14.5 4,440; 14.6 4,180 (was 6,100 incl. summary/tables; ≤ 4,400 as ruled); s14-summary 1,910 (text + two tables).

## Editor rulings R1–R10

| Ruling | Done / how |
|---|---|
| R1 "at least ΔS/|S|" | Now "an estimate of the leading correction, not a bound" with D.38's caveat (ground-state change at the same order excluded; ⟨S^z⟩, W∥ held at LSWT values): 14.1 sum-rule paragraph, WE 14.1, Limit Check 14.1a text, D.38, F row, nuisance table (basis "est."), Summary. No "bound"/"at least" left. D.38 convergence: "inverse square of the grid size", extrapolates to 0.0785 (we14_1.log: diffs 1.08e-4, 4.97e-5, 2.70e-5; n⁻² extrapolation 0.0785). WE also states it. |
| R2 neutron no-go | Key result retitled "Neutron scattering and the longitudinal spin response": model-independent statement at a given q; added "Within the localized-moment model of eq:14.4-data, transverse data at several q+G determine the full tensor". New paragraph + eq:14.4-Glat (S(k+G) = |F|² S^lat(k)), rank argument (we14_4.log: 6 shifted wavevectors → rank 6; reconstruction error 7e-16), hypotheses (dipole form factor, known basis; YIG needs basis phases). O₆/O₁₀/ALP: "not measurable without a model, but follow within the localized-moment model under these assumptions". Closing paragraph reduced; nuisance row, F row, Summary aligned. Also: q vs q+G one sentence (reader-a); dipolar interaction added to "only SOC breaks isotropy" (14.4 l.97); spin-incoherent 2/3 caveat; Lovesey citation replaced by App. C.19. |
| R3 GaAs ⟨|L^ph|⟩ | Keeps 0.124; states grid (0.126/0.118), masses (0.115/0.112), weighting (0.135/0.117) and dipole-part variation (0.175–0.107, ±40 %) cannot make a factor 2; single Cartesian component 0.062 given as a possible origin. New lph14_5.py/log. "factor-two level" removed. F row updated. |
| R4 coherence time | Book convention 1/(m v₀²) everywhere: E.26 (1.04 ms, 249 m; also line edge 3.5e-6, fixed-amplitude factor 1.99/2.7 instead of "3 to 10"), s11-8 (1.05 → 1.04 ms). "Both vs shorter" resolved: 14.3 (golden-rule mean needs the shorter; a single record matches only beyond t_coh), 14.6 opener rewritten around ²⁰⁷Pb T₂ = 16.7 ms; 14.6 "t² regime" sentence restricted to records shorter than T₂. s8-2 light pass (two sentences, ensemble mean vs single record). |
| R5 numbers | MnF₂ ω_M/ω_E: 1.3e-3 was Vaidya's M_s = 47.7 kA/m read as SI (it is M/4π); now 1.6e-2 with μ₀M = 0.74 T (we14_3.log). MnF₂: measured 1.1 meV and spin flop ~9.4 T lead; fitted fields (1.021 meV, 8.75 T) second, both 7 % low; refit ω_A = 0.110 meV, weight 0.100/0.250 per pair, 0.79 of YIG, spin flop 9.4 T, peak rate unchanged 2.6e-2 (we14_3.log). Aybas 2.9 nT = equilibrium (S13), 1.9 nT measured. 14.5 "0.23 MeV" → 0.2 MeV. YIG q_1BZ: 987 eV = 2π/a for Berlin's a = 12.56 Å; with 12.375 Å, 1002 eV = Γ–H zone corner; inscribed radius 708 eV; "every q inside the zone" below 134 keV (we14_4.log). c_M: J₂-only 1.39e-4 labelled; J₁+J₂ 1.29–1.36e-4; edge 7.3 keV, ratio 5.1, 1.46 keV (we14_1.log); 14.1, 14.2, Summary, inputs table. ×29 is an upper value (in-plane branch near 0.6 meV). Accidental zero at X added (A = B = 6J₂ − 2J₁ = 116.8 meV, we14_1.log). Summary 4.77/5.0 → exact factor 5.1; 0.073 vs 0.078 clarified (differ by ΔS²). M = 3.25 MeV from the book's D_sw (Chigusa's 3.5 MeV quoted), shift 1.1e-18 (we14_3.log). De Broglie with 2π: 148 m (we14_3.log). Also: K = 0.0973 meV; "factor of eleven" → 11.4; R_peak 3.63 s⁻¹kg⁻¹ = 1.15e8. |
| R6 labels/sources | Γ_M/ω = 1e-5 "assumed, a free parameter set to the YIG Kittel width; not a millikelvin measurement" (14.3 text, WE, MnF₂ "same assumed ratio", Summary, inputs table). 4.54 meV: "value used by Hutchings and Samuelsen and quoted by dos Santos et al." "hexaferrite" → hexagonal Lu₁₋ₓScₓFeO₃. Sm³⁺ flagged as J-mixing fragile. Fernandez L/S → "as quoted by Kwon and Min"; Abragam g ≈ 2.2 → "the value usually quoted" (still cites the unread book; see owed items); Lovesey dropped in favor of App. C.19. Alves: "for any nonrelativistic speed", boosted fraction does not apply to absorption (halo absorption triggers with full density for m_φ ≥ 1e-2 eV, cannot below); −DS_z² cited to Alves, O₄⁰ to Edwards. Røising 10.5 µC/cm², 0.02 µ_B labelled DFT for h-LuFeO₃ (x = 0). |
| R7 reproducibility | Neyman construction stated in the text (N_eff bins, statistic 𝖰, Gamma vs noncentral χ² laws, CDF = 0.05 condition) with 12.5/3.17 → 1.99 (median) and 57.4/7.72 → 2.73 at the detection threshold (reproduces Centers 2.7). limit14_6c.py extended and rerun: log now complete (41 lines, incl. 23.25/5.37 crossover, −0.674 slope, 1.758, 1.015, 135.9/8.7). Eight-site cluster: construction stated in 14.3 (cube corners, 12 bonds, H with Δ_XXZ, ω_E = 3J|S|, ω_A = 3J|S|(Δ_XXZ − 1), weight ⟨0|(S^x_tot)²|0⟩/4 in the S^z_tot = 0 ground state); ed14_3.log was already complete. |
| R8 structure/prose | Summary (\section*{Summary}), nuisance table and inputs table moved to new tex/ch14/s14-summary.tex, input last; recap paragraph after the table moved into the Summary; 14.6 = 4,180 words (cuts C1–C11 partly: Budker/Aybas reconciliation to one clause, photon statistics, k-sign discussion, line statistics, NMR background, spin-noise, material-inputs paragraph, Centers merge). 14.2: ΔS / four-lattices / extended-zone / ferromagnet repeats cut, 7 % credited to we:14-nio, 14.2.5 reduced to one paragraph (~260 words), opener outline cut. Restating endings cut: 14.4.2 last two sentences, 14.4.3 closing paragraph (one sentence), 14.5 "Open problems" subsection (lanthanide-moment item moved into 14.5.3), 14.1 l.115 restatement. Register: "so"/"gives"/"therefore" thinned in 14.2–14.6 (→ since, and, thus, however, leads to, yields), "however"/"note that" added at real contrasts; percent style \SI throughout 14.1/14.4/14.5. Definitions added: Kittel mode (forward ref at first use), Schiff moment, PMN-PT, ν and z, eq:14.5-GL symbols (θ = φ g_aγγ, χ_θ, α_me, α_M, m_P, ω_a, c), pseudo-angular momentum, phonon Hall effect, T_CM; δ′_k/ϑ_k removed (14.2.5 no longer uses them). "at 1 keV" → "at q = 1 keV". Four "??": opening and Summary pointers to Chap. 15 → "the next chapter" (Summary pointer cut as a repeat); sec:17.3 and chap:20 → prose pointers ("the comparison of channels later in the book", "the readout models later in the book"). Nuisance table: 14.4 row (g spread 0.83/0.73, q dependence 0.973), 14.5 rows added (band-average chirality; Mn₁₂ upper-well population); basis labels "data"/"named"/"bound" → "input spread"/"unsized"/(gone). Inputs table: duplicate "Corrections" column cut. Other prose items: opener 14.4 outline cut, figurative openers replaced (14.4 l.85, l.62), negation framings (14.2 l.3, 14.3 l.3, 14.5 l.68/l.107/l.142, 14.6 l.90), stacked appositive 14.3 l.56, tab:14-lande caption "it", Chigusa reconciliation reduced to a parenthesis, YIG 1750 vs 2460 G linked, Berlin factor 2 = 4 × ½, fig:14-limit → fig:14-limit-absorption, fig:14-neutron "Right:" → "(b), right-hand columns", WE 14.5 title, chapter opening (14.5 clause; one orienting sentence), D.38 self-narration and (v^M)² typo. |
| R9 notation | Ω_ion for the per-ion volume (14.1, 14.2, D.38, inputs table); Ω = unit cell elsewhere. 14.5 ω_M, η_M → ω_soft, γ_soft. Spectroscopic g → g_ion (14.3, 14.4, F rows, figure label of limit14_4a); point-group element → 𝗁. 14.2 Δ → ω_gap (gap), δ_mp (detuning). Γ_T → Γ_tg (14.6, nuisance table, F row). λ_S row corrected. M → M_sw for the dispersion mass. 𝒢 kernel → 𝒢_rd. ~40 Ch14 rows added to NOTATION.md and an R9 ruling note. |
| R10 scripts | Rerun: we14_1, we14_3, we14_4, limit14_6c, limit14_4a, map14 (map unchanged in content: box numbering still 14.1–14.8), new lph14_5. Figures unchanged otherwise (fig14_3 keeps the fitted fields; caption says so and marks the measured 1.1 meV / 9.4 T). |

## Earlier editor-note items addressed to the review

| Item | Status |
|---|---|
| 14.4 g_J vs spectroscopic g; NOTATION λ_S row | done (g_ion; row rewritten) |
| MnF₂ zero-point correction to AFMR weight (not computed) | stays unsized (nuisance row "MnF₂ not sized"); already in DEFERRED-COMPUTE |
| Γ_M assumed | done (R6) |
| MnF₂ 1.021 vs 1.1 meV | reconciled (R5) |
| SPINE 2001.10666 Eq. (35) | SPINE fix owed at merge (text cites only (25)–(27), (38), (55), (59), (19)–(20)) |
| 14.1/14.2 notation and repeats | done (w_⊥ = |S|w^M_q; repeats cut) |
| 4.54 meV source | softened (R6) |
| Ni²⁺ form-factor coefficients vs ITC table | unchanged; table number unverified (closed source), listed below |
| Rerun map14 | done |
| 14.1a rate panel (optional) | not done (optional) |
| WP4 §2.3 / magnetoelastic App. E.20 spec | not in scope (App. E pass) |
| NiO magnon–phonon unsized | stays unsized in table |
| Rückriegel (3.1) stray factor 2 | not reproduced by derivation-1 (arXiv HTML); no text change; drop the editor note |
| FSI 0.04 tagged estimate | kept ("an estimate") |
| Unread sources (Abragam, Fernandez, Lovesey) | Fernandez "as quoted by", Lovesey removed, Abragam softened; Abragam still needs the citation audit |
| Limit Check numbering vs map | consistent (labels name sections, numbers count boxes); no change |
| GaAs 0.124 vs 0.07 | R3 |
| 14.5 ω_M rename | done |
| E.20 𝒢_OA units/wording | done (units of S_jj; enantiomer difference) |
| Limit Check 14.5a/b design vs App. F plan | kept (acceptable as built; F rows describe the design) |
| Alves trigger claim | R6 |
| S^z_tot zero of R_{s^z𝒥} | derivation-2 CHECKED; wording "at least second order in SOC" with the two sources |
| E.26 2π; 8.2 light pass | R4 |
| 14.6 summary/nuisance recheck | done (rows vs final 14.4/14.5) |
| 1.99 vs 2.7–10 | R7 (2.73 printed) |
| "data" basis label | → "input spread" |
| 14.6 over budget | 4,180 words |

## Report items not covered by a ruling (all five reports)

- derivation-1 A5/14.2 l.60 "lowest level of total spin N/2 − 2": done. A3 YIG M_s link: done. A1 ×29 and X point: done. D: Ω drift and missing symbols: done (R9). F12 Rückriegel: no change.
- derivation-2 4.1 factor 2 = 4 × ½ (14.4 and F row): done; App. C.19 l.26 has the same one-cause wording: owed at the next App. C touch. 4.5 dipolar: done. 5.3 Z* = 2.09 labelled PBE of Sect. 5.5: done. 5.4 Alves/Edwards: done. 5.6 h-LuFeO₃ DFT: done. 5.7 "at least second order": done. 5.8 mean-field units in lim:14.5b caption: done. 6.2 ⟨v⊥²⟩ outside the line integral called an approximation: done (text; the figure is unaffected). 6.5 g_d collides with WE 8-sectors' local g_d; γ_n accepted clash: not changed (listed for NOTATION merge).
- prose 1–65: done as listed under R8, except item 22 (attribution style: "and collaborators" used throughout new text; "Berlin et al." kept in 14.4, where it is the established short form) and item 41 (14.4 recap of 14.3's L = (g − 2)S kept as a one-clause pointer).
- reader-a: "carried automatically" sentence (J_AB sign) added; 𝒜 sign written as sinh(θ_{k−q} − θ_k) ≃ −q·∇θ; Kittel mode forward reference; eq:14.5-GL symbols; S_nj enantiomer-odd step written out; Neyman numbers reproducible; Schiff/PMN-PT glossed; K = 0.0973 meV.
- reader-b: 2π de Broglie; B′ ∼ vE′ suppression note; R_peak digits; factor 11.4; δ′_k/ϑ_k removed; MnF₂ 4π; Sm³⁺; ν, z; "at q = 1 keV"; ??; spin-incoherent.

## Changes owed in campaign ledgers (not edited here)

- **state/CORRECTIONS.md**: (1) MnF₂ shape-shift ratio ω_M/ω_E is 1.6e-2, not 1.3e-3 (Vaidya's M_s = 47.7 kA/m is M_sub/4π; SI μ₀M_sub = 0.74–0.75 T). (2) MnF₂ reference values: measured AFMR 1.1 meV and spin flop ~9.4 T; Vaidya fitted fields give 1.021 meV / 8.75 T (7 % low); refit ω_A = 0.110 meV, weight 0.100 (0.250 per pair). (3) YIG q_1BZ = 987 eV is 2π/a for a = 12.56 Å (superseded); with a = 12.375 Å: 2π/a = 1002 eV (Γ–H), inscribed radius 708 eV, every q inside the zone below 134 keV (not 186 keV). (4) NiO c_M = 1.39e-4 is the J₂-only speed; J₁+J₂: 1.29–1.36e-4; edge 7.3 keV, two-magnon gain 5.1, 1.46 keV at 1 meV. (5) Aybas μ₀M₀ = 2.9 nT is the equilibrium value (S13); measured 1.9 nT. (6) ΔS/|S| is an estimate, not a lower bound (one-magnon defect). (7) Neutron no-go holds model-independently only; within localized moments, q+G data fix the full tensor. (8) E.26 t_coh: 1/(m v₀²) = 1.04 ms at 1 µeV (was 2π version 6.6 ms). (9) YIG uniform-mode exchange mass from the book's D_sw: 3.25 MeV (Chigusa ~3.5 MeV).
- **state/SOTA.md**: neutron-data route for longitudinal couplings: status "model-dependent (localized-moment q+G inversion)" rather than "no route"; fixed-amplitude factor reproduced as 1.99 (median) / 2.73 (threshold) vs Centers 2.7 (verified); GaAs ⟨|L^ph|⟩ 0.124 vs 0.07 open, possible single-component origin (0.062). SOTA l.145 "F^mag ∼ 0.5 at q ≈ 0.5 keV for Fe³⁺" is implausible (Fe³⁺ ⟨j₀⟩ ≈ 0.99 there): mark refuted/unused.
- **LOOSE-ENDS**: (a) source for NiO in-plane AFMR branch ~0.6 meV (stated without citation in 14.1); (b) Abragam & Bleaney g ≈ 2.2 for octahedral Ni²⁺ still cited unread; (c) ITC Table 4.4.5.2 number for the Ni²⁺ ⟨j₀⟩/⟨j₂⟩ coefficients unverified; (d) Vaidya Fig. 1 "μ₀H_SF ∼ 9.4 T" as the measured spin flop: confirm against an original measurement (Jacobs 1961, ref. 27 of Vaidya); (e) App. C.19 l.26 factor-2 wording (4 × ½); (f) E.26 still prints Γ_T for the target width (rename Γ_tg at the next App. E pass); (g) g_d (14.6) vs local g_d (WE 8-sectors); (h) SPINE 14.3 Chigusa Eq. (35) reference; SPINE 14.4 g_J → g_ion; (i) the "??" pointers were turned into prose; restore \cref{chap:15}, \cref{sec:17.3}, \cref{chap:20} when those chapters exist, if the editor prefers links.
- **NOVELTY**: (a) the q+G localized-moment inversion as the route to the longitudinal spin response from transverse neutron data (book-phase statement; standard neutron-diffraction logic applied to dark-matter tensors); (b) S^z_tot conservation forces R_{s^z𝒥}(0, ω ≠ 0) = 0 (checked by derivation-2); (c) the Neyman reconciliation 1.99 vs 2.73 of the fixed-amplitude penalty.
- **DEFERRED-COMPUTE**: (a) MnF₂ zero-point correction to the AFMR weight at ω_A/ω_E = 0.017 (exists; unchanged); (b) NiO biaxial two-constant anisotropy rate near the edge (would replace the ×29 upper value); (c) optional: per-direction ⟨v⊥²|v⟩-weighted line for the gradient coupling in Limit Check 14.6a (text calls the factorized form an approximation); (d) "Unsized leading corrections (App. F)": none added.

## Post-revision check (postrev-check.md: ACCEPT WITH FIXES), applied 2026-11-06

| Fix | Done / how |
|---|---|
| 1 Isotropy is a hypothesis | Key-result box: "Without a model of the magnet (of the spin density within the cell, or the spin-isotropy hypothesis of Sect. 14.4.3)"; 14.4.3 opener adds "at the price of a hypothesis on the Hamiltonian: spin–orbit coupling and the dipolar interaction are neglected". New label sec:14.4-iso. |
| 2 Debye–Waller in eq:14.4-Glat | e^{−2W(k+G)} written beside |F|²; text says DW taken at k+G. |
| 3 Neyman inputs (s14-6) | Bins of width 2π/t_int with one on the line peak; s = σ²_sig t_int at every record length; Q_obs = median of Gamma(N_eff, b). |
| 4 Cluster ordering threshold | "below ω_A ≈ 0.3 ω_E for |S| = 3/2, and about 0.6 ω_E for |S| = 1" (ed14_3.log gaps). |
| 5 E-26 l.7 | Single record matches the mean only for t_int ≫ t_coh; below t_coh one Rayleigh amplitude and t_int^{−1/2}. |
| 6 fig:14-2 caption | Ω → Ω_ion. |
| 7 GaAs nuisance row | "0.07 (Matas et al.; a single Cartesian component gives 0.062, a possible origin)". |
| Optional | Limit Check 14.3a caption: "The square marks MnF₂ with the fitted fields." |

Still owed: Centers et al.'s detection-threshold convention for the frequentist 2.7 was not checked against the source (LOOSE-ENDS).
