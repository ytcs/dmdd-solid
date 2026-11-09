# Ch10 part 2 (10.6–10.10): derivation review (isolated)

Scope: tex/ch10/ch10.tex, s10-6 … s10-10. Method: sympy for the algebra (explicit 4×4 Dirac matrices for every trace),
independent numerical scripts on the cached npz (si_elf_binned, core10_6_orbitals) with my own halo, η and rate code
(no reuse of the writer's rate code), and the cited sources fetched into sources/review-ch10/. No QE runs.
Scripts: /tmp/claude-0/-home-user/364f612b-be7d-56fd-924b-36b7d0d3bbab/scratchpad/rev/{compton,hoch,ferm,halo,boost,cher3,core,rate}.py.
Key: CHECKED = redone independently and agrees; WRONG = error, with the correction; GAP = missing step, citation or registration.

## PRIORITY verdicts

**P1. 10.8(a) ALP dark-Compton factor: CONFIRMED.** I evaluated the tree amplitude for a(k)+e(p)→γ(k')+e(p') from
g a ψ̄iγ⁵ψ with explicit Dirac matrices at threshold (a and e at rest; transverse photon sum), so the comparison does not
rely on the writer's numerics:
⟨|M|²⟩ = 2e²g²m_φ²/[m_e(m_φ+m_e)], σv = e²g²m_φ²(m_φ+2m_e)/[16π m_e²(m_φ+m_e)³] = Eq. (10.8-alpC), exactly.
- 2109.08168 Eq. (17)/(3) over the tree result = (m_φ+2m_e)/(m_φ+m_e), symbolically (Eq. 10.8-factor ✓).
- Their Eq. (15) is 1/4 of my spin-summed trace. Their vector Eq. (9) also has the 1/4, and their Eq. (12) is correct, so the
  printed normalization is the same for both.
- **New detail for the text:** their *differential* Eq. (16), integrated over cos θ at v→0, gives exactly the tree result
  (ratio 1, sympy). The error therefore enters between their Eq. (16) and Eq. (17)/(18), not in the amplitude. Suggest
  adding to 10.8 after "The factor enters in the integration over the final states": "their differential rate,
  Eq. (16), integrates to Eq. (10.8-alpC); the factor appears only in the integrated Eqs. (17) and (3)". This makes the
  correction checkable from their own paper.
- Vector: the same trace (3 massive polarizations, k^μk^ν drops) gives Eq. (10.8-compton) exactly. The series 1 − 3x/2 +
  5x²/2 − 15x³/4 (exact) against −35x³/8 (seagull, NR recoil) and −17x³/4 (exact ω_γ) all check, as do the large-x limit 1/4,
  the ALP series 1 − 5x/2 + 9x²/2 and the spin-seagull leading term.

**P2. 10.8(b) pseudoscalar pair absorption not velocity-suppressed: CONFIRMED.** On shell, ψ̄iγ⁵ψ = (1/2m_e)∂_μ(ψ̄γ^μγ⁵ψ)
(this holds with a vector potential present). Integrating by parts puts ∂_μ on φ†φ, and on the pair that gives
−i(p+p̄)_μ. The time component, E+Ē ≃ 2m_φ, multiplies ψ̄γ⁰γ⁵ψ, which is the spin-current row 𝒥_e; the space components
carry q⃗ = p⃗+p̄⃗ and are negligible. So g_𝒥 = 2m_φG_P is not suppressed. The following check:
Γ_pair/V = (ρ/2m)²G_P²S_𝒥𝒥 = (ρ/2m)²·3m_φG_P²σ₁(2m_φ)/e²; equivalence to Eq. (10.7-alp) at 2m_φ with g_eff² of (10.8-geff);
scalar g_eff²; vector 2G_V²m_φ²⟨|v−v̄|²⟩L/e²; numbers 4.0×10⁻¹⁷ (pseudoscalar, 5 eV, σ₁ = 12.68 eV) and 4.7×10⁻²⁴ (vector);
G_S = 1.37×10⁶G_F; Λ ≈ 0.25 GeV; g_eff = 1.28×10⁻²¹.

**P3. 10.9(a) boosted-DM factor (1−ω²/𝒬²)²: CONFIRMED.** Conserved currents on both sides (q_μJ^μ_χ = 0; ωn = q⃗·j⃗ between
eigenstates) give J⁰n − J⃗·j⃗ = J⁰n(1−ω²/𝒬²) − J_T·j_T, and the massless limit is the Coulomb J⁰n/𝒬² (Eq. 10.9-amp ✓).
2401.11971 Eq. (5) and the Supplement (⟨|ū γ⁰u|²⟩ ⟨f|ρ̂|0⟩ only) indeed omit the longitudinal current.
- Trace ½Σ|ūγ⁰u|² = (2E−ω)²−𝒬² ✓.
- Convexity bound ω ≤ v𝒬 ✓; (1−v²)⁻² = 2.0 % (v = 0.1) and 8.5 % (v = 0.2) ✓.
- My own integration over the binned RPA+LF tables (ω 1.11–89 eV, 𝒬 from ω/v to 22.5 keV) gives exact/published, light
  mediator: 0.9967, 0.937, **0.639**, 0.166 at v = 0.1, 0.5, 0.9, 0.99, against the book's 0.997, 0.94, 0.65, 0.17.
  Heavy mediator: 0.99993 at every v ✓. The 0.65 against 0.64 difference comes from the ω grid (the book's script
  interpolates to 0.05 eV), well inside the stated rounding.

**P4. 10.9(b) fermionic absorption, free vertex not current-conserving: CONFIRMED, with a sharpening (GAP).**
- Dark-side traces and tensor ✓: D⁰⁰ = D^{ii} = 1/4Λ_F⁴, D^{0i} = −q^i/(4qΛ_F⁴). Contracting with J_μ = (n, −j) gives
  (1/4Λ_F⁴)[|n + q̂·j|² + |j_T|²], and continuity turns it into (m_χ/q)²|n|² + |j_T|² ✓. The sign is fixed by the free limit
  q̂·j = q/2m_e = ω/q.
- Exact free-electron trace (sympy): it equals Dror et al. Eq. (9) up to M⁴(M+2m_e)²/[2Λ⁴(M+m_e)²], i.e. relative
  O(m_χ²/m_e²), consistent with their "terms of O(q³)".
- Eq. (10.9-ratio): the closed form and its expansion 1 − ω²/m_χ² + ω(m_χ−ω)(2m_χ−ω)/(m_em_χ²) + O(m_χ²/m_e²) ✓.
- Xe 1s, rough check: 1 − ⟨ω²/m²⟩ + the 1/m_e term gives 0.59 at 56.5 keV ✓. E_B = 33317.4 eV matches Table I ✓.
- Si 1s: Z_eff = 11.626 gives 1839 eV ✓, and the continuum oscillator strength 0.4350 ✓.
- **Sharpening:** the closing sentence of the xenon paragraph and the 10.9-open text ("Whether the full current-conserving
  rate lies closer to one form or to the other is open") are too cautious. Within the book's non-relativistic,
  local-potential framework the vector rate is (σ_F/2π)[S̄_nn + (q²/m_χ²)Tr S̄_jTjT], and the transverse term is a sum of
  squares, so it is ≥ 0. The current-conserving rate is therefore ≥ the density term > the free-vertex form wherever r < 1.
  At 56.5 keV the free vertex underestimates by at least 1/0.59 = 1.7. Only the relativistic corrections, (Zα)² ≈ 0.13
  (smaller than the 41 % deficit), are of undetermined sign. Correction: "the free-vertex form is below the
  current-conserving rate by at least the factor r; the transverse term only adds; relativistic corrections of order
  (Zα)² ≈ 0.13 are of undetermined sign." Apply the same change to 10.10-open and to the limitbox 10.9c closing sentence
  ("of comparable size and has not been computed": add that it can only raise the rate).

**P5. 10.9(c) Cherenkov-like transverse dominance: CONFIRMED in substance; novelty claim to be scoped.**
- Analytic check, independent of the tables: with ε₂→0 the transverse term of Eq. (10.9-fermi) per ω is
  ∫d𝒬/𝒬 (v² − ω²/𝒬²) Im[𝒬²/(𝒬² − ω²ε)] → (π/2)(v² − 1/ε₁) once v²ε₁ > 1, independent of ε₂.
  At 1.5 eV and v = 0.5 this is 0.2754; adaptive quadrature with the measured ε gives 0.27493. The writer's θ-substitution
  agrees with quad to 10⁻⁷ at 1.5, 3, 5, 10, 20, 40 and 80 eV.
- The density row below 2 eV (tables' L/𝒬) is 4.5×10⁻⁴ (integrated), so ratios of order 50 (v = 0.3) and 500 (v = 0.5)
  follow. 49 and 530 are reproduced from the same inputs.
- Thresholds v > ε₁^{−1/2}: 0.281 at 1.2 eV, 0.149 at 3.31 eV ✓. Absorption lengths 1/(2ω Im n_r): 0.37 mm at 1.2 eV and
  12 μm at 1.5 eV ✓. Fermi form = 2608.20715 Eq. (2) exactly ✓.
- **Novelty scope (for 21.5/E.16):** the Cherenkov term in the transparent window is standard for fast charged particles
  (Fermi's formula; the photo-absorption-ionization treatment of energy loss in Si). The new part is only its size in a
  boosted-DM rate with a light mediator, and the failure of the electron-gas estimate of 2608.20715 there. The text makes no
  priority claim, so it can stay as is. When flagging for 21.5/E.16, state that scope and the two modelling choices: tables'
  L together with measured 300 K ε, and Cherenkov photons counted as deposited.

**P6. 10.4 (listed in the brief; not my file, verdicts only).**
- (a) **10.4 is right; Table 8.3 (tab:8-screening) is wrong on two rows.** The spin current is a triplet row. The Coulomb
  kernel acts on the total density, so the spin current has no proper correlation with the charge: unscreened, like the spin
  density, with only the triplet xc kernel beyond RPA. "Local fields only" is wrong for it. 𝒯_e is A₁g-scalar, so
  R̃_{𝒯n}(q, G = 0) ≠ 0 at finite q, and it is head-screened. At q→0 in non-polar crystals that correlation is O(q²), as 10.7
  derives, which is presumably what 8.4 had in mind. Fix: move "spin current" into the spin-density row ("none without SOC
  or magnetic order"). Give 𝒯_e its own row: "head and local fields; R̃_{𝒯Z} = O(q²) at small q in crystals without a polar
  axis". Keep the transverse current as written.
- (b) **W̄₅ ≡ 0 exactly in Si/Ge: CONFIRMED.** B₅ = i(q/m_e)·(f⃗ × f⃗*) is the antisymmetric part of the vector–vector
  response contracted with q. Inversion gives S_ab(q) = S_ab(−q), and time reversal gives S_ab(q) = S_ba(−q), so S_ab is
  symmetric and W̄₅ = 0, likewise Im W̄₂. Equivalently, e^{iq·r} and p e^{iq·r} are PT-even, so the products are real after
  summing degenerate multiplets. This holds for any Hamiltonian with inversion and time reversal. 2105.02233 itself calls
  Im W̄₂ and W̄₅ "orders of magnitude smaller" and attributes them to imperfect symmetry. The book's "numerical noise" reading
  is correct; their atomic-symmetry explanation is not the real reason.

## 10.6 Core and relativistic states

- 10.6-core prefactor 4π = 2π × spin; equals (2π/Ω)Σ_κS^at with S^at summed over σ ✓.
- 10.6-Sat closure: ∫p dp over [|k−q|, k+q] = 2kq, so ∫dω S^at = N_nl ✓.
- Near-opening form: (2√2/3) N m_e^{3/2} φ(q)² (qv_max − E_core)^{3/2} ✓ (sympy).
- S^at = q²Ωε₂/(8π²α) from S = (2q²/e²)ε₂, two atoms per cell ✓.
- Germanium counts, from my own integration of 10.6-Sat over the cached orbitals: 3d gives 0.0040 (12 keV), 0.025 (15 keV),
  0.036 (20 keV); the atomic valence gives 0.002 at 20 keV. All ✓.
- ⟨r⟩(3d) = 0.736 a₀ = 0.39 Å ✓; rms p(3d) = 20.40 keV ✓; ⟨v²⟩ = 1.59×10⁻³ (Ge 3d) and 1.31×10⁻³ (Si 2p) ✓; 75 % of 3d
  above 11 keV ✓.
- Openings and masses: 11.30/11.53 keV, 8.53/8.70 MeV; 3p 46 keV; 3s 68 keV; Si 2p 38 keV; 2s 57 keV ✓.
  m_χ ≥ 24.5 MeV (q = 12.5 keV) and 18.7 MeV (13 keV) ✓; the 10 MeV window q ∈ [16.3, 36.7] keV ✓; q₃d = 3.35 q₀ ✓.
- Picture change −q²/4m_e²: 1.2×10⁻⁴, 8.6×10⁻⁴, 2.0×10⁻³ ✓. Spin term 5.9×10⁻⁴ and its square 3×10⁻⁷ ✓. Doublet/binding
  2.0 % ✓.
- Dirac factor: (q/Zαm_e)^{(Zα)²} = 1.0009 (Si 2s at 57 keV), 1.134 (Ge 1s at 10Zαm_e = 1.19 MeV) ✓; Ge 1s opens at 4.2 MeV ✓;
  (Zα)² = 0.055 ✓.
- Fermi factor 2πν/(1−e^{−2πν}) = 11.7 (2 keV) and 4.7 (5 keV) ✓.
- Ge valence ω_p = 15.6 eV ✓; ε−1 = 0.0128 at 12 keV ✓; screening |ε|⁻² ≈ 2.4 % ✓ ("about 2 percent").
- Orbit–orbit double commutator, redone by hand: [[H_oo,n],n†] = (α/m_e²)Σ_{i<j} q·T·q cos(q·r_ij), and the kinetic one is
  −Nq²/m_e. Eq. (10.6-oo), its sign and the small-qr limit −(4/3)E_ee/(N m_e) ✓. FT of (1 + r̂r̂)/r = 8π(1 − k̂k̂)/k² ✓.
- δ_mv: −1.83×10⁻³ (Si), −5.76×10⁻³ (Ge, 2075.3 Ha → K̄ = 1764.7 eV) ✓. δ_oo −5.65×10⁻⁴ / −1.81×10⁻³, ratio 0.31, totals
  −0.24 % / −0.76 % ✓.
- GAP (verification, not text): the Thomas–Fermi −0.23/−0.73 %, the crystal-valence values (0.44 and 0.03 at 5 and 10 keV;
  0.0084 at 12 keV; switch mismatch 27 %; "factor of six") and the rate ratios of WE 10-ge3d (6×10⁻⁵ … 3.4) need the
  Knapen table plus a halo integration over (q, ω). I did not redo them; script-reported only.

## 10.7 Absorption on electrons

- Γ_L = ζ²(m²/ω²)σ₁/|ε|² and Γ_T = ζ²m⁴σ₁^T/|ω²ε^T − p²|² from −(1/ω)Im Π × m⁴/|m² − Π|² ✓.
- Γ_T/Γ_L = 1 + v²[2Re(1/ε) − 1] (sympy, x = p²/m²) ✓; −1.73×10⁻⁶ at 10 eV ✓. (pa)² = 7.6×10⁻¹⁰ ("about 10⁻⁹") ✓.
- WE 10-darkphoton: |ε|² = 5.139, L = 0.2467, σ₁ = 12.68 eV, 1/|ε| = 0.441, Π = (288 − 127i) eV², 6.76; R = 1.52×10³³ and
  7.82×10³³ ζ²; ζ = 4.44/1.96×10⁻¹⁷ ✓ (unit conversion redone by hand).
- ALP spin trace ½/(2/3) = ¾ ✓; Eq. (10.7-alp) ✓ = 1608.01994 Eq. (10) = 2106.12586 Eq. (47) ✓. Ratio to DP 1.61×10⁻⁸ ✓.
- Magnetized ALP: E = −gφ₀ε⁻¹B₀; identity (ε⁻¹)†(ε−ε†)ε⁻¹ = (ε⁻¹)† − ε⁻¹; Γ = g²B₀² B̂·Im[−ε⁻¹]·B̂/m ✓. 2305.05681 Eqs. (6)
  and (7) ✓ (their Σ_λ(e_λ·B₀)² Im[−1/ε_λ] is the projected inverse). 10 T = 1953 eV²; ζ_eq = 1.95×10⁻¹⁷; 0.58/kg/yr;
  μ_B B = 0.58 meV ✓.
- Eq. (10.7-aniso) ✓ (sympy).
- Scalar: [[p², V], V] = −2|∇V|²; ½⟨[[𝒯,H],𝒯]⟩ = ⟨|∇V|²⟩/2m_e; Eq. (10.7-sumrule) and ∫m²Γ ✓.
- Hydrogen asymptote: ⟨k|V|1s⟩ → −4√π/k² gives ∫d³k/(2π)³ (k²/2)(16π/k⁴) = (4/π)√(2Λ) ✓.
- Eq. (10.7-scalar) = 2106.12586 Eq. (56) with g² = 4πd²m_e²/M_Pl² and Π_{v̄²v̄²} = R_𝒯𝒯/m_e² ✓.
- 300 K Si: ε(1.12 eV) = 12.56, absorption numbers, TA occupation 0.96–0.97 (300 K) and 0.067 (77 K) ✓.
- EPM numbers (0.8–1.15, 9.8×10²⁹ g², 1.30×10³ eV³, 2 %/41 %, 41→34 peak): script-reported, not redone (GAP, verification
  only).

## 10.8 Two-insertion processes

- P1 and P2 above. Seagull coefficient ζe²/m_e ✓; spin seagull (eg/m_e²)∂_tφ A·s_e from minimal coupling in Eq. (1.4-alp) ✓;
  spin factor ½ ✓.
- Thomson integral: 4π·2π·(2/3)/(16π³·2m) = 1/(6πm) gives Eq. (10.8-thomson) ✓. σ_Th = e⁴/6πm_e² = 6.65×10⁻²⁵ cm² ✓.
- ALP σv at 100 keV: 1.338×10⁻²⁵ cm² (tree), 2.457 (published), 1.622 (NR, +21 %) ✓.
- Kinematics: ω_γ = 91.82 keV, ω_C = 8.18 keV ✓; Si K reached at 45.2 keV, Ge K at 118.2 keV, L (100 eV) at 10.2 keV ✓.
- n_e/ρ_T = 3.002×10²³ g⁻¹ ✓; ω_p(all) = 31.05 eV and n_r − 1 = −1.93×10⁻⁷ ✓; 92 keV = 46.6 Å⁻¹ ✓.
- Compton/absorption 6.24 (DP), 5.13/9.43 (ALP), total 1.70 ✓; √1.836 = 1.355 ✓; Ge/Si photoelectric 15.4 ✓.
- Pair rate normalization 1/(4EĒV) per pair ✓. ξ = 8π^{3/2}/0.99415 = 44.81 ✓, with 0.99415 = erf(2.5) − (5/√π)e^{−6.25}
  ✓. (0.39/0.3)² = 1.69 ✓.
- Halo, my own MC (v₀ 238, v_esc 544, v_E 250.5 km/s): ⟨v²⟩^{1/2} = 378.8 km/s, K̄ = 1.597×10⁻⁶ m, Var K = 0.2531 K̄²,
  ⟨|v−v̄|²⟩^{1/2} = 401.8 km/s (1.80×10⁻⁶), ⟨|v+v̄|²⟩^{1/2} = 2.142×10⁻³ ✓ (all quoted values).
  Density/kinetic "factor 50" = 1/(1.68×10⁻²×1.145) = 52 ✓.
- Bauer et al. Eq. (8) has 2g_DM m⁴β_c³ in the denominator; the book drops g_DM. This is harmless, because their phase space
  carries g_DM², but write "per degree of freedom" or keep g_DM (minor).
- GAP: the kinetic-row pair rate 1.6×10⁻¹² is EPM-model, script-only.

## 10.9 Inelastic, exothermic, boosted, fermionic

- Halo average: ⟨δ(ω−ω_q)⟩ = η/2q gives Eq. (10.9-inel)'s 1/(8π²α) ✓.
- Shell measure: ∫d³q δ G = m k_* ∫d²n̂ G with k_*² = q_Δ² + m²v²; Eq. (10.9-shell) with 4π²α ✓. Correction factor
  √(1+x)(1+2x) → 2.5x; 2.9 % at 0.1 MeV / 3 eV ✓. Edge law (|Δ|−ω)^{−1/2} ✓.
- My independent rate code on si_elf_binned (own η): 10 MeV LF 314 / 5.89×10⁴ / 7.52×10⁵ (heavy) and 6.2 / 9.78×10³ /
  5.06×10⁵ (light; book 5.2×10⁵, 2.5 % low, from my 𝒬 floor at the integrable q→0 end) ✓.
  IP/LF at 1 MeV: 18.5 (Δ = −5) and 9.33 (Δ = 0) ✓.
  Elastic gates: 3 MeV IP/RPA/LF 5.20×10⁴/2.49×10⁴/1.85×10⁴, light 5.97×10³; 10 MeV 1.36×10⁵/8.6×10⁴/5.9×10⁴ ✓.
- WE 10-exo: ω_line 1.64/3.70/6.62/8.54 eV; q_line 1.29/1.94/2.60/2.96 keV and 3.20 keV (∞); q_Δ at the peaks
  0.78/1.51/2.83/4.03 keV; v_max/v_Δ 0.34/…/1.97; thresholds 0.60/3.16 MeV; 2|Δ|/v_max² = 2.85 MeV ✓.
- WRONG (wording), WE 10-exo: "half-maximum widths from about 4 to 8.5 eV (to 11.8 eV at 3 MeV)". The log gives the
  half-maximum *edges* (4.47–8.29, 3.77–8.43, 4.07–8.91, 4.63–11.75 eV). The widths are 3.8–4.9 eV (7.1 eV at 3 MeV).
  Fix: "half maximum between about 4 and 8.5 eV (11.8 eV at 3 MeV)". Also "41 %" at 0.1 MeV: the log prints 0.40; check
  the third digit.
- Retardation bound and Fermi form: see P3/P5. Solar core: T = 1.5×10⁷ K gives (3T/m_e)^{1/2} = 0.087 ✓.
  GAP (known item): add the SSM citation (Bahcall et al.) for 1.5×10⁷ K.
- Flux replacement (ρ/m)η → ∫dv v⁻² dΦ/dv ✓ (= 2607.09352 Eq. (11)). D_eff = 8.02 kpc ✓ (2401.11971).
- Fermionic: P4. Light-mediator factor: t = 2m_χω − m_χ² ✓ and the expansion ✓. Free-electron limits σ_F(1 − O(m_χ/m_e)) ✓.
  Per-atom response π|f_ion|²/2E_ej = 2π × (closure-normalized |f|²/4E) ✓, consistent with 10.6. ω = 9.8 keV at 100 keV ✓.
- 1509.01598 Eqs. (A.18)–(A.21) ✓ (A.20: 2k'³ with the sum over occupied states); Dror et al. Eq. (8): 4k'³ with an explicit
  spin factor ✓.
- WRONG (citation fidelity), lim:10.9a: the box formula, with q⁻² and |…| in v_min, is dimensionally right but is not what
  2203.06664 prints. Their Eq. (16) is dR/dE_e ∝ ∫dq F²|f_c|²η, with no q⁻², which is dimensionally inconsistent as printed.
  Their Eq. (11) has no absolute value; they handle the sign through their piecewise q_min, Eq. (10). Fix: cite "Eqs. (10),
  (11), (15), (16) and (20), with the factor q⁻² of 1509.01598 Eq. (3.13) restored". Also drop "absolute value included"
  as an attribution in the text after Eq. (10.9-inel) (line 16), or say the book adds it.
- Decay: Γ_vac = μ_M²Δ³/π (M1 analog of ω³|d|²/3π with Σ|σ|² = 3) ✓. Eq. (10.9-decay) prefactor 2/π² (spin ½Tr = δ,
  transverse B gives 2𝒬²) ✓; vacuum and n_r³ limits ✓; E1 ∝ n_r ✓; Si n_r³ = 40.8–44.4 ✓; absorbing window 3.2–22.5 eV ✓;
  55 eV ✓.
- WRONG (citation): baryakhtar2020electromagnetic is a JHEP-style paper whose equations are numbered (2.1) and (2.2). The text
  and lim:10.9d cite "[Eqs. (1) and (2)]". Fix: "Eqs. (2.1) and (2.2)". Note also that their operator gives μ_M = 2/Λ_d after
  reduction (σ^{μν}F_{μν} → −2σ·B), so the book's rate is (4/π²) × their πδ³/Λ_d². Their "∼" covers this, but write
  "μ_M ≃ 2/Λ_d" rather than "μ_M ∼ 1/Λ_d".

## 10.10 Uncertainties

- Gates reproduced by my rate code (see 10.9). Window 10.53 eV and 15.9 keV; m_min 0.316 → 0.333 MeV; 8.5 %; 48.5/day ✓.
- Band: ln(1+δ) = 0.247, 0.289, −0.078, 0.065; σ = 0.393; 1.19–2.62×10⁴; variance share 93 %; 1.65 with δ_𝒳 = 0.49;
  Δ = 0.075 from ±0.10; 2.27×10⁴ at ϑ = 1; light 1.67 ✓.
- 8.0 E_x^b = 0.118 eV; 1.155 eV line ✓.
- Table: every editor-note nuisance is present (10.2 large-q LF, 10.3 branching, 10.5 coupling block, 10.7 p_φ² terms,
  10.8 bound shells and axial with SOC, temperature row) ✓.
- GAP: add the P4 sharpening to the "free-electron vertex" sentence of 10.10-open.

## Notation (NOTATION.md drift)

- WRONG, clash: K̄ is "mean kinetic energy per electron" (4.3; used as such in 10.6). 10.8 reuses K̄ = m_φ⟨v²⟩ for the pair
  and bare K for the pair kinetic energy (K is a zone point; "italic K not used"). Rename to K_pair, K̄_pair (also in
  lim:10.8a and fig:10-pair-limit).
- WRONG, clash: 10.8 uses bare ξ = 44.8 (Bauer normalization) against bare ξ = energy mismatch (entry 2.1). Use ξ_B or write
  the number.
- GAP, unregistered symbols (no NOTATION rows): σ_F, μ_M, G_S/G_P/G_V/G_A, g_eff, 𝒢_a, ω_γ, ω_C, σ_Th, β_c, q_Δ, v_Δ, k_*,
  ω_line, q_line, N^acc_nl, S^at_nl, δ_mv/δ_oo (check 4.3), H_oo, T_ij, E_ee, H_sg, 𝒯^C, 𝒯^{(2)}_ab, J_a, ε'', Γ_pair, D_eff,
  p_K, r (fermionic ratio). Only x (10.8) and 𝒬 (10.9) are registered.
- Conventions: e² = 4πα, S_nn(free) = 2πn_eδ, S = (2q²/e²)L and the 1/(2ω) absorption normalization are used consistently
  in every formula I re-derived. I found no factor-2, π or sign drift against NOTATION/App. A.

## Sources

Fetched into sources/review-ch10/: 2401.11971, 2011.01940, 2507.14287, 2106.12586, 2305.05681, 1608.01994, 2608.20715,
2607.09352, 1412.8378, 2203.06664, 2308.00309, 2006.13918, 2509.14534. Already present and used: 2109.08168, 1509.01598,
2105.05253, 2105.02233. PDFs of the folders I fetched were deleted; the pre-existing folders were left to their owner.
