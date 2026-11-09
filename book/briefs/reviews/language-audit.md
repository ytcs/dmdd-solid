# Final language-only audit (run once, after every chapter is ACCEPTED and before the final figure check)
Scope: the whole book (tex/ch*, appA–appF, front matter). **Language only.** No number, equation, label, citation or cross-reference changes; if a sentence's physics looks wrong, log it separately for the editor and do not change it.

Targets, in priority order:
1. chapter openings;
2. section openers (the first paragraph of each section);
3. figure, table and Limit Check captions, and key-result boxes;
4. body text.
Read targets 1–3 in full even where lint is clean. For the body, use lint hits plus a skim.

What to fix (skills/long-form-writing/references/prose-review.md):
- pattern 0 (information content: the deletion test);
- pattern 25 (periphrasis, negation-stacked withholding);
- pattern 24 (invented metaphor vocabulary);
- patterns 21–23 (gesturing titles, self-narrating provenance, unannotated master equations);
- filler, stacked hedges, reflexive triads, inflated adjectives;
- STYLE.md "Plain words, positive statements";
- the REGISTER.md calibration.

Procedure, one batch per Part (I, II, III, then the appendices):
- Reviewer (read-only): run lint.py with BANNED-TERMS.txt on every file, then read the targets.
- Reviewer output: ledgers/REVIEWS/language/<part>.md, listing `file:line → quoted sentence → plain rewrite`. Mark each item MUST or OPTIONAL.
- Reviser: applies the MUST items and the clear OPTIONAL ones with exact Edits, reruns lint, and builds main.tex with 0 LaTeX errors and no new undefined references.
- Reviser log: ledgers/REVIEWS/language/<part>-applied.md.

The pattern was measured on 2026-11-03 with the PERIPHRASIS regex, which catches only the literal forms: 3 hits (ch01, ch11, appD). The figurative forms are broader than any regex, so this audit reads instead of grepping.
- Also check prose-review pattern 26 (looped restatement): for each paragraph, list its new facts and flag any paragraph that adds none, especially at the end of subsections. First known case: Sect. 1.3.1.
