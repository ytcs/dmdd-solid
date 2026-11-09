# R16 brief CMPMC-DEV: bring CMPMC to state of the art (user: "I want it to be SOTA")

## Target
Implement the prioritised "SOTA upgrade list" in /home/user/dmdd-solid/returns/R15/CMPMC-AUD.md in the campaign-owned repo /home/user/cmpmc. Work on branch `paer-sota`, which now equals main at cd56e1b; `git checkout paer-sota` first. Then fix the audit's DO-NOT-USE modules where that is feasible: the IV Matrix model (×4 over Jacoboni–Reggiani in Si), bulk 3D-QP transport, and the shortcut engines (jump-to-ballistic, fast-chord HV Luke, NEE, SoA/GPU). Each must reproduce the reference path to a stated tolerance, or stay marked unsupported with a runtime guard.

## Required
- One physics change per git commit. The message cites the formula source: a campaign equation and/or an [FT] paper with equation number (fetch it; tag it).
- Every change ships with a CTest test in tests/, registered in CMakeLists.txt, against a closed form, published data or an independent numeric route. Existing tests must keep passing. Physics constants come from [FT]/[DB] sources, never demo values; the surface down-conversion coefficients are currently G4CMP demo values.
- Keep the campaign theory consistent: WP2-v3 phonons, WP5-v4 cascade, WP7-E-v3 ledger (E9)–(E12), WP8-R §2–§3, and the WP8-R referee points (referees/R14/REF-WP8-R-A.md, -B.md: frequency-dependent pair-breaking η_pb(Ω) with film loss, and soft ballistic gap phonons from surface recombination).
- Update README.md and PLAN.md to state what is validated and against what, plus a VALIDATION.md table: module → test → reference → tolerance.
- Work in priority order. Stop at any item whose implementation would need more than ~2 h of work, and write its design note instead.
- Multi-core runs only via /home/user/dmdd-solid/code/run-heavy.sh. Build dirs in /root/.
- Do NOT push and do not touch main; the coordinator verifies and merges.
- Literature via /home/user/dmdd-solid/skills/breakthrough-maths/scripts/lit.py into /home/user/dmdd-solid/literature/papers-CMPMC-DEV/. Delete the PDFs.

## Return
/home/user/dmdd-solid/returns/R16/CMPMC-DEV.md (≤ 300 lines): per item, done/designed/skipped with the commit hash, the test, and the validation numbers; the final ctest summary; and the remaining items. Final message ≤ 15 lines.
