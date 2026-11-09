# R7 / REF-WP3-A: hostile referee of returns/R6/WP3-v2.md (isolated)

Read: WP3-v2.md (all 626 lines), code/WP3-v2/checks.py (run: 66/66 PASS, about 10 s), CONVENTIONS, NOTATION (spot checks), CONTROLS, DONE,
LIMITS, WP0-v2 (only the interfaces (4.7), (4.9), (5.7), (6.3), (9.1)). Full text was fetched and read for this round, then deleted:
2603.13052, 1604.02394, 2210.06490, 2302.08085, 1608.01994. No simulations were run; the sympy and arithmetic checks are inline below.

## Verdict table
| # | Claim (location) | Verdict | One-line reason |
|---|---|---|---|
| V1 | Four paths, Pauli/exchange theorem, unrestricted-m amplitude (M.1)–(M.2) (§M2) | STANDS | Re-derived paths C and D by hand (sign, denominators, on shell); matches C11a–d |
| V2 | Rate (M.3)–(M.7), η/(2q), \|f_crys\|² dictionary | STANDS WITH CORRECTION | The prefactors are right, but the thermal factor is counted twice between (M.3)/(M.4) and (M.14)/(W.4c) (§1) |
| V3 | Window (M.8)–(M.9); no sideband–ZPL interference | STANDS | All four per-path bounds re-derived |
| V4 | Dyson convention outside the window, (M.10), Hadamard fp, DC | STANDS | The C13 series was checked; the expansion is analytic in Γ (no Γ log Γ term) |
| V5 | f-sum, aggregate compensation (§M5, J5) | STANDS | Under hypothesis (L); the per-diagram claim was correctly withdrawn to [C] |
| V6 | Screened M̃ (M.13)–(M.14), four Coulomb classes, frame theorem | STANDS (at RPA/ALDA) | The C15 limit and the commutator c_𝔄 = iℓ_Qê·q were verified; the topology argument is accepted, not re-derived |
| V7 | Interim factor [0.5, 1.2] on L^{PA} | STANDS WITH CORRECTION | It is not the envelope of the stated components unless two undeclared or conjectured signs are assumed (§2) |
| V8 | Soft limit (M.15), Ward identity (M.16), IR, C7a–e | STANDS | Interband commutator, intraband 0/0 terms and the (M.16) algebra re-derived (§3) |
| V9 | Fixed-q onset p_on = 2 / 3 / ½ | STANDS WITH CORRECTION | The threshold is min over (k,k′) of ε_c − ε_v + ω_{k′−k−q}, which lies below E_g + ω_{Q*} by O(m*c_ν²) (§4a) |
| V10 | Angle-averaged rule p̄ = p+1 / p+2; the minimum sits at q̂ ∥ K̂ | STANDS WITH CORRECTION | Needs c_ν(Q̂) stationary at Q̂ ∥ K̂ (true on symmetry axes); with generic anisotropy the minimum moves off axis (§4b) |
| V11 | **Si TA edge p̄_on = 4 (TA vertex zero on the valley axis); LA kink p̄ = 3** | **FALLS** | By C4v selection rules TA is allowed on the axis and LA is forbidden. The package's own argument is ∝ ρ_cv, which vanishes on the axis for every branch (§4c) |
| V12 | Edge-shell criterion Q_w = (2(m_c+m_h)δ₀)^{1/2} ≈ 0.2 Å⁻¹ | STANDS WITH CORRECTION | The value is right (0.19 Å⁻¹). It removes the whole |q| shell, where only a polar cap fails the window; linear c_TA·d is used at d ≥ 0.2 Å⁻¹ (§4d) |
| V13 | Migdal unification L7a–d as truncations of (W.5); 4α | STANDS | The C2b algebra was re-derived, including the sign of ∇_RV (attractive −U); the L7a TRK step was checked |
| V14 | L7c leading correction ~10⁻⁵; 2210.06490 fn. 3 "therefore conservative" | STANDS WITH CORRECTION | Under the stated free-recoil hypothesis the even term p²/(Mω_e) ≈ 2×10⁻⁴ dominates. Fn. 3 already calls itself "the most conservative value" (§5) |
| V15 | 2603.13052 Eq. (4.7) misprint, and the repair "m_N → m_N², rate consistent" | Misprint CONFIRMED; repair REFUTED | Their Eq. (4.6) carries the compensating 1/m_N. The package's repair leaves a spurious 1/m_N in the rate (§6) |
| V16 | 2603.13052 Eq. (3.11) sign +K → −K; Eq. (4.8) = 2× standard | CONFIRMED; UNRESOLVED as an error | Momentum conservation needs −K. Eq. (4.8) depends on their σ̄ normalisation (§6) |
| V17 | ZG energy-δ defect vs 1604.02394 Eq. (24); (W.11)–(W.12) | STANDS WITH CORRECTION | Quote CONFIRMED and the authors acknowledge the defect. "Antithetic sign pairing (Eqs. (7)–(8)), exact to O(σ⁴)" misattributes the mechanism and the order (§7) |
| V18 | Crystal NR bremsstrahlung (W.13); GaAs ~10³× atomic, 2.6×10⁻¹³ | STANDS [E] | Re-estimated ratio ≈ 3×10³ at 1 eV (∝ ω⁻⁴); probability reproduced within ×3 (§8) |
| V19 | J8: E^{Mig}_3, KK form, link to WP0-v2 (4.7), ratio 10⁻⁶ | STANDS | Consistent with WP0-v2 (4.7) contact form; 10⁻⁶ reproduced; IF-2 normalisation is an honest exact gap |
| V20 | Contested corrections (§11): totals are weight-independent (F1) | STANDS | Both factorisations of R − R† derived (§9) |
| V21 | L9 vs EPW 2302.08085 Eqs. (60)–(64), Noffsinger; "under development"; Wannier-only sums | CONFIRMED | Prefactor 2π·(e²/ε₀)/(Ωω²) → 8π²α/(Ωω²); both quotes verbatim (§10) |
| V22 | L9b(b): 1608.01994 rate "overestimated, O(1) within ~0.1 eV; E_g rises by ≈ 50 meV" | REFUTED in size | 1608.01994 uses the 77 K data near the edge. The 77 K → 0 shift is ≈ 4 meV and n_TA(77 K) ≈ 0.07 (§10) |
| V23 | Notation: "no deviations" (§16) | STANDS WITH CORRECTION | K, E_th collide with NOTATION; Q_w, d(|q|), p̄_on, θ are undeclared (§11) |
| V24 | Gap closures G2, G5, G6 and bremsstrahlung (§8 of the package) | STANDS | Each has a formula, a route, inputs, convergence parameters and a cost. G5 is stated as an exact remaining gap |

---
## 1. Thermal factor counted twice (V2)
CONVENTIONS §6 gives proper ε₂ = (e²/2q²)(1 − e^{−βω})S^{prop}. (M.3) defines S^{PA} = (4π/Ω)⟨⟨Σ(n+½±½)|M|²δ⟩⟩, which is the golden-rule
structure factor: emission weight n+1, absorption weight n, no stimulated subtraction. Then:
- (M.4) writes ε₂^{PA} = (e²/2q²)(1 − e^{−βω})S^{PA} = (8π²α/Ωq²)⟨⟨…⟩⟩. The second equality drops (1 − e^{−βω}), so it holds only to O(e^{−βω}).
- (M.14) defines L^{PA} = (8π²α/Ωq²)⟨⟨Σ(n+½±½)|M̃|²δ⟩⟩, also without the factor, and then sets S^{X+} = (2q²/e²)L^{PA}/(1 − e^{−βω}).
- (W.4c) asserts S^{X+} = (4π/Ω)⟨⟨…⟩⟩ = (2q²/e²)L^{PA}/(1 − e^{−βω}). Since (2q²/4πα)(8π²α/Ωq²) = 4π/Ω, this reads X = X/(1 − e^{−βω}), which is false at T > 0.

EPW Eq. (64) shows the proper object: P = (n + (1+β)/2)f_n(1 − f_m) − (n + (1−β)/2)(1 − f_n)f_m. This equals (1 − e^{−βω})(n+½±½) only after the
electron factors are included. **Correction:** either define L^{PA} with the factor (1 − e^{−βω}), i.e. (8π²α/Ωq²)(1 − e^{−βω})⟨⟨…⟩⟩, or state
S^{X+} = (4π/Ω)⟨⟨…⟩⟩ directly and drop the "÷(1 − e^{−βω})" of F7/C21. The error is numerically nil at T ≪ E_g (e^{−E_g/T}). As written, though,
the F7 "correction" is itself a double count, and C21 tests only the β → ∞ limit, which cannot detect it.

Everything else in V2 checks out:
- 𝒢 = (2π/q)∫v f dv = η/(2q).
- (M.6) prefactor: π·4π/(2·8π³) = 1/(4π).
- Equating (M.6) with 1509.01598 Eq. (17) per unit mass gives |f_crys|² = Ωq³S̄/(4παm_e²).
- With ∫d³q′ = Σ_{G′}∫_BZ d³k′ and S^{(1)} = 4π∫d³k/(2π)³…, I recover (2π²q/(αm_e²Ω))∫∫(Ωd³k/(2π)³)(Ωd³k′/(2π)³)Σδ(q − |k′ − k + G′|)|ρ|²δ.

## 2. The [0.5, 1.2] interval (V7)
The stated components are δ_ω = ±(1–2)%, δ_LF = 5–20% with no sign given, δ_pair = −(10–50)% with sign [C], and δ_ion ≲ 10⁻⁴.
- Multiplicative envelope with δ_LF of either sign and δ_pair ≤ 0: [0.8·0.5·0.98, 1.2·1.0·1.02] = [0.39, 1.22].
- The quoted [0.5, 1.2] needs δ_LF ≥ 0, which is never stated.
- If the conjectured sign of δ_pair fails (|δ_pair| ≤ 50% either way), the upper end is ≈ 1.8.

**Correction:** state the composition rule and the two sign hypotheses next to the interval, and tag the interval [E/C]. Otherwise widen it to
[0.4, 1.2], or to [0.4, 1.8] if the δ_pair sign is not adopted. WP6 imports this as an A-type nuisance, so the bound matters.

## 3. Soft limit and Ward identity, re-derived (V8)
- **Interband terms.** At Q → 0, g_mn(k,0) = (ε_n − ε_m)𝔄_mn. The m ≠ c terms of A give −Σ_{m≠c}𝔄_cmρ_mv and the m ≠ v terms of B give
  +Σ_{m≠v}ρ_cm𝔄_mv, so together they give [ρ,𝔄]_cv + (𝔄_cc − 𝔄_vv)ρ_cv. Using [e^{iq·r}, p] = −q e^{iq·r}, this equals iℓ_Qê·(q − p_cc + p_vv)ρ_cv, as the
  package states.
- **Intraband 0/0 terms.** They give ±iℓ_QQ̂·Ξ^n·ê/(Q̂·v^g_n ± c_ν). With Ξ^n = D^n + v^g_n⊗p_nn, the identity (Q̂·v)(ê·p)/(Q̂·v ± c) = ê·p ∓ c(ê·p)/(Q̂·v ± c)
  turns this into (M.15).
- **Ward identity (M.16).** For g → g + i s(ε_n − ε_m ∓ ω_Q), path A shifts by −i s_cmρ_mv and path B by +iρ_cm s_mv. The total shift is
  i[ρ,s]_cv = −i⟨[s, e^{iq·r}]⟩, which gives (M.16) with the stated sign, exactly and for all Q on shell.
- **Remainder.** The O(|Q|^{1/2}) remainder is ℓ_Q·O(|Q|), which is consistent.

## 4. Onset exponents and the edge-shell criterion (V9–V12)
**(a) Fixed q.** At fixed q the threshold is min over (k,k′) of F = ε_c(k′) − ε_v(k) + ω_ν(k′ − k − q), not E_g + ω_{Q*}. Near a non-Γ Q*, the gradient
∇ω_ν shifts the minimum by about −½(m_c + m_h)|∇_Qω|² ~ m*c_ν² ≈ 0.1–1 meV. Since F has a 6-dimensional quadratic minimum, p_on = 2 is robust;
only the threshold label moves. The package should write the threshold as min F, or quote the shift.

**(b) Angle average.** Write Q* = K − q with q at angle θ to K̂. Then the component of Q* parallel to K̂ is d (to O(θ²)) and the perpendicular
component is |q|θ. So the direction Q̂* rotates by about |q|θ/d, which is O(1) once θ ~ d/|q|. Then E_th(θ,φ) = E_g + c_ν(Q̂*)|Q*| picks up a linear term
|q|θ ∂_φc_ν, unless c_ν(Q̂) is stationary at K̂. C23a assumes isotropic c_ν. The rule p̄ = p+1 survives, because any isolated quadratic interior
minimum gives it, but "the minimum is at q̂ ∥ K̂" needs this hypothesis. In Si, Q̂* ∥ [100] is a C4v axis, so the hypothesis holds there. It fails
for Umklapp K = k_c + G that are off the symmetry axes.

**(c) Si TA vertex zero: FALLS.** Hypotheses: no SOC (P4), hole at Γ25′, electron at the Δ1 minimum k_c ∥ x, and q ∥ Q* ∥ x on the minimising
direction. All four wavevectors are invariant under C4v(x), and total momentum is conserved, so the nonsymmorphic phases cancel. Then:
- The operator e^{iq·r} transforms as Δ1.
- Γ25′ decomposes along Δ as Δ2′ ⊕ Δ5.
- The phonon representations along Δ are LA Δ1, TA Δ5, LO Δ2′, TO Δ5 (standard compatibility tables; cited from memory, so [UNVERIFIED] this round).
- The amplitude ⟨Δ1(c); ph|n_e(q)H_ep|v⟩ is nonzero only if Δ1 ⊂ Δ1⊗Γ_ph⊗Γ_v, i.e. Γ_ph = Γ_v.
- Hence **TA (Δ5) is allowed via the Δ5 holes, LO (Δ2′) via the Δ2′ hole, TO is allowed, and LA (Δ1) is forbidden.**

The package's argument is internally inconsistent. It uses only the conduction intravalley term Ξ_u(Q̂·k̂)(k̂·ê), which multiplies ρ_cv(k,q). But
ρ_cv(Γ, q ∥ x) between Δ1 and Γ25′ vanishes for the same symmetry reason. This is the "symmetry-forbidden, q ∥ [100]" zero-phonon exciton that the
package itself cites in §M9. So the soft-limit form vanishes on the axis for every branch and cannot single out TA. The surviving on-axis TA amplitude
comes from interband paths: path A through m ∈ Δ5 at k+q, with g_{c m} via a Δ5 phonon. It vanishes only as Q* → 0 (ASR) and is nonzero at d ≥ Q_w.

**Correct statement [D, group theory, SOC = 0]:** the Si S̄ edge has p̄_on = 3 at E_g^{ren} + ω_TA(Q*_min). The LA kink has p̄ = 4, because the LA
amplitude is ∝ θ off the axis. TO is p̄ = 3, and LO is p̄ = 3, allowed via Δ2′. With SOC (Γ8⁺ → Δ6 ⊕ Δ7, Δ1 → Δ6) the LA zero is lifted at O(Δ_so/δ).
§M3 (ii), §3 (L8 entry), §10 and IF-5 must be amended, and WP6's replacement bullets ("Si TA edge: 4") must not be adopted.

**(d) Q_w.** The window condition at q̂ ∥ K̂ is d²/2M − ω_TA(d) ≥ δ₀, with M = m_c + m_h. This gives d ≥ Mc + (M²c² + 2Mδ₀)^{1/2}, where the Mc term is about
0.007 Å⁻¹ (negligible). For M = 1.4m_e and δ₀ = 0.1 eV, Q_w = 0.19 Å⁻¹, as quoted.

Two corrections:
- (i) For | |q| − |K| | < Q_w, only a polar cap of directions (angle ≲ Q_w/|q|) fails the window. The rest of the |q| sphere is in window. Assigning the
  whole shell to the edge shell discards in-window PAER. S̄ on such shells is then a mixed window-plus-DC object, and that must be stated.
- (ii) At d ≥ 0.2 Å⁻¹ the Si TA branch is already sub-linear. Use ω_TA(Q*_min), as §3 does, not c_TA·d.

## 5. Migdal unification and the L7c correction (V13, V14)
**4α and the ∇_RV sign.** With electron–nucleus potential energy −U, the Fourier expansion gives ∇_RV = V^{-1}Σ_p(ip)U(p)e^{−ip·R}n_e(p); the sign
is correct, and (W.6) interference signs are safe. Next, Σ_a⟨…⟩δ(ω − E_a) = (V/2π)S, so dP/dω = (1/2π)∫d³p/(2π)³(q·p)²U²S^{ee}/(M²ω⁴). With
S^{ee} = (2p²/e²)L and U = Ze²/p², this is 4αZ²(q·p)²L/(M²ω⁴p²), which is KKL Eq. (6).

**L7a.** [H,[H,r]] = ∇V/m_e. Since Σ_i∇_iV_ee = 0, ⟨n|Σ∇_iV|0⟩ = m_e(E_n − E₀)²⟨n|Σr|0⟩. **J3:** 2m_e²ΣE|x|² = N_em_e (TRK).

**L7c.** The package's own bracket is [1/(ω′ − v_N·p) − 1/ω′] with ω′ = ω_e + p²/2M, so the leading term v_N·p/ω′² differs from the EFT value
v_N·p/ω_e² by a factor (1 − p²/(Mω_e)) in amplitude. For Si with p = 5 keV and ω_e = 5 eV, the rate shifts by 2p²/(Mω_e) ≈ 3.8×10⁻⁴. This is even in p
and survives the angular average. So under the stated "[D free recoil]" the first surviving term is about 4×10⁻⁴, not 10⁻⁵. For bound nuclei it is
replaced by O(ω_ph/ω_e) terms, whose cancellation the package does not show. The conclusion (negligible) stands; the order quoted is wrong.

**2210.06490 fn. 3 (FT).** The footnote states q ~ √(2m_Nω_g) with ω_g ≃ 1.2 / 0.7 eV, i.e. m_χ ≳ 250 / 320 MeV, and adds "Here we take the most conservative
value, ω ∼ ω_g". The package's 242 / 301 keV come from 1.12 / 0.67 eV, which is a misquote of the inputs. Its "therefore conservative" adds nothing the
footnote does not already say. Re-word this as agreement, not as a correction.

## 6. 2603.13052 (FT) (V15, V16)
Printed formulas:
- Eq. (4.6): dR/dω = (n_χN_T/(m_N M_T))∫dq∫d³v v f_χ (dσ/dq)(dP/dω).
- Eq. (4.7): dP/dω = (2αq²/(3ω⁴m_N))∫d³k_e/(2π)³Σ_K Z²Im(−ε^{-1}_{KK}).
- Eq. (4.8): dσ/dq = (q/(μ_χn²v²))Σσ̄F.
- An unnumbered intermediate step: dR/dE = (n_χN_T/M_T)∫dω (2α/(3(ω²m_Nμ_χn)²))∫d³v (f_χ/v)∫q³dq Σσ̄F ∫d³k Z²Im(−ε^{-1}) S(q,E).

Sympy (inline, exact):
- (4.6)×(4.7)×(4.8) equals their intermediate step (ratio 1).
- Their intermediate step equals KKL dP/dω (4αq²/(3m_N²ω⁴)) combined with the standard dσ/dq = qσ/(2μ²v²) (ratio 1).
- **The package's repair** (m_N → m_N² in (4.7), keeping (4.6)) gives KKL × 1/m_N.

Verdicts:
- (4.7) is dimensionless as printed, so the misprint is **CONFIRMED**.
- The diagnosis is incomplete. One m_N was moved from (4.7) into the prefactor of (4.6); N_T/M_T is already 1/m_N per nucleus. The correct repair
  is to move 1/m_N from (4.6) into (4.7). After that, the ½ in (4.7) and the 2× in (4.8) compensate. **The package's "with m_N → m_N² … the rate is
  consistent" is REFUTED** (C3b tests only the dP × dσ product, not the (4.6) prefactor).
- **Eq. (3.11)** prints S(q − k_e + K, …), and so do the appendix and the text ("q′ → q − k_e + K"). The numerator q·(k_e + K)Z(|k_e + K|) fixes the
  Coulomb-line momentum at k_e + K, so the nuclear recoil is q − k_e − K, as in 2210.06490 Eq. (3.8). Sign misprint **CONFIRMED**. It has no
  numerical effect in their free-ion, soft-limit evaluation.
- **Eq. (4.8)** "2× standard" is correct as printed. Whether it is an error depends on their σ̄ and F_ij normalisation, which I did not trace:
  **UNRESOLVED** as an error, but consistent with the package's [E] tag.

## 7. ZG (V17)
**Quote CONFIRMED.** 1604.02394 Eq. (24) is (2n+1)δ(ε_c − ε_v − ħω), and the text says "the Dirac delta function does not contain the phonon
energy… the WL theory provides the adiabatic limit of the HBB theory". (W.12) Δ𝓜₁ = ω_Q|M|² is verified (C6a). The defect is therefore
acknowledged by the authors. The URF content is the T = 0 onset shift and the hybrid prescription, and that stands.

**Correction.** The package writes "exact to O(σ⁴) as N → ∞ by antithetic sign pairing (Eqs. (7)–(8))". In the paper:
- Eqs. (7)–(9) obtain the O(σ⁴) agreement from the alternating signs (−1)^{ν−1} over frequency-ordered, effectively degenerate modes.
- "Antithetic pair" denotes S and −S, which is Eq. (12) and removes the odd orders.
- The paper then claims the limit to all orders, Eq. (10), by a heuristic argument.

So the paper should be cited as "alternating-sign cancellation, Eqs. (7)–(10); antithetic pair Eq. (12) at finite N". "Deterministic one-configuration
quadrature" stands.

## 8. Bremsstrahlung (V18) [E]
- Per-photon ratio, crystal over atom: n_rZ*²/|f_atom(ω)|². With α_pol(Ga) ≈ 8 Å³ = 54 a.u., |f| = ω²α_pol ≈ 0.073 at 1 eV, so the ratio ≈ 3.0×10³ (∝ ω⁻⁴).
- Over 0.1–1.4 eV the crystal spectrum is ∝ dω/ω and the atomic one ∝ ω³dω, so the band-integrated ratio is ~10⁴.
- P ≈ (2α/3π)n_rZ*²v_N²ln 14 with q ≈ 77 keV gives about 10⁻¹³ at 100 MeV.
- "~10³" is the right order at 1 eV; quote the ω dependence.
- The hypotheses (ω_γ ≫ ω_TO, transverse Born charge, emission ∝ n_r for a macroscopic dipole) are adequate. Relevance stays [C].

## 9. Contested corrections (V20)
R = (1 − R⁰f)^{-1}R⁰ = R⁰(1 − fR⁰)^{-1}. Hence R − R† = (1 + Rf)(R⁰ − R⁰†)(1 + fR†) = (1 + R†f)(R⁰ − R⁰†)(1 + fR). Taking the 00 element of each gives
the in-state and out-state totals respectively. Both are exact for any Hermitian f and any ρ, which is the content of C17a,b. Pair-resolved weights
differ (C17d). The §11 resolution is right.

## 10. Other published-paper claims
**EPW 2302.08085 (FT): CONFIRMED.**
- Eq. (63): Im ε = 2(πe²/(ε₀Ωω²))Σ∫∫|e·(S1 + S2)|²Pδ, giving 8π²α/(Ωω²).
- S1 and S2 equal −A₁^v and −A₂^v on shell; a common sign is irrelevant in |·|².
- §computational: "restricted to the manifold … included in the Wannierization" and "a more general theory … is under development" are verbatim.
- C1 and L9 stand.

**1608.01994 (FT): REFUTED in magnitude.** The paper says: "Anticipating the low operating temperatures … we use the T = 77 K data where available.
(The difference between absorption at temperatures of 77 K and 4.2 K is even smaller.)" Near the Si edge the 77 K data are used. Consequences:
- Varshni gives E_g(0) − E_g(77 K) ≈ 4 meV.
- n_TA(77 K) ≈ 0.07, and n_TO is negligible.
- The overestimate is therefore O(1) only within ≈ ω_TA + few meV ≈ 20–25 meV of the edge.
- The "≈ 50 meV" rise and "O(1) within ~0.1 eV" apply only to 300 K data.

The T-transfer formula of L9b(b) itself stands.

## 11. Notation (V23)
NOTATION reserves **K** for the kinematic-regime label "inside τ (only)", but §M3 uses K ≡ k_c − k_v + G (source quotes are exempt). **E_th** is
NOTATION's detection or kinematic threshold, but §M3 uses it as the angle-dependent PAER threshold. **Q_w, d(|q|), p̄_on and θ** are new and are
missing from §16 "Introduced here", which nonetheless claims "no deviations". **Fix:** rename (e.g. K_pk, E^{PA}_{th}(q̂)) and declare them.

## 12. Items that stand without comment
- Rubric (a): DERIVED steps carry hypotheses.
- Window bounds (M.8): d_A (m occupied) ≥ E_g ± ω_Q; d_B (m empty) ≥ E_g ± ω_Q; d_A (m empty) and d_B (m occupied) ≥ E_min(q) − ω.
- (M.12) expansion, with the sign ∓ω_Q[gρ/d_A² − ρg/d_B²].
- Dark-photon O(e·g) statement.
- J3 and J7 (C4, C5).
- J8 versus WP0-v2 (4.7): (q²/3)Ze²𝓃_e(R_κ) contact.
- 𝔨₃^{GS}/𝔨₃^X ≈ 3·0.11/(4π·14·1747) ≈ 1×10⁻⁶ in atomic units.
- C8 and Si-window kinematics:
  - |G₁₁₁|(GaAs) = 1.93 Å⁻¹ gives m ≳ 0.84 MeV at 1.5 eV.
  - The Si G₁₁₁ vertical transition at 3.4 eV gives m ≳ 1.10 MeV.
  - The Si PAER minimum is m = 2ω/v_max² = 0.339 MeV.
  - The ZPL at |K| = 0.98 Å⁻¹ opens at ≈ 0.47 MeV.
- F8 numbers.
- The δ₀/Q_min IR statement.
- G2/G5/G6 specifications.

## Owed corrections (for CORRECTIONS.md)
1. **S:** §M3 (ii), §3, §10, IF-5: Si edge p̄_on = 3 (TA allowed on the axis); LA kink p̄ = 4; derivation per §4c. Notify WP6.
2. **S:** (M.4), (M.14), (W.4c), F7/C21: the thermal factor appears once; L^{PA} includes (1 − e^{−βω}).
3. **S:** §2 L7c: 2603.13052 repair = move 1/m_N from (4.6) into (4.7); delete "m_N → m_N², rate consistent"; extend C3b to the (4.6) prefactor.
4. **W:** [0.5, 1.2]: state the sign hypotheses or widen to [0.4, 1.2] (or [0.4, 1.8]).
5. **W:** §M3: c_ν(Q̂) stationarity hypothesis; threshold = min F (O(m*c²) shift); Q_w removes a polar cap, not a shell; use ω_TA(Q), not c_TA·d.
6. **W:** §5: 1604.02394 mechanism (alternating signs Eqs. (7)–(10); antithetic Eq. (12)); L7c first surviving correction ≈ 2p²/(Mω_e) ≈ 4×10⁻⁴; fn. 3 inputs 1.2 / 0.7 eV, masses 250 / 320 MeV.
7. **W:** L9b(b): 1608.01994 used the 77 K data near the edge; O(1) only within ≈ 20–25 meV.
8. **N:** K, E_th collisions; declare Q_w, d, p̄_on, θ.
