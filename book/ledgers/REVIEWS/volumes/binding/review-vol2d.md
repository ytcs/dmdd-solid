# Independent review, block vol2d (ch19, ch21, ch22, appE)

Base 60cc72c. Files: all of tex/ch19, tex/ch21, tex/ch22, tex/appE (none is marked generated). I read the sentence-level diff of every changed paragraph against the base, with the surrounding paragraph in the current file wherever a pointer, a name or a claim needed context. I read the editors' logs (ch19.md, ch21-ch22.md, appE.md) only afterwards, to check their stated interpretations.

## Verdict

| chapter | changed sentences checked | accepted | fixed | reverted |
|---|---|---|---|---|
| ch19 | 208 | 204 | 4 | 0 |
| ch21 | 199 | 194 | 5 | 0 |
| ch22 | 45 | 43 | 2 | 0 |
| appE | 305 | 304 | 1 | 0 |
| total | 757 | 745 | 12 | 0 |

"Changed sentences" counts the sentences on the new side of the diff. The editing is good. Most changes name the antecedent or split a heavy sentence correctly, and fidelity holds. I checked these interpretive points and accept them: s19-1:29 (c3 "which carries the force of the neighbors": base "The two omissions" confirms a two-item list); s19-1:71 ("estimates for a criterion of 0.1": every regime criterion in the list below it is 0.1); s19-5:195 (in a replacement the moving atom stops in the site its target emptied); s21-5:3 ("either rate" read as the low-energy event rate and the dark rate); D-38:27 (upper sign near Γ: ε_G = +1 at G = 0); the D-30 block names (singlet, triplet, cross, current block; "current block" was already used at D-30:59 in the base and in ch10).

## Fixes (editor sentences and recall misses)

| file:line | editor / base text | my text | reason |
|---|---|---|---|
| ch22/s22-2:131 | "The other missing step is the renewal analysis…" | "A second missing step is the renewal analysis…" | "the other" had no two-member set; the preceding sentence says "mostly a rate" |
| ch22/s22-3:62 | "The Born parameter $Z_\kappa\alpha/v_F$ of …, set by the electrons that the ion meets, measures the same failure at low speed." | "A second Born parameter, $Z_\kappa\alpha/v_F$ of …, is set by the electrons that the ion meets and measures the same failure at low speed." | left-heavy subject with an apposition; the contrast with the first Born parameter had been lost |
| ch22/s22-3:18 (recall) | "…the ground state of $^{125}$I, 5/2+, cannot be reached from it by an allowed transition" | "…cannot be reached from the $^{125}$Te ground state by an allowed transition" | "it" had two candidates (the two ground states) |
| ch19/s19-5:93 | "One reason a heat measurement alone determines neither the trapped fraction nor the stored energy is that the two can cancel in a single measurement." | "The trapped fraction and the stored energy can cancel in a single measurement, and this cancellation is one reason that a heat measurement alone determines neither quantity." | the reordering made a clausal subject of 14 words |
| ch19/s19-3:108 | "The piece above $q_0$ is therefore …" | "The piece above $q_0$ is …" | the editor added "therefore" right after a sentence that already ends on "therefore" |
| ch19/s19-3:134 (open item) | "…so that the logarithm is large: a proton of 1 MeV has …" | "…so that the logarithm is large. A proton of 1 MeV has …" | split the long base sentence at the colon; each half now parses in one pass |
| ch19/s19-6:29 | "has the exponent 25.2 and needs an exponent 6 % lower" | "has the exponent 25.2 and needs a true exponent at least 6 % lower" | fidelity: the base "needs 6 %" is parallel to "at least 14 % below" in the previous sentence; the edit dropped "at least" |
| ch19/s19-6:152 | "The continuum formulas for the energy and the mass of the kink hold far beyond the range in which the barrier formula holds." | "…are far more accurate than the formula for the barrier." | fidelity: the paragraph compares accuracies at $d_{kink} = a_{ch}$ (1.4 %, 3 %, 22 %), not ranges of validity |
| ch19/s19-6:68 (recall) | "absorbs a fraction $f_{ph}$ of the phonon energy, which depends on where the release happens…" | "…of the phonon energy; $f_{ph}$ depends on where the release happens…" | "which" bound first to "phonon energy" |
| ch19/ch19.tex:9 caption (recall) | "…and Lindhard quenching and Bethe stopping as its limits" | "…as limits of the electronic excitation" | "its" had two candidates (electronic excitation, binary threshold) |
| ch21/s21-2:97 | "exceeds the formula by about the fraction by which…" | "exceeds the formula by the fraction by which…" | the editor added the qualifier "about"; the base said "the corresponding fraction", and the numbers match exactly |
| ch21/s21-2:115 | "the leakage is a normalization uncertainty of its bin, and it enters…" | "…of its bin, with the width set by \cref{eq:21.2-fsleak}, and it enters…" | fidelity: the edit dropped the base's "with that width" |
| ch21/s21-4:12 | "since no events on a background above 2.303 occur in fewer than 10 % of experiments" | "since observing no events on a background above 2.303 happens in fewer than 10 % of experiments" | the edit created a garden path ("no events … occur" reads first as a negation) |
| ch21/s21-4:92 (recall) | "the four move the limit by factors…" | "the four theory uncertainties move the limit…" | the quantifier had no noun in the sentence |
| ch21/s21-4:107 (open item) | "reads the uncertainty budgets of the chapters along the other axis" | "…channel by channel" | "the other axis" was never named |
| ch21/s21-5:29 | "Separate parameters … and so understates" | "… and so understate" | agreement error introduced by the edit |
| ch21/s21-7:3 | "Neither family was among the eleven crystals ranked in \cref{sec:17.6}:" | "Neither family was among those eleven crystals:" | robotic repeat of the full phrase from the previous-but-one sentence; "those eleven crystals" has one antecedent |
| appE/D-36:59 | "…complete the square … pair by pair. With the retarded interaction the square is completed pair by pair; the advanced interaction…" | "…complete the square … pair by pair when the interaction is retarded. The advanced interaction…" | the edit repeated the previous sentence word for word |
| appE/D-38:7 (recall) | "The sites of A lie on that lattice" | "The sites of A are lattice vectors of the sublattice" | "that lattice" could be read as the reciprocal lattice of the preceding sentence |

## Recall (unchanged paragraphs)

I sampled with a fixed stride over the unchanged prose paragraphs of each file (every 6th to 8th, plus a second stride in s19-3, s19-5 and s19-6). In ch22 I read every unchanged paragraph.

| chapter | paragraphs sampled | words | misses | per 1000 words |
|---|---|---|---|---|
| ch19 | ch19.tex:9; s19-1:38, 91; s19-2:30, 102; s19-3:17, 38, 62, 92, 111; s19-5:27, 47, 67, 135, 163, 205, 219, 256, 264; s19-6:27, 68, 97, 125, 139, 189; summary:5 | 2159 | 2 | 0.9 |
| ch21 | ch21.tex:9; s21-1:33; s21-2:15, 58, 101; s21-3:18, 83, 144; s21-4:41, 92; s21-5:34; s21-7:15, 69; summary:13 | 1168 | 1 | 0.9 |
| ch22 | all unchanged: s22-2:8, 13, 19; s22-3:7, 9, 18, 20, 33, 35, 41, 56, 72 | 1413 | 1 | 0.7 |
| appE | D-30:43; D-31:20; D-32:7; D-33:7; D-34:7; D-35:26; D-36:22, 84; D-37:79; D-38:7; D-39:3; D-40:9; D-42:45; D-43:11, 78; D-44:29; D-45:31; D-46:13, 52; D-47:7 | 1069 | 1 | 0.9 |

No chapter is above 2 misses per 1000 words, so none needs a second pass. All misses are fixed (rows marked "recall" above).

## Open items

- **ch19 s19-5:65**, "the two missing energies are equal when both are zero". Stays. As written it is a sufficient condition, and the next sentence ("The truncation therefore holds when …") uses it only that way. Changing it to "only when" would strengthen the claim. It would also contradict s19-5:93, where the trapped fraction and the stored energy can cancel. "both" picks from "the two missing energies" in the same sentence.
- **ch19 s19-3:134**, long base sentence. Fixed: split at the colon (see table).
- **ch21 s21-4**, "along the other axis". Fixed: "channel by channel" (s21-4:107).
- **ch21 names** ("closed form at $v_E^{ref}$", "standard-halo rate/curve"). I checked them: they are used consistently in s21-1 and s21-2.
- **appE D-30 block names**. Checked and accepted (see Verdict).
- **appE D-30:57**, "inversion maps q back to -q". This is a physics slip, not wording. I left it in the text and propose an erratum below.

## Proposed erratum (for the errata review)

- **Location:** tex/appE/D-30.tex:57, paragraph "Inversion with time reversal".
- **Old text:** "Time reversal maps $n_e(\vect{q})$ to $n_e(-\vect{q})$ and $\vect{j}_e(\vect{q})$ to $-\vect{j}_e(-\vect{q})$, since time reversal reverses momenta; inversion maps $\vect{q}$ back to $-\vect{q}$ and reverses $\vect{p}$ again."
- **Proposed new text:** "…since time reversal reverses momenta; inversion maps $-\vect{q}$ back to $\vect{q}$ and reverses $\vect{p}$ again."
- **Reasoning:** after time reversal the argument is $-\vect{q}$. Inversion ($\vect{r} \to -\vect{r}$) maps $n_e(-\vect{q})$ to $n_e(\vect{q})$ and $-\vect{j}_e(-\vect{q})$ to $+\vect{j}_e(\vect{q})$, since the current is a polar vector. That is why the next sentence can say that both rows are even under $\mathsf{PT}$ "at the same $\vect{q}$". The printed mapping goes in the wrong direction. The conclusion is unaffected. The appE editor flagged the same slip (appE.md).

## Checks

- `tools/invariant.py 60cc72c` on all block files: 0 files with a STOP (notes only: repeat counts and added \cref to existing labels).
- Lint on the files I edited: no blocking hits, and none of the LONG-SENT hits comes from my edits (all are in the base: captions, tables, lists).
- `tools/chapcheck.sh` ch19, ch21, ch22, appE into /tmp/binding-review-vol2d: all exit 0, 0 undefined references, 0 multiply defined labels (ch19 reports 2 overfull hboxes > 5 pt; I did not check where they come from).
