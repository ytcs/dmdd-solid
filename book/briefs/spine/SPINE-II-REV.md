# Book brief SPINE-II-REV: revise the Parts II–III spine after both reviews

Apply every item of /home/user/dmdd-solid/book/ledgers/REVIEWS/spine/structural-II.md and reader-II.md to /home/user/dmdd-solid/book/SPINE.md (Parts II–III, Appendices, front matter), NOTATION.md, ledgers/{CONCEPTS,THREADS,CLAIMS}.md and ledgers/check_concepts.py.

Follow STYLE.md and the current user rules:
- **Openings:** chapter openings are motivational, never section lists.
- **Citations:** they attribute only; nothing requires the reader to consult a source.
- **Limit boxes:** each is a comparison plot that stands without its source.
- **Length:** no length cap, and fluff is cut.
- **No process artifacts.**
- **Computation:** computational connection is woven into the text. No dedicated how-to-compute sections.

## Editor decisions (apply as stated)
1. **Limit boxes (BLOCKER S1–S3).**
   - Each of the 113 boxed entries specifies four things: the literature formula, in the book's notation; the **controlling parameter** (the plot's x-axis); the **fuller result** it is compared with (which equation or section); and the **validity region**, which is shaded.
   - Add every plot to its chapter's figure list and to the budget.
   - Rewrite 9.4 to the new format.
   - Explain how a box is read once, in the front-matter "How to read this book", so that Chap. 8 can use boxes before Chap. 9.
   - The Appendix F map gains the truncation (𝔗) column. Reconcile the four status-tag disagreements between entries and F against /home/user/dmdd-solid/state/SOTA.md.
2. **Next-target guide (S6–S7).**
   - Chap. 17 keeps the channel comparison and the response-level figures of merit (rate and reach FOMs per material).
   - Move the next-target guide, which needs ε_eh, readout and backgrounds, to the end of Part III. Make it a section of the last physics chapter before open problems, or its own short chapter, whichever is cleaner.
   - Capability (crystal mass or array, readout, radiopurity) is a **column**, never a filter.
   - Specify the guide's table columns.
3. **Chapter openings (S4).** Rewrite every Part II–III chapter "outline" field as a motivational or transitional purpose statement.
4. **13.7 (S5).** Fold the how-to-compute material into the running text and Appendix E. The section goes.
5. **Status (S8–S9, reader items).**
   - Anything that is an estimate ([E]), CLAIMED, or new and only claimed is presented as such, never as established. Align the 13.10 PAER window statements with SOTA "R17 final state".
   - The Al bulk gap is settled; it is not open.
   - Define or remove L43's "OPEN".
6. **Duplicates (S10–S13 and reader list).** Teach each result once and point back:
   - f-sum (D.6/D.26);
   - loss-function exactness;
   - the Hall–Bardeen–Blatt edge;
   - donors;
   - spin waves;
   - anisotropy;
   - the repeated worked example and titles;
   - the Part I re-teaching in 8.2–8.3;
   - the double 𝔗 placement;
   - Si-edge absorption.

   Also fix the Frenkel-pair/exciton prerequisite in 16.4.
7. **Prerequisites never taught (S14–S16, reader LOST items).** Add short primers as Appendix C sections, or fold them into Part I where they fit naturally, and point to them:
   - statistics (likelihoods, C.L., profiling);
   - the Dirac equation and the Foldy–Wouthuysen reduction;
   - the quantized photon field;
   - point and space groups;
   - continuum elasticity;
   - magnetic neutron scattering;
   - spin-boson and crowdion basics (for 16.8).

   Also fix 8.5 (the truncation label before any formula exists).
8. **Open problems (S17).** Each open item is stated once, in its chapter's open-problems passage. Chap. 22 becomes an indexed table that points to those passages, not a restatement.
   - Give every one of the ≥ 14 unlabelled open items an exact-gap label.
   - Give the 7 doubled exact gaps one home each.
9. **Overloaded sections (S18).** Split, or move material to appendices.
10. **E/E′ pointers (S19).** Make each pointer match by content, not only by list.
11. **Front matter.** Reading paths through Parts II–III for the three personas.

## Required
- A change log row for every review item.
- Rerun check_concepts.py and report 0 violations.
- Recompute every coverage count: LIMITS 155/155, atlas 48/48, DC 98/98, exact gaps each in one home.
- Do not commit. Final message ≤ 12 lines.
