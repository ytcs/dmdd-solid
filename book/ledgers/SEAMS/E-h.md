# SEAM: E.25–E.27 (computational specifications: event-level transport; coherent fields, fermionic absorption and two insertions; halo, backgrounds and figure-of-merit inputs)

Files: tex/appE/E-25.tex, E-26.tex, E-27.tex; inserted in tex/appE/appE.tex after \input{appE/E-24} with `\setcounter{section}{24}`
(remove the counter line once E.18–E.21 exist). Sources (text extracts): sources/E-h/{1401.1937, 1607.04560, 1803.02903, 1805.09942,
2012.12430, 2303.02196}.txt; sources/E-d/1109.1193.txt (Sect. IV G, V A). Nothing was run.

## The reader now knows
- E.25: readout-window kinetics as a joint law of N_meas and E_st(t_win) given (E_R, r̂_R, ℰ, t_win, T); tables Y_ph(t_win) at
  t_win ∈ {1 µs, 100 µs, 10 ms, 1 s} and thresholds {0.3, 1, 3, 16} eV; acceptance Y_ph = 0.952 (agnese2018nuclear Sect. 4),
  (6.08 ± 0.18)% (agnese2018energy), Hecht limit. Space charge: field jump e n_s/(ε₀ε₀^SI); 1% of 1 V/cm in Si needs
  n_s = 6.5–12.9×10⁴ cm⁻²; 5–10 h at 1 Hz of 100 eV events on 1 cm² with a ~10% per-carrier trapping probability (a model input of
  albakry2023first, not a measurement). Athermal emission: D⁰ ionization needs > 10.9 THz phonons (local to the next track); Luke phonons
  ionize D⁻/A⁺; two-electron envelopes, valley–orbit splitting, Born fails at threshold, 216-atom cell gives only the central cell.
  Mark-sufficiency test: n = 2p(1 − p)(z/ΔP)² per arm (2×10⁴ at ΔP = 0.01); ΔP = 0 does not prove sufficiency. LEE inputs: U_rel by
  thermo-elastic FEM (5% under mesh ×2), epoxy MLIP (none exists; 10⁶ → 4×10⁶ atoms), b_br by KMC on the release catalogue (10% under
  50 → 100 paths, 10⁵ → 4×10⁵ packets, L → 2L); τ_av = 3/2 carries to energy only for iid finite-mean releases; shape–time factorization is
  a hypothesis. Collection kernels ℭ_s(E_ath; r_ev): two geometries (ren2021design 1×1×0.4 cm³ Si, two arrays on one face; 1-cm Ge
  cylinder), 40 log energies 0.41–62 meV, 8³ positions, 10⁴ phonons/cell, V_bias 2/4/10 V; acceptance ϖ_O to 0.01, stats < 1%,
  mean-field limit (wall-hit rate v̄/2d, ~10⁻³ loss per bounce, leman2012invited Sect. IV G); mean-field ϖ_O ≈ 0.1–0.4, position spread
  0 by construction; sub-2Δ_Al assignment sets sign of 𝔯_coll − 1; cost 2×10¹² steps ≈ 36 h on 4 cores (~140 core-h), 1-D 4.4 h,
  first pass 0.44 h. Gap release: channels ℓ, birth density N_eh E_g Σ π_ℓ s_ℓ; Robin-face probability [S/(S + D_X/L_X)]e^{−z₀/L_X};
  s_ℓ scanned as mixtures (κ_s) of a hard line and a Debye spectrum cut at 2/4/8 meV, or computed by Huang–Rhys; 13% surface
  recombination share in Ge at ±3 V (leman2012invited Sect. V A). Created spectra: L¹ bound, single-sign condition, negative
  sources never clipped. Efficiencies f_coll^(p) for CDMS II Si (76 mm × 10 mm, 4 V/cm) and SuperCDMS Ge (±2 V, ²⁰⁶Pb); ρ_g to
  ±0.02 (ρ_g − 1 = 0.24 alone ≈ 1 − Y_ph = 0.048); electrode energy referred to the contact Fermi level. Interfaces: anisotropic
  6×6 welded problem, transfer matrix, flux sum 10⁻¹⁴, reciprocity, 1 − 2E₃(2d_f/𝔩_f) vs 1 − e^{−4d_f/𝔩_f}, 34.9° / 60% trapped
  flux, fitted 0.3–0.55 is t̄P_abs. Film-cascade validation: Y_qp = 2Δ/E below 4Δ, 0.57–0.6 asymptote (guruswamy2014 Sect. I),
  600-nm fall, closure 10⁻¹⁴ at 50–350Δ, Ge prompt phonons ~200Δ_Al; overflow pitfall. Table tab:E-25-runs.
- E.26: regime test t_int vs min(t_coh, 1/Γ_T); t_coh = 6.6 ms and ℓ_coh 1.6 km at 1 µeV (v₀ = 238 km/s); NMR inputs (GIPAW
  shielding/EFG, effective field, T₁, T₂, spin temperature tanh(β_sω_L/2) = p); BAR inputs (DFPT elastic/piezo, FEM, orientation factors
  1, 3ε₀/(ε₀+2), ε₀); dln a/dln α = dln a/dln m_e = −1 as the nonrelativistic benchmark, |2δ^a_rel| ≈ 0.01–0.02 (Cu, estimate);
  multiferroics only for T ≪ T_CM. Grids: ≥ 3000 points over [m_φ, (1 + 3.6×10⁻⁶)m_φ]; Asimov statistic to 1%; random amplitude in the
  likelihood or a penalty, never both (centers2021). Fermionic absorption along ω = m_χ − q: density row (weight m_χ²/q²) + transverse
  current row; light-mediator factor (m_med² − 2m_χω + m_χ²)⁻²; DHF for q ≳ m_e/3; both-spin convention (essig2016direct Eqs. (49)–(52));
  size of the dror2021 Eq. (9) continuity defect open (−ω²/m_χ² vs (Zα)² ≈ 0.16). Two insertions: pair tensor with 20³ velocity
  quadrature (bauer2026dark), dark Compton Thomson-limit acceptance test (σ_Th = e⁴/6πm_e², agrees with hochberg2022 Eq. (2) to O(x²)),
  Barkas via HEG quadratic response + LDA. GaAs Fano map: Γ_n(k) = −2 Im Σ^FM_nk(ε_nk) at 10 K, n_g = 2; detuning δ_F; branch probability
  (Γ^(ν)/Γ^tot)(1 + c̄^F − c^F_ν) ≥ 0; |c^F| ≲ 0.3Γ/δ_F, positivity quoted only for Γ/δ_F ≤ 0.5; onset shells ±2Γ at Γ–L (~0.3 eV)
  and split-off (0.34 eV), edge shell 3Γ; run parameters and acceptance (Si control c^F = 0); costs.
- E.27: LP bound (eq:E.27-lp) with stream kernel 𝔎_i(w) and objective 𝔥(w); ≤ N_bins streams; 768 × 100 × 24 grid ≈ 1.8×10⁶ columns,
  ~2×10¹² multiply-adds per mass, 10–100 GPU-h for ~50 masses; dual certificate, lab-frame isotropic reduction, kernel positivity,
  Bonferroni, aliasing. Cosmogenic: A = Σ R_k(1 − e^{−λ_dec t_k})e^{−λ_dec t′_k}; Si ³H 124 /(kg d) (saldanha2020) ⇒ 0.17 /(kg d keV)
  below 1 keV after 100 d, 11 at saturation (8.9% of the ³H β spectrum below 1 keV, computed here with a Fermi-function spectrum);
  ACTIVIA + Geant4/TALYS; validate on Si and Ge; ³H models span 27.7–210 /(kg d) in Ge (armengaud2017 Sect. 6.3). Spin-dependent:
  incoherent only; w_iso (eq:E.27-wiso); S^inc_κ = (q²/2M_κ)g_ph,κ(ω)e^{−2W_κ}/ω at T = 0; ≥ 2 shell-model interactions (klos2013);
  ⟨ω⁻¹⟩ to 1%, bin ≤ threshold/4; coherent reuse and even–even isotopes give zero.

## Symbols introduced (with defining equation or sentence)
- E.25: t_win (readout window); N_meas (measured pair number); ℭ_s(E_ath; r_ev) (collection kernel of sensor s, fraktur C; 20.5 should adopt
  it or rename — script 𝒦 is taken by 𝔗); f_coll^(p) (collection efficiency of population p, in the f family as f_det, f_ion); ρ_g
  (gap-to-hard efficiency ratio); U_rel, Γ_min, Γ_max, b_br, s (LEE model, as 19.6 will define); π_ℓ, s_ℓ (channel flux and spectrum);
  D_X, L_X, Γ_X, S_surf (exciton diffusion constant, length, decay rate, surface recombination velocity); κ_s (mixing weight of the scan;
  local); s_hard, s_soft; τ_h (hard-part term of the 20.2 bound); n_s (trapped areal charge); E_b^D (donor binding energy, as 7.4); E_b for catalogue barriers in the LEE paragraph (as E.11); t_ν(θ, φ) (mode-resolved interface transmission); E_3 (exponential integral).
- E.26: m_med (mediator mass of the fermionic-absorption scalar portal; local); σ_Th (Thomson cross-section, distinct from σ_T);
  Γ^(ν), Γ^tot (branch and total widths, italic \varGamma); c^F_ν, c̄^F (Fano coefficient and its width-weighted mean); δ_F (detuning of a
  zero-phonon state from the nearest continuum feature; distinct from δ_w, δ_coll); β_s (spin inverse temperature), ω_L (Larmor
  frequency — clash with ω_L of 5.5, longitudinal optical frequency! editor: rename to ω_Lar or ω_L^I), p (polarization), δ^a_rel.
- E.27: 𝔎_i(w) (stream kernel, fraktur K), 𝔥(w) (objective weight), 𝓑 (velocity ball), F (velocity measure), N_i^up, λ_i (dual
  variables; λ is the exciton label — local to eq:E.27-lp, editor may prefer y_i), u₀; λ_dec (decay constant), R_k, t_k, t′_k, A (activity
  — A is the mass number: editor may prefer 𝒜_act); J_nuc, x_iso, w_iso, a_p, a_n, ⟨S_p⟩, ⟨S_n⟩, g_ph,κ(ω) (projected phonon DOS), S^inc_κ.

## Terms introduced
- readout window; mark-sufficiency test (the 18.3/19.6 hypothesis, tested); field distortion by trapped charge; collection kernel
  (event-level use), collection efficiency per population; gap-energy release channels; Robin face; anisotropic welded interface;
  film-cascade validation; coherent regime test; spin temperature; fermionic-absorption line ω = m_χ − q; pair tensor; onset shells;
  stream kernel; dual certificate; cosmogenic activity; spin weight; projected phonon density of states.

## Promises made to later sections
- 19.5: N_meas/E_st joint law; ρ_g and the two-bias residual; electrostatic-energy share of the balance.
- 19.6: the LEE model's two missing inputs (U_rel with its rate spread; b_br); mark test.
- 20.1: space-charge sheet bound (½–1 × jump); athermal-emission locality; flashing creates D⁻/A⁺.
- 20.2: the L¹ transfer bound with τ_h and its single-sign condition.
- 20.3: reciprocity 𝔫₁t̄₁₂ = 𝔫₂t̄₂₁; 1 − 2E₃ flux average; 34.9°/60% trapped flux; AMM/DMM factor 1.26 in t_l.
- 20.5: mean-field limit ϖ_O ≈ 0.1–0.4 (E.25 quotes it as "the mean-field estimate of 20.5"; 20.5 must give it), sign rule of 𝔯_coll − 1.
- 8.6/13.6: Fano coefficient and branch-probability positivity; Γ/δ_F ≤ 0.5.
- 10.9: the vector-operator continuity defect is open; 14.6: windowed response, t^{−1/2} vs (t t_coh)^{−1/4}; 21.2: eq:E.27-lp, D.46,
  leakage bound; 21.7: the Si ³H numbers (0.17 and 11 /(kg d keV)); 11.6: the incoherent spin-dependent response and w_iso.

## Notes for the editor
- NOTATION's gloss of 𝔯_coll reads "collection ratio (NR over ER)"; the research and E.25 define it as the efficiency for Luke phonons over
  that for the primary phonons of an electron recoil. 19.5 should fix the gloss.
- E.25 runs ~4,400 words against a 3,000 budget (ten items, two tables' worth of parameters in one table). Candidates for cutting: the
  LEE paragraph on b_br pitfalls and the interface paragraph's film-formula hypotheses (both belong partly to 19.6 and 20.3).
- All DC items of the three rows are placed: E.25 — kinetics (69), LEE inputs (74), mark test (75), athermal/space charge (76), kernels (78),
  gap release (79), created spectra (80), efficiencies (81), interfaces (82), film-cascade validation (83); E.26 — Fano map (38), coherent
  inputs (84), fermionic absorption (85), two insertions (86); E.27 — directional bound (87), cosmogenic (89), spin-dependent (90).

## Proposed ledger rows (the editor merges them)
NOTATION: t_win | readout window | s | E.25 (19.5 may define first) · N_meas | measured pair number | 1 | E.25 · ℭ_s(E_ath; r_ev) | collection
kernel of sensor s | 1 per energy | 20.5 (used E.25) · f_coll^(p) | collection efficiency of phonon population p | 1 | E.25 · ρ_g | gap-energy to
hard-primary efficiency ratio | 1 | E.25 · U_rel, b_br | relaxable elastic energy; release branching ratio | J; 1 | 19.6 · D_X, L_X, S_surf |
exciton diffusion constant, diffusion length, surface recombination velocity | cm² s⁻¹; µm; cm s⁻¹ | E.25 · c^F_ν, δ_F | Fano coefficient of
branch ν; detuning from the continuum | 1; eV | E.26 (13.6 may define first) · σ_Th | Thomson cross-section e⁴/6πm_e² | cm² | 10.8 ·
𝔎_i(w), 𝔥(w) | stream kernel of bin i; objective weight of the halo-independent program | counts; — | 21.2 · λ_dec | decay constant | d⁻¹ | E.27 ·
w_iso, J_nuc, ⟨S_p⟩, ⟨S_n⟩, a_p, a_n | spin weight; nuclear spin; proton and neutron spin expectation values; couplings | 1 | 11.6 ·
g_ph,κ(ω) | phonon density of states projected on species κ | eV⁻¹ | 11.6.
GLOSSARY: mark-sufficiency test; collection kernel; collection efficiency; Robin boundary; stream kernel; dual certificate; cosmogenic
activation; spin temperature.
CONCEPTS: event-level transport as the last link from cascade to observable; linear-response map of birth spectra to sensors.
CLAIMS: Si ³H 0.17 /(kg d keV) after 100 d and 11 at saturation [derived here from saldanha2020's 124 /(kg d), 12.32 y half-life,
8.9% below 1 keV]; space-charge 6.5–12.9×10⁴ cm⁻² and 5–10 h [derived; uses a ~10% model-input trapping probability]; mean-field ϖ_O
0.1–0.4 [estimate, 20.5]; kernel cost 2×10¹² steps [derived]; t_coh = 6.6 ms at 1 µeV [derived]; all costs [estimates].
INDEX: collection kernel; space charge; athermal emission; low-energy excess (inputs); Robin boundary; acoustic mismatch (anisotropic);
quasiparticle yield (validation); spin temperature; GIPAW; fermionic absorption; pair absorption; dark Compton scattering; Fano term;
halo-independent bound; HEALPix; cosmogenic activation; ACTIVIA; spin-dependent coupling.

## Revision (2026-11-02, App. E.14–E.27 review)
- E.25: Y_ph band labeled 95 % C.L.; trapping probability 12.7 %; field jump e n_s/ε₀ (HL; SI form labeled); kinetics grid stated (20 E_R, four fields, impurity census); recaps of 19.5/19.6/20.5 and E.12 benchmarks cut to pointers; LEE table row "elastic energy per component", FEM 10²–10³ core-h; new label app:E.25-film.
- E.26: title "Coherent and second-order absorption"; GaAs Fano map moved to E.14; essig2016direct Eqs. (A.18)–(A.21); pair tensor → 10.8 (bauer2026dark Eqs. (5)–(8)); source density 0.39 GeV cm⁻³ → factor 0.59; acceptance tests for pair absorption and Barkas added; GIPAW/DFPT convergence; closing line.
- E.27: title "Halo, background and nuclear-spin inputs"; app:D.46 pointer → sec:21.2; stream grid 55 galactic-frame speeds to v_esc (≈ 10⁶ columns, 5–50 GPU-h, ≈ 4×10⁴ LP variables; DC-87 to be aligned); sea-level spectra named (Gordon et al. neutrons scaled to NYC; measured protons), tritium 124 ± 25 total / 112 ± 24 neutrons; ²⁹Si and ⁷³Ge ⟨S_n⟩, ⟨S_p⟩ from klos2013large Table III.
- appE.tex: opening lists 𝒦 and 𝔐; Summary extended with two sentences on E.14–E.27.
