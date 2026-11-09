# R14 referee report REF-GAP-EF-A (hostile, isolated) on returns/R14/GAP-EF.md

Read: returns/R14/GAP-EF.md, code/GAP-EF/*, returns/R13/WP5-v4.md §6.2–§6.4, returns/R12/WP7-E-v3.md (E1-W4, IF-E9), returns/R8/WP6-v3.md
(yield row), returns/R8/WP0-v3.md (grep), returns/R13/WP8-U-table.csv (spot rows), CONVENTIONS, NOTATION, DONE, LIMITS. Nothing else.
Reran `checks.py`: **19/19 PASS, 15 s** (as claimed). Own checks (scratchpad, ≤ 25 s each): an independent brute-force recursion, the
Rényi gap integrals (mpmath), R&K slope comparison, an X-convergence test. Full texts fetched to literature/papers-r14-REF-GAP-EF-A/
(0911.1532, 2004.10709, 2004.11499, 2610.16949, 2308.03893, 2311.05011, 2311.03902, 2008.08560, 1909.05806, 2305.09005, 1602.08005).
The PDFs and HTML were deleted afterwards; the .txt extracts were kept for the locators.

## Verdict table (one row per §0 item)
| # | Claim | Verdict | Reason |
|---|---|---|---|
| 1 | Exact moment recursions (EF3)–(EF4), solved by quadrature | **STANDS** | My independent triple-enumeration code reproduces every m, s array to 1e-13 (R1) |
| 2 | Energy constraint: F = σ_h²/ε², and 54/175 is the N-fixed value (0.039 with the constraint) | **STANDS WITH CORRECTION** | Algebra re-derived. WP5-v4 (ii) had already named the constraint as the leading physics; its error is the *direction* (W) |
| 3 | F_eh = 𝒱_< + 𝒱_> + 2𝒞_<>; Si 0.091 + 0.288 − 0.265 | **STANDS** | Cov(ℋ_<, ℋ_>) computed directly, not as a remainder, closes to 1e-14 (R1). C4's second clause is a tautology |
| 4 | Final-state (renewal) model "not a bound in either direction" | **FALLS** | In every case computed, F_ren < F. The RPP sentence has the sign reversed. 0911.1532 itself says "lower bound" |
| 5 | Limits: RPP exact; Klein = identity + (K1) + (K2); R&K F_∞ reproduced | **STANDS WITH CORRECTION** | RPP and R&K both confirmed, R&K more strongly than the return claims (R3). Three numerical and attribution errors (§b) |
| 6 | One parameter; F_Si = 0.114 predicted vs 0.119 ± 0.002 | **STANDS WITH CORRECTION** | It is uncalibrated, but it reproduces R&K's published 0.115 and sits 2.6σ_exp low. F is insensitive to 𝒜_ph |
| 7 | Closed form (EF9) and quadratic (EF10), tagged "observed" | **STANDS WITH CORRECTION** | The fits and substitution are re-verified. "The cascade therefore predicts", IF-EF6's "derived" and L42's "2.73E_g + 0.55" contradict the tag or the source |
| 8 | Validation on 7 [FT] materials, rms 10% | **STANDS WITH CORRECTION** | GaN "measured 8.9" is not an established measurement. The "ABS pattern" and "ab initio does better" readings are contradicted by the rows |
| 9 | Predictions for 27 materials, [E] bands | **STANDS WITH CORRECTION** | The 4H-SiC limit F ≤ 0.04, which the return lists itself, lies below the floor of the whole model class and is not confronted |
| 10 | IF-E9: Bernoulli thinning, excitons, (EF11)–(EF14) | **STANDS WITH CORRECTION** | (EF12) is missing a hypothesis. The impact-excitation shift is [E], not D |
| 11 | Owed correction IF-EF1 to WP5-v4 §6.4(ii) | **STANDS WITH CORRECTION** | Valid as S, but its text must also say the sibling-residual reading of (ii) is not borne out (§a.2) |

## Rerun and independent routes (rubric f)
- **R1: brute-force recursion.** I re-implemented (EF3)–(EF4) for the joint vector (N, ℋ_<, ℋ_>) by explicit enumeration over (i, j, k) with
  i + j + k = q. The full 3×3 second-moment matrix is formed, with all six ordered cross terms written out, and the code shares nothing with
  cascade.py except the grid convention. Test case: Si-like λ = 3.5501, h = 1/37, n_w = 2, X = 14E_g. Against `Cascade`: max|Δm| = 1.0e-13 and
  max|Δs|/s = 3.9e-14 for N, ℋ_< and ℋ_>. Asymptotic slopes on this short grid: F = 0.1124, 𝒱_< = 0.081, 𝒱_> = 0.266, 2𝒞_<> = −0.235, which sum
  to F to 6e-14. (EF7) is therefore an identity; the return computes 2𝒞 as Var ℋ − 𝒱_< − 𝒱_>, and here it is confirmed as a directly
  computed covariance. (With the return's X = 40, 74 pts/E_g the numbers become 0.091/0.288/−0.265, consistent.) **Note on C4:** its clause
  "VR + VP + Cov2 = F" is true by construction (`Cov2 = vH − vR − vP`). Only its first clause (N route = heat route) and R1 test anything.
- **R2: energy-constraint algebra (sympy, independent).** With √x on [0, θE_g], ⟨x⟩ = (3/5)θ and Var = (12/175)θ². At θ = 3/2:
  2σ_c² = 54/175 ✓; ε = 14/5 ✓; F^{ren} = (54/175)(5/14)² = 27/686 = 0.03936 ✓. Renewal theorem (Feller): Var N ≃ ωσ²/ε³ for iid costs, so
  F = σ²/ε² ✓ (EF6). The hypothesis "per-pair costs iid" is stated only implicitly ("model the cascade as a renewal sequence"); state it.
- **R3: R&K, cross-checked more strongly than claimed.** `run(A, E_g)` around (5.2, 1.124), with R&K's fitted planes Eqs. (12)–(13)
  [FT 2004.10709 p.6] for comparison: ε 3.651 vs 3.648; ∂ε/∂A 0.0852 vs 0.084; ∂ε/∂E_g 1.72 vs 1.7; ∂F/∂A 0.00150 vs 0.0015;
  ∂F/∂E_g −0.0282 vs −0.028. This four-slope agreement is the real cross-check, and the return should quote it. Its "agreeing to 0.5%" is
  partly luck: R&K's MC Fano values have "2% level" scatter (p.6), and Eq. (13) gives F = 0.1163 at these parameters (model 0.1145, −1.6%).
  CROSS-CHECKED stands, but at ~2%.
- **R4: random parking.** C1 is confirmed (1/ε → 0.74760, F → 0.05104). For C2 see §b.1.
- **R5: asymptote.** At X = 25 (scan.py) vs X = 60: at λ = 100, w₀ = 0.05, F is −1.1% and ε −0.24% off; at λ = 10–30 the shifts are < 3e-4.
  The fit domain therefore carries a ~1% edge bias, within the stated 2.3%. But scan.py's comment "asymptote reached at X = 25" for λ ≤ 100
  contradicts predict.py's own rule (X = 60 for λ > 5) and §1.4. Correct the §1.9 row so that it covers the fits.

## (a) DERIVED steps and hypotheses
1. (EF1), (EF3)–(EF4), (EF7), (EF8): derived, and the hypotheses (H-EF1)–(H-EF7) are stated. (EF8) needs exactly 2 terminal carriers per pair,
   which holds because the seed sibling sits at the band edge (code: `carriers_per_pair` = 2.000). State this; with a seed that is not a pair
   the identity has an O(1/n̄) defect.
2. §1.5's bold "WP5-v4 §6.4(ii) is an N-fixed artefact": **correct, but incomplete**. WP5-v4 wrote "54/175 ≈ 0.31 … 2.6× the data. The
   energy constraint and the anti-correlation between sibling residuals are the leading physics" (WP5-v4 l.661). GAP-EF shows two things:
   (i) the constraint takes the independent-residual model *below* the data (0.039, 3×), not down to it; (ii) the dominant anticorrelation is
   ℋ_<–ℋ_> along a carrier line, not between siblings. IF-EF1 should state both. Type S stands.
3. §1.6's statement "2𝒞 ≈ 0 … with its sibling correlations" (no-phonon row) conflates 𝒞_<> with sibling correlation. At λ → 0, ℋ_> ≡ 0,
   so 𝒞_<> vanishes trivially. The sibling correlation is visible as F − F^{ren} = 0.081 − 0.057. Reword (W).
4. (EF12) is **not** derived under the stated hypotheses. Binomial thinning F′ = (1 − f)F + f needs the capture probability to be the same for
   every carrier and independent of the cascade (in particular of its terminal residual x_i). The return's own f_cap = 1 − exp[−𝓃∫σ_cap(u_car)u_car dt]
   depends on u_car, and §1.6 shows the residuals are correlated with N. In general, with Φ = Σ_i f(x_i):
   Var N′ = E Σ f_i(1 − f_i) + Var(N_e − Φ), which reduces to (EF12) only for constant f. Add the hypothesis, or keep the correction term. C16 checks only
   the constant-f algebra.
5. §4.2(iii)'s Δε_eh ≈ −f_imp E_x^b dε_eh/dE_g is an ansatz (a gap shift on a fraction of pairs), so tag it [E], not D.
   (EF13) is fine: by WP7-E-v3 (E1-W4), ℋ_eff ≡ ω − N_ehE_g holds identically, so the "identical F" is a tautology of the ledger. Say so.
6. (EF11): the derivative of (EF9) is verified (Si 1.694; the FD gives 1.78). It is a derivative of an *observed* fit, so its status is
   observed/[E], not D.

## (b) Proposed LIMITS rows
- **L39 ✔.** C1 confirmed. Quotes CONFIRMED [FT 0911.1532]: Eq. (2) "Fexact = 0.0510387" (p.2); Eq. (23) "ρ∞ = 0.7475987" (p.4).
  Validity "narrow valence band, constant conduction DOS": add "θ_ii = 1, no phonons".
- **b.1 (L39 / L41 / C2): a printed value in 0911.1532 is wrong.** The paper prints "Func ≡ Func(∞) = 0.0439766…" (p.4). My mpmath
  evaluation of the paper's own G(x) (Eqs. (16)–(18), (24)) gives **F_unc = 0.0443977**, with ρ∞ = 0.747598 and ⟨x⟩ = 0.337617. The paper's
  own F_nnp = F_unc + δF_nnp = 0.05208 (p.5, with δF_nnp = 0.007685) also requires 0.044398, not 0.043977. The printed number is a
  transposition typo: **CONFIRMED (two routes)**. The solver gives 0.04440 (Richardson), which is right. C2 hardcodes the typo, and passes only
  because its tolerance (5e-4) is 50× looser than C1's agreement. Fix the C2 target to 0.0443977 and tighten it to 1e-5. In the text,
  "F_unc = 0.0440" should read 0.04440.
- **L40 ✎.** The derivation (K1) + (K2) → 14/5 is correct (R2). The quote is CONFIRMED: 1602.08005 Eq. (3) "ε = (14/5)E_g + rħω_R" (p.6), and
  2610.16949 p.2 "ε = (14/5)E_g + 0.5". The Validity cell is **mis-normalised**. The exact c₀ = 1.585 / 2.056 lies 28% / 27% *below* (K2)'s
  2.2 / 2.8, so (K2) *overstates* by 39% / 36%. "27–33%" fits neither, and 33 has no source in C11. Attributing (K2) to Klein himself is
  **UNRESOLVED**: there is no Klein full text, and 2610.16949 p.2 attributes "uniform population, E_f = 0.6E_i" to Shockley/ABS [41].
- **L41 ✎ (from FALLS #4).** The computed ratios F^{ren}/F are: RPP 0.0444/0.0510 = 0.87; no-phonon 0.057/0.081 = 0.70; Si θ = 3/2
  0.047/0.113 = 0.42; Si 0.022/0.114 = 0.19; Ge-like 0.016/0.125 = 0.13. The renewal estimate is *below* F in every case. §1.6 says it
  "over-predicts in the RPP limit (0.0444 vs 0.0510)", which is false. 0911.1532 states that the uncorrelated final-state model "gives only a
  lower-bound estimate to F" (p.2), and only the different nnp approximation overshoots. The leading-correction cell "×0.2–×1.2" should read
  F^{ren}/F ∈ [0.13, 0.87]. "Miss it by up to 5×" (§1.6) should read up to 7.8× (Ge). Allowed status: "DERIVED (C10); lower bound in all
  computed cases, not proven in general". The return has no counterexample to boundedness.
- **L42 ✎.** The chain and C8 are fine (R3). The quote is CONFIRMED [FT 2004.10709]: Eq. (8) Γ_ph/Γ_eh = A(105/2π)(E − ħω₀)^{1/2}/(E − E_g)^{7/2} (p.3).
  I checked that (EF2) with ρ = √x gives exactly this prefactor, since Φ(y) = Γ(3/2)³/Γ(9/2) y^{7/2} = (2π/105)y^{7/2}. Further quotes
  confirmed: "W is only 12 eV" (p.3); E_g 1.164 eV at 110 K and A "5.2 eV²" (Table I p.5); F∞ = 0.115 (p.6). **Delete "ε_eh ≈ 2.73E_g + 0.55
  empirical"** from this chain. 2610.16949 p.2 attributes that line to Alig and Bloom [11] ("using similar approaches", i.e. Shockley-type),
  not to the random-k A = 5.2 model, and this model gives C = 11.4 eV against 2.73·5.47 + 0.55 = 15.5. The row as written claims the chain
  reproduces a law that (EF9) contradicts. The plasmon claim in (H-EF7), "C8 shows it changes F_∞ by < 0.5%", is not shown by C8. The
  evidence is R&K's own sentence, "we do not observe any impact on the ionization yield by adding or removing this mechanism" (p.4), which
  concerns the yield, not F. Re-attribute it and drop "< 0.5%".
- **L43 ✎.** Keep the status "observed". Make the source cell read "agrees with" 1.54E_g + 1.89 [FT 2610.16949 p.2, quote CONFIRMED], not
  "explains / is". k₂ = 2.33(𝒜_phω₀^{0.96})^{0.24}E_g^{0.05} is not a constant: it ranges over ω₀ ∈ [20, 165] meV and E_g ∈ [0.2, 14] eV
  by ≈ 1.2–2.6 eV. At the stated validity (λ ≤ 100) the formula excludes the narrow-gap rows of §3.
- **L23 ✎ addition.** This is acceptable as "Si F_eh = 0.114 predicted under (H-EF1)–(H-EF7)", provided it adds "= R&K's 2020 model value
  0.115 reproduced; 2.6σ_exp below 0.119 ± 0.002; structural spread −10% (a_DOS = 1)".

## (c) Claims about published work: ratings (full text)
| Claim | Rating |
|---|---|
| 0911.1532: Eq. (2), Eq. (23), F_nnp = 0.0521 | CONFIRMED. Its printed F_unc 0.0439766 is a typo for 0.0443977 (my finding, CONFIRMED, b.1); the return quotes the typo |
| 0911.1532 shows the sign "depends on sibling correlations" (§1.6) | REFUTED as worded. The paper calls F_unc a lower bound; nnp is a different approximation |
| 2004.10709 Eq. (8) = (EF2) with 𝒜_ph = A; W = 12 eV; F∞ = 0.115; MC; E_g Table I | CONFIRMED. The units point (eV³) agrees with WP5-v4 §6.2(1) |
| 2004.11499: 3.749 ± 0.001 eV, F = 0.119 ± 0.002, 123 K, 5.9 keV (abstract; table p.5) | CONFIRMED |
| 2610.16949: Shockley Eq. (1); Klein 14/5; ABS A = 5.2, "Ge, AgBr, 3C-SiC" good, "SiO₂, C, PbO, CdS" less accurate (p.3); 1.54E_g + 1.89; Table II (3C 6.90, 4H 7.83/7.82, SiO₂ 18.0, 16.4) | CONFIRMED |
| "Klein's slope overshoots wide gap": 2311.05011 Klein → 15.92 eV for C; diamond data 13.1, 13.25, 13.05, 12.82; β-Ga₂O₃ "experimental estimation" 15.6 | CONFIRMED |
| GaN ε_eh = 8.9 eV "measured" [FT 2308.03893 pp.18–19] | **UNRESOLVED**. 8.9 is the paper's *calculated* value. It adds that "Ref. [101] … a value of 8.9 eV is reported", without saying it is a measurement. Only EBIC 9.59 is identified as measured |
| 4H-SiC 7.83 ± 0.02; F 0.1 (2011), ≤ 0.04 (2005) [2311.03902 Tables 1–2] | CONFIRMED |
| 6H 6.7 [34], 3C "5.7–7.7†" estimated, ω_LO values [2008.08560 Table I] | CONFIRMED (6H is a secondary quote) |
| Ge: 2.96 eV, 0.73 eV, E_x 2.7 meV, F 0.06–0.13, model 0.106 [1909.05806 pp.14–15]; Si F 0.137(6), 0.146(9), ε 3.748(2), 3.783(4) [2305.09005 Table I] | CONFIRMED |
| Klein (K2) = "uniform-in-k terminal population" | UNRESOLVED (no Klein full text) |
| WP5-v4 §6.4(ii) "2.6× the data" is an N-fixed artefact | CONFIRMED (R2), with the completion of §a.2 |
Not checked (not fetched): 2202.03924 "< 0.31", 1901.07569, 1910.10716 (the inputs match WP8-U-table.csv in spot rows), 2411.12320.

## (d) Consistency with WP0-v3, CONVENTIONS and NOTATION
- WP0-v3 has no ε_eh/F_eh statement that conflicts. WP6-v3's yield row carries "ε_eh: 𝒩(3.75, 0.05) eV (Si, 130 K) [E]", so the IF-EF2 quote is
  CONFIRMED. WP7-E-v3 (E1-W4), N_eh ≡ N_e^f + N_X: (EF12)–(EF13) are consistent with it.
- **Notation collisions (N type).** All of these are declared "new":
  - **σ_c** is taken (NOTATION: "σ_c, ξ_D | suddenness", W0);
  - **w₀** is taken (NOTATION: "w₀ … X0 weight", O4 row);
  - **Φ_t** was renamed *away* from WP5 because of the Φ collision (NOTATION: 𝒰_t, W5 "Φ_t" ⚠), and Φ is force constants, electronic states
    and flux. Rename to e.g. 𝔓_t.
  - 𝒱_≶ and 𝒞_<> are next to 𝒱_a, 𝒱_ν, 𝒞_m and 𝒞_adm; they need ⚠ rows at least.
  - ρ_t (carrier DOS) is next to ρ_T (mass density).
  - R_t, p_t, r_C, r_O, r₀ are generic and should be local to their sections.
- CONVENTIONS §14: unprefixed labels "C1…C19" appear in §0–§7 alongside the prefixed "GAP-EF-Cn". Prefix them.

## (e) Provenance tags
- GaN 8.9 is tagged [FT] as a measurement; it should be [UNVERIFIED] as a measurement (see c). Validation statistics recomputed from the
  return's residuals:
  - GaN excluded: 6 rows, range −6.5% … +13.9%, mean +5.5%, rms 8.7%;
  - GaN at EBIC 9.59: +24.7%, mean +8.3%, rms 12.4%.
  C13 should state which convention it uses. §5's "0% (GaN)" ab initio error is circular, so delete it.
- ε_r (GaN 9.5, ZnO 8.1, 4H-SiC 9.8) are literature constants tagged [E]; they should be [UNVERIFIED] or [DB] with a locator. Hydrogenic
  E_x^b values recomputed: 26, 42, 49 meV ✓ [E]. Note that the remembered data (ZnO ≈ 60 meV, 4H-SiC ≈ 20 meV) differ by about 2×, so
  "Wannier-limit only" should carry that warning.
- The calibration uses E_g(110 K) for a 123 K datum. The effect is ≲ 0.1% in ε; state it.
- The rest check out: λ_ph values (Al₂O₃ 0.0082, LiF 0.0020, InSb 405, PbSe 1140 ✓), the (EF9) Si value 3.220 ✓, (EF10) Si 0.1136 ✓, k₂ = 1.86 / 2.31 eV ✓,
  E_g^{0.05} = E_g^{1−(3+γ)β} ✓, the ε residual statistics as quoted (mean 6.96%, rms 10.0%) ✓, and DB/CSV inputs as in WP8-U-table.csv (GaN,
  InSb spot rows) ✓.

## (f) Central questions, point by point
- **F_eh = 𝒱_< + 𝒱_> + 2𝒞_<> with the energy constraint.** Re-derived (R1). The constraint is carried exactly because ℋ = ω − NE_g holds
  pathwise (C3; R1). STANDS.
- **0.31 → 0.039.** Confirmed (R2). STANDS, with §a.2.
- **0.05104.** Confirmed (R4). STANDS. The renewal companion 0.0444 is right, and the cited 0.0440 comes from the source's typo (b.1).
- **Klein identity.** (EF8) is an exact identity (a.1). 14/5 = (EF8) + (K1) + (K2) is right. The size of the (K2) error is misquoted (L40).
- **R&K 0.115.** Reproduced, and more strongly than claimed (R3). The comparator precision is ~2%, not 0.5%.
- **Is F_Si = 0.114 a genuine prediction?** Only in a weak sense.
  - (i) F is nearly independent of the calibrated parameter: ∂F/∂𝒜_ph = 0.0015 per eV³ (R3), so a ±10% change in 𝒜_ph moves F by 0.7%.
    The number is fixed by the structural choices θ_ii = 1, a_DOS = ½, B_h and ω₀, which are taken from R&K, whose F∞ = 0.115 with the
    same structure was published in 2020 (p.6, "not tuned for a specific Fano factor, and is thus predictive"). This is a reproduction of
    an existing prediction, not a new one.
  - (ii) It is 2.6σ_exp below 0.119 ± 0.002. C7b's 5% tolerance admits a 4.4% miss and is not a test.
  - (iii) The structural spread is −10% (a_DOS = 1) to −1% (θ_ii = 3/2).
  - (iv) Over the whole (λ, w₀) domain, F ∈ [0.081, 0.145], so any value in 0.10–0.13 is generic.
  The defensible statement: "the random-k model with one 𝒜_ph is consistent with F_Si to −4% (2.6σ_exp); this is not independent support".
- **Validation residuals and [UNVERIFIED] exclusions.** Excluding GaAs, CdTe and β-Ga₂O₃ is consistent with the tags. GaN should get the same
  treatment (e). The "Reading" bullets contain two false statements:
  - **"This is the ABS pattern".** ABS did well for 3C-SiC and less well for SiO₂ and C [2610.16949 p.3]. This model gets SiO₂ right (+3.4%)
    and 3C-SiC wrong (+12.8%), so it *differs* from ABS on two of the four overlapping materials. That calls into question how faithfully
    the reduction reproduces ABS 1980, which is unverified because there is no full text. The reading should be withdrawn.
  - **"The ab initio route does better on exactly these materials … C, GaN, 4H-SiC".** For 4H-SiC the model (7.57, −3.3%) beats ab initio
    (7.3, −6.8%), and 4H-SiC is not one of "these" under-predicted materials. GaN is circular. True for C and 3C-SiC only.
- **4H-SiC tension (prediction #9).** The return tabulates F ≤ 0.04 (2005 linewidth limit) next to its model value of 0.093. That limit lies
  below the floor of every case of the model class (RPP 0.051; no-phonon 0.081; narrow-band 0.068). If the limit holds, (H-EF3)
  random-k fails for 4H-SiC. §2 and GE-2 must state this as a conflict, and the §3 bands, which include 4H-SiC, are not covering.
- **IF-E9 Bernoulli thinning.** The algebra is correct for constant f (C16). The hypothesis is missing (a.4). STANDS WITH CORRECTION.
- **Closed-form and quadratic tags.** (EF9) and (EF10) are correctly tagged *observed*. But §1.8's bold "The cascade therefore predicts the linear
  form …", Item 7's "explains", and IF-EF6's "derived from the cascade … SOTA row" upgrade an observed fit of a model with one calibrated
  parameter to a derivation. CONVENTIONS §12 (R13) forbids this. Reword as "an observed fit of the (H-EF1)–(H-EF7) model agrees with
  1.54E_g + 1.89". The IF-EF6 SOTA row should be tagged observed/CLAIMED.

## Owed corrections (summary)
| # | Type | Item |
|---|---|---|
| K1 | S | §1.6, §0 item 4, L41: "not a bound / over-predicts in RPP" → renewal is below F in all cases (ratio 0.13–0.87); "up to 5×" → 7.8× |
| K2 | S | (EF12): add "f_cap identical and independent of the terminal state", or keep the covariance term (a.4) |
| K3 | S | §2: GaN 8.9 is not established as a measurement. Restate the residual statistics; withdraw "ABS pattern" and "ab initio better on 4H-SiC"; delete §5 "0% (GaN)" |
| K4 | S | §2/§3/GE-2: confront 4H-SiC F ≤ 0.04 against the model floor ≥ 0.051 |
| K5 | S | L42: delete "2.73E_g + 0.55"; (H-EF7) plasmon claim → R&K p.4 statement on yield, not C8 |
| K6 | W | §1.7(d), item 6, L23: F_Si is "R&K's model value reproduced, 2.6σ_exp low, weakly dependent on 𝒜_ph", not an independent prediction; C7b's tolerance |
| K7 | W | §1.8, item 7, IF-EF6: "predicts/explains/derived" → "observed fit agrees with" |
| K8 | W | L40/C11: "overstates c₀ by 27–33%" → by 36–39% (exact is 27–28% below (K2)); (K2) attribution UNRESOLVED |
| K9 | W | C2/§1.6: target 0.0443977 (0911.1532's printed 0.0439766 is a typo); tolerance 1e-5 |
| K10 | W | C4: say the (EF7) closure is an identity; cite an independent Cov route (as R1) |
| K11 | W | IF-EF1 text: add "the leading anticorrelation is ℋ_<–ℋ_>, not sibling residuals" (§a.2); §1.6 no-phonon row "2𝒞 ≈ 0" wording |
| K12 | W | (EF11) and §4.2(iii) → observed/[E]; scan.py comment vs the X = 60 rule; §1.9 row should cover the 1.1% fit-edge bias |
| K13 | N | σ_c, w₀, Φ_t collide (NOTATION W0, O4, W5 rename); ⚠ rows for 𝒱_≶, 𝒞_<>, ρ_t; prefix the Cn labels (CONVENTIONS §14) |
| K14 | W | ε_r tags [E] → [UNVERIFIED]/[DB]; E_g(110 K) vs 123 K noted |

**Overall.** The core of the return holds. The deterministic solver is correct (independently reproduced to 1e-13), the decomposition (EF7)
and the constraint factor (E_g/ε)² are right, and the R&K cross-check is stronger than claimed. Its interpretive layer overreaches: the
"not a bound" claim falls, the "ABS pattern" and "ab initio better" readings contradict the return's own rows, the GaN datum is not
established, the 4H-SiC F limit is ignored, and an observed fit is promoted to a derivation. Status after corrections K1–K14: CROSS-CHECKED
(solver); the material predictions remain [E].
