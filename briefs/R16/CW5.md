# R16 closure brief CW5: close the loose ends assigned to CW5

## Target
The user: "resolve all leftover items, we want to close all loose ends before entering the writing stage." Close every row assigned to **CW5** in /home/user/dmdd-solid/state/LOOSE-ENDS.md §2 (read §1 for the rows, §1b and §3 for context). Deliverable directive (STATEMENT.md, user 2026-11-01): the book derives all theory and formulae; heavy numerics are not required if the quantity is derived and explained clearly, so a compute row is closed by (i) a clear derivation of the quantity and (ii) a complete computation specification (inputs, grids, cost; written for the qe-rtsc fork layout, /home/user/dmdd-solid/code/ENV.md). Run nothing heavy unless the row is marked compute-in-box.

Include the queued GAP-LEE scope (predictive LEE model; zero-field gap-energy release law, now UNRESOLVED per the R14 WP8-R referees). Use returns/R14/WP5-AUD.md, its referee reports referees/R14/REF-WP5-AUD-{A,B}.md, and returns/R14/GAP-EF.md.

**Computational connection (user):** the book explains how quantities such as form factors are computed (appendix on ab initio methods), without running them first. Every compute-formulate specification must also say, in prose a reader can follow, what is computed, which approximation (expansion-hierarchy level) it embodies, the method, its key convergence parameters and its pitfalls.

## Required, per row
- State the item, then close it to the row's closure criterion: a derivation [D] with hypotheses (sympy/numpy-checked where algebraic), a literature verification [FT] (fetched and quoted with page/equation), a data value with provenance, or an **exact remaining gap** (the strongest derived statement + the single missing step + its computation specification). "Not done" is not a closure.
- Mark each row CLOSED / CLOSED-AS-EXACT-GAP / CANNOT-CLOSE (with reason). Where a closure changes a refereed result, give the exact replacement text and its target (return §, LIMITS row, NOTATION row) as an owed correction; do not edit those files.
- Book-readiness: write each derivation clearly enough to become a textbook passage (hypotheses, steps, limits, leading correction).

## Read
/home/user/dmdd-solid/state/LOOSE-ENDS.md, the sources each row cites (returns/R8/*-v3.md, returns/R12/*, returns/R13/*, LIMITS.md, SOTA.md as cited), /home/user/dmdd-solid/CONVENTIONS.md, /home/user/dmdd-solid/NOTATION.md, /home/user/dmdd-solid/CONTROLS.md. Do not read referees/ unless a row cites a specific report.

## Rules
- Checks in /home/user/dmdd-solid/code/CW5/checks.py (≤ 2 min, must pass). Multi-core jobs only via /home/user/dmdd-solid/code/run-heavy.sh.
- Literature via /home/user/dmdd-solid/skills/breakthrough-maths/scripts/lit.py into /home/user/dmdd-solid/literature/papers-CW5/; verify every arXiv ID; delete PDFs at the end. INSPIRE for citation walks.
- Follow CONVENTIONS (incl. R13 amendments, [CALC] tag) and NOTATION; new symbols only in the closing 'Symbols' section.
- Write only /home/user/dmdd-solid/returns/R16/CW5.md (≤ 700 lines) and code/CW5/. Do not commit. Do not edit any other file.
- Start with a closure table (row → status → location in the return). End with 'Symbols introduced/used', 'Interface flags', 'Owed corrections' (target → exact text), 'Proposed LIMITS rows'.
- Final message ≤ 15 lines.
