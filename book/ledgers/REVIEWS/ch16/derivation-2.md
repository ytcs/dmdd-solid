# Ch16 part 2 derivation check (s16-4, s16-5, s16-6; ch16.tex opening)
Reviewer: isolated derivation verifier, 2026-11-06. Sources were fetched with lit.py into sources/review-ch16/<id>/; the PDFs are deleted and the text and HTML are kept.
Read: 1604.00041 (Rangel), 1912.02822, 2103.08601 (Blanco), 2212.04504 **v1** (Du), 0812.0148 (Vinh), 1705.03016 (Budnik),
1608.02940 (Essig), 2104.13926 (Cogswell), 2503.20732 (Araujo), 2412.21060 (Guerrero-Perez), 1803.02903 (Agnese), 1910.10716 (Griffin).
Not open or not read: Brock–Dunitz 1990, Huber–Herzberg, Kohn–Luttinger 1955, Doherty 2013 (not needed).
Independent scripts are in the scratchpad: chk1.py (GOS sum rules, valley lines, borrowing), chk2.py (Du f-sum), chk3.py (misprint impact).
I recomputed the numbers from the cached logs in figscripts/ch16 (frenkel16_4, we16_4, fig16_4, limit16_4a, donor16_5, gos16_5, valley16_5,
mott16_5, we16_5, limit16_5a, fig16_5, fig16_6, we16_6, limit16_6a), and ran nothing heavy.
Verdict summary: 6 WRONG (all small or wording, none changes a printed result), 7 GAP, everything else CHECKED.

## WRONG (correction required)
W1. s16-6 l.26 (Budnik reduction): "their $\sigmae$ times $A^2/\mu_{\chi n}^2$". Budnik's cross-section is the DM–nucleon σ̄_n
  (1705.03016 Eq. (1), (7): "σ̄_n is the DM-nucleon interaction cross section"), not σ̄_e.
  → "their per-nucleon cross-section σ̄_n (σ_p of eq:2.2-nucleus) times A²/μ_χn² is σ_N,κ/μ_χκ²".
W2. s16-6 l.113: "Essig et al. found that quantum effects lower the mass threshold by about 10 % ..., which lies between."
  The book's own shifts are factors 0.84 (impulse) and 0.75 (improved Born), i.e. lowerings of 16 % and 25 %, so Essig's O(10 %)
  (1608.02940 p.6 and Eq. (3.8); 0.90 for H₂ with Δp = 6.53 keV, limit16_6a.log 0.9022) is smaller than both, not between them.
  → "...by about 10 %, less than either: their estimate, Eq. (3.8), shifts q_min by one standard deviation of the momentum only."
W3. s16-6 l.30 and the fig16_6 caption (a): the electronic F–H route. The text says the threshold is the exciton energy, which lies below the
  14.2 eV gap, but then gives the gap mass (2×14.2/v_max² = 4.044 MeV ✓ arithmetic) as the requirement, and the caption labels
  "the exciton route at the band gap ... needs 4.0 MeV". The route opens at the (free) exciton energy, so its mass threshold lies below
  4.0 MeV. With the commonly quoted LiF exciton peak ≈ 12.6 eV (no source in the book; one must be added) it is ≈ 3.6 MeV, and the
  ratio to the 0.186 GeV fluorine displacement becomes ≈ 52, not 46. → Either quote 4.0 MeV as "to deposit the gap (an upper bound
  on the exciton-route threshold)" in both places, or add a sourced exciton energy and recompute (2E_x/v_max²).
W4. s16-6 l.36: "the two emissions grow with time constants of 6.5 and 9 h", read in the order F₂⁰, F₃⁺ just named. In the source
  6.5 h belongs to F₃⁺ and 9 h to F₂⁰ (2503.20732 Fig. 3 text, l.258). → "with time constants of 9 h (F₂⁰) and 6.5 h (F₃⁺)".
W5. s16-5 Limit Check 16.5a box text: it writes "W(0,m_φ)" and "W = ε₂^D/|ε_host|²". NOTATION reserves W for the Debye–Waller exponent
  (row W_κ), and the campaign rename list (CORRECTIONS v3: "W (quoted ELF) → L") maps the quoted ELF to L. The section itself uses L^D.
  → L^D(m_φ) = ε₂^D/ε_host² in the box.
W6. s16-4 l.56: "their momentum transfer has the opposite sign". This holds for Blanco et al. 2020 (1912.02822 Eq. (12),
  ω = q²/2m_χ − q·v), but the sentence refers to the 2021 trans-stilbene paper, whose Eq. (8) δ(ΔE + q²/2m_χ − q·u) and Eq. (9) e^{iq·r}
  use the book's sign. → attribute the sign remark to blanco2020dark Eq. (12). (The √2 of Eq. (9) is correctly stated.)

## GAP (unsupported or incomplete statement)
G1. Limit Check 16.4a text (l.82): "For a heavy mediator between 1.2 and 7.5 MeV, and for a light mediator at every mass above 1.2 MeV ...
  10 to 35 %". limit16_4a.log shows |ratio − 1| = 0.1 crossings at 1.004, 1.172, 7.491 MeV (heavy) and 0.999, 1.198 MeV (light), and a ratio of
  1.38/1.39 at 0.90 MeV. The ratio is also off by more than 10 % just above threshold, 0.88–1.0 MeV, where the full model's lowest exciton
  (threshold 0.862 MeV) differs from the binned line. The box should state this window (or say "above 1.0 MeV"). Also, at 0.9 MeV the
  heavy ratio exceeds the stated "10 to 35 %" range only marginally (1.38), so the range should read 6–38 %.
G2. s16-5 l.60 (line strengths): "a factor of 3.2 to 3.4 below those of the effective-mass envelope" holds for the 2p lines only
  (2p₀ 3.16, 2p± 3.35; fig16_5.log). For 3p₀ it is 1.88 and for 3p± 2.66. → "the 2p lines a factor 3.2–3.4 (3p: 1.9–2.7)". The same
  "×3.2–3.4" bracket in editor-notes should carry the same qualifier.
G3. s16-5 eq:16.5-E and the numbers 0.022 / 0.0032 (CHECKED arithmetic below) assume one and the same variational envelope for A₁ and E.
  The section itself says that the central cell contracts A₁ (31.3 → 45.59 meV and line strengths ×1/3). With different envelopes the
  bracket becomes the difference of the A₁–E overlap transforms, still zero along [111] and at q = 0, but of different size. → add
  "with a common effective-mass envelope; the central-cell contraction of A₁ changes the size (App. E.21)".
G4. s16-5 l.36 and l.40: "In effective-mass theory that ratio [the local field] is eq:16.5-floc, close to one." Nothing is computed (the text calls
  it an open input). The Lorentz value (ε+2)/3 ≈ 4.5 is what the photoionization literature behind Du's 2.2 uses. The argument that applies
  is that the orbit spans ~10³ cells, so the Lorentz cavity construction fails. Say this in one clause, or soften to "expected close
  to one". The derivation of eq:16.5-floc itself is CHECKED.
G5. s16-6 l.93: the CM Doppler spread "(⟨ω⟩_CM/4M_1)^{1/2}" is the homonuclear special case. In general δv_min = P_z/M_mol with
  ⟨P_z²⟩ = M_mol⟨ω⟩/2, so σ_v = (⟨ω⟩_CM/2M_mol)^{1/2}. This equals the printed form for H₂ (1.63e-6 ✓, "2e-6"). → write the general form.
G6. s16-6 l.36: "Araujo et al. count one emitting aggregate for every two or three [vacancies]". The source infers it ("the number of color
  centers is 1/3 to 1/2 of those numbers", l.170, from F₂⁰/F₃⁺ stoichiometry); it does not count. → "estimate".
G7. Measured inputs that are still missing (review requests): no open source was found for the measured anthracene Davydov splitting (quick
  arXiv search; neither Rangel nor Blanco quotes it) or for measured Si:P line oscillator strengths. Keep the model labels. (Literature
  memory, unsourced: the measured splitting is ~200–220 cm⁻¹ ≈ 25–27 meV, with the b-polarized component lower, consistent with the model's 31 meV
  and its ∥b ordering.) Section numbers cited for Du (II, VII.1, VII.2, VII.6) follow the arXiv HTML numbering of v1 and match it.

## Notation drift (against NOTATION.md)
N1. None of the new 16.4–16.6 symbols has a NOTATION row: 𝔍, 𝔬, 𝔵, A^λ, F_𝔬𝔵, N_mol, 𝓑, θ_CT, t_CT, f_CT, E_Fr, E_CT, ε_host, 𝔣^loc_D,
  𝒰_{j′j}, S^D, L^D, ε₂^D, ε^D, y, α_pol, Y_CC, p_surv, p_q, f_opt, p_FH, ⟨N_X⟩, p_esc, M_1, M_mol, μ_12, q_12, p_12, E_bond, ω_vib, σ_ω,
  y_L, k, g(ε), ϵ, T_d, E_int. Clashes to rule on: Lindhard ϵ (reduced energy) and k against the dielectric ε and the wavevector k;
  g(ϵ) against g_deg; y (Maxwell Garnett) against y_L; ε_host against ε₀ (NOTATION row 493 uses ε₀ in the donor Coulomb term of 7.4, D.23);
  𝔵 against the existing state labels; a* is defined in 16.5 as (2m*E_b^D)^{-1/2}, which matches the row's ε₀m_ea₀/m* only for the
  hydrogenic donor (true here).
N2. p_FP: the NOTATION row calls it a "Frenkel-pair survival probability", but 16.6 defines it as the formation probability and keeps
  survival in p_surv. Align the row to the 16.6 meaning.
N3. No factor-2, π or sign drift found. 2π/Ω per cell, 1/4π = 2π·π/(2π)³, and L = (e²/2q²)S with e² = 4πα: Du's (2π)²αn_D/q² of
  their Eq. (10) equals the book's 4π²αn_D/q² ✓. The singlet √g_deg sits inside f ✓. The Lorentzian peak 2/πΓ ✓.

## CHECKED: s16-4 (molecular crystals)
- 0.883 MeV = 2×3.1 eV/v_max² (v_max = 2.6502e-3) ✓. Rangel Tables I–III: gas S1 3.5, crystal S1 3.1, gas gap 7.4−0.5 = 6.9, crystal gap
  3.9–4.2, G₀W₀-BSE S1 3.3, T1 1.9 ✓. Blanco 2021 Φ_FB ≥ 0.63 (Sect. IV B) ✓, Eq. (A1) −0.63ħ²/(m_e x²) ✓; Blanco 2020 Z_eff = 3.15 (Eq. 2) ✓.
- Exchange-only coupling between molecules at zero overlap, and the CT decoupling: correct qualitative reduction of eq:4.9-kernels.
- eq:16.4-S → eq:16.4-binned: Σ_λ|Σ A*F|² = F†(Σ_λ A A†)F = Σ|F|² = Σ|f|² (|e^{iq·r}| = 1) when the set is closed under 𝔍 ✓.
  **Davydov sum rule** Σ_λ|ê·d_λ|² = Σ_𝔬|ê·d_𝔬|² follows from the same completeness ✓ (numeric 2×2 check: 1.69288 = 1.69288, we16_4.log).
  Oscillator strengths add only to O(𝔍/E): ratio 0.9337 vs the energy ratio 0.9366 ✓ (stated as "close to", correct).
- **eq:16.4-borrow, first order** (sympy, 2-level perturbed eigenvector): δW = 2F₁F₂J/(E₁−E₂), equal and opposite in the outside level;
  the normalization correction is O(J²) ✓. Sign and Hermitian placement as printed ✓. Consistent with the CORRECTIONS row of 2026-11-06.
- eq:16.4-rate: ∫d³v f δ(ω − q·v + q²/2m) = f̂(v_min)/q; prefactor πσ/μ² · 2π/(2π)³ = σ/(4πμ²) ✓. ∫dΩ_q f̂ = 2πη exactly ✓ → isotropic
  form ρσ/(2mμ²M_cell)Σ∫q dq η F²⟨|f|²⟩ ✓, which equals Blanco 2020 Eq. (19) (N_B ρσ/(8πmμ²)∫d³q/q) and Blanco 2021 Eq. (8) ✓. Dimensions ✓.
- Static ε_mac−1 = (2e²/Ωq²)Σ|f|²/E finite at q→0 ✓. qv₀ = 1.6 eV at 2 keV ✓. 2×4 eV/v_max² = 1.14 MeV ✓.
- Model numbers vs frenkel16_4.log: S1(PPP) 3.851 eV, shift −0.751, |d| 0.920 eÅ, f 0.2296 (my 2m_eω|d|²/3 = 0.2295), B_b 4.492 eV / f 2.458,
  L_b +18 meV, dipole-free ✓. Angles 30.7°/26.9°/51.5° ✓. Overlap: +1.4 % (2 keV), +10.8 % (4 keV); L_b 0.5 %, 16 % ✓.
  a_mol 2.66 Å, q a_mol 1.58 at 1.170 keV ✓. |f|² at 2.07 keV: 9.8e-8 (normal), 0.251 (short), 2.0e-9 (long) ✓.
- WE 16.4: J₁₁ = −196.6, J₁₂ = −15.6 meV (we16_4.log; the Ewald test at Q = 0.01 Å⁻¹ gives 15.73, an analytic Q-dependence, immaterial).
  E_∓ = 3.1 − 0.1966 ∓ 0.0156 = 2.888/2.919 eV ✓; the ∥b symmetric combination is lower for J₁₂ < 0 ✓ (my 2×2 with R_b = diag(−1,1,−1)).
  |d_−|² 1.334, |d_+|² 0.359, sum 1.693 = 2(0.92)² ✓. f sums 0.429 vs 0.459, ratio 0.934 ✓. q = 3 keV ∥M1: 0.0013 @3.086, 0.1858 @3.144,
  0.0599 + 0.1272 = 0.1871, separation 57.8 meV ✓. Band 2.827–3.185 eV ✓.
- Limit Check 16.4a / l.85 vs limit16_4a.log: 6.3 % flat ✓; La–Bb 122/180 meV, ΔE 1.39 eV ✓; light 1.29–1.35 above 2 MeV ✓; heavy max 1.272 ✓;
  no macroscopic term ×8.8 at 1.085 MeV ("ninefold at 1.1 MeV") ✓; ε_mac−1 0.83 (1.17 keV), 0.51 (2 keV) ✓; shift 0.27 eV ✓; unitarity 1.00000 ✓.
- CT: tan2θ = 2t/ΔE, sin²θ transfer, θ² ≈ t²/ΔE²: t = 0.1 eV, ΔE 0.8–1.1 eV → 0.8–1.6 % ("about one percent") ✓.
- Anisotropy and modulation vs fig16_4.log: 8.02e4/2.29e4 at 10 MeV ✓; Si IP 1.36e5 matches s10-2 l.38 (also unscreened) ✓; max/min 92.2/68.8 (1 MeV),
  2.26/5.27 (1.5), 1.20/1.39 (10), 1.17/1.30→1.29 (≥100) ✓; L_a share 1.000/0.676/0.192 ✓; A_day bounds 0.979 (light 0.971), 0.387/0.681,
  0.092/0.165, 0.077/0.127 ✓ (rounding "0.98" also covers light 0.97: acceptable). The R_max at b holds only up to 1.5 MeV (heavy), as stated.
  Evenness in v̂_E: holds for any crystal (real transition densities); the "centrosymmetric" clause is harmless but not the reason.

## CHECKED: s16-5 (dopants)
- 45.59 − 11.48 = 34.11 meV; T₂, E at 11.70/13.01 meV; 2×45.59 meV/v_max² = 12.98 keV ✓. Vinh: T1 = 205 ± 18 ps, 1/T1 = 0.026 cm⁻¹, narrowest 0.034 cm⁻¹ ✓;
  0.034 cm⁻¹ = 4.22 µeV, ħ/205 ps = 3.21 µeV ✓. 1e15/(2e23) = 5e-9 ✓.
- eq:16.5-SD screening once; eq:16.5-ff structure; intervalley q ≃ k_j′ − k_j − G ✓. Envelope transform [1 + (r⊥²p⊥² + r∥²p∥²)/4]⁻² is the transform of |F|² ✓;
  1/r⊥ = 197.3 eV nm / 2.43 nm = 81 eV ✓.
- **eq:16.5-floc**: ⟨s|e^{i(q+G)·r}|s′⟩ → 𝒰_jj(−G)×envelope(q) ⇒ ñ = (ε⁻¹)₀₀[1 + ε_host Σ_{G≠0}(ε⁻¹)_{G0}𝒰_jj(−G)] n ✓ (see G4 for "close to one").
- **eq:16.5-gos** (chk1.py): with the book's prefactor and bracket, the Bethe sum Σ(E_f−E₀)|M|² = q²/2 and completeness
  |F_el|² + Σ_n + ∫ = 1 hold to 1e-5 at q̃ = 0.3, 1, 2, 4 (discrete part from the closed hydrogen GOS); continuum f(q→0) = 0.4350 ✓.
  L = (e²/2q²)S at q→0 equals 4π²αn|z|²/ε², consistent with eq:16.5-abs ✓. Du Eq. (12) v1 prefactor 2¹⁰π²αm*n_Da*⁴/(3|ε|²) matches ✓.
- **Du misprint**: v1 Eq. (12) prints (3q̃ + k̃² + 1) ✓ (verified in the source). Impact with Du's parameters, my own integral (chk3.py,
  SHM 238/250.5/544 km/s): heavy 1.469 / 0.909 / 0.593 / 0.562 at 0.02/0.1/1/10 MeV = book's 1.47 … 0.56 ✓. This is **the same misprint**
  as the campaign's (SOTA: CW4 "3q̃ → 3q̃², impact 1.47–0.56 (heavy)"; WP7-B1-v2 CONFIRMED) ✓. The "Lyman lines" claim (refuted in SOTA) is
  correctly absent. Absorption is unaffected (q = 0) ✓.
- **(E_eff/E₀)² = 4.84 f-sum claim** (chk2.py): 1/(2m*a*²) = 85.73 meV ✓; Du continuum at q = 0 carries 0.3003 of the f-sum of mass m* (consistent
  hydrogenic: 0.4350) ✓; ×4.84/0.3 = 4.846 (m_e units) > 3.854 = (2/0.1905 + 1/0.9163)/3 ✓. Ratios to the central-cell model 1.13/1.31/1.48 at
  50/60/70 meV ✓ (fig16_5.log). Du's description of the factor (local/average field, matched to photoabsorption, Sect. VII.2) is quoted faithfully ✓.
- Valley lines (chk1.py, r⊥ = 24.3, r∥ = 14.0 Å): Σ_E|⟨E|e^{iq·r}|A₁⟩|² = (2/9)(g∥ − g⊥)² for q∥[100] (1/6 + 1/18), derived independently ✓;
  max 0.0222 at 150 eV ✓; [110] 0.00319 ✓; [111] 0 ✓; T₂ cancels identically ✓. Intervalley |q|: 0.685, 3.602, 3.881 (opposite), 2.334, 2.744
  (perpendicular) keV ✓; masses 29.3 keV (150 eV, 13.01 meV), 130 keV, 441 keV ✓.
- eq:16.5-abs = first order of Im(−1/ε) in ε^D ✓. Cubic averages |Z|²/3 (p₀) and 2|X|²/3 (p±) ✓. f = 2m_eω|r|²: 0.122 / 0.385 (2p₀), 0.517 / 1.734 (2p±) ✓;
  line shares of the TRK sum 0.253 / 0.486 ✓; 1/ε² = 1/130 ✓; EMT 1s 31.32 meV, central cell ranges 3.2/6.3 Å within 2 % ✓.
- WE 16.5: ∫ε₂ = 7.73e-6 eV ✓; peak 1.168 ✓; L = 8.99e-3 ✓ (8.986e-3); effective medium 0.9949 → 8.94e-3 ✓; mv²/2 = 0.017 µeV ✓; R = 5.5e31ζ²
  (6.173e33 × L; my unit conversion agrees) ✓; ζ = 2.33e-16 ✓; continuum L 2.06e-5, ζ 4.85e-15 ("4.9e-15") ✓; ratio 21 ✓; EMT ζ 1.34e-16 ✓; Γ/m 1.24e-4 ✓.
- **Effective-medium validity** (limit16_5a.log, sympy): Im(−1/ε_eff)/(ε₂/ε²) = 1/|1+2y|² exactly; expansion 1 − 4Re y + 4[3(Re y)² − (Im y)²] ✓; line centre
  1/[1 + (4/9)(ε₂/ε)²] ✓. Densities 8.8e17 (CC) and 2.6e17 (EMT) at 60 meV, gray < 2.63e17 ✓; line-centre failure 4.83e15 (CC, "4.8e15") ✓,
  where ε₂/ε = 0.495 ✓. (EMT envelope: 1.5e15; the box quotes the CC value, which is fine, but say "with the central cell".)
- Impurity band: P(neighbour < 4.86 nm) 4.8e-4 / 0.382 / 0.579 ✓; α_pol/ε = 4π×3.81e-20 and 4π×1.11e-20 cm³ ✓; CM divergence 6.27e18 / 2.1e19 ✓;
  static enhancement 1.15–1.57 (1e18), 1.28–2.21 (1.8e18) ✓. Du: n_c ≳ 3e18 (Sect. II), 1e18 projections, 1.8e18 optical comparison,
  T ≈ 5 K, BIB layer (VII.1), phonons below ~10 meV ballistic and line broadening (VII.6) ✓.

## CHECKED: s16-6 (color centres and broken bonds)
- E_R^max(F) at 0.5 GeV: 187.7 eV ✓; masses 0.1864 (27 eV), 0.113 (10), 0.2546 (50), Li→F 0.1288, Li own 0.1140 GeV ✓; 4M_LiM_F/(ΣM)² = 0.7878 with ⁷Li
  (natural Li gives 0.784: say "⁷Li"). Arrows 31.0/188/711 eV ✓. Guerrero-Perez: gap 14.2 eV, F band ~5.1 eV, computed 4.85/4.90 eV ✓.
- eq:16.6-ccrate: (M_κ/M_cell)ρσ/(2mμ²) = (1/M_cell)(ρ/m)(M_κσ/2μ²) ✓ (dims E⁻¹ per E_R) ✓; σ_ω² = E_R⟨ω⟩ ⇔ ⟨p_z²⟩ = M⟨ω⟩/2 (KE ω/4 per dof) ✓;
  initial KE 3⟨ω⟩/4 ✓; σ→0 limit v_min → q/2μ ✓. Budnik Eq. (1), (2) with n_θ = n_φ = 4, a = 0.4 (Table I is MgO/LiH: a borrowed value for LiF,
  as the caption says "angular model"), (5), (6) Δp ~ αm_e, (7), (10) ✓. Note that Budnik's Table I is not a LiF table.
- Doppler width 0.951/1.444 eV (3.5/5.4 %) ✓; zero-point 17.2/26.1 keV = 4.6/7.0 αm_e ✓; q_min = 977.6 keV; ratios 0.018/0.027 ✓; 1.36 E_d ↔ 0.218 GeV ✓;
  < 2 % above 1.96 E_d ✓; −1.4 % in mass at 1.1 E_d ✓; directional to 10 % at 4.82 E_d ↔ 0.414 GeV ✓; (1 − 0.4)² = 0.36 ✓.
- Lindhard (Agnese Eq. (3) form verified): k 0.1320, ϵ 0.0683, g 2.214, y_L 0.226, T_d 774, KP 14.3 / 18.5, 7.2, 16 pairs ✓; 0.5 GeV: T_d 155, 2.86, 2.33 ✓;
  0.3 GeV: 69 eV, T_d 58.5 → 1.08, 0.75 pairs ✓; 0.2 GeV: T_d 26.7 < 27 ✓. Cogswell E_d = 27 eV, 80 eV half-efficiency (Table I), KP (Sect. II),
  1e-12–1e-10 ✓. Griffin LiF optical 33.5–77.2 meV (Table I; a crystal band, not F-site specific; labelled as a model range) ✓.
- **Bond-breaking convolution eq:16.6-conv**: R₁ = R_CM + (μ₁₂/M₁)r ✓; with neighbour forces on R_CM only, [H_CM, H_int] = 0, the Heisenberg operators
  commute at all times and the ground state factorizes ⇒ the correlation factorizes ✓; the product in t gives ∫dω′/2π S_CM S_int with the
  2πδ normalization ✓; q₁₂ = (μ₁₂/M₁)q ✓. Free limit q²/2M_mol + μ₁₂q²/2M₁² = q²/2M₁ ✓ (sympy-trivial).
- eq:16.6-qmin = Essig Eq. (3.3) ✓: H₂ 133.55 keV, 25.89 MeV ✓; ω_vib 0.5457 eV, ratio 8.70 ✓. eq:16.6-diss (impulse, p → p + q₁₂) ✓.
- **ω_vib/4 impulse vs improved Born**: Essig's plane-wave final state has q̃² = 2μ₁₂(E_int + ΔE_B) (Eq. (3.17)), so dissociation ⇔ |q₁₂+p₁₂|²/2μ₁₂ > E_bond ✓;
  the difference from eq:16.6-diss is p₁₂²/2μ₁₂, with mean ⟨p_r²⟩/2μ = ω/4 = 0.1364 eV for the J = 0 Gaussian of Eq. (3.12) ✓ (a random variable; "the initial kinetic
  energy" is correctly worded). rms projection (μω/6)^{1/2} = 6.53 keV = 1.75 αm_e ✓; Eq. (3.8) → 0.90 ✓.
- Limit Check 16.6a (b): 42.9 MeV at (q_max/q_min)² = 2.65 ✓; 22.80 MeV (0.8385), 20.33 MeV (0.7476) vs 27.19 MeV ✓ (see W2 for the comparison sentence).
- NV: 2×1.945/v_max² = 0.554 MeV, q = m v_max = 1.47 keV ✓; Budnik photon budget 1e21×1e-17 = 1e4 s⁻¹, ×1e3×0.1×0.5 = 5e5 ✓; 1 in 1e5, 1e-9, 1000 °C ✓.
  Araujo: 450/525/650 nm, ×50 γ/n, months, 350 °C, 1200 µm⁻¹ ✓.

## Campaign cross-checks
- CORRECTIONS l.641 (first-order borrowing): consistent with the text and verified. SOTA "Frenkel: incoherent sum exact in bins wider than the Davydov
  splitting" (WP7-B1) is superseded by the book's stronger condition (whole manifold, no outside coupling, constant η and ε). SOTA should cite 16.4.
- SOTA l.613 Du misprint impact 1.47–0.56 (heavy) [E]: now independently reproduced, so it can be upgraded from [E] to [CALC] (chk3.py, gos16_5.log).
- DC-RESULTS / returns R18: no row bears on 16.4–16.6. DC-67's withdrawn P_casc reader (LiF P(N=1) error) is not used in 16.6 ✓; DC-51
  (impurity band) has no result yet, and the text correctly calls it open. No superseded value is used.

## Editor-note items for these sections (verdicts)
16.4: first order ✓ (CHECKED); anisotropy ×92 (note says ×90) ✓; A_day 0.98 and 0.08–0.13 ✓; measured splitting not found (G7); a Limit Check against
m_χ is a reasonable choice, but see G1.
16.5: 4.84 f-sum violation ✓; Eq. (12) misprint, the same one as the campaign's, impact ✓; effective-medium densities ✓; ×3.2–3.4 needs the 2p qualifier (G2);
1s(E) directional at 100–150 eV, zero along [111] ✓ (G3 caveat); T₂ 0.685–3.88 keV ✓; Mott 3e18 is quoted from Du correctly.
16.6: arXiv numbering of 1608.02940 verified ((3.3), (3.8), (3.11), (3.12), (3.17)); E_d 27 eV a TRIM input ✓; ⟨ω⟩_CM = 10 meV negligible
(1.6e-6 ≪ 2.65e-3) ✓; convolution ✓; ω_vib/4 ✓; 4.0 MeV is the gap, not the exciton threshold (W3).
