# Writer brief: Appendix E.4, E.5, E.6 (ab initio methods)
Read /home/user/dmdd-solid/book/briefs/sections/COMMON.md and book/REGISTER.md first. They apply in full.
- **Content:** the SPINE.md entries E.4, E.5, E.6 under "### Appendix E". Write tex/appE/E-4.tex, tex/appE/E-5.tex, tex/appE/E-6.tex, each starting `\section{Title}\label{app:E.n}`.
- **Purpose (user directive).** The book explains how each material quantity is computed, without running the calculations. Each section builds the method up for a first-year PhD reader (READER.md):
  - what is computed;
  - which approximation it embodies, mapped to the book's expansion hierarchy (Chap. 8 by planned label);
  - the convergence parameters;
  - typical cost;
  - pitfalls;
  - silicon as the worked case.
  Concrete, plain prose. No code listings beyond a few-line input sketch where it clarifies.
- **Accuracy.** Methods are standard, but every claim about a method's accuracy or cost is either derived or cited (citation as credit; the statement itself is in the text).
- **Grounding material (yours only, never named in the book):** /home/user/dmdd-solid/code/ENV.md (the codes and the convergence experience), returns/R15/COMP-PH.md and COMP-PAER.md (real convergence tables for Si and Ge), and state/DEFERRED-COMPUTE.md (what each method is used for).
- **Concurrency.** Three other writers do the other Appendix E groups in parallel. Do not edit tex/appE/appE.tex; the editor assembles it. Edit book.bib only with small exact insertions.
