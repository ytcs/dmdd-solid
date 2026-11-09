# Writer brief: Appendix D.16, D.17, D.18, D.19, D.20, D.21, D.22, D.23 (Long derivations)
Read /home/user/dmdd-solid/book/briefs/sections/COMMON.md and REGISTER.md first. They apply in full. Build only in a private directory (-outdir=/tmp/build-D-c).
- Your content brief: the SPINE.md rows D.16, D.17, D.18, D.19, D.20, D.21, D.22, D.23 under "### Appendix D", plus the "Appendix D map" note near the end of SPINE.md. D.16–D.18 (AHC, phonon self-energy, phonon-assisted absorption) build on D.10, D.11 and Sect. 4.7. D.19–D.23 serve Chapter 7. Heisenberg convention: the NOTATION editor ruling (pairs counted once, J > 0 antiferromagnetic, one-magnon ω = |S|[J(Q) − J(0)]) is binding for D.19.
- Read tex/appD/D-10.tex and D-11.tex for voice and conventions (𝖦, Matsubara, diagram rules). Each D section is self-contained. It states the result in the form its chapter uses (see that chapter's SPINE entry) and derives it fully. Use \cref{sec:...} pointers to the chapters only for context.
- Files: tex/appD/D-16.tex … D-23.tex, each starting `\section{Title}\label{app:D.n}`. Insert the \input lines into tex/appD/appD.tex in order after D-11 with exact Edit insertions, re-reading the file first; another D writer edits it in parallel. Keep the numbering correct.
- Ledger: ledgers/SEAMS/D-c.md. Bib: append only, with DOIs checked. Check numbers with a script, figscripts/appD/check_D_c.py.
- Editor rulings in NOTATION.md apply (rates \varGamma, a₀ = 1/(αm_e), Si ε∞ = 11.7, γ^G for Grüneisen parameters, γ_{Qν} for linewidth).
- Cite textbooks at chapter level only if you have checked the chapter; otherwise cite the book alone.
- Do not git commit. Report: files, word counts, build and lint status, open questions.
