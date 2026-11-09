# Ch7 prose review (style, register, standalone scrub)

Scope: tex/ch07/ch07.tex, s7-1 … s7-4 (Summary included, it sits at the end of s7-4.tex), App. D.19–D.23. Checked against STYLE.md, style-guide.md, prose-review.md, REGISTER.md and ledgers/REVIEWS/ch07/editor-notes.md. Line numbers are file lines. The tex was not edited.

## Verdicts

| Section | Words | Verdict | Reason |
|---|---|---|---|
| Chapter opening (ch07.tex) | 264 | PASS | Concrete and motivational. It runs through the targets in section order, which is borderline (C1). |
| 7.1 Magnetic order and spin waves | ~3.8k | REVISE | About 4 hits per 1k words: 12 S-items plus C2, C3a and C4. The voice is good, but there is a garden-path closing (S1-9) and a forward reference to a definition (S1-2). |
| 7.2 Superconductivity | ~4.5k | REVISE | Count-teasers, a closing paragraph that restates the section, the 900× Cooper comparison made twice, a cross-seam contradiction about σ, overloaded paragraphs, and "coherence length" never used. |
| 7.3 Dirac and narrow-gap materials | ~4.1k | REVISE | The "steep"/"slow" contradiction, the 10 keV claim against the 10.5 keV threshold, an incorrect pair-at-rest picture, the ε_bg double-counting point made three times, and a long uniqueness derivation in the running text. |
| 7.4 Defects and dopants | ~4.9k | REVISE | About 3 hits per 1k words, including two outright errors: "1s triplet" (S4-7) and the overloaded symbol a (S4-8). |
| Summary (end of s7-4) | ~830 | REVISE | Wrong file. Its 29.7 meV does not match the 31.3 meV reference. Its triad repeats 7.4. |
| D.19 | 1.2k | PASS | Title is long. It cites E.9 equations where the main text defines them. Numerical assurance at l.104. |
| D.20 | 1.1k | REVISE | "as one checks" (user rule). "the second form" (pattern 13). "Machine precision" assurance. |
| D.21 | 1.4k | REVISE | Upright Γ for vertices (editor ruling). "RPA" in prose. Precision assurances. |
| D.22 | 0.9k | REVISE | "only" tic (86 per 10k). One unclear sentence (l.55). Title acronym. α and β not yet swept. |
| D.23 | 1.0k | REVISE | "prolate" should be oblate (an outright error). α_j clashes with α. |

## 1. Lint (lint.py with BANNED-TERMS)

No banned-term hits and no blocking hits in any file.
- **EQ-PUNCT (16 hits): all are false positives.** s7-1:107; s7-2:66, 93, 122, 164, 196; s7-3:89; D-19:45, 70; D-20:32, 106; D-21:47; D-22:8; D-23:67. In each one the punctuation sits before `\end{gathered|aligned|split}`, or the sentence continues past the display (s7-2:164 "…are the physical operators"; s7-2:196 "…at every frequency"; D-22:8 "…per state"). **The real fault is one the lint missed:** s7-1 l.16, `eq:7.1-dirac` ends with "," and the sentence resumes "has the singlet energy". The comma separates subject and verb. Delete it.
- **TITLE (1):** D-19 l.1, "Linear spin waves of a two-sublattice antiferromagnet" (6 words). Use "Antiferromagnetic spin waves".
- **LONG-SENT (24).** About half come from the lint merging a sentence across a display or a caption, so they are not real: s7-1 kinetic-exchange, caption and spin-density; s7-2 Eliashberg; D-20 model, Fermi, keyresult; D-21 Ward. These are real and should be split:
  - s7-1 l.93, "Leaving out the one-magnon states … costs $0.382|J^{\mathrm{ex}}|$ in linear spin-wave theory: magnons attract each other, …" (~55 words). Split at the colon.
  - s7-1 l.192, "Inverting it, … and \cref{app:D.19} shows that the transverse spin … near the zone center …, and near the ordering wavevector, …" (~70 words). Split into one sentence per region.
  - s7-2 l.31, "If one also replaces the frequency-dependent coupling …" See R7.2c.
  - s7-2 l.139 and l.179. See S2-6 and S2-9.
  - s7-4 l.37 (the cleft sentence, R7.4a); l.83 ("At $T=0$ the emission lines …"; acceptable); l.130 (the E_d definition; acceptable).
  - D-20 l.81, the harmonic-number sentence (~80 words). Split after "vanishes".

## 2. Chapter-level findings

**C1 Opening (ch07.tex l.3).** The first sentence is concrete ("Silicon offers dark matter two kinds of excitation …") and the last orients in one sentence, as required. In between, five sentences take NiO → Al → Dirac → donors in section order. This is a roll-call, close to the outline the user rule forbids. It does not need a rewrite. Fix: merge the Dirac and donor sentences into one ("Dirac materials offer pair excitations from a few to tens of meV, and donors and color centers put bound levels inside the gap of silicon itself, shallow for a donor and deep for a color center"). Also replace "the bound $2\omega/v_{\mathrm{max}}^2$" with "$2E_{\mathrm{th}}/v_{\mathrm{max}}^2$", the form 7.2 l.3 uses. The intro also leaves out displacement damage, the third role in 7.4. Add one clause: "and a struck atom can leave a defect that stores energy."

**C2 Uniform roadmap tail (patterns 1, 18).** All four section openers end the same way: "We will … ; the section closes/ends with [worked example]".
- 7.1 l.3: "We will derive … The section closes with the magnon velocity of NiO …"
- 7.2 l.3: "We will derive … Then we compute … The section ends with the gap and the threshold mass of aluminum."
- 7.3 l.3: "In this section we obtain … ; at the end we evaluate …"
- 7.4 l.3: "We will compute …"

Fix: keep at most one "we will" sentence, saying what the reader will be able to compute. Delete every "The section ends/closes with …" sentence, since the worked example announces itself. In 7.3, change "In this section we obtain" to "We obtain".

**C3 Restatement across sections (pattern 5).**
- (a) The intro says "every spin is paired in a bond and flipping one costs the gap". 7.1 l.3 repeats it: "Silicon has nothing comparable. Its electrons pair their spins in the bonds, and flipping one spin means making an electron–hole pair, which costs at least the gap." Cut the 7.1 version to one clause: "In silicon, where bonded spins cost the gap to flip, a spin-coupled particle has no such channel."
- (b) "0.36 meV / 0.1 keV" appears five times: intro, 7.2 l.3, WE 7.2 l.222–224, 7.2 l.233 and the Summary. Drop it from the 7.2 closing (see S2-12).
- (c) The intro says "the gap can be a few meV" and 7.3 l.3 repeats "Their gap can be a few meV." Cut the 7.3 copy.
- (d) Every section except 7.4 closes on a recap, and the Summary recaps again. Close each section on a consequence or a pointer (REGISTER 3.7).

**C4 Numerical-precision assurances (pattern 19).** Checks that carry physics stay:
- the magnon attraction (s7-1 l.93);
- the Anderson–Bogoliubov speed 0.579 against 0.577 (s7-2 l.202);
- the bare bubble off by factors of 28 and 4 (D-21 l.103);
- the exact effective-mass solution against the variational one (s7-4 l.28);
- the D.19 statement that the classical and linear quantum theories agree.

Pure reassurance to a reviewer should be cut or reduced to a clause:
- s7-1 l.93, "agree with $\omega^{\mathrm{M}}_k$ to $4\times10^{-16}|J^{\mathrm{ex}}|$". The statement was proved two sentences earlier.
- s7-1 l.156, "A scan of $4\times10^5$ wavevectors with a local maximization finds that …". Change to "Both conditions hold at once, so …".
- s7-2 l.148, "agrees with their closed form in elliptic integrals to numerical precision". Change to "reproduces their closed form in elliptic integrals".
- D-19 l.104, "to $10^{-12}J_2$"; D-20 l.93; D-20 l.125, "to machine precision"; D-21 l.103, "holds to $10^{-15}$"; D-22 l.33, "to $10^{-5}$"; D-22 l.64, "to $10^{-4}$".

**C5 Duplicated keyresult boxes.** The gap equation, the coherence factors, the conserving response and the Ward identity each appear as a keyresult in both 7.2 and D.20/D.21. The AFM spin waves appear in both 7.1 and D.19. The text already states each result and points to the derivation. Fix: keep the box in the main text, and make the appendix copy a plain numbered equation.

**C6 Summary placement and content.** The `\section*{Summary}` is in s7-4.tex at l.149. Move it to ch07.tex after `\input{ch07/s7-4}`, since STYLE requires one file per section. At l.157, "Effective-mass theory gives \SI{29.7}{meV} for every donor, and the central-cell correction … brings phosphorus to its measured \SI{45.6}{meV}". But the 14.3 meV correction is measured from 31.3 meV, so write "\SI{29.7}{meV} (\SI{31.3}{meV} at the liquid-helium $\varepsilon_0 = 11.4$)". At l.157, "Donors are targets, color centers are targets and optical readouts, and displaced atoms are final states with a memory." This repeats the 7.4 subsection and the opener. Cut it and end on the pointer to Chap. 8.

**C7 Seams.**
- intro→7.1: see C3a.
- 7.1→7.2: good. 7.2 l.58 ties the fermionic Bogoliubov transformation to the AFM, and l.202 ties the Goldstone mode to the ferromagnet.
- 7.2→7.3 is a **contradiction**. s7-2 l.170 says "which we do not call $\sigma_i$ because those act on the electron spin". s7-3 l.14–18 then uses $\sigma_x,\sigma_y,\sigma_z$ for the doublet Pauli matrices. Apply the editor ruling, $\sigma^{\mathrm{d}}_i$. A one-clause bridge would help at the 7.3 opener: like the BCS edge, the Dirac pair continuum starts at twice a half-gap.
- 7.3→7.4: acceptable. However, the "0.333 MeV that silicon requires" is attributed to `\cref{sec:1.3}` in s7-3 l.3 and to `\cref{sec:3.3}` in s7-4 l.3. Use one, sec:1.3 (where m_min is defined).

**C8 Register (per 10k words; L = Lin).**

| | 7.1 | 7.2 | 7.3 | 7.4 | D.19–23 | L |
|---|---|---|---|---|---|---|
| typical(ly) | 0 | 0 | 0 | 0 | 0 | 15 |
| we will/can/see/have/find | 3 | 2 | 5 | 2 | 0 | ~40 |
| however | 8 | 4 | 0 | 4 | ≤9 | 8 |
| gives | 19 | 20 | 12 | 24 | 21–34 | 7 |
| so | 24 | 11 | 24 | 16 | 7–35 | 11 |
| of order | 3 | 9 | 12 | 2 | 8–20 | 0 |
| only | 21 | 15 | 17 | 20 | **86 in D.22** | 11 |

- The voice is consistent across the four writers: plain verbs, "we", good physical pictures, honest caveats.
- The register still lacks the model's hedge ("typical") and its "we see/we can", as before.
- "gives" runs at about 3× the model's rate. Swap a third of them for "is", "leads to" or "yields".
- 7.3 has no "however".
- D.22 should cut four "only"s (l.3, 14, 33, 69).
- Spell "percent" one way: the text mixes "5 percent" and `\SI{2.6}{\percent}` in a single sentence (s7-4 l.37).

**C9 Field terms missing.**
- 7.2 never says **coherence length**, though it uses $v_{\mathrm{F}}/\pi\Delta_{\mathrm{BCS}}$ ("the size of a pair") at l.213 and l.226.
- 7.4 l.50 describes the **Mott (metal–insulator) transition**, "the isolated-donor picture fails before the orbits touch", without naming it.
- Name each one once.

**C10 Source process artifact.** ch07.tex l.5 has the comment "% Sections are \input here as they are accepted". Delete it.

## 3. Issues by section (location → problem → fix)

### 7.1
- S1-1, l.3 [18]. "To compute such a rate we need three things: …", then "We will derive …", then "The section closes with …": three roadmap sentences. → Keep "three things" and cut the last two (C2).
- S1-2, l.34–38 [arrangement, 19]. $J_2$ and $J_1$ are quoted "in the convention of \cref{eq:7.1-heis} below, which is the convention of that reference", before the model is defined, and the clause reassures rather than informs. → Move eq. (7.1-NiO) to after the Heisenberg model (l.45), or keep it and delete ", which is the convention of that reference". The convention note at l.45 already covers this.
- S1-3, l.45 [one job per paragraph]. The paragraph defines the model, gives the convention warning, describes the FM and AFM ground states, NiO type II and the anisotropy (~230 words). → Start a new paragraph at "If every $J^{\mathrm{ex}}_{ij} < 0$".
- S1-4, l.16 [eq. punct.]. See §1.
- S1-5, l.80 [idiom]. "In a picture, the magnon …" → "Physically, the magnon …".
- S1-6, l.100 [1]. "here are its steps and its result." → Delete the clause.
- S1-7, l.106 [13]. "the last term creates or destroys deviations in pairs" → "the pair term $d_{\mathrm{A}i}d_{\mathrm{B}j} + \text{h.c.}$ creates or destroys …".
- S1-8, l.129 [5]. "the ground state lies below the classical Néel energy. The Néel state is not the ground state, and …" says the same thing twice. → "…below the classical Néel energy: in the true ground state each site of A carries …".
- S1-9, l.199 [second reading]. "The spin waves of an ordered magnet thus give dark matter with a spin coupling a target whose excitations run from …" is a garden path. → "For dark matter with a spin coupling, an ordered magnet is a target whose excitations run from a few meV, where anisotropy cuts off the Goldstone mode, to about \SI{0.1}{eV}, below any electronic gap of the same crystal."
- S1-10, l.168 [20]. "with one of the couplings of Ref.~\cite[Table~I]{trickle2020detecting}" leaves the content to the source. → "with a spin-dependent coupling (the operators are listed and derived in \cref{sec:8.1}), the interaction takes the form …~\cite[Eq.~(4)]{trickle2020detecting}."
- S1-11, Fig. 7.1 caption (l.141) [caption]. The energy unit is missing. → "(b) Magnon energies $\omega^{\mathrm{M}}_{\vect{k}}$ (meV) …".
- S1-12, l.176 [comma chain]. "the inverse radius of the shell, a few \si{\angstrom^{-1}}, that is several keV, for a $3d$ shell (…), above most …" → "For a $3d$ shell it stays close to one up to the inverse shell radius, a few \si{\angstrom^{-1}} or several keV (\cref{app:C.19}), above most momentum transfers of sub-MeV dark matter."

### 7.2
- S2-1, l.3 [18, 5]. "Three questions have to be answered before any rate can be written down." is a count-teaser. The two "We will … Then we compute …" sentences then answer the same three questions in the same order. → Delete the teaser and keep the three questions. Replace the two roadmap sentences and "The section ends with …" by "We answer them in turn, from the electron–phonon vertex of \cref{sec:6.2}."
- S2-2, l.31 [18]. "\Cref{eq:7.2-NV} leaves out two effects of the same order." → "\Cref{eq:7.2-NV} leaves out the Coulomb repulsion and the quasiparticle renormalization, both of the same order."
- S2-3, l.31 [register, arrangement]. "If one also replaces …, \cref{eq:E.9-Delta} becomes the gap equation \cref{eq:7.2-gap} below, written in Matsubara form, with". The "one" construction and the forward reference to a result not yet derived. → R7.2c.
- S2-4, l.51 against l.230 [5]. The single-pair binding "about 900 times smaller" and "the pairs bind each other more strongly than a single pair is bound" appear in both places. → Keep l.51 and cut the last paragraph of WE 7.2 (l.230), or the reverse.
- S2-5, l.89 [symbol]. $g_{\mathrm{deg}}$ is used here for spin degeneracy, while 7.3 l.36 defines it per Dirac cone. → Keep both, but state the meaning at each use (already done at 7.3). Acceptable.
- S2-6, l.139 [one job; length]. The kinematics argument (~230 words) carries a 45-word sentence starting "Two quasiparticles with $E + E' = \omega$ …". → Split after "at some angle", and start the dark-matter regime as its own paragraph at "This is the regime of dark-matter scattering in a metal."
- S2-7, l.170 [seam]. "which we do not call $\sigma_i$ because those act on the electron spin" contradicts 7.3. See C7.
- S2-8, l.18 [first use]. $\Omega$ in "$V = N\Omega$ the volume of the crystal" is not defined in 7.2. In 7.1 l.182 it is the volume per magnetic ion. → "with $\Omega$ the unit-cell volume".
- S2-9, l.179 [17]. "The response then becomes a random-phase approximation in the channels … with the kernel …, the random-phase approximation of \cref{sec:4.5} with the pair channels in place of the Coulomb one:" names the approximation twice. → "The response is then the random-phase approximation of \cref{sec:4.5}, with the pair channels $(\boldsymbol{\eta},\mathsf{s}_1,\mathsf{s}_2)$ in place of the Coulomb channel and the kernel $K = …$:".
- S2-10, l.211 [one job; semicolon chain]. One ~300-word paragraph covers the normal-state check, the gap term, the ladder, the Goldstone pole, the spin density and a scope pointer. "Its Nambu vertex is the unit matrix, which commutes with $h_{\vect{k}}$; total $S^z$ commutes with $H_{\mathrm{MF}}$ and …; the case-II curve … is final at this level." → Start a new paragraph at "The spin density needs no such correction." and make three sentences of the semicolon chain.
- S2-11, l.213 [second reading; C9]. "the wavelength $1/q$ that the particle probes divided by $\pi$ times the size of a pair, $v_{\mathrm{F}}/\pi\Delta_{\mathrm{BCS}}$" → "$1/\pi$ times the ratio of the probed wavelength $1/q$ to the coherence length $v_{\mathrm{F}}/\pi\Delta_{\mathrm{BCS}}$, the size of a pair". Use "coherence length" at l.226 too.
- S2-12, l.233 [5; REGISTER 3.7]. The closing paragraph restates the section in five sentences, and the Summary restates it again. → Keep the first sentence (edge 3000× below the Si gap) and the f-sum-rule sentence, then the pointer to \cref{chap:15} and \cref{sec:20.4}. Cut the rest.
- S2-13, l.228 [first use]. "$\omega_{\log} = \SI{270}{K}$" is undefined here. → "the logarithmic average phonon energy $\omega_{\log}$ of \cref{sec:6.4}". If it is defined in E.9, point there.
- S2-14, l.204–211 [editor]. The dressed vertices still use $\varGamma$. Rename to $\mathsf{V}$ (editor ruling, open).

### 7.3
- S3-1, l.3 and l.154 [contradiction]. "because the bands are steep but not too steep" (l.3) and "slow, steep bands" (l.154) contradict each other: slow bands have a shallow slope. What matters is $v_{\mathrm{D}} < v_{\mathrm{max}}$. → l.3: "because the bands are linear with a velocity below that of the dark matter". l.154: "through a gap of tens of meV and bands slower than the dark matter".
- S3-2, l.3 against the Fig. 7.3 caption (l.66) [precision]. "Dark matter as light as \SI{10}{keV} can carry an electron across this gap" conflicts with the caption: "The \SI{10}{keV} curve stays just below the continuum; the threshold mass is \SI{10.5}{keV}". → "Dark matter of about \SI{10}{keV}". Same fix at l.154, "reach dark matter of 10 keV".
- S3-3, l.3 [1]. "In this section we obtain …; at the end we evaluate …" See C2.
- S3-4, l.7 [style]. "$\Delta_{\mathrm{D}}$ is the \emph{half-gap}." starts a sentence with a symbol. → "We write $\Delta_{\mathrm{D}}$ for this \emph{half-gap}."
- S3-5, l.14–16 [succinct background]. The proof that Kramers symmetry forces the Dirac form takes about 450 words of matrix algebra in the running text. → Move the uniqueness argument (from "Define $N_i = M_iM_1^{-1}$" through "$M = \sum_iv_i\kappa_i\sigma_i$") to \cref{app:D.22} as a new first subsection. Keep in the text the reason (Kramers doublets plus parity leave only the off-diagonal velocity block, which a basis choice brings to $\sum_i v_i\kappa_i\sigma_i$) and the keyresult.
- S3-6, l.34 [precision]. "why calculations and measurements disagree on its size: first-principles values range from 24 to \SI{35}{meV}" gives only calculations. → Either quote the measured gap, or write "why first-principles values disagree on its size: they range from 24 to \SI{35}{meV}".
- S3-7, l.40 [mismatch]. "How many states does a Dirac cone offer within an energy $\omega$ of its edge?" is answered with $\mathcal{N}_{\mathrm{D}}(E)$. → "How many states does a Dirac cone offer at energy $E$?"
- S3-8, l.61 [wrong picture]. "The edge is the energy of a pair at rest in the frame that moves with velocity $v_{\mathrm{D}}$" is wrong: a pair at rest has energy $2\Delta_{\mathrm{D}}$. → "The edge is the dispersion of a relativistic particle of mass $2\Delta_{\mathrm{D}}$ and momentum $q$, with $v_{\mathrm{D}}$ in place of the speed of light."
- S3-9, l.74 [clarity]. "In a material whose gap is tens of meV it is large" gives a reason that conflicts with the definition, which excludes the Dirac electrons. → State the source of the large background (remote interband transitions and, if included, the lattice), or drop "whose gap is tens of meV".
- S3-10, l.110, l.134 and l.151 [5]. The point that the background must exclude the Dirac part, or the Dirac term is counted twice, is made three times. → Keep it in the computational paragraph (l.134). At l.110 cut "A consistent set of parameters has $\varepsilon_{\mathrm{bg}}$ computed with the states inside $\Lambda_{\mathrm{D}}$ left out." At l.151 keep only the consequence, "already contain a Dirac term of this size".
- S3-11, l.114 [attribution]. The limitbox attributes the hard-cutoff formula to "\cite[Eq.~(2.7)]{hochberg2018detection}", which uses a subtraction (l.96). → "after~\cite[Eq.~(2.7)]{…}, with a hard cutoff". The box itself meets the limitbox rule: the formula is stated, the plot is against $v_{\mathrm{D}}q/\Delta_{\mathrm{D}}$ with the validity region shaded and the correction visible, and one sentence says what breaks down.
- S3-12, l.123 [comma splice]. "the electron gas screens a charge completely beyond $1/k_{\mathrm{TF}}$, a gapless Dirac material only reduces it" → "…beyond $1/k_{\mathrm{TF}}$, whereas a gapless Dirac material only reduces it …".
- S3-13, l.141 [19]. Three sentences reconcile the earlier parameter set and the $g_{\mathrm{deg}} = 4$ convention. → Reduce to one convention clause: "an earlier calculation~\cite[Table~1]{hochberg2018detection}, with faster velocities and smaller dielectric constants, gives nearly the same $\tilde\alpha = 0.20$ (quoted there as $0.80$, with four states per band)."
- S3-14, l.147 [device name]. "never in the gapless regime of the limit box" → "never in the gapless regime of \cref{fig:7-gapless-limit}".
- S3-15, l.151 [precision]. "with $\varepsilon \approx 55$ … reduced fifty-fold" → "about fifty-fold".
- S3-16, l.34 [cite style]. `\cite[Table~1]{geilhufe2020dirac}\cite[Table~1]{hochberg2018detection}` renders as two bracket groups. → "…~\cite[Table~1]{geilhufe2020dirac} and~\cite[Table~1]{hochberg2018detection}".
- S3-17, l.14–30 [editor]. $\sigma_i$ should be $\sigma^{\mathrm{d}}_i$ (C7), and $\alpha_i,\beta$ should be $\alpha_{\mathrm{D}},\beta_{\mathrm{D}}$ (l.18, 24, 30). Bare $\beta$ is inverse temperature. Open.

### 7.4
- S4-1, l.3 [C2, C7]. The roadmap sentence "We will compute …" is fine. Change `\cref{sec:3.3}` to `\cref{sec:1.3}` for 0.333 MeV.
- S4-2, l.9 [cite style]. `\cite{kohn1955theory}\cite[Chap.~4]{yu2010fundamentals}` → "…~\cite{kohn1955theory} and~\cite[Chap.~4]{yu2010fundamentals}".
- S4-3, l.37 [second reading]. The cleft sentence → R7.4a.
- S4-4, l.41 [13]. "It also lifts a degeneracy …" opens a paragraph with "It" pointing back to the previous paragraph. → "The central cell also lifts a degeneracy …".
- S4-5, l.48 [pairing]. "with a triplet and a doublet at 33.89 and \SI{32.58}{meV}" asks the reader to pair two lists. → "with the triplet $T_2$ at \SI{33.89}{meV} and the doublet $E$ at \SI{32.58}{meV}".
- S4-6, l.54 [idiom]. "because no other method holds the envelope" → "because no supercell is large enough to hold the envelope".
- S4-7, l.65 [terminology]. "the measured $1s$ triplet of phosphorus, $A_1$ at …, $T_2$ at … and $E$ at …" lists three levels, of which only $T_2$ is the triplet. → "the three measured $1s$ levels of phosphorus". Same line: "is the largest of the two intervalley terms" → "the larger of the two".
- S4-8, l.67–69 [symbol clash]. In the same worked example, $a$ is the lattice constant in "$a^3/8$" and the transverse radius in "$1/a = \SI{81}{eV}$" and "$qa \approx 0.42$". → Name the radii $r_\perp, r_\parallel$ (here and in D.23), and keep $a$ for the lattice constant.
- S4-9, l.90 [one job]. One paragraph covers the T center and the NV center. → Start a new paragraph at "The \emph{nitrogen--vacancy center} of diamond …".
- S4-10, l.74 [units]. "1326 nm", "637 nm" → `\SI{1326}{nm}`, `\SI{637}{nm}`.
- S4-11, l.113 [clarity]. "is … = 0.30 in $S_{\mathrm{HR}}$; the true factor lies between 1.47 and about 1.8" → "shifts $S_{\mathrm{HR}}$ by at most 0.30, so the true Huang–Rhys factor lies between 1.47 and about 1.8 …".
- S4-12, l.139 [first use]. "with $M = \SI{26.16}{GeV}$" leaves M undefined, and M is also the mass-weighting mass at l.76. → "with the silicon nuclear mass $M = \SI{26.16}{GeV}$".
- S4-13, l.50 [C9]. "the isolated-donor picture fails before the orbits touch" → add "(the Mott metal–insulator transition, \cref{sec:16.5})".
- S4-14, l.76 and l.83 [editor]. $\omega_0$ is reused (C.7 two-mode parameter in 7.1 l.114; effective mode here). $E_{\mathrm{d}}$ is also reused. Both are open per the editor note.

### Appendices
- D19-1, l.3 and l.7 [cross-ref]. "The result is \cref{eq:E.9-afm}" and "The Hamiltonian is \cref{eq:E.9-heis}" point to App. E for objects the main text defines. → Write "The Hamiltonian is \cref{eq:7.1-heis}" and "The result, \cref{eq:D.19-omega}, is used in \cref{sec:7.1} and \cref{app:E.9}".
- D20-1, l.41 [user rule: nothing left to the reader]. "as one checks by applying \cref{eq:D.20-gamma} to it." → Write the step: "applying $\gamma_{\vect{k}1}$ to the factor $u + v\,c^\dagger_{\vect{k}\uparrow}c^\dagger_{-\vect{k}\downarrow}$ gives $(uv - vu)\,c^\dagger_{-\vect{k}\downarrow} = 0$". Adjust the signs to the convention.
- D20-2, l.68 [13]. "the second form for weak coupling" → "the exponential form, valid for weak coupling, …".
- D20-3, l.97 [unclear]. "the operator of \cref{sec:7.1} at a single electron" → "\cref{eq:7.1-se} in second quantization".
- D20-4, l.93 and l.125 [C4].
- D21-1, l.94 and l.101 [editor; prose-visible]. Upright $\Gamma_{\boldsymbol{\eta}}$ and $\boldsymbol{\Gamma}_{\vect{j}}$ use the symbol now reserved for the zone center. Rename to $\mathsf{V}$ along with 7.2. Also l.101 writes $\mathbf{1}$ where 7.3 writes $\mathbb{1}$. Pick one.
- D21-2, l.70 and l.90 [abbrev.]. "this is an RPA", "adds the RPA" → "random-phase approximation", as in 7.2.
- D22-1, l.1 [title]. "RPA polarization of three-dimensional Dirac electrons" → "Polarization of Dirac electrons".
- D22-2, l.55 [clarity]. "only the combination $\ee^{-5/6}\Lambda_{\mathrm{D}}$ is defined unambiguously by a hard cutoff; a physical number requires matching …" → "A hard cutoff and a subtraction differ only in this constant. Either way, $\Lambda_{\mathrm{D}}$ is a model parameter fixed by matching to the computed band structure."
- D22-3, l.59 [18]. "The static long-wavelength limit, the gapless limit and the static gapless limit are used in \cref{sec:7.3}." → Delete it, and open with "At $q \to 0$ and $\omega = 0$ …".
- D22-4, l.7 [editor]. $\boldsymbol{\alpha}$ and $\beta$ should be $\alpha_{\mathrm{D}}$ and $\beta_{\mathrm{D}}$. Open.
- D23-1, l.60 [wrong term]. "The orbit is a prolate spheroid, flattened along the heavy axis": radii 24.3, 24.3 and 14.0 Å describe an **oblate** spheroid. → "an oblate spheroid".
- D23-2, l.64 [symbol]. The valley coefficients $\alpha_j$ sit beside the fine-structure $\alpha$ in $-\alpha/\varepsilon_0 r$. → $c_j$. The same applies to 7.4 l.41.
- D23-3, l.38 against 7.4 l.26 [5]. "brackets the answer without giving it" appears in both. Keep one.

## 4. Register calibration (2–3 passages per section)

**7.1.**
- (a) l.131, "Physically, a long-wavelength deviation on one sublattice drags the other along through the pair term …". Yes, Lin could have written this.
- (b) l.95, "For dark matter the quadratic dispersion matters." Yes.
- (c) l.199. No. → *Rewrite (R7.1):* use the S1-9 sentence.

**7.2.**
- (a) l.12, "The picture is one of timing." Yes.
- (b) l.156, "The culprit is the mean field." Yes.
- (c) l.31, "If one also replaces the frequency-dependent coupling …". No. → *Rewrite (R7.2c):* "If we go further and cut the frequency-dependent coupling off at about $\omega_{\mathrm{D}}$, the Eliashberg gap equation reduces to the BCS one derived below, with the effective coupling $\mathcal{N}_{\mathrm{F}}V_{\mathrm{BCS}} \simeq (\lambda_{\mathrm{ep}} - \mu^*_{\mathrm{C}})/(1 + \lambda_{\mathrm{ep}})$."

**7.3.**
- (a) l.70, "the velocity decides whether a cone can be reached at all, and the gap decides at which mass". Yes.
- (b) l.47, "halving the velocity multiplies the states by eight". Yes.
- (c) l.3, "because the bands are steep but not too steep". No. → *Rewrite (R7.3):* "Pairs are cheap in momentum too: the bands are linear, and slow enough, $v_{\mathrm{D}} < v_{\mathrm{max}}$, for a dark-matter particle to outrun them."

**7.4.**
- (a) l.135, "It loses energy to every atom it pushes." Yes.
- (b) l.37, "For them, effective-mass theory is as good as the hydrogen atom." Yes.
- (c) l.37, "It is the value of the static constant at liquid-helium temperature, where donor spectra are taken, that calculations of donor levels use …". No. → *Rewrite (R7.4a):* "This is the static constant at liquid-helium temperature, where donor spectra are taken, \SI{2.6}{\percent} below the room-temperature 11.7, and it is the value that calculations of donor levels use~\cite{faulkner1969higher,smith2017ab}."

## 5. Other checks

- **Titles.** All are short noun phrases. Exceptions are D.19 and D.22 (§1, D22-1). "Further target materials" is acceptable.
- **Captions.** Figs. 7.2–7.5 and the limit figure stand alone. Fig. 7.1 needs the energy unit (S1-11).
- **Cross-references.** All use \cref; no hard-coded numbers (the "Chap. 4" and "Sect. 1.1" occurrences are cite postnotes for external sources). Fix D19-1 and the 0.333 MeV attribution (C7).
- **Citations.** The style is biblatex numeric with equation-level postnotes, as required. Problems: the adjacent \cite pairs (S3-16, S4-2), S1-10 (pattern 20) and S3-11.
- **Standalone scrub.** No internal labels and no exercises or checkpoints. Pattern 19 items: C4, S1-2 and S3-13. Pattern 20: S1-10. "limit box" is a device name (S3-14). Source comment: C10.

## 6. Editor-notes items (prose-relevant status)

| Item | Status |
|---|---|
| α_D, β_D (7.3, D.22) | **Open**: s7-3 l.18, 24, 30; D-22 l.7. |
| σ^d_i for doublets (7.3) | **Open**, and now a prose contradiction with s7-2 l.170 (C7). |
| 7.1 NiO parameters | Fine for prose. |
| Si ε = 11.7; 11.4 for the p-level fits | Accepted as written. Note that 11.4 appears in three places, not once (caption l.33, l.37, l.61), consistently. The prose fix R7.4a is optional. |
| T-center S_HR inferred, stated as such | Yes: caption l.97 and WE l.113. |
| ω₀ and E_d reuse (7.4) | **Open** (S4-14). |
| Al T_c = 1.18 K | Consistent throughout 7.2 and the Summary. |
| \varGamma → \mathsf{V} (7.2, D.21) | **Open**. D.21 uses upright Γ, which is worse (D21-1). |
| 40 meV BCS cutoff as a modelling choice | Stated in WE 7.2 (l.228) and at l.161. Accepted. |
| Bergeron arXiv-only citation | Audit item, not prose. |
