# Ch16 mock-reader review: persona (a), first-year PhD student (isolated)

Read: tex/ch16/*.tex (the PDF build is current), appD/D-41.tex, appD/D-42.tex; reread s7-3 (Dirac bands, eq:7.3-eps, threshold mass) and s10-3 (the 2860 km/s figure). Read linearly. I redid every closed-form step and most quoted numbers in sympy/scipy (scratch scripts only). Appendix C.20 was out of scope, so the steps that depend only on it are listed under "not reproduced".

**Verdict: MINOR GAPS.** No point blocks the material that follows. Every closed-form derivation I tried came out, and almost every number checked to the quoted digits. The gaps are a few unclear or misleading sentences, notation clashes, and model jargon that goes past persona (a).

## 16.1 Dirac-material rates (with D.41)
Reproduced: eq:16.1-L from eq:7.3-epsbg; L_pub = eps_bg^2 L; Gamma_pub = eps_bg Gamma; the reach shifts; the identity Lambda' = Lambda exp[3pi/(g alpha~)], and the reference's 12pi^2 eps v/(g e^2) and 288pi^4 prefactor; R_DD = R0/eps_pub, so -v_C Im R_DD = L_pub; absorption is largest at eps_bg = |eps_D|. WE 16-factor, all lines: bracket 5.545+3.142i, eps_D = 10.73+6.08i, |eps|^2 = 2611, ratio 0.61; with the 5/3 scheme, 0.35 and 0.54; 3.35e30 zeta^2/kg-yr; zeta = 9.5e-16 against 1.5e-16. ZrTe5: harmonic means 50.5 and 25.34, eps_ii^2, 221, 4.6 and 17.6, exciton binding 0.14 meV, Sommerfeld 1.5 at b = 0.68 (i.e. 1.37 x the edge), expansion parameter 0.93.

Lost points:
1. WE 16-factor, scattering: "The reference's density is 1/(n_e V_uc) = 3.33 g/cm^3". This expression is not a mass density as written, and n_e is not defined here. The absorption part of the same example uses 10 g/cm^3 "of the reference". I could not tell why one model material has two densities. Fix: say what n_e is (electrons per unit mass?) and why scattering and absorption use different densities.
2. Chapter opening: "bring the electronic threshold down to about 10 keV". keV here is a threshold *mass*, while the energy threshold is 2 Delta_D = 31 meV. Say "threshold mass".

Not reproduced (numerical, inputs only partly given): 98 events/kg-yr; 2e-40 cm^2; 4800-6600; the factors 0.86-0.94 and 0.74; the 85/18/5 % weights near the edge.
Used before defined: none. (s, rho(s), B and alpha~ all come from 7.3 or are restated.)
Pace: the published-rate paragraph that follows eq:16.1-ratio is dense with citations (cutoff absorption, footnote 5, the v_F,z misprint). I followed it only after reading D.41. A one-line pointer "(D.41 shows this)" placed earlier would help.
Outcomes: (i) write L for a Dirac target with eps_bg in the total eps: yes. (ii) Convert a published reach: yes, I redid the 1600 and sqrt(40). (iii) Say when one loop fails: yes, g alpha~ ln(...) ~ 1. (iv) Anisotropic case: yes in principle, by eq:D.41-ratio, but numbers need code.

## 16.2 Low-dimensional plasmons and layered stacks
Reproduced: F_th and its expansion (0.946, 0.850, 0.90 at 191 eV); the tube kernel and its 10 % point at q r_t = 0.383 (108 eV); D_Dr = g E_F/4pi; the graphene plasmon 2 alpha E_F q (20x and 6.4x v_max, end at 30.2 eV); v_D = 3.41e-3; R0_1D; the pole, the delta-function weight and S_1D; the f-sum N_ch v q^2; g_c = 0.176/0.225/0.357 and 7.3/5.7/3.6 v_max; the 2.1x four-channel ratio; the parabolic-channel expansion (sympy: exact match); the demon (omega_a, v_a, slope, share, both widths); WE 16-demon in full (k_F = 156.4 eV, q_s = 1.49 keV, v_a = 2.42e-4, 41.8 -> 4.81 meV, width 0.77 meV, 191.5 meV, 1.75e-4, kinematics 1.37 and 3.8 keV); the stack kernel geometric series and both limits; the EMT identity; the 16.2-corr expansion (sympy: exact); the thin-film limit; the 0.4226 and 0.2754 eV effective-medium peaks; the 0.477 eV surface plasmon; 77 eV -> 14.5 keV.

Lost points:
3. "the long-wavelength form ends at q_par = 30 eV and 0.30 eV": I first read these as two momenta. They are (q, omega). Write "at q_par = 30 eV, where omega = 0.30 eV".
4. WE 16-demon, Weight: "The light band's own pair continuum below 15.3 meV carries ... 1.72e-4". The light continuum at q = 20 eV extends to q v_F + q^2/2m = 32.6 meV, and 15.3 meV is half of q v_F,l. I could not tell which part of the continuum is meant, or why it is cut at 15.3. One clause would fix this.
5. The opening says g_c ~ 0.2 makes the line "four to seven times faster" than the halo. Later the line runs 3.6 to 7.3 times faster over 1-100 eV. Minor.

Not reproduced: the limit-check crossover values (1.28 k_F, 0.157, 0.53, ka_s < 1.94). These are numerical, and their closed forms are given.
Used before defined: "Luttinger parameter" in the first sentence; it is defined only in eq:16.2-wire three paragraphs later. "Bosonize" is used only as a label, which is fine.
Pace: good. The 2D Lindhard facts (Re f2 = 1, Im f2 = nu/sqrt(1-nu^2)) are quoted, not derived. That is acceptable.
Outcomes: embedding (eq:16.2-embed) and the oblique-q kinematics: yes. 1D plasmon and g_c: yes. Demon velocity, weight and width: yes. Stack effective medium and in-plane correction: yes.

## 16.3 Graphene, nanotubes and quantum dots
Reproduced: m = 1.22 MeV and 1.62 keV; beta = 7.51 keV; the 1/4pi combination; eq:16.3-iso's 1/16pi^3; mean pi binding 4.41 eV over 0-8.4 eV (Monte Carlo); Fermi factors 7.3/3.4/2.6; v_D = 3.02e-3; 2 Delta_1 = 0.80 eV; q r_t >= 0.76 and 1.52 with J0^2 = 0.74 and 0.25; 226 keV; the overlap (theta'q/2)^2; eq:16.3-R1D from the two roots; the s-integral g v; the delta(s) limit, consistent with 16.2 at g_c = 1; the large-q tube kernel equal to the sheet kernel over 2 pi r_t; eq:16.3-eps2; the Weyl count and 9pi/8kR; kR = 33 <-> 109 E_conf; mu/4omega = 4.05e4; 0.2 mm; the Maxwell Garnett first order; the depolarization criterion and the real-eps form; WE 16-depol (0.275, 0.0567, 6.00, 4.62, 6.71, 0.566, 2.45).
Lost points: none blocking. The OPW paragraph gives ranges (0.46-25, 0.4-4.3, 740) with no formula for K(p,q) under the 2p_z model. I could not reproduce them without writing that integral myself.
Not reproduced: the ejection rates (6.9e3, 1.0e4, 2.8e3, 5.2e3), the factors 1.44 and 1.84, and the limit-box ratios. All are numerical.
Used before defined: "Wannier functions", "pseudopotential", "Delta SCF" (16.6) are tool names only. Fine.
Outcomes: ejection rate as a sum of per-orbital cross-sections: yes. Why OPW gives M = O(q): yes. Tube van Hove response: yes. Dot bulk limit and its surface deficit: yes. Depolarization factor: yes.

## 16.4 Molecular crystals
Reproduced: 0.883 MeV; f = 0.23 from |d| = 0.92 e A at 3.1 eV; the Davydov energies 2.888 and 2.919 eV; the dipole sum 1.693 = 2|d|^2; oscillator ratio 0.934 against the energy ratio 0.937; the binned weight 0.1871 = 0.0599 + 0.1272; q v_0 = 1.6 eV at 2 keV; 1.17 keV and q a_mol = 1.58; 1.1 MeV continuum onset; the direction average of eq:16.4-rate down to the isotropic 1/2 prefactor; the static eps_mac - 1 from the Lehmann sum; the 1/4pi.
Lost points:
6. The model paragraph (Pariser-Parr-Pople SCF, Mataga-Nishimoto, Slater 2p_z with Z_eff = 3.15, the resonance integral -0.63/(m_e x^2), Platt's L_a/B_b/L_b) is too fast for me. I can treat it as a black box, since the text says it is a guide to sizes. One sentence saying what PPP adds to Hueckel (e-e repulsion in a pi-only basis) would let me picture it.
7. A_day bounds: from the quoted ratios, light 69 -> 0.97 (not 0.98) at 1 MeV, and light 1.39 -> 0.16 (text 0.17) at 10 MeV. Rounding only.
8. The summary and tab:16-nuisances say "+6.3 % above 30 MeV". The section says only "far above threshold ... flat in mass" and never gives 30 MeV.
Not reproduced: J11 and J12 (Ewald), the 3 keV weights, 8.0e4 and 2.3e4 /kg-yr, 92 and 69, the 6.3 % and 27-35 %. All need the model code.
Used before defined: "Radon transform f^_gal" (11.7) and "Huang-Rhys" (5.6) are referenced back. Fine.
Outcomes: the Frenkel Hamiltonian from the BSE in a molecular basis: yes. The binned sum rule and its three failure modes: yes. Why the near-threshold rate is directional (short axis, out-of-plane zero): yes. The A_day bound from R_max/R_min: yes.

## 16.5 Dopants
Reproduced: 13 keV; 5e-9; 1/r_perp = 81 eV; the E-state formula 2/9[F_par - F_perp]^2 from the valley vectors; r_par ~ 1.4 nm implied by the 0.022 peak; 29 keV; the T2 momenta 0.685, 3.60, 3.88, 2.33, 2.74 keV and the masses 130 and 441 keV; eq:16.5-gos integrates to the hydrogen continuum f-sum 0.4350 (numerical check of the bracket); eps2^D = 4 pi^2 alpha n sum|e.r|^2; the line strengths 0.12 and 0.39; the f-sum 3.85; Du et al.'s 85.7 meV; WE 16-sip-line (7.73e-6 eV, 4.22 and 3.21 ueV, eps2 = 1.17, 8.99e-3, 5.5e31, 2.3e-16, 4.9e-15, 1.2e-4); the line-centre saturation 1/[1+(4/9)(eps2/eps_h)^2] and 4.8e15 cm^-3; the second-order expansion of the effective medium; the neighbor probabilities 4.8e-4, 0.38, 0.58; the Clausius-Mossotti factors 1.15-1.57 and 1.27-2.21; the divergences 2.1e19 and 6.3e18.
Lost points:
9. "A row without a proper correlation with the charge, the spin density of ... , enters unscreened". "Row" refers back to the coupling matrix of 8.4, and I had to reread 8.4 to decode it. Write "an operator (a row of the coupling vector) with no proper correlation...".
10. WE 16-sip-line: "m_phi = 45.59 meV - 11.48 meV". 11.48 meV is the 2p_0 binding energy, which the text has not stated.
11. lim:16.5a writes W(0, m_phi) for the quantity the key result calls L^D. Use one symbol.
Not reproduced: 1.47/0.56 (the misprint effect), 1.13-1.48, 4.85, 25 %/49 %, the 10 % densities 2.6e17 and 8.8e17. All are numerical.
Outcomes: first-order donor response with host screening counted once: yes. GOS: yes. The valley-orbit selection rules and their directions: yes. Resonant absorption reach and where it saturates: yes. The impurity-band criterion: yes.

## 16.6 Color centers and broken bonds
Reproduced: 188 eV at 0.5 GeV; F masses 0.113/0.186/0.255 GeV; 0.218 and 0.414 GeV; Li transfer 0.788, 0.129 and 0.114 GeV; recoil arrows 31/69/188/711 eV; q_min = 978 keV; widths 0.95-1.44 eV; zero-point 17-26 keV (4.6-7.0 alpha m_e, ratio 0.018-0.027); 4.0 MeV and 46x; Lindhard k, eps, g, y_L = 0.226 and KP 14.3/18.5; T_d 155/58/26.7 eV and pairs 2.3/0.7/0.3; eq:16.6-ccrate's prefactor and its delta limit q/2mu; H2 q_min = 134 keV and 25.9 MeV; 8.7; the CM Doppler 1.6e-6; p_rms 6.53 keV = 1.75 alpha m_e; deposit q^2/2M_1; omega/4 = 0.136 eV; 0.90; 0.84 and 0.75; 42.9 MeV; NV 0.554 MeV and 1.47 keV; the photon budget 5e5.
Lost points:
12. The intro to 16.6-cc says "a rate averaged over directions before the yield is applied is wrong near threshold". The key formula then averages <Y>_r over recoil directions. The next paragraph explains that this is exact only for isotropic recoil directions, but on first reading it looks like a contradiction. Move the caveat up, or call eq:16.6-ccrate the orientation-averaged rate.
13. tab:16-nuisances gives "within 10 % for E_R^max >= 1.22-1.36 E_d". The text and limit box give only 1.36.
Outcomes: rate = class rate x yield: yes. Recovering Budnik et al. and Essig et al. as limits: yes. Sizing the zero-point corrections: yes. Naming the four unmeasured yields and the measurement for each: yes.

## 16.7 Glasses, random media and two-level systems
Reproduced: the Jacobian giving eq:16.7-P; the norm integral = Pbar; 87 % from u > 0.5; chi''_res; tan delta; the Debye static susceptibility 2b^2(D_as/D)^2 d tanh; eq:16.7-relax from it; both limits (pi/4 -> 1/2 plateau; 1/3 and pi^4/8 -> (pi^3/12) K T^3/omega); K_ph = 4.63e4 eV^-2; 1.34 K; 4e-9 at 10 mK; 2^{1/2}; 42 m; WE 16-tls-dp (7.69e-5, 2.07e23, 5.03e29, 2.44e-15, x16.7, 0.24, 0.894, 22 mg, 5.2e-13, p = 0.23 e A = 1.1 D); the Rabi rate < 6e-7 s^-1 and tau_1^-1 = 1.07e6 s^-1; 1.15 neV, 0.28 MHz, 115 neV; eq:16.7-S; the host term and 9.85e20, |f_host| = 2.86; <|f_core|^2>; the eq:16.7-rate prefactor 1/4 (from 2m^2<v>); 9.0e-3 and 3.1e-2 /kg/day/meV; 1.2e16 systems; eq:16.7-eps2 and the plane-wave C^IR; the Debye numbers alpha = 0.10 cm^-1, eps2 = 3.1e-3, 1.4e30; the crossings at 0.46 and 6.4 meV; 115 cm^-1 and 9 %; 62 um; the exponential-correlation transform and eq:16.7-Ffluc; sigma_crit = 1.16/2.41/57 e-38; V/E = 1.86 and 1.29; Born reflectance and its 1+V/E correction.
Lost points:
14. Relaxation limits: "When every system relaxes fast, omega tau_1 << 1, the u integral is pi/4". With omega tau << 1 in the integrand the integral tends to zero. The pi/4 comes from the systems with u^2 ~ omega tau_min, the slow ones, because tau_1 is proportional to 1/u^2. I was stuck until I redid it. Fix: "when the fastest systems (u = 1) satisfy omega tau_min << 1, the u integral, dominated by u^2 ~ omega tau_min, is pi/4".
15. Notation clashes in 16.7-ir/16.7-random: alpha is the absorption coefficient next to the fine structure alpha; "IR" is both Ioffe-Regel (omega_IR) and infrared (C^IR, A^IR); C is the tunneling strength, C^IR, and Taraskin's "alpha = Cg"; R is both the sphere radius and the reflectance.
16. q_x = |f_host|/(8d) uses the unaveraged core amplitude 8qd. The orientation average, 64 q^2 d^2/3, would move q_x up by sqrt 3. The word "near" covers this, but the definition sits right after the averaged formula.
Not reproduced: the 2.2e-2 core term and the median q = 1.73 keV (need eta). 1.36 K is from the full integral.
Outcomes: STM distribution and why Pbar alone counts couplers: yes. Dark-photon rate from tan delta: yes. Scattering structure factor and host/core vertices: yes. Glass IR absorption A + B omega^2 and why A survives: yes. Born limit of coherent scattering: yes.

## 16.8 Two-level systems at millikelvin (with D.42)
Reproduced: eq:16.8-golden (and D.42's J normalization 2J = 2 pi sum lambda^2 delta); J_ph = 2K omega^3 from the mode sum; the Sahling prefactor; 16.6x (silica) and 50x (Al); Gamma^el = 2.49e9 s^-1; D.42 alpha = 4K_b; the phase-shift form, its expansion 1 - (2/3)pi^2 K_b, 0.19 at K_b = 0.07, and +32 %; the Bessel reduction (the y = a(cosh - 1) substitution) and sinh u K1(u) = 0.86/0.71, 0.91 at 0.7T; the asymptotics; the 2e-9 s^-1 at 50 mK; 0.88 Delta; 1.5 K; the Gamma ratio 0.71 and 10 % at alpha = 0.091; T_coh and 2.4 Delta_r; small-coupling consistency with eq:16.8-scaling; the kappa_PB series 1/24 and 7/5760; T_x = 18.5 K; lambda <= 23.6; Eckart V_b = 248 meV and T_x = 240 K; T_frz; the pi^2/12 energy integral and the 1/2t window sum; the 10.6-of-12.2 decades; WE 16-heat (1.64e-7 J, 46/1.9/0.27 pW, 0.84 uJ, 5e12 eV, 1.4x, 4.6/0.19 nW); the cascade mean 1/(1-b).
Lost points:
17. "relaxes in aluminum at 1.8e5 s^-1 below 0.1 K": at 0.1 K, coth(Delta/2T) = 1.20 gives 2.1e5. The rate is 1.8e5 only below about 50 mK.
18. WE 16-heat: "0.05 x 3 = 0.15 of the normal density". The 3 is (8.0 - 2.0)/2.0, the ratio of the stress-lowered defects to the heat-release density, and the text never says so. Add four words.
Not reproduced (outside my reading scope): eq:16.8-scaling from eq:C.20-ohmrate, and "Delta~0^2 = Delta_r^{2(1-alpha)}(2 pi T)^{2 alpha}" from eq:C.20-Dr. Both need App. C.20, and the Gamma(1-2 alpha)cos(pi alpha) factor must be inside Delta_r. I accepted them.
Used before defined: "noninteracting-blip result" (C.20 only). "Case-I coherence factor" is cross-referenced to 7.2.
Outcomes: one-phonon and electron T1 from J_s: yes. Superconducting suppression including the Bessel correction: yes. When Black's rate fails and the scaling limit takes over: yes, qualitatively. Heat release 1/t law with prefactor: yes, I redid the worked example.

## 16.9 Material inputs, and Summary
Reproduced: eq:16.9-power; the direction-average ratio 0.327 and the 64 % within 30 deg of y (Monte Carlo); (9.8/20.75)^2 = 0.22; 2^{1.87-1.94} = 3.7-3.8; the static Dirac terms 9.8/1.57/6.7 and their 3-8 % share; alpha~_y 0.155 -> 0.327; the gap-shifted thresholds 7.2 and 10.5 keV; the zeta bands 1.8, 4.1 and 0.39-1.33; the sigma shifts 0.69/0.54 and 0.94/0.74; J0^2 = 0.68 at q r_t = 0.86. The summary matches the sections, apart from point 8.
Outcomes: classifying a target as theory-, calculation- or data-limited, and turning a power-law input into a reach band: yes.

## Too slow / too fast (overall)
- Too fast: the PPP/anthracene model (6); the long chain of literature-correction remarks in 16.1 before D.41 is read; the 16.8 scaling limit, which leans entirely on C.20.
- Too slow: nothing I would cut. The three "remarks" after eq:16.7-dp (single tanh, 1/eps_r, saturation) are useful.

## Overall
I would keep reading. The chapter's method is to derive the response, recover the published formula as a limit, size the correction in a limit box, and list the inputs. I could follow that pattern throughout, and each key result traced back to Chapters 4, 7, 8 and 10 without new formalism. The numbers held up under independent recomputation, about 300 values checked with no substantive discrepancy. What remains is local: the plateau sentence in 16.7 (14), the two-density puzzle in WE 16-factor (1), the 15.3 meV clause (4), notation clashes (15), and a few unstated inputs (10, 18).
