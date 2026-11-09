# R12 verification VER-WP7-B1-A (referee A of R11) on returns/R12/WP7-B1-v2.md

Scope: the v2 return (all changed sections: §0 change table, §2 E5.2′, §3(a)–(c), §5 E10, §7(a,b), §8, §9, §10 A6, §12 I5, §13–§19) and
code/WP7-B1-v2/checks.py, which I re-ran: **30/30 PASS** (about 10 s). Same isolation as R11: I read no other referee report, no state/ and no
other return. I re-derived the new or changed results by hand; they are marked [R]. I fetched no new literature: the quotes I checked against
the full text in R11 still match the text reused in v2.

## Verdict per R11 item (REF-WP7-B1-A)
| R11 item | Verdict | Evidence in v2 |
|---|---|---|
| 1 Embedding lemmas (STANDS) | RESOLVED | §1 kept; the wording "dynamically independent at ω ≠ 0" is correct |
| 2 / §1 E5: "exactly"; bare sum needs qa ≫ 1; novelty | RESOLVED | (E5.2′) now carries the errors [1 + O((𝔍^F/ΔE)², Δ_bin∂_ω ln ε̃^{-1})]. The bare-\|f\|² sum is said to need qa_mol ≫ 1. The result is credited as the Davydov oscillator-strength sum rule ("lemma, not new") |
| 3 / §2 E8(a): "violates (4.6)" overclaim | RESOLVED | It is now called the band-projected Schwinger-term sum rule, "not WP0 (4.6)", with the correct caveat that projection can generate g₄ ≠ g₂ couplings |
| 3 / §2 N_ch = 4 undercount of 2607.15338 | RESOLVED | Added in §3(a), IF-B1-10, LB1-2 and C2e, and credited to R11. S_wire = N_ch g_c\|q\|δ(ω − v_F\|q\|/g_c) is correct [R] |
| 4 E8(b,c) (STANDS) | RESOLVED; new content checked | C3c (Landau width) is new. Im ε = (k²/q²)(π/2)ω/(qv_F,1) and ∂_ωε = 2Ω²/ω³ give an amplitude damping γ/ω_a = (π/4)v_a/v_F,1 [R], so Γ = 2γ (FWHM) → (π/2)v_a/v_F,1 as stated and coded (Γ = 2 Im ε/∂_ωε). It is correct if "width" means FWHM; say so in one word |
| 5 E9 / 2110.01587 (16) (STANDS) | RESOLVED | Kept; the mapping f_fill = d/L is stated correctly |
| 6 / §3 E10 quote (bulk σ_A, QD ε) | RESOLVED | Quote corrected to "σ_A measured for bulk PbS; ε from Ref. [139], d = 5 nm dots" |
| 6 / §3 factor ×≈6, ω range | RESOLVED (improved) | "×≈6" withdrawn. The condition factor > 1 ⇔ \|ε_in + 2ε_out\| < 3\|ε_in\| is correct [R], and the check value 9·2/26 = 0.69 for ε_in = 1 + i, ε_out = 2 is correct [R]. Marking the size and sign UNRESOLVED is the honest status |
| 6 / §3 2208.05967 Eq. (6)/(10)/(12) prefactor | RESOLVED (as UNRESOLVED gap) | My dimensional diagnosis is reproduced verbatim. LB1-5 reads "structure DERIVED, prefactor UNRESOLVED", recorded as gap G-E10b |
| 7 E12; 1706.02487 misprint (STANDS) | RESOLVED | Kept |
| 8 X6(a): dP/dω asserted | RESOLVED | It is now derived in the text (U_κ = Z_ion e²/\|p+G\|², the 1/2π of (W.5), the angular average), and C7 is made independent: angular average, prefactor and angular δ are computed symbolically. I checked the C7 code: it does not assume the output. The ε^{sym} rename removes the collision with NOTATION's ε̃ |
| 9 X6(b): LB1-8 "DERIVED" | RESOLVED | LB1-8 now reads "SKETCH under (H_W)", exact remaining gap G-X6 |
| 10 X8 size estimate | RESOLVED | It is marked "a lower bound: the ω_e⁻⁴ of (W.5) favours the lowest lines" |
| 11 / §5 A2 attribution (Allen 1971) and L15 / OW4-3 | RESOLVED | Allen, PRB 3, 305 (1971) is credited for (A2.1)–(A2.2) and for the case-I vs MB distinction. The equation numbers in Allen are honestly marked UNVERIFIED. IF-B1-1 is re-worded, and the closed form of 𝔤_I is declared not new. (A2.2) stays [D, sketch] with gap G-A2 |
| 12 / §6 A6 double screening | RESOLVED | (A6.1) now reads Γ = κ²m lim(e²/2q²)S^D = κ²m ε₂^D/\|ε_host\|². ε₂^D is defined by the explicit sum, with 𝔣^loc removing (ε^{-1})_{00}, so screening is applied once [R]. This is consistent with CONVENTIONS §6 and with 𝒲 = ε₂^D/\|ε\|² |
| 12 / §6 "Lyman lines absent" (REFUTED) | RESOLVED | Withdrawn in §10(ii), §14 and LB1-11. The source's empirical bound-to-bound treatment (its sub-ionisation appendix, Fig. 7) is described correctly |
| 12 / §6 n_D values | RESOLVED, with a minor slip (N1) | Both values (1.8×10¹⁸ and 10¹⁸) are stated, together with the source's Mott value ≳ 3×10¹⁸ |
| 13 I3 (STANDS) | RESOLVED | Kept. The IF-B1-5 distinction between line positions and integrated rate is correct |
| 14 / §7 I5: transverse row mis-sized | RESOLVED | It is now O(v_χ²ω²/q²), up to O(v_χ⁴), from continuity and ε_T(q→0) = ε_L(q→0). Quoted from 2608.20715: 10⁻⁶–10⁻⁴ in the plasmon window and about 8% at ω ≲ 1 eV, which matches the full text I read in R11. v1's "≲ 10⁻⁴" is withdrawn, and the statement that both rows must be kept for v_χ ≳ 0.5 is added |
| 14 / §7 novelty (Fermi 1940; 2608.20715 Eq. (2)) | RESOLVED | Both are credited, and no novelty is claimed for the transverse/Cherenkov structure. 2608.20715 is now listed as [FT]. C12c is now non-tautological: explicit Dirac and plane-wave currents, both conservation laws checked numerically (residuals ≤ 10⁻¹⁶), and the decomposition verified at ω/Q = 0.34 |
| 14 / §7 "~1%" → "≲ 2%" | RESOLVED | (1 − v²)² = 0.98 at v_χ = 0.1 |
| 15 Gaps (add E10 prefactor, transverse size) | RESOLVED | G-E10b and a re-sized G-I5 are added in §13 |
| §8 notation (ε_b, 𝒫^W_0) | RESOLVED | ε_b,lay (≠ ε_bg); 𝒫^W_0 listed with the projector family; ε^{sym} added |
| §8 checks as identities | RESOLVED | The header labels C1a, C9a and C12a as identity checks that do not replace the text derivations. C1c is now general (Θ(v − v_min)/(qv) for all v_min) |
| Paper-claim ratings (table in R11) | RESOLVED | §14 asserts only CONFIRMED claims, marks UNRESOLVED ones as such, and withdraws the REFUTED one. Every rating matches mine |

## Rebuttals
None is addressed to referee A. §18 states that no R11 verdict is contested. Its clarification (ii) accepts A-§2 in full, and I have nothing to
adjudicate there. Clarification (i) answers referee B, so it is outside my remit; in any case it agrees with my R11 §7 argument (the shell
sphere is centred at m_χv, so for even S the O(v) term cancels).

## New issues in the changed sections (minor, none is an error of substance)
- **N1 (§10(iii)).** "n_D/n_c ≈ 0.5–0.6" covers only n_D = 1.8×10¹⁸ (1.8/3 = 0.6). The main-projection density 10¹⁸ gives ≈ 0.33. Write
  "≈ 0.3–0.6". The qualitative conclusion is unchanged: impurity-band effects matter near the edge at the appendix density.
- **N2 (§12, literature limit).** "spuriously enhanced as Q → ω" describes a limit that kinematics forbids, since ω/Q ≤ v_χ < 1 (stated in the
  same section). Write "as ω/Q → v_χ, bounded by (1 − v_χ²)^{-2} = γ_χ⁴". The bound itself is already given correctly in the preceding clause.
- **N3 (§3(c), C3c).** State that Γ_a is the full width at half maximum (= 2 Im ε/∂_ωε). Without that, a reader taking Γ as the amplitude damping
  rate would be off by a factor of 2.
- No new error was found in (E5.2′), (E8.1) with N_ch, (E10.3), (A6.1), (I5.0)–(I5.1), C2e, C3c, C7 or C12c.

## Overall
Every item of REF-WP7-B1-A is RESOLVED. There is no NEW ERROR of substance; three wording fixes (N1–N3) are optional. As far as referee A is
concerned, LB1-1 to LB1-13 in §17 can enter LIMITS with the statuses written there: LB1-5's prefactor and LB1-8 stay non-DERIVED as recorded.
