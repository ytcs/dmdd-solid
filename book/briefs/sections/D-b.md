# Writer brief: Appendix D.12, D.13, D.14, D.15 (Long derivations)
Read /home/user/dmdd-solid/book/briefs/sections/COMMON.md and REGISTER.md first. They apply in full. Build only in a private directory (-outdir=/tmp/build-D-b).
- Your content brief: the SPINE.md rows D.12, D.13, D.14, D.15 under "### Appendix D", plus the "Appendix D map" note near the end of SPINE.md. D.12 (BSE from the ladder) builds on D.11 (Wick and Feynman rules, drafted) and Sect. 4.7 (drafted). D.13–D.15 serve Chapters 5–6 (not written), so read their SPINE entries.
- Read tex/appD/D-10.tex and D-11.tex for voice and conventions (𝖦, Matsubara, diagram rules). Each D section is self-contained. It states the result in the form its chapter uses (see that chapter's SPINE entry) and derives it fully. Use \cref{sec:...} pointers to the chapters only for context.
- Files: tex/appD/D-12.tex … D-15.tex, each starting `\section{Title}\label{app:D.n}`. Insert the \input lines into tex/appD/appD.tex in order after D-11 with exact Edit insertions, re-reading the file first; another D writer edits it in parallel. Keep the numbering correct.
- Ledger: ledgers/SEAMS/D-b.md. Bib: append only, with DOIs checked. Check numbers with a script, figscripts/appD/check_D_b.py.
- Editor rulings in NOTATION.md apply (rates \varGamma, a₀ = 1/(αm_e), Si ε∞ = 11.7, γ^G for Grüneisen parameters, γ_{Qν} for linewidth).
- Cite textbooks at chapter level only if you have checked the chapter; otherwise cite the book alone.
- Do not git commit. Report: files, word counts, build and lint status, open questions.
