# Ch6 derivation check (isolated verifier, long-form-writing SKILL.md §5)

Scope: tex/ch06/ch06.tex, s6-1 … s6-5, tex/appD/D-16 … D-18. Algebra redone in sympy (scratch `sym6.py`), numbers recomputed in
Python (`num6.py`) from the stated inputs. Cached DFPT data came from figscripts/ch05/fig5_2_data.npz. The brief names
figscripts/ch06 for the npz and gaas_cache, but those files are in figscripts/**ch05**. fig6_6.py (Al model) was re-run with its output
redirected to scratch, and figscripts/appD/check_D_c.py d16–d18 were re-run. Both are light. QE was not run. Sources fetched with lit.py and
checked against the text: Giustino RMP 2017 (1603.06965), Verdi–Giustino 2015, Poncé 2015, Li–Graziosi–Neophytou 2021, Noffsinger 2012,
Zacharias–Giustino 2020, Calandra 2010, Savrasov 1996, Ibe 2018, Miglio 2020, EPW 2016. PDFs deleted afterwards.
Paywalled sources were not checked: Macfarlane 1958, Alex 1996, Cardona 2005, Lockwood 2005, Strauch 1990, Vurgaftman 2001, Hall 1954, Born–Huang, Migdal.

Legend: CHECKED = redone and agrees; WRONG = error, with the correction; GAP = claim not supported as stated, or imprecise.
Known items (editor-notes.md) are listed at the end and are not repeated as findings.

## Findings that need action (summary)

1. **s6-4 l.98 (empty-core model), WRONG, factor 4π convention drift.** The text writes "a Coulomb potential −3e²/r" and
   `w(q) = −4π·3e² cos(q r_c)/[Ω q² ε_Lin]`. Both are Gaussian-unit forms. In the book's Heaviside–Lorentz units (e² = 4πα; 6.1 writes
   −Z e²/(4π r), and 6.2 writes v_κ(k) → −Z e²/k²) they read **−3e²/(4π r)** and **w(q) = −3e² cos(q r_c)/[Ω q² ε_Lin(q,0)]**.
   fig6_6.py works in Hartree atomic units (e² = 1, Gaussian), so every number (λ = 0.436, ω_log = 250 K) is unaffected.
   Fix the text only.
2. **s6-2 l.17, WRONG citation.** "…the dynamically screened vertex of Bardeen and Pines~\cite[Eq.~(5)]{giustino2017electron}". In
   Giustino, Eqs. (3)–(5) are Bardeen's (1937) static Lindhard screening, V0 → V_κ(q)/ε(q). Bardeen–Pines (1955) appears only in
   prose there, for screened exchange. Either cite Giustino Eqs. (3)–(5) as Bardeen's static screening and keep "dynamic" uncited, or
   drop the equation number and attribute to Bardeen and Pines through the review's Sect. II.A text.
3. **s6-4 l.61 and D-17 l.46, WRONG wording.** Both say that Giustino "writes the same rate as an inverse lifetime with the spin sum implicit
   [Eq. (146)]". Giustino Eq. (146) is 1/τ = (2π/ħ) Σ_mn **2** ∫dk/Ω_BZ |g|²(f−f)δ(…), so the spin factor 2 is **explicit**, and 1/τ equals the
   book's full width γ^ep (4π/N Σ) exactly. Change to "with the spin factor written explicitly".
4. **D-18 l.49, WRONG attribution.** The text says Eq. (D.18-eps2PA) "with V = NΩ and (D.18-alpha) … is Ref. [Giustino Eq. (200)], the form used in
   [noffsinger2012], whose prefactor contains the spin sum implicitly". Noffsinger Eq. (1) has an explicit factor 2 (prefactor
   2·4π²e²/(ω c n_r V_cell N_k N_q)), as s6-5 l.64 correctly says. Giustino Eq. (200) has πe²/(ε0 c Ω ω n_r) with no 2, so it
   matches the book only with the spin implicit. Correct to: "…Ref. [Giustino Eq. (200)], whose prefactor leaves the spin sum implicit;
   Ref. [noffsinger] writes it explicitly." s6-5 l.64 ("it is also Ref. [Eq. (200)]") should add "with the spin sum implicit".
5. **s6-3 l.127 (WE 6.3), WRONG as displayed.** "−(\SI{353}{K}/2)×\SI{0.33}{meV/K} = −\SI{59}{meV}": the displayed product is −58.2.
   The 59 comes from the unrounded slope 0.332 (→ −58.6). Write "−58 meV", or quote the slope as 0.332. Its use as a bracket
   (51.8 … 58–59 around 56.2) stands.
6. **s6-2 l.77, GAP (cited value is right but described wrongly).** "Li et al. combine its elements in quadrature into a single value,
   10.45 eV/Å [Eq. (12)]". Li's Eq. (12) quadrature gives 10.65 eV/Å (Γ→Γ+q) and 10.84 (Γ−q/2→Γ+q/2). 10.45 is the
   **average** of the Eq. (12) value 10.65 and the value 10.26 from maximizing over rotations of the degenerate subspace. Suggest:
   "Li et al. combine its elements into a single value, 10.45 eV/Å, the mean of two such combinations [Eq. (12) and text below]."
7. **s6-2 l.59 and Fig. 6.2 caption, GAP.** "…linear in Q up to about 0.1 Å⁻¹ and bend away beyond it [Fig. 5]". Li's Fig. 5 spans only
   0–0.1 Å⁻¹, so nothing beyond is shown. Their text (near Fig. 4) says that for holes a slope can be taken only below about a tenth of half the
   zone. Reword to "linear over the computed range, up to 0.1 Å⁻¹". The caption's solid/dotted split can stay as a modelling choice.
8. **s6-3 l.105, GAP (attribution).** "…fall short of it by about 20 %, which is attributed to the small Kohn–Sham gap overscreening the
   vertex [Zacharias Sect. VII B]". Zacharias invoke LDA overscreening to explain why GW gives 66 meV against their 57. They do not
   compare with 71–73 meV or quote 20 %. The arithmetic is right (56.2/72 → 22 % short). Suggest "…which is consistent with the
   overscreening of the vertex by the small LDA gap: a GW-based calculation gives 66 meV [Zacharias Sect. VII B]".
   For awareness only: Zacharias (same paragraph) state that non-adiabatic AHC corrections *increase* the Si ZPR by 8 meV, the opposite
   sign to Poncé Table VI (−64.3 adiabatic, −56.2 non-adiabatic). The book follows Poncé's table correctly. Do not import Zacharias' sentence.
9. **s6-4 WE 6.4, GAP (minor).** "…0.396, 9 % below the 0.436 of the full model **and of the measured 0.42–0.43**": the gap is 9 % against 0.436
   but only 6–8 % against 0.42–0.43. Write "9 % below the full model's 0.436 and 6–8 % below the measured 0.42–0.43".
10. **NOTATION drift, bare μ (entry 31: reduced masses carry subscripts, and bare μ is not used).** s6-1 l.119 uses bare μ for the electron–proton reduced
    mass, with a_μ, and l.137 (WE 6.1) uses bare μ again for the χ–H reduced mass. That gives two meanings in one section. Use μ_ep (and a_ep or
    a_{μ_ep}) and μ_χH (as 1.3 writes μ_χN).
11. **NOTATION drift, bare W in D-17 l.78–80, 91.** The band-width cutoff W (∫_{−W}^{W}dε, "W = 100 ω′") clashes with entry 11 (W
    is reserved for W_κ and W^scr). Rename it, e.g. E_cut or W_band. This is separate from the known W_ab item in D.18.

## s6-1 Non-adiabatic coupling

- l.3 numbers: CHECKED. q = 5.10 MeV and v_N = q/M = 1.96×10⁻⁴ (58.7 km/s) use the ²⁸Si mass 26.06 GeV, as in 1.3. Natural Si would give
  1.95×10⁻⁴. α/v_N = 37.2; m_e v_N = 100 eV; α m_e = 3.73 keV; (v_N/α)² = 7.2×10⁻⁴.
- Eq. (6.1-d) and the antisymmetry: CHECKED. For real states d_ji = −d_ij* = −d_ij. The ∇² identity with completeness and the antisymmetry step are redone.
- Eq. (6.1-Pd): CHECKED (sympy). (∇+d)²f = f″ + d′f + 2df′ + d²f, which with −1/2M reproduces (5.1-N) exactly. The off-diagonal first-order term is
  −(i/M) d·p.
- Eq. (6.1-tdep): CHECKED. Projection of iΣ(ċ_iΨ_i + c_i u̇·∇Ψ_i) = ΣE_i c_iΨ_i. d_ji = F_ji/(E_i − E_j) agrees with the off-diagonal
  Hellmann–Feynman relation. "Force" means the force on the electrons (∇_R V = −∇_r V), as in 5.1.
- Scalar/derivative ratio |d|/(Mv), ℓ_zp/a₀ ~ κ_BO, 1/(q a₀): CHECKED. v ~ α κ_BO³: CHECKED. κ_BO³ = (m_e/M_Si)^{3/4} = 2.94×10⁻⁴ → "2.9×10⁻⁴" ✓.
  v_N/(ακ³) = 91.4 ✓. Second-order shift α²m κ⁶, relative κ⁴ = m_e/M ✓. ω_opt/E_g = 64.1/1170 = 0.055 ✓.
- l.40 "κ_BO² … about 10⁻²": the actual values are 4.4×10⁻³ (Si) and 3.4×10⁻³ (Al ω_max/E_F). This is a known item (editor: "10⁻³ to 10⁻²"); apply it here as well as in 6.3.
- Interaction-picture amplitude and integration by parts, Eq. (6.1-accel): CHECKED. Eq. (6.1-sudden1) ✓. The first term persists while
  Ẋ = v_N; the text's reading (dressing of the moving atom, not an excitation) is consistent.
- Eq. (6.1-model): CHECKED. ∫sech²s e^{iks}ds = πk/sinh(πk/2) (numerical check in sympy), Ẍ = (v_N/2τ)sech²(t/τ), α_d = −i(m/2ω)^{1/2}∫Ẍe^{iωt}
  (forced oscillator), so |α_d|² = (m v_N²/2ω)[y/sinh y]² with y = πωτ/2. Bracket 0.466 (ωτ=1) → "0.47" ✓, 0.0740 (ωτ=2) ✓. Asymptote
  π²(ωτ)²e^{−πωτ} ✓. Dimensions: m v²/ω is dimensionless ✓. Fig. 6.1 shaded region ωτ < 0.3: bracket 0.93 there, within 10 % ✓.
- l.107 factor [1 − (ω_ph/ω_e)²]^{−2}: CHECKED by derivation (a kick plus harmonic return gives ∫Ẍe^{iωt} = v_N/(1 − r²)). Its value is 1.006 ✓. Kick duration
  R/v_max = 4.4×10⁻²¹ s ✓ (radius, not diameter, and used consistently with the hydrogen case). 1/E_g = 0.56 fs ✓.
- Eq. (6.1-boost) and the dipole equivalence: CHECKED. d_j0 = m_e ΔE ⟨j|Σr|0⟩ from P = i m[H,Σr]. The boost sign agrees with Ibe Eq. (1) e^{−i m_e v·Σx}; P = |⟨Φ*|Φ′⟩|²
  is Ibe Eq. (2) ✓, and q_e = m_e v is Ibe Eqs. (55)–(58) ✓.
- Hydrogen separation, argument (m_e q/M_H)a_μ = q/(α m_p): CHECKED (the reduced mass cancels). Eq. (6.1-P0) and its expansion 1 − v²/α²: CHECKED.
- WE 6.1, all numbers CHECKED: M_H = 938.783; μ = 484.21 MeV; q = 2.566 MeV; recoil 3.508 keV; v_N = 2.735×10⁻³ (820 km/s); v_N/α = 0.3748,
  x² = 0.1405; F = 0.9333; P₀ = 0.8710; 1 − P₀ = 0.1290; small-v form 9 % high (1.089) ✓; P₀ = ½ at x = 0.870, v_N = 6.35×10⁻³,
  q = 5.96 MeV, recoil 18.9 keV ✓; ΔE = 10.20 eV, 1/ΔE = 0.0645 fs, τ = 1.06×10⁻²¹ s, ΔEτ = 1.6×10⁻⁵ ✓; Si 1 − P₀ = 7.2×10⁻⁴ ✓.
- Eq. (6.1-Hep) and the displacement-wave Bloch property: CHECKED (relabeling; the prefactor (2NMω)^{−1/2} matches A.6). The density operator \op{n} is a known item.

## s6-2 Electron–phonon matrix elements

- Eq. (6.2-screen): CHECKED. (1 − fR⁰)⁻¹ = 1 + fR⁰(1 − fR⁰)⁻¹ = 1 + fR. Thomas–Fermi: Z e²Q/(Q² + k_TF²) ✓.
- Eq. (6.2-g): CHECKED. (2M_κω)^{−1/2} = ℓ_Qν (M_cell/M_κ)^{1/2} with NOTATION ℓ = (2M_cellω)^{−1/2}. EPW Eq. (2) and Li Eq. (2), g = √(ħ/2m₀ω) M with m₀ the cell mass,
  are the same normalization, so Li's eV/Å constants transfer without conversion ✓.
- Eq. (6.2-asr): CHECKED. ⟨m|−i[p,H]|n⟩ = −i(ε_n − ε_m)p_mn, and T_d derivative = −i[p,V] = −∂V ✓. g_nn ∝ Qℓ ∝ Q^{1/2} ✓.
- Strain and Eq. (6.2-D): CHECKED (∂_αu_β = iQ_α ê_β ℓ/√N e^{iQr}B; symmetric D). |g|² = E₁²Q/(2M_cell c) ✓. E₁ = Ω∂ε/∂Ω is Giustino Eq. (6) ✓.
- Herring–Vogt angular forms: CHECKED against Li Eqs. (13), (14). Li values Ξ_d = 1.01 and Ξ_u = 8.84 eV ✓ (text after Eq. (14); Table II).
- Numbers l.3 and l.59: CHECKED with the DFPT c_LA = 8.34 km/s: ω = 0.549 meV, ℓ = 0.2604 Å, |g| = 9.85×0.01×0.260 = 25.6 meV → "26" ✓; across
  the axis 2.63 meV ✓. Scaling √10 and 10 ✓.
- Piezoelectric vertex: CHECKED. ε∞Q̂·E + Q̂·P = 0, V = eQ̂·E/(iQ) for charge −e, P_α = i e_{αβγ}Q_β ê_γ ℓ/√N, giving −(e/ε∞)ℓ Q̂·e^pz:Q̂ê. Dimensions:
  e·e^pz·ℓ = energy ✓.
- Eq. (6.2-d) and l.77: ℓ₀ = 0.02409 Å at 64.1 meV; |g| = 0.252 eV ✓; "ten times" (9.7) ✓. On "in quadrature", see finding 6.
- g^L (D.14-gL) against Verdi Eq. (4): CHECKED (e²_SI/ε₀ → e², single G term, force-first index order).
- Eq. (6.2-frohlich): CHECKED (sympy). Two-atom LO with e_κ = ±(μ/M_κ)^{1/2}Q̂ gives Σ = ZQ/(2μω_L)^{1/2}. With ω_L² − ω_T² = e²Z²/(Ωε∞μ) and
  LST, C_F² = (e²ω_L/2Ω)(1/ε∞ − 1/ε₀). Against Verdi Eq. (1) (HL map, √N moved out) ✓. C_F in eV² ✓ (NOTATION).
- ΔE integral and Eq. (6.2-alphaF): CHECKED (sympy: ∫dQ/(a + bQ²) = π/(2√ab); α_F = α(1/ε∞ − 1/ε₀)(m*/2ω_L)^{1/2}; ΔE = −α_Fω_L).
- WE 6.2, all CHECKED: Ω = 44.80 Å³ = 5.831×10⁻⁹ eV⁻³; 0.09191 − 0.07752 = 0.01439; e² = 0.09170; C_F² = 4.114×10³ eV⁴; C_F = 64.14 eV²;
  |g^L|(0.01 Å⁻¹) = 3.25 eV and (0.1) 0.325 ✓; √ = 686.2; α_F = 0.0721; shift 2.62 meV; length 39.55 Å (7.0 a); Q = 0.0253 Å⁻¹
  (zone/44, "about a fortieth" acceptable); |g^L| = 1.286 eV ✓. LST route: 0.013287 (−7.7 % → "8 %"), α_F = 0.0665 → "0.067" ✓; LST residual
  1.4 % ✓; amplification 5.5× ("fivefold") ✓.
- Fröhlich adiabatic integral (6.3 l.56): CHECKED (−Ω m* C_F²/π² ∫dQ/Q²).
- Eq. (6.2-gW): CHECKED as Giustino Eq. (178) with Bloch sums (176). l.17 Bardeen–Pines citation: see finding 2.
- Li Eq. (15) note (no change needed): Li's isotropic constants (6.27 and 3.13 eV) use plain θ averages (Ξ_d² + Ξ_dΞ_u + 3Ξ_u²/8 and Ξ_u²/8). The
  book's 6.3 averages (2/3, 1/5, 2/15) are the correct solid-angle averages (sympy). Do not align them with Li.

## s6-3 Electron self-energy from phonons

- Eq. (6.3-HAH)/(D.16-gAH): CHECKED. The 1/N combines the two 1/√N, and the ½ is from the Taylor term. Giustino Eqs. (39) and (40) ✓.
- Eq. (6.3-FM)/(D.16-FM): CHECKED, residue by residue. n_B(iω_F − ξ) = −(1 − n_F) and n_B(−ω₀) = −(1 + n_B) give the weights (n + 1 − f) and (n + f), with
  T Σ = −Σ Res and the overall sign +. check_D_c.py d16 reproduces the direct Matsubara sum to 6 digits ✓. Giustino Eqs. (157) and (158) ✓.
- ⟨B_QB_{−Q}⟩ = 2n + 1 and [B_Q, B_{−Q}] = 0: CHECKED. Eq. (6.3-AH) and Giustino Eqs. (160) and (161) ✓.
- Eq. (6.3-adiabatic): CHECKED ((n+1−f) + (n+f) = 2n+1). Giustino Eq. (167) ✓. The frozen-phonon route (D.16-frozen) with ⟨u_Q u_{−Q}⟩ weight (2n+1)/(2N√(MM′)ω) ✓.
- −9.14 versus −8.73 meV: CHECKED against 4.8 (−9.14 × z_qp 0.952 = −8.70).
- Translational cancellation: CHECKED. The g^AH prefactor is ½ℓ²ê ê (the text's "ℓ²ê ê" refers to the fraction without the ½, and the ½ reappears in the next line).
  −[p,[p,H]] from the twice-differentiated T_dVT_d†. ⟨n|[p,[p,H]]|n⟩ = 2Σ(ε_n − ε_m)|p_mn|². Fan + AH = 0 is checked numerically on random Hermitian
  matrices (|residual| < 10⁻¹⁵).
- Sum rules (D.16-sr1/sr2), (D.16-ria), (D.16-AHria) = (6.3-ria): CHECKED. The Hessian of ε from (D.16-frozen) is summed over a; the rigid-ion
  on-site element and N⁻¹ per-cell matrix element give the result, and symmetrization keeps Re(·) for Hermitian ∂V and symmetric real B. Giustino Eqs. (193)–(198) ✓.
  check_D_c d16 PASS: Hessian 4.0×10⁻⁶ ✓; ria 4×10⁻⁸ (text "10⁻⁷", conservative) ✓; non-rigid failure 0.66 ✓. Poncé: large non-rigid corrections in molecules ✓.
- Eq. (6.3-smear): CHECKED (⟨e^{−iG·u}⟩ = e^{−G·B·G/2}; ½B∂∂v ↔ −W v(G)). "Fuzziness" below Giustino Eq. (154) ✓.
- ZPR values: CHECKED against Poncé Table VI and text: −64.3 adiabatic, −56.2 non-adiabatic (Γ−0.848X), experimental −62 (mass derivative) and −64
  (extrapolation). Zacharias Sect. VII B: VBM +35, CBM −22, ZPR 57 meV, 8×8×8 supercell = 1024 atoms ✓. Miglio Table S2: Si ZPLR +9 meV ✓.
  −71 to −73 ✓. On the 20 % attribution, see finding 8.
- Eq. (6.3-einstein) and its high-T limit (slope 2Δ(0)/ω, zero intercept), isotope relation ZPR = −2M∂E_g/∂M: CHECKED.
- WE 6.3, CHECKED from fig5_2_data.npz: ω_Ein = 30.42 meV = 353 K; ⟨u²⟩(300)/⟨u²⟩(0) = 2.661; rms 0.0495 Å ("0.05", l.3) ✓.
  ω/2T = 0.588 and coth = 1.892, so the text's 1.891 is a rounding difference only; −50.15 → "−50.1" ✓. Varshni: E_g(300) = 1.12302 eV, fall 46.18 meV ✓; −57.4 (adiabatic) → "−57.3"
  (rounding) ✓; slopes 0.259 and 0.332 meV/K ✓; model 0.3186 ✓; 93.35 meV ✓; −46.2/0.891 = −51.8 ✓; −59: see finding 5. 1.2254 eV ✓; isotope +1.79 meV ✓;
  2n_B(1 K) = 1.2×10⁻¹⁵³ ✓.
- Fig. 6.4 text: max |model − measured| = 5.0 meV (at 390 K) over 0–600 K ✓. Below 150 K the model lies 0–3 meV above, so it falls too slowly ✓.
- Eq. (6.3-ImFM) and Γ = −2z ImΣ: CHECKED. Eq. (6.3-cherenkov): CHECKED (sympy; cosθ root, m*/(kQ) Jacobian, Q_max = 2(k − m*c)).
  Dimensions: Ω Ξ² m Q³/(M c k) is in eV ✓.
- Lifetime numbers: CHECKED. m*_d = (0.916·0.191²)^{1/3} = 0.3221; Ξ_L = 4.754 and Ξ_T = 3.228 eV; thresholds 0.0651 and 0.0312 meV; at 10 meV,
  7.15 + 5.15 = 12.30 μeV, 53.5 ps; at 1 meV 0.91 ns; at 30 meV 16.2 ps ✓. Threshold kinetic energies below 1 K ✓.
- Migdal theorem paragraphs: the "10⁻²" is a known item. α_F = 0.072 ✓. The "order α_F" vertex estimate is a known item.

## s6-4 Phonon self-energy and the Eliashberg function

- Bubble sign (D-17): CHECKED. The sign is (−1)(−1)²(−1) = +1, the Lindhard frequency sum gives (f_n − f_m)/(iω + ε_n − ε_m), the spin gives 2, and Π = 2ωΠ^b gives the factor 4ω.
  The Dyson form D = 2ω/(ω² − ω_Q² − Π) ✓. Static Π < 0 in an insulator ✓. Even in ω: pairs give 2Δ/(ω² − Δ²) ✓. NOTATION ruling (Π in eV², FWHM) ✓.
- Eq. (6.4-pole): CHECKED (Lorentzian 1/(ω − ω̃ + iγ/2), γ = −ImΠ/ω is a FWHM).
- Eq. (6.4-nonad) against Calandra Eqs. (22) and (23) (dynamic minus static) ✓; Giustino Eq. (140) W_e(ω) − W_e(0) ✓; "up to 30 %" is in Calandra (ref. 12 there),
  a known item. Al: v_F = 2.03×10⁶ m/s, Q = 2.2×10⁻³ Å⁻¹ ✓; (64.1/1170)² = 0.0030 ✓; 0.0034 and 0.0015 ✓.
- Eq. (6.4-gamma): CHECKED (−ImΠ/ω with Sokhotski–Plemelj). The comment on Eq. (146): see finding 3. Raman 0.18 meV → 56.7 periods ✓; e^{−E_g/2T} = 3.9×10⁻¹⁰
  (with 1.12 eV) ✓.
- Eq. (6.4-allen): CHECKED (f(ε) − f(ε+ω) ≈ ωδ(ξ)). Against Giustino Eq. (185), γ/(πω) = 2Σ_mn∫dk/Ω_BZ|g|²δδ: this gives γ_G = 2πω(1/N)Σ, with the spin 2 shown. That is half the book's full
  width 4πω(1/N)Σ, so "Giustino's γ a half width, spin included" holds ✓. Electron-gas check (D.17): angular m/(kQ), radial ∫(f − f)dε = ω, giving m²ω/(4π²Q) ✓. check_D_c d17 PASS (ratio 1.00000) ✓.
- Eqs. (6.4-a2F) and (6.4-lambda): CHECKED (term-by-term comparison; λ_Qν = γ/(2πN_FΩω²)). Giustino Eqs. (205) and (206) ✓. d17: λ from widths = 2∫α²F/ω ✓.
- Eq. (6.4-mass)/(D.17-mass): CHECKED (logarithms; derivative −1/ω′ + 1/(W + ω′) each; finite-W shortfall ω′/(W + ω′) = 0.99 % ✓; d17 0.10166 vs 0.10268 ✓).
- Specific heat: CHECKED. (π²/3)·(5.49/13.6057 eV⁻¹)·k_B²·N_A = 0.951 mJ K⁻² mol⁻¹; ratio 1.430; λ = 0.43 ✓. Savrasov Table II: λ_calc 0.44, λ_tun 0.42, λ_s−h 0.43,
  N(ε_F) 5.49, γ 1.36 ✓. Table III ω_log 270 K ✓. Table I (X_L 9.69, X_T 5.78, L_L 9.69, L_T 4.19 THz) ✓. "Practically identical to the empirical
  rigid-ion pseudopotential result" ✓. Savrasov's ω_max ≈ 470 K (40.5 meV) ✓ "40 meV".
- Eq. (6.4-a2Fgas): CHECKED (Ω m²/(4π²q)·2π²/(m k_F) = Ωm/(2k_F q); |g|² = q²(q̂·e)²w²/(2Mω)). On the w(q) prefactor, see finding 1. Plane-wave matrix element
  (1/Ω) i q v(q) gives w = v(q)/Ω ✓.
- Model numbers re-run (fig6_6.py, output redirected): λ = 0.436; ω_log = 250 K; r_c = 0.564 Å; λ(0.55) = 0.443 and λ(0.59) = 0.459 ✓; fit residuals L_T 1.6 % and
  L_L 8 % ✓; ω_max 40.1 meV ✓; k_F = 1.749 and E_F = 11.65 eV ✓; |G₁₁₁| = 2.687 ✓; peaks 23.38/35.12, split 31.88, 2.236 modes ✓; A_T = 3.128, A_L = 2.258 ✓;
  two-peak λ 0.396, parts 0.306 and 0.130, ω_log 26.7 meV = 310 K ✓; constant-α² 0.500 and 228 K ✓; ⟨γ/ω⟩ = 0.0044, ⟨γ⟩ = 0.122 meV, 36 periods ✓; 70 % ✓;
  "half as strongly" (0.47) ✓. Percentage wording: see finding 9.

## s6-5 Phonon-assisted optical absorption

- Optical vertex: CHECKED. E = −∂_tA; the e^{−iωt} coefficient of sin ωt is i/2 → eE/2ω. α_abs = ωε₂/n_r (ε₂ = 2nκ, intensity e^{−2ωκx}) ✓.
  Optical limit ρ_mn → q·v/(ε_m − ε_n) from v = i[H,r] ✓. Eq. (6.5-eps2dir) agrees with the standard 4π²e_G²/(m²ω²V)·2Σ|ê·p|² ✓.
- Four paths (D-18 items 1–4): CHECKED (operator reorderings, both −1; on-shell denominators map paths 3→2 and 4→1). Eq. (6.5-M) = (D.18-M) ✓. check_D_c d18:
  four-path = exact Fock-space T to 3×10⁻¹⁶; dropping the hole paths changes T by 0.79 and 0.81 ✓. Sign comparison: Noffsinger Eqs. (2) and (3) and Giustino Eq. (200) have both
  denominators negated, with upper sign = emission in each ✓. The constant 100 meV width is "not very sensitive" ✓.
- Eq. (6.5-eps2PA) = (D.18-eps2PA): CHECKED (⟨⟨⟩⟩ = N⁻²Σ; 2πe²/(ω²VN)Σ = g_deg πe²/(ω²Ω)⟨⟨⟩⟩). Against Noffsinger Eq. (1) (e² = 4πe_G²): prefactor 2·4π²e_G²/(ωn_rV_cell) ✓.
  On the spin wording in D-18, see finding 4. 40³ k and q, 14 meV, 4.1×10⁹ pairs, rigid shift 0.15–0.23 eV ✓ (Noffsinger).
- Eq. (6.5-joint): CHECKED (sympy; ∫√ε√(x−ε) = πx²/8; (2m)^{3/2}(2m)^{3/2}/16π⁴·π/8 = (mm)^{3/2}/16π³). Eq. (D.18-HBB) prefactor e²Ω(m m)^{3/2}/(8π²ω²) ✓
  (sympy). A_ν = g_deg e²Ω(m*_d m_h)^{3/2}/(16π²ωn_r)Σ|M|² = e²…/(8π²) ✓. Dimensions: ε₂ is dimensionless, A_ν is in eV⁻¹, α_abs is in eV ✓. m*_d = 0.322 → "0.32" ✓.
- Eq. (6.5-ratio) and slope ratio e^{−ω/2T}: CHECKED.
- l.118–122 conversions: 212 K = 18.27 meV and 670 K = 57.73 meV ✓; 4.49 THz = 18.57 and 13.90 THz = 57.49 meV ✓; agreement 1.6 % and 0.4 % ✓. Macfarlane values
  were not checked (paywalled; the Yu–Cardona assignment is a known item).
- WE 6.5, all CHECKED: thresholds 1.1123, 1.1517, 1.1883, 1.2277; excitonic 1.0976, 1.1370, 1.1736, 1.2130; 2ω = 36.5 and 115.5 meV; n_TA = 0.973 and n_TO = 0.1201;
  √ 0.987, 1.405, 0.347 (text "0.346"; √0.12007 = 0.3465, rounding) and 1.058; ratios 0.702 and 0.327; −2T ln 0.702 = 18.29 (≈ 18.27 within rounding of 0.702) ✓;
  77 K: T = 6.635, n = 0.068 and 1.7×10⁻⁴, ratios 0.252 and 0.0129 ✓; 20 K: 2.5×10⁻⁵ ✓; 10 mK: ω/T = 2.12×10⁴, "e^{−21200}" ✓.
- Fig. 6.8 caption and summary: consistent with Eq. (6.5-edge) ✓.

## Summary section (s6-5 l.158–168)

- CHECKED against the sections, with these exceptions. "Within a few meV up to room temperature" is consistent (≤ 5 meV to 600 K). "0.42 to 0.43 from tunneling and the
  specific heat" ✓. α_F = 0.072 ✓. The re-read of the 6.3 and 6.4 summary paragraphs is a known item.

## Known items (editor-notes.md), not re-reported

\op{n} → \hat{\nd} in 6.1; the ω_e upright/italic clash note; Migdal 1941 has no DOI; Born–Huang App. VIII and the Yu–Cardona Chap. 6 assignment at the audit; Fig. 6.2 caption
saying the curves are limiting forms (present ✓); delivery of the Q→0 cancellation in 6.3 (delivered ✓, Eq. (6.3-cancel)); D.18 fixes (m_e → m*_d, ê → ê_γ,
W_ab clash, "√α straight segments", "machine precision" sentence; D.17 l.91 also says "to machine precision" for the tight-binding λ check, same style issue);
A_ν versus A_TA/A_LA letter repeat; first use of n_r; the λ_ep 0.436 model label; the calandra arXiv number (bib entry still lacks eprint 1007.2098); the original source
of the 30 % figure (Calandra's ref. 12, Lazzeri–Mauri 2006); "10⁻³ to 10⁻²" (also needed at 6.1 l.40 and 6.3 l.177); E.8 ZPR pair; ω_Ein row; A.6 wording; the α_F
vertex-correction estimate; Cardona 2005 and Alex 1996 via secondary sources.
