# Ch 17 mock-reader review: persona (a), isolated

Reader: first-year PhD student, direct detection (READER.md persona a). Read build/main.pdf pp. 969–1014 (PDF pp. 979–1024) linearly. I opened the tex only to check how the PDF lost the brackets of Eq. (17.9). I re-did every number I could in python, assuming vmax = 2.650e-3 (793 km/s) and v0 = 238 km/s.

## Global issues (all sections)
- **Broken cross-references.** "(??)" appears where Sect. 21.7 should be: intro p. 969, Fig. 17.1 caption, p. 995, p. 1003, p. 1006, p. 1012 (twice), Summary p. 1013. Sect. 17.1.1 p. 971 has "????" for the section on how much of a lattice deposit a phonon sensor collects. I cannot follow any of these pointers.
- **Fig. 17.1 graphic vs caption.** The box says "Sect. 17.5; Limit Check 17.5", but the caption and the text say Limit Check 17.1.
- **Notation clash.** In 17.2.3, n_B is the Bose occupation n_B(m_phi). In 17.4.2 (box of Eq. 17.11, and the paragraph after it), "n_B = 1" is the Born–Oppenheimer order. I read "n_B = 1" as an occupation of one quantum until context fixed it.

## 17.1 Scattering across channels
**Lost points**
- p. 974, 17.1.3 vs intro: the ratio 4.4e4 at 1 MeV times 16.7 gives 7.3e5, but the intro and Summary say "about 8e5". The difference is small, but the two numbers come from the same pair of rates.
- p. 975: "the mass of 12.3 MeV is a property of the model". The text is clear on this. But Table 17.1 lists 12.3 as a map edge, and the "(model)" tag there is easy to miss.

**Steps reproduced:** E_R^max (0.054, 5.3 eV); M/4m_chi = 6.5e3; q_max = 53.0 keV; x_R = 1.31; e^{-2W} = 1/2 at 6.3 MeV; impulse onset at 17.5 MeV; Migdal 6.07e-5 × 0.0537 = 3.26e-6; Poisson P(n ≥ 11; 1.76) = 2.53e-6; 11 × 63.7 meV = 0.70 eV; decay length 0.1/ln 65 = 0.024 eV; omega_x/E_R = 5.7 and omega_x/omega_top = 4.8; the e-fold of 0.020 eV and the 0.014 eV shift; Migdal opening 2E_g/v^2 = 0.316/0.333 MeV; 2.8–2.9 omega_top; acoustic edges 6.1 keV (Si) and 10.2 keV (Ge); GaAs polar 10.4 keV; GaAs direct floor 0.433 MeV with q = 1.15 keV; Z m_e/M = 2.73e-4; 2pi/a = 2.28 keV with 64 meV at the top of the branch.
**Could not reproduce:** none. The rates (crossover grid, shares 0.97/0.65/0.33) I take as computed.
**Used before defined:** none new. Terms recalled from earlier chapters without a reminder: "window", "first zero-phonon edge" (Ch 13), "electron-following sector" (8.6). Fine for someone who read Chs 8 and 13.
**Pace:** the crossover paragraph on p. 972 lists seven masses, five shares and six Migdal rates in a row. It is too dense to absorb on one reading. A two-column table would carry the numbers better.
**Outcome:** given a coupling, mass and threshold, name the dominant sector of Si and say why. *Yes.* Test: nucleon coupling, 30 MeV, omega_th = 1 eV. E_R^max = 0.054 × (29.97/9.996)^2 = 0.49 eV, and omega_x = 0.83 eV < 1 eV, so the sector is Migdal. The zero-phonon share is 0.10, so the event is phonon-dressed Migdal. The second outcome is to explain why a dark photon has no Si lattice channel when an electron-only mediator does. *Yes* (Z* = 0, so the weight goes as q^4).

## 17.2 Absorption across channels
**Lost points**
- WE 17.2, p. 981: "only a crystal absorbing 10 cm^-1 would move it 40 meV up". The square-root edge given just above, alpha = 13.3 (Delta/eV)^{1/2}, puts the handover at (10/(2.15 × 13.3))^2 = 0.122 eV, not 40 meV. My guess is that the TO replica, about 40 meV higher, takes over. If so, one clause saying so is needed, because as written the step contradicts the formula shown.
- WE 17.2: "eps2 = 2.5e-4 at 1.17 eV, an absorption coefficient of 4.6 cm^-1". From alpha = eps2·omega/(n_r ħc) with n_r = 3.48 I get 4.26 cm^-1. The Lorentz value checks (0.008 cm^-1).
- 17.2.3: it took me two passes to see that "the noise power fluctuates by (n_B+1)N_coh^{1/2}" is the step that gives the linear-readout significance. Stating "per-bin rms n_B+1, summed in quadrature" would fix this.

**Steps reproduced:** Eq. (17.1). The caps 0.043 (Si), 0.13 (SiO2), 7.7e-5 (TLS), 0.024/0.0016 (ZrTe5), 3.3e-9 and 4.4e-17 (Al). The YIG scan fraction 1.57e-5 and averaged reaches 4.0e-15 and 4.8e-14. WE 17.2: the factor 2.15, alpha_Si at 0.1 and 1 meV, the handovers 0.012 and 1.2 meV, and the factor of 2000. Eq. (17.2): e^{1/2} = 1.65 and e^{1/4} = 1.28. Thermal quanta 3.6e5 and 861. The zero-count masses 17.3, 20.1, 194 and 222 µeV (20–26 T), checked numerically. N_coh = 8.7e8; 4.9e4 against 3 (factor 127); 3200 quanta, 330 and 18. 0.86 µeV = 208 MHz.
**Could not reproduce:** the 40 meV and 4.6 cm^-1 above.
**Used before defined:** none.
**Pace:** good. Table 17.2 is the most useful object in the chapter for me.
**Outcomes:** (i) say which target absorbs a given boson at a given mass, and why longitudinal modes win for the dark photon. *Yes.* Test: a dark photon at 0.5 eV has no target (it falls in the 0.36–1.17 eV gap). (ii) Choose between a counting and a linear readout. *Yes.* Test: at 50 µeV and 10 mK, m/T = 58 > 26, so counting wins and is background-free for a day's record.

## 17.3 Exothermic and inelastic dark matter
**Lost points**
- p. 984, NiO paragraph: "The ratio 3.1 is that of v_nu to the mean speed, 3.77 ... The magnetic form factor reduces it, 0.60 on the shell against 0.89 elastic." But 3.77 × 0.60/0.89 = 2.54, not 3.13 = 8210/2620. A factor of about 1.23 is unaccounted for. It may be the weight 1.149 against an elastic weight suppressed near Gamma. Also, "it" in "reduces it" is ambiguous.
- 17.3.3, p. 986: "the rates are 1.12 and 1.39 times their elastic values, 976 events ... for single phonons and 16.7 for pairs." I first took 976 and 16.7 as the exothermic rates. Only "raised by 31" (3.0e4/976) shows that they are the elastic ones. Please reword.
- p. 988: "(v_max/v_nu)^2 ≤ 0.34 there" (10–80 eV). At exactly 10 eV I get 0.35. The bound holds from 10.3 eV.
- WE 17.3: the heavy rate at |Delta| = 0.5 eV. Scaling 0.0314 by (q_nu'/q_nu)^3 = 0.334 gives 0.0105, but the text says 0.012. The halo correction may be larger at lower v_nu. If so, say that 0.012 is the full integral.
- p. 983: "10 keV at the escape speed carries 35 meV". This uses v_max (escape plus Earth), not v_esc.

**Steps reproduced:** Eq. (17.5) from Eq. (17.3), including the 1/(pi Omega) prefactor and the slope q/m + u. Eq. (17.6) by completing the square; the free-electron check. The width 2 mu q v/|m*| and Eq. (17.7), including the normalisation of eta. The acoustic root and its relative width 2v_max/v_nu. NiO q_nu = 4.45 keV and 435 eV, v_max/v_nu = 0.61, width 58–60 meV. Plasmon: alpha_pl = 0.451, m* = 567 keV, mu = 362 keV, shares 0.638 and 0.946, line at 18.77 eV, q = 1.57 keV, width 5.3 eV, window 6.9 eV, threshold 15.3 and 14.6 eV. WE 17.3: the line weight 7.59e-4 eV, q_nu = 240.5 eV (0.110 of 2pi/a), v_nu, the 6 % halo correction, the full width 0.099 meV and 0.964 eV. **R = 1817 kg^-1 yr^-1 checked absolutely** from the boxed formula (rho_T = 5.32). The heavy rate 0.0314; 2600 at 0.5 eV; 2.6e4 at 10 keV. Eqs. (17.8) and (17.9) and all fifteen entries of Table 17.3. The percentages 12–28 % and 1 %; the factors 2.09 and 32; 4.73 MeV; 2.40 eV.
**Could not reproduce:** the NiO factor 3.1 and the heavy rate 0.012 above.
**Used before defined:** Delta S (zone average 1 + 2 Delta S) and w_q^M are recalled only by citation (WE 14.1, Eq. 14.2). That is acceptable.
**Pace:** 17.3.1–17.3.2 are dense but complete. This is the best derived section of the chapter.
**Outcomes:** compute the line position, width and rate for down-scattering into a mode, and the endothermic floor. *Yes.* Test: the Si optical phonon at Delta = +0.1 eV gives m ≥ 2(0.1641)/v^2 = 46.7 keV.

## 17.4 Interference between channels
**Lost points**
- p. 990: "What survives, Z*^2 screened by eps_inf, is the optical-phonon rate ..., smaller by 216 and 245 than the bare nuclear charges alone would give." The ratios 216 and 245 are Z^2/Z*^2 and leave out eps_inf. Say whether "smaller by" includes the screening.
- 17.4.2: I could not derive Eq. (17.10) from what is on the page. The factor (q·p_G)/(Omega M omega_e^2) comes from the boost Eq. (12.5), which is not restated here. I took it on trust. The reading "left to right" helps.

**Steps reproduced:** the ratios Z^2 : F^2 : -2ZF; Si -392 against 392; GaAs F = 28.89 and 35.11, 99.75 % and 99.81 %. m_e/M = 1.95e-5; (1 + Z m_e/M)^2 - 1 = 5.47e-4; 7.5e-8. Z/M = 0.4446 and 0.4405; 2 m_e z = 4.83–4.88e-4; (m_e z)^2 = 5.9e-8. Cauchy–Schwarz to Eq. (17.12). Eq. (17.13) to Eq. (17.14). The upper edge (4×) at V_nuc = -(M/m_e)V_e. (m_e/M)^2 = 3.8e-10. E_g/v_max = 0.19 and 0.26 of 2pi/a; q* = 0.52. M/m_e = 5.1e4 and 1823.
**Could not reproduce:** Eq. (17.10), Eq. (17.11) (on trust, see above).
**Used before defined:** theta_ep ("unique to relative order theta_ep") is used with no reminder of what it is. "Edge shell" and delta_w appear in the Fig. 17.5 caption without definition in this chapter.
**Pace:** 17.4.2 is too fast for me; it is the only place I had to stop reproducing. 17.4.3 is clear.
**Outcome:** decide whether a cross term enters for a given coupling, and size it at small q. *Yes.* Test: a dark photon in Ge gives 2 × 32 × 5.486e-4/72.63 = 4.83e-4 for both electronic sectors.

## 17.5 Figures of merit per channel
**Lost points**
- **WE 17.5, p. 1001 (contradiction).** "The figure of merit ranks the pair correctly, by a factor two, at every mass above the edges." But the table directly above gives 1+delta = 6.12 at 10 keV: diamond leads silicon by about 3 there, and 10 keV is above both edges (3.2 and 6.4 keV). The order flips somewhere between 10 and 20 keV. Restrict the claim, for example to "above about 15 keV".
- Polar log formula, p. 1002: the displayed ratio 1 - ln(omega_A/omega_B)/ln(2 m v^2/omega_B) does not say which v. With v = v_max I get 0.87 at 1 MeV and 10 % agreement at about 5 MeV, against the text's 0.77 and 52 MeV. With v ≈ v0 = 238 km/s I recover 0.79, 0.87 and 54 MeV. State the effective speed.
- p. 1001: the CsI "floor at 1.726 km/s, 20 % above the tabulated value". 1.726/1.379 = 1.25. Either "25 % above" or "the tabulated value is 20 % below".
- 17.5.2: "the argument ... applies to it unchanged". But g = eps^-1 - 1/eps_core(0) tends to 1 - 1/eps_core(0), not zero, at omega → ∞. The sum rule therefore holds only as an intermediate-asymptotic statement, with the core constants cancelling. I could repair this myself, but "unchanged" overstates it.
- 17.5.5, p. 1003: "the bound of silicon is 1.1e5 times that of LiF". That equals the ratio of the L-integral bounds alone. With the nuclear factor 3.38 the F_Mig bounds differ by 3.2e4. Say which is meant.

**Steps reproduced:** 1102/654 = 1.686 = 8.956/5.313. 2I1/I0 → 135 km/s; brackets 0.934 and 0.866; settling values 1.027, 0.932, 1.049 (CsI), 0.883 (diamond/CsI) and 0.905 (diamond/Ge); the 13.5 km/s rule. WE 17.5: 322.6; edges 3.19 and 6.39 keV; caps 0.42 and 0.65 MeV; every 1+delta in the table; u_- = 251 and 124 km/s; 3.9 edges; 0.9327. Speeds: 1.547, 1.551, 2.054; CsI 2.46, 2.37 and 42 %; CaWO4 8.4 %; CsI 3.73 and 6.49; edges 23.1 and 11.0 keV; CaWO4 1.96 and 2.10. omega_p^val = 16.61 eV; 433 eV^2; the factor 0.970; Eq. (17.16) (with the caveat above); 3.5; 28.4 MeV; valence electrons per nucleon 0.142, 0.055, 0.333 and 0.308. Polar: 134 × 0.77 = 103; edges 21.98 keV and 13.7–32.0 keV; 1.7 GeV (with v0). Migdal: 0.570, 1.928, 3.38; LiF omega_p = 26.1 eV, 3.87, 0.87; Ge 0.47; (omega_p/E_g)^5 = 5.7e5.
**Used before defined:** none in this section. kappa_eta, I0 and K_eta are recalled by equation number only.
**Pace:** the five-crystal audit of the Griffin table (pp. 1001–1002) is long for a section on figures of merit. It is worth having, but a table would shorten it.
**Outcome:** compute a figure of merit and its pairwise window, and check a tabulated sound speed. *Yes.* Test: Ge against diamond settles at 1 - (5.313 - 18.16)/135 = 1.095, which is at the edge of the band.

## 17.6 Ranking under uncertainty
**Lost points**
- Table 17.6, Migdal row: the header says "relative to Si at X_pole = 1", but Si is listed at 1.73. I needed a minute to see that the values are medians that include X_pole, whose median is √3 = 1.73. Then LiF 1.51/1.73 = 0.87 agrees with 17.5.5. A footnote would save the minute.
- 17.6.5: "GaAs, last in rate by a factor of 130". GaAs is 130× below the leader but only 65× below the next crystal (sapphire 9.12). Say "130 below LiF".
- Fig. 17.8: open symbols get an *upward* shift on cooling. The lead salts lead the plot, and I recall that their gaps shrink on cooling. If their listed gaps are room-temperature values, the convention moves them the wrong way. The text does not say which applies.
- Table 17.5 uses X_pole before 17.6.4 defines it. The forward reference is acceptable, but a pointer is needed.

**Steps reproduced:** the rms 0.064 and mean -0.048 of the JARVIS logarithms; 2.39 and 1.22; the sampling error ≤ 0.0035. Phi(0.242/0.122) = 0.977. CaWO4/GaAs 0.69. TeO2/CaWO4 0.988. The intervals [2.19, 2.60] and [1.92, 2.00]. GaAs/Ge about 0.88 → 0.73–0.74 with the 4.8 % offset. r = 0.5 → 0.9975. Si eighth. All heights and tiers of WE 17.6. The tiers of the nuclear-edge row (GaAs 6, CaWO4 7). PbSe 4.4× below Ge. GaSb 0.205 MeV. 24 crystals in 21 tiers. Diamond/sapphire 1.66. LiF/NaF 1.9. CsI 2.35 cold, 3.7–3.8, more than 1.5× TeO2.
**Could not reproduce:** none. P(first) and the X_pole results are Monte Carlo outputs, which I take as given.
**Used before defined:** X_pole (see above).
**Pace:** 17.6.1 is a long inventory of sources. The interval-order material (17.6.3, WE 17.6) is at the right speed and new to me.
**Outcome:** turn input provenance into P(first), rank intervals and tiers, and say what each claims. *Yes.* Test: for two computed speeds 10 % apart with sigma = 0.086 each, P = Phi(0.0953/0.1216) = 0.78 at r = 0, and 0.94 at r = 0.5.

## Summary and Table 17.7
They agree with the body. "The two are equal for masses below the temperature" (counter against linear readout) is loose: the ratio tends to one only for m << T.

## Overall
I would keep reading. The chapter does what its opening promises: it puts channels from seven chapters on common axes and turns them into a few material numbers with stated windows. Almost every number I tried came out right, including the absolute rate of WE 17.3 and all of Table 17.3. Nothing blocks the material that follows. The defects are local:
- an unresolved "??" to Sect. 21.7 in eight places;
- one false claim in WE 17.5 (the ranking is correct at every mass above the edges);
- two steps in WE 17.2 that do not follow from the formula shown (40 meV, 4.6 cm^-1);
- the NiO ratio 3.1;
- an unspecified v in the polar log formula;
- the n_B clash.

Sect. 17.4.2 is the one place where I had to take a derivation on trust.

**Verdict: MINOR GAPS**
