# Ch. 3 batch review: derivation check (isolated)

Scope: tex/ch03/s3-1…s3-6, appC/C-1…C-8, appD/D-4, D-5. Verdicts: CHECKED / WRONG / GAP (with correction) / FIG-PASS (number from Figs. 3.6, 3.7, 3.8, 3.11, 3.12 or the 3.6 Wannier spreads and interpolation errors; not checked).
Method: every non-definitional step redone by hand and, where it involves algebra, with sympy or numpy (scratch scripts chk1, nfe, epm, w1d, misc, sym; nothing heavy, no QE). The 1D nearly-free-electron model (25 PW), the Cohen–Bergstresser Si model (113 PW), the two-band chain and the Fig. 3.9/3.10 atomic numbers (copies of figscripts/ch03 re-run on the stored ld1 output, figure output redirected to scratch) were recomputed. Sources: sources/review-ch03/ (text only; PDFs deleted).
Dimensions: every displayed result was checked. All are consistent in natural units (ħ = c = k_B = 1, e² = 4πα). No dimensional errors were found; the ones that needed care are listed at the end.

## Summary of findings (details below)
- WRONG: C.4 sign in the intermediate display of d PV/dx (the result is right); 3.6 claim about the wannier90 Si example; 3.3 sum-rule decomposition ("single valence band", 2.9e-3, 2.27); WE 3-Zalpha 0.27 % → 0.26 %; WE 3-w1d 4.8 → 4.7 meV. (Kane 0.0718: a precision issue for the figure pass, not WRONG.)
- GAP: 3.5 eq:3.5-rhoAE normalization; 3.3 empirical-pseudopotential inputs not stated; 3.3 says Figs. 3.6/3.7 are DFT, but the caption of 3.7 says empirical pseudopotential; WE 3-scales uses E_g = 1.11 eV; C.3 T_d vs O_h; WE 3-w1d "0.36 eV a" depends on the random draw; 3.3 lattice-constant labels (see known items); several NOTATION drifts.
- Editor-requested checks: the diamond (200)/(222) claim is CHECKED (symmetrized numerically). The 3.6 sp³ orientation is FIG-PASS, but independent evidence from the wannier90 tutorial benchmark is given (it supports the text's ordering).

## §3.1
- l.3–5: 2.14e25 atoms/kg, M/m_e = 5.12e4: CHECKED.
- eq:3.1-R … eq:3.1-BZvol: CHECKED (sympy: b₁ = (2π/a)(−1,1,1), Ω = a³/4; the triple-product identity and its sign bookkeeping in the unnumbered display; (2π)³/Ω).
- eq:3.1-bfcc and the parity rule h+k = 2m₃ etc.: CHECKED. Numbers: 2π/a = 2283 eV = 1.157 Å⁻¹, |G₁₁₁| = 3.954, |G₂₀₀| = 4.566 keV, a = 2.752e-3 eV⁻¹, Ω = 40.05 Å³, d_nn = 2.352 Å, 8/a³ = 4.99e22, ρ = 2.329 g cm⁻³, 32/a³ = 2.00e23: CHECKED.
- Fig. 3.2 caption and l.101–103: Γ–X, L, K, W = 1, 0.866, 1.061, 1.118 (2.28, 1.98, 2.42, 2.55 keV); the octahedron |k_x|+|k_y|+|k_z| ≤ 3/2; K is the hexagon–hexagon edge midpoint; equal-volume sphere 0.985(2π/a) = 2.25 keV: CHECKED.
- l.49: LDA a = 5.401 Å, 0.5 % below, Poncé Sect. 10.2: CHECKED (source: 10.207 vs 10.262 bohr, LDA-PZ = 5.401 vs 5.430 Å, 0.54 %).
- eq:3.1-crystalmomentum, eq:3.1-kgrid, eq:3.1-latticesum (geometric sums), counting: CHECKED.
- l.141: N = 1.07e25 cells/kg; Fermi sphere 4^{1/3}×2.25 = 3.57 keV = (3π²·0.2 Å⁻³)^{1/3}; q₀ = 3.73 keV = 1.66 ≈ "1.7" × 2.25 keV: CHECKED. Essig Sect. 4.1 (8 electrons, 4 valence bands): CHECKED.
- Unnumbered matrix-element display and eq:3.1-selection: CHECKED (T n_e(q) T⁻¹ = e^{iq·R} n_e(q) with (TΨ)(r) = Ψ(r+R)).
- l.161: "|q| > 2|ΓW| ⇒ always Umklapp": CHECKED (|k_i+q| ≥ |q| − |ΓW| > |ΓW|).
- Fig. 3.3 caption: |q| = 5.150 keV, |q_r| = 1.229 keV, G_q = (2,0,0) is the nearest vector (the (1,1,±1) candidates are at 1.64), q_r is inside the zone, 2m_χv_max = 5.30 keV, v_max = 2.6502e-3: CHECKED.
- WE 3-scales: 0.419 keV = 0.18(2π/a); q_max = 4.84/52.6/530 keV = 2.12/23.0/232 (2π/a); lower end 0.46 → 0.42 keV; q₀ = 1.63(2π/a); ball estimate 1.31e4 / 1.31e7: CHECKED.
- WE 3-scales "a direct count gives 13106": GAP (fragile). The direct count is 13107 at q = 53.000 keV and 13323 at q = 2m_χv_max = 53.003 keV: the shell |G|² = 539(2π/a)², with 216 vectors, sits on the boundary, and 13106 equals the volume estimate. Correction: "a direct count gives 1.31e4 as well", or drop the parenthesis.
- WE 3-scales uses E_g = 1.11 eV: GAP (convention drift against the 1.17 eV ruling, §3.3). Correction: use 1.17 eV (q ≥ 0.44 keV = 0.19(2π/a), q_max(1 MeV) = 4.81 keV, lower end 0.49 keV; the 10 and 100 MeV values are unchanged to the digits shown), or say explicitly that this is the 1.11 eV of WE 1-mmin.
- eq:3.1-fG, eq:3.1-Sbas and the convention f_G = Ω⁻¹∫e^{iG·r}f (A.3): CHECKED (sign consistent with A.3).
- WE 3-diamond: S^bas = 1 + e^{iπ(h+k+l)/2}; (111) gives 1 − i; (220) and (400) give 2; (200) and (222) give 0; the GaAs factor is 31 − 33 = −2 against 64, ratio 4/4096: CHECKED.
- Editor item "(200) vanishes by the glide, (222) returns through the bond charge": CHECKED independently. A random set of lattice-periodic Fourier components (all-even and all-odd G with |hkl| ≤ 3) was symmetrized over Fd-3m, written as T_d (origin on atom 1) plus inversion through the bond centre, i.e. r → τ₂ − r times T_d. Then |f₂₀₀| = 9e-17 (it vanishes identically: the T_d orbit of (2,0,0) is all six vectors, and the second coset carries the phase e^{iG₂₀₀·τ₂} = −1), while |f₂₂₂| = 0.52 and |f₁₁₁| = 0.29 are nonzero: (222) is only a site extinction.
- l.218: the four-point simple-cubic structure factor: CHECKED.

## §3.2
- eq:3.2-He … eq:3.2-Hk, the periodicity of the bands, eq:3.2-pw ("c_nk(G) is the A.3 component at −G times Ω^{1/2}"): CHECKED.
- eq:3.2-central: CHECKED (G″ = G′ − G; hermiticity from U_{−G} = U_G*).
- eq:3.2-twowave, eq:3.2-epm, eq:3.2-gap: CHECKED (sympy eigenvalues). The limit far from the plane: CHECKED. The second-order shift Σ|U_G|²/(ε⁰_k − ε⁰_{k−G}): CHECKED.
- l.79: the standing waves (cosine lower for U_G < 0) and zero slope on the Bragg plane: CHECKED.
- Fig. 3.4 caption: gaps 0.998 eV and 96 meV; 2|U|/v_max = 0.38 keV: CHECKED (25 PW, |j| ≤ 12).
- WE 3-gap1d: ε⁰ = 1.275 eV, edges 0.775/1.775, full 0.752/1.749, gap 0.998; 9×1.275 = 11.47; U²/(ε⁰_k − 9ε⁰_k) = −0.025; second gap 5.099 eV, 0.049, 0.098 vs full 0.0964; |ψ|² of the lower state is zero at a/2 and of the upper state at 0 (exact by parity plus the Bloch condition): CHECKED.
- WE 3-gap1d "both edges moved down by 0.024 eV": WRONG (minor). The full calculation gives 0.023 (lower) and 0.026 eV (upper). Correction: "by 0.023 and 0.026 eV".
- l.100: |G₁₁₁|²/8m_e = 3.82 eV: CHECKED.
- eq:3.2-blochsum, eq:3.2-HS, eq:3.2-LCAO, eq:3.2-TB, eq:3.2-fcc: CHECKED. Γ: −12t; L: 0; X and the whole X–W line: +4t (cxcy+cycz+czcx = −1 there); K: 3.657t (Fig. 3.5); bandwidth 16t; m* = 1/(2ta²): CHECKED.
- eq:3.2-hybrids: orthonormal, along the four bond directions from τ₁ (verified against the neighbours τ₂ − a_i); on-site energy (E_s+3E_p)/4: CHECKED.
- Density vertex: both unnumbered displays, eq:3.2-rho (periodic gauge u_{m,k+q} = e^{−iG_U·r}u_{mk′}), eq:3.2-rhopw, eq:3.2-closure, eq:3.2-ne: CHECKED. Essig Eqs. (3.14)–(3.17): CHECKED against the source (u_i(k+G) normalization, f_[ik,i′k′,G′]).
- eq:3.2-pv, eq:3.2-r (−i v_mn/(ε_m−ε_n)), eq:3.2-dHk, eq:3.2-vg, eq:3.2-dudk, eq:3.2-optical (with v*_nm = v_mn), eq:3.2-validity: CHECKED.
- l.266: v_F = 7.0e-3: CHECKED. l.268: Ismail-Beigi Fig. 1, "15 % to 20 %" for diamond: CHECKED.
- WE 3-vertex: q/448 eV; v₂₁ = 2.234e-3 (two-wave) and 2.244e-3 (full); |ρ₂₁| = 0.0225/0.0225 at 10 eV, 0.210/0.225 at 100 eV, 0.496/0.849 at 377 eV (ratio 1.71; squared 2.93); the transition deposits 1.62 eV and needs q ≥ 0.611 keV; Umklapp 0.5 vs full 0.501; |ρ_m1|² = 0.298, 0.251, 0.226, 0.225; closure to 4e-16; |v₂₁| = 0.85v_max: CHECKED (25 PW, periodic gauge with the G index shifted by G_U).

## §3.3
- eq:3.3-Eg, eq:3.3-Edir, eq:3.3-kc: CHECKED. "85 percent of the way to the face", 1.94 keV = 0.98 Å⁻¹, photon momentum/k_c = 6.0e-4: CHECKED.
- Gaps (cited): Si 1.1692 eV (Ramanathan Eq. (11): E_g(0) = 1.1692): CHECKED. 1.12 at 300 K and Ge 0.66, GaAs 1.52/1.42 (Lucero Table I): CHECKED. Si E_dir 3.4 (Rideau Table II, Γ15); E₁(L) 3.45 (Table VI); Ge E_g 0.744 (Table VI, L1); Ge E_dir 0.89 (Table II, Γ2′); Δ_SO 0.044/0.296 and G₀W₀ 0.0499/0.312 (Table II); Hensel masses 0.9163/0.1905 and Ge 1.588/0.08152 (Table VII); Luttinger parameters Si (4.285, 0.339, 1.446) and Ge (13.25, 4.20, 5.56) (Table VII): CHECKED against cond-mat/0607510.
- GaAs L/X 1.815/1.981, 0.30/0.46 above; Δ_SO 0.341; m* 0.067; Luttinger (6.98, 2.06, 2.93): CHECKED against the standard Vurgaftman values (paywalled, not fetched). n = 3.42 → ε∞ = 11.70 (Li 1980, paywalled): CHECKED arithmetic. Feher 0.85: standard value, not fetched.
- Lattice constants, l.33/35 and Table 3.1 (known item): Lucero Table II does list Ge 5.658 and GaAs 5.648 as "0 K" values, so the text matches its source. Note, however, that Lucero's Ge "0 K" 5.658 is the usual room-temperature value. Under the editor's ruling (room temperature throughout): Ge 5.658 stays, relabelled as room temperature; GaAs becomes 5.653 Å (Vurgaftman 2001, 5.65325 Å at 300 K, which is already cited), so a room-temperature source is in hand; Si stays at 5.431 (CODATA). The Table 3.1 caption must be changed with them.
- l.44: GAP (internal consistency). "The bands in Figs. 3.6, 3.7 come from density-functional theory", but the caption of Fig. 3.7 says Cohen–Bergstresser empirical pseudopotential, and the sentence "A first-principles calculation obtains them from DFT, which yields the potential from the electron density (§3.4)" repeats the opening sentence. Resolve this together with the figure ruling for 3.6/3.7.
- Si EPM check, l.102: GAP (inputs). The book never states the Cohen–Bergstresser form factors (they are in figscripts/ch03/epm.py l.10, 29). Correction: state V_S(3, 8, 11) = −0.21, +0.04, +0.08 Ry, τ = ±(a/8)(1,1,1), and the basis |G|² ≤ 20(2π/a)², which gives exactly 113 plane waves. With these inputs (recomputed): k_c = 0.853(2π/a), m∥ = 0.872, m⊥ = 0.184, and the sum over all 113 bands gives 0.8724/0.1844, matching the finite differences to four digits: CHECKED. The gap is 0.82 eV.
- l.102, "the light transverse mass comes mostly from a single valence band, 3.73 eV below, with a velocity matrix element of 2.9e-3 …; that one term contributes 2.27 of the total m_e/m*⊥ = 5.43": WRONG. The valence level 3.73 eV below the minimum is the doubly degenerate Δ5 pair. Its total contribution along one transverse axis is 4.53 of 5.42, with Σ|v|² = (4.07e-3)². The split 2.27 + 2.27 (|v| = 2.9e-3 each) holds only in a basis of the pair rotated by 45° about the valley axis; in the basis aligned with y and z it is 4.53 + 0. The writer's check (figscripts/ch03/fig3_6.py l.141–147) takes the largest single-band term from the eigh basis of the pair, which explains its 2.27. Correction: "… comes mostly from the doubly degenerate valence level 3.73 eV below the minimum, whose two states together contribute 4.53 of the total m_e/m*⊥ = 5.43, with Σ|v^y|² = (4.1e-3)²."
- eq:3.3-ni: CHECKED (Boltzmann integral (mT/2π)^{3/2}; √(np)). m_dc = 1.064, m_dv = 0.5005 (spherical average from (γ₁ ∓ 2γ̄), γ̄ = (2γ₂+3γ₃)/5): CHECKED. n_i = 6.1e9 cm⁻³ (300 K), 1.0e-20 (77 K), 2e-721 (4 K); 429 cm³: CHECKED.
- eq:3.3-kp, eq:3.3-mass (symmetrized Re[v^α_nm v^β_mn]), eq:3.3-valley: CHECKED. Aspect ratios 2.19 and 4.4 (Ge ratio 19.5): CHECKED.
- Kane energy definition E_P = 2m_e|v|² and eq:3.3-kane2: CHECKED.
- l.120, "E_P = 18.3 eV and gap 1.42 eV … predicts m* = 0.0718": FIG-PASS follow-up (printed precision). With the printed inputs, 1/(1 + 18.3/1.42) = 0.0720; 0.0718 needs E_P = 18.36. Print E_P to that precision, or give 0.072.
- Gawarecki Table VIII: GaAs E_P0 = 22.911 eV; range 16.4 (InP) to 22.9 eV across B/Al/Ga/In P/As/Sb: CHECKED (note: the source's E_P0 is the 30-band parameter). |v| = 4.73e-3 = 1.79v_max: CHECKED.
- eq:3.3-HSO, the L·S values, the 3/2 ξ splitting and the zero weighted mean; H 2p: ξ = α⁴m/48, splitting α⁴m/32 = 4.53e-5 eV = 0.365 cm⁻¹: CHECKED (sympy for the 1s/2p radial averages).
- NIST ASD (sources/3.3 copies): Si⁺ 287.24 cm⁻¹ = 35.6 meV (787× H, "800"); Ge⁺ 1767.36 cm⁻¹ = 219.1 meV (6.15×); As²⁺ 2940 cm⁻¹ = 0.3645 eV; Ga 826.19 cm⁻¹ = 0.1024 eV: CHECKED. Ratios 6.7 and 6.2; "30 %" (1.24 and 1.35): CHECKED.
- eq:3.3-DSO: CHECKED as a statement. Δ_SO/3 = 15 meV (1.3 %) and 0.099 eV (13 %): CHECKED.
- j = 3/2 projector (2/3)(1+L·S), weights 2/3 and 1/3, eq:3.3-kaneSO: CHECKED. m* = 0.0660, 0.0246, 0.0755: CHECKED.
- eq:3.3-holes: CHECKED, including both limits ([100]: γ₁ ∓ 2γ₂; [111]: the root equals γ₃κ²). All twelve hole masses in Table 3.1: CHECKED (0.277/0.718, 0.201/0.139; 0.206/0.469, 0.046/0.041; 0.350/0.893, 0.090/0.078).
- eq:3.3-Emin, periodicity, the q = 0 value E_dir, minimum E_g: CHECKED. eq:3.3-Eminpar (k = −m_hΔq/(m∥+m_h)): CHECKED. 1.196 m_e and 0.350 keV for 0.1 eV; |G₂₀₀| − k_c = 2.63 keV: CHECKED.
- l.175: 1.26 eV near 3.1 keV, 2.13 eV: FIG-PASS. eq:3.3-allowed: CHECKED.
- WE 3-kc: 2650 ± 2164 eV → 0.49–4.81 keV; 5.14 − 1.88 = 3.26 eV; 0.474 MeV; m_min = 0.333 MeV at 0.88 keV = 0.39(2π/a); image |k_c − G₂₀₀| = 2.63 < 5.30 keV: CHECKED. "About 1.9 eV in Fig. 3.6(b)": FIG-PASS.
- WE 3-mmin: 0.968 MeV/2.57 keV; 0.253 MeV/0.67 keV; 0.212 MeV/0.56 keV; 36 % below Si; |ΓL|(Ge, a = 5.658) = 1898 eV, 5.03 eV, 0.420 MeV: CHECKED.
- Fig. 3.6 and 3.7 captions and l.44/l.102 PBE values (0.843, 0.557, 2.56, 2.70, 0.61 scissor, 3.17, 0.95/0.193; Ge/GaAs model energies): FIG-PASS. For the re-check: the PBE numbers in §3.3/3.4 mix lattice constants, e.g. l.44 quotes k_c = 0.843 (measured a) beside m∥ = 0.95 (E.1: relaxed a), and the caption of Fig. 3.12 has 0.85.

## §3.4
- l.3: 0.52 eV → 0.148 "0.15 MeV": CHECKED.
- eq:3.4-HF and the Σ_x display (same spin through x, Heaviside–Lorentz e²/4π): CHECKED (see D.4).
- l.22: ε_x = −6.22 eV, (3/5)E_F = 7.48 eV, free bandwidth 12.47 → 20.77 eV: CHECKED.
- eq:3.4-HK, eq:3.4-LDA, eq:3.4-KS: CHECKED (see D.5). v_x = (4/3)ε_x = −8.29 eV: CHECKED. HSE has 1/4 short-range Fock exchange: CHECKED.
- l.66: a = 5.477 (+0.85 %), k_c = 0.840, gaps 0.602/0.557, ε∞ 13.04, m∥ 0.95: CHECKED for consistency with E.1 (these are not Fig. 3.6 values: E.1 gives 0.840 and 2.55 at the relaxed a).
- eq:3.4-fundgap (I − A = E_{N+1} − 2E_N + E_{N−1}), eq:3.4-gap: CHECKED.
- l.84: LDA 0.52 (Aryasetiawan Table I: Si LDA 0.52, GW 1.29/1.24/1.25, exp 1.17): CHECKED. GaAs LSDA 0.43 and Ge 0.00 (Lucero Table I): CHECKED. Figure values (0.54, 0.84, 0.53–0.64): FIG-PASS.
- l.93: GW 1.24–1.29 (Aryasetiawan Table I); 1.10 converged (Klimeš Sect. IV C, "1.10 (Si)"); HSE 1.22 (Lucero Table I, HSE column): CHECKED. 1/ε∞ ≈ 1/12: CHECKED.
- eq:3.4-scissor, the ∇_kH^s display, the c–v, c–c′ and v–v′ elements, eq:3.4-vscis: CHECKED (each step redone; ⟨∇u_c|u_v⟩ = −⟨u_c|∇u_v⟩).
- l.105: Δ_scis = 0.568/0.613 eV: CHECKED. Scissor accuracy 0.1/0.2/0.4 eV (Aryasetiawan Sect. V B, quoting Godby 1988): CHECKED.
- l.132: 3.12/2.55 = 1.22, square 1.50: CHECKED; the pairing is consistent (both at the PBE lattice constant, E.1).
- l.134: excess of the f-sum rule Δ_scis Σ_c|ρ_cv|²: CHECKED.
- WE 3-mmin-gap: 0.148, 0.171, 0.313–0.367, 0.333 MeV; factor 2.25; 0.407 MeV; 8.5 %; the 6 % agrees with s1-3 l.212: CHECKED.

## §3.5
- l.3: 1/q = 0.066 Å: CHECKED. 2p peak 0.21 Å: CHECKED (re-run fig3_10).
- eq:3.5-pw; N_PW = Ωk³/6π² = 2121 at 60 Ry (816 eV); 1800 Ry → 3.5e5 ("3×10⁵"): CHECKED.
- l.15: the 1s transform 8πp₀/(p²+p₀²)² and the density (8/π²)p₀⁵/(p²+p₀²)⁴ (normalized); p₀ = 52 keV; p⁻⁸ tail: CHECKED.
- l.15/Fig. 3.9: nodes of 3s at 0.078 and 0.377 Å, of 3p at 0.377 Å: CHECKED (stored ld1 output; not an independent atomic calculation).
- l.17: 2k_cut = 58 keV; qv_max = 79.5 eV; q²/2m_e = 0.88 keV: CHECKED. eq:3.5-Ecut: CHECKED (kinematic argument).
- eq:3.5-radial, eq:3.5-logder: CHECKED. (u̇u′ − uu̇′)′ = 2m_eu², the sign of the final form included.
- Hamann Eq. (23), the generalized norm conservation ⟨φᵢ|φⱼ⟩_rc = ⟨ψᵢ|ψⱼ⟩_rc: CHECKED.
- l.45: SG15 r_c = 2.40480 and 3.56481 bohr = 1.273 and 1.886 Å; qcut 5.113 and 3.503 bohr⁻¹ = 19.07 and 13.06 keV (from the PP_INPUTFILE of /root/pseudo/sg15/Si_ONCV_PBE-1.2.upf): CHECKED, except "1.88 Å" for p, which should be 1.89 Å (minor; in the caption of Fig. 3.9 too).
- l.47/Fig. 3.9: charges 0.662/0.767; 10 % agreement below 2.07 and 4.90 keV; above 10 keV, AE 3s 6.8 % against PS 0.14 %; ratios at 30 keV 1.3e4 and 1.3e9: CHECKED (re-run of fig3_9 on the stored ld1 output).
- eq:3.5-PAW, eq:3.5-PAWop: CHECKED (cross-term argument redone).
- eq:3.5-rhoAE: GAP (normalization). As written, with ψ̃ normalized over V, ⟨p̃_κi|ψ̃⟩ for the reference-cell projector is O(N^{−1/2}), so the one-centre term is O(1/N) against the O(1) smooth term, and "every cell contributes the same terms" implies a factor N. Correction: say, as E.2 l.75 does, that the states in the projections are normalized over one cell (A.5), or insert the factor N. The phase e^{iq·τ_κ}: CHECKED.
- l.83: the small-q orders 1, qr_c, (qr_c)²: CHECKED. Griffin Sect. 3.1 ("even with thresholds as low as ~10 eV", heavy mediator; light mediator less): CHECKED.
- WE 3-Ecut: 5.66 MeV, 79.5 eV, 92 eV, p_f = 9.70 keV, 39.7 keV, 1.54 keV = 113 Ry, k_cut = 10.65 bohr⁻¹, Ω = 270.3 bohr³, 5510 PW (2.6×), Ωp_f³/6π² = 80, 28.9 keV: CHECKED. Above 30 keV: PS < 1e-7 (1.1e-8 and 3e-12), AE 0.73 % and 0.38 %: CHECKED (re-run). Griffin Sect. 2.1 (E_cut 1 keV, E_AE 2 keV); (2m_e·2 keV)^{1/2} = 45.2 keV: CHECKED.
- l.101: xdb Table 1-1: Si 2p₃/₂ 99.42, 2p₁/₂ 99.82, 2s 149.7, 1s 1839; Ge 3d 29.2/29.8, 2p 1217.0/1248.1 eV: CHECKED. Radial peaks 0.206/0.240/0.038 Å; median momenta 14.3 (2p), 37.0 (1s) and 2.2–2.8 keV (valence): CHECKED (re-run fig3_10).
- l.103: q ≥ ω/v_max and the minimization at q = (2m_χω)^{1/2}: CHECKED. 28.6 MeV/37.9 keV; 43.0 MeV/57.0 keV; 1s 524 MeV; 2.7 % above 38 keV: CHECKED.
- l.105: Ge 3d 8.47 MeV, q ≥ 11.2 keV, 74 % above, peak 0.268 Å: CHECKED. Griffin Sects. 1 and 3.3 (3d dominates for m_χ ≳ 10 MeV, heavy mediator): CHECKED. Fig. 3.10 caption: Ge 1s opens at 4.19 MeV; core outnumbers valence above 5.2 (Si) and 5.0 keV (Ge): CHECKED. l.114: 2p/valence at 30 keV = 37 ("forty"): CHECKED.
- Pauli reduction, l.118–135: both Dirac component equations; the expansion; Φ = (1 + p²/8m²)ψ_A; the cancellation of ε p²/4m²; p²U = Up² − 2i∇U·p − ∇²U; σ·p U σ·p = Up² − i∇U·p + σ·(∇U×p); eq:3.5-HBP: CHECKED (sympy on a general spinor, both identities exact). Darwin contact term πZα/2m²·δ³; the SO term equals eq:3.3-HSO (σ = 2S): CHECKED. "Fails within Zα/2m_e": CHECKED.
- l.138: virial ⟨v²⟩ = (Zα/n)²; ⟨U⟩ = 2ε, ⟨U²⟩ = 2(Zα)⁴m², ⟨p⁴⟩ = 5(Zα)⁴m⁴, ⟨H_mv⟩ = −(5/8)(Zα)⁴m, Darwin +(1/2)(Zα)⁴m, sum = −(Zα)²/4 of the binding energy (the Dirac 1s term): CHECKED (sympy).
- l.142: (l+1/2)ξ; hydrogen-like 2p 1.74 eV (Si) and 47.5 eV (Ge); Ge 2p doublet 31.1 eV; 3d 0.6 eV, weights 4:6: CHECKED. Si "a few tenths of an eV" (Booklet 0.40): CHECKED (known item). The Dirac–KS values 0.65/31.9 eV come from an atomic run that was not repeated.
- WE 3-Zalpha: (Zα)² = 0.0104/0.0545 and /4 = 0.26/1.36 %: CHECKED. "The 1s level of silicon moves from −1781.2 to −1785.9 eV, by 0.27 %": WRONG. 4.7/1781.2 = 0.264 % → 0.26 %, unless the levels change. The editor note's "0.27 % Si" inherits this. Ge 158/10803 = 1.46 %: CHECKED. ⟨r⟩₃d = 10.5/Z_eff → Z_eff = 14.2 (0.737 bohr = 0.390 Å, re-run); ⟨v²⟩ = 1.2e-3; 2.8 %; 0.6/29.5 = 2 %: CHECKED. l.158: Ge 2p opens at 347 MeV (> 0.3 GeV) and Si 2s at 43 MeV: CHECKED.

## §3.6
- l.3: (2m⊥·10 meV)^{1/2} = 44.2 eV = 1.9 % of 2π/a; |b|/44 eV = 90; 7e5 points: CHECKED.
- eq:3.6-wannier1, eq:3.6-inverse, the orthonormality display, eq:3.6-wannier, eq:3.6-projection (phase cancellation: the row phase e^{−iφ_m} is undone in ψ^W): CHECKED. Marzari 2012 Eqs. (8)–(10), (16)–(17), Fig. 2: CHECKED. Brouder (Chern = 0 ⇔ exponential localization; time reversal ⇒ Chern = 0): CHECKED.
- eq:3.6-spread (MV97 Eq. (11)), the r w_n display (integration by parts; the boundary term vanishes in the periodic gauge), eq:3.6-blount (MV97 Eqs. (4), (8)), the centre-shift argument, the Berry-phase polarization factor −2e/Ω: CHECKED.
- eq:3.6-discrete (MV97 Eqs. (31), (32), Σλ_bb_αb_β = δ_αβ): CHECKED. eq:3.6-split (MV97 Eqs. (13)–(16); the P + Q insertion redone): CHECKED. eq:3.6-stationary (MV97 Eq. (52), with R, T, A, S and the factor 4): CHECKED. eq:3.6-spillage (Souza Eqs. (8)–(9), T_kb = tr[P_kQ_{k+b}]): CHECKED.
- l.93 and Fig. 3.11 (spreads, centre 0.80 Å, 16.2/19.8/14.0 Å², 3.5–3.7 Å², decay length 1.57 Å): FIG-PASS. Editor priority item, independent evidence without QE: the wannier90 distribution's tutorial 11 benchmark (test-suite testw90_example11_2 and docs tutorial_solution_11: 4³ grid, Si:sp3 trial orbitals, frozen 6.5 eV, outer 17 eV) gives two groups of functions. On the atom at (a/4)(1,1,1) the four point away from the bonds, with centres 0.79 Å from the nucleus and spreads 2.017 Å² each. On the atom at the origin the four point along the bonds, with centres 0.39 Å from the nucleus and spreads 2.370 Å². Total 17.55 Å², Ω_I = 12.34 Å². The reason is that the default sp3 trial orbitals have the same orientation on both atoms, so they start "toward" on one sublattice and "away" on the other, and the minimization stays in both basins. Caveat: that run's windows are absolute energies; its VBM is 6.387 eV (silicon.eig), so the frozen window reaches only 0.11 eV and the outer window 10.6 eV above the VBM, against 2.5 and 12 eV in Fig. 3.11. The disentangled subspace therefore differs from the book's, and the agreement is in the per-function spreads and centres, not in the totals. This supports the text's ordering, with the away set more localized per function (2.02 vs 2.37 Å², the same 2.02 Å² and 0.79–0.80 Å as Fig. 3.11), and shows that both are local minima.
- l.93 "The silicon example distributed with wannier90 reaches the same set": WRONG. Correction: "The silicon example distributed with wannier90, whose trial hybrids have the same orientation on both atoms, ends with the four functions on one atom in this set (2.02 Å², centres 0.79 Å from the nucleus) and the four on the other pointing along the bonds (2.37 Å²)." Cite the tutorial or benchmark, not only Pizzi 2020.
- eq:3.6-HWR, eq:3.6-HWk (Marzari 2012 Eqs. (98)–(99)), the coarse-grid display, eq:3.6-alias (lattice sum on the grid redone), eq:3.6-exact (including the Wigner–Seitz boundary weights): CHECKED.
- l.138: MV97 Table I, 6×6×6: Ω = 7.611 Å² ("7.61"): CHECKED. 7.58, 350/120/51 meV, 0.02/0.12/0.03 eV, 40/84 meV: FIG-PASS. Two and three ⟨110⟩ steps = 7.68 and 11.52 Å: CHECKED. Velocity interpolation (Marzari 2012 Eqs. (106)–(109)); v_mn = (ε_n − ε_m)⟨u_m|∇u_n⟩: CHECKED.
- Fig. 3.12 caption: FIG-PASS (note "0.85" against 0.843 elsewhere).
- l.149–151 gauge argument: CHECKED.
- WE 3-w1d (recomputed): H(k); bands ±1.118 to ±3.041 eV, gap 2.236 eV; n_k = 2 error 0.242 eV and n_k = 3, 4, 6 error 4e-15; H^W(R) = 2.192, 0.468, 0.0525, 0.0120 eV; cos ka* = −1.3125, a/ξ = 0.771, e^{−a/ξ} = 0.462, e^{−a/2ξ} = 0.680; errors 51.1 meV, 0.637 meV, 2.43 µeV; range of (∂H/∂k)₊₋ 0.274–1.000 eV a; same gauge 1e-15: CHECKED. The R^{−3/2} prefactor (square-root branch point): CHECKED.
- WE 3-w1d "4.8 meV for 8": WRONG (minor). 4.747 meV → 4.7 meV (the gauge does not enter for one band).
- WE 3-w1d "off by up to 0.36 eV a": GAP (not reproducible). The value depends on the random phases: five draws gave 0.27 to 0.82 eV a. Correction: state the seed, or write "off by amounts up to 0.3–0.8 eV a, as large as the matrix element itself".
- Summary (l.170–182) against the accepted 3.5 (editor item): CHECKED. Cutoff q + p_f; norm conservation fixes the charge inside r_c; PAW reconstruction; core and semicore added where kinematics opens them; (Zα)², a few percent below about 0.3 GeV: all consistent with §3.5. Other numbers in the Summary (5.431, 40.05, 3.95, 1.17, 0.85, 0.916/0.191, 3.4, 0.333, 0.52 → 0.148): CHECKED.

## Appendix C.1
- eq:C.1-delta and the squeezed family: CHECKED. Areas of the three kernels equal 1, including the golden-rule (2/π)sin²(u/2)/u²: CHECKED. The 1/t² correction for a finite second moment: CHECKED.
- Dirichlet integral by the convergence factor; eq:C.1-sinsq (by parts); central lobe 90.28 %; |∫₀ᵗe^{iξs}|² and the Parseval area 2πt: CHECKED.
- Split into w(0)πt/2 + ½fp − ½∫cos…, eq:C.1-sincorr, eq:C.1-sinc: CHECKED. DLMF 1.8.10 (Riemann–Lebesgue) and 1.16 (distributions): CHECKED.
- eq:C.1-deltag; elastic example (μ/p)δ(p′ − p); eq:C.1-surface: CHECKED.
- eq:C.1-complete (finite window 2 sin(ωT/2)/ω), derivative rule −iq, eq:C.1-parseval, eq:C.1-conv; Helm factors 3j₁(qR)/(qR)·e^{−q²s²/2}: CHECKED. eq:C.1-causal: CHECKED.

## Appendix C.2
- eq:C.2-comb, eq:C.2-poisson ((L/2π)g̃(mL); DLMF 1.8.14, Poisson): CHECKED. Gaussian image term e^{−L²Δp²/2}: CHECKED.
- eq:C.2-dos (free particle V m p/2π², per spin): CHECKED.
- eq:C.2-latticesum, the infinite-crystal form (2π)³/Ω·Σδ³, counting, eq:C.2-unfold, eq:C.2-grid, the Monkhorst–Pack phase (−1)^{l_i} for a half-step shift, δ³(0) = V/(2π)³: CHECKED. Known item: the derivation is still duplicated here (editor ruling: cut to a pointer to §3.1).

## Appendix C.3
- eq:C.3-j0, eq:C.3-j1 (derivative under the integral), DLMF 10.49.3: CHECKED. Both Laplace transforms and the combined radial integral 8βq/(β²+q²)³: CHECKED (sympy, difference = 0).
- eq:C.3-moments and the double-factorial formula (⟨x⁴⟩ = 1/5): CHECKED.
- Y_lm convention (DLMF 14.30.1, Ferrers functions with the Condon–Shortley phase), eq:C.3-ortho (14.30.8), eq:C.3-addition (14.30.9), eq:C.3-unsold: CHECKED.
- Plane-wave expansion: l-fold parts, the I_l recursion, I_l = 2^{l+1}l! z^{−l}j_l (DLMF 10.49.14), ∫P_l e^{izu} = 2i^l j_l, eq:C.3-planewave (10.60.7), eq:C.3-jlimits (10.52.1, 10.52.3): CHECKED. qr_orb = 1 at 1.97 keV ≈ q₀/2: CHECKED.
- eq:C.3-cubic: the normalization (41/105, 16/525, product 1) and the decomposition √(7/12)Y₄₀ + √(5/24)(Y₄₄ + Y₄,₋₄): CHECKED (sympy at three directions, agreement to 1e-16). Invariant counts l = 6, 8, 10 (one each) and 12 (two): CHECKED.
- l.94, "The point group of silicon, germanium and gallium arsenide contains the rotations that map a cube onto itself": GAP (wrong for GaAs). T_d contains only the 12 proper rotations of T; the C₄ and C₂′ rotations appear as S₄ and σ_d. The conclusion survives, since T_d together with q → −q gives O_h. Correction: "The point group of silicon and germanium is O_h; that of GaAs, T_d, becomes O_h once q → −q is added (below)."

## Appendix C.4
- eq:C.4-PV (second form, Lipschitz bound), the Lorentzian identification t = 2/Γ_w, the real-part dominated-convergence argument, eq:C.4-SP, eq:C.4-cauchy, eq:C.4-jump (difference w, sum (1/πi)PV): CHECKED.
- xδ = 0, x PV(1/x) = 1, eq:C.4-difference, d ln|x|/dx = PV: CHECKED.
- Derivative of PV, l.53–55: WRONG (sign in the intermediate display). Integration by parts gives ∫_{|x|>x_c} w′/x dx = −[w(x_c)+w(−x_c)]/x_c + ∫_{|x|>x_c} w/x² dx (numerical check with w = e^{−(x−0.3)²}: both sides −2.9408). The display has "−∫ w′/x" on the left. Correction: drop the minus on the left, or write −∫w′/x = [w(x_c)+w(−x_c)]/x_c − ∫w/x² → −fp∫w/x². Then ⟨PV′, w⟩ = −⟨PV, w′⟩ = −fp, and eq:C.4-dPV, which is right, follows.
- eq:C.4-square (−d/dx of 1/(x+i0)) and the summary's ± signs: CHECKED.
- eq:C.4-lorentz, eq:C.4-lorentzcorr (the O(ε) coefficient −(π/2)εw″(0) redone in general), the test 1/(1+Γ/2) = 1 − Γ/2 + Γ²/4, fp = −π, w″ = −2, 10 % and the Gaussian 0.72 %: CHECKED. Spectrum of e^{−Γ|t|/2} = 2πδ_Γ; convolution widths add: CHECKED.
- Summary-of-definitions block (PV and fp folded forms, the expansion of 1/(x²+Γ²/4)): CHECKED.

## Appendix C.5
- eq:C.5-Rz (analyticity for y > 0), the sign-convention remark: CHECKED.
- eq:C.5-spectral (ϱ_R = −Im R/π), eq:C.5-highfreq, the first moment (2π)⁻¹·2∫ωS = 𝓃_e q²/m_e (detailed balance and FDT): CHECKED, given the A.7 f-sum normalization ∫dω ωS/2π = 𝓃q²/2m.
- Cauchy/KK derivation, eq:C.5-KK, eq:C.5-KKhalf (both halves): CHECKED.
- eq:C.5-screening (π/2 for perfect screening), eq:C.5-KKeps, ε∞ − 1 = (2/π)∫ε₂/ω, high-frequency limit ∫ωε₂ = (π/2)ω_p²: CHECKED.
- Residues of n_B (T) and n_F (−T), eq:C.5-matsum, the oscillator example (2n_B+1)/2ω₀: CHECKED (residues ∓1/2ω₀; numeric Matsubara sum equals the closed form to 15 digits). Continuation uniqueness (Baym–Mermin): CHECKED.

## Appendix C.6
- eq:C.6-gauss (completing the square; the contour shift), Fresnel e^{iπ/4}, Gaussian transform e^{−q²s²/2}, eq:C.6-moments, eq:C.6-generating, eq:C.6-gaussn, eq:C.6-isserlis: CHECKED.
- eq:C.6-hadamard; the BCH ODE and eq:C.6-BCH (both forms): CHECKED.
- eq:C.6-D ([X,Y] = |α|²), D†dD = d + α, e^{iqx} = D(iqℓ₀), eq:C.6-coherent, mean q²/2M; ²⁸Si M = 26.06 GeV, q = 55.9 keV: CHECKED.
- eq:C.6-normal ([X,Y] = −η²); ground-state e^{−q²ℓ₀²/2} is the square root of the survival probability: CHECKED.
- eq:C.6-bloch with ⟨x²⟩ = ℓ₀²(2n_B+1); eq:C.6-product (exponent ½⟨A²⟩ + ½⟨B²⟩ + ⟨AB⟩); e^{−2W}: CHECKED.

## Appendix C.7
- PSD equivalences, the diag(0, −1) counterexample, eq:C.7-CS, the outer-product form of S_ab: CHECKED.
- Block factorization (multiplied out), eq:C.7-block, det, eq:C.7-head, eq:C.7-partition ("E minus the Schur complement"): CHECKED.
- eq:C.7-dyson, both forms; R = R̃/ε; eq:C.7-woodbury, including the right-multiplication check: CHECKED.
- Bosons: inverse transformation, the two normal-ordered identities (redone), tanh2θ = g₀/ω₀, eq:C.7-Eboson: CHECKED. Truncated Fock space (n ≤ 39 per mode), lowest levels −0.2, 0.6 = E_b − ω₀, 2E_b − ω₀; numbers 0.8, −0.2, 0.125; ηh eigenvalues ±E_b: CHECKED.
- Fermions: inverse, the four product expansions and the two identities (redone), tan2θ = g₀/ξ₀, constant ξ₀ − E_f, eq:C.7-Efermion: CHECKED (4×4 Fock-space spectrum {ξ₀−E_f, ξ₀, ξ₀, ξ₀+E_f} for ξ₀ = 0.4, g₀ = 0.9).

## Appendix C.8
- eq:C.8-erf, eq:C.8-interval, eq:C.8-y2 (and N_esc): CHECKED. eq:C.8-series (DLMF 7.6.1) and partial sums settling after 9 terms: CHECKED. erf(1.0525): 0.86337 at 1.0525, 0.86338 at 250.5/238 = 1.05252, consistent with s1-2. eq:C.8-asymptotic (7.12.1): CHECKED. With x = 544/238 = 2.2857 (x² = 5.2245): 1.329e-3, 1.238e-3, exact 1.227e-3, erf = 0.99877: CHECKED. Note: "2.286" is rounded, and the e^{−5.224} it implies holds only for the unrounded ratio.
- l.39, "the second term … sets the size of the correction: 1.5 %": the Gaussian term alone is 1.39 %, and the cut total is 1.51 % (with erfc). Wording: "together with erfc, 1.5 %". Minor.
- eq:C.8-KE (19.2.8), eq:C.8-KEseries (19.5.1/2; 9/64, −3/64), eq:C.8-Klog (19.12.1), K(s′ = 0.1) = 3.6956 vs 3.6889, difference 1.2e-4 at s′ = 0.01: CHECKED. eq:C.8-reduce (both substitutions): CHECKED.
- eq:C.8-FL (series 1 − y²/3 − y⁴/15; large y 1/3y² + 1/15y⁴; derivative ½ln|1−y| at y = 1) and eq:C.8-branch (also through the Sokhotski–Plemelj route): CHECKED (sympy).

## Appendix D.4
- eq:D.4-energy, the density-matrix invariance, the variation (factor ½ cancelled by the two slots), h_HF, hermiticity, eq:D.4-HF, the exchange hole integrating to −1 (idempotency): CHECKED.
- E_γ, eq:D.4-Etot, eq:D.4-koopmans (frozen orbitals), the O(1/N) relaxation argument: CHECKED.
- Electron gas: angular integral (kp)⁻¹ln|(k+p)/(k−p)|, the 1/4π²k prefactor, the antiderivative (sympy: derivative − t ln = 0), 2xF_L(x), eq:D.4-gas, Σ_x(0) and Σ_x(k_F) = Σ_x(0)/2, widening e²k_F/4π² = αk_F/π = 8.29 eV, 20.8 eV: CHECKED.
- Average of F_L over the sphere = 3/4 (sympy), eq:D.4-Ex: −3αk_F/4π = −0.916/r_s Ry (coefficient 0.9163), r_s = 2.005, −6.22 eV, (3/5)E_F = 7.48 eV: CHECKED.
- l.78: the pointer for k_F and E_F is \cref{sec:4.2}, while §3.4 points to §2.5 for the same numbers. Check the target (cross-reference, not a derivation).

## Appendix D.5
- HK proof (the strict inequalities and their sum), eq:D.5-levy, the two-step minimization, the Euler–Lagrange condition with μ_ch: CHECKED.
- eq:D.5-Exc, the chain-rule variation, eq:D.5-KS: CHECKED.
- Σn_γE_γ = K_s + ∫V_KS𝓃 and eq:D.5-Etot: CHECKED.
- eq:D.5-janak (the implicit term vanishes by normalization), the HOMO = −I argument from linearity, eq:D.5-gap: CHECKED.
- eq:D.5-LDA, v_x = (4/3)ε_x = −e²k_F/4π² = Σ_x(k_F); Slater average (3/4)Σ_x(0) = (3/2)v_x = −12.4 eV; "two thirds of Slater's": CHECKED.

## NOTATION and convention drift (not in the editor notes unless marked)
- V(r) in eq:3.3-HSO and V_l(r) in eq:3.5-radial: bare V is the normalization volume, and V(x) "always with its argument" is the dark-matter–electron potential. Propose U_at(r) and U_l(r), in line with U and U₁ of §3.2 and §3.5.
- Unhatted ϱ(x, x′) in D.4 (one-body density matrix) and ϱ_R (spectral density) in C.5: NOTATION has only ϱ̂, ϱ_MK and ϱ̃. Propose ϱ̂₁(x, x′) or γ_dm, and a row for ϱ_R (or use ρ_R).
- φ in several roles while bare φ is the absorbed dark matter: φ(p) and φ_nl (captions of Figs. 3.9, 3.10), the phases φ_n(k) and trial orbitals φ^tr_n (§3.6; φ^tr is a known new symbol), and the PAW partial waves typeset \phi in 3.5 but \varphi in 3.2 and 3.6 (glyph inconsistency). Known: the 3.2 atomic orbitals become φ^at_j.
- Known items, present unchanged: 𝛋 = k − k₀ (§3.3) against κ, the basis index only; \op{\vect{v}} (3.2) against bare v in A.5 l.38 (default: A.5); L and S as angular momenta (§3.3, 3.5) against the loss function L and the structure factor S; ξ_SO and ξ_W against bare ξ, the energy mismatch; the upright Γ for rates in 3.1 l.101; H_Dar vs H_D (D.6).
- Fourier, sign and normalization conventions in eq:3.1-fG, eq:3.2-pw, eq:3.2-central, eq:C.1-complete, eq:C.5-Rz, eq:3.6-wannier and eq:3.6-blount: CHECKED against A.3/A.5 (e^{+iG·r} forward, f = Σf_G e^{−iG·r}; retarded functions analytic in the upper half plane). No factor-of-2, π or sign drift was found in these files apart from the items above.

## Dimensional analysis (displays that needed care)
- eq:3.3-ni: [eV³]·(ħc)⁻³ → cm⁻³; checked with ħc = 1973.27 eV Å.
- eq:3.5-logder: both sides dimensionless; eq:3.5-HBP: each term eV.
- eq:3.6-blount and eq:3.6-discrete: λ_Δk [length²], r̄ [length], ⟨r²⟩ [length²].
- eq:3.2-r [length] = [1]/[eV]; eq:3.4-HF: e²𝓃/r [eV] with e² = 4πα.
- D.4-Ex: Ry/r_s with k_F = 1.919/(r_s a₀).
- C.6-coherent: q²ℓ₀² dimensionless.
- C.5-highfreq: R ~ 𝓃q²/(m z²) [eV²], matching the NOTATION units of R.
All other displays carry consistent units by inspection; no dimensional error was found.
