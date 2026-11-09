# R8 / VER-WP6-B: verification of returns/R8/WP6-v3.md against REF-WP6-B (R7)

Referee B, same isolation as in R7. I read WP6-v3's header, §0, all changed sections (§1, §2.3–2.5, §3, §4, §5, §6.2–6.4, §7.1/7.4 gates),
§12 rebuttals, §13 flags, §14 closing table, and code/WP6-v3/checks.py. I reran the checks: **41/41 PASS** (≈ 2 min).
No papers were re-fetched: the R7 full-text verdicts are reused unchanged.

## 1. Item-by-item verdicts (numbers = rows of my R7 verdict table)
| # | R7 item | v3 action (location) | Verdict |
|---|---|---|---|
| 1 | Halo functional (1.2) | kept; 𝔇^{(2)} = 𝒱₁†𝒱₁ made explicit | RESOLVED (stood) |
| 2 | \|v_min\| for exothermic DM | Θ(v − \|u\|) in (1.3), (4.1); C10a,b symbolic for both signs | RESOLVED |
| 3 | No cubic ℓ = 1; daily mean keeps the zonal part | (1.5): G_eff, lowest odd ℓ 3 (T, T_d) / 9 (O), ℓ = 1 only for polar G_eff; P_ℓ(cos β)K_ℓ(n̂) (C27, C28); (V3) restated | RESOLVED |
| 4 | Dictionary (1.6) | kept | RESOLVED (stood) |
| 5 | (1.7) | kept; tr[𝔇ᵀS] (WP0-v3 G1) | RESOLVED (stood) |
| 6 | Exact asymmetric finite shifts; equation-number convention | (V4) table ×2.26/×0.100, ×2.22/×0.373 (C16); HTML↔JCAP map in the header | RESOLVED (map checked against my R7 reading) |
| 7 | D1 last sentence → [E]; uniqueness REFUTED | §2.5 D1 marked UNRESOLVED/[E]; (4.2a) attribution dropped; D4 extended | RESOLVED |
| 8 | 0.333/0.212 are unattained floors; general edge formula | (3.1′) min_q q²/[2(qv_max − E_th(q))]; edge table; degeneracy qualifier | RESOLVED, but see NEW-1 |
| 9 | (3.2) gap attribution; δ ln v_max 2–7% | (3.2), (3.5) (C16, C17) | RESOLVED |
| 10 | Corner exponent 4 + k + p; validity window; "Si TA p_on = 4" not the edge | (3.3): corner case, window Δm/m ≲ 1–5% (C19, C20); WP3-v3 table, Si edge 13/2 + k_tail | RESOLVED |
| 11 | (4.1) | kept, with \|v_min\| | RESOLVED (stood) |
| 12 | Monotone column; (P) a hypothesis; CL | (4.2): d𝒜_i/dv = …[A⁰δ + 2vA²Θ] ≥ 0 (I rederived it: the δ term from A² vanishes); sufficient conditions (i)–(iii), O(ω_Q/ε_eh) leakage, library gate, Bonferroni | RESOLVED |
| 13 | dim ker 𝒜 ≥ | written | RESOLVED |
| 14 | M on matrices; A positivity; prior encodings | (5.1): M on scalars or the PSD geodesic (C22); A PSD iff Δ PSD (C23); median/σ_ln: 1.61/0.22 and 0.85/0.75 (I checked both; C25) | RESOLVED |
| 15 | (5.1′) support sentence | corrected to ⊆; equality rebutted (R-B1) | RESOLVED (rebuttal ACCEPTED, §2) |
| 16 | f-sum informative for scissor / GW–BSE rungs | (5.3) | RESOLVED |
| 17 | ×1.8 → ×1.35 / ×1.57; W_Lam | (6.2), §8, IF6-9; w_δ | RESOLVED (cosmetic residue: C8b label still says "via Lambert W") |
| 18 | Recast exact only for min-over-bins; CL | (6.4), (4.2) | RESOLVED |
| 19 | Profiling cost | (4.4): per-θ recontraction; prefix sums 7.5×10⁹ → 7.5×10⁷ (C29) | RESOLVED |
| 20 | G8 repair | §4, (7.5): closed under (I), (P), monotone column and gate | RESOLVED |
| 21 | Contested corrections (v2 §12) | unchanged | RESOLVED (stood) |
| 22 | C10 spot checks, C11 TR test, C5b numeric fallback | C10a,b symbolic; C11 tests every odd ℓ; C5b gammasimp | RESOLVED |
The NOTATION collisions of my §G (K, δ) are RESOLVED: 𝐊_pk, δ_θ and d_K are introduced, and NOTATION is flagged (IF6-2).

## 2. Rebuttal R-B1 (support of Π_mom): ACCEPT
My R7 F4 said "supp Π_mom[X] = supp X ∪ supp S^τ". Equality is false. Π_mom[X] = X − S^τ·p with p(y_R) = Σ_b c_b y_R^b fixed by the three
moment equations. The function is zero on supp X ∪ supp S^τ wherever X = S^τ·p.
Counterexample: take X = S^τ·y_R². The equations Σ_b 𝔪_{a+b}c_b = ∫y_R^a X = 𝔪_{a+2} are solved by c = (0, 0, 1), and the solution is unique
because the Hankel matrix is invertible. So Π_mom[X] ≡ 0, whose support is empty, a strict subset of supp X ∪ supp S^τ.
In general, Π_mom annihilates the 3-dimensional subspace S^τ·{1, y_R, y_R²}. Cancellation on a set of positive measure is non-generic but allowed.
Only "⊆" holds, as REF-A said. My substantive point stands unchanged: "no new support iff supp Δ′_A ⊆ supp S^τ". v3 states that condition.

## 3. New errors in the changed sections
**NEW-1 (minor-substantive): inconsistent floor in (3.1′) once exciton replicas are included.**
- The edge table gives the Si exciton-replica PAER edge as E_x + ω_TA(Q*) with E_x = E_g − 14.7 meV and ω_TA ≈ 13.5 meV. That is
  1.1688 eV, so m ≈ 0.3327 MeV.
- This lies **below** the line labelled "kinematic floor 2E_g/v_max² = 0.333 MeV (0.3330), unattained: S̄ vanishes at ω = E_g for every q
  reachable there". The replica is part of S̄ (ladder row (ii) plus the e–ph sideband), so S̄ ≠ 0 at ω = E_g for q near 0.9 keV and the
  "unattained" statement is false.
- The real floor is 2E_th^{glob}/v_max² with E_th^{glob} = E_x, i.e. 0.329 MeV. The table lists 0.329 as the "zero-phonon floor".
- Consequence (i) also cites CONTROLS C5 ("no PAER below E_g + min ω_Q"). C5 holds for the e–h continuum only; the replica violates it as worded.
- Fix:
  - label 0.333 "floor at E_g for the continuum"; the floor of the total S̄ is 0.329 MeV;
  - state that whether the replica edge falls below 2E_g/v_max² is undecided at the ±1.5 meV uncertainty of ω_TA(Q*), since the replica
    edge is 0.3327 ± 0.0004 MeV, within errors of 0.3330;
  - flag C5's scope (continuum, not bound excitons) to the coordinator.
- The same applies to Ge: E_x + ω_TA ≈ 0.7475 eV, edge ≈ 0.213 MeV, against a floor of 0.212 MeV computed at 0.744 eV; consistent, but
  label it the same way.

**NEW-2 (minor): the existence condition of type T (5.1″) is incomplete on a bounded grid.**
- v3 writes "unique minimiser iff T lies in the interior of the moment cone of supp S_c, here T_0 > 0 and T_2T_0 − T_1² > 0 (… not a
  half-line)". For support in [y_min, y_max], the interior of the moment cone also needs y_min < T_1/T_0 < y_max and the upper Hausdorff
  bound Var ≡ T_2/T_0 − (T_1/T_0)² < (y_max − ȳ)(ȳ − y_min).
- So θ_δ is bounded above on the grid. Tilting cannot push the variance beyond the support width²/4.
- In practice the bound sits many σ out, so the prior is realisable to excellent approximation. Still, "θ_A, θ_δ ~ 𝒩(0,1) realisable" and
  "not a half-line" should cite both bounds.

**NEW-3 (wording): uniqueness of μ̂ in (4.2a).** −ln ℒ is strictly convex in μ_i only for bins with N_i > 0; for N_i = 0 it is linear in μ_i.
μ̂ is unique on the bins with N_i > 0. On the zero-count bins it can vary along a face of the minimiser set. Say so explicitly; the parenthesis
already half-says it.

**NEW-4 (cosmetic).**
- The C7b label still calls 1.188 eV → 0.338 MeV the "PAER edge"; the text now says 0.337 (continuum) / 0.333 (replica), and 0.338 is the
  withdrawn E_g + ω_TA(K) value.
- The C8b label says "exact via Lambert W".
- The C18 label says the tangency is "first-order in c′", but the text (correctly) says the slope enters at second order. I checked the
  linear case: 2A/(v + c′)² = 2E(q₀)/(v² − c′²) with q₀ = 2A/(v + c′), which is second order.
- The closing-table counts are garbled: lines 686–688 duplicate the sentence with "kept 17" vs "kept 14".

**Checked and correct (new material):**
- (3.1′) and its equivalent form; the linear-onset formula 2A/(v + c′)².
- The halo–gap scaling d ln m_min/d ln λ = 2E_th′/v_max. Rederived by substituting q = λq′: only E_th(λq′) changes, and ∂ln m/∂E ≈ 1/E at
  the optimum.
- Si and Ge edge numbers: 1.1835 eV → 0.337 MeV, 1.1553 eV → 0.329 MeV, 0.474 MeV for X0 at the pocket.
- The validity window, 0.4–2.5% in δ_v,0/v_max, i.e. 1–5% in Δm/m.
- The p̄_on/k_tail ω-shape qualifier (ω − E_th)^p(ω_max − ω)^{5/2+k}.
- The PSD geodesic (congruence of a PSD power, with the support condition stated); "A PSD ∀a > 0 iff Δ PSD".
- The ×1.35 / ×1.57 ratios and the δ_θ > 0.607 no-limit statement.
- The Bonferroni coverage argument; the prefix-sum cost.
- The daily mean P_ℓ(cos β)K_ℓ(n̂) (addition theorem).
- The orientation average (1.3a) vs the component-wise average ((s_L + 2s_T)δ/3, C26).
- d𝒜_i/dv and the monotone-column bound.
I did not verify claims owned by other packages and only relayed here (WP3-v3 p̄_on table, WP1-v3 [E13] window, WP4-v3 O(q³) odd part,
WP5-v3 priors). The [E] reading ω_TA(0.53 Å⁻¹, [100]) ≈ 13.5 ± 1.5 meV agrees with my recollection of the measured Si dispersion
(≈ 12–14 meV).

## 4. Summary
All 22 R7 items are RESOLVED. R-B1 is ACCEPTED. There is one minor-substantive new error, NEW-1: the Si/Ge exciton-replica edge lies at or
below the "unattained" E_g floor, and C5 needs its scope stated. NEW-2 and NEW-3 are minor, and NEW-4 is cosmetic.
Recommended status for WP6-v3: STANDS WITH CORRECTION (NEW-1 to NEW-3); no item FALLS.
