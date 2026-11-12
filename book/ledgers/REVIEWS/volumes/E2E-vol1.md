
## Block ch01, ch02, appD D-1 to D-3

Words before/after: ch01 19363 -> 19315; ch02 22922 -> 22902; D-1/D-2/D-3 3215 -> 3156; total 45500 -> 45373 (-0.3 %). The unit pass had already removed most duplication; cuts here are cross-section repeats and process residue only.

Read in order: ch01.tex, s1-1 ... s1-5, ch02.tex, s2-1 ... s2-5, D-1, D-2, D-3; dup list; undefined-labels list (no label of the list is cited in this block). No "nuisance" in the block (Terminology item: nothing to change).

Changes
- s1-3 (we:1-nuclear): cut "This momentum transfer, 5.1 MeV, is below the inverse nuclear radius ... coherently (\cref{sec:1.4})"; the same fact stands in s1-4 (Scattering on nuclei) next to its explanation.
- s1-3 (after fig:1-eta): cut "Note that inside eta the Earth speed is the actual |v_E(t)|, while reference scalars ... use v_E^ref"; stated in s1-2 below eq:1.2-vmax (and again in appA A-8).
- s1-3 (end of sec:1.3-edge): cut the clause "the escape-speed uncertainty moves it by about 6 %"; the 6.3 % with its derivation is in "Threshold mass" of the same section.
- s1-5 (annual-modulation paragraph of sec:1.5-limit): removed a second "(\cref{sec:1.2})" in consecutive sentences.
- s2-2 (we:2-free): closing sentence cut to "As m_V -> 0 it grows as q_0^4/(m_V^2 q_max^2), the small-angle divergence of \cref{sec:1.4}."; the Rutherford divergence and "sigma_e is a normalization" are stated in sec:1.4 and again at eq:2.2-born.
- s2-5 (free electron gas): "For the four valence electrons per atom of silicon, n_e = 2.00e23 cm^-3 (\cref{app:A.2})" -> "At the valence density of silicon, n_e = ... (\cref{sec:2.3})"; the density is introduced with its motivation in s2-3.
- D-1: cut the numerical-quadrature check sentence (process residue); opening of "Speed distribution" rewritten from "uses one fact that we check here: ..." to "The cut in eq:1.2-Fspeed removes directions only for v > v_esc - v_E, because the galactic speed ...".
- D-3 (line shape): cut the normalization sentence that repeats s2-4 below eq:2.4-lorentz.

Sentences written that are not built from existing text: "As $m_V \to 0$ it grows as ..., the small-angle divergence of \cref{sec:1.4}." (tail only); "At the valence density of silicon, ..." (opening clause); "The cut in \cref{eq:1.2-Fspeed} removes directions only for ..., because the galactic speed ..." (connective). All checked against prose-review patterns; lint clean on changed files (only pre-existing LONG-SENT/EQ-PUNCT warnings in untouched sentences).

Checks: chapcheck ch01 (/tmp/e2e-ch01), ch02 (/tmp/e2e-ch02), appD (/tmp/e2e-appD-0102): exit 0, 0 undefined references, 0 multiply defined labels, 0 floats too large. No label removed.

Volume-level observations (no change made)
- Openings and maps: ch01 opening and ch02 opening connect correctly (ch02 picks up eq:1.5-rate and we:1-flux); fig:2-map caption matches Sects. 2.1-2.5 and lim:2.2a. ch02 Summary closes on chap:4 and chap:3,5, the true dependents.
- Threads closed in block: master rate (eq:1.1-rate -> eq:1.5-rate -> eq:2.5-golden, derived "term by term" in s2-5); kinematic edge (s1-3 -> s1-5 low-mass edge); theory uncertainty (s1-1 -> s1-5 Inputs of a limit -> chap:21 pointer).
- Forward pointers into Vol III are already light: app:E.1/E.3/E.4 (s1-3, computed gap and phonons), app:E.6 (s1-4, dielectric function), app:E.7 (s1-5 and s2-2, form factors, one per chapter), app:E.1 (s2-5, smearing), sec:3.4 (s2-3, Hartree-Fock minimization). Each is the first in its chapter; kept.
- Possible inconsistency left: tab:1-quanta (s1-5) gives the silicon optical phonon "60 meV optical at creation", the text of the same section and fig:1-kinematics give 64 meV (limitbox lim:1.3a uses omega_0 = 60 meV as "a typical silicon phonon energy", which is a model choice). Not plainly a typo; lead to decide whether the table should read 64 meV.
- Cross-block problems: see E2E-vol1-notes.md (A-8, A-9, A-2 restatements of ch01/ch02; ch09/s9-2:96 repeats s1-3:65).

## Block: appA, appC, appB (appB.tex, B-2.tex), appD.tex, front (plan.tex, conventions.tex)

Words (all files of the block): 40721 before, 40621 after (−0.25 %). Appendix A is the convention authority printed in all volumes and was left as it stands apart from one display; Appendix C was cut where it repeated a chapter.

Changes:
- appC/C-4.tex: `eq:C.4-lorentzcorr` (display removed in an earlier pass, two references left, on the undefined-labels list) retargeted to `eq:2.4-split`, which multiplied by Γ_w/2π is the same expansion: "The expansion of \cref{eq:2.4-split} then reads …"; "the linear correction, the finite-part term of \cref{eq:2.4-split}, survives …".
- appA/A-9.tex: display `eq:A.9-dsdq` was referenced nowhere (grep of tex/, only xref). Kept on its merits, since Appendix A is printed in Volumes II and III, where eq:2.2-dsdq is not at hand and the nuclear form in the next sentence needs it; made unnumbered (`equation*`), label dropped, final comma corrected to a full stop. No convention, sign or symbol changed.
- appC/C-2.tex: cut "a zone of volume (2π)³/Ω holds N crystal momenta, one per cell" (repeats s3-1, dup list pair s3-1:126/C-2:30); opening signpost "This section says when each replacement is accurate …" merged into the Poisson-formula sentence.
- appC/C-6.tex: application of `eq:C.6-product` to the crystal displacements (repeats s5-6:61-65, which cites it) cut to a pointer.
- appC/C-13.tex: last sentence ("Tiers never invent an order … reports them together with the probability of ranking first") cut; s17-6:68 says it at the point of use.
- appC/C-14.tex (statistics behind 8.8 and 21.4, where "nuisance parameter" is defined): bare "nuisance" → "nuisance parameter" three times.
- front/conventions.tex: Appendix F "lists each" → "lists the most used of these formulas with their source equations and the sizes of their leading corrections" (lead's request); long sentence split.
- front/plan.tex: Volume I "ends with the master rate formula" → "ends with the master rate formula and the response framework built on it (\cref{chap:8})" (Chap. 8 ends with final states and truncations, not 8.2); app:F "the table of literature formulas" → "an index of literature formulas".

Checked, no change: each C section is cited (grep; list in notes); dup-list pairs with A (s5-3/A-6, s3-2/A-5, s2-2/A-9, s1-2/A-8, s2-3/A-2) are convention restatements that the reference appendix needs; appB.tex, B-2.tex and appD.tex need nothing; no "nuisance" elsewhere in the block; no process residue found.

Sentences written (not assembled from existing text): C-2 "The Poisson summation formula gives the error of both replacements, and also the infinite-crystal form of the lattice sum of \cref{sec:3.1}."; C-6 "\Cref{sec:5.6} builds the multiphonon response from it."; the two retarget phrases in C-4; the two replacement phrases in plan.tex and the one in conventions.tex. All reread against the prose-review patterns.

Checks: chapcheck appA (/tmp/e2e-appA), appC (/tmp/e2e-appC), appD (/tmp/e2e-appD-apps): exit 0, 0 undefined references, 0 multiply defined labels, 0 floats too large (overfull hboxes 2, 1, 5, none in edited text). Lint on the 8 changed files: 0 blocking; one LONG-SENT left in C-6 in an untouched sentence.

Left for others: see E2E-vol1-notes.md (C sections that serve only Vols II/III; s13-9 and s14-4 repeats of C.17 and C.19; italic V for \Vol in A-5 and A-7; app:D.17 in generated B-1).

## Block ch03, ch04, appD D-6 to D-12
Read: openings and Summaries of Chaps. 1-2; every file of tex/ch03, tex/ch04 and appD D-6 to D-12 in order. No "nuisance" in the block; no reference to a label of E2E-undefined-labels.txt.

Words: 69277 before, 68840 after (-437, 0.6 %). Changed: ch03/s3-1 4279->4278, s3-3 5757->5738; ch04/s4-1 4230->4172, s4-2 3915->3863, s4-3 4341->4327, s4-4 5202->5125, s4-5 4673->4640, s4-6 3900->3865; appD D-7 956->935, D-8 1103->1038, D-9 1473->1411. Other files unchanged.

Changes
- s3-3.tex:24: deleted "Detectors run at millikelvin ... the value 1.11 eV of \cref{we:1-mmin} is the one commonly used in projections." we:1-mmin (ch01) now uses 1.17 eV, so the pointer was false; the low-temperature gap is stated in the same paragraph.
- s3-3.tex:224: the closing sentence ("a potential U(r) that is derived rather than fitted") led into the old Sect. 3.4, which is now Chap. 23; added ", the Kohn--Sham potential of \cref{chap:23}".
- s3-1.tex:170: dropped the parenthetical \cref{sec:3.5} (Vol. III); the chapter map caption already points to Chap. 24 for the core region (Addendum 3).
- s4-1.tex:76: cut the paragraph on how R_ee of silicon is computed (KS states, RPA/TDDFT, pointers to sec:3.4 and app:E.6). It interrupted the frequency-dependence thread and repeated s4-2.tex:86 and s4-4.tex:49; s4-2:86 keeps the statement with one Vol. III pointer.
- s4-4.tex:49: cut the paragraph "The dielectric function of silicon is computed from Kohn--Sham states ...": the KS/RPA/kernel route is s4-2:86 and Sect. 4.6, the overestimate of eps_inf by semilocal functionals is s4-6:39 with the number 13.04, the tests against optics and EELS are s4-4:92.
- s4-2.tex:111: dropped the repeated formula (2pi/V)|<n_e(q)>|^2 delta(omega) of the elastic term (given at s4-2:58).
- s4-2.tex:144 and we:4-hydrogen: cut the sentence recalling how Sect. 2.2 identified the gas-of-atoms S (said again two lines below), and the unlabeled display of the hydrogen-gas rate, which is eq:2.2-bound; the sentence now reads "... inserted into eq:2.5-golden it gives n_T times the sigma_T v of one atom, eq:2.2-bound."
- s4-3.tex:168: cut "We want to know over which energies each part of the sum is collected." (announcement).
- s4-5.tex:44: the paragraph on the crystal Lehmann sum duplicated Sect. 4.6; cut to its last fact (the gas tests the codes), with a pointer to Sect. 4.6.
- s4-6.tex:145 (we:4-siepsinf): cut the last sentence, which restated the "about a quarter" spread already given at s4-6:138.
- dup pair s4-5:30 / D-8:60: removed the redisplay of the static Lindhard limit in D-8 (label eq:D.8-static deleted; its only reference, s4-5:30, retargeted to \cref{app:D.8}); D-8 keeps the step and points to eq:4.5-static.
- D-8.tex:56: cut the restatement that eq:D.8-Im is -1/2 times S^0 of we:4-gas via the FDT (said at s4-5:28); kept the remark that the two calculations are independent.
- dup pair s4-5:146 / D-9:90: cut the D-9 redisplay of the Drude function and conductivity and the repeated f-sum discussion (both in s4-5:146-151); D-9 keeps the q->0 step and the large-omega tail step in two sentences.
- D-7.tex:115: cut "A code computes the head and wings analytically ..." (said at s4-6:41).
- dup pair s4-8:7 / D-11:16: read; the chapter states the expansion, D-11 derives it. No cut.

Sentences written that are not built from existing text: ", the Kohn--Sham potential of \cref{chap:23}" (s3-3); "The crystal bubble of \cref{sec:4.6} is computed on a grid of k points, over a finite number of bands and with a broadening in place of i0^+." (s4-5, condensed from the cut sentences); "The many-body definition produces its structure factor directly." (s4-2, from the cut sentence); "\Cref{we:4-gas} found the same forms by counting the transitions with a delta function; here they appear as the jump of a logarithm across its cut." (D-8); "The result is \cref{eq:4.5-static}." (D-8); the two-sentence D-9 replacement. All reread against the prose-review patterns.

Checks: chapcheck ch03 (/tmp/e2e-ch03), ch04 (/tmp/e2e-ch04), appD (/tmp/e2e-appD-0304): exit 0, 0 undefined references, 0 multiply defined labels, 0 floats too large (overfull hboxes 1, 3, 4, none in edited sentences). Lint on the 11 changed files: 0 blocking; remaining hits (EQ-PUNCT, LONG-SENT) are in untouched sentences.

Left for the lead
- Consistency, PBE gap of silicon: ch03/s3-3.tex:29 (fig:3-si-bands caption) and :44 give 0.557 / 0.56 eV for the PBE calculation of app:E.1 at the measured lattice constant; ch04/s4-7.tex:121 and the ch04 Summary (s4-9.tex:166) give 0.602 eV with no lattice constant stated (ch23/s3-4.tex:84 gives "0.56 to 0.60 eV"). Not a typo; suggest s4-7 state the setting of the 0.602 eV or use the 0.557 eV of fig:3-si-bands.
- Volume shape: none found. Sect. 4.7-4.8 (Green's functions, diagrams) serve the BSE of 4.9 and the e-ph self-energy of 6.3; they belong here. D-6, D-10, D-11, D-12 hold derivations the chapter does not give and stay.
- Outside-block dup pairs: see E2E-vol1-notes.md (A-5, C-2, ch23; no action needed).
