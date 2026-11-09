# Ch22 prose review (style and prose, isolated)

Files: tex/ch22/ch22.tex (opening), s22-1.tex, s22-2.tex, s22-3.tex, s22-summary.tex. Line numbers are file lines.
Against: STYLE.md, style-guide.md, prose-review.md (patterns 0–26), REGISTER.md, editor-notes.md.

## Verdicts

| Unit | Verdict | Main reasons |
|---|---|---|
| Opening (ch22.tex) | REVISE | 2nd paragraph is a section outline; process-artifact clause |
| 22.1 Calculations specified but not done | REVISE | 22.1-checks restates home sum rules at length; repeated numbers; count-teaser and aphoristic close; register flat |
| 22.2 Exact gaps in the theory | REVISE | loop after keyresult; "home" label; withholding opener; number-word mixing; empty opener l.154 |
| 22.3 Channels outside the framework | REVISE (light) | "four classes" vs six rows; anthropomorphic "knows nothing"; looped close of 22.3-cc; f-sum typography |
| Summary | REVISE | missing-step counts contradict 22.2 (53/11/8 vs 55/11/6); omits 22.1's priority result; self-narrating first sentence |

No REWRITE: voice is consistent across the three writers (same flat declarative register, same "home"/"index" vocabulary), and every section carries concrete content. The problems are local and listed below.

## 1. Lint (lint.py --banned BANNED-TERMS.txt), 0 blocking

- s22-1.tex: 5 LONG-SENT. Two are table artifacts (tab:22-calc caption/header). Three are real prose: l.7 ("An exact relation holds for every Hamiltonian ..."), fig:22-limits caption ("The classes are read from ..."), l.122 ("The background tensor of ZrTe$_5$ ..."), l.124 ("They are the cold absorption edge ..."). Fixes in Sect. 3.
- s22-2.tex: 2 AI-PHRASE "landscape" (l.23, l.152) are the `landscape` environment: false positive. 14 LONG-SENT are table rows: false positives.
- s22-3.tex: EQ-PUNCT at l.58 is a false positive (eq:22.3-fermi ends "... ,"; lint misreads `gathered`). LONG-SENT on tab:22-scope header (artifact) and l.57 (real; fix in Sect. 3).
- s22-summary.tex: clean.

## 2. Editor-notes items that concern prose

- 22.3/Summary Q4 (recheck summary against final 22.1): NOT done. Summary l.5 gives "a specified calculation in 53 of them, a measurement in 11 and a proof or method in 8"; s22-2 l.19 gives 55 / 11 / 6. One is wrong; the derivation reviewer should recount the "Missing step" column, then both files must agree. Summary l.3 also omits 22.1's actual conclusion (the four calculations and five measurements of s22-1 l.124, and the 11/10/2 split of l.120); it spends its sentences on the sum-rule inventory instead.
- 22.3 Q2 (Dror Eq. 4.10): s22-3 l.65 states it as a fact about the printed formula, as ruled. Two sentences with a derived factor; acceptable under pattern 19, but can be one clause: "Equation (4.10) of that reference prints the prefactor $2(1+\gamma_{\mathrm d})$ and $\Gamma(1+\gamma_{\mathrm d})^2$ in the denominator, which makes it larger by 4.0 at $Z_{\mathrm d}=1$ and 3.2 at $Z_{\mathrm d}=53$ and spoils the nonrelativistic limit."
- 22.3 Q5 ("as quoted by" Lee–Fukuyama): kept at s22-3 l.99. Fine, but the same sentence repeats the identification of the 0.951 meV mode from l.97 (see 22.3 issues).
- 22.1 Q1 ("settled" for boosted DM heavy mediator): s22-1 l.107 "One recast in the last group is settled for the heavy mediator." Reads fine.
- 22.1 Q2 (Ge hybrid functional): s22-1 l.97 prose is clear; citation attributes only.
- 22.1 Q4 (WE tolerance "about 2 %" labeled an estimate): s22-1 l.92 labels it, but awkwardly and with plain "percent" against `\SI{}{\percent}` elsewhere. Fix in 22.1 issues.

## 3. Issues: location → problem → fix

### Opening (ch22.tex)

1. l.4 → pattern 18 / user rule "motivational opening, not an outline": the whole paragraph is a section-by-section list ("Three indexes follow, each pointing to the homes and restating none of them: the calculations ...; the exact gaps ...; and the processes ..."). → Delete l.4 and end l.2 with one orienting sentence: "This chapter puts them side by side: which calculation would move which result, which gaps remain exact, and which processes the master formula cannot describe."
2. l.2 → pattern 19 (process artifact): "and the book has stated every such item once". Bookkeeping aimed at a reviewer. → Cut the clause: "Each of these statements stands in the section where its quantity arises, next to the calculation or the measurement that would settle it."
3. l.2 → the first two sentences are good concrete openers (numbers, open edge, 100 eV recoil). Keep. The opening never says that this is the last chapter of the book; one plain clause would make the ending deliberate ("At the end of the book, a reader who wants to know ...").

### 22.1 Calculations specified but not done

4. Title l.1 → participial, slightly long. → "Open calculations" (noun phrase, index term).
5. l.3 → pattern 22 (self-narrating plan): "We index them here by the result each changes, give each the exact relation or the control it must pass, and then sort the channels of the book by what limits them, theory, calculation or data." → "Each is listed by the result it changes and the exact relation or control it must pass, and each channel of the book is classed by what limits it: theory, calculation or data." Better: cut, since the subsection titles say it.
6. l.3 → repeated number (closing-chapter rule): "a factor of ten on the only electron-recoil rate between 0.333 and 0.405 MeV" repeats ch22.tex l.2 verbatim in content, and recurs at l.79, s22-2 l.17, s22-2 l.172, summary l.3. → Quote it once in prose with the pointer (keep ch22.tex l.2 with \cref{sec:13.9}); here write "Done, it would turn the factor-of-ten estimate of the window into a number with an error bar."
7. l.3 vs table l.38 vs s22-2 l.115 → three different upper ends of the window (0.405, "0.333 to 0.43 MeV", "lead to ≈0.43 MeV"). A reader of the closing chapter cannot tell which is the zero-phonon edge and which the crossover. → Name them once: "0.405 MeV, the zero-phonon edge; ≈0.43 MeV, where the zero-phonon rate takes over (\cref{sec:13.9})".
8. l.7–17 (22.1-checks, five paragraphs) → closing-chapter rule and pattern 26: an inventory of sum rules from Ch4, 7, 8, 13, 14, 18, 20, each restated with its equation; the "Check it must pass" column of tab:22-calc and summary l.3 restate it again. New facts per paragraph: l.7 exact relation vs control (new framing, keep); l.9 list of f-sum forms (restatement); l.11 positivity/KK (restatement plus one new sentence "A table that stores $S_{ab}$ with a negative eigenvalue ... fails before any comparison with data"); l.13 Ward identity (restatement plus "never by setting the electron–phonon vertex to zero", a calculation instruction); l.15 symmetry zeros, spin, cascade, transport (restatement plus "A calculation that returns these zeros at the level of its numerical noise has its phases and labels right"). → Keep l.7 and l.17; compress l.9–15 into one paragraph that keeps the three new sentences quoted above and points to the table for the individual relations.
9. l.7 → LONG-SENT, two-read parse: "An exact relation holds for every Hamiltonian of a stated class, so a result that violates it carries an error in its sum over states, in the labeling of its final states or in its normalization, whatever approximation it makes to the interactions." → "An exact relation holds for every Hamiltonian of a stated class. A result that violates it has an error in its sum over states, its labeling of final states or its normalization, whatever it approximates in the interactions."
10. l.21 → pattern 26: second and third sentences restate the table's group headings ("The order starts with the silicon electron recoil ... and last the lattice, spin, superconducting and Dirac targets and the recasts of published limits"). → Keep the first two sentences and the reason ("the running example and the channel on which most published limits rest"); cut the rest.
11. tab:22-calc rows l.52, l.57 → table not readable on its own: "Migdal row of the guide", "survivors", "threshold in quanta of the guide", "in one tier", "P(first)" are Ch21 terms. → Add to the caption: "Guide and survivors: the ranking table and the screened crystals of \cref{sec:21.7}."
12. l.79 → long paragraph with two jobs (head-row argument, then the cheapest row, then the sum-rule check). → Split before "The direct calculation of $\omega_{\mathrm{TA}}(\vect{Q}^*)$". Also "It cannot settle the window alone, however." is good register (the only "however" in the section); keep.
13. l.92 (WE) → Q4 phrasing: "Taking the order-$g^4$ term as $\theta_{\mathrm{ep}}^2$ of the $f$-sum, an estimate, the two sides must agree to about \SI{2}{\percent} of either, 1.8 percent at ... and 2.1 percent at 0.016." Parenthetical "an estimate" mid-sentence and "percent" spelled out. → "If the order-$g^4$ term is estimated as $\theta_{\mathrm{ep}}^2$ of the $f$-sum, the two sides must agree to about \SI{2}{\percent}: \SI{1.8}{\percent} at $\theta_{\mathrm{ep}}=0.010$ and \SI{2.1}{\percent} at 0.016."
14. l.82 (WE) → "The check has three parts." count-teaser (pattern 18) followed by run-in heads that name them. → "The check has three parts: the remainder, the nonlocal term and the transfer rule."
15. l.95 → parse failure: "Above 1 MeV the zero-phonon rate of silicon is a computed quantity whose band two calculations would narrow." Reads as "band two". → "Above 1 MeV the zero-phonon rate of silicon is computed, and two calculations would narrow its band." Same paragraph, last clause "for which \cref{eq:10.4-band} is all a limit can use until then" → "until then a limit can use only the bound \cref{eq:10.4-band}".
16. l.95, l.101, l.103 → repeated numbers already in tab:22-calc (×1.48, ×3.2, 0.119 vs 0.114, 1.128 vs 0.81–1.02). Prose and table give the same digits twice on one spread. → In prose keep the argument and drop digits the adjacent table row carries, or the reverse; each Ch10–21 number once in this chapter.
17. l.101 → pattern 25: "The charge of a low-energy nuclear recoil waits for one kernel." Also s22-2 l.3 "waits for a proof ... waits for a calculation", l.158 "Eleven gaps wait for a measurement". → "One kernel decides the charge of a low-energy nuclear recoil: the close-collision kernel \cref{eq:19.2-kernel}." Vary the others ("needs a proof", "needs a calculation").
18. l.101 → symbol: $Z\alpha/v_{\mathrm F}$ appears without $v_{\mathrm F}$ defined in the chapter. → "with $v_{\mathrm F}$ the Fermi velocity" (and derivation reviewer to confirm the Born parameter's form).
19. l.107 → $\mathcal{Q}$ in $(1-\omega^2/\mathcal{Q}^2)^2$ undefined here. → "with $\mathcal{Q}$ the ... of \cref{sec:10.9}" at first use.
20. l.111 title "Theory-limited and data-limited channels" → omits the largest class (calculation-limited, 11 of 22). → "Theory, calculation and data limits", or "Limiting factor by channel".
21. fig:22-limits caption → pattern 19: "the figure carries no numbers" echoes the chapter-map rule and is aimed at a reviewer. Caption is otherwise standalone. → Cut that clause; also split the LONG-SENT: "The classes are read from the open problems and nuisance tables of each chapter and from \cref{tab:21-dominant}."
22. l.120 → number style within one sentence: "11 are limited first by calculation, 10 by data and two by theory". → "11 ... 10 ... and 2 by theory" (technical count), or restructure.
23. l.122 → LONG-SENT stacking four unrelated sample properties. → Split after "(\cref{we:16-band})": "The gap and mean free path of an aluminum film, the two-level-system parameters of one film, the collection of a stated detector and the $^{210}$Pb and cosmogenic activities of a crystal are of the same kind."
24. l.124 → pattern 18 count-teaser opener: "The calculations and measurements that would change the most are few." → open with the content: "Four calculations each replace a factor of order ten or an unsized rate in a leading result: ..."
25. l.124 → aphoristic close (pattern 25, figurative cadence): "Each of them settles a question that the calculations of \cref{tab:22-calc} cannot, and each calculation settles one that no measurement listed here reaches." Deletion test: no fact lost. → Cut; end on the tagged-recoil sentence or on the two-bias measurement.
26. l.124 → periphrasis: "would open the zero-phonon window of the leader of the electron-recoil floor". → "would open the zero-phonon window of germanium, the crystal with the lowest electron-recoil threshold mass in \cref{tab:21-guide}" (or whatever "leader of the floor" means in Ch21; name it).
27. l.124 → LONG-SENT listing five measurements. → Keep as one list sentence but cut the "They are" frame: "On the data side, five measurements move a leading result: the cold absorption edge ..., the pair energy ..., ..."

### 22.2 Exact gaps in the theory

28. Title l.1 → 11 of the 72 missing steps are measurements; "in the theory" misdescribes. → "Exact remaining gaps" (the defined term, findable in the index).
29. l.3 → mild figurative: "The silicon rate of a particle with an anapole moment sits at the other end." → "At the other end is the silicon rate of a particle with an anapole moment."
30. l.3 → repeated number: "exceeds the static-electron formula at least 16 times" is also in tab:22-calc l.42, l.17 here ("the factor of at least 16 above"), and tab:22-gaps. Acceptable as the section's opening example; then drop it from l.17 ("such as the anapole bound above").
31. l.3 → redundancy with ch22.tex l.2 and the keyresult: "the book states each such item once, in the section where it arises". Third statement of the one-home rule (also keyresult l.10, tab:22-gaps caption, summary). → Cut here; the keyresult carries it.
32. l.7 → pattern 25 withholding: "The germanium window is open, but \cref{sec:13.9-open} says more than that." → "\Cref{sec:13.9-open} states the open germanium window in two parts."
33. l.13 → pattern 26 (loop after keyresult). New facts: the four kinds of strongest statement (theorem, bound, estimate, number awaiting check). Repeats: "The missing step is single in the sense that nothing else stands between the statement and the result" (= keyresult "single missing step ... that would turn the statement into the full result"); last sentence repeats keyresult's pointer to \cref{app:E}. → Move "a theorem under stated hypotheses, a bound, an estimate with its factor, or a computed number that awaits an independent check" into the keyresult's first part and delete the paragraph.
34. l.17 → number style: "Five gaps ... The other 67 ... For 10 ... For 18 ... For 34 ... The last 5". Mixed word/numeral for the same count series. → Numerals throughout the series (technical counts): "5 gaps are of this kind" — or rephrase so no sentence starts with a numeral: "Of the 72, five limit only a proof ...".
35. l.19 → counts disagree with summary l.5 (see Sect. 2). Also pattern 19: "Here every gap appears once, in the order of the book, whatever its weight." → cut "whatever its weight"; the caption already says "by chapter".
36. tab:22-gaps caption and column head "Gap; home", and throughout ("home" 7× in s22-1, 14× in s22-2, 4× in s22-3, 1× in summary and ch22.tex) → standalone scrub: "home" is the campaign's internal label for the owning section, not a word of the field or of a printed book. The caption defines it, so it is not fatal, but the WE title "read from its home" and phrases like "the homes" (s22-1 l.111, ch22.tex l.4) read as process jargon. → Column "Sect."; in prose "the section that states it" or "its chapter"; WE title "The constant term of the mean pair number".
37. tab:22-gaps → readable on its own except row shorthands: "survivors" (Ch21), "off-shell window", "four-path amplitude", "growth lead". → Same caption clause as issue 11; the rest are acceptable as abbreviations covered by "The statements are abbreviated".
38. l.154 → empty opener (pattern 0/18): "The table has a shape." → Delete; open with "The five proof gaps sit at the two ends of the theory, ...".
39. l.156 → pattern 19 bookkeeping at the end: "The 72 rows therefore stand for fewer independent steps, and \cref{sec:22.1} counts each calculation once." → "The 72 rows therefore stand for fewer independent steps; \cref{tab:22-calc} lists each calculation once."
40. l.158 → enumeration in prose without argument (pattern 11 borderline): two "Four concern ..." lists. Acceptable as a genuine enumeration; vary the rhythm (two parallel "Four concern" sentences).
41. l.161 (WE) → "Reading it from its home takes four steps." Count-teaser and internal label; the run-in heads already show the steps. → Cut, or "The four parts of the gap are as follows." Better cut.
42. l.169 (WE) → close is a looped verdict ("The gap therefore limits a proof: ... \Cref{tab:22-gaps} lists it as such."). The last sentence is bookkeeping. → Cut "\Cref{tab:22-gaps} lists it as such."
43. l.172 → repeats the factor of ten again (fifth time in the chapter). → "There the strongest statement is an estimate, and the missing step ..." (pointer already present).

### 22.3 Channels outside the framework

44. l.3 → strong concrete opener (626 keV, factor 6.3, charge 53). Keep. Pattern 15 anthropomorphic: "a tensor $\mathfrak{D}_{ab}(\vect{q},\vect{v})$, which knows nothing of the target, multiplies a response $S_{ab}(\vect{q},\omega)$, which knows nothing of the dark matter". → "a tensor $\mathfrak{D}_{ab}(\vect{q},\vect{v})$ that depends only on the dark-matter side multiplies a response $S_{ab}(\vect{q},\omega)$ that depends only on the target". Same at l.72: "A response sums over final states with no knowledge of how the outgoing particle sees them" → "A response sums over final states independently of the outgoing particle".
45. l.3 last sentence → pattern 22: "For each such process we give the reason and the calculation or measurement that a prediction would need." → Cut; the table caption says it.
46. l.7–9 → count mismatch: "three properties" give three violation classes, "A fourth class lies inside the framework", then two assumptions of \cref{sec:8.2-conditions} add two more rows, and l.9 says "\Cref{tab:22-scope} lists every process of the four classes". The table has six rows, two of which belong to no listed class. → "\Cref{tab:22-scope} lists these processes, the two that the assumptions of \cref{sec:8.2-conditions} exclude, and the one inside the framework that has no conserving response yet."
47. l.9 → $\mu_{\chi T}$ and the "20A" bound without a pointer for the reader of an index chapter. → add "(\cref{sec:8.2-conditions})" after the bound.
48. tab:22-scope → readable on its own; "Home" column again (issue 36). Caption "Processes outside the framework" but last row is inside; the caption's "for the last row" clause handles it. Fine.
49. eq:22.3-cc l.42 → first-use definitions: $\Lambda_{\mathrm F}$ is not defined in the text (only implied), nor $p$, $n$, $e$, $\chi$ as fields. → "with $\Lambda_{\mathrm F}$ the scale of the charged-current operator, $p$, $n$, $e$ and $\chi$ the proton, neutron, electron and dark-matter fields, $P_R = ...$".
50. l.53 → ambiguous: "Adding them alone would keep the framework". → "Adding these rows, and nothing else, would keep the framework".
51. l.57 → LONG-SENT. → "The wave can then be evaluated at the nucleus. Its squared amplitude relative to a plane wave is the Fermi function \cite[Eq.~(6)]{hayen2018high},".
52. l.65 → "here $\Gamma$ is Euler's gamma function": STYLE reserves upright $\Gamma$ for the zone-center point. Flag to the notation reviewer (the gamma function is standard, but NOTATION.md should list the exception).
53. l.85 → two-read sentence: "Counting the nucleon-level rate once per neutron, the factor $n_j \simeq A - Z$ of the published projections~\cite[Eq.~(4.6)]{dror2020absorption}, gives 73 for $^{125}$Te, where the Fermi sum rule allows 21 in total, all of it in one state." → "The published projections count the nucleon-level rate once per neutron, $n_j \simeq A-Z = 73$ for $^{125}$Te~\cite[Eq.~(4.6)]{dror2020absorption}. The Fermi sum rule allows 21 in total, all of it in the analog state."
54. l.87, l.91 (and ch22.tex l.4) → pattern 10 rhythm: three consecutive "needs three things ... The first ... The second ... The third" scaffolds in one section. → Keep one; in l.91 fold into one sentence: "A prediction needs the abundance of $\chi_2$ at the detector, ..., the local field at the decaying particle, ..., and the absorption length of the photon."
55. l.87 last sentence → pattern 26: "Beyond the allowed approximation the rate has no product form, and the golden rule with the full electron wave is the only statement." Restates l.55 and the WE close (l.76 "the general rate is a property of the target together with the electron"). → Cut l.87's last sentence; keep l.55.
56. WE title l.67 → "Why ..." clause title. → "The Fermi function of $^{125}$Te absorption".
57. l.97–99 → small loop: l.97 "which Kim and collaborators identify as the phason"; l.99 "who identify the \SI{0.951}{meV} mode of (TaSe$_4$)$_2$I with the massive phason". → In l.97 say "the massive phason" once; in l.99 "Lee and Fukuyama showed this, as quoted in \cite{kim2023observation}."
58. l.97 → $v_{\mathrm{max}}$ undefined in chapter. → "with $v_{\max}$ the maximum dark-matter speed in the laboratory".
59. l.97 → "can excite modes 263 to 315 times below the charge gap" → "can excite modes that lie 263 to 315 times below the charge gap".
60. l.101, l.103, tab l.35, summary l.3, l.9 → typography: "f-sum" in roman; s22-1 writes "$f$-sum". → "$f$-sum" throughout.
61. l.103 → "Three checks decide whether the result can be trusted." Count-teaser; l.101 already states the Goldstone and $f$-sum conditions. → "The checks are the Goldstone limit (with $\vect{Q}_{\mathrm{CDW}}$ made artificially incommensurate ...), the $f$-sum rule and the measured modes ...".

### Summary

62. l.3 → pattern 22/19: "and this chapter indexes each without restating it". Self-narration, and the summary then restates. → "The open problems of the book fall into three kinds."
63. l.3 → restates the 22.1-checks inventory (f-sum shares, positivity, Kramers–Kronig, Ward identity, acoustic sum rule, zeros; four controls) but omits the section's result. → Replace the two inventory sentences with the outcome: "Of the 22 channels, 11 are limited first by calculation, 10 by data and 2 by theory. Four calculations each replace a factor of order ten or an unsized rate in a leading result: the phonon-assisted loss function of silicon, the coherent Migdal response below $2q_{\mathrm{BZ}}$, the loss functions of the survivors near their gaps and the close-collision kernel; five measurements do the same on the data side."
64. l.5 → 53/11/8 contradicts s22-2 l.19 (55/11/6). Fix after recount.
65. l.7 → long (≈240 words) against ≈150 for 22.1; re-quotes 6.34, 4.3 %, 14 MeV and adds 3.5, a number not in s22-3 ((A−Z)/(A−2Z) is new formulation). → Keep the reason, the Fermi-function point and the sum-rule point; drop 4.3 %; either add "a factor 3.5" to s22-3 l.85 or drop it here.
66. l.9 → the book ends on "263 to 315 times below its charge gap", a detail of one row. No advertising tone (good), but no closing statement either. → End on one plain sentence that closes the book on the priority result, e.g. "Most of what the book leaves open is calculation, not theory: the framework is complete for 20 of the 22 channels, and the numbers are missing." Keep it flat; no "exciting", no "future".

## 4. Pattern 25 sentence-by-sentence (openings, section openers, captions)

- ch22.tex l.2: four sentences, all positive and concrete. "sees dark matter only through" is a plain restriction, not periphrasis. OK. l.4: outline (issue 1), no periphrasis.
- s22-1 l.3: OK. 22.1-checks l.7: OK. 22.1-list l.21: OK. 22.1-limits l.111: "only if" plain. OK.
- s22-2 l.3: "sits at the other end" (issue 29); "waits for a proof/calculation" (issue 17). 22.2-definition l.7: "says more than that" (issue 32). 22.2-table: no prose opener.
- s22-3 l.3: "knows nothing of" twice (issue 44). 22.3-scope l.7, 22.3-cc l.40, 22.3-tracks l.91, 22.3-cdw l.97: OK.
- Captions: tab:22-calc OK; fig:22-limits "carries no numbers" (issue 21); tab:22-gaps OK ("no number of the book changes" is a definition); tab:22-scope OK.

## 5. Pattern 26 (new facts per paragraph), flagged paragraphs only

- s22-1 l.9, l.11, l.13, l.15: mostly restatement of home equations (issue 8).
- s22-1 l.21: order sentence restates the table groups (issue 10).
- s22-1 l.124: first and last sentences add nothing; middle lists repeat l.79–101 in brief. Keep as the section's synthesis, trimmed (issues 24–25).
- s22-2 l.13: subset of the keyresult except the four kinds of statement (issue 33).
- s22-3 l.87 last sentence; WE l.76 last clause (issue 55).
- s22-3 l.103: checks repeat l.101 (issue 61).
- Summary: sanctioned recap; but l.3 recaps the wrong part (issue 63).

## 6. Closing-chapter checks

- Restating home chapters at length: 22.1-checks (≈700 words) is the one place it happens (issue 8). The rest indexes with pointers.
- Each Ch10–21 number once with a pointer: fails for the phonon-assisted factor of ten (5× in prose), the 0.333–0.405 MeV window (3×), the anapole "at least 16" (3× in prose plus two tables), the Ge onset (2× prose, at two precisions: 0.2119–0.2141 in s22-1 l.97, 0.212–0.214 in s22-2 l.7), and the ×1.48, ×3.2, 0.119/0.114 and 1.128 values (prose duplicates the adjacent table row). Tables may carry them; prose should quote each once (issues 6, 16, 30, 43).
- Gap table and scope table on their own: captions define every column and class; remaining opacity is Ch21 shorthand ("survivors", "guide", "tier", "P(first)") and the "home" label (issues 11, 36, 37).
- Ending: no advertising tone anywhere (no "exciting", "promising", "future work"). The book ends abruptly on a table detail (issue 66).

## 7. Seams

- Opening → 22.1: both open on the 0.333–0.405 MeV window and the factor of ten; 22.1 l.3 restates ch22.tex l.2. Change 22.1's opener to the specification and cost (it already has them) and drop the repeated number (issue 6).
- 22.1 → 22.2: 22.1 ends on the aphorism (issue 25); 22.2 opens on the decomposition theorem. After the cut, the join is clean. 22.2 l.19 points back to 22.1 correctly.
- 22.2 → 22.3: 22.2 ends on the ZP/PA ratio; 22.3 opens on $^{125}$Te. No bridge needed (independent index), but the last row of tab:22-gaps (Ch22 rows) already introduces charged-current absorption and the CDW, so 22.3 reads as their home. Fine.
- 22.3 → Summary: summary order matches sections.

## 8. Register calibration (REGISTER.md)

Connective counts (prose and tables, per section): "however" 1 / 0 / 0 (s22-1/2/3); "we will/can/see/find" 0 everywhere; "typical" 0 everywhere; "note that" 0; "for example/instance" 0; "since" 4 / 0 / 1. Tics within bounds: "so" 8 / 5 / 8 in ≈4.9k / 4.7k / 3.1k words (under 3 per 1,000); "therefore" 1 / 2 / 3; "of order" 3 / 2 / 2 (L 0). No "thereby", "whereby", "respectively", "in order to", "i.e.", "e.g." or exclamation marks. The voice is consistent across the three writers but airless in the way REGISTER Sect. 1 describes: flat assertions, no "we", no reasons in "since" clauses. Target per checklist item 8: one "however"/"but" and one "we" construction per 1,000 words.

Passages and one Lin-style rewrite each:
- s22-1 l.111 "A better calculation sharpens a channel only if the channel is limited by calculation." Lin could write this. OK.
- s22-1 l.105 "The lattice, spin, superconducting and Dirac entries each move a correction or a special target." Not Lin. → "For the running example, the lattice calculations hardly matter: for a nucleon coupling we already know the silicon lattice rate to a quarter of a percent (\cref{sec:11.9})."
- s22-1 l.101 → "Since the Born parameter $Z\alpha/v_{\mathrm F}$ is 15 in silicon and 35 in germanium, no linear response can describe the close collisions ..." (raise "since").
- s22-2 l.15 "A gap differs from a nuisance." Lin-like, OK.
- s22-2 l.154 → "The five proof gaps, we see, sit at the two ends of the theory ..." is too mannered; better: "Note that the five proof gaps sit at the two ends of the theory: ..."
- s22-2 l.17 → "What a gap limits decides how we can use it" (for "how a reader uses it").
- s22-3 l.55 "The electron prevents that." Lin-like, OK.
- s22-3 l.93 → "A silicon ion at typical dark-matter recoil speeds has a Born parameter of 117 to over a thousand, so no single scattering is perturbative." (adds the model's main hedge).
- s22-3 l.97 → "However, nothing in the master formula changes for such a target; what we lack is a response that obeys the exact relations of \cref{sec:8.3}."

## 9. User-rule checks (pass unless listed above)

- No exercises, checkpoints, "you", or steps left to the reader: pass.
- Citations attribute only: pass. s22-3 l.45, l.57, l.65, l.85 and s22-1 l.97, l.107 state the content in the book; the Dror Eq. (4.10) note is a fact about the literature (Sect. 2).
- Cross-references all via \cref/\Crefrange; no hard-coded internal numbers. "Equation~(4.10) of that reference" is external and fine.
- Equation punctuation: all four displays punctuated (lint hit is a false positive).
- No bare "Limit N.M" or "limit box"; \cref{lim:12.3a}, \cref{lim:14.5b} only.
- Standalone scrub: no SPINE, DC-, writer/reviewer labels in the tex; "home" is the one internal label (issue 36).
