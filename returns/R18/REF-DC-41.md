# R18 / REF-DC-41: hostile referee report on DC-41 (Al BCS response)

Referee REF-DC-41, 2026-11-05. Under review: returns/R18/DC-41.md, code/DC-41/. Read: that return and code, CW4 §1, §8, the relevant CW4-errata rows (IF-CW4-1, A9), CONVENTIONS, NOTATION. No other R18 return and no referee report was read.
Code and data: code/REF-DC-41/ (`core.py`, `spec.py`, `dirty.py`, `t1`–`t10`, data/). Nothing is imported from code/DC-41. No literature was fetched.

## 0. Verdicts

| # | Claim | Verdict | Evidence |
|---|---|---|---|
| A1 | L^{BCS}/(𝔤_I L^{nor}) = 0.866 / 0.998 / 1.068 / 1.066 / 1.022 (clean GRPA) | **STANDS** as a number of the clean model | §1, §6 |
| A2 | This overturns CW4 §8 near the edge | **STANDS WITH CORRECTION** | Overturned at y ≥ 2.5 for every ℓ_mfp down to 30 nm. At y = 2.2 only for ℓ_mfp ≳ 1 μm; CW4's band is re-entered near 300 nm and undercut below ~100 nm. The clean *numbers* are accurate to a few % only at ℓ_mfp ≳ 10 μm (§4) |
| A3 | "the table holds for Al bulk … and for films" (§1) | **FAILS** | y = 2.2 ratio is 0.19 at ℓ_mfp = 30 nm, below CW4's 0.33–0.40 (§4) |
| A4 | "threshold step … screened away in L" → "bare only" (§0, §6) | **FAILS** | GRPA L also → 0 at threshold with no step, but only over y − 2 ≲ 0.03 (§6) |
| B1 | AB pole below 2Δ for every Q, 11.6% of the f-sum at the y = 2.2 edge Q | **STANDS WITH CORRECTION** | True of R̃ only. Its share of the loss L is exactly zero (§2, §5) |
| B2 | The pole "drives items 1, 3, 5" | **FAILS** for y ≥ 3 | Pole term is 0.052 of 0.332 at y = 3 and 0 at y ≥ 5 (§6) |
| C1 | 𝔰_eff^{GRPA} < 0 at the edge, values −5.51 … −0.96 | **STANDS** as a number | §6 |
| C2 | "the conserving superconductor screens less than the normal metal" | **FAILS** for y ≲ 4.5 | \|ε\|/\|ε^{nor}\| = 1.30 at y = 2.2 (§6) |
| E | Bare Im ε = 𝔤_I Im ε^{nor} exactly for y² − 4 ≤ Q² (§0 item 2) | **STANDS** | Ratio − 1 ≤ 4×10⁻¹⁶ at five points with s = s* ∓ t² (`t11`); the residual the return attributes to its endpoint panel is indeed quadrature |
| D | Re P̃ > 0 "in a small corner, y ≤ 2.2 at Q ≲ 6" | **STANDS WITH CORRECTION** | Wrong boundary (§6) |

No error was found in (DC41-1), the ladder, the Coulomb treatment, the amplitude argument or the f-sum. The faults are in scope and interpretation. Exact replacement text is in §7.

## 1. Test 1: closed form (DC41-1) against direct quadrature: STANDS
Three routes, none using the return's code.
- **Projector bubble at complex z = y + iγ** (`core.py`, `t1.py`). Coherence factors come from tr[τ_i P₊(ξ′)τ_j P₋(ξ)], derived from TΣ tr[τ_iG′τ_jG], with no δ-function roots. Twelve points, including (2.2, 5.64), (2.02, 7.8), (2.2, 9.7), (5, 12.82), (10, 25.64), (2.5, 30), (4, 1.5), (0.3, 1), and sub-gap γ = 0 points. |P̃_direct − P̃_closed|/|P̃| ≤ 1.8×10⁻¹⁰ at every point. The worst is sub-gap; above 2Δ all are ≤ 10⁻¹¹.
- **Energy-first route** (`dirty.py`). ξ and μ are done analytically and ε numerically on the R/A sectors, a different order of integration. At Γ = 10⁻³ it reproduces P33 to ~10⁻⁴ and P̃ to O(Γ) away from the pole, including the static −1.
- **Own real-axis evaluator** (`spec.py`, s = s* ∓ t² removes the inverse-square-root edges). All edge rows of the §3 table reproduce: 𝔳, 𝔰_eff (bare and GRPA), L ratios (t8 block E).

Δ → 0 control (t8 block G): at x = 0.39, |P̃ − Lindhard| = 4.4×10⁻³, 6.5×10⁻⁵, 8.6×10⁻⁷, 1.1×10⁻⁸ at Q = 10², 10³, 10⁴, 10⁵. Same behaviour at x = 0.8 and 1.5. **PASS.** The bare y ≫ 1 limit 𝔰_eff → 𝔰_BCS also holds for GRPA: 4.014, 2.034, 1.053, 0.501 at Q = 10⁵.

## 2. Test 2: gauge invariance, Goldstone, Coulomb: STANDS
- **Ladder derived independently.** From H_int = −(g/4)(A² + B²), one gets R̃ = χ₃₃ + χ₃₂χ₂₃/[χ₂₂(0,0) − χ₂₂], with 2/g = −χ₂₂(0,0). This is the return's form and confirms its D3. Π₂₃ = −Π₃₂ holds to 10⁻¹⁶ from the traces.
- **Ward identity, independent of the f-sum.** With the current vertex sτ⁰ dressed by the same ladder, z R̃_nn = R̃_jn to ≤ 6×10⁻¹¹ at all ten points of `t1` that carry the current vertex. The bare bubble violates it by 21–95%. The identity also holds with impurities (`t6` block C). This is a stronger test than the return's C4 and C5.
- **Neutral control.** ω_AB/(Q/√3) = 1.00000, 0.99978, 0.99448, 0.97835 at Q = 0.01, 0.1, 0.5, 1. The Goldstone mode is retained.
- **RPA denominator applied once.** A full 2×2 solve in (density, phase) with both kernels equals R̃/(1 − v_CR̃) to all printed digits at six Q (t8 block H). L in the return is built from ε = −(k_TF²/q²)P̃ once. There is no double counting.
- **Anderson–Higgs.** The pole of R̃ is a pole of ε, hence a zero of L. The Goldstone weight moves to the plasmon: the root of 1 = K P̃ is 15.9076 eV = k_TFv_F/√3 at Q = 0.3, 5.64, 100.
- **Does anything sub-gap survive in L? No.** I tested the strongest route to a surviving mode. ε rises with ω² between poles (Herglotz), so a sign change of ε between ω_AB and 2Δ would force a real zero, that is a δ-function in L below 2Δ. There is none: P̃(2⁻) > 0 at all 23 Q from 0.5 to 100 (0.48 at Q = 5.64, d = 10⁻²⁰⁰), so ε < 0 on the whole interval (ω_AB, 2Δ), and a direct sign scan at six Q finds no zero with the "1" kept. L ≡ 0 for y < 2.
- **New closed L-level sum rule.** h = 1/P̃ is Herglotz with h → 3y²/Q² + c and h(0) = −1, so (2/π)∫dy Im(1/P̃)/y = −1 − c = 4/5 (Lindhard: 0.80000). With **no** sub-gap term, GRPA gives 0.80000 at Q = 0.3, 1, 3, 5.64, 6.41, 7.69, 12.82, 25.64, 50 (`t4`). This closes the question and is a better acceptance test than the R̃ f-sum, because it acts on the observable.

The return's sentence "L has a zero, not a peak (Coulomb removes the mode)" is correct.

## 3. Test 3: dropped amplitude channel: STANDS
Π₃₁ and Π₂₁ are 10⁻¹⁸ with constant DOS, so the parity argument holds. The return did not size the actual breaking, so I did (`t9`, data/t9b.out). With N(ξ) = N(0)(1 + aξ), a = Δ/2E_F = 7.7×10⁻⁶, cutoff 200Δ, the 3-channel P̃ differs from the 2-channel P̃ by 1.8×10⁻⁹ (y = 2.2), 1.9×10⁻⁹ (y = 3) and 1.1×10⁻⁸ (y = 1.9, next to the pole). Scaling is a². The amplitude denominator Π₂₂(0,0) − Π₁₁ = −¼⟨(u² − 4)f⟩ is −1.195 at (1.9, 5.64) and has no sub-gap zero, because (u² − 4)f > 0 for y < 2. There is no Higgs pole to amplify the coupling.
Correction to my own run: data/t9.out used Π₁₁(0,0) in that denominator and is off by exactly 1. The closed form exposed this. Use data/t9b.out.

## 4. Test 4: is the pole physical, and is the clean limit valid for Al?
**T = 0 damping.** E + E′ has minimum 2Δ at every q < 2k_F, so the clean pole is undamped at T = 0. Landau damping needs thermal quasiparticles, ~e^{−Δ/T} ≈ e⁻⁴² at 50 mK, which is negligible. The return is right on this.

**Impurities: new calculation.** `dirty.py` is T = 0, Born scalar impurities, 1/τ = 2ΓΔ, with GRPA and impurity ladders together. Validation: normal state equals Mermin–Lindhard to 6 digits at five points. Ward identity holds at Γ = 0.5–5. Γ → 0 gives the clean result. Dirty limit approaches Mattis–Bardeen, with a residual: at Dq² = 0.004–0.017, L ratio 0.243–0.251 against MB 0.2352 at y = 2.2 (3–7%), 0.758–0.782 against 0.7440 at y = 2.5 (2–5%), 1.306–1.335 against 1.3024 at y = 3 (0.3–2.5%) (`t14`). I attribute the residual to finite Dq² and a numerical floor, not proved: the code has an absolute floor |δP̃| ~ 10⁻⁵ from the inverse-square-root edges, and refining the grid does not lower it below that (conditioning of the ladder at the edge). So runs with |P̃| ≲ 10⁻³ are meaningless (`t11`, Q = 1 at Γ ≥ 1000, discarded). On the table below |P̃| ≥ 10⁻², so the floor is ≲ 0.3% (`t13`: 0.2805 → 0.2810 at y = 2.2, Γ = 124). MB σ₁ is taken by magnitude. The Γ = 124 entry at y = 2.2 sits above the MB value (0.157 after dividing by 𝔤_I) because Dq² = 0.043 is not small there; either value is below CW4's band. f-sum 1.0000 / 0.9995 and compressibility 1.0000 at Γ = 0.37 / 3.7. Dirty phase velocity gives ω_AB = 0.359 against (Q/√3)√(π/2Γ) = 0.366 at Q = 5.64, Γ = 124.

ℓ_mfp = ħv_F/(2ΓΔ) with v_F = 6.8×10⁻³, Δ = 0.18 meV. Entries are L^{BCS}/(𝔤_I L^{nor}(Γ)) on the edge Q = y/0.39, with the normal state at the same Γ (data/dirty_edge.csv):

| Γ | ℓ_mfp | y = 2.05 | 2.2 | 2.5 | 3 | 5 | 10 |
|---|---|---|---|---|---|---|---|
| 0.037 | 100 μm | 0.676 | 0.863 | 0.996 | 1.067 | 1.066 | 1.022 |
| 0.37 | 10 μm | 0.639 | 0.835 | 0.981 | 1.062 | 1.065 | 1.022 |
| 1 | 3.7 μm | 0.569 | 0.780 | 0.950 | 1.050 | 1.064 | 1.022 |
| 3.7 | 1 μm | 0.365 | 0.600 | 0.854 | 1.021 | 1.057 | 1.020 |
| 12.4 | 300 nm | 0.168 | 0.375 | 0.733 | 1.027 | 1.066 | 1.016 |
| 37 | 100 nm | 0.080 | 0.246 | 0.633 | 1.025 | 1.082 | 1.018 |
| 124 | 30 nm | 0.045 | 0.187 | 0.569 | 1.008 | 1.091 | 1.021 |

Reading:
Two criteria must be kept apart: whether CW4 is overturned, and whether the clean number is accurate.
- **y ≥ 3:** ratio stays in 1.01–1.09 from clean to 30 nm. CW4 is overturned and the clean number is accurate at every ℓ_mfp. The return's §7 caution is too pessimistic here.
- **y = 2.5:** 0.57 at 30 nm is still above CW4's 0.45–0.54, so CW4 is overturned at every ℓ_mfp, but the clean 0.998 is accurate to 2% only at ℓ_mfp ≳ 10 μm.
- **y = 2.2:** above CW4's 0.33–0.40 for ℓ_mfp ≳ 1 μm (0.60). Inside that band near 300 nm (0.375). Below it at 100 nm and 30 nm (0.25, 0.19). So in films the suppression at this y returns and is stronger, by the Mattis–Bardeen route (σ₂ ≫ σ₁).
- **Clean numbers:** accurate to ≤ 4% only for ℓ_mfp ≳ 10 μm at y ≤ 2.5.

**Gap anisotropy, clean** (separable ladder, Gaussian φ uncorrelated with μ, Goldstone preserved, not combined with Γ):

| σ_φ | y = 2.05 | 2.2 | 2.5 | 3 | 5 |
|---|---|---|---|---|---|
| 0 | 0.680 | 0.866 | 0.998 | 1.068 | 1.066 |
| 0.05 | 0.521 | 0.821 | 0.996 | 1.068 | 1.066 |
| 0.1 | 0.341 | 0.720 | 0.983 | 1.070 | 1.067 |

σ_φ ~ 0.1 is the value I recall for Al (⟨a²⟩ ~ 0.01) [UNVERIFIED, from memory]. It exceeds 2 − ω_AB = 0.071 at the edge, so the clean pole lies inside the smeared continuum. Typical film ℓ_mfp (tens of nm) is also from memory [UNVERIFIED]; the table does not depend on it.

**Fate of the pole under impurities.** My expectation was that Γ would cut off the log and destroy the pole. That is wrong, and I record it. Below 2Δ at T = 0, Born impurities add no damping and the pole moves **down**: at Q = 5.64, ω_AB = 1.925, 1.813, 1.491, 1.010, 0.359 at Γ = 0.037, 1, 3.7, 12.4, 124. Its R̃ share is 12%, 17%, 17%, 9%, 1.2%. So "11.6%" is specific to the clean model, while the pole's existence is not. At Q = 12.82 the pole is visibly lifted off 2Δ for Γ ≳ 3.7. Z at Γ ≤ 0.01 is unreliable in my code (numerical derivative next to the edge; the shares at Γ = 10⁻³ disagree with the clean value) and is not quoted. The L table is unaffected: at Γ = 10⁻³ it agrees with the clean row to 0.4%.

**Is it physical?** In a charged superconductor the pole of R̃ is not an excitation seen in L at any Γ. It enters only through Re ε at y > 2.

## 5. Test 5: f-sum: STANDS WITH CORRECTION
Own grid, own residue: f-sum 1.000000 and compressibility 1.000000 at nine Q from 0.3 to 50; share 11.62% at Q = 5.64, 5.58% at 6.41, 1.33% at 7.69. The numbers are right.
What fails is the label. This is the f-sum of the Coulomb-proper R̃, not of L. The physical sum (2/π)∫ωL dω = ω_p² is saturated by the plasmon at 15.9 eV, and the pole's share in it is exactly zero. A reader of §0 item 6 would take it for observable weight. Note also that the check tests the 1/y² coefficient; the Ward identity (§2) is what tests the vertex directly.

## 6. Test 6: negative 𝔰_eff, and items resting on it
**The number is real.** Edge values reproduce: −9.36, −5.52, −3.58, −2.55, −1.56, −0.96 at y = 2.02, 2.2, 2.5, 3, 5, 10. It is not a sign error or a quadrature artefact. 𝔰_eff = 0 at Q = 8.37, 11.85, 22.8, 55.5 (x = 0.263, 0.253, 0.219, 0.180) for y = 2.2, 3, 5, 10. The return's "0.12–0.25" is low at the top end; I did not test y > 10.

**The interpretation is definition-bound.** 𝔰_eff measures only the Re ε shift, whereas screening of a probe is 1/ε:

| y (edge) | 2.2 | 3 | 3.5 | 5 | 10 |
|---|---|---|---|---|---|
| 𝔰_eff^{GRPA} | −5.52 | −2.55 | −2.12 | −1.56 | −0.96 |
| \|ε^{GRPA}\|/\|ε^{nor}\| | 1.299 | 1.069 | 1.028 | 0.994 | 0.991 |
| L^{GRPA}/L^{nor} | 1.299 | 1.412 | 1.361 | 1.227 | 1.074 |

So where 𝔰_eff is most negative, |ε| exceeds the normal value by up to 30%. |ε| drops below normal only at y ≳ 4.5, by ≤ 1%. "Screens less" is false by the measure that enters the rate. L > L^{nor} comes from raised Im ε. Also, 𝔰_eff is a function of (y, Q), and at the edge Q𝛿P ~ 1, so it is not a small correction comparable with 𝔰_BCS(y).

**B2: what drives it.** KK split of Re P̃ − Re P^{nor} (t8 block J):

| y | direct | pole term | 𝔰_eff | 𝔰_eff without pole |
|---|---|---|---|---|
| 2.2 | 0.978 | 1.100 | −5.52 | +0.69 |
| 3 | 0.332 | 0.052 | −2.55 | −2.15 |
| 5 | 0.121 | 0.000 | −1.56 | −1.56 |
| 10 | 0.037 | 0.000 | −0.96 | −0.96 |

The pole explains the sign only at y ≲ 2.3. At y ≥ 3 the sign comes from the continuum vertex, which also contradicts the return's own §7 ("no resonance" at y ≥ 5).

**A4: threshold.** On the edge Q = 5.128, L^{GRPA}/L^{nor} = 0.096, 0.149, 0.263, 0.430, 0.578, 0.814, 0.972 at y − 2 = 10⁻¹², 10⁻⁹, 10⁻⁶, 10⁻⁴, 10⁻³, 10⁻², 0.03. So L has no mathematical step at 2Δ in GRPA either, because Im P̃ itself vanishes at threshold (the return's own D7), and the §6 edit "→ bare only" is wrong as written. The width matters, though: L recovers to 0.97 L^{nor} by y − 2 = 0.03 (≈ 5 μeV at Δ_BCS = 0.18 meV), which is a sharp step for any rate integral. In the bare bubble at the same Q the ratio is still 0.30. So what GRPA overturns is the *breadth* of CW4's suppression, not the formal limit. The range "[0.58, 1.08]" is a grid statement: the ratio → 0 for y → 2⁺.

**D: the Re ε sign change.** Re P̃ > 0 on 2 < y < y_c(Q), with y_c − 2 = 0.353, 0.170, 0.091, 0.040, 0.016, 8.4×10⁻⁴, 6.3×10⁻⁶ at Q = 5.64, 6, 6.41, 7, 7.69, 9.7, 12.82. It persists as a sliver at all these Q. It reaches past y = 3 at Q ≲ 5.3. The y grid (lowest y = 2.02) cannot resolve it for Q ≳ 7.7. L has no resonance there: Im P̃ is large at y_c (−1.18 to −7.9), so no narrow peak was missed by the grid.

Item 4 of §0 ("within 1.5% of KK-∞") checks against data/edge_table.csv: worst 1.4% (y = 2.2), 1.1% at y = 3. **STANDS.**

## 7. Exact replacement text
**DC-41 §0, closing paragraph.** Replace "The clean-model GRPA therefore overturns the near-edge reading of CW4 §8 ("the threshold step of Im ε is screened away in L"). It holds only for the bare bubble, which fails the f-sum." with:
"The clean-model GRPA replaces the CW4 §8 table. CW4 is overturned at y ≥ 2.5 for every ℓ_mfp down to 30 nm, and at y = 2.2 for ℓ_mfp ≳ 1 μm (REF-DC-41 §4). At y ≥ 3 the ratio L^{BCS}/(𝔤_I L^{nor}) is 1.01–1.09 at all these ℓ_mfp. At y ≤ 2.5 the clean numbers themselves hold only for ℓ_mfp ≳ 10 μm; at y = 2.2 the ratio is 0.87 clean, 0.60 at 1 μm, 0.38 at 300 nm (inside CW4's band), 0.19 at 30 nm (below it). In the clean model L still vanishes at 2Δ_BCS, because Im ε does, but it recovers to 0.97 L^{nor} by y − 2 = 0.03, so the broad suppression of CW4 §8 is absent."

**§0 item 5.** Replace "near the edge the conserving superconductor screens less than the normal metal, opposite to WP4 §4.2 "Sign"" with:
"near the edge Re ε lies below its normal value, opposite to the sign of 𝔰_BCS in WP4 §4.2. This concerns Re ε only: |ε|/|ε^{nor}| = 1.30, 1.07, 0.99 at y = 2.2, 3, 5." Replace "x = y/Q ≈ 0.12–0.25" with "x = y/Q ≈ 0.18–0.26 (y = 10 to 2.2)".

**§0 item 6.** Replace with:
"The ladder gives R̃ an Anderson–Bogoliubov pole at ω_AB < 2Δ_BCS for every Q; the KK and f-sum of R̃ need it. It carries 11.6% of the f-sum of R̃ at the y = 2.2 edge Q (clean; 1–17% with impurities). It carries no weight in L: ε has a pole there, ε < 0 on (ω_AB, 2Δ_BCS), L ≡ 0 below 2Δ_BCS, and (2/π)∫Im(1/P̃)dy/y = 4/5 closes with no sub-gap term. The pole dominates Re P̃ only at y ≲ 2.3; at y ≥ 3 the shift comes from the continuum vertex."

**§1.** Replace "so the table holds for Al bulk (0.18 meV [E], CONVENTIONS row 33) and for films" with:
"so the table scales with Δ_BCS, but it is a clean-limit table: its values at y ≤ 2.5 are accurate to a few % only for ℓ_mfp ≳ 10 μm (Γ = ħv_F/2ℓ_mfpΔ_BCS ≲ 0.4). For shorter ℓ_mfp, which includes Al films, use REF-DC-41 §4."

**§3.** Replace "Re ε^{GRPA} changes sign (Re P̃ > 0) in a small corner, y ≤ 2.2 at Q ≲ 6." with:
"Re P̃ > 0 on 2 < y < y_c(Q), y_c = 2.35, 2.09, 2.016, 2.0008 at Q = 5.64, 6.41, 7.69, 9.7, a sliver that narrows with Q; L has no peak there." After "lies in [0.58, 1.08]" add "(on the grid, whose lowest y is 2.02; the ratio → 0 as y → 2⁺)".

**§6, first bullet.** Replace "The line "the threshold step of Im ε is screened away in L" → bare only." with:
"The line "the threshold step of Im ε is screened away in L" → "L vanishes at 2Δ_BCS: in the bare bubble because Re ε diverges, with suppression out to y ~ 3 and beyond; in clean GRPA because Im ε vanishes, with L back to 0.97 L^{nor} by y − 2 = 0.03." The GRPA row is accurate at ℓ_mfp ≳ 10 μm for y ≤ 2.5; use the ℓ_mfp-dependent table of REF-DC-41 §4 otherwise."

**§6, WP6 bullet.** Replace "but they are no longer needed in the clean model; RG9 ("the full-KK route removes the mask") is delivered." with:
"but removing them depends on ℓ_mfp. At y ≥ 2.5 the GRPA value stays above the cut column down to 30 nm. At y = 2.2 it does so only for ℓ_mfp ≳ 1 μm; for ℓ_mfp ≲ 300 nm it lies at or below the cut column (0.38 at 300 nm, 0.19 at 30 nm, against 0.40), so "central = cut" is not conservative there. RG9 is delivered for ℓ_mfp ≳ 1 μm, with the mask question at y ≈ 2.2 open for films."
Likewise, in the "Consequence to check" sentence, after "is pessimistic in the clean model" add "and may be optimistic for films at y ≈ 2.2".

**§6, WP4 "Sign" bullet.** Replace "reversed near the edge" with "reversed for Re ε near the edge, without |ε| falling below normal at y ≲ 4.5".

**§7, first bullet.** Replace with:
"Clean, T = 0, constant DOS. Impurities are computed in REF-DC-41 §4: y ≥ 3 is insensitive, and y ≤ 2.5 is strongly sensitive. In a toy separable anisotropy model, σ_φ = 0.1 [UNVERIFIED for Al] lowers y = 2.2 to 0.72. Finite T and strong coupling are not computed."

**New acceptance test for the CONTROLS list.** "(2/π)∫dy Im(1/P̃)/y = −1 − c, c = lim[1/P̃ − 3y²/Q²] = −9/5 (L-level sum rule); z R̃_nn = R̃_jn (Ward identity)."

## 8. Limits of this report
- Impurities: Born, isotropic, T = 0, no anisotropy in the same calculation, no strong coupling, no interaction–disorder (Altshuler–Aronov) corrections. Results at ω τ ≲ 1 are therefore model values, not predictions.
- The anisotropy model is a toy (separable, φ independent of μ).
- ⟨a²⟩ for Al and film ℓ_mfp are from memory, unfetched.
- The rate consequences of the dirty L^{nor} itself were not computed.
