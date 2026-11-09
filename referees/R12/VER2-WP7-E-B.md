# R12 re-verification VER2-WP7-E-B of returns/R12/WP7-E-v3.md (+ code/WP7-E-v3/checks.py) against referees/R12/VER-WP7-E-B.md

Same isolation as before. Read: WP7-E-v3 §0–§3.2, §5, §6, the closing table; ran checks.py (47/47 PASS). Re-derived (E7), (E13), the r-shift and the bounds by
hand. Ran a sympy/Monte-Carlo test of the bound inequality (scratchpad, < 1 min; no physics simulation). No new literature fetch: the quotes checked in VER are
unchanged, and the new 2007.14289 threshold quote matches what I read in R12.

## Verdicts on VER-WP7-E-B items
| Item | Verdict | Note |
|---|---|---|
| N1 additive O(1) sensor loss | RESOLVED | (E7) E_sig = ϵ_prim(ω − D′) + ϵ_NTL·NTL. D′ is pre-sensor only. The absolute loss cancels (C7a). (E8), (E13) and A-4 are now first order in small d′, δ. Re-derived: η = (1+g)[(1−δ)(1−d′_NR) + rgy]/(1 − d′_ER + rg) − gy |
| N1 (missing (1−κ)X_ER) | RESOLVED | (E13) d′_NR − κd′_ER = [E_st + ΔX + (1−κ)X_ER]/ω (C7d) |
| N1 sign premise of bounds | RESOLVED, with one caveat (below) | conditions (B-a) Δϵ ≥ 0, (B-b) r ≥ 1, (B-c) X_NR ≥ κX_ER stated |
| N2 central values labelled as bounds | RESOLVED | Si 0.055/(0.4·0.65) = 0.212, p_surv ≲ 0.47; Ge 0.0644/(0.4·0.8) = 0.201, p_surv ≲ 0.66; central values 0.18/0.19 relabelled |
| N3 exciton bookkeeping | RESOLVED | explicit E_X = Σ(E_g − E_x^b); E_pairs over unbound carriers. (E1-pr) → (E1-W4) re-derived: N_e^f(E_c−μ_F) + N_h^f(μ_F−E_v) = N_e^fE_g + E_pairs^{unp}, and E_X = N_XE_g + E_x. μ_F cancels under neutrality (C13b). Ledger and A-1 now agree |
| N4 1803.02903 collection-efficiency reading | RESOLVED | field/model ratio; used only as a one-sided, model-flagged product; θ_tr prior widened (σ_ln 0.5); A-5 says so |
| N5 A-10 sign and omission | RESOLVED | ℋ_eff = ℋ + E_trap^{pr} + E_es + E_pairs^{unp} + E_x − 𝒲_bias(t_pr), E_x ≤ 0: matches (E1-W4) |
| minor A-16 left-hand side | RESOLVED | dℛ/d𝐌 with P(𝐌,t\|Λ); the cascade dℛ/d𝐍 kept as the t_pr marginal |
| minor "²⁵²Cf-resonance" | RESOLVED | "10–100 keV (²⁵²Cf neutron calibration)" |
| minor CPD threshold | RESOLVED | quoted from 2007.14289 [FT] ("4.2 σ … 16.3 eV") |

## Multiplicative rewrite, bounds, and the r = 1.14 claim
- **r-shift:** at zero deficit, η₀ = [1 + g + gy(r−1)]/(1 + rg) = 1 + g(1−r)(1−y)/(1+rg). Correct. Solving η₀ = 0.952 with g = 1.047, y = 0.3 gives r = 1.144
  (hand: 0.6827r = 0.781). **The claim "r = 1.14 alone reproduces 0.952" STANDS as algebra.** Two notes:
  (i) g = eV_b/ε is not [UNVERIFIED]. 1803.02903 [FT] states the electrodes "were biased to 4 V …, creating an electric field of 4 V/cm", so V_b = 4 V and
  g = 4/3.82 = 1.047 are sourced. Update the tag.
  (ii) For fixed r the shift scales as (1 − y). Over 10–100 keV, y ≈ 0.22–0.35 gives η₀ = 0.947–0.955, within the quoted +0.9/−0.7 band. So the energy
  dependence does not break the degeneracy with present precision. A sharper η(E_R) measurement would. Optional: add this to §3.1 as a discriminant.
- **Bounds.** The text states E_st/ω ≤ 1 − η under (B-a)–(B-c), but writes the combination only at first order around r = 1. I checked the exact η for
  r ≥ 1. To first order in the deficit, 1 − η − e = g(r−1)[(1 − y) − e]/(1 + rg) + (δ, ΔX terms ≥ 0), with e = E_st/ω. So the bound needs the extra
  condition e ≤ 1 − y as well as (B-a)–(B-c). It is trivially satisfied here (e ≲ 0.06, 1 − y ≈ 0.7). A Monte-Carlo scan of the exact η over
  g ∈ [1, 1.1], y ∈ [0.2, 0.4], r ∈ [1, 1.3], δ ≤ 0.05, X ≤ 0.05, e ≤ 0.06 (3×10⁵ points) found no violation. Over wide ranges (y → 1, large
  deficits) violations occur, as the condition predicts. **Bounds STAND.** Add "and E_st/ω ≤ 1 − y" to (B-a)–(B-c), or state "to first order in d′ for r ≥ 1".
- The Ge row's "κ ≈ 0.6 [E]" and "same NR/ER structure (phonon − Luke)" are estimates, honestly tagged, and acceptable.

## New items
- **M1 (NEW ERROR, minor).** The coordinator's ZPE decision puts ΔZPE inside ℋ_ph, as ℋ_ph = ℋ_ph^{avail} + ΔZPE, and "only ℋ_ph^{avail} can reach a sensor".
  But (E7) uses ω − D′ with D′ = E_stored + E_esc, where E_stored = E_st + E_trap + E_es^{trap} has no ΔZPE. The sensor-visible primary energy is ω − D′ − ΔZPE(t_win).
  Add ΔZPE(t_win) to D′ in (E7), (E8), (E13) and A-4, or define E_stored to include it. Size: ~1% of E_st, i.e. ≲ 10⁻³ of ω. It does not move any bound,
  but the ledger is otherwise not closed for the observable.
- No other new error found in §1.1–§3.2, §5 (A-1…A-16) or §6.

## Summary
N1–N5 and all three minor items are RESOLVED. The multiplicative rewrite is correct. The bounds 0.21 (Si) and 0.20 (Ge) at 95% C.L. stand under the stated
conditions plus the trivially satisfied e ≤ 1 − y. The r = 1.144 degeneracy is algebraically correct and robust to the y(E) variation at present precision.
One minor new error: ΔZPE is missing from the pre-sensor deficit D′ (M1). Also, the g input can be retagged [FT].
