# SEAM: E.22–E.24 (computational specifications: defects and two-level systems; nuclear-recoil partition and charge yield; electron cascades)

Files: tex/appE/E-22.tex, E-23.tex, E-24.tex (each with a summary table). Inputs added to tex/appE/appE.tex after E-17 with
`\setcounter{section}{21}`. Sources: sources/E-g/{2303.02196, 2405.10405, 2610.16949, 1910.11168}.txt; sources/E.10/2009.03804.txt;
sources/C-c/1806.11002.txt. No App. D file. No figure.

## The reader now knows
- E.22: α_ohm by two routes (KKR eigenphases of S_RS_L† in a midpoint basis; supercell orthogonality slope −d ln|⟨Ψ_L|Ψ_R⟩|/d ln L = α_ohm,
  derived from eq:E.10-ohm); l-diagonal form π⁻²Σ(2l+1)δ̃_l² only for reorientations; Born limit 4K_b; Al resonator fits K_b = 0.07, 0.11
  (maillet2023, single-spin DOS) → α_ohm 0.28, 0.44; spin-counting and smearing pitfalls; W 250-atom memory ≈ 7 GB per k.
- E.22: Huang–Rhys S_HR,k = ω_kΔQ_k²/2 and E_reorg (eq:E.22-SHR); weak/strong coupling; λ_tun; release verdict ln(Γ_0 t_obs) = 47.2 → λ_tun ≤ 23.6;
  two-parabola Si estimate 27.5 (V = 0.1 eV, d = 1.5 Å, illustrative inputs); 64-atom pilot (384 SCFs per Hessian, ≈ 120 core-h); release-path
  sum rule as acceptance; shared configurational table with E.23; Poisson tail for carrier-driven reactions.
- E.22: crowdion in W: Peierls profile (meV atomistic, µeV FK; fitzgerald2018), S_pol(T) (eq:E.22-Spol) with S_pol(0) = 𝒥₃ω_D²/2π and
  thermal part π𝒥₃T²/3 (derived); noise < 0.1 meV/cell; Al dumbbell glide.
- E.22: f_TLS(q) (eq:E.22-fTLS); two-SCF method vs DFPT at Γ; 216-atom a-SiO₂, 80 Ry, memory 2.5 GB; small-q long-range part added
  analytically; never rebuild from Born charges.
- E.22: TLS ensemble: khomenko2020 (≈10³ active TLS from ≈10⁶ minima; TLS density falls 100× with stability); acoustic-loss control
  (phillips1987); preparation pitfall.
- E.23: Massey parameter ξ_M ≈ 15 at 20 eV, ≈ 2 at 1 keV (derived); TDDFT kernel spec; partition tables; Wigner-initial-state reference
  error 31 meV/atom = 126 eV per 4096 atoms (from 5.3's 123 meV/cell ZPE); created-phonon projection; yield below threshold with three
  channels, law of total variance, n ≥ 1112 for 6% (κ = 2); Si data Table II of albakry2023 (0.10/0.22/0.46 keV), Ge 64 ± 8 eVee at
  254 eVnr (kavner2024); dense tracks (n_pair a_x³ expansion); Auger loss f_A = C_Aug λ_tr²/(12π²D_amb r_tr²) (eq:E.23-fA, derived);
  amorphous pockets (two cluster cuts).
- E.24: Nielsen–Fischetti full-band MC (Si 3.10 eV DFT, 3.50 eV GW/BSE; 4H-SiC 7.3 vs 7.8, 3C-SiC 6.6 vs 6.9, SiO₂ 16.7 vs 18.0);
  full cascade spec (grids, convergence criteria, k-resolved first generation estimator, N_s ≤ 8×10⁴); W^scr memory 21 GB (N_G 300,
  200 ω, 72 irreducible q); plasmon tagged, not added (consistent with E.13); z_qp = 0.8 shifts the RK-model ε_eh by 3% via E.13's fit;
  r_ii(E); w_mem (eq:E.24-wmem) and the spread bound; library inversion (eq:E.24-dft); exciton/capture set; binomial thinning
  ε_eh/(1 − f), (1 − f)F + f (derived).

## Symbols introduced (with defining equation) — all proposed, please check against NOTATION
- f_TLS(q): density vertex of a two-level system, ⟨R|n_e(q)|R⟩ − ⟨L|n_e(q)|L⟩ (eq:E.22-fTLS). 16.7 is unwritten: reconcile with its symbol.
- λ_tun: tunneling exponent ∫ds[2(V(s) − E)]^{1/2} along the mass-weighted path (E.22) (bare λ is the exciton label).
- S_HR,k, ΔQ_k, E_reorg, ε_hop: mode-resolved Huang–Rhys factor (S_HR family of 5.6), mass-weighted mode displacement (ΔQ_k already flagged in
  clash entry 72), reorganization energy, energy released in a hop (E.22). S_HR,R, ω_R: reaction-coordinate Huang–Rhys factor and frequency.
- S_pol(T): polaron (phonon-dressing) exponent of crowdion hopping (eq:E.22-Spol); 𝒥₃: coefficient of 𝒥(ω) = 𝒥₃ω³ (𝒥 of C.20).
- t_obs: observation time of the release verdict (E.22).
- ξ_M: Massey parameter E_gℓ/v_N (E.23) (bare ξ is the energy mismatch of 2.1).
- b_imp, E_coll, ω_e(as used in dP/dω_e): impact parameter, relative collision energy; ω_e already in NOTATION (12.1, energy given to
  electrons) — same meaning, check.
- E_heat: lattice heat of a recoil in the partition table P(E_heat, E_st, N_eh|E_R, r̂_R, T) (E.23); research wrote ℋ.
- t_pr: time at which the recoil state is quenched and recorded (10–100 ps) (E.23).
- E_s, p_s, u_s, ω_s: energy, momentum, displacement, frequency of mode s of the quenched end state (E.23, local).
- 𝓃_pair (\nd_{pair}): pair density in a track (E.23).
- C_Aug, λ_tr, r_tr, D_amb, f_A: Auger coefficient, track line density, initial track radius, ambipolar diffusion constant, Auger loss
  fraction (eq:E.23-fA).
- ℰ_b: bias field (E.23, E.24) — ℰ is the macroscopic field of 5.5; check E.25/20.x usage.
- N_a: number of atoms in amorphous pockets (E.23).
- P_n(q, ω, T): pair-number distribution of a deposit (E.24).
- r_ii(E): ratio of the impact-ionization rate beyond first order in W^scr to the first-order rate (E.24) (research wrote ζ, which is
  kinetic mixing).
- w_mem(E), Γ_k, Γ_E, Γ_ph,loss: memory probability (eq:E.24-wmem); momentum-randomizing and energy-changing rates; phonon energy-loss rate.
- 𝒢_Λ(z), z_j, N_z, σ_N, x_e, x_h, ω_ph, h: generating function of P_casc, roots of unity, FFT length, standard deviation of N_eh, seed
  carrier energies above the band edges, single phonon energy of the reduced model, energy step (E.24). ω_ph against ω_AB of E.13 (same
  role, material-specific here); 𝒢 against other script G's.
- M_i, V_i, N_s: subtree mean and variance of a sampled first step; number of samples (E.24).
- σ_cap(E, T, ℰ_b), f: capture cross-section; capture probability in the thinning law (E.24).
- p_FP (E.11) used in E.23 (not P_FP): the E.11 flag "p_FP against P_FP of E.23" is resolved by using p_FP.

## Terms introduced
- orthogonality-overlap route to α_ohm; release verdict (tunneling exponent bound); polaron narrowing of a crowdion; two-level density
  vertex; landscape sampling of two-level systems; Massey parameter; close-collision excitation kernel; partition table; created-phonon
  spectrum; dense track; track plasma, plasma time; amorphous pocket; momentum memory probability; pair-number library; binomial
  thinning by capture.

## Threads: none.

## Promises made to later sections
- E.22 → 16.7 (f_TLS ratio to the rigid-ion core; ensemble tables), 16.8 (α_ohm; ensemble), 19.6 (release paths, verdict; crowdion band).
- E.23 → 19.1 (partition, dense tracks, f_A), 19.2 (kernel, yield vs albakry/kavner), 19.4 (E_st vs bounds), 19.6 (pockets), 19.5
  (correlations of N_eh with heat and E_st), E.25 (kinetics).
- E.24 → 18.1 (q dependence; w_mem bound), 18.2 (variance terms), 18.4 (computed ε_eh, F_eh), 18.5 (r_ii; exciton/capture set), 21.6
  (library), 21.7 (flags), chap 17, E.25.
- Unwritten targets referenced: sec:16.7, 16.8, 18.1–18.5, 19.1–19.6, 21.6, 21.7, chap:17, sec:11.3, app:E.25 (others' files).

## Notes for the editor
- E.13 says GW includes plasmon emission (no extra channel); the planning spec asked for an "explicit plasmon channel". E.24 resolves
  this as "tagged, its variance share reported, not added".
- Not placed as numbers (campaign-internal, unverifiable publicly): the TLS fraction "10⁻⁵ per atom" (replaced by khomenko2020's
  order-of-magnitude counts), the crowdion Mathieu band width, the 4H-SiC conflicting Fano values, the internal-solver acceptance numbers
  (3.651 eV / 0.1145; Rényi limits), the +1.3% off-grid bias (stated instead as the general h/2 bound). Si ⟨ω⟩ = 45 meV replaced by
  5.3's 123 meV/cell zero-point energy (gives 126 eV, not 138 eV, per 4096 atoms).
- The recrystallization energy "of order 0.1 eV per atom" is flagged in the text as an estimate (no source fetched).

## Proposed ledger rows (the editor merges them)
NOTATION: rows above. · GLOSSARY: Massey parameter | ratio of the collision time scale to the electronic one, E_gℓ/v_N; ≫ 1 adiabatic | E.23 ·
reorganization energy | ΣS_HR,kω_k, energy the lattice relaxes after a configurational change | E.22 · amorphous pocket | connected
non-crystalline cluster left by a recoil cascade | E.23 · binomial thinning | each pair lost independently with probability f | E.24.
CONCEPTS: orthogonality slope = α_ohm; release verdict λ_tun ≤ ½ln(Γ_0t_obs); reference-state rule for stored energy; momentum-memory bound.
CLAIMS: maillet2023 K_b = 0.07, 0.11 [cited, PDF p. 4–5]; fitzgerald2018 meV vs µeV [cited]; khomenko2020 counts and 100× density drop
[cited]; albakry2023 Table II and Eq. (1) [cited]; kavner2024 64 ± 8 eVee, 25 ± 3% [cited, abstract]; nielsen2026 Table II, Sect. IV
[cited]; grueneis2014 vertex shifts of tenths of eV [cited, abstract-level]; λ_tun bound, 27.5 estimate, S_pol limits, ξ_M values,
126 eV, n ≥ 1112, f_A, w_mem, DFT inversion, thinning, 3% z_qp shift, memory estimates [derived]; all costs [estimates from the
specifications].
INDEX: ohmic coupling (computation); orthogonality catastrophe (supercell route); Huang–Rhys factor (release paths); crowdion (Peierls
profile, polaron); two-level system (density vertex; ensemble sampling); Massey parameter; Landau–Zener promotion; partition table;
stored energy (reference state); created-phonon spectrum; charge yield (sub-threshold); Fano factor (nuclear recoil); dense track;
Auger loss; amorphous pocket; pair creation energy (wide-gap); impact ionization (vertex corrections); energy-only reduction (memory
bound); pair-number library; exciton parameters (computation); cascade capture.

## Revision (2026-11-02, App. E.14–E.27 review)
- E.22: aluminum spelling; α_ohm supercells 54/128/250 atoms at Γ only (L = cell side) or one fixed-density grid; cost 10³ GPU-h per defect; configurational-energy rule now a pointer to E.23; TLS transplanted into the 216-atom cell (protocol stated); ≈ 10⁴ screened pairs per glass; closing sentence added.
- E.23: E_d/p_FP protocol is E.11's (one set of numbers); E.23 states t_pr and the 20-direction DFT check. Kernel grid 10 E_coll × 8 b_imp; ≈ 250 core-h per trajectory; HSE subset a few 10⁶ core-h. ZPE offset 126 eV is ten to thirty times a Frenkel pair. C_Aug a scanned parameter. Configurational-energy rule stated here once.
- E.24: BSE pointer → E.6; W^scr to 60 eV with the free-electron kernel above; A_AB = 5.2, ΔA_AB = 1.3 explicit; Ge 77 K pair energy flagged as an input to be measured; 50–1500 eV photon validation at 300 K; wide-gap set 6×10⁵–2.5×10⁶ core-h; q steps of αm_e.
