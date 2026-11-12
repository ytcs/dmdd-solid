# Prose round (LLM-ese police): Volume II, tex/appE/ (appE.tex, D-30 to D-47)

Base commit 8904b84. Language only; no equation, number, symbol, label, citation or reference target changed.

Words (`cat tex/appE/*.tex | wc -w`): 22436 -> 22426. Every file read in full. The Addendum-4 sentences (E2E-vol2.md, blocks ch09-10, ch11, ch12-13, ch14-15, ch16-17, ch18-19, ch20-22) were read first.

Checks: `tools/chapcheck.sh appE /tmp/prose-appE` exit 0, 41 pp, 0 undefined references, 0 multiply defined labels, 0 floats too large, 0 overfull > 5pt.

## Detector (tools/llmese.py), hits before -> after
| file | before | after |
|---|---|---|
| D-30 | 1 (cleft) | 0 |
| D-31 | 1 (X-not-Y) | 1 (kept) |
| D-44 | 1 (count-teaser) | 0 |
| D-45 | 1 (metaphor-verb) | 1 (kept) |
| D-47 | 1 (self-narration) | 0 |
| all other files | 0 | 0 |

Kept hits:
- D-31:16, "since it came from the static positions, not from the phonons": the reader has just seen the phonon momenta reduced by G and would expect this phase to be reduced too. The contrast takes one clause.
- D-45:27, "the source does the work": this is literal physics (mechanical work), not a metaphor.

## Lint (lint.py with BANNED-TERMS.txt), hits per file before -> after
D-30 2->2, D-31 0->0, D-32 0->0, D-33 3->3, D-34 2->2, D-35 2->2, D-36 1->1, D-37 5->5, D-38 3->3, D-39 1->1, D-40 8->8, D-42 2->2, D-43 0->0, D-44 1->1, D-45 2->2, D-46 5->5, D-47 1->1, appE.tex 0->0. There are 0 blocking hits before and after. All remaining hits are LONG-SENT or EQ-PUNCT in untouched sentences or in display markup. None is in a sentence written in this round.

## Sentences changed: 23 (in 14 files)

| file:line | before | after | pattern |
|---|---|---|---|
| D-30:41 | Three symmetries reduce the rows of eq:8.1-rows for the electrons. (four items follow, the first is continuity) | The continuity equation and three symmetries (spin rotations, inversion with time reversal, and rotations about a symmetry axis) reduce the rows ... | count-teaser; count did not match the list |
| D-30:43 | What remains of the currents are the transverse components ... | The remaining currents are the transverse components ... | cleft |
| D-43:7 | Two hypotheses of sec:18.1-branching enter. The process is Markov: ... And different particles evolve independently: ... | The process is Markov, and its particles evolve independently, the two hypotheses of sec:18.1-branching: the outcome ..., and the kernels ... | count-teaser, sentence-initial "And" |
| D-43:38 | A carrier cascade terminates for a simple reason. Order the states ... | Order the states ... | evaluation without content (0) |
| D-40:37 | ... the coherent part of the total. Two corrections set it. The self-energy ... | ... the coherent part of the total. The self-energy ... | count-teaser |
| D-42:47 | Two limits are closed. As Δ_tl → 0 ... | As Δ_tl → 0 ... | count-teaser |
| D-44:27 | Four conditions are needed. | The proof needs four conditions: | count-teaser, now the lead-in to the list |
| D-36:71 | The four-path term alone gives something else. With y_ab = ..., write ... | For the four-path term alone, with y_ab = ..., write ... | withholding (25) |
| D-36:28 | The density matrix reaches the theorem without Fock space: | The density-matrix derivation needs no Fock space: | anthropomorphic verb (15) |
| D-31:39 | ... doing the elementary angular integrals reduces each pair by spherical Bessel functions ... | ... turns the average for each pair into a sum of spherical Bessel functions ... | Addendum-4 sentence that needed a second reading |
| D-32:48 | Every order of the expansion is available: the k-th derivative ... gives the cumulant | The k-th derivative ... gives the cumulant | colon reveal |
| D-47:3 | Here we derive the three statements ... | We derive the three statements ... | self-narration |
| D-38:65 | The excess sits in the square roots of eq:7.1-HP | The excess comes from the square roots of eq:7.1-HP | metaphor verb |
| D-42:36/45 | "..., with f the Fermi function." attached to the normal-state expression, which has no f | definition moved to the display that uses f: "with E' = E + Δ_tl and f the Fermi function." | definition at first use |
| D-37:39 | electrons that ride on the displaced lattice | electrons that move with the displaced lattice | figurative verb |

Other changes: "sits at/sit on/sits where" became "lies at/lie on/lies where" (D-34:27, D-38:7, D-46:42). "therefore" was deleted where the preceding sentence already makes the inference (D-32:44, D-38:11, D-44:9, D-45:27). The other "therefore" and "Hence" mark derivation steps and were kept.

## Addendum 4 audit (routine algebra replaced by a sentence)
Each replacement sentence in D-30, D-31, D-32, D-34, D-35, D-38, D-39, D-40, D-42, D-43, D-45, D-46 and D-47 names its operation and its result, either as a display or as a labelled equation. None of them is a bare "it can be shown" or "straightforward algebra".

## Left for the reviewer (not changed)
- D-36:84: "... which with the gas value f_x = -e^2/4k_F^2 (sec:4.6) is the ratio quoted in sec:13.4." This sentence points to the result instead of stating it. Adding the number would be new content, which this round does not allow.
- D-45:51: "non-negative term by term under conditions (a), (b), (d) and (e) ..., together with (c), which makes the x terms non-negative together" reads awkwardly, with "together" twice. I could not split it without deciding which terms each condition covers, which would change the claim. Left as is.
- D-32:48 and D-40:75 attribute with source equation numbers (\cite[Eqs. (37)-(39) and App. B], \cite[Eq. (17)]), and D-42:7 and D-42:47 do the same. This is pattern 22, but citation arguments are outside the limits of this round.
