# Chapter 1 opener pass (small, targeted)
Apply rule 18 of /home/user/dmdd-solid/skills/long-form-writing/references/prose-review.md (abstract category frames, count-teasers, recap openers) to every chapter, section, subsection and paragraph opening sentence in /home/user/dmdd-solid/book/tex/ch01/*.tex, appC/C-9.tex and appD/D-1.tex. Examples to fix:
- s1-3 "Two consequences need no knowledge of the target."
- "Two momentum scales of the target decide what these transfers probe."
- "The energy side has two scales as well."
- "The kinematics treats the two kinds differently."
- s1-4 "Three bosons are standard."
- s1-2 "Two effects are left out of …"
- s1-5's opener "The previous sections fixed …"

Rewrite only the offending sentences, minimally: name the members, or open with the concrete question. Keep the physics, numbers and length unchanged (±1%). Change nothing else.

After editing, rebuild with `cd book/tex && latexmk -pdf -interaction=nonstopmode -outdir=../build main.tex` and run the lint. List every change (before → after) in /home/user/dmdd-solid/book/ledgers/REVIEWS/ch01/openers.md. Do not commit. Final message ≤ 6 lines.
