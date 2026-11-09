# Light pass, part A: Chapters 1–12 (plus C-18)
Read briefs/reviews/lightpass-common.md first; it binds you. Scope: tex/ch01–ch12, tex/appC/C-18.tex, and their figscripts. Items:
1. Ch7 ZrTe₅: every 15.6 meV half-gap → 11.8 meV (LE-186). Check the derived numbers against Ch16 (velocities 1.1e-3, 4.5e-4, 1.0e-3; cutoff 0.191 eV).
2. 12.3 and 12.6: σ_n → σ_p where the per-proton cross-section is meant. Read NOTATION for both symbols.
3. 6.4 and C-18: room-temperature Al elastic constants → the book's 0 K set (isotropic 6.63/3.30 km/s; [111] 6.67; 2.70 g/cm³), where Al constants enter.
4. Si plasmon energy: 16.4 eV measured, used consistently (10.x shows 16.6 in places); keep a computed value only where it is labelled as computed.
5. Si static dielectric constant: one value book-wide, the one NOTATION and the accepted Ch10 use. Fix the 11.4/11.7 mismatches, and say "at low temperature" where that is the reason.
6. Si direct gap: one value (3.4 vs 3.17 eV mismatch between Ch3/Ch9/Ch10). Use the accepted Ch3/Ch10 number, with the measured value cited, and make Ch9 agree.
7. 10.9: (Zα)² for xenon 0.13 → 0.155 at l.~176 and l.~232. 10.9 boosted-dark-matter passage: bring it up to DC-49/54/36 (quote only the REF §4 wording: heavy-mediator CRDM limit unchanged; light mediator below about 3 keV undetermined).
8. 10.5: remove the "interim statement" wording. 10.6: the Ge hybrid claim is already softened (check). 10.2, 10.9 and 17.1 use a "tables' gap 1.11 eV": align it with the Ch18 cascade and Ch21's usage. Fix 10.2 and 10.9 here; part B fixes 17.1.
9. Ge exciton binding 4.2 meV: give it a citation (find the measured value with lit.py and cite it), or remove it if no source supports it.
10. s11-1 l.~168: Ge a = 5.652 → 5.658 Å; rerun the script.
11. 8.6: the stale drag-mass sentence → align with 12.5 (14 mₑ is the exact trace value; the open quantity is the on-site element, valence 18.6 mₑ, bounded 12–24).
12. 12.4: the Limit Check 12.4b text should place it on n_B (2→4, sized by 2⟨ω_ph²⟩/ω_e², as 8.5 counts it), matching App F and 9.4.
13. Acronyms in Ch1–12: expand each at first use in the book (book order: Ch1 first). The list is figscripts/appB/gen_B3.log ("never expanded" and "expanded after first use"). Use the expansions in figscripts/appB/gen_B3.py. Expand an acronym only at its first use in the whole book; if that first use is in Ch13–22, leave it to part B.
14. DC-RESULTS sweep for Ch1–12 (common rules).
