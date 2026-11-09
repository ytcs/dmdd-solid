# Chapter 1 batch review: style and prose (isolated)
Review /home/user/dmdd-solid/book/tex/ch01/s1-1.tex to s1-5.tex (with C-9 and D-1) against /home/user/dmdd-solid/book/STYLE.md, /home/user/dmdd-solid/skills/long-form-writing/references/style-guide.md and /home/user/dmdd-solid/skills/long-form-writing/references/prose-review.md.

1. Run `python /home/user/dmdd-solid/skills/long-form-writing/scripts/lint.py --banned /home/user/dmdd-solid/book/BANNED-TERMS.txt <file>` on each file and record the hits.
2. Read the whole chapter as a copy editor would. Check:
   - voice consistency across the five writers;
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
   - the user rules: no exercises or checkpoints, nothing left to the reader, succinct general background.
3. Check the chapter as a whole:
   - the opening outline paragraph;
   - the summary;
   - redundancy across sections;
   - the seams between sections (read each pair of adjacent sections across the join).

Output /home/user/dmdd-solid/book/ledgers/REVIEWS/ch01/prose.md, ≤ 220 lines. Give one verdict per section (PASS / REVISE / REWRITE). Then list each issue as location → problem → fix, with quoted text. Do not edit the tex. Do not commit. Final message ≤ 10 lines.
- Also check prose-review pattern 25 (periphrasis, negation-stacked withholding) sentence by sentence in every chapter opening, section opener and caption.
- Also check prose-review pattern 26 (looped restatement): for each paragraph, list its new facts and flag any paragraph that adds none, especially at the end of subsections. First known case: Sect. 1.3.1.
