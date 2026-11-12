# Prose round (LLM-ese police): ch21 and appF

Unit: tex/ch21/ (all files), tex/appF/appF.tex, tex/appF/F-rows.tex. Base 8904b84. Language only: no equation, number, unit, symbol, label, citation key or reference target changed (word diff of `git diff 8904b84 -- tex/ch21 tex/appF`: the only `\cref` touched is `\cref{chap:22}`, moved within its sentence). The worked examples recomputed in errata/G4.md are untouched in their numbers.

Read first, in priority order: the sentences written in the three-volume edit (ch21.md "Sentences written", E2E-vol2.md and its sentences-written lists for s21-1, s21-2, s21-4, s21-7 and the Chap. 21 Summary, errata/G4.md items 1-21 with amendments A1-A8); the chapter opening, section openers, Summary, captions, key-result boxes and worked-example introductions; then every file in full.

## Detector (tools/llmese.py), hits before -> after
| File | Before | After |
|---|---|---|
| ch21/ch21.tex | 1 | 1 |
| ch21/s21-1.tex | 0 | 0 |
| ch21/s21-2.tex | 3 | 1 |
| ch21/s21-3.tex | 0 | 0 |
| ch21/s21-4.tex | 5 | 2 |
| ch21/s21-5.tex | 4 | 0 |
| ch21/s21-7.tex | 4 | 2 |
| ch21/s21-summary.tex | 0 | 0 |
| appF/appF.tex | 0 | 0 |
| appF/F-rows.tex | 0 | 0 |
| total | 17 | 6 |

Remaining hits kept on purpose: ch21.tex:2 "a phonon energy ..., not a deposited energy" (the reader would otherwise take the signal for a deposited energy; one clause); s21-2:22 "far from any equilibrium model" (content: the extremal halos are unphysical); s21-4:86 "they move the central value, not the band" (the point of the step); s21-4:92 "Taken one at a time" (literal: each parameter varied alone); s21-7:44 "separate the two pools most clearly" (the leaders differ in both pools there); s21-7:62 "do not move with b, but the sensitivity ... does" (a needed contrast).

## Lint (lint.py with BANNED-TERMS.txt)
0 blocking in every file. Hit counts after = before in every file (ch21 1, s21-1 0, s21-2 7, s21-3 5, s21-4 7, s21-5 2, s21-7 15, summary 1, F-rows 1, appF 0); all are old LONG-SENT or EQ-PUNCT hits in untouched sentences. Two LONG-SENT hits introduced by first drafts of my own wording (s21-2 "with one added term", s21-7 "As a survivor it keeps its lead ...") were shortened away.

## chapcheck
- ch21 (/tmp/prose-ch21): exit 0, 43 pages, 0 undefined references, 0 multiply defined labels, 0 floats too large, 0 overfull hboxes > 5 pt.
- appF (/tmp/prose-appF): exit 0, 2 pages, 0 undefined, 0 multiply defined; 19 overfull hboxes, all from the citation keys that chapcheck leaves unresolved in the table cells (appF was not edited).

## Changes
Sentences changed: 48, of which 4 deleted outright (s21-1 "At the floor the rate is zero.", s21-3 "The model loss function is the idealization.", s21-7 "A ranking needs the inputs of a second candidate.", s21-7 "Two further steps stand between a lead salt and a target.", the last merged into the next sentence). appF.tex and F-rows.tex: read in full, no change needed (index prose and table cells, no tells). s21-summary: read hard, no change (its "floor, never an edge" is the claim of Sect. 21.1).

The 15 most important:
| file:line | before | after | pattern |
|---|---|---|---|
| ch21.tex:4 | "what remains open is indexed in \cref{chap:22}" | "\cref{chap:22} indexes the open problems" | pseudo-cleft |
| s21-1:47 | "A coupling that depends on the dark-matter velocity adds no freedom to this picture." | "... needs no halo function beyond $\eta$." | 0, figurative/negation |
| s21-1:90 | "At the floor the rate is zero. Near $v_{\max}$ the halo supply $\eta$ vanishes ..." | "Near $v_{\max}$ the mean inverse speed $\eta$ vanishes ..." | 26 (repeat of l.86), 25 (periphrasis) |
| s21-2:33 | "for the step ...: all of $\tilde\eta$ sits below the speed $v$, the halo of a single stream at $v$." | "for the step ..., the shape of $\tilde\eta$ for a single stream at $v$." | metaphor verb |
| s21-2:44 | "the minimum over bins is the exact optimum, not an estimate, because" | "the minimum over bins is the exact optimum, because" | X-not-Y (delete) |
| s21-2:108 | "measures the table, not the physics" | "measures the cells of the table" | X-not-Y |
| s21-3:3 | "therefore carry the halo model as much as the target" | "therefore depend on the halo model as much as on the target" | metaphor verb |
| s21-3:131,133 | "Two handles distinguish the target from the halo. The first is a second edge with a different mixture." / "The second handle is time." | "A second edge, with a different dependence on the gap and on $v_{\max}$, distinguishes the target from the halo." / "The annual cycle distinguishes them as well." | count-teaser, 24 |
| s21-4:30 | "it changes the expected counts, it is not the quantity being measured, and the likelihood is profiled over it. The nuisance parameters are removed by profiling ..." | "it changes the expected counts but is not the quantity being measured. The nuisance parameters are removed by profiling ..." | 3 (triad), 26 |
| s21-4:32 | "How much does a theory uncertainty cost a limit? One bin ... shows the structure." | "One bin ... shows how much a theory uncertainty costs a limit." | 8 (rhetorical question), 0 |
| s21-4:37 | "at the price ... that price is below the threshold: the profile then excludes nothing at all." | "at the cost of a term ... that term is below the threshold: the profile then excludes nothing." | "the price of", sentence-final "at all" |
| s21-5:16 | "How much the shape buys depends on where the events fall." | "The gain from the shape depends on where the events fall." | cleft, metaphor verb |
| s21-5:31 | "... are choices, not uncertainties, and they are removed by the recomputation, not profiled." | "... are removed by the recomputation rather than profiled." | double negation framing |
| s21-7:9 | "Membership is a statement about the documented record of a crystal, not about its physics, and ..." | "Membership records what has been documented for a crystal, and ..." | X-not-Y |
| s21-7:62 | "Every figure of merit in the guide is a signal figure: it ranks rates, not the backgrounds against which they are seen. A background enters ..." | "Every figure of merit in the guide ranks signal rates, and a background enters ..." | X-not-Y, colon reveal |

Other changes (same kinds): s21-1:27 "stands alone" -> "All time dependence is now in the kernel"; s21-1:92 "belongs to" -> "depends on"; s21-2:22 "not the optimizer that produced it" -> "whatever optimizer produced it"; s21-2:48 "opens to" -> "grows to"; s21-2:84 "sits at" -> "is at"; s21-2:101 "at a price" -> "with a correction"; s21-3:29, :133 "sits" -> "lies"; s21-3:108 idealization sentence cut, "The halo side is never the limitation" -> "The expansion of the halo tail holds at all these masses"; s21-3:123 "sit in" -> "enter" (twice); s21-4:21 "it is there that" (cleft) -> "the theory uncertainties enter through it"; s21-4:39 "not one per experiment" -> "one common value"; s21-4:41 "calibrated, not known exactly" -> "known from calibrations"; s21-4:50 "not as independent entries" cut; s21-4:71 "charges" -> "gives"; s21-4:73 "sits at small q" -> "comes from small q"; s21-4:101 "What it costs" -> "Its cost"; s21-4:107 "take over" -> "dominate"; s21-5:7 "The price is that" cut; s21-5:16 "sits apart" -> "lies apart"; s21-5:20 "would have charged" -> "would give"; s21-5:29 "pays the constraint" -> "counts the constraint"; s21-5:31 "not as an error of each experiment" cut; s21-5:76 "carries a cost in confidence" -> "lowers the confidence"; s21-7:42 "what the 50 mK fit leaves open is the number, not the order" -> "so the 50 mK fit affects the number and leaves the order unchanged", count-teaser merged ("No lead salt has been operated ..."); s21-7:44 "The softness that wins these rows loses the nuclear edge" -> "The same softness gives CsI a poor nuclear edge", "Once in, its lead must survive its background" -> "Its lead then depends on its background"; s21-7:58 looped closing sentence cut.

Every sentence written here was reread against prose-review patterns 0-26 and the brief's tell list. Scratch: /tmp/claude-0/-home-user-dmdd-solid/d1725f47-7573-51dd-bf4b-00f15cc471f7/scratchpad/ch21-appF/ (detector and lint outputs before and after).
