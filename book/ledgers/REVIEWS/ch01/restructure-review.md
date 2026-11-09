# Chapter 1 restructure: combined review and fix (rev2, 2026-11-02)

Scope: tex/ch01/ch01.tex (opening), s1-1.tex (rewritten), s1-5.tex ("Event rate" subsection and Summary), three edits in s1-2.tex. The rest of Chapter 1 was read for context.
Sources fetched into sources/review-ch01b/ (text extracts kept, PDFs deleted): 2108.03239, 1807.06209, 1204.3622, 1904.07915, 1112.0524, 1605.04909, astro-ph/0608407.

## Pass 1: derivation and numbers

| # | Finding | Fix | Location |
|---|---|---|---|
| D1 | eq:1.1-rate against eq:2.5-golden: Γ = ∫d³q/(2π)³ \|Ṽ\|² S(q, ω_q), with S = (2π/V)𝒮. The 2π and the 1/V sit inside S, so eq:1.1-rate correctly has no 2π in front of the delta function. The brief's schematic "2π δ(…)" assumes a different S normalization. This matches Kahn and Lin Eq. (8) exactly. | None needed (recorded so it is not raised again). | s1-1 eq:1.1-rate |
| D2 | Sign of the delta function: δ(ω − q·v + q²/2m_χ) = δ(ω − ω_q), with ω_q = q·v − q²/2m_χ (eq:1.3-omegaq at Δ_χ = 0; KL Eq. (9)). Correct. | None. | s1-1 |
| D3 | Reduction to eq:1.5-rate: (1/4π)∫dΩ_q δ = Θ(v − v_min)/(2qv); the halo average gives η/2q; 4πq²dq/(2π)³ · η/2q = q dq η/(2π)². That agrees with the measure q dq η/4π² of sec:1.3-eta and with eq:1.5-rate, KL Eq. (11) and the 2.5 text. | None. | s1-1, s1-5 |
| D4 | Dimensions of eq:1.1-rate: 1/ρ_T [eV⁻⁴] · ρ_χ/m_χ [eV³] · d³q [eV³] · \|Ṽ\|² [eV⁻⁴] · dω S [eV³] · δ [eV⁻¹] = dimensionless (a rate per unit mass). eq:1.5-rate check in s1-5 also verified (S in eV²). | None. | s1-1, s1-5 |
| D5 | Ω_c h² = 0.1200 ± 0.0012 (Planck Table 2, Eq. (23)); Ω_b h² = 0.02237 ± 0.00015 (Table 2; Eq. (24)); ratio 5.36 → "5.4". Verified. | None. | s1-1 |
| D6 | ⟨σv⟩: 2.2 × 10⁻²⁶ above 10 GeV, 5.2 × 10⁻²⁶ at ≈ 0.3 GeV, for a Majorana WIMP; canonical 3 × 10⁻²⁶ (Steigman et al., abstract and Sect. II). Verified. | Glossed "Majorana" for the reader (R3). | s1-1 |
| D7 | Lin Eq. (32) (Y_fo ∝ 1/⟨σv⟩), Eq. (44) (m_χ²/m_V⁴ scaling, Lee–Weinberg), Sect. I A (keV bounds), Sect. I C (PBHs to ≈ 50 M⊙), 10⁻²² eV light end: verified. Lee and Weinberg (1977, 2 GeV) and Tremaine–Gunn (1979) were not fetchable; checked against Lin Sect. I A and Eq. (44) only. | None. | s1-1 |
| D8 | Lin Sect. I A attributes the few-hundred-eV Pauli bound to dwarf galaxies and calls it "related to" the Tremaine–Gunn bound. The text called it the Tremaine–Gunn bound. | "the argument is related to the Tremaine–Gunn bound". | s1-1, "What gravity fixes", para 3 |
| D9 | KL Sect. I: xenon thresholds at "the few hundred eV scale"; KL Table I: band gap ∼ 1 eV, optical phonon ∼ 50 meV. Clowe et al.: lensing mass offset from X-ray plasma at 8σ. Green Sect. 3.1: local density from mass modelling. Verified. | None. | s1-1 |
| D10 | eq:1.1-rate was credited only through its angular average (KL Eq. (11)). Its own form is KL Eq. (8). | Cite KL Eq. (8) for eq:1.1-rate; point to eq:1.5-rate for the averaged form (KL Eq. (11)). | s1-1, line after eq:1.1-rate |
| D11 | **Contradiction.** s1-1 said that a limit "can be translated to another model without returning to the solid"; s1-5 (sec:1.5-plot) says that a limit for one mediator "cannot be rescaled to the other without the response". | 1.1 now says that once S is tabulated, a limit can be recast by weighting it with the new coupling, without computing the solid again. | s1-1, para 3 |
| D12 | Kinetic energies (0.5 keV, 0.5 eV, 0.5 meV at v = 10⁻³), the 0.1 keV xenon deposit (s1-3: 0.11 keV), 90 decades (10⁻²² eV to 50 M⊙ ≈ 10^67.7 eV): consistent. | None. | s1-1 |

## Pass 2: prose and register

| # | Finding | Fix | Location |
|---|---|---|---|
| P1 | The paragraph that maps factors to chapters read as a table of contents: "Sect. 1.2 fixes … Sect. 1.3 then works out … Sect. 1.4 derives … Chapters 3–7 build …". | Rewritten as argument. The halo needs no new physics (convention). Kinematics follows before any target, *since* the delta function holds no target property. The coupling is a choice of model, and limits are quoted on σ̄_e. The response, *however*, is a many-body problem (chapters 3–8, 10–17). Even an exact S does not finish the job, *because* a detector records quanta, not ω. Every cref is kept, now in parentheses. The redundant opener "The three factors also differ in how much work they take" was dropped because it restated the end of the previous paragraph. | s1-1, para 4 |
| P2 | "The halo is ρ_χ/m_χ, which is the number density…" equated a factor with a quantity. | "The halo enters through ρ_χ/m_χ, the number density …, and through f_χ(v), …". | s1-1, para 2 |
| P3 | "Each S in the book comes with a label that names the approximation": "label" reads as internal apparatus. | "Each S in the book names the approximation behind it and comes with an estimate of its error". | s1-1, para 5 |
| P4 | "A boson light enough to be absorbed" is inaccurate (absorption is not a lightness condition). | "A bosonic dark-matter particle can instead be absorbed." | s1-1, para 5 |
| P5 | s1-5 repeated the 1.1 sentence "Chap. 2 derives this structure from Fermi's golden rule", and it said that 4.2 "defines" S, which 1.1 and 2.5 already define. | "Sect. 2.5 derives it term by term from the thermal golden rule, and Sect. 4.2 develops the properties of S(q, ω)." | s1-5, after eq:1.5-rate |
| P6 | Seam 1.2 → rate: "The general rate formula in Sect. 1.5 uses ρ_χ, f_χ and v_max" was out of date after the restructure (the general formula is now eq:1.1-rate). | "The rate of eq:1.1-rate takes ρ_χ and f_χ from here, and Sect. 1.3 combines them and v_max with the kinematics of a single collision." | s1-2, last paragraph |
| P7 | Seams checked: the chapter opening ends on the rate (motivational, not an outline) and leads into the 1.1 opener "A dark-matter detector counts events." (concrete). 1.1 ends on a pointer to 1.2, whose opener is concrete. The 1.5 back-pointer ("The schematic rate of eq:1.1-rate becomes concrete …") works. s1-2 edits ("flat rotation curve of Sect. 1.1", v_c) are consistent with the new 1.1. Other back-references to sec:1.1 in s1-3, s1-4 and s1-5 (keV window, 0.11 keV, thermal relic below a keV, mediator) still resolve to content in the new 1.1. | None. | ch01.tex, s1-1, s1-2, s1-5 |
| P8 | Long sentences that the fixes introduced were split, so lint is clean on the changed text. Register counts for s1-1 (≈ 2,100 words): "so" 1, "since" 1, "because" 2, "however" 2, "but" 1, within REGISTER §6.8. No "we will/we can/we see" in 1.1. This is acceptable for a schematic section and was not padded. | Splits only. | s1-1, s1-5 |
| P9 | Lint (BANNED-TERMS.txt): ch01.tex 0 hits; s1-1 0; s1-5 1 and s1-2 2, all LONG-SENT parse artifacts of table and figure environments that predate this restructure. | None. | — |
| P10 | No process artifacts, no ordinal references to unlabelled parts, and no citation used as content in the changed text. The new KL Eq. (8) and Eq. (11) citations attribute only, since the forms are stated in the book. | None. | — |

## Pass 3: fresh reader (persona a, first-year PhD student)

| # | Finding | Fix | Location |
|---|---|---|---|
| R1 | The schematic was not understandable at first sight: S was described only as "how readily the solid absorbs q and ω, per unit volume", which a reader cannot evaluate. | Added a words-only definition: at T = 0, a sum over excited states at energy ω above the ground state of the squared density matrix element at wavevector q, times 2π from the golden rule, divided by the target volume (eq:2.5-golden; sec:4.2). No new symbols, so NOTATION first uses are unchanged. | s1-1, para 2 |
| R2 | "spin-independent interaction" was used undefined. A reader from condensed matter would not know it. | "an interaction that couples to their density and not to their spins". | s1-1, para 1 |
| R3 | "Majorana particle" was used undefined. | "one that is its own antiparticle". | s1-1, freeze-out paragraph |
| R4 | "indirect gap" and "crystal momentum" were used before their definition (crystal momentum is defined in 1.3). | Gloss "where the highest filled and the lowest empty electron states differ in crystal momentum (sec:1.3)". | s1-1, para 5 |
| R5 | "Kohn–Sham states rather than true quasiparticle states" relied on DFT and many-body terms that the reader is not assumed to know. "Absorption probability" was used for a scattering process. | "as Kohn–Sham states, the eigenstates of an effective one-electron problem rather than of the interacting electrons"; "transition probabilities". | s1-5, "Event rate" |
| R6 | The first paragraph listed three readout quanta, while 1.5 has four (quasiparticles were missing). | Added "quasiparticles". | s1-1, para 1 |
| R7 | "mediator" was used in paras 4 and 5 before its definition in "What gravity fixes". | Defined at first use: "Its simplest form is the exchange of a \emph{mediator}, a particle that carries the interaction between the dark matter and the electron." The later freeze-out sentence no longer redefines the term ("a new, light mediator, with a mass at or below the GeV scale, to carry the interaction …"). | s1-1, para 4 |

## Build
`latexmk -outdir=/tmp/build-ch01rev2`: 0 LaTeX errors. Compared with the writer's build (/tmp/build-ch01rev), the only differences in undefined references are app:E.14 and app:E.27, both from appE/appE.tex (another writer). app:D.23, app:D.7 and sec:4.4 now resolve, because concurrent writers added them. The build was rerun after the final edits. The unresolved citations (allen1972/1976/1981, calandra2010, migdal1958) are all in refsection 13, not in Chapter 1. The undefined references from the changed Chapter 1 files are all planned forward labels confirmed in SPINE: chap:8, 10, 12, 13, 17, 18, 20, 21; sec:5.3, 7.2, 10.2, 10.7 (5.3 and 7.2 checked in SPINE).

## Open items (outside write scope)
- None blocking. If a symbolic definition of S is wanted in 1.1 (n_e(q), |0⟩, E_f, V), the NOTATION first uses must move to 1.1. NOTATION.md is outside this review's scope.
