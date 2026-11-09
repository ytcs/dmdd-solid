# Editor task: ledger merge for Chapter 7 and App. D.19–D.23
Follow the procedure of briefs/ledger-merge-ch01-02.md. Merge the proposed rows (including revision blocks) of ledgers/SEAMS/7.1.md … 7.4.md (including their dated revision blocks) and the D.19–D.23 rows of D-c.md into NOTATION.md, GLOSSARY.md, ledgers/CONCEPTS.md, ledgers/CLAIMS.md and INDEX.md. Rename clashes per NOTATION and the editor rulings, and keep every row consistent with the revised tex (grep it).
- SPINE.md: set 7.1–7.4 and D.19–D.23 to ACCEPTED.
- Run ledgers/check_notation.py on tex/ch07 and appD/D-19..D-23, fill the gaps, and run ledgers/check_concepts.py until it reports 0 violations.
Other agents edit tex/ch07, and also append to NOTATION.md now and then. Use exact, small Edit replacements and re-read before each. Do not commit. Final message ≤ 8 lines.
Accepted judgment calls from the Ch7 revision:
- ε₀ in D.23/7.4 is the static dielectric constant, per the NOTATION row. Make sure that row says so unambiguously.
- E_d stays the displacement threshold. Rename the local E_d of WE 4.7 (tex/ch04) to a distinct symbol, reading it in context first.
- New symbols c_AB, 𝖼₂ and 𝗌_a: add their rows.
