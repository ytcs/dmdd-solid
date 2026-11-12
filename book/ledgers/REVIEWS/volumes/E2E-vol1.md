
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

## Block ch07, ch08, appD D-20 to D-28
Read in full: openings and Summaries of Chaps. 1-6; ch07 (all), ch08 (all), D-20 ... D-28.
Words: ch07 20400 -> 20399; ch08 39074 -> 39123 (+49, terminology and the one definition of "nuisance parameter"); D-20 ... D-28 15366 -> 15064 (-302). chapcheck: ch07, ch08, appD exit 0, no undefined references, no multiply defined labels, no float too large (the overfull hboxes in s7-4 come from citations that chapcheck leaves undefined). No label of E2E-undefined-labels.txt is cited in the block.

### Changes
- Terminology (Sect. 8.8 keeps "nuisance parameter", now defined once at its first use, s8-8 subsection 1): bare "nuisance" replaced sentence by sentence by "uncertainty", "truncation uncertainty", "normalization/threshold uncertainty", "many-body uncertainty" or "nuisance parameter" (where it is the likelihood parameter). Titles: "The nuisance of a truncation" -> "The uncertainty of a truncation"; "Nuisances in the likelihood" -> "Nuisance parameters in the likelihood"; we:8-lf-nuisance "The local-field nuisance ..." -> "The local-field uncertainty ..."; caption of tab:8-nuisances "Nuisance types" -> "Types of truncation uncertainty". Outside 8.8: ch08.tex map caption ("become theory uncertainties"), s8-3:29 and :180, s8-5:112. Labels unchanged.
- dup s7-2:185 / D-21:32: the $\vect{q} = 0$ bubbles are displayed once, in s7-2, which now carries the label eq:D.21-q0 (moved from D-21; only reference was s7-2, now \cref{app:D.21}). D-21 keeps the trace algebra and the gap-equation step; cut its repeat of the particle-hole-symmetry assumption and of the bare $q = 0$ weight and first moment (eq:7.2-violation).
- dup s8-2:25 / D-25:33: D-25 no longer repeats "the two orders differ by ..."; D-25 also loses the closing sentences of the classical-field subsection (conditions $t \gg t_{\mathrm{coh}}$ and the 1 ns number, stated in s8-2).
- dup s8-3:99 / D-26:42: reviewed, kept: eq:D.26-M3 is the general $s \ne s'$ form that eq:8.3-M3 needs.
- D-20: mean-field error and gap-equation steps shortened to what sec:7.2 does not state. D-22: Lorentz-invariance sentence shortened; last sentence (hard cutoff vs subtraction, stated in s7-3) cut. D-23: valley degeneracy and A1/E/T2 qualitative sentences shortened to pointers (stated in s7-4).
- Symbols (plain typos of \Vol, same derivation): s7-2:175 "$/4V$" -> "$/4\Vol$" (as in D-21); s8-3:39 "$VS_{ab}$" -> "$\Vol S_{ab}$" twice.
- Summary s8-8: in-medium factor "770" -> "$|\varepsilon|^2 = 761$", the value of s8-4.
- Prose: "Note that" cut (s7-1:45, s7-2:76); "of course" cut (s8-5:72).
- Figures: map08.py, fig8_3.py edited and rerun (see notes file).

### Sentences written (not built from existing text)
- s8-8: "In the likelihood the truncation is represented by a \emph{nuisance parameter} $\vartheta_k$, a parameter that is fitted together with the cross-section without being itself the quantity sought. It interpolates between the two responses."
- s8-3:29 "and constrains the theory uncertainties of \cref{sec:8.8}"; s8-3:180 "constrain the uncertainties that \cref{sec:8.8} assigns to truncations"; s8-8 "How much does a theory uncertainty cost a limit?"
- D-21: "With $F(\omega)$ of \cref{sec:7.2}, ... which gives the bubbles \cref{eq:D.21-q0}."
- D-22: "The cutoff breaks the Lorentz invariance of the response, its dependence on $\vect{q}$ and $\omega$ through $q^2$ and $s$ alone, only in these neglected terms."
- D-23: "At the order of \cref{eq:7.4-EMT} the six valley states $F_j\psi_{c\vect{k}_j}$ of silicon are degenerate (\cref{sec:7.4}). They couple ..."; "The $A_1$ state has the largest density at the core, ...; the $E$ and $T_2$ states have nodes there."

### Left for others (details in E2E-vol1-notes.md)
- Later-side duplicates in Vol II: ch10/s10-7:104, ch09/s9-1:71-75, ch11/s11-2:55, ch12/s12-1:84, ch22/s22-2:19.
- Proposal: move Sect. 8.7 to Chap. 18 and the likelihood subsection of Sect. 8.8 to Sect. 21.4.
- Check 761 vs 774 (s8-4:149 arithmetic).

## Block ch05, ch06, appD/D-13, D-14, D-16 (E2E Volume I)

Words before/after: 52020 / 51363 (-657, -1.3 %). Changed files: ch05/s5-3 3994→3986, s5-5 3854→3851, s5-7 4632→4612; ch06/s6-1 3802→3696, s6-3 5192→5156, s6-5 5384→5376; appD/D-13 1385→1140, D-14 506→404, D-16 1351→1222. Other files unchanged.
chapcheck: ch05 exit 0 (50 pp), ch06 exit 0 (45 pp), appD exit 0 (60 pp); no undefined references, no multiply defined labels, no float too large. The 4 overfull hboxes in ch05 and 4 in appD are in lines not touched here. Lint: no hit in a touched sentence (two LONG-SENT hits introduced by my edits were split). No "nuisance" in the block; no cited label from E2E-undefined-labels.txt.

Changes
- D-13: removed the subsection "Clamped-nuclei states" (eq:D.13-expand, the first-order equivalence of the two bases), which repeated s5-1 (eq:5.1-expand and the dressed-states sentence) and s6-1 (derivation of H_ep, screening, equivalence of the two bases). Label eq:D.13-expand removed; its only reference (s5-1) retargeted to eq:6.1-Hep.
- D-14: cut the closing display eq:D.14-frohlich (identical to the keyresult eq:6.2-frohlich) and its commentary on 1/ε∞ − 1/ε0 (stated in s6-2 after the keyresult); the derivation now ends on \cref{eq:6.2-frohlich}. Only reference (s5-5:149) retargeted to eq:6.2-frohlich. Section and labels app:D.14, eq:D.14-gL kept (cited from ch11 and appB).
- D-16: cut the restatement of the expansion and of H_ep/H^(2) (given in s6-3), the first paragraph of "The adiabatic limit" (the steps of s6-3), the closing paragraph on off-site second derivatives (stated in s6-3 after eq:6.3-ria), and the Volume III pointer to app:D.5.
- s6-1: cut the opening pointer to app:D.13 (s5-1 opening already gives it); cut the sentence restating the κ_BO^6 / m_e/M nonadiabatic shift (keyresult of s5-1); cut the restatement of the mixing amplitude and of ω_ph/E_g = 0.055 (s5-1, eq:5.1-mixing and we:5-kappa), keeping the metal / Migdal-theorem content with a pointer to sec:5.1; removed the app:D.13 tag after the Taylor-series sentence (subsection removed).
- s5-1: app:E.8 (Vol III) for the 60 meV zero-point gap shift → sec:6.3; app:D.13 → sec:6.1 for the dressed-states statement.
- s5-3: removed the repeat of the 4^3-grid values 0.050/0.081 Å (given in we:5-kappa); the convergence comparison points there.
- s5-5: fixed "…\label{eq:5.5-LOTO}\end{equation} The difference" (comma then capital) to "and the difference"; eq:D.14-frohlich → eq:6.2-frohlich.
- s5-7: deleted "\Cref{app:E.8} describes the practice." (Addendum 3; the eq:E.8-* pointers that carry formulas stay); Summary sentence on Z*²/ε∞ condensed (it repeated the last sentence of we:5-lst).
- s6-3: Luke phonons pointer app:E.12 (Monte Carlo, Vol III) → sec:20.1 (physics of drifting carriers); deleted the pointer to we:E-zpr after a sentence that states the rule itself; trimmed the paragraph after eq:6.3-smear that restated the Debye–Waller naming convention and probability reading of sec:5.6.
- s6-5: opening pointer for phonon-assisted boson absorption chap:8 → sec:13.8 (where it is worked out); cut a clause in we:6-siedge repeating the exciton-kink statement of the same section.

Sentences written that are not built from existing text: none beyond connective fragments ("These values and those of the $4^3$ grid of \cref{we:5-kappa} differ …"; "a probability that multiplies a rate at the momentum transfer of the scattering"; "What is left is the Fröhlich vertex \cref{eq:6.2-frohlich}"; "so a rate that needs $Z^{*2}/\varepsilon_\infty$ takes $\varepsilon_\infty$ from experiment").

Duplicate list (E2E-vol1-dups.txt): all three pairs of this block have the later side outside it (appA, ch26 ×2); written to the notes file.
Problems left for others: see E2E-vol1-notes.md, block ch05/ch06.
