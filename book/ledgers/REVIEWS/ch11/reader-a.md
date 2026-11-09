# Chapter 11 mock-reader review: persona (a), first-year PhD student (isolated)

**Text read.** build/main.pdf (Nov 1) is older than the sources (Nov 2), so I read tex/ch11/ch11.tex, s11-1 to s11-9 and appD/D-31, D-32 linearly. Ch. 1-8 and 10 count as read. App. A.8, C.3, C.10, C.18, D.14, D.15 and E.* count as **unread**. I reconstructed what I needed from them, and I mark where that was impossible.
**Checks.** sympy/numpy with the SHM of Sec. 1.2 (v0 = 238, vesc = 544, vE = 250.5 km/s, vmax = 794.5 km/s), the elastic tensors as quoted, and the stated phonon frequencies. Numbers that need the PBE DOS, the force constants or the He cell model could not be checked (marked "no inputs").
**Reproduced** (each checked against the text). Edge 6.1/6.39 keV (Si), 10.2 (Ge), 3.1 (C); kappa_eta = 3.14 / 3.09; I0 = 5.32e-7; eta(0) = 1/287.9 km/s; R/R_light = 0.148, 0.591/0.546 (x9), 0.625 (x10), 0.902/0.907 (x44); heavy plateau 654 /kg/yr; c̄_LA = 9.017, 1/<1/c> = 9.011, coefficient 8.956, c_max = 9.352 km/s; Ge 5.36/5.313, C 18.20/18.16; densities 5.34, 3.52; Theta_D = 648/655/641 K (Si), 375 K (Ge), 2248 K (C); Rayleigh floor 6.48 km/s; Z*/eps_inf = 0.1938; I_pol(GaAs) = 0.822 / 0.759 meV; 0.170 and 19.0 meV cm3/g; edges 10.35, 21.98, 2.85 keV; Poisson-tail numbers of we:11-tail (all three q); 47 % energy share at 50 keV; impulse width 88.4 meV, 265 m/s, 1.15 km/s; onsets 92.5/138.8 keV (Si), 113/170 keV (Ge); fermion factors 16x, 1 - m/M, 1 - 2m/M, Helm zero 256 MeV; toy model: E_kin = 1 - 44l3^2 + 12l4 (exact diagonalization), n=2 ratio 1 + 16l3^2/k^2 (+50 % at q_BZ), n=3 crossover; MK nodes 59.8/191.1/371.3 meV with weights .191/.670/.139; B-L: b̄ = 0.50235, sigma_b^2/b̄^2 = 1.88e-4, <delta^M>_b = -0.054, Gamma_iso = 1.37e-2 eV, Gamma_EM = 2.96e-6 eV; g_md = 2.0e-4; Upsilon_2/0, Upsilon_4/0 at 300-700 km/s, sign changes at 196, 138 and 435 km/s; Y4c range -0.43/+0.65, 0.640 at h = 0, 1.83 factor; GaAs scalar d = -1.21e-3, bracket 0.226, 8.2x, 6.7-9.0x, PBE /250; zeta = 2.9e-17 (GaAs) and 1.0e-17 (sapphire); resonator P_n prefactor 32; bar response (pi^2/24 vs 4/pi^2); sigma_lnR = 2.4e-3.

---
## 11.1 Acoustic phonons
**Lost points.**
- eq:11.1-master. omega_q (the energy the DM loses) sits next to omega_{Qnu} and omega_{qnu} = c_nu q (phonon frequencies). I had to go back to Ch. 8 to see which is which. Fix: write the DM argument as omega_q^chi, or restate it.
- "In silicon the rate reaches 90 % of the plateau value, 654 events..." reads as if 654 were the 90 % value. I computed 654 from eq:11.1-heavy, so it is the plateau. Fix: put "(plateau 654 ...)" in parentheses.
- Sound-speed subsection. eq:C.18-cubic, eq:C.18-rayleigh, Voigt ordering and the Christoffel quadrature all live in App. C.18. I re-derived the [100]/[110]/[111] eigenvalues and the first-order s_Q form, so this did not block me.

**Could not reproduce.** None in the derivations. Figures limit11_1a/b/c and the PBE value 8.83 km/s have no inputs.
**Used before defined.** "quasi-transverse" (pointer to C.18 only). "Zener ratio" is fine. "Hill average" is fine.
**Too slow / too fast.** Too slow: the m_p vs m_u reconciliation (1.5 %) and the Debye-temperature convention paragraph are long for this reader. The light-mediator expansion (kappa_eta) is well paced.
**Outcomes.** (i) Derive S^(1) and its long-wavelength form: yes (did the A_cell/M_cell algebra, 1/4 prefactor). (ii) Compute the acoustic edge and the light/heavy limits: yes (6.1 keV, 654 /kg/yr). (iii) Sound speeds from C_ij: yes (9.017 km/s).

## 11.2 Optical phonons in polar crystals
**Lost points.**
- The paragraph "The same eigenvectors change the nucleon vertex... |a_N| = 0.24 ... 0.61 and 4.5" is dense, rests entirely on we:8-nucleon, and is a digression from the charge row. I could not judge it. Fix: move it to a footnote or to Ch. 8.
- Two halo names appear: "standard halo of Sec. 1.2" in 11.1 and "halo of App. A.8" here. My numbers agree with the same SHM, but the text never says the two are the same.

**Could not reproduce.**
- **eq:11.2-Ipol for sapphire.** The stated upper bound, (pi/2)(1/eps_inf - 1/eps_0) omega_T,max (eps_0/eps_inf)^{1/2}, gives **45.6 meV** with the quoted frequencies. The text says [15.9, **37.1**] meV, and 37.1 = (pi/2) Sum w x omega_L,max, a tighter bound that is not stated. The lower end 15.9, I_pol = 36.4 and 95.1 % I reproduce.
- Sapphire eps_0 - eps_inf from the factorized model: I get 6.63, the text says 6.58 (minor).

**Used before defined.** "dynamical quadrupoles" (App. E.5 only, never defined in the text). "proper response" (Ch. 8, fine).
**Too slow / too fast.** The Sherman-Morrison step is well paced. The lower-symmetry paragraph (zeros between poles) is fast but optional.
**Outcomes.** (i) Loss-function lines from the full dynamical matrix: yes (re-derived L with the i0 prescription). (ii) Band integral and Z*/eps_inf from the splitting: yes (0.759 meV, 0.194, the error budget 0.9 % / 1.0 %). (iii) Why rate and reach reverse (LiF vs GaAs): yes (112 = 29 x 40 x 0.21 x 0.45; edges).

## 11.3 Multiphonon response
**Lost points.**
- Two different "0.44"s in adjacent paragraphs: j_BZ of a bond, and the bond correlation coefficient of the longitudinal displacements. I first took them for the same quantity. Fix: name one of them differently.
- Kahn et al. q_0^2 = 2M omega_0 reuses q_0, which is alpha m_e everywhere else in the book.

**Could not reproduce.** None in the derivations. D.31 supplies every step: the first moment from completeness, the j_BZ = 3j_1(x)/x value 0.4435 with four bonds giving 1.78, the Cauchy-Schwarz band, the pi^3/k integral and the TDS prefactor 1/16. delta^coh values, Fig. 11.3, the 17 % bin agreement and the 1.07 at 293 K have no inputs.
**Used before defined.** None. "Thermal diffuse scattering" is explained in place.
**Too slow / too fast.** The charge-vertex subsection is fast and abstract ("G_alpha times the density": a factor -i is suppressed). Otherwise the pacing is good.
**Outcomes.** (i) Write S at all orders and the n-phonon term: yes (D.31). (ii) When the incoherent approximation holds, and the first-moment shares: yes (47 % at 50 keV). (iii) Poisson tail above threshold: yes (6.1e-7, 6.2e-4, 1.7e-2 reproduced). (iv) TDS 1/|q-G| bound: yes.

## 11.4 Impulse limit and free nuclear recoil
**Lost points.**
- Two onsets compete: "fails below about 90 keV" (intro, x_R = 4) and "within 10 % from x_R = 2.3, q >= 70 keV" (box). The text explains this later, but the intro sentence misled me at first.

**Could not reproduce.** None. The width, Doppler reading, skewness 0.55, shift of 24 meV, Ge estimate 23.6 meV, free-recoil rate (D.32) and absorption slope 1 + q/M all check. Fig. 11.4 peak positions (0.36/0.81 E_R) have no inputs.
**Used before defined.** None.
**Too slow / too fast.** Well paced. The "slope 1 + q/M" of the absorption line is deferred to D.32, where it is one line. Fine.
**Outcomes.** (i) Impulse width from E_kin: yes (88.4 meV). (ii) Recover the Lewin-Smith rate as x_R -> inf: yes (D.32 steps). (iii) Absorption on nuclei in a crystal: yes (1 - e^{-2W} = 0.061 -> factor 16).

## 11.5 Anharmonic and quantum-crystal corrections
**Lost points.**
- **The Markov-Krein subsection depends on App. C.10**, which I have not read. "Canonical representation through xi", "Christoffel function", "the leading coefficient of the kernel K(.,xi) changes sign and a node passes through infinity", the red bars and eq:C.10-stieltjes were opaque to me. I reconstructed the three-node construction myself from five moments (nodes and weights reproduced). Fix: give that construction in two lines here.
- "E_kin changes by -0.14 to +0.08 %". With the quoted ranges l3 = 0.006-0.01 and l4 = (2-3)e-4, the extremes are **-0.20 % to +0.20 %**. The two quoted values belong to the specific pairs (0.01, 2.5e-4) and (0.006, 2e-4) of the box caption. Fix: name the pairs.
- "The first three hold at any temperature" (eq:11.5-moments). D.32 proves mu̅_3 only at T = 0. I checked that cyclicity with a state commuting with H gives the same <D^3> + 1/2<[D,[H,D]]> at any T, so the claim is correct but its proof is one line missing.

**Could not reproduce.** The helium cell model (r_L = 0.23, 0.117, 0.094, the 17 cm3/mol and 6.5 cm3/mol crossovers): no inputs (no Morse range parameter). I could not check the half-line windows 0.65-0.85 E_R.
**Used before defined.** "Kubo-transformed correlations", "ring-polymer/centroid MD" (open-problem paragraph, acceptable). In "lambda_3^nu k^{2i}", nu is an exponent, while nu is the branch index everywhere else.
**Too slow / too fast.** Too fast: the MK band (above) and the cubic-decay paragraph that brings in the off-shell gamma(omega). The toy-model perturbation theory is a model of good pacing: I reproduced 2sqrt2 l3, 16l3^2/k^2 and 6sqrt2 by hand.
**Outcomes.** (i) Exact moments and the q -> -q selection rule: yes (derived mu̅_3, mu̅_4, oscillator check 3mu̅_2^2). (ii) Few-phonon anharmonic counting: yes (+50 % at q_BZ, crossover 1.6 keV). (iii) Use an MK band: partly (nodes yes, half-line sharpness no). (iv) Judge the He quasi-harmonic validity: only from the stated r_L thresholds.

## 11.6 Nuclear-spin and isotope couplings
**Lost points.**
- Forward references to Sec. 11.8 ("coupling-to-mass cancellation of sec:11.8-single", "zone-center absorption of sec:11.8"). The text re-explains the cancellation in place, so this did not block me. Fix: make 11.6 the place where the cancellation is first stated.
- Pair-term paragraph (t_j, (G^2)_II): dense. I followed it only because I knew the T-matrix.

**Could not reproduce.** The local-mode threshold delta > 0.22, the 51 % at 65.1 meV, h_iso(50 meV) = -1.55, the 1.78 and 0.72 peaks: no inputs (PBE DOS). The derivations (Lifshitz/Dyson, first order h_iso, random-vertex average, Gamma_iso, Gamma_EM, the 5.0e3 ratio, the n2 - n1 >= 0 bound) all reproduce.
**Used before defined.** zeta (Sec. 10.7, fine). sigma_1 = omega eps_2 (stated).
**Too slow / too fast.** Good pacing. The B-L worked example is exemplary.
**Outcomes.** (i) Broadband response of a random vertex: yes. (ii) LDOS of a mass defect: yes (formula). Numbers have no inputs. (iii) Isotope vs EM channel for B-L: yes (1.37e-2 eV, 2.96e-6 eV).

## 11.7 Anisotropy and daily modulation
**Lost points.**
- The symbol u is the velocity vector u = v + v_E and also the cosine u = q̂.v̂_E in the same displayed equation, and in 11.1 it was q/2m_chi. Fix: rename the cosine.
- we:11-daily says every q <= 2.84 q0 "lies inside the range of the electronic model", but the model was said to stop at 2.8 q0 (two paragraphs earlier and in the box).
- "at q = 1.79 q_BZ, at the shell |G_111| = 3.95 keV": 3.95/2.25 = 1.76.

**Could not reproduce.** L_4/L_0, S_4/S_0 values, R_4/R_0 = 4.9e-3 and 3.2e-3, the sapphire 0.6 %/7 %/12 % and the 3000-orientation scan: no inputs. Radon transform, the q/4pi^2 prefactor, Upsilon_0 = eta, the odd-term interference, the cubic-harmonic values, the A_day factor 1.83, eq:11.7-dw and the P_2 range 0.997 to -0.495 all reproduce.
**Used before defined.** "Lebedev grids" (App. E.16 pointer only). Cubic harmonics Y^c_l (App. C.3, unread): I normalized Y^c_4 myself.
**Too slow / too fast.** The literature correction (dipole vs l = 4) is valuable and well argued. The nuclear-anisotropy paragraph is fast, with many numbers per sentence.
**Outcomes.** (i) Rate as halo multipoles x response multipoles: yes. (ii) Selection rules (no odd, no l = 2 in cubic): yes. (iii) Estimate A_day for a mounting: yes, given the R_l (1.83 x R_4/R_0).

## 11.8 Absorption on phonons and acoustic modes
**Lost points.**
- **Mitridate electron counts.** The rigid-ion structure is quoted as Z - Q/eps_inf (30.724/33.276, giving 8.2x), then "their GaAs projection takes the electron numbers 28 and 36". 28/36 = Z -/+ Q, presumably the proper (unscreened) count before the (1 - 1/eps_inf)Q shift, but the sentence does not say so. Taken literally, 28/36 in eq:11.8-d gives d = -0.079 and a rate ~4000x, not 7-9x. Fix: say which count enters where.
- eq:11.8-shift. I could reproduce it only after **assuming** the rank-one form R = R̃_ab + v_C R̃_aZ R̃_Zb / eps with eps = eps_inf - v_C x from Sec. 8.4. With that assumption the x_a x_b, linear and chi chi terms (constant v_C chi chi/eps_inf) all come out. Fix: restate the form.
- Sapphire band integral is 35.9 meV here but 36.3 meV (ordinary axis) in 11.2, with no explanation (polarization-averaged?). "The same comparison as for scattering (Sec. 11.2)": 11.2 compared LiF with GaAs, not sapphire.

**Could not reproduce.** Q_DM = 1.34e6 at 256 km/s, and the PBE Z* = 2.094 (taken as given). Everything else checks (d, 0.226, 8.8x sensitivity, 0.1501, Lorentzian peak 1.33, zeta 2.9e-17, f_sh, the mode normalization, the 32 prefactor, Q_eff -> (pi/2)|d eta/dv|, the bar solution, sum 4/(pi^2 n^4) = pi^2/24).
**Used before defined.** "phonon polariton" (Sec. 5.5, fine). Fraktur Q for the quality factor next to Q for wavevector (clear from context).
**Too slow / too fast.** Too fast: the "do the algebra once for any rows" paragraph. Too slow: none. The resonator and bar subsections are clear.
**Outcomes.** (i) Site coupling Z - Z*/eps_inf and d: yes (GaAs numbers). (ii) Dark-photon line area and reach: yes. (iii) Resonator power and the Q_eff regimes: yes. (iv) Resonant-mass omega^2 drive: yes.

## 11.9 Nuisance parameters
**Lost points.** None blocking. "Free recoil 6.8 % lower": 4.91/5.26 is 6.65 % (rounding).
**Could not reproduce.** The central 5.26e3 and 110 /kg/yr, the dilation coefficients 0.12 and 2.2, the 1.9 % Gaussian difference, and the MK 0.19-0.95 at 80 keV: no inputs. The quadrature, x_R values, eta_anh^2 = 2.4e-3, 0.15 meV and 1.0024 all reproduce.
**Used before defined.** None (Sec. 8.8 classes recalled).
**Too slow / too fast.** Slow by design: it repeats numbers from 11.1-11.8. The table is useful. The Summary repeats them a third time.
**Outcomes.** Assemble a nuisance band from templates: yes (sigma_lnR = 2.4e-3 from the three entries).

## Appendix D.31 and D.32
Both read cleanly and fill every step that Sec. 11.3 and Sec. 11.4 defer, including the first-moment proof, the zone average, the Bessel direction average, the TDS integral, the cumulants and the free-recoil rate. Only gap: D.32 states the third moment at T = 0, while Sec. 11.5 claims it at any T (see above).

## Notation clashes (one line each)
q_0 (alpha m_e vs sqrt(2M omega_0)); u (three meanings); omega_q vs omega_{qnu}; c (c_kappa, c_nu, c_k, c_4^(i), c_1^(kappa)); nu (branch vs exponent); eta (mean inverse speed vs eta_anh, kappa_eta); kappa (species vs kappa_eta); d (site difference, neighbor distance, dipole d_fi); Omega (cell volume vs solid angle).

## Overall
I would keep reading. Every number that depends only on the halo, the elastic tensors or the stated frequencies reproduced (list above), and D.31-D.32 make the two hardest sections self-contained. Nothing I could not follow blocks the next section. The real gaps are the sapphire bracket of eq:11.2-Ipol (stated bound 45.6 vs quoted 37.1 meV), the ambiguous 28/36 electron count in 11.8, the Markov-Krein subsection's reliance on unread App. C.10, and a cluster of small numeric inconsistencies (E_kin range, 2.84 vs 2.8 q0, 1.79 vs 1.76 q_BZ, 35.9 vs 36.3 meV). The chapter is long and number-dense, but the derivations are honest.

**Verdict: MINOR GAPS**
