# R8 / VER-WP3-A: verification of returns/R8/WP3-v3.md against referees/R7/REF-WP3-A.md

**Scope.** I read the following parts of WP3-v3:
- the change table §0;
- §M3 (a)–(e) and the final p̄_on table;
- (M.3), (M.4) and (M.14), plus the (W.4c) line;
- §M7 (the envelope);
- §M9 (the restated M1 window);
- §2 L7c, §4 L9b(b) and §5;
- §11, R1 and R2, the closing table §13 and §16.

**Checks.** code/WP3-v3/checks.py ran 105/105 PASS in about 11 s. Below, "re-derived" means I checked the step by hand or by my own short computation,
independently of the package's code. Isolation was kept: I did not read the referee files, WP1-v3, or state/.

## 1. Item-by-item verdicts (R7 items A-V1 … A-V24)
| Item | R7 verdict | R8 verdict | Basis |
|---|---|---|---|
| V1, V3, V4, V5, V8, V13, V20, V21, V24 | STANDS / CONFIRMED | RESOLVED (kept unchanged) | spot-checked; text unchanged in substance |
| V2 thermal factor | SWC | **RESOLVED** | 𝒫_± = (1 − e^{−βω})(n+½±½)f_v(1 − f_c) equals EPW Eq. (64) on shell at every T (re-derived below); (M.3), (M.4), (M.14) and (W.4c) are now mutually consistent (C21b) |
| V6 (M̃ at RPA/ALDA) | STANDS | RESOLVED (tag narrowed to RPA/TDH plus an ALDA k_xc source) | R2.4: accepted, see §2 |
| V7 [0.5, 1.2] | SWC | **RESOLVED** | (1 ± 0.02)(1 ± 0.2)(1 ± 0.5) gives [0.392, 1.836], quoted as [0.4, 1.8] [E/C]; the conditional range [0.5, 1.2] is kept with its two sign hypotheses stated |
| V9 fixed-q threshold | SWC | **RESOLVED** | min F; the shift −½(m_c + m_h)c² = 0.137 meV (TA) and 0.285 meV (LA) re-derived (1.41 m_e; 5.85 and 8.43 km/s) |
| V10 c_ν stationarity | SWC | **RESOLVED, and strengthened** | criterion (M.7a) re-derived (§3); my R7 sentence "the hypothesis holds in Si" was incomplete, see R2.1 below |
| V11 Si TA p̄ = 4 | FALLS | **RESOLVED** | C24 characters give: G′ = 0, LA (Δ₁) forbidden, TA/TO/LO allowed; edge 3, LA kink 4 (§3) |
| V12 Q_w / polar cap | SWC | **RESOLVED** | cos ϑ_w = 1 − (Q_w² − d_K²)/(2\|q\|\|K_pk\|) is the cap rim from \|Q*\|² = d_K² + 2\|q\|\|K_pk\|(1 − cos ϑ); ω_TA(Q*) used, not c_TA·d_K; Q_w(δ₀ = 0.3 eV) = 0.333 Å⁻¹ re-derived |
| V14 L7c size; fn. 3 | SWC | **RESOLVED** | 2p²/(Mω_e) ≈ 3.8×10⁻⁴ and (ω_max/ω_e)² = (0.06/5)² ≈ 1.4×10⁻⁴ give ≲ 10⁻³; fn. 3 inputs (1.2 / 0.7 eV, 250 / 320 MeV) and its "most conservative" wording are now quoted correctly |
| V15 2603.13052 (4.7) | misprint CONFIRMED; repair REFUTED | **RESOLVED** | v2 repair withdrawn; m_N misplaced between (4.6) and (4.7); C3b–d agree with my R7 sympy ratios (1, 1, 1/m_N) |
| V16 (3.11) / (4.8) | CONFIRMED / UNRESOLVED | RESOLVED (recorded as rated) | — |
| V17 ZG mechanism | SWC | **RESOLVED** | §5 now cites alternating signs, Eqs. (7)–(9), the heuristic all-orders Eq. (10), and the antithetic pair at Eq. (12), matching the full text I read in R7 |
| V18 bremsstrahlung | STANDS [E] | RESOLVED | ω⁻⁴ scaling and 10³–10⁴ adopted |
| V19 J8 | STANDS | RESOLVED (amended for WP0-v3 G5) | I did not re-verify the new factor [1 + 2𝓃_e/𝓃_e(R_κ)]: it comes from WP0-v3, outside my scope (flag F3) |
| V22 1608.01994 | REFUTED in size | **RESOLVED** | 77 K data; ≈ 4 meV; n_TA ≈ 0.07; O(1) within ≈ 20–25 meV |
| V23 notation | SWC | **RESOLVED** | K_pk, E^{PA}_th(q̂), ϑ, d_K, p̄_on, Q_w, γ_c, β_c, C^{el}, 𝒫_± are all declared |

Count: 24 of 24 RESOLVED; no item is NOT RESOLVED.

## 2. Rebuttals and settlements touching REF-A
§R1 addresses REF-B only; no rebuttal is addressed to me. The §R2 settlements that rule on my positions are adjudicated here.

- **R2.1, the location of the Si TA minimum (REF-A said "on the axis, since stationary"): ACCEPT.**
  - Setup: take Q* = K_pk − q at polar angle ϑ. Then |Q*|² = d_K² + |q||K_pk|ϑ² + O(ϑ⁴), and the tilt is ϑ_Q ≃ |q|ϑ/d_K, valid for |q| on either side of |K_pk|
    because c_ν(Q̂) = c_ν(−Q̂).
  - Threshold: with c = c₀(1 + γ_cϑ_Q²), E = c₀|Q*|(1 + γ_cϑ_Q²) = c₀d_K + c₀(|q|/d_K)(|K_pk|/2 + γ_c|q|)ϑ², which is (M.7a).
  - Lowest-TA curvature: with Q in (001), the out-of-plane TA has ρc² = C₄₄ exactly, so γ = 0 for it. The in-plane 2×2 Christoffel lower root is
    C₄₄ + (A − B²/A)ϑ_Q², so γ_c = −(B² − A²)/(2AC₄₄). With the stated constants this gives −0.961, which I reproduced numerically.
  - Result: the axis is a minimum only for |q| < |K_pk|/(2|γ_c|) = 0.52|K_pk|. With |K_pk| = 1.94 keV this is ≈ 1.0 keV.
  - So my R7 statement was a necessary condition presented as sufficient. The exponent conclusion (p̄ = 3) is unaffected.
- **R2.2, size of the threshold shift: ACCEPT.** The numbers are re-derived in §1 (V9).
- **R2.3, multiplicative envelope: ACCEPT.** The composition is at the |M̃|² level. The additive alternative understates the high end when |δ_pair| ~ 0.5.
- **R2.4, (M.13) is [D] only at RPA/TDH: ACCEPT.** I accepted the topology argument without deriving the source N in R7, so the narrower tag is the
  correct one. I have not checked the ALDA k_xc term itself (flag F3).
- **R2.5, δ₀ = 0.3 eV: ACCEPT.** (M.9) needs δ₀ ≫ ω_max ≈ 60 meV, and my R7 Q_w check used 0.1 eV, which is inconsistent with that requirement.
- **R2.7, the L7c terms: ACCEPT.** Free-recoil and bound-lattice terms are distinct regimes, and both are ≲ 10⁻³.

## 3. Changed sections: verification
**LA/TA selection rules (C24): verified.** Group-theory facts used:
- Γ₂₅′(T₂g) restricted to C₄ᵥ is B₂ ⊕ E = Δ₂′ ⊕ Δ₅.
- Phonons along Δ are A₁ ⊕ B₂ ⊕ 2E, with LA = Δ₁ (the branch continuous to the in-phase translation), LO = Δ₂′ and TA = TO = Δ₅. This agrees with the
  table I quoted from memory in R7, so the [UNVERIFIED] tag on it is now discharged by derivation.

Selection rule: the amplitude is nonzero iff Γ_ph ⊗ Γ_v ⊃ Γ_op.
- G′ = 0, Γ_op = Δ₁: only Γ_ph = Γ_v survives, so LA is forbidden and TA, TO, LO are allowed.
- G′ = (2̄00): Γ_op = Δ₂′. With G′·t = −π, the operator has character −1 on C₄ and σ_v and +1 on σ_d, i.e. B₂. Then:
  - LA (Δ₁) needs a Δ₂′ hole, which exists: allowed.
  - Δ₅ ⊗ Δ₅ ∋ Δ₂′: TA and TO allowed.
  - Δ₂′ ⊗ Δ₂′ = Δ₁ and Δ₂′ ⊗ Δ₅ = Δ₅, neither contains Δ₂′: LO forbidden.
  - This matches C24g.
- The 2.28 keV switch point is the midpoint of |K_pk| = 1.94 and 2.63 keV (k_c = 0.85X, and k_c − 2X).
- Ge: C₃ᵥ ⊂ T_d carries no t, Γ₂₅′ restricted to C₃ᵥ is Λ₁ ⊕ Λ₃, and the phonons are 2Λ₁ ⊕ 2Λ₃, so all branches are allowed. [111] is the conical acoustic axis
  of cubic crystals, so the TA minimum is off axis and p̄ = 3.

**Final p̄_on table: verified.** The rule is p̄ = p_on + 1 at a generic isolated minimum and p_on + 2 at a symmetry zero located at the minimum.
- Si TA: allowed and generic, so 3.
- Si LA: γ_LA > 0 puts the minimum on the axis, where the vertex is zero, so 4.
- Si (2̄00) class LO: 4, provided the LO minimum is on the axis; that location is tagged [E] and remains open.
- Exciton replicas: ½ + 1 = 3/2, and Si LA ½ + 2 = 5/2.
- SOC: an admixture of (4%)² = 2×10⁻³ is consistent.

**Envelope [0.4, 1.8]: verified** (§1, V7).

**M1 window: verified within its [E] tags.**
- Second-class zero-phonon threshold: minimising (E_g + |K_pk − q|²/2M_x)/|q| + |q|/2m_χ over |q| ≤ |K_pk| (E_g = 1.170 eV, |K_pk| = 1.94 keV, v_max = 794.5 km/s)
  gives m_χ^{ZP} = 0.419 MeV for M_x = 1.41 m_e and 0.449 MeV for M_x = 0.48 m_e. This supports "0.42 (0.40–0.44)", and confirms that v2's pinned 0.47 was an
  upper bound.
- PAER edge: 2E_g/v_max² = 0.333 MeV. Adding ω_TA(Q*) of ≈ 12–18 meV gives 0.336–0.338 MeV, as stated.
- The ratio ϖ_II band (0.43 / 0.54 MeV) and the Ge numbers come from WP1-v3 [E13]/[E14], which I did not read; I accept them as cited inputs.

## 4. New errors and flags in the changed sections
No new error found. Minor flags:
- **F1.** The summary table and IF-8 give the Si PAER-only window as "0.333–≈0.42". But 0.333 is the floor for exciton replicas, or the bare 2E_g/v_max²; the
  free-pair PAER edge is 0.336–0.338 (§M9). Name which edge the 0.333 belongs to wherever it appears.
- **F2.** The Si (2̄00)-class "LO 4" assumes an on-axis LO minimum. The table tags the location [E], but the exponent is listed without the conditional. Add
  "if the minimum is on the axis; otherwise 3".
- **F3.** The J8 factor [1 + 2𝓃_e/𝓃_e(R_κ)] and the ALDA k_xc source (C27) are new material that I have not verified. They should be confirmed by whoever
  referees WP0-v3 G5 and X2/TDH. This flag is not a defect.
