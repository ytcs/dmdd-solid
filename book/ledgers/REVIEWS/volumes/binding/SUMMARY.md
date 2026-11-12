# Sentence-construction round (binding and parse depth): summary

Base commit 60cc72c. Rule: prose-review pattern 27 of the long-form-writing skill; book/STYLE.md, last section. Briefs: briefs/volumes/BINDING.md (editors), BINDING-REVIEW.md (reviewers). Content guard: tools/invariant.py (no math, number, citation or label new to a file or removed from it, except reviewed errata). Ranker: skills/long-form-writing/scripts/binding.py (candidates only; every paragraph was read whole).

## Process
1. Pilot (Sect. 2.4) by the lead, independent review, calibration added to the brief.
2. 28 editor units covering every chapter, appendix, caption, box, worked example, table cell and the front matter.
3. 14 independent review blocks: every changed sentence checked for fidelity, binding, depth and over-repair; at least one unchanged paragraph in ten sampled for misses. Threshold: more than 2 misses per 1000 words sends a chapter to a second pass.
4. Second passes: App. C (2.8), Ch. 8 (3.0), Ch. 10 (2.9), Ch. 15 (3.0), Ch. 27 (2.3), Ch. 28 (2.1).
5. Physics errors found by editors and reviewers went through the errata process: G9 (ER-33 to ER-41), G10 (ER-42, ER-43), G11 (ER-44 to ER-47), each proposal checked by an independent reviewer before application.

## Numbers
| Volume | Sentences changed by editors (approx.) | Reviewer fixes / reverts | Misses per 1000 words in sampled unchanged text, after second passes |
|---|---|---|---|
| I | 2,500 | 46 / 4 | 0–1.8 (App. C 2.8 before its second pass) |
| II | 4,100 | about 100 / 5 | 0–1.8 (Ch. 8, 10, 15 at 2.9–3.0 before their second passes) |
| III | 1,000 | 38 / 1 | 0.4–1.8 (Ch. 27, 28 at 2.3, 2.1 before their second pass) |

Ranker candidates per 1000 words, before → after: Vol I 23.6 → 20.3, Vol II 23.6 → 21.2, Vol III 21.9 → 19.8. The ranker falls little by design: naming an antecedent lengthens a sentence, and pronouns with one candidate were kept.

Names given one meaning (examples): energy denominator = E_i − E_m (Ch. 2); kinematic vs pair-breaking edge (Ch. 15); kinematic window (Ch. 17); "the Fock term" for Σ_x (Ch. 23); one-sided split (Ch. 18); impact-ionization threshold vs threshold ratio (Ch. 18); 2W_κ is the Debye–Waller exponent (Ch. 5, NOTATION.md).

Errata applied: ER-33 to ER-45 and ER-47 (ER-46 needs no change given ER-47). Layout: all overfull boxes cleared (0 in all volumes). Build: Vol I 618 pp, Vol II 826 pp, Vol III 254 pp; 0 errors, 0 undefined references or citations.

## Examples
| Location | Before | After | Failure fixed |
|---|---|---|---|
| s2-4 opening | "Silicon absorbs such photons all the same, because a lattice vibration can supply the missing momentum. The photon lifts an electron into a state that conserves crystal momentum but not energy, and a phonon emitted or absorbed a moment later takes it to a final state that conserves both. The state in between is never observed. It enters the rate through an energy denominator, the mismatch between its energy and that of the initial state." | "Silicon nevertheless absorbs these photons, because a phonon can supply the crystal momentum that the photon lacks. The absorption is a second-order process. The photon first takes the system from the initial state to an intermediate state, in a transition that conserves crystal momentum but not energy. Emitting or absorbing a phonon then takes the system from the intermediate state to a final state, and the whole process, from the initial to the final state, conserves both energy and crystal momentum. The intermediate state is never observed; it enters the absorption rate through an energy denominator, which is the difference between the energy of the initial state and the energy of the intermediate state." | pointers to non-nouns, garden path, four names for one state, relational nouns without arguments |
| s13-2:24 | "as long as no E_m equals E_i + ω or E_i. The second never happens in an insulator. The first would mean …, which cannot happen while …" | "An E_m equal to E_i never occurs in an insulator. An E_m equal to E_i + ω would mean that the density alone creates a real zero-phonon pair at (q, ω), and no such pair exists while …" | *the first/the second* across sentences; *which* for a proposition |
| s13-2:69 | "Keeping only empty intermediate bands, the natural truncation when the intermediate states are thought of as virtual electrons, gets the amplitude wrong …" | "When the intermediate states are thought of as virtual electrons, the natural truncation keeps only empty intermediate bands. This truncation gets the amplitude wrong …" | gerund subject with a defining apposition before the verb |
| s13-1:23 | "The bound pair does not change this picture. … it lowers the threshold mass by …" | "Binding the pair into an exciton changes the threshold mass only slightly. … the exciton lowers the threshold mass by …" | definite before introduction; *this picture* a proposition; *it* with three candidates |
