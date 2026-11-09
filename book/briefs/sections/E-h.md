# Writer brief: Appendix E.25–E.27 (computational specifications)
Read /home/user/dmdd-solid/book/briefs/sections/COMMON.md and REGISTER.md first. They apply in full, including the compute policy: write specifications only and run nothing. Build in a private directory only (-outdir=/tmp/build-E-h).
- Your content brief: the SPINE.md rows E.25 to E.27 in the block "Sections E.14–E.27: computational specifications" (read the block header too), and, for each row, the planning items in /home/user/dmdd-solid/state/DEFERRED-COMPUTE.md that its writer-only "DC" list names. Read each DC item together with the source specification it names.
- Every section is a standalone specification that a computational group could execute. For each quantity it gives:
  - the physics and the book section that defines it (\cref);
  - the exact quantity and its units;
  - the method and approximation level (its place on the truncation label 𝔗, \cref{sec:8.5});
  - inputs and codes;
  - grids and convergence parameters, with the acceptance test (a sum rule, a measured control or a stated benchmark);
  - cost (core-hours, memory);
  - pitfalls;
  - where the result enters the book.
  Write it as argued prose. Tables are welcome for parameters. Do not use step-by-step recipe lists.
- The text must contain NO internal labels: no "DC-n", "LE-n", "CW", "WP", "COMP-", "[CALC]" or campaign vocabulary (see BANNED-TERMS.txt). Point by content to the book sections listed in each row's "(→ …)" and [N.M] tags; most of them are not written yet, so use \cref{sec:N.M} labels.
- Read tex/appE/appE.tex, E-1.tex and E-4.tex for voice. The methods sections E.1–E.13 are accepted; point to them for method background rather than repeating it.
- Files: tex/appE/E-25.tex … E-27.tex, each starting `\section{Title}\label{app:E.n}`. Insert the \input lines into tex/appE/appE.tex in order with exact Edit insertions, re-reading the file first, because other E writers edit it in parallel.
- Ledger: ledgers/SEAMS/E-h.md. Bib: append only, with checked DOIs.
- Editor rulings in NOTATION.md apply.
- Do not git commit. Report: files, word counts, build and lint status, and any DC item you could not place.
