# R7 referee report REF-WP4-B (hostile, isolated) on returns/R6/WP4-v2.md

Read: WP4-v2.md, code/WP4-v2/checks.py (run: 23/23 PASS, < 5 s), CONVENTIONS, NOTATION (grep), CONTROLS, DONE, LIMITS, WP0-v2 (§2,
§6.2). Full texts fetched with lit.py into literature/papers-r7-WP4-B/ and deleted afterwards: 1708.08929, 1910.02091, 2101.08263,
1512.04533, 2609.06423, 2412.16279 (QROCODILE), 1905.13744. No numerical simulation was run.

## Verdict table
| # | Claim (WP4-v2 location) | Verdict | One-line reason |
|---|---|---|---|
| V1 | OW4-2: 1708.08929 and 1910.02091 omit the background factor 1/ε_bg² for the dark photon (§5.3) | **STANDS: CONFIRMED for both papers**; the statement should be upgraded from conditional to a claim | Both define ε_r = ε_tot/κ (1708.08929 Eq. (A.8); 1910.02091 Eq. (3.3) puts e²/κ in the loop), use F_med = 1/ε_r and keep σ̄_e in vacuum, so the rate is exactly κ² times the URF rate. Their absorption rates are also too large, by κ (§A4) |
| V2 | L16 chain [5.1]; 2101.08263 Eq. (4) recovered exactly (§5.2) | STANDS | Checked against 2101.08263 Eqs. (4), (S.21), (S.22): W = Im δε_D/κ² |
| V3 | Anisotropic background enters as q̂·ε_bg·q̂ [5.2]; 1910.02091 Eq. (3.14) has a typo | STANDS WITH CORRECTION | Correct. The same typo (q_x²v_{F,z}²) is already in the 00 entry of Eq. (3.13), not only in (3.14) |
| V4 | L15 chain; K2 (the GRPA response vanishes at q = 0); the bare bubble violates conservation (§4.2) | STANDS | K2 re-derived; the coherence factor tends to Δ²/E² at Q → 0, so the bare Π_QP(0,ω) ≠ 0 |
| V5 | Closed form 𝔤_I [4.2] and L^{BCS} = 𝔤_I L^{nor} in the DM region (§4.3) | STANDS WITH CORRECTION | The math is right (case-I creation factor, K4, 𝔤_I(2⁺) = π/2). The reading "the analytic form of 2609.06423's agreement for ω ≳ 5Δ" is **wrong**: their agreement is for \|ε_BCS\|²/\|ε_Lin\|², and their Eq. (10) keeps Im ε_BCS |
| V6 | Validity numbers for Al (§4.3) | STANDS WITH CORRECTION | "q ≥ 2Δ_BCS/v_max ≈ 0.13 keV" should read **0.13 eV** (a units error). qξ_coh ≥ 1.6 and the bound 0.04 are right |
| V7 | 2101.08263 Eq. (3): Re ε is k_TF²/q², not k_TF²/2q²; a factor 4 in L (K1) | STANDS: CONFIRMED | Their own (S.13)–(S.15) with λ_TF = √3ω_p/v_F (S.14) give λ_TF²/q² |
| V8 | 1512.04533 Eq. (13) [PDF (3.3)]: e₋ lacks a factor 4 (K7) | STANDS: CONFIRMED | e₋ = p_min²/2m = (E_D − E_q)²/(4E_q); the paper prints (E_D − q²/2m)²/(q²/2m) |
| V9 | 2609.06423 Eqs. (4) and (7) are time-ordered, not retarded | STANDS WITH CORRECTION: CONFIRMED for Eqs. (7)–(8), REFUTED as a defect of Eq. (4) | Eq. (4) is the T = 0 Feynman propagator and is legitimate. The defect is only that the time-ordered Π (−i0⁺ on the second pole) is used as the retarded ε |
| V10 | 2101.08263 attributes W(q,−ω) = −W(q,ω) to causality (§4.3(d)) | STANDS WITH CORRECTION | The attribution is confirmed (their line "Causality also implies…"). The package's own phrase "causality alone gives ε(q,−ω) = ε(−q,ω)*" is also wrong: that identity follows from **reality** of the time-domain kernel, not from causality |
| V11 | §4.4: the acausal branch is "off by up to 10⁷ because it puts negative-frequency weight at ω > 0" | STANDS WITH CORRECTION | The size and direction are confirmed: 2101.08263 SM says the acausal choice **suppresses** the rate by up to 10⁷. The stated mechanism is asserted, not derived, and should be tagged [E] or removed |
| V12 | Mermin [4.3]–[4.4]: L_Mer/L_Drude → πqℓ_mfp/6; QROCODILE's Drude ε underestimates L (§4.5) | STANDS WITH CORRECTION (algebra); **the QROCODILE claim is REFUTED** | QROCODILE's bulk rate and limits use Lindhard with ω + iΓ (Γ = 0.1E_F); Drude enters only their thin-layer anisotropy (SM Fig. S1). The WSi momenta q = 1–5 keV are not ≪ k_F ≈ 2.7 keV or k_TF ≈ 3.6 keV, so the asymptotic ratio does not apply at the upper end |
| V13 | Reciprocity theorem [3.1] | STANDS | The relabelling and the T/P argument are correct (antiunitary T included) |
| V14 | Magnetochiral expansion [3.2], S(q) − S(−q) = 2q·𝐛_NR + O(q³) | STANDS WITH CORRECTION | For the **density** channel the odd part starts at O(q³), not O(q): continuity gives S_nn = q_αq_βS_{j^αj^β}/ω², and S_nn(q → 0, ω ≠ 0) = 0 |
| V15 | Chiral selection rule [3.3] and the −½ fix (K12) | STANDS | Independently checked: only 𝒪₅×𝒪₈ survives; the 𝒪₅×𝒪₅, 𝒪₈×𝒪₈ and n-row cross terms vanish; the coefficient +2∫(q²/m_e)Re(c₅*c₈)γ^R_OA/(4m_χm_e)² is correct |
| V16 | η_pb = Δ_BCS⟨N_qp⟩/ω with N_qp counting quasiparticles; η_pb(2Δ⁺) = 1 (§4.6) | STANDS (minor sharpening) | The definition and the removal of the factor 2 are correct. N_qp = 2 holds for all ω < **4Δ_BCS** (the larger QP has E ≤ ω − Δ, and pair breaking needs E ≥ 3Δ), not only for ω < 3Δ |
| V17 | Theorem D-g (a): "[D given U_qp]", Hermitian PSD, complete, no double counting (§8) | STANDS WITH CORRECTION | Completeness needs [H, U_qpN̂U_qp†] = 0 up to a stated error, as WP0-v2 (6.1) carries O(κ_BO^{n+1}). This is incompatible with Γ_qp > 0 in (G1). As written, (a) is [D] only with an error term O(Γ_qp/bin), which merges it into (c) [C] |
| V18 | L13 magnon chain [2.1]–[2.2]; n_s = \|𝐒\|/Ω (K6) | STANDS | Consistent with 1905.13744 App. Eqs. (A.10)–(A.13) (n_s = total spin density of the effective FM) |
| V19 | Two-magnon [2.3]–[2.4]; magnon–phonon [2.5]; exothermic [7.1]–[7.2]; dopants [6.1]–[6.3]; budget §1.3 | STANDS | Algebra checked (K9, K13, K10, K14); tags appropriate; specifications are sufficient as gap closures (e) |
| V20 | Vertex-correction size O((Δ_BCS/v_Fq)²) ≤ 0.04 for Al as the package's own estimate (K16, RG1) | STANDS WITH CORRECTION (attribution) | 2609.06423 §IV already states the phase-mode suppression Δ²/(v_FQ)² ≤ 1/25 for ω ≥ 5Δ (Fig. 3). Cite it |

---
## A. TOP PRIORITY: OW4-2, the background factor (V1) [settled]

**A1. 1708.08929 (full text).** (i) *Coupling.* Eq. (2.1) is kinetic mixing of A′ with F_{μν}, coupled to eJ^μ_EM: the **total** EM
current, remote bands included. Eq. (2.2) gives the in-medium coupling εe q²/(q² − Π_L). (ii) *σ̄_e.* Eqs. (3.8), (3.10) and (3.11) give
σ̄_e = 16πμ²ε²α_EMα_D/q₀⁴ with the bare e²: **vacuum**. (iii) *F_med.* Eqs. (3.7) and (3.11) give ⟨|M|²⟩ = 16m_e²m_χ²g_D²e²ε²/((q² − m²)²|ε_r|²)
and F_med = 1/ε_r. The κ convention is fixed by Eq. (A.8):
  ε_r(ω,q) = 1 − (1/V)(e²/(κq²))∫Σ g_s|f|²(f_FD′ − f_FD)/(E′ − E − ω − iη),
so ε_r = 1 + δε_D/κ = ε_tot/κ, with δε_D the bare (e²) Dirac polarisation. Eq. (2.6) has the same e²g/(κv_F) prefactors. The paper's own
footnote 5 sets the charge at the cutoff to e₀² = e²/κ. That is the physical screening by remote bands, yet (3.7) carries e², not e₀².
(iv) *Plotted limits.* Eqs. (3.13)–(3.14) (R_tot ∝ κ²v_F²I) and Fig. 4 (κ = 40) are computed with F_med = 1/ε_r.
*Rate ratio [D].* Golden rule with (3.5)–(3.6): Σ_f|f|²δ(ω − ω_f) = (κq²/(πe²))Im ε_r = (q²/(πe²))Im ε_tot, by (A.8). So
  R_1708 ∝ |Ṽ|²(q²/e²)Im ε_tot/|ε_r|² = κ²·|Ṽ|²(q²/e²)Im ε_tot/|ε_tot|² = κ²·R_URF   (URF: S = (2q²/e²)Im[−1/ε_tot], WP0-v2 (5.3)/(5.4)).
The factor is exactly κ² = 1600 at κ = 40, for any q and ω. The package's reading of the "κ² growth" of (3.14) is also right.
Λ′ = Λ exp(12π²κv_F/(ge²)) makes ln²(4Λ′²/…) ∝ κ² at large κ, so R_1708 → Im δε_D·const is κ-independent and R_URF ∝ 1/κ².
**Verdict: CONFIRMED.** The rate corresponds to a DM coupled only to Dirac-band charge. Check: R_DD = R̃_D/(1 − v_CR̃_D/κ) = κR̃_D/ε_tot
gives Im(R̃_D/ε_r) = Im R̃_D/|ε_r|², since Im(R̃_D·R̃_D*) = 0. This is the package's §5.3 reading, verified.

**A2. 1910.02091 (full text, v2).** (i) Dark photon, F_med = M/M₀ = D^{00}/D₀^{00} (Eq. (2.5)) with D⁻¹ = D₀⁻¹ − iΠ (Eq. (2.6)). (ii) σ̄_e is
vacuum (Eqs. (2.3)–(2.4), q₀ = αm_e). (iii) Eq. (3.3) is Π^μ_ν = −((−ie)²/κ)(g/2)∫Tr…, so Π contains only the Dirac loop with e²/κ.
D₀ = 1/q² carries **no** background, and the electron vertex carries bare e. Hence F_med = q²/(q² − Π^{00}) = 1/(1 + δε_D/κ) = 1/ε_r
(Eqs. (2.7), (3.14)). The physical propagator is D^{00} = 1/(κq² − Π^{00}_bare), so F_true = (1/κ)(1/ε_r). Their own text on Eq. (3.9)
quotes the effective charge e/√κ at the cutoff, which again is not applied to the external vertex. **Verdict: CONFIRMED**, the same κ² as
1708.08929. For anisotropic κ, Eq. (3.14) is not κ_eff·F_true for any κ_eff, because F_true = q²/(q·κ·q + Σq_i²v_i²π): this confirms
[5.2]. Typo: the 00 entry of Eq. (3.13) already reads −q_x²v_{F,z}²/κ_xx (HTML LaTeX source checked), so the typo propagates into (3.14).

**A3. Consequence (owed).** Under CONVENTIONS §9 (σ̄_e in vacuum, screening only in S), both papers' dark-photon scattering reach is
optimistic by κ² in rate: 1600 for the 1708.08929 benchmark, and per-direction (q̂·κ·q̂)² for ZrTe₅ in 1910.02091. §5.3 should drop
"conditional" and state this as a claim [D + FT]. Item (i) is total charge, (ii) vacuum, (iii) the plotted limits use 1/ε_r: all three
check items close. 2101.08263 Eq. (4) (W ∝ 1/κ²) agrees with the URF and contradicts the two earlier papers. That is an independent
literature cross-check the package should cite.

**A4. Extension found by the referee (not claimed by WP4).** For absorption, 1708.08929 Eqs. (4.4)–(4.5) give
R ∝ ε²_eff Im ε_r with ε²_eff = ε²/|ε_r|² (Π = ω²(1 − ε_r)). The URF gives ε²ω Im[−1/ε_tot] = ε²ω Im ε_r/(κ|ε_r|²), so their absorption
rate is κ × URF. 1910.02091 Eqs. (2.25)–(2.27) (Π_ii ∝ 1/κ_ii, D₀ without background) give the same factor κ_ii per polarisation. WP4
should add this to §5.3 as a [D] statement, or flag it to the WP owning L9b.

## B. BCS items (V4–V9, V16, V20)

**B1. K2 and the bare bubble.** I re-derived the q = 0 Nambu bubbles per k in Matsubara form. Π₃₃ = 4Δ²/(E(4E² + Ω²)),
Π₃₂ = −Π₂₃ = −2ΔΩ/(E(⋯)), and Π₂₂ − Π₂₂(0) = −Ω²/(E(⋯)) all share the k-dependence h = 1/(E(4E² + Ω²)). Then
Π₃₃ − Π₃₂Π₂₃/(Π₂₂ − Π₂₂(0)) ∝ Σh·[4Δ² − 4Δ²Ω²/Ω²] = 0, for every Ω and hence every ω after continuation. Correct, and standard (Anderson).
2609.06423 Eq. (7) has coherence factor 1 − (εε′ − Δ²)/(EE′) → 2Δ²/E² at Q → 0, so (4πα/Q²)Π_QP ∝ 1/Q²: spurious. Their Fig. 2 region
ω > v_FQ (Im ε_Lin = 0 but Im ε_BCS ≠ 0) is this artefact, as WP4 says. The paper itself flags the phase mode Π_θ (§IV, Fig. 3) with
suppression Δ²/(v_FQ)² ≤ 1/25. WP4's RG1 estimate is therefore not new (V20).

**B2. 𝔤_I [4.2].** I derived it independently. For ω < qv_F − q²/2m_e the angular average makes ∫dξdξ′ uniform, the ξξ′ term averages to
zero over the four sign combinations, and the creation coherence factor (uv′ + vu′)² = ½(1 − (ξξ′ − Δ²)/EE′) → ½(1 + Δ²/EE′) (case I).
Then Im ε^{BCS}/Im ε^{nor} = (1/ω)∫_Δ^{ω−Δ}dE(EE′ + Δ²)/(√(E² − Δ²)√(E′² − Δ²)), E′ = ω − E, which is [4.2]. Near y = 2 the integral is
(1/2)(2/2)∫dx/√((x − a)(b − x)) = π/2: a finite step, as stated. K4 agrees to 10⁻¹² at six points. **But:** 2609.06423's "good agreement for
ω ≳ 5Δ" is about |ε_BCS|²/|ε_Lin|² (their Fig. 2 and its caption: "ratio of squared dielectric functions"). In WP4's own [4.2] this is
the statement Re ε^{BCS} = Re ε^{nor}(1 + O(Δ²/v_F²q²)), not 𝔤_I. Their Eq. (10) explicitly *keeps* Im ε_BCS and replaces only |ε|².
Replace "the analytic form of 2609.06423's 'agreement for ω ≳ 5Δ' (15% at 5Δ_BCS)" with: "𝔤_I is the production-rate ratio. 2609.06423's
|ε|² agreement is the Re ε statement of [4.2]; their Eq. (10) already carries 𝔤_I implicitly." The closed form being new is not checked
here (no priority search).

**B3. Units error (V6).** q_min = 2Δ_BCS/v_max = 3.4×10⁻⁴ eV / 2.65×10⁻³ = 0.128 **eV**. With ξ_coh = v_F/(πΔ_BCS) = 12.7 eV⁻¹ this gives
qξ_coh = 1.63, which agrees with K16 only for eV. The text "≈ 0.13 keV" is wrong by 10³. The conclusions (q ≪ k_F; q ≲ 1/ξ_coh
unreachable) are unaffected.

**B4. Source defects.** (V7) 2101.08263 Eq. (3) prints λ_TF²/2q². (S.13) has prefactor 3ω_p²/(q²v_F²) = λ_TF²/q² by (S.14), and the
bracket → 1 for ω ≪ qv_F, q ≪ k_F (K1/K1b, re-run). So Re ε ≈ 1 + λ_TF²/q², and L ≈ Im ε/(Re ε)² is off by 4 in their Eq. (3) scaling.
CONFIRMED. (V8) 1512.04533 (3.3): e₋ is the minimum initial-electron kinetic energy. p_∥ = m_eE_D/q − q/2, so e₋ = (E_D − E_q)²/(4E_q),
which agrees with 2101.08263 (S.34). CONFIRMED. This affects ξ at T > 0 and the validity statement "e₋ < μ", not (3.4). (V9) 2609.06423
Eqs. (7)–(8): the second pole −1/(ω + E + E′ − i0⁺) sits at ω = −(E + E′) + i0, in the upper half-plane, so Π is time-ordered. A retarded Π
needs +i0⁺. CONFIRMED. For ω > 0 at T = 0, Im Π_T = Im Π_R, so their numbers are unaffected, as WP4 says. Eq. (4) is S_p(ω), the T = 0
Feynman propagator in the QP basis. It is the correct object inside a T = 0 diagram and should be removed from the defect list. (V10)
ε(q,−ω*) = ε(−q,ω)* follows from the real-valued time-domain kernel (Hermitian density), and causality gives only analyticity in
Im ω > 0. WP4's physics conclusion stands (W odd in ω needs q ↔ −q symmetry: P or T).

**B5. η_pb (V16).** η_pb ≡ Δ_BCS⟨N_qp⟩/ω with N_qp = number of QPs is the standard definition (energy stored at the gap edge). It gives
η_pb ≤ 1 and η_pb(2Δ⁺) = 1. The v1 factor 2 was a pair/QP double count. Correct. Sharpening: a QP of energy E emits phonons of energy
≤ E − Δ, and pair breaking needs ≥ 2Δ, so E ≥ 3Δ is required. In a prompt pair max E₁ = ω − Δ, so N_qp = 2 exactly for ω < 4Δ,
η_pb = 2Δ/ω there. [4.6] normalisation (K15) checked.

## C. Mermin/Drude (V12)
Algebra [D]. In the diffusive limit (qℓ ≪ 1, ω ≪ γ_rel) ε → 1 + k_TF²D/(Dq² − iω), L = ω/(k_TF²D)[1 + O(q²/k_TF², ω/k_TF²D)] for any
ω/Dq² (K11). In the ballistic limit Mermin gives ε − 1 = (k_TF²/q²)(1 + iπ(ω + iγ)/(2qv_F))/(1 − πγ/(2qv_F)); I derived this,
corrections are O(1/qℓ), and L → πωq/(2k_TF²v_F). The ratio πqℓ/6 follows. K11's ratio test is tautological: it checks only the algebra
of the quoted asymptotes, not the reduction of [4.3] to them.
**QROCODILE (2412.16279, full text; WP4 cites [ABS] "via catalog").** SM §I: "We approximate ε(q,ω) by the Lindhard dielectric function
ε_L … plasmon … width Γ = 0.1 × E_F" for the bulk rate, which sets the limits. Drude is used only for the thin-layer Maxwell solution,
"as is appropriate for small momentum transfers", to estimate directional anisotropy (Fig. S1). WP4's sentence "QROCODILE's Drude ε for
WSi … underestimates L by πqℓ_mfp/6 … conservative for their limit" is therefore **REFUTED**. The relevant defect of their bulk ε is
§4.4's: ω + iΓ Lindhard is not conserving. Mermin is the fix, and with Γ = 0.7 eV (ℓ = v_F/Γ ≈ 1.5 nm) qℓ ≈ 7–40 at q = 1–5 keV. Also,
for E_F = 7 eV, k_F = 2.67 keV and k_TF = (4αm_ek_F/π)^{1/2} ≈ 3.6 keV. The window q = 1–5 keV violates q ≪ k_F and q ≪ k_TF used in [4.4].
At qℓ = 1.5 the asymptotic ratio is 0.79 < 1, so "×1–10" is not supported at the low end either. Restate [4.4] for q ≪ k_F, and drop or
re-derive the WSi numbers with the full Mermin–Lindhard form.

## D. Chiral and nonreciprocal (V13–V15)
[3.1] is correct: relabel q → −q, |Ṽ(q)| = |Ṽ(−q)|, and antiunitary T gives |⟨Θf|n_{−q}|Θi⟩| = |⟨f|n_q|i⟩|. **[3.2] order:** the density
response obeys S_nn(q,ω) = q_αq_βS_{j^αj^β}(q,ω)/ω² (continuity, WP0-v2 (4.8)/CONVENTIONS §6), and S_nn(0,ω ≠ 0) = 0. A term linear in q
in S_jj (the magnetochiral/gyrotropic response) therefore enters S_nn at O(q³): S_nn(q) − S_nn(−q) = 2q_αq_βq_γb_{αβγ}(ω)/ω² + O(q⁵). The
"q-linear" form [3.2] holds for current/spin channels, not for the density coupling assumed in [3.1]. **[3.3]:** with WP0-v2 (2.2)
matching, 𝒪₅ → j-row −iε_{αγδ}𝐒^αq^γ/m_e and 𝒪₈ → −𝐒^δ. The other antisymmetric contributions vanish: 𝒪₈×𝒪₈ (δ_{δε}/4), 𝒪₅×𝒪₅
(q²δ − qq, symmetric), and the n-row cross terms (ε_{βγδ}v^βq^γv^δ = 0 and ε_{βγδ}v^βq^γq^δ = 0 against the only isotropic vector q).
Σ𝔇_abS_ab ⊃ −Σ𝔇^AS^A is correct for Hermitian S = S^S + iS^A. K12 (re-run) gives +q²Re(c₅*c₈)γ_OA/(m_e(4m_χm_e)²), and γ^L = −γ^R doubles
it: [3.3] is right, and the v1 "−½" was wrong. P-parities: 𝒪₈ P-odd, 𝒪₅ P-even, both T-even. Correct.

## E. Theorem D-g (V17)
Inserting 1 = Σ𝒬_{n,m} on the final side of (3.1) gives |Σ_n⟨f|𝒬_nO|i⟩|², which equals Σ_n|⟨f|𝒬_nO|i⟩|² only if every H-eigenstate f lies in
one sector, i.e. [H, 𝒬_{n,m}] = 0. WP0-v2 (6.1) handles the analogous issue with U_n block-diagonalising H to O(κ_BO^{n+1}) and carries
that error. D-g (a) states neither the condition nor an error term. With (G1)'s on-shell width Γ_qp > 0, QP number is not conserved and the
cross terms are O(Γ_qp/bin width). So "complete, no double counting [D given U_qp]" holds only if U_qp is *defined* to make N̂_qp, N̂_ph
conserved, which contradicts (G1). Fix: (a) [D] → "S = Σ S^{(n,m)} + C_cross, |C_cross| = O(Γ_qp + Γ_ph)/Δω_bin [E]", with exact
completeness only in the conserved-number limit. (b)–(e) [C] stand as conjectures. n ∈ {0, 2} for bilinears on a T = 0 BCS reference is
correct (only γ†γ† acts on |BCS⟩).

## F. Other checks
- L13: the 6-step chain and [2.2]'s absorption term (−k, ω_{−k,ν}) are correct. 1905.13744 (A.10)–(A.13) show n_s is the total spin
  density of the n = 1 effective FM, so K6's identification n_s = |𝐒|/Ω is consistent. The quotes of Eqs. (5) and (6) match the HTML
  source. 2009.13534 was not re-fetched; its §2.1 "S′^x/S′^y labels are S′^±" was not checked (low impact, notational).
- The Dirac quotes [5.1] (1708.08929 Eqs. (2.6), (3.7), (3.11)), the κ table (187.5, 9.8, 90.9; ion-clamped DFPT, confirmed) and the
  harmonic mean 25.3 are all correct. K17 numbers re-run: α̃ = 0.912, Re δε_D/ε_bg = 0.268.
- 1512.04533 (3.2): z/(1 − e^{−z})·(1 + ξ/z)T = E_D(1 + ξ/z)/(1 − e^{−βE_D}). The free-gas Im ε ∝ T(z + ξ), so the factorisation as
  (1 − e^{−βω})^{-1} × proper part is exact, as stated.
- 2609.06423 Eq. (8) normalisation: with 1 − (εε′ − Δ²)/EE′ = 2(uv′ + vu′)² and the p ↔ −p−Q double count, Δ → 0 reproduces spin-summed
  Lindhard. Their Eq. (9) prefactor agrees with K8.
- (d) Consistency: [4.1], [5.1] and the rate normalisations follow CONVENTIONS §6–§9. The sign of q is the campaign's ([3.1]). Spin trace
  δ/4 in [3.3] is correct. NOTATION v4 symbols are used as listed (spot checks: 𝔤_I, η_pb, N_qp, ξ_coh, 𝐛_NR, γ_OA, ℓ_mfp, k_TF). No
  WP0-v2 interface mismatch found. The F5 hand-over is conditional on the V17 fix.
- (e) Gap closures: [2.4], [2.5], [4.2]+[4.6], [6.1]–[6.3] and [7.2] are formula plus algorithm, cost and convergence criterion:
  sufficient. Theorem D-g is a restatement of the OW0-9 gap with structure, correctly tagged [C] except for (a).
- (f) "Contested corrections: None": nothing to adjudicate.
- DONE rung-4 rubric: no screening double count (Dirac: ε_bg once, in ε). Bose factors in [2.2] are correct. The q-sign is respected.
  The dipole limit is not misused. The kinematic numbers K18 (v_max = 794.5 km/s) were re-run.

## G. Required edits (summary)
1. §5.3/§0/OW4-2: replace the conditional with the confirmed claim (A1–A3). Add the absorption factor κ (A4). Note the typo in 1910.02091 (3.13).
2. §4.3: correct 0.13 keV to 0.13 eV. Rewrite the "agreement for ω ≳ 5Δ" sentence (B2). Credit 2609.06423 for Δ²/(v_FQ)² ≤ 1/25.
3. §0/§4.3(c): drop Eq. (4) from the 2609.06423 defects. §4.3(d): "reality", not "causality".
4. §4.4: tag the acausal-branch mechanism [E] or drop it. State that the acausal choice *suppresses* the rate.
5. §4.5/§0: remove the QROCODILE-Drude claim (their limits use Lindhard + iΓ). Restrict [4.4] to q ≪ k_F, k_TF. Redo the WSi numbers.
6. [3.2]: the density-channel odd part is O(q³). Keep q-linear for the j/s channels.
7. §8 (a): add the commutation hypothesis and the cross-term error. Retag accordingly.
8. §4.6: N_qp = 2 holds for ω < 4Δ_BCS (optional sharpening).
