# App. C.10–C.20 (no C.18) and E.14–E.27: prose review

Brief: briefs/reviews/appCE-prose.md. Read against STYLE.md, style-guide.md, prose-review.md (patterns 0–26), REGISTER.md and the App E ruling (ledgers/REVIEWS/appE2/editor-notes.md: specifications read as prose, not as a recipe list). No tex edited.

## 1. Lint (`lint.py --banned BANNED-TERMS.txt`)
- 0 blocking hits in all 24 files. No banned terms, no PERIPHRASIS hits.
- LONG-SENT (>45 words): C-10 0, C-11 0, C-12 0, C-13 0, C-14 0, C-15 0, C-16 1, C-17 2, C-19 0, C-20 1; E-14 6, E-15 15, E-16 9, E-17 21, E-18 6, E-19 5, E-20 8, E-21 11, E-22 5, E-23 2, E-24 3, E-25 12, E-26 3, E-27 9. About a third of the E hits are artefacts: the linter joins a heading or a table caption to the next sentence. The rest are parameter sentences (see recipe pattern, Sect. 3).
- EQ-PUNCT: E-18 l.53–60 is a false positive. The `gathered` block ends with " ," on l.58.

## 2. Verdicts
| Section | Verdict | Main reason |
|---|---|---|
| C.10 Moment problems | PASS | 3 minor |
| C.11 Generating functions, branching and renewal | PASS | 2 minor |
| C.12 Linear programming and duality | PASS | 1 minor |
| C.13 Interval orders | PASS | 1 looped paragraph |
| C.14 Likelihoods, intervals and profiling | PASS | 2 minor |
| C.15 Dirac equation and FW reduction | PASS | clean |
| C.16 The quantized radiation field | PASS | clean |
| C.17 Point and space groups | PASS | 2 long sentences |
| C.19 Magnetic neutron scattering | PASS | citation style, vague close |
| C.20 Dissipative two-level systems and kinks | PASS | 1 citation as content |
| E.14 Phonon-assisted recoil from first principles | REVISE | count-teasers, 430-word Ge paragraph, process residue |
| E.15 Excitons and core states | REWRITE | recipe template throughout (24 slots / 2.6k words), stale HSE06 pointer |
| E.16 Electronic response libraries | REVISE | recipe template, count-teasers, fragment list |
| E.17 Lattice libraries | REVISE | recipe template, "the recipe is uniform", bookkeeping sentences |
| E.18 Migdal and nonadiabatic quantities | REVISE (light) | broken parallel sentence, mislabelled pitfalls |
| E.19 Anharmonic, disordered and quantum solids | REVISE | recipe template, restated C.10 band |
| E.20 Magnetic, superconducting and Dirac targets | REWRITE | recipe template (23 slots / 3.2k words), defensive asides |
| E.21 Dopants, color centers and small targets | REWRITE | recipe template (21 / 2.8k), subjectless sentence, STE undefined |
| E.22 Defects and two-level systems | REVISE (light) | closing cliché after the table |
| E.23 Nuclear-recoil partition and charge yield | REVISE (light) | mislabelled "double countings", looped close |
| E.24 Electron cascades | PASS | 4 minor |
| E.25 Event-level transport | REVISE | tense of acceptance tests, ε₀ clash, count mismatches |
| E.26 Coherent and second-order absorption | REVISE (light) | gesturing title, unanchored "It"/"the source", recap |
| E.27 Halo, background and nuclear-spin inputs | REVISE | duplicate notation for the C.12 program, uncited "Gordon et al." |

## 3. Cross-section findings (voice and consistency)
- **Recipe template (App E ruling).** I counted the slot openers per section: "The quantity/quantities is/are", "The method is", "The acceptance test(s) is/are", "Convergence is", "The cost is", "The result enters", "On 𝔗 / On the truncation label". Per 1,000 words, the accepted E.1–E.13 run 0–1.5. The new sections run E.15 9.4, E.21 7.6, E.20 7.1, E.17 5.4, E.19 5.2, E.23 4.8, E.16 4.7, E.22 4.4, E.18 3.9, E.24 2.9, E.25 2.3, E.14 1.6, E.26 1.3, E.27 1.3. Above about 4 per 1,000 words the subsections read as forms to fill in. Fix: in each subsection, open with what goes wrong or what is unknown (as E.22 and E.24 do). Then fold the slots into causal prose. Bad: "The method is X. Convergence is Y. The cost is Z." Good: "X gives …; it is converged when Y, and the whole run costs about Z." Keep each slot word at most once per subsection, and leave lists of parameters to the tables, which already exist.
- **Count-teasers (pattern 18).** "Three things make the amplitude hard" (E.14 l.3), "Six controls test the physics" (E.14 l.40), "Two cautions govern the reading" (E.14 l.46), "The cost forces two choices" (E.16 l.9), "Two calculations ride on the library" (E.16 l.11), "Three calculations would size the correction" (E.16 l.19), "Three runs separate the corrections" (E.16 l.23), "Two pieces remain" (E.17 l.34), "Two numerical errors matter more than the counting" (E.22 l.13), "Three double countings must be avoided" (E.23 l.37), "The pitfalls … apply, with four more" / "Three additions are needed" / "Three pitfalls concern the physics" (E.24 l.15, 19, 57), "Four pitfalls decide the sign or the size" (E.25 l.43), "Nuclear-spin precession needs three inputs" (E.26 l.9), "Two pitfalls give zero for the wrong reason" (E.27 l.52), "Three of its properties carry" (C.12 l.3), "Two effects compete" (C.20 l.73). Fix: name the members in the sentence itself, or drop the teaser and start with the first member. In three places the count is wrong as well (E.23 l.37, E.25 l.9, E.27 l.52; see below).
- **Truncation-label phrasing.** The new sections alternate between "On the truncation label of \cref{sec:8.5} the calculation sits at …" and "On $\mathfrak{T}$ it sits …". Write "On the truncation label $\mathfrak{T}$ (\cref{sec:8.5})" at the first mention in a section, then "On $\mathfrak{T}$". Better still, fold it into the method sentence and drop it as a slot.
- **Post-table recap paragraphs (pattern 26).** E.22 l.85, E.23 l.76, E.24 l.78, E.25 l.92, E.26 l.23 and E.27 l.54 each end the section with a summary after the table. None of the E.1–E.13 sections does this. Cut them, or keep only a fact they add (E.24 l.78 adds the run order; move it into l.21).
- **Table conventions.** Header case is mixed ("stage/parameters" in E.14, E.17, E.18, E.20, E.21; "Quantity/Method and grid" in E.22–E.25). Label style is mixed too (`tab:E14-params` against `tab:E-22-summary`). Use lower-case headers and `tab:E22-…` throughout.
- **Units outside \SI.** "7.3 against the measured 7.8~eV …" (E.24 l.21) and "$E_R \in \{50, 100, 300, 1000\}$~eV" (E.25 l.51). Use \SI / \SIlist.
- **App C openings.** Every section opens with a concrete fact and names the tool and its chapters (C.10 → 11.5; C.11 → 18.1, 18.2; C.12 → 21.2; C.13 → 17.6; C.14 → 8.8, 21.4, 21.5, 17.6; C.15 → 10.6, 12.5, 10.9; C.16 → 12.6; C.17 → 13.9, 14.5; C.19 → 14.4; C.20 → 16.8, 19.6). This matches C.1–C.9. The voice matches as well: derivations written out, "we" used sparingly, no exercises, nothing left to the reader.
- **Nothing left to the reader / no exercises.** No violation found in any of the 24 files.

## 4. Section findings (location → problem → fix)

### C.10
- l.3 "how much five moments tell us about" → mild periphrasis (pattern 25: "the data tell us") → "what five moments fix about".
- l.92 "Moments control the bulk of a distribution, and only the bulk." → aphoristic restatement of the preceding sentence (pattern 26) → cut it. The paragraph then ends on "five moments leave it undetermined".
- l.103 closing paragraph → repeats the opening pointer to 11.5. Its one new clause is "path-integral simulations give [the moments] for any anharmonicity" → move that clause into l.3 and cut l.103.

### C.11
- l.106 "Probability generating functions turn sums of independent counts into products." and l.122 "Generating functions turn sums into products." → stated twice (pattern 26) → cut it from l.106, or open l.122 with "If $N_1$ and $N_2$ are independent, …".
- l.149 "The lesson for a cascade is that" → lecture framing → "In a cascade, the fixed-point equation of a branching process has spurious roots; the physical solution is the minimal one, …".

### C.12
- l.3 "Three of its properties carry \cref{sec:21.2}. Any feasible dual … And solving the program …" → count-teaser plus a three-sentence rhythm → "\Cref{sec:21.2} uses three of its properties: any feasible dual solution certifies an upper bound, the optimum is a halo of a few streams, and a grid solution errs by an amount that a Lipschitz constant bounds."

### C.13
- l.98 "The example shows what a tier asserts and what it does not. A member of tier $k > 1$ is resolved below …" → abstract frame (pattern 18), and the second sentence repeats l.90 (pattern 26) → open with "A tier does not assert that every member of a higher tier beats every member of a lower one: $B$ does not beat $C$." and drop the repeated sentence.

### C.14
- l.135 "which is where dark-matter limits live" → figurative → "the regime of dark-matter limits".
- l.159 "One draws $N_{\mathrm{MC}}$ sets of inputs" → impersonal "one", against REGISTER §6.9 → "We draw …" or passive "$N_{\mathrm{MC}}$ sets of inputs are drawn".

### C.17
- l.26, l.48 (LONG-SENT) → acceptable as derivation; optionally split "Its trace is the dimension of that subspace:" off its display. No other issues.

### C.19
- l.121 "\cite[Chap.~7]{squires2012introduction}\cite{lovesey1984theory}" → two cites run together → "\cite[Chap.~7]{squires2012introduction}, \cite{lovesey1984theory}".
- l.121 "the combination that \cite[Eq.~(26)]{berlin2025determining} extracts" → citation used as a noun → "the combination that Berlin et al. extract from neutron data~\cite[Eq.~(26)]{…}".
- l.151 "\Cref{sec:14.4} works out what this implies for the dark-matter responses that need it." → gesture with no content (pattern 0) → "A dark-matter response that needs $S_{xx}$ therefore cannot be taken from neutron data; \cref{sec:14.4} takes it from …".

### C.20
- l.17 "Its form at low $\omega$ decides the physics." → low content → "Its power law at low $\omega$ fixes the long-time decay of the bath correlation, \cref{eq:C.20-Q}:".
- l.73 "reduces to $\tilde\Delta_0^2/\gamma_0$ in the notation of \cite[Eq.~(10)]{qureshi1995dynamics}" → symbols defined only in the source (pattern 20) → give the limit in book notation, for example "reduces to the overdamped Lorentzian width $\Delta_{\mathrm{r}}^2/(\ldots)$ in the notation of this section~\cite[Eq.~(10)]{…}".
- l.73 "Two effects compete." → count-teaser → "Cooling shrinks the dressed amplitude and lengthens the dephasing time."

### E.14
- l.3 "Three things make the amplitude hard. … And the external screening …" → count-teaser → "The amplitude is hard for three reasons: the band sum …, the density vertex …, and the external screening …".
- l.11 "Everything hinges on one gauge." and "the phases of the sum scramble" → teaser and figurative → "$g$, $\rho_{mn}$ and the energies must be rotated with the same $U(\vect{k})$ …; with a mismatch every band energy is still correct but the phases of the sum are wrong."
- l.13 "with the pair channel beyond that calibration not sized" → nominal pile-up at the end of a 75-word sentence → split: "… for the external factor and the local-field wings. The pair channel beyond that calibration has no estimate; \cref{app:E.16} gives the supercell route."
- l.40, l.46 "Six controls test the physics" / "Two cautions govern the reading" → count-teasers → name them, or start with "The optical limit tests …" and "The form-factor estimate is not a lower bound …".
- l.62 Germanium paragraph, about 430 words in one paragraph → split at "HSE06 with spin--orbit coupling …" (the failure) and at "On bands that pass, …" (the procedure). "A scissor applied to that order gives a confident and wrong window" → anthropomorphic → "… gives a window that is wrong by the Γ–L inversion". "\cite[Fig.~1(a) and text]" → "\cite[Fig.~1(a)]".
- l.64 "On a $4^3$ wavevector grid their transverse-acoustic frequencies came out 13.5 % low" → laboratory-notebook past tense (pattern 19) → "On a $4^3$ grid the transverse-acoustic frequencies are 13.5 % (X) and 11.6 % (L) below neutron data …".
- l.66 "Since the L minimum sets the top of the GaAs band, all three are low-temperature values." → justification aimed at a reviewer (pattern 19) → cut it. "low-temperature conduction minima" earlier in the sentence already says this.
- l.72 "It is perturbative only where the width …" → "It" has no clear antecedent (the Fano term, three sentences back) → "The Fano term is perturbative only where …".
- l.76 "The scissor and valley offsets enter the widths, the detunings and the amplitude identically, and the Fermi level and frozen window … are read from the ground-state run itself." → consistency assurance (pattern 19) → cut it.

### E.15 (REWRITE of the specification paragraphs; the opening and l.9–14 stay)
- l.7, 16, 20, 29, 33, 39, 48, 52 → slot sequence "The quantity is … The method is … The controls are … The acceptance tests are … The cost is … The result enters …" (24 slots). This is the recipe pattern the editor ruled out. Example rewrite for l.39: "A nuclear kick can leave the crystal in a bound exciton … so the exciton lines are needed over the whole zone. The finite-momentum BSE above supplies them on the 29 irreducible points of an $8^3$ grid of $\vect{p}$ and their Umklapp copies …; they must reproduce the optical exciton strength as $\vect{p}\to0$ and close the $f$-sum with the continuum to 1 %, and the run costs 60 to 100 node-hours."
- l.56 "The calculation reuses the HSE06 run with spin--orbit coupling of \cref{app:E.14}" → wrong pointer. E.14 now shows that HSE06+SOC fails the Ge band check and no longer prescribes that run (editor notes) → "The calculation uses the germanium bands that pass the check of \cref{app:E.14} …". Also drop the HSE-specific "Fock cutoff 120 → 160 Ry, exchange grid $3^3\to4^3$" convergence clause. E.14 dropped those settings.
- l.9 "and how it is treated matters" → low content → cut; the next sentence gives the size.
- l.29 "The trap is near Γ" → colloquial slot → "Near Γ the heavy and light holes are degenerate, so scalar masses fail and the hole needs …".
- l.35 one sentence of about 90 words specifying the model chain → split after "$\Eg = 2t$" and after "(checked at four)".

### E.16
- l.9 paragraph of about 380 words → split at "The cost forces two choices" (which also needs de-teasing: "Storing the full matrix is impossible: at …"). "Symmetry gives a free diagnostic" / l.15 "two free diagnostics" → colloquial → "Symmetry gives a check that costs nothing: …".
- l.11 "Two calculations ride on the library." → teaser and figurative → "The library also gives the screening of the current by local fields and the spin channel beyond independent particles."
- l.15 "The quantities are …", "The trap is projecting a line …" → slots → fold in: "Projecting a line that is sharp in $\omega$ before binning gives meaningless coefficients, so $\omega$ is binned first."
- l.34 "Directions: three for a cubic crystal, and for a uniaxial one …" → sentence fragment in list style → "A cubic crystal needs three directions, a uniaxial one the directions parallel and perpendicular to the axis and one oblique."
- l.40 → slots "The quantity is … Convergence is …", and the semicolon list of pitfalls at the end → rewrite as two sentences of cause and consequence.
- Titles: "Static step of a relaxing lattice" → gesturing (pattern 21) → "Static screening with lattice relaxation". "The kinetic-energy row" → "Kinetic-energy response". "A recast for boosted dark matter" → "Boosted dark matter in silicon and germanium" (or keep "recast" and define it in the first sentence).
- l.69 "evaluates it differently" → vague (pattern 0) → "drops the factor $(1-\omega^2/q^2)^2$ and the transverse row".

### E.17
- l.7 "The GaAs phonons and Born charges printed in \cref{sec:5.5} were computed instead at the static-lattice constant 5.638 Å, and the base reports its GaAs frequencies at both." → bookkeeping (pattern 19) → keep it only if a reader would otherwise compare mismatched numbers, as one clause: "(\cref{sec:5.5} quotes GaAs at the static-lattice constant, 5.638 Å)".
- l.11 "those of germanium were 12 to 14 % soft on a coarse grid" → past tense, and rounded differently from E.14 (13.5 % X, 11.6 % L) → "are 11.6 to 13.5 % soft on the $4^3$ grid (\cref{app:E.14})".
- l.13 "The run takes minutes. The magnitude of the result decides an ordering:" → low content → "Its size decides which terms dominate the soft limit: …".
- l.17 "and the later specifications state which they tabulate" → asks the reader to track conventions across sections (pattern 19) → cut it, and state the unit in each table caption instead.
- l.38, 44, 48 → slots "The quantities are / The method is / The acceptance tests are / The cost is" → rewrite as in E.15.
- l.55 "and one value of $Z^*$ is used in both the vertex and the mixing term" → consistency assurance → cut it.
- l.59 "The recipe is uniform:" and l.81 "follow the oxide recipe" → literally the recipe register → "Each candidate gets a relaxation, a zone-centre DFPT run with the field (…), and $4^3$ and $6^3$ wavevector grids for …".
- l.85 "The cost is … They enter \cref{sec:11.8}." → "They" refers back past the cost → "The lifetimes enter \cref{sec:11.8}." "Last, the thermal contraction …" → list sequencing → "The thermal contraction …".
- l.85 "With these tables every material column of \cref{sec:21.7} rests on a measurement or a calculation." → generic close (pattern 0/26) → cut.

### E.18
- l.3 "The Wannier picture of the boost is exact only for a flat band; and a scalar that couples …" → semicolon plus "and" joins two unrelated facts → make them two sentences.
- l.35 "The bookkeeping pitfall is the one \cref{sec:12.3} warns about." → abstract frame → "The Migdal term must not be added to a lattice response computed with the bare mass and unit weight (\cref{sec:12.3}): …". The 70-word sentence "A response diagonal in $\vect{G}$ keeps …, and this calculation is what sizes them." → split before "and drops the elements".
- l.46 "The method therefore takes only the bare perturbation (…), which \texttt{ph.x} computes but does not write out, so a small modification of the code is needed; evaluates …; and screens it …" → broken parallelism; the verb series is interrupted by a consequence clause → "The method takes only the bare perturbation …, evaluates …, and screens it …. \texttt{ph.x} computes the bare change but does not write it out, so the code needs a small modification."
- l.64 "The two pitfalls err in opposite directions." → the pitfalls named next (missing Umklapp terms; screening twice) are not shown to have opposite signs → "Two pitfalls: a diagonal dielectric matrix misses every Umklapp term, and screening the $\vect{G}=0$ term again double counts $1/|\varepsilon|^2$." Also l.64 "It is accepted when …" → "It" is ambiguous → "The calculation is accepted when …".

### E.19
- l.7 "The band is absolute. It is wide at the peak, … It bounds bin-integrated rates in the bulk …" → restates C.10 at length (pattern 26 across sections) → one sentence plus a pointer: "The Markov--Krein band of \cref{app:C.10} then brackets every response with these moments; it bounds bin-integrated rates in the bulk and threshold rates only from above."
- l.9, 35, 44, 46, 57, 59 → slots → rewrite as in E.15. l.13, 39, 55 already read as prose; use them as the model.
- l.15 "The pitfalls decide what may be quoted." → fine as a topic sentence. Keep it.

### E.20 (REWRITE of the specification paragraphs; the opening and l.7, 21 stay)
- l.7, 15, 26, 28, 32, 36, 38, 42, 46, 50, 52, 54 → slot template (23 slots). l.11 and l.17 stack "And …" sentence openers into a checklist. Rewrite each subsection as problem → method → what checks it → what it costs.
- l.17 "Finally, a Wannier tight-binding model …" → sequencing narration → drop "Finally".
- l.28 "Pad\'e continuation produces artifacts near $2\Delta_{\mathrm{BCS}}$." → stray sentence with no consequence → "…, so the real-axis solution is used within $5\Delta_{\mathrm{BCS}}$ of the edge."
- l.32 "for the shells that matter" → vague → name them ("to the third neighbor shell" or whatever 14.1 uses).
- l.50 "the implemented row of Geilhufe et al." and the table caption "from the implemented rows of Ref." → process jargon → "the parameters Geilhufe et al. use in their rate~\cite[Tables~1 and 2]{…}".
- l.52 "and is used for nothing else" → defensive (pattern 19) → cut.
- l.54 "so the factor 0.55--0.62 that a recalculation with only its imaginary part needs is not applied to them as well" → aimed at a reviewer (pattern 19) → cut, or "Their curves keep the real part of the Dirac polarization and need no further factor."
- l.54 "(the source prints $v_{D,z}$ in its Eq.~(3.14))" → hard-coded source equation outside \cite → "(a misprint in \cite[Eq.~(3.14)]{geilhufe2020dirac})". "The re-plot takes CPU minutes" / table "re-plots" → "The recalculation takes minutes".
- l.42, l.46 → trailing spaces after the last sentence (cosmetic).

### E.21 (REWRITE of the specification paragraphs; openings stay)
- l.12, 14, 18, 20, 26, 28, 32, 34, 38, 45, 49, 57 → slot template (21 slots).
- l.14 "with a 1728-atom PBE cell as the third size if it is not" → "it" has no antecedent → "… and from 512 to 1000 atoms; if it is not stable, a 1728-atom PBE cell is added."
- l.28 "The transition densities are taken on a real-space grid …, Fourier transforms them, builds the intermolecular coupling …, and diagonalizes the Frenkel Hamiltonian" → the subject changes partway (the densities cannot Fourier transform themselves) → "The code takes the transition densities on a real-space grid …, Fourier transforms them, builds …, and diagonalizes …".
- l.32 "for tubes of radius $r_{\mathrm{t}}$ and stacks of period $a_s$" → dangling, attached to nothing → move to where $r_{\mathrm{t}}$ and $a_s$ are first used (l.32, second sentence).
- l.51 "The STE and F--H energies" → abbreviation never defined → "The self-trapped-exciton and F--H pair energies".
- l.22 "Redoing the integral with their Lindhard $\varepsilon(q,\omega)$ takes minutes and fixes the impact on their curves." → reads as a to-do note → "Redoing the integral with their Lindhard $\varepsilon(q,\omega)$ gives the corrected curves; it takes minutes."

### E.22
- l.13 "Two numerical errors matter more than the counting." → teaser → "$\vect{k}$ sampling and smearing blur the Fermi surface …" as the opening.
- l.40 "A climbing-image elastic band" → write "nudged elastic band" as everywhere else.
- l.85 "…the inputs on which the delayed-release and low-energy-excess estimates of \cref{sec:19.6} stand or fall." → cliché and recap after the table (patterns 25, 26) → cut. Each subsection already names its entry point.

### E.23
- l.37 "Three double countings must be avoided." → only the first (friction plus kernel) is a double counting; dropping carriers and premature thermostat absorption are losses → "Three errors must be avoided: …".
- l.76 "They share one potential, one quench and one table of configurational energies, and the yield below the threshold … depends on all of them" → restates l.21 (pattern 26). "All of them" also includes track recombination, on which the sub-threshold yield does not depend → cut the paragraph, and keep the table pointer in l.3.

### E.24
- l.13 "For germanium the pair energy at 77 K is an input to be fixed by a measurement made with the same definition before it serves as a test." → hard to parse → "For germanium no measurement at 77 K uses the same definition of the pair energy; until one does, the germanium value is an input, not a test."
- l.21 "The results enter \cref{sec:18.4} as … replacing the estimates of \cref{sec:18.4}." → the section is named twice (pattern 17) → "… and replace its estimates."
- l.15, 19, 57 count-teasers (Sect. 3); l.21 units (Sect. 3).

### E.25
- l.3 "What the chapters cannot yet supply are these numbers for a stated detector, and the readout verdicts of \cref{sec:20.5} wait on them." → "these numbers" has no antecedent, and "verdicts … wait" is figurative (pattern 25) → "The chapters do not supply the rates, kernels and efficiencies of a stated detector, and the readout comparison of \cref{sec:20.5} is conditional until they are computed." Also "strings the steps together" → "chains the steps".
- l.9 "with four additions, of which the exciton module is new code. The trap occupations … carry over …, trap energies …, the electrostatic energy …, and the drift …" → four additions are listed and the exciton module is a fifth item → "with four additions (…); the exciton module is new code."
- l.11 "are both reproduced by the same parameter set" → reads as an achieved result, but this is a specification → "must both be reproduced by one parameter set".
- l.17 "(Heaviside--Lorentz units, with $\varepsilon_0$ the static dielectric constant; $en_s/(\varepsilon_0\varepsilon_0^{\mathrm{SI}})$ in SI)" → $\varepsilon_0$ is used for the relative static constant next to $\varepsilon_0^{\mathrm{SI}}$ for the vacuum permittivity: a symbol clash at first use → use the NOTATION symbol for the static relative permittivity (for example $\varepsilon_{\mathrm{s}}$, or the book's $\varepsilon(0)$) and write "$e n_s/(\varepsilon_{\mathrm{s}}\epsilon_{\mathrm{vac}})$ in SI".
- l.31 "None exists; it is trained on …" → the present tense describes training that has not been done → "None exists; one has to be trained on …".
- l.43 "Four pitfalls decide the sign or the size of the answer." → teaser; and "And the engine has to pass …" → cut the teaser and join the last item with a semicolon.
- l.49 "The soft end is not hypothetical:" → negation framing (pattern 6) → "Soft surface spectra are measured: in germanium …".
- l.67 "must pass four tests … The fourth test is …" → tests one to three are never numbered, so "fourth" does not resolve → drop "four" and "fourth", or number all four.

### E.26
- l.19 title "Two insertions" → gesturing (pattern 21) → "Pair absorption, dark Compton scattering and the Barkas term".
- l.9 "(estimated from typical scalar-relativistic shifts)" → vague hedge → give the shift used (for example "with $\delta^a_{\mathrm{rel}} \approx -0.5$ to $-1$ % for Cu") or cite it.
- l.21 "The source takes a local density of 0.39 GeV cm⁻³" → "the source" is ambiguous → "Bauer et al. take …~\cite{bauer2026dark}". "It is new code of about $10^2$ core-hours" → "It" is ambiguous → "The Barkas table is new code …".
- l.17 "The size of the defect is therefore open until both are computed, and this calculation computes both." → circular → "This calculation computes both, which fixes the size of the defect."
- l.23 closing recap → cut (Sect. 3).

### E.27
- l.30 "These are the stream kernel $\mathsf{k}_i$ and the measure $\Xi$ of \cref{eq:21.2-stream}, written here in the notation of a general linear program; \cref{app:C.12} writes the same problem with $\mathsf{k}_i$, $\Xi$, the objective $\mathsf{f}$ and the dual weights $\lambda_i$, which are $\mathfrak{h}$ and $\xi_i$ below." → a third set of symbols ($\mathfrak{K}_i$, $F$, $\mathfrak{h}$, $\xi_i$) for the program that Ch. 21 and C.12 already write with $\mathsf{k}_i$, $\Xi$, $\mathsf{f}$, $\lambda_i$. This breaks one symbol, one meaning, and the sentence exists only to translate → use the C.12 symbols throughout E.27 and delete the sentence.
- l.46 "measured by Gordon et al. at five sites" → no citation → add the citation (the JEDEC sea-level neutron spectrum paper), or attribute it through \cite{saldanha2020cosmogenic} if that is where the spectrum is taken from.
- l.52 "Two pitfalls give zero for the wrong reason." → the second (even–even isotopes contribute nothing) is a correct zero → "Reusing the coherent one-phonon response with spin weights gives zero for the wrong reason, because …; even--even isotopes contribute nothing, so …".
- l.26 "and each needs one computation that the book explains but does not report. They complete the inputs …" → low content → "Each needs one computation, specified below."
- l.40 "the support constraint lives in the galactic frame" → "is imposed in the galactic frame". "the bound with a defect of \cref{sec:21.2-leak}" → unclear → "the leakage-corrected bound of \cref{sec:21.2-leak}".
- l.52 "survivors" (also in l.46, 50) → the term is defined only in Ch. 21 → at first use write "the targets retained in \cref{sec:21.7} (the survivors)".

## 5. Calibration against the register (REGISTER §6.13)
- C.16 l.124 ("Emission into a mode that already holds $n$ photons is therefore $n + 1$ times faster …") and C.20 l.117 ("A wide kink is light: … because moving it by one spacing moves each of many atoms by a small fraction of a spacing") could have been written by Lin: an estimate, a picture, then the reason.
- E.22 l.25 (the $\lambda_{\mathrm{tun}} = 27.5$ estimate against the 23.6 threshold) is the model for App E: a number, a verdict, and the precision that follows.
- E.17 l.38 is not in the register. Lin-style rewrite of its core: "Path-integral MD with i-PI on the machine-learned potential gives the momentum distribution to all orders in the anharmonicity; at 10 K silicon would need about 250 beads, so we run at 50 to 100 K with a colored-noise thermostat and correct to zero temperature with the harmonic difference."
