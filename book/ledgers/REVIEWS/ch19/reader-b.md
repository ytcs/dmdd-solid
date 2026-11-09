# Chapter 19 mock-reader review: personas (b) and (c)

Text read: tex/ch19/*.tex (the PDF is newer than every source file, so the two agree), linearly, with Ch. 1–8 and 10–18 as background.
Checked with sympy/scipy: every closed-form step and nearly every number in 19.1–19.6 and the WEs. Reproduced exactly, among others:
the Wigner shift (19.1-wigner) and deposit (19.1-dH); sigma_omega = 0.72 eV; the 1.6 deg scatter; all the WE 19-boundary numbers (0.41/0.54 eV, 11.24 eV/A^2,
xi_M = 15, 0.87/4.6 keV, masses 28/32/154/262 MeV/1.3 GeV); omega_max and E_R,th (352/336/399/387 eV); p_min = 1.86 k_F; Fano spread 170 eV; Migdal
3.9e-4/4.4e-4; c_L, a_L, k_L, J = 0.4742, 3.29 k_L; y_L (0.153 @0.1, 0.210 @1, 0.302 @10, 0.346 @20, 0.507 @100 keV; Ge 254 eV 14.3 %); the Bethe algebra and
PDG limit; I_val = 20.3 eV (19.0 at Gamma = 2 eV) and the 88/7.8/2.4 % f-sum split; ln I = 5.082; the Kinchin–Pease derivation; xi_d = 0.70 (0.72 at 10 E_d) by my own
marching solution with T^{-4/3}; the WE 300 eV counts; all bound/table entries; Ge E_d = 4.3 eV/4.6/28/35/24; (19.5-calib), (19.5-first), (19.5-bound) and (19.5-widen)
symbolically; 1.407/1.280/1.017; 3.5/3.6/4.1 %; r_coll = 1.154 (1.123–1.178, 1.144), 1.077; 0.9195/0.935/0.913; delta_gap = 0.048; lambda_tun 27.5/36.7/25.2;
47.2, 2.7e-15, ~443; the three-state WE at 1, 10 and 100 years; the defecton D (incl. the I_0 solution, 5/576, 0.28 and 0.93 Delta, local exponent -7.9, alpha_P = 1.27,
the Pushkarov match at eps(p) = Delta/4); crowdion d_k, E_kink, M_cr, the -a^2/72d^2 correction, Mathieu bands 90/166 and 13/34 micro-eV; the Borel asymptotics.

---------------------------------------------------------------------------------------------------
## Persona (b): particle physicist (QFT, no solid-state physics)

### 19.1 Nuclear recoil on the BO surface
- Lost points: none blocking. The hand-over is the best part of the chapter for me: the Weyl symbol of T(p)+V(x) is the classical H, so the
  deposit E_R + q.p/M per trajectory and the IA mean and width follow at once. I checked that (q^2/M^2)<p_q^2> = E_R<omega> at T = 0 with E_kin = <omega>/4 per component.
- One stumble: "1.49 A" appears twice for different things: the cage turning point at 12.5 eV (WE) and the head-on closest approach at 20 eV (19.1-md).
  I first took them for the same quantity. Say "closest approach (Tab. E-md-si)" and "cage amplitude" explicitly.
- Used before defined: t_pr shows up in the Fig. 19-recoil caption (regimes subsection) before 19.1-partition defines it. Bond defect, tetrahedral site, (1-10) plane,
  polarization vector e_{kappa s}: defined in Ch. 3/5/7, which I have read; fine.
- Pace: right. The MD acceptance tests (19.1-md) are fast for me (machine-learned potential, quench at fixed cell), but App. E is cited for details. Acceptable.
- LOs: hand over the kicked ensemble (yes); compute the four regime numbers and boundaries (yes, all reproduced); write and justify the partition (yes).

### 19.2 Electronic excitation by the recoil
- Lost points: none. The moving-wall argument is a nice second derivation of (19.2-transfer).
- Small inconsistency: the free-gas fraction "vanishes at E_R,th" (text and Fig. 19-yield(b) caption), but with the -m_e v_N term kept in (19.2-pmin) it vanishes at the
  exact threshold 336 eV. At 352 eV I get 1 - (0.9765)^3 = 0.069, which is the "0.07" the text quotes in the next sentence. Say "vanishes at 336 eV, the threshold with v_N^2 kept".
- Landau–Zener, the double passage 2P(1-P), and the Born parameter Z alpha/v_F = 14.6 (Ge 34.8) are correct in my field's conventions.
- Not reproducible from the text alone: the pseudopotential momentum-tail fractions (23 %, 2.2 %, 0.34 %; 0.27/0.047/5.6e-3/4e-4). They are model outputs, which the text says.
- LOs: derive the binary threshold (yes); explain why it is soft (yes); write the kernel and the chain to <N_eh> (yes, conceptually); size the Migdal share of a measured
  yield and avoid double counting (yes, 3.9e-4, one part in 261). The double-counting paragraph is exactly what a particle-side reader needs.

### 19.3 Stopping of slow ions
- Lost points: none blocking. I reproduced the impulse-deflection form theta = -eps^{-1} dI/dbeta (with p = mu v, mu v^2 = E), the Rutherford limit f = 1/2x,
  the eps^{1/6} asymptotics (p = 7/6, J = 0.4742) and the Bethe derivation including the cancellation of q_0.
- **Error (my field, the only real one I found): WE 19-lnI, "Normalized instead to the exact (pi/2) omega_p^2 ... 174 eV".** With a spectrum whose weight is 1.015 times
  the f-sum, (2/pi omega_p^2) Int omega L ln omega is not invariant under a change of energy unit: ln(omega/eV) and ln(omega/keV) give different I. Working in keV I get
  ln I = 1.015 x (5.082 - 6.908) => I = 157 eV, not 174 eV. Only the self-normalized 161 eV is a unit-independent number. Either drop the 174 eV or renormalize the spectrum
  shape-preservingly and say how the excess weight is treated; then the claim "173.0 eV ... inside this range" needs rewording.
- Awkward sentence: "the prefactor 2Z^2 alpha/pi v^2 ... becomes 4 pi Z^2 alpha^2 n_e/(m_e v^2) . (2/pi omega_p^2)" reads as if something changed; it is an identity
  rewrite. "equals" would be clearer.
- Small inconsistency: the constant-binding yield "vanishes for E_R <= 2U", and with U = 0.15 keV that is 300 eV, but the text and Fig. 19-yields say 298 eV. Either U is not
  exactly 0.15 keV or the onset is not 2U; one sentence fixes it.
- Not reproducible: lambda_L = 1.283, the peak 0.43 of f_LSS, the numerical solution (3 % / 4–5 % / 13 %) need the Thomas–Fermi numerics. Stated as computed; fine.
- Pace: the Lindhard-name disambiguation is useful, not condescending. The PDG cross-check of the Bethe formula is welcome.
- LOs: derive Lindhard's equation and its small-energy law (yes); list its hidden assumptions (yes); derive Bethe from L(q,omega) and say why it fails for recoils (yes).

### 19.4 Defects and stored energy
- Lost points: 19.4-calib and 19.4-bounds are **forward-loaded**. Luke phonons, r_coll, delta_coll, f_ion and the result (19.4-fDF) are quoted from 19.5 before 19.5
  derives them, so on a linear read I took (19.4-fDF) on trust and could verify it only after (19.5-first). Possible fixes: move 19.4-calib and 19.4-bounds after 19.5, or
  give the two signal formulas (19.5-signal) here, since the four-line derivation then follows at once.
- Reproduced: the KP equation and c = 1/2E_d; xi_d = 0.70 (my own solve: 0.700 asymptotic, 0.717 at 10 E_d); the WE (2.69 x 7.5 = 20.2, the text has 20.1: a rounding
  nit); all bounds, the table, and the Ge E_d sensitivity.
- Choice I questioned: the bounds on p_surv E_FP/E_d and the 10 keV survival statements use NRT's 0.8, although the section has just argued that 0.70 is the
  consistent screened value. The caption says 0.70 raises the bound by 14 %; I would make 0.70 the main entry, or say why 0.8 was kept.
- LOs: compute <E_st> from basins (yes); derive the displacement count (yes); turn f_DF into a stored-energy bound with stated conditions (yes, after reading 19.5).

### 19.5 The energy balance law
- Lost points: none. Measuring carrier energies from the electrode Fermi level is a sharp point: once one carrier of a pair has been collected, the d/d mu argument
  shows why no other reference closes the books. The Ramo argument is standard for me.
- Reproduced symbolically: (19.5-calib), the first-order expansion (19.5-first), the exact bound identity (19.5-bound), (19.5-widen) and (19.5-linear) with its determinant.
- Two numerical nits. (i) b = 0.52 gives Y_ph(0) = 1.158, not 1.156 (b = 0.525 gives 1.156); quote b to one more digit. (ii) "errs by at most 2.8e-3 when each of the
  three is below 0.05": I get 2.6e-3 (4 V) and 2.75e-3 (40 V) for values in [0, 0.05], but 6.5e-3 if negative values are allowed (delta_coll can be negative). Say
  "between 0 and 0.05". (iii) An error of 0.005 on Y_40 moves r' by 0.026 in my solve; "0.02" is slightly low.
- Used before defined: "flashing" (after the calibration identity) is never defined in this chapter. 19.4 mentions "infrared neutralization", and I guessed they are the same.
- Pace: 19.5-yield to 19.5-inversion is dense but self-contained; the WE degeneracy is the clearest single page of the section.
- LOs: write the balance law (yes); derive heat quenching and the release law (yes); derive the calibration identity and invert two biases (yes, verified).

### 19.6 Delayed release and the low-energy excess
- Lost points: none blocking. The sum rule proof and the three-state WE check out (4.474 eV in 1.050 hops; 5.539/1.431; 6.994/1.950).
- **Overstatement:** 19.6-lee says "Nuclear recoils store at most 5.5 % ... at 95 % confidence" with no condition. 19.4/19.5 make that bound conditional on r_coll >= 1,
  a branch the book itself says transport estimates do not support. The conclusion survives (the event-seeded term is small anyway), but the conditions should be restated here.
- Not reproducible from the text: the E_PN values 1.2e-4 to 3.6e-7 eV need (C.20-EPN), which is only cited. Their ratio fits exp(-pi^2 d_k/a) with a slowly varying
  prefactor; one line giving the formula would let me check them. S_pol (E.22-Spol) and Delta_r (Ch. 16) are used without being restated.
- LOs: write the master equation and prove the sum rule (yes); estimate the tunneling verdict (yes); derive the defecton T^{-9} law (yes, including the prefactor); bound the LEE by
  energy conservation (yes).

### Field check and tone (b)
- Kinematics, E_R,max, Migdal counting, Bethe/PDG and Landau–Zener are right, apart from the ln I normalization above. Nothing is condescending to a particle physicist;
  the QFT-adjacent steps (Weyl symbol, first-order dielectric stopping, Born parameter) are pitched at the right level.

**Verdict (b): MINOR GAPS.** Nothing blocks what follows. Fix the 174 eV normalization and the forward-loading of 19.4-calib; the rest are nits.

---------------------------------------------------------------------------------------------------
## Persona (c): condensed-matter theorist (DFT, many-body; no dark-matter physics)

### 19.1
- No DM obstacles: the top axis "smallest DM mass" and E_R,max (Eq. 1.3) were introduced in Ch. 1. "Electron-following" is from Ch. 11/12; fine.
- Field check: the classical Wigner propagation is exact for a quadratic H; zero-point leakage under anharmonic collisions is described correctly. The 3<omega>/4 potential
  zero-point per atom (31 meV; 126 eV per 4096-atom cell) is right, and so is the argument for quenching both end states. The harmonic-limit test (mode shares
  |q.e|^2/2NM summing to E_R) is correct. No errors found.
- Pace: the Wigner-function definition and the "phase-space function of H" remark are slightly slow for me, but not condescending.

### 19.2
- Field check: the semilocal gap 0.56 eV vs 1.17 eV and the sign of the crossing error are right. Smooth pseudo-orbitals understate the momentum tail: right, and it is good that the text
  says so. The free-gas "vanishes at E_R,th" slip (see b) is also a CM-side slip.
- DM-side terms: "ionization yield", "quenching factor", "electron-equivalent energy" are defined before use. "Neutron calibration ... tagged at a fixed angle": clear enough.
- Too slow: WE 19-threshold works out k_F and E_F from the density, which is routine for me. It earns its place for persona (a).

### 19.3
- Lindhard/LSS is new to me and was well taught. The criticism of Sarkis et al.'s cross term under approximation (D) is convincing.
- **Error in my field:** Sarkis's U_FP = 23.6 eV is called "the formation energy of a Frenkel pair", while 19.4 and Sec. 7.4 give 6.8–7.5 eV (close) and 8.1–9.7 eV
  (separated). 23.6 eV is not a Frenkel-pair formation energy of silicon; it is close to a displacement-threshold scale. The text should say that this is how the cited
  model names its parameter, and that it exceeds the configurational energy by a factor of about three. Without that, "In the partition U_FP is stored energy" overstates the stored share.

### 19.4
- Field check: KP rules, recombination in metals vs semiconductors, and the stored energy as the difference of minima (not the threshold) are all right.
- DM/detector jargon that blocked me briefly: "CDMS II", "SuperCDMS", "surface events", "210Po sources facing two detectors", "Luke phonons". Luke phonons and
  the detector setup become clear in 19.5, but on a linear read 19.4-calib assumes them (same forward-loading as for b).
- Condition (c) "infrared neutralization of the traps": I did not know this. One clause on what it is ("flashing" with LEDs before data taking) would help, and it would also
  define "flashing" for 19.5.

### 19.5
- Field check: carrier energies counted from mu_F, the electrostatic and image energy in E_pairs, and Delta E_zp kept in the phonons but unabsorbable are all correct and carefully booked.
  The bimolecular and Auger laws (19.5-bimol) integrate as stated. 2 Delta_BCS(Al) = 0.36 meV is right.
- Unknown terms: "pair-breaking energy of the sensor films" and "transition-edge/tungsten sensor" are explained enough in Ch. 1.5 for me to follow. "Athermal sensors" (WE 19-sumrule) is
  not defined here; I could infer it.
- LOs: all reproduced (see b).

### 19.6
- **Error in my field:** in 19.6-defecton the localization criterion is stated as |grad phi| a > Delta_dfn. With phi = V_0 (a/r)^3 this gives 3 V_0 (a/r)^4 > Delta,
  so R_0 = a (3 V_0/Delta)^{1/4}, not a (V_0/Delta)^{1/3}. The quoted R_0 corresponds to the different criterion |phi| > Delta. The crowdion R_0 = 18–43 spacings uses the
  1/3 law; with the stated criterion I get 12–22. Either restate Pushkarov's criterion as he uses it, or change the formula and the numbers.
- Field check: the energy-gap law at T = 0, the Gaussian line shape for strong coupling, the instanton remark, the defecton derivation (backward equation, I_0, the high-T limit
  Delta^2/12<q^2>), the Frenkel–Kontorova kink mass and the discreteness correction are all correct. theta_p = c/2a is about 1/8 of theta_D for one atom per a^3: correct.
- Gap in the LEE argument: bound (19.6-leebound) has two reservoirs, elastic U_rel and event-seeded E_st. Point defects grown in or frozen in at cooldown, which
  19.6-spectrum lists as a family, are in neither. They are probably also small, but the "three consequences without any model" need that term or a sentence excluding it.
  The third consequence ("differ only in U_rel") also assumes that mounting does not change f_ph or stress-assisted defect rates. Say so.
- DM side: the low-energy excess is introduced well enough for an outsider. Exposure, thresholds and "muons and radioactivity" above 85 eV are clear.

### Tone (c)
- No condescension. The many-body content (Huang–Rhys, the Ohmic bath of Ch. 16, the Bloch momentum density) is used at a professional level without re-teaching.

**Verdict (c): MINOR GAPS.** Fix U_FP (19.3) and R_0 (19.6). Neither blocks what follows.

---------------------------------------------------------------------------------------------------
## Prioritized fixes
1. WE 19-lnI: "174 eV" is unit-dependent; drop it or normalize the spectrum properly (b).
2. 19.6-defecton R_0: the stated gradient criterion gives the exponent 1/4; correct the formula or the criterion, and the crowdion 18–43 spacings (c).
3. 19.3-assumptions: U_FP = 23.6 eV is not a Frenkel-pair formation energy (7–10 eV); qualify it (c).
4. 19.4-calib/bounds: forward-loaded on 19.5 (r_coll, delta_coll, f_ion, Luke phonons, eq. 19.4-fDF); reorder, or give (19.5-signal) here (b, c).
5. 19.6-lee: restate the conditions (a)–(d) when quoting the 5.5 %/6.4 % stored-energy bounds; add grown-in defects to the bound or exclude them (b, c).
6. Nits: free-gas fraction vanishes at 336 eV, not 352; 298 vs 2U = 300 eV; b = 0.52 -> 1.158; "below 0.05" -> "between 0 and 0.05"; r' moves by 0.026; 20.1 -> 20.2 eV;
   define "flashing" and "athermal sensor"; t_pr is used in the Fig. 19-recoil caption before it is defined; the two different "1.49 A"; 0.8 vs 0.70 in the bound table.

**Overall: MINOR GAPS** (both personas). I would keep reading; every derived result I attempted could be reproduced, apart from the items above.
