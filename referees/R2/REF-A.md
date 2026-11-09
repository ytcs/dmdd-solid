# R2 / REF-A: hostile referee report on R1/D1 (golden rule) and R1/D2 (Kubo)

Scope: D1.md, D2.md, code/D1/symbolic_checks.py, code/D2/identities.py, STATEMENT, NOTATION, CONTROLS, DONE.
I ran no numerics. I ran one sympy script (< 5 s), quoted inline in §4 and §0. Equation numbers refer to the returns.
Only the items below count. Anything not flagged was checked and found correct.

## Verdict table

| # | Claim | Verdict | One-line reason |
|---|---|---|---|
| 1 | D1 (1)–(4) ≡ D2 (2.1)–(2.2), all factors | **STANDS WITH CORRECTION** | Amplitude, N, Ω, 2π, spin and α↔e² agree exactly. But D1's isotropic reduction 𝒢 = η/q is wrong by a factor 2 (it is η/2q). D2's script docstring drops the spin 2. |
| 2 | Pauli/exchange theorem (unrestricted m on shell) | **STANDS WITH CORRECTION** | The fermion signs and the on-shell substitution are correct, and the route list is complete. D1's resonance bound misstates the hole-type denominators. D2 extends the theorem to third-order ZPL terms without proof. |
| 3 | f-sum / DW: who compensates | **STANDS WITH CORRECTION (D2 correct, D1 compatible but loose)** | The Allen–Heine A² tadpole is first-moment neutral, so the compensation is Fan-type. D1's "DW" is the scattering e^{−2W}, which is not the AH tadpole. D2's per-diagram "cutting pair" is asserted, not derived. Only the sum (SE+V) is proven. |
| 4 | C7 acoustic limit | **FALLS (both)** | D1 drops O(1) intraband terms, so its i ℓ_Q(û·q)ρ_cv is wrong. D2's i u·(q − m_eΔv)ρ_cv sets intraband g_nn/(Q·v_n+ω_Q) → 0, but that ratio is 0/0 and finite. The true limit is direction-dependent. |
| 5 | Screening: DFPT g inside + one external 1/ε(q,ω) | **FALLS (as a proof)** | Both returns claim every Coulomb line carries either (q,ω) or Q. That is false: a third class carries the pair momentum (q+Q, ω∓ω_Q) and is Coulomb-proper, O(g²) and RPA-level. It is omitted. The rigid-shift limit shows the screening argument ε must be the pair's. |
| 6 | D1 §4: standard DFPT gives only path B | **STANDS WITH CORRECTION** | True of the Sternheimer output P_c∂ψ_v. But DFPT ∂V_SCF gives every g_mn, so SOS has all paths, and P_v∂ψ_v is a cheap finite sum. D1's adiabatic error scale δ is misidentified. |
| 7 | Resonance prescription; no ZPL interference at O(g²) | **STANDS WITH CORRECTION** | No interference holds (orthogonal phonon sectors). D2's window criterion misses the hole-path (B, m occupied) resonance, which is a ZPL at q, not a "band-crossing" effect. D1's E_min(q) is the right criterion. D1's "P" of 1/Δ² needs a Hadamard finite part. |
| 8 | D2: C8 decoy may fail for GaAs | **FALLS as stated** (survives only for m_χ ≲ 1 MeV) | It uses only q_min at a parabolic Γ valley. It ignores the q-integration and the Umklapp vertical ZPL at q ≈ G₁₁₁, which is open at E_dir for m_χ ≳ 0.9 MeV. |
| 9 | C1 optical limit | **STANDS WITH CORRECTION** | The prefactor 8π²α/(Ωω²), the paths, the Bose factors and the intraband terms all match. D1's partial-fraction derivation divides by zero for m = v, c, though the result is right. D2's nonlocal caveat misses the phonon-vertex commutator [g_NL, q·r]. |
| 10 | Wannier F_ij(R,q) recipe | **STANDS WITH CORRECTION** | The formula and the Umklapp handling are exact. But at keV q the weight of ρ_mv sits on the Bethe ridge (q²/2m_e ≈ 13.6 eV·(q/αm_e)²), outside an 8–16-band manifold, so the recipe and its cost need a plane-wave/Sternheimer high-band remainder for ρ **and** g. Also missing: PAW augmentation at all q for US/PAW inputs, Si dynamical quadrupoles in g, and a nonlocal-modified f-sum for C4 checks. |
| R4 | Rung-4 rubric sweep | see §11 | Time orderings, Pauli, Bose, normalisation, Umklapp and sign of q are clean. The rubric failures are screening (5), DM kinematics (1, factor 2) and C7 (4). Yield/threshold is not addressed (deferred). |

---

## 1. Term-by-term agreement

**Amplitude.** Take D2 (2.1) and set ω = ε_{ck'} − ε_vk ± ω_Q. The first denominator becomes ω − ε_{m,k+q} + ε_vk = ε_{ck'} − ε_{m,k+q} ± ω_Q, which is D1 (1). The second denominator is identical. D2's M carries N^{−1/2}. D1 puts the N^{−1/2} in T_fi. So M_{D2} = N^{−1/2}M_{D1}. The phonon labels agree: the A_Q = b_Q + b†_{−Q} term of H_ep both emits −Q and absorbs +Q with the same g(·,Q), and no other term contributes.

**S and ε₂.** Derived from scratch:
S = (2π/V)·2·Σ_{kQcvν±} N^{−1}(n+½±½)|M_{D1}|²δ = (4π/Ω)N^{−2}Σ_{kQ}(…), which is D1 (2).
Then ε₂ = (e²/2q²)S = 2πe²/(Ωq²)⟨⟨…⟩⟩ = 8π²α/(Ωq²)⟨⟨…⟩⟩, which is D1 (4).
D2 (2.2) gives 2πe²/(q²V)·Σ_{kQ}N^{−1}|M_{D1}|² = 2πe²/(Ωq²)⟨⟨…⟩⟩. They are identical.
- The spin factor 2 cancels the ½ of the ε₂–S conversion in both. D2 says so.
- Correction: `code/D2/identities.py` check (3) states ε₂ = (π e²/q²V)Σ|⟨f|n_q|0⟩|²δ. That omits the spin 2 and contradicts (2.2). It is harmless only because the check is dimensional.
- Rate: Γ = ∫d³q/(2π)³|Ṽ|²S and |Ṽ|² = πσ̄_eF²/μ² are correct in both.

**Error in D1 §2 (isotropic reduction), confirmed by sympy.** Take ∫d³v f δ(ω − q·v + q²/2m_χ). The angular integral gives 2π/(qv)·Θ(v − v_min). Hence
𝒢 = (2π/q)∫v f dv = **η(v_min)/(2q)**, with η ≡ ∫d³v f/v Θ.
D1 writes η/q. Consequences:
- D1's prefactor ρ_χσ̄/(2π m_χρ_Tμ²) must be ρ_χσ̄/(4π m_χρ_Tμ²).
- D1's crystal form factor "4π²/(αm_e²Ω)" must be 2π²/(αm_e²Ω).
- D1's open item comparing 4π² with Essig's printed constant is therefore contaminated by its own factor 2.

Eq. (3) itself is correct. Only the reduced form is wrong. This is a rung-4 "DM kinematics" defect.

## 2. Pauli/exchange theorem

**Signs.**
c†_m c_v c†_c c_m|Φ₀⟩ = −c†_c n_m c_v|Φ₀⟩ = −c†_c c_v|Φ₀⟩ for m occupied. For m empty the result is +c†_c c_v|Φ₀⟩. D2's commutator form [c†_{v'}c_v, c†_c c_{v'}] = −c†_c c_v agrees.

**Substitution.**
- Path D: −g_cmρ_mv/(ε_m − ε_c' ∓ ω_Q) = g_cmρ_mv/(ε_c' − ε_m ± ω_Q). This is the A form on shell.
- Path C: −ρ_cm g_mv/(ω − ε_c' + ε_m). With ω − ε_c' = −ε_v ± ω_Q this becomes ρ_cm g_mv/(ε_v − ε_m ∓ ω_Q), the B form.
- The S1a/S1b checks reproduce both.

**Completeness of routes.** Two one-body vertices take Φ₀ to one pair. Either the first vertex creates (a; b) and the second moves a → c (b = v) or v → b (a = c), or the first vertex is diagonal, which requires q ∈ G (measure zero). There are no other routes. **Stands.**

**Off shell.** The identity uses ω = E_f − E_i. Three consequences:
- (a) Off-shell quantities, such as ε₁^{PA}, need the four-path or Kubo form. Both returns say so, and neither uses ε₁^{PA} at O(g²) in the window.
- (b) Inside a broadened resonance (D1 §5.2), the unrestricted form is wrong by O(γ/Δ) for the hole-type terms. This is harmless at the stated precision.
- (c) **Unproven extension.** D2 §2c item 4 applies "the same Pauli argument" to the third-order virtual-phonon vertex δρ^V, which has two energy denominators and a zero-phonon final state. That is a different identity, with three time orderings and intermediates on both sides. It is not shown. It must be derived, or the ZPL bookkeeping in §2c–§3 must be stated in Kubo form only.

**D1 §5.1 "theorem" misstated.** D1 claims that for ω < E_min(q) every denominator satisfies |Δ| ≥ E_min(q) − ω. That holds only for:
- A with m empty, where the denominator is ω minus a momentum-q transition;
- C (the B form with m occupied), where it is ω − (ε_{c,k+Q+q} − ε_{m,k+Q}).

For D and for B with m empty, the denominators are momentum-Q transition energies ± ω_Q, bounded by E_g ∓ ω_Q and not by E_min(q) − ω. When E_min(q) > 2E_g these are the **smaller** of the two. Correct bound: |Δ| ≥ min(E_min(q) − ω, E_g − ω_Q). The conclusion that nothing vanishes still holds, but it feeds into §6.

## 3. f-sum rule and "Debye–Waller"

**Exact statement (agrees with D2 §3).** For an all-electron Hamiltonian, [H_ep, n_q] = [H_DW, n_q] = [V_ee, n_q] = 0. So ∫₀^∞ωS dω/2π = n_e q²/2m_e at every order. This holds for both ε₂ and L.

**AH tadpole is neutral.** The proof needs one more step than D2 gives. The tadpole is ⟨H_DW⟩ = ½Σ⟨uu⟩:∂²V(r), a static local one-body potential δV. For the electronic Hamiltonian H_e + δV the double commutator is [[T,n_q],n_q†] = N_e q²/m_e, a c-number independent of the state. So the first moment of the ZPL is unchanged at O(δV). The two-phonon final states of H_DW are O(g⁴) in weight. **D2 is right**: the tadpole contributes zero net first moment.

**Who compensates.** At O(g²) the first-moment shift equals the 1/ω² coefficient of the high-frequency expansion of Π.
- The reducible diagram (X), χ⁰gDgχ⁰, goes as ω^{−6}, so it contributes zero.
- (T) vanishes at equilibrium.
- (DW) contributes zero, as shown above.

Hence M₁(SE-p + SE-h + V) = 0. Its phonon cut is M₁^{SB} > 0, so its non-phonon cuts give −M₁^{SB}. This is the **aggregate** "cutting pair" and it is proven.
- D2's stronger claim, "each diagram's phonon cut and non-phonon cut add to zero", is asserted with no derivation. It is not obvious for (V), whose phonon cut 2Re A₁A₂* has no definite sign. It must be downgraded to [C] or proven.
- D2's "mainly from g_cc − g_vv" is an estimate inside a [D] block.

**D1.** D1 §5.3 and §6.2(b) say the sideband is compensated by "the reduction of the zero-phonon weight … e^{−2W}". The e^{−2W} of the rigid-shift (BO) picture expands at O(u²) into contributions from second-order linear coupling (Fan type) and from first-order ½uu∂²V (AH tadpole). By the argument above, only the Fan-type part moves first moment. So D1 is **right if "DW" means the scattering/Huang–Rhys ZPL factor**, and wrong if it means the AH tadpole. D1 never says the latter, but it lists "Debye–Waller shifts of ε_nk" (AH) alongside the e^{−W} dressing without separating them.

**Verdict.** They are saying the same thing at the level of the claim "ZPL weight reduction compensates". D2's sharper attribution is correct. The paper must fix one meaning of "DW".

Both returns agree that formula (4)/(2.2) alone overshoots C4 by +M₁^{SB}, and that the compensation occurs at ZPL frequencies, outside the window. That stands.

## 4. C7 acoustic Q → 0 limit: derivation

**ASR (both returns, correct).** For an acoustic mode at Q = 0, Σ_κ∂_κV = −∇V = −i[p, H₀] for local V. Hence
g_ab = (ε_b − ε_a)A_ab, with A = −iℓ_Q û·p, ℓ_Q = (2M_cell ω_Q)^{−1/2} (plus N^{−1/2} in D2's convention).
In particular g_aa(Q = 0) = 0.

**Off-diagonal terms.** Set ω_Q → 0 in the m ≠ c terms of A and the m ≠ v terms of B:
Σ_{m≠c}(ε_m − ε_c)A_cmρ_mv/(ε_c − ε_m) + Σ_{m≠v}ρ_cm(ε_v − ε_m)A_mv/(ε_v − ε_m) = −(Aρ)_cv + A_ccρ_cv + (ρA)_cv − ρ_cvA_vv,
which equals [ρ, A]_cv + (A_cc − A_vv)ρ_cv = iℓ_Q û·(q − m_eΔv)ρ_cv.
This uses [e^{iq·r}, p] = −q e^{iq·r} and A_nn = −iℓ m_e û·v_n.

**D1's error.** D1 uses S3c: (E_m − E_f)/(E_i + ω − E_m) = −1 + ω_Q/(E_i + ω − E_m). It keeps the −1 for **all** m and discards the rest as O(ω_Q/δ). For m = f (that is, m = c in A) the denominator is itself ω_Q, so the discarded piece equals +A_ccρ_cv, which is O(1). The same happens for m = v in B. D1's i ℓ_Q(û·q)ρ_cv omits the −m_eΔv term **even within its own assumptions**.

**D2's error.** D2's sympy check (2) sets g_ff = λ(e_f − e_f)d_ff = 0 and lets ω₀ → 0. The intraband term is then 0/ω₀ = 0. Physically ω_Q and Q vanish together, and for acoustic branches g_nn(k,Q) = iℓ_Q Q·Ξ_n·û + O(Q²ℓ), the deformation potential. The m = c term of A and the m = v term of B are then
T_c = g_cc ρ_cv/(ε_{c,k+q+Q} − ε_{c,k+q} + ω_Q) → iℓ_Q (Q̂·Ξ_c·û)/(Q̂·v_c + c_ν(Q̂)) ρ_cv,
T_v = ρ_cv g_vv/(ε_vk − ε_{v,k+Q} − ω_Q) → −iℓ_Q (Q̂·Ξ_v·û)/(Q̂·v_v + c_ν(Q̂)) ρ_cv.
These are **O(ℓ_Q)**, the same order as the claimed result, and direction-dependent.

Sympy check (3 levels, intraband g = iXQ and iYQ, band slopes s_c and s_0, ω_Q = c_sQ, limit Q → 0):
limit − D2 form = i ρ_cv[X/(c_s + s_c) − Y/(c_s + s_0)] ≠ 0.

Size estimate: Ξ ~ 5–10 eV and c_s ~ 3×10^{−5}, so at band extrema Ξ/c_s ~ 300 keV. That is ≫ q ~ keV. **The deformation terms dominate the limit by about 10²** [E].

**Correct statement:**
M^{(2)}_{ac}(Q → 0) = iℓ_Q ρ_cv(k,q)·[û·(q − m_eΔv) + (Q̂·Ξ_c·û)/(Q̂·v_c + c_ν) − (Q̂·Ξ_v·û)/(Q̂·v_v + c_ν)] + O(Q^{1/2}).
(The split between the Δv and Ξ pieces depends on how g_nn is decomposed. Only the sum is meaningful.)

What survives from both returns:
- (i) M = O(ℓ_Q), so |M|²(n+1)Q²dQ ~ QdQ at T = 0 and ~ dQ at T > 0. It is integrable.
- (ii) M ∝ ρ_cv(k,q), so it vanishes at q → 0 (c ≠ v).
- (iii) In the window the limit is kinematically inaccessible. As Q → 0, the A denominator for m = c is ω − (ε_{c,k+q} − ε_vk) ≤ −(E_min(q) − ω) < 0, while it must → 0.

So C7 can only be tested off shell, or in the ZPL-open region.

**Consequence.** The CONTROLS amendment (D2's formula) would flag a **correct** EPW implementation as buggy, because a real code uses the true g_nn(k,Q). It must be replaced by (i)–(iii) plus the formula above.

## 5. Screening

**The claimed partition is incomplete.** D2 §4b: "every Coulomb line either carries (q,ω) or the phonon momentum; no Coulomb line can belong to both classes". D1 §3 says the same. There is a third class.
- Take a triangle T(q, Q → q+Q) with one ρ vertex and one g vertex, emitting a Coulomb line at (q+Q, ω∓ω_Q).
- Follow it with a bubble chain χ⁰(q+Q), and close with T*. The phonon line joins the g vertices.
- Cutting the (q+Q) Coulomb line does not disconnect the diagram, because the phonon line remains. So it is Coulomb-proper with respect to q.
- It is O(g²), at the same RPA (bubble-chain) level as the external 1/ε(q,ω) both returns keep.
- It is neither DFPT screening, which is in channel Q, nor "local fields of the DM vertex", which is what D1 §5.5 excludes.

Physically, the second-order density at (q+Q) produces a Hartree field that drives the same final pairs. This is the RPA final-state screening of the composite vertex.

**The rigid limit shows it matters at O(1).** For a rigid acoustic shift, the exact BO result is a convolution with ⟨e^{−iq·u(t)}e^{iq·u}⟩. Its one-phonon term is
|q·u|²S_el(q, ω − ω_Q) = |q·u|²(2q²/e²)ε₂⁰(q, ω−ω_Q)/|ε(q, ω−ω_Q)|².
So the single screening factor belongs to the **pair channel** (q+Q → q, ω − ω_Q).
- D1 and D2 give |q·u|²ε₂⁰(q, ω−ω_Q)/|ε(q,ω)|². That coincides only to O(ω_Q∂_ωε₁) because q+Q → q.
- Naively adding the omitted chain on top of 1/ε(q,ω) gives 1/|ε|⁴ in this limit, which is wrong.

So the internal (q+Q) chain and the external (q,ω) chain must partially cancel. The cancellation presumably involves the displaced induced charge, a term absent from "DFPT g + external 1/ε". Neither return shows this. In general (Q not small) the relevant screening is some combination of ε(q,ω) and ε_{GG'}(q+Q, ω∓ω_Q).
- For Si near the indirect edge, |q+Q+G|_min ≈ 0.85·2π/a ≈ 1 Å⁻¹, where ε ~ 2–4 [E]. This is not a small correction.

**What stands.**
- DFPT g is the correct Q-channel dressing, and the bare g would be wrong.
- Applying 1/ε(q,ω) to g would be wrong.
- In the window ε₂⁰(q,ω) = 0, so L^{PA} = ε₂^{PA}/ε₁⁰² + O(g⁴) given the proper Π^{PA}. D2's exact expansion shows this needs no H2. D1's H2 is redundant there.
- H1 (ω ≫ ω_LO) and H3 (O(g²)) are correctly used. The static screening of g, O(ω_Q/E_g), is correct.

**Required correction.** Π^{PA} must include the (q+Q)-channel RPA dressing, with ε_{GG'}(q+Q, ω∓ω_Q) acting on the projection of M_f onto ρ_f(q+Q+G). Then show that the result reduces to 1/|ε(q, ω−ω_Q)|² in the rigid limit, or bound the effect numerically. Until then "no double screening" is unproven, and missing screening is likely. This is a correlated error of the two "independent" derivations.

## 6. Adiabatic claim (D1 §4)

∂_λD = ⟨∂ψ_c|e^{iq·r}|ψ_v⟩ + ⟨ψ_c|e^{iq·r}|∂ψ_v⟩.
- The second term is Σ_m ρ_cm g_mv/(ε_v − ε_m): the B form, with m empty for B and m occupied for C.
- The first term is the A form: m empty is A, m occupied is D.

DFPT's Sternheimer output is P_c|∂ψ_v⟩, which is path B only. **Correct.** Corrections:
- (a) "Standard DFPT gives only path B" is true only of the wavefunction route. DFPT's ∂V_SCF gives every g_mn (as EPW uses it), so the SOS form (1) has all four paths at no extra DFPT cost.
- (b) P_v|∂ψ_v⟩ = Σ_{v'}|v'⟩g_{v'v}/(ε_v − ε_{v'}) is a finite occupied-band sum, not an extra solve.
- (c) The error δ: from §2, the smallest denominator is min(E_min(q) − ω, E_g − ω_Q), not "the distance to the nearest first-order threshold". For Si, ω_Q/E_g ≲ 6%, which caps the adiabatic error from below the claimed estimate in the deep window.
- (d) The non-SCF Sternheimer for ∂ψ_c is well conditioned in the window, because ω − ω_Q < E_min(q). The returns should state this.

## 7. Resonances and interference

**No interference.** Zero-phonon and one-phonon final states are orthogonal in the phonon factor, so the rate is Σ_f|A_f|². D2's parity argument (n_q even, H_ep odd in A) gives the same result. It fails only when the exact eigenstates mix sectors (degeneracy), which is excluded in the window. **Stands.**

**Window criterion.**
- D2 §2b says A₂ with m valence is a "hole-relaxation resonance, only near band crossings". On shell, ε_vk − ε_{m,k+Q} ∓ ω_Q = 0 ⇔ ω = ε_{c,k+Q+q} − ε_{m,k+Q}. That is a **first-order transition at the same q** from occupied m, generic and not tied to band crossings.
- D2's criterion (A₁ only) is therefore incomplete.
- D1's E_min(q), minimised over all occupied n and empty m, covers both. D1 §5.4 is the correct prescription.

**Linewidth split (D1 §5.2).** |Δ + iγ/2|^{−2} = (2π/γ)δ(Δ) + FP(1/Δ²) needs the Hadamard finite part, not a principal value. The resonant/non-resonant cross terms give P(1/Δ). This is formal only, because D1 restricts quantitative claims to the window.

## 8. C8 decoy (D2)

The arithmetic is correct: q_min = 1.5 eV/(794 km/s) = 562 eV = 0.285 Å⁻¹, and q²/2(m_c + m_h) = 0.55 eV (parabolic). The argument still fails as stated:
- (a) dR/dω integrates over all q ≥ q_min, so the decoy concerns the q-integrated rate, not the edge at q_min.
- (b) **Umklapp.** At |q| ≈ |G₁₁₁| = 1.93 Å⁻¹ (3.8 keV), k+q folds onto k, and the vertical Γ ZPL is open at E_dir with form factor ⟨u_c|e^{iG·r}|u_v⟩ ≠ 0. This is kinematically allowed when qv_max − q²/2m_χ ≥ ω, i.e. **m_χ ≳ 0.9 MeV** at ω = 1.5 eV. The ZPL then occupies a shell of thickness ~√(2M(ω − E_dir)) ≈ 0.09 Å⁻¹ at ω − E_dir = 0.1 eV. The PAER/ZPL ratio is ~10^{−3}–10^{−2} (D2's own C3), so the PAER-leads window closes [E].
- (c) The L valley (E_L ≈ 1.71 eV) needs |q| ≈ 0.97 Å⁻¹ (1.9 keV), so it caps the window only where that q is reachable.
- What survives: for m_χ ≈ 0.4–0.9 MeV (ω_max = ½m_χv_max² ≥ E_dir + ω_LO), both the Umklapp and L-valley ZPL can be kinematically closed. **Restate it as a flag for that mass band only.**
- The same logic applies to Si itself: the ZPL at q ≡ k_c − k_v (≈ 1 Å⁻¹) is open at E_g for m_χ ≳ 0.5 MeV. T5 must quote the window in (m_χ, ω) after the q-integration, not in (q, ω).

## 9. C1 optical limit

D2's route is exact for local potentials: ⟨f|n_q|i⟩ = ⟨f|q·j_q|i⟩/ω on shell (E_f − E_i = ω, phonon included). The q → 0 limit gives (q/ω)q̂·M_v, with M_v using v_mn including v_nn and the same denominators.
- Check: expanding the intraband m = v (A) and m = c (B) terms with ε_{n,k+q} = ε_nk + q·v_n gives (g_cv/ω²)q·(v_vv − v_cc). That matches M_v.
- D1's final S₁, S₂ (all m) agree. D1's derivation, however, uses X_mv = q·v_mv/(ε_m − ε_v) (S3a/S3b), which is undefined for m = v and m = c. The intraband terms come from the k+q shift of ε and g, which D1 never does. The result is right and the derivation has a gap.
- Prefactor: 2πe²/(Vω²)·N^{−1}Σ = 8π²e_G²/(Ωω²)N^{−2}Σ in both. That matches the Hall–Bardeen–Blatt/Noffsinger form with spin included and with S₁ (photon first, ε_m − ε_v − ω) and S₂ (phonon first, ε_m − ε_v ± ω_Q).
- ε^L = ε^T: holds after the full k, Q, band sum by O_h invariance of a rank-2 tensor. D2's "ê·" should read "q̂·" before that step.
- Gauge and nonlocality: the ρ form is the gauge-invariant longitudinal vertex. Its equivalence to the velocity form uses energy conservation, so it is on shell only. With nonlocal V_NL, [H, n_q] gains [V_NL + u·∂V_NL, e^{iq·r}]. At O(q) this gives v = p/m + i[V_NL, r] **and** a phonon-vertex term i[g^{NL}, q·r]_cv/ω.
  - D1 keeps both. **D2's caveat ("holds only approximately") is wrong in kind.** The identity is exact with the full current. D2 misses the [g^{NL}, r] term, which standard Noffsinger-type velocity matrix elements also omit.
  - For C1 comparisons, state which velocity the reference used.

## 10. Recipe (D1 §7)

**F tensor.** With ψ_nk = N^{−1/2}Σ_R e^{ik·R}Σ_j U_jn(k)w_jR:
⟨w_{iR'}|e^{iq·r}|w_{jR}⟩ = e^{iq·R}F_ij(R' − R, q),
so ρ_mn = [U†(k+q)F̃(k+q, q)U(k)]_mn with F̃(κ,q) = Σ_R e^{−iκ·R}F(R,q). The checks:
- F̃(κ+G) = F̃(κ), so unfolding is immaterial, the periodic gauge is consistent, and Umklapp is automatic.
- |F(R,q)| ≤ ∫|w_iR||w_j0| decays in R.

**Stands for the in-manifold block.**

**Missing pieces:**
- (a) **Bethe ridge.** At |q| ≳ αm_e, the f-sum Σ_m(ε_m − ε_v)|ρ_mv|² = q²/2m_e puts most of the weight of ρ_mv(k,q) on bands at ε_m − ε_v ≈ q²/2m_e (13.6 eV at 1 a.u., 54 eV at 2 a.u.). Those bands lie outside an N_W = 8–16 manifold.
  - Path A, Σ_m g_cm(k+q,Q)ρ_mv/(…), therefore needs ρ **and** g_cm to high bands. EPW interpolates g only within the manifold.
  - The "Sternheimer remainder" must be a plane-wave solve per (k, q, Q), (H − ε_{ck'})|∂ψ_c⟩ = …, contracted with e^{iq·r}. Its cost is O(N_PW log N_PW · N_iter) per (k,q,Q), not the O(N_W³ + N_mN_νN_cN_v) quoted.
  - The cost estimate must be redone, and the N_W-only route flagged as valid only for q ≲ 0.5 αm_e [E].
- (b) **PAW/US augmentation.** It is needed at **all** q, not only at q ≳ 3–4 keV: without the augmentation charges, ρ_nn(k,0) ≠ 1. For norm-conserving inputs, the pseudo-versus-AE error grows with q, as D1 states.
- (c) **Nonlocal pseudopotentials.** They do not enter the ρ vertex (e^{iq·r} is local). They do enter the C4 check: with V_NL the f-sum becomes ⟨[[H, n_q], n_q†]⟩ ≠ N_eq²/m_e, so the numerical sum-rule test must use the modified double commutator. They also enter the C1 comparison (§9).
- (d) **Si dynamical quadrupoles.** The long-range part of g in nonpolar Si is not captured by "Fröhlich only for polar". It is needed for accurate Wannier interpolation of g at small Q.
- (e) The ASR correction to g is fine. It interacts with §4: the corrected g_nn must keep its O(Q) deformation part.

## 11. Rung-4 rubric sweep (other items)
- Time orderings and exchange: complete (§2).
- Bose factors: n+1 and n, with n_{−Q} = n_Q. Correct.
- Spin factor: correct in both, apart from D2's script docstring.
- Phonon normalisation: ℓ = (2NMω)^{−1/2} with g = O(1) and an explicit N^{−1/2}. Consistent with EPW.
- Umklapp: correct. Sign of q: e^{+iq·r} in both. Correct.
- Double counting with first order: handled by D1 §5.2/§5.4. With ZPR: D1 §5.4 (renormalised edges). Correct to O(g²).
- Resonant denominators: §7. Dipole limit: neither misuses it.
- Screening: §5 (FALLS). DM kinematics: §1 (factor 2).
- Ionization threshold and yield: not addressed by either return. Deferred to T5, but it must appear before any reach statement.
