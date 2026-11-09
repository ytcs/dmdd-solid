# Ch10 prose review (style, register, standalone)

Scope: tex/ch10/ch10.tex, s10-1 … s10-10, appD/D-29, D-30, read in full against STYLE.md, style-guide.md, prose-review.md and REGISTER.md; editor-notes items that concern prose at the end. Line numbers are per file. No tex edited.

## Verdicts

| Section | Verdict | Main reasons |
|---|---|---|
| Opening (ch10.tex) | REVISE | middle of the paragraph is a disguised section list |
| 10.1 | REVISE | title; count-teasers; q₀ undefined at first use; bare "transfer"; f-sum excess not said to be unexplained |
| 10.2 | REVISE | 1.11 eV used as the physical gap; banned research label "GS" in a symbol; IP rate not reconciled with 10.1; closing restates |
| 10.3 | PASS | minor: "This section derives" frame, a repeated sentence, a hard-coded source equation |
| 10.4 | REVISE | title; |ε|² = 770 vs 761; 2.4×10⁻³ vs 2.5×10⁻³; "book halo"; table vs text on screening of j_T; 330-word paragraph |
| 10.5 | PASS | stray comma, starred subsection, one caption item unexplained |
| 10.6 | REVISE | clause titles; "f-sum" typography; consistency aside; "acceptance test"; K̄ clash with 10.8 |
| 10.7 | REVISE | 761 vs 770; 77 K gap still vague (editor); undefined source notation in a limit box; Λ clash; tautological caption |
| 10.8 | REVISE | editor's two cuts not made; normalization bookkeeping; "core-hours"; bare Λ; 𝒯 overloaded |
| 10.9 | REVISE | title; solar-core temperature uncited (editor); hard-coded source equation numbers; four "truncation label" paragraphs |
| 10.10 | PASS | minor: "Home" column, "Until that library exists" |
| Summary | REVISE | two IP rates side by side with no reconciliation |
| App. D.29 | PASS | "f-sum" typography only |
| App. D.30 | PASS | its 2.5×10⁻³ is right; 10.4 must match it |

No section needs a REWRITE. The voice is consistent across the ten writers: "we" throughout, concrete openers, estimate before result, no exercises, no "you", no exclamation marks. The problems that run through the whole chapter are the register connectives (Sect. C below), count-teasers, and the formulaic "truncation label" paragraph that follows most limit boxes.

## A. Lint

| File | Hits | Assessment |
|---|---|---|
| ch10.tex | 0 | — |
| s10-1 | TITLE l.1; EQ-PUNCT l.44; LONG-SENT ×1 (caption) | title is real; EQ-PUNCT false (comma present before \end{aligned}) |
| s10-2 | LONG-SENT ×2 (captions) | caption sentences (l.30, l.119); no action |
| s10-3 | LONG-SENT ×3 (table, caption, derivation run) | false positives (table and display math are joined by the linter) |
| s10-4 | TITLE l.1; LONG-SENT ×2 (caption) | title is real |
| s10-5 | EQ-PUNCT l.38; LONG-SENT ×5 | EQ-PUNCT false; the caption of fig:10-xq (l.29) is the only real long run |
| s10-6 | EQ-PUNCT l.68, l.115; LONG-SENT ×2 | false: l.115 continues "is the relative shift", which needs no punctuation |
| s10-7 | LONG-SENT ×4 | caption and keyresult joins; no action |
| s10-8 | LONG-SENT ×4 | caption joins; no action |
| s10-9 | TITLE l.1; EQ-PUNCT l.99, 155, 169; LONG-SENT ×4 | title is real; EQ-PUNCT false |
| s10-10 | EQ-PUNCT l.69; LONG-SENT ×5 (table rows) | false |
| D-29 | EQ-PUNCT l.30, 46, 53; LONG-SENT ×1 | false |
| D-30 | EQ-PUNCT l.29, 53 | false |

There are no blocking hits. Equation punctuation checked by hand: every display in the chapter is punctuated as part of its sentence. The linter missed one standalone-scrub hit: **s10-2 l.104, 112 `\mathcal{G}_{\mathrm{GS}}`**. NOTATION entry 51 lists "GS" as a banned research label for the electron-following sector, and BANNED-TERMS only catches "GS sector". Fix: rename it, for example `\mathcal{G}_{\mathrm{ef}}` ("electron-following"), here, in E.16 (`eq:E.16-step`) and in NOTATION, and extend BANNED-TERMS with `\\mathrm\{GS\}`.

## B. Chapter as a whole

**Opening (ch10.tex l.2).** The first five sentences do the job well: the signal, the 1.17 eV gap, single-electron readout, 1 MeV → 3.5 eV, and the connection to Chaps. 8–9. From "The band structure alone gives the first answer…" to "…each case asks the crystal a different question", however, each sentence maps onto one section (10.1, 10.2/10.5, 10.4, 10.7/10.9). That is the section list STYLE forbids, in prose form. Fix: replace those four sentences with one motivating sentence, then keep the existing closer. For example: "The answer turns on what the band structure leaves out: other electrons that screen the potential and bind the pair, couplings to spin and current rather than number, and particles that are absorbed, split or fast rather than slow and elastic." Keep "Throughout, the nuclei stay clamped…" and the last sentence.

**Summary (s10-10 l.98–118).** It is in connected prose, one paragraph per section, and ends on a pointer to Chap. 11, which is good. Problem: l.100 gives the IP rate as 1.60×10⁵ and l.102 gives it as 1.36×10⁵, two sentences apart, with no explanation. Fix: add to l.102 "(two independent-particle tabulations differ by 18 %, Sect. 10.10)". l.112 "761" must match whatever 10.4 is corrected to (below).

**Redundancy across sections.**
- The identity "IP structure factor = −2 Im of the bubble head" is derived in 10.1 l.21 and again in 10.2 l.19. Fix: in 10.2, write "Since $S^{\mathrm{IP}} = (2q^2/e^2)\varepsilon_2^{\mathrm{IP}}$ (\cref{sec:10.1}, \cref{eq:4.6-R0}), the prefactor …" and drop the re-derivation.
- The screening ratio "2.3 / 3.7" appears at 10.2 l.3, l.38, l.55, l.125, and again in 10.4 l.43. The closing paragraph of 10.2 (l.125) is a summary of the section, which is pattern 5. Fix: cut l.125 to its last two sentences ("The sum rules cap … in the phonon band. \Cref{sec:10.3} takes …").
- Triplet excitons and the exchange splitting are stated in 10.4 l.49 ("a fraction of order 10⁻³ of the binding…") before 10.5 l.117 derives them. Fix: in 10.4, after "…the attraction between the electron and the hole." write only "\Cref{sec:10.5-triplet} computes what this does to the triplet rows."
- The local fields at large q appear in 10.1 l.59, 10.2 l.53 and 10.10 l.11. 10.10 reconciles them, which is correct. Leave as is.
- 10.3 l.117 says twice in four sentences that a third body can take the momentum ("…or when a third body takes the momentum" and "A third body can take the momentum."). Cut the second.

**Seams.** 10.1→10.2, 10.2→10.3, 10.3→10.4, 10.7→10.8 and 10.9→10.10 hand over explicitly and well. The weak joins:
- 10.4→10.5: 10.4 ends on velocity couplings, and 10.5 opens on the density exciton with no turn. Fix: add a clause to the end of the 10.5 opener: "…and for the density coupling of \cref{sec:10.2} the first correction beyond the random-phase rung is the electron–hole attraction."
- 10.6→10.7: 10.6 ends on an open item about Ge spin–orbit ("\Cref{app:E.15} specifies that calculation."), and 10.7 switches from scattering to absorption with no bridge. Fix: end 10.6 with one sentence of consequence, for example "Up to these open items, the response of every shell that halo dark matter scatters off is in hand; a particle that is absorbed asks for it at a single point, $\vect{q} \simeq 0$." This also gives 10.7's opener its setup.
- 10.8→10.9: 10.8 ends on compute budgets (see 10.8 below). It reads better once that sentence is cut.

**"Open problems" subsections** are inconsistent: starred in 10.5 (l.121), numbered and labelled in 10.6, 10.8, 10.9 and 10.10, absent elsewhere. Fix: make them all `\subsection{Open problems}\label{sec:10.N-open}`. Use the same form in 10.2 for the starred `\subsection*{A lattice that relaxes}` (l.93).

**Truncation-label paragraphs.** After most limit boxes a paragraph recites the chain and the label: 10.1 l.59 "The chain from the master formula is short…"; 10.2 l.112; 10.3 l.38; 10.9 l.79, 142, 195, 228. Together they read like the old Source/Chain/Validity procedure list moved out of the boxes. Each is fine alone, but the repetition is a voice problem. Fix: keep one clause of label per box, folded into a physics sentence. For example, 10.9 l.228 "The formula sits outside the truncation label, since no response of the target enters it." becomes "No response of the target enters the vacuum rate; the medium acts only through $\varepsilon^{\mathrm{T}}$ at $\mathcal{Q} = \omega n_r$…". 10.1 l.59: delete "The chain from the master formula is short." and "but the ratios are what the box needs", which is meta talk about the box.

**Process artifacts (pattern 19).** "acceptance test" appears at 10.6 l.129, l.133 and 10.8 l.84; "at about 10² core-hours" at 10.8 l.176; "Until that library exists" at 10.10 l.94; "the response library … computes it" at 10.4 l.111. These read as a project plan. Fix: say what the appendix calculation checks, not how it is accepted or budgeted. For example, 10.6 l.129 "the acceptance test of the four-component response in \cref{app:E.15} compares with the shifted value" becomes "a four-component response (\cref{app:E.15}) should be checked against the shifted value". 10.8 l.176: delete ", at about $10^2$ core-hours". 10.10 l.94 "Until that library exists" becomes "Until these rows are computed".

**Count-teasers (pattern 18).** 10.1 l.23 "Three properties of \cref{eq:10.1-S0} carry over from \cref{chap:3}. First, the threshold." Rewrite: "As in \cref{chap:3}, $S^0$ vanishes below $E_{\mathrm{min}}(\vect{q})$ …", and open the next items with "Its total weight is fixed by closure …" and "Its energy-weighted sum …". Also: 10.1 l.100 "Three parameters control it. … A fourth matters at large $q$."; 10.2 l.47 "The rate ratio of 2.3 is set by three things that a pointwise factor leaves out."; 10.6 l.43 "Two approximations of the model need checking."; 10.6 l.81 "The separation fails in four places…"; 10.10 l.94 "Four calculations would remove most rows"; 10.10 l.96 "Three open items are not nuisances…". Fix each by naming the members in the sentence. For example, 10.6 l.43: "Two features of the model need checking, the non-orthogonality of plane-wave final states and the missing Coulomb pull of the ion."

## C. Register (REGISTER.md)

Rates per 10k words (39.5k words of prose after stripping math and macros; REGISTER's L value in brackets): "only" 30 [11]; "gives" 19 [7]; "so" 20 [11]; "therefore" 8.9 [2.9]; "of order" 9.6 [0]; "about" 21 [5]; "however" 1.0 [8.0]; "typical/typically" 0 [15.3]; "we can" 0 [13.6]; "we will" 2.8 [12.6]; "for example/instance" 0 [9.5]; "of course" 0 [3.6]; "note that" 0.3 [6.1]; "as a result" 0 [2.2]. Clean: no "i.e.", "e.g.", "respectively", "thereby", "whereby", "in order to", "we call", "let's", "it is easy to see" or "one finds".

So the chapter has the book's known airlessness: flat assertions joined by "so", "gives" and "only", and almost none of the models' "however", "typical", "we can" or "for example". Writers should, on revision: replace "of order" with "∼" or "typical" in running prose (10.4 l.49, 10.5 l.117, 10.7 l.15, 10.9 l.176 are examples); turn "A gives B" into "A is B" or "A leads to B" in about half of the cases; and add one "however" or "but" and one "we can/we see" per 1,000 words where a real contrast or step is present. The field terms are good: heavy and light mediator, momentum transfer, kinematically allowed, reach, threshold, background-free reach, screening, loss function, Landau damping, f-sum rule, phonon-assisted, Migdal effect, zero-point. The exception is bare "transfer" (REGISTER term 6) at 10.1 l.74 "the transfer resolves the bond", 10.1 l.76 "moves against the transfer", 10.6 l.14 "A transfer $q$ deposits", and 10.6 l.54 "A transfer $q$ with deposit $\omega$". Write "momentum transfer" each time. (10.7 l.32/46 and 10.9 l.222/225 use "transfer" in a different sense and are fine.)

**Calibration (2–3 passages per section; "yes" means Lin, or Kahn and Lin, could have written it).**

| § | Passage | Verdict | One-sentence rewrite where "no" |
|---|---|---|---|
| 10.1 | l.3 "…can transfer up to 53 keV of momentum and deposit up to 35 eV" | yes | — |
| 10.1 | l.76 "That is why … falls as $q^{-5}$" | yes | — |
| 10.1 | l.23 "Three properties … First, the threshold." | no | "As in Chap. 3, $S^0$ vanishes below $E_{\mathrm{min}}(\vect q)$, so a mass is kinematically allowed only where \cref{eq:3.3-allowed} holds." |
| 10.2 | l.3 "Yet the screened rate … is only 2.3 times smaller" | yes | — |
| 10.2 | l.81 "The upper limit, … is not a general theorem. It holds in the random-phase approximation…" | no (G's syntax) | "The upper limit is the catch: $\varepsilon^{-1}(\vect q,0) \ge 0$ is not guaranteed in general, although we can show that it holds in the random-phase approximation for any insulator." |
| 10.2 | l.97 "The size follows from the acoustic peak." | yes | — |
| 10.3 | l.3 "A model with one parameter … lands within seven percent of the crystal." | yes | — |
| 10.3 | l.38 "On the truncation label of Sect. 8.5 the gas rate sits at 𝒳 = RPA…" | no | "Compared to silicon, the gas is the random-phase approximation for a homogeneous medium; the gap, the local fields and the bound momentum distribution are what the crystal adds." |
| 10.3 | l.107 "The suppression is not a power of a small ratio." | yes | — |
| 10.4 | l.84 "The two terms are easy to estimate… We expect the electron term to exceed … by about 20 to 30" | yes | — |
| 10.4 | l.3 "…Which responses…? Which of them…? And how large…?" | no | "Every coupling beyond the density needs new responses of the crystal, screened in its own way, and an interference term that nobody has computed; we will find that a single ratio controls how much that term can matter." |
| 10.5 | l.47 "How much weight the lines take is a short calculation." | yes | — |
| 10.5 | l.86 "A resonant-only evaluation is harmless for heavy mediators … and wrong by a factor of two for light mediators" | yes | — |
| 10.6 | l.3 "A germanium atom has 32 electrons, and the band structure … follows four of them." | yes | — |
| 10.6 | l.108 "The same nonrelativistic atomic calculation gives K̄ = 561.3 eV for silicon, against the Hartree–Fock value of Sect. 4.3." | no | delete (consistency check addressed to a reviewer, pattern 19) |
| 10.7 | l.37 "An expansion in $\Pi_{\mathrm{em}}/m_\phi^2$ is useless here" | yes | — |
| 10.7 | l.82 "a dark photon in disguise" | yes | — |
| 10.8 | l.62 "They are small." | yes | — |
| 10.8 | l.30 "Their momentum distribution … ξ = 44.8 … ξ = 8π^{3/2}/0.99415 = 44.81 makes this ρ_χ/2m_φ, as here." | no | "With their normalization of the Gaussian, the rates of Ref. [bauer] equal ours at the same density, and their $\rho_\chi = \SI{0.39}{GeV.cm^{-3}}$ makes them larger by $(0.39/0.3)^2 = 1.69$." |
| 10.9 | l.129 "The transverse row … holds a surprise in a semiconductor." | yes | — |
| 10.9 | l.142 "On the truncation label the published row departs from the master formula on the dark-matter side…" | no | "The published row errs on the dark-matter side, not in the target: …" |
| 10.10 | l.3 "…makes 5.2×10⁴ … 2.5×10⁴ … 1.85×10⁴ … The last one is the best computed so far, but it is not the rate." | yes | — |
| 10.10 | l.89 "That step has been taken; what remains is the one after it" | yes | — |

## D. Issues by section (location → problem → fix)

**10.1**
- l.1 "Band-to-band scattering and the crystal form factor": title is not a short noun phrase. Use "The crystal form factor".
- l.54 (caption) and l.59: $q_0$ is first used here but defined only in 10.6 l.52. Add "$q_0 = \alpha m_e = \SI{3.73}{keV}$" at the first text use, l.59.
- l.23 "the f-sum value" and l.61 "The f-sum rule catches it": italic $f$ as in 10.2–10.5. The same goes for 10.6 l.81, 106 (title), 108, 129, 133 and D-29 l.25, 70.
- l.65 "1.11 eV, the room-temperature value": 10.7 l.44 gives the 300 K gap as 1.12 eV. Write "close to the room-temperature gap".
- l.72: editor note. After "…without changing its weight", add "which accounts for about ten percent of the excess; the rest has no identified cause (\cref{sec:10.10-rungs})."

**10.2**
- l.7 "An electron–hole pair in silicon costs at least $\Eg = \SI{1.11}{eV}$, seventeen times the top of the phonon band": this is a physical statement, so by the Ch2/editor ruling it needs 1.17 eV. Write "at least \SI{1.17}{eV}, eighteen times the top of the phonon band".
- l.86 (WE) "the threshold $\omega_{\mathrm{th}} = \Eg$ of a charge detector": here Eg is the tables' 1.11 eV. Write "the threshold $\omega_{\mathrm{th}} = \SI{1.11}{eV}$, the gap of the tables".
- l.38: the IP total 1.36×10⁵ sits beside 10.1's 1.60×10⁵ with no comment. After the first sentence of the numbers, add "(the tabulation of \cref{sec:10.1} gives 1.60×10⁵; \cref{sec:10.10-rungs} traces the difference)".
- l.93 `\subsection*{A lattice that relaxes}`: starred, and a clause. Use `\subsection{Relaxing lattice}` with a label.
- l.104, 112: rename $\mathcal{G}_{\mathrm{GS}}$ (banned label, see A).
- l.110 "is $c_1^{(e)}\nd_e$ here": $c_1^{(e)}$ is not defined in the chapter. Add "with $c_1^{(e)}$ the electron coupling of \cref{eq:8.1-…}" or drop the clause.
- l.112: "$\mathcal{K}$ = one-phonon" is label bookkeeping in prose. Fold it into a sentence: "The lattice term is harmonic and adiabatic, with one phonon in the final state."
- l.125: closing restatement (see B).

**10.3**
- l.3 "This section derives the electron-gas rate and finds…": a "this section" frame. Write "We derive the electron-gas rate, find where it agrees with silicon and why, and then isolate the plasmon pole …".
- l.78 "their Eq.~(14)": hard-coded. Write `\cite[Eq.~(14)]{kurinsky2020dark}` in the book's normalization.
- l.117: repeated sentence (see B).

**10.4**
- l.1 "Spin, current and velocity couplings in the medium": write "Spin and current couplings".
- l.3: triad of rhetorical questions and an ordinal outline ("the first … the second … the third"). Rewrite as in the calibration table.
- l.27 (table) "$j_{\mathrm{T}}$ through local fields only" against l.45 "The transverse current is, to this accuracy, an unscreened row with a local-field correction of order ten percent": the two descriptions point opposite ways. Use one phrase in both places, "unscreened at the head; local fields only, ∼10 %". Editor PRIORITY (a), the class disagreement with Table 8.3, is a derivation matter; once it is adjudicated, use the same wording here, in the caption and in 8.4.
- l.35 "Small nonzero values of $\overline W_5$ in a calculation measure its numerical noise.": too confident while editor (b) is unverified. Write "…so that nonzero values in a calculation, such as those of Ref. [catena2021crystal], have to come from numerics or from a term outside these assumptions (\cref{app:D.30})" until the derivation review rules.
- l.56 "At \SI{3}{eV} silicon has $|\varepsilon|^2 = 770$": 10.7 l.23 and the Summary give 761. Use one value.
- l.58: a 330-word paragraph that surveys four published treatments. Split before "EXCEED-DM makes the opposite choice" and before "The sum-rule bounds of \cref{sec:10.2}".
- l.65 (caption) "book halo": write "the standard halo of \cref{sec:1.2}".
- l.95 "below \SI{10}{\percent} only for $r < 2.4\times10^{-3}$": solving 2√r/(1+r) = 0.1 gives 2.51×10⁻³, which D-30 l.101 has. Write 2.5×10⁻³. The caption's 2.4×10⁻³ (l.65) uses a different criterion, (√r+1)² ≤ 1.1, and is right.
- l.111 "That ratio is the second open quantity": the ordinal has no anchor (the first is never named). Write "That ratio is open, and with it the factor …"; also "the response library of \cref{app:E.16} computes it" becomes "\cref{app:E.16} sets out its calculation".

**10.5**
- l.47 "The free continuum without the Fermi factor, holds": delete the comma.
- l.64: $|\varGamma(2 + \ii\xi_{\mathrm{C}})|$ uses the rate glyph for the gamma function. Check NOTATION for the gamma-function symbol (upright Γ is the zone center).
- l.98 `\cites[…]{taufertshofer2026excitonic}` with one key: use `\cite`.
- l.102 (caption) "Dash-dotted: $|\vect{q}| = \SI{0.7}{\angstrom^{-1}}$": add "(\SI{1.39}{keV}, the momentum of the worked numbers in the text)" so that the caption stands alone.
- l.121: starred subsection (see B).
- l.123: Open problems is one 330-word paragraph with a derivation (Huang–Rhys) inside it. Split at "So is the response of crystals in which the exciton is not large."

**10.6**
- l.63 "When core and valence responses separate": a clause title. Write "Separation of core and valence".
- l.45 (WE title) "The germanium 3d onset in q": write `$3d$` and `$q$` in math.
- l.108: the 561.3 eV aside (pattern 19; see calibration). Also, $\bar K$ here is NOTATION's mean kinetic energy, and 10.8 l.30–32 reuses $\bar K$ for the pair's kinetic energy. Rename the 10.8 symbol (for example $\bar K_{\mathrm{pair}}$, or $\langle K\rangle$) and propose it in NOTATION.
- l.119 "is the relative shift of $\mathscr{M}^1_{ee}$": the symbol is not defined in the chapter. Write "of the first moment $\mathscr{M}^1_{ee}$ of \cref{eq:4.3-fsum}".
- l.129, 133: "acceptance test" (see B).
- l.135: the section ends on an open item. Add a closing consequence (see Seams).

**10.7**
- l.23: 761 vs 770 (see 10.4).
- l.32 (caption) "The model curves are models, not predictions for silicon.": tautology. Write "The model curves show the size and shape of the kinetic and spin responses, not predictions for silicon."
- l.46 "the gap is a few meV smaller than at millikelvin temperatures": the editor asked for a number with a source, or a deletion. Write "the gap is \SI{1.166}{eV} against \SI{1.169}{eV}~\cite[…]{…}", or delete the clause.
- l.130 "an s state": write "an $s$ state", as in 10.5.
- l.133 (box) "$\varGamma \simeq -(g_{\phi ee}^2/m_\phi)\Imag\Pi_{\bar v^2\bar v^2}$ … $\op\psi^\dagger\overleftrightarrow{\nabla}^2\op\psi$": source notation that the book never defines, so the reader has to open the paper (pattern 20). Write the box formula in book symbols, $\varGamma = -(g_{\phi ee}^2/m_\phi m_e^2)\Imag R_{\mathcal{T}\mathcal{T}}$, and keep the citation for credit.
- l.137 (caption) "up to an excitation energy $\Lambda$": bare Λ is the final-state class (NOTATION 56). Use $E_{\mathrm{cut}}$ or $\Lambda_E$.

**10.8**
- l.30: normalization bookkeeping for Bauer et al. (ξ, 0.99415, 44.81), pattern 19. Compress to one clause (see calibration).
- l.22, l.62 "for a new-physics scale $\Lambda$", "at a scale $\Lambda \approx \SI{0.25}{GeV}$": bare Λ is reserved. Use $\Lambda_{\mathrm{NP}}$ or $\Lambda_\phi$ (propose in NOTATION).
- l.9 $\mathcal{T}^{(2)}_{ab}$ and l.92 $\mathcal{T}^{\mathrm{C}}$: script T is the kinetic-energy row $\mathcal{T}_e$ in the same section (l.39–41). Use $\mathsf{T}^{(2)}$ or $\hat t^{(2)}$ for the transition operator.
- l.71 `\Cref{lim:10.8a}`: the `lim:` prefix is not in the STYLE label list. Either add it to STYLE or cite the figure, `\cref{fig:10-pair-limit}`. The same applies to the labels in 10.9.
- l.84: "\Cref{app:E.26} specifies them, with the reduction to single absorption at $2m_\phi$ as the acceptance test." becomes "…and the reduction to single absorption at $2m_\phi$ is their check."
- l.86: the real-field pair-absorption paragraph. The editor asked for it to be cut. Cut it, keeping at most its last sentence on two-photon decay as a clause in l.84.
- l.134 "A detector much smaller than that records only $\omega_{\mathrm{C}}$, … depends on its geometry~\cite{…}": the editor asked for this cut. Delete it; Chap. 18/21 own detector geometry.
- l.171 "too large by a factor between 2 and 1 at every mass": write "too large by a factor that falls from 2 at small mass to 1 well above $m_e$".
- l.176 "at about $10^2$ core-hours": delete (pattern 19).

**10.9**
- l.1 "Inelastic, exothermic, boosted and fermionic dark matter": a list title. Write "Inelastic and relativistic dark matter", or "Modified kinematics".
- l.85 "at about $1.5\times10^7$\,K": the editor asks for a source. Add `~\cite{bahcall…}` (standard solar model).
- l.166 "That paper's general Eq.~(7) … in its Eq.~(8)": hard-coded source numbers. Write `\cite[Eq.~(7)]{dror2021absorption}` and `\cite[Eq.~(8)]{dror2021absorption}`.
- l.79, 142, 195, 228: the truncation-label paragraphs (see B). l.195 "The box sits at $\mathcal{X}$ = independent particles for an atom, with the vector-operator tensor taken from free kinematics." becomes "The box treats the atom as independent electrons and takes the vector tensor from free kinematics."
- l.234: the closing paragraph restates the section's four cases. Keep its last two sentences.

**10.10**
- l.32 (table header) "Home": write "Section".
- l.94 "Until that library exists": see B.

**App. D.29 / D.30**
- D-29 l.25, 70 "f-sum": write $f$-sum.
- D-30 is consistent with 10.4 apart from 2.5×10⁻³ (fixed in 10.4).

## E. Standalone scrub, citations, cross-references, captions, user rules

- Banned terms: none found by lint. "GS" was found by hand (see A). There are no exercises, checkpoints, "left to the reader" or "you". Nothing is left undone: every step points to App. D or E.
- Citation style: numeric throughout, with equation-specific `\cite[Eq.~(n)]{…}`. Exceptions: the hard-coded "Eq. (n)" at 10.3 l.78 and 10.9 l.166, and the single-key `\cites` at 10.5 l.98. Citations attribute rather than carry content, with one exception: the 10.7 l.133 box (above).
- Cross-references: all through \cref, with no hard-coded section or equation numbers of the book. The `lim:` labels need a STYLE entry.
- Captions stand alone almost everywhere and state units, parameters and what is shaded. Exceptions: 10.5 l.102 (the dash-dotted line), 10.4 l.65 ("book halo") and 10.7 l.32 (the tautology).
- Limit boxes all have a formula with a one-line source, a comparison plot and one sentence on the breakdown, with no procedure list. 10.1, 10.2a and 10.8b say "Nothing is shaded" with a reason, which is acceptable.
- The same empirical-pseudopotential model is anchored three ways: `we:8-rung` (10.1), `sec:4.6` (10.7, 10.8) and `\cite{cohen1966band}` (10.4 caption, 10.5 caption). Pick one anchor (`we:8-rung`) and cite Cohen–Bergstresser there.
- Section titles: three fail the noun-phrase rule (10.1, 10.4, 10.9). Subsections: "Which rows are screened" (10.4 l.39) becomes "Screening by row"; "What a plasmon decays into" (10.3 l.119) becomes "Plasmon decay"; "A lattice that relaxes" and "When core and valence responses separate" are covered above. Several worked-example titles exceed five words ("In-medium suppression of dark-photon absorption in silicon at 10 eV", "Line positions of exothermic dark matter with Δχ = −10 eV in silicon"). Shorten them to "Dark-photon absorption at 10 eV" and "Exothermic lines in silicon".

## F. Editor-notes items that concern prose

| Item | Status in text | Action |
|---|---|---|
| Gap 1.17 physical / 1.11 tables | opening, 10.1, 10.3, 10.9, 10.10 comply | 10.2 l.7 and l.86 do not (D, 10.2) |
| 10.2 acoustic peak labelled as a model | done (caption l.30, box sentence) | — |
| 10.2 / 10.1 local fields at large q → 10.10 | done (10.10 l.11, table row) | — |
| 10.1 WE rate vs 10.2 IP rate | reconciled only in 10.10 l.13 | add pointers in 10.2 l.38 and the Summary |
| 10.1 f-sum excess partly unexplained | said in 10.10 l.13, not in 10.1 | add a clause at 10.1 l.72 |
| 10.3 q_c = 2.60 book value, 2.24 quadratic | done (l.72); no "often quoted" | — |
| 10.3 plasmon branching → 10.10 | done (table row) | — |
| 10.4 title | not done | "Spin and current couplings" |
| 10.4 (a) screening class vs Table 8.3; (b) W̄₅ | derivation; prose impact at l.27/45 and l.35 | soften l.35 until it is verified |
| 10.5 coupling-block ~10 % → 10.10 | done | — |
| 10.7 77 K gap shift number + source | not done (l.46 "a few meV") | number with citation, or delete |
| 10.7 scalar 16–18 eV → 10.10 | done | — |
| 10.8 cut real-field paragraph and detector-geometry sentence | not done (l.86, l.134) | cut both |
| 10.8 nuisance candidates (shells, axial pair with SOC) | done (table rows) | — |
| 10.9 solar-core temperature source | not done (l.85) | cite the standard solar model |
| 10.9 (A.18)–(A.21) citation | done (l.166, box l.185; essig2016direct = 1509.01598) | — |
