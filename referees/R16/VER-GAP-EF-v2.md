# R16 verification report VER-GAP-EF-v2 (hostile, isolated) on returns/R16/GAP-EF-v2.md

Read only: the return, code/GAP-EF-v2/*, returns/R14/GAP-EF.md, referees/R14/REF-GAP-EF-A.md and -B.md, returns/R13/WP5-v4.md ((W4′), ΔE_X^b),
returns/R16/EF-LIT.md, LIMITS.md (L23), state/LOOSE-ENDS.md (LE-168). No referees/R16, other R16 returns, briefs or log files were opened.
**Rerun:** `checks.py`, **28/28 PASS in 15.6 s**, the same as claimed. **Own checks** (scratchpad, each under 2 min): (V1) an independent mpmath evaluation of the
Rényi jamming gap moments from G(h) = 2∫₀^∞ t e^{−ht} exp[−2Ein(t)] dt; (V2) sympy for the Klein/renewal algebra, (EF11), the (EF9) exponent
and the (EF12′) total-variance law; (V3) every §0–§3 number recomputed from data/results.json and data/scan.json; (V4) a reading of
cascade.py's threshold branch and its decomposition() against (EF6′). **Full texts** fetched with lit.py to
literature/papers-r16-VER-GAP-EF-v2/: 0911.1532, 2004.10709, 1902.02687, 2311.03902, 2311.05011, 2308.03893, 2610.16949. The PDFs and HTML were
deleted afterwards; the .txt extracts were kept. Page numbers are PDF pages.

## Verdict table (scope 1–3 items)
| # | Item (where) | Verdict | Reason |
|---|---|---|---|
| 1 | IF-EF1 owed correction: 54/175 is the N-fixed value, 27/686 = 0.0394 is the constrained value (3× below the data); the leading anticorrelation is ℋ_<–ℋ_>; 𝒱_> is 7× Poisson (§1.5, §1.6, IF-EF1) | **STANDS** | Sympy (V2): ⟨x⟩ = 3θ/5, Var = 12θ²/175, 2Var at θ = 3/2 is 54/175, and with ε = 14/5 the constrained value is 27/686. 0.119/0.0394 = 3.0 and 0.309/0.119 = 2.6. Shot noise 0.0428 (V2), and 0.288/0.043 = 6.7. Wording note: see a.4 |
| 2 | F^{ren} is a lower bound in all 7 computed cases, ratio 0.12–0.87; [C] in general (§0 #4, §1.6, L-EF3) | **STANDS** | The json ratios are 0.870, 0.697, 0.837, 0.193, 0.418, 0.18, 0.123, and Ge gives 1/0.123 = 8.1×. The 0911.1532 quote "gives only a lower-bound estimate to F" is CONFIRMED on p.2, and again on pp.8–9. The downgrade from v1's D to "D (cases); [C]" is correct |
| 3 | (EF6′) defines F^{ren} as the code computes it (§1.5) | **STANDS** | cascade.py l.117–123: vt = σ²_res,e + σ²_res,h (one carrier of each type per pair, since ct·ε = 1), and 2w·P_c = ω₀⟨ℋ_>⟩/(n̄E_g²). This is (EF6′) |
| 4 | (K2) overstates c₀ by 39% / 36%; the exact values lie 28% / 27% below; r̄_c is +105% / +70% at λ → 0 and −16% in Si (§1.7(b), L-EF2) | **STANDS** | From the json (V3): 2.2/1.58526 − 1 = 38.8%, 2.8/2.05617 − 1 = 36.2%, 1 − c₀/(K2) = 27.9% and 26.6%, 0.6/0.29272 − 1 = +105%, 0.9/0.52808 − 1 = +70.4%, 0.6/0.71477 − 1 = −16.1% |
| 5 | λ → 0 rows Richardson-extrapolated in every column, closing (EF8) "to 10⁻⁴" (§1.6, GAP-EF-v2-C23) | **STANDS WITH CORRECTION** | For θ_ii = 1, 1 + 2r̄_c = 1.58544 against ε/E_g = 1.58526, which is 1.8 × 10⁻⁴, not 10⁻⁴. C23's tolerance is 2 × 10⁻³, 10× looser than the text. The row's 𝒱_> (−6 × 10⁻⁶ after extrapolation, a negative variance) and 2𝒞_<> = −1.5 × 10⁻⁴ are an O(h) grid artefact: at the grid point x = E_g, 𝔓(0) = 0 gives p = 0, so cascade.py l.74 sends the carrier down the "phonon" branch with nw = 1 even when phonon=False. Say "ℋ_> = 0 up to an O(h) threshold artefact" (N) |
| 6 | Published misprint: 0911.1532 p.4 prints F_unc = 0.0439766…; the correct value is 0.0443977 (§1.7(a), L-EF1, C2) | **STANDS WITH CORRECTION** | **CONFIRMED by two routes.** (V1) gives ρ∞ = 0.7475979, ⟨g⟩ = 0.3376174, F_unc = Var g/(1 + ⟨g⟩)² = **0.04439766**. The paper's own F_nnp = F_unc + 0.007685 = 0.05208 (p.5) needs 0.044395. The misprint is a **dropped digit** (0.04**4**39766 → 0.0439766), not the "transposition" the text calls it (§1.7(a)). The corrected value and C2's agreement to 1.8 × 10⁻⁶ stand |
| 7 | Published unit error: R&K print A in "eV²"; it is eV³ ((H-EF4)) | **STANDS** | **CONFIRMED.** In Eq. (8) [FT 2004.10709 p.3], Γ_ph/Γ_eh = A(105/2π)(E − ħω₀)^{1/2}/(E − E_g)^{7/2} is dimensionless only if A is in eV³. "5.2 eV²" is printed in Table I p.5 and on p.6 |
| 8 | R&K cross-check at ≈ 2% scatter, with five points and three slopes against Eqs. (12)–(13) (§1.7(c), C8) | **STANDS WITH CORRECTION** | Eqs. (12)–(13), "constant at 2% level", "not tuned … predictive" and F∞ = 0.115 are CONFIRMED on p.6. Recomputed plane values are 3.4628/3.6476/3.7988 and 0.11303/0.11633/0.11903. Maximum deviations from rk_slopes are 1.1% (ε) and 2.4% (F), both at A = 3. Locator: the attribution of the scatter to "Monte-Carlo statistics" is in the Fig. 3 caption on **p.7**, not p.6 (N). The solver's ∂F/∂E_g = −0.030 against −0.028 is not quoted; add it or drop "three slopes" in favour of four (N) |
| 9 | (H-EF7): the plasmon effect on F is UNRESOLVED; R&K's sentence concerns the yield (§1.2, §1.9) | **STANDS** | "we do not observe any impact on the ionization yield by adding or removing this mechanism" is CONFIRMED on p.4 |
| 10 | F_Si = 0.1138: untuned, 2.6σ low, ±0.7% per ±10% in 𝒜_ph, not independent support (§0 #6, §1.7(d), C7b, L23) | **STANDS** | (0.119 − 0.1138)/0.002 = 2.58. Si_F_pm10A gives half the difference = 0.68%. ∂F/∂𝒜 = 0.00138 eV⁻³. The scan F range is [0.0826, 0.1418], as quoted |
| 11 | k₂ = 2.33(𝒜ω₀^{0.96})^{0.24}E_g^{0.05} spans 1.2–2.5 eV (1.5–2.5 eV inside the fit domain) (§1.8, C25, L-EF5, IF-EF6) | **STANDS WITH CORRECTION** | Recomputed per row: minimum PbTe 1.196, CsI 1.331, maximum SiO₂ 2.534 and C 2.520. Inside the domain the minimum is GaSb 1.505. 1 − (3 + γ)β = 0.0507. Si (63 meV, 1.164 eV) gives **1.87 eV, not 1.86** (N) |
| 12 | Validation convention and statistics: GaN at EBIC 9.59; primary rms 12.3%, without GaN 8.7%, extended 23.0%, all 63.4% (§2, C13) | **STANDS WITH CORRECTION** | Arithmetic CONFIRMED (mean 8.23%, rms 12.34%; without GaN −6.5…+13.9%, rms 8.74%; extended mean 14.2%; all 63.4%). 2308.03893 calculates ∼8.9 eV (abstract) and quotes "9.59 eV … via electron-beam induced current [100]" and "Ref. [101], in which a value of 8.9 eV is reported": CONFIRMED. **Internal contradiction:** §2 says ab initio does "worse" on SiO₂ (+7.8% against the model's +3.4%), while §5 says "comparable for SiO₂". Make them agree (W) |
| 13 | Ab initio residuals (§2, §5) | **STANDS** | 2610.16949 Table II (p.8): Si 3.1, 3C 6.6, 4H 7.3, SiO₂ 16.7. 2311.05011: C 12.87 and β-Ga₂O₃ 11.24 eV. The residuals +16, +4.5, +7.3, +7.8, +0.6, +38.8% and GaN +7.8% all recompute |
| 14 | β-Ga₂O₃ inputs: E_g 4.8 eV, ω₀ = 97.3 meV, ε 15.6 eV, model 9.99 eV, +56% (§2) | **STANDS WITH CORRECTION** | All quotes CONFIRMED: 2311.05011 p.1 gives "Eg = 4.8 eV"; p.5 gives 15.6 eV, "experimental estimation", EBIC on a Schottky barrier "mixed with an MC simulation"; 1902.02687 p.6 gives "maximum value of 784.92 cm⁻¹ … zone edge along the b₃ direction" = 97.32 meV, and p.1 gives the gap "near 4.5 eV". **Convention mix:** this ω₀ is a zone-edge maximum, while the other rows use ω_LO or ω_O,max at Γ. Flag it in the table (W) |
| 15 | 4H-SiC: the 2005 limit F ≤ 0.04 lies below the computed floor 0.0510 of the model class (§2, C22, GE-2) | **STANDS** | 2311.03902 Table 2 p.2 ("0.1 … Calculated from linewidth", 2011; "≤ 0.04 … Upper limit from linewidth", 2005) and Eq. (3) p.2 are CONFIRMED. 0.093/0.04 = 2.3. The floor is labelled computed, not proven |
| 16 | CsI grid fix: 11.46 → 11.21 eV; grid() raises (model.py, C20) | **STANDS** | model.py now raises outside tol, with Nmax ≥ 2n_w/w. json CsI is 11.208 at N = 608, consistent with REF-B's 11.227 at X = 12 |
| 17 | (EF12′) general law; (EF12) only under (H-cap); C16b toy (§4.1) | **STANDS WITH CORRECTION** | The total-variance law holds given κ_i conditionally independent given the cascade (sympy, V2), and the reduction to (1 − f)F + f is correct. C16b is a valid counterexample (0.4647 against 0.4041). **But** the clause "ℋ_eff += Σ_captured E^tr_{e,j}", carried unchanged from v1 into the revised (EF12), contradicts (W4′). With E_st = E_esc = 0, ℋ_eff ≡ ω − N_ehE_g [WP5-v4 l.177], and each capture lowers N_eh by one, so ℋ_eff rises by **exactly E_g** per captured electron, however that E_g splits among E_trap^{pr}, E_pairs^{unp} and ℋ. This is the same logic the return used to fix (EF13). Replace the clause (W) |
| 18 | (EF13) after the fix: ℋ_eff unchanged, bare heat +N_XE_x^b, extra variance (§4.2(i), C21) | **STANDS** | With ΔE_X^b ≡ −N_XE_x^b [WP5-v4 l.174, l.685], (W4′) gives ℋ = ℋ_eff + N_XE_x^b, and the variance identity is exact. The post-prompt timing matches WP5-v4 K1 |
| 19 | (EF9)–(EF11), tagged observed; E_g^{0.05}; (EF10) turns down at e > 6.7; scan-edge bias (§1.8, C14, C15, C24) | **STANDS** | (EF11) at Si: sympy 1.695 against FD 1.777, as quoted. The turning point is 0.03643/(2 × 0.002711) = 6.72. C24 reproduces the bias (−1.13% in F, −0.24% in ε) |
| 20 | §0 row 11 tag "D" for IF-E9 (v1: "D / D, sketch / E") | **STANDS WITH CORRECTION** | This is an upgrade that no closing-table row covers. §4.1 still says "D, sketch for σ_cap" and §4.2 still says "E for numbers". Restore the composite tag (W) |
| 21 | Klein (K2) attribution UNRESOLVED; 2610.16949 p.2 attributes "uniform population" to Shockley/ABS (§1.7(b)) | **STANDS** | 2610.16949 pp.2–3: Shockley's "uniformly populated", "ε = (14/5)E_g + 0.5 and ε = 2.73E_g + 0.55" (Klein; Alig–Bloom) and "1.54E_g + 1.89", together with "is not linear". All CONFIRMED |

No item FALLS. Every correction above is of type W or N.

## (0) Closing table and §1 as a textbook derivation
**Closing table.** I checked each row against the R14 item it answers:
- **Resolved:** K1–K8, K10–K14, A-a.1, A-R2, A-a.5, A-b L39/L42/L43/L23, the A-e diamond mean, B-2.1 (both halves), B-2.2, B-2.5–2.8, B-7, B-R4 and B §1. The label sweep found no unprefixed Cn in the text, which confirms K13. The scan.py comment is fixed (l.27–28, K12).
- **Partly resolved:**
  - A-K9 resolves the number but repeats REF-A's "transposition" diagnosis, which is wrong; it is a dropped digit (item 6).
  - B-2.1's λ → 0 closure is overstated (item 5).
  - A-K6 (L23) and A-K5 are resolved, but L-EF4 now overclaims in a new way (§5 below).

**§1 as a textbook passage.** Hypotheses come before use for (EF1), (EF6) (R-iid), (EF7), (EF8) (two terminal carriers per pair) and (EF12) (H-cap). The
step structure of §1.3 is correct: I re-derived the single and pair sums of Step 2. It omits the following:
- **a.1 (W)** The seed and the ω ↔ x identification are never stated in §1.1–§1.3. (EF1) is written in ω, while (EF3)–(EF4) and C3 are in x
  (x = N E_g + ℋ_< + ℋ_>). The sections do not say what the initial state is (a carrier at x = ω − E_g with its partner at the band edge?) or whether N counts the seed
  pair. "One-sided seed" first appears in §1.4 and "pair seed" first appears in §1.7(b). Add one sentence before Step 1.
- **a.2 (N)** The ⟨Σs_i⟩ term of (EF4) is left implicit. It is the single-sum formula with P_t → ρ_ts_t. Write it.
- **a.3 (N)** §1.4, the asymptotic linearity that defines F_eh as the slope, stays [D, sketch], which is honest. Yet §0 rows 1 and 3 are tagged D or "exact in
  the model". Those numbers rest on the sketch plus the numerical check C6. Say "D (recursions); asymptote [D, sketch] + C6".
- **a.4 (W)** "The sibling effect is the gap F_eh − F^{ren}" (§1.6, IF-EF1 (ii′)). F^{ren} is the iid renewal value, so the gap measures
  *every* departure from iid per-pair costs: e–h correlations within a pair, correlations between more distant carriers, and the non-identical
  per-pair laws. It does not measure sibling correlations alone. "Sibling correlations raise F" is therefore an interpretation. 0911.1532 p.8 makes the same
  qualitative point for RPP ("the correlation correction to F is positive", and "division correlations are not the only … correlation corrections"). Reword it as "correlations beyond iid
  per-pair costs raise F".

## (1)–(3) Further notes on re-derived items
- (EF6) states the renewal theorem with its hypotheses (finite variance, non-lattice) by citation. 0911.1532 Eq. (7) is F_unc = ⟨δε²⟩/ε²,
  "a lower bound estimate" (p.2–3): CONFIRMED.
- (EF8): ⟨ℋ_<⟩ = 2n̄r̄_c needs exactly two terminal carriers per pair. The json gives carriers_per_pair = 2.000 in all rows. The identity follows
  by dividing the ledger by n̄. Correct.
- (EF12′): Var N′ = E[Var(N′|cascade)] + Var(E[N′|cascade]) = EΣf_i(1 − f_i) + Var Σ(1 − f_i). For constant f this gives
  (1 − f)²F n̄ + f(1 − f)n̄ over (1 − f)n̄, which equals (1 − f)F + f. Correct.
- Ge decomposition (json): 0.1451 + 0.4440 − 0.4644 = 0.1247, and 2𝒞 exceeds 𝒱_>, as the text says. Si: 0.2648/0.2876 = 92.1%.
- F_Ge = 0.1247 is 0.1247/0.106 = 1.18 times 1909.05806's model value, i.e. 18% above it. This is unchanged from v1 and was not re-fetched; REF-A confirmed it.

## (4) CLOSED-AS-EXACT-GAP rows
The return has **no row labelled CLOSED-AS-EXACT-GAP**. GE-1…GE-5 are open gaps, so there is nothing to verify as closed. I assessed §4.3 and §5, the
specifications that would close GE-1, GE-3 and GE-4:
- **Present:**
  - what is computed: the ii and phonon kernels, F, E_x^b, f(x);
  - the approximation level: G0W0/BSE, EPW and the full band;
  - the method: deterministic (EF3)–(EF4) on iso-energy kernels, or event sampling;
  - statistics: N_ev ≈ 2/δ² is right for a near-Gaussian N, since the relative error of a sample variance is √(2/N);
  - one pitfall: the plasmon channel kept explicit.
- **Missing (W):**
  - (i) convergence criteria for the kernel tabulation (10 meV bins, ≈ 100 eV cap): no bin-halving or cap test is specified;
  - (ii) the **ω₀-on-grid alignment pitfall**, which caused v1's CsI bug: with 10 meV bins, ω₀ = 10–20 meV (CsI, NaI, PbTe) is off-grid by up to 50%, so
    the spec should require bins commensurate with each phonon branch or an interpolated phonon step;
  - (iii) "only the n_gen = 1 k-resolved step needs sampling" names no sample size and no estimator;
  - (iv) no acceptance test against the R&K/RPP limits for the full-band code. It should be required to reproduce L-EF1 and L-EF4 when its kernels are replaced by the
    reduced ones.

## (5) Proposed LIMITS rows
| Row | Verdict | Notes |
|---|---|---|
| L-EF1 | **STANDS WITH CORRECTION** | Eq. (2) "Fexact = 0.0510387" (p.2) and Eq. (23) "ρ∞ = 0.7475987" (p.4) are CONFIRMED, and (V1) gives ρ∞ = 0.7475979. In the source cell, "corrected for the printed typo" should say "dropped digit". Validity is complete. Leading correction "parabolic DOS, phonons" is acceptable |
| L-EF2 | **STANDS WITH CORRECTION** | Quotes CONFIRMED (2610.16949 p.2 "(14/5)E_g + 0.5"; 1602.08005 Eq. (3) not re-fetched, confirmed by REF-A). The **Validity** cell holds the size of the correction (39%/36%), not a validity domain. Validity should read "θ_ii = 3/2, uniform-in-k terminal population, λ_ph → 0 for c₀", and the 39%/36% belongs under Leading correction |
| L-EF3 | **STANDS** | 0911.1532 Eq. (7) and the "lower-bound estimate" (p.2) are CONFIRMED. The status wording is right ([C] in general) |
| L-EF4 | **STANDS WITH CORRECTION** | (i) "ε, F planes = R&K Eqs. (12)–(13)" should read "agree with Eqs. (12)–(13) to ≤ 1.1% (ε), ≤ 2.4% (F)". (ii) Status "DERIVED" should be **CROSS-CHECKED**: R&K's model has a P(E, E_r) first split, a re-split for E_h > W and plasmons [FT p.6 steps 1–4], none of which are in (H-EF3)–(H-EF7). The row records two different models agreeing numerically at 2%; it does not derive one from the other. (iii) F_∞ = 0.1145 is at E_g = 1.124 eV (300 K), which is correct |
| L-EF5 | **STANDS** | "observed" is correct. 1.54E_g + 1.89 and "is not linear" are CONFIRMED (2610.16949 pp.2–3). The domain cell is correct |
| L23 ✎ | **STANDS** | The wording follows REF-A b (L23). LIMITS l.37 L23 is "DERIVED, REFEREED (R7)", and the ✎ is an addition, not a status change |

## Owed corrections (summary)
| # | Type | Target | Replacement |
|---|---|---|---|
| V-1 | W | §1.7(a), A-K9 row, L-EF1 source cell: "transposition typo" | "dropped-digit misprint (0.04439766 printed as 0.0439766)" |
| V-2 | W | §1.6 "close the identity (EF8) … to 10⁻⁴"; C23 tolerance 2e-3 | "to 2 × 10⁻⁴ (θ_ii = 1), 10⁻⁶ (θ_ii = 3/2)"; tighten C23 to 5e-4; note that the θ_ii = 1 row's 𝒱_>, 2𝒞_<> entries are an O(h) threshold-grid artefact (cascade.py l.74) |
| V-3 | W | (EF12) "ℋ_eff += Σ_captured E^tr_{e,j} (+ E_trap^{pr} in the ledger)" | "ℋ_eff rises by exactly E_g per captured electron ((W4′) with E_st = E_esc = 0), split among E_trap^{pr}, E_pairs^{unp} and ℋ" |
| V-4 | W | §5 "comparable for SiO₂" | "worse for SiO₂ (+7.8% against +3.4%)", as in §2 |
| V-5 | W | L-EF4 chain and status | "agree with Eqs. (12)–(13) to ≤ 1.1% / ≤ 2.4%"; status CROSS-CHECKED at ≈ 2% (GAP-EF-v2-C8), not DERIVED |
| V-6 | W | §0 row 11 tag "D" | "D (formulas); D, sketch (σ_cap); E (numbers)" |
| V-7 | W | §2 β-Ga₂O₃ ω₀ | add "zone-edge maximum (other rows: ω_LO/ω_O,max at Γ)" |
| V-8 | W | §1.6 bullet 3, IF-EF1 (ii′) "sibling effect = F_eh − F^{ren}" | "correlations beyond iid per-pair costs (sibling, e–h and longer-range) raise F: F_eh − F^{ren} = +0.025, +0.013" |
| V-9 | W | §1.3, before Step 1 | state the seed (initial state, ω ↔ x) and whether N counts the seed pair |
| V-10 | W | §5 specification | add kernel-bin and cap convergence tests, the ω₀-on-grid pitfall, the n_gen = 1 sampling size, and RPP/R&K acceptance tests |
| V-11 | W | L-EF2 Validity cell | move 39%/36% to Leading correction; Validity "θ_ii = 3/2, uniform-in-k terminal population" |
| V-12 | N | §1.7(c) | MC-scatter attribution locator p.7 (Fig. 3 caption); quote ∂F/∂E_g = −0.030 against −0.028 or say "three of four slopes" |
| V-13 | N | §1.8 | k₂ = 1.87 eV (not 1.86) at ω₀ = 63 meV, E_g = 1.164 eV |
| V-14 | N | §1.3 (EF4); §0 rows 1 and 3 | write ⟨Σs_i⟩ explicitly; tag the asymptote "[D, sketch] + C6" |

**Overall.** The v2 return absorbs every R14 item. The solver, (EF6)–(EF8), (EF12′) and the corrected (EF13) are right, and the two
published-error claims (0911.1532 F_unc; R&K's eV² unit) are CONFIRMED. The 0911.1532 claim needs one wording fix: it is a dropped digit. The remaining defects are presentational or bookkeeping:
- a ledger clause in (EF12) not brought into line with (W4′);
- an overclaimed L-EF4 status;
- a closure tolerance stated 10× tighter than it is tested;
- one internal contradiction (SiO₂);
- a §5 specification without convergence or acceptance criteria.

Status after V-1…V-14: solver CROSS-CHECKED; (EF1)–(EF8), (EF12′) and (EF13) DERIVED under the stated hypotheses; material numbers [E].
