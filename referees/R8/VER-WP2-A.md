# R8 / VER-WP2-A: verification of returns/R8/WP2-v3.md against REF-WP2-A (R7)

Referee A, same isolation as R7: I read only WP2-v3 (closing table §16 and the changed sections §0, §2, §3.3–3.6, §5.1–5.2″, §6.1, §7.1,
§9, §12–§15) and code/WP2-v3/checks.py. I re-ran checks.py: **31/31 PASS**. I did not read REF-WP2-B or SOTA, so I take the B-items and the
REF-WP0-A/REF-WP5-A cross-notes cited by v3 at face value; I checked them only where they change WP2 formulas.

## 1. Item-by-item verdicts (R7 items A-1 … A-30)

| R7 item | R7 verdict | v3 action | Verdict |
|---|---|---|---|
| A-1 reduction (1.1)–(1.2) | STANDS | kept; B-1's O(2W) vertex-DW bookkeeping added (C14) | RESOLVED (the addition is correct: ⟨1∣e^{iq·u}∣0⟩ = iq·⟨1∣u∣0⟩e^{−W}) |
| A-2 coherent S (2.2) | STANDS | citation slips fixed, statuses marked | RESOLVED |
| A-3 T > 0 shell sum wording | W/ CORR | "absolutely divergent, a lattice Fourier sum" (§2, §12 gap 3) | RESOLVED |
| **A-4 BZ-average theorem (2.4)** | W/ CORR | all inter-sublattice ΔR with j_BZ(ΔR + r_κ − r_κ′); Bravais-only identity; C9 re-described; C9b, C9c; hypothesis q ≫ max(n_ph, 2W_κ)q_BZ | **RESOLVED** (see §2a) |
| **A-5 2607.24933 Eq. (47)** | W/ CORR | caveat quoted; intra-cell charge withdrawn; claim limited to polarisation weights | **RESOLVED** |
| A-6 incoherent S | STANDS | kept | RESOLVED |
| A-7 truncation loss | STANDS (+ species form) | (3.4″) species-weighted; signed-moment and multiplicative-vertex qualifiers; C3d | RESOLVED (formula correct) |
| A-8 Panjer (3.5) | STANDS | kept; T > 0 numerical route changed to FFT of e^{−2W}[e^Φ − 1] | RESOLVED (the change is correct: at T > 0 the bin equation is not triangular) |
| A-9 Sherman–Morrison | STANDS | kept, hypotheses explicit | RESOLVED |
| A-10 1712.06598 Eq. (5) | STANDS | kept, CONFIRMED | RESOLVED |
| A-11 1712.06598 Eq. (12) | W/ CORR | "declared rough estimate, negligible" | RESOLVED |
| A-12 (4.3)–(4.5) | STANDS | kept | RESOLVED |
| A-13 cumulants (5.1) | STANDS | kept | RESOLVED |
| A-14 2205.02250 "peak" | W/ CORR | discrepancy dropped; recorded as a clarification (§5.1, L6, §13, IF-14) | RESOLVED |
| A-15 GS/X split (5.2) | STANDS | kept; a remark that 𝔨₃^{GS} must be computed directly, never as 𝔨₃ − 𝔨₃^X | RESOLVED (remark correct: the O(𝔨₁/ΔE₃) error relative to 𝔨₃ is ×8×10⁵ relative to 𝔨₃^{GS}) |
| A-16 (5.2′) closed form | STANDS | kept; neutral V_eN + V_NN precision; renamed 𝓜³_κκ∣^{self}_pot | RESOLVED (precision correct: the electron-only field gradient is conditionally convergent) |
| **A-17 κκ/eκ relation** | W/ CORR | q a_1s qualifier; new (5.2″) with Δ𝓃_κ(q); C11e–g; "exactly"/"at contact" withdrawn; IF-1 rewritten | **RESOLVED** (see §2b) |
| A-18 free recoil chain | STANDS | kept; hep-ph/0608035 quote marked UNRESOLVED | RESOLVED |
| A-19 (6.1) normalisation | W/ CORR | factor (2π/Ω)∣c_κ∣² = 2π𝓃_κ∣c_κ∣² added; C12b | RESOLVED |
| A-20 toy 𝔨₃ | STANDS | kept | RESOLVED |
| A-21 2309.10839 e^{−W} | STANDS | kept, CONFIRMED | RESOLVED |
| A-22 spin channel | STANDS (+ n_ph ≥ 1) | S̃_self starts at n_ph ≥ 1; isotope-mass caveat O(ΔM/M) on the identification | RESOLVED |
| A-23 currents | STANDS | kept | RESOLVED |
| A-24 (8.1), selection rules | STANDS | kept | RESOLVED |
| A-25 cubic isotropy | STANDS | kept | RESOLVED |
| A-26 2411.03433 IA width | W/ CORR | "declared approximation" (§8.2(iv), L19, §13) | RESOLVED |
| A-27 LIMITS entries | W/ CORR | L5 chain uses all-ΔR κ ≠ κ′; L6 clarification; IF-14 to LIMITS/WP0 | RESOLVED |
| A-28 gap closures | STANDS | G13 contraction tagged [D, sketch]; G3 cells at q ≲ n_ph q_BZ flagged | RESOLVED |
| A-29 consistency with WP0-v2 (4.7) | W/ CORR | q → 0 qualifier; (5.2″) | RESOLVED |
| A-30 contested corrections | STANDS | §14 now settles 8 A/B disagreements; no rebuttal of A | RESOLVED |

**Count:** 30/30 RESOLVED, 0 NOT RESOLVED, 0 NEW ERROR in the A-items.

## 2. Checks of the changed sections

**(a) (2.4) and its gradient terms.**
- Σ_ΔR j_BZ(ΔR + d) = (Ω/(2π)³)∫_BZ Σ_R e^{−ip·(R+d)} = Σ_{G∈BZ} e^{−iG·d} = 1 (Poisson summation; only G = 0 is inside). ✓
- 1D diatomic: j_BZ(na + a/2) = (−1)ⁿ/(π(n + ½)). ✓ (I derived this independently in R7.)
- 1D self-term gradient: ⟨(1 + p/q)^{2n}⟩_BZ − 1 = C(2n,2)⟨p²⟩/q² = n(2n − 1)q_BZ²/(12q²), using ⟨p²⟩ = (π/a)²/3 = q_BZ²/12. ✓ The linear term
  vanishes for the self term (inversion-symmetric BZ) but not for the cross terms. ✓
- So the hypothesis q ≫ max(n_ph, 2W_κ)q_BZ is the right one, and it is stricter than my R7 "O(q_BZ/q)". I accept B's scale.
- The size estimate 4 × 0.44 × 0.3² ≈ 0.16 is labelled "up to" and [E]. That is acceptable. It ignores the e^{−iq·d} phases, which can only
  reduce the size.

**(b) (5.2″), new material.**
- Sign and normalisation: (q̂·∇)²(1/4πρ) = −δ³/3 + PV(3c² − 1)/(4πρ³), and the ℓ = 2 part of e^{−iq·ρ} is −5j₂P₂. Together these give
  ⟨e^{−iq·ρ}(q·∇)²U⟩ = −(Z e²q²/3)[𝓃(0) + Δ𝓃], with Δ𝓃 = 6∫𝓃(ρ)j₂(qρ)dρ/ρ for a spherical density. So the "+Δ𝓃" in (5.2″) is right. ✓
- Uniform part: ∫₀^∞ j₂(y)dy/y = 1/3 (mpmath 0.329 on an oscillatory quadrature; exact value √πΓ(1)/(4Γ(5/2)) = 1/3), so Δ𝓃 = 2𝓃_e. ✓
  - Si: 2𝓃_e/𝓃_e(R) = 1.4 Å⁻³/1.1×10⁴ Å⁻³ ≈ 1.2×10⁻⁴. ✓
  - The q → 0⁺ non-analyticity statement is correct.
- Hydrogenic closed form 𝔯(ξ) = 3 + 3/ξ² − 3(1 + ξ²)arctan ξ/ξ³:
  - Series 1 + 2ξ²/5 = 1 + (qa)²/10. ✓
  - Independent mpmath quadrature of 1 + 6∫e^{−2ρ}j₂(2ξρ)dρ/ρ gives 1.0906, 1.2876, 1.6741 at ξ = 0.5, 1, 2, equal to the closed form. ✓
  - Si values 9.0% at 51 keV and 28.7% at 102 keV ✓ (ξ = 0.5, 1 with 1/a_1s = 51.1 keV).
- The G ≠ 0 anisotropic finite-q term "≲ 10⁻⁴" is tagged [D, sketch / E]. That is acceptable, but the tag must stay.

**(c) GS f-sum with the Migdal prescription (§3.4, IF-2).** X first moment = E^{Mig}_1 + P_Mig q²/2M. The GS share is
(1 − P_Mig)q²/2M − E^{Mig}_1 = (1 − P_Mig)q²/2(M + δM) + O(P·δM/M, (δM/M)²). ✓ This is to first order, as stated.

**(d) Shell numbers (§3.3).**
- q = 10 keV: q∣d∣ = 11.9, j₀ = 0.052, 4 × 0.052 × 0.09 = 1.9%. ✓
- q = 2 keV: q∣d∣ = 2.38, j₀ = 0.29, giving 10.4%. ✓
- Envelope 4c̄²/(q∣d∣) ✓.

**(e) (3.5) at T > 0.** The time-domain uniqueness statement (∂_tŜ = Φ̇Ŝ fixes Ŝ up to normalisation) and the FFT route are correct.
The degeneracy at ω = 0 is correctly identified.

## 3. New errors
None that changes a result. Two wording points (no verdict change):
1. §0 item 3 and §13: "Eq. (47) is not used in their numerics" is a statement about 2607.24933. It agrees with my R7 reading (their numerics
   are the 1D N-site model), but v3 should tag it [FT] like the other source claims.
2. (6.1): the identity (2π/Ω)∣c_κ∣² = 2π𝓃_κ∣c_κ∣² assumes one κ site per cell. Write 𝓃_κ = (number of κ sites per cell)/Ω, or sum over sites.

## 4. Verdict
All R7 REF-WP2-A items are RESOLVED, with no NEW ERROR. The two revised focus results are correct as now stated:
- the BZ-average theorem: Bravais-only identity, asymptotic in q ≫ max(n_ph, 2W_κ)q_BZ;
- the κκ/eκ third-moment relation: exact for the contact term, and q a_1s ≪ 1 plus O(10⁻⁴) for the full moments.
The two wording points in §3 are optional.
