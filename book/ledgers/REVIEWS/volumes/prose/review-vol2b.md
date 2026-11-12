# Stage-2 review of the prose round, Volume II (b): Chaps. 14–22, Apps. E, F

Base 8904b84. Read: `git diff --word-diff=plain 8904b84 -- book/tex/ch14 … appF` (297 changed lines, 357 change spans; appF had none), every span against the old text, with the surrounding paragraph for each deletion. Rules: PROSE.md (incl. Stage 2) and prose-review.md.

## Counts
- Change spans reviewed: 357. Kept 342, fixed 12, reverted 3.
- Untouched text: 15+ paragraphs sampled (list below); 3 misses fixed (s19-6:169, s19-5:293, s18-3:91), plus the D-45:51 sentence the appE editor flagged.
- Total interventions in this review: 19 (12 fixed, 3 reverted, 4 untouched-text fixes).

## Checks
- chapcheck (`tools/chapcheck.sh <unit> /tmp/rev2b-<unit>`) for ch14, ch16, ch17, ch18, ch19, ch20, ch21, appE: exit 0 each; 0 undefined references; 0 multiply defined labels.
- llmese.py on the 17 touched files: one new candidate, s21-2:108 X-not-Y "measures the table, not the physics" (restored on purpose: the contrast the reader needs). The restored s17-5:113 and s21-7:9 contrasts raise no hit. lint.py with BANNED-TERMS: 0 blocking in every touched file.
- Flat-verb check: I scripted a count of "lie(s)", "dominat*" and "is at/in" in every paragraph with a changed line. Stacks the edit created were fixed at s14-5:140, s16-8:46, s17-1:24, s17-3:3 and s18-4:80. s17-4:87 has two parallel "the rate lies on the lower/upper edge", kept as parallel. The others are 200 or more characters apart, or were in the old text.

## Editors' flags
- s19-6:169 (three hypotheses listed, then each restated, then "The second hypothesis"): kept the listing sentence, which names the members (pattern 18; restored in an earlier round). The restatements became one sentence that carries only the details the list lacks (where the reservoir is stored, local events thermal or tunneling, the bounds Γmin, Γmax, the glass analogy), plus "We write the law of single-event energies as p_LEE(E)". "The second hypothesis" still refers to the listed order. No fact lost.
- D-45:51 ("together" twice): "…, together with (c), which makes the $x$ terms non-negative together." → "…, and under condition (c), which makes the sum of the $x$ terms non-negative." The assignment of conditions to terms is unchanged: (a), (b), (d) and (e) term by term, and (c) for the $x$ terms jointly.

## Fixes and reverts in the round's edits (current line numbers)
| file:line | old (8904b84) | edited (round) | verdict | why / now |
|---|---|---|---|---|
| ch14/s14-5:116 | Two steps carry the estimate: the created phonons sample the band as the average assumes, and their chirality survives | The estimate assumes that the created phonons sample the band as the average does and … | fixed | "as the average does" was opaque. Now "each created phonon lands at random in the band, as in the average, and that its chirality survives the decay" (the paragraph's own "placed at random") |
| ch14/s14-5:140 | the metastable line sits at 1.098 meV | … lies at … (next sentence: "lies 0.18 meV lower") | fixed | "lies" stacked; now "is at" |
| ch16/s16-2:3 | which is what the sum-rule bounds … need to come close to saturation | the case in which the sum-rule bounds … come close to saturation | fixed | necessary condition had become sufficient (s16-2:200: the line's position also matters); now "which the sum-rule bounds of \cref{sec:10.2} need to come close to saturation" |
| ch16/s16-8:46 | one phonon takes over below 0.21 K | the one-phonon rate dominates below 0.21 K | fixed | "dominate" twice in adjacent sentences; now "the one-phonon rate exceeds the electron rate below 0.21 K" |
| ch17/s17-1:9 | The boundary does not sit exactly at the ceiling | The boundary lies above the ceiling | reverted | "lies above" dropped "near"; now "is not exactly at the ceiling" |
| ch17/s17-1:24 | the free recoil takes over above 60 MeV | … dominates … (previous sentence: "dominate") | fixed | now "the free recoil leads", the chapter's own verb (s17-1:62) |
| ch17/s17-3:3 | where its line sits | where its line lies (same sentence group: "lies below the splitting") | fixed | now "where its line falls" |
| ch17/s17-5:113 | A window ``against silicon'' does not give the ranking of the materials among themselves, and every pair needs its own. | (deleted) | reverted | the conclusion appears nowhere else, and the worked example we:17-window gives only its title; restored verbatim |
| ch17/s17-6:68 | A wide interval can therefore rise. | A material with a wide interval can therefore be in a higher tier. | fixed | "higher tier" is ambiguous (tier 6 ranks above 7); now "can therefore rank in a better tier than one with a better median" (the GaAs/CaWO4 example) |
| ch18/s18-4:80 | slope 1.54 sits below …; the nonlinearity sits in $k_2$ | … lies below …; … lies in $k_2$ (after "1.89 lies inside") | fixed | three "lies" in three sentences; now "is below" and "comes from $k_2$" |
| ch18/s18-5:123 | Nor is the separation of the pairs …, which decides … whether a field prevents binding. | Nor has the separation …, which decides …, been computed. | fixed | split verb needed a second reading; now "The separation …, which decides …, has not been computed either." |
| ch19/s19-2:124 | Their balance shifts at low energy. | The balance between the two channels shifts … (previous sentence: "boundary between the two channels") | fixed | repeated phrase; now "The balance between Migdal and collisional excitation shifts at low energy." |
| ch20/s20-5:90 | What survives is the soft energy, the share $f_s$ … | The soft energy remains, the share $f_s$ … | fixed | dangling appositive; now "The soft energy remains. It is the share $f_s$ …" |
| ch21/s21-2:108 | measures the table, not the physics. | measures the cells of the table. | reverted | the contrast is the point (an artifact of the tabulation); old restored |
| ch21/s21-7:9 | is a statement about the documented record of a crystal, not about its physics, | records what has been documented for a crystal, | fixed | the reader would otherwise read "conditional" as "physically worse"; now "records what has been documented for a crystal, not its physics, and it changes …" |

Checked and kept, though suspected of drift: D-30:41 (the continuity equation is named because it heads its own paragraph), D-36:71 (the paragraph ends "the two terms add to the frame result"), s14-summary:9 ("too strong by 1.99 for records shorter than the coherence time" matches s14-6:171 and tab. at s14-5:197), s15-1:3 ("accurate far above the pair-breaking edge" is the claim of the ch15 opening), s15-2:71, s16-1:40 (the paragraph's last sentence states the meaning), s17-2:64 and :74 ("handover" is defined by the worked-example title), s17-4:9, s17-5:172 (3.87 > 3.38, so "more than compensates" holds), s18-1:52, s18-4:14 (s18-4:118 names the constant as the likely cause), s19-5:65, s21-1:27, s21-1:47 (η2 is fixed by η, s21-1:52), s21-1:90, s21-3:108, s21-3:131 (the 0.54/−1.62 vs 1/−2 dependences are the "mixture").

## Untouched paragraphs sampled (step 3)
1. ch14.tex opening paragraph; 2. caption of fig:14-map; 3. ch17.tex opening (both paragraphs); 4. ch19.tex opening paragraph; 5. appF.tex opening; 6. s16-summary, paragraphs 3–4 (donors/color centers, glasses); 7. s18-summary (all paragraphs); 8. s21-summary, paragraphs 2–6; 9. s22-summary, paragraph 1; 10. s14-1:3 section opener; 11. s16-3:3 opener; 12. s20-3:3 opener and its next paragraph; 13. s20-4:3 opener; 14. s22-2:3 opener; 15. D-39 opening; 16. worked examples we:16-heat, we:18-capture, we:19-degeneracy (s19-5:293), we:20-ceiling, we:15-film; 17. Limit Check boxes lim:18.3a, lim:20.2a, lim:20.4a, lim:16.7c; 18. s16-6:115, s16-7:26, s21-4:92; 19. s19-6:169.

Misses fixed:
| file:line | old | now | pattern |
|---|---|---|---|
| ch19/s19-6:169 | three hypotheses listed, then "The source is a reservoir … It relaxes by local events … whose rates are spread uniformly in lnΓ … The energies of single events follow a law … that does not change in time." | "The reservoir $U_{\mathrm{rel}}$ is stored at cooldown in the crystal, the glue and the interfaces of the holder, and it relaxes by local events, thermally activated or tunneling, with rates between Γmin and Γmax, spread as the barriers of a glass are (…). We write the law of single-event energies as $p_{\mathrm{LEE}}(E)$." | 26, looped restatement |
| ch19/s19-5:293 | "It gives f_ion = 0.324; Lindhard's yield alone, …, gives 0.346; the same analysis notes …" | split at both semicolons into three sentences | needs a second reading |
| ch18/s18-3:91 (caption fig:18-limit-seed) | "Light gray: ω > 12.95 eV, where the uniform and equal splits are." | "… where the uniform and equal splits are again within 0.1 of the dark-matter seed." | elliptical, needs a second reading |
| appE/D-45:51 | see Editors' flags | | flagged by the editor |

The other sampled paragraphs pass. Their remaining X-not-Y and "far from" hits are validity statements or contrasts the reader needs.

## All change spans of the round (file:line at review time | old | edited | verdict | why)
Generated from the word diff. Each row is one change span: changes less than 60 characters apart are merged. Long spans are cut at 140 characters. "kept" rows give the pattern the edit removed and confirm that the meaning, numbers and references are unchanged.

| file:line | old | edited | verdict | why |
|---|---|---|---|---|
| appE/D-30.tex:41 | Three symmetries | The continuity equation and three symmetries (spin rotations, inversion with time reversal, and rotations about a symmetry axis) | kept | rewording; meaning, numbers and references unchanged |
| appE/D-30.tex:43 | What remains of the | The remaining | kept | cleft -> direct statement |
| appE/D-31.tex:39 | reduces each pair by | turns the average for each pair into a sum of | kept | rewording; meaning, numbers and references unchanged |
| appE/D-32.tex:44 | therefore | (deleted) | kept | redundant "therefore" cut; inference still explicit |
| appE/D-32.tex:48 | Every order of the expansion is available: the | The | kept | rewording; meaning, numbers and references unchanged |
| appE/D-34.tex:27 | sits | lies | kept | "sit" metaphor verb -> plain verb; literal position |
| appE/D-36.tex:28 | density matrix reaches the theorem without | density-matrix derivation needs no | kept | rewording; meaning, numbers and references unchanged |
| appE/D-36.tex:71 | The four-path term alone gives something else. With | For the four-path term alone, with | kept | count-teaser cut; members named in the text |
| appE/D-37.tex:39 | ride on | move with | kept | rewording; meaning, numbers and references unchanged |
| appE/D-38.tex:7 | sit | lie | kept | "sit" metaphor verb -> plain verb; literal position |
| appE/D-38.tex:11 | therefore | (deleted) | kept | redundant "therefore" cut; inference still explicit |
| appE/D-38.tex:65 | sits in | comes from | kept | "sit" metaphor verb -> plain verb; literal position |
| appE/D-40.tex:37 | Two corrections set it. | (deleted) | kept | count-teaser cut; members named in the text |
| appE/D-42.tex:36 | absorption, with $f$ the Fermi function. | absorption. | kept | rewording; meaning, numbers and references unchanged |
| appE/D-42.tex:45 | \Delta_{\mathrm{tl}}$. | \Delta_{\mathrm{tl}}$ and $f$ the Fermi function. | kept | rewording; meaning, numbers and references unchanged |
| appE/D-42.tex:47 | Two limits are closed. | (deleted) | kept | count-teaser cut; members named in the text |
| appE/D-43.tex:7 | Two hypotheses of \cref{sec:18.1-branching} enter. The | As in \cref{sec:18.1-branching}, the | kept | count-teaser cut; members named in the text |
| appE/D-43.tex:7 | And different | Different | kept | rewording; meaning, numbers and references unchanged |
| appE/D-43.tex:38 | A carrier cascade terminates for a simple reason. | (deleted) | kept | deleted sentence carried no fact absent from the paragraph |
| appE/D-43.tex:78 | provides two checks on any solution. The | gives two checks on any solution: the | kept | count-teaser cut; members named in the text |
| appE/D-44.tex:9 | therefore | (deleted) | kept | redundant "therefore" cut; inference still explicit |
| appE/D-44.tex:27 | Four conditions are needed. | The proof needs four conditions: | kept | rewording; meaning, numbers and references unchanged |
| appE/D-45.tex:27 | therefore | (deleted) | kept | redundant "therefore" cut; inference still explicit |
| appE/D-46.tex:42 | sits | lies | kept | "sit" metaphor verb -> plain verb; literal position |
| appE/D-47.tex:3 | Here we | We | kept | rewording; meaning, numbers and references unchanged |
| ch14/ch14.tex:2 | stand in for | replace | kept | rewording; meaning, numbers and references unchanged |
| ch14/s14-1.tex:7 | lives | is localized | kept | rewording; meaning, numbers and references unchanged |
| ch14/s14-1.tex:7 | at all | (deleted) | kept | sentence-final "at all" cut |
| ch14/s14-1.tex:18 | two things change. The | the | kept | count-teaser cut; members named in the text |
| ch14/s14-1.tex:61 | true ground state is not the Néel state. The pair term of \cref{eq:7.1-Hk} mixesin states with a deviation on each sublattice, | pair term of \cref{eq:7.1-Hk} mixes states with a deviation on each sublattice into the ground state, | kept | negation framing -> positive statement; condition kept |
| ch14/s14-1.tex:76 | does not remove weight; it moves the fraction $\Delta S/\|\vect{S}\|$ of it | moves the fraction $\Delta S/\|\vect{S}\|$ of the weight | kept | negation framing -> positive statement; condition kept |
| ch14/s14-1.tex:110 | Two limits | The light and heavy ends | kept | rewording; meaning, numbers and references unchanged |
| ch14/s14-1.tex:124 | take over, | dominate, | kept | metaphor verb -> "dominates" |
| ch14/s14-1.tex:124 | later | higher | kept | rewording; meaning, numbers and references unchanged |
| ch14/s14-2.tex:19 | response at all, | response, | kept | sentence-final "at all" cut |
| ch14/s14-2.tex:61 | do not move independently. | interact. | kept | negation framing -> positive statement; condition kept |
| ch14/s14-2.tex:114 | sits | lies | kept | "sit" metaphor verb -> plain verb; literal position |
| ch14/s14-2.tex:114 | takes over | dominates | kept | metaphor verb -> "dominates" |
| ch14/s14-3.tex:14 | ions, and | ions; | kept | rewording; meaning, numbers and references unchanged |
| ch14/s14-3.tex:14 | and $\mathcal{J}^{\alpha\alpha}_e$therefore | so $\mathcal{J}^{\alpha\alpha}_e$ | kept | redundant "therefore" cut; inference still explicit |
| ch14/s14-3.tex:33 | sit | lie | kept | "sit" metaphor verb -> plain verb; literal position |
| ch14/s14-3.tex:33 | fragile | sensitive | kept | figurative word -> technical verb/noun |
| ch14/s14-3.tex:52 | belongs | applies | kept | figurative word -> technical verb/noun |
| ch14/s14-3.tex:56 | sits | lies | kept | "sit" metaphor verb -> plain verb; literal position |
| ch14/s14-3.tex:109 | sits | lies | kept | "sit" metaphor verb -> plain verb; literal position |
| ch14/s14-3.tex:115 | sits on | is tuned to | kept | "sit" metaphor verb -> plain verb; literal position |
| ch14/s14-4.tex:14 | corrections | corrections, for temperature and for the orbital moment, | kept | rewording; meaning, numbers and references unchanged |
| ch14/s14-4.tex:14 | first is temperature. The | (deleted) | kept | deleted sentence carried no fact absent from the paragraph |
| ch14/s14-4.tex:41 | can be trusted | holds | kept | rewording; meaning, numbers and references unchanged |
| ch14/s14-4.tex:53 | is in close agreement | agrees closely | kept | rewording; meaning, numbers and references unchanged |
| ch14/s14-4.tex:62 | positivity gives only a lower bound. The | the transverse part alone is only a lower bound on the rate of the contact interaction: the | kept | rewording; meaning, numbers and references unchanged |
| ch14/s14-4.tex:62 | negative, and the transverse part alone is a lower bound on the rate of the contact interaction. | negative. | kept | rewording; meaning, numbers and references unchanged |
| ch14/s14-4.tex:62 | say nothing. | leave the rate unconstrained. | kept | negation framing -> positive statement; condition kept |
| ch14/s14-4.tex:94 | at the price of | with | kept | figurative word -> technical verb/noun |
| ch14/s14-4.tex:104 | cleaner | easier | kept | rewording; meaning, numbers and references unchanged |
| ch14/s14-4.tex:118 | costs more. | gives larger errors. | kept | rewording; meaning, numbers and references unchanged |
| ch14/s14-4.tex:118 | is there to check. | checks. | kept | rewording; meaning, numbers and references unchanged |
| ch14/s14-5.tex:116 | Two steps carry the estimate: the created phonons sample the band as the average assumes, and | The estimate assumes that the created phonons sample the band as the average does and that | fixed | "as the average does" was vague; now "each created phonon lands at random in the band, as in the average, and that its chirality survives" |
| ch14/s14-5.tex:127 | sit | lie | kept | "sit" metaphor verb -> plain verb; literal position |
| ch14/s14-5.tex:140 | sits | lies | fixed | "lies at ... lies 0.18 meV lower" in consecutive sentences; first now "is at" |
| ch14/s14-5.tex:166 | decides what the response is made of. | shows which states contribute. | kept | cleft -> direct statement |
| ch14/s14-6.tex:16 | sits | lies | kept | "sit" metaphor verb -> plain verb; literal position |
| ch14/s14-6.tex:41 | The golden-rule mean is not yet what one record measures. | (deleted) | kept | cleft -> direct statement |
| ch14/s14-6.tex:41 | is a different matter, | behaves differently, | kept | rewording; meaning, numbers and references unchanged |
| ch14/s14-6.tex:62 | sit | lie | kept | "sit" metaphor verb -> plain verb; literal position |
| ch14/s14-6.tex:66 | nucleus, and what survives, through | nucleus; | kept | cleft -> direct statement |
| ch14/s14-6.tex:66 | leaves), is | leaves) gives | kept | rewording; meaning, numbers and references unchanged |
| ch14/s14-summary.tex:9 | it, and a fixed-amplitude analysis misses the random amplitude by a factor 1.99 for the median limit. | it. A fixed-amplitude analysis, which ignores the random amplitude, sets the median limit too strong by a factor 1.99 for records shorter... | kept | rewording; meaning, numbers and references unchanged |
| ch15/s15-1.tex:3 | adequate in stated regimes: | accurate far above the pair-breaking edge: | kept | rewording; meaning, numbers and references unchanged |
| ch15/s15-1.tex:41 | What is left | The remaining integral | kept | cleft -> direct statement |
| ch15/s15-1.tex:70 | nothing | zero | kept | negation framing -> positive statement; condition kept |
| ch15/s15-1.tex:123 | rest | depend | kept | rewording; meaning, numbers and references unchanged |
| ch15/s15-1.tex:139 | at all | (deleted) | kept | sentence-final "at all" cut |
| ch15/s15-2.tex:71 | So is the film geometry, | The film geometry also lies outside the model | kept | rewording; meaning, numbers and references unchanged |
| ch15/s15-3.tex:91 | does not select by itself. | alone does not select. | kept | negation framing -> positive statement; condition kept |
| ch15/s15-3.tex:125 | is the input to the sheet response, not the final answer. | enters the rate only through the sheet response. | kept | negation framing -> positive statement; condition kept |
| ch15/s15-4.tex:13 | sits | lies | kept | "sit" metaphor verb -> plain verb; literal position |
| ch15/s15-4.tex:48 | current: the third body decides. | current. | kept | rewording; meaning, numbers and references unchanged |
| ch15/s15-4.tex:86 | wins | dominates | kept | metaphor verb -> "dominates" |
| ch15/s15-4.tex:102 | is not at | lies above | kept | negation framing -> positive statement; condition kept |
| ch15/s15-4.tex:124 | sit | lie | kept | "sit" metaphor verb -> plain verb; literal position |
| ch15/s15-4.tex:128 | controlling caveat. | main limitation. | kept | rewording; meaning, numbers and references unchanged |
| ch15/s15-summary.tex:9 | by itself | without a third body | kept | rewording; meaning, numbers and references unchanged |
| ch16/ch16.tex:2 | inputs rather than by their formulas. | inputs. | kept | rewording; meaning, numbers and references unchanged |
| ch16/s16-1.tex:22 | sits | is | kept | "sit" metaphor verb -> plain verb; literal position |
| ch16/s16-1.tex:40 | The published loss function has an exact physical meaning. | (deleted) | kept | deleted sentence carried no fact absent from the paragraph |
| ch16/s16-1.tex:80 | which the reach of an anisotropic target must be computed with. The background tensor also orders the directions by itself. | and the reach of an anisotropic target must be computed from these integrals. The background tensor also orders the directions. | kept | rewording; meaning, numbers and references unchanged |
| ch16/s16-1.tex:101 | What replaces \cref{eq:16.1-L} for such targets is open. | For such targets \cref{eq:16.1-L} has no known replacement. | kept | cleft -> direct statement |
| ch16/s16-2.tex:3 | sits in a single line at low energy, whichis what the sum-rule bounds of \cref{sec:10.2}need to | is in a single line at low energy, the case in which the sum-rule bounds of \cref{sec:10.2} | fixed | edit turned a necessary condition ("what the bounds need") into a sufficient one; now "which the sum-rule bounds of sec:10.2 need to come close to saturation" |
| ch16/s16-2.tex:100 | How much of it reaches a sensor is a question for the cascade of \cref{chap:18}, not for the response. | The fraction that reaches a sensor is set by the cascade of \cref{chap:18}. | kept | negation framing -> positive statement; condition kept |
| ch16/s16-2.tex:172 | sits | lies | kept | "sit" metaphor verb -> plain verb; literal position |
| ch16/s16-2.tex:187 | sits | is | kept | "sit" metaphor verb -> plain verb; literal position |
| ch16/s16-2.tex:200 | sits | lies | kept | "sit" metaphor verb -> plain verb; literal position |
| ch16/s16-4.tex:3 | sit | are | kept | "sit" metaphor verb -> plain verb; literal position |
| ch16/s16-4.tex:62 | sits | lies | kept | "sit" metaphor verb -> plain verb; literal position |
| ch16/s16-4.tex:82 | beyond the reach of the incoherent sum. | which the incoherent sum does not contain. | kept | rewording; meaning, numbers and references unchanged |
| ch16/s16-5.tex:60 | sits | is | kept | "sit" metaphor verb -> plain verb; literal position |
| ch16/s16-5.tex:102 | sit at | occupy | kept | "sit" metaphor verb -> plain verb; literal position |
| ch16/s16-5.tex:106 | What replaces it is | The isolated-donor response must be replaced by | kept | cleft -> direct statement |
| ch16/s16-6.tex:3 | sit | lie | kept | "sit" metaphor verb -> plain verb; literal position |
| ch16/s16-6.tex:36 | What is read in practice are | In practice the readout uses | kept | cleft -> direct statement |
| ch16/s16-6.tex:59 | sits | is | kept | "sit" metaphor verb -> plain verb; literal position |
| ch16/s16-6.tex:78 | that failure is what the escape probability below absorbs. | the escape probability below accounts for that failure. | kept | cleft -> direct statement |
| ch16/s16-7.tex:3 | sit in | occupy | kept | "sit" metaphor verb -> plain verb; literal position |
| ch16/s16-7.tex:3 | plainest | simplest | kept | rewording; meaning, numbers and references unchanged |
| ch16/s16-7.tex:13 | sit, | are, | kept | "sit" metaphor verb -> plain verb; literal position |
| ch16/s16-7.tex:98 | What the two-level systems addis | The two-level systems add | kept | cleft -> direct statement |
| ch16/s16-7.tex:233 | the velocities that dominate the observable, not at one speed. | all the velocities that dominate the observable. | kept | negation framing -> positive statement; condition kept |
| ch16/s16-8.tex:28 | win | dominate | kept | metaphor verb -> "dominates" |
| ch16/s16-8.tex:46 | one phonon takes over | the one-phonon rate dominates | fixed | "dominate" twice in adjacent sentences; now "the one-phonon rate exceeds the electron rate below 0.21 K" |
| ch16/s16-8.tex:74 | wins against | outweighs | kept | metaphor verb -> "dominates" |
| ch16/s16-summary.tex:5 | at the price of | suppressed by | kept | figurative word -> technical verb/noun |
| ch17/s17-1.tex:9 | wins | dominates | kept | metaphor verb -> "dominates" |
| ch17/s17-1.tex:9 | does not sit exactly at | lies above | reverted | "lies above the ceiling" dropped the nearness of "not exactly at"; now "The boundary is not exactly at the ceiling, however:" |
| ch17/s17-1.tex:24 | take over | dominate | kept | metaphor verb -> "dominates" |
| ch17/s17-1.tex:24 | takes over | dominates | fixed | "dominate"/"dominates" in adjacent sentences; this one now "the free recoil leads" (the chapter's own verb, s17-1:62) |
| ch17/s17-1.tex:44 | sits | lies | kept | "sit" metaphor verb -> plain verb; literal position |
| ch17/s17-1.tex:44 | Three regimes explain its values. | (deleted) | kept | count-teaser cut; members named in the text |
| ch17/s17-1.tex:53 | sits | lies | kept | "sit" metaphor verb -> plain verb; literal position |
| ch17/s17-1.tex:62 | reflects | at \SI{12.3}{MeV} is a property of | kept | rewording; meaning, numbers and references unchanged |
| ch17/s17-1.tex:62 | The mass of \SI{12.3}{MeV} is a property of the model, not of silicon. | (deleted) | kept | negation framing -> positive statement; condition kept |
| ch17/s17-1.tex:64 | Which of the low-threshold regions exists is decided by screening. | Screening decides which of the low-threshold regions exists. | kept | rewording; meaning, numbers and references unchanged |
| ch17/s17-1.tex:64 | channel at all. | channel. | kept | sentence-final "at all" cut |
| ch17/s17-1.tex:91 | at which electron recoil takes over | above which electron recoil dominates | kept | metaphor verb -> "dominates" |
| ch17/s17-1.tex:91 | robust against | insensitive to | kept | rewording; meaning, numbers and references unchanged |
| ch17/s17-2.tex:14 | sit | lie | kept | "sit" metaphor verb -> plain verb; literal position |
| ch17/s17-2.tex:57 | takes over; | dominates; | kept | metaphor verb -> "dominates" |
| ch17/s17-2.tex:64 | \emph{The phonon line does not decide it.} | \emph{GaAs at \SI{1.17}{eV}.} | kept | negation framing -> positive statement; condition kept |
| ch17/s17-2.tex:74 | silicon takes over within a meV of its | the handover lies within a meV of the silicon | kept | metaphor verb -> "dominates" |
| ch17/s17-2.tex:92 | Three regimes follow. | (deleted) | kept | count-teaser cut; members named in the text |
| ch17/s17-2.tex:92 | quantum at all. | quantum. | kept | sentence-final "at all" cut |
| ch17/s17-2.tex:94 | Two effects | Squeezing and dark counts | kept | rewording; meaning, numbers and references unchanged |
| ch17/s17-2.tex:94 | counter, moreover, | counter | kept | rewording; meaning, numbers and references unchanged |
| ch17/s17-3.tex:3 | Here we follow it into the collective modes, phonons, magnons and plasmons, which \cref{sec:8.2-exothermic} showed to be the natural fina... | The collective modes, phonons, magnons and plasmons, are the natural final states of down-scattering (\cref{sec:8.2-exothermic}): | kept | figurative word -> technical verb/noun |
| ch17/s17-3.tex:3 | sits, | lies, | fixed | "lies below ... where its line lies" in one paragraph; now "where its line falls" |
| ch17/s17-3.tex:54 | Three kinds of mode follow from these formulas. | (deleted) | kept | count-teaser cut; members named in the text |
| ch17/s17-3.tex:54 | carries | includes | kept | figurative word -> technical verb/noun |
| ch17/s17-3.tex:70 | sits | lies | kept | "sit" metaphor verb -> plain verb; literal position |
| ch17/s17-3.tex:96 | paid from | supplied by | kept | rewording; meaning, numbers and references unchanged |
| ch17/s17-4.tex:9 | This cell is never a correction. | (deleted) | kept | deleted sentence carried no fact absent from the paragraph |
| ch17/s17-4.tex:49 | sits at | is of | kept | "sit" metaphor verb -> plain verb; literal position |
| ch17/s17-4.tex:72 | restriction to one sector needs care. The | (deleted) | kept | deleted sentence carried no fact absent from the paragraph |
| ch17/s17-4.tex:74 | Written in | In | kept | rewording; meaning, numbers and references unchanged |
| ch17/s17-4.tex:74 | is the following result. | reads as follows. | kept | rewording; meaning, numbers and references unchanged |
| ch17/s17-4.tex:87 | is thennot absent but cancels the other two, and the rate sits | then cancels the other two, and the rate lies | kept | "sit" metaphor verb -> plain verb; literal position |
| ch17/s17-4.tex:87 | sits | lies | kept | "sit" metaphor verb -> plain verb; literal position |
| ch17/s17-4.tex:89 | trouble is that the silicon window | silicon window, however, | kept | rewording; meaning, numbers and references unchanged |
| ch17/s17-4.tex:98 | it changes an observable rate by more than a correction to a correction in the window alone. | only in the window does it change an observable rate by more than a correction to a correction. | kept | rewording; meaning, numbers and references unchanged |
| ch17/s17-4.tex:111 | is the one that matters, and it | (deleted) | kept | deleted sentence carried no fact absent from the paragraph |
| ch17/s17-5.tex:3 | number of this kind, a property of the material alone that the rate or the reach of one channel is proportional to, is what a comparison ... | comparison of targets needs numbers of this kind, properties of the material alone to which the rate or the reach of one channel is propo... | kept | cleft -> direct statement |
| ch17/s17-5.tex:42 | What a single number can giveis | A single number can give | kept | cleft -> direct statement |
| ch17/s17-5.tex:90 | pull in opposite directions: | favor opposite lattices: | kept | rewording; meaning, numbers and references unchanged |
| ch17/s17-5.tex:92 | and the reason is the shift of the halo integral by the sound speed. | because the sound speed shifts the halo integral. | kept | rewording; meaning, numbers and references unchanged |
| ch17/s17-5.tex:100 | carries | enters with | kept | figurative word -> technical verb/noun |
| ch17/s17-5.tex:113 | A window ``against silicon'' does not give the ranking of the materials among themselves, and every pair needs its own. | (deleted) | reverted | deleted sentence carried a conclusion stated nowhere else (a window against silicon does not rank other pairs); restored verbatim from 8904b84 |
| ch17/s17-5.tex:146 | The errors matter for the figures of merit. | (deleted) | kept | deleted sentence carried no fact absent from the paragraph |
| ch17/s17-5.tex:172 | gives it back. | more than compensates. | kept | rewording; meaning, numbers and references unchanged |
| ch17/s17-5.tex:174 | sits | lies | kept | "sit" metaphor verb -> plain verb; literal position |
| ch17/s17-5.tex:176 | sit | lie | kept | "sit" metaphor verb -> plain verb; literal position |
| ch17/s17-6.tex:3 | turns | depends | kept | figurative word -> technical verb/noun |
| ch17/s17-6.tex:27 | carry | decide | kept | figurative word -> technical verb/noun |
| ch17/s17-6.tex:49 | rewards a lead that the widths cannot overturn, not the size of the lead. | measures whether the widths can overturn a lead, not how large the lead is. | kept | negation framing -> positive statement; condition kept |
| ch17/s17-6.tex:60 | The pairs that do not separate are the instructive ones. | (deleted) | kept | negation framing -> positive statement; condition kept |
| ch17/s17-6.tex:60 | temperature, and the widths make this visible. | temperature. | kept | rewording; meaning, numbers and references unchanged |
| ch17/s17-6.tex:68 | wide interval can therefore rise. | material with a wide interval can therefore be in a higher tier. | fixed | "be in a higher tier" is ambiguous (tier 6 is better than 7); now "rank in a better tier than one with a better median" |
| ch17/s17-6.tex:68 | never invent an | add no | kept | rewording; meaning, numbers and references unchanged |
| ch17/s17-6.tex:68 | the two are read together. \Cref{fig:17-rank-floor}c shows both at once. | \cref{fig:17-rank-floor}c shows both. | kept | count-teaser cut; members named in the text |
| ch17/s17-6.tex:77 | are blind to correlation. Joint statements are what move. | do not depend on the correlation. Joint statements change. | kept | cleft -> direct statement |
| ch17/s17-6.tex:108 | sits | lies | kept | "sit" metaphor verb -> plain verb; literal position |
| ch18/ch18.tex:23 | The chain never asks for the total $S_{ab}(\vect{q},\omega)$ on its own: | No step of the chain uses the total $S_{ab}(\vect{q},\omega)$: | kept | rewording; meaning, numbers and references unchanged |
| ch18/s18-1.tex:52 | in a cascade has a special place. | depends on the sector of the seed. | kept | rewording; meaning, numbers and references unchanged |
| ch18/s18-1.tex:72 | The ratios of rates enter, not the rates, since the cascade at a given energy depends on which collision comes first, not on when; | Only the ratios of rates enter, because the cascade at a given energy depends on the order of the collisions and not on their timing; | kept | negation framing -> positive statement; condition kept |
| ch18/s18-1.tex:79 | sit | are | kept | "sit" metaphor verb -> plain verb; literal position |
| ch18/s18-1.tex:82 | sits | is then | kept | "sit" metaphor verb -> plain verb; literal position |
| ch18/s18-1.tex:104 | What the reduction does fix is where the momentum memory sits. | The reduction does fix which carriers keep a memory of momentum. | kept | "sit" metaphor verb -> plain verb; literal position |
| ch18/s18-1.tex:128 | does not inject one carrier: it | (deleted) | kept | negation framing -> positive statement; condition kept |
| ch18/s18-2.tex:3 | sit on the axis of deposited energy, and how sharp | lie on the axis of deposited energy, and how wide | kept | "sit" metaphor verb -> plain verb; literal position |
| ch18/s18-2.tex:13 | has nothing todo with | is unrelated to | kept | negation framing -> positive statement; condition kept |
| ch18/s18-2.tex:26 | identity. Its content is that every term | identity, and every term in it | kept | rewording; meaning, numbers and references unchanged |
| ch18/s18-2.tex:47 | is not the residual energy below threshold but the phonon energy above it. | comes from the phonon energy above threshold. | kept | negation framing -> positive statement; condition kept |
| ch18/s18-2.tex:49 | What a long run of phonons adds to $E_>$, it takes from $E_<$. | (deleted) | kept | cleft -> direct statement |
| ch18/s18-2.tex:83 | is far from this limit in two ways. Its densities of states rise as $x^{1/2}$, and phonons | differs from this limit in its densities of states, which rise as $x^{1/2}$, and in the phonons that | kept | rewording; meaning, numbers and references unchanged |
| ch18/s18-2.tex:109 | in hand. | available. | kept | rewording; meaning, numbers and references unchanged |
| ch18/s18-3.tex:3 | promises. | predicts. | kept | rewording; meaning, numbers and references unchanged |
| ch18/s18-3.tex:7 | momenta. The price is | momenta, which loses | kept | figurative word -> technical verb/noun |
| ch18/s18-3.tex:77 | price. | cost. | kept | figurative word -> technical verb/noun |
| ch18/s18-3.tex:82 | price | cost | kept | figurative word -> technical verb/noun |
| ch18/s18-3.tex:82 | the mean is wrong even on average. | even the mean is wrong. | kept | rewording; meaning, numbers and references unchanged |
| ch18/s18-3.tex:82 | never converges. | itself never approaches that of the cascade. | kept | rewording; meaning, numbers and references unchanged |
| ch18/s18-4.tex:14 | assumption. It is the reason the comparison with other crystals tests the model, and the first suspect where the comparison fails. | assumption, and the comparison with other crystals tests it. | kept | rewording; meaning, numbers and references unchanged |
| ch18/s18-4.tex:16 | sits | lies | kept | "sit" metaphor verb -> plain verb; literal position |
| ch18/s18-4.tex:41 | comparison is sharper | test is stronger | kept | rewording; meaning, numbers and references unchanged |
| ch18/s18-4.tex:56 | is not universal. | differs from crystal to crystal. | kept | negation framing -> positive statement; condition kept |
| ch18/s18-4.tex:80 | sits | lies | kept | "sit" metaphor verb -> plain verb; literal position |
| ch18/s18-4.tex:80 | linear at all~\cite[Sect.~II]{nielsen2026first}; in the model, the nonlinearity sits | linear~\cite[Sect.~II]{nielsen2026first}; in the model, the nonlinearity lies | fixed | three "lies" in three sentences; now "is below" and "comes from $k_2$" |
| ch18/s18-4.tex:118 | culprit | cause | kept | rewording; meaning, numbers and references unchanged |
| ch18/s18-4.tex:124 | outside, each for a physical reason. | outside it. | kept | rewording; meaning, numbers and references unchanged |
| ch18/s18-5.tex:7 | sits | is | kept | "sit" metaphor verb -> plain verb; literal position |
| ch18/s18-5.tex:39 | fragile: | sensitive to losses: | kept | figurative word -> technical verb/noun |
| ch18/s18-5.tex:53 | What it changes is where the energy sits: | It changes only the energy held by the pair: | kept | "sit" metaphor verb -> plain verb; literal position |
| ch18/s18-5.tex:101 | sits | lies | kept | "sit" metaphor verb -> plain verb; literal position |
| ch18/s18-5.tex:110 | take over. | dominate. | kept | metaphor verb -> "dominates" |
| ch18/s18-5.tex:121 | What is known are the binding energies, \SI{14.7}{meV} in silicon and a few meV in germanium, and | The binding energies are known, \SI{14.7}{meV} in silicon and a few meV in germanium, and so are | kept | cleft -> direct statement |
| ch18/s18-5.tex:123 | is | has | kept | rewording; meaning, numbers and references unchanged |
| ch18/s18-5.tex:123 | binding. | binding, been computed. | fixed | "Nor has the separation ..., which decides ..., been computed" needed a second reading; now "... has not been computed either" |
| ch19/s19-1.tex:7 | carries | has | kept | figurative word -> technical verb/noun |
| ch19/s19-1.tex:38 | sit | lie | kept | "sit" metaphor verb -> plain verb; literal position |
| ch19/s19-1.tex:74 | What the dynamics adds to the responseis | The dynamics adds to the response | kept | cleft -> direct statement |
| ch19/s19-1.tex:99 | natural | accuracy | kept | figurative word -> technical verb/noun |
| ch19/s19-1.tex:99 | takes over; | dominates; | kept | metaphor verb -> "dominates" |
| ch19/s19-1.tex:103 | sit | are | kept | "sit" metaphor verb -> plain verb; literal position |
| ch19/s19-1.tex:130 | sits in | is part of | kept | "sit" metaphor verb -> plain verb; literal position |
| ch19/s19-2.tex:7 | Here we can stay with a simpler question: where can the integrand be nonzero at all? | (deleted) | kept | sentence-final "at all" cut |
| ch19/s19-2.tex:66 | natural object is | excitation is instead described by | kept | figurative word -> technical verb/noun |
| ch19/s19-2.tex:71 | electrons at all. | electrons. | kept | sentence-final "at all" cut |
| ch19/s19-2.tex:80 | carries the main theory uncertainty of the charge channel, and it | holds the main theory uncertainty of the charge channel, which | kept | figurative word -> technical verb/noun |
| ch19/s19-2.tex:84 | What a charge readout recordsis | A charge readout records | kept | cleft -> direct statement |
| ch19/s19-2.tex:102 | says more. It | (deleted) | kept | deleted sentence carried no fact absent from the paragraph |
| ch19/s19-2.tex:107 | sit | lie | kept | "sit" metaphor verb -> plain verb; literal position |
| ch19/s19-2.tex:122 | therefore | (deleted) | kept | redundant "therefore" cut; inference still explicit |
| ch19/s19-2.tex:122 | carries | has | kept | figurative word -> technical verb/noun |
| ch19/s19-2.tex:122 | their boundary from the Migdal side: toward | the boundary between the two channels from the Migdal side. Toward | kept | rewording; meaning, numbers and references unchanged |
| ch19/s19-2.tex:124 | Their balance | The balance between the two channels | fixed | "between the two channels" twice in two sentences; now "between Migdal and collisional excitation" |
| ch19/s19-2.tex:124 | loses on two counts, | decreases for two reasons, | kept | rewording; meaning, numbers and references unchanged |
| ch19/s19-3.tex:26 | Lindhard's insight was | Lindhard showed | kept | figurative word -> technical verb/noun |
| ch19/s19-3.tex:84 | has least claim to hold. | is least justified. | kept | rewording; meaning, numbers and references unchanged |
| ch19/s19-3.tex:92 | at all | (deleted) | kept | sentence-final "at all" cut |
| ch19/s19-3.tex:98 | data and needs no repair. | data. | kept | rewording; meaning, numbers and references unchanged |
| ch19/s19-3.tex:124 | sits inside | is averaged with | kept | "sit" metaphor verb -> plain verb; literal position |
| ch19/s19-3.tex:147 | sit | lie | kept | "sit" metaphor verb -> plain verb; literal position |
| ch19/s19-3.tex:149 | what a track detector readsis | a track detector reads | kept | cleft -> direct statement |
| ch19/s19-5.tex:29 | sits inside | is part of | kept | "sit" metaphor verb -> plain verb; literal position |
| ch19/s19-5.tex:63 | what remains is the difference between the two kinds of recoil. | only the difference between the two kinds of recoil remains. | kept | cleft -> direct statement |
| ch19/s19-5.tex:65 | The second condition does not hold by accident. | (deleted) | kept | negation framing -> positive statement; condition kept |
| ch19/s19-5.tex:174 | sit | lie | kept | "sit" metaphor verb -> plain verb; literal position |
| ch19/s19-5.tex:187 | It is not an ionization threshold. | (deleted) | kept | negation framing -> positive statement; condition kept |
| ch19/s19-5.tex:187 | belongs to | is set by | kept | figurative word -> technical verb/noun |
| ch19/s19-5.tex:305 | does not reach | stays below | kept | negation framing -> positive statement; condition kept |
| ch19/s19-5.tex:305 | is not excluded | remains possible | kept | negation framing -> positive statement; condition kept |
| ch19/s19-5.tex:317 | Solving \cref{eq:19.5-linear} with these values returns the inputs. | (deleted) | kept | figurative word -> technical verb/noun |
| ch19/s19-5.tex:321 | Three further measurements or calculations split it. | (deleted) | kept | count-teaser cut; members named in the text |
| ch19/s19-6.tex:3 | turns | depends | kept | figurative word -> technical verb/noun |
| ch19/s19-6.tex:29 | The verdict for both defects is therefore conditional | Whether either defect releases its energy therefore depends | kept | rewording; meaning, numbers and references unchanged |
| ch19/s19-6.tex:33 | its distribution in energy and time is what a detector sees. | a detector sees its distribution in energy and time. | kept | cleft -> direct statement |
| ch19/s19-6.tex:77 | carry | depend on | kept | figurative word -> technical verb/noun |
| ch19/s19-6.tex:88 | all this | these rates | kept | rewording; meaning, numbers and references unchanged |
| ch19/s19-6.tex:97 | the idea was born, | defectons were first proposed, | kept | rewording; meaning, numbers and references unchanged |
| ch19/s19-6.tex:97 | A narrow band has a weakness. | (deleted) | kept | deleted sentence carried no fact absent from the paragraph |
| ch19/s19-6.tex:152 | sits | lies | kept | "sit" metaphor verb -> plain verb; literal position |
| ch19/s19-6.tex:154 | calculation that decides is that of the | (deleted) | kept | deleted sentence carried no fact absent from the paragraph |
| ch19/s19-6.tex:154 | vacancy, from | vacancy remain to be computed with | kept | rewording; meaning, numbers and references unchanged |
| ch19/s19-6.tex:160 | already bounds what any defect source can supply, and we can use it before choosing a | bounds what any defect source can supply, whatever the | kept | rewording; meaning, numbers and references unchanged |
| ch19/s19-6.tex:167 | Each event obeys the same bound on its own. | The same bound holds for each event separately. | kept | rewording; meaning, numbers and references unchanged |
| ch19/s19-6.tex:167 | is then a statement about elastic energy, notabout | then reflects elastic energy, not | kept | rewording; meaning, numbers and references unchanged |
| ch19/s19-6.tex:179 | A spectrum rising toward threshold as a power with an exponential cutoff is what such a cascade of elementary releases produces. | Such a cascade of elementary releases produces a spectrum that rises toward threshold as a power with an exponential cutoff. | kept | cleft -> direct statement |
| ch19/s19-6.tex:181 | sits | lies | kept | "sit" metaphor verb -> plain verb; literal position |
| ch19/s19-6.tex:187 | is not free of a heat deficit. | has a heat deficit too. | kept | negation framing -> positive statement; condition kept |
| ch19/s19-summary.tex:9 | (none) | next chapter follows to the sensors the | kept | rewording; meaning, numbers and references unchanged |
| ch19/s19-summary.tex:9 | window are not yet a signal; the next chapter follows them to the sensors. | window. | kept | negation framing -> positive statement; condition kept |
| ch20/ch20.tex:4 | the energy balance of \cref{chap:19} can be read at all. | a detector can read the energy balance of \cref{chap:19}. | kept | sentence-final "at all" cut |
| ch20/ch20.tex:4 | energy at all. Whether Luke phonons arein fact | energy. Whether Luke phonons are | kept | sentence-final "at all" cut |
| ch20/ch20.tex:4 | What the readout measures feeds | The quantities the readout measures enter | kept | cleft -> direct statement |
| ch20/s20-1.tex:3 | not the pair number $N_{\mathrm{eh}}$ of \cref{sec:18.2}but $N_{\mathrm{eh}}$ | the pair number $N_{\mathrm{eh}}$ of \cref{sec:18.2} | kept | negation framing -> positive statement; condition kept |
| ch20/s20-1.tex:7 | sits | is | kept | "sit" metaphor verb -> plain verb; literal position |
| ch20/s20-1.tex:49 | and at | At | kept | rewording; meaning, numbers and references unchanged |
| ch20/s20-1.tex:49 | is what | (deleted) | kept | cleft -> direct statement |
| ch20/s20-1.tex:88 | What trapping changesis | Trapping changes | kept | cleft -> direct statement |
| ch20/s20-1.tex:99 | is of a different kind. It | (deleted) | kept | deleted sentence carried no fact absent from the paragraph |
| ch20/s20-1.tex:127 | sits | lies | kept | "sit" metaphor verb -> plain verb; literal position |
| ch20/s20-1.tex:131 | A detector run therefore carries a history: the | The | kept | redundant "therefore" cut; inference still explicit |
| ch20/s20-1.tex:131 | (none) | therefore | kept | rewording; meaning, numbers and references unchanged |
| ch20/s20-2.tex:3 | sits | is | kept | "sit" metaphor verb -> plain verb; literal position |
| ch20/s20-2.tex:32 | Not every branch decays.In the isotropic continuum a transverse phonon cannot decay at all. | In the isotropic continuum a transverse phonon cannot decay. | kept | sentence-final "at all" cut |
| ch20/s20-2.tex:99 | says what the spectrumlooks like once it has settled, not when it settles. | gives the spectrum once it has settled. | kept | cleft -> direct statement |
| ch20/s20-2.tex:116 | How long does the birth spectrum leave a trace?We measure the trace | We measure the trace that the birth spectrum leaves | kept | rewording; meaning, numbers and references unchanged |
| ch20/s20-2.tex:125 | answer | memory time | kept | rewording; meaning, numbers and references unchanged |
| ch20/s20-2.tex:125 | What remains is the soft fraction: the | The remaining difference is the soft fraction. The | kept | cleft -> direct statement |
| ch20/s20-2.tex:136 | Sapphire does not fit this picture. Its isotope constant | The isotope constant of sapphire | kept | negation framing -> positive statement; condition kept |
| ch20/s20-2.tex:136 | silicon, however, | silicon | kept | rewording; meaning, numbers and references unchanged |
| ch20/s20-2.tex:140 | The memory of the spectrum matters through what a readout measures. | (deleted) | kept | cleft -> direct statement |
| ch20/s20-2.tex:150 | \Cref{eq:20.2-bound} names the one number that the created-phonon spectra of the two recoils must supply, | The only input that \cref{eq:20.2-bound} needs from the created-phonon spectra of the two recoils is | kept | count-teaser cut; members named in the text |
| ch20/s20-2.tex:150 | enter at all. | enter. | kept | sentence-final "at all" cut |
| ch20/s20-3.tex:50 | what matters is the transmission averaged | its transmission is the average | kept | cleft -> direct statement |
| ch20/s20-3.tex:64 | The two directions are not independent. | Reciprocity ties the two directions together. | kept | negation framing -> positive statement; condition kept |
| ch20/s20-3.tex:149 | The reason is reciprocity: in | In | kept | rewording; meaning, numbers and references unchanged |
| ch20/s20-3.tex:149 | \cref{eq:20.3-pabs,eq:20.3-recip}, | reciprocity (\cref{eq:20.3-pabs,eq:20.3-recip}), | kept | rewording; meaning, numbers and references unchanged |
| ch20/s20-4.tex:13 | Whether an arriving phonon is absorbedat all | The probability that an arriving phonon is absorbed | kept | sentence-final "at all" cut |
| ch20/s20-4.tex:28 | plays no role | is negligible | kept | rewording; meaning, numbers and references unchanged |
| ch20/s20-4.tex:45 | film at all. | film. | kept | sentence-final "at all" cut |
| ch20/s20-4.tex:81 | Two effects compete above four gaps. A | Above four gaps a | kept | count-teaser cut; members named in the text |
| ch20/s20-4.tex:81 | The second effect | Escape | kept | rewording; meaning, numbers and references unchanged |
| ch20/s20-4.tex:90 | seed, so that like is compared with like. | seed. | kept | rewording; meaning, numbers and references unchanged |
| ch20/s20-4.tex:103 | For detector phonons the energy dependence matters more than any single value. | (deleted) | kept | deleted sentence carried no fact absent from the paragraph |
| ch20/s20-4.tex:103 | (none) | energy dependence | kept | rewording; meaning, numbers and references unchanged |
| ch20/s20-4.tex:109 | What leaves the film is of three kinds. | (deleted) | kept | cleft -> direct statement |
| ch20/s20-5.tex:3 | run through | depend on | kept | rewording; meaning, numbers and references unchanged |
| ch20/s20-5.tex:28 | answer: | result. | kept | rewording; meaning, numbers and references unchanged |
| ch20/s20-5.tex:79 | is what | (deleted) | kept | cleft -> direct statement |
| ch20/s20-5.tex:90 | What survives is the soft energy, | The soft energy remains, | fixed | "The soft energy remains, the share ..." dangling appositive; split: "The soft energy remains. It is the share ..." |
| ch20/s20-summary.tex:9 | measured charge and phonon signals, with these conditions, are what the exclusion limits of the next chapter start from. | exclusion limits of the next chapter start from the measured charge and phonon signals, with these conditions. | kept | cleft -> direct statement |
| ch21/ch21.tex:4 | what remains open is indexed in \cref{chap:22}. | \cref{chap:22} indexes the open problems. | kept | cleft -> direct statement |
| ch21/s21-1.tex:27 | The galactic distribution now stands alone, | All time dependence is now in the kernel, | kept | rewording; meaning, numbers and references unchanged |
| ch21/s21-1.tex:47 | adds no freedom to this picture. | needs no halo function beyond $\eta$. | kept | rewording; meaning, numbers and references unchanged |
| ch21/s21-1.tex:90 | At the floor the rate is zero.Near $v_{\mathrm{max}}$ the halo supply | Near $v_{\mathrm{max}}$ the mean inverse speed | kept | rewording; meaning, numbers and references unchanged |
| ch21/s21-1.tex:92 | belongs to the halo and to | depends on the halo and on | kept | figurative word -> technical verb/noun |
| ch21/s21-2.tex:22 | not the optimizerthat | whatever optimizer | kept | negation framing -> positive statement; condition kept |
| ch21/s21-2.tex:33 | u)$: all of $\tilde\eta$ sits below the speed $v$, the halo of | u)$, the shape of $\tilde\eta$ for | kept | "sit" metaphor verb -> plain verb; literal position |
| ch21/s21-2.tex:44 | not an estimate, | (deleted) | kept | negation framing -> positive statement; condition kept |
| ch21/s21-2.tex:48 | opens | grows | kept | rewording; meaning, numbers and references unchanged |
| ch21/s21-2.tex:84 | sits | is | kept | "sit" metaphor verb -> plain verb; literal position |
| ch21/s21-2.tex:101 | at a price | with a correction | kept | figurative word -> technical verb/noun |
| ch21/s21-2.tex:108 | table, not the physics. | cells of the table. | reverted | "measures the cells of the table" lost the point (an artifact of tabulation, not physics); old "measures the table, not the physics" restored |
| ch21/s21-3.tex:3 | carry the halo model as much as | depend on the halo model as much as on | kept | figurative word -> technical verb/noun |
| ch21/s21-3.tex:29 | sits | lies | kept | "sit" metaphor verb -> plain verb; literal position |
| ch21/s21-3.tex:108 | model loss functionis the idealization. The computed one | computed loss function | kept | rewording; meaning, numbers and references unchanged |
| ch21/s21-3.tex:108 | halo side is never the limitation at | expansion of the halo tail holds at all | kept | rewording; meaning, numbers and references unchanged |
| ch21/s21-3.tex:123 | sit in | enter | kept | "sit" metaphor verb -> plain verb; literal position |
| ch21/s21-3.tex:123 | sit in | enter | kept | "sit" metaphor verb -> plain verb; literal position |
| ch21/s21-3.tex:131 | Two handles distinguish the target from the halo.The first is a second edge with a different mixture. | A second edge, with a different dependence on the gap and on $v_{\mathrm{max}}$, distinguishes the target from the halo. | kept | rewording; meaning, numbers and references unchanged |
| ch21/s21-3.tex:133 | second handle is time. | annual cycle distinguishes them as well. | kept | rewording; meaning, numbers and references unchanged |
| ch21/s21-3.tex:133 | sits | lies | kept | "sit" metaphor verb -> plain verb; literal position |
| ch21/s21-4.tex:21 | it is there that the theory uncertainties enter. | the theory uncertainties enter through it. | kept | rewording; meaning, numbers and references unchanged |
| ch21/s21-4.tex:30 | counts, it is not the quantity being measured, and the likelihood is profiled over it. | counts but is not the quantity being measured. | kept | negation framing -> positive statement; condition kept |
| ch21/s21-4.tex:32 | How much does a theory uncertainty cost a limit?One bin with no events and no background shows the structure. | One bin with no events and no background shows how much a theory uncertainty costs a limit. | kept | rewording; meaning, numbers and references unchanged |
| ch21/s21-4.tex:37 | price | cost of a term | kept | figurative word -> technical verb/noun |
| ch21/s21-4.tex:37 | price is below the threshold: the profile then excludes nothing at all. | term is below the threshold: the profile then excludes nothing. | kept | sentence-final "at all" cut |
| ch21/s21-4.tex:39 | value for it, not one per experiment | common value for it | kept | negation framing -> positive statement; condition kept |
| ch21/s21-4.tex:41 | calibrated, not known exactly, | known from calibrations, | kept | negation framing -> positive statement; condition kept |
| ch21/s21-4.tex:50 | together, not as independent entries. | together. | kept | negation framing -> positive statement; condition kept |
| ch21/s21-4.tex:71 | charges | gives | kept | rewording; meaning, numbers and references unchanged |
| ch21/s21-4.tex:73 | sits at | comes from | kept | "sit" metaphor verb -> plain verb; literal position |
| ch21/s21-4.tex:101 | What it costs | Its cost | kept | cleft -> direct statement |
| ch21/s21-4.tex:107 | take over: | dominate: | kept | metaphor verb -> "dominates" |
| ch21/s21-5.tex:7 | The price is that every event, background or not, | Every event, background or not, then | kept | negation framing -> positive statement; condition kept |
| ch21/s21-5.tex:16 | How much the shapebuys | The gain from the shape | kept | rewording; meaning, numbers and references unchanged |
| ch21/s21-5.tex:16 | sits | lies | kept | "sit" metaphor verb -> plain verb; literal position |
| ch21/s21-5.tex:20 | have charged | give | kept | rewording; meaning, numbers and references unchanged |
| ch21/s21-5.tex:29 | pays the constraint once for each, | counts the constraint once for each experiment, | kept | figurative word -> technical verb/noun |
| ch21/s21-5.tex:31 | parameter, not as an error of each experiment. | parameter. | kept | negation framing -> positive statement; condition kept |
| ch21/s21-5.tex:31 | choices, not uncertainties, and they are removed by the recomputation, not | removed by the recomputation rather than | kept | negation framing -> positive statement; condition kept |
| ch21/s21-5.tex:76 | carries a cost in | lowers the | kept | figurative word -> technical verb/noun |
| ch21/s21-7.tex:9 | is a statement about the documented record of a crystal,not about its physics, | records what has been documented for a crystal, | fixed | dropped contrast is one the reader needs (conditional does not mean physically worse); "not its physics" restored as a clause |
| ch21/s21-7.tex:42 | still; what the 50~mK fit leaves open is the number, not the order. | still, so the 50~mK fit affects the number and leaves the order unchanged. | kept | cleft -> direct statement |
| ch21/s21-7.tex:42 | Two further steps stand between a lead saltand a target. None | No lead salt | kept | count-teaser cut; members named in the text |
| ch21/s21-7.tex:44 | softness that wins these rows loses the | same softness gives CsI a poor | kept | metaphor verb -> "dominates" |
| ch21/s21-7.tex:44 | Once in, its lead must survive | Its lead then depends on | kept | rewording; meaning, numbers and references unchanged |
| ch21/s21-7.tex:58 | A ranking needs the inputs of a second candidate. | (deleted) | kept | deleted sentence carried no fact absent from the paragraph |
| ch21/s21-7.tex:62 | is a signal figure: it ranks rates, not the backgrounds against which they are seen. A | ranks signal rates, and a | kept | negation framing -> positive statement; condition kept |
| ch22/ch22.tex:2 | Read one at a time, they do not say where effort pays. | (deleted) | kept | negation framing -> positive statement; condition kept |
| ch22/s22-2.tex:13 | What a gap limits decides how we can use it, and the table sorts the gaps into five classes. | The table sorts the gaps into five classes by what each limits. | kept | rewording; meaning, numbers and references unchanged |
| ch22/s22-2.tex:131 | What is missing there | There the missing step | kept | cleft -> direct statement |
| ch22/s22-3.tex:7 | $\mathfrak{D}_{ab}$ at all, | $\mathfrak{D}_{ab}$, | kept | sentence-final "at all" cut |
| ch22/s22-3.tex:28 | A condensed-matter reader knows the structure from the x-ray edge, where | The x-ray edge has the same structure: | kept | rewording; meaning, numbers and references unchanged |
| ch22/s22-3.tex:62 | What a track detector or a paleo-detector readsis | A track detector or a paleo-detector reads | kept | cleft -> direct statement |
| ch22/s22-3.tex:66 | Nothing in the master formula changes for such a target. What is missing | The master formula applies to such a target unchanged; the missing input | kept | cleft -> direct statement |
| ch22/s22-3.tex:70 | sits | lies | kept | "sit" metaphor verb -> plain verb; literal position |
| ch22/s22-summary.tex:5 | sits | lies | kept | "sit" metaphor verb -> plain verb; literal position |

