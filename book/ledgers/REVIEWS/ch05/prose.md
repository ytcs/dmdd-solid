# Ch. 5 prose review (style and register, isolated)
Scope: tex/ch05/ch05.tex, s5-1 … s5-7 (summary in s5-7), App. D.13–D.15, App. C.18. Against STYLE.md, style-guide.md, prose-review.md, REGISTER.md. No tex edited. Line numbers are those of each file.

## 1. Lint (lint.py --banned BANNED-TERMS.txt)
Banned/internal-label hits: 0 in every file. No "you", "I", "let's", i.e./e.g., "in order to", thereby/whereby, "respectively", "one finds", em dashes, itemize/enumerate. No `limitbox` in Ch. 5. Candidates for the structural editor (not a prose ruling): the Klemens law \cref{eq:5.7-klemens} with fig5-decay(c), and the Debye DOS with fig5-si(b), both already comparison plots. No exercises or tasks for the reader.
- EQ-PUNCT s5-2:8, s5-2:82, s5-3:105, s5-4:74, s5-6:135, s5-7:8, :33, :50, C-18:53 → false positives: `gathered`/`split`/`aligned` with the comma or period on the last line inside the environment. All fine.
- EQ-PUNCT s5-4:24 (equation* ending "…\ee^{\ii\vect{Q}\cdot\vect{R}_s}") → the display is the subject of "holds exactly" on the next line, so no mark is needed. Fine.
- LONG-SENT s5-1 (×3): l.29 "Inserting the expansion…" (acceptable), l.41 "The electrons then stay in one adiabatic state, for an insulator…" (comma splice; fix below), l.113 "The same differentiation…" (acceptable).
- LONG-SENT s5-2 (×4), s5-3 (×3), s5-4 (×2), s5-5 (×2), s5-7 (×2), D-13 (×1), D-15 (×1): captions, table caption, or a sentence carrying a display; the only one to split is the 5.3 table caption (below).
- TITLE D-15:1 "The Bloch identity and the Debye--Waller factor" → two-item title; see D.15.

## 2. Verdicts
| Unit | Verdict | Basis |
|---|---|---|
| Chapter opening (ch05.tex) | PASS | motivational, concrete, one orienting closing sentence |
| 5.1 Born–Oppenheimer | REVISE | 7 hits / 3.1k words + structural overlap with D.13 |
| 5.2 Harmonic crystal | REVISE | 7 hits / 4.3k + long roadmap opener |
| 5.3 Phonons | PASS | 5 minor hits / 3.3k |
| 5.4 First principles | REVISE | 8 hits / 3.7k + register tic ("gives" 46 per 10k, L 7) |
| 5.5 Polar crystals | REVISE | 6 hits / 3.3k + structural overlap with D.14 |
| 5.6 Displacement correlations | PASS | 5 minor hits / 3.6k |
| 5.7 Anharmonicity | PASS | 4 minor hits / 3.4k |
| Summary (s5-7) | REVISE | missing the practical 5.5 conclusion; one wrong number |
| App. D.13 | REVISE | one factual misstatement; overlap with 5.1 |
| App. D.14 | REVISE | comma splice (editor item), process sentence, overlap with 5.5 |
| App. D.15 | PASS | title, normalization wording (editor item), notation |
| App. C.18 | PASS | two minor |

## 3. Issues by section (location → problem → fix)

### Chapter opening (ch05.tex)
- l.3 is good: concrete opener (0.33 MeV, 1.17 eV, 64 meV, 18 keV), three physical questions, one orienting closing sentence. Keep. The three rhetorical questions are motivational, not pattern 8.

### 5.1
- l.3 "the derivations are written out in \cref{app:D.13}" → but l.5–79 then reproduce D.13's coupled equations, $\mathcal N_{ji}$, and the power counting nearly sentence for sentence (compare s5-1 l.29–39, 67–79 with D-13 l.20–34, 63–74) → pattern 5 across files. Fix: 5.1 keeps eq. 5.1-H, 5.1-BO, 5.1-scales, the keyresult and the picture; replace the derivation of 5.1-coupled/5.1-N by one sentence plus the displayed result and "(derived in \cref{app:D.13})"; cut the non-adiabatic counting paragraph l.79 to its conclusion. D.13 keeps the full derivation.
- l.41 "The electrons then stay in one adiabatic state, for an insulator at low temperature the ground state, and the nuclei move in its energy:" → comma splice. Fix: "The electrons then stay in one adiabatic state (for an insulator at low temperature, the ground state), and the nuclei move in its energy:".
- l.48 "a function of the $3N_{\mathrm{at}}$ coordinates of the $N_{\mathrm{at}}$ nuclei of the crystal" → NOTATION defines $N_{\mathrm{at}}$ as atoms per (super)cell. Fix: "of the $3n_{\mathrm{at}}N$ coordinates of the nuclei of the crystal".
- l.61 "The clamped-nuclei approximation therefore misses three things that matter for detection." → count-teaser (pattern 18). Fix: "The clamped-nuclei approximation therefore has no phonons, the only excitations below the gap, no phonon-assisted transitions…, and no zero-point renormalization of the gap…" (fold the next three sentences in).
- l.129 "and its size we check against the counting below" → inverted, vague pointer. Fix: "and \cref{we:5-kappa} checks its size against the counting."
- l.134 caption (b) "Gray dashed: the estimate $\kappa_{\mathrm{BO}}a_0$ (gray dashed)." → duplicated. Fix: delete "(gray dashed)".
- l.147 "the measured value is \SI{0.0771}{\angstrom}" → editor note: Flensburg–Stewart is a lattice-dynamical fit to neutron data (the caption already says so). Fix: "the lattice-dynamical fit to neutron data gives \SI{0.0771}{\angstrom}".
- l.50 two citations of `giustino2017electron` Sect. III A in one paragraph, the first for "every code prints it as its standard output" → citing a triviality. Fix: drop the first citation.
- Register calibration. (a) l.3 "During one swing of the nuclei the electrons have time to settle, many times over…" → Lin could have written it. (b) l.65 "A nucleus and an electron in the same crystal feel forces of the same size, since the Coulomb interaction does not care about mass." → yes. (c) l.79 "The derivative coupling is then of order … and the scalar coupling of order …" → no: a chain of "of order" (13 per 10k; L 0). Rewrite: "Counted the same way, the derivative coupling is $\sim\alpha^2m_e\kappa_{\mathrm{BO}}^3$ and the scalar one $\sim\alpha^2m_e\kappa_{\mathrm{BO}}^4$."

### 5.2
- l.3 opener: concrete first four sentences, then five roadmap sentences ("We will expand… Two symmetries… then fix… We close with… The construction is…") → REGISTER checklist 1 allows one "we will" sentence. Fix: keep one: "We will find these branches as the normal modes of the energy surface near its minimum, see how translations and rotations fix the acoustic branches at long wavelength, and end with the Debye model that the rest of the book uses for estimates." Move the Born–Huang/Ashcroft–Mermin attribution to the first citation point (l.35).
- l.3 "sharp peaks, near \SI{18}{meV}" vs l.136 "a sharp peak at \SI{17}{meV}" and l.187 "peak at \SI{17}{meV}" → inconsistent. Fix: 17 meV throughout (also Summary).
- l.65 "The model gets the shape right; the numbers, however, are off by up to \SI{20}{\percent}. The rest comes from…" → "The rest" has no referent. Fix: "…off by up to 20 %. The difference comes from forces between planes farther apart…".
- l.109 "The physical picture of the two terms is direct." → filler (pattern 17). Fix: delete; start "The first term is the stiffness…".
- l.119 "The bond-bending stiffness that sets them is the weakest force constant of the crystal, and the error of the functional shows there first." → editor note: state the TA softening as a known PBE trend, with a source. Fix: "…shows there first; PBE softens the transverse acoustic modes of silicon by a similar amount in other calculations~\cite[…]{…}".
- l.183 "$\omega_{\mathrm{D}} = \hbar\bar cQ_{\mathrm{D}}$ … $\Theta_{\mathrm{D}} = \omega_{\mathrm{D}}/k_{\mathrm{B}}$" → ħ and $k_{\mathrm B}$ in a book in natural units, after l.155 said the two "are the same number". Fix: "$\omega_{\mathrm D} = \bar cQ_{\mathrm D} = \SI{55.6}{meV}$ (13.4 THz), that is $\Theta_{\mathrm D} = \SI{645}{K}$."
- l.47 "In practice the force constants are computed, not fitted." → see chapter-level "In practice" item.
- Register calibration. (a) l.117 "Stretching a bond is stiff, while changing the angle between two bonds is soft, and a short-wavelength transverse wave mostly bends bonds." → Lin, yes. (b) l.45 "A quick estimate fixes the scale…" → yes (estimate first, check after). (c) l.96, the 250-word $T^{\alpha\beta\gamma}$ paragraph → no; it narrates index manipulations. Rewrite its first sentence: "Rotational invariance kills the first-order term; here is why." and move the index-cycling chain into a displayed equation.

### 5.3
- l.93 "The book writes that length as the \emph{zero-point length} of the mode," → self-reference to the book (standalone scrub). Fix: "We write that length as the zero-point length of the mode,".
- l.89 "This is \cref{eq:A.6-u}, the convention of the whole book," (also s5-2 l.35, s5-7 l.160) → three repetitions of a bookkeeping phrase. Fix: keep once (here) as "the convention used throughout"; in 5.2 and the Summary drop it.
- l.167 "the mass of the phonon calculation of \cref{fig:5-si}; \cref{we:5-kappa} used the mass of $^{28}$Si, which differs by \SI{0.4}{\percent}." → pattern 19 (which value was adopted and why). Fix: "We take the natural isotope mixture, $M_\kappa = 28.0855$ u = 26.16 GeV, and the Debye frequency…" and drop the comparison clause.
- l.100 "$M_{\mathrm{cell}}$ two silicon masses (\SI{52.3}{GeV}…)" → NOTATION and 1.5 have 52.33 GeV (editor item). Fix: 52.33 GeV.
- l.192 table caption: the Ge DFPT cells are "--" with only "A dash marks a value not given here." → leaves the reader asking why (editor item). Fix: add "Germanium has no DFPT entry because PBE at the measured lattice constant makes it a metal (\cref{app:E.1})." Split the caption after "…with the natural isotope masses." into two sentences; it is 230 words.
- l.182 "The Debye model at the same temperature, however, predicts … \SI{31}{\percent} low." then "The Debye model is low by \SI{18}{\percent} at zero temperature and by about a third at room temperature" → restates within the paragraph. Fix: drop the first sentence's percentage, keep the second.
- Register calibration. (a) l.133 "Each Cartesian component … behaves roughly like an oscillator… should roughly double" → Lin, yes (estimate before result). (b) l.162 "a spring stretched by thermal energy does not care what mass hangs on it" → yes. (c) l.37 "In these variables the Hamiltonian separates. In the kinetic term we write…" → borderline: narrates the algebra step by step. Acceptable as the main derivation of the chapter.

### 5.4
- l.3 opener: concrete (sixteen calculations, 432 atoms, $5\times10^4$), then six declaratives that preview the section ("The linear-response route is… Its central equation… The $2n+1$ theorem says… A Fourier transform…") → list as prose. Fix: one sentence: "We will derive both routes, the Sternheimer equation that makes the linear-response one cheap, and the Fourier interpolation that turns a few dynamical matrices into the whole dispersion."
- "gives" 17 times (46 per 10k; L 7), e.g. l.34 "gives $\Phi_{\mathrm{opt}}$ …", l.34 "gives $\Phi^{(3)}_{\mathrm{opt}}$", l.38 "gives", l.42 "gives … gives" → book tic (REGISTER Sect. 4). Fix: vary: "yields", "is", "we find", "comes out at"; e.g. l.42 "The central difference of the forces … leads to 13.63 eV Å⁻² and 63.71 meV; DFPT at the same settings finds 63.7 meV".
- l.55, 66, 90, 111 "which is Ref.~\cite[Eq.~(10)]{baroni2001phonons}" and variants (five times) → mechanical citation formula, unlike 5.1–5.3. Fix: attach the citation to the clause it credits: "…with the static response of the electrons~\cite[Eq.~(10)]{baroni2001phonons}."
- l.42 "the representative calculation of \cref{fig:5-si}" → "representative" is the editor's internal ruling word. Fix: "the calculation of \cref{fig:5-si}".
- l.42 "\SI{0.7}{\percent} higher" vs s5-2 l.119 "\SI{0.8}{\percent} low" for the same 63.7 vs measured → consistency (see Sect. 5).
- l.129 "The way out is the observation of the frozen-phonon subsection read backward." → vague internal pointer. Fix: "The way out is \cref{eq:5.4-alias} read backward."
- l.143 "The $3^3$ grid, with four inequivalent points, does not contain X, however, and puts the transverse acoustic mode there at …, but the test points are within …" → two contrasts in one sentence. Fix: "The $3^3$ grid, with four inequivalent points, misses X and puts the transverse acoustic mode there 14 % low, at 14.75 meV; at the test points, however, it is within 1.2 meV."
- l.143 "below the \SI{2.6}{\percent} mean difference between this functional and experiment (\cref{sec:5.2})" → 5.2 never states a 2.6 % mean. Fix: state it in 5.2 l.119, or write "below the 2 % agreement of this functional with experiment (\cref{sec:5.2})".
- l.81 "The picture is simple." → filler. Fix: delete.
- Register calibration. (a) l.47 "A second derivative needs less than it seems." → Lin, yes. (b) l.81 "electrons move away from where their potential energy rises" → yes. (c) l.27 "Long wavelengths need large cells: the cost of a complete set of force constants grows as the ninth power of their range" → yes. Target rewrite for the "gives" chain at l.34: "From the stretched bond we find 13.21 eV Å⁻², from the compressed one 14.04; the spread is the cubic term."

### 5.5
- l.7–40 and l.44–69 reproduce D.14 l.7–54 (energy 5.5-U, 5.5-FP, Maxwell relation, neutrality, longitudinal constraint, two-atom LO–TO) almost verbatim, while l.3 says "The general derivations … are in \cref{app:D.14}; here we carry them through for the two-atom cubic crystal" → but D.14 also does the two-atom crystal. Fix: 5.5 keeps the energy, the definitions, the physical paragraphs (l.27, l.36, l.40), eq. 5.5-na and 5.5-LOTO; D.14 keeps the general-tensor algebra, polaritons, Cochran–Cowley and Fröhlich, and drops its two-atom LO–TO subsection to a pointer to 5.5. Amend l.3 accordingly.
- l.38 the 8³→28³ narration of $\sum Z^*$ ("$-0.26$, … $-0.044$, $-0.011$ and $-0.003$") → a convergence log; the 8³ run is superseded (editor note); pattern 19. Fix: one sentence: "The sum rule is a cheap convergence test: on the $8^3$ grid of the phonons the two charges miss neutrality by 12 %, and only near a $28^3$ grid does the sum vanish, with $Z^* = 2.094$, within 1 % of the value 2.11 that the measured splitting implies."
- l.78 "PBE usually makes phonons slightly soft; here, however, the measured lattice constant compresses the crystal relative to the PBE minimum…" → two semicolons in one sentence. Fix: "…\SI{1.8}{\percent} above the measured \SI{33.62}{meV}. PBE usually makes phonons slightly soft, but here the measured lattice constant compresses the crystal relative to the PBE minimum at 5.746 Å."
- l.82 "That case is the subject of the last part of this section." → self-referential signpost. Fix: "…field that is uniform in space, the case of the coupling below."
- l.138 "\Cref{eq:5.5-HE} says three things. First, … Second, … Third," → count-teaser. Fix: start "In \cref{eq:5.5-HE} the acoustic modes do not couple." and keep the three as consecutive paragraphs' first sentences without the ordinals.
- l.27 "dividing up the static density, a division that has no unique answer" → fine. l.56 "the ratio stays finite as $Q \to 0$ without having a limit" → good.
- Register calibration. (a) l.3 "For dark matter this dipole is the point of the material." → Lin, yes. (b) l.44 "In a lattice wave nobody applies it: the displaced ions create it, and it acts back on them." → yes. (c) l.116, the bare multiplication of four numbers in a display → acceptable in a worked example (REGISTER Sect. 7 digits).

### 5.6
- l.31 "\Cref{sec:5.3} found that the Debye model underestimates $\langle u_x^2\rangle$ of silicon by \SI{18}{\percent}…" and WE l.104 "low by \SI{18}{\percent} and \SI{35}{\percent}" → third and fourth statement of the same Debye error (5.3 l.182 twice). Fix: l.31 keep one clause: "For numbers we use the computed spectrum, since the Debye model misses the flat transverse branches (\cref{we:5-u2})."
- l.59 "\cite[App.~N]{ashcroft1976solid}\cite[Chaps.~3 and~4]{lovesey1984theorynuclear}" → two \cite commands run together. Fix: "\cite[App.~N]{ashcroft1976solid}, \cite[Chaps.~3 and~4]{lovesey1984theorynuclear}" (or one \cites).
- l.73 "Its normalization is $2W_\kappa$ itself" right after "$P_1$ … normalized to one" → ambiguous "Its". Fix: "The prefactor is $2W_\kappa$, since at $t = 0$ the left side is $\vect q\cdot B_\kappa\cdot\vect q$."
- l.62 "Two cautions apply." → count-teaser. Fix: delete; the next sentence carries the first caution.
- l.109 "The dark-matter kick of the previous subsection" → it is two subsections back. Fix: "The momentum kick of \cref{eq:5.6-poisson}".
- l.174 "The harmonic crystal is the ingredient behind the Gaussian state and the Poisson weights, and \cref{sec:5.7} turns to what the anharmonic terms… do" → muddled seam. Fix: "Both rest on the harmonic crystal, whose thermal state is Gaussian; \cref{sec:5.7} asks what the anharmonic terms of the potential do to that picture and to the phonons themselves."
- Register calibration. (a) l.3 "What does the lattice do instead? Sometimes nothing: the nucleus takes up the momentum…" → Lin, yes. (b) l.86 "The mean energy deposited takes no calculation at all." → yes. (c) l.102 "Indeed, a single oscillator of frequency \SI{30.4}{meV} reproduces…" → yes (KL's "indeed").

### 5.7
- l.114 "The bookkeeping of \cref{sec:8.5} counts powers of the anharmonic expansion parameter … both of anharmonic order $n_A = 2$. The leading anharmonic phonon self-energy sits at that order." → aimed at cross-chapter consistency, and $n_A$ is used before its definition in 8.5 (pattern 19 + first-use). Fix: one clause: "…of one order, which \cref{sec:8.5} labels as anharmonic order two." Drop $n_A$ here.
- l.23 "A bond is stiffer under compression than under stretching, and a bond that is stretched is softer than at rest." → second clause restates the first. Fix: "A bond is stiffer under compression than under stretching: its force constant falls as it lengthens."
- l.129 "The zero-point energy of \cref{sec:5.3} also depends on the volume, and its pressure expands the lattice…" → third statement (5.1 l.54, 5.3 l.75). Fix: keep here (where it belongs, in the quasi-harmonic paragraph); cut to a pointer in 5.1 and 5.3.
- "of order" 7 times (17 per 10k; L 0), e.g. l.109, l.116 "coefficients of the counting are of order one" → book tic. Fix: "∼" or "are close to one".
- Register calibration. (a) l.3 "What kills them is the part of the energy surface that the harmonic approximation dropped" → Lin, yes. (b) l.93 "The Klemens law is a good parametrization … It does not predict that width" → yes. (c) l.135, the SCHA variation paragraph → G rather than L; acceptable for a derivation.

### Summary (s5-7 l.154–170)
- l.158 "flat transverse acoustic branches that pile up states near \SI{18}{meV}" → body says 17 meV. Fix: 17 meV.
- l.164 (5.5 paragraph) omits the practical result of 5.5 (editor asked to recheck): PBE $\varepsilon_\infty$ is 26 % high, so the splitting (or computed $Z^*$ with measured $\varepsilon_\infty$) is the input for $Z^{*2}/\varepsilon_\infty$. Fix: add one sentence.
- l.160 "is the convention of the whole book" → drop (see 5.3).
- l.166 (5.6) and the closing l.170 are good; the closing hands off to Chap. 6 on a consequence.

### App. D.13
- l.72 "The zero-point amplitude is the fraction $\kappa_{\mathrm{BO}}$ of a bond length" → loose, and inconsistent with the 0.021 of \cref{we:5-kappa}: the scaling is in units of $a_0$. Fix: "of the Bohr radius".
- l.3 "This appendix writes… It derives… It ends with…" → outline; acceptable for an appendix but trim to one sentence.
- Overlap with 5.1: see 5.1, first item.

### App. D.14
- l.41 "less than $10^{-4}$ of the zone, Dark-matter scattering transfers…" → comma splice with capital (editor item). Fix: "…of the zone. Dark-matter scattering…". This paragraph also duplicates s5-5 l.82; keep it in one place.
- l.80 "A numerical check with three polar modes, random masses, … reproduces \cref{eq:D.14-LSTgen} to machine precision." → pattern 19 (verification log aimed at a reviewer). Fix: delete.
- l.3 "derives these four results" → count without names. Fix: "derives the direction dependence, the splitting, the Lyddane–Sachs–Teller relation and the Fröhlich vertex from one energy function…".

### App. D.15
- l.1 title (lint) → two-item title. Fix: "Bloch's identity and the Debye–Waller factor" is still two; prefer "The Debye--Waller factor".
- l.62 "For a crystal of one species … with one atom per cell … normalized here to three modes per cell" → editor ruling: the DOS is per atom, normalized to three; 5.3 l.160 applies this result to silicon (two atoms per cell). Fix: "…in terms of the density of states per atom, $g_{\mathrm{ph}}/n_{\mathrm{at}}$, normalized to three (\cref{eq:5.3-u2})", and drop "one atom per cell".
- l.62–76 $\omega_D$ (italic D) vs $\omega_{\mathrm D}$ in 5.2/5.3; l.72 $E_{\mathrm{R}}$ vs $E_R$ in 5.6 and NOTATION (editor item). Fix: $\omega_{\mathrm D}$ and $E_R$ throughout.
- l.76 "the bracket … is $4.11$: the thermal motion already quadruples the zero-point exponent" → the thermal part is 3.11 times the zero-point part. Fix: "the exponent is four times its zero-point value".

### App. C.18
- l.3, 62, 76, 106 "km/s" vs "km.s^{-1}" in 5.2 and 5.4 → one unit form. Fix: \SI{…}{km.s^{-1}}.
- l.50 "which is the form in which \cref{app:E.12} writes it" and l.85 "one diagonalizes" → minor (consistency note; "one" construction). Fix: delete the clause; "we diagonalize".

## 4. Chapter as a whole
- **Opening.** Passes the user rule: question-led, no section list, one closing orientation sentence.
- **Section openers.** All seven start concretely (64.1 meV, neutron data, 0.05 Å, sixteen calculations, GaAs TO/LO, 50 keV, Raman width). Good. But five of them (5.2, 5.3, 5.4, 5.5, 5.7) end in two to six roadmap sentences ("We will… Then… We close with…"); 5.2 and 5.4 are the worst. Fix: one "we will" sentence each.
- **"In practice" template.** Opens a paragraph in s5-1 l.127, s5-2 l.47, s5-3 l.164, s5-5 l.38, s5-6 l.62, s5-7 l.25 (pattern 10). Fix: keep it in 5.3 and 5.7; elsewhere open on the content ("A code returns the energy and every force…", "DFPT computes the whole matrix…").
- **Voice.** Consistent across the seven writers: "we", short declaratives after derivations, verdict sentences in worked examples. "We will/can/see" is rare everywhere (2–9 per 10k against L ~28) and "typical" is absent from 5.1, 5.2, 5.5, 5.7 (L 15). Raise both where an estimate or a result is announced. "however" (2–6 per 10k) and "since" (9–28) are near the models'. Terms of art conform to REGISTER Sect. 2: "momentum transfer" always as the full noun ("transfers" occurs only as a verb), kinematically allowed, Born effective charge, harmonic and adiabatic (Born–Oppenheimer) approximation, frozen-phonon vs DFPT, dynamical matrix, Debye–Waller factor, zero-point motion, Fröhlich coupling, phonon-assisted. No coinages found. Appendix calibration: D.13 l.74 and D.15 l.25 read as Giustino rather than Lin (formal, cumulative clauses), and C.18 is G throughout; acceptable for derivation appendices.
- **Redundancy across sections.** (i) 5.1 ↔ D.13 and 5.5 ↔ D.14 near-verbatim derivations (above). (ii) The Debye error for $\langle u^2\rangle$: s5-3 l.182 (twice), s5-6 l.31, s5-6 WE l.104. (iii) The zero-point pressure: s5-1 l.54, s5-3 l.75, s5-7 l.129. (iv) The polariton paragraph: s5-5 l.82 and D-14 l.41. (v) 5.6 restates eqs. 5.3-B/D.15-B only by reference, which is fine.
- **Seams.** 5.1→5.2: pass (5.1 closes on "expanding it to second order… harmonic crystal of 5.2"). 5.2→5.3: pass ("What they are not yet is quantum"). 5.3→5.4: weak; 5.3 closes on single-phonon rates and 5.4 reaches back to \cref{fig:5-si} of 5.2. Fix: end 5.3 with one sentence that hands over ("All of this needs $\omega_{\vect Q\nu}$ and $\vect e_{\kappa\nu}$ on fine grids; \cref{sec:5.4} shows how density-functional theory supplies them."), or open 5.4 with the cost of that need. 5.4→5.5: pass (field in place of a displacement). 5.5→5.6: pass. 5.6→5.7: muddled closing sentence (fix above). 5.7→Summary: pass.
- **Citation style.** Bare \cite in 5.1–5.3 and 5.6–5.7; "which is Ref.~\cite[Eq.~(n)]{…}" five times in 5.4 and "as tabulated in Ref.~\cite[Table~…]{…}" in captions and WEs. The second is fine (credit for a tabulation). Make the first consistent with the rest (attach to the clause). No citation carries content: every formula used is stated in the book (pattern 20 clean).
- **Cross-references.** All \cref; no hard-coded numbers. Exceptions are prose pointers without labels: s5-4 l.129 "the frozen-phonon subsection", s5-5 l.82 "the last part of this section", s5-7 l.25 "the methods of the last part of this section" (acceptable).
- **Titles.** All short noun phrases; only D.15 is a two-item title.
- **Equation punctuation.** Correct throughout (lint hits are false positives).
- **First-use symbols.** Clean except $N_{\mathrm{at}}$ (s5-1 l.48) and $n_A$ (s5-7 l.114).
- **Captions.** Stand alone, with settings and units. Fix the duplicate in fig5-scales (b) and split the tab:5-phonons caption.
- **Lists.** None in the chapter. No prose bullets.

## 5. Consistency (not prose; does not count toward verdicts)
- Si DOS peak 17 vs 18 meV (s5-2 l.3, Summary l.158 vs s5-2 l.136, 187).
- PBE optical vs measured: "0.8 % low" (s5-2 l.119) vs "0.7 % higher" (s5-4 l.42) for 63.7 vs 64.1 meV (0.6 %); align.
- Cell mass 52.3 (s5-3 l.100) vs 52.33 GeV (NOTATION, 1.5).
- fig5-scales caption (s5-1 l.134): 50 Ry, $8^3$ k grid vs the 60 Ry ruling for the single representative calculation (editor item: rerun at 60 Ry).
- "2.6 % mean difference" (s5-4 l.143) has no source in 5.2.
- $\omega_D$/$E_{\mathrm R}$ (D.15) vs $\omega_{\mathrm D}$/$E_R$ (body).

## 6. Editor notes: prose items and status
- 5.1/5.3 Flensburg–Stewart "measured" → "lattice-dynamical fit": done in captions, 5.3 and 5.6; **open** at s5-1 l.147.
- 5.2 TA 8 % soft as a known PBE trend with a source: **open** (s5-2 l.119).
- 5.2/5.3 D.15 "three modes per cell" → per atom: **open** (D-15 l.62).
- 5.3 Ge DFPT column: no explanation in the table: **open** (caption sentence above).
- 5.3 cell mass 52.33: **open** (s5-3 l.100).
- 5.5 D.14 comma splice in the polariton paragraph: **open**, located at D-14 l.41.
- 5.5 8³ run superseded: text still narrates it (s5-5 l.38); compress as above.
- 5.6 $E_R$ vs $E_{\mathrm R}$ alignment with D.15: **open**. $E_{\mathrm{ZPL}}$ first use is in 5.6 (done). Bloch left uncited (done).
- 5.7 summary paragraphs for 5.5 and 5.6: 5.6 fine; 5.5 **open** (missing $\varepsilon_\infty$ conclusion).
- 5.4 SPINE figure list: not a prose item; fig5_3 is the interpolation figure as ruled.
