# Editor task: merge the ledger rows of the accepted Appendix E (E.1–E.13)

Merge the proposed rows of ledgers/SEAMS/E.1-E.3.md, E.4.md, E.5.md, E.6.md, E.7-E.10.md, E.11.md, E.12.md and E.13.md, including their revision rows, into NOTATION.md, GLOSSARY.md, ledgers/CONCEPTS.md, ledgers/CLAIMS.md and INDEX.md. Follow the procedure of briefs/ledger-merge-ch01-02.md: rename clashes according to the NOTATION clash list and the editor rulings, keep every row consistent with the tex (grep it), and dedupe the index.
- Confirmed renames: E_ph → E_ath and V_b → V_bias (in E.12); N_f → N_fine; broadening η_b; the 𝔗 components (n_B, n_T, n_A, n_g) written in italic.
- SPINE.md: set the App. E rows E.1–E.13 to ACCEPTED.
- Run ledgers/check_notation.py on tex/appE and fill every gap with a row. Run ledgers/check_concepts.py (0 violations).
- Other writers are drafting in tex/ch03, ch04 and appD and are not editing these ledger files. Use exact Edit replacements. Do not commit. Final message ≤ 8 lines.
