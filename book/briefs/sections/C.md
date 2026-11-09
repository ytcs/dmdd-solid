# Writer brief: Appendix C.1–C.8 (Mathematical tools)
Read /home/user/dmdd-solid/book/briefs/sections/COMMON.md and book/REGISTER.md first. They apply in full.
- Your content brief is the SPINE.md entries C.1 to C.8 under "### Appendix C". C.9 already exists; read tex/appC/C-9.tex for voice.
- Write tex/appC/C-1.tex … C-8.tex, each starting `\section{Title}\label{app:C.n}`. In tex/appC/appC.tex, \input them in order before C-9, and remove the `\setcounter{section}{8}` line and its comment.
- **Priority.** Chapters 1 and 2 already point here for specific proofs. These must be in the text exactly as cited:
  - C.1: the limit sin²(xt/2)/x² → (πt/2)δ(x);
  - C.2: box normalization and continuum limits;
  - C.3: angular averages and the plane-wave expansion;
  - C.4: Sokhotski–Plemelj, the Hadamard finite part and Lorentzian limits;
  - C.8: the error function and the elliptic integrals that 1.2 and 1.3 use.
  Before writing, grep tex/ch01, tex/ch02 and tex/appA, D for every `\cref{app:C.n}` and the sentence around it, and make each appendix section deliver exactly what the pointing sentence promises.
- **C.5–C.7 are needed by Chapter 4 onward.** Write them in full as specified.
- **Appendix content is mathematics**, but the register rules still apply: concrete openers, no process artifacts, no "left to the reader", and every step shown.
