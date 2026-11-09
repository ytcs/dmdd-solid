# R16 / GAP-EF-v2: the pair-creation energy ε_eh and the Fano factor F_eh from the cascade (corrected, standalone)

Agent GAP-EF-v2, brief briefs/R16/REV-GAP-EF.md. This return **replaces** returns/R14/GAP-EF.md (v1), which stays untouched as the record. It
absorbs every item of referees/R14/REF-GAP-EF-A.md (K1–K14) and referees/R14/REF-GAP-EF-B.md (owed items 1–9); the closing table maps each
item to its resolution. **User directive applied:** §1, the derivation of ε_eh and F_eh, is written as a textbook passage: hypotheses, steps,
limits, leading corrections. §2–§5 (validation, predictions, IF-E9, ab initio specification) are secondary.

Inputs read: returns/R14/GAP-EF.md, both R14 referee reports, returns/R13/WP5-v4.md §1.2, §6.4 and §R13.1 (K1, A-1), returns/R12/WP7-E-v3.md
(E1-W4, E12, IF-E9) through WP5-v4's quotes, returns/R16/EF-LIT.md (used in §2), returns/R13/WP8-U-table.csv (prediction inputs, as in v1),
LIMITS.md, CONVENTIONS.md (§12, §14, R13 amendments), NOTATION.md. **No first-principles numerics and no Monte Carlo were run.** All numbers
come from deterministic quadrature of exact moment recursions in **code/GAP-EF-v2/** (a copy of code/GAP-EF/, fixed and extended):
`cascade.py` (solver), `model.py` (grid and calibration; grid bug fixed), `predict.py` → `data/results.json` (rerun in full, 11–23 min),
`scan.py` → `data/scan.json` (v1 output, unchanged; see §1.8), and `checks.py`: **28 checks, 28/28 PASS in ≈ 15 s**, cited GAP-EF-v2-Cn.
v1 checks are cited GAP-EF-Cn. Tags follow CONVENTIONS §12. **Literature:** the v1 extracts in literature/papers-GAP-EF/ plus one new paper,
1902.02687 (β-Ga₂O₃ phonons), fetched with lit.py into literature/papers-GAP-EF-v2/ (PDF deleted, `.txt` and API record kept). Page numbers
are PDF pages. **Status:** solver CROSS-CHECKED (two independent routes: the exact random-parking solution, GAP-EF-v2-C1/GAP-EF-v2-C2, and the R&K
Monte Carlo and its fitted planes, Eqs. (12)–(13), GAP-EF-v2-C8; two referees reproduced the recursions independently, REF-A R1, REF-B R1); material numbers [E].

---
## 0. Results at a glance
| # | Item | Result | Tag |
|---|---|---|---|
| 1 | Reduction of WP5 (W3) | Exact first and second moment recursions (EF3)–(EF4) of the energy-only cascade, solved by quadrature. Discretisation ≤ 0.05% (Si), 0.12% (C) (GAP-EF-v2-C5); asymptote stable to 10⁻⁴ (GAP-EF-v2-C6) | D given (H-EF1)–(H-EF7) |
| 2 | Energy constraint | With ω fixed and iid per-pair costs, F = Var(per-pair heat)/ε_eh², **not** /E_g² (EF6). WP5-v4 §6.4(ii)'s 54/175 ≈ 0.31 is the N-fixed value; the constrained value of the same model is 27/686 = **0.0394**, 3× *below* the data (GAP-EF-v2-C9, GAP-EF-v2-C10) | D |
| 3 | The uncomputed term | F_eh = 𝒱_< + 𝒱_> + 2𝒞_<> (EF7). Si: **0.091 + 0.288 − 0.265 = 0.114**; 2𝒞_<> computed by two routes (GAP-EF-v2-C4b). The dominant anticorrelation is between the residual heat ℋ_< and the above-threshold phonon heat ℋ_> along each carrier line; it cancels 92% of 𝒱_> | D (exact in the model) |
| 4 | Final-state (renewal) model | **A lower bound on F_eh in every computed case**: F^{ren}/F_eh = 0.87 (RPP), 0.70 and 0.84 (no phonons, θ_ii = 1, 3/2), 0.42 (Si, θ_ii = 3/2), 0.19 (Si), 0.12 (Ge) (GAP-EF-v2-C19). Not proven in general | D (cases); [C] (general) |
| 5 | Limits | Rényi/RPP exactly (F = 0.05104, GAP-EF-v2-C1; renewal value 0.0443995 vs the corrected 0911.1532 value 0.0443977, GAP-EF-v2-C2). Klein's 2.8E_g + rω₀ = identity (EF8) + threshold 3/2 E_g + uniform population; (K2) **overstates c₀ by 39% (θ_ii = 1) and 36% (θ_ii = 3/2)** (GAP-EF-v2-C11). R&K: F_∞ 0.1145 vs 0.115, **agreement at their ≈ 2% MC scatter**, plus five points and three slopes of their fitted planes, Eqs. (12)–(13) (GAP-EF-v2-C8) | D |
| 6 | One calibrated parameter | 𝒜_ph = 5.595 eV³, fixed by Si ε_eh = 3.749 eV alone (ABS fit 5.2). **F_Si = 0.1138 is an untuned model value equal to R&K's published model value (0.115), nearly 𝒜_ph-independent (±10% in 𝒜_ph → ±0.7% in F), and 2.6σ below 0.119 ± 0.002.** It is not independent support for the model (GAP-EF-v2-C7b) | D/E |
| 7 | Closed form | ε_eh/E_g = 1.613 + 2.327(λ_ph w_ph^{0.964})^{0.2395} (0.52% max) is an **observed fit** of the model. In eV it reads ε_eh ≈ 1.61E_g + k₂ with k₂ = 2.33(𝒜_phω₀^{0.96})^{0.24}E_g^{0.05}, and **k₂ is not a constant: it spans 1.2–2.5 eV** over the survivors (1.5–2.5 eV inside the fit domain; GAP-EF-v2-C25). This agrees in form with the empirical 1.54E_g + 1.89; it is not a derivation of it | observed |
| 8 | Validation | Primary set (7 named measurements, **GaN at EBIC 9.59 eV**): residuals −6.5% … +24.6%, mean +8.2%, rms **12.3%**. Without GaN: rms 8.7%. β-Ga₂O₃ (EBIC + MC estimate 15.6 eV) **included** in an extended set: +56%, rms 23%. EF-LIT rows (Al₂O₃ 27 eV vendor value, CaWO₄ 29.8 eV model value) shown, +63% and +179%, not measurements (GAP-EF-v2-C13) | E |
| 9 | 4H-SiC F tension | Model F = 0.091–0.093. The two measurements disagree: 0.1 (2011 linewidth) vs ≤ 0.04 (2005 upper limit). **The 2005 limit is below every F this model class produced (minimum 0.0510, RPP; GAP-EF-v2-C22)**; if it holds, (H-EF3)/(H-EF1) fail for 4H-SiC | E; stated conflict |
| 10 | Predictions, 27 materials | §3 table, rerun after the CsI grid fix (CsI ε_eh 11.46 → **11.21 eV**, −2.2%; GAP-EF-v2-C20). Bands now carry the +24.6% GaN residual | E |
| 11 | IF-E9 | (EF12) thinning **requires an energy-independent capture probability**; general law (EF12′) otherwise (GAP-EF-v2-C16, GAP-EF-v2-C16b). (EF13) made consistent with WP5-v4 (W4′): **ℋ_eff unchanged, bare heat +N_XE_x^b, plus a variance term** (GAP-EF-v2-C21) | D |
| 12 | Owed correction | IF-EF1 to WP5-v4 §6.4(ii)–(iii), restated in the Interface flags | S |

---
## 1. Theory: ε_eh and F_eh as moments of the cascade

### 1.1 The question and the exact starting point
A deposit ω creates N_eh electron–hole pairs. Under the conditions of WP5 (W4) — no capture, no excitons and no bias work before t_pr, and
E_st = E_esc = 0 — every event obeys the energy ledger ω = N_ehE_g + ℋ, where ℋ is all the energy that ends as heat. Taking the mean and the
variance of this identity at fixed ω gives

  ε_eh ≡ ω/n̄,   F_eh ≡ Var N_eh/n̄ = Var ℋ/(E_g² n̄)   (exact; WP5 (W14), WP5v3-C3).                                                                     (EF1)

F_eh is therefore a property of the heat. The whole task of this section is to compute Var ℋ, including the correlations that the energy
ledger forces between its parts. In the reduced cascade defined below, ℋ splits into two parts:
- ℋ_<, the residual kinetic energy that each carrier holds when it falls below the impact-ionization (ii) threshold for good;
- ℋ_>, the phonon energy emitted while the carrier is still above threshold.

WP5-v4 §6.4 wrote F_eh = [Var(Σ residuals, with the energy-constraint anticorrelation) + Var(phonon)]/(E_g² n̄) and left the first term
uncomputed. Two naive evaluations are available and both fail:
- (a) *Independent residuals with N held fixed.* Var ℋ = n̄·2σ_res², with σ_res² the per-carrier residual variance, gives F = 2σ_res²/E_g².
  In the Klein distribution this is WP5v3-C4b's 54/175. It treats N as fixed, but at fixed ω the pair number N is itself determined by ℋ.
- (b) *Phonon shot noise alone* (WP5-v4 §6.4(iii)). This drops the residual term altogether.

What is needed is the joint law of (N, ℋ_<, ℋ_>) at fixed ω. §1.2–§1.6 obtain its first two moments exactly within a controlled reduction of
(W3).

### 1.2 Hypotheses (H-EF1)–(H-EF7)
- **(H-EF1) Energy-only reduction.** WP5 (W7) under (R-k) or (R-k′): after the first collision a carrier's state is its type t ∈ {e, h} and its
  kinetic energy x ≥ 0 above its band edge. Momentum is averaged out. The error is θ_{R-k}, not quantified here (WP5 gap R2).
- **(H-EF2) Independent siblings, Markov, minimal solution, termination.** WP5 (B1), (B2), (H-t), (H-m). (B2), the independence of sibling
  subtrees, is controlled only for small seeds (θ_dense).
- **(H-EF3) Random-k ii kernel.** This is the Alig–Bloom–Struck "scattering-rate" assumption of constant matrix elements [FT 2610.16949 pp.2–3].
  For x ≥ E_th^{ii} ≡ θ_iiE_g, an ii event of a carrier of type t produces (t, x₁) + (t, x₂) + (t̄, x₃) with x₁ + x₂ + x₃ = x − E_g. The
  three energies have the joint density ρ_t(x₁)ρ_t(x₂)ρ_t̄(x₃)/𝔓_t(x − E_g), where 𝔓_t ≡ ρ_t * ρ_t * ρ_t̄ is the three-body phase space (a
  threefold convolution). The DOS shape is ρ_t(x) ∝ x^{a_DOS}, optionally truncated at the hole bandwidth B_h.
- **(H-EF4) Competing phonon channel.** One effective optical mode ω₀ (= ω_LO, or ω_max where only ω_max is tabulated); emission only, T ≪ ω₀.
  The ratio of the phonon rate to the ii rate is

  R_t(x) ≡ Γ^{ph}_t/Γ^{ii}_t = λ_ph ρ_t(x − ω₀)/𝔓_t(x − E_g),   λ_ph ≡ 𝒜_ph/E_g³,   w_ph ≡ ω₀/E_g.                                                  (EF2)

  For a_DOS = ½, 𝔓(y) = Γ(3/2)³y^{7/2}/Γ(9/2) = (2π/105)y^{7/2}, so (EF2) is R&K Eq. (8), Γ_ph/Γ_eh = A(105/2π)(E − ħω₀)^{1/2}/(E − E_g)^{7/2},
  with 𝒜_ph = their A [FT 2004.10709 p.3; checked by both referees]. 𝒜_ph has units eV³ (R&K print "eV²"; WP5-v4 §6.2 discrepancy (1)).
- **(H-EF5) Universal 𝒜_ph.** One 𝒜_ph serves all materials (the ABS hypothesis), calibrated once on Si ε_eh. Its failure is not modelled; it is
  measured by the validation residuals of §2.
- **(H-EF6) Temperature enters only through E_g(T).** Phonon absorption is neglected (n_B(ω₀) ≈ 4 × 10⁻³ for Ge at 77 K). WP5 §6.2 says this is
  incomplete.
- **(H-EF7) No plasmon channel.** By WP5 Theorem C(a) the plasmon decays into the same e–h weight. R&K add an explicit plasmon channel and report
  "no impact on the ionization yield by adding or removing this mechanism" [FT 2004.10709 p.4]; that statement concerns the yield, not F.
  **The effect of the plasmon channel on F_eh is UNRESOLVED.** The net agreement with R&K's F_∞ (§1.7(c)) is the sum of all model differences
  (plasmons, R&K's first split and hole re-split) and lies inside their ≈ 2% Monte Carlo scatter, so it cannot isolate the plasmon term.

### 1.3 The moment equations [D]
Consider an additive deposit Y that collects d_ii at each ii event, d_ph at each phonon emission and d_<(x) at termination. Let
m_t(x) = E[Y | t, x], s_t(x) = E[Y² | t, x] and p_t(x) = 1/(1 + R_t(x)), the probability that the next collision is an ii event.

*Step 1 (first-step analysis).* Condition on the first collision of the carrier. With probability p_t it ionizes into three independent
subtrees (H-EF2) with energies (x₁, x₂, x₃) drawn from (H-EF3); with probability 1 − p_t it emits a phonon and continues at x − ω₀.

*Step 2 (factorisation).* Write Y = d_ii + Y₁ + Y₂ + Y₃ after an ii event. Independence of the subtrees gives E[Y_iY_j] = m m for i ≠ j at
the drawn energies. Averaging over (H-EF3) with P_t ≡ ρ_tm_t, the single and pair sums are

  ⟨Y₁ + Y₂ + Y₃⟩ = [2P_t * ρ_t * ρ_t̄ + ρ_t * ρ_t * P_t̄](y)/𝔓_t(y),   ⟨Σ_{i<j}m_im_j⟩ = [P_t * P_t * ρ_t̄ + 2P_t * ρ_t * P_t̄](y)/𝔓_t(y),   y = x − E_g.

*Step 3 (the recursions).* For x ≥ θ_iiE_g,

  m_t(x) = p_t [d_ii + ⟨m_t(x₁) + m_t(x₂) + m_t̄(x₃)⟩] + (1 − p_t)[d_ph + m_t(x − ω₀)],                                                        (EF3)
  s_t(x) = p_t [d_ii² + 2d_ii⟨ΣY_i⟩ + ⟨Σs_i⟩ + 2⟨Σ_{i<j}m_im_j⟩] + (1 − p_t)[d_ph² + 2d_ph m_t(x − ω₀) + s_t(x − ω₀)].                        (EF4)

Below threshold, m = d_<(x) and s = d_<². Three choices of deposit give the three quantities of interest: Y = N (d_ii = 1), Y = ℋ_< (d_< = x)
and Y = ℋ_> (d_ph = ω₀). Two more give independent routes to their covariance: Y = ℋ_< + ℋ_> and Y = ℋ_< − ℋ_> (d_ph = −ω₀).

*Step 4 (solution).* Every term on the right of (EF3)–(EF4) is a one-dimensional convolution of quantities already known at lower energy, so a
single upward sweep in x solves the system at cost O(K²) on a K-point grid. The grid is chosen with ω₀ on it: n_w steps with
|n_wh/w_ph − 1| < 1%, **now enforced** (model.grid raises otherwise; v1 silently ran CsI with 2.04 w_ph, REF-B 2.7; GAP-EF-v2-C20).

*Numerical facts.* The discrete kernel conserves energy, x = N E_g + ℋ_< + ℋ_> on every path, to 8.6 × 10⁻¹⁶ (GAP-EF-v2-C3). Var N from the N
recursion equals Var(ℋ_< + ℋ_>)/E_g² from the heat recursion to 10⁻⁹ (GAP-EF-v2-C4a): this is (EF1) verified numerically. (GAP-EF-v2-C3–GAP-EF-v2-C6 use B_h = ∞; the
calibration uses B_h = 12 eV; the difference in Si is ≤ 10⁻⁴, REF-B R4.)

### 1.4 Asymptotic linearity [D, sketch]
For x ≫ E_g the solutions become n̄ = ω/ε_eh + b_N and Var N = F_ehω/ε_eh + O(1). This is WP5 §6.4, by the key renewal theorem under (r1)–(r3).
Hypothesis (r2), non-lattice increments, fails on the {E_g, ω₀} lattice; the periodic remainder averages out in a linear fit over [X/2, X].
- The slopes change by < 10⁻⁴ between X = 40E_g and 80E_g and between fit windows (Si, GAP-EF-v2-C6).
- For λ_ph > 5 (gaps ≲ 1 eV) the asymptote is slower: predict.py uses X = 60E_g there (X = 25 shifts F by 4% for InSb).
- scan.py (the fits of §1.8) used X = 25 throughout. At its edge (λ_ph = 100, w_ph = 0.05) that biases F by −1.1% and ε by −0.24% (GAP-EF-v2-C24), inside
  the fits' stated maxima; v1's comment "asymptote reached at X = 25" was wrong and is corrected in the code.
- By-product [E]: for Si, b_N = 0.345 for a one-sided seed (all energy on the electron) and ≈ 0 for a symmetric seed; b_N depends on the seed
  (WP5 VER-WP5-A N2).

### 1.5 The energy constraint: why ε_eh, not E_g, sits in the denominator [D]
*Hypothesis (R-iid).* Model the cascade as a renewal sequence: pair i costs E_g + ℋ_i, where ℋ_i is the heat attributed to that pair, and the
ℋ_i are **independent and identically distributed**, with mean ε_eh − E_g and variance σ_pair². Pairs are produced until ω is spent.

*Step.* The renewal theorem for iid costs c_i with mean ε and variance σ² gives Var N ≃ ωσ²/ε³ (Fano 1947; Feller; 0911.1532 Eqs. (5)–(7)
[FT pp.2–3]). With σ² = σ_pair² and (EF1):

  F^{ren} = σ_pair²/ε_eh²,   equivalently   Var ℋ = n̄ σ_pair² (E_g/ε_eh)².                                                                         (EF6)

*Reading.* At fixed ω the fluctuations of ℋ and of N are locked together: a pair that costs more heat leaves less energy for later pairs. This
energy-constraint anticorrelation multiplies the naive N-fixed variance n̄σ_pair² by (E_g/ε_eh)². GAP-EF-v2-C10 checks (EF6) against an explicit
renewal recursion with the exact energy constraint (0.0426 vs 0.0426).

*Application to Klein's population.* Uniform-in-k residuals (√x on [0, θ_iiE_g]), two carriers per pair, θ_ii = 3/2: ⟨x⟩ = (3/5)θ_iiE_g,
Var x = (12/175)θ_ii²E_g², 2σ_res² = (54/175)E_g², ε = (14/5)E_g, and F^{ren} = (54/175)(5/14)² = **27/686 = 0.0394**, not 0.31 (GAP-EF-v2-C9). The
N-fixed value 0.31 is 2.6× the data; the constrained value is 3× *below* it. **Correct statement:** WP5-v4 §6.4(ii) is an N-fixed artefact,
and with the constraint the independent-residual model *under*-predicts F_eh. The correlations it omits must therefore *raise* F, and §1.6
shows which ones do. This is the owed correction IF-EF1.

*What the code calls F^{ren}.* In the cascade solver the renewal estimate is built from the computed terminal statistics, one electron and one
hole per pair, plus Poisson phonon noise:

  F^{ren} ≡ [σ_res,e² + σ_res,h² + ω₀⟨ℋ_>⟩/n̄]/ε_eh²,                                                                                             (EF6′)

i.e. (EF6) with σ_pair² replaced by the variance of uncorrelated per-carrier residuals plus shot-noise phonon heat (REF-B 2.1).

### 1.6 The exact decomposition and the computed anticorrelation term [D within (H-EF1)–(H-EF7)]
*Step.* Write ℋ = ℋ_< + ℋ_> in (EF1) and expand the variance:

  F_eh = 𝒱_< + 𝒱_> + 2𝒞_<>,   𝒱_≶ ≡ Var ℋ_≶/(E_g² n̄),   2𝒞_<> ≡ 2Cov(ℋ_<, ℋ_>)/(E_g² n̄).                                                    (EF7)

(EF7) is an identity. Its content is that every term is computed: 𝒱_< and 𝒱_> by their own recursions, 2𝒞_<> by the ℋ_< − ℋ_> recursion,
and the result agrees with the remainder Var ℋ − 𝒱_< − 𝒱_> to 10⁻⁹ (GAP-EF-v2-C4b; REF-A R1 reproduced the full 3×3 moment matrix independently to 10⁻¹³).

| case (a_DOS = ½ unless stated) | ε_eh/E_g | 𝒱_< | 𝒱_> | 2𝒞_<> | F_eh | F^{ren} (EF6′) | F^{ren}/F_eh | r̄_c/E_g |
|---|---|---|---|---|---|---|---|---|
| RPP: a_DOS = 0, δ hole DOS, θ_ii = 1, no phonons | 1.3376 | 0.0510 | 0 | 0 | **0.0510** | 0.0444 | 0.87 | 0.169 |
| λ_ph → 0, θ_ii = 1 | 1.5853 | 0.0813 | 0 | −0.0001 | **0.0811** | 0.0566 | 0.70 | 0.293 |
| λ_ph → 0, θ_ii = 3/2 | 2.0562 | 0.0826 | 0 | 0.0000 | **0.0826** | 0.0692 | 0.84 | 0.528 |
| Si V0 (λ_ph = 3.55, w_ph = 0.054, θ_ii = 1) | 3.221 | 0.0910 | 0.2876 | −0.2648 | **0.1138** | 0.0219 | 0.19 | 0.715 |
| Si V1 (θ_ii = 3/2, re-calibrated) | 3.221 | 0.1013 | 0.1776 | −0.1659 | **0.1130** | 0.0473 | 0.42 | 0.900 |
| Si V3 (a_DOS = 1, re-calibrated) | 3.221 | 0.0839 | 0.2767 | −0.2583 | **0.1023** | 0.0189 | 0.18 | 0.745 |
| Ge (λ_ph = 14.4, w_ph = 0.051, 77 K) | 3.827 | 0.1451 | 0.4440 | −0.4644 | **0.1247** | 0.0153 | 0.12 | 0.774 |

The first three rows are Richardson-extrapolated on one grid pair (h = 0.01, 0.005) in **every** column, so they close the identity (EF8) below,
ε/E_g = 1 + 2r̄_c, to 10⁻⁴ (GAP-EF-v2-C23). (v1 mixed an extrapolated ε with an unextrapolated r̄_c; REF-B 2.1.) r̄_c is the mean terminal residual per carrier.

What the table shows:
- **The leading term is not the residual variance.** When phonons compete (Si, Ge) the largest piece is 𝒱_>, the variance of the
  above-threshold phonon heat. It is far above Poisson shot noise (Si: 0.288 against w_ph(ε/E_g − 1 − 2r̄_c) = 0.043), because the number of
  phonons a carrier emits before it ionizes is a broad, geometric-like random variable.
- **The anticorrelation is between ℋ_> and ℋ_< along a carrier line.** A carrier that loses more energy to phonons near threshold reaches
  termination with a smaller residual, or ionizes later at lower energy. Energy conservation along each line enforces this: 2𝒞_<> removes 92%
  of 𝒱_> in Si (0.2648/0.2876) and more than all of it in Ge. It is not, as WP5-v4 §6.4(ii) guessed, an anticorrelation between sibling residuals.
- **Sibling correlations raise F.** Without phonons ℋ_> ≡ 0, so 𝒞_<> vanishes trivially (it does not measure sibling correlations; v1's wording
  was wrong, REF-A a.3). The sibling effect is the gap F_eh − F^{ren}: +0.025 at θ_ii = 1 and +0.013 at 3/2, both **positive**. The no-phonon
  value F_eh = 0.081 is pure partition noise: the exact jamming distribution of residuals, strongly peaked at x → 0 as in Rényi parking.
- **The final-state model is a lower bound in every computed case.** F^{ren}/F_eh ∈ [0.12, 0.87] over the seven cases (GAP-EF-v2-C19); the renewal
  model misses F_eh by up to 8× (Ge) when phonons compete. This agrees with 0911.1532, which states that the uncorrelated final-state model
  "gives only a lower-bound estimate to F" [FT p.2]. (v1's "not a bound in either direction" and "over-predicts in the RPP limit" were a sign
  error and are withdrawn, REF-A K1, REF-B item 1. 0911.1532's F_nnp = 0.0521 is a different, nearest-neighbour-corrected estimate.) Whether
  F^{ren} ≤ F_eh holds for every kernel of the class is **not proven** [C].
- **The net F_eh is a small difference of large terms.** That is why F^{ren}, which keeps one-particle residual statistics and Poisson phonons,
  misses it.

### 1.7 Limits recovered
**(a) Random parking (Rényi).** Take a_DOS = 0 for electrons, a δ-function hole DOS (narrow valence band), θ_ii = 1 and no phonons. Then the
ii event of (H-EF3) places the two electron residuals uniformly on [0, x − E_g], and the cascade is Rényi's random parking of unit cars.
(EF3)–(EF4) give coverage 1/ε = 0.74760 and F = 0.05104 after Richardson extrapolation, against the exact 0.7475987 and 0.0510387
[FT 0911.1532 Eq. (23) p.4, Eq. (2) p.2] (GAP-EF-v2-C1). The renewal estimate of the same limit is F^{ren} = 0.0443995. 0911.1532 prints
F_unc = 0.0439766 (p.4); that is a transposition typo for **0.0443977**, as REF-A b.1 showed by evaluating the paper's own G(x) and as the paper's
own F_nnp = F_unc + δF_nnp = 0.0443977 + 0.007685 = 0.05208 (p.5) requires. GAP-EF-v2-C2 now targets 0.0443977 with tolerance 10⁻⁵ (agreement 1.8 × 10⁻⁶).

**(b) Shockley/Klein identity.** *Condition:* exactly two terminal carriers per pair. This holds for a pair seed because the seed's sibling sits at
the band edge (solver: 2.000 carriers per pair in every case); for a seed that is not a pair the identity has an O(1/n̄) defect. Under this
condition, energy conservation gives exactly

  ε_eh = E_g + 2r̄_c + ⟨ℋ_>⟩/n̄   (≡ E_g + 2r̄_c + rω₀, r = phonons emitted above threshold per pair).                                          (EF8)

This is Shockley's ε = 2E_f + E_i + rE_R [FT 2610.16949 Eq. (1) p.2] with E_i → E_g in the pair term and the threshold entering through r̄_c.
**Klein's ε = (14/5)E_g + rω₀** [FT 2610.16949 p.2; FT 1602.08005 Eq. (3) p.6] follows from (EF8) under two truncations:
- (K1) θ_ii = 3/2 (parabolic bands, equal masses, momentum conserved);
- (K2) a uniform-in-k terminal population below threshold, r̄_c = (3/5)θ_iiE_g (GAP-EF-v2-C9).

*Leading correction (size of (K2)).* At λ_ph → 0 the exact c₀ ≡ ε_eh/E_g is 1.585 (θ_ii = 1) and 2.056 (θ_ii = 3/2), against (K2)'s 2.2 and 2.8:
**(K2) overstates c₀ by 39% and 36%** (equivalently, the exact values lie 28% and 27% below (K2)) (GAP-EF-v2-C11). The reason is in r̄_c: the true jamming
population sits at low x, r̄_c = 0.293E_g and 0.528E_g, so (K2)'s 0.6θ_iiE_g overstates r̄_c by +105% (θ_ii = 1) and +70% (θ_ii = 3/2). With
phonons the comparison reverses: carriers stall just above threshold and r̄_c rises (Si 0.715E_g), so (K2)'s 0.6E_g at θ_ii = 1 *under*states
r̄_c by 16%. (v1's "27–33%" and "−20% to +40%" had no consistent definition and are replaced by these numbers.) *Attribution:* whether Klein
himself used (K2) is **UNRESOLVED** (no Klein full text; 2610.16949 p.2 attributes "uniform population, E_f = 0.6E_i" to Shockley/ABS).

**(c) R&K / ABS.** θ_ii = 1, a_DOS = ½, B_h = 12 eV, 𝒜_ph = 5.2 eV³, E_g = 1.124 eV, ω₀ = 63 meV give F_∞ = 0.1145; R&K's Monte Carlo gives
0.115 [FT 2004.10709 p.6]. R&K state that their F is "constant at 2% level" across scans and attribute the point scatter to MC statistics
(p.6), so **the agreement is at their ≈ 2% scatter**, not at 0.5%. The stronger cross-check is against R&K's own fitted planes, Eq. (12)
ε = 1.7E_g + 0.084A + 1.3 and Eq. (13) F = −0.028E_g + 0.0015A + 0.14 (p.6), over A ∈ {3, 5.2, 7} and E_g ∈ {1.0, 1.124, 1.2} (GAP-EF-v2-C8):

| quantity | solver | R&K Eqs. (12)–(13) |
|---|---|---|
| ε at (A, E_g) = (3, 1.124) / (5.2, 1.124) / (7, 1.124) | 3.425 / 3.651 / 3.787 eV | 3.463 / 3.648 / 3.799 eV |
| F at the same points | 0.1103 / 0.1145 / 0.1168 | 0.1130 / 0.1163 / 0.1190 |
| ∂ε/∂A (secant over A ∈ [3, 7]) | 0.090 | 0.084 |
| ∂F/∂A (secant) | 0.0016 | 0.0015 |
| ∂ε/∂E_g (secant over E_g ∈ [1.0, 1.2]) | 1.69 | 1.7 |

All five points agree to ≤ 1.1% in ε and ≤ 2.4% in F. This is an independent route (event sampling against deterministic quadrature), so the
solver is CROSS-CHECKED, at ≈ 2%.

**(d) Measured Si and Ge Fano factors.** With 𝒜_ph fixed by Si ε_eh only:
- Si: F_Si = 0.1138 against 0.119 ± 0.002 at 5.9 keV, 123 K [FT 2004.11499 p.1, p.5]; Lowe's 0.118 ± 0.004 is quoted on p.5. The model value is
  **2.6σ below** the measurement (no model error assigned). It is **untuned**, but it is **not independent support**, for three reasons: it is
  R&K's published model value (0.115, "not tuned for a specific Fano factor, and is thus predictive", [FT 2004.10709 p.6]) reproduced; it hardly
  depends on the one calibrated parameter (∂F/∂𝒜_ph = 0.0014 eV⁻³, so ±10% in 𝒜_ph moves F by ±0.7%, GAP-EF-v2-C7b); and it is set by the structural choices
  (θ_ii, a_DOS, B_h, ω₀), whose spread (a_DOS = 1: −10%) is larger than the data–model gap. Over the scan domain of §1.8, F ∈ [0.083, 0.142] (0.081 at λ_ph → 0),
  so a value in 0.10–0.13 is generic for a semiconductor with λ_ph ~ 1–10.
- Ge: F_Ge = 0.125 (77 K), inside the reported 0.06–0.13 [FT 1909.05806 p.14, a secondary quote of five experiments] and 18% above that paper's
  model value 0.106.

### 1.8 Closed forms (observed)
For θ_ii = 1 and a_DOS = ½, a 60-point scan over λ_ph ∈ [0.003, 100] and w_ph ∈ [0.01, 0.1] (scan.py, X = 25; GAP-EF-v2-C14) is fitted by

  ε_eh/E_g = 1.613 + 2.327 (λ_ph w_ph^{0.964})^{0.2395}   (max 0.52%, rms 0.19%),                                                                (EF9)
  F_eh = 0.02347 + 0.03643 e − 0.002711 e² + 0.01653 w_ph,   e ≡ ε_eh/E_g   (max 2.3%, rms 0.8%).                                              (EF10)

Tag: **observed** (CONVENTIONS §12, R13 amendment): verified on the scan, not derived. Domain: the scan box; rows with w_ph < 0.01 (LiF, NaF, CaF₂,
MgF₂, NaCl, NaI, CsI) and λ_ph > 100 (InSb, PbS, PbTe, PbSe) are outside it, and their §3 values come from the solver, not from (EF9)–(EF10).
(EF10) is not "a quadratic in e" alone: it has a w_ph term, and it turns down for e > 6.7, so it must not be extrapolated.

Substituting λ_ph = 𝒜_ph/E_g³ into (EF9) gives E_g^{1−(3+γ)β} = E_g^{0.05}, so

  ε_eh ≈ 1.61E_g + k₂(E_g, ω₀),   k₂ = 2.33(𝒜_phω₀^{0.96})^{0.24}E_g^{0.05}   (𝒜_ph in eV³, energies in eV).

k₂ is not a constant: over the survivors of §3 it spans **1.2 eV (PbTe, ω₀ = 13.5 meV; CsI 1.3 eV) to 2.5 eV (SiO₂ and C, ω₀ = 149–163 meV)**,
and 1.5–2.5 eV over the rows inside the fit domain (GAP-EF-v2-C25); it is 1.86 eV at ω₀ = 63 meV and E_g = 1.16 eV. (REF-B quoted 1.2–2.3 eV and REF-A
1.2–2.6 eV; the E_g^{0.05} factor lifts the large-gap, stiff-lattice rows to 2.5 eV.) **Reading:** the observed fit agrees in form with the empirical 1.54E_g + 1.89 [FT 2610.16949 p.2] for ω₀ ≳ 60 meV. It is not a
derivation of that law: the fit is of a model with one calibrated parameter, the model under-predicts C and GaN, which set the empirical slope at
large E_g, and Nielsen–Fischetti note that ε(E_g) "is not linear" [FT 2610.16949 p.3]. Klein's slope 2.8 overshoots wide-gap materials
[FT 2311.05011 p.5: Klein gives 15.92 eV for diamond against measured ≈ 13], consistently with (K2) above.

The effective-gap sensitivity at fixed 𝒜_ph and ω₀ follows from (EF9) (tag **observed**, a derivative of a fit):

  dε_eh/dE_g = c₀′ + c₁u(1 − 3β − γβ),   u = (λ_ph w_ph^γ)^β,   (c₀′, c₁, γ, β) = (1.613, 2.327, 0.964, 0.2395)   [Si: 1.69; solver FD 1.78, GAP-EF-v2-C15].   (EF11)

R&K's Eq. (12) slope 1.7 agrees.

### 1.9 Truncation budget and leading corrections
| Item | Size | Status |
|---|---|---|
| discretisation (ω₀ on grid; N vs 2N) | ε 0.05%, F 0.05% (Si); ε 0.12% (C); 0.18% (SiO₂) | quantified (GAP-EF-v2-C5; REF-B R6) |
| ω₀ off the grid | now < 1% in w_ph for every row (v1: +104% for CsI → +2.2% in ε) | enforced (GAP-EF-v2-C20) |
| asymptote, predictions | < 10⁻⁴ (λ_ph ≲ 5, X = 25); X = 60 for λ_ph > 5 | quantified (GAP-EF-v2-C6) |
| asymptote, fits (scan at X = 25) | edge bias −1.1% F, −0.24% ε at λ_ph = 100; inside the fit maxima | quantified (GAP-EF-v2-C24) |
| θ_ii ∈ [1, 3/2] (re-calibrated) | ε: 0 to +10%; F: −1 to −3% | quantified (§3 band) |
| a_DOS ∈ [½, 1] (re-calibrated) | ε: up to +8%; F_Si: −10% | quantified (§3 band) |
| narrow valence band B_h = E_g | F → 0.068; ε +4–7% (ionic) | quantified (§3 band) |
| fits (EF9)–(EF10) | 0.52% / 2.3% max | quantified (GAP-EF-v2-C14) |
| calibration at E_g(110 K) for a 123 K datum | ≲ 0.1% in ε [E] (dε/dE_g ≈ 1.8) | estimated |
| (H-EF1) energy-only reduction | — | **not quantified**: θ_{R-k}, WP5 R2 |
| (H-EF5) universal 𝒜_ph | ε residual −6.5% … +24.6% (§2) | absorbed into the validation band |
| (H-EF7) plasmon channel, effect on F | — | **UNRESOLVED** |
| (H-EF6) T only via E_g(T); (H-EF2) (B2) at ≳ keV | — | not quantified (WP5 §6.2; θ_dense) |

### 1.10 What is derived and what is not
- **Derived [D]** given (H-EF1)–(H-EF7): (EF1), (EF3)–(EF4), (EF7) with all three terms computed, (EF8) given two terminal carriers per pair,
  (EF6) given (R-iid), and the limits (a)–(b).
- **Computed, not proven:** F^{ren} ≤ F_eh (seven cases, [C] in general); the model floor F ≥ 0.051 (§2, GAP-EF-v2-C22).
- **Observed:** (EF9)–(EF11) and the linear form with k₂ ∈ [1.2, 2.5] eV.
- **Not independent evidence:** F_Si = 0.114 (= R&K's model value; 2.6σ low).

---
## 2. Data compilation and validation
**The calibration (the only fitted parameter).** 𝒜_ph is fitted to Si ε_eh = 3.749 ± 0.001 eV (123 K, 5.9 keV) [FT 2004.11499 p.1, p.5], with
E_g = 1.164 eV (110 K) [FT 2004.10709 Table I p.5], ω₀ = 63 meV [FT 2004.10709 p.3] and B_h = 12 eV [FT 2004.10709 p.3]: 𝒜_ph = 5.595 eV³ (V0).
Re-calibrated variants: V1 (θ_ii = 3/2) 5.525; V3 (a_DOS = 1, different units of 𝔓) 0.688.

**Validation convention (declared; GAP-EF-v2-C13).** *Primary set*: [FT] rows with a named measurement, **GaN at the EBIC value 9.59 eV**. GaN 8.9 eV is
not used: in 2308.03893 pp.18–19 it is the paper's own calculated value, and the "8.9 eV reported" in its Ref. [101] (a review) is not identified as a
measurement. *Extended set*: primary + β-Ga₂O₃, whose 15.6 eV is a self-described "experimental estimation" from EBIC on a Schottky barrier mixed
with an MC simulation [FT 2311.05011 p.5]; it is included, not excluded, and reported separately because the value is model-assisted.
(The GaN EBIC datum, Ref. [100] of 2308.03893, may come from the same group's method; not checked [UNVERIFIED].) *EF-LIT rows*: the two [FT]
numbers that returns/R16/EF-LIT.md found for the four survivors; neither is a measurement.

| Material | E_g, ω₀ (eV) [source] | ε_eh measured (eV) [source] | model V0 (V1, V3) | resid. | F measured | F model V0 |
|---|---|---|---|---|---|---|
| Si (calib.) | 1.164, 0.063 [FT 2004.10709] | 3.749 ± 0.001 [FT 2004.11499]; 3.748(2), 3.783(4) at 0.68/1.49 keV [FT 2305.09005 Table I] | 3.749 | — | 0.119 ± 0.002 (5.9 keV); 0.137(6), 0.146(9) at 0.68/1.49 keV [FT 2305.09005 Table I p.6]; < 0.31 [FT 2202.03924 Table II p.7] | 0.114 |
| Ge | 0.73 [FT 1909.05806 p.15], 0.037 [FT 1901.07569 Table I p.2] | 2.96 [FT 1909.05806 p.14]; "∼3" [FT 1602.08005 p.6] | 2.79 (2.79, 2.69) | +5.9% | 0.06–0.13 [FT 1909.05806 p.14, secondary] | 0.125 |
| C | 5.47, 0.163 [FT 1901.07569 Table I] | 13.1 ± 0.2, 13.25 ± 0.5, 13.05 ± 0.2, 12.82 ± 0.13 [FT 2311.05011 p.5]; weighted mean 12.95 (plain 13.06) | 11.37 (11.81, 12.24) | +13.9% | — | 0.088 |
| 4H-SiC | 3.26, 0.120 [FT 2008.08560 Table I p.5] | 7.83 ± 0.02 [FT 2311.03902 p.1, p.5] | 7.57 (7.68, 8.05) | +3.5% | 0.1 (2011 linewidth); ≤ 0.04 (2005 limit) [FT 2311.03902 Table 2 p.2] | 0.093 |
| 6H-SiC | 3.02, 0.120 [FT 2008.08560] | 6.7 [FT 2008.08560 Table I, secondary quote of its Ref. 34] | 7.17 (7.25, 7.60) | −6.5% | — | 0.094 |
| 3C-SiC | 2.39, 0.1205 [FT 2008.08560] | 6.90 [FT 2610.16949 Table II p.8] | 6.12 (6.15, 6.40) | +12.8% | — | 0.099 |
| GaN | 3.43, 0.0889 [FT 1910.10716 Table I p.2] | **9.59 (EBIC)** [FT 2308.03893 pp.18–19]; 8.9 not used (calculation / unspecified review) | 7.69 (7.84, 8.22) | +24.6% | — | 0.091 |
| SiO₂ | 9.2, 0.149 (α-quartz) [FT 1910.10716] | 18.0, one sample 16.4 (1975 oxide) [FT 2610.16949 p.8] | 17.41 (19.05, 18.76) | +3.4% | — | 0.084 |
| β-Ga₂O₃ (extended) | 4.8 [FT 2311.05011 p.1] (4.5 [FT 1902.02687 p.1]), 0.0973 (maximum phonon frequency, zone edge along b₃, DFPT-LDA) [FT 1902.02687 p.6] | 15.6, EBIC + MC "experimental estimation" [FT 2311.05011 p.5] | 9.99 (10.40, 10.76) | +56.1% | — | 0.087 |
| Al₂O₃ (EF-LIT) | 8.8, 0.104 [FT 1910.10716] | 27, vendor-datasheet value [FT 1504.04023 Table 1 p.3, via EF-LIT]; not a measurement | 16.54 (18.21, 17.84) | +63.2% | none found (EF-LIT) | 0.084 |
| CaWO₄ (EF-LIT) | 5.2, 0.106 [FT 1910.10716] | 29.8 = 2.35E_g/B, B = 0.41 (Robbins–Lempicki model) [FT 1001.5461 Table 2, via EF-LIT]; model value | 10.69 (11.17, 11.51) | +178.8% | none found (EF-LIT) | 0.087 |
| GaAs | 1.42, 0.0349 [FT 1910.10716] | ≈ 4.2 [UNVERIFIED: Bertuccio–Maiocchi, DOI 10.1063/1.1490158, no open full text] | 3.95 | (+6.4%, excluded) | — | 0.104 |

**Residual statistics** (meas/model − 1, V0):
- **Primary** (7 rows: Ge, C, 4H-SiC, 6H-SiC, 3C-SiC, GaN at 9.59, SiO₂): range −6.5% … +24.6%, mean +8.2%, rms 12.3%. This sets the §3 bands.
- Without GaN (6 rows): −6.5% … +13.9%, mean +5.5%, rms 8.7%. GaN at 8.9 eV would give +15.7% (v1's choice).
- **Extended** (+ β-Ga₂O₃, 8 rows): −6.5% … +56.1%, mean +14.2%, rms 23.0%. With E_g = 4.5 eV the β-Ga₂O₃ model value would be lower still, so the residual is not an artefact of the gap choice [E].
- All [FT] rows (+ the two EF-LIT values, 10 rows): −6.5% … +178.8%, rms 63.4%. Shown for completeness only: the EF-LIT numbers are a vendor value and a model value with a different (thermalised-pair) definition.
- Excluded as [UNVERIFIED]: GaAs ≈ 4.2 and CdTe ≈ 4.4 eV (no open full text).

**Reading.**
- The one-𝒜 model is good to ±6% for Ge, 4H-SiC, 6H-SiC and SiO₂.
- It under-predicts C (+13.9%), 3C-SiC (+12.8%) and GaN (+24.6% at EBIC), and β-Ga₂O₃ grossly (+56%). (H-EF5) is the most likely culprit
  (light-atom and polar lattices), but this is not demonstrated.
- v1's "this is the ABS pattern" is **withdrawn**: ABS did well for 3C-SiC and less well for SiO₂ and C [FT 2610.16949 p.3], while this model gets
  SiO₂ right and 3C-SiC wrong. The model differs from ABS on two of the four overlapping materials, so how faithfully (H-EF3)–(H-EF5) reproduce
  ABS 1980 is unverified (no full text).
- **Where the ab initio route does better, corrected** [FT 2610.16949 Table II p.8; FT 2311.05011 p.5; FT 2308.03893 pp.18–19]: C (12.87 eV,
  residual +0.6% against the model's +13.9%), 3C-SiC (6.6 eV, +4.5% against +12.8%), GaN (8.9 eV against EBIC 9.59: +7.8% against +24.6%) and
  β-Ga₂O₃ (11.24 eV, +39% against +56%). It does **worse** on 4H-SiC (7.3 eV, +7.3% against the model's +3.5%) and SiO₂ (16.7 eV, +7.8% against
  +3.4%). (v1 listed 4H-SiC as an ab initio success; that was false, REF-A K3, REF-B 2.6.)
- The low-energy rise of the measured Si F (0.137–0.146 below 1.5 keV [FT 2305.09005 Table I]) is not in the asymptote: it is finite-ω structure
  or the PCC systematics that 2305.09005 models.

**The 4H-SiC Fano tension (stated openly).** 2311.03902 Table 2 (p.2) lists two measured values that disagree with each other: F = 0.1 "calculated
from linewidth" (2011, Schottky) and F ≤ 0.04, an "upper limit from linewidth" (2005, diode); the other two entries are a Klein-model value and a
hypothesis. The model gives F = 0.093 (V0), 0.091 (V1), 0.091 (V3): consistent with the 2011 value and 2.3× above the 2005 limit. The 2005 limit
lies below **every** F computed for this model class: the minimum over all cases, variants, validation rows and predictions is 0.0510, the RPP
limit, which needs a narrow valence band and no phonons; with phonons and a narrow band the floor is 0.068, and with a broad band 0.081 (GAP-EF-v2-C22).
This floor is computed, not proven. Consequences: (i) if the 2005 limit holds, the random-k reduction (H-EF3) or the energy-only reduction (H-EF1)
fails for 4H-SiC, and the §3 F bands are not covering for it or for any material where the same failure occurs; (ii) a linewidth-based limit rests
on σ²_Fano = σ²_meas − σ²_noise − σ²_absorbed [FT 2311.03902 Eq. (3) p.2], so an overestimated noise term drives it down. Which of the two is the
case cannot be decided here [C]. The 4H-SiC F prediction in §3 is therefore **conditional on the 2011 value**. GE-2 records this.

---
## 3. Predictions for WP8-U survivors lacking data [E]
**Recipe.**
- Inputs E_g and ω₀ = ω_O,max (or ω_Γ,max) are copied from returns/R13/WP8-U-table.csv, with its source and locator: [FT 1910.10716 Table I
  p.2] unless marked; TeO₂, SrTiO₃ and KTaO₃ use JARVIS JVASP-57128, -8082 and -1127 (TBmBJ gap and Γ modes) [DB], a DFT proxy gap.
- The central value is V0. The band combines in quadrature the variant spread (V1, V3, and B_h = E_g for ionic and oxide materials, marked ⁿ)
  with the primary validation range (−6.5% / **+24.6%** on ε; Si's +4.5% on F). The +24.6% is GaN at EBIC; with GaN excluded it would be +13.9%.
- **No bias correction** is applied (it would be a second calibrated parameter). The model tends to under-predict polar and stiff wide-gap
  materials, so the upper half of each ε band is the more likely one.
- **v2 rerun.** Every row was recomputed with ω₀ on the grid (GAP-EF-v2-C20). Only CsI changed materially (ε_eh 11.46 → 11.21 eV, F 0.0834 → 0.0828);
  all others are unchanged to < 10⁻³ relative; bands moved because the validation range changed.
- **Li₂MoO₄ stays GAP** (no ω₀ and no experimental gap).
- EF-LIT found no ε_eh measurement and no F of any kind for Al₂O₃, CaWO₄, LiF or NaF (returns/R16/EF-LIT.md), so these rows stay predictions;
  the two EF-LIT numbers are compared in §2.

| Material (WP8-U verdict) | E_g | λ_ph | w_ph | ε_eh [eV] (band) | ε_eh/E_g | F_eh (band) |
|---|---|---|---|---|---|---|
| GaAs (S) | 1.42 | 1.95 | 0.0246 | 3.95 (3.69–4.93) | 2.78 | 0.104 (0.096–0.108) |
| Al₂O₃ (S)ⁿ | 8.8 | 0.0082 | 0.0118 | 16.54 (15.46–20.94) | 1.88 | 0.084 (0.067–0.088) |
| TeO₂ (S)ⁿ [DB gap] | 4.645 | 0.056 | 0.0192 | 9.69 (9.06–12.19) | 2.09 | 0.088 (0.068–0.092) |
| CaWO₄ (S)ⁿ | 5.2 | 0.04 | 0.0204 | 10.69 (9.99–13.45) | 2.06 | 0.087 (0.068–0.091) |
| LiF (S)ⁿ | 14.2 | 0.002 | 0.0054 | 25.06 (23.42–32.47) | 1.76 | 0.082 (0.068–0.086) |
| NaF (S)ⁿ | 11.5 | 0.0037 | 0.0043 | 20.49 (19.15–26.46) | 1.78 | 0.082 (0.068–0.086) |
| Ge (S), F only | 0.73 | 14.4 | 0.0507 | 2.79 (2.58–3.48) | 3.83 | 0.125 (0.108–0.130) |
| C (C), F only | 5.47 | 0.034 | 0.0298 | 11.37 (10.63–14.30) | 2.08 | 0.088 (0.083–0.092) |
| 4H-SiC (C), F only, F conditional (§2) | 3.26 | 0.16 | 0.0368 | 7.57 (7.07–9.49) | 2.32 | 0.093 (0.088–0.097) |
| GaN (C), F only | 3.43 | 0.14 | 0.0259 | 7.69 (7.19–9.66) | 2.24 | 0.091 (0.086–0.095) |
| AlN (C) | 6.2 | 0.023 | 0.0176 | 12.34 (11.53–15.53) | 1.99 | 0.086 (0.081–0.090) |
| SiO₂-q (C)ⁿ | 9.2 | 0.0072 | 0.0162 | 17.41 (16.27–22.00) | 1.89 | 0.084 (0.067–0.088) |
| ZnO (C)ⁿ | 3.3 | 0.16 | 0.0192 | 7.32 (6.83–9.19) | 2.22 | 0.090 (0.069–0.095) |
| MgO (C)ⁿ | 7.83 | 0.012 | 0.0105 | 14.84 (13.87–18.76) | 1.90 | 0.084 (0.067–0.088) |
| ZnS (C) | 3.8 | 0.1 | 0.0108 | 7.95 (7.43–10.00) | 2.09 | 0.088 (0.083–0.091) |
| NaCl (C)ⁿ | 8.75 | 0.0084 | 0.0035 | 15.84 (14.80–20.31) | 1.81 | 0.083 (0.067–0.087) |
| NaI (C)ⁿ | 5.8 | 0.029 | 0.0034 | 10.91 (10.19–13.81) | 1.88 | 0.084 (0.067–0.088) |
| CsI (C)ⁿ | 6.14 | 0.024 | 0.0016 | 11.21 (10.48–14.33) | 1.83 | 0.083 (0.067–0.087) |
| CaF₂ (C)ⁿ | 11.81 | 0.0034 | 0.0047 | 21.04 (19.67–27.15) | 1.78 | 0.082 (0.068–0.086) |
| MgF₂ (C)ⁿ | 12.4 | 0.0029 | 0.0059 | 22.14 (20.69–28.53) | 1.79 | 0.082 (0.068–0.087) |
| SrTiO₃ (C)ⁿ [DB gap] | 2.302 | 0.46 | 0.0285 | 5.68 (5.24–7.12) | 2.47 | 0.096 (0.071–0.101) |
| KTaO₃ (C)ⁿ [DB gap] | 3.326 | 0.15 | 0.0196 | 7.37 (6.88–9.26) | 2.22 | 0.090 (0.069–0.095) |
| GaSb (C) | 0.72 | 15 | 0.0379 | 2.67 (2.48–3.32) | 3.70 | 0.122 (0.106–0.128) |
| InSb (C) | 0.24 | 405 | 0.0896 | 1.75 (1.40–2.19) | 7.31 | 0.159 (0.127–0.166) |
| PbS (C) | 0.29 | 229 | 0.0928 | 1.92 (1.57–2.39) | 6.61 | 0.155 (0.124–0.162) |
| PbTe (C) | 0.19 | 816 | 0.0711 | 1.52 (1.19–1.90) | 8.02 | 0.162 (0.129–0.170) |
| PbSe (C) | 0.17 | 1140 | 0.1006 | 1.56 (1.17–1.94) | 9.16 | 0.168 (0.133–0.175) |

**Caveats** (each widens the band beyond what is written; tagged [E]).
- *Ionic crystals (alkali halides, fluorides, oxides).* Self-trapped and Frenkel excitons with E_x^b ~ eV mean that the "pair" of the charge
  ledger and the cascade quantum differ (§4). The narrow anion-p valence band (ⁿ) drives F to 0.068. The fluoride and halide rows lie outside the
  (EF9) domain (w_ph < 0.01); their numbers are solver values.
- *4H-SiC F* is conditional on the 2011 measurement (§2). The same caveat applies to any F row if (H-EF3) fails as the 2005 limit suggests.
- *Narrow-gap rows (λ_ph ≫ 100).* Outside the fit domain and the validated range; phonon-dominated cascades with free-carrier and Auger channels
  absent from (H-EF3).
- *Incipient ferroelectrics (SrTiO₃, KTaO₃).* The soft modes break (H-EF4)'s single ω₀.

---
## 4. WP7-E-v3 IF-E9: capture at the end of the cascade and exciton parameters

### 4.1 Prompt shallow-level capture (t < t_pr) [D for the algebra; D, sketch for σ_cap]
The cascade ends with carriers at x ≲ θ_iiE_g. They relax to the band edges through ℋ_<, and electron i can be captured on level j before t_pr
with probability f_i. Capture does not change the number of ii events N_ii, so ε^{cas} ≡ ω/⟨N_ii⟩ = ε_eh of §1–§3. Per WP5 A-1, a captured electron
leaves N_eh ≡ N_e^f + N_X, so N′ = Σ_{i ≤ N_ii}(1 − κ_i) with κ_i ~ Bernoulli(f_i), independent given the cascade.

*General law [D].* Conditioning on the cascade and using the law of total variance,

  Var N′ = E[Σ_i f_i(1 − f_i)] + Var[Σ_i (1 − f_i)].                                                                                           (EF12′)

*Hypothesis (H-cap): the capture probability is the same for every carrier and independent of the cascade, in particular of its terminal energy
x_i (f_i ≡ f_cap^e).* Then Σ(1 − f_i) = (1 − f_cap^e)N_ii and (EF12′) reduces to binomial thinning:

  ε_eh^{(W4)} = ε^{cas}/(1 − f_cap^e),   F_eh′ = (1 − f_cap^e)F_eh + f_cap^e   (GAP-EF-v2-C16),   ℋ_eff += Σ_captured E^tr_{e,j} (+ E_trap^{pr} in the ledger).   (EF12)

(H-cap) is a real restriction: the cross-section below depends on the carrier energy, and §1.6 shows the terminal residuals are correlated with N.
GAP-EF-v2-C16b gives an exact toy in which (EF12′) holds and (EF12), evaluated with the mean f, is off by more than 5%. When f depends on x_i, use (EF12′)
with f_i = f(x_i) on the cascade-end distribution.
- Hole capture leaves N_eh unchanged but adds E_pairs^{unp} and E_trap^{pr} (WP7-E-v3 (E1-W4)). In N^meas each captured carrier contributes
  𝔮_i ≈ 0; this enters WP7-E-v3 (E12) through m_ind(r) and Var 𝔮, not through F_eh.
- *Cross-section [D, sketch; prefactor UNVERIFIED].* For an attractive shallow centre, a carrier of kinetic energy E is captured if it emits a
  phonon inside the Coulomb radius r_C(E) = e²/(4πε_rE): σ_cap(E) ≈ πr_C² min[1, r_C/ℓ_ε(E)], with ℓ_ε the energy-relaxation length. For thermal
  carriers this reduces to the Lax/Abakumov–Perel–Yassievich form (4π/3)r_T³/ℓ_ε [UNVERIFIED]. At the cascade end E ≈ r̄_c ~ 0.3–0.8E_g (§1.6), so
  r_C is a few Å and prompt capture is small unless 𝓃_j ≳ 10¹⁸ cm⁻³ [E]. Capture during the slow acoustic cooling below ω_LO is post-prompt
  (WP7-E-v3 §2.1).

### 4.2 Excitons at the end of the cascade [D for the bookkeeping; E for numbers]
*Time.* Per WP5-v4 §R13.1 K1 and A-1, exciton formation is two-body and post-prompt (≳ ns > t_pr). At t_pr, N_X = 0 and nothing below applies;
(EF13)–(EF14) are statements at the read-out time t > t_pr, with the ledger (W4′) evaluated at that time.

- **(i) Ledger, consistent with WP5-v4 (W4′).** By WP7-E-v3 (E1-W4), N_eh ≡ N_e^f + N_X counts bound pairs, so excitons do not change N_eh,
  ε_eh or F_eh. (W4′) defines ℋ_eff ≡ ω − N_ehE_g − E_st − E_esc, so **ℋ_eff is unchanged** when a pair binds. The binding energy is released into
  the lattice: with ΔE_X^b = −N_XE_x^b and the other (W4′) terms zero, the **bare heat rises**, ℋ = ℋ_eff − ΔE_X^b = ℋ_eff + N_XE_x^b. Hence

  F_eh = Var ℋ_eff/(E_g²n̄)  (a tautology of the ledger),   F^{ℋ} ≡ Var ℋ/(E_g²n̄) = F_eh + [(E_x^b)²Var N_X + 2E_x^b Cov(ℋ_eff, N_X)]/(E_g²n̄),
  ⟨ℋ⟩ = ⟨ℋ_eff⟩ + ⟨N_X⟩E_x^b.                                                                                                                     (EF13)

  A heat-based Fano estimator (calorimetric) is therefore biased upward in the mean by ⟨N_X⟩E_x^b/ω per unit energy, and in the variance by the
  N_X fluctuations and their covariance with ℋ_eff (GAP-EF-v2-C21). (v1 wrote that excitons shift ℋ_eff by −N_XE_x^b; that contradicts (W4′), REF-B 2.8.)
- **(ii) Geminate formation.** The thermalisation distance r₀ of a cascade pair is set by its cooling. Onsager escape [UNVERIFIED classic] gives
  p_esc ≈ exp(−r_O/r₀), r_O = e²/(4πε_rk_BT_c) with T_c the carrier temperature, enhanced by ℰ_b. A pair that forms an exciton and never
  dissociates gives 𝔮 = 0. Per pair this is Bernoulli, so (reuse of WP7-E-v3 (E12), single position)

  N^meas: ϵ → ϵ_coll(1 − f_X(1 − p_diss)),   F_meas = ϵF_eh + 1 − ϵ.                                                                            (EF14)

  Non-geminate (density-dependent) formation is not Bernoulli. It enters as the ⟨N_eh⟩Var_r m_ind/⟨𝔮⟩ term of (E12), which grows with N.
- **(iii) Impact excitation [E].** In materials with large E_x^b, a carrier in [E_g − E_x^b, θ_iiE_g) can create a bound pair directly. As an
  ansatz (a gap shift on a fraction f_imp of pairs), Δε_eh ≈ −f_impE_x^b·dε_eh/dE_g, with (EF11) giving ≈ 1.7 (Si) to ≈ 1.6 (wide gap). This matters
  only for ionic crystals (E_x^b ~ 1 eV [UNVERIFIED]); for Si and Ge, E_x^b ≈ 15 and 3 meV ([UNVERIFIED]; 2.7 meV in [FT 1909.05806 p.15]) and the
  shift is < 1%.
- *Hydrogenic estimates [E]* (E_x^b = 13.606μ*/ε_r² eV, JARVIS BoltzTraP masses [DB], ε_r: GaN 9.5, ZnO 8.1, 4H-SiC 9.8 [UNVERIFIED]): GaN 26 meV,
  ZnO 42 meV, 4H-SiC 49 meV (GAP-EF-v2-C17). **Warning:** the remembered binding energies are ZnO ≈ 60 meV and 4H-SiC ≈ 20 meV [UNVERIFIED], a factor ≈ 2
  either way, so these are Wannier-limit orders of magnitude, not values. Alkali halides and fluorides need BSE.

### 4.3 Computation specification (not run)
- **Exciton parameters (E_x^b, a_x, oscillator strengths, binding to donors/acceptors).** G0W0 + BSE (BerkeleyGW or Yambo).
  - Fine k-grid by double-grid interpolation with spacing ≲ 1/(3a_x): Si/Ge need 10⁴–10⁵ k-points; ionic crystals 8³–12³.
  - 4–8 valence and 4–8 conduction bands; lattice screening ε₀ vs ε_∞ through a polaronic correction when E_x^b ~ ω_LO.
  - Validation: Si and Ge free-exciton binding; the LiF and NaCl exciton peaks. Cost [E]: 10³–10⁴ core-h (semiconductors), 10⁴ (oxides).
- **Capture.**
  - Shallow levels: effective-mass levels E_d = 13.6m*/ε_r² eV with central-cell DFT corrections; σ_cap(E, T, ℰ_b) from cascade-capture theory
    with EPW acoustic and optical emission rates (the same g^S as WP5 (W2), O4-d2).
  - Deep levels: multiphonon capture with DFT charge-transition levels and Huang–Rhys factors (WP4-v3 §6 [6.3]).
  - Output: f(x) on the cascade-end distribution of §1 (r̄_c, σ_res per type), as input to (EF12′) (not (EF12), unless f is shown flat in x)
    and θ_tr^{pr}. Cost [E]: ~10⁵ CPU-h per material (WP7-E-v3 §7).
- **Exciton kinetics.** As in the WP7-E-v3 §7 module, seeded by the cascade-end pair-separation distribution (needs k-resolved (H-EF1)
  violations: θ_{R-k}).

---
## 5. Computation specification for the full ab initio route (not run)
The pipeline is WP5-v4 §2, not repeated here: QE + G0W0 bands, BerkeleyGW full-frequency ε⁻¹(p,ω) for the (W1′) ii kernel, EPW for (W2) with
WP5-cp1–cp3, and a full-band cascade. Additions for ε_eh and F_eh:
- **Kernels.** Tabulate the ii kernel 𝒦̄(E → E′; E_e′, E_h′) and the phonon kernel per branch on 10 meV bins up to ≈ 100 eV. Above ≈ 15 eV,
  match to free-electron states with GW lifetimes. Hole bands and B_h come from the band structure. Include the plasmon channel explicitly, so that
  its effect on F (UNRESOLVED, (H-EF7)) is measured.
- **Statistics for F.** F_eh is a second moment. Event sampling needs N_ev ≈ 2/δ² events for relative precision δ (2 × 10⁴ events of ≥ 1 keV
  for 1% on F). Alternatively, the deterministic (EF3)–(EF4) on the iso-energy kernels gives F directly, and only the n_gen = 1 k-resolved step
  needs sampling.
- **Per material.** Si, Ge (SOC), GaAs (SOC, polar: Fröhlich g^L, cp1–cp3): 10⁴–10⁵ core-h each (WP5 §2). C, SiC (3C/4H; the 4H cell has 8 atoms):
  ×2. GaN, AlN (wurtzite, polar): ×2. Al₂O₃ (10-atom cell), CaWO₄ (12), TeO₂ (12), LiF, NaF (2): ≈ 10⁵ core-h for the oxides; the halides as Si,
  plus BSE (§4.3) because excitons are large.
- **Expected accuracy.** The DFT/TDDFT full-band MC residuals (meas/calc − 1) are +16% (Si), +0.6% (C), +7.3% (4H-SiC), +4.5% (3C-SiC), +7.8%
  (SiO₂), +7.8% (GaN against EBIC) and +39% (β-Ga₂O₃ against the EBIC + MC estimate) [FT 2610.16949 Table II p.8; FT 2311.05011 p.5;
  FT 2308.03893 pp.18–19]. (v1's "0% (GaN)" compared the calculation with a number it may share an origin with, and is deleted.) The ab initio route is
  clearly better than the one-𝒜 model for C, 3C-SiC and GaN, comparable for SiO₂, and worse for 4H-SiC.
- **Recommendation.** Run the ab initio route first for the polar/stiff wide-gap survivors (Al₂O₃, CaWO₄, LiF, NaF), where (H-EF5) is least
  trustworthy and where EF-LIT found no measurement at all. Also compute F for 4H-SiC: it decides between the 2011 value and the 2005 limit at the
  level of (H-EF3). No ab initio F_eh exists in the sources read, so the first one would be new.

---
## 6. Exact remaining gaps
- **GE-1.** (H-EF1) (θ_{R-k}) and (H-EF5) (universal 𝒜_ph) are the two unquantified truncations. The second is the most likely cause of the
  +14% to +25% residuals for C, 3C-SiC and GaN, and of the +56% for β-Ga₂O₃. (H-EF7) on F is UNRESOLVED.
- **GE-2.** No open full-text ε_eh for GaAs or CdTe; no F for diamond; no ε_eh or F for Al₂O₃, CaWO₄, LiF, NaF (EF-LIT). The only wide-gap F
  measurements are the two conflicting 4H-SiC values; the 2005 limit F ≤ 0.04 is below the computed floor 0.051 of the whole model class (§2).
- **GE-3.** T dependence beyond E_g(T) (phonon absorption, n_B in (W1)). Ge at 77 K vs mK is open (1602.08005).
- **GE-4.** Exciton-dominated ionic crystals: the cascade quantum vs the ledger pair, impact excitation (f_imp), and the energy dependence of
  capture (EF12′).
- **GE-5.** F^{ren} ≤ F_eh and the floor F ≥ 0.051 are computed in all cases, not proven [C].

---
## 7. Checks (code/GAP-EF-v2/checks.py, 28/28 PASS, ≈ 15 s)
| Check | Content |
|---|---|
| GAP-EF-v2-C1, GAP-EF-v2-C2 | RPP limit: coverage and F_exact; renewal F_unc → corrected 0911.1532 value 0.0443977 to 10⁻⁵ (v1: typo target 0.0439766, tolerance 5 × 10⁻⁴), and F_unc < F_exact |
| GAP-EF-v2-C3 | energy conservation of the discrete kernel |
| GAP-EF-v2-C4a, GAP-EF-v2-C4b | F from N-moments = F from heat moments (independent recursions); 2𝒞_<> from the ℋ_< − ℋ_> recursion = the remainder (v1's GAP-EF-C4 closure was a tautology) |
| GAP-EF-v2-C5, GAP-EF-v2-C6 | discretisation (Si N vs 2N; diamond); asymptote and fit-window stability |
| GAP-EF-v2-C7, GAP-EF-v2-C7b | calibration 3.749 eV with 𝒜_ph ∈ [5, 6] eV³; F_Si = 0.1138 is 2.6σ low, moves < 1% per 10% in 𝒜_ph, equals R&K's 0.115 within 2% (no 5% pass band) |
| GAP-EF-v2-C8 | R&K F_∞ within 2% (their MC scatter); five (A, E_g) points and three slopes against R&K Eqs. (12)–(13) |
| GAP-EF-v2-C9, GAP-EF-v2-C10 | Klein algebra (14/5; 54/175 N-fixed; 27/686 constrained); renewal F = σ²/ε² against an explicit constrained recursion |
| GAP-EF-v2-C11 | (K2) overstates c₀ by 39% / 36% |
| GAP-EF-v2-C12, GAP-EF-v2-C13 | spot rows of data/results.json recomputed; validation statistics under the declared convention (primary, extended, EF-LIT, no-GaN) |
| GAP-EF-v2-C14, GAP-EF-v2-C15 | fits (EF9)–(EF10) against fresh solver runs; (EF11) against a finite difference |
| GAP-EF-v2-C16, GAP-EF-v2-C16b | thinning (EF12) for constant f (sympy); exact toy: (EF12′) holds, (EF12) with mean f fails for state-dependent f |
| GAP-EF-v2-C17 | hydrogenic E_x^b values (26, 42, 49 meV) |
| GAP-EF-v2-C18 | all 16 cited arXiv IDs verified (API records in papers-GAP-EF and papers-GAP-EF-v2) |
| GAP-EF-v2-C19 | F^{ren} < F_eh in all seven computed cases, ratio ∈ [0.12, 0.88] |
| GAP-EF-v2-C20 | ω₀ on the grid for every validation and prediction row (< 1%); CsI on N ≥ 600; grid() fails loudly outside tolerance |
| GAP-EF-v2-C21 | (EF13): bare heat ℋ = ℋ_eff + N_XE_x^b, mean and variance identities (exact enumeration) |
| GAP-EF-v2-C22 | 4H-SiC model F > 0.04 in all variants; minimum F over every computed case ≥ 0.0510 |
| GAP-EF-v2-C23 | λ_ph → 0 rows on one grid pair close (EF8) with two carriers per pair |
| GAP-EF-v2-C24 | scan fit-edge bias at λ_ph = 100 (X = 25 vs 60) inside the fit budgets |
| GAP-EF-v2-C25 | k₂ range over the survivors 1.2–2.5 eV (1.5–2.5 inside the fit domain) |

## 8. Literature (arXiv API verified; [FT] = read in full text)
2610.16949 Nielsen–Fischetti, first-principles ε_eh, Table II, Klein/ABS/Shockley forms [FT] · 0911.1532 Subashiev–Luryi, exact Fano statistics of
random parking (printed F_unc is a typo, §1.7(a)) [FT] · 2004.11499 Rodrigues et al., Si F and ε_eh [FT] · 2004.10709 Ramanathan–Kurinsky,
Eqs. (8), (12), (13) [FT] · 2305.09005 Si F below 1.5 keV [FT] · 2202.03924 Botti et al. [FT] · 1909.05806 Ge F, ε_eh [FT] · 1602.08005 Ge ε_eh(T),
Klein form [FT] · 2311.03902 4H-SiC ε_eh and F compilation, Eq. (3), Table 2 [FT] · 2311.05011 diamond and β-Ga₂O₃ (E_g 4.8 eV p.1; 15.6 eV
estimate and 11.24 eV calculation p.5) [FT] · 2308.03893 GaN (8.9 calculated, 9.59 EBIC, pp.18–19) [FT] · 1901.07569, 2008.08560, 1910.10716 (material
inputs) [FT] · 2411.12320 (4H-SiC 7.8 eV quoted) [FT] · **new:** 1902.02687 Mengle–Kioupakis, β-Ga₂O₃ phonons (maximum phonon frequency 784.92 cm⁻¹
= 97.3 meV, DFPT-LDA, p.6; gap "near 4.5 eV", p.1) [FT]. Via returns/R16/EF-LIT.md: 1504.04023 (Al₂O₃ 27 eV, vendor value) and 1001.5461 (CaWO₄
B = 0.41) [FT there; not re-read here]. Classic sources (Fano 1947, Shockley 1961, Klein 1968, Alig–Bloom 1975, Feller, Lax capture, Onsager) are
cited only through the FT quotes above or as [UNVERIFIED].

---
## Closing table: referee items → resolution → location
| Item | Type | Resolution | Location |
|---|---|---|---|
| A-K1 / B-1 (FALLS #4, V4) | S | "Not a bound" withdrawn; F^{ren} < F_eh in all 7 cases, ratio 0.12–0.87; RPP sign fixed (0.0444 < 0.0510 is an under-prediction); "up to 5×" → 8×; general case [C]; L41 replaced by L-EF3 | §0 #4, §1.6, GAP-EF-v2-C19, LIMITS L-EF3 |
| A-K2 / B-8 (first half) | S | (EF12) given hypothesis (H-cap): f energy- and state-independent; general (EF12′) stated; toy counterexample | §4.1, GAP-EF-v2-C16, GAP-EF-v2-C16b |
| A-K3 / B-6 | S | GaN 8.9 not a named measurement → EBIC 9.59 used; statistics restated (rms 12.3%; no-GaN 8.7%); "ABS pattern" withdrawn; ab initio list corrected (C, 3C-SiC, GaN better; 4H-SiC, SiO₂ worse); §5 "0% (GaN)" deleted | §2, §5, GAP-EF-v2-C13 |
| A-K4 / B-6 (4H-SiC) | S | 2005 limit F ≤ 0.04 confronted with the computed floor 0.0510; two measurements disagree; consequences stated; 4H-SiC F prediction conditional | §0 #9, §2, §3, GE-2, GAP-EF-v2-C22 |
| A-K5 / B-3 | S | L42 no longer lists 2.73E_g + 0.55 (ABS-era Shockley-type law, not this chain); plasmon claim → R&K p.4 statement on yield; effect on F UNRESOLVED; R&K agreement at ≈ 2% scatter; Eqs. (12)–(13) cross-check added | (H-EF7), §1.7(c), GAP-EF-v2-C8, L-EF4 |
| A-K6 / B-4 | W | F_Si: untuned, = R&K's model value, ∂F/∂𝒜_ph small (±0.7% per ±10%), 2.6σ below 0.119 ± 0.002; Lowe 0.118 ± 0.004 quoted; GAP-EF-v2-C7b has no 5% pass band | §0 #6, §1.7(d), GAP-EF-v2-C7b, L23 ✎ |
| A-K7 / B-5 | W | "predicts/explains/derived" → "observed fit agrees in form with"; k₂ is not constant: 1.2–2.5 eV over the survivors (computed; the brief's 1.2–2.3 is REF-B's figure, which omits the E_g^{0.05} lift at large gaps); IF-EF6 status observed | §0 #7, §1.8, GAP-EF-v2-C25, IF-EF6 |
| A-K8 / B-2 | W | (K2) overstates c₀ by 39% / 36% (exact 28% / 27% below); "−20% to +40%" replaced by defined r̄_c comparisons (+105%, +70%, −16%); (K2) attribution to Klein UNRESOLVED | §1.7(b), GAP-EF-v2-C11, L-EF2 |
| A-K9 | W | GAP-EF-v2-C2 target 0.0443977 (0911.1532's 0.0439766 is a typo), tolerance 10⁻⁵, agreement 1.8 × 10⁻⁶; text uses 0.04440 | §1.7(a), GAP-EF-v2-C2 |
| A-K10 | W | v1's GAP-EF-C4 split: GAP-EF-v2-C4a (N route = heat route), GAP-EF-v2-C4b (independent Cov route via ℋ_< − ℋ_>); closure stated to be an identity | §1.3, §1.6, GAP-EF-v2-C4a, GAP-EF-v2-C4b |
| A-K11 | W | IF-EF1 now says the constraint takes the model *below* the data and that the leading anticorrelation is ℋ_<–ℋ_> along carrier lines, not sibling residuals; no-phonon "2𝒞 ≈ 0 … sibling" wording fixed (sibling effect = F − F^{ren} > 0) | §1.5, §1.6, IF-EF1 |
| A-K12 | W | (EF11) observed; §4.2(iii) [E]; scan.py comment corrected; §1.9 covers the 1.1% fit-edge bias | §1.8, §1.9, §4.2(iii), GAP-EF-v2-C24 |
| A-K13 / B-9 (notation) | N | σ_c → σ_res; w₀ → w_ph; Φ_t → 𝔓_t; ⚠ rows for 𝒱_≶, 𝒞_<>, ρ_t; R_t, p_t, r_C, r_O, r₀ local; all labels prefixed (GAP-EF-v2-Cn, GAP-EF-v2 (EFn)) | throughout; Symbols |
| A-K14 / B-9 (tags) | W | ε_r → [UNVERIFIED] with the factor-2 warning; E_g(110 K) vs 123 K noted (≲ 0.1%) | §4.2, §1.9 |
| A-a.1 | W | (EF8) condition "two terminal carriers per pair" stated before the identity | §1.7(b), GAP-EF-v2-C23 |
| A-R2 | W | (R-iid) stated before (EF6) | §1.5 |
| A-a.5 / B-8 (second half) | S | (EF13) made consistent with WP5-v4 (W4′): ℋ_eff unchanged, bare heat +N_XE_x^b, extra variance (E_x^b)²Var N_X + 2E_x^bCov; time (post-prompt, WP5-v4 K1) stated | §4.2(i), GAP-EF-v2-C21 |
| A-b L39 | W | Validity "θ_ii = 1, no phonons" added | L-EF1 |
| A-b L42 | W | Attribution corrected: 2.73E_g + 0.55 is Alig–Bloom's Shockley-type line [2610.16949 p.2], not the random-k A = 5.2 chain; chain output is R&K Eq. (12) | L-EF4 |
| A-b L43 / B-§3 | W | "agrees with"; k₂ not constant; domain excludes w_ph < 0.01 and λ_ph > 100 rows | L-EF5, §1.8 |
| A-b L23 | W | "Si 0.114 = R&K's 0.115 reproduced; 2.6σ below; structural spread −10%" | L23 ✎ |
| A-e (C mean) / B-2.6 | W | Diamond 12.95 eV is the inverse-variance weighted mean (plain mean 13.06) | §2 table |
| A-(e) GAP-EF-v2-C13 convention | W | Convention declared (primary = named measurements, GaN at EBIC) | §2, GAP-EF-v2-C13 |
| B-2.1 (F^{ren} definition) | W | F^{ren} defined as the code computes it, (EF6′), including the Poisson phonon term | §1.5 |
| B-2.1 (λ → 0 row) | W | Whole row on one grid pair (Richardson in every column); (EF8) closes (GAP-EF-v2-C23) | §1.6 |
| B-2.2 (GAP-EF-v2-C2 1% gap) | W | Resolved: the 1% was against the typo; the solver agrees with the corrected value to 1.8 × 10⁻⁶ | §1.7(a), GAP-EF-v2-C2 |
| B-2.6 (β-Ga₂O₃) | S | Included (extended set): E_g 4.8 eV [FT 2311.05011], ω_max 97.3 meV [FT 1902.02687]; model 9.99 eV, residual +56% | §2 |
| B-7 (CsI grid bug) | S | grid() enforces its tolerance and raises; Nmax ≥ 2n_w/w; predictions rerun; CsI 11.46 → 11.21 eV; GAP-EF-v2-C5 extended to diamond | model.py, §3, GAP-EF-v2-C5, GAP-EF-v2-C20 |
| B-2.7 (fit domain) | W | Halide/fluoride rows flagged as outside (EF9); solver values | §1.8, §3 caveats |
| B-2.5 (EF10 wording) | W | w_ph term and the downturn for e > 6.7 stated | §1.8 |
| B-2.8 ((EF14)) | W | labelled reuse of WP7-E-v3 (E12) | §4.2(ii) |
| B §1 (rung 4: Bose factors, mixed-T gaps) | W | n_B noted under (H-EF6); input gaps are as tabulated (110 K, 77 K or room T, per source) | §1.2, §2 table |
| B-R4 (GAP-EF-v2-C3–GAP-EF-v2-C6 B_h = ∞) | W | stated | §1.3 |
| Brief item 3 (EF-LIT) | — | EF-LIT existed at validation: Al₂O₃ 27 eV (vendor) and CaWO₄ 29.8 eV (model) added as [FT] rows with residuals, outside the primary statistic; no F found | §2, GAP-EF-v2-C13 |

---
## Symbols introduced/used
| Symbol | Meaning | Status |
|---|---|---|
| 𝒜_ph | ABS/R&K phonon-to-ii rate constant (eV³; R&K "A") | **new** (A is the mass number) |
| λ_ph ≡ 𝒜_ph/E_g³, w_ph ≡ ω₀/E_g, θ_ii ≡ E_th^{ii}/E_g, a_DOS | reduced rate ratio, phonon/gap ratio, threshold ratio, DOS exponent | **new** (w_ph replaces v1's w₀, which is O4's X0 weight) |
| 𝔓_t | three-body ii phase space ρ_t * ρ_t * ρ_t̄ | **new** (replaces v1's Φ_t; Φ is force constants/states/flux, and WP5's Φ_t was renamed 𝒰_t) |
| ρ_t ⚠ | carrier DOS shape of type t (local to §1) | **new**, ⚠ against ρ_T (mass density) |
| R_t(x), p_t(x), P_t | rate ratio (EF2); ii branching probability; ρ_tm_t | **new**, local to §1 |
| ℋ_<, ℋ_>, ℋ_i | residual heat below threshold; phonon heat above threshold (ℋ = ℋ_< + ℋ_>); heat attributed to pair i in (R-iid) | **new** |
| 𝒱_<, 𝒱_> ⚠, 𝒞_<> ⚠ | normalised variances and covariance of (EF7) | **new**, ⚠ against 𝒱_a (DM vertex), 𝒱_ν (B2 vertex), 𝒞_m, 𝒞_adm |
| r̄_c, σ_res (σ_res,e, σ_res,h) | mean and SD of the terminal residual per carrier (per type) | **new** (σ_res replaces v1's σ_c, which is W0's suddenness) |
| σ_pair² | variance of the per-pair heat in (R-iid) | **new** (replaces v1's σ_h²) |
| F^{ren}, c₀, k₁, k₂ | renewal (final-state) Fano estimate (EF6), (EF6′); λ_ph → 0 limit of ε_eh/E_g; slope and offset of the linear form | **new** |
| N_ii, ε^{cas}, f_cap^{e,h}, f_i, κ_i, f_X, p_diss, p_esc, f_imp | ii pair count; cascade pair energy; capture probabilities (uniform, per carrier) and indicator; exciton, dissociation, escape and impact-excitation fractions (§4) | **new** |
| r_C, r_O, r₀, ℓ_ε, T_c | Coulomb capture radius, Onsager radius, thermalisation distance, energy-relaxation length, carrier temperature | **new**, local to §4 |
| F^{ℋ} | Fano factor of a bare-heat estimator (EF13) | **new** |
| (H-EF1)–(H-EF7), (R-iid), (H-cap), (K1), (K2), (EF1)–(EF14), (EF6′), (EF12′), GAP-EF-v2-C1…C25, V0/V1/V3, GE-1…GE-5, IF-EF1…IF-EF7, L-EF1…L-EF5 | labels (prefix GAP-EF-v2 when cited) | labels |
| used unchanged | ω, E_g, ε_eh, F_eh, F_meas, n̄, N_eh, b_N, B_h, E_th^{ii}, ω₀, ℋ, ℋ_eff, ΔE_X^b, E_x^b, a_x, N_X, N_e^f, E_trap^{pr}, E_pairs^{unp}, E_st, E_esc, 𝔮, m_ind, ϵ_coll, 𝓃_j, σ_cap, u_car, t_pr, ℰ_b, θ_{R-k}, θ_dense, θ_tr^{pr}, θ_GW, θ_Z | NOTATION / WP5 / WP7-E |

## Interface flags
| # | Owner | Item | Action |
|---|---|---|---|
| **IF-EF1** (owed, restated) | WP5 (v4 §6.4(ii)–(iii); WP5v3-C4b) | **(ii)** 54/175 ≈ 0.31 is the variance with N held fixed. With the energy constraint the same independent-residual model gives 27/686 = 0.0394, **3× below** the data, not down to it; so the direction of WP5-v4's sentence is wrong, not only its number: the omitted correlations must *raise* F. **(ii′)** The leading anticorrelation is between ℋ_< and ℋ_> along each carrier line (2𝒞_<> = −0.265 against 𝒱_> = 0.288 in Si), not between sibling residuals; sibling correlations are positive (F − F^{ren} = +0.025 at λ_ph → 0). **(iii)** Phonon shot noise is not the leading term either: the phonon-heat variance 𝒱_> is 7× Poisson. Replace (ii)–(iii) by (EF6), (EF6′), (EF7) with the §1.6 table | **S**: rewrite §6.4(ii)–(iii); relabel WP5v3-C4b "N fixed"; L23 note |
| IF-EF2 | WP6-v3 §5.2 (yield rows) | (EF3)–(EF4) can serve as the "URF (energy-only)" member of the {step, R&K, URF} choice; ε_eh prior 𝒩(3.75, 0.05) unchanged; θ_GW and θ_Z on Γ_ii are equivalent to a factor on 𝒜_ph (degenerate, WP5 §8); F_eh is nearly 𝒜_ph-independent, so the F prior must come from the structural spread (−10%), not from 𝒜_ph | adopt; one M-type factor on 𝒜_ph |
| IF-EF3 | WP8-F / WP8-U | §3 table fills the ε_eh/F_eh GAP rows, [E] with bands (v2 values supersede v1; CsI changed); 4H-SiC F conditional; EF-LIT found no data for the four S survivors | consume; prefer [FT] measurements where present |
| IF-EF4 | WP7-E (IF-E9) | (EF12) only under (H-cap); otherwise (EF12′); (EF13) in the (W4′)-consistent form; §4.3 spec | close IF-E9 at the formula level; numbers open (GE-4) |
| IF-EF5 | NOTATION | Symbols "new" (σ_res, w_ph, 𝔓_t; ⚠ rows ρ_t, 𝒱_≶, 𝒞_<>) | add rows |
| IF-EF6 | coordinator: SOTA | "ε_eh ≈ 1.61E_g + k₂, k₂ = 1.2–2.5 eV (ω₀- and weakly E_g-dependent): an observed fit of the one-parameter cascade model, agreeing in form with 1.54E_g + 1.89" | SOTA row, status **observed / CLAIMED** (v1's "derived" withdrawn) |
| IF-EF7 | coordinator: LIMITS | v1's proposed L39–L43 collide with WP8-R's proposed L39–L42 (LE-168); v2 uses return-local L-EF1…L-EF5 (CONVENTIONS §13 row 24 practice); v1's L41 is replaced by L-EF3 | assign numbers |

## Proposed LIMITS rows (return-local labels; the coordinator assigns numbers)
| # | Chain (URF) | Source | Validity | Leading correction | Status |
|---|---|---|---|---|---|
| L-EF1 (v1 L39) | (W3) → (H-EF1)–(H-EF4) → (EF3)–(EF4) with a_DOS = 0, δ hole DOS, θ_ii = 1, no phonons: Rényi parking, F = 0.0510387; renewal value 0.0443977 | 0911.1532 Eqs. (2), (23) [FT] (F_unc corrected for the printed typo) | narrow valence band, constant conduction DOS, θ_ii = 1, no phonons | parabolic DOS, phonons | DERIVED (GAP-EF-v2-C1, GAP-EF-v2-C2) |
| L-EF2 (v1 L40) | (EF8) + (K1) θ_ii = 3/2 + (K2) uniform-in-k population → Klein ε = (14/5)E_g + rω₀ | 2610.16949 p.2; 1602.08005 Eq. (3) [FT] | (K2) overstates c₀ by 39% (θ_ii = 1) / 36% (θ_ii = 3/2) at λ_ph → 0 (GAP-EF-v2-C11); (K2) attribution to Klein UNRESOLVED | exact jamming population (EF3) | DERIVED (truncation) |
| L-EF3 (replaces v1 L41) | (EF6) with (R-iid): renewal (final-state) F^{ren} = σ_pair²/ε_eh² | 0911.1532 Eq. (7), p.2 "lower-bound estimate" [FT] | iid per-pair costs | sibling and carrier-line correlations (EF7): F^{ren}/F_eh ∈ [0.12, 0.87] in all computed cases | DERIVED (GAP-EF-v2-C10); lower bound in all computed cases (GAP-EF-v2-C19), not proven in general [C] |
| L-EF4 (v1 L42) | (EF3)–(EF4) with a_DOS = ½, θ_ii = 1, B_h, one 𝒜_ph → R&K random-k model: F_∞ = 0.1145 (Si, 300 K); ε, F planes = R&K Eqs. (12)–(13) | 2004.10709 Eq. (8) p.3, Eqs. (12)–(13) and F_∞ = 0.115 p.6 [FT] | universal 𝒜_ph; plasmon channel effect on F UNRESOLVED | per-material 𝒜_ph (C +14%, GaN +25%) | DERIVED; CROSS-CHECKED at ≈ 2% (GAP-EF-v2-C8) |
| L-EF5 (v1 L43) | (EF9) → ε_eh ≈ 1.61E_g + k₂, k₂ = 2.33(𝒜_phω₀^{0.96})^{0.24}E_g^{0.05} ∈ [1.2, 2.5] eV over the survivors | agrees in form with 2610.16949 p.2 (1.54E_g + 1.89) [FT] | λ_ph ∈ [0.003, 100], w_ph ∈ [0.01, 0.1] (excludes halides, fluorides, lead salts, InSb) | (H-EF5), (H-EF1) | observed (fit of a derived model) |
| L23 (✎) | add: F_eh = 𝒱_< + 𝒱_> + 2𝒞_<> (EF7), all terms computed; Si 0.114 under (H-EF1)–(H-EF7) = R&K's 2020 model value 0.115 reproduced; 2.6σ below 0.119 ± 0.002; structural spread −10% (a_DOS = 1) | 2004.11499, 2004.10709 [FT] | (H-EF1)–(H-EF7) | θ_{R-k}; T beyond E_g(T); plasmon term | DERIVED (GAP-EF-v2-C4a, GAP-EF-v2-C4b); not independent evidence (GAP-EF-v2-C7b) |
