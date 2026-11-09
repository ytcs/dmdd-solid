# Editor task: ledger merge for Chapter 21 and its App. D rows
Follow the procedure of briefs/ledger-merge-ch01-02.md.
- Merge the proposed rows of ledgers/SEAMS/21.1.md … 21.7.md, including their revision blocks and any App. D rows inside them, into NOTATION.md, GLOSSARY.md, ledgers/CONCEPTS.md, ledgers/CLAIMS.md and INDEX.md. ledgers/REVIEWS/ch21/revision.md lists the renames, the new rows (NOTATION Ch21 block, clash entry 93) and the SPINE changes owed. Key values to carry: one Neyman construction chapter-wide (profiled factor 1.427; WE 21.4 1.24e-41 nominal, band 8.38e-42–1.84e-41, profiled 1.77e-41 / 1.54e-41 one-sided); pair bins from the Ch18 cascade (σ_lim 3.72e-42 at 10 MeV, ×2.12 / ×3.70; leakage ≤ 0.035); cold-gap double count removed (10.10 central 1.85e4, band 1.25e4–2.75e4 — update the Ch10 rows too); ²¹⁰Pb 724 per kg·d·keV per Bq/kg, budget 1.38 mBq/kg (Hayen Eq. 6, prefactor 4). Also merge D.46 and D.47 rows and the E.27 fixes. Keep every row consistent with the revised tex: grep it.
- Apply every ruling in ledgers/REVIEWS/ch21/editor-notes.md (R1–R8), revision.md (including its post-check section) and postrev-check.md to the rows.
- SPINE.md:
  - Set 21.1–21.7 to ACCEPTED, and add a Chapter 21 sentence to the status paragraph at the top.
  - Apply the line → new text list at the end of ledgers/REVIEWS/ch21/revision.md ("SPINE fixes for the coordinator"), matching by text, not by line number.
- Mark the CONCEPTS/CLAIMS rows of 21.1–21.7 WRITTEN.
- Run ledgers/check_notation.py on tex/ch21 and fill the gaps. Run ledgers/check_concepts.py until it reports 0 violations.
- Then add \input{ch21/ch21} after ch20 in tex/gate.tex (s20-summary is input by ch21.tex). Build the gate with latexmk -pdf -interaction=nonstopmode -outdir=/tmp/claude-0/build-gate21 gate.tex. Copy the PDF to releases/book-gate-ch21.pdf and delete releases/book-gate-ch20.pdf (keep one gate PDF). Report the page count and any undefined references.
Use exact, small Edit replacements and re-read before each. Do not commit. Final message ≤ 8 lines.
