# App. E.21–E.27 accuracy review (part 2, isolated)

Scope: tex/appE/E-21.tex … E-27.tex. Record used: SPINE rows E.21–E.27 and the DC items of their writer-only lists,
the DC source specs where a number was in doubt (CW3 §2.3 + errata §1.4; CW4 §13; CW6-errata §6; WP5-AUD §3.1; WP7-D-v2; WP7-E-v3),
SOTA, LOOSE-ENDS, SEAMS E-f/E-g/E-h. Sources: existing extracts sources/{E-d,E-f,E-g,E-h,E.10,C-c}/*.txt, plus four fetched by lit.py into
sources/review-appE2/ (2007.10584, 1509.01598, 2011.01940, 2109.08168; PDFs deleted, .txt kept). No heavy computation was run; the arithmetic
checks are one-line evaluations, and the tritium β fraction was computed with a Fermi-function spectrum.
Verdicts: CHECKED = agrees with the record, the source or a recomputation; WRONG = contradicts one of them; GAP = an executability or
clarity hole; MISSING = something the record has that the text drops.

## 0. Global
- Internal labels: a regex sweep of E-21…E-27 against all of BANNED-TERMS.txt plus DC-, LE-, CW\d, WP, COMP-, [CALC], [E-DC], GAP:, INF-
  found no hits → CHECKED.
- The brief's known case (E.14's "≈ 0.50 MeV" (2̄00) zero-phonon line versus the SOTA edge of 0.405–0.408 MeV and the PAER onset of
  0.333/0.337 MeV) lies in part 1. None of E.21–E.27 quotes a zero-phonon edge or PAER onset value. E.26 §Fano refers to "E_min^ren(q)" and
  "the edge of the off-shell window" symbolically only → nothing to reconcile here.
- SPINE pointer lists: every "(→ …)" section of each row is cited in the matching file → CHECKED.
- Cost lines against the DC cost columns: all agree within rounding (E.24 Si/Ge/GaAs 10⁵–6×10⁵ vs DC 9×10⁴–6.3×10⁵; wide-gap 4×10⁵–1.5×10⁶ vs
  4.2×10⁵–1.5×10⁶) → CHECKED, except the items flagged below.

## E.21 Dopants, color centers, molecular and low-dimensional targets
- l.3, l.14 NV⁻ ZPL 1.945 eV, singlet line 1.19 eV (1042 nm) [doherty2013] → CHECKED. 512–1000 atoms, WEST/cRPA, 4–6 orbitals, FCI, 10⁵ core-h
  = DC-47 → CHECKED. Δr ≤ π/q_max → CHECKED.
- l.14 executability → GAP: no plane-wave cutoff, k-sampling or supercell-convergence criterion for the 512/1000-atom HSE runs. The
  "stable to 5% under enlargement of the supercell" test needs a stated third size or extrapolation rule.
- l.18 "𝓃_D = 10¹⁸ and 1.8×10¹⁸ cm⁻³ sit at 𝓃_D/𝓃_c ≈ 0.3–0.6" → CHECKED against the record. WP7-B1-v2 l.332 takes the source's
  𝓃_c ≳ 3×10¹⁸ cm⁻³ [FT], which gives 0.33 and 0.6. Note: the commonly quoted Si:P 𝓃_c = 3.7×10¹⁸ cm⁻³ would give 0.27–0.48, and CW4 §13 and
  LE-109 round this to ≈ 0.5. Optional: state the 𝓃_c used.
- l.18 k₀ = 0.85(2π/a) = 1.94 keV; 3.88 and 0.685 keV (opposite valleys); 2.74 and 2.33 keV (perpendicular) → CHECKED (recomputed:
  2π/a = 2.283 keV; 2×2.283 − 3.88 = 0.686; |(−0.15, 0.15, 1)|·2.283 = 2.33).
- l.20 TB 10⁴–10⁵ sites, 100 realizations, 10³ + 10⁴ core-h = DC-51 → CHECKED. GAP: the overlap model for the hopping (envelope radius a*,
  central-cell correction) and the DFT cluster cutoff are not given.
- l.22 Du et al. misprint: factor 0.6–1.5 over 0.02–10 MeV for the heavy mediator at fixed ε; absorption unaffected → CHECKED (CW4 §13 table:
  1.47, 0.91, 0.59, 0.56). It is a model estimate [E, CALC] in the record. "With the host ε held fixed" signals this, but adding "estimated"
  would match the record's status.
- l.26–28 molecular crystals: 4³, 200 bands, 50–100 atoms, CSD structures, 590 directions, 0.4 a₀ at 30 keV (π/(30/3.73 a₀⁻¹) = 0.39 a₀),
  10³–10⁴ per crystal, ≈ 10 for tables = DC-52 → CHECKED. tan2θ two-state formula → CHECKED.
- l.32 kernels 2αI₀K₀ (shell) and e²/(q_∥(ε₁+ε₂)) (sheet, Heaviside–Lorentz) → CHECKED (consistent in one unit system).
- l.34 tube f-sum "∫ωS dω = N_ch v_D q²" → GAP. For N_ch linear channels the per-length sum rule is N_ch v_D q²/(2π) with the measure dω and
  S = Σ|⟨n|ρ_q|0⟩|²δ(ω − ω_n)/L. It equals N_ch v_D q² only if S carries the 2π of the dω/2π convention. State the normalization of S (that
  of §4.2) next to the acceptance test, or the 10⁻³ test cannot be applied.
- l.34 costs <1, 10²–10³, 10⁴ core-h = DC-53 → CHECKED.
- l.38–45 R_OPW (eq:E.21-ROPW) dimensionless, q 1–60 keV ⇒ m_χ ≈ 10 MeV (2m_χv_max ≈ 53 keV) → CHECKED. Sommerfeld 2πη/(1 − e^{−2πη}) at
  10/50/100 eV = 7.33/3.41/2.57 → CHECKED. CPU minutes and CPU hours (FSI) = DC-53 → CHECKED.
- l.49–51 color centers: ΔSCF HSE/PBE0 at 0.25/0.40, 64–216 atoms, ≥ 10³ FSSH trajectories, 10⁴ directions, 10⁵ core-h per material = DC-73
  → CHECKED. GAP: the only stated convergence target is p_FH to 10% (from the trajectory count). Add the cell-size test (64 → 216) on the
  STE/F–H energy difference and a convergence criterion for E_d(r̂).
- l.55–57 bond breaking: reduced momentum (μ₁₂/m₁)q → CHECKED. 10³ trajectories, 10³ core-h = DC-77 → CHECKED. GAP: no target is named
  ("molecular crystals"). DC-77 points to WP7-B2-v2 §10 (D5). Name at least one crystal, or say that the choice follows §16.6.
- Table tab:E21-params agrees with the text → CHECKED.

## E.22 Defects and two-level systems
- l.9 l-diagonal form α = π⁻²Σ(2l+1)δ̃_l² from ½Σ_{σν}δ̃²/π² → CHECKED. l.11 Anderson exponent and slope −α_ohm → CHECKED.
- l.11 W numbers: 5a = 15.8 Å; k_cut(60 Ry) = 14.6 Å⁻¹; N_PW = 3963×3137/59.2 ≈ 2.1×10⁵; 14 e/atom (5s²5p⁶5d⁴6s²); 7 GB per k → CHECKED.
- l.11 "the four targets cost about 4×10³" → GAP. The paragraph names crowdion-W, H-Nb, TLS in Al, its oxide and a-WSi (five items), and the
  table lists W, Nb–H, Al, AlOₓ, WSi. DC-55 counts four (Al/AlOₓ as one). Say which four, or write "about 10³ per target".
- l.13 K_b = 0.07, 0.11 → α_ohm = 0.28, 0.44 [maillet2023; sources/E.10/2009.03804.txt l.326, 347] → CHECKED.
- l.17–23 S_HR,k = ½ω_kΔQ_k² and E_reorg = ΣS_HR,kω_k (ħ = 1) → CHECKED. λ_tun as a mass-weighted WKB integral → CHECKED.
- l.25 ln(10¹³ s⁻¹ × 1 yr) = ln(3.16×10²⁰) = 47.2 → λ ≤ 23.6; two-parabola λ = (d/2)(2MV)^{1/2}: (0.75/1973)(2×26.16×10⁹×0.1)^{1/2} = 27.5;
  23.6/27.5 = 0.858 ⇒ 14% → CHECKED. (The two-parabola form, cusp at the midpoint, is right; an inverted-parabola barrier would carry an extra π/2.)
- l.27 64-atom pilot: N_PW ≈ 3.7×10⁴ at 40 Ry (Ω = 1309 Å³), 140 bands < 0.1 GB, 384 displacements per minimum, ≈ 900 SCFs, 120 core-h;
  production 10⁴–10⁵ GPU-h = DC-56 → CHECKED.
- l.29 Poisson tail e^{−S}Sⁿ/n! → CHECKED.
- l.35–38 S_pol(0) = 𝒥₃ω_D²/2π and thermal part π𝒥₃T²/3 → CHECKED (recomputed). W bulk T_c ≈ 15 mK → CHECKED. Peierls "meV atomistic,
  µeV FK" [fitzgerald2018, C-c/1806.11002.txt l.27, 112, 116] → CHECKED. 10⁵ core-h per material = DC-57 → CHECKED.
- l.53–55 TLS vertex: 216 atoms = 72 SiO₂, side ≈ 14.8 Å at 2.2 g/cm³; 2π/L = 0.42 Å⁻¹ = 0.83 keV; k_cut(80 Ry) = 16.9 Å⁻¹;
  N_PW = 3375×4830/59.2 = 2.75×10⁵; 576 bands (1152 valence e); 2.5 GB; qd = 0.51–1.01 at 1–2 keV; 2×100×1 h = 200 GPU-h; method B ≈ 10× (DC-58)
  → CHECKED.
- l.63 khomenko2020: n_active = 1008 TLS at T_f = 0.092 from 848 698 sampled minima ("order 10³ from some 10⁶") and a 100× drop in n₀ from
  hyperquenched to ultrastable [sources/E-g/1910.11168.txt l.165–166, 246, 260–263] → CHECKED.
- l.63 ≥ 10⁸ pairs, 10⁵–10⁶ GPU-h, < 10 core-h = DC-59 → CHECKED. GAP: "at least 10⁴ glasses of 10³–10⁴ atoms" combined with
  "≈ 10⁸ pairs" implies ~10⁴ pairs per glass; one sentence relating the two would make the budget checkable.
- Table tab:E-22-summary: the α_ohm cost "10³ GPU-h per defect" is consistent with DC-55 → CHECKED.

## E.23 Nuclear-recoil partition and charge yield
- l.3 E_R,th ≈ 352 eV (Si), 395 eV (Ge) = SOTA l.111/251/349 (R8 values, soft) → CHECKED. Si Y = 0.102^{+0.034}_{−0.030} at 0.10 keVnr;
  "no sign of an ionization production threshold above 100 eV" [albakry2023 Table II, abstract; E-g/2303.02196.txt l.104, 339] → CHECKED.
  Ge 64 ± 8 eVee at 254 eVnr, QF 25 ± 3% [kavner2024 abstract] → CHECKED.
- l.9 Massey: v(20 eV Si) = 11.7 km/s, ξ_M = 15.2; v(1 keV) = 82.7 km/s, ξ_M = 2.2 → CHECKED.
- l.11 216-atom cell 16.3 Å, 0.2 Å grid ⇒ 5.4×10⁵ points, 432 orbitals, 3.7 GB; 10⁶ core-h = DC-60 → CHECKED. GAP: the number of E_coll
  and b_imp grid points is not given (only the ranges and 20–50 trajectories per point), so the 10⁶ core-h cannot be reproduced from
  the text.
- l.17–19 40 log energies × 100 directions × 100 seeds; MLIP training ≈ 10⁴ PBE/SCAN configs, 50 meV/Å, 3 meV/atom; E_d by ≈ 3×10⁴ runs
  ≈ 10³ GPU-h; 20 directions BO-DFT-MD 10⁵ core-h; tables 10⁴–10⁵ GPU-h per material = DC-61 → CHECKED.
- l.21 31 meV/atom = ½ × 123 meV per 2-atom cell; 126 eV per 4096 atoms → CHECKED (the SEAM records the change from the record's 138 eV,
  which used ⟨ω⟩ = 45 meV, to §5.3's value). The reference-state protocol = WP5-AUD §3.1 (1)–(4) → CHECKED.
- l.21 "two orders of magnitude more than a Frenkel pair stores" → WRONG. A Si Frenkel pair stores ≈ 4–11 eV (close pair to separated;
  E.22 l.3 itself says "a few eV"), so 126 eV is ≈ 10–30×, one order of magnitude. Not in the record (WP5-AUD §3.1 has no such comparison).
  Correct to "one to one and a half orders of magnitude more" or "ten to thirty times".
- l.31 n ≥ 1112 from [2/(n−1) + κ/n]^{1/2} = 0.06 at κ = 2 → CHECKED (= CW5-errata A5). 10³–5×10³ GPU-h = DC-62 → CHECKED.
  Si Y and F_NR at 0.10/0.22/0.46 keV (0.9^{+0.7}_{−0.4}, 0.5^{+0.2}_{−0.1}, 1.8^{+0.6}_{−0.5}) and 3.8 eV per pair [albakry2023 Table II, Eq. (1)] →
  CHECKED.
- l.37 dense tracks: 10⁴ GPU-h + 10³ core-h = DC-70 → CHECKED.
- l.41–45 eq:E.23-fA: ∫d²ρ 𝓃³ = λ³/(3π²s²) and ∫dt/(r² + 4Dt)² = 1/(4Dr²) ⇒ Cλ²/(12π²Dr²); dimensionless (cm⁶s⁻¹·cm⁻²/(cm²s⁻¹·cm²))
  → CHECKED. < 10³ core-h = DC-71 → CHECKED.
- l.53–55 pockets: 0.2–20 keV, ≥ 10³ cascades, 10⁵–10⁶ atoms, 10–50 ps, ≈ 100 pockets, 10⁴–10⁵ GPU-h = DC-72 → CHECKED. The 0.1 eV/atom
  recrystallization energy is flagged as an estimate in the text → CHECKED.

## E.24 Electron cascades
- l.3 nielsen2026: Si 3.10 eV (DFT), "about 14.9% lower than ∼3.6 eV"; 3.50 eV with GW quasiparticle shifts + BSE loss function; Table II
  4H-SiC 7.3 vs 7.83/7.82, 3C-SiC 6.6 vs 6.90, SiO₂ 16.7 vs 18.0 [E-g/2610.16949.txt l.19–24, 490–510, 529, 613] → CHECKED.
- l.3 "Fano factor falls two standard deviations below" = E.13 l.71 (0.115 vs 0.119 ± 0.002) → CHECKED.
- l.13 rodrigues2021: ε_eh = 3.749 ± 0.001 eV, F = 0.119 ± 0.002 at 123 K [E-d/2004.11499.txt l.27–28] → CHECKED. ramanathan2020 photon data
  at 3–8 and 50–1500 eV → CHECKED [E-d/2004.10709.txt l.336–337]. GAP: the 50–1500 eV data (Scholze et al.) are at 300 K, so the validation must
  be run at that temperature, not at 123 K. The "ε_eh of germanium at 77 K" is given with no value or reference; give both (≈ 2.96 eV).
- l.9 W^scr from 0 to 60 eV versus l.13 "raising the energy cap from 100 to 150 eV" → GAP (internal consistency). Carriers above 60 eV need
  ε⁻¹ above 60 eV for the impact-ionization kernel. DC-63 says "to 60–100 eV". Either extend the W^scr grid to the cap, or state that the
  cap applies to the free-electron/asymptotic region above the 15–20 eV matching point, where W^scr is not used.
- l.11 (2/N_s)^{1/2} ⇒ 8×10⁴ → CHECKED. l.15 72×300²×200×16 B = 21 GB (72 irreducible points of Γ-centred 12³ in O_h) → CHECKED.
- l.25 z_qp = 0.8 ⇒ A_AB × 1.25; 0.084 × 1.3 = 0.11 eV (3%) → CHECKED only after reconstruction. The text never states A_AB ≈ 5.2 eV
  (from E.13: 3.71 = 1.7×1.160 + 0.084A + 1.3), so "0.084×1.3" reads like the fit's constant 1.3. GAP (clarity): write "raises A_AB ≈ 5.2 eV
  by 1.3 eV, and ε_eh by 0.084 × 1.3 eV = 0.11 eV".
- l.25–27 r_ii: 3×10⁴ core-h = DC-65 → CHECKED. l.33 w_mem = Γ_E/(Γ_E + Γ_k) → CHECKED. l.38 10³–10⁴ = DC-66 → CHECKED. The noisy-max bias
  2σ(2 ln n_k)^{1/2} → CHECKED (order-of-magnitude form of the Gumbel location).
- l.42–49 eq:E.24-dft aliasing statement; h = 0.02E_g ⇒ ≤ 12 meV of 63 meV; seconds/minutes = DC-67 → CHECKED.
- l.55 BSE 10³–10⁴ / 10⁴; capture ≈ 10⁵ per material; ≈ 6.5×10⁵ = DC-68 → CHECKED. l.57 Si FE binding 14.7 meV [shaklee1970] → CHECKED.
  Binomial thinning: mean (1 − f)N, Var = (1 − f)²VarN + f(1 − f)N, ε → ε/(1 − f), F → (1 − f)F + f → CHECKED.

## E.25 Event-level transport
- l.3 100 eV/3.75 eV ≈ 27 pairs → CHECKED.
- l.11 Y_ph = 0.952^{+0.009}_{−0.007} [agnese2018nuclear Sect. 4; E-h/1803.02903.txt l.783] → CHECKED, but the source band is a 95% C.L. The
  acceptance test should say "at 95% C.L." (otherwise it reads as 1σ and is too tight by ≈ 2). (6.08 ± 0.18)% [agnese2018energy] → CHECKED.
  Cost ≤ 10³ per set, 10³–10⁴ = DC-69 → CHECKED.
- l.9 field ionization ≳ 4×10⁴ V/cm = WP7-E-v3 C17 → CHECKED.
- l.17 n_s = ΔE ε_rε₀/e = 6.5×10⁴ cm⁻² (full jump) to 12.9×10⁴ (half jump) for 1% of 1 V/cm → CHECKED. 5–10 h → CHECKED against CW6-errata
  §6 ([E]). With albakry's 12.7% per carrier, 26 pairs per event gives 5.5–11 h. "Of order 10%" is right; the source value is 12.7% and
  could be quoted.
- l.19 45 meV ⇒ 10.9 THz; D⁻/A⁺ binding "a few meV" (≈ 0.055 E_b(D⁰) ≈ 2.5 meV, [UNVERIFIED] in CW6-errata); 216-atom cell 1.6 nm; ≈ 10³
  core-h = DC-76 → CHECKED.
- l.25 n = 2p(1 − p)(z/ΔP)² = 2×10⁴ → CHECKED; 10²–10³ = DC-75 → CHECKED.
- l.31–33 LEE inputs: 5% under mesh ×2; 10⁶ → 4×10⁶ atoms; 50 → 100 paths, 10⁵ → 4×10⁵ packets, L → 2L at 10%; 10²–10³ core-h + 10³–10⁴
  GPU-h = DC-74 → CHECKED.
- Table tab:E-25-runs, LEE row: "U_el to 5%" → WRONG (notation). The text defines U_rel, and U_el appears nowhere in E.25. Write "elastic
  energy per component to 5%" (or U_rel). The same row lists only the GPU-h; add the FEM 10²–10³ core-h.
- l.39–43 kernels: 0.1–15 THz = 0.41–62 meV; 8³ = 512 positions; 40×512×10⁴×10⁴ = 2.05×10¹² steps / 1.6×10⁷ s⁻¹ = 35.6 h ×4 = 142 core-h;
  1-D 4.44 h; first pass 0.44 h at ≈ 3% (1/√1000) = DC-78 / CW6-errata A15 → CHECKED. 2Δ(Nb-like) = 3.0 meV, 2Δ(Al) = 0.36 meV → CHECKED.
  Wall-hit rate v̄/2d → CHECKED. ≈ 10⁻³ loss per bounce [leman2012 Sect. IV G; E-d/1109.1193.txt l.664] → CHECKED.
- l.49 Robin-face probability [S/(S + D/L)]e^{−z₀/L} → CHECKED. 13% surface recombination share in Ge at ±3 V [leman2012 Sect. V A, l.844] →
  CHECKED. Cost seconds / 10³ per center = DC-79 → CHECKED.
- l.51 E_R ∈ {50, 100, 300, 1000} eV, 0.5 → 0.25 meV, ≈ 10⁸ steps = DC-80 → CHECKED.
- l.55–57 CDMS II 76 mm × 10 mm at 4 V/cm [1803.02903 l.201] → CHECKED. ρ_g − 1 = 0.24 vs 0.048 = CW6-errata §5 → CHECKED. 10¹¹ steps, 2 h
  × 4 cores = 8 core-h per geometry (DC-81: 16 for both) → CHECKED.
- l.61–63 AMM/DMM ×1.26, θ_c = 34.9°, 60% of film flux = CW6-errata l.36, 188–189 → CHECKED. 1 − 2E₃(2d/𝔩) vs 1 − e^{−4d/𝔩}: 3.0% at 0.01
  and 11.9% at 0.2 (recomputed) → CHECKED. Si–Al 0.3–0.55 [martinez2019; E-d/1805.02495.txt l.26] → CHECKED. 2–10 core-h = DC-82 → CHECKED.
- l.67 Y_qp asymptote 0.57–0.6 [guruswamy2014 Sect. I; E-h/1401.1937.txt l.128] → CHECKED. 36 meV/0.18 meV = 200Δ → CHECKED. Test points
  4.5, 6, 10–100Δ and 3, 5, 10, 40Δ = DC-83 → CHECKED.
- GAP (kinetics, l.7–11): the grid in E_R, field values and the impurity census (species, concentrations) that the rate equations need are not
  listed. The table gives only windows and thresholds.

## E.26 Coherent fields, fermionic absorption and two insertions
- l.3 t_coh = 2π/(m v₀²) = 6.56 ms and ℓ_coh = 2π/(m v₀) = 1.56 km at 1 µeV, v₀ = 238 km/s → CHECKED. The t^{−1/2} and (t t_coh)^{−1/4}
  scalings → CHECKED (WP7-D-v2 L-D3).
- l.9 tanh(β_sω_Lar/2) = p → CHECKED. dln a/dln α = dln a/dln m_e = −1 (nonrelativistic) and +2δ_rel → CHECKED. The Cu value 0.01–0.02 is
  [E, UNVERIFIED] in WP7-D-v2 l.154 and is labelled "an estimate" in the text → CHECKED.
- l.11 fixed-amplitude overstatement 3–10 [centers2021] = WP7-D-v2 IF-D7 ([ABS] level) → CHECKED. Line [m, (1 + 3.6×10⁻⁶)m] ⇒ v_max ≈ 805 km/s →
  CHECKED. 10²–10⁴ core-h, multiferroic 10³ = DC-84 → CHECKED. GAP: no cutoff or k-grid convergence criterion for the GIPAW and DFPT inputs.
- l.15 ω = m_χ − q; propagator (m_med² − 2m_χω + m_χ²)⁻², expansion 1 − 2m_χ²/m_med² + … → CHECKED (t = −m_χ² + 2m_χω).
- l.17 "[Eqs. (49)–(52)]{essig2016direct}" → WRONG (locator). Those are the arXiv-HTML sequential numbers. The PDF/JHEP numbering is
  Eqs. (A.18)–(A.21) (normalization, ionization rate, f_ion definition, dR/dlnE_R; review-appE2/1509.01598.txt l.1990–2029). Cite "Eqs. (A.18)–
  (A.21)" (the record itself flags HTML-vs-PDF numbering for 1306.6089). "[Eq. (9)]{dror2021absorption}" (vector operator times |f_ion|²) → CHECKED
  (2011.01940.txt l.363). (Zα)² = 0.155 for Xe → CHECKED. 10⁴–10⁵ core-h per crystal = DC-85 → CHECKED.
- l.21 dark Compton: σ_Th = e⁴/6πm_e² (HL) and ω′ + ω′²/2m_e = m_φ. Against hochberg2022 Eq. (2): the ratio (m+2m_e)(m²+2mm_e+2m_e²)/4(m+m_e)³
  matches the book's ω′/[m(1 + ω′/m_e)] to 6×10⁻⁷, 6×10⁻⁵, 4×10⁻⁴ at m/m_e = 0.01, 0.05, 0.1 (difference O(x³)) → CHECKED. 10² core-h, minutes
  = DC-86 → CHECKED.
- l.21 GAP: only dark Compton has an acceptance test. Pair absorption (e.g. its reduction to single absorption at 2m_φ for the scalar
  tensor) and the Barkas module (e.g. the HEG quadratic-response limit or the known Z³ stopping correction) need one each. The Barkas
  grid is not given.
- l.25–31 GaAs Fano map: |c^F| ≲ 0.3Γ/δ (first order), positivity only for Γ/δ ≤ 0.5, onset shells ±2Γ at Γ–L and at split-off 0.34 eV, edge
  shell 3Γ = CW3-errata §1.4 (l.54–56, 82–86) → CHECKED. Fröhlich Γ ≈ 3 meV at 0.3 eV (α_F = 0.068, ω_LO = 36 meV), 20–60 meV above → CHECKED.
  Run parameters (90 Ry, a = 5.653 Å, 8³ k, 6³ Q, 16 spinor WFs, 100³ fine, 13 824 k; Si 70 Ry, 8 WFs, 60³) and convergence (80³→100³,
  40³→60³, 10/5/2.5 meV, 10 meV interpolation, c^F to 10% with +20 bands) = CW3 §2.3 → CHECKED. Costs = DC-38 → CHECKED.

## E.27 Halo, backgrounds and figure-of-merit inputs
- l.7–13 eq:E.27-lp primal/dual pair → CHECKED. At most as many streams as bins → CHECKED. Single-bin lab-frame check
  N/inf_{v≥u₀}[vK(v)] for 𝔥 = Θ(v − u₀)/v → CHECKED.
- l.15 768 (N_side = 8) × 100 × 24 = 1.84×10⁶ columns; 7.7×10⁴ LP variables after the phase average; 1.8×10⁶ × 10⁶ ≈ 2×10¹² per mass;
  10–100 GPU-h for ≈ 50 masses = DC-87 → CHECKED.
- l.21 tritium in Si "124 atoms per kg and day" [saldanha2020] → CHECKED as the total cosmic-ray rate (124 ± 25). The neutron-only rate
  is 112 ± 24 (review-appE2/2007.10584.txt l.19–23). Consider "(124 ± 25), all cosmic-ray components". T½ = 12.32 yr → CHECKED. 8.9% of the
  β spectrum below 1 keV → CHECKED (recomputed 8.92%). 100 d ⇒ 0.169 and saturation 11.0 kg⁻¹d⁻¹keV⁻¹ → CHECKED.
- l.21 L/M capture lines near 1 and 0.1 keV [armengaud2017 Sect. 1; E-h/1607.04560.txt l.112–114] → CHECKED. l.23 Ge tritium models
  27.7–210 nuclei/kg/day [Sect. 6.3, l.796] → CHECKED. 1–3 CPU-h per material, a few tens to 100 core-h (DC-89: 34–102) → CHECKED.
- l.23 GAP: the "sea-level neutron and proton spectra" are not named (parameterization and normalization site). Name them (e.g. the
  parameterization ACTIVIA uses, and New York City sea level as in saldanha2020 l.1124).
- l.27–32 spin average J(J+1)/3; w_iso = (4/3)((J+1)/J)[a_p⟨S_p⟩ + a_n⟨S_n⟩]²; S^inc = (q²/2M)g(ω)e^{−2W}/ω at T = 0 → CHECKED. ≥ 2
  interactions [klos2013]; 10–100 core-h = DC-90 → CHECKED.

## Summary of corrections
WRONG (3): E.23 l.21 "two orders of magnitude" → one order (10–30×).
E.25 tab:E-25-runs "U_el" → U_rel / elastic energy. E.26 l.17 essig2016direct "Eqs. (49)–(52)" → "Eqs. (A.18)–(A.21)".
GAP (executability/clarity, main ones): E.24 W^scr to 60 eV vs energy cap 100–150 eV; E.24 A_AB ≈ 5.2 eV unstated; E.24 Ge 77 K value and the
300 K temperature of the 50–1500 eV data; E.21 tube f-sum normalization (2π); E.22 "four targets" vs five listed; E.25 Y_ph band is 95% C.L.;
E.26 acceptance tests for pair absorption and Barkas; E.27 cosmic-ray spectra unnamed; E.23 kernel grid size; NV⁻ cutoff and k grid; bond-
breaking target unnamed; color-center convergence tests.
MISSING: none of the DC items listed in SPINE for E.21–E.27 is absent from the text.
