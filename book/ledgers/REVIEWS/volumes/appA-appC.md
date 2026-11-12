# Unit appA / appB (hand-written parts) / appC: copy-edit log

## Words before and after (`cat <files> | wc -w`)

| Part | Before | After | Change |
|---|---|---|---|
| appA (appA.tex, A-1 … A-9) | 7225 | 7073 | −2.1 % |
| appB hand-written (appB.tex, B-2.tex) | 1260 | 796 | −36.8 % |
| appC (appC.tex, C-1 … C-20) | 33644 | 33052 | −1.8 % |

Per file, changed files only: A-2 682→669; A-3 962→927; A-4 601→586; A-5 817→766; A-7 900→862; appB.tex 61→65; B-2 1199→731; C-1 1720→1613; C-2 1333→1316; C-3 1613→1588; C-4 1480→1378; C-5 1723→1594; C-8 1370→1314; C-9 1810→1776; C-10 2093→2065; C-11 2214→2198; C-18 2277→2244; C-20 2372→2328. Unchanged: A-1, A-6, A-8, A-9, C-6, C-7, C-12 … C-17, C-19.

Appendices A and C shrink by less than the 3 % guide. Reason, checked against the citing chapters: Appendix A is the convention authority and almost every sentence is a definition, a sign or a conversion; Appendix C is the single home of its mathematics. In every citing passage I read (s1-4, s2-4, s3-1, s4-1, s4-4, s4-7, s5-2, s5-6, s11-5, s12-6, s13-9, s14-4, s16-8, s17-6, s19-6, D-15) the chapter states the result and points to the C section for the proof; none repeats the derivation. The one true duplicate found (B-2 against A) is where the words went.

## Cuts and moves longer than three sentences

1. **B-2.tex, the four closing paragraphs** ("Fourier transforms", "Sign of the mixing term", "Units of charge", "Normalization of the structure factor"; 499 words, 9 citations). Every statement stands in Appendix A: Fourier signs and the Hochberg/Trickle variants in A.3 (and A.4), the mixing sign and the Lin/Essig forms in A.9 "Kinetic mixing", the charge map in A.2, the 2π/V normalization, f-sum rule, per-electron form and spin factor in A.7. Replaced by the lead sentence that was already there, now carrying a \cref to each of A.3, A.9, A.2, A.7. A.9 keeps its pointer to B.2 for the symbols used for ζ (table row). B-2 now holds the table only.
2. **C-4, subsection "Summary of definitions"** (140 words, one four-line display). It repeated eq:C.4-SP, eq:C.4-square, eq:C.4-dPV, eq:2.4-split and the folded finite part that eq:2.4-fp already gives. The one item given nowhere else, the folded form of the principal value with the remark on numerical work, moved to the paragraph after eq:C.4-PV.
3. **C-1, paragraph "The same number follows from a physical reading"** (104 words). A second derivation, by Parseval's theorem with a forward reference to eq:C.1-parseval, of the area ∫sin²u/u² = π that eq:C.1-sinsq has just proved. Removed; eq:C.1-parseval itself stays in "Fourier identities".
4. **C-5** (129 words in all): the outline sentence of the opening (the assumed prerequisites and the two citing sections stay); the paragraph "The sign convention matters at this point …" (two sentences, content in A.3, which the preceding paragraph already cites); the sentence "two faces of one statement"; three signposts.
5. **C-18, Debye speed and temperature of the isotropic [100] model** (45 words, 6.35 km/s and 696 K against 645 K). The identical numbers and reason stand in s5-2 (line 188). Replaced by a clause pointing to sec:5.2. See cross-unit note 2.

Smaller cuts (three sentences or fewer): A-5 normalization remark repeated from A.3 (now a \cref); A-3 prose restatement of eq:A.3-unreduced; A-4 repetition of "never reduced" from A.3; A-7 two sentences around eq:A.7-fsum and the closing restatement; A-2 signpost; B-2 sentence describing the table columns; C-3 outline sentence and a rhetorical question; C-8 two outline sentences of the opening (each repeated by its subsection); C-9 unit check repeated from A.2 (with a forward reference); C-10 outline sentence; C-11 two signposts; C-20 outline sentence, one figurative clause, one summary sentence ahead of its own explanation; C-1, C-4 signposts. C-18: "evaluates" → "evaluate" (grammar).

## Labels

- `eq:C.2-latticesum` removed: the display repeated eq:3.1-latticesum. Grep found no reference outside C-2; the two references inside C-2 now point to `eq:3.1-latticesum`, and the formula stays inline.
- No other label removed.

## Seams fixed

- appB.tex, first sentence: "Every symbol of the book is listed in B.1" → "Every symbol first used in this volume is listed in B.1" (the generated list is per volume and says so). Second sentence: the sign and normalization conventions are now said to be in Appendix A (\cref{app:A}), since B.2 no longer repeats them.
- Appendix A: no wording found that assumes one volume ("earlier in the book", "Appendix E" in words); all references to moved material are \cref's. Nothing changed for this reason.
- Appendix C: no "Part", "Appendix E" or neighbour-chapter wording found.

## Sentences written (not assembled from existing text)

1. C-4: "Folding the negative half line onto the positive one gives PV∫dx w(x)/x = ∫₀^∞ dx [w(x) − w(−x)]/x, whose integrand is finite at the origin: a principal-value integral over a tabulated spectrum is computed by folding, not by cutting out an interval around the pole." (formula and both clauses taken from the deleted summary; only the joining is new)
2. C-18: "; \cref{sec:5.2} compares its Debye temperature with that of the full angular average."
3. appB.tex: "…; the sign and normalization conventions in which they differ from this book are in \cref{app:A}."
4. C-2: "On the Born--von Karman grid of a block of N cells, …, the lattice sum is … (eq:3.1-latticesum), and a zone of volume (2π)³/Ω holds N crystal momenta, one per cell." (rebuilt from the old sentence after the display was removed)
5. A-4: "The first-zone part q_r of the momentum transfer labels …" (old sentence with its subject spelled out after the preceding sentence was cut).
All reread against the prose-review patterns; lint run on every changed file, no hit in a touched sentence.

## Appendix C sections against their citing chapters ("fold" candidates for the lead editor)

No C section became short enough to fold: the shortest is C.13 (957 words). Assessment per section:

- **C.13 (interval orders), cited only by ch17/s17-6.tex** — the nearest candidate. s17-6 (line 44 and the paragraph at line 66, plus `we:17-tiers`) already states the order, the height, the antichain property, "tiers never invent an order" and has its own worked example. What only C.13 holds: the proof of transitivity and of the antichain and "resolved below tier k−1" properties, the Fishburn characterization, the sorting algorithm, the dependence of tiers on the confidence level. Suggestion: fold into ch17/s17-6.tex at the paragraph that cites `eq:C.13-order` (labels `eq:C.13-order`, `eq:C.13-height` would move with it), dropping C.13's four-material example in favour of `we:17-tiers`; about 400 words would move.
- **C.16 (quantized radiation field), cited only by ch12/s12-6.tex**: 1300 words of derivation that s12-6 uses by reference (line 7 quotes eq:C.16-soft, line 28 the medium mode). Too long to fold; keep.
- **C.10** (ch11/s11-5, ch31/E-19), **C.11** (ch18, D-43, D-44), **C.12** (ch21/s21-2, D-46), **C.19** (ch7, ch14), **C.20** (ch16, ch19, ch31, D-42): each 1200–2300 words of proof used from two or more files or volumes; keep.
- C.1–C.9, C.14, C.15, C.17, C.18: shared tools used by several chapters across volumes; keep.

## Cross-unit problems seen, not fixed

1. **appB bibliography in Volume III.** B-2.tex no longer cites anything, and appB/B-1-vol3.tex has no citation either, so `\printbibliography[heading=subbibliography]` in appB.tex is empty in Volume III (biblatex "Empty bibliography" warning; nothing prints). Volumes I and II still have the citations of their B-1 lists. If the volume build treats the warning as an error, guard the line in appB.tex for \volid = 3. Not checked by chapcheck (no appB unit).
2. **ch05/s5-2.tex line 188 and appC/C-18.tex line 62: the "isotropic [100] model".** It is used nowhere else in the book and is dominated by the full angular average of `we:5-debye` (645 K against its 696 K). I removed only the duplicated Debye numbers from C-18. If the Chap. 5 editor removes the model under the Pareto directive, the two remaining sentences in C-18 ("The simplest approximation keeps the measured constants … 8.43 and 5.84 km/s; \cref{sec:5.2} compares …") should go with it; if the model stays, s5-2 is its home and C-18 only defines it.
3. **ch19/s19-6.tex lines 132 and 142** give the kink profile and E_kink twice within one subsection (once by \cref to eq:C.20-kink, eq:C.20-Ekink, once written out as "the published crowdion"); the second is a repeat of C.20 for the Chap. 19 editor.
4. **Appendix A, internal duplicate left in place:** eq:A.2-SL (A.2) and the first relation of eq:A.7-SL (A.7) are the same formula. Both labels exist and A.2 says "derived in A.7"; I did not remove a labelled equation of the convention appendix. Likewise ε = 1 + iσ_cond/ω is stated in A.2 (conversions) and A.7 (definition).
5. **ch01/s1-4.tex lines 30 and 57** cite app:C.9 for the Born amplitude and σ = μ²|Ṽ|²/π "(app:C.9; derived in sec:2.2)". The C.9 subsection "From the potential to a cross-section" only previews sec:2.2; it was kept because of these two citations. If the Chap. 1 editor cites sec:2.2 alone, that subsection (about 150 words) can be removed.

## Checks

- `tools/chapcheck.sh appA`: exit 0, 0 undefined references, 0 multiply defined labels (2 overfull hboxes > 5pt, present before the edit: table and displays untouched).
- `tools/chapcheck.sh appC`: exit 0, 0 undefined references, 0 multiply defined labels (1 overfull hbox > 5pt, in untouched text).
- Lint on all 18 changed files: 0 blocking; remaining warnings are LONG-SENT / EQ-PUNCT in sentences not touched.
- B-1*.tex and B-3.tex not touched. Not committed by me (the lead's snapshot commits picked up some of the edits).
