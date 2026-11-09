# R16 / CW5-errata: verification corrections to returns/R16/CW5.md (VER-CW5)

Errata agent ERR-CW5, brief briefs/R16/ERR-CW5.md, 2026-11-01. **Read together with returns/R16/CW5.md**, which is not edited (returns are the record).
Where this file gives replacement text, it supersedes the CW5.md text at that site. **The merger uses only §B of this file** for the owed corrections
and proposed LIMITS rows, and §A0 for the closure-table cells. Everything not named here stands as written in CW5.md (VER-CW5 rows marked plain STANDS).
Read: returns/R16/CW5.md, referees/R16/VER-CW5.md, CONVENTIONS.md (§§10–14, R8/R13 amendments), NOTATION.md (greps), code/CW5/ (checks.py, LE-128/, LE-137/),
returns/R14/WP5-AUD.md (§3.3 Table II quote, A-12), returns/R13/WP5-v4.md §1.5 (K_ν, signed sampler), returns/R12/WP7-E-v3.md (C15, A-12),
returns/R12/WP7-T-v2.md (1.3).
**Literature** (lit.py → literature/papers-ERR-CW5/; full text read via pdftotext, PDFs and text dumps deleted, HTML and graph records kept): 1805.09942,
cond-mat/0507622, 2009.03804, 1705.01108, cond-mat/0310283 [FT]. Crossref (lit.py `works`, records kept as works-*.json): Kesten (1974) and Alsmeyer (1994),
bibliography only. Facts that only VER-CW5 read are tagged **[FT per VER-CW5]**.
**Checks:** `python3 code/CW5/checks.py` gives **26/26 PASS in 13–35 s (machine load)**. Revised checks keep their CW5-Cn labels; new ones are ERR-CW5-Cn (§D).
No heavy numerics were run. Tags are as in CONVENTIONS §12. Equation labels of this file are ERR-CW5 (E.n). Status of everything new: CLAIMED.

---
## A. Corrections, by verifier row

### A0. Closure-table cells (CW5 §0) that change
| Row | Replacement "Status" cell |
|---|---|
| LE-133 | CLOSED: **exponent** DERIVED (T⁻⁹); prefactor [FT] (cond-mat/0310283 Eq. (61)) |
| LE-138 | CLOSED-AS-EXACT-GAP (≈ 2.7% on ε_eh for the Z part [E], absorbed by calibration; spec with convergence target, §A15) |
| LE-139 | CLOSED-AS-EXACT-GAP (bound derived **conditional on (H-BGK)**, itself a relaxation-time form of (R-k); spec completed, §C) |
| LE-141 | CLOSED-AS-EXACT-GAP (linear law (CW5-4) [D]; dense-track law corrected (ERR-CW5 (E.3)–(E.6)); the missing input is a **rate set**, §C) |
| LE-143 | CLOSED: leading term DERIVED under (r1′)–(r5′) (§A12); b_N and variance stay [D, sketch] |
| LE-144 | CLOSED-AS-EXACT-GAP (**two** missing steps: p_FH(T), p_surv) |
| LE-145 + GAP-LEE (b) | CLOSED-AS-EXACT-GAP (bound + structure derived; **two** missing steps: U_rel with (Γ_min, Γ_max), and b_br) |
| LE-149 | CLOSED-AS-EXACT-GAP (TV bound; exact **if** the marks are sufficient; the spec estimates ΔP, not TV) |
| LE-151 | CLOSED-AS-EXACT-GAP (**two** missing steps; measurement proposal) |

### A2. Row 2: Ge field in the drift sentence (CW5 §1.2 "L36–L38 unaffected" bullet; OC-1) — STANDS WITH CORRECTION
1805.09942 [FT, PDF p. 2]: the iZIP faces "were biased respectively at +2 V and −2 V, while the interleaved phonon sensors were held at ground". The paper
does not state the crystal thickness (checked here). Replacement for the bullet's last clause: "…the Ge datum (1805.09942) is also biased (±2 V on the
two faces [FT, PDF p. 2]), i.e. ≈ 1.6 V/cm across the crystal [E: 4 V over 25.4 mm, the SuperCDMS Soudan iZIP thickness, which 1805.09942 does not state;
UNVERIFIED]. With v_d = 10⁵–10⁶ cm s⁻¹ [E] the Ge drift time is ≈ 2.5–25 µs (ERR-CW5-C5), still ≲ ¼ of the ≳ 100 µs phonon windows [E], so the [E]
conclusion holds for both data sets." The Si clause (1 µs at 4 V/cm, v_d from WP7-E-v3 C15) is unchanged. Owed text: §B OC-1.

### A3. Row 3: tag of "≤ 0.25 eV per carrier" (OC-2) — STANDS, tag added
The number is WP7-E-v3 C15's [E] (250 V/cm, saturated 10⁷ cm s⁻¹, t_pr = 100 ps). Owed text: §B OC-2.

### A5. Row 5: trajectory count (CW5 §1.2 B-2 bullet; OC-4) — STANDS WITH CORRECTION
√(2/(n − 1) + 2/n) ≤ 0.06 needs **n ≥ 1112** (n = 1100: 6.03%; n = 1111: 6.0017%; CW5-C17). Re-checking also showed that the n = 500, κ_ex = 2 error is
8.95%, which CW5 rounded to "9.0%": replace by "8.9%" (8.949%) in CW5 §1.2 and §6 (C17). Replacement for the B-2 bullet's parenthesis: "(√(2/(n − 1) + κ_ex/n):
8.9% at κ_ex = 2, n = 500; ≥ 1112 trajectories for 6%)". Owed text: §B OC-4.

### A6. Row 6: L38 bound for X^{oth}_ER of either sign (CW5 §1.2 L38 bullet; OC-5) — STANDS WITH CORRECTION, sharpened to an exact bound
VER-CW5 §1.1 is correct: f₀|_{r_coll = 1} = X^{oth}_ER·E_st/ω exactly, and its counterexample (g_Luke = 1.047, r_coll = 1.1, y = 0.3, X = −0.01) gives
f₀ = +0.067 at E_st/ω = 0.06 and −0.0055 at 0.69 (CW5-C3). CW5's proof needs X^{oth}_ER ≥ 0. Re-derived (sympy, CW5-C3) with e ≡ E_st/ω, X ≡ X^{oth}_ER,
κ ≡ κ_cal(r_coll), S_ER ≡ 1 − X + r_collg_Luke and f ≡ (1 − e − η^φ_NR)S_ER:

  f = f₀(e) + (1 + g_Luke)[δ_coll(1 − e − κX) + x(1 − δ_coll)]   (exact identity),                                                              (E.1)

with f₀ linear in e, f₀(0) = g_Luke(r_coll − 1)(1 − y_ion)(1 − X/(1 + r_collg_Luke)), f₀(1 − y_ion) = (1 − y_ion)X(1 + g_Luke)/(1 + r_collg_Luke). On the
domain of the proof (x ≥ 0, δ_coll ∈ [0, 1], d′_NR ≤ 1, r_coll ≥ 1, X ≤ 1 + r_collg_Luke, e ∈ [0, 1 − y_ion]) the bracket in (E.1) is ≥ 0 and f₀(0) ≥ 0. Linear
interpolation then gives f ≥ f₀(e) ≥ e·min(X, 0)(1 + g_Luke)/(1 + r_collg_Luke), i.e.

  E_st/ω ≤ (1 − η^φ_NR)/(1 − c_X),   c_X ≡ X⁻(1 + g_Luke)/[(1 + r_collg_Luke)S_ER],   X⁻ ≡ max(−X^{oth}_ER, 0)   (for c_X < 1).                        (E.2)

(E.2) is exact. For X ≥ 0 it is CW5's bound (c_X = 0). CW5-C3 now samples X ∈ [−0.2, 1] over the full (x, δ_coll) domain: min of (f + eX⁻(1+g)/(1+rg))/S_ER
is +1.4×10⁻³ ≥ 0. In the physical region (e ≲ 0.06, |X| ≲ 0.01, r_coll ≈ 1) c_X ≲ 5×10⁻³, so the bounds 0.055/0.064 move by ≤ 3×10⁻⁴. Status:
"REFEREED" is removed from the OC-5 Status cell. The coordinator records it after this R16 round (VER-CW5 §3, L38 row). Owed text: §B OC-5 and the L38 row.

### A8. Row 8: OC-7 support at 220 and 100 eV — STANDS (numbers added to the checks)
ERR-CW5-C1 (ε = 3.8 eV, ⟨𝔮⟩ = 0.873, F_ER = 0.119, Table II 1σ bands of 2303.02196 as quoted in WP5-AUD §3.3): 220 eV 1σ corner (Y 0.098, F_NR 0.4) gives
**1.72**; Y ∈ [0.085, 0.10] at F_NR 0.4 gives 1.70–1.87 (VER V6 reproduced). 100 eV 1σ corner (Y 0.072, F_NR 0.5) gives **1.27**. All eight 1σ corners at
100 and 220 eV are < 2 (max 1.72). "Firm at E_R ≲ 220 eV (1σ)" is therefore checked at both measured points below 300 eV. OC-7 text unchanged.

### A9. Row 9: L42 source tag — STANDS WITH CORRECTION
CW5 "Proposed LIMITS rows", L42 source cell: "2303.02196 [FT, via REF-WP5-AUD-A/B]" → "[FT] (2303.02196, as read by REF-WP5-AUD-A/B)". Re-issued in §B.

### A11. Row 11: signed seed sampler (CW5 §2.1; OC-9) — STANDS WITH CORRECTION (wording) + positivity derived
(a) **Variance → second moment (conceded).** With R ≡ Σ|K|/ΣK, the signed estimator Z = sign(K_i)R f(i), i ~ |K|/Σ|K|, has 𝔼Z = ⟨f⟩_K and
𝔼Z² = R²𝔼_{|K|}f², exactly R² times the second moment of the |K|-weighted estimator. The variance R²𝔼_{|K|}f² − ⟨f⟩_K² is not bounded by R²Var_{|K|}f: for
f ≡ 1 it is R² − 1 = 0.21 against 0 (CW5-C7, analytic). Replacement for CW5 §2.1's sentence: "…the estimator is **unbiased**, and its **second moment** is
exactly (Σ|K|/K_tot)² times that of the |K|-weighted estimator (CW5-C7: R² = 1.21); its variance is not bounded by that factor (f ≡ 1: 0 → 0.21)."
(b) **Where the sampler is needed.** WP5-v4 §1.5 samples phonon-branch classes ν with signed K_ν (the Fano term). For the defect seeds of WP7-T-v2 (1.3),
both δ(x) terms seed the **same** pole state. Per q bin they form one class of weight K_q = π|B|²/η_pole − 2πIm(a*B), which is ≥ 0 wherever |Im(a*B)| ≤
|B|²/(2η_pole) (VER-CW5's point, conceded for defect seeds). The signed sampler is needed in the bins where that fails, and for the K_ν wherever
4π max|c^F| > 1. One sampler covers all classes.
(c) **Positivity per N_eh [D].** CW5 had not shown Σ_iK_iP_i(N_eh) ≥ 0 for every N_eh. It holds in the following form. At fixed q the pole-region weight is
w(x) = |a + B/(x − iη)|² ≥ 0 pointwise. The classes (δ, fp, PV) are a signed split of w, and P(N_eh|x) ≥ 0 pointwise. Hence
Σ_iK_iP_i(N_eh) = ∫dx w(x)P(N_eh|x) + O(η) ≥ −O(η) **provided every class is evaluated with the same P(N_eh|x)** (the O4-d8/d9 consistency rules of WP5-v4 §2).
A negative class sum therefore diagnoses an inconsistent cascade (different smearing or T between classes), not physics. Owed text: §B OC-9.

### A12. Row 12: renewal leading term (CW5 §2.7(b); OC-10; LIMITS "new (renewal)") — STANDS WITH CORRECTION; proof completed
Notation: CW5 §2.7(a) "E N(E)" → **𝔼N(E)**, and (CW5-5) "E_unit[…]" → 𝔼_unit[…] (𝔼 = expectation; NOTATION has no expectation symbol, §E).
**Added hypotheses.** (r4′) *Summable approach to the scale-free law:* the lineage kernel K_x (law of ξ = ln(x_{j+1}/x_j), with a cemetery for leaving the
lineage into the gap or a phonon) obeys ‖K_x − K_∞‖_TV ≤ C(E_g/x)^κ for some C, κ > 0 (O(E_g/x) corrections give κ = 1); K_∞ has no killing.
(r5′) *Regularity in the threshold region:* for each cut x_c, h_c(z) ≡ 𝔼[Σ_{j: x_j ≤ x_c}1/x_j | first entry below x_c at z] is bounded uniformly in x_c and
continuous in z. This holds if x ↦ K_x is TV-continuous and the expected number of lineage steps in [E_g, x_c] is finite (VER-CW5 §1.4 (c)).
*Kernel property (part of the definition, not a new hypothesis):* the branching conserves energy, so a child never carries more than its parent and ξ ≤ 0
at every step. With (r3′) and (r4′) there are δ, p > 0 and x₁ such that P_{K_x}(ξ ≤ −δ) ≥ p for all x ≥ x₁ (below x₁, the threshold region, by (r5′)).
**Proof [D].** Write S ≡ Σ_j 1/x_j = S_> + S_≤ (terms above/below x_c ≫ E_g). (1) Because ln x_j is non-increasing and drops by ≥ δ with probability ≥ p at
each step, the number of visits to any unit log-interval is stochastically ≤ (1/δ + 1)·Geometric(p), **uniformly in x, for the perturbed lineage itself**.
Summing over log-bands gives 𝔼S_> ≤ C_v Σ_{k≥0}e^{−k}/x_c = O(1/x_c), and the same bound gives sup_{x_c} sup h_c ≤ C_vΣ_k e^{−k}/E_g (the uniformity in (r5′)). (2) Couple the true lineage from E to the K_∞ walk (the K_∞ walk inherits the same visit bound). The probability that they separate
before entering (0, x_c] is ≤ 𝔼Σ_{x_j > x_c}‖K_{x_j} − K_∞‖_TV = O((E_g/x_c)^κ), by (r4′) and the same visit bound. (3) Under K_∞ (iid, non-lattice (r2′),
finite mean (r3′)), the undershoot below ln x_c converges in law as ln(E/x_c) → ∞ (key renewal theorem for the ladder process [textbook, UNVERIFIED reference:
Feller vol. II, ch. XI]). With (r5′), 𝔼h_c(x_τ) converges. (4) Hence limsup_{E→∞}𝔼S − liminf_{E→∞}𝔼S ≤ O(1/x_c) + 2 sup h·O((E_g/x_c)^κ) → 0 as x_c → ∞.
The limit 1/ε_eh ≡ lim 𝔼S exists, and (CW5-5) gives m(E) = E/ε_eh + o(E). ∎ No rate is claimed.
A Markov-renewal theorem (Kesten, Ann. Probab. 2, 355 (1974), doi:10.1214/aop/1176996654; Alsmeyer, Stoch. Proc. Appl. 50, 37 (1994),
doi:10.1016/0304-4149(94)90146-5; bibliography verified (Crossref), content [UNVERIFIED]) would replace (r4′) and the coupling by Harris-type conditions. It is
not needed for the leading term. **Evidence:** CW5-C5 tests toys only (gamma(2), lattice, uniform fragmentation) and is not cited as evidence for the
branching limit. ERR-CW5-C2 illustrates the (r4′) mechanism: with killing a/x per event the tagged-unit sum converges, and successive differences fall ≈ 4×
per factor 4 in x. Owed text: §B OC-10 and the "new (renewal)" row.

### A14. Row 14: PECVD relabel (CW5 §3.4 table row 7, §3.4 "Strongest statement", §3.9 table and "Reading"; OC-12) — STANDS WITH CORRECTION
cond-mat/0507622 [FT, PDF p. 7]: "The SiO2 studied in this experiment was deposited with plasma enhanced CVD techniques using SiH4 and O2 as precursor
gases." So CW5's "CVD 5×10⁻³ vs PECVD 2.7–2.9×10⁻³" compares two PECVD films. Replacements: §3.9 first row "CVD a-SiO₂, 300 nm …" → "PECVD a-SiO₂ (SiH₄ + O₂),
300 nm …", with source "cond-mat/0507622 PDF pp. 3, 7, Fig. 1 caption p. 10". §3.9 second row "PECVD SiO₂" → "PECVD SiO₂ (0802.2404)". §3.9 Reading: "spans
3×10⁻⁴ (thermal oxide) to 5×10⁻³ (PECVD, cond-mat/0507622); the two PECVD films differ by ≈ 2× (preparation, OH content)". Bracket: "**tanδ₀ = 3×10⁻⁴
(thermal) and 5×10⁻³ (PECVD)**". §3.4: "for CVD SiO₂" → "for PECVD SiO₂ (cond-mat/0507622)". The L32 secondary bulk-quartz relation sits at PDF pp. 6–7
(its refs 13, 22). Owed text: §B OC-12 and the L32 row.

### A15. Row 15: LE-138 size (CW5 §0 row, §2.2) — STANDS WITH CORRECTION
d ln ε_eh/d ln λ_ph = β(ε_eh/E_g − c₀)/(ε_eh/E_g) = 0.1196 (CW5-C10). In §0 and §2.2: "size ≤ 2.7%" / "moves ε_eh by +2.7%" → "**≈ 2.7% for the Z part [E]**
(Z_qp = 0.8; W versus W_R untreated; (EF9) is an observed fit, L43)". Spec addition (thin-spec ruling, VER §2): §C LE-138.

### A16. Row 16: (CW5-1) scope (CW5 §2.3 last sentence) — STANDS WITH CORRECTION
Replacement: "**Spec addition.** Report w_mem(E) from the same EPW/GW rates and osc_k on 50 meV bins. θ_{R-k} is then bounded by (CW5-1) **given (H-BGK)**.
(H-BGK) is itself a relaxation-time form of (R-k), so the bound is conditional and is not an independent test of (R-k)." Full spec: §C LE-139.

### A17. Row 17: Theorem CW5-G hypotheses (CW5 §2.5) — STANDS WITH CORRECTION
Replacement for the theorem statement: "**Theorem CW5-G [D given (H-g1)–(H-g3)].** At mK there is no back-transfer (B → X, X → F), so in the order
(F, X, B_j) M is lower triangular and γ_k^{gap} are its diagonal entries k_FX + k_FT, k_X↓ + Σ_jk_XB,j, k_B↓,j. Then r_g(t) = 𝟙ᵀe^{Mt}p(0) = Σ_k P_k(t)e^{−γ_k^{gap}t}
with Σ_kP_k(0) = 1. The P_k are constants (w_k) when the γ_k are distinct (M diagonalisable), and polynomials in t of degree < multiplicity otherwise. The w_k
are **not** positive in general: a loss-free transfer F → X gives the weight −b/(a − b) < 0 (ERR-CW5-C3; CW5-C6 rates: w = 1.041, −0.077, 0.037). With
luminescence fractions η_X (X decay) and η_B,j (BX decay, a parameter; η_B,j = 0 if BX decay is purely Auger), the asymptotic split is: trapped
b_trap = k_FT/(k_FX + k_FT); light (1 − b_trap)(k_X↓η_X + Σ_jk_XB,jη_B,j)/(k_X↓ + Σ_jk_XB,j) (for B_j that do not branch further); heat the rest (CW5-C6,
exact to 10⁻¹²)."

### A18. Row 18: §2.5 (ii), dense tracks — **FALLS as stated → re-derived**
**What falls.** Under (CW5-2), r_g counts E_pairs + E_X. A formation step F + F → X moves E_g − E_x^b from E_pairs to E_X and releases only E_x^b. Bimolecular
**formation** alone therefore leaves r_g ≈ 1. CW5-C6b (replaced) integrates dn_F/dt = −C_Xn_F², dn_X/dt = C_Xn_F² − k_X↓n_X with C_Xn₀ = 1, k_X↓ = 10⁻³/t₀:
r_g = 0.9997, 0.992, 0.909 at t/t₀ = 1, 10, 100 while n_F = 1/(1 + t/t₀) (VER V3 reproduced). The old C6b compared n₀/(1 + C n₀t) with itself and is removed.
**Replacement for (ii)** (r_g ≈ n_F + n_X up to the ≤ E_x^b/E_g ≈ 1.3% exciton offset; n normalised to n₀; t₀ defined per channel):
"(ii) **Dense tracks break (H-g2).** Only gap-energy **loss** channels lower r_g; formation (F + F → X) moves gap energy between E_pairs and E_X.
- (ii-a) *Formation-limited* (k_X↓ ≫ C_Xn_F(t) throughout, no diffusion): r_g ≈ n_F = 1/(1 + t/t₀), t₀ = 1/(C_Xn₀) (CW5-C6b: to 5×10⁻⁴ at k_X↓t₀ = 10³).   (E.3)
- (ii-b) *X–X annihilation* (dn_X/dt = −k_X↓n_X − γ_XXn_X², fast formation, no diffusion): r_g = e^{−k_X↓t}/[1 + (k_X↓t₀)⁻¹(1 − e^{−k_X↓t})], t₀ = 1/(γ_XXn₀);
  → 1/(1 + t/t₀) for k_X↓t ≪ 1.   (E.4)
- (ii-c) *Free-carrier Auger* (dn/dt = −C_An³, no diffusion): r_g = (1 + 2t/t₀)^{−1/2}, t₀ = 1/(C_An₀²).   (E.5)
- (ii-d) *Diffusing tracks* (Gaussian profile, s = r₀² + 4D_Xt, first order in γ_XX beyond which the Gaussian shape is a closure): a compact NR cloud of N₀
  pairs saturates, 1/N_∞ − 1/N₀ = γ_XX/(4√2π^{3/2}D_Xr₀), and is followed by the linear law (CW5-4); a long cylindrical track of line density λ₀ decays only
  logarithmically, λ(t) = λ₀/[1 + (γ_XXλ₀/8πD_X) ln(1 + 4D_Xt/r₀²)] (ERR-CW5-C4).   (E.6)
The D-1 term at t_win is 𝔶𝒢_gap r_g^{NR}(t_win) with r_g from (E.3)–(E.6). A power-law tail (𝔶𝒢_gap t₀/t_win, or 𝔶𝒢_gap(t₀/2t_win)^{1/2} for Auger)
requires 4D_Xt_win ≪ r₀² and k_X↓t_win ≪ 1. A compact diffusing cloud instead gives a density-dependent saturated loss and an exponential approach. Because
t₀, N₀/r₀ and λ₀ depend on the track density, **r_g^{NR} ≠ r_g^{ER} whenever a bimolecular loss channel acts within t_win** [D given (E.3)–(E.6)]. This is
REF-A's point, now with its mechanism stated."
Consequences: OC-1's "(CW5 (CW5-4), bimolecular tail)" → "(CW5-4) and ERR-CW5 (E.3)–(E.6) (bimolecular loss)"; L37 and "new (gap release)" rows; the LE-141 spec
must say which channel (§C). Re-issued in §B. Rebuttal on the diffusion regime: §C-R1.

### A21. Row 21: α_ohm pitfall factor (CW5 §3.1 (b), last sentence; LIMITS "new (α_ohm)") — STANDS WITH CORRECTION
Replacement: "Pitfall: with a both-spin n₀ (= 2N_σ) and K_both ≡ (n₀VΩ)² = 4K, one gets α_ohm = K_both (factor 1). Using α_ohm = 4K with a both-spin K
overstates α_ohm by 4." 2009.03804 [FT, read here; page (suppl. PDF p. 14) per VER-CW5]: "introducing the (single-spin) electronic density of states (DoS) n". CW5-C8b
(replaced) checks the Born limit numerically on the 1D chain: at v = ±0.15 the fitted α_ohm = 0.00895, the exact-phase value 0.00898 and 4K_σ = 0.00912
(ρ_σ = 1/π). It also checks the spin counting (factor 1 with K_both). The old C8b restated its own algebra and is removed.

### A23. Row 23 (CW5 §3.3 table, Al row): "≥ 6%" → "**≥ 5.6%**" (1 − 23.6/25 = 0.056; Si 14.2%; CW5-C9).

### A24. Row 24 (CW5 §3.4 table row 1 and the sentence under it) — STANDS WITH CORRECTION
1705.01108 [FT, read here; page (PDF p. 13) per VER-CW5]: "σ ≈ 0.4 - 0.5 (GHz µm2)−1 … Assuming a typical tunnel barrier thickness of 2-3 nm, these measurements correspond to defect
densities of σ ≈ 102 /(µm3 GHz)". Replacement: "σ = 0.4–0.5/(GHz µm²) over 2–3 nm, i.e. (1.3–2.5)×10²/(µm³ GHz) (the source rounds to ≈ 10²) =
**(3.2–6.0)×10¹⁹ /(eV cm³)** per unit E (CW5-C15)". Also CW5 §3.9 "tanh(hν/2k_BT) = 0.99999 at 25 mK" → "**0.99998**" (CW5-C15; found while re-checking).

### A25. Row 25 (CW5 §3.5 (b), last sentence): delete "It is also exactly the type-T tilt θ_𝒦 of WP6." No derivation exists; none is attempted here.

### A26. Row 26: L30 scope and the T < Δ_dfn citation (CW5 §3.7 "Limits"; status; L30 row) — STANDS WITH CORRECTION (qualified, §C-R2)
Status: "L30 (T⁻⁹) → **DERIVED (exponent)**; prefactor [FT] (cond-mat/0310283 Eq. (61))". Replacement for the first "Limits" sentence: "For T < Δ_dfn
(effective-mass regime) cond-mat/0310283 Eqs. (55)–(56) give the kinematics (phonon wave-vector change), and the source's diffusion law there is Eq. (64),
D_B ≈ 0.59(as/σ₀)(θ_p/T)⁷ (Boltzmann defectons) [FT, PDF p. 8]; it is not derived here."

### A29. Row 29 (CW5 §4.2 (iii)) — STANDS WITH CORRECTION
Prediction 4 is replaced by: "(H-L3) states that shape and time law factorise. This is a hypothesis, not a prediction. A time-dependent spectral shape falsifies
(H-L3), not (CW5-9)'s 1/t law." Add after (CW5-9): "τ_av = 3/2 is the size law in the number of releases s (CW5-C13 tests it in s). It carries over to energy,
E = Σ_{i≤s}E_i, if the per-release energies are iid with finite mean, because then P(E_1 > x) = o(x^{−1/2}) and P(E > x) ~ P(s > x/⟨E_1⟩) [D, sketch:
random-sum asymptotics]. Otherwise p(E) is a compound law and τ_av must be fitted." The 2208.02790/2202.05097 quotes stay "[FT as read in WP7-E-v3 §3.3; not
re-read]".

### A32. Row 32 (CW5 §4.6): "exact **iff** the marks are a sufficient statistic" → "exact **if** the marks are a sufficient statistic for Λ (then TV = 0).
The converse fails: ΔP = 0 can hold with TV > 0 when 𝒫_det ignores the omitted features." Spec completion: §C LE-149.

### A34. Row 34: LE-137 Method B (CW5 §3.10; code/CW5/LE-137/) — STANDS WITH CORRECTION
Replacement for "Method B": "ph.x at q = Γ of the supercell (xq = 0), nat_todo restricted to the core atoms, fildvscf/fildrho on. A supercell vector G_sc
is equivalent to Γ, so **one** Γ response gives δρ_κ at every G_sc as its Fourier components; vertex Σ_Iδρ_κ(G_sc)·(u_I^R − u_I^L). scf.in must use
`K_POINTS automatic 1 1 1 0 0 0` (ph.x does not support the Γ-trick wavefunctions of `K_POINTS gamma`), which costs ≈ 2× in memory and SCF time [E]." In
"Inputs and grids": "Γ only" → "Γ only (as `automatic 1 1 1 0 0 0`)". Applied in code/CW5/LE-137/{scf.in, ph.in, notes.txt}.

### A35. VER §4 minor items not covered above
- §2.5 (CW5-4) "Σ_kw_k = 1": holds; w_k of either sign (A17).
- §6 checks table: "C7 … variance factor" → "second-moment factor"; "C6, C6b … bimolecular r_g" → "C6b: ODE r_g = n_F + n_X (row 18)"; C18 → "bookkeeping".
- C17 label "cap 92.6" → 92.7 (CW5 text "93" stands).

---
## B. Re-issued owed corrections and LIMITS rows (merger: use this section only)
**Owed corrections.** OC-3, OC-6, OC-7, OC-8, OC-11: **unchanged** (as in CW5.md). OC-7's 220/100 eV support is in ERR-CW5-C1, and its text is unchanged.
| ID | Target | Type | Exact text (complete replacement) |
|---|---|---|---|
| OC-1 | WP5-AUD §1.2 D-1 bullet, D-1 row, AUD-C3d label, R-e; WP5-v4 A-4/(W11); WP7-E-v3 (E7)–(E8) | S | "D′ ≡ E_st(t_win) + E_pairs(t_win) + E_X(t_win) + E_trap(t_win) + E_es^{trap} + ΔZPE(t_win) + E_esc, used only in the exact ratio Y_H = (1 − δ_coll)(ω − D′_NR)/(ω − D′_ER). At zero field Y_H = (1 − δ_coll)[1 − 𝔶𝒢_gap r_g^{NR}(t_win) − d′^{oth}_NR]/[1 − 𝒢_gap r_g^{ER}(t_win) − d′^{oth}_ER], 𝒢_gap = E_g/ε_eh, r_g ≡ [E_pairs + E_X](t_win)/(N_ehE_g) (trapped and escaped gap energy are already in E_trap, E_esc). Si, 100 eV, r_g = 1: 1.407 (+0.41); the first-order term 0.28 is invalid because 𝒢_gap r_g ≈ 0.31. (W11)'s first-order form requires 𝒢_gap r_g(t_win) ≪ 1. Excitons carry E_g − E_x^b each. r_g^{NR} ≠ r_g^{ER} whenever a bimolecular gap-energy **loss** channel (X–X annihilation, Auger) acts within t_win (CW5 (CW5-4); CW5-errata (E.3)–(E.6)); bimolecular exciton formation alone does not change r_g. 'L36–L38 numbers unaffected' → '[E]: drift ≈ 1 µs (Si, 4 V/cm) and ≈ 2.5–25 µs (Ge iZIP, ±2 V, ≈ 1.6 V/cm [E: 25.4 mm thickness assumed, not stated in 1805.09942]) against ≳ 100 µs windows'." |
| OC-2 | WP5-AUD D-2; WP5-v4 A-12 | N | D-2 reclassified as clarification. Append to A-12: "(E7) counts 𝒲_bias(t_pr) once, inside NTL heat; never weight ℋ_pr (which contains it) by ϵ_prim. Its collection efficiency lies between ϵ_prim and ϵ_NTL [E]; ≤ 0.25 eV per carrier at 250 V/cm, saturated drift, t_pr = 100 ps [E] (WP7-E-v3 C15)." |
| OC-4 | WP5-AUD B-2 | W | "N_eh ≤ ⟨N_eh⟩ + 6σ (≥ 100 at 1 keV); trajectories per point ≥ 1112 for 6% on the variance at κ_ex = 2 (error √(2/(n − 1) + κ_ex/n); 8.9% at n = 500); 2303.02196's sub-keV E_r is set by neutron kinematics; its Eq. (1) books the non-NTL phonon energy as E_r (unit heat quenching), which is the L37 truncation; ⟨𝔮⟩ = 0.873 is a worst case from detector-model trapping probabilities [E]." |
| OC-5 | LIMITS L38 (Validity, Status) | W | Validity: "… hypotheses (B-a), (B-b) r_coll ≥ 1, (B-d), X^{oth}_NR ≥ κ_cal(r_coll)X^{oth}_ER (implied by κ_cal(1) for r_coll ≥ 1 only), on the domain d′_NR ≤ 1, δ_coll ∈ [0, 1], E_st/ω ∈ [0, 1 − y_ion]. For X^{oth}_ER ≥ 0: E_st/ω ≤ 1 − η^φ_NR. For X^{oth}_ER < 0 (ΔZPE of either sign): E_st/ω ≤ (1 − η^φ_NR)/(1 − c_X), c_X = X⁻(1 + g_Luke)/[(1 + r_collg_Luke)(1 − X^{oth}_ER + r_collg_Luke)], X⁻ = −X^{oth}_ER (exact; c_X ≲ 5×10⁻³ in the physical region)"; Status: "DERIVED (AUD-1: AUD-C1, REF-A/B; bound: REF-B §2 proof, CW5-C3 as revised in CW5-errata (E.1)–(E.2))". REFEREED is recorded by the coordinator after the R16 round, not here. Chain: move "g_Luke = 4/3.82 [FT]" out of the remainder clause. |
| OC-9 | WP5-v4 §1.5 (sampler), §3.1 | S | "Defect seeds exported at phonon poles (WP7-T-v2 (1.3), IF-T9) carry the signed weight (π\|B\|²/η_pole)δ − 2πIm(a*B)δ. Both terms seed the same pole state: per q bin the class weight is K_q = π\|B\|²/η_pole − 2πIm(a*B), non-negative wherever \|Im(a*B)\| ≤ \|B\|²/(2η_pole). Where any class weight (K_q or the Fano K_ν) is negative, sample all classes with \|K_i\|/Σ\|K\| and score sign(K_i)Σ\|K\|; never clip. Report the second-moment factor (Σ\|K\|/ΣK)² (exact relative to the \|K\|-weighted estimator; the variance is not bounded by it). The class sum Σ_iK_iP_i(N_eh) is ≥ 0 for every N_eh, to O(η_pole), when all classes use the same P(N_eh\|x) (O4-d8/d9); report min_{N_eh} of the class sum and treat a negative value as a cascade-consistency failure." |
| OC-10 | WP5-v4 §6.4 "Asymptotics"; LIMITS L23 | W | "n̄(ω) = ω/ε_eh + o(ω) is DERIVED (CW5 §2.7 with CW5-errata §A12: tagged-unit identity (CW5-5), coupling to the scale-free lineage, key renewal theorem for the undershoot, under (r1′)–(r5′); (r4′): ‖K_x − K_∞‖_TV ≤ C(E_g/x)^κ; (r5′): bounded, continuous threshold-region functional). The constant b_N and Var N_eh = F_ehω/ε_eh + O(1) remain [D, sketch] (second-order renewal). CW5-C5 tests toy identities only." |
| OC-12 | LIMITS L32 (last cell); WP8-F (4.2) "tanδ₀ of a-SiO₂ not quoted" | W | "tanδ₀ (low power, mK, ~6 GHz): thermal SiO₂ 3.0–3.3×10⁻⁴ and PECVD SiO₂ 2.7–2.9×10⁻³ (0802.2404 Table I [FT]); PECVD a-SiO₂ (SiH₄ + O₂) ≈ 5×10⁻³ at 25 mK (cond-mat/0507622 PDF pp. 3, 7 [FT]); the two PECVD films differ by ≈ 2× (preparation, OH content); divide by tanh(hν/2k_BT) = 0.894 if taken at 100 mK; bulk fused-silica mK value GAP." |

**Proposed LIMITS rows (complete replacements for the CW5 rows named; the L36 row is unchanged).**
| # | Change / chain | Source | Validity | Leading correction | Status |
|---|---|---|---|---|---|
| L30 ✎ | Status "(T⁻⁹) [D, sketch]" → DERIVED (exponent): one-phonon forbidden (v_max ≪ c), two-phonon amplitude ∝ ω in both coupling channels, transport factor (qa)² | cond-mat/0310283 Eqs. (12), (49), (54), (61) [FT] | Δ_dfn ≪ T ≪ θ_p, dilute | T < Δ_dfn: kinematics Eqs. (55)–(56), source law D_B ∝ (θ_p/T)⁷ Eq. (64) [FT, p. 8] (not derived); defecton–defecton D ∝ 1/(xσ); localisation Eqs. (17)–(18) | DERIVED (exponent, CW5-C4); prefactor [FT] Eq. (61) |
| L32 ✎ | tanδ₀ values (OC-12) | 0802.2404, cond-mat/0507622 [FT]; bulk-quartz relation is the latter's secondary quote (its refs 13, 22), PDF pp. 6–7 | low power, T ≪ hν/k_B | OH content; bulk vs film; PECVD film-to-film ≈ 2× | ✎ |
| L37 ✎ | Validity: "r_g^{NR,ER}(t_win)𝒢_gap ≪ 1 (else the exact-ratio D-1 form (CW5-3))" | — | — | (CW5-4); bimolecular loss (E.3)–(E.6) (annihilation 1/(1 + t/t₀), Auger (1 + 2t/t₀)^{−1/2}, diffusion-limited forms) | DERIVED |
| L38 ✎ | OC-5 | 1803.02903 [FT] | (B-a), (B-b), (B-d); X^{oth}_ER ≥ 0, else (E.2) | O(d′², δ_colld′); c_X for X^{oth}_ER < 0 | DERIVED (REFEREED to be recorded by the coordinator after R16) |
| L42 ✎ (WP8-R) | OC-7 text | [FT] (2303.02196, as read by REF-WP5-AUD-A/B) | 1σ bands | ⟨𝔮⟩ [E] | CONDITIONAL |
| new (α_ohm) | (CW5-6) → Born limit α_ohm = 4K, K = (N_σVΩ)², Black rate | 2009.03804 Eq. (4) p. 4, K values p. 5, single-spin n₀ suppl. p. 14 [FT; page per VER-CW5] | weak coupling (K ≪ 1); per-spin DOS (with a both-spin K: α_ohm = K, factor 1) | eigenphase form beyond Born; displaced scatterer | DERIVED (Born, CW5-C8b revised); [D, sketch] (6) |
| new (renewal) | (W3) → tagged-unit (CW5-5) → m(E) = E/ε_eh + o(E) | key renewal theorem for the undershoot (textbook); coupling under (r4′) | (r1′)–(r5′) | b_N, variance: [D, sketch] | [D] (CW5-errata §A12); CW5-C5 tests toys only, not evidence |
| new (gap release) | WP7-E-v3 (E1) + linear pair kinetics → r_g(t) = Σ_kP_k(t)e^{−γ_kt} (CW5-4); only gap-energy **loss** lowers r_g; bimolecular loss (E.3)–(E.6) | — | (H-g1)–(H-g3) for (CW5-4); geometry regime stated for (E.3)–(E.6) | droplets; rates at mK; w_k of either sign | DERIVED (CW5-C6, C6b revised; ERR-CW5-C3, C4) |

---
## C. Thin specifications completed; missing steps listed (VER-CW5 §2) — and Rebuttals
Each spec gives what is computed, the approximation level, the method and convergence, and the pitfalls. LE-129, LE-130 and LE-147 were ruled ADEQUATE and are unchanged.
- **LE-138 (addition).** Convergence target: ζ(E) to 2% per 50 meV bin under N_G 250 → 350, empty bands 200 → 400 and k per bin 10³ → 2×10³. The SOSEX term
  is reported separately to the same 2%. A variation of ζ(E) below 2% over [E_th^{ii}, 10 eV] counts as constant (absorbed by 𝒜_ph).
- **LE-139 (completed).** *What:* osc_k m_k(E) for m = mean pair number and its second moment, Si, 3–8 eV, 50 meV bins, and w_mem(E). *Level:* (H-BGK)
  relaxation-time closure, first order in w_mem per generation. *Method:* the k-resolved n_gen = 2 subset of WP5 §2, ≥ 200 k samples per iso-energy bin
  (area-weighted on the surface), ≥ 10³ cascades per k sample. Γ_k from EPW (intervalley + acoustic, the WP5 (W2) g^S); Γ_E = Γ_ii (G0W0 Im Σ, LE-138 grid) +
  phonon-loss rate (EPW). *Convergence:* osc to 10% under k samples 200 → 400 and cascades 10³ → 4×10³. *Pitfalls:* (H-BGK) is itself an (R-k)-type closure
  (§A16). A max − min of noisy estimates is biased upward by ≈ 2σ_m√(2 ln n_k), so use the 5–95% quantile range or subtract the noise. Γ_k and Γ_E must come
  from one EPW/GW run (no mixed DFT/QP energies).
- **LE-141 (completed; the missing input is a rate set, not a single number).** *Missing:* {k_FX, k_FT, k_XB,j, k_B↓,j, η_X, η_B,j, C_X} and, for dense
  tracks, the **loss** coefficients γ_XX and C_A(mK) with n₀, r₀ and D_X of the NR track (§4.5). *Convergence:* exciton levels (G0W0 + BSE) to 1 meV under
  k-mesh 8³ → 12³ (dense near the band edges; E_x^b ≈ 15 meV) and BSE bands 4v4c → 6v6c; D⁰X/A⁰X central-cell DFT in 216 → 512-atom cells, binding energies to
  10%; C_X(T) and the rates at 10, 20 and 50 mK. Rate changes of more than 10% across that range are reported as T-dependence. *Pitfalls:* name the bimolecular
  channel, because formation does not lower r_g and loss does (row 18); state the geometry regime ((E.3)–(E.5) non-diffusing; (E.6) diffusing cloud or cylinder);
  exciton cooling by acoustic phonons is slow at mK, so the exciton temperature is not the lattice temperature; E_x^b(Si) stays [UNVERIFIED].
- **LE-131 (completed).** *What:* b_br, the mean number of releases triggered by one release's phonon pulse. *Level:* first generation, linear in the phonon
  flux, ballistic phonons. *Method:* the pulse of a release E_rel is propagated by phonon Monte Carlo (G4CMP-type: anisotropic focusing, isotope scattering,
  anharmonic down-conversion; mode- and frequency-resolved flux Φ_ph(r, t)). A catalogue site (WP7-T-v2 §4.6) with barrier V_b triggers with probability
  p_trig(r) = 1 − exp[−∫dt Γ_ij(t; Φ_ph)], where Γ_ij is the phonon-assisted rate driven by the absorbed flux at ω ≳ V_b. Triggering volume V_trig ≡ ∫d³r p_trig(r)
  and b_br = n_bar(V_b < E_ph)·V_trig, averaged by KMC over 10⁶ seeds. *Convergence:* b_br to 10% under catalogue 50 → 100 paths, phonon packets 10⁵ → 4×10⁵ and box
  L → 2L. *Pitfalls:* a finite box truncates V_trig (absorbing boundaries or L ≫ phonon mean free path); an incomplete catalogue (missing low barriers) biases
  b_br low; the bath and the pulse must not both drive the same rate; the pulse spectrum depends on E_rel, so b_br(E_rel) is energy-dependent.
- **LE-144 (completed; two missing steps).** (1) p_FH(T) at mK; (2) p_surv of the close F–H pair. ε_X and E^{conf}_FH come from the same ΔSCF. *Convergence:*
  cells 64 → 216 atoms (F–H separations up to the third neighbour), hybrid fraction 0.25 → 0.40 (report both), ≥ 10³ surface-hopping trajectories, p_FH to ±10%.
  *Pitfalls:* STE localisation (on- vs off-centre) depends on the hybrid fraction; surface hopping needs a decoherence correction (FSSH over-coherence); at mK
  only the athermal channel acts; charged components need finite-size electrostatic corrections.
- **LE-145 (completed; two missing steps, not "single").** (1) U_rel with its rate spread (Γ_min, Γ_max) for a given holder and glue; (2) b_br, which fixes τ_av
  and E_cut^{av}. *Spec:* (a) FEM of the cooldown 300 K → 10 mK with C_ij(T), α(T) of crystal, glue and holder (data), U_el per component converged to 5% under
  mesh refinement ×2; the relaxable fraction and its ln Γ spread from low-T dynamic mechanical data of the glue. (b) No MLIP for cured epoxy at mK exists:
  train one (ACE/NequIP class) on dispersion-corrected DFT of the cured network and the crystal–epoxy interface, validate on elastic constants and thermal
  expansion, add bond-breaking configurations by active learning; 10⁶ atoms at 1–10 K; event energies from energy drops; event-energy law stable under box
  10⁶ → 4×10⁶ atoms. (c) Fit (CW5-9) jointly. *Pitfalls:* MD reaches ns, so it gives the event-energy law, not the rates (those come from (a)); the glue
  structure depends on curing; MLIP transferability to crack events is not assured without the active-learning step.
- **LE-149 (addition).** The spec estimates ΔP (the observed difference in N^meas and E_sig between full and mark-resampled microstates), **not** TV, which is
  high-dimensional and is not computed. Sample size: n_traj = 2p(1 − p)(z/ΔP)² per arm, i.e. 2×10⁴ per seed class for a 2σ resolution ΔP = 0.01 at p = 0.5
  (ERR-CW5-C5). Common random numbers between arms lower this. Pitfall: ΔP = 0 does not imply sufficiency (§A32).
- **LE-151 (relabel).** "Single missing step" → "**two** missing steps: p_q·p_surv·f_opt at sub-keV recoils, and p_FH(T → 0)". Measurement proposals unchanged.

### C-R. Rebuttals and refinements of VER-CW5 (each with its check)
- **R1 (row 18, verifier's fix (b)): conceded with a qualification.** The verifier's 1/(1 + t/t₀) (annihilation) and (1 + 2t/t₀)^{−1/2} (Auger) are exact only for
  a non-diffusing density (4D_Xt ≪ r₀²). In a diffusing track the bimolecular loss rate falls with the density. sympy (ERR-CW5-C4): ∫n²dV = N²/(2√2(πs)^{3/2}),
  so a compact cloud's loss **saturates** at 1/N_∞ − 1/N₀ = γ/(4√2π^{3/2}Dr₀); a cylinder has ∫n²dA = λ²/(2πs), giving a **logarithmic** decay. The
  verifier's proposed D-1 tail 𝔶𝒢_gap t₀/t_win therefore needs 4D_Xt_win ≪ r₀² and k_X↓t_win ≪ 1, and §B states both conditions. The NR ≠ ER conclusion
  survives in all regimes, through the density dependence of t₀, N₀/r₀ or λ₀.
- **R2 (row 26): refined.** The verifier is right that Eq. (55) is kinematics, not a D law. The advice to "cite (55)–(57) as kinematics only" is incomplete: the
  source gives a T < Δ diffusion law, Eq. (64), D_B ≈ 0.59(as/σ₀)(θ_p/T)⁷ ("If at the same time T < Δ, then Boltzmann statistics applies", [FT, PDF p. 8], read
  here). §A26 cites it, and the L30 row lists it as the leading correction.
- **R3 (row 2): the replacement number is itself an assumption.** VER's "≈ 1.6 V/cm" assumes a 25 mm crystal that 1805.09942 does not state (VER says so;
  confirmed here). It is tagged [E]/[UNVERIFIED]. The drift time at that field depends on v_d at 1.6 V/cm, which no source here gives, so a range (2.5–25 µs,
  ERR-CW5-C5) replaces a point value. The [E] conclusion holds at the slow end with margin ≥ 4.
- **R4 (row 11, last sentence): partly rebutted.** VER: "CW5 has not shown Σ_iK_iP_i(N_eh) ≥ 0 for every N_eh". It was not shown in CW5. It follows, to O(η),
  from w(x) = |a + B/(x − iη)|² ≥ 0 and P(N_eh|x) ≥ 0 whenever the classes share one cascade law (§A11(c)), so it is a consistency diagnostic, not an open
  physics condition. VER's "sampler unnecessary if the per-bin condition holds" is right for defect seeds alone. In WP5's joint sampler the Fano K_ν can still
  be negative (WP5-v4 §1.5), so the sampler stays.
- **R5 (row 12): a weaker tool suffices, and one condition was missing.** VER asks for a Markov-renewal theorem (Kesten, Alsmeyer). The leading term needs only
  the iid key renewal theorem plus coupling under (r4′) (§A12). VER's list (a)–(c) also omits the regularity of the threshold-region functional ((r5′)), which
  the convergence of 𝔼h_c(x_τ) needs. VER's (b) is used as an *expected* sum (to bound the coupling failure), not only an a.s. sum.
- **No rebuttal (verified, conceded):** rows 5 (1112; CW5-C17), 6 (counterexample reproduced; CW5-C3), 11 (f ≡ 1: 0 → 0.21; CW5-C7), 18 (V3 reproduced;
  CW5-C6b), 21 (factor 1; CW5-C8b), 23 (5.6%; CW5-C9), 24 ((3.2–6.0)×10¹⁹; CW5-C15), 14 (PECVD quote read here, PDF p. 7).

---
## D. Changes to code/CW5/checks.py (26 checks, 13–35 s; was 21 in 19 s)
| Label | Change |
|---|---|
| all | tolerances: every quoted number checked to half a unit of its last quoted digit (TOL); Monte Carlo checks (C5c, C7, C16) at 4 SE from the sample |
| CW5-C1, C2 | tightened (C1: 2×10⁻³ → rounding-consistent; C2: 1–3×10⁻³ → rounding-consistent, ε 3.8 F_NR* added to the test) |
| ERR-CW5-C1 | new: 220 eV and 100 eV 1σ corners (row 8) |
| CW5-C3 | revised: exact identity (E.1), f₀\|_{r=1} = Xe, VER counterexample, sharpened bound (E.2) over X ∈ [−0.2, 1] and the full (x, δ) domain (20 000 points) |
| CW5-C5 | relabelled "toys only"; MC at 4 SE. **ERR-CW5-C2** new: (r4′) mechanism (killed lineage, log-grid integral equation; a = 0 reproduces 2 − 1/x) |
| CW5-C6 | revised: η_B, w_k from the eigen-decomposition (a negative weight), diagonal γ_k. **ERR-CW5-C3** new: degenerate rates, negative weight (sympy) |
| CW5-C6b | **replaced** (was circular): ODE integration of r_g = n_F + n_X; VER V3 numbers; (E.3)–(E.5). **ERR-CW5-C4** new: diffusion integrals and log law (E.6) |
| CW5-C7 | revised: second-moment factor exact, f ≡ 1 variance counterexample; unbiasedness at 4 SE |
| CW5-C8b | **replaced** (was a restatement): numerical Born limit on the chain at v = ±0.15; spin counting (factor 1 with K_both) |
| CW5-C9, C10, C15, C17 | revised: 5.6% and 14.2%; 0.1196; (3.2–6.0)×10¹⁹, 0.99998; n_min = 1112, 8.95%, cap 92.7 |
| ERR-CW5-C5 | new: Ge field and drift range, LE-149 n_traj, E_x^b/E_g |
| CW5-C18 | labelled BOOKKEEPING; adds the two Crossref records and checks that no PDF is kept |
Also code/CW5/LE-137/: scf.in `K_POINTS automatic 1 1 1 0 0 0`; ph.in xq = 0 (one Γ run for all G_sc); notes.txt updated (§A34).

## E. Symbols introduced here (NOTATION grep: no collisions)
| Symbol | Meaning | Where |
|---|---|---|
| 𝔼, 𝔼_unit | expectation (replaces CW5's "E N(E)", "E_unit") | §A12 |
| X⁻, c_X | max(−X^{oth}_ER, 0); relative correction of the L38 bound | (E.2) |
| γ_XX, t₀ (per channel), D_X, N₀, λ₀ | exciton–exciton annihilation coefficient; bimolecular time scale; exciton diffusion constant; initial pair number / line density of a track | (E.3)–(E.6) |
| η_B,j, P_k(t) | BX luminescence fraction; polynomial weights of r_g for degenerate γ_k | §A17 |
| K_x, K_∞, ξ, x_c, h_c, κ | lineage kernel at energy x and its scale-free limit; log decrement; cut energy; threshold functional; approach exponent (local) | §A12 |
| K_q | per-q-bin defect-seed class weight | §A11 |
| (E.1)–(E.6), ERR-CW5-C1…C5, (r4′), (r5′) | labels (prefix ERR-CW5) | — |

## F. Closing table (verifier item → resolution → location)
| VER item | Resolution | Location |
|---|---|---|
| 1 OC-1 / D-1 exact ratio | STANDS, no action (C1 tightened) | §D |
| 2 drift sentence, Ge field | corrected: ±2 V [FT p. 2], ≈ 1.6 V/cm [E, thickness unstated], drift 2.5–25 µs [E] | §A2, §B OC-1, §C-R3 |
| 3 OC-2 "≤ 0.25 eV" tag | [E] tag and its source added | §A3, §B OC-2 |
| 4 OC-3 | STANDS, no action; OC-3 unchanged | §B |
| 5 OC-4 n ≥ 1100 | → 1112; also 9.0% → 8.9% | §A5, §B OC-4, CW5-C17 |
| 6 OC-5 / L38 X < 0 | exact sharpened bound (E.1)–(E.2); X ≥ 0 stated; REFEREED removed | §A6, §B OC-5, L38 row, CW5-C3 |
| 7 OC-6 | STANDS, no action; OC-6 unchanged | §B |
| 8 OC-7 / D-7 | STANDS; 220 eV (1.72; 1.70–1.87) and 100 eV (1.27) corners added | §A8, ERR-CW5-C1 |
| 9 L42 tag | corrected | §A9, §B L42 row |
| 10 OC-8 | STANDS, no action; OC-8 unchanged | §B |
| 11 OC-9 signed sampler | variance → second moment (conceded); class structure; positivity per N_eh derived | §A11, §B OC-9, §C-R4, CW5-C7 |
| 12 OC-10 / renewal | (r4′), (r5′) added; proof written; C5 not evidence; 𝔼 notation | §A12, §B OC-10, renewal row, §C-R5, ERR-CW5-C2 |
| 13 OC-11 Andreev–Lifshitz | STANDS, no action; OC-11 unchanged | §B |
| 14 OC-12 PECVD | relabelled (PDF p. 7 quote) | §A14, §B OC-12, L32 row |
| 15 LE-138 "≤ 2.7%" | "≈ 2.7% (Z part) [E]"; convergence target added | §A0, §A15, §C |
| 16 (CW5-1) overclaim | conditional on (H-BGK) | §A16, §C LE-139 |
| 17 Theorem CW5-G | lower-triangular M, degenerate case, w_k sign, η_B | §A17, CW5-C6, ERR-CW5-C3 |
| 18 bimolecular r_g | **FALLS → re-derived** (E.3)–(E.6); OC-1, L37, gap-release row follow; C6b replaced | §A18, §B, §C-R1, CW5-C6b, ERR-CW5-C4 |
| 19 E_x^b ≤ 1.3% | STANDS, no action (ERR-CW5-C5 records 1.26%) | — |
| 20 (CW5-6) | STANDS, no action | — |
| 21 α_ohm factor 2 | → factor 1; Born limit checked numerically | §A21, α_ohm row, CW5-C8b |
| 22 §3.2 S_HR | STANDS, no action | — |
| 23 Al 6% | → 5.6% | §A23, CW5-C9 |
| 24 σ conversion | → (3.2–6.0)×10¹⁹ /(eV cm³); also 0.99998 | §A24, CW5-C15 |
| 25 θ_𝒦 identification | deleted | §A25 |
| 26 L30 scope; Eq. (55) | exponent only; (55)–(56) kinematics, Eq. (64) T⁻⁷ cited [FT] | §A26, L30 row, §C-R2 |
| 27 §3.8 | STANDS, no action | — |
| 28 (CW5-8) | STANDS, no action | — |
| 29 Prediction 4; τ_av | hypothesis restated; energy carry-over condition | §A29 |
| 30, 31 (CW5-10), (CW5-11) | STANDS, no action | — |
| 32 TV "iff" | → "if"; converse fails | §A32, §C LE-149 |
| 33 LE-150 | STANDS, no action | — |
| 34 LE-137 Method B | Γ run, `automatic 1 1 1`; inputs fixed | §A34, code/CW5/LE-137/ |
| §2 LE-138 | convergence target | §C |
| §2 LE-139, 141, 131, 144, 145 | specs completed; LE-141 rate set; LE-144, 145 two steps | §C, §A0 |
| §2 LE-149 | ΔP not TV; n_traj | §C, ERR-CW5-C5 |
| §2 LE-151 | two steps | §C, §A0 |
| §2 LE-129, 130, 147 | ADEQUATE, no action | — |
| §3 L30, L32, L37, L38, L42, α_ohm, renewal, gap release | re-issued | §B |
| §3 L36 | STANDS, unchanged | — |
| §4 minor items | applied | §A5, §A17, §A23–§A25, §A29, §A35, §D |
