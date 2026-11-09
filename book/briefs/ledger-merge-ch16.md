# Editor task: ledger merge for Chapter 16 and its App. D rows
Follow the procedure of briefs/ledger-merge-ch01-02.md.
- Merge the proposed rows of ledgers/SEAMS/16.1.md … 16.9.md, including their revision blocks and any App. D rows inside them, into NOTATION.md, GLOSSARY.md, ledgers/CONCEPTS.md, ledgers/CLAIMS.md and INDEX.md. ledgers/REVIEWS/ch16/revision.md lists the renames and new rows (clash entry 87; ε_pub; v_D = 3.02e-3) and the SPINE changes owed: the 16.9 retitle ("Material inputs of the novel targets"); the 1608.02940 arXiv equation numbering; 16.2 now cites DLMF for I₀, K₀ (not App. C.8); the ZrTe₅ central row (11.8 meV, whole row); the DM–TLS rate 2.3e-2; the corrected published values (Dirac ε_bg, Blanco Eq. (6), Du (E_eff/E₀)², Liu Born validity, Meißner factor, Qureshi factor) with no novelty wording. Keep every row consistent with the revised tex: grep it.
- Apply every ruling in ledgers/REVIEWS/ch16/editor-notes.md (R1–R13), revision.md (including its post-check section) and postrev-check.md to the rows.
- SPINE.md:
  - Set 16.1–16.9 and D.41–D.42 to ACCEPTED, and add a Chapter 16 sentence to the status paragraph at the top.
  - Apply the line → new text list at the end of ledgers/REVIEWS/ch16/revision.md ("SPINE fixes for the coordinator"), matching by text, not by line number.
- Mark the CONCEPTS/CLAIMS rows of 16.1–16.9 WRITTEN.
- Run ledgers/check_notation.py on tex/ch16 and D-41, D-42 and fill the gaps. Run ledgers/check_concepts.py until it reports 0 violations.
- Then add \input{ch16/ch16} after ch15 in tex/gate.tex, and add the accepted D.41–D.42 in order (s16-summary is input by ch16.tex). Build the gate with latexmk -pdf -interaction=nonstopmode -outdir=/tmp/claude-0/build-gate16 gate.tex. Copy the PDF to releases/book-gate-ch16.pdf and delete releases/book-gate-ch15.pdf (keep one gate PDF). Report the page count and any undefined references.
Use exact, small Edit replacements and re-read before each. Do not commit. Final message ≤ 8 lines.
