# Editor task: ledger merge for Chapter 6 and App. D.16–D.18
Follow the procedure of briefs/ledger-merge-ch01-02.md. Merge the proposed rows (including revision blocks) of ledgers/SEAMS/6.1.md … 6.5.md (including the "Revision after the Chapter 6 review" blocks), the D.16–D.18 rows of D-c.md, and the A.md revision rows into NOTATION.md, GLOSSARY.md, ledgers/CONCEPTS.md, ledgers/CLAIMS.md and INDEX.md. Rename clashes per NOTATION and the editor rulings, and keep every row consistent with the revised tex (grep it).
- SPINE.md: set 6.1–6.5 and D.16–D.18 to ACCEPTED.
- Run ledgers/check_notation.py on tex/ch06 and appD/D-16..D-18, fill the gaps, and run ledgers/check_concepts.py until it reports 0 violations.
Other agents edit tex/ch07, and also append to NOTATION.md now and then. Use exact, small Edit replacements and re-read before each. Do not commit. Final message ≤ 8 lines.
Also make these consistency edits in accepted tex (read each occurrence in context first):
- Spelling sweep: "non-adiabatic" → "nonadiabatic" and "translational invariance" → "translation invariance" in tex/ch05, appD/D-13, appE/E-8, E-11, E-18 and E-23 (and anywhere else outside tex/ch07).
- E.8 (around l.92): do not credit the 20 % shortfall to Zacharias directly. Word it as in the revised 6.3: "consistent with" Zacharias' GW-based 66 meV.
