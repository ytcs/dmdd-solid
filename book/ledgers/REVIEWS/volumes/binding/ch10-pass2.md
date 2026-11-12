# Binding round, second pass: ch10 (Electronic excitations)

Editor: second sentence-construction pass (BINDING.md, prose-review pattern 27). It follows the independent review (review-vol2a.md), which found 2.9 misses per 1000 words in the unchanged text of Ch. 10, mostly heavy or clausal subjects before the main verb. Base commit for invariant.py: 60cc72c. Files: tex/ch10/ch10.tex and s10-1.tex to s10-10.tex.

I read every paragraph of all eleven files again, whole: body text, section openings, key-result and Limit Check boxes, worked examples, figure and table captions, open problems and the Summary. Before reading, I made a hit list with a regex pass over every sentence, flagging those that open on a gerund, those that open on *Whether / What / How / Which / That / Where*, and those with a relative pronoun among the first ten tokens. I also marked which sentences were still verbatim from 60cc72c, and read those hardest. Line numbers are paragraph lines in the edited files.

I left the reviewer's fixes as they are: s10-3:24/26, s10-4:7/58/105, s10-5:55/70/93/125, s10-6:63/131, s10-7:15/63/73/82, s10-8:7/37/62, s10-9:7/114/127, s10-1:30 and s10-2:17/113. Short gerund subjects such as "Dividing the power by … gives" are the reviewer's own repairs, and I kept them. So are the accepted single-candidate pronouns, for example the parallel "It has no screening / It has no lattice" list in s10-1.

## Per file

"Edits" counts the replaced passages. "Sentences changed" counts the sentences of the edited file that do not occur verbatim in the file before this pass, so a sentence split in two counts twice.

| file | ranker before (flagged / per 1000 w) | ranker after | edits | sentences changed |
|---|---|---|---|---|
| ch10.tex | 8 (22.8) | 8 (22.9) | 2 | 2 |
| s10-1.tex | 54 (23.4) | 50 (21.6) | 7 | 7 |
| s10-2.tex | 93 (21.2) | 88 (19.9) | 18 | 22 |
| s10-3.tex | 38 (20.8) | 35 (19.1) | 7 | 7 |
| s10-4.tex | 63 (22.3) | 58 (20.5) | 10 | 10 |
| s10-5.tex | 88 (20.0) | 89 (20.2) | 15 | 17 |
| s10-6.tex | 74 (19.8) | 74 (19.7) | 17 | 20 |
| s10-7.tex | 93 (21.1) | 90 (20.4) | 13 | 15 |
| s10-8.tex | 71 (20.0) | 68 (19.1) | 13 | 14 |
| s10-9.tex | 84 (20.1) | 80 (19.1) | 14 | 15 |
| s10-10.tex | 47 (21.5) | 44 (20.0) | 11 | 14 |
| total | 713 | 684 | 127 | 143 |

The ranker counts move little. Most repairs move a heavy subject behind its verb or turn it into an adverbial or a conditional clause, and the ranker still counts the resulting sentence for length or for a remaining single-candidate pronoun. s10-5 rises by one because two sentences were split.

Kinds of repair, roughly by frequency:
- Heavy subjects with a relative or reduced relative before the verb (about 45). These became a fronted adverbial ("In silicon, a dark-matter particle …"), a conditional ("If a particle deposits …, it …"), a participle opener whose subject is the agent ("Absorbed in silicon, a dark photon …"), or a sentence with the heavy material after the verb.
- Appositive and equation-appositive subjects (about 20). Examples: "The first moment of the line, $…$, is"; "The largest, the spin–orbit structure …, is"; "Three events in a kilogram-year, the background-free reach, need"; "The radiative part, a photon … that …, lies".
- Clausal subjects (*Whether / Which …*) (6): s10-1:3, s10-2:51, s10-5:3, s10-5:66, s10-5:93, s10-9:116.
- Heavy gerund subjects of eight or more words (6): s10-4:109, s10-5:3, s10-6:77, s10-8:24, s10-9:78, s10-10:74.
- Long coordinated subjects (6). Examples: the Summary's "Continuity, spin rotation and …", the two "calculation" sentences of the s10-10 open problems, and "The crystal form factor … and the independent-particle head …".
- Binding (about 15): *the one / the … one* (s10-2:19/53/58, s10-5:22, s10-7:63, s10-8:128, s10-10:9); *it* with several candidates (s10-2:51, s10-3:3); *Its* (s10-3:69); *which* attaching to two heads (s10-7:3); *which* for a proposition (s10-4:13); *both* without a coordinated set (s10-2:95, s10-4:95, s10-4:116, s10-8:95); *Those* (s10-7:119).
- Garden paths and attachment (5): ch10.tex:2 ("the signal most searches for …"), s10-6:79 ("attract each other and the valence electrons"; "A semicore shell kept in the valence hybridizes"), s10-5:45 ("a finite step, where independent pairs start"), s10-7:128 (dangling "Compared to the $f$-sum rule").

## Fifteen instructive changes

| file:line | before | after | failure fixed |
|---|---|---|---|
| ch10.tex:2 | An electron--hole pair is the signal most searches for sub-GeV dark matter look for. | Most searches for sub-GeV dark matter look for an electron--hole pair. | garden path: "the signal most searches for …" reads *searches* as the verb |
| s10-1:3 | Whether it leaves an electron--hole pair behind depends, for each pair $(\vect{q},\omega)$, on how strongly … | Its chance of leaving an electron--hole pair behind depends, for each pair …, on how strongly … | clausal subject; the graded "depends on how strongly" is kept |
| s10-2:49 | and the head screening, the ratio of the independent-particle rate to the random-phase rate without local fields at that momentum, is 1.18 | We call the ratio of the independent-particle rate to the random-phase rate without local fields, at a given momentum transfer, the head screening; at \SI{8}{keV} the head screening is 1.18 | defining apposition inside a 20-word subject |
| s10-2:51 | Whether the moved weight is lost depends on the largest energy … At \SI{1}{MeV} it is \SI{3.5}{eV} | The moved weight counts only if it lies below the largest energy … At \SI{1}{MeV} the largest energy is \SI{3.5}{eV} | clausal subject; *it* with three singular candidates (weight, mean energy, largest energy) |
| s10-2:115 | the bound \cref{eq:10.2-bound} with $n = -1$, and with every $n < 1$ through the power $(1 - n)/2$, fails for an electron-only coupling once the lattice relaxes | Once the lattice relaxes, the bound … with $n = -1$ fails for an electron-only coupling, and through the power $(1 - n)/2$ so does the bound with every $n < 1$ | subject split from its verb by a parenthetical coordination |
| s10-3:16 | The factor $Z_L$ is the residue of the longitudinal photon propagator at the plasmon pole that Kozaczuk and Lin use for … | Kozaczuk and Lin use the factor $Z_L$ for the plasmon's polarization vector, as the residue of the longitudinal photon propagator at the plasmon pole | *that* could attach to the pole or to the residue |
| s10-4:95 | Both edges need the density and current rows to be proportional | Each edge needs the density and current rows to be proportional | *both* picking from "the edges of the band" in the previous sentence |
| s10-5:93 | Which kernel remains in the coupling block depends on how the long-range part is handled. | The treatment of the long-range part decides which kernel remains in the coupling block. | clausal subject with a second clause after the verb |
| s10-6:79 | The excited electron and the hole left in the $3d$ shell attract each other and the valence electrons relax around the hole. … A semicore shell kept in the valence hybridizes … | … attract each other, and the valence electrons relax around the hole. … A semicore shell that is kept in the valence hybridizes … | coordination garden path ("attract … the valence electrons"); reduced relative read as the main verb |
| s10-7:3 | The axion-like particle couples to the spin current of the electrons, which without spin--orbit coupling has the response of the current itself but no mixing | … couples to the spin current of the electrons. Without spin--orbit coupling the spin current has the response of the current itself but no mixing | *which* with two heads (electrons, spin current); a relative clause with an interposed adverbial |
| s10-7:128 | Compared to the $f$-sum rule \cref{eq:4.3-fsum}, which has …, the squared momentum kick $q^2$ is replaced by the mean squared force on an electron. | In \cref{eq:10.7-sumrule} the mean squared force on an electron replaces the squared momentum kick $q^2$ of the $f$-sum rule \cref{eq:4.3-fsum}, which has … | dangling comparative opener; passive with the agent last |
| s10-8:60 | The squared amplitude of Bauer and collaborators for the spin flip, $G_{\mathrm{A}}^2$ times the square of the relative velocity transverse to the field over four, is the integrand of … | Bauer and collaborators give the squared amplitude of the spin flip as $G_{\mathrm{A}}^2$ times …. This squared amplitude is the integrand of … | 25-word subject holding a defining apposition |
| s10-9:157 | An excited state $\chi_2$ that survives from the early universe, or that a scattering in the Earth produces, can decay … A transition magnetic moment $\mu_{\mathrm{M}}$ between the two states, $H = …$ with $\boldsymbol{\sigma}$ …, gives the vacuum rate | An excited state $\chi_2$ may survive from the early universe or be produced by a scattering in the Earth, and it can then decay … Let the two states have a transition magnetic moment $\mu_{\mathrm{M}}$, with the interaction $H = …$ and $\boldsymbol{\sigma}$ …. The vacuum rate is | two relatives in one subject; equation apposition in the next subject |
| s10-10:83 | A second-order electron--phonon calculation at the plasma frequency, and shell Compton profiles, settle the plasmon branching and the bound-shell correction to dark Compton scattering | A second-order electron--phonon calculation at the plasma frequency settles the plasmon branching, and shell Compton profiles settle the bound-shell correction to dark Compton scattering | coordination scope: which input settles which item. The pairing is the one implied by the cited sections (10.3 for the branching, 10.8 for the shells) |
| s10-10:89 | Continuity, spin rotation and the product of inversion and time reversal reduce the spin and current responses to twelve real functions … | Three constraints reduce the spin and current responses to twelve real functions … (\cref{sec:10.4}): continuity, spin rotation and the product of inversion and time reversal. | 11-word coordinated subject, repaired as the reviewer did at s10-4:7 |

## Judgment calls the lead may want to check

- s10-1:3: "Whether it leaves an electron--hole pair behind depends …" now reads "Its chance of leaving … depends …". The dependence stays graded ("how strongly"), and the sentence makes no new claim.
- s10-2:51: "Whether the moved weight is lost depends on the largest energy …" now reads "The moved weight counts only if it lies below the largest energy …". This is the same condition. The next sentences, unchanged, give the two cases (35 eV and 3.5 eV).
- s10-7:145: "the margin by which \cref{eq:10.7-scalar} holds is therefore open, and it is fixed by …" now reads "the accuracy of \cref{eq:10.7-scalar} is therefore open, and the same all-electron calculation …, fixes it".
- s10-10:83: the coordinated "calculation …, and shell Compton profiles, settle X and Y" is now split into two paired clauses (table above).
- s10-4:9: "the current along $\vect{q}$, $j_{\mathrm{L}} = …$" now reads "the longitudinal current $j_{\mathrm{L}} = …$". The term already names $j_{\mathrm{L}}$ in s10-4:41 and in Tab. 10-minimal.
- s10-2:49: "the head screening" is now defined once, by "We call …". The sentence keeps the reference to a given momentum transfer, and the later uses (s10-2:53, s10-4:54, s10-10:9) refer to the same ratio.

## Checks

- invariant.py 60cc72c on all 11 files, after the last edit: 0 STOP, exit 0. Only `note` lines: repeat counts of existing items and `\cref`s to existing labels. I made no intended symbol unification. No equation, number, label, citation key or cross-reference target was changed. Sentences were reordered only inside a paragraph.
- Lint (BANNED-TERMS), diffed per file against the lint output of the pre-pass copies: no new hit. My edits introduced three LONG-SENT hits along the way (s10-5 Wannier sentence, s10-6 semicore and xenon sentences, s10-9 massless-mediator sentence), and I split each of them. One pre-existing LONG-SENT is gone, in the s10-10 open problems. The s10-3 LONG-SENT is the pre-existing hit across the display before the $Z_L$ sentence, with changed wording.
- chapcheck ch10 (output in the session scratchpad): exit 0, 0 undefined references, 0 multiply defined labels, 0 oversized floats, 0 overfull hboxes over 5pt.
- No git command except diff, show and log. All scratch files are outside the repository.
