# Chapter 20 mock-reader review: persona (a), isolated

Reader: first-year PhD student entering dark-matter direct detection (READER.md persona a). Read linearly from
the .tex sources tex/ch20/*.tex, checked against build/main.pdf (pdftotext). Every derivation was redone on paper
or in sympy/numpy. The numerical checks included an AMM boundary solver, the Kaplan-cascade recursion, the
fragmentation equation by matrix exponential, and the mean-field kernel solve. Scripts are in the session
scratchpad and are not part of the book.

## Chapter opening and map
- Clear. The opening numbers (27 pairs, 31 eV gap, 69 eV phonons) match Ch. 19. The question is well posed:
  what does a readout measure, and does it still discriminate?
- Fig. 20.1 caption is helpful. No lost points.

## 20.1 Charge transport and the measured charge
Lost points
- L.26: "the Coulomb energy alpha/(eps0 r)". This works only if I remember that the book writes the dielectric constant as
  eps0 in Heaviside-Lorentz units. I did remember. But L.135, "in SI units eps0 becomes eps0 eps0^SI", made me stop:
  the same symbol appears twice with two meanings. A different symbol for the SI vacuum permittivity would fix it.
- L.75: "the Luke phonon energy is g_Luke <q> omega". I had to recall that omega is the deposited energy from
  earlier chapters. One clause ("for a deposit omega") would help.
- L.156: the "scattering length l0" is introduced only as a combination of constants. I could not tell what
  scatters over that length. One sentence on its meaning (or "a convenient length") would help.
Steps I could not reproduce
- Limit box 20.1a caption: "deficit at most 8.9 %" at mu E = 0.1 v_sat. I get 8.85 %, which rounds to 8.8 %. Trivial.
- L.174: mean Luke energy of holes at 1 V/cm. With the text's own x = k/ks = 4.31 I get 1.5 * 0.230 * 3.31 = 1.14 meV,
  not 1.2. For electrons I get 1.09 and 2.04 meV, against the text's 1.1 and 2.1. Small, but the 20.5 text then
  quotes "1.1 and 2.1 meV for silicon carriers", so the rounding should be made consistent.
Everything else reproduced exactly: Green reciprocity giving Ramo, and the 2/3 example. The Coulomb-vs-bias comparison (1.26e-5 eV vs 4 meV). Cut-off mean path, Hecht, the depth average and its expansion (including the +x^2/24 term and the x/4 accuracy). 0.632/0.736/0.787/0.952/0.968. Limit-box 20.1b gray limits 0.030 and 0.015. Compound-sum variance leading to eq. 20.1-Fpos. Binomial limit. Gray f_det >= 0.923. Worked example 20-fano in full: lambda = 4.83 and 6.41 d. sigma^2 = 0.0156. 0.125. <q^2> = 0.9026. <sigma^2> = 0.0230. Var = 1.16e-4. 1.22e-4 N. 82 pairs. 6e-6. Boltzmann factor. Poole-Frenkel 0.45 and 2.25 meV. eq. 20.1-dE and the sheet bound. 1.59e-7 V/cm per charge/cm^2. 6.3-12.6e4 cm^-2. 5-10 h. The Luke golden rule: root Q*, Jacobian Q*/2m, the (1-ks/k)^3 integral and l0 rewrite. 0.230 meV, 7.5 um, 4.0e8 s^-1, 2.0e8 s^-1, 0.35/0.46 meV. The balance equation and x = 4.3/7.0. The (Ec/Emax)^4 = 0.3 %.
Used before defined
- None of substance. "flashing" is defined where it is used. "conductivity mass" (L.174) is used without
  definition. That is borderline for persona (a), who has not taken solid state; "the effective mass that sets
  the drift" would do.
Pace
- Ramo/reciprocity paragraph (L.7) is dense but complete; I needed two passes. The Fano subsection and its worked
  example are the best-paced part of the chapter.
- Luke subsection: the step "integrating over Q and the azimuth" hides one line (the 2pi/(8pi^3) * 2pi * 2m/Q*
  bookkeeping). I reproduced it, but a weaker reader may not.
Learning outcomes (inferred)
- Use Ramo's theorem to find the induced charge and bias work for a planar detector: YES (did the 2/3 case).
- Compute the collected fraction with trapping for face, midplane and bulk events: YES.
- Decompose the measured Fano factor into cascade, partial-charge and position terms: YES (reproduced the WE).
- Estimate the space-charge field distortion and the time to reach it: YES.
- Derive the Luke emission rate and mean phonon energy: YES.

## 20.2 Athermal phonons in the substrate
Lost points
- Eq. 20.2-frag, L.78: "P_d(y) the distribution of the energy fraction y that a decay passes to a daughter, counting both
  daughters, so that int P_d = 1". I first read this as a number distribution, which would integrate to 2.
  It is the energy-weighted distribution, P_d = 2 y p(y). That only became clear from the stand-in 60 y^3(1-y)^2
  = 2y * 30y^2(1-y)^2 at L.105. Saying "energy-weighted" once, and writing P_d = 2y p(y), would remove this.
  Sec. 20.5 later uses the number form 2p(u), so the relation between the two matters.
- L.9-11, the soft fraction f_s: "Each pair then sheds on average omega_opt". The reason is that each of the two carriers
  has mean kinetic energy omega_opt/2. That takes a moment. Also, the cap at 64 meV is 8.7 meV, so "below about 6 meV" is
  loose. Fine as an estimate.
- x_L: here x_L = 0.093 for silicon (from Kelsey). In 20.5 the "longitudinal share of the density of states" is
  0.0975, from the isotropic speeds. I computed 0.0975 myself from c^-3 weights. The two values are never
  reconciled. A reader wonders which one is right.
Steps I could not reproduce
- L.138: "A phonon of 45 meV ... decays within 0.95 ns, by which time it has spread over 1.4 um". The decay time
  checks (E* = 45 meV at 0.956 ns). But the text's own formula (10/9) v^2 (xA)^{4/5} t^{9/5}/B, with the inputs that
  give 8.6 um at 10 ns, gives 1.03 um at 0.95 ns, not 1.4 um.
- I could not independently check the Delta_h thresholds (0.51-0.53 E_mem) or the memory times 6.8 ns, 47 ns, 0.15 us
  and 1.0 us. They are consistent with E* scaling, though: e.g. E*(0.15 us) = 0.52 * 31 meV.
Reproduced: Phonon dilution (6e11 modes, 4e-9). Acoustic caps 8.7 and 6.0 meV. f_s 1.7 % and 1.3 %. V3 scaling, the phase-space Jacobian, and so Gamma ~ omega^5. The transverse no-decay argument. Lifetimes 18 ps and 14 us. The isotope matrix element, the golden-rule sum giving (pi/6) g omega^2 g_ph, and the Debye reduction to B = 4 pi^3 g Omega <c^-3>. All of WE 20-iso: g_md 2.007e-4, 70 %. 20.02 A^3. 4.69e-12. B = 2.44e-42. 0.41 us. 3.9e-7. 5.85 km/s. 2.4 mm. 4e5. Factor 15. B/A = 33 and 228 THz. The scaling equation, the energy check, and E* values 44.6/28.1/17.7/11.2 and 37.8/23.8/15.0/9.5. Settling times 0.19/1.3 ns. My own matrix-exponential solve gives the settled mean 0.667 E*, median 0.66, and 10-90 % band 0.36-0.97 E*. N_mix 164/650/1300/5100. RMS spread 8.6/68/540 um and 1.8 um (Ge). Shell fractions 0.21/1.7/13.5/36 %. Sapphire numbers. The transfer-kernel bound proof.
Used before defined
- None. "total-variation distance" is defined in place.
Pace
- The isotope derivation (L.38-42) is fast for persona (a). The cubic-site identity N^-1 sum e e* delta =
  delta_bg g_ph/3 is asserted, not shown. Acceptable, but a one-line reason (cubic symmetry makes the tensor isotropic,
  and normalization fixes the 1/3) would help.
- The memory subsection is long. The four total-variation numbers (0.13, 0.026, 0.015, 0.012) could be cut to two.
Learning outcomes
- Explain why anharmonic decay goes as E^5 and isotope scattering as E^4: YES.
- Compute B_iso for natural silicon from masses and abundances: YES.
- State and use the scaling spectrum and E*(t): YES.
- State the transfer-kernel bound and when it fails (single sign, near faces, sapphire): YES.

## 20.3 Phonons into films
Lost points
- None blocking. Eq. 20.3-b: the "+-Q_z" sign conventions for reflected vs transmitted waves are stated tersely. I wrote
  my own solver and needed the sign of the reflected waves' z-direction. The text's convention worked once I took
  "-" for reflected.
Steps I could not reproduce
- None. My AMM solver reproduces: t = 0.991/0.960 at normal incidence; 0.98 to 70 deg; 0.905 at 78 deg. SV conversion 0.035 at 30 deg and a 0.192 maximum at 75.7 deg. All critical angles; 0.30 at 45.4 deg. Averages 0.934 (0.977/0.892/0.960) and 0.327 (0.605/0.270/0.318); reciprocity to 3e-10. n_Si/n_Al = 0.350; 0.669, 0.895, 0.598; DMM 0.741/0.259; the impedance-law factors 1.06, 0.347, 3.03. Absorption: 2E3 = 1 - 2y; P_abs -> 4d/(l t); the t_l derivation; v_s = 3.29; t_l 0.223/0.281 ns; P_abs 0.467 vs 0.462. The inverted fit: l/d 25.8-9.1; 1.55-0.54 um; 0.47-0.17 ns; angle-kept 1.43-0.50 um; DMM 1.36-0.36 um; 0.105-0.193. Anisotropy 0.291/0.360 and 0.925-0.937; 0 K Al 0.368 and 0.187 ns. Quarter-wave t_min 0.855 at 0.72 THz; 1 nm layer 0.907.
- Minor: "within 10 % of eq. 20.3-pabs for d_f/l_f < 0.074, above it everywhere, by up to 14 %". The lumped form
  re-enters the 10 % band for d_f/l_f > 0.55 (max excess 13.5 % at 0.235), so "< 0.074" is not the whole statement.
Used before defined
- None.
Pace
- Good. The S-matrix trace argument for reciprocity is short and complete. The 60 % trapped-flux point is made
  clearly and reused well.
Learning outcomes
- Compute angle-resolved AMM transmissions and their isotropic averages: YES (built a solver from the text).
- Derive and use the reciprocity n1 t12 = n2 t21, and the DMM value: YES.
- Compute P_abs and t_l for a film: YES.
- Interpret a fitted interface coefficient as an absorption probability: YES.

## 20.4 Quasiparticle yield in superconductors
Lost points
- L.103: "Guruswamy et al. estimate t_l/t_0 ~ 0.5, where the film costs up to 40 percent of the infinite-volume
  yield". Just above, for t_l/t_0 = 0.5, the text gives 0.238 at 60 Delta and about 0.30 at 16 Delta, against 0.590.
  That is a cost of 49-60 % in the detector band, not "up to 40 %". The 40 % holds only over Guruswamy's
  2-10 Delta range (0.349 vs 0.59). I was confused about which band was meant. The same "up to 40 %" recurs in 20.5
  L.74 and in the nuisance table.
- Notation: t_0 here is the pair-breaking time at threshold (0.26 ns). In 20.5 L.101, t_0 is the release-time scale
  of eq. 19.5-bimol. Two meanings of one symbol in adjacent sections.
Steps I could not reproduce
- None. Reproduced: 16 gaps, 9.5, <5. v_F/v_s = 311. g_I(2) = pi/2, g_I(3) = 1.322, g_I(10) = 1.05. t_pb(10 Delta) = 0.30 t_0. Conserving correction 1.6e-3. The kinematic proof below 4 Delta. WE 20-al3: 0.792 t_0, 0.206 ns, 43.5 GHz. p_pb 0.84/0.93. Escape at 200 Delta 0.4 %. Isotope rates 140 and 2.1e3 s^-1; 39 m and 1.5 m. Factor 99. My own recursion of eq. 20.4-cascade (grid 0.01-0.02 Delta, so +-0.002): t_l = infinity: max 0.601 at 5.46 Delta, asymptote 0.591. t_l/t_0 = 4: 0.562 at 5.2 Delta, 0.526 at 10 Delta, 0.498 at 40 Delta. At 10 Delta: 0.349/0.478/0.556 for 0.5/2/8. 60 Delta at 0.5: 0.238. Band drops 20.8/6.6/1.8 % (text 20.5/6.5/1.7). All agree.
Used before defined
- "rho_g of sec. 19.5" (L.111) is a Ch. 19 symbol. I had to look back to recall it. A short reminder clause would help.
Pace
- Good. The exact below-four-gaps result is the clearest single idea in the chapter. The Chang-Scalapino comparison
  paragraph is dense with numbers; acceptable.
Learning outcomes
- Prove Y_qp = 2 Delta/E below 4 Delta: YES.
- Write and solve the Kaplan-cascade mean equations in a lumped film: YES (solved them).
- Explain why the yield depends on t_l/t_0 and falls across the detector band: YES.
- Explain why electrode recombination phonons are soft and ballistic: YES.

## 20.5 Collection kernels and recoil discrimination
Lost points
- L.46: "Aluminum gets more because a quarter of the energy arrives below 3 meV". The text's own split
  (58.4 - 40.4 = 18 %) implies about 18 % below 3 meV, and my mean-field solve gives 18 %. "A quarter" does not
  match. In the same sentence, "a mean energy of 4.4 meV": I get 3.95 meV (number-weighted) or 4.99 meV
  (energy-weighted). Please say which mean is meant and check the value.
- L.87: "O_obs = a_prim + varpi_O phi_Luke + varpi_gap phi_gap to first order". This is plausible, but I had to
  construct it myself from the channel fractions. One line of derivation would help.
- L.89: the soft share is now f_soft and omega_op; in 20.2 it was f_s and omega_opt. Same quantity, two notations.
- L.108: the low-bias route says "Let all pairs be drifted, with g = f_det g_Luke". The optimum bias "near 12 V" matches
  f_det = 1 (11.7 V). With f_det = 0.873 the bias is 13.5 V. State which.
- L.108: F_eh = 0.119 here. In 20.1 (L.108 caption, WE 20-fano) the cascade value is 0.114. Two values of the same
  quantity in one chapter with no comment.
- L.139: "The most favorable corner of the 1 sigma bands ... gives 1.72". I get 1.36 with trapped carriers inducing
  nothing and 1.72 in the mean-charge case. The sentence follows the mean-charge sentence, but it reads as if it
  applies to the baseline case. Add "(mean-charge case)".
Steps I could not reproduce
- L.108: the smallest varpi_O for S_sep = 2 at 100 eV. My implementation of the stated noise model gives
  0.11/0.22/0.43 for sigma_pos = 0.02/0.05/0.10, at about 10-12 V, against the text's 0.13/0.24/0.45. My
  implementation: same E_R for both recoils, F_meas binomial with F_eh = 0.119 and F_NR = 0.9, f_det = 0.873,
  baseline 2.65 eV/E_ph, Y' or Y_q. Either an input differs from what the text states (equal E_R or equal E_ph?
  which Fano for ER?) or the numbers need a recheck. The conclusion does not change.
Reproduced: Slab hit rate v/2d. v_bar 5.75, x_L 0.0975. Absorption 15/30 us and bare loss 1.0/2.0 %. My mean-field solve gives 40.5/58.3/1.2 %, a_prim 0.590, eps_prim 0.583, closure 1e-8. r_coll 0.935 at 0.75 meV and 0.998 at 4.7 meV. varpi_O 0.41, 0.20, 0.08, 0.03. s_sub 0.085/0.017/0.005 and 0.13/0.058/0.032/0.008. The 0.61 meV crossing. s_ng -0.047/+0.002, and +0.062/+0.058 with Y = 0.50. Eq. 20.5-sign. Delta_soft 0.015 and the 0.008 bound. Gap route 0.28(1-b) and the sign change at 3.86 t_0. The low-bias optimum (1-sqrt Y)/(1+sqrt Y) = 0.516 at g = 3.1. Eq. 20.5-hv derivation. WE 20-ceiling exactly: 765.9, 31.54, 5.459/7.343, 1.885, 0.5635/0.2309, 1.22, 1.50, 1.32, F_NR < 0.21, and 1.72 for F_NR = 0 with nothing induced. Ceiling 16.8/10.7/3.4/1.22/0.43 vs bias.
Used before defined
- None new.
Pace
- The kernel definitions are clear. The routes subsection is long: three routes, each with conditions. The
  conditional verdicts are honest and well flagged.
Learning outcomes
- Define collection kernels and the readout functionals (varpi, sigma_pos, r_coll): YES.
- Set up and solve the mean-field kernel equation: YES (reproduced the primary split and the Luke curves).
- Say what fixes the sign of r_coll - 1: YES (sub-gap fate and near-gap yield; eq. 20.5-sign).
- Bound the primary-phonon route and evaluate the high-voltage ceiling: YES.
- Size the low-bias Luke route: PARTLY. I get the method, but my required contrasts come out about 0.02 lower.

## Summary section and PDF
- The summary is faithful to the sections. It repeats "1.5 %" and "0.8 %" correctly.
- PDF: one unresolved reference in 20.5-verdicts, "guide to next targets (??)" (sec:21.7, presumably not yet written).
  It needs a placeholder or a fix once Ch. 21 exists.

## Overall
This is a demanding chapter, but it is honest and almost fully reproducible from the text and earlier chapters. I
redid essentially every derivation and nearly all of the numbers, including four non-trivial numerical solves
(AMM averages, scaling spectrum, Kaplan cascade, mean-field kernels), and they agree with the book. Nothing blocks
the following material. The defects are local:
- two numbers I could not reproduce (the 1.4 um spread at 0.95 ns; the low-bias varpi_O thresholds);
- one internal inconsistency ("a quarter" vs 18 % below 3 meV; the 4.4 meV mean);
- the misleading "up to 40 percent" for thin-film losses in the detector band;
- notation duplications (eps0 used twice; t_0 used twice; f_s/f_soft and omega_opt/omega_op; x_L 0.093 vs 0.0975;
  F_eh 0.114 vs 0.119);
- the energy-weighted P_d that is never called energy-weighted.
I would keep reading. The chapter tells me what each readout actually measures, and it says where the answer is
conditional.

Verdict: MINOR GAPS
