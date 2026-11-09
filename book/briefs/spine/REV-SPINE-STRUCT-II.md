# Spine review (structural), Parts II–III (Chapters 8–22) and Appendices E′ and F

You are an isolated structural reviewer of the textbook spine. Read only: /home/user/dmdd-solid/book/SPINE.md (Part I and Appendices; Parts II–III only to check forward pointers), /home/user/dmdd-solid/book/READER.md, /home/user/dmdd-solid/book/STYLE.md, /home/user/dmdd-solid/book/NOTATION.md, /home/user/dmdd-solid/book/ledgers/CONCEPTS.md, THREADS.md, CLAIMS.md, and /home/user/dmdd-solid/skills/long-form-writing/SKILL.md §2.

Check and report:
1. **Dependency violations.** For each section, check every concept used against its prerequisites. Re-derive the CONCEPTS DAG order yourself; do not trust the ledger's own check.
2. **Gaps.** Look for material that Part II–III chapter outlines will need, but that Part I does not teach. Check for each that it is either in Part I or deliberately deferred.
3. **Duplicated coverage.** Look for the same idea taught twice, or in two voices.
4. **Budget realism.** Words versus content per section (3,000–6,000 words per section is the unit). Flag sections that are overloaded or thin.
5. **Learning outcomes.** Each must be testable, and each must be taught in its section.
6. **Directive compliance.**
   - No exercises or checkpoints; nothing is left to the reader.
   - The computational connection is woven into the text, with Appendix E.
   - Silicon is the running example.
   - Titles are short noun phrases.
7. **Appendix D/E pointers.** Every pointer is matched in both directions.
8. **NOTATION.** Check that the planned symbols cover what the sections introduce, and look for clashes.

Output /home/user/dmdd-solid/book/ledgers/REVIEWS/spine/structural-II.md (≤ 200 lines). Start with a table: issue → section → severity (BLOCKER/MAJOR/MINOR) → proposed fix. Do not edit any other file. Do not commit. Final message ≤ 10 lines.

## Additions for Parts II–III
- Part I is already designed and reviewed; check that Parts II–III build on it without re-teaching it, with no duplicated coverage between Part I and Parts II–III.
- **Length policy (user):** no hard cap, but fluff is cut. Flag sections that repeat a template mechanically, restate earlier material, or pad. Do not flag length for its own sake.
- Check that every 'Open problems' item is stated as an open problem and not presented as established.
- Check the Chap. 17 next-target guide and the limit-box design (comparison plots, STYLE.md).
- Also check the coverage claims: all 155 LIMITS rows, 48 atlas cells, 42 exact gaps and 98 deferred computations each have exactly one home. Re-derive this from SPINE.md itself, not from the check script.
