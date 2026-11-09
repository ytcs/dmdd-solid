# Ch. 14 part 1 derivation check (ch14.tex, s14-1, s14-2, s14-3, D-38)

Reviewer: derivation verifier, isolated (2026-11-06). Algebra in sympy, numerics in numpy, run independently of the figscripts. Cached logs were read only for comparison. No QE runs; tex not edited.
Scripts: /tmp/claude-0/-home-user-breakthrough-maths/30a63adb-c597-5cb8-b46c-4c5645c8b7d4/scratchpad/chk/{sym.py,nio.py,rate.py,edge.py}.
Sources fetched with lit.py into sources/review-ch14/ (1905.13744, 2009.13534, 2508.12153, 2210.13516, cond-mat/0504684, 1402.6575, 2001.10666, 2005.10256, cond-mat/0108424, 1302.4867, 2005.01203). I read each one and deleted my PDFs afterwards. Closed sources I did not open: Anderson 1952, ITC Vol. C, Wortis 1963, Silberglitt–Torrance 1970, Kittel 1948/1958, Colpa 1978, Nakatsuka 1995.

Verdicts: CHECKED = redone and agrees; WRONG = error, with the correction; GAP = step, scope or wording that is missing or too strong.

## A. PRIORITY items

### A1. One-magnon response at full momentum transfer and its rate (14.1, D.38)
- D.38 lattice-sum phases. CHECKED. With r_j = R + δ₀ on B, Σ_B e^{iq·r_j}d†_Bj gives N_s^{1/2}ε_G d†_{B,−q_r}, so A_q = A_{q_r} and B_q = ε_G B_{q_r}. For NiO, δ₀ = a x̂ and 2δ₀ ∈ A (p = (n₁+n₂+n₃)/2 is additive), so ε_G = ±1.
- D.38 S^±(q) in magnon operators, the amplitudes c and ε_G c, and eq:D.38-weight. CHECKED by sympy: (u − εv)² = (A − εB)/√(A² − B²) for ε = ±1.
- D.38 branch polarizations and the cancellation of the off-diagonal elements. CHECKED: the S_xy contributions are +i and −i times (2π/𝓥)|F c|²/4. The sum with 𝓥 = 2N_sΩ and |c|² = 2|S|N_s w gives π|S|F²w/Ω, which is eq:14.1-Safm.
- Limits near Γ and Q_AF (14.1 l.20–25). CHECKED. A_Q = J_AB(0) holds exactly in type II: the parallel NN lie in the (111) plane, so Q·δ = 0. Both closed forms hold. 2|S|J_AB(0) = 12(J₁ + J₂) = 211.68 meV. At 5 meV, w = 0.0236 near Γ and 42.3 near Q_AF. The 0.02 % agreement within 0.01 Å⁻¹ is confirmed (0.015 %).
- eq:14.1-contract, eq:14.1-sigma. CHECKED. 𝔇_ab = |c₄|²δ_ab/4, bracket = |c₄|²/2, ⟨|S_χ·S_e|²⟩ = 3/16.
- Against the source (Trickle 2020 Eq. (11)): CHECKED. σ̄_e = μ²|M_free|²/(16π m_χ²m_e²) with M = 4m_χm_e Ṽ is μ²⟨|Ṽ|²⟩/π. Note that Table I of that paper has no O₄ row; "the definition … for this operator" applies their general definition, which is fine.
- eq:14.1-rate prefactor 2ρσ̄|S|/(3m ρ_T μ²Ω). CHECKED, from π|c₄|²/2 × 16πσ̄/3μ² × 1/4π² (A.8-eta kernel). Dimensions: rate per mass, dimensionless in natural units. CHECKED.
- eq:14.1-inc. CHECKED: ∫du u η(u) = ⟨v⟩/2. ⟨v⟩ = 354.1 km/s (my halo sample: v₀ 238, v_E 250.5, v_esc 544). Ratios 0.96 and 0.989 agree with the log.
- NiO rates (14.1 l.124). My own Monte Carlo integral (separate script: 3000 directions × 400 q, Brown ⟨j₀⟩) gives, per kg·yr at 1e−40 cm²:

  | m_χ | 10 keV | 100 keV | 1 MeV | 3 MeV | 10 MeV |
  |---|---|---|---|---|---|
  | this check | 10.3 | 434 | 2.66e3 | 3.19e3 | 1.52e3 |
  | text | 10 | 430 | 2.6e3 | 3.2e3 | 1.5e3 |

  F^mag = 1 at 10 MeV gives 1.74e4, a factor 11.4. CHECKED, within MC noise (≤ 2 %). The log also gives 280 at 30 keV, a share of 19 % (0.187) from |q| < Q_AF/2 at 1 MeV, a factor 0.89 at 1 MeV, < 20 % spread above 0.3 MeV (17 % at 0.3 MeV), and edges 30/85 keV. All are consistent.
- eq:14.1-mmin, edge 7.2 keV. GAP (convention drift). c_M = 1.39e−4 is the J₂-only speed 2√3J₂|S|a of we:7-nio. The J₁+J₂ model that the same figure uses has c_M = 1.291e−4 to 1.364e−4, depending on direction (7.1 itself prints 255–269 meV·Å). With the fastest direction the edge is 7.3 keV, and the grid gives 7.4 keV. Say "J₂-only speed" or use 1.36e−4. The same drift affects the 14.2 numbers in A5.
- "|F|² = 0.84 at 2.6 keV, 0.49 at 5.3 keV". CHECKED (0.837, 0.490). The coefficients agree with Brown's Ni²⁺ ⟨j₀⟩ (0.0163, 35.8826, 0.3916, 13.2233, 0.6052, 4.3388, −0.0133), as I recall the table. Editor item: the ITC table number 4.4.5.2 is unverified (closed source).
- NiO inputs Ω = 18.13 Å³, ρ_T = 6.842 g cm⁻³, |Q_AF| = 2.575 keV, vertical line 0.486 MeV. CHECKED.
- Gap model: K = 0.0974 meV, factor 29.5 at 10 keV, 1.35 at 30 keV, < 3 % above 100 keV, weight √(K/2A₀), exponents 5268 at 10 mK and 52.7 at 1 K. CHECKED.
  - GAP: the one-constant easy-axis model gaps BOTH degenerate branches at 4.54 meV. NiO's biaxial anisotropy leaves the in-plane AFMR branch near 0.6 meV (≈0.14 THz; reviewer knowledge, source to cite). So the near-edge enhancement "×29 at 10 keV" is plausibly about halved, since only one branch reaches 4.5 meV. Say so, or treat the factor as an upper value.
- Undistorted J₁–J₂ model. GAP. It has a third, accidental zero at X = (2π/a)(1,0,0): A = B = 6J₂ − 2J₁ there, so ω = 0 (I verified this; 14.2's figure caption mentions it). 14.1 l.50 and l.126 speak only of Γ and Q_AF. This does not change any printed number (w → 0 at X, and |X| = 2.97 keV), but the statement "magnetic anisotropy lifts the Goldstone modes at Γ and Q_AF" should add that the rhombohedral distortion lifts the soft point at X.
- 4.54 meV attribution (editor item). CHECKED in substance, GAP in citation. dos Santos et al. Sect. III use 4.54 meV as the magnon energy at their M point, "consistent with Hutchings–Samuelsen, based on infrared measurements" (their refs. 132–133: Kondoh 1960; Sievers & Tinkham 1963). Far-IR measures the k = 0 AFMR (36.6 cm⁻¹ = 4.54 meV, value recalled, not opened), so "zone-centre magnon from far-IR" is correct physics. Cite Sievers–Tinkham/Kondoh for the measurement and dos Santos only for its use.

### A2. ΔS sum-rule bound and NiO numbers (14.1, D.38, 14.1/14.2 consistency)
- eq:14.1-ratio and eq:D.38-Wperp/Wpar. CHECKED.
  - ⟨d†d⟩ = v², W⊥ = |S|(1+2ΔS).
  - Wick: ⟨n²⟩ = ΔS(1+2ΔS), W∥ = ΔS(1+ΔS) (sympy). The on-site anomalous average vanishes.
- Zone average of w^M = 1 + 2ΔS. CHECKED analytically ((u−v)² + (u+v)²)/2, and numerically (1.15686 vs 1+2ΔS to 1e−12).
- Sum rule. CHECKED by sympy.
  - Excess ΔS(1+2ΔS).
  - W⊥^sr = (|S|−ΔS)(1+2ΔS).
  - The full-root half-sum equals W⊥^sr exactly.
  - The first omitted term −(2|S|)^{1/2}n d/4|S| reproduces it at O(|S|⁰).
  - One + two = |S|(1+2ΔS) − ΔS².
- Independent support: Huberman et al. Eq. (4) write the one-magnon weight with (S − ΔS), the same prefactor.
- "high by at least ΔS/|S|" (14.1 l.76, l.89; 14.2 l.121). GAP (scope). D.38 l.74 correctly says that the O(1/|S|) change of the ground state (hence of ⟨S^z⟩ and W∥) is not included. The 14.1 text drops this and states "at least" unconditionally. Add "at this order, with ⟨S^z⟩ and W∥ held at their linear spin-wave values" to l.76 and to the WE sentence.
- ΔS = 0.0784 (we:14-nio). My offset grids give 0.07827 at 60³ and 0.07843 at 100³. CHECKED to the printed digits. J₁ = 0 gives 0.0783; the change from 80³ to 100³ is 5e−5.
  - WRONG (minor), D.38 l.76: "grid sums converge as the inverse grid size". The successive differences, 1.1e−4 (60→80) and 5e−5 (80→100), scale as n⁻², which is expected for an integrable 1/k singularity in 3D. The extrapolated value is 0.0785; fig14_2.log at 128³ also says 0.0785.
  - Fix: "converge as the inverse square of the grid size". 0.0784 → 0.0785 is optional (0.078 stands everywhere).
  - Minor: the cube of side 4π/a is two primitive periods of the fcc reciprocal lattice, not "a full period". The average is unaffected.
- WE numbers: W⊥ 1.1569, W∥ 0.0846, ratio 0.0731, ordered moment 0.9216, W⊥^sr 1.0661, total 0.9947 (0.995), ΔS/|S| = 0.078 is 6.4× smaller than 0.5. |S| = ½: 15.7 % and 14.6 % (printed 16 % and 15 %). |S| = 5/2: 3.1 % and 2.9 %. Gray band |S| ≥ 0.784. J₁/J₂ = −0.0721. CHECKED.
- Consistency between 14.1 and 14.2. CHECKED: ΔS 0.078 and W∥/W⊥ 0.073 match. The zone averages of w∥ and w⊥ in 14.2 l.36 reduce to W∥ and W⊥ (sympy).
  - Notation: w^M_q (14.1) = w⊥(q)/|S| (14.2) = (u−v)² in the extended zone. This is three objects for one weight (editor item confirmed). Unify.
- Anderson's 0.078 for the simple-cubic AFM: consistent with my simple-cubic grid (0.0783–0.0784). The paper was not opened.

### A3. Magnetoelastic vs exchange-striction mixing; YIG hybridization gap (14.2)
- Exchange-striction claim (WP4 §2.3 correction, CORRECTIONS l.625). CHECKED. About a collinear state, S_i·S_j = S^zS^z + ½(S⁺S⁻ + h.c.), and every term is even in the bosons (D.19 bond expansions). ∂J/∂u therefore couples a phonon to pairs only. The linear transverse term comes from f_me. The B₂ term gives 2B₂(m_xX_xz + m_yX_yz), and the B₁ term is second order. CHECKED.
- eq:14.2-fme against Kittel and Rückriegel. CHECKED. Rückriegel (2.13)/(3.1) is B⊥Σ_{α≠β}M_αM_βX_αβ/M_s² with tensor strain, the same form as the book's.
- eq:14.2-gmp. CHECKED by hand. The coupling per cell is (2/|S|)^{1/2}B_me[…]. With X_αz → (ik/2)(2NM_cellω)^{−1/2} and the lattice sum, the result is g = B_me k/(2|S|M_cellω_p)^{1/2} on b₊ = (b_x + ib_y)/√2.
  - This matches Rückriegel (3.23)/(3.25) for k ∥ z: |Γ·ê₊| = B⊥k/√S, and X = (a + a†)/√(2mω).
- Editor item "Rückriegel Eq. (3.1) has a stray factor 2 against (3.23)": NOT REPRODUCED. In the arXiv HTML, (3.1) reads (n/M_s²)∫Σ B_αβ M_αM_β X_αβ. Expanding it gives exactly the B⊥√(2/S) of (3.23); the "2" in a text extraction is the exponent of M_s². The book cites only (3.23)/(3.25), so nothing needs to change. Drop the editor note, or restrict it to the journal version.
- Inputs. CHECKED against Rückriegel:
  - 4πM_s = 1750 G, giving |S| = 14.23.
  - ρ_s = 2μ_B × 5.17e−9 Oe cm², which is (2.13), giving D_sw = 5.985 meV nm².
  - nB⊥ = 6.96e6 erg cm⁻³, which is (3.7), giving B_me = 8.233 meV (95.6 K in their (3.9)).
  - ρ = 5.17 g cm⁻³ (3.15), giving M_cell = 5.496 TeV.
  - c⊥ = 3.843e5 cm s⁻¹ (3.16).
  - Their a is 12.376 Å; the book's 12.375 Å makes no difference.
- WE numbers. CHECKED:
  - Roots k = 4.628e−3 and 0.4181 nm⁻¹.
  - Lower crossing: ω× = 11.705 µeV (2.83 GHz), λ = 1.36 µm, g = 0.1757 µeV, gap 0.351 µeV = 84.9 MHz = 3.0 %.
  - k-window 3.07 %.
  - |X^p|² = 0.146 at Δ = 2g and 0.0097 at Δ = 10g.
  - Upper crossing: gap 3.34 µeV, 0.32 %, ka = 0.517.
  - (g/ω)² = 2.25e−4.
  - Absorption: p = 1.16e−8 eV, phonon content 2.9e−12.
  - eq:14.2-hyb contents (sympy). CHECKED.
- Note: WE 14.2 uses the room-temperature M_s (1750 G), and WE 14.3 uses the 0.1 K value (2460 G). Each states its own, but a clause linking them would help the reader.

### A4. Larmor line, λ_S = g_J − 1 scope, Kittel and AFMR weights, YIG WE (14.3)
- eq:14.3-abs. CHECKED: g^φ = ig p/m_e from (g/m_e)∇φ·s_e of eq:8.1-alp. Dark-photon coefficient: CHECKED against Chigusa (55) and (59), with H = −(εeQ/m_e)B_H·S, Q = −1, B_H = v×H̃ m.
- Larmor theorem: [H, S⁻_tot] = ω_L S⁻_tot, with Zeeman −ω_L S^z_tot when z is along the net spin. CHECKED. Matches Oshikawa–Affleck (2.4)/(2.5).
- Detailed balance gives ⟨S⁺S⁻⟩ = 2⟨S^z⟩/(1 − e^{−βω}) (sympy). eq:14.3-larmor: CHECKED; at T = 0 and 𝔰 = |S| it equals eq:7.1-Sfm. eq:14.3-rate: CHECKED. Dimensions CHECKED.
- Against Mitridate et al. (27) and (35). CHECKED. With f = −(i/√2)g(g_j−1)√ρ v/m_e, U = 1, V = 0, r = (1, i, 0), their peak rate is S g²λ²ρv⊥²/(m_e²m_cellγ). This equals eq:14.3-peak with 𝔰 = S, and their γ is the full width (Breit–Wigner factor 4ωω_νγ/…).
- Against Chigusa (25)–(27): the two-level rate (π/2)|V|²δ with |V|² = sNρv⊥²/f² equals the book's sample rate. CHECKED.
- Against Chigusa (38): equality at τ = 4/Γ_M without the cavity factor ½. CHECKED.
- Selection rule for the 19 gapped YIG branches and Mitridate (28). CHECKED.
- λ_S = g_J − 1 by projection, and Mitridate (30) and (34). CHECKED. Mitridate (30) is the standard Landé form.
- Table 14-lande (sympy): Ce, Sm, Gd, Dy, Er g_J and λ_S. CHECKED. Sm³⁺ ratio −5. CHECKED.
- Quenched-ion argument. CHECKED: ⟨L_a⟩ = −2ξΣΛ_abS_b, g_ab = 2δ − 2ξΛ, and the spin changes only at second order; g = 2.2 gives 1.44. The scope sentence "λ_S = g_J − 1 belongs to J multiplets only" is correct.
  - NOTATION λ_S row: WRONG. "spin–lattice factor" should read "spin fraction of the ionic angular momentum, s_e(0) = λ_S J (g_J − 1 for a J multiplet; 1 for a quenched ion)". This confirms the editor item.
- Kittel. CHECKED by sympy.
  - eq:14.3-Hu with ω_M = 2μ_B M_s (Heaviside–Lorentz, μ₀ = 1) from ½𝓥ΣN_iM_i² and S^z ≈ S − (S_x² + S_y²)/2S.
  - Oscillator frequency √(ω_x ω_y).
  - ⟨x²⟩₀ = ½√(ω_y/ω_x).
  - The weights of eq:14.3-ellipse and their average (ω_x + ω_y)/2ω_Kit.
  - Film in-plane and film normal, sphere.
- Limit Check 14.2(a) curve and gray band B₀ ≥ 4.77 μ₀M_s; YIG markers at x = 0.111 and 0.351. CHECKED.
- AFMR: |S|A₀ = ω_E + ω_A, |S|B₀ = ω_E. eq:14.3-afmr and the weight (u−v)²|S| = ω_A/ω_AFMR · |S| = |S|ω_AFMR/(2ω_E + ω_A) (sympy). CHECKED. The mapping 𝔰 → 2|S|ω_AFMR/(2ω_E + ω_A) per pair cell follows from (2π/𝓥)Σ|⟨S_x⟩|². CHECKED.
- Limit Check 14.2(b) and the end paragraph: ED ratios 0.849/0.911 at ω_A = ω_E, 5–23 % at |S| = 3/2, gray band ≤ 0.42. CHECKED against ed14_3.log and limit14_3a.log. The cluster itself was not rerun.
- YIG WE. CHECKED:
  - Ω = 947.6 Å³, m_cell = 2951.7 u, 𝔰 = 10 (12 vs 8, which is Mitridate Sect. III).
  - μ₀M_s = 0.2460 T, 37.84 emu/g (Chigusa: 38 emu/g at about 100 mK), ω_M = 28.48 µeV.
  - B₀ = 86.4 mT, saturation at 82.0 mT, 9.49 µeV, internal field 4.4 mT.
  - βm = 11.6, thermal factor 1 + 9e−6.
  - Γ_M = 1e−10 eV = 24.2 kHz, 6.58 µs.
  - ⟨v⊥²⟩ = 1.3284e−6.
  - **R_peak = 3.635 s⁻¹ kg⁻¹ = 1.15e8 kg⁻¹ yr⁻¹** (my own evaluation).
  - 2.71 g sphere, 35 h⁻¹, ratio 0.474.
  - Film: ω_L = 3.16 µeV, B₀ = 27.3 mT, weights 3.16 and 0.316, average 1.74.
- Γ_M/ω = 1e−5 (editor item). GAP. Mitridate Sect. V B treats the width as a free parameter and shows γ/ω = 1e−2 and 1e−5, the latter "consistent with … YIG's Kittel magnon width". The text's "take" is accurate but does not say the value is assumed. Write "assume (a free parameter, set to the YIG Kittel width)". The same applies to the MnF₂ sentence "With the same ratio".
- Exchange dispersion M ≈ 3.5 MeV. CHECKED against Chigusa (19) and the text below it. Inconsistency: the book's own D_sw (WE 14.2) gives M = 1/2D_sw = 3.25 MeV. This is immaterial for the 1e−18 estimate; quote either value consistently.
- MnF₂ 1.021 vs 1.1 meV (editor item). GAP, reconciled as follows.
  - Vaidya et al. give μ₀H_E = 47.05 T and μ₀H_A = 0.82 T (text and Fig. 1 caption). These reproduce ω_AFMR = 1.021 meV (247 GHz) and B_sf = √(2H_EH_A) = 8.78 T.
  - Their own Fig. 1 caption, however, puts the measured spin flop at "μ₀H_SF ∼ 9.4 T", and Bayrakci et al. give a 1.1 meV gap at 4 K.
  - Since ω_AFMR ≈ gμ_B B_sf for ω_A ≪ ω_E, the measured pair is self-consistent (1.1 meV ↔ 9.50 T), while the fitted fields are about 7 % low.
  - Correction: give the measured gap (1.1 meV) and spin flop (≈9.4 T) as the reference, and present 1.021 meV and 8.75 T as values of the fitted fields. Keeping ω_E and fitting ω_A to 1.1 meV gives ω_A = 0.110 meV, weight 0.100 (0.250 per pair, +8 %), and B_sf = 9.5 T.
  - The peak rate (∝ |S|ω_A/ω_AFMR²) is unchanged: 0.0909 vs 0.0910, so 2.6e−2 s⁻¹ kg⁻¹ stands.
  - fig14_3 and its caption (8.75 T) follow the fitted values.
- MnF₂ numbers as printed. CHECKED:
  - ω_E 5.447 meV, ω_A 0.0949 meV, ω_AFMR 1.0213 meV, 247 GHz, weight 0.0929 vs 0.0933, 0.232 per pair.
  - 0.74 of YIG per mass, peak ratio 7.2e−3, 2.6e−2 s⁻¹ kg⁻¹.
  - B_sf = [B_A(2B_E − B_A)]^{1/2} = 8.746 T, lower line 0.009 meV, ω_M/ω_E = 1.27e−3.
  - Easy axis mainly dipolar: matches Bayrakci.
- Chigusa equation numbers: (25)–(27), (38), (55), (59) are correct in the fetched version. (35) is the cavity–magnon Hamiltonian, as the editor notes, and the text does not cite it.

### A5. Two-magnon response, edges and kinematics (14.2)
- eq:14.2-amp. CHECKED. The momentum labels (k′ = k − q on A, k + q on B) and the creation-creation terms u_k v_{k−q} − v_k u_{k−q} were rederived by hand.
- eq:14.2-S2m and w∥ normalization: (2π/Ω)(1/2N_s)Σ|𝒜|². CHECKED.
- Against Huberman Eq. (5): f = ½(u₁v₂ − u₂v₁)², the same form. CHECKED.
- Zero at q = 0 and at reciprocal vectors, the q² law, and sinh2θ near Q_AF. CHECKED.
- Ladder: −(2/𝓥)Im[𝒜†𝒢𝒜] = eq:14.2-S2m, and the ω-integral sum rule (2π/𝓥)𝒜†𝒜. CHECKED.
- NiO weights. CHECKED by my own grid/Monte Carlo:
  - w⊥ ≃ 0.289 qa (analytic: c[111]/(2J_AB(0)a)).
  - w∥/(qa)² = 0.0148.
  - At (¼,¼,¼): 1.287 keV, w⊥ = 1.000, w∥ = 0.0817.
  - Ratio peak 0.0822 at 1.39 keV; ratio 0.048 at 0.515 keV.
  - w∥(Q_AF) = 0.246 → 0.250 (64³ → 100³; log 0.262). "Near 0.25" is fine.
- Edges. CHECKED: one-magnon energy at (¼,¼,¼) 105.84 meV; continuum minimum at the one-magnon branch (random search 107.4 ≥ 105.8; X-shifted pairs 116.8); max ω 118.17 meV, giving 236.3 meV.
- eq:14.2-mratio 5.03 and the masses 1.43 keV / 0.285 keV. CHECKED with c = 1.39e−4. With the J₁+J₂ fastest speed, 1.36e−4, the values are 5.1 and 1.46 keV (see A1). c_M = v_max/19.1 CHECKED. (qa)² ≈ 2.5e−6 CHECKED.
- Ferromagnetic ring (14.2 l.60). CHECKED by ED (45 states): 0.3277|J| vs free pair 0.3820|J| at the same total momentum.
  - GAP (wording): the lowest two-deviation levels are 0 and 0.191 (descendants of the zero- and one-magnon states). Write "the lowest level of total spin N/2 − 2".
- Single-ion energies 4D(S−1), 2D(2S−1), difference 2D (sympy). CHECKED.
- FSI nuisance 0.5 × 0.073 ≈ 0.04, tagged as an estimate (editor item). CHECKED: the text already says "an estimate of that size".
- Esposito et al. (two-magnon reach down to about 1 keV for NiO, MnO, Cr₂O₃): CHECKED against their Sect. on the two-magnon channel ("as low as m_χ ∼ 1 keV").

## B. Limit Check numbering vs chapter map
CHECKED. Counter within chapter (preamble l.38). build/main.aux gives lim:14.1a = 14.1, 14.3a = 14.2, 14.4a = 14.3, 14.5a/b = 14.4/14.5, 14.6a–c = 14.6–14.8. The tags in map14.pdf (pdftotext) are 14.1 (Sect. 14.1), 14.2 (Sect. 14.3), 14.3 (Sect. 14.4), 14.4–14.5 (Sect. 14.5), 14.6–14.8 (Sect. 14.6). All match.

Editor note "map14.py labels this box Limit Check 14.3 while the label is lim:14.4a": consistent, not an error. Labels name sections, while printed numbers count boxes. The aux is from 05:36 and the map from 04:17; a rebuild is needed only if boxes are added or removed. The numbers printed inside the boxes (14.1a and 14.3a captions and text) were all checked above.

## C. Dimensional analysis (all displayed results)
CHECKED. Every one of these equations has the units it should:
- eq:14.1-Safm, 14.1-contract and 14.2-S2m: eV², like S_ab of the density row.
- eq:14.1-rate and 14.1-inc: rate per mass, dimensionless in natural units.
- eq:14.1-mmin: eV.
- eq:D.38-weight and eq:14.2-mratio: dimensionless.
- eq:14.2-gmp and eq:14.2-hyb: eV.
- eq:14.2-ladder: eV².
- eq:14.3-abs and 14.3-rate: eV.
- eq:14.3-larmor: eV².
- eq:14.3-peak: dimensionless.
- eq:14.3-Hu, 14.3-kittel and 14.3-afmr: eV.
- eq:14.3-afmrweight: dimensionless.

## D. Drift against NOTATION (factor 2, π, sign, convention)
- No factor-2 or π drift found. S_ab normalization (2π/𝓥) and the ferro/Larmor prefactor π|S|/Ω agree across 7.1, 14.1, 14.3 and D.38. The sign of iε_abc ẑ_c is consistent with S⁻ creating the magnon.
- Ω. GAP: NOTATION allows only "unit-cell volume". 14.1 and D.38 use "volume per magnetic ion", and 14.3 uses "volume of the magnetic cell" (YIG primitive cell, MnF₂ pair cell). For NiO the ion volume equals the chemical primitive cell, but within one chapter Ω changes meaning between 14.1 and 14.3. Define Ω_ion, or state the cell each time, and add a NOTATION note.
- Symbols used in 14.1–14.3/D.38 that have no NOTATION row (merge item):
  - Magnon weights and energies: w^M_q, w∥(q), w⊥(q) (beside W∥, W⊥), 𝒜^{2m}_k(q), U^mm, 𝒢^{2m}, c_M.
  - Magnon–phonon hybrids: g^mp, B_me, B₁, B₂ (clash with the Bogoliubov B_k and with field B), X^m_h, X^p_h, ω_m, ω_p, D_sw, M_cell (check), b₊.
  - Larmor and Kittel: ω_Lar (partII notes say accepted, but there is no row), 𝔰_net, ω_Kit, ω_Kit,i, N^dm_i, ω_M (clashes with ω^M_k and with 14.5's ω_M, as the editor notes), Γ_M, H_u.
  - AFMR and anisotropy: B_E, B_A, B_sf, D_an, K (easy-axis).
  - ε_G (D.38; clashes with energy ε).
  - Bare Δ, used both as detuning ω_m − ω_p and as anisotropy gap in 14.2 (CORRECTIONS bans bare Δ).
- λ_S row: WRONG (see A4).
- t_coh = 1/(m v₀²) = 0.104 ms at 10 µeV: consistent with the NOTATION row (8.2 estimate); no 2π.

## E. Campaign values (CORRECTIONS, SOTA, DC-RESULTS, R18)
- CORRECTIONS l.344 (r_2m = 0.146 and ΔS/S = 0.156 at S = ½) matches the book (14.6 %, 15.7 %). l.625 (exchange striction) is applied correctly. r^M_mag = ΔS/S matches.
- SOTA l.145 estimates "F^mag ∼ 0.5 at q ≈ 0.5 keV for Fe³⁺". The book does not use it, and it is implausible (Fe³⁺ ⟨j₀⟩ ≈ 0.99 at 0.25 Å⁻¹).
- No superseded value is used in these sections.
- DC-RESULTS and returns/R18 hold DC-83, 5, 41, 93, 49/54/36, 4, 2 and 67. None concerns magnons or absorption, so nothing applies here. DC-43 (magnon sector) and DC-book-14.3 (MnF₂ zero-point correction) are still "to write" in DEFERRED-COMPUTE.

## F. Corrections owed (summary)
1. D.38 l.76: "inverse grid size" → "inverse square of the grid size". ΔS extrapolates to 0.0785 (optional digit change).
2. NOTATION λ_S row wording (WRONG).
3. 14.1 l.76/l.89 and 14.2 l.121: qualify "at least ΔS/|S|" as holding at this order, with ⟨S^z⟩ and W∥ at their linear spin-wave values.
4. 14.1 l.55 and 14.2 l.56: c_M = 1.39e−4 is the J₂-only speed. The J₁+J₂ model gives 1.29–1.36e−4; the edge becomes 7.3 keV, the ratio 5.1, and 1 meV needs 1.46 keV. Alternatively, label the value as J₂-only.
5. 14.1 l.126: the one-constant easy axis gaps both branches. NiO's in-plane mode is about 0.6 meV, so the factor 29 is an upper value. Also mention the accidental soft point at X.
6. 14.1 l.126 and fig caption: cite the original far-IR AFMR measurement (Sievers–Tinkham 1963; Kondoh 1960) for 4.54 meV.
7. 14.3 l.75 and l.139: Γ_M/ω = 1e−5 is an assumed value (Mitridate Sect. V B, free parameter).
8. 14.3 l.139 and fig14_3: measured 1.1 meV and B_sf ≈ 9.4 T vs the fitted-field values 1.021 meV and 8.75 T. Present the measured values as the reference; the peak rate is unchanged.
9. 14.3 l.80: M = 3.5 MeV (Chigusa) vs 3.25 MeV from the book's D_sw. Pick one.
10. 14.2 l.60: "lowest level of total spin N/2 − 2".
11. Notation: unify w^M/w⊥/W⊥; settle the Ω meaning; add the missing rows in D.
12. Editor note on the Rückriegel (3.1) factor 2: not reproduced (arXiv HTML); no change to the text.
