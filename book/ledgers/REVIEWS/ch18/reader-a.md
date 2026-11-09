# Chapter 18 mock-reader review: persona (a), first-year PhD student

Read: tex/ch18/*.tex linearly (ch18, s18-1 to s18-5, summary), cross-checked against build/main.pdf
(pp. 1019 ff.; figures 18.2 and 18.7 inspected as rendered). Prior chapters 1-8, 10-17 as already read.
Checks done in sympy/mpmath/numpy (scripts in my scratchpad, not in the repo).

## Global items (all sections)
- **Forward references render as "??" in the PDF.** 15 occurrences in Ch. 18: sec 19.5 (x3), chap 20 (x3),
  sec 20.1 (x4), sec 20.2, sec 21.6, sec 21.7 (x3). Presumably later chapters not built yet; a reader sees "??".
- **Two calibrations of the same model, explained late.** 18.1 (fig 18.2 caption, end of 18.1.4) uses
  Eg = 1.17 eV and A_AB = 5.2 "chosen to reproduce the measured pair energy". 18.2.1 then uses Eg = 1.160 eV and
  A_AB = 5.674 eV^3, "the one constant fixed by the measured pair energy (sec 18.4)". Reading 18.2 I thought one
  of the two was a typo. The reconciliation (5.2 is the Alig fit used by R-K at 300 K; 5.674 is the 123 K value)
  arrives only in 18.4.1, with a partial aside in 18.3.2 ("the calibrated constant lowers them by less than 0.03").
  Fix: one sentence at the first appearance of 5.674 in 18.2.1.
- Units of A_AB: fig 18.2 caption gives "A_AB = 5.2" with no unit; 18.1.4 later says eV^3.

## 18.1 The carrier cascade
**Lost points**
1. 18.1.1, last sentences of the paragraph after the key result: "The element-wise imaginary part of W_GG' agrees
   with it only when W_GG' = W_G'G, which holds in Si and Ge with the origin at an inversion center but not in
   GaAs." I followed the algebra ((W - W^dagger)/2i vs Im W) but not why the G-sum then is still real for GaAs
   while the element-wise version is not; one line showing that the bilinear form rho* A rho with Hermitian A is
   real would fix it.
2. 18.1.2, polar crystals: the three matching conditions (Born charges, multipole order, Gaussian cutoff) are
   stated, not shown. For me this is a level jump (quadrupoles in g^L were only briefly in 6.2). Not blocking,
   since silicon has Z* = 0.
**Steps reproduced**
- Eq. (18.3) threshold: m v0 = (2m+M)u, x = Eg + x m/(2m+M) gives theta = (2m+M)/(m+M). Equal masses 3/2. OK.
- Eq. (18.2) from (18.1): -2 rho* Im W rho with W = v eps^-1 gives 2 v |rho|^2 L. OK.
- Pauli/Coulomb estimates: 2.0e23/12 = 1.7e22 /cm^3/eV; 267 pairs in a 10 nm sphere = 6.4e19 /cm^3;
  fraction 3.8e-3; n a_x^3 = 4.7 (1 keV), 0.47 (100 eV). All reproduced.
- Energy identity: G(lN, lH) = e^{lH w} G(lN - lH Eg, 0). OK.
- WE 18.1 (toy): G2 = 19/25 s + 6/25; G_Lambda = s(361 s^2 + 228 s + 36)/625; P = 36, 228, 361 /625;
  mean 63/25, variance 228/625, w/mean = 1.98, F = 0.145; heat on each path = 2 - N. All reproduced.
- Dirichlet integral Gamma(3/2)^3/Gamma(9/2) = 2 pi/105. OK.
- Fig 18.2 caption: 27 = 1 + 2x13 carriers; heat 50 - 13x1.17 = 34.8 eV. OK.
**Could not reproduce**: none of the derived steps. The Monte Carlo numbers (13.06, 2.997, 2.712, 3.029, the
percentages) need the simulation; not attempted.
**Used before defined**
- "Alig-Bloom model" and the subscript AB (omega_AB, A_AB) appear in the fig 18.2 caption and 18.1.4 without saying
  who/what Alig-Bloom is; eq. (E.87) is in an appendix. One clause would do.
- "random-k" appears in the section opener and fig 18.2 before 18.1.4 defines it; the opener's one-line gloss
  is enough.
**Pace**: 18.1.1 is dense (Umklapp sum, matrix FDT, local fields, z_qp, vertex corrections in two paragraphs);
18.1.3 and the toy are at the right speed, and the toy is the most useful thing in the section.
**Outcomes (inferred)**
- Write impact ionization as a master-formula rate and reduce it to the loss function: yes (done above).
- Derive the momentum-conserving threshold: yes.
- Set up the backward equation and solve a finite cascade by generating functions: yes (toy reproduced).
- State the energy-only and random-k reductions, and what each assumes: yes, including why silicon violates
  the first above 3-5 eV.
- Explain why the seed's split matters at a few pairs (nonlinearity of G_t): yes.

## 18.2 Mean energy per pair and the Fano factor
**Lost points**
1. 18.2.6, eq. (18.14) (tagged-unit formula). The sum over j runs over "the kinetic energies of the successive
   carriers that hold it". With phonons, the same carrier holds the unit across many phonon emissions. The
   weight 1/x is given only at ionizations, so the sum must run over the ionization events along the unit's
   chain, not over carriers or over all collisions. As written I could read it either way, and the two give
   different answers. Fix: "the kinetic energies x_j at which the successive holders of u ionize".
2. Grid step: Eg/74 here vs "halving the grid step from Eg/73" in 18.4.1. Is this the same calculation?
3. Parking limit box (fig 18.5): the ratio there is lambda_AB/(x - Eg) for a constant DOS, so A_AB carries eV, not
   eV^3, and lambda_AB = A_AB/Eg^3 no longer fits that case. Say what lambda_AB means in this kernel.
**Steps reproduced**
- (18.10), (18.11) as identities. OK.
- Poisson estimate of V_>: 0.0543 x 0.93/1.16 = 0.0435; 0.291/0.043 = 6.7; covariance removes 0.269/0.291 = 92%;
  1% in V_> moves F by 2.6%. OK. Also lambda_AB = 5.674/1.16^3 = 3.635; 3.232 x 1.160 = 3.749.
- Dashed curves of fig 18.3: Var/n = F(1 + c eps/(F w))/(1 + b eps/w). OK. b_N eps/w at 10 eV = 13%. OK.
- WE 18.2 (random parking): Laplace step, ODE phi' + 2e^{-s}phi/s = -1/s^2, integrating factor e^{-2E1}, and
  phi -> rho/s^2 all reproduced. rho_inf = 0.74759792025 (mpmath). Gap law: int G = rho_inf, int (1+g)G = 1,
  <g> = 0.3376174, Var g = 0.0794372, F_ren = 0.0443977, ratio 0.870. All reproduced.
- I also solved the parking moment recursions myself (grids 0.02, 0.01, extrapolated): rho -> 0.7476,
  F -> 0.0510. Agrees with 0.0510387.
- Shockley uniform population: mean 9/10, variance 27/175, F at fixed N 54/175 = 0.31, at fixed w 27/686 = 0.039.
  OK.
**Could not reproduce**
- Small wording point in WE 18.2: "At small s, E1(s) = -gamma - ln s + Ein(s)" is exact for all s > 0. Because
  it says "at small s" I first worried that using it under the t-integral out to infinity was an approximation.
  It is not; say "exactly". The step from m(s) ~ rho/s^2 to M(x) ~ rho x is a Tauberian step and is presented
  as immediate. Fine for me, but a footnote would help.
- 18.2.6, the linear-yield proof (renewal in ln x): accepted on trust, deferred to App. D.44. I did not check D.44.
**Used before defined**: none blocking. "Key renewal theorem" relies on App. C.11, which I had read.
**Pace**: about right; the 18.2.3 prose repeats numbers readable from fig 18.4.
**Outcomes**
- Express eps_eh and F_eh as moments of the heat: yes.
- Decompose F into V_<, V_>, 2V_<> and explain the large cancellation: yes (the run-length argument is clear).
- Derive the random-parking pair energy: yes, reproduced.
- Explain why the renewal estimate divides by eps_eh^2, not Eg^2: yes (the constraint at fixed w).
- Explain why the mean yield is linear: qualitatively yes; the precise statement is blocked by lost point 1.

## 18.3 Seeding and the phenomenological models
**Lost points**
1. 18.3.3: "b_N ... is 0.015 for the uniform split ... (lim 18.2a)". Lim 18.2a gives only 0.35 for the one-sided
   seed. Where does 0.015 come from?
2. WE 18.3, dark-matter seed: P(1) = 0.830 etc. needs the seed distribution, which is not tabulated. I can follow
   the method but not check the numbers. Acceptable, but a one-line histogram of the share (or "see fig X") would
   let me reproduce it.
**Steps reproduced**
- (18.19) law of total variance: OK. 0.283 + 0.031 = 0.314; from the rounded P(2..4) I get 0.307, consistent.
- WE 18.3: p_ii from (18.8) at 2, 2.5, 3, 3.5, 3.84 eV = 0.0041, 0.0185, 0.049, 0.100, 0.146; 43 steps;
  P_no = 0.1747; integral form -1.744, giving 0.1749; equal split P_no(1.92)^2 = 0.981 ("98%"). All reproduced.
  (-ln(1-p) ~ p/(1-p) is only first-order accurate; it happens to agree here.)
- Step model: 1 + floor(3.84/3.749) = 2; mean (w - Eg)/eps + 1/2 = w/eps + 0.19. OK.
- sigma_N at 20.2 eV = 0.78; 2.627 pairs gives 3.81 eV per pair (1.5% high); step model mean +14%; 1/0.170 = 5.9;
  photon P(2) +12%. OK.
**Used before defined**: d_TV defined at first use, good. P_det, marks: defined in place.
**Pace**: the text after lim 18.3a repeats the box's numbers (4.37, 12.95, 0.86, 0.39, 0.21); cut by half.
**Outcomes**
- Build P(N|q,w,v) from a seed distribution and cascade tables (18.18): yes.
- Separate the seed and cascade contributions to the variance: yes.
- Show the step model and R-K as limits, and where they fail: yes. WE 18.3 makes the 5 eV case concrete.
- Know which seed a photon calibration measures, and how large the error is: yes (<= 0.062 in d_TV here).

## 18.4 Pair energies in Si, Ge and GaAs
**Lost points**
1. 18.4.4 and lim 18.4a: the figure is the theta = 3/2 cascade at silicon's lambda. "Silicon, at 3.64, sits almost on
   that point; Klein's form differs from the cascade by 0.2%". But the calibrated silicon model of tab 18.1 has
   theta = 1, with E_res = 0.716 Eg (18.4.4 itself). So which model is "silicon" here? Fix: "the theta = 3/2 cascade
   at silicon's lambda_AB" (where A was recalibrated to 5.604, per fig 18.6).
2. Sensitivity sentence: "Raising A_AB by 10% raises eps by 1.2% and F by 0.65%." From the slopes quoted three
   paragraphs earlier (d eps/dA = 0.090, dF/dA = 0.0016) I get 1.36% and 0.80%. Perhaps a secant at Eg = 1.160
   rather than plane slopes at 1.124; please say so.
3. Validated range "lambda_AB <= 14" while germanium, one of the defining crystals, has 14.3.
**Steps reproduced**
- lambda and w for Ge (14.3, 0.051), GaAs 300 K (1.98, 0.026), and every row of tab 18.2; residuals; mean +8.0%,
  rms 12.2%. OK.
- Shockley split 1.160 + 1.661 + 0.928; E_res = 0.716 Eg; 14.7 phonons. OK.
- (18.24)-(18.26): 3/5 theta Eg, 14/5. Uniform vs cascade: 2.2/1.585 (+39%), 2.8/2.056 (+36%); E_res 0.293, 0.528. OK.
- Diamond lambda = 0.035; Klein 15.3 + 0.5-0.6 = 15.9 eV. OK.
- Exponent 1 - 3.9666 x 0.2404 = 0.046; k2(Si) = 1.87 eV. OK.
- WE 18.4 (GaAs): 1.616, 0.02391, 0.04377, 0.4713, 2.715, 4.13 eV; k2 = 1.67; empirical 4.23; Klein 4.76;
  300 K gives 3.96 eV. All reproduced.
**Used before defined**: r_K, omega_K defined in place; Klein's relation introduced in 18.2.5 with a forward
pointer, then defined here. Fine.
**Pace**: good; the caveat on the R-K cross-check (18.4.2) is helpful.
**Outcomes**
- Calibrate the one constant and state what is then predicted: yes.
- Derive Shockley's balance and Klein's 14/5 from the cascade, and say which assumption fails: yes.
- Use the linear law to estimate a pair energy for a new crystal: yes (GaAs redone).
- Say whether a crystal lies in the validated range: yes, from tab 18.2 and the stated box.

## 18.5 The end of the cascade
**Lost points**
1. Fig 18.8 discussion: "half of the gap energy has returned to the lattice at 0.83 us". At 0.83 us,
   r_gap = 0.5, but 5% of the energy is already trapped, so the lattice holds about 0.45. Likewise, a window
   closing at 1 us misses 42% (held) plus the 5% trapped. Say "has left the pairs and excitons".
2. N_eh is redefined here ("counts electrons in the conduction band, free or bound"). Later F_eh, F_heat and
   F_meas all appear. This is consistent, but I had to reread to see that an exciton changes F_meas and F_heat
   but not F_eh. A three-row summary (which readout sees which F) would help.
**Steps reproduced**
- f_cap = 0.005/0.886 = 0.56% (0.34-0.79%); eps shift 0.57%. OK.
- r_C: alpha/eps0 = 0.126 eV nm; 1.26 nm, 5.0e-14 cm^2; 0.36 nm, 4.1e-15 cm^2; mfp 20 cm at 1e12; 29 um at 50 mK. OK.
- WE 18.5: 25.80, 26.97, 1.124 eV, 4.17 eV (+11.1%), F' = 0.207, sigma 1.09 to 1.37, variance 0.96 + 0.90. OK.
- (18.33) from Var(E_np + E_x N_X); the all-bind limit (1 - E_x/Eg)^2 = -2.5% (Si), -1.3% (Ge). OK.
- r_E = 0.56 um (4 V/cm), 0.11 um (100 V/cm); exciton field 3.5e4 V/cm; Poole-Frenkel 2.25 meV; exponents
  1.06e4 and 1.0e4. OK.
- Rate equations: I solved them with the caption's rates. B peak 0.145 at 0.446 us; r_gap = 0.5 at 0.833 us,
  0.01 at 4.41 us, 0.42 at 1 us; weights +1.278, -0.329, +0.050; split 0.050 / 0.009 / 0.941. All reproduced.
**Used before defined**: Auger decay of the bound exciton, explained in place. "Electron-hole droplets" in
18.5.4 is mentioned once and never defined (an open-problems list, so harmless).
**Pace**: right; the capture bookkeeping (three shares adding to Eg) is the clearest paragraph of the chapter.
**Outcomes**
- Book a captured electron and a bound exciton in energy and pair number: yes.
- Apply binomial thinning to eps and F, and know when it fails: yes.
- Compute F_heat for full binding, and r_E for a given field: yes.
- Solve the linear rate equations for the branching fractions and r_gap(t): yes (redone numerically).

## Overall
The summary and tab 18.3 match the body in every number I checked.
I would keep reading. Every derivation I tried came out: the threshold, the kernel reduction, the toy and
random-parking generating functions, the renewal and Shockley/Klein algebra, the step-model probabilities at 5 eV,
the GaAs linear law, the capture/exciton bookkeeping and the rate-equation solution. The main friction is
bookkeeping, not physics. First, two calibrations of the one constant (5.2 at 1.17 eV, 5.674 at 1.160 eV) are
reconciled only in 18.4. Second, eq. (18.14) is ambiguous about which events enter the sum. Third, the
"silicon" point of the Klein box is a theta = 3/2 model, not the calibrated one. Fourth, there are small
loose wordings (r_gap vs lattice, b_N = 0.015 unsourced, sensitivity percentages that do not follow from the
quoted slopes). The forward references to Chs. 19-21 print as "??". None of these blocks the later material.
**Verdict: MINOR GAPS**
