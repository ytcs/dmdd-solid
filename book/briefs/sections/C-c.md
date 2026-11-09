# Writer brief: Appendix C.18–C.20 (Mathematical tools)
Read /home/user/dmdd-solid/book/briefs/sections/COMMON.md and REGISTER.md first; they apply in full. Build only in a private dir (-outdir=/tmp/build-C-c).
- Your content brief is the SPINE.md rows C.18 to C.20 under "### Appendix C". Read tex/appC/C-5.tex and C-9.tex for voice. Each section gives the mathematics its "Used by" chapters need, in the form they use it. Those chapters are not written yet, so read their SPINE entries to learn which form that is.
- Files: tex/appC/C-18.tex … C-20.tex, each starting `\section{Title}\label{app:C.n}`. In tex/appC/appC.tex, \input them in order after C-17, using exact Edit insertions.
- The register rules still apply: concrete openers, every step shown, nothing left to the reader, citations for attribution only.
- Ledger: ledgers/SEAMS/C-c.md. Bib: append only, with checked DOIs.
- Do not git commit. Report: files, word counts, build and lint status, open questions.
- Heisenberg and spin conventions: follow the NOTATION editor rulings (pairs counted once, J > 0 antiferromagnetic).
