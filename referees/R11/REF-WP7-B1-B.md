# R11 referee REF-WP7-B1-B (hostile, isolated) on returns/R10/WP7-B1.md

Scope read: returns/R10/WP7-B1.md, code/WP7-B1/checks.py (re-run: 28/28 PASS, ~10 s), returns/R8/WP0-v3.md and WP4-v3.md (cited
sites only), CONVENTIONS, NOTATION, CONTROLS, DONE, LIMITS. Full text (arXiv HTML, fetched with lit.py into
literature/papers-r11-WP7-B1-B/, deleted at the end): 2212.04504, 2401.11971, 2208.05967, 1706.02487, 2607.09352, 2607.15338,
2507.07164, 2110.01587, 2011.13352, 1912.13484, 1604.06800, 1912.02822, 2203.06664, 2312.00866, 2604.26773, 1606.08849,
2103.08601 (17 of the 20 [FT] papers). No numerical simulations were run; only the return's own sympy/mpmath script was re-run.

## Verdict table
| # | Claim | Verdict | Reason (details in §§1–5) |
|---|---|---|---|
| 1 | (1.1) embedding lemma S = 𝓃_u\|F_⊥\|²S_d | STANDS | Connected inter-unit correlations vanish without inter-unit Coulomb at ω ≠ 0 (the static ⟨n⟩⟨n⟩ term is elastic). |
| 2 | E5 (E5.1)–(E5.2′): "binned = incoherent molecule sum, exactly" | STANDS WITH CORRECTION | Exact only up to O((𝔍^F/ΔE_𝔵𝔵′)²) inter-manifold mixing and the ω-variation of ε̃⁻¹ in w over the bin. The "new finding" is the classical Davydov oscillator-strength sum rule, not new (§1.1). |
| 3 | LB1-1 (1912.02822 (11),(13),(19); 2103.08601 (8),(9)) | STANDS | Quotes verified [FT]. The 1/(8π) and η/2q chain is correct (C1b, C1c). |
| 4 | E8(a) (E8.1), LB1-2 (2607.15338) | STANDS WITH CORRECTION | Formula right. (i) The f-sum is the band-projected Schwinger-term sum, not WP0 (4.6). (ii) The "new finding" gv = v_F is textbook (Haldane's v_J = v_F) and explicit in the source itself (v_g = v_F/g). (iii) Missed: the source is a 1-channel model, but CNTs have N_ch = 4, so at a given measured g_c its rate is low by ×4 (§1.2). |
| 5 | E8(b) (E8.2), E12 (E12.1), LB1-3 (2312.00866 part) | STANDS | Algebra checked (C6a–c, units HL e² = 4πα). One wording error: "halves v_C^{2D} up to 2.4" should read "divides by (1+ε_sub)/2 ≈ 2.4". |
| 6 | E8(c) demon weight (E8.3), LB1-3 (2507.07164 part) | STANDS; novelty FALLS | (E8.3) is correct (C3). "Neutral demon invisible at q ≪ k_TF" is Pines (1956), and 2507.07164 itself calls it "a neutral collective mode". Missing leading correction: Landau damping by the light species (§1.3). |
| 7 | E9 (E9.1)–(E9.3); LB1-4 (2110.01587 Eq. (16) exact at any filling) | STANDS (claim CONFIRMED) | Quote verified. I re-did the algebra: Eq. (16) is identically the uniaxial EMT. The source's own k_x = 0 remark is exact too. This is a strengthening, not an error. |
| 8 | E10 (E10.2)–(E10.3); LB1-5; "2208.05967 Eq. (16) conservative ×≈6" | STANDS WITH CORRECTION | Local-field algebra correct (C5, Maxwell–Garnett). Misquote: the source does not say ε is bulk (ε from Ref. [139]; data "readily available for QDs with d = 5 nm"). The factor 9\|ε_in\|²/\|ε_in+2ε_out\|² exceeds 1 only where \|ε_in+2ε_out\| < 3\|ε_in\|. The return evaluates it at 1 eV, outside the source's ≥ 2.5 eV regime, and the UV part of the source range can be optimistic (§2.3). |
| 9 | E12.2, LB1-6 (1606.08849 (5),(7); 1706.02487 Eq. (23) misprint) | STANDS | Quotes verified. Misprint CONFIRMED (§2.4). |
| 10 | X6(a), LB1-7 (2011.13352 (1),(11),(12)) | STANDS WITH CORRECTION | Quotes verified. Notation collision: the source's ε̃ is the symmetrised RPA matrix, while NOTATION ε̃ is the unsymmetrised test-electron 1 − f_HxcR⁰. C7 only compares prefactors once dP/dω is assumed, so it does not test the (W.5) → dP/dω step (§3.1). |
| 11 | X6(b) (H_W) Wannier picture, LB1-8 (1912.13484 (2.7)–(2.8)) | STANDS as [D, sketch] | Quotes verified. The 2011.13352 "itinerant" characterisation is fair (its §II.1, after Eq. (6)). |
| 12 | X8 (X8.1)–(X8.2), LB1-9 (2604.26773 (1),(6)) | STANDS | C8 exact. Quotes verified. |
| 13 | A2 (A2.1)–(A2.2), IF-B1-1, LB1-10 (1604.06800) | STANDS WITH CORRECTION | Quotes verified, C9a/b correct. The E-function (case-I) Holstein form is Allen, PRB 3, 305 (1971), which 1604.06800 itself cites. It must be cited as the source of (A2.2) and of the IF-B1-1 "refinement". It is not a new finding (cf. LIMITS L15 note). |
| 14 | A6 (A6.1)–(A6.2), LB1-11 (2212.04504) | STANDS WITH CORRECTION | Eq. (12) misprint 3q̃ → 3q̃² CONFIRMED. "Lyman (bound) lines absent / missing" REFUTED: the source adds bound-to-bound transitions from optical data (§ Sub-ionization, Fig. 7). The Mott proximity is understated (§2.1). |
| 15 | I3 (I3.1)–(I3.3), LB1-12 (2203.06664), IF-B1-5 | STANDS | C11 exact. The O(v) cancellation also holds for anisotropic even S (sphere centred at m_χv). Quotes verified. |
| 16 | I5 (I5.0)–(I5.1), LB1-13; "2401.11971 Eq. (5) lacks (1 − ω²/Q²)²" | STANDS (claim CONFIRMED) | The source's own S.9–S.12 couple ū γ⁰u to ρ̂ only (§2.2). The 2607.09352 mixed-𝒳 caveat is CONFIRMED as a methodological caveat (not an error). C12c is tautological. |
| 17 | "28/28 PASS" as verification | STANDS WITH CORRECTION | Re-run passes. C7 and C12c encode the claimed result as input, and C1c tests one value only, so they do not count as independent verification (§3.2). |

## 1. Derivations and novelty (rubric a, f)
**1.1 E5 binning theorem.** Σ_λ|Σ A^{λ*}w|² = Σ|w|² needs three things. (i) A restricted to the bin must be unitary. That fails at O((𝔍^F/ΔE_𝔵𝔵′)²) when 𝔍^F
mixes an in-bin manifold with an out-of-bin one; the return states 𝔍 ≪ ΔE as a hypothesis but then writes "exactly". (ii) w_𝔬𝔵(q) must be
ω-independent across the bin, which holds only when ε̃⁻¹(q,ω) is flat over the bin; this is fine for qa ≫ 1, where the return uses it. (iii) No other
𝔵′ may fall inside the bin. Correction: "exact up to O((𝔍^F/ΔE)²) and the bin-scale ω-dependence of the out-state weight". Novelty: conservation of
total oscillator strength under Davydov splitting is classical molecular-exciton theory. Drop "new finding".

**1.2 E8(a) Luttinger modes (LB1-2).** (E8.1) is correct: the C2a–c pole and residue, v_C^{1D} = 2αI₀K₀ (HL), and the N_ch = 4 Kane–Balents–Fisher form.
Three corrections:
- (i) The sum rule used is ⟨[[H,ρ_q],ρ_−q]⟩ on linear bands (the anomaly/Schwinger term). It is a band-projected partial sum, not WP0 (4.6), whose
  right-hand side is πn_eq²/m_e over all electrons. For Dirac CNT bands v_F is unrelated to k_F/m_e, so the C2d note "(Galilean, n = Nk_F/π)" does not
  apply. Rephrase: "a pair with gv ≠ v_F violates the projected sum rule unless velocity-dependent (g₄ ≠ g₂) couplings are present".
- (ii) gv = v_F for g₂ = g₄ is textbook (Haldane 1981, v_J = v_F). The source also states v_g = v_F/g [FT, "Detectors" section], so it is not new.
- (iii) **Missed source discrepancy.** 2607.15338 Eqs. (1)–(4) are a spinless single-channel model (c_R, c_L only). Its benchmark g = 0.2–0.7 is the
  measured CNT charge-mode parameter of the 4-channel theory (its refs. [41, 9, 14]). By the return's own (E8.1) and C2c–d, the 4-channel density
  response is S = 4g_c|q|δ(ω − v_F|q|/g_c). The free limit (g_c = 1) must give the 4-channel f-sum 4v_Fq². So at fixed g_c the source's S_1D, and
  its rate Eq. (6), are low by N_ch = 4. LB1-2 should read "DERIVED at N_ch = 1; for CNTs ×N_ch = 4 at fixed g_c (source understates)".

**1.3 E8(c) demon.** (E8.3) is right (C3b). It assumes the light species is static, so it needs Ω_{p,2}/k_TF,1 ≪ v_F,1. It drops the Landau damping
Im ε₁ ≈ (π/2)(k_TF,1²/q²)(ω/qv_F,1). That damping is the leading correction (it broadens the mode and moves weight), and it must be listed. The
q⁴/k_TF⁴ suppression of the acoustic-plasmon weight is Pines (1956). 2507.07164 already calls the Sr₂RuO₄ demon "a neutral collective mode"
and reports the acoustic plasmon as giving "weaker" support (SM §VIII). The novelty claim falls; (E8.3) remains a useful explicit formula.

**1.4 E9, E10, E12, X8, I3.** I checked the following and they are correct:
- the C4a lattice sum (HL: e²/2q per sheet);
- the q_∥a_s → 0 and a_s → ∞ limits;
- the Rytov dispersion and its EMT limit;
- the multipole factor (2ℓ+1)ε_out/(ℓε_in+(ℓ+1)ε_out);
- Maxwell–Garnett 9ϕ Im ε_in/|ε_in+2ε_out|²;
- graphene Im χ⁰ = −(g/16)q²/√(ω²−v²q²) with Re χ⁰ = 0 above the cone, so (E12.1) has the right denominator;
- the hydrogenic 1s→2p₀ boost probability;
- the exothermic shell integral;
- the edge law ∝ (|Δ_χ|−ω)^{−1/2}.
Minor overclaim in E9: a zero-thickness sheet (N_lay = 1) does not resolve the finite-thickness film modes of WP4-v3 [4.5]. IF-B1-2 should say
"for films with d ≪ 1/q".

**1.5 A2.** Two items check out: the T-parity argument (i[j,g] is T-even, so the pair coherence factor is (EE′+Δ²)/… and finite at threshold), and the
Landen identity (C9b). Allen (1971) derived exactly this E-function form for phonon-assisted absorption in superconductors. 1604.06800
cites it in its reference list and Eq. (17) is it. Under DONE rung 1 ("Standard is not a step: cite it"), (A2.1) and (A2.2) must cite
Allen 1971. IF-B1-1 then only aligns WP4-v3's sentence with Allen.

## 2. Claims that published papers are wrong (rubric c)
**2.1 2212.04504 Eq. (12): "3q̃" should be "3q̃²". CONFIRMED.** The HTML (from the LaTeX source) prints (3q̃ + k̃² + 1). The hydrogenic GOS
(Bethe form q²(q² + (1+k²)/3)) has 3q̃². C10's Coulomb-wave partial-wave sum agrees with 3q̃² to 10⁻⁶ and differs from the printed form by ×2.23
between q̃ = 0.5 and q̃ = 2. The absorption limit q̃ → 0 is unaffected. The impact on their scattering numerics is UNRESOLVED (not checked by the
return or by me).
**Claim (ii), "bound Lyman lines absent": REFUTED as stated.** Eq. (12) contains only ionisation. The paper's section on sub-ionization energy
depositions explicitly adds bound-to-bound transitions, taking the ELF from optical data (𝒲(q,ω) ≈ 𝒲(0,ω)), with reach curves in Fig. 7.
Correct LB1-11 to: "bound lines are treated phenomenologically in the source (q-independent optical ELF); (A6.1) gives their q dependence".
**Claim (iii), Mott margin: understated.** The quoted numbers are right: n_D = 1.8×10¹⁸ cm⁻³ and a* = 23 a.u. (variational, their ref. [93]),
which give 𝓃_D^{1/3}a* = 0.148. But the measured Si:P transition is ≈ 3.5–3.7×10¹⁸ cm⁻³ (the source says "≳ 3·10¹⁸"), so n_D/n_c ≈ 0.5–0.6. The
EMT criterion with a* = 23 a.u. puts n_c ≈ 10¹⁹. The source itself needs a Mermin width Γ = 70 meV to fit the n_D = 1.8×10¹⁸ data. So
"impurity-band broadening as a correction" should be "impurity-band/cluster effects O(1) near the edge at this density".

**2.2 2401.11971 Eq. (5) lacks (1 − ω²/Q²)². CONFIRMED.**
- The source's supplementary Eqs. (S.9)–(S.12) write the amplitude as ū γ⁰u · g_χg_e/(Q² − ω² + m²) · ⟨f|ρ̂(Q)|0⟩. Only the time component is
  kept: the DM current's −J_χ·J_e part is dropped entirely.
- With both currents conserved (ωJ⁰ = Q·J), the longitudinal part of J_χ·J_e is J⁰_χρ(1 − ω²/Q²). I re-derived (I5.0) independently.
- Hence their density-channel rate is too large by (1 − ω²/Q²)⁻². Since ω/Q ≤ v_χ (E_χ is convex in p), that is ≤ (1 − v_χ²)⁻² = 1.78 at v_χ = 0.5.
- For the light mediator their |F_DM|² ∝ (Q² − ω²)⁻² is non-integrably enhanced as Q → ω, which ultra-relativistic CRDM can reach (Q_min → ω). The
  correct longitudinal propagator is Coulombic, 1/Q².
- Their stated NR-limit check (Eq. (5) → g²/(Q²+m²)²) is satisfied by both forms, so it cannot catch the error.
- Caveat to add: near Q ~ ω the optical ELF and the transverse in-medium pole (the return's Cherenkov remark) dominate, so the numerical size of the
  correction to their Fig. 3 is UNRESOLVED without recomputation.
- C12c builds the factor in by hand (J_L = (ω/Q)J⁰). It is a restatement, not a check.

**2.3 2208.05967 Eq. (16): bulk ε for dots in solvent, "conservative ×≈6". STANDS WITH CORRECTION (claim UNRESOLVED as quantified).**
- Physics: for a dilute suspension with k_φR ≪ 1, the macroscopic ε_eff governs the k → 0 dark-photon self-energy. Per dot, Im(−1/ε_eff)/ϕ =
  9 Im ε_in/|ε_in+2ε_out|², against Im ε_in/|ε_in|² in κ²σ_A/|ε|². The missing local-field factor is real whatever ε_in is used.
- Misquote: the source says σ_A was "measured for bulk PbS"; ε comes from Ref. [139] (Hechster & Sarusi 2017), and it says such data are "readily
  available for QDs with d = 5 nm". The return's "uses bulk PbS σ_A and ε" must become "uses the material ε_in, not the composite ε_eff".
- Sign of the effect: the ratio 9|ε_in|²/|ε_in+2ε_out|² is > 1 only where |ε_in+2ε_out| < 3|ε_in|. The return's ≈ 6 uses ε_in ≈ 17 "near 1 eV", but
  the source restricts itself to bulk-like absorption above ≈ 2.5 eV and plots to ≥ 10 eV. Where |ε_in| → O(1) (far UV), the factor drops below 1
  (e.g. 0.7 for ε_in = 1+i, ε_out = 2), so the source is optimistic there.
- Replace "conservative by about this factor" with "off by 9|ε_in|²/|ε_in+2ε_out|² (> 1 in the visible/near-UV where |ε_in| ≫ ε_out, ≤ 1 in the far
  UV); size over their mass range not computed".

**2.4 1706.02487: "E_r = k′²/2M_χ" should be "k′²/2m_e". CONFIRMED.** The text before Eq. (23) defines E_r = k′²/(2M_χ) for the electron recoil energy.
dR/dlnE_r = (k′/2)dR/dk′ does not depend on the mass, so Eq. (23) is unaffected, as the return says.

**2.5 2607.09352 Eq. (10), mixed 𝒳. CONFIRMED as a caveat.** Eq. (10) multiplies the QCDark IP |F_c|² by a jellium Mermin |ε⁻¹|² (Γ = 3.2 eV). This
is not one 𝒳 rung, as the return says. The source reports agreement with QCDark2 (RPA) in its window (Fig. 3), so this is a consistency
caveat, not an error. The flux conversion dn/d³v = (dΦ/dv)/(4πv³) for an isotropised flux is correct.

**2.6 2110.01587 Eq. (16).** The return calls it exact beyond the stated d/L ≪ 1. CONFIRMED (sympy-equivalent identity; I also checked the k_x = 0
limit by hand). Wording to fix: the source's d is the ε₁ thickness, so the return's f_fill ↔ (1 − d/L) mapping must be stated.

## 3. Checks and consistency (rubric d, e)
**3.1 X6(a) notation.**
- 2011.13352 Eq. (13) defines ε̃_{GG′} = δ − (4πα/V)/(|k+G||k+G′|)·χ⁰: the *symmetrised RPA* matrix.
- NOTATION (row "ε̃") reserves ε̃ for the *unsymmetrised test-electron* matrix 1 − f_HxcR⁰.
- So the return's S^{ee}_{GG′} = (2|p+G||p+G′|/e²)Im[−ε̃⁻¹_{GG′}] is right only for the source's ε̃ with f_xc = 0. With NOTATION's ε̃ the prefactor is
  |p+G|²/f_Hxc-type, not |p+G||p+G′|/e².
- Fix: introduce ε^{sym} (or cite WP1's symbol) and state "RPA".
- C7 only verifies the overall constant after dP/dω = 4αZ²q²ℱ/(3M²ω⁴Ω) is assumed. The (W.5) → dP/dω step (isotropic average and G ≠ G′ symmetrisation)
  is untested by script. Its tag should be [D, sketch] unless a check is added.

**3.2 Script.** Re-run: 28/28 PASS.
- C12c inserts J_L = (ω/Q)J⁰ by hand and then confirms the factor it inserted.
- C1c evaluates the angular δ at the single value v_min = v/2.
- C2d's comment about the Galilean f-sum is irrelevant for Dirac bands (§1.2).
None of these is wrong; they should not be cited as independent verification.

**3.3 WP0-v3 and CONVENTIONS.**
- Units: HL (e² = 4πα) is used consistently: v_C^{2D} = e²/(q(ε₁+ε₂)), S = (q²/2πα)L, and (I3.3)'s α³m_e⁴.
- Rates are per target mass. E8 and E12 report per tube length or per area, as the sources do; those must be converted per CONVENTIONS before entering
  WP6 tables. The return notes this only in (1.1).
- IF-B1-6 (F_DM evaluated at the four-momentum) changes the CONVENTIONS §7 F_DM definition for relativistic DM. This needs an explicit CONVENTIONS
  amendment row, not only a flag.
- IF-B1-5 is consistent with WP4-v3 [7.2]: WP4's O(v/v*) concerns line positions (Doppler), while the return's O(v²/v*²) concerns ω-integrated or
  smooth-S rates. State that distinction in the flag.

**3.4 Computation specifications (rubric e).** Sufficient for E5, E8–E10, E12, A2, A6, I3: inputs, codes, grids, convergence criteria and costs are
given. Insufficient for X8.1, which has no BSE-at-finite-p convergence criterion beyond the "[E8] limit", and for I5's transverse/Cherenkov channel
(gap G-I5 is correctly declared). For E10, add the composite ε_eff (MG or Bruggeman by ϕ_QD) to the absorption specification.

## 4. Required corrections (minimal list)
1. E5: replace "exactly" by the O((𝔍^F/ΔE)²) and ω-flatness qualifiers. Drop the novelty claim.
2. E8(a)/LB1-2: the f-sum is the projected Schwinger-term sum, not (4.6). gv = v_F is textbook. Add: 2607.15338 is N_ch = 1, and CNT rates at
   fixed g_c are ×4.
3. E8(c): add Landau damping by the light species as the leading correction. Drop "new finding".
4. E10/LB1-5: fix the misquote (ε source). Make the factor's direction conditional (> 1 only where |ε_in+2ε_out| < 3|ε_in|). Evaluate it inside
   the source's ≥ 2.5 eV range or mark it [E, outside source range].
5. A6/LB1-11: delete "missing Lyman lines" (the source includes bound lines from data). State n_D/n_c ≈ 0.5 for Si:P (measured n_c), so
   impurity-band effects are not small.
6. A2/IF-B1-1: cite Allen PRB 3, 305 (1971) for the case-I E-function form.
7. X6(a): resolve the ε̃ notation collision (symmetrised RPA vs NOTATION test-electron). Retag the dP/dω step or add a check.
8. I5/LB1-13: keep. Add that the numerical impact on 2401.11971's reach is UNRESOLVED and that C12c is a restatement.
9. E8(b) wording: "divides by (1+ε_sub)/2", not "halves".

## 5. Literature-claim ratings (rubric c)
| Claim | Rating |
|---|---|
| 2212.04504 Eq. (12) 3q̃ → 3q̃² | CONFIRMED |
| 2212.04504 lacks bound (Lyman) lines | REFUTED (bound-to-bound included phenomenologically) |
| 2401.11971 Eq. (5) lacks (1 − ω²/Q²)² | CONFIRMED |
| 2208.05967 Eq. (16) conservative ×≈6 | UNRESOLVED (missing local field CONFIRMED; sign and size range-dependent; "bulk ε" misquoted) |
| 1706.02487 E_r = k′²/2M_χ misprint | CONFIRMED |
| 2607.09352 Eq. (10) mixed 𝒳 | CONFIRMED (caveat, not error) |
| 2110.01587 Eq. (16) exact at any d/L | CONFIRMED |
| 2607.15338 (not flagged by return) N_ch = 1 for a 4-channel CNT | new referee finding: rate ×4 low at fixed g_c |
