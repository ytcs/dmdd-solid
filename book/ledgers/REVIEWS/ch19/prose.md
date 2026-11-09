# Ch19 prose review (style and prose, isolated)

Scope: tex/ch19/ch19.tex (opening, map caption), s19-1 … s19-6, s19-summary, tex/appD/D-45.tex. Checked against STYLE.md, style-guide.md, prose-review.md (patterns 0–26), REGISTER.md and the prose items in editor-notes.md. Line numbers are per file. No tex edited.

## Verdicts

| Section | Verdict | Main reason |
|---|---|---|
| Opening + map (ch19.tex) | PASS | Concrete, motivational; one wording fix ("lattice heat"). |
| 19.1 Nuclear recoil on the BO surface | PASS | Minor: an undefined symbol, a restating closing paragraph, one mis-titled worked example. |
| 19.2 Electronic excitation by the recoil | REVISE | A looped recap paragraph (pattern 26), "so" at 2× target, provenance note, negation opener. |
| 19.3 Stopping of slow ions | REVISE | Provenance chains (pattern 22), weak motivation for the Bethe half, a scope-disclaimer ending, notation drift (Z, ℓ/x). |
| 19.4 Defects and stored energy | REVISE | Re-displays the 19.5 machinery before 19.5 derives it; conditions (a)–(d) printed three times; process artifacts. |
| 19.5 The energy balance law | REVISE | 1.144 process artifact; symbol clashes (x, e, b, ε); withholding opener; count-teasers; "only" at 53/10k. |
| 19.6 Delayed release and the LEE | REVISE | Open-problem paragraphs restate the text; symbol clashes (ω_p, p, ⟨q²⟩); unmotivated defecton entry; reviewer-facing Pushkarov aside. |
| Summary | PASS | Accurate and complete except that it omits the double-counting rule; two wording fixes. |
| App. D.45 | PASS | Title is too long; s has two meanings. |

## 1. Lint results (lint.py --banned BANNED-TERMS.txt)

No blocking hits and no banned terms. Warn-tier hits:
- s19-1: 2 LONG-SENT (l33 p_FP sentence; partition keyresult).
- s19-2: EQ-PUNCT l67 (kernel display; this is a **false positive**, since the sentence continues with "of the electronic excitation energy"); 3 LONG-SENT (l84 subsection lead-in, the fig19_2 caption (b), l102 total-variance sentence).
- s19-3: 4 LONG-SENT (l45 (A)–(E) sentence, the limit-19.3a caption tail, the Bethe keyresult, the limit-19.3b caption tail).
- s19-4: 3 LONG-SENT (lim 19.4a caption tail; **l102 conditions sentence, about 110 words**; tab:19-bounds caption).
- s19-5: EQ-PUNCT l126 (**false positive**: the full stop sits inside `split`); 4 LONG-SENT (l53 E_miss lead-in, the lim 19.5a caption, the calibration keyresult, **l152 conditions sentence, about 120 words**).
- s19-6: 1 LONG-SENT (lim 19.6a caption); MONOTONY l20 (eight sentences of near-equal length in the hop-rate paragraph).
- summary: 3 LONG-SENT, all table rows (acceptable).
- D-45: TITLE l1; EQ-PUNCT l48 and l89 (**false positives**, punctuation inside `split`).

Every other display equation in the chapter is punctuated as part of its sentence; I checked them all by hand.

## 2. Chapter-level findings

**C1. 19.4 runs ahead of 19.5 (redundancy and arrangement).** 19.4 l73–85 defines g_L, Y_ph, f_DF, 𝔯_coll, δ_coll, d_NR, x_NR/ER, f_ion and C_cal, and re-displays eq:19.5-first as eq:19.4-fDF. 19.5 l97–133 then defines the same objects again (g_L displayed twice, at 19.4 l75 and 19.5 l38; Y_ph defined at 19.4 l77 and 19.5 l108; the CDMS reconstruction described at 19.4 l73 and 19.5 l108; C_cal displayed at 19.4 l82 and 19.5 l129). The bound appears as eq:19.4-bound and as eq:19.5-bound/eq:19.5-widen. Limit Checks 19.4b and 19.5b plot the same branch (0.086 against "+0.031 at 𝔯_coll = 0.9").
Fix: keep the definitions, signal model and bound in 19.5, where they are derived. Reduce 19.4-calib/-bounds to the two data sets, a one-line statement "E_st/ω ≤ 1 − Y_ph under conditions (a)–(d) of \cref{sec:19.5-yield} (\cref{eq:19.5-bound})", the numbers and tab:19-bounds. Then either drop lim:19.4b or turn it into the p_surv E_FP/E_d plot. This also settles the editor note "four conditions … keep them in one place (19.5)".

**C2. Conditions (a)–(d) printed three times**: 19.4 l102, the tab:19-bounds caption l110 and 19.5 l152. Fix: state them in full once (19.5 l152, split into four sentences); the table caption gives "conditions (a)–(d) of \cref{sec:19.5-yield}".

**C3. Repeated statements across sections.**
- "The displacement threshold is a barrier, not stored energy": 19.1 l130, 19.4 l12, 19.5 l27. Keep 19.1; cut the 19.4 clause "it is not itself an energy that the crystal keeps"; reduce 19.5 l27 to "The displacement threshold appears nowhere in \cref{eq:19.5-balance}."
- "At millikelvin defects move only by tunneling or with the phonons of later events": 19.1 l111, 19.4 l18, 19.5 l7. Keep 19.1 and 19.6; cut the 19.4 sentence.
- "One table of configurational energies, one potential and cell": 19.1 l103, 19.4 l20, 19.6 l54. Keep 19.1 (requirement) and 19.6 (sum-rule condition); cut 19.4 l20 sentence 2.
- "Friction assigns losses to final states that are strongly suppressed": 19.1 l107 and 19.3 l84, almost verbatim. Keep 19.3 (the argument) and cut the clause in 19.1, which can point to \cref{sec:19.3-assumptions}.
- Pointers of the form "the calculation that would decide is …, specified in \cref{app:E.23}" close 19.1 l132, 19.2 l109, 19.3 l97, 19.4 l20, 19.4 l147 and 19.2 l130. Keep at most one per section.
- "Lindhard = partition with E_st = 0 and continuum ω_e": 19.1 l134 and 19.3 l3. Keep it in 19.3.
- The 0.72 eV step width is quoted at 19.1 l33, l38, the WE and l99, and at 19.4 l14. The 19.4 occurrence can be a pointer without the number.
- "Electron recoils store no energy": 19.4 l79 (0.14 MeV electron) and 19.6 l166 (10 eV electron, 0.78 meV). Keep one; 19.6 can point to 19.4.

**C4. Count-teasers (pattern 18), a chapter-wide tic.** Examples: 19.3 l80 "makes three assumptions"; 19.4 l79 "Three kinds of terms make up f_DF"; 19.4 l143 "rests on four choices"; 19.5 l146 "bounds the stored energy under four conditions"; 19.5 l166 "come from three sources"; 19.5 l197 "Three further handles exist"; 19.6 l54 "Five conditions make it exact"; 19.6 l70 "two families dominate"; 19.6 l99 "The exponent follows in four steps"; 19.6 l154 "Three effects decide"; 19.6 l166 "Three consequences follow without any model"; 19.6 l168 "makes three hypotheses". Fix: name the members in the sentence, for example 19.3 l80 "…makes three assumptions that its list does not name (no stored energy, friction down to zero speed, and conversion to pairs in proportion), and each fails below a keV in silicon."

**C5. Section-opener template.** 19.2 l3, 19.3 l3, 19.4 l3 and 19.5 l3 all close on a four-verb outline sentence ("We derive …, show …, write …, and separate …"; "This section computes …, writes …, and turns …"). Each one is allowed by REGISTER §6.1 on its own, but together they read as one formula. Fix: keep the outline in 19.2 as a "we will" sentence; in 19.3–19.5 end the opener on the question (see the per-section entries).

**C6. Register (REGISTER §4, counts per 10k words).** All six sections have 0 "however", 0 "we will/we can/we see", 0 "note that", 0 "typical" and 0 "for example" (one in 19.6). Over target: "so" 61 in 19.2 (target ≤ 30); "only" 53 in 19.5 and 55 in the summary (L 11); "gives" 30–38 in 19.3, 19.5 and 19.6 (L 7); "not" 45–48 in 19.2, 19.4 and 19.6. Fix: in each section replace three or four "so … therefore" chains with "since"/"as a result", add one "however" where a real contrast exists (19.2 l100 "Germanium, however, shows the opposite deviation"; 19.5 l185 already has one) and one "we will"/"we can" in each opener; change "gives" to "is"/"leads to".

**C7. Symbol overloads (first use, one symbol one meaning).**
- E_φ: `E_\varphi` at 19.4 l73/75, `E_\phi` at 19.5 l108/136. Unify.
- g_L: the Luke gain against Lindhard's g_L(ε_L). The 19.4 l77 parenthetical "(written without argument; g_L(ε_L) of 19.3 is Lindhard's function)" patches an open clash and is a process artifact. Rename the Luke gain as the editor notes ask (g_Luke) and delete the parenthetical.
- 19.5 `x`: x_NR/x_ER and "x = 0" (l154) for missing energy, but l161 also uses x as the gap-fraction multiplier ("x = 1 for the electron, x = f_ion"). Rename the second one (for example χ_g).
- 19.5 `e = E_st/ω` (l146) sits next to eV_bias (elementary charge). Use e_st or s_st.
- 19.5 `b(t)` (released fraction) against b_N, b_imp, the basin index b (19.4) and b_br (19.6).
- 19.5 `ε` (sensor fraction, l57, \epsilon) against ε_L (\epsilon_L, 19.3) and ε_eh.
- 19.6 l22: ω_p is the accepting-mode energy, but ω_p is the plasma frequency in 19.3; p counts quanta while p_i are probabilities in the same section and p is momentum in 19.2. Use ω_acc and n_q.
- 19.6 ⟨q²⟩ (l101) is a *rate* of change of the squared crystal momentum, written like a mean, with q the book's momentum transfer. Use $\dot{\mathcal{K}}$ or ⟨Δk²⟩/t.
- 19.6 l180: Y (Young's modulus) next to Y_q/Y_ph, and σ (stress) next to σ (cross-section).
- 19.3: Z (l11), Z_κ (19.2 l66) and Z_1 (Bethe) are all used for the silicon charge. Write Z_κ for the target atom throughout.
- 19.3: the path length is ℓ at l25/l49 but x in eq:19.3-bethe and in "−dE/dx". Pick one.
- 19.4 WE l64: "M = 26.16 GeV" should be M_κ.
- 19.1 l33: E^kin_κ is not defined (it is the mean kinetic energy per Cartesian component of the zero-point motion). Define it in the sentence.
- 19.6 l154: Δ_r is not defined; give "the renormalized tunneling amplitude Δ_r of \cref{sec:16.8-ohmic}".
- D.45: s is the fraction of the gap crossed (l73, as in 19.5 l31) and also the calibration factor (l77). Rename the factor.

**C8. Citation style.** The naming varies: "Sarkis, Aguilar-Arevalo and D'Olivo" (19.3 l23), "Sarkis and coworkers" (l30) and "Sarkis et al." (l43ff). Use "Sarkis et al." throughout. "Ref.~\cite" as a noun appears at 19.5 fig:19-shares caption ("the detector of Ref.~\cite{alkhatib2021light}") and 19.6 l63 ("the athermal sensors of Ref.~\cite{…}"); elsewhere the chapter uses bare citations. Write "the athermal sensors of that measurement~\cite{…}". In Limit Check 19.3a the Lindhard formula is credited to agnese2018nuclear [Eq. (3)]; the editor note says "Lindhard 1963 credit only", so credit lindhard1963integral, with the secondary source used for the equation number.

**C9. Percent style.** 19.3 l73 "8 to 38 percent" and 19.2 l89 "about one percent" should use \SI{}{\percent} with numerals, as everywhere else ("8 to \SI{38}{\percent}").

**C10. Seams (reading across each join).**
- Opening → 19.1: both open by narrating one recoil's fate (21 eV/12 km/s, then 12.5 eV ⟨111⟩). Acceptable, since the examples differ.
- 19.1 → 19.2: clean; 19.1 l134 hands the sub-threshold charge to 19.2.
- 19.2 → 19.3: **the same number twice across the join.** 19.2 l100 "by a factor of 1.5 at 100 eV (0.153 against 0.102)" is followed by 19.3 l3 "y_L = 0.153 at 100 eV … below it by a factor of 1.5". Fix: 19.3 l3 can point back ("lie below it by the factor 1.5 of \cref{sec:19.2-yield}") or open on the 13 % model dependence.
- 19.3 → 19.4: 19.3 ends on a scope disclaimer (l154), which is a weak join; see 19.3 below.
- 19.4 → 19.5: the join exposes C1, since 19.5 re-introduces the CDMS calibration that 19.4 has just analysed.
- 19.5 → 19.6: good. 19.5 l197 (two read windows, release within the window) leads straight into delayed release.
- 19.6 → Summary: clean.

**C11. Comparisons with Ch10–16 and quoted numbers.** Ch19 does not restate the home chapters at length. 19.6 l15–20 re-derives eq:16.8-golden as a special case in one sentence, which is fine. Exceptions:
(i) the tunneling bound 23.6 of \cref{sec:16.8-hop} is quoted three times in 19.6 (l3, l27, l29), and again in the open problems. Give it once (l27) and refer to it.
(ii) 19.3 l132 re-describes and re-cites the Franta/Henke loss function of \cref{sec:10.7}. A pointer is enough: "Take the measured loss function of \cref{sec:10.7}."
(iii) The Bethe subsection of 19.3 (keyresult, worked example and Limit Check, about 1/3 of the section) is weakly motivated in a low-energy chapter. Its own conclusion is that recoils sit at β < 10⁻³ and that its only use for slow ions is the first-order stopping. Fix: motivate it in one sentence at l3 (what a reader gains, namely that the solid enters only through Ī and that the friction regime begins below 2 v_F), and shorten the worked example to the valence/L/K split.
(iv) The comparisons are otherwise well motivated (19.2 against the data, 19.4 against NRT, 19.6 against Pushkarov and Fitzgerald).

## 3. Per-section issues (location → problem → fix)

### Opening (ch19.tex)
- l2 "Most of it becomes lattice heat." → the editor note on E.23 says that E_heat is all phonon energy and that "lattice" belongs to E_lat → write "Most of it becomes heat."
- l4 "…and writes one balance law that books every share once." The outline is acceptable: it says how the chapter connects to Chaps. 11, 18 and 20 and is not a list of sections. Pattern 25 is clean: no figurative stand-ins, and "neither sees the stored energy until it is released" is technical.
- l9 map caption: it stands alone. Its "Migdal events counted apart" is clear.

### 19.1
- l9 "the energy ω is lattice heat, carried by the phonons that the response lists" → "the energy ω is heat, carried by …" (same reason as the opening).
- l33 E^kin_κ is undefined → see C7.
- l42 "is decided by four dimensionless numbers" → name them: "…by four numbers: the quantum ratio λ_dB/ℓ_R, the anharmonic ratio η_R, the threshold E_d and the Massey parameter ξ_M."
- l71–78: the description list enumerates genuine regimes, which is allowed.
- l80 WE title "The harmonic-to-cascade boundary for silicon" → the example covers all four boundaries and the masses → "Regime boundaries for silicon".
- l134 (pattern 26) "In the two regimes below E_d … all of its energy as heat. … The displacement regime adds E_st > 0 … and the nonadiabatic regime adds ω_e …". Sentences 1–3 and 5 restate the l71–78 list and the WE; the new facts are e^{−ξ_M} = 5×10⁻⁹ at 12.5 eV, the 150 MeV mass reach and the source of sub-threshold charge. Fix: keep those three facts and the hand-off to 19.5, cut the regime re-listing and the Lindhard sentence (C3).
- Calibration (REGISTER §6.13). l38 (step width matters because the spectrum falls steeply near its endpoint) could be Lin's. l111 (choice of t_pr) could be. l9 could not; rewrite it as: "Here there is nothing left to follow: the response already lists the phonons, and their energy ω goes straight to the phonon readout (\cref{sec:8.7})."

### 19.2
- l3: the opener is concrete and good. "Yet a binary collision …" is a negation, but technical.
- l55 subsection opener "A recoil of a few hundred eV does not travel in a straight line through a smooth electron gas." (pattern 25, negation first) → "Within a few femtoseconds a recoil of a few hundred eV strikes a neighbor, closer than a bond length, and passes on part of its energy; …" (merge it with the next sentence).
- l59 "the Landau–Zener probability~\cite{zener1932non}, in the form derived by Vutha~\cite{vutha2010simple}" (pattern 22, provenance; editor note: Zener unread) → "the Landau–Zener probability~\cite{zener1932non,vutha2010simple}".
- l78 last sentence "Dividing … thus undercounts the pairs of near-gap excitations and misses that each of them gives a pair with certainty." This restates the numbers before it → cut it, or keep only "each near-gap excitation gives a pair with certainty".
- l109 (pattern 26) "These numbers are what the chain of this section must reproduce. … Every step of it is specified in \cref{app:E.23}." New facts: none. The binary channel being closed below 352 eV is in l24/l39; the chain is in l71–77; the pointer to E.23 is in l80 and l130. Fix: delete the paragraph and move its one useful clause ("the Fano factors test the distribution, not only the mean") to the end of l107.
- l122 end "The measured charge … is therefore almost entirely collisional: the Migdal electrons account for one part in 260 of it at 100 eV." This restates "0.4 % of the measured yield at 100 eV" from three lines earlier → keep "almost entirely collisional" and cut "one part in 260".
- l124 "Both pieces are excitations of the electrons by the nucleus, ordered in time, one sudden and one spread over the slowing-down." Fails the deletion test → cut it.
- l130 Open problems restates l100–107 (0.10, 0.22, 0.46 keV; Ge 254 eV). The only new fact is the zero-charge probability → shorten to the missing input (the kernel) and that consequence.
- Register: "so" appears 19 times. Examples to change: l7 "so in the crystal frame" → "and in the crystal frame"; l39 "so that no binary collision" → "too little for a binary collision at the measured 100 eV point to make a pair"; l49 "so below E_R,th" → "Below E_R,th, as a result, …".
- Calibration: l14 (the moving wall) is Lin-like. l3 is Lin-like. l109 is not; if any of it is kept: "The two lowest points are the real test: at 0.10 and 0.22 keV the binary channel is closed, so the whole yield must come from crossings and the momentum tail."

### 19.3
- l3 last two sentences "We derive the integral equation …; then we derive the opposite limit … The two limits bracket the recoil problem: one is a fit at the speeds of recoils, the other a derived result at speeds no recoil reaches." The outline is followed by an aphoristic cadence (pattern 25 borderline) → "We will derive Lindhard's equation from that partition and see which of its assumptions fail below a keV; the Bethe formula, derived from the loss function, shows where the opposite, first-order limit begins (above about 2 v_F)."
- l5 "Lindhard's name is attached to two different objects in this book." "In this book" is self-reference → "Two objects carry Lindhard's name: the Lindhard function ε_Lin of \cref{sec:4.5} … and Lindhard quenching y_L."
- l23 "the form that Sarkis, Aguilar-Arevalo and D'Olivo write as … with t = x_L²~\cite[Eq.~(2)]" (pattern 22/19, a convention mapping aimed at a checker) → cut it, or reduce to one clause "(with t = x_L² this is the form of~\cite[Eq.~(2)]{sarkis2023ionization})".
- l43 "which is Lindhard's basic integral equation~\cite{lindhard1963integral} as Sarkis et al.\ write it~\cite[Eq.~(3)]" → "Lindhard's basic integral equation~\cite{lindhard1963integral}, \cite[Eq.~(3)]{sarkis2020study}".
- l45 "listed by Sarkis et al." is provenance → "Lindhard reduced \cref{eq:19.3-basic} with five further approximations~\cite[Sect.~II]{sarkis2020study}:". Split the (A)–(E) run-on: put a colon after the lead-in, give each item its own clause, and end with a full stop.
- l63 "is the fit to their solution given by Lewin and Smith~\cite{…}, as Sorensen traces it~\cite[…]" (pattern 19/22, a provenance chain) → "is Lewin and Smith's fit to their solution~\cite{lewin1996review,sorensen2015atomic}".
- l73 Limit Check sentence: "8 to 38 percent" → \SI form (C9).
- l80 count-teaser → see C4.
- l84 "Below E_R,th the friction assigns losses to final states that are strongly suppressed." Keep it here and drop it from 19.1 l107 (C3).
- l97 "Each modified model repairs one assumption and fits the data with constants that absorb the others, so the agreement it reaches does not show which assumption is responsible." (calibration) → "Each modified model fixes one assumption and lets its fitted constants absorb the rest; a good fit therefore does not tell us which assumption was wrong."
- l132 Franta/Henke re-description → see C11(ii).
- l154 "The fast-ion side has a reason to stop here. … that calculation lies outside the scope of this book." (pattern 22, a self-narrating scope note that ends the section on a disclaimer) → cut the first sentence. Either end on the physical fact ("A fast heavy ion leaves a track … what a track detector reads is a defect configuration, not an excitation spectrum."), or move the whole paragraph to one clause in \cref{sec:19.3-bethe} l152.
- Calibration: l25 ("The electronic losses are a friction") could be Lin's. l97 (rewritten above) could not.

### 19.4
- l3 "This section computes how much energy a recoil leaves in defects, writes the measured deficit as …, and turns the data into upper bounds …" (C5) → "How much of that 5–6 % is stored energy? We will count the defects a recoil leaves and then ask what the two calibrations allow."
- l12 "it is not itself an energy that the crystal keeps" → cut (C3).
- l18 "At millikelvin, recombination proceeds only by tunneling or with the phonons of later events (\cref{sec:19.6})." → cut (C3).
- l20 sentence 2 (one table) → cut (C3).
- l73 subsection opener "Neither measurement sees the stored energy directly." (pattern 25, negation first) → "Both measurements see the stored energy only through a phonon deficit: they compare …"
- l73–85 → see C1.
- l77 g_L parenthetical → see C7 (process artifact).
- l79 "Three kinds of terms make up f_DF." → see C4.
- l102 conditions sentence (about 110 words) → see C2, and split it.
- l107 "A two-standard-deviation edge, 0.0644, gives the same germanium value at two digits." (pattern 19, a robustness assurance aimed at a reviewer) → cut it.
- l110 table caption: it repeats the conditions (C2). The "Sources:" line is fine as attribution.
- l68 WE close, first sentence "The stored energy of a sub-keV recoil is thus several percent of E_R if survival is complete, comparable to the deficits measured at 10 to 100 keV." This restates l66 → keep only the comparison to the measured deficits and the 20 eV reading error.
- WE title "Energy stored by a 300 eV silicon recoil" is fine.
- Calibration: l3 is Lin-like ("Collection can too" is good). l102 is not; rewrite it as four short sentences: "The bound needs four conditions. (a) Primary phonons of a nuclear recoil are collected no better than those of an electron recoil, δ_coll ≥ 0. (b) …"

### 19.5
- l3 "The conversion is correct only if …, and that holds only under conditions that the bookkeeping of all shares at every time makes explicit. This section writes that bookkeeping as one law and derives from it …" (pattern 25 withholding with a stacked "only … only"; C5) → "The conversion is correct only if electron and nuclear recoils of the same energy deliver the same share. To see when that holds, we book every share at every time in one law; applied to the CDMS II silicon calibration, it shows that the measured ratio fixes a combination of stored energy and collection, which a second bias can separate."
- l27 → see C3.
- l123 second sentence "\Cref{eq:19.5-calib} separates what the bias adds … from what a calorimeter without bias would measure." This restates the keyresult → cut it; keep the r′ and "away from r′ = 1" facts.
- l133 C_cal explanation (calibration; the reasoning is folded into one long sentence) → "The coefficient C_cal measures how much a deficit of the calibrating electron recoils matters. Such a deficit lowers the phonon scale and so raises every reconstructed nuclear-recoil energy. However, it acts only through the primary part of the signal, and the nuclear recoil has less Luke signal to offset; as a result C_cal < 1, 0.663 at 4 V and 0.402 at 40 V."
- l146 "The silicon datum bounds the stored energy under four conditions." → see C4. l152 is a 120-word sentence → split it into one sentence per condition (C2).
- l154 "Transport estimates of a two-film geometry therefore give 𝔯_coll at or slightly below one" is a quantitative claim with no number and no pointer to where the estimate is made (pattern 0; the editor note says 20.5 must carry the number) → "…give 𝔯_coll at or slightly below one (\cref{sec:20.5})", and put the number in once 20.5 has it.
- l166 "The other parts of the offset come from three sources." → see C4; name them in the sentence.
- l181 "With f_ion = 0.3 and the source's 3.82 eV per pair, g_L = 1.047, the same formula gives 1.144." (pattern 19, bookkeeping of which value was adopted; editor note "the WE prints both") → cut it. If a literature comparison is wanted, write one clause as a fact about the literature: "(1.144 with the f_ion = 0.3 and 3.82 eV per pair of~\cite{agnese2018nuclear})".
- l188 sentence 1 "The datum fixes one combination of 𝔯_coll, δ_coll and the missing energies, not the stored energy." This restates the opener and the WE → cut it; start the paragraph with "A second bias separates the collection ratio from the rest."
- l197 "Three further handles exist." → see C4.
- Symbol clashes x, e, b, ε and E_φ → see C7.
- Calibration: l65 (unit heat quenching: what it requires and why it fails) could be Lin's. l72 ("Nothing in it is small. …") could be. l133 could not (rewritten above).

### 19.6
- l3 opener: good, concrete, with no periphrasis. "the obvious suspect" is a plain idiom.
- l22–29: 23.6 is quoted three times in the section → see C11(i).
- l20 MONOTONY → vary the rhythm: merge "An eV release is far above the phonon band, and the bath can take it only as many quanta at once" with the Huang–Rhys sentence.
- l92 subsection opener "A defect whose tunneling between equivalent sites is fast compared with the disorder around it is not localized at all." This is a negation (pattern 25), and the subsection has no motivation → "A light defect that tunnels between equivalent sites faster than the disorder around it can detune them becomes delocalized. This matters here because a mobile defect reaches its partner, or a surface, on a time set by its band and not by a barrier." The second sentence is the motivation (arrangement check: why the reader needs it).
- l115 "His T^-9 law takes the defecton energy as a mean ε(p) and coincides with D_9 for ε(p) = Δ_dfn/4. His T^-7 coefficient is half that of \cref{eq:19.6-D}, since his collision time is defined as an estimate." (pattern 19, a reviewer-facing reconciliation) → reduce to one clause: "These are the two limits of Pushkarov's interpolation~\cite[Eqs.~(61), (64)]{pushkarov2004quantum}, whose low-temperature coefficient is half ours because it rests on an estimated collision time."
- l132 subsection opener "An extra atom in a close-packed row … does not sit between two neighbors. It spreads over many, as a kink in the row, a crowdion." (pattern 25) → "An extra atom in a close-packed row of a bcc metal spreads over many neighbors as a kink in the row, a crowdion."
- l182 "This is a statement about missing information, not a derivation of the observed exponential spectra." The negation framing (pattern 6) is honest but weak as a subsection ending → "It describes missing information; it does not derive the observed exponential spectra." Alternatively, move the paragraph ahead of l180 so that the subsection ends on the testable prediction ("no free parameter").
- l186 Open problems (pattern 26) restates l29 nearly verbatim (14 %, 6 %, 5 %, one calculation per path). Fact list: none new → reduce to one sentence with a pointer: "The release of close pairs at millikelvin (\cref{sec:19.6-kinetics}) awaits one calculation per path (\cref{app:E.22})."
- l190 restates l180 ("A rate needs two inputs that do not exist …") → cut it.
- Count-teasers l54, l70, l99, l154, l166, l168 → see C4.
- Symbol clashes ω_p, p, ⟨q²⟩, Y, σ, Δ_r → see C7.
- Calibration: l128 ("holds better than its derivation suggests … a defecton moves faster the colder the crystal") is Lin-like. l166 is not; rewrite it as: "Without any model we can already say three things. The event-seeded term is small: electron recoils cannot displace atoms at all, and nuclear recoils store at most 5.5 % (silicon) and 6.4 % (germanium) of their energy (\cref{sec:19.4}). …"

### Summary
- The recap is accurate: 0.41/0.54 eV, 150 MeV, 352/399 eV, 13 %, 0.055/0.064, 1.154, 0.033 and 14 %/6 % all match the sections.
- l5 "non-perturbative" against "nonperturbative" at 19.2 l66 → "nonperturbative".
- l11 "a Frenkel–Kontorova kink of a tenth of an atomic mass" is ambiguous (atomic mass unit?) → "with a tenth of the mass of a tungsten atom".
- Missing key result: the rule of 19.2 l124, that a measured yield already contains the Migdal ionization and that adding a computed Migdal rate counts it twice. Add one sentence after the Migdal sentence in l5.
- l13 last sentence is fine (a pointer to the next chapter, not a list).
- tab:19-nuisances caption stands alone.

### Appendix D.45
- l1 title "The energy balance law and the phonon-yield ratio" (lint TITLE, two-item "and") → "Energy balance and calibration algebra".
- l73/l77: s is used for two things (C7).
- l3 "This appendix proves …, derives …, and carries out the algebra behind …" is acceptable for an appendix map.

## 4. Captions (stand-alone check)

The captions of fig:19-map, fig:19-recoil, fig:19-yield, fig:19-yields, fig:19-shares, fig:19-release and all eight Limit Check plots name the quantity, units and parameters. The Limit Checks are self-contained comparison plots with a one-sentence breakdown statement and no Source/Chain list. Minor points:
- lim 19.3a: the x-axis quantity (E_R in keV) is not named; add "against the recoil energy".
- lim 19.4b: the last caption sentence "No computed stored energy exists to compare with." is a process-style admission. Either cut it, or turn it into the plot's comparison ("the literature reading is the 𝔯_coll = 1 point").
- fig:19-shares: "Ref.~\cite" as a noun (C8).
- Pattern 25 in captions: clean.

## 5. Standalone scrub and user rules

- No exercises, checkpoints or "left to the reader". No "you", "I", contractions, i.e./e.g., thereby, whereby, "respectively", "in order to" or em dashes.
- Process artifacts: 19.5 l181 (1.144), 19.4 l107 (2σ edge), 19.4 l77 (g_L parenthetical), 19.6 l115 (Pushkarov reconciliation), 19.3 l23/43/63 (provenance chains), 19.2 l59 (Vutha form).
- Citations as content (pattern 20): none blocking. Every formula is stated in the book's notation, and the Limit Check boxes state their formula before citing it.
- No hard-coded "Sect./Eq./Fig." numbers; all cross-references use \cref.
- Illustrative inputs are labelled as such (19.5 fig, 19.6 WE, Al barrier, V₀, pockets, f_ph = 0.25).

## 6. Pattern 26 fact lists (paragraphs by order within each section; ✓ = adds at least one new fact)

- 19.1 (25 ¶): ¶1–24 ✓. ¶25 (l134) is mostly a subset of ¶12 and the WE; its new facts are 5×10⁻⁹, 150 MeV and the source of charge → trim it.
- 19.2 (23 ¶): ✓ except ¶19 (l109), which has no new fact → delete; ¶20 tail (l122, "1/260") repeats 0.4 %; ¶23 (l130) has one new fact (the zero-charge probability).
- 19.3 (26 ¶): all ✓. ¶26 (l154) carries only scope → rewrite (above).
- 19.4 (24 ¶): ✓, but ¶3 (l12), ¶6 (l18) and ¶7 (l20, apart from the Sassi numbers) repeat 19.1, and ¶14–15 (l73–85) and ¶18 (l97–107, conditions) repeat 19.5 (C1, C2).
- 19.5 (27 ¶): ✓. ¶19 (l123) sentence 2 restates the keyresult; ¶25 (l188) sentence 1 restates the WE.
- 19.6 (34 ¶): ✓ except ¶30 (l186, a subset of ¶5) and ¶32 (l190, a subset of ¶28).
- Subsection endings: 19.2-yield ends on the recap ¶19 → delete it; 19.3-bethe ends on a scope note → fix; 19.6-lee ends on the max-entropy caveat → reorder. All others end on a new fact.

## 7. Editor-notes items concerning prose

- "lattice heat" for E_heat: still at ch19.tex l2 and s19-1 l9 → fix (above).
- ℓ → ℓ_int: done in 19.1. ⟨ω⟩ = 40.9 meV: used consistently.
- v_th → v_{N,th}: done.
- g_L clash (Lindhard against Luke): open; patched by a parenthetical at 19.4 l77 → rename (C7).
- 𝔯_coll 1.154 against 1.144: the text adopts 1.154 but still prints 1.144 at 19.5 l181 → cut it (process artifact).
- Conditions in both 19.4 and 19.5: still in both and in the table caption → C2.
- 19.4 must cite rather than re-derive the 19.5 results: it cites them but re-displays them → C1.
- Zener unread: this shows in the "in the form derived by Vutha" provenance note → fix (19.2 l59).
- Illustrative inputs labelled: yes.
- Limit Check numbering ("19.1/19.2" against lim:19.3a/b): this is a build issue, not prose; it is still to be checked against other chapters.
