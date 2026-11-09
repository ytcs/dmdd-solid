# SEAM: Appendix C.18–C.20 (Mathematical tools, third block)

Length (wc on .tex, math included): C-18 2,197; C-19 1,192; C-20 2,298; total 5,687 (spine 1,500 + 1,200 + 1,300 = 4,000; C.18 and
C.20 carry full derivations of the cubic Rayleigh bound, the normal-incidence impedance law, the bath correlation function, the ohmic
NIBA rate and the Peierls–Nabarro barrier). appC.tex inputs C-18, C-19, C-20 after C-17, before \printbibliography.
Build: wrapper of main.tex without ch05 (s5-1.tex, being drafted elsewhere, has unfilled placeholders `\SI{UZERO}{…}` that stop
siunitx), `latexmk -pdf -f -outdir=/tmp/build-C-c`: 0 LaTeX errors from C.18–C.20, 0 undefined citations book-wide, 0 overfull boxes
in C.18–C.20. Remaining book errors are missing figures figures/ch03/fig3_11.pdf, fig3_12.pdf (not mine).
Lint: C-18 one EQ-PUNCT false positive (punctuation sits inside `aligned`, eq:C.18-cubic); LONG-SENT false positives where the linter
merges a sentence across a display (keyresult of eq:C.18-rayleigh; C-20 before eq:C.20-FK). No banned terms.
Figures: none (spine lists none). Sources (text extracts, PDFs deleted): sources/C-c/1805.02495.txt (Si tensor and Lamé pair, Table I),
1806.11002.txt (Eqs. (1)–(6)), 2504.02927.txt (Eqs. (2), (8), (21)–(26)), cond-mat_9409105.txt (Eqs. (2), (6)–(10)), 1910.10716.txt
(read for App. A3; not cited here).
Bib appended (DOIs checked against Crossref, arXiv IDs against the arXiv API, 2026-11-02): landau1986theory (10.1016/C2009-0-25521-8),
squires2012introduction (10.1017/CBO9781139107808), lovesey1984theory (no DOI), berlin2025determining (2504.02927, 10.1103/4yxf-lkr6),
blume1963polarization (10.1103/PhysRev.130.1670), moon1969polarization (10.1103/PhysRev.181.920), leggett1987dynamics
(10.1103/RevModPhys.59.1), qureshi1995dynamics (cond-mat/9409105, 10.1103/PhysRevB.52.7976), braun2004frenkel
(10.1007/978-3-662-10331-9), fitzgerald2018structure (1806.11002, 10.1142/S2424913018400039). Existing keys reused:
martinez2019measurements, kittel2005introduction, swartz1989thermal.
Numbers checked by script (scratchpad checks.py, checks20.py, pn.py):
- C.18: Christoffel eigenvalues of Si (165.6, 63.9, 79.5 GPa; 2.33 g/cm³): LA 8.430, 9.131, 9.352 km/s along [100], [110], [111];
  TA 5.841 (×2), 5.841 and 4.672, 5.091 (×2). B = 97.8 GPa, √(B/ρ_T) = 6.479 km/s (23% below min c_LA = 8.432). E.12's form
  C_ijkl Q_jQ_k ê_l equals C_ijkl Q_jQ_l ê_k (checked numerically). Isotropic Lamé pair (52.4, 68.0) → 8.99, 5.40 km/s = E.12's 9.0,
  5.4. Si anisotropy 2C₄₄/(C₁₁ − C₁₂) = 1.563; Al 1.223. Al (106.8, 60.7, 28.2 GPa; 2.70 g/cm³): c_LA 6.289 [100], 6.488 [111].
  Z_ac Si[100] 19.64, Al[100] 16.98 (10⁶ kg m⁻² s⁻¹); t₁₂(0) = 0.9947. Critical angle arcsin(6.29/8.43) = 48.3°.
  For 11.1 and 17.5 (not printed here): Si c̄_LA = ⟨c_LA⟩ = 9.017 km/s (80 Gauss–Legendre × 160 φ); ⟨Σ_ν(q̂·ê_ν)²/c_ν⟩⁻¹ = 8.956 km/s;
  ⟨c⁻³⟩⁻¹ᐟ³ (three branches) = 5.886 km/s.
- C.19: (γ_n r_cl)² = (1.91304 × 2.81794 fm)² = 29.061 fm² = 0.2906 b. Constants (m_n/2π)·2γ_nμ_Nμ_B = γ_n r_cl m_n/m_p.
- C.20: ∫₀^∞dx(1 − cos ax)/(x(eˣ − 1)) = ½ln[sinh πa/(πa)] (a = 0.1…2); T = 0 integral ½ln(1 + ω_c²t²); full Re 𝒬(t) vs eq:C.20-Qohm at
  T/ω_c = 0.01, t = 150/ω_c: 3.730 vs 3.740. NIBA closed form eq:C.20-ohmrate vs direct quadrature of eq:C.20-rate with eq:C.20-Qohm at
  (α, T/ω_c, Δ_as/ω_c) = (0.3, 0.01, 0), (0.3, 0.01, 0.02), (0.2, 0.005, −0.01), (0.4, 0.02, 0.05): agreement to 10⁻⁹. Duplication form
  at Δ_as = 0 equal. Small-α equivalence with Qureshi's Δ̃₀²/γ₀ (both → Δ₀²(2πT/ω_c)^{2α}/(2πTα)). Kink energy integral = (2a/π)√(2V_sK)
  (Fitzgerald Eq. (3)) at βa² = 20, 50, 100. Equipartition PN barrier: direct lattice sum = eq:C.20-EPN to all digits; Fitzgerald Eq. (6)
  is half of it. Relaxed discrete chain (L-BFGS, 601 atoms): barrier/formula = 0.674 (d = 0.71a), 0.778 (d = 1.007a), 0.827 (d = 1.233a).
  M_kink/M_κ = 2/(3π²) = 0.068 at d = 3a; E_PN = 3.4×10⁻⁶V_s at d = 2a.

## The reader now knows
- C.18: displacement field as the continuum limit of eq:A.6-u; strain eq:C.18-strain; energy density w_el eq:C.18-energy with the 21
  symmetries; stress σ_ij and Hooke's law; equation of motion eq:C.18-eom; Voigt map and the factor 2 on shear strains (pitfall → E.4);
  cubic C₁₁, C₁₂, C₄₄, eigenvalues of the cubic form, Born stability eq:C.18-born; bulk modulus eq:C.18-bulk (Voigt/Reuss named);
  isotropic medium and Lamé constants (literature λ, μ quoted once), Si isotropic convention vs measured tensor; Christoffel equation
  eq:C.18-christoffel and matrix 𝖬 (symmetric, positive definite), link to D^dyn and to c_ν, ê_ν; quasi-L/T, group velocity ≠ phase
  direction; cubic eigenvalues eq:C.18-cubic with Si values; Rayleigh-quotient bound eq:C.18-rayleigh **proved** for cubic, Born-stable;
  sphere average eq:C.18-average and the three averages used later; quadrature recipe, branch-degeneracy kinks, 1/48 wedge;
  impedance eq:C.18-impedance, normal-incidence r, t, energy flux ½Z_acω²A², t₁₂(0) eq:C.18-transmission **derived**, symmetric;
  Si/Al 0.995; acoustic Snell law eq:C.18-snell, mode conversion, critical angle (Al → Si 48°).
- C.19: neutron kinematics in the book's q, ω; 𝛍_n = γ_nμ_N𝛔_n; spin magnetization −2μ_B s_e; B_e = P_T M_e eq:C.19-field **derived**
  from magnetostatics, with the demagnetizing-field picture; amplitude eq:C.19-amplitude with r_cl; cross-section eq:C.19-cross in S_ab
  (O_a = s_e,a), (γ_n r_cl)² = 0.2906 b; dictionary to Berlin et al. Eq. (26) (σ vs σ/2, per formula unit); Debye–Waller absorbed;
  spin-only form factor eq:C.19-spinonly (⟨j₀⟩), dipole form factor eq:C.19-dipole with the (g_J/2) prefactor and the 2/g_J − 1 weight
  derived from the spin ⟨j₀⟩ and orbital ⟨j₀⟩ + ⟨j₂⟩ parts (the latter stated, Squires); neutron sees S + L/2, spin probe sees
  (g_J − 1)J; polarization matrix elements eq:C.19-polar; NSF/SF content; chiral term; XYZ channels (x ∥ q̂): SF ∝ S_yy + S_zz, S_zz,
  S_yy; S_xx absent from every channel (the structural fact; its consequence is 14.4's).
- C.20: spin–boson Hamiltonian eq:C.20-H, Δ_tl = (Δ_as² + Δ₀²)^{1/2} tied to 2.5; spectral density eq:C.20-J; superohmic phonons
  (ω³) and ohmic electrons eq:C.20-ohmic with α_ohm (literature α, K); displaced oscillators, H_R = D H_L D†; correlation C(t) = e^{−𝒬}
  eq:C.20-Q **derived** from eq:C.6-BCH and eq:C.6-bloch; T = 0 Poisson (Franck–Condon) reading; ohmic 𝒬 eq:C.20-Qohm **derived**
  (sum over Bose terms, sinh product); orthogonality catastrophe; golden-rule (NIBA) rate eq:C.20-rate from eq:2.5-corr; closed form
  eq:C.20-ohmrate **derived** (contour shift, Beta integral), detailed balance, symmetric form, T^{2α−1} anti-Arrhenius growth for
  α < ½ and its picture; small-α match to Qureshi Eq. (10); Δ_r eq:C.20-Dr (definitional, Leggett et al.'s prefactor) and the scaling
  limit; adiabatic-renormalization argument; validity Δ_r ≪ T ≪ ω_cut; coherent regime and localization at α ≥ 1 (stated, Leggett).
  FK Hamiltonian eq:C.20-FK; crowdion boundary values; discrete static equations eq:C.20-discrete (how 19.6's discrete profile is
  obtained); sine-Gordon eq:C.20-sG with c_ch, ω_s; kink eq:C.20-kink, width d_k; pointwise equipartition; E_kink eq:C.20-Ekink
  (= Fitzgerald Eq. (3)); Lorentz invariance and M_kink = E_kink/c_ch² eq:C.20-mass; PN series eq:C.20-PN **derived** (equipartition +
  eq:C.2-poisson); barrier eq:C.20-EPN; site/bond centering; relaxed-chain comparison; d_k/a_ch as the controlling parameter.

## Symbols introduced (proposed below)
𝐮(𝐫, t) (continuum displacement field), u_ij, w_el, C_ijkl/C_IJ (existing row), σ_ij, ε_I (Voigt strain), 𝖬_ik(Q̂), ρ_1, ρ_2,
Z_ac,i, r₁₂, t^amp₁₂, t₁₂(θ), θ₁, θ′, s_Q (local), c_TA (existing E.4 row); m_n, μ_N, γ_n, 𝛔_n, 𝐩_n, 𝐩′_n, 𝐁_e, 𝐌_e, r_cl, f̂_mag,
f̂_nuc, 𝐬_⊥, ϱ_s, R_sh, ⟨j_l(q)⟩, 𝐉_j, P̂; |L⟩, |R⟩, σ_x, σ_z (pseudo-spin), Δ₀, Δ_as, d_k, ω_k, λ_k, 𝒥(ω), ω_cut, b_k, δ_k, C(t), 𝒬(t),
Γ_LR, Γ_RL, Γ(z) (Euler gamma), Δ_r, p (local O(1) constant); a_ch, K_ch, V_s, z_n, u_n (chain), z_0, φ, c_ch, ω_s, d_k, E_kink, M_kink,
E_PN.

## Promises made to later sections
- 11.1: eq:C.18-christoffel, eq:C.18-cubic, eq:C.18-rayleigh (cubic only), eq:C.18-average and the quadrature recipe; C.18 says
  "\Cref{sec:11.1} evaluates c̄_LA for silicon in a worked example" (worked example 11.1). Script value 9.017 km/s for that example.
  Debye temperature (Anderson convention) is not treated here.
- 17.5: the polarization-weighted average ⟨Σ_ν(q̂·ê_ν)²/c_ν⟩ (its c_NR1 = inverse; Si 8.956 km/s by script); C.18 says 17.5 tests
  tabulated speeds against eq:C.18-rayleigh. c_LA,max = largest LA phase speed: for cubic it is [111] or [100] (linear in s_Q).
- 20.3: eq:C.18-impedance, eq:C.18-transmission, eq:C.18-snell, mode conversion and critical angle; C.18 says 20.3 "solves the oblique
  problem and averages it over angles". Si/Al numbers 19.6, 17.0, 0.995 and 48° are available for worked example 20.3 / Fig. 20.3.
- 14.4: eq:C.19-cross (P_T contracted with S_ab), eq:C.19-dipole with g_J/2, eq:C.19-polar and the XYZ channels; the no-go is left to
  14.4. 14.1 is pointed to for the magnetic insulators; 14.3 for g_J.
- 16.8: eq:C.20-H, -J, -ohmic, -Q, -Qohm, -rate, -ohmrate, -Dr; the anti-Arrhenius T^{2α−1} law is derived here in its general NIBA
  form, so 16.8 can apply it with α_ohm = 4K_b and the superconducting factor, and point back. C.20 says 16.8 computes α_ohm from phase
  shifts.
- 19.6: eq:C.20-FK, -discrete, -sG, -kink, -Ekink, -mass, -PN, -EPN; M_cr = M_kink of a crowdion row (E₀ of the spine is E_kink here);
  d_k/a_ch as the controlling parameter of limitbox 19.6b; the relaxed-chain ratios above for its plot.

## Undefined references from C.18–C.20 (all to unwritten targets)
sec:5.2, sec:5.6 (Chap. 5 omitted from the wrapper build; not yet written), sec:7.1, sec:11.1, sec:14.1, sec:14.3, sec:14.4, sec:16.8,
sec:17.5, sec:19.6, sec:20.3.

## Open questions / for the editor
1. **Fitzgerald Eq. (6).** 1806.11002 Eq. (5) has amplitude 2V₀π²/(µ²a²) per term and Eq. (6) a barrier 8V₀π²/(µ²a²)cosech(π²/µa).
   A direct lattice sum of the equipartition energy (his Eq. (4)) gives the barrier 16π²V₀/(µa)² cosech(π²/µa) (= eq:C.20-EPN with
   d_k = 1/µ, V_s = V₀), twice his Eq. (6) and four times the barrier (twice the n = 1 amplitude) implied by his Eq. (5). The book's form agrees with the asymptotic
   32π²g ε_s e^{−π²√g} usually quoted from Braun–Kivshar (g = (d_k/a)²). C.20 therefore cites Fitzgerald only for Eqs. (2)–(4) and gives
   its own barrier; 19.6 must not quote his Eq. (6) as the barrier. Braun–Kivshar is cited without an equation number (not read).
2. **Qureshi's K vs NOTATION's K_b.** Mapping Qureshi's bosonized coupling (his Eq. (2), two spin channels) onto eq:C.20-J gives
   𝒥 = 2πKω, so his K is α_ohm (Leggett's α), not K_b. NOTATION entry 61 says "the research's coupling K of a tunnelling defect is K_b",
   with α_ohm = 4K_b. If 16.8 cites cond-mat/9409105 Eqs. (8)–(10), it should read K there as α_ohm. C.20 says so in one clause.
3. **First-use moves.** P_T (row: 14.4), g_J (14.3), F^mag and s_e(q) (7.1), c_LA (10.2), c̄_LA and B (11.1), α_ohm (16.8), Δ_tl (2.5 only), c_TA (E.4), ê_ν (A.6 only): all now
   appear in App. C. The rows' first-use columns should add "C.18"/"C.19"/"C.20" (ê_ν: widen "A.6 only" to "A.6, C.18"; Δ_tl: widen
   "2.5 only" to "2.5, C.20").
4. **Rayleigh bound scope.** eq:C.18-rayleigh is proved for cubic, Born-stable crystals (as the research derived it). For lower
   symmetry the Rayleigh step ρc_LA² ≥ C_ijklq̂q̂q̂q̂ holds, but whether that quartic exceeds B in every direction is not established;
   17.5 applies the floor to CsI (cubic) only. Say so if a non-cubic use appears.
5. **Al constants.** Al ρ = 2.70 g/cm³ and C₁₁, C₁₂, C₄₄ = 106.8, 60.7, 28.2 GPa are cited to Kittel (8th ed.) without a table
   number; the editor may want a primary reference (Kamm and Alers 1964 give low-temperature values about 7% higher in C₁₁).
   Closed 2026-11-07 (final-residuals): no Kittel text is readable here, so the table-number request is dropped and the citation stays general.
6. **Gamma function.** C.20 uses upright Γ(z) (Euler's gamma function, always with an argument) next to italic Γ_LR rates; STYLE
   reserves argument-free upright Γ for the zone center. Proposed as a clash entry below.
7. **Pseudo-spin Pauli matrices.** σ_x, σ_z of the two-level system (C.20; 16.7, 16.8 will need them) break the rule that Pauli
   matrices appear only inside s_e; proposed as a row with the clash noted. The neutron's are 𝛔_n (bold, subscript).
8. **Stress σ_ij.** Two Cartesian indices mandatory; clash with σ (cross-section), σ₁, σ₂ (conductivity), σ_Qν (E.8) noted.
9. **Length.** 5,687 words against 4,000 planned: C.18 (+700) has the cubic eigenvalue table, the proved bound and the impedance
   derivation; C.20 (+1,000) derives the bath correlation, the closed-form ohmic rate and the PN series, which 16.8 and 19.6 would
   otherwise need as D items.

## Proposed ledger rows (the editor merges them)
NOTATION:
| 𝐮(𝐫, t) | continuum displacement field, long-wavelength limit of u_Rκ (bold; argument mandatory) | Å | C.18 |
| u_ij | strain tensor ½(∂_iu_j + ∂_ju_i) (two indices mandatory) | 1 | C.18 |
| w_el | elastic energy per unit volume ½C_ijklu_iju_kl | GPa | C.18 |
| σ_ij | stress tensor C_ijklu_kl (two Cartesian indices mandatory) ⚑ | GPa | C.18 |
| ε_I | Voigt strain vector (u₁₁, u₂₂, u₃₃, 2u₂₃, 2u₁₃, 2u₁₂) (one Voigt index mandatory) ⚑ | 1 | C.18 |
| 𝖬_ik(Q̂) | Christoffel matrix C_ijklQ̂_jQ̂_l (sans-serif; bold upright 𝐌 is a generic matrix of C.7) | GPa | C.18 |
| Z_ac | acoustic impedance ρc of a medium (subscript mandatory; Z is a charge number) ⚑ | kg m⁻² s⁻¹ | C.18 |
| ρ₁, ρ₂ | mass densities of the two media of an interface (C.18, 20.3) | g cm⁻³ | C.18 |
| r₁₂, t^amp₁₂ | displacement reflection and transmission amplitudes at normal incidence (C.18 only) | 1 | C.18 |
| t₁₂(θ₁) | energy transmission from medium 1 to 2 at incidence angle θ₁ (t̄₁₂ of 20.3 is its angle average) | 1 | C.18 |
| m_n, γ_n, μ_N | neutron mass; neutron magnetic moment in nuclear magnetons, −1.913; nuclear magneton e/2m_p | eV; 1; eV⁻¹ | C.19 |
| 𝛔_n, 𝐩_n, 𝐩′_n | neutron Pauli matrices; incident and outgoing neutron momenta (subscript n mandatory) | 1; eV | C.19 |
| 𝐁_e, 𝐌_e | magnetic field and spin magnetization of the electrons (subscript mandatory; 𝐁₀ stays the static field) | eV² | C.19 |
| r_cl | classical electron radius α/m_e = 2.818 fm (r_e is a position, A.3) | fm | C.19 |
| f̂_mag, f̂_nuc, 𝐬_⊥ | magnetic and nuclear neutron amplitude operators; transverse spin density P_T s_e(q) | fm; 1 | C.19 |
| ϱ_s(r), R_sh(r), ⟨j_l(q)⟩ | normalized unpaired-spin density of an ion; radial function of its shell; radial integrals of j_l | Å⁻³; Å^{-3/2}; 1 | C.19 |
| 𝐉_j | total angular momentum of magnetic ion j (bold, site index mandatory; J^μ and J^ex are distinct) ⚑ | 1 | C.19 |
| σ_x, σ_z | pseudo-spin Pauli matrices of a two-level system in the localized basis \|L⟩, \|R⟩ (C.20, 16.7, 16.8) ⚑ | 1 | C.20 |
| Δ₀, Δ_as, Δ_r | tunneling amplitude; asymmetry; renormalized tunneling amplitude (eq:C.20-Dr) (subscripts mandatory, entry 14) | eV | C.20 |
| d_k, ω_k, λ_k | bath oscillators, energies and couplings of the spin–boson model (k a bath-mode label; d_γ family of 2.3) ⚑ | —; eV; eV | C.20 |
| 𝒥(ω) | bath spectral density πΣλ_k²δ(ω − ω_k) (script J) | eV | C.20 |
| ω_cut | high-energy cutoff of a bath spectral density | eV | C.20 |
| 𝒬(t), C(t) | bath correlation exponent and overlap e^{−𝒬} (script Q; local to C.20, 16.8) ⚑ | 1 | C.20 |
| Γ_LR, Γ_RL | incoherent hopping rates between the configurations (italic \varGamma) | eV | C.20 |
| Γ(z) | Euler's gamma function (upright, argument mandatory) ⚑ | 1 | C.20 |
| a_ch, K_ch, V_s | spacing, spring constant and substrate-potential amplitude of a Frenkel–Kontorova chain (subscripts mandatory) | Å; eV Å⁻²; eV | C.20 |
| c_ch, ω_s, d_k | sound speed of the free chain; single-atom frequency in the substrate; kink width c_ch/ω_s | km s⁻¹; meV; Å | C.20 |
| E_kink, M_kink, E_PN | kink rest energy; kink mass E_kink/c_ch² (M_cr of 19.6 for a crowdion); Peierls–Nabarro barrier | eV; eV; eV | C.20 |
Clash notes: σ_ij joins the σ family (entry 32: σ, σ₁, σ₂, σ_Qν). ε_I (Voigt) against ε family (dielectric): one Voigt index
mandatory. Z_ac against Z_κ, Z*, Z_eff. 𝐉_j against J^μ, J^ex, 𝒥(ω). σ_x, σ_z pseudo-spin against the rule of entry 32 (Pauli matrices
only inside s_e): allowed as two-level operators in C.20, 16.7, 16.8. d_k joins d_γ (2.3), d_kj (C.16); d_k (kink width, upright k)
against d_k (bath mode): the kink width is d_{\mathrm{k}}, the bath operator d_k with italic index (consider renaming the width
d_kink at the next touch). 𝒬(t) against bold 𝐐 (phonon wavevector). Γ(z) (upright, argument) against Γ (zone center, no argument) and
italic Γ rates. λ_k (C.20 local) against λ (exciton label) and Lamé λ (literature, C.18 only). The literature's Lamé μ is quoted once
in C.18 (μ_χe etc. are decorated).
GLOSSARY:
| strain, stress | symmetric displacement gradient u_ij; force per area σ_ij = C_ijklu_kl | C.18 |
| Voigt notation | 6×6 form C_IJ of the elastic tensor, shear strains doubled | C.18 |
| Born stability conditions | positivity of the elastic energy; cubic: C₁₁ > \|C₁₂\|, C₁₁ + 2C₁₂ > 0, C₄₄ > 0 | C.18 |
| bulk modulus | −V dP/dV; cubic (C₁₁ + 2C₁₂)/3 | C.18 |
| Christoffel equation | ρc²ê = 𝖬(Q̂)ê for elastic plane waves | C.18 |
| quasi-longitudinal, quasi-transverse | branches whose polarization is near, not exactly, along or across Q̂ | C.18 |
| acoustic impedance | Z_ac = ρc | C.18 |
| acoustic Snell law, mode conversion, critical angle | sinθ/c conserved across an interface; L ↔ T conversion; evanescent beyond arcsin(c₁/c′) | C.18 |
| magnetic cross-section | (γ_nr_cl)²(p′/p)(V/2π)Σ(P_T)_abS_ab | C.19 |
| dipole form factor | ⟨j₀⟩ + (2/g_J − 1)⟨j₂⟩ | C.19 |
| spin-flip, non-spin-flip scattering | neutron channels seeing s_⊥ across and along the polarization | C.19 |
| spin–boson model | two-level system linearly coupled to a harmonic bath through σ_z | C.20 |
| spectral density; ohmic, superohmic bath | 𝒥(ω); 𝒥 ∝ ω; 𝒥 ∝ ω³ (3D phonons) | C.20 |
| orthogonality catastrophe | vanishing overlap of the two bath ground states for an ohmic bath | C.20 |
| noninteracting-blip approximation | rate second order in Δ₀ with the bath equilibrated in the initial configuration | C.20 |
| scaling limit, renormalized tunneling amplitude | Δ₀, T ≪ ω_cut at fixed α_ohm; Δ_r of eq:C.20-Dr | C.20 |
| Frenkel–Kontorova chain | harmonic chain in a periodic substrate potential | C.20 |
| sine-Gordon kink | 4 arctan e^{−z/d_k} solution of the continuum chain | C.20 |
| Peierls–Nabarro barrier | dependence of the kink energy on its position relative to the lattice | C.20 |
CONCEPTS: "Continuum elasticity and the Christoffel problem" | C.18 | `eq:C.18-christoffel`, `eq:C.18-rayleigh`. "Acoustic impedance"
| C.18 | `eq:C.18-transmission`. "Magnetic neutron cross-section and transverse projection" | C.19 | `eq:C.19-cross`, `eq:C.19-polar`.
"Spin–boson model, ohmic bath" | C.20 | `eq:C.20-Q`, `eq:C.20-ohmrate`, `eq:C.20-Dr`. "Frenkel–Kontorova kink" | C.20 | `eq:C.20-kink`,
`eq:C.20-mass`, `eq:C.20-EPN`.
CLAIMS:
- Cubic Rayleigh bound c_LA ≥ √(B/ρ_T) in every direction under Born stability | C.18 | derived (Rayleigh quotient + linearity in
  s_Q); Si 6.48 vs ≥ 8.43 km/s, checked numerically.
- Normal-incidence energy transmission 4Z₁Z₂/(Z₁ + Z₂)², symmetric | C.18 | derived (Swartz and Pohl attribution). Si/Al[100] 0.995 |
  C.18 | computed; Al constants from Kittel.
- B_e(q) = P_T M_e(q) from magnetostatics; cross-section eq:C.19-cross with (γ_nr_cl)² = 0.2906 b | C.19 | derived (Squires,
  Lovesey attribution). Dipole form factor eq:C.19-dipole | C.19 | derived given the stated spin/orbital radial weights (Squires).
  Polarization channels | C.19 | derived (Blume 1963; Moon, Riste and Koehler 1969).
- Bath correlation eq:C.20-Q and ohmic form eq:C.20-Qohm | C.20 | derived, checked numerically. NIBA rate eq:C.20-ohmrate with detailed
  balance | C.20 | derived, checked against quadrature (Leggett et al. attribution). Δ_r prefactor | C.20 | stated (Leggett et al.),
  scaling argued adiabatically. Coherent regime α < ½, localization α ≥ 1 | C.20 | stated (Leggett et al.).
- Sine-Gordon kink, E_kink, M_kink | C.20 | derived (= Fitzgerald Eqs. (2), (3)). PN barrier eq:C.20-EPN | C.20 | derived in the
  equipartition approximation; relaxed chain lower by 22% at d_k = a_ch, by 17% at 1.23a_ch (computed).
INDEX: continuum elasticity; strain; stress; Hooke's law; elastic constants; Voigt notation; Born stability conditions; bulk modulus;
Voigt and Reuss averages; Lamé constants; shear modulus; isotropic medium; Christoffel equation; Christoffel matrix; quasi-longitudinal
mode; phonon focusing; Rayleigh quotient; sphere average; Gauss–Legendre quadrature; acoustic impedance; reflection coefficient;
transmission coefficient; acoustic Snell law; mode conversion; critical angle; neutron magnetic moment; nuclear magneton; magnetic
neutron scattering; transverse projector; demagnetizing field; classical electron radius; magnetic form factor; dipole approximation;
Landé factor; polarization analysis; spin-flip scattering; chiral scattering; spin–boson model; spectral density; ohmic bath;
superohmic bath; displaced oscillators; orthogonality catastrophe; noninteracting-blip approximation; detailed balance; anti-Arrhenius
law; scaling limit; renormalized tunneling amplitude; adiabatic renormalization; Frenkel–Kontorova model; sine-Gordon equation;
kink; crowdion; kink mass; Poisson summation; Peierls–Nabarro barrier.
