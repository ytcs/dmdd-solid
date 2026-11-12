# Independent review, block vol2e: ch18 (Ionization yield)

Brief: briefs/volumes/BINDING-REVIEW.md. Base 60cc72c. Files: tex/ch18/ch18.tex, s18-1 to s18-5, s18-summary (none is marked generated).
Procedure note: my first command printed the editor log (ch18.md) together with the brief, so I saw the editor's log before I reviewed the diff. I then read the whole word diff of every file, sentence by sentence, and the current files, and formed the verdicts below from that reading. I used the log only for the open items and for the editor's stated interpretations.

## Verdict

| file | editor sentences checked | accepted | fixed | reverted |
|---|---|---|---|---|
| ch18.tex | 22 | 21 | 0 | 1 |
| s18-1.tex | 69 | 69 | 0 | 0 |
| s18-2.tex | 35 | 34 | 1 | 0 |
| s18-3.tex | 49 | 48 | 1 | 0 |
| s18-4.tex | 41 | 40 | 1 | 0 |
| s18-5.tex | 51 | 50 | 1 | 0 |
| s18-summary.tex | 12 | 9 | 3 | 0 |
| total | 279 | 271 | 7 | 1 |

My sentence-level comparison of the base with the current files, after my fixes, gives 290 changed sentences: the editor's 279 plus the sentences I changed outside the editor's edits. The editor's work is careful. Fidelity is kept almost everywhere, and the negations the editor restated keep both of their claims (s18-1:35, s18-3:97 "exceeds 0.1 from 4.37 eV on"). I found one fidelity error (Summary:9) and one introduced pointer (s18-4:45).

## Fixes and reverts

| file:line | editor text (or base, if unchanged) | my text | reason |
|---|---|---|---|
| ch18:8 | the joint distribution of the electron and the hole of the pair over bands | the joint distribution of the electron and the hole over bands | revert: *the pair* is used before any pair has been introduced, and the nearest candidate is "each pair of coupling rows" |
| s18-1:106 | Near threshold phonon emission decides the count (base) | Near threshold, phonon emission decides the count | garden path: "threshold phonon emission" reads as a compound noun. Which threshold is meant stays as in the base (open item) |
| s18-2:43 | the constant terms describe the approach to the limits to within 1% | the constant terms describe, to within 1%, the approach to the high-energy limits | "to the limits to within" needs a second parse; the definite *the limits* now names which limits (as in the caption of the limit check) |
| s18-3:3, :14 | the generating function of \cref{sec:18.1} / of \cref{eq:18.1-seed} (base sentences) | generating functional | one name for two objects: the book reserves "function" for the one-variable $\mathfrak{G}_t(x;s)$, which s18-3:14 defines in the next sentence |
| s18-3:97 | so this split can put the energy only on the electron, and its mean | so the one-sided split gives all the energy to the electron, and its mean | open item; see below |
| s18-3:108 | the generating function of \cref{eq:18.1-backward} carries them (base) | generating functional | same object as s18-3:3; the functional has vector components $\mathfrak{m}$ |
| s18-4:45 | Its strongly unequal electron and hole masses and its Γ, L and X conduction valleys make a single parabolic random-$k$ kernel especially crude. | A single parabolic random-$k$ kernel is especially crude for GaAs, with its strongly unequal electron and hole masses and its Γ, L and X conduction valleys. | the editor's "The optical phonons of GaAs …" left *Its* with three candidates (GaAs inside a PP, the constant matrix element, the coupling of silicon) |
| s18-5:7 (2), s18-5:46, Summary:3 | the energy balance \cref{eq:18.1-energy} | the energy identity \cref{eq:18.1-energy} | one name for eq:18.1-energy. s18-1, s18-2 and s18-4:49 say "energy identity", and s18-4:54 uses "Shockley's energy balance" for a different equation. "the deposit is shared by" became "shared according to" |
| Summary:9 | Over its parameters, the calibrated cascade reduces to | The calibrated cascade reduces over its parameter range to | *its* came before its antecedent, and the subject of the previous sentence is the full-band cascade |
| Summary:9 | The seven crystals span the validated range of the calibrated cascade | The crystals with a measured pair energy, silicon included, span the validated range of the calibrated cascade | fidelity: the validated range is spanned by all crystals with a measured pair energy, silicon included (its $w_{\mathrm{AB}} = 0.054$ is the upper edge; Ge has 0.051). Wording now as in s18-4:122 and as in the base ("which defines") |
| tab:18-nuisances | would close the silicon Fano gap | would account for the difference between the cascade and the measured Fano factor of silicon | "gap" means band gap everywhere else; relational noun without its arguments (wording as in the Summary) |
| tab:18-nuisances | threshold at $\frac32\Eg$ gives 0.113 | impact-ionization threshold at $\frac32\Eg$ gives 0.113 | the editor's naming decision for "threshold", applied to the table cell |
| tab:18-nuisances | Direct creation of bound pairs by carriers below threshold | … below the impact-ionization threshold | same |
| tab:18-nuisances | the energy dependence and the carrier--electron exchange act on $F_{\mathrm{eh}}$ | a factor that varies with carrier energy, from the residue and the carrier--electron exchange, acts on $F_{\mathrm{eh}}$ | *the energy dependence* of nothing named; now matches s18-5:125 |

Naming point for the lead: "one-sided seed" (s18-2:30, s18-3:60, tab:18-nuisances "0.35 (one-sided seed)") and "one-sided split" (s18-3:94, :97) name the same fixed split, all the energy to one carrier. 18.3 introduces this split at s18-3:75 without a name. I left both terms, because fixing them needs a naming decision across 18.2, 18.3 and the table.

Considered and left: s18-5:101 "one of the weights $w_k$ is then negative" (the editor's self-fix). Which exponential gets the negative weight depends on whether $\varGamma_{B,j}$ exceeds the decay constant of $X$, so naming the bound-exciton term would be stronger than the text supports. The editor's other three self-fixes (s18-5:125, s18-3:99, s18-1:72) are correct, and I accepted them. In ch18:23 the condition now trails at the end ("… when the error leaves the class weights unchanged"). The scope is slightly wider than in the base, but it reads in one pass, so I accepted it.

## Recall (unchanged paragraphs)

Sampled, whole paragraphs that the editor did not touch (words by `wc -w` on the lines): ch18:14 (30); s18-1:14, 26, 44, 52, 56, 86, 88, 92, 137 (561); s18-2:13, 30, 65, 74, 103 (294); s18-3:49, 52, 64, 77, 108 (320); s18-4:23, 49, 67, 74, 100 (516); s18-5:12, 16, 30, 48, 60, 78, 96 and the 17 rows of tab:18-nuisances, 139–155 (1083). The total is 2804 words (2196 of prose, 608 in table rows): 49 of the 60 unchanged lines over 25 words, table rows included. s18-3 and s18-4 have the highest ranker density (24 per 1000 words), so I sampled them at about 1 in 2. The Summary has no unchanged paragraph; I read all of it under Job 1. I also read tab:18-pairs and tab:18-valid, which hold only numbers and short status cells, and found no miss there.

Misses: 5 (s18-3:108 "generating function"; the four tab:18-nuisances cells above). That is **1.8 per 1000 words** for the chapter, below the threshold of 2, so ch18 needs no second pass. Four of the five misses are in the table, which the editor did not edit. The prose alone has 1 miss in 2196 words (0.5 per 1000 words); the table has 4 in 608 (6.6 per 1000 words).

## Open items

1. **fig:18-tree caption, "(generating function of \cref{sec:18.3})": stays.** The caption's mean and variance are those of the pair number, computed from the one-variable $\mathfrak{G}_t(x;s)$. Sect. 18.3 defines that function (s18-3:14) and its evaluation at roots of unity (s18-3:24). "Function" is therefore the right word, and sec:18.3 is the right target. The general functional is built in 18.1, but the caption does not refer to it. Changing the target is outside the hard limits in any case.
2. **s18-3:97: fixed.** The editor's reading is right. Holes above 12 eV are rejected (caption of fig:18-limit-seed). At 21 eV the excess energy of 19.8 eV no longer fits in the valence band, so the symmetric one-sided split keeps only its electron branch. The editor's "can put the energy only on the electron" was ambiguous in scope ("can only" against "only the energy"), and *this split* was a second name. It now reads "so the one-sided split gives all the energy to the electron".
3. **s18-5:62, "A bound pair is neutral and drifts as a whole": physics; proposed erratum below.** Not edited.
4. **Table prose in tab:18-nuisances: fixed** (four cells, see above). invariant.py, which compares table cells item by item, reports no STOP.
5. **s18-1:106, "Near threshold": comma added.** The referent stays as in the base. At 4 eV the text speaks about a deposit making a second pair, so the threshold meant is probably the onset of the second pair, $(1+\theta_{\mathrm{ii}})\Eg$ (2.32 eV), not $\theta_{\mathrm{ii}}\Eg$. Choosing one would add a claim, so I left the choice to the lead.
6. **ch08 hand-off block in ch18.tex:** I accept the editor's prose edits there. The labels (sec:8.7-needs, fig:8-chain) are unchanged, and chapcheck shows no multiply defined labels.

## Proposed erratum

- **Location:** s18-5:62 (subsection on excitons, charge readout).
- **Old:** "A bound pair is neutral and drifts as a whole, so it induces no charge on the electrodes."
- **New:** "A bound pair is neutral, so a uniform field exerts no net force on it and does not make it drift; it induces no net charge on the electrodes."
- **Reasoning:** a neutral exciton has no drift velocity in a uniform field, since the forces on the electron and the hole cancel. A bound pair that moves as a whole (by diffusion, phonon wind or strain gradients) induces no net charge. "Drifts" says the field carries the exciton toward an electrode, which is wrong, although the conclusion of the sentence (no induced charge) is right.

## Checks

- invariant.py 60cc72c on all seven files: 0 STOP (10 note lines: repeat counts and existing labels, as the editor listed).
- lint: hit counts equal to the base or lower in every file (ch18 3/3, s18-1 7/7, s18-2 5/5, s18-3 6/7, s18-4 8/8, s18-5 11/11, Summary 1/1).
- chapcheck ch18 (output in the scratchpad rev-vol2e/chapcheck): exit 0, 0 undefined references, 0 multiply defined labels, 0 oversized floats. The 2 overfull hboxes are the same as before: both are in s18-4 and in the base (8.1 pt at line 9, 19.6 pt at line 56), and my edit at s18-4:45 does not affect them.
- ranker after review (flagged / per 1000 words): ch18 24 (21.6), s18-1 84 (19.2), s18-2 52 (20.5), s18-3 82 (24.1), s18-4 67 (24.3), s18-5 72 (20.4), Summary 8 (17.2).
