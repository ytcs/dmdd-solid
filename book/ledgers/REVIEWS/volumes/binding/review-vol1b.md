# Binding review, block vol1b (Chaps. 4-7)

Reviewer: independent, against base 60cc72c. Files: tex/ch04/*.tex, tex/ch05/*.tex, tex/ch06/*.tex, tex/ch07/*.tex.
Method: every changed sentence pair (old/new, with the preceding sentence for antecedents) was read against pattern 27, the register and the calibration; contexts were opened in the files wherever a pointer reached across sentences. Editors' logs were not read before the verdicts.

## Verdict

| Chapter | changed sentences checked | accepted | fixed | reverted |
|---|---|---|---|---|
| Ch. 4 | 213 | 207 | 6 | 0 |
| Ch. 5 | 217 | 213 | 4 | 0 |
| Ch. 6 | 216 | 213 | 3 | 0 |
| Ch. 7 | 194 | 190 | 4 | 0 |
| total | 840 | 823 | 17 | 0 |

("Sentence" = one changed sentence group from a sentence-level diff of each paragraph.) The editing is careful: no lost qualifier or number, no wrong physics apart from one narrowed claim (s4-4:90). The failures are seven splits that left a new sentence opening on a bare pronoun (found by a mechanical pass over all inserted sentence starts), one introduced apposition, four new pointers with the wrong or no antecedent, one coordination garden path, and one misattribution. Where the editors turned a bare "This" into "This + noun" at an existing sentence start, I accepted the change: the noun is named and no new split was made.

The intended symbol unification at s5-6:42 is **correct**. The base called $W_\kappa(\vect{q})$ the Debye-Waller exponent at line 42 but $2W_\kappa(\vect{q})$ at s5-6:3 (base text) and in the worked example "The Debye-Waller exponent of silicon" (which computes $2W_\kappa$). Everywhere else the book also uses $2W_\kappa$: ch08 s8-5:29,68; ch09 s9-1:91, s9-3:14; ch11 s11-7:65; ch12 s12-1:3, s12-4:3,134; ch25 E-4:69; appB B-1:525. Line 42 was the only outlier, and the editor's change removes it. The invariant STOP (`- 1x math:W_\kappa(\vect{q})`) is that change and nothing else. Note for the lead: NOTATION.md row 497 puts "Debye-Waller exponent" in the row of the symbol $W_\kappa$; the row should name $2W_\kappa$ as the exponent so that it matches the book.

## Fixes and reverts

| file:line | editor text | my text | reason |
|---|---|---|---|
| s4-1:136 | Causality, the rule that a response cannot precede its cause, appears in \cref{eq:4.1-kubo} as the step function | Causality means that a response cannot precede its cause. In \cref{eq:4.1-kubo} causality appears as the step function | the edit introduced a defining apposition |
| s4-1:174 | The oscillator response does not depend on temperature because its matrix elements grow up the ladder | ... because the matrix elements of the oscillator grow up the ladder | "its" bound to "response", which has no matrix elements |
| s4-4:90 | The interference between electron and nuclear densities, at energies between the phonon band and the electronic excitations, is treated in \cref{chap:8}. | For a mediator that couples to electrons and nuclei with weights other than those of the total charge, the interference between the electron and nuclear densities is treated in \cref{chap:8}. | the editor read base "between those two cases" (dark-photon coupling and electron-only coupling) as an energy window, which narrows the claim; Sect. 8.3 treats the interference at all energies, the Migdal range included |
| s4-9:129 | ..., \SI{0.36}{eV} below the measured \SI{4.24}{eV}, a downward shift that is the double counting described above. | ...; the \SI{0.36}{eV} by which it falls below the measured \SI{4.24}{eV} is the double counting described above. | "a downward shift" attributed the whole move of the peak to double counting; only the 0.36 eV deficit is |
| s5-1:153 | and a calculation should quote these ratios to the scales of the crystal. | and a calculation should quote ratios to these scales of the crystal. | "quote ... to the scales" parses as quoting to the scales; register |
| s5-6:3 | the phase $\vect{q}\cdot\vect{u}$ that the push imprints | ... that the momentum transfer imprints | the edit deleted "pushes on", leaving "the push" without an antecedent |
| s5-6:88 | from the frequencies and polarization vectors on a fine grid of wavevectors, which Fourier interpolation of the DFPT force constants provides. | from frequencies and polarization vectors that Fourier interpolation of the DFPT force constants provides on a fine grid of wavevectors. | "which" bound first to the grid or the wavevectors |
| s6-2:3 | The screened vertex also describes, at large wavevector, the phonon that lets a slow dark-matter particle cross ... | The phonon that lets a slow dark-matter particle cross the indirect gap of silicon couples through the screened vertex as well, at large wavevector | (OPEN item) the name is right, but "the vertex describes the phonon" misstates its role; the base structure is restored with the name |
| s7-1:82 | At small $k$, expanding $J^{\mathrm{ex}}(\vect{k})$ to second order gives | For the ferromagnet at small $k$, expanding ... gives | the quadratic law follows a sentence on the antiferromagnet, so the reader binds it to the antiferromagnet |
| ch04.tex:3 | ...of excitons. It needs quasiparticle energies and a screened interaction, and the Green's functions | ...of excitons, which needs quasiparticle energies and a screened interaction; the Green's functions | the split left a sentence opening on "It"; merged |
| s4-2:111 | ...adds to $S^0$. It contains cross terms | ...adds to $S^0$; it contains cross terms | the split left a sentence opening on "It" |
| s5-2:185 | ...between 26 and \SI{55}{meV}. It leaves | ..., and it leaves | the split left a sentence opening on "It" |
| s5-6:88 (with the row above) | ...of the zone. They are computed after the phonon calculation, from | ...of the zone, computed after the phonon calculation from | the split left a sentence opening on "They"; restored the base participle |
| s6-1:105 | It also fails where the classical path itself fails | The sudden picture also fails where... | the split left a sentence opening on "It" |
| s6-4:7 | ...propagation of a phonon. It is the bubble | ...; it is the bubble | the split left a sentence opening on "It" |
| s7-1:53 | Removing one unit of spin from site $j$ does not give an eigenstate, ... moves this spin deviation to the neighbors. | A state with a spin deviation at site $j$, one unit of spin removed there, is not an eigenstate, ... moves the deviation to the neighbors. | "this spin deviation" pointed back to a gerund clause |
| s7-1:62 | ...compared with $2\lvert\vect{S}\rvert$. It replaces | ...; it replaces | the split left a sentence opening on "It" |
| s7-4:141 | The stored energy is invisible to a calorimeter that measures the heat and is missing from the measured deposit; | ... that measures the heat, and it is missing from the measured deposit; | coordination garden path: "and is missing" first attaches to the relative clause on the calorimeter |

Open-item and recall fixes (base wording, untouched by the editors):

| file:line | old text | my text | reason |
|---|---|---|---|
| s4-5:168 | 9.4 percent between 16.3 eV and 40 eV and the rest above, lies | ... and the rest above \SI{40}{eV}, lies | OPEN item; anchored without a new number |
| s5-1:134 (caption fig:5-scales) | $-\dd E/\dd u$ from the fit (line) | ... from the sixth-degree fit (line) | OPEN item; the caption has a sixth-degree and a quartic fit; figscripts/ch05/fig5_1.py:78 differentiates the degree-6 fit |
| s6-3:177 | The counting fails in flat bands for the same reason, | The counting fails for the same reason in flat bands, where the Fermi velocity is small, | OPEN item; "the same reason" had two candidates (parallel shells; $v_{\mathrm{F}}Q \lesssim \omega$); the clause states the defining property of a flat band and binds the reason to the second |
| s7-2:31 | both of the same order. | both of the same order as $\lambda_{\mathrm{ep}}$ itself. | OPEN item; "same order" had no term of comparison; eq:7.2-NVren and the numbers below it ($\mu^*_{\mathrm{C}} = 0.12$, $1 + \lambda_{\mathrm{ep}}$, effective coupling halved) show that both corrections enter at the order of $\lambda_{\mathrm{ep}}$ |
| s4-6:116 | The name is the gas analog of the local fields of a crystal: | The name local-field factor comes from the local fields of a crystal: | recall: the sentence equates a name with a physical object |
| s7-1:55 | Holstein and Primakoff turned this into a boson problem | ... turned the problem of spin deviations into a boson problem | recall cross-check: a bare "this" across a paragraph break stood for the whole spin problem |
| s6-5:182 (Summary) | the squared amplitude gives | the squared second-order amplitude $\lvert M^\pm\rvert^2$ gives | recall: "the squared amplitude" has no antecedent in the summary |

## Recall (Job 2)

Sample: unchanged paragraphs of at least 40 words, about one paragraph in eight per file (one in ten of all paragraphs, rounded up), spread evenly through each file. Every section file was sampled, and captions were included where unchanged.

| Chapter | paragraphs sampled (file:line) | words | misses | per 1000 words |
|---|---|---|---|---|
| Ch. 4 | s4-1:7,82,113,166; s4-2:7,114,154; s4-3:3,64,120,182; s4-4:7,64,112,179,221; s4-5:5,68,136,172; s4-6:7,51,116,141; s4-7:7,83,165,231; s4-8:7,52,103,172,200; s4-9:27,83,148,170 | 3370 | 1 (s4-6:116) | 0.3 |
| Ch. 5 | s5-1:12,29,67,149; s5-2:35,113,122,179; s5-3:15,42,104,153; s5-5:27,98,123,147; s5-6:28,92,124,167,197; s5-7:25,85,156,168 | 2161 | 0 | 0.0 |
| Ch. 6 | s6-1:55,70,135,143; s6-2:9,55,103,116,160; s6-3:11,107,117,154,175; s6-4:12,46,82,129; s6-5:15,80,119,143,182 | 1845 | 1 (s6-5:182) | 0.5 |
| Ch. 7 | s7-1:7,21,45,104,108; s7-2:7,38,71,185,197; s7-3:12,54,77,149; s7-4:9,52,92,149,159 | 1336 | 0 | 0.0 |
| total | 105 paragraphs | 8712 | 2 | 0.23 |

Cross-check against the ranker: for each chapter I read 9 flagged sentences in unchanged paragraphs (36 in all, spread evenly over the ranker output, preferring PRON/PROP/REL flags), and found 1 miss (s7-1:55). Recomputed with math, references and macros stripped from the word count (prose words), and with both samples together: Ch. 4 1/2820 = 0.35; Ch. 5 0/1860 = 0.0; Ch. 6 1/1660 = 0.60; Ch. 7 1/1280 = 0.78; total 3/7620 = 0.39 per 1000 prose words.

Borderline, not counted: s5-2:35, "the two choices", picks from the cell vector and the full position, which are named in the two preceding sentences. No chapter exceeds 2 misses per 1000 words, so no chapter needs a second pass on recall. The ranker densities (13.8-25.0 flagged sentences per 1000 words) are uniform across files and point to no hot spot. The paragraph sample was mostly derivation prose, and the samples per chapter are small (1-3k prose words), so these rates are lower bounds rather than precise figures.

## Open items (OPEN.md, this block)

- ch04 s4-5 L168 "the rest above": **fixed** (anchored at 40 eV; the 3.6 percent was not added, since it would be a new number).
- ch05 s5-6:42 STOP (W to 2W): **verified correct**; see Verdict.
- ch05 fig5_1 caption "from the fit": **fixed** (sixth-degree fit, from the figure script).
- ch05 s5-2:50 "both kinds of branch": **stays**. The section opening names exactly two kinds (three branches that start at zero energy and three that start at the optical frequency), and the paragraphs in between introduce no other kind of branch, so the phrase has one referent. The terms "acoustic" and "optical" are defined only by this example (s5-2:58), so they cannot be used here.
- ch07 s7-2:31 "both of the same order": **fixed** (as $\lambda_{\mathrm{ep}}$ itself).
- ch06 s6-3:177 "for the same reason": **fixed**.
- ch06 s6-2:3 "The screened vertex": **name verified** (it is the title of the next subsection and the term used in s6-3:11 and s6-4:32); the sentence was **rewritten** so that the phonon couples through the vertex.

## Proposed errata

None. The one physics change found (s4-4:90, interference narrowed to an energy window) was introduced by the edit and is fixed above. No physics error in the base text turned up in the sentences read.

## Checks after fixes

- `python3 tools/invariant.py 60cc72c tex/ch0{4,5,6,7}/*.tex`: one STOP, tex/ch05/s5-6.tex `- 1x math:W_\kappa(\vect{q})`, the intended unification; no other STOP.
- Lint on the 17 files I touched: 0 blocking, and no hit on any line I edited.
- `tools/chapcheck.sh chNN /tmp/binding-review-vol1b-chNN` for ch04-ch07: exit 0 for each; 0 undefined references and 0 multiply defined labels. Overfull hboxes over 5 pt (3, 4, 0, 3) are at lines I did not edit (s4-4:86, s4-5:153, s4-7:120, s5-1:70, s5-2:34, s5-7:3,59, s7-2:159, s7-4:9,39).
