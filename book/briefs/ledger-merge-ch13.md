# Editor task: ledger merge for Chapter 13 and its App. D rows
Follow the procedure of briefs/ledger-merge-ch01-02.md.
- Merge the proposed rows of ledgers/SEAMS/13.1.md … 13.9.md, including their revision blocks and any App. D rows inside them, into NOTATION.md, GLOSSARY.md, ledgers/CONCEPTS.md, ledgers/CLAIMS.md and INDEX.md. ledgers/REVIEWS/ch13/revision.md lists the renames the reviser applied (ς → 𝔰^(2), x/y → 𝗑/𝗒, F(q) → x_max(q), S_αβ → u_αβ, W^{scr,R}, the three-argument M^±, and the rest). Keep every row consistent with the revised tex: grep it.
- Apply every ruling in ledgers/REVIEWS/ch13/editor-notes.md (R1–R10), revision.md and postrev-check.md to the rows.
- SPINE.md:
  - Set 13.1–13.9 and D.35–D.37 to ACCEPTED, and add a Chapter 13 sentence to the status paragraph at the top.
  - Apply the line → new text list at the end of ledgers/REVIEWS/ch13/revision.md ("SPINE fixes for the coordinator"), matching by text, not by line number.
- Mark the CONCEPTS/CLAIMS rows of 13.1–13.9 WRITTEN.
- Run ledgers/check_notation.py on tex/ch13 and D-35..D-37 and fill the gaps. Run ledgers/check_concepts.py until it reports 0 violations.
- Then add \input{ch13/ch13} after ch12 in tex/gate.tex, and add the accepted D.35–D.37 in order. Build the gate with latexmk -pdf -interaction=nonstopmode -outdir=/tmp/claude-0/build-gate13 gate.tex. Copy the PDF to releases/book-gate-ch13.pdf and delete releases/book-gate-ch12.pdf (keep one gate PDF). Report the page count and any undefined references.
Use exact, small Edit replacements and re-read before each. Do not commit. Final message ≤ 8 lines.
