# R7 / REF-WP4-A: hostile referee report on returns/R6/WP4-v2.md

Referee A, isolated. Read: WP4-v2.md, code/WP4-v2/checks.py (run: 23/23 PASS, < 1 min), CONVENTIONS, NOTATION, CONTROLS, DONE,
LIMITS, WP0-v2 §3, §4, §6.2. Full texts fetched with lit.py (deleted afterwards): 1708.08929, 1910.02091 (v2), 2101.08263,
1512.04533, 2609.06423, 2412.16279, 2009.13534. No numerical simulation. Sympy checks only (the package's own script).

## Verdict table
| # | Claim (WP4-v2 location) | Verdict | One-line reason |
|---|---|---|---|
| V1 | §5.3 / OW4-2: 1708.08929 and 1910.02091 omit the background factor 1/ε_bg² (conditional statement) | **STANDS, now unconditional** | All three conditions verified in both full texts (§1). Rate is ε_bg² too large, exact for any δε_D. One explanatory sentence is wrong (§1.4) |
| V1′ | (new, not claimed by WP4) dark-photon *absorption* in both papers | **referee finding** | The same omission makes their absorption rates ε_bg (not ε_bg²) too large (§1.5) |
| V2 | [5.1] L16 chain, K5, 2101.08263 Eq. (4) recovered | STANDS | Verified: 2101.08263 (S.21)–(S.22) uses the total ε and 1/κ², which agrees with the URF |
| V3 | [5.2] anisotropic background q̂·ε_bg·q̂; typo in 1910.02091 Eq. (3.14) | STANDS | Typo CONFIRMED in (3.13) and (3.14) (q_x²v_{F,z}²/κ_xx). The ratio 366 is larger along q ∥ y. State which direction is larger |
| V4 | §5.4(i) charge renormalisation 0.27, rate factor 0.62 (K17) | STANDS WITH CORRECTION | The number depends on the cutoff convention: with 1708.08929 Eq. (2.6) (MS-bar, μ̃ = 2v_FΛ) the value is 0.35 and the factor 0.55 (§6) |
| V5 | [4.1] conserving GRPA, K2: R̃^{GRPA}(0,ω) ≡ 0, while the bare bubble ≠ 0 | STANDS WITH CORRECTION | Algebra verified. But 2609.06423 already introduces the phase-field polarisation Π_θ (their Fig. 3) and bounds it by Δ²/(v_FQ)² ≤ 1/25. WP4 does not credit this, and its §14 "no conserving BCS ε found" overstates novelty (§2.2) |
| V6 | [4.2] 𝔤_I(y) closed form (K4) | STANDS | Re-derived: the endpoint and the asymptote are right, and the quadrature matches to 10⁻¹². Novelty not verified (priority check owed) |
| V7 | "rate_BCS/rate_Lindhard = 𝔤_I is the analytic form of 2609.06423's agreement for ω ≳ 5Δ" | **FALLS** | 2609.06423's 5Δ statement compares \|ε_BCS\|²/\|ε_Lin\|² (screening). Their Eq. (10) keeps Im ε_BCS, so 𝔤_I is not what they compare (§2.4) |
| V8 | [4.6] η_pb = Δ_BCS⟨N_qp⟩/ω, = 2Δ/ω for ω < 3Δ | STANDS WITH CORRECTION | The definition and the threshold value are right. N_qp = 2 holds up to ω < 4Δ_BCS, not 3Δ_BCS (§2.5) |
| V9 | K1: 2101.08263 Eq. (3) Re ε should be k_TF²/q², not k_TF²/2q²; factor 4 in W | STANDS (CONFIRMED) | Their own (S.13)–(S.15) with λ_TF² = 3ω_p²/v_F² give a bracket → 1 |
| V10 | K7: 1512.04533 Eq. (13)/(3.3) e₋ lacks a 4 | STANDS (CONFIRMED) | Printed e₋ = (E_D − q²/2m)²/(q²/2m). The Pauli-blocking minimum is (E_D − E_q)²/(4E_q) |
| V11 | 2609.06423 Eqs. (4), (7) are "time-ordered, not retarded", listed as a source defect | STANDS WITH CORRECTION | The fact is CONFIRMED. Calling it a defect is REFUTED: Eq. (4) is the correct T = 0 Feynman propagator, the paper works only at T = 0 and ω > 0 and says so ("for ω > 0"), and it never calls it retarded |
| V12 | 2101.08263 attributes W(q,−ω) = −W(q,ω) to causality | STANDS WITH CORRECTION | CONFIRMED that they do. WP4's replacement "causality alone gives ε(q,−ω) = ε(−q,ω)*" is also misattributed: that relation follows from reality of the density kernel, not from causality |
| V13 | [4.4] Mermin: L_Mer/L_Drude → πqℓ/6 (qℓ ≫ 1), → 1 (qℓ ≲ 1) | STANDS | Re-derived, including the first-order survival of the Lindhard Im ε inside Mermin for ω ≪ γ_rel (§3) |
| V14 | "QROCODILE's Drude ε underestimates L by πqℓ/6; conservative for their limit" | **FALLS** | 2412.16279 SM §I: the bulk rate uses **Lindhard** (Γ = 0.1E_F). Drude appears only in the thin-layer anisotropy/modulation model. WSi with ℓ_mfp ≈ 0.3–1 nm (k_Fℓ ~ 1) is outside the relaxation-time model (§3) |
| V15 | [3.1] reciprocity: a v-odd rate needs P and T both broken | STANDS | Verified (antiunitary Θ n(q) Θ⁻¹ = n(−q)). "iff" holds only as a necessary condition for the integral |
| V16 | [3.3] chiral 𝒪₅×𝒪₈ selection rule; v1 −½ factor fixed | STANDS | Hand contraction reproduces K12, with 𝔇_ab = ½tr(𝒱_a†𝒱_b) matching WP0-v2 (3.1)/(3.3) ordering. The P and T parities of 𝒪₅ and 𝒪₈ are verified (§4) |
| V17 | §8 Theorem D-g (a) "[D given U_qp]": PSD, complete, no double counting | STANDS WITH CORRECTION | Completeness needs [H, U_qpN̂U_qp†] = 0 (or a stated O(·) bound). With finite Γ_qp, the cross terms 𝒬_n δ(ω−H) 𝒬_{n′} do not vanish. The added hypothesis is the bin condition (c), so (a) is conditional on a [C] item (§5) |
| V18 | L13 chain [2.1]–[2.2], K6. 2009.13534 Eq. (36) S′^x,S′^y are really S′^± | STANDS (CONFIRMED) | Eq. (36) as printed is non-Hermitian for "S′^x". It is notational only, as WP4 says |
| V19 | §4.3 validity: "q ≥ 2Δ_BCS/v_max ≈ 0.13 keV" | STANDS WITH CORRECTION | 2×0.17 meV/2.65×10⁻³ = 0.13 **eV**. qξ_coh ≥ 1.6 is right (it uses eV consistently). The "all DM kinematics has Q₊ < 1" claim fails for q ≳ 4 keV in Al |
| V20 | [7.2] exothermic lines, halo-independent to O(v/v*) | STANDS WITH CORRECTION | The formula is right (K9, K13). The worked example (m_χ = 1 MeV, \|Δ_χ\| = 1 eV) has v*/v_max ≈ 1.8, so v/v* = O(1): the example lies outside the stated validity |
| V21 | §1.3 spectral budget 8.4% / YIG 5% | STANDS | 4·10 meV·m_e·(4 Å)² = 0.084, and 0.084·6·6.25·5/343 = 0.046 |
| V22 | §6 kinematics (Si:P 13.0 keV, 17 eV; NV 0.554 MeV, 734 eV); [6.2] | STANDS | Recomputed |
| V23 | §11 Contested corrections: none | n/a | Nothing to adjudicate |

## 1. OW4-2: the ε_bg² question, settled

### 1.1 1708.08929 (full text)
- Coupling: Eq. (2.1), L ⊃ −(ε/2)F_μνF′^{μν} + eJ_EM·A. The dark photon couples through J_EM, i.e. to **all** charges, including the
  remote bands. Item (i): total charge. CONFIRMED.
- κ convention: App. A.2 Eq. (A.8), ε_r(ω,q) = 1 − lim (1/V)(e²/(κq²))Σ g_s,n|f|²(f_FD − f_FD)/(E − E − ω − iη), summed over the
  **Dirac bands only** (n = −, n′ = +). So ε_r = 1 + δε_D/κ, i.e. ε_r = ε_total/κ. Eq. (2.6) has the same structure (prefactor e²g/(4π²κv_F)).
- Matrix element: Eq. (3.7), ⟨|M|²⟩ = 16m_e²m_χ²g_D²e²ε²/((q² − m_A′²)²|1 − Π_L/q²|²) = …/|ε_r|², using Eq. (2.4) Π_L = q²(1 − ε_r).
  Eq. (3.11): F_med = 1/ε_r, σ̄_e = 16πμ²ε²α_EMα_D/q₀⁴ with **vacuum** α_EM (Eq. (3.10) from the free M). Item (ii): vacuum. CONFIRMED.
- Plotted limits: Eqs. (3.13)–(3.14) build the rate from 1/|ε_r|². The prefactor 288π⁴κ²v_F²/(e⁴g²) is exactly
  ½·(24π²κv_F/(e²g))², i.e. |f|²·1/|ε_r|² with the "1" absorbed into Λ′. Fig. 4 is labelled "in-medium effects included". Item (iii):
  F_med = 1/ε_r is used for the limits. CONFIRMED.
- Derivation of the factor. The physical longitudinal ε is ε = κ + δε_D = κε_r, because the remote-band polarisation is part of Π_L for a
  field that couples to J_EM. The amplitude is ∝ g_Dεe/(q²ε), so ⟨|M|²⟩_true = ⟨|M|²⟩_free/|κε_r|². With the same bare |f|² (their
  Eq. (3.6), unit charge), Rate_1708/Rate_URF = |κε_r|²/|ε_r|² = κ² **exactly**, for any δε_D (not only |δε_D| ≪ κ). Equivalently
  Im δε_D/|ε_r|² = κ²·Im δε_D/|κ + δε_D|² = κ²·L_URF·(norm.).
- Internal inconsistency, in their own words. Footnote 5 fixes the charge at the cutoff to e₀² = e²(μ̃) = 4πα_EM/κ ("electrons behave as
  in an ordinary insulator"). At that matching point their F_med → 1, so their vertex is the vacuum e, not e₀. Text below (3.11): "the
  in-medium form factor ensures that the matrix element scales as e²(q) rather than e₀²". With e²(q) = e₀²/ε_r = e²/(κε_r), that
  sentence gives the URF result, 1/(κ²|ε_r|²) in |M|², not Eq. (3.7).
**Rating: CONFIRMED.** At κ = 40: ×1600. For the ZrTe₅ curve (κ̃ = 25.3): ×640.

### 1.2 1910.02091 (full text, v2)
- Eq. (2.5): F_med = j′D j/(j′D₀ j) ≃ D⁰⁰/D₀⁰⁰. Eq. (2.6): D⁻¹ = D₀⁻¹ − iΠ, with D₀ the **vacuum** propagator. Eq. (2.7):
  F_med = q²/(q² − Π⁰⁰).
- Eq. (3.3): Π^{μν} = −((−ie)²g/κ)∫Tr[…], the Dirac loop only, with 1/κ inserted ("we have not included κ in π(q̃²)", Eq. (3.5)). The
  background never enters D₀. Eq. (3.14): F_med = [1 + Σ_i q_i²v_{F,i}²π/(κ_ii q²)]⁻¹ = 1/ε_r (isotropic case).
- Eq. (2.3): σ̄_e = μ²|M₀(q₀)|²/(16πm_χ²m_e²), the free amplitude (vacuum). Coupling: dark photon, all charges (§2).
- Text below (3.8): "matching condition for the effective electron charge which is given by e/√κ at the cutoff". At the cutoff F_med → 1,
  so the vertex is e, not e/√κ: the same inconsistency as 1708.08929.
- Correct form: D⁰⁰⁻¹ ∝ q·κ·q − Π_D⁰⁰ (Π_D without 1/κ). Ratio |F_med,theirs|²/|F_med,URF|² = |κq² − Π_D|²/|q² − Π_D/κ|² = κ² (isotropic).
**Rating: CONFIRMED.**

### 1.3 Cross-check against 2101.08263 (shared authorship with 1708.08929)
2101.08263 (S.21) gives Im ε_Dirac = e²/(12πv_F) **without κ** (the total-ε Dirac part), and (S.22)/Eq. (4) W = Im ε/κ². This is the URF
form [5.1] (in the |δε_D| ≪ κ limit). So two papers by overlapping authors differ by κ² for the same model, and neither notes it.

### 1.4 Correction to §5.3 wording
"The ε_bg²-growth of 1708.08929 Eq. (3.14) (∝ κ²v_F²I) then reflects absorbing the '1' of ε_r into Λ′" is wrong as an explanation. The
κ² prefactor *is* the missing 1/κ². Absorbing the 1 (Λ′ = Λexp(12π²κv_Fe⁻²g⁻¹)) is identical in the correct theory, because
κ + Re δε_D = (e²g/24π²v_F)·ln(Λ′²…) with the same Λ′. So Rate_URF = Rate_1708/κ² exactly, with the same I(v_F, Λ′, m_χ). Replace the sentence
with: "the κ² of Eq. (3.14) is the omitted 1/ε_bg²; the κ-dependence through Λ′ is common to both." The "rank-one, Dirac-charge-only coupling"
interpretation is right: δn_D = R̃_Dφ_ext/(1 − v_CR̃_D/κ) gives Im(−R̃_D/ε_r) ∝ κ²Im δε_D/|κ + δε_D|². But that model is not a kinetically
mixed dark photon.
**Action:** WP4 §5.3 can drop "conditional". LIMITS L16 can record: "1708.08929 Eqs. (3.7), (3.11), (3.14) and 1910.02091 Eqs. (2.7), (3.14)
overstate the scattering rate by ε_bg² (exact) under the campaign σ̄_e convention; [R7 FT check]."

### 1.5 Referee finding (beyond the package): absorption is off by ε_bg
1708.08929 Eqs. (4.4)–(4.5) take ε²_eff = ε²m⁴/|m² − Π|² and R ∝ ε²_eff Im ε_r, with Π from ε_r (Eq. (2.4)). 1910.02091 Eqs. (2.25)–(2.26)
take |ε_med,x|² = ε²m⁴/|m² + Π₁₁|² and Γ_x = |ε_med|²Im Π₁₁/m, with Π₁₁ ∝ π/κ_xx. Correct: Π_total contains κ, so the rate is
∝ Im ε/|ε|² = κ⁻¹ Im ε_r/|ε_r|². Theirs ∝ Im ε_r/|ε_r|². **Their absorption rates are κ too large** (κ_ii per polarisation in 1910.02091).
The 1708.08929 Fig. 5 optimisation "optimal κ/g ~ O(10)" inherits this. [D by the referee; not propagated to their plotted curves.]

## 2. Superconductors (L15)

### 2.1 K2 and the coherence factor
The checks reproduce, per k at q = 0 (Matsubara Ω): Π₃₃ = 4Δ²/(E(4E² + Ω²)), Π₃₂ = −2ΔΩ/(E(…)), Π₂₂ − Π₂₂(0) = −Ω²/(E(…)). All three share
the k-dependence h(E) = 1/(E(4E² + Ω²)), so after Σ_k, R̃ = H[4Δ² − (r₃₂r₂₃)/r₂₂] = 0. Correct and standard (Anderson/Nambu 1958–60).
K3: (uv′ + vu′)² = ½(1 − (ξξ′ − Δ²)/(EE′)) → Δ²/E² at Q → 0, so the bare Π_QP(Q → 0, ω) ≠ 0 and ε_BCS acquires a spurious 1/Q². Correct.

### 2.2 Credit owed to 2609.06423
2609.06423 (§IV end, Fig. 3) adds "a further contribution Π_θ describing the phase exchange … parametrically suppressed with respect to Π_QP
by Δ²/(v_FQ)² ∼ (ξ₀⁻¹/Q)²", and states that the relative error "is at most 1/25" for ω > 5Δ. That is WP4's RG1 bound (v_max/2v_F)² = 0.04
(K16), already in the source. WP4 must cite it in §4.2 step 3 and remove "No DM calculation of … a conserving BCS dielectric function was
found" from §14. Neither work computes the vertex: RG1 stays open. Calling the bare bubble a "violation" is fair. Calling it a source error
is not: the authors identify the missing piece themselves.

### 2.3 𝔤_I closed form
Independent check: in the clean regime ω ≪ v_Fq, at fixed (E₁, E₂) all four sign pairs (ξ, ξ′) are reachable with equal weight (ξ′ − ξ =
v_Fq cosθ spans ±v_Fq ≫ ω). So ⟨ξξ′⟩ → 0 and the coherence factor is ½(1 + Δ²/E₁E₂). With N_s = E/√(E² − Δ²) the ratio to the normal state
is (1/ω)∫dE₁(E₁E₂ + Δ²)/√(…)√(…), which is [4.2]. Splitting off 2∫dy′/√(…) = 8K(k)/(y + 2) and using T = 0 Mattis–Bardeen for the
(E₁E₂ − Δ²) part gives (1 + 2/y)E(k) − 4K(k)/(y + 2). At y → 2⁺: k → 0, 2·π/2 − π/2 = π/2. At y → ∞: → 1. Correct. The statement
"Re ε^{BCS} = Re ε^{nor}[1 + O(Δ²/v_F²q²)]" is asserted, not derived: tag [D, sketch] or cite 2609.06423 (which shows it numerically).
"Q₊ < 1, where all DM kinematics lies" is false for q ≳ 2k_F(1 − v_max/v_F) ≈ 4.3 keV in Al (m_χ ≳ 3 MeV). There 𝔤_I ≈ 1 anyway, so it is
harmless but should be stated.

### 2.4 Misattribution (V7)
2609.06423 Fig. 2 plots |ε_BCS|²/|ε_Lin|². Their Eq. (10) (the QROCODILE-style approximation) "retains the BCS coherence factor"
in Im ε_BCS and replaces only the screening. Their "Lindhard accurate above 5Δ" therefore concerns Re-dominated screening (error Δ²/(v_FQ)²),
not the Im ε ratio 𝔤_I. 𝔤_I(5) = 1.15 is a 15% effect that appears in **both** of their Eqs. (9) and (10). WP4's sentence must be replaced
by: "𝔤_I is the ratio Im ε^{BCS}/Im ε^{nor}. It is contained in 2609.06423's Eqs. (9)–(10) and is distinct from their 5Δ screening
statement. Rate_BCS/rate_Lindhard = 𝔤_I applies when the Lindhard rate uses Im ε^{nor}, e.g. 2101.08263."

### 2.5 η_pb (V8)
Δ⟨N_qp⟩ ≤ ω, because each QP carries ≥ Δ, so η_pb ≤ 1, and η_pb(2Δ⁺) = 1. Correct, and consistent with WP5 (W13). The bound: a third QP
needs one QP to emit a phonon of energy ≥ 2Δ while it keeps ≥ Δ, i.e. E₁ ≥ 3Δ. Since E₁ ≤ ω − Δ, this needs ω ≥ 4Δ. So N_qp = 2 and
η_pb = 2Δ/ω for all ω < 4Δ_BCS. "ω < 3Δ_BCS" is true but too weak; correct it in [4.6] and in the K15 note.

### 2.6 Source items
- K1, 2101.08263 Eq. (3): printed λ_TF²/(2q²). Their (S.13) prefactor 3ω_p²/(q²v_F²) times a bracket → 1, and (S.14) λ_TF = √3ω_p/v_F, give
  λ_TF²/q². Their own (S.15) agrees. **CONFIRMED.** The Im term 3πω_p²ω/(2q³v_F³) is right. W from Eq. (3) is 4× too large.
- K7, 1512.04533 (3.3) (= Eq. (13) in the journal version): e₋ = (E_D − |q|²/2m_e)²/(|q|²/2m_e). From p∥_min = m(ω − E_q)/q:
  e₋ = (ω − E_q)²/(4E_q). **CONFIRMED.** It affects only T > 0 and the edges, not (3.4).
- 2609.06423 Eqs. (4), (7): S_p = diag(1/(ω − E + i0), 1/(ω + E − i0)) and the bubble with −i0 on the negative pole are time-ordered.
  **CONFIRMED.** They are used only at T = 0 and ω > 0, where Im Π^T = Im Π^R, and the paper writes "reduces to the Lindhard function
  for ω > 0". **Defect: REFUTED.** Move it from "Source defects" to a remark: "time-ordered; do not use for ω < 0, KK or T > 0".
- 2101.08263 SM: "Causality also implies W(q,−ω) = −W(q,ω)". **CONFIRMED** that they say this. The correct origin is reality of the
  density kernel (R(q,−ω) = R(−q,ω)*) plus inversion or T (isotropy). WP4's "causality alone gives …" must read "reality alone gives …".

## 3. Films and disorder (V13, V14)
Diffusive: ε ≈ 1 + k_TF²D/(Dq² − iω). For k_TF² ≫ q², ω/D, Im(−1/ε) = ω/(k_TF²D) for any ω/Dq², with D = v_Fℓ/3. Drude for ω ≪ γ:
ε ≈ 1 − ω_p²/γ² + iω_p²/(ωγ), so L = ωγ/ω_p², and k_TF²D = (3ω_p²/v_F²)(v_F²/3γ) = ω_p²/γ. Equal. Ballistic: L = (πω/2qv_F)(q²/k_TF²),
ratio πqℓ/6. Inside Mermin at qv_F ≫ γ ≫ ω: with δ = −πγ/(2qv_F) + iπω/(2qv_F) and a = iγ/(ω + iγ), (ε_Mer − 1)/(ε_L(0) − 1) =
(1 + δ)/(1 + aδ) ≈ 1 − iωδ/γ, whose Im part is πω/(2qv_F) (Lindhard), up to O((qℓ)⁻²). [4.4] STANDS.
**V14 FALLS.** 2412.16279 SM §I: "We approximate ε(q,ω) by the Lindhard dielectric function ε_L(q,ω) … plasmon width Γ = 0.1E_F". The Drude
function is used only "in the case of thin layers", to solve Maxwell's equations for the q-direction dependence (their Fig. S1, modulation).
So (a) their bulk limit is already on the ballistic (Lindhard) branch, and "×1–10, conservative for their limit" does not apply. (b) Their
ω + iΓ Lindhard is the non-conserving prescription WP4 itself criticises in §4.4; that is the relevant comment. (c) Amorphous WSi with
ℓ_mfp ≈ 0.3–1 nm has k_Fℓ ~ 1 (Ioffe–Regel). q = 1–5 keV is comparable with k_F ≈ 2.7 keV and not ≪ k_TF. The RTA–Mermin model has no
control there, so any WSi factor is at most [E, outside validity]. Also, G9's source was tagged [ABS]: the claim about a published paper
was made without reading it.

## 4. Chiral and nonreciprocal (V15, V16)
Contraction by hand: 𝒱_δ = N[−(ic₅/m_e)ε_{abδ}S^aq^b − c₈S^δ], N = 1/(4m_χm_e), and 𝔇_δε = ½tr(𝒱_δ†𝒱_ε). The cross terms give
𝔇_δε ⊃ (iN²/2m_e)Re(c₅*c₈)ε_{δbε}q^b, so 𝔇^A_δε = −(N²/2m_e)Re(c₅*c₈)ε_{δεb}q^b. With S^A_δε = ε_{δεc}q^cγ_OA,
−Σ𝔇^AS^A = (N²/2m_e)Re(c₅*c₈)γ_OA·2q² = q²Re(c₅*c₈)γ_OA/(m_e(4m_χm_e)²). Γ^R − Γ^L doubles this because γ^L = −γ^R. This matches K12
and [3.3]. The ordering 𝔇_ab = ⟨𝒱_a*𝒱_b⟩ against S_ab = ⟨O_a†…O_b⟩ is that of WP0-v2 (3.1)/(3.3). The v1 factor −½ is corrected.
Parities: 𝒪₅ = iS_χ·(q × v⊥)/m_e is P-even and T-even, 𝒪₈ = S_χ·v⊥ is P-odd and T-even. The interference is P-odd and T-even, matching
γ_OA. So the "P-violating DM" conclusion stands. The overall sign of [3.3] is tied to the sign convention of γ_OA (S = S^S + iS^A); WP4
should state that γ_OA > 0 is defined by this decomposition, not by an optical convention.

## 5. Theorem D-g (V17)
WP0-v2 §6.2 (i) gets "restriction by orthogonal projectors summing to 1" because U_n block-diagonalises H to O(κ_BO^{n+1}). Final
eigenstates |f⟩ then lie in one sector up to that error. In D-g, U_qp is required only to "map bare fermions and phonons onto QPs", with
on-shell width Γ_qp > 0 (G1). Then [H, U_qpN̂U_qp†] ≠ 0. Write S_ab(ω) = ⟨i|O_a†δ(ω − H + E_i)O_b|i⟩ = Σ_{n,n′}⟨i|O_a†𝒬_nδ(ω − H)𝒬_{n′}O_b|i⟩.
The diagonal terms are PSD, but the n ≠ n′ terms are nonzero at resolution finer than Γ_qp + Γ_ph. So "complete, no double counting" fails
unless one adds (G5): ‖𝒬_{n}H𝒬_{n′}‖ ≤ ε_D for n ≠ n′, with an error O(ε_D/bin) in (6.1)-type sums. (G5) is the content of the [C] bin
condition (c). So (a) is [D] only conditional on a [C] hypothesis. Retag (a) as "[D given U_qp **and (G5)**]" and state the error term.
(b) is fine as [C]. Note that the phase and Higgs modes are pair (n = 2) composites, so assigning them to (0,0) is a convention, not a
consequence. (d) is fine.

## 6. Smaller numerical points
- V4: ∫₀¹x(1−x)ln[1/(x(1−x))]dx = 5/18. With Eq. (2.6)'s scale μ̃ = 2v_FΛ, Re δε_D/ε_bg = (α̃/6π)[ln((2v_FΛ_D)²/𝓈) + 5/3] = 0.349 at
  √𝓈 = 10 meV, rate factor 0.55. K17 (0.268, 0.62) uses the e^{−5/6}-redefined Λ of Eq. (2.7). Since Λ_D = 0.2 keV is quoted from the same
  paper, state which convention is used, and quote 0.55–0.62 as the cutoff-scheme spread.
- V19: 0.13 keV → 0.13 eV in §4.3 (the conclusion q ≪ k_F holds a fortiori).
- V20: v* = √(2|Δ_χ|/m_χ) = 1.41×10⁻³ against v_max = 2.65×10⁻³ for the example. Choose |Δ_χ| ≳ 10 eV at 1 MeV, or say "O(1) Doppler
  corrections".
- V3: (ε_xx/ε_yy)² = 366 (1708.08929 clamped-ion), or 221 with 1910.02091's DFT values (308.4, 20.75). The q ∥ y rate is the larger one.

## 7. Rubric summary
(a) DERIVED steps: mostly sound. Exceptions: the Re ε^{BCS} statement (sketch) and D-g (a) (hidden hypothesis). (b) LIMITS L13, L15, L16:
source formulas are quoted correctly (spot-checked 1708 (2.6), (3.7), (3.11), (3.14); 1910 (2.5)–(2.7), (3.13)–(3.14); 2609 (6)–(9);
2101 (3), (4), (S.13)–(S.16), (S.34); 1512 (3.2)–(3.4); 2009 (36), (38)). The chains are valid. Validity numbers need V19 and V20.
(c) Paper-is-wrong claims: 1708.08929 κ² CONFIRMED; 1910.02091 κ² CONFIRMED; 1910 (3.14) typo CONFIRMED; 2101 Eq. (3) CONFIRMED;
1512 e₋ CONFIRMED; 2609 time-ordered fact CONFIRMED but defect REFUTED; 2101 "causality" CONFIRMED (with WP4's own fix also
misattributed); 2009 Eq. (36) CONFIRMED (notational); QROCODILE "Drude for the limit" REFUTED. (d) CONVENTIONS/NOTATION: consistent;
σ̄_e in vacuum (CONVENTIONS §9) is what makes V1 decisive. (e) Gap closures (two-magnon, magnon–phonon, NV, films) are formula plus
specification, not restatements; G9 needs V14. (f) No contested corrections. (g) All focus items covered above.
