# App. E.14–E.27 revision log (2026-11-02)

Sources: accuracy-1.md (A1), accuracy-2.md (A2), prose.md (P), reader.md (R), appE2/editor-notes.md (EN), partII/editor-notes.md (P2), brief appE2-revise.md (B). "Done" = fixed in the text without announcement. Locations are file and subsection. Nothing was run (compute policy); four sources were fetched for verification (sources/review-appE2rev/: 1304.7684, 2301.07617, 2507.14287; 1910.02091 HTML already in sources/D-c).

## Editor rulings (B, EN)

| # | Item | Fix | Location |
|---|---|---|---|
| B1 | Rewrite E.14; break the recipe pattern | E.14 rewritten as argued prose: opens on why the rate is uncertain and what makes the amplitude hard; content headings ("The loss function and its inputs", "Physical controls", "Where the phonon-assisted rate stops leading", "Verification of the onset", "Germanium and gallium arsenide", "Fano widths and detunings in GaAs", "The f-sum check…"); Cost and Pitfalls sections removed (costs into a cost column of tab:E14-params; the two new pitfalls folded into controls; rest already stated in place). Elsewhere: acceptance-first orderings kept/added (E.15 BSE, E.18 Migdal), "The quantity is…" openers replaced where they led a subsection (E.16 intro, E.20 conserving, E.21 color centers, E.25 collection kernels), cost sentences merged into tables (E.20). | E-14 all; E-15 l.3–20; E-16 l.3; E-20; E-21; E-25 |
| B2 | Remove project history | Deleted/rewritten: "has been computed once", "pre-registered", "the old 0.89", "the first calculation chose", "that route has already been taken", "In the one calculation done so far", "is no longer open", "turn three open rows into established ones" (E.14); "has been run … only", "In silicon this has been computed" (E.15); "which 4.3 did not estimate … stands until it is computed", "interim factor" (E.16); "no longer carry estimates" (E.17); "and 16.7 labels it so" (E.19); "and the text states that choice", "are kept or explicitly dropped" (E.20); "A new module" ×3, "computable and missing" (E.21); "lists their prediction as an open calculation" (E.23); "the first one will be new" (E.24); overflow-list story, "the exciton module is new code" kept once as a fact (E.25); "never copied from a template" (moved Fano map). | E-14…E-26 |
| B3 | Cuts to word targets | Raw wc after revision: E.14 3,834 (target ≈ 3,600 incl. Fano map; the cost column and the new-code/replica/Sternheimer statements required by A1 add ≈ 200), E.20 3,211 (≈ 2,800; the new parameter table tab:E20-dirac, required by P #20, adds ≈ 120), E.21 2,724 (≈ 2,350; the NV cutoff/k grid, color-center convergence, ML surface, bond target and molecular-band count required by A2/R add ≈ 300), E.22 3,215 (≈ 2,900; BvK-length prescription and TLS transplant add ≈ 150), E.25 3,924 (≈ 3,700; kinetics grid added). Each section was cut by the prose report's (a)–(h) list; the residual overrun is gap-filling the brief also requires. | — |
| B3 | Duplications | E.14/E.5: quadrupole and operation count now a pointer to E.5. E.23/E.11: E_d/p_FP protocol now E.11's (directions, steps, cell, run length); E.23 states only t_pr and the DFT check. E.24/E.13: plasmon-not-twice clause now a pointer. E.25/E.12: Hecht, approximation level, lumped film → pointers to E.12. Configurational-energy rule stated once (E.23 partition), pointed to from E.22 and the E.23 pocket paragraph. | E-14, E-23, E-24, E-25, E-22 |
| B4 | One shared lattice setting | E.17 base: PBE, SG15, 60 Ry, measured a (5.431/5.658/5.653 Å), Si 12³ k/8³ q, Ge and GaAs 8³/6³, 80 Ry check for 3d. Cost derived once there (≈ 100 core-h Si, ≈ 15 Ge, ≈ 20 GaAs); E.14 ("base"), E.18 (2× base), E.21, E.25, E.26 point to it. GaAs removed from tab:E17-batch (it is the base). E.14 table and text agree with E.17. | E-17 base; E-14 tab; E-18; E-26 |
| B4 | Neutron test allows PBE TA softening | Per-branch tolerance: optical and LA 3 %; Si TA 10 % (8 % soft, Sect. 5.2); Ge TA 15 % until the 12³-k test of E.14 separates grid and functional; where TA sets an edge the neutron-scaled branch is the reference. | E-17 base; E-14 onset, Ge |
| B5 | E.14 costs 200–300 and 80–240 | Density vertices 200–300 core-h (table), ≈ 10⁶ diagonalizations (630 × 12³); Ge window 80–240 core-h. | E-14 tab, Ge |
| B5 | Onsets 0.3333/0.3375 | Neutron-scaled onsets 0.3333 and 0.3375 MeV. | E-14 onset |
| B5 | E.15 TDA attribution + pass test | ×2 error attributed to the resonant-only form (ε₁^res); retarded TDA has no ×2, residual ≈ 10 % on ε₂; S reported full / retarded TDA / resonant-only at 0.5–1.4 keV, pass |TDA/full − 1| ≤ 15 %. | E-15 BSE |
| B5 | Units E.18, E.17 | E.18 S(q;ω_l,ω_e) in eV⁻² per cell; E.17 S per cell (eV⁻¹) with the per-volume conversion stated; 𝔚^(n) made dimensionless per cell (1/Ω dropped). | E-18; E-17 multiphonon |
| B5 | G-vector count | ≈ 725 (Si), 821 (Ge, GaAs) per Q. | E-17 charge vertex |
| B5 | GaAs scissor targets | Low-temperature Γ 1.519, L 1.815, X 1.981 eV with vurgaftman2001band (already in book.bib; values are that review's recommended T → 0 parameters; table number not cited). | E-14 GaAs |
| B5 | E.23 order of magnitude | "ten to thirty times what a Frenkel pair stores". | E-23 partition |
| B5 | U_rel in E.25 | Table row now "elastic energy per component to 5 %", FEM 10²–10³ core-h added. | E-25 tab |
| B5 | essig2016direct equations | (A.18)–(A.21). | E-26 fermionic |
| B6 | Pointers | app:D.46 → sec:21.2 (no D.46 exists); E.18 drag inputs → app:E.17; E.24 BSE app:E.3 → app:E.6 (×3). | E-27, E-18, E-24 |
| B6 | Implausible costs | E.16: full R⁰_GG′ ≈ 600 TB on the full grid → stored on a coarse subset (≈ 10 GB); Dyson by iterative solve for the needed RHS; ≈ 10³ core-h (Si). E.18 Migdal: matrix at 72 reduced p (not the 50³ Cartesian grid, ≈ 10¹⁹ ops), frequencies contracted on the fly, ≈ 10⁴ core-h. E.21 color centers: ML surface fitted to ΔSCF points (direct hybrid surface hopping 10⁶–10⁷ stated). E.15 STE raised to ≈ 10⁴ core-h. | E-16 library; E-18; E-21; E-15 |
| B6 | E.22 supercell series | Cells 54/128/250 at Γ only (L = cell side), or one fixed-density grid with L its BvK length; shrinking grids ruled out. | E-22 ohmic |
| B6 | Name targets | MOF: InF₃(4,4′-bipyridine) (romao2023chiral, verified in the fetched extract); lanthanide host/ion → Sect. 14.5; magnetoelectric crystal: Cr₂O₃; molecular solid for bond breaking: anthracene (C–H). | E-19, E-20, E-21 |
| B6 | Units of S | Stated once in E.17 (per cell eV⁻¹ = per volume eV² × Ω); E.18 eV⁻² per cell; E.19 "per volume, eV²"; E.21 donors eV⁻¹ per donor; low-dimensional S per area/length with 2πδ normalization. | E-17, E-18, E-19, E-21 |
| B7 | E.24 GAPs | W^scr grid to 60 eV, free-electron kernel above (cap need not be reached by W); A_AB = 5.2 and ΔA_AB = 1.3 stated; Ge 77 K pair energy flagged as an input to be fixed by a measurement with the same definition (no source in book.bib); 50–1500 eV photon validation run at 300 K. | E-24 |
| B7 | E.26 pair absorption and Barkas tests | Pair: scalar reduction to single absorption at ω = 2m_φ, k → 0 and analytic velocity moments to 10⁻³; Barkas: electron-gas Z₁³ stopping correction and linear limit; Barkas grid (50 r_s, E.16 (q,ω) grid). | E-26 two insertions |
| B7 | E.27 cosmic-ray spectra | Gordon et al. neutron spectrum (five US sites, scaled to New York City, mid solar modulation) and measured sea-level proton spectra, as used by saldanha2020 (verified in the extract); tritium 124 ± 25 total, 112 ± 24 neutrons. | E-27 cosmogenic |
| B7 | NV⁻ cutoff and k grid | SG15 C/N 80 Ry, Γ checked on 2³ (512 atoms); third size 1728 atoms (PBE) if 512→1000 is not stable. | E-21 NV |
| B7 | E.23 kernel grid | 10 E_coll × 8 b_imp = 80 points; ≈ 250 core-h per trajectory → 10⁶; HSE subset a few 10⁶ costed. | E-23 kernel |
| B7 | Bond-breaking target | Anthracene, C–H bond. | E-21 |
| B7 | Color-center convergence | STE/F–H energies to 0.1 eV between 64 and 216 atoms; E_d to 1 eV on doubling directions; ML surface to 50 meV on held-out points. | E-21 |
| B7 | α̃ in E.20 | α̃ = α/(ε_bg v_D) (eq:7.3-alpha); ZrTe₅ from the implemented row of Geilhufe Tables 1–2 (as we:7-zrte5): Δ_D 15.6 meV, v_D 7.6×10⁻⁴, ε_bg 50.5, g_deg = 2 → α̃ = 0.19 (Hochberg Table 1: 0.20; their 0.80 is g_deg α̃ with g_deg = 4), "α̃ ≈ 0.2". Recomputed Ry_D ≈ 0.14 meV, a_D ≈ 1.0×10³ Å, grid ratio 19. The earlier Δ_D = 11.8 meV was Geilhufe's unoptimized-cell value and v_D = 1.3×10⁻³ the experimental row; both replaced. New tab:E20-dirac with the three materials (values read from the source HTML). | E-20 ZrTe₅ |
| B7 | Relativistic-shift naming | E.15: "mass–velocity shift … −0.58 % in the Thomas–Fermi estimate", tested crystal-vs-atomic (E.16) to 0.1 %; E.16: total −0.23/−0.73 %, mass–velocity part −0.58 % (Ge). | E-15 core; E-16 |
| B7 | Sternheimer remainder above 1.86 keV | Correction below ≈ 1.9 keV; carried in full on 1.9–2.5 keV bins. | E-14 inputs |
| B8 | Register | "must" cut by about a third in the rewritten passages (E.14 rewritten with "has to"/statements), "however" added (E.14, E.15, appE), "we" where choices are made; American spelling (aluminum ×4, one-center ×2). | all |
| B9 | Summary | Reviewer's two sentences added; opening lists 𝒦 and 𝔐. | appE.tex |
| B10 | DEFERRED-COMPUTE | Dated note; DC-1 (window values, replica shell, Sternheimer range, 10¹⁶ flop, cost), DC-5, DC-6 (0.407 vs ≈ 0.50 MeV; 0.547/0.62 withdrawn), DC-11 (2–3×10³ core-h), DC-12 (≈ 10⁴, ×2), DC-14 (≈ 10³ Si, storage plan), DC-22 (G count). | state/DEFERRED-COMPUTE.md |

## Accuracy part 1 (A1) — remaining items

| Item | Fix / reason | Location |
|---|---|---|
| E.14-1 optional clarity | 0.405–0.408 state named as the glide class with small vertex. | E-14 stops leading |
| E.14-3 replica shell | Stated: E.15 envelope × free-pair amplitude, matched at E_g + ω_TA. | E-14 inputs |
| E.14-10 Ge 6³ cost; wording | Shared-base Ge DFPT ≈ 15 core-h (13–16 min/q); PBE-order sentence reworded so 0.744/0.89 are the measured order. | E-17; E-14 Ge |
| E.14-12 GaAs window cost basis | 8 core-h (scissor) and 40–80 core-h (hybrid), 4-core convention. | E-14 GaAs |
| E.14-14 flop/total | Amplitude cost now E.5's count; CPU total 350–450 core-h. | E-14 inputs, tab |
| E.15-5/6 DC alignment | Done (DC-11, DC-12). | DC |
| E.15-7 | Done (B7). | — |
| E.16-1 DC-14 | Done. | DC |
| E.16-8 kinetic row | 𝒯_e = p²/2m_e² normalization stated; equivalence to Σ_m p·p over all bands incl. core. | E-16 kinetic |
| E.17-2 deformation cost | Declined: "minutes" vs DC-18 5–20 core-h is minor and the frozen-strain run on a 2-atom cell is minutes on four cores. | — |
| E.17-12 missing costs DC-92/94/95/98 | Batch rows added to tab:E17-batch. | E-17 table |
| E.19-1 garbled cost | Rewritten. | E-19 |
| E.20-6 α̃ | Done (B7). | E-20 |
| Executability E.14 new code | "a few hundred lines on top of EPW". | E-14 inputs |
| E.16 PAW f-sum threshold (optional) | Declined: the 95 % rule is stated for NC + commutator; a PAW threshold has no source value. | — |

## Accuracy part 2 (A2) — remaining items

| Item | Fix / reason | Location |
|---|---|---|
| E.21 n_c used (optional) | Declined: the ratio 0.3–0.6 is quoted as in the record; adding a second n_c invites two numbers. | — |
| E.21 TB overlap model | Envelope radius a* and central-cell correction of Sect. 16.5 named; DFT clusters at the shared setting. | E-21 donors |
| E.21 Du et al. "estimated" | "changes the estimated heavy-mediator rate". | E-21 |
| E.21 tube f-sum normalization | S per unit length with 2πδ; f-sum stated in that normalization. | E-21 low-D |
| E.22 four vs five targets | Cost now per defect (10³ GPU-h each). | E-22 |
| E.22 pairs per glass | ≈ 10⁴ screened pairs per glass stated. | E-22 ensemble |
| E.24 cap vs W grid; A_AB; Ge 77 K; 300 K | Done (B7). | E-24 |
| E.25 Y_ph 95 % C.L.; 12.7 % | Both stated. | E-25 kinetics, space charge |
| E.25 kinetics grid | 20 E_R values 10 eV–10 keV, fields 0/1/4/40 V/cm, impurity census of the modeled detector. | E-25 kinetics |
| E.26 GIPAW/DFPT convergence | Shared setting, 1 % in cutoff and k. | E-26 coherent |
| E.26 wrong locator | Done. | E-26 |
| E.27 tritium components | Done. | E-27 |

## Prose (P) — items not covered above

| Item | Fix / reason | Location |
|---|---|---|
| Opening E.14 re-frames appendix | Outline sentences cut. | E-14 opening |
| E.14 "The book knows" | "That rate is known only to a factor of ten." | E-14 |
| E.14 dramatic frame (gauge) | Lin-style "Everything hinges on one gauge…". | E-14 inputs |
| E.14 ordinal six controls | Each control opens with what it tests. | E-14 controls |
| E.15 roadmap, imperative, colon-reveal, "of order" | Rewritten. | E-15 |
| E.16 8-item roadmap; "a quarter of it"; "two diagnostics"; "spec"; 2W; next rung; "Convergence has five parts" | Rewritten. | E-16 |
| E.17 title, roadmap, "Three traps", "It", "one runs", "Four rules … First" | Rewritten. | E-17 |
| E.18 "these four"; "previous subsection"; "converse" | Named; \cref{app:E.18-drag}; "err in opposite directions". | E-18 |
| E.19 lint sentence l.59 | Split. | E-19 |
| E.20 title; 𝔩_e; #20 Tables 1–2; "pitfalls are sign…"; previous subsection | "ZrTe₅ and corrected Dirac reaches"; defined; tab:E20-dirac; rewritten; \cref{app:E.20-magnet}. | E-20 |
| E.21 title; "new module" ×3 | Short title both forms; passive constructions. | E-21 |
| E.22 aluminium; "Two numerical errors are worse"; "One number settles"; pilot/production; closing; code-manual aside; counterfactual; memory arithmetic; Poisson; coth derivation; spin counting | Done as listed in P Length (a)–(g); closing sentence added. | E-22 |
| E.23 bare units; "lists … open"; missing verb | Done. | E-23 |
| E.24 "four changes"; "three more"; "which"; tautology; six-calculations parallel | Named list; "four more"; subject made explicit; tautology cut; opener "two cascades, two tests…, two sets of inputs". | E-24 |
| E.25 ε₀ clash | Field jump written e n_s/ε₀ (HL units) with the SI form labeled; NOTATION already reserves ε₀^SI for quoted SI formulas. | E-25 space charge |
| E.25 "last subsection"; #20 Guruswamy; abstract closer; opener | \cref{app:E.25-film}; trend stated with reason; closer starts with content; opener rewritten. | E-25 |
| E.26 title; "earlier specifications"; v₀; stray comma; stacked hedge; #20 bauer; ρ_χ rescale; "0.3 eV" collision; template clause; closing | "Coherent and second-order absorption"; \crefrange{app:E.14}{app:E.16}; v₀ defined → Sect. 1.2; fixed; fixed; pair tensor → Sect. 10.8 (source cited for Eqs. (5)–(8); the tensor itself belongs in 10.8, decline to restate it in an appendix spec); source density 0.39 GeV cm⁻³ and factor 0.59 stated (verified in fetched 2507.14287); Fano map moved, collision rewritten in E.14; template clause cut; closing added. | E-26, E-14 |
| E.27 title; GPU job; saturation; #20 shell-model; awkward closer | "Halo, background and nuclear-spin inputs"; fixed; fixed; ⟨S_n⟩, ⟨S_p⟩ for ²⁹Si and ⁷³Ge from klos2013 Table III (fetched, read); "can be quoted without the standard halo". | E-27 |
| Writer split (\mathrm{d}, \num{e3}, E_{\mathrm{g}}, \mathrm{Im}) | Macros \dd, $10^n$, \Eg, \Imag used in E.23–E.27. Γ markup left as is (upright either way). | E-23…E-27 |
| Table abbreviations | Spelled out in captions (KK, CNT, ML, KKR, NEB, SCF, MD, TDDFT, MLIP-MD, MC, GW+BSE; "Si gate" replaced). | tables |
| Restating target sections (E.20 l.36/l.7, E.21 l.49/l.32, E.25 l.37/l.29) | Reduced to clauses with \cref. | E-20, E-21, E-25 |

## Reader (R) — items not covered above

| Item | Fix / reason | Location |
|---|---|---|
| Systemic 1: 𝒦, 𝔐 undefined in appE intro | Added to the opening. | appE.tex |
| Systemic 2: candidate lists | Pointers to Sects. 17.5/21.7 kept; the lists belong to those chapters (unwritten). Decline for now; second consistency pass after Parts II–III (EN). | — |
| E.14 "30 directions … about the valley axis" ambiguous | "30 directions in the irreducible wedge of the cubic group". | E-14 |
| E.14 Ge 16 → 36 WFs | 36 = 16 sp³ + 20 for the 3d shell, stated. | E-14 Ge |
| E.14 GaAs Z*, ε∞ source | Measured, through eq:E.17-lst. | E-14 GaAs |
| E.15 f-sum test scope | Applied to the full-coupling loss function. | E-15 |
| E.15 Z_eff ≈ 4 for Ge 3d | Declined: A1 checked the value against the record (CW1 §10); no source for a different Z_eff at hand. | — |
| E.15 model chain parameters | Hopping, gap, phonon frequency and Fock truncation stated. | E-15 replicas |
| E.15 STE inputs | Lattice constant, sampling, cutoff criterion, luminescence tolerance 0.2 eV. | E-15 STE |
| E.15 60 irreducible points | 29 irreducible points of 8³ plus Umklapp copies ≈ 60. | E-15 Migdal |
| E.15/E.24 exciton binding overlap | E.24 BSE stated as the check of E.15's effective-mass binding. | E-24 excitons |
| E.16 1D model inputs; "exact answers" | ω_Q, Q, u₀ stated; "known limits". | E-16 |
| E.16 4 Ry ≈ 37 G | Done. | E-16 |
| E.16 1×1×N cells | "conventional cubic". | E-16 step |
| E.17 coherent two-phonon at finite T | Pointwise zone sum used at 1 K and 77 K. | E-17 |
| E.17 LST 4π | Heaviside–Lorentz stated. | E-17 |
| E.18 neutron acceptance not executable | Made conditional on the tagged-recoil measurement. | E-18 |
| E.18 ph.x bare perturbation | Small code modification stated. | E-18 Wannier |
| E.19 operating temperatures | Bands at the mK operating temperature; dynamics at 50 and 100 K. | E-19 |
| E.19 glass C^IR two k-shells; 1728-atom box < 4 nm | Box sizes stated (5184 → 4.3 nm; 1728 → 3.0 nm only in the size test). The k-shell conditioning is declined here (method choice for Sect. 16.7). | E-19 glass |
| E.19 MICROSCOPE geometry | Declined: dimensions and alloy are mission data not in the sources at hand; the spec names the two cylinders. | — |
| E.20 Al N_F, v_F | v_F = 2.0×10⁶ m/s; N_F free-electron. | E-20 opening |
| E.20 ε_bg tensors side by side | One set (Geilhufe implemented row) for the threshold; ionic static tensor justified; Hochberg's 25.3 used only for re-plotting Hochberg's own curve. | E-20 |
| E.20 a-WSi text vs table | Table 1.6×10⁴–1.6×10⁵. | E-20 table |
| E.21 molecular G₀W₀ bands | Occupied counts (66, 136) and ≈ 1000 bands or a Sternheimer GW stated. | E-21 molecular |
| E.22 TLS carved into 216-atom cell | Transplant protocol stated. | E-22 vertex |
| E.22 swap MC for SiO₂ | Declined: the cited study's protocol is followed; "or a comparable method" kept. | — |
| E.23 cell 64 atoms < 15 Å | 216 atoms or more. | E-23 kernel |
| E.23 C_Aug circular | Carried as a stated, scanned parameter. | E-23 recombination |
| E.23 MLIP family | Fast linear (ACE) family fixed. | E-23 partition |
| E.24 q grid step | Steps of αm_e. | E-24 |
| E.24 wide-gap sum | 6×10⁵–2.5×10⁶ core-h (text and table). | E-24 |
| E.24 exciton k-mesh contradiction | Ionic crystals 8³→12³; Si/Ge by doubling the double-grid density. | E-24 excitons |
| E.24 3.6 vs 3.749 | 3.6 named as the room-temperature value; 3.749 at 123 K for validation. | E-24 opening |
| E.25 epoxy MLP training cost | Declined: no source basis for a number. | — |
| E.26 GaAs cutoff conflict | Fano map (now in E.14) states 90 Ry as the one departure (fully relativistic spinors with Ga 3d) from the 60 Ry base. | E-14 Fano |
| E.26 13 824 k points | "of the final shell". | E-14 Fano |
| E.27 stream grid beyond v_esc | 55 galactic-frame speeds to v_esc; columns ≈ 10⁶; 10¹² ops per mass; 5–50 GPU-h; ≈ 4×10⁴ LP variables. DC-87 not changed (not in the brief's list). | E-27 bound |
| E.27 Geant4 1–3 CPU-h | Declined: matches DC-89's source; the reader's 10–30 h has no source. | — |

## Partial / editor notes (P2) in scope

| Item | Fix | Location |
|---|---|---|
| 16.1/E.20 ZrTe₅ g_deg, α̃ | Done (B7). | E-20 |
| 0.50 MeV vs 0.405–0.408 vs 0.333/0.337 distinguished | Done in E.14 and DC rows. | E-14, DC |
| E.14–E.17 over budget; cut GaAs first | GaAs paragraph compressed; Fano map absorbed. | E-14 |
| E.25 trim vs 19.6/20.3 | Recaps of 19.5/19.6/20.5 cut to clauses. | E-25 |
| E.21 short running head | Single short title. | E-21 |

## Notes for the editor

- Ch. 5's GaAs figure uses a = 5.638 Å; the brief's shared value is 5.653 Å (used here). Not touched (ch05 outside scope).
- Two E.17 batch rows (magnetic, 23 further) carry costs from DC-94/95; their cutoffs are "per material" because the record gives none.
- Second consistency pass after Parts II–III (EN plan): candidate lists, Sect. 17.5/21.7 pointers, 10.8 pair tensor.
- DC-3 (Ge rate, 400–800 core-h) and DC-87 (stream grid, now 55 speeds, ≈ 10⁶ columns, 5–50 GPU-h) are not in the brief's alignment list and were left unchanged; align at the next ledger pass.
- Register (B8): "must" reduced by about 40 in E.16, E.17, E.22, E.24, E.25 (statements of fact instead of obligations) and removed from the rewritten E.14; "however" kept only where it marks a real contrast (E.14 controls, E.15 opening); "so" thinned in E.14.
