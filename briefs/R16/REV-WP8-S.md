# R16 revision brief REV-WP8-S: WP8-S v2, the substrate ranking per channel

## Target
Write /home/user/dmdd-solid/returns/R16/WP8-S-v2.md. It is a standalone, corrected version of the WP8-S synthesis in returns/R16/CW7.md §12: the optimal substrate per interaction channel within the pickable universe. It absorbs every item of referees/R16/REF-WP8-S-A.md and REF-WP8-S-B.md, the ERR-CW7 refinements (returns/R16/CW7-errata.md, IF-ERR7-1), and uses only the current inputs:
- WP8-F-v3.md (figures of merit);
- WP8-U-v3.md and WP8-U-table-v4.csv (properties, screening, S4);
- GAP-EF-v2.md with its errata (ε_eh, F_eh).

## Required
1. **Uncertainty propagation.**
   - Rewrite the ranking as code/REV-WP8-S/rank.py, starting from code/CW7/rank.py, against table v4. Use `c_NR1_heavy` and the corrected Christoffel tensors.
   - Every input carries its provenance-based uncertainty: [FT] stated; [DB] by family; [E] wide.
   - Propagate by Monte Carlo or linearised log-error to each FOM and report P(material i ranks first) and the rank intervals.
   - Tiers are defined by overlap of 68% intervals, not chained from the first member.
2. **FOM-level fixes from WP8-F-v3.**
   - The light-mediator single-phonon NR FOM is target-independent; rank only the heavy-mediator case, with its mass window.
   - Polar: use one consistent ε pair and report reach as well as rate.
   - Migdal: include 𝓠_Mig (plasmon-pole factor) and the compound Σ_κ/A_cell scaling; state the NiO valence convention or drop it.
   - ε_eh: parse ranges correctly and say which temperature each value refers to.
   - ER edge: use consistent-temperature gaps.
3. **Completeness.**
   - Every survivor and conditional survivor appears in every channel, or is listed with the reason it is missing (GAP input). Li₂MoO₄ in particular.
   - S4 conditions are carried into the channel rows: TeO₂, and ²¹⁰Pb for the Pb salts.
   - State that the tiers ignore backgrounds except through S4, and say which channels would reorder under background-limited reach.
4. **Readings.** Write only the readings that survive the uncertainty analysis, each with its probability. Flag any ranking driven by an [E] or GAP value.
5. **Checks** in code/REV-WP8-S/checks.py: they must test the orderings and the probabilities, not only the inputs, and they must pass.
6. End with a closing table (one row per referee item → resolution), then the sections 'Symbols introduced/used', 'Interface flags' and 'Proposed LIMITS rows'.

## Rules
- Run no heavy numerics; a Monte Carlo of ≤ 2 min is fine.
- Follow CONVENTIONS and NOTATION.
- Literature via skills/breakthrough-maths/scripts/lit.py into literature/papers-REV-WP8-S/, PDFs deleted.
- Write only the return and code/REV-WP8-S/. Do not commit.
- Final message ≤ 12 lines.
