# R14 / GAP-EF: the pair-creation energy ε_eh and the Fano factor F_eh from the cascade, including the residual anticorrelation term; final-stage capture and excitons (WP7-E-v3 IF-E9)

Agent GAP-EF, brief briefs/R14/GAP-EF.md. **Coordinator directive applied:** this return is written as a textbook section. §1 is the derivation:
hypotheses, the exact moment equations, the energy-constraint (anticorrelation) mechanism, the limits, and the closed forms. §2–§5 (validation,
predictions, IF-E9 and the ab initio specification) are secondary. Inputs read: returns/R13/WP5-v4.md §1–§3 and §6, returns/R12/WP7-E-v3.md
§1, §2, §7 and IF-E9, returns/R8/WP6-v3.md (yield θ rows), returns/R13/WP8-U.md §0 and §4 with WP8-U-table.csv, LIMITS.md, CONVENTIONS.md
(including the R13 amendments), NOTATION.md (including "Rows added WP7-E"), and state/CORRECTIONS.md §11 and §18. Following that file, WP5's
"W ≈ 12 eV" is written B_h and its "b" is b_N. **No first-principles numerics and no Monte Carlo were run.** The results come from deterministic
quadrature of exact moment recursions in code/GAP-EF/: `cascade.py` is the solver, `model.py` sets the grid and does the calibration,
`predict.py` and `scan.py` write `data/results.json` and `data/scan.json`, and `checks.py` holds **19 checks, 19/19 PASS in 14 s**, cited GAP-EF-Cn.
Tags follow CONVENTIONS §12. **Literature:** 17 papers were fetched into literature/papers-GAP-EF/ and 15 are cited. All arXiv IDs were verified
against the API (`arxiv-*.json`, GAP-EF-C18). Page numbers are PDF pages. The PDFs were deleted, and the `.txt` extracts were kept for the
locators. **Status:** CLAIMED. The solver is CROSS-CHECKED against two independent routes: the exact random-parking solution (C1, C2) and the
R&K Monte Carlo (C8).

---
## 0. Results at a glance
| # | Item | Result | Tag |
|---|---|---|---|
| 1 | Reduction of (W3) | Exact first- and second-moment recursions (EF2)–(EF4) of the energy-only cascade, solved by quadrature. Discretisation error ≤ 0.05% (C5); asymptote stable to 10⁻⁴ (C6) | D given (H-EF1)–(H-EF7) |
| 2 | Energy constraint | With ω fixed, the heat variance is a renewal variance: F = Var(per-pair energy)/ε_eh², **not** /E_g² (EF6). WP5-v4 §6.4(ii)'s "54/175 ≈ 0.31" is the N-fixed value; the constrained value of the same model is **0.039** (C9, C10) | D |
| 3 | The uncomputed term | F_eh = 𝒱_< + 𝒱_> + 2𝒞_<> (EF7). For Si: **0.091 + 0.288 − 0.265 = 0.114**. The anticorrelation is between residual heat ℋ_< and heat ℋ_> emitted above threshold, and it cancels 92% of 𝒱_> | D (exact in the model) |
| 4 | Final-state (renewal) models | Not a bound in either direction: 0.022 vs 0.114 (Si), 0.044 vs 0.051 (RPP limit) | D |
| 5 | Limits | Rényi/RPP exactly (F = 0.05104, C1). Klein's 2.8E_g + rω₀ = identity (EF8) + threshold 3/2 E_g + uniform population, which overstates c₀ by 27–33% (C11). The R&K Monte Carlo F_∞ = 0.115 is reproduced as 0.1145 (C8) | D |
| 6 | One calibrated parameter | 𝒜_ph = 5.59 eV³, fixed by Si ε_eh = 3.749 eV alone; the ABS fit is 5.2 [FT 2610.16949 p.3]. Predicted, uncalibrated: **F_Si = 0.114** vs 0.119 ± 0.002 | D/E |
| 7 | Closed form | ε_eh/E_g = 1.613 + 2.327(λ_ph w₀^{0.964})^{0.2395} (0.5% max), i.e. **ε_eh ≈ 1.61E_g + 2.33(𝒜_phω₀^{0.96})^{0.24}E_g^{0.05}**. This explains the empirical form 1.54E_g + 1.89 [FT 2610.16949 p.2]. F_eh is a quadratic in ε_eh/E_g (2.3% max) | observed (fit) |
| 8 | Validation, 7 [FT] materials | ε_eh residuals (meas/model − 1): −6.5% to +15.7%, rms 10%. The model under-predicts the stiff or polar wide-gap materials (C, GaN, 3C-SiC) | E |
| 9 | Predictions, 27 materials | §3 table, asymmetric bands, all [E]. Wide-gap insulators: ε_eh ≈ 1.8–2.1E_g, F_eh ≈ 0.082–0.088 (0.068 if the valence band is narrow) | E |
| 10 | IF-E9 | Prompt capture is Bernoulli thinning (EF12). Excitons leave N_eh and ε_eh unchanged and act on ℋ_eff and N^meas (EF13)–(EF14). Effective-gap sensitivity (EF11). BSE/capture specification in §4.3 | D / D, sketch / E |
| 11 | Owed correction | WP5-v4 §6.4(ii), WP5v3-C4b (S type): IF-EF1 | D |

---
## 1. Theory: ε_eh and F_eh as moments of the cascade

### 1.1 The question and the exact starting point
A deposit ω creates N_eh pairs. Under the conditions of WP5 (W4) (no capture, no excitons and no bias work before t_pr, E_st = E_esc = 0), every
event obeys ω = N_eh E_g + ℋ, so

  ε_eh = ω/n̄,   F_eh = Var N_eh/n̄ = Var ℋ/(E_g² n̄)   (exact; WP5 (W14), WP5v3-C3).                                                                     (EF1)

So F_eh is a property of the heat ℋ. In the reduced cascade below, ℋ splits into two parts:
- ℋ_<, the residual kinetic energy that each carrier holds when it falls below the ii threshold for good;
- ℋ_>, the phonon energy emitted while the carrier is still above threshold.

WP5-v4 §6.4 left F_eh = [Var(Σ residuals, with the energy-constraint anticorrelation) + Var(phonon)]/(E_g² n̄) with the first term uncomputed.
Two naive evaluations fail:
- (a) *Independent residuals with N held fixed.* Var ℋ = n̄·2σ_c², with σ_c² the per-carrier residual variance, gives F = 2σ_c²/E_g². This is
  WP5v3-C4b's 54/175 in the Klein distribution. It treats N as fixed, but N is itself determined by ℋ.
- (b) *Phonon shot noise alone* (WP5 (iii)). This drops the residual term altogether.

What is needed is the joint law of (N, ℋ_<, ℋ_>) at fixed ω. Sections 1.2–1.4 obtain it exactly within a controlled reduction of (W3).

### 1.2 Hypotheses (H-EF1)–(H-EF7)
- **(H-EF1) Energy-only reduction.** WP5 (W7) under (R-k) or (R-k′): after the first collision a carrier's state is its type t ∈ {e, h} and its
  kinetic energy x ≥ 0 above its band edge. Its error is θ_{R-k}, not quantified here (WP5 gap R2).
- **(H-EF2) Independent siblings, Markov, minimal solution, termination.** WP5 (B1), (B2), (H-t), (H-m). (B2) is controlled only for small
  seeds (θ_dense).
- **(H-EF3) Random-k ii kernel.** This is the Alig–Bloom–Struck "scattering-rate" assumption, constant matrix elements [FT 2610.16949 pp.2–3].
  For x ≥ E_th^{ii} ≡ θ_ii E_g, a carrier of type t produces (t, x₁) + (t, x₂) + (t̄, x₃) with x₁ + x₂ + x₃ = x − E_g. The joint density is
  ρ_t(x₁)ρ_t(x₂)ρ_t̄(x₃)/Φ_t(x − E_g), with Φ_t ≡ ρ_t * ρ_t * ρ_t̄ (a threefold convolution). The DOS shape is ρ(x) ∝ x^{a_DOS}, optionally
  truncated at the hole bandwidth B_h.
- **(H-EF4) Competing phonon channel.** One effective optical mode ω₀ (= ω_LO, or ω_max where only ω_max is tabulated). Emission only, T ≪ ω₀.
  The rate ratio is

  R_t(x) ≡ Γ^{ph}_t/Γ^{ii}_t = λ_ph ρ_t(x − ω₀)/Φ_t(x − E_g),   λ_ph ≡ 𝒜_ph/E_g³.                                                                     (EF2)

  For a_DOS = ½ this is R&K Eq. (8) with 𝒜_ph = their A [FT 2004.10709 p.3]. The units of 𝒜_ph are eV³ (WP5 §6.2 discrepancy (1)).
- **(H-EF5) Universal 𝒜_ph.** One 𝒜_ph serves all materials (the ABS hypothesis). It is calibrated once, on Si ε_eh. Its failure is not
  modelled; it is measured by the validation residual band of §2.
- **(H-EF6) Temperature enters only through E_g(T).** WP5 §6.2 says this is incomplete. Phonon absorption is neglected.
- **(H-EF7) No plasmon channel.** By WP5 Theorem C(a) the plasmon decays into the same e–h weight. R&K add an explicit plasmon channel; C8 shows
  it changes F_∞ by < 0.5%.

### 1.3 The moment equations
For a deposit Y that adds d_ii at each ii event, d_ph at each phonon emission and d_<(x) at termination, let m_t(x) = E[Y|t, x] and
s_t(x) = E[Y²|t, x], and let p_t = 1/(1 + R_t). First-step analysis of (W3), conditioning on the first collision and factorising the three
independent subtrees with (H-EF2), gives for x ≥ θ_ii E_g:

  m_t(x) = p_t [d_ii + ⟨m_t(x₁) + m_t(x₂) + m_t̄(x₃)⟩] + (1 − p_t)[d_ph + m_t(x − ω₀)],                                                        (EF3)
  s_t(x) = p_t ⟨(d_ii + Y₁ + Y₂ + Y₃)²⟩ + (1 − p_t)[d_ph² + 2d_ph m_t(x − ω₀) + s_t(x − ω₀)],   ⟨Y_iY_j⟩ = m m (i ≠ j, independent subtrees),     (EF4)

with ⟨·⟩ the (H-EF3) average. Below threshold m = d_<(x) and s = d_<². The pair number is Y = N (d_ii = 1). The residual heat is Y = ℋ_<
(d_< = x). The above-threshold phonon heat is Y = ℋ_> (d_ph = ω₀).

Because the ii averages are convolutions with ρ's, every term of (EF3)–(EF4) is a one-dimensional convolution of quantities that are already
known at lower energy. A single upward sweep in x therefore solves the system at cost O(K²) on a K-point grid. The grid is chosen with ω₀ on it
(n_w steps); without this, the phonon-to-gap ratio would be distorted by up to 30% at coarse spacing.

The discrete kernel conserves energy to 10⁻¹⁵ (C3). The variance of N and the variance of ℋ_< + ℋ_> come from independent recursions and satisfy
E_g² Var N = Var(ℋ_< + ℋ_>) to 10⁻⁹ (C4). This is (EF1) verified numerically.

### 1.4 Asymptotic linearity
For x ≫ E_g the solutions become n̄ = ω/ε_eh + b_N and Var N = F_eh ω/ε_eh + O(1). This is WP5 §6.4, [D, sketch] by the key renewal theorem
under (r1)–(r3). Hypothesis (r2) fails on the {E_g, ω₀} lattice, but the periodic remainder averages out in the linear fit.
- Numerically the slopes change by < 10⁻⁴ between X = 40E_g and X = 80E_g and between fit windows (C6).
- For λ_ph ≳ 5 (gaps ≲ 1 eV), the asymptote needs X = 60E_g; X = 25 shifts F by 4% for InSb.
- By-product [E]: for Si, b_N = 0.345 for a one-sided seed (all energy on the electron) and b_N ≈ 0.00 for a symmetric seed. b_N therefore
  depends on the seed, which is the statement of WP5 VER-WP5-A N2.

### 1.5 The energy constraint: why ε_eh, not E_g, sits in the denominator [D]
Model the cascade as a renewal sequence: each pair costs ε_i = E_g + h_i, where h_i is that pair's heat. The h_i have mean ε_eh − E_g and
variance σ_h², and pairs are produced until ω is spent. The renewal theorem gives Var N ≃ ωσ_h²/ε_eh³ (Fano 1947; 0911.1532 Eqs. (5)–(7)
[FT p.2–3]). With (EF1),

  F^{ren} = σ_h²/ε_eh²,   equivalently   Var ℋ = n̄ σ_h² (E_g/ε_eh)².                                                                               (EF6)

At fixed ω, the fluctuations of ℋ and of N are locked together. A pair that costs more heat leaves less energy for later pairs. This is the
energy-constraint anticorrelation, and it multiplies the naive N-fixed variance by (E_g/ε_eh)².

C10 checks (EF6) against an explicit renewal recursion with the exact energy constraint (agreement 0.0426 vs 0.0426). Applied to Klein's
uniform-population residual (√x on [0, θ_iiE_g], two carriers per pair): F^{ren} = 2σ_c²/ε² = (54/175)(5/14)² = **0.0394**, not 0.31 (C9).
**WP5-v4 §6.4(ii) ("2.6× the data") is therefore an N-fixed artefact.** The independent-residual model *under*-predicts F_eh by 3×. This is an
owed correction, IF-EF1.

### 1.6 The exact decomposition and the computed anticorrelation term [D within (H-EF1)–(H-EF7)]
Taking the second moments of ℋ_< and ℋ_> from (EF3)–(EF4) separately gives

  F_eh = 𝒱_< + 𝒱_> + 2𝒞_<>,   𝒱_≶ ≡ Var ℋ_≶/(E_g² n̄),   2𝒞_<> ≡ 2Cov(ℋ_<, ℋ_>)/(E_g² n̄).                                                    (EF7)

| case (θ_ii = 1, a_DOS = ½) | ε_eh/E_g | 𝒱_< | 𝒱_> | 2𝒞_<> | F_eh | F^{ren} (EF6) | r̄_c/E_g |
|---|---|---|---|---|---|---|---|
| λ_ph → 0 (no phonons) | 1.585 (Richardson) | 0.080 | 0.000 | +0.001 | 0.081 | 0.057 | 0.30 |
| Si (λ_ph = 3.55, w₀ = 0.054) | 3.221 | 0.091 | 0.288 | −0.265 | **0.114** | 0.022 | 0.715 |
| Si, θ_ii = 3/2 (re-calibrated) | 3.221 | 0.101 | 0.178 | −0.166 | 0.113 | 0.047 | 0.900 |
| λ_ph = 13 (Ge-like) | 3.86 | 0.148 | 0.454 | −0.477 | 0.125 | 0.016 | 0.77 |

(r̄_c is the mean terminal residual per carrier.) The table answers the question left open in WP5-v4:
- **The leading term is not the residual variance.** When phonons compete (Si, Ge), the largest piece is 𝒱_>, the variance of the
  above-threshold phonon heat. It is far above Poisson shot noise (0.288 vs w₀⟨ℋ_>⟩/(E_g n̄) ≈ 0.04), because the number of phonons a carrier
  emits before it ionizes is a wide, geometric-like random variable.
- **The anticorrelation is between ℋ_> and ℋ_<.** A carrier that loses more energy to phonons near threshold reaches termination with a smaller
  residual, or it ionizes later at lower energy. Energy conservation along each carrier's line enforces this, and 2𝒞_<> removes 92% of 𝒱_> in Si.
- **The net F_eh is a small difference of large terms.** That is why "final-state" models, which keep only one-particle residual statistics
  (F^{ren}), miss it by up to 5×.
- **The final-state model is not a bound.** It under-predicts by 1.4–5× in the semiconductor cases but over-predicts in the RPP limit
  (0.0444 vs 0.0510, C2, which reproduces 0911.1532's F_unc = 0.0440 [FT p.4]). Its sign depends on the sibling correlations, as 0911.1532
  shows for nearest-neighbour terms (F_nnp = 0.0521).
- **Without phonons, F_eh → 0.081.** This value is purely partition noise: the exact jamming distribution of residuals, which is strongly
  peaked at x → 0 as in Rényi parking, with its sibling correlations (2𝒞 ≈ 0).

### 1.7 Limits recovered (LIMITS rows below)
- **(a) Random parking (Rényi).** a_DOS = 0 for electrons, a δ-function hole DOS (narrow valence band), θ_ii = 1, no phonons. (EF3)–(EF4) give
  coverage 1/ε = 0.74760 and F = 0.05104 after Richardson extrapolation. The exact values are 0.7475987 and 0.0510387 [FT 0911.1532 Eq. (23)
  p.4, Eq. (2) p.2] (C1). This tests the second-moment algebra against an exactly soluble cascade.
- **(b) Shockley/Klein identity.** Two terminal carriers per pair and energy conservation give, exactly,

  ε_eh = E_g + 2r̄_c + ⟨ℋ_>⟩/n̄   (≡ E_g + 2r̄_c + rω₀,  r = phonons emitted above threshold per pair).                                          (EF8)

  This is Shockley's ε = 2E_f + E_i + rE_R [FT 2610.16949 Eq. (1) p.2], with E_i → E_g in the pair term and the threshold entering through r̄_c.
  **Klein's ε = (14/5)E_g + rω₀** [FT 2610.16949 p.2; FT 1602.08005 Eq. (3) p.6] follows from (EF8) under two truncations:
  (K1) θ_ii = 3/2 (parabolic bands, equal masses, momentum conserved);
  (K2) a uniform-in-k terminal population, r̄_c = (3/5)θ_iiE_g (C9).
  The truncation error of (K2) is computed here. At λ_ph → 0 the exact c₀ ≡ ε_eh/E_g is 1.585 (θ_ii = 1) and 2.056 (θ_ii = 3/2), against
  (K2)'s 2.2 and 2.8 (C11). The true jamming population sits at low x, with r̄_c ≈ 0.30θ_ii–0.35θ_ii instead of 0.6θ_ii. With phonons, r̄_c rises
  (0.715E_g for Si), because carriers stall just above threshold. (K2) therefore errs by −20% to +40% depending on λ_ph.
- **(c) R&K / ABS.** θ_ii = 1, a_DOS = ½, B_h = 12 eV, 𝒜_ph = 5.2 eV³, E_g = 1.124 eV, ω₀ = 63 meV give F_∞ = 0.1145. R&K's Monte Carlo gives
  0.115 [FT 2004.10709 p.6] (C8). This is an independent route agreeing to 0.5%, so the solver is CROSS-CHECKED.
- **(d) Measured Si and Ge Fano factors.** With 𝒜_ph fixed by Si ε_eh only:
  - Si: F_Si = 0.1138, against 0.119 ± 0.002 at 5.9 keV, 123 K [FT 2004.11499 p.1, p.5] (−4.4%; C7b).
  - Ge: F_Ge = 0.125 (77 K), inside the reported 0.06–0.13 [FT 1909.05806 p.14, a secondary quote of five experiments] and at the
    1909.05806 model value 0.106 + 18%.

### 1.8 Closed forms and the linear law (observed)
For θ_ii = 1, a_DOS = ½, a 60-point scan over λ_ph ∈ [0.003, 100] and w₀ ≡ ω₀/E_g ∈ [0.01, 0.1] (scan.py; C14) gives

  ε_eh/E_g = 1.613 + 2.327 (λ_ph w₀^{0.964})^{0.2395}   (max 0.52%, rms 0.19%),                                                                  (EF9)
  F_eh = 0.02347 + 0.03643 e − 0.002711 e² + 0.01653 w₀,   e ≡ ε_eh/E_g   (max 2.3%, rms 0.8%).                                                (EF10)

Substituting λ_ph = 𝒜_ph/E_g³ into (EF9) gives ε_eh ≈ 1.61E_g + 2.33(𝒜_phω₀^{0.96})^{0.24}E_g^{0.05}. The second term is almost independent
of E_g: it is 1.86 eV at ω₀ = 63 meV and 2.31 eV at 163 meV. **The cascade therefore predicts the linear form ε_eh = k₁E_g + k₂ with
k₁ ≈ 1.6 and k₂ ≈ 1.9–2.3 eV.** This is the recent empirical fit 1.54E_g + 1.89 [FT 2610.16949 p.2]. It also explains why Klein's slope 2.8
(fitted to small-gap data, where λ_ph is large) overshoots in wide-gap materials [FT 2311.05011 p.5: Klein gives 15.92 eV for diamond against a
measured ≈ 13].

(EF10) shows F_eh rising monotonically with how phonon-dominated the cascade is: from 0.081 (no phonons) to ≈ 0.14 (λ_ph = 100). Tag:
**observed** (CONVENTIONS §12, R13 amendment): it is verified on the scan but not derived. For λ_ph > 100 (E_g ≲ 0.38 eV) use the solver, not the
fits. The effective-gap sensitivity at fixed 𝒜_ph and ω₀ (used in §4) follows from (EF9):

  dε_eh/dE_g = c₀′ + c₁u(1 − 3β − γβ),   u = (λ_ph w₀^γ)^β,   (c₀′, c₁, γ, β) = (1.613, 2.327, 0.964, 0.2395)   [Si: 1.70; solver FD 1.78, C15].   (EF11)

### 1.9 Truncation budget
| Item | Size | Status |
|---|---|---|
| discretisation (ω₀ on grid; N vs 2N) | ε 0.05%, F 0.05% (Si); 0.2% (SiO₂) | quantified (C5) |
| asymptote / fit window (r1)–(r3) | < 10⁻⁴ (λ_ph ≲ 5); 1.4% ε, 4% F at X = 25 for λ_ph ≈ 400 (X = 60 used) | quantified (C6) |
| θ_ii ∈ [1, 3/2] (re-calibrated) | ε: +0 to +10%; F: −3% | quantified (§3 band) |
| a_DOS ∈ [½, 1] (re-calibrated) | ε: up to +8%; F_Si: −10% | quantified (§3 band) |
| narrow valence band B_h = E_g | F → 0.068; ε +4–7% (ionic) | quantified (§3 band) |
| fits (EF9)–(EF10) | 0.5% / 2.3% max | quantified (C14) |
| (H-EF1) energy-only reduction | — | **not quantified**: θ_{R-k}, WP5 R2 |
| (H-EF5) universal 𝒜_ph | ε residual −6.5% … +15.7% (§2) | absorbed into the validation band |
| (H-EF6) T only via E_g(T); (H-EF2) (B2) at ≳ keV | — | not quantified (WP5 §6.2; θ_dense) |

---
## 2. Data compilation and validation
**The calibration (the only fitted parameter).** 𝒜_ph is fitted to Si ε_eh = 3.749 ± 0.001 eV (123 K, 5.9 keV) [FT 2004.11499 p.1, p.5], with
E_g = 1.164 eV (110 K) [FT 2004.10709 Table I p.5], ω₀ = 63 meV [FT 2004.10709 p.3] and B_h = 12 eV [FT 2004.10709 p.3]. The result is
𝒜_ph = 5.595 eV³ (V0). Re-calibrated variants: V1 (θ_ii = 3/2) 5.525; V3 (a_DOS = 1, different units of Φ) 0.688.

| Material | E_g, ω₀ (eV) [source] | ε_eh measured [source] | model V0 (V1, V3) | resid. | F measured | F model |
|---|---|---|---|---|---|---|
| Si (calib.) | 1.164, 0.063 [FT 2004.10709] | 3.749 ± 0.001 [FT 2004.11499]; 3.748(2), 3.783(4) at 0.68/1.49 keV; 3.71 ± 0.08 below 150 eV | 3.749 | — | 0.119 ± 0.002 (5.9 keV); 0.137(6), 0.146(9) at 0.68/1.49 keV [FT 2305.09005 Table I p.6]; < 0.31 [FT 2202.03924 Table II p.7] | 0.114 |
| Ge (77 K) | 0.73 [FT 1909.05806 p.15], 0.037 [FT 1901.07569 Table I p.2] | 2.96 [FT 1909.05806 p.14]; "∼3" [FT 1602.08005 p.6] | 2.79 (2.79, 2.69) | +5.9% | 0.06–0.13 [FT 1909.05806 p.14, secondary] | 0.125 |
| C | 5.47, 0.163 [FT 1901.07569 Table I] | 13.1 ± 0.2, 13.25 ± 0.5, 13.05 ± 0.2, 12.82 ± 0.13 [FT 2311.05011 p.5]; mean 12.95 | 11.37 (11.81, 12.24) | +13.9% | — | 0.088 |
| 4H-SiC | 3.26, 0.120 [FT 2008.08560 Table I p.5] | 7.83 ± 0.02 [FT 2311.03902 p.1, p.5]; earlier values 5.05–8.6 (Table 1 p.2) | 7.57 (7.68, 8.05) | +3.5% | 0.1 (2011 linewidth); ≤ 0.04 (2005 limit) [FT 2311.03902 Table 2 p.2] | 0.093 |
| 6H-SiC | 3.02, 0.120 [FT 2008.08560] | 6.7 [FT 2008.08560 Table I] | 7.17 (7.25, 7.60) | −6.5% | — | 0.094 |
| 3C-SiC | 2.39, 0.1205 [FT 2008.08560] | 6.90 [FT 2610.16949 Table II p.8]; "5.7–7.7†, estimated" [FT 2008.08560] | 6.12 (6.15, 6.40) | +12.8% | — | 0.099 |
| GaN | 3.43, 0.0889 [FT 1910.10716 Table I p.2] | 8.9; 9.59 (EBIC) [FT 2308.03893 pp.18–19] | 7.69 (7.84, 8.22) | +15.7% (+25% EBIC) | — | 0.091 |
| SiO₂ | 9.2, 0.149 (α-quartz) [FT 1910.10716] | 18.0, one sample 16.4 (1975 oxide) [FT 2610.16949 p.8] | 17.41 (19.05, 18.76) | +3.4% (−5.8%) | — | 0.084 |
| GaAs | 1.42, 0.0349 [FT 1910.10716] | ≈ 4.2 [UNVERIFIED: Bertuccio–Maiocchi, DOI 10.1063/1.1490158, no open full text; plotted in 2610.16949 Fig. 1] | 3.95 | (+6%, excluded) | — | 0.104 |

**Residuals** over the seven [FT] rows: range −6.5% to +15.7%, mean +7.0%, rms 10.0% (C13). GaAs and CdTe (≈ 4.4 eV [UNVERIFIED]) have no open
full text and are excluded; so is β-Ga₂O₃ (15.6 eV, a self-described "experimental estimation" from EBIC+MC [FT 2311.05011 p.5]).

**Reading.**
- The one-𝒜 model is good to ±6% for Ge, the SiC polytypes and SiO₂.
- It under-predicts the stiff or polar wide-gap materials (C, GaN, 3C-SiC) by 13–16%. This is the ABS pattern: ABS work for Si, Ge, AgBr and
  3C-SiC and fail for SiO₂, C, PbO and CdS [FT 2610.16949 p.3]. Physically, (H-EF5) underestimates the electron–phonon coupling of light-atom
  and polar lattices.
- **The ab initio route does better on exactly these materials** [FT 2610.16949 Table II; FT 2311.05011 p.5; FT 2308.03893 p.19]: C 12.87,
  GaN 8.9, 4H-SiC 7.3 eV.
- The low-energy rise of the measured Si F (0.137–0.146 below 1.5 keV [FT 2305.09005]) is not in the asymptote. It is either finite-ω structure
  or the PCC systematics that 2305.09005 models. It is not a model failure at keV.

---
## 3. Predictions for WP8-U survivors lacking data [E]
**Recipe.**
- Inputs E_g and ω₀ = ω_O,max (or ω_Γ,max) are copied from returns/R13/WP8-U-table.csv, with its source and locator: [FT 1910.10716 Table I
  p.2] unless marked; TeO₂, SrTiO₃ and KTaO₃ use JARVIS JVASP-57128, -8082 and -1127 (TBmBJ gap and Γ modes) [DB], a DFT proxy gap.
- The central value is V0. The band combines in quadrature the variant spread (V1, V3, and B_h = E_g for ionic and oxide materials, marked ⁿ)
  with the validation range (−6.5% / +15.7% on ε; Si's +4.5% on F).
- **No bias correction is applied**; that would be a second calibrated parameter. The one-𝒜 model tends to under-predict polar and stiff
  wide-gap materials, so the upper half of each band is the more likely one.
- **Li₂MoO₄ stays GAP** (no ω₀ and no experimental gap).

| Material (WP8-U verdict) | E_g | λ_ph | ε_eh [eV] (band) | ε_eh/E_g | F_eh (band) |
|---|---|---|---|---|---|
| GaAs (S) | 1.42 | 1.95 | 3.95 (3.69–4.58) | 2.78 | 0.104 (0.096–0.108) |
| Al₂O₃ (S)ⁿ | 8.8 | 0.0082 | 16.5 (15.5–19.6) | 1.88 | 0.084 (0.067–0.088) |
| TeO₂ (S)ⁿ [DB gap] | 4.65 | 0.056 | 9.7 (9.1–11.4) | 2.09 | 0.088 (0.068–0.092) |
| CaWO₄ (S)ⁿ | 5.2 | 0.040 | 10.7 (10.0–12.6) | 2.06 | 0.087 (0.068–0.091) |
| LiF (S)ⁿ | 14.2 | 0.0020 | 25.1 (23.4–30.7) | 1.76 | 0.082 (0.068–0.086) |
| NaF (S)ⁿ | 11.5 | 0.0037 | 20.5 (19.2–25.0) | 1.78 | 0.082 (0.068–0.086) |
| Ge (S), F only | 0.73 | 14.4 | 2.79 (2.58–3.23) | 3.83 | 0.125 (0.108–0.130) |
| C (C), F only | 5.47 | 0.034 | 11.4 (10.6–13.4) | 2.08 | 0.088 (0.083–0.092) |
| 4H-SiC (C), F only | 3.26 | 0.16 | 7.57 (7.07–8.84) | 2.32 | 0.093 (0.088–0.097) |
| GaN (C), F only | 3.43 | 0.14 | 7.69 (7.19–9.01) | 2.24 | 0.091 (0.086–0.095) |
| AlN (C) | 6.2 | 0.024 | 12.3 (11.5–14.5) | 1.99 | 0.086 (0.081–0.090) |
| SiO₂-q (C)ⁿ | 9.2 | 0.0072 | 17.4 (16.3–20.6) | 1.89 | 0.084 (0.067–0.088) |
| ZnO (C)ⁿ | 3.3 | 0.16 | 7.32 (6.83–8.57) | 2.22 | 0.090 (0.069–0.095) |
| MgO (C)ⁿ | 7.83 | 0.012 | 14.8 (13.9–17.6) | 1.90 | 0.084 (0.067–0.088) |
| ZnS (C) | 3.8 | 0.10 | 7.95 (7.43–9.34) | 2.09 | 0.088 (0.083–0.091) |
| NaCl (C)ⁿ | 8.75 | 0.0084 | 15.8 (14.8–19.2) | 1.81 | 0.083 (0.067–0.087) |
| NaI (C)ⁿ | 5.8 | 0.029 | 10.9 (10.2–13.0) | 1.88 | 0.084 (0.067–0.088) |
| CsI (C)ⁿ | 6.14 | 0.024 | 11.5 (10.7–13.7) | 1.87 | 0.083 (0.067–0.087) |
| CaF₂ (C)ⁿ | 11.81 | 0.0034 | 21.0 (19.7–25.7) | 1.78 | 0.082 (0.068–0.086) |
| MgF₂ (C)ⁿ | 12.4 | 0.0029 | 22.1 (20.7–27.0) | 1.79 | 0.082 (0.068–0.087) |
| SrTiO₃ (C)ⁿ [DB gap] | 2.30 | 0.46 | 5.68 (5.24–6.63) | 2.47 | 0.096 (0.071–0.101) |
| KTaO₃ (C)ⁿ [DB gap] | 3.33 | 0.15 | 7.37 (6.88–8.64) | 2.22 | 0.090 (0.069–0.095) |
| GaSb (C) | 0.72 | 15 | 2.67 (2.48–3.09) | 3.70 | 0.122 (0.106–0.128) |
| InSb (C) | 0.24 | 405 | 1.75 (1.40–2.03) | 7.3 | 0.159 (0.127–0.166) |
| PbS (C) | 0.29 | 229 | 1.92 (1.57–2.22) | 6.6 | 0.155 (0.124–0.162) |
| PbTe (C) | 0.19 | 816 | 1.52 (1.19–1.76) | 8.0 | 0.162 (0.129–0.170) |
| PbSe (C) | 0.17 | 1140 | 1.56 (1.17–1.80) | 9.2 | 0.168 (0.133–0.175) |

**Caveats** (each widens the band beyond what is written; tagged [E]).
- *Ionic crystals (alkali halides, fluorides, oxides).* Self-trapped and Frenkel excitons with E_x^b ~ eV mean that the "pair" of the charge
  ledger and the cascade quantum differ (§4). The narrow anion-p valence band (ⁿ) drives F to 0.068.
- *Narrow-gap rows (λ_ph ≫ 100).* They sit outside the fit domain and outside the validated range. Their cascades are dominated by phonons, with
  free-carrier and Auger channels absent from (H-EF3).
- *Incipient ferroelectrics (SrTiO₃, KTaO₃).* The soft modes break (H-EF4)'s single ω₀.

---
## 4. WP7-E-v3 IF-E9: capture at the end of the cascade and exciton parameters

### 4.1 Prompt shallow-level capture (t < t_pr) [D for the algebra; D, sketch for σ_cap]
The cascade ends with carriers at x ≲ θ_iiE_g. They relax to the band edges through ℋ_<, and each can be captured on level j before t_pr. Write
f_cap^{e,h} = 1 − exp[−𝓃_j∫_0^{t_pr}σ_cap(u_car)u_car dt].
- Capture does not change the number of ii events, N_ii (pairs created), so ε^{cas} ≡ ω/⟨N_ii⟩ = ε_eh of §1–§3.
- Per WP5 A-1, a captured electron leaves N_eh ≡ N_e^f + N_X. If captures are independent per carrier (dilute traps, (H-E5) at the carrier
  level), N_eh is a Bernoulli thinning of N_ii:

  ε_eh^{(W4)} = ε^{cas}/(1 − f_cap^e),   F_eh′ = (1 − f_cap^e)F_eh + f_cap^e   (C16),   ℋ_eff += Σ_captured E^tr_{e,j} (+ E_trap^{pr} in the ledger).   (EF12)

- Hole capture leaves N_eh unchanged but adds E_pairs^{unp} and E_trap^{pr} (WP7-E-v3 (E1-W4)). In N^meas each captured carrier contributes
  𝔮_i ≈ 0. This enters WP7-E-v3 (E12) through m_ind(r) and Var 𝔮, not through F_eh.
- *Cross-section [D, sketch; prefactor UNVERIFIED].* For an attractive shallow centre, a carrier of kinetic energy E is captured if it emits a
  phonon inside the Coulomb radius r_C(E) = e²/(4πε_r E). This gives σ_cap(E) ≈ πr_C² min[1, r_C/ℓ_ε(E)], with ℓ_ε the energy-relaxation length.
  For thermal carriers (E → k_BT) it reduces to the Lax/Abakumov–Perel–Yassievich form (4π/3)r_T³/ℓ_ε [UNVERIFIED]. At the cascade end
  E ≈ r̄_c ~ 0.3–0.7E_g (§1.6), so r_C is a few Å and prompt capture is small unless 𝓃_j ≳ 10¹⁸ cm⁻³ [E]. Capture during the slow acoustic
  cooling below ω_LO is post-prompt (WP7-E-v3 §2.1).

### 4.2 Excitons at the end of the cascade [D for the bookkeeping; E for numbers]
- **(i) Ledger.** By the WP7-E-v3 convention, N_eh = N_e^f + N_X counts bound pairs, so excitons do not change ε_eh or F_eh. They shift only
  ℋ_eff by ΔE_X^b = −N_XE_x^b:

  F_eh^{ℋ} = Var(ℋ_eff)/(E_g²n̄) with ℋ_eff = ℋ + ΔE_X^b (WP5 (W4′)) — identical to F_eh because N_eh is unchanged; the heat estimator alone moves by −⟨N_X⟩E_x^b/ω.   (EF13)

- **(ii) Geminate formation.** The thermalisation distance r₀ of a cascade pair is set by its cooling. Onsager escape [UNVERIFIED classic] gives
  p_esc ≈ exp(−r_O/r₀), with r_O = e²/(4πε_r k_BT_c) and T_c the carrier temperature, enhanced by ℰ_b. A pair that forms an exciton and never
  dissociates gives 𝔮 = 0. Per pair this is Bernoulli, so

  N^meas: ϵ → ϵ_coll(1 − f_X(1 − p_diss)),   F_meas = ϵF_eh + 1 − ϵ   (WP7-E-v3 (E12), single position).                                    (EF14)

  Non-geminate (density-dependent) formation is not Bernoulli. It enters as the ⟨N_eh⟩Var_r m_ind/⟨𝔮⟩ term of (E12), which grows with N.
- **(iii) Impact excitation.** In materials with large E_x^b, a carrier in [E_g − E_x^b, θ_iiE_g) can create a bound pair directly. To first
  order this lowers the effective pair cost: Δε_eh ≈ −f_imp E_x^b·dε_eh/dE_g, with (EF11) giving ≈ 1.7 (Si) to ≈ 1.6 (wide gap) and f_imp the
  fraction of pairs created bound. This matters only for ionic crystals (E_x^b ~ 1 eV [UNVERIFIED]); for Si and Ge, E_x^b ≈ 15 and 3 meV
  ([UNVERIFIED]; 2.7 meV quoted in [FT 1909.05806 p.15]) and the shift is < 1%.
- *Hydrogenic estimates [E]* (E_x^b = 13.606 μ*/ε_r² eV, JARVIS BoltzTraP masses [DB], ε_r: GaN 9.5, ZnO 8.1, 4H-SiC 9.8 [E]): GaN 26 meV,
  ZnO 42 meV, 4H-SiC 49 meV (C17). These are Wannier-limit numbers only. Alkali halides and fluorides need BSE.

### 4.3 Computation specification (not run)
- **Exciton parameters (E_x^b, a_x, oscillator strengths, and binding to donors/acceptors).** G0W0 + BSE (BerkeleyGW or Yambo).
  - Fine k-grid by double-grid interpolation, with spacing ≲ 1/(3a_x): Si/Ge need 10⁴–10⁵ k-points; ionic crystals 8³–12³.
  - 4–8 valence and 4–8 conduction bands; lattice screening ε₀ vs ε_∞ through a polaronic correction when E_x^b ~ ω_LO.
  - Validation: Si and Ge free-exciton binding; the LiF and NaCl exciton peaks.
  - Cost [E]: 10³–10⁴ core-h for semiconductors, 10⁴ for oxides.
- **Capture.**
  - Shallow levels: effective-mass levels E_d = 13.6m*/ε_r² eV with central-cell DFT corrections; σ_cap(E, T, ℰ_b) from cascade-capture theory
    with EPW acoustic and optical emission rates (the same g^S as WP5 (W2), O4-d2).
  - Deep levels: multiphonon capture with DFT charge-transition levels and Huang–Rhys factors (WP4-v3 §6 [6.3]).
  - Output: f_cap(t) on the cascade-end distribution of §1 (r̄_c, σ_c per type), as input to (EF12) and θ_tr^{pr}.
  - Cost [E]: ~10⁵ CPU-h per material (WP7-E-v3 §7).
- **Exciton kinetics.** As in the WP7-E-v3 §7 module, seeded by the cascade-end pair separation distribution (needs k-resolved (H-EF1)
  violations: θ_{R-k}).

---
## 5. Computation specification for the full ab initio route (not run)
The pipeline is WP5-v4 §2, which is not repeated here: QE + G0W0 bands, BerkeleyGW full-frequency ε⁻¹(p,ω) for the (W1′) ii kernel, EPW for
(W2) with WP5-cp1–cp3, and a full-band cascade. Additions for ε_eh and F_eh:
- **Kernels.** Tabulate the ii kernel 𝒦̄(E → E′; E_e′, E_h′) and the phonon kernel per branch on 10 meV bins up to ≈ 100 eV. Above ≈ 15 eV,
  match to free-electron states with GW lifetimes. Hole bands and B_h are taken from the band structure, not as parameters.
- **Statistics for F.** F_eh is a second moment. An event-sampling solver needs N_ev ≈ 2/δ² events for relative precision δ, i.e. 2×10⁴ events
  of ≥ 1 keV for 1% on F. Alternatively, the deterministic (EF3)–(EF4) on the iso-energy kernels (no sampling) gives F directly, and only the
  n_gen = 1 k-resolved step needs sampling.
- **Per material.**
  - Si, Ge (SOC), GaAs (SOC, polar: Fröhlich g^L, cp1–cp3): 10⁴–10⁵ core-h each (WP5 §2).
  - C, SiC (3C/4H; 4H cell has 8 atoms): ×2.
  - GaN, AlN (wurtzite, polar): ×2.
  - Al₂O₃ (10-atom cell), CaWO₄ (12), TeO₂ (12), LiF, NaF (2): ≈ 10⁵ core-h for the oxides; the halides as Si, plus BSE (§4.3) because
    excitons are large.
- **Expected accuracy.** The DFT/TDDFT full-band MC errors were −14% (Si), −0.6% (C), 0% (GaN), −6.8% (4H), −4% (3C) and −7% (SiO₂). GW/BSE
  improves Si to −3% [FT 2610.16949 Table II p.8, p.9; FT 2311.05011 p.5; FT 2308.03893 p.19]. This is comparable to the semi-analytic model
  (§2) for Si, Ge, SiC and SiO₂, and clearly better for C and GaN. **Recommendation:** run the ab initio route first for the polar/stiff
  wide-gap survivors (Al₂O₃, CaWO₄, LiF, NaF), where (H-EF5) is least trustworthy. No ab initio F_eh exists in those sources, so the first one
  would be new.

---
## 6. Exact remaining gaps
- **GE-1.** (H-EF1) (θ_{R-k}) and (H-EF5) (universal 𝒜_ph) are the two unquantified truncations. The second accounts for the +14% to +16%
  residuals in C and GaN.
- **GE-2.** No open full-text ε_eh or F_eh for GaAs, CdTe or diamond F. No measured F for any wide-gap material except the 4H-SiC linewidth
  estimate.
- **GE-3.** T dependence beyond E_g(T) (phonon absorption, n_B in (W1)). Ge at 77 K vs mK is open (1602.08005).
- **GE-4.** Exciton-dominated ionic crystals: the cascade quantum vs the ledger pair, and impact excitation (f_imp).

---
## 7. Checks (code/GAP-EF/checks.py, 19/19 PASS, 14 s)
| Check | Content |
|---|---|
| C1, C2 | Rényi/RPP limit: coverage and F_exact; renewal F_unc = 0.0440 (0911.1532) |
| C3, C4 | energy conservation of the discrete kernel; F from N-moments = F from heat moments; (EF7) closes |
| C5, C6 | discretisation (N vs 2N); asymptote and fit-window stability |
| C7, C7b | calibration reproduces 3.749 eV with 𝒜_ph ∈ [5, 6] eV³; uncalibrated F_Si within 5% of 0.119 |
| C8 | R&K parameters reproduce their MC F_∞ = 0.115 within 1% |
| C9, C10 | Klein algebra (14/5; 54/175 is N-fixed; constrained 0.0394); renewal F = σ²/ε² against an explicit constrained recursion |
| C11 | c₀(θ_ii) at λ_ph → 0 vs Klein's uniform population |
| C12, C13 | spot rows of data/results.json recomputed; validation residual statistics |
| C14, C15 | fits (EF9)–(EF10) against fresh solver runs; (EF11) against a finite difference |
| C16, C17 | Bernoulli thinning (EF12) (sympy); hydrogenic E_x^b estimates |
| C18 | all 15 cited arXiv IDs verified (API records present, IDs match) |

## 8. Literature (arXiv API verified; [FT] = read in full text here)
2610.16949 Nielsen–Fischetti, first-principles ε_eh, Tables I–II, Klein/ABS/Shockley forms [FT] · 0911.1532 Subashiev–Luryi, exact Fano
statistics of random parking [FT] · 2004.11499 Rodrigues et al., Si Fano absolute measurement [FT] · 2004.10709 Ramanathan–Kurinsky [FT] ·
2305.09005 Si F, ε_eh below 1.5 keV [FT] · 2202.03924 Botti et al. [FT] · 1909.05806 Ge F, ε_eh [FT] · 1602.08005 Ge ε_eh(T), Klein form [FT] ·
2311.03902 4H-SiC ε_eh and F compilation [FT] · 2311.05011 diamond and β-Ga₂O₃ [FT] · 2308.03893 GaN [FT] · 1901.07569, 2008.08560, 1910.10716
(material inputs) [FT] · 2411.12320 (4H-SiC 7.8 eV quoted) [FT]. Not used for values: 1308.2886, 2303.07978. Classic sources (Fano 1947,
Shockley 1961, Klein 1968, Alig–Bloom 1975, van Roosbroeck 1965, Lax capture, Onsager) are cited only through the FT quotes above or as
[UNVERIFIED].

---
## Symbols introduced/used
| Symbol | Meaning | Status |
|---|---|---|
| 𝒜_ph | ABS/R&K phonon-to-ii rate constant (eV³; R&K "A") | **new** (A is taken by the mass number) |
| λ_ph ≡ 𝒜_ph/E_g³, w₀ ≡ ω₀/E_g, θ_ii ≡ E_th^{ii}/E_g, a_DOS | reduced rate ratio, phonon/gap ratio, threshold ratio, DOS exponent | **new** |
| R_t(x), p_t(x), ρ_t, Φ_t | rate ratio (EF2); ii branching probability; carrier DOS; three-body phase space | **new** (local to §1) |
| ℋ_<, ℋ_> | residual heat below threshold; phonon heat emitted above threshold (ℋ = ℋ_< + ℋ_>) | **new** |
| 𝒱_<, 𝒱_>, 𝒞_<> | normalised variances and covariance of (EF7) | **new** |
| r̄_c, σ_c | mean and SD of the terminal residual per carrier | **new** |
| F^{ren}, c₀, k₁, k₂ | renewal (final-state) Fano estimate (EF6); λ_ph → 0 limit of ε_eh/E_g; slope and offset of the linear law | **new** |
| N_ii, ε^{cas}, f_cap^{e,h}, f_X, p_diss, p_esc, r_O, r₀, r_C, ℓ_ε, f_imp | ii pair count; cascade pair energy; capture, exciton and escape probabilities and lengths (§4) | **new** |
| (H-EF1)–(H-EF7), (EF1)–(EF14), GAP-EF-C1…C18, V0/V1/V3, GE-1…GE-4, IF-EF1…IF-EF6 | labels (prefix GAP-EF) | labels |
| used unchanged | ω, E_g, ε_eh, F_eh, F_meas, n̄, N_eh, b_N, B_h, E_car, E_th^{ii}, ω₀, ℋ, ℋ_eff, ΔE_X^b, E_x^b, a_x, N_X, N_e^f, E_trap^{pr}, E_pairs^{unp}, 𝔮, m_ind, ϵ_det, ϵ_coll, 𝓃_j, σ_cap, u_car, ℓ^tr, t_pr, ℰ_b, θ_{R-k}, θ_dense, θ_tr^{pr}, θ_X, θ_Z, θ_GW | NOTATION / WP5 / WP7-E |

## Interface flags
| # | Owner | Item | Action |
|---|---|---|---|
| IF-EF1 | WP5 (v4 §6.4(ii); WP5v3-C4b) | 54/175 is the N-fixed variance; the energy-constrained value is 0.0394, an under-prediction; the leading physics of F_eh is 𝒱_> − 2|𝒞_<>| (EF7) | **S**: replace (ii) and (iii) by (EF6)–(EF7); relabel C4b "N fixed"; L23 note |
| IF-EF2 | WP6-v3 §5.2 (yield rows) | the discrete {step, R&K, URF} choice can use (EF3)–(EF4) as the "URF (energy-only)" member; ε_eh prior 𝒩(3.75, 0.05) unchanged; θ_GW and θ_Z on Γ_ii are equivalent to a factor on 𝒜_ph (degenerate, as WP5 §8 says) | adopt; one M-type factor on 𝒜_ph |
| IF-EF3 | WP8-F / WP8-U | §3 table fills the ε_eh/F_eh GAP rows, tagged [E] with bands | consume; prefer FT where present |
| IF-EF4 | WP7-E (IF-E9) | (EF12)–(EF14) and the §4.3 specification | close IF-E9 at the formula level; numbers open (GE-4) |
| IF-EF5 | NOTATION | §Symbols "new" | add rows |
| IF-EF6 | coordinator: SOTA | "ε_eh = k₁E_g + k₂ derived from the cascade: k₁ ≈ 1.6, k₂ ≈ 1.9–2.3 eV (one parameter, 𝒜_ph)" | SOTA row, CLAIMED |

## Proposed LIMITS rows (numbers provisional; the coordinator assigns)
| # | Chain (URF) | Source | Validity | Leading correction | Status |
|---|---|---|---|---|---|
| L39 | (W3) → (H-EF1)–(H-EF4) → (EF3)–(EF4) with a_DOS = 0, a δ hole DOS, θ_ii = 1, no phonons: Rényi parking, F = 0.0510387 | 0911.1532 Eqs. (2), (23) [FT] | narrow valence band, constant conduction DOS | parabolic DOS, phonons | DERIVED (C1) |
| L40 | (EF8) + (K1) θ_ii = 3/2 + (K2) uniform-in-k population → Klein ε = (14/5)E_g + rω₀ | 2610.16949 p.2; 1602.08005 Eq. (3) [FT] | (K2) overstates c₀ by 27–33% at λ_ph → 0 (C11) | exact jamming population (EF3) | DERIVED (truncation) |
| L41 | (EF6): Fano renewal F = σ_h²/ε_eh² (final-state model) | 0911.1532 Eq. (7) [FT] | iid per-pair energies | sibling correlations (EF7): ×0.2–×1.2 | DERIVED (C10); not a bound |
| L42 | (EF3)–(EF4) with a_DOS = ½, θ_ii = 1, B_h, one 𝒜_ph → R&K/ABS: F_∞ = 0.115 (Si, 300 K); ε_eh ≈ 2.73E_g + 0.55 empirical | 2004.10709 p.6; 2610.16949 pp.2–3 [FT] | universal 𝒜_ph | per-material 𝒜_ph (C, GaN +14–16%) | DERIVED; CROSS-CHECKED (C8) |
| L43 | (EF9) → ε_eh ≈ 1.61E_g + 2.33(𝒜_phω₀^{0.96})^{0.24}E_g^{0.05} ≈ k₁E_g + k₂ | 2610.16949 p.2 (1.54E_g + 1.89) [FT] | λ_ph ∈ [0.003, 100], w₀ ∈ [0.01, 0.1] | (H-EF5), (H-EF1) | observed (fit of a derived model) |
| L23 (✎) | add: F_eh = 𝒱_< + 𝒱_> + 2𝒞_<> (EF7), computed; Si 0.114 predicted vs 0.119 ± 0.002 | 2004.11499 [FT] | (H-EF1)–(H-EF7) | θ_{R-k}; T beyond E_g(T) | DERIVED (C4, C7b) |
