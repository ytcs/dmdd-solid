# Ch7 derivation check (isolated): 7.1–7.4, App. D.19–D.23

Reviewer: derivation verifier (long-form-writing SKILL §5). Date 2026-11-02.
Method: every non-definitional step redone by hand and with sympy/numpy/scipy (light, ephemeral scripts in the session scratchpad
/tmp/claude-0/-home-user/364f612b-be7d-56fd-924b-36b7d0d3bbab/scratchpad/c7{1,2,2b,3,4}.py; not kept; no QE). Sources fetched with lit.py into sources/review-ch07/ (PDFs converted to text, then deleted);
Hutchings (abstract) and Holmström (text) were read from sources/7.1 and sources/7.4.
Cache note: figscripts/ch07 holds no npz or gaas_cache, and no Ch7 number depends on QE output, so nothing was taken from caches.
Excluded as known (editor-notes.md): bare α_i, β (→ 𝛂_D, β_D), doublet Pauli σ (→ σ^d), italic ϝ vertex (→ 𝖵, also the upright Γ_η of D.21),
ω₀ and E_d reuse, ε₀ = 11.4 vs 11.7, S_HR = −ln 0.23 inferred, Bergeron arXiv-only, 40 meV BCS cutoff, the Δ/(v_F q) ≤ 0.20 bound.

Summary: no error in any displayed key result. 2 WRONG statements of substance (D.19 coefficient asymptotics; T-center hole binding
vs source), 4 small WRONG items (oblate/prolate, 0.3 % claim, 10 keV claim, valley-orbit reference rounding), 3 GAPs, 6 notation drifts.

## WRONG

1. **D-19.tex, "The spin operators", "both coefficients diverge as (A₀/2ω^M_k)^{1/2}"** → missing |S|. From (u^M)² = A/(2(A²−B²)^{1/2})
   and ω^M = |S|(A²−B²)^{1/2}: u^M ≃ v^M ≃ (|𝐒|A₀/2ω^M_𝐤)^{1/2}. (Dimensionally the printed form is fine; it is wrong by |S|^{1/2}
   for |S| ≠ 1, e.g. Ni²⁺ is |S| = 1 so NiO numbers are unaffected.)
2. **s7-4.tex, T center paragraph, "a hole is bound … by only 22 to 32 meV"** cited to bergeron2020characterization. The paper quotes 22 and
   32 meV only as earlier estimates (its Refs. 9, 2); its own result supersedes them. It (arXiv:2006.08794, Sect. IV) measures the acceptor-like Rydberg series and extrapolates the hole ionization limit to 969.84(15) meV, i.e. a hole binding
   of **34.78(15) meV**; 22 and 32 meV are the older estimates it quotes (Irion 1985, Safonov 1996). Correction: "by about 35 meV
   (earlier estimates 22 to 32 meV)". The 235 meV total pair binding and the structure are as in the source.
3. **D-23.tex, "The orbit is a prolate spheroid, flattened along the heavy axis"** → an ellipsoid with two radii 24.3 Å and one 14.0 Å is
   **oblate**. (7.4 says "flattened", correctly.)
4. **s7-4.tex text after Fig. 7.4 and Fig. 7.4 caption, "within 0.3 %"**: recomputed EMT at ε₀ = 11.4 (independent coupled-radial solver,
   l ≤ 12): 2p₀ 11.506, 2p± 6.416, 3p₀ 5.491 meV vs measured 11.48, 6.40, 5.47 → 0.23 %, 0.26 %, **0.39 %**. With the rounded values in
   the text (11.51, 6.42, 5.49) the deviations are 0.26, 0.31, 0.37 %. Correction: "within 0.4 %".
5. **s7-3.tex opening ("Dark matter as light as 10 keV can carry an electron across this gap") and the closing paragraph ("reach dark matter
   of 10 keV")** contradict the computed threshold 10.5 keV (recomputed: 10.49 keV) and Fig. 7.3's caption ("the 10 keV curve stays just
   below the continuum"). Correction: "of about 10.5 keV" (or "of order 10 keV"). The "thirty times lighter" (333/10.5 = 32) stands.
6. **s7-4.tex WE 7.4, valley-orbit paragraph**: with the stated reference −31.3 meV the shifts are −14.29, −2.59, −1.28 meV, not
   −14.27, −2.57, −1.26 (those use −31.32). The extracted elements barely move: Δ_f = −2.17, Δ₀ + Δ_g = −5.62 (text −5.60),
   Δ₀ = −4.10, Δ_g = −1.51 meV. Even with the text's own numbers Δ₀ = (−5.596 − 2.57)/2 = −4.08, not −4.09. Fix: quote the reference as
   −31.32 meV or recompute with −31.3. Signs and the ordering |Δ_f| > |Δ_g| are confirmed.

## GAP

7. **s7-3.tex WE 7.3, static screening, "expansion parameter g α̃ ln(v_DΛ_D/2Δ_D) = 0.66"**: the paragraph before the limit box defines the
   parameter with ln(v_DΛ_D/max(Δ_D, v_D q)), which at q → 0 is 0.38 ln 11.5 = **0.93**. Recomputed both (0.666, 0.929). Use one definition:
   either write the definition with max(2Δ_D, v_Dq) (pair threshold) or quote 0.93 ("below one, barely").
8. **s7-4.tex WE 7.4, "Size"**: the displayed formula with the rounded radii 24.3 and 14.0 Å gives a³/(8π·24.3²·14.0) = **7.71×10⁻⁴**; 7.8×10⁻⁴
   needs the unrounded minimizer (a = 24.27, b = 13.96 Å → 7.75×10⁻⁴). Quote 7.7×10⁻⁴ or the unrounded radii.
9. **s7-1.tex end of the exchange subsection, "linear spin-wave theory with the best of them overestimates the measured magnon energies by about
   14 percent [dossantos Sect. III]"**: the source's 14 % is the average overestimate of the *maximum* magnon energies, by TDDFPT+U and
   LSWT with ΔE-derived J together. Say "the maximum magnon energy". (Sect. III and the < 5 meV anisotropy gap are as cited.)

## Notation and convention drift (against NOTATION.md)

10. **s7-3.tex, bold κ = k − k₀ throughout 7.3** (Eqs. 7.3-block, 7.3-H, DOS paragraph, anisotropy): NOTATION row "δk … replaces the bold κ of
    the draft, κ is the basis-site index". Rename to δ𝐤 (components δk_i). Sect. 3.3 itself uses δ𝐤 (13 times, no bold κ), so this is a 7.3-only drift.
11. **s7-1.tex, E₀ used twice in one section**: one-electron energy in Eq. (7.1-dirac) and the AFM ground-state energy in Eq. (7.1-afm)
    (also D.19-omega); NOTATION has E₀(u) as the electronic ground-state energy of 5.1. Rename the 7.1-dirac one (e.g. E_orb).
12. **𝒩_s(E)** (BCS quasiparticle DOS, 7.2 Eq. 7.2-dos, D.20-dos) clashes with the existing row 𝒩_s (GAP-fit environments, E.11), and sits
    next to N_s (sublattice site count, 7.1/D.19). Propose 𝒩_qp(E) or 𝒩^BCS(E).
13. **γ overload in one chapter**: γ_𝐤 (7.1 fcc structure factor), γ_𝐤1, γ_𝐤2 (7.2 quasiparticle operators), γ₂ (7.2/D.21 phase-channel vertex
    coefficient), γ_m (7.4 mass ratio), γ_E. γ_𝐤 vs γ_𝐤ν in adjacent sections is a genuine clash; none has a row. Propose γ^fcc_𝐤 (or ζ_𝐤)
    for 7.1 and a row for each.
14. **D-19.tex, Fourier sign**: S^+_A(𝐤) ≡ Σ_i e^{−i𝐤·𝐫_i}S^+_i, while 7.1 (and App. A, n_e(𝐪) = Σ e^{+i𝐪·𝐫}) uses S^±(𝐪) = Σ e^{+i𝐪·𝐑}S^±.
    The algebra in D.19 is internally right (D.19's S^+(𝐤) is 7.1's S^+(−𝐤) = [S^−(𝐤)]†), but the convention drifts; state the relation
    or use e^{+i} and S^+(−𝐤).
15. **D-23.tex, U(𝐫) = −e²/(4πε₀r)**: correct in Heaviside–Lorentz with dimensionless ε₀ (e² = 4πα), but reads as SI; NOTATION reserves
    ε₀^SI for quoted SI formulas. Write −α/(ε₀r) only.
16. **s7-4.tex WE 7.4 and D-23.tex, a and b**: "a" is the silicon lattice constant in "Size" (a³/8) and the variational radius in "Kinematics"
    (1/a = 81 eV, qa ≈ 0.42) of the same worked example; D.23 also uses a for the radius. Rename the radii (e.g. r_⊥, r_∥).
    Rows still missing for Ch7 symbols (check_notation.py, expected at the merge): V_BCS, ω^M_𝐤, K_ex, E_cl, A_𝐤, B_𝐤, Ry*_⊥, a*_⊥, w_ZPL, Δ₀,
    Δ_g, Δ_f, Λ̃, 𝒩_D, F(ω), K, O_A, h_𝐤, γ_E.

## CHECKED

### 7.1 Magnetic order and spin waves
- Singlet/triplet energies of Eq. (7.1-dirac): S₁·S₂ = −3/4, 1/4 → E₀+C±K_ex; coupling −2K_ex FM. Kinetic exchange: two-site singlet
  −4t²/U (exact −U/2+… vs −0.00799 at t/U = 0.02), J = 4t²/U − 2K_ex (Eq. 7.1-superexchange). Dimensions of K_ex: energy.
- NiO estimate: (J₂U_H)^{1/2} = 0.296–0.395 eV for U_H = 4.6–8.2 eV; t/U = 0.048–0.064. Hutchings convention H = J S·S per pair,
  J₂ = 19.01, J₁ = −1.37 meV, 78 K, ~250 meV Å, ~117 meV: as in the abstract. Fischer Table I a = 4.17 Å, Table IV T_N = 523 K,
  Table III NiO J₂ (their H = −Σ_{i≠j}, J_ours = −2J_F): DFT entries 5.50–13.35 → 11–27 meV (UHF/Fock are Hartree–Fock, excluded as stated).
- Holstein–Primakoff: S⁺S⁻ = (2S−n)(n+1), S⁻S⁺ = n(2S−n+1), difference 2S^z. Bond expansions (FM and AFM) and E_cl's of 7.1-fm and D.19.
- Eq. (7.1-fm) and small-k form; chain: 2|J|S(1−cos ka), |J|Sa²k², max 4|J|S; exact one-magnon argument (diagonal −2JS, hop JS).
  Ring checks recomputed by exact diagonalization: one-deviation error 4×10⁻¹⁶; two deviations, N = 10, S = ½: 0.3277 vs LSWT 0.3820;
  N = 8, S = 1: 1.0827 vs 1.1716. Group velocity 2a(ω|J|S)^{1/2}.
- AFM: Eq. (7.1-Hk) = D.19-Hk coefficients; Bogoliubov signs consistent with C.7-Hboson (tanh2θ = g₀/ω₀); ω^M = |S|(A²−B²)^{1/2};
  E₀ = E_cl + Σ(ω − |S|A); branch S^z assignments; Eq. (7.1-weights) (u ∓ v)² = (A ∓ B)/(A²−B²)^{1/2}; D.19 (u−v)² = [(A−B)/(A+B)]^{1/2};
  D.19-linear; type-II geometry (6 NNN and 6 NN antiparallel, 6 NN parallel, by (111)-plane index); Eq. (7.1-J2), max 6J₂|S|, slope 2√3J₂|S|a.
- WE 7.2: 274.6 meV Å, 1.392×10⁻⁴, 41.7 km/s; [111] slope 254.8 meV Å; other directions 254.8–269.2 (20 000 random directions: claim
  255–269 holds); bound A ≤ 6J₂ − 3J₁; 4×10⁵-point scan + local max gives 118.17 meV = |S|(6J₂−3J₁); 6J₂ = 114.06; zeros at (½,½,½),
  (½,½,−½), (1,0,0) confirmed; A²−B² ≥ 0 elsewhere (stable). v_max/v = 19.0; 41.7/8.43 = 4.95.
- Ordering wavevector √3π/a = 1.305 Å⁻¹ = 2.575 keV → m_χ ≥ 0.486 MeV ("≳ 0.5 MeV").
- Eq. (7.1-Sfm) against Eq. (4.2-Sab) = (2π/V)Σ⟨i|O_a†|f⟩⟨f|O_b|i⟩: prefactor π|S|/Ω, +iε_abc z_c sign, eigenvalues 2, 0, 0; dimension eV².
  Trickle: Eq. (4) form −Σ Ô_χα S_eα, polarization √(S/2)(1, i, 0) of Eq. (6), Table I: as cited.

### 7.2 Superconductivity
- Eq. (7.2-Veff) static limit; pair-term coefficient −(2/N)|g|²/ω; V_BCS = 2Ω⟨Σ|g|²/ω⟩; N_F V_BCS = λ_ep via Eqs. (6.4-a2F), (6.4-lambda)
  (same 1/(N_FΩN²) normalization, N_F per spin). Dimensions: V_BCS eV⁻², N_F V_BCS dimensionless.
- Eq. (7.2-NVren): (0.44−0.12)/1.44 = 0.222. Savrasov Table III: T_c 1.18 K, Δ₀ (calc, exp) 0.18 meV, μ* 0.12, ω_log 270 K, λ 0.44: as cited.
- Cooper problem: condition and E_bind = 2ω_D/(e^{2/NV}−1); Al: 0.402 µeV, ratio 892 ("~900").
- Mean field and Eq. (7.2-gamma): inversion, b_𝐤 = uv(1−2n_F), BCS state annihilated by γ₁; signs consistent with C.7-Hfermion; Eq. (7.2-E).
- DOS Eq. (7.2-dos), state conservation 2N_F(ω²−Δ²)^{1/2}. Gap equation, arsinh form, Δ = ω_D/sinh(1/NV), T_c = 1.1339ω_D e^{−1/NV}
  (D.20 Matsubara derivation, harmonic-number step and vanishing remainder redone), ratio πe^{−γ_E} = 1.76388; numerical gap equation at
  NV = 0.2: 1.76396. Al: 2Δ/T_c = 3.540 vs 3.528; exponent at 10 mK: −208.
- Coherence factors: expansions of c†c for both spins (D.20), Eq. (7.2-coh), squares Eq. (7.2-cohE) with sympy-equivalent algebra
  (both sign cases). Nambu trace for A = B = η reproduces case I.
- Pair-creation spectrum: S_n = 2πN_Fω/(v_Fq) = m_e²ω/(πq) (equals −2 Im of the free-gas χ); Eq. (7.2-pairspec) from the averaged factors
  and the DOS; jump π/2 (numerically 1.5708 at ω = 2.0001Δ); ω = 4Δ: 1.211 and 0.672; case II equals Mattis–Bardeen's T = 0 elliptic form
  [(1+2Δ/ω)E(k) − (4Δ/ω)K(k), k = (ω−2Δ)/(ω+2Δ)] to 10⁻¹² at ω/Δ = 2.5, 3, 4, 8. v_F = 6.67×10⁻³ (= 2.0×10⁶ m/s of 6.4), v_F/v_max = 2.52.
- Eq. (7.2-violation): (4π/V)ΣΔ²/E = 8πΔ²/V_BCS via the T = 0 gap equation; dimension eV⁴ = f-sum's. Finite-q claim recomputed (linearized
  band, Δ_𝐤 = Δ inside the 40 meV shell): spurious moment / (8πΔ²/V_BCS) − 1 = −5×10⁻⁵, −4.5×10⁻⁴, −1.7×10⁻³ at v_Fq = 0.5, 5, 20Δ
  ("0.2 %" holds). Ratio to the f-sum 12(Δ/v_Fq)²/NV with 𝓃_e = (4/3)N_F E_F; crossover v_Fq = 8.55Δ.
- Nambu algebra: O_η = n_e (q ≠ 0), O_𝗌₁, O_𝗌₂ in terms of B_𝐏; [𝗌₁, η] = −2i𝗌₂; Eq. (7.2-comm) including the unit-matrix kinetic bilinear
  reducing to Σ(ξ_{k+q}−ξ_k)c†c; H_int = −(V_BCS/4V)ΣO_aO_a + one-body (cross terms are a commutator); mean field −ΔO_𝗌₁.
- q = 0 bubbles (D.21-q0) from Tr[σ_aP^±σ_bP^∓] = δ − nn ∓ iεn: 4Δ²F, ω²F − 2/V_BCS, ±2iΔωF; s₁ mixing odd in ξ. Eq. (7.2-Rc) as the
  resummed series; Eq. (7.2-cancel) = 0; γ₂ = −2iΔ/ω; Ward identity (7.2-ward) at q = 0 and the normal-state check (current vertex ∝ unit
  matrix). Kernel dimension: KR⁰ dimensionless.
- WE 7.3: T_c = 0.10168 meV, Δ = 0.1794, 2Δ = 0.359 → 0.36 meV; m_min 102.5 eV (film 0.6 meV: 170.9 eV); q = 0.272 eV, 1/q = 0.73 µm; pair size
  2.34 µm; v_Fq = 10.1Δ, Δ/v_Fq = 0.099; NV = 0.1639 (40 meV), 0.180 (ω_log = 23.27 meV); T_c = 54.2, 19.9, 5.85 K for NV = 0.44, 0.306,
  0.222, and 1.180 K for 0.164; exp(1/0.164 − 1/0.222) = 4.92 (5.85/1.18 = 4.96, so "4.9" is a slight truncation of 5.0; acceptable);
  40/23.3 = 1.72.

### 7.3 Dirac and narrow-gap materials
- Kramers-form argument: N N† = (|z|²+c²)𝟙 + 2(Im z)𝐜·σ; SO(4) ≅ SU(2)×SU(2) basis freedom; α_i, β anticommute; Eq. (7.3-H) spectrum.
- Kane: |v| = (E_P/2m_e)^{1/2} = 4.73×10⁻³, m = m_eE_g/E_P = 0.0664 m_e (1 % from 0.067), v/v_max = 1.79.
- DOS Eq. (7.3-dos) and both limits; Eq. (7.3-nc) (parabolic edge, mass 0.0529 m_e); Δ/T = 0.60 (300 K), 45.3 (4 K); n_c = 1.04×10⁻⁵ cm⁻³;
  exact integral over (7.3-dos) 4.3 % higher ("4 percent").
- Pair edge (convexity) Eq. (7.3-edge); 4Δ/v_max² = 8.89 keV; threshold with v_D: 10.49 keV; along v_y 9.39, along v_x 12.67 keV;
  v_D/v_max = 0.287.
- Eq. (7.3-epsbg) placement; α̃ = 0.190, gα̃ = 0.380; Hochberg set α̃ = 0.199, harmonic mean 25.34; Hochberg Eq. (2.5) α̃_H = gα/(κv), Table 1
  (g = 4, κ 187.5/9.8/90.9, v 2.9/0.50/2.1 ×10⁻³, 2Δ = 35 meV), quoted 0.80 = 4 × 0.20: as cited. Geilhufe Table 1 (ISIF7 row), Table 2
  (308.4, 20.75, 126.1, g = 2), Eq. (1.1), Eq. (2.21) Λ̃ = min Λ_i v_i, Eq. (3.10) constant e^{−5/3}: as cited; gaps 23.6–35 meV ("24 to 35").
- D.22 chain: overlap 𝓕 = (v²q² − D²)/(4EE') (also Hochberg Eq. A.7 with λλ' = −1); d³k = 2πEE'dEdE'/(v⁴q); boundary inequality (20 000
  random tests); ∫(v²q²−D²)dD = (4/3)v³q³ρ; Eq. (D.22-R) sign and iε; Im part; ∫ρdu/u = ln(U/Δ²) − 5/3 (substitution verified);
  ∫_{x−}^{x+}6x(1−x) = b(3−b²)/2 and the log identity (sympy); ∫x(1−x)ln[x(1−x)] = −5/18 (sympy). Eqs. (7.3-eps), (7.3-Im),
  (7.3-static), gapless limit and its −6Δ²/(v²q²−ω²) correction; Hochberg Eq. (2.6) has no −5/3, so its Λ = e^{−5/6}Λ_D = 0.435Λ_D, and its
  Eq. (2.7) equals the hard-cutoff gapless form: both statements correct. Na₃Bi 10 %: as cited.
- Limit-box caption: gapless within 0.1 for v_Dq > 7.43Δ ("7.5"), with correction from 3.64Δ ("3.7"), residual 3.0×10⁻³ at 10Δ.
- WE 7.3: v_iΛ_i = 0.499, 0.188, 0.180 eV; Λ_D = 236 eV = 0.120 Å⁻¹; ln 23.08 = 3.139; ε(0,0)/ε_bg − 1 = 0.0930, ε = 55.2; finite q: 0.0813
  (q = 41 eV), 0.0527 (q = 118 eV); doubling Λ: 2.8 %; v_DΛ_D = 11.5Δ_D. Anisotropic Eq. (7.3-aniso) rederived by rescaling; additions 9.81,
  1.57, 6.71 (3.2, 7.6, 5.3 %); axis couplings 0.0650, 0.155, 0.109; 0.19/0.065 = 2.9 ("threefold").
- Dimensions: 𝒩_D eV², n_c eV³, α̃ and every ε dimensionless, R⁰_D eV².

### 7.4 Defects and dopants
- Hydrogenic Eq. (7.4-hydrogenic): Ry*_⊥ = 18.98 meV, a*_⊥ = 32.4 Å; longitudinal 91.0 meV, 6.76 Å; γ_m = 0.2085.
- D.23 variational energy: kinetic and ⟨1/r⟩ = arcsin(e)/(ae) rederived; minimum −1.5642 Ry*_⊥ = 29.69 meV at 24.27, 13.96 Å; 4.5 and 2.6
  lattice constants. Independent coupled-radial solution: 1s −1.5660 Ry*_⊥ (29.73 meV at 11.7, 31.31 at 11.4), 2p₀/2p± at 11.7: 10.92/6.09 meV.
  ε₀ fit 11.7(6.09/6.40)^{1/2} = 11.41; 2.6 %. Smith: 3p± 3.12 meV, 1s 31.27 meV (Faulkner), ε = 11.4: as cited.
- Vinh Fig. 1: P 45.59, T₂ 33.89, E 32.58, 2p₀ 11.48, 2p± 6.40, 3p₀ 5.47; As 53.76, 2p₀ 11.50, 2p± 6.40: as cited. Claes Table 3: Sb 42.71, P (PBE,
  extrapolated) 19.20 vs 45.6: as cited.
- Central cell 14.3 meV (31 %), 15.9/1.6 meV at 11.7. Valley-orbit eigenvalues of Eq. (7.4-vo)/(D.23-vo) from the 6×6 matrix; A₁ − E = 6Δ_f.
- Volume 3.44×10⁻²⁰ cm³, 2.9×10¹⁹ cm⁻³; 10¹⁵ cm⁻³ → 100 nm; 10¹⁵/2.0×10²³ = 5×10⁻⁹.
- Kinematics: 2×45.59 meV/7.023×10⁻⁶ = 12.98 keV; 333/13 = 26; q = 34.4 eV; 1/24.3 Å = 81 eV, 1/14.0 Å = 141 eV; qa = 0.42.
- Color centers: 1326 nm, 637 nm; Eq. (7.4-cc) vertical energy Sω₀; (2S)^{1/2} = 1.71, 2.77; e^{−27.6} = 1×10⁻¹²; T-center weights 0.23,
  0.34, 0.25, 0.12; bound 0.30, e^{−1.77} = 0.17; NV: 0.0213, strongest p = 3 at 0.202, 0.246 eV, 2.19/1.70/0.49 eV; Poisson average 0.677
  (moments S, S+S², S+3S²+S³), photon fraction 0.0315; −ln 0.032 = 3.44 (source writes 3.45). Alkauskas: S = 3.85 ± 0.05 at 8 K (Sect. 3),
  64 meV, DW 3.2 %, Eq. (2) ω³ weighting, converged S = 3.67 (Sects. 4.2–4.3); Bergeron PRX Quantum: 0.94(1) µs, DW 0.23(1), 1.4/4.2 K, ²⁸Si;
  Dhaliah: 985 meV in a 512-atom cell: as cited.
- Displacement: Holmström Table III formation energies (vacancy 3.4–3.9, interstitials 4.7–5.8, close FP 6.8–7.5, bond defect 2.6–3.0 eV,
  4.7 Å), Table IV (12.5 ⟨111⟩, 19.5–20.5 ⟨100⟩, 35–36 FP average, 23–24 BD/FP), SW overshoot along ⟨111⟩ 4 and 6 eV, Loferski 12.9 ± 0.6:
  as cited. Recoil thresholds with M = 26.16 GeV: 0.1535 GeV (12.5 eV), 0.2615 GeV (36 eV). 7/12.5 ≈ ½, 7/36 ≈ ⅕.
- T center target 266 keV, gap offset 0.235 eV, q = 0.706 keV, 2.80 Å; NV 554 keV, 1.47 keV; 10 mK barrier exponent 1.16×10⁵.

### Appendix D.19–D.23 (beyond the items above)
- D.19: Fourier transform with opposite phase on B and the pair-sum identity; ferromagnetic reduction for J_AB = 0; D.19-omega = 7.1-afm.
- D.20: H_MF constant VΔ²/V_BCS; u = cos θ, tan 2θ = Δ/ξ; Matsubara sum T Σ 1/(x²+ω_j²) = tanh(x/2T)/2x; all of the T_c derivation.
- D.21: all identities listed under 7.2; continuity of the time-dependent mean field (argument consistent; the shell correction O(v_Fq/ω_D)).
- D.22, D.23: see 7.3 and 7.4.

### Not re-run (machine-precision consistency claims, not derivation steps)
D.19 256-site precession check (10⁻¹²); D.20 four-mode Fock check; D.21 48×48 lattice check (factors 28 and 4) and the Goldstone speed
0.579 v_F (Anderson's v_F/√3 confirmed analytically only); D.22 direct quadratures (10⁻⁵, 10⁻⁴). They are stated as numerical checks and
need the authors' scripts (figscripts/appD) to audit.
Sources not checked against text: Doherty 2013 and Kadribasic 2018 (cited qualitatively, not fetched); Jagannath 1981 and Faulkner 1969
(paywalled; their numbers 45.59 and 31.27 meV were confirmed through Vinh Fig. 1 and Smith 2017); Kohn–Luttinger, Tinkham, Anderson 1958,
Nambu, Cooper, BCS, Bardeen–Pines, Holstein–Primakoff, Mattis–Bardeen, Loferski (paywalled or cited for attribution; the formulas they
carry were rederived instead; Mattis–Bardeen's closed form was checked numerically).
