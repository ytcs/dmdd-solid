# Ch18 part 1: derivation check (ch18.tex, s18-1, s18-2, s18-3, D-43, D-44)
Verifier: derivation (isolated). 2026-11-06. No tex edited, nothing committed, no QE run.

**Method.** Algebra: sympy (θ_ii, Dirichlet integral, WE 18.1 toy, Shockley population, D.44 check, parking ODE).
Parking constants: mpmath at 30 digits. Cascade numbers: my own solver, written from scratch
(scratchpad `rev18/mycasc.py`, `pgf.py`). It uses cell-mass densities of states, a commensurate ω_AB
(N = 92, 184, 313, 626 steps per E_g; no ω interpolation), moment recursions for N, E_<, E_>, E_heat and the
PGF at 32 roots of unity. Two cross-checks: a separate 40 000-event Monte Carlo, and the book's mom18_2 solver
rerun on finer grids. Seeds come from the cached figscripts/ch18/seeds18_3.json.
Sources checked against arXiv HTML: 2004.10709 (RK), 0911.1532 (SL), 0812.2923 (Kotani–vS), 2004.11499
(Rodrigues), 1509.01598 (Essig). The PDFs in sources/review-ch18/ were deleted.

## Summary of findings
| # | location | verdict | correction |
|---|---|---|---|
| W1 | s18-3 l.80, l.87 | WRONG | b_N(uniform split) = **0.008**, not 0.015; one-sided b_N = **0.345**, not 0.352. The casc18_3 "constant offset" subtracts ω/3.749 eV, while that grid at A = 5.6737 has ε = 3.7467 eV (bias +0.0077 at 40–44 E_g). Write "b_N between 0.008 and 0.35". This settles the editor-note item 0.345 vs 0.352: 0.345 (fit, h = 1/74: 0.3453; my continuum: 0.3452–0.3457). |
| W2 | s18-3 l.99 (lim:18.3a, after the box) | WRONG | "the Beta splits span distances up to 0.39" holds only for α_RK = 1 and α_RK → ∞ (0.208, 0.392). The α_RK → 0 split reaches **0.674 at 5.37 eV**. Write "the splits with α_RK = 1 and ∞ reach 0.21 and 0.39, the one-sided split 0.67". |
| W3 | s18-1 l.152 | WRONG (statistical) | All-to-electron, A = 5.2, E_g = 1.17 eV: the printed 3.029 ± 0.004 is a 2.8σ Monte Carlo fluctuation. Deterministic PGF (grid-independent to 4 digits for N = 130–520) gives **3.018**, P(2) = **0.133**; my 40 000-event MC gives 3.018 ± 0.003, P(2) 0.135. Moot after the ruling rerun (3.005, see G6). |
| W4 | s18-1 l.139 | WRONG | "A_AB = 5.2 is chosen to reproduce the measured pair energy": in this model at E_g = 1.17 eV, A = 5.2 gives ε_eh = **3.725 eV** (my solver; RK Eq. (12) gives 3.726), not 3.749. RK fix 5.2 against the **300 K** pair energies (Sect. IV A: "in agreement with Table I at 300 K"). Reword: "chosen in the source to reproduce the room-temperature pair energy". |
| W5 | NOTATION l.1409 (A_AB) | WRONG (drift) | The unit column says eV²; 18.1 l.139, 18.2–18.3 (5.674 eV³) and E.13 l.69 all use eV³ correctly. Change the row to eV³, noting that the source prints "eV²". |
| W6 | s18-2 l.49 | WRONG (wording) | "Just above threshold the probability that the next collision ionizes is a few percent": p_ii = 2×10⁻⁴ at 1.5 eV, 0.0041 at 2 eV, 0.0185 at 2.5, 0.049 at 3 eV. A few percent holds only 1.3–1.8 eV above threshold, and within a few phonons of threshold p_ii < 10⁻⁴. Write "a few percent at 2.5–3 eV and far less below". |
| W7 | s18-3 l.87 | WRONG (minor) | At 20.2 eV, σ_N = (F_eh ω/ε_eh)^{1/2} = **0.78**. The printed 0.79 is the s.d. of the computed distribution (0.794). Quote 0.79 as computed, or 0.78 from the formula. |
| W8 | s18-2 l.160 | WRONG (minor) | "change by 1.3×10⁻⁴ (in F) and 4×10⁻⁵ (in ε)": these are **relative** changes (absolute ΔF = 1.5×10⁻⁵, Δε = 1.4×10⁻⁴ E_g). Insert "relative". |
| G1 | s18-1 l.69 (LO double count) | GAP | The three matching conditions are correct, but one condition is missing. The **ionic part of the dielectric matrix in W^scr must be restricted to the same model as g^L** (its macroscopic dipole/quadrupole head with the same cutoff). A full ionic ε_GG′ (DFPT, all G) also contains the short-range coupling, which would then be counted twice against g^S. That includes silicon: Z* = 0 removes only the dipole head, so "does not arise at dipole order" is true only for a dipole-model ionic W. Add one sentence. |
| G2 | D-44 l.126; s18-2 l.149 | GAP | With the hole DOS cut at B_h (the model actually solved), Φ_e(y) = (π/8)∫₀^{B_h}(y−x₃)²√x₃ dx₃ ∝ y² for y ≫ B_h. The phonon/ionization ratio then falls as **x^{−3/2}**, not x^{−3}. The hole's share tends to 0, so the limit law is Beta(3/2, 3/2) between the two electrons, not the three-parameter Dirichlet law. κ = 1 still holds (the leaving probability E_g/x dominates) and the proof is unaffected. State the cut-band case. |
| G3 | s18-2 l.30, l.49–53, fig:18-decomp, lim:18.2a | GAP (grid) | The printed last digits are production-grid values (h = E_g/74, ω interpolated over n_w = 3, 4, 5). The book's own mom18_2 at N = 184 and 313 and my solver (N up to 626) converge to V_> 0.2891, 2V_<> −0.2670 and phonon heat 0.793 E_g = **0.920 eV** at A = 5.674, with ε = 3.7467 eV (−0.06 %). Recalibrated in the continuum: **A_AB = 5.703 eV³**, terms **0.092 + 0.290 − 0.268 = 0.114**, phonon heat 0.923 eV, "1 % in V_> → 2.5 %" (not 2.6). F_eh, V_<, 6.7×, 92 % and b_N are stable. At λ_AB = 0.003, V_> = 0.0091, not 0.0097 ("0.010" → "0.009"). Either label these values "on the solver grid" or print the continuum values. This is the same pattern as REF-DC-67 (5.588 → 5.616). |
| G4 | limit18_2c.py l.70; fig:18-limit-renewal caption | GAP | The Ge marker (0.125) is run **without the hole band cut** (W not passed), while Si uses 12 eV. The caption does not say so. Either state it or rerun with the Ge valence width. |
| G5 | s18-1 l.139, l.141; fig:18-tree caption | GAP (attribution) | RK neither cut the hole DOS nor reject draws. They cap E_h at W and **re-split the excess among the other carriers** (Sect. IV A, step 5), and the seed carries the constraint E_h < W (step 1). The book's rejection/DOS cut is a variant of RK, so say so. |
| G6 | ruling "one parameter set" (editor notes 18.3) | GAP (effect sizes) | Computed (deterministic) for 5.2/1.17 → 5.674/1.160. 10 eV seeds: equal −0.011, uniform −0.015, all-to-one −0.014, so "< 0.03" holds. **But for the 50 eV electron**, new pairs go 13.08 → 13.00 (MC printed 13.06), heat 34.7 → 34.9 eV and var/mean 0.118 → 0.119. The p_ii = ½ crossing moves 5.76 → **5.88 eV** (l.123 "5.8" → "5.9"). Also change ch18.tex l.2 "1.17 eV gap" → 1.160, and the fig:18-tree caption. |
| G7 | s18-1 l.22 | GAP | "makes about 13 new pairs … remaining 35 eV" is a model number: label it as in the fig caption (editor note). |
| G8 | s18-1 l.56 | GAP (minor) | we:4-siplasmon gives ε₂ = 0.224 **at the zero of ε₁ (16.3 eV)**, not at the loss peak (16.4 eV). Write "at the plasmon (the zero of ε₁)". |
| G9 | NOTATION vs s18-1..3, D-43/44 | GAP (drift) | No rows exist for λ_AB, w_AB, B_h, b_N, c_N, E_heat, E_<, E_>, σ_pair, F_ren, F_park, 𝔓_t, 𝒦_c, δN_c, x_th, N_sub. In D.44, **κ** (condition 1) clashes with NOTATION entry 12 (κ is the species index only; rename it, e.g. ϰ or η_c), and **x_c** clashes with 2.4's cut-off. D.43's s_t(x) (second moment) and the PGF variable s sit side by side: rename s_t → M_t. |
| G10 | s18-2 l.138 | GAP (citation) | SL Sect. IV: the uncorrelated model is a lower bound "for intermediate coverage ρ ≤ 0.7 and near the jamming state". At small ρ all models coincide (F ≈ 1 − 2ρ), and SL identify a negative contribution (L ≈ 3 lots, δF₃ ≈ −0.0021) that the positive terms outweigh. Replace "at every stage of the filling" with "at intermediate filling and at jamming". |
| G11 | s18-3 l.74 | GAP (citation) | RK do not show that the plasmon channel "changes no yield". They report no significant feature at the plasmon energy in any model, and that the hole band width, rather than plasmons, has a visible impact (abstract, Sect. IV). Soften. |

## PRIORITY items (editor notes ch18 + partII), verdicts
- **eq:18.1-ii, impact-ionization kernel — CHECKED.** NOTATION has S = (2π/𝓥)Σ…, W^scr = v_C + v_C R v_C and L = Im[−(ε⁻¹)₀₀].
  The matrix FDT S = −2(1+n_B)(R−R†)/2i gives ρ*v[(R−R†)/2i]vρ = ρ*[(W−W†)/2i]ρ, and v_C drops out (real diagonal).
  The diagonal limit gives 2v_C|ρ|²L·(1−f)(1+n_B), the eq:4.8-lifetime form via 2L/v_C = (1−e^{−βω})S.
  It is the standard −2ImΣ_out (Quinn–Ferrell). Dimensions: ∫d³p [eV³] × W [eV⁻²] = eV.
  The anti-Hermitian part equals the elementwise Im only for a symmetric W. Inversion with time reversal makes R_GG′ = R_G′G, so W is symmetric (ε⁻¹ itself is not): CHECKED.
  −2ImΣ^R = Γ_out + Γ_in, with in-scattering ∝ f n_B (consistent with s4-8 l.147). Γ_qp = −2z ImΣ (eq:4.7-qp).
  Kotani–vS Sect. II: "Typically Z ∼ 0.8", Eq. (5) is the Kane formula, Fig. 2 shows the scatter, and the exchange (M_E) is absent from the GW form: CHECKED.
- **θ_ii = (2m_e+m_h)/(m_e+m_h) — CHECKED** (sympy; minimum relative KE at common velocity; equal masses 3/2; the hole case swaps the masses).
- **LO double-count conditions — CHECKED with G1.** g^L = iC_Fρ/Q matches eq:6.2-frohlich (C_F² ∝ 1/ε∞ − 1/ε₀).
- **Backward equation (eq:18.1-backward) and D.43 first-step analysis — CHECKED.** Factorization, Kolmogorov
  form, minimal solution (monotone iteration from 0, G^(n) interpretation, the toy 1−p+ps² extinction (1−p)/p),
  and termination bound ω/δ_min all check.
  Moment recursions D.43-mean/second checked by differentiating the product. The law of total covariance
  (eq:D.43-cov) checked by expansion: Σ⟨ZZᵀ + Σ_j C_j⟩ − Γmmᵀ = Γ(M − mmᵀ).
  Energy-only convolutions (2P_t∗ρ_t∗ρ_t̄ + ρ_t∗ρ_t∗P_t̄; P∗P∗ρ + 2P∗ρ∗P) and D.43-m1/m2 checked.
- **Energy identity eq:18.1-energy and 𝔊(λ_N,λ_H) = e^{λ_Hω}𝔊(λ_N−λ_HE_g,0) — CHECKED.**
  Numerically, my solver gives mean identity 4×10⁻¹³, Var N vs Var E_heat 4×10⁻¹¹ and F(pair) = F(heat) to 10⁻⁵ displayed.
- **WE 18.1 toy — CHECKED** (sympy): 𝔊₂ = 19s/25 + 6/25; P(1,2,3) = 36, 228, 361 /625; mean 63/25 = 2.52;
  var 228/625 = 0.3648; 1.984 E_g per pair; var/mean 0.1448. The heat paths (1, ½+½, ½+½+1) all satisfy heat = 2 − N.
- **Seed split 2.997 vs 2.712 (10 eV, A 5.2, E_g 1.17) — CHECKED**: deterministic 2.997 and 2.707 (MC 2.712 ± 0.004, 1.3σ).
  P(2) equal 0.035 (0.036) and uniform 0.347 (0.343). All-to-electron: see W3.
  Calibrated set: 2.986, 2.692, 3.005, var 0.079, f_e = ¼ → 2.437: all reproduced to 4 digits.
- **Two Si parameter sets (18.1 vs 18.2/18.3) — GAP**, see G6, W4. The ruling's "< 0.03" is confirmed for the 10 eV seeds, not for the 50 eV figure.
- **D.43 moments and decomposition — CHECKED** (D.43-moments, D.43-decomp, two checks; 18.2-moments and decomp identical).
- **D.44 renewal theory — CHECKED with G2.** The tagged-unit identity (each ionization weighted 1/x on x units)
  and the uniform propagation of the unit along its line (probability x_i/x, E_g/x, ω/x) check.
  The check example M = 2x−1 checks (sympy: (2/x)∫₁ˣ(2y−1)dy = 2(x−1); size-biased step ∫2v ln v = −½; ⟨S⟩ = 2 − 1/x).
  Hypotheses 1–4 and the visits/coupling/undershoot/limit steps are sound as sketched.
  The non-lattice argument implies μ > 0. The claim "independence of siblings not needed" is correct (linearity of the mean along one line).
- **0911.1532 misprints — CHECKED.** SL Eq. (23) prints ρ∞ = 0.7475987, against the integral **0.74759792025** (30 digits).
  F_unc (unnumbered, after Eq. (26)) printed 0.0439766, correct **0.04439766476**: one "4" is lost.
  SL's own F_nnp = F_unc + 0.007685 = 0.05208 (Eq. (38) and after) requires 0.0443977. SL's "about 14 %" follows from the misprint; the correct figure is 13.0 %.
- **Fano decomposition 0.092 + 0.291 − 0.269 = 0.114 at 1.160 eV — CHECKED to ±0.001**, with grid caveat G3.
  mom18_2 at h = 1/74 reproduces 0.09196, 0.2906, −0.2685, 0.11407. The continuum at calibration gives 0.0922, 0.2898, −0.2678, 0.1142.
  The SPINE/summary values 0.091 + 0.288 − 0.265 are the campaign GAP-EF values at E_g = 1.164 eV (SOTA l.557). They are superseded for the book; use the 1.160 eV values.
- **Step-model overcount 5.9× — CHECKED** (independent PGF: DM P(2) at 5 eV = 0.1699, so 1/0.1699 = 5.89; photon 0.1905, +12 %).
- **TV thresholds 4.37 / 12.95 eV, photon vs DM ≤ 0.062 — CHECKED** (independent PGF on the seeds json, 0.02 eV grid).
  Step model: first > 0.1 at 4.37 eV; equal split last > 0.1 at 12.95, uniform 4.73–7.01; photon max 0.062 at 5.67 eV.
  Step 0.859 at 4.91 eV; values at 21 eV: α→0 0.180, uniform 0.012, equal 0.031, step 0.569.
- **b_N 0.345 vs 0.352 — RESOLVED: 0.345** (W1).
- partII notes concerning these files: a_x = 4.2 nm (s18-1 l.81) agrees with 10.5 (CHECKED). E_e/E_h renaming is applied (CHECKED).
  Upright Γ(a) for Euler's gamma and \varGamma for rates (CHECKED). n_B(ω) always carries its argument (CHECKED). No other partII item touches these files.

## Location-by-location (CHECKED unless flagged above)
**ch18.tex**
- l.2, 10 eV / 1.17 eV ⇒ 8.5, "eight": CHECKED.
- l.2, 3.749 ± 0.001 eV at 123 K (Rodrigues abstract): CHECKED. The 1.17 eV gap: G6.
- l.2, "two or three in nearly every event": CHECKED (P(2)+P(3) = 0.97 equal, 0.95 uniform, 0.85 one-sided).

**s18-1**
- l.27 / l.141, MC log: 13 ionizations, 27 carriers, 199 phonons, heat 34.79, mean 13.06, var/mean 0.116, 3.83 eV/pair, heat 34.7: CHECKED. My PGF/moments give 13.08 and 0.118.
- l.37–52, kernel: CHECKED (above).
- l.58–63, θ_ii: CHECKED.
- l.67, phonon response 2π[(n+1)δ(ω−ω_Q) + nδ(ω+ω_Q)]: CHECKED.
- l.81, Pauli estimate: 1.998×10²³ cm⁻³, 1.66×10²² cm⁻³ eV⁻¹, 267 pairs (1000/3.749), 6.37×10¹⁹ cm⁻³, 3.8×10⁻³: CHECKED.
- l.81, n a_x³ = 4.72 (1 keV) and 0.47 (100 eV): CHECKED.
- l.91, branching ratios ∫𝒦_c/Γ_x as the p_c of eq:C.11-functional: CHECKED.
- l.98, energy identity: CHECKED.
- l.100–111, WE 18.1 toy: CHECKED.
- l.118, iso-energy average: CHECKED (definition).
- l.123: p_ii = ½ at 5.76 eV (A 5.2) → "5.8": CHECKED. After the ruling it becomes 5.88 (G6).
- l.127–137, eq:18.1-phase and the Dirichlet integral: Γ(3/2)³/Γ(9/2) = 2π/105, exponent 3a−1 = 7/2: CHECKED.
- l.132, eq:18.1-randomk with 𝔓 = (2π/105)y^{7/2} is RK Eq. (8) (A·105/2π·(E−ħω)^{1/2}/(E−E_g)^{7/2}): CHECKED. Units eV³: CHECKED.
- l.141, "199 phonons all below 6 eV": CHECKED (log).
- l.147–150, eq:18.1-seed; RK Eq. (5) as its first moment: CHECKED.
- l.152, 8.83 eV, 2.997/3.6 % and 2.712/34 %: CHECKED. 3.029/13 %: W3.
- l.152, hole +0.9 eV for DM vs photon at 10 eV: CHECKED (seeds log, excess 9.25 eV: ⟨E_h⟩ 4.39 vs 3.46).

**s18-2**
- l.3: 5.9 keV/3.749 = 1573.8, √ = 39.67, σ = √(0.119·1573.8) = 13.68 (Rodrigues table: μ 1573.48, σ 13.69): CHECKED.
- l.9–13, eq:18.2-moments: CHECKED. Dimensionless: CHECKED.
- l.16–28, decomposition, additive deposits, two identity checks (2.6×10⁻¹⁵, 4.2×10⁻¹⁵): CHECKED.
- l.30: λ_AB = 5.674/1.16³ = 3.635, w_AB = 0.05431, 3.232 E_g = 3.749 eV, E_g = 1.160 eV (RK Eq. (11): 1.1692 − 4.9×10⁻⁴·123²/778 = 1.1597): CHECKED. A_AB: G3.
- l.32, b_N = 0.35, c_N = −0.02: CHECKED (0.3453; −0.0177).
- lim:18.2a: 14.9 E_g = 17.3 eV (mine 14.89); F(ω) up to 1.50 F_eh (mine 1.503 at 3.7 E_g): CHECKED. Residuals at 10 E_g: 0.07 % / 0.9 % (mine 0.06 % / 0.8 %): CHECKED.
- l.49–53: 0.93 eV (G3: 0.92), 14.7 phonons, Poisson 0.043, ×6.7, 92 %, 0.081 at λ → 0: CHECKED.
- l.49–53: λ 0.003 / 30 terms; F 0.085 → 0.132; 0.105–0.122 for λ 1–10: CHECKED (mine 0.0846, 0.1318, 0.1050, 0.1224). V_> at λ = 0.003: G3.
- l.64–92, WE 18.2: the Laplace step φ′ + 2e^{−s}φ/s = −1/s² and the integrating factor e^{−2E₁} check, as do the small-s limit to ρ∞/s² and ρ∞ = 0.74759792025.
- l.64–92, WE 18.2 (cont.): 1/ρ∞ = 1.3376, ∫G = ρ∞, ∫(1+g)G = 1, ⟨g⟩ = 0.337617 = 1/ρ∞ − 1, Var g = 0.079437, F_ren = 0.0443977 = 0.870 F_park: all CHECKED (mpmath).
- l.64–92, WE 18.2 (cont.): grid extrapolation 0.051040 / 0.747599: CHECKED (log).
- WE 18.2 citations: SL Eqs. (2), (44) for F; (23) for ρ∞ (lim:18.2b cites (2), (23)); (19) for G; (7) for F_unc; Sect. I "test": all CHECKED.
- l.96: 1.338 → 1.585 E_g, 0.051 → 0.081: CHECKED (log).
- lim:18.2b, 0.4 %/0.1 % grid offsets, λ < 0.40, 0.8λ, 3.2 %/3.7 % at 0.1, F = 0.072 = 1.41 F_park at λ = 3: CHECKED (log).
- lim:18.2b, the constant-DOS ratio λ/(x−E_g): CHECKED.
- l.113–118: renewal Var N ≃ σ²ω/ε³ ⇒ F = σ²/ε²: CHECKED.
- l.113–118, Shockley: mean 9/10, var 27/175, ε = 14/5, 54/175 = 0.31 (2.6×), 27/686 = 0.039 (3.0× below): CHECKED (sympy).
- l.122, eq:18.2-rencasc: CHECKED (one terminal electron and one hole per pair; carriers per pair 2.000).
- lim:18.2c markers 0.870, 0.696, 0.837, 0.191, 0.415 (A 5.604), 0.125: CHECKED from log (Ge: G4). Factors 5 and 8, 0.70 → 0.10, 0.025 / 0.013: CHECKED.
- l.142–158, eq:18.2-tagged and eq:18.2-linear: CHECKED (D.44). G2 applies to l.149.
- l.164, 2.67 and 13 %: CHECKED.

**s18-3**
- l.3, 17 %, "one in six", 3.84 eV: CHECKED.
- l.9–32: eq:18.3-seed normalization; eq:18.3-pcasc; eq:18.3-pq (exchange of class sum and integral); DFT aliasing Σ_j P(N + jN_z): CHECKED.
- l.9–32 (cont.): forced region; first ionization at (1+θ)E_g = 2.32 eV; eq:18.3-moments (law of total variance): CHECKED.
- l.24, "none has a mean above six": CHECKED (5.994 at 21.16 eV, tight).
- l.38, q₀ = αm_e = 3728.9 eV; d_TV definition; screened vs unscreened 0.010: CHECKED.
- fig:18-pn10 and l.47–49: every P, mean and variance reproduced by my PGF (DM 0.413/0.548/0.040, mean 2.627, var 0.314 = 0.283 + 0.031; photon 0.399/0.556/0.045, 2.646; uniform 2.692; equal 2.986, 0.079; one-sided 3.005, P(4) 0.143): CHECKED.
- l.47, 3.81 eV and +1.5 %; step +14 %: CHECKED.
- WE 18.3: N_step = 1 + ⌊1.024⌋ = 2 (also with 1.11/3.6); p_ii 0.0041, 0.0185, 0.049, 0.100, 0.146; 43 steps; P_no = 0.1747; CSDA −1.744: CHECKED.
- WE 18.3 (cont.): second ionization ≈ 0.002; 0.990 → 98 %; ⟨E_e⟩ = 2.08 eV; 26 %; P = 0.830/0.170/6×10⁻⁵, mean 1.170, 4.27 eV; 5.9×; photon 0.190, +12 %: CHECKED (independent).
- WE 18.3, "−ln(1−p) ≈ p/(1−p)": first-order only, harmless (it equals Γ_ii/Γ_ph).
- l.69–80, RK Eqs. (5), (6), (7), (8), (10), (14) and Sect. IV B (α rises 4–7.5 eV, extrapolated in the UV gap): CHECKED. b_N: W1. Plasmon: G11.
- l.82–87, eq:18.3-step; offset ½ − E_g/ε = 0.1906; d_TV = 1 − P(n); 0.45 at 20.2 eV: CHECKED (σ_N: W7). Essig Eq. (5.1) = arXiv Eq. (26), the first equation of §5: CHECKED.
- lim:18.3a and l.102–104: all thresholds and maxima: CHECKED (independent). The "0.39" sentence: W2.
- l.102–104: P_DM(2) = 0.14 at 4.91 eV; step min 0.206 (> 4.92 eV) and 0.391 (> 9 eV); mean gap 0.36 at 21 eV; photon 0.014 at 10 eV and ≤ 0.03 above 15 eV: CHECKED.
- l.115, binomial thinning f_det F + 1 − f_det: CHECKED (agrees with SOTA l.114 on RK App. A).

**D-43**: all CHECKED (above). **D-44**: CHECKED with G2 and the κ clash (G9).

## Campaign values, CORRECTIONS/SOTA, DC-RESULTS
- No superseded campaign value is printed in these files. F_eh = 0.114 at E_g = 1.160 eV is the book's own computation.
  It is consistent with DC-67/REF-DC-67 §8 item 6 (F ≈ 0.114, continuum), which is quoted nowhere here, so its restriction is respected.
- Campaign GAP-EF uses E_g = 1.164 eV (DC-67 l.21) with 𝒜_ph = 5.588 eV³ (production) or 5.616 eV³ (continuum). The book's 5.674 eV³ is at 1.160 eV. The difference is expected, not a drift.
  The grid-to-continuum shift is the same +0.5 % in both (book 5.674 → 5.703; campaign 5.588 → 5.616): see G3.
- DC-RESULTS has no row (DC-4 running, DC-41/49/54/36/2/83/91/93) that bears on numbers in 18.1–18.3, D.43 or D.44.
- 2.5σ vs 2.6σ is in 18.4/SPINE, outside these files. The continuum figure is 2.5σ (REF-DC-67 l.87); my continuum F = 0.1142 gives 2.4σ.

## Editorial items in the editor notes (not derivation; no verdict)
fig:18-limit-a rename (done on the 18.3 side), Limit Check 18.2a axis ruling, λ_AB re-display in 18.4,
ceperley entry, "ledger" label, heat-symbol unification (E_heat = E_< + E_> is consistent in 18.1/18.2/D.43).
