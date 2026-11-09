# Appendix E.14–E.27 (computational specifications) batch review: style and prose (isolated)
Review /home/user/dmdd-solid/book/tex/appE/E-14.tex to E-27.tex (the computational specifications of Appendix E: standalone specs of deferred calculations) against /home/user/dmdd-solid/book/STYLE.md, /home/user/dmdd-solid/skills/long-form-writing/references/style-guide.md and /home/user/dmdd-solid/skills/long-form-writing/references/prose-review.md.

1. Run `python /home/user/dmdd-solid/skills/long-form-writing/scripts/lint.py --banned /home/user/dmdd-solid/book/BANNED-TERMS.txt <file>` on each file and record the hits.
2. Read the whole chapter as a copy editor would. Check:
   - voice consistency across the four writers;
   - filler, inflated adjectives, reflexive triads, stacked hedges, and paragraphs that restate the one before;
   - lists used in place of argument;
   - sentence length;
   - titles (short noun phrases);
   - equation punctuation;
   - first-use symbol definitions;
   - captions that stand alone;
   - the citation style;
   - cross-reference style (\cref);
   - the standalone scrub: no process or internal labels;
   - the user rules: no exercises or checkpoints; nothing left to the reader; succinct general background; the transition from E.13 into E.14 (the appendix opening in appE.tex already frames both parts); concrete openers (prose-review rule 18); no process artifacts (pattern 19); citations attribute only, so nothing requires opening a source (pattern 20); limit boxes as self-contained comparison plots; the register of /home/user/dmdd-solid/book/REGISTER.md (word frequencies, terms of art, idioms), including its calibration check of 2–3 passages per section.
   - App E is a methods appendix, so procedure is in scope, but it must be written as argued prose and not as recipe lists. Flag numbered step lists (e.g. E.5) and any instruction addressed to the reader ("run", "set", "choose"). Also review the items in ledgers/REVIEWS/appE/editor-notes.md that concern prose.
3. Check the chapter as a whole:
   - the opening outline paragraph;
   - the summary;
   - redundancy across sections;
   - the seams between sections (read each pair of adjacent sections across the join).

Output /home/user/dmdd-solid/book/ledgers/REVIEWS/appE2/prose.md, ≤ 260 lines. Give one verdict per section (PASS / REVISE / REWRITE). Then list each issue as location → problem → fix, with quoted text. Do not edit the tex. Do not commit. Final message ≤ 10 lines.
- Length: E.14, E.20, E.21, E.22 and E.25 are over budget. There is no hard cap; flag duplication with the main chapters and with the methods sections E.1–E.13, and propose concrete cuts.
- Also check prose-review pattern 25 (periphrasis, negation-stacked withholding) sentence by sentence in every chapter opening, section opener and caption.
- Also check prose-review pattern 26 (looped restatement): for each paragraph, list its new facts and flag any paragraph that adds none, especially at the end of subsections. First known case: Sect. 1.3.1.
