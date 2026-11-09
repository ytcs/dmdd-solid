# SEAM: E.18–E.21 (computational specifications: Migdal; anharmonic, disordered and quantum solids; magnetic, superconducting and Dirac targets; dopants, color centers, molecular and low-dimensional targets)

Length (wc): E-18.tex ≈ 2,060; E-19.tex ≈ 2,800; E-20.tex ≈ 3,230; E-21.tex ≈ 2,680 (total ≈ 10,800 against 8,000 budgeted; E.20 and E.21 carry
seven quantities each). No App. D file, no figures. Lint 0 blocking (remaining: long sentences, one SPINE-fixed title). Build: full main.tex into
/tmp/build-E-f, exit 0, no errors, no undefined citations; undefined references only to unwritten Chaps. 8, 11–16 (list below); one cosmetic
overfull running head (34 pt) from the long SPINE title of E.21.

## The reader now knows
- E.18: drag mass and inverse moments 𝓘₂–𝓘₄ of the force spectral measure dσ_κ (eq:E.18-moments); δM_κ = 2𝓘₃, P_Mig = q²𝓘₄/M_κ² (from 12.5);
  the bound P_Mig ≤ E_R δM_κ/(M_κE_g) in one line; free-atom δM/M = 2.7×10⁻⁴ (Si), 2.4×10⁻⁴ (Ge) keep P_Mig < 10⁻³ only to E_R ≈ 4.3, 3.1 eV;
  two-solve Sternheimer formulas (eq:E.18-sth); RPA δM from the ω² slope of Φ^el(iω); trace rule Σ δM(Q = 0) = N_e m_e per cell; GaAs zero-field
  and gap pitfalls. Crystal Migdal joint response: AE RPA+LFE S^ee (p ≤ 30 keV, ω_e ≤ 100 eV), four closure checks incl. the neutron
  measurement proposal of Adams et al.; (1 − P_Mig), M + δM bookkeeping. Non-rigid Wannier ratio 𝔯_W (eq:E.18-rW), absolute bound coefficient
  1.56 (20 eV), 0.25 (100 eV); bare vertex screened at ω_e. Couplings not ∝ mass: eq:E.18-X, (200) zero, (111), (220) weights 2, 4.
- E.19: exact moments 𝓜⁰–𝓜⁴ of the self response by PIMD, Markov–Krein band (absolute; tail upper bound only); TRPMD/CMD/SSCHA ladder with full
  convergence block; Kubo-transform restriction T ≳ ω/10 (not at 10 mK); solid ⁴He (Aziz, 21 cm³/mol, 1 K, P = 64 → 128). Time-reversal
  cancellation of first-order Φ³, so the leading anharmonic correction is n_A = 2 (editor ruling). Glass models; C^IR from the Born-charge
  structure factor with branch weights ŵ_ν ∝ c_ν⁻³ (eq:E.19-CIR); locally neutral charge models forbidden. Reflection force above σ_crit
  (eq:E.19-wall), σ_crit ≈ 1.2×10⁻³⁸ cm² (Ti–6Al–4V, 20 eV, v = 10⁻³), ρ_χv² ≈ 5×10⁻¹¹ Pa. Chiral-phonon branching as a linear system
  (eq:E.19-branch), with isotope scattering and loss; giant-moment amplitudes by the projector derivative.
- E.20: conserving BCS vertex fraction 𝔳 for Al (inputs 𝒩_F, v_F, Δ_BCS = 0.18 meV only); amorphous WSi five-stage chain; Holstein absorption
  eq:E.20-holstein with EPW α²F_tr and strong-coupling weights; DFT + U magnet inputs (editor Heisenberg convention); two-magnon ladder,
  ΔS = 0.078 and W_∥/W_⊥ = 0.146, 0.049, 0.029; orbital form factors ⟨j_K⟩, K ≤ 6; finite-q optical activity 𝒢_OA; ZrTe₅ in book α̃:
  α̃ = α/(ε_bg v_D) ≈ 0.2 (0.19 from the implemented row of Geilhufe Tables 1–2 as in we:7-zrte5: Δ_D = 15.6 meV, v_D = 7.6×10⁻⁴,
  ε_bg = 50.5, g_deg = 2; 0.20 from Hochberg Table 1), Ry_D ≈ 0.14 meV, a_D ≈ 1.0×10³ Å (revised 2026-11-02; superseded values 0.22/0.15/2.0×10³); Dirac re-plot factors ε_bg²,
  ε_bg^{1/2} (1600/6.3 at 40; 640/5.0 at 25.3), no 0.55–0.62 factor on top.
- E.21: NV⁻ transition densities (eq:E.21-gamma), q range capped at ≈ 25 keV by SG15 C unless AE reconstruction; Si:P disorder average with
  valley–orbit momenta 3.88, 0.685, 2.74, 2.33 keV; the misprint of Du et al. (factor ≈ 0.6–1.5 with fixed ε); molecular GW-BSE vs Frenkel with
  θ_CT; low-D RPA tables (projected f-sum, N_ch = 4 charge mode); R_OPW (eq:E.21-ROPW) and Sommerfeld upper bounds 7.3, 3.4, 2.6; ionic color
  centers (p_FH, p_surv, E_d(r̂); measured controls); bond breaking with p_esc.

## Symbols introduced (with defining equation) — proposals for NOTATION
- dσ_κ(Δ), 𝓘_k: spectral measure of the force on nucleus κ and its inverse moments (eq:E.18-moments) | eV-based | E.18.
- 𝔯_W(q, ω_e); A^DFPT, A^W: non-rigid Wannier ratio; Migdal amplitudes with the true and the Wannier vertex (eq:E.18-rW) | 1 | E.18.
- c_κ, c̃, δc̃_κ: nucleus coupling of a scalar, its mass-proportional part and remainder (c_κ/M_κ = c̃ + δc̃_κ); Ξ_G(k) (eq:E.18-X) | E.18.
  (Chap. 12.6 may introduce c_κ first; Ξ chosen to avoid 𝒲, the band window, and 𝒞_κκ′.)
- δ_anh(q, ω): relative anharmonic correction S/S^harm − 1 | 1 | E.19.
- S^Z_ν(k), ŵ_ν, M̄: Born-charge structure factor of branch ν, branch weight c_ν⁻³/Σc⁻³, mean atomic mass (eq:E.19-CIR) | E.19.
- b_χN, V_opt, R(v_n), R_slab, P_wall: χN scattering length (σ_χN = 4πb²), optical potential, step and slab reflectances, wall pressure
  (eq:E.19-wall) | E.19. (R here is a reflectance; the resolvent R of the giant-moment paragraph is local.)
- L^ph_Qν, L_th, 𝖬_λλ′ (sans-serif), b_λ, 𝒩^ch_λ, t_obs: phonon angular momentum, threshold, branching matrix, terminal indicator, mean
  terminal count (eq:E.19-branch), observation time | E.19. (κ_URF is not used, per clash entry 54.)
- P_K, E_K, H_CF, R: ground-Kramers-doublet projector and energy, crystal-field Hamiltonian, reduced resolvent | E.19.
- ξ_coh = v_F/(πΔ_BCS): BCS coherence length (if 15.1 has not named it) | nm | E.20.
- 𝔳(q, ω), R^cons, R^bare: conserving vertex fraction; conserving and bare density responses of BCS | 1 | E.20.
- ⟨L⟩, P_Δ: configurational-average loss function; local-gap distribution | E.20.
- σ₁^S(ω), α²F_tr, N_s, P_s, λ_tr: Holstein conductivity (eq:E.20-holstein), transport Eliashberg function, Eliashberg pair weights, transport
  coupling | E.20.
- S^(2m)(q, ω): interacting two-magnon response | eV² | E.20.
- ⟨j_K(q)⟩: radial form-factor integrals | 1 | E.20.
- 𝒢_OA(q, ω): odd (antisymmetric) part of the current response | 1 | E.20.
- Ry_D, a_D, v_D,i, ε_bg,ii, Λ_D,i: Dirac exciton Rydberg and radius; direction-resolved Dirac parameters | E.20.
- γ^FI_ij: one-body transition matrix of active-space states (eq:E.21-gamma) | 1 | E.21.
- t_CT, θ_CT, E_CT, E_Fr: charge-transfer integral, mixing angle, CT and Frenkel energies | E.21.
- r_t: tube radius (low-D kernel) | Å | E.21.
- R_OPW, M_OPW, M_PW: rate-weighted orthogonalization factor and amplitudes (eq:E.21-ROPW) | 1 | E.21.
- p_FH, p_q, f_opt, E_d(r̂): STE → Frenkel-pair probability, charge-state factor, readout fraction, direction-resolved displacement threshold
  (E.21; p_surv as 19.4; the creation probability is described in words to avoid P_FP of E.23 / p_FP of E.11).
- S_int, S_CM, p_esc, μ₁₂, m₁: internal and center-of-mass responses, cage-escape probability, bond reduced mass, struck-atom mass | E.21.

## Terms introduced
- drag-mass trace rule; non-rigid Wannier ratio; vertex fraction (conserving BCS); Born-charge structure factor; reflection force of a random
  medium; terminal chiral set; rate-weighted orthogonalization factor; cage escape (computational).

## Threads: none opened or closed (specification sections).

## Promises / pointers made
- To 12.3 (crystal Migdal convolution, impulse bracket, Wannier picture with ket-side ordering), 12.5 (δM = 2𝓘₃, P_Mig = q²𝓘₄/M², contact-density
  third moment, atomic per-shell P_Mig), 12.6 (acceleration form; reduction to the loss function for c ∝ M).
- To 11.5 (moments, Markov–Krein band, exact linear constraints of the anharmonic increment), 14.5 (chiral phonons, L^ph, giant moments),
  16.7 (Born random-medium rate, σ_crit, C^IR).
- To 15.1 (conserving form, kinematic grid), 15.3 (relaxation-time forms invalid), 15.4 (Holstein formula, open renormalization factors),
  14.1 (W_∥/W_⊥, ΔS), 14.2 (ladder, bound states), 14.5 (𝒢_OA), 16.1 (Ry_D, ε_bg² and ε_bg factors).
- To 16.2–16.6 (kernels, dot embedding and confinement factors, Frenkel/CT model, multivalley donors and the GOS misprint, yield factors).
- Cross-appendix: app:E.17 (lattice tables, PIMD kinetic energy), app:E.22 (tunneling-path machinery for p_surv).
- Not pointed to by cref: Sect. 14.3 (absorption into magnons). The uniform-mode output of the magnon code is mentioned in words in E.20 only,
  because 14.3 is not in the row's pointer list.

## Undefined references in the build (all to unwritten sections)
sec:8.3, 8.5, 8.8, 11.5, 12.3, 12.5, 12.6, 14.1, 14.2, 14.5, 15.1, 15.3, 15.4, 16.1, 16.2, 16.3, 16.4, 16.5, 16.6, 16.7.

## Proposed ledger rows (the editor merges them)
NOTATION: the symbol rows above. ·
GLOSSARY: drag-mass trace rule — the sum of the Q = 0 drag-mass tensor over a cell equals N_e m_e · non-rigid Wannier ratio — |A^DFPT|²/|A^W|² ·
rate-weighted orthogonalization factor — R_OPW · cage escape — fragments leaving the molecular site in a crystal. ·
CONCEPTS: exact static moments as the acceptance test of approximate quantum dynamics; time-reversal cancellation of first-order cubic
anharmonicity in S_κκ; branching expectations as a linear system. ·
CLAIMS: P_Mig bound [derived here in one line from 12.5]; eq:E.18-sth [derived in place]; eq:E.18-X [derived in place from the acceleration form];
eq:E.19-CIR [derived under the plane-wave hypothesis]; eq:E.19-wall [derived in place]; eq:E.19-branch [derived, first-step analysis];
eq:E.20-holstein [from 15.4; Debye limit = Hochberg, Lin, Zurek Eqs. (16)–(17)]; ZrTe₅ α̃, Ry_D, a_D [computed in the book's α̃; inputs
Geilhufe et al.]; numbers 1.56/0.25, ΔS and W_∥/W_⊥, Sommerfeld factors, valley momenta [derived/checked arithmetic]; OPW ratio ranges and the
misprint factors [model estimates, labelled as such in the text]; NV⁻ 1.945 and 1.19 eV [Doherty et al. 2013]. ·
INDEX: drag mass (computation); inverse moments; Migdal effect (computation); Wannier picture (non-rigid ratio); Markov–Krein band
(computation); ring-polymer molecular dynamics; centroid molecular dynamics; stochastic self-consistent harmonic approximation; glass models;
infrared coupling (glass); optical potential; MICROSCOPE; chiral phonons (decay); crystal-field derivatives; conserving response (BCS);
amorphous WSi; Holstein absorption (Eliashberg); DFT + U exchange constants; two-magnon bound states; magnetic form factors (non-dipole);
optical activity (finite q); ZrTe₅; Dirac re-plot; nitrogen–vacancy center (transition densities); Si:P impurity band; charge-transfer
excitons; low-dimensional RPA; orthogonalized plane waves; F centers (creation); bond breaking.

Sources read (text extracts kept, PDFs deleted): sources/E-f/{2609.06423, 1604.06800, 1910.02091}.txt — Gan et al. Eq. (7), Hochberg–Lin–Zurek
Eqs. (16)–(17), Geilhufe et al. Eqs. (3.13)–(3.14) (the q_x²v_F,z² slip confirmed in (3.14)), Tables 1–2 (κ = 308.4, 20.75, 126.1) checked.

Bib (appended, IDs and DOIs checked against arXiv API and Crossref): adams2023measuring, liang2020describing, rossi2014remove,
monacelli2021time, eriksson2019hiphive, taraskin2006universal, liu2025coherence, romao2023chiral, gan2026mean, hochberg2016absorption,
margine2013anisotropic, toth2015linear, zabalo2023natural, du2022doped, essig2017detection. Reused: sangalli2019many, deslippe2012berkeleygw,
pizzi2020wannier90, kapil2019ipi, monacelli2021stochastic, togo2015distributions, ponce2016epw, timrov2018hubbard, he2021tb2j,
colpa1978diagonalization, geilhufe2020dirac, hochberg2018detection, doherty2013nitrogen.

## Revision (2026-11-02, App. E.14–E.27 review)
- E.18: drag-mass inputs are the shared base of E.17 (60 Ry); cost 2× base (200/30/40 core-h Si/Ge/GaAs). Crystal Migdal S(q;ω_l,ω_e) in eV⁻² per cell; matrix at 72 reduced p of a 12³ grid, contracted on the fly; ≈ 10⁴ core-h. Neutron Migdal check conditional on the proposed measurement. New label app:E.18-drag.
- E.19: dynamics at 50 and 100 K, bands at mK; first MOF named, InF₃(4,4′-bipyridine) (romao2023chiral); lanthanide host/ion → 14.5; glass boxes 4.3 nm (5184) and 3.0 nm (1728, size test only).
- E.20: α̃ = α/(ε_bg v_D) defined at use (eq:7.3-alpha); ZrTe₅ parameters as we:7-zrte5 (see the corrected line above); new tab:E20-dirac (ZrTe₅, Yb₃PbO, BNQ-TTF from Geilhufe Tables 1–2); subsection title "ZrTe₅ and corrected Dirac reaches"; magnetoelectric crystal Cr₂O₃; new label app:E.20-magnet; v_F(Al) = 2.0×10⁶ m/s.
- E.21: single short title "Dopants, color centers and small targets"; NV 80 Ry, Γ checked on 2³; color centers on an ML surface fitted to ΔSCF (direct hybrid surface hopping 10⁶–10⁷ core-h); bond breaking: anthracene, C–H; donor S per donor in eV⁻¹; low-D S per area/length with 2πδ.
