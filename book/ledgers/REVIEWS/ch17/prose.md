# Ch17 prose review (style and prose, isolated)

Scope: ch17.tex (opening, map), s17-1 to s17-6, s17-summary. Checked against STYLE.md, style-guide.md, prose-review.md (patterns 0-26), REGISTER.md, editor-notes.md. Line numbers are per file. The tex was not edited.

## Verdicts

| Unit | Words | Verdict | Main reasons |
|---|---|---|---|
| Chapter opening (ch17.tex) | ~400 | REVISE | The second paragraph is a three-item outline, and the measurement disclaimer is stated as a negation |
| 17.1 Scattering across channels | 3,230 | REVISE | Outline sentences in the opener, two looped paragraphs, "only"/"about"/"therefore" at 5-10x the register rate, British "labelled", σ_n vs σ_p, run-in "Open problems" heading used only here |
| 17.2 Absorption across channels | 2,985 | REVISE | Periphrasis in the opener ("answers", "asks for"), undefined $\tilde c$ and $\gamma_{\mathrm{L}}$, a Ch10 caveat restated at length, YIG dark-photon point with no derivation line |
| 17.3 Exothermic and inelastic DM | 2,960 | REVISE | Title, one unpunctuated display, undefined $\Delta S$, $\bar L$, $q_\Delta$, a looped closing paragraph, "kilogram-year" against the chapter's "kilogram and year" |
| 17.4 Interference between channels | 2,990 | REVISE | $n_B$ clash with $n_{\mathrm{B}}$ of 17.2, $\theta_{\mathrm{ep}}$ undefined, forward-teaser paragraphs, the worked example repeats the GaAs numbers of 17.4.1, one looped paragraph |
| 17.5 Figures of merit per channel | 4,320 | REVISE | Subsection 17.5.7 is a recap (pattern 26), the polar subsection restates Ch11, process sentences in the sound-speed audit, straight quotes, undefined $\kappa_\eta$, $Z_{\mathrm{val}}$, $L_{\mathrm{Mig},\kappa}$ |
| 17.6 Ranking under uncertainty | 3,910 | REVISE (borderline REWRITE in 17.6.1 and 17.6.5) | 190-word opener with self-narration, process artifacts in the pool paragraph, CaWO$_4$ tensor repeated from 17.5, two looped paragraphs, "tier" used 42 times, a caption that disagrees with the text |
| Summary | 1,760 | REVISE | The 17.4 and 17.5 recaps share one paragraph, a process sentence, "6 %" against 17.5's "7 %", $L(\vect{k},\omega)$ against $L(p,\omega)$ |

None of the 48 lint hits is blocking. Lint hits per file: s17-1 4 (all LONG-SENT); s17-2 2 (one DASH, a false positive inside a table preamble; one LONG-SENT in a caption); s17-3 9 (TITLE l.1, EQ-PUNCT at the `cases` display, 7 LONG-SENT); s17-4 2 (EQ-PUNCT at eq:17.4-Sek is a false positive, since the sentence continues with "with the zone averages"; one LONG-SENT in the keyresult); s17-5 7 LONG-SENT; s17-6 11 LONG-SENT; summary 13 LONG-SENT (5 in table rows, so false positives). The real long sentences are listed under each section.

## Register calibration (REGISTER.md Sects. 4, 6; per 10k words, Lin in brackets)

| | 17.1 | 17.2 | 17.3 | 17.4 | 17.5 | 17.6 | Summ. |
|---|---|---|---|---|---|---|---|
| only (11) | 59 | 37 | 27 | 60 | 60 | 33 | 51 |
| so (11) | 31 | 10 | 27 | 20 | 28 | 36 | 23 |
| therefore (3) | 19 | 7 | 7 | 10 | 9 | 8 | 0 |
| about (5) | 50 | 17 | 14 | 10 | 19 | 20 | 28 |
| gives (7) | 15 | 17 | 37 | 23 | 35 | 15 | 34 |
| however (8) | 0 | 0 | 0 | 7 | 5 | 5 | 0 |
| we will/can/see/have/find (40+) | 3 | 0 | 0 | 3 | 0 | 0 | 0 |
| since (14) | 0 | 7 | 0 | 7 | 19 | 3 | 0 |
| of order (0) | 0 | 7 | 14 | 10 | 0 | 3 | 0 |

The chapter keeps the book-wide tics: "only" runs at 3-5x Lin's rate, "about" at up to 10x in 17.1, and "gives" at 5x in 17.3 and 17.5. It also lacks the register's connective tissue: zero "however" in 17.1-17.3, almost no "we will/can/see", and no "since" in 17.1 or 17.3. No "thereby", "whereby", "respectively", "in order to", "i.e." or "e.g." occurs. The six writers' voices are close on the page. The differences: 17.6 takes up order-theory vocabulary (antichain, interval order, height, tier); 17.4 is the most formal; 17.1 alone uses a run-in "Open problems" heading; 17.3 writes "per kilogram-year" (7 times) where the rest write "per kilogram and year"; 17.5 writes km.s$^{-1}$ where 17.1 and 17.6 write km/s.

Calibration (two or three passages per section were read; one rewrite per section is shown in the issue list, marked CAL). The passages that pass as Lin: 17.4 l.3 ("It can push the electrons… whose electrons lag behind"); 17.3 l.34 (the incoherent-limit reading, $\nd\sigma v_\nu$); 17.2 l.93 (the three readout regimes). The ones that fail: 17.1 l.15 (a method paragraph), 17.5 l.168 (a recap), 17.6 l.3 and l.31 (a frame and a catalogue).

## Chapter opening (ch17.tex)

1. l.4 → pattern 18 and STYLE "openings are not outlines": "This chapter answers that question at the level of the response. It reads the atlas… The outcome is a map…, a short list of material numbers…, and a ranking…" is a frame followed by a three-item outline. → Keep one orienting sentence: "Read along the interaction axis, the atlas of \cref{chap:9} gives, for each coupling, the channel that dominates at each mass and threshold, the few material numbers that set its rate and reach, and how firmly those numbers rank materials." Delete "This chapter answers… response."
2. l.4 → pattern 25 (negation first): "A ranking of responses does not decide which experiment to build. The energy needed to create one quantum, the readout and the backgrounds decide that, …" → "Which experiment to build also depends on the energy per quantum, the readout and the backgrounds, which the guide to next targets combines with these rankings (\cref{sec:21.7})." This is the first of five statements of the measurement-side disclaimer (see Cross-chapter, item C1).
3. l.2 → redundancy: the hook numbers (17 events, $8\times10^5$) come back in 17.1 l.50 and in the summary. That is acceptable for an opening hook, but 17.1 l.50 should then point back rather than restate ("the factor $5\times10^4$ of the opening").
4. Caption of fig:17-map → it stands alone and carries no new numbers. PASS.

## 17.1 Scattering across channels

5. l.3 → too many moves in the opener: "We put the scattering rates… We draw the map… explain each boundary… and then say how the map changes…" is four sentences of plan after a good concrete start. → Merge them into one: "We will draw that map for silicon, explain each boundary by kinematics or screening, and then follow it into germanium and GaAs."
6. l.3 → wordy: "Where such changes happen, for each coupling, is what a target and a threshold must be chosen against." → "A target and a threshold are chosen against where these changes happen."
7. Title of 17.1.1, "Sectors and their kinematic ceilings" → pattern 21 ("X and its …"). → "Kinematic ceilings of the sectors".
8. l.7 → hyphenation: "cross section" (twice) against "cross-section" in 17.3 l.86; REGISTER Sect. 7 fixes the hyphen. → "cross-section" throughout.
9. l.7, l.20, l.28, l.39 against 17.3 caption l.82 and 17.5 eq:17.5-cNR1 → one quantity under two symbols: 17.1 writes $\sigma_n$ per nucleon and 17.3/17.5 write $\sigma_p$. The editor notes also record a clash of $\sigma_n$ with the conductivity of 15.4. → Use $\sigma_p$ in all of Ch17 (as Ch11 does), or define the relation once.
10. l.11 → the closing paragraph line "The two maps below make both factors visible." fails the deletion test (pattern 0). → Delete it.
11. l.15 → pattern 18 recap opener: "For a nucleon coupling every rate of the map comes from a result already derived." → Open with the content: "The nucleon-coupling map uses four responses: the long-wavelength acoustic form \cref{eq:11.1-Sac} below $q_{\mathrm{BZ}} = \SI{2.25}{keV}$, …"
12. l.15 → British spelling "labelled" → "labeled".
13. l.15 against the caption of fig:17-sectors (l.20) → the labeling criteria (one phonon versus two or more phonons, the free-recoil median above \SI{92.5}{keV}) appear in both. Keep them in the text and shorten the caption to the symbols, or the reverse.
14. l.15 → CAL. "By the sum rule of \cref{eq:12.4-harm} it holds at every momentum transfer, and the lattice enters only through energy conservation, which we impose with the mean lattice energy $q^2/2M$, so that the deposited energy is $\omega_e + q^2/2M$." → As Lin would write it: "Since the sum rule \cref{eq:12.4-harm} holds at every momentum transfer, the lattice only has to conserve energy, and we let it take its mean share, $q^2/2M$."
15. l.24 → sentence length: "Multiphonon deposits take over above \SI{20}{MeV}… and above about \SI{22}{MeV} at higher thresholds." (52 words; two crossovers with four numbers) → Split at the semicolon.
16. l.28 → pattern 19: "the value at \SI{100}{MeV} is the one of \cref{sec:12.3}" is a consistency assurance. → Delete it.
17. l.31 (WE) → first use: "the recoil parameter is $x_R = 1.31$" gives no definition, and $\langle u_x^2\rangle$ is also new. → Add "$x_R = E_R/\langle\omega\rangle$" (or the book's definition) with a pointer to \cref{sec:11.4}.
18. l.42 → pattern 26: "A silicon calorimeter with a threshold between about 0.3 and \SI{35}{eV} therefore sees… only through ionization" restates the fig:17-sectors band and l.26. → Keep only the new fact: "A charge readout at the single-electron level records these events with no lattice background from the dark matter itself." Then merge that sentence into l.28.
19. l.46 → pattern 18 count-teaser: "An electron coupling reaches three sectors of silicon." → "An electron coupling reaches the zero-phonon, phonon-dressed and electron-following sectors of silicon."
20. l.50 (end) → pattern 26: "A nucleon coupling is unscreened at phonon energies in silicon for the same reason… (\cref{sec:8.4})" restates l.11 ("The nucleon coupling is not screened at phonon energies in a crystal whose Born charges vanish"). → Delete one of the two. The l.50 version carries the reason, so keep it and cut the l.11 clause.
21. l.54 → wordy: "We have not computed the germanium crossover, because the book has no germanium phonon density of states beyond the Debye estimate" is also repeated in Open problems (l.80). → Keep the Open-problems version and cut the l.54 sentence.
22. l.56 (end) → pattern 26: "The same crystal thus has a lattice sector below the gap that is large for a dark photon and small for a nucleon coupling, the reverse of silicon, …" recaps the paragraph. → Delete it. The summary already carries it.
23. l.56 → number given twice: "\SI{10.4}{keV}" (here and in tab:17-boundaries) against "\SI{10.35}{keV}" in 17.3 l.3, tab:17-endo, 17.5 and tab:17-rank. → Use 10.35 throughout.
24. l.56 → a long sentence of 50+ words ("Its vertex on the optical phonon at small $q$ is set by the difference of nucleon number per mass…"). → Split it after "per u".
25. l.59 caption of tab:17-boundaries → not standalone: "Status as in \cref{tab:13-window}." → "Status: computed (one or two calculations), measured data, or estimate, as marked in each cell."
26. l.80 → voice: `\paragraph{Open problems.}` occurs only in 17.1; 17.2-17.6 fold their open problems into prose. Also "Three inputs limit the maps." is a count-teaser. → Drop the run-in heading and open with the first input: "The maps are limited first by the electron-following sector of an electron-only coupling, known in silicon only as the long-wavelength model of \cref{sec:10.2}."

## 17.2 Absorption across channels

27. l.3 → pattern 25 (periphrasis): "of which material answers at each mass and how much of its answer the medium screens". → "of which material absorbs at each mass, and by how much the medium screens it."
28. l.7 → anthropomorphic opener: "Each boson asks for one response function at that point." → "Each boson probes one response function at that point."
29. l.14 → first use: $\gamma_{\mathrm{L}}$ in "$L = 2\mathcal{I}_{\mathrm{pol}}/\pi\gamma_{\mathrm{L}}$" is undefined in Ch17. → Add "with $\gamma_{\mathrm{L}}$ the width of the longitudinal line".
30. l.14 → CAL. "The large values of $L$ sit where $\varepsilon_1$ crosses zero, at the longitudinal modes." This passes. "The deepest minima of the dark-photon reach curves are longitudinal modes." is good Lin, but l.55 repeats it (next item).
31. l.55 (end) → pattern 26: "The strongest dark-photon targets are the phonon lines of polar crystals and the plasmon of silicon, both longitudinal modes at a zero of $\varepsilon_1$" restates l.14. → Keep only "with $\zeta \approx 10^{-17}$ for three events in a kilogram-year" and attach it to l.14.
32. l.18 → Ch17 restating a home chapter at length (brief item): "For the silicon optimum two caveats of \cref{sec:10.7-alp} apply. The measured $\sigma_1$ belongs to singlet pairs… must be computed separately." takes three sentences. → One clause: "the measured $\sigma_1$ understates the triplet response near the peak by about a fifth, and spin–orbit coupling breaks the factor $\frac34$ in heavier crystals (\cref{sec:10.7-alp})."
33. l.20 → first use: $\tilde c$ in "$\zeta^2$ replaced by $\tilde c^2m_e^2\langle v^2\rangle/e^2$" is undefined. → Name it: "the coupling $\tilde c$ per unit mass of \cref{eq:12.6-absrate}".
34. l.29 caption and l.43 table → editor ruling on the YIG dark-photon point ($\zeta = 7.6\times10^{-17}$, "vacuum $\zeta$"): the 17.2 text gives no derivation line. If the point stays, 17.2 must state the substitution in one sentence (the 14.3 axion result with $g_{aee}$ replaced by…). If not, drop it from the caption and the table (pattern 20: the reader cannot reproduce it).
35. l.57 → number style: "The scalar has the fewest:" is a colon-reveal (pattern 8). → "The scalar has two targets: …"
36. l.91 → pattern 19 or 20: "Lamoreaux and collaborators compared the two readouts with Poisson statistics… the bunched variance extends the comparison to every occupation." This is legitimate as a fact about the literature, but it reads as provenance. → One clause in the keyresult note: "(the Poisson treatment of \cite[Eqs.~(12)--(14)]{lamoreaux2013analysis} is the $n_{\mathrm{B}} \ll 1$ limit)".
37. l.95 → pattern 26 (mild): "A coherent detector therefore overtakes a counting detector below a mass of the order of the temperature" restates l.93 ("For $m_\phi \approx T$ the gain is modest"). The new facts are \SI{210}{MHz} and the gray band. → Open with them: "The gray band of \cref{fig:17-abs-coverage}, $m_\phi < T$ (\SI{0.86}{\micro eV}, \SI{210}{MHz} at \SI{10}{mK}), is where the field must be read."
38. Seam from 17.1 → 17.2 → the jump from scattering maps to absorption has no bridge clause. → Start l.3's fourth sentence with "Unlike scattering, absorption leaves no kinematic freedom: …"

## 17.3 Exothermic and inelastic dark matter across channels

39. l.1 → title (lint TITLE): "Exothermic and inelastic dark matter across channels" is a doubled noun (exothermic is a subset of inelastic) and runs to six words. → "Inelastic dark matter" or "Inelastic scattering into collective modes".
40. l.3 → outline tail: "One formula covers all the modes, and the dispersion of each mode decides… We then compare… and close with…" → Keep the first sentence. Replace the second with "We will then compare the electronic and lattice channels of silicon and the endothermic thresholds."
41. l.12 → symbols in the weight formulas are not defined here: $A_\kappa$, $c_4$, $F^{\mathrm{mag}}$, $w^{\mathrm{M}}_{\vect{q}}$. → Add "in the notation of" with the equation labels, as was done for \cref{eq:14.1-contract}, for each.
42. l.23 → sentence length (lint): "Writing $\dd^3q = …$, the radial integral picks up… and the rate of one particle… is …:" runs about 70 words with two inline formulas. → Split it: "The radial integral then picks up $q_\nu^2/(q_\nu/\mchi + u_\nu)$ at each root. Summed over branches and directions, the rate of one particle is"
43. l.32 → pattern 26 (mild): "The rate per particle does not depend on its velocity, so the halo drops out of \cref{eq:17.3-rate} except through $\rho_\chi$." restates the keyresult. → Start at "At finite $\vect{v}$ the surface…"
44. l.34 → first use: "its zone average $1 + 2\Delta S = 1.156$". $\Delta S$ is undefined in Ch17. → "with $\Delta S$ the zero-point spin reduction of \cref{we:14-nio}".
45. l.54 → sentence length: the NiO sentence ("In NiO at \SI{0.1}{MeV}… more than the line energy.") has about 60 words. → Split it after "over directions".
46. l.56 → negation tail: "… and not a resonance of down-scattering." → Make it positive: "The uniform precession of \cref{sec:14.3} is therefore the end point of the exothermic spectrum, where the halo speeds take over from the splitting." This also settles the editor note on the 14.3 promise in prose. The closure is still in words only, which is accepted.
47. l.63 (WE) → first use: "With this line in place of $\bar L$" ($\bar L$ is defined in 10.9, not here). → "in place of the averaged loss function $\bar L$ of \cref{eq:10.9-shell}".
48. l.82 caption → $\sigma_p$; see item 9.
49. l.86 → "each at its reference cross-section" is the one hyphenated form in the chapter. Keep it and change the others.
50. l.88 → sentence length: "The residual does not come from the halo speeds…, but from the condition on the weight…" has 55 words and negation-first. → "The residual comes from the condition on the weight in \cref{eq:17.3-rate}, not from the halo speeds (whose correction is $\le 0.34$): the one-phonon weight varies on the scale $q_{\mathrm{BZ}} = \SI{2.25}{keV}$, smaller than $\mchi v_{\mathrm{max}}$."
51. l.90 → first use: "$q_\Delta^3\bar L$" ($q_\Delta$ is undefined in Ch17). → Write "$q_\nu^3\bar L$" if that is meant, or define $q_\Delta$ with a pointer to 10.9.
52. l.90 (end) → pattern 26: "The comparison at fixed splitting therefore turns on what the detector records… With an electronic coupling, the splitting becomes visible energy. With a nucleon coupling, it becomes kinetic energy…" restates l.88 ("The deposited energy does not follow the splitting") and the start of l.90. → Cut it to one sentence: "With an electronic coupling the splitting becomes visible energy; with a nucleon coupling it goes into the outgoing particle, and the phonon deposit stays below \SI{64}{meV}."
53. l.92 → CAL. "The two are different models, the gas with an undamped pole and the crystal with a broad loss peak, and the comparison says only that the plasmon is a minority share…" → As Lin would write it: "Of course the two are different models, an undamped pole in a gas against a broad loss peak in a crystal; the upshot is only that the plasmon is a minority share of exothermic electron recoil even where it is open."
54. l.101 → a literal Unicode en dash in "electron–hole". → "electron--hole".
55. l.106 → equation punctuation (lint EQ-PUNCT): eq:17.3-endolin ends with "otherwise ," and the next sentence starts "At $\Delta_\chi = 0$…". → Change it to a full stop.
56. l.3, l.82, WE → units phrasing: "per kilogram-year" in 17.3 against "per kilogram and year" everywhere else. → Use one form chapter-wide.

## 17.4 Interference between channels

57. l.3 → this passes as an opener (concrete, a plain physical picture). The four-item "We will derive…, find…, bound…, and fix…" is acceptable as one "we will" sentence.
58. l.7 → "For a dark photon the three cells of $S_{e\kappa}$ differ in size by more than three orders of magnitude." This is a count-teaser of size. Acceptable, since it is quantified.
59. l.9, l.13 against the WE (l.99, l.101) → redundancy inside the section: the GaAs numbers (99.75/99.81 %, 216/245, $4.83$-$4.88\times10^{-4}$, $Z/M = 0.4446$/$0.4405$) appear in 17.4.1 and again in the worked example. → Keep the general statement and the silicon numbers in 17.4.1, and move all GaAs numbers to the WE (or the reverse).
60. l.11 → the line "This is the ionic correction to the zero-phonon line." is good; it names the thing. PASS.
61. l.32 → symbol clash: "Born--Oppenheimer order $n_B = 1$" against $n_{\mathrm{B}}(m_\phi)$, the Bose occupation of 17.2 (eq:17.2-ratio). → Use the Ch8/Ch12 symbol for the BO order if one exists. Otherwise write "at first Born--Oppenheimer order" without a symbol, here and at l.43.
62. l.47 → first use: "unique to relative order $\theta_{\mathrm{ep}}$" ($\theta_{\mathrm{ep}}$ is undefined in Ch17). → Add "the window parameter $\theta_{\mathrm{ep}}$ of \cref{sec:8.6}".
63. l.51 → count-teaser: "The cross term is absent from the rate in four cases." It names them one by one afterward, so it is acceptable. Trim "The first is the one already met:" to "First,".
64. l.57 (end) → pattern 22: "That limit is the content of the next subsection." → Delete it.
65. l.59 → forward teaser plus loop (pattern 26): "Couplings in proportion to mass… are a different case. Their cross term does not vanish. It cancels the other two terms, as the next subsection shows." The same content is stated at l.83. → Delete the paragraph.
66. l.85 → CAL. "There the phonon-assisted amplitude itself departs from its optical limit by a factor of order one (\cref{sec:13.5}), with a dipole extrapolation five to twenty times larger in rate" → As Lin would write it: "The trouble is that the window lies at 0.4-0.6 of $2\pi/a$, where the phonon-assisted amplitude is already off its optical limit by a factor of order one, so the relation sets only the scale of the cross term."
67. l.94 → pattern 26: "Both windows lie between a fifth and three fifths of the way to $2\pi/a$, where \cref{eq:17.4-lock} sets the scale of the cross term but not its value." restates l.85. → Delete it.
68. l.110 → pattern 26 (partial): "For such a mediator the electronic sectors at small $q$ see only the combination $\tilde V_e - (m_e/M_\kappa)\tilde V_{\mathrm{nuc}}$…, which vanishes for couplings in proportion to mass" restates the keyresult and l.83. The new facts are $M_\kappa/m_e = 5.1\times10^4$, 1823, and "computed separately and added miss it by the full cross term". → Keep only those.
69. Caption of fig:17-interference → standalone and long, but acceptable. "a model that lies \SI{0.13}{eV} above the computed bands at \SI{1}{keV}" is good practice.

## 17.5 Figures of merit per channel

70. l.3 → pattern 18 or 22: "This section derives one figure of merit per channel, its window and its inputs, and collects them in \cref{tab:17-fom}." → "We will derive one such number per channel, with its window and inputs (\cref{tab:17-fom})."
71. l.3 → the second instance of the measurement-side disclaimer ("The energy needed to create one quantum ranks quanta, not rates…"). → Delete it (see item C1).
72. l.7 → count-teaser: "Two kinds of number appear." → "A figure of merit is either a reach number or a rate number."
73. l.14 → "The tolerance is a convention, chosen to match the accuracy of most inputs." Acceptable. "and \cref{sec:17.5-phonon} shows that this fails for sound speeds" is fine as a pointer.
74. l.53 → first use: $Z_{\mathrm{val}}$ in "$e^2Z_{\mathrm{val}}/(m_em_uA_{\mathrm{cell}})$" is undefined. → "with $Z_{\mathrm{val}}$ valence electrons per cell".
75. l.57 → first use: $\kappa_\eta$ in "$1 - (1 + \kappa_\eta)\,m_{\mathrm{min}}^{\mathrm{ac}}/\mchi$" is undefined. → Add "($\kappa_\eta$ of \cref{eq:11.1-correction})".
76. l.61 → REGISTER item 11: "We name its inverse the \emph{effective sound speed}…" introduces a term by fiat. → "Its inverse is an effective sound speed, $c_{\mathrm{NR1}}$, …"
77. l.91 → LaTeX quotes: `A window "against silicon"` will print straight double quotes. → ``against silicon''.
78. l.91 → CAL. "so the inverse speeds rank two crystals to \SI{10}{\percent} only if their effective speeds differ by less than about \SI{13.5}{km.s^{-1}}." → As Lin would write it: "Roughly, the inverse speeds rank two crystals to 10 % as long as their speeds differ by less than ∼ 13 km/s, which most pairs of interest do not satisfy."
79. l.124-132 → pattern 19 or 20 (source bookkeeping): "We take the recommended constants of Vurgaftman and Meyer for the nitrides, as quoted by Lopuszyński and Majewski…, and the Brillouin constants of ZnO, as quoted by Gopal and Spaldin". The constants themselves are not stated, so a reader must open the source to check the speeds 8.08/11.02/6.10. → State the constants (as is done for CaWO$_4$ and CsI) and keep the citations as bare attribution.
80. l.132 → pattern 19: "The bulk-modulus floor is used here only for CsI, which is cubic; for the hexagonal and tetragonal crystals the comparison is with the Christoffel speeds themselves (\cref{app:C.18})." This is method bookkeeping. → Cut it to "(For non-cubic crystals the test uses the Christoffel speeds, \cref{app:C.18}.)" or delete it.
81. l.132 (end) → pattern 26: "A tabulated speed is therefore an input to be checked, not a measured property, and the check costs one Christoffel solve." restates l.124 ("they can be tested against measured elasticity without any phonon calculation"). → Delete it. The subsection should end on the CaWO$_4$ numbers.
82. l.136-146 → Ch17 restating its home chapter: the polar subsection re-quotes 11.2 almost entirely (0.1415/0.153/9.12/19.0; "103 = 134 × 0.77"; sapphire 7 % and 2.1; GaAs 8 %; amplification 3.5). The paragraph at l.146 ("The inputs of $\mathcal{I}_{\mathrm{pol}}$…") is entirely Ch11 material. → Keep the new result (the logarithmic $K_\eta$ ratio, the empty pairwise window, the figure of merit as a pair). Replace l.146 with one sentence: "Its inputs and their fragility on the dielectric route are those of \cref{we:11-ipol,lim:11.2d}; a crystal known only through $\varepsilon_\infty$, $\varepsilon_0$ and $\omega_{\mathrm{T}}$ is ranked by its interval."
83. l.150 → first use: $N_\kappa$, $A_{\mathrm{cell}}$ and $L_{\mathrm{Mig},\kappa}$ are undefined in Ch17. → Add "with $N_\kappa$ atoms of species $\kappa$ per cell of $A_{\mathrm{cell}}$ mass units and $L_{\mathrm{Mig},\kappa}$ the loss function seen by its ion (\cref{eq:12.3-permass})".
84. l.162 (end) → deletion test: "The nuclear factor is a factor, not a ranking, …" → "Light nuclei win only at fixed $L_{\mathrm{Mig}}$ (\cref{sec:12.3})."
85. l.166 title "Windows and inputs compared" → pattern 21 (gesturing title). l.168 → pattern 26: the whole subsection recaps 17.5.1-17.5.6 ("The reach figures of merit are kinematic and exact… The windows end through…"). Its one new fact is that the absorption figures of merit of 17.2 are exact at each mass. → Delete the subsection. Introduce the table with one sentence at the end of 17.5.1 and put the absorption clause in its caption or the table row (it is already in the row).
86. Limit Check 17.5a → this is self-contained and has its comparison plot, validity band and breakdown sentence. Note that it boxes the chapter's own keyresult eq:17.5-partial, not a literature formula. The STYLE rule is for literature limits, but the check against data earns its place. PASS.

## 17.6 Ranking under uncertainty

87. l.3 → the opener is 190 words. It is concrete up to "…not about the medians." What follows is a frame, a triad and self-narration: "This section turns each figure of merit… and reads off three objects… All three are conditional on the widths, which are conventions, and we say so with each number. We then show… and close with…" → Cut after "medians" and add: "We will give each input a width set by how it was obtained and read off, for each channel, the probability of ranking first, the interval of ranks and the tier." Delete "and we say so with each number" (pattern 22).
88. l.3 → negation framing (pattern 6), mild: "is a question about those errors, not about the medians" → "turns on those errors."
89. Caption of tab:17-widths (l.10) → not standalone and inconsistent with the text: "the evidence for the two largest is discussed in the text". The text (l.27) discusses the database speed width (0.086) and the gap shift. The largest width is the $X_{\mathrm{pole}}$ prior (log-uniform on [1, 3], σ ≈ 0.32). → "Widths for computed sound speeds and for room-temperature gaps are tested against the book's crystals in \cref{sec:17.6-widths}."
90. l.27 → mild hedge stack: "Neither width is a bound. A crystal whose computed tensor errs by \SI{25}{\percent}… is not excluded by the convention, and the rankings below are only as good as these choices." → Keep the 25 % example and drop "and the rankings below are only as good as these choices" (the keyresult already says this).
91. l.31 → pattern 19 (process artifacts), three in one paragraph: "Book values replace every other source where they exist."; "the Christoffel solution reproduces the book's $c_{\mathrm{NR1}} = 8.956$, 5.313…" (a consistency assurance); "The sound speed that the target table of Griffin and collaborators lists for CaWO$_4$ is inconsistent with this tensor (\cref{sec:17.5}), and it is not used." → Delete all three.
92. l.31 → redundancy with 17.5 l.130: the full CaWO$_4$ tensor ($C_{11}$… $C_{66}$, the source chain, $\rho_T$) is repeated. → "CaWO$_4$ enters with the measured tensor of \cref{sec:17.5-phonon}, $c_{\mathrm{NR1}} = \SI{4.58}{km/s}$."
93. l.31 → pattern 20: "the other gaps are the experimental values tabulated by Griffin and collaborators"; "the computed $Z^*$, $\varepsilon_\infty$ and highest optical energy of Griffin and collaborators for LiF and NaF". The values are not stated in the book. → Give the gaps (or the floors, already in tab:17-rank) and the LiF/NaF $Z^*$, $\varepsilon_\infty$, $\omega$ in one line or a table column.
94. l.31 → sentence length: "The polar inputs are those of \cref{sec:11.2}: …" (about 60 words). → Split it at "both from measured frequencies".
95. l.47 → first use: $\Phi$ (the normal CDF) is undefined. → Add "with $\Phi$ the standard normal distribution function".
96. l.49 → pattern 22: "The number depends on the width assigned to TeO$_2$'s tensor, and we show this by changing the width." → "With the computed-speed width doubled to 0.172, …"
97. l.49 → leaving judgement to the reader: "a reader who trusts the database less should read the second" → Delete it. The two numbers and the condition suffice.
98. l.68 → pattern 25 (negation-stacked withholding): "A tier claims less than its number suggests. It does not claim that every member of tier 1 beats every member of tier 2, nor that…" → State it positively: "A tier asserts only that each member is resolved below some member of the tier above."
99. l.68 → sentence length: "A wide interval rises: the nuclear edge… is the lower." (about 60 words). → Split it after "in tier 6".
100. l.82 → pattern 26: "The tier boundary of the worked example shows the price of a strict rule… Tiers therefore summarize a ranking; the probabilities carry its strength." restates the WE paragraph "What the tiers rest on" and l.68 ("the two are read together"). → Delete the paragraph.
101. Pattern 24 ("tier", 42 uses): "tier" is a defined object (height in the interval order, App. C.13), so it is not a private metaphor. It is still not field parlance for a referee in dark-matter detection. → Keep it, as App. C is book-wide, but write "tier (height in the interval order)" at first use in 17.6 (now only in the keyresult) and cut uses where "rank interval" or "resolved above" says the same.
102. l.97 → this passes. The measured-versus-computed offset (0.884 → 0.741) is new and is handled cleanly.
103. l.101 → the third instance of the measurement-side disclaimer ("The energy per electron–hole pair… is not in the table."). → Delete it.
104. l.122 → pattern 26 (mild): "No crystal leads every channel. Germanium has…, TeO$_2$…, diamond…, LiF…, GaAs…" lists the leader column of tab:17-rank, and "Two pairs of rows run in opposite directions, as \cref{sec:11.1,sec:11.2} found" restates 17.5 (l.61, l.144). → Keep "Silicon, the running example, leads none and sits mid-row" and the diamond/LiF reversal with its numbers (first versus last, factor 130). Cut the list of leaders.
105. l.124 → pattern 26: "The readings differ in what they rest on." restates TeO$_2$ 0.781 (l.49), the Migdal artifact (l.95) and the light-mediator row (tab:17-rank, 17.5 l.59). The only new facts are diamond over sapphire by 1.66 and LiF's factor of two. → Reduce the paragraph to those two sentences. The long Migdal sentence (about 60 words) goes.
106. l.126 → the fourth instance of the measurement-side disclaimer ("…is not a property of their response, and the guide to next targets weighs it…"). → Keep the CsI and lead-salt facts and end on "(\cref{sec:21.7})".
107. CAL. l.7: "It is assigned by convention, by the kind of input, not derived for each number" → As Lin would write it: "The width is a convention, set by the kind of input rather than worked out number by number."

## Summary

108. l.9 → structure: the 17.5 recap ("Each channel then reduces to a few material numbers…") starts in the middle of the 17.4 paragraph. → Start a new paragraph at "Each channel".
109. l.5 → pattern 19: "The Dirac targets enter with the background dielectric constant in the total $\varepsilon$, as \cref{sec:16.1} requires." is a convention assurance. → Delete it.
110. l.5 → pattern 20 (mild): "its spin current breaks pairs directly, with the conditions of \cref{sec:15.4}". → Name the condition (clean limit, below $2\Delta$ plus…) or drop the clause.
111. l.7 → imprecise: "The endothermic thresholds close each channel at the mass that pays the splitting plus the mode energy." This misses the two results of 17.3.4. → "An endothermic splitting of \SI{1}{eV} brings every collective channel to about \SI{0.3}{MeV}, half the pair threshold of silicon, and the plasmon is closed at every mass."
112. l.7 → number style: "1,810" here against "1810" in 17.3. → Pick one form.
113. Table row l.33 (shift of $\eta$) → inconsistent number: "rate ratios differ from the speed ratios by up to \SI{6}{\percent}" against 17.5 ("biased by \SI{7}{\percent}", 0.933). → Write "7 %".
114. l.13 → notation: "the loss function $L(\vect{k}, \omega)$ that the Migdal row needs" against $L(p,\omega)$ in 17.5. → $L(p,\omega)$.
115. l.13 (end) → the fifth instance of the measurement-side disclaimer. This one is legitimate in the summary. Keep it.
116. Length → 1,760 words, about 8 % of the chapter. Acceptable, but l.3 re-quotes all seven crossover regimes; the three representative numbers suffice.
117. Table caption tab:17-nuisances → standalone. "(values follow \cref{sec:16.1})" in the ZrTe$_5$ row is a process note. → Delete it.

## Cross-chapter checks

C1. Redundancy: the measurement-side disclaimer (energy per quantum, readout, backgrounds, \cref{sec:21.7}) appears in the opening l.4, 17.5 l.3, 17.6 l.101, 17.6 l.126 and the summary l.13. → Keep the opening and the summary (items 2, 71, 103, 106).
C2. Redundancy: the CaWO$_4$ tensor and the Griffin CaWO$_4$ inconsistency appear in 17.5 l.130 and 17.6 l.31 (item 92). The CsI $c_{\mathrm{NR1}}$ appears in 17.5 and 17.6 l.126 (with a pointer, fine). The book's $c_{\mathrm{NR1}}$ values appear in 17.5 and 17.6 l.31 (item 91).
C3. Redundancy: "stiff lattice: low edge, small heavy-mediator rate" appears in 17.5 l.61, 17.6 l.122 and the summary. "Rate and reach rank oppositely (polar)" appears in 17.5 l.144, 17.6 l.122 and the summary. Each should appear once in the body plus once in the summary.
C4. Numbers from Ch10-16, given once with a pointer: mostly done well (17.2's screening factors, 17.3's plasmon inputs). Exceptions: the 17.5 polar subsection (item 82); the 17.2 $\sigma_1$ caveats (item 32); and 17 versus $8\times10^5$ in the opening, 17.1 and the summary (item 3).
C5. Motivation of the comparisons: each section opens on a concrete cross-chapter number that the home chapters could not set side by side (the 17.1 thresholds, the 17.2 couplings, the 17.3 GaAs line, the 17.4 dark photon at 1.2 eV, the 17.5 Ge/Si ratio, the 17.6 TeO$_2$ versus CaWO$_4$). PASS on motivation.
C6. Seams. Opening → 17.1 is fine. 17.1 → 17.2 needs a contrast clause (item 38). 17.2 → 17.3 jumps from absorption back to scattering; 17.3 l.3 should add "Back in scattering, …" or tie to 17.1's GaAs polar edge, which it already quotes. 17.3 → 17.4 is fine (17.1 l.7 promised 17.4). 17.4 → 17.5 is abrupt but self-contained. 17.5 → 17.6 is good (built on $c_{\mathrm{NR1}}$). 17.6 → summary is fine.
C7. Titles: "across channels" occurs in the chapter title and in three section titles. Acceptable for parallelism. Fix 17.3 (item 39) and the two gesturing subsection titles (items 7, 85). "Response-level rankings of the scattering channels" (17.6.5) is long. → "Rankings of the scattering channels".
C8. Standalone scrub (internal labels): no SPINE, WP, campaign or "research ranking" terms appear in the text. The editor note's placeholder `\SI{MIGEQ}` is gone from s17-1. PASS, apart from the process sentences in items 16, 79-80, 91, 109 and 117.
C9. User rules: no exercises or checkpoints (PASS); nothing left to the reader except item 97 (minor); Γ typography is correct (`\varGamma` for rates, `\Gamma` for the zone center); no bare "Limit N.M" or "limit box"; citations carry equation or table numbers. The failures are under pattern 20 (items 34, 79, 93).

## Editor-notes items that concern prose

- 17.1, symbol clashes: $\sigma_n$ against $\sigma_p$ inside Ch17 is item 9. $\omega_\times$ and $\omega_{\mathrm{top}}$ against $\omega_{\mathrm{max}}$ do not clash in the prose; they are defined at first use.
- 17.1, "not evaluated" cells for Ge and GaAs: these are fine in prose. Each cell is stated as open, and the Open-problems text names the missing input.
- 17.2, YIG dark-photon point: item 34. The prose currently gives no derivation line, so under the ruling it should be dropped unless one is added.
- 17.2, ZrTe$_5$ two half-gaps: the caption labels both (solid and dotted) and the nuisance row states the spread. This is acceptable prose until the rerun.
- 17.2, GaAs density 5.361: the WE uses it silently. No prose change; this belongs to the book-wide pass.
- 17.3, Larmor closure: item 46.
- 17.3, plasmon 0.09-0.16: labeled as two models at l.92, and the nuisance row agrees.
- 17.4, the "ionic correction of the zero-phonon line" wording is used at l.11 and in the WE. Consistent.
- 17.6, recheck the summary against the final 17.4 and 17.5: done. The mismatches are items 108, 113 and 114. The 17.4 numbers (5.47e-4, 4.83-4.88e-4) and the 17.5 numbers (0.970, 3.5, 28.4 MeV, 5.7e5) agree.
- 17.6, $X_{\mathrm{pole}}$ defensibility: the prose states it as a convention "far narrower than the range the two limits allow" and reads the rankings at $r_{\mathrm{mat}} = 0$. That is honest prose. The caption of tab:17-widths needs fixing (item 89).
- 17.5, "17.6 must use book halo values": 17.6 keeps $v_{\mathrm{max}} = 2.650\times10^{-3}$ fixed and uses the book's 1.69/0.49 ratios. No prose conflict.
