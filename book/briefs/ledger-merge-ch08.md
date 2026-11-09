# Editor task: ledger merge for Chapter 8 and App. D.24–D.28
Follow the procedure of briefs/ledger-merge-ch01-02.md. Merge the proposed rows (including revision blocks) of ledgers/SEAMS/8.1.md … 8.8.md (including their revision blocks; D.24–D.28 rows are inside them) into NOTATION.md, GLOSSARY.md, ledgers/CONCEPTS.md, ledgers/CLAIMS.md and INDEX.md. Rename clashes per NOTATION and the editor rulings, and keep every row consistent with the revised tex (grep it).
- SPINE.md: set 8.1–8.8 and D.24–D.28 to ACCEPTED.
- Run ledgers/check_notation.py on tex/ch08 and appD/D-24..D-28, fill the gaps, and run ledgers/check_concepts.py until it reports 0 violations.
Other agents edit tex/ch10, ch11, and also append to NOTATION.md now and then. Use exact, small Edit replacements and re-read before each. Do not commit. Final message ≤ 8 lines.
Also:
- 𝖫 stays the likelihood (C.14, 8.8). Rename 4.9's pair propagator, reading each occurrence in context, to a distinct symbol (e.g. 𝖫^{(2)} → 𝒫^{eh} or similar per NOTATION free letters), in tex/ch04/s4-9.tex and appD/D-12.tex. Update the rows.
- Drop the unused ρ_c row. Add the rows for E_e/E_h carrier kinetic energies (8.7), J_s(ω) (C.20/E.22) and the 𝒥 spin current.
- Mark 8.1–8.8's CONCEPTS/CLAIMS WRITTEN.
