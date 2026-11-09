# Chapter 1 prose review (style and prose, isolated)

Scope: tex/ch01/s1-1.tex to s1-5.tex, ch01.tex, tex/appC/C-9.tex, tex/appD/D-1.tex, checked against STYLE.md,
style-guide.md and prose-review.md. Tex not edited. Locations are `file:line` in the source.
Rule (prose-review.md): PASS needs at most 3 minor hits per 1,000 words. **B** marks a blocking hit (standalone or
consistency failure), which forces REVISE whatever the count.

## 1. Lint (lint.py --banned BANNED-TERMS.txt)
| file | hits | note |
|---|---|---|
| s1-1 | 0 | |
| s1-2 | 1 LONG-SENT | false positive: detex merges the tab:1-shm caption with its cells |
| s1-3 | 1 LONG-SENT | false positive: tab:1-kinematics caption plus cells |
| s1-4 | 1 LONG-SENT | false positive: tab:1-interactions caption plus cells |
| s1-5 | 1 LONG-SENT | false positive: tab:1-quanta caption plus cells |
| C-9, D-1 | 0 | |
No banned term fires. The lint regexes miss two internal terms that do occur: "thread(s)" (s1-3:207, s1-5:189) and the
comment "NOTATION reserves" (s1-1:2). The lint should be extended with `\bthreads?\b` (prose only) and `\bNOTATION\b`.

## 2. Verdicts
| section | words (approx., prose only) | minor hits | PASS allowance | blocking | verdict |
|---|---|---|---|---|---|
| 1.1 Evidence for dark matter | 1,200 | 5 | 3 | 1 | REVISE (light) |
| 1.2 The local halo | 3,500 | 7 | 10 | 1 | REVISE (light; one blocking number) |
| 1.3 Kinematics of slow dark matter | 3,650 | 9 | 11 | 5 | REVISE |
| 1.4 Light dark-matter models | 2,400 | 8 | 7 | 0 | REVISE (light) |
| 1.5 Detector signals (+ Summary) | 3,400 | 7 | 10 | 3 | REVISE |
| App. C.9 | 1,400 | 2 | 4 | 0 | PASS |
| App. D.1 | 700 | 1 | 2 | 1 | REVISE (one-line fix) |
| Chapter level | n/a | n/a | n/a | 1 (no outline paragraph) | REVISE |
No section needs REWRITE. The voice problems are local, not systemic.

## 3. Voice consistency across the five writers
All five sections use "we" consistently, never "I" and never "you", and use American spelling throughout. A grep found no
British forms. Register is the same everywhere: claims carry numbers, and hedges are rare and conditional.
Differences between writers: 1.2 and 1.3 write in very long, numerically dense paragraphs (up to about 330 words). 1.4
and 1.5 use shorter paragraphs and run-in headings. 1.1 is the most compressed. Source macros differ (`\mchi` in 1.3,
`m_\chi` elsewhere), which renders the same and needs no change. Two section openers echo each other (1.1:4 and 1.4:3,
see seams). The one reader-addressing phrase is s1-3:7 "which every reader has met".

## 4. Issues by section (location | pattern | quoted text | fix)

### 1.1
- s1-1:2 | B scrub (source) | "% Number density: NOTATION reserves script n; no macro exists yet ... (see open questions)" | Delete; STYLE now defines `\nd`.
- s1-1:68 | first use | "$g_{\mathrm{deg}}(m_\chi T/2\pi)^{3/2}$" | Define it: "with $g_{\mathrm{deg}}$ the number of internal states of $\chi$".
- s1-1:42 | first use | "the combination $\Omega_{\mathrm{c}} h^2$ is reported" | Define it first: "$\Omega_{\mathrm{c}} = \rho_{\mathrm{c}}/\rho_{\mathrm{crit}}$, the cold-dark-matter fraction".
- s1-1:30 vs s1-2:90 | consistency | "0.3 to \SI{0.5}{GeV.cm^{-3}}" vs "between 0.2 and \SI{0.6}" | Quote one range (Baxter's 0.2 to 0.6) in both, or say why the ranges differ.
- s1-1:83 | #5 restating | "These masses point to solids. Light dark matter carries between a meV and a keV..." | This repeats the kinetic-energy list of s1-1:62 and the bands of Fig. 1.1. Fold its one new fact (the excitation scales) into s1-1:62 and end the section on the freeze-out paragraph, or replace it with one bridging sentence to 1.2.
- s1-1:68–79 | user rule (succinct background) | the in-text iteration for $x_{\mathrm{fo}}$ and the $s_0$ algebra | Optional: keep the result and the 2e-26 check, and move the iteration to an appendix or cite it. The section is within budget, so this is advisory.

### 1.2
- s1-2:90 | B consistency | density range differs from 1.1 | See 1.1.
- s1-2:104 and s1-2:121 | #5 redundancy | "$v_0 = \SI{238}{km.s^{-1}}$, from the proper motion of the radio source..." and again "the Sun's angular velocity ... \SI{30.24}{...} ... gives $v_0 = 238$" | Keep the arithmetic at :121 only; at :104 write "the adopted value is $v_0 = 238$ km/s (derived below Eq. (1.2-vsun))".
- s1-2:167 and s1-2:233 | #5 redundancy | "the annual mean of $|\vect{v}_{\mathrm{E}}(t)|$ is 252.1 ..., not 250.5" and "The reference convention costs little ... annual-mean speed 252.1" | Keep the reason (quadrature) at one place (:231) and give only the consequences for $\eta$ at :233. 1.3:182 repeats it a third time (see chapter level).
- s1-2:249 and s1-2:316 | #5 | "\SI{0.47}{km.s^{-1}} at the equator" and "The Earth's rotation adds at most \SI{0.47}{km.s^{-1}}" | Drop the second sentence or point back: "(the rotation, 0.47 km/s, is negligible; see daily modulation)".
- s1-2:160 | paragraph job | one paragraph defines notation, the wind, the mean velocity, the spread, the angular fractions and the relativistic correction | Split after "cut or no cut." and move "Relativistic corrections..." next to Eq. (1.2-galilean).
- s1-2:283 | paragraph job (about 310 words) | "For an isotropic target ... \Cref{chap:10} treats the target side" | Split at "The simplest anisotropy shows" and again at "Polar crystals with". The repeated citation \cite[Sect.~III\,C]{griffin2018directional} can then appear once.
- s1-2:211 | forward definition | "$\eta(\vmin) = \langle \Theta(v - \vmin)/v\rangle$ that \cref{sec:1.3} introduces" | Allowed by design, but $\vmin$ is not defined here. Add "with $\vmin$ the minimum speed of \cref{eq:1.3-vmin}".
- s1-2:245 | #9 tone (mild) | "Annual modulation is a signature because..." | Acceptable; no change.

### 1.3
- s1-3:207 | B scrub | "This edge is a thread of the book:" | "The edge recurs throughout the book:".
- s1-3:3 vs s1-1:62 | B consistency | "carries a few eV of kinetic energy at \SI{1}{MeV} and a few meV at \SI{1}{keV}" vs 1.1 "\SI{0.5}{eV} at \SI{1}{MeV}" | Write "at most 3.5 eV at 1 MeV and 3.5 meV at 1 keV (at $v_{\mathrm{max}}$)", or "about 0.5 eV ... at a typical speed".
- s1-3:171 vs D-1:160 | B consistency | "Eqs.~(67) and (68) of Ref.~\cite{essig2016direct}" vs "\cite[Eqs.~(66) and (68)]{essig2016direct}" | Check the source and use one pair in both places, inside the cite option.
- s1-3:166–170 | B redundancy with D.1 | `eq:1.3-eta-shm` displays exactly `eq:D.1-eta1` | The 1.3 brief says to point to D.1, not duplicate it. Replace the display with "\cref{app:D.1} gives the three branches, \cref{eq:D.1-eta1,eq:D.1-eta2}". If a display is kept for the reader, label it once and \cref it from D.1.
- s1-3:45 | B typography | `"every particle qualifies"` (ASCII double quotes) | Use ``every particle qualifies'' or rephrase without quotes.
- s1-3:7 | #17 / voice | "which every reader has met" | Delete.
- s1-3:7 and s1-3:121 | #5 / order | "We never fold $\vect{q}$ back into a Brillouin zone" before the zone is introduced, and the argument for it again at :121 | Keep only the forward pointer at :7, "(\cref{sec:1.3} explains below why $\vect{q}$ is never folded)", or drop :7 entirely.
- s1-3:45 | seam circularity | "as stated in \cref{sec:1.4}" (1.4 comes later, and its :167 re-explains this) | "as \cref{sec:1.4} uses for exothermic models".
- s1-3:37, :158 | citation style | `\cite[Eq.~(9)]{kahn2022searches}\cite[Eq.~(116)]{lin2019tasi}\cite[...]` | Use `\cites[Eq.~(9)]{kahn2022searches}[Eq.~(116)]{lin2019tasi}...`, as s1-1:81 does.
- s1-3:66 and s1-3:123 | #5 | the gap "\SI{1.11}{eV} at room temperature~\cite[Eq.~(5.2)]{essig2016direct}" given twice | At :123 write "$\Eg$ (\cref{we:1-mmin})".
- s1-3:119 | #2 / accuracy | "\cref{tab:1-kinematics} gives $2\mchi v_{\mathrm{max}} = q_0$ at $\mchi = \SI{0.70}{MeV}$" | The table has no 0.70 MeV row. Write "$2\mchi v_{\mathrm{max}} = q_0$ at 0.70 MeV". Also cut "exactly" in "transfers exactly the momenta".
- s1-3:123 | #1 signposting | "each defined here in one sentence and treated later" | Delete the clause.
- s1-3:95 | caption standalone | "Columns: the largest momentum transfer...; the largest energy transfer; ... The third column is also the threshold" | The caption lists three data columns, but "third" counts $\mchi$ as the first. Write "The $\tfrac12\mchi v_{\mathrm{max}}^2$ column is also the threshold for which $m_{\mathrm{min}} = \mchi$".
- s1-3:146, :184 | label scheme | `sec:1.3-eta`, `sec:1.3-edge` (also `sec:1.5-quanta`, `-rate`, `-limit`, `-plot`, `-inputs`) | STYLE labels are `sec:N.M`. Either accept subsection labels in the scheme (add the rule to STYLE) or rename them. No visible effect.
- s1-3:21, s1-3:205 | paragraph length (about 330 and 240 words) | | Split :21 at "To keep the models of"; split :205 at "The recovery above the edge is slow."

### 1.4
- s1-4:3 | seam / #5 | "Gravity fixes how much dark matter there is; a detector needs to know how it couples" | This echoes the s1-1:4 opener and skips 1.3. Write: "Kinematics (\cref{sec:1.3}) decides which transfers are open; the interaction decides how often they occur."
- s1-4:58 (×3), s1-4:105 | sentence opens with a symbol | "$\sigmae$ has a direct meaning." / "$\sigmae$ is that cross-section" / "$\sigmae$ is defined in vacuum." / "$\Pi$ and the longitudinal..." | "The reference cross-section has a direct meaning."; "It is that cross-section..."; "The quantity $\sigmae$ is defined in vacuum."; "The self-energy $\Pi$ and...".
- s1-4:167 and s1-5:197 | notation | "$\omega_q$" | Use `$\omega_{\vect{q}}$` as in Eq. (1.3-omegaq).
- s1-4:167 | #5 cross-section | "For $\Delta_\chi > 0$ (endothermic) ... For $\Delta_\chi < 0$ (exothermic) the dark matter releases $|\Delta_\chi|$" | This was already stated in 1.3:37 and :61. Keep the model origin here and replace the two sentences with "(endothermic and exothermic cases, \cref{sec:1.3})".
- s1-4:3, :114 | citation style | `\cite[Sect.~III]{lin2019tasi}\cite{kahn2022searches}`, `\cite{lewin1996review}\cite[Eq.~(104)]{lin2019tasi}` | Use `\cites`.
- s1-4:56 | citation style | "which are Eqs.~(11) and (12) of Ref.~\cite{knapen2021dark}" | Write "in agreement with Ref.~\cite[Eqs.~(11) and (12)]{knapen2021dark}". (s1-4:37 already cites these equations, so the clause can go.)
- s1-4:114 | paragraph job (about 270 words) | coherence, isospin, $Z^2$, silicon numbers, Helm, screening and phonons in one block | Split after "...the standard convention for spin-independent scattering" and again before "At larger $q$".
- s1-4:148 | caption standalone | "The target quantities are made precise in the chapters cited in the text." | Name them: "(Chap. 4 for density response and conductivity, Chap. 8 for spin and kinetic responses, Chap. 5 for phonons)" via \cref.
- s1-4:21–23 | equation punctuation / layout | "With the Fourier convention of \cref{app:A.3} and \cref{eq:C.9-Gq}," then a blank line before the keyresult | Remove the blank line so the sentence runs into the box, or end the sentence before the box.
- s1-4:105 | #17 | "propagate differently from in vacuum" | "propagate differently than in vacuum", or "the medium modifies the mixing".

### 1.5
- s1-5:189 | B scrub + hard-coded numbers | "Two threads of this book start here. ... Part~I builds the response, and Part~III" | Write: "Two lines of argument start here." Use \cref to part labels (add `part:N` to the STYLE label scheme), or name the parts.
- s1-5:44 | B consistency | "each photon above the \SI{1.2}{eV} gap" | 1.11 eV is used everywhere else. Write "above the silicon gap (\SI{1.1}{eV})", or say that 1.17 eV is the low-temperature gap.
- s1-5:99–101 | #17 / punctuation | "In words, well above threshold" followed by an equation | "Well above threshold, therefore,".
- s1-5:42, :80 | #17 | "(precise in \cref{sec:7.2})", "(precise in \cref{sec:4.2})" | "(made precise in ...)".
- s1-5:119, :124, :129, :139, :201 | units style | "90\%", "95\%", "21\%" | Elsewhere the chapter uses `\SI{..}{\percent}`. Use one form, e.g. \SI{90}{\percent} confidence.
- s1-5:66 vs s1-4:130 | first use / double definition | "uses the \emph{target mass density} $\rho_T$" (already defined at 1.4:130), and $\mathcal{R}$ is used at 1.4:127 before this definition | At 1.4:125 write "the absorption rate $\mathcal{R}$ per unit target mass (\cref{sec:1.5})"; at 1.5:66 write "the target mass density $\rho_T$ (\cref{sec:1.4})".
- s1-5:146–150 | #11 | "The factors are:" followed by four semicolon fragments | Acceptable as an enumeration inside a worked example; optionally set it as an itemize or a single sentence.
- s1-5:159 | title | "Reading an exclusion plot" (gerund phrase) | "Exclusion plots".
- s1-5:191 | structure | `\section*{Summary}` inside s1-5.tex | Acceptable, but STYLE gives one file per section. Consider moving it to tex/ch01/summary.tex, input from ch01.tex.

### App. C.9 (PASS)
- C-9:65 | #14 over-claim | "the static potential is exact for every purpose of this book" | "accurate to a part in $10^{5}$ for every purpose of this book" (this matches s1-4:31).
- C-9:102 | paragraph length | the kinetic-mixing paragraph covers the shift, the rescaling, the millicharge alternative and the electron sign | Optional split before "For $m_V = 0$ the alternative shift".

### App. D.1 (REVISE, one-line fix)
- D-1:160 | B consistency | "Eqs.~(66) and (68)" vs 1.3:171 "(67) and (68)" | See 1.3.
- D-1:112–116 | equation numbering | the `gather` numbers both lines but labels only the second (`eq:D.1-gauss`) | Add `\notag` to the first line and refer to "\cref{eq:D.1-gauss} and the line above", or label both.

## 5. Checklist dispositions (items with no further hits)
- Sentence length: no prose sentence over 45 words (the lint hits are table artifacts). The long units are paragraphs, listed above.
- Filler and inflation: only "exactly" (s1-3:119) and "every reader has met" (s1-3:7). "classic result" (s1-3:19) and "most studied" (s1-4:78) are factual. No delve, crucial, notably and similar words.
- Reflexive triads and stacked hedges: none found.
- Lists for argument: none. The four run-in paragraphs of 1.5 (Charge, Phonons, Quasiparticles, Photons) carry prose argument.
- Titles: all section and subsection titles are short noun phrases except "Reading an exclusion plot". There are no colons, questions or epigraphs.
- Equation punctuation: every display checked ends with a comma or full stop as grammar requires (including the cases, aligned and split endings). The exceptions are the 1.4:21 paragraph break and the 1.5:99 "In words".
- First-use symbols: gaps at $g_{\mathrm{deg}}$, $\Omega_{\mathrm{c}}$, $\vmin$ at 1.2:211 and $\mathcal{R}$ at 1.4:127. Everything else is defined at or before first use.
- Captions: figures 1.1 and 1.3 to 1.9 stand alone. Two table captions fail (1.3:95, 1.4:148).
- Citations: numeric, with equation-specific options throughout. The inconsistencies are concatenated `\cite\cite` versus `\cites`, and equation numbers written outside the cite (1.3:171, 1.4:56).
- Cross-references: `\cref`/`\Cref` everywhere. The exceptions are hard-coded "Part~I"/"Part~III" (1.5:189) and "the next six chapters" (1.5:201, use \crefrange{chap:2}{chap:7}).
- User rules: no exercises, checkpoints or tasks for the reader. Every "check" is carried out in the text, and the derivations sent to D.1 are written out there. Background is succinct apart from the optional freeze-out trim (1.1).

## 6. Chapter as a whole
- **Opening outline paragraph: missing (B).** ch01.tex goes from `\chapter{Light dark matter}\label{chap:1}` straight to `\input{ch01/s1-1}`. Add a 4–6 sentence outline before the first \input: what the chapter fixes (density, halo, kinematics, interaction conventions, signal and limit) and the reference values later chapters inherit ($\rho_\chi$, $v_{\mathrm{max}}$, $\sigmae$, $\FDM$, $\eta$). Also delete the process comment ch01.tex:2 "% Sections are \input here as they are accepted".
- **Summary (s1-5:191–201).** It covers all five sections, in order, and reads as prose. Fixes:
  (a) :197 "every rate contains the mean inverse speed $\eta(\vmin)$" is wrong for absorption. Write "every scattering rate" and call $\eta$ "the mean inverse speed above $\vmin$".
  (b) :197 `$\omega_q$` should be `$\omega_{\vect q}$`.
  (c) :193 "open over many decades" should match 1.1: "about 90 decades".
  (d) It omits the *theory uncertainty* that 1.5:187 defines as a book-long concern. Add one sentence.
  (e) :201 "the next six chapters" should be a \crefrange.
- **Redundancy across sections.**
  (1) The reference versus actual Earth speed and the 781–810 km/s end point are stated at 1.2:167, 1.2:233, the 1.2 figure caption, 1.3:63 and 1.3:182. Keep the definition in 1.2 and only consequences in 1.3.
  (2) The endothermic/exothermic explanation appears at 1.3:37, 1.3:61 and 1.4:167.
  (3) Eq. (1.3-eta-shm) duplicates Eq. (D.1-eta1).
  (4) The kinetic-energy-versus-solid-scales paragraph appears at 1.1:62/83 and again in the 1.3 opener.
  (5) $q_0 = \alpha m_e = 3.73$ keV is restated in 1.4:37 and the Fig. 1.7 caption. That is acceptable as recall with \cref.
- **Seams.**
  - 1.1|1.2: 1.1 ends by pointing to 1.3 ("\cref{sec:1.3} derives what energy..."), skipping 1.2. 1.2 opens well ("Every rate in this book is an average..."). Fix: end 1.1 on the solids sentence plus "The next step is the velocity distribution of the particles that reach a detector (\cref{sec:1.2})."
  - 1.2|1.3: clean. 1.2 hands over $\rho_\chi$, $f_\chi$ and $v_{\mathrm{max}}$ explicitly, and 1.3 picks them up. The only defect is the 0.5 eV versus "a few eV" conflict at 1.3:3.
  - 1.3|1.4: weak. 1.3 ends on the edge "thread", and 1.4 restarts from gravity, echoing 1.1:4. Use the 1.4:3 rewrite above.
  - 1.4|1.5: clean. 1.5:3 recaps 1.2 to 1.4 in one sentence and states its own job.
