# Chapter 20: mock reader b (personas b and c)
Source read: tex/ch20/*.tex (same content as build/main.pdf, built 20:38 after the last .tex edit). Chapters 1-19 assumed read; a few terms were spot-checked there with grep.
Checks: Python/scipy scripts in the session scratchpad. I re-derived or recomputed about 120 numbers. Each discrepancy below is one I could reproduce.

## Persona (b): particle physicist, QFT yes, solid state no

### 20.1 Charge transport
- **Lost points.**
  - L1 (minor). §20.1-space, sheet bound \eqref{eq:20.1-sheet} "which a sheet at a face attains". By \eqref{eq:20.1-dE}, a sheet exactly at z0 = 0 (or d) changes the field nowhere: the bracket vanishes for every z > z0. The bound is only *approached* as z0 -> 0, and then the distortion -e n/eps lives in the layer 0 < z < z0, whose thickness goes to zero. The following "6.3e4 cm^-2 for a sheet at a face" therefore describes a distortion confined to a vanishing layer. Fix: say "approached by a sheet close to a face, where the distorted region is the thin layer between sheet and electrode". Or quote the midplane value (12.6e4, which spans half the crystal) as the operative one.
  - L2 (notation). eps_0 is the *relative* static dielectric constant, and "in SI units eps_0 becomes eps_0 eps_0^SI". For a particle physicist eps_0 means the vacuum permittivity; I had to stop twice. A one-line reminder at first use in the chapter would help, or a different symbol (eps_r).
- **Steps reproduced.** All of these agree to the printed digits:
  - Ramo/reciprocity, eq-qpair and its 2/3 example; Coulomb energy 1.3e-5 eV vs 4 meV.
  - Hecht limits; the depth average and its expansion, including the +d^2/24lambda^2 term and "accurate to d/4lambda".
  - Collection values 0.632/0.736/0.787/0.952/0.967(5) and the 1/3 argument.
  - Limit-box gray regions: 8.85% deficit, d <= 0.030 lambda and 0.015 lambda_e, f_det >= 0.9234.
  - eq-Fpos via the law of total variance, and its binomial limit.
  - The whole Fano worked example: lambda = 4.83 d and 6.41 d; sigma^2 = 0.0156; F = 0.125; <q^2> = 0.9026, <sigma^2> = 0.0230, Var = 1.16e-4; 0.1325; position terms 0.003/0.033/0.19; 82 pairs; 6e-6.
  - Space charge: Boltzmann factor 1.04e4; Poole-Frenkel 0.45 and 2.25 meV; 1.59e-7 V/cm per charge/cm^2; 5.2 and 10.3 h.
  - Luke rate: golden rule, root Q*, Jacobian Q*/2m, the cos-theta integral, l0 rewrite, <u> = 3a/4, eq-Eluke; holes l0 = 7.47 um, mc^2 = 0.230 meV, c/3l0 = 4.0e8 s^-1; the balance equation and k/ks = 4.3, 7.0 (holes) and 7.1, 12.4 (electrons); the 0.3% below 2Delta.
- **Numerical slip.** For holes at 1 V/cm the balance gives <E_L> = 1.5 x 0.230 x 3.31 = **1.14 meV**. The text prints 1.2 (4 V/cm: 2.05 -> "2.1" is fine). §20.5 later quotes "near 1.1 meV" for the same quantity. Use 1.1 in both places.
- **Used before defined.** "Conductivity mass" (electrons, 0.26 m_e) is defined only in App. E.12, not in the main text before this point. The over-charged states D^- and A^+ first appear in Open problems with a half-sentence gloss.
- **Pace.** Good. The bias-work paragraph with three electrodes is fast but optional.
- **Outcomes.** Induced charge from weighting potentials: yes. Hecht/bulk collection: yes. The three Fano terms and when each dominates: yes. Space-charge bound and flash time: yes. Luke rate and spectrum: yes. I can redo every number.

### 20.2 Athermal phonons
- **Lost points.**
  - L3 (minor). The definition of P_d(y) ("the distribution of the energy fraction y ... counting both daughters, so that int P_d = 1") reads as a *number* distribution, which would integrate to 2. Only on reaching "30y^2(1-y)^2 ... gives P_d = 60y^3(1-y)^2" did I see that P_d is energy-weighted (2y p(y)). The gain term of eq-frag needs exactly that. Fix: write "energy-weighted" in the definition. §20.5 then uses the number density 2p(u), which is consistent but in a different convention; a cross-reference would help.
  - L4. The vertex argument (zeroth order cancels for translation polarizations, first surviving term ~Q1Q2Q3) needs eq 5.7-V3 and the sum rule recalled. It went fast for me, but I could follow it with ch5 open.
- **Steps reproduced.**
  - Occupation 4e-9.
  - Cap 8.7/6.0 meV; f_s = 1.7% and 1.3%.
  - Phase-space angle integral and the omega^5 law.
  - 18 ps / 14 us lifetimes.
  - Scaling equation from eq-frag, including dE*/dt and the energy check.
  - Settling times 0.19 and 1.3 ns; E*(t) for Si and Ge, all eight values.
  - Mean of the settled spectrum: my matrix-exponential solve gives <E> = 0.667 E* (0.673 at 0.46 ns, 0.667 at 10-100 ns).
  - g_md = 2.007e-4 with the 70% share; B_iso = 2.44e-42; 0.41 us; 2.4 mm; 5.85 km/s; <c^-3> = 4.69e-12 for the code speeds.
  - Ratios 33 and 228 THz; N_mix = 164/654 (Si) and 1274/5072 (Ge).
  - rms distances 8.5/68/539 um (Si) and 1.8/15/116 um (Ge); shell fractions 0.21/1.7/13.5/36%.
  - Sapphire numbers.
  - Proof of the transfer-kernel bound.
- **Could not reproduce.** "A phonon of 45 meV ... decays within 0.95 ns, by which time it has spread over **1.4 um**." The decay time is right (0.951 ns). But the book's own rms law (8.5 um at 10 ns, r ∝ t^0.9) gives **1.03 um** at 0.95 ns. I could not tell which input gives 1.4.
- Memory thresholds (0.51-0.53 E_mem; 6.8 ns, 47 ns, 0.15 us, 1.0 us; TV 0.13/0.026/...) are numerical. I did not rerun them; they are plausible from my solve.
- **Outcomes.** Why E^5 and E^4: yes. Scaling form and E*(t): yes. Isotope rate from masses: yes. The bound and its single-sign caveat: yes.

### 20.3 Phonons into films
- **Lost points.** None blocking. In eq-pabs-theta, the sentence before the display uses y_f before the display defines it (trivial).
- **Steps reproduced.**
  - Voigt speeds and anisotropy ratios.
  - All critical angles (36.9, 57.5, 20.2, 29.0, 35.2, 45.4 deg).
  - My own 4x4 AMM solve: tbar(Si->Al) = 0.9338, tbar(Al->Si) = 0.3270, the per-polarization 0.977/0.892/0.960 and 0.605/0.270/0.318; reciprocity holds to 8e-11.
  - n = 0.0809/0.2311, 0.669, 0.895, 0.598, DMM 0.741/0.259; impedance law 0.991, factor 3.03, 0.347.
  - v_s = 3.288 km/s; t_l = 0.223/0.282 ns; t_l/t0 = 0.86/1.08.
  - E_3 expansion; P_abs = 0.467; lumped form within 10% for d/l < 0.074, max +13.5%.
  - Inversion l_f/d = 25.8 and 9.1; 0.105-0.193.
  - SiO2 layer: t_min = 0.855 at 0.725 THz; 1 nm -> 0.907.
  - The S-matrix trace argument for reciprocity (very clear for a QFT reader).
- **Outcomes.** All yes.

### 20.4 Quasiparticle yield
- **Lost points.**
  - L5. **"up to 40 percent"** is used inconsistently. The last paragraph of §20.4-film says that at t_l/t0 ≈ 0.5 "the film costs up to 40 percent of the infinite-volume yield". The book's own cascade at t_l/t0 = 0.5 gives 0.349 at 10Delta (cost 41%) but 0.238 at 60Delta (cost **60%**), and the sentence is about the detector band 16-62Delta. "Up to 40%" is Guruswamy's 2-10Delta range; §20.5 repeats it. Fix: "40% at 10Delta and 60% at 60Delta".
- **Steps reproduced.**
  - g_I(3) = 1.3221, giving t_pb = 0.792 t0; g_I(10) = 1.0505, giving 0.299 t0.
  - v_F/c_s = 311 and 1.6e-3; p_pb = 0.835 and 0.930; 0.4% at 200Delta.
  - The kinematic proof of Y = 2Delta/E below 4Delta.
  - My own event Monte Carlo of eq-cascade (t_l -> inf, alpha^2F ∝ E^2, 2500 events) gives Y = 0.597 at 5.46Delta, 0.594 at 10Delta and 0.591 at 30Delta, against 0.600/0.590 printed (statistical error about 0.005).
  - Isotope rates 140 and 2.1e3 s^-1; 39 m.
- **Minor.** "Three-phonon decay ... takes 0.3 s in germanium" uses A = 6.43e-55 (and no x_L). With the 1.61e-55 used everywhere else in the chapter it is 1.2 s, or 13 s with x_L = 0.098. The conclusion (ballistic) is unaffected, but name the constant.
- **Used before defined.** Eliashberg alpha^2F, Allen's formula and the case-I/II coherence factors were all introduced in chs 6-7, so they are fine, but I needed those pages open.
- **Outcomes.** Exact yield below 4Delta: yes. Write and solve the cascade equations: yes, I did. Yield vs t_l/t0: qualitatively yes; I did not rerun the finite-t_l numbers.

### 20.5 Collection kernels and discrimination
- **Lost points.**
  - L6. **Worked example "220 eV": "The most favorable corner of the 1sigma bands, Y_q = 0.098 and F_NR = 0.4, gives 1.72."** In the setting of the example (trapped carriers induce nothing) that corner gives **1.36**. 1.72 needs the corner *plus* the mean-charge limit (I get 1.724). The figure caption's dark band does include both, but the sentence misleads. The same 1.72 then appears in §20.5-hv and in the table.
  - L7. **"Its ceiling ... is that of the charge yield itself, 10.3 at 100 eV."** Eq-hv at g = 0 with the stated inputs (Y_q = 0.102, F_NR = 0.9, F_eh = 0.119, f_det = 0.873, 3.8/3.75 eV) gives **10.8**, or 14.3 with f_det = 1. With F_eh = 0.114 it is 10.9. I could not find inputs that give 10.3.
  - L8. The spread model of the low-bias route is under-specified. Is sigma_pos applied to both recoils? Is sigma_ph/E_ph taken at each recoil's own E_ph? Is the comparison at equal E_R, as the phi_Luke expressions imply, or at equal E_ph, as in the HV route? My reading gives varpi_O = 0.11/0.22/0.43 against the printed 0.13/0.24/0.45, at about 10-12 V. That is close, but I cannot confirm it.
  - L9. "g = Y_q^-1/2 = 3.1, near 12 V": with g = f_det g_Luke that is 13.4 V at f_det = 0.873, or 11.7 V at f_det = 1. f_det is only fixed later in the paragraph.
  - L10. Gap route: "Delta O_b changes sign at t_1 = 3.87 t_0". I reproduce 3.865, but it solves e^-x(1+x) = Y_q and so depends on Y_q = 0.102, which the text does not say. **t_0 also clashes** with the pair-breaking time t_0 of §20.4 (0.26 ns), used one section earlier. Rename (e.g. t_rel).
- **Inconsistencies across sections** (none blocking):
  - "primaries born at the **Debye energy, 62 meV**" (§20.5) vs "Debye energy omega_D = 55.6 meV" (§20.2), where 62 meV is the band top.
  - x_L = 0.093 (§20.2, Kelsey) vs 0.0975 (§20.5; I confirm 0.0975 from 9.0/5.4 km/s).
  - F_eh = 0.114 (§20.1, cascade) vs 0.119 (§20.5, measured; this is not said there).
  - omega_opt / f_s (§20.2) vs omega_op / f_soft (§20.5) for the same quantities.
- **Steps reproduced.**
  - 2.68 pairs; v/2d; vbar = 5.752 km/s; absorption times 15.3 and 30 us; bare-face 1.0/2.07%.
  - Mean-field solve: shares 40.5/58.3/1.2%, a_prim = 0.590.
  - r_coll = 0.991 (sub-gap absorbed; printed 0.992).
  - eq-sign; s_sub at all eight quoted points; s_ng = -0.0475 and +0.002; +0.062/+0.058 for Y_inf = 0.5.
  - eq-lowbias and its maximum 0.516.
  - eq-hv derivation and the 220 eV example (16.76, 10.70, 3.41, 1.220, 0.431; 1.50; 1.32; F_NR < 0.213; F_NR = 0 still 1.72 < 2).
  - Delta_soft = 0.015; 0.28 (1-b).
- **Could not reproduce.** "down-converted to a mean energy of 4.4 meV" and "a quarter of the energy arrives below 3 meV". In my mean-field solve, which reproduces the shares above, the absorbed energy has an energy-weighted mean of 5.0 meV and a number-weighted mean of 3.95 meV. The absorbed energy below 3 meV is 18%; the resident energy below 3 meV is 31%. State the weighting.
- **Own-field comments (statistics).**
  - S_sep >= 2 as "useful" is a weak criterion. For equal Gaussians it is roughly 84% NR acceptance at 84% ER rejection. The CDMS rejection quoted next (1 in 10^3) corresponds to S of about 6. One sentence on what S = 2 means in rejection would stop a particle physicist from reading "useful" as "background-free".
  - Corner scans of correlated Y_q/F_NR bands are fine as a conservative envelope, but say whether the two are correlated in the source.
  - No errors in particle physics: there is little of it, and the HL units are consistent.
- **Condescension.** None. The Cherenkov analogy and the S-matrix framing are pitched well for me.
- **Outcomes.** Define kernels and functionals: yes. Mean-field solve: yes, I reimplemented it. Sign of r_coll - 1: yes. HV ceiling: yes. Low-bias requirement: approximately.

### Verdict (b): MINOR GAPS
Nothing blocks the following material. L6 and L7 are wrong or ambiguous printed numbers in the chapter's headline results (also in the summary and the table) and should be fixed first. Then L5 and the 1.4 um / 1.2 meV slips.

## Persona (c): condensed-matter theorist (DFT, many-body), no dark matter

### Section by section
- **20.1.**
  - No lost points.
  - The deformation-potential vertex |M|^2 = D^2 Q/(2 rho V c) and the LA-only coupling for isotropic D are standard and correct.
  - Herring-Vogt, the Xi_u transverse coupling and the omission of TA emission are honestly listed.
  - The Poole-Frenkel lowering 2 e E r_E (Coulomb center in a field) is correct.
  - The dark-matter framing (why the readout matters for an exclusion limit, what "flashing" is for) was clear enough from the opening.
  - Used before defined, for me: "ionized fraction f_ion" and "collection ratio r_coll" (ch19, fine).
- **20.2.**
  - Tamura's isotope rate: I rederived the matrix element of p^2 (factor 2 from the two orderings), the cubic-site polarization sum delta_bg g_kappa/3 and (pi/6) g omega^2 g_ph. Correct, including the Debye reduction to 4 pi^3 g Omega <c^-3>.
  - Transverse stability in the isotropic continuum (collinear T -> T + T with a vanishing vertex) is correct and properly qualified for real crystals.
  - The rate hierarchy argument (isotope mixing faster than decay, so the decay rate is x_L Gamma_anh) is the right effective description.
  - The sapphire exception is well argued.
- **20.3.** AMM/DMM are standard (Swartz-Pohl form for the DMM). Reciprocity via flux-normalized S-matrix unitarity is correct and nicely general. The Voigt rather than Hill average is a choice; I would mention Hill once, since Al is nearly isotropic either way.
- **20.4.**
  - Case I for phonons and case II for photons are correct.
  - The Kaplan split and emission kernels are as in Kaplan 1976.
  - The low-energy alpha^2F = bE^2 means a normal-state linewidth linear in E, which is consistent with Allen.
  - The "exact" yield below 4Delta is a clean kinematic statement. I agree, and my Monte Carlo confirms the 0.59 asymptote.
  - Expressing v_F in units of c (6.75e-3) is unusual for my field; 2.0e6 m/s would read faster.
  - The 40% vs 60% issue (L5) is the one real error.
- **20.5.**
  - Linearity and the definition of the kernel are sound.
  - The mean-field triangular equation is correct.
  - The sign analysis of r_coll is the most useful thing in the chapter for me.
  - New to me: S_sep, the "two-window" gap observable and the yield definition with 3.8 eV per pair are dark-matter-specific but introduced in place. The difference between Y_q and Y'_q took me a reread; one sentence on *why* the measured yields carry 3.8 eV would help.

### Errors or overstatements in my field
- None serious. Two small ones:
  - "Debye energy 62 meV" (§20.5) conflates the band top with the Debye energy, which §20.2 correctly gives as 55.6 meV for Si. For Ge, §20.4 also calls the band top (35.7 meV) the Debye energy, as Leman does. Pick one usage.
  - x_L: 9.3% (from anisotropic DOS, Kelsey) and 9.75% (isotropic speeds) are both used, without saying which is which.
- "in the isotropic continuum A_anh is a closed form in five elastic constants": two Lamé plus three Murnaghan constants. Correct.

### Pace and condescension
- No condescension.
- §20.3 spends a paragraph on the b-vector bookkeeping, which is slow for me but right for persona (a).
- §20.2's vertex scaling and §20.4's Allen/alpha^2F link are brisk; I filled them in from memory.
- §20.5's low-bias spread model is too brief to reproduce (L8).

### Outcomes (c)
- Isotope rate from masses: yes.
- AMM averages and reciprocity: yes.
- t_l for a given film: yes.
- Y_qp below 4Delta, and the cascade: yes.
- Mean-field kernels and the sign of r_coll: yes.
- What a dark-matter detector needs from these (the NR/ER separation logic): yes, after one reread of §20.5-routes.

### Verdict (c): MINOR GAPS

## Priority list
1. L6 (1.72 corner, 220 eV worked example, §20.5-hv, table) and L7 (10.3 vs 10.8).
2. L5: the 40% thin-film cost is really 60% over the detector band (§20.4-film, §20.5-sign).
3. The 1.4 um at 0.95 ns (book's own law gives 1.0 um); the hole <E_L> 1.2 vs 1.14 meV.
4. "4.4 meV" and "a quarter below 3 meV" in §20.5-meanfield: state the weighting.
5. Notation: t_0 clash; eps_0 (relative); omega_op/omega_opt; f_s/f_soft; F_eh 0.114 vs 0.119; x_L 0.093 vs 0.0975; Debye energy 62 vs 55.6 meV.
6. Under-specified: the low-bias spread model (L8); the dependence of t_1 = 3.87 t_0 on Y_q (L10); P_d energy weighting (L3); the face-sheet bound (L1).
