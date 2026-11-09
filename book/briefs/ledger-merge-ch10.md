# Editor task: ledger merge for Chapter 10 and its App. D rows
Follow the procedure of briefs/ledger-merge-ch01-02.md. Merge the proposed rows (including revision blocks) of ledgers/SEAMS/10.1.md … 10.10.md (including their revision blocks and any App. D rows inside them; see ledgers/REVIEWS/ch10/revision.md) into NOTATION.md, GLOSSARY.md, ledgers/CONCEPTS.md, ledgers/CLAIMS.md and INDEX.md. Rename clashes per NOTATION and the editor rulings, and keep every row consistent with the revised tex (grep it).
- SPINE.md: set 10.1–10.10 and their App. D derivations (D.29–D.32 as applicable) to ACCEPTED.
- Run ledgers/check_notation.py on tex/ch10 and the App. D files Ch10 owns, fill the gaps, and run ledgers/check_concepts.py until it reports 0 violations.
Other agents edit tex/ch11 and tex/ch12, and also append to NOTATION.md now and then. Use exact, small Edit replacements and re-read before each. Do not commit. Final message ≤ 8 lines.
Also:
- Apply every ruling in ledgers/REVIEWS/ch10/editor-notes.md and revision.md to the rows.
- Mark 10.1–10.10's CONCEPTS/CLAIMS WRITTEN.
- Then add tex/ch10 (and the accepted App. D files) to tex/gate.tex in order and build the gate PDF: latexmk in a private outdir (/tmp/build-gate10), copy the PDF to releases/book-gate-ch10.pdf, and delete releases/book-gate-ch07.pdf so at most 2 PDFs remain. Report the page count and any undefined references.
