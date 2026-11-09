# Chapter 2 prose review (style and prose, isolated)

Scope: tex/ch02/ch02.tex, s2-1.tex to s2-5.tex (with the Summary), tex/appA/A-1.tex to A-9.tex (+ appA.tex), tex/appD/D-2.tex,
D-3.tex. Checked against STYLE.md, style-guide.md, prose-review.md and REGISTER.md. Tex not edited, nothing committed.
Locations are `file:line` in the source. PASS needs at most 3 minor hits per 1,000 words. **B** marks a blocking hit (standalone
scrub, number or symbol inconsistency, an unapplied REGISTER rewrite, a pattern-19 process artifact), which forces REVISE.

## 1. Lint (lint.py --banned BANNED-TERMS.txt)
| file | hits | note |
|---|---|---|
| ch02.tex, A-2 to A-9 | 0 | |
| s2-1 | 1 LONG-SENT | false positive: detex joins a sentence across a display |
| s2-2 | 2 LONG-SENT | false positives: figure caption and limitbox merged by detex |
| s2-3 | 1 EQ-PUNCT (:33), 6 LONG-SENT | EQ-PUNCT false positive: the full stop sits inside `aligned`, before `\end{aligned}`. LONG-SENT: table caption and cells (:124), displays merged |
| s2-4 | 1 LONG-SENT | false positive (display merged) |
| s2-5 | 5 LONG-SENT | false positives (displays and the fig:2-twolevel caption merged) |
| A-1 | 1 LONG-SENT | false positive: tab:A-conversions caption plus cells |
| D-2 | 1 LONG-SENT | false positive (display merged) |
| D-3 | 1 EQ-PUNCT (:14) | false positive: full stop inside `aligned` |
No banned term fires. Lint gaps: the regex set misses the process comments `% Sections are \input here as they are accepted`
(ch02.tex:5, appA.tex:2, appD.tex:2). Add `(?i)as they are accepted` (comments included). The EQ-PUNCT check should accept a
full stop placed just before `\end{aligned}`.

## 2. Verdicts
| section | words (prose) | minor hits | PASS allowance | blocking | verdict |
|---|---|---|---|---|---|
| 2.1 Fermi's golden rule | 2,800 | 11 | 8 | 2 | REVISE |
| 2.2 Born approximation and form factors | 4,850 | 16 | 15 | 3 | REVISE |
| 2.3 Second quantization | 4,350 | 13 | 13 | 2 | REVISE |
| 2.4 Second-order processes | 5,050 | 12 | 15 | 2 | REVISE (light) |
| 2.5 Thermal states and detailed balance (+ Summary) | 2,900 | 7 | 9 | 2 | REVISE (light) |
| App. A (A.1 to A.9) | 6,350 | 14 | 19 | 9 | REVISE |
| App. D.2 | 1,150 | 1 | 3 | 0 | PASS |
| App. D.3 | 1,000 | 1 | 3 | 1 | REVISE (one-line fix) |
| Chapter level | n/a | n/a | n/a | 2 (scrub comment, summary vs 2.4) | REVISE |
No section needs REWRITE. Every section opens on concrete content except 2.1 (R9 not applied), and the voice problems are local.

## 3. Voice consistency across the five writers
All five use "we", never "I" or "you", use American spelling, and use no contractions, "i.e.", "e.g.", "thereby", "whereby",
"in order to" or "respectively" pairings. No ASCII quotes and no exclamation marks. Counts per 10k words (REGISTER Sect. 4 targets):
| | so (L 11) | gives (L 7) | however (L 8) | we will/can/see (L 29) | since (L 14) | bare "transfer" |
|---|---|---|---|---|---|---|
| 2.1 | 50 | 46 | 0 | 0 | 7 | 0 |
| 2.2 | 19 | 21 | 0 | 2 | 10 | 16 |
| 2.3 | 62 | 53 | 0 | 0 | 7 | 0 |
| 2.4 | 10 | 8 | 2 | 2 | 14 | 0 |
| 2.5 | 7 | 14 | 7 | 3 | 21 | 0 |
These are differences between writers, not a shared tic. 2.4 and 2.5 are close to the models: there are reasons in "since"
clauses, a "however" and "of course" (2.5:144), and picture sentences such as "Nothing in nature diverges here" (2.4:94). 2.1
and 2.3 write the flat-assertion register that REGISTER Sect. 1 diagnoses, chains of "so"/"gives"/"therefore", and have no
connective for contrast. 2.2 is in between, but writes bare "transfer(s)" for q eight times. Paragraph length also differs:
2.1 and 2.2 run to about 330 words (2.1:73, 2.2:77), while 2.4 and 2.5 split at about 150. Shared phrase tics across writers:
"the other / some $10^{26}$ electrons" ×5 (ch02.tex:3, 2.3:3, 2.3:117, 2.4:90, 2.5:155) and "anticipated in \cref…" ×5
(2.2:59, 2.3:74, 2.5:39, 2.5:102; "promised" 2.2:3).

## 4. Issues by section (location | pattern | quoted text | fix)

### 2.1 (REVISE)
- s2-1:3 | B #18, REGISTER R9 unapplied | "This section derives that rate, Fermi's golden rule, states the window, and fixes the normalization of states in which every later rate is written." | Use R9: "To see how a rate emerges, and when the idea stops making sense, we derive Fermi's golden rule; along the way we fix the normalization of states that every later rate uses."
- s2-1:68 | B REGISTER R10 unapplied (stacked validity) | "The step is valid when $t$ is long compared with ..., short compared with ..., and short enough for first order to hold." | Use R10: "The catch is that $t$ has to sit in a window. It must be long compared with ..., so that energy is resolved; short compared with ..., so that the levels still look continuous; and short enough that the initial state is barely depleted."
- s2-1:35 | #17 | "up to a relative correction of order $1/t$ divided by the energy range over which $g$ varies" | "with a relative error $\sim 1/(t\,\delta E_g)$, where $\delta E_g$ is the range over which $g$ varies".
- s2-1:40 | REGISTER tic | "...is therefore independent of $t$ in the limit, which is what a rate means." (third "therefore" in 12 lines) | "...is independent of $t$ in the limit: that is what we mean by a rate."
- s2-1:48 | paragraph job | units, energy resolution and switch-on in one paragraph | Split before "The sudden switch-on at $t = 0$".
- s2-1:73 | paragraph job (about 330 words) | the DM continuum, the volume bound, the window, Wigner–Weisskopf and the DM crossing in one block | Split before "The upper bound $2\pi\mathcal{D}_f$" and before "At times beyond $1/\Gamma_i$".
- s2-1:92 | paragraph job / redundancy with 2.3:74 | "matrix elements proportional to $\sqrt{n}$ and $\sqrt{n + 1}$ ... The extra $1$ is spontaneous emission" | Split before "For a classical field". Keep the $\sqrt{n}$, $\sqrt{n+1}$ statement here and let 2.3:74 point back with one clause.
- s2-1:113 | #13 | "This is the breakdown time: the linear law holds for $\Gamma t \lesssim 0.2$." | "First order therefore breaks down at $\Gamma t \approx 0.2$."
- s2-1:131–145 | "so" ×6 in two paragraphs | "so its flux is", "so for any function", "so" ... | Replace two with "since"/"because", and add one "we can" or "we see" (for example "We see that the rate is proportional to $1/V$").
- s2-1:147–151 | user rule (succinct background) | the relativistic-normalization paragraph (about 260 words) | Advisory: keep the dictionary $|\mathcal{M}|^2 = 16m_\chi^2m_e^2|\tilde V|^2$ and the reason for box normalization, and cut the $\op{T}$-matrix detour to one clause (A.9 restates it).
- s2-1:118 | citation (weight) | "~\cite[Eqs.~(A1) and (A2)]{lin2019tasi}" for the textbook sum-to-integral rule | Acceptable, but optional: the rule needs no attribution.
- Calibration. (a) s2-1:138 "it is the rate at which two particles placed in the same box find each other": Lin could have written it, yes. (b) s2-1:94 "the rate is fixed by the energy density of the field, and the speed of the dark matter does not enter": yes. (c) s2-1:40 "The probability per unit time is therefore independent of $t$ in the limit, which is what a rate means": no. Rewrite: "Since the area stays fixed while the width shrinks, the probability per unit time stops depending on $t$, and that is what we mean by a rate."

### 2.2 (REVISE)
- s2-2:94, s2-2:222 | B #19 | "These numbers are printed by the script of \cref{fig:2-hydrogen}." / "...of \cref{fig:2-helm}." | Delete both sentences. The reader cannot run the script, and STYLE already says that every number traces to one.
- s2-2:61 vs s2-4:3,160 vs ch1 (1.11 eV) | B consistency | "a semiconductor gap of \SI{1.1}{eV}" | Use one gap value book-wide (1.11 eV at 300 K, or say "about 1.1 eV").
- s2-2:61 | B clarity / number | "$\omega \approx q_0v \approx \alpha m_ev \approx \SI{4}{eV}$ for $v \approx 10^{-3}$ ... $q \gtrsim \SI{0.4}{keV}$" | At $v = 10^{-3}$ crossing the gap needs $q \gtrsim 1.1$ keV. 0.4 keV holds only at $v_{\mathrm{max}}$. Write "$q \gtrsim \SI{0.4}{keV}$ at $v_{\mathrm{max}}$". Also write "kinematic match" (REGISTER #10) for "kinematic matching".
- s2-2:21,61,68,94,110,153 + 2 more | REGISTER #6 | bare "transfer(s)": "The transfer $\vect{q}$", "range of transfers", "absorbs the transfer", "forces transfers" | "momentum transfer" in each case.
- s2-2:77 | paragraph job (about 350 words) | closed shells, spin counting, crystals, the gas $S(q,\omega)$, second quantization and temperature in one paragraph | Split before "For a gas of such atoms" and before "For several electrons". Untangle "...unchanged, and each occupied orbital contributes once ..., and a full shell ..." into two sentences.
- s2-2:38 | #19 (bookkeeping) | "\Cref{eq:2.2-dsdq} is the normalization collected in \cref{app:A.9} (\cref{eq:A.9-dsdq})." | Delete it, or fold it into a parenthesis: "(also \cref{eq:A.9-dsdq})".
- s2-2:131 | #19 borderline | "Since our derivation includes both spins, that expression counts the $2(2l + 1)$ electrons of a full shell." | Keep it as a fact about the literature, in one clause: "the expression of Ref. [..] counts all $2(2l+1)$ electrons of a full shell". (The editor note asks to verify the factor 2 against the source.)
- s2-2:156 | #20 | "becomes the crystal form factor of Ref.~\cite[Eqs.~(3.10) and (3.13)]{essig2016direct}; \cref{chap:10} treats it" | Name it in one clause ("the same overlap between valence and conduction Bloch states, summed over $\vect{k}$"), and keep the citation for credit.
- s2-2:160–175 | #5 redundancy | "checking it fixes the meaning of $\sigmae$ once more" (repeats eq:2.2-sigma-free in the lab frame) | Keep the worked example for its $m_V$ numbers, and cut "once more" and the duplicate $\sigma_T = \sigmae$ sentence (:168).
- s2-2:162 | title | "Dark-matter scattering off a free electron reproduces $\sigmae$" (a sentence) | "Scattering off a free electron".
- s2-2:174 | REGISTER (at most one per chapter) | "For concreteness take" | Keep this one; it is the only one in the chapter.
- s2-2:197 | #17 grammar | "The rate per unit target mass multiplies by the number of nuclei per unit mass, $1/M$, the dark-matter flux ... and integrates over velocities" | "Multiplying by the number of nuclei per unit mass, $1/M$, and by the flux ..., and integrating over $v > \vmin$, the factor $v/v^2$ becomes $\eta(\vmin)$:".
- s2-2:197 vs s2-1:145 | symbol | $M$ (nucleus) here, $m_T$ (any target) in 2.1 | Both are in NOTATION. Add "with $M$ the nuclear mass" at :197.
- s2-2:225 | #13 unanchored | "Below about \SI{10}{MeV}, a nucleus bound in a crystal no longer recoils freely" | "For dark-matter masses below about ... MeV" (confirm the number with the 5.x writer).
- s2-2:208 | typography | "$c_{\mathrm{nuc}} = 1.23A^{1/3} - \SI{0.60}{fm}$" | "$(1.23A^{1/3} - 0.60)$\,fm", here and in the fig:2-helm caption.
- s2-2:183 | citation needed (editor note) | "nuclear excitation energies are typically hundreds of keV or more" | Cite it or soften it to "the lowest excited states of $^{28}$Si lie at about 1.8 MeV" with a source.
- s2-2:96 | #8 (mild) | "Where does the inelastic probability go?" | Acceptable once, in the Lin manner.
- s2-2:140–154 limit box | STYLE check | It has the formula, a one-line source citation, a comparison plot with the validity region shaded and the ratio panel showing the leading correction, and a closing statement of the breakdown. Within spec. The closing is two sentences against "one sentence". Merge them: "Above the shaded region, where most of the rate lies, $q \ge (E_B + E_{\mathrm{ej}})/v \gg p_{\mathrm{ej}}$ probes the Coulomb wave at $r \sim 1/q$, where it is not a rescaled plane wave, and the approximation falls to a quarter of the exact spectrum at $E_{\mathrm{ej}} = 10E_B$." Restating eq:2.2-ion inside the box is allowed, since the box is self-contained.
- Calibration. (a) s2-2:68 "A momentum transfer much smaller than $1/r$ barely changes the state": yes. (b) s2-2:110 "At $q \ll q_0$ the two cancel and the dark matter sees a neutral atom": yes. (c) s2-2:61 "This is the kinematic matching that makes eV-gap targets work": no. Rewrite: "This is why eV-gap targets are a good kinematic match to sub-GeV dark matter: a \SI{1.1}{eV} gap sits below this energy."

### 2.3 (REVISE)
- s2-3:240–245 | B symbol clash | "$\sum_{\mathrm{s}}z_{\mathrm{s}}^2N_{\mathrm{s}}$, where the sum over $\mathrm{s}$ runs over electrons and nuclear species" (upright s, beside spin $s$ in the same equations) | Use another index, for example $\sum_{a}z_a^2N_a$ over "particle kinds $a$". Register it in NOTATION.
- s2-3:240, A-2:96 | B one symbol, one meaning | "$z_e = -1$ and $z_\kappa = Z_\kappa$" next to $Z_\kappa$ | Either drop $z_\kappa$ (write $z_e = -1$ and use $Z_\kappa$ for nuclei) or list $z$ in NOTATION as the signed charge number.
- s2-3:124,185–190, A-2:67 | notation (editor note) | `v_C(k)` with italic C | Book-wide upright: `v_{\mathrm{C}}`, ideally through a macro.
- s2-3:57 | #18 count-teaser | "Two consequences follow at once." | "Every bilinear commutes with $\op{N}_e$, and ..." (drop the teaser).
- s2-3:51 | #18 | "One identity does most of the work in later calculations." | "The commutator of a bilinear with a single operator, ..., does most of the work later:".
- s2-3:88 | #17 | "The picture is simple." | Delete.
- s2-3:156 | #18 | "A two-orbital example shows what this means." | "Two orbitals, one on each of two neighboring atoms, show what this means for silicon's covalent bond."
- s2-3:221 | accuracy / seam | "jellium ... It is the subject of \cref{sec:2.5,sec:4.5}, and it shows how the cancellation works." (we:2-jellium directly below does the cancellation) | "Jellium (used again in \cref{sec:2.5,sec:4.5}) shows how the cancellation works, in \cref{we:2-jellium} below."
- s2-3:7 | #17 | "so no measurement can change when we swap their labels" | "so swapping their labels changes no measurement".
- s2-3:47 | #14 over-claim | "From here on we never write a determinant again." | The section writes them at :154 and :156. Write "From here on we rarely need a determinant."
- s2-3:32–57, 112, 198 | REGISTER tic (so 62, gives 53 per 10k) | "Each pass costs a sign, so", "So $c_\gamma$ empties", "gives" ×23 | Replace about a third with "since", "because" or "is"/"leads to". Add one "we see" and one "however", for example at :211, "Electrons with opposite spins, however, can be told apart".
- s2-3:117, :3 | tic | "The other $10^{26}$ electrons" | Keep it at :3, and write "the spectators" at :117.
- s2-3:181 | voice (imperative) | "Mind the order of the last two indices" | "The order of the last two indices matters:".
- s2-3:154 | layout | `\end{equation*} Inserting` on one line | Put a line break after `\end{equation*}`. No visible effect.
- s2-3 overall | user rule (succinct background) | at 4,350 words, the longest treatment of textbook background | Advisory: the extensivity check (:259) and the Hartree–Fock energy (:213–217) can shrink to two sentences each. Sect. 3.4 needs only the formula.
- Calibration. (a) s2-3:245 "The nuclei are their own neutralizing background": yes. (b) s2-3:223 "The interaction is not a small perturbation of free electrons": yes. (c) s2-3:57 "The sign problems of fermions cancel in pairs here: a bilinear behaves like an ordinary operator that moves one particle." Mostly yes. (d) s2-3:40 "So $c_\gamma$ empties orbital $\gamma$ if it is full and gives zero if it is empty. Applied twice to the same orbital, either operator gives zero.": no. Rewrite: "In words, $c_\gamma$ empties a full orbital and kills an empty one, and neither operator can act twice on the same orbital."

### 2.4 (REVISE, light)
- s2-4:69–90 vs :3 | B symbol clash (editor note) | state labels $a$, $b$ with "$2\pi/a$" (lattice constant) in the same section | Rename the target states, for example $|\mathrm{i}_T\rangle$, $|\mathrm{f}_T\rangle$ or $g$/$e$, per NOTATION, in the text, eq:2.4-orderings and fig:2-orderings.
- s2-4:3,160 | B consistency | "the \SI{1.12}{eV} gap" | See 2.2. Also the "photon of \SI{1.2}{eV}" example should sit clearly above the chosen gap value.
- s2-4:7 | #18 recap opener | "\Cref{sec:2.1} expanded the state as ... and solved the amplitude equations ... to first order." | Open on the question: "To go beyond first order we need the amplitude equations in a form that iterates; the interaction picture gives it."
- s2-4:61 | clarity | "Second-order processes matter in this book for another reason. The first-order matrix element of the dark-matter interaction vanishes, or no final state is kinematically allowed" (reads as a fact, not a condition) | "...for another reason: when the first-order matrix element vanishes, or no final state is kinematically allowed, a second, internal interaction ... opens the channel."
- s2-4:61 vs :156–164 | #5 within section | The same "first order vanishes, by selection rule or kinematics" argument appears twice | Keep it at :156 and cut :61 to a forward pointer ("\cref{sec:2.4} below lists when").
- s2-4:88 | #6, #17 | "The two orderings are not alternatives to choose between." / "Their denominators differ in an important way." | "Both orderings connect the same states, so their amplitudes add before squaring and can interfere." Delete the second sentence.
- s2-4:102 | #19 (mild) | "which is how \cref{sec:2.1} could claim that $\Gamma_i$ keeps its meaning" | "which justifies the statement of \cref{sec:2.1} that ...".
- s2-4:102 vs s2-1:73,113, D-3:220 | #5 cross-section | the 0.4 % agreement of we:2-continuum, stated three times | Keep it in the worked example and D.3, and cut it here to "(\cref{we:2-continuum})".
- s2-4:24, :59 | #1 signposting | "as the next subsection shows", "which is the problem of the subsections below" | Delete both.
- s2-4:90 | tic | "whatever the other $10^{26}$ electrons do" | "whatever the other electrons do".
- s2-4:150 | symbol | "$\delta_w$" (scale) beside $\delta_1$, $\delta_2$ (denominators) and $\delta(x)$ | Use $\Delta_w$ (not $E_{\mathrm{w}}$, which 2.1 uses) or "an energy scale $W$".
- s2-4:3 | opener length | a 9-sentence motivation that ends in a three-part plan | Acceptable. The plan sentence follows the motivation (REGISTER checklist 1).
- Calibration. (a) s2-4:94 "Nothing in nature diverges here. The trouble is that ... a real excited state decays.": yes. (b) s2-4:183 "In silicon the intermediate electron ... becomes real once the photon energy exceeds the direct gap": yes. (c) s2-4:65 "With a finite observation time $t$, \cref{eq:2.4-golden2} holds for $t \gg 1/|E_i - E_m|$ for every intermediate state that matters.": no. Rewrite: "As long as we watch for longer than $1/|E_i - E_m|$, about a femtosecond below a direct gap, the denominator form holds."

### 2.5 (REVISE, light)
- s2-5:3, :129 vs A-1:51 | B consistency (editor note) | "each optical phonon mode of silicon, at about \SI{60}{meV}" / "take a \SI{60}{meV} optical phonon" vs "$\SI{15.5}{THz}$ ... $\SI{64.1}{meV}$" | Use 64 meV and recompute 0.11 → 0.092, $\beta\omega_0 = 2.48$, ratio 11.9, $10^{-76}$ → $10^{-81}$. Or call it a round illustrative value: "a 60 meV mode (silicon's is 64 meV)".
- s2-5:39, :102 | tic | "that \cref{sec:2.1} anticipated", "anticipated in \cref{sec:2.3}" | Drop "anticipated": "This is the thermal average of initial states (\cref{sec:2.1})".
- s2-5:85 | #18 | "The simplest case shows what it says." | "In a two-level system with splitting $\Delta$ ..." (start with the system).
- s2-5:83 | #19 bookkeeping | "The density form is the diagonal element of \cref{eq:A.7-DB}." | Fold it into the keyresult as "(\cref{eq:A.7-DB})".
- s2-5:64 | citation | "as defined in \cref{eq:A.7-S} and in Ref.~\cite[Eq.~(4)]{knapen2021dark}" | Fine (attribution). Optionally: "the dynamic structure factor of the electron density (\cref{eq:A.7-S}; Ref. [.., Eq. (4)])".
- s2-5:3 | opener | "We will write the thermal state, average the golden rule over it, and derive detailed balance" | Acceptable: the motivation comes first.
- Calibration. (a) s2-5:129 "the ``$+1$'' of spontaneous emission is the whole signal: the dark matter creates a phonon in an empty mode": yes. (b) s2-5:144 "Silicon is of course not a metal ... The gas sets the scales, however.": yes. (c) s2-5:19 "The Gibbs state is a function of $H$, and commutes with $H$.": no. Rewrite: "Since the Gibbs state is a function of $H$, it commutes with $H$ and does not evolve."

### App. A (REVISE)
- appA.tex:2 | B scrub (source) | "% Appendix sections are \input here in order as they are accepted." | Delete. Same in appD.tex:2.
- A-4:190 | B #19 (the checklist's own example) | "The book's sign is binding for this reason, and a formula taken from a source with the other convention is converted before use, by $\vect{q} \to -\vect{q}$ in every target quantity." | Make it a fact about the literature: "A formula written in the other convention becomes ours under $\vect{q} \to -\vect{q}$ in every target quantity."
- A-7:163 | B #19 | "...is one and is dropped; the text says so when it does." | "At $T \ll \omega$ the factor is one."
- A-7:195 | B #19 | "...and a source quantity defined per spin is labeled as such when it is quoted." | Delete the clause.
- A-6:131 | B #19 | "so the book never uses one name for both" | Delete. The preceding sentence already fixes the name.
- A-2:96 | B #19 | "A formula quoted from a source keeps the source's units and says so; the text then states its form in Heaviside--Lorentz units." | Delete it. Move "Charge numbers are written $z_e$ ..." out of the fields paragraph (see 2.3 on $z_\kappa$).
- A-8:3 | B #19 | "The values are conventions, chosen so that results of different experiments and calculations can be compared" | "These are the standard values of Ref. [baxter, Table 1]; the measured ranges are in \cref{sec:1.2}."
- A-5:31 | B typography | ". a vertex defined with an extra factor $N$" (lowercase sentence start) | "A vertex defined ...".
- A-8:29, :39 | B cross-reference | "\cref{eq:A.7-S} absorbs the remaining $2\pi/V$ (\cref{sec:2.2})"; "contraction ... with the response matrix $S_{ab}$ (\cref{sec:2.2})" | The thermal golden rule with $S$ is eq:2.5-golden. Write \cref{sec:2.5}. For the second, point to the chapter that builds $S_{ab}$ (\cref{chap:8}).
- A-9:77, :82 | notation (editor note) | "$\dd\sigma/\dd\Omega_q$", "$\dd\sigma/\dd q = q\sigma/(2\mu^2v^2)$" | Write $\sigma_T$, $\mu_{\chi T}$ (or $\mu_{\chi e}$/$\mu_{\chi N}$), and $\dd\Omega_{\vect{q}}$ as in eq:2.2-born.
- A-4:180 | REGISTER #9 | "The least speed that makes a transfer $(\vect{q},\omega)$ possible" | "The minimum velocity needed for a momentum transfer $\vect{q}$ and energy deposit $\omega$".
- A-4:184 | wording | "The sign of $\omega$ is never folded either" | "Nor is $\omega$ restricted to positive values".
- A-3:172 vs A-4:192 | #5 | "The transfer $\vect{q}$ itself is never folded" / "The transfer $\vect{q}$ is also never reduced to the first Brillouin zone" | Keep one, in A.3, and let A.4 point to it.
- A-8:7–13 | #5 cross-chapter | the reference Earth speed and 781–810 km/s, the fifth statement after ch1 (ch1 review, redundancy 1) | As the definition home, keep it here. Cut "and the book keeps them apart".
- A-8:13 | typography | "$v_{\mathrm{E}} \approx \SI{232}{}$ to \SI{244}{km.s^{-1}}" | `\SIrange{232}{244}{km.s^{-1}}`.
- A-1:15, A-2:94, A-3:163 | #20 | "tabulates the astrophysical units"; "our $\tilde R$ up to the sign and the factor $1/V$ that each source fixes in its own definition"; "states the transforms ... that the electron--phonon literature uses" | A-2:94 is the real case: state the sign and the $1/V$ relation. The other two are optional reading pointers and can stay or go.
- A-2:88, A-7:204, A-9:56 | #18 count-teasers | "Three cases occur in this book." / "Two other forms are in common use." / "Three choices in this definition need stating" | Name them: "The plasma frequency, the dielectric matrix and the optical conductivity convert as follows."
- A-5:40 | title | "Phases and one gauge" | "Gauge consistency".
- A-1:27 | #19 (mild) | "\Cref{sec:1.2} rounds the first to ..." | Delete.

### App. D.2 (PASS)
- D-2:110 | #18 (mild) | "The proofs rest on one lemma." | Acceptable for an appendix proof. Optionally: "Everything rests on the following lemma."

### App. D.3 (REVISE, one-line fix)
- D-3:218–220 | B symbol | "$Z = 1/(1 - R'(z_{\mathrm{p}}))$", "$Z^2\ee^{-\Gamma_it/(1-R')}$" (Z is the charge number, and $\mathcal{Z}$ the partition function) | Use NOTATION's residue symbol $z_{\mathrm{qp}}$ or a new $Z_{\mathrm{p}}$. Register it.
- D-3:211 | #10 (mild) | "The size of the corrections follows from an exact solution" | Fine.

## 5. Checklist dispositions (items with no further hits)
- Sentence length: no prose sentence over 45 words (all lint hits are detex merges). The long units are paragraphs (2.1:73, 2.2:77, 2.2:208, 2.3:259).
- Filler and inflation: "The picture is simple" (2.3:88), "in an important way" (2.4:88), "standard reference" (A-5:10, mild). There is no delve, crucial or notably, and no generic praise.
- Reflexive triads and stacked hedges: none. The three-part plans in the 2.4 and 2.5 openers carry content.
- Lists for argument: none. The only itemize (2.3:227, the three $\vect{k} = 0$ terms) is a genuine enumeration.
- Titles: all section and subsection titles are short noun phrases. Two fail: the worked-example title at 2.2:162 (a sentence) and A-5:40.
- Equation punctuation: every display checked ends with a comma or full stop as grammar requires. The two lint hits are false positives.
- First-use symbols: all defined at or before first use, or in NOTATION ($M$, $a_0$, $\mathcal{D}_f$, $v_C$). Clashes are listed above ($a$/$b$, $\mathrm{s}$/$s$, $z_\kappa$/$Z_\kappa$, $Z$ residue, $\delta_w$).
- Captions: figures 2.1 to 2.6, fig:2-ionization-limit and tables 2.1 and A.1 stand alone. fig:2-ionization-limit relies on "\cref{tab:1-shm}" for the halo parameters, which is acceptable.
- Citations: numeric, with equation-specific options, and no concatenated `\cite\cite`. Section-level textbook pointers (Sakurai, Cohen-Tannoudji, Landau–Lifshitz, Peskin) are attribution only. The editor note asks to verify their section numbers.
- Cross-references: `\cref`/`\Cref` throughout, with no hard-coded numbers. The one wrong target is A-8 (sec:2.2 for 2.5).
- User rules: no exercises, checkpoints or tasks for the reader, and no "you". Every check is carried out in the text, and D.2 and D.3 write out the steps 2.3 and 2.4 defer. Pattern-20 hits are listed under App. A and 2.2:156. Background is succinct apart from the advisory trims in 2.1 and 2.3.

## 6. Chapter as a whole
- **Opening (ch02.tex:3).** It is motivational and concrete: flux, kinetic energy and the $10^{26}$-electron question, with a closing orientation sentence. However, its middle runs through 2.3, 2.4 and 2.5 in order ("The final states ... second quantization. Some of its transitions ... intermediate state ... And a detector is not at absolute zero"), which is close to an outline in disguise, and it says nothing of absorption (2.1). This is acceptable. Optional: fold the three topics into one sentence about why a solid differs from two-body scattering, and mention absorption by bosonic dark matter once.
- **Scrub (B).** ch02.tex:5 "% Sections are \input here as they are accepted: \input{ch02/s2-1} ..." | Delete (as in ch1).
- **Summary (s2-5:153–161).** It reads as prose and covers 2.1, 2.2, 2.3 and 2.5 in order. Fixes:
  (a) B: 2.4 gets one clause (:159), merged into the 2.3 paragraph. Its main results are missing: the T-matrix, the two time orderings and their interference, Wigner–Weisskopf decay at the golden-rule rate, and the split of a resonant rate into cascade plus finite part (eq:2.4-split). Give 2.4 its own paragraph of 3–4 sentences.
  (b) :161 "vanishes in a cryogenic detector for every excitation above a few tens of μeV" | "is suppressed by $\ee^{-\beta|\omega|}$ and negligible in a cryogenic detector for ...".
  (c) :155 repeats the "some $10^{26}$ electrons" opener. Open on the golden rule itself.
  (d) It omits the Born-validity statement (all couplings $\lesssim 10^{-3}$) and the $\eta$ structure of 2.2. Add one clause on each.
- **Redundancy across sections.**
  (1) $\sqrt n$/$\sqrt{n+1}$ and spontaneous emission: 2.1:92, 2.3:74, 2.5:108, WE 2-oscillator. Keep the derivation in 2.3 and the thermal form in 2.5, and make 2.1 a forward pointer.
  (2) The "first order vanishes" argument: 2.1:75, 2.4:61, 2.4:156. Keep 2.4:156.
  (3) $\sigmae$ as the free cross-section: eq:2.2-sigma-free, WE 2-free, eq:2.1 final paragraph ($|\mathcal{M}|^2$), A.9:82. A.9 should point to 2.2 only.
  (4) WE 2-continuum's 0.4 % agreement: 2.1:113, 2.4:102, D-3:220. See 2.4.
  (5) The halo average of the delta function, $\eta/(2q)$: 2.2:72, 2.5:66, A-8:23. Acceptable as recall with \cref. Make 2.5:66 cite eq:2.2-spectrum.
  (6) $\nd_e = 2.00\times10^{23}$ cm⁻³ for silicon: 2.3:223, 2.5:144, A-2:94. Acceptable with \cref{app:A.2}.
- **Seams.**
  - 2.1|2.2: clean. 2.1 ends "\Cref{sec:2.2} evaluates the cross-section with \cref{eq:2.1-Vbox}" (:145) and then a relativistic coda (:147–151). 2.2 opens on the free-electron cross-section. Moving the coda before :140, or into A.9, would make 2.1 end on the hand-off.
  - 2.2|2.3: good. 2.2 ends on nuclei and phonons (:225). 2.3 opens on the many-electron final state, which 2.2:77 had flagged ("second quantization ... is the bookkeeping"). The seam is on the topic, not on the last paragraph. Optional: end 2.2 with one sentence returning to the many-electron problem.
  - 2.3|2.4: weak. 2.3 ends on DFT and codes (:269). 2.4 opens with the silicon photon example, which is fine, but its first subsection opens with a recap (:7, see 2.4). The bridge exists (2.3:57 says the oscillation "is how the energy denominators of \cref{sec:2.4} ... arise"), so 2.4:12 already picks it up. No further change.
  - 2.4|2.5: clean. 2.4 ends on 6.5 and phonon-assisted rates. 2.5 opens on phonon occupations at 300 K and 4 K, the thermal factors that 2.4:88 deferred ("\cref{sec:2.5} averages them").
