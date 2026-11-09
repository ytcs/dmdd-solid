# Chapter 1 register and artifact pass (one agent)

**Files.** /home/user/dmdd-solid/book/tex/ch01/ch01.tex, s1-1.tex … s1-5.tex, /home/user/dmdd-solid/book/tex/appC/C-9.tex, /home/user/dmdd-solid/book/tex/appD/D-1.tex.

**Task.** Apply the following to every paragraph:
1. /home/user/dmdd-solid/book/REGISTER.md: the register model's voice, terms of art, characteristic moves, idiom frequencies, and the checklist. Use its 10 before → after rewrites as calibration. Fix the over-used crutches it found, such as "so", "gives", "therefore", "only" and "of order" at several times the model's rate, and change "least speed" and bare "transfers" to the field's "minimum velocity" and "momentum transfer".
2. Pattern 19, process artifacts, in /home/user/dmdd-solid/skills/long-form-writing/references/prose-review.md. Remove every sentence that exists only because of review rounds:
   - consistency assurances;
   - reviewer-directed justifications ("presented as a film value, labelled and attributed", notes on why a source's number is not quoted, "we keep … so that it can be compared");
   - fix announcements.
   Keep a convention note only where a reader comparing with the literature would be misled, and then as one clause about the literature.
3. Rule 18 (concrete openers) stays satisfied.

**Constraints.**
- Physics, numbers, equations, labels, citations and cross-references stay unchanged.
- Length within ±5%.
- Use exact-string Edit replacements only.

**When done.**
- Rebuild into a private directory: `cd /home/user/dmdd-solid/book/tex && latexmk -pdf -interaction=nonstopmode -outdir=/tmp/build-ch01reg main.tex`.
- Run the lint (`python /home/user/dmdd-solid/skills/long-form-writing/scripts/lint.py --banned /home/user/dmdd-solid/book/BANNED-TERMS.txt <file>`).
- Log a representative sample of changes (before → after, about 30) and the counts of each kind in /home/user/dmdd-solid/book/ledgers/REVIEWS/ch01/register.md.

Do not commit. Final message ≤ 6 lines.
