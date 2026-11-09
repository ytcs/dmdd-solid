# Chapter 14 mock-reader review: reader b (personas b and c)

What I read: Chapter 14 in the built PDF (pp. 797-852) and App. D.38 (pp. 1058-1060), linearly. The PDF (05:36) is newer than every ch14 .tex source. I read nothing else.
How I checked: by hand and with numpy, from the book's own inputs only. I rebuilt the NiO type-II linear spin-wave model from Eq. (7.9) and redid the arithmetic of every worked example. The chapter has no exercises, so the worked examples stand in for them.

## Checks reproduced (both personas)
- 14.1. 5.3 keV and |Q_AF| = 2.575 keV. 2|S|J_AB(0) = 211.7 meV; w = 0.024 and 42 at 5 meV. Eq. (14.5) and the 7.2 keV edge (needs v_max ~ 2.64e-3). The prefactor of Eq. (14.4), from pi/2 x 16pi/3mu^2 x 1/4pi^2. The large-mass limit (14.7), via int dq q eta(q/2m) = 2m^2<v>. Omega = 18.13 A^3, rho_T = 6.84 g/cm^3, |F|^2 = 0.84 and 0.49. Gap: K = 0.097 meV gives 4.53 meV, close to 4.54. Thermal exponents 5.3e3 and 53.
- WE 14.1 and D.38. Delta S = 0.0783 on a 60^3 grid. The zone average of w = 1.158 = 1 + 2 Delta S. Every sum-rule identity: the excess Delta S(1 + 2 Delta S), W_perp^sr = (|S| - Delta S)(1 + 2 Delta S), 1-mag + 2-mag = |S|(1 + 2 Delta S) - Delta S^2. The Wick result <n^2> = Delta S(1 + 2 Delta S). The exact-HP half-sum 2|S|n + |S| - n^2. All the values at |S| = 1/2, 1 and 5/2. D.38's assembly of (14.1) from (2 pi/V)|F c|^2/4 per branch, with V = 2 N_s Omega.
- 14.2. w_perp ~ 0.29 qa and w_par ~ 0.015 (qa)^2 (I get 0.289 and 0.0150). At q = (1/4,1/4,1/4): w_perp = 1.00, w_par = 0.0818, omega = 105.84 meV. w_par -> 0.246 near Q_AF. Band top x 2 = 236.3 meV. Factor (14.11) = 5.0; 1.43 and 0.285 keV. Single-ion pair energies 4D(|S|-1) against 2D(2|S|-1). Exact diagonalization of the 10-site S = 1/2 ferro ring: 0.3277 |J|, and 0.382 for the free pair. All of WE 14.2: |S| = 14.23, D_sw, c_TA, M_cell = 5.50 TeV, B_me = 8.23 meV, k_x = 4.63e-3 nm^-1, g = 0.176 ueV, 85 MHz, 3.0 %, 3.1 % of k_x, 0.146 and 0.010, the upper root 0.418 nm^-1 with 0.32 %, ka = 0.52. The derivation of g^mp in Eq. (14.14), including the circular b_+. The absorption phonon content 2.9e-12.
- 14.3. Table 14.1 in full (g_J, lambda_S, ratio). The Larmor commutator and the weight (14.20) via detailed balance. (14.21) and (14.22). The modulation factor 0.47 and the shift 1e-18. The Kittel energy (14.23): Zeeman plus (1/2)V sum N_i M_i^2 in HL units. The oscillator frequency, the elliptic weights and (omega_x + omega_y)/2 omega_Kit. All of WE 14.3: Omega, 2951.8 u, 0.246 T, 37.8 emu/g, 28.5 ueV, 86.4/82.0 mT, 9.49 ueV, 1 + 9e-6, 24 kHz, 6.6 us, R_peak = 3.64 s^-1 kg^-1, 35 per hour, film 3.16 ueV/27.3 mT/1.74. AFMR (14.26) and (14.27). MnF2: 5.447, 0.0949, 1.021 meV, 247 GHz, 0.0929 and 0.0933, 0.232, 0.74 of YIG, 7.2e-3 and 2.6e-2, B_sf = 8.75 T, 0.009 meV at the flop.
- 14.4. p_n(120 meV) = 15.0 keV and E_kin(5.7 MeV) = 20 eV. (gamma r_cl)^2 = 0.2906 b and the normalization of (14.28), from the standard magnetic cross-section. r_cl^2/4pi = e^4/[8 m^2 (2 pi)^3]. The dipole form factor <j0> + (1 - 2/g)<j2>, consistent with the J-multiplet form. C_sn = 0.83, 1.19, 0.73; <j2>/<j0> = 0.035 and 0.152; ratios 0.994, 0.973, 0.904 at 10 keV. The D_ab of O4, O6, O9, O10. Eq. (14.31) and the polarized-beam elements. The inversion (14.32). All of WE 14.4 (0.050, 0.112, 3.7 %, 0.141, 2.5P1 - 2P2, 0.32). The (q/30 keV)^2 phonon estimate.
- 14.5. q g33 = 7.0e-5 and 21.6 deg/mm from rho = omega^2 Re g/2. The helicity algebra e*_pm x e_pm = pm i q-hat and (14.36). Delta-alpha = 2 omega^2 Im g. The O5-O8 interference contraction, (1/m_e) Re(c5* c8) q.G, up to the overall sign convention of D. The D3 character counts 0, 1 and 2. The averaged gyration -0.0057 bohr = -0.045 g33. The Ga moment bound 0.030 mu_N. Mn12: D = 0.0563 meV, 19D = 1.070, the quartic term +0.144 meV giving 1.214, omega_meta = 1.098 meV, the next line 0.18 meV lower, the barrier top at m = -1 at 4.59 meV (53 K). The 90 % line weight at omega_meta/T = 3.0, which is 4.2 K. The spin-current identity and the sign bookkeeping sigma^T sigma^T = sigma^P sigma^P = -1.
- 14.6. 241.8 kHz, 26.8 mT, occupation 4.6e39, t_coh = 1.045 s, 6.6 s, 249 km, 3.5e-6. The (2 pi)^4/2 normalization of (14.46). The Fejer kernel and its unit integral. 3.4e7 coherence times. 207Pb: 9.03 MHz/T, 0.164 ueV, p = 2.3e-4, mu0 M0 = 2.9 nT. The Bloch rotating-frame equation and all three forms of (14.51). Budker's half-width envelope. u_sp = 3.8e-4. The three regimes of (14.52). The weak-signal t ~ sum x_k^2 and both laws of (14.55), including t = 2 pi t_int sigma^4/(Delta omega_eq S_n^2). WE 14.6: 0.41 Hz, 1.7e-6, 63, 3447 and 82 730, 24^(1/4) = 2.21.

## Persona (b): particle physicist (QFT, no solid-state physics)

### 14.1 Magnon scattering
- Lost: none. Holstein-Primakoff as a 1/|S| expansion maps onto a loop expansion, and the spin-length sum rule is a clean consistency check. The phase epsilon_G = +-1, and the trick of evaluating A, B at the unreduced q, are well motivated (D.38 makes them airtight).
- Not reproduced: the Fig. 14.3 rates (10, 280, 430, 2.6e3, 3.2e3) need the full integral, so I checked only the large-mass end. At 10 MeV, Eq. (14.7) x 0.989 / 11 gives 1.59e3 against the quoted 1.5e3. That is consistent if "a factor of eleven" means about 11.6. State the factor to two digits.
- Used before defined: none (the spin rows, D_ab, eta, A.42 are all from Ch. 1, 8 and App. A).
- Pace: right. The w ~ omega/211.7 and 211.7/omega forms with the tilt picture are the best paragraph of the chapter for me.
- Outcomes. (i) Write S_ab for a collinear AFM at any q, and explain the suppression at Gamma and the enhancement at Q_AF: yes. (ii) Turn it into an O4 rate with sigma-bar_e (14.3): yes; I reproduced the 4/3 and the high-mass limit. (iii) Size the 1/|S| correction: yes, Delta S/|S| = 7.8 % for NiO.

### 14.2 Two-magnon continua and magnon-phonon modes
- Lost: none. Final-state interactions as a ladder (Bethe-Salpeter-like), and the resolvent sum rule that fixes the integrated weight, are familiar.
- Not reproduced: nothing essential. U^mm is never written out, but the text says the solution is open.
- Used before defined: delta_k' and theta_k (14.2.5) come from Sect. 8.8 with no reminder of what each multiplies. One clause each would do.
- Pace: 14.2.3 is a little fast on why the quartic term from the square root is "of the same size". 14.2.4 is right.
- Outcomes. (i) Write the longitudinal two-magnon response and its kinematic edges: yes. (ii) Explain why pairs lower the mass reach by v_max/4c_M but yield little near the edge: yes. (iii) Compute a magnon-phonon gap and mixing: yes, WE 14.2 reproduced.

### 14.3 Absorption into magnons
- Lost: none. The Larmor theorem from [H, S^-_tot] = omega S^-_tot is exactly how I would want it, and the YIG selection rule follows.
- Errors in my field. (1) Opening paragraph: the Compton wavelength 12 cm includes the 2 pi, but "de Broglie wavelength 1/(m v_E^ref) of 24 m" is the reduced one; 2 pi/(m v) is about 150 m. Say "reduced" or include the 2 pi. (2) The dark-photon B' coupling is fine, but say once that B' ~ v E' is velocity-suppressed relative to the electric field. That is why it is subleading wherever electric dipoles exist, and it would help a reader who compares with the in-medium mixing of Ch. 8 and 10.
- Not reproduced: none. 1.2e8 kg^-1 yr^-1 is 3.6 x 3.156e7 = 1.15e8; write 1.1e8, or keep three digits for R_peak.
- Used before defined: "Kittel mode" appears in 14.3.3 (the width paragraph, "for the Kittel mode of YIG"), before 14.3.4 defines it. Forward-reference it or say "uniform mode".
- Pace: right. 14.3.2 on quenching is new to me and was clear.
- Outcomes. (i) Absorption rate of an ALP or dark photon into the uniform mode, with the Lorentzian peak: yes (3.64 s^-1 kg^-1). (ii) Shape corrections: yes. (iii) AFMR frequency and weight: yes, MnF2 reproduced. (iv) Choose lambda_S for a J multiplet against a quenched ion: yes.

### 14.4 Spin responses from neutron data
- Lost: none. The transverse-projector no-go is clean, and the symmetry part of the argument is airtight.
- Not reproduced: none.
- Used before defined: none.
- Pace: right. The two-angle inversion and its error propagation (WE 14.4) is useful and not overdone.
- Outcomes. (i) Convert S_neu to Tr[P_T S]: yes. (ii) Say which operators the data calibrate, bound or miss: yes (O9/anapole calibrated, O4 bounded below, O6/O10/ALP absorption missed). (iii) Apply C_sn: yes.

### 14.5 Chiral and nonreciprocal targets
- Lost: briefly, at "at 1 keV the quartz value of g33 gives q g33 = 0.034". The preceding clause is about energy ("Dark matter at energy omega brings q >= omega/v_max"), so I read 1 keV as an energy: q >= 377 keV and q g33 = 12.6. The 0.034 is for momentum q = 1 keV, an energy of about 2.7 eV, which matches Fig. 14.9b. Write "at q = 1 keV".
- Errors in my field: none. The parity assignments (O8 odd, O5 even; magnetic dipole -> O5, anapole -> O8) are right.
- Not reproduced: the GaAs band averages 0.124 and 0.112, the 2.2/0.8/0.23 MeV boundaries, and the Fig. 14.11 numbers (0.94, 0.37, 1.4, 4.5). They need the book's force constants or spin-wave sums, which I did not rebuild. The definitions are adequate to repeat them.
- Used before defined: the exponents nu and z in tau ~ |T - T_CM|^(-nu z). I know them from RG, but name them "correlation-length and dynamic exponents".
- Pace: 14.5.5 is fast. The step from the Lehmann form to "second order in spin-orbit coupling" packs two separate suppressions into a few lines. I followed it, but only just.
- Outcomes. (i) Use Eq. (14.33) to decide which blocks may be odd in q: yes. (ii) Count gyrotropic invariants for a point group: yes, for D3. (iii) Write the enantiomer-difference rate: yes. (iv) Give the metastable SMM line and its weight: yes.

### 14.6 Coherent fields and precessing nuclear spins
- Lost: none. This is my home ground, and the treatment is correct and careful: the k = -m v sign, the Fejer-kernel approach to the golden rule, the bunching variance N + N^2/N_coh, and the warning against double-counting the Centers et al. correction.
- Errors in my field: none found.
- Not reproduced: the Neyman-construction numbers (1.99, 1.76, 1.5 %, 23 and 5.4 t_coh, 136 and 8.7 t_coh, slope -0.67, factor 3.46). The construction is described only in the Fig. 14.15 caption ("summed power of the bins that hold the line", N_eff equal bins). One displayed equation for the statistic and its distribution (a Gamma law with N_eff dof) would make them reproducible.
- Used before defined: "Schiff moment" (14.6.3) is undefined, which is fine for me. E* uses the star that the book also uses for Born charges Z*; harmless.
- Pace: the random-amplitude point is made three times (14.6.1, 14.6.3, 14.6.4). It could be trimmed slightly.
- Outcomes. (i) Decide golden rule against coherent regime from t_coh and 1/Gamma_T: yes. (ii) Solve the driven Bloch equation: yes. (iii) State the sensitivity scalings and the crossover: yes for the laws; the crossover coefficients only by trusting Fig. 14.15.

### Condescension (b)
None. The explanation of the t^(-1/2) law as "familiar" is pitched right.

## Persona (c): condensed-matter theorist (DFT, many-body; no dark-matter physics)

### 14.1 Magnon scattering
- Lost: none on the magnet side. On the DM side, sigma-bar_e and the O4 normalization (14.3) were the only new items, and they are self-contained.
- Errors in my field. (1) "Delta S/|S| is a lower estimate" of the one-magnon defect, carried into Table 14.3 with basis "bound". D.38 itself says that the ground-state change at the same order is not included, so this is a strong argument, not a proven inequality. I would relabel the basis "est." or add "at this truncation". (2) NiO has two zone-centre gaps: an in-plane one near 0.6 meV and an out-of-plane one near 4.5 meV. The one-constant easy-axis model represents only the upper one. That does not matter at a 5 meV threshold, but say so, because the anisotropy row dominates near the edge.
- Not reproduced: none on the spin-wave side (Delta S, w, sum rules all reproduced).
- Pace: the sum-rule paragraph is the right length. The 1/|S| counting is textbook for me but short, so it is not condescending.
- Outcomes. (i) Rates from S_ab and a DM tensor: yes. (ii) The 1/|S| bookkeeping: yes, and I could extend it to multi-sublattice YIG with Colpa.

### 14.2 Two-magnon continua and magnon-phonon modes
- Errors in my field. (1) "On a ring of ten spins 1/2 the lowest level with two deviations lies at 0.328|J|": in the S^z_tot = N/2 - 2 sector the lowest levels are 0 and 0.191|J| (rotated members of the S = N/2 and N/2 - 1 multiplets). 0.3277 is the lowest level of total spin N/2 - 2 (I confirmed by ED). Say "with total spin N/2 - 2". (2) Exchange striction couples a phonon only to pairs in a collinear magnet: correct. Elsewhere the text rightly notes that DM-type or canted order adds cubic vertices.
- Not reproduced: none.
- Pace: right. The Wortis and Silberglitt-Torrance summaries are accurate.
- Outcomes. (i) Two-magnon S_zz and its zone-average check: yes. (ii) Magnon-phonon hybrid contents and the off-diagonal S_{s,n}: yes. (iii) Place the corrections into the nuisance classes of Sect. 8.8: mostly; delta_k' and theta_k needed a look back.

### 14.3 Absorption into magnons
- Errors in my field. (1) MnF2 shape shift: "omega_M/omega_E, 1.3e-3 in MnF2 with omega_M formed from the sublattice magnetization". With 5 mu_B per Mn and one Mn per sublattice per cell (a^2 c = 78.6 A^3), mu0 M_sub = 0.74 T. In the book's own HL convention (omega_M = 2 mu_B mu0 M_s, which gives 28.5 ueV for YIG) that is omega_M = 86 ueV, so omega_M/omega_E = 1.6e-2. The quoted 1.3e-3 is that value divided by 4 pi: Gaussian M in place of 4 pi M. Please recheck. It is an order-of-magnitude statement, but the stated number looks wrong. (2) Table 14.1 and the projection rule: correct. Sm3+ is the textbook case where J = 7/2 admixture (about 0.1 eV away) matters, and because g_J = 2/7 is tiny, a small admixture moves lambda_S/(g_J/2) = -5 a lot. Flag Sm3+ explicitly as fragile.
- Not reproduced: the eight-site XXZ cluster numbers (0.85, 0.91; 5-23 %), which needs ED that I did not redo.
- Pace: 14.3.2 (Wigner-Eckart, quenching, g_ab = 2 - 2 xi Lambda) is standard for me but compact, so it is not condescending. The warning against lambda_S = g - 1 for 3d ions is valuable.
- Outcomes. (i) The Larmor theorem and when it breaks: yes. (ii) The Kittel formula from a two-quadrature oscillator: yes. (iii) AFMR weight suppression: yes.

### 14.4 Spin responses from neutron data
- Errors in my field: none. The dipole form factor sign is right for a quenched ion with g > 2, the perpendicular-projection rule is stated correctly, and the four-of-nine count with full polarimetry is right. The FDT correction to T -> 0 is correctly caveated as exact only for harmonic magnons.
- Not reproduced: none.
- Pace: right.
- Outcomes: all yes, as for (b). I would add that spin-flip scattering with P parallel to q also contains nuclear-spin-incoherent scattering (one third of it). It is small for YIG and NiO, but not zero for hydrogenous frameworks.

### 14.5 Chiral and nonreciprocal targets
- Lost: the DM-side items (the O5/O8 tensors and the parity-violating DM argument) are new to me but self-contained.
- Errors in my field. (1) "such as the one that cants the spins of the hexaferrite": h-(Lu,Sc)FeO3 is a hexagonal ferrite (an improper ferroelectric of the h-RMnO3 family), not a hexaferrite. That term normally means the Ba/Sr M-, Y- and Z-type ferrites. (2) The chiral-phonon section correctly separates the Born-charge moment (about 1e-2 mu_N) from the giant moments of electronic origin. The non-conservation argument [H, L_z] = 2i u.[J_z, D]u is right.
- Used before defined: "Schiff moment" (14.6.3, for this persona), and "pseudo-angular momentum" (14.5.3) is named but not defined.
- Pace: 14.5.1 is right. 14.5.5 is fast (see (b)). The Landau versus mean-field versus spin-wave comparison is welcome.
- Outcomes: yes for the symmetry tables and the point-group test. For the multiferroic I can state why the static response needs both symmetries broken, and second order in SOC, but I could not compute R_{sz J} from the text alone. The text says so.

### 14.6 Coherent fields and precessing nuclear spins
- Lost: none. The Gaussian-field statistics were new and clearly built. The Bloch and NMR parts are standard.
- Errors in my field: none. The spin-noise argument (coth = 1/p_pol) is neat and correct.
- Not reproduced: the Fig. 14.15 numbers, as for (b).
- Used before defined: "Schiff moment" is used without a sentence on what it is (the residual nuclear EDM-like moment that survives electronic screening). One clause would help this persona.
- Outcomes: yes, except the crossover coefficients (see (b)).

### Condescension (c)
None. Hund's rules, Wigner-Eckart and the Bogoliubov transformation are recalled in a line or two, as they should be.

## Issues for both personas
- Four unresolved references "??" in the PDF: the chapter opening ("superconductors ... follow in ??"), 14.3.3 (exothermic dark matter "is treated in ??"), 14.5.4 ("readout models of ??") and the Summary ("are the subject of ??").
- The 4 pi in the MnF2 shape-shift ratio (14.3.5), above.
- The 1 keV energy/momentum ambiguity in 14.5.2, above.
- "Lower estimate" against "bound" in Table 14.3 for the one-magnon defect, above.

## Verdict
Persona (b): MINOR GAPS. Persona (c): MINOR GAPS.
I checked every derived equation and every worked-example number I could reach, and none failed except the MnF2 omega_M/omega_E ratio and the wording of the 1 keV example. The Neyman-construction and cluster/ED numbers are presented without enough method to reproduce. None of these blocks the following material. Both personas would keep reading.
