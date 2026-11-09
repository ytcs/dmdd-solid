# R11 referee report REF-WP7-B1-A (hostile, isolated) on returns/R10/WP7-B1.md

Scope: the return, code/WP7-B1/checks.py (re-run here: **28/28 PASS**, about 10 s), WP0-v3, WP4-v3 [6.1] (cited), CONVENTIONS, NOTATION, CONTROLS,
DONE, LIMITS. Full texts fetched with lit.py into literature/papers-r11-WP7-B1-A/ (deleted at the end): 2212.04504, 2401.11971, 2208.05967, 1706.02487,
2607.09352, 2110.01587, 1604.06800, 2607.15338, 1912.02822, 2103.08601, 2312.00866, 2203.06664, 2604.26773, 1606.08849, 2011.13352, 1912.13484,
2608.20715 (novelty check). No numerical simulations. Hand algebra is cited as [R].

## Verdict table
| # | Main claim | Verdict | Reason (details in the numbered sections) |
|---|---|---|---|
| 1 | (1.1)–(1.2) embedding lemmas | STANDS | Cross-unit terms vanish for dynamically independent units at ω ≠ 0; (1.2) = WP4-v3 [6.1] verbatim |
| 2 | E5 Frenkel (E5.1)–(E5.3), binning theorem, LB1-1 | STANDS WITH CORRECTION | "Exactly" is too strong: exact only if the bin holds the whole coupled manifold *and* w is ω-independent over the bin. The bare-f incoherent sum of 2103.08601 still needs qa ≫ 1 (§1) |
| 3 | E8(a) 1D Luttinger (E8.1), f-sum gv = v_F, LB1-2 | STANDS WITH CORRECTION | "gv ≠ v_F violates WP0 (4.6)" is an overclaim. The return misses that 2607.15338 uses one R/L channel, while for a CNT (N_ch = 4) the weight is N_ch g_c (§2) |
| 4 | E8(b,c) 2D sheet plasmon, demon weight (E8.3), LB1-3 | STANDS | C3a,b and C6b,c re-derived [R]; quotes of 2312.00866 (13)–(19) correct |
| 5 | E9 stack (E9.1)–(E9.3); 2110.01587 Eq. (16) exact at any filling, LB1-4 | STANDS | Claim CONFIRMED by hand algebra [R] and C4c; the quote is exact (layers ⊥ x, k_z in-plane) |
| 6 | E10 QD (E10.1)–(E10.3); 2208.05967 Eq. (16) local-field factor, LB1-5 | STANDS WITH CORRECTION | Physics CONFIRMED. The return misquotes which input is "bulk". The scattering-prefactor match (Eqs. (6), (10)–(12)) has no check and the source is dimensionally inconsistent: UNRESOLVED (§3) |
| 7 | E12 graphene (E12.1)–(E12.2), LB1-6; 1706.02487 misprint | STANDS | (E12.1) re-derived [R]; misprint CONFIRMED |
| 8 | X6(a) bremsstrahlung picture = (W.5) truncation, LB1-7 | STANDS | 2011.13352 Eqs. (11), (12) quoted correctly; C7 prefactor agrees with FT |
| 9 | X6(b) Wannier picture under (H_W), LB1-8 | STANDS WITH CORRECTION | Tagged [D, sketch], so its LIMITS status cannot read "DERIVED" (DONE rung 1) (§4) |
| 10 | X8 bound Migdal (X8.1)–(X8.2), LB1-9 | STANDS | C8 exact; 2604.26773 Eqs. (1), (6) quoted correctly; the (X8.1) size estimate is loose (§4) |
| 11 | A2 Holstein (A2.1), SC case-I (A2.2), IF-B1-1, LB1-10 | STANDS WITH CORRECTION | Formulas verified (C9a,b; source FT). (A2.2) and the case-I vs MB distinction are Allen, PRB 3, 305 (1971), which is the source's own Ref. [29]: not a new finding (§5) |
| 12 | A6 dopant (A6.1)–(A6.2); 2212.04504 misprint; "Lyman lines absent", LB1-11 | STANDS WITH CORRECTION | Misprint CONFIRMED; "Lyman lines absent" REFUTED. (A6.1) as written screens twice (§6) |
| 13 | I3 inelastic (I3.1)–(I3.3), O(v²) shell, LB1-12 | STANDS | C11 and the O(v²/v_Δ*²) and O(v)-cancellation arguments re-derived [R] |
| 14 | I5 relativistic DM (I5.0)–(I5.1); 2401.11971 Eq. (5) lacks (1 − ω²/Q²)², LB1-13 | STANDS WITH CORRECTION | Missing factor CONFIRMED (S.9–S.12). The transverse-row size estimate is wrong. The structure is the classical Fermi energy-loss formula and was already in 2608.20715: the novelty check missed it (§7) |
| 15 | §13 exact remaining gaps | STANDS | Each names a single missing step. Add the 2208.05967 prefactor (row 6) and the transverse-row size (row 14) |

## Published-paper error claims (rubric c)
| Claim | Rating | Evidence (full text) |
|---|---|---|
| 2212.04504 Eq. (12) prints (3q̃ + k̃² + 1); the correct form is (3q̃² + k̃² + 1) | **CONFIRMED** | HTML alttext and PDF both print `3\tilde{q}`. The hydrogenic GOS ∝ q²[q² + (1 + k²)/3] (Landau–Lifshitz §148), and C10 (exact Coulomb partial waves) agrees. Only the q-shape is affected; W(0, ω) is not |
| 2212.04504 omits the bound (Lyman) lines | **REFUTED** | App. VII.6 "Sub-ionization energy depositions and phonon signals" computes bound-to-bound transitions from optical data, W(q, ω) ≈ W(0, ω) for ω < E_I, with reach in Fig. 7 (scattering and absorption, n_D = 1.8×10¹⁸ and 3.4×10¹⁷ cm⁻³). Only Eq. (12) is ionisation-only. Correct reading: "Eq. (12) has no bound lines; the paper adds them empirically (App. VII.6); (A6.1)(a) supplies the theory form" |
| 2401.11971 Eq. (5) lacks (1 − ω²/Q²)² | **CONFIRMED** (magnitude caveat §7) | Supplement Eq. (S.9) uses the vertex ū γ⁰ u ⟨f\|ρ̂\|0⟩ only (J⁰ρ); (S.11)–(S.12) carry it to Eq. (5). With conserved currents J_L = (ω/Q)J⁰ and j_L = (ω/Q)ρ (WP0-v3 §5.3: S_{j_Lj_L} = (ω/q)²S_nn), the longitudinal amplitude is J⁰ρ(1 − ω²/Q²) [R] |
| 2208.05967 Eq. (16) uses bulk ε for dots in solvent (conservative ×≈6) | **CONFIRMED in substance, quote corrected** | The text reads "σ_A … While these were measured for bulk PbS"; ε is "obtained from Ref. [139]" (Hechster–Sarusi), and d = 5 nm is chosen "since dielectric-function data exists for this size". The omission is the depolarisation (Maxwell–Garnett) factor of a sphere in solvent, not "bulk ε". Factor 9\|ε_in\|²/\|ε_in + 2ε_out\|² re-derived [R]; ≈6–8 for \|ε_in\| ≫ ε_out [E] |
| 1706.02487: E_r = k′²/2M_χ should read k′²/2m_e | **CONFIRMED** | Text above Eq. (23): "recoil energy of the electron E_r = k′²/(2M_χ)"; dR/dlnE_r = (k′/2)dR/dk′ holds for either mass |
| 2607.09352 Eq. (10) mixes 𝒳 (IP \|F_c\|² × Mermin \|ε⁻¹\|²) | **CONFIRMED** | §III.2 and App. A: QCDark crystal form factor with a jellium Mermin ε (Γ = 3.2 eV), which the source itself calls a "valid alternative" pending QCDark2. Remark, not an error |
| 2110.01587 Eq. (16) exact beyond its stated "d/L ≪ 1" | **CONFIRMED** | ε_∥D − ε₁ε₂ = f(1 − f)(ε₁ − ε₂)² with D = fε₂ + (1 − f)ε₁ [R], so Eq. (16) = 1/(ε_∥ŝ² + ε_⊥(1 − ŝ²)) identically, in the quasi-static kL ≪ 1 regime |

## 1. E5 (Frenkel)
- (E5.2′) relies on unitarity of A^F over the **full** basis {𝔬𝔵}. With the hypothesis "𝔍^F ≪ E_𝔵 − E_𝔵′" the bin-integrated weight has an
  error of O((𝔍^F/ΔE)²) from inter-manifold mixing. There is a second error from the ω-dependence of ε̃^{-1}(q, ω) inside w across the bin.
  Replace "(exactly, interference terms cancel)" with "exact for a complete manifold with ω-independent w; otherwise O((𝔍^F/ΔE)², Δ_bin∂_ω ln ε̃)".
- The sentence "not an approximation that needs q ≫ 1/a" is true only for the **screened** vertices w_{𝔬𝔵}. 2103.08601 sums bare |f|². For
  q ≲ 1/a_mol, the local field (ε̃^{-1})_{G0} still differs from the bare sum, which is the return's own correction (ii). The source's stated reason
  (localisation at its q) is thus still needed for the *bare* sum. Reword.
- Novelty: "incoherent sum exact in bins" is a one-line unitarity identity (C1a). It is a lemma, not a "new finding".
- Quotes verified: 1912.02822 Eqs. (11), (13), (19) (ξN_Bρσ̄/(8πmμ²)); 2103.08601 Eqs. (8), (9) and the incoherence sentence. C1b and C1c re-derived.

## 2. E8 (1D and 2D plasmons)
- The f-sum argument is right for a projected model whose interactions are density–density. Its kinetic double commutator is then the free
  Schwinger term N_ch v_F q², so g v = v_F (C2a, C2d verified). But WP0-v3 (4.6) is the sum rule of the full Hamiltonian, π𝓃q²/m_e over all
  electrons, under hypothesis (L). A projected low-energy (g, v) pair does not have to saturate it. In lattice Luttinger liquids, projection
  generates non-density terms, so v_J ≠ v_F is allowed. Correct to: "violates the projected (Schwinger-term) sum rule of a density–density model;
  (4.6) itself is not tested by the low-energy pair".
- **Missed source correction.** 2607.15338 (FT, Eqs. (1)–(4)) uses "one right-moving and one left-moving electron mode" (spinless, single
  channel). In a metallic CNT, DM couples to the total density n = Σ_{i=1}^{4} n_i = √N_ch ∂φ_c/π, so S = N_ch g_c|q|δ(ω − v_c|q|), which is
  (E8.1) and C2c with N = 4. At the measured g (the charge-mode g_c, 0.2–0.7 in the source), the source's S_1D and rate are low by **N_ch = 4**.
  The three neutral modes (g = 1) do not couple to density. Add this to LB1-2's leading corrections and to §0. Its rating here is
  [D, this report]: it follows from (E8.1) and needs no new input.
- (E8.1) v_C^{1D} = 2αI₀K₀ is consistent with CONVENTIONS e² = 4πα (Gaussian 2e²I₀K₀ with e²_G = α). The (E8.2) and (E12.1) denominators and
  ω_pl² were re-derived [R].

## 3. E10 (quantum dots)
- (E10.2) C5 was re-derived. (E10.3): Im[−1/ε_eff] = (3ϕ/ε_out)Im β = 9ϕ Im ε_in/|ε_in + 2ε_out|² [R]. For a liter-scale colloid (size ≫ 1/ω), the
  in-medium transverse and longitudinal mixing at k → 0 both give Γ = κ²m Im(−1/ε_eff), so the factor is physical. CONFIRMED.
- Quote correction: see the table. The phrase "uses bulk PbS σ_A and ε ('measured for bulk PbS')" must become "bulk σ_A; ε of 5 nm dots from
  Ref. [139]; no depolarisation factor". The ×≈6 [E] uses ε_in ≈ 17 "near 1 eV", but the source's absorption reach runs to 10 eV, where
  |ε_in| ≫ ε_out and the factor tends to 9. State the ω range.
- **Scattering prefactor, UNRESOLVED.** LB1-5 lists 2208.05967 Eqs. (6), (10)–(12) as DERIVED with "N_t ↔ ϕ_QD", but no check covers it (C5 is the
  local field only). The full text has dimensional problems. Eq. (6) is N_tρσ̄/(8m_χμ_eχ)∫q dq η F²|f_QD|², with μ to the first power. Eq. (10)
  defines |f_QD|² with a δ(E) (dimension E⁻¹), while Eq. (12), the QEdark normalisation 2π²/(E_rαm_e²V_cell)…, is dimensionless. Eq. (6) is
  dimensionally consistent only with Eq. (10), yet it is evaluated with Eq. (12). The return must either show the WP0 (9.2) → Eq. (6) map with an
  explicit dimension check (a sympy line) or record the source's normalisation as UNRESOLVED. Until then LB1-5 is "DERIVED (structure; bulk
  limit), prefactor UNRESOLVED".

## 4. X6, X8
- X6(b) is tagged [D, sketch] throughout, and the sign and normalisation of the boost restriction to 𝒫^W_0 are not derived. LB1-8 "DERIVED under
  (H_W) [D, sketch]" violates DONE rung 1. Use "SKETCH under (H_W); exact remaining gap G-X6". The identity ⟨a|Σ∇V|0⟩ = m_eω²⟨a|R|0⟩ was verified
  [R]; it needs internal forces to cancel (true) and V_pot to be the electron–nucleus potential only.
- X6(a): the step to dP/dω = 4αZ²q²ℱ/(3M²ω⁴Ω) is asserted ("Then"), not derived. It is acceptable only by reference to WP3-v3 L7b (REFEREED).
  Say so.
- (X8.1) size [E]: the Migdal spectrum carries ω_e⁻⁴. Near-edge bound weight is therefore enhanced relative to the continuum by more than
  E_x^b/ω_e suggests, so the estimate is a lower bound. The conclusion for Si/Ge (negligible) is unaffected.

## 5. A2 (superconductors and metals)
- C9a reproduces 1604.06800 Eq. (16) (both branches, λ_tr = 2∫α²F/Ω), and C9b reproduces Eq. (17) with x·E(k), k² = 1 − 4Δ²/x². Quotes (8),
  (13), (16), (17), (19), (20) are exact. Γ_abs = κ²σ₁/|ε|² holds in HL units (ε = 1 + iσ/ω).
- **Novelty/attribution.** The source states "Following Ref. [29]", which is P. B. Allen, PRB 3, 305 (1971), for Eq. (17). The case-I elliptic
  form for phonon-assisted absorption in a superconductor, and its difference from Mattis–Bardeen (case II, E − b²K), are Allen's result. "New
  finding: 1604.06800 (17) = x𝔤_I exactly" and IF-B1-1 are re-identifications. Credit Allen. The Landen identity 𝔤_I(y) = E(√(1 − 4/y²)) is the
  standard case-I pair integral, so it **resolves LIMITS L15 / OW4-3 against novelty** of any "𝔤_I closed form". Record that.
- (A2.2) stays [D, sketch] (the T-parity argument for the off-shell vertex i[j, g]/ω is plausible [R], with T-even parity, but there is no Nambu
  calculation). LB1-10 already says so; keep G-A2.

## 6. A6 (dopants)
- **Double screening in (A6.1).** WP4-v3 [6.1] defines S^D with ñ_e = Σ_G(ε^{-1}_host)_{G0}n_e(q+G), so S^D contains the macroscopic
  (ε^{-1}_host)_{00}. Then lim(e²/2q²)S^D = ε₂^D/|ε_host|² (= 2212.04504's 𝒲, as the return itself states three lines later), **not** ε₂^D. The
  explicit right-hand side of (A6.1) (with 𝔣^loc a ratio that removes (ε^{-1})_{00}) is ε₂^D. As printed, the first equality inserted into
  Γ = κ²mε₂^D/|ε_host|² screens twice (rubric item "screening applied twice"). Fix: Γ_abs = κ²m lim_{q→0}(e²/2q²)S^D = κ²mε₂^D/|ε_host|², with
  ε₂^D defined by the explicit sum. CONVENTIONS §6 (ε₂ = (e²/2q²)S^{prop}) confirms that the proper part is meant.
- Finding (ii) is REFUTED (see the table). LB1-11 "Lyman lines added" becomes "theory form of the bound lines (source: empirical, App. VII.6)".
- Minor: the source's main projections (Fig. 2) use n_D = 10¹⁸ cm⁻³; 1.8×10¹⁸ is the appendix and data value. The Mott check holds for both
  (𝓃^{1/3}a* = 0.12, 0.15; a* = 23 a.u. is the source's value).

## 7. I5 (relativistic DM)
- The missing factor is CONFIRMED (table). The bound ω/Q ≤ v_χ holds for any convex E(p) [R]. For a crystal, S(q → 0, ω) = (q²/2πα)L(0, ω) ≠ 0,
  so the region ω/Q → v_χ is populated and the factor is not negligible.
- **Transverse row mis-sized.** (I5.1) gives the relative size of 𝔇_{j_Tj_T}S_{j_Tj_T} as O(v_χ²⟨v_e²⟩) ≲ 10⁻⁴. That holds only where
  ω/q ~ v_e. In the optical region ε_T(q → 0) = ε_L(q → 0), and continuity gives S_{jj} ~ (ω/q)²S_nn. The transverse/density ratio is therefore
  O(v_χ²(ω/q)²), up to O(v_χ⁴), which is the same order in ω/q as the retained (1 − ω²/q²)² correction times v_χ². The full text of 2608.20715
  (Aug 2026, before R10) finds the transverse term up to O(8%) of the longitudinal one at ω ≲ 1 eV for v_χ ≃ c (HEG RPA), and 10⁻⁶–10⁻⁴ only in
  the plasmon window. Replace the [E] with "O(v_χ²ω²/q²); ≤ 10⁻⁴ in the plasmon window, up to ~10% at ω ≲ 1 eV for v_χ → 1 (2608.20715)".
  Including (1 − ω²/q²)² while dropping the transverse row is consistent only to leading order in v_χ²; at v_χ ~ 0.5 near ω/q → v_χ, both must
  be kept.
- **Novelty/literature (rubric f).** (I5.0) is the conserved-current form of the classical Fermi (1940) energy-loss formula. 2608.20715 Eq. (2)
  gives exactly Im(−1/ε_L) + (v_χ² − ω²/Q²)Im[−Q²/(ω²ε_T − Q²)], including the Cherenkov-type transverse pole that §12 calls "[D for the
  structure]". The return's literature list does not contain 2608.20715. Cite it and Fermi, drop any novelty for the transverse/Cherenkov
  channel, and keep only the specific diagnosis of 2401.11971 Eq. (5).
- "NR basis accurate to ~1% for v_χ ≲ 0.1": (1 − v_χ²)² = 0.98 at 0.1, so it is ≲ 2% on the rate near the edge. Minor.
- 2607.09352 caveats are verified (θ_iso anisotropy, §III.1; mixed 𝒳, §III.2).

## 8. Consistency (rubric d) and checks
- Units: e² = 4πα, v_C = e²/k², f-sum π𝓃q²/m over ℝ, and S ↔ L are used consistently (CONVENTIONS §1, §6, §13 item 12). WP0 citations checked:
  (3.3), (3.5)–(3.6), (4.6) with hypothesis (L), (5.1), §5.3 (S_{j_Lj_L} = (ω/q)²S_nn), §7.2.
- NOTATION: no hard collisions found. The new ε_b (interlayer background) sits next to the existing ε_bg (remote-band background); rename it to
  ε_b,lay, or reuse ε_bg if the meaning is the same. 𝒫^W_0 joins the projector family (𝒫₀, 𝒫_⊥, 𝒫_GS) and should be listed with them.
- Checks: 28/28 PASS reproduced. C1a, C7, C12a–c and C9a are algebraic identities of formulas the return states; they do not derive them. That
  is acceptable, but the LIMITS "DERIVED" tags should rest on the text derivations, not on these checks. E10 has no rate-prefactor check (§3).
- Rung-4 rubric: Bose factors (only (E9.1) at T > 0, correct); spin factors (E10.1 ×2, A6 ×1, E12 g_deg) correct; q sign (sources with
  opposite e^{±iq·r} flagged as immaterial for |f|², correct); dipole limit used only at q → 0 (A6, E10 absorption). Screening twice: §6.

## 9. Required corrections (for the coordinator)
1. §6 / LB1-11: drop "missing Lyman lines" as a source error (REFUTED); fix the (A6.1) double screening.
2. §7 / LB1-13: re-size the transverse row as O(v_χ²ω²/q²) and cite 2608.20715 and the Fermi formula; no novelty for the transverse/Cherenkov
   structure.
3. §5 / LB1-10 / IF-B1-1: credit Allen (1971); record that 𝔤_I's closed form is not new (closes L15 / OW4-3 on novelty).
4. §3 / LB1-5: correct the quote (bulk σ_A, QD ε); mark the 2208.05967 Eq. (6)/(10)/(12) prefactor UNRESOLVED or add a dimension check.
5. §2 / LB1-2: soften the "violates (4.6)" sentence; add the N_ch = 4 undercount of 2607.15338.
6. §1 / LB1-1: qualify "exactly"; the bare incoherent sum still needs qa ≫ 1.
7. LB1-8: status "SKETCH under (H_W)", not DERIVED.
