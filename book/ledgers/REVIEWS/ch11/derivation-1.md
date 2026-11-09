# Ch11 part 1 — derivation check (s11-1 … s11-4, D-31, D-32)
Reviewer: derivation verifier (isolated). Date: 2026-11-02. No tex edited, nothing committed, no QE run.
Method: sympy for the algebra (lepton-tensor contraction, series, constants, transforms); small numpy/scipy checks for the
closed-form numbers; the cached outputs in figscripts/ch11 (we11.py re-run, about 20 s; limit11_1a/b/c re-run with savefig
disabled because they have no .log; every other .log was read as is). Sources fetched with lit.py into sources/review-ch11/
(13 arXiv papers + 1904.07915); the PDFs and the .txt files made from them were deleted afterwards, and the .html files were kept.
Verdicts: CHECKED = redone and agrees; WRONG = error with correction; GAP = not verifiable from the text, the logs or the sources.

## A. PRIORITY items (editor-notes ch11 + partII, for these sections)
- 11.4 l.99–109 / D.32 l.284–288, fermionic absorption on nuclei → CHECKED (independent sympy). For p = (m,0), k' = (q,−q q̂),
  q = m − ω, continuity J = (ρ, (ω/q)ρ q̂): the spin-averaged vector contraction is m³ρ²/q, the scalar one is mqρ². With
  1/(2m·2E') and d³k' this gives exactly (σ_F/2π)∫dω S̄ for the vector, σ_F = m²/4πΛ⁴, and an extra q²/m² for the scalar.
  The δ slope is 1 + q/M; the series are 1/(1+q_abs/M) = 1 − x + 3x²/2 and (q/m)²/(1+q/M) = 1 − 2x + 15x²/4 (x = m/M). So the
  rate goes as m²(1 − m/M) for the vector and m²(1 − 2m/M) for the scalar, as stated. The caption's "(1 − m/M)²" is right only to
  leading order, which is what it says. The normalization matches Dror Eq. (3) at M → ∞: |M|² = 4m²M²A²F²/Λ⁴.
- 11.4 numbers for the absorption → CHECKED: E_R(10 MeV) = 1.91 keV; scattering endpoint 54 meV; 1 − e^{−2W} = 0.061/0.43/0.900 at
  10/30/60.5 keV; overcount 16.4 at 10 keV; 10 % band 60.8 keV–3.00 GeV (limit11_4b.log; 1/(1+q_abs/M) = 0.902 at 3 GeV);
  Helm first zero 255.6 MeV (Lewin–Smith R₁ = 3.47 fm); proton 0.908 at 100 MeV; 46.26 keV/m; halo rms shift 1.46e-3; equal at
  31.7 MeV.
- 11.4 l.93, onsets (editor note) → CHECKED: Si q = 2(2M⟨ω⟩)^{1/2} = 92.5 keV, E_R = 164 meV; x_R = 9 gives 138.8 keV and 0.37 eV;
  m = 17.5/26.2 MeV. Ge: Θ_D = 373 K → ¾ω_D = 24.11 meV × 0.981 = 23.65 meV → 113 keV/95 meV, 170 keV/0.21 eV, 21.3/32.0 MeV.
  Ge ⟨ω⟩ = 23.6 meV is labelled as an estimate in the text; none of the fetched sources has a published Ge DOS mean (the DarkELF
  pDoS files in figscripts cover only Si, GaAs, SiC and Al₂O₃), so keep the label.
- 11.4 / 12.5 split (c₃ = BO-surface curvature vs the full Coulomb third moment) → CHECKED, kept at l.95 and D.32 l.244.
- 11.1 limit boxes (editor note: 0.48 q_BZ, 44×, 9×, WE 11.2 at 3×) → CHECKED by re-running limit11_1a/b/c: the 10 % limit is at
  0.48 q_BZ = 1.08 keV and 5 % at 0.34; the formula is 25.6 % low at q_BZ (full/formula 1.344); 43.8× and 8.8×; WE 11.2 values
  0.1494/−0.365, 0.625/0.591, 0.902/0.907; κ_η = 3.094 (c = 8.956) and 3.141 (c → 0).
- 11.3 editor note → CHECKED: n_T = 2 label for the singular TDS term (l.133); "not a 10 % certificate, 2.7×" (l.122; fig11_3.log
  2.69); Warren cited at book level only.
- partII 11.1: c̄_LA = 9.017 and c_NR1 = 8.956 km/s → CHECKED (we11.py: 9.0167, 8.956).
- partII 9.2: m_min^ac = ω_th/[2c(v_max − c)] → CHECKED (Eq. 11.1-edge); Si at 1 meV: 6.12 keV (c_LA,max), 6.39 keV (c_NR1).
  κ_η 3.14 (c → 0)/3.09 (Si) → CHECKED in the text. NOTATION row 851 still says only "constant 3.14": WRONG (outside the tex);
  add "3.09 at the sound speed of Si".
- partII C.18: the bulk-modulus floor is stated as cubic-only (l.197, l.200) → CHECKED. Proof redone: q̂·M·q̂ = C₁₁ − 2Δ_C s_Q, and
  C₁₁ − 2Δ_C s_Q − B ≥ ⅔(C₁₁ − C₁₂) (Δ_C < 0) or ≥ 4C₄₄/3 (Δ_C > 0).
- partII 11.2: check WE 8.6's GaAs nucleon vertex against the full phonons → CHECKED (we8_6_check.log): |a_N| = 0.2375/1.739 at
  13.7/100 eV along [111]; zone-center eigenvectors 0.613/4.47 (×2.6); [100] 2.06e-3, zone-center 0.354. The text at l.55 matches.
- partII 11.2: LiF inputs = computed values of 1910.10716 Table I (1.05, 2.02, 33.5–77.2) → CHECKED against the source. Factorized
  sapphire model: ε₀(LST) = 9.78 against Table I's 9.3 (5 %) → CHECKED; the text uses the factorized model.
- partII 11.2 "ω̄ → ω̄_pol" → WRONG, not yet done: s11-2 l.120 (twice) and the fig:11-limit-2b caption still print \bar\omega.
  NOTATION row 522 reserves ω̄ for 5.3 only. Rename to ω̄_pol and register it.

## B. s11-1 (Acoustic phonons)
- l.3 opening: q_max = 0.530 keV; q²/2M = 5.37 µeV; c_LA q = 15.8 meV → CHECKED.
- l.11: F_N − 1 < 1e-3 (qR = 8.8e-5 at 5 keV) → CHECKED.
- l.15 (11.1-master) → l.26 (11.1-S1): one-phonon matrix element, the factor N cancelling, 2π/Ω, (n+1)/2ω → CHECKED; DW e^{−W_κ}
  inside the modulus, consistent with NOTATION 2W_κ = q·B_κ·q.
- l.33: the CD2020 normalization (per cell) is Ω/2π × ours (their Eq. (2), (1/N)Σ|…|²δ) → CHECKED; their Eq. (7) amplitude and
  Eq. (8) (G and DW dropped) → CHECKED. Truncation label (n_T = 1 for absorption, rate order) → CHECKED against the 𝔗 ruling.
- l.35: 2W = 3.2e-3 at 2.25 keV → CHECKED.
- l.41–44: q_BZ = 1.1393 Å⁻¹ = 2.249 keV; ΓL = 1.977 and ΓX = 2.283 keV; Q_D/q_BZ = n_at^{1/3} → CHECKED.
- l.48–54 (11.1-Sac): q(q̂·ê)A_cell/√M_cell, the prefactor π q A²/(Ω M_cell c), ÷ρ_T → π q/m_u² → CHECKED. Dimensions OK.
- l.59–63: CD2020 Eq. (10) and the "drops out" text; CD2022 Eq. (30) with Θ(ω_LO − ω) and Eq. (27) eigenvector → CHECKED against
  the sources. (m_u/m_p)² = 0.9856 → "1.5 %" → CHECKED.
- l.70 caption / l.76: 0.48, 0.34 q_BZ, 26 % low, 0.20 MeV (0.48 q_BZ/2v_max = 0.204) → CHECKED. The dotted (dispersion-only)
  curve overshoots (1.145 vs 1.108 at q_BZ/2), so "pull the other way" is CHECKED.
- l.80–90 (11.1-rate): η/2q from the angular delta; collecting 4π·π·π/(2(2π)³) = 1/4 (sympy) → CHECKED. Dimensions: rate per mass
  dimensionless in natural units → CHECKED.
- l.92–97 edge: v_max/4c = 21.2; threshold mass 0.285 keV; 6.12 keV at c_LA,max = 9.351 → CHECKED. Griffin Eq. (36) "20 keV
  (ω/meV)(1e-5/c)" → CHECKED against the source.
- l.104 caption: edges 6.1/10.2/3.1 keV, m_hi 0.42/0.41/0.65 MeV → CHECKED (phon11).
- l.110–118 light mediator: q₀⁴/(2m)∫η/u², the limit q₀⁴cη/ω_th, (11.1-light) → CHECKED; (c/v₀)² ≈ 1.4e-3 → CHECKED; m⁻³ → CHECKED.
  Griffin Eq. (35) and the "drops out" text after it; their σ̄_n at q₀ = m v₀ (Eq. (2)) → (m v₀/q₀)⁴ → CHECKED.
- l.121–131 (11.1-kappa)/(11.1-correction): first-order expansion redone → CHECKED; 0.985 → CHECKED (0.9851). The rate-weighted
  edge speed ⟨Σw/c⟩⁻¹ holds with v_max − c treated as constant (1 % effect) → CHECKED as an approximation.
- l.138 caption: "the curve changes by 2 % at m = 10 m_min between 3 and 18 km/s" → WRONG: limit11_1b prints 0.6329/0.6251/0.6128
  at c = 3/9/18 km/s, a 3.2 % span (+1.2/−2.0 % about 9 km/s). Correction: "by 3 % between 3 and 18 km/s".
- l.145 WE 11.2: 33–100 eV; tail above 270 km/s (c + u₋ = 9 + 261 km/s) → CHECKED; the remaining numbers are in A.
- l.150–155 heavy mediator: 8m³u²du, (11.1-heavy), I₀ = 5.32e-7 → CHECKED; 8.956/5.313 = 1.686 and 8.956/18.16 = 0.493 → CHECKED;
  rates at 0.3 MeV give 1.732 and 0.460 (P.rate_per_mass, re-run) → CHECKED; 654 /kg/yr, 45 keV (×7.1), 0.935, 0.872 → CHECKED.
  Griffin Eq. (37) R ∝ σ_n/c_s → CHECKED.
- l.164: Griffin App. A3 (a 20 × 20 grid on a sphere of q ≈ 10 eV) → CHECKED.
- l.169 WE 11.1: 165.6/194.25/203.80 GPa, 8.430/9.131/9.352 km/s; Δ_C = −57.3; ⟨s_Q⟩ = 1/5; 188.52 GPa → 8.995 km/s = Voigt v_L →
  CHECKED. The first-order eigenvalue is exact on [110] and [111] → CHECKED.
- l.171–175: 9.019/9.017/9.017; 9.011; 8.956; Ge 5.362, C 18.196; ρ = 5.343 and 3.516 g/cm³; Haxhijaj Table III tensors (131/49/68,
  1081/125/579) → CHECKED. "between the extremes 8.44 and 9.35" → WRONG (minor): the [100] value printed four lines up is 8.430
  (exact); 8.439 is the coarse-grid minimum. Use 8.43.
- l.177: Griffin Table I 2.84/1.61/5.98 → −5.6/−10.0/−1.5 % → CHECKED (source and we11). The PBE value 8.83 km/s → CHECKED
  (limit11_1a: ⟨c_LA⟩ = 8.828).
- l.180: A_Z 1.56/1.66/1.21 → CHECKED; the isotropic + Δ_C·diag(q̂ᵢ²) Christoffel decomposition → CHECKED; the transverse weight
  Δ_C²p_Q/(C₁₂ + C₄₄)² and the 2nd-order eigenvalue C₁₁ − 2Δ_C s_Q + Δ_C²p_Q/(C₁₂ + C₄₄) checked numerically at small Δ_C (agree to
  O(Δ_C³)) → CHECKED.
- l.187 caption / l.190 / l.193: 1.0067/1.0092/1.0021, 0.50–1.70, 1.098 at A_Z = 4, Jensen gap 0.07 %, −0.40, c_LA,max/c̄ = 1.037 →
  CHECKED (limit11_1c re-run).
- l.200: B = 97.8/76.3/443.7 GPa; floors 6.48/3.78/11.23; 23/24/36 % → CHECKED.
- l.202–210 (11.1-thetaD): G_V = 68.04, G_R = 64.88; v_L = 8.945, v_T = 5.341, v_m = 5.912; Θ_D = 648 (655/641), exact 645; Ge 375/373;
  C 2248/2246; 0.5/0.3/1.2 %; 512 K → CHECKED. Kurinsky Table I (2220/645/374 K, c_s 13360/5880/3550) and Griffin 2021 Table I and
  T_D = πc_s(6ρ/π)^{1/3} (text after Eq. (B8)) = (6π²n)^{1/3}c_s → CHECKED.

## C. s11-2 (Optical phonons in polar crystals)
- l.3: Z*/ε∞ = 0.194 → CHECKED.
- l.9–22 (11.2-eps)→(11.2-SM): Sherman–Morrison step, b = e p/(Ωε∞)^{1/2}, Im of the pole = π(b·e)²δ/2ω_ν, and the line formula
  πe²/(2Ωε∞²)Σ(p·e)²/ω_ν δ → CHECKED.
- l.29 (11.2-SZZ): ×2q²/e² → (2π/Ω)|…|²/(2ω ε∞²) → CHECKED. e² = 4πα (HL) is consistent with NOTATION row 15 and with LO–TO.
- l.36: Trickle Eq. (105) "setting ε → ε∞" and Eq. (106) → CHECKED; Griffin 2018 Eq. (19) (phase-convention footnote) → CHECKED.
- l.38: (1/1.26)² → 37 % low → CHECKED. l.40: (ω_L/E_g)² = 5.7e-4; 2W = 7.7e-8 at 13.7 eV; ω_L/T = 4.2e4 → CHECKED.
- l.47 caption / l.53: 88 eV = 0.04·2π/a; optical within 1.3e-4 at 88 eV and 0.4 % at 446 eV; LO dispersed by 0.3 meV; acoustic
  0.9–1.1 % at 88 eV, 5.3 % at 446 eV along [111], 0 along [100] → CHECKED (limit11_2a.log).
- l.59–69 (11.2-rate): ∫q dq/(4π²v)·πσq₀⁴/(μ²q⁴)·2q²/e² → σq₀⁴/(2πμ²e²)∫L K → CHECKED; dimensions OK. Edge 2ω/v_max² = 10.35 keV
  → CHECKED; the single-speed K_η = ln(q₊/q₋)/v → CHECKED.
- l.71: 0.2·2π/a ↔ m = 83 keV → CHECKED (fig11_2.log 82.98). "The optical phonons alone would keep the one-branch form within 1 % up
  to 370 keV" → GAP: in no log (fig11_2.log gives the heavy full/one-branch ratio only at 99 keV, 1.0011, and at 1 MeV, 0.376).
  Add the printout or drop the number.
- l.76 caption: "ω_L = 36.34 meV" next to "measured ε∞ = 10.88" → WRONG (minor): fig11_2.py uses the DFPT 36.342 meV (measured is
  36.35, the value in l.3 and WE 11.ipol). Write "ω_L = 36.34 meV (DFPT)". Coincidence to 3e-4 → CHECKED (1.0002–1.0003).
- l.80: "peaks near 32 keV at about 850 events" → GAP: fig11_2.log has only 835.8 at 28.9 keV; plausible but unlogged. "4 % lower
  at 1 MeV" → CHECKED (0.963). "The acoustic branches … add less than 1 % below 100 keV" → WRONG: fig11_2.log gives
  acoustic/optical = 0.026 at 10.6 keV (near the edge), 0.004 at 14–20 keV and 0.0104 at 99 keV. Correction: "add at most 3 %,
  near the edge, and about 1 % at 100 keV".
- l.84–89 (11.2-onebranch): Im[−1/ε] at the pole, (πω_L/2)ε∞⁻¹(1 − ω_T²/ω_L²); the eigenvector sum Z*q/√μ_red; both forms equal via
  ω_L² − ω_T² = e²Z*²/(Ωμε∞) → CHECKED (we11_3.log 1.6539e-2 vs 1.6547e-2). |Ṽ|²S = 2πδ e'²(ω_L/2)Δ/q² → CHECKED; Griffin 2018
  Eqs. (21), (22) → CHECKED.
- l.92 (11.2-Gamma): redone from (11.2-rate) for one speed → σq₀⁴ω_LΔ/(4μ²e²v)·ln → CHECKED; equals Griffin 2018 Eq. (24)
  |e'|²ω_L/(4πv)(…) with e'² = πσq₀⁴/(μ²e²); Knapen Eq. (8), σ̄_e = 4μ²κ²g²α/(αm_e)⁴, gives the same relation → CHECKED.
  Threshold limit (log → 0 at m v² = 2ω_L) → CHECKED.
- l.98–103 (11.2-kk): KK at ω = 0, (2/π)∫L/ω = 1 − 1/ε; w^pol_ν from the line formula, Σw = Δ → CHECKED.
- l.106–111 (11.2-Ipol): the bracket inequality is correct (the top ratio ω_L,max/ω_T,max ≤ ∏ratios = (ε₀/ε∞)^{1/2}, with pairing by
  interlacing) → CHECKED.
- l.133 sapphire: weights 0.9518/0.0041/0.0413/0.0027, Δ = 0.2103, I_pol = 36.30 meV, ω̄ = 109.9, 9.12 meV cm³/g, γ_L = 16 cm⁻¹ →
  1.8 % → CHECKED (limit11_2b.log; Griffin 2018 Table II o-ray in cm⁻¹ → 112.40/78.05/59.72/48.06 and 78.56/70.55/54.44/47.73 meV;
  Table I ε∞ = 3.2, ρ = 3.98). "close to the top of the bracket (11.2-Ipol), [15.9, 37.1] meV" → WRONG: (11.2-Ipol)'s upper end
  is (π/2)Δ ω_T,max(ε₀/ε∞)^{1/2} = 45.4 meV (limit11_2b.log); 37.1 is (π/2)Δ ω_L,max, a different (tighter) bracket that needs
  ω_L,max. Correction: "[15.9, 45.4] meV" (36.3 is then about 70 % of the way up); or quote both and say which one needs ω_L,max.
- l.127 caption, l.133: 2.1× at 40 keV; within 7 % above 64 keV (1.066 at 65 keV); edges 13.7–32.0 keV; one-branch worse at every
  mass → CHECKED.
- l.137 (11.2-static) → CHECKED (ε(0) of 5.5-eps). l.147 caption: 6.58/8.90; l.153: 2.7 %, 0.484/0.443 at 70.5/54.4 meV, 78.6 within
  0.5 meV of 78.05 → CHECKED.
- l.159–166 (11.2-Zeps) and the error budget: dln = −½δε/ε + (ω_Lδω_L − ω_Tδω_T)/(ω_L² − ω_T²) → CHECKED; 6.92; 0.91 %; 1.04 % →
  CHECKED. 0.194 → CHECKED (0.1938).
- l.173 caption / l.176 / l.179: r = +1.43 %; 2.21 vs 2.11 (+4.8 %); amplification 3.46; |r| < 0.29 %; splitting 8.1 %; LiF 2.30
  and 0.62 → CHECKED. Griffin 2018 (B11), (B14), (B15) → CHECKED.
- l.184–194 WE: ρ_T = 5.361; μ = 36.11 u; 0.01439; 0.822 meV/0.153; 0.759/0.1415; 8 % = 1.4 % × 5.39; Table I 2.27/10.9/34.9 →
  0.1702 (+20 %, Z* 7.6 %); LiF M = 25.94, μ = 5.084 → 18.99, ×111.6; factors 29.1/39.6/0.214/0.452; edges 10.35/21.98 → CHECKED
  (we11_3.log, own arithmetic, source Table I).
- l.197: 0.77, 103, 46, 17, 2.6, GaAs ahead at 25 keV (0.39), crossing 26.7 keV → CHECKED.
- l.199: CsI 6.9–10.0 meV (Table I) → edge 2.85 keV → CHECKED.

## D. s11-3 and D-31 (multiphonon response)
- s11-3 l.3: 0.42–26 MeV window → CHECKED.
- l.10 (11.3-exact) / D.31 l.135–140: pair sum, factor N, 1/Ω → CHECKED.
- l.21 (11.3-Sn) / D.31 l.146–158: (D.31-Cs) after Q → −Q in the absorption term; momentum sum NΣ_Gδ; prefactor (1/Ω)(1/n!)N^{−n}·N
  → N^{−(n−1)}; the |Σ_κ…|² rearrangement with (y^s)* = q·e^s → CHECKED (term by term).
- l.28: CD2020 Eq. (12) contact term, the per-cell normalization, s₁,₂ ↔ 1/n! → CHECKED against the source.
- l.32: variance of A 0.1587, 2.01e-4 of 790.1 → CHECKED (IUPAC 92.223/4.685/3.092). CD2022 Eq. (11) (variance) → CHECKED.
- l.40 (11.3-inc): CD2022 Eqs. (15), (36) with D_d ↔ g_ph,κ/3 → CHECKED; Kahn 2021 Eq. (10) with q₀² = 2Mω₀ ↔ 2W = q²/2Mω₀ →
  CHECKED.
- l.45–48 (11.3-fsum) / D.31 l.162–170: ∫ωS = (2π/Ω) i f'(0); Σ_s(n + ½(1+s))(−is)/2ω = −i/2 (sympy); completeness → δδ/(2M); self
  term n(2W)^{n−1}/n!·E_R → CHECKED.
- l.50: 2W(50 keV) = 1.573; the energy share of n ≥ 3 is 0.466 → CHECKED.
- l.55–63 WE 11.tail: 166.8 meV; 63.67 meV; P₃…P₆ fractions 1.4/11/35/62 %; 2W 0.063/0.566/1.573; E_R 1.91/17.2/47.8 meV;
  probabilities 6.1e-7, 6.2e-4 (0.38:0.43:0.16), 1.7e-2; bounds 4.0e-5 (65×), 2.0e-2, 0.21; 93.4 keV; 17.6 MeV; 53 keV; Einstein
  8e-11/2.8e-5/5.6e-3 → 7400/22/3 → CHECKED (we11_4.log + own arithmetic).
- l.66 / D.31 l.174–181: j_BZ(bond) = 3j₁(2.679)/2.679 = 0.444; four bonds 1.775; the Legendre identity ½∫e^{−ixμ}P_l = (−i)^l j_l →
  CHECKED. The asymptotic statement (linear term vanishes for the self terms only) → CHECKED.
- l.73 caption, l.76, l.79: 2.95 q_BZ = 6.63 keV; 7.85 q_BZ = 17.6 keV; q → 0: +0.355 (nn +0.21); δ₂ −0.079/+0.014/−0.018/−0.025;
  δ₃ −0.027/+0.016/−0.006/−0.012; coefficient 0.443 → CHECKED (limit11_3a.log). "Above q_BZ [the nn pairs] follow the full curve
  within one percent of the weight" → WRONG (minor): at q_BZ itself δ₂ = −0.109 against nn −0.085 (2.4 %). It holds from about
  2 q_BZ (0.8 % at 4.5 keV). Correction: "above about 2 q_BZ".
- l.81 / fig caption l.86: 0.058 (0.0579), 1.84e-3 (1.86e-3), 4.0e-5; Poisson 0.059/1.9e-3; e^{−2W} = 0.939; within 17 % at 22–120 meV
  (0.856–1.170); about one half at the edges (0.563); 2.69× → CHECKED (fig11_3.log).
- l.94 (11.3-Bkk), l.101 (11.3-weight) / D.31 l.185: setting t = 0, Ω∫dω/2π → f(0) → CHECKED. NOTATION 2W_κ = q·B_κ·q is consistent
  with B_κκ(0) = B_κ.
- l.106 / D.31 l.187: FTs ∫d³Q e^{iQr}/Q = 4π/r² and /Q² → 2π²/r; B ~ Ω/(4π²M_cell c r²); convergence for n ≥ 2 at T = 0 and linear
  divergence at n = 2 for T > 0 → CHECKED.
- l.108: ⟨u_x²⟩ = 2.4499e-3 Å²; tail < 2e-3 beyond 30 Å (1.8e-3) → CHECKED. "Largest off-site element 5.1e-4 Å²" → GAP: not
  printed by limit11_3a (only the coefficient 0.443, i.e. a longitudinal projection of 1.09e-3 Å²). Print it, or say which element.
  CD2022 Sect. III C order-of-magnitude statement → CHECKED (the comparison itself is in III B; III C opens with the conclusion).
- l.113 (11.3-band) / D.31 l.191–195: Cauchy–Schwarz term by term; the p-average turns the constraint into 1/N and factorizes into
  (2W)^nP_n → CHECKED. The zone average holds the vertex at q, as stated.
- l.130 (11.3-tds) / D.31 l.199–215: coth x ≤ 1/x + x/3 → (2n+1)/2ω ≤ T/ω² + 1/12T; ∫d³Q/(Q²|k−Q|²) = π³/k (sympy, and the log's
  31.04 numerical check); collection (Ω/2)(2π)⁻³π³ = Ω/16 → CHECKED. Dimensions: Ω T² q⁴/(M² c⁴ k) is dimensionless → CHECKED.
- l.133: c_min = √((C₁₁−C₁₂)/2ρ) = 4.67 km/s, TA[110]⟨1̄10⟩ → CHECKED; J/π³ = 0.460 → CHECKED; n_T = 2, cross terms n_T = 1 with a
  log singularity → CHECKED.
- l.140 caption, l.146: 0.13 q_BZ (293 K), 0.065 q_BZ (77 K), 48.4 meV (Hill c_T = 5.34; with c_min = 4.67 it would be 55 meV),
  2e-5 q_BZ, T² ratio 1.2e-9, 1.07 → CHECKED (limit11_3b.log). For consistency with l.133 say "T/c_T with the Hill c_T".

## E. s11-4 and D-32 (impulse limit)
- l.3: 106 keV; E_R = 191.1 meV (3.0× 63.7); 2W = 6.29; σ = 88 meV → CHECKED. l.7: 44× q_BZ → CHECKED.
- l.9–15 / D.32 l.222–239: H_q = H + D; the moment rule i^k I^{(k)}(0); the second derivative D² + [D,H]; ⟨[D,H]⟩ = 0; σ² = q²⟨p_q̂²⟩/M²
  = 4E_R E^kin → CHECKED (expanded by hand and the commutator algebra checked).
- l.23 / D.32 l.239–243: T = 0 third moment ⟨D³⟩ + ⟨DAD⟩, ⟨DAD⟩ = ½⟨[D,[A,D]]⟩ = (q²/2M²)⟨∂²V⟩; cumulant κ₃ = c → CHECKED. The 1/q
  scaling of the skewness → CHECKED.
- l.25: ⟨ω⟩/σ_ω = x_R^{−1/2} at T = 0 → CHECKED.
- l.29 / D.32 l.258–266: ⟨p p⟩ with coth; E^kin = ¼⟨ω coth⟩ → ⟨ω⟩/4; classical limit T/2 → CHECKED.
- l.33 (11.4-IAgauss), l.37 / D.32 (D.32-ck): cumulants from the exponent, odd E_R⟨ω^{k−1}⟩ and even with coth (derived) → CHECKED;
  skewness (⟨ω²⟩/⟨ω⟩²)x_R^{−1/2}; mode shift ≈ γσ/2 → CHECKED. CD2022 Eqs. (37)–(39), Δ_d² = q²ω̄_d/2m_d → CHECKED; Kahn 2021
  Eq. (4) q(ω₀/2m_N)^{1/2} → CHECKED. D.32 l.271 on-site force constant M⟨ω²⟩ → c₃ = E_R⟨ω²⟩ → CHECKED.
- l.39: ⟨ω⟩ = 40.90, 1.194, 10.23 meV, 237.3 K, +2.3 % (77 K), +55.7 % (300 K), width ×1.248 → CHECKED (imp11.log).
- l.41 / l.46 caption: x_R 1.17/4.67/18.69/74.76; maxima 0.36/0.805/0.968/0.992; 0.208 zero-phonon; deviations 0.19/0.069/0.033 →
  CHECKED (fig11_4.log).
- l.53–61 WE 11.width: M = 26.162 GeV; 191.1 meV; 4.672; 10.23; 88.4 meV; 0.463; 265 m/s; 1.146 km/s; FWHM 208 (Gaussian) and 207
  (full, 1.082 E_R); skewness 0.551 → 24 meV; peak 154 meV (37 below); 110 meV at 300 K; Ge 73.9 meV, 3.1, 0.57, 2.59× heavier →
  CHECKED. "rms width 88.1 meV; 68.4 % within E_R ± σ_ω" → GAP: not in fig11_4.log. Add the printout.
- l.68–75 (11.4-LS) / D.32 l.275–280: ∫d³q/(2π)³δ → q dq/(4π²v)Θ; the ω-integral; v_min = q/2μ_χN; σ_N = σ_pA²μ_N²/μ_p² → CHECKED.
  Dimensions (per mass per energy) → CHECKED. CD2022 Eq. (42), Kahn–Lin Eqs. (90)–(92), Lin TASI Eq. (104) → CHECKED in structure.
- l.78 / l.87 caption: x_R ≥ 2.3 (2.28), 93 meV, 70 keV; 2 % from 4.3 (4.29) → CHECKED (limit11_4a.log). CD2022 Sect. III D "free form
  works where the Gaussian is not narrow" → CHECKED against the source.
- l.80: 50 MeV endpoint 1.337 eV, x_R = 32.7; 5–21 % (crystal/free 0.826–0.949); x_R = 14.3 at 4.86σ; Gaussian within 5 % from 3.55
  (1 GeV) and 3.78 (50 MeV) → CHECKED. Citation "Kahn, Krnjaic and Mandava … [text after Eq. (12)]" for the reach extension →
  WRONG pointer: the text after their Eq. (12) says the matching justifies free elastic kinematics; the reach-extension statement is
  in the text after their Eq. (4) ("This observation extends the reach of solid-state nuclear recoil detectors to sub-GeV DM…").
  Correction: [text after Eq. (4)].
- l.93: 92.5 keV, 164 meV, x_R = 9 at 139 keV/0.37 eV; CD2022 "use (39) for q > 2√(2m_dω̄_d)" → CHECKED; the Ge chain → see A.
- l.104 (11.4-ferm-nuc): → see A. The wording "per unit volume of a target of free nuclei" → WRONG (minor): Γ_V = σ_F𝓃_N A²F² has
  dimension eV. It is the absorption rate per dark-matter particle in a target of nucleus density 𝓃_N (NOTATION 842: rates in eV),
  consistent with the event rate (ρ_χ/m_χρ_T)Γ_V. Correction: "per dark-matter particle, in a target of free nuclei".
- l.109: Dror Eqs. (1), (3), (4), σ_NC = m²/4πΛ⁴, Helm at q = m, ρ_χ ≃ 0.4 → CHECKED against the source; 3 GeV, 256 MeV, proton
  ≈ 10 % at 100 MeV → CHECKED.
- l.111 / D.32 l.290: zero-phonon absorption needs |G| = m within O(v); the n ≥ 1 weight 1 − e^{−2W}; "mostly one phonon below 20 keV"
  (0.88 of the inelastic weight at 20 keV) → CHECKED.
- l.113: 46.3 keV/m; 4.6 %/0.46 %; 379 km/s → 1.46e-3; 32 MeV; Dror "ΔE_R/E_R ∼ 1e-3 from higher-order corrections to Eq. (2)" →
  CHECKED.
- l.120 caption / l.123: 61 keV–3.0 GeV; overcount e^{−2W}/(1 − e^{−2W}) → CHECKED.

## F. Convention / NOTATION drift (factor-2, π, sign: none found in 11.1–11.4, D.31, D.32)
- No factor-of-2, π or sign drift: S normalization (4.2-Sab) vs per-cell sources (Ω/2π), e² = 4πα, 2W = q·B·q, η/2q, σ_F and the
  rate-order 𝔗 labels all agree with NOTATION and the cited equations.
- ω̄ (s11-2) → ω̄_pol (see A). κ_η row (see A).
- 𝔫_κ(p) (11.4, D.32: nuclear momentum distribution) clashes with NOTATION row 923, where 𝔫₁, 𝔫₂ is a fraktur n already used for
  interface-weighted phonon densities. Rename it, e.g. to n^p_κ or 𝔣_κ, and register it.
- The letter c is overloaded inside 11.3–11.4: c_κ (species coupling), c_k and c₃ (cumulants, 11.4/D.32), c_ν and c_min (sound
  speeds). c_k next to c_κ in one section is a legibility hazard; rename the cumulants (e.g. 𝔠_k) or the
  coupling. D (kick operator, 11.4/D.32) shadows D^an/D^dyn of 11.2; acceptable with the superscripts, but register it.
- Unregistered symbols introduced in these files (NOTATION has no rows): 𝔚^(n), 𝔚^(n)_inc, 𝔓^(n), δ^coh_n, j_BZ, B_κκ'(ΔR),
  E^kin_κ, σ_ω, c_k/c₃, 𝔫_κ, q_abs, I₀, K_η, w^pol_ν, ω̄_pol, A_cell, A_Z, Δ_C, p_Q, c_min, S_A, c_κ. Add the rows at the
  Ch11 NOTATION pass.
- O_A(q) = Σ_κ A_κ n_κ(q) (s11-1 l.9) CLASHES with NOTATION row 637 (O_A = Nambu bilinear, 7.2/D.21). Rename it (e.g. O_N).
- c_κ (species coupling, s11-3 l.7) is now taken, but the partII notes say "12.6 must introduce c_κ": either 12.6 uses another
  symbol or 11.3 writes the c₁^{(κ)} of 8.4 that it cites.
- Γ typography: \varGamma for the rates (11.2 l.92, 11.4 l.104) and \mathrm{\Gamma} for the zone center → CHECKED (STYLE 2026-11-02).

## G. Process notes
- limit11_1a/b/c write no .log; their printed numbers were reproduced here by re-running with savefig disabled. Add a .log, as for the
  other scripts.
- Shared folder: at the end I ran `find sources/review-ch11 -name "*.pdf" -o -name "*.txt" -delete` over the whole folder.
  It also covered the subfolders of a concurrent reviewer (1409.4945, 1508.01798, 1809.02863, 2308.06314, 2309.10839, 2409.02439,
  2411.03433, 2411.10542, 2501.05504, 2607.06005). Any PDF or .txt they still needed is gone; the .html and .fetch.log files remain.
- 11.8 items in editor-notes (rigid-ion GaAs 8.2×, resonator 1.8×, s11-8 duplicate paragraph) are outside this batch (s11-5…9).
