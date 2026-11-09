# R8 / VER-WP1-B: verification of returns/R8/WP1-v3.md against REF-WP1-B (R7)

Referee B, same isolation as in R7. I read the closing table (§13), §0, §R1–R3 and all changed sections (§1.3–1.5, §2.2–2.6, §3.2–3.7,
§4.2, §5.1–5.2, §6, L3, L10, L11, L14, L17, L19, §8, §10, §11). I re-ran code/WP1-v3/checks.py: 49/49 PASS (about 1 min). The hand
checks are below. No literature was re-fetched.

## 1. Item-by-item verdicts (B-n = row n of my R7 table)
| Item | R7 verdict | v3 action | Verdict |
|---|---|---|---|
| B-1 [E1], ladder | STANDS | kept | RESOLVED |
| B-2 [E2] out-state, F1 | STANDS | kept; Hermitian f_Hxc G-matrix now stated (§1.3) | RESOLVED |
| B-3 [E3] beyond RPA | w/ corr. | (1.4′) (−R⁰)^{-1} + f_xc > 0; DKM; counterexample C3c | RESOLVED (checked: R⁰ = −1, f_xc = −2, v = 3 ⇒ 1 − f_HxcR⁰ = 2, R̃ = +1, ε^{-1} = −½; R̃^{-1} = R⁰^{-1} − f_xc < 0 ⇔ (1.4′)) |
| B-4 §1.5 pointwise vs rate | w/ corr. | 0.117/0.451 separated from ×1.4–2.5 | RESOLVED |
| B-5 [E4] SOC, Δ_χ | w/ corr. | [H, s_e] = 0 added; remainder (Δ_χ/q)n_e | RESOLVED (q·v_χ = ω_q + Δ_χ ⇒ (q̂·v^⊥)n ≐ (Δ_χ/q)n on shell) |
| B-6 [E5] | STANDS | Σ_λ form; degeneracy on 3-/4-fold axes stated | RESOLVED |
| B-7 [E6] | w/ corr. | R̃_s ≡ R_mm = 4R_{s^zs^z}; triplet W-ladder leading; f_xc^T as [E] upper bound | RESOLVED |
| B-8 ALP | STANDS | kept, with the ladder caveat | RESOLVED |
| B-9 count | w/ corr. | 12 (Si/Ge), 18 (general); R⁰_{GG′} output | RESOLVED; rebuttal ACCEPTED (§2) |
| B-10 [E7] | STANDS | kept | RESOLVED |
| B-11 selection rules | STANDS | (2̄00) on-axis Umklapp allowed (A-11) | RESOLVED. I concede: my R7 §F phase cancellation assumed q = k_c (G = 0); the residual e^{−iG·t_d} = −1 for G = (2̄00) gives the operator the character (1, 1, −1, −1, +1) on (E, C₂, C₄, σ_v, σ_d) = Δ₂′ ⊂ Γ₂₅′↓C₄ᵥ (Γ₂₅′ restricts to (3, −1, −1, −1, +1) = Δ₅ + Δ₂′), so the transition is allowed. Consistent with X₁ band sticking |
| B-12 [E8] | STANDS | second-class factor 1/3 (A-13); "+35%" downgraded | RESOLVED (1/3 is right for a fixed gradient: only the p_m along ∇_kρ contributes) |
| B-13 thresholds | FALLS | [E13] min over q; Si 0.42 / 0.54; Ge L 0.32–0.36; Γ rebutted | RESOLVED; Ge-Γ rebuttal ACCEPTED (§2) |
| B-14 [E10] | STANDS | consistency with [E13] stated; allowed on-axis branch ≥ 2.28 keV | RESOLVED |
| B-15 q_c | w/ corr. | 2.24 keV | RESOLVED ((3/5)(q_cv_F)²/ω_p² = 0.53: not small, as v3 says) |
| B-16 FW spin curl, Ge 3d | w/ corr. | (i/m_e)q × s_e (C2d); "~10⁻³ (bounded by 2%)" used throughout | RESOLVED |
| B-17 §6.1 | STANDS | kept | RESOLVED |
| B-18 2607.06005 | STANDS | kept; finite-k Migdal framing adopted | RESOLVED |
| B-19 L1 | STANDS | kept; numbering scheme stated (PDF, HTML noted) | RESOLVED |
| B-20 L2 | STANDS | kept | RESOLVED |
| B-21 L3 (a) PT | w/ corr. | Im 𝒲̄₂ ≡ 𝒲̄₅ ≡ 0 under PT; V_NL reading withdrawn; 2 independent responses in Si/Ge | RESOLVED |
| B-22 L3 (c) 𝒪₈ | w/ corr. | 𝒪₂, 𝒪₅ added; medium factor; number UNRESOLVED; Cauchy–Schwarz bound | RESOLVED, with wording item N3 |
| B-23 L10 | STANDS | kept | RESOLVED |
| B-24 L11 | w/ corr. | ×(5/1.9)² dropped; ≈ 1.4 | RESOLVED |
| B-25 L14 | STANDS | kept | RESOLVED |
| B-26 L17 (c) | w/ corr. | (1.4′) | RESOLVED |
| B-27 gaps | w/ corr. | G5 matrix-free (no 7 TB kernel); G7 consistent; G10 count and R⁰_{GG′}; exciton-gap min_q spec | RESOLVED |
| B-28 contested | STANDS | kept | RESOLVED |

Totals: 28/28 RESOLVED. No item is NOT RESOLVED. The new errors (all minor) are in §3.

## 2. Rebuttals addressed to me
**R1-a (B-13, Ge Γ onset 0.256 MeV): ACCEPT.** My 0.256 MeV is 2E_dir/v_max², the flat-band floor, reached only if E^{ZP}(q) = E_dir at
q = 2E_dir/v_max ≈ 0.68 keV. A Γ pair of total momentum q has minimum energy E_dir − E_x^b + q²/2M_x, with M_x = m_c(Γ) + m_hh ≤ 0.04 + 0.50 =
0.54 m_e. At q = 0.67 keV that is q²/2M_x = 4.49×10⁵/(2×2.75×10⁵) ≈ 0.82 eV, not negligible. (In R7 I mis-scaled this term by 10³.) Then
m_χ = q²/[2(qv_max − E − q²/2M_x)] = 4.49×10⁵/[2(1.776 − 0.888 − 0.817)] ≈ 3.1 MeV, which reproduces C9f. The Γ channel undercuts the L
onset only for a pair mass ≥ 2.3 m_e at 0.31 q_BZ, which the Ge heavy-hole band does not support. Ge zero-phonon onset ≈ 0.32–0.36 MeV
(L, allowed) [E]. My own L range 0.33–0.37 agrees.

**R1-b (B-9, "14 = 7 + 7"): ACCEPT.** My singlet 7 combined a real S_{nj_T} (2) with a nonzero antisymmetric jj part (1).
- Under TR, S_ab(q) = η_aη_bS_ab(−q)*; under inversion, S_ab(q) = η_aη_bS_ab(−q). Together (PT) they make every S_ab real. A Hermitian real
  matrix is symmetric, so the antisymmetric part vanishes.
- PT case: the {n, j_T1, j_T2} block is real symmetric, 6 functions. General case: Hermitian 3×3, 9 functions. No class has 7.
- The IP triplet block is ¼ of the IP singlet block (spin-rotation invariance), so 6 + 6 = 12 and 9 + 9 = 18.

**R1-c (my §E (iii), "angle-averaged 𝒲̄₅ ≡ 0 under TR alone"): ACCEPT.**
- TR gives S_jj(q) = S_jj(−q)*. Write the antisymmetric part as iM(q), M real antisymmetric with axial vector g. Then
  iM(q) = −iM(−q), so g is odd.
- 𝒲̄₅ ∝ q·g(q), which is even, so the angle average need not vanish; my conclusion was a non sequitur.
- The isotropic part of q·g is a pseudoscalar. It vanishes in achiral crystals and survives in chiral TR-invariant ones (the q-linear
  gyrotropy ε^A_ij ∝ iγε_ijk q_k gives q·g ∝ γq²).
- T_d: the lowest pseudoscalar even polynomial is (x²−y²)(y²−z²)(z²−x²). Under S₄ᶻ (x→y, y→−x, z→−z) it changes sign, and under σ_d it
  changes sign, so the claimed degree 6 is correct.
- Also checked: Im 𝒲̄₂ ∝ q·Im S_{nj}, and TR makes Im S_{nj} even in q, so Im 𝒲̄₂ is odd in q and its angle average vanishes, as v3 states.

## 3. New errors or overstatements in the changed sections
- **N1 (§3.7, IF-6, minor, wording):** "above ≈ 0.54 MeV the allowed zero-phonon line leads (PAER/ZPL ≈ 10⁻³–10⁻²)" is not established.
  The 0.54 MeV class is the (2̄00) on-axis branch. §3.2 (c) itself says its amplitude is unknown and possibly small (the (200) potential
  Fourier component vanishes; the glide-forbidden reflection). The leading claim must be conditional on |ρ_cv| of that branch. The robustly
  allowed class is (1̄11) at ≈ 0.62 MeV [E]. Fix: "allowed by symmetry from ≈ 0.54 MeV; leads once |ρ^{(2̄00)}| ≳ (η_PA)^{1/2}|ρ^{ref}|,
  otherwise from ≈ 0.62 MeV ((1̄11))".
- **N2 (§3.7, [E14], minor):** the formula is correct. I re-derived it: (k_rel²/3)(1 + ζ_S²) = (ε + E_x^b)/(3a_x²E_x^b) with
  2μ_xE_x^b = 1/a_x²; the central value at ε = 0.1 eV is ≈ 2. But η_PA is calibrated against the *allowed* ZPL at PAER's excess energy
  (WP3 ratio 10⁻³–10⁻²). Using that number in the Si G = 0 region, whose own PAER amplitudes are WP3's, is an [E] transfer; label it so in
  IF-6b. The window bounds 0.338–≈ 0.43 MeV rest on it.
- **N3 (L3 (c), minor, tag):** "Their limits are therefore conservative by at least an order of magnitude" is labelled [D]. The [D] content
  is the bound (√r − 1)² for r ≥ 4 (C6c, correct). "At least an order of magnitude" needs r ≳ 20, which is the IP [E] estimate. Retag that
  clause [E].
- **N4 (§3.4 table, cosmetic):** the Si (2̄00) row's "pair offset +0.10 eV, electron at X" uses the parabolic M_x across X, where the Δ₁
  band sticks with Δ₂′. That is acceptable as [E], but the "validity" column should say "at X (band-sticking point; nonparabolic)", not
  leave it implicit.
- No new error found in §1.3–1.4, §2.2–2.6, §4.2, §5.2, §6, L10, L11, L14, L17, L19 or §8. The new checks C3c–d, C6c–e, C7b–d, C8b–c,
  C9a–g, C10c–e and C12e test the claimed identities. C9e and C9f reproduce my parabolic scan to the stated precision.

## 4. Summary
28/28 R7 items RESOLVED. All three rebuttals addressed to me are ACCEPTED:
- the Ge Γ onset: my 0.256 MeV was the flat-band floor, with a mis-scaled pair-energy term;
- the response count 12/18;
- the 𝒲̄₅ parity: q·g is even.

Also conceded: B-11 missed the (2̄00) on-axis Umklapp (REF-A right). New issues: N1 (the leading claim above 0.54 MeV must be
conditional on the unknown (2̄00) vertex), N2 and N3 ([E] tags), N4 (cosmetic). None changes a verdict.
