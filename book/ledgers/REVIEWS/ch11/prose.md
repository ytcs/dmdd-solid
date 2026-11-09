# Ch11 prose review (style, register, standalone)

Scope: tex/ch11/ch11.tex, s11-1 … s11-9, appD/D-31, D-32, read in full against STYLE.md, style-guide.md, prose-review.md and REGISTER.md. The editor-notes items that concern prose are in Sect. F. Line numbers are per file. No tex was edited. The chapter runs to about 37,000 words (sections 3,400–4,500 each, D.31 1,600, D.32 1,000).

## Verdicts

| Section | Verdict | Main reasons |
|---|---|---|
| Opening (ch11.tex) | REVISE | paragraph 2 is a five-sentence outline that leaves out 11.8 and 11.9; "Below about 10 MeV" needs a qualifier |
| 11.1 | REVISE | literature-normalization bookkeeping; self-narration; a 380-word paragraph; Debye-temperature digression; "largest transfers" |
| 11.2 | PASS | minor: "modelling"; count-teaser; 26 %/37 % stated twice; "easy to read off"; abstract opener at l.36 |
| 11.3 | PASS | minor: literature bookkeeping at l.28 and l.43; "ten percent"; Warren cited without equation; title "The coherent remainder" |
| 11.4 | REVISE | three count-teasers; "minimum speed"; "in this book"; N_T undefined in the limit box; bookkeeping at l.37 and l.109 |
| 11.5 | REVISE | upright Γ for a rate; "so" at 4× the model's rate; outline sentence in the opener; "The second consequence" with no first |
| 11.6 | REVISE | forward pointer to 11.8 for a cancellation that 11.6 derives itself; "Before we compare"; process aside in a caption |
| 11.7 | REVISE | limit box in the source's notation; "we call"; Y^c_ℓ used before it is defined; "only" at 5× the model's rate; 400-word paragraph |
| 11.8 | REVISE | "modelling" ×3 and "(modelling choice)" tags; core-kinetic estimate not labelled (editor); "Neither this section nor the literature" |
| 11.9 | REVISE | restating paragraph (l.62); self-narration (l.3, l.31); 𝓡^𝔗 undefined; process phrases |
| Summary | PASS | minor: "ten percent" against \SI; "about 7 keV" against the 6.6 keV of 11.3 and 11.9 |
| App. D.31 | PASS | "of order" 11 times in 1,600 words; `\end{equation*} Collecting` run-on (l.87) |
| App. D.32 | PASS | `\end{equation*} The translation` run-on (l.10) |

No section needs a REWRITE. The voice is consistent across the nine writers. All of them use "we", open on a number or a concrete question, give the estimate before the result, write no exercises and no "you", and use no exclamation marks. Every equation is part of a sentence. The problems that run through the whole chapter come from shared habits, and one sweep fixes them:
- (i) Each section opener ends with a "We will derive …" roadmap of three to five sentences, and each section ends with a recap and a pointer.
- (ii) Agreement with the literature is shown by normalization bookkeeping ("whose normalization per cell is Ω/2π times ours …").
- (iii) The register connectives are off the model's rates (Sect. C).
- (iv) Count-teasers.
- (v) Process tags such as "(modelling choice)".

## A. Lint

| File | Hits | Assessment |
|---|---|---|
| ch11.tex, D-31, D-32 | 0 | — |
| s11-1 | EQ-PUNCT l.24; LONG-SENT ×7 | EQ-PUNCT false (the comma comes before `\end{aligned}`). Real long prose sentences: l.59 (Campbell-Deem et al.), l.97 ("It lies above … a factor of about 21"), l.202 (Hill average). The rest are captions. |
| s11-2 | EQ-PUNCT l.104; LONG-SENT ×1 | false; caption |
| s11-3 | EQ-PUNCT l.19, l.113; LONG-SENT ×6 | false; l.38 ("What is left is the self part …") is the only real run |
| s11-4 | LONG-SENT ×2 | captions |
| s11-5 | EQ-PUNCT l.9; LONG-SENT ×12 | false; real: l.82 ("Near the peak the band is wide: …"), l.139 ("And at the lowest pressures …") |
| s11-6 | EQ-PUNCT l.37, l.138; LONG-SENT ×6 | false; real: l.121 ("Light enough, the vector …"), l.136, l.149 |
| s11-7 | LONG-SENT ×7 | l.26 (addition theorem) and l.73 are real; the rest are the l.93 caption |
| s11-8 | LONG-SENT ×4 | l.18–22 and l.128 are real; the rest are captions |
| s11-9 | EQ-PUNCT l.74; LONG-SENT ×4 | false (the line ends with "."); table rows and the table caption |

All eight EQ-PUNCT hits are false positives of the linter on `aligned`/`gathered`. Equation punctuation passes throughout.

## B. Chapter as a whole

**Opening (ch11.tex).**
- l.2 is the motivational opening STYLE asks for. It is concrete (10 MeV, 50 keV, 50 meV, "fifty times smaller") and ends on a question.
- l.4 is an outline: "The harmonic crystal … supply the response …; What the chapter adds is …; Beyond the harmonic picture lie …; A crystal also has directions …". That is five sentences, where STYLE allows one orienting sentence. "What the chapter adds is" is self-narration (pattern 22), and the list still leaves out absorption (11.8) and the nuisance budget (11.9).
  - Fix: keep the sentence on what Chap. 5 and Chap. 8 supply. Replace the rest with one sentence: "Each regime reduces to a few material numbers, sound speeds, Born charges and Debye–Waller exponents, each checked against the fuller result; throughout, the electrons stay in their ground state, and the Migdal effect and phonon-assisted electron recoil follow in Chaps. 12 and 13."
- l.2 "Below about \SI{10}{MeV}, … cannot give a silicon nucleus enough energy to treat it as free." Sect. 11.4 puts the impulse regime from 17.5 MeV (x_R = 4) or 26 MeV (x_R = 9), and 11.3 gives a multiphonon window of 0.4–26 MeV. The two do not contradict each other, but the reader will compare them. Fix: "Below about 10 MeV, where the free recoil energy reaches the phonon energies, …".

**Summary (s11-9 l.98–116).** It has one paragraph per section and ends on a pointer to Chap. 12, which is correct. `\section*{Summary}` matches Chap. 10. Fixes:
- "within ten percent from about \SI{7}{keV}" (l.104): 11.3 and 11.9 give 6.6 keV. Use "from about 6.6 keV", or round it the same way everywhere.
- "ten percent" (l.104, l.106) and "six percent" (l.112) against `\SI{10}{\percent}` elsewhere. STYLE puts numerals with units, so use \SI throughout (the same applies in s11-3 l.3 and l.122, s11-5 l.3, s11-7 l.3 and l.59, s11-9 l.96).
- l.116 restates the 26 %/37 % semilocal ε∞ point for the fourth time (see the redundancy list below). Keep it here, and cut it elsewhere.

**Redundancy across sections.**
- The coupling-to-mass cancellation is derived in full twice, at s11-6 l.13 and s11-8 l.43. Keep the derivation at its first appearance (11.6), and at s11-8 l.43 write "the coupling-to-mass cancellation of Sect. 11.6". s11-6 l.13 and l.132 now point forward to `sec:11.8-single` for a result they derive themselves.
- "semilocal ε∞ 26 % high, rate 37 % low" appears at s11-2 l.38, s11-2 l.166, s11-9 l.23, the Summary l.116 and the s11-9 table. Keep s11-2 l.38 and the table row, and cut s11-2 l.166's last sentence ("is not an option at this precision").
- 11.9 says every nuisance three times: in prose (l.7–27), in the table (l.32–60), and again in l.62 ("For a nucleon coupling in silicon the table holds no item above a few percent …"). The Summary then says it a fourth time. l.62 is a restating paragraph (pattern 5): cut it, and move its one new clause ("errors of a simpler one, by up to a factor of 16 and 8.2") into l.17.
- 11.1 l.202–210 (the elastic Debye temperature) states that it is "not an input to the rates above". It belongs to Sect. 5.2. Cut it to two sentences with a pointer, or move it there.
- s11-4 l.111 and the caption and box text of `lim:11.4b` give the same 61 keV/16× numbers. Keep them in the text, and let the box keep only its single breakdown sentence.

**Seams (each adjacent pair read across the join).**
- 11.1→11.2: l.212 uses "A coupling to charge" twice in a row ("A coupling to charge and momentum transfers beyond the zone lie outside it. A coupling to charge, the dark photon, …"). Delete the first sentence. 11.2 then opens cleanly on GaAs.
- 11.2→11.3: passes. The end of 11.2 (several phonons at the zone scale) leads into the q window of 11.3.
- 11.3→11.4: passes. l.152 names 11.4 and 11.5. One pointer is enough, so drop "Sect. 11.5 asks …", which 11.4 l.128 repeats.
- 11.4→11.5: passes ("Sect. 11.5 turns to them" → η_anh = 0.049).
- 11.5→11.6: passes ("their spin and their mass number").
- 11.6→11.7: 11.6 ends on the missing cold measurement and 11.7 opens at 45°N with no bridge. Ending on an open problem is allowed (REGISTER 3.7), and the 11.7 opener stands alone.
- 11.7→11.8 and 11.8→11.9: pass.
- 11.6 opens by citing 11.8 forward (l.3, "The couplings of Sects. 11.1, 11.2, 11.8 never noticed"). Drop 11.8 from that list; it is also anthropomorphic (pattern 15). Write "The couplings of Sects. 11.1 and 11.2 are the same on every site of a sublattice".

## C. Register (REGISTER.md Sect. 4 and checklist)

Counts per 10k words, chapter (L = Lin, the model):

| | ch11 | L | Worst section |
|---|---|---|---|
| however | 1.4 | 8.0 | 0 in s11-1, 4, 5, 6, 7, 9 |
| typical/typically | 0 | 15.3 | everywhere |
| note that | 0 | 6.1 | everywhere |
| we can / we see | 0 | 13.6 / 2.7 | everywhere |
| only | 30 | 11 | s11-7 52, s11-6 38, s11-5 33 |
| gives | 27 | 7 | s11-9 39, s11-4 38, s11-6 36, D-32 90 |
| so | 22 | 11 | s11-5 44, s11-7 27, s11-1 25 |
| of order | 6 | 0 | D-31 69, s11-5 14 |

Thereby, whereby, respectively, in order to, i.e./e.g., one finds and Let's are all absent. Fixes: in each section, convert three to five "so"/"gives" to "since …"/"leads to"/"is", and add "however" where there is a real contrast (s11-1 l.155, "It never exceeds 94 %"; s11-4 l.80, "From x_R = 14 upward …"). Hedge running estimates with "typical" or "∼" where the text says "of order" (s11-5 l.48; D-31 l.46–51).

Terms of art:
- s11-1 l.155 "the largest transfers" → "the largest momentum transfers".
- s11-4 l.68 "the minimum speed" → "the minimum velocity".
- s11-7 l.26 "which we call the halo multipoles" (R2/R5) → "the multipoles of the halo, $\varUpsilon_\ell$".

Spelling: "modelling" at s11-2 l.47, s11-8 l.71, l.108, l.209 and s11-9 l.25 → "modeling" (American spelling).

Γ typography:
- s11-5 l.124 "$\Gamma = (\pi\bar\sigma_n/…)$" is a rate, so it takes `\varGamma`.
- The zone center is written `$\Gamma$` in s11-1 (l.44, l.164) and `$\mathrm{\Gamma}$` in s11-3 (l.106, l.122) and s11-9 (l.13). Pick one form.

## D. Section-by-section issues (location → problem → fix)

Calibration: two or three passages per section, with one sentence rewritten as Lin would write it.
### 11.1 Acoustic phonons — REVISE
Calibration:
- l.3 opener (0.53 keV → 5.4 μeV → 16 meV): Lin could write it. Yes.
- l.155 ("soft crystals win"): yes.
- l.166 "The elastic constants are themselves a computed or measured material quantity.": no. Rewrite: "In practice the elastic constants are either measured or computed by DFT, from finite strains or strain perturbation theory; reading them off the slopes of interpolated acoustic branches is much less reliable (App. E.4)."

Issues:
- l.33 "whose structure factor is normalized per cell and is Ω/2π times …; their one-phonon structure factor drops G and the Debye–Waller factors" → normalization bookkeeping (pattern 19) → keep "At T = 0 this is the amplitude of Campbell-Deem et al. [Eq. (7)]" and put the convention in one clause or drop it.
- l.59–63 two sentences that reconcile two papers' normalizations and m_p against m_u, plus "The step function is their cutoff …; it is not part of the long-wavelength limit" → pattern 19 → keep one sentence: "Campbell-Deem et al. derived the longitudinal case and noted that the composition drops out [cites]; they apply it up to q = 2π/a, which the box tests."
- l.76 "The box answers how far the long-wavelength form can be trusted." → self-narration (pattern 22) → delete; begin with "The departure is driven by the dispersion: …".
- l.99 "The two mediators behave in opposite ways, and the next two subsections explain each." → pattern 22 → "For a light mediator the curves merge at high mass; for a heavy one they plateau at levels set by the sound speed."
- l.119 the conversion of Griffin's σ̄_n ("changes the normalization by (mχv0/q0)^4 but not the conclusion") → pattern 19 → cut it; App. A.9 carries it.
- l.155 "The plateau holds between two limits." → count-teaser (pattern 18) → "The plateau is reached only well above the edge and ends near 0.42 MeV." The paragraph runs about 380 words and does five jobs (scaling, comparison with Griffin, approach to the plateau, the zone cut, Sect. 17.5). Split it after "between 0.1 and 1 MeV".
- l.166 "Tabulated tensors carry one pitfall that has nothing to do with physics" → count-teaser and filler → "Some codes and databases store the shear rows of the Voigt matrix in the order xy, yz, zx …".
- l.35 "the factor is one for every purpose" → vague → "the factor is one to 3×10⁻³".
- l.183 limitbox: "computed here from the Christoffel problem of the Voigt-ordered elastic tensor" → process ("here") → "from the Christoffel problem of the elastic tensor in Voigt order".
- l.212 duplicate "A coupling to charge" → see seams.
- l.11 "the electrons enter by carrying the nuclei's forces" → unclear → "the electrons enter only through the forces they transmit between nuclei".
### 11.2 Optical phonons in polar crystals — PASS
Calibration:
- l.69 "All powers of q cancel but one. A light mediator weights every logarithmic interval …": yes.
- l.153 the plasmon analogy: yes.
- l.36 "The same result can be reached with another bookkeeping.": no. Rewrite: "Trickle and collaborators reach the same result with the ions in the vertex: they couple to q·Z*_κ and screen with ε∞ alone [Eq. (105)]."

Issues:
- l.40 "rests on three conditions" … "Of the three, the first is the one that matters" → count-teaser and ordinal reference (patterns 18, 13) → name it: "The small-q vertex is the condition that matters in practice".
- l.47 "(modelling choice)" → pattern 19 and spelling → "Born charges held at their zone-center value".
- l.166 last sentence repeats l.38 → cut.
- l.192 "The factors are easy to read off" → close to the banned "it is easy to see" → "The factors are:".
- l.199 "built into the physics, not an accident of two materials" → false contrast (pattern 6) → "The reversal is general."
### 11.3 Multiphonon response — PASS
Calibration:
- l.66 "When does the incoherent approximation hold?": yes.
- l.146 "In a dark-matter detector this term is negligible.": yes.
- l.122 "It bounds the error, but the pointwise accuracy … has to come from Eq. (11.3-Sn) itself.": nearly. Rewrite: "So the band bounds the error, but it is too loose to vouch for the incoherent spectrum point by point below a few q_BZ; for that we need Eq. (11.3-Sn) itself."

Issues:
- l.28 "whose normalization per cell is Ω/2π times ours and whose factor s²₁,₂ … plays the role of 1/n!" → pattern 19 → keep "is the contact term of Campbell-Deem et al. [Eq. (12)]".
- l.43 "with their f̄_d, m_d, D_d(ω) and Ω_c for our c_κ, M_κ, g/3 and Ω" → a symbol dictionary for a source; acceptable in one clause, but drop "Their result at T = 0 … is Eq." and fold it into the previous sentence.
- l.66 "The next subsection computes it, and the box shows the result for silicon." → pattern 22 → delete.
- l.3 and l.122 "ten percent" → `\SI{10}{\percent}`.
- l.133 and l.136: `\cite{warren1969xray}` with no equation or section (STYLE asks for one). The editor accepted citing it at book level, so this is minor.
- Title l.90 "The coherent remainder" gestures (pattern 21) → "Exact phonon-order weights".
### 11.4 Impulse limit and free nuclear recoil — REVISE
Calibration:
- l.25 "The term q·p/M is a Doppler shift: a nucleus moving toward the kick absorbs more energy": yes.
- l.39 "as much as a classical gas at 237 K would": yes.
- l.93 "Germanium has no first-principles density of states in this book (Table 5.x).": no. Rewrite: "For germanium a rough ⟨ω⟩ is enough, and its Debye temperature of 373 K supplies one: …".

Issues:
- l.11 "Two exact statements follow" → count-teaser → "Its mean and variance follow exactly (App. D.32):".
- l.93 "A single number needs a criterion, and two are in use." → count-teaser → "The onset depends on the criterion."
- l.95 "three effects lie outside it" → count-teaser → name them: "It leaves out anharmonicity, electronic excitation and atom displacement."
- l.37 "with their Δ_d² = q²ω̄_d/2m_d for our σ_ω²" and l.109 "their ρ_χ ≃ 0.4 GeV.cm⁻³ becomes our 0.3" → pattern 19 → keep the first as one clause, and cut the second (the halo is fixed in Chap. 1).
- l.68 "minimum speed" → "minimum velocity".
- l.116 limitbox: "per $N_T$ nuclei", where N_T is undefined → "per nucleus", or define it.
- l.61 "With the estimate ⟨ω⟩ ≈ 23.6 meV made below" → forward reference inside a worked example → move the l.93 estimate before WE 11.x, or quote its source in one clause.
### 11.5 Anharmonic and quantum-crystal corrections — REVISE
Calibration:
- l.3 "For the impulse peak, by a part in a thousand. For a deposit of several phonons … by factors of several": yes.
- l.122 the helium picture ("far out on the attractive tail"): yes.
- l.22 "The second consequence is a selection rule.": no. Rewrite: "Time reversal adds a selection rule."

Issues:
- l.3 "We will find the corrections in this order: the moments …, the first correction …, a bound …, and the quantum crystal." → outline list in the opener → cut; the three preceding sentences already name the cases.
- l.22 "The second consequence" with no first stated → name both, or use the rewrite above.
- l.31 "for every practical purpose" → "to a part in a thousand" (the number is already in the sentence before).
- l.124 upright `\Gamma` for Ashour's rate → `\varGamma`.
- The "so" rate is 44/10k (l.22, 31, 48, 59, 61 …) → change half of them to "since"/"as a result".
- l.139 a 60-word sentence ("And at the lowest pressures, … neither is exact: …") → split at the colon.
### 11.6 Nuclear-spin and isotope couplings — REVISE
Calibration:
- l.65 "How does a single heavier atom vibrate in a crystal of lighter ones? Its neighbors push it with the same springs, and only its inertia differs.": yes, model register.
- l.170 "which makes enrichment a control of the signal": yes.
- l.61 "\Cref{eq:11.6-alp} contains one approximation.": no. Rewrite: "Note that the spin sits on ²⁹Si, 3.2 % heavier than the mean silicon atom, whose local density of states is not that of the host; the literature uses the host density of states for every isotope."

Issues:
- l.13 and l.132 "the coupling-to-mass cancellation of \cref{sec:11.8-single}" → forward pointer for a result derived right here → "This is the coupling-to-mass cancellation [Mitridate et al.]"; 11.8 l.43 then points back.
- l.3 "never noticed either fact" → anthropomorphic, and points forward to 11.8 → see seams.
- l.61 "Before we compare, we need the vibrations of one atom of a different mass." → pattern 22 → delete; the subsection title says it.
- l.89 "The spin-carrying isotope is the case at hand." → fails the deletion test → delete.
- l.111 caption "No many-defect calculation is done; the pair term is evaluated to first order …" → process aside → "Pair term to first order in the second defect's scattering, from the host Green function."
- l.121 a 70-word sentence ("Light enough, the vector can be the dark matter, and it is then absorbed like a dark photon: …") → split after "dark photon".
### 11.7 Anisotropy and daily modulation — REVISE
Calibration:
- l.3 "A liquid would not notice.": yes.
- l.36 "The halo therefore filters the anisotropy of a crystal": yes.
- l.112 "The cubic crystals combine both sectors of the book in one example.": no. Rewrite: "In silicon both the electron and the nucleon rates modulate, and with the same phase."

Issues:
- l.89 limitbox: it states the source formula in the source's notation (W_ℓm, 𝓡^(ℓ)_mm′(t), f̂_ℓm′), never defined, then "In the book's notation this is …" → patterns 20 and 22 → state Eq. (11.7-rate) in the box with the cites for credit, and drop the source symbols and "the book's".
- l.26 "which we call the halo multipoles" → see Sect. C.
- l.32 keyresult uses Y^c_ℓ ("one cubic harmonic") before its definition, which is pointed to only at l.121 → add "(\cref{eq:C.3-cubic})" at l.32.
- l.79 is about 400 words with six jobs: long-wavelength S₄, behavior beyond the zone, two phonons, App. E.17, the conclusion, the mass dependence → split before "A cubic crystal therefore modulates".
- "only" at 52/10k (l.47, 55, 61, 63, 79, 101, 110, 135 …) → halve.
- l.112 "both sectors of the book" → see the calibration rewrite.
### 11.8 Absorption on phonons and acoustic modes — REVISE
Calibration:
- l.79 "GaAs is the obvious target, polar and well measured, and it turns out to be close to the worst case.": yes.
- l.190 "Why should an oscillating size excite a mode at all? A static change of a excites nothing.": yes.
- l.97 "Neither this section nor the literature includes it.": no. Rewrite: "This is a parametric estimate from the virial theorem; no calculation has included it yet, and Sect. 11.9 carries it as a nuisance of about 20 % in the rate."

Issues:
- l.97 the core-kinetic term is not called a parametric estimate here, and the 20 % rate effect is stated only in 11.9 (editor item) → use the rewrite above.
- l.71, l.108, l.209 "(a modelling choice …)", "(modelling choice)", "(modelling choice, for visibility; …)" → pattern 19 and spelling → "widths set to 1 % of each frequency", "an assumed width of 1 %", "𝔔 = 100 for visibility".
- l.43 the coupling-to-mass cancellation is derived again → "As in Sect. 11.6, a coupling proportional to the mass excites no optical phonon [Eq. (44)]".
- l.67 limitbox "with the self-energy of the field built from the one-phonon propagator and site form factors [Eqs. (2), (7), (14), (16)]" → describes the source's method instead of stating a formula (pattern 20) → state Eq. (11.8-Gamma) and cite for credit.
- l.99 repeats the "Z*/ε∞ to 1 %" sensitivity of WE 11.x l.90 → cut "A rate of an electron-coupled scalar … needs Z*/ε∞ to 1 % or better".
### 11.9 Nuisance parameters of the lattice rates — REVISE
Calibration:
- l.3 "That difference is not an uncertainty.": yes.
- l.96 "The largest error a published rate can carry on the lattice side is the use of the free recoil below the impulse onset.": yes.
- l.62 "For a nucleon coupling in silicon the table holds no item above a few percent once the response is computed in full.": no. Rewrite: "The upshot is that, once the full response is computed, nothing in the table exceeds a few percent for a nucleon coupling in silicon."

Issues:
- l.3 the last two sentences ("We give the lattice sector those templates …", "The open calculations … are grouped at the end by the calculation that would close them.") → pattern 22 → keep the result ("The band is a quarter of a percent …") and cut the plan.
- l.31 "Each row gives the truncation or input, the type of its template, …" duplicates the table caption → delete.
- l.62 restating paragraph → see redundancy.
- l.69 $\mathcal{R}^{\mathfrak{T}}$ undefined in the chapter → "(the truncated rate of Eq. (8.8-…))" at first use.
- l.21 "the change on cooling is named but not sized here" → process phrasing → "the change on cooling has not been sized".
- l.25 "computed neither in Sect. 11.8 nor in the literature" → pattern 19 → "a parametric estimate from the virial theorem".
### App. D.31 — PASS
Derivation register; calibration not applied.
- l.87 `\end{equation*} Collecting` → break the line, so that the source text gets a new paragraph or a continued sentence.
- "of order" appears 11 times (l.46–59); in an appendix this is acceptable, but change two or three to "∼".
### App. D.32 — PASS
Derivation register; calibration not applied.
- l.10 `\end{equation*} The translation` → same run-on.

## E. Standalone scrub and user rules

- **No exercises or checkpoints; nothing left to the reader.** Satisfied: every step is in the text or in D.31/D.32.
- **Standalone.** No internal labels or campaign words appear in the prose. The process tags are listed above.
- **Citations attribute (pattern 20).** Violations are the 11.7 box (l.89) and the 11.8 box (l.67). The 11.7 figure (l.106 caption) uses "the published site tensors of Stratman and Lin" as its input without stating them; add the two numbers that matter (the ratio B^cc/B^aa per site) in the caption.
- **Limit boxes as self-contained comparison plots.** All 20 boxes have a formula, a credit citation, a plot with a validity band, and one breakdown sentence. Exceptions: the 11.7 and 11.8a boxes have multi-sentence, source-led statements, and the 11.4b box uses N_T, which is undefined.
- **Titles.** All are short noun phrases. Only "The coherent remainder" gestures.
- **Cross-references.** All use \cref. Two hard-coded source figures appear in captions ("Fig.~3 of Deinzer and Strauch", s11-6 l.175); a source figure cannot take \cref, so they are fine.
- **Captions stand alone.** Yes, except the 11.7 caption at l.106 (flagged above).
- **Lists, triads, hedges.** No bullets stand in for argument (the only run-in lists are worked-example items and the 11.9 nuisance display). No reflexive triads or stacked hedges were found.
- **Voice checks.** Grep for "you", contractions and "!" finds only factorials.

## F. Editor-notes items that concern prose

- **11.1** (0.48 q_BZ; 44× and 9×; the failure in WE 11.x at 3× the edge): stated in the captions (s11-1 l.70, l.138) and in the worked example. Satisfied.
- **11.8** (label the core kinetic-term shift as a parametric estimate and move it to the 11.9 nuisance table): it is labelled and tabled in 11.9 (l.25, l.53), but not labelled in 11.8 (l.97). Not yet satisfied; see 11.8.
- **11.8 l.97–99, "possible near-duplicate"**: these are not duplicates. l.97 covers the core, mass and frequency terms; l.99 covers the DFPT inputs and PBE ×250. Do not merge. Trim l.99's repeat of the 1 % sensitivity.
- **11.3** (the band is not a 10 % certificate): stated at l.122. Satisfied.
- **11.4** (the Ge ⟨ω⟩ is a labelled estimate): l.93 ("An estimate follows …"). Satisfied. The forward use at l.61 is the only issue.
- **11.6** (the absorption value was read off a figure, about 10 %, and the text must say so; 11.9 quotes it): stated at l.163 and l.167, in the caption at l.175, and in 11.9 l.27. Satisfied.
- **11.7** (odd multipoles need BOTH symmetries broken; EPM labelled; sapphire and SiC are estimates): stated at l.49, l.63 and l.110. Satisfied.
- **11.5** (the three-phonon coefficient is fitted; the boxes are labelled models; helium "about a quarter"): stated at l.31, l.68, l.133 and l.122. Satisfied.
- **WE 11.10** (writer's choice of threshold and σ_p; the upper frequency template): stated at s11-9 l.13 ("an upper template"). Satisfied.
- **Other items.** These are already in the text: n_T = 2 (s11-3 l.133), n_A = 2 (s11-5 l.76) and 8.0 % (s11-6 l.161). Lifshitz, Dawber–Elliott and Warren are cited without equation numbers; that is credit only, which is acceptable. The overfull boxes are a build item, not a prose one.
