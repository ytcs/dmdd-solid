# Editor task: ledger merge for Chapter 15 and its App. D rows
Follow the procedure of briefs/ledger-merge-ch01-02.md.
- Merge the proposed rows of ledgers/SEAMS/15.1.md … 15.4.md, including their revision blocks and any App. D rows inside them, into NOTATION.md, GLOSSARY.md, ledgers/CONCEPTS.md, ledgers/CLAIMS.md and INDEX.md. ledgers/REVIEWS/ch15/revision.md lists the renames (Ω_AB, 𝔴, the D.39 symbols, L^bare/L^cons) and the SPINE changes owed: the edge values (conserving, DC-41), the y < 3 cut, the two-sided remainder, the 15.2 retitle, LO(iii) of 15.1 (first-order term is bare-only), the new open items of 15.4 (phonon-assisted spin-current coherence factor; scalar absorption near the edge), the spin-current result with its R0 caveats, and the deletion of NOTATION row 1068. Keep every row consistent with the revised tex: grep it.
- Apply every ruling in ledgers/REVIEWS/ch15/editor-notes.md (R0–R11), revision.md (including its post-check section) and postrev-check.md to the rows.
- SPINE.md:
  - Set 15.1–15.4 and D.39–D.40 to ACCEPTED, and add a Chapter 15 sentence to the status paragraph at the top.
  - Apply the line → new text list at the end of ledgers/REVIEWS/ch15/revision.md ("SPINE fixes for the coordinator"), matching by text, not by line number.
- Mark the CONCEPTS/CLAIMS rows of 15.1–15.4 WRITTEN.
- Run ledgers/check_notation.py on tex/ch15 and D-39, D-40 and fill the gaps. Run ledgers/check_concepts.py until it reports 0 violations.
- Then add \input{ch15/ch15} after ch14 in tex/gate.tex, and add the accepted D.39–D.40 in order (s15-summary is input by ch15.tex). Build the gate with latexmk -pdf -interaction=nonstopmode -outdir=/tmp/claude-0/build-gate15 gate.tex. Copy the PDF to releases/book-gate-ch15.pdf and delete releases/book-gate-ch14.pdf (keep one gate PDF). Report the page count and any undefined references.
Use exact, small Edit replacements and re-read before each. Do not commit. Final message ≤ 8 lines.
