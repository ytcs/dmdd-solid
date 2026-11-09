# R8 / VER-WP1-A: verification of returns/R8/WP1-v3.md against referees/R7/REF-WP1-A.md

Isolation as in R7 (read: WP1-v3, code/WP1-v3/checks.py, my R7 report, CONVENTIONS/NOTATION/WP0-v2 as needed). checks.py re-run:
**49/49 PASS**. Independent recomputations this round: the optimum condition of [E13] (C9b), the (2̄00) branch value at q = X, the Ge Γ
bound M_xv_max²/2, the (1.4′) counterexample, the [E14] algebra and two table entries, the §2.6 counts and the TR-only parity of Im 𝒲̄₂.

## 1. Item-by-item (A-n = row n of my R7 verdict table)
| Item | R7 verdict | v3 action | Verification |
|---|---|---|---|
| A-1 [E1] | STANDS | kept | RESOLVED |
| A-2 [E2] | STANDS | kept + T-matrix reading | RESOLVED |
| A-3 [E3] beyond RPA | w/ corr. | (1.4′) (−R⁰)^{-1} + f_xc > 0; DKM; counterexample C3c | RESOLVED (R⁰ = −1, f_xc = −2, v_C = 3: 1 − f_HxcR⁰ = 2 > 0, ε^{-1} = 1 + 3(−½) = −½, and (1.4′) gives −1 < 0: correct) |
| A-4 on-shell projection | STANDS | kept (B-5 remainder (Δ_χ/q)n_e added) | RESOLVED |
| A-5 [E5] | w/ corr. | Σ_λ(2ω²/e²) Im ε_{T,λ} | RESOLVED |
| A-6 [E6] | STANDS | R̃_s ≡ R_mm = 4R_{s^zs^z} stated | RESOLVED |
| A-7 3-of-5 / Im 𝒲̄₂ | w/ corr. | PT ⇒ Im 𝒲̄₂ ≡ 𝒲̄₅ ≡ 0; two independent in Si/Ge; V_NL statement withdrawn; V_NL acts on the real relation | RESOLVED. Also checked the TR-only extension: S_nj(q) = −S_nj(−q)* makes q·Im S_nj odd in q, so Im 𝒲̄₂ averages to 0, as stated |
| A-8 O₈ vs 2510.25835 | w/ corr. | 20–30 (IP, ⟨p_T²⟩) [E]; medium factor |ε_L|²(1 − δ_LFE); Cauchy–Schwarz; "not fixed by Im(−1/ε_L) alone; fixed by ε_ij" | RESOLVED (see D3 below: I accept the in-medium enhancement, which I had missed; it only strengthens "conservative") |
| A-9 response count | w/ corr. | 12 (Si/Ge), 18 (generic q̂) | RESOLVED (real symmetric 3×3 = 6, Hermitian 3×3 = 9; the IP triplet = ¼ of the IP singlet) |
| A-10 [E7] | STANDS | kept | RESOLVED |
| A-11 (2̄00) Umklapp | w/ corr. | allowed on axis, |q| = 2.63 keV, C10c; Δ₁ ↔ Δ₂′ relabelling across X (C10e) | RESOLVED. The cross-check is right: along the axis, q = (−s,0,0) with s < 1 has its final state at reduced k = −s (G = 0, forbidden); for s > 1 it is at 2 − s with G = (2̄00) (allowed). The switch at X matches the X₁ = Δ₁ ⊕ Δ₂′ sticking |
| A-12 thresholds | FALLS | pinned boundary dropped; [E13] min over q, class-resolved | RESOLVED. Optimum: 2D = QD′ with D = Qv − E − (Q₀−Q)²/2M gives Q(Mv + Q₀) = 2ME + Q₀² (C9b); Si: Q = 1455 eV ✓, 0.422 MeV ✓. (2̄00) branch at q = X: electron at X, offset 0.096 eV, m = (2.28 keV)²/[2(6.04 − 1.25) eV] = 0.543 MeV ✓. Ge L 0.32–0.36 MeV ✓. Floors 0.329/0.211 MeV ✓ |
| A-13 [E8] | w/ corr. | factor 1/3; continuum |∇_kρ|²k_rel²/3; C8c line/continuum matching; +35% downgraded | RESOLVED (n_H → ∞ line density |∇ρ|²/(6πa_x⁵E_x^b) matches the continuum at E_min⁺: checked) |
| A-14 [E10] Si sentence | w/ corr. | "Umklapp only ≥ 3.25 keV" dropped; allowed on axis for |q| ≥ 2.28 keV | RESOLVED |
| A-15 plasmon | STANDS | q_c → 2.24 keV (D2) | RESOLVED; I concede my R7 A13(c) (see D2) |
| A-16 §5 | STANDS | FW spin-curl coefficient fixed (B-16) | RESOLVED (not re-derived by me) |
| A-17 §6 / 2607.06005 | STANDS | kept | RESOLVED |
| A-18 L1 [E12] | STANDS | kept | RESOLVED |
| A-19 KKL eq. number | w/ corr. | Eq. (24) (PDF), HTML (27) noted | RESOLVED (both numberings name the same equation; my "no Eq. (27)" referred to the PDF) |
| A-20 L14/L17 | STANDS | kept | RESOLVED |
| A-21 EXCEED-DM | w/ corr. | K_e·σ_e spin-current vertex; (B15)–(B18) | RESOLVED |
| A-22 G5 | w/ corr. | matrix-free Haydock, interpolated coarse kernel | RESOLVED |
| A-23 contested | STANDS | kept | RESOLVED |

## 2. Rebuttals addressed to REF-A
None. §R1 rebuts REF-B only. My positions are settled against me in two §R2 rows, both ACCEPTED:
- **D2 (q_c): ACCEPT B's 2.24 keV.** ω_pl(q) = (ω_p² + ⅗q²v_F²)^{1/2} = qv_F + q²/2m_e at q = 2.24 keV: LHS (275.6 + 0.6·244.6)^{1/2} = 20.55 eV,
  RHS 15.64 + 4.91 = 20.55 eV. Near the crossing ⅗(qv_F/ω_p)² ≈ 0.4–0.5, so my "O(q²v_F²/ω_p²), negligible" was wrong. The no-plasmon
  conclusion stands (ω_p/v_max = 6.26 keV > 2.24 keV).
- **D6 (2002.06937 q_c ≈ 5 keV): ACCEPT B's CONFIRMED** (FT quote "a is the lattice spacing"; 2π/a_lat = 2.28 keV). I had marked it UNRESOLVED.
- **D3: ACCEPT.** In medium S_nn carries 1/|ε_L|² while j_T is screened by LFE only, so the ratio exceeds the IP moment ratio by
  ≈ |ε_L|²(1 − δ_LFE). My 20–30 is the IP value. Calling the factor UNRESOLVED pending G10 is the right status.
- D1, D4, D5, D7–D9: consistent with my R7 derivations; no objection.

## 3. New errors and overclaims in the changed sections
- **N1 (W, §3.7 and IF-6/IF-6b): "above ≈ 0.54 MeV the allowed zero-phonon line leads (PAER/ZPL ≈ 10⁻³–10⁻²)".** This contradicts §3.2 (c),
  where the (2̄00) vertex is "amplitude unknown, possibly small" because the (200) potential component vanishes. The 10⁻³–10⁻² ratio uses
  a reference-size allowed vertex (η_PA) that has not been shown for this branch. In addition, at m_χ just above 0.54 MeV the allowed region
  is a single point (q = X, on axis), so the integrated ratio starts at 0, exactly as the text argues for the second-class onset. Required:
  "above ≈ 0.54 MeV an allowed zero-phonon channel opens; whether it leads depends on |ρ_cv| on the (2̄00) branch [E, open]". The same
  hedge belongs in the IF-6 row ("allowed… leads") and in the M1 statement.
- **N2 (minor, [E13] Si second class): the lowest bright state differs from E_x.** On the axis the 1s line is dark in the forbidden class;
  the lowest bright state is the 2p line (E_min − E_x^b/4) or the off-axis 1s with weight ∝ |δq_⊥|². Using E_x = E_g − E_x^b(1s) shifts
  m_χ^{ZP} by only ≈ g·ΔE/(Qv − E) ≈ 0.42 × 0.011/3.8 ≈ 0.001 MeV, far below the parabolic uncertainty. State that the second-class value
  is the onset with a vanishing weight.
- **[E14] checked:** the algebra follows from the corrected [E8] (|∇ρ|²·2μ_xε/3·(1 + ζ_S²) = |∇ρ|²(ε + E_x^b)/(3a_x²E_x^b)). Central entries
  were recomputed: ε = 0.1 eV gives 2.2, ε = 1 meV gives 0.35 (table: 2, 0.3). The inputs (ℓ_∇, η_PA) are correctly tagged [E]. No error.
- **M1 window [E]:** Si PAER-leading 0.338–≈0.43 MeV follows from [E13] and the ∂ω_max/∂m_χ = q²/2m_χ² ≈ 6 eV/MeV estimate (checked). The upper
  edge inherits the parabolic Δq ≈ 0.21 q_BZ caveat, which v3 states. Ge PAER-only ≈ 0.21–0.32 MeV: consistent.
- The Ge Γ rebuttal to B (§R1) was checked only for arithmetic: M_xv_max²/2 = 0.54 × 511 keV × 7.02×10⁻⁶/2 = 0.97 eV > 0.888 eV. The rebuttal
  rests on the [E] valence-band argument, which is for REF-B to adjudicate.

## Verdict
All 23 R7 items are RESOLVED, and none is resolved incorrectly. There are no rebuttals to adjudicate; three §R2 settlements against REF-A
(D2, D3, D6) are accepted. One new wording overclaim (N1) needs a hedge, plus a minor clarification (N2). [E13] and the (2̄00) treatment
are correct.
