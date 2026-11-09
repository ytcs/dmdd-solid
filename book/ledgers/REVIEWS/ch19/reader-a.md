# Chapter 19 mock-reader review: persona (a), first-year PhD student
Source read: tex/ch19/*.tex (the PDF at build/main.pdf is current, 19:09, and newer than every ch19 source). I read it linearly
and checked every derived step by hand or with numpy/scipy/sympy (scripts in the session scratchpad). Earlier chapters were
consulted only via pdftotext of the pages before Ch. 19, to check whether a term had been defined.

## Chapter opener
- Every number checks: 200 MeV gives 21.1 eV; 21 eV gives 12.0 km/s; 2.35 A / 12 km/s = 19.6 fs. No lost points. The map
  figure caption is long but tells me where each piece goes.

## 19.1 Nuclear recoil on the Born-Oppenheimer surface
**Lost points**
- None that blocked me. The kicked Wigner function (19.1-wigner), the energy shift (19.1-dH) and the step "classical flow
  conserves H_cl, so the deposit reproduces the impulse approximation term by term" are clear and short.
- Small hiccup: E^kin_kappa = <omega>/4 is used per Cartesian component (the "rms per component" sentence). It is defined in
  Ch. 11, but saying "per component" in the sentence that gives 10.2 meV would save a check.
**Steps I could not reproduce**
- WE "harmonic-to-cascade boundary": "less than half the shortest phonon period of 67 fs". The book's own silicon optical
  phonon (64.1 meV, 15.5 THz, Ch. 5) has a period of 64.5 fs. 67 fs corresponds to 61.7 meV. The conclusion stands; the
  number does not match the book's own value.
- Everything else reproduces: sigma_omega = 0.715 eV (5.7 %); angle 1.64 deg; lambda_dB/l_R = pi<omega>/E_R; stiffness
  11.24 eV/A^2; 0.41 eV (x_R = 9.9); 0.54 eV; lambda_dB = 0.054 A, l_R = 0.42 A, correction 0.017; l_R(12.5 eV) = 1.49 A;
  v_N = 9.27 km/s; 25 fs; xi_M(20 eV) = 15.2, e^-xi = 2.6e-7; 0.87 keV, 4.6 keV; e^-xi(12.5 eV) = 4.6e-9; DM masses 28, 32,
  154, 262 MeV and 1.34 GeV; ZPE 30.7 meV/atom, 126 eV per 4096 atoms; harmonic mode shares summing to E_R; Boltzmann
  exponent 1.16e5. (eta_R^2 at 1 eV is 0.185, printed as "0.18". This is a rounding choice only.)
**Used before defined**
- c_3 "of eq. D.32" and the method appendices (E.11, E.17, E.23) are cited, but I can read past them. "p_FP": I inferred
  FP = Frenkel pair; one word would confirm it.
**Pace**
- 19.1-md (acceptance tests) is written for someone who will run MD. It is fast for me (ML potential, ZBL-type splice,
  quench at fixed cell), but I could follow what each test protects against. The partition key result is well paced.
**Outcomes**
- Derive the hand-over ensemble and its deposit: yes, reproduced. Compute the four regime numbers and boundaries for Si:
  yes, all reproduced. Write the partition and the heat form (19.1-heat), and say why E_st is configurational: yes.

## 19.2 Electronic excitation by the recoil
**Lost points**
- 19.2-soft and Fig. 19.2(b) caption: the free-gas fraction is said to "vanish at E_R,th", but the next numbers give the
  free gas 0.07 at 352 eV = E_R,th. Since p_min in (19.2-pmin) keeps the -m_e v_N term, the free-gas fraction actually
  vanishes at 336 eV (the v_N^2-kept threshold). I checked: 1-(p_min/k_F)^3 = 0.071 at 352 eV. I stopped here for several
  minutes. Fix: say "vanishes at 336 eV, the threshold with v_N^2 kept" or drop the m_e v_N term consistently.
- 19.2-kernel, last paragraph: "Ehrenfest dynamics with a hybrid functional, surface hopping with decoherence, multireference
  calculations". Ehrenfest and multireference appear nowhere earlier, and surface hopping only once. I can take them as names
  of methods, but the "nuisance = spread between three treatments" sentence then means little to me.
**Steps I could not reproduce**
- None that matter. Checked: crossing k = 2m_e(v_N+v_F) and omega_max (19.2-transfer); the moving-wall derivation;
  (19.2-Eth) = 351.5 eV, quadratic 335.9 eV (-4.4 %); Ge k_F = 1.736, E_F = 11.48, M/m = 132396, 399 / 387 eV (-3.1 %);
  omega_max(100 eV) = 0.63 eV; p_min(100 eV) = 3.37 A^-1 = 1.86 k_F; xi_M = 6.8 / 3.6 / 2.1; Born parameters 14.6 and 34.8;
  the 2P(1-P) double passage; 0.44 and 0.84 GeV; Lindhard 0.153 at 100 eV and 0.188 at 0.46 keV (ratio 1.38 to the 0.136
  datum); Ge Lindhard 14.3 %; Fano: Var E_el from the law of total variance gives sigma = 170 eV (18 %); Migdal 3.9e-4 and
  4.4e-4; 1/260; 0.6 % weight at 100 eV.
- Trivial: "0.78 at 2.9 eV" for omega_e/eps_eh gives 0.77 with 3.749 eV.
**Used before defined**
- Landau-Zener symbols are defined on the spot. Fine.
- "Migdal yield per recoil falls only in proportion to E_R" (19.2-migdal, last paragraph): the yield Delta Y_q is constant
  (just shown); what scales as E_R is the Migdal pair number per recoil. The word "yield" trips me after it has just been
  shown constant.
**Pace**
- Good. The Fano argument is the clearest part. The kernel subsection is method-heavy for my background (see above).
**Outcomes**
- Derive and evaluate the binary threshold for Si and Ge: yes. Explain why it is soft (momentum tail, level crossings):
  yes. Compute the Migdal share of a measured yield and say why adding a Migdal rate double-counts: yes. Use (19.2-FNR) to
  turn a Fano factor into an electronic-energy spread: yes.

## 19.3 Stopping of slow ions
**Lost points**
- WE "mean excitation energy of silicon", second paragraph: "Normalized instead to the exact (pi/2)omega_p^2 ..., the same
  data give 174 eV." If the tabulated spectrum holds 1537 eV^2 and is divided by 1514, the weights sum to 1.015, and
  ln I = sum w_j ln omega_j then depends on the unit of omega (I reproduce 174 eV = exp(5.082 x 1.0152) only in eV; in keV
  or hartree a different number comes out). As written, 174 eV is not a well-defined result, so I cannot tell what
  "inside this range" means. Fix: say what is done with the 1.5 % excess (e.g., removed from a stated band), or drop it.
- 19.3-bethe: "the prefactor 2Z_1^2 alpha/pi v^2 ... becomes 4pi Z_1^2 alpha^2 n_e/(m_e v^2) . (2/pi omega_p^2)". I had to
  rebuild what is meant: prefactor x (pi/2)omega_p^2 = 4pi Z^2 alpha^2 n_e/(m_e v^2). Stating it that way would be clearer.
- 19.3-assumptions: "the yield vanishes for E_R <= 2U", then with U = 0.15 keV "reaches zero at 298 eV". 2U = 300 eV.
  Presumably the fit value is 0.149 keV; as printed, it looks like an error.
**Steps I could not reproduce**
- The full numerical solution of (19.3-simple) with the TF cross-section (the 3 %, 4-5 %, 13 % and 10 % statements): not
  attempted, because the TF solution and the f_LSS table are needed. Everything I tried reproduces: a_L = 0.1375 A;
  c_L = 0.02436/keV = 11.5 Z^-7/3; impulse deflection theta = -I'(beta)/eps (needs the full -inf..inf path, which the
  definition of I from 0 hides, so I first got a factor 2 wrong); Rutherford f = 1/2x; k_L = 0.1458; Z^1/6 = 1.55;
  0.88/2.77/8.76 eV/A; 0.32 x 196 = 64 eV/A (23x); the reduction to (19.3-simple); the eps^1/6 asymptote with J = 0.4742 and
  3.29 k_L; the Bethe log algebra; 2m_e v^2 = 2.2 keV / 0.78 eV; Born 0.16 / 117; 0.60 v_F; damped-oscillator
  ln I = 3.011 (20.3 eV), f-sum fractions 88 / 7.8 / 2.4 %, 19.0 eV at 2 eV damping; omega_p(14 e) = 31.05 eV; L-shell
  two thirds, valence one sixth.
**Used before defined**
- None. The note separating the "Lindhard function" from "Lindhard quenching" helps.
**Pace**
- The impulse derivation of f_LSS is compact and needed paper; it is fair. The list of assumptions is well organized.
**Outcomes**
- Derive Lindhard's equation from the partition and get its low-energy eps^1/6 law: yes. Name the three unstated
  assumptions and why each fails below a keV: yes. Derive Bethe from the loss function and compute I for a model: yes;
  for the measured spectrum: yes, apart from the normalization point above.

## 19.4 Defects and stored energy
**Lost points**
- 19.4-calib, after (19.4-fDF): "it lowers the phonon scale and with it the reconstructed energy of every event". By my
  derivation (and by the minus sign in front of C_cal x_ER), a deficit in the calibrating electron recoils raises the
  reconstructed nuclear-recoil energy. 19.5 says "raises". As written, 19.4 reads as the opposite.
- (19.4-fDF) is quoted from 19.5 before it is derived. I derived it myself from the stated model and it is correct, but a
  reader who does not will be carrying an unproved formula for a page.
**Steps I could not reproduce**
- None. Checked: the hard-sphere counting equation, N_FP = (2/E) int N, and c = 1/2E_d; eps_L(36 eV) = 8.8e-4 and the
  ~80 eV edge; dsigma ~ T^-4/3; xi_d: I solved (19.4-count) for the pure T^-4/3 law and get 0.723 at 10 E_d and 0.706 at
  60 E_d, matching 0.72 and 0.70; 1 - y_L = 0.698 and 0.493; m_chi(300 eV) = 0.770 GeV; Y_q = 0.119; counts 3.67/2.94; stored
  18.3-20.2 eV and 22-26 eV; E_d = 24 eV gives 3.95; the electron's 12.4 eV transfer at 0.14 MeV; f_DF zeroth and first order
  and C_cal = 0.64-0.75; (19.4-bound); r = 0.9 gives 0.086; 1.153; table entries 0.20/0.28/0.23 (0.22); p_surv 0.95-1.04 and
  0.73-0.88; 6.9 % at 300 eV; 2.06 sigma; Ge 4.3 eV, 4.6 eV/eV, 28 eV, and 35/28/24 eV.
**Used before defined**
- None.
**Pace**
- Fine. The worked example at 300 eV is the most useful paragraph for my own analysis work.
**Outcomes**
- Derive Kinchin-Pease and explain why the screened factor is 0.70: yes (reproduced numerically). Estimate the stored
  energy of a sub-keV recoil: yes. Turn a measured defect fraction into a bound and state its conditions: yes.

## 19.5 The energy balance law
**Lost points**
- "flashing" ("which flashing keeps small"; "after flashing") is never defined in Chapters 1-19 (pdftotext search). From
  19.4 I guess it means infrared/LED neutralization of traps, but say so.
**Steps I could not reproduce**
- Heat-quenching numbers: with b = 0.52 exactly I get Y_ph(0) = 1.158, not 1.156 (b = 0.525 gives 1.156). Minor.
- Two-bias inversion: "an uncertainty of 0.005 on the 40 V ratio moves the inverted r' by 0.02". Solving (19.5-linear) with
  Y_40 = 0.9195 +/- 0.005 moves r' by 0.026. Minor.
- Reproduced: 33.9 pairs and 39.6 eV; 905 eV; 943 eV, 2.0 eV trapped; 59 us; g_L 1.07/26.7; 1.407 and 1.280; 1.017;
  1-b <= 0.035/0.036/0.041; both bimolecular solutions (19.5-bimol); the calibration identity (19.5-calib); C_cal 0.663 and
  0.402; first-order error at most 2.75e-3 (scanned); the exact bound (19.5-bound) (sympy: identity holds exactly); (19.5-widen),
  0.016/0.031; delta_gap = 0.048 and 0.0035; r = 1.153, band 1.123-1.178, 1.144; 1.077; 0.949/0.964/0.954; 40 V 0.9196 and
  0.935; determinant (Y-f)(g1-g2); high-bias limit 0.913.
**Used before defined**
- "flashing" (above). Notation drift: 19.4 writes x_ER where 19.5 writes d_ER and later sets x_ER = d_ER. It causes no
  error but needs a moment of matching.
**Pace**
- The Fermi-level paragraph is subtle but well argued. The release law with the 41 % example works well. The section is
  long; the two-bias part felt the right length.
**Outcomes**
- Write the balance law and check it reduces to the partition: yes. Derive the release law and say when unit heat
  quenching holds: yes. Derive the calibration identity and the stored-energy bound: yes. Design and invert a two-bias
  measurement: yes.

## 19.6 Delayed release and the low-energy excess
**Lost points**
- 19.6-defecton: localization criterion |grad phi| a > Delta_dfn with phi = V_0(a/r)^3 gives r < a(3V_0/Delta)^{1/4},
  not R_0 = a(V_0/Delta)^{1/3}. The quoted formula corresponds to |phi| > Delta. The crowdion numbers (18-43 spacings) use the
  quoted formula; the gradient criterion gives 12-22. Either the criterion or R_0 needs a sentence.
- Symbol clash: omega_p is the plasma frequency in 19.3 (16.6, 31.05 eV) and here the 60 meV accepting mode of the
  energy-gap law, in the same chapter.
- After (19.6-D): "The bracket of eq. (19.6-D) expands as 1 - (5/16)(A/T)^2". The bracket [1 - I_0^-2] goes as y^2/2. It is
  D/D_9 that expands as 1 - 5y^2/16 (I verified this, and 5/576 in Delta units).
**Steps I could not reproduce**
- E_PN values (1.2e-4 to 3.6e-7 eV) and the Mathieu bandwidths (90-166 ueV, 13-34 ueV): these need eq. C.20-EPN and a Mathieu
  solution that the chapter does not give. Not attempted.
- The T^-9 four-step argument (cancellation of the two time orderings): accepted on trust.
- Reproduced: lambda_tun = 27.5, x4/3 = 36.7; 47.2 and 23.6; 14 % and Al 25.2 / 6 %; energy-gap factor 2.7e-15 (+16.8), so
  6.8; ln factor ~443 for 7 eV; the sum-rule proof; WE rates, 38.5 days, 0.953, p_B = 0.902, p_0 = 0.098, hops 0.9525 /
  0.0474 / 0.0505, 4.474 eV, 1.05 hops; 10 and 100 years (5.539 eV in 1.43 hops; 6.994 eV in 1.95 hops); sensor events
  1.05/1.75/0.70 eV; TLS mean quantum 1.187 T (0.49 meV); Fig. 19.5(b) 6.5 h, 3.6e5 yr, 0.389 in one year; pocket 3 eV;
  0.78 meV; 152 eV = 22 pairs; the defecton Fokker-Planck derivation to (19.6-D) step by step; alpha_P = 1.27; 0.28 and 0.93
  Delta (0.899 and 0.990); local exponent -7.91; the crowdion d_k, E_kink, M_cr; recoil energies 0.117/0.166 meV; the
  discreteness correction -a^2/72d^2; the Borel tail and its cutoff.
**Used before defined**
- S_pol(T) "of eq. E.22-Spol" is defined only in an appendix. "Nudged elastic band", "kinetic Monte Carlo" and
  "Peierls-Nabarro barrier" appear without a gloss (the last only through eq. C.20).
**Pace**
- The sum rule and its worked example are excellent. The defecton and crowdion subsections are fast and feel like
  excursions; they kept my attention, but I could not say how either changes a detector rate. The LEE subsection is clear,
  and the energy-conservation bound is the strongest argument in the chapter.
**Outcomes**
- Solve a small release network and verify the sum rule: yes. Decide with (19.6-window) whether a defect releases within a
  run: yes. Derive defecton diffusion from k-space diffusion: yes. Bound the LEE by energy conservation and argue for elastic
  energy: yes. Crowdion band: only partly (needs C.20).

## Overall
I would keep reading (the Summary section matches the body). Nearly every number in the chapter reproduces, and the chain partition, then Lindhard/Bethe as limits,
then stored-energy bounds, then the balance law, then the sum rule hangs together. Nothing blocks the following material. The
real gaps are local: the 174 eV normalization in the I_bar example (unit-dependent as written), the R_0 formula against its
stated criterion, the free-gas fraction "vanishing at 352 eV", the sign of the C_cal sentence in 19.4, "flashing" undefined,
the omega_p clash, plus four small numeric mismatches (67 fs, 2U = 300 vs 298 eV, b = 0.52 vs 1.156, 0.02 vs 0.026).

**Verdict: MINOR GAPS**
