# Language audit, Part II (tex/ch09–ch17): reviewer ledger

Reviewer: read-only. Brief: briefs/reviews/language-audit.md. Date: 2026-11-07.

## Procedure and scope
- Lint: `skills/long-form-writing/scripts/lint.py --banned BANNED-TERMS.txt` on all 73 files of ch09–ch17. Result: 471 hits, 0 blocking. By type:
  - 406 LONG-SENT: mostly captions, tables and display-adjacent text, where the splitter counts math as words. The prose cases worth splitting are listed below (C11.3, C12.1).
  - 62 EQ-PUNCT: 57 are displays that end in ` ,` or ` .` before `\end{…}` or have an inner `\\`. Two need punctuation, and these are typographic, not equation content: ch10/s10-6.tex:115 (eq:10.6-oo, followed by "with …") needs a final comma, and ch13/s13-9.tex:8 (the display "$m_{\mathrm{min}}^{\mathrm{ZP}} = \SI{0.407}{MeV}$", followed by "with spin--orbit …") also needs a final comma. Both are OPTIONAL. ch13/s13-4.tex:111 continues the sentence ("… to $\tilde M^\pm$") and is correct as written.
  - 2 DASH: table code in s9-1:22 and s17-2:37, false positives.
  - 1 PERIPHRASIS: s11-4:99, item C11.8.
- Read in full: the 9 chapter openings, the 66 section openers, all 174 figure, table and Limit Check captions, the 100 key-result boxes (titles and prose), and the 9 Summary openers.
- Body: lint hits, plus a skim of the last paragraph of each of the 277 subsections (pattern 26), plus targeted reads for figurative verbs (pulls, lives, knows, feels, sees, finds, wins), negation stacks, "bookkeeping", "ladder", "upshot", "of course", "the price of", and self-narration ("this section", "we will").
- Not flagged on purpose: (a) the "We will derive …" roadmap sentences at the end of section openers. REGISTER.md §1 asks for the models' "we will" and "we turn to", so these stay unless they carry no content. (b) The book-wide devices of Ch. 8 ("many-body axis", "truncation label", "home section", "atlas"), which are defined terms, not private metaphors used in place of a field term. (c) Caption house formulas ("Gray: … within 10 %", "Nothing is shaded").
- Overall: the prose is dense and mostly plain. The remaining problems cluster in four places. Section openers still narrate in places ("This section shows …", "In this section we …"). Some figurative verbs remain ("pull", "knows", "lives"). A few closing paragraphs only recap (pattern 26). Two chapter openings contain long sentences with dangling modifiers (ch11, ch12).

Format: `file:line → "quoted sentence" → plain rewrite` [MUST/OPTIONAL; pattern]. Line numbers are physical lines of the .tex file. Each paragraph is one physical line, so the quote locates the sentence within it.

---

## Ch. 9, Channel atlas

C9.1 ch09/ch09.tex:2 → "\Cref{chap:8} built the machinery for all of them: every coupling reduces to …" → "\Cref{chap:8} gave the rate for all of them: every coupling reduces to …" [OPTIONAL; p24/p0, "machinery" is a gesture]

C9.2 ch09/ch09.tex:2 → "At that size the hazard is bookkeeping. The literature computes many channels with formulas of its own, and a process can enter two of them: …" → "At that size the hazard is double counting. The literature computes many channels with formulas of its own, and a process can enter two of them: …" [OPTIONAL; p0, name the hazard]

C9.3 ch09/s9-4.tex:3 → "We will say how such a box is built, show that its horizontal axis follows from …" → "We build such a box, show that its horizontal axis follows from …" [OPTIONAL; p22, "say how" adds nothing]

## Ch. 10, Electronic excitations

C10.1 ch10/s10-1.tex:3 → "Along the way we will be precise about what such a calculation contains and what it leaves out, since the rest of this chapter adds the missing pieces one at a time." → "The rest of the chapter adds, one at a time, what such a calculation leaves out." [MUST; p0/p22, self-narration with no payload]

C10.2 ch10/s10-1.tex:100 → "Screening is the largest at small momentum transfer, and the box above already shows where it sets in; we turn to it next." → "Screening, the largest of them at small momentum transfer, comes next." [OPTIONAL; p26, the box already shows the onset]

C10.3 ch10/s10-2.tex:3 → "Two sum rules of the loss function then bound it from above, with nothing but the plasma frequency and the static dielectric function as input." → "… with only the plasma frequency and the static dielectric function as input." [MUST; p25, negation stack "nothing but"]

C10.4 ch10/s10-2.tex:47 → "A pointwise factor leaves out where the rate lives in $q$, the $f$-sum rule, and the local fields, …" → "A pointwise factor leaves out where in $q$ the rate comes from, the $f$-sum rule, and the local fields, …" [OPTIONAL; p15/p24]

C10.5 ch10/s10-2.tex:95 → "… the electrons it pulls drag their nuclei along, and the crystal answers as an elastic medium." → "… the electrons it displaces drag their nuclei along, and the crystal responds as an elastic medium." [OPTIONAL; p25 "pull", p15 "answers"]

C10.6 ch10/s10-2.tex:125 → "The sum rules cap the rate of any material by a few numbers, but are loose for silicon at MeV masses, and the cap on the inverse moment does not hold for an electrophilic mediator in the phonon band." → delete. The section opener and s10-2:90 state all three facts, so the paragraph keeps only "\Cref{sec:10.3} takes the loss function of the electron gas, …". If the sentence is kept, write "a mediator that couples to electrons alone" for "electrophilic mediator", the term used in the opener. [MUST; p26, looped restatement]

C10.7 ch10/s10-3.tex:3 → "A model with one parameter, the electron density, lands within seven percent of the crystal." → "A model with one parameter, the electron density, comes within seven percent of the crystal rate." [OPTIONAL; colloquial precision]

C10.8 ch10/s10-3.tex:130 → "The electron gas thus gives the rate of a density coupling to within a factor 1.5 in the energy band … Its plasmon, the feature that dominates the loss function at small momentum transfer, lies outside the reach of halo dark matter." → delete both sentences; keep "\Cref{sec:10.4} turns from the number of the electrons to their spin and their current." The factor-1.5 band is in the caption of fig:10-gas-limit, the failures are in s10-3:48, and the out-of-reach plasmon is in the opener and the worked example. [MUST; p26]

C10.9 ch10/s10-4.tex:3 → "… screen them row by row, and find that a single ratio controls how much the interference term can matter." → "… screen them row by row, and find that the ratio $r$ of the current-row rate to the density-row rate bounds the interference term." [OPTIONAL; p18, count-teaser that leaves the ratio unnamed]

C10.10 ch10/s10-5.tex:3 → "The attraction does more than add a line below the threshold. It pulls the electron toward the hole in every pair it touches." → "Besides adding a line below the threshold, the attraction raises the probability of finding the electron at the hole in every pair of the continuum." [MUST; p6 false contrast "does more than", p25 "pulls … touches"]

C10.11 ch10/s10-5.tex:3 → "… the change is largest in the first eV above the gap, where light dark matter collects its rate." → "… where most of the rate of light dark matter lies." [OPTIONAL; p24]

C10.12 ch10/s10-5.tex:3 → "… and how much a common shortcut in solving the equation costs." → "… and how much a resonant-only solution of the equation costs." [MUST; p18/p0, names the shortcut treated at s10-5:70–105]

C10.13 ch10/s10-5.tex:50 → "The next subsection explains the weakness: on the valley axis the vertex at the extrema vanishes, and the $1s$ line is dark." → "The line is weak because on the valley axis the vertex at the extrema vanishes, and the $1s$ line is dark." [OPTIONAL; p22]

C10.14 ch10/s10-6.tex:43 → "… the non-orthogonality of plane-wave final states and the missing Coulomb pull of the ion." → "… the missing Coulomb attraction of the ion." [MUST; p25, STYLE "Plain words"]

C10.15 ch10/s10-7.tex:147 → "The kinetic row is where absorption stops being a property of light. The dark photon and the axion-like particle read the optical constants of the target, …" → "The kinetic row has no optical counterpart." Keep the sentences that follow only where they add to the section opener: the core-weighted scalar response and the forward pointer. [OPTIONAL; p26, aphoristic opener]

C10.16 ch10/s10-8.tex:3 → "The exact tree-level rate then tells us how far the non-relativistic form can be trusted, and it corrects a published rate for axion-like particles." → "The exact tree-level rate then gives the range of validity of the non-relativistic form, and it corrects a published rate for axion-like particles." [OPTIONAL; p25 "tells us"]

C10.17 ch10/s10-9.tex:3 → "An excited state can also decay inside the detector without hitting anything, and we end with the interface between that decay and the framework." → "An excited state can also decay inside the detector without scattering, and we end with the rate of that decay inside the crystal." [OPTIONAL; p0, "the interface … and the framework" names nothing]

C10.18 ch10/s10-10.tex:15 → "The many-body ladder holds one more trap, an evaluation error rather than a truncation." → "The Bethe--Salpeter step carries one more pitfall, an evaluation error rather than a truncation." [MUST; p24, "ladder" used for the sequence of approximations rather than the BSE diagrams]

C10.19 ch10/s10-10.tex:89 → "And it is wider than the step between the two best computed approximations, … which a reader might be tempted to quote as the uncertainty. That step has been taken; what remains is the one after it, and the spread between calculations in the same approximation." → "It is also wider than the step between the two best computed approximations, $2.49\times10^4$ to $1.85\times10^4$. That step is not an uncertainty, since it has been taken; the band covers the next step and the spread between calculations in the same approximation." [OPTIONAL; p19, reviewer-directed aside]

## Ch. 11, Lattice excitations

C11.1 ch11/ch11.tex:2 → "Below about \SI{10}{MeV}, where the free recoil energy reaches the phonon energies, a dark-matter particle that couples to nucleons cannot give a silicon nucleus enough energy to treat it as free." → "Below about \SI{10}{MeV} the largest free recoil energy that a nucleon-coupled dark-matter particle gives a silicon nucleus falls to the phonon energies, and the nucleus can no longer be treated as free." [MUST; p17, a dangling infinitive ("enough energy to treat it") that needs a second reading]

C11.2 ch11/ch11.tex:2 → "… into a few phonons in between, and into a recoil broadened by the motion of the nucleus in its well only above." → "… into a few phonons in between, and, only at the top of the range, into a recoil broadened by the motion of the nucleus in its well." [OPTIONAL; p17, dangling "only above"]

C11.3 ch11/ch11.tex:4 → "Starting from the harmonic crystal of \cref{chap:5} and the master formula of \cref{chap:8}, each regime of \cref{fig:11-map} reduces to a few material numbers, sound speeds, Born effective charges and Debye--Waller exponents, each checked against the fuller result; throughout, the electrons stay in their ground state and follow the nuclei, and the Migdal effect and phonon-assisted electron recoil that start from this sector follow in \cref{chap:12,chap:13}." → "From the harmonic crystal of \cref{chap:5} and the master formula of \cref{chap:8}, each regime of \cref{fig:11-map} reduces to a few material numbers: sound speeds, Born effective charges and Debye--Waller exponents, each checked against the fuller result. Throughout, the electrons stay in their ground state and follow the nuclei. The Migdal effect and phonon-assisted electron recoil, which start from this sector, follow in \cref{chap:12,chap:13}." [MUST; p17, a 70-word sentence with a dangling participle and stacked appositives]

C11.4 ch11/s11-1.tex:30 → "The branch weights, the conservation of crystal momentum and the Debye--Waller factor carry the physics of \cref{eq:11.1-S1}." → "Three factors of \cref{eq:11.1-S1} set the response: the branch weights, the conservation of crystal momentum and the Debye--Waller factor." [OPTIONAL; p0, "carry the physics" is a gesture]

C11.5 ch11/s11-1.tex:205 → "The one-phonon rate of a nucleon coupling is thus fixed by the long-wavelength acoustic branches, through an elastic tensor that is measured for every crystal of interest, up to masses of about \SI{0.4}{MeV} and down to an edge of a few keV." → delete; the opener and s11-1:148 state this. Start the paragraph at "A coupling to charge, the dark photon, …". [OPTIONAL; p26]

C11.6 ch11/s11-2.tex:3 → "… and at long wavelength a coupling to charge finds nothing there; in the optical branch of GaAs it finds a vertex $Z^*/\varepsilon_\infty = 0.19$ per cell …" → "… and at long wavelength a coupling to charge has no vertex there; in the optical branch of GaAs its vertex is $Z^*/\varepsilon_\infty = 0.19$ per cell …" [OPTIONAL; p15]

C11.7 ch11/s11-2.tex:69 → "… each line weighted by a kinematic factor that knows only its energy and the dark-matter mass." → "… each line weighted by a kinematic factor that depends only on its energy and the dark-matter mass." [MUST; p15, anthropomorphic]

C11.8 ch11/s11-4.tex:99 → "For nucleons in place of electrons nothing changes except the response." → "For nucleons in place of electrons only the response changes." [MUST; p25, lint PERIPHRASIS hit]

C11.9 ch11/s11-4.tex:95 → "It does not ask what the nucleus does afterward, and it leaves out anharmonicity, electronic excitation and the displacement of the atom." → "It ignores the motion of the nucleus after the kick, and it leaves out anharmonicity, electronic excitation and the displacement of the atom." [OPTIONAL; p15]

C11.10 ch11/s11-5.tex:3 → "… and the harmonic lattice does not even have real frequencies." → "… and some harmonic frequencies are imaginary." [OPTIONAL; p25, negation]

C11.11 ch11/s11-5.tex:145 → "For a crystal like silicon, then, anharmonicity changes the impulse width by a part in a thousand and the few-phonon weights … For quantum crystals it changes the phonons themselves, and for the strongest cases only moments remain." → delete both sentences, since the section opener (s11-5:3) states each fact. Keep "The nuclei carry one more property …, which \cref{sec:11.6} takes up." [MUST; p26]

C11.12 ch11/s11-6.tex:85 → "A heavy atom thus pulls weight down from the top of each band." → "A heavy atom thus shifts weight down from the top of each band." [OPTIONAL; p25]

C11.13 ch11/s11-7.tex:3 → "A liquid would not notice. A crystal responds differently to momentum transfers along different crystal axes, so its rate follows the sidereal day." → "An isotropic target such as a liquid has the same rate in every orientation; a crystal responds differently along different crystal axes, so its rate follows the sidereal day." [OPTIONAL; p15 "would not notice", and the paragraph states the crystal-direction point twice]

C11.14 ch11/s11-7.tex:75 → "The anisotropy of the cubic nuclear response lives in the coherent terms, …" → "The anisotropy of the cubic nuclear response is entirely in the coherent terms, …" [OPTIONAL; p24]

C11.15 ch11/s11-8.tex:215 → "The scalar of \cref{sec:11.8-gaas} thus meets a crystal in two ways. …" → cut to the sentences that add the classical regime between the two limits; the meV and peV statements repeat s11-8:3 and the subsections. [OPTIONAL; p26]

## Ch. 12, The Migdal effect

C12.1 ch12/ch12.tex:2 → "In the decomposition of \cref{sec:8.6} it is the first mixed sector, the nuclear density reaching the electrons; \cref{chap:13} treats the second and \cref{sec:17.4} their interference, and we derive every form of the effect from one response that resolves the energy given to the lattice and to the electrons, of which the published formulas are truncations (\cref{fig:12-map})." → "In the decomposition of \cref{sec:8.6} it is the first mixed sector, the nuclear density reaching the electrons; \cref{chap:13} treats the second and \cref{sec:17.4} their interference. We derive every form of the effect from one response that resolves the energy given to the lattice and to the electrons; the published formulas are its truncations (\cref{fig:12-map})." [MUST; p17, chained clauses that end on a dangling "of which"]

C12.2 ch12/s12-1.tex:5 → "The same object then tells us how to add Migdal and lattice rates without counting a kick twice, …" → "The same object then fixes how Migdal and lattice rates are added without counting a kick twice, …" [OPTIONAL; p25 "tells us"]

C12.3 ch12/s12-1.tex:71 → "… and the Migdal effect pays off where the recoil itself is invisible: it trades the factor …" → "… and the Migdal effect matters where the recoil itself is invisible: it trades the factor …" [OPTIONAL; colloquial]

C12.4 ch12/s12-1.tex:97 → "The joint response separates what the total hides: two forms of the leading entry …" → "The joint response resolves what the total sums over: two forms of the leading entry …" [OPTIONAL; p15]

C12.5 ch12/s12-1.tex:133; s12-5.tex:87; s12-6.tex:174 (table cell); s12-6.tex:192 → "The bookkeeping, however, is exact" / "The probability, small per event, sets the bookkeeping." / "normali\-zation of the bookkeeping" / "The bookkeeping depends on the on-site drag mass" → name the object once and use it: "the counting of Migdal and lattice events" (prose). For the table cell, use "normalization of the added lattice rate", or whatever s12-1:133 shows the drag mass to normalize. [OPTIONAL in prose; the table cell is the least clear; p24/p0, "bookkeeping" stands in for a defined operation]

C12.6 ch12/s12-2.tex:145 → "The upshot for a crystal is that its core shells inherit the atomic probability, …" → "In a crystal the core shells inherit the atomic probability, …" [OPTIONAL; REGISTER, "upshot" as filler]

## Ch. 13, Phonon-assisted electron recoil

C13.1 ch13/ch13.tex:2 → "Light does the same between the indirect and the direct gap, and the measured absorption edge of silicon measures that process (\cref{sec:6.5})." → "… and the absorption edge of silicon is a measurement of that process (\cref{sec:6.5})." [OPTIONAL; "measured … measures"]

C13.2 ch13/ch13.tex:2, ch15/ch15.tex:4, ch16/ch16.tex:2, ch17/ch17.tex:4 → "\Cref{fig:13-map} shows how the pieces connect." / "… shows how the sections connect." / "… shows how the targets connect to the bulk responses." / "… shows how the comparisons connect." → keep one pointer, but fold it into the preceding sentence as a parenthesis "(\cref{fig:13-map})", as ch10 and ch12 do. [OPTIONAL; p0, formulaic closing sentence]

C13.3 ch13/s13-1.tex:3 → "We will make this precise: derive the lightest mass …, evaluate both in silicon and germanium, and see what happens in a direct-gap crystal." → "… evaluate both in silicon and germanium, and show that a direct-gap crystal such as GaAs has a window as well." [OPTIONAL; p0, "see what happens"]

C13.4 ch13/s13-1.tex:19 → "The second form is one minimization over six continuous variables, three for $\vect{q}$ and three for $\vect{k}$, and it says something the first form hides. Fixing the hole at the valence-band maximum, or restricting $\vect{q}$ to a few directions, can only raise the result." → "The second form is one minimization over six continuous variables, three for $\vect{q}$ and three for $\vect{k}$, and it shows that fixing the hole at the valence-band maximum, or restricting $\vect{q}$ to a few directions, can only raise the result." [OPTIONAL; p0/p8, teaser]

C13.5 ch13/s13-2.tex:3 → "Kahn and Lin name this process among the excitations of an indirect-gap crystal near its gap~\cite[Sect.~VI]{kahn2022searches}." → keep the credit in a clause, e.g. append to the previous sentence: "…, a process listed by Kahn and Lin~\cite[Sect.~VI]{kahn2022searches}." [OPTIONAL; p19, provenance sentence; citation unchanged]

C13.6 ch13/s13-4.tex:3 → "We now write the amplitude with all three, show that the loss function keeps …" → "With all three in the amplitude, the loss function keeps one macroscopic factor … and nothing else outside it; we size each piece in silicon, and \cref{app:D.36} gives the steps at the random-phase level." [OPTIONAL; p22, "we now"]

C13.7 ch13/s13-5.tex:3 → "In this section we take its limit $\vect{q}\to0$ and show that it is the phonon-assisted absorption $\varepsilon_2^{\mathrm{PA}}(\omega)$ of \cref{eq:6.5-eps2PA}." → "Its limit $\vect{q}\to0$ is the phonon-assisted absorption $\varepsilon_2^{\mathrm{PA}}(\omega)$ of \cref{eq:6.5-eps2PA}." [MUST; p22]

C13.8 ch13/s13-6.tex:3 → "This section shows that the soft acoustic phonon is harmless: translation invariance fixes its amplitude, and inside the window it never occurs on the energy shell." → "The soft acoustic phonon produces no divergence: translation invariance fixes its amplitude, and inside the window it is never on the energy shell." [MUST; p22 self-narration, p0 "harmless"]

C13.9 ch13/s13-6.tex:27 → "… nearly cancel, since an electron that hardly feels the ions hardly feels them move." → "… nearly cancel, since a weak electron--ion potential gives a weak electron--phonon vertex." [OPTIONAL; aphorism; physics unchanged]

C13.10 ch13/s13-8.tex:3 → "This section rebuilds the amplitude of \cref{sec:13.2} from exciton states, states when …, reduces it …, and works out …" → "We rebuild the amplitude of \cref{sec:13.2} from exciton states, state when …, reduce it …, and work out …" [OPTIONAL; p22]

C13.11 ch13/s13-9.tex:3 → "Where the phonon-assisted rate stops leading, how large it is, and what happens in germanium and GaAs are known only as estimates or not at all, and we state them as such. The chapter's nuisance table and its open problems close the section." → "Where the phonon-assisted rate stops leading, how large it is, and the windows of germanium and GaAs are known only as estimates or not at all." Delete the second sentence. [MUST; p19 "we state them as such", p22 narration]

## Ch. 14, Magnetic excitations

C14.1 ch14/s14-4.tex:3 → "The catch is that a neutron sees only the part of the spin density perpendicular to the momentum transfer, and how much of the dark-matter response that part fixes depends on the coupling and on how much of a model of the magnet we are willing to add." → "A neutron, however, couples only to the part of the spin density perpendicular to the momentum transfer, and how much of the dark-matter response that part fixes depends on the coupling and on how much model input is added for the magnet." [OPTIONAL; colloquial idiom, p15 "sees"]

C14.2 ch14/s14-5.tex:3 → "… unless inversion and time reversal are both broken, and magnetic order is what breaks time reversal, which brings such crystals into a chapter on magnets." → "… unless inversion and time reversal are both broken; in a crystal, magnetic order breaks time reversal." [OPTIONAL; p19, a sentence about the book's structure]

## Ch. 15, Superconductors

C15.1 ch15/s15-2.tex:32 → "Two things pull the loss function below $\mathfrak{g}_{\mathrm{I}}L^{\mathrm{nor}}$." → "The gap and the case-I factor both lower the loss function below $\mathfrak{g}_{\mathrm{I}}L^{\mathrm{nor}}$." [OPTIONAL; p18 count-teaser, p25 "pull"]

C15.2 ch15/s15-3.tex:93 → "Of course, a causal response is not enough. Every calculation of the superconducting $\varepsilon$, … has to avoid three traps." → "A causal response alone is not enough: every calculation of the superconducting $\varepsilon$, … must avoid three errors." [OPTIONAL; "of course", "traps"]

## Ch. 16, Novel targets

C16.1 ch16/s16-1.tex:57 (two), :64 (two), :69 (caption); ch16/s16-summary.tex:3 → "with the book's halo" / "for the book's halo" → "with the standard halo" [OPTIONAL; p0, name the halo; no cref added]

C16.2 ch16/s16-5.tex:3 → "Its weakness is the number of electrons, five parts in $10^9$ of the valence electrons at …" → "The drawback is the number of donor electrons, five parts in $10^9$ of the valence electrons at …" [OPTIONAL; unanchored "Its"]

C16.3 ch16/s16-5.tex:62 → "… which the central cell pulls in to \SI{45.59}{meV}." → "… which the central-cell potential deepens to \SI{45.59}{meV}." [OPTIONAL; p25]

## Ch. 17, Comparison across channels

C17.1 ch17/ch17.tex:2 → "These two numbers happen to sit in one section, but most of the comparisons an experimentalist needs are spread over seven chapters." → "Both numbers come from one section; most comparisons an experimentalist needs are spread over seven chapters." [OPTIONAL; p19/p0, "happen to sit"]

C17.2 ch17/s17-1.tex:3 → "A target and a threshold are chosen against where such changes happen, coupling by coupling." → "For each coupling, where these changes fall in mass and threshold decides the choice of target and threshold." [MUST; p17, unclear construction "chosen against where"]

C17.3 ch17/s17-3.tex:3 → "Back in scattering, a dark-matter particle of \SI{10}{keV} at the largest laboratory speed …" → "A dark-matter particle of \SI{10}{keV} at the largest laboratory speed …" [OPTIONAL; p0, the transition sentence-opener carries no content]

C17.4 ch17/s17-3.tex:60 → "Since the plasmon exists only below the Landau-damping momentum, the line lives in a window of splittings." → "… the line exists only in a window of splittings." [OPTIONAL; p24]

C17.5 ch17/s17-3.tex:92 → "Of course the two are different models, an undamped pole in a gas against a broad loss peak in a crystal; the upshot is that the plasmon is a minority share of exothermic electron recoil even where …" → "The two are different models, an undamped pole in a gas against a broad loss peak in a crystal; in both, the plasmon is a minority share of exothermic electron recoil even where …" [OPTIONAL; "of course", "upshot"]

## Book-wide crutch in Part II (one item)

C-X.1 "the price of / is the price / at the price of" at ch10/s10-7.tex:61, s10-8.tex:58, s10-9.tex:96; ch11/s11-6.tex:48; ch13/s13-1.tex:27, :32, s13-2.tex:130, s13-6.tex:77; ch14/s14-4.tex:94; ch16/s16-2.tex:14, s16-8.tex:44, s16-summary.tex:5; ch17/s17-6.tex:124 → 13 uses. Keep at most a few. Elsewhere say what the cost is, e.g. s10-8:58 "The factor … = 1.8e-6 is the price of the derivative coupling." → "The derivative coupling brings the factor … = 1.8e-6." [OPTIONAL; REGISTER crutch frequency]

---

## Physics doubts (for the editor; not changed, not language items)

D1. Top of the silicon phonon band / optical phonon: 64.1 meV in ch09/ch09.tex:2 ("an optical phonon of \SI{64.1}{meV}"), the caption at ch10/s10-2.tex:30 ("$\omega_{\max} = \SI{64.1}{meV}$ the top of the phonon band") and the caption at ch17/s17-3.tex:114 ("the optical phonon of silicon at \SI{64.1}{meV} (\cref{sec:5.2})"). But 63.7 meV in the captions at ch11/s11-6.tex:175 ("top of the band, \SI{63.7}{meV}"), ch12/s12-4.tex:131 ("band top \SI{63.7}{meV}") and ch17/s17-1.tex:20 ("capped at the band top, \SI{63.7}{meV}"), and in ch17/s17-summary.tex:3. ch13/s13-1.tex:27 has "no phonon of silicon has more than \SI{64}{meV}". This is probably measured against PBE, but s10-2:30 calls 64.1 meV "the top of the phonon band" while s11-6 and s17-1 call 63.7 meV the band top. Check which value each use intends and whether the source should be stated.

D2. ch14/s14-1.tex:3: "A dark-matter particle of \SI{1}{MeV} that couples to the spin of the electron carries up to \SI{5.3}{keV} of momentum". 5.3 keV is $2m_\chi v_{\max}$, the largest momentum transfer; the particle itself carries at most $m_\chi v_{\max} = 2.65$ keV. Probably "can transfer up to", but the word sets the physics, so it is left to the editor.

D3. Acoustic edge of silicon at 1 meV: 6.1 keV (fastest longitudinal speed) in ch09/s9-2.tex:3 and the ch11 Summary (ch11/s11-9.tex:98), against 6.39 keV "for the rate-weighted speed" at ch11/s11-1.tex:136 and in the caption at s11-1.tex:129 ("silicon, all branches and directions … $m_{\mathrm{min}}^{\mathrm{ac}} = \SI{6.39}{keV}$"). Both can be right under different definitions (6.39 keV corresponds to $c \approx 9.0$ km/s, 6.1 keV to 9.35 km/s). The caption, however, attaches 6.39 keV to "all branches and directions", where the edge is set by the fastest direction. Confirm which definition the caption means.

No other numerical doubt was found in the targets read. The recomputed checks that passed include: $E_R^{\max}$ at 46.8 and 100 MeV, dark Compton 91.8/8.2 keV, the 241.8 kHz at 1 neV, the 12 cm and 148 m wavelengths at 10 µeV, $v_{\max}/v_F = 0.392$, the floor 0.3332 MeV, and the 2.39 and 1.22 sound-speed ratios in s17-6.

---

## Counts
- MUST: 18 (C10.1, C10.3, C10.6, C10.8, C10.10, C10.12, C10.14, C10.18, C11.1, C11.3, C11.7, C11.8, C11.11, C12.1, C13.7, C13.8, C13.11, C17.2). Of these, three are pattern-26 deletions (C10.6, C10.8, C11.11) and five are self-narrating or unclear section-opener sentences.
- OPTIONAL: 49 items (some cover several locations: C12.5 four, C13.2 four, C16.1 six, C-X.1 thirteen), plus 2 display commas (lint section).
- Physics doubts: 3 (D1–D3).
- Lint: 471 hits, 0 blocking (406 LONG-SENT, 62 EQ-PUNCT, 2 DASH, 1 PERIPHRASIS).
