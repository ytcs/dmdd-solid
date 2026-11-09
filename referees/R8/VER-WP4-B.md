# R8 verification VER-WP4-B, on returns/R8/WP4-v3.md (referee B of R7)

Read: WP4-v3 §0, §3, §4, §5, §8, §11, §11A, §12, §13, and code/WP4-v3/checks.py (run: 34/34 PASS). I also ran an independent mpmath
quadrature of 𝔰_BCS (scratchpad, < 1 min). Same isolation as R7: no other referee reports, state/ or other returns were read.

## 1. Item-by-item status of REF-WP4-B (R7)
| R7 item | v3 action | Verdict |
|---|---|---|
| V1 OW4-2, ε_bg² (both papers) | §5.3 is now a firm claim; [5.3] exact for any δε_D; K22 | RESOLVED |
| V1/§A4 absorption factor κ | §5.5 [5.4]–[5.5], K24: ×ε_bg (×ε_bg,ii per polarisation) | RESOLVED. It agrees with my A4 derivation |
| V2 L16 chain, 2101.08263 Eq. (4) | unchanged | RESOLVED (stood) |
| V3 typo also in 1910.02091 (3.13) | §5.1, §5.2 | RESOLVED |
| V4 L15 chain, K2 | unchanged | RESOLVED (stood) |
| V5 𝔤_I reading of 2609.06423 | sentence replaced ("Reading of 𝔤_I"); the O(Δ²) part rebutted (R-2) | RESOLVED. See [4.2′] in §3 for a new caveat |
| V6 0.13 keV → eV | §4.3, K16 | RESOLVED |
| V7 2101.08263 Eq. (3) | kept | RESOLVED |
| V8 1512.04533 e₋ | kept | RESOLVED |
| V9 2609.06423 time-ordered | Eq. (4) dropped as a defect; (7)–(8) rebutted (R-3); usage remark kept | RESOLVED (R-3 accepted, below) |
| V10 reality, not causality | §4.3 (c), for both the source and WP4 | RESOLVED |
| V11 acausal-branch mechanism | mechanism withdrawn; "suppresses" stated | RESOLVED |
| V12 Mermin validity, QROCODILE, tautological K11, WSi numbers | [4.4] restricted to q ≪ k_F, k_TF; asymptote caveat added; QROCODILE claim dropped; K11 now derives both limits from [4.3]; WSi declared out of validity (K31) | RESOLVED. I checked that K11 now expands 𝔣_Lin = 1 − (z/u)artanh(u/z) |
| V13 reciprocity | unchanged; "necessary only" added (from A) | RESOLVED |
| V14 density odd part O(q³) | [3.2′], K26; [3.2] kept for the j and s rows | RESOLVED. The argument is correct: only the αβ-symmetric (P,T-odd) part of b^{NR} survives q_αq_β, and γ_OA drops out |
| V15 chiral [3.3] | unchanged; sign convention stated (I9) | RESOLVED |
| V16 N_qp = 2 to 4Δ_BCS | §4.6, K27 | RESOLVED |
| V17 D-g (a) cross terms | (G5) and [8.1] with a Duhamel bound, K30 | RESOLVED in form. **NEW ERROR** in the size of the hypothesis (§3 N2) |
| V18 L13 chain | unchanged | RESOLVED (stood) |
| V19 gap closures | unchanged | RESOLVED (stood) |
| V20 credit 2609.06423 for Δ²/(v_FQ)² ≤ 1/25 | §4.2 step 3, RG1 | RESOLVED |

## 2. Rebuttals addressed to me
**R-2 (O(Δ²) screening statement): ACCEPT.** My R7 B2 used v2's assertion Re ε^{BCS} = Re ε^{nor}[1 + O(Δ²/v_F²q²)] as the content of 2609.06423's
|ε|² agreement. I did not derive it myself. I re-derived [4.2′]. In the DM region δIm ε(ω′) = Aω′[𝔤_I(y′)Θ(y′ − 2) − 1], with
A = (π/2)k_TF²/(q³v_F). KK gives
  δRe ε(ω) = (2/π)P∫dω′ ω′δIm ε/(ω′² − ω²) = (2/π)AΔ_BCS·𝔰_BCS(y),
and dividing by Re ε^{nor} = k_TF²/q² gives (Δ_BCS/qv_F)𝔰_BCS(y). This is first order. The integrand decays as y′⁻² because
𝔤_I − 1 ≈ (2ln 2y − 1)/y², so the cutoff at ω′ ~ qv_F contributes only at O(Δ²/q²v_F²). My independent quadrature gives:
- the sum rule ∫₀^∞[𝔤_IΘ(y − 2) − 1]dy = 0, to 7×10⁻⁹ (limited by the asymptotic tail), so 𝔰_BCS(0) = 0;
- 𝔰_BCS(5) = 1.053, 𝔰_BCS(10) = 0.501 and 𝔰_BCS(20) = 0.248, which confirms both "1.05" and "≈ 5/y".

This also explains 2609.06423's Fig. 2 statement that |ε_BCS|² and |ε_Lin|² deviate "near the edge of the energy gap": 𝔰_BCS has a log
divergence at y = 2. So R-2 is right, and the v3 replacement is right.

**R-3 (2609.06423 Eqs. (7)–(8) as a retarded ε): ACCEPT.** The first pole term is identical in both prescriptions. In the second term,
1/(ω + Ω − i0) − 1/(ω + Ω + i0) = 2πiδ(ω + Ω), with Ω = E + E′ ≥ 2Δ > 0, so it vanishes for every ω > 0. Hence Π^T(ω) ≡ Π^R(ω) for ω > 0,
complex value included, and ε_BCS and Im ε/|ε|² at ω > 0 are exactly the retarded ones. R7 already said the numbers were unaffected.
Calling the use a "defect" was too strong, because the paper never leaves ω > 0 and T = 0. The usage remark (ω < 0, KK, T > 0) is the
right residue.

**R-4 (the "κ² growth" reading): ACCEPT.** With Re ε_r = (α̃/6π)ln((2v_FΛ′_D)²/|𝓈|) in both theories:
- the source has 1/|ε_r|² = (6π/α̃)²/|𝓛′_D|², with an explicit prefactor ∝ ε_bg²;
- the URF has 1/(ε_bg²|ε_r|²), where α̃ε_bg = αg_deg/v_F carries no ε_bg.

So the explicit ε_bg² in 1708.08929 Eq. (3.14) is exactly the omitted factor, and the Λ′ rewrite is common to both theories. v2's sentence
explained the discrepancy by the rewrite, which is wrong. My R7 statement was correct about the asymptotics: the apparent κ² growth is
offset by 𝓛′_D ∝ ε_bg. It was wrong to endorse v2's sentence as the explanation of the discrepancy. K23 is consistent with this.

## 3. New errors and caveats in the changed sections
**N1. [4.2′]: first-order screening near threshold [D sketch, incomplete scope].** In §0, §4.3 and I12 the effect on L is given only at
y = 5 and y = 10. At the Al kinematic edge, q = ω/v_max, my quadrature of |δL/L| = 2(v_max/v_F)𝔰_BCS(y)/y gives:

| y | 2.2 | 2.5 | 3 | 5 | 10 |
|---|---|---|---|---|---|
| \|δL/L\| | 1.42 | 0.88 | 0.53 | 0.16 | 0.04 |

So for y ≲ 3.5 near the edge the first-order term is O(1). The expansion [4.2′] fails there, and L^{BCS} = 𝔤_I L^{nor} is uncontrolled. This
is the region where the 𝔤_I step (π/2) matters most. The sign is a suppression. Required: state the validity of [4.2′] as
2(Δ_BCS/qv_F)𝔰_BCS ≪ 1. Near threshold at small q, use the full KK of Im ε^{BCS}, or quote the threshold region as uncontrolled. Then
amend I12, which currently reads "≤ 16%", to state this. The "≤ 16% at ω = 5Δ_BCS" in §0 is correct as written.

**N2. (G5)/[8.1]: the operator-norm hypothesis is vacuous in the thermodynamic limit, and 𝔥_off ~ Γ_qp + Γ_ph is not justified.** The
Duhamel bound and c_g = 1/π are right (K30). The bound ‖f_Δ(A) − f_Δ(B)‖ ≤ (1/2π)∫|ĝ(Δt)||t|dt‖A − B‖ = c_g‖A − B‖/Δ² holds. But
‖H_off‖ for an interacting extensive H scales with volume, so the hypothesis ‖H_off‖ ≤ 𝔥_off with 𝔥_off intensive fails for bulk targets.

The fix is the state-restricted Duhamel form,
  ‖(f_Δ(ω − H) − f_Δ(ω − H_d))O_b|i⟩‖ ≤ (1/2π)∫dt|ĝ(Δt)||t| sup_{|s|≤|t|}‖H_offe^{−iH_ds}O_b|i⟩‖,
which needs only an intensive 𝔥_off on few-quasiparticle states.

Even then, golden-rule counting gives ‖H_offψ‖² = Σ_f|⟨f|H_off|ψ⟩|² ≈ ∫dE Γ_qp(E)/2π over the final-state bandwidth W. So
𝔥_off ~ (Γ_qpW)^{1/2} ≫ Γ_qp, not 𝔥_off ~ Γ_qp. With that size, [8.1] demands Δω_bin ≫ (Γ_qpW)^{1/2}. That is far stricter than the bin
condition (c), Δω_bin ≫ Γ, so "(G5) is the quantitative content of (c)" is not established. Required:
- restate (G5) on the relevant states;
- retag "𝔥_off ~ Γ_qp + Γ_ph" as [C], or replace it with (Γ_qpW)^{1/2} [E];
- say that [8.1] is sufficient but loose, and that (c) stays [C].

**N3 (minor). §5.3 "×640 for its ZrTe₅ curve".** This is right as the source's own isotropic-κ̃ (harmonic-mean) rate ratio. The true
ZrTe₅ URF rate is direction-dependent via (q̂·ε_bg·q̂)², so ×640 should be labelled "for the source's isotropised model".

No other new errors were found. I checked: §5.4 (i) ∫x(1−x)ln[1/(x(1−x))] = 5/18, giving 0.349 and the factor 0.55; §5.5 K24; K29
(q* = 10 keV, v_max/v* = 0.265); K27; [3.2′]/K26.

## 4. Summary
- 20/20 R7 items are RESOLVED.
- R-2, R-3 and R-4 are all ACCEPTED.
- There are two new issues: N1 ([4.2′] is O(1) near threshold at the kinematic edge; state its validity) and N2 ((G5) uses an
  operator-norm size that is vacuous in bulk, and the 𝔥_off ~ Γ estimate is unsupported).
- N3 is a minor labelling point.
