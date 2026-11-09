# R16 closure brief CW7: close the loose ends assigned to CW7

## Target
The user: "resolve all leftover items, we want to close all loose ends before entering the writing stage." Close every row assigned to **CW7** in /home/user/dmdd-solid/state/LOOSE-ENDS.md §2 (read §1 for the rows, §1b and §3 for context). Deliverable directive (STATEMENT.md, user 2026-11-01): the book derives all theory and formulae; heavy numerics are not required if the quantity is derived and explained clearly, so a compute row is closed by (i) a clear derivation of the quantity and (ii) a complete computation specification (inputs, grids, cost; written for the qe-rtsc fork layout, /home/user/dmdd-solid/code/ENV.md). Run nothing heavy unless the row is marked compute-in-box.

CW7 also produces the WP8-U and WP8-F revisions (LE-19, LE-21): returns/R16/WP8-U-v2.md (+ WP8-U-table-v3.csv building on returns/R14/WP8-U-table-v2.csv and WP8-U-top.md) and returns/R16/WP8-F-v2.md, standalone, absorbing referees/R14/REF-WP8-U-{A,B}.md, REF-WP8-F-{A,B}.md (read them) and the WP8-F rulings of returns/R14/WP5-AUD.md, each with a closing table (one row per referee item). Use returns/R14/GAP-EF.md if present for ε_eh/F_eh.

**Computational connection (user):** the book explains how quantities such as form factors are computed (appendix on ab initio methods), without running them first. Every compute-formulate specification must also say, in prose a reader can follow, what is computed, which approximation (expansion-hierarchy level) it embodies, the method, its key convergence parameters and its pitfalls.

## Required, per row
- State the item, then close it to the row's closure criterion: a derivation [D] with hypotheses (sympy/numpy-checked where algebraic), a literature verification [FT] (fetched and quoted with page/equation), a data value with provenance, or an **exact remaining gap** (the strongest derived statement + the single missing step + its computation specification). "Not done" is not a closure.
- Mark each row CLOSED / CLOSED-AS-EXACT-GAP / CANNOT-CLOSE (with reason). Where a closure changes a refereed result, give the exact replacement text and its target (return §, LIMITS row, NOTATION row) as an owed correction; do not edit those files.
- Book-readiness: write each derivation clearly enough to become a textbook passage (hypotheses, steps, limits, leading correction).

## Read
/home/user/dmdd-solid/state/LOOSE-ENDS.md, the sources each row cites (returns/R8/*-v3.md, returns/R12/*, returns/R13/*, LIMITS.md, SOTA.md as cited), /home/user/dmdd-solid/CONVENTIONS.md, /home/user/dmdd-solid/NOTATION.md, /home/user/dmdd-solid/CONTROLS.md. Do not read referees/ unless a row cites a specific report.

## Rules
- Checks in /home/user/dmdd-solid/code/CW7/checks.py (≤ 2 min, must pass). Multi-core jobs only via /home/user/dmdd-solid/code/run-heavy.sh.
- Literature via /home/user/dmdd-solid/skills/breakthrough-maths/scripts/lit.py into /home/user/dmdd-solid/literature/papers-CW7/; verify every arXiv ID; delete PDFs at the end. INSPIRE for citation walks.
- Follow CONVENTIONS (incl. R13 amendments, [CALC] tag) and NOTATION; new symbols only in the closing 'Symbols' section.
- Write only /home/user/dmdd-solid/returns/R16/CW7.md (≤ 700 lines) and code/CW7/. Do not commit. Do not edit any other file.
- Start with a closure table (row → status → location in the return). End with 'Symbols introduced/used', 'Interface flags', 'Owed corrections' (target → exact text), 'Proposed LIMITS rows'.
- Final message ≤ 15 lines.
