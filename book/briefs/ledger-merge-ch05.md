# Editor task: ledger merge for Chapter 5 and App. D.13–D.15, C.18
Follow the procedure of briefs/ledger-merge-ch01-02.md. Merge the proposed rows (including revision blocks) of ledgers/SEAMS/5.1.md … 5.7.md (including Revision blocks), the D.13–D.15 rows of D-b.md and the C.18 rows of C-c.md into NOTATION.md, GLOSSARY.md, ledgers/CONCEPTS.md, ledgers/CLAIMS.md and INDEX.md. Rename clashes per NOTATION and the editor rulings, and keep every row consistent with the revised tex (grep it).
- SPINE.md: set 5.1–5.7, D.13–D.15 and C.18 to ACCEPTED.
- Run ledgers/check_notation.py on tex/ch05, appD/D-13..D-15 and appC/C-18, fill the gaps, and run ledgers/check_concepts.py until it reports 0 violations.
Other agents edit tex/ch06, ch07 and appE E.14+, and also append to NOTATION.md now and then. Use exact, small Edit replacements and re-read before each. Do not commit. Final message ≤ 8 lines.
Also apply the open renames of NOTATION clash entry 74(c) in the accepted tex, reading each occurrence in context first:
- V(r) in eq:3.3-HSO → U_at(r);
- E.10's E_H → E_host;
- A.5's φ_n(k) → θ_n(k).
E.3's E_qp is already done. Update the rows and mark 74(c) as applied.
