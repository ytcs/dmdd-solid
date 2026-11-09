# R12 verification VER-WP7-B1-B (referee B, isolated) of returns/R12/WP7-B1-v2.md

What I read:
- returns/R12/WP7-B1-v2.md: the change summary, §§1–5, 7–10, 12, 14–19;
- code/WP7-B1-v2/checks.py. I re-ran it: **30/30 PASS**, about 10 s;
- my own R11 report;
- CONVENTIONS for section numbers;
- full-text extracts kept from R11 (1604.06800 reference list).
No new fetches. No referees/, state/ or other returns read.

## Rebuttals
§18 contests no B verdict, so there is nothing to ACCEPT or REJECT. The two "clarifications" are not rebuttals and I agree with both:
- (i) B-15 anisotropic O(v) cancellation: now stated in §11;
- (ii) the projected-sum-rule reading of E8(a): matches B-§1.2(i).

One retraction of my own. In R11 §2.6 I asked for the 2110.01587 filling to be mapped as f_fill ↔ (1 − d/L). That was wrong. At k_z = 0 the source's
Eq. (16) gives (1 − d/L)/ε₂ + (d/L)/ε₁. The EMT 1/ε_⊥ = f/ε_A + (1 − f)/ε_B gives the same expression with f = d/L and ε_A ≡ ε₁. v2's mapping
"f_fill = d/L, d the ε₁ thickness" (§4, LB1-4) is the correct one.

## Item-by-item (my R11 verdict-table rows and § items)
| B item | R11 verdict | v2 action (checked in the text) | Verdict |
|---|---|---|---|
| 1 (1.1) lemma | STANDS | "dynamically independent at ω ≠ 0" wording; conversion to per-mass rates (CONVENTIONS §8) | RESOLVED |
| 2 E5 "exactly", novelty | SWC | (E5.2′) now carries [1 + O((𝔍^F/ΔE)², Δ_bin∂_ω ln ε̃⁻¹)]; Davydov oscillator-strength sum rule credited; bare-\|f\|² sum still needs qa ≫ 1 | RESOLVED |
| 3 LB1-1 quotes | STANDS | unchanged | RESOLVED |
| 4 E8(a) f-sum, novelty, N_ch | SWC | Projected (Schwinger) sum rule, explicitly not WP0 (4.6). v_J = v_F credited (Haldane, marked UNVERIFIED). C2d relabelled. ×N_ch = 4 finding added. n = √N_ch ∂φ_c/π is correct for orthonormal φ_c = N_ch^{-1/2}Σφ_i, giving S = N_ch g_c\|q\|δ. C2e passes. IF-B1-10 and LB1-2 updated | RESOLVED |
| 5 E8(b) "halves" | wording | "divides v_C^{2D} by (1+ε_sub)/2 ≈ 2.4" | RESOLVED |
| 6 demon novelty, Landau damping | novelty FALLS | Pines credited. Validity v_a ≪ v_F,1 stated. Γ_a/ω_a → (π/2)v_a/v_F,1 (C3c), which I re-derived (note below) | RESOLVED |
| 7 E9 / 2110.01587 (16) | STANDS | f_fill = d/L stated (correct; see retraction above) | RESOLVED |
| §1.4 IF-B1-2 overclaim | correction | "for films with d_film ≪ 1/q" in §4 and §16 | RESOLVED |
| 8 E10 misquote, sign/size | SWC | Quote corrected (σ_A bulk; ε from Ref. [139], 5 nm dots). Factor 9\|ε_in\|²/\|ε_in+2ε_out\|² stated as > 1 only where \|ε_in+2ε_out\| < 3\|ε_in\|. "×≈6" withdrawn; size UNRESOLVED. ε_eff (MG/Bruggeman) added to the computation specification | RESOLVED (caveat C-1 below) |
| 9 E12 / 1706.02487 | STANDS | unchanged | RESOLVED |
| 10 X6(a) ε̃ clash; C7 not independent | SWC | ε^{sym}_{GG′} = δ − v_C^{1/2}R⁰v_C^{1/2} introduced, RPA stated, NOTATION ε̃ untouched (§15). New C7 derives: (a) the isotropic average ⟨(q̂·a)(q̂·b)⟩ = a·b/3 by integration; (b) the S_{GG′}–ε^{sym} prefactor, giving 4αZ²q²/(3M²ω⁴); (c) the angular δ. I checked (b) by hand: (1/2π)·Z²e⁴/(P_a²P_b²)·(2P_aP_b/e²)·(q²P_aP_b cos/3) = 4αZ²q² cos/3 per M²ω⁴. The (q/M)/ω² amplitude shape of (W.5) is still taken as input from WP3-v3; that is acceptable because L7b is REFEREED | RESOLVED |
| 11 X6(b) LB1-8 | STANDS as sketch | LB1-8 "SKETCH under (H_W)" | RESOLVED |
| 12 X8 | STANDS | unchanged; size marked as a lower bound | RESOLVED |
| §3.4 X8 convergence criterion | correction | 5% stability under k-mesh and band-number doubling added | RESOLVED |
| 13 A2 Allen attribution | SWC | Allen, PRB 3, 305 (1971) credited for (A2.1)–(A2.2) and for case I vs MB. "Via 1604.06800 Ref. [29]" is correct: [29] is Allen 1971 in that reference list. IF-B1-1 re-worded; 𝔤_I closed form declared not new | RESOLVED |
| 14 A6 Lyman, Mott | SWC | Lyman claim withdrawn as REFUTED, with the source's empirical bound-line treatment described correctly. n_D/n_c ≈ 0.5–0.6, so O(1) impurity-band effects (1.8/3 = 0.6 using the source's "≳ 3×10¹⁸"). Misprint impact UNRESOLVED (G-A6). Screening is now applied once (an A item): (e²/2q²)S^D = \|ε⁻¹_00\|²·ε₂^D with 𝔣^{loc}_D normalised to (ε⁻¹)_00, which is consistent | RESOLVED |
| 15 I3 | STANDS | IF-B1-5 now separates line positions (O(v/v*)) from integrated rates (O(v²/v*²)) | RESOLVED |
| 16 I5; C12c tautological | STANDS | Impact on 2401.11971 Fig. 3 UNRESOLVED. New C12c builds explicit Dirac spinor and plane-wave transition currents, checks both conservation laws numerically (residuals ~10⁻¹⁶), then the Minkowski decomposition at ω/Q = 0.34. The (1 − ω²/Q²) factor is no longer an input | RESOLVED |
| 17 checks as verification | SWC | C7 and C12c independent. C1c tested for general v_min. Identity checks (C1a, C9a, C12a) labelled as support only | RESOLVED |
| §3.3 rate units; CONVENTIONS row for F_DM | correction | Per length/area → per mass (§1, IF-B1-9). CONVENTIONS amendment row proposed in IF-B1-6, addressed to the coordinator and correctly placed under §9 "σ̄_e and F_DM" (my R11 wrote §7; §9 is right) | RESOLVED |
| §5 literature-rating table | ratings | §14 asserts only CONFIRMED items, marks UNRESOLVED ones, withdraws REFUTED ones; ratings match mine | RESOLVED |

Score: 17/17 table rows and 6/6 § items RESOLVED. 0 NOT RESOLVED.

## Checks on the changed sections (new-error hunt)
- **C3c / demon width.** At q ≪ k_TF,1, write ε ≈ ε′(ω_a)(ω − ω_a) + i Im ε, with ε′ = 2Ω²/ω_a³ and Im ε = (π/2)(k²/q²)(ω_a/qv_F,1). Then:
  - half-width/ω_a = Im ε/(ε′ω_a) = (π/4)Ω/(k v_F,1);
  - so full width Γ_a/ω_a = (π/2)v_a/v_F,1, with v_a = Ω/k. This matches v2 and C3c, which uses 2 Im ε/ε′.
  - Wording only: §3(c) should say Γ_a is the full width (FWHM). Not an error.
- **I5 transverse row.** Two parts:
  - In the optical region ε_T → ε_L, and continuity gives S_{j_Lj_L} = (ω/q)²S_nn. Hence S_{j_Tj_T} ~ (ω/q)²S_nn per component, and the rate ratio
    is O(v_χ²ω²/q²) ≤ O(v_χ⁴). This is correct, and the v1 "≲ 10⁻⁴" is properly withdrawn.
  - "(1 − v_χ²)² = 0.98 at v_χ = 0.1, so ≲ 2%" is correct arithmetic.
- **E8(a) channel count.** The neutral modes (orthogonal combinations) have zero overlap with the total density, so they do not couple. Correct.
- **A6 / E10 / X6.** No new algebra beyond the items above. Notation (ε^{sym}, ε_b,lay, v_a, v_F,1, Γ_a) collides with no NOTATION row I can see.

**New errors found: none.**

## Residual caveat (not an error, no action required for closure)
- **C-1 (E10, Ref. [139]).** v2 calls Ref. [139] (Hechster & Sarusi 2017) "dielectric data for d = 5 nm dots". I could not verify that reference's
  content. If its ε is an *ensemble/film* effective dielectric function rather than the intrinsic ε_in of a dot, part of the depolarisation is
  already inside it. The ε_eff appropriate to a dilute solvent suspension would then differ from both. v2 already leaves the size and sign
  UNRESOLVED, so the asserted statement ("the composite depolarisation factor is not applied") stays safe. A one-line note "ε of Ref. [139]:
  intrinsic or film, not checked" would make it airtight.

## Verdict
All referee-B items are RESOLVED. No rebuttal needs adjudication. No new error was found in the changed sections. From referee B's side, WP7-B1-v2
is ready for LIMITS entry of LB1-1 … LB1-13 with the statuses given in its §17.
