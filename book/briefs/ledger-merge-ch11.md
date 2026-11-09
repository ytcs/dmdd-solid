# Editor task: ledger merge for Chapter 11 and its App. D rows
Follow the procedure of briefs/ledger-merge-ch01-02.md. Merge the proposed rows (including revision blocks) of ledgers/SEAMS/11.1.md … 11.9.md (including their revision blocks and any App. D rows inside them; see ledgers/REVIEWS/ch11/revision.md) into NOTATION.md, GLOSSARY.md, ledgers/CONCEPTS.md, ledgers/CLAIMS.md and INDEX.md. Rename clashes per NOTATION and the editor rulings, and keep every row consistent with the revised tex (grep it).
- SPINE.md: set 11.1–11.9 and their App. D derivations (D.31–D.32) to ACCEPTED.
- Run ledgers/check_notation.py on tex/ch11 and the App. D files Ch11 owns, fill the gaps, and run ledgers/check_concepts.py until it reports 0 violations.
Other agents edit tex/ch12 (Ch12 under review), and also append to NOTATION.md now and then. Use exact, small Edit replacements and re-read before each. Do not commit. Final message ≤ 8 lines.
Also:
- Apply every ruling in ledgers/REVIEWS/ch11/editor-notes.md and revision.md to the rows.
- Mark 11.1–11.9's CONCEPTS/CLAIMS WRITTEN.
- Then add tex/ch11 (and the accepted App. D files) to tex/gate.tex in order and build the gate PDF: latexmk in a private outdir (/tmp/build-gate11), copy the PDF to releases/book-gate-ch11.pdf, and delete releases/book-gate-ch08.pdf so at most 2 PDFs remain. Report the page count and any undefined references.
- NOTATION already has 33 Ch11 rows and clash entry 80 from the reviser (ledgers/REVIEWS/ch11/revision.md); verify, don't duplicate.
