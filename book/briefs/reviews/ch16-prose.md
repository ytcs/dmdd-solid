# Chapter 16 batch review: style and prose (isolated)
Review /home/user/dmdd-solid/book/tex/ch16/s16-1.tex to s16-9.tex and s16-summary.tex (with App. D.41–D.42 at tex/appD/D-41.tex, D-42.tex) against /home/user/dmdd-solid/book/STYLE.md, /home/user/dmdd-solid/skills/long-form-writing/references/style-guide.md and /home/user/dmdd-solid/skills/long-form-writing/references/prose-review.md.

1. Run `python /home/user/dmdd-solid/skills/long-form-writing/scripts/lint.py --banned /home/user/dmdd-solid/book/BANNED-TERMS.txt <file>` on each file and record the hits.
2. Read the whole chapter as a copy editor would. Check:
   - voice consistency across the nine writers;
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
   - the user rules: no exercises or checkpoints; nothing left to the reader; succinct general background; motivational chapter opening (not an outline); concrete openers (prose-review rule 18); no process artifacts (pattern 19); citations attribute only, so nothing requires opening a source (pattern 20); limit boxes as self-contained comparison plots; the register of /home/user/dmdd-solid/book/REGISTER.md (word frequencies, terms of art, idioms), including its calibration check of 2–3 passages per section.
3. Check the chapter as a whole:
   - the opening outline paragraph;
   - the summary;
   - redundancy across sections;
   - the seams between sections (read each pair of adjacent sections across the join).

Output /home/user/dmdd-solid/book/ledgers/REVIEWS/ch16/prose.md, ≤ 260 lines. Give one verdict per section (PASS / REVISE / REWRITE). Then list each issue as location → problem → fix, with quoted text. Do not edit the tex. Do not commit. Final message ≤ 10 lines.
- Also review ledgers/REVIEWS/ch16/editor-notes.md items that concern prose.
- Also check prose-review pattern 25 (periphrasis, negation-stacked withholding) sentence by sentence in every chapter opening, section opener and caption.
- Also check prose-review pattern 26 (looped restatement): for each paragraph, list its new facts and flag any paragraph that adds none, especially at the end of subsections. First known case: Sect. 1.3.1.
- Ch16 is long (~35,000 words, nine sections): flag cuts, sections over budget (16.4, 16.6, 16.7), repeats across sections, and the 22 long sentences in 16.7.
