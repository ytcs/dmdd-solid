# Title, deferral and organizing-equation pass (2026-11-02)

Scope: tex/ch01–ch09, ch11 (not s11-5), appA, appC, appD, appE. Not touched: tex/ch10, tex/ch11/s11-5.tex. \label keys unchanged. Nothing committed.

## 1. Titles

Every \chapter, \section, \subsection and \section* title in scope (about 640) was listed and checked with the index test. Ch. 1 already carried the user's two renames (1.1 "The master equation of direct detection", "Inputs from cosmology"). Titles that already name their content (most of them) were left as they were. Renamed (53):

| File | Old | New |
|---|---|---|
| tex/appA/A-2.tex | Why Heaviside--Lorentz | Heaviside--Lorentz units and the loss function |
| tex/appA/A-3.tex | Why the plus sign | Sign of the spatial transform |
| tex/appA/A-7.tex | Moments | The first frequency moment |
| tex/appC/C-4.tex | Lorentzian limits and their corrections | Corrections to the Lorentzian limit |
| tex/appC/C-5.tex | Which functions obey them | Direct and inverse dielectric functions |
| tex/appC/C-9.tex | When the static limit holds | Validity of the static limit |
| tex/appC/C-13.tex | What a tier asserts | Interpretation of tiers |
| tex/appD/D-8.tex | Limits | Static, small-$q$ and high-frequency limits |
| tex/appD/D-9.tex | Limits | Static and long-wavelength limits |
| tex/appD/D-12.tex | Spin | Spin structure of the kernel |
| tex/appD/D-13.tex | A solvable check | A solvable harmonic model |
| tex/appD/D-19.tex | The model | The two-sublattice Heisenberg model |
| tex/appD/D-21.tex | The bare bubble and its violation | Ward-identity violation of the bare bubble |
| tex/appD/D-22.tex | Dirac electrons and their polarization | Polarization of Dirac electrons |
| tex/appD/D-22.tex | Limits | Static and long-wavelength limits |
| tex/appD/D-25.tex | Index order | Index order of the contraction |
| tex/appD/D-26.tex | Moments and their brackets | Moments as commutator brackets |
| tex/appD/D-26.tex | Which moments exist | Existence of the fourth moment |
| tex/appD/D-29.tex | Conversions | Conversions between normalizations |
| tex/appD/D-31.tex | The harmonic nuclear response at all phonon orders | Nuclear response at all phonon orders |
| tex/appD/D-32.tex | The impulse limit of the nuclear response and the Doppler width | Impulse limit and Doppler width |
| tex/appD/D-32.tex | Moments | Moments of the recoil spectrum |
| tex/appE/E-14.tex | The loss function and its inputs | The phonon-assisted loss-function grid |
| tex/ch02/s2-4.tex | When second order dominates | Forbidden first-order transitions |
| tex/ch03/s3-4.tex | The best single determinant | Hartree--Fock theory |
| tex/ch04/s4-1.tex | A weak field switched on | Response to a weak field |
| tex/ch04/s4-2.tex | Correlation functions and the dynamic structure factor | Correlations and the dynamic structure factor |
| tex/ch04/s4-3.tex | When the sum rule changes | Nonlocal potentials and the f-sum rule |
| tex/ch04/s4-6.tex | The spread between the rungs | Rung spread as an error measure |
| tex/ch04/s4-7.tex | Adding and removing an electron | The one-electron Green's function |
| tex/ch04/s4-9.tex | The completed ladder | The ladder of approximations |
| tex/ch05/s5-1.tex | The small parameter | The Born--Oppenheimer parameter |
| tex/ch05/s5-6.tex | Counting phonons | Expansion in phonon number |
| tex/ch06/s6-3.tex | Two terms at second order | Fan--Migdal and Debye--Waller terms |
| tex/ch06/s6-5.tex | Two time orderings | The phonon-assisted amplitude |
| tex/ch06/s6-5.tex | From light to dark matter | Phonon-assisted dark-matter scattering |
| tex/ch07/s7-1.tex | The spin density and its response | Spin-density response |
| tex/ch07/s7-3.tex | Pairs and kinematics | Interband pair threshold |
| tex/ch08/s8-2.tex | Conditions | Assumptions of the formula |
| tex/ch08/s8-2.tex | Two couplings at once | Conditions for off-diagonal terms |
| tex/ch08/s8-3.tex | The relations together | Table of exact relations |
| tex/ch08/s8-5.tex | The many-body rung | Many-body rungs as resummations |
| tex/ch08/s8-6.tex | What each sector contains | Densities in each sector |
| tex/ch08/s8-6.tex | The zero-phonon line and its sideband | Zero-phonon line and phonon sideband |
| tex/ch08/s8-7.tex | The hand-off to the cascade | Cascade probabilities of a final state |
| tex/ch08/s8-7.tex | What the measurement chain receives | Inputs to the measurement chain |
| tex/ch08/s8-8.tex | How a nuisance acts | Scale, tilt and edge shifts |
| tex/ch11/s11-1.tex | Long wavelengths | The long-wavelength limit |
| tex/ch11/s11-1.tex | The rate | Orientation-averaged rate |
| tex/ch11/s11-2.tex | The rate | The polar single-phonon rate |
| tex/ch11/s11-4.tex | The impulse limit and free nuclear recoil | Impulse limit and free nuclear recoil |
| tex/ch11/s11-6.tex | One atom of a different mass | An isotopic mass defect |
| tex/ch11/s11-6.tex | Random couplings | Broadband response of random couplings |

**SPINE.md** brought into line: 1.1 → "The master equation of direct detection" (it still had the old title), and the 1.1 Purpose line ("without derivation" → "derived in Chaps. 2–4"; "what gravity fixes" → "the inputs from cosmology"); 4.2 → "Correlations and the dynamic structure factor"; 11.4 → "Impulse limit and free nuclear recoil"; D.31 → "Nuclear response at all phonon orders"; D.32 → "Impulse limit and Doppler width"; C.13 entry "what a tier asserts" → "interpretation of tiers". Two section headings that already differed from the tex were also fixed: 4.6 "RPA, local fields and TDDFT kernels" → "Local fields and exchange–correlation kernels"; 6.1 "Non-adiabatic coupling" → "Nonadiabatic coupling". The remaining differences between SPINE and the tex are only the dash typography (– vs --).
**INDEX.md, CONCEPTS.md, GLOSSARY.md:** no entry quotes a renamed title. "hand-off to the cascade" and "many-body rung" are terms the body still uses, so those entries stay.

## 2. Self-narrating and provenance sentences (40 rewritten)

*Provenance ("in the form of Ref.", "the form of Ref.", "as in Ref.", "Following Ref.") → bare citation (34).* Where the clause followed a display, the citation moved to the clause that introduces the display (the style of s1-5), the display now ends with a period, and the provenance clause was deleted. Locations: A-2:22, A-3:31, A-3:65, A-5:53–57, A-7:74–78, C-9:102 (kept as a convention note: "differs from Ref. [Eq. (72)] only in the sign convention for the current"), C-20:75/80, C-20:119, D-12:83, D-14:3, D-14:72, D-22:99, D-28:28, D-29:67, E-5:45, s1-3:169–172, s1-4:83–87, s2-2:59, s2-2:208–212, s2-5:64, s4-2:86, s4-4:143, s4-5:156–159, s5-4 (three displays: Eqs. 5.4-hess, 5.4-Dwave, 5.4-lin), s5-7:59, s6-1:64, s6-1:117, s6-3:123, s6-4:89, s7-3:137, s8-4:160, s11-4:76, s11-8:55/71/92.
Examples:
- s5-7: "This is the result of Maradudin and Fein [..], in the form of Ref. [Eq. (6)]." → "This is the result of Maradudin and Fein~\cites{…}[Eq.~(6)]{…}."
- s4-4: "…$\sigma_1 = \omega|\varepsilon|^2L$, which is the form of Ref. [..] in our units." → "…$\sigma_1 = \omega|\varepsilon|^2L$~\cite{…}."
- s7-3: "Following Ref. [Eq. (2.21)] we keep the states…" → "We keep the states … the smallest of the three~\cite[Eq.~(2.21)]{…}, …"

*Self-narration (6).*
- s1-4:127 "We quote their couplings to electrons from the literature, with equation numbers, and do not derive them here." deleted. The next sentence already says where the book derives them (App. C.9, Chap. 2).
- s8-1:184 "…and the kinematics, to which we now turn." → "…and the kinematics of absorption, which fixes $\omega = m_\phi$ at $q \approx m_\phi v$ (Sect. 8.2)."
- s8-2:3 "…, and we state precisely what else it assumes." cut (the subsection "Assumptions of the formula" lists them).
- s4-3:42 "…, and we now derive it, and its relatives, directly." cut.
- s2-3:224 "…the Hamiltonian that these methods start from is the one we now write down." → "…all of them start from the Coulomb Hamiltonian of Worked Example 2-jellium."
- D-12:83 "Its resonant block is the matrix of Ref. [Eq. (20)] … has the form of Ref. [Eq. (18)]." → "In the resonant block the exchange kernel carries the singlet factor $g_{\mathrm{deg}}$~\cite[Eqs.~(18) and (20)]{…}."

Kept on purpose: sentences that map another source's convention onto the book's (for example D-14:61, "It is the G = 0 term of Ref. [Eq. (4)], with $e^2_{SI}/\varepsilon_0 \to e^2$…", and s1-4 "Ref. [..] writes it with $y_\chi^2 = 4\pi\alpha_D$"). These state a fact the reader needs and do not send the reader out of the book.

## 3. Organizing equations annotated (5 new, plus Eq. 1.1-rate as the model)

| Equation | Underbraces |
|---|---|
| eq:1.5-rate (s1-5) | $\rho_\chi/m_\chi$ halo; $\eta(\vmin)$ halo, kinematics; $\pi\bar\sigma_e F_{DM}^2/\mu^2$ coupling; $S$ target |
| eq:2.5-golden (s2-5) | $|\tilde V|^2$ coupling; $S$ target |
| eq:8.2-rate (s8-2) | $\mathfrak D_{ab}$ coupling; $S_{ab}$ target |
| eq:8.2-spectrum (s8-2) | now a two-line split: halo, coupling, target, kinematics (prefactor written as $(1/\rho_T)(\rho_\chi/m_\chi)$, which is identical to before) |
| eq:8.2-abs (s8-2) | $g^{\phi*}_a g^\phi_b$ coupling; $S_{ab}$ target (first line) |

Considered and not annotated: eq:11.4-LS (the text after it does not discuss its factors one by one) and eq:1.4-Vsq (a definition, not an organizing equation).

## 4. Deletion test (pattern 0; scope extension)

Coverage: the scope holds about 450,000 words, so a sentence-by-sentence read was not possible. The pass was done in layers instead: (a) lint.py with the new BANNED-TERMS.txt on every file in scope; (b) a grep for the pattern-0 forms the banned list does not cover ("is central to", "key role", "has consequences", "nontrivial", "subtle(ty)", "remarkabl", "it is worth", "what matters", "the lesson", "as we will see", "we now", "in this section", "the rest of the book", "important", "fundamental", "deep", …), with each hit judged at sentence level (the REGISTER connectives "however", "note that", "indeed" and "of course" were left alone); (c) a read of the opening paragraph of every chapter in scope (ch01–ch08, ch11), every `\section*{Summary}` (ch01–ch08) and the closing sentence of every section in ch01–ch08 and ch11. The appendices were covered only by (a) and (b).
Results: most grep hits are technical uses (fundamental gap, deep level, "matters for X" with X named) and stay. The section closings are forward pointers that name their target and stay. Cuts and rewrites beyond §2 (13, of which 4 are the subscript renames):
- ch11 opening (1): "The answer uses nothing new in principle." cut.
- s4-2 (1): "Positivity has consequences for rates, for interference and for absorption." → "Positivity constrains rates, interference and absorption."
- s6-5 (1): "The one-electron picture hides a subtlety that Sect. 2.4 anticipated:" → "The one-electron picture ignores Pauli blocking, which Sect. 2.4 anticipated:"
- s7-4 (2): "There is one subtlety in comparing Eq. (7.4-zpl) with experiment." → "Comparing … with a luminescence spectrum needs one correction."; "The three kinds of defect enter the rest of the book in different roles." cut.
- s8-7 (1): "The guess is right, and it is worth seeing why, because the same algebra admits a second answer." → "The guess is right, and the algebra that confirms it admits a second answer."
- D-12 (1): "One term of the exchange kernel plays a role of its own." → "The G = 0 term of the exchange kernel is the long-range macroscopic field and is treated apart."
- E-16 (1): "…; what matters here is what the tables contain and which checks make them usable." cut.
- E-16 (4 occurrences, BANNED): subscript $\mathcal G_{\mathrm{GS}}$ → $\mathcal G_{\mathrm{rel}}$, the symbol NOTATION.md already fixes for the relaxed-lattice step.
- C-20 (1): "disappears from" → "drops out of", to remove an overfull line created by the citation move.
Counts by section (all passes, excluding titles): A-2 1, A-3 2, A-5 1, A-7 1, C-9 1, C-20 3, D-12 2, D-14 2, D-22 1, D-28 1, D-29 1, E-5 1, E-16 5, 1.3 1, 1.4 2, 2.2 2, 2.3 1, 2.5 1, 4.2 2, 4.3 1, 4.4 1, 4.5 1, 5.4 3, 5.7 1, 6.1 2, 6.3 1, 6.4 1, 6.5 1, 7.3 1, 7.4 2, 8.1 1, 8.2 1, 8.4 1, 8.7 1, 11.4 1, 11.8 3, Chap. 11 opening 1.

## 5. Build and lint

- `latexmk -pdf -outdir=/tmp/build-titles main.tex`: 0 errors; 554 unresolved references, the same as before the pass (forward references to unwritten sections); the set of overfull boxes over 5 pt is the same as the baseline (46).
- `lint.py --banned BANNED-TERMS.txt` on all scope files: before 558 hits, 14 blocking, 16 TITLE-GESTURE, 3 TITLE; after 531 hits, **0 blocking, 0 TITLE-GESTURE, 0 TITLE**. LONG-SENT went from 422 to 428. The new hits come from the lint's sentence splitter, not from longer sentences: it splits at "Ref.", and after a display that ends with a period it merges the text before and after the display. EQ-PUNCT 101 (unchanged).

## 6. Open item outside scope

- tex/appF/F-rows.tex:76 has the same relaxed-lattice step. It is outside this pass's scope, and it still uses the banned subscript GS; it should be renamed to $\mathcal G_{\mathrm{rel}}$ to match E.16 and NOTATION.md.
- `python3 ledgers/check_concepts.py` after the SPINE edits: 0 violations.
