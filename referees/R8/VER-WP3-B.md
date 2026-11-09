# R8 / VER-WP3-B: verification of returns/R8/WP3-v3.md against referees/R7/REF-WP3-B.md

Isolated referee B (same isolation as R7). Read: WP3-v3 §0, §M3, §M7, §2 L7c, §6, §R1, §R2, §12–§16. Ran code/WP3-v3/checks.py: 105/105 PASS (≈ 11 s).
My own extra work: re-derived (M.7a), the EPW weight identity, Q_w and the dispersion-corrected criterion in §3 below. No literature re-fetched (no new paper claims).

## 1. Item-by-item verdicts (R7 table rows; B-n in the v3 closing table)
| R7 item | v3 action | Verdict | Note |
|---|---|---|---|
| B-1 amplitude, Pauli | kept, my C11c remark noted | RESOLVED | — |
| B-2 thermal factor twice | 𝒫_± (EPW (64)) in (M.4), (M.14); (M.3) adds f_v(1−f_c) | RESOLVED | Re-derived: second/first EPW term = [n/(n+1)]·e^{−β(ε_c−ε_v)} = e^{−βω} on shell (emission). Absorption gives the same; C21a–c pass |
| B-3 η/(2q) | kept | RESOLVED (stood) | — |
| B-4 δ₀ vs (M.9) | δ₀ = 0.3 eV; 0.1 eV values kept with the ω_Q/δ₀ ≈ 0.6 caveat | RESOLVED | — |
| B-5, B-6 Dyson/fp, f-sum | kept | RESOLVED (stood) | — |
| B-7 (M.13) TDH, not ALDA; retarded W | tag [D at RPA/TDH]; k_xc source; W retarded | RESOLVED, with a NEW minor error | ½ factor on the cross term (§3.2) |
| B-8 [0.5, 1.2] conditional | [0.4, 1.8], multiplicative (1+δ_ω)(1+δ_LF)(1+δ_pair) | RESOLVED | Multiplicative composition is the right one at the \|M̃\|² level. I withdraw my additive [0.5, 1.7]. Product range 0.8·0.5 = 0.4 to 1.2·1.5 = 1.8 ✓ |
| B-9 soft limit (off-shell control) | caveat applied in §M3(d) | RESOLVED | — |
| B-10 fixed-q onset | threshold = min F, shift −½(m_c+m_h)\|∇ω\|² | RESOLVED; **my R7 "μeV" was wrong** | ½·0.72 MeV·(1.95×10⁻⁵)² = 0.137 meV (TA). I concede §R2.2 |
| B-11 C23 blind to c_ν(Q̂) | (M.7a), C23d–k | RESOLVED, with a NEW caveat | (M.7a) is derived for linear dispersion only (§3.1) |
| B-12 Si TA p̄ = 4 FALLS | Si TA edge 3; LA kink 4; C4v/C3v tables (C24) | RESOLVED | Conclusion adopted. The rebuttal of (a) is accepted (§2). The LA = Δ₁ zero is verified (§3.3) |
| B-13 Q_w | Q_w = M_xc + (M_x²c² + 2M_xδ₀)^{1/2} = 0.33 Å⁻¹ at 0.3 eV; polar cap | RESOLVED | Re-derived: \|Q\|²/2M − δ₀ ≥ c\|Q\| ⇒ the root. 2·1.41·0.511 MeV·0.3 eV ⇒ 657 eV = 0.333 Å⁻¹ ✓. Cap formula ✓ |
| B-14 Migdal / 4α | kept | RESOLVED (stood) | — |
| B-15 2603.13052 (3.11) | kept CONFIRMED | RESOLVED | — |
| B-16 (4.6)/(4.7) m_N | "m_N misplaced between (4.6) and (4.7)"; C3a–d; (4.8) UNRESOLVED | RESOLVED | C3c correctly shows the v2 repair leaves 1/m_N |
| B-17 L7c ≲ 10⁻³ | applied (2p²/Mω_e and ω_ph²/ω_e² together) | RESOLVED | — |
| B-18 ZG wording | "alternating signs (7)–(10)"; characterisation, not an error of the paper | RESOLVED | — |
| B-19 EPW claims | kept CONFIRMED | RESOLVED | — |
| B-20 (W.13) ∝, impulse, ratio | equality in the WP0-v2 (3.3) measure, with δ(ω_q − ω_ph − ω_γ); E_R ≫ ω_ph; 10³–10⁴ | RESOLVED | Measure consistent with S = (2π/V)Σ\|·\|²δ and Γ = ∫d³q/(2π)³∫dω 𝔇 S δ |
| B-21 J3 "upper bounds" | [E] | RESOLVED | — |
| B-22 J8 | kept + WP0-v3 G5 factor [1 + 2𝓃_e/𝓃_e(R)] | RESOLVED (not re-audited beyond C26a: 6∫j₂(y)dy/y = 6·⅓ = 2 ✓) | — |
| B-23 §11 / F1; B-24 interfaces | kept | RESOLVED | — |
| B §9 checks | C3a–d, C21a–c, C23d–k, C27, C28, C30 added; C14b marked as bookkeeping | RESOLVED | No check covers dispersion in (M.7a) (§3.1) |

## 2. Rebuttal §R1 (to B-12(a)): ACCEPT
Claim: the on-axis TA threshold is a minimum iff γ_c > −|K_pk|/(2|q|), not γ_c > −½. My R7 statement holds only at |q| ≈ |K_pk|.
**Derivation.** Q* = K_pk − q, ϑ = ∠(q̂, K̂_pk). Then |Q*|² = d_K² + 2|q||K_pk|(1 − cos ϑ), so |Q*| = d_K + |q||K_pk|ϑ²/(2d_K) + O(ϑ⁴).
The transverse part of Q* is |q| sin ϑ. The parallel part is ±(|K_pk| − |q| cos ϑ) ≈ ±d_K for either sign of |q| − |K_pk|. Hence ϑ_Q ≈ |q|ϑ/d_K.
With c = c₀(1 + γ_cϑ_Q²):
E − E_g = c₀|Q*|(1 + γ_cϑ_Q²) = c₀d_K + c₀(|q|/d_K)(|K_pk|/2 + γ_c|q|)ϑ² + O(ϑ⁴).
This is (M.7a) for both signs of |q| − |K_pk|. In R7 I set |q| = |K_pk| in the bracket and then wrote "along every azimuth" without that restriction. With γ_c ∈ [−0.96, −0.78] the axis is:
- a minimum along all azimuths for |q| < |K_pk|/1.92 ≈ 0.52|K_pk|;
- a saddle for 0.52 < |q|/|K_pk| < 0.64;
- a maximum above that.
The saddle band is not stated in §M3(e); it is harmless, since its minima are off axis. C23i's exact-geometry scan (on axis at 0.5|K_pk|, off axis at 1.3|K_pk|) agrees. The rebuttal does not affect p̄ = 3, which the package keeps.
**Caveat (does not reverse the acceptance):** see §3.1. The numerical crossover "≈ 1.0 keV, which covers the low-mass end of the M1 window" is not established once TA dispersion is included.

## 3. New errors and caveats in the changed sections
**3.1 (M.7a) uses linear dispersion; the on-axis/off-axis criterion changes with ω_TA(Q) (NEW ERROR, [E]-level, location only).**
§M3(c) itself requires "thresholds use ω_ν(Q*) … never c_ν·d_K", and (e) concedes d_K ≈ 0.3–1 Å⁻¹ is "beyond [elasticity's] range". Yet (M.7a) and the 1.0 keV crossover use c₀d_K.
With ω(Q, ϑ_Q) = ω₀(Q)(1 + γ_ω(Q)ϑ_Q²):
E − E_g = ω₀(d_K) + [ω₀′(d_K)|q||K_pk|/(2d_K) + ω₀(d_K)γ_ω|q|²/d_K²]ϑ².
So the axis is a minimum iff **γ_ω(d_K) > −(|K_pk|/(2|q|))·r(d_K)**, where r ≡ v_g d_K/ω₀(d_K) ≤ 1 for sub-linear branches.
At the window's low edge (|q| ≈ 0.9 keV = 0.46 Å⁻¹, d_K ≈ 0.52 Å⁻¹ ≈ 0.45 X), a sine-like Si TA dispersion gives r ≈ 0.83. The right-hand side is then ≈ −0.89.
γ_ω ≈ −0.96 (the elastic value) lies below that, so the axis is already a saddle or maximum along the (001) tilt plane there. The crossover moves to |q| ≈ 0.43|K_pk| ≈ 0.85 keV.
Correction: replace (M.7a) by the dispersive form above; mark the crossover "≈ 0.8–1.0 keV [E, needs ab initio ω_TA(Q) and γ_ω(Q)]" (O-WP3-9 already lists the ab initio dispersion); drop "covers the low-mass end" from §R1/§M3(e).
p̄_on (TA = 3 on and off axis) is unaffected, because TA is symmetry-allowed on the axis (C24f).
**3.2 ALDA cross term factor (NEW ERROR, minor).** ½k_xc(δn_q + δn_Q)² contains the cross term k_xc δn_q δn_Q, with coefficient 1, not ½.
§M7's "½k_xc⋆[δn^{(1)}(q,ω)δn^{(1)}_ph(Q,ω_Q)]" is low by 2, unless ⋆ is defined to sum both orderings; define ⋆ or drop the ½. The size [E] and the tag are unaffected.
**3.3 Selection rules and the LA kink (verified, no error).** C4v(x) restriction: Γ₂₅′ (T₂g) → B₂ ⊕ E = Δ₂′ ⊕ Δ₅, with no Δ₁. LA = Δ₁, LO = Δ₂′, TA = TO = Δ₅. Operator Δ₁ for G′ = 0.
Then A₁ ⊂ Δ₁ ⊗ Γ_ph ⊗ (Δ₂′ ⊕ Δ₅) needs Γ_ph ∈ {Δ₂′, Δ₅}. So LA is forbidden, and TA, TO, LO are allowed (consistent with the strong TA/TO, weak LA replicas of Si optical absorption).
The LA minimum is on the axis (γ_LA > 0). On the axis the fixed-q exponent is 3 (|M|² ∝ δk² at the pocket bottoms). Off axis |M|² ∝ ϑ².
Both pieces give E⁴ after the 2D angular integral, so **LA kink p̄ = 4** ✓. Ge: C3v has no t_d elements, Γ₂₅′ → Λ₁ ⊕ Λ₃, and all branches are allowed ✓. [111] is a conical acoustic axis of cubic crystals, so TA minima are off axis ✓.
Exciton Si LA 5/2 = ½ + 2 ✓. The (2̄00) class boundary 2.28 keV is the midpoint of |K_pk| = 1.94 and 2.62 keV ✓ (not independently re-derived: the Δ₂′ operator character, C24g).
**3.4 Other changed items checked, no error:** the multiplicative envelope (C28); Q_w and the polar cap (C30); (W.13) normalisation; the GaAs ratio n_rZ*²/|f|² ≈ 3×10³ at 1 eV with ω⁻⁴ scaling; C3a–d; the C25 shift.

## 4. Summary
- All 24 R7 items are RESOLVED, including B-12 (Si TA p̄ = 3).
- I concede B-10's size (0.14 meV, not μeV) and B-8's composition (multiplicative [0.4, 1.8]).
- Rebuttal §R1: ACCEPT. The axis-minimum criterion is γ_c > −|K_pk|/(2|q|).
- New issues:
  - (i) (M.7a) and the "≈ 1.0 keV" crossover assume linear TA dispersion. The general criterion γ_ω > −(|K_pk|/2|q|)·v_g d_K/ω₀ moves the crossover to ≈ 0.85 keV, below the window's low edge [E]. This affects the location only, not the exponents.
  - (ii) The ALDA cross-term coefficient is k_xc, not ½k_xc.
