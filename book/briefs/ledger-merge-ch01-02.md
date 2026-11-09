# Editor task: merge the ledger rows of the accepted Chapters 1–2 and their appendices

Merge the "proposed rows" blocks of /home/user/dmdd-solid/book/ledgers/SEAMS/1.1.md … 1.5.md, 2.1.md … 2.5.md and A.md (including all "Revision rows" sub-blocks) into the book files below.

- **/home/user/dmdd-solid/book/NOTATION.md** (Symbol | Meaning | Units | First use)
  - Rename any proposed symbol that collides with an existing row, following the confirmed clash list and the editor decisions at the end of NOTATION.md, and record each rename in a new clash entry.
  - Where the text already uses a renamed symbol (the revisers did this), the row must match the text.
  - Grep the tex.
- **/home/user/dmdd-solid/book/GLOSSARY.md** (Term | Definition | Defined in)
- **/home/user/dmdd-solid/book/ledgers/CONCEPTS.md** and **/home/user/dmdd-solid/book/ledgers/CLAIMS.md**
  - Mark the Part I rows of concepts and claims defined or derived in Chapters 1–2 and App. A as WRITTEN, with their \label.
  - Add any that are missing.
- **/home/user/dmdd-solid/book/INDEX.md** (new): index entries proposed by the writers (term → section), deduplicated.
- **/home/user/dmdd-solid/book/SPINE.md**
  - Set the status of 1.1–1.5, 2.1–2.5, App. A.1–A.9, C.9 and D.1–D.3 to ACCEPTED.
  - Set C.1–C.8 to DRAFTED (in review with Chapter 3).

**Check** that every symbol used in tex/ch01, tex/ch02 and tex/appA has a NOTATION row. Write a script /home/user/dmdd-solid/book/ledgers/check_notation.py that extracts macro-level symbols where feasible, and list the gaps it finds; or check by careful grep where extraction is not feasible.

**Rules**
- Edit only the files named above.
- Use exact Edit replacements; other writers are drafting in parallel and do not touch these files.
- Do not commit.

Final message ≤ 8 lines.
