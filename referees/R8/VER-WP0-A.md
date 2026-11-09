# R8 / VER-WP0-A: verification of returns/R8/WP0-v3.md against referees/R7/REF-WP0-A.md

Referee: REF-WP0-A, isolated as in R7. I read WP0-v3 §0, §1–§7, §8.3, §9.2, §11, §12, §14 and §16–§18, plus code/WP0-v3/checks.py.
I re-ran checks.py: 76/76 PASS, and inspected C15–C22. I did not read other referees' reports or state files.

## 1. Item-by-item verdicts (R7 items A-V1 … A-V18, A-m1 … A-m4)
| Item | v3 location | Verdict | Note |
|---|---|---|---|
| V1 master rate, anchor | (3.3), (2.2) | RESOLVED (no change needed) | — |
| V2 tr[𝔇S] → tr[𝔇ᵀS] | (3.4), index-order paragraph, (4.4), (7.3); G1 | RESOLVED | −2tr[𝔇_IS_I] is right (C15c). CONVENTIONS §8 still needs the amendment (G1, coordinator) |
| V3 𝒪₂ excluded | §2 basis; G2; OW0-16 | RESOLVED | — |
| V4 orbit–orbit term | (1.2), (4.6″); §17.1 | RESOLVED, with rebuttal ACCEPTED (§2 below) | — |
| V5 R^∞ ≡ 0 | (4.2); C17 | RESOLVED | R^L_jj(q,0) = −𝓃/m re-derived from (q·j)_fi = ω_fi n_fi |
| V6 (4.6e) H_hf off | (4.6)(e) | RESOLVED | — |
| V7 moment reading of (4.7) | (4.5), (4.7); C16 | RESOLVED | v3's pairing S_ab[O] + S_ba[O†] is the correct one. My R7 wording "S_eκ[O†]" was loose; I re-derived it below |
| V8 (4.7) q → 0 limit | (4.7′), §16.1; C19 | RESOLVED | See §3 below; the independent RPA check (C19h) confirms the corrected form |
| V9 Ward identity | (4.8) | RESOLVED (no change needed) | — |
| V10 (4.9) import tag | (4.9) | RESOLVED | — |
| V11 Bohm–Staver ε | (5.3); G15 | RESOLVED | — |
| V12 (5.5) classes, sketch, TR | (5.5) | RESOLVED | TR ⇒ R(Q,−ν) = R(Q,ν)† checked: Lehmann R_{GG′}(q,−ω) = R_{−G,−G′}(−q,ω)* combined with TR R_{GG′}(q) = R_{−G′,−G}(−q) |
| V13 "to O(g²)"; 𝔗 | (5.6), (5.7a) | RESOLVED | (5.7a) has the standard second-order density-matrix structure, (ω_f − ε_a + ε_b)r^{(2nd)} = [F¹,r²] + [F²,r¹], tagged [D in X2] |
| V14 CC-1 caveats | (7.2), §10, §16.2 | RESOLVED | Two-level tag ([D] in TDH/ALDA, [D, sketch] many-body) is correct |
| V15 Theorem D | §6.2, (6.1); G10 | RESOLVED, but NEW ERROR N1 | κ_BO² parameter, leakage qualifier, N-uniformity and the Ge 𝔉 [C] are all applied |
| V16 (6.3) prefactor; definitions | (6.3), (iv″c) | RESOLVED | (5/2π + 1/π)Γ/δ = 1.114Γ/δ at ℓ_win = δ, consistent with (1.1 + b_λ) |
| V17 L0 | §9.1 | RESOLVED (no change needed) | — |
| V18 L17 (iii), (ii), citation | §9.2, (9.4′); C20; G6 | RESOLVED, but NEW ERROR N2 (Si example) | — |
| m1 (4.6c) sign change at T = 0 only | (4.6)(c) | RESOLVED | — |
| m2 imported steps retagged | (4.9), (iii), (iv″) | RESOLVED | — |
| m3 NOTATION deviations | §15 | RESOLVED | — |
| m4 numbers | — | RESOLVED (no change needed) | — |

## 2. Rebuttal §17.1 (to A-V4): ACCEPT
The claim is that E_ee in δ_oo must be replaced by E′_ee (uniform Hartree part removed), because the uniform part contributes exactly zero.
*Derivation.* The Breit kernel is the transverse photon propagator: (𝟙 + r̂r̂)/(2r) ↔ 4π(𝟙 − k̂k̂)/k², so FT[(𝟙 + r̂r̂)/r] = (8π/k²)(𝟙 − k̂k̂).
As a cross-check, FT[r̂r̂/r] = (4π/k²)(𝟙 − 2k̂k̂), whose k̂k̂ contraction is −4π/k² (C18c output). Then
⟨[n†,[H_oo,n]]⟩ = Σ_{i≠j}⟨q·𝒦·q e^{iq·r_ij}⟩ = ∫d³k/(2π)³ q·𝒦̃(k)·q ⟨Σ_{i≠j} e^{i(k+q)·r_ij}⟩, plus the term with q → −q.
The uniform part of the pair density forces k = −q, and there q·(𝟙 − q̂q̂)·q = 0. The contribution therefore vanishes identically, not only in angular average.
My R7 step "cos(q·r_ij) → 1 for all pairs, with E_ee" is ill-defined for an extended solid, because E_ee per electron diverges with L. v3 is right.
The surviving inhomogeneous (G ≠ 0, atomic-scale) and xc parts at q r ≪ 1 reproduce the angular factor: the k̂-average of q·(𝟙 − k̂k̂)·q·8π/k² is
(2/3)q²·8π/k², which equals (4/3)q²·4π/k², the real-space ⟨1 + (q̂·r̂)²⟩ = 4/3. Using E′_ee ≈ E_ee^{atom} (Thomas–Fermi ≈ T/3) keeps 0.27δ_mv as an [E].
Both the operator identity and the number survive. The rebuttal correctly sharpens the definition. ACCEPT.

## 3. Rebuttal §17.2 and §16.1, so far as they bear on A-V8: v3 sides with A-V8. I confirm the derivation, and the remaining point
- G = 0: (q·q)²/q² = q², exact at every q ≠ 0, non-analytic ✔. G ≠ 0: (q·G)²/G², with cubic stars giving q²/3 per element ✔. Total
  −(q²/3)Z e²𝓃_κ[𝓃_e(R) + 2𝓃̄_e]/(m_eM) ✔. This is identical to my R7 result.
- Real-space split: contact −(q²/3)Ze²𝓃_e(R) exact at all q. Uniform ℓ = 2 part: ∫_{−1}^{1}e^{−ixc}P₂(c)dc = −2j₂(x) and ∫₀^∞j₂(x)/x dx = 1/3,
  giving −(2/3)q²Ze²𝓃̄_e, independent of q ✔. The weight sits at y ~ 1/q, so expanding j₂ for small qy is invalid for the uniform part ✔.
- RPA route (independent of my R7 argument): the species Dyson equation at large ω gives R_eκ ≈ R⁰_e(−Z v_C)R⁰_κ with R⁰_s → 𝓃_sq²/(m_sω²). Its ω⁻⁴ coefficient is
  −Ze²𝓃_e𝓃_κq²/(m_eM). The ω⁻⁴ coefficient equals 𝓜³ by (4.2) plus detailed balance, ∫ω³(1 − e^{−βω})S_ab = ∫ω³[S_ab + S_ba[O†]].
  For an uncorrelated g_eκ ≡ 𝓃̄_e, (4.7′) gives exactly this (3𝓃̄_e/3), and the v2 form gives 1/3 of it ✔.
- O(q³) at T_d sites: the O(q³) part of (q·(q−G))²/|q−G|² is −2q²(q·G)/G² + 2(q·G)³/G⁴, which is odd in G. Against n_{−G} = n_G* it picks up i·Im n_G,
  which is nonzero without inversion and ∝ iq_xq_yq_z by T_d invariance ✔. It is imaginary, which is allowed because 𝓜³_eκ is not Hermitian-diagonal.
- Order of limits (§16.1 item 5): correct. For a finite sphere with qL ≪ 1, ∫P₂dΩ = 0. The κκ-face statement (a neutral, absolutely convergent sum
  keeps 𝓃_e(R)) is plausible and is flagged in G5. F4 is correctly re-opened at the 10⁻⁴ level.
§17.2 is addressed to REF-B; I note only that its content is consistent with my derivation.

## 4. New errors in changed sections
- **N1 (§6.2 (H1), W).** "Nuclei of finite size (rigid smeared charges with the form factor F^M_κ of §2)" is wrong. F^M_κ is the DM–nucleon
  form factor, which tends to f_pZ_κ + f_n(A_κ − Z_κ) at q → 0 (line 112). It depends on the DM couplings and contains neutrons. The Coulomb
  smearing that restores Spohn–Teufel H_k must use the nuclear **charge** form factor (proton distribution, Z_κF^{ch}_κ(k), F^{ch}(0) = 1).
  Fix: introduce F^{ch}_κ (new NOTATION row) in (H1) and in (1.1)'s "finite size enters only through…" sentence.
- **N2 (§9.2 (iii) and C20c, E).** "Si at finite q (𝔞_e, 𝔞_ion) = (10.7, 0.5): 1 − ε_e^{-1} = 1.32" is unsupported. The (9.4′) model sets R̃_eκ = 0
  and so makes ε_tot = 1 + 𝔞_e + 𝔞_ion. In non-polar Si, ε₀ = ε_∞ at q → 0 requires the proper cross term R̃_eκ (electrons following the ions,
  Z* = 0) to cancel 𝔞_ion. The R̃_eκ = 0 model is therefore not a description of Si, and the input 0.5 is not derived. The GaAs-like
  counterexample is enough for "false in general". Drop the Si number, or redo it with R̃_eκ ≠ 0, where the static acoustic (strain) response also enters ε_e.
- **N3 (§12, W).** Stale lines contradict the new ones. "O5 at RPA+LFE (WP1 [E3])" is still listed as closed next to "O5: closed for ch = c only".
  "OW0-8: CLOSED (F4)" still stands although G5 and F4 are re-opened. OW0-7 is listed both open and closed. Delete the superseded lines.
- No other new errors found. I checked (4.2), (4.3) (O(q³) for densities follows from n_fi = O(q) and dipole–quadrupole interference), (4.5)
  general k (relabelling i ↔ f gives the −(−1)^k sign), (4.6″), (5.5) TR statement, (5.7a), (6.3) and the b_λ bound, (8.3) ratios (1.5/1.112 = 1.35;
  2/1.276 = 1.57), and §9.2 (iii) Lehmann positivity of −v_CR(q,0).

## 5. Summary
- R7 items: 22/22 RESOLVED (18 main + 4 minor).
- Rebuttals: §17.1 (A-V4) ACCEPTED.
- §16.1 (A-V8 vs B-V6) confirmed on the side of A-V8, including the T_d O(q³) refinement.
- New errors: N1 (wrong form factor in the Theorem D smearing hypothesis), N2 (unsupported Si number in the L17 counterexample),
  N3 (stale §12 lines), all wording or estimate level. None changes a derived result.
