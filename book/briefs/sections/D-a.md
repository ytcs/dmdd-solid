# Writer brief: Appendix D.4, D.5, D.8, D.9, D.11 (Long derivations)
Read /home/user/dmdd-solid/book/briefs/sections/COMMON.md and REGISTER.md first; they apply in full. Build only in a private dir (-outdir=/tmp/build-D-a).
- Your content brief is the SPINE.md rows D.4, D.5, D.8, D.9 and D.11 under "### Appendix D", plus the "Appendix D map" note near the end of SPINE.md.
- Read tex/appD/D-3.tex and D-10.tex for voice. D.10 (imaginary time) and Sect. 4.7 (tex/ch04/s4-7.tex) are drafted, and D.11 builds on both, with the same 𝖦 conventions: bare 𝖦 with a real argument means the time-ordered function. 4.2 (tex/ch04/s4-2.tex) defines S, S⁰ and the FDT; D.8 and D.9 use them.
- The chapters these serve (3.4, 4.5, 4.8) are not written yet. Each D section must be self-contained: state the result in the form its chapter uses, per the SPINE entries for 3.4, 4.5 and 4.8, and derive it fully. Use \cref{sec:...} pointers to those sections for context only.
- Files: tex/appD/D-4.tex, D-5.tex, D-8.tex, D-9.tex, D-11.tex, each starting `\section{Title}\label{app:D.n}`. Edit tex/appD/appD.tex with exact Edit insertions so the numbering is correct: \input D-4 and D-5 after D-3, then `\setcounter{section}{7}% D.6–D.7 not yet written`, then D-8 and D-9, then D-10 (delete its old setcounter line), then D-11. Re-read appD.tex before each edit, because other writers may touch it.
- Ledger: ledgers/SEAMS/D-a.md. Bib: append only, with checked DOIs.
- Editor rulings in NOTATION.md apply (rates \varGamma, a₀ = 1/(αm_e), Si ε∞ = 11.7).
- Do not git commit. Report: files, word counts, build and lint status, open questions.
