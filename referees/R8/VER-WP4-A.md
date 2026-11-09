# R8 / VER-WP4-A: verification of returns/R8/WP4-v3.md against REF-WP4-A (R7)

Referee A, same isolation as R7. Read: WP4-v3 §0, §3, §4.2–§4.6, §5, §7, §8, §11, §11A, §12, §13. Ran code/WP4-v3/checks.py: 34/34 PASS.
Independent mpmath check (in sympy) of the new [4.2′] coefficient 𝔰_BCS. No literature was re-fetched: every full-text fact used here was
verified in R7.

## 1. Item-by-item verdicts (R7 items A-V1 … A-V23, plus A §2.3)
| R7 item | Verdict | Note |
|---|---|---|
| A-V1 OW4-2, ε_bg² (firm) | RESOLVED | §5.3 is firm. [5.3] ratio = ε_bg² exactly. The explanation is replaced: Λ′_D = Λ_De^{3π/α̃} is common to both theories, and ½(6π/α̃)² = 288π⁴κ²v_F²/(e⁴g²) (checked). The ε_bg,ii² per principal axis is right: for q ∥ x, F_src = 1/(1 + v_x²π/κ_xx) against κ_xx/(κ_xx + v_x²π) |
| A-V1′ absorption ×ε_bg | RESOLVED | [5.4]: m² − Π_γ = m²ε at ω = m, so Γ = κ_mix²m Im ε/\|ε\|² = κ_mix²m Im ε_r/(ε_bg\|ε_r\|²). The source gives Im ε_r/\|ε_r\|², hence the ratio ε_bg. Correct. "Not propagated to their plotted curves" is stated honestly |
| A-V2 | RESOLVED | — |
| A-V3 direction | RESOLVED | q ∥ y larger; 366 / 221 |
| A-V4 scheme spread | RESOLVED | 0.35/0.55 vs 0.27/0.62 |
| A-V5 credit 2609.06423 Π_θ | RESOLVED | §4.2 step 3 credits it, and the §14 novelty sentence is removed |
| A-V6 𝔤_I | RESOLVED | Novelty marked UNRESOLVED (OW4-3). New asymptote 𝔤_I − 1 = (2ln2y − 1)/y²: I confirm it numerically (y = 200: 10.9833 vs 10.9829 for y²(𝔤_I − 1)) |
| A-V7 5Δ misattribution | RESOLVED | The "Reading of 𝔤_I" paragraph is correct |
| A-V8 4Δ | RESOLVED | The recombination remark is right: a 2Δ phonon re-breaks exactly one pair |
| A-V9, A-V10 | RESOLVED | — |
| A-V11 time-ordered, not a defect | RESOLVED | — |
| A-V12 reality vs causality | RESOLVED | — |
| A-V13 Mermin | RESOLVED | Derivation added. The q ≪ k_F, k_TF domain (REF-B's point) is compatible with my algebra |
| A-V14 QROCODILE | RESOLVED | The claim is withdrawn and the WSi factor dropped. K31 numbers are right (k_F = 2.67 keV, k_TF = 3.56 keV) |
| A-V15 "iff" | RESOLVED | — |
| A-V16 γ_OA sign convention | RESOLVED | Flag I9 (dependence on the WP0 contraction order) is correct and useful |
| A-V17 D-g (a) hypothesis | RESOLVED, with NEW ERROR N1 | (G5) and [8.1] are added and the bound is proved correctly. But the stated size of 𝔥_off is wrong (§3, N1) |
| A-V18 | RESOLVED | — |
| A-V19 0.13 eV; Q₊ < 1 | RESOLVED | Rebuttal R-1 ACCEPTED (§2) |
| A-V20 exothermic example | RESOLVED | (1 MeV, 50 eV): v* = 0.010, v_max/v* = 0.265, q* = 10 keV. In Si, x_R = 10⁸/(2·26.2 GeV·40 meV) = 0.048. Correct |
| A-V21, A-V22 | RESOLVED | — |
| A §2.3 Re ε^{BCS} order | RESOLVED, by replacement | Rebuttal R-2 ACCEPTED, with a size caveat (§2, §3 N2) |

## 2. Rebuttals addressed to REF-A

**R-1 (A-V19 mass threshold): ACCEPT.** At fixed q the largest DM energy loss is ω_max(q) = qv_max − q²/2m_χ. Q₊ < 1 ⇔ ω < qv_F − q²/2m_e.
So Q₊ < 1 holds for all ω ≤ ω_max(q) iff q(1/m_e − 1/m_χ)/2 < v_F − v_max, i.e. q < 2k_F(1 − v_max/v_F)(1 − m_e/m_χ)⁻¹ ≈ 4.24 keV (Al, m_χ ≫ m_e).
Reachable momenta extend to q ≈ 2m_χv_max, which equals 4.24 keV at m_χ = 4.24 keV/(2·2.65×10⁻³) = 0.80 MeV. My "m_χ ≳ 3 MeV" used a typical
v instead of v_max, so it marks where the failure covers most of the halo, not the threshold. v3's two-part statement (§4.3) is right.

**R-2 (A §2.3, "tag [D, sketch] or cite"): ACCEPT.** v3 replaces the asserted "Re ε^{BCS} = Re ε^{nor}[1 + O(Δ²/v_F²q²)]" with [4.2′]. Check: with
Im ε^{nor} = A ω, A = (π/2)k_TF²/(q³v_F), the KK integral
δRe ε(ω) = (2/π)P∫dω′ ω′ δIm(ω′)/(ω′² − ω²), with ω′ = Δy′, gives (2/π)AΔ·𝔰_BCS(y) = Re ε^{nor}·(Δ/qv_F)·𝔰_BCS(y), using Re ε^{nor} ≈ k_TF²/q².
This is first order, as claimed. Since L = Im/Re², δL/L = −2(Δ/qv_F)𝔰_BCS. My independent quadrature (closed-form 𝔤_I, PV by subtraction, analytic tail
(2ln2Y + 1)/Y beyond Y = 1000) gives:
- 𝔰_BCS(0) = −7×10⁻⁹ (tail-limited; zero within accuracy). So the static sum rule ∫₂^∞(𝔤_I − 1)dy = 2 holds.
- 𝔰_BCS(3) = 2.03, 𝔰_BCS(5) = 1.053, 𝔰_BCS(10) = 0.501, 𝔰_BCS(20) = 0.248 (so ≈ 5/y for y ≳ 10, as stated).
- Bound: in the DM region Δ/qv_F ≤ v_max/(y v_F), so |δL/L| ≤ 2·0.39·1.053/5 = 0.164 at y = 5. Confirmed.
Physically, the case-I step moves Im weight from [0, 2Δ] to just above 2Δ, and its KK image is O(Δ/qv_F). The vanishing static coefficient expresses the
unchanged compressibility. My R7 request is superseded by a better result. The size caveat is N2 below.

**R-3, R-4** are addressed to REF-B. **§11A-1 and §11A-2** side with REF-A; I checked the derivations given (K23, K25) and they are correct. On
**§11A-3**, I accept REF-B's domain restriction (q ≪ k_F, k_TF; the formula is an asymptote, so 0.79 at qℓ = 1.5 is not applicable). It does not
contradict my algebra.

## 3. New errors and weaknesses in the changed sections
**N1 (§8 (G5), [8.1]): the size of 𝔥_off is wrong. NEW ERROR (moderate, in an [E] identification; the theorem's algebra is right).**
(a) The Duhamel bound itself is correct: f_Δ(A) − f_Δ(B) = (1/2π)∫dt ĝ(Δt)(e^{iAt} − e^{iBt}) gives c_g = (1/2π)∫|s||ĝ|ds, which is 1/π for a
Gaussian, and Σ_{n,m}S^{(n,m)} = ⟨O_a†f_Δ(ω − H_d)O_b⟩ because f_Δ(H_d) is block-diagonal.
(b) The trouble is the size. As written, (G5) is an operator norm, ‖H_off‖ ≤ 𝔥_off. For a many-body H with local e–ph and e–e terms, ‖H_off‖ is
**extensive** (∝ volume), so the bound is vacuous.
(c) The repair is a state-restricted Duhamel bound: ‖(e^{iHt} − e^{iH_dt})ψ‖ ≤ |t| sup_s‖H_off e^{iH_ds}ψ‖ with ψ = O_b|i⟩. That needs
𝔥_off ≡ sup_s‖H_off e^{iH_ds}O_b|i⟩‖/‖O_b|i⟩‖.
(d) Even then "𝔥_off ~ Γ_qp + Γ_ph" is wrong. For a state φ that decays by the golden rule into a continuum of width W_c,
‖H_offφ‖² = Σ_f|V_f|² = (Γ/2π)·W_c. So 𝔥_off ~ √(ΓW_c/2π) ≫ Γ.
(e) Consequence: the norm bound [8.1] demands Δω_bin ≫ √(ΓW_c), parametrically stricter than the bin condition (c), Δω_bin ≫ Γ. "(G5) is the
quantitative content of (c)" is therefore false. Either restate (c) as Δω_bin ≫ 𝔥_off with 𝔥_off the state-restricted second-moment
quantity, or keep Δω_bin ≫ Γ as a separate [C] (a resolvent/golden-rule estimate would give cross terms O(Γ/Δω_bin), but that is not
what the Duhamel bound proves). K30's 2×2 tests cannot detect either issue (no extensivity, no continuum).

**N2 ([4.2′] size at the kinematic edge): weakness, tag the number [E].** 𝔰_BCS integrates y′ to ∞. The actual KK range ends at
ω′ ≈ qv_F, where Im ε^{nor} stops being linear, i.e. at Y = qv_F/Δ. At the edge q = ω/v_max quoted for the 16%, Y = y v_F/v_max ≈ 13
(y = 5). The omitted tail ∫_Y^∞ y′²(𝔤_I − 1)/(y′² − y²)dy′ ≈ (2ln2Y + 1)/Y ≈ 0.58 is comparable to 𝔰_BCS(5) = 1.05. This "second-order"
remainder, O((Δ/qv_F)²·ln(qv_F/Δ)) relative, is not small at the edge: there the effect is 8–16%, not "≤ 16%" as a firm number. The
first-order statement and the sum rule stand. The cutoff effect is the same size as REF-B's warning about the Lindhard nonlinearity near qv_F.
Write "≈ 0.1 (8–16%) at y = 5 at the edge [E]".

**N3 (minor, §0 L15 row and I12).** The sign of the screening term is not stated in words. Since 𝔰_BCS > 0 for y ≳ 3 (checked at 3, 5, 10, 20; near y = 2 the log singularity needs its own statement), screening in the superconductor is stronger and L^{BCS} < 𝔤_IL^{nor}. Say so, because WP5/WP6 nuisances need the direction.

No error found in: §5.3 (both the derivation and the Λ′ algebra), §5.5, [3.2′] (continuity ω²S_nn = q_αq_βS_jj, odd part
2q^αq^βq^γb_{(αβγ)}/ω², ℓ = 1 and 3), K25, K27, K28, K29, K31, the 4Δ derivation, or the Mermin rebuild.

## 4. Summary
All 23 R7 items plus A §2.3 are RESOLVED. Rebuttals R-1 and R-2 are ACCEPTED (R-2 improves on my request). One new error, N1: (G5)'s operator
norm is extensive, and 𝔥_off ~ Γ underestimates the state-restricted norm, which scales as √(ΓW_c), so "(G5) = bin condition" is false.
One weakness, N2: the 16% figure in [4.2′] has an O(50%) cutoff uncertainty at the edge. One minor item, N3: state the sign of the
screening term.
The L16 ε_bg² (scattering) and ε_bg (absorption) statements are correct as written and may go to LIMITS.
