# R7 referee report REF-WP5-A (hostile, isolated) on returns/R6/WP5-v2.md

Read: WP5-v2.md, code/WP5-v2/checks.py (re-run: 37/37 PASS, ~3 s), CONVENTIONS, NOTATION (grep), CONTROLS, DONE, LIMITS,
WP0-v2 (§5.4–§7.3). Full texts fetched and read at the cited equations, then deleted: 2004.10709, 2001.06503, 2209.04503,
0812.2923, 2301.06592, 2506.03810, 1805.09942. No numerical simulation; sympy checks of a few seconds only.

## Verdict table
| # | Claim | Verdict | One-line reason |
|---|---|---|---|
| V1 | Theorem C, (W1): carrier rate = master formula with S_cc = 2\|Im Σ^GW\| | STANDS WITH CORRECTION | (W1) is the out-scattering rate. It equals 2\|ImΣ\| only when f·n_B → 0, and equals the GW lifetime only when Z → 1 (0812.2923 Eq. (1) has 2Z\|ImΣ\|, Z ≈ 0.8) |
| V2 | Theorem C(c): four Coulomb-line classes, g^S = g − g^L in (W2) | STANDS WITH CORRECTION | The argument is right, but there is no double counting only if the ionic part of ε_tot in (W1) and g^L use the same Z*, ε_∞, multipole content and range separation. The package does not state this |
| V3 | Theorem C(e) / L20: Born parameter Z_κα/v_N ≈ 3.7×10² at 1 keV | STANDS WITH CORRECTION | Wrong velocity. For v_N ≪ v_F the linearity parameter is Z_κα/v_F ≈ 15 (Si). The conclusion survives; the number is wrong by a factor of 25 |
| V4 | (W3) branching generating functional + moment equations | STANDS WITH CORRECTION | Correct first-step analysis. Missing hypotheses: a.s. termination and the minimal-solution choice. The (B2) density estimate is wrong by 10–30× and is compared with the wrong criterion (see V5) |
| V5 | (B2) "pair density ≲ 10¹⁹ cm⁻³ ≪ 𝓃_e" | STANDS WITH CORRECTION | 300 pairs in (10 nm)³ is 3×10²⁰ cm⁻³ (7×10¹⁹ for a 10 nm-radius sphere). That exceeds the Si Mott density. The relevant criterion is n_pair·a_X³, not n_pair/𝓃_e |
| V6 | Moment limits: Lindhard (L20) "first moment = 2001.06503 Eq. (3) exactly" | STANDS WITH CORRECTION | Exact only after adding the binary-collision approximation (uncorrelated targets at rest, pair potential) and Markov ion transport. A cross-section "on E^ad_0" is undefined. Must move to the truncation list |
| V7 | Moment limits: R&K mean (L21), Kinchin–Pease (L22), F_eh/F_NR as second moments (L23) | STANDS | Checked: R&K Eq. (5) is the first moment with an e–h seed; NRT is the first moment of N_FP; F_NR follows from the law of total variance |
| V8 | Asymptotics "n̄ = ω/ε_eh + b_N + o(1) [D, renewal theorem]" | STANDS WITH CORRECTION | The renewal-theorem hypotheses (stationary, non-lattice loss law with finite second moment) are not shown and fail for the 1/W² knock-on tail. Downgrade to [D, sketch] under stated hypotheses |
| V9 | (W4) exact bookkeeping and (W14) F_eh = (ε_eh/E_g − 1)𝔡_H | STANDS | Re-derived exactly below. (iii) phonon shot noise contradicts (ii) and is not evidence |
| V10 | (R-k) energy-only reduction: hypothesis Γ_k ≫ Γ_E "holds for e–ph above ~1 eV" | STANDS WITH CORRECTION | Γ_E must include Γ_ii, and Γ_ii ≳ Γ_ph above ~3–5 eV in Si. The stated hypothesis fails where the cascade is decided. A second hypothesis is needed (ii final states iso-energy random) |
| V11 | Binary thresholds E_R,th = 375 eV (Si), 465 eV (Ge) | STANDS WITH CORRECTION | The inputs are wrong: k_F(Ge) = 1.60 Å⁻¹ against 1.74 for 4 e/atom (gives 395 eV); Si gives 352 eV with k_F = 1.81. "Linear-response stopping vanishes below" is false in a crystal: suppressed, not zero |
| V12 | R&K: [A] must be energy³, so "5.2 eV²" is inconsistent | STANDS (CONFIRMED) | 2004.10709 Eq. (8) as printed: A·(E−ħω₀)^{1/2}/(E−E_g)^{7/2} |
| V13 | R&K Eq. (9): \|M_ph\|/\|M_eh\| should be squared; "Δ undefined" | STANDS WITH CORRECTION | Unsquared ratio CONFIRMED. "Δ undefined" REFUTED as stated: the paper defines it ("volume per electronic state"), and dimensions fix it as a real-space volume |
| V14 | R&K App. A: F_meas = ϵ_detF + 1 − ϵ_det, not F/ϵ_det + 1 − ϵ_det; "lower bound" wrong way | STANDS WITH CORRECTION | Formula and numbers CONFIRMED (HTML Eqs. (22)–(23)). The direction is right but the reason given is wrong: (23) − exact = F(1−ϵ²)/ϵ ≥ 0, so (23) is an upper bound. F_meas ≥ F_eh is irrelevant |
| V15 | Claims involving 2001.06503 | STANDS | The boundary-condition inconsistency is correctly attributed (their own remark). 0.0243 keV⁻¹ CONFIRMED |
| V16 | Claims against 2209.04503 | STANDS WITH CORRECTION | "½εS_e not derived" is REFUTED: it is derived in 2001.06503 App. B, Eq. (29). The "Z_1 = 12 in C, 10%" claim is UNRESOLVED; with Z_1 = 14 the difference is −7% |
| V17 | (W15) Fano-term TV bound and GaAs estimate \|ΔP\| ≲ 0.11Γ/δ | STANDS WITH CORRECTION | The bound algebra is right. c^F = Im(ρ*a^off) as written makes 𝔉 dimensionally wrong. A spread of 0.36 is unjustified (Q / valley dependence), so use ≤ 1, which gives ≲ 0.3Γ/δ. Ge (SOC) needs the Kramers-pair trace |
| V18 | Migdal drag-energy subtraction: GS first moment = q²/2M − E^{Mig}_1 | STANDS WITH CORRECTION | Inconsistent with "zeroth moment depleted by P_Mig" in the impulse regime: the X sector also carries recoil energy P_Mig·E_R. C20b encodes the inconsistent statement |
| V19 | Gap closure G1 / G3 / G12 (formula + computation spec) | STANDS WITH CORRECTION | Sufficient as specifications, except that the Z-factor / Eq. (1) vs (5) choice and the g^L ↔ ε_ion consistency must be fixed in the spec, not left to R1 |
| V20 | θ_seed size "≤ 50% in p_2 at 4–8 eV (2004.10709 [FT])"; "bounded by R&K's α-envelope" | STANDS WITH CORRECTION | The 50% in R&K is a 50% effect on DM limits and "systematics", not on p_2. The α family is e/h-symmetric, so it cannot bound an asymmetric DM seed |

## 1. Theorem C (V1–V3)
**(W1) normalisation (checked).** |𝒱|²S_cc = (e⁴/p⁴)|ρ|²(2p²/e²)L/(1−e^{−βω}) = 2v_C|ρ|²L/(1−e^{−βω}). The Fröhlich test passes. With
Im[−1/ε_tot] = (π ω_LO/2)(1/ε_∞ − 1/ε_0)δ(ω−ω_LO) for ω > 0, (W1) gives 2π∫d³p/(2π)³ (e²/p²)(ω_LO/2)(1/ε_∞−1/ε_0)δ(…)(n+1). This equals (W2)
with |g_Fr|² = (e²/Ωp²)(ω_LO/2)(1/ε_∞−1/ε_0) and (2π/N)Σ_Q = 2πΩ∫d³Q/(2π)³. Lindhard's slow-ion formula also follows. Take ω = k·v_N and
d cosθ = dω/(kv_N), and keep only ω > 0 at T = 0 (the factor 1/(1−e^{−βω}) → θ(ω)). Then −dE/dx = (2Z²α/πv_N²)∫dk/k∫_0^{kv_N}ωL dω, as stated.
**Correction V1a.** The thermal factor in (W1) is [1−f](1+n_B). GW gives 2|ImΣ| ∝ 1 − f + n_B = (1−f)(1+n_B) + f·n_B. The extra
f·n_B is the in-scattering term. So (W1) is the out-scattering rate, which is the correct cascade kernel, and equals 2|ImΣ| only when
f·n_B → 0 (true for hot electrons at T ≪ E_g). Reword "is 2|ImΣ^GW|" accordingly.
**Correction V1b.** 0812.2923 Eq. (1) (FT, checked) is τ^{-1} = (2Z/ħ)|ImΣ|. Their item (a) under Eq. (8) gives Z_kn ∼ 0.8. Item (b) says
Eqs. (1)/(8) contain no M_E (exchange) term. Hence:
- "Theorem C = GW lifetime" holds only at Z = 1, consistent with first order in W but numerically a ~20% global factor.
- That factor is not a near-threshold effect. §1.1(d) and R1 locate it "near threshold"; it belongs in θ_GW or a separate θ_Z.
- Item (d) (Kane exchange |M|²) cannot be "added to (W1)". (W1) has no |M_dir|². Exchange first needs Eq. (7) (Im W ≈ W_R Imχ₀W_R), which replaces Im W by W_R and is beyond the stated first-order-in-W hypothesis.
- Tag (d) [beyond hypothesis], not part of [D].
**Correction V2 (four classes).** Mapping WP0-v2 (5.5)'s ionic class (a phonon line at the external momentum) to "the ionic part of
ε_tot at the carrier's Coulomb line (p,ω)" is legitimate, and g^L is that same Coulomb line. Every line is then counted once only if:
- (i) ε_ion in (W1) and g^L use identical Z*_κ, ε_∞ (tensor) and ω_LO from the response/DFPT run;
- (ii) they have the same multipole content. §1.1 and §2 include quadrupoles in g^L ("SOTA R2") but build ε_ion "via DFPT Z*_κ, ε_∞" (dipole only). If the EPW g^L (dipole + quadrupole) is subtracted for GaAs, the quadrupolar long-range part is lost. Either subtract only the dipole g^L or put Q_κ into ε_ion;
- (iii) they have the same range separation. The EPW g^L carries a Gaussian (Ewald) cutoff over G, while (W1) sums the unscreened ionic head over all p = Q+G. A G-tail mismatch of order e^{−|Q+G|²/4α_E} is double-counted unless the same cutoff is used.

State (i)–(iii) as code-pair conditions (analogues of O4-d2).
**Correction V3 (Born parameter).** Bohr's κ = 2Z₁v₀/v is for a fast ion and electrons at rest. For v_N ≪ v_F (Si: v_F/c = 0.0070,
v_N(1 keV)/c = 2.8×10⁻⁴) the electron–ion relative speed is ~v_F. Linear (Lindhard) dielectric stopping is controlled by Z_κα/v_F ≈ 14.6 (Si)
and 35 (Ge); nonlinear DFT stopping (Echenique–Nieminen–Ritchie) is the standard remedy. Replace 3.7×10² by ≈15 in §1.1(e), §6.1 Validity and C6.
The conclusion ("Born fails") stands.

## 2. Branching functional and moments (V4–V10)
**(W3) is correct** as the backward Kolmogorov equation for a branching Markov process with additive 𝐍. It needs two more hypotheses. (H-t):
the tree terminates a.s. (each particle reaches an absorbing state in finite time; true if every non-absorbing state has a positive
energy-loss rate). (H-m): (W3) is solved by the minimal non-negative solution (iteration from the terminal data), since 𝔊 ≡ const
spuriously solves it at ϑ = 0. Add both to (B1)–(B3).
**V5.** 300/(10⁻⁶ cm)³ = 3×10²⁰ cm⁻³ (7×10¹⁹ for r = 10 nm), not ≲ 10¹⁹. "≪ 𝓃_e" (valence density) is the wrong test for (B2): Pauli
blocking is set by the occupation of the final-state window, and carrier–carrier Coulomb by n_pair a_X³ (Si a_X ≈ 4 nm, Mott density
~10¹⁸–10¹⁹ cm⁻³). Early keV ER tracks, and all NR tracks, are not dilute. (B2) holds for the eV–100 eV DM-electron seeds (≲ 30 pairs), which
is the G1 use. Restrict the claim and tag the keV case [C].
**V6 (Lindhard).** 2001.06503 Eq. (3) (FT) is a balance over binary collisions with a target at rest, with dσ_{n,e} cross-sections.
(W3) restricted to the ion type reproduces it only if collisions are binary and uncorrelated (BCA) and ion transport is Markov. Inside
E_R ≲ few keV dense cascades in Ge (thermal spikes) both fail. Step 3 "exactly … dσ_n = classical scattering on E^ad_0" must become
"exactly, given BCA + Markov (truncation 0)", and BCA moves into step 4's list.
**V7.** R&K Eq. (5) n(E_r) = 1 + ∫P⟨N⟩ (FT) is the first moment of (W5) with 𝔊_Λ = e^{ϑ_N}𝔊_e𝔊_h (P normalised to 2). NRT 0.8E_dam/2E_d is
a first moment. The law of total variance gives Var N = E[Var(N|E_el)] + Var(E[N|E_el]) = F_eh⟨E_el⟩/ε_eh + Var(E_el)/ε_eh². Dividing by
⟨E_el⟩/ε_eh gives F_NR = F_eh + Var(E_el)/(ε_eh⟨E_el⟩) (C12b). The C12a/C12c numbers re-computed: k_L = 0.1458, 𝓔_red = 0.608, g = 3.911,
E_el = 9.08 keV, σ/⟨E_el⟩ = 9.95%.
**V9 (W14), re-derived.** Fix ω and set E_st = E_esc = 0. (W4) gives N = (ω−ℋ)/E_g, so Var N = Var ℋ/E_g² and n̄ = (ω−⟨ℋ⟩)/E_g. Then
ε_eh = ω/n̄ = E_g + ⟨ℋ⟩/n̄ and F_eh = Var ℋ/(E_g²n̄) = [⟨ℋ⟩/(n̄E_g)]·[Var ℋ/(E_g⟨ℋ⟩)] = (ε_eh/E_g − 1)𝔡_H. Exact.
- Klein (i): ⟨E⟩ = (3/5)a for a √E density on [0, a], a = 3E_g/2, so ε_eh = E_g + 2(3/5)(3/2)E_g = 14E_g/5. Checked.
- (ii): Var = a²(3/7 − 9/25) = 12a²/175, so F = 2·Var/E_g² = 54/175. Checked.
- (iii) uses Var ℋ = ω₀⟨ℋ⟩ and drops the residual-KE variance. That variance is 0.21 eV² per carrier against ω₀⟨E_res⟩ ≈ 0.066 eV², and (ii) calls it the leading physics. (iii) contradicts (ii) and its 0.121 must not be cited as support. The text already hedges ("may be accidental"); make it [E, inconsistent model].
**V8.** Linearity with an o(1) offset needs a convolution (renewal) structure m(E) = ∫m(E−x)F(dx) + … with F stationary, non-lattice and
with finite second moment. For the primary the loss law depends on E (Bethe logarithm). The knock-on tail ∝ W⁻² up to E/2 gives ∫W²F(dW) ∝ E,
so the second-moment hypothesis fails and corrections can be O(ln ω), not o(1). Tag [D, sketch], state the hypotheses, and keep
"F_eh is a computable functional" (true without the theorem).
**V10 (R-k).** Write Γ_E = Γ^{ph}_E + Γ_ii (energy-changing rates). In Si above ~3–5 eV Γ_ii ≳ Γ^{ph} (this is why ε_eh ≈ 3E_g), so
Γ_k ≫ Γ_E fails exactly in the region of (W8) and p_2. (R-k) can still hold if ii final states are themselves iso-energy-distributed (large
unrestricted p). That is a separate, unproven hypothesis (R-k′) and belongs with gap R2, which currently covers only "below ~1 eV above
threshold".

## 3. Thresholds and nuclear recoil (V11, V18)
**V11.** Binary bound: in the ion frame an electron at v_F + v_N reflects to −(v_F + 2v_N) in the lab, so ΔE_max = 2m_ev_N(v_N + v_F). Checked.
The free-electron k_F with 4 valence e/atom is n = 32/a³:
- Si: a = 5.431 Å gives n = 0.1998 Å⁻³, k_F = 1.808 Å⁻¹ and E_R,th = 352 eV (C5 uses 1.75, giving 375).
- Ge: a = 5.658 Å gives n = 0.1767 Å⁻³, k_F = 1.736 Å⁻¹ and E_R,th = 395 eV. C5's k_F = 1.60 has no stated source and inflates the threshold by 18%.

Correct to ≈ 350 eV (Si) and ≈ 395 eV (Ge) [E]. The Ge 254 eV point (2405.10405) and the 2506.03810 comparison are unaffected.
"Below E_R,th the linear-response electronic stopping in a gapped crystal vanishes" is false beyond jellium. In (Theorem C(e))
−dE/dx needs L(k,ω ≥ E_g) at k ≥ E_g/v_N ≈ 2k_F. A crystal's L(k,ω) at k > 2k_F, ω ≈ E_g is the low-ω tail of the Bethe ridge, fed by the
high-momentum tail of the valence momentum density. That tail is small but non-zero. Replace "vanishes" by "is suppressed by the
valence momentum-density tail; the threshold is soft".
**V18 (drag-energy subtraction).** The nuclear f-sum is exact with the bare mass: ∫ω S_κκ dω ∝ q²/2M_κ per nucleus. In the impulse regime a
Migdal (X) event carries ω_e plus a recoil ≈ q²/2M_κ, so
𝓜¹_X = P_Mig q²/2M_κ + E^{Mig}_1 (+ small), E^{Mig}_1 = ∫ω_e dP_Mig = q·δM·q/2M² (TRK sum with δM = N_e m_e for an atom; checked).
Hence 𝓜¹_GS = q²/2M − E^{Mig}_1 − P_Mig q²/2M ≈ (1 − P_Mig)q²/2(M + δM), with zeroth moment (1 − P_Mig). The package's
"GS first moment = q²/2M − E^{Mig}_1, the remainder being the X-sector (Migdal) energy moment", together with "zeroth moment depleted by
P_Mig", is inconsistent unless X events carry no recoil. WP0-v2 §6.2(iii) writes 𝓜¹^{(e)} (the electronic part) for the X share.
Estimate: P_Mig ~ 2m_eE_R(m_e/M)⟨r²⟩ ≈ 5×10⁻³ at E_R = 1 keV (Si valence, ⟨r²⟩ = 1 Å², [E]) against δM/M = 2.7×10⁻⁴. The omitted
P_Mig E_R term dominates at keV.
Correct prescription: multiply S^{GS} by (1 − P_Mig(q)) and use M_κ + δM_κ in the (W9) δ-function; do not "rescale the first moment" alone,
which is operationally undefined (weight, energy axis or mass?). Fix C20b/C20c to include P_Mig·q²/2M.

## 4. (W15) Fano term in GaAs (V17)
Algebra checked. With Σ_ν𝔉_ν = 0, ΔP = Σ(𝔉_ν/Γ^tot)(P_ν − P̄), so |ΔP| ≤ ½(Σ|𝔉_ν|/Γ^tot)·spread. Also Σ_νΓ^{(ν)}|c̄ − c_ν| ≤ 2Γ^{ph}max|c|,
which gives the second inequality. Three corrections:
- (a) **Dimensions.** As printed, c_ν^F = Im(ρ*a^off). With WP0-v2 (6.3) |g|²[|ρ|²fp(1/δω²) + 2Re(a^{off*}ρ)PV(1/δω) + …], a^off ~ ρ/energy. So c^F ~ |ρ|²/energy, and 𝔉_ν = 2πΓ^{(ν)}(c̄ − c_ν) is not a rate. The GaAs estimate quietly uses 2π|c| = O(Γ_Λ₀|a^off|/|ρ|), i.e. c is normalised by Γ_Λ₀/|ρ|². State the normalised definition (or quote O4's) so that K_ν is dimensionless.
- (b) **Spread.** The first phonons differ in Q as well as energy. In GaAs intervalley (Γ→L, X) and intravalley emission send the carrier to valleys with different ii thresholds. Near the 1e⁻/2e⁻ boundary, and below 1 eV above threshold (R2: no (R-k) bound), max|P_ν − P_ν′| can be O(1). "≲ 0.36" from ΔE/0.1 eV ignores this. The defensible statement is |ΔP| ≤ 2π max|c| ≲ 0.3Γ/δ [E], with 0.11Γ/δ as optimistic.
- (c) **Ge with SOC.** The PT argument for 𝔉 = 0 needs (PT)² = +1 (real gauge). With SOC, (PT)² = −1, so ρ and a^off are quaternion-real 2×2 blocks and Im tr(ρ†a^off) = 0 only after the Kramers-pair trace. State that Λ₀ is Kramers-summed. The spec uses SOC for Ge.

## 5. Literature claims (rubric c) — verified in full text
| Paper / claim | Rating | Evidence |
|---|---|---|
| 2004.10709: [A] must be energy³ | CONFIRMED | Eq. (8): A(105/2π)(E−ħω₀)^{1/2}/(E−E_g)^{7/2}; table and text: "A = 5.2 eV²" |
| 2004.10709 Eq. (9) unsquared \|M_ph\|/\|M_eh\| | CONFIRMED | printed A = (\|M_ph\|/\|M_eh\|)(4π⁴/VΔ)(ħ²/2m)³ |
| 2004.10709: "Δ undefined" | REFUTED (as stated) | "Δ is the volume per electronic state"; with 1/(VΔ)·(ħ²/2m)³ and [A] = E³, Δ is a real-space volume |
| 2004.10709: E_r symbol collision | CONFIRMED | Eq. (5) E_r = deposited energy; Eqs. (15)–(16) "E_r are phonon losses" |
| 2004.10709 App. A: F/η + (1−η) wrong; exact ηF + 1 − η | CONFIRMED | HTML Eqs. (20)–(23) (PDF (A4)–(A7)); numerator F·n should be η²F·n |
| 2004.10709 numbers 0.130/0.160 vs exact 0.133/0.159, Eq. (23) 0.137/0.171 | CONFIRMED | recomputed |
| 2004.10709 "lower bound" has the wrong direction | CONFIRMED (package's reason wrong) | (23) − exact = F(1−η)(1+η)/η ≥ 0 (sympy) |
| 2004.10709 "~50% in p_2 at 4–8 eV" | UNRESOLVED / misattributed | text: "~50% in limits", "systematics on the order of 50%" |
| 2001.06503 BC inconsistency (ν̄′ → 1 vs 0) | CONFIRMED (their own remark) | text after Eq. (7) |
| 2001.06503 vs 2209.04503 reduced energy, 0.0243 vs 0.0268 keV⁻¹ | UNRESOLVED (0.0243 CONFIRMED) | 2209.04503 introduces Z_1 = 12 later, "effective number of valence electrons in the incident ion"; whether it enters C is not stated. Z_1 = 14 gives 0.0226 (−7%). "Parameters not transferable": CONFIRMED either way |
| 2209.04503: ½εS_e "not derived" | REFUTED | 2001.06503 App. B Eq. (29): mean-value theorem with t̄_n ≈ ⟨t_n⟩ = ε/2 (cited by 2209.04503 "following [5]"). Valid hostile point instead: the cross term ∫dσ_{n,e}T_nΣT_e is in tension with approximation (D)/(III) (separate nuclear and electronic collisions) |
| 2209.04503: Lindhard's Z^{1/6} by hand; U "effectively incorporates the Migdal effect"; χ²/dof = 1870/101, 680 eV–3 MeV | CONFIRMED | text. Minor misquote: Eq. (3) is U_EDFT; U = U_FP + U_EDFT is in the text |
| 2301.06592 Eq. (6) m_n vs nucleon μ_{m_D−n} (Eq. (5)) | CONFIRMED | printed |
| 2506.03810 "halted … below 10 eV_nr, as no ionization occurs below this threshold", Eq. (3) friction | CONFIRMED quote; inference [E] UNRESOLVED | the "property of the friction model" judgement is physics, not checkable in the text |
| 1805.09942 Eq. (4), 6.08 ± 0.18%, 19.7 eV, "TRIM predicts a monotonic, decreasing relationship" | CONFIRMED | text |

## 6. Rubric (a), (b), (d), (e), (f) remaining items
- (a) **[D] tags that are not derivations.** "(R-k) … error O(Γ_E/Γ_k) per generation" is asserted, not derived: tag [E]. "θ_seed bounded by R&K's α-envelope" is not a bound, because the Beta family imposes e/h symmetry (2004.10709 Eq. (6)) while a q ≠ 0 seed is e/h-asymmetric and electrons and holes have different thresholds: tag [E]. 𝔉 = 0 in Ge needs the SOC caveat (§4c).
- (b) **LIMITS L20–L23.**
  - Source quotes checked against full text: 2001.06503 Eqs. (3)–(7), 2209.04503 Eq. (2), 2004.10709 Eqs. (5)–(11), (16), (22)–(23).
  - L20: the truncation chain needs BCA as an explicit step (V6), the Born parameter is wrong (V3), the threshold numbers are wrong (V11), and discrepancy (3) is withdrawn (V16).
  - L21: chain correct. The three-body phase space Γ(3/2)³/Γ(9/2) = 2π/105 (checked: π^{3/2}/8 · 16/(105√π)). 2004.10709 §II step 5 indeed samples splits "by integrating over the density of states" and caps E_h ≤ W (= B_h, step 3).
  - L22: fine.
  - L23: fine, except the (iii) estimate (V9) and V14's reason.
- (d) **Consistency.**
  - Labels prefixed; S_cc ≡ S_chch (ch = c) is allowed by CONVENTIONS §6.
  - WP0-v2 (7.1)–(7.3) and (5.5) interfaces are consistent apart from V2 and V18.
  - "No new WP0-v2 defect" (§7) is acceptable, but WP0-v2 §6.2(iii)'s 𝓜¹^{(e)} wording invites the V18 misreading. Flag it to WP0.
- (e) **Gap closure.** G1: the spec is concrete (bands, W, kernels, grids, validation) and suffices as a specification once two choices are fixed in the spec: the Z-factor / 0812.2923 Eq. (1) vs (5) definition and the g^L ↔ ε_ion code-pair conditions (V2). G3: the formula plus MD/TDDFT spec is sufficient for the GS/heat partition. The sub-threshold charge channel rests on gap R3 (honestly stated). G12: the rates and the 1/t law are derived (C8 checked: 𝒩_bT(1−e^{−Γ_att t})/t; T_× = 76 K checked). The spectrum is [C] and stated so.
- (f) **Contested corrections:** none claimed. However, closing-table row 11 calls (W15) a "rigorous TV bound [D]". It is rigorous only once c^F is defined dimensionally (§4a).

## 7. Required corrections (summary)
1. (W1): out-scattering rate; = 2|ImΣ| only for f·n_B → 0. The GW lifetime has Z (≈0.8): a global θ_Z, not a near-threshold effect. Exchange (d) is beyond the first-order-in-W hypothesis.
2. Theorem C(c): add code-pair conditions (same Z*, ε_∞, ω_LO, multipole order and Ewald cutoff in ε_ion and g^L). GaAs must not subtract a quadrupolar g^L that ε_ion lacks.
3. Replace Z_κα/v_N ≈ 3.7×10² by Z_κα/v_F ≈ 15 (Si), 35 (Ge) in §1.1(e), §6.1 and C6.
4. Add (H-t) and (H-m) to (W3). Correct the (B2) density (3×10²⁰ cm⁻³) and criterion; restrict (B2) to ≲ 100 eV seeds.
5. L20 step 3: BCA + Markov as truncation 0.
6. Asymptotics: [D, sketch] with explicit renewal hypotheses.
7. (R-k): include Γ_ii in Γ_E. Add (R-k′) and extend gap R2.
8. E_R,th ≈ 350 eV (Si), 395 eV (Ge). The threshold is soft, not a vanishing.
9. R&K: withdraw "Δ undefined". Fix the "lower bound" reason to (23) − exact = F(1−ϵ²)/ϵ ≥ 0. Fix the θ_seed attribution.
10. 2209.04503: withdraw discrepancy (3) (derived in 2001.06503 App. B). Mark the Z_1 = 12 point UNRESOLVED (−7% with Z_1 = 14).
11. (W15): define c^F dimensionally. GaAs |ΔP| ≲ 0.3Γ/δ (worst case) [E]. Kramers trace for Ge.
12. Drag subtraction: S^{GS} → (1 − P_Mig)S^{GS} with M_κ + δM_κ in (W9). Fix C20b/C20c.
