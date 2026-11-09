# R17 brief CW8-LIT: literature, novelty and data closures

## Target
Close LOOSE-ENDS rows **LE-135, 158, 161, 162, 163** (literature and novelty) and **LE-10, 11** (data). Also verify the PDG [FT] claim behind LIMITS L-D11′ (CW3-errata). Read each row's text in /home/user/dmdd-solid/state/LOOSE-ENDS.md.

## Required
1. **LE-161: a novelty and priority register.** For every claim tagged NEW, "appears new", "first" or similar in the authoritative returns and the R16 returns, run a priority search: lit.py search/theorems/works and INSPIRE citation walks.
   - Record each result as NONE FOUND (searched: queries and dates) or PRIOR ART (citation with equation).
   - Write it to /home/user/dmdd-solid/state/NOVELTY.md.
   - Include LE-135 (DM–TLS) and LE-158 (WP8-F per-mass re-derivations).
2. **LE-162, LE-163: source verification.** For every UNRESOLVED, [ABS]-only or [UNVERIFIED] source quote these rows list, fetch the open full text and verify the quote with page and equation, then retag it [FT].
   - Where no open full text exists, keep [UNVERIFIED] and note "closed access".
   - Classic textbooks (Hecht, Pines, Haldane, Braun–Kivshar, …): verify via an open edition or a later [FT] paper that quotes the equation, or mark them textbook-standard with the edition.
3. **LE-10, LE-11, data.**
   - Al and Ir elastic constants: measured C_ij [FT] or NIST/handbook.
   - YIG lattice constant: experimental, [FT]/COD.
   - Put the values in a new data file /home/user/dmdd-solid/state/DATA-ADDENDA.csv, using the WP8-U table columns. Do not edit table v4.

## Edit only
- state/NOVELTY.md (new) and state/DATA-ADDENDA.csv (new);
- the status cells of those LE rows in state/LOOSE-ENDS.md;
- the source tags of the affected LIMITS.md rows;
- returns/R17/CW8-LIT-log.md (new).

## Rules
- You act for the coordinator and may edit only the files named in your brief.
- Follow CONVENTIONS and NOTATION.
- Literature via /home/user/dmdd-solid/skills/breakthrough-maths/scripts/lit.py into /home/user/dmdd-solid/literature/papers-<ID>/. Verify every arXiv ID against the API. INSPIRE for citation walks. Delete the PDFs at the end.
- Do not commit. Write a log file: returns/R17/<ID>-log.md, recording every edit as file → section → source.
- Final message ≤ 12 lines.
