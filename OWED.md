# OWED: calculations still owed

The tracker of every calculation the campaign specified, started or promised and has not closed. It is an index, compiled 2026-11-09 from the ledgers below; the ledgers hold the specifications and stay authoritative for them.

| Ledger | Holds |
|---|---|
| state/DEFERRED-COMPUTE.md | the specification of each DC item (physics, quantity, method, convergence, acceptance test, cost), the infrastructure list and the dependency graph |
| state/DC-RESULTS.md | results of the items run in phase 2; overrides the status lines of DEFERRED-COMPUTE |
| returns/R18, returns/R19 | the returns and referee reports behind DC-RESULTS |
| book/RESUME.md | book text and figures waiting on a calculation |
| state/LOOSE-ENDS.md | open problems (LE labels) that a calculation would close |

**Keeping it current.** When a calculation lands: record the result in state/DC-RESULTS.md, change the status in this file, and add the book sections that take the number to §6. Only a result marked VALIDATED in DC-RESULTS may be quoted in the book. A new owed calculation gets a row here in the same commit that first names it.

**Count (2026-11-09).** 98 DC items: 84 not started, 10 run in part or failed their control, 4 closed. 14 infrastructure items, none built. 35 book-phase items open (§4), 1 closed.

## 1. Started and not closed

These have code and a return in the repository. Each line states what remains.

| Item | State | Still owed | Where |
|---|---|---|---|
| DC-2-gw: Ge quasiparticle bands by G₀W₀ (Yambo; BerkeleyGW fallback) | Deferred by the user 2026-11-07. Only a timing benchmark exists: 3 of 7 planned variants, on a loaded machine, from a start Yambo reads as metallic. No physics result | The whole pre-registered run: starting points S1 (PBE+SOC) and S2 (PBE0+SOC), convergence in bands and screening cutoff, controls C1–C4, then E_min(q) if a start passes. Rerun the timing benchmark on a quiet machine first | code/DC-2-gw/PREREG.md; returns/R18/DC-2-gw-bench.md |
| DC-2: Ge zero-phonon edge and PAER window | HSE06+SOC failed its control (Γ below L). DFT+α (DC-2-alpha) failed pre-registered test T3 (masses +23 %, +39 %). Both routes closed | A band structure that passes the controls: DC-2-gw. Until then the Ge window stays an estimate | returns/R18/DC-2.md, DC-2-alpha.md |
| Ge LDA phonons (book Table 5.1) | X and L valid. Γ invalid | A clean q1 (Γ) rerun; then the LDA ω_TA(Q*) and edges, and the Γ entry of Table 5.1 | returns/R18/DC-4.md addendum |
| DC-4: Ge DFPT on a 6³ q grid | Converged on the q grid. TA fails the neutron-scattering control (X −13.5 %, L −11.6 %). Not refereed | A referee. A TA branch that passes the control (the LDA rerun above is the candidate) | returns/R18/DC-4.md |
| DC-41: Al BCS conserving response | Validated with corrections, one referee | The second referee the ladder asks for. Al anisotropy and film mean free paths in the referee report are unverified | returns/R18/DC-41.md, REF-DC-41.md |
| DC-49, DC-54, DC-36: Dirac-material replot, CRDM recast, MICROSCOPE reflection force | Partly validated, one referee. The returns contain withdrawn numbers | A rerun of all three. Light mediator below about 3 keV is undetermined. Any bound from the reflection channel is a conjecture until the DWBA of DC-36 is run | returns/R18/REF-DC-49-54-36.md §4 |
| DC-67: semi-analytic cascade library | Si physics stands (ε 3.7468 eV, F 0.11398). The library is not releasable: wrong below threshold across θ_ii = 3/2, 21 of 30 tables | Fix the below-threshold branch, regenerate the tables, restate the accuracy and coverage | returns/R18/DC-67.md, REF-DC-67.md |
| DC-91: small-cell survivor DFPT batch | Γ stage validated for C, 3C-SiC, LiF, NaF (not refereed). GaAs failed its control. 4³ stage partial, TA unconverged in all four | GaAs by a route that passes the control. 4H-SiC and Al₂O₃ (not run). The 6³ stage for slopes, sound speeds, ω_max and the phonon density of states. LiF and NaF frequencies need a control. A referee | returns/R18/DC-91.md |
| DC-93: CsI elastic constants | Closed from measured values (Vallin et al. 1964, abstract only) | The ranking rerun with the measured C_ij (the figure of merit 3.7–3.9 is a rescaling). Read the full paper | returns/R18/DC-93.md |
| DC-63 stage 1: Si full-band cascade (FBC) | Done and refereed | Stage 2 (DC-FBC-2 in §4): excitonic final states, GW-level impact-ionisation rates, DFPT electron–phonon couplings for both carriers, photon-seed k convergence; then Ge and GaAs with spin–orbit | returns/R19/FBC-v2.md |
| DC-5, DC-6, DC-7: Si Umklapp vertex, forbidden-edge ratio, window residuals | Done at estimate level in returns/R16/CW1.md | The tier-H values, which need DC-1. For DC-7: the finer q̂ search and the spin–orbit admixture | returns/R16/CW1.md, CW1-errata.md |

Closed in phase 2, nothing owed: DC-83 (Kaplan-buffer recheck, validated).

## 2. The deferred-computation list (DC-1 to DC-98)

Status: OWED = specified, not run. PART = run in part, see §1. P = priority (P1 narrative-critical, P2 completes a channel or ranking row, P3 refinement). "needs" lists blockers: INF items are in §3, DC items must run first. The full specification of DC-n is the section "DC-n" of state/DEFERRED-COMPUTE.md.

Critical path for the P1 items:

```
INF-4 (quadrupoles) ─┐
INF-2 (Wannier ρ) ───┼─→ DC-1 Si tier H ─→ DC-6 ratio ─→ book Ch. 13
INF-3 (PAER kernel) ─┘        └─→ DC-8 GaAs decoy, DC-3 Ge tier H, DC-38
DC-4 Ge phonons ─→ DC-2 Ge window (now DC-2-gw) ─→ DC-3 Ge tier H
```

Never started although listed for the 4-core box (DEFERRED-COMPUTE §4, phase 0): DC-39, DC-16, DC-7 remainder, DC-18, DC-82, DC-89, the first pass of DC-78 and part N1 of DC-17.

### A. Electronic sector and PAER

| ID | P | status | quantity | materials | needs |
|---|---|---|---|---|---|
| DC-1 | P1 | OWED | Si PAER loss function L^PA(q,ω) from the full (M.1) amplitude, then rate dℛ/dω and reach σ̄_e^95 (tier H, T6) | Si | INF-2, INF-3, INF-4, INF-1; DC-17 feeds the pair/LFE term |
| DC-2 | P1 | FAILED-CONTROL on HSE06+SOC and on DFT+α; next route is GW (DC-2-gw), deferred | Ge zero-phonon kinematic edge E_min^ZPL(q), PAER edge and window m_χ^PA, m_ZPL (HSE06+SOC Wannier bands) | Ge | DC-4; no new code |
| DC-3 | P2 | OWED | Ge PAER tier H rate and reach (as DC-1 with SOC and L-valley classes) | Ge | DC-2, DC-1, INF-2, INF-3, INF-4 |
| DC-4 | P1 | PART: q-grid converged, TA fails the INS control, not refereed; Ge LDA Γ rerun owed | Ge DFPT on a 6³ q grid, and the Ge results COMP-PH left as placeholders (GE_TABLE, GE_WIN, GE_INS, GE_WTA, GE_MPAER, GE_AXIS, GE_CTRL, GE_QCONV, GE_K) | Ge | none |
| DC-5 | P1 | DONE at [E] level (R16/CW1 §2); tier-H part rides on DC-1 | Magnitude of the Si (2̄00) Umklapp density vertex \|ρ_cv(k,q+G)\| and ∇_kρ_cv at the conduction extremum | Si | none |
| DC-6 | P1 | PART: done at [E] level (R16/CW1); the tier-H value needs DC-1 | Forbidden-ZPL / PAER ratio ϖ_II [E14] at the Si edge and +0.1 eV, from S^PA on WP1's (q,ω) grid | Si | DC-1, DC-5 |
| DC-7 | P3 | PART: LE-27 part done (R16/CW1); finer q̂ search and SOC admixture owed | Si window residuals: SOC admixture of the LA kink and (2̄00)-class LO minimum on axis (LE-27 remainder); finer q̂ search of E_min^ZPL for \|q\| < 1.3 keV | Si | none |
| DC-8 | P2 | OWED | CONTROLS C8 GaAs decoy: GaAs bands + [E13]-type window scan, then the tier-H pipeline with lpolar (Fröhlich) | GaAs | DC-1, DC-91, INF-2, INF-3, INF-4 |
| DC-9 | P2 | OWED | Finite-q BSE beyond TDA for Si/Ge with bound lines; exciton dispersion along Γ–X (both sides) and Γ–L; hydrogenic series with ab initio anisotropic masses | Si, Ge | INF-1 |
| DC-10 | P3 | OWED | Exciton–phonon replicas (W.14): converged finite-P BSE at the pocket set with EPW g^x | Si, Ge | INF-1, DC-9 |
| DC-11 | P3 | OWED | Crystal exciton Migdal (G-X8): finite-p BSE over the BZ inside the G6 code path | Si, Ge | INF-1, DC-25 |
| DC-12 | P3 | OWED | Frenkel / self-trapped excitons in NaI (localisation, binding, release) | NaI | INF-1; CW1 formula pointer still owed |
| DC-13 | P3 | OWED | G7 core and relativistic response: Ge 3d, Ga 3d, Si 2p core-level finite-q BSE with SOC (ZORA/FLAPW) | Ge, GaAs, Si | INF-1, INF-6 |
| DC-14 | P2 | OWED | Non-density operator library: G10 IP response tables (12 real functions Si/Ge) with exported R⁰_GG′; LFE screening of j_T and in-medium 𝒪₈ ratio; triplet channel beyond… | Si, Ge | INF-9, INF-1 |
| DC-15 | P3 | OWED | G11 electronic anisotropy S₄, S₆, S₈(\|q\|, ω): full-q RPA+LFE ELF projected on cubic harmonics | Si, Ge, GaAs | INF-1 |
| DC-16 | P3 | OWED | SOC mixing near the Ge edge and the SOC-lifted Si on-axis vertex | Si, Ge | DC-2 |
| DC-17 | P2 | OWED | X2 numerics: N1 1D two-band contact-kernel model vs real-time TDH; N2/N3 Si Route S (ZG supercell, RPA local fields) at q = 0 and 0.5/1/2 keV (δ_LF, δ_pair, Λ(q)); N4 ε̃… | Si (N1: model) | N1 none; N2–N4: INF-1 or Route-S code |
| DC-18 | P3 | OWED | X1 residual tags: frozen-strain deformation tensors D^n for Si (symmetric D^n under rotations, D/c_ν ≫ q, piezo-log relevance) | Si | none |

### B. Lattice, Migdal, anharmonicity, disorder

| ID | P | status | quantity | materials | needs |
|---|---|---|---|---|---|
| DC-19 | P2 | OWED | Shared harmonic stack A: DFPT force constants, eigenpairs, per-atom PDOS, B_κ, Z*, ε_∞ at 80 Ry on an 8³ q grid (experimental a; PBE vc-relax partner) | Si, Ge, GaAs | none; COMP-PH outputs replace the Si/Ge part when converged at 80 Ry |
| DC-20 | P3 | OWED | Coherent two-phonon S^(2)_coh(q,q̂,ω) at q < q_BZ and rate-level ℛ₂, ℛ₃ (CW2.1)–(CW2.3) | Si (then Ge, GaAs) | DC-19, INF-9 |
| DC-21 | P2 | OWED | G3 multiphonon library tables S(q,q̂,ω), P_ph(n_ph\|q,ω), ρ^ph_κν, f_coh, ℛ_n (HDF5) and G11 lattice anisotropy S_ℓm (Lebedev 590) | Si, Ge, GaAs (then survivors) | DC-19, INF-9, DC-20 |
| DC-22 | P3 | OWED | Valence charge deformation Δ_κα(Q+G) at q ≫ q_BZ (\|Q+G\| ≤ 20 keV) and core polarisation Δ^core_κ(q) (L4 add-on 𝒵_κα(Q+G)) | Si, Ge, GaAs | DC-19, INF-6 |
| DC-23 | P3 | OWED | Finite-q eκ factor Δ𝓃_κ(q,q̂) beyond hydrogenic 1s²: crystal valence AE density and finite-nucleus Dirac 𝓃_e(R_κ) | Si, Ge, GaAs | INF-6 |
| DC-24 | P2 | OWED | Drag mass δM_κ, inverse moments ℐ₂–ℐ₄, C_κ and P_Mig(E_R) by frequency-dependent Sternheimer | Si, Ge, GaAs | DC-19, INF-5 |
| DC-25 | P2 | OWED | G6 Migdal single code path: all-electron RPA+LFE S^ee_GG′(p,ω_e) (p ≤ 30 keV, ω_e ≤ 100 eV) convolved with S^GS_κκ; quenching-subtraction kernel; T2/LFE band (also the W… | Si, Ge | INF-1, INF-6, DC-21 |
| DC-26 | P3 | OWED | Non-rigid Wannier correction ratio 𝔯_W(q,ω_e) = \|A^DFPT\|²/\|A^(H_W)\|² with the bare ∇_RV screened by RPA+LFE at ω_e | Si, Ge, diamond | INF-1, DC-25 |
| DC-27 | P3 | OWED | X10 valence amplitude for c_κ not ∝ M_κ: S^ee_GG′(k → 0, ω) for \|G\| ≤ 6(2π/a), ω from E_g to 100 eV + core edges, contracted with (CW2.26) | Si (diamond-structure) | INF-1 |
| DC-28 | P2 | OWED | Loss function L(k,ω) = Im[−(ε⁻¹)₀₀] (RPA+LFE, scissor/GW gap, semicore) for every survivor, \|k\| ≤ 5 keV, ω ∈ [E_g, 5ω_p]; 𝓠_Mig,κ and w_acc⟨1/ω⟩ | all 42-pool survivors (WP8-U v4) | INF-1; DC-91/94/96/97 ground states |
| DC-29 | P3 | OWED | G3 PIMD inputs: nuclear momentum distribution 𝔫_κ(p), E^kin_q̂, ⟨∂²_q̂E^ad_0⟩ (= 𝔨₃^GS), 𝔨₄ pieces | Si, Ge | INF-7 |
| DC-30 | P3 | OWED | Non-perturbative anharmonicity and quantum crystals: TRPMD/CMD/SSCHA/TDEP F_s(q,t), S_self(q,ω) for soft-mode and light-atom targets; solid ⁴He moments and band (PIMD, A… | KTaO₃, SrTiO₃, LiH, solid He | INF-7 |
| DC-31 | P2 | OWED | G13 / G-F2 anharmonic nuisance template: phono3py fc3 (4×4×4, 128 atoms), hiPhive/TDEP fc4, bubble spectral function, W₃/W₄ contour sums, Δ^τ_A(q,ω) | Si (then Ge, GaAs) | INF-12, DC-19, DC-29 |
| DC-32 | P3 | OWED | Glass models: melt-quench MLIP glasses (648–5184 atoms, ≥ 5 quenches), full Hessians, Z*_I; amorphous S_dist at n_ph = 2, 3 (CW2.12′); IR coefficients A^IR, B^IR of C^IR… | a-SiO₂, a-Si, SiN_x | INF-13, INF-9 |
| DC-33 | P3 | OWED | Isotope B−L channel: Γ_iso(ω) exactly from isotope-resolved Hessians (4096-atom natural-Si supercells, 10 realisations); T = 0 two-phonon ε₂(ω) of Si from ∂Z*/∂u | Si | DC-19 |
| DC-34 | P2 | OWED | GaAs electron-scalar single-phonon rate as a near-cancellation: DFPT Z*, ε_∞ to ≲ 1% with LST data; PhonoDark-abs with vertex Z_κ − Z*_κ and the mixing term; Γ^ph_ν from… | GaAs | DC-19, INF-12 |
| DC-35 | P3 | OWED | Crystal NR bremsstrahlung: Z*_κ(ω) at zero macroscopic field for ω ∈ [0.05, E_g], n_r(ω), dℛ/dω_γdω_ph by (W.13) | GaAs (Si, Ge) | INF-5, DC-19, DC-21 |
| DC-36 | P3 | PART: one referee; rerun owed; reflection-channel bound stays [C] | Reflection/refraction force above σ_crit for the MICROSCOPE cylinders (CW2.25) and the DWBA for density fluctuations ⟨δnδn⟩ | Pt/Ti cylinders; random media | none |
| DC-37 | P3 | OWED | κ_URF in MOF cells (three-phonon branching with angular-momentum labels, (CW2.27′)) and giant-moment 4f orbit–lattice amplitudes ∂⟨s_e,L⟩/∂u (CASSCF-SO on embedded clust… | chiral MOFs; SMMs | INF-12, INF-7 |

### C. Fano/edge shell and WP0 extensions

| ID | P | status | quantity | materials | needs |
|---|---|---|---|---|---|
| DC-38 | P2 | OWED | Γ_Λ₀/δ map over (q, ω), Fano coefficient c_ν^F(Λ₀), K_ν ≥ 0 test, d11 edge-shell and onset-shell masks | GaAs (and Si) | c^F part: INF-3; Γ part: none |
| DC-39 | P3 | OWED | All-electron orbit–orbit f-sum shift δ_oo(q) (CW3.3) and total δ_rel = δ_mv + δ_oo | Si, Ge | crystal part only: INF-6 |
| DC-40 | P3 | OWED | Relaxed electron-channel static step 1 − ε_e⁻¹(q,0) = clamped step + 𝒢_GS(q) (CW3.4) with the electron-following charge Z^(e)_κ(q) from frozen-phonon supercells | Si, GaAs | DC-19; clamped step from DC-28 |

### D. Spin, superconducting, Dirac, low-dimensional and molecular targets

| ID | P | status | quantity | materials | needs |
|---|---|---|---|---|---|
| DC-41 | P2 | DONE with corrections; second referee owed (quote REF-DC-41 §7) | Al BCS response: GRPA vertex 𝔳_GRPA(q,ω) on the WP4 [4.2] grid; full Im ε^BCS, its KK transform and the 𝔰_BCS-corrected L^BCS table | Al | none |
| DC-42 | P3 | OWED | Amorphous WSi: ⟨L⟩(q,ω) from RPA+LFE on MLIP-quenched cells, Kubo–Greenwood σ₁, and Δ_BCS inhomogeneity P_Δ by BdG | a-W_xSi_{1−x} | INF-13, INF-1 |
| DC-43 | P2 | OWED | Magnon sector: two-magnon S^(2m)(q,ω) with the 1/S ladder and bound states (RG3); LSWT beyond Larmor (anisotropic, dipolar, AFM; demag) for absorption; magnon FOM r_2m a… | YIG, NiO, MnF₂, α-RuCl₃ (benchmarks) | DC-44 |
| DC-44 | P2 | OWED | Magnet inputs from DFT+U: exchange J^ex (four-state or TB2J), single-ion anisotropy, g tensors where no INS/ESR fit exists | YIG, NiO, MnO, Cr₂O₃, NiPS₃ | none |
| DC-45 | P3 | OWED | Non-dipole orbital magnetic form factors ⟨j_K(q)⟩ (K = 0…6) and multiplet-projected matrix elements for SOC ions | SOC ions of the WP8-U survivors | none |
| DC-46 | P3 | OWED | Finite-q optical activity 𝒢_OA(q,ω) and S_{j^αj^β}(±q,ω) with SOC (current vertex with the non-local commutator) | Te or α-SiO₂; one magnetoelectric target | INF-9, INF-1 |
| DC-47 | P3 | OWED | Finite-q multiplet transition densities \|⟨F\|ñ_e(q)\|I⟩\|² for the NV⁻ manifold (QDET/CRPA + CI) | diamond NV⁻ | none |
| DC-48 | P3 | OWED | Anisotropic massive-Dirac ZrTe₅: G₀W₀ (SOC) fit of k·p parameters and ε_bg,ii; analytic Elliott–Sommerfeld threshold; model BSE on a log-graded radial k grid; beyond-lad… | ZrTe₅ (Bi₂Se₃ ε_bg) | INF-1 |
| DC-49 | P2 | PART: one referee; rerun owed (quote REF-DC-49-54-36 §4 only) | Re-plot of the 1708.08929 / 1910.02091 scattering and absorption reaches with ε_bg², ε_bg and the 0.55–0.62 charge renormalisation | ZrTe₅, BNQ-TTF, Yb₃PbO | none |
| DC-50 | P3 | OWED | Superconducting Holstein absorption σ₁^{S,(2,1)}(ω) with Eliashberg spectral functions (EPW α²F, α²F_tr) | Al, Nb | none |
| DC-51 | P3 | OWED | Disorder-averaged donor response ⟨S^D(q,ω)⟩ of Si:P near the impurity band (multivalley EMT tight binding, 10⁴–10⁵ sites) with DFT central-cell check; impact number of t… | Si:P (n_D = 10¹⁸, 1.8×10¹⁸ cm⁻³) | none |
| DC-52 | P3 | OWED | Molecular crystals: periodic GW-BSE vs Frenkel/Hückel/PPP transition densities, charge-transfer weight θ²_CT, Frenkel form-factor tables (frenkel-ff) | anthracene, t-stilbene | INF-1, INF-9 |
| DC-53 | P3 | OWED | Graphene/CNT vacuum ejection: rate-weighted OPW factor R_OPW(E_kin) with all occupied orbitals; FSI with screened-hole scattering states; low-D RPA tables (lowd-rpa) for… | graphene, CNT, layered stacks, QDs | INF-9 |
| DC-54 | P3 | PART: one referee; rerun owed (quote REF-DC-49-54-36 §4 only) | Recast of 2401.11971 (CRDM) limits with the exact density-row ratio (1 − ω²/Q²)² and the transverse row | Si, Ge | none |

### E. Defects, TLS, cascades, yields, low-energy excess

| ID | P | status | quantity | materials | needs |
|---|---|---|---|---|---|
| DC-55 | P3 | OWED | Ohmic electron-bath coupling α_ohm of tunnelling defects from eigenphases of S_R S_L† (CW5-6) | crowdion in W, H in Nb, TLS in Al/AlOx, WSi | DC-56 |
| DC-56 | P2 | OWED | Release paths of eV-scale defects: Huang–Rhys S_HR,k, E_reorg, λ_eff along the MEP, ring-polymer instanton action; production catalogue (50 paths/material) and KMC rates… | Si, Ge close Frenkel pairs; Al SIA | INF-7, DC-61 |
| DC-57 | P3 | OWED | Crowdion in W (Peierls profile, polaron narrowing S_pol, FK mass, strain interaction with the parent vacancy) and Al ⟨100⟩ dumbbell / cluster 1D glide | W, Al | INF-7 |
| DC-58 | P3 | OWED | DM–TLS core vertex 𝔣^def_e(q) = ⟨R\|n_e(q)\|R⟩ − ⟨L\|n_e(q)\|L⟩ for real a-SiO₂ TLS (Method A: two SCFs; Method B: one Γ ph.x) | a-SiO₂ | DC-59 |
| DC-59 | P3 | OWED | TLS ensemble sampling: landscape filtering / swap-MC on MLIP glasses (≳ 10⁸ minimum pairs), NEB, λ_P, γ^def, 𝐩^def; tls_response tables ΩS̄^def | a-SiO₂, AlOx, a-WSi | INF-13, INF-9 |
| DC-60 | P2 | OWED | Close-collision electronic excitation kernel dP/dω_e(b_imp, E_coll) for Si–Si, Ge–Ge collisions (E_coll 50 eV–5 keV) with the xc nuisance θ_LZ | Si, Ge | INF-8 |
| DC-61 | P2 | OWED | NR partition tables P(ℋ, E_st, N_eh \| E_R, r̂_R, T), anisotropic E_d(r̂_R) and P_FP, created-phonon spectra (WP5-AUD B-1), E_st with the quench protocol and one shared… | Si, Ge (then survivors: GAP:E_st1_p_surv, GAP:y_ion_QF) | INF-7 |
| DC-62 | P2 | OWED | Charge yield below E_R,th (B-2): P(N_eh \| E_R, r̂_R, T) on [20 eV, 1 keV], 𝔶(E_R), F_NR(E_R), P(N_eh = 0) | Si (validation 2303.02196), Ge (2405.10405) | DC-60, DC-61, DC-63 |
| DC-63 | P2 | PART: stage 1 for Si done and refereed (R19/FBC-v2); stage 2 and Ge, GaAs owed (DC-FBC-2) | Ab initio hot-carrier cascade: G₀W₀ bands, full-frequency ε⁻¹_GG′(p,ω) to 60–100 eV, ii kernel (W1′), EPW e–ph kernel, full-band cascade → P_n(q,ω,T), ε_eh, F_eh, decomp… | Si, Ge, GaAs | INF-1, INF-4, INF-14 |
| DC-64 | P2 | OWED | Ab initio ε_eh and F_eh for wide-gap and polar survivors (priority Al₂O₃, CaWO₄, LiF, NaF; then 4H-SiC F, C, 3C-SiC, GaN, AlN, TeO₂) | Al₂O₃, CaWO₄, LiF, NaF, 4H-SiC, C, 3C-SiC, GaN, AlN, TeO₂ | DC-63, INF-1, INF-14, DC-68 |
| DC-65 | P3 | OWED | Energy dependence ζ(E) of the ii-rate ratio Γ_ii^NEGF/Γ_ii^(W1) (G₀W₀ Im Σ with and without Z_kn, + SOSEX) and its effect on F_eh through (EF7) | Si | INF-1, DC-63 |
| DC-66 | P3 | OWED | k-resolved osc_k m_k(E) and w_mem(E) for Si between 3 and 8 eV (bound (CW5-1) on the energy-only reduction) | Si | DC-63 |
| DC-67 | P2 | PART: Si physics stands; the cascade library is not releasable (wrong below threshold in 21 of 30 tables) | Semi-analytic cascade library: P_casc(N \| x_e, x_h; θ) tables for every Λ-sector and survivor (cascade_gf.py), and the GAP-EF(-v2) rerun on ω₀-commensurate grids | 27–42 survivors | none |
| DC-68 | P2 | OWED | Exciton and capture parameter set: G₀W₀+BSE E_x^b, a_x, oscillator strengths; D⁰X/A⁰X central-cell DFT; cascade-capture σ_cap(E,T,ℰ_b) with EPW rates; deep-level multiph… | Si, Ge (then LiF, NaF, Al₂O₃, CaWO₄) | INF-1 |
| DC-69 | P2 | OWED | Event-level charge/exciton kinetics: exciton/EHD rate equations, drift–trap transport with history n_j(t), athermal emission, μ_F-referenced E_trap, E_es; windowed Y_H(t… | Si, Ge | INF-10, INF-11, DC-68, DC-61, DC-81 |
| DC-70 | P3 | OWED | Dense tracks: EMC-MD with P³M Coulomb among carriers (θ_dense, ΔF_NR) and MLIP-MD + two-temperature model for Ge thermal spikes | Si, Ge | INF-7, DC-63, DC-72 |
| DC-71 | P3 | OWED | Track recombination and the plasma phase: drift–diffusion–Poisson with Auger, exciton formation and SRH on the track geometry; f_A(E_R, ℰ_b), plasma time, Ramo delay | Si, Ge | DC-68, DC-72 |
| DC-72 | P3 | OWED | Amorphous-pocket size distribution P(N_a \| E_R, r̂_R) and recrystallisation barrier spectrum from MLIP cascades | Si, Ge | INF-7, DC-61 |
| DC-73 | P3 | OWED | Ionic targets and colour centres: STE and F–H adiabatic surfaces (constrained hybrid DFT), p_FH(T) at mK, p_surv of close F–H pairs, E_d(r̂) of the anion sublattice, F-b… | LiF, NaF, MgO, LiH (NaI shares the method) | INF-7, INF-1 |
| DC-74 | P2 | OWED | Low-energy-excess model inputs: FEM cooldown stress U_el per component with (Γ_min, Γ_max); cured-epoxy and interface MLIP event-energy law; avalanche branching b_br by… | Si/Ge crystals in holders with glue | INF-10, DC-56 |
| DC-75 | P3 | OWED | Mark sufficiency test of (H-E6): ΔP between full and mark-resampled microstates | Si | DC-69 |
| DC-76 | P3 | OWED | Athermal emission Γ^em_j (phonon ionisation of D⁰/A⁰ and H⁻-like D⁻/A⁺, impact ionisation σ_ii(u)) and space-charge nonlinearity ξ_SC(t) over an exposure history | Si, Ge | INF-10 |
| DC-77 | P3 | OWED | Bond breaking in molecular solids: S_int, S_CM, cage-escape p_esc by MLIP MD (10³ trajectories per (E_int, r̂)) | molecular crystals (D5) | INF-7 |

### F. Phonon and charge transport (CMPMC)

| ID | P | status | quantity | materials | needs |
|---|---|---|---|---|---|
| DC-78 | P2 | OWED | Collection kernels 𝒦_1, 𝒦_2(f; r_ev) for a stated geometry, then ζ_O, ζ_gap, σ_pos, r_coll by (CW6-1) | Si 1×1×0.4 cm (2012.12430, two TES arrays); 1-cm CDMS-like… | INF-10; DC-83 |
| DC-79 | P3 | OWED | Gap-energy release site–spectrum: exciton diffusion π_ℓ(z,t) with surface loss S_surf, per-channel spectra s_ℓ(f), then ζ_gap and its timing distribution | Si, Ge | DC-68, DC-78, INF-11 |
| DC-80 | P2 | OWED | Created-phonon spectra (WP5-AUD B-1) propagated to the sensors: ΔO_obs(t) and arrival spectra for ER and NR at E_R ∈ {50, 100, 300, 1000} eV; Δ_soft in (CW6-2) | Si (then Ge) | DC-61, DC-78; INF-10 for the direct check |
| DC-81 | P2 | OWED | Collection efficiencies ϵ_prim^NR, ϵ_prim^ER, ϵ_NTL, ϵ_gap and hence δ_coll (CW6-3), r_coll for the 1803.02903 Si ZIP and the 1805.09942 Ge iZIP | Si, Ge | INF-10; item 3 done in CMPMC-DEV c43569b; DC-78 |
| DC-82 | P3 | OWED | Anisotropic welded AMM t_ν(θ,φ) for Al(111)/Si(001) and W/Si with thin-film interference; τ_l(ω) for d = 40–600 nm (film elastic constants from DFT or [FT]) | Al/Si, W/Si | INF-10 |
| DC-83 | P1 | DONE: validated (R18/DC-83) | Kaplan-buffer recheck of R15-era CMPMC numbers at CMPMC main ≥ 3d43a02 (fix f61d710): CMPMC-AUD T8 η_pb (no loss 4.5Δ, 6Δ, 10–100Δ; 600 nm film 3, 5, 10, 40Δ; surrogate… | Al film on Ge/Si (CMPMC presets) | none |

### G. Coherent fields, fermionic absorption, two insertions

| ID | P | status | quantity | materials | needs |
|---|---|---|---|---|---|
| DC-84 | P3 | OWED | Coherent-field regime inputs: GIPAW shielding/EFG, E*_I; elastic and piezoelectric tensors (DFPT) for BAR modes; dln a/dln α and dln a/dln m_e from scaled-constant DFT;… | NMR (CASPEr) targets, BAR quartz/sapphire, multiferroics | none |
| DC-85 | P3 | OWED | Fermionic absorption χ + target → ν̃ + excitation: all-electron S_nn, S_{J_TJ_T} along ω = m_χ − q for m_χ ∈ [E_g, 1 MeV] (spin-orbital convention fixed in the table hea… | Si, Ge (crystals); atoms by DHF | INF-6 |
| DC-86 | P3 | OWED | Two-insertion processes: pair absorption S_OO(k ≈ 0, 2m_χ) with 𝔇^pair, dark Compton (J^(sh)(p_z), n_r), Barkas term with an HEG R^(2) + LDA map | Si, Ge, electron gas | DC-14 |

### H. Uncertainty, figures of merit, backgrounds

| ID | P | status | quantity | materials | needs |
|---|---|---|---|---|---|
| DC-87 | P3 | OWED | Halo-independent directional bound (G8′): stream matrix 𝔎_i(w_k) on 768 HEALPix × 100 speeds × 24 phases and the LP per m_χ (HiGHS) | Si, Ge (any q̂-resolved library) | DC-1, DC-15 |
| DC-88 | P3 | OWED | Scalar-absorption kinetic row: Im R⁰_𝒯𝒯(0,ω) (direct kinetic route + PAW one-centre correction), then RPA+LFE R̃_𝒯𝒯 | Si (box), 10-atom oxides (fork) | none |
| DC-89 | P2 | OWED | Cosmogenic sea-level production rates per nuclide (ACTIVIA; Geant4 Shielding or TALYS for ³H, ⁷Be) and sub-keV rate density with EC line fractions | 34 survivors without measured rates (all but Si, Ge, NaI, T… | none |
| DC-90 | P3 | OWED | Spin-dependent nucleon FOM class (G-F6): per-isotope ⟨S_p⟩, ⟨S_n⟩ from ≥ 2 shell-model interactions and the incoherent SD one-phonon response from DFPT partial DOS D_κ(ω) | odd-A isotopes of the survivors | DC-91, DC-95 |

### I. Owed material data (WP8-U v4 GAP cells)

| ID | P | status | quantity | materials | needs |
|---|---|---|---|---|---|
| DC-91 | P2 | PART: Γ stage done for C, 3C-SiC, LiF, NaF (unrefereed); GaAs failed control; 4H-SiC, Al₂O₃ not run; 4³ partial, 6³ owed | Small-cell survivor Γ-DFPT batch: relax, ε_∞, ε₀ (dynmat.x), Z*, ω_TO, ω_LO, then ph 4³ → 6³ for slopes, sound speeds, ω_max, phonon DOS | C, 3C-SiC, GaAs, LiF, NaF, 4H-SiC, Al₂O₃ | none |
| DC-92 | P2 | OWED | CaWO₄ and Li₂MoO₄ dielectric and lattice data: ε₀, ε_∞, Z* tensors, ω_TO/ω_LO mode sums (ω_T,min), elastic tensors, sound speeds, θ_D, ω_max, n_e/ω_p | CaWO₄, Li₂MoO₄ | none |
| DC-93 | P2 | DONE from measured C_ij; ranking rerun with them owed | CsI elastic constants C₁₁, C₁₂, C₄₄ (finite strain or DFPT) to replace the [E] B-floor model | CsI | none |
| DC-94 | P3 | OWED | Magnetic survivors' dielectric and lattice data by DFT+U DFPT: ε₀, ε_∞, Z*, ω_TO/ω_LO, elastic tensors (positive-definite), θ_D, ω_max | YIG, NiO, MnO, Cr₂O₃, NiPS₃ | DC-44 |
| DC-95 | P3 | OWED | Remaining survivors' DFPT batch for DFT-fillable GAP cells: Z* tensors, ε₀ (vetted), ω_T/ω_L, phonon DOS, directional sound speeds, ω_max | NaI, NaCl, CsI (dielectric), MgO, MgF₂, CaF₂, ZnO, ZnS, GaN… | none |
| DC-96 | P3 | OWED | Phonon lifetimes (three-phonon linewidths) for the survivors | 35 survivors (GAP:ph_lifetime) | INF-12, DC-91/94/97 |
| DC-97 | P3 | OWED | Per-survivor PAER/ZPL window inputs: E_min(q), band masses m_eff, ω_TA(Q*) and EPW-class g at Q* (GW/HSE where PBE fails) | 36 survivors (GAP:E_min_q, GAP:EPW_g_omegaTA_Qstar, GAP:m_e… | DC-91/94/96/97; DC-2 route for PBE-failing cells |
| DC-98 | P3 | OWED | Integrated thermal contraction ∫Δα_th dT (300 K → mK) by quasi-harmonic DFPT | 38 survivors (GAP:alpha_th_integral) | DC-91/94/96/97 |

Estimated cost of the whole list (DEFERRED-COMPUTE §5): 3×10⁶–6×10⁶ core-hours and 1.6×10⁵–1.4×10⁶ GPU-hours; the P1 items alone 394–707 core-hours and 3–15 GPU-hours, blocked by code (INF-2, INF-3, INF-4), not by compute.

## 3. Infrastructure owed before the calculations can run

None of these is built. Full rows: state/DEFERRED-COMPUTE.md §3.

| ID | Missing | Blocks |
|---|---|---|
| INF-1 | GW and finite-q RPA with local fields; finite-Q BSE (github.com/ytcs/qe-rtsc issue 1). Yambo 5.3 is the choice made for DC-2-gw | DC-1, 9–15, 17, 25–28, 42, 46, 48, 52, 63–65, 68, 73 |
| INF-2 | PAER density vertex in the Wannier gauge (tier-H stage 5) | DC-1, DC-3, DC-8 |
| INF-3 | PAER kernel (tier-H stage 6) | DC-1, DC-3, DC-8, DC-38 |
| INF-4 | Dynamical quadrupoles for the long-range electron–phonon vertex (ABINIT) | DC-1, DC-3, DC-8, DC-63 |
| INF-5 | Frequency-dependent mixed field–displacement DFPT | DC-24, DC-35 |
| INF-6 | All-electron density stack (PAW reconstruction or LAPW; Dirac atoms) | DC-13, 22, 23, 25, 39, 85 |
| INF-7 | Machine-learned interatomic potentials for Si, Ge, the oxides and LiH | DC-29, 30, 37, 56, 57, 61, 70, 72, 73, 77 |
| INF-8 | Real-time TDDFT with Ehrenfest nuclei | DC-60 |
| INF-9 | Small response-library modules (multiphonon, two-phonon coherent sum, vertex module, tls_response, lowd-rpa, frenkel-ff, disorder/isotope) | DC-14, 20, 21, 32, 46, 52, 53, 59 |
| INF-10 | CMPMC modules not yet implemented (η_pb table, anisotropic mismatch with film interference, trap kinetics, and others) | DC-69, 74, 76, 78, 80, 81, 82 |
| INF-11 | Exciton and electron–hole-droplet kinetics; history-dependent drift–trap transport | DC-69, DC-79 |
| INF-12 | phono3py, hiPhive, TDEP installation | DC-31, 34, 37, 96 |
| INF-13 | Glass models and the two-level-system sampler | DC-32, 42, 59 |
| INF-14 | Full-band cascade solver (stage 1 exists as FBC, returns/R19) | DC-63, DC-64 |

## 4. Calculations the book asks for

From state/DEFERRED-COMPUTE.md, "Book-phase additions" and "Unsized leading corrections". The book prints an estimate, a model or the word "unsized" at each of these.

### 4.1 Figures and tables drawn from models

| Item | Owed | Book |
|---|---|---|
| Si loss function and BSE absorption | First-principles RPA, local-field, ALDA loss and BSE absorption in place of the empirical-pseudopotential model | Fig. 4.7, Fig. 4.11 |
| Al α²F | EPW at a converged grid; check λ_ep ≈ 0.44, ω_log ≈ 270 K | Fig. 6.6 |
| Ge DFPT column | LDA at the measured lattice constant (X and L done, Γ owed: §1) | Table 5.1 |
| Ge band structure | First-principles bands that pass the DC-2 controls, in place of the scissored empirical pseudopotential; or the Chelikowsky–Cohen 1976 nonlocal parameters with spin–orbit once the table is in hand | Fig. 3.7a |
| GaAs phonon figure legend | Rerun of fig11_2 (needs Quantum ESPRESSO matdyn.x); layout only | Fig. 11.2 |

### 4.2 Estimates a calculation would replace

| Item | Owed | Book |
|---|---|---|
| Off-diagonal ε⁻¹_GG′ in the crystal Migdal rate, Si then Ge | Full RPA matrix with local fields and a realistic ion vertex, G sum converged; ratio full/diagonal as a function of m_χ and E_R. The empirical-pseudopotential bracket (1.1–1.45) is done; a few hundred core-hours for the full run | Ch. 12, tab:12-nuisances, E.18 |
| DC-book-12: coherent Migdal response, Si, 0.75 keV ≲ q ≲ 2 q_BZ | Full lattice coherence and local fields (LE-188); carries ≥ 99.8 % of the Si Migdal rate at 0.42–1 MeV | Ch. 12, Ch. 17 |
| Crystalline-Si Migdal drag mass δM_κ | From DFT (same quantity as DC-24) | 8.6, 12.5 |
| GaAs dynamical quadrupoles | DFPT quadrupole calculation (INF-4) | 11.2 |
| Plasmon decay into pairs plus phonons, Si | Second-order electron–phonon with RPA; branching ratio | 10.3 |
| Ge 3d core-to-conduction form factor | All-electron or PAW crystal calculation | 10.6 |
| GaAs core-electron kinetic-energy correction to the scalar phonon rate | In place of the parametric estimate (about 20 %) | 11.9, Table 11.1 |
| DC-book-15.4a: Al α²F_tr(Ω) at low frequency | First principles; the free-electron model is off by about 1.25×10⁴ | 15.4 |
| DC-book-17a: GaAs and TeO₂ elastic tensors | DFPT or measured, low temperature; decides two ranking probabilities | 17.6 |
| DC-book-17c: L(p, ω) near the gap at p of several keV for LiF, NaF, Ge; Ge core screening | RPA loss function (with DC-28) | 17.5 |
| DC-book-14.1b: NiO biaxial two-constant anisotropy rate near the one-magnon edge | Optional refinement of the ×29 upper value | 14.1 |
| DC-FBC-2: full-band cascade stage 2 | See §1 | Ch. 18 |
| LE-179: pair-channel ratio at finite q between the solvable limits | Supercell route of App. E.16 | Ch. 13 |
| LE-184: dirty-film conserving response off the kinematic edge | Edge remainder with impurities | Ch. 15 |

### 4.3 Leading corrections printed as "unsized" (App. F)

Size each, then replace `\Fsize{unsized}` in book/tex/appF/F-rows.tex.

| Item | Owed | Book |
|---|---|---|
| Fermionic absorption on electrons | Transverse-current row and Dirac corrections, O((Zα)²): rerun figscripts/ch10/fermi10_9.py with the Tr S_jTjT row; Dirac part from the literature | 10.9, E.26 |
| In-medium decay of an excited state | Local field at the particle; finite-Q ε^T for the non-radiative part | 10.9, E.16 |
| Wannier picture of the boost (lim:12.3d) | Non-rigid vertex: model size from figscripts/ch12/limit12_3d.py; the Si number needs the DFPT deformation potential on Wannier functions (DC-26) | 12.3, E.18 |
| Linear mean yield | Remainder term b_N and the variance law; b_N = 0.35 is known numerically, not derived | 18.2 |
| DC-book-14.3 | Zero-point correction to the AFMR weight, \|S\| = 5/2, MnF₂: larger-cluster ED, DMRG or 1/S series | 14.3 |
| DC-book-14.1 | Two-magnon to one-magnon weight ratio beyond linear spin-wave theory, NiO | 14.1 |
| DC-book-15.4b | Mattis–Bardeen impurity absorption; spin-current pair breaking with strong coupling | 15.4 |
| DC-book-15.4c | Electron–electron umklapp absorption in Al near 1 meV (LE-185); spin-current line shape; strong-coupling gap in scattering | Ch. 15 |
| DC-book-15.2 | Strong-coupling correction to the conserving edge response | 15.2 |
| DC-book-16.3 | Nanotube response beyond the linear-channel model | 16.3 |
| DC-book-16.4 | Molecular crystals: charge-transfer admixture and the gap to a periodic BSE calculation (DC-52) | 16.4 |
| DC-book-16.5 | Local-field ratio of Si:P (inputs in E.21) | 16.5 |
| DC-book-17d | Coherent correction on the Si one-phonon contours below 3.4 MeV | 17.1, Fig. 17.2a |
| DC-book-19.2 | Si nuclear-recoil charge yield below the binary threshold from a non-perturbative close-collision kernel (DC-60, DC-62) | 19.2, E.23 |
| DC-book-19.5 | Gap-energy release law in dense tracks; inputs of the two-bias inversion | 19.5 |
| DC-book-20.1 | Luke emission into transverse phonons | 20.1 |

Closed: DC-book-16.1.

## 5. Data that a measurement or a literature fetch must supply

Not calculations; listed because calculations above wait on them or are validated by them. Full list: state/DEFERRED-COMPUTE.md §7 and LE-187.

- Low-temperature gaps of GaAs, GaSb, Ge; measured gap and pair-creation energy of TeO₂, Li₂MoO₄, γ-LiAlO₂.
- Measured pair-creation energy and Fano factor of Al₂O₃, CaWO₄, LiF, NaF, diamond, GaAs, CdTe (validates DC-64).
- Measured elastic constants of TeO₂ and GaAs at low temperature (DC-book-17a, DC-book-17.6); the full text of Vallin et al. 1964 for CsI; the primary CaWO₄ source; Li₂MoO₄ density; LiF low-temperature ε₀.
- Neutron-scattering phonon data: Nilsson and Nelin, PRB 6, 3777 and PRB 3, 364 (the control of DC-4). Macfarlane Ge indirect edge (control C1 of DC-3). Ge phonon density of states (DC-book-17b).
- Cold Si absorption within about 25 meV of the indirect threshold at mK (LE-180): the two data sets differ by 20 at 1.20 eV.
- Measured Davydov splitting of anthracene (DC-book-16.4b); LiF free-exciton energy; Si:P oscillator strengths.
- Chelikowsky–Cohen 1976 Ge parameters with spin–orbit (Fig. 3.7a).
- Loss tangent per film; ²¹⁰Pb, U, Th activities; ⁷⁶Ge specific activity; PbS and PbSe low-temperature ε₀; Al bulk gap; Jacoboni–Reggiani Z_f.

## 6. Book text waiting on a result

| When this lands | Update |
|---|---|
| DC-2-gw (Ge bands) | E.14, Sect. 10.6, Sect. 22.1: one sentence each; Fig. 3.7a; then DC-3 and the Ge window in Ch. 13 and Ch. 17. Rebuild the release |
| Ge LDA Γ rerun | Table 5.1 Γ entry; LDA ω_TA(Q*) and Ge edges against Ch. 13 and Sect. 22.1 |
| DC-1 (Si tier H) | Ch. 13 rate and reach; DC-6 ratio |
| Off-diagonal Migdal ratio | tab:12-nuisances row; Limit Check 12.3a |
| DC-93 ranking rerun | CsI figure of merit in Ch. 17 |
| DC-67 library fix | Cascade tables may then be cited (App. E) |
| Any §4.3 item | `\Fsize{unsized}` in book/tex/appF/F-rows.tex, and the open-problems field of the section |
| matdyn.x available | Rerun fig11_2 (recipe in book/ledgers/REVIEWS/figures/B.md) |

After any of these: rerun book/figscripts/appB/gen_B1.py and gen_B3.py if symbols changed, and rebuild book/releases/book-full.pdf.
