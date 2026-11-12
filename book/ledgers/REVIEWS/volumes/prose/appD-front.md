# Prose round (LLM-ese police): appD and front matter

Unit: tex/appD/ (all 22 section files and appD.tex), tex/front/plan.tex and tex/front/conventions.tex. Base commit 8904b84. Language only. No equation, number, unit, symbol, label, citation key, cited equation number or cross-reference target was changed. The only change inside a display is one punctuation mark (D-23, see the table). No validity condition was removed.

Read in full: every file of the unit. The sentences that the three-volume edit wrote in appD and the front files (logs ch01-02, ch03-05, ch04, ch06, ch07, ch08, E2E-vol1, E2E-vol2, errata/G2, G7) were read first. Then the section openers, and then the body.

## Detector (tools/llmese.py), hits before -> after
| File | Before | After | Remaining hit |
|---|---|---|---|
| D-10 | 1 | 0 | |
| D-12 | 1 | 0 | |
| D-13 | 1 | 1 | self-narration "Here we derive the equations that Sects. 5.1, 6.1 state": kept, because it is a section opener that points inside the book (STYLE allows this) |
| D-14 | 1 | 0 | |
| D-20 | 1 | 0 | |
| D-23 | 1 | 1 | "far from the core": a false positive (the literal distance) |
| D-25 | 1 | 0 | |
| D-26 | 1 | 0 | |
| D-27 | 2 | 1 | "the position of a line relative to the cycle ..., not the values of the momenta": kept, because the next sentence treats coinciding momenta and the contrast is needed |
| conventions.tex | 1 | 1 | "an estimate of where the formula fails, not a bound": kept, because a reader would otherwise take the band edge for a bound |
| other 13 appD files, appD.tex, plan.tex | 0 | 0 | |
| **Total** | **11** | **4** | |

Lint (BANNED-TERMS): 0 blocking hits before and after in every file, and the warning count is the same in every file. A LONG-SENT that my first D-10 edit introduced was split.

chapcheck appD (/tmp/prose-appD): exit 0, 60 pp., 0 undefined references, 0 multiply defined labels, 0 floats too large, 2 overfull hboxes (none of them in an edited line). front/conventions.tex: no reference or macro changed.

## Changes
37 edits in 19 files, touching 38 sentences (5 of them deleted outright). plan.tex: read sentence by sentence and left unchanged. Its four sentences name their content.

Left as it is on purpose: the "Gapless targets" paragraph of D-28 (errata/G7). Its content is to be kept exactly, so I did not touch its two pre-existing tells ("the probe's quasiparticle sits on the filled Fermi sea", "is what the estimate describes"). The lead may want to look at them.

The 15 most important changes:

| file:line | before | after | pattern |
|---|---|---|---|
| front/conventions.tex:10 | "a fuller result for the same quantity, computed in the book from a crystal calculation or from a model that keeps the physics the formula drops, or measured." | "a fuller result for the same quantity: a measurement, or a calculation in the book for the crystal or for a model that keeps the physics the formula drops." | needed a second reading (trailing "or measured") |
| front/conventions.tex:10 | "The sentence under the plot says what breaks down outside the band, and the steps from the book's general result to the formula are derived in the running text next to the box." | "The sentence under the plot says what breaks down outside the band. The running text next to the box derives the formula from the book's general result." | two unrelated clauses; passive nominal |
| D-3:159 | "and the decay does not remember its own past: the probability to decay in the next instant is the same at every time, which is the content of an exponential law." | "and the probability to decay in the next instant is the same at every time, which defines an exponential law." | figurative restatement; colon reveal |
| D-20:44 (written in the edit) | "Dividing Δ_BCS(0) by T_c, the unknown ω_D and the exponential cancel" | "In Δ_BCS(0)/T_c the unknown ω_D and the exponential cancel" | dangling participle |
| D-20:5 | "(Sect. 7.2). What remains is" | "(Sect. 7.2). The mean-field Hamiltonian is" | cleft |
| D-14:69 | "and the Born charge and the masses drop out. What is left is the Fröhlich vertex" | "and the Born charge and the masses drop out, leaving the Fröhlich vertex" | cleft |
| D-25:86 | "What remains is the sum over modes of the harmonic rate" | "The rate is then the sum over modes of the harmonic rate" | cleft |
| D-25:126 | "Neither the target's symmetries nor the form of the coupling entered; only the Hermiticity of the interaction and the Gibbs weights did." | "Only the Hermiticity of the interaction and the Gibbs weights entered, not the target's symmetries or the form of the coupling." | negation framing (positive fact first) |
| D-27:79 | "It is not a Coulomb line but the ionic polarization inserted into the external chain" | "It is the ionic polarization inserted into the external chain" | not-X-but-Y |
| D-27:41 | "they are what separates the electron-channel function ... from ε⁻¹" | "and they make the electron-channel function ... differ from ε⁻¹" | pseudo-cleft |
| D-28:49 | "The cancellation is what makes the result independent of how the nucleus moved before the kick: only the momentum transferred appears." | "The cancellation makes the result independent of how the nucleus moved before the kick; only the momentum transferred appears." | pseudo-cleft; colon reveal |
| D-28:89 | "Its use for the ambiguity is a bound on 1 − z⁻¹" | "The ambiguity estimate needs a bound on 1 − z⁻¹" | nominalization |
| D-16:113, 126 | "Translation invariance trades them for products of first derivatives"; "The rigid-ion approximation closes the gap. It writes the potential" | "expresses them through products of first derivatives"; "The rigid-ion approximation supplies it by writing the potential" | metaphor verbs |
| D-26:88, D-27:73, D-1:33 | "Two hypotheses enter."; "Two cases arise."; "There are three branches." | deleted (the items follow at once, labeled or as "must" sentences) | count-teasers |
| D-23:113 (written in the edit) | "The radii are four and a half and two and a half lattice constants." | "The radius r⊥ is four and a half lattice constants, r∥ two and a half." | reader must pair two lists |

The other edits:
- Metaphor verbs replaced by the plain verb: D-9:19 "collisions pull" -> "relax"; D-12:36 "sit on" -> "lie on"; D-27:3 "sits at" -> "is at"; D-27:7 "stays inside R̃" -> "is included in R̃"; D-8:131 "has moved into a cancellation" -> "now enters as a cancellation"; D-22:21 "The only escape is" -> "The remaining case is"; D-3:172 "plays no role in any rate" -> "affects no rate".
- Clefts replaced by direct statements: D-10:119 "What remains is" -> "The two lines give"; D-13:22 "what is left is" -> "the remaining terms give"; D-26:38 "What remains is" -> "The term is therefore"; D-28:87 "What remains," -> "The rest,"; D-2:107 "The subtraction of the diagonal is what turns" -> "Subtracting the diagonal turns".
- Other cuts: D-12:59 "on its own" and "anyway"; D-13:14 "The diagonal term N₀₀ takes a simple form." (deleted; it was written in the edit and the next sentence gives the form); D-28:87 "so the response calculation does not need Γ^tot, only the cascade does" -> "and only the cascade needs Γ^tot".
- Sentences that needed a second reading: D-22:61 (written in the edit), where the stacked appositive is now in parentheses; D-23:80 "which being nonpolar has" -> "which is nonpolar and has"; D-24:63 "Three cases show every pattern." now names the three operators.
- D-23:101: the display before "Measuring lengths ..." ended with a comma although a capitalized new sentence follows. The display now ends with a full stop. The math is unchanged.

## Sentences written in this round
All of them are in the tables above. Each was reread against the library: no cleft, no negation framing, no metaphor verb, no count-teaser, no colon reveal.
