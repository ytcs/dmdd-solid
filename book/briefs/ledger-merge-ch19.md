# Editor task: ledger merge for Chapter 19 and its App. D rows
Follow the procedure of briefs/ledger-merge-ch01-02.md.
- Merge the proposed rows of ledgers/SEAMS/19.1.md … 19.6.md, including their revision blocks and any App. D rows inside them, into NOTATION.md, GLOSSARY.md, ledgers/CONCEPTS.md, ledgers/CLAIMS.md and INDEX.md. ledgers/REVIEWS/ch19/revision.md lists the renames and new rows (clash entry 91; g_Luke book-wide; ~70 new rows) and the SPINE changes owed: the 19.1 retitle; the binary threshold 352/399 eV; the two-ε calibration chain (𝔯_coll 1.128 [1.099, 1.152]; bound 0.055 with condition (e), 0.049 with the book ε; collection-only disfavoured on present transport estimates; the 𝔯_coll sign open per 20.5); the calibration machinery lives in 19.5 (merged Limit Check 19.5b); the 19.3 sensitivity framing; the displacement factor 0.70; the 19.6a validity (T ≥ 0.28 band widths). Keep every row consistent with the revised tex: grep it.
- Apply every ruling in ledgers/REVIEWS/ch19/editor-notes.md (R1–R8), revision.md (including its post-check section) and postrev-check.md to the rows.
- SPINE.md:
  - Set 19.1–19.6 and D.45 to ACCEPTED, and add a Chapter 19 sentence to the status paragraph at the top.
  - Apply the line → new text list at the end of ledgers/REVIEWS/ch19/revision.md ("SPINE fixes for the coordinator"), matching by text, not by line number.
- Mark the CONCEPTS/CLAIMS rows of 19.1–19.6 and D.45 WRITTEN.
- Run ledgers/check_notation.py on tex/ch19 and fill the gaps. Run ledgers/check_concepts.py until it reports 0 violations.
- Then add \input{ch19/ch19} after ch18 in tex/gate.tex (add D-45 after D-44; s19-summary is input by ch19.tex). Build the gate with latexmk -pdf -interaction=nonstopmode -outdir=/tmp/claude-0/build-gate19 gate.tex. Copy the PDF to releases/book-gate-ch19.pdf and delete releases/book-gate-ch18.pdf (keep one gate PDF). Report the page count and any undefined references.
Use exact, small Edit replacements and re-read before each. Do not commit. Final message ≤ 8 lines.
