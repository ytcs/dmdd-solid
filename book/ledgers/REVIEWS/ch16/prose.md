# Ch. 16 prose review (isolated): style, register, arrangement

Scope: tex/ch16/ch16.tex, s16-1 … s16-9, s16-summary; tex/appD/D-41.tex, D-42.tex. Checked against STYLE.md, style-guide.md, prose-review.md (patterns 0–26), REGISTER.md and the prose items of editor-notes.md. Line numbers are file lines. The tex was not edited.

Length (detex words; budget from the section ledgers): 16.1 2,636/4,500 · 16.2 4,398/4,500 · 16.3 3,491/4,500 · **16.4 3,917/3,500 (+12 %)** · 16.5 2,946/4,000 · **16.6 4,022/4,000 (raw 4,302)** · **16.7 5,012/6,000 (raw 5,746; longest section, 16 genuine >45-word sentences)** · 16.8 3,797/4,500 · 16.9 2,381/3,000 · summary 2,440 · D.41 1,200 · D.42 1,171. Total ≈ 35,000. Cuts that bring 16.4, 16.6 and 16.7 back under budget, and the chapter down by about 1,500 words, are listed in §8.

## Verdicts

| Unit | Verdict | Main reason |
|---|---|---|
| Chapter opening (ch16.tex) | REVISE | a catalogue of the eight targets in section order (an outline in prose); "this chapter asks" frame; British "tunnelling" ×4; map caption lists only 2 of 17 Limit Checks |
| 16.1 Dirac-material rates | REVISE | the opener's "≈ 2550" is the number the section later rejects (4800–6600); l.33 repeats D.41 argument by argument; two reviewer-facing asides; colon in the Limit Check title |
| 16.2 Low-dimensional plasmons and layered stacks | PASS (minor) | v_D = 3.41e-3 here against 3.02e-3 in 16.3; pointer to App. C.8 for I₀, K₀, which C.8 does not contain; "four to seven times" contradicts the 3.6 of l.74 |
| 16.3 Graphene, nanotubes and quantum dots | REVISE (light) | two process artifacts (misprint aside l.27, "machine precision" l.76); a_cc/t here against a_CC/γ₀ in 16.2; double colon l.33 |
| 16.4 Molecular crystals | REVISE | over budget; three count-teasers; the E.21 periodic calculation announced three times; ends on a recap; Mataga–Nishimoto form and U uncited |
| 16.5 Dopants | REVISE (light) | new symbol W in lim:16.5a for L^D; "f-sum" vs "$f$-sum"; numerical-check assurance l.37; the conditions of l.112 taken second, first, third |
| 16.6 Color centers and broken bonds | REVISE | over budget; last paragraph restates l.14 and l.115; p_esc used (l.110) before it is defined (l.115); NV paragraph off the subsection's topic |
| 16.7 Glasses, random media and two-level systems | REVISE | 16 genuine long sentences; ε_r and ε₁ for one quantity; α, C, A, B and "IR" reused with new meanings; undefined "MICROSCOPE"; restating sentences after the key result |
| 16.8 Two-level systems at millikelvin | REVISE (light) | re-derives the σ_z rotation of eq:16.7-rot; Γ₁ vs τ₁⁻¹; "that Lawrence calls the instanton"; l.118 attributes freezing to "the crossover"; s undefined (l.179) |
| 16.9 Material inputs of the novel targets | REVISE | l.44 and l.73 recap the published-rate corrections and the table, which the Summary does again; opener promises two classes, the section gives three |
| Summary | PASS (minor) | omits the vibrational absorption of glasses (16.7.4); "each has a direct measurement" reads as "has been measured" |
| App. D.41 | PASS (minor) | opens with "This appendix derives …" |
| App. D.42 | PASS (minor) | same opener; a numerical-agreement sentence at the end |

## 1. Lint (lint.py with BANNED-TERMS.txt)

0 blocking hits in every file; no banned or internal terms. ch16.tex and D-41: 0 hits.
- EQ-PUNCT: s16-3 l.20; s16-4 l.19; s16-5 l.8, 50; s16-6 l.17, 48, 77; s16-8 l.77, 166; D-42 l.51. **All false positives**: the punctuation sits on the last line inside `gathered`/`split`. Equation punctuation is clean chapter-wide.
- LONG-SENT: s16-1 3 (two captions, l.37); s16-2 4 (l.25/30, l.57–61, two captions); s16-3 2 (captions); s16-4 2 (caption, l.82); s16-5 3 (caption, l.71, WE); s16-6 3 (caption, l.71, caption); **s16-7 22 (16 genuine, 6 artifacts of a display or box joining two sentences; see §4)**; s16-8 6 (caption, box joins, l.68, l.179); s16-9 3 (table caption/cells, l.42); summary 9 (2 prose, 7 table cells); D-42 2 (l.30, l.37).
- MONOTONY: s16-2 WE 16-demon (l.144–146); s16-8 l.3. Both read acceptably; vary one sentence in each if touched.

## 2. Chapter-wide findings

**C1. Chapter opening is an outline (STYLE "motivational, not outline"; pattern 18).** ch16.tex l.2 walks through the targets in section order ("The slow linear bands of a Dirac material … Electrons confined to sheets … The response of a molecular crystal … dopants, color centers and the tunnelling defects of glasses …") and then frames the chapter abstractly ("For each of these targets this chapter asks whether it adds a channel …"). → Fix: keep the first sentence (0.333 MeV); replace the catalogue with the stakes the chapter delivers, e.g. "Several have been proposed with projected reaches that a correct treatment moves by orders of magnitude: the published Dirac-material reaches leave the remote bands out of the screening and are too strong by ε_bg², a factor of 10³–10⁴ in ZrTe₅, and the printed quantum-dot rate is 4×10⁴ too large." Keep "In most cases the limit is a material input …: a background dielectric constant, a density of tunnelling states, the yield of a defect" (good). One closing sentence pointing to the map.

**C2. Map caption (STYLE chapter maps; editor notes 16.1, 16.3, 16.8).** fig:16-map tags lim:16.1a and lim:16.4a only. → Add lim:16.2a–c, 16.3a–b, 16.5a, 16.6a, 16.7a–d, 16.8a–d (and rerun map16.py so the nodes carry them).

**C3. Spelling.** "tunnelling" ch16.tex l.2 (×3), l.7, against "tunneling" everywhere else → "tunneling". "labelled" s16-1 l.64 → "labeled". "87 per cent" s16-7 l.36 → \SI{87}{\percent}. "+6 to +35~\%" s16-9 l.26 and summary l.49 → \SI{}{\percent} as elsewhere. "f-sum" s16-5 l.62, 71 (×2) → "$f$-sum" (the other eight uses). "rms" s16-6 l.98 → "root-mean-square" (as s16-4 l.85).

**C4. Rate units phrased five ways.** "per kilogram-year" (16.1, 16.4), "per kg-year" (16.3, 16.5), "per kg and year" (16.7), "in a kilogram-year", "per kg, day and meV". → Pick "per kg-year" and "per kg, day and meV" (or the spelled-out pair) and use it in all sections.

**C5. One symbol, one value (NOTATION).** Graphene v_D = 3.41×10⁻³ from a_CC, γ₀ = 3.16 eV (s16-2 l.55, fig:16-dispersion, lim:16.2a caption) against 3.02×10⁻³ from a_cc, t = 2.8 eV (s16-3 l.69); Table 16.1 l.22 prints both ("3.02 or 3.41×10⁻³"). Also a_CC vs a_cc and γ₀ vs t for the same hopping. → Unify (editor ruling pending), then delete the Table 16.1 clause. τ₁⁻¹ (s16-7 l.60–66, 16.8 figure captions) vs Γ₁ (s16-8 throughout) for one rate → one symbol. ε_r and ε₁ both for the real permittivity of the glass (s16-7 eq:16.7-tand, fig:16-limit-ir "ε₁ = 3.9") → ε_r throughout 16.7.

**C6. Register (REGISTER §4, per 10k words; Lin in brackets).** "gives" 21 [7], "so" 20 [11], "only" 20 [11], "about" 11.5 [5], "of order" 4.5 [0]; "typical(ly)" 0.6 [15], "however" 2 [8], "we will/can" 2 [26], "for example" 0.3 [7], "note that" 0 [6]. Better than Ch. 1 on "so", still flat on connectives. → In each section turn a third of "gives" into "is"/"leads to"; replace "of order" with "∼" or "typical" in prose (s16-1 l.37 "of order ten", l.79 "of order one", s16-7 l.13 "of the order of"); add "however"/"note that" at real contrasts (candidates in §3: s16-4 l.62, s16-7 l.96, s16-9 l.9).

**C7. Redundancy across sections.** (a) The σ_z rotation into the eigenbasis appears in s16-7 l.14–18, again in s16-8 l.7 and again in D-42 l.7 → keep 16.7 and D.42; in 16.8 write "By \cref{eq:16.7-rot} only the off-diagonal element Δ₀/Δ_tl changes the state, so …". (b) The deformation-potential convention is set in s16-7 l.40, repeated in s16-8 l.14 and D-42 l.11 → 16.8 cites eq:16.7-H1 only. (c) The published-rate corrections (ε_bg², μ/4ω, ×4 nanotube, 4.84 donor) are recapped in s16-9 l.44, s16-9 l.73 and summary l.19 → keep the summary. (d) "estimate, not a bound" s16-9 l.9 and l.73 → keep l.9. (e) s16-1 l.23 and l.33 repeat D-41 l.29 and l.43–51 nearly step by step (three-piece construction, Eq. (3.13) cutoff identity, "mediator that couples to the Dirac electrons alone") → in 16.1 keep the key result and two sentences of reason; point to D.41 for the rest.

**C8. Seams.** 16.1→16.2: no link, though nanotubes and graphene are Dirac materials of lower dimension → open 16.2 with a clause such as "Confine the Dirac electrons of \cref{sec:16.1} to a tube and …". 16.3→16.4: both end on photon readout (dot re-emission, organic scintillation) and could share it in a clause; otherwise clean. 16.5→16.6: good (readout of a final state on both sides). 16.7→16.8: good. 16.8→16.9: abrupt return to ZrTe₅; acceptable for a synthesis section, but the 16.9 opener should name its role ("Most of the uncertainties of this chapter are material inputs: …"). 16.9→Summary: 16.9 ends on a recap that the summary repeats (C7c).

**C9. Summary.** Stands alone and is correct; it is the one sanctioned recap. (a) No sentence on 16.7.4: add "Below the Ioffe–Regel frequency the vibrations of silica absorb through the constant term A^IR of random Born charges, and overtake the two-level systems of thermal SiO₂ above 0.46 meV." (b) l.13 "Four yields at millikelvin temperatures are open, and each has a direct measurement" → "…, and each can be measured directly (\cref{sec:16.6-yields})". (c) l.13 "A color center is not a prompt final state:" → "A color center forms after the prompt window:". (d) l.19 "of another order" (ambiguous) → "larger by three orders of magnitude".

## 3. Issues by section (location → problem → fix)

**16.1**
- l.3 → "the two differ by ε_bg² ≈ 2550 in the scattering rate": 2550 is the harmonic-mean estimate that l.64 rejects ("more than the square of the harmonic mean, 50.5² = 2550"); the opener sets up a wrong number. → "and for ZrTe₅ the two differ by a factor 4800 to 6600 in the scattering rate."
- l.3 → two outline sentences ("With the background … we obtain …", "We then derive …") → one: "We derive the loss function with ε_bg in the total ε, the change of the published reaches, the anisotropic case of ZrTe₅, and where one loop fails."
- l.17 → α̃ used before its definition at l.35 → define at l.17: "g_deg α̃, with α̃ = α/(ε_bg v_D), times a logarithm".
- l.33 → "In the anisotropic in-medium factor of Ref. [Eq. (3.14)] … the term of the x axis reads q_x²v_{F,z}² for q_x²v_{F,x}²; we use the latter." Misprint report aimed at a reviewer (pattern 19). → Cut, or one clause in D.41.
- l.33 → "The factor is not tied to the cutoff either. Absorbing the constant 1 … is an identity that both rates share, and the explicit ε_bg² …" duplicates D-41 l.45–51 → replace by "The factor survives the rescaling of the cutoff used in the original analysis (\cref{eq:D.41-lprime})."
- l.37 → 50-word sentence ("In the published form the scattering rate grows … of order ten found in Ref. [Sect. 4.2]") → split after "|ε_D|, 7.6 at 50 meV in the material of lim:16.1a."; "of order ten" → "∼10".
- lim:16.1a title "Dirac-material rates: the background in the total dielectric function" → colon title (STYLE) → "Background screening of Dirac-material rates".
- l.64 → "The half-gap is the number that enters eq:7.3-H. The reference lists it in a column labelled as band gaps, but its text states …" three sentences of source bookkeeping (pattern 19) → one clause: "Δ_D = 15.6 meV, half the computed gap of 31.2 meV that the reference tabulates~\cite[…]".
- l.77 → "The corrections of next order are of three kinds." count-teaser (pattern 18) → "At next order the electron–hole ladder, the self-energy and vertex of the carriers, and the material outside the model all enter."

**16.2**
- l.3 → "four to seven times faster than any particle of the halo" vs l.74 "7.3, 5.7 and 3.6 times v_max" → "four to seven times faster at momenta below 10 eV" or "3.6 to 7.3 times".
- l.39 → "with I₀ and K₀ the modified Bessel functions of \cref{app:C.8}": C-8.tex contains neither (editor note 16.3). → Repoint or add them to C.8.
- l.55 → the graphene velocity is defined after its use in l.3 and fig:16-dispersion, and differs from 16.3 (C5). → Define v_D for graphene once, at first use, with the unified value.
- l.121 → "The rate follows from it through their Eqs. (1) and (2), which are \cref{eq:4.4-SL} inserted in \cref{eq:8.2-spectrum}" provenance mapping → "Their rate is \cref{eq:4.4-SL} inserted in \cref{eq:8.2-spectrum}~\cite[Eqs.~(1), (2)]{…}."
- lim:16.2b body → attributes the 2D width to "the random-phase response of Ref. [Eqs. (13)–(19)]{das2023sub} with two bands", a bilayer-graphene paper with no acoustic plasmon (l.55 says its loss function "has no sheet plasmon"). → Say the 2D width is derived here; cite das2023sub only for the 2D Lindhard response, or drop it.
- fig:16-demon-limit → "too broad and asymmetric for its width to mean much" colloquial → "too broad and asymmetric for a width to be defined".

**16.3**
- l.27 → "Their text defines the recoil energy as k'²/2M_χ where k'²/2m_e is meant, a misprint that leaves the integral as written unaffected." Affects nothing (pattern 19) → cut.
- l.33 → "The symptom is the limit q → 0: M_PW → ψ̃(p), which is not zero: plane waves …" two colons → "As q → 0, M_PW tends to ψ̃(p), which is not zero, so plane waves predict ejection …".
- l.38 → "A table of ratios is not a rate correction; the rate weights each (p, q) by the halo." negation framing → "The rate weights each (p, q) by the halo, so these ratios bound the correction without giving it."
- l.69 → "which Castro Neto et al. round to 10⁶ m s⁻¹" bookkeeping → cut after C5 is settled.
- l.76 → "A direct integration over k at finite q_∥ agrees with \cref{eq:16.3-R1D} to machine precision." numerical assurance (pattern 19) → cut; the symmetry argument already makes the result exact.
- l.116 → "The deficit has a simple origin." low content → "The deficit comes from the surface."

**16.4**
- l.3 → three orienting sentences at the end ("We will derive … A model of anthracene then sizes …") → one.
- l.28 → "The environment is not a small effect. In anthracene it lowers the lowest singlet by 0.4 eV, from 3.5 to 3.1 eV." repeats the opener's numbers and opens with a negation → "In the crystal the environment lowers the fundamental gap from 6.9 eV to 3.9–4.2 eV, …" (drop the singlet repeat).
- l.28 last sentence, l.85 last sentence, l.97 last two sentences → the same E.21 periodic calculation, three times (pattern 26) → keep only l.97's statement of what it outputs.
- l.44 → "Three conditions stand behind \cref{eq:16.4-binned}, and each fails in a definite way." count-teaser → "\Cref{eq:16.4-binned} needs the window to hold whole manifolds, ε_mac and η to stay flat across it, and the vertex to be bare."
- l.49 → "This intensity borrowing is of first order in 𝔍/ΔE, not second:" "not second" answers a past correction (pattern 19) → "This intensity borrowing is first order in 𝔍/ΔE: the cross term …".
- l.60 → "Mataga–Nishimoto form" and "one-center repulsion of 11.13 eV" uncited (editor note) → cite or state "a standard parametrization".
- l.62 → "and its B_b transition is strong" as a caveat is unexplained → say what follows from it ("and its strong B_b transition makes the borrowing of l.85 an upper estimate"), or cut.
- l.85 → "\Cref{fig:16-limit-frenkel} separates three effects." count-teaser; 12-sentence paragraph → name them ("intensity borrowing far above threshold, band dispersion near it, and the macroscopic term"); split before "The dash-dotted curve".
- l.97 → "Four further corrections are of known form." count-teaser → begin with the first: "The nuclei move when a molecule is excited, …".
- l.112 → "Compared to silicon, whose electronic rate modulates by 0.9 % …, the reason is the crystal class." dangling comparison → "The modulation is a hundred times silicon's 0.9 % at 2 MeV because of the crystal class."
- l.112 last sentence "The model rates rest on the binned form, whose corrections … and on π-electron form factors, which … would replace." recap (pattern 26) → cut; end on the Blanco et al. comparison.

**16.5**
- l.3 → "The donor is more than a silicon atom with a smaller gap, because …" negation framing → "Compared to the host, the donor has sharp bound lines and a ground state built from six valleys."
- l.37 → "The bracket equals a direct sum over the partial waves of the Coulomb continuum to 10⁻⁵" numerical assurance (pattern 19) → cut; keep the q → 0 check.
- lim:16.5a → "W = ε₂^D/|ε_host|²" new symbol for L^D of eq:16.5-abs (W is also the weight of eq:16.4-borrow) → write L^D.
- l.112 → "when the detector can count it …, when the deposit could have made nothing else, and when the donors are dilute. The second condition is kinematic." then "The first condition …", then "the third" → reorder the sentence to kinematic, readout, density, and discuss in that order.
- l.104 → "as quoted by Du et al." on a textbook density (n_c ≈ 3×10¹⁸) is acceptable; no change.

**16.6**
- l.3 → "Both final states persist long after the event, both sit in a crystal that is transparent …, and both can in principle be counted one at a time." anaphoric triad plus hedge (patterns 3, 4) → "Both final states persist, both sit in a crystal transparent to the light that reads them, and both can be counted singly."
- l.7 → "A center is not a prompt final state." negation opener (pattern 25) → "A color center forms after the prompt window of \cref{sec:8.7}."
- l.32 → "The material quantities of \cref{eq:16.6-yield} are computed in three different ways." count frame → "The threshold surface and p_FP come from recoil molecular dynamics …" (start with the content).
- l.110 → p_esc appears in the lim:16.6a closing sentence before its definition at l.115 → drop it there or define it in the box.
- l.123 → NV-center paragraph sits under "Measured yields and single-center readout" and is about a target, not a yield → move to 16.6.1 after the electronic route, or cut to its last sentence.
- l.125 → "Four yields are open at millikelvin temperatures, and each is a property of the final state that no response function contains." restates l.14 ("None of them enters the response; they are properties of the final state") and l.115; first five sentences re-list the definitions (pattern 26) → keep only the three proposed measurements: "Each can be measured directly. Neutrons scattered at a tagged angle …".

**16.7** (long sentences in §4)
- l.3 → "A crystal has no excitations at these energies besides its long acoustic phonons." negation-stacked (pattern 25) → "At these energies a crystal has only its long acoustic phonons."
- l.3 → 260-word opener with two outline sentences ("We will derive …", "For the disordered solid we derive …") → one.
- eq:16.7-tand → "tan δ = ε₂/ε₁ … tan δ₀ = πP̄p²/3ε_r" two symbols for one quantity (C5).
- l.58 → "Müller et al. print the acoustic form of their Eq. (20) with an extra factor ½, although …" misprint aside (pattern 19) → cut, or a footnote-length clause.
- l.96 → "Three points of the derivation deserve a remark." count-teaser, no content → "Note that the factor tanh(m_φ/2T) appears once."
- l.98 → "The absorption is the dielectric loss of the glass, read at the dark-photon mass, which is its whole content: …" restates the key result (pattern 26) → open with "What the two-level systems add is a loss that is flat in frequency, …".
- WE 16-tls-dp l.101 → "the static permittivity of amorphous SiO₂, ε_r = 3.9" stated as fact; 16.9 l.11 and Table 16.1 call it assumed (editor note: no open source) → "an assumed ε_r = 3.9".
- l.121 → computational passage on the tunneling parameters sits at the end of 16.7.2; STYLE wants it where the quantity first appears → move to the end of 16.7.1.
- l.144 → "The transfer must be static" bare "transfer" (REGISTER term 6) → "The momentum transfer must be static".
- l.180–193 → symbol clashes: ω_IR (Ioffe–Regel) next to C^IR (infrared); α for the absorption coefficient (α is the fine-structure constant in the same chapter); "α = Cg in their units" reuses C (tunneling strength); A, B beside A^IR, B^IR. → Give the Ioffe–Regel frequency a subscript that is not "IR" (e.g. ω_{IoR}), write α_abs for the absorption coefficient, and drop "in their units".
- l.193 → "A = 4000 cm⁻² and B = 0.3 with frequencies in cm⁻¹" — B's units are not given and "in their units" sends the reader to the source (pattern 20; editor note "Taraskin B units") → state the units of A, B and α_abs explicitly.
- l.220 → "the MICROSCOPE test masses" undefined acronym → "the test masses of the MICROSCOPE satellite test of the equivalence principle".
- l.250 → first four sentences restate l.58, l.107 and l.144 (which combination fixes which rate) → compress to one sentence: "The loss tangent fixes P̄p², the acoustic loss P̄γ², and neither fixes P̄; the core term, the relaxation corrections and the kinetics of 16.8 need all three."

**16.8**
- l.3 → three orienting sentences, ending "the spin–boson language of \cref{app:C.20} carries all four results" (unanchored count) → one sentence naming phonon and electron relaxation, the ohmic scaling limit, hopping and heat release.
- l.7 → eigenbasis rotation re-derived (C7a); l.14 convention re-stated (C7b).
- l.76 → "his Laplace-transformed correlation function of σ_z, Eqs. (8) and (9) of his paper" prose equation reference → \cite[Eqs.~(8), (9)]{qureshi1995dynamics}.
- l.114 → "the periodic imaginary-time path of period 1/T that Lawrence calls the instanton" presents a term of art as one author's coinage → "…, the instanton, whose action …".
- l.118 → "The crossover also fixes which defects of a glass contribute to its heat release." The paragraph is about activated freezing at T_frz, not T_× → "Activation also fixes …".
- l.179 → 60-word opening sentence; "its distribution approaches s^{-3/2}" with s undefined (s is the Dirac invariant in 16.1, 16.3) → split after "1/r³"; "the distribution of cascade sizes N_casc approaches N_casc^{-3/2}".

**16.9**
- l.3 → "sort the targets into those whose rates are limited by theory and those limited by data" vs three classes in 16.9.2 (theory, calculation, data) → "into those limited by theory, by a calculation and by data".
- l.7 → "The inputs of \cref{tab:16-inputs} are of three kinds, and they enter an analysis differently." count frame → "Some inputs are measured constants that vary between samples: …".
- l.38 → "Three targets of the chapter are of this kind." count-teaser → name them in the sentence.
- l.44 → whole paragraph recaps 16.1, 16.2, 16.3, 16.5 (C7c) → cut; the Summary carries it.
- WE 16-band l.58 → "Its central tensor" ("its" = the reach) → "The central tensor".
- l.73 → restates l.9 ("estimate … not a bound"), l.44 ("three orders of magnitude") and four table rows (pattern 26) → cut to its one new fact: "Above 100 keV, where the pair edge carries less than a fifth of the rate, the tensor band is the largest sized uncertainty of the reach."

**Summary, D.41, D.42**
- Summary: C9.
- D-41 l.3, D-42 l.3 → "This appendix derives …" (pattern 22) → D.41: keep the concrete first sentence and cut the second; D.42: "For the coupling ½σ_zX, \cref{eq:16.8-golden} needs only J_s(ω); we derive it for …".
- D-42 l.69 → "The numerical integral agrees with the closed form to 7×10⁻⁴ … and to 2 % at …" → keep the second clause (it states where the expansion fails), cut the first.

## 4. The 22 long-sentence warnings of 16.7

Six are lint artifacts (a display or box joins two sentences): l.88–91 (key result), l.125, l.130, l.173, the lim:16.7d "Gray" line, the lim:16.7c "Dotted" line. The 16 genuine ones, with splits:
1. l.13 (46) → end at "Δ₀ = ω_w e^{-λ_tun}, with ω_w of the order of the vibration energy in one well." New sentence: "For a particle of mass M_tun crossing a barrier V_b between wells d_tun apart, λ_tun = …".
2. fig:16-tls (a) (56) → end after "(blue)"; "Weighted by the squared transition amplitude u² (red), it integrates to one, \cref{eq:16.7-norm}; \SI{87}{\percent} of that comes from u > 0.5."
3. fig:16-tls (b) (≈45) → end after "values"; "Red: the scattering structure factor …; blue dashed: the net absorption …".
4. l.40 (50) → "The atoms move between configurations with different elastic and electric dipoles. To first order the asymmetry becomes …, with S …".
5. l.121 (51) → split at the semicolon (and move, §3).
6. l.137 (53) → "For the host term take the defect as an elastic dipole. In configuration R it exerts a force dipole that differs from that of L by −2γ_TLS along its deformation, since …".
7. l.250 (53) → split before "and for the films of real detectors".
8. l.161 (57) → "The heavy-mediator weight has its median at q = 1.73 keV, where qd = 0.88 for d = 1 Å. The host and core terms cross lower, at q_× = 0.71 keV. Most of the rate therefore comes from momentum transfers outside the window of \cref{eq:16.7-host}, near the scale at which the glass stops being a continuum."
9. l.167 (≈45 before the display) → "Take one configuration of the glass in the harmonic approximation, with modes ν …, masses M_I and Born charges Z*_I. Its dielectric function has the rank-one form of \cref{sec:11.8}, with the Hessian in place of the dynamical matrix,".
10. l.186 (47) → split at the semicolon.
11. fig:16-limit-ir (53) → end after "(blue, dashed)"; "Inputs: the terahertz fit …".
12. l.210 (48) → "… a de Broglie wavelength of about 60 μm. A momentum transfer of order m_χv cannot resolve atoms, and the particle scatters off the smoothed nucleon density of a whole body."
13. l.222 (≈45 before the display) → "…, the medium acts on the particle as an optical potential. It is the sum of the pseudopotentials 2πb/μ of the nucleons, with b the scattering length, σ = 4πb², and μ ≈ m_χ:".
14. l.233 (47) → "The homogeneous term … contains the scattering of the wave by the surface of the body. For a planar face its first-order form can be compared with exact reflection off a potential step."
15. fig:16-limit-born (49) → end after "(blue) medium"; "E_n is …".
16. l.246 (64) → "… and on the composition difference of the two masses. \Cref{app:E.19} specifies the transfer-matrix calculation; until it is done, a bound from this channel is a conjecture."

## 5. Pattern 25 sweep (chapter opening, section and subsection openers, captions)

Read sentence by sentence; lint PERIPHRASIS: 0. Hits: s16-7 l.3 "no excitations … besides" (fixed above); s16-5 l.3 "more than a silicon atom with a smaller gap"; s16-6 l.7 "A center is not a prompt final state" and summary l.13 (same); s16-4 l.28 "The environment is not a small effect"; fig:16-demon-limit "to mean much". Clean: all other openers (16.1 ZrTe₅ numbers, 16.2 nanotube line, 16.3 work function, 16.4 anthracene, 16.6 F center, 16.8 46 pW, 16.9 tensor spread) open on a concrete number; no figurative stand-ins ("pull", "silence", "whisper", "heart of") anywhere. "window" (kinematic, energy) is technical and stays.

## 6. Pattern 26 sweep (paragraph fact lists; paragraphs that add nothing new)

Each paragraph was listed against its predecessors. Paragraphs whose list is empty or a subset: s16-4 l.112 last sentence; s16-6 l.125 sentences 1–5; s16-7 l.98 sentence 1; s16-7 l.250 sentences 1–4; s16-9 l.44 (whole); s16-9 l.73 (all but one clause); s16-8 l.7 sentences 3–4 (subset of 16.7); s16-1 l.33 sentences 6–7 (subset of D.41). Ends of subsections: 16.1.2 ends on the design rule (new); 16.2.2 on the cascade pointer (new); 16.3.1 on the consistent final state (new); 16.4.3 on the E.21 calculation (repeat, see §3); 16.5.3 on the open problem (new); 16.7.1 on saturation (new); 16.8.5 on the specific-heat comparison (new). No recap closes a subsection except 16.4.3, 16.4.5 and 16.9.

## 7. Register calibration (2–3 passages per section; one rewrite where the answer is no)

- 16.1: l.33 "The powers differ because the numerators differ." yes. l.64 source bookkeeping, no → "Note that the reference tabulates the full gap, 31.2 meV; the half-gap, 15.6 meV, is what enters \cref{eq:7.3-H}."
- 16.2: l.74 "The interaction is strong." yes. l.12 packing sentence yes. l.121 no → "Their rate is just \cref{eq:4.4-SL} inserted in \cref{eq:8.2-spectrum}."
- 16.3: l.3 opener yes. l.12 "Ejection probes the short-distance structure of the orbitals, as atomic ionization does" yes. l.76 no → cut (§3).
- 16.4: l.42 "The phases have dropped out." yes. l.44 no → rewrite in §3. l.112 dangling comparison no → §3.
- 16.5: l.114 "while ionization needs a single-electron counter, which exists" yes. l.3 no → "Compared to the host, the donor has sharp bound lines and a ground state built from six valleys."
- 16.6: l.115 "A broken bond is not yet a signal." yes. l.28 "The Doppler width is the first correction, and it is small." yes. l.125 no → "Each of these yields can be measured directly:".
- 16.7: l.161 "This number is an estimate, uncertain by about a factor 3." yes. l.107 "The target mass is the problem." yes. l.96 no → "Note that the factor tanh(m_φ/2T) appears once."
- 16.8: l.46 "A superconducting film … leaves its two-level systems coupled to phonons alone, as an insulator would." yes. l.114 no → "…, along the instanton, the periodic path in imaginary time, whose action replaces V_b/T."
- 16.9: l.44 "These are errors of a formula, not uncertainties of an input." yes. l.7 no → "Some inputs are measured and vary from sample to sample: …".

## 8. Cuts (budget and redundancy)

- **16.4 (−420 needed):** l.3 outline (−40); l.28 singlet repeat + E.21 clause (−60); l.56 √2/sign clause shortened (−25); l.62 overlap-density details to the lim:16.4a caption or E.21 (−90); l.85 compress, drop E.21 sentence (−100); l.97 last two sentences merged with l.85's (−60); l.112 last sentence (−40). ≈ −415.
- **16.6 (−300 suggested):** l.125 sentences 1–5 (−120); l.123 NV paragraph to its last sentence (−80); l.32 compress (−40); l.26 "The source states the limits of its formula itself …" (−30); WE l.62 last sentence (−25).
- **16.7 (−250, plus the 16 splits):** l.3 outline (−70); l.58 misprint aside (−35); l.96 (−40); l.98 sentence 1 (−35); l.250 sentences 1–4 to one (−60).
- **Elsewhere:** 16.1 l.33 to D.41 (−120); 16.8 l.7, l.14 (−90); 16.9 l.44, l.73 (−230); ch16.tex catalogue (−80). Chapter total ≈ −1,500.

## 9. Editor-notes items that concern prose

- 16.1 ε_r → ε_pub: done (s16-1 l.23 "written ε_r there"). Map rerun: open (C2).
- 16.2/16.3/16.9 graphene v_D: open (C5); the Table 16.1 clause stays until unified.
- 16.3 add lim:16.3a,b to the map caption: open (C2). App. C.8 lacks I₀, K₀: open; s16-2 l.39 points there.
- 16.4 Mataga–Nishimoto and U uncited: open (§3). Over budget: §8. "Probably overstated" label: present (l.85).
- 16.5 model labels (line strengths, n_c via Du et al.): present.
- 16.6 E_d = 27 eV and phonon bracket labelled as model values: present (l.28, l.38, fig:16-lif). "Cage effect": now described in words (l.115); acceptable without a citation.
- 16.7 22 long sentences: §4. ε_r = 3.9 label: inconsistent (§3, WE). Taraskin B units: open (§3).
- 16.8 τ₁⁻¹ vs Γ₁: open (C5). "For Δ_tl ≪ T" when quoting the bare factor: done in summary l.17 and tab:16-nuisances (summary l.61); 16.9 does not quote it.
