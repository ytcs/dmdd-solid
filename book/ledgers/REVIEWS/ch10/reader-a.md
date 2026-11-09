# Chapter 10 mock-reader review: persona (a), isolated
Reader: first-year PhD student entering dark-matter direct detection (READER.md, primary persona).
Text read: `tex/ch10/ch10.tex`, `s10-1` to `s10-10`, `tex/appD/D-29.tex`, `D-30.tex`, linearly. The built PDF
(Nov 1 23:46) predates every ch10 source (Nov 2), so I read the .tex. I reread the referenced equations of
Chs. 1-8 and A.8 (eq:4.2-Sab, 4.4-SL, 4.4-fsumL, 4.6-R0, 4.6-eps2, 4.9-S, 8.2-spectrum, A.8-eta/rate/fcrys,
3.2-rho/closure, 2.2-fion-pw). I checked the algebra by hand and the numbers in sympy/scipy (scratchpad only).

## 10.1 Band-to-band scattering and the crystal form factor
- **Reproduced:** eq:10.1-S0 from the bubble (-2 Im R^0_00 with g=2, sum_k -> V int d^3k/(2pi)^3); the prefactor
  4pi; substituting eq:10.1-fcrys into eq:10.1-rateiso to get the limit-box form, including the extra factor omega;
  the WE prefactor 2.45e5 /kg/yr (M_cell = 52.33 GeV = 9.33e-26 kg, c = 3e10 cm/s); mu = 486.2 keV;
  1.60e5/365 = 440 /kg/day; 2pi/a = 0.61 q0, |G111| = 1.06 q0, 2.2 q0 = 8.2 keV; 10 MeV reach 35 eV / 53 keV.
- **Lost point (moderate, not blocking).** WE 10-rate gives the IP heavy-mediator rate at 10 MeV as 1.60e5, a peak
  at 6.5 eV and a mean of 6.0 eV. Sec. 10.2 then calls its own IP rung "the unscreened rate of Sec. 10.1"
  (Fig. 10-rungs caption) but quotes 1.36e5, a peak "near 5 eV" and a mean of 6.2 eV. On a first read I took this
  for an error. The explanation (two tabulations disagree by 18-34%) comes only in 10.10. Fix: one sentence in
  10.2 saying the IP rung of the DarkELF tables is 15% below the Essig table, with a pointer to 10.10.
- **Arithmetic slip:** "q = 1.9 q0 = 7.2 keV" (WE 10-rate). 1.9 x 3.73 = 7.09 keV, so either 7.1 keV or 1.93 q0.
- **Minor inconsistency:** 10.1 sends daily modulation to Sec. 11.7, 10.2 sends it to Sec. 1.2.
- **Used before defined:** none blocking. PBE, scissor, Umklapp, T_0 and "70 Ry" are all from Chs. 3 and 8.
- **Pace:** the normalization material appears three times (the body paragraph "Five conversions...", the
  paragraph after the box, and D.29 Conversions). That is slow. Otherwise the pace is right.
- **Outcomes.** (i) Derive S^0 from the master formula: yes. (ii) Convert between |f_crys|^2, S-bar^0 and eps_2,
  and spot spin and bin factors: yes, I checked eps_2 = 2 pi alpha S-bar/q^2 against eq:4.4-SL.
  (iii) Compute a rate from a tabulated form factor: yes, prefactor reproduced. (iv) Apply the f-sum test:
  yes (first moment 4pi*4/Omega*q^2/2m = pi n_e q^2/m with n_e = 8/Omega).

## Appendix D.29
- Every step reproduced: the pair states, eq:D.29-S0, the zeroth/first moments, the angle average written as
  delta(q - |k'-k+G'|), and the prefactor 2pi^2/(alpha m^2 Omega) = 1.99 eV with Omega = 40.05 A^3.
- One gloss is too quick. "The valence-valence terms cancel between q and -q" really needs two facts: the sum
  at -q is minus the sum at q (reverse transitions), and the sum at -q equals the sum at q (S^0(q) = S^0(-q)).
  Together they make it zero. Stating both would take one clause.

## 10.2 Screening and the loss-function rate
- **Reproduced:** |V|^2 S = sigma F^2 q^2 L/(2 alpha mu^2), and with it the prefactor 1/(8 pi^2 alpha) of
  eq:10.2-rate; the Hölder interpolation (exponents r = 2/(1+n), s = 2/(1-n)) and the 1/(16 pi alpha) of
  eq:10.2-bound; the eigenvalue argument that (eps^-1)_GG lies in (0,1] in the RPA; S_ee^ac from the phonon
  amplitude (2 M N omega)^(-1/2), its first moment and inverse moment; Omega_P,e = 0.51 eV, the lattice term
  equal to one at 18 keV and 3e2 at 1 keV; r_s = 2.0; 1.11/0.0641 = 17; 7.3e7 x (16.6/31.1)^2 = 2.1e7.
- **Lost point (minor).** The last sentence of the paragraph after eq:10.2-relaxed ("the coupling carried by a
  unit volume, which vanishes for the charge, is c_1^(e) n_e here") did not parse for me. I could not tell
  what "coupling carried by a unit volume" refers to. Fix: say it is the coefficient of q.U in the
  electron-following density row, which cancels between electrons and nuclei for a charge coupling.
- **Too fast:** the subsection "A lattice that relaxes" moves quickly from phonon quantization (Ch. 5) to
  the electron-following charge. It is reproducible with Ch. 5 open, but persona (a) needs it open.
- **Outcomes.** Write the loss-function rate and say when it is exact: yes. Explain why 1/|eps|^2 at one q
  overstates the screening of a rate (three reasons): yes. Derive the sum-rule bounds: yes. Show why the
  n<1 bounds fail for an electron-only coupling with a relaxing lattice: yes.

## 10.3 Electron-gas models and plasmons
- **Reproduced:** k_TF^2 = 3 omega_p^2/v_F^2; k_F = 3.57 keV and omega_p = 16.6 eV at r_s = 2; Z_L and its
  expansion (d eps_1/d omega = (2/omega_pl)(1+2x)/(1+x)); that the first moment equals the whole f-sum to order q^2;
  9.85 keV; k_F v_max = 9.5 eV; v_th = v_F + q_c/2m_e = 9.53e-3 (9.18e-3 quadratic); the quadratic cutoff
  2.24 keV / 20.6 eV; q = 6.27 keV; the log ratio 1.24 (1.31); Maxwellian tails 3.7e-49 and 1.8e-53 at
  10.5 and 11.0 v0.
- **Ambiguity (minor):** WE 10-plasmon places the closest approach of omega_pl(q) - q v_max at 1.34 keV and
  14.7 eV. That matches the exact Lindhard zero (I get 1.335 keV, 14.73 eV). The quadratic dispersion, which
  is the only one written out, gives 1.72 keV and 14.5 eV. Say "exact Lindhard dispersion".
- The decay subsection is followable. B_pl^+ is an order-of-magnitude estimate and is stated as one.
- **Outcomes.** Compute the gas rate and say why it agrees at 100 MeV (cancelling errors): yes. Isolate the
  pole and its residue: yes. Show that the halo cannot reach the plasmon: yes, by v_th and by the explicit gap.

## 10.4 Spin, current and velocity couplings
- **Reproduced:** the 17 operators and 289 elements; the 1/4 triplet factor; eq:10.4-O8, prefactor
  1/(16 pi^2) = (1/4pi^2)(1/4); eta_2 = 2 int v' eta from J'(vmin) = -2 vmin eta; eta_2/eta(0) = <v>/<1/v>
  ~ 1.1e-6; (2/5) v_F^2 = 2.0e-5; the band edges; the WE numbers 36.4, 26.3, 41-76, 29-60, 42-77.
- **Inconsistency (minor):** the text says the half-width 2 sqrt(r)/(1+r) is below 10% only for
  r < 2.4e-3. D.30 says 2.5e-3 for the same criterion, and 2.5e-3 is correct (s = 0.0501). The 2.4e-3 belongs
  to the figure's different criterion, (sqrt r + 1)^2 <= 1.1. Give each criterion its own number.
- Rounding: (sqrt 25.3 - 1)^2 = 16.24. The WE prints 16.3, presumably from an unrounded r_IP. |eps|^2 at
  3 eV is 770 here and 761 in 10.7.
- **Used before defined:** "anapole moment" is fine (Sec. 8.1). Spin current J^{alpha beta} is fine (eq:8.1-rows).
- **Pace:** the "published treatments" paragraph (Hochberg, EXCEED-DM, Catena-Iglicki) is dense, with three
  papers and their row choices in one paragraph. I could follow it but had to reread it twice.
- **Outcomes.** List the rows a given operator needs and which are screened: yes (Tab. 10-minimal). Write
  the O_8 rate: yes. Bound an uncomputed cross term: yes.

## Appendix D.30
- Every step reproduced: eq:D.30-O8 and its contraction; the longitudinal terms collecting to
  (Delta/q)^2 S_nn; the kernel; the PT parity of n, j (even) and s (odd); the Catena dictionary
  (f = (q/2m) f - j checked on plane waves; W_1 = (2 Omega omega/pi) S-bar from eq:10.1-fcrys);
  eq:D.30-optical (ratio 2 omega^2 |eps|^2/q^2).
- The Wigner-Eckart step for the triplet block is stated, not shown. That is acceptable, since Ch. 7 used it.

## 10.5 Excitons at finite momentum
- **Reproduced:** eq:10.5-rate from eq:4.9-S (4 pi^2 alpha against 8 pi^2 alpha); the line-to-continuum match
  at the edge (both 1/(2 pi a^3 E_b)); the 8.0 E_b and 7.1 E_b; 1/(pi a_x^3) = 4.3e-6 A^-3; 0.333 -> 0.329 MeV;
  the C4 argument (yz odd, (zx,xy) like (z,y)); R_n1 small-r coefficient; the 2p/1s ratio (g/rho)^2/(32 a^2) ~ 1e-3;
  the single-oscillator ratio (E+omega)/2E, 3.4 at omega -> 0, and 2.23 at 1.39 keV (E_0 = 9.1 eV);
  the coupling-block ratio (Delta+2K)/(Delta+K); (a/a_x)^3 = 2e-3.
- **Error.** The second paragraph after eq:10.5-lines says the Fermi factor "falls to 2.6 at 10 E_x^b". With
  xi = 10^-1/2, 2 pi xi/(1 - e^{-2 pi xi}) = 2.30. The value 2.6 belongs to omega - E_min = 0.10 eV = 6.8 E_x^b,
  which is the case WE 10-xline uses (1.27 eV), and the WE is right. Change "2.6 at 10 E_x^b" to "2.3".
- **Used before defined:** Gamma_25' is explained in place. "Second class" is defined in place. Glide
  symmetry is pointed to App. C.17. All fine.
- **Outcomes.** Write the exciton rate: yes. Derive the Elliott edge: yes. Explain why the 1s line is
  dark on the [100] valley axis: yes. Size the resonant-only error: yes.

## 10.6 Core and relativistic states
- **Reproduced:** eq:10.6-Sat from eq:2.2-fion-pw (with phi normalized to 1, |f|^2/4E gives (2l+1) m/q int k phi^2);
  the closure check; the near-opening N_acc; the openings 11.30/11.52 keV and the masses 8.5/8.7 MeV; 25 and
  19 MeV; the 16-37 keV window at 10 MeV; q^2/4m^2 = 1.2e-4, 8.6e-4 and 2.0e-3; qp/4m^2 = 5.9e-4;
  delta_mv = -1.83e-3 and -5.76e-3; delta_oo = -5.7e-4 and -1.8e-3; totals -0.24% and -0.76%;
  the orbit-orbit double commutator, sign included; 1.13 and 0.055; screening 0.012 at 12 keV.
- No lost points. The projector argument for the absence of interference is clean.
- **Pace:** the f-sum subsection (10.6-fsum) is the most specialist part of the chapter. It is correct and
  followable, but it serves the acceptance test of a code rather than the rate a student computes.
- **Outcomes.** Say at which q a core shell takes over: yes (Ge 3d at 12.5 +- 1 keV). State when core and
  valence factorize: yes. Size the relativistic corrections: yes.

## 10.7 Absorption on electrons
- **Reproduced:** Gamma_L and Gamma_T from the self-energies, and Gamma_T/Gamma_L = 1 + v^2[2 Re(1/eps) - 1];
  WE 10-darkphoton in full (|eps|^2 = 5.139, L = 0.2467, rate 1.52e33 zeta^2 against 7.82e33, zeta = 4.4e-17,
  -1.7e-6); the ALP spin trace and the 3/4; eq:10.7-alp; the ratio 1.6e-8; the B-field rate from the dissipated
  power ((eps^-1)^dag - eps^-1 identity); B_0 = 1953 eV^2, zeta = 2.0e-17, 0.58 /kg/yr, mu_B B = 0.58 meV;
  eq:10.7-aniso; the scalar sum rule [[p^2,V],V] = -2|grad V|^2.
- **Used before defined (minor):** "polar group", "pyroelectric", and O_h, T_d, D_3d as group names in the scalar
  mixing argument. Ch. 7 introduced T_d and irreps but not the polar groups. One clause would do: "groups that
  leave some direction fixed under every operation".
- **Outcomes.** Compute DP, ALP (electron and photon couplings) and scalar absorption rates, and say which
  response each needs and whether it is screened: yes.

## 10.8 Two-insertion processes
- **Reproduced:** the pair-rate bookkeeping, and that eq:10.8-geff makes the pair event rate equal the
  single-scalar event rate at mass 2 m_phi exactly; the pseudoscalar and vector forms; <|v - v-bar|^2>^(1/2) = 402 km/s;
  G_S = 1.4e6 G_F, Lambda = 0.25 GeV, g_eff = 1.3e-21; the Thomson-limit derivation (2/3, Jacobian);
  series eq:10.8-series, including -17/4 with exact kinematics, -0.3% at 100 keV, 1% at 165 keV, 10% at 517 keV;
  the |M|^2 to Gamma check; the ALP series 1 - 5x/2 + 9x^2/2; NR within 10% below 49 keV, 21% high at 100 keV;
  WE 10-alpcompton (1.34e-25 and 2.46e-25 cm^2, ratios 5.1 and 9.4, overstatement 1.70).
- **Lost point (minor):** "The two coincide, particle by particle" after eq:10.8-geff. A pair makes one event,
  so per-particle counting made me stop. What coincides exactly is the event rate per volume of the pair channel
  and that of a scalar of mass 2 m_phi at density rho_chi. Saying that is clearer.
- The criticism of the published ALP Compton rate is argued well. I can see that the small-mass limit
  contradicts eq:10.8-alpNR.
- **Outcomes.** Reduce pair absorption to single absorption: yes. Derive the Thomson limit and judge the
  seagull: yes. Explain the factor in the published ALP rate: yes.

## 10.9 Inelastic, exothermic, boosted and fermionic dark matter
- **Reproduced:** the endothermic thresholds 0.60 and 3.2 MeV; the exothermic sphere (delta in k gives m k*);
  the 1/(4 pi^2 alpha) of eq:10.9-shell; omega_line = mu|Delta|/m_e, with the WE line positions 1.64, 3.70, 6.62,
  8.54 eV and the momenta 1.29-2.96 keV (3.20 keV at infinite mass); the condition 2|Delta|/v_max^2 = 2.9 MeV;
  the Dirac trace (2E - omega)^2 - Q^2 and the v -> 0 limit; the convexity bound and 2%/9%; the Cherenkov
  thresholds 0.28/0.15; the fermion tensor and continuity (m_chi/q)^2; sigma_F/2pi; the ratio expansion
  eq:10.9-ratio (sympy); Gamma_vac = mu^2 Delta^3/pi from the dipole formula; eq:10.9-decay in vacuum and
  in a transparent medium (n^3); 3.44^3 = 41, 3.54^3 = 44.
- No lost points. The section is long (four topics), but each subsection stands alone.
- **Too fast:** "up to the sign convention of the antisymmetric term" in the fermion trace. It is dropped at
  once, so it costs nothing, but a student would like to be told which convention.
- **Outcomes.** Write the inelastic rate and find the exothermic peaks: yes. Bound the retardation error
  of the NR density row: yes. Build the fermionic-absorption tensor: yes. Say when an in-medium decay is
  radiative: yes.

## 10.10 Uncertainties and open problems
- **Reproduced:** the rung steps (52%/26%, ratio 2.8); 10.5 eV and 15.9 keV; m_min 0.316 -> 0.333 MeV;
  the WE band: ln terms 0.247/0.289/-0.078/0.065, sigma = 0.393, 1.19e4 to 2.62e4, 93% of the variance, 1.65
  with +0.49, the light mediator 1.67, theta = 1 giving 2.27e4.
- This section resolves my 10.1/10.2 confusion, but only here.
- **Outcomes.** Turn truncations into nuisance templates and put a band on a rate: yes.

## Cross-chapter summary
1. Lost points (none blocking): the IP-rate mismatch between 10.1 and 10.2, explained only in 10.10 (the
   largest); the opaque "coupling carried by a unit volume" sentence (10.2); "particle by particle" (10.8).
2. Steps I could not reproduce: none. One error found: the Fermi factor "2.6 at 10 E_x^b" should be 2.3 (10.5).
   Slips: 7.2 keV for 1.9 q0 (10.1); r < 2.4e-3 against 2.5e-3 (10.4 vs D.30); unspecified dispersion for
   the 1.34 keV / 14.7 eV closest approach (10.3); |eps|^2 770 vs 761; daily modulation sent to 11.7 vs 1.2.
3. Used before defined: polar group / pyroelectric / O_h, D_3d (10.7). "Dirac-Hartree-Fock" (10.9) is named only.
4. Too slow: the normalization conversions are stated three times (10.1 body, after the box, D.29). Too fast:
   the relaxing-lattice derivation (10.2); the published-treatments paragraph (10.4).
5. Outcomes: I could carry out every inferred outcome of every section, and I reproduced each worked example's
   numbers.

**Overall.** I would keep reading. The chapter is long and dense, but each derived step closed when I did it,
and the cross-references to Chs. 3, 4 and 8 point to the right equations. The many numerical claims checked out
to the printed precision, except the slips listed above. The one place that could make a careful reader distrust
the text is the unexplained 15% gap between the "same" independent-particle rate in 10.1 and 10.2. A forward
pointer would remove it. Nothing blocks the material that follows.

Verdict: **MINOR GAPS**
