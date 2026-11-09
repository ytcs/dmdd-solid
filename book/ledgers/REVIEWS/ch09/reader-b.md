# Chapter 9 mock-reader review: reader b (personas b and c)

Source read: tex/ch09/{ch09,s9-1,s9-2,s9-3,s9-4,s9-summary,tab9-3}.tex (PDF stale). Chapters 1-8 taken as read; cross-references into Ch. 1-8 resolved
(all labels exist; q_0, delta M_kappa, n_B, n_g, theta_ep, x_R, xi_D, the Dyson convention and Fano term are all defined there). Chapters 10-22 not
read. Numbers re-derived with python/scipy: every floor, edge, halo exponent, reach curve, Debye-Waller value, valley-image length and table count was
recomputed. Except where flagged below, they agree to the stated rounding.

Count checks (script over the .tex): atlas has 24 rows, 54 populated cells, 90 empty; populated per column 14/6/8/11/10/5. tab:9-limitchecks has 75
boxes; 27 on a label component (X 12, K 6, n_A 3, M 3, n_D 2, n_T 1), 48 qualifiers (model 29, kinematics 9, long wavelength 5, DM side 5); per
chapter 10:8/15, 11:7/20, 12:7/9, 14:0/8, 16:2/17. All match the prose.

## Persona (b): particle physicist, knows QFT, no solid-state physics

### 9 intro and 9.1 The excitation-interaction matrix
- Lost points
  1. Worked example 9-darkphoton, last paragraph: the tally says the dark photon populates "two of the last" column, but the paragraph before names
     three cells: pairs (10.9), plasmons (17.3) and optical phonons (17.3). Fix: say "three", or explain which one does not count.
  2. Same tally: from the nuclear column it counts only the Migdal row. A heavy dark photon couples to Z n_kappa (stated two paragraphs earlier), and
     at q above the atomic scale the nucleus is unscreened, so dark-photon-mediated free nuclear recoil (11.4) and the nuclear multiphonon cell look
     open. To a particle physicist Z^2-enhanced nuclear recoil through a dark photon is a standard channel. Either count it or say why it is excluded
     (for example, that it is subleading to electron recoil for a light mediator).
  3. 9.1-empty, "Kinematics of absorption": "to absorb the boson it would need m_phi = (m_phi v)^2/2M, which no mass in the halo satisfies." The
     solution m_phi = 2M/v^2 (about 5e7 GeV) is far outside the nonrelativistic regime. The clean statement is exact: a free particle at rest cannot
     absorb a massive boson, since (E_phi+M)^2 - p^2 = M^2 would need m_phi^2 + 2E_phi M = 0. Error in my field (an imprecise argument; the conclusion
     is right).
  4. "Dark Compton scattering" is listed as second order in the dark coupling. In the axion/ALP literature "dark Compton" usually means phi e -> gamma
     e, which is first order in the dark coupling. If the book means phi e -> phi e, say so in the gloss, because the 10.8 pointer alone does not
     settle it.
  5. B-L couplings "reach the lattice through the random couplings of 11.6". I could work out that B-L is random because of isotope disorder (neutron
     number), but the text should say it in five words.
- Steps I could not reproduce: none. The c_nu figure of 10^-8 m_phi, the 116 micro-eV/T line and the dark- photon B' = i p x e A' estimate all
  reproduce.
- Used before defined: the column header "rows of q, Delta_chi" (last column) is opaque until the prose. The sector code "qp" is defined only in the
  caption. Both are acceptable.
- Too slow / too fast: the six-column paragraph is dense but fine for me: the NREFT operator content (O_1, O_4, O_5, O_8, O_11 split into density and
  current parts) is correct. The sector subsection is too fast for a non-solid-state reader: "electron-following sector on the spin manifold" and
  "quasiparticle-number sectors with the caveats of eq:8.6-bin" lean entirely on 8.6.
- Learning outcomes
  * Find the home section of a channel: yes.
  * Say why a cell is empty: yes for operator content and absorption kinematics.
  * List the cells a model fills. Test: an ALP coupling to electron spin fills pairs/excitons 10.7, phonons 11.8, Migdal 12.6, PA 13.8, magnons 14.3,
    chiral 14.5, superconductors 15.4 and the acoustic body 11.8. I can do this.

### 9.2 The kinematic map
- Lost points
  1. The Si plasmon is inconsistent across sections. 9.2 gives a phase velocity of at least 9.54e-3; 9.3 and we:9-open give q_c = 2.60 keV; the fig
     9.2 caption gives "cutoff at 2.24 keV" for omega_pl^2 = omega_p^2 + (3/5) q^2 v_F^2 with omega_p = 16.6 eV. My recomputation with that formula
     and v_F = 6.98e-3 (n = 32/a^3) gives q_c = 2.24 keV and a phase velocity of 9.17e-3 there. The 2.60 keV and 9.54e-3 values instead come from (q
     v_F + q^2/2m)/q at 2.60 keV, which is a different dispersion. Fix: use one model, and say which.
  2. Si 2p edge: "whose opening momentum is 38 keV, at 2 x 38 keV / v_max = 28.7 MeV". The expression is not eq:9.2-mch. It equals the floor 2E_0/v^2
     only if the "opening momentum" is defined as E_0/v_max (100.6 eV / 2.65e-3 = 38.0 keV), which the text never says. As written, it reads as if a
     new formula had appeared.
  3. Halo paragraph: "When E_ch rises at q-bar, the minimum moves to ... the exponent exceeds 2." This is true only at a stationary minimum (E = q(v +
     E')/2 > qv/2). The gapless linear branch also rises but sits on a constraint, and gives -1.012. Add "at a stationary minimum".
  4. "Two entries of the atlas are closed this way" (Si plasmon, narrow-gap III-V pairs), yet both atlas cells are populated (10.3, 16.1). Say "closed
     in these materials" or "closed to elastic scattering".
  5. The intro to 9.2 says a free Si nucleus takes up the gap from "about 45 MeV". 9.3 says 46.7 MeV, and I get 46.7 as well. Use one number.
  6. "Onset of free recoil" uses three criteria in one chapter: four mean phonon energies (9.2, 17.5 MeV), nine phonon energies (9.4 opening,
     lim:1.3a) and x_R >= 2.3 (we:9-place). we:9-place reconciles 9 with 2.3; the "four" needs a clause of its own.
- Steps reproduced: eq:9.2-mch and its floor bound; gapless and gapped branches (ZrTe5 7.1/9.66/8.04 keV, exponents -2.12/-2.76/-2.36; the text has
  9.6 and -2.74, which I put down to rounding of v_D/v_max = 0.42); offset bounds 0.474/0.420 MeV; quadratic branch 17.46 MeV; eq:9.2-halo; the shifts
  of 6.3/3.2/7.4 per cent and the exact -6.0/+6.6 per cent. The annual floor shifts come out as -3.8/+3.5 per cent from 781/810 km/s, against the
  text's -3.9/+3.4, presumably from unrounded endpoints. I could not check this without 1.2.
- Too slow / too fast: we:9-acoustic is well paced. "Offset minimum" is too fast. It strings eight edge values from 13.1/13.9 in one paragraph, and a
  reader without band-structure intuition cannot tell why GaAs, a direct-gap crystal, still has a phonon-assisted band.
- Learning outcomes: compute the lightest mass for a given dispersion (yes: Ge acoustic 10.19 keV, Al 8.60 keV, Si transverse 9.76 keV reproduced);
  explain why a linear branch is v/4c above the floor (yes, from the backscattering argument); give the halo scaling of an edge (yes).

### 9.3 Excitations on the momentum-energy plane
- Lost points
  1. The direct gap of Si: 9.1 and 9.2 say the direct gap is 3.4 eV, but 9.3 gives E_min(q -> 0) = 3.17 eV from PBE bands with a scissor shift. A
     reader sees two "direct gaps". One clause would fix it (PBE plus scissor underestimates Gamma-Gamma).
  2. Table 9-overlaps, row 4: "zero for every one-body self-energy, by inversion with time reversal and an even electron number". I accept it on trust
     but cannot see the argument. A pointer to the equation in 8.6 would help.
- Steps reproduced: the 2W values; the 247 keV crossing and 46.7 MeV; the valley-image lengths (1.94, 2.63, 3.25, 4.96, 5.27, 5.32 keV); the 0.11 eV
  half-gap cost; the reach of 0.3/1/10 MeV (1.05 eV at 0.80 keV; 0.49-4.81 keV; 53 keV, 35 eV); we:9-open (1.11 MeV, 195 km/s, 32 phonons, the 2e-8
  Migdal estimate, the margin windows 2.29/1.72-2.02/2.01 eV); 5.47e-4 = (1 + 14 m_e/M)^2 - 1; 196 + 196.
- Too fast: the paragraph on the zero-phonon sector, with its direction dependence and Umklapp images. I needed the script to believe it.
- Learning outcome: decide which sectors serve a point (q, omega) in Si. Mostly yes, but it needs direction-resolved E_min values that the book gives
  only at the few points quoted.

### 9.4 Limit Checks and the truncation label
- Lost points
  1. The opening says the channel chapters "give 75 of them [the 90 formulas] a box". 9.4-appF says "Eighty belong to the 75 Limit Checks". Fix the
     opening: "80 of them appear in 75 boxes".
  2. we:9-place, loss-function rate: "in a model of the acoustic peak at 1 MeV" is ambiguous: a dark-matter mass of 1 MeV, or an energy? It reads as
     an energy until context resolves it.
  3. Table 9-3 lists lim:11.4a as "K: impulse -> multiphonon", while the prose calls its leading correction "the next term of the impulse expansion".
     On the lattice-regime axis this "step" goes back toward fewer phonon numbers. State the direction convention for K.
- Steps reproduced: all counts (see top). x_R = 2.3 at 70 keV, and x_R = 1 at 46 keV, with <omega> = 40.9 meV.
- Too slow: the anatomy of a box (9.4-plot) explains a format at length. Too fast: the "four kinds" of qualifier are named without an example of each.
- Learning outcome: place a formula on T and name its controlling parameter. Partly. I can read off the answer for the three examples, but for
  Lindhard (omega/E_g as the controlling parameter) I would not have predicted the axis without the table.

### Verdict (b): MINOR GAPS
I would keep reading. Nothing blocks the channel chapters, and the kinematic section is the best physics explanation in the chapter for me. The dark-
photon tally and the plasmon numbers need fixing before release.

## Persona (c): condensed-matter theorist (DFT, many-body), no dark-matter physics

### 9 intro and 9.1
- Lost points
  1. The NREFT operator list (O_1 ... O_15, c_1^(e) = V-tilde) assumes 8.1 has fully landed. For me the column definitions are the hardest part of the
     chapter. A one-line physical gloss per column ("couples to where electrons are / where nuclei are / to spins and currents") would anchor it, and
     the column headers almost do this.
  2. The sector of "Precessing nuclear spins": ad. Electrons stay in the ground state and nuclei carry the energy, so it fits the definition, but it
     is not a lattice state. A word would help.
  3. "c_nu between 2e-5 and 3e-5 in silicon": LA [111] is 9.35 km/s = 3.12e-5. Say "up to 3.1e-5".
- Field check (no errors found): electron density commuting with total S, so no magnon without SOC: correct. Triplet pairs carry no charge, so no
  plasmon in the spin column: correct. Kohn-type argument for a clean metal (j(0) = P/m conserved by e-e scattering): correct, given the stated free-
  electron description. Z*_Si = 0: correct. The f-sum constraining the four electronic cells together: correct. The drag-mass and Born-charge
  statements are consistent with 5.5 and 8.6. No condescension. If anything the solid-state terms are used briskly, not over-explained.
- Learning outcomes: as for (b), yes.

### 9.2
- Lost points
  1. The "floor" 2 omega_th/v_max^2 and v_max = v_esc + v_E^ref come from Ch. 1. Fine for me, but the reason a light particle must backscatter to make
     an acoustic phonon (we:9-acoustic) is the key insight for a CM reader. It is stated well; keep it.
  2. NiO: the magnon is treated as gapless and linear (c_M = 1.36e-4, edge 7.3 keV at 5 meV). Two paragraphs later, and in tab:9-supports, a zone-
     center magnon sits at 4.54 meV, just below that threshold. As a CM reader I know NiO has two branches with very different gaps. The text should
     say that the edge uses the lower, nearly gapless branch; otherwise a 4.54 meV gap next to a 5 meV threshold looks inconsistent.
  3. ZrTe5 parameter rows (11.8 meV measured structure against 15.6 meV relaxed cell in we:7-zrte5): the switch is flagged, which is good, but two
     Delta_D values within one sentence slow the reading.
  4. Superconductor "on the floor because v_F q >= omega": correct as a statement of reach. The coherence factors that suppress the density response
     at 2 Delta are not mentioned. The closing paragraph ("the map ranks reach, not rate") covers this.
- Field check: Si/Ge/GaAs gaps, Ge 3d binding, Ge direct gap 0.89 eV, exciton 14.7 meV, TA-assisted onset 1.1728 eV, LO of GaAs 36.35 meV, Si optical
  64.1 meV, diamond 3.1 keV: all consistent with standard values. No errors in my field.
- Learning outcome: rank targets by reach at a common threshold. Yes.

### 9.3
- Lost points
  1. The plasmon cutoff, 2.24 keV in the caption against 2.60 keV in the text (see b, 9.2.1). For a CM reader this is a visible inconsistency: the
     stated RPA small-q dispersion with the 3/5 coefficient gives 2.24 keV.
  2. The Si direct gap of 3.17 eV against 3.4 eV (see b, 9.3.1). The measured Gamma'25-Gamma15 is about 3.35-3.4 eV; PBE plus a rigid scissor shift
     fitted to the indirect gap lands lower. State it.
  3. The Fano row, "inversion with time reversal and an even electron number": as a many-body theorist I want to know whether this is Kramers
     degeneracy making the coefficients real, so that they cancel pairwise, or a parity selection rule. One sentence would do.
  4. Table 9-supports, two-magnon continuum "from the one-magnon energy": the lower edge at small q is about epsilon_q + epsilon_0, so roughly the
     one-magnon energy plus a gap. Acceptable as a gloss.
- Field check: <u_x^2> = 2.45e-3 A^2 at T = 0 (B of about 0.19 A^2), PBE X-point phonons 17/51 meV, Landau damping of the plasmon at entry into the
  continuum, the 3/5 RPA coefficient, valley images k_c + G: all correct. The "overlap is not interference" argument (orthogonal phonon-number states;
  cross terms only for two-species couplings or at the sector boundary) is the clearest statement in the chapter. No condescension.
- Learning outcome: identify where double counting or a dropped cross term can occur. Yes. Region 1 (the cancellation of 14 - 14 charge) is a vivid
  example.

### 9.4
- Lost points
  1. The 75 against 80 count (see b, 9.4.1).
  2. "Twelve are on the many-body axis": the table uses "RPA + LF", "conserving" and "BSE, one time ordering -> both". These are fine for me, but
     "conserving" (a Baym-Kadanoff conserving approximation for the BCS bubble?) should be glossed for persona (a).
  3. The Lewin-Smith/Helm rate placed at K = impulse, n_B = 0: fine. "The mean deposit E_R is exact at every anharmonic and thermal order, since it is
     fixed by the sum rule": correct (f-sum for the nucleus).
- Field check: the IP -> RPA -> RPA+LF screening hierarchy, screening strongest at small q, and the loss- function identity being exact for total-
  charge coupling: all correct.
- Learning outcome: from a formula's assumptions, name the next step and what it costs. Yes for the electronic examples. For the magnetic and glass
  boxes I take the table on trust.

### Verdict (c): MINOR GAPS
Clear and well argued from a CM point of view, with no errors in condensed-matter physics beyond the inconsistencies flagged (plasmon cutoff, Si
direct gap, NiO branch). The dark-matter side (columns, floor, halo) is understandable from Ch. 1 and 8 alone.

## Priority fixes (both personas)
1. Plasmon cutoff and phase velocity: 2.24 keV and 9.17e-3 against 2.60 keV and 9.54e-3 (9.2, 9.3, fig 9.2 caption).
2. Dark-photon tally: "two of the last" against three named cells; nuclear-recoil cells not counted.
3. 9.4 opening, "give 75 of them a box", against "eighty belong to the 75 Limit Checks".
4. Si 2p "opening momentum" formula; "about 45 MeV" against 46.7 MeV; Si direct gap 3.17 against 3.4 eV.
5. Free-nucleus absorption argument; "exponent exceeds 2" holds only at a stationary minimum; "closed" entries that the atlas shows as populated.
6. Minor glosses: the B-L random coupling, "dark Compton", the NiO branch, the Fano parity argument.

Overall verdict: MINOR GAPS.
