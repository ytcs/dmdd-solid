# Ch5 derivation check (isolated verifier, SKILL.md §5)

Scope: ch05.tex, s5-1 … s5-7, D-13 … D-15, C-18. Algebra redone by hand and with sympy; numbers recomputed from the cached
QE outputs (fig5_1_data.npz, fig5_2_data.npz, fig5_3_data.npz, fig5_6_fc.npz, gaas_cache/) and from the stated inputs. No QE was run.
Verifier scripts: /tmp/claude-0/-home-user/364f612b-be7d-56fd-924b-36b7d0d3bbab/scratchpad/v5/{n1..n8,s1,s2}.py.
Sources were fetched to sources/review-ch05/ as html and txt; the PDFs were deleted.
Items in editor-notes.md (15.5/15.53 THz, 52.3/52.33 GeV, Flensburg "measured", E_R vs E_{\mathrm R}, D.15 normalization, the D.14
comma splice, the GaAs 5.8 meV ASR value, and the citation-audit items) are not repeated below.

Legend: CHECKED = redone and correct; WRONG = error, with the correction; GAP = correct in substance, but a step, a pointer or the
wording needs repair.

## Summary of findings (details in the sections below)
1. WRONG, s5-4 WE 5.6 (we:5-frozen) and s5-7: Φ⁽⁴⁾_opt ≈ 90 eV Å⁻⁴ is not supported by the data, and "the quartic correction is
   0.02 eV Å⁻² at 0.03 Å, 0.15 %" is arithmetically wrong even with Φ⁽⁴⁾ = 90.
2. WRONG, s5-2 WE 5.3, last paragraph: "The two agree below about 7 meV". The computed g_ph is 1.28–1.40 × g_D at 1–7 meV.
3. GAP, s5-2 WE 5.3 against the accepted C.18: the "isotropic model of App. C.18" is not C.18's isotropic convention.
4. WRONG (wording), D-13 eq. D.13-scales: "the fraction κ_BO of a bond length" should be "of the Bohr radius".
5. GAP (factor 2), s5-1 after the key result: the exact frequency differs by m_e/M; this holds for ω², and ω differs by m_e/2M.
6. Notation: p_n carries two meanings in 5.6; Λ clashes with the 8.7 row; w carries three meanings; ω_D is italic in D.15; several
   Chap. 5 symbols have no NOTATION row (list at the end).

## 5.1 (s5-1.tex)
- Intro of ch05.tex: 2E_g/v_max² = 0.333 MeV, 2ω/v_max² = 18.3 keV (v_max = 794.5 km/s), m_e/M ≈ 2×10⁻⁵ → CHECKED.
- ¶1: 15.5 THz = 64.10 meV, period 64.5 fs, 2π/E_g = 3.53 fs, ratio 18.3 → CHECKED.
- eq:5.1-coupled, eq:5.1-N (projection of the nuclear Laplacian onto Ψ_j) → CHECKED; it agrees with D.13 term by term.
- eq:5.1-BO and the Born–Huang N₀₀ remark → CHECKED (N₀₀ = Σ⟨∇Ψ₀|∇Ψ₀⟩/2M_κ ≥ 0, from D.13).
- eq:5.1-expand → CHECKED.
- eq:5.1-scales: the balance (m_e/M)(a₀/ℓ)² = (ℓ/a₀)² gives ℓ/a₀ = κ_BO and ω ~ α²m_eκ² → CHECKED.
- Power counting ¶ (cubic κ³; derivative coupling (1/M)(1/a₀)(1/κa₀) = α²m_eκ³; scalar coupling κ⁴; second order κ⁶) → CHECKED. 1/M = κ⁴/m_e and 1/(m_ea₀²) = α²m_e.
- keyresult (Born–Oppenheimer hierarchy) → CHECKED.
- After the keyresult: "the exact vibrational frequency differs from the Born–Oppenheimer one by the relative amount m_e/M" → GAP (factor 2). eq:D.13-model gives ω² = (K_N/M)(1 − m_e/M + …), so ω_exact/ω_BO − 1 = −m_e/2M. Correction: "the exact squared frequency differs … by m_e/M" (equivalently, ω by m_e/2M; the mass becomes M + m_e). The order-of-magnitude statements are unaffected.
- eq:5.1-mixing: (1/M)⟨Ψ_j|∇Ψ₀⟩·∇ ~ ωℓF/ΔE with ℓ² = 1/(Mω); dividing by ΔE gives the result → CHECKED. It is dimensionless.
- eq:5.1-HF and the electrostatic force (Heaviside–Lorentz, e² = 4πα: attraction toward the density, repulsion from the nuclei, signs and 4π) → CHECKED.
- eq:5.1-dcoup: from ⟨Ψ_j|∇H|Ψ_i⟩ + E_j⟨Ψ_j|∇Ψ_i⟩ = E_i⟨Ψ_j|∇Ψ_i⟩; the V_NN term drops for j ≠ i → CHECKED (sign E_i − E_j correct).
- eq:5.1-Fk → CHECKED (definition).
- Frozen-phonon ¶ (from fig5_1_data.npz). Quartic fit over |u| ≤ 0.1 Å: Φ_opt = 13.63 eV Å⁻², Φ⁽³⁾ = −41.5 eV Å⁻³. ω = (2Φ/M)^{1/2} = 63.70 meV with M = 28.0855 u. Hellmann–Feynman against the degree-6 fit, |u| ≤ 0.2 Å: max deviation 0.059 % (stated "< 0.1 %"). All → CHECKED. The cubic invariant u_xu_yu_z of the F2g optical coordinate is nonzero along [111] and zero along [100] → CHECKED.
- Fig. 5.1 caption: ℓ_zp = (M_κω_opt)^{-1/2} = 0.0483 Å → CHECKED. Typo: "Gray dashed: the estimate κ_BO a₀ (gray dashed)" repeats "gray dashed"; delete the parenthesis.
- WE 5.1: m_e/M = 1.961e-5, κ = 0.0665, κ² = 4.43e-3, κ³ = 2.95e-4, κa₀ = 0.0352 Å, κ²α²m_e = 0.120 eV, ω/α²m_e = 2.36e-3 = 0.53κ², ω/E_g = 0.0548 = 12.4κ², α²m_e/E_g = 23, E_g/ω = 18 → CHECKED. ⟨u_x²⟩^{1/2}: 0.050 Å is 1.42 κa₀; √0.005941 = 0.0771 Å; 0.0495/a = 0.0091; κ/0.0091 = 7.3; a = 10.3 a₀; bond = 4.44 a₀; 0.050/2.352 = 0.021 → CHECKED. The 4³-grid DOS (fig5_1) gives 0.0497 Å at 0 K and 0.0812 Å at 293 K → CHECKED. η = 41.5×0.048/(3×13.6) = 0.049 → CHECKED. κ⁴ω = 1.26 µeV ("about 1 µeV") → CHECKED.

## 5.2 (s5-2.tex)
- eq:5.2-eom → eq:5.2-Ddyn: insertion of the ansatz; the sign e^{+iQ·R} matches eq:A.6-Ddyn and Giustino Eq. (14) → CHECKED. Hermiticity, D(−Q) = D(Q)*, and D(Q+G) = D(Q) → CHECKED.
- Scale estimate: α²m_e/a₀² = 97 eV Å⁻² against Φ_opt = 13.6 eV Å⁻², a factor 7 → CHECKED.
- WE 5.2 (diatomic chain): the force constants, D(Q), the characteristic polynomial and ω±² → CHECKED (sympy). The small-Q limit KQ²a_c²/2(M₁+M₂) and c → CHECKED (sympy). Eigenvectors, u₁/u₂ = −M₂/M₁, center of mass at rest, ω₀₊² = 2K/μ_red, zone-boundary ω² = 2K/M_{1,2} → CHECKED. Equal masses: (2K/M)(1 ± cos(Qa_c/2)) = folded chain with Q′ = 2π/a_c − Q → CHECKED. Numbers: a/4 = 1.358 Å; 12.32 THz = 50.95 meV; K = Mω²/4 = 6.90 eV Å⁻²; ω_X = 45.3 meV; c_LA = aω/8 = 6.61 km/s; GaAs gap (74.922/69.723)^{1/2} − 1 = 3.7 % → CHECKED. "the numbers, however, are off by up to 20 %": c_LA is 21.6 % low → GAP; write "by up to 22 %" or "by about 20 %".
- eq:5.2-asr, the acoustic vector in D(0), and the optical orthogonality Σ√M_κ e_κν = 0 → CHECKED. ASR violation 0.163 THz (npz) → CHECKED.
- First-order term: matrix element (iQ_γ/M_cell)ê^αê′^βT^{αβγ}; antisymmetry from pair symmetry; the torque identity → symmetric in βγ; the τ-term vanishes by the transposed ASR; the six-step alternation → T = 0 → CHECKED.
- eq:5.2-sound and the Λ formula: −(1/2M_cell)ΣΦ(Q·R)² from D₂ and the second-order −|o†D₁a|²/ω_o² → CHECKED (signs). The internal-strain remark (no D₁ coupling for LA along [100], nonzero for shear) → CHECKED.
- ρ_TΛ = Christoffel matrix; [100]: ρc_LA² = C₁₁, ρc_TA² = C₄₄ → CHECKED. Optical frequency × a/4 = 13.2 km/s; c/v_max = 0.011 → CHECKED.
- Phonons of Si (fig5_2_data.npz): PBE Γ 15.40 THz; X: TA 4.13, LA/LO 12.26, TO 13.85; L: TA 3.17, LA 11.15, LO 12.41, TO 14.69. Against Savrasov Table I (15.53/4.49/12.32/13.90/3.43/11.35/12.60/14.68; verified in the source): six of eight within 2 %, TA −8.1 % and −7.6 %, mean |dev| 2.59 % (used in 5.4 as "2.6 %"), Γ −0.84 % → CHECKED. Optical band at the zone boundary 12.3–14.7 THz → CHECKED. PBE a 5.477/5.431 − 1 = 0.85 % → CHECKED (agrees with s3-4). Note: Table E-functionals uses a different PBE value, 5.466 Å; outside scope.
- eq:5.2-dos, eq:5.2-dosac (∫Q²dQ δ(ω − cQ) = ω²/c³; prefactor Ω/2π²) → CHECKED; units eV⁻¹. DOS numbers, 48³ grid: raw normalization 6.000; peaks at 17.2, 57.9 and 60.5 meV; 22.4 % of the modes below 20 meV; g/(Aω²) = 1.09 at 7 meV → CHECKED. Intro ¶ and Summary: "peaks near 18 meV" against 17 meV in the body (computed 17.2) → GAP (cosmetic); use 17 meV throughout.
- eq:5.2-debye, eq:5.2-gD (9n_atω²/ω_D³, integral 3n_at), eq:5.2-cbar → CHECKED.
- WE 5.3 (Debye), recomputed with a 200×400 Gauss–Legendre×trapezoid sphere grid: c_LA[100] = 8.430, c_TA = 5.841; [110]: 9.131, 5.841, 4.672; [111]: 9.352, 5.091 km/s; ⟨c_ν⁻³⟩^{-1/3} = 9.004, 5.656, 5.040; LA share 9.3 %; c̄ = 5.886 km/s; n_at/Ω = 4.994e22 cm⁻³; Q_D = 1.4354 Å⁻¹ = 1.241(2π/a); ω_D = 55.61 meV = 13.45 THz; Θ_D = 645 K; per-cell convention 512 K; anisotropy 11 % and 25 %; ω_D 13.2 % below 64.1 meV → all CHECKED. Isotropic model with C₁₁ and C₄₄: c̄ = 6.352 km/s, Θ_D = 696 K (+7.9 %) → numbers CHECKED, but → GAP against C.18. C.18's "isotropic convention" is the one with the Lamé constants λ = 52.4 and µ = 68.0 GPa, which gives 9.0/5.4 km/s. That convention gives c̄ = 5.97 km/s and Θ_D = 655 K (+1.5 %), not 697 K. Either call the 697 K model "isotropic speeds c_LA² = C₁₁/ρ_T, c_TA² = C₄₄/ρ_T (the [100] speeds in every direction)" and drop the attribution to C.18, or quote 655 K for C.18's convention. (This is the WE 5.3/C.18 recheck that the editor notes ask for.) PBE ω² fit, 1–6 meV: c̄ = 5.42 km/s, Θ_D = 594 K; 37.7 % of the modes above ω_D; g < g_D between 26.1 and 55.6 meV → CHECKED. "The two agree below about 7 meV, where both follow ω²" → WRONG. Both follow ω², but the computed g_ph is 1.31 × g_D at 5 meV and 1.40 × g_D at 7 meV, since (5.886/5.42)³ = 1.28, as the same paragraph later explains. Correction: "Below about 7 meV both follow ω², with the computed coefficient 28 % larger, the cube of the 8 % deficit in c̄ discussed below."

## 5.3 (s5-3.tex)
- eq:5.3-normal ↔ eq:5.3-inverse (lattice sum plus completeness), u† = u_{−Q}, and [u_Q, p_{Q′}] = iδ → CHECKED.
- eq:5.3-Hnormal (kinetic and potential terms), the Heisenberg equations u̇ = p† and ṗ† = −ω²u → CHECKED (redone by commutators).
- eq:5.3-b, [b, b†] (two cross terms ½ each), [b, b] cancellation; the inversions u = (b + b†₋)/(2ω)^{1/2} and p† = −i(ω/2)^{1/2}(b − b†₋) → CHECKED.
- The bracket expansion leading to eq:5.3-Hb → CHECKED. Translation: b_Q → e^{−iQR}b_Q, b† → e^{iQR}b† → CHECKED.
- ZPE: mean ω = 40.90 meV; ½∫gω = 122.7 meV per cell → CHECKED.
- keyresult eq:5.3-u and the p expansion (relabel −Q, e(−Q)* = e(Q)) → CHECKED; it is identical to eq:A.6-u. Citation "Giustino [Eqs. (16)–(18)]": those are the orthonormality and e(−q) = e* relations. The displacement expansion is Giustino Eq. (20), with l_qν in Eq. (21) → GAP; cite Eqs. (16)–(21). The same applies to A.6, which is outside scope.
- eq:5.3-ell, ℓ(64.1 meV) = 0.0241 Å, equal to ℓ_zp/2 by e = ±ê/√2; ℓ(18.6 meV) = 0.0447; ℓ(5 meV) = 0.0860; N(1 kg) = 1.072e25; ℓ/√N = 7.4e-15 Å → CHECKED.
- eq:5.3-me; n_B(64.1 meV, 300 K) = 0.0914; n_B(18.6 meV) = 0.949; 1/√⟨u_x²⟩ = 25.6 keV ("26 keV") → CHECKED. The one-phonon amplitude (factor N/√N = √N, the phase e^{iq·τ}, δ_{q,Q+G}) → CHECKED.
- eq:5.3-B and its limits; the cubic-site reduction to eq:5.3-u2; (3/2M)⟨ω⁻¹⟩ and (3T/M)⟨ω⁻²⟩ → CHECKED.
- eq:5.3-debye (zero-point part 9/4Mω_D, thermal part 4(T/ω_D)²∫) → CHECKED. High-T: ∫₀^y x/(eˣ−1) = y − y²/4 + y³/36 − y⁵/3600; bracket 4/y + y/9 → CHECKED (sympy). ω̄ = 2ω_D/3 → CHECKED. Thermal = zero-point at T = 0.4399 Θ_D = 284 K → CHECKED.
- Computed vs Debye ¶: 4³ grid 0.0497/0.0812 Å; 48³ grid 0.0495/0.0799 Å at 293 K; difference ≤ 1.6 % → CHECKED.
- WE 5.4: M = 26.16 GeV; Mω_D = 1.4546e9 eV²; 9/4Mω_D = 1.5468e-9 eV⁻² = 6.023e-3 Å²; u_x = 0.0448 Å; ω_D/T = 2.151; ∫ = 1.2588; bracket 2.0886; ⟨u²⟩ = 1.2580e-2 Å²; u_x = 0.0648 Å (text 0.0647; rounding); √2.088 = 1.44; equipartition u_x² = 3.734e-3 (−11 %); ×1.1285 → 4.214e-3 against 4.193e-3 (0.5 %) → CHECKED. At 293 K: Debye 4.116e-3 Å² (31 % below 5.941e-3); DOS 2.446e-3 (0 K) and 6.379e-3 (293 K, +7.4 %); Debye low by 18 % and 35.5 %; modes below 20 meV 22.4 % carrying 44.5 % of the zero-point u²; Debye 4.65 % and 12.9 %; ⟨ω⁻¹⟩⁻¹ = 30.42 meV; ⟨ω⁻²⟩^{-1/2} = 25.22 meV; 37.07 and 32.10 meV → all CHECKED. The verdict "reproduces … to 20–30 %" is GAP: the computed deficits are 18 % (0 K) and 36 % (293 K). Write "20 to 35 %".
- Ge ¶ and Table 5.1: ρ = 5.344 g cm⁻³; c̄ = 3.542 km/s; Θ_D = 373.1 K; u_x = 0.0366 (0 K) and 0.0671 Å (300 K); T/Θ = 0.804; thermal/zero-point 2.35 ("2.4"); 64.1√(28.0855/72.63) = 39.9; mass ratio 2.59; TA_X/ω_D = 0.31 (Si 0.33) → CHECKED. Ge 9.1/2.4 THz = 37.6/9.9 meV and C_ij 131/49/68 against Haxhijaj Tables IV and III → CHECKED in the source. Si row 0.045/0.065/0.049/0.081/0.077 → CHECKED. The DFPT 300 K entry from the 48³ DOS is 0.0807 → 0.081. GaAs row (gaas_cache): TA_X 10.45 meV; Ga 0.0404/0.0803 Å; As 0.0392/0.0781 Å at 0/300 K → CHECKED. Optical 33.6/36.4 → CHECKED.

## 5.4 (s5-4.tex)
- ¶1: 216² ≈ 4.7e4 ("5e4") → CHECKED. The 16 irreducible points of the 6³ grid, 4 of 3³ and 3 of 2³ (Γ, X, L) → CHECKED.
- Force expansion, eq:5.4-fd (the central difference cancels the even powers; the residual Φ⁽⁴⁾h²/6) → CHECKED.
- eq:5.4-alias and the exact D(Q) on the N_Q³ grid; X needs the doubled cell (e^{iQ·R} = −1 for n₃ odd) → CHECKED. Ninth-power scaling → CHECKED against Baroni Sect. IV.2 (= IV.B), which states 3N_at × R⁹.
- WE 5.6 (frozen phonon), from fig5_1_data.npz: E(±0.03) = 5.943/6.316 meV; 2E/u² = 13.207/14.036; half-difference 0.4147 → Φ⁽³⁾ = −41.5; symmetric 13.621 (0.03 Å) and 13.641 (0.06 Å); ω = 63.68 meV; central HF difference 13.634 → 63.71 meV; one-sided ω −1.53/+1.51 % (0.03 Å) and −3.09/+2.99 % (0.06 Å) → CHECKED. "The quartic correction is 0.02 eV Å⁻² at 0.03 Å, 0.15 %, and Φ⁽⁴⁾_opt ≈ 90 eV Å⁻⁴" → WRONG on two counts. (i) Arithmetic: Φ⁽⁴⁾u²/12 at 0.03 Å with Φ⁽⁴⁾ = 90 is 0.0068 eV Å⁻² (0.05 %). The 0.02 is the difference of the corrections at 0.06 and 0.03 Å. (ii) Robustness: the two-point estimate (13.641 − 13.621)·12/(0.06² − 0.03²) = 90 rests on a 0.02 eV Å⁻² difference. That is comparable to the higher-order (Φ⁽⁶⁾) and numerical noise. Polynomial fits of the same data give smaller values: energies, degree 4, |u| ≤ 0.1 Å: 42; energies, degree 6, |u| ≤ 0.2/0.3 Å: 37/35; HF forces, degree 3/5: 38/36; central force differences at 0.03/0.06 Å: 54. Correction: "Φ⁽⁴⁾_opt ≈ 40 eV Å⁻⁴ (fits to the energies and forces over |u| ≤ 0.1–0.3 Å; the two-step estimate is noise-limited); the quartic correction to the symmetric combination is 0.003 eV Å⁻² (0.02 %) at 0.03 Å". Propagate the change to s5-7 (below). Pointer: "DFPT at the same settings gives 63.7 meV (Sect. 5.1)". Sect. 5.1 quotes 63.7 meV only from the frozen-phonon curvature. The 4³ DFPT run of fig5_1 has 63.67 meV (DOS top) → GAP; cite Fig. 5.1(b)/its caption, or state the value here. 63.69 meV (fig5_2) and 64.1/63.69 − 1 = 0.65 % ("0.7 %") → CHECKED.
- eq:5.4-hess (Baroni Eq. (10)) → CHECKED in the source.
- eq:5.4-Dwave: Σ_{RR′}e^{−iQ·R}e^{iQ·R′}Φ(R,R′) = NΣΦ(0,R)e^{iQ·R} → CHECKED. Baroni Eq. (82) writes e^{−iq·R} with its own R convention; equivalent → CHECKED. ∂V_ext = −Σe^{iQ·R}∂_αv, and the electronic force-constant expression (from eq:5.4-hess with u_i = (κα,−Q)) → CHECKED.
- eq:5.4-lin (Baroni (25)), the occupied–occupied cancellation in δn, P^c(H − ε_v)P^c → −1, the shift a_sh > bandwidth → CHECKED.
- keyresult eq:5.4-sth (Baroni (31), Giustino (48)) → CHECKED. eq:5.4-dn factor 4 = spin × time reversal (Baroni (35)) → CHECKED.
- 2n+1 proof (error O(λ^{2n+2})) → CHECKED. Baroni Sect. II.6.1 (= II.F.1) and Eq. (123) → CHECKED in the source.
- Interpolation: N_Q⁻³Σ_Q e^{iQ·(R′−R)} = Σ_Tδ → aliased constants → CHECKED. Baroni II.4.3 (= II.D.3) and V.1.1 (= V.A.1) on the ⟨110⟩ chains → CHECKED in the source.
- fig5_3_data.npz numbers: TA_X 17.063 meV on 2³ and 6³ (identical); 2³ off-grid max error 3.97 meV (25 %); 3³: TA_X 14.75 (−13.6 %) and off-grid 1.15 meV; 6³ off-grid 0.30 meV (1.46 %); blocks 23.26/8.01/0.585 (3.840 Å)/0.211 (5.918 Å)/0.117 (7.681 Å = 3.27 bonds); 0.117/8.01 = 1.5 % → CHECKED. The third neighbor (4.50 Å) is 0.085 < 0.1 → CHECKED.
- ASR: ω₀ = 0.6747 meV = 0.163 THz; z = 0.02: 1.067 against 0.828 meV (+29 %); z = 0.1: +1.06 %; √(ω₀² + c²Q²) reproduces it; slopes 5.44/8.34 km/s → CHECKED.

## 5.5 (s5-5.tex) and D.14
- eq:5.5-U ↔ eq:D.14-U (Heaviside–Lorentz, D = ℰ + P, −(Ω/2)ℰ(ε∞ − 1)ℰ); eq:5.5-FP; eq:5.5-Z (Maxwell relation, index order) → CHECKED. Baroni (89)–(91), (98): Gaussian units, transposed Z* → CHECKED in the source.
- eq:5.5-neutral; Si Z* = 0 from bond-center inversion plus neutrality → CHECKED.
- GaAs convergence (epsZ.json): Z_Ga + Z_As = −0.262 (8³), −0.0443, −0.0106, −0.0031 (12³, 16³, 20³); Z = 2.094 (28³); ε∞ 26.0/16.8/14.7/14.1/13.8/13.70; last step −0.81 %; 13.70/10.88 = +25.9 %; KS gap 0.573 eV → CHECKED. "12 % of either": 11–12.4 %, acceptable. The "(tab:E-functionals)" pointer supports only the measured 1.52 eV; that table has no PBE gap column → GAP (cosmetic).
- keyresult eq:5.5-na from Q̂·D = 0 (the sign and the Z·Q̂ index placement) → CHECKED. It equals D.14-na/√(MM′) and is consistent with Gonze–Lee.
- eq:5.5-w, transverse/longitudinal fields, eq:5.5-LOTO = D.14-LOTO → CHECKED. Estimate: e²Z²/(Ωεμ) = 1.70e-4 eV² ("~2e-4") against ω_T² = 1.13e-3 → CHECKED.
- Fig. 5.4 ¶ (gaas_cache): TO 34.222, LO 36.342 meV (+1.79 %, split 2.12, −22 %); with the measured ε∞: LO 36.872, split 2.650 (−2.9 %); LA_X 27.650; optical minimum on the path 27.831 (gap 0.18 meV); PBE a 5.746 Å (Table E-functionals) → CHECKED.
- Polariton ¶ and D.14: √12.9×0.03 eV = 0.108 eV; 2π/a = 2.19 keV; ratio 4.9e-5 → CHECKED.
- eq:5.5-eps, eq:5.5-LST; poles and zeros → CHECKED. eq:D.14-LSTgen: the interlacing argument → CHECKED. An independent random 4-atom scalar model (ASR, neutral Z) reproduces the product to 1e-15 → CHECKED.
- WE 5.7 (LST): 8.13/8.79 THz = 33.62/36.35 meV (Dehghani Table I → CHECKED in the source); ε 12.9/10.88 (Knapen → CHECKED in the source); 1.1857/1.1690 (1.43 %); ω_L pred 36.61 (+0.26 meV, 0.7 %); split 2.99 (+9.5 %); Δω²/ω_T² = 0.169; Ω = 44.80 Å³ = 5.831e-9 eV⁻³; μ = 36.115 u = 33.64 GeV; e² = 0.0917; Δω² = 1.910e-4 eV²; Z* = 2.108 ("2.11"); static route 2.210 (+4.8 %); 2.094 is 0.68 % low → CHECKED. Griffin: dielectric constants change by "percent-level or less" → CHECKED in the source.
- eq:5.5-HE: Σ_R e^{iQ·R} = Nδ_{Q0}; z_ν; acoustic z ∝ ΣZ* = 0; optical z = Z*ê/√μ_red → CHECKED.
- D.14 Fröhlich: the field of the wave, ∇V^L = eℰ, V^L, eq:D.14-gL (dimension eV), the two-atom sum Z*Q/√μ_red, and the reduction to eq:D.14-frohlich via ω_L² − ω_T² = ω_L²(1 − ε∞/ε₀) → CHECKED. Verdi Eqs. (1) and (4), with e²/(4πε₀)·4π → e² and the G = 0 term → CHECKED in the source.

## 5.6 (s5-6.tex) and D.15
- D.15 proof: [A,d] = −η₂; d e^{θA} = e^{θA}(d + θη₂); d e^{−βH} = e^{−βω}e^{−βH}d; ⟨d e^{θA}⟩ = θη₂(n+1)F; ⟨d†e^{θA}⟩ = θη₁nF; F′ = θ⟨A²⟩F → CHECKED. The multi-mode factorization and the Wick count → CHECKED.
- eq:D.15-B/eq:5.3-B, eq:D.15-W, eq:5.6-W, eq:5.6-C = D.15-C, eq:5.6-gen = D.15-gen (with t = 0 consistency) → CHECKED. Im 𝒞 temperature-independent → CHECKED.
- Debye T = 0: 2W = 3q²/4Mω_D = (3/2)E_R/ω_D → CHECKED. D.15 high-T expansion → CHECKED (sympy). Bracket at T = ω_D: 4.110 → CHECKED.
- Counting: q·𝒞·q = (q²/3)∫(g/n_at)…; P₁ at ω < 0 via n_B(−x) + 1 = −n_B(x); eq:5.6-multi; eq:5.6-poisson → CHECKED. At T = 0, E_R/2W = 1/(2M⟨u_x²⟩) = ⟨ω⁻¹⟩⁻¹ → CHECKED.
- eq:5.6-sum: [p²/2M, e^{iq·X}] = O(q·p/M + q²/2M); double commutator q²/M; the slope of 𝒞 at t = 0 is −i/2M by completeness → CHECKED.
- (111) reflection: |G| = 3.954 keV; 1 − e^{−q²⟨u_x²⟩} = 2.36 % → CHECKED.
- WE 5.8 (DW): 1 Å² = 2.5682e-7 eV⁻². 10 keV: E_R 1.911 meV; 2W 0.0629/0.1638/0.1526; weights 0.939/0.059/0.0019. 50 keV: E_R 47.78 meV; 2W 1.573; weights 0.207/0.326/0.257/0.135/0.053; ≥2 phonons 0.467; 30.37 meV; 4.096/3.814; e^{−4.10} = 0.0166. Crossover 39.9 and 25.6 keV; 56 keV (C.6) = 55.9; Debye 1.289/2.643 (−18/−35 %), e^{−2W} 0.276/0.071, ratio 4.3, q within 10.5 % → CHECKED.
- Displaced oscillator: 𝒟 shift Δx = 2ℓ₀α; H_e = E_ZPL + 𝒟H_g𝒟†; eq:5.6-FC; S = MωΔx²/2 = ωΔQ²/2; relaxation Sω; Stokes 2Sω → CHECKED.
- A(E) time form, ⟨A²⟩ = −S(2n+1), ⟨AB⟩, eq:5.6-Gt → CHECKED. Bessel expansion, eq:5.6-bessel (numerical identity to 1e-15), T → 0 limit → Poisson, w₋ₚ/wₚ = e^{−pβω}, mean S → CHECKED.
- Fig. 5.5 caption: n_B = 0.5 ⇒ T = ω/ln 3 = 0.910ω; ZPL 0.607/0.135/0.0067 → CHECKED.
- WE 5.9: Δx = 0.1358 Å (5.77 % of the bond); 128/256 meV; overlap e^{−Δx²/8ℓ²} and |⟨1_e|0_g⟩|² = Se^{−S} (sympy); Poisson S = 2 row; n_B = 0.0914; w₋₁ = 0.0208; w₁ = 0.2486; ratio 0.0838 → CHECKED. Alkauskas Sect. 2.2 → CHECKED in the source.
- Notation clash inside 5.6 → GAP: p_n is the Poisson weight in eq:5.6-poisson and then "p_n are the Gibbs weights of the ground-state oscillator" in A(E). Rename the Gibbs weights (e.g. P^G_n).

## 5.7 (s5-7.tex)
- eq:5.7-expand, eq:5.7-asr (n − 1 derivatives of the total-force identity) → CHECKED.
- eq:5.7-H3/eq:5.7-V3: N^{−3/2}·N = N^{−1/2}; V⁽³⁾ has dimension Φ⁽³⁾(Mω)^{−3/2} = eV; V(−1,−2,−3) = V* → CHECKED. It agrees with Paulatto Eqs. (4)–(5) → CHECKED in the source.
- Decay matrix element (3! cancels), golden rule ½Σ, the occupation identities n(1+n₁+n₂) − n₁n₂ → (1+n₁+n₂)δn and n n₁(1+n₂) − (n+1)(n₁+1)n₂ → (n₁ − n₂)δn, and the prefactor π/N → eq:5.7-gamma → CHECKED. It matches Paulatto Eq. (6) term by term. Wording in the keyresult → GAP: with Q₂ = −Q − Q₁, the vertex V(Qν,Q₁ν₁,Q₂ν₂) absorbs Q₁ (b_{Q₁} ∈ B_{Q₁}) and creates −Q₂. The merging term is therefore "with Q₁ν₁ into −Q₂ν₂", not "with −Q₁ν₁". Harmless, since the sum is over all Q₁.
- eq:5.7-klemens → CHECKED. Numbers: 1.45 cm⁻¹ = 0.1798 meV; γ/ω = 2.80e-3; 3.66 ps = 56.7 periods ("57"; intro "some sixty"); n_B(ω/2) = 0.408 (300 K), 0.0080 (77 K) → 1.016; ω/2T = 3.72e4 (10 mK); 2.63 cm⁻¹; 1.45×2.01 = 2.91 ("2.92"); 743.8 K ("≈ 740 K"); TA top 26.39 meV (path) < 31.84 → CHECKED. Pair fractions: an independent 48³ check with si_ifc gives LA+TA 90.5 %, LA+LA 5.3 %, O+TA 4.2 %, TA+TA 0, and the 300 K factor 2.011, against 89/7/4 % and 2.01 on the 80³ grid. CHECKED within grid convergence; the LA+LA share is the grid-sensitive one. Debernardi Table 1 (1.43, 1.45, 5.7/94.3 %, spread 1.24–2.1) → CHECKED in the source.
- eq:5.7-eta, its estimate (η ~ κ), eq:5.7-order (second-order cubic, first-order quartic and the golden-rule width all η²ω) → CHECKED. Si: η = 0.0488; 3Φ₂/|Φ₃| = 0.983 Å (42 % of the bond); η² = 2.38e-3; γ/ω = 2.80e-3 = 1.18η² → CHECKED. "quartic-to-harmonic ratio Φ⁽⁴⁾ℓ²/12Φ⁽²⁾ = 1.3e-3" and "quartic one is about 90 eV Å⁻⁴ (we:5-frozen)" → WRONG (follows item 1). With Φ⁽⁴⁾ ≈ 40 eV Å⁻⁴ the ratio is 0.6e-3 (0.25η²). The conclusion "coefficients of order one" survives. H: κ = 0.153 → CHECKED. ℓ ∝ M^{−1/4} → CHECKED.
- eq:5.7-strain → CHECKED.
- SCHA variation (F_trial + ⟨E − V⟩; the ½⟨δXδX⟩δΦ terms cancel; Gaussian/Price identity), eq:5.7-scha → CHECKED. Errea Eqs. (21)–(22) are force averages → CHECKED in the source. TDEP = average curvature for a Gaussian sample (Stein) → CHECKED.
- Summary: the 5.5 and 5.6 paragraphs (36.4/33.6, 1.4 %, Z* = 2.11, 40 keV) agree with the final sections → CHECKED. The 5.2 paragraph says "near 18 meV" (see 5.2).

## D.13
- D.13-coupled/N, the N₀₀ formula, D.13-HF, D.13-dcoup, D.13-expand and the first-order equivalence of the expansions → CHECKED.
- After eq:D.13-scales: "The zero-point amplitude is the fraction κ_BO of a bond length" → WRONG. By eq:D.13-scales it is the fraction κ_BO of the Bohr radius a₀. WE 5.1 shows that the bond-length ratio is 0.021, a third of κ. Correction: "of the Bohr radius".
- Counting ¶ (κ³ cubic; κ⁴ quartic and second-order cubic; derivative coupling κ³; scalar κ⁴; N₀₀ curvature κ⁴ → levels κ⁶; second-order derivative κ⁶) → CHECKED. eq:D.13-mixing: same as 5.1 → CHECKED. Here ℓ² = 1/(Mω) (order of magnitude).
- Solvable model: E₀(X), ω_BO, N₀₀ = m_eω_e/4M (⟨p²⟩ = m_eω_e/2), the determinant, and eq:D.13-model (ω² = (K_N/M)[1 − ε + (1 − K_N/k_e)ε²], sympy) → CHECKED. Numbers for K_N = k_e/2: relative deviations 5.07e-5, 5.01e-7, 5.00e-9. The first is printed as "5.0e-5" → GAP (rounding: 5.1e-5, the O(ε³) term). Also "relative correction to the vibrational frequency is of order m_e/M": order only; ω shifts by m_e/2M (item 5).
- ¶1: 26.06 GeV/m_e = 5.10e4 → CHECKED.

## C.18
- Strain, w_el, Voigt factors, Hooke, eq:C.18-eom → CHECKED. B = (C₁₁ + 2C₁₂)/3 = 97.8 GPa → CHECKED. Isotropic B = C₁₁ − 4C₄₄/3 → CHECKED. 2C₄₄/(C₁₁ − C₁₂) = 1.563 → CHECKED. Martinez Table I (165.6/63.9/79.5, 2.33, λ = 52.4, µ = 68.0) → CHECKED in the source.
- "The quadratic form (C.18-energy) has three eigenvalues … C₄₄ (three times) for the shears" → GAP (convention). As a form on the Cartesian strain tensor (Frobenius normalization) the shear eigenvalue is 2C₄₄; C₄₄ is the eigenvalue of the Voigt matrix C_IJ. Write "the Voigt matrix C_IJ has eigenvalues …". The Born conditions are unchanged.
- eq:C.18-christoffel, eq:C.18-cubic ([110] and [111] eigenvalues, sympy) → CHECKED. Speeds 8.43/9.13/9.35 and 5.84/5.84/4.67/5.09; isotropic 9.0/5.4 (Lamé) → CHECKED.
- Rayleigh form C₁₁Σ Q̂⁴ + (2C₁₂ + 4C₄₄)s_Q (sympy) and the end values minus B → CHECKED. Bound 6.479 km/s, 23 % below 8.43 → CHECKED.
- Impedance: r, t, flux t₁₂ = 1 − r²; Z_Si = 1.964e7; Al c = 6.289 (100) and 6.488 (111) km/s; Z_Al = 1.698e7; t = 0.9947; Al anisotropy 1.223; arcsin(6.29/8.43) = 48.3° → CHECKED.

## Convention / NOTATION drift
- Factor-2 convention between two "zero-point lengths": ℓ_zp = (M_κω)^{-1/2} (bond coordinate, reduced mass M/2; 5.1, D.13, 5.6 WE, 5.7) and ℓ_Qν = (2M_cellω)^{-1/2} (NOTATION). Both are used correctly; 5.3 explains the factor 2. ℓ_zp (and ℓ₀, α_d of 5.6) have no NOTATION row. Add one (proposed: "ℓ_zp, zero-point length (M_κω)^{-1/2} of the bond coordinate, 5.1").
- D.15 writes ω_D (italic D) throughout, against ω_{\mathrm{D}} in 5.2/5.3/5.6 and the STYLE rule for upright text subscripts. Change to \omega_{\mathrm{D}}.
- Λ^{αβ}, Λ_ν (sound-speed matrix, 5.2) clash with the NOTATION row "Λ, P_Λ, final-state class (8.7)". Rename (e.g. 𝖫 or Λ^ac) or flag.
- w: relative displacement 𝐰 (5.5, D.14) vs w(ξ) (2.1/2.4 row) vs w_p Bessel weights (5.6) vs w_el (C.18). Rename the 5.5 coordinate (e.g. 𝐮_rel) or add rows.
- μ_red: NOTATION first use 11.2; it is used in 5.2 (chain) and 5.5 → move the first use to 5.2.
- Missing rows for symbols used in Chap. 5: Ψ^nuc_i, 𝒩_ji, C^an_κκ′, C₀, 𝐳_ν, T^{αβγ}, D_n(Q), Q_D, a_c, K (chain spring), Φ_opt, Φ⁽³⁾_opt, P_n(ω), p_n, ρ_pair, P̂^c, E_dir (row exists, 3.3) and S_ent. The a_sh/P̂^occ row exists (E.4); move its first use to 5.4.
- Z* index order (force/displacement first), D(Q) with e^{+iQ·R}, e_κν(−Q) = e*: consistent with A.6 and E.4 throughout. Transposed or sign-flipped sources (Baroni, Verdi) are flagged in the text. No sign or π drift found.
