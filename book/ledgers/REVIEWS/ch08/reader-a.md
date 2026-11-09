# Chapter 8 — mock reader (a), first-year PhD student, isolated review

Read: tex sources ch08/s8-1 … s8-8 and appD/D-24 … D-28 (the built PDF of Nov 1 23:46 predates every source file, so it is stale).
Method: read linearly and redid the algebra. I checked the numbers by hand or in Python, and diagonalized the toy model of we:8-sectors in numpy (160 oscillator states).

**Verdict: MINOR GAPS.** Nothing blocks the following material. Six items need a sentence or a fix (L1–L6 below).

## 8.1 Dark-matter couplings to a target
Reproduced:
- v⊥ for an electron at rest, and q·v⊥ = 0.
- The matrix elements of every row in eq:8.1-rows, including the second form of T_s (K² = q² + 4k·k′).
- The reductions O7, O8, O3, O5, O12, O13, O15 against tab:8-operators.
- eq:8.1-transverse.
- The 29Si numbers (0.312, 0.073, 10 %, 841).
- we:8-darkphoton: (q/m_V)² = 3×10⁻⁶; q²/8m² = 7×10⁻⁶ and 1.3×10⁻³; 1.9×10⁻⁵; 1.4×10⁻⁴.
- we:8-O2 in full: k_∥ = −1.18 keV, the annulus 2.50–3.37 keV, ⟨B⟩ = 3.37×10⁻⁵, ⟨B²⟩ = 1.167×10⁻⁹, v_min, v_T², the azimuthal average (A+B)²+2AB, and the total 1.46×10⁻⁹.
- The ALP and scalar rows against eq:1.4-alp and eq:1.4-scalar, with the sign of H = −L.
- eq:8.1-omega-inel.

Lost points:
- **L1 (we:8-O2, last paragraph).** The text says "the kinetic-energy row carries 80 %, and its interference with the dark-matter velocity, through the current row, the remaining 20 %". This does not follow from the transverse bookkeeping.
  - The 4A⟨B⟩ term is half n–T interference (2A⟨B⟩) and half |current row|² (2A⟨B⟩).
  - Each row also contains longitudinal velocity, which cancels only between rows. For example, (k+k′)_∥/2m = ω/q = 1.34×10⁻³ sits inside T.
  - Taken alone, the T row gives ⟨((k+k′)²/4m²)²⟩ ≈ 1.29×10⁻⁹, which is 88 % of the total, not 80 %.
  - Fix: attribute the shares to "the electron's transverse velocity squared" and "the cross term", not to rows.
- The paragraph mapping models to operators ("electric dipole → O11; magnetic dipole → O1, O4, O5, O6; anapole → O8, O9") is cited only, so I could not check it. For me it is the fastest paragraph of the chapter (Dirac bilinears, γ⁵), although app:C.15 and D.24 back it up. D.24 let me verify all four bilinears and the vector-exchange potential.

Used before defined: none that blocked me (n_Z, q_0, η and v_max are all from earlier chapters).
Pace: right, except the bilinear paragraph, which is fast.

## 8.2 The master rate formula
Reproduced:
- The full derivation in D.25: spin trace → 𝔇_ab, and one power of 1/V cancelling.
- Tr[𝔇Sᵀ] − Tr[𝔇S] = 2Tr[𝔇_I S_I].
- Γ_abs = S/(2ω) from the √(N/2ωV) matrix element.
- Γ_net from the FDT, including why "Im" of the matrix sum is the anti-Hermitian part.
- The dark-photon reduction to ζ²σ₁.
- |f|m_V = 2×10⁻⁸.
- Classical-wave threshold ≈ 7 eV (using ρ = 0.3 GeV/cm³) and t_coh ≈ 1.2 ns.
- Figure numbers: 35 eV at 26.5 keV, and 40 meV.
- Detailed balance eq:8.2-db, via D.25.
- we:8-cross completely:
  - k_F↑ = 4.50 keV, E_F↑ = 19.8 eV, the edge at 19.2 eV, and S_↑ = m²ω/2πq = 5.57×10⁷ eV², which I rederived from the annulus area 2πmω;
  - (Ṽ_n + ½Ṽ_s)², the O1–O7 cross term reducing to c₁c₇(v_T·ẑ)S_↑, v_T = 1.47×10⁻³, and the bound 5.7×10⁻⁵ with the 4.0 S_↑ ratio;
  - 8.4×10⁻⁴, the minority edge at 7.07 eV, and S_ns/S_nn = 0.068.

Lost points: none. One small question: the O7-alone bound includes "spin flips into the empty minority band". With an exchange splitting above 19.8 eV these flips are closed at ω = 5 eV, so the bound is valid but loose. Saying so would help.

Used before defined: the thermal order n_T and the label 𝔗 (sec:8.5) carry real content in the exothermic subsection ("drops it at every order", "sits at n_T = 1"). It is a forward reference I could only parse after 8.5.
Pace: good.

## 8.3 Exact relations
Reproduced:
- The interference bound, and the moment-matrix brackets (both orderings, the (−1)^k sign, and units of eV^{k+3}).
- The Hankel argument, and the M⁴ divergence (ω^{-9/2} tail).
- eq:8.3-M3 from scratch, including the sign through [n_e†, H] = q·j_e†.
- The (q·∇)²(1/y) identity, the −8π j₂ angular integral and ∫j₂/x = 1/3, which give the bracket [n^(κ) + 2n_e]/3.
- eq:8.3-M3sph, and the spring check −Kq²/(mMV) by both routes.
- Silicon conversions: 1765 a₀⁻³ = 1.19×10²⁸ cm⁻³, 1.2×10⁻⁴, 2.68 a₀⁻¹, 0.20 Å, (8.76 keV)², (8.78 keV)², (2.34 keV)², (98 eV)², and (469 eV)², which implies K̄ = 562 eV, consistent with the virial value.
- The free-particle M³_ss by direct averaging, and the jellium 3n² (via D.26).
- The Ward identities and eq:8.3-boostward, with (m/M)² = 3.8×10⁻¹⁰.
- we:8-chain: one-phonon and two-phonon elements, the flux element 4iK sin², the dispersion, and 8.8×10⁻⁴.

Lost points:
- **L2.** The text says the interference is "positive at low energies, where the electrons follow the nucleus (8.6)". Shortly after, eq:8.3-boostward gives S_eκ = −(m/M)S_ee (< 0) for every final state at finite energy at small q. I had to work out myself that the positive weight must sit in the acoustic branch (ω → 0 with q). One sentence would fix it.

Steps I could not reproduce: the Hartree–Fock contact density, and the bracket 0.3353, 0.347 and 0.427, which need the atomic calculation. I checked only the unit conversions and the ratios.
Pace: dense but fair. The section moves one commutator per sentence.

## 8.4 Screening for every coupling
Reproduced:
- eq:8.4-screened, with the order of v and ε⁻¹ (push-through, D.27).
- v R_ZZ = ε⁻¹ − 1 and S_ZZ = (2q²/e²)L/(1 − e^{−βω}).
- we:8-nucleon completely:
  - the TO pole cancelling to the LO pole, and S_NN = πq²|a_N|²δ/(μΩω_L);
  - A/M = 1.001073 for Ga and 1.001046 for As, so a_N = 9.4×10⁻⁴;
  - the crossover at 0.021 eV, |a_N| = 0.61 and 4.5, the shares 7.2×10⁻⁵ and 3.8×10⁻³, and Z*/ε∞ = 0.19.
- In-medium mixing: |ε|² = 774; Γ_net = ζ²m L = ζ_eff²σ₁ (D.25 too); Im(R̃ε*) = Im R̃.
- The exactness theorem with the Cauchy–Schwarz conclusion in D.27.
- Static vertex: the even-in-ω′ argument and (ω/E_g)² ≈ 3×10⁻³; ω_p²/q₀² = 2×10⁻⁵.

Lost points:
- Nit: the GaAs ionic part at 1.5 eV is (ε₀ − ε∞)ω_T²/(ω_T² − ω²) = −0.92×10⁻³, which reads more naturally as −0.9×10⁻³ than −1.0×10⁻³ (ε₀ = 12.72).
- In the Coulomb-line classes, D.27 case 2 says the bridging phonon line "is a second phonon line beside the one in the final state", but in that case it is the only phonon line drawn. I could not tell what the final state is there.
- The proof by graph topology is fast for someone with only sec:4.8, but D.27 made it followable.

Used before defined: κ_BO-suppressed "Migdal amplitudes of sec:8.6" and eq:8.6-fsum-e (forward references).
Pace: good. The table helps.

## 8.5 The expansion hierarchy
Reproduced:
- κ_BO = 0.0665, κ³ = 2.9×10⁻⁴, 0.055 ≈ 12κ², θ_ep = 0.010–0.016, and η² = 2.4×10⁻³.
- T = 0.862 µeV, 4.6×10⁻⁵, e^{−21550}, 7.4×10⁻⁷, 4×10⁻¹⁵.
- E_R = 1.91 meV, x_R = 0.047, the 46 keV crossing, 2W = 0.063, 2W = 1 at 40 keV, and 1.35.
- The compound-Poisson cumulants c_k = E_R⟨ω^{k−1}⟩, x_R ≥ 9 at 139 keV and 0.37 eV, and 0.54 eV.
- 7×10⁻⁶, 0.56 fs, 1.006, the 100 eV boost, ξ_D = 1.9, 0.05 and 5×10⁻⁶, and 0.555 q²a₀².

Lost points:
- **L3.** n_B counts powers of the derivative coupling d, but the table puts κ_BO beside it. The text then offers three different sizes for "one step" in n_B:
  - κ³ (zero-point mixing);
  - ω_ph/ΔE ≈ 12κ², which enters squared;
  - κ⁴ (drag, f-sum share).
  - tab:8-nuisances then uses (ω_ph/E_g)² for the n_B entry. I cannot turn "n_B = 0 → 2" into a number without guessing which one applies. A one-line rule would fix it.

Used before defined: "off-shell window", defined in 8.6.
Pace: values appear three times (text, table caption, table), which is slightly slow. The multiphonon subsection is excellent.

## 8.6 The decomposition theorem
Reproduced:
- 2W = 1.57 at 50 keV, giving 21 % and 47 %.
- The f-sum share Zm/M = 2.73×10⁻⁴.
- The two partial sums in eq:8.6-fsum-k add to n q²/M at first order.
- δM = N_e m for an atom via TRK (D.28).
- The tilt and boost amplitude, including the cancellation of the ∇Ψ terms (D.28).
- h_off² = Γ ΔE_c/2π, and 5/2π + 1/π = 1.11.
- The δ-coefficient of D.28-delta.
- **we:8-sectors, every quoted number from an exact diagonalization:**
  - ZPL at 1.04625 eV; first adiabatic line at 63.4 meV;
  - σ_x weights 1.253×10⁻³, 0.15205 and 0.84670;
  - first moment 1.169148 eV, with 8.32×10⁻⁵ eV in the electron-following sector;
  - P_Mig = 3.94×10⁻⁶ = 0.38 + 3.56 (×10⁻⁶), and the leading formula 3.51×10⁻⁶;
  - 4.72 µeV;
  - interference ±(2.17 − 13.22i)×10⁻⁴ eV, summing to zero to 10⁻¹⁹;
  - 6.4×10⁻⁵.

Lost points:
- **L4 (eq:8.6-fano).** The text says "The Fano coefficients c^F_ν sum to zero with the weights Γ^(ν)". With c̄^F defined as their weighted mean, it is (c̄^F − c^F_ν) that sums to zero, not c^F_ν. Even that holds only if the weights Γ^(ν)/Γ^tot sum to one:
  - With other decay channels (impact ionization, Γ^tot > ΣΓ^(ν)), the sum over phonon branches of (Γ^(ν)/Γ^tot)(c̄^F − c^F_ν) is −c̄^F(1 − r), where r = ΣΓ^(ν)/Γ^tot.
  - This contradicts "they change no total and no number of zero-phonon events".
  - D.28 is consistent only because it uses the phonon-only Γ_m.
  - Fix: let ν run over all decay channels, and reword the sentence.
- The gapless-target subsection is the one place I am lost. Landau's theory, the Migdal–Eliashberg equations, the dressing unitary, the joint spectral projectors and the "limiting-absorption principle" (in the open problems) are all beyond the persona.
  - It does not block anything I need next; I took the bound eq:8.6-bin on trust, though its D.28 proof via Duhamel is readable.
  - "Schrieffer–Wolff transformation" is used without a gloss.

Steps I could not reproduce: eq:8.6-leak (Panati–Spohn–Teufel, cited); the level-and-band values z = 1.0064 and −0.0064, from ch4 and not recomputed.
Pace: the Dyson-convention subsection is the densest of the chapter, with fp/PV distributions, residues and windows in one page, but D.28 carries it. The toy example is the best-calibrated passage of the chapter.

## 8.7 Final-state-resolved response
Reproduced:
- eq:8.7-factor and its reversed-order twin.
- i[1/(x+i0) − 1/(x−i0)] = 2πδ.
- The closure of eq:8.7-screened into a squared modulus.
- S = (q²/2πα)L.
- 1.633 (2π/a), 0.84 keV, |ε⁻¹₀₀|² = 0.33, 0.33 × 0.87 = 0.29, and m²ω/πq₀ = 2.2×10⁸ eV².

Lost points:
- **L5 (we:8-pairs).** Every pair at ω = 10 eV shares ω − E_g = 9.2 eV between its carriers. Dark matter gives 4.8 + 4.4 = 9.2 and the transverse current 5.4 + 3.9 = 9.3, but the photon gives 5.4 + 3.3 = **8.7 eV**. Either a value is wrong, or the 0.10 eV Lorentzian tails combined with the 1/Δε² optical weights pull the mean down by 0.5 eV. Either way it needs a sentence, because the headline "a volt below" rests on the 3.3.
- **L6.** The PT argument that the advanced weight is the conjugate of the retarded one needs f real symmetric (f* = f), not only Hermitian. This holds for RPA and the ALDA kernel in a centrosymmetric crystal, but the text should say so.

Pace: good. The hand-off conditions are clear and concrete.

## 8.8 Uncertainty structure
Reproduced:
- The power form is negative at ϑ = −1/δ (2σ for δ = 0.5).
- The geodesic matrix form is PSD by congruence.
- Debye–Waller 6.1 %, and η²ω_opt = 0.15 meV.
- The convexity argument for λ₀ and λ₁ (Hessian = Hankel matrix).
- eq:8.8-cost: u = w/k², N_nom = u e^{k²u}, and the expansion 1 + k²t*/4. The values 1.010, 1.079 and 1.191 for δ = 0.1, 0.3 and 0.5 give 1 %, 8 % and 19 %, and the δ > 0.47 switch-off holds.
- 3.5 eV/MeV; (11.45/10.22)² = 1.255.

Lost points: none. A small precision: "lighter than ~7 MeV samples only δ_X < 0" holds at q₀ only up to the zero of the template at 4 eV.
Pace: good. The worked example on the RPA rung makes the tilt and f-sum argument concrete.

## Learning outcomes (as I infer them), tested
1. Reduce any O_i to rows, and write 𝔇_ab with its spin traces: **yes** (did O3, O12, O13, O15, and the ½-spin trace).
2. Write scattering, absorption and inelastic or exothermic rates from one formula, and recover the ch1 rates: **yes**.
3. Use the interference bound, the moment matrices, M³_eκ and the Ward identities as checks: **yes** (rederived M³_eκ and the chain).
4. Decide how a coupling is screened, and when the loss function is exact: **yes** (redid the GaAs LO shift and the theorem).
5. Label a formula with 𝔗 and size the next step: **partly**. I can place labels, but cannot size n_B steps (L3).
6. Assign final states to sectors, apply partial sum rules and avoid double counting: **yes** (toy model reproduced). The gapless case I follow only qualitatively.
7. Compute screened pair weights and state the hand-off conditions: **yes**, with L5 open.
8. Build a nuisance (template, type, constraints) and estimate its cost to a limit: **yes**.

## Overall
I would keep reading: almost every number reproduced, and the appendices close every derivation I tried except the cited theorems. The chapter is long and dense, but it moves at a steady pace. My open items are L1–L6, mostly a missing sentence or a loose word. L4 (the Fano weights) is the only statement that is wrong as written. L5 (photon pair energies) is the only number that is inconsistent with its neighbours. Neither blocks the following material. Verdict: **MINOR GAPS**.
