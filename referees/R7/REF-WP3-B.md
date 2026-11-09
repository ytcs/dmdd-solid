# R7 / REF-WP3-B: hostile referee report on returns/R6/WP3-v2.md (+ code/WP3-v2/checks.py)

Isolated referee B. Read only: WP3-v2, checks.py, CONVENTIONS, NOTATION, CONTROLS, DONE, LIMITS, WP0-v2. checks.py re-run: 66/66 PASS in ~10 s.
Full text fetched for this review and then deleted: 2603.13052, 2210.06490, 1604.02394, 1607.01789, 2302.08085.
Extra checks I ran: sympy/numpy Christoffel eigenvalues for Si elastic constants (< 5 s, no simulation).

## Verdict table
| # | Claim (location) | Verdict | One-line reason |
|---|---|---|---|
| 1 | PAER amplitude (M.1)–(M.2), four paths, Pauli/exchange theorem (§M2) | STANDS | Re-derived: D gives the A-form and C the B-form on shell; the q = 0 cancellation is exact (not only on shell) |
| 2 | Rate and ε₂^{PA} (M.3)–(M.4); S^{X+} = (2q²/e²)L^{PA}/(1−e^{−βω}) (M.14), (W.4c) | STANDS WITH CORRECTION | The thermal factor is applied twice. (M.3), (M.4) and (M.14) cannot all hold as equalities. Effect O(e^{−E_g/T}) |
| 3 | η/(2q), (M.5)–(M.7) | STANDS | Re-derived ∫d³v f δ(ω−ω_q) = η/(2q) and the 1/(4π) prefactor of (M.6) |
| 4 | Window (M.8)–(M.9), no sideband–ZPL interference | STANDS WITH CORRECTION | Bounds re-derived. But every numerical example (Q_w, Q_min) uses δ₀ = 0.1 eV, which breaks the theorem's own δ₀ ≫ ω_max ≈ 60 meV |
| 5 | Dyson convention outside the window (M.10), DC, O4 (iv″) | STANDS | Hadamard fp is correct; the O(Γ²) remainder checked. The rigorous version stays [C], as the package states |
| 6 | f-sum, aggregate compensation (M.11), §M5 | STANDS | Commutators vanish for a local H. The per-diagram claim is correctly withdrawn to [C] |
| 7 | Screened amplitude M̃ (M.13), tagged "[D at RPA/ALDA]" | STANDS WITH CORRECTION | [D] only at RPA (TDH). ALDA adds a second-order xc source k_xc δn_q δn_Q at P that is missing. The pair line (P,ω_f) is always open, so W must be retarded |
| 8 | Interim systematic [0.5, 1.2] on L^{PA} | STANDS WITH CORRECTION | Not derived. The bracket assumes δ_pair < 0, which the package itself tags [C]. With the sign open it becomes [0.5, 1.7] |
| 9 | Soft limit (M.15), Ward identity (M.16), C7a–e, IR | STANDS | Interband [ρ,𝔄] + (𝔄_cc−𝔄_vv)ρ and the intraband Ξ = D + v⊗p cancellation re-derived; power counting re-checked |
| 10 | Fixed-q onset p_on = 2 / 3 / ½ (§M3) | STANDS | Two independent parabolic pockets give ∫√x√(E−x) ∝ E². A linear acoustic tilt does not change the exponent |
| 11 | Angle-averaged p̄_on = p+1 generic; "isolated quadratic minimum at q̂ ∥ K̂ for acoustic branches" (C23a) | STANDS WITH CORRECTION | True only for an isotropic c_ν. A minimum over q̂ must include c_ν(Q̂*); see §3 |
| 12 | **Si TA S̄ edge p̄_on = 4 at E_g^{ren} + c_TA d** (§M3 (ii), §3 L8, IF-5) | **FALLS** | Two independent reasons: (a) Si elastic anisotropy makes q̂ ∥ K̂ a *maximum* of the TA threshold; (b) the valence shear deformation potential gives a nonzero on-axis TA vertex. Si TA: p̄ = 3 at ≈ E_g^{ren} + 0.97 c_TA d |
| 13 | Edge-shell criterion Q_w = (2(m_c+m_h)δ₀)^{1/2} | STANDS WITH CORRECTION | Leading-order derivation correct. Use a δ₀ consistent with (M.9) (0.3 eV → ≈ 0.35 Å⁻¹) and the longitudinal masses |
| 14 | Four Migdal formulas as truncations of (W.5); 4α prefactor | STANDS | (W.5) with S^{ee} = (2p²/e²)Im(−ε^{-1}) and U = Ze²/p² gives 4α exactly; the L7a dipole identity re-derived |
| 15 | 2603.13052 Eq. (3.11) prints S(q−k_e+K) (paper wrong) | CONFIRMED | Full text: (3.11) and (4.1) print +K. Parent 2210.06490 (3.8) has −K, and momentum transfer k_e+K requires −K |
| 16 | 2603.13052 Eq. (4.7) has the wrong dimension, and is ½ of KKL (paper wrong) | CONFIRMED, with correction to the package | (4.7) is dimensionless. Its partner (4.6) carries an *extra* 1/m_N, so the product is dimensionally right. Replacing m_N → m_N² in (4.7) alone breaks (4.6). C3b ignores (4.6) |
| 17 | 2210.06490 fn. 3 bound is conservative; the EFT and the impulse formula are one function | CONFIRMED / STANDS WITH CORRECTION | The footnote itself says "most conservative". The package's leading correction "≈ 10⁻⁵" is too small by ~10: ω_ph²/ω_e² ≈ 1.4×10⁻⁴ |
| 18 | ZG energy-δ defect against 1604.02394 Eq. (24) | CONFIRMED (characterisation, not an error of the paper) | Quote verified verbatim. The paper itself calls Eq. (24) the adiabatic limit. The O(1) onset error at the lowest m_χ follows. "Antithetic pairing" is a misnomer |
| 19 | EPW 2302.08085 (60)–(63): Wannier-only j sum; iη at resonance | CONFIRMED | Text: "restricted to the manifold … included in the Wannierization"; "a more general theory … is under development". Prefactor 8π²α checked |
| 20 | Crystal NR bremsstrahlung (W.13); GaAs ≈ 2.6×10⁻¹³, "~10³× atomic" | STANDS WITH CORRECTION | Atomic limit checked against 1607.01789 Eq. (8) in full text. But (W.13) is written with "∝" (measure not fixed) and still counted as a gap closure. The ratio is 10³–10⁴ [E] |
| 21 | J3 drag mass; "Si, Ge δM/M ≤ 2.7, 2.4×10⁻⁴ (upper bounds)" | STANDS WITH CORRECTION | J3 re-derived (atom: δM = N_e m_e via TRK). The per-nucleus "upper bound" is not derived: the diagonal of a PSD δM_{κκ′} is not bounded by N_e m_e/n |
| 22 | J8 third moment; link to WP0-v2 (4.7) | STANDS | Re-derived from second-order perturbation theory; the sign and the contact-density estimate (≈10⁻⁶) re-checked; IF-2 normalisation consistent |
| 23 | §11 "Contested corrections: none"; F1 resolution | STANDS | Total Im R_00 is independent of the in/out weight (C17a,b); the weights differ only where pairs are open |
| 24 | Consistency with WP0-v2 interfaces and NOTATION | STANDS | (M.13) = WP0-v2 (5.7); (M.15) = (4.9); (M.5) = (3.4) + (9.1); J8 agrees with (4.7) and its sign |

## 1. Amplitude, rate, thermal factor (focus: PAER amplitude, Pauli theorem, rate, η/(2q))
**Pauli theorem.** Path D: the phonon creates (c,k′) and a hole in occupied m at k+q, so E_i−E_I = ε_m − ε_c ∓ ω_Q. The Fock sign is −1. Amplitude:
−ρ_mv g_cm/(ε_m−ε_c∓ω_Q) = g_cm ρ_mv/(ε_c−ε_m±ω_Q), which is the A-form with d_{A,m} after the on-shell substitution of ω. C and B work the same way. At q = 0,
ρ(k,0) = δ, so A(m=v) = g_cv/(ε_c−ε_v±ω_Q) and B(m=c) = g_cv/(ε_v−ε_c∓ω_Q). They cancel identically, not only on shell (C11c is stronger than it claims).
**Rate.** (2π/V)·2·Σ_{kQ}N^{-1}|M|²δ = (4π/Ω)N^{-2}Σ_{kQ}|M|²δ, which is (M.3). Then ε₂ = (e²/2q²)(1−e^{−βω})S gives the 8π²α/(Ωq²) of (M.4).
**Thermal factor (correction).** Taken literally, the golden-rule S of (M.3), with weights (n+½±½), is exact for T ≪ E_g. Then ε₂ = (1−e^{−βω})(8π²α/Ωq²)⟨⟨…⟩⟩,
so the second "=" in (M.4) drops (1−e^{−βω}). L^{PA} as defined in (M.14) uses the same S-weights, so S = (2q²/e²)L^{PA}_{def}, and the "÷(1−e^{−βω})" (row 34, F7)
is off by exactly that factor. EPW 2302.08085 Eq. (64) shows the consistent choice: P = (n+(1+β)/2)f(1−f′) − (n+(1−β)/2)(1−f)f′ (absorption minus stimulated emission).
With P in place of (n+½±½) in (M.4) and (M.14), the division in (M.14) is exact. Numerically it is irrelevant (e^{−βE_g}), but as written (M.3), (M.4) and (W.4c) are mutually inconsistent.
**η/(2q).** For isotropic f: ∫d³v f δ(qv cosθ − q²/2m_χ − ω) = 2π∫v²dv f/(qv) = η/(2q). Then ∫d³q/(2π)³ = ∫q²dq/(2π²) gives the ρ_χσ̄/(4πm_χρ_Tμ²) of (M.6). Correct.

## 2. Window, Dyson convention, screening, systematic
**(M.8).** On shell, d_{A,m} = ω − ε_{m,k+q} + ε_{vk}, and d_{B,m} = ε_{ck′} − ε_{m,k+Q} − ω. For m empty and m occupied respectively, both are ≥ E_min(q) − ω.
The other two are ≥ E_g ∓ ω_Q. Correct.
**δ₀ inconsistency.** (M.9) requires δ₀ ≫ max(ω_Qν, Γ, T). In Si, ω_max ≈ 58–64 meV (TO/LO), so δ₀ = 0.1 eV gives a ratio of 1.6, not ≫ 1. Q_w ≈ 0.2 Å⁻¹, Q_min ≈ 0.015 Å⁻¹
and the "Si Γ/δ ≈ 0.02–0.6" map are all quoted at δ₀ = 0.1 eV. Either quote them at a δ₀ that satisfies (M.9) (e.g. 0.3 eV: Q_w ≈ 0.35 Å⁻¹ with m_l + m_hh ≈ 1.4 m_e),
or state the adiabatic error ω_Q/δ₀ ≈ 0.6 that goes with δ₀ = 0.1 eV (§M6 uses the same δ).
**(M.10).** ∫Γφ/(x²+Γ²/4) = 2πφ(0) + Γ fp∫φ/x² + Γ·O(Γ²)∫φ″ = 2πφ(0) + Γ fp + O(Γ²). The remainder is correct; there is no PV of 1/x². The double-counting statement
(δ part = Γ^{(1)} × branching, already in the ZPL) is correct.
**(M.13), ALDA overclaim.** In second-order TDDFT, v^{(2)}_eff(P) = f_Hxc δn^{(2)}(P) + ½ k_xc ⋆ [δn^{(1)}(q,ω) δn^{(1)}_{ph}(Q,ω_Q)], with k_xc = δ³E_xc/δn³.
The package's source N = [ρ̃,s^{(g)}] + [g,s^{(ρ̃)}] is explicitly the time-dependent Hartree (TDH) source. It has no k_xc term. So (M.13) is [D] at RPA. At ALDA one adds
Σ_G ρ_cv(k,P+G)(ε̃^{-1}k_xc[δn_q δn_Q])_G. Size [E]: comparable to δ_LF, i.e. ≲ 5–20% of the pair term. Also: (P,ω_f) is the final pair's own energy and momentum,
so ε̃(P,ω_f) is **always absorptive** (an open first-order channel at P). "(M.14) exact because ε̃^{-1}(q,ω) is non-absorptive" covers only the external line.
For the pair line the golden-rule form is exact only with the retarded (out-state) W^{scr}, by the same identity as C17a. "Exact for GaAs too" needs this stated.
**[0.5, 1.2].** 1 + δ_LF + δ_pair ± δ_ω with δ_LF ∈ [0.05, 0.2] and δ_pair ∈ [−0.5, −0.1] gives [0.53, 1.12]. So the bracket is just the interval sum of [E] numbers,
with δ_pair's sign assumed. §M7 and §10 tag that sign [C]. If the sign is open, the honest interim bracket is [0.5, 1.7]. Alternatively, keep [0.5, 1.2] and label it
"conditional on the [C] sign" in WP0-v2 (8.1). It is not a derived systematic.

## 3. Onset exponents, Si TA, Q_w (focus: p_on (3/4; Si TA 4), Q_w) — main defect
**Fixed q.** Correct. With Q = k′−k−q, ω_Q ≈ c|Q*| + cQ̂*·(δk′−δk) only tilts the paraboloids (shift O(m c²) ~ μeV), so p_on = 2.
**C23a assumes an isotropic c_ν.** E_th(q̂) = E_g^{ren} + c_ν(Q̂*)|Q*|, with Q* = K − q. Near q̂ ∥ K̂ with |q| > |K| (d = |q|−|K|), the transverse component of Q*
is |q|θ, so Q̂* turns by φ ≈ |q|θ/d. That is a large lever: |q|/d ≈ 5 at d = 0.2 Å⁻¹. Write c(φ) = c₀(1 + γφ²). Then
E_th − E_g = c₀d + (|q|/d)(c₀|K|/2 + γc₀|q|)θ² + O(θ⁴) ≈ c₀d + (|K|²/d)c₀(½ + γ)θ²,
so q̂ ∥ K̂ is a minimum only if γ > −½. C23a sets γ = 0.
**Si numbers.** Elastic constants C11 = 165.7, C12 = 63.9, C44 = 79.6 GPa. I diagonalised the Christoffel matrix for n = (cosφ, sinφ cosψ, sinφ sinψ).
The lowest (TA) branch gives c/c₀ = 0.9906 at φ = 0.1 (ψ = 0), so γ ≈ −0.94; at ψ = π/4, γ ≈ −0.76. Both are < −½. Hence **q̂ ∥ K̂ is a local maximum of the
Si TA threshold along every azimuth.** To leading order |Q*| ≈ d/cosφ. Minimising c(Q̂)/cosφ gives min = 0.966 c₀ at φ ≈ 0.41 rad, ψ = 0: four isolated off-axis minima
per K, in the {001} planes. For LA, c increases away from [100], so the on-axis LA minimum stands.
**Consequences.**
(i) The Si TA S̄ edge sits at ≈ E_g^{ren} + 0.966 c_TA d [E, continuum elasticity, d ≈ 0.2–0.4 Å⁻¹], not at E_g^{ren} + c_TA d. The shift is ≈ 0.3 meV at d = 0.2 Å⁻¹.
(ii) At the true minimum Q̂* is 23° off the valley axis. There ê_TA is not ⊥ k̂, so Ξ_u(Q̂·k̂)(k̂·ê) ≠ 0 and the vertex-zero argument does not apply. **p̄_on = 3.**
(iii) The vertex zero fails even on axis. The argument used only the conduction-valley Ξ_u. The hole path B has g_{mv}(k,Q) inside the Γ₂₅′ valence multiplet.
A TA wave along [100] polarised ⊥ gives shear strain ε_xy, which couples the multiplet through the deformation potential d (Si ≈ −4.8 eV), which is nonzero.
Symmetry check, little group C4v of the [100] axis: c is Δ₁, the y,z hole components are Δ₅, the TA phonon is Δ₅, and e^{iq·r} with q ∥ x is Δ₁.
Δ₁ ⊗ Δ₅ ⊗ Δ₅ ∋ Δ₁, so the on-axis amplitude is **symmetry-allowed**. Interband Δ₁–Δ₅ couplings g_cm in path A are allowed for the same reason.
So "M̃ vanishes on q̂ ∥ K̂" is false even before the anisotropy point.
(iv) The window argument also used the long-wave deformation picture at Q* = d ≥ Q_w. But on shell in the window, (M.15) does not apply ("Off shell because the window
forbids |Q| < Q_min"). Only the intraband g_cc(Q) is deformation-like; the full M̃ is not.
**Required corrections:** in §M3 (ii), §3 L8, IF-5 and closing-table row 64, Si TA becomes p̄_on = 3 at E_g^{ren} + min_{q̂}c_TA(Q̂*)|Q*| (≈ 0.97 c_TA d).
"4 on a vertex zero" stays only as a non-generic case. Add c_ν(Q̂) anisotropy to C23 (a test with γ < −½ must move the minimum off axis). WP6 must not adopt "Si TA 4".
**Q_w.** E_min(q) = E_g + d²/(2(m_c+m_h)) for q̂ ∥ K̂. Window onset c d ≤ d²/2M − δ₀ gives d ≳ (2Mδ₀)^{1/2} + O(c M). Correct, given the δ₀ caveat in §2.

## 4. Migdal unification, 4α, J3, J8
**(W.5) → KKL.** U U* S^{ee} = Z²e⁴/p⁴ · 2p²/e² · Im(−ε^{-1}) = 2Z²e²Im/p². Times 1/(2π) this gives e²/π = 4α. So S^X = S^{GS} × 4α∫d³p(2π)^{-3}Z²(q·p)²Im/(M²ω⁴p²),
which is KKL Eq. (6) with v_N = q/M. It is consistent with J4 (∫dω/2π S = 𝓃_κ), so the factor is dP/dω and not 2π·dP/dω. Correct.
**L7a.** ⟨n|∇V|0⟩ = i(E₀−E_n)⟨n|p|0⟩ = m(E_n−E₀)²⟨n|r|0⟩, which gives the amplitude (m_e q/M)·⟨n|Σr|0⟩. Correct.
**L7c correction size.** The relative correction 2v_N·p/ω_e is odd and vanishes for any time-reversal-even ELF (inversion is not needed). But O(ω_ph²/ω_e²) = (0.06/5)² ≈ 1.4×10⁻⁴,
and p²/(2Mω_e) ≈ 10⁻⁴ for the quoted (p = 5 keV, ω_e = 5 eV), which enters ω′⁻⁴ as ≈ 4×10⁻⁴. So "≈ 10⁻⁵" should read "≲ 10⁻³". The conclusion (EFT = impulse) is unchanged.
**J3.** E^{Mig}_1 = (q²/M²)Σ|∂V_{a0}|²/ω_a³ = q·δM·q/(2M²). Atom: |∂V_{a0}|² = m²ω_a⁴|r_{a0}|², and TRK gives δM = N_e m_e. Correct.
"Si δM/M ≤ 14m_e/M (upper bound)": δM_{κκ′} is PSD with Σ_{κκ′}δM_{κκ′} = N_e m_e per cell (uniform drag). That bounds the trace, but not a diagonal element against the per-atom share.
Downgrade to [E] (the core part ≈ 10 m_e is rigid, so the estimate is plausible).
**J8.** Second-order perturbation theory gives ∂²E₀ = ⟨∂²V⟩ − 2Σ|∂V_{a0}|²/ω_a, hence E^{Mig}_3 = (q²/M²)Σ|∂V|²/ω_a = (q²/2M²)(⟨∂²V⟩ − ∂²E₀). V_NN cancels.
∇²_R V_eN = 4πZe²_G δ, cubic (T_d) isotropy gives ⟨∂²V_eN⟩ = (4π/3)Ze²_G 𝓃_e(R) = (1/3)Ze²_{HL}𝓃_e, and the ratio to Mω̄² is ≈ 2×10⁻⁶ (Si 1s). The sign of
𝓜³_eκ(q→0) agrees with WP0-v2 (4.7) (V_eN = −U_κ). The IF-2 identity 𝔨₃^{(eN)} = −(m_e/M)𝓜³/(2𝓃) follows. Correct.

## 5. Literature claims (rubric c)
- **2603.13052 (3.11) +K: CONFIRMED.** Full text (3.11) and (4.1): "S(q − k_e + K, …)" with Z(|k_e+K|) and q·(k_e+K). 2210.06490 (3.8) and (5.x): S(q − k_e − K, …).
  S is not G-periodic (Debye–Waller depends on |q′+G|), so this is a real inconsistency, not a relabelling.
- **2603.13052 (4.7): CONFIRMED (dimension), the package's diagnosis needs correcting.** In natural units α q² d³k/(ω⁴m_N) is dimensionless, but dP/dω needs E^{-1}.
  The package overlooked that (4.6) reads dR/dω = (n_χN_T/(**m_N**M_T))∫dq∫d³v v f (dσ/dq)(dP/dω), with one more 1/m_N than a rate needs.
  The (4.6)×(4.7) product carries m_N^{-2} and is dimensionally consistent. With (4.8) dσ/dq = qσ̄/(μ²v²), the product is 2αq³σ̄/(3μ²v²m_N²ω⁴), which is KKL × the standard
  qσ̄/(2μ²v²), as the package says. Correct statement: m_N is misplaced between (4.6) and (4.7). (4.7) alone, as an "ionization probability", is dimensionally wrong.
  After moving the m_N it is ½ of KKL; the 2× in (4.8) compensates [E: σ̄ normalisation in their App. A not re-derived]. Fix the C3a/C3b docstrings and §2 L7c text accordingly.
- **2210.06490 fn. 3: CONFIRMED.** The footnote: "Here we take the most conservative value, ω ∼ ω_g". The package's v_N·p/ω_e argument is KKL's and is sound. The "practically challenging" quote (p. 9) is verified.
- **1604.02394 Eq. (24): CONFIRMED.** Verbatim: "the Dirac delta function does not contain the phonon energy … the WL theory provides the adiabatic limit of the HBB theory".
  Eqs. (5)–(8): deterministic, O(σ⁴) error as N → ∞. The mechanism is sign alternation of frequency-adjacent modes ((−1)^{ν−1}), not "antithetic pairing" (that is §IV's ±S averaging).
  The package's "defect" is the paper's own adiabatic statement applied at T → 0. It is not a claim that the paper is wrong; label it so.
- **EPW 2302.08085 (60)–(64): CONFIRMED.** Text: "restricted to the manifold of valence and conduction bands included in the Wannierization"; η "to avoid singular denominators …
  a more general theory … is under development". 2πe²/(ε₀Ω) × 2 spin gives 8π²α/(Ωω²) (Ω = cell volume, ∫dk/Ω_BZ normalised). Note Eq. (64): see §1.
- **1607.01789 Eq. (8): quote CONFIRMED** (Gaussian units, α(ω) = −(α/m_eω²)f(ω)). (W.13) reduces to it: (4α/3πω)(E_R/m_N)|f|² with E_R = q²/2M gives (2α/3πω)q²|f|²/M².

## 6. Bremsstrahlung and the GaAs ~10³ estimate
(W.13) is written "∝" with "(2α/(3πω_γ))n_r|Z*·q|²/M²". The polarisation/direction factor is fixed, but the measure d³Γ/(dω_γdω_phd³q) has no stated 1/(2π)⁴ bookkeeping.
A gap "closed by formula plus specification" (DONE) needs the equality: dΓ = ∫d³q/(2π)³∫dω_ph 𝔇 S^{GS}(q,ω_ph) (2α n_r/(3πω_γ))|Z*(ω_γ)·q|²/M² dω_γ
(energy δ(ω_q − ω_ph − ω_γ)). The n_r factor (quantised E_mac with 1/ε normalisation × n_r³ density of states) is correct for coupling to the Born charge Z*.
Cross-check of the estimate: v_N = q/M ≈ 0.2 MeV/65 GeV ≈ 3×10⁻⁶ gives P ≈ (2α/3π)(3.6)(4.4)v_N² ln 14 ≈ 3–6×10⁻¹³, consistent with 2.6×10⁻¹³.
Atom (Ga, α_pol ≈ 50 a.u.): f(1 eV) ≈ ω²α_pol ≈ 0.07, and ∫|f|²dω/ω over 0.1–1.4 eV ≈ 4×10⁻³, against n_rZ*² ln 14 ≈ 42. Ratio ≈ 10⁴. "~10³" should read 10³–10⁴ [E].
Validity needs E_R ≫ ω_ph (impulse, q ≳ 125 keV in GaAs) as well as ω_γ ≫ ω_ph. Add that hypothesis.

## 7. Soft limit and C7 (focus)
I re-derived (M.15). ASR gives g_cm(k+q,0)/d_{A,m} → −𝔄_cm and ρ_cm g_mv/d_{B,m} → +ρ_cm𝔄_mv. Their sum is [ρ,𝔄]_cv + (𝔄_cc−𝔄_vv)ρ_cv = iℓê·(q − p_cc + p_vv)ρ_cv,
using [e^{iq·r}, p] = −q e^{iq·r}. The intraband terms (Q̂·v_n)(p_nn·ê)/(Q̂·v_n ± c) = p_nn·ê ∓ c p_nn·ê/(…) cancel the p terms, which gives (M.15). Correct.
The O(|Q|^{1/2}) remainder (ℓ ∝ Q^{-1/2}) is correct. The IR counting Q^{d−2} (T = 0) and Q^{d−3} (T > 0) is correct. C7a–e is a sufficient check set.
**Caveat (see §3 (iv)):** (M.15) is an off-shell control. It must not be used for on-shell window statements such as vertex zeros.

## 8. Rubric (b), (d), (e), (f) summary
(b) L7a–d, L8, L9, L9b, L12: the source formulas are quoted correctly where I checked full text (2210.06490 (3.8) −K; 1604.02394 (24); 1607.01789 (8); EPW (61)–(63)).
The chains are valid. Corrections: L8 onset (Si TA p̄ = 3, §3); L7c correction size (§4); L12 wording. (d) Consistent with WP0-v2 (3.4), (4.7), (4.9), (5.7), (6.3), (9.1),
and with NOTATION v4 symbols as far as checked. (e) G2 and G6 closures are sufficient (formula, routes, convergence parameters). G5 is honestly left as a gap.
Bremsstrahlung is not closed until the ∝ in (W.13) is replaced by the equality. (f) §11 is correct.

## 9. Checks script remarks
C3a/C3b encode the incomplete (4.7) diagnosis (they ignore (4.6)'s 1/m_N). C19/C23 are generic calculus and cannot detect the c_ν(Q̂) defect.
C14b is close to tautological (it expands 1/(1−t x) − t x to O(t)); C14a carries the content. C9's "upper bound" labels for δM/M are not derived (§4).
No check covers the thermal-factor consistency of (M.3)/(M.4)/(M.14) or the TDH-versus-ALDA source of (M.13).

## Required actions (blocking marked *)
1*. §M3 (ii), §3 L8, IF-5, row 64: Si TA S̄ edge p̄_on = 3 at ≈ E_g^{ren} + 0.97 c_TA d. C23a: minimise over q̂ including c_ν(Q̂). WP6 relay to be corrected.
2. (M.13): tag [D, RPA/TDH]; add the ALDA k_xc source or drop "ALDA"; state the retarded W(P,ω_f) (always open).
3. (M.4), (M.14), (W.4c): use EPW's P-factor or drop the ÷(1−e^{−βω}); one consistent thermal convention.
4. [0.5, 1.2]: mark it conditional on the [C] sign of δ_pair, or widen to [0.5, 1.7].
5. Numerical examples (Q_w, Q_min, Γ/δ): use a δ₀ that satisfies (M.9), or carry ω_Q/δ₀ ≈ 0.6.
6. 2603.13052: "m_N misplaced between (4.6) and (4.7)"; fix C3 docstrings.
7. L7c correction "≲ 10⁻³"; J3 "upper bounds" → [E]; ZG "sign alternation"; (W.13) equality and impulse hypothesis; GaAs ratio 10³–10⁴.
