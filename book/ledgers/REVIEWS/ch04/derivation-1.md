# Ch4 part 1 (4.1–4.5, D.6–D.9, C.5–C.7): derivation check

Reviewer: derivation verifier (isolated), 2026-11-02. Nothing in these files is regenerated in the figure pass, so there are **no FIG-PASS entries**: every number was checked.
Method. I redid the algebra by hand and with sympy (Lindhard antiderivative, high-frequency series of 𝓘(w), moments ⟨Δ^n⟩, iteration for the plasmon q⁴ term, mass–velocity expansion, ∫x²/(1+x⁴)²). Numbers were recomputed in numpy/scipy from the closed forms. The Si optical numbers came from the repo data (sources/4.4/si_franta_300K.yml, sources/4.3/si_henke.nff).
Sources. Fetched to sources/review-ch04a/ and deleted afterwards: Knapen 2101.08275, Hochberg 2101.08263, Kahn–Lin 2108.03239 and Ismail-Beigi cond-mat/0101383. Paywalled sources were checked from recall only: Kubo 1957, Bunge 1993, Bethe–Salpeter §61, Mermin 1970 and Lindhard 1954.
Scripts are in the scratchpad: sym.py, num1.py, num2.py, lind.py, data.py, d89.py.

## Summary
- WRONG: 1 (a number in the plasmon limit-box caption).
- GAP: 7 (one of them is the open editor item on Mermin causality, for which an argument is supplied below).
- NOTATION drift: 10 items beyond the known λ/Δ/M renames.
- Everything else is CHECKED.

## Known items (editor-notes.md)
- 4.1 λ → λ_osc, Δ → Δ_tl, and M for the oscillator mass: still bare in s4-1 (ll.115–176). Pending at the revision, not re-reported. Also: s4-4 l.185 uses M for the projectile mass and C.6 uses M for the oscillator mass. Check both against entry 24 when renaming.
- Kubo isolated vs isothermal: see the GAP at s4-1 l.112. The attribution itself is consistent with Kubo 1957 §5–6 (from recall, paywalled).
- 4.3 hydrogen TRK split 0.565/0.435: CHECKED. The bound sum is 0.56500 and the continuum 0.43500 (total 1.000000), consistent with the Bethe–Salpeter §61 table.
- 4.3 Bunge Si HF energy −288.854 Eh: CHECKED against the standard RHF value −288.85436 Eh (recall). It gives K = 7.860 keV and K̄ = 561.4 eV.
- 4.5 q⁴ plasmon coefficient: CHECKED. sympy iteration of ε_Lin = 0 gives ω² = ω_p² + (3/5)v_F²q² + [1/4m² + (12/175)v_F⁴/ω_p²]q⁴. 12/175 = 3/7 − 9/25, and the single-particle term is q⁴/4m², from (q²/2m)² in A.
- 4.5/D.9 Mermin causality: GAP, still open. Argument below.

## s4-1 (Kubo formula)
- l.9–33 density-matrix expansion, trace identity Tr([B,ϱ]A)=Tr(ϱ[A,B]), Eq. 4.1-general: CHECKED.
- l.16–18 real potential split into n_e(q)φ + n_e(q)†φ*: CHECKED (A.3 sign: e^{iq·r} gives momentum +q).
- l.39–40 Eq. 4.1-kubo, and l.46–50 the ripple with V^{-1}Σe^{-iq′·r}n_e(q′): CHECKED.
- l.51 **GAP (dimension).** "The response function … has the dimension eV²": this holds for R(q,ω) only. R(q,t), the object in the convolution just displayed, has eV³. Correction: "R_ee(q,ω) has the dimension eV² (R(q,t) has eV³)".
- l.60–66 switching e^{−iωt+ηt} and transform at ω+iη: CHECKED.
- l.69–74 Eq. 4.1-reality, including R*(q,t) = −(i/V)Θ⟨[O_a(t),O_b†]⟩, and the even/odd parity: CHECKED.
- l.82–89 commutator in eigenstates, −i∫e^{i(x+i0)t} = 1/(x+i0), and Eq. 4.1-lehmann: CHECKED.
- l.96 Eq. 4.1-ImR, with 𝒮_{O†}(−ω) the emission sum: CHECKED.
- l.101–106 Eq. 4.1-power: CHECKED by time averaging: P = −½ωφ₀²V Im R. It agrees with Eq. 2.1-harmonic using Ô = ½φ₀O_b (rate (π/2)φ₀²𝒮). φ₀² = 2ρ_χ/m_φ² is consistent with NOTATION.
- l.110–112 static limit VR(0) = −2Σ|O_fi|²/ΔE and the second-order shift ½VR(0)φ₀²: CHECKED.
- l.112 **GAP (wording).** The ω→0 limit of the Kubo function is Kubo's *isolated* susceptibility. "Exchanges no heat with its surroundings" describes the thermodynamic adiabatic susceptibility, which equals the isolated one only when energy is the sole conserved quantity. Suggest: "…describes a target isolated from any bath (Kubo's isolated response)", and drop "exchanges no heat".
- l.117–123 [O(t),O] = −2iλ² sin ω₀t, the transform ω₀/(ω₀²−z²), and Eq. 4.1-osc (both forms): CHECKED.
- l.124 Lehmann weights (n_B+1)/(ω−ω₀) + n_B/(ω+ω₀); the antiresonant term swaps the denominators, so n_B cancels: CHECKED.
- l.126 λ² = 1/(2Mω₀), x(ω) = φ/[M(ω²−ω₀²)], VR(0) = −2λ²/ω₀ and the shift −λ²φ₀²/ω₀: CHECKED. The limiting case (the classical spring) agrees.
- l.130–133 damped response, −Im VR, the peak 2λ²/Γ_w (10λ²/ω₀ at Γ_w = 0.2ω₀), the sign of Re below and above resonance, and the 2λ²ω₀/ω² tail: CHECKED.
- l.143 analyticity argument: CHECKED. l.147–151 poles −iΓ_w/2 ± (ω₀²−Γ_w²/4)^{1/2}, |ω| = ω₀, critical damping: CHECKED. Caption: the upper pole at Γ_w = 3ω₀ is −0.382iω₀: CHECKED.
- l.162–165 Eq. 4.1-tail. The 1/z coefficient ⟨[O_a†,O_b]⟩ and the 1/z² double commutator, written out in eigenstates, are both CHECKED. Oscillator [O,[H,O]] = 2λ²ω₀: CHECKED.
- l.170–176 Eq. 4.1-twolevel: CHECKED. p₀−p₁ = tanh(βΔ/2); at T = Δ/2 the weights are 0.8808/0.1192 and the factor 0.7616, so VR(0) = −1.523|O₁₀|²/Δ: CHECKED. The T ≫ Δ limit −|O₁₀|²/T and the tail 2Δ(p₀−p₁)|O₁₀|²: CHECKED.

## s4-2 (correlation functions, S)
- l.11–18 Eq. 4.2-Sab, Hermiticity S_ab* = S_ba, and the detailed balance S_ab(−q,−ω) = e^{−βω}S_ba(q,ω): CHECKED. This agrees with Knapen Eq. (4) (2π/V, Gibbs weights, δ(ω+E_i−E_f)). Knapen writes n_{−k}, which is the same object for S(−q) = S(q).
- l.22 Eq. 4.2-rate, dimensions eV³·eV⁻⁴·eV² = eV: CHECKED.
- l.29 q₀ = 3.729 keV, 2π/q₀ = 3.325 Å, 1/(10 eV) = 0.0658 fs: CHECKED.
- l.34–45 Van Hove steps (stationarity, r″ = r′+r, t → −t) and Eq. 4.2-vanhove: CHECKED. Dimensions: 𝒢_VH in Å⁻³ and S in eV²: CHECKED.
- l.48 classical reading, 𝒢(r,0) = δ³(r) + 𝓃_e g_pair: CHECKED (homogeneous target).
- l.50 free electron: correlation e^{−iq²t/2m_e} and 2πδ(ω−q²/2m_e): CHECKED.
- l.54–58 Eq. 4.2-static: both forms CHECKED. The Bragg term (2π/V)|⟨n_e⟩|²δ(ω): CHECKED.
- l.62 diagonal FDT through detailed balance: CHECKED. l.64 off-diagonal FDT: redone term by term, (R_ab − R_ba*) = −i(1−e^{−βω})S_ab. Eq. 4.2-fdt is CHECKED and agrees with Knapen Eq. (3) (Im χ = −½(1−e^{−βω})S).
- l.75–78 relabelled Lehmann form (p_i−p_f)c_if and Eq. 4.2-spectral: CHECKED.
- l.82 the silicon gap at 300 K gives e^{−βω} = 2.25×10⁻¹⁹ ("2×10⁻¹⁹"): CHECKED.
- l.84 oscillator FDT: 1/(1−e^{−βω₀}) = n_B+1 and 1/(1−e^{βω₀}) = −n_B: CHECKED.
- l.86 S = (2q²/e²)L: CHECKED (see s4-4).
- l.92–102 positivity, the Cauchy–Schwarz bound and i(R−R†) ⪰ 0 for ω > 0: CHECKED.
- l.108 Eq. 4.2-S0: CHECKED.
- l.111 **GAP (wording).** The elastic term is not "from γ′ = γ" of the single-particle sum. At T = 0 those terms carry n(1−n) = 0. The elastic term is the many-body f = i term, (2π/V)|Σ_γ n_γ⟨γ|e^{iq·r}|γ⟩|²δ(ω), which also contains cross terms between different γ. Correction: "plus the elastic term of the many-body diagonal, f = i, which at T = 0 is (2π/V)|⟨n_e(q)⟩|²δ(ω)".
- l.116–124 Eq. 4.2-gas: CHECKED. Steps: weight m_e/kq at u₀ = (m_eω/q−q/2)/k; Pauli bound k² + 2m_eω > k_F²; prefactor 4π·2π/(2π)³·m_e/q = m_e/πq.
- l.126–130 edges ω_±, the linear form m_e²ω/πq and the parabola: CHECKED. The forms meet on ω = qv_F − q²/2m_e at m_e(2k_F−q)/2π: CHECKED. At q = k_F/2 this is 0.2387 m_ek_F at ω = 0.75E_F: CHECKED.
- l.132 total weight 2π𝓃_e(3x/4 − x³/16): CHECKED. The first-moment argument (k → −k−q antisymmetry) and π𝓃_eq²/m_e: CHECKED.
- l.134 Si valence numbers:
  - k_F = 3.570 keV, E_F = 12.47 eV, v_F = 6.99×10⁻³, v_max/v_F = 0.3793: CHECKED.
  - 2k_F(1−v_max/v_F) = 1.241k_F = 4.43 keV: CHECKED.
  - S⁰ = m_e²v_max/π = 2.20×10⁸ eV² = 0.1207 m_ek_F: CHECKED.
- Fig. 4.2 caption numbers (0.239 at 0.75E_F; ω_− = 3E_F and ω_+ = 15E_F at 3k_F): CHECKED.
- l.149 Eq. 4.2-hydrogen: CHECKED (inelastic 2π𝓃_T Σ|f|², elastic (2π/V)F_1s²|Σe^{iq·R}|²).
- l.154 rate = 𝓃_T σ_T v: CHECKED.
- l.160 F_1s(q₀)² = 0.4096 and 1−F² = 0.590: CHECKED. Σ_m|f_{1s→2p}(q₀)|² = 0.0611, recomputed by quadrature: CHECKED. S^st(q₀) = 1: CHECKED.

## s4-3 (causality and sum rules)
- l.9–11 KK from Eq. 4.2-spectral: CHECKED. l.16–17 Eq. 4.3-KK and l.23 the contour derivation, R = (iπ)⁻¹PV∫R/(ω′−ω): CHECKED.
- l.34 Eq. 4.3-KKhalf and l.39 Eq. 4.3-static (sign, factor 1/π, T = 0 reduction): CHECKED. The large-ω limit −(2/πω²)∫ω′Im R: CHECKED.
- l.46–48 Eq. 4.3-moments: redone, including the (−1)^k and S_ba(−q) bookkeeping. CHECKED. l.55 Eq. 4.3-firstmoment, l.60 ∫ωS_aa = π𝓜¹_aa, and the oscillator first moment 2πλ²ω₀ (for VS): CHECKED.
- l.64–66 Eq. 4.3-continuity ([p², e^{iq·r}] and the symmetrized current) and l.69 the position-space continuity sign: CHECKED. 𝓜¹ in eV⁴ matches NOTATION.
- l.71 [e^{−iq·r}, p] = q e^{−iq·r}, q²/m_e per electron, Eq. 4.3-fsum: CHECKED.
- l.80 conversion to per electron at T = 0, and the T > 0 fold ∫₀^∞ω(1−e^{−βω})S = π𝓃_eq²/m_e: CHECKED.
- l.82 mean energy q²/(2m_eS^st): CHECKED (the elastic δ(ω) is included in the weight; harmless).
- l.86–89 ω_p² = e²𝓃_e/m_e: 16.606 eV (valence) and 31.07 eV (7.00×10²³ cm⁻³): CHECKED. ∫ωL = (π/2)ω_p²: CHECKED.
- l.95 Eq. 4.3-fsumNL: CHECKED algebraically. The "12 to 19 percent" figure lives in E.2 and is not in scope.
- l.100 (p+q)⁴ + (p−q)⁴ − 2p⁴ = 4p²q² + 8(p·q)² + 2q⁴ (sympy): CHECKED. Darwin and spin–orbit drop out: CHECKED.
- l.102 Eq. 4.3-mv: −(q²/m_e)[(5/3)K̄/m_e + q²/4m_e²]: CHECKED. Dimensionless: CHECKED.
- l.105 Si relativistic numbers:
  - K = 7.860 keV, K̄ = 561.4 eV, (5/3)K̄/m_e = 1.83×10⁻³ = 0.0256 e/atom: CHECKED.
  - Z²α²m_e/2 = 2.667 keV, giving 8.70×10⁻³: CHECKED.
  - q²/4m_e² at 53 keV = 2.69×10⁻³, with 53 keV = 2·10 MeV·v_max: CHECKED.
- l.111 Eq. 4.3-species and l.116 the mixed rule ∫ω Re S_eκ = 0 (inversion + Hermiticity): CHECKED. Nuclear share 14m_e/M_Si = 2.735×10⁻⁴ (2.745×10⁻⁴ for ²⁸Si; the text uses the natural mass): CHECKED.
- l.120–134 Eqs. 4.3-atomq, 4.3-osc and 4.3-TRK, including the dipole limit and the factor 2m_e: CHECKED.
- l.140–148 hydrogen (WE 4.3):
  - f_np = 0.4162, 0.0791, 0.0290, 0.0139: CHECKED.
  - Large-n limit (2⁸/3)e⁻⁴/n³ and density (2⁷/3)e⁻⁴/E_B = 0.7815/E_B: CHECKED.
  - Continuum formula, threshold value and ω^{−7/2} tail: CHECKED.
  - Bound 0.5650, first three 0.5243, continuum 0.4350, within E_B 0.3163, above 10E_B 0.00421, total 1.0000: CHECKED.
- l.150 q₀²/2m_e = E_B and 0.061·¾ = 0.0458E_B: CHECKED.
- l.154–158 free-gas f-sum (WE 4.4):
  - The x integral gives q²k_F³/3πm_e = π𝓃_eq²/m_e: CHECKED.
  - Linear-region share (1−q/2k_F)³ = 27/64 = 0.42: CHECKED.
  - Mean energy (2/3)qv_F: CHECKED.
  - The "10⁻⁶ from 0.1 to 4k_F" claim: reproduced at 0.4 and 1.0k_F (D.8 forms, error < 10⁻¹⁴). The other q were not run.
- l.160–164 S^st ≤ q²/(2m_eE_g); crossover 3m_eE_g/2k_F = 0.238 keV; ratio 0.420 at 0.1 keV: CHECKED.
  - **GAP.** The bound assumes the valence f-sum ∫ωS_val = π𝓃_valq²/m_e exactly. WE 4.5 shows the valence share is only about 3.93 of 4 (core–valence Pauli transfer). Add "to the accuracy with which the valence electrons carry their own f-sum (about 2 percent in Si, \cref{we:4-sifsum})".
- l.168–176 Si f-sum (WE 4.5), recomputed from si_henke.nff:
  - Region integrals 0.348 / 8.461 / 1.603: CHECKED.
  - Power-law extension of the last decade (3–30 keV): 0.008 with my fit against the printed 0.007, which is a fit choice. The total 10.420 and the 3.580 below 30 eV are unchanged: CHECKED.
  - 3.55 with mass–velocity and 3.93 below the L edge: CHECKED.
  - Edges: L onset 99.6–99.8 eV (mid-step 100.0 eV), K 1.839 keV: CHECKED.
  - Saturation 96.9% by 1 keV, 83.5% by 5 keV and 95.7% by 10 keV against the printed 97/84/96: CHECKED.
  - 99.8 eV/ω_p = 6.01: CHECKED. f₂ = (π/2)ω df/dω from σ = 2r_eλf₂: CHECKED.
- l.176 q²/2m_e at 10 keV = 97.8 eV: CHECKED. q·v_max = 26.5 eV is printed as "26": round to 27, or write 26.5.

## s4-4 (screening, dielectric function)
- l.7–23 Eqs. 4.4-phitot, 4.4-proper and 4.4-dyson: CHECKED. l.39–40 Eq. 4.4-eps, both forms: CHECKED. It agrees with Knapen Eq. (5) (1/ε = 1 + (4πα/k²)χ).
- l.47 the factor 1/11.7 ("a twelfth"): CHECKED.
- l.60–64 Eq. 4.4-epsGG: CHECKED. Symmetrized diagonal equality: CHECKED.
  - **GAP (attribution).** "the longitudinal dielectric matrix of Ref. [Knapen, Eqs. (A5)–(A7)] in its unsymmetrized form": Knapen's (A5)–(A7) are the *symmetrized* matrix (their footnote 3). Correction: "…the unsymmetrized counterpart of the symmetrized matrix of Ref. [Eqs. (A5)–(A7)]".
- l.68–75 ε_mac = 1/(ε⁻¹)₀₀, the Schur form and 1 − v_C R̄₀₀: CHECKED (see D.7).
- l.82–85 Eq. 4.4-SL: 2q²/e² = q²/2πα. CHECKED against Knapen Eq. (6), Hochberg Eq. (S.24) (S = 2q²W/e²) and Hochberg Eq. (S.7).
- l.92 dark photon and total-charge L: consistent with Hochberg (main text and Supplementary Material, "exactly the correct rate for a dark photon mediator").
- l.94 L = ε₂/|ε|² and S = S^prop/|ε|²: CHECKED.
- l.96 Si data from Franta (300 K):
  - ε₂ peaks 3.42 and 4.24 eV: CHECKED.
  - At 3 eV ε₂ = 2.376 and L = 3.12×10⁻³: CHECKED.
  - ε₁ zeros at 4.22 and 16.30 eV: CHECKED.
  - L peak 4.49 at 16.45 eV, FWHM 3.659 eV: CHECKED.
- Fig. 4.5 caption: f-sums 96.4% (ε₂) and 92.4% (L) below 40 eV: CHECKED.
- l.109 Eq. 4.4-fsumL: CHECKED. It agrees with Hochberg Eq. (S.10) (∫ωW = (π/2)ω_p²). l.112 2.73×10⁻⁴: CHECKED.
- l.116 Eq. 4.4-fsumeps: CHECKED. The removal argument is the known 4.8 item. (π/2)ω_p² = 433.2 eV²: CHECKED.
- l.123 Eq. 4.4-inverse (both) and the metal value π/2: CHECKED. From the data, with ε∞ = ε₁(4 meV) = 11.685: 99.8% and 97.8%. (With 11.7 they would be 99.7% and 97.7%.) CHECKED.
- l.131–134 Eq. 4.4-Ebar: Ē = 17.365 eV; 17.4/1.11 = 15.7: CHECKED.
- l.140 Eq. 4.4-sigma, from Ampère–Maxwell (HL): CHECKED. σ₁ = ω|ε|²L agrees with Hochberg's σ₁ = (ω/4π)|ε|²W in Gaussian units. Π_em = ω²(1−ε^T) = −iωσ: CHECKED.
- l.145–147 ε^{αβ} from the minimal coupling (p+eA)²/2m_e: signs redone (J = −e × particle current, A = −iE/ω). CHECKED. The free-electron limit 1 − ω_p²/ω²: CHECKED.
- l.153 Eq. 4.4-ward ω²R_ee = 𝓃_eq²/m_e + q_αq_βR_jj: CHECKED independently from the Lehmann form with ω²/(ω∓ω_fi) = ω ± ω_fi + ω_fi²/(ω∓ω_fi). The longitudinal projection gives ε: CHECKED.
- l.165–175 Thomas–Fermi: δ𝓃 = −2𝒩_Fφ and k_TF² = 2e²𝒩_F = 4αm_ek_F/π = 3ω_p²/v_F². All three forms agree (4117.0 eV): CHECKED. Yukawa α e^{−kr}/r: CHECKED. Hochberg (S.14), ω_p = λ_TF v_F/√3: CHECKED.
- l.178–180 TF numbers (WE 4.6):
  - 𝒩_F = 9.24×10⁷ eV², k_TF² = 1.695×10⁷ eV², k_TF = 4.12 keV, 1/k_TF = 0.479 Å (a fifth of 2.35 Å): CHECKED.
  - ε_TF(q₀) = 2.219, squared 4.92: CHECKED.
  - k_TF/k_F = 1.153: CHECKED.
  - Crossover 1.259 keV, at 1/q = 1.57 Å: CHECKED (but see the notation note on 1/q vs 2π/q).
- l.187–191 stopping: |Ṽ|² = Z₁²e⁴/q⁴, the measure 2πq²dq du and Eq. 4.4-dEdx (both prefactors): CHECKED. The fast limit is Bethe's 4πZ₁²α²𝓃_e/(m_ev²)·ln: CHECKED. Dimensions eV² = energy/length: CHECKED.
- l.199–212 single oscillator (WE 4.7):
  - L form: CHECKED.
  - ∫ωL = (π/2)ω_p² and ∫L/ω = (π/2)ω_p²/ω_res² (numerically 1.000000): CHECKED.
  - ε resonance Ē/√ε∞ = 5.077 eV and ε(0,0) = ε∞: CHECKED.
  - Peak height ω_p²/(Γ_wĒ) = 4.339: CHECKED.
  - S first moment, S^st = q²/(2m_eω_res): CHECKED.
- l.214–218 slow-particle stopping:
  - min ω_res/q = (Ē/m_e)^{1/2} = 5.83×10⁻³ at q = 4.21 keV: CHECKED.
  - ∫x²/(1+x⁴)² = π/(8√2) (sympy) and the prefactor 1/6: CHECKED.
  - 0.181 eV/Å at v = 10⁻³. Full integral 0.1857 (+2.7%) and +22.4% at v_max: CHECKED.
- l.220 model L(3 eV) = 0.0353, 11.3× the data: CHECKED.

## s4-5 (electron gas)
- l.5 r_s = 2.005, ω_p/E_F = 1.332, k_TF/k_F = 1.153, k_TF²/k_F² = 0.6634 r_s: CHECKED.
- l.9–14 Eq. 4.5-R0: Pauli factors cancel to n_k − n_{k+q}. CHECKED.
- l.19–22 Eq. 4.5-lindhard: CHECKED (see D.8). Same as Hochberg (S.13) and Knapen (17)–(18) at Γ = 0.
- l.24–28 branch, the two Im forms (= −½ S⁰ forms): CHECKED.
- l.32–36 Eq. 4.5-static: F_L(0) = 1, F_L(1) = ½, large-q form 4k_F²/3q² (expanded): CHECKED.
- l.36–42 R⁰ = 𝓃_e⟨2Δ/(z²−Δ²)⟩ and Eq. 4.5-moments: ⟨Δ⟩, ⟨Δ³⟩, ⟨Δ⁵⟩ by sympy and ⟨k²u²⟩ = k_F²/5, ⟨k⁴u⁴⟩ = 3k_F⁴/35: CHECKED.
- l.55 RPA content: no derivation; consistent.
- l.59–61 ε_Lin(q,0) and F_L = 1 − q²/12k_F²: CHECKED. ε_Lin(q₀,0) = 2.101 and |ε|² = 4.415: CHECKED.
- Limit box TF (Fig. 4.tf-limit): 2% at q = 0.487k_F and 10% at 1.062k_F: CHECKED. Above 2k_F the term falls as 1/q⁴: CHECKED.
- l.74 perfect screening:
  - Induced density −(1−1/ε)φ/v_C: CHECKED.
  - 1−1/ε at 0.1k_F = 0.99253; the RPA inverse moment, continuum plus plasmon, is 0.99253 (agrees to 3×10⁻⁷): CHECKED.
  - 1−1/11.7 = 0.9145 ("0.915"): CHECKED.
- l.80 slab argument (HL, E = e𝓃_eu): CHECKED.
- l.84–93 Eq. 4.5-dispersion: CHECKED (known item).
- l.95 3T/m_e analogue, ⟨k²u²⟩/m_e² = v_F²/5, α_pl = (3/5)E_F/ω_p = 0.451: CHECKED.
- Limit box plasmon (Fig. 4.plasmon-limit). Exact RPA zero from Eq. 4.5-lindhard:
  - q_c = 0.7297k_F = 2.605 keV with ω_+(q_c) = 24.84 eV: CHECKED.
  - The quadratic formula is within 1% for q < 0.388k_F: CHECKED.
  - ω_p/v_F = 0.6656k_F, 8.8% low: CHECKED.
  - Kahn–Lin Eq. (171) and the text after it (ω² ≈ ω_p² + 3q²v_F²/5, q_c ≃ ω_p/v_F): CHECKED.
  - **WRONG.** "there the q⁴ term reduces the error to below 3×10⁻⁴". The q⁴-formula error is −3.0×10⁻⁵ at 0.2k_F, −3.3×10⁻⁴ at 0.3k_F and −1.54×10⁻³ at 0.39k_F. It is below 3×10⁻⁴ only for q < 0.295k_F. Correction: "there the q⁴ term reduces the error to below 1.6×10⁻³ (below 3×10⁻⁴ for q < 0.30k_F)".
- l.110–117 plasmon residue:
  - Eq. 4.5-plasmonL and the q → 0 limit (π ω_p/2)δ: CHECKED.
  - Both sum rules exhausted at q → 0: CHECKED.
  - S = (πq²ω_p/e²)δ and S^st = q²/(2m_eω_p): CHECKED.
  - At 0.1k_F, 7.51×10⁻³ vs 7.5×10⁻²: CHECKED.
  - Plasmon share 1−3.6×10⁻⁵ at 0.1k_F and 0.9566 at 0.5k_F. Continuum plus plasmon = (π/2)ω_p² to 3×10⁻⁷: CHECKED.
- l.119 q_c and ω_pl: CHECKED as above. Fig. 4.6 caption: plasmon at 0.3k_F = 17.652 eV: CHECKED.
- Fig. 4.6b, Mermin vs naive at γ = 1 eV, 0.3k_F: FWHM 1.06 vs 2.00 eV ("twice as wide") and maximum tail ratio 1.72 ("up to 1.7"): CHECKED.
- l.128–130 q_c… ω_p/v_max = 6.27 keV = 1.755k_F: CHECKED.
  - Corner L ≃ e²m_e²qω/(2πk_TF⁴): CHECKED.
  - Informational: Kahn–Lin Eq. (169) writes Re ε ≈ λ_TF²/2q², which makes their (170) four times this. The book is right (Re ε → k_TF²/q²) and does not cite Kahn there.
- l.132 q₀v_max = 9.88 eV: |ε_Lin|² = 3.963 and L = 0.1833: CHECKED.
- l.139 Eq. 4.5-mermin: CHECKED against Knapen Eq. (19) and Kahn–Lin Eq. (168) (Γ, Γ_p). The γ → 0 limit: CHECKED.
- l.144 **GAP (causality, known item, open).** "Since R⁰(z+iγ) is analytic, the Mermin response is causal" is not sufficient: the denominator ω + iγR⁰_γ/R⁰_st could vanish for Im z > 0. Supply in D.9 (or 4.5) the following argument.
  - The relaxation equation is linear and time-invariant. With w_k = (n_k−n_{k+q})/(ξ_{k+q}−ξ_k) ≥ 0, the norm F = Σ_k|δϱ_k|²/w_k obeys, for the homogeneous equation, dF/dt = −2γ_rel[Σ|δϱ_k|²/w_k − |Σδϱ_k|²/Σw_k] ≤ 0 (Cauchy–Schwarz).
  - Modes with w_k = 0 decay at rate γ_rel.
  - No free mode grows, so R^Mer has no pole with Im z > 0. The point z = 0 is removable, since numerator and denominator are both ∝ iγ/z.
  - Numerical support: a grid scan of |z + iγR⁰(z+iγ)/R⁰(0)| over the upper half plane (q = 0.3 and 1.2k_F; γ = 0.1, 1, 3.66 and 20 eV) finds no zero. The minimum is iγ at the z → 0 edge.
- l.148 static limit ε_Mer → ε_Lin(q,0) = 15.67 vs naive ε_Lin(q,iγ) = 12.83 at 0.3k_F, 1 eV: CHECKED.
- l.150–153 Drude limit and σ = ω_p²/(γ−iω); naive → 1 + ω_p²/γ²: CHECKED.
  - f-sum at γ = 1 eV, q = 0.3 and 1.2k_F: Mermin −1.4×10⁻⁷ and −6×10⁻¹⁰; naive 5×10⁻⁸ and −4×10⁻⁹. CHECKED (< 2×10⁻⁵).
- l.157–159 Drude L: CHECKED against Kahn–Lin Eq. (172). The tail γω/ω_p², naive poles ±ω_p−iγ, and twice the width and tail: CHECKED.
- l.163 Knapen Eqs. (20)–(21) (A_i rescaled for the f-sum, θ(ω−ω_edge)): CHECKED.
- l.168 zero 1.88% above 16.30 eV ("1.8 percent"; 1.9 is the closer rounding). Consider 1.9.
- l.170 87% (0.869) below 16.30 eV at rms 6.46 eV: CHECKED.
  - (ω_i/ω)² = 0.16: CHECKED.
  - Slope at the zero: 0.127 by pointwise gradient, 0.129 by a ±0.3 eV fit, printed 0.128. The gas value 2ω_p²/ω³ = 0.1274: CHECKED.
  - 9.41% between 16.3 and 40 eV: CHECKED.
- l.172 ε₂ at the zero = 0.224: CHECKED.
  - Width 2ε₂/slope = 3.5 eV from the data (3.44 from the printed 0.22 and 0.128; print ε₂ = 0.224 or the width as 3.4–3.5).
  - Mermin peak ω_p/γ = 4.537: CHECKED.
  - L(3 eV) = 0.0425, 13.7× the data: CHECKED.
- l.174 Kahn–Lin: "FEG describes the DM-electron spectrum for ω ∈ [5,15] eV in Si and Ge quite well": CHECKED.

## Appendix D.6–D.9
- D.6: Eqs. D.6-shift and D.6-dc (second difference) and the current identity ½{p,A} = A(p+q/2): CHECKED. Eqs. D.6-species, D.6-charge and the 2.73×10⁻⁴ ratio: CHECKED. Eq. D.6-NL and its small-q form −[q·r,[q·r,V_NL]], plus the velocity commutator: CHECKED. SO-ordering argument (ε_{γαβ}∂_α∂_βU = 0), the mass–velocity expansion and the virial K̄ = −E/Z: CHECKED.
- D.7: Eq. D.7-dyson, the push-through identity and Eq. D.7-eps: CHECKED. Eqs. D.7-mac and D.7-head (Schur): CHECKED. R⁻¹ = R̄⁻¹ − v₀, the closed head equation and Eq. D.7-macbar: CHECKED. Small-q orders (head finite, wings 1/q × q): CHECKED. Metal limit: CHECKED. Symmetrized similarity v^{−1/2}εv^{1/2}, off-diagonal factor |q+G|/|q+G′|, finite wings: CHECKED. Knapen footnote 3: CHECKED. The "single wavevector removed from the Hamiltonian" equivalence is the known 4.8 item.
- D.8: Relabelling, angular integral and branch (Im w > 0 ⇒ ratio in the lower half plane): CHECKED. Prefactor m_ek_F²/2π²q and the antiderivative of κ ln[(w+κ)/(w−κ)] (sympy): CHECKED. Eq. D.8-Rz assembly: CHECKED. Eqs. D.8-Re and D.8-Im, the step regions, both Im forms and ν₊² − ν₋² = 2m_eω/k_F²: CHECKED. Eq. D.8-static: CHECKED. Eq. D.8-smallq (𝓘′ = 2 − wℓ) and its Im = −πN_Fω/qv_F = −m_e²ω/2πq: CHECKED. 𝓘 series (2/3)w⁻¹ + (2/15)w⁻³ (sympy) and Eq. D.8-highfreq: CHECKED. Parabolic f-sum −q²k_F³/6πm_e: CHECKED. Numerical f-sum at 0.4 and 1.0k_F: reproduced to < 10⁻¹⁴. The complex-z quadrature check was not reproduced.
- D.9: Commutators of c†_kc_{k+q} with H₀ and with n_e(q), and the equation of motion: CHECKED. Static local-equilibrium solution and Eq. D.9-condition: CHECKED. Partial fractions, the δ𝓃 equation, Eq. D.9-R and Eq. D.9-eps (matches Mermin's form, Knapen (19) and Kahn (168)): CHECKED. Continuity: −D_k = q·(k+q/2)/m_e, the current matrix element and Eq. D.9-continuity: CHECKED. Limits (static, Drude, perfect screening, large-ω tail): CHECKED. Numerical f-sum at γ = 0.1E_F, q = 0.5 and 1.5k_F: Mermin 1.5×10⁻⁷ and 5×10⁻¹²; naive 7×10⁻⁸ and 2×10⁻⁹ (< 10⁻⁴). CHECKED. Causality: the GAP above. D.9 is the natural place for the Lyapunov argument.

## Appendix C.5–C.7
- C.5: Eqs. C.5-Rz and C.5-spectral (ϱ_R = −Im R/π, sign by frequency): CHECKED. Eq. C.5-highfreq with ∫ω′ϱ_R = 𝓃_eq²/m_e via the full-line fold, which gives 2∫ωS: CHECKED. KK derivation and Eq. C.5-KK, with ½R(ω) from the δ: CHECKED. Eq. C.5-KKhalf (both, including the 2ω/π of the second): CHECKED. Eq. C.5-screening: CHECKED. Eq. C.5-KKeps and the large-ω route to ∫ωε₂ = (π/2)ω_p²: CHECKED. Matsubara residues T and −T, Eq. C.5-matsum (signs), and the oscillator example (2n_B+1)/2ω₀ (= ⟨x²⟩M): CHECKED.
- C.6: Gaussian, Fresnel e^{iπ/4}, FT e^{−q²s²/2}, moments, Isserlis: CHECKED. Hadamard and BCH (both forms): CHECKED. D(α) normal form, D†dD = d+α, e^{iqx} = D(iqℓ₀): CHECKED. Poisson weights and mean ω₀|α|² = q²/2M: CHECKED. √(2Mω₀) = 55.9 keV for 60 meV and M = 26.06 GeV: CHECKED. Eq. C.6-normal and ⟨0|…|0⟩ = e^{η²/2}: CHECKED. Eqs. C.6-bloch and C.6-product (A = −iq·u(t), B = iq·u(0) give e^{−2W}·e^{⟨…⟩}): CHECKED.
- C.7: PSD equivalences and the diag(0,−1) counterexample: CHECKED. Eq. C.7-CS and the outer-product form of S_ab: CHECKED. Block factorization and Eqs. C.7-block, C.7-head: CHECKED. Eq. C.7-partition (E − Schur complement): CHECKED. Dyson X⁻¹ = X₀⁻¹ − K and the right-hand form: CHECKED. Woodbury bracket identity: CHECKED. Boson Bogoliubov: operator identities redone, tanh2θ = g₀/ω₀, Eq. C.7-Eboson; the numbers 0.8, −0.2 and sinh²θ = 0.125; η·h eigenvalues: CHECKED. Fermion: all four expansions redone, tan2θ = g₀/ξ₀, constant ξ₀ − E_f, Eq. C.7-Efermion: CHECKED.

## Not reproduced
- Fig. 4.3b caption: "KK reconstruction agrees to better than 10⁻¹¹λ²/ω₀". This depends on the quadrature method, so it was not rerun. The ω = 0 value −2λ²/ω₀ is CHECKED.

## NOTATION and STYLE drift (new; one line each)
- s4-1 ll.128–156 and Fig. 4.1 caption: upright `\Gamma_{\mathrm{w}}`. STYLE (2026-11-02) and NOTATION require `\varGamma_{\mathrm{w}}`, which s4-3 and s4-4 already use.
- s4-1 l.124 and s4-2 l.84: bare n_B (no argument) for n_B(ω₀). NOTATION entry 403 reserves the bare n_B for the BO order. Write n_B(ω₀).
- s4-1 l.63: bare η for the switching rate, and s4-3 l.142: bare η for the Coulomb (Sommerfeld) parameter. NOTATION allows only η(v_min), η_anh and η_b. Use η_b (or 0⁺) for the switching rate and rename the hydrogen parameter (e.g. η_C).
- s4-1 l.63: τ = t − t′. Entry 43 reserves τ for imaginary time. Use s or t″.
- D.8: κ = k/k_F. Entry 12 makes κ the species index only. Rename (e.g. k̃).
- s4-5 and D.8: ν, ν_± as reduced frequency. ν is the phonon branch (NOTATION l.338). Rename (e.g. ϑ, ϑ_±) or add a local-variable row.
- y has two meanings: Im z in 4.1 and C.5, and q/2k_F in 4.5 and D.8. Not in NOTATION; also clashes with y edge (15.2) and y_χ, y_e. Add a local-variable note or rename one of them.
- Bare u for the angle cosine (4.2, 4.4, 4.5, D.8): not in NOTATION (u_Rκ is the displacement). Add it as a local variable.
- α_pl (4.5 l.95) and Ē (4.4): not in NOTATION. Propose rows; the editor already moved the Ē rows to 4.4.
- Length conventions: 4.2 l.29 quotes 2π/q₀, while 4.4 l.180 quotes 1/q (1.6 Å; 2π/q would be 9.9 Å). State which one is meant at each use.
- Factor-of-2, π and sign conventions (Fourier e^{+iωt}, ε⁻¹ = 1 + v_C R, S normalization 2π/V, f-sum π over the full line, k_TF² = 2e²𝒩_F with 𝒩_F per spin): consistent throughout against NOTATION and A.7. No drift found.
