# Log

## 2026-10-31: setup
- Target fixed (STATEMENT.md) from the user's instruction. The gap was identified in
  surveys/dm-solid-state-scattering.md §4(c): a lit.py search, an INSPIRE citation walk of 791 papers,
  and six full texts found no prior calculation.
- Layout modelled on campaign/rtsc (physics, compute plus theory) and campaign/qg (STATEMENT / DONE /
  NOTATION / CONTROLS / registry / LAUNCHES / state).
- Local machine: 4 cores, 15 GB RAM. Installed numpy, scipy, sympy and pyscf. No LaTeX, no DFT codes.
  RunPod is not authorised, so tier H is pre-registered only.
- Kinematic window (coordinator estimate, surveys §4): Si 0.34–0.47 MeV, Ge 0.20–0.23 MeV. To be
  re-derived in N1.

## 2026-10-31: user directives
- "Hold off all numerical work, but build the theory that drives it." N1 stopped. D1 and D2 were told to
  run no numerics and to specify each computation instead. Tier B/H numbers are deferred: STATEMENT T5
  and T6 become specifications (inputs, grids, outputs) and are no longer deliverables of this phase.
- New user request: catalog the complete space of DM–solid-state processes, their importance for
  experimental analysis (exclusion plots), and the literature gaps. Launched as R1b CAT-A and CAT-B.

## 2026-10-31: R1 and R1b returns
- D1 and D2 agree term by term: amplitude, ε₂^PA prefactor, spin and Bose factors (state/SOTA.md). Rung 5 is
  satisfied by D1 ⟂ D2. R2 referees launched.
- L1: priority NONE. CATALOG-A (~95 processes) and CATALOG-B (analysis chain, 13 ranked gaps) synthesised into
  surveys/dm-solid-state-processes/ on the working branch.
- Incident: L1 deleted literature/papers/ wholesale during cleanup. CAT-B was not harmed (it had finished
  reading). Rule for future briefs: each agent downloads into its own subfolder.

## 2026-10-31: scope v2 (user directive)
- The target is now the Unified Response Framework (STATEMENT v2; v1 archived). The plan is in FRAMEWORK.md
  (WP0–WP6) and the formulas to recover are in LIMITS.md (L0–L24). M1 (PAER) continues and feeds WP3.
- Numerics remain on hold.

## 2026-10-31: user directive on conventions
- Standardise conventions and notation across the whole campaign. Running agents (WP1–WP4, O4) were asked to
  use WP0 §10 and the fixed conventions, and to append a symbol table. The NOTATION-APPLY pass is queued for
  when they return: it writes CONVENTIONS.md, NOTATION.md v3 and state/CORRECTIONS.md, plus a cross-return
  consistency audit of the key formulas. RULES.md is updated.

## 2026-10-31: user directive (second pass before hostile review)
- "Once all packages return, do a full second pass to resolve all corrections and inconsistency before hostile review passes." The R6 referees were stopped within minutes, and their partial outputs deleted. The new sequence (LAUNCHES.md): NOTATION-APPLY → REV-WP0 → REV-WP1..6 → consistency audit → R7 hostile review → synthesis.

## 2026-10-31: book plan (user directive)
- The final deliverable will be a book-length technical manuscript, not a paper. The long-form-writing skill
  was created (skills/long-form-writing on the working branch). The book spine was designed in book/SPINE.md
  (3 parts, 22 chapters, ~125 sections, ~550k words), with READER.md, BANNED-TERMS.txt and seeded ledgers.
  No writing yet. Chapters 8–22 are BLOCKED until hostile review (R7) clears; Part I can be drafted first
  when the user authorises writing.

## 2026-10-31: second pass complete; R7 launched
- Revisions, audit fixes and NOTATION v4 renames are all done and all checks pass. Committed and pushed per the user's instruction. R7 hostile review launched (14 referees).

## 2026-10-31: queued tasks (user)
- After R7 and the follow-up package (WP7): WP8, figures of merit per interaction channel and optimal
  substrate per channel within the pickable universe (thermal-cycle stable, ≥ gram-scale synthesizable,
  instrumentable). Plan in FRAMEWORK.md.

## 2026-11-01: framework review complete
- R7 hostile review, the R8 correction round, R8 verification, AUDIT-2 and the R9 clean-up are all done. All 409 checks pass. Committed and pushed.

## 2026-11-01: R13 resumed (user)
- WP8-U and WP8-R launched. WP7-E merged into LIMITS (L33–L38), NOTATION and CORRECTIONS §18, with the pending coordinator decisions recorded in CONVENTIONS §13 rows 23–28. WP5-ERR and WP8-F follow the merge commit. A joint WP5-v4 + WP7-E audit with R×2 referees (FRAMEWORK) is queued before WP8-S.
- R13 returns in: WP5-v4 (75/75), WP8-U (10 survivors + 30 conditional), WP8-F (9 FOM classes, 39/39), WP8-R (provisional NO-GO, 48/48). Committed to the campaign branch, now the single paer branch (duplicate session branches removed by the user).

## 2026-11-01: numerics hold partly lifted (user)
- "for computation that fits the size of your box and can be completed relatively quickly go ahead and run them. otherwise computations should be formulated but not performed (I'll provide more powerful compute once all the theory is in)". QE 7.6 (conda-forge) installed; the Ubuntu QE 6.7 package crashes and was removed. code/ENV.md, code/setup-env.sh, code/run-heavy.sh; tag [CALC]; per-job default ≤ 3 h, ≤ 12 GB. 'qe-fast' not found.
- S4 (intrinsic radioactivity) screening sent to WP8-U-TOP as a reversible default: budget 1 /(kg·day·keV) below 1 keV; KTaO₃ and InSb fail by orders of magnitude.

## 2026-11-01: deliverable clarified (user)
- "Btw the main deliverable is the textbook that derive all the theory and formulae, concrete numerical results that relies on heavy computation is not required as long as the quantity to compute is explained and derived clearly in the theory. The compute work can happen later unless the numerical value is important for physical reasons and/or critical to the framing or presentation of the book's narrative"
- Rescoped: COMP-PAER to the tier-B window/order-of-magnitude estimate (tier H specified, not run); COMP-PH to Si/Ge only (survivor Γ-DFPT specified); LOOSE-ENDS compute items default to formulate-only. CMPMC-AUD continues (user wants CMPMC at SOTA in its own right). CMPMC merge policy: directly into main after tests.
- User clarification (2026-11-01): "for some quantities such as form factors we definitely want to explain the computational connection in the book (maybe even worth having an appendix on ab initio methods e.g. DFT), just we don't necessarily need to actually do the computational before we write the book". SPINE: new Appendix E (ab initio methods), E′ (specifications); channel chapters' (f) explain the computational route.
- User (2026-11-01): "just the book is fine for now. Once the book is done we'll look into actually carrying out all the deferred computational work, then expand/revise the book with the numerical results". DONE amended (book only; phases 1–3); LE-173 closed.
- User (2026-11-01): "\"how to compute it\" doesn't need to be a dedicated subsection per se. we don't want to break the narrative flow too much." SPINE: the channel template is a content checklist; the computational route is woven into the text with pointers to Appendix E.

- User (2026-11-01): "keep going. when all results are validated and all loose ends are closed, begin creating the latex workspace and work on the book in accordance to the book plan and long form writing skill."
- User (2026-11-01): "No end of chapter exercises. Nothing is left to reader." SPINE: no exercises, Appendix G removed; BANNED-TERMS extended.
- User (2026-11-01): "gram scale experiment is still feasible by running multiple / stack of 0.2 g substrate". S2 redefined as total mass via arrays of ≥ ~0.1 g instrumented crystals (CONVENTIONS §13 row 38); diamond becomes a full survivor; passed to ERR-WP8 for the ranking rerun.
- User (2026-11-01): "I think this is more valuable because we want to help experimentalists identify where the next future experiment target might lie". FRAMEWORK WP8 purpose and SPINE Chap. 17 framing updated; ERR-WP8 asked for a 'next-target' readings table.
