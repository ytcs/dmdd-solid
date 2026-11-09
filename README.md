# dmdd-solid: dark-matter direct detection in solids

The theory, formulae and numbers for dark-matter scattering and absorption in crystals and other solid targets, with the book that derives them: *book/releases/book-full.pdf* (22 chapters, appendices A–F, 1842 pages). The work began as a research campaign on phonon-assisted electron recoil (PAER) in silicon and germanium and grew to cover the electronic, lattice, magnetic, superconducting and detector-response channels.

**Status (2026-11-09).** The book is complete. Most of the heavy numerical work it specifies has not been run: **OWED.md** tracks every calculation still owed.

## Layout
Start with STATEMENT.md (goal and tiers), DONE.md (done condition and verification ladder), RULES.md
(machine and process rules) and log.md (history). The current understanding is state/SOTA.md.

| Path | What |
|---|---|
| STATEMENT.md | the target: theory, computable formula and Si numbers for phonon-assisted DM–electron scattering |
| DONE.md | tiers, verification ladder, minimum budget |
| CONVENTIONS.md | authoritative conventions (units, signs, normalisations, halo, vocabulary) |
| NOTATION.md | symbol table (v3+); overrides every other file |
| OWED.md | calculations still owed: status of every deferred, partial and book-requested calculation; update it when a result lands |
| state/CORRECTIONS.md | index of owed corrections per return and site: read it before quoting a return |
| FRAMEWORK.md, LIMITS.md | URF work-package plan; ledger of literature formulas recovered as limits |
| CONTROLS.md | control cases every derivation and computation must pass |
| RULES.md | local-machine limits, firewall, literature policy |
| registry.md | approach families with status |
| LAUNCHES.md | round-by-round launch log |
| log.md | dated history and decisions |
| briefs/<round>/ | briefs, one per agent |
| returns/<round>/ | returns: arguments, not results (see state/SOTA.md). returns/R6/*-v2.md are the revised, refereeable packages; returns/R6/AUDIT.md is the cross-package audit |
| referees/<round>/ | isolated hostile referee reports |
| literature/ | priority check and the literature map (surveys/dm-solid-state-scattering.md is the field survey) |
| code/ | scripts behind every number (short, rerunnable) |
| book/ | the book: tex/, figscripts/, ledgers/, releases/book-full.pdf; resume point in book/RESUME.md |
| surveys/ | the field surveys the campaign started from |
| skills/ | the protocols the work ran under: breakthrough-maths (research campaign, with scripts/lit.py for literature) and long-form-writing (book production) |
| state/SOTA.md | what is currently established, with status per claim |

Origin: the gap identified in surveys/dm-solid-state-scattering.md §4(c), for which no prior calculation was found.
