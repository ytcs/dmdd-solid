# Editor task: ledger merge for Chapter 18 and its App. D rows
Follow the procedure of briefs/ledger-merge-ch01-02.md.
- Merge the proposed rows of ledgers/SEAMS/18.1.md … 18.5.md, including their revision blocks and any App. D rows inside them, into NOTATION.md, GLOSSARY.md, ledgers/CONCEPTS.md, ledgers/CLAIMS.md and INDEX.md. ledgers/REVIEWS/ch18/revision.md lists the renames and new rows (clash entry 89; A_AB in eV³; Ē_res, B_h) and the SPINE changes owed: the one continuum-calibrated Si set (A_AB = 5.703 eV³, E_g = 1.160 eV); F_eh 0.114 at 2.4σ (not 2.6σ); the retitles of 18.3/18.4/18.5; the linear law and validated range (residuals −19.8 to +7.0 %, model/measured − 1); the full-band reference (R19 FBC: ε 4.15 [3.95, 4.73] + ≥ ±0.4 eV, P(N≥2, 5 eV) 0.097 [0.030, 0.173], step overcount ~10× (≥ 6×)); and the Part III heading. Keep every row consistent with the revised tex: grep it.
- Apply every ruling in ledgers/REVIEWS/ch18/editor-notes.md (R1–R8), revision.md (including its post-check section) and postrev-check.md to the rows.
- SPINE.md:
  - Set 18.1–18.5 and D.43–D.44 to ACCEPTED, and add a Chapter 18 sentence to the status paragraph at the top.
  - Apply the line → new text list at the end of ledgers/REVIEWS/ch18/revision.md ("SPINE fixes for the coordinator"), matching by text, not by line number.
- Mark the CONCEPTS/CLAIMS rows of 18.1–18.5 and D.43–D.44 WRITTEN.
- Run ledgers/check_notation.py on tex/ch18 and fill the gaps. Run ledgers/check_concepts.py until it reports 0 violations.
- Then add \part{Measurement} and \input{ch18/ch18} after ch17 in tex/gate.tex (as main.tex does) (add D-43, D-44 after D-42; s18-summary is input by ch18.tex). Build the gate with latexmk -pdf -interaction=nonstopmode -outdir=/tmp/claude-0/build-gate18 gate.tex. Copy the PDF to releases/book-gate-ch18.pdf and delete releases/book-gate-ch17.pdf (keep one gate PDF). Report the page count and any undefined references.
Use exact, small Edit replacements and re-read before each. Do not commit. Final message ≤ 8 lines.
