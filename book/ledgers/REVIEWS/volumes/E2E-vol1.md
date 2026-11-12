
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
