# Chapter 21 prose review (isolated)

Scope: tex/ch21/ch21.tex, s21-1 to s21-7, s21-summary; App. D.46, D.47. Checked against STYLE.md, style-guide.md, prose-review.md (patterns 0–26), REGISTER.md, editor-notes.md. No tex edited.

## 1. Lint (lint.py --banned BANNED-TERMS.txt)

| File | Hits | Blocking | Notes |
|---|---|---|---|
| s21-1 | 0 | 0 | |
| s21-2 | 1 | 0 | LONG-SENT (Limit Check 21.2a closing sentence plus caption run-on) |
| s21-3 | 3 | 0 | EQ-PUNCT l.62 is a false positive (the period sits before `\end{aligned}`); 2 LONG-SENT (l.68 window sentence, tab:21-edge caption) |
| s21-4 | 5 | 0 | LONG-SENT: l.36, keyresult l.43, fig:21-band caption (2), tab:21-dominant caption |
| s21-5 | 2 | 0 | LONG-SENT: l.24, tab:21-recast caption |
| s21-6 | 1 | 0 | LONG-SENT: tab:21-schema caption |
| s21-7 | 20 | 0 | 2 AI-PHRASE "landscape" are the LaTeX environment (false positives); 18 LONG-SENT, 6 of them table cells; prose hits l.7 (two), l.11, l.13, l.15, l.21, l.81, l.83, l.97, l.113, l.136, l.138 |
| summary | 5 | 0 | LONG-SENT: l.7, l.15, l.17, two in tab:21-nuisances |
| D-46 | 2 | 0 | LONG-SENT l.7, l.79 |
| D-47 | 2 | 0 | LONG-SENT l.3, l.121 |

Banned terms: none. Standalone scrub: no internal labels, file names or ledger vocabulary found.

## 2. Verdicts

| Unit | Words | Verdict | Main reason |
|---|---|---|---|
| Chapter opening (ch21.tex) | 456 | REVISE | The second paragraph is a section-by-section outline |
| 21.1 Rate assembly | 2,950 | REVISE | Gesturing title; provenance in prose; floor position contradicts 21.3; duplicate E.27 pointer |
| 21.2 Halo-independent bounds | 3,740 | REVISE | Count-teasers; "any reader can check"; step model used without a caveat; union bound restated later |
| 21.3 The kinematic edge | 3,870 | REVISE | Year-average position contradicts 21.1/21.4; "contact" column undefined; u_ν undefined; 350-word paragraph |
| 21.4 Theory nuisances in a limit | 3,370 | REVISE | Restates first/second order three times; construction caveat twice; June floor misused as a halo parameter |
| 21.5 Statistics, combination and recasting | 3,680 | REVISE | Vague title; jargon subsection title; formalism narration; three statistical coefficients split from 21.4 |
| 21.6 Shared response libraries | 3,580 | PASS | Minor: teasers, one looped sentence, "The normalization follows" |
| 21.7 Next targets | 5,980 | REVISE | Coined "no reading"; ambiguous "gap"; Ch20 restated at length; defensive aside; overlong paragraphs |
| Summary | 1,750 | REVISE | Two factual slips (June escape speed; leakage condition inverted); β_k called "weight" |
| App. D.46 | 1,740 | PASS | Abstract opener only |
| App. D.47 | 930 | PASS | Math typo l.150 |

## 3. Issues (location → problem → fix)

### Chapter opening
1. ch21.tex l.4 → Outline paragraph (STYLE "never a section-by-section list"; pattern 18 abstract frame): "This chapter turns the rates of the previous chapters into such limits. It asks how the halo enters a rate, … It then asks how … Finally it returns to the question …" → Replace with one orienting sentence: "Turning a zero into a trustworthy, reusable limit, and the limits into a choice of the next target, takes the steps of \cref{fig:21-map}; what remains open is indexed in \cref{chap:22}." Fold the clause on the four guide inputs into 21.7, where it already appears (l.3).
2. ch21.tex l.2 → Pattern 25 (negation): "The velocity distribution of the halo is not measured in any laboratory" → "The velocity distribution of the halo is known only from models and stellar kinematics". A mild aphorism, "The prediction, however, carries choices that the count does not.", is acceptable.

### 21.1
3. Title → Gesturing (pattern 21): "Rate assembly" does not predict the central result (the rate is linear in f_χ) → "The rate as a functional of the halo".
4. l.54 → Provenance in prose and a hard-coded source appendix (patterns 20, 22): "Eqs.~(3.13) and (3.17) of Essig et al.~\cite{essig2016direct} divided by the target mass. … which the same reference gives in its Appendix~B" → "…is the rate of \cref{lim:10.1a}, divided by the target mass~\cite[Eqs.~(3.13), (3.17)]{essig2016direct}. In the standard halo η is the closed form of \cref{app:D.1}~\cite[App.~B]{essig2016direct}."
5. l.86 → Count-teaser (pattern 18): "that value is a floor, never the edge of a limit, for three reasons." → "…is a floor, never the edge of a limit: a real onset depends on q, the rate vanishes at the floor, and the floor moves with the halo."
6. l.92 → Process artifact (pattern 19) and contradiction with 21.3 l.131 (editor note "one position"): "That shift is part of the halo uncertainty of the limit, not a change in the definition of the floor" defends against a past dispute. 21.3 instead concludes that "the exposure average … is the one that belongs to a limit", which puts an exposure's edge at the June value. → One position: "An exposure that includes June has its edge at the June value (\cref{sec:21.3-degeneracy}); the floor at $v_{\mathrm{max}}$ of the reference speed is the convention for comparing targets." Apply the same change to 21.4 l.34 (item 24) and to summary l.3.
7. l.45 → Low content (pattern 0): "The two forms say the same thing in different variables." → Delete. The next sentence carries the content.
8. l.52 → Filler and a loop (patterns 17, 26): "In kernel language nothing changes at all: $\varGamma(v)$ simply contains the extra terms" plus the closing "every velocity-dependent coupling probes the same function of the halo, η, that the density does", which repeats the paragraph's first sentence ("adds no freedom") → "In the kernel form $\varGamma(v)$ contains the extra terms, and \cref{eq:21.1-functional} holds as written." Drop the last sentence.
9. l.74 → Throat-clearing (pattern 1): "The numbers behind the box are these." → Delete; start "At $\vmin = 0$ the yearly average is 0.9965 of the closed form…".
10. l.76 last sentence → Redundant with 21.2 l.97 and 21.6 l.21 (the E.16/E.27 pointer for direction-resolved kernels, given three times) → Cut it here; keep 21.2's.
11. l.47 → Symbol not defined in the chapter: "at $\Delta_\chi = 0$" → "at zero mass splitting, $\Delta_\chi = 0$ (\cref{sec:8.1})".
12. l.88 → Low content: "Silicon shows the size." → "In silicon the difference is 25 percent:" (gap floor 0.3332 against zero-phonon onset 0.405 MeV), or delete.

### 21.2
13. l.15 → Count-teaser: "Three choices cover the uses. The first is … The second is … The third is …" → "The quantity to bound is a second linear functional: the mean inverse speed above u_0, …; the count of a second experiment, …; or a modulation amplitude, …".
14. l.22 → Recap opener and count-teaser: "Its two properties that matter here were derived in \cref{app:C.12}." → "By \cref{app:C.12}, any vector λ ≥ 0 with …".
15. l.44 → Count-teaser: "Two conditions are easy to break." → "The closed form fails if a column decreases somewhere … or if the kernel and the objective use different speeds."
16. l.48 → Pattern 25 (figurative): "The gap between the curves is what the halo model was worth." → "The ratio of the bound to the standard curve is the cost of dropping the halo model."
17. l.68 → Addresses the reader and leaves a step to the reader (user rule): "any reader can check that on the column without solving anything" → "the check needs the column alone, not the program."
18. l.46 → Editor note (step model against Ch18): the examples use the step model (1.11 eV, 3.6 eV per pair), while 21.7 l.83 states that the cascade puts about ten times fewer events in the two-pair bin at 5 eV → Add one clause at first use: "the step model of \cref{sec:1.5}, a simplification of the cascade of \cref{sec:18.3} that overcounts the two-pair bin near threshold". The same applies to 21.5 l.34.
19. l.106 → Nominalized (register): "The second term converts the violation into the most halo mass that the bounds allow there." → "The second term is the violation times the largest halo mass the bins still allow on the support of f."
20. Limit Check 21.2a title → The title names a directional bound, but the boxed formula is the speed-only one → "Speed-only bound against a directional response".
21. l.33 → Symbol not defined in the chapter: $M_{\mathrm{cell}}$ → "with $M_{\mathrm{cell}}$ the mass of the unit cell".

### 21.3
22. l.29 → Count-teaser and an opaque reference: "Two cases change the half." → "The ½ becomes 1 when $x_{\mathrm{max}}(q)$ has a corner at its maximum:".
23. l.72, l.121 → $u_\nu$ is not defined in the chapter → "with $u_\nu$ the phonon velocity term of \cref{eq:13.1-mPA}".
24. l.131 → One 350-word paragraph that holds two handles plus the year average, and the conflict of item 6: "Near the edge a limit computed at a fixed Earth speed is therefore a statement about that day" → Split at "The second handle is time." and align the closing with item 6.
25. l.87 → Ambiguous: "The Coulomb attraction lowers the onset of a continuum at fixed q by one half, from x^{1/2} to a step" → "lowers the onset exponent … by one half".
26. tab:21-edge → The caption does not stand alone: column "contact" (smooth/corner) is undefined → Rename the column "$x_{\mathrm{max}}$ at $q^*$" and add to the caption "smooth or corner maximum of $x_{\mathrm{max}}(q)$ (\cref{eq:21.3-power})".
27. l.7 → Dangling modifier: "Generalizing the definition of \cref{sec:13.3} … the response rises above it as $x^{p_{\mathrm{on}}}$" → "We generalize the definition of \cref{sec:13.3} to any channel: the response rises…".

### 21.4
28. l.34 → Wrong example and conflict (item 6): "varied in a band of their own: the June floor lies 3.9 % below the reference one" (the June shift is an Earth-speed effect of the exposure, not a halo-parameter variation) → "…varied in a band of their own, the ±25 km/s of $v_{\mathrm{esc}}$ and ±6 km/s of $v_0$ of \cref{sec:1.2}."
29. l.55 → Looped restatement (pattern 26): "The band is of first order in the templates and the profiled limit of second." This is already said in the opener (l.3) and in eq:21.4-profile → Delete.
30. l.19 and l.57 → The same caveat twice: "a published limit must say which construction it used" / "a published limit must say which construction it reports" → Keep l.57 only.
31. l.57 and 21.5 l.44 → Editor note (one statistical construction): three k² coefficients (1.15, 0.65, 2.30) are split across two sections → Give all three in 21.4 l.57, stating that the fixed-best-fit profile (2.30) is the most conservative. In 21.5 keep only "a cost of 1.12, the coefficient $N_{90}$ of \cref{sec:21.4-like}".
32. l.3 → A rhetorical question (pattern 8; mild): "Which number should the experiment publish, and how wide is the uncertainty on it?" → Acceptable as a genuine question; optionally "The experiment has to choose one number and state its uncertainty."
33. l.97 → Count-teaser: "Two kinds of row stand out. Some are missing calculations. … Others are missing data" → "The dominant rows are missing calculations (…) or missing data (…)."
34. tab:21-dominant row 1 → The pointer misattributes a number: "×3.2 at 1 MeV … \cref{sec:10.10}" (10.10 quotes 3 and 10 MeV only; editor note) → Point the 1 MeV value to \cref{fig:21-band} alone.
35. l.21, l.104 (caption) → "cross-section limit" here, but "cross section" 12 times elsewhere in the chapter, against the book's "cross-section" (119 against 22) → Use "cross-section" chapter-wide.

### 21.5
36. Title → Vague, a list of three nouns: "Statistics, combination and recasting" → "Combining and recasting limits".
37. sec:21.5-corrected title → Jargon: "Dirac re-plots and boosted fluxes" → "Recasts for Dirac materials and boosted fluxes".
38. l.14 → Translated-from-formalism prose (register): "The $k = 1$ term … is then $-\ee^{-N_{\mathrm{sig}}}$, written as $(kx - N_{\mathrm{sig}})^k - k(kx - N_{\mathrm{sig}})^{k-1}$ times $\ee^{-kx}/k!$" → "At $g = 1$ only $k = 0, 1$ contribute, the $k = 1$ term is $-\ee^{-N_{\mathrm{sig}}}$, and $C_0 = 1 - \ee^{-N_{\mathrm{sig}}}$ recovers $N_{90}$."
39. l.18 → Forbidden construction (REGISTER §4): "For the observed events one evaluates $C_n$" → "we evaluate".
40. l.31 → Count-teaser and mixed ordinals: "Three steps come before the product. The signal … is first recomputed … Second, … Third, …" → "Before the product, the signal of every experiment is recomputed …; one set of halo parameters acts on all factors; and searches in different materials share …".
41. l.76 → Restates 21.2 l.24 (union bound, ln 30 = 3.401) → Keep the new fact (coverage 0.9ⁿ) and point: "…the union-bound correction of \cref{sec:21.2-program} restores it."
42. l.102 → Self-narrating pointer placed before the last subsection: "What the response side must provide is the subject of \cref{sec:21.6}." → Move it to the end of 21.5 (after the boosted flux) as a closing pointer, or drop it.
43. l.9 → Anthropomorphic/elliptic: "The shape of the expected signal does better." → "Using the shape of the expected signal gives a stronger limit."
44. l.117, l.106 → Symbols not defined in the chapter: $\mathcal{Q}$, $\varepsilon_{\mathrm{D}}$ → Add "with $\mathcal{Q}$ the four-momentum transfer of \cref{eq:10.9-Drel}" and "$\varepsilon_{\mathrm{D}}$ the Dirac polarization (\cref{sec:16.1})".
45. eq:21.5-K → Editor note: $\mathcal{K}_j$ clashes with 14.6's $\mathcal{K}_t$ (and the label component $\mathcal{K}$ in 21.6 l.70) → Rename it (for example $\mathcal{C}_j$, recast factor) and add it to NOTATION.

### 21.6
46. l.49 → Low content and ambiguous: "The normalization follows." → "Next comes the normalization."
47. l.17 → Loop (pattern 26): "With these three owners the chain … is assembled from published tables only: material tables up to the marks …, the detector response …, and the halo outside both." This repeats the two preceding sentences → Cut it after "…contracts it with the kernel in \cref{eq:21.1-functional}."
48. l.15, l.53 → Count-teasers: "Two choices fix the weights and are part of the table." / "Two of them need a separate entry each." → Name them: "The weights are retarded, and the sector split follows one declared convention; both are part of the table." / "The scissor gap and the pair-conversion gap need separate entries:".
49. l.3 → A Ch10 number repeated (brief): "two tabulations … differ by a third (\cref{sec:10.10})" also appears in 21.5 l.31 and in tab:21-dominant → Keep it here as motivation; in 21.5 write "the tabulation spread of \cref{sec:21.4}".
50. l.59 → Editor note: the release tolerances ($-10^{-6}$ of the trace; KK below 1 %) are stated as the book's rule without a source in App. E → Either add them to the relevant section of \cref{app:E} and point there, or phrase them as an example ("for instance, …").

### 21.7
51. l.81, l.57 (table), summary l.15 → Invented vocabulary (pattern 24): "no reading", "without giving the row a reading" → "no resolved leader" (the field's term; the section already uses "No full-pool leader is resolved").
52. l.89 and l.134 → "gap" is ambiguous in a section about band gaps: "The deciding gap is a band with no target" / "Three gaps limit the guide." → "The deciding hole in coverage is a band with no target" / "Three missing inputs limit the guide: the loss functions of the survivors, measured elastic constants, and internal-background rates." (The last version also removes the count-teaser.)
53. l.3 → Defensive aside (patterns 6, 19): "Neither crystal family was in that pool, and not by oversight." → "Neither family was in that pool, for documented reasons:".
54. l.3, l.7, l.9 → Said three times (pattern 26): "Current capability enters it as a column, never as a filter." / "Only positive evidence removes a crystal from the full pool." / "They select no crystal out of the ranking." → Keep l.3 and l.7; delete the l.9 sentence.
55. l.7 → Sentence length: the four requirements form one 80-word sentence, and the paragraph is about 400 words → Itemize the four conditions (a genuine enumeration, which style-guide allows) or give them as four sentences; start a new paragraph at "The survivor pool is the eleven crystals".
56. l.15 → Low content (pattern 0): "Germanium needs a word." → "Germanium has no pair energy measured directly at millikelvin temperatures."
57. l.83 → Restates Ch20 at length (brief: Ch21 must not restate home chapters): "mode, frequency or angle selection … cannot separate … A high-voltage readout … cannot separate … The collection ratio of Luke phonons lies between 0.81 and 1.02 … All of these verdicts assume transport that has not yet been validated." → Reduce to one sentence plus pointer: "By \cref{sec:20.5}, the recoil type is read from the charge, not from the phonons, in silicon and germanium." Keep the consequences for the guide (charge readout through $P(N_{\mathrm{eh}})$, ten times fewer two-pair events than the step model; phonon rows through collection; quasiparticle yield).
58. l.77 → Unclear: "it costs CsI nothing in data quality" / "The nuclear edge reverses the order of stiffness" → "and it rests on measured constants" / "In the nuclear edge the stiffest crystals lead:".
59. l.129 → Process artifact (implies history): "CsI's rank … no longer hinges on an input" → "does not hinge on a computed input".
60. eq:21.7-pb210 (l.106) → Equation punctuation: the display ends with "," and the next text starts a new sentence ("Of these, 605.6 …") → End the display with ".".
61. fig:21-leaders caption → Stacked negation (pattern 25): "below it no material is more likely than not to lead" → "below it the leader has less than even odds".
62. l.75 → Symbol not defined in the chapter: "phonon strengths, $\lambda_{\mathrm{AB}}$ from 230 to 1160" → Add "(\cref{sec:18.4-range})" at first use and give its meaning in a clause.
63. Capability column and l.7 → Editor note: capability statuses carry no citations (h-BN "crystals below 0.1 g", lead salts "mK, mass and readout not shown", YIG "millimeter spheres") → Cite a public source for each positive statement. Where a statement is an absence of record, phrase it as "not reported" in the table key, so that no uncited claim stands as fact.
64. Subsection titles → "Two pools and the capability column" names a table device; "Absorption, magnons, superconductors and special targets" is a four-item list → "Candidate pools and detector readiness"; "Absorption and unranked channels".
65. l.113 → "Klein--Nishina cross-section" is hyphenated while the chapter elsewhere writes "cross section" (see item 35).

### Summary
66. tab:21-nuisances "Halo of the floor" row → Factual slip: "June escape speed lowers the floor by 3.9 %" (it is the Earth speed: $v_{\mathrm{esc}} + |\vect{v}_{\mathrm{E}}|$ = 810.4 km/s) → "June Earth speed lowers the floor by 3.9 %". Rename the row "Earth speed at the floor".
67. l.5 → Inverted condition: "a final-state assignment that is not stochastically ordered leaks at most 0.034 of a bin" (21.2 l.110 requires the pair number to grow stochastically) → "the zero-phonon/phonon-dressed split misassigns at most 0.034 of a silicon bin, provided the pair number grows stochastically with the seed energy".
68. l.9 → Terminology clash: "Each nuisance acts on the limit through its weight $\beta_k$" (21.4 calls β_k the sensitivity, and $a_j$ the weights) → "through its sensitivity $\beta_k$"; and "$e^{\pm\sigma_\beta}$" → `\ee`.
69. l.3, l.5, tab rows → House forms: "non-negative" (book 32:7 "nonnegative"); `\SI{..}{km/s}` (book: `km.s^{-1}`, which Ch21's sections use) → Conform.
70. tab:21-nuisances "Statistical construction" row → Omits 21.5's fixed-best-fit construction (coefficient 2.30, cost 1.12 for δ = 0.25) → Add it; recheck after the ruling of item 31 (editor note).
71. l.5 → "semi-infinite" first appears in the chapter in the summary (it is defined in App. C.12) → Use it in 21.2 l.3 ("a semi-infinite linear program, the problem of \cref{app:C.12}") or drop it here.

### Appendices
72. D.46 l.3 → Abstract opener (pattern 18): "This appendix derives the stream kernel …" → Open with the object: "A single stream at galactic velocity $\vect{w}$ leaves in bin $i$ the count $\mathsf{k}_i(\vect{w})$; here we derive it, its multipole form \cref{eq:21.2-multipole}, and …".
73. D.47 l.150 → Math typo: "$\mathsf{t}' = 2N^{\mathrm{up}}$ $= 2.61$" → "$\mathsf{t}' = 2N^{\mathrm{up}} = 2.61$".
74. D.47 l.3 → Mild metaphor: "the profile likelihood … charges for that motion" → "the profile likelihood … penalizes it through the constraint terms".

## 4. Chapter-level checks

**Opening outline.** Item 1. Para 1 is a model motivational opener: a concrete zero count, three named choices with numbers, and the stakes. Para 2 must shrink to one orienting sentence. The map (fig:21-map) has 8 nodes, is referred to once and carries no new numbers, as STYLE requires.

**Summary.** It recaps one paragraph per section, ends with the Ch22 pointer, and its table is complete except item 70. Fix items 66–71. It introduces nothing new apart from "semi-infinite" (item 71).

**Redundancy across sections.**
- Union bound: 21.2 l.24, 21.4 l.21 and 21.5 l.76. Keep 21.2 (item 41).
- E.16/E.27 pointer for direction-resolved kernels: 21.1 l.76, 21.2 l.97 and 21.6 l.21. Keep 21.2 and 21.6 (item 10).
- Tabulation spread "a third": 21.5 l.31 and 21.6 l.3 (item 49).
- First/second order of band and profile: 21.4 l.3, l.55 and D.47 (item 29).
- Statistical-construction coefficients: 21.4 l.57 and 21.5 l.44 (item 31).
- Capability column "never a filter": three times in 21.7 (item 54). The June 3.9 % appears in 21.1, 21.3, 21.4 and twice in the summary, with two incompatible readings (items 6, 24, 28).
- Repeated 0.034 leakage and ×231 gap shift: each repeat carries a pointer and is acceptable.

**Seams.**
- Opening→21.1: smooth. 21.1→21.2: smooth. The debris flow leaves the threshold at the standard floor; 21.2 opens on the fastest dark matter.
- 21.2→21.3: 21.2 ends on a leakage nuisance pointing to 21.4, which skips 21.3. The real link (21.2 l.48, "weakest exactly where a limit near its kinematic edge draws its events") sits mid-section. Either end 21.2-leak with "…\cref{sec:21.4} carries it into the band", and open 21.3 with a clause that picks up l.48, or accept.
- 21.3→21.4: acceptable. 21.4 opens on a new concrete limit and reuses the degeneracy at l.34.
- 21.4→21.5: good. 21.5 l.3 names the failure of 21.4's known-background limit.
- 21.5→21.6: the pointer to 21.6 is buried before the last subsection (item 42).
- 21.6→21.7: good (21.6 l.61 names the guide's inputs). 21.7→Summary: fine.

**Channel comparison (brief items).** Comparisons are well motivated (21.4-dominant: "which nuisance sets the band"; 21.7 opener: what a ranking cannot answer). Home chapters are not restated at length, except Ch20 in 21.7 l.83 (item 57). Ch10–16 numbers are given with pointers. Repeats in prose: the tabulation spread (item 49) and the 1 MeV ×3.2 pointer (item 34). Repeats in tab:21-dominant and tab:21-guide are acceptable as tables. Silicon remains the running example throughout.

**Lists, titles, citations, cross-references.**
- No bullet lists stand in for argument. The only list-like prose is 21.6 (a specification, acceptable) and the four requirements (item 55).
- All titles are noun phrases with no colons. Rename the titles in items 3, 36, 37 and 64.
- Citations use numeric `\cite[Eq.~…]` with the content stated in the book (the Lisanti family, the Kuhlen shell, the Yellin C_0 and the Feldman–Cousins ordering are all written out). The one exception is item 4.
- Cross-references are all `\cref`. No hard-coded book numbers.
- Equation punctuation: correct except item 60. No exercises, checkpoints or tasks for the reader. Item 17 is the one reader-directed phrase.

**Limit Checks.** 21.1a and 21.2a are self-contained: formula, one source citation, comparison plot with the validity region shaded, one closing sentence on breakdown. Neither has a procedure list. Item 20 (21.2a title).

## 5. Pattern 25 sweep (openers and captions, sentence by sentence)
- Chapter opening: one hit (item 2).
- Section openers 21.1–21.7: 21.1 "Simulated galaxies hold dark matter that this distribution does not describe" (mild negation; optional "…hold components outside this distribution"); 21.7 "and not by oversight" (item 53). 21.2–21.6 are clean.
- Captions: fig:21-leaders one hit (item 61); tab:21-guide "it is not the probability that a crystal is the better target" is a needed clarification, keep; clean: fig:21-map, limit21_1a, fig:21-kernel, fig:21-hib, limit21_2a, tab:21-edge, fig:21-edge, fig:21-band, tab:21-dominant, tab:21-recast, fig:21-dirac-recast, tab:21-schema, tab:21-nuisances.

## 6. Pattern 26 (new facts per paragraph)
Notation: Pn = paragraph n; ∅ = no new fact.
- **Opening:** P1 zero count, 2.3 events, screening ×2, PA ×10, the three choices. P2 ∅ beyond the four guide inputs, which 21.7 l.3 repeats (item 1).
- **21.1:**
  - P1 1.60e5; VL2 22 %, 340 km/s. P2 eq:21.1-functional. P3 linearity, the absorption analog. P4 kernel ≥ 0, v_on, exposure average.
  - P5 absorption kernel. P6 eq:gammav. P7 η form; last sentences restate (item 7). P8 η₂, the quartic term; closing sentence ∅ (item 8).
  - P9 Essig link, annual δv_E. P10 convexity near the end. Box. P11 ratios 0.9965…1.78, escape cut ×1.18–6.8, +0.8/+4.3 %. P12 kernel values; last sentence repeats 21.2 (item 10).
  - Floor P1–P4 new (q-onset numbers; June 0.3202; flow floor 0.6031). Debris P1 shell distribution. WE all new.
- **21.2:**
  - Opener and program paragraphs new. Literature paragraph new (attribution). Union-bound paragraph new; later restated (item 41).
  - Iso: P1 column; keyresult; P2 proof, Fox–Liu–Weiner, failure modes; P3 fig numbers; P4 2.22/3.52, 9.1/63.
  - WE new. Dir: P1–P3 new; daily paragraph new. Leak P1–P3 new.
- **21.3:** Every paragraph adds a fact (powers, lens, King 4.7e-6, beta function, 0.70/0.74, exponent counting, 3.5 meV per 0.001 MeV, degeneracy numbers, 0.54/−1.62, ×62). None is empty.
- **21.4:**
  - Poisson P1–P3 new. Nuisances P1–P3 new. P4 new except the June example (item 28). Keyresult.
  - P after box: the first sentence is ∅ (item 29); the rest is new (1.195 against 1.179; t' = 2.61). Coefficient paragraph new (0.65; 1.103).
  - Fig paragraph new. WE new. One-sided, excluded cells, dominant: new. Closing 1.11: new.
- **21.5:** All paragraphs add facts. l.76 is partly a repeat (item 41).
- **21.6:** All paragraphs add facts, except the last sentence of l.17 (item 47).
- **21.7:** l.9 last sentence ∅ (item 54). l.83 mostly repeats Ch20 (item 57). All other paragraphs carry new numbers.
- **Summary:** sanctioned recap.
- **D.46/D.47:** no loops.

## 7. Register (REGISTER.md)
**Word frequencies.** Chapter prose, about 27k words after math is stripped; counts per 10k words, with Lin's rate in brackets:

| Word or phrase | Chapter | Lin | Verdict |
|---|---|---|---|
| "only" | 38 | 11 | 3.5× high |
| "gives" | 19.5 | 7 | high |
| "so" | 21 | 11 | high |
| "therefore" | 8.1 | 2.9 | high |
| "however" | 2.2 | 8 | low |
| "we will / can / see / have / find" | 1.8 | ≈40 | low |
| "typical(ly)" | 0.4 | 15 | low |
| "since" | 9.9 | 13.9 | near |
| "note that", "of course" | 0 | — | absent |
| "thereby", "whereby", "respectively", "in order to", "i.e.", "e.g." | 0 | — | clean |

Revisers should:
- cut "only" where it does not restrict (for example 21.2 l.97 "varies by … only", 21.6 l.7 "in two places only");
- swap some "gives" for "is" or "leads to", and some "therefore" for "since" clauses;
- add "typical" or "∼" hedges in the estimate sentences (21.3 l.3, 21.7 l.95);
- use "however" for the real contrasts (21.4 l.59, 21.7 l.77).

**Terms of art.** Correct usage: heavy and light mediator, momentum transfer, reach, exposure, kinematically allowed, background-free, phonon-assisted, Migdal effect, loss function, minimum velocity. The coinage to remove is "no reading" (item 51). "Truncation label" is the book's own defined term. Bare "transfer" appears only as "energy transfer ω_e" (21.6 l.51), which is fine.

**Calibration (2–3 passages per section; would Lin write it?).** Each line gives the passages checked, then one sentence rewritten as Lin would.
- **21.1:**
  - Checked: l.3 ("the recomputation is cheap because every rate … is linear") yes; l.76 ("The heavier the particle, the flatter the kernel…") yes; l.45 no.
  - Rewrite: "The two forms are of course the same integral: one asks how much response a particle of speed v can reach, the other what fraction of the halo is fast enough for a given pair."
- **21.2:**
  - Checked: l.22 ("The extremal halos are therefore cold streams, far from any equilibrium model") yes; l.106 no (item 19).
  - Rewrite: "Note that the extremal halos are cold streams, nothing like an equilibrium model, and the bound holds for every halo because it holds for them."
- **21.3:**
  - Checked: l.83 ("their exponents add because the rate is a convolution") yes; l.29 and l.87 no.
  - Rewrite: "There are two exceptions to the one half."
- **21.4:**
  - Checked: l.12 ("The background lowers the limit even though nothing was seen") yes; l.32 (row taxonomy) borderline; l.55 no.
  - Rewrite: "To this order, however many nuisances there are, they act like a single one of width σ_β."
- **21.5:**
  - Checked: l.7 ("The price is that every event, background or not, weakens the limit") yes; l.14 no (item 38).
  - Rewrite: "We can do better by using the shape of the expected signal."
- **21.6:**
  - Checked: l.17 ("The library ends there.") yes; l.47 yes; l.49 no.
  - Rewrite: "Next comes the normalization, the most common source of factors of 2π and 4π."
- **21.7:**
  - Checked: l.79 ("Silicon leads no row, because…") yes; l.15 and l.83 no.
  - Rewrite: "Germanium is a special case, since nobody has measured its pair energy directly at millikelvin temperatures."

## 8. Editor-notes items that concern prose
| Note | Status in the text | Item |
|---|---|---|
| 21.1 floor/SPINE | Text accepts the refined floor; the defensive clause remains | 6 |
| 21.3 "one position" (floor against year average) | Open; conflict between 21.1 l.92, 21.3 l.131 and 21.4 l.34 | 6, 24, 28 |
| 21.2/21.5 step model against Ch18 | Open; caveat missing at first use | 18 |
| 21.3 comparison halos at v0 = 238 | Done (fig:21-edge caption) | — |
| 21.5/21.4 one statistical construction | Open | 31, 70 |
| 21.5 $\mathcal{K}_j$ against $\mathcal{K}_t$ | Open | 45 |
| 21.4 ×3.2 at 1 MeV new | Pointer should go to the figure | 34 |
| 21.4 attraction template zeroed above 10.5 eV; 10 % efficiency illustrative | Stated in caption and WE ("Suppose") | — |
| 21.6 release tolerances; patch/major rule | Tolerances need an App. E home; rule reads as a book rule (fine) | 50 |
| 21.6 scissor of 10.10 | Ch21 text consistent with the source; fix belongs to 10.10 | — |
| 21.7 capability statuses uncited | Open | 63 |
| 21.7 recheck summary after ruling | Open | 70 |
| E.27 symbols, SPINE/Ch22 updates, rebuild | Not prose | — |
