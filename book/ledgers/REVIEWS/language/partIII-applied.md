# Language audit, Part III (ch18–ch22): reviser log

Brief: briefs/reviews/language-audit.md, reviser role. Ledger: ledgers/REVIEWS/language/partIII.md.
Files edited: only tex/ch18–ch22 (27 files). Each edit was an exact string replacement, checked to match exactly once in the current file before it was applied. Nothing committed.

## Applied

MUST (17 of 17): 18-3, 18-8, 18-9, 19-1, 19-3, 19-9, 19-10, 19-15 (first clause), 19-17, 19-18, 19-19, 20-1, 20-5, 20-8, 20-9, 20-10, 21-1.
- 20-5: I applied the ledger rewrite and added "the room-temperature density" before \SI{2.70}{g.cm^{-3}}, so that the next sentence ("The zero-temperature density, 2.73, …") reads as a contrast (see P1).

OPTIONAL applied (32): 18-1, 18-2, 18-4, 18-5, 18-6, 18-7, 18-10; 19-2, 19-4, 19-6, 19-7, 19-8, 19-11, 19-12, 19-13, 19-14, 19-15 (both remaining clauses), 19-16; 20-2, 20-3, 20-4, 20-6, 20-7, 20-11, the s20-2:111 note ("the mean still depends on the birth spectrum"); G1 line s20-1:88; 21-2, 21-3, 21-4, 21-5; 22-1, 22-2. G4 is covered by 18-1, 19-2 and 20-2.
- After G1, no "book/booked/books" accounting verbs remain in ch18–ch22. "Bookkeeping" as an ordinary noun is kept, as the ledger advises.

OPTIONAL not applied:
- 19-5 ("hand-over" → "initial state"). appE/E-23 also uses "hand-over", and appE is outside my scope, so renaming only in ch19 would break consistency. The term is kept consistently as it is. If the editor wants the change, it should be made in ch19 and appE together. The label sec:19.1-handover is not affected either way.
- 20-12 ("survives the memory loss" → "survives down-conversion"). Down-conversion is narrower than the defined memory loss (which also includes mode mixing), so this rewrite would change the meaning. Kept.
- 21-6 ("tier"). ch17 defines it (sec:17.6-tiers, eq:C.13-height), so it is a defined term. Kept.
- G2 (register rates). There was no sentence-level edit beyond the items above.

## Physics doubts

- P1 (s20-3 caption). figscripts/ch20/amm20_3.py and amm20_3.log confirm that the computation uses the zero-temperature Al elastic constants with rho = 2700 kg/m^3 (c_L = 6.628, c_T = 3.302 km/s). The caption was mislabelled, and I fixed it narrowly to "aluminum, zero-temperature elastic constants at the room-temperature density, 6.63, \SI{3.30}{km.s^{-1}}, \SI{2.70}{g.cm^{-3}}". No number changed.
- P2 (ch22 opening, "between 0.333 and 0.405 MeV"). In 13.x the phonon-assisted onsets are 0.3332 MeV (exciton replica) and 0.3374 MeV (free pair), and s13-9:81 says the rate between them is the replica's. The lower end is therefore the replica onset, not a gap without rate. I changed 0.333 to 0.3332 so that it matches s13-1/s13-7/s13-9 exactly. The upper end, 0.405, is the lower end of the first zero-phonon edge (0.405–0.408) and is unchanged. s22-1:3 ("0.333 MeV deposits at most 1.17 eV") is the floor 2Eg/v_max^2 and is left alone. s21-3:3 quotes only the free-pair onset 0.3374; this is consistent, so no change.
- P3 (the 0.81–1.02 and 1.30–1.53 values in the s19 and s20 summaries). These are consistent, and both summaries still carry the same numbers after the edits. No change.
- P4 (ch18 opening, "two or three in nearly every event"). The text of s18-3:47 gives P(4) = 0.039 for the dark-matter seed and 0.045 for the photon seed, so two or three pairs account for 96% of events. The wording holds for the cascade model with band seeds. Only the one-carrier split (0.143) would not fit, and that split is a bracketing rule, not the model. No change.

## Checks

- Lint (lint.py --banned BANNED-TERMS.txt on tex/ch18–ch22): 220 hits, 0 blocking (the reviewer's run had 221).
- Build: latexmk -pdf into /tmp/claude-0/build-lang3. The first run hit the pass limit (concurrent edits to other Parts, e.g. appD) and the rerun finished with rc 0. 0 LaTeX errors, 0 undefined or multiply defined references, 1840 pages.
