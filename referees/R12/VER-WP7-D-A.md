# R12 verification VER-WP7-D-A: returns/R12/WP7-D-v2.md against referees/R11/REF-WP7-D-A.md

Same isolation as R11: no other referee reports, no state/, no other returns or briefs.
- I re-ran code/WP7-D-v2/checks.py: 49/49 PASS in about 5 s.
- I recomputed by hand or in sympy: the dark-Compton series to O(x³), the N6 ratios, the R_{I⁺I⁺} sign, the N4 single-bin numbers and the
  (F.7) propagator.
- I re-fetched 2308.00309 into literature/papers-r12-VER-WP7-D-A/ and deleted it afterwards.

## Item-by-item
| R11 item | v2 change | Verdict |
|---|---|---|
| C1: golden-rule mean "for any t_int" | §1.4(i): holds for t_int ≫ min(t_coh, 1/Γ_T) with a stationary coupling; Fejér-windowed otherwise; the t² counterexample is stated | RESOLVED |
| C2: crossover (3/2)t_coh | Now O(1)·t_coh, dropped from LIMITS. N4: s/b = 2.65 exact, 1.65 weak-signal, 2.02 offset-averaged (I reproduced all three) | RESOLVED |
| C3: Rayleigh penalty "O(1)" | 3–10 from 1905.13650 [ABS]. Stated as already inside the exponential-bin likelihood, so "apply one or the other" | RESOLVED. Correct: the 1711.10489 likelihood is the stochastic one. |
| C4: FDT at the lattice temperature | Spin temperature tanh(β_sω_L/2) = p in §1.5(c) and (D.5) | RESOLVED |
| C5: (D.7) per volume | P_abs/V | RESOLVED |
| C6: Q_DM^eff dependences | ω_n and annual v_E(t) dependence stated; "standard result, not new" | RESOLVED |
| C7: slab wording | Withdrawn. Orientation factors relative to the bulk κ/ε: 1 (slab, normal), 3ε₀/(ε₀+2) (sphere), ε₀ (slab, parallel). I checked these. | RESOLVED |
| C8a: 1508.01798 citation | "Eq. (7) and following text" | RESOLVED |
| C8b: (Zα)² = 0.045 for Cu | Kept only as an upper bound; 2δ_rel^a ≈ 0.01–0.02 tagged [E, UNVERIFIED] | RESOLVED. The new number is honestly tagged. |
| C9: J_L wording | §2.4(a): density row alone gives 1 − 2m/M; continuity changes this to 1 − m/M | RESOLVED |
| C10: f_ion factor-2 convention | N5a/b: the Gaunt identity is coded; the agreement requires "occupied states" to count both spins, which C10a's match to Eq. (52) forces; the R_{k′l′} normalisation of 2011.01940 is left UNRESOLVED-minor | RESOLVED, with an honest residual |
| C11: what 2011.01940 flags | Quote corrected; "paper wrong" left UNRESOLVED; sizes recomputed | RESOLVED. One new imprecision: see E2. |
| C12: pair-absorption operators | (T.1)–(T.2): i(S†∂↔S) with a (p − p̄)^μ pair tensor; per unit volume; ρ 0.39 → 0.3; n_φ²/2 in §3.3 | RESOLVED. N8 and N13 are correct. |
| C13: M1 decay ∝ n_r³ | §4.2 and L-D12; E1 ∝ n_r for contrast | RESOLVED |
| C14: [FT] tag misuse | 2501.09642 and 1509.01598 now [ABS + named section] | RESOLVED |
| C15: weak checks | N1 (quantum two-level Kubo check against the golden rule), N2, N3 added; C3 made a plain identity | RESOLVED |
| (f): 2308.00309 unread | Read; (F.7) light-mediator factor with t = 2m_χω − m_χ² | RESOLVED. Physics checked; quote flag in E1. |
| §(c) ratings | 1306.6089 envelope CONFIRMED; 2011.01940 Eq. (9) UNRESOLVED; ξ = 44.8 CONFIRMED; Q_DM^eff a reinterpretation | Consistent with R11 |
| LIMITS rows L-D3, L-D4, L-D5, L-D8, L-D9, L-D12 | All ✎ applied (§8) | RESOLVED. L-D8 should carry the E2 caveat. |

## New errors and flags in the changed sections

**E1 (W, minor): a spliced quotation.** §2.4(c) quotes 2308.00309 as "valid provided m_φ ≫ m_χ, with corrections of order (m_χ/m_φ)²" in
one pair of quotation marks. In the source these come from two separate sentences:
- the first is just before their Eq. (15): "The EFT description is therefore valid provided m_φ ≫ m_χ";
- the second is after their Eq. (16): "corrections of order (m_χ/m_φ)² as m_φ approaches m_χ".

Quote them separately. The physics of (F.7) is right:
- the amplitude ∝ Y_eeY_χν/(m_φ² − t) reduces to Λ⁻⁴ = Y²Y²/m_φ⁴ in the contact limit;
- t = ω² − q² = 2m_χω − m_χ²;
- the rate factor is 1 − 2(m_χ² − 2m_χω)/m_φ² + …. At ω → 0 this is the stated 1 − 2m_χ²/m_φ².

Eqs. (1), (14) and (15) of 2308.00309, and its citation of the 2011.01940 erratum, are quoted correctly.

**E2 (S-minor): the valence sizes are single-point values.** §2.4(b) says "valence shells 1.007 (100 keV), 1.021 (200 keV)". In N6 the ratio is
evaluated only at ω = free recoil + 12 eV, the impulse peak. Across the valence spectrum the ratio varies: at ω → |E_B| it is
1 − m_χ²/(2m_e²) = 0.981 (100 keV) and 0.923 (200 keV), from my evaluation of the same coded bracket. State it as "+0.7% to +2% at the
impulse peak, −2% to −8% at threshold". This is of the same order as the dropped S_{J_TJ_T} term, as v2 already says. The Xe K-shell values
check out: 0.887 at (100 keV, ω = 43 keV) and 0.661–0.592 at 56.5 keV. Those are also representative single ω points, and should be labelled
as such.

**E3 (none): the dark-Compton O(x²) claim is verified.** My independent series:
- NR seagull (T.4): 1 − 3x/2 + 5x²/2 − 35x³/8;
- 2109.08168 Eq. (2): 1 − 3x/2 + 5x²/2 − 15x³/4.

They agree through O(x²) and differ first at O(x³), so N12 is correct. v1's statement that "the O(x²) difference is relativistic" was wrong
and is correctly withdrawn. I also checked that the NR and relativistic two-body kinematics for ω′ agree through O(x³). The x³ difference is
therefore not kinematic, which is consistent with v2 leaving its attribution UNRESOLVED. Caution for L-D10: the "D" tag covers the algebraic
agreement only. That the NR omissions (Pauli spin terms, Klein–Nishina structure) vanish or cancel through O(x²) is observed, not derived.
Say so in one clause.

**E4 (none): checked, no error.**
- §1.5, R_{I⁺I⁺}: with H = +ω_LI^z, ⟨[I⁻(t), I⁺]⟩ = −2⟨I^z⟩e^{−iω_Lt} gives R = −2⟨I^z⟩/(V(ω − ω_L + i/T₂)). Absorption, −Im R > 0, then
  requires ⟨I^z⟩ < 0. I checked this.
- §1.5(b), the 1306.6089 resonant amplitude, has been moved to UNRESOLVED (factor 2). In R11 I read it as consistent in the H = −dσ·E
  convention, which matches the source's Larmor frequency 2μB. The source's own sentence calls d_nε_SE* the splitting, so UNRESOLVED is a
  defensible, conservative rating. Not an error.
- (D.1)/(D.3), pairing at k = −m_φv: consistent with N2 and with CONVENTIONS §2 signs. No error.

## Summary
All 15 R11 corrections and the (f) item are RESOLVED, and no item is NOT RESOLVED. Two minor new issues need fixing:
- E1: a spliced quotation from 2308.00309;
- E2: the valence ratio quoted at one point, the impulse peak (−2% to −8% at threshold).

The new dark-Compton claim (agreement through O(x²), first difference at O(x³)) is CONFIRMED.
