# Ch6 prose review (style, register, standalone scrub)

Scope: tex/ch06/ch06.tex, s6-1 … s6-5; tex/appD/D-16 … D-18. Checked against STYLE.md, style-guide.md, prose-review.md, REGISTER.md, and the prose items of editor-notes.md. Line numbers are real file lines. No tex edited.

## 1. Lint record (`lint.py --banned BANNED-TERMS.txt`)

| File | Hits | Blocking | Content |
|---|---|---|---|
| ch06.tex | 0 | 0 | — |
| s6-1 | 4 | 0 | 4 LONG-SENT |
| s6-2 | 1 | 0 | 1 LONG-SENT (caption, artifact) |
| s6-3 | 5 | 0 | 2 EQ-PUNCT, 3 LONG-SENT |
| s6-4 | 9 | 0 | 1 EQ-PUNCT, 8 LONG-SENT |
| s6-5 | 8 | 0 | 1 WORDY ("in terms of", l.160), 3 EQ-PUNCT, 4 LONG-SENT |
| D-16 / D-17 / D-18 | 3 / 2 / 1 | 0 | 2+1 EQ-PUNCT, 1+1+1 LONG-SENT |

- **All 9 EQ-PUNCT hits are false positives.** The punctuation sits before `\end{aligned}`/`\end{gathered}`. A separate scan of every display in the ten files found no unpunctuated display.
- **LONG-SENT artifacts.** The lint counts an environment opening plus the next sentence as one sentence: s6-1 keyresult (l.123), s6-2 caption, s6-3 l.66 and keyresult, s6-4 figure/workedexample/keyresult (l.79, 91, 105, 114), s6-5 l.57. The genuine over-long sentences are listed by section below.
- Clean checks: no hard-coded `Sect.~N`/`Eq.~(N)`/`Chap.~N`/`Fig.~N` outside `\cite[...]`; every cross-reference uses `\cref`. Citations are numeric, with equation or table locators wherever a result is used. All titles are short noun phrases (one 6-word subsection title, Sect. 6 item 14). There is no "I", no "you" and no contraction. There are no exercises or checkpoints, and the four posed questions ("Is the kick sudden?", "How well is α_F known?", "How fast …?", "How large is the remainder?") are answered at once, in the register, so they are not flagged.
- Forbidden constructions (i.e., e.g., respectively, in order to, thereby, whereby, one obtains/finds, it turns out), banned inflation words, em dashes and bullets: **none in the chapter**. The only list is the enumerate in D-18 l.27 (four intermediate-state paths). Those are genuinely enumerable, so it is acceptable.

## 2. Verdicts

| Unit | Words | Hits | Verdict | Main reasons |
|---|---|---|---|---|
| Chapter opening (ch06.tex) | 210 | 0 | PASS | Concrete, motivational, one orienting sentence |
| 6.1 Non-adiabatic coupling | 3.4k | 12 | REVISE | density-operator symbol; a check left to the reader (×2); undefined ω_opt; redundant close |
| 6.2 Electron–phonon matrix elements | 4.2k | 9 | REVISE | **𝐝** clash; undefined **w**; two convention/process notes |
| 6.3 Electron self-energy from phonons | 4.6k | 14 | REVISE | the 10 mK lesson stated three times; m_l/m_t; v_F at first use; uncited α_F claim; seam wording |
| 6.4 Phonon self-energy … | 3.0k | 13 | REVISE | Giustino reconciliations ×6; Migdal counting repeated; fig 6.6 caption; "only"/"gives" rates |
| 6.5 Phonon-assisted optical absorption | 4.7k | 10 | REVISE | E_dir at first use; Noffsinger convention sentence; captions; A-letter clash |
| Summary (in s6-5) | 0.95k | 4 | REVISE | ZPR comparison flatters; Kohn-anomaly attribution; "overlap … with itself" |
| D.16 | 1.7k | 3 | REVISE (minor) | numerical-check paragraph; "believed to be small" |
| D.17 | 1.5k | 4 | REVISE (minor) | numerical-check sentences; fourth copy of the Migdal counting |
| D.18 | 1.4k | 7 | REVISE | editor's D.18 fixes all still open (Sect. 9) |

Nothing is REWRITE. The voice is consistent across the five sections: authorial "we", concrete openers, an estimate before each exact result, worked examples with their digits. The REVISE grades come from notation, redundancy and process residue, not from systemic voice problems.

## 3. Register (REGISTER.md §4), per 10k words, math stripped

| | 6.1 | 6.2 | 6.3 | 6.4 | 6.5 | D.16–18 | L (target) |
|---|---|---|---|---|---|---|---|
| however | 0 | 2 | 2 | 0 | 2 | 0 | 8.0 |
| we can / note that / of course | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 | 0 | 13.6/6.1/3.6 |
| typical(ly) | 6 | 0 | 0 | 0 | 0 | 0 | 15.3 |
| for example / instance | 0 | 0 | 0 | 0 | 2 | 0 | 9.5 |
| only | 18 | 26 | 19 | **33** | **32** | 14–41 | 11 |
| gives | 12 | 17 | 17 | **37** | 21 | 28–47 | 7 |
| so | 9 | 17 | 17 | 10 | 6 | 21–34 | 11 |
| since (causal) | 9 | 19 | 9 | 10 | 13 | 7–14 | 13.9 |
| therefore | 6 | 9 | 2 | 7 | 4 | 0–7 | 2.9 |

The diagnosis in REGISTER §1 still holds. The prose is correct but carries almost none of the models' connective tissue ("however", "we can", "note that", "typical", "for example"), and it leans on "only" and "gives". "So" and "therefore" are back near the models' rates. Targeted fixes (one per paragraph, never mechanical):
- s6-2 l.30 "then costs only the matrix element in" → "then costs just one matrix element,".
- s6-4 l.96 "computed from first principles …, gives \SI{0.951}" → "corresponds to \SI{0.951}"; s6-3 l.43 "the two choices give" → "the two choices yield".
- s6-4 l.63 "No term survives. The phonons of an insulator are broadened only by" → "No term survives. However, the phonons of an insulator are still broadened, by anharmonicity …".
- s6-5 l.51 "Optical-phonon vertices in silicon are a few tenths of an eV" → "Typical optical-phonon vertices in silicon are a few tenths of an eV". This is the models' main hedge, and it is absent from 6.2–6.5.

## 4. Section 6.1 (s6-1.tex)

Issues (location → problem → fix):
1. l.46, l.48 `\op{n}(\vect{r})` → the density-operator ruling is open (editor-notes 6.1/6.2), and NOTATION l.398 gives 𝓃̂_e(r) → write `\op{\nd}_e(\vect{r})` in both places and in the clause "With the electron density operator …".
2. l.27 "as expanding $(\nabla + \vect{d})^2$, with $\nabla$ acting on everything to its right, confirms term by term" → this leaves a check to the reader (user rule) → write the one-line expansion, $(\nabla+\vect{d})^2 = \nabla^2 + 2\vect{d}\cdot\nabla + (\nabla\cdot\vect{d}) + \vect{d}\cdot\vect{d}$, or point to D.13 for it.
3. l.107 "larger than the free-recoil value by the factor $[1 - (\omega_{\mathrm{ph}}/\omega_{\mathrm{e}})^2]^{-2}$, which follows from the classical motion in the same way" → the step is not shown → give the driven-oscillator line, or cite the appendix equation that has it.
4. l.107 "$\omega_{\mathrm{opt}}/\Eg = 0.055$" → ω_opt appears nowhere else, and l.40 writes the same number as ω_ph/E_g → write "$\omega_{\mathrm{ph}}/\Eg = 0.055$ of the optical phonon of silicon", as in l.40.
5. l.38 "is 90 times faster than this zero-point estimate, $v_N/(\alpha\kappa_{\mathrm{BO}}^3) = 91$" → the round number and the exact one clash → "is 91 times faster than this zero-point estimate".
6. l.40 "about $10^{-2}$" → the editor wants "10⁻³ to 10⁻²" (6.4 l.49 has 0.0034 for Al) → "$10^{-3}$ to $10^{-2}$". The same applies at 6.3 l.177.
7. l.66 already sends the reader to 6.2 ("\cref{sec:6.2} derives the screened vertex and its physical forms"), and l.152 repeats it as the section close → pattern 5 → cut l.66's pointer clause, or shorten l.152 to its first sentence plus the pointer.
8. l.150 "Two different results carry Migdal's name …" restates l.40 (adiabatic theorem) and l.134 (Migdal effect). The paragraph has a real job, telling the two Migdals apart, so keep it but trim the 1958 half to one sentence: the counting is already in l.40.
9. LONG-SENT l.72 "To first order, \cref{eq:6.1-tdep} then yields, in the interaction picture of …, the amplitude of an excited state $j$ at energy …" → "In the interaction picture of \cref{eq:2.4-ipicture}, \cref{eq:6.1-tdep} gives to first order the amplitude of an excited state $j$, at $\Delta E_j = E_j - E_0$ above the ground state,".
10. LONG-SENT l.89 "In the frame of the nucleus, with $y = x - X(t)$ the position of the electron relative to it, the Hamiltonian is that of an oscillator pushed by the inertial force" → split: "Let $y = x - X(t)$ be the position of the electron relative to the nucleus. In the frame of the nucleus the electron is an oscillator pushed by the inertial force $-m_e\ddot X$,".
11. l.82 "If instead $\Delta E_j\tau_{\mathrm{acc}} \ll 1$, the phase does not move during the acceleration, the integral is just $\vect{v}_N$, and" → this chains three clauses → "If instead $\Delta E_j\tau_{\mathrm{acc}} \ll 1$, the phase stays fixed while the nucleus accelerates. The integral is then just $\vect{v}_N$, and".
12. l.134 "or recoil-induced ionization" → REGISTER #44 bans this as a name; here it is only a gloss after the field's name (allowed by R2) → optional cut.

Calibration (could Lin or Kahn–Lin have written it?):
- l.3, the opener ("They do, but not perfectly. Seen from the recoiling nucleus …"): **yes**. It is a picture with numbers, and the estimate comes before the formula.
- l.36 "It is a quantum correction to the classical trajectory, of order $\vect{d}^2/M$ against $v\,\vect{d}$ for the derivative coupling.": **no** (nominal, compressed). Lin's version: "Roughly speaking, the scalar coupling is the quantum correction to a classical trajectory, and compared to the derivative coupling it is suppressed by $|\vect{d}|/(Mv)$."
- l.150 (the two Migdal results): **yes**.

## 5. Section 6.2 (s6-2.tex)

1. l.34 "displaced by the same vector $\vect{d}$" (also 6.3 l.70 and D.16 l.85) → bold **d** is the derivative-coupling vector 𝐝_ji of 6.1, and 𝐝_ji itself is not in NOTATION → proposal: write the rigid translation as $\vect{a}$, or as $\vect{t}$ with $\op{T}_{\vect{t}}$ (check NOTATION: $a$ is the lattice constant), in 6.2, 6.3 and D.16, and add 𝐝_ji ("derivative-coupling vector, 6.1") to NOTATION.
2. l.81 "every cell acquires a dipole $eZ^*\vect{w}$" → **w** is undefined here → "a dipole $eZ^*\vect{w}$, with $\vect{w}$ the relative displacement of the two sublattices (\cref{sec:5.5})", or use the 5.5 symbol.
3. l.59 "Their vertex is $\ell_{\vect{Q}\nu}$ times a matrix element in eV per \si{\angstrom}, the form of \cref{eq:6.2-g}, so the constants enter here without conversion." → pattern 19, bookkeeping aimed at a reviewer → cut the sentence. The units are already stated in l.28.
4. l.97 "in the form of Ref.~\cite[Eq.~(1)]{verdi2015frohlich} with $e^2_{\mathrm{SI}}/\varepsilon_0^{\mathrm{SI}} \to e^2$ (\cref{eq:A.2-map}), the factor $N^{-1/2}$ moved into $H_{\mathrm{ep}}$, and the density vertex in place of the overlap $\delta_{mn}$" → pattern 19, a full sentence of convention reconciliation → keep one clause: "This is Fröhlich's vertex~\cite{frohlich1954electrons}, generalized to the density vertex $\rho_{mn}$ in place of the single-band overlap~\cite[Eq.~(1)]{verdi2015frohlich}."
5. l.28 "This is Ref.~\cite[Eqs.~(33)--(38)]{…} with its reference mass set to $M_{\mathrm{cell}}$, and the normalization of Ref.~\cite[Eq.~(2)]{ponce2016epw}." → acceptable attribution, but with item 4 there are two convention notes in one subsection → shorten to "This is the normalization of Refs.~\cite[…]{…} and~\cite[…]{…}."
6. l.3, the opener paragraph, has 8 sentences and three forward pointers → fine. But "The two behaviors decide much of what follows." is a count-teaser (rule 18) → cut it. The next three sentences name the consequences themselves.
7. l.59 "Across the valley axis the coupling is ten times weaker, \SI{2.6}{meV}." → good. However, the caption gives Ξ_d = 1.01 eV, which is a ratio of 9.75 → write "almost ten times".
8. l.162 "Its pitfalls are practical: a Wannier manifold …, a coarse grid …, a gauge …" → a triad, but each item has content → keep.
9. l.164 (section close) is a three-item roadmap of 6.3–6.5 that duplicates the chapter opener's last sentence → acceptable as a closing pointer (REGISTER 3.7), but trim it to the 6.3 pointer, since the 6.4 and 6.5 pointers recur in their own seams.

Calibration:
- l.3, the opener (two vertices, two numbers, the scaling): **yes**.
- l.28 "The form separates the two scales of the vertex. The zero-point length, a few hundredths of an Å for an optical phonon, carries the dependence on the frequency and on the mass. The matrix element of … is the change of the potential per unit mass-weighted displacement" → **no** (it narrates the equation factor by factor). Lin's version: "The zero-point length, typically a few hundredths of an Å, carries all the mass and frequency dependence; what is left is how much the potential changes when the atoms move, in eV per Å."
- l.97 "A static charge in the crystal is screened by electrons and ions together, through ε₀. The field of the displaced ions, as seen by the electrons, is screened by the electrons alone": **yes**.

## 6. Section 6.3 (s6-3.tex)

1. The "10 mK gap is zero-point" lesson appears at WE end (l.129), l.139 ("The lesson for a detector is the one at the end of \cref{we:6-zpr}") and l.181. The chapter opener and the summary also carry it → pattern 5 → cut l.139's last sentence, and make l.181 the single statement.
2. l.181 "For a silicon detector all three results point the same way." → a count-teaser and a vague verb → "For a silicon detector this section leaves three facts:" (or simply cut the sentence; the next three sentences stand alone).
3. l.181 "The same diagram, cut through the electrons instead of the phonon, broadens and shifts the phonons" → "cut" is the cutting-rule term the chapter uses for Im Σ, and 6.4 l.9 states the relation correctly → "The same two vertices, joined the other way into an electron loop, shift and broaden the phonons, the subject of \cref{sec:6.4}."
4. l.167 "$m^* = (m_lm_t^2)^{1/3} = 0.322\,m_e$" → NOTATION (l.278) has m*_∥, m*_⊥, and 6.5 l.72 writes $m^*_{\mathrm{d}} = (m^*_\parallel m^{*2}_\perp)^{1/3}$ → use $m^*_{\mathrm{d}}$ and the NOTATION components. Also make the value agree: 0.322 here against 0.32 in 6.5.
5. l.173 first use of $v_{\mathrm{F}}$ ("thickness $\omega_{\mathrm{D}}/v_{\mathrm{F}}$") with no gloss. NOTATION restricts v_F to the electron gas → "the Fermi velocity $v_{\mathrm{F}}$".
6. l.173 "$\lambda_{\mathrm{ep}}$ the dimensionless electron--phonon coupling, the number by which the coupling enhances the mass … $1 + \lambda_{\mathrm{ep}}$" → imprecise: the enhancement is 1+λ, not λ → "…coupling, defined so that the mass of an electron at the Fermi surface is enhanced by $1 + \lambda_{\mathrm{ep}}$ (\cref{sec:6.4})".
7. l.179 "the crossed diagram is smaller than the Fan--Migdal one by a relative order $\alpha_{\mathrm{F}}$" → uncited (editor-notes 6.3) → cite it, or mark it as an estimate: "by a relative order $\sim\alpha_{\mathrm{F}}$, by the same counting".
8. l.177 "about $10^{-2}$" → "$10^{-3}$ to $10^{-2}$" (editor-notes 6.4).
9. l.3 "to about ten percent" and l.117 "is a modelling choice" → the number style (\SI{10}{\percent}) and American spelling ("modeling") are wrong. l.117 also reads as a defensive aside → "The adiabatic weight of \cref{eq:6.3-einstein} applied to a non-adiabatic ZPR is an approximation; the two forms differ by \SI{8}{meV} at $T = 0$."
10. l.36 "together they are Ref.~\cite[…]{giustino2017electron} in the notation of this book" → pattern 19 residue → cut "in the notation of this book".
11. l.99 "and this book keeps that name for the factor (\cref{app:A.6})" → a useful naming note, but it is phrased as book bookkeeping → "Note that it is a different object from the Debye–Waller factor $\ee^{-2W_\kappa(\vect{q})}$ of \cref{sec:5.6}, to which we reserve the name."
12. l.66 "In the Fan sum … the energy difference appears squared in the numerator and once in the denominator, and the mode contributes" → this narrates the formula; it can stay short → "Squared in the numerator and once in the denominator, the energy difference leaves".
13. l.86 "That correction has been shown to be large in molecules" → the passive hides the agent → "Poncé et al.\ find that correction large in molecules~\cite{ponce2015temperature}; for crystals the rigid-ion form is standard."
14. The l.60 subsection title "Translational invariance and the rigid-ion approximation" is 6 words, and "translational invariance" (6.3, 6.5, D.16) alternates with "translation invariance" (6.1, 6.2, 6.5, summary) → pick one book-wide. "Translation invariance" is the shorter.

Calibration:
- l.3 opener ("At 10 mK a silicon crystal holds no thermal phonons, yet …"): **yes**.
- l.81 "The Allen–Heine vertex needs second derivatives …, a second-order perturbation calculation that few codes perform. Translational invariance offers a way around it.": **yes**.
- l.112 "That straight line passes through zero at $T = 0$. Extrapolated back from high temperature, a measured gap lands on the gap of the clamped lattice" → **no** (it states the result before the reason). Lin's version: "Since the high-temperature line extrapolates to zero shift at $T = 0$, extrapolating a measured gap back from high temperature lands on the clamped-lattice gap, and the low-temperature gap sits below it by the ZPR."

## 7. Section 6.4 (s6-4.tex)

1. There are six Giustino reconciliations: l.26 (×2), l.45 "in Giustino's notation the subtraction $W_e(\omega) - W_e(0)$", l.61 "Giustino writes the same rate as an inverse lifetime with the spin sum implicit", l.70 "with Giustino's $\gamma$ a half width", l.79 "This is Ref.~\cite[Eq.~(205)]", l.89 → pattern 19 by accumulation. They are needed in D.17, which repeats them all → keep one convention clause in the text (the full-width note at l.89) and move the rest to D.17.
2. l.89 "The numerical factors assume, as everywhere in this book, a full width and a density of states per spin" → this is a consistency assurance → "With a full width and a density of states per spin the factors are as written; a half width or a two-spin $\mathcal{N}_{\mathrm{F}}$ changes them by factors of two (\cref{eq:D.17-lambda})."
3. l.49 (vertex corrections) re-derives the Migdal counting of 6.3 l.173–177 and repeats its failure list ("small Fermi surfaces, flat bands, and … $v_{\mathrm{F}}Q \lesssim \omega$"). This is the third copy in the chapter and the fourth with D.17 l.89 → compress it to "The same counting as for the electron self-energy (\cref{sec:6.3}) makes vertex corrections to the bubble of relative order $\lambda_{\mathrm{ep}}\omega_{\mathrm{D}}/E_{\mathrm{F}}$, at most 0.0015 for aluminum."
4. l.108 caption: "The transverse peak is suppressed, although three quarters of the modes lie below \SI{32}{meV}, in $\alpha^2F$ because a transverse displacement couples …" → the word order is garbled → "In $\alpha^2F$ the transverse peak is suppressed, although three quarters of the modes lie below \SI{32}{meV}, because a transverse displacement couples to an electron only through umklapp momentum transfers."
5. l.108 caption uses $\omega_{\log}$ before the text defines it (l.112), and quotes "0.44 and \SI{270}{K} from linear-response calculations and 0.42 from tunneling" with no citation → the caption must stand alone → add "(the logarithmic average frequency)" and \cite{savrasov1996electron}.
6. l.115 WE: $A_{\mathrm{TA}}, A_{\mathrm{LA}}$ are α²F weights (in meV), while 6.5 uses $A_\nu$, $A_{\mathrm{TA}}$, $A_{\mathrm{TO}}$ for edge coefficients → the same letter has two meanings (editor-notes 6.5) → rename the α²F weights $w_{\mathrm{TA}}, w_{\mathrm{LA}}$, or $I_{\mathrm{TA}}, I_{\mathrm{LA}}$ (check NOTATION).
7. l.47 "Calandra, Profeta and Mauri report corrections of up to 30 percent~\cite{…}, which is why graphite intercalation compounds and doped graphene are the standard examples, and why the adiabatic frequencies are the right starting point everywhere else." (LONG-SENT) → "\SI{30}{\percent}", and split: "… report corrections of up to \SI{30}{\percent} there~\cite{…}; graphite intercalation compounds and doped graphene are the standard examples. Everywhere else the adiabatic frequencies are the right starting point."
8. l.79 LONG-SENT "The symbol is read as one: if $|g|^2$ were the same …, and the historical notation splits it this way into a coupling $\alpha^2(\omega)$ and a density $F(\omega)$." → the colon-reveal runs past 50 words → end the sentence after "phonon density of states $g_{\mathrm{ph}}(\omega)$ of \cref{eq:5.2-dos}." and start a new one: "The historical notation splits it this way …".
9. l.98 is a 9-sentence model paragraph (force constants, gas, pseudopotential, umklapp, integrals) → split before "The electrons are a free gas" so that phonon model and electron model each get a paragraph.
10. l.121 "the transverse branches carry 70 percent of the coupling" → "\SI{70}{\percent}".
11. l.3 "whose relation to the self-energy has to be clear before any correction is added to it" → slightly abstract → "and adding a self-energy correction to it double-counts unless the static part is removed (\cref{eq:6.4-nonad})". That names the content.
12. Text and appendix duplicate each other almost verbatim: l.26 ≈ D.17 l.15 (dropped branch-mixing bubbles), l.36 ≈ D.17 l.27 (sign of the static part), l.70 ≈ D.17 l.53 (Allen formula validity), l.9 ≈ D.17 l.15 ("which is why a phonon is screened by the same transitions") → keep the physical sentence in 6.4 and cut the duplicate in D.17, or keep the derivation detail in D.17 only.
13. l.126 (close) is good. It ends on a consequence (REGISTER 3.7).

Calibration:
- l.3 opener (Al phonon vs Si optical phonon, "What differs is whether real pairs exist at the phonon's energy."): **yes**.
- l.26 "The form keeps the screened vertex $g$ at both ends and noninteracting electrons between them, as in Ref.~[Eq.~(146) and the text before it]. The exact self-energy has the bare vertex at one end …" → **no** (written to a reviewer). Lin's version: "Note that we have put the screened vertex at both ends; strictly, one end should be bare, and we will see below why this matters only for the static part."
- l.112 "The shape carries more information than the number. Compared to the density of states, the transverse peak near \SI{23}{meV} is strongly suppressed. The reason is the factor …": **yes**, the REGISTER 3.5 move exactly.

## 8. Section 6.5 (s6-5.tex)

1. l.24 "In a frozen lattice this vanishes below $E_{\mathrm{dir}}$." → first use in the text. l.3 gives "the smallest vertical gap … \SI{3.4}{eV}" without the symbol, and only the caption (l.40) defines it → l.3: "Yet the smallest vertical gap of silicon, $E_{\mathrm{dir}}$, is \SI{3.4}{eV}".
2. l.64 "That reference writes the charge in Gaussian units, $e_{\mathrm{G}}^2 = e^2/4\pi$ (\cref{app:A.2}), shows the spin factor explicitly, and multiplies the occupation factor by $f_{v\vect{k}} - f_{c,\vect{k}+\vect{Q}}$, which is one for $T \ll \Eg$; it is also Ref.~\cite[Eq.~(200)]{giustino2017electron}." → pattern 19, a full-sentence reconciliation → "In Gaussian units, $e_{\mathrm{G}}^2 = e^2/4\pi$, this is the form of Refs.~\cite[Eq.~(1)]{noffsinger2012phonon} and~\cite[Eq.~(200)]{giustino2017electron}."
3. l.40 caption "the process runs through the hole ordering described in the text" → not standalone → "the process runs through hole orderings, in which an electron from an occupied band is promoted first and the valence electron fills the hole (sign $-1$), so the denominator never vanishes."
4. l.129 caption "Modelling choices: equal coefficients …" → British spelling and a process label → "The two branches are given equal coefficients $A_{\mathrm{TA}} = A_{\mathrm{TO}} = A$, so their relative heights are illustrative; the gap is held at its low-temperature value …; excitonic thresholds, \SI{14.7}{meV} lower, are omitted."
5. l.57 LONG-SENT "The final states are labeled by $\vect{k}$, $\vect{Q}$, $\nu$, $c$, $v$, the spin and the sign, and summing over them we obtain" → "Summing over the final states, labeled by $\vect{k}$, $\vect{Q}$, $\nu$, $c$, $v$, the spin and the sign, we obtain (\cref{app:D.18})".
6. l.3 "This is the first composite process of the book" → a book-structure remark → keep, or change to "It is the simplest composite process:" so that it reads as physics.
7. l.51 "A rough size follows from \cref{eq:6.5-M} before any calculation." → a good REGISTER 3.1 move. "a percent-level fraction" → "about \SI{1}{\percent}" (or "$\sim10^{-2}$"), which removes the spelled "percent".
8. l.112 and the WE (l.149) both state $\ee^{-21200}$, and l.112 forward-points to the WE → keep only the WE value, and say "vanishingly small" at l.112.
9. l.154 is a 9-sentence paragraph. "Its vertex is the matrix element of $n_e(\vect{q}) = \int\dd^3r\,\ee^{\ii\vect{q}\cdot\vect{r}}\,\op{\nd}_e(\vect{r})$" is consistent with NOTATION (l.180, l.398), which is good. Split the paragraph after "…instead of two."
10. l.156 "even smaller compared to its energy than a photon's" → awkward → "a smaller momentum for its energy than a photon carries".

Calibration:
- l.3 opener (solar cells vs the 3.4 eV vertical gap): **yes**.
- l.51 (rough size before any calculation): **yes**.
- l.64 (the Noffsinger units sentence): **no**. Lin's version: "This is the expression used in first-principles work~\cite{noffsinger2012phonon}, written there in Gaussian units."

## 9. Appendices D.16–D.18

- D.16 l.121 "A numerical check confirms the steps. Take a one-dimensional crystal of three cells …" (whole paragraph), D.17 l.91 "A numerical quadrature … confirms the two to $10^{-5}$ … machine precision … falls short … by \SI{1}{\percent}", and D.18 l.38 "A model with seven orbitals … agrees with it to machine precision" → these are pattern 19 (verification reports addressed to a reviewer). The editor asked for the D.18 sentence to be cut → treat all three the same way: cut them, or keep one clause each where it carries physics. The D.16 rigid-ion failure of \SI{66}{\percent} with a bond-centered well is real physics worth one sentence in the l.119 discussion, and the D.17 finite-band shortfall $\omega'/(W+\omega')$ is worth one clause.
- D.16 l.39 "in the notation of this book" → cut.
- D.16 l.119 "In crystals the neglected term is believed to be small" → an unattributed hedge → "In crystals the neglected term is usually taken to be small; Ref.~\cite{ponce2015temperature} reports that it is large in molecules."
- D.17 l.89 → this is the fourth statement of the Migdal counting and failure list → keep it as the full statement, and let 6.4 point here (Sect. 7, item 3).
- D.18 l.75 "a plot of $\sqrt{\alpha_{\mathrm{abs}}}$ against $\omega$ is a sequence of straight segments" → false for the sum, and 6.5 l.99 says so (editor-notes) → "each component of \cref{eq:D.18-edge} is a straight line in a plot of $\sqrt{\alpha_{\mathrm{abs}}}$ against $\omega$; their sum bends at every threshold".
- D.18 l.75 "the ratio of the coefficients of the two branches, $n_\nu/(n_\nu+1)$" → "branch" means phonon branch everywhere else, and 6.5 says "components" → "of the two components of a branch".
- D.18 l.53–64 `m_{\mathrm{e}}` for the valley density-of-states mass → this clashes with the electron mass → $m^*_{\mathrm{d}}$ as in 6.5 (editor-notes, open).
- D.18 l.7 and throughout: bare $\hat{\vect{e}}$ → $\hat{\vect{e}}_\gamma$ as in 6.5 (open). l.26 $W_{ab} = \hat{\vect{e}}\cdot\vect{v}_{ab}$ → this clashes with W_κ (Debye–Waller), W_AB and the band width W of D.17 → propose $\Pi_{ab}$ or simply $\hat{\vect{e}}_\gamma\cdot\vect{v}_{ab}$ written out (open).
- D.18 l.7 "with $\op{\vect{V}} = \sum_j\vect{p}_j/m_e$ the total velocity" → 6.5 l.15 restricts this to a local potential → add "for a local potential".

## 10. Chapter as a whole

**Opening (ch06.tex l.3): PASS.** It opens on a number (1.17/1.12 eV, 60 meV), then the question (why the static lattice misses it), why it matters for detection (indirect gap, carrier cooling, Migdal), and one closing orientation sentence. It is not an outline. Nit: "it decides whether the electrons stay behind" → "the coupling decides …".

**Summary (s6-5 l.158–168): REVISE.**
- l.164 "the computed zero-point renormalization is \SI{-56.2}{meV}, against \SI{-62}{} to \SI{-64}{meV} extracted from experiment" → this flatters the comparison. 6.3 l.105 says the e–ph part implied by experiment is −71 to −73 meV after the +9 meV zero-point expansion, so the calculation is ≈\SI{20}{\percent} short → "against $-71$ to \SI{-73}{meV} for the electron–phonon part implied by experiment, once the zero-point expansion of the lattice is removed".
- l.166 "in an insulator that difference is of relative order $(\omega/\Eg)^2$, and in a metal it leaves Kohn anomalies in the dispersion" → misattributed. The Kohn anomaly comes from the static bubble (6.4 l.36), not from the dynamic–static difference → "…of relative order $(\omega_{\vect{Q}\nu}/\Eg)^2$. In a metal the static bubble leaves Kohn anomalies in the dispersion."
- l.160 "the overlap of the boosted ground state with itself gives the probability that nothing happens to them" → wrong object; it is the overlap with the unboosted ground state → "the overlap of the boosted ground state with the original one". The same sentence is LONG-SENT → split at "suddenly,".
- l.160 "this chapter restored the rest" and the WORDY "Written in terms of the nuclear velocity" → "Written with the nuclear velocity". The summary runs to about 950 words, so trimming about 20 % would match the sections' own closing paragraphs.

**Redundancy across sections.**
- Migdal counting and its failure list: 6.1 l.40, 6.3 l.169–179, 6.4 l.49, D.17 l.89 → the full statement goes in 6.3; 6.1 keeps the estimate; 6.4 gets one sentence (Sect. 7, item 3).
- ω_ph/E_g = 0.055 as the insulator's small parameter: 6.1 l.40 and l.107, 6.2 l.17, 6.3 l.179, 6.4 l.47 (squared) → this is a deliberate thread, so keep it, but write ω_ph consistently (Sect. 4, item 4).
- 60 meV ZPR in the chapter opener, 6.3 l.3 and summary l.164: acceptable (opener → section → summary).
- Acoustic cancellation: announced 6.2 l.46, derived 6.3 l.74–79 → good division of labor.

**Seams** (each adjacent pair read across the join).
- 6.1 → 6.2: smooth. 6.1 ends on the screened vertex as the next object, and 6.2 opens with two vertex values. Remove the double pointer (Sect. 4, item 7).
- 6.2 → 6.3: 6.2 ends with a 3-section roadmap and 6.3 opens concretely → trim the roadmap (Sect. 5, item 9).
- 6.3 → 6.4: the wording "cut through the electrons" conflicts with 6.4 l.9 → fix as in Sect. 6, item 3.
- 6.4 → 6.5: 6.4 ends pointing to Chap. 7, and 6.5 opens on solar cells → this is a topic jump, but a clean one. The 6.5 opener ties back via "the electron–phonon vertex $g$ of \cref{sec:6.2}", which is enough.
- 6.5 → Summary: fine.

**Book-wide consistency sweeps** (one fix each).
- "non-adiabatic" (13×: 6.1, 6.3, 6.5) vs "nonadiabatic" (5×: 6.4, D.17) → American usage and Ch6's own subsection title in 6.4 suggest "nonadiabatic" → sweep, including the 6.1 title "Non-adiabatic coupling" → "Nonadiabatic coupling".
- Spelled "percent" (s6-2 l.126, s6-3 l.3 and l.179, s6-4 l.47 and l.121, s6-5 l.51) vs \SI{}{\percent} elsewhere → use numerals with \SI for counts; a vague "a few percent" may stay.
- "modelling" ×2 (s6-3 l.117, s6-5 l.129) → "modeling".

**Structural note for the editor (not a verdict driver).** Ch6 has no `limitbox`. The Fröhlich vertex (6.2), Allen's formula (6.4) and the HBB edge (6.5) are literature formulas recovered as limits, and they sit in `keyresult`, with fig 6.2 and fig 6.8 doing comparison-plot work. Whether STYLE's limitbox rule applies here is a structural decision above this review.

## 11. Editor-notes items concerning prose: status

| Item | Status |
|---|---|
| 6.1 density operator 𝓃̂ (\hat{\nd}) instead of \op{n} | **open**: s6-1 l.46, 48 |
| 6.1 ω_e upright | done |
| 6.2 Fig 6.2 caption says it plots the limiting formulas | done (l.132 "these limiting forms, not vertices computed point by point") |
| 6.3 delivers the Q→0 acoustic cancellation promised in 6.2 | done (eq:6.3-cancel) |
| 6.5/D.18 "√α is straight segments" applies per component only | 6.5 done (l.99); **D.18 l.75 open** |
| D.18 cut the "machine precision" sentence | **open** (D.18 l.38; same pattern in D.16 l.121, D.17 l.91) |
| D.18 m_e → m*_d; ê → ê_γ; W_ab clash | **open** (all three) |
| 6.3 and 6.4 summary paragraphs re-read once final | done here: 6.3 ZPR comparison and 6.4 Kohn-anomaly attribution need fixing (Sect. 10) |
| A_ν vs A_TA/A_LA letter repeat | **open** (s6-4 l.115 vs s6-5 l.95, 129) |
| n_r first use in 6.5 | done (s6-5 l.24) |
| 6.3 says ω_D/E_F is "10⁻³ to 10⁻²" | **open** (s6-3 l.177; also s6-1 l.40) |
| 6.3 cite the Fröhlich vertex-correction ∼α_F claim or mark it as an estimate | **open** (s6-3 l.179) |
| 6.4 "up to 30 %" cited to Calandra | in text with citation; spelling fix only (Sect. 7, item 7) |
