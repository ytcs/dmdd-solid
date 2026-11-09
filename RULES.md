# Operating rules

## Local machine
- **User directive (2026-11-01, deliverable):** "Btw the main deliverable is the textbook that derive all the theory and formulae, concrete numerical results that relies on heavy computation is not required as long as the quantity to compute is explained and derived clearly in the theory. The compute work can happen later unless the numerical value is important for physical reasons and/or critical to the framing or presentation of the book's narrative". Default for every computation: derive and explain the quantity, give the complete specification (qe-rtsc layout), run nothing heavy. Run in-box only when the value is physically important or narrative-critical, with the reason recorded.
- **User directive (2026-11-01):** "for computation that fits the size of your box and can be completed relatively quickly go ahead and run them. otherwise computations should be formulated but not performed (I'll provide more powerful compute once all the theory is in)". This supersedes the 10-min rule below for ab initio jobs: per job ≤ 3 h wall, ≤ 12 GB (coordinator default), run through code/run-heavy.sh; environment in code/ENV.md (QE 7.6, SG15). Larger jobs are specified, not run.
4 cores, 15 GB RAM, no GPU. Python with numpy, scipy, sympy and pyscf.
- Light computation only: scripts ≤ 10 min wall, ≤ 4 GB RAM, one heavy script at a time.
- First-principles checks: ≤ 16 atoms in pyscf (GTH pseudopotentials).
- Production EPW / ZG (tier H) needs remote compute. The RunPod connector is not authorised in this
  session, so tier H is pre-registered only.
- Scratch lives in the session scratchpad. Only the scripts and small outputs behind cited numbers go
  in code/.

## Firewall and literature
- Physics targets are not incubated (SKILL.md §12): derivation agents may use their own knowledge of the
  standard formalisms.
- Derivation agents do not search the literature for PAER itself, and do not see each other's returns.
- The literature agent works separately, with `skills/breakthrough-maths/scripts/lit.py` (fetch full
  texts), and does not see the derivations.
- Referees see only the return under review, STATEMENT, NOTATION, CONTROLS and DONE. They never see
  another referee's report.

## Process
- Returns are the historical record and are never edited. Corrections go in state/SOTA.md.
- Every number in the paper traces to a script in code/.
- This repository is self-contained: every file is tracked on `main` and committed in the ordinary way. (Before 2026-11-09 the campaign lived as an ignored directory of another repository and was committed with `add -f` on a side branch; mentions of that in older files are history.)
- Conventions (user directive, 2026-10-31): CONVENTIONS.md and NOTATION.md are authoritative across the whole campaign. Every new brief must point to them. Every return must end with a "Symbols introduced/used" table. The paper uses only standardized notation. A NOTATION-APPLY pass runs after each round that adds returns.
