# Chapter 11 revision (one reviser)
Revise tex/ch11/ch11.tex and s11-1.tex … s11-9.tex (the Summary is at the end of s11-9), and tex/appD/D-31.tex and D-32.tex. All paths are under /home/user/dmdd-solid/book. Edit only these files (plus figscripts/ch11 logs and NOTATION.md clash entries); 12.4–12.6 writers are working in tex/ch12 in parallel. Do not commit. Final message ≤ 10 lines.
Address every item of the five reports in ledgers/REVIEWS/ch11/ (derivation-1.md, derivation-2.md, prose.md, reader-a.md, reader-b.md) and of ledgers/REVIEWS/ch11/editor-notes.md, which binds you.
Follow COMMON.md (compute policy: rerun only the existing figscripts/ch11 Python scripts, no QE), PARTII.md, STYLE.md, REGISTER.md, NOTATION.md and READER.md.

## Editor rulings
All rulings R1–R12 in ledgers/REVIEWS/ch11/editor-notes.md bind you. Also:
- **Prose (prose.md):**
  - cut the multi-sentence "We will…" roadmaps at section openers to one sentence;
  - cut the chapter opening's paragraph 2 to one sentence;
  - de-duplicate 11.9 (nuisances stated once: table plus one prose pass) and the five repeats of the ε∞ 26 %/37 % point;
  - use American spelling ("modeling");
  - drop the "(modelling choice)" tags.
- **Notation:**
  - Register every new symbol the reviews list; resolve the O_A, 𝔫_κ and c_κ clashes against NOTATION and add clash entries.
  - Define every symbol inside each Limit Check box in book notation, not the source's.
  - An upright Γ never denotes a rate.
- **Numbers:** apply every WRONG item from derivation-1/2 and the slips the readers found (1.76 q_BZ for G₁₁₁, 2.84 q₀, the ±0.2 % E_kin range, the 140 vs 90 keV impulse-onset consistency, and so on). For every GAP number, rerun the existing figscripts/ch11 scripts so that the value lands in a log, or drop the number.
- **Content:**
  - 11.6 must not point forward to 11.8 for a cancellation it derives itself.
  - Slow down the certified band (11.3) and the Markov–Krein band (11.5) enough to follow without App. C.10: one worked line each.
  - D.32: prove, or state, that all five moments hold at any temperature.
