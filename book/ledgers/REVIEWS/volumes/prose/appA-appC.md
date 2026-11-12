# Prose round (LLM-ese police): appA, appB (appB.tex, B-2.tex), appC

Base commit 8904b84. Files: tex/appA/appA.tex, A-1 … A-9; tex/appB/appB.tex, B-2.tex (generated B-1*.tex and B-3.tex not touched); tex/appC/appC.tex, C-1 … C-20. Language only: no equation, number, symbol, label, citation key or cross-reference target changed; no validity condition removed.

## Priority 1: sentences written during the three-volume edit

From ledgers/REVIEWS/volumes/appA-appC.md ("Sentences written") and ch08.md (second pass, "Sentences written in this pass"); E2E-vol1.md and the errata logs G2, G4 add no new sentences in these files (G2 changes only `V` → `\Vol`).
- appB.tex "…the sign and normalization conventions in which they differ from this book are in \cref{app:A}": plain, kept.
- A-2 (two sentences on eq:A.7-SL and the conductivity forms): plain, kept.
- A-4 "The first-zone part q_r of the momentum transfer labels …": kept.
- C-4 "Folding the negative half line … computed by folding, not by cutting out an interval around the pole" (and the C-4 sentence on eq:2.4-split): kept. The contrast stays because eq:C.4-PV defines the principal value by cutting out an interval, so the reader would otherwise do exactly that; it is one clause.
- C-10 "For the nuclear response,": kept.
- C-12 "Three of its properties are needed:" (count-teaser): cut; the three properties now stand as the sentence. C-12 "for a halo-independent limit the velocities …" (did not parse on first reading): now "which for a halo-independent limit is the set of velocities …".
- C-19 "The ratio of the two is the conversion factor for neutron data.": kept.
- C-20 "…17 % lower at d = 1.23 a_ch, more for narrower kinks (\cref{lim:19.6b}), …": kept.
- C-18 and C-2 sentences from the first pass have since been removed by later passes.

## Detector hits (`tools/llmese.py --files`), before → after

| File | Before | After |
|---|---|---|
| A-3 | 1 | 1 |
| A-8 | 1 | 0 |
| C-1 | 4 | 4 |
| C-2 | 1 | 0 |
| C-3 | 1 | 0 |
| C-4 | 3 | 2 |
| C-9 | 2 | 0 |
| C-10 | 2 | 2 |
| C-11 | 1 | 0 |
| C-12 | 1 | 0 |
| C-14 | 2 | 0 |
| C-16 | 1 | 0 |
| all other files | 0 | 0 |
| **total** | **20** | **9** |

The 9 hits left were read and kept as they are. A-3:74 (kinematics depend on |q|, not |q_r|) and C-1:20 (corrections set by the values of w far from the origin, not by its curvature) correct a wrong assumption the reader would make otherwise. C-4:12 is the folding sentence above. C-1:47 ("does not apply, but the same splitting does"; "not integrable") is a mathematical statement. C-10:43 ("as shown above") is a back-reference inside a proof. C-10:85 ("dominated by its last entry") and C-4:3 ("Here we prove the splitting") are false positives.

The `sits`/`sit` metaphor (11 instances, not all flagged by the detector) was replaced by the plain verb throughout appC. Lint (`lint.py --banned BANNED-TERMS.txt`): 0 blocking in every file. The remaining LONG-SENT warnings (A-1, A-2, B-2, C-1, C-5 … C-8, C-16 … C-18, C-20) are in sentences this round did not touch.

## Sentences changed: 48

The 15 most important changes:

| file:line (per-file, after edit) | before | after | pattern |
|---|---|---|---|
| C-12:3 | "That is a linear program … Three of its properties are needed: any feasible dual solution certifies …" | "… Any feasible dual solution certifies …" | count-teaser (18) |
| C-12:18 | "a nonnegative measure Ξ on a compact set 𝓑, for a halo-independent limit the velocities w with …" | "…, which for a halo-independent limit is the set of velocities w with …" | second reading |
| C-20:73 | "At weak coupling the longer time wins." | "For α_ohm < ½ the time grows faster than the squared amplitude falls." | figurative aphorism |
| C-3:83 | "A crystal is not spherical, but a cubic crystal comes close." | "Cubic symmetry is the closest a crystal comes to spherical symmetry." | not-X-but-Y |
| C-4:74 | "It is the price of the slow 1/x² tails," | "It comes from the slow 1/x² tails," | metaphor (price of) |
| C-4:36 | "\Cref{app:C.5} draws the consequences, the Kramers–Kronig relations." | "\Cref{app:C.5} derives from it the Kramers–Kronig relations." | figurative verb |
| C-9:67 | "Absorption, however, has no static limit at all. … an oscillating, on-shell field, not a static potential." | "… has no static limit. … an oscillating, on-shell field." | "at all."; X-not-Y repeating the previous sentence |
| C-16:11 | "What remains is ∑ 2𝓥ω²\|c\|²." | "The remaining terms sum to ∑ …" | cleft |
| C-19:14 | "…cancels it exactly, and a neutron passing through sees nothing." | "…cancels it exactly, so such a magnetization does not scatter neutrons." | anthropomorphic periphrasis |
| C-10:43 | "We now show that the three points carry a quadrature exact for …" | "The three points carry a quadrature that is exact for …" | self-narration |
| C-10:81 | "Five moments say almost nothing about the median." | "Five moments thus leave the median almost undetermined." | anthropomorphic aphorism |
| C-14:41 | "quantities that are not of interest but are not known exactly:" | "quantities of no direct interest that are known only approximately:" | stacked negation |
| A-3:51 | "The reason for this bookkeeping is that every intensive quantity must …" | "Every intensive quantity must …" | throat-clearing / justification |
| A-8:13 | "that spread belongs to the uncertainty of the halo, not to the definition of the edge." | "that spread is part of the uncertainty of the halo." | X-not-Y (the fixed edge is defined in the sentence before) |
| B-2:3 | "lists the renamings that a reader moving between the book and the papers will meet." | "lists the renamed symbols." | reader-directed phrase |

Other changes: A-3 "sits with the inverse transform" → "is in"; A-8 "absorbed" → "treated"; C-1 "takes for granted" → "uses", "rests on two integrals" → "needs"; C-2 "sit" → "lie", "a set of spikes, not a function of ω" → "a set of spikes" (the next sentence says that they merge into a curve), "carries a resolution" → "has"; C-3 "light dark matter sits in the transition region" → "the momentum transfers of light dark matter lie in …"; C-5 "is all that the following derivations need" → "The derivations below assume only that …"; C-6 ", as it must be" cut; C-10 "rests on" → "uses", "To see this, note that" → "First,", ", which is what we need" cut, "indeed" cut, "sits" → "lies"; C-11 "pulls" → "moves", "not to the other root" → "the smaller root"; C-12 "Where the streams sit follows" → "The positions of the streams follow", "sit" → "lie" (×2); C-13 ", no more" cut, "sits" → "is" (×2); C-14 "tens of events, not a few" → "tens of events", "faithfully" cut; C-17 ", and it can be proved in two lines" cut; C-19 "sits on the ions" → "is localized on the ions", "sit in an open shell" → "occupy"; C-20 "shows the content: each term" → "shows that each term", "wherever its center sits" → "is", "The minimum sits with … and the maximum with …" → "The energy is lowest with … and highest with …", "rest on … as well" → "also assume".

Untouched and read in full: A-1, A-2, A-4 … A-7, A-9, appB.tex, C-7, C-8, C-15, C-18 (no tells beyond idiomatic physics usage such as "the neutron sees", "carries the size dependence").

## Checks
- `tools/chapcheck.sh appA /tmp/prose-appA`: exit 0, 0 undefined references, 0 multiply defined labels, 0 oversized floats, 2 overfull hboxes > 5pt (the same count as in earlier passes; no table or display edited).
- `tools/chapcheck.sh appC /tmp/prose-appC`: exit 0, 0 / 0 / 0, 0 overfull hboxes.
- B-2.tex has no chapcheck unit. Its one change is inside a sentence and touches no LaTeX structure.
