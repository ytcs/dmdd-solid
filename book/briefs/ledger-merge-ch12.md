# Editor task: ledger merge for Chapter 12 and its App. D rows
Follow the procedure of briefs/ledger-merge-ch01-02.md. Merge the proposed rows (including revision blocks) of ledgers/SEAMS/12.1.md … 12.6.md (including their revision blocks and any App. D rows inside them; see ledgers/REVIEWS/ch12/revision.md) into NOTATION.md, GLOSSARY.md, ledgers/CONCEPTS.md, ledgers/CLAIMS.md and INDEX.md. Rename clashes per NOTATION and the editor rulings, and keep every row consistent with the revised tex (grep it).
- SPINE.md: set 12.1–12.6 and their App. D derivations (D.33–D.34) to ACCEPTED.
- Run ledgers/check_notation.py on tex/ch12 and the App. D files Ch12 owns, fill the gaps, and run ledgers/check_concepts.py until it reports 0 violations.
Other agents (a chapter-map agent) may insert a map figure into chNN.tex files, including ch12.tex, and also append to NOTATION.md now and then. Use exact, small Edit replacements and re-read before each. Do not commit. Final message ≤ 8 lines.
Also:
- Apply every ruling in ledgers/REVIEWS/ch12/editor-notes.md and revision.md to the rows.
- Mark 12.1–12.6's CONCEPTS/CLAIMS WRITTEN.
- Then add tex/ch12 (and the accepted App. D files) to tex/gate.tex in order and build the gate PDF: latexmk in a private outdir (/tmp/build-gate12), copy the PDF to releases/book-gate-ch12.pdf, and delete releases/book-gate-ch10.pdf so at most 2 PDFs remain. Report the page count and any undefined references.
- Two small tex actions before the gate (exact Edits):
  (a) Apply the "Off-diagonal G≠G′ estimate" block at the end of ledgers/REVIEWS/ch12/editor-notes.md. The G≠G′ row of tab:12-nuisances and its mentions in 12.1/12.3 get the estimated size (full over diagonal ≈ 1.2–1.4 in an empirical-pseudopotential RPA model for Si, flat in m_χ, not converged in G), replacing "unsized" and citing no process. The full calculation stays named as open.
  (b) Fix eq:12.3-FL as the block says: include the phase e^{i(G−G′)·X} of the struck nucleus, or state that the origin sits on that atom. Check that the citation of Liang et al. Eqs. (12)–(13) matches.
- check_notation.py splits keys at ";", so S^ad_{κ;GG′} shows as a gap; teach the script that key (it is a false gap).
