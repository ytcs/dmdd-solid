# Editor task: ledger merge for Chapter 20 and its App. D rows
Follow the procedure of briefs/ledger-merge-ch01-02.md.
- Merge the proposed rows of ledgers/SEAMS/20.1.md … 20.5.md, including their revision blocks and any App. D rows inside them, into NOTATION.md, GLOSSARY.md, ledgers/CONCEPTS.md, ledgers/CLAIMS.md and INDEX.md. ledgers/REVIEWS/ch20/revision.md lists the renames and new rows (f_LA; t₀ disambiguation; ε₀; f_ret; f_s/ω_opt) and the SPINE changes owed: the memory-loss times (6.8/47 ns near-top; 0.15/1.0 µs broad; ~1 µs for 22 meV TA); 0 K isotropic Al constants (6.63/3.30 km/s) and the 20.3 numbers; the golden-rule Luke rate (E.12 fixed); the FINAL 𝔯_coll band 0.81–1.02 (selective-sink 1.05–1.53 an upper envelope) and the conclusion wording; the HV ceiling (1.22; 1.36 binomial at f_det 0.873 / 1.52 full; 1.72 mean-charge); low-bias 10.8; film loss 47–58 % over 13.6–43.8Δ; the verdicts subsection cut. Also merge the Ch19 amendment (ledgers/REVIEWS/ch19/revision.md "Ch19 amendment"; t_rel) into the Ch19 SPINE/CLAIMS rows. Keep every row consistent with the revised tex: grep it.
- Apply every ruling in ledgers/REVIEWS/ch20/editor-notes.md (R1–R8 and the addendum), revision.md (including its post-check section) and postrev-check.md to the rows.
- SPINE.md:
  - Set 20.1–20.5 to ACCEPTED, and add a Chapter 20 sentence to the status paragraph at the top.
  - Apply the line → new text list at the end of ledgers/REVIEWS/ch20/revision.md ("SPINE fixes for the coordinator"), matching by text, not by line number.
- Mark the CONCEPTS/CLAIMS rows of 20.1–20.5 WRITTEN.
- Run ledgers/check_notation.py on tex/ch20 and fill the gaps. Run ledgers/check_concepts.py until it reports 0 violations.
- Then add \input{ch20/ch20} after ch19 in tex/gate.tex (s20-summary is input by ch20.tex). Build the gate with latexmk -pdf -interaction=nonstopmode -outdir=/tmp/claude-0/build-gate20 gate.tex. Copy the PDF to releases/book-gate-ch20.pdf and delete releases/book-gate-ch19.pdf (keep one gate PDF). Report the page count and any undefined references.
Use exact, small Edit replacements and re-read before each. Do not commit. Final message ≤ 8 lines.
