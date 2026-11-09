# Ch8 derivation review, part 1 (s8-1 to s8-4, App. D.24 to D.27)

Scope: tex/ch08/ch08.tex, s8-1.tex to s8-4.tex, tex/appD/D-24.tex to D-27.tex, against NOTATION.md and STYLE.md.
Method: sympy for the algebra (scratch scripts, not kept in the book), numpy for every quoted number. I also wrote an independent
PySCF ROHF run for the Si bracket of WE 8.4 (different basis from figscripts/ch08/we8_4.py, and a 3D Becke grid instead of the
script's radial-angular product). No QE was run. Sources were fetched with lit.py into sources/review-ch08/<arXiv id>/, and the
PDFs were deleted afterwards.
Verdicts: CHECKED (redone; agrees), WRONG (correction given), GAP (missing hypothesis or step).

## Summary
- New findings: 2 WRONG (both minor numeric or order-of-magnitude slips), 4 GAP or wording items. I found no sign, factor-2 or π error
  in any derivation.
- PRIORITY items: (i) the mixed third moment is CHECKED independently, including the Ward cancellation and the Si numbers;
  (ii) the exactness theorem's proof is CHECKED, but the statement has two GAPs (ω ≠ 0, and the acoustic-phonon hypothesis);
  (iii) the 8.7 pair-by-pair in/out equality is CHECKED algebraically (outside these files; derivation-2 owns the numbers);
  (iv) the Fitzpatrick/Anand sign flips are CHECKED against the sources.

## New findings
1. WRONG, s8-4 l.140 (third consequence). The ionic part of ε(1.5 eV) in GaAs: −(ε₀ − ε∞)ω_T²/ω² with ε₀ = ε∞ω_L²/ω_T² = 12.72 gives
   **−9.2×10⁻⁴**, not −1.0×10⁻³ (8.5×10⁻⁵ of ε∞, so "10⁻⁴ of ε∞" stands). Write "−0.9×10⁻³".
2. WRONG (minor), D-26 l.53 (spring check). For a free center of mass, a final state with only the COM recoiling has
   ω = q²/2M_tot and an O(1) cross amplitude ⟨e^{ic_e q·u_r}⟩⟨e^{−ic_κ q·u_r}⟩, which gives 2ω³/V = q⁶/(4M_tot³V).
   "The center-of-mass mode contributes at order q⁸" should read **q⁶**. It is still beyond q², so the check stands.
3. GAP/wording, s8-4 l.50 ("with the same weight") and l.119 ("the weight is unchanged"). From the displayed R_NN and S_NN, the
   δ-coefficient of S is πC/ω_L, against πC/ω_T for the proper response. Only the f-sum weight ∫ωS dω/2π = C/2 (the residue in ω²)
   is unchanged; the zeroth moment changes by ω_T/ω_L = 0.925. Say "the same f-sum weight".
4. GAP, s8-4 keyresult eq:8.4-exact, "at every q, ω". D-27's sufficiency proof (and s8-4 l.67) gives S_cc = λ_Z²S_ZZ only at ω ≠ 0.
   On the clamped branch the static Bragg term D changes the elastic δ(ω) part. Correction: write "at every q and every ω ≠ 0".
5. GAP, the same keyresult's hypotheses. The necessity proof uses a long-wavelength LA phonon that moves the crystal locally as a whole
   (D-27 "Necessity, small momentum"). The editor note lists "a sharp LA phonon" among the stated conditions, but the keyresult
   does not state it. Add "a crystal (a target with a long-wavelength longitudinal acoustic mode)" to the hypotheses beside
   "different masses per Z" and "F_N = 1". Fluids also qualify through sound, but the proof as written is for the crystal.
6. GAP (precision), s8-3 l.78 and D-26 l.62, "corrections of relative order q/G_min at sites without inversion symmetry". The
   first-order term is odd in G. For a real density, the odd part of n^{(κ)}_G is i·Im n^{(κ)}_G, so the O(q/G) correction is
   **purely imaginary**: it enters Im 𝓜³_eκ, which a T_d site allows, since 𝓜³_eκ need not be real. Re 𝓜³_eκ is corrected only at
   O((q/G)²) at T_d sites too. Add one clause.
7. Wording, s8-3 l.143, "in a harmonic crystal". Campbell-Deem et al. Table I also lists the anharmonic multiphonon channel at q⁴
   (and helium). Say "in a crystal with a coupling proportional to mass".

## Known items (editor-notes) — status
- 8.1 sign flips for i = 3, 5, 9, 10, 11, 13, 14: CONFIRMED (see 8.1 below).
- NOTATION l.681, 𝓜^k unit "eV^{k+1}": CONFIRMED WRONG. It must be **eV^{k+3}**: S_ab is eV², and dω·ω^k adds eV^{k+1}. This agrees
  with the text (s8-3 l.39) and with 𝓜¹ = eV⁴ (NOTATION l.359).
- 8.3 mixed third moment: CHECKED independently (below).
- 8.4 exactness theorem: CHECKED, with GAPs 4 and 5 above.
- 𝒥^{αβ}_s (spin current) has no NOTATION row, and C.20's 𝒥(ω) (NOTATION l.839) clashes with it: still open, as in the editor note.
  Also missing from NOTATION: 𝐬_e/𝐣_e as rows of 8.1, n_M, 𝖳^{αβ}, n_e^{(κ)}, λ_Z and a_N (all "rule at merge").
- 8.1 Coulomb-energy row (l.184): there is no later user in these files; no derivation issue.

## 8.1 Dark-matter couplings (s8-1, D-24)
- eq:8.1-vperp / D.24-vperp: CHECKED. Boost invariance holds. For an electron at rest, v⊥ = v − q/2μ. D.24-free gives q·v⊥ = Δχ
  (sympy: p² − p'² = q·(p + p'), k'² − k² = q·(k + k')). Dimensionless.
- Sign convention vs sources: CHECKED. Fitzpatrick Eq. (11): q = p' − p = k − k' (momentum the DM gains), and Eq. (14):
  v⊥ = v + q/2μ_N. Anand Eq. (10) is the same. The book's q is lost by the DM, and its v⊥ = v − q_book/2μ = v + q_F/2μ, so v⊥ is
  identical, as l.20 says. The operators odd in q are O3, O5, O9, O10, O11 (one q) and O13, O14 (one q); O6 and O15 have two
  q's. The flip list {3, 5, 9, 10, 11, 13, 14} is complete and correct. Independent cross-check: Anand Table 1 row 2 gives
  N̄iγ⁵N → +i q_A·S_N/m_N, and D-24 gives −i q_book·S/m; these agree because q_A = −q_book. Trickle et al. Eq. (12) uses
  q = p − p' and says it is opposite to Refs. [58, 60–62] (Fitzpatrick/Anand), which agrees.
- Table 8.1 operator definitions: CHECKED against Fitzpatrick Eqs. (19)–(24), (45) and Anand Eqs. (12), (13): /m_N as in Anand,
  O15 = −(S_χ·q/m)[(S_N×v⊥)·q/m], O16 omitted (Anand Eq. 14 shows it is dependent). The count is fifteen.
- Table 8.1 reductions: CHECKED term by term (O2, O3, O5, O7, O8, O9–O15). The index order of 𝒥^{γα} in O3 and of 𝒥^{γβ} in O12
  and O15 (velocity index first) is consistent with D-24 l.63–69.
- eq:8.1-rows: CHECKED. The plane-wave elements are 1, S, K/2m, K^αS^β/2m and K²/8m. The second form of 𝒯 uses K² = q² + 4k·k'
  (sympy). Units: n, s dimensionless; j, 𝒥 dimensionless (velocity); 𝒯 eV. These match NOTATION 𝒯_e "eV".
- Bilinears D.24-S-V0, D.24-bilinears: CHECKED by explicit Pauli algebra. Scalar: 1 − K²/8m² − iS·(q×K)/4m². V⁰: 1 − q²/8m² + iS·(q×K)/4m².
  Spatial V: K/2m − i(q×S)/m. A^i: 2S; A⁰: S·K/m. P: −iq·S/m. These agree with Trickle Table I (q of the same sign).
- D.24-vector (Proca, ω ≪ q): CHECKED. The sign of the spatial term follows from H = y(A'⁰J⁰ − A'·J).
- l.22 model → operator list: CHECKED against Anand Table 1 (rows 2 → O10, 4 → O6) and Trickle Table II (EDM → O11;
  MDM → O1, 4, 5, 6; anapole → O8, 9). The O2 statement agrees with Anand Sect. 2.1 (O2 discarded). Catena Table I omits O2: CHECKED.
- eq:8.1-O7O8, eq:8.1-O2: CHECKED. Dimensions: each 𝒪 is dimensionless and c_i is eV⁻², as Ṽ.
- eq:8.1-transverse / D.24-long: CHECKED. q·v̄_χ = ω + Δχ follows from eq:1.3-omegaq (ω_q = q·v − q²/2mχ − Δχ), and
  ⟨f|q·j|i⟩ = ω⟨f|n|i⟩ holds for local potentials. The spin-current analogue needs [H, S_j] = 0, as stated.
- eq:8.1-D / D-24 spin traces: CHECKED. The tensor is Hermitian and PSD; Tr(S^αS^β) = δ(2S+1)S(S+1)/3, which gives 1/4 for S = ½.
  Dimension: eV⁻⁴ × (model velocity factors).
- eq:8.1-nuclear / D-24 nuclei: CHECKED (Wigner–Eckart: w J = c_p⟨S_p⟩ + c_n⟨S_n⟩). ²⁹Si ⟨S_n⟩ = 0.156 and ⟨S_p⟩ = 0.016 agree with
  Klos et al. Table III ("This work"). The numbers: c₄ = 0.312c₄^{(n)}; 0.312² × ¾ = 0.0730; the ratio to a free neutron is 9.7 %
  ("10 %"); A² = 841. Fitzpatrick Eqs. (26)–(27) do split v⊥ into nuclear-c.m. and internal parts: CHECKED. The D-24 l.89 spin weight
  (4/3)(J+1)J⁻¹[…]²: CHECKED.
- l.113 numbers: 2mχv_max = 5.3 MeV at 1 GeV ("≈ 5"). 1/R = 197.3/3.47 fm = 56.9 MeV (s1-4). The max recoil on Si at 1 GeV is 498 eV
  (0.50 keV): CHECKED.
- WE 8.1 (dark photon): CHECKED. c₁ = y_χy_e/(q² + m_V²) with y_e = −ζe, c₁^{(p)} = −c₁^{(e)}, and the sum gives −Ṽn_Z.
  q_max = 53 keV; (q/m_V)² = 3.1×10⁻⁶; q₀²/8m_e² = 6.7×10⁻⁶; (53 keV)²/8m_e² = 1.34×10⁻³; v_max v_F = 1.85×10⁻⁵;
  q²/4mχm_e = 1.37×10⁻⁴. F_N − 1 ≲ (qR)²/10 ~ 10⁻⁷.
- WE 8.2 (O2): CHECKED, every number. k_∥ = −1.18 keV, 2.55 keV; annulus 2.499–3.370 keV; ⟨v_eT²⟩ = 3.37×10⁻⁵;
  ⟨v_eT⁴⟩ = 1.167×10⁻⁹; v_min = 1.360×10⁻³; A = 2.152×10⁻⁶; ratios 15.7 and 6.5. The azimuthal average (A+B)² + 2AB holds (sympy).
  Terms 0.0046/0.290/1.167 ×10⁻⁹, total 1.462×10⁻⁹; shares 0.32 %/19.8 %/79.8 %; ×91 the naive v⁴.
- l.159: Zα = 0.102 for Si 1s: CHECKED.
- Absorption, eq:8.1-alp: CHECKED from eq:1.4-alp (= Mitridate Eq. 18). The element of ψ†σ·∇↔ψ is iσ·K = 4im_e S·K/2m_e, which gives
  −(g/m_e)∂_tφ 𝒥^{αα} in ℒ and + in H. The first term: −(g/2m)∇φ·σ = −(g/m)∇φ·s, which gives + in H.
- eq:8.1-scalar: CHECKED. ∇↔² (s1-4 definition = Mitridate) has element −K², and (1/8m²)(−K²) = −(1/m)(K²/8m). H = −ℒ gives
  −gφ[n − 𝒯/m]. The bracket is the O(v²) term of ū'u in D.24-S-V0 (the spin–orbit term is dropped, O(p_φ·v)). Mitridate
  Sect. III C (kinetic term dominates) and Sect. III B: CHECKED.
- eq:8.1-omega-inel / D-24 l.99–104: CHECKED (sympy). Fermionic: ω = mχ − q for v → 0, and on a free nucleus E_R ≈ mχ²/2M, which
  agrees with Dror et al. 2020 Eq. (2) (q ≃ mχ, E_R ≃ mχ²/2M). The operators agree with Dror 2020 Eq. (1) and Dror 2021 Eqs. (1)–(2).
  "Larger than an elastic recoil by 1/v²" is an order of magnitude (max elastic 2mχ²v²/M; ratio 1/4v²); acceptable.
- l.20 "4mχm_e c_i": CHECKED against NOTATION ℳ (|ℳ|² = 16mχ²m_e²|Ṽ|²).

## 8.2 Master rate formula (s8-2, D-25)
- eq:8.2-rate / D-25 scattering: CHECKED. The spin sums give the trace (completeness over s'), Σ_{p'} = V∫d³q/(2π)³, and one 1/V
  goes into S_ab of eq:4.2-Sab. Dimension: [d³q] eV³ × 𝔇 eV⁻⁴ × S eV² = eV, a rate.
- eq:8.2-spectrum: CHECKED. ρ_χ/(mχρ_T) × eV → events per mass per energy. The single-row limit goes to A.8-rate. The direction average
  gives η(v_min)/2q (∫d³v f δ(ω − q·v + …) = η/q per dq, angular half): consistent with eq:1.5-rate.
- Index order, s8-2 l.22 / D-25 l.33–38: CHECKED. Tr[𝔇Sᵀ] = Tr𝔇_RS_R + Tr𝔇_IS_I and Tr[𝔇S] = Tr𝔇_RS_R − Tr𝔇_IS_I (sympy with random
  Hermitian matrices). The difference is 2Tr[𝔇_IS_I]. Sᵀ = S* is PSD, so the rate is ≥ 0.
- eq:8.2-abs / D-25 quantized field: CHECKED. Matrix element √(N/2ωV), Γ = NΓ_abs, emission (N+1)e^{−βω}Γ_abs. The FDT step
  −2Im Σx*x R = (1 − e^{−βω})Σx*xS uses eq:4.2-fdt (s4-2 l.71). Dimension: for a dimensionless g on a dimensionless row (scalar:
  g_φee on n_e and 𝒯_e/m_e), g²S/2ω = eV²/eV = eV, a rate.
- Classical field, D-25 l.69–94: CHECKED. ⟨energy density⟩ = Σ2ω²⟨|φ_k|²⟩, so n_k = 2ω⟨|φ_k|²⟩. Single mode: |φ₀| = φ₀/2,
  ρ = m²φ₀²/2. Rate VΣ n_kΓ_abs.
- l.55 numbers: ρ_χ/(m⁴v³) = 1 at m_φ = 6.93 eV ("≈ 7"). t_coh = 1/(m v₀²) = 1.04 ns at v₀ = 238 km/s ("≈ 1 ns"). CHECKED.
- l.57 / D-25 mixing: CHECKED. J = −ζm²Π/(m² − Π)A'; Im[Π(m² − Π*)] = m²ImΠ; Γ = ζ²m⁴σ₁/|m² − Π|². This agrees with Hochberg 2017
  Eqs. (5)–(6) (κ²_eff = κ²m⁴/|m² − Π|²) and Mitridate Eqs. (20)–(22), (34), (40).
- eq:8.2-db / D-25 l.108–126: CHECKED. The reverse amplitude uses Ṽ† and O†, which gives 𝔇_ba, and relabeling closes it; p_f = p_i e^{−βω}.
- l.30 Born estimate: |f|m_V = μ|Ṽ|m_V/2π = 2.3×10⁻⁸ ("2×10⁻⁸"): CHECKED.
- Fig. 8.1 caption: ω_max = 35.1 eV at q = 26.5 keV; q = m_φv = 40 meV: CHECKED (fig8_1.py inputs match).
- WE 8.3 (polarized gas): CHECKED, every number. k_F↑ = 4.498 keV, v_F↑ = 8.80×10⁻³, E_F↑ = 19.80 eV, linear edge 19.22 eV.
  S↑ = m²ω/2πq = 5.57×10⁷ eV²; the one-spin Lindhard linear region is independent of k_F (derived: k_T² range = 2mω). The rank-one
  matrix and (Ṽ_n + ½Ṽ_s)² hold. The cross term c₁c₇(v_T·ẑ)S↑ holds: longitudinal parts cancel since (2k+q)·q̂/2m = ω/q = q̂·v̄_χ.
  v_T = 1.467×10⁻³. O7 bound (v_max + v_F↑ + q/2m)²/4 = 5.70×10⁻⁵; k_F↑²/2mω = 3.96 ("4.0"); cross/O7 = 5.1 ("at least five").
  |v_E| = 8.36×10⁻⁴. Partial polarization 0.5: minority edge 7.07 eV, S_ns/S_nn(10 eV) = 0.0676 ("0.068").
- l.116 "twice the geometric mean": consistent with eq:8.3-bound.

## 8.3 Exact relations (s8-3, D-26)
- eq:8.3-bound: CHECKED. λ-scaling keeps 𝔇 PSD (D·𝔇·D, D real diagonal); the discriminant gives Γ_AB² ≤ 4Γ_AΓ_B; the band
  (√Γ_A ∓ √Γ_B)² holds. "From zero to twice the sum" ((a+b)² ≤ 2(a²+b²)) holds.
- eq:8.3-moments / D-26 l.7–12: CHECKED. The two Lehmann lines give ∫ω^k[S_ab(q) − (−1)^kS_ba(−q)] for the commutator. This is the
  stated sum for odd k (commutator) and for even k (anticommutator). f-sum check: [n(−q), q·j(q)] = Nq²/m, i.e. 𝓜¹ = n q²/m.
  Units eV^{k+3}.
- eq:8.3-hankel: CHECKED (positive measure; the T = 0 shifted Hankel matrix).
- l.50 divergence of 𝓜⁴: CHECKED (∫d³y y⁻⁴ ~ ∫dy/y²). Hydrogen df/dω ∝ ω^{−7/2}, so S ∝ ω^{−9/2}; ω³S is integrable and ω⁴S is not.
  D-26 triangle-inequality argument: CHECKED.
- **eq:8.3-M3 (PRIORITY): CHECKED independently.** My chain: [n_e†, H] = q·j_e†; [U, q·j_κ] = (i/M)Σe^{iqX}q·∇_IU;
  [q·j_e†, F(r_j)] = −i e^{−iqr_j} q·∇F; and (q·∇_j)(q·∇_I)w = −(q·∇)²w. The result is
  𝓜³ = −(n_κ/m_eM)∫d³y n_e^{(κ)}(y)e^{−iq·y}(q·∇)²w. Stationarity identity: ⟨[X,[H,Y]]⟩ − ⟨[[X,H],Y]⟩ = ⟨[H,XY]⟩ − ⟨[H,YX]⟩ = 0.
  Kinetic and e–e/n–n terms drop out. Dimension: eV·eV⁵ = eV⁶ = eV^{k+3}. D-26 l.38–45 term by term: CHECKED (sympy for f³ − g³,
  the same-particle potential (1/m²)(q·∇)²U, and the dropped (iq²/m²)⟨q·∇U⟩ = 0).
- eq:8.3-M3lim: CHECKED. Hessian of 1/y = −(4π/3)δ + (3cos² − 1)/y³ (sympy). The contact part gives n^{(κ)}/3; the uniform quadrupolar
  part gives 2n_e/3 via ∫dΩ e^{−iq·y}P₂ = −4πj₂ (verified numerically) and ∫₀^∞ j₂(x)/x dx = 1/3 (sympy). e² = 4πα (NOTATION l.15).
  D.26-Gsum: FT of (q·∇)²w = Ze²(q·(q−G))²/|q−G|²; the cubic-star average of (q·Ĝ)² is q²/3, so q²[n_e + (n^{(κ)} − n_e)/3]: CHECKED.
  Order of limits as stated. See finding 6 on the O(q/G) term.
- eq:8.3-M3sph: CHECKED (prefactors: −(n/mM)(−Ze²/4π)[−(4π/3)q²n(0) − 8πq²∫n̄j₂/y]). Large-q limit: bracket → n^{(κ)} (stated
  "rises to n^{(κ)}"; "toward 3n^{(κ)}" in the M3lim bracket is the same statement). A(x) limits: A(0) = 1, A(∞) = 1/3 (sympy).
- Spring reading (l.76, D-26 l.53): CHECKED. (q·∇_r)(q·∇_X)½K(r−X)² = −Kq²; spectral side −q²[mM/(m+M)²]/(2μω_r) × 2ω_r³/V
  = −Kq²/(mMV). See finding 2 for the COM order.
- WE 8.4 (Si third moment): CHECKED independently. My ROHF (uncontracted cc-pCVQZ + 7 tight s, Becke 3D grid) gives
  E = −288.8542 Ha (Bunge −288.854, which confirms the cited value indirectly; the paper was not fetched), n(0) = 1764.3 a₀⁻³ (text 1765),
  and B/n(0) = **0.3353 / 0.3474 / 0.4265** at 10/30/100 keV (text 0.3353/0.347/0.427). Other numbers: 1765 a₀⁻³ = 1.191×10²⁸ cm⁻³;
  2n_e/n^{(κ)} = 1.18×10⁻⁴; q = 2.682 a₀⁻¹; 1/q = 0.197 Å; 14/a₀ = 52.2 keV; √(Z e²B/m_e) = 8.780 keV (q → 0: 8.755, "8.76").
  The "1.8×10⁻⁴" is n_e/B (we8_4.py), a bound by the full n_e, not 2n_e/3 (which gives 1.2×10⁻⁴): fine as "at most". The 3s share
  7.6/1765 = 0.43 % holds.
- l.85 "relativity raises the contact density by ~8 % in Si": not sourced in the text (deferred to 12.5). My point-Dirac/finite-nucleus
  estimate is (1+γ)/Γ(2γ+1)·(2ZR/a₀)^{2(γ−1)} = 1.077 for R = 3.1 fm: CHECKED as an estimate. 12.5 should cite a source.
- eq:8.3-M3ss / D.26-M3: CHECKED. The free-particle check is (a+b)³ + (a−b)³ = 2a³ + 6ab² with a = q²/2m. ⟨(q̂·p)²⟩ = 2mK̄/3.
  Jellium: ∇²U_bg = e²n_e gives f-sum × ω_p² (ω_p² = e²n/m, HL units). l.159: √(e²[n^{(κ)} + 2n_e]/3m_e) = 2.340 keV;
  q²/2m_e = 97.8 eV; K̄ = 288.854 Ha/14 = 561.4 eV (virial), so √(2q²K̄/m_e) = 468.8 eV ("469"): CHECKED.
- eq:8.3-M3ee / D-26 l.105–113: CHECKED independently. e–n enters only at i = j (contact; the uniform quadrupolar part cancels
  against the e–e "1" term by neutrality). e–e: Σ_{i≠j}(1 − e^{−iq·r})(q·∇)²w_ee, with contact cancelling and 2e²q²n_e/3 per electron.
  Ward: m_e𝓜³_ee + Σ_κM_κ𝓜³_eκ = 0 at O(q²) under n_e = ΣZ_κn_κ (sympy).
- eq:8.3-mass, eq:8.3-ward: CHECKED (Σ_s m_s j_s = g; ω_fi⟨n_M⟩ = q·⟨g⟩; the conjugation slot is consistent with eq:4.2-Sab).
- eq:8.3-flux / D.26-flux: CHECKED. g = ΣA(p + q/2); kinetic part via D.26-shift; pair part via A_i − A_j = iq·r_ij∫dλ…;
  sign −Σ∂^αw r^β∫. Dimension: 𝖳 eV² (g eV, q eV, [H, g] eV²).
- eq:8.3-soft: CHECKED (two Ward steps; S_{n_Mn_M} ∝ q⁴/ω⁴). Campbell-Deem Table I (acoustic ∝ q; optical and two-phonon ∝ q⁴
  for mass coupling) and Sect. V B (helium): CHECKED. See finding 7.
- eq:8.3-boostward: CHECKED. (m_e/M)² = 3.82×10⁻¹⁰ ("3.8×10⁻¹⁰", M = 26.16 GeV). The D-26 boost route: Σ_I∇_IΨ = −Σ_i∇_iΨ,
  P_e = i m[H, Σr]; the algebra closes to −(m_e/M)⟨iq·Σr⟩.
- WE 8.5 (chain): CHECKED independently. One phonon: ⟨n⟩ = iq(N/2Mω)^{1/2}, ⟨g⟩ = i(NMω/2)^{1/2}. Two phonons: −q²/2M√(ωω'),
  −q(ω+ω')/2√(ωω') (both orderings counted). Flux element 4iK sin²(qd/2)(N/2Mω)^{1/2}, which gives Mω² = 4K sin²(qd/2).
  Numbers: d = 1.358 Å, M = 26.16 GeV, c = 6.61 km/s, qd = 0.688, ω_q = 21.6 meV, q²/2Mω_q = 8.8×10⁻⁴.
- Table 8.3 (tab:8-exact): the hypotheses agree with the derivations. The "local" hypothesis for the Ward identity is right
  ([H, n_s] = q·j_s needs local potentials).
- l.70 Puff 1965 (single-species third moment): not fetched (APS, not open access); attribution only.

## 8.4 Screening (s8-4, D-27)
- eq:8.4-proper → eq:8.4-screened / D-27: CHECKED. δn = (1 − Pv)⁻¹R̃_Zbφ; push-through v(1 − Pv)⁻¹ = (1 − vP)⁻¹v;
  ε_GG' = δ − v_G R̃_{Z_GZ_G'}. The Hartree field sign: H = v_Cδn_Z·n_Z, and with δO = Rφ and R < 0 static, ε > 1.
  Dimension: R̃ eV², v_C eV⁻², so ε is dimensionless.
- eq:8.4-rank1: CHECKED (scalar case). D.27-ZZ: vR_ZZ = ε⁻¹ − 1 (sympy). Hence S_ZZ = −2ImR_ZZ/(1 − e^{−βω}) = (2q²/e²)L/(1 − e^{−βω}).
  This agrees with Knapen et al. Eq. (6) (k²/2πα = 2q²/e², e² = 4πα). Knapen Eq. (8) and the text below it (two bases): CHECKED.
  Im(R̃ε*) = ImR̃: CHECKED.
- eq:8.4-electron / D.27-ee: CHECKED (bilinearity). Limit: clamped nuclei give eq:4.4-eps.
- Spin rows unscreened (spin-rotation invariance) and longitudinal current as (ω/q)n: CHECKED. Π_em/q² ≈ ω_p²/q₀² = 1.98×10⁻⁵
  ("2×10⁻⁵"): CHECKED.
- **Exactness theorem (PRIORITY), eq:8.4-exact / D-27 l.43–67: CHECKED, with GAPs 4–5.** Sufficiency: D static means the same transitions.
  Large q: recoil peaks at q²/2m_s with weight c_s²n_s and widths ∝ q, separated ∝ q², which needs distinct masses per Z; this gives
  D.27-peaks. Small q: the acoustic amplitude ∝ qΣc_sN_s, while S_ZZ starts at q⁴ (piezo/strain charge), which gives D.27-acoustic.
  Conclusion via Cauchy–Schwarz per mass group: the equality forces c_κ = λZ_κ. I re-derived the steps and they hold, including the
  isotope grouping. The sign freedom ±λ_Z is consistent between s8-4 and D-27. Hochberg et al. 2021 attribution (p. 2: "as long as ion
  contributions to the loss function are negligible … screened identically"): CHECKED.
- WE 8.6 (GaAs nucleon coupling): CHECKED. Vertex a_N (u_Ga = μ/M_Ga u_rel); Born-charge vertex Z*(μ/M_Ga + μ/M_As) = Z*. Pole algebra
  (sympy): R̃_NN + screening = C/(ω² − ω_L²) exactly, with ε = ε∞(ω_L² − ω²)/(ω_T² − ω²) and e²Z*²/(Ωμε∞) = ω_L² − ω_T².
  S_NN = πC/ω_L δ(ω − ω_L) from S = −2ImR. Units: C = q²|a_N|²/(μΩ) is eV⁴, so R = C/ω² is eV². Numbers (AME2020 masses, IUPAC
  abundances as quoted; the tables were not fetched, but the inputs are the standard values): M̄_Ga = 69.723 u, μ = 36.114 u,
  Ā/M̄ = 1.001072 (Ga) and 1.001046 (As), a_N(0) = 9.37×10⁻⁴ ("9.4×10⁻⁴"). |Δτ| = √3a/4 = 2.441 Å with a from Ω = 44.80 Å³
  (a = 5.638 Å; consistent with we:5-lst). Crossover at q ≈ 0.021 eV; ω_L/v_max = 13.72 eV; |a_N| = 0.614 (×656) at 13.7 eV and
  4.48 at 100 eV; optical share μ(q·Δτ)²/M_cell = 7.2×10⁻⁵ and 3.8×10⁻³; ΣA = 144.8; Z*/ε∞ = 0.194. Griffin et al. Eqs. (30), (33)
  (in-cell destructive interference for the optical mode under an A-proportional coupling): CHECKED. See finding 3.
- Coulomb-line classes / D-27 l.69–81: CHECKED (tree plus one line closes one cycle; bridges carry q + G; momenta on the cycle
  Q + G, Q + q + G, Q + G; the second case puts the phonon bridge in the ionic ε). The static vertex: reality plus Onsager give
  R(Q, −ω') = R(Q, ω')†, even below the gap: CHECKED. (ω_Q/E_g)² = 2.6–3.0×10⁻³ for 60–64 meV ("3×10⁻³"). See finding 1.
- In-medium mixing: CHECKED. |ε|² = ε₂/L = 774 ("770"; ε₂ = 2.4 and L = 3.1×10⁻³ are taken from 4.4, not recomputed here).
  eq:8.4-zetaeff is dimensionless. Π_L = (ω² − k²)(1 − ε) agrees with Mitridate Eq. (34) (Q² = ω² − q²); Γ_net = ζ²m_φL agrees with
  Eq. (40) (κ²σ₁/|ε|²m_φ per ρ/ρ_T); Eqs. (20)–(22) mixing term Π_φAΠ_Aφ/(m² − Π_AA): CHECKED.
- Table 8.4 (tab:8-screening): CHECKED against the text. The total-charge row is exact at all ω. If finding 4 is adopted, the
  electron-density row's "clamped nuclei only" should read "clamped nuclei, ω ≠ 0".

## 8.7 PRIORITY (outside these files; for derivation-2)
- Pair-by-pair in/out equality for PT-invariant targets (s8-7 l.72): CHECKED algebraically. With PTψ_nk(r) = ψ*_nk(−r) (possible
  when (PT)² = +1: no SOC, even N), substituting r → −r gives ρ_cv(k, q+G) = ρ_cv(k, q+G)* for every G in a common gauge. Then
  R_GG' = R_G'G. For f real symmetric (RPA: f = v_C δ; a real xc kernel), the advanced weight is the conjugate of the retarded
  (ε̃⁻¹)_G0, and |Σ_G w_Gρ_G| = |Σ_G w_G*ρ_G| for real ρ. Degenerate bands: the statement holds for the degenerate set, as the text
  says. Caveat: an xc kernel that is Hermitian but not real-symmetric would break the step; the text's "Hermitian kernel" should read
  "real symmetric kernel" for this claim. The EPM Si/GaAs numbers (15 %) are left to derivation-2.

## Sources consulted
Fetched and checked: Fitzpatrick 2013 (1203.3542), Anand 2014 (1308.6288), Trickle 2022 (2009.13534), Trickle 2020 (1910.08092),
Catena 2021 (2105.02233), Klos 2013 (1304.7684), Mitridate 2021 (2106.12586), Dror 2020 (1905.12635), Dror 2021 (2011.01940),
Hochberg 2021 (2101.08263), Knapen 2021 (2101.08275), Griffin 2018 (1807.10291), Campbell-Deem 2020 (1911.03482),
Hochberg 2017 (1608.01994). Not fetched (not open, or a book or table): Puff 1965, Sakurai 2017 (Chap. 6, Born series), Bunge 1993
(reproduced indirectly), AME2020 and IUPAC 2013 (standard values used).
