# Chapter 17: mock reader review, personas (b) and (c)

Text read: tex/ch17/ch17.tex, s17-1 ... s17-6, s17-summary (the brief allows these sources; PDF stated current). I also looked at the rendered Fig. 17.2 (sectors). I read nothing else except earlier chapters, to check where terms are defined.
Arithmetic checked with python/scipy (SHM v0 = 238, vesc = 544, vE = 250.5 km/s, so vmax = 794.5 km/s = 2.650e-3).
Reproduced exactly or to rounding: every kinematic ceiling and edge in §17.1, Tab. 17.1 and Tab. 17.3. The crossover worked example (P(N>=11; 1.76) = 2.53e-6; e-fold 0.020 eV; shift 0.014 eV). The L <= 1/2|eps1| caps. The counting/linear ratio, its thresholds (17.3/20.1 ueV at 10 mK, 194/222 ueV at 100 mK; 8.7e8 bins; 4.9e4 quanta; 330/18) and the scan average 4.1e-15. The g_agg conversions. The exothermic shell formula and the parabolic line, width and eta profile (the normalization ∫eta = 1 is right). The NiO, plasmon (m* = 567 keV, 0.638, 18.77 eV, 5.3 eV) and GaAs WE numbers, and all endothermic edges. All F, Z*^2, (1 + Z me/M)^2 - 1 = 5.47e-4 and 2 me zbar numbers. The c_NR1 shift (2I1/I0 = 5.879/vmax, i.e. 1/135.1 km/s). The diamond window table. The CsI, CaWO4, GaN, AlN and ZnO speeds. The pole factors 0.87 and 0.47. Every closed-form pairwise probability in §17.6 (0.977, 0.689, 0.884 -> 0.741, 0.987, 0.997). The tier heights of WE 17.6.

Discrepancies found by both personas (numbered once, cited below as [Dn]):
- [D1] WE "cross terms of a heavy dark photon in GaAs", electron-following cell: "without the cross cell their rate would be 216 times (gallium) and 245 times (arsenic) larger" is wrong. Without the cross cell the sum is Z^2 + F^2 = 1795.6 and 2321.7, which is 403 and 521 times Z*^2 = 4.452. 216 and 245 are Z^2/Z*^2, the nucleus *alone*, which is how §17.4-cells (correctly) phrases it. Fix: "without the electron cloud" or the numbers 403/521.
- [D2] WE 17-handover: "only a crystal absorbing 10 cm^-1 would move it 40 meV up". From the displayed alpha_Si = 13.3 cm^-1 sqrt(x/eV), 2.15 alpha = 10 gives x = 0.122 eV, not 40 meV. The 0.1 and 1 cm^-1 cases (0.012, 1.2 meV) do reproduce. If the 40 meV uses the further replicas of eq. 13.8-edge (TO/LA open within ~60 meV), say so. Otherwise correct it.
- [D3] §17.3-silicon, the elastic baselines do not agree. 16.7 pairs = 1.39 x elastic gives an elastic rate of 12.0. The chapter opening, §17.1 and the summary say 17. The "gain of 3e6" at 80 eV fits 17 (5.3e7/17); with 12.0 it would be 4.4e6. The phonon case has the same problem. 976 = 1.12 x elastic gives an elastic rate of 871, and 3.2e4 at 10.3 eV is then 37x. The text (and the summary) say "at 10 eV ... raised by 31", which needs a 15% drop between 10.0 and 10.3 eV; Gamma ~ q^3 gives only 4.5%. Fix: state which elastic rate Fig. 17.4 uses, and recompute 31 and 3e6 against it.
- [D4] Plasmon window, §17.3-lines: I take the stated dispersion (alpha_pl = 0.451, E_F = 12.47 eV) and the continuum edge q vF + q^2/2m. They meet at q = 2.30 keV, which puts the window 7.3 eV above omega_p at 1 MeV. The text has 2.24 keV and 6.9 eV. Say which continuum edge is meant.
- [D5] §17.1 GaAs: (A/M)_Ga - (A/M)_As, with natural abundances (Ga 60.108/39.892 %), is 2.70e-5 per u, against the 2.59e-5 in the text. Give the definition used.
- [D6] §17.1: the Migdal endpoint E_R^max reaches the 89 eV end of the tables at about 414 MeV, not "above about 500 MeV" (at 500 MeV E_R^max = 129 eV).
- [D7] §17.2: "1/eps_host^2 = 1/130" implies eps = 11.4, but two paragraphs earlier silicon has eps1 = 11.7 (1/137). Presumably 11.4 is the cold value; say so, or use one value.
- [D8] §17.5 CsI: the floor 1.726 km/s is 25% above the tabulated 1.379. "20% above" is the tabulated value expressed relative to the floor (20% *below* it).
- [D9] §17.5 Migdal: "the bound of silicon is 1.1e5 times that of LiF" holds for the per-p energy integral alone. With the nuclear factor (x 1/3.38) the F_Mig bound ratio is 3.2e4. Say which is meant.
- [D10] §17.6-rankings: "GaAs, last in rate by a factor of 130". 130 is the ratio to the leader LiF (134). GaAs is 65x below its neighbour sapphire.
- [D11] §17.3 NiO: the elastic-to-exothermic ratio 3.1 is "v_nu/<v> = 3.77, reduced by the form factor". But 3.77 x 0.60/0.89 = 2.54. The missing factor of 1.22 (the shell weight 1.149 against the elastic weight?) is not explained.
- [D12] §17.3-endo: "lighter than the gap of silicon by a factor of two, against 32 for elastic". 32 holds for GaAs; for the NiO magnon the elastic ratio is 333/7.16 = 47.
- [D13] §17.1: "the one-phonon term 2W e^-2W stays the largest single order until 2W passes one". P1 > P2 until 2W = 2, and the map's own criterion (P1 against P>=2) flips at 2W = 1.26. Say "until 2W reaches about 1.3, where the sum of higher orders overtakes it".
- [D14] §17.6 opening: "TeO2 has the softest lattice of the crystals we compare", but §17.5 compared CsI at 2.40 km/s. Add "in the pool".
- [D15] Summary, last paragraph: L(k, omega). §17.5 writes L(p, omega) for the same object.

## Persona (b): particle physicist, QFT yes, solid state no

**Opening and Fig. 17.1.** The motivating numbers (17 against 8e5) set up the chapter well. Lost point: "reads the atlas of Chapter 9 along the interaction axis". I have not read Chapter 9 and the phrase carries no content for me. One clause saying what the atlas is (a table of channel x target?) would do.

**§17.1 Scattering.**
- Lost: none blocking. The kinematic-ceiling argument, M/4m_chi between lattice and electronic ceilings, is exactly the argument I would make for a nucleus against an electron. Clear.
- Not reproduced: [D5], [D6], [D13]. The crossover WE I reproduced fully, including the factor-of-two robustness. "about the inverse of the Migdal probability per kick" is plausible (1/(6.07e-5 x <E_R>) ~ 8e5 at 10 MeV for <E_R> ~ 20 meV), but I had to guess the mean E_R.
- Used before defined: none (q_BZ, impulse onset, Helm, 2W and the Debye-Waller factor are all in Chs. 2 and 11).
- Pace: the nucleon-map paragraph (labels, which response in which q range, how the Migdal deposit is formed) is dense. It is fine for a reference, but I reread it three times. A bullet list of the four labels with their criteria would read faster. The electron-coupling subsection is the best part of the chapter for me: "a detector below the gap tests whether the mediator couples to total charge or to electrons alone" is a sharp, model-building-relevant statement.
- Outcome (explain each boundary by kinematics or screening; get the ceilings): yes. I computed E_R^max(10 MeV) = 53.5 meV, omega_max(1 MeV) = 3.51 eV, the Migdal floor 0.317/0.334 MeV and the acoustic edges 6.13/10.2 keV.

**§17.2 Absorption.**
- Lost: none. The bound L <= 1/2|eps1| and its corollary, that the strong absorbers are longitudinal modes, are clean.
- Not reproduced: [D2], [D7]. I checked the readout derivation as a particle physicist would. The variance of chaotic counts, n(n+1) per mode, and the linear-amplifier noise n + 1 (half a quantum at the input, half added) are both correct, and the ratio e^{m/2T} follows in one line. The cited thresholds reproduce to 1-2%.
- Field check: the conversions zeta -> g_agg = zeta m/B (10 T = 1953 eV^2) give 5.4e-13, 5.8e-13 and 8.4e-11 GeV^-1. The text has 5.4, 5.9 and 8.8, all within the rounding of zeta. No error in my field. No condescension: the chapter does not re-explain kinetic mixing or the ALP couplings, which is right.
- Used before defined: none in my reading. Ioffe-Regel (Ch. 16), the Kittel line (Ch. 14) and the loss tangent (Ch. 16) are all earlier.
- Pace: Tab. 17.2 plus its two prose paragraphs restate each other. Acceptable.
- Outcome (read coverage; say where a counter beats a field measurement): yes. At 10 mK, a day and 24.8 ueV I get N_coh = 8.72e8 and 4.86e4 quanta, a ratio of 128 in the coupling.

**§17.3 Exothermic and inelastic.**
- Lost: none. The Jacobian (q/m_chi + u_nu)^-1 is derived in two lines and is easy to verify. The eta-shaped line profile is a neat result. I checked the normalization ∫_0^∞ eta du = 1 analytically.
- Not reproduced: [D3] (most visible: the summary repeats "31"), [D4], [D11], [D12]. A minor one: at |Delta| = 0.5 eV the heavy-photon rate 0.012 is the full integral (the shell form gives 0.0105), while the light-photon 2600 is the shell form (2619). Say which.
- Field check: "the rate per particle of exothermic down-scattering is n sigma v_nu" is the standard inelastic-DM statement and is correctly made. No error.
- Outcome (rate into a collective mode; line position and width; endothermic thresholds): yes. I rebuilt all 18 entries of Tab. 17.3 from eqs. 17.3-endogap and 17.3-endolin, including the change of case for the Si acoustic row at 10 meV.

**§17.4 Interference.**
- Lost: none at the level of structure. The momentum-conservation lock (the mass density has no O(q) matrix element to excited states because P is conserved) is the cleanest argument in the chapter. I could reproduce it from ∂_t rho_m = -div g.
- Not reproduced: [D1]. That error matters, because the WE is where a reader takes the number from.
- Field remark: the closing paragraph says that a mediator with nucleon coupling about 1823x its electron coupling "lands there". A particle physicist will want a model: a Higgs-portal scalar (y_f ∝ m_f, with f_N ~ 0.3) is the natural near-"proportional to mass" case, while B-L is not (per nucleon = per electron). One clause naming it would anchor the result.
- Used before defined: "Born-Oppenheimer order n_B" (Ch. 8, fine). The window margin delta_w in the Fig. 17.5 caption needs a pointer to Ch. 13.
- Pace: eq. 17.4-Mmig and the following paragraph are fast for me (polarization vectors, the G sum, pseudopotentials), but I can follow what each factor does.
- Outcome (write the cross term; list when it vanishes; apply the bound and the small-q lock): yes, except evaluating 17.4-Mmig, which needs band data.

**§17.5 Figures of merit.**
- Lost: the partial f-sum derivation. I follow the logic, but "applies unchanged" leans on Appendix C.5, which I have not studied in detail. It is acceptable because conditions (i) to (iii) are listed.
- Not reproduced: [D8], [D9]. For the polar weight ratio, the displayed asymptotic formula gives about 0.87 at 1 MeV (with v ~ vmax), against the "full" 0.77 in the text. The 0.77 and the 52 MeV cannot be rebuilt from the chapter. Say that the asymptotic form is poor at 1 MeV.
- Used before defined: "Laue class 4/m" and "Brillouin scattering" are not defined anywhere in the book (grep of Chs. 1-16 and the appendices). The Christoffel problem is defined (Chs. 5, 11).
- Outcome (define rate and reach FoMs and the pairwise window; derive the c_NR1 shift): yes. Ge/Si settles at 1 + 3.643/135 = 1.027 and C/Si at 0.932, both as stated.

**§17.6 Ranking.**
- Lost: none. As someone used to Bayesian nuisances, I find the provenance widths honest. The repeated "conditional on the widths" is welcome.
- Not reproduced: [D10], [D14]. Small: the medians in Tab. 17.6 (LiF 18.9, NaF 9.93) differ from the §17.2/§11.2 inputs (19.0, 9.95) by more than the Monte Carlo error on a lognormal median (~0.2%). If the cause is the computed density, say so.
- Field check: Var ln(xA/xB) = sA^2 + sB^2 - 2 r sA sB follows from eq. 17.6-zmethod. Correct.
- Outcome (P(first), rank interval, tiers; the effect of correlation): yes. I reproduced the WE heights and the r = 0.5 value 0.997.

**Persona (b) verdict: MINOR GAPS.** Nothing blocks. [D1] to [D3] are numerical slips that a careful reader will trip on, and [D3] reaches the summary. I would keep reading.

## Persona (c): condensed-matter theorist (DFT, many-body), no dark matter

**Opening.** Clear. I needed vmax, the meaning of sigma_e and the "standard halo" from Ch. 1, and found them. The chapter does not over-explain the dark-matter side to me.

**§17.1.**
- Lost: none. Field check: the screening statements are right. The vanishing Born charge in Si makes S_ZZ acoustic start at q^4, a nucleon vertex is not screened by the electron dielectric function, and F = Z - Z* is the cloud charge. The model electron-following sector (28 electrons per cell follow the nuclei, linear LA branch to 2pi/a) is crude, but the text says that the 12.3 MeV crossing "is a property of the model, not of silicon". Good.
- Not reproduced: [D5], [D6], [D13]. The Debye temperatures (374, 645 K) and the elastic edges reproduce.
- Pace: the dark-photon/Si cancellation is stated in the opening, §17.1, §17.4 and the summary. For me that is repetition, not condescension. Once with a pointer would do.
- Outcome: yes.

**§17.2.**
- Lost: none. L <= 1/(2|eps1|) is elementary and well used. The handover WE (eps2 = n alpha/omega, L = alpha/(n^3 omega), factor 2.15) is correct.
- Not reproduced: [D2], [D7]. Field check: the claim that the damped-factorized eps2 tends to eps_inf(gamma_L - gamma_T)/omega far above the line is correct and well spotted as an artifact. Clean Al, eps1 ~ -(omega_p/omega)^2 ~ -2e8 at 1 meV, matches the order quoted.
- Outcome: yes.

**§17.3.**
- Lost: none. Field check: the plasmon dispersion coefficient alpha_pl = (3/5) E_F/omega_p is the RPA value (from (3/10) vF^2/omega_p). Correct, though the RPA coefficient is known to overestimate dispersion in real Si; one sentence would warn the reader. The GaAs LO weight (pi omega_L/2)(1 - omega_T^2/omega_L^2)/eps_inf = 7.585e-4 eV reproduces.
- Not reproduced: [D3], [D4]. The negative LO group velocity giving a line 0.071 meV below omega_L is consistent with u q/2 = 0.075 meV.
- Outcome: yes.

**§17.4.**
- Lost: none. Field check: the rank-one argument from momentum conservation is correct and elegant. The gauge independence of the product of amplitudes is correctly argued. The requirement of one set of bands and phonons for both amplitudes is the right warning. The frame ambiguity of the boost (transition densities fixed or following the ion) is honestly flagged.
- Not reproduced: [D1].
- Outcome: yes.

**§17.5.**
- Lost: none. Field remarks:
  (i) The partial f-sum with eps_core constant is exact *within* the model that conditions (i) to (iii) define. The "large-frequency tail" of g is an intermediate asymptote, not the true omega -> ∞ limit, which is 1 - 1/eps_core(0). Say "within this model" rather than "unchanged".
  (ii) Ge "with the 3d shell in the core" and eps_core ~ 1: the Ge 3d shell (~29 eV) is shallow and polarizable, so eps_core(0) - 1 for Ge is far larger than Si's 0.0154. The measured Ge plasmon (~16 eV) sits above the free-valence 15.6 eV. The factor 0.47 therefore carries an unflagged core-screening and d-hybridization error of tens of percent. Flag it, or apply 1/eps_core^2.
  (iii) The LiF valence count of 8 includes F 2s (~30 eV binding), and Li 1s lies at ~55 eV, so the window below the "first core edge" is narrow for LiF. This affects the 0.308 ceiling number.
- Not reproduced: [D8], [D9]. Field check: the elastic constants (Ge 131/49/68, CsI at 4.2 K, CaWO4) and the Christoffel speeds reproduce. The Laue-class remark is correct but undefined for persona (b).
- Outcome: yes.

**§17.6.**
- Lost: none. Field remark: the systematic low bias of the database speeds (-4.8% mean, all three the same sign) is the expected signature of a GGA-type functional underbinding. Name the functional JARVIS used, since the sign of the offset follows from it and a reader from DFT will ask. The provenance width of 0.07 for DFPT Born charges and eps_inf is reasonable. eps_inf is often overestimated by 5-15% in LDA/GGA, with a known sign, which again argues for the correlated variant.
- Not reproduced: [D10], [D14]. Tiers and interval order are defined well enough in the text that Appendix C.13 is not needed.
- Outcome: yes.

**Summary.** Faithful to the sections, but it carries [D3] ("31 times") and [D15].

**Persona (c) verdict: MINOR GAPS.** No error in my field that changes a conclusion. Items (ii) of §17.5 and [D1] are the ones I would fix first.

## Overall verdict: MINOR GAPS
Both personas could reproduce every derivation and almost every number. Nothing blocks the material that follows. Fix first, in priority order: [D1] (wrong factor in a worked example), [D3] (inconsistent elastic baselines, repeated in the summary), [D2] (handover number cannot be reproduced from the displayed formula), and the Ge core-screening caveat in §17.5.
