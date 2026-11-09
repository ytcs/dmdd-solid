# R14 referee report REF-GAP-EF-B (hostile, isolated) on returns/R14/GAP-EF.md

Referee B. I read GAP-EF.md, code/GAP-EF/*, WP5-v4 §1.2 and §6.4, WP7-E-v3 IF-E9, WP8-U-table.csv, CONVENTIONS, NOTATION, LIMITS and DONE.
I did not open referees/, state/, briefs/ (only my own brief), LAUNCHES/log, or any other R14 or R15 return. I re-ran `checks.py`: **19/19 PASS, 15 s**.
I fetched nine papers into literature/papers-r14-REF-GAP-EF-B/ (2004.10709, 0911.1532, 2610.16949, 2308.03893, 2311.05011, 2004.11499,
1909.05806, 2311.03902, 2305.09005), read the parts I needed in full text, and deleted the PDFs and HTML; the .txt extracts are kept for locators.
My own checks are listed in §R. Each one ran in under 2 min and none is a Monte Carlo run.

## Verdict table
| # | Main claim | Verdict | Reason |
|---|---|---|---|
| V1 | (EF3)–(EF4): exact moment recursions; the solver | **STANDS** | I re-derived the cross terms of (EF4): ⟨m_im_j⟩ = [P_t*P_t*ρ_t̄ + 2P_t*ρ_t*P_t̄]/Φ_t, which is what the code computes. The RPP limit is reproduced to 10⁻⁴ (C1). An independent exact enumeration (R1) confirms the structure. The solver also reproduces R&K's *own* fits, Eqs. (12)–(13), to ≤ 1.1% (ε; 0.1% at A = 5.2) and ≤ 2.5% (F) (R2) |
| V2 | (EF6) and IF-EF1: WP5-v4 §6.4(ii)'s 54/175 ≈ 0.31 is the N-fixed value; with the energy constraint it is 0.0394 | **STANDS** | Sympy gives (54/175)(5/14)² = 27/686 = 0.03936 (R3). The renewal law Var N ≃ ωσ²/ε³ is 0911.1532 Eqs. (5)–(7) [FT p.2–3] |
| V3 | (EF7), F_eh = 𝒱_< + 𝒱_> + 2𝒞_<>, and the Si numbers 0.091 + 0.288 − 0.265 = 0.114 | **STANDS** | Given (EF1) the identity is exact. Reproduced: 0.0910 / 0.2876 / −0.2648 → 0.1138, both with and without B_h (R4); the exact toy confirms the identity (R1) |
| V4 | "The final-state (renewal) model is not a bound in either direction"; "over-predicts in the RPP limit (0.0444 vs 0.0510)" | **FALLS** | Sign error: 0.0444 < 0.0510 is an *under*-prediction. 0911.1532 p.3–4 states that F_unc = 0.0439766 "is smaller than the exact value" and that the uncorrelated final-state model "gives only a lower-bound estimate". In every case the return computes, F^{ren} < F_eh (R5) |
| V5 | Limits (EF8) and Klein: (K2) "overstates c₀ by 27–33%" | **STANDS WITH CORRECTION** | The identity holds (2 carriers per pair, verified). The numbers are wrong: 2.2/1.585 − 1 = **+39%** and 2.8/2.056 − 1 = **+36%**; measured relative to Klein's value instead, the gap is 28% and 27%. Neither reading gives 33% |
| V6 | R&K cross-check: F_∞ = 0.1145 vs 0.115; "C8 shows the plasmon channel changes F_∞ by < 0.5%" | **STANDS WITH CORRECTION** | The reproduction is confirmed [FT 2004.10709 p.6; Eq. (8) p.3 = (EF2) with 2π/105 = Γ(3/2)³/Γ(9/2)]. The plasmon sentence does not follow (§2.3) |
| V7 | One calibrated parameter; F_Si = 0.114 is a genuine prediction | **STANDS WITH CORRECTION** | F is not tuned. But it is (a) the R&K model's known output [FT 2004.10709 p.6: "not tuned for a specific Fano factor, and is thus predictive"], and (b) almost independent of 𝒜_ph, so the calibration hardly constrains it. It is also 2.6σ from 0.119 ± 0.002 (§2.4) |
| V8 | (EF9)–(EF10) and the "linear law" k₁E_g + k₂; tags | **STANDS WITH CORRECTION** | The fits are correctly tagged **observed**. "Explains", "predicts" and IF-EF6's "derived from the cascade" are overclaims. Over the survivors' ω₀, k₂ spans ≈ 1.2–2.3 eV, not 1.9–2.3 (§2.5) |
| V9 | Validation: 7 [FT] rows, residuals −6.5% to +15.7%, rms 10.0%; [UNVERIFIED] exclusions | **STANDS WITH CORRECTION** | The arithmetic is confirmed. Problems: GaN 8.9 eV comes from a review, not a measurement; the "ab initio does better" list wrongly includes 4H-SiC; the β-Ga₂O₃ exclusion is selective; F(4H-SiC) conflicts with the ≤ 0.04 limit and the return does not say so (§2.6) |
| V10 | Predictions for 27 materials, §3 | **STANDS WITH CORRECTION** | CsI is run with ω₀_eff = 2ω₀ (a grid floor), which biases ε by +2.3%. The halide and fluoride rows lie outside the (EF9) domain w₀ ≥ 0.01 (§2.7) |
| V11 | IF-E9: Bernoulli thinning (EF12) | **STANDS WITH CORRECTION** | The algebra is confirmed (sympy). It needs a hypothesis the return omits: f_cap must not depend on the terminal energy. The ℋ_eff bookkeeping in (EF13) is wrong (§2.8) |
| V12 | Proposed LIMITS rows L39–L43 and the L23 note | L39 STANDS; L40 SWC; **L41 FALLS as written**; L42 SWC; L43 SWC; L23 ✎ STANDS | §3 |
| V13 | Notation (d) | **STANDS WITH CORRECTION** | "New" symbols collide with NOTATION: σ_c (suddenness, W0) and w₀ (X0 weight, O4). 𝒱_≶ sits next to 𝒱_a and 𝒱_ν without a ⚠ |

SWC = STANDS WITH CORRECTION.

## 1. Rung 4 (DONE.md) items applicable here
- **Ionization threshold or yield assumptions.** These are the core of the return. θ_ii ∈ {1, 3/2} and a_DOS ∈ {½, 1} are bracketed, and their spreads
  are propagated into the §3 bands. This is acceptable. (H-EF1) (θ_{R-k}) remains unquantified, as the return admits (GE-1).
- **Bose factors.** (H-EF6) is emission-only, T ≪ ω₀. For Ge at 77 K, n_B(37 meV) ≈ 4×10⁻³, so this is fine. The validation inputs mix gaps at
  110 K, 77 K and room T without stating it (most of the 1910.10716 gaps are "T not stated (room T)" per the CSV).
- **Double counting.** Plasmon versus ii: the plasmon channel is dropped by (H-EF7), so it is not double-counted. Exciton: see §2.8. The other rung-4 items
  (time ordering, Umklapp, screening, DM kinematics, q sign) do not apply to an energy-only reduction.

## 2. Detailed findings
### 2.1 (a) Derived steps
- **(EF3)–(EF4).** Correct. The code `cascade.py::_moments` implements m and s with the cross term
  `cr = (P_t·H[t][t̄] + 2P_t·H[t̄][t])/Φ`, where H[a][b] = P_a*ρ_b. This matches the three pair terms ⟨m₁m₂⟩ + ⟨m₁m₃⟩ + ⟨m₂m₃⟩. Two further checks:
  - C3: discrete energy conservation holds to 8.6×10⁻¹⁶.
  - C4: Var N from the N recursion equals Var(ℋ_<+ℋ_>)/E_g² from the heat recursions, to 10⁻⁹. This closes (EF7) numerically; 2𝒞 is obtained
    as the difference, which is legitimate because Var ℋ comes from an independent recursion.
- **(EF6).** [D] as the renewal theorem under iid per-pair costs, with the N-fixed factor (E_g/ε)² correctly identified. One weakness: the code's
  F^{ren} (`decomposition`) is not "one-particle residual statistics" alone. It also adds a Poisson phonon term 2w₀P_c/ε². §1.6 should define
  F^{ren} as the code computes it.
- **"2𝒞_<> removes 92% of 𝒱_>".** Confirmed: 0.2648/0.2876 = 0.921.
- **"Shot noise ≈ 0.04".** Confirmed: w₀(ε/E_g − 1 − 2r̄_c) = 0.0541 × 0.791 = 0.043.
- **"(K2) errs by −20% to +40% depending on λ_ph".** No check supports it. If the figure refers to r̄_c, (K2)'s 0.6θ_iiE_g overstates the exact jamming
  value by +97% (θ = 1: 0.6 vs 0.3045) and +71% (θ = 3/2: 0.9 vs 0.526) at λ_ph → 0 (R5). Delete it or state which quantity it means.
- **λ→0 table row.** It mixes a Richardson-extrapolated ε/E_g = 1.585 with an r̄_c = 0.30 taken at h = 0.01 (1.609 unextrapolated). The (EF8) row
  then fails to close: 1 + 2(0.30) = 1.60 ≠ 1.585. Use one grid for the whole row.

### 2.2 (b), (c) Final-state model and the bound claim: FALLS
| case | F^{ren} | F_eh | F^{ren}/F_eh |
|---|---|---|---|
| RPP (exact 0.0510387 [FT 0911.1532 Eq. (2)]) | 0.0444 (code); 0.0439766 [FT p.4] | 0.0510 | 0.87 |
| λ→0, θ = 1 | 0.057 | 0.081 | 0.70 |
| λ→0, θ = 3/2 (R5) | 0.069 | 0.083 | 0.83 |
| Si (V0) | 0.022 | 0.114 | 0.19 |
| Si θ = 3/2 | 0.047 | 0.113 | 0.42 |
| Ge (λ = 14.4, R5) | 0.0153 | 0.125 | 0.12 |
- Every computed case has F^{ren} < F_eh. "Over-predicts in the RPP limit" is a sign error that contradicts the cited source (0911.1532 p.2: "the
  uncorrelated final-state model gives only a lower-bound estimate to F"). The return's 0.0521 (F_nnp) is a *nearest-neighbour-corrected* estimate,
  not the final-state model, so it cannot show "either direction".
- The under-prediction range is **1.15–8×**, not "1.4–5×" (Ge-like: 0.125/0.016 ≈ 8). Results-table row 4, §1.6 bullet 4 and L41's "×0.2–×1.2" all
  need rewriting. Corrected statement: "F^{ren} ≤ F_eh in every case computed (ratio 0.12–0.87). This is not proved in general [C]."
- C2 calls 0.04440 against 0.0439766 a reproduction, but it is a +1.0% mismatch, while C1 reaches 10⁻⁴ on the same grids. Either the type-resolved
  estimator differs from Subashiev's per-gap definition or the Richardson step is not converged. State the 1% gap and do not call it a reproduction.

### 2.3 (f) The R&K reproduction and the plasmon sentence
- **Source checked [FT 2004.10709].** All parameters match:
  - Eq. (8) p.3 is Γ_ph/Γ_eh = A(105/2π)(E − ħω₀)^{1/2}/(E − E_g)^{7/2}, which is (EF2) with Φ = (2π/105)x^{7/2} for a_DOS = ½.
  - A = 5.2, which R&K print as "eV²". Dimensionally it is eV³, so the return's unit remark is CONFIRMED.
  - W = 12 eV; termination at E < E_g (θ_ii = 1); E_g = 1.124 eV at 300 K; F_∞ = 0.115 (p.6).
- **The cross-check is stronger than the return claims.** R&K's own regressions, Eq. (12) ε = 1.7E_g + 0.084A + 1.3 and Eq. (13)
  F = −0.028E_g + 0.0015A + 0.14 (p.6), are reproduced by the solver at A ∈ {3, 5.2, 7} and E_g ∈ {1.0, 1.2} to ≤ 1.1% in ε (0.1% at A = 5.2) and ≤ 2.5% in F (R2).
  The return should cite this.
- **The plasmon claim is not supported.** R&K's model differs from (H-EF1)–(H-EF7) in more than the plasmon channel:
  - a P(E, E_r) first split;
  - a post-hoc "re-split" when E_h > W;
  - plasmons n_p = ⌊E_i/ħω_pl⌋ treated as ionizations.
  R&K also say that F is "constant at 2% level" across their scans, and the Fig. 3 caption attributes the point scatter to Monte Carlo statistics (p.6). A 0.5% net agreement therefore cannot isolate the plasmon effect.
  Replace with: "the net difference of all model differences is ≤ 0.5%, inside R&K's ≈ 2% MC scatter".

### 2.4 (f) Is F_Si = 0.114 a genuine prediction?
- **It is genuine in the narrow sense.** 𝒜_ph is fixed by ε_Si alone, and F is not fitted.
- **But it is not new, and the test is weak:**
  - The same model with A = 5.2 is already published as predicting F_∞ = 0.115 [FT 2004.10709 p.6].
  - F barely depends on the one parameter: the solver gives F = 0.110, 0.1145 and 0.117 at A = 3, 5.2 and 7 (R2). The prediction is therefore set
    almost entirely by structural choices (θ_ii = 1, a_DOS = ½, √x DOS). Variant V3 (a_DOS = 1) moves F by −10%, which is twice the data–model gap.
  - The model–data gap is −4.4%, or **2.6σ** against 0.119 ± 0.002 [FT 2004.11499 p.1]. 2004.11499 p.5 also quotes Lowe's F = 0.118 ± 0.004 at 123 K.
    "Within 5%" (C7b) is a tolerance chosen by the author, not a statistical agreement.
- **Required wording.** "Untuned; it reproduces the published R&K model value; agreement −4.4% (2.6σ of the stated error, no model error assigned)."

### 2.5 (f) Closed form, the linear law, and tags
- **Algebra and tags.** Substituting λ_ph = 𝒜/E_g³ into (EF9) gives E_g^{1−(3+γ)β} = E_g^{0.0506}, so the algebra is correct. Both (EF9) and (EF10)
  are tagged **observed**, which is correct (CONVENTIONS §12 amendment). (EF11) checks out: c₁u(1 − 3β − γβ) gives 1.694, against a finite
  difference of 1.777 (C15). This independently matches R&K's dε/dE_g = 1.7 (Eq. (12)).
- **Overclaims.**
  - (i) Results-table row 7, "This explains the empirical form", and §1.8, "The cascade therefore predicts the linear form", are too strong for a
    fit. Nielsen–Fischetti [FT 2610.16949 p.3] say that ε(E_g) "is not linear" and that 1.54E_g + 1.89 is a data fit.
  - (ii) k₂ = 2.33(𝒜ω₀^{0.96})^{0.24}E_g^{0.05} depends on ω₀. At ω₀ = 10 meV (CsI) it is ≈ 1.2 eV; at 163 meV it is 2.3 eV. Across the survivors, k₂
    therefore ranges over ≈ 1.2–2.3 eV, and "k₂ ≈ 1.9–2.3 eV" holds only for ω₀ ≥ 63 meV.
  - (iii) IF-EF6's SOTA wording "derived from the cascade" must read "observed (fit of the model), CLAIMED".
  - (iv) The model under-predicts C and GaN, the materials that set the empirical slope at large E_g, so k₁ ≈ 1.6 against 1.54 is a coincidence of
    form, not an explanation.
- **"F_eh is a quadratic in ε_eh/E_g".** (EF10) also has a w₀ term, so the claim as written is incomplete. The fit decreases for e > 6.7, so it
  must not be used for the narrow-gap rows. The return does say "use the solver", which is right.

### 2.6 (e) Validation provenance and residuals
- **Arithmetic confirmed.** Residuals: +5.9, +13.9, +3.5, −6.5, +12.8, +15.7 and +3.4%; mean +7.0%; rms 10.0%.
- **C mean.** "Mean 12.95" is the inverse-variance weighted mean (12.948). The plain mean is 13.055. Say "weighted".
- **GaN 8.9 eV.** 2308.03893 p.19 calls 8.9 its *own calculated* value and adds that "a value of 8.9 eV is reported" in Ref. [101], Sellin–Vaitkus,
  NIM A 557 (2006), a review. The only measurement named there is 9.59 eV (EBIC, Ref. [100]). The validation therefore uses a tertiary review number
  that coincides with the ab initio value.
  - §5's "0% (GaN)" error of the ab initio route compares that calculation with a number it may share an origin with. That comparison is circular.
  - With 9.59 as the GaN row, the residual becomes +24.6%, the rms 12.3% and the band top +24.6%. Report both rows or tag 8.9 "[FT, secondary review]".
- **"The ab initio route does better on exactly these materials: C 12.87, GaN 8.9, 4H-SiC 7.3".** 4H-SiC is not among "these" (C, GaN, 3C-SiC).
  There the ab initio value is *worse*: 7.3 against 7.83 is −6.8%, while the model's 7.57 is −3.3% [FT 2610.16949 Table II p.8]. Replace 4H-SiC
  with 3C-SiC (6.6 against 6.90, −4.3%, model −11.3%).
- **Exclusions.**
  - GaAs and CdTe: correctly kept out as [UNVERIFIED].
  - β-Ga₂O₃ (15.6 eV, [FT 2311.05011 p.5]): the exclusion as an "experimental estimation" is defensible. But it is the only [FT] value excluded on
    quality grounds, while 6H-SiC 6.7 is kept (I did not check that value's provenance in 2008.08560). Using (EF9) with E_g ≈ 4.85 eV [UNVERIFIED] and
    ω₀ ≈ 0.09 eV [E], the model gives ≈ 10.0 eV, a residual of about +56%. State this alongside the exclusion.
- **Omitted tension.** For 4H-SiC the model gives F = 0.093, but the table lists "≤ 0.04 (2005 limit)" [FT 2311.03902 Table 2 p.2] without comment.
  The model exceeds that limit 2.3×. Say so: either the limit is wrong or (H-EF5)/(H-EF3) fail.
- **Verified quotes [FT]:** 4H-SiC 7.83 ± 0.02 [2311.03902 p.1]; C 13.1/13.25/13.05/12.82 and Klein 15.92 eV [2311.05011 p.5]; SiO₂ 18.0/16.4 and
  3C-SiC 6.90 [2610.16949 p.8, Table II]; Ge 2.96, 0.73, F 0.106 [1909.05806 pp.14–15]; Si 0.137(6)/0.146(9) [2305.09005 Table I]; ABS/Klein/1.54E_g + 1.89 [2610.16949 pp.2–3].

### 2.7 Predictions (§3)
- **CsI grid floor.** `predict.R` uses `Nmax=300, nwmin=1`. For CsI (w₀ = 0.00163) no grid with n_w ≥ 1 exists below N = 307, so `grid()` returns
  N = 300, n_w = 1, and the run uses **w_eff = 0.00333 = 2.04 w₀**. This is a 104% phonon-energy error. The 1% tolerance in `grid()` is not enforced,
  and nothing warns.
  - At X = 12 (R6): N = 300 gives ε = 11.488 eV, against 11.227 eV at N = 614 with the correct w. The CsI ε is biased by **+2.3%** (F by +0.3%).
  - NaI and NaCl (w₀ ≈ 0.0035) fall on grids within 1%.
  - Fix: Nmax ≥ 2/w₀, or fail loudly. Also extend C5 beyond Si: C at N 67 → 134 gives 0.12%, and SiO₂ 0.18% (R6, confirming the budget).
- **Spot checks.** λ_ph for Al₂O₃, LiF, InSb, PbTe, PbSe, GaSb, Ge and SrTiO₃ recomputed: correct. The ω₀ inputs match WP8-U-table.csv
  (ω_O,max [FT 1910.10716]).
- **Fit domain.** LiF, NaF, CaF₂, MgF₂, NaCl, NaI and CsI have w₀ < 0.01, outside the (EF9) domain. Their solver values are valid, but L43 and the
  "wide-gap insulators: ε ≈ 1.8–2.1E_g" reading must not cite (EF9) for them.

### 2.8 IF-E9 (§4)
- **(EF12).** Var(N′) = (1 − f)²F n̄ + f(1 − f)n̄, so F′ = (1 − f)F + f and ε′ = ε/(1 − f). Correct (sympy, C16).
  - Missing hypothesis: f must be **the same for every carrier and independent of the cascade**. §4.1 itself makes σ_cap depend on the carrier's
    energy E ≈ r̄_c, and r̄_c is correlated with N through ℋ_< (§1.6).
  - With f_i = f(x_i): Var N′ = E[Σf_i(1 − f_i)] + Var(Σ(1 − f_i)) ≠ (1 − f̄)²Var N + f̄(1 − f̄)n̄. Add the hypothesis, or state the general form [D].
- **(EF13) is inconsistent with (W4′).** By WP5-v4 (W4′), ℋ_eff ≡ ω − N_eh E_g (E_st = E_esc = 0). If excitons leave N_eh unchanged, then **ℋ_eff is
  unchanged**, and it is the bare heat that rises: ℋ = ℋ_eff + N_X E_x^b. "Excitons shift only ℋ_eff by ΔE_X^b" is therefore wrong, and the
  "−⟨N_X⟩E_x^b/ω" shift has the wrong sign for a bare-heat estimator.
  - Moreover Var ℋ = Var ℋ_eff + (E_x^b)²Var N_X + 2E_x^bCov(ℋ_eff, N_X). A heat-based Fano estimator is therefore biased by the fluctuations in N_X,
    not only shifted in mean. The "identical to F_eh" statement is true only for ℋ_eff, where it is a tautology.
  - WP5-v4 K1 also places exciton formation *after* t_pr. §4.2(i)–(ii) should say which time it uses.
- **(EF14).** This is the WP7-E-v3 (E12) single-position form, so it is not new; label it "reuse".
- **σ_cap sketch and hydrogenic numbers.** σ_cap is a sketch with a prefactor tagged [UNVERIFIED], which is acceptable. The hydrogenic numbers
  check: 26, 42 and 49 meV. But the ε_r values (9.5, 8.1, 9.8) are literature constants tagged "[E]", which is a misuse of [E] (CONVENTIONS §12);
  tag them [UNVERIFIED] or cite them. These are Wannier estimates and should not be presented as values: the known binding energies are ZnO ≈ 60 meV
  [UNVERIFIED] and 4H-SiC ≈ 20 meV [UNVERIFIED].

### 2.9 (d) Consistency with WP5, CONVENTIONS and NOTATION
- **WP5-v4 (W14) and (W4′) are used correctly**, except for (EF13) (§2.8).
- **IF-EF1 against the WP5-v4 text.** WP5-v4 §6.4(ii) says the energy constraint and the sibling anticorrelation are "the leading physics". The return
  shows that the constraint *lowers* F to 0.039, below the data, so the *net correlation* (EF7) must *raise* F in the Klein model. IF-EF1 should say
  this explicitly. The direction of WP5's sentence is wrong, not only its number. Type S: agreed.
- **NOTATION collisions.** σ_c is already "suddenness" (NOTATION l.235) and w₀ is already "X0 weight" (l.225). Both are marked "new" with no ⚠.
  Rename them, e.g. σ_res and w_ph. 𝒱_≶ and 𝒞_<> next to 𝒱_a, 𝒱_ν and 𝒞_adm need a ⚠ under the decorator rule (IF-EF5).

### 2.10 (c) Ratings of claims that a published source is wrong
R&K's "eV²" for A is really eV³: **CONFIRMED** (dimensional analysis of Eq. (8)). Klein's uniform population (K2) overstates c₀: **CONFIRMED** within the model (R5).
Klein overshoots diamond (15.92 vs ≈ 13 eV): **CONFIRMED** [2311.05011 p.5]. WP5-v4 §6.4(ii)'s 0.31 is an N-fixed artefact: **CONFIRMED** (R3).
"The final-state model is not a bound", against 0911.1532's lower bound: **REFUTED**. R&K's plasmon channel changes F_∞ by < 0.5%: **UNRESOLVED**.

## 3. Proposed LIMITS rows
| Row | Verdict | Correction |
|---|---|---|
| L39 RPP | **STANDS** | Source quotes are exact [0911.1532 Eq. (2) p.2, Eq. (23) p.4]; C1 to 10⁻⁴ |
| L40 Klein | **SWC** | "(K2) overstates c₀ by 36–39% at λ_ph → 0" (not 27–33%). The source quote "(14/5)E_g + 0.5" [2610.16949 pp.2–3] is correct |
| L41 renewal | **FALLS as written** | Validity "not a bound" and correction "×0.2–×1.2" are wrong. Replace with: "F^{ren} ≤ F_eh in all computed cases (ratio 0.12–0.87); proved lower bound only for RPP [0911.1532]; general case [C]" |
| L42 R&K | **SWC** | "ε ≈ 2.73E_g + 0.55 empirical" is ABS's empirical fit and is not produced by the chain. The chain gives R&K Eq. (12), 1.7E_g + 0.084A + 1.3 (R2). Cite Eqs. (12)–(13) as the cross-check. Drop the plasmon inference |
| L43 linear law | **SWC** | observed; k₂ ≈ 1.2–2.3 eV across ω₀ = 10–163 meV; domain w₀ ≥ 0.01 excludes the halide and fluoride rows |
| L23 ✎ | **STANDS** | Add "2.6σ below 0.119 ± 0.002; reproduces the R&K model value" |

## R. Referee checks (scratchpad scripts, deterministic)
- **R1.** Exact enumeration with Fractions of a toy cascade (G = 3 units, uniform-composition ii, q_ph = ½, x ≤ 30). Every event satisfies
  nG + ℋ_< + ℋ_> = x, and G²Var N = Var ℋ_< + Var ℋ_> + 2Cov holds exactly. With phonons, 2𝒞 = −0.078 against 𝒱_> = 0.107. This confirms (EF7) and the
  sign of the anticorrelation independently of the return's code.
- **R2.** Solver against R&K Eqs. (12)–(13) at A = 3 / 5.2 / 7 (E_g = 1.124):
  - ε: 3.425 / 3.651 / 3.787 vs 3.463 / 3.648 / 3.799;
  - F: 0.1103 / 0.1145 / 0.1168 vs 0.1130 / 0.1163 / 0.1190.
  At E_g = 1.0 / 1.2 (A = 5.2): ε 3.441 / 3.779 vs 3.437 / 3.777.
- **R3.** Sympy: 2σ_c² = 54/175 for √x on [0, 3/2]; ×(5/14)² = 0.03936 (re-run of C9).
- **R4.** Si V0, B_h = 12 eV and B_h = ∞: ε = 3.7490 / 3.7487, F = 0.1138 / 0.1138, 𝒱_< 0.0910, 𝒱_> 0.2876 / 0.2875, 2𝒞 −0.2648 / −0.2647, r̄_c 0.715,
  F^{ren} 0.0219, b_N 0.345. (C3–C6 use B_h = ∞ while the calibration uses 12 eV; the effect is ≤ 10⁻⁴, so harmless, but state it.)
- **R5.** λ → 0, h = 0.01:
  - θ = 1: F 0.0811, F^{ren} 0.0568, r̄_c 0.3045;
  - θ = 3/2: F 0.0826, F^{ren} 0.0689, r̄_c 0.526, c₀ 2.052.
  Ge (λ = 14.4): F 0.1247, F^{ren} 0.0153.
- **R6.** Grid doubling:
  - C: 11.374 → 11.360 (0.12%);
  - SiO₂: 17.407 → 17.376 (0.18%);
  - LiF (X = 12): 25.090 → 25.077;
  - CsI (X = 12): 11.488 (w_eff = 0.00333) → 11.227 (w_eff = 0.00163).
- **C1–C18 re-run.** 19/19 PASS. Two of the checks are weaker than their wording: C2 has a 1% mismatch called a reproduction (§2.2), and C17 tests
  only 5 < E_x^b < 100 meV.

## Owed corrections (summary for the author)
1. **S.** Results-table row 4, §1.6 and L41: replace the bound claim with "F^{ren} ≤ F_eh in all cases computed" and fix the RPP sign error.
2. **W.** Klein: 27–33% → 36–39%. Delete or define "−20% to +40%". Use one grid for the whole λ → 0 row.
3. **W.** R&K: drop the plasmon inference; add the Eq. (12)–(13) cross-check; L42 must not list 2.73E_g + 0.55 as a chain output.
4. **W.** F_Si: "reproduces the R&K model value; 2.6σ; F is nearly 𝒜-independent".
5. **W.** Linear law: "consistent in form", not "explains" or "predicts"; k₂ is 1.2–2.3 eV; IF-EF6 status observed.
6. **S.** Validation: GaN provenance (8.9 vs 9.59), the 4H-SiC ab initio statement, the β-Ga₂O₃ residual, and the tension with the 4H-SiC F limit.
7. **S.** CsI grid bug (+2.3% in ε); enforce the `grid()` tolerance.
8. **S.** (EF12) hypothesis that f is energy-independent; (EF13) ℋ_eff is invariant, and the bare heat shifts by +N_XE_x^b with an added variance.
9. **N.** σ_c and w₀ clashes; ⚠ on 𝒱_≶ and 𝒞_<>; ε_r tags.
