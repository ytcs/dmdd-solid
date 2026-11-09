# Editor task: ledger merge for Chapter 14 and its App. D rows
Follow the procedure of briefs/ledger-merge-ch01-02.md.
- Merge the proposed rows of ledgers/SEAMS/14.1.md … 14.6.md, including their revision blocks and any App. D rows inside them, into NOTATION.md, GLOSSARY.md, ledgers/CONCEPTS.md, ledgers/CLAIMS.md and INDEX.md. ledgers/REVIEWS/ch14/revision.md lists the renames the reviser applied (Ω_ion, g_ion, 𝗁, ω_gap, δ_mp, ω_soft/γ_soft, Γ_tg, M_sw; λ_S row fixed). It also lists SPINE fixes owed: 14.3 Chigusa Eq. (35) → the equations cited in the text; 14.4 g_J → g_ion; the 14.6 summary file. Keep every row consistent with the revised tex: grep it.
- Apply every ruling in ledgers/REVIEWS/ch14/editor-notes.md (R1–R10), revision.md (including its post-check section) and postrev-check.md to the rows.
- SPINE.md:
  - Set 14.1–14.6 and D.38 to ACCEPTED, and add a Chapter 14 sentence to the status paragraph at the top.
  - Apply the line → new text list at the end of ledgers/REVIEWS/ch14/revision.md ("SPINE fixes for the coordinator"), matching by text, not by line number.
- Mark the CONCEPTS/CLAIMS rows of 14.1–14.6 WRITTEN.
- Run ledgers/check_notation.py on tex/ch14 and D-38 and fill the gaps. Run ledgers/check_concepts.py until it reports 0 violations.
- Then add \input{ch14/ch14} after ch13 in tex/gate.tex, and add the accepted D.38 in order (s14-summary is input by ch14.tex). Build the gate with latexmk -pdf -interaction=nonstopmode -outdir=/tmp/claude-0/build-gate14 gate.tex. Copy the PDF to releases/book-gate-ch14.pdf and delete releases/book-gate-ch13.pdf (keep one gate PDF). Report the page count and any undefined references.
Use exact, small Edit replacements and re-read before each. Do not commit. Final message ≤ 8 lines.
