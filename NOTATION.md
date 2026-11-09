# NOTATION v4 (2026-10-31; NOTATION v4 pass after R6: audit rows A14, A20). Overrides every other file except CONVENTIONS.md.

**v4 changes:** §M (new rows requested by WP1-v2 IF-9, WP2-v2 IF-5/IF-6, WP3-v2 §16, WP4-v2 I6/I7, WP5-v2 §14, WP6-v2 IF6-2/IF6-3);
A14 collisions resolved (𝒜^{2m}_α, 𝒜^{PA}_ν, y_BCS / y_R, 𝒮_F^D, ζ_S^D, 𝓃_D); rows edited in §D (Sommerfeld), §E (experiment index), §H (𝓃_D).
Owed renames inside the R6 v2 returns: state/CORRECTIONS.md §17.

**Rule:** one symbol, one object. v3 starts from WP0 §10 (v2) and extends it with every symbol in D1, D2, REF-A, REF-B, X1, X2, WP0–WP6,
O4, L1 and state/*. One row per symbol per meaning. **⚠** marks a letter that carried two or more meanings in the returns; each
meaning now has a distinct name (a decorator, subscript, superscript or alphabet is part of the name and may not be dropped).
"Returns" lists where the object appears and its local name there (= means the v3 name was used). Conventions (signs, normalisations,
units) are in CONVENTIONS.md; owed renames inside returns are indexed in state/CORRECTIONS.md (returns are not edited).
Abbreviations: RA/RB = referees R2/REF-A, REF-B; W0…W6 = WP0…WP6; all = every return from R1 on.

## A. Units, global constants, kinematics, DM side
| Symbol | Meaning | Returns (local name) |
|---|---|---|
| ħ = c = k_B = 1; e² = 4πα; e_G² = α | natural HL units; Gaussian source charge | all; D1 N6, D2 C1, W3 (e_G) |
| ε₀^SI | vacuum permittivity, SI sources only | W3 (EPW "ε₀") |
| α | fine-structure constant (bare α only) | all |
| v_C(k) ⚠ | Coulomb kernel e²/k² (matrix v_C) | W0, W4 "v_k, v_q", W5 "v_p", X2 "v(P)", D2 "v_q" |
| Ω, N, V = NΩ | cell volume, number of cells, crystal volume | all (sources: V_cell) |
| ρ_T | target mass density | all |
| χ ⚠ | the DM particle only | all (D1 N6, D2, X2 "χ" = response → R; W3 "χ_f" = vibrational state → Ψ^vib_f) |
| m_χ, μ_χe, μ_N, μ_p | DM mass; DM–electron, DM–nucleus, DM–proton reduced masses | all; W2, W6 |
| v ⚠ | DM lab-frame velocity (bare v only) | all |
| v_χ = v − q/2m_χ | DM-side Galilean velocity (WP0 (2.1)) | W0, W1, W6 |
| v^⊥ | Fitzpatrick relative velocity v_χ − v_s (target-side operator) | W0, W1 "v^⊥" |
| v_T ⚠ | halo velocity transverse to q̂ | W6 "v_⊥", W1 (2510.25835 "v_⊥") |
| v_∥ = (ω+Δ_χ)/q | on-shell longitudinal DM velocity | W6 "u_∥" |
| q | momentum DM → target, unreduced | all |
| q_r, G_q | 1BZ part and reciprocal vector of q | W1 |
| q₀ = αm_e | σ̄_e reference momentum | all |
| ω | energy given to the target | all |
| ω_q = q·v − q²/2m_χ − Δ_χ | kinematic energy transfer | all (D1/D2 without Δ_χ) |
| Δ_χ ⚠ | DM mass splitting (exothermic < 0) | W0, W4, W6 (D1/D2 "Δ" denominators → d) |
| v_min, v_* , q_* | minimum speed; kinematic minimum √(2ω/m_χ) and its q | all; W6 |
| v_max = v_esc + v_E^ref | reference speed cutoff (794.5 km/s, quoted 794) | W1, W6, L1 |
| δ_v, δ_v,0 ⚠ | v_max − v_min; v_max − √(2E_th/m_χ) | W6 "δ", "Δ₀" |
| m_min = 2E_th/v_max² | edge mass | W6, L1 "m_χ^min" |
| j_χ, 𝐒_χ | DM spin quantum number, DM spin operator (bold) | W0, W4 |
| 𝒪_i ⚠ | Fitzpatrick NR-EFT operators, i = 1…15 | W0, W1, W4 "O_i, O₁…O₁₅" |
| c_i^{(s)} | NR-EFT coefficients of 𝒪_i for species s | W0 "c_i^{(ψ)}", W4 "c₅, c₈" |
| 𝒱_a^{s′s}(q,v_χ) | DM vertex for target operator O_a | W0, W4, W6 |
| 𝔇_ab; 𝔇^{(n)} | DM tensor (Hermitian PSD); its velocity-polynomial coefficients | W0–W6 "𝔇, 𝔇⁽ⁿ⁾" |
| 𝔇^S, 𝔇^A | symmetric and antisymmetric parts of 𝔇 | W4 |
| Ṽ(q) | Fourier potential, |Ṽ|² = πσ̄_eF_DM²/μ_χe² | D1, D2, W0 (= |𝒱_{n_e}|²), W4 |
| σ̄_e | reference DM–electron cross-section at q₀ | all |
| σ_N, σ_p | DM–nucleus, DM–proton cross-sections | W2, W3 |
| F_DM(q); F_DM,i(q) | DM form factor; per-operator mediator factor | all; W0 "F_i(q)" |
| m_V | mediator mass | L1 (KKL), W1 |
| y_χ, y_e, y_N | mediator couplings (sources' g_χ, g_e, g_N) ⚠ | L1 "g_χ g_e", W3 "g_χ g_N", W4 "g_D" |
| e_χ | DM charge in light-mediator models | W1 "e_χ", W2 "Q_χ" ⚠ |
| κ_mix ⚠ | dark-photon kinetic mixing | W0 "κ", W3 (1608.01994 "κ", "κ_eff") |
| g_aee, g_aγγ, B₀ | ALP couplings; static magnetic field | W0, W3 |
| φ ⚠ | absorbed bosonic DM field (mode operator a^φ_k, momentum k_φ) | W0 (3.3) "φ, a_k, k", W3 |
| Γ_χ(v) ⚠ | rate per DM particle | W0 "Γ(v)", D1, D2, W4 |
| Γ_abs, Γ_emit, Γ_net | absorption rates (WP0 (3.5)) | W0, W3 |
| dℛ/dω, ℛ ⚠ | event rate per unit target mass (sources: dR/dω, R) | all "dR/dω, R" |

## B. Electrons, bands, vertices
| Symbol | Meaning | Returns (local name) |
|---|---|---|
| k, k′ | electron crystal momenta (1BZ) | all (W2 "k_i" = phonon → Q_i; W3 (W.5) "k" loop → p) |
| n, m, v, c (subscripts only) ⚠ | band labels: generic, intermediate, occupied, empty | all (O4 "m" = X0 pair → Λ₀) |
| ε_{nk} ⚠ | band energy (always two band/k subscripts) | all |
| ε̃_{nk}, ε^{ren}_{nk} | AHC/ZPR-renormalised band energy | D2, W3, O4 "Ẽ_m" |
| ψ_{nk}, u_{nk} ⚠ | Bloch state over V, periodic part over Ω | all |
| E_g, E_dir, k_c | indirect gap, minimum direct gap, CBM crystal momentum | all |
| E_cv(k,q) ⚠ | ε_{c,k+q} − ε_{vk} | X1 "Δ_cv(k,q)" |
| E_min(q), E_min^{ren}(q,T) | min pair energy at fixed q; renormalised | D1, RA, RB, X1, W1, W3 |
| E_th | detection or kinematic threshold energy | W6, W5 |
| ρ_{mn}(k,q) ⚠ | density vertex (O(1)) | all; X2 "ρ_f(P+G)", W1 |
| ρ_{cv}(k,q;λ_fd) | frozen-phonon transition density at displacement λ_fd | D1 §4 "D(λ)" ⚠ |
| ρ̃_{mn}(k,q) ⚠ | externally screened vertex Σ_G(ε̃^{-1})_{G0}ρ(k,q+G) | X2, W3, W0 (7.2) |
| ρ^{ren}_{cv} ⚠ | renormalised zero-phonon vertex (Fan Z, mixing, virtual phonon) | D2 §2c "ρ̃", O4 "ρ̃_m" |
| M^{(1)}_{cv} = ρ_{cv} | zero-phonon amplitude | NOTATION v2, X1 |
| M^{(2)}_{cvν,±}(k,q,Q) | one-phonon amplitude, D1 eq. (1) normalisation | D1 "M^{(2)}", D2 "M^{(2),±}" (= M/√N), X1, X2, W3 |
| M_v | velocity-form amplitude (optical limit) | D2 C1 |
| A₁, A₂ | the two time-ordering families of M^{(2)} | D2, O4 |
| A₁^v, A₂^v | velocity-form families (sources' S1, S2) | D1 §6.1 "S₁, S₂", W3 "S1, S2", L1 |
| M̃_± | fully screened PAER amplitude (X2 (2.2)) | X2, W3, W0 (5.7) truncated |
| M_{f}^{X+} | Feshbach X+ amplitude | O4 "A_f" ⚠ |
| a^{off}_f, Υ_Λ₀ | off-shell path amplitude per g; its Σ-weighted sum | O4 "λ_f", "Υ_m" ⚠ |
| d_{A,m}, d_{B,m} ⚠ | energy denominators of the A/B families | D1 "Δ_{A,m}", D2 |
| δ, δ₀ | off-shell distance; window margin | D1, X1, O4, W0 |
| p, p_{mn}, p_{nn} ⚠ | momentum operator; its matrix elements; diagonal band momentum | all; X1 "P_n", RB |
| v^g_n(k) ⚠ | band group velocity ∇_kε_{nk} | X1 "v_n, v_c, v_v", D2 "v_nk", RA, RB |
| r_{mn}, v_{mn} | position, velocity matrix elements | D1, D2 |
| j_e^α(q), j_L, j_T | paramagnetic current (Cartesian α); longitudinal/transverse parts | W0 "j_e^a", W1, D2 "j_q" |
| s_i, 𝐬 | electron spin s_i = σ_i/2 | W0 |
| s_e^α(q), J_e^{αβ}(q), J_T | spin density, spin-current, transverse spin current | W0 "s_e^b, J^{ab}", W1 |
| 𝒯_e(q) ⚠ | kinetic-energy density operator | W0, W3 "τ_e" |
| O_a(q), a = (s,Γ) | target operator basis (16 per species) | W0 "a = (ψ,Γ)", all |
| Γ | operator-structure label (NR rows {0,b,a,ab}; Dirac bilinears) | W0, W1 "O_Γ" |
| T_e, ⟨T⟩ | electron kinetic-energy operator; mean KE per electron | W0, W1 |
| H, H_C, H_rel, H_hf, H_ext, H_ep, H_AH ⚠ | Hamiltonian and parts | all; D2 "H_DW" → H_AH |
| f_{nk} | occupation | all |
| E_i, E_f, p_i, 𝒵 | many-body energies, Gibbs weights, partition function ⚠ | all ("Z" → 𝒵) |
| T_fi | T-matrix element | D1 |

## C. Phonons, lattice, nuclei
| Symbol | Meaning | Returns (local name) |
|---|---|---|
| Q ⚠ | phonon wavevector (1BZ) | all; W2 "k_i" → Q_i |
| ν | phonon branch | all (W2 "λ" NA modes → ν) |
| ω_{Qν}, e_{κν}(Q) | phonon frequency, polarisation | all |
| b_{Qν}, B_{Qν} = b_{Qν} + b†_{−Qν} | phonon operators; displacement field | D1/W2 "a", D2 "b, A_Qν" ⚠ |
| n_{Qν}, n_B(x) | Bose occupation, Bose function | all; W3 "n(ω)" for refractive index → n_r |
| g_{mnν}(k,Q) ⚠ | EPW e–ph matrix element | all |
| g^S, g^L, g^{AH}, g^{ac} | short-/long-range, Allen–Heine, acoustic parts | W5, D2 "g^{DW}" → g^{AH}, D1 |
| g^x_{λλ′ν} ⚠ | exciton–phonon vertex | W3 "𝒢_{SS′ν}" |
| ℓ_Q ⚠ | zero-point length (2M_cellω_{Qν})^{-1/2}, N outside | D1, X1, W3; W0 (4.9) N inside; D2 "u^{zp}" = ℓ_Qê/√N |
| ê, Q̂ | acoustic polarisation, direction of Q | D1 "û", X1, RA, RB |
| κ ⚠ | nuclear species index (only) | all |
| κ_BO | (m_e/M)^{1/4} | W0, W2 |
| M_κ, M_cell, A_κ, Z_κ | nuclear mass, cell mass, mass number, charge | all |
| I | nucleus label; R_I, P_I positions and momenta | W0, W3 |
| 𝐈_I, 𝒥_κ ⚠ | nuclear spin operator; nuclear spin quantum number | W0; W2 "J_κ" |
| R ⚠ | lattice translation (Wannier and lattice sums) | D1 "R", D2 "R_p", W2 "ℓ" |
| ΔR | lattice separation R − R′ | W2 "L" ⚠ |
| r_κ, x⁰_{Rκ}, u_{Rκ}, u_I | basis position, equilibrium site, displacement | W2, D2 "τ_κ", X2 "τ_κ" ⚠ |
| s ∈ {e, κ} ⚠ | species label | W0 "s" and "ψ" |
| z_s, n_s(q), N_s, 𝓃_s | charge number, density operator, number, number density N_s/V | W0 "n_s" (both) ⚠ |
| 𝓃_e | electron number density | W0, W3 "n_e" ⚠ |
| n_κ^F, F^M_κ, F^Σ_κ | nuclear density with form factor; nuclear form factors | W0, W2 |
| I_κ^α(q), j_κ^α(q), J_κ^{αβ}(q) | nuclear-spin density, nuclear CM current, nuclear spin-current | W0 "I_κ^b, j_κ^a, J_κ^{ab}", W2 |
| PAER, ZPL, ZG, ZPR, AHC, HBB | process and method names (CONVENTIONS §10) | all |
| ρ_c(q), ρ_M(q), 𝐠(q) | charge density; mass density; momentum density | W0 "ρ_c, ρ_m, g(q)" ⚠ |
| c_s ⚠ | species coupling vector (W2 f_κ, c_e) | W0 (5.3), W2 "f_κ(q), c_e" |
| c_ν ⚠ | sound speed of branch ν | W0 "c_s", X1 "c, c_ν", RA "c_s, c_ν", RB |
| D^n, Ξ^n = D^n + v^g_n⊗p_{nn} | comoving and lab deformation tensors | X1, W3, W0 "Ξ_n" |
| d^n | optical deformation potential | X1 |
| C_F, C_pz | Fröhlich, piezo couplings | X1 |
| Z*_κ, Z*_κ(ω), C_κ | Born charge; dynamical Born charge; its ω² coefficient | W2, W3 |
| 𝒬_κ ⚠ | dynamical quadrupole | W2 "Q_κ" |
| δρ_κ(q), 𝒵_κ(q) ⚠ | electronic charge-response vector (core + valence); δρ^val_κ = δρ_κ − q f^core_κ (WP2-v3 IF-11); total charge vertex | W2 "Δ_κ(q)", "𝒵_κ" |
| ρ̄_e(q;R), 𝓕_κ(q) | adiabatic electron density; adiabatic electron form factor | W2; W3 (J7 "F(q)") |
| f^at_κ(q) | atomic form factor | W2 |
| ε_∞, ε₀ ⚠ | high-frequency, static dielectric constants | W2, W4, D2 |
| ω_L, ω_T | LO, TO frequencies | W2 |
| ω_Lar ⚠ | Larmor frequency | W2 "ω_L" |
| D^dyn_A, D^dyn_NA ⚠ | analytic, non-analytic dynamical matrices | W2 "D_A, D_NA" |
| p(q̂)_{κα} | mode-charge vector | W2 |
| B_κ | displacement tensor ⟨u_κu_κ⟩ | W2 |
| W, 2W_κ(q) ⚠ | Debye–Waller (Franck–Condon) exponent only | W0, W2, W3 |
| S_HR, S_HR,k ⚠ | Huang–Rhys factor; per mode | W0, W2, W4 "S_k" |
| D_κ(ω), D_κ^{q̂}(ω), D_κ^{αβ}(ω) ⚠ | partial, projected, tensor phonon DOS | W2; W5 (W9) "g_κ(ω′)" |
| w_κ(q;ω′) ⚠ | one-phonon measure | W2 "μ_κ(q;ω′)" |
| ρ^ph_κ(ω′|q,ω) ⚠ | final-state phonon spectrum | W2 "ρ_κ(ω′|q,ω)" |
| Φ_{κκ′}(ΔR,t), Φ^{(n)} ⚠ | displacement correlator; force constants (superscript mandatory) | W2 |
| c̄_ΔR, z_ΔR, j_BZ(r) | shell correlation, coordination, BZ form factor | W2 "c̄_L, z_L" |
| S^{(n_ph)}, n_ph | n-phonon term, phonon order | W2 "S^{(n)}, n" ⚠ |
| s^ph_i = ±1 ⚠ | emission (+) / absorption (−) label | W2 "s_i" |
| 𝔨_m, 𝔨₃^{GS}, 𝔨₃^X ⚠ | ω-cumulants of S_self; GS/X split | W2 "κ₁…κ₄, κ₃^G, κ₃^X" |
| 𝒞_m ⚠ | displacement cumulants (beyond Gaussian) | W2 "K₃, K₄" |
| 𝔫_κ(p), E^kin_q̂ ⚠ | nuclear momentum distribution; kinetic energy per direction | W2 "n_κ(p), K_q̂", W5 (W9) |
| x_R, x_coh | recoil parameter; (retired) coherence parameter | W0, W2 |
| λ^anh_3, λ^anh_4, η_anh | anharmonic couplings; small parameter | W2 "λ₃, λ₄" ⚠ |
| A^ph_ν(k,ω), Π^ph_ν ⚠ | phonon spectral function, phonon self-energy | W2 "A_ν, Σ_ν" |
| ω₀, ω̄, ⟨ω^{-1}⟩ | Einstein/toy frequency, DOS moments | W2, W5 |
| x_κ, P_κ, h^I_κ, o_{Rκ} ⚠ | isotope abundance, polarisation, spin coupling, occupancy | W2 "c_κ, P_κ, g_κ, σ_ℓκ" |
| Ω_{p,ion}, ω_{p,c} | ionic and total-charge plasma frequencies | D1, W0 |
| v_N = q/M_κ | nuclear recoil velocity | W3 |

## D. Response, screening, dielectric
| Symbol | Meaning | Returns (local name) |
|---|---|---|
| S ⚠ | dynamic structure factor S_ee (bare S only for this) | all |
| S_ab(q,ω) | response matrix (WP0 (3.1)) | W0–W6, O4 |
| S^{prop}, S^{(1)}, S^{PA}, S_inc, S_coh, S_self, S_IA, S^FR | proper; zero-phonon; PA; incoherent; coherent; self; impulse; free recoil | D1, D2, W2 |
| S̄ | angle average | all |
| S_ℓm(q,ω) ⚠ | harmonic coefficients of S | W2 "S_ℓm", W1 "T_ℓm" |
| S(q,ω;Λ) | final-state-resolved response | W0, W5, W6 |
| S_ab(q;ω_ph,ω_e) | joint response | W3 |
| R_ab, R̃_ab, R⁰ ⚠ | retarded, Coulomb-proper, KS-bubble responses | W0–W6; D1 "χ, χ⁰, χ_ee", D2 "χ, Π", X2 "χ_KS, χ" |
| Π^γ_T, Π^γ_L ⚠ | photon self-energy (e²-normalised) | W1 "Π_T", W3/W0 "Π" (1608.01994, 2106.12586) |
| Π^N_{ij} | Nambu bubbles | W4 "Π_ij" |
| R̃^{GRPA} | conserving BCS density response | W4 |
| ε(q,ω), ε_{GG′}, ε₁, ε₂ ⚠ | total longitudinal dielectric function/matrix | all |
| ε̃ | test-electron dielectric matrix 1 − f_Hxc R⁰ | X2 |
| ε_e, ε_c ≡ ε ⚠ | electron-channel, total-charge dielectric | W0 (L17), D1 "ε_e" |
| ε_mac ⚠ | macroscopic 1/(ε^{-1})_{00} | W1 "ε_M" |
| ε_Mer, ε_Lin ⚠ | Mermin, Lindhard dielectric functions | W4 "ε_M, ε_L", W1 |
| ε_L, ε_T ⚠ | longitudinal, transverse dielectric functions | W0 (3.6), W1, L1 (KKL "ε_L") |
| ε_bg, ε_r = ε/ε_bg ⚠ | remote-band background dielectric; relative permittivity | W4 "κ, κ_ij, ε_r" |
| ε₂^{PA} | phonon-assisted ε₂ | D1, D2, W3 |
| L ⚠ | loss function Im[−(ε^{-1})_{00}] | all; W4/2101.08263 "W" |
| L_c, L_e; K_n^{(ch)} | channel loss functions; their moments | W0 "L_X, K_n^X" |
| L^{PA} | PA loss function | D2, X2, W3 |
| 𝓜¹_ab, 𝓜³_ab, 𝓜₁^{SB} ⚠ | moment matrices; sideband first moment | W0 "M¹, M³", D2 "M₁^{SB}", W3 "M¹" |
| ω_p, ω_{p,e} | all-electron plasma frequency | all |
| f_xc, f_xc^T, f_Hxc = v_C + f_xc ⚠ | xc kernel, triplet kernel, Hxc kernel | W1, X2 "K" |
| G_LF(q) ⚠ | HEG local-field factor | W1 "G(q)" |
| W^{scr}_{GG′}(P,ω_f) ⚠ | screened interaction ε̃^{-1}f_Hxc (pair channel, GW) | X2 "W", W5 "W" |
| P = q+Q ⚠ | pair momentum (bare P only for this) | X2, W3, W0 |
| ω_f = ω ∓ ω_Q | pair energy | X2, W0 "ω_e" (5.5) |
| 𝔗_G(P) ⚠ | second-order KS density (triangle) | X2 "T_G" |
| r^{pair}_f ⚠ | pair-channel relative correction | X2 "Λ_f" |
| c_coh ⚠ | heuristic coherence factor | X2 "η" |
| δ_ω, δ_LF, δ_pair, δ_ion | screening error pieces | X2 |
| δM^{intra}_f ⚠ | intraband (non-convective) amplitude part | X2 "D_f" |
| A^λ_{cvk}, E_λ, H^{exc}, λ ⚠ | BSE envelope, exciton energy, pair Hamiltonian, exciton label | W1; W3 "A^S, Ω_S, S" |
| E_x, E_x^b, a_x, μ_x, Q_x ⚠ | exciton energy, binding, radius, reduced mass, momentum | W1 "E_b", W3 "E_x^b" |
| 𝒮_F, ζ_S ⚠ | Sommerfeld factor 2πζ_S/(1 − e^{−2πζ_S}) and parameter (3D Coulomb: excitons, donor final states) | W1 "S_F, κ", W4 [6.2] "S_C, ζ" |
| 𝒮_F^D, ζ_S^D ⚠ | Dirac (2D-type) Sommerfeld factor πζ_S^D/(1 − e^{−πζ_S^D}), ζ_S^D = α/(ε_bg v_F b_D) | W4 §5.4 "η"; W4-v2 §5.4 "𝒮_F, ζ_S" |
| L^{BSE}, Ξ^{BSE} ⚠ | two-particle correlation function, BSE kernel (source) | W1 "L, Ξ" |
| ω_pl(q), w_pl(q), q_c | plasmon dispersion, f-sum share, Landau onset | W1 "F(q)" ⚠ |
| j₀, Y_ℓm, P_ℓ, K^cub_ℓ ⚠ | Bessel; harmonics; Legendre; cubic harmonics | W1 "K_ℓ", W2, W6 |
| ℓ | multipole order (bare ℓ only) | W1, W2, W6 |

## E. Sectors, expansion hierarchy, uncertainty
| Symbol | Meaning | Returns (local name) |
|---|---|---|
| GS, X0, X+, X = X0∪X+ ⚠ | Theorem D sectors | W0 "G, X0, X+", W2, W3 "S^G" |
| 𝒫₀, 𝒫_⊥, U_n, U_ep | adiabatic projectors; decoupling unitaries | W0, W3 |
| P₀, P₊, H₀, V_ep | O4 sector projectors; split H = H₀ + V_ep | O4 "V" |
| Λ, P_Λ ⚠ | prompt final-state class, projector | W0, W5, O4 |
| Λ₀, Λ₊ ⚠ | an X0 pair label; an X+ final state | O4 "m", "f" |
| Ẽ_Λ₀, Z_Λ₀, Γ_Λ₀ | renormalised pair energy, residue, width | O4 "Ẽ_m, Z_m, Γ_m" |
| Σ^{FM}, Σ^{AH}, Σ (Feshbach), Γ̂ ⚠ | Fan–Migdal, Allen–Heine, Feshbach self-energies; width operator | D2 "Σ^{DW}" → Σ^{AH}, O4 |
| Γ^{ph}, Γ^x, Γ^{tot}, Γ^{(f)} | phonon, non-phonon, total, per-final-state widths | O4 |
| δω_Λ₀ = ω − Ẽ_Λ₀ ⚠ | detuning | O4 "Δ" |
| fp, PV | Hadamard finite part; principal value | D1, RA, RB, O4 "P" |
| DC ⚠ | Dyson resonant-part convention | O4 "C1" |
| 𝒞_adm(ℓ_win), ℓ_win, w₀, b_λ ⚠ | admissible class, window half-width, X0 weight, constant | O4 "𝒜(ℓ), ℓ" |
| 𝔉_{Λ₀,b}, c_b^F (b ∈ {ν, x}) | R16 (CW3-errata §2.2 item 4): 𝔉_b = Γ^{(b)}(c̄^F − c_b^F) (rate units; O4 (O4.7) is the spectral-weight form 2π\|ρ\|²𝔉_b/Γ^{tot}); c_b^F = Γ^{tot}_Λ₀ Im(ρ*a^{off}_b)/\|ρ_Λ₀\|², dimensionless; b includes non-phonon branches; vanishes for PT-symmetric targets with N_e even and a scalar O(g²) level-shift matrix on D(Λ₀) (CW3 §2.2 (P1)–(P5)); without (P5) only Σ_b𝔉_b = 0 (was c_ν^F = Γ_Λ₀ Im(Σ_Kramers ρ*a^{off}_ν)/\|ρ_Λ₀\|², WP5 (W17)) | O4 "𝔉_{m,ν}, c_ν" ⚠; CW3 (CW3.1) |
| 𝒦_{Λ₀→Λ₊} ⚠ | cascade first-step kernel | O4 "K_{m→f}" |
| w_test ⚠ | smooth test function | O4 "φ" |
| ϵ_reg, σ | fp regulator; δ smearing | O4 "ϵ_r" |
| τ = (n_B, n_g, n_A, 𝒳, n_T, K, 𝔐, n_D) ⚠ | truncation multi-index (CONVENTIONS §11) | W0, W1, W3 "τ_J", W6 |
| 𝒳 ⚠ | kernel-ladder rung | W0/W1 "X" |
| K | kinematic regime label inside τ (only) | W0 |
| η_ep, η_xc | e–ph and xc small parameters | W0 |
| t_ph = T/ω_ph, t_g = T/E_g ⚠ | thermal small parameters | W0 "τ_ph, τ_g" |
| σ_c, ξ_D | suddenness; multipole parameter | W0 |
| θ_k, Δ^τ_k ⚠ | nuisance parameter; truncation increment S^{τ+e_k} − S^τ | W0 "Δ_k", W1 "Δ_X", W2 "Δ_anh", W6 |
| r^M_k | ratio Δ^τ_k/S^τ (M-type nuisance) | W6 "r_k" |
| θ^det_ex ⚠ | detector nuisances of experiment ex | W6 "ν_e" |
| σ_E, σ_T, r_mat | energy-shift width, sensor width, cross-material correlation | W6 "σ_E, σ_T, ρ_mat" ⚠ |
| 𝔈_i, P_det, N_i^up, s_{ex,i}, b_{ex,i}, N^obs_{ex,i} ⚠ | exposure × efficiency, detector matrix, per-bin limit, signal per unit σ̄_e, background, observed counts; index ex = experiment (never e) | W6 "s_ei, b_ei", W6-v2, W0-v2 (8.3) |
| 𝒜_ij, A^{(0)}, A^{(2)} ⚠ | halo-independent response matrix (bare 𝒜 with bin/step indices only); its O₁-type and v_T² contractions | W6 "𝒜_ij, A₀, A₂" |
| p_on ⚠ | response onset exponent | W6 "p" |

## F. Halo
| Symbol | Meaning | Returns (local name) |
|---|---|---|
| ρ_χ, f_χ(v) | local DM density (0.3 GeV/cm³), lab-frame distribution | all; 1509.01598 "g_χ" ⚠ |
| v₀, v_esc, v_⊙, v_⊕(t), v_E(t), v_E^ref | 2105.00599 parameters (CONVENTIONS §8) | W1, W6, L1 |
| N_esc ⚠ | SHM normalisation | W6/1509.01598 "K" |
| η(v_min), ξ(v_min), η̃ ⚠ | halo integrals; scaled η | all; W6 |
| 𝒢(q,ω) ⚠ | velocity kernel ∫d³v f_χδ(ω−ω_q) = f̂^{(0)}/q | D1 "𝒢", W2 "g(q,ω;x)" |
| f̂^{(n)}(q̂,u) | Radon transform and its transverse moments | W6 |
| x = q̂·v̂_E | Radon kernel variable | W2 |
| k_tail | halo-tail index | W6 "k" ⚠ |

## G. Energy partition and measured quanta (WP5, WP4 §4.6)
| Symbol | Meaning | Returns (local name) |
|---|---|---|
| N_eh ⚠ | ionization yield (number of e–h pairs) | W0; L21 sources "Q", SOTA/O4 "P(Q|…)" |
| N_eh^{step} | step model 1 + ⌊(ω − E_g)/ε_eh⌋ | W5, W6, L1 "Q, n_e" |
| P_casc(𝐍|Λ), P(N_eh|q,ω), P_n | cascade distribution; quanta distribution; P(N_eh = n) | W0, W5 "p_n", W6 |
| 𝐍 = (N_e^f, N_h^f, N_e^{tr}, N_h^{tr}, E_trap^{pr}, ℋ, E_st, N_FP, E_esc, N_X, E_X); marks 𝔪 (class, geometry) | deposited observables, additive (R16: replaces the stale (N_eh, ℋ, E_st, N_FP, E_esc, …)); N_eh is a derived function of 𝐍 and P_casc(N_eh\|Λ) its marginal | W5 "𝐍 = (N_eh, ℋ, E_st, N_FP, E_esc, …)"; WP5-v4 A-2 (IF-R13-1) |
| ℋ ⚠ | heat deposit | W5 "H" |
| E_st, E_esc, E_d, N_FP, N_trap | stored defect energy, escaped energy, displacement threshold, Frenkel pairs; N_trap ≡ N_e^{tr} + N_h^{tr} **before t_pr only** (after t_pr: trap occupations n^{e,h}_j, rows WP7-E) (R16: IF-R13-1, WP5-v4 A-15) | W5 |
| 𝔊_x(ϑ), ϑ ⚠ | branching generating functional; generating variable | W5 "G_x(s), s" |
| 𝒦_c ⚠ | cascade kernel of channel c | W5 "K_c" |
| Γ^{ph}_{nk→…}, Γ_ii, Γ_E, Γ_k | e–ph, impact-ionization, energy-loss, momentum-randomization rates | W5 |
| dE/dt|_ph ⚠ | phonon energy-loss rate | W5 "P(E)" |
| p_no-ii | survival probability against ii | W5 |
| ε_eh, ε_eh^γ ⚠ | mean energy per pair; photon asymptote | W5 "ε, ε_γ", W6 "ε", L1 |
| F_eh, F_NR, F_qp, F_meas ⚠ | Fano factors | W5 "F", W4, W6 |
| 𝔡_H ⚠ | heat dispersion index Var(ℋ)/(E_g⟨ℋ⟩) | W5 "D" |
| ϵ_det ⚠ | detection efficiency (thinning) | W5 "η" |
| b_N ⚠ | asymptotic yield offset | W5 "b" |
| E_el ⚠ | mean energy into electronic excitation (Lindhard) | W5 "η̄" |
| 𝓔_red, k_L, ν̄_L ⚠ | Lindhard reduced energy, constant, nuclear energy fraction (source) | W5 "ε, k, ν̄" |
| σ²_strag ⚠ | electronic straggling (2209.04503) | W5 "W(ε)" |
| U_bind | binding term U(E) (2209.04503) | W5 "U" |
| Y_H(t_win) ⚠ | NR/ER heat-signal ratio at equal ω (multiplicative collection): Y_H = (1 − δ_coll)(ω − D′_NR)/(ω − D′_ER) (exact; CW5-errata OC-1); R16: replaces the stale "heat quenching ⟨ℋ_meas⟩/E_R" | W5 "Q_h"; WP5-v4 A-4 (IF-R13-1) |
| Y_tot, Y_casc | ionization yields with/without Migdal | W3 |
| E_R, E_R,th | nuclear recoil energy; binary e–h threshold | W5, W2 |
| σ_ω ⚠ | impulse Doppler width | W5 "σ_ω", W2 "Δ" |
| ξ_Mas ⚠ | Massey parameter | W5 "ξ" |
| B_h ⚠ | hole bandwidth | W5 "W ≈ 12 eV" |
| E_bar, 𝒩_b(E_bar), Γ_ij, T_× ⚠ | barrier energy, barrier density, hop rates, tunnelling crossover | W5 "E_b, g(E_b), k_ij, T_c" |
| N_i(t), 𝔰_i(t) ⚠ | defect populations; their source | W5 "n_i, S_i" |
| 𝒮_inst ⚠ | instanton action | W5 "S_inst" |
| S^{stop}_e ⚠ | electronic stopping power | W5 "S_e" |
| 𝔅₀, 𝒰_t, P_FP | perfect-crystal basin, dissipative flow, displacement probability | W5 "Φ_t" ⚠ |
| N_qp, η_pb, t_esc ⚠ | quasiparticle number, pair-breaking efficiency, phonon transmission | W4 "η_pb, η_esc", W5 "η" |
| E_sub, E_excess | sub-gap phonon and excess energies | W5 |
| n_gen ⚠ | cascade generation index | W5 "g" |

## H. Spin, superconducting, Dirac and defect targets (WP4)
| Symbol | Meaning | Returns (local name) |
|---|---|---|
| Δ_BCS ⚠ | superconducting gap | W4 "Δ", W5 |
| Δ_D ⚠ | Dirac half-gap | W4 "Δ" |
| Δ_scis ⚠ | scissor shift | W1 "Δ_sc" |
| Δ_Mott, Δ_SO, Δ_ad | charge (Mott) gap; spin–orbit splitting; adiabatic gap | W4 "Δ_c"; W1; W0 |
| E_k, ξ^{BCS}_k, u^B_k, v^B_k ⚠ | Bogoliubov energy, normal energy, coherence factors | W4 "E_k, ξ_k, u_k, v_k" |
| U^B, V^B, X^{m,p}_h ⚠ | Colpa blocks; hybrid-mode content (mode index h) | W4 "U, V, X_λ" |
| 𝔤_I(x), 𝔤_II(x) ⚠ | case-I, case-II pair-breaking functions | W4 "g_I, g_II" |
| ℰ^α_ν(q), ℰ_ν, ℱ_ν | one-magnon, collective-mode, one-phonon amplitudes | W4 "E^b_ν" ⚠ |
| 𝐒_j, λ_{S,j}, λ_{L,j}, R_j, r_j | ionic spin (bold), weights, local frame (2009.13534) | W4 |
| F^{mag}_j(q) ⚠ | magnetic form factor | W4 "F_j" |
| J^{ex}_{ij}, g_mp | exchange, magnon–phonon coupling | W4 "J_ij" ⚠ |
| a_{kν}, n_ν | magnon operators, magnon/hybrid Bose occupation | W4 |
| v_F, k_F, k_TF, E_F, N(0) | metal parameters | W1, W4 "λ_TF" |
| γ_rel, ℓ_mfp, D_diff ⚠ | relaxation rate, mean free path, diffusion constant | W4 "γ, ℓ, D", "τ" |
| Λ_D ⚠ | Dirac momentum cutoff | W4 "Λ" |
| g_deg ⚠ | spin × cone degeneracy | W4 "g, g_s, g_C" |
| α̃, 𝓈 = ω² − v_F²q² ⚠ | Dirac effective coupling; invariant | W4 "α̃, s" |
| 𝐛_NR(ω), γ_OA(ω) ⚠ | nonreciprocal vector, optical activity | W4 "𝐠(ω), γ(ω)" |
| q_ν*, v* | exothermic shell momentum and velocity | W4 |
| 𝓃_D ⚠, a*, E_b^D, E_ZPL | defect number density (n_D is τ's multipole slot), effective Bohr radius, donor binding, NV ZPL | W4, W4-v2 "n_D", W4 "E_b" ⚠ |
| g_e, g_I, μ_B, μ_N, 𝛍_e | g-factors, magnetons, electron moment | W0, W4 "μ_e" |

## I. Mixed sector, Migdal, absorption (WP3)
| Symbol | Meaning | Returns (local name) |
|---|---|---|
| ω_e, ω_ph | electronic-label and lattice energies of the prompt final state | W3 |
| Ê_e, Ê_L | label-energy operators | W3 |
| A^{Mig}_f, A^{PAER}_f | Migdal and PAER amplitudes | W3 "A_f" ⚠ |
| U_κ(p), Z_κ(p) | ion potential, effective ion charge | W3, L1 (KKL "Z_ion") |
| Ψ^{vib}_f ⚠ | vibrational state | W3 "χ_f" |
| δM_κ, E^{Mig}_1(q), P_Mig(q) ⚠ | drag-mass tensor; Migdal energy moment; Migdal probability | W3 "δM_κ, W_e(q), P_Mig" |
| T0–T6 (as WP3-T0…) | WP3 truncation labels | W3 |
| n_r(ω) ⚠ | refractive index | W3 "n(ω)", L1 "n_r" |
| ω_γ, α_pol(ω) | photon energy; atomic polarisability | W3 "α(ω)" ⚠ |
| σ₁ | real conductivity | W3, L1 |
| τ_J | the WP3 truncation point of τ | W3 |

## J. Soft limit and Ward identity (X1)
| Symbol | Meaning | Returns (local name) |
|---|---|---|
| 𝔄 = −iℓ_Q ê·p ⚠ | rigid-translation generator | D1, X1, X2, RA, RB "A" |
| 𝔖, s^W(Q) ⚠ | Ward-identity generator; its one-body operator | X1 "S, s" |
| K^{soft}_± ⚠ | soft vector of the eikonal factor | X1 "K_±" |
| Q_min, Q_p | minimal on-shell |Q| in the window; patch radius | X1 |
| |Q| → 0 | soft-limit parameter | X1 "η" ⚠ |

## K. Source-only notation (quote, never use in campaign formulas)
| Source notation | Campaign object |
|---|---|
| χ (response, D1/D2/X2), Π (D2) | R, R̃ |
| W = Im(−1/ε) (2101.08263) | L |
| n_{−k} (KKL eq. 4) | n_q with q = −k (sign differs) |
| e^{−iq_e·x} (Ibe, 1707.07258) | opposite phase to the boost e^{+im_ev·x}; |Z|² unaffected |
| S1, S2, iη, iΓ, β (EPW, Noffsinger) | A₁^v, A₂^v; resonant regulators (forbidden inside the window); emission label |
| q (EPW phonon wavevector) | Q |
| ε₀ (SI) | ε₀^SI |
| W̄_l, B_l (2105.02233) | 𝒲̄_l (per spin), B^{Cat}_l |
| 𝐋_s (2009.13534 orbital) | orbital angular momentum of species s (bold) |
| E_e, E_r (1509.01598, 2004.10709) | ω; E_R (R&K reuse E_r for phonon losses) |
| Q (step model, EXCEED-DM) | N_eh^{step} |
| λ_TF | k_TF |
| κ, ε_r (1708.08929, 1910.02091) | ε_bg, ε_r |
| g_χ(v) (1509.01598) | f_χ(v) |

## L. Label namespaces (always prefix with the return; CONVENTIONS §14)
| Label | Meanings |
|---|---|
| C1…C10 | CONTROLS.md controls; checks in WP1–WP6; O4's convention (now DC) |
| D1…D6 | return R1/D1; WP0-defect lists in WP1, WP2, WP4; WP6 source discrepancies D1–D6 |
| W1…W24, (W.n), (W), W1–W5 | WP5 equations; WP3 equations; X1 Ward identity; WP6 WP0-defects |
| N0–N6, N1–N5, N-a…N-e, X2-N1…N4, N1 | D1 conventions; WP3 rules; D1 specs; X2 specs; WP6 NOTATION flag (and return N1) |
| R1–R6, R1–R3, (R1)–(R3), R-k | WP5 gaps; X1 numerical rules and WP6 report objects; WP4 hypotheses; WP5 reduction |
| T1–T6 | STATEMENT v1 tasks; WP3 truncations (T0–T6); O4 toy checks (T0–T5) |
| K1–K10, J1–J7, G1–G13, L0–L24, O1–O6, RG1–RG8 | checks (X2, WP4); WP3 sum rules; gaps; LIMITS; WP0 open items; WP4 gaps |
| S1–S4 | D1/D2/X1/O4 sympy checks |

### Rows added from WP0-v2 (2026-10-31)
| Name | Meaning | Source |
|---|---|---|
| y_φ | coupling constant of absorbed boson φ to its target operator O (H_int = y_φ∫φO) | WP0-v2 (3.3), WP0-v3 [corrected R9] |
| 𝒟^γ_{μν} | in-medium photon propagator (Coulomb part v_C/ε_L, transverse 1/(ω² − k² − Π^γ_T)); NOT the DM-side tensor, which is 𝔇 | WP0-v2/v3 (3.6) [corrected R9] |
| Φ₀, Φ_n | adiabatic electronic ground and excited states Φ(r;R) | WP0-v2 |
| P_tot, M_tot | total momentum and total mass of the target | WP0-v2 |
| 𝓃_e(R_κ) | electron contact density at nucleus κ (sum rule 4.7) | WP0-v2 |
| δ_rel | relativistic fractional f-sum shift | WP0-v2 |
| E_e, E_h | carrier (electron, hole) energies in the final-state-resolved response | WP0-v2 (F10) |

## M. v4 additions (requested rows; R6 v2 returns)
| Symbol | Meaning | Returns (local name) |
|---|---|---|
| a_lat | lattice constant (bare a stays an operator index) | W1-v2, W4-v2 |
| q_BZ ≡ 2π/a_lat, G_min | zone-scale momentum (Si 2.28 keV); shortest nonzero G | W2-v2 IF-6, W0-v2 Table 6.1 |
| n_H | hydrogenic principal quantum number (n stays a band label) | W1-v2 [E8] |
| α_χ ≡ e_χ²/4π | dark fine-structure constant | W1-v2 L11 |
| k_v | VBM crystal momentum (companion of k_c) | W1-v2 |
| ψ̂(r) | electron field operator (hat mandatory) | W1-v2 §5.1 |
| α_LRC | LRC xc-kernel strength (−α_LRC/|q+G|²) | W1-v2 §1.2 |
| p_T | electron momentum transverse to q̂ (P_T stays the projector) | W1-v2 L3 |
| E_min,0(|q|), δq̂ | minimum of E_min(q) over q̂ at fixed |q|; angular offset from it | W1-v2 §3.6 |
| V_pot, V_ee, V_eN, V_NN ⚠ | potential energy and its parts (bare V = crystal volume) | W2-v2 IF-5; W0-v2 §6.2, (4.8) "V" |
| E^ad_n(R); E^ad_0 ≡ E_BO(R) ⚠ | adiabatic electronic energies; BO ground surface | W2-v2; W5-v2 "E_BO" |
| ∂_q̂ ≡ q̂·∇_{R_I} | directional nuclear derivative | W2-v2 |
| ε_∞(q̂) ≡ q̂·ε_∞·q̂ | directional high-frequency dielectric constant | W2-v2 |
| ν′, e^A_{ν′} | analytic (TO) modes of D^dyn_A | W2-v2 (4.2) |
| e^{s}_{κν} | e^{+} ≡ e*, e^{−} ≡ e (with s^ph) | W2-v2 (2.2) |
| c̄_κ, S̃_self,κ | mean random coupling (mean of c_κ); normalised self term | W2-v2 (7.1) |
| f^core_κ, δρ^val_κ | core form factor; valence part of δρ_κ | W2-v2 §10 |
| P_ph(n_ph|q,ω) | phonon-number distribution | W2-v2 |
| ΔE₃ | ω³-weighted mean excitation energy | W2-v2 (5.2′) |
| Δ^τ_A, a^A_{n_A}, θ_A | anharmonic increment, its A-type amplitude, anharmonic nuisance | W2-v2 "a_A", W6-v2 "θ_A" |
| E^{Mig}_3(q) | ω_e³ moment of the Migdal spectrum per nucleus | W3-v2 J8 |
| M^{exc}_{λ±} | exciton-replica amplitude (exc = exciton) | W3-v2 (W.14); W3 "M^{exc}_{S±}" |
| 𝒜^{PA}_ν(ω;T) ⚠ | T-independent phonon-assisted branch spectrum (σ₁ transfer) | W3-v2 §4 "𝒜_ν" |
| 𝒜^{2m}_α ⚠ | two-magnon amplitude | W4-v2 [2.4] "𝒜^α" |
| 𝒜̄^{1m}_{α,ν} ⚠ | one-magnon absorption amplitude ⟨0|s_e^α|ν,−k⟩/√N | W4-v2 [2.2] "𝒜̄^α_ν" |
| y_BCS, y′_BCS ⚠ | ω/Δ_BCS and its integration variable in 𝔤_I, 𝔤_II | W4-v2 [4.2] "y, y′" |
| y_R ⚠ | ω − E_R (impulse-peak offset) | W6-v2 (5.1′), W2-v2 "y" |
| τ^N_i, G^N(k,iν), g_pair | Nambu Pauli matrices; Nambu Green function; pairing coupling | W4-v2 [4.1] |
| ε^{BCS}, ε^{nor}, L^{BCS}, L^{nor} | superconducting / normal dielectric and loss functions | W4-v2 [4.2] |
| E₁, E₂ | Bogoliubov QP energies of the prompt pair | W4-v2 [4.6], W5-v2 §5 |
| x_qp, f_qp | non-thermal QP fraction; QP distribution | W4-v2 §4.3 |
| λ_ep, α²F(ω′), μ* | e–ph coupling constant; Eliashberg function (one symbol); Coulomb pseudopotential | W4-v2, W5-v2 |
| T_c, ω_D | superconducting critical temperature; Debye energy | W4-v2, W5-v2 "Ω_D" |
| ξ_coh ⚠ | BCS coherence length (ξ^{BCS}_k is the normal-state energy) | W4 "ξ₀", W5-v2 "ξ_BCS" |
| E_cut, w_⊥, 𝒫_L, H_L | Bogoliubov cutoff; weight outside 𝒫_L; low-energy projector; SW Hamiltonian | W4-v2 [1.1] |
| q_ff | momentum below which |F^{mag}_j|² ≳ 0.9 | W4-v2 §2.1 |
| z_ex, 𝓃_mag, N_sub | exchange coordination; magnetic-ion density; magnetic sublattices per cell | W4-v2 §1.3, §2.2 |
| 𝐒′_{Rj}, x_{Rj} | local-frame spin; magnetic-ion position (cell R, site j) | W4-v2 §2.1 |
| ω_{kν}, ω_h | magnon and hybrid-mode frequencies | W4-v2 §2 |
| S^S_ab, S^A_ab | real symmetric / antisymmetric parts of S_ab | W4-v2 §3.2 |
| γ^R_OA, γ^L_OA, Γ^R_χ, Γ^L_χ | optical activity and rates of the two enantiomers | W4-v2 [3.3] |
| d_film, S_film, S_bulk, S_surf | slab thickness; slab, bulk, surface DSFs | W4-v2 [4.5], W5-v2 §5 |
| R̃_D, R̃_bg, δε_D, E_bg, b_D, ω^D_max | Dirac/background proper responses; Dirac part of ε; remote gap; pair velocity factor; Dirac ω cutoff | W4-v2 §5 |
| m*, ι, a^{val}_ι, F^{env}_ι, k_ι | effective mass; valley index; valley amplitude; envelope; valley momentum | W4-v2 [6.2] |
| S^D_ab, ñ_e, Õ_a, ε_host, 𝓃_NV, r_tr | defect response; host-screened operators; host dielectric; NV density; transition-density size | W4-v2 §6 "n_NV" |
| Γ^{(ν)}_χ | rate per DM into mode ν (exothermic) | W4-v2 [7.2] |
| 𝒬^{D-g}_{n,m} ⚠, N̂_qp, N̂_ph, U_qp, Z_qp, Γ_qp, Γ_ph, S^{(n,m)}_ab | Theorem D-g sector projectors, number operators, dressing, QP residue and width, phonon width, sector spectra | W4-v2 §8 "𝒬_{n,m}" |
| 𝔱, x′_j | cascade particle type; child states of a vertex | W5-v2 (W3), (W7) |
| E_car | carrier energy above its band edge (local) | W5-v2 (W7), (W8) "E" |
| E_th^{ii}, 𝒦̄_𝔱 | impact-ionization threshold; iso-energy-averaged kernel | W5-v2 |
| M^{ii}_{dir}, M^{ii}_{xch} ⚠ | direct and exchange impact-ionization amplitudes | W5-v2 "M^{dir}, M^{exc}"; 0812.2923 "M_D, M_E" |
| E^{conf}_i, r̂_R | defect-configuration energy; recoil direction | W5-v2 §3–§4 |
| λ_dB, ℓ_int, t_pr | de Broglie wavelength; interaction length in ξ_Mas; prompt time | W5-v2 §3.2 |
| E^{form}_V, E^{form}_I | vacancy, interstitial formation energies | W5-v2 §3.2 |
| h_LZ, ΔF_LZ, P_LZ | Landau–Zener coupling, slope difference, probability | W5-v2 §3.3 |
| b_imp, E_coll, V_bias | impact parameter; collision energy; NTL bias voltage | W5-v2 §3.4, (W11) |
| ℛ_rel, ω_bar, Γ_att, E_slope | relaxation-event rate; barrier curvature frequency; attempt rate; release-spectrum slope | W5-v2 §4 |
| Γ_pb, Γ_esc | pair-breaking and phonon-escape rates | W5-v2 §5 |
| N_FP^{NRT}, E_dam, E_st,1, p_surv | NRT count, damage energy, stored energy per FP, survival fraction | W5-v2 §6.3 |
| a₀ | Bohr radius | W5-v2 §6.1 |
| θ_seed, θ_{R-k}, θ_GW, θ_exch, θ_Eg, θ_𝔉, θ_PES, θ_LZ, θ_esc ⚠ | WP5 nuisances (θ_k family) | W5 "θ_k", W5-v2 "θ_Rk", W6-v2 "θ_W, θ_X" |
| ℒ, π_k | likelihood; prior of θ_k | W6-v2, W0-v2 (8.3) |
| a^A_k ⚠ | A-type nuisance amplitude (a_{kν} stays the magnon operator) | W6-v2, W0-v2 (8.1) "a_k" |
| A^{(n)}(q,ω;Λ), tr_T, d₂, d₂′ | Λ-resolved A^{(n)}; transverse trace; isotropic 𝔇^{(2)} coefficients | W6-v2 (1.4), (4.1) |
| Π_mom[·] ⚠, c_b, 𝔪_n, Δ′_A, P_δ, θ_δ, σ_δE, δ_θ | moment projection, coefficients, moments of S^τ, shape template, δE^kin amplitude and uncertainty; fractional nuisance size (6.2) | W6-v2 (5.1′) "Π[·]"; W6-v3 "δ" (IF6-2) |
| P(i|Λ), 𝒜_i(u₀), v_j, η̃_j, N_v | detector-cascade map; single-step column of 𝒜; halo steps | W6-v2 |
| δ_v,×, a_lens, ϱ | regime crossover speed; lens curvature; axial distance | W6-v2 (3.2), (3.4) |
| k_δ, w_δ = √(1 + 2.71k_δ²) − 1 ⚠ | ln(1+δ_θ); quadratic-root value (replaces W_Lam; not a Lambert W) | W6-v2 (6.2) "W", W6-v3 "W_Lam" (IF6-2) |
| σ̄_e^up, q_max, N_q, N_ω, N_bins | upper limit; library cutoff; grid sizes | W6-v2 |
| 𝓃_e^{(sh)}, J^{(sh)}(p_z), E_B^{(sh)}, p_z | shell density, Compton profile, mean binding, projected momentum | W6-v2 (5.2); W6 "J_s" |
| 2.71 (χ²₁ 90% quantile) | written as a number, never bare c | W0-v2 (8.3), W6 "c = 2.71" |

## Rows added R9 (2026-10-31; from returns/R8/AUDIT-2.md §6, m17, m26–m31)
| Symbol | Meaning | Source |
|---|---|---|
| R^{phys}_{j^αj^β} = R_{j^αj^β} + δ_αβ𝓃_s/m_s | physical current kernel (R^∞ ≡ 0) | W0-v3 (4.2), G11; B "K" |
| 𝐁^{NR}_{αβγ} ≡ b^{NR}_{αβγ}/ω² | cubic nonreciprocity tensor of S_ee; b^{NR}_{αβγ}(ω): odd (q-linear) part of the current response, S_{j^αj^β}(q) − S_{j^αj^β}(−q) = 2b^{NR}_{αβγ}q^γ; one object (AUDIT-2 m17) | W0-v3 (4.3); W4-v3 [3.2′]; W6-v3 (1.5) |
| K_pk (= 𝐊_pk) ⚠ | pocket-pair vector k_c − k_v + G | W3-v3, W6-v3; v2 "K" |
| d_K(\|q\|) ⚠ | \|\|q\| − \|K_pk\|\| | W3-v3, W6-v3; W6-v2 "d" |
| ϑ, ϑ_Q ⚠ | polar angles of q̂ and Q̂* from K̂_pk | W3-v3; v2 "θ" |
| Q_w | window radius in \|Q*\| | W3-v3 §M3, W6-v3 |
| p̄_on | onset exponent of the angle-averaged S̄ (p_on keeps the fixed-q meaning) | W3-v3, W6-v3 |
| γ_c, β_c | quadratic anisotropy and linear (conical) coefficients of c_ν about an axis | W3-v3 |
| C^{el}_{11}, C^{el}_{12}, C^{el}_{44} | elastic constants (C_κ is taken) | W3-v3 |
| E^{PA}_th(q̂) ⚠ | PAER threshold at direction q̂ | W3-v3; v2 "E_th(q̂)" |
| m_χ^{PA} | PAER kinematic edge mass | W3-v3 |
| m_χ^{ZP} | zero-phonon kinematic threshold mass [E13] (distinct from m_min) | W1-v3 |
| E^{ZP}(q), q^{ZP} | lowest zero-phonon final-state energy at total momentum q; the \|q\| at which [E13] is attained (not q_*, not Q*) | W1-v3, W6-v3 |
| M_x, m_l, m_hh | exciton/pair translational mass M_x = m_l + m_hh; conduction longitudinal mass; heavy-hole mass | W1-v3, W3-v3 |
| k_rel | relative e–h momentum offset from the minimum-energy pair | W1-v3 |
| ℓ_∇, ρ_cv^{ref} | vertex-gradient length \|∇_kρ_cv\|/\|ρ_cv^{ref}\|; reference allowed vertex | W1-v3 |
| η_PA, ε̄_PA | PAER-to-allowed-ZPL spectral ratio; PAER excess energy in [E14] | W1-v3 |
| ϖ_II | forbidden-class ZPL / PAER ratio [E14] | W1-v3 |
| ε_ex ≡ ω − E_min(q) ⚠ | excess energy above the zero-phonon edge | W1-v3 [E14]; v3 draft bare "ε" (AUDIT-2 m26) |
| t_d ≡ (¼,¼,¼)a_lat | diamond nonprimitive translation | W1-v3 §3.2 |
| k_xc ≡ δ³E_xc/δn³ | second-order xc kernel (ALDA source term in (M.13)) | W3-v3 §M7 |
| w^{EPW}_± ⚠ | EPW thermal weight | W3-v3 (M.4) "𝒫_±" (collides with projectors 𝒫₀, 𝒫_⊥, 𝒫_GS; AUDIT-2 m27) |
| ad_H | ad_HX ≡ [H, X] (not L) | W0-v3 (4.5) |
| H_oo, 𝒦^{oo}_ij | Breit orbit–orbit term and its kernel | W0-v3 (1.2), (4.6″) |
| δ_oo, δ_mv | orbit–orbit and mass-velocity parts of δ_rel | W0-v3 (1.2) |
| E′_ee | e–e Coulomb energy without the uniform G = 0 Hartree part | W0-v3 (4.6″) |
| 𝓃_e^{(κ)}(y), 𝓃^{(κ)}_G | electron density conditional on a nucleus κ; its Fourier components | W0-v3 (4.7′); A "𝓃̄_e" = 𝓃_e |
| 𝔞_e, 𝔞_ion | two-fluid static susceptibilities −v_CR̃_ee, −v_CZ_κ²R̃_κκ | W0-v3 (9.4′); A/B "a, b" |
| 𝒫_GS, 𝒫_X | sector projectors (not Π) | W0-v3 §6.2(i) |
| N_nuc, Γ_max | number of nuclei; O4's maximal width in the 𝒞_adm bound | W0-v3 |
| 𝔰_BCS(y) | BCS screening function P∫₀^∞dy′y′²[𝔤_IΘ(y′−2) − 1]/(y′² − y²); 𝔰_BCS(0) = 0 | W4-v3 [4.2′] |
| 𝔣_Lin(z_rel), z_rel | small-q Lindhard bracket (ε_Lin(q,z) − 1)/(ε_Lin(q,0) − 1); complex frequency ω + iγ_rel | W4-v3 §4.5 |
| H_d, H_off, 𝔥_off | sector-diagonal part of H; off-diagonal remainder; its norm bound (G5) | W4-v3 §8 |
| f_Δ, g_bin, ĝ_bin, Δω_bin, c_g | bin function g_bin(x/Δω_bin)/Δω_bin; its shape and Fourier transform; bin width; (1/2π)∫\|s\|\|ĝ_bin\| | W4-v3 [8.1] |
| S^{bin}_ab, C^{cross}_ab | binned spectrum; cross-sector remainder | W4-v3 [8.1] |
| Λ′_D, 𝓁, 𝓛′_D | Dirac cutoff with the "1" absorbed (Λ_De^{3π/α̃}); ln((2v_FΛ_D)²/\|𝓈\|); complex log with Λ′_D | W4-v3 §5.3 |
| Π^{med}_γ ⚠, κ_mix,eff | in-medium photon self-energy (all charges); in-medium effective mixing | W4-v3 [5.4] "Π_γ" (collides with Π^γ; AUDIT-2 m28) |
| Rate_src, Rate_URF, Γ_abs,src | source-convention and URF rates (ratios only) | W4-v3 [5.3], [5.5] |

## Rows added WP7 (2026-11-01; WP7-B1-v2, WP7-B2-v2, WP7-D-v2, WP7-T-v2 after R12 verification; WP7-E rows in the next section)
Abbreviations: B1, B2, D, T = returns/R12/WP7-{B1,B2,D,T}-v2.md. The "Clashes resolved" table at the end lists every rename; returns are not edited, so a
return's local name is read through this table (owed renames → state/CORRECTIONS.md).
| Symbol | Meaning | Source (local name) |
|---|---|---|
| 𝔬, r_𝔬, 𝖱_𝔬, N_mol | molecule-in-cell label (κ stays the nuclear species), its position, orientation, molecules per cell | B1 (E5.1) |
| 𝔵, E_𝔵, f^{(𝔬)}_{0𝔵}(q) | molecular singlet excited state, its energy, molecular form factor (√2 included) | B1 (E5.1) |
| H^F, 𝔍^F(Q), A^{F,λ}_{𝔬𝔵}(Q), w_{𝔬𝔵}(q) | Frenkel Hamiltonian, transition-density Coulomb coupling, Frenkel envelope, screened molecular vertex | B1 (E5.1)–(E5.2) |
| 𝓃_mol | molecule number density (one object in B1 §2 and B2 (B2.7.2)) | B1, B2 |
| 𝓃_u, 𝓃_t | unit density of a low-dimensional embedding; tube areal density | B1 (1.1), (E8.1) |
| F_⊥(q_⊥), F_z(q_z), ϱ_⊥ | transverse form factors and profile of a low-dimensional unit | B1 (1.1), (E12.1) |
| d (dimension), S_d, S_wire, S_sheet ⚠ | embedding dimension; d-dimensional, wire, sheet responses per unit d-volume (S_d ≠ S^D_ab, the defect response) | B1 (1.1), (E8.1)–(E8.2) |
| N_ch, g_LL (= g_c), v_LL, r_t, ε_env | 1D channel number; Luttinger charge parameter and velocity; tube radius; environment dielectric constant | B1 (E8.1); 2607.15338 "g, v" |
| v_C^{1D}, v_C^{2D}, v_C^{L}(q_∥,q_z) | wire, sheet, layered-stack Coulomb kernels | B1 (E8.1), (E8.2), (E9.1) |
| R̃^{2D}, R̃^{2D}_low, R̃^{2D}_bg, r_K | sheet proper response, low-energy and remote parts; Keldysh length (r_Kq ≡ −v_C^{2D}R̃^{2D}_bg) | B1 (E8.2) |
| k_TF,1, ω_{p,2}, ω_a, w_a(q), v_a, v_F,1, Γ_a | light-species TF momentum; heavy-species plasma frequency; demon mode, its f-sum share, velocity ω_{p,2}/k_TF,1; light-species Fermi velocity; demon Landau width (FWHM) | B1 (E8.3), §3(c) |
| a_s, ε_b,lay, N_lay, f_fill, ε_A, ε_B, d_A, d_B, ε_∥, ε_⊥ | stack period; interlayer background (≠ ε_bg); layer number; filling; layer dielectrics and thicknesses; EMT tensor | B1 §4 |
| R_QD, ϕ_QD, 𝓃_QD, ε_in, ε_out, E_g^{QD}, 𝔣^{loc}_ℓ, ρ_cv^{cell} | dot radius, volume fraction, density; inside/outside dielectric; confined gap; multipole local-field factor; band-edge cell form factor | B1 §5 |
| 𝒫^W_0, (H_W), δM^W, N_e^W | site-0 Wannier projector (projector family 𝒫₀, 𝒫_⊥, 𝒫_GS, 𝒫_X, 𝒫^W_0); rigid-Wannier hypothesis; its drag mass; electrons in site-0 WFs | B1 §7 |
| ε^{sym}_{GG′} | symmetrised RPA dielectric matrix δ − v_C^{1/2}R⁰v_C^{1/2} (NOTATION ε̃ unchanged) | B1 §7(a); 2011.13352 "ε̃" |
| P^{Mig}_f(q) | Migdal transition probability to a bound final state f | B1 (X8.2) |
| γ_H(ω), α²F_tr, λ_tr | Holstein rate; transport Eliashberg function; transport coupling | B1 (A2.1) |
| 𝔣^{loc}_D, ε₂^D | donor local-field ratio; dopant ε₂ (screening applied once through 𝔣^{loc}_D) | B1 (A6.1); 2212.04504 "E_eff/E_0" |
| q_Δ*, v_Δ* | exothermic shell momentum and velocity (q_ν* stays the mode shell) | B1 (I3.2) |
| E_χ, p_χ, J^μ_χ, Φ_χ | DM energy, momentum, vector current, flux (relativistic DM) | B1 §12 |
| 𝒱_ν(k) ⚠ | k → 0 one-phonon absorption vertex of a target row (≠ 𝒱_a, the DM vertex) | B2 (B2.1.1) |
| 𝔳_κ, 𝔳_I, 𝔳̄, δ𝔳_κ, δ𝔳_I, 𝔳^{LO}_κ | per-site linear absorption vertex; mass-averaged vertex Σ𝔳/ΣM; mass-subtracted vertex; LO-residue vertex Z_κ − Z*_κ/ε_∞ | B2 (B2.1.1)–(B2.2.1) "v_κ, v̄, δv, v^{LO}" (renamed) |
| D_I(ω), e_Iν, ω_ν | site-projected VDOS (site analogue of D_κ(ω)); modes ν of one disordered configuration | B2 §2 |
| λ^I_κ | nuclear spin coupling F^Σ_κh^I_κ | B2 §2.2; 2411.10542 "λ_j" |
| C^{IR}(ω), A^{IR}, B^{IR} | IR-to-VDOS coupling function; its Taraskin coefficients (C^{IR} = A^{IR} + B^{IR}ω²) | B2 §2.3 "A, B" (renamed) |
| p_ν | mode effective charge Σ_Iε̂·Z*_I·e_Iν/√M_I (not p_nn) | B2 (B2.3.1) |
| Γ^{ph}_ν | mode-resolved phonon linewidth (Γ_ph is its mode-independent form) | B2 (B2.3.1) |
| ϑ^{BL}_I (= ϑ_I), ϑ̄, σ_w | B−L charge per unit mass N_I/M_I; mass-weighted mean; weighted variance Σx_IM_I(ϑ_I − ϑ̄)² | B2 §2.4 |
| Ω_at | atomic volume | B2 (B2.4.2) |
| ω_BP, d_nn, g₂(r) | boson-peak frequency; nearest-neighbour distance; pair distribution | B2 §2.3, §2.5 |
| V_opt, 𝔟_χN, σ_crit(v) | optical potential; χN scattering length; Born-validity cross-section | B2 §3 |
| δ_Lind, Φ^{(2)}_eff, ρ_G, B^{SCHA}_κ | Lindemann ratio; SCHA force constants; Gaussian trial state; its displacement tensor | B2 §4 |
| 𝔰_net, k_⊥ | net spin per magnetic cell; k transverse to the moment | B2 §5 |
| ω_{K,x}, ω_{K,y}, ω_K, N_{x,y,z}, M_s ⚠ | Kittel stiffnesses and frequency; demagnetising factors; saturation magnetisation (≠ m_s species mass) | B2 (B2.5.3) |
| F_M, F^{mag}_S | neutron magnetic form factor (spin + orbital); spin-only form factor | B2 (B2.6.1) |
| T_d | temperature of the neutron data set | B2 §6 |
| L^{ph}_{Qν}, 𝐌^{ph}(q), 𝐣(q) | phonon angular momentum (≠ ℓ_Q); Born-charge orbital moment; ionic current Σ(eZ*/M)Pe^{iq·R} | B2 §7 |
| D_ZFS, ω_Z, p_m | SMM zero-field splitting; Zeeman energy; level populations | B2 (B2.7.2) |
| κ_URF | URF chiral-detection branching (source κ is not κ_mix) | B2 §7 |
| c̃, c̃_κ, r^{ion}_core | coupling per unit mass; ionic-core radius | B2 §8 "r_c" (renamed) |
| Y_CC, p_q, f_opt, ⟨N_x⟩, p_FH | colour-centre yield factors | B2 (B2.9.1) |
| S_CM, S_int, S^{diss}, p_esc, ΔE_B | molecular structure factors; cage escape; bond energy | B2 (B2.10.1) |
| m_φ | mass of the absorbed boson φ (companion of y_φ); for a dark photon as DM also m_φ | B2, D, T (D §3.4 "m_V", renamed) |
| t_coh, ℓ_coh, t_int, N_dB, 𝒩_c, Γ_T | coherence time and length; integration time; occupation per de Broglie volume; coherence cells; target response width | D §1.0, §1.4 |
| 𝒮_φ(k,ω), F_φ(ω), f_sp(v) | field spectral density; normalised line; speed distribution | D (D.1) |
| O_rd, X_rd | readout operator; its sample total | D (D.2), (D.5) |
| 𝒮^{sig}, 𝒮^{int}, 𝒮^{det}, 𝒮_n, TS_A | signal, intrinsic, detector, noise PSDs; Asimov statistic | D (D.5)–(D.6) |
| β_s, p_pol | inverse spin temperature, tanh(β_sω_Lar/2) = p_pol; spin polarisation | D §1.5 "p" (renamed) |
| δω_Lar, T₁, T₂, M₀, Ω_Rabi | Larmor detuning (ω_Lar row §C); spin relaxation times; equilibrium magnetisation; rotating-frame Rabi frequency | D (D.4) "δω_L, Ω_a" (renamed) |
| d_EDM, E*_I | nucleon EDM; effective field at site I | D §1.2 |
| γ^{mode}_n, 𝔔_mode, 𝔔^{eff}_DM | mode width; mode quality factor; effective DM quality factor (quality factors are 𝔔, as in T) | D (D.7) "γ_n, Q_mode, Q_DM^eff" (renamed) |
| 𝔘_C(k) | Coulomb-energy density row (∂H/∂ln α) | D (D.8) |
| h_mod, d_{m_e}, d_α, δ_rel^a | modulus strain; modulus couplings; fractional relativistic lattice shift | D (D.8); source "d_e" |
| ν̃, m_ν̃, E_ν̃, 𝐤_ν̃, Λ_F, 𝔏, 𝔇^F, ω^F_q, σ_NC | fermionic-absorption final fermion, its mass, energy, momentum; contact scale; lepton tensor; DM-side tensor; relativistic ω_q; NC cross-section | D (F.1)–(F.6) |
| m_φ^{med}, t_M | (F.7) light scalar mediator mass (valid for m_φ^{med} > m_χ); four-momentum transfer squared t_M = 2m_χω − m_χ² | D (F.7) "m_φ, t" (renamed) |
| 𝒮̄_at | per-atom S̄ (= π\|f_ion\|²/2E_R, spin-orbital convention) | D §2.4(b) |
| 𝒢_a, 𝔇^{pair} | DM-side pair vertex; pair tensor for derivative DM currents | D (T.1)–(T.2) |
| 𝒯^{(2)}, 𝒯^C, R^{(2)}_{abc} | second-order and Compton operators; three-point response (not χ^{(2)}) | D §3.1, (T.3) |
| e_λ, e′_λ′ ⚠ | dark-boson and photon polarisation vectors (≠ e_{κν} phonon eigenvectors, ≠ charge e) | D (T.3) |
| ω′_γ, σ_Th, x | emitted photon energy; Thomson cross-section (σ_T is WP6's); dark-Compton expansion parameter x = m_φ/m_e (local) | D (T.4) "ω′" (renamed) |
| Ī, Γ_med, Σ_χ* | Bethe mean excitation energy; in-medium width; DM self-energy | D (S.2), §4.2 |
| geom (metadata) | geometry key ∈ {bulk, body, 1D, 2D, stack} (CONVENTIONS §13 row 25, R13 amendments) | D IF-D3; B1 IF-B1-9 |
| Δ_as, Δ_tun, E_TLS | TLS asymmetry, tunnel splitting, splitting | T §1.2; 1705.01108 "ε, Δ₀" |
| 𝔣^{def}_s, 𝔣^{def,core}_s, 𝔣^{def,loc}_s | defect vertex (1.1)–(1.2); core part; localised form factor (decoration mandatory) | T §1.2–§1.3 |
| γ^{def}, 𝐩^{def}, D (local to T §1.3) | deformation potential (δΔ_as = 2γ:S); TLS dipole; force-dipole tensor (D_R − D_L = −2γ) | T §1.3 |
| w^{ac}_e, w^{ac}_N, w^{ac}_c | acoustic species weights of the host term | T §1.3 "w_e, w_N, w_c" (renamed) |
| G^{ac}(q,ω), x, η_pole, B, a (local to T (1.3)) | acoustic propagator; pole variable; pole width ωΓ_ph; host and core amplitudes | T (1.3) "G, η" (renamed) |
| P̄_STM, C_TLS, tanδ₀, tanδ_TLS, 𝔔_ph, 𝔔_el, ℓ_TLS | STM density (one-sign); tunnelling strength; loss tangents; acoustic and electric quality factors; TLS phonon mean free path | T §2 |
| Γ₁, Γ₂, Γ_dph, Γ_↓, Γ_↑ | TLS relaxation, decoherence, pure-dephasing, down and up rates (Γ_ph as in §M) | T §2.1 "Γ_φ" (renamed) |
| J^{dfn}, Δ_dfn, ϖ^{dfn}(k), E^{loc}_D, ε^{dfn}(k), m^{dfn} | defecton hopping, bandwidth, dispersion shape, site energy, dispersion, band mass | T §3.1 "ϖ, ε_D" (renamed) |
| a₁₁₁, μ_FK ⚠, V_P, M_cr, E_mig, E_rec | crowdion (FK) spacing, inverse kink width (not a reduced mass), Peierls barrier, FK kink mass, migration and recombination energies | T §3.2 |
| λ_ij, λ_P, ω_well, d_tun, M_eff | tunnelling exponent; Phillips/Jäckle λ_P = (d_tun/2)√(2M_effV); well frequency; tunnelling distance; tunnelling mass | T §4.1–§4.2 "d" (renamed) |
| ε^{hop}_ij, Δ_ij, ΔZPE_ij | configurational release of hop i → j (E^{conf}_i − E^{conf}_j); tunnelling element ω_well e^{−λ_ij}; zero-point change, carried in ℋ_ph | T §4.1 "ε_ij" (renamed) |
| λ^{sb}_k, J^{sb}, J_ph, J_el, J_loc, 𝒬^{sb}(t), A_T(ε) | bath couplings and spectral densities; overlap exponent; finite-T FC line shape | T (4.1)–(4.2) "𝒬(t)" (renamed) |
| α_ohm, ω_co | ohmic coupling (= 4K₂₀₀₉); cutoff | T §4.1 |
| T_hi, T_lo | start and end temperatures of the heat-release law (LIMITS L29) | T §4.5; 1610.03974 "T₁, T₀" (renamed) |
| p_st, 𝔠, 𝒦^{rel}, 𝒦̂^{rel}, ⟨N_hop⟩ | stored-energy distribution; defect class; hop-event release kernel (5.2), unit-normalised form; mean hop number | T §5.2–§5.3 "c" (renamed) |
| E_st^{rel}, E_st^{unrel}(t_obs), E_st^{frz} | released, unreleased-by-t_obs, frozen (t_obs → ∞) stored energy | T §5.3 |
| r^{def}_core | defect-core radius (static window q ≪ 1/r^{def}_core) | T §1.4 "r_core" (renamed) |
| Source-only (quote, never use in campaign formulas) | 2411.10542 ξ_κ; 2504.02927 S_n, γ_n, N_f, Ω_c; 2507.14287 G_{S,i}, f_DM, g_DM, ξ (written ξ_pair = 44.8 when cited; ≠ ξ(v_min), ≠ F_DM); 2308.00309 Y_ee, Y_χν; 2011.01940 f_ion; 2501.05504 Q_s, Q_p (→ 𝔔_s, 𝔔_p); 2110.01587 d/L (f_fill); 2101.01241 ω_a, M_a | B2, D, B1 |
| LIMITS labels LB1-1…13, B2-L1…10, L-D1…12, L25–L32 | WP7 LIMITS rows (always with the prefix); catalog process IDs are written "Cat. E5, Cat. L9, …" | LIMITS "WP7 (R12, REFEREED)" |

**Clashes resolved (CONVENTIONS: one symbol, one object; NOTATION v4 rule "a decorator is part of the name").**
| Return symbol (meaning) | Clashes with | Resolved name |
|---|---|---|
| D ω_L (Larmor frequency) | NOTATION §C ω_L = LO frequency; ω_Lar = Larmor | ω_Lar, δω_Lar (as B2 already does) |
| D γ_n (mode width) | B2 γ_n (2504.02927 neutron quantity) | γ^{mode}_n; B2's γ_n source-only |
| D Q_mode, Q_DM^eff, source Q_s, Q_p (quality factors) | Q ⚠ phonon wavevector; T uses 𝔔 for quality factors | 𝔔_mode, 𝔔^{eff}_DM, 𝔔_s, 𝔔_p |
| D Ω_a (Rabi frequency) | Ω (cell volume), B2 Ω_at (atomic volume) | Ω_Rabi |
| D p (spin polarisation) | p_i (Gibbs weights), momentum p | p_pol |
| D ξ (2507.14287 pair normalisation) | ξ(v_min) halo integral (CONVENTIONS §8) | source-only, cited as ξ_pair |
| D m_φ in (F.7) (scalar mediator mass) | m_φ = absorbed-boson mass (D §1, B2, T) | m_φ^{med} |
| D m_V in §3.4 (dark-photon DM mass), x = m_V/m_e | m_V = mediator mass in F_DM (CONVENTIONS §9) | m_φ; x = m_φ/m_e |
| D t in (F.7) (Mandelstam t) | t = time | t_M |
| D ω′ (emitted photon energy) | ω′ = phonon-energy variable (D_κ(ω′), w_κ(q;ω′), α²F(ω′)) | ω′_γ |
| D T₁, T₂ (spin times) vs T §4.5 / 1610.03974 T₁, T₀ (temperatures) | each other (WP7-internal) | spin times keep T₁, T₂; heat-release temperatures T_hi, T_lo |
| B2 v_κ, v̄, δv, v^{LO} (absorption vertices) | v ⚠ DM velocity family; v_s target-species velocity (v^⊥ = v_χ − v_s) | 𝔳_κ, 𝔳̄, δ𝔳, 𝔳^{LO} |
| B2 A, B (Taraskin IR coefficients) | A_κ (mass number), B_κ (displacement tensor); T local B | A^{IR}, B^{IR} |
| B2 r_c (ionic-core radius) | c reserved for band/charge-channel subscripts (CONVENTIONS §4, §6); T r_core (defect core) | r^{ion}_core; T's r^{def}_core |
| T c (defect class) | CONVENTIONS §4: c only as a band subscript | 𝔠 (WP7-E-v3 already writes 𝔠; nothing owed there) |
| T η (local pole width ωΓ_ph) | η(v_min) halo integral | η_pole |
| T G(q,ω) (local acoustic propagator) | G reciprocal vector; G^N Nambu Green function | G^{ac}(q,ω) |
| T ε_ij (hop release energy) | ε_{GG′} dielectric matrix (two-index ε); bare ε flagged in AUDIT-2 m26 | ε^{hop}_ij |
| T ε_D(k), ϖ(k) (defecton dispersion, shape) | ε (dielectric) and δε_D (Dirac part of ε); ϖ_II (R9) | ε^{dfn}(k), ϖ^{dfn}(k) |
| T 𝒬(t) (overlap exponent) | 𝒬_κ (dynamical quadrupole), 𝒬^{D-g}_{n,m} (sector projectors) | 𝒬^{sb}(t) |
| T Γ_φ (pure dephasing) | subscript φ = absorbed boson (m_φ, y_φ, 𝒮_φ) | Γ_dph |
| T w_e, w_N, w_c (acoustic weights) | w_κ(q;ω′) ⚠ one-phonon measure | w^{ac}_s |
| T d (tunnelling distance) | B1 d (embedding dimension) | d_tun |
| B1 and B2 𝓃_mol | same object in both | one row (merged) |
| B1 / D geom values | same metadata key, different value sets | geom ∈ {bulk, body, 1D, 2D, stack} (CONVENTIONS §13 row 25) |
Kept with ⚠ (distinct names under the decorator rule, but easy to confuse): S_d vs S^D_ab; 𝒱_ν vs 𝒱_a; e_λ vs e_{κν}; M_s vs m_s; μ_FK vs μ_χe; D (T local) vs D_I, D_ZFS, D^n.

## Rows added WP7-E (2026-11-01, R13 merge; returns/R12/WP7-E-v3.md after R12 VER ×2 and VER2 ×2)
Abbreviation: E = returns/R12/WP7-E-v3.md. Energies are configurational; ΔZPE is carried inside ℋ_ph (CONVENTIONS §13 row 23). Owed renames inside E: state/CORRECTIONS.md §18.
| Symbol | Meaning | Source (local name) |
|---|---|---|
| E_hot, E_pairs, E_X ⚠, E_trap, E_es (E_es^{trap}, E_es^{img}), E_esc, E_sig, E_sl | event reservoirs: hot carriers, thermalised pairs, exciton reservoir Σ(E_g − E_x^b), trapped carriers, electrostatic (trap, image), escaped, signal, sensor loss (E_X ≠ E_x, the exciton energy) | E §1.1 |
| ℋ_ph = ℋ_ph^{avail} + ΔZPE, ℋ_pr, ℋ_el | phonon reservoir (only ℋ_ph^{avail} reaches a sensor); prompt and electronic heat | E §1.1 |
| ΔE_X^b ≡ −N_XE_x^b, N_X, φ_EHD | exciton binding correction, bound-pair number, droplet energy per pair | E §1.1 "E_x" (renamed) |
| ΔZPE(t), δZPE | zero-point shift of occupied basins (inside ℋ_ph); per-hop change (ΔZPE_ij as WP7-T) | E §1.1 |
| E_st^{unrel}(t_obs), E_st^{rel}, E_stored, ⟨N_hop⟩ | as WP7-T rows; E_st configurational | E §1.2 |
| N_e^f, N_h^f, N_e^{tr}, N_h^{tr}, E_pairs^{unp} | free and trapped carrier counts; unpaired free-carrier energy | E §1.3 |
| μ_F, ℰ_b, D_diff, r_cap | contact Fermi level; bias field; carrier diffusion constant; capture radius | E §1.3, §2.1 "r_c" (renamed) |
| 𝔪 ⚠ | event marks (≠ 𝔪_n, moments of S^τ) | E (E3) |
| 𝒲_bias, V_k, Q_k | bias (battery) work; electrode potentials and charges | E (E11) |
| ϵ_prim^{NR}, ϵ_prim^{ER}, ϵ_NTL, Δϵ, δ_coll ≡ Δϵ/ϵ_prim, r_coll ≡ ϵ_NTL/ϵ_prim | multiplicative collection efficiencies; NR/ER difference; its fraction; NTL/primary collection ratio | E §3.1 "δ, r" (renamed) |
| D′, d′ = D′/ω, X^{oth} | pre-sensor deficit (incl. ΔZPE); its fraction; non-E_st deficits | E §3.1 "X" (renamed) |
| κ_cal ≡ (1 + y_iong_Luke)/(1 + g_Luke), g_Luke ≡ eV_b/ε_eh, y_ion | calibration ratio; Luke gain; ionization yield (1803.02903 "y") | E (E13) "κ, g, y" (renamed) |
| η₀(r_coll) | η^φ_NR with no stored energy (collection only) | E (E13) |
| E^tr_{e,j}, E^tr_{h,j}, n^{e,h}_j, 𝓃_j, σ_cap(u_car), u_car, Γ^{em}_j, ℓ^tr_{e,h} | trap depth, occupations, trap density, capture cross-section and carrier speed, emission rate, trapping length | E §2.1 "σ" (renamed) |
| U_R, 𝔮_i, m_ind(r), N^meas = Σ_i𝔮_i, φ_t, F_meas^{obs} | Ramo potential; per-carrier induced-charge mark; position-mean mark; measured charge; its cumulant generating function; observed Fano factor | E §2.3 "𝔵, m(r)" (renamed) |
| t_win, t_obs, E_thr^det, P_rel, ϵ_coll, ℛ_q^{del}, ℛ_del, dℛ_bg, 𝔰_𝔠, 𝒯_𝔠, 𝒯_q, 𝐌 ⚠, 𝒫_det | windows; detector threshold; release probability; collection efficiency; delayed rates; background; class sources and transfers; measured-observable vector (≠ 𝐌^{ph}); detector stage | E (E3), §3.3 |
| C_X, τ_X, n_X, n_BX, σ_BX | exciton kinetics (capture coefficient, lifetime, densities, biexciton cross-section) | E §7 |
| θ_unrel, θ_λ, θ_γ, θ_𝒦, θ_law, θ_st, θ_tr^{pr}, θ_tr, θ_em, θ_SC, θ_coll, θ_exc, θ_bg,𝔠 | WP7-E nuisances (θ_k family; WP6-v3 types); θ_exc = exciton formation/recombination and gap-energy release (type T on r_g^{NR}, r_g^{ER} separately) | E §6 "θ_X" (renamed R16: θ_X was WP6-v2's local name for θ_exch) |
| Source-only (quote, never use) | 1803.02903 ε (= ε_eh), y_C, η^φ_NR as quoted; 1805.09942 f_DF, f, f_sur | E §3–§4 |
| LIMITS labels L33–L38 | WP7-E LIMITS rows | LIMITS "WP7-E" |

**Clashes resolved (WP7-E).**
| Return symbol (meaning) | Clashes with | Resolved name |
|---|---|---|
| E κ (calibration ratio) | κ ⚠ nuclear species index (only) | κ_cal |
| E X, ΔX (non-E_st deficits) | X sector (CONVENTIONS §13 row 18) | X^{oth}, ΔX^{oth} |
| E g ≡ eV_b/ε (Luke gain) | g_{mnν} e–ph vertex | g_Luke |
| E y (ionization yield) | y_R, y_BCS, y_χ family | y_ion |
| E ε (1803.02903 pair energy) | ε dielectric family | ε_eh (same object, NOTATION §G) |
| E δ ≡ Δϵ/ϵ | δ off-shell distance | δ_coll |
| E r ≡ ϵ_NTL/ϵ_prim | r position family | r_coll |
| E r_c (capture radius) | c reserved for band subscripts; B2 r^{ion}_core | r_cap |
| E σ(u_car) (capture cross-section) | σ cross-section family (σ_N, σ̄_e, …) | σ_cap |
| E 𝔵, 𝔵_i (induced-charge mark) | B1 𝔵 molecular excited state | 𝔮, 𝔮_i |
| E m(r) (position-mean mark) | m masses | m_ind(r) |
| E E_x ≡ −N_XE_x^b (binding correction) | E_x exciton energy (§D) | ΔE_X^b |
Kept with ⚠: E_X (reservoir) vs E_x (exciton energy); 𝐌 vs 𝐌^{ph}; 𝔪 vs 𝔪_n.

## Rows added R14–R16 (2026-11-01, CW8-A merge; verified R14–R16 returns read through their errata)
Abbreviations: AUD = returns/R14/WP5-AUD.md; EF = returns/R16/GAP-EF-v2.md (+ errata); C2…C7 = returns/R16/CW2…CW7.md (+ CWn-errata, "E" suffix = errata only);
R = WP8-R-v2; U = WP8-U-v3; F = WP8-F-v3; MA = returns/R15/CMPMC-AUD.md; MD = returns/R16/CMPMC-DEV.md; CP = returns/R15/COMP-PAER.md. The "Clashes resolved" table at
the end lists every rename; returns are not edited, so a return's local name is read through it (owed renames → state/CORRECTIONS.md §19.16). Rows marked "local"
are used inside one section of one return only and are always cited with the return prefix (CONVENTIONS §14). Equation and check labels ((CW5-1), CW6-Kn, (E.1) …)
carry their return prefix and are not listed. Pending items applied in this pass: IF-R13-1 (§G rows 𝐍, N_trap, Y_H rewritten) and θ_X → θ_exc (WP7-E row).
| Symbol | Meaning | Source (local name) |
|---|---|---|
| **Cascade, yields, gap release (AUD, C5, EF, C7, R)** | | |
| κ_cal(r_coll) | (1 + r_collg_Luke y_ion)/(1 + r_collg_Luke); κ_cal ≡ κ_cal(1) | AUD (AUD-1) |
| r_g(t), r_g^{NR}, r_g^{ER}; P_g ≡ 1 − r_g | fraction of the created-pair gap energy still in E_pairs + E_X at t, r_g ≡ [E_pairs + E_X](t)/(N_ehE_g); released fraction (P_g as redefined by C5 (CW5-2)) | C5 (CW5-2)–(CW5-4); AUD "P_g" |
| 𝒢_gap ≡ E_g/ε_eh ⚠ | gap share of the pair energy (Si 0.312); ≠ 𝒢(q,ω) velocity kernel, 𝒢_GS, 𝒢₂^{2m}, 𝒢^{lat}_{00}, 𝒢^γ_OA | C5 (CW5-3); R |
| b_trap, γ_k^{gap}, w^g_k, P_k(t) | prompt-trap branch of a pair; decay rates of r_g; their weights (either sign); polynomial weights for degenerate γ_k | C5 (CW5-4) "w_k"; C5E §A17 |
| E_s ⚠, E_s^{(0)} | harmonic-mode energy of the quenched end state at t_pr; its zero-point value ω_s/2 per end-state mode (C5 OC-3 redefinition) (E_s ≠ E_st) | AUD B-1; C5 OC-3 |
| w_mem | k-memory weight Γ_E/(Γ_E + Γ_k) | C5 (CW5-1) |
| δ̃_ν, N_σ(E_F) | eigenphases of S_RS_L†; per-spin DOS at E_F | C5 (CW5-6) |
| S_pol(T) ⚠, W^{hop}_eff, W^{hop}_r | polaron exponent; dressed and electron-renormalised defect hopping | C5 §3.8 "W_eff, W_r" |
| b_br, τ_av, E_cut^{av}, U_rel, E_rel | trigger branching ratio; avalanche exponent and cutoff; relaxable elastic energy; energy of one release event | C5 §3.5, (CW5-9); C5E §C |
| 𝓔_X, p_rxn, ω_rxn, S_HR,rxn | energy per exciton (ionic targets); athermal reaction probability; reaction-mode frequency and HR factor | C5 (CW5-8), (CW5-11) "ε_X, p_R, ω_R, S_HR,R" |
| f_A, λ_trk, r_trk, D_amb | Auger loss fraction; track line density and radius; ambipolar diffusion constant | C5 (CW5-10) "λ_L, r₀, D_a" |
| θ_U, θ_τ, θ_H-E6, θ_exc | nuisances: M on U_rel; Δ on τ_av; detector-stage sufficiency; exciton/gap-release (WP7-E θ_X renamed) | C5 §4.2, §4.6; WP7-E-v3 §6 |
| X⁻, c_X | max(−X^{oth}_ER, 0); relative correction of the L38 bound | C5E (E.2) |
| γ_XX, t₀, D_X, L_X, N₀, λ₀ | exciton–exciton annihilation coefficient; bimolecular time scale (per channel); exciton diffusion constant and length (L_X = (D_X/γ_X)^{1/2}); initial pair number / line density of a track | C5E (E.3)–(E.6); C6 §3 |
| η_B,j | bound-exciton luminescence fraction | C5E §A17 |
| K^{lin}_x, K^{lin}_∞, ξ_ren, x_c, h_c, κ_ren, 𝔼, 𝔼_unit | lineage kernel at energy x and its scale-free limit; log decrement; cut energy; threshold-region functional; approach exponent; expectation (local to the renewal proof) | C5E §A12 "K_x, K_∞, ξ, κ" |
| K_q | per-q-bin defect-seed class weight π\|B\|²/η_pole − 2πIm(a*B) | C5E §A11 |
| 𝒜_ph | ABS/R&K phonon-to-ii rate constant (eV³; R&K "A") (𝒜 ≠ A_κ mass number) | EF §1 |
| λ_ph ≡ 𝒜_ph/E_g³, w_ph ≡ ω₀/E_g, θ_ii ≡ E_th^{ii}/E_g, a_DOS | reduced rate ratio, phonon/gap ratio, threshold ratio, DOS exponent (w_ph replaces v1's w₀, O4's X0 weight) | EF §1 |
| 𝔓_t ⚠ | three-body ii phase space ρ_t * ρ_t * ρ_t̄ (≠ 𝔓^{(n)} of C2) | EF §1 (v1 "Φ_t") |
| ρ_t ⚠, S_t ≡ ρ_ts_t, R_t(x), p_t(x), P_t | carrier DOS shape of type t (≠ ρ_T mass density); local to EF §1 | EF §1; EFE IF-EF5 |
| ℋ_<, ℋ_>, ℋ_i | residual heat below threshold; phonon heat above threshold (ℋ = ℋ_< + ℋ_>); heat of pair i in (R-iid) | EF §1.6 |
| 𝒱_<, 𝒱_> ⚠, 𝒞_<> ⚠ | normalised variances and covariance of F_eh = 𝒱_< + 𝒱_> + 2𝒞_<> (≠ 𝒱_a DM vertex, 𝒱_ν B2 vertex, 𝒞_m, 𝒞_adm) | EF (EF7) |
| r̄_c, σ_res (σ_res,e, σ_res,h), σ_pair² | mean and SD of the terminal residual per carrier; variance of the per-pair heat | EF §1.6 (v1 "σ_c, σ_h²") |
| F^{ren}, c₀, k₁, k₂, F^{ℋ} | renewal (final-state) Fano estimate; λ_ph → 0 limit of ε_eh/E_g; slope and offset of the linear form; Fano factor of a bare-heat estimator | EF (EF6), (EF6′), (EF13) |
| N_ii, ε^{cas}, f_cap^{e,h}, f_i, 𝟙^{cap}_i, f_X, p_diss, p_esc^X, f_imp | ii pair count; cascade pair energy; capture probabilities and indicator; exciton, dissociation, escape and impact-excitation fractions | EF §4 "κ_i, p_esc" |
| r_C ⚠, r_O, r₀ (local), ℓ_ε, T_car | Coulomb capture radius (≠ r_cap of WP7-E, related); Onsager radius; thermalisation distance; energy-relaxation length; carrier temperature | EF §4 "T_c" |
| 𝔊_t(x;z) ⚠ | probability generating function of the ii count of a carrier (≠ 𝔊_x(ϑ) branching functional, related) | C7 (CW7-153a) |
| λ^P_i, ϱ_−, ϱ, Δ_i, ΔP, θ_seedP | (P) leakage fraction; negative-part ratio sup_ω max([A_X+]_−, [A_X0]_−)/⟨A_tot⟩_i (C7E redefinition); absolute X+ ratio; bin width; P_X+ − P_X0; seeding nuisance | C7 §5 "λ_i"; C7E §1.5 |
| **Lattice, Migdal, disorder (C2)** | | |
| B_{κκ′}(ΔR) | static displacement correlation tensor (B_κ = B_{κκ}(0)) | C2 (CW2.2) |
| 𝔚^{(n)}(q), 𝔚^{(n)}_inc, 𝔚^{(n)}_dist | ω-integrated n-phonon weight; self and (glass) distinct parts | C2 (CW2.3), (CW2.12) |
| ℛ^{coh}_n(q) | exact rate-level coherence correction 𝔚/𝔚_inc − 1 (≠ ℛ physical rate) | C2 (CW2.4) "ℛ_n" |
| 𝔓^{(n)}(q,ω) ⚠, f_coh | momentum-resolved self n-phonon density; table coherence flag (≠ 𝔓_t of EF) | C2 (CW2.5) |
| 𝓂_k ⚠, ϱ_MK(ξ) | normalised ω-moments of S (≈ 𝔪_n moments of S^τ); Markov–Krein (Christoffel) mass at ξ | C2 (CW2.10)–(CW2.11) "ϱ(ξ)" |
| B_L(r), B_T(r), b^{pr}, τ^{pr} | longitudinal/transverse glass pair correlations; longitudinal–transverse vector and traceless transverse part of B_IJ about r̂_IJ | C2 (CW2.12); C2E (CW2.12′) "b, τ" |
| Φ^{on}_κ, Φ^{el}_{κκ}(ω) | on-site force constant; dynamical electronic on-site force constant | C2 (CW2.13)–(CW2.14) |
| σ_κ(Δ), ℐ_k, ψ⁽¹⁾, ψ⁽²⁾ | force-operator spectral measure; its inverse moments; first/second Sternheimer functions | C2 (CW2.14)–(CW2.15) |
| α₂ | ω² coefficient of the proper cell polarisability | C2 (CW2.19) |
| 𝒮^{(ν)}_Z(k), ŵ_ν ⚠ | Born-charge structure factor; branch mode fraction c_ν⁻³/Σc⁻³ at fixed ω (replaces C2's ŵ^{pol}_ν; ≠ w^{pol}_ν of F) | C2 (CW2.20); C2E (CW2.20′) |
| δ^M_I, 𝒢^{lat}_{00}(ω), κ^M_1, h_iso(ω) | isotope mass defect; host on-site lattice Green function; isotope correlation coefficient; its spectral function | C2 (CW2.21)–(CW2.22) |
| R_slab, P_wall | thickness-averaged reflectance 2R/(1+R); reflected-flux pressure | C2 (CW2.25) |
| 𝒲_G(k), δc̃_κ | Umklapp vertex of the non-mass-proportional coupling; per-mass remainder | C2 (CW2.26) |
| M_{λλ′}, b^{ch}_λ, 𝒩_χ, 𝒞_chi | cascade daughter matrix; chiral-stable probability; expected chiral count; chiral-stable terminal set | C2 (CW2.27); C2E (CW2.27′) "b_λ, 𝒞" |
| Γ^{u}, Γ^{iso}, Γ^{loss}, Γ^{all} | unordered-pair 3-phonon, Tamura, loss and total rates | C2E (CW2.27′) |
| 𝓃̂_G | Fourier coefficient of the crystal electron density Ω⁻¹∫_Ω e^{−iG·r}n_e; 𝓃̂_0 = 𝓃_e (≠ 𝓃^{(κ)}_G conditional density) | C2E E-14 |
| ρ^{nuc}_κ, R^{nuc}_κ | normalised nuclear charge distribution; its uniform-sphere radius √(5/3)r_rms | C2E E-6 |
| P^{gd}, 𝒜^{O}_{Qν}, B^q_k | ground-doublet projector; one-phonon giant-moment amplitude; Stevens CF parameters | C2E (CW2.28) "P_g" |
| **Architecture, Fano, basis, WP7-D extensions (C3)** | | |
| c_b^F, c̄^F, K_b, 𝔉_b (b ∈ {ν, x}) | Fano coefficient normalised with Γ^{tot}; first-emission branching incl. the non-phonon branch x (K_ν is the WP5 class weight); rate-unit Fano term | C3 (CW3.1); §C row updated |
| Θ_PT | antiunitary PT; Θ_PT² = (−1)^{N_e} on the N-electron sector (≠ Heaviside Θ) | C3 §2.2 "Θ" |
| δ_Λ₀ | off-shell scale of seed Λ₀ (min of edge distance, valley threshold, JDOS scale) | C3 §2.3 |
| 𝔳²_s(q) ⚠ | velocity-square density row, ⟨k′\|𝔳²\|k⟩ = (k+k′)²/4m_s² (17th basis row; ≠ 𝔳_κ B2 absorption vertices) | C3 (CW3.2) |
| 𝒮_st(k) | all-electron static structure factor ⟨n_e(k)n_e(−k)⟩/N_e | C3 (CW3.3) |
| Z^{(e)}_κ(q) | electron-following charge (tensor); q → 0: Z_κ𝟙 − Z*_κ | C3 (CW3.4) |
| 𝒢_GS(q), Ω_{P,e} | GS lattice part of the electron-only static step; Ω²_{P,e} = e²𝓃_e²/ρ_T | C3 (CW3.4) |
| GS-m, X-m, 𝒬^{D-m}_n, U^{sl}_b, N̂_hyb | Theorem D-m sectors; symplectic magnon–phonon normal-mode map; hybrid-quanta number | C3 §1.3 "U_b" |
| α̃(ω), N_D, Λ_D | running Dirac fine-structure constant (α̃₀ its bare value); number of four-component nodes (≠ 𝓃_D); band cutoff | C3 §1.5; C3E §1.7 |
| O^{CC}_F, O^{CC}_{GT}, F_Fermi(Z,E) | charged-current nuclear rows; Fermi function | C3 §4.1 "F(Z,E)" |
| H_sg | NR ALP–photon seagull −(eg_aee/2m_e²)(∂_ta)σ·A | C3 §4.9 |
| (P5), η^{ls}_ij, Υ^{PV} | scalar O(g²) level-shift matrix on D(Λ₀); 2(e_i − e_j)/(γ_i + γ_j); principal-value part of the off-shell self-energy Υ | C3E §1.2–§1.3 "η_ij" |
| 𝔥^c_off, M^c(k), M^{FM}(k), (G5′-c), (M5) | connected off-diagonal norm; connected and Fan–Migdal zeroth-moment band matrices; connected (G5′); positive-definite quadratic spin–lattice form | C3E §1.1, §1.6 |
| 𝒯^{thr}_K | threshold set of the fibre Hamiltonian H_K (≠ 𝒯_e, 𝒯^{(2)}) | C3E §1.13 "𝒯_K" |
| **Spin, SC, Dirac, low-dimensional, QD (C4)** | | |
| 𝔳_GRPA(q,ω) ⚠ | GRPA vertex fraction Im[R̃^{GRPA} − Π^N₃₃]/Im Π^N₃₃ | C4 (1.1) |
| M^N_i | Nambu pair-creation amplitude ⟨+,ξ′\|τ^N_i\|−,ξ⟩ | C4 §1, §12 "M_i" |
| P_Δ(Δ; r) | local-gap distribution from BdG | C4 (2.1) |
| Γ^{(4m)}_q, 𝒢^{2m}₂ | two-magnon quartic vertex; free two-magnon propagator | C4 (3.1) "𝒢₂" |
| 𝒢^γ_OA(q,ω) | full-q antisymmetric current response (γ_OA its slope) | C4 §4 |
| γ^{FI}_{ij} | one-body transition density matrix of embedded multiplets | C4 (5.1) |
| Ry_D | massive-Dirac exciton Rydberg Δ_D(α̃/g_deg)²/4 | C4 (6.1) |
| ⟨j_K(q)⟩, 𝒞^{(ℓ,J)}_{KK′} | radial form-factor integrals; multiplet reduction coefficients | C4 (7.1) |
| 𝔯_ε, δ_𝔰 | Im ε^{nor}/Re ε^{nor}; KK screening shift relative to Re ε^{nor} | C4 (8.1) "𝔯" |
| J_F, R_dd, 𝐝_tr | Förster coupling, inter-dot distance, transition dipole | C4 (15.1) "𝐝" |
| θ_CT, t_CT, S_HL, f_C | Frenkel–CT mixing angle, transfer integral, HOMO–LUMO overlap, CT form factor | C4 (16.1) |
| R̃_1D,n, Δ_n, V_1D, R_tube, ε_1D, β_2p | 1D subband bubble, subband half-gap, tube Coulomb kernel (2αI₀K₀), radius, 1D dielectric function; Slater exponent of C 2p (≠ ζ_S) | C4 (17.1) |
| p^W_0, W_𝒲, 𝔯_W | one-body site-0 Wannier projector; bandwidth of the Wannierised manifold; DFPT/(H_W) ratio | C4 §19 |
| A^{sw}, B^{sw}, ω_E, ω_A, ω_AFMR, n_pair | k = 0 LSWT coefficients; exchange, anisotropy and AFMR frequencies; AFM pairs per cell | C4 (20.1) |
| (H_iso), S_∥, S_⊥, cos θ_qm | uniaxial-tensor hypothesis, its components; q̂·m̂ | C4 §21 "c" |
| **Transport, collection, phonon readout (C6, R, MA, MD)** | | |
| 𝒦_s(f; r_ev) | collection kernel of sensor s (energy delivered per unit birth energy at f, r_ev) | C6 (CW6-1) |
| ζ_O, ζ_gap, θ_ζ, θ_ζg, θ_pos, θ_Ssurf, S_surf | NTL/primary and gap/primary contrasts (a_pop oriented: lower-gap film share or NTL-enriched channel); their nuisances; surface recombination velocity | C6 §2–§3, §9; C6E A4 |
| π_ℓ(r, t), s_ℓ(f) | gap-release flux per channel ℓ; its emitted spectrum | C6 §3 |
| f_m ≡ f_*(t_mem), Δ_soft, τ_h, Δũ | memory frequency; soft-born NR/ER difference; hard-part TV distance; birth-spectrum difference | C6 (CW6-2), C6E (CW6-2′) |
| δ_coll^{prim}, δ_coll^{gap}, δ_coll^{pos}, δ_coll^{esc}, ρ_g ≡ ϵ_gap/ϵ_hard, ϵ_soft, ϵ_hard, ϵ_gap, x_ER, x_NR | parts of δ_coll; gap/hard collection ratio; released gap fractions | C6 (CW6-3), C6E A6; R §6 "δ_prim" |
| ξ_SC, n^{tr}_s, ρ_tr | space-charge nonlinearity; trapped areal and volume charge densities | C6 §6 "n_s" |
| σ_ph-ion,j, σ_ii,j | phonon-ionisation and impact-ionisation cross-sections of trap j | C6 §6 |
| P_abs(θ), a_opt, t̄_esc, t̄_{12}, τ_l, Σ_c ≡ c_L⁻² + 2c_T⁻², θ_esc^{film} | film absorption per entry; in-film optical depth; flux+mode-averaged transmission; film loss time (1401.1937's τ_l adopted); reciprocity weight; RG7 nuisance | C6 (CW6-4), §7 "a, Σ"; C6E OC-CW6-7 |
| t^{AMM}_{P,SV,SH}(θ), t_AMM(ν, θ), t_DMM, Z_ac, 𝔯_ac | AMM coefficients per mode and angle (substrate→film, energy flux); DMM transmission; acoustic impedance; AMM ratio | R §3.2 "Z, 𝔯"; MD |
| f, f_*(t), f_b, f_eq, f_D ≡ ω_D/2π, 𝒜_anh ⚠, 𝒜_iso ⚠, x_L, N_mix, r_rms, t_mem, ℓ_mem, f_s | phonon frequency and its decay scale; anharmonic and isotope rate constants (≠ bare 𝒜 halo index); L fraction; mixing events; rms spread; memory time/length; ER soft fraction | R §2 (v1 rows, LE-164) |
| O_obs, a_pop, φ_pop, σ_pos, σ_Nph, σ_ph, 𝒮_sep, 𝒮_int, 𝒮_b, O_b, Δφ_L, Δφ_gap, Δf_g | observable; channel and energy fractions; spreads; separations (v1 𝔖, 𝔖_int; 𝔖 is the Ward generator); two-window observable; NR/ER energy-fraction differences | R "O, 𝔖" |
| A_iso, Γ_md | Tamura/Klemens isotope rate constant A_iso = Γ_mdΩ⟨c⁻³⟩/(4π) (s³); mass-defect coefficient (2408.04732 Eq. (5)); CMPMC's B = (2π)⁴A_iso | C6 §8; MA |
| 𝔐_c, ℓ₀, ϱ_LT, Γ_Luke, p_spec, p_diff, p_anh, f_dk | carrier Mach number k/k_s (≠ 𝔐 Migdal-regime slot); carrier–acoustic-phonon length πħ⁴ρ/(2m³Ξ²); v_L/v_T; Luke emission rate (v_L/3ℓ₀)(𝔐_c − 1)³/𝔐_c; surface branching probabilities; per-step wavevector-change bound | MA "𝔐" |
| E^{coll}_rel, I(Ω) | energy a collected carrier releases at the contact, E_kin + (E_c − μ_F) (e⁻) or E_kin + (μ_F − E_v) (h⁺); pair-breaking integral, 1/τ_pb = I/(πΔτ₀^φ) | MD "E_rel" |
| **Uncertainty, FOM, materials (C7, F, U)** | | |
| 𝔎_i(w) | stream kernel: bin-i count of a unit-density stream at velocity w | C7 (3.1) |
| F_w, 𝔹_v, Φ_ℓ, φ_ℓ, Φ_max, λ^{dual}_i, N_i^{up}, N_b, 𝒞_R, R*_v, g_test | halo measure on the velocity ball; bounded functional and weight; maximum; dual weights; upper counts; number of bins; cone of admissible Radon data; back-projection; test function (local to C7 §3) | C7 §3 "F, B, Φ, φ, λ_i, 𝒞, R*, g" |
| O_φ, Γ_φ (scalar), FOM_φ | scalar target operator n_e − 𝒯_e; scalar absorption rate; per-mass FOM | C7 §6 |
| ΔS ⚠, r_2m, W_⊥, W_∥, r^M_mag | zero-point spin reduction (≠ ΔS_coh); two-/one-magnon local weight ratio; local weights; residual magnon M width ΔS/S (an r^M_k of §E); ✎R17: [D] as the transverse sum-rule defect, [E] (lower estimate) as the one-magnon width (WP8-errata §9) | C7 §7; C7E §1.7 "r^M" |
| θ_mag, θ_Fmag, θ_BCS, σ_BCS(y), y_mask | magnon, form-factor and SC nuisances (θ_SC is WP7-E's); SC one-sided width; SC mask boundary (KK-∞ column, threshold 0.3): 3.8 | C7 §7–§8; C7E §1.8 |
| K^{lm}_ν(m_χ) | ∫_{q₋}^{q₊}(dq/q)η(v_min(q, ω_Lν)), per-branch light-mediator weight (K_ν is the WP5 class weight) | C7E §1.2; F "K_ν" |
| c_NR1, c_LA,max | ⟨Σ_ν(q̂·ê_ν)²/c_ν(q̂)⟩⁻¹ (heavy-mediator NR-1ph speed); largest LA phase speed | U §4.1′; F (2.3a″) |
| w_iso, P_κ | SD isotope weight (4/3)((J+1)/J)[a_p⟨S_p⟩ + a_n⟨S_n⟩]²; nuclear polarisation (the §C P_κ row) | C7E §1.12; F §7 |
| 𝒦^{kin,(0)}_a, 𝒦^{kin,(2)}_a | kinematic factors qF²η/(4π²), qF²ξ/(4π²) (≠ 𝒦_c cascade kernels) | F "𝒦_a" |
| ℛ, 𝓡_a, C_χ | physical rate per target mass and time; material functional at fixed \|𝒱_a(q₀)\|²; flux factor ρ_χπ/(m_χμ_χe²), ℛ = C_χσ̄𝓡_a | F |
| 𝓠_Mig,κ(ω) | Z_κ(k)²-weighted ω⁻⁴ ELF moment ∫d³k Z_κ(k)²L(k,ω)/(3(2π)³ω⁴) | F "𝓜_Mig" (≠ 𝓜¹_ab) |
| 𝓈_λ, w^{pol}_ν ⚠ | Σ_jλ_{S,j}²\|𝐒_j\|/Ω (≠ 𝓃_s); per-branch weight of 1/ε_∞ − 1/ε₀ (R13 "Δ_ν"; ≠ ŵ_ν of C2) | F "𝓃_S, Δ_ν" |
| ω̄_κ, D_sw, v_θ | ⟨ω⁻¹⟩⁻¹ of D_κ; FM spin-wave stiffness; AFM magnon speed | F "𝔇_sw" |
| 𝓡_a, 𝓩_0, 𝓩_B, 𝓻_s, 𝓻̂_s, b_bg, ϵ_cut, f_sys, ΔE_ROI, δ_rank, 𝓘_pol, Δ_mag, ω_max^{mag,ph}, m_min^{ac}, Δm_PAER/m, w_acc, 𝓟_* | WP8-F rate functional, reach scalars, background, systematics, ranking tolerance, polar integral, magnetic gap, edges, acceptance, LEE proxies | R13 WP8-F (IF-F6), kept in F |
| T_D, τ_life, g_iso, ω_p^{val}, s_spin ≡ S_cell/Ω, c₁^{spin}, ω_Γ,max^{DFT}, a(²¹⁰Pb), 𝓇^{int}_{<1}, 𝓇^{cos}_{<1} | Debye temperature (θ_k is the nuisance family); source lifetime; isotope pair term; valence plasma frequency; net spin density; source-only coupling; max Γ mode; ²¹⁰Pb specific activity; intrinsic and cosmogenic sub-keV rates | U §8 "θ_D, τ_ph, g₂^iso, ħω_p, 𝓃_spin, c₁" |
| **PAER computation (CP)** | | |
| ℱ_ρ(q), f_win(q,ω), α_abs(ω), n(ω) | finite-q form-factor proxy ⟨Σ\|ρ_cv(Γ,q)\|²/q²⟩ normalised to q → 0; fraction of q̂ in the window; measured absorption coefficient; refractive index | CP "𝔉_ρ" |
| m_χ^{PA}, m_χ^{ZP} | PAER edge mass; first zero-phonon mass | CP; WP3 §M9 |
| LIMITS labels L39–L46, L-EF1…5, CW2-L1…5, CW4-a…g, CW6-L1…6, L-H1…4, L-F1…4, LU2′, LU4′, LU5′, LT1–3, CMPMC-AUD-L1…5, CMPMC-DEV-L1…4, L8-N1, L8-N2, L9-N1, L-D10′, L-D11′, L-D13, L17′, L-O2, L-Fano, L9b′, R1-L17 | LIMITS "R14–R16" rows (CONVENTIONS §13 row 30) | LIMITS |

**Clashes resolved (R14–R16).**
| Return symbol (meaning) | Clashes with | Resolved name |
|---|---|---|
| WP7-E-v3 θ_X (exciton nuisance) | WP6-v2 local θ_X (= θ_exch) | θ_exc |
| C2E P_g (ground-doublet projector) | AUD/C5 P_g (gap-energy release fraction) | P^{gd} (P_g kept for 1 − r_g) |
| C7E/F K_ν(m_χ) (light-mediator weight) | WP5/C3 K_ν, K_b (Fano class weight) | K^{lm}_ν |
| C5E K_x, K_∞ (lineage kernel) | C3 K_x (non-phonon branch weight) | K^{lin}_x, K^{lin}_∞ |
| C5E ξ, κ (renewal proof) | ξ(v_min) halo integral; κ species index | ξ_ren, κ_ren |
| C4 𝔯 (Im ε/Re ε); R 𝔯 (AMM ratio) | C2 𝔯_κ, C4 𝔯_W | 𝔯_ε; 𝔯_ac |
| MA 𝔐 (carrier Mach number) | 𝔐 ∈ {ad, sud} (τ slot, CONVENTIONS §11) | 𝔐_c |
| C2E b, τ (pair tensors) | b phonon operator; τ truncation multi-index | b^{pr}, τ^{pr} |
| C2 b_λ, 𝒞 (chiral cascade) | b phonon operator; 𝒞_adm, 𝒞_<> | b^{ch}_λ, 𝒞_chi |
| C2 ℛ_n (coherence correction) | ℛ physical rate (F) | ℛ^{coh}_n |
| C2 ϱ(ξ) (Markov–Krein mass) | ϱ_−, ϱ (C7); ϱ_⊥ (WP7-B1) | ϱ_MK(ξ) |
| C3 Θ (PT) | Θ Heaviside step | Θ_PT |
| C3 U_b (symplectic map) | U^B Bogoliubov, U_qp | U^{sl}_b |
| C3 F(Z,E) (Fermi function) | F_DM, Fano F family | F_Fermi(Z,E) |
| C3E η_ij (level-shift ratio) | η(v_min), η_pb, η_pole | η^{ls}_ij |
| C3E 𝒯_K (threshold set) | 𝒯_e, 𝒯^{(2)} | 𝒯^{thr}_K |
| C4 M_i (Nambu amplitude) | M_κ masses, M^{(2)} | M^N_i |
| C4 𝐝 (transition dipole) | d dimension, d_tun, d_film | 𝐝_tr |
| C4 c ≡ q̂·m̂; u, v | c band subscript only (CONVENTIONS §4, §13 item 9); v DM velocity | cos θ_qm; u^B_k, v^B_k |
| C5 w_k (r_g weights) | w_κ one-phonon measure | w^g_k |
| C5 ε_X (energy per exciton) | ε dielectric family; E_X reservoir, E_x exciton energy | 𝓔_X |
| C5 λ_L, r₀, D_a (track) | ω_L, λ_ph; EF r₀ (thermalisation distance) | λ_trk, r_trk, D_amb |
| C5 p_R, ω_R, S_HR,R (reaction) | E_R recoil energy | p_rxn, ω_rxn, S_HR,rxn |
| C5 W_eff, W_r (hopping) | W_κ (Debye–Waller), W_Lam | W^{hop}_eff, W^{hop}_r |
| MD E_rel (contact release) | C5 E_rel (TLS/LEE release event) | E^{coll}_rel (C5 keeps E_rel) |
| C6/R Σ, Z | Σ self-energy; Z_κ, Z*_κ | Σ_c, Z_ac |
| C6 a (optical depth) and a (channel fraction) | each other; a_lat | a_opt; a_pop (R's name) |
| C6 n_s (trapped areal charge) | 𝓃_s species density | n^{tr}_s |
| C7 F, B, Φ, φ, g, 𝒞, R*, λ_i (LE-152) | F_DM/Fano F; B_κ; Φ force constants; g e–ph vertex; 𝒞_adm; λ_ph and λ^P_i | F_w, 𝔹_v, Φ_ℓ, φ_ℓ, g_test, 𝒞_R, R*_v, λ^{dual}_i |
| C7 λ_i (LE-154 leakage) | λ^{dual}_i; λ_ph; λ exciton index | λ^P_i |
| C7E/F r^M (magnon width) | r^M_k (M-type ratio row, §E) | r^M_mag (an instance of r^M_k) |
| F 𝔇_sw (FM stiffness) | 𝔇 DM-tensor family | D_sw |
| EF T_c, κ_i, p_esc | T_c critical temperature; κ species; WP7-B2 p_esc | T_car, 𝟙^{cap}_i, p_esc^X |
| CP 𝔉_ρ (form-factor proxy) | 𝔉 Fano term | ℱ_ρ |
| MA/MD LIMITS AUD-L, DEV-L | WP5-AUD labels AUD-n, IF-AUD-n | CMPMC-AUD-L, CMPMC-DEV-L (and "CMPMC-AUD IF-AUD-n" vs "WP5-AUD IF-AUD-n") |
| EF v1 LIMITS L39–L43 | WP8-R L39–L42 | L-EF1…L-EF5 |
| LIMITS L17 (R1 table) | LIMITS L17 (v3 bounds table) | R1-L17 |
Kept with ⚠ (distinct names under the decorator rule, but easy to confuse): 𝒢_gap vs 𝒢(q,ω), 𝒢_GS, 𝒢^{2m}₂, 𝒢^{lat}_{00}; 𝔓_t vs 𝔓^{(n)}; ŵ_ν vs w^{pol}_ν; ρ_t vs ρ_T; 𝒱_≶ vs 𝒱_a, 𝒱_ν;
𝒞_<> vs 𝒞_chi, 𝒞_R, 𝒞_adm; E_s vs E_st; r_C vs r_cap; 𝓂_k vs 𝔪_n; ΔS vs ΔS_coh; 𝔳²_s and 𝔳_GRPA vs 𝔳_κ; 𝔊_t vs 𝔊_x; S_pol vs S_HR,k; D_X (exciton) vs D_diff (carrier), D_amb.
Same object, one row: D_X (C5E and C6); P_κ (WP2 polarisation, F nuclear polarisation); A_iso (C6) and CMPMC's B (factor (2π)⁴); t_esc → t̄_esc (C6 replaces the phenomenological t_esc).

## Rows added R17 (2026-11-01, CW8-B; returns/R13/WP5-v4.md "Symbols introduced/used", R13 and R8 tables, read with returns/R14/WP5-AUD.md and returns/R16/CW5-errata.md)
LE-164 remainder. Every symbol of the two WP5-v4 "Introduced here" tables (R13 and R8) that had no NOTATION row is entered below, or mapped to an existing row in the
clash table. The v3 "used as defined" and "Introduced in v2" lists were spot-checked: x′_j, E_car, h_LZ, ω_bar, Γ_att, ℛ_rel, E_slope, a₀, n_B, q_c, 𝓜¹ (§M, §D) are present.
Labels ((W4′), (W11′), K1–K17, IF-R13-n, WP5v4-Cn, WP5-cp1–cp3, (H-t), (H-m), (B2a), (B2b), (R-k′), (r1)–(r3), IF-R8-n) carry the WP5 prefix (CONVENTIONS §14)
and are not listed.
| Symbol | Meaning | Source (local name) |
|---|---|---|
| 𝒦_cap ⚠ | prompt (t < t_pr) capture kernel onto trap level j: cascade capture for shallow levels, multiphonon for deep levels (WP7-E-v3 (E9) at t < t_pr) (≠ 𝒦_c, cascade kernel of channel c) | WP5-v4 §1.2 (A-1); WP7-E-v3 |
| 𝔱 = tr_j, 𝔱 = pl | values of the cascade type 𝔱 (row §M): "trapped on level j"; undamped plasmon pole as a final state (metals, q < q_c; CONVENTIONS §13 item 21) | WP5-v4 §1.2 (A-1); §1.1(a), §5 |
| Γ_pl | damping rate of the 𝔱 = pl final state | WP5-v4 §1.1(a), §5 |
| ℋ_eff | effective heat of (W14): ℋ + E_trap^{pr} + E_es + E_pairs^{unp} + ΔE_X^b − 𝒲_bias(t_pr) (WP5-v4 (W4′); equivalently ω − N_ehE_g − E_st − E_esc, GAP-EF-v2 (EF13)) | WP5-v4 (W4′), §6.4 (A-10) |
| R_final^{min}, 𝔅₀^{min} | quenched (basin-minimum) end and start configurations of the E_st definition (WP5-AUD §3.1 protocol, IF-R13-3) | WP5-v4 §3.2 ([v4] reading); WP5-AUD |
| P(𝐌, t\|Λ) | marked observable law (WP7-E-v3 (E3)) used in (W6); WP0-v3 (7.3) is its t = t_pr marginal | WP5-v4 (W6) (A-16) |
| Γ^{out}_{nk}, Γ^{in}_{nk} | carrier out- and in-scattering rates; 2\|ImΣ\| = Γ^{out} + Γ^{in} (W16); the cascade rate (W1) is Γ^{out} | WP5-v4 (W1), (W16) |
| α_E ⚠ | Ewald (range-separation) parameter of g^L (≠ α, α²F, α_ohm) | WP5-v4 §1.1(c) |
| 𝓃_pair | local e–h pair density of a track ((B2) condition; 3×10²⁰ cm⁻³ quoted) | WP5-v4 §1.2 (B2) "n_pair" (renamed: n_pair is the C4 AFM-pair count) |
| ℋ_nuc | heat delivered to atomic motion through the ion branch (Lindhard's ν without the electronic sub-cascade); L20 observable ν = ℋ_nuc + E_st | WP5-v4 §6.1; WP7-E-v3; CW5 |
| U_FP, U_EDFT | source-only (2209.04503): Frenkel-pair and inner-shell parts of U_bind (§K rule: quote, never use) | WP5-v4 §6.1 |
| 𝓜⁰_GS, 𝓜¹_GS, 𝓜¹_X ⚠ | zeroth and first energy moments per nucleus of the GS and X sectors (𝓜⁰_GS = 1 − P_Mig, 𝓜¹_GS = (1 − P_Mig)q²/2M_κ − E^{Mig}_1, IF-R8-1) (sector-resolved κκ moments; ≠ the moment matrices 𝓜¹_ab) | WP5-v4 §3.1 |
| F_loss ⚠ | renewal loss law of the (W14) asymptotics (hypotheses (r1)–(r3)) (≠ the Fano family F_eh, F_NR, F_qp, F_meas) | WP5-v4 §6.4; CW5 §2.7 |
| θ_Z, θ_dense | WP5 nuisances: quasiparticle residue (0.8–1, global); (B2) violation [C] (IF-R8-6, WP6-v3 IF6-16) | WP5-v4 §8 |
**Clashes resolved / read-through (returns not edited; owed renames → state/CORRECTIONS.md §19.5):**
| Return symbol | Collides with / same as | Read as |
|---|---|---|
| WP5-v4 n_pair (track pair density) | C4 n_pair (AFM pairs per cell, row "Rows added R14–R16") | 𝓃_pair |
| WP5-v4 a_X (exciton Bohr radius) | §D a_x (exciton radius; same object) | a_x |
| WP5-v4 W_{GG′} ((W1′), right index ε⁻¹_{GG′}v_C(p+G′)) | §D W^{scr}_{GG′} (same object in G-space at the RPA kernel f_Hxc = v_C; WP5-v4 says "= W^{scr} in G-space") | W^{scr}_{GG′}, index order as (W1′) |
| WP5-v4 Z_qp (normal-state carrier residue) | §M Z_qp (Theorem D-g QP residue; WP5-v4 flags the dual use) | Z_qp (same object: the QP residue of the reference used) |
| WP5-v4 c_ν^F | §E row 𝔉_{Λ₀,b}, c_b^F (dimensionless; R16 form supersedes (W17)'s Γ_Λ₀ normalisation, IF-R8-4) | c_b^F with b = ν |
Kept with ⚠: 𝒦_cap vs 𝒦_c; α_E vs α, α_ohm; 𝓜⁰_GS/𝓜¹_GS/𝓜¹_X vs 𝓜¹_ab; F_loss vs F_eh, F_meas.

## Rows added R17 (CW8-FINAL, 2026-11-01; returns/R16/CW1.md and CW1-errata.md "Symbols", returns/R17/WP8-errata.md §17.2 as corrected by referees/R17/VER-ERR-WP8.md C6)
Collision check: every symbol below was grepped in this file before entry (0 hits each; ϖ_II, the WP1 pointwise ratio, already exists and is kept distinct from ϖ̄_II).
GAP-EF-v3's h, n_w, w_eff, θ_eff, δ, p, x₀ are return-local (GAP-EF-v3 "Symbols") and are not entered; its ω₀,eff is the WP8 row below.
| Symbol | Meaning | Source |
|---|---|---|
| ϑ_ZP | tilt of q̂ from the valley axis at the [E13] optimum (Si: 0.181 rad, {001} plane) | CW1 §1 |
| β^{ZP}_θ, β^{ZP}_z | in-plane / out-of-plane angular curvatures of E^{ZP}_min at the optimum (eV/rad²) | CW1 §3 |
| β^{ZP}_2(α) | angular curvature of the second heavy-hole pair energy at the on-axis edge, azimuth α (4.51, 2.12, 1.07 eV/rad² at α = 0, π/8, π/4) | CW1-errata E-7(c) |
| ϖ̄_II | angle-averaged forbidden-class ZPL/PAER ratio at fixed \|q\| ((CW1.4), superseded in value by (CW1.4′)); ≠ ϖ_II (WP1 pointwise) | CW1 §3; CW1-errata E-7 |
| ε_ex^{max}(m_χ) | largest reachable excess energy above E_min at the optimum \|q\| (slight underestimate at fixed m_χ, CW1-C51) | CW1 §3.3 |
| ε_touch | excess energy at which adjacent {001} cones touch, ϑ_ZP²β_θβ_z/(β_θ + β_z) (Si 0.049 eV) | CW1-errata E-7(a) |
| ∂_{q_z}ρ\|_rel | relaxed-pair (centre-of-mass) q coefficient of the second-class vertex out of the mirror plane (1.57 Å; CW1's \|∂_{q_z}ρ\| = 1.38 Å was at fixed k_v) | CW1-errata E-7(b) |
| ς_n | σ_z glide parity of a Bloch state with reduced-zone k in the plane: eigenvalue ς_n e^{−ik·T/2}, T = (a/2, a/2, 0) | CW1-errata E-8 |
| δ_LF^{jT}, δ_LF^{(0)} | LFE correction of the transverse current (CW1.12); vertex-level proxy of δ_LF (CW1.19) | CW1 §12, §19 |
| ΔZPR_n | non-adiabatic minus adiabatic Fan ZPR of band n (CW1.25) | CW1 §25 |
| B_pl^{X+} | plasmon phonon-assisted branching (CW1.14) | CW1 §14 |
| m_ZPL (COMP-PH) | ≡ m_χ^{ZP} (continuum); use m_χ^{ZP} | CW1 "Symbols" note |
| L, M, N (Dresselhaus) | named constants of CW1 §1.3/§6 only, not symbols (L, M, N keep their meanings elsewhere) | CW1 "Symbols" note |
| r^M_mag (status note on the R14–R16 row) | [D] as the LSWT transverse sum-rule defect ΔS/S; [E] (lower estimate) as the one-magnon width | WP8-errata §9 |
| κ_η | (u₊/η₀)∫₀^{u₊}(η₀ − η(u))u⁻²du, light-mediator first-order constant; 3.14 for the CONVENTIONS §8 SHM | WP8-errata (EW-7.1) |
| m_on, m_hi, W_AB | heavy-mediator 1/c 10% onset (per material, normalised to I₀ = ∫₀^{v_max}u²η du: 4.7–5.7 m_min^{ac}(c); against Si ≈ 4.2 m_min^{ac} of the softer material); upper end m_hi = q_BZ/(2v_max); pairwise window W_AB = the contiguous m_χ range, capped at min(m_hi,A, m_hi,B), where \|(R_A/R_B)(c_A/c_B) − 1\| < 0.1 | WP8-errata §6 + VER-ERR-WP8 C6 |
| Z_prim | formula units per primitive cell (q_BZ,prim = q_BZ,fu/Z_prim^{1/3}) | WP8-errata §6 |
| P₁, P(A ≻ B), rank_68, tier, X_pole | as WP8-S-v2 "Symbols"; tier = height in the interval order (correlation-blind); X_pole = plasmon-pole prior of 𝓠_Mig ([1, 3], a prior, not a bound) | WP8-S-v2; WP8-errata §14 |
| ω₀,eff | h·round(ω₀/h), the phonon step a non-commensurate cascade grid actually uses | WP8-errata §5; GAP-EF-v3 |
| ν_CsI | Poisson-ratio band of the CsI B-floor model, U[0.20, 0.35] around the Cauchy 1/4 [E] | WP8-errata §4 |
