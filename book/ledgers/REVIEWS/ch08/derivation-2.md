# Ch8 part 2: derivation check (s8-5 … s8-8, D-28; ch08.tex; PRIORITY items of 8.1/8.3/8.4)
Reviewer: derivation verifier (long-form-writing SKILL §5). Date 2026-11-02. Tex not edited.
Tools: sympy/numpy/scipy scripts (scratchpad, not kept); cached npz of we8_10; independent re-implementation of WE 8-sectors.
No QE or EPM runs. Sources fetched with lit.py into sources/review-ch08/ (PDFs deleted afterwards).
Format: location → verdict, then correction. Known editor-note items are marked [known].

## A. PRIORITY items

- **8.1, sign flips of O_i against Fitzpatrick/Anand → CHECKED.** Both sources define q = p′ − p (1203.3542 Eq. (11);
  1308.6288 text before Eq. (12)), and the book uses q = p − p′. FKLM v⊥ = v + q_F/2μ = v − q_book/2μ, which is the book's
  Eq. (8.1-vperp) for a target at rest, so v⊥ is the same vector in both. The operators odd in q are exactly
  O3, O5, O9, O10, O11, O13, O14. O6 and O15 are quadratic in q, and O1, O2, O4, O7, O8, O12 contain no q. The table
  operators have the same form as FKLM Eqs. (19)–(24) and Anand Eq. (13) (O13–O15). The flip list is correct.
- **8.3, mixed third moment, Eqs. (8.3-M3), (8.3-M3lim), (8.3-M3sph) → CHECKED.** Re-derived independently:
  [[e^{-iq·r},H],[H,[H,e^{iq·X}]]] = −(1/mM) e^{-iq·(r−X)} (q·∇)² w(r−X). sympy confirms the 1D form, and the
  Jacobi/stationarity step is exact. Summing over electrons and nuclei of species κ and dividing by V gives Eq. (8.3-M3)
  with the moment convention of Eq. (8.3-moments). Contact term: (q·∇)²(1/y) = −(4π/3)q²δ + q²(3c²−1)/y³ (sympy).
  With ∇²w = Z e² δ this gives Z e² q² 𝓃^(κ)/3. Uniform term: the angular integral of e^{-iq·y}(3c²−1) is −8π j₂(qy)
  (sympy), and ∫₀^∞ j₂(x)/x dx = 1/3 (numerical, 0.33333), which gives 2𝓃_e/3. The bracket of Eq. (8.3-M3sph) follows with
  the factor 2 as printed, and its large-q limit is 𝓃^(κ). Ward check: m_e𝓜³_ee + Σ M_κ𝓜³_eκ = (e²q²/3m_e)[2𝓃_e² − 2𝓃_eΣZ𝓃_κ]
  = 0 by neutrality, as stated. Puff/jellium: the e–e term (2/3)e²q²𝓃² plus the background term (1/3) gives 𝓃q²ω_p²/m ✓.
  Spring model: (q·∇)²(Ky²/2) = Kq², so the result is −Kq²/(m M V) ✓.
  WE 8-third numbers: (Z e²𝓃^(κ)/3m_e)^{1/2} = 8.754 keV, and with ×1.006 it is 8.781 keV ✓. Per electron 2.340 keV ✓.
  1765 a₀⁻³ = 1.191e28 cm⁻³ ✓. 𝓃_e = 6.99e23 ✓. 2𝓃_e/𝓃^(κ) = 1.17e-4 ✓. q = 2.682 a₀⁻¹ ✓. 1/q = 0.197 Å ✓.
  14/a₀ = 52.2 keV ✓. (q²/2m)^{1/2} → 97.8 eV ✓. (2q²K̄/m)^{1/2} = 468.8 eV with K̄ = 288.854 Ha/14 ✓. (m_e/M)² = 3.8e-10 ✓.
  The contact density value itself (HF, Gaussian basis) was not recomputed, because no all-electron code was run. → GAP
  (low): cache the atomic calculation's output next to the figscripts.
- **8.4, exactness theorem, Eq. (8.4-exact) → CHECKED.** Sufficiency: v_C R_ZZ = ε⁻¹ − 1 with the FDT and v_C = e²/q²
  gives S_ZZ = (2q²/e²)L/(1−e^{−βω}). Necessity, large q: incoherent recoil peaks with weights c_s²𝓃_s, separated by
  mass. Necessity, small q at the LA phonon: the weight is ∝ q²(Σc_s𝓃_s)², while S_ZZ is O(q⁴), so Σc_s𝓃_s = 0 is
  needed. With |c_e| = |λ| and |c_κ| = |λ|Z_κ, Σ(σ_e+σ_κ)Z_κ𝓃_κ = 0 forces σ_κ = −σ_e for every κ. The argument is
  sound under the three stated conditions (distinct masses per Z, a sharp LA phonon with nonzero weight, F_N = 1).
  Note: isotopes of one Z are separated by mass too, and each must then carry |λ|Z, which is consistent.
- **8.7, pair-by-pair in/out equality for PT-invariant targets → CHECKED, with a GAP in the hypotheses.**
  Eq. (8.7-factor) is re-derived, and so are the retarded column (1+fR)_{G0} and the advanced weight
  δ + Σf_{GG′}R*_{0G′}. With PT-invariant many-body states the amplitudes ⟨f|n_e(q+G)|i⟩ are real, so R_{GG′} = R_{G′G}
  (complex symmetric). The advanced weight equals the conjugate of the retarded weight **only if f is real**
  (f_{GG′} = f*_{GG′}). Hermiticity alone is not enough. Toy test (6 G, 40 pairs, random): with real amplitudes and real
  symmetric f, max|R−Rᵀ| = 1e-15 and the pair weights agree to 6e-14. With real amplitudes and a complex Hermitian f,
  Σ|Δw|/Σw = 0.43. With complex amplitudes it is 0.71.
  Corrections: (i) state that f must be PT-invariant, i.e. real in a frame centered on an inversion point. RPA (v_C
  diagonal) and ALDA (real f_xc(r), even about that point) satisfy this. (ii) State that R_{GG′} = R_{G′G} holds with the
  origin at an inversion center. Pair moduli do not depend on the frame, but the symmetry of R does. The WE's "as the PT
  argument requires" is fine, because the CB model sits on the bond-center origin (script record: max|R−Rᵀ| ~ 1e-16).
  The D-28 "Real amplitudes under PT" argument, with (PT)² = (−1)^N, the invariant-basis construction and the reality
  of ⟨a|O|b⟩, → CHECKED.

## B. Sect. 8.5 (s8-5.tex)
- κ_BO = (m_e/26.06 GeV)^{1/4} = 0.06654 → 0.0665 ✓. κ³ = 2.95e-4 ✓. 12κ² = 0.053 ≈ ω_opt/E_g = 0.055 ✓.
- θ_ep: 0.25²/2.5² = 0.010 and 0.25²/2² = 0.0156 ✓. θ = 1 at δ_off = 0.25 eV ✓. Acoustic vertex ×1/10 gives θ ×1/100 ✓.
- η² = 2.40e-3 ✓. T(10 mK) = 0.8617 µeV ✓. T/ω_TA = 4.64e-5 ✓. ω_TA/T = 21550 ✓. T/E_g = 7.37e-7 ✓.
  (T/ω_D)³ = 3.7e-15 ("4e-15") ✓.
- Recoil (natural Si, M = 26.16 GeV): E_R(10 keV) = 1.911 meV ✓. x_R = 0.0467 ✓. x_R = 1 at 46.3 keV ✓.
  2W = 0.0629 at 10 keV ✓. 2W = 1 at 39.9 keV ✓. x_R = 9 at 138.8 keV, E_R = 0.368 eV ✓. Einstein 9×60 meV = 0.54 eV ✓.
  0.37/0.54 = 0.68 ("down by a third") ✓. ⟨ω⟩⟨ω⁻¹⟩ = 40.9/30.4 = 1.345 ✓.
- Eq. (8.5-cumulants): compound-Poisson cumulants c_k = 2W∫ω^kP₁. With P₁ ∝ g/ω and 2W = E_R⟨ω⁻¹⟩, c_k = E_R⟨ω^{k−1}⟩ ✓.
  Eq. (8.5-width), c₂^{1/2}/c₁ = x_R^{−1/2} ✓ (dimensionless). The width falls below E_R/3 for x_R ≥ 9 ✓.
- Suddenness: 1/E_g = 0.5626 fs ✓. E_gτ = 7.1e-6 ✓. [1−0.055²]⁻² = 1.0061 ✓.
- Multipoles: q₀ = 1.890 Å⁻¹ ✓. m_e v_N = 100.2 eV, so ξ = 0.051 ✓. Absorption gives ξ = 5.1e-6 ✓.
  |f_{1s→2p}|² = (128√2/243)² q²a₀² = 0.5549 q²a₀² ✓.
- Rung paragraph: 11.45 → 10.22 is −10.7% (stated "11 percent") ✓. TDDFT restores 0.59/1.23 = 48% ✓.
  (11.9/10.22)² = 1.36, i.e. "up to a third" in 1/ε² ✓.
- Label rules (n_g, n_A, n_T, n_B counting) agree with the NOTATION editor ruling (line 1491) ✓.
- WE 8-label: (ω_ph/E_g)² = 3.0e-3 ✓. The other numbers are cross-references (14.7 meV, e^{−21550}) and agree with 4.9 and 8.5 ✓.

## C. Sect. 8.6 (s8-6.tex) and D-28
- Opening: v_N = 5.10 MeV/26.06 GeV = 1.957e-4 ✓ (q_max implies v_max ≈ 794 km/s, consistent). (v_N/α)² = 7.2e-4 ✓.
  At 50 keV, 2W = 1.572, so P₀ = 0.208 ("21%") ✓ and P(≥2) = 0.466 ("47%") ✓.
- **"Their small parameter is (m_e/M)^{1/2} = κ_BO², the ratio of a nuclear to an electronic velocity at equal momentum"
  → WRONG.** At equal momentum the velocity ratio is m_e/M = κ⁴. Correction: "…at equal kinetic energy". This also
  matches the D-28 scaling (nuclear kinetic term −κ⁴∇²/2, momenta in units of (M/m_e)^{1/2}).
- Eq. (8.6-leak) and the D-28 construction against PST: Thm. 2.1 (ε = (m/M)^{1/2}, almost-invariant Π, O(ε^∞)) ✓.
  Sect. 4.5 energy cutoff ✓. Eq. (38) is the BO-type Hamiltonian ✓. The unitary's symbol "below Eq. (39)",
  |ψ⟩ + iεR₀p·∇ψ, has the same sign as Eq. (D.28-tilt) ✓. Eq. (40) last term −ε²⟨p·∇ψ,R₀p·∇ψ⟩ = −Σ(p·d₀ⱼ)(dⱼ₀·p)/(M²ΔE) ✓.
  Born–Huang term (1/2M)Σ|d|² ✓. Spohn–Teufel Sect. 2 (regularity fails for point nuclei, their l. 313–314) ✓.
- **Eq. (8.6-decomp), remainder "+O(κ^{2(n+1)})" → GAP (dimensions).** S_ab has units eV², and the remainder as
  printed is dimensionless. Eq. (D.28-lemma) gives the cross terms relative to a binned value as
  O(𝔥_off/Δω_bin) ≤ O(κ^{2(n+1)} α²m_e/Δω_bin). Write it so. Note that the prefactor α²m_e/Δω_bin ≈ 2.7e4 for 1 meV bins
  at n = 0: for phonon-scale bins the statement needs n ≥ 2. The text says "bins wider than the leak", which is right, but
  the equation hides this.
- Eq. (D.28-lemma): the Fourier representation of f_Δ, Duhamel (sign checked by differentiation), the bound
  |t|𝔥‖ψ‖, and 𝔠_b = (1/2π)∫|y||ŵ| ✓. Gaussian: ∫|y|e^{−y²/2} = 2, so 𝔠_b = 1/π (sympy) ✓, matching Eq. (8.6-bin).
  Rectangular bin divergence ✓.
- Eq. (D.28-tilt) and Eq. (8.6-boost)/(D.28-boost): the integration by parts and the cancellation of ∇Ψ⁰ terms are redone ✓.
  Remark: the step "using d₀ⱼ = −dⱼ₀" holds for real states only. In general d₀ⱼ = −dⱼ₀*, and the complex conjugate in
  Ψ′₀* restores the same result, so the formula is general (optional wording fix).
  Consistency: −i q·d/(MΔE) = sudden amplitude v·d/(iΔE) with v = q/M, and for an atom it equals −i m_e v·r_{j0}
  (electrons kicked opposite), as in Eq. (8.3-boostward) ✓.
- Eq. (8.6-PMig) ✓. Electronic energy Σ_j P_jΔE_j = q·δM·q/2M² with d = F/(E₀−E_j) ✓.
  Eq. (D.28-dM)/(8.6-fsum-k): kinetic ½p(M+δM)⁻¹p ✓. Atom: F_{j0} = −m_eΔE²r_{j0}, so δM_xx = 2m_e²ΣΔE|x|² = m_eΣf = N_e m_e
  (TRK) ✓. The sum of the ad and 0+ parts equals 𝓃q²/M to first order ✓. "Summed over ±q is twice the one-sided" ✓.
- Eq. (8.6-fsum-e): [F†,[p²/2M,F]] = |∇F|²/M re-derived ✓. Rigid clouds give q²Σ𝓃|f|²/M ✓. Ratio Z m_e/M = 2.735e-4
  (natural M) ✓. Eq. (8.6-fsum-ek): (∇ρ̄)†·iq e^{iqX} = q²f* ✓ (sign positive). Mirror rule from Eq. (4.3-species) ✓.
- δM/M = 14 m_e/M ≈ 2.7e-4 ✓ [known: atomic estimate, labeled; move first uses of δM_κ, P_Mig to 8.6].
- Off-shell window paragraph and D-28 "Labels inside the window": the convergent Lippmann–Schwinger series and the
  admixture norm ≤ θ_ep ✓.
- Eq. (8.6-amp), Eq. (8.6-dyson), Eq. (D.28-delta): G_m ≈ z/(x + i zΓ/2) gives |G|² weight 2πz/Γ (sympy) ✓.
  The cross term gives −2πc_ν δ. Im Υ = −½ΣΓ_μA_μ, which gives +Γ_μc_μ. Collected: (Γ_ν/Γ)[z|ρ̃|² + Γ(c̄ − c_ν)] ✓.
  The dimensions of S⁺ match S⁰ (|ρ|²/energy) ✓.
- **Eq. (8.6-fano) and the sentence "The Fano coefficients c^F_ν sum to zero with the weights Γ^(ν)" → WRONG.**
  Σ_νΓ^(ν)c^F_ν = Γ^tot²c̄/|ρ|² ≠ 0 in general. What vanishes is Σ_νΓ^(ν)(c^F_ν − c̄^F). Also, the main text normalizes with
  Γ^tot (which includes impact ionization), while ν runs over phonon branches. Then
  Σ_ν(Γ^(ν)/Γ^tot)(c̄ − c_ν) = −c̄(1 − Σ_νΓ^(ν)/Γ^tot) ≠ 0, so "change no total and no number of zero-phonon events"
  fails. Correction: let ν run over **all** decay channels of the pair, including non-phonon ones, each with its own
  off-shell amplitude A_ν. The vertex correction Υ_m then contains them too, as D-28's derivation requires. Then write
  "the Fano terms c̄^F − c^F_ν average to zero with the weights Γ^(ν)". D-28 is consistent for the phonon-only case
  (Γ_m = Σ_νΓ^(ν)), but its sentence "If the pair also decays by other channels … becomes Eq. (8.6-fano)" needs the same
  all-channels clause.
- Eq. (8.6-zsum): Re Σ = (2π)⁻¹PV∫Γ/(ω−ω′), so ∂ReΣ = −(2π)⁻¹fp∫Γ/(ω′−ω)², and z = 1 + ∂ReΣ + O(g⁴) ✓.
  Level check: z − 1 = 0.0064 = −(finite part) with fp∫_{−W/2}^{W/2}dy/y² = −4/W, so −2Γ/(πE_w) ✓ (matches s4-7).
- Eq. (8.6-ambiguity): 5/(2π) + 1/π = 1.114 ("1.1") ✓. The D-28 bound |1 − z⁻¹| ≤ (5/2π)Γ̂/δ_F (outside 2, inside 2,
  curvature 1) ✓. Lorentzian tail 2∫(Γ/2π)/x² = Γ/(πx_w) (sympy) ✓. The z → z² change is first order ✓.
- Eq. (8.6-bin) and D-28 "Gapless targets": 𝔥² = ΓΔE_c/2π from the golden rule ✓. The Fan–Migdal zeroth moment
  (n+1−f) + (n+f) ≤ 2n+1 ✓. 2Δ_BCS(Al) = 0.36 meV ✓.
- Decomposition keyresult, partition, and sector positivity under commuting projectors ✓.
- Table 8-sectors citations: griffin2018 Eqs. (19)–(23) (Fröhlich element with Z*, ε∞, rate (23)) ✓ [known item
  verified]. essig2016 Eq. (3.13) ✓. campbelldeem2020 Eqs. (5)–(8) ✓. ibe2018 Eqs. (55)–(58) (q_e = m_e v_F) ✓.
  knapen2021migdal Eqs. (3), (6) ✓. **knapen2021dark Eq. (6) → WRONG (precision)**: Eq. (6) is the S–ELF relation, and
  the loss-function rate is Eq. (13). Cite "Eqs. (6) and (13)".
- WE 8-sectors, re-implemented independently (exact diagonalization, N = 90 and 160, BO product states from a DVR) → all
  CHECKED. 40 states reached ✓. Min overlap 0.9961 ✓. σ_x weights 1.253e-3 / 0.15205 / 0.8467 ✓. Ad line at 63.39 meV ✓.
  ZPL at 1.04625 eV ✓. Surfaces 63.39 / 65.52 meV ✓. First moment 1.169148 eV ✓. Ad share 8.322e-5 eV, fraction 7.12e-5 ✓.
  (2g_n/Δ)² = 1.169e-3 ✓. 4g_n²ω₀/Δ³ = 6.40e-5 ✓, and it equals δM/(M/2) for the model (derived) ✓.
  P_Mig = 3.939e-6 (0.382 + 3.557) ✓. Boost estimate 3.508e-6 ✓. S_HRω₀/Δ = 0.110 ✓. Electronic energy 0.400 + 4.322
  = 4.72 µeV ✓. Estimate 0.253 + 4.10 µeV ✓. Interference ad = (2.172 − 13.219i)e-4 eV, electronic sectors exactly
  opposite ✓. ℓ₀ = 0.0483 Å ✓. q = 41.1 keV ✓. E_R = ω₀ ✓.
- Dirac width ∝ α̃²ω: argued from "the only scale is ω", which is dimensional reasoning ✓ [known; already worded acceptably].

## D. Sect. 8.7 (s8-7.tex)
- Eq. (8.7-IP): (2π/V)×2 spins = 4π/V ✓. The bubble anti-Hermitian part i[1/(x+i0) − 1/(x−i0)] = 2πδ, which gives (4π/V)Σρ*ρδ ✓.
  S = i(R − R†) at T = 0, ω > 0 from Eq. (4.2-fdt) ✓.
- Eq. (8.7-factor) and Eq. (8.7-screened): algebra ✓. Element 00 closes into |Σ_G ε̃⁻¹_{G0}ρ_G|² iff f is Hermitian ✓.
  S = (q²/2πα)L ✓.
- Second ("advanced") distribution: identity (1+Rf)(R⁰−R⁰†)(1+fR†) = R − R† ✓. Sakurai Lippmann–Schwinger form ✓.
  "Agree when R is Hermitian" ✓.
- PT paragraph: see PRIORITY (GAP: f real; origin at the inversion center).
- Continuity: ⟨f|q̂·j|i⟩ = (ω/q)⟨f|n|i⟩ with q·j(q) = [H, n(q)] (re-derived) ✓. The step model 1 + ⌊(ω−E_g)/ε_eh⌋ ✓.
- WE 8-pairs, geometry: q₀/(2π/a) = 1.6331 ✓. |q+G| = 0.838 keV ✓. **51** vectors with |q+G|² ≤ 12(2π/a)² (counted) ✓.
  Free gas m_e²ω/πq₀ = 2.23e8 eV² ✓, valid since ω = 10 < qv_F − q²/2m = 12.4 eV ✓.
  |ε⁻¹₀₀|² = 0.329 ✓. "Further 13 percent": 1 − 1/1.143 = 12.5% ✓. 4.9/17 = 0.29 (script 0.288) ✓.
- **WE 8-pairs numbers → GAP (not recomputed).** No cached output exists, and the ~6 min EPM run was not done under the
  compute policy. Every quoted number agrees with the convergence record in the we8_pairs.py header (NK = 24, rounded
  as NK = 20/24 agree), but that is a transcription check, not a recomputation. Cache an npz/log as we8_10 does.
  "IP weights within three percentage points" and "other three bands about a third each" are not in the record.
- **WE 8-pairs photon seed → WRONG/GAP (high impact).** ε_e + ε_h must equal ω − E_g = 9.18 eV for every pair.
  DM (4.84 + 4.42 = 9.26) and the transverse current (5.41 + 3.85 = 9.26) nearly do, but the photon gives
  5.43 + 3.30 = **8.73 eV**, 0.45 eV short. The cause is consistent with the 0.10 eV Lorentzian tails weighted by the
  optical 1/Δ² factor, which pull in low-energy vertical pairs. This biases the "a volt below" hole comparison, which is
  repeated in 8.7-handoff ("about a volt more energetic"), the closing paragraph of 8.7-pairs and the Summary
  (4.4 vs 3.3 eV). Correction: recompute the optical (and, for consistency, all) seeds with a kernel that keeps
  ε_e + ε_h = ω − E_g (narrow Gaussian, or renormalize the Lorentzian on a window of a few η). Otherwise state the
  broadening bias and quote the difference only to the accuracy that survives.
- GaAs 15% (record 0.156) ✓. 0.01 eV mean difference ✓ [known: labeled EPM model, gap 0.82 eV].
- Ramanathan & Kurinsky cites: Sect. II A ("equal split … minimizes overall impact ionization") ✓. Eqs. (5)–(7) ✓.
  Wording: their split distribution is a phenomenological fit to photon-ionization yields → "fitted to photon
  absorption" rather than "computed for photon absorption".

## E. Sect. 8.8 (s8-8.tex)
- Eq. (8.8-M): first order (1+δ)^ϑ ≈ 1 + ϑ ln(1+δ) ✓. 1 + ϑδ < 0 at ϑ = −2 for δ = 0.5 ✓.
- **Eq. (8.8-geodesic), "positive semidefinite for every real ϑ" → GAP.** For ϑ < 0 a negative power of
  S^{−1/2}S⁺S^{−1/2} exists only if S⁺ is positive *definite* on supp S. The stated condition (S⁺ has no weight outside
  supp S) suffices only for ϑ ≥ 0. Require supp S⁺ = supp S, or restrict to ϑ ≥ 0. It reduces to Eq. (8.8-M) for one row ✓.
  Congruence preserves PSD ✓.
- Table 8-nuisances: 1 − e^{−0.063} = 0.0611 ✓. η²ω_opt = 0.154 meV ✓. ZPR −56.2 / −64.3 (8 meV) agrees with s6-3 ✓.
  Minor wording: "too large by 6.1 percent" is relative to the truncated value. Relative to the correct value it is
  e^{0.063} − 1 = 6.5%. Say "the correct rate is 6.1 percent lower".
- Eq. (8.8-fsum): the rungs IP/RPA/RPA+LF/ALDA conserve the first moment ✓ (npz: IP vs RPA 0.08%, RPA vs LF ≤ 2e-4).
- Eq. (8.8-tilt): gradient = moment mismatch, Hessian = Hankel moment matrix of the deformed spectrum (strictly convex),
  and λ = 0 at ϑ = 1 ✓.
- Eq. (8.8-like) and Eq. (8.8-cost): profile condition ϑ̂ = −kN ✓. t_p = 2u + k²u² ✓. u = w/k² ✓.
  N_nom = u e^{k²u} ✓. Ratio 2we^w/(k²t*) ✓. Values: 1.0105, 1.0794, 1.1909 → 1.0%, 8%, 19% ✓. t* = 4.605 ✓.
  (t*)^{−1/2} = 0.466 ✓. Envelope 1 + δ ✓. Minor: the series has no k⁴ term (sympy: 1 + k²t*/4 + O(k⁶)), so "O(k³)" is
  true but loose. cowan2011 Eq. (7) ✓.
- WE 8-rung, recomputed from we8_10_data_NK{16,20}.npz → CHECKED. At q₀: −0.059 (2 eV), −0.060 (3), 0.000 (4),
  −0.033 (5), −0.026 (7), −0.061 (10). Min −0.147 at 17.5 eV. Zero at 25.5 eV. +0.018 at 30 eV.
  At 2q₀: −0.438, −0.303, −0.223, −0.057 (NK16 −0.066). Zero 28.3–29 eV.
  Weighted means −0.059 / −0.092. Zeroth moments −2.06% / −3.01%. First moments ≤ 2e-4. (11.45/10.22)² = 1.255 ✓.
  −0.44/−0.09 ≈ 5 ✓. ½m v_max² = 3.56 eV per MeV ✓. 25.6/3.56 = 7.2 MeV ✓.
  Minor: δ_X touches zero at 4 eV (NK16 gives +0.003), so "only energies where δ_X < 0" should read "≤ 0" or "not > 0".
- Intro "22 to 44 percent between 2 and 10 eV at 7.5 keV" ✓. Summary numbers agree with 8.1–8.7 (A² = 29² = 841 ✓,
  0.0665, 2.73e-4 and 1765 a₀⁻³ ✓). The 4.8/4.4 vs 5.4/3.3 eV split inherits the photon-seed issue above.
- kahn2022searches cite (8.5): the Poisson/E_R content is Eqs. (90)–(91), and the width √(ω₀E_R) statement is in the
  text after Eq. (92). → Cite "Eqs. (90)–(92)". giustino2017 Sect. III A, text by Eq. (19) (harmonic + adiabatic) ✓.

## F. NOTATION drift (my files)
- **𝒬_{n,m} (8.6, sector projectors) and 𝒬_A (D-28) clash** with 𝒬 (10.9, boosted-DM momentum) and 𝒬(t) (C.20).
  Rename (e.g. 𝒫_{n,m}^{qp}, or reuse 𝒫_A with a superscript) and add a row.
- New symbols with no NOTATION row: δ_F (Dyson detuning), Υ_m (vertex correction), c^F_ν and c̄^F (Fano
  coefficients), 𝔥_off, Δω_bin, x_w, 𝔠_b, f_Δ, w_b, H_d and H_off, GF_m, ρ_m and ρ_{j0}, g_d and g_n (WE).
- δ_w: NOTATION first use is 13.6, but the symbol is now used in 8.6. Update the location.
- Known [editor notes]: δM_κ, P_Mig first uses → 8.6; ε̃⁻¹ row; P_casc → 8.7; 𝖫 clash with the 4.9 pair propagator;
  δ_k, ΔS_k, 𝔗_k⁺, δE_k, r_j; Γ typography. The files use \varGamma throughout, and no upright \Gamma rate was found ✓.
- Conventions: q (lost by DM), n_s(q) = Σe^{iq·r}, M^k with the ±q symmetrization, and S = −2ImR/(1−e^{−βω}) are used
  consistently across 8.5–8.8 and D-28. No factor-2 or 2π drift found beyond the items above.
