# Chapter 1 mock-reader review: reader b (personas b and c, isolated)
Read: tex/ch01/s1-1..s1-5, appC/C-9, appD/D-1 only. Numerics re-derived in Python/scipy (scratch scripts, not
committed). Almost every quoted number reproduces to the stated digits (list at the end); exceptions below.

## Persona (b): particle physicist, QFT yes, solid state no

### 1.1 Evidence for dark matter
- Lost points: none. Read as a fair summary; I already know the evidence, and the section is brief about it.
- Reproduced: rho_halo(r_sun)=0.53 GeV/cm^3; rho_crit=1.053e-5 h^2; 1.26e-6 GeV/cm^3; 9.7e-48 GeV^4; s0;
  H=1.66 g*^1/2 T^2/M_Pl; the x_fo log equation (from n<sigma v>=H with Boltzmann n); x_fo=25.4 (100 GeV),
  20.7 (1 GeV); <sigma v>=1.98e-9 GeV^-2 = 2.3e-26 cm^3/s. "90 decades" checks.
- Field check: g*~80 is used at 1 GeV too, where T_fo~50 MeV and g*~10-17. x_fo moves by ~1, so harmless,
  but a field reader notices; one clause would help.
- Field check: "few-hundred-eV thresholds of ton-scale xenon detectors" (l.62). Standard S1+S2 nuclear-recoil
  thresholds are ~keV_nr; only S2-only analyses go lower. The conclusion (0.1 keV is below) holds either way;
  say which analysis is meant.
- Outcomes: estimate local density from v_c: yes. Thermal <sigma v> and the need for a light mediator: yes.
- Pace: right for me.

### 1.2 The local halo
- Lost points: none on the halo physics. Daily modulation (l.200): "uniaxial crystal", "optic axis",
  "polar crystals" are undefined for me. Inferable from context, but one gloss would help.
- Astronomy terms (right ascension, declination, sidereal time, proper motion) are used without definition. The
  vector formulas make them recoverable, so this is not blocking.
- Reproduced: N_esc=7.393e7; <1/v>=1/287.9 (1041 natural); <v>=354.1; flux 1.06e8; v_rms 291/284;
  F peak 335; tail fractions 36/15/4.2/0.58/0.10%; 94%, 59%, mean cos 0.66 (Monte Carlo); annual amplitude
  14.6, phase 71.9 deg, t_peak=72.9 d; extremes 266.4/237.4 and mean 252.1; second-order 1.3/1.6;
  crossing 364; eta reversal at 211; modulation +21/-16% (600) and +42/-28% (700); yearly-average offsets
  -0.3%, +2.6%, +5.6%; dln<1/v>/dv_E=-2.195e-3 giving -3.2%; v0 and v_esc sensitivities (1.11/0.89, 1.06/0.92,
  2.26/0.10); theta_E=42.5 deg; NCP vector; (east,north,up) at 45N; sin^2 theta_E=0.456.
- Too slow: the paragraph checking that the orbit vectors are orthonormal, and the second-order term discussion,
  are more than I need. They are cheap, though.
- Too fast: none.
- Outcomes: write f_chi in the lab, compute N_esc, <1/v>, <v>, flux, the annual amplitude and phase, and the
  daily angle: yes, all done.

### 1.3 Kinematics
- Used before defined: "Brillouin zone" (l.7, "never fold q back into a Brillouin zone") appears in the first
  paragraph. "Reciprocal-lattice vector" only appears at l.121, and "crystal momentum" at l.61 ("lowest
  electronic excitations sit at a nonzero crystal momentum") is never defined. For me the l.7 sentence is noise
  until l.121. Fix: move the folding remark to l.121, or add one gloss at l.7.
- Reproduced: eq 1.3-elastic, ERmax, omega_q, vmin (via the cos theta bound), omegamax and minimizing q;
  m_min 0.28 MeV/eV, 0.32 MeV (Si gap), q=0.84 keV; 8.5 keV, q=23 eV; table 1-kinematics, all 15 entries;
  gap band 0.46-4.8 keV and 0.42-53 keV; 45 MeV for 1.11 eV on a free Si nucleus; Xe 0.11 keV; 4mu^2/(mM)=0.142;
  angular delta average 1/(2qv); measure q dq/4pi^2; eta(300)=1.53e-3, eta(700)=7.96e-6 (ratio 192, text
  "190"); eta(600)=19.2, eta(700)=2.38 natural; June/Dec ratios at 700/760/780; edge expansion eq 1.3-edge
  (I expanded it myself), scale 173 km/s, 0.81/0.92 and 0.98/0.99; mass-edge eta ratios 2.8e-4, 1.9e-3, 1.1%,
  14%, 85%.
- Small: m_min annual swing "-/+3.6%" is the mean of +3.4% and -3.9%.
- Small: the table caption says "The third column is also the threshold for which m_min = m_chi". The caption
  lists three described columns, so "third" reads as the Si-nucleus column. It means 1/2 m v_max^2. Say "the
  second data column" or name it.
- Small: s1-3 l.171 cites Essig 2016 "Eqs. (67) and (68)". D.1 l.52 cites "Eqs. (66) and (68)" for the same
  branches. One of them is wrong.
- Outcomes: derive omega_q and vmin, get m_min for any threshold, sketch the (q, omega) region, write eta in the
  SHM and its edge form: yes.

### 1.4 Models
- Field check (my field). The appendix C.9 derivations are correct and I re-did them: Proca equation and Lorenz
  condition from the divergence, Green's function by residues, the sign of the interaction energy
  (vector repels like couplings, scalar attracts), kinetic-mixing shift (F'^2 coefficient -(1-zeta^2)/4),
  y_e=-zeta e, B-L charges, pseudo-Dirac splitting giving an off-diagonal vector current, the ALP
  -1/4 g phi F Ftilde = g phi E.B (with the eps^{0123}=+1 convention, unstated). No errors.
- Condescension: the main text is not condescending. C.9 goes slowly for me (Euler-Lagrange for Proca, Jordan's
  lemma), but it is an appendix and pitched for persona (a), so it is acceptable.
- Mild: the energy as -integral of L for the non-dynamical A'^0 sector is a known subtlety. The text's check
  against 1/2 int E^2 settles it; fine.
- Reproduced: sigma_e(heavy dark photon)=7.67e-18 MeV^-2 = 3.0e-39 cm^2; freeze-in 6.0e-38 cm^2; both
  limit-box leading corrections; mu ratios 1.22/950 and 3.96/3100; 1/R=40 MeV.
- Used before defined: Pi, sigma_1, S(q,omega), "plasma frequency", "RPA with local fields". All are forward
  referenced; fine for a road-map section.
- Outcomes: derive V(x) and V~(q), define sigma_e and F_DM, compute sigma_e for given couplings, coherent
  A^2 scaling, absorption kinematics: yes.

### 1.5 Detector signals
- Lost points: none blocking. Solid-state device content (skipper CCD, NTL, TES, KID, quasiparticles) is
  explained enough for me to follow the logic, if not the devices.
- Reproduced: 27 pairs and spread 1.8 vs 5.2; step-model 2 and 3 pairs; thresholds 1.11/4.71/8.31 eV leading to
  0.32/1.34/2.37 MeV; 0.17 keV for 0.6 meV; dimension check of eq 1.5-rate; Poisson limit derivation;
  N90=2.303, 3.00, 3.89, 5.32; background sqrt scaling; modulation N>=144 (2A/pi=0.118); toy rate 7.106e33,
  r=2.243e41, N=22.4, limit 1.03e-41.
- Could not reproduce: fig 1-exclusion numbers (heavy-mediator minimum at 9.7 MeV, factor 46 at 1 MeV). The
  caption's toy is "S flat between E_g and 30 eV and cut off at q ~ 2q0". With a sharp cut I get a minimum at
  5.1 MeV and a factor of 21. A Gaussian cut gives 6.8 MeV and 23; an exponential cut gives 14.7 MeV and 56. The
  light-mediator numbers (2.0 MeV, 1.5) do reproduce. Fix: state the cutoff function.
- Field check: the frequentist statement ("at least 90%") is correct for a discrete Poisson count. Good.
- Outcomes: assemble the rate, set a zero-background limit, explain the edge and slopes of an exclusion plot: yes.

### Persona (b) verdict: MINOR GAPS
I would keep reading. The particle-physics content is correct and not condescending. My only friction is
solid-state vocabulary dropped early in 1.2-1.3 (Brillouin zone, crystal momentum, optic axis).

## Persona (c): condensed-matter theorist, DFT and many-body yes, dark matter no

### 1.1
- Lost points: "comoving volume" (l.73) is undefined; I inferred it from n/s = const. Otherwise the cosmology is
  given at the depth I need, and the freeze-out estimate is done in steps I could redo with stat mech alone.
- Outcomes: yes (as for b).

### 1.2
- Lost points: the astronomical frame work (galactic axes, LSR, RA/Dec, sidereal time, hour angle) is dense
  for me. I followed it only because explicit Cartesian vectors are given. A short glossary sentence for RA/Dec
  would help. Not blocking.
- Field check: the uniaxial-crystal cos^2 argument is correct (evenness in n, axial symmetry of the halo). The
  sapphire vs GaAs remark is sensible.
- Outcomes: yes. I reproduced the daily angle range for an arbitrary axis.

### 1.3
- Condescension: none. "Each defined here in one sentence" for band gap and phonons is the right tone, and it
  reads as service to persona (a), not lecturing.
- Field check, 2pi/a: for silicon (fcc, a = 5.43 A) the shortest reciprocal-lattice vector is
  |G_111| = sqrt(3) 2pi/a ~ 4.0 keV, not 2pi/a ~ 2.3 keV. The text calls a "the lattice constant of a cubic
  crystal" and treats 2pi/a as the folding scale. Two consequences: "above about 0.4 MeV, 2 m v_max exceeds
  2pi/a" would be ~0.75 MeV for G_111, and the "0.6 q0" scale shifts to ~1.1 q0. Order-of-magnitude
  statements survive. Fix: say 2pi/a is the cubic-cell scale and that the first G of fcc Si is sqrt(3) larger.
- Field check, phonons: "phonons ... from zero to about 100 meV" (l.123) sits oddly against "optical phonons of
  30 to 150 meV" in 1.1 l.83. Make them consistent.
- Field check, limit box: "the recoil energy exceeds the binding of the atom to the lattice and the phonon
  energies, E_R >> 0.1 eV" conflates two scales. The impulse approximation needs E_R >> omega_phonon (tens of
  meV). The displacement or binding energy (~10-20 eV in Si) is a different, larger scale, and it is not what
  the free-recoil formula requires. Reword.
- Field check, optical phonons: "can be excited at any q >= omega/v_max" assumes a flat branch and should also
  carry q <= 2 m v_max. Minor.
- Outcomes: yes. The kinematics is new to me, and the region plot and vmin were the most useful part of the chapter.

### 1.4
- Lost points: field-theory notation (Proca, F Ftilde, gamma^5) is new for me, but C.9 carries me through the
  vector and scalar cases. The ALP non-relativistic reduction, eq 1.4-alp, is quoted, not derived; I take it on
  trust. That is acceptable because it is attributed and deferred to ch. 8.
- Field check: in-medium mixing and 1/|eps|^2 screening are stated correctly. "Pi set by the plasma frequency"
  is fine. "Matrix elements of n_q vanish as p -> 0 by charge conservation" is right via continuity
  (<f|n_q|i> = q.<f|j_q|i>/omega).
- Outcomes: yes. I computed sigma_e for the benchmark.

### 1.5
- Condescension: the definitions of hole and electron-hole pair are basic for me, but short. Fine.
- Field check, Al gap: "In aluminum 2Delta_BCS is below a meV; the dark-matter literature adopts 0.6 meV."
  Bulk Al has Delta ~ 0.18 meV (1.76 k_B T_c, T_c = 1.2 K), so 2Delta ~ 0.34-0.4 meV in films. 0.6 meV is
  ~1.5x too large as a physical value. State the measured 2Delta next to the adopted convention. Otherwise the
  0.17 keV threshold mass reads as physical; with 0.36 meV it is ~0.10 keV.
- Field check, phonon cascade: "optical phonons of about 60 meV ... decay into acoustic phonons of a few meV"
  compresses a multi-stage anharmonic and isotope-scattering cascade. The first decay gives ~30 meV LA/TA, and
  propagation is quasi-diffusive before it becomes ballistic. Acceptable as a one-liner; "eventually" would
  make it accurate.
- Field check, numbers: the Si gap is given as 1.11 eV (1.3, 1.5) and as "the 1.2 eV gap" (1.5 photons,
  l.44); unify. CsI gap 6.4 eV is high; ~6.1-6.2 eV is usual. Minor.
- Field check, TES: "phonons from the crystal break Cooper pairs in a superconducting film, and the change in
  resistance ... is read out". For QET-style TES the pairs are broken in Al collector fins and the
  quasiparticles heat the W TES. Fine at this level.
- Field check, DFT: "DFT gives the bands and wavefunctions" (l.87). A CM reader wants "Kohn-Sham" and a hint
  that these are not quasiparticle states; the pointer to app. E covers it.
- Outcomes: yes. Same as for (b).

### Persona (c) verdict: MINOR GAPS
I would keep reading. Nothing blocks. The CM content is mostly right; the fixes are 2pi/a for fcc Si, the Al
gap value, the limit-box validity wording, and the gap and phonon-range inconsistencies.

## Overall verdict: MINOR GAPS
No step blocks later material. The algebra and almost all numbers reproduce. Priority fixes:
1. Fig 1-exclusion: state the toy q cutoff, because 9.7 MeV and 46 do not reproduce from "cut off at q ~ 2q0".
2. The Brillouin-zone sentence in the first paragraph of 1.3 comes before any definition; move it or gloss it.
3. Si folding scale: give 2pi/a vs |G_111| = sqrt(3) 2pi/a explicitly.
4. Al 2Delta: state the physical value next to the 0.6 meV convention.
5. Limit-box validity: E_R >> phonon energy, not ">> binding to lattice".
6. Citation clash: Essig 2016 Eqs. (67)-(68) in 1.3 vs (66)-(68) in D.1.
7. Consistency nits: phonon range 100 vs 150 meV; Si gap 1.11 vs 1.2 eV; table-column wording; xenon
   threshold wording; g* at 1 GeV.
