# Ch13 prose review (style and prose, isolated)

Scope: tex/ch13/ch13.tex, s13-1 … s13-9 (Summary inside s13-9), App. D.35–D.37. Checked against STYLE.md, the skill style guide, prose-review.md (patterns 1–17; patterns 18–26 as defined in STYLE.md, since prose-review.md stops at 17), REGISTER.md, and editor-notes.md (prose items). No tex edited. Nothing committed.

## Verdicts

| Unit | Verdict | Main reasons |
|---|---|---|
| Chapter opening (ch13.tex) + map caption | REVISE | a provenance sentence; a figurative phrase; four orienting sentences where the rule allows one |
| 13.1 The indirect-gap window | REVISE (light) | British "favours"; the last subsection mostly restates and points ahead (pattern 26); "only" and "gives" overused |
| 13.2 The phonon-assisted amplitude | REVISE | provenance sentence; a preview paragraph that the subsections then repeat; bare "transfer"; abstract opener; two paragraphs over 300 words |
| 13.3 The phonon-assisted rate | REVISE | two provenance sentences; δ_w used before it is defined; "we call"; the 1.33 keV bound is not labeled as parabolic |
| 13.4 Screening of the phonon-assisted rate | REVISE | the environment name "keyresult" appears three times in the prose (standalone scrub); rhetorical question; negation-stacked opener; restated numbers |
| 13.5 The optical limit | REVISE | the L^PA / ε₂^PA convention from 13.4 is not followed; the keyresult box disagrees with the corrected factors given in the text after it |
| 13.6 Soft phonons, resonances and the off-shell window | REVISE | the title is a list (lint); anthropomorphism; an unclear θ_ep sentence; "Estimates give" with no source |
| 13.7 Temperature and zero-point renormalization | REVISE | rebuttal of an internal estimate (pattern 19); AHC used without definition; "measured" written for "computed"; closing paragraph adds nothing (pattern 26) |
| 13.8 Excitons with phonons and phonon-assisted absorption | REVISE | reconciliation sentence in the opener; provenance sentence; a test written as a plan; a source coefficient left undefined (pattern 20) |
| 13.9 The silicon window (with Summary) | REVISE | rhetorical question; novelty claim; production-status wording ("interim", "computed once", "has not been run"); a VERIFY item; the Summary misstates the screening factor; Open problems restate earlier text |
| D.35 | PASS | minor: its title repeats the chapter title; abstract opener |
| D.36 | PASS | minor: abstract opener written as an outline |
| D.37 | REVISE (light) | title too long (lint); "A check in one dimension" duplicates the worked example; aphorism at the close |

No section needs REWRITE. The voice is consistent across the nine writers: "we" throughout, connected prose, no bulleted argument, numbers given with their basis. The problems that recur in every section are provenance sentences, register tics, and the chapter's habit of explaining the light-versus-dark-matter contrast four times.

## 1. Lint (lint.py --banned BANNED-TERMS.txt)

0 blocking hits in every file. No banned terms.
- ch13.tex 1 LONG-SENT. s13-1 3 LONG-SENT. s13-2 2 EQ-PUNCT, 5 LONG-SENT. s13-3 2 EQ-PUNCT, 2 LONG-SENT. s13-4 4 EQ-PUNCT, 1 LONG-SENT. s13-5 1 LONG-SENT (caption). s13-6 1 TITLE, 8 LONG-SENT. s13-7 3 EQ-PUNCT, 6 LONG-SENT. s13-8 3 EQ-PUNCT. s13-9 1 EQ-PUNCT, 9 LONG-SENT (mostly table rows and captions). D-35 2 EQ-PUNCT, 1 LONG-SENT. D-36 1 EQ-PUNCT, 2 LONG-SENT. D-37 1 TITLE, 1 EQ-PUNCT, 3 LONG-SENT.
- EQ-PUNCT: every hit read by hand. All are false positives: the punctuation sits before `\end{aligned}` or `\end{gathered}`, or the display continues the sentence (s13-4 l.110, s13-9 l.8, D-36 l.37, D-37 l.46). One real miss that lint did not flag: s13-4 l.116 (below).
- TITLE: s13-6 and D-37, both confirmed (items 13.6-1 and D.37-1).
- LONG-SENT: most hits are table rows, captions or sentences with inline math. The prose sentences worth splitting are listed under each section.

## 2. Issues by location (location → problem → fix)

### Chapter opening (ch13.tex l.2) and map caption
- O-1 l.2 → provenance sentence (STYLE: no self-narrating or provenance sentences): "and most of what follows is derived in this book rather than taken from the literature" → delete the clause.
- O-2 l.2 → figurative phrase (pattern 25): "the measured absorption edge of silicon is the record of it" → "and the measured absorption edge of silicon measures that process".
- O-3 l.2 → the paragraph has four orienting sentences (8.6 sector, second order, optical limit and App. E.14, the map), where the rule allows at most one → keep "\Cref{fig:13-map} shows how the pieces connect." and the sector sentence; cut "The amplitude is of second order…" (it is repeated in the map caption, 13.2 l.3 and the Summary) and the App. E.14 clause.
- O-4 l.2 → awkward wording: "how to compute it without counting again the zero-phonon rate" → "without double-counting the zero-phonon rate"; "and what about the edges of that window is still open" → "and which of its edges are still uncertain".
- O-5 caption l.7 → "Side objects:" is an informal label → "The figure also places the off-shell window …".

### 13.1
- 1-1 l.7 → British spelling: "favours" → "favors". It is the only British spelling in the chapter.
- 1-2 l.7 → figurative (pattern 25): "The two requirements pull apart" → "The two requirements conflict".
- 1-3 l.19 + l.23 → stated twice (patterns 5/26): l.19 "can only raise the result. Both are common simplifications, and both give upper values." and then l.23 "These are upper values." → keep l.19's "…can only raise the result" and open l.23 with "The pair need not move along the valley axis…".
- 1-4 l.43 (subsection "Onset precision and the zero-phonon edge", paragraph 1) → pattern 26. New facts: only "where the window ends is a ratio of two rates". The rest restates the worked example ("\SI{3e-4}{MeV}" per meV is the worked example's 2.8e-4; the Ge 0.002 MeV is the 0.2119–0.2141 bracket) and then lists pointers to 13.3, 13.7, 13.8 and 13.9 that the chapter map already gives → cut to two sentences: kinematics fixes the onset and upper values for the zero-phonon edge, and the end of the window is a ratio of rates (13.3, 13.9).
- 1-5 l.106 → two adjacent cite commands: `\cite{nilsson1971phonon}\cite[Table~IV]{haxhijaj2026lattice}` → `\cites{nilsson1971phonon}[Table~IV]{haxhijaj2026lattice}`. The same applies at 13.7 l.28, l.48 and the fig:13-window-T caption.
- 1-6 l.106 → paragraph of about 380 words with three jobs (Ge onset, Ge zero-phonon side, the Γ route) → break after "…the measured TA branch." and again before "The route through the direct gap".
- 1-7 l.29, l.61 → sentences over 45 words that carry inline math → split at "that is," and at ", so the optimum".
- 1-8 register → "only" is at 57 per 10k words (L 11), "gives" at 40 (L 7), "so" at 30, "of order" at 3. Calibration: l.27 and l.47 read like Lin. l.43 does not ("Everything else about the window needs more than kinematics.") → "Beyond kinematics, three things are still needed: …".

### 13.2
- 2-1 l.3 → provenance (STYLE): "the amplitude at finite $\vect{q}$, with every path that contributes, is derived here." → end the sentence at the citation: "…near its gap~\cite[Sect.~VI]{kahn2022searches}." The section itself shows the derivation.
- 2-2 l.5 → preview paragraph (pattern 5/26): "We obtain four results." It lists five items, then every subsection restates them. The paragraph also says "four results" next to "four paths", which confuses → cut it, or reduce it to one sentence: "The four paths combine on shell into a one-electron band sum, do not interfere with the zero-phonon line, and reduce adiabatically to a frozen-phonon derivative."
- 2-3 l.18 → bare "transfer" (REGISTER term 6): "The transfer $\vect{q}$ is not folded" → "The momentum transfer $\vect{q}$ is not folded".
- 2-4 l.67 → App. D.35 cited twice in three sentences ("(\cref{app:D.35}). The general statement … is proved in \cref{app:D.35}") → keep the second.
- 2-5 l.69 → "Three conditions limit the theorem, and each matters later." The keyresult is titled "Phonon-assisted amplitude", not a theorem, and "each matters later" carries no fact → "The band-sum form \cref{eq:13.2-M} holds under three conditions." Name the theorem once ("the band-sum theorem") and use that name in 13.4, 13.6 and D.35–D.37, which already say "band-sum theorem".
- 2-6 l.71 → abstract opener (rule 18): "The theorem has a practical side." → "Keeping only empty intermediate bands gets the amplitude wrong by a factor of order one; \cref{we:13-exchange} finds 2.4 in a model."
- 2-7 l.115 → unclear referent: "and the binding one is the margin below the zero-phonon edge" → "and the tighter bound is the margin below the zero-phonon edge".
- 2-8 l.135 → paragraph of about 330 words with three jobs (error estimate, silicon numbers, chain check plus valence crossings) → break before "In silicon," and before "The same estimate disposes".
- 2-9 l.137 → the computational passage runs to about 250 words, where STYLE asks for a short passage pointing to App. E → keep the first two sentences and the last three; move the Sternheimer detail to App. E.5.

### 13.3
- 3-1 l.17 → provenance: "The rate and its loss-function form are derived here." → delete.
- 3-2 l.93 → provenance and novelty claim: "These exponents are derived here; to our knowledge they have not been given before." → delete. If a novelty claim is wanted, it belongs in the preface or Chap. 1 and should be stated once for the book.
- 3-3 l.7 → first-use definition: δ_w appears here ("$\omega \le E_{\mathrm{min}}(\vect{q}) - \delta_{\mathrm{w}}$") but is defined only at l.106 and in 13.6 → add at l.7: "with $\delta_{\mathrm{w}}$ the margin of \cref{sec:8.6}, \SI{0.3}{eV} in silicon (\cref{sec:13.6})".
- 3-4 l.106 → the bound is not labeled (editor note 13.6): "hold for $|\vect{q}| \le … = \SI{1.33}{keV}$" → "…\SI{1.33}{keV} for parabolic valleys (\SI{1.27}{keV} with the computed bands, \cref{sec:13.6})". Make the same change at 13.6 l.84 ("as \cref{sec:13.3} found for $|\vect{q}| \le \SI{1.33}{keV}$").
- 3-5 l.73 → "We call the power … the \emph{onset exponent}" (REGISTER item 11) → "The power of $x$ in $\bar S^{\mathrm{PA}}$ … is the \emph{onset exponent} $p_{\mathrm{on}}$."
- 3-6 l.50 (also 13.7 l.24) → "f-sum" in roman type, where 13.2, 13.8 and 13.9 write "$f$-sum" → "$f$-sum" throughout.
- 3-7 l.19 → restates 13.1 l.54, and the logic jumps ("At the millikelvin temperatures … already at \SI{1}{K}") → "At detector temperatures the transverse acoustic phonon of \SI{15}{meV} is unoccupied ($n_{\mathrm{B}} < 10^{-74}$ below \SI{1}{K}, \cref{sec:13.1})".
- 3-8 l.3 vs 13.2 l.137 → the seam repeats a phrase: 13.2 ends "Squared, summed over final states…", and 13.3 l.3 starts again "Squared and summed over the final states, it gives…" → in 13.3 l.3 write "Its square, summed over final states, enters the rate exactly as…".
- 3-9 register → "so" 36 and "gives" 39 per 10k words; no "we will/can/see". Calibration: l.73 ("Both powers are instances of one rule.") reads like Lin. l.21 does not ("On the expansion label $\mathfrak{T}$ of \cref{sec:8.5} the rate is quadratic…") → "In the expansion of \cref{sec:8.5} the rate is quadratic in the electron–phonon vertex, $n_g = 2$…".

### 13.4
- 4-1 l.92, l.94, l.96 → standalone scrub: the LaTeX environment name appears in prose: "The keyresult is therefore the familiar…", "The keyresult has two simpler forms.", "Outside the window the keyresult fails twice." → "\Cref{eq:13.4-Lscr} is therefore…", "\Cref{eq:13.4-Lscr} has two simpler forms.", "Outside the window \cref{eq:13.4-Lscr} fails twice."
- 4-2 l.3 → negation-stacked withholding (pattern 25): "Screening is not a small correction here. It is also not a single factor." → "Screening therefore cuts the rate by a factor of 30 to 50, and it enters at three places."
- 4-3 l.3 → provenance: "The screening of the final pair, the pair channel, is derived here; \cref{app:D.36} gives the steps…" → "\Cref{app:D.36} gives the steps at the random-phase level."
- 4-4 l.16 → rhetorical question and reveal (pattern 8): "How many factors of $1/\varepsilon$ survive once the local fields are kept? Exactly one." → "Exactly one factor of $1/\varepsilon$ survives once the local fields are kept."
- 4-5 l.74 → coined term that collides with an established one: "which we call the coherent-potential limit". "Coherent potential" is the CPA of alloy theory → "the applied-potential limit", without "we call".
- 4-6 l.116 → display not punctuated (lint missed it): `\frac23\Bigl(…\Bigr)^2\,\frac{…}{…}` is followed by "where the last ratio" → add "," at the end of the display.
- 4-7 l.122, l.128, l.141, l.147, l.150 → the same numbers appear three or more times (pattern 5/26). l.122 gives the worked example's factors before the worked example; l.128 repeats 3e-3 and 2e-3; l.150 restates l.124 ("a quarter to a third") and l.126 ("the two solvable limits span a factor of ten") → l.122: keep only the |q| dependence (10.2 → 6.1–6.6 → 3.2–3.7). l.128: keep. l.150: keep its three new facts (q-independence of the pair ratio untested, the excitonic ladder in 13.8, one combined factor in 13.9) and drop the rest.
- 4-8 l.74 vs l.126 → apparent inconsistency: l.74 says the two energies "differ by less than $10^{-3}$", while l.126 says the rigid limit changes the rate by "$2\times10^{-3}$" → l.74: "In silicon $\varepsilon_1$ differs by $1\times10^{-3}$ between the two energies, the rate by $2\times10^{-3}$".
- 4-9 l.74, l.126 → paragraphs of about 330 and 300 words → split l.74 at "In the second," and l.126 at "What is known".
- 4-10 register → "of order" 23, "therefore" 21 and "so" 34 per 10k words; no "however". Calibration: the l.72 picture ("The momentum of the pair channel is pinned.") reads like Lin. l.126 ("What is known is where the number comes from.") does not → "Where the number comes from is known."

### 13.5
- 5-1 l.3, l.33 (eq:13.5-limit), l.48, l.52 → convention break (editor note 13.4). After 13.4 l.92, $L^{\mathrm{PA}}$ means the screened loss function and $\varepsilon_2^{\mathrm{PA}}$ contains $\tilde M$, pair channel included. Yet 13.5 takes the limit of "$L^{\mathrm{PA}}$ of \cref{eq:13.3-LPA}" (the independent-particle value), and l.48 writes "$\varepsilon_2^{\mathrm{PA}}/(\varepsilon_1^0)^2$ plus the screening of the pair", which counts the pair channel twice in words → write $L^{\mathrm{PA}}_{\mathrm{IP}}$ (or "the independent-particle $L^{\mathrm{PA}}$ of \cref{eq:13.3-LPA}") in l.3, the keyresult and l.52. In l.48 drop "plus the screening of the pair". Add one sentence saying the identity holds for the screened pair as well (13.4 l.94 already states it).
- 5-2 l.105–112 → the keyresult box prints 2.6/1.9/1.5/1.3 and "more than a factor of two for $x < \SI{23}{meV}$". The next paragraph corrects these to 2.3/1.7/1.3/1.1 and 18 meV (editor note 13.5: decide or print a band). A key result should not be overridden in the text that follows it → print the band in the box: "2.3–2.6, 1.7–1.9, 1.3–1.5, 1.1–1.3 … (the lower values with the measured fall of branch strength), more than a factor of two for $x <$ 18–\SI{23}{meV}". Carry the same band into the Summary (S-2) and nuisance row l.166.
- 5-3 l.62 → missing word: "by 1.4 at \SI{36}{meV} and by 2 at \SI{17}{meV}" → "by a factor of 1.4 … and of 2 …".
- 5-4 l.65 → abstract opener: "The comparison separates what the limit tests." → "Over half an electronvolt the free-pair power two and the two measured branches hold with a single scale."
- 5-5 l.71 → "we call that spectrum" → "and that spectrum is $\alpha^0_{\mathrm{abs},\nu}(\omega)$".
- 5-6 l.112 → clumsy chain: "the dark-photon rate of silicon of \cref{sec:10.7-edge}" → "the silicon dark-photon rate of \cref{sec:10.7-edge}".
- 5-7 l.132 → anthropomorphic (pattern 15): "for three reasons that the optical data cannot see" → "for three reasons outside the reach of optical data".
- 5-8 cross-section → cold threshold 1.1875 eV (E_g(0) = 1.1692) against 6.5's 1.1883/1.1736 (editor note) → align book-wide at revision. In the prose, cut the reconciliation from 13.8's opener (8-1).
- 5-9 register → good: "however" is absent, but the contrasts are carried by "but" and "while". Calibration: l.92 ("One spectrum cannot fix two unknown functions.") reads like Lin.

### 13.6
- 6-1 title (lint) → a three-item list: "Soft phonons, resonances and the off-shell window" → "The off-shell window" (the window theorem is the section's index entry).
- 6-2 l.7 → anthropomorphic (pattern 15): "The electron--phonon vertex knows this only in part." → "The electron–phonon vertex reflects this only in part."
- 6-3 l.3 → negation framing (pattern 25): "The vanishing zero-phonon detunings are not harmless." → "The vanishing zero-phonon detunings set the boundary…" (merge with the next sentence).
- 6-4 l.29 → abstract opener: "The third use is negative, and it matters most." → "Inside the off-shell window the soft limit is never reached."
- 6-5 l.71 → unclear: "looks at first like the controlling one, and it would say otherwise" → "looks like the controlling parameter, and taken at face value it would forbid a margin of \SI{0.3}{eV}: …". This also settles the 8.5 conflict in the editor note: say once that 8.5's "θ_ep = 1 at 0.25 eV" is the bound, not the size.
- 6-6 l.110 → claim with no source: "Estimates give $|c^{\mathrm{F}}_\nu| \lesssim 0.3\,\varGamma_m/\delta_{\mathrm{F}}$" → state the estimate and its basis ("A model with … gives …"), or "We estimate … (\cref{app:E.14})".
- 6-7 l.57 → a sentence of about 55 words ("Above it, at fixed $(\vect{q},\omega)$, the resonance condition…") → split after "crosses that surface".
- 6-8 l.73, l.99 → paragraphs of about 380 and 300 words → l.73: break before "For the widths". l.99: break before "The rate of \cref{sec:13.3} continued".
- 6-9 caption fig:13-offshell → "Ref.~\cite{li2021deformation}". No other caption or paragraph uses "Ref." → "computed constants~\cite{…}".
- 6-10 register → "of order" 35 and "only" 37 per 10k words, the highest in the chapter. Calibration: l.21 ("Each term has a picture. The recoil term…") reads like Lin. l.84 ("There the book quotes only totals") speaks of "the book" in the third person → "There we quote only totals".

### 13.7
- 7-1 l.100 → process artifact (pattern 19): "An estimate of \cref{eq:13.7-sqrt} with a vertex half as large, \SI{0.12}{eV}, gives \SI{0.3}{meV} per band, below \SI{2}{meV} in total, which the direct calculation shows to be too small." It rebuts an internal estimate (CW1, editor note) that the book never states → delete. The Miglio sentence before it can stay, cut to: "Differences between methods, such as the \SI{9}{meV} between … \cite[Table~S2]{miglio2020predominance}, mix form and inputs and do not measure this correction."
- 7-2 l.100 → acronym not defined in the chapter: "both forms of AHC theory" (first use; l.48 writes it out) → "both forms of the Allen–Heine–Cardona (AHC) theory", or avoid the acronym.
- 7-3 l.58 → wrong verb: "For silicon the same convergence has been measured directly" → "computed directly". The same applies at 13.8 l.54 ("The two-pair sector can be measured in a model") → "computed".
- 7-4 l.36 → wordy opener (pattern 17): "The claim to be shown is that one configuration…" → "One configuration … reproduces \cref{eq:13.7-WL} as the supercell grows."
- 7-5 l.139 → pattern 26: the closing paragraph repeats 13.6 (0.09 at 300 K) and "the variation bounded above". Its only new fact is that the margin is measured from the edge at each temperature → fold that clause into l.106 and delete the paragraph. The section then ends on the worked example's "Reading", which is a consequence.
- 7-6 l.45 → a sentence of about 60 words ("For the higher even orders the reason is statistical: …") → split after "$(2N_{\mathrm{m}})^{1/2}$ for $N_{\mathrm{m}}$ modes."
- 7-7 l.24 → filler: "which is to be expected, since" → "since".
- 7-8 worked example we:13-windowT → "\emph{Reading.}" is an odd run-in label → "\emph{Consequence.}".
- 7-9 register → "since" at 20 per 10k words is the best in the chapter. Calibration: l.106 ("At detector temperatures the window does not move.") reads like Lin.

### 13.8
- 8-1 l.3 → a reconciliation sentence in the section opener (editor note 13.8/13.5): "and \SI{1.1736}{eV} with the rounded gap of \SI{1.17}{eV} used in \cref{sec:6.5}" → delete once the cold gap is aligned book-wide. Until then, move it to the figure caption.
- 8-2 l.116 → provenance and novelty: "The interband phonon-assisted channel at the indirect edge of an insulator, …, is derived here." → delete. The attribution sentence before it (Mitridate et al.) stays.
- 8-3 l.54 → a test written as a plan (pattern 19, and "nothing left to the reader"): "At $W = 0$ the two must agree…; at $W \ne 0$ their difference is the two-pair correction, to be set against $E_x^b/\Eg$. The diagonalization must contain the two-pair sector, … or the test only compares the formula with itself." → state it as the known gap: "A model with an exact two-pair sector would size this correction; App. E.15 specifies one." Cut the procedure.
- 8-4 WE l.121 → pattern 20: "$\alpha_{\mathrm{abs}} = 5.5\times\SI{325}{eV^{-2}.cm^{-1}}\times(\SI{0.0477}{eV})^2$". The reader cannot tell what 325 and 5.5 are without opening Ref. stanford2021 → give the fit form in book notation first ("their fit is $\alpha = A_{\mathrm{TA}}C(\omega - E_{\mathrm{g}}^{\mathrm{eff}} - \omega_{\mathrm{TA}})^2 + …$ with $C = …$ and $A_{\mathrm{TA}} = 5.5$").
- 8-5 title → two topics joined by "and" → "Exciton replicas and bosonic absorption".
- 8-6 l.97 → anthropomorphic: "An absorbed boson asks for the response at…" → "Absorption of a boson probes the response at…".
- 8-7 l.91 → paragraph of about 330 words → break before "The measured spectra test the shape."
- 8-8 register → calibration: l.99 ("The dark photon has no phonon-assisted amplitude of its own…") reads like Kahn and Lin. l.52 ("With the interaction the statement is not proven: …") → "With the interaction it is unproven, and it reduces to the size of the two-pair sector."

### 13.9 (sections)
- 9-1 l.13 → rhetorical question (pattern 8): "Why off the axis?" → "The joint minimum leaves the axis because, at $|\vect{q}| = 1.2$ to \SI{1.48}{keV}, the [100] axis is a local maximum…".
- 9-2 l.53 → novelty claim: "The allowed Umklapp line of silicon and its glide-parity origin are derived here; we are not aware of them in the dark-matter literature." → delete.
- 9-3 l.87, l.163, l.180, l.190 → wording that reports production status (pattern 19): "interim assignment", "interim factor" → "an assumed range", "an assumed factor".
- 9-4 l.108, l.180, l.184, l.188 → more status wording: "it has not been run", "it has been made once", "The onset is computed once.", "has been tested once" → state the scientific status: "No calculation of this control exists.", "the only completeness test so far", "The onset rests on one set of force constants.", "has been tested with one pseudopotential".
- 9-5 table:13-window → the block headers "Established" and "Open" do not match l.112 ("computed and checked" / "computed once or estimated"), and the status labels "computed, checked" and "computed once" read as an internal QA ledger → headers "Established" / "Estimated or open", matching l.112. Status labels: "two independent calculations", "one calculation", "symmetry, confirmed numerically", "estimate", "open".
- 9-6 l.108 → editor VERIFY: "with the L energy at room temperature, about \SI{1.71}{eV}~\cite{vurgaftman2001band}" is taken from recalled Varshni parameters → check the locator and add it (\cite[Table~…]{…}), or delete the sentence. The detector value does not depend on it.
- 9-7 l.106 → periphrasis (STYLE pattern 25): "Silicon does not tell us whether the germanium optimum leaves the axis." → "The silicon result does not settle whether the germanium optimum leaves the axis."
- 9-8 l.180 → pattern 26: it restates the table (two dominant rows, thresholds small). Its new content is that the measured edge cannot be divided by the external factor again (already said in 13.3 l.40 and 13.4 l.98) → reduce it to its first two sentences, or delete it.
- 9-9 l.184–194 (Open problems) → pattern 26 at the end of a subsection: l.184 repeats l.81 and 13.1, l.186 repeats l.102, l.190 repeats l.87 → merge into one paragraph that names each open item and its App. E pointer, one clause per item. Keep l.194 (the measurement), with a concrete opener (9-10).
- 9-10 l.194 → vague opener: "Above these stands a measurement." → "One measurement would test the chain directly: the cold absorption edge of silicon within \SI{25}{meV} of threshold, never measured at millikelvin temperatures…".
- 9-11 l.85 → paragraph of about 340 words → break before "The weakest step is the form factor."
- 9-12 l.85 → "which we quote as a factor of ten" with no reason → "which we round up to a factor of ten to cover the correlated inputs".
- 9-13 register → "only" 45 per 10k words. Calibration: l.89 ("Take a background-free exposure of \SI{1}{kg.yr}…") reads like Lin. l.102 ("The estimate therefore reads as follows.") → cut, and start with "The phonon-assisted rate leads…".

### Summary (s13-9 l.196–212)
- S-1 l.204 → wrong number: "The external factor is one inverse macroscopic dielectric function …, $1/40$ to $1/48$ in the loss function". 1/40–1/48 is the head-only value. The macroscopic factor that 13.4 l.24 says survives is 1/30–1/38 (13.4 WE l.141; nuisance row l.162) → "$1/30$ to $1/38$".
- S-2 l.206 → "more than a factor of two within \SI{23}{meV}" ignores the branch-strength correction (18 meV) → "within 18 to \SI{23}{meV}" (see 5-2).
- S-3 l.198 → units typed as text: "0.3374 MeV for the free pair, 0.3332 for the exciton replica" → `\SI{0.3374}{MeV}`, `\SI{0.3332}{MeV}`.
- S-4 l.212 → figurative (pattern 25): "the electron density, which is blind to spin" → "the electron density, which does not act on spin". Also "Germanium and GaAs await their bands." → "Germanium and GaAs need quasiparticle band calculations."
- S-5 l.206 → "by a Ward identity of the second-order amplitude". 13.5 calls it the continuity identity (it is labeled eq:13.5-ward but never called a Ward identity) → "by the continuity equation applied to the second-order amplitude", or name it once in 13.5.
- S-6 accuracy, checked against the final sections (editor item): the 13.7 paragraph (46 meV, 0.324→0.337, 8 meV, ≤0.002 MeV) and the 13.8 paragraph match. The 13.6 bound is correctly labeled 1.33/1.27. Apart from S-1 and S-2 the Summary is accurate. Length (about 1,200 words) is acceptable for a chapter of about 34,000 words.

### Appendices
- D35-1 title → repeats the chapter title "Phonon-assisted electron recoil" → "Band sum and adiabatic form of the phonon-assisted amplitude", or "The phonon-assisted band sum".
- D35-2 l.3, D36-1 l.3, D37-2 l.3 → abstract openers ("This appendix proves the statements…", "This appendix derives…") → start with the result: "Two one-body vertices acting on a Slater determinant pass only through one-pair intermediate states; on the energy shell the hole paths become the Pauli-blocked electron paths. We prove this and…". Lower priority than the main text.
- D37-1 title (lint) → "The soft acoustic limit of the phonon-assisted amplitude" → "The soft acoustic limit".
- D37-3 l.84 ("A check in one dimension") → duplicates we:13-soft (pattern 26) and disagrees with it in one detail: D.37 says the identity holds "at $|\vect{Q}| = 0.1$ and $0.25$ of $2\pi/a$", while the worked example reports 0.10 only → replace the subsection with one sentence pointing to \cref{we:13-soft}, or add the 0.25 point to the worked example.
- D37-4 l.93 → closing aphorism (pattern 25): "a long acoustic wave is a translation, and a translation is not emitted." → "since the squared amplitude grows only as $1/|\vect{Q}|$."
- D35, editor note → overfull boxes at l.34–38 and 74–75 belong to the figure/layout check, not prose. They were not checked here.

## 3. Cross-cutting checks

- **Equation punctuation**: correct throughout, except 13.4 l.116 (4-6).
- **First-use symbols**: δ_w (3-3) and AHC (7-2). The other symbols (ς, ϰ_ν, 𝒲_x, ξ_C, M_eh, ℓ_Qν) are defined at first use.
- **Captions**: all standalone, with quantity, units and parameters. Minor: map caption "Side objects" (O-5); "Ref." in fig:13-offshell (6-9).
- **Citations**: numeric with equation locators where a formula is used. Combine adjacent \cite commands (1-5). Values taken from a source without a locator: macfarlane1958fine (18.27 meV, 13.1 l.77; 20 K absorption, 13.9 l.85), knapen2021dark (13.4 WE mesh values), vurgaftman2001band (9-6) → add Table/Fig. locators.
- **Cross-references**: \cref used throughout; no hard-coded numbers. Subsection labels such as sec:8.4-lines and sec:10.5-rules exist book-wide and are acceptable.
- **Standalone scrub**: no banned terms. Leaks: "keyresult" (4-1), production-status wording (9-3, 9-4, 9-5), and the rebuttal of an internal estimate (7-1).
- **User rules**: no exercises or checkpoints, and nothing left to the reader, except the planned test in 13.8 (8-3). Limit Checks 13.5a and 13.7a comply: formula with a one-line citation, comparison plot, one sentence on what breaks down; prose refers to them by \cref. Background is succinct. The chapter opening is motivational, with too many orienting sentences (O-3).
- **Pattern 25** (every opener and caption, sentence by sentence): hits at O-2, 4-2, 6-3, 1-2, 9-7, S-4 and D37-4. Section openers 13.1, 13.2, 13.3, 13.5, 13.7, 13.8 and 13.9 start on a concrete number or physical fact and pass. Captions are clean.
- **Pattern 26** (new facts per paragraph): flagged paragraphs are 1-3, 1-4, 2-2, 3-7, 4-7, 7-5, 9-8, 9-9 and D37-3. Every other paragraph adds at least one fact, number or step. The subsection-ending paragraphs at 13.1 l.43, 13.4 l.150 and 13.7 l.139 match the pattern of the first known case (Sect. 1.3.1).
- **Provenance and novelty sentences** (STYLE): ch13 l.2, 13.2 l.3, 13.3 l.17, 13.3 l.93, 13.4 l.3, 13.8 l.116, 13.9 l.53. That is seven, one per writer. Cut them all. If the book wants novelty claims, put them in one place.

## 4. Chapter as a whole

- **Opening outline paragraph**: motivational and concrete (1.94 keV, 0.4 MeV, 64 meV), and not a section list. It fails "at most one orienting sentence" (O-3) and carries a provenance clause (O-1).
- **Summary**: one paragraph per section block, in order, each with its numbers. Two numbers are wrong or stale (S-1, S-2).
- **Redundancy across sections**:
  - (a) The light-versus-dark-matter momentum contrast ("a photon's phonon must supply all of $\vect{k}_{\mathrm{c}}$; dark matter supplies $\vect{q}$ itself") appears in the ch13 opening, 13.1 l.77, 13.2 l.3, 13.5 l.3 and 13.5 l.132 → keep 13.1 l.77 and 13.5 l.132; cut the 13.2 and 13.5-opener versions to a clause.
  - (b) "The amplitude is of second order, one density vertex and one electron–phonon vertex" appears in the ch13 opening, the map caption, 13.2 l.3 and the Summary → drop it from the opening (O-3).
  - (c) The three-excitation final-state picture (hole at the valence-band maximum, electron at the valley, TA phonon carrying about 1 keV) opens both 13.2 and 13.3 → open 13.3 on what is new: "Summed over final states, the squared amplitude of \cref{sec:13.2} is a structure factor…", keeping the 1.22 eV vs 1.77 eV numbers.
  - (d) The n_B values of 13.1 are repeated in 13.3 l.19 and 13.7 l.106 → cite them instead.
  - (e) The 8.6 additivity prescriptions are restated in 13.3 l.40, 13.4 l.98 and 13.9 l.180 → keep 13.3.
- **Order**: δ_w is used in 13.3, 13.4 and 13.5 before 13.6 fixes it. With 3-3 in place, a forward pointer is enough. Moving 13.6 to follow 13.3 would also work, but changes the map and labels.
- **Seams** (each adjacent pair read across the join):
  - 13.1→13.2: good ("it begins with the amplitude of \cref{sec:13.2}" → onset numbers).
  - 13.2→13.3: duplicated "Squared and summed" (3-8) and a duplicated final-state picture (c).
  - 13.3→13.4: 13.3 ends by pointing to 13.9, then 13.4 opens on screening with no bridge → add one clause to 13.3's last paragraph, or open 13.4 with "The loss function of \cref{sec:13.3} uses the bare density vertex. At \SI{1}{keV} …".
  - 13.4→13.5: acceptable; 13.4 l.150 mentions the edge calibration that 13.5 takes up.
  - 13.5→13.6: abrupt. 13.5 ends on App. E.5 controls; 13.6 restarts from 1.77 eV. Add a bridging clause: "Every result so far assumed the off-shell window; its boundary is fixed here."
  - 13.6→13.7: good, with an explicit hand-over.
  - 13.7→13.8: acceptable. Both are concrete, but there is no link. Optional: 13.8 could open "The \SI{14.7}{meV} by which the pair binds lowers every threshold of \cref{sec:13.7}…".
  - 13.8→13.9: good (13.8 l.93 points to 13.9).
- **Register calibration** (REGISTER Sect. 6; 2–3 passages per section, recorded above under each section): the chapter keeps the models' sentence length and terms of art (heavy/light mediator, momentum transfer, reach, exposure, background-free, phonon-assisted, kinematic floor). Measured per 10k words:
  - It lacks the models' connectives: "however" 0–3 (L 8), "we will/can/see" 0–3 (L 25+), "typical" 0 (L 15).
  - It overuses its own tics: "only" 23–57 (L 11), "gives" 9–40 (L 7), "of order" up to 35 in 13.6 (L 0), "so" up to 36.
  - Each section needs a few connective sentences of the kind given in 13.1, 13.3, 13.4 and 13.9 above; no rewrite is needed.

## 5. Editor-notes items that concern prose

- GaAs window 0.433 to 0.517–0.560 MeV: closed in 13.1 and 13.9. 13.9's room-temperature 1.71 eV sentence remains VERIFY (9-6).
- δ_w = 0.3 eV: confirmed in 13.6. 13.3 needs the first-use definition (3-3). |q| bound 1.33 (parabolic) vs 1.27 (computed bands): labeled in 13.6, the Summary and the nuisance row, but not in 13.3 l.106 or 13.6 l.84 (3-4).
- Zero-phonon edge 0.60 vs 0.73 eV: both labeled in we:13-onset-exp. Done.
- Pair mass 1.19 mₑ: used consistently in 13.1, 13.3 and 13.6. Done.
- 13.5 temperature factors: both sets are printed, but the keyresult shows only one (5-2). The "TA-only upper bound" wording was softened. The spurious ≈1.4 cm⁻¹ residue is stated. The cold threshold 1.1875 vs 1.1883 needs book-wide alignment (5-8).
- L^PA / ε₂^PA screened convention from 13.4 on: not followed in 13.5 (5-1).
- 13.8 excitonic threshold 1.1736 vs 1.1728: the reconciliation sits in the opener (8-1). Align book-wide. N7 narrowed: 13.8 l.116 still has an "is derived here" claim (8-2).
- ZPR 8 meV vs ≲2 meV: resolved in 13.7, but the rebuttal of the ≲2 meV estimate is still in the text (7-1).
- Joint minimum 1.29 vs 1.33 keV in the 13.7 caption: aligned to 1.33. Done.
- Recheck the Summary paragraphs for 13.7 and 13.8: they match (S-6). The screening and 77 K numbers do not (S-1, S-2).
