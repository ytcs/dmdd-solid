# Sentence-construction round: independent review

You review the edits of the sentence-construction round in one block of chapters. You did not make them. Read first: /home/user/dmdd-solid/skills/long-form-writing/references/prose-review.md pattern 27 (end of file), book/STYLE.md last section, book/REGISTER.md, and book/briefs/volumes/BINDING.md (the editors' brief, including its Calibration section and hard limits). Do not read the editors' logs before you have formed your own view of the diff; afterwards you may use them to check their stated "interpretations".

Diff: `cd /home/user/dmdd-solid/book && git diff -U0 60cc72c -- <your files>`; read the current files whole as well.

## Job 1: every changed sentence
For each changed sentence check:
- **Fidelity.** Same claim, same strength; no qualifier, validity condition, domain or uncertainty lost or added; the physics is still right; a name the edit introduced refers to the same object everywhere it is used in the chapter.
- **Binding and depth.** Every pointer has exactly one antecedent noun phrase in the same or previous sentence; no garden path, heavy subject, PP chain, dangling modifier, or sentence that needs two parses.
- **Register.** No over-repair: a pronoun with one candidate that is the subject of the previous clause was fine and should not have become a repeated noun; no robotic repetition a careful physicist would not write.
Fix what fails, directly in the file (the editors' hard limits apply to you too), or revert to the base wording when the base was better.

## Job 2: recall
Read at least one paragraph in ten that the editors did not change, spread over every file (more where the ranker `python3 /home/user/dmdd-solid/skills/long-form-writing/scripts/binding.py <file>` still flags much), and count the pattern-27 failures left. Fix them. Report misses per 1000 words of the paragraphs you sampled.

## Open items
book/ledgers/REVIEWS/volumes/binding/OPEN.md lists points the editors left to the lead for your files. Decide each: fix it, or state why it stays. A point that is a physics error rather than wording (for example a wrong statement of what a quantity is) is not yours to fix: write it as a proposed erratum (location, old text, proposed new text, reasoning) in your log, and the lead will route it through the errata review.

## Checks and report
- After your fixes: `python3 tools/invariant.py 60cc72c <files>` (no STOP except intended symbol unifications the editors listed), the lint on changed files, and `tools/chapcheck.sh <chNN|appX> /tmp/binding-review-<block>` for each chapter or appendix (exit 0, no undefined references, no multiply defined labels).
- Log to book/ledgers/REVIEWS/volumes/binding/review-<block>.md: a verdict table (changed sentences checked / accepted / fixed / reverted), every fix or revert as a row (file:line | editor text | your text | reason), the recall count per 1000 words with the paragraphs sampled, the decision on each open item, and any proposed errata. If recall misses exceed 2 per 1000 words in a chapter, say so plainly: that chapter gets a second pass.
- Other agents are editing other chapters, and the lead commits work in progress (HEAD moves). Touch only your files; no git commands except diff/show/log. Final message at most 10 lines.

Note: tools/invariant.py now compares the math, numbers and citations inside tables item by item, so prose in table cells (and the table pointers editors left, e.g. tab:13-window, tab:13-nuisances, tab:14-nuisances) can be fixed.
