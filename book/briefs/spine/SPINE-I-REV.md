# Book brief SPINE-I-REV: revise the Part I spine after the spine reviews

Apply every item of /home/user/dmdd-solid/book/ledgers/REVIEWS/spine/structural.md (30 issues) and /home/user/dmdd-solid/book/ledgers/REVIEWS/spine/reader.md to /home/user/dmdd-solid/book/SPINE.md (Part I, Appendices, front-matter plan), /home/user/dmdd-solid/book/NOTATION.md and /home/user/dmdd-solid/book/ledgers/{CONCEPTS,THREADS,CLAIMS}.md. Follow /home/user/dmdd-solid/skills/long-form-writing/SKILL.md §2, READER.md and STYLE.md (no exercises; nothing left to the reader).

## Editor decisions (apply as stated)
1. **BLOCKER 1:** add a phonon self-energy section to Chap. 6, covering the Eliashberg function, phonon linewidths from electron–phonon coupling, and the phonon-side Migdal theorem. It is needed by 7.2 and Part II. Renumber Chap. 6.
2. **BLOCKER 2:** split 4.5 into "RPA, local fields and TDDFT kernels" and "Excitons and the Bethe–Salpeter equation".
   - Teach local fields once (resolve the 4.4/4.5 duplication).
   - Place sections so that the BSE ladder comes after the diagram and Green's-function machinery it needs. The reader proposes the order 4.4 → 4.7 → 4.5 → 4.6; choose a valid order and justify it.
3. **4.6 (Green's functions and diagrams) is overloaded.** Split it, or move material into Appendix C/D, and fund it by taking about 2,000 words from 2.1 and 2.5.
   - Include finite-temperature (Matsubara) Green's functions and Wick's theorem at the level later chapters need. Steps go in Appendix D, not "only mentioned".
4. **1.4:** do not require the reader to derive potentials with field theory. Add Appendix C.9, a short classical-field and Yukawa-potential primer, and point to it. Mention in-medium dark-photon mixing.
5. **Fix all seven forward uses.** Check every field of every entry (learning outcomes, key results and worked examples too), not only the prerequisites. Add the missing concepts, each with a defining section: velocity matrix elements, the Debye model, oscillator strengths, k_F, self-energy before GW, and the conductivity σ₁ for Part II absorption.
6. **Fix READER.md mismatches.** Either a prerequisite is on the "assumed" list, or it is taught.
7. **Front matter:** add a skip path for each persona.
8. **Expert flags:** superexchange for NiO; the Berry-phase caveat for Born charges; the scope of Migdal's theorem in insulators; the BCS pairing mechanism, in brief; the separation of the Migdal theorem (1958) from the Migdal kick (1941).
9. **Rebalance:** 7.2 is overloaded and 6.3 is a method section; move it to Appendix E with a narrative stub. Add the missing Appendix E pointers for 6.5, 5.6 and 3.3.
10. **NOTATION:** resolve Ω, Φ_κκ′, chemical potential μ, ω, V, κ and v_F.

## Required
- A change log in SPINE.md, with one row per review item → resolution.
- Rewrite the CONCEPTS order check as a script that scans **all** fields of every entry. Save it as /home/user/dmdd-solid/book/ledgers/check_concepts.py, run it, and report 0 violations.
- Recompute the totals.
- Edit only the files named above plus check_concepts.py. Do not commit.
- Final message ≤ 12 lines.
