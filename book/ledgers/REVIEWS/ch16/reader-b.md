# Ch16 mock-reader review: personas (b) and (c), isolated
Read: Chapter 16 (ch16.tex, s16-1 to s16-9, summary) and App. D.41, D.42, as .tex sources (I checked the PDF build time: current).
Read linearly. Recomputed every derived step with sympy/scipy (scripts in the session scratchpad). Read no briefs, ledgers or sources.
**Shared result of the recomputation.** Every closed-form step and worked-example number I could redo agrees with the text. That covers
WE 16-factor (bracket 5.545+3.142i, eps 50.73+6.08i, L = 2.33e-3, ratio 0.61, published 3.73 = 1600 L, the 5/3 scheme 0.54,
3.35e30 zeta^2/kg-yr, zeta 9.5e-16); the threshold masses 10.5/12.7/9.4/11.3 keV (my own kinematics with v_max = alpha/2.75); the Sommerfeld
and binding numbers; D.41 in full (L_pub = eps_bg^2 L, R_DD, Lambda', the 288 pi^4 prefactor, Gamma_pub = eps_bg Gamma); F_th 0.95/0.85/191 eV;
the I0K0 10 % point (0.383); g_c 0.176/0.225/0.357 and 7.3/5.7/3.6 v_max; 2.1x for 4 vs 1 channel; the parabolic-band correction
(numerical root against the closed form); the demon WE (k_F, v_a, q_s, 4.81 meV, 0.160, 1.75e-4, 1.37/3.8 keV); the stack kernel sum; the EMT
identity; eq. 16.2-inplane (direct boundary-value solution) and eq. 16.2-corr; eq. 16.3-R1D (overlap, roots, integral = g v_D); the
tube kernel limit; the Fermi factors 7.3/3.4/2.6; the depolarization algebra and WE; 9 pi/8kR; mu/4 omega = 4.05e4; the Davydov sums
(1.693, 0.934 vs 0.937, 0.1871); the E-state valley sum 2/9 and the intervalley |q| values; the GOS bracket (hydrogen continuum
f = 0.435; Du's 0.30 and 4.85); WE 16-sip-line in full; the Clausius-Mossotti numbers; the LiF masses and Lindhard/Kinchin-Pease numbers;
q_min(H2) = 134 keV and 25.9 MeV; the STM Jacobian and norm; the relaxation limits pi/4, 1/3, pi^4/8, pi^3/12; K_ph = 4.63e4;
1.34 K and 1.15 neV; WE 16-tls-dp; the scattering prefactor 9.0e-3 and the core/host ratio 2.45 (my own SHM: median q 1.73 keV);
sigma_crit 1.16e-38; D.42 in full (J_ph, alpha_ohm = 4K_b, arctan form, the case-I ratio, sinh u K1(u)); the 16.8 rates 1.8e5 and 2.5e9 s^-1;
T_coh 2.4 Delta_r; Gamma ratio 0.71; kappa_PB series; WE 16-heat (1.64e-7 J, 46/1.9/0.27 pW, 0.84 uJ); eq. 16.9-power; the WE 16-band ratios.
What I could not reproduce is the output of a full numerical model: the ZrTe5 rate and reach curves, the OPW spectra, anthracene PPP, the donor line strengths, the limit-box curves.

## Persona (b): particle physicist, QFT yes, solid state no

**16.1 Dirac rates.** *Lost:* none. In the opening, "the factor 1.2 that the Dirac electrons contribute alone" made me stop. It is
|1 + eps_D/eps_bg|^2 = 1.09^2, which one clause would say. *Not reproduced:* 98 events/kg-yr, the 2e-40 cm^2 reach, the 4800-6600 range,
0.86-0.94, the 87 % polarization share, 6.2-6.3. All are numerics; each is plausible against my eps_bg^2 and eps_bg^(1/2) checks.
*Used before defined:* "remote bands" and "clamped-ion constant" (both clear from Ch 7), and "ionic poles" (Sec. 5.5, fine).
*Pace:* the published-rate paragraph (charge at the cutoff, Eq. 3.13 of the reference) is dense. I needed D.41 to follow it,
and the pointer is there. *Outcomes:* (i) write L with the total eps: yes. (ii) Convert a published reach (sigma x eps_bg^2,
zeta x eps_bg^(1/2)): yes, I did it for WE 16-factor. (iii) Bound the factor below by (alpha/v_max)^2 = 7.6: yes. (iv) Name the next-order
corrections and their sizes: yes.
*Own field:* the QED analogy is correct. g_deg alpha/(6 pi v_D) ln(4 v^2 Lambda^2/s) is the vacuum polarization of one Dirac fermion
with c -> v_D, and the "+5/3" is the MS-bar constant. The Sommerfeld variable pi alpha~/b correctly uses the relative velocity 2b. No condescension.

**16.2 Low-dimensional plasmons.** *Lost:* "the long-wavelength form ends at q = 30 eV and 0.30 eV" reads as two momenta. It means
q = 30 eV and omega = 0.30 eV. *Used before defined:* the Luttinger parameter g_c appears in the opening sentence and is defined only in eq. 16.2-wire;
add a forward pointer. "Drude weight" is defined at first use (good). *Not reproduced:* the 2860 km/s for the Si plasmon. With a free-electron
v_F for the Si valence gas I get about 2750 km/s, so the value depends on Ch 10.3 inputs I did not recheck. *Pace:* about right; the stack
section is long but every step is shown. *Outcomes:* derive the 2D and 1D kernels: yes. S_1D and its f-sum: yes. Explain why a mode
faster than v_max is reachable: yes. The demon velocity and weight: yes. The EMT stack: yes.
*Own field:* the bosonization remark (RPA exact for linear bands with forward scattering) is correct, the loop-cancellation theorem.
No condescension.

**16.3 Graphene, tubes, dots.** *Lost:* none. *Used before defined:* "maximally localized Wannier functions" and "pseudopotential" sit in an
inputs paragraph; I could skip them. *Pace:* the OPW paragraph lists ratios (0.46-25, 740) faster than I can picture them. The text says
itself that "a table of ratios is not a rate correction", which helps. *Outcomes:* write the ejection rate: yes (factor 1/4 pi checked). Explain
the q -> 0 defect of plane waves and the OPW cure: yes. Derive the 1D massive-Dirac response from Lorentz invariance plus current
conservation: yes. That argument is Pi^00 = q^2 Pi(s), the Ward identity, and I liked it. Dot depolarization: yes.
*Own field:* "invariant under boosts with v_D" is used correctly. No error.

**16.4 Molecular crystals.** *Lost:* the BSE kernels paragraph. "Direct kernel contains overlap densities phi*_c phi_c'''" assumes
Sec. 4.9's index conventions, and I had to reread 4.9 to see which kernel is "exchange". The four-prime index is hard to parse.
*Used before defined:* Pariser-Parr-Pople, Mataga-Nishimoto, zero differential overlap, Platt notation and Ewald summation are named, not explained.
That is acceptable for a model description, but a non-chemist cannot judge "the model is a guide to sizes". *Pace:* fast in 16.4-bse, fine
after. *Outcomes:* derive the binned sum rule (eq. 16.4-binned): yes, completeness of A^lambda. Size intensity borrowing (first order): yes.
Explain the quadrupole argument for daily modulation: yes. Bound A_day: yes (0.98, 0.39, 0.68, 0.09, 0.17, 0.08, 0.13 reproduced).
*Own field:* nothing.

**16.5 Dopants.** *Lost:* none. *Used before defined:* "umklapp" (Sec. 16.5, T2 paragraph), which I assume Ch 5 defined. *Pace:* the
valley-orbit paragraph lists many momenta at once, but I reproduced them all from 0.85(2 pi/a). *Outcomes:* write S^D with the
host screening once: yes. Compute a line's absorption and reach (WE): yes. State when first order fails (4.8e15 at the line): yes.
Explain the E-line directionality: yes.
*Own field:* absorption rate = zeta^2 (rho_chi/rho_T) L, with hbar restored: correct.

**16.6 Color centers, bonds.** *Lost:* none. *Not reproduced:* the limit-box curves (numerics). *Pace:* fine. *Outcomes:* write the
hand-off rate with Y_CC: yes. Recover Budnik et al. as a limit: yes. Compute q_min and the bond mass threshold: yes. The impulse
dissociation condition and its difference from improved Born (omega_vib/4): yes.
*Own field, error:* "their sigma_e times A^2/mu_chi n^2 is sigma_N,kappa/mu_chi kappa^2". In this book sigma_e is the electron reference cross-section.
The per-nucleon cross-section of Budnik et al. should carry its own symbol (sigma_n). As written it reads as a book-wide notation clash.
Also, the CM Doppler shift "(<omega>_CM/4M_1)^(1/2)" equals (<omega>/2M_mol)^(1/2) only for a homonuclear molecule. Write the general form.

**16.7 Glasses.** *Lost:* (1) "When every system relaxes fast, omega tau_1 << 1, the u integral is pi/4". Because tau_1 grows as 1/u^2,
systems with small u are never fast. The plateau needs omega tau_1(u = 1) << 1, and the pi/4 comes from the u ~ (omega tau_min)^(1/2) region.
I reproduced pi/4 only after rereading it this way, so the condition needs rewording; the result is right. (2) Notation: S is the strain
(eq. 16.7-H1) and S(q, omega) the structure factor (eq. 16.7-S) in the same section. R is the body radius, and two paragraphs later the
reflectance R = |(k - k')/(k + k')|^2. alpha is the absorption coefficient next to the fine-structure constant (16.7-ir).
*Not reproduced:* none of the closed forms; the limit curves are numerics. *Pace:* the STM part is well paced for me. The random-medium
part is quick but self-contained. *Outcomes:* derive tan delta = tan delta_0 tanh: yes. Derive the dark-photon rate and the single tanh: yes.
Compute WE 16-tls-dp: yes. The host-term scattering rate: yes. The Born criterion sigma_crit: yes.
*Own field, imprecision:* "at qR >> 1 this beats the homogeneous term by a factor of order R/xi_c" omits the factor (delta n/n_0)^2, which is
7e-4 for Ti-6Al-4V. The optical-potential criterion and sigma = 4 pi b^2 are correct. The conclusion (at 4e-38 cm^2 the Born treatment fails)
follows, and I agree.

**16.8 TLS at millikelvin.** *Lost:* none in the text. I needed App. C.20 for J_s normalization (J = pi sum lambda^2 delta). D.42 states it
("each mode contributes 2 pi lambda^2 delta to 2J"), but 16.8 relies on it silently. *Not reproduced:* the 0.21 K crossover and the
2e-9 s^-1 at 50 mK, only roughly (I get 1.7e-9). *Pace:* the ohmic-scaling subsection is fast. "Duplication and reflection formulas" is left to the
reader; I accepted eq. 16.8-scaling by checking only its ratio to Delta~_0^2/gamma_0. *Outcomes:* derive Gamma_1 from J_s: yes. Phonon and
electron J_s: yes (D.42). The superconducting factor: yes. The heat-release law: yes, and WE reproduced. T_coh: yes.
*Own field:* the instanton and Wigner statements are correct, and the T_x = omega^ddagger/2 pi divergence of kappa_PB is right.
In WE 16-heat, "0.05 x 3 = 0.15": the 3 (= specific-heat density over heat-release density, minus one) is not said.

**16.9 Inputs.** *Lost:* none. *Outcomes:* convert an input range into a reach band with the power p: yes (eq. 16.9-power checked). Classify
targets as theory, calculation or data limited: yes. **Summary:** "overstate scattering by eps_bg^2 and absorption by eps_bg ..., by at least
7.6": the 7.6 bound holds for scattering only; for absorption it is alpha/v_max = 2.75.

**Verdict (b): MINOR GAPS.** Nothing blocks the material that follows. The blocking risk is the "every system relaxes fast" phrasing in 16.7,
and a reader who takes it literally cannot get pi/4. I would keep reading: the chapter's best feature is that every published formula is
recovered as a stated limit.

## Persona (c): condensed-matter theorist, DFT and many-body yes, dark matter no

**16.1.** *Lost:* "Three events in a kilogram-year reach about 2e-40 cm^2". The step from a rate to a reach is in Ch 1.5 and 8.8, and
I needed Eq. 1.5-limscaling to see why sigma_lim scales as 1/rate. The pointer is given only in 16.9. A one-line pointer in 16.1 would help.
*Own field:* the RPA with a local eps_bg, the Thomas-Fermi k_TF^2 = e^2 N/eps_bg, the excitonic binding Delta alpha~^2/4 and the
next-order list (ladder, self-energy, vertex, doping, ionic poles) are all correct and fairly stated. The warning that a computed eps tensor
contains the Dirac pairs is the right one. *Outcome:* yes.

**16.2.** *Own field:* the Keldysh form, the 2D Lindhard (Re f2 = 1 exactly inside the continuum), the demon weight and width, the
superlattice kernel and the EMT are all correct. The Lasenby-Prabhu identity "at every filling" is true; I checked it symbolically. Nothing is condescending:
the Drude-weight and f-sum reminders are brief. *Outcome:* yes.

**16.3.** *Own field:* the OPW argument is standard and correctly framed, including the warning not to multiply OPW by a Fermi factor.
The 1D massive Dirac response and its van Hove edge are correct. The quantum-dot closure rule is correct. *Lost:* the dark-matter kinematics
"q_perp r_t >= 2 n v_D/3 v_max, independent of radius" took me a moment. It combines omega = 2 Delta_n with q >= omega/v_max, and
saying so would help this persona. *Outcome:* yes.

**16.4.** *Own field, three points.*
(1) Double counting of the environment. The model levels are shifted so that E_La = 3.1 eV, the measured crystal value, which already contains the
whole 0.4 eV gas-to-crystal shift. WE 16-davydov then adds J_11 = -0.20 eV, giving excitons at 2.89/2.92 eV. That is 0.2 eV below the measured
crystal absorption that was used to fix E_La. The text notes that J_11 is "about half" of the 0.4 eV, which implies that E_x should sit near 3.3 eV.
The limit box re-shifts by 0.27 eV, but WE 16-davydov and Fig. 16-anthracene ("lowest singlet at 3.1 eV") use different
conventions. State which energy is the molecular E_x and keep it fixed.
(2) "L_b has no dipole at all" is a property of the PPP/CIS model of an alternant hydrocarbon (pairing theorem). In real anthracene ^1L_b is
weakly allowed along the long axis. Say "in the model".
(3) The model Davydov splitting (31 meV, lower component b-polarized) could be compared with the measured value for anthracene, about 25 meV,
also with b lower. The comparison would support the claim that the model "sizes" J.
Also: the binned sum rule assumes a Hermitian H^F (Tamm-Dancoff); that is implicit and worth one word. *Outcome:* yes.

**16.5.** *Own field:* the multivalley donor, the valley-orbit selection rules and the central-cell correction are correct, as is the Clausius-
Mossotti saturation. The 1/eps_host^2 "counted once" argument is correct and clearly contrasted with 16.1. *Outcome:* yes.

**16.6.** *Own field:* the yield factorization is sensible. "Lindhard ... its use for a fluorine recoil in a compound is a model choice" is an
honest statement. F-center optics, the F2/F3+ wavelengths and the self-trapped exciton route are correct. *Lost:* the hand-off formula (eq. 8.7-handoff)
and the "prompt window" are dark-matter-framework terms. I had to go back to 8.7, and the pointer is given. *Outcome:* yes.

**16.7.** *Own field:* the STM, the factor-2 convention for Delta_as >= 0, tan delta_0 = pi P p^2/3 eps_r and C = P gamma^2/rho c^2 are standard and correct.
The relaxation integral is correct, but see persona (b) on "every system relaxes fast". The comparison of the deposited oxide with the
vibrational absorption at 6.4 meV lies above omega_IR = 4.3 meV, outside the A + B omega^2 law the same paragraph relies on. Flag it as an extrapolation.
*Lost:* the scattering crossover "q_x = |f_host|/(8d)" is the aligned (q parallel to d) estimate. With the orientation average the text itself uses,
128(1 - sinc) = |f_host|^2 gives q d = 0.62, about 1.2 keV, not 0.71 keV. The conclusion (most of the rate lies outside the host window) is unchanged.
*Outcome:* yes.

**16.8 and D.42.** *Own field:* Black's rate, Jackle's rate, the case-I coherence factor, the Born versus phase-shift coupling, the orthogonality-
catastrophe normalization and the Leggett Delta_r are all correct. I recomputed sinh u K1(u) and the large-u limit (pi/8u)^(1/2). The remark
on the spin convention of K (factor 4) is valuable. Minor: the "1.8e5 s^-1 below 0.1 K" is the T -> 0 value; at 0.1 K, coth(1.2) = 1.2. Say
"at 10 mK". *Outcome:* yes.

**16.9.** *Lost:* none. The classification is useful to me: it says which numbers a condensed-matter calculation would change.
*Outcome:* yes.

**Condescension (c):** none found. Pointers to Ch 4-7 replace re-derivations of RPA, BSE and BCS.

**Verdict (c): MINOR GAPS.** The only own-field error of substance is the E_x/J_11 bookkeeping in 16.4. It does not block, but it makes the anthracene
energies internally inconsistent by about 0.2 eV.

## Combined list of fixes (both personas)
1. 16.4: fix the molecular E_x convention (3.1 eV includes the environment, then J_11 is added again); align WE 16-davydov, Fig. 16-anthracene and lim:16.4a.
2. 16.7: reword "every system relaxes fast/slowly" as "the fastest systems (u = 1) relax fast/slowly, omega tau_1(u=1) << 1 / >> 1".
3. 16.6: replace "their sigma_e" by the per-nucleon symbol; write the CM Doppler width as (<omega>/2M_mol)^(1/2).
4. 16.7: rename the strain (or the structure factor) and the reflectance (or the radius); add (delta n/n_0)^2 to "beats the homogeneous term".
5. 16.7: q_x with the orientation average (about 1.2 keV), or say "aligned estimate".
6. 16.2: "ends at q = 30 eV and omega = 0.30 eV"; add a forward pointer for g_c at first mention.
7. 16.4: "L_b has no dipole in the model (alternancy)"; compare the 31 meV splitting with experiment.
8. 16.8: "at 10 mK" for 1.8e5 s^-1; in WE 16-heat say where the factor 3 comes from.
9. Summary: the "at least 7.6" applies to scattering; absorption at least 2.75.
10. 16.1: say once that the factor 1.2 = |1 + eps_D/eps_bg|^2.
