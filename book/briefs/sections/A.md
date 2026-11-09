# Writer brief: Appendix A (Conventions and units), all sections
Read /home/user/dmdd-solid/book/briefs/sections/COMMON.md first; it applies in full.
- Your content brief is the SPINE.md entry "### Appendix A" (one assignment, about 8,000 words, sections A.1–A.n). Write it as tex/appA/A-1.tex … A-n.tex, each starting `\section{Title}\label{app:A.n}`, and \input them in tex/appA/appA.tex in order.
- **Source material, for you only:** /home/user/dmdd-solid/CONVENTIONS.md (the authoritative conventions: units, Fourier, kinematics, Bloch, phonons, response and FDT, screening, halo and rate normalisation, σ̄_e and F_DM, terminology). Make it standalone: no internal labels, decision numbers or campaign references. Every convention is stated with its reason, and with the correspondence to the conventions in common use in the literature, cited.
- **Consistency with the written text.** Chapter 1 already references app:A.1, A.2, A.3, A.4, A.8 and A.9. Read tex/ch01/*.tex and tex/appC/C-9.tex and make the appendix match what they assume:
  - natural units first used in 1.1;
  - Heaviside–Lorentz charge units;
  - metric signature (+,−,−,−);
  - kinetic-mixing sign per Lin arXiv:1904.07915 Eq. (70) (NOTATION editor decision);
  - the halo conventions of 1.2.
- **Concurrency.** Other writers work in parallel. Add your bib entries with small Edit-tool insertions.
