# Chapter 13: mock reader (a), first-year PhD student, isolated review

Read: ch13/*.tex (s13-1 to s13-9) and appD/D-35, D-36, D-37, read straight through; the PDF is current.
Checks: about 60 numbers re-derived in Python (numpy/scipy) and every displayed derivation I was pointed to
redone on paper. Unless a point below says otherwise, every number I checked reproduced to the digits printed.

## 13.1 The indirect-gap window
**Reproduced.** The parabolic m_ZP is 0.4246 MeV at q = 1.460 keV, with shortfall 0.480 keV and kinetic energy 0.189 eV.
The floor is 0.3332 MeV at q = 883 eV, and depositing the gap at q = k_c needs 0.4739 MeV. The exciton shift is 0.00249 MeV.
For the onset, the stationarity condition qv - 2E + qE' = 0 and m = 2E/(v^2 - u^2) both check.
The silicon onset takes two passes (883 then 894 eV, 0.463 then 0.458 (2pi/a)) and gives 0.3374 MeV. The sensitivity is 2.8e-4 MeV/meV.
The scaled TA branch gives 0.3378 MeV, the optical-edge phonon 0.3384 MeV and the bound pair 0.3332 MeV.
Germanium: the parabola gives 0.3241 MeV at q = 1.104 keV and the onset bracket is 0.2119-0.2141 MeV.
GaAs: m_g = 0.847 m_e and the [111] pair opens at 3.68 MeV. The [100] heavy-hole pair never opens, the onset is 0.433-0.436 MeV, and the L floor and edge are 0.517 and 0.561 MeV.
The direct-gap formula (13.1-mZPdir) follows from maximising qv - q^2/2mu, which gives mu v^2/2 = Eg.
**Lost.** None.
**Used before defined.** "the phonon-assisted process of Sec. 9.1": I have not read Chapter 9, but the sentence is understandable without it.
The bracket 0.40-0.42 MeV leans on Sec. 13.9, which is a forward reference, and the text says so.
**Pace.** Good. The germanium paragraph is long but readable.
**Outcomes.**
(i) Compute m_ZP and m_PA from the band and phonon data: yes, I redid Si, Ge and GaAs.
(ii) Say why the onset is insensitive to the bands: yes; u^2/v^2 is about 1e-5.
(iii) Say why a direct-gap crystal also has a window: yes; I rederived Eq. 13.1-mZPdir.

## 13.2 The phonon-assisted amplitude
**Reproduced.** All four denominators of (13.2-paths) follow from the intermediate-state energies. The three-swap fermion sign checks; D.35 shows it line by line. On shell, C becomes the B form and D becomes the A form with the sign restored, by direct substitution. The q = 0 cancellation works: path A with p = v gives g/omega, path B with p = c gives -g/omega. The frozen-phonon derivative gives Eq. 13.2-Mad. The error series in D.35 sums r/(1-r) to omega/(delta - 2 omega). The error estimates: 18.27/1.11 is 1.6%, 57.73/1.11 is 5.2%, and the 0.18 and 0.58 eV thresholds follow.
**Not reproduced.** The 924-determinant brute force of WE 13-exchange, which needs code I don't have.
I accepted the table, and its numbers agree with each other: the C/D values equal the blocked B/A values.
**Lost (minor).** "In silicon the bound for pairs at Q is at least 1.11 eV, and the binding one is the margin below the zero-phonon edge."
I first read "binding" as the exciton binding energy; "the tighter one" or "the one that binds" would avoid that.
**Used before defined.** None that blocked me: Herzberg-Teller, the base point and theta_ep all come from Ch. 8.
**Pace.** Right. The repeated statement of the signs (text, then D.35) helped.
**Outcomes.**
(i) Write the four paths with their signs: yes.
(ii) Prove the unrestricted band sum on shell: yes, from D.35.
(iii) Say why there is no interference with the zero-phonon line at order g^2: yes (orthogonal phonon occupations).
(iv) Get the adiabatic form and its error: yes.

## 13.3 The phonon-assisted rate
**Reproduced.** Counting the factors gives (2 pi/V)*2*N^-1*N^2 << >> = 4 pi/Omega. L^PA uses e^2 = 4 pi alpha and gives 8 pi^2 alpha/(Omega q^2). Near the edge, (13.3-near) follows from the convolution of two 3D densities of states, (m_e m_h)^{3/2} x^2/(16 pi^3). Combined with 4 pi Omega it gives Omega (m_e m_h)^{3/2}|M|^2 x^2/(4 pi^2). Exact. In the cone average, u = kappa theta^2 gives C x^3 <1/kappa>/12; the LA case gives C x^4 r^2 <1/kappa^2>/48. The cost ratio is x(a1 + a2)/24 = 1.2e-3 at 0.1 meV, and the solid angle is pi x/kappa. The first term of kappa is 16.9 x 0.983 x 0.507/(2 x 0.477) = 8.83 meV (8.85 printed, rounding). The window bound on |Q*| is 614 eV, i.e. 0.62 keV. The tilt shift (1/2) M_eh u^2 is 0.015 meV for TA. The C4v product rule makes LA forbidden on the axis.
**Not reproduced.** The kappa ranges over azimuth (2.3-8.5, 18-24, 16.8 meV) and the 1.34 keV off-axis crossover.
Both need the force constants; I accepted them.
**Lost.** None. The rule "D free variables give x^{D/2-1}" is a good unifier.
**Used before defined.** delta_w = 0.3 eV is used here, but only Sec. 13.6 fixes it; the text points forward.
**Pace.** Slightly fast in the group-theory paragraph: the step "LA is Delta_1" is asserted.
One more sentence on why an in-phase longitudinal displacement is invariant would help a reader without group theory.
**Outcomes.**
(i) Write S^PA and L^PA with the right normalisation: yes.
(ii) Derive the onset exponents 2, 3 and 4: yes.
(iii) State when S^0 plus S^PA double-counts (the f-sum): yes, qualitatively.

## 13.4 Screening of the phonon-assisted rate
**Reproduced.** The macroscopic factorisation in D.36: R = Rbar + Rbar v0 R gives (eps^-1)_G0 = (1 + v0 R00)[delta + (fbar Rbar)_G0], and 1 + v0 R00 = 1/eps_mac. It checks. The band-sum theorem from the density matrix (D.36), with the occupation differences. The rigid-translation limit: v_C[R0(omega_f) - R0(omega)] = eps(omega) - eps(omega_f) gives 1/eps(omega_f) - 1/eps(omega). WE 13-external: 1/6.31^2 = 0.025 and 1/6.93^2 = 0.021; 1/5.52^2 = 0.033 and 1/6.20^2 = 0.026; the ratios are 1.31 and 1.25. The ratios to 1/eps_inf^2 are 2.9-3.4 and 3.6-4.5, and RPA misses the measured value by 13% and 22%. The k_xc estimate: n = 0.1998 A^-3, k_F = 1.808 A^-1, (0.983/3.62)^2 = 0.074, giving 0.05. The pair-channel factor 1/eps^2 for eps = 2.9-3.8 is 0.07-0.12.
**Not reproduced (taken on trust).** "The equation of motion of the pair element is that of a first-order coherence driven at omega_f ... its numerator is the amplitude". The analogy with a single field is plausible, but I could not derive it myself. The optical-theorem paragraph (the absorptive part of W equals W-dagger times Im R0 times W). D.36 sketches it with a reference to Eq. 8.7-factor, which I accept but did not rederive.
**Lost (minor, not blocking).** The pair channel is the hardest page of the chapter.
I can follow the classification of the three places where screening enters and the two limits. I could not compute delta_n^(2) for a real case.
The text is honest that nobody has done that calculation.
**Pace.** Too fast in "The pair channel" (second-order TDHF in one paragraph); D.36 fixes most of it. The screening-factors subsection is clear.
**Outcomes.**
(i) Say why exactly one 1/eps_mac survives: yes.
(ii) Size the external factor at 1 keV from tabulated eps: yes.
(iii) Write the pair-channel term: yes, formally; I cannot evaluate it.
(iv) Name the classes left out: yes.

## 13.5 The optical limit
**Reproduced.** The Ward identity (13.5-ward), from first-order dressed states. The prefactor 8 pi^2 alpha/(Omega omega^2). The forward-transfer arguments: absorption replica at omega - DeltaEg + 2 omega_nu. The inverse series, with r = n/(n+1) = e^{-omega/T}. The occupations: n_TA(77 K) = 0.0680 and r = 0.0637; TO r = 1.7e-4; at 300 K, 0.49 and 0.11. WE 13-TA-transfer: forward ratio 1.469; inverse terms +1.1908, -0.2154, +0.0272, -0.0029, +0.0003, partial sums to 1.00002. Exact. Untransferred 77 K factors: 2.65, 1.90, 1.47, 1.29; the factor of 2 is reached at x = 22.8 meV (23 printed); with 0.88, 2.33, 1.68, 1.29, 1.13 and x = 18.5 meV. Stanford strength factors e^{-c1 T}: 0.61 and 0.88.
**Small inconsistency.** The 300 K factors "38, 16 and 7" match my two-branch model (38.4, 15.7, 7.0), not the TA branch alone (34, 14, 7.5).
The preceding sentence ("TA alone and two-branch to two digits") is true only for the 77 K factors. Say which model gives the 300 K numbers.
**Lost.** None.
**Pace.** Good; the worked example is exactly the right size.
**Outcomes.**
(i) Show lim L^PA = eps_2^PA: yes.
(ii) Say why L equals T for cubic crystals: yes.
(iii) Transfer branch-resolved data between temperatures, and say why the transfer is ill-posed without branch resolution: yes; I re-ran the series.

## 13.6 Soft phonons, resonances and the off-shell window
**Reproduced.** The Ward identity D.37: the ratio is +1 or -1 band by band, and the sum is the commutator. [s, e^{iqr}] = i l (e.q) e^{i(q+Q)r}. WE 13-soft, bracket: deformation (-15.237 - 0.0329 x 1.450)/11.083 - (-4.563 - 0.0329 x 0.776)/5.943 = -0.607. The table says -0.6076. The factor 10.4: dropping the Galilean terms (q - p_cc + p_vv = -0.046) gives (0.0667/0.0207)^2 = 10.4. The extremum case: 2.09 +/- 4.86 A^-1, an amplitude ratio of 2.5, and D/c of about 225 A^-1. Silicon numbers: D/c_nu = 320 keV and Q_min = 0.3/16.7 = 0.018 A^-1; m* c_nu = 1.0e-3 and 6.7e-3 A^-1. The ratios that set the margin: 0.21, 0.19-0.24, 0.05 and 0.09; theta_ep (0.25/0.3)^2 = 0.69; theta_ep times delta_w/E_w is about 0.2.
**Minor issues.** D.37-Qmin is labelled "for emission", but with +omega_Q the emission bound is delta_w/(v - c). The printed delta_w/(v + c) is the absorption bound, which covers both signs. It is harmless numerically, but the label is wrong. WE 13-soft: "Setting the interband vertices to zero now halves |M|^2". That holds for one sign of Q only; for the other, |4.91|^2/|2.09 - 4.91|^2 is about 3.
**Not reproduced.** The window end at 1.07 keV for a 0.5 eV margin, and the widths of 3-21 meV; both need the bands and a literature rate.
**Lost (minor).** "Resonant denominators beyond the window" and "The Fano term" use the Dyson convention, finite parts and delta_F from Secs. 2.4 and 8.6 in a compressed way.
I followed the logic (cascade goes to the zero-phonon sector, finite part to the sideband), but would not trust myself to build a table beyond the window from this text alone.
That is acceptable, since the book says only totals are quoted there.
**Pace.** The soft-limit part is well paced. The resonance and Fano subsections are fast.
**Outcomes.**
(i) Say why soft acoustic phonons are harmless: yes.
(ii) State the window theorem and the margin: yes.
(iii) Explain why S^+ can be negative beyond the window: yes.

## 13.7 Temperature and zero-point renormalization
**Reproduced.** (13.7-sqrt) in closed form: -pi (2m)^{3/2} sqrt(omega)/2 times Omega g^2/(2 pi^2). The numbers give 1.98, 0.43 and 0.75 meV for 0.44, 0.16 and 0.23 m_e, a total of 3.2 meV. The coefficients: 2/(v+u)^2 = 0.283 MeV/eV, and 2 m^2/q^2 = 0.187 for m = 0.407 MeV, q = 1.33 keV. I also rederived q* = 2E/(v - u) and the 2/(v+u)^2 form. WE 13-windowT: DeltaEg(300 K) = -46.2 meV, onset 0.3243 MeV, shift 0.0131 MeV. The sidebands open at 0.3157 MeV (n = 1.25) and 0.3027 MeV (n = 0.10). At 77 K the shift is -0.0011 MeV and the sideband starts at 0.3279 MeV. (1 + omega/x)^3 < 1.1 needs x > 31 omega, which is 0.46 eV. n_B(14.8 meV) is 3.5e-8 at 10 K and 1.9e-4 at 20 K. The 13.7-WLdiff bracket has zeroth moment 0 and first moment +omega_Q.
**Not reproduced.** The special-displacement cancellation of cross terms is argued heuristically and cited, and the model figure is accepted as shown.
I understand why it works (neighbouring modes become degenerate), not how fast.
**Lost.** None.
**Used before defined.** The zero-phonon edge "0.405-0.408 MeV" and q_ZP = 1.33 keV come from Sec. 13.9 before that section derives them. They are flagged as forward references, but they are used inside a worked example.
**Pace.** OK. The special-displacement proof is fast but optional for my purpose.
**Outcomes.**
(i) Write the renormalized S^0 and the f-sum transfer: yes.
(ii) Say why a special-displacement spectrum must not be added to S^PA, and by how much it misplaces the onset: yes.
(iii) Shift the window with temperature: yes, reproduced.

## 13.8 Excitons with phonons and phonon-assisted absorption
**Reproduced.** The free limit of (13.8-M) gives the four paths. The normalisation (2 pi g/(N V)) V Sum_P = 4 pi Omega Int d^3kappa/(2 pi)^3. The line weight 4 pi E_b^{3/2}/n^3 in continuum units, and the coefficients 32 and 8/pi of (13.8-edge). The continuum edge (32/3) E_b^{1/2} x^{3/2}; the lines hold the free weight within 8.0 E_b (from 4 pi zeta(3)). The thresholds 1.1728, 1.1838 and 1.2122 eV. The excitonic/free ratio for the two branches: 80.5 at 1.200 eV, 15.6 at 50 meV, 7.3 at 100 meV; the 1s share is 0.744 at 1.200 eV. The kinetic-row identity (13.8-MT): the h-part gives g(eps_v - eps_c)/omega = -(1 -/+ omega_Q/omega) g. WE 13-darkphoton-edge: Stanford 5.5 x 325 x 0.0477^2 = 4.07 cm^-1; L = 1.51e-6; R = 9.3e27 zeta^2. This gives zeta = 1.8e-14, with ratios 6.6 and 17. The ALP/dark-photon ratio is 7.3e-9.
**Lost (minor).** In WE 13-darkphoton-edge the "Loss function" step writes alpha_abs without saying which of the four values just listed is used (4.16, 2.95, 4.8, 27.3 cm^-1).
Only 4.16 (the Stanford fit) reproduces eps_2 = 2.44e-4; I had to work that out backwards. One phrase would fix it.
**Not reproduced.** The 0.154 scale ratio and the 6.4/4.0/0.77 cm^-1 at 1.21 eV need the fits; I accepted them.
**Pace.** The completeness and two-pair subsection is short and honest. The scalar paragraph is dense but rederivable.
**Outcomes.**
(i) Write the replica amplitude and its free limit: yes.
(ii) Derive the Wannier-Mott replica edge: yes, all coefficients.
(iii) Get a dark-photon rate from a measured edge: yes.
(iv) Say why the dark photon has no new amplitude: yes.

## 13.9 The silicon window
**Reproduced.** m_ZP = q^2/(2(qv - E)) = 0.4077 MeV for q = 1.33 keV and E = 1.355 eV. The 1s shift is 0.0028 MeV. The glide algebra: w = (a/2)(1,1,0) and w/2 - tau = (0,0,-a/4); G'.w/2 = -pi; the h + k = 0 mod 4 rule. The mass-edge integrals: Int x^p (F - x)^2 = 2F^{p+3}/((p+1)(p+2)(p+3)), and the q integral gives F0^{p+3}(2 m F0)^{1/2} B(1/2, p+4). Hence p_on + 7/2. F0 = 3.5 meV per 0.001 MeV; (1 - 0.0004/0.005)^{6.5 to 7} = 0.56-0.58. The largest energies above the first edge: 0.015, 0.066, 0.115, 0.161 eV, consistent with my fixed-q values 0.012, 0.064, 0.113, 0.160.
**Not reproduced.** eps_2 = 5.9e-4 from 11 cm^-1 at 1.25 eV. With n_r = 3.57, eps_2 = n alpha (hbar c/omega) gives 6.2e-4; 5.9e-4 needs n of about 3.4. State the n used, or correct the number. Everything computed on the Wannier and plane-wave bands: the optimum point, the beta values, the glide-zero numbers, the ratios 0.02-3.9, and the cross sections 3e-29, 7e-32, 1.3e-31 and 4e-34 cm^2. These are presented as computed or estimated, with status labels, so this is expected.
**Lost (minor).** The rate-estimate paragraph (form factor 0.12, model dielectric function, error budget giving a factor of 4 quoted as 10) packs five steps into one paragraph.
I understand what was done; I could not redo it without the inputs.
**Pace.** The edges and glide subsections are well paced and the worked example is excellent. The rates subsection is fast but labelled as an estimate.
**Outcomes.**
(i) Say why the first zero-phonon edge is off axis and weak: yes.
(ii) Apply the glide rule (13.9-glide) to an Umklapp class: yes, reproduced -pi.
(iii) Derive the mass power p_on + 7/2: yes.
(iv) Read the window table and its status labels: yes.

## Summary section
**Error.** "The external factor is one inverse macroscopic dielectric function ... 1/40 to 1/48 in the loss function at 1 keV".
In Sec. 13.4 and WE 13-external, 1/40 to 1/48 is the head-only value, 1/eps_00^2 = 0.021-0.025.
The macroscopic value is 1/30 to 1/38 (0.026-0.033), and the nuisance table has it right.
The summary pairs the word "macroscopic" with the wrong number.

## Exercises
The chapter has no exercise set, so I worked these myself from the text alone:
(1) The GaAs zero-phonon direct threshold and onset bracket (Eq. 13.1-mZPdir and Eq. 13.1-mPA).
(2) The 77 K to cold transfer at x = 15-100 meV.
(3) The onset mass and window at 300 K.
(4) The Wannier-Mott replica coefficients.
All four were doable and matched the printed values.

## Cross-cutting
Cross-references are very dense: Secs. 8.4-lines, 8.6, 8.7, 2.4, App. E. Having read Ch. 8 I could resolve them all, but 13.4 and 13.6 are hard to follow without Ch. 8 open beside them. The status labels (computed / estimate / open) are applied consistently and helped me know what to trust.

## Overall
I would keep reading. Sections 13.1-13.3, 13.5, 13.7 (renormalization and temperature) and 13.8 are fully reproducible from the text, and I reproduced essentially every number I tried.
The pair channel (13.4) and the convention-heavy resonance and Fano material (13.6) went past me in places, but the book itself labels them as not computed or as totals-only.
Nothing downstream depends on my reproducing them.
The concrete defects are small: the summary mislabels the 1/40-1/48 screening factor as macroscopic; the alpha_abs used in WE 13-darkphoton-edge is ambiguous; the "for emission" label on D.37-Qmin is wrong; the 300 K transfer factors are not attributed to a model; eps_2 = 5.9e-4 in 13.9 is not reproducible with the stated n_r; "binding" in 13.2 reads ambiguously; "halves |M|^2" in WE 13-soft holds for one sign only.

**Verdict: MINOR GAPS**
