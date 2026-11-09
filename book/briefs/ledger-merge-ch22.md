# Editor task: ledger merge for Chapter 22 and its App. D rows
Follow the procedure of briefs/ledger-merge-ch01-02.md.
- Merge the proposed rows of ledgers/SEAMS/22.1.md … 22.3.md, including their revision blocks and any App. D rows inside them, into NOTATION.md, GLOSSARY.md, ledgers/CONCEPTS.md, ledgers/CLAIMS.md and INDEX.md. ledgers/REVIEWS/ch22/revision.md lists the new rows (Λ_F extended; two 22.3 rows; clash entry 94; STYLE upright Γ) and the changes owed. Key values: tab:22-gaps 73 rows (3/10/17/38/5; missing step 55/11/7); Fig. 22.1 12/9/2; tab:22-calc covers calculations that change a printed result; ¹²⁵Te IAS 13–14 MeV, Fermi strength A−2Z = 21; Dror gamma-factor 3.22 at Z = 53; Ge row per E.14 (GW pending). Ch22 has no App. D rows. Thread T3 is closed by 22.1. Keep every row consistent with the revised tex: grep it.
- Apply every ruling in ledgers/REVIEWS/ch22/editor-notes.md (R1–R8), revision.md (including its post-check section) and postrev-check.md to the rows.
- SPINE.md:
  - Set 22.1–22.3 to ACCEPTED, and add a Chapter 22 sentence (the last chapter of Part III; book chapters complete except Ch9) to the status paragraph at the top.
  - Apply the line → new text list at the end of ledgers/REVIEWS/ch22/revision.md ("SPINE fixes for the coordinator"), matching by text, not by line number.
- Mark the CONCEPTS/CLAIMS rows of 22.1–22.3 WRITTEN.
- Run ledgers/check_notation.py on tex/ch22 and fill the gaps. Run ledgers/check_concepts.py until it reports 0 violations.
- Then add \input{ch22/ch22} after ch21 in tex/gate.tex (s22-summary is input by ch22.tex). Build the gate with latexmk -pdf -interaction=nonstopmode -outdir=/tmp/claude-0/build-gate22 gate.tex. Copy the PDF to releases/book-gate-ch22.pdf and delete releases/book-gate-ch21.pdf (keep one gate PDF). Report the page count and any undefined references.
Use exact, small Edit replacements and re-read before each. Do not commit. Final message ≤ 8 lines.
