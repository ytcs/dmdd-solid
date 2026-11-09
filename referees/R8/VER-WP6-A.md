# R8 / VER-WP6-A: verification of returns/R8/WP6-v3.md against REF-WP6-A (R7)

What I read: WP6-v3 §0, §1.3–1.5, §3, §4, §5.1–5.1″, §6.2–6.4, §12–§14. I re-ran code/WP6-v3/checks.py: 41/41 PASS (it takes longer than 2 min).
My own checks (mpmath, < 1 min): the annual factors at 760 km/s and every Si/Ge edge number in (3.1′). Isolation was kept: no other referee files or returns were read.

## 1. Item-by-item verdicts (R7 items A-1…A-23 and sub-items)
| Item | R7 verdict | v3 action | Verdict |
|---|---|---|---|
| A-1, A-4, A-5 | STANDS | kept | RESOLVED (nothing owed) |
| A-2 orientation average | w/ corr. | (1.3a) defined with co-rotated indices. The component-wise counterexample (s_L + 2s_T)δ/3 is correct. A^{(2)} = d₂ ≥ 0 is proved | RESOLVED |
| A-3 odd ℓ, ℓ = 1, n = 2 form | w/ corr. | G_eff stated, TR/P removes all odd ℓ, no cubic ℓ = 1, lowest odd ℓ 3 (T, T_d) and 9 (O). The n = 2 form is given | RESOLVED. v3 also fixes something I missed in R7: the density odd part is O(q³) (dipole × quadrupole; the monopole has no transition element), not 2q·𝐛 |
| A-6 (V2) | w/ corr. | rewritten as a model hypothesis | RESOLVED |
| A-7…A-10 D1–D5 | CONFIRMED | kept; D4 extended with the Θ(v_esc − v_χ) typo | RESOLVED |
| A-11 uniqueness | FALLS | dropped; replaced by "local = global, μ̂ unique, η̃̂ mod ker 𝒜" | RESOLVED |
| A-12 m_min / E_th | w/ corr. | (3.1) hypothesis stated; general (3.1′); floors relabelled | RESOLVED (§3 below) |
| A-13 sensitivities | w/ corr. | exact asymmetric factors | RESOLVED. I recomputed them: v_E = 266.45 / 237.35 give ×2.218 / ×0.373; v_esc ± 25 gives ×2.26 / ×0.100 |
| A-14 edge exponent | STANDS | tangency argument and bin qualifier added | RESOLVED |
| A-15 p_on | STANDS (arith.) | replaced by the WP3-v3 table (Si TA p̄ = 3, exponent 13/2 + k; replica 5 + k) | RESOLVED for the arithmetic; the p̄ values are owned by WP3-v3 and I did not verify them |
| A-16 (P), single step | w/ corr. | monotone-column theorem, P′ stated, integrated kernels, gate, Bonferroni | RESOLVED (wording nit N4) |
| A-17 (5.1) types | STANDS | M restricted to scalars or the PSD geodesic; A only for PSD Δ | RESOLVED (an improvement) |
| A-18 (5.1′) | w/ corr. | type L named; support "⊆" fixed; positivity collapse shown; type T added | RESOLVED for every R7 point. NEW ERRORS in type T (N1, N2) |
| A-19 ×1.8 | w/ corr. | ×1.35 (M) / ×1.57 (linear); no linear limit above 0.607; IF6-9 to WP0-v3 | RESOLVED |
| A-20 recast | STANDS | qualifier and trials note added | RESOLVED |
| A-21 G8 | w/ corr. | closed under (I), (P), the monotone column and the gate | RESOLVED |
| A-22 notation | w/ corr. | 𝐊_pk, δ_θ, d_K | RESOLVED in the return. The NOTATION §M rows are still owed (IF6-2) |
| A-23 contested | STANDS | kept | RESOLVED |
| A-B3 §3.5 sizes | sub-item | 6.8 % / 13.6 %; 2.5 % against 1.170 eV | RESOLVED |
| A-D3 bound lines | sub-item | applied with rebuttal R-A1 | RESOLVED; R-A1 ACCEPTED (§2) |
| A-G (6.1), D6 | not fetched | marked UNRESOLVED | RESOLVED as a disposition (the attribution stays unverified) |

## 2. Rebuttal R-A1: ACCEPT
In R7 I said that a bound-exciton line has p_on = −1 and therefore edge exponent 5/2 + k_tail. That holds only if the line energy depends on |q| alone.
**Derivation.** Line: S(q,ω) = Z(q)δ(ω − E_l(q)). For the rate, set G(q) ≡ ω_kin(|q|) − E_l(q) with ω_kin = |q|v_max − q²/2m_χ. Then
v_max − v_min = G/|q| on the line, and η ∝ δ_v^{2+k}, so
ℛ ∝ ∫d³q Z G_+^{2+k}/|q|^{…} ≈ const·∫d^n x (ε − Σ_{i≤n} c_i x_i²)^{2+k}, with ε ∝ δ_v,0 and n the number of curved directions of G at its maximum.
The radial ∫dx (ε − cx²)^{2+k} gives ε^{5/2+k}, and each further curved direction adds ½.
- Isotropic E_l(|q|): the maximum is a sphere, n = 1, so ε^{5/2+k}. This is my R7 value.
- Cubic crystal, E_l depending on q̂: the maximum is isolated, n = 3, so ε^{7/2+k}.
In S̄ language, the q̂-average of δ(ω − E_min − cθ²) over a 2-D quadratic minimum is ∝ Θ(ω − E_min), so p̄ = 0 and (3.3) gives 7/2 + k. This is the
same +1 I used for the continuum in R7 §D3 and failed to apply to lines. With a vertex ∝ θ² (forbidden on the axis), the extra ∫θdθ θ² weight gives p̄ = 1,
hence ε^{9/2+k}.
For an indirect Si exciton at |q| ≈ 0.9 keV, E_l(q) = E_x + ħ²|q − 𝐊|²/2M_x has six isolated minima along the 𝐊 directions, so n = 3 applies.
**Verdict: ACCEPT.** My 5/2 + k is the isotropic-dispersion special case. C19 encodes all three cases.

## 3. Changed sections: checks and new errors
**General edge (3.1′): correct.**
- E_th(q)/q + q/2m ≤ v_max ⇔ m ≥ q²/[2(qv_max − E_th(q))] (with qv_max > E_th).
- Linear onset A − c′q gives the optimum q₀ = 2A/(v_max + c′) and m_min = 2A/(v_max + c′)².
- Tangency: 2E_th(q₀)/v_max² = 2A(1 − 2c′/V)/v_max² differs from the exact value only at O(c′²/v_max²). Verified.
- m_min is monotone in E_th(·) pointwise, and Si TA is sublinear (ω_TA(Q) ≤ c_TAQ). So my R7 linear construction (≈ 0.3389 MeV, recomputed) is an upper bound.
- Settlement §12 item 1 is therefore correct: E_g + ω_TA(0.53 Å⁻¹) ≈ 1.1835 eV gives 0.3370 MeV, and the replica (E_x^b = 14.7 meV) gives 0.3328 MeV.
  The floors are 0.333 and 0.329 (E_x) MeV, and Ge PAER is 0.2140 MeV. All recomputed and correct.
- ω_TA(0.53 Å⁻¹ [100]) ≈ 13.5 meV is consistent with the measured Si TA (≈ 3.3 THz near mid-zone). [E] is the appropriate tag.
- The scaling claim d ln m_min/d ln λ = 2E_th′(q₀)/v_max = −2c′/(v_max + c′) ≈ −1.5 % is correct (the text says ~1 %; the magnitude is fine).
- The validity window ω_max − E_th ≈ 2E_thδ_v,0/v_max, giving Δm/m ≲ 1–5 %, is correct.
- The corner contact ∫(ε − s|x|)^{n}dx ∝ ε^{n+1}, giving 4 + k + p̄, is correct.
**Monotone step column (4.2): correct.** With η̃ = ∫Θ(v − |u|)dν and ν ≥ 0: μ_i = ∫𝒜_i dν ≥ h·inf_{v≥u₀}𝒜_i, and
d𝒜_i/dv = ∫ΣP[A^{(0)}δ(v − |v_min|) + 2vA^{(2)}Θ] ≥ 0 under (P). The grid gate min_j Δ_j𝒜_i ≥ 0 is the exact discrete condition, and Bonferroni coverage
≥ 90 % is correct. Exothermic |v_min| is handled consistently.
**Type T (5.1″): construction correct.** The dual F(λ) is strictly convex, λ(0) = 0, and the first order reproduces Π_mom (C24 exact). It has these new errors:
- **N1 (substantive). With ψ ≡ Δ′_A/S_c, θ_A = 1 does not reproduce the template S_c + Δ′_A.** It gives S_c·exp(Δ′_A/S_c + λ·φ), which agrees only to first
  order in Δ′_A/S_c. Wherever |Δ′_A| ≳ S_c (tails; exactly the regime that broke type L), the response to θ_A is exponential, e.g. e^{2ψ} at 2σ. So
  "θ_A ~ 𝒩(0,1) scaled by η_anh" loses its meaning that one unit equals one template. *Fix:* ψ = ln(1 + Δ′_A/S_c), which requires Δ′_A > −S_c and is an
  M-type shape followed by re-tilting. θ_A = 1 then reproduces S_c + Δ′_A up to the moment re-projection, and the first order is unchanged.
- **N2 (wording error in the existence condition).** "On the bounded library grid a unique minimiser exists iff T_0 > 0 and T_2T_0 − T_1² > 0" is incomplete.
  On a support [a, b] the interior of the (1, y, y²) moment cone also requires (a + b)T_1 − abT_0 − T_2 > 0 (variance below the endpoint maximum).
  A negative θ_δ cannot violate this, but a large positive θ_δ (or a narrow grid) can.
  On unbounded support, increasing the variance needs λ₂ > 0, and this is integrable only if λ₂ is below the tail decay rate of S_c: always attainable for
  Gaussian tails, never for power-law tails. The moments then depend on the grid cutoff. State both conditions.
- **N3 (minor).** The first-order identity is Π_mom with moments of S_c. (5.1′) defines Π_mom with moments of S^τ. They differ at O(Δ^τ_A). Say which one is used.
**Other new errors.**
- **N4 (wording).** "equals h·𝒜_i(u₀) iff 𝒜_i is non-decreasing on [u₀, v_max]" is false for a single u₀: the correct condition is 𝒜_i(u₀) ≤ 𝒜_i(v) for all
  v ≥ u₀. The "iff non-decreasing" holds for the bound to hold at every u₀ simultaneously, which is what the gate tests. Rephrase.
- **N5 (editorial).** In the §14 counts paragraph, a duplicated, truncated sentence follows the first one. It gives "kept as STANDS 14", while the first gives
  "kept as STANDS/CONFIRMED 17". Delete the fragment.
No other errors were found in §1.3–1.5, §3.2–3.5, §4.1–4.4, §5.1, §6.2–6.4, or IF6-9 to IF6-17 as they concern my items.

## 4. Summary
- All 23 R7 items and the 4 sub-items are RESOLVED, with A-G remaining UNRESOLVED as a disposition.
- R-A1 is ACCEPTED.
- New errors: N1 (the type-T θ_A template meaning; fix with ψ = ln(1 + Δ′/S_c)), N2 (incomplete moment-cone condition and tail integrability), N3–N5 (minor or editorial).
- Recommended status: L24 and G8 DERIVED/REFEREED. G4 is REFEREED after N1 and N2.
