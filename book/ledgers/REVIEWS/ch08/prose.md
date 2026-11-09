# Ch8 prose review (style, register, standalone scrub)

Scope: tex/ch08/ch08.tex, s8-1 … s8-8; tex/appD/D-24 … D-28. Checked against STYLE.md, style-guide.md, prose-review.md, REGISTER.md and editor-notes.md. No tex edited.

## Verdicts

| Unit | Verdict | Non-minor reason (minor items listed below) |
|---|---|---|
| Chapter opening (ch08.tex) | REVISE | 2nd paragraph is a section-by-section list in prose |
| 8.1 Couplings | REVISE | orphan Coulomb-energy row; ²⁹Si abundance missing; outline opener |
| 8.2 Master rate formula | REVISE | required O₇ sentence missing; 𝔗, n_T used before 8.5 defines them |
| 8.3 Exact relations | REVISE | n_B used undefined (l.50); "of order" at 26/10k |
| 8.4 Screening | REVISE | ε_e means two things in one chapter (8.4 l.48 vs 8.7 l.12); Π_em and "improper response" undefined at first use |
| 8.5 Expansion hierarchy | PASS | minor only |
| 8.6 Decomposition theorem | REVISE | about 5,900 words of prose (editor budget note: 6,050); "This section…" frame; α̃ unglossed; one 60-word sentence |
| 8.7 Final-state response | REVISE | ε_e clash; "a volt" used for an energy; recap opener |
| 8.8 Uncertainty structure + Summary | PASS | minor only (closing overclaim, % style) |
| App. D.24–D.28 | PASS | minor only |

The voice is consistent across the eight sections. Every section opens on a concrete number, picture or question. Lists appear only for real enumerations: the Coulomb-line classes, the label components and the sector tables. No section needs a REWRITE.

## 1. Lint (lint.py --banned BANNED-TERMS.txt)

No blocking hits and no banned-term hits in any file. Every EQ-PUNCT hit is a false positive: the punctuation sits inside `gathered`/`aligned`, or the sentence continues after the display. Checked: s8-1:28, s8-2:42, s8-3:71, s8-4:18, s8-6:109/151, s8-7:18, D-24:24, D-25:61/87, D-26:89. Most LONG-SENT hits are keyresult, table or caption text merged by the parser.
- ch08.tex 0 · s8-1 3 (1 EQ, 2 LONG) · s8-2 3 (1/2) · s8-3 6 (1/5) · s8-4 2 (1/1) · s8-5 2 (0/2) · s8-6 9 (2/7) · s8-7 2 (1/1) · s8-8 2 (0/2)
- D-24 1 (1/0) · D-25 6 (2/4) · D-26 3 (1/2) · D-27 2 (0/2) · D-28 6 (0/6)
- Genuine overlong sentences (more than 48 words with math collapsed): s8-6 l.197 (Dirac, 60 words, three clauses joined by semicolons); s8-3 l.78 ("For q ≳ 1/a_core …", 51); s8-2 l.83 ("The worked example takes …", the last sentence of the paragraph, 69 counted through the WE head); s8-7 l.74 ("A code that returns … (\cref{sec:21.6})", ~45, two sentences joined by a semicolon). Split each one.

## 2. Chapter-level checks

**Opening (ch08.tex).** Paragraph 1 is good. It is motivational, it is concrete (NiO, Al, Si, a magnetic moment, an absorbed fermion), and it ends on the question. Paragraph 2 breaks STYLE ("at most one closing sentence orients the reader; never a section-by-section list"). After "The answer is short.", a colon-reveal (pattern 8), its six sentences track 8.1→8.6 in order: "Every slow coupling reaches the target through a handful of operators per species …" (8.1), "Scattering, absorption and … are three regions of one rate formula" (8.2), "A few relations … hold for every target" (8.3), "Screening has to be counted once" (8.4), "Every model … is a truncation of one expansion …" (8.5–8.6).
- Fix: drop "The answer is short." Keep one sentence of answer: the model collapses into a tensor and the target into one response matrix, so a new model or target means a new tensor or a new matrix, not a new calculation. Then one "we will" sentence that ends at the hand-off to Chap. 18.
- "three regions of one rate formula" contradicts 8.2's own wording: a region, a line and a point (s8-1 l.205, Fig. 8.1). Use "three places in the (q, ω) plane".
- "Every slow coupling": a coupling is not slow. Write "Every coupling of a slow particle".

**Summary (s8-8 l.129–145).** It is a `\section*` as in Chaps. 1–7, it has one paragraph per section, and it ends on the pointer to Chap. 9. Acceptable.
- l.137 "a theorem fixes when an electron coupling does" is vague. Write "an electron-density coupling does so only at a static lattice".
- l.139 gives silicon values for four of the seven parameters and none for the other three. Either give all seven or name none.
- l.145 "In silicon the step from the random-phase approximation to local fields is such a tilt" adds no number. Give one: "−0.44 to +0.25".

**Redundancy across sections.**
- The pointer to 8.4 is written four times in near-identical words: s8-1 l.109 "Which rows are screened, and how, is the subject of \cref{sec:8.4}"; s8-2 l.57 "Which rows are screened in this way, for every coupling, is the question of \cref{sec:8.4}"; s8-2 l.116 "\cref{sec:8.4} decides which rows of the contraction are screened"; s8-3 l.205 "Which rows … the medium screens … is the question of \cref{sec:8.4}". Keep the one in s8-3 (the seam) and cut the other three to a bare \cref.
- The dark-photon absorption reduction appears twice: s8-1 l.165 ("its response is the optical conductivity … which is why \cref{eq:1.4-dp-abs} needs nothing else") and s8-2 l.57 (the full reduction). Cut the s8-1 clause to "(\cref{sec:8.2-absorption} reduces it to the conductivity)".
- Fermionic absorption gets the same sentence three times: s8-1 l.186 "its spinors enter a tensor … which \cref{sec:10.9} constructs", s8-1 l.205 and s8-2 l.59 "Only $\mathfrak{D}_{ab}$ changes: the spinors … which \cref{sec:10.9} constructs". Keep it in s8-2 only.
- The interference bound is stated as a result in s8-2 l.116 ("limits its size to twice the geometric mean") one page before 8.3 proves it. Rephrase it as a pointer: "how large it can be is fixed by positivity (\cref{sec:8.3-bound})".
- The sector recap appears twice: s8-6 l.5 lists the three sectors, and s8-7 l.9 opens by listing them again (see 8.7).

**Seams.** Each adjacent pair was read across the join.
- 0→8.1 is clean. 8.1→8.2 is clean: 8.1 ends on "covers all three", and 8.2 opens on three processes asking "one question".
- 8.2→8.3 is clean apart from the pre-stated bound above. 8.3→8.4 is clean. 8.4→8.5 is clean, and 8.5→8.6 is clean (θ_ep ≪ 1 hand-over).
- 8.6→8.7: 8.6 ends on open problems. 8.7 opens on the 10 eV deposit, but its first subsection then recaps 8.6.
- 8.7→8.8 is clean.
- **Systemic arrangement problem.** The label of 8.5 is used from 8.2 on, before it is defined: 𝔗 (s8-2 l.30 "the truncation label $\mathfrak{T}$ of \cref{sec:8.5}"), n_T (s8-2 l.63), n_B (s8-3 l.50, bare: "In the Born--Oppenheimer approximation, $n_B = 0$,") and n_g (s8-4 l.128). This violates "no forward references for definitions". Fix in prose, without reordering: gloss each first use in words, for example s8-3 l.50 "In the Born–Oppenheimer approximation (no derivative coupling, the order that \cref{sec:8.5} calls $n_B = 0$)", and s8-2 l.63 "the expansion in phonon occupations (\cref{sec:8.5})".

**Register (REGISTER.md).** Counts per 10k words of prose, math stripped. L = Lin (TASI).

| | so | gives | only | however | we will/can/see | typical | of order | note that |
|---|---|---|---|---|---|---|---|---|
| L (model) | 11 | 7 | 11 | 8 | ~30 | 15 | 0 | 6 |
| 8.1 | 25 | 22 | 32 | 2 | 0 | 0 | 5 | 0 |
| 8.2 | 19 | 22 | 16 | 6 | 3 | 0 | 3 | 0 |
| 8.3 | 17 | 26 | 26 | 5 | 0 | 2 | **26** | 0 |
| 8.4 | 19 | 17 | 19 | 2 | 2 | 0 | 14 | 0 |
| 8.5 | 28 | 14 | 14 | 6 | 3 | 3 | 11 | 0 |
| 8.6 | 19 | 14 | **39** | 3 | 2 | 2 | 14 | 2 |
| 8.7 | 27 | 17 | 19 | 2 | 5 | 2 | 7 | 0 |
| 8.8 | 29 | 16 | 27 | 2 | 2 | 0 | 2 | 0 |

- The chapter shows REGISTER's "airless" profile. It has almost no "we will/can/see", "however" at a quarter of Lin's rate, almost no "typical", and an excess of "only" and "of order".
- It is not a voice failure, since the sentences are idiomatic. Fix it per section, through the calibration rewrites below.
- REGISTER rule 11 ("We call") is broken twice: s8-6 l.24 "We call the range of $\mathcal{P}_{\mathrm{ad}}$ the \emph{electron-following sector}" and s8-7 l.92 "… we call \emph{seeding}".
- REGISTER term 6 (bare "transfer" as a noun): D-24 l.7 "The transfer $\vect{q}$ is invariant".
- The tic "exactly" runs at 17/10k in 8.4 and 8.6. Keep it where it marks a theorem and cut it elsewhere (for example s8-4 l.54, s8-6 l.29).

**Number style.** Percentages are written two ways within the chapter: `\SI{10}{\percent}` (s8-1, s8-3, s8-4, s8-8 summary) and "21 percent", "2 percent", "a factor three" (s8-5, s8-6, s8-7, s8-8). Pick `\SI{}{\percent}`, as Chap. 5 does, and apply it chapter-wide.
- s8-7 l.81, 83, 88, 110 "a volt" for 1 eV. A volt is a potential, not an energy. Write "about 1 eV".
- s8-7 l.79 "a factor 0.29" → "a factor of 0.29".

**Standalone scrub, user rules and citations.**
- No exercises, checkpoints, "left to the reader" or internal labels anywhere. Cross-references are all \cref. There are no limit boxes in this chapter. Every display is punctuated.
- Citations attribute, with two exceptions that lack an equation pinpoint: s8-3 l.70 `\cite{puff1965application}` and s8-4 l.58 `\cite{hochberg2021determining}`. Add the equation or section. `\cite{fano1961effects}` and `\cite{cohen1966band}` cite whole works and are acceptable.
- No citation carries content. Tab. 8.6 cites literature equations per cell, but each cell also names the section of this book that derives the formula, so it is not pattern 20.
- Floats: `tab:8-sectors` sits at s8-6 l.71, before its first citation at l.89. Move the environment below that paragraph. Every other float is cited before it appears.
- Captions stand alone. Exception: Fig. 8.3 (s8-7 l.133) ends "Schematic; chapter numbers inside the figure follow the table of contents." That is a production note (pattern 19). Drop it, or make the figure use the book's numbers.

## 3. Sections

### 8.1 Dark-matter couplings to a target (~4,000 words): REVISE
Calibration. (a) l.3 opener: Lin could have written it. (b) l.87 "The reduction separates the dark-matter velocity from the target's own velocity, and it makes the rows overlap.": a category frame. (c) l.159 "The electron gas understates the effect in a real crystal …": good.
Rewrite of (b), as Lin: "In a solid the electron moves too. A valence electron of silicon is seven times faster than any dark-matter particle in the lab, so the velocity operators pick up a piece that has nothing to do with the dark matter's motion."
- l.3 | 1 | "In this section we build the list, reduce each … and add …" → "We will build the list, …". Better still, cut it, because l.3 already states the result.
- l.184 | editor | The Coulomb-energy row (the photon kinetic-term scalar). Grep of tex/ finds no later user, and the row is absent from Tab. 8.1. Either point to its user (\cref{sec:10.7}?) and add a table row, or drop the paragraph.
- l.124 | editor | The ²⁹Si abundance (4.68 %, IUPAC, `meija2016isotopic`) is missing. The 10 % figure is per ²⁹Si nucleus. Add "and it makes up 4.68 % of natural silicon~\cite{…}" so that a natural sample is not misread.
- l.124 | 13 | "A $^{29}$Si nucleus thus responds with \SI{10}{\percent} of the strength of one neutron, whereas …" is good. "A sample … moreover" → drop "moreover".
- l.15 | 17 | "With $\vect{q}/m_e$ in place of $\vect{q}$, each operator is dimensionless." This needs "(the table writes $\vect{q}/m$)". As written the reader cannot tell whether $\mathcal{O}_i$ already contains $1/m$.
- l.20 | 19 | "Also, the operators are written here with the $\vect{q}$ of this book, which the dark matter loses." → "Refs. [ ] define $\vect{q}$ as the momentum the dark matter gains, so …". One clause on the literature (pattern 19 allows convention notes phrased as a fact about the literature).
- l.26 | 18 | "A solid is not a free electron." Good, keep it.
- l.109 | 2/13 | "A practical calculation computes …" → "In practice a calculation computes …" (REGISTER idiom).
- Symbol (editor): $\mathcal{J}^{\alpha\beta}_s$ (spin current) clashes with C.20's $\mathcal{J}(\omega)$. Rule it at the merge. Renaming C.20 to $J_{\mathrm{s}}(\omega)$ leaves Chap. 8 untouched.

### 8.2 The master rate formula (~3,200 words): REVISE
Calibration. (a) l.3 opener, "… all ask the crystal one question.": Lin could have written it. (b) l.28 "The derivation uses four assumptions, and each can fail in a known place.": a count-teaser that is then enumerated. Acceptable. (c) l.83 "The off-diagonal terms of the contraction are the part of a rate that no single-operator calculation contains.": good.
Rewrite of l.65 "Exothermic dark matter moves the support instead of the weight.", as Lin: "Exothermic dark matter does something different: it does not reweight the band, it moves it."
- l.100 | editor | The required sentence is missing: that no standard model produces $\mathcal{O}_7$ at leading order. After "A spin coupling free of $\vect{S}_\chi$ is $\mathcal{O}_7$ …" add "No standard model produces it at leading order (\cref{sec:8.1}); we take it as the simplest operator with the right symmetry."
- l.30, l.63 | arrangement | "the truncation label $\mathfrak{T}$ of \cref{sec:8.5}", "the thermal order $n_T$ of \cref{sec:8.5}". Gloss these in words (see §2).
- l.30 | 9 | "The master formula sits at every point of that label." → "No truncation of the target changes the master formula; it changes only $S_{ab}$."
- l.55 | 10 | The paragraph is 280 words on classical bosons. Split it at "The average needs an observation time …".
- l.57 | redundancy | "Which rows are screened in this way, for every coupling, is the question of \cref{sec:8.4}." Cut (see §2).
- l.116 | redundancy | "The bound \cref{eq:4.2-positivity} limits its size to twice the geometric mean …" Make it a pointer (see §2).
- Editor note: t_coh is now first used here (l.55). Done.

### 8.3 Exact relations (~4,200 words): REVISE
Calibration. (a) l.3 "A computed response of silicon can be wrong in ways that no convergence test reveals.": exactly Lin's register. (b) l.109 "pushes every part of the crystal in the same proportion … like a gravitational field": Lin could have written it. (c) l.78, a long chain of regimes: no.
Rewrite of l.78, as Lin: "The small-q form has a limited range. Once q passes $G_{\min}$ the valence structure starts to matter, and once q resolves the 1s shell the contact term grows. For larger q the bracket climbs from $\nd_e^{(\kappa)}/3$ toward $\nd_e^{(\kappa)}$."
- l.50 | first use | "In the Born--Oppenheimer approximation, $n_B = 0$," uses $n_B$ before 8.5 defines it. Write "(order $n_B = 0$ in the label of \cref{sec:8.5})", or drop the symbol here.
- l.3 | 18 | "The multi-operator rate of \cref{sec:8.2} needs three more." The next sentences name them, so this is acceptable. Better: "… needs three more: an interference bound, higher moments and a Ward identity."
- passim | register | "of order" at 26/10k (L: 0). Use "∼" or "at order" in l.50, 74, 78, 143 and 152.
- l.70 | citation | `\cite{puff1965application}` lacks a pinpoint. Add the equation.
- l.85 | 12 | "by some \SI{8}{\percent} … and by more in heavier atoms": give the scaling ($\propto (Z\alpha)^2$).
- l.180 | 5 | "They share a structure. Each follows from a symmetry or a conservation law …" This restates l.3 ("holds for every target", "None depends on an approximation"). Keep one sentence and the table pointer.
- Editor: \varGamma_A/B/AB done; $\mathscr{M}^k$ in $\mathrm{eV}^{k+3}$ done (l.39).

### 8.4 Screening for every coupling (~4,200 words): REVISE
Calibration. (a) l.3 opener, the GaAs zero of ε at 36.35 meV: Lin could have written it. (b) l.119 "The rule $1/|\varepsilon|^2$ gets this wrong in an instructive way.": good. (c) l.69, a 400-word paragraph on necessity: no.
Rewrite of l.69's opening, as Kahn and Lin: "The converse takes two limits in which electrons and nuclei come apart. At large q each particle recoils on its own, and the peaks sit at different energies. At small q the crystal moves as a whole, and only the net charge per cell matters."
- l.48 vs s8-7 l.12 | symbol | $\varepsilon_e$ is the electron-channel dielectric function here and the electron's kinetic energy in 8.7 (editor 76(d)). Rename the carrier energies (for example $E_{\mathrm{e}}, E_{\mathrm{h}}$ or $\epsilon_{\mathrm{e}}$).
- l.54 | first use | $\Pi_{\mathrm{em}}$ appears in "its propagator $1/(\omega^2 - q^2 - \Pi_{\mathrm{em}})$" but is defined only at l.151. Add "with $\Pi_{\mathrm{em}}$ the photon self-energy of the medium".
- l.146 | term | "it is the photon version of the improper response". "Improper" is used nowhere else; the book says "full" or "photon-reducible". Write "the photon-reducible part of the response".
- l.159 | register | "One may instead put the chain into the mediator" → "We can instead …".
- l.58 | citation | `\cite{hochberg2021determining}` lacks a pinpoint. Add the equation or section.
- l.69 | 10 | The paragraph is ~400 words. Split it at "The signs are fixed at the opposite end".
- l.163 | 3 | "the many-body rung, the phonon order, the static vertex" (a rhythmic triad of label jargon) → "what a calculation keeps of it is a truncation that \cref{sec:8.5} labels".
- l.128 | arrangement | "($n_g = 2$ in the label of \cref{sec:8.5})" is a forward symbol. Write it in words.
- Editor: n_Z used, ρ_c unused. Prose-neutral.

### 8.5 The expansion hierarchy (~3,600 words): PASS
Calibration. (a) l.3 "… agree with the neutron values to 2 percent … and yet it is a truncated formula.": Lin could have written it. (b) l.72 "The boundaries are, of course, gradual …": good. (c) l.81, the rule for orders: dense but clear.
Rewrite of l.112, "The steps differ in sign and do not shrink.", as Lin: "Each rung moves $\varepsilon_\infty$ by about as much as the last, and not always in the same direction, so there is nothing to expand in."
- Title l.56 | 16 | "One phonon, many phonons, free recoil" is a triad, not a noun phrase. Use "Lattice regimes". l.5 "Seven small numbers" → "Small parameters".
- l.81 | 19 | "The Born--Oppenheimer order $n_B$ always appears with its value, as in $n_B = 0$, which distinguishes it from the Bose function $n_{\mathrm{B}}(\omega)$." Typography is carrying a symbol clash. Rename one of the two at the merge (notation), then drop the sentence.
- l.3, 112, 132 | style | "2 percent", "11 percent", "a few percent". Use \SI (see §2).
- l.83 | 18 | "Each component is best seen at its two lowest values, and the earlier chapters have met both." Acceptable.

### 8.6 The decomposition theorem (~5,900 words of prose): REVISE
Calibration. (a) l.3 opener, the 1 GeV kick, 7×10⁻⁴, "21 percent … 47 percent": Lin could have written it. (b) l.22 "the electron cloud of a moving nucleus lags behind it and is slightly polarized": a model physical picture. (c) l.183 (Fano paragraph, about 300 words): no.
Rewrite of l.183's opening, as Lin: "There is one more term, and it changes no total. When the pair decays, its first phonon can interfere with the same phonon emitted directly. That shifts which branch the first phonon goes into, by an amount of order the width over the detuning."
- l.5 | 18 | "This section turns the bookkeeping into a theorem." is an abstract frame. → "To keep the sum honest we split the final states of every response into three sectors: …".
- l.24 | REGISTER 11 | "We call the range … the \emph{electron-following sector}" → "The range of $\mathcal{P}_{\mathrm{ad}}$ is the \emph{electron-following sector}".
- l.197 | 10/editor | The Dirac sentence (60 words, three clauses joined by semicolons) needs splitting, and the reasoning should be named. Write "By dimensional analysis the quasiparticle width is ω times a function of α̃, which starts at α̃² because a decay needs two Coulomb vertices. The split is therefore meaningful only for α̃² ≪ 1." Also gloss α̃ at its first use in the chapter: "the effective coupling α̃ of \cref{sec:7.3}".
- l.3, l.210 | style | "21 percent", "47 percent", "12 percent". Use \SI.
- l.183 | 10 | The paragraph is ~330 words and does three jobs (Fano term, the Fano-factor disambiguation, the PT theorem). Split it at "In many crystals it vanishes."
- l.174 | 10 | The ambiguity paragraph is ~350 words. Split it at "Two mixed conventions are common and wrong."
- Budget (editor). My count is ~5,850 prose words without math, which is at the 6,050 note. Cut candidates: the restated sector list at l.5 (the table and l.29 carry it), and the l.91 paragraph on code chains, which could shrink to two sentences pointing to App. E.
- Editor: $P_{\mathrm{Mig}}$ and $\delta M_\kappa$ now first appear here (l.105, l.117). Done. "The atomic value, $14\,m_e$, … we take it as the estimate" is labeled. Done.
- l.71 | float | Tab. 8.6 appears before it is cited (see §2).

### 8.7 Final-state-resolved response (~4,150 words): REVISE
Calibration. (a) l.3 opener, the 10 eV deposit, lopsided versus even split, the step model: Lin could have written it. (b) l.88 "A volt is close to the gap, and so to the energy scale on which impact ionization switches on.": the picture is good but the unit is wrong. (c) l.116 "The cascade remembers $\vect{q}$ mainly through its first generation.": excellent.
Rewrite of l.83's last sentence ("Three seeds at one energy deposit, three different distributions of the energy that the cascade starts from."), a verbless fragment, as Lin: "So three seeds with the same energy hand the cascade three different starting distributions."
- l.9 | 18 | "\Cref{sec:8.6} split every final state into three sectors: …" is a recap opener. → "The cascade needs more than the sector a final state lies in: it needs the state itself, …" and cut the sector list.
- l.12, 81, 116 | symbol | $\varepsilon_e$, $\varepsilon_h$ clash with 8.4 l.48 (see 8.4).
- l.81, 83, 88, 110 | units | "a volt", "about a volt more energetic" → "about 1 eV".
- l.92 | REGISTER 11 | "The step … we call \emph{seeding}" → "This step, \emph{seeding}, turns …".
- l.79, 81, 83, 85 | style | "13 percent", "63 percent", "83 percent", "15 percent", "factor 0.29". Use \SI and "factor of".
- l.133 | 19 | The caption tail "Schematic; chapter numbers inside the figure follow the table of contents." Drop it (see §2).
- l.139 | 18 | "Two questions remain open. The identification …" is followed by "The second is …". Mark the first one ("The first is the identification …") for symmetry.
- Editor: P_casc first used here (l.92), done. ε̃⁻¹ glossed as "the inverse dielectric matrix of a test electron" (l.49), done. The ε_e/ε_h widening is done but creates the clash above.

### 8.8 Uncertainty structure (~4,400 words): PASS
Calibration. (a) l.3 opener, local fields shifting the screening factor by a quarter: Lin could have written it. (b) l.113 "The two are different statements, a likelihood and an envelope, and a result must say which it reports.": good. (c) l.22 "When is $\Delta S_k$ computable? … In the first case … In the second … In the third …": acceptable.
Rewrite of l.20, "The one thing a nuisance must not do is vary from bin to bin.", as Kahn and Lin: "A nuisance must not vary from bin to bin. A truncation is a property of the calculation, not of the bin, and the same parameter has to act everywhere."
- l.127 | 14 | "The uncertainty of a rate is thus no longer a matter of judgment." This overclaims, since l.22 admits a third case with no width (the pair-channel screening). → "The uncertainty of a rate then rests on computed steps wherever they exist, and names its omissions where they do not."
- l.108 | editor | "for this illustration we set the threshold to the value $\mathsf{t}^* = 2N_{90}$" is labeled. Done.
- l.103 | symbol (editor) | $\mathsf{L}$ (likelihood) clashes with 4.9's pair propagator. Rule it at the merge.
- l.73, 113, 118, 122 | style | "6.1 percent", "1.0 percent … 19 percent", "13 percent", "2.1 and 3.0 percent". Use \SI.
- l.3 | 18 | "What remains is to turn each truncation into a number that a likelihood can use." This is a bridge with payload. Acceptable.

## 4. Appendix D.24–D.28: PASS
- D-24 l.3 | 18 | "This section derives the four steps: …" is a count-teaser and list opener. → "Four steps take a two-particle interaction to target rows: …". l.7 "The transfer $\vect{q}$" → "The momentum transfer $\vect{q}$". l.12 "(local to this section)" → "(used only in this section)".
- D-28 | structure | It uses `\subsection*` (8 times), while D.24–D.27 use numbered `\subsection`. Pick one.
- D-28 l.3 | 18 | The opener lists five verbs ("bounds…, constructs…, derives…, proves…, and expands…"). Acceptable for an appendix, but shorten it to the first sentence plus "The notation is …".
- D-27 l.67 "which no crystal of this book contains" is fine. D-25 and D-26 are clean. Their equations are punctuated and every symbol is defined.

## 5. Editor-notes items that concern prose
| Item | Status |
|---|---|
| 8.1 ²⁹Si abundance and J = ½ | J done; abundance and its citation missing (8.1) |
| 8.1 Coulomb-energy row: find its user or drop it | no user found in tex/; drop it or point to one (8.1) |
| 8.1 𝒥 spin current vs C.20 𝒥(ω) | notation, rule at the merge |
| 8.2 the text must say no standard model produces O₇ | **missing** (8.2 l.100) |
| 8.2 t_coh first use moved here | done |
| 8.6 Dirac width ∝ α̃²ω: say it comes from dimensional reasoning | implicit only; add "by dimensional analysis" (8.6) |
| 8.6 P_Mig and δM_κ first uses; δM_κ labeled as an atomic estimate | done |
| 8.6 budget (~6,050 words) | ~5,850 prose words; cuts proposed |
| 8.7 P_casc first use; ε̃⁻¹ gloss; ε_e/ε_h widened | done; the widening creates the ε_e clash with 8.4 (fix) |
| 8.3 \varGamma rates; 𝓜^k units | done |
| 8.5 n_B vs n_B(ω) (raised here) | notation; the prose workaround at s8-5 l.81 should go once renamed |
| 8.8 𝖫 vs 4.9; t* labeled | notation at the merge; t* done |
