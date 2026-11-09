# Book brief SPINE-II: detailed spine for Parts II–III (Chapters 8–22) and Appendices E′, F

You are the spine designer for Parts II and III of *Dark Matter Detection in Solids*. Follow /home/user/dmdd-solid/skills/long-form-writing/SKILL.md §2, and use the template /home/user/dmdd-solid/skills/long-form-writing/templates/spine-entry.md.

Read first:
- /home/user/dmdd-solid/book/READER.md, /home/user/dmdd-solid/book/STYLE.md.
- /home/user/dmdd-solid/book/SPINE.md: the design principles, the production directives (succinct background, batched review, no exercises), the full Part I entries (Parts II–III build on them), and the Chapter 17 framing (the next-target guide for experimentalists).
- /home/user/dmdd-solid/book/NOTATION.md and the ledgers.

The research is complete. Its authoritative state is:
- /home/user/dmdd-solid/state/SOTA.md, especially the "R14–R16 consolidated state" and "R17 final state" blocks;
- /home/user/dmdd-solid/LIMITS.md (every literature formula recovered as a limit, each with status; these feed the limitbox environments and Appendix F);
- /home/user/dmdd-solid/FRAMEWORK.md;
- /home/user/dmdd-solid/state/LOOSE-ENDS.md (every exact remaining gap, for the open-problems sections);
- /home/user/dmdd-solid/state/NOVELTY.md (claims of novelty vs prior art; the book states priority modestly);
- /home/user/dmdd-solid/state/DEFERRED-COMPUTE.md (quantities the book explains but does not compute yet).

The returns hold the derivations: returns/R8/*-v3.md, returns/R12/*, returns/R13/WP5-v4.md, returns/R16/*.md with their errata, and returns/R17/*.

## Target
1. **Expand every Chapter 8–22 section to the full entry template.** Every key result must point to its derivation in the research material (writer-only source paths) and to its public citation where one exists. Status tags come from SOTA/LIMITS: only REFEREED or VERIFIED content is presented as established. Items CLAIMED, or exact gaps, are presented as open, in the chapter's open-problems material.
   - You may restructure chapters and sections where the final research demands it. Examples: the PAER chapter now has the established Si window; the WP7 channels (B1/B2/D/T/E) need homes; WP8-S feeds Chap. 17's target guide; the energy-partition and ε_eh/F_eh theory goes to Part III. Justify every change in the change log.
2. **Coverage checks.**
   - Every LIMITS row maps to exactly one section and one limitbox. Map each one, and list any that are unmapped.
   - Every channel of the excitation × interaction atlas (Chap. 9) has exactly one home.
   - Every exact remaining gap appears in an open-problems passage.
3. **Appendices.** Design E′ (computational specifications per quantity; source: DEFERRED-COMPUTE.md, made standalone) and F (the full table of literature formulas as limits).
4. **Ledgers** (this closes the campaign's LE-171 and LE-172):
   - extend CONCEPTS.md, CLAIMS.md and THREADS.md (T1–T7 advanced and closed);
   - add the planned symbols to NOTATION.md as standalone rows;
   - extend book/ledgers/check_concepts.py to cover Parts II–III, run it, and report 0 violations.
5. **Status tags.** Set each chapter's tag to PLANNED, or to BLOCKED(reason) only where content is truly not established.
6. **Production directives.** Apply them throughout: succinct background, the computational connection woven into the text, and no exercises.

## Rules
- Edit only /home/user/dmdd-solid/book/SPINE.md (Parts II–III, Appendices E′ and F, the change log and the totals), /home/user/dmdd-solid/book/NOTATION.md, /home/user/dmdd-solid/book/ledgers/{CONCEPTS,THREADS,CLAIMS}.md and /home/user/dmdd-solid/book/ledgers/check_concepts.py.
- Do not commit.
- Arrange the work so the final spine is internally consistent.
- Final message ≤ 12 lines: sections planned, total words, structural changes, the LIMITS-mapping result and the check result.
