# R13 brief WP5-ERR: apply the WP7-E amendment to WP5

## Target
WP7-E (refereed) wrote an 'Amendment to WP5-v3' (A-1..A-16) in /home/user/dmdd-solid/returns/R12/WP7-E-v3.md. Produce /home/user/dmdd-solid/returns/R13/WP5-v4.md: WP5-v3 with the amendment applied. Under the coordinator convention, ΔZPE is carried in ℋ_ph and energies are configurational.

## Required
1. Apply A-1..A-16 exactly. Where an amendment item conflicts with WP5-v3 text, WP7-E-v3 wins. Record every such conflict.
2. Check consistency against WP7-T-v2 (Theorem T-1, conditions (i)–(v)) and WP6-v3 (nuisance types).
3. Add a changelog table mapping each A-item to the WP5-v4 location.
4. Copy /home/user/dmdd-solid/code/WP5-v3/ to /home/user/dmdd-solid/code/WP5-v4/, extend it with checks for the changed equations, and rerun it.

## Read
/home/user/dmdd-solid/returns/R8/WP5-v3.md, /home/user/dmdd-solid/returns/R12/WP7-E-v3.md, /home/user/dmdd-solid/returns/R12/WP7-T-v2.md, /home/user/dmdd-solid/returns/R8/WP6-v3.md, /home/user/dmdd-solid/CONVENTIONS.md, /home/user/dmdd-solid/NOTATION.md, /home/user/dmdd-solid/state/SOTA.md (last 25 lines).

## Rules
- Theory and data compilation only. Run no new first-principles numerics such as DFT, DFPT or Monte Carlo. Closed-form estimates and sympy/numpy checks of ≤ 2 min are fine. Put the checks in /home/user/dmdd-solid/code/<ID>/checks.py, and they must pass.
- Every material property needs provenance: a database entry ID (OPTIMADE/JARVIS-DFT/COD/NIST) or a full-text quote with page/table. Tag each value [FT] (full text), [DB] (database), [E] (estimate) or [UNVERIFIED].
- Literature: use /home/user/dmdd-solid/skills/breakthrough-maths/scripts/lit.py into /home/user/dmdd-solid/literature/papers-<ID>/. Verify every arXiv ID against the API. Delete the PDFs at the end. Use INSPIRE for citation walks (OpenAlex is rate-limited).
- Do not use the Materials Project REST API (no key). Public OPTIMADE endpoints, including MP's, and JARVIS downloads are fine.
- Follow /home/user/dmdd-solid/CONVENTIONS.md and /home/user/dmdd-solid/NOTATION.md. Introduce new symbols only in the closing 'Symbols' section.
- Write only your return file and your code/ folder. Do not commit.
- End with three sections: 'Symbols introduced/used', 'Interface flags' and 'Proposed LIMITS rows'.
- Your final message is a summary of ≤ 15 lines.
