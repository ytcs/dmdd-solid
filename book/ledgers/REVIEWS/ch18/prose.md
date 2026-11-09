# Ch18 prose review (style and prose, isolated)

Scope: ch18.tex (opening, map), s18-1 to s18-5, s18-summary, App. D.43 and D.44. Checked against STYLE.md, style-guide.md, prose-review.md (patterns 0-26), REGISTER.md and editor-notes.md. Line numbers are per file. The tex was not edited.

## Verdicts

| Unit | Words | Verdict | Main reasons |
|---|---|---|---|
| Chapter opening (ch18.tex) | ~420 | PASS (minor) | Concrete, motivational; one withholding phrase ("inherits something"); the measured 3.749 eV is then quoted again in 18.2 and 18.4 |
| 18.1 The carrier cascade | 4,210 | REVISE | The 50 eV cascade numbers are given three times (opener, caption, l.122); uses the uncalibrated parameter set (5.2, 1.17 eV) against 18.2-18.4; "only" at 4x the register rate; "the least" |
| 18.2 Mean energy per pair and the Fano factor | 4,090 | REVISE | Six process sentences about numerics (grid, 1e-15 checks, window stability, an erratum paragraph); two looped passages (l.13, l.32 vs Limit Check 18.2a); b_N = 0.35 stated five times in the chapter; outline tail in the opener; "Open problems" title duplicated in 18.5 |
| 18.3 Seeding and the phenomenological models | 3,450 | REVISE | l.102 restates the Limit Check 18.3a sentence; three process sentences (N_z, 2e-15, parameter-set reconciliation); "the box"; "their Eq. (8)" in prose; British "centred"; "gives" at 8x the register rate; the calibration is pointed to the wrong section |
| 18.4 Pair energies in Si, Ge and GaAs | 4,080 | REVISE | Outline in the opener; subsection 18.4.2 is a numerics cross-check with a process title and a defensive closing paragraph; grid step Eg/73 against Eg/74 in 18.2; "we could trace", "We found no"; "box" for a fit region inside a Limit Check |
| 18.5 The end of the cascade | 3,420 | PASS (minor) | One mis-punctuated display (eq:18.5-rates); title gestures; "co-workers"; E_v undefined; the last open-problems paragraph repeats 18.1 |
| Summary | 990 | REVISE | Omits the linear law and the validated range of 18.4 and the photon-seed error of 18.3 (the chapter's main dark-matter result); one process sentence |
| App. D.43 | 1,540 | PASS | Opener narrates its moves (acceptable in an appendix); l.92 checks belong here, not in 18.2 |
| App. D.44 | 1,150 | PASS | Enumerated hypotheses are genuine conditions; clean |

Lint (`lint.py --banned BANNED-TERMS.txt`): 0 blocking hits in every file. s18-1 3 LONG-SENT (2 in the fig:18-tree caption, 1 in we:18-toy); s18-2 1 TITLE (l.1, false positive: a noun phrase naming the two results) and 3 LONG-SENT (all in Limit Check captions); s18-3 0; s18-4 2 TITLE (l.1, l.110; see below for l.1; l.110 is a false positive) and 5 LONG-SENT (4 captions, 1 at l.76); s18-5 2 EQ-PUNCT (l.79-86 real, l.102-107 false positive: the sentence continues "for the fractions") and 3 LONG-SENT (keyresult l.25-30, l.55-57, l.78); summary 5 LONG-SENT (3 in table rows, false positives; l.3 and l.11 real); D-43 0; D-44 0; ch18.tex 1 LONG-SENT (map caption, acceptable). The editor-note labels (fig:18-limit-a duplicate, sec:18.2-ledger) are resolved in the current text.

## Register calibration (REGISTER.md Sects. 4, 6; per 10k words, Lin in brackets)

| | 18.1 | 18.2 | 18.3 | 18.4 | 18.5 | Summ. |
|---|---|---|---|---|---|---|
| only (11) | 40 | 24 | 38 | 20 | 23 | 30 |
| gives (7) | 26 | 22 | 55 | 39 | 21 | 71 |
| so (11) | 29 | 20 | 32 | 12 | 23 | 30 |
| therefore (3) | 10 | 12 | 9 | 7 | 6 | 0 |
| about (5) | 12 | 12 | 15 | 10 | 18 | 10 |
| however (8) | 0 | 2 | 3 | 2 | 3 | 0 |
| we will/can/see (29) | 2 | 2 | 3 | 0 | 0 | 0 |
| since (14) | 10 | 15 | 0 | 12 | 15 | 0 |
| typical(ly) (15) | 2 | 0 | 0 | 0 | 0 | 0 |

The chapter carries the book-wide tics ("gives" at 3-10x, "only" at 2-4x, "therefore" at 2-4x) and lacks the register's connectives: almost no "however", no "we can/we see", no "typical". No "thereby", "whereby", "respectively", "in order to", "i.e.", "e.g." or "one obtains" occurs. The five writers are close in voice. The differences: 18.1 and 18.3 write "random-k", 18.2 and 18.4 "random-$k$"; 18.4 writes "coworkers", 18.5 "co-workers"; 18.2/18.4 "band width", 18.3 "bandwidth"; 18.2 and 18.4 report numerical convergence in the running text, while 18.3 and 18.5 mostly keep it out. 18.5 is closest to Lin (plain verbs, physical picture first: l.3, l.39, l.53).

Calibration passages read (2-3 per section). Pass as Lin or Kahn-Lin: 18.1 l.3 and l.62 (Pauli estimate); 18.2 l.49-51 (why the phonon term is 6.7x Poisson); 18.3 l.3 and l.104; 18.4 l.66 and l.108; 18.5 l.3, l.39, l.53. Fail: 18.1 l.104, 18.2 l.30, 18.3 l.26, 18.4 l.41, 18.5 l.101. One rewrite per section is given below, marked CAL.

## Chapter opening (ch18.tex)

1. l.4 → pattern 25/18 (withholding): "The cascade also inherits something from the dark-matter interaction that started it." → "The cascade also inherits the split of energy between the electron and the hole that the dark-matter interaction made."
2. l.2, then s18-2 l.3 and s18-4 l.3 → cross-section redundancy: the Rodrigues values (3.749 ± 0.001 eV at 123 K; 0.119 ± 0.002) are quoted with citation three times. → Keep the full quotation in 18.2 l.3 (it builds the Fano argument from it); in ch18 l.2 keep "three times the gap" without the digits, or with the digits and no repeat in 18.4 l.3 ("The measured pair energy and Fano factor of silicon, 3.749 eV and 0.119 (\cref{sec:18.2}), ...").
3. l.4 → the closing orientation is two sentences (Part III, then the map). Acceptable under STYLE (one orienting sentence plus the map pointer). No change needed.

## 18.1 The carrier cascade

4. l.3, fig:18-tree caption (l.8), l.122 → pattern 26: "about 13 new electron--hole pairs ... remaining 35 eV" (opener), "13.06 ± 0.02 new pairs with a variance of 0.116 times the mean" (caption) and "A 50 eV electron makes 13.06 ± 0.02 new pairs over 4000 cascades ... variance of 0.116 times the mean" (l.122). → In l.122 delete the sentence beginning "A 50 eV electron makes"; keep "3.8 eV per pair at this energy" by moving it into the caption, and keep the new fact of l.122 ("every one of the 199 phonons ... is emitted by a carrier below 6 eV").
5. l.120, l.122, l.133, caption l.8 → editor-note ruling (one parameter set): 18.1 runs on A_AB = 5.2, E_g = 1.17 eV; 18.2-18.4 on 5.674 eV³, 1.160 eV. s18-3 l.47 then has to reconcile them ("With A_AB = 5.2 and E_g = 1.17 eV the same splits give the means quoted in \cref{sec:18.1-seed}; the calibrated constant lowers them by less than 0.03"), a process sentence. → Rerun fig:18-tree and the l.133 numbers (2.997, 2.712, 3.029; 3.6 %, 34 %, 13 %) with the calibrated set and delete the s18-3 l.47 sentence. Until then, label l.120 "A_AB = 5.2 is the value of Ramanathan and Kurinsky at 300 K; \cref{sec:18.4} recalibrates it to 5.674 eV³ at 123 K".
6. l.133 and s18-3 l.49 → cross-section repeat: "At a few pairs the distribution of the split, not only its mean, sets the count." / "At a few pairs the shape of the seed, not its mean, sets the bins." → Delete the s18-3 sentence (its paragraph already ends on the 4 eV carrier picture).
7. l.104 → CAL and "of order" tic (REGISTER Sect. 4): "The error of either is of order $\varGamma_E/\varGamma_k$ per generation, an estimate rather than a derived bound, and \cref{app:E.24} specifies the calculation that would bound it; \cref{sec:18.5} lists it among the open problems." → "We expect an error of roughly $\varGamma_E/\varGamma_k$ per generation. This is an estimate, not a bound; \cref{app:E.24} sets out the calculation that would give one."
8. l.39 → REGISTER tic "the least" (L 0.2): "At the least kinetic energy at which an electron can make a pair" → "At the threshold energy, the lowest at which an electron can make a pair".
9. l.3 → pattern 15 (anthropomorphic, negation): "Neither can forget the seed, the electron and hole that the dark matter left behind" → "Both must keep the seed, the electron and hole that the dark matter left behind".
10. l.18 → first-use definition: "$S = -2\,(1 + n_{\mathrm{B}}(\omega))\,(R - R^\dagger)/2\ii$" uses $R$ without naming it. → "... with $R$ the retarded density response of \cref{sec:8.7}, ...".
11. l.50 → count teaser (pattern 18): "only if three things match in the two calculations." → "only if the two calculations use the same Born charges, $\varepsilon_\infty$ and $\omega_L$, the same multipoles, and the same long-range cutoff." Then keep the three explanatory sentences without "The ... must be the same numbers".
12. l.62 → count teaser: "Three hypotheses make this a branching process, and each can fail." → "The cascade is a branching process if collisions are Markovian, carriers evolve independently, and every line terminates; each can fail." 
13. l.106 → the Kane attribution reads well ("as written by Kane and quoted by Kotani and van Schilfgaarde"); keep (editor note satisfied).
14. Register: "only" at 40 per 10k (Lin 11). Cut where it adds nothing: l.72 "Only the ratios of rates enter" → "The ratios of rates enter, not the rates"; l.104 "Only the first generation ... keeps" → "The first generation ... keeps"; l.39 "Energy conservation alone would let it ionize" (keep, it is contrastive).

## 18.2 Mean energy per pair and the Fano factor

15. l.3 → outline tail (pattern 18/22) and filler "turns out": "We will derive ... and split ... The random-parking limit then checks the whole construction against closed-form values, and the estimate built from the statistics of the final carriers alone turns out to fall below the full value in every case we compute." → Keep the first "We will derive" sentence; replace the last with "An exactly solvable limit, Rényi's random parking, checks the construction, and the final-state estimate of Subashiev and Luryi falls below the full value in every case."
16. l.13 → pattern 26: "The pair energy is the gap plus the heat per pair, and the Fano factor is the variance of the heat, per pair, in units of the squared gap. Every question about the fluctuations of $N_{\mathrm{eh}}$ becomes a question about how the heat fluctuates." restates eq:18.2-moments and s18-1 l.79 ("every statement about the fluctuations of N_eh is a statement about those of the heat"). → Delete both sentences.
17. l.26 → pattern 26: "One sweep upward on an energy grid solves the recursions, each step a one-dimensional convolution." repeats s18-1 l.72 and D.43 l.74. → Delete; keep "The covariance follows from the second moment of $E_< - E_>$".
18. l.28 → pattern 19 (process): the whole paragraph ("both hold to a few parts in $10^{15}$, the rounding error of the arithmetic ...") is a numerics assurance; D.43 l.92 already states the two checks. → Delete the paragraph.
19. l.30 → pattern 19 and CAL: "The grid step is $\Eg/74$, and since the sweep reads the moments at $x - \Eg$ and $x - \omega_{\mathrm{AB}}$, the grid must contain both as whole numbers of steps; we solve at the three commensurate phonon energies nearest $\omega_{\mathrm{AB}}$ and interpolate to its value." → Move to D.43 l.74 (which already states the commensurability rule). In 18.2 keep at most: "In practice the recursions are solved on a grid of step $\Eg/74$ (\cref{app:D.43})."
20. l.30 vs s18-4 l.9-14 → arrangement (definition used before it is made): 18.2 uses $A_{\mathrm{AB}} = 5.674$ "(\cref{sec:18.4})" and 18.3 l.3 says "with the constant calibrated in \cref{sec:18.2}". → Fix one home. Simplest: state the calibration here in 18.2 (one sentence, eq:18.4-AAB moved to 18.2 as eq:18.2-AAB) and let 18.3 and 18.4 point back; 18.4.1 then needs only the universality paragraph (l.14 from "Everything else").
21. l.32 and lim:18.2a (l.35) → pattern 26: the Ramanathan-Kurinsky definitions $\varepsilon(\omega)$, $F(\omega)$ "tend to constants at high energy~\cite[Eqs.~(2)--(3)]" appear in l.32 and again verbatim in the box. → In l.32 keep only the constant-term expansions and b_N, c_N; let the box carry the definitions.
22. b_N = 0.35 → stated in l.32, the lim:18.2a caption, l.160, l.164 and s18-3 l.80. → Keep l.32 and the caption; in l.160 write "The first is the constant term $b_N$, which depends on the seed (\cref{sec:18.3})"; in l.164 keep the 13 % consequence without restating 0.35.
23. l.45 last sentence → pattern 26: "A detector calibrated with X-rays at keV energies measures the limits, while a search near threshold works where the step structure dominates." repeats the box's closing sentence. → Delete.
24. l.51 → pattern 6 (false contrast): "The covariance is also not, as one might first guess, a correlation between the residual energies of sibling carriers. It is the correlation between the two kinds of heat along one line of descent." → "The covariance is the correlation between the two kinds of heat along one line of descent, not between sibling carriers."
25. l.53, l.95 (s18-4), l.81 → pattern 19: "(moment recursions on two grids, extrapolated linearly in the step)". In the worked example (l.81) a grid statement is a demonstration and may stay; in l.53 and s18-4 l.95 move it to the figure captions.
26. l.94 → pattern 19/20: a separate paragraph of errata against Subashiev and Luryi. Allowed only as one clause about the literature. → Fold into the end of we:18-parking: "(The printed values $\rho_\infty = 0.7475987$ and 0.0439766 in Ref.~\cite{subashiev2010correlation} carry misprints in the seventh and third digits.)", and delete l.94.
27. l.99 vs l.81 → citation inconsistency: $F_{\mathrm{park}}$ is cited as "\cite[Eqs.~(2), (23)]" in the Limit Check and "\cite[Eqs.~(2), (44)]" in the worked example. → Check the source and use one equation number.
28. l.160 → pattern 19: "In silicon they change by $1.3\times10^{-4}$ (in $F_{\mathrm{eh}}$) and $4\times10^{-5}$ (in $\varepsilon_{\mathrm{eh}}$) between $X = 40\Eg$ and $80\Eg$, and by as little between the windows ..." → Delete the sentence, or move it to the lim:18.2a caption.
29. l.162 and s18-5 l.119 → two subsections titled "Open problems" in one chapter (pattern 21: the title does not name the content). → Retitle 18.2.6 "Constant term and the renewal bound", or move its two questions into 18.5.4 and retitle that "Open problems of the ionization yield". Opener "Two questions about the moments themselves remain open." is a count teaser → "The constant term of the yield and the status of the renewal estimate as a lower bound are open."
30. l.62 → opener count teaser: "One limit of the cascade has an exact solution." → "Rényi's random-parking problem is the one limit of the cascade with an exact solution."
31. CAL (l.30): "A first-principles cascade replaces the two free-particle kernels by those of \cref{sec:18.1}, and \cref{app:E.24} specifies it, with the three terms of \cref{eq:18.2-decomp} reported separately." → "A first-principles cascade would replace both kernels by those of \cref{sec:18.1}; \cref{app:E.24} sets it up so that the three terms come out separately."

## 18.3 Seeding and the phenomenological models

32. l.1 → pattern 21: "Seeding and the phenomenological models" names a process and a vague class. → "Seed distributions and the step model" (or "Seeded pair-number distributions").
33. l.3 → wrong pointer: "with the constant calibrated in \cref{sec:18.2}" (the calibration is in 18.4 today). → Follow item 20.
34. l.24, l.26 → pattern 19: "Every distribution in this section uses $N_z = 32$, and none has a mean above six." and "Numerically the silicon tables below sum to one within $2\times10^{-15}$." → Delete the second; move the first to the fig:18-pn10 caption.
35. l.26 → CAL and count frame: "Normalization, the forced region and the moments follow from the recursion without computing anything." → "The recursion alone guarantees three things: the distribution is normalized, it is exactly one pair below $(1 + \theta_{\mathrm{ii}})\Eg$, and its variance splits into a cascade part and a seed part."
36. l.47 last sentence → pattern 19 (reconciliation of two parameter sets). → Delete after item 5.
37. l.74 → pattern 22: "whose rate ratio \cref{eq:18.1-randomk} is their Eq.~(8), with the ionization probability ... of their Eq.~(10)" puts source equation numbers into the prose. → "\cref{eq:18.1-randomk}~\cite[Eq.~(8)]{ramanathan2020ionization}, with the ionization probability per collision $[1 + \varGamma_{\mathrm{ph}}/\varGamma_{\mathrm{ii}}]^{-1}$~\cite[Eq.~(10)]{ramanathan2020ionization}".
38. l.80 → spelling: "centred" → "centered" (American spelling, STYLE).
39. l.99 and l.102 → pattern 26: the box sentence ("the step model is off by up to 0.86 at its first step, $\omega = \SI{4.91}{eV}$"; "Between 4.4 and 13 eV the split ... decides") is restated in l.102 ("Its distance from the cascade rises to 0.86 at its first step ..."; "The validity region of the box is thus ... In between there is none."). → Cut from l.102 the 0.86 clause and the last three sentences; keep the new facts (stays above 0.2 up to 21 eV; 0.18 for the one-sided split; the $\omega^{-1/2}$ decay).
40. l.102 → STYLE ("Never write ... limit box"): "The validity region of the box" → "The validity region of \cref{lim:18.3a}" (or delete with item 39).
41. l.104 → pattern 26: "At the two-pair threshold the error is the \SI{12}{\percent} of \cref{we:18-step5}." repeats the worked example. → Delete.
42. l.106 → pattern 24 (coined term): "Observable law of a marked event"; "marks" and "observable law" are not field terms. → Title "Pair number at the readout"; in the text "the cascade also records, besides $N_{\mathrm{eh}}$, the carrier positions, ... ($\mathfrak{m}$)" and "the distribution of the recorded quantity".
43. Register: "gives" 19 times in 3,450 words. Replace about half: l.3 "gives every event two" → "puts every event in the two-pair bin"; l.47 "gives two pairs with probability 0.413" → "yields two pairs with probability 0.413"; l.58 "gives one pair in 98 %" → "leaves one pair in 98 %".
44. l.12 vs s18-1 l.52 → the phonon-sector heat is pointed to \cref{sec:19.5} here and \cref{sec:8.7} in 18.1 for the same statement. → Use one pointer (sec:8.7, where it is established).

## 18.4 Pair energies in Si, Ge and GaAs

45. l.1 → title: the section covers seven crystals, Klein's relation and the linear law; the title names three crystals by symbol (the book writes element names in prose). → "Pair energies across crystals" or "Calibrated pair energies".
46. l.3 → pattern 18/22 (outline): "This section computes the model values ... It recovers Klein's relation as a truncation of the cascade, reduces the cascade to a linear law in the gap, and fixes the range ..." → Replace with one forward sentence that names results: "With one constant fixed in silicon, the cascade comes within 5-6 % of germanium and GaAs, explains why Klein's 14/5 slope fails for wide gaps, and reduces to $\varepsilon_{\mathrm{eh}} \approx 1.61\Eg + k_2$."
47. l.7 → pattern 19 and inconsistency: "In silicon, halving the grid step from $\Eg/73$ changes $\varepsilon_{\mathrm{eh}}$ by 0.04 % and $F_{\mathrm{eh}}$ by 0.05 %." 18.2 l.30 and every caption use $\Eg/74$. → Delete the sentence (or move to D.43 with the correct step). The previous sentence on fit windows can go to the fig:18-limit-c caption, which already states them.
48. l.16 → pattern 12 (vague quantifier): "a calculation of this kind exists for a handful of crystals" → name the number: "for six crystals (the last column of \cref{tab:18-valid})".
49. l.18-41 → pattern 19 (process) and 21: subsection "Cross-check against the Monte Carlo model" exists to confirm numerics; l.20 "which tests the numerics against an independent method", l.39 (a paragraph of slope-by-slope agreement) and l.41 ("What this agreement shows is limited ...") are aimed at a reviewer. → Keep Limit Check 18.4b (it recovers a literature formula). Retitle "Monte Carlo planes of Ramanathan and Kurinsky", cut l.39 to its first sentence plus the slope $\partial\varepsilon_{\mathrm{eh}}/\partial\Eg = 1.70$ (used in s18-5 l.74), and replace l.41 by CAL: "Of course, this only shows that two codes solve the same model; it says nothing about whether the model describes silicon, since both share the free-particle bands, the single phonon and the fitted constant."
50. l.66 last sentence and Summary l.9 → l.66 "the two together count as one prediction, not two" repeats l.41; the summary sentence "The agreement with the Ramanathan--Kurinsky Monte Carlo ... is agreement of two implementations of one model" is a third pass. → Keep l.66; drop the summary sentence.
51. l.66 → pattern 26 (cross-section): "The Fano factor of silicon is set by the variance of the phonon heat emitted above threshold and its anticorrelation with the residual heat (\cref{sec:18.2}). It is sensitive to the shape of the rate ratio within a few phonon energies of threshold" repeats s18-2 l.53. → Shorten to "As \cref{sec:18.2-silicon} showed, it is set within a few phonon energies of threshold, where the free-particle form of \cref{eq:E.13-ab} is least reliable (\cref{app:E.13})."
52. l.81 → first-use definition: "$\varepsilon = 2E_f + E_i + rE_R$ in his notation" leaves $E_f$, $E_R$, $r$ undefined. → "in his notation, with $E_f$ the mean final kinetic energy, $E_R$ the phonon energy and $r$ the number of phonons per pair".
53. l.112, l.117, l.123, fig:18-limit-c caption, l.133 → "box" for the parameter region $0.003 \le \lambda_{\mathrm{AB}} \le 100$, $0.01 \le w_{\mathrm{AB}} \le 0.1$, used inside and next to a Limit Check box ("Outside the box, the law ..."). → "fit region" throughout.
54. l.153 → pattern 19: "every measured pair energy we could trace to a named measurement" → "the measured pair energies of seven crystals besides silicon".
55. l.180 → pattern 19: "We found no measured pair energy or Fano factor for sapphire, CaWO$_4$, LiF or NaF." → "Neither the pair energy nor the Fano factor of sapphire, CaWO$_4$, LiF or NaF has been measured." (State it as a fact about the literature.)
56. CAL (l.174): "The likeliest culprit is the universal constant, since the light-atom and polar lattices that it misses most have phonon couplings unlike those of silicon, but the comparison does not prove it." passes. Keep.
57. "X, not Y" constructions cluster: l.66 "one prediction, not two", l.108 "a coincidence ..., not a vindication", l.117 "an observed fit ..., not a derivation", l.136 "agree in form, not in derivation". Keep two (l.108, l.117); recast l.136 as "The two lines have the same form for different reasons."

## 18.5 The end of the cascade

58. l.1 → pattern 21: "The end of the cascade" gestures. → "Capture and excitons" (the map caption already says "capture and excitons").
59. l.79-87 → equation punctuation: the aligned display ends "$p_{B,j}$ ," and the next sentence starts "Here $\varGamma_{FX}$ is ...". → End the display with a full stop, or keep the comma and write "where $\varGamma_{FX}$ is ...". (l.102-107: lint false positive.)
60. l.14 → first-use definition: $E_v$ appears in "a free hole $\mu_F - E_v$" without definition ($E_c$ is defined). → "a free hole $\mu_F - E_v$, with $E_v$ the valence-band edge".
61. l.87 → "co-workers" against "coworkers" in 18.4 (and "as quoted by Lo and co-workers"). → "coworkers".
62. l.74 → "an electronvolt" against "eV" elsewhere ("an eV or more" in s18-4 l.180). → "by about \SI{1}{eV}".
63. l.125 → pattern 26 (cross-section): "Impact ionization enters at first order ... without the quasiparticle residue and without the exchange ..." and "The energy-only reduction ... assumes that a carrier forgets its momentum" restate s18-1 l.35 and l.104. The new content is the 3 % and the 0.1 / one-half estimates. → Open with the new numbers: "A constant factor of 0.8 on the impact-ionization rate, the quasiparticle residue left out of \cref{eq:18.1-ii}, changes $\varepsilon_{\mathrm{eh}}$ by about 3 %, and calibration removes it ..."; drop the restated definitions.
64. CAL (l.101): "Where the gap energy ends follows from the time integrals of the occupations, $\int_0^\infty p\,\dd t = -M^{-1}p(0)$ ..." → "To see where the gap energy ends up, we integrate the occupations over time, $\int_0^\infty p\,\dd t = -M^{-1}p(0)$, ...".
65. l.46 → consistency: the worked example takes $\varepsilon_{\mathrm{eh}} = 3.75$ eV from \cref{sec:1.5} with $\Eg = 1.17$ eV at millikelvin, while tab:18-pairs gives 3.766 eV at the low-temperature gap. A sentence of the form "at the 123 K value, 3.75 eV" (or 3.77 eV) avoids mixing the two.
66. l.72 → $a_x = 4.2$ nm is restated with its pointer after s18-1 l.62. Acceptable (each with \cref{sec:4.9}); drop the value here if space is wanted.

## Summary

67. l.9 → editor note confirmed: the 18.4 paragraph omits the linear law $\varepsilon_{\mathrm{eh}} \approx 1.61\Eg + k_2$ ($k_2$ 1.2-2.5 eV, 1.87 eV for silicon) and the validated range (residuals −7 to +25 % over seven crystals; $0.007 \le \lambda_{\mathrm{AB}} \le 14$). → Add one sentence each, and cut the Monte Carlo sentence (item 50) to make room.
68. l.7 → the 18.3 paragraph omits the comparison that matters for dark matter: the photon seed stays within $d_{\mathrm{TV}} = 0.062$ of the dark-matter seed, which sizes the photon-calibration error left open in \cref{sec:8.7-handoff}, and the split decides the count between 4.4 and 13 eV. → Add: "A photon calibration seeds the cascade within $d_{\mathrm{TV}} = 0.062$ of a dark-matter kick at $q_0$, but between 4.4 and 13 eV the split of the energy, which the phenomenological models fix by rule, decides the count."
69. l.3, l.11 → long sentences (lint). l.3 "Its impact ionization is the rate ..., so that the kernel is ... and, without local fields, ...; the plasmon ..." → split at the semicolon and at "so that". l.11 "They return their binding energy as heat, which lowers ... when every pair binds, and an exciton that is never split thins ..." → split before "and an exciton".
70. l.3 → the 10 eV seed numbers (2.997, 2.712) follow the uncalibrated set; update with item 5. Table row l.26 likewise.
71. Register: "gives" 7 times in 990 words. → l.5 "reproduces", l.9 "the cascade yields", l.11 "turns ... into" (already) — vary.

## Chapter-level checks

72. Seams. Opening → 18.1: clean (the map pointer, then a 50 eV electron). 18.1 → 18.2: clean in content, but 18.2 re-quotes the measured values of the opening (item 2). 18.2 → 18.3: 18.2 ends on "Open problems", 18.3 opens on the 5 eV step model; the join works, but 18.3 credits the calibration to 18.2 (item 33). 18.3 → 18.4: 18.3 ends on readout effects (pointing to 18.5 and Ch20), 18.4 returns to high-energy moments and quotes Rodrigues a third time; a bridging clause in 18.4 l.3 ("Back at keV deposits, where the two moments suffice, ...") would mark the turn. 18.4 → 18.5: clean (halides and excitons lead into capture and excitons).
73. Arrangement: the calibrated constant is used in 18.2 and 18.3 before 18.4 derives it (item 20). The random-k model with its parameters is described in full four times (s18-1 l.106-122, s18-2 l.30, s18-3 l.38, s18-4 l.7) and in six captions. → Describe it once (18.2 l.30, with the calibration) and write "the calibrated random-k cascade of \cref{sec:18.2-heat}" elsewhere; captions keep their parameter lists (captions must stand alone).
74. Redundancy across sections: b_N = 0.35 (item 22); "at a few pairs the split, not its mean, sets the count" (item 6); the Ramanathan-Kurinsky agreement (item 50); the silicon-Fano mechanism (item 51); the first-order and momentum-memory caveats (item 63).
75. Numbers from earlier chapters (brief bullet on Ch10-16): Ch18 is not a channel comparison, and it does not restate Ch10-16. The numbers it imports from Chaps. 4, 5, 7, 8 and 12 (ε₂ = 0.224 at the plasmon, $E_x^b = 14.7$ meV, $a_x = 4.2$ nm, the 45.6 meV donor, 37.6 and 36.35 meV phonons, the 0.9 eV hole shift of we:8-pairs, the 5 meV germanium exciton) each come with a \cref pointer. Only $a_x$ and the two phonon energies appear twice, each time with the pointer. No change needed beyond item 66.
76. Captions: all stand alone except fig:18-limit-b (s18-4 l.33), "the Monte Carlo scatter of the source" and "Parameters as in the source" → "of Ramanathan and Kurinsky"; and the lim:18.2a caption's range "fitted between 30 and $60\Eg$" for b_N, c_N against the text's seed window "between $20\Eg$ and $40\Eg$" for the slopes (two windows for two fits; say so: "constant terms fitted between 30 and $60\Eg$").
77. Limit Checks: each carries the formula, a one-line citation, a comparison plot with a shaded validity region and one sentence on the breakdown; none has a Source/Chain list. Editor-note ruling on lim:18.2a (plotted against $\omega/\Eg$): from the prose side, accept; $\omega$ is the parameter that controls the approach to the limit, and the box text says so.
78. Standalone scrub and user rules: no exercises, checkpoints or reader tasks; no internal labels or campaign terms in the text (R19, SPINE, WP5 absent); citations attribute (the "as quoted by" chain is used consistently); the open problems are stated with what is missing, not left to the reader. The process sentences of items 18, 19, 25-28, 34, 36, 47, 49, 54, 55 are the one systemic failure.
79. Notation (prose side only): NOTATION.md gives $A_{\mathrm{AB}}$ in eV² ("5.2 in the source units"), while 18.1 l.120 and 18.2-18.4 use eV³. Flag to the notation pass. Upright $\Gamma$ for the gamma function (s18-1 l.116-118) is a standard exception to the zone-center rule; leave it.

## Editor-notes items concerning prose (status)

- Duplicate fig:18-limit-a: resolved (18.3 uses fig:18-limit-seed).
- Unify heat symbols (E_heat, E_<, E_>): resolved; E_np is new in 18.5 and defined there.
- Label model numbers (random-k, A_AB = 5.2, E_g = 1.17): open; see item 5 (one set, rerun 18.1) and item 36.
- Kane "as quoted by": done (s18-1 l.106).
- Summary omits the linear law: confirmed; item 67.
- "ledger" label: resolved.
- Fano decomposition book values: resolved (summary l.5 reads 0.092 + 0.291 − 0.269).
- λ_AB, w_AB re-displayed in 18.4: no longer displayed; s18-4 l.7 restates them inline with a pointer, acceptable (item 73 would shorten it further).
- b_N 0.345 vs 0.352, text 0.35: the text is consistent; repetition is the issue (item 22).
- 0911.1532 misprints: item 26 (one clause).
- Limit Check 18.2a axis: accept (item 77).
- ε_s 11.4 vs 11.7: 18.5 uses ε₀ = 11.4 "at liquid-helium temperature", consistent with the NOTATION ε₀ row; no prose change.
- Si Fano 2.5σ: the text uses 2.5σ throughout.
- Second-hand measurements "quoted by": done.
