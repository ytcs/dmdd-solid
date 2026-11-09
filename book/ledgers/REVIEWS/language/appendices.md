# Language audit: appendices (reviewer, read-only)

Brief: briefs/reviews/language-audit.md. Scope: tex/appA (all), tex/appB/appB.tex and B-2.tex (B-1 and B-3 are generated and not reviewed), tex/appC, tex/appD, tex/appE (appE.tex and E-1 to E-27; appE-gate.tex is the gate copy and is not in main.tex), tex/appF (appF.tex opening and F-rows.tex row text).

## Method
- Ran `skills/long-form-writing/scripts/lint.py --banned BANNED-TERMS.txt` on every file in scope: 558 hits, 0 blocking. Language hits: 1 PERIPHRASIS (A-1:45, "signature of most particle-physics texts", a false positive for the metric signature), 1 MONOTONY (D-11, derivation text, no action). The rest are EQ-PUNCT (50, not language), and LONG-SENT/DASH in F-rows (table cells, by design).
- Read in full: the appendix openings (appB, appE, appF; appA, appC and appD have none), the first paragraph of every section, all captions and key-result boxes, the last paragraph of every section in C, D and E (pattern 26), and the subsection openers of C and E.
- Body: read all of appA and B-2. Skimmed C, D and E with targeted searches (metaphor nouns, self-narration, count-teasers, negation framing, bare "transfer", process artifacts). F-rows: read the opening and a sample of rows (Sects. 1.3–2.2, 15.4–16.2, 20.3–21.2), then searched the whole table.
- Overall: the appendices are in good shape. There are no figurative openers and no "silence"/"pull" periphrasis. The recurring faults are mechanical: "This appendix" in 28 sections of App. D, count-teasers, a few private metaphor nouns ("layer", "machinery", "pitfall", "engine", "recipe"), and some self-narrating roadmap sentences.

Items: 22 MUST (G1 covers 28 files), 30 OPTIONAL; 3 physics doubts.

## Global items

G1. MUST. tex/appD/D-{1,2,3,4,5,6,7,8,9,10,11,12,14,16,17,18,19,20,21,22,23,26,27,28,34,39,40,45}.tex:3 → "This appendix evaluates/proves/derives/carries out/supplies/solves/writes/first/bounds/collects …" → "This section …". Each D-n is a \section that the text cites as "Sect. D.n" (\crefname{section}{Sect.}), and Apps. C and E already write "This section". Change only those two words in each of the 28 files.

G2. OPTIONAL (REGISTER #6, "momentum transfer, always the full noun"). Bare "transfer" for q: A-3:69 "a transfer $\vect{q}$ is split" → "a momentum transfer $\vect{q}$ is split"; A-4:14 title "Direction of the transfer" → "Direction of the momentum transfer"; A-6:65 "of a transfer $\vect{q}$ to nucleus" → "of a momentum transfer $\vect{q}$ to nucleus"; A-7:10 and B-2:72 "$\vect{k}$ for the transfer" → "$\vect{k}$ for the momentum transfer"; C-17:95 "so a transfer whose Umklapp vector" → "so a momentum transfer whose Umklapp vector"; E-13:81 "the transfers reach $2k_E$" → "the momentum transfers reach $2k_E$". (E-13:40 "the transfer $(\vect{q},\omega)$ to the pair" can stay, since it names energy and momentum together.)

G3. OPTIONAL (REGISTER calibration). Rates per 10k words, with Lin's rate in parentheses: "so" 28–37 (11), "gives" 20–27 (7), "only" 21–25 (11), "therefore" 6–9 (3), and 0–0.8 "however" (8). In C, D and E this is the main register gap. When the reviser rewrites the items below, prefer "then", "which means", "and" or a plain new sentence over "so"/"therefore", and vary "gives" with the specific verb ("is", "fixes", "yields", "reduces to"). Do not run a mechanical sweep.

G4. OPTIONAL (target 1, chapter openings). appA, appC and appD start straight with their first \section, while appB, appE and appF have an opening paragraph. Editor's call whether to add one. If added, each should be one sentence that names the members, for example:
- appA.tex:1 → (add) "This appendix fixes the units and signs of the book, from natural and Heaviside–Lorentz units to the Fourier, Bloch, phonon, response, halo and cross-section conventions, and gives for each the conversion from the main conventions of the literature."
- appC.tex:2 → (add) "The chapters use, without proof, the delta-function and Fourier identities, the Kramers–Kronig relations, Gaussian and matrix identities, special functions, moment problems, branching processes, linear programs, likelihoods, group theory and elasticity; each is derived here in the book's conventions."
- appD.tex:1 → (add) "Each section completes a derivation that a chapter states and uses, in the chapter's notation."

## App. A

A1. MUST (patterns 24/25). A-2:17 → "The dielectric response of a solid is then expressed in the same units, and the bridge between them is free of stray factors." → "The dielectric response of a solid is expressed in the same units, so the relation between the structure factor and the loss function carries no factors of $4\pi$."

A2. MUST (pattern 0, deletion test). A-3:74 → "One statement of the identification removes the ambiguity." → delete. The sentence before it already states the identification.

A3. OPTIONAL. A-1:7 → "Four products do all the work." → "Four constants suffice:" (and join it to the next sentence), or delete.

A4. OPTIONAL (two negations in a row). A-4:12 → "Nor is $\omega$ restricted to positive values: an expression that holds only for $\omega > 0$ says so." → "The book does not restrict $\omega$ to positive values; an expression that holds only for $\omega > 0$ says so."

A5. OPTIONAL (evaluation). A-5:10 → "This is the convention of Ref.~[giustino2017electron, Eq. (29)], the standard reference for first-principles electron–phonon calculations." → "This is the convention of the review of first-principles electron–phonon calculations, Ref.~[…, Eq. (29)]."

A6. OPTIONAL (unclear phrasing). A-8:13 → "…; a comparison with them changes the halo first." → "…; to compare with them, first change to their halo parameters."

## App. B (B-2 and appB.tex)

B1. OPTIONAL (count-teaser, though the four items are named in the \emph labels that follow). B-2:64 → "Four conventions differ from parts of the literature by a sign or a factor rather than by a letter, and a formula taken from a paper must be converted before it is combined with the book's." → "The Fourier sign, the sign of the mixing term, the units of charge and the normalization of the structure factor differ from parts of the literature by a sign or a factor rather than by a letter, and a formula taken from a paper must be converted before it is combined with the book's."

appB.tex: no items.

## App. C

C1. MUST (pattern 18, count-teaser). C-1:24 → "Two integrals come first." → "The golden-rule limit rests on two integrals, $\int_0^\infty\dd u\,\sin u/u = \pi/2$ and $\int\dd u\,\sin^2u/u^2 = \pi$."

C2. MUST (pattern 18, category frame). C-5:3 → "This section derives the statements behind such results. They are analyticity of a retarded function in the upper half of the complex frequency plane, the Kramers--Kronig relations and the sum rules that follow from them, and the continuation of a function known at the imaginary Matsubara frequencies to real frequencies." → "This section derives the analyticity of a retarded function in the upper half of the complex frequency plane, the Kramers--Kronig relations and the sum rules that follow from them, and the continuation of a function known at the imaginary Matsubara frequencies to real frequencies."

C3. OPTIONAL (pattern 22). C-3:3 → "…which we derive here with every step." → "…which is derived here in full."

C4. OPTIONAL (count-teaser). C-8:3 → "This section gives the properties used there and the numbers they produce. It then treats two other closed forms. The complete elliptic integrals appear when … The logarithm of the Lindhard function …" → "This section gives the properties used there and the numbers they produce. It then treats the complete elliptic integrals, which appear when …, and the logarithm of the Lindhard function of the electron gas (\cref{sec:4.5}), which needs a branch at real frequencies."

C5. OPTIONAL. C-10:3 → "…and state what changes when the distribution lives on $\omega \ge 0$." → "…when the distribution is supported on $\omega \ge 0$." The same applies at D-46:17, "lives on the ball" → "is supported on the ball".

## App. D (besides G1)

D1. MUST (unclear referent). D-24:3 → "Four steps take it there: the invariants …, and the identities that relate the rows on shell. It then treats nuclei, the spin traces of the dark-matter-side tensor, and the kinematics of absorption." → "…on shell. This section then treats nuclei, the spin traces of the dark-matter-side tensor, and the kinematics of absorption." Here "It" reads as "the reduction".

D2. MUST (overloaded sentence, two readings needed). D-36:3 → "We derive both, and the screened loss function that \cref{sec:13.4} uses, from second-order time-dependent mean-field theory, with the band-sum theorem as a by-product, the rate from the optical theorem, two solvable limits, and the extra source of an adiabatic local-density kernel." → "We derive both, and the screened loss function that \cref{sec:13.4} uses, from second-order time-dependent mean-field theory; the band-sum theorem follows as a by-product. The section then obtains the rate from the optical theorem, works two solvable limits, and adds the extra source term of an adiabatic local-density kernel."

D3. OPTIONAL (pattern 22). D-12:3 → "We will see which first-order diagrams produce the exchange and the direct kernels, and with which signs." → "The first-order diagrams fix the exchange and direct kernels and their signs."

D4. OPTIONAL (pattern 22). D-29:3 → "The conversions between the normalizations in use close the section." → "The last subsection converts the rate to the normalizations in use." Or delete.

D5. OPTIONAL (pattern 22). D-47:3 → "Nuisances whose sign is known and the removal of cells from the signal follow." → "The last two subsections treat nuisances of known sign and the removal of cells from the signal."

D6. OPTIONAL (process artifact). D-1:3 → "…; the adopted values give $v_{\mathrm{E}}/v_{\mathrm{esc}} \le 0.49$." → "…; the values of \cref{app:A.8} give $v_{\mathrm{E}}/v_{\mathrm{esc}} \le 0.49$." The same applies at D-1:89, "For the adopted parameters" → "For the parameters of \cref{app:A.8}".

D7. OPTIONAL (pattern 24). D-39:3 → "the one quadrature recipe for the conserving response" → "the single quadrature formula for the conserving response"; D-39:24 → "This one recipe gives every value of …" → "This one quadrature gives every value of …".

## App. E

E0. MUST (wrong direction, in the Summary). appE.tex:35 → "The specifications that follow share one discipline: each calculation is accepted against an exact limit or sum rule …" → "The specifications of \crefrange{app:E.14}{app:E.27} share one rule: each calculation is accepted against an exact limit or sum rule …". The Summary comes after them, so "that follow" is wrong.

E1. MUST (pattern 24, "layer" for a part of a calculation). E-19:7 → "The calculation therefore has two layers, exact moments and an approximate real-time response tested against them." → "The calculation therefore has two parts, exact moments and an approximate real-time response tested against them." Then E-19:9 "The static layer is …" → "The static part is …", and E-19:11 "The dynamic layer compares …" → "The dynamic part compares …".

E2. MUST (pattern 24). E-24:11 → "The pair number is computed in two layers." → "The pair number is computed in two stages."

E3. MUST (patterns 6/25, negation and story metaphor). E-5:43 → "The dipole is not the whole long-range story. A displaced atom also carries a dynamical quadrupole, which …" → "Besides its dipole, a displaced atom carries a dynamical quadrupole, which …".

E4. MUST (undefined referent). E-16:3 → "The library and the calculations built on it or beside it use the methods of \cref{app:E.6,app:E.7}." → "A library of these matrices, and the calculations that use it, follow the methods of \cref{app:E.6,app:E.7}." The sentence before it never introduces "the library".

E5. MUST (unclear referent, "verdicts"). E-25:3 → "The chapters do not supply the rates, kernels and efficiencies of a stated detector, and the readout verdicts collected in the Summary of \cref{chap:20} are conditional until they are computed." → "The chapters do not supply the rates, kernels and efficiencies of a stated detector, and the readout conclusions in the Summary of \cref{chap:20} stay conditional until these are computed."

E6. MUST (pattern 18, count-teaser). E-8:85 → "The method has a limit that matters for detectors. Being adiabatic, it does not distinguish …" → "Being adiabatic, the method does not distinguish …" (delete the first sentence).

E7. MUST (pattern 18). E-12:20 → "Two bulk processes remove a phonon from its ballistic path." → "Isotope scattering and anharmonic decay remove a phonon from its ballistic path."

E8. MUST (pattern 18). E-12:99 → "Three inputs carry errors that no closure check sees." → "No closure check sees the errors in three inputs: the sound speed used to convert a decay calculation to the fifth-power law, the starting phonon spectrum, and the surface, intervalley and trapping parameters." Then shorten the three sentences that follow accordingly.

E9. MUST (pattern 18; the count also misleads, since three items follow). E-6:92 → "Two errors of bookkeeping are easy to make and hard to see." → "Three settings are easy to get wrong and hard to spot afterwards: the head element, the reciprocal-lattice index of the momentum transfer, and the broadening."

E10. MUST (pattern 18, three items follow). E-8:97 → "Two artifacts are easy to mistake for physics." → "Three numerical effects are easy to mistake for physics: the band splitting from the $\vect{Q} = -\vect{Q}$ modes, the imaginary broadening of the AHC denominators, and the missing edges of phonon-assisted absorption."

E11. MUST (pattern 18, a "pitfall" teaser). E-13:85 → "The last pitfall is interpretive. Two models that reproduce the same $\varepsilon_{\mathrm{eh}}$ do not validate each other's $F_{\mathrm{eh}}$, …" → "Two models that reproduce the same $\varepsilon_{\mathrm{eh}}$ do not validate each other's $F_{\mathrm{eh}}$, …" (delete the first sentence).

E12. MUST (pattern 18). E-22:57 → "One pitfall is physical. Below $q = 2\pi/L$ the periodic cell forces …" → "Below $q = 2\pi/L$ the periodic cell forces …"; and in the same line "The other pitfall is a shortcut: rebuilding the density change from Born effective charges places …" → "Rebuilding the density change from Born effective charges places …".

E13. OPTIONAL (same "pitfall" label). E-22:65 "The main pitfall is the preparation of the glass." → "The result depends most on how the glass is prepared."; E-24:51 "The main pitfall is the commensurability of the phonon step." → "The phonon step must be commensurate with the energy grid."; E-4:149 "A pitfall that has nothing to do with the physics catches many users: the ordering of the shear rows." → "Codes differ in the order of the shear rows."; E-1:104 "smearing an insulator is a pitfall in its own right, taken up at the end of this section" → "smearing an insulator is an error, discussed at the end of this section".

E14. OPTIONAL (pattern 24). E-4:3 → "Here we use them: the machinery that gives a phonon also gives, with an electric field or a strain in place of the displacement, …" → "Here we use them: the same linear-response equations that give a phonon also give, with an electric field or a strain in place of the displacement, …". E-21:53 "from the tunneling-path machinery of \cref{app:E.22}" → "from the tunneling-path calculation of \cref{app:E.22}".

E15. OPTIONAL (pattern 26 plus pattern 24). E-10:64 → "Each defect property in the book thus rests on a few large calculations with controls that the perfect crystal does not need: … The machinery that extends these calculations to millions of atoms and to the statistics of nuclear-recoil cascades is the subject of \cref{app:E.11}." → keep the first sentence only if its three controls are not already listed in the subsections above (they are, so prefer deleting it), and replace the second with "\Cref{app:E.11} extends these calculations to millions of atoms and to the statistics of nuclear-recoil cascades."

E16. OPTIONAL (pattern 24). E-25:43 "the engine has to pass the film validation" → "the transport code has to pass the film validation"; E-25:67 "the engine that produces it is tested before any kernel is trusted" → "the code that produces it is tested before any kernel is trusted". E-12:73 "handled there with the hole recipe" → "handled there as for holes".

E17. OPTIONAL (pattern 0). E-9:103 → "The two halves of this section rest on different foundations." → "Exchange constants and Eliashberg gaps carry uncertainties of different kinds." (The rest of the paragraph stays.)

E18. OPTIONAL (pattern 22, repetition). E-1:3 → "Here we will follow one calculation of silicon from its input to its bands and masses, and see which of its numbers can be used as they stand. The worked numbers come from one calculation: the PBE functional, …" → "We follow one calculation of silicon from its input to its bands and masses, and test which of its numbers can be used as they stand: the PBE functional, …".

E19. OPTIONAL (pattern 18, recap opener). E-3:3 → "For an electronic threshold this correction of more than half an eV is the largest a calculation makes, and \cref{sec:3.4} showed how it moves … ; \cref{sec:4.8} defined the $GW$ self-energy … Here we will see how the corrections are computed in practice, … We will also see what they do to …" → split after "makes." Then: "Its effect on the minimum mass, on the gap and on the velocities is in \cref{sec:3.4}, and the $GW$ self-energy $\Sigma = \ii\GF W^{\mathrm{scr}}$ and the electron–electron lifetime are defined in \cref{sec:4.8}. This section computes the corrections in practice, from a scissor shift to a full one-shot $G_0W_0$ calculation and its self-consistent successors, and shows what they do to the energies, lifetimes and matrix elements of a rate and which parameters must be converged, at what cost."

E20. OPTIONAL (caption). E-3:48 → "Minimum band gaps of the running semiconductors in LDA, …" → "Minimum band gaps of silicon, germanium and GaAs in LDA, …".

E21. OPTIONAL (pattern 18, category frame). E-19:3 → "The calculations below supply what \cref{sec:11.5,sec:14.5,sec:16.7} need for these cases. They are the moments and approximate dynamics of …" → "For \cref{sec:11.5,sec:14.5,sec:16.7} the calculations below supply the moments and approximate dynamics of …".

E22. OPTIONAL (pattern 24). E-14:3 → "Everything else is the chain of standard steps that \cref{app:E.5} follows link by link, including its operation count." → "Everything else follows the standard steps of \cref{app:E.5}, including its operation count."

E23. OPTIONAL (negation). E-17:11 → "…with a tolerance per branch, since PBE at the measured lattice constant is not uniformly wrong." → "…with a tolerance per branch, since the error of PBE at the measured lattice constant differs from branch to branch."

E24. OPTIONAL (pattern 26, roadmap ending). E-1:153 → "The bands and the density of a converged ground state are the starting point of every later section of this appendix." → delete. The next sentence already says where the bands go.

E25. OPTIONAL. appE.tex:3 → "\Crefrange{app:E.14}{app:E.27} turn this around and specify, quantity by quantity, …" → "\Crefrange{app:E.14}{app:E.27} go the other way and specify, quantity by quantity, …".

## App. F

F1. MUST (needs a second reading). appF.tex:2 → "Each row of \cref{tab:F-rows} records a published formula that the book recovers as a limit, with what a Limit Check leaves to the running text: the source equation, the approximation chain, the conditions of validity and the leading correction." → "Each row of \cref{tab:F-rows} records a published formula that the book recovers as a limit, together with four items that its Limit Check does not state: the source equation, the approximation chain, the conditions of validity and the leading correction."

F2. MUST (pattern 0). F-rows.tex:2 → "The table is set in landscape." → delete.

F3. OPTIONAL (arrangement). F-rows.tex:2 → "The Leading-correction column opens with the size of that correction in bold, taken from the text, the Limit Check or its figure; \Fsize{unsized} marks a correction that the book does not yet size." → move this sentence to the end of the opening paragraph in appF.tex, so that all column conventions are in one place. Keep the wording.

F4. No other items in the row text. The cells are deliberate note form ("Chain: … $\to$ …", "Published form: …"), and the convention notes about a source's equation ("The source's Eq. (6) exceeds …", "a misprint in …") are comparisons with the literature that the table exists to record (pattern 19 allows them).

## Physics doubts (for the editor; no change made)

P1. D-13:3. "A silicon nucleus is $5.10\times10^4$ times heavier than an electron … At equal forces it moves that much more slowly". For equal force constants the time scales differ by $\sqrt{M/m_e} \approx 226$, and zero-point speeds by $(M/m_e)^{3/4}$. Only for equal momenta is the speed ratio $M/m_e$. As written, the sentence implies a factor $5\times10^4$. Suggest the editor check the intended statement (for example, "At equal forces its vibrations are $\sqrt{M/m_e} \approx 230$ times slower").

P2. E-18:3 against D-13:3 and C-6. The drag-mass ratios $14\,m_e \leftrightarrow 2.73\times10^{-4}$ and $28.7\,m_e \leftrightarrow 5.60\times10^{-4}$ imply $M = 26.16$ GeV, the natural-abundance mean atomic mass of Si. D-13 and C-6 use $M = 26.06$ GeV for $^{28}$Si. The difference is 0.4%, but the book should say which mass is meant, or use one.

P3. C-20:3. "the result is a hopping rate that grows as the temperature falls" holds for $\alpha_{\mathrm{ohm}} < 1/2$ only, since $\varGamma \propto T^{2\alpha_{\mathrm{ohm}}-1}$ (\cref{eq:C.20-ohmrate}). Consider "…that, for weak coupling ($\alpha_{\mathrm{ohm}} < 1/2$), grows as the temperature falls".

P4. Spot-checked numbers with no doubt found: A-1 (speed in units of c, $\SI{1}{kg^{-1}.yr^{-1}}$ conversion), A-2 ($\omega_p = 16.6$ eV), A-4 ($\beta\omega > 10^5$), A-9 (factor 16), E-2 (1800 Ry), E-6 ($\Omega$), E-9 (750 Matsubara frequencies), E-11 (26 km/s), E-13 (13 pairs, 35 eV), E-23 (25%), E-24 (14%), E-26 (1.04 ms, 249 m), F-rows:569 ($k_{\mathrm{F}} = 282$ eV), C-15 ($Z\alpha$), C-17 (48 operations).

## Notes outside language scope
- appD.tex:29 still has `\setcounter{section}{27}`. STYLE.md ("Appendix numbering") says such lines are removed once all sections exist, and D-1 to D-47 now all exist. Removing it should not change numbering, since D-28 follows D-27, but the editor should confirm with a build.
- A-1:45: lint PERIPHRASIS false positive ("signature of most particle-physics texts", meaning the metric signature). No change.
