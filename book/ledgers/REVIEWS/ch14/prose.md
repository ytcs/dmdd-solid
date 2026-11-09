# Ch. 14 prose review (style and prose, isolated)

Scope: tex/ch14/ch14.tex, s14-1 … s14-6, tex/appD/D-38.tex. Checked against STYLE.md, style-guide.md, prose-review.md (patterns 0–26), REGISTER.md and editor-notes.md. No tex was edited.

## Verdicts

| Section | Verdict | Main reasons |
|---|---|---|
| Chapter opening + map (ch14.tex) | REVISE (minor) | two orienting sentences where one is allowed; 14.5 is missing from the opening |
| 14.1 Magnon scattering | REVISE (minor) | restatement at the end of 14.1.4; duplicate subsection titles; mixed "percent" style |
| 14.2 Two-magnon continua … | REVISE | repeats 14.1 (ΔS, four sc lattices, 0.073/0.078, one-magnon edge); 14.2.5 mostly restates; wrong cref in the opener |
| 14.3 Absorption into magnons | REVISE | golden-rule condition contradicts 14.6; Γ_M assumption not flagged as assumed; reviewer-facing reconciliation; Ω/ω_M clashes |
| 14.4 Spin responses from neutron data | REVISE | looped restatement at the ends of 14.4.2 and 14.4.3; `g` used for a group element; figurative openers |
| 14.5 Chiral and nonreciprocal targets | REVISE | "Open problems" restates; ω_M/η_M clashes; "hexaferrite"; negation framings |
| 14.6 Coherent fields … | REVISE (cuts) | over budget (≈6,100 vs 4,500); the opener contradicts the 207Pb worked example; the Budker reconciliation is a process artifact; recap paragraph after the table |
| App. D.38 | PASS (minor) | third copy of ΔS = 0.078 and the four sc lattices; self-narrating first paragraph |

## 1. Lint (lint.py --banned BANNED-TERMS.txt)

| File | Hits | Blocking | Notes |
|---|---|---|---|
| s14-1 | 4 (1 EQ-PUNCT, 3 LONG-SENT) | 0 | EQ-PUNCT l.63 is a false positive (the gathered display ends in "," before "with"). The LONG-SENT hits span keyresult/figure environments, so they are parser artifacts. |
| s14-2 | 0 | 0 | clean |
| s14-3 | 5 LONG-SENT | 0 | four are environment artifacts (keyresult, figure, limitbox); the real one is l.58 ("With 𝔰_net … :" runs into the box) |
| s14-4 | 2 LONG-SENT | 0 | box/caption artifacts |
| s14-5 | 2 EQ-PUNCT, 6 LONG-SENT | 0 | EQ-PUNCT l.8, l.128 false positives. Real long sentences: l.7 (three "and" clauses), l.166 (last sentence, about 45 words) |
| s14-6 | 1 EQ-PUNCT, 11 LONG-SENT | 0 | EQ-PUNCT l.78 false positive; 5 hits are table rows. Real long sentences: l.11–12, l.30, l.35, l.90 |
| D-38 | 2 EQ-PUNCT | 0 | both false positives (comma before \end{aligned}/\end{gathered}) |

Banned terms: none. Bare "Limit N.M" or "limit box" in prose: none (all \cref). Exercises, "the reader", "you": none. Internal labels (SPINE, WP, DC-, F row): none.

## 2. Register (REGISTER.md §4), per 10k prose words (math stripped; approximate)

| | so (L 11) | only (L 11) | gives (L 7) | therefore (L 3) | of order (L 0) | however (L 8) | we will/can/see (L ≈29) | typical(ly) (L 15) | median sentence length |
|---|---|---|---|---|---|---|---|---|---|
| 14.1 | 34 | 30 | 20 | 10 | 0 | 3.4 | 0 | 0 | 23 |
| 14.2 | 46 | 43 | 14 | 16 | 13.5 | 2.7 | 2.7 | 0 | 23 |
| 14.3 | **55** | 26 | 32 | 15 | 8.7 | 2.9 | 0 | 0 | 25 |
| 14.4 | 31 | **61** | 19 | 12 | 0 | 0 | 3.8 | 0 | 21 |
| 14.5 | 37 | 37 | **42** | 10 | 7.3 | 2.4 | 0 | 0 | 23 |
| 14.6 | 17 | 31 | 19 | 8 | 1.9 | 1.9 | 1.9 | 0 | 21 |
| D.38 | 50 | 30 | 20 | 20 | 0 | 0 | 0 | 0 | 21 (hence 40) |

Verdict: sentence length matches the models. The book's tics ("so", "only", "gives", "therefore") run at 3–6 times Lin's rate, and the models' connectives ("however", "we will/can/see", "typical", "note that") are nearly absent in every section. Each writer should convert about a third of the "so … " clauses into "since"/"because"/"as a result", and add a "however" wherever a real contrast is written as a bare juxtaposition. Examples: 14.1 l.76, 14.3 l.73, 14.4 l.62.

**Calibration (2–3 passages per section; would Lin or Kahn–Lin write this?)**
- 14.1 l.110 "Two limits fix the shape of the rate before any integral is done": yes (estimate first). l.25 "Physically, a long-wavelength transverse probe tries to tilt…": yes. l.115 "This is the flux … times a cross-section per ion. The cross-section is that of a free electron, rescaled … At large momentum transfer the magnet scatters like a set of free spins…": no, the third sentence repeats the first two. Rewrite: "In other words, at large q the magnet looks like a gas of free spins, each with the transverse weight W_⊥ in place of the electron's 3/4."
- 14.2 l.56 "NiO gains little because its magnons are fast": yes. l.117 "In the nuisance types of \cref{sec:8.8} they are new support, a normalization and a tilt, and each is one step of the expansion…": no (bureaucratic; "respectively" pairing in disguise). Rewrite: "In the language of \cref{sec:8.8}, the continuum adds new support, the weight defect is a normalization, and the hybrids tilt the spectrum."
- 14.3 l.3: yes. l.137 "an antiferromagnet trades rate for reach": yes. l.56 "Consider a magnet whose spins interact by exchange that is invariant under a common rotation of all spins, as …, in a uniform field, with one value of λ_S and of g for all ions.": no (stacked appositives). Rewrite: "Take a magnet with rotation-invariant exchange, such as the Heisenberg model \cref{eq:7.1-heis}, in a uniform field, and give all ions the same λ_S and g."
- 14.4 l.3 "The catch is that a neutron sees only…": yes. l.114: no (see 14.4 issues). l.109 "Errors decide whether the inversion is worth doing.": yes.
- 14.5 l.63 "That number sets a scale only.": yes. l.22: no (four symmetry statements in one paragraph without a picture). Add the picture first: "Physically, 𝒢_OA measures whether the electrons circulate one way more easily than the other along q, which only a handed crystal allows."
- 14.6 l.157 "Inside one coherence time the signal adds in amplitude and the noise in power…": yes. l.30: no (it narrates the Kubo formalism before saying why). Rewrite the opener: "We need two things from linear response: the signal a readout sees, and when its average turns into the golden-rule rate."

## 3. Issues by section (location → problem → fix)

### Chapter opening (ch14.tex)
1. l.2 → two closing orientation sentences ("It builds on … follow in \cref{chap:15}. \Cref{fig:14-map} shows how the sections connect, and the chapter summary collects …"), against the "at most one" rule. → Keep "It builds on … \cref{chap:15}." Merge the map reference into it ("…; \cref{fig:14-map} maps the sections.") and cut "and the chapter summary collects the magnet inputs and the size of the 1/|S| corrections in one table".
2. l.2 → the three questions omit 14.5 (chiral and multiferroic targets), so the opening covers five of the six sections. → Add a clause: "…and which crystals, by breaking inversion or time reversal, respond differently to q and −q".
3. Map caption l.7 → stands alone and is concrete. It carries hard-coded Limit Check numbering via map14.py (editor note: the 14.4a box is labeled "Limit Check 14.3"). → Rerun map14.py before sign-off. Not a prose fix.

### 14.1
4. l.3 → the opener's last two sentences outline the section ("We derive …, insert …, and estimate … The result is …"). This is acceptable after a concrete first sentence, but "Here we turn those weights into a rate." already says it. → Cut "We derive … ordered moment." and keep "Here we turn those weights into a rate, from the lightest mass that can emit a magnon above a few meV to masses where the magnetic form factor cuts it off."
5. l.115 → pattern 26 restatement inside the paragraph (see calibration). → Replace the last two sentences before "With ⟨v⟩ = …" with the one rewrite given above.
6. Titles l.29 "The one-magnon rate" and l.106 "The one-magnon rate of NiO" → near-duplicate titles. → l.29 "The orientation-averaged one-magnon rate" (or "Rate formula and mass edge").
7. l.124, l.126 → "19 percent", "20 percent", "three percent" next to \SI{7.8}{\percent} in the same section. The same mix appears in 14.4 (l.39, 104, 109, 111) and 14.5 l.144. → Use \SI{..}{\percent} throughout, as STYLE "numerals with units" requires.
8. l.126 "To see how much this matters, we add …" → filler opener (REGISTER: "to see this" at most once per chapter). → "We add an easy-axis term K …".
9. l.126 and caption l.120 → "zone-center magnon … far-infrared" for 4.54 meV. The editor note says the source calls it the M point. → The wording must wait for the source check; if the source is right, rewrite as "the magnon at 4.54 meV seen in far-infrared absorption".
10. Notation (editor note) → 14.1 w^M_q equals 14.2's w_⊥/|S|. → Pick one symbol (keep w^M_q; write 14.2's weight as |S| w^M_q) and update eq:14.2-wpar, fig:14-weights and 14.2 l.34–38.

### 14.2
11. l.3 "a fluctuation weight equal to \SI{7}{\percent} of the one-magnon weight … (\cref{sec:7.1})" → the 7% is derived in 14.1 (we:14-nio), not in 7.1, so the cref sends the reader to the wrong place. → "(\cref{we:14-nio})" for the number, keeping \cref{sec:7.1} only for "creates magnons in pairs".
12. l.3 "and no single magnon carries it" → negation framing (pattern 25). → "…carried entirely by magnon pairs."
13. l.3 "We will derive … the final-state interaction …, and the magnon--phonon hybrids …, and the section closes by sizing them for NiO as nuisances" → self-narrating outline (patterns 18, 22). → Keep one sentence: "Together with the weight defect of \cref{sec:14.1}, these are the 1/|S| corrections to the one-magnon rate, and for NiO we size each."
14. l.17 last sentence "In the same extended-zone convention the one-magnon weights … are the single expression (u − v)²" → repeats 14.1 l.9 and D.38 eq:D.38-weight. → Cut.
15. l.19 "This holds beyond linear order: the fully polarized state is an exact eigenstate…" → third statement of the ferromagnet result (14.1 l.74, D.38 l.61). → Cut to "(exactly, as in \cref{sec:14.1})".
16. **l.38 "Over the zone the ratio of averages is W∥/W⊥ = 0.073, with ΔS = 0.078. The same value of ΔS comes out with J₂ alone: … four interpenetrating simple-cubic antiferromagnets, whose zero-point reduction is 0.078, and J₁ changes it only in the fourth digit."** → repeats 14.1 (we:14-nio), which owns it (editor note). → Cut from "Over the zone" to the end of the paragraph, or reduce to "averaging to W∥/W⊥ of \cref{we:14-nio}".
17. l.51 "A single magnon near Γ, with ω = c_M q …, satisfies this only for q ≤ 2mχ(v − c_M)…" → re-derives eq:14.1-mmin. → "The one-magnon channel opens at \cref{eq:14.1-mmin}; a pair can take any energy …" (saves about 40 words).
18. l.73 "For NiO the interaction is not small …, and how it reshapes the continuum is open. … The solution …, and the existence, energy and weight of a bound pair …, are open." → "open" twice in three sentences. The last sentence ("Without it, … the sum rule above fixes its integrated weight") restates l.69 (pattern 26). → "For NiO, with 1/(2|S|) = 0.5, the solution of \cref{eq:14.2-ladder} and the existence of a bound pair are open; \cref{app:E.20} specifies the calculation: …" Cut the last sentence.
19. **14.2.5 l.117–125 (looped restatement)** → l.117 restates 14.1's 0.078 and l.38's 0.073. l.121 restates 14.1 l.76 in full ("transverse weight implied by … lower than … by ΔS/|S|, a lower estimate…"), adding only "with the sign that weakens it". l.125 "The chapter summary collects the three sizes with the magnet inputs." is a signpost. All of these rows reappear in tab:14-nuisances. → Keep only the new facts: (i) the q-resolved ratio (0.082 at 1.4 keV, < 0.05 below 0.5 keV); (ii) the final-state estimate 0.5 × 0.073 ≈ 0.04, moved in energy; (iii) the one-magnon defect weakens a limit; (iv) how B₁, B₂ are computed. That is about 150 words in one paragraph, down from about 520. Cut l.117, the signpost, and the restatement in l.121.
20. l.119 "so δ_k' is an estimate of that size"; l.125 "one parameter ϑ_k" → symbols not defined in this chapter (first use). → "the nuisance amplitude δ_k′ of \cref{eq:8.8-open}" and "the nuisance parameter ϑ_k of \cref{sec:8.8}", or drop the symbols (the prose does not use them again).
21. l.49 "a gap Δ in both branches" vs l.98 "detuning Δ = ω_m − ω_p" → one symbol, two meanings in one section. → Write the detuning as δ_mp or Δ_mp.
22. l.34 "Huberman and coworkers" vs "and collaborators" (14.3, 14.5, 14.6) vs "Berlin et al." (14.4) → three attribution styles across the writers. → Use "and collaborators" (or "et al.") everywhere; the chapter uses "and collaborators" 20 times.

### 14.3
23. **l.80 "The golden rule needs an exposure long compared with both t_coh and 1/Γ_M (\cref{sec:8.2-absorption})"** → contradicts 14.6 l.35–37, which shows the ensemble mean needs only t ≫ min(t_coh, 1/Γ_T). → "The golden-rule mean needs an exposure long compared with the shorter of t_coh and 1/Γ_M (\cref{sec:14.6-regime}); …". The editor note asks for a light pass on 8.2 as well.
24. l.75 "for the Kittel mode of YIG, Mitridate and collaborators take a full width Γ_M = 10⁻⁵ω" and l.139 "With the same ratio Γ_M/ω = 10⁻⁵" → the editor requires the text to say this is assumed, not measured. "take" is too weak, and MnF₂ inherits the assumption silently. → "…assume a full width Γ_M = 10⁻⁵ω; no millikelvin measurement exists." At l.139: "With the same assumed ratio …".
25. l.115 "The rate equals the coherent result of Ref.~\cite[Eq.~(38)]{chigusa…}, without its factor ½ for the hybridization with a cavity mode, when their coherence time is set to 4/Γ_M." → reconciliation aimed at a checker (pattern 19). → Cut, or reduce to one clause with attribution: "(the coherent rate of \cite[Eq.~(38)]{…} with t_coh → 4/Γ_M)".
26. l.107 "against the measured \SI{38}{emu/g} at \SI{0.1}{K} that Chigusa and collaborators quote" → bookkeeping. → "close to the measured 38 emu/g at 0.1 K \cite{…}".
27. l.3 "The spin waves of \cref{sec:14.1} away from k = 0 do not enter." → negation close (pattern 25). → "Only the k = 0 mode enters."
28. l.159 "The two corrections that the limit check does not show are those of linear spin-wave theory itself." → abstract category frame (pattern 18). → "Linear spin-wave theory itself adds no correction to the Larmor line and one to the antiferromagnetic weight."
29. Notation → Ω is the volume per magnetic *cell* here (l.58, YIG Ω = a³/2), per *ion* in 14.1–14.2, and the formula-unit cell in 14.4. ω_M is the magnetization frequency here, but a mode frequency in 14.5 (eq:14.5-GL), and ω^M_q is the magnon energy in 14.1. M ≈ 3.5 MeV (l.80) collides with magnetization M. → Unify per NOTATION (for example Ω_cell vs Ω), rename 14.5's ω_M to ω_{\mathrm{soft}} (editor note), and write the dispersion mass as M_{\mathrm{sw}}.
30. tab:14-lande caption "The last column divides it by the moment g_J/2" → unanchored "it" (pattern 13). → "The last column gives λ_S/(g_J/2), the spin coupling relative to the moment that a magnetic field, a neutron and a dark photon see."
31. l.3 de Broglie wavelength "1/m_φ v_E^ref" → v_E^ref is not defined in the chapter; elsewhere the text writes v_E and \vect{v}_E. → Define at first use ("with v_E^ref the reference speed of the Earth, \cref{sec:1.2}") and use one form.
32. l.139 MnF₂ 1.021 meV (fit) vs 1.1 meV (neutrons): both printed (editor note) → add the one-clause reason, otherwise the reader sees an unexplained 7% gap. For example: "the fitted fields neglect the zero-point and dipolar corrections that the neutron gap contains" (the reason must be confirmed).

### 14.4
33. l.33 "Neutron data on a rare-earth magnet thus say little about its spin response until C_sn is applied." → pattern 25 ("the data tell us"). → "For a rare-earth magnet the neutron response differs from the spin response by C_sn, from 1/9 (Er³⁺) to 25 (Sm³⁺)."
34. l.62 "For 𝒪_4 positivity gives half an answer." → figurative. → "For 𝒪_4 positivity gives only a lower bound."
35. l.72 "let g be an element of the magnetic point group" → g is the spectroscopic factor in this same section (eq:14.4-data). → Write the group element as 𝗀 or h.
36. **l.76 "The no-go is the standard projection rule read for dark matter, not a new limitation. For dark matter it puts 𝒪_6, 𝒪_10 and the absorption of axion-like particles out of reach … and leaves only a lower bound for 𝒪_4."** → repeats l.62 and l.64 (pattern 26), plus negation framing. → Cut both sentences; the subsection ends on the symmetry argument.
37. **l.114 closing paragraph** → restates the keyresult and l.62 ("no data-only route to it exists, and every route adds information that the cross-section does not contain"). Its new facts are only the model-fit route as a normalization nuisance and the permeability at q → 0 (already in l.64). → Reduce to one sentence: "A spin-wave model fitted to the transverse data supplies the longitudinal element too, with the fit uncertainty as a normalization nuisance (\cref{sec:8.8}); a measured longitudinal response at dark-matter momenta does not exist."
38. l.85 opener "What the data cannot supply, a symmetry of the spins can." → aphoristic cadence (STYLE "Plain words"). → "Spin-rotation symmetry about the moments supplies the missing element."
39. l.53 "the data-driven rate agrees closely with the Heisenberg-model rate" → vague quantifier (pattern 12). → Give the ratio from Berlin et al. Fig. 3, or "within a factor of …".
40. l.12 "Their susceptibility is χ'' = 2(1 − e^{−βω})S_ab …, the factor 2 because their spin operator is σ where ours is σ/2, and their constant … is r²_cl/4π." → convention bookkeeping. It is allowed only as one clause about the literature. → "(Berlin et al. write the spin as σ, so their χ'' is 2(1 − e^{−βω})S_ab.)" Drop the constant identity.
41. l.20 repeats 14.3 l.52 (L = (g − 2)S at first order, λ_S at second order) → acceptable as a short recap, but trim to "with g the spectroscopic g factor of a quenched ion (\cref{sec:14.3-lande})".
42. Subsection title "Couplings the data calibrate" → close to the gesturing type (pattern 21). → "Transverse projection of the neutron cross-section".
43. Editor items (citations, not prose): g ≈ 2.2 (Abragam, unread), L/S = 0.34 (Fernandez, closed access). l.39 attributes both as findings. → If the audit cannot verify them, soften to "quoted in \cite{kwon…}".

### 14.5
44. **14.5.6 "Open problems" (l.186–188)** → "Three inputs are missing." is a count-teaser (pattern 18). The paragraph restates l.63 (𝒢_OA at keV unknown), l.116 (the three-phonon linear system) and l.173/183 (T_CM unknown); its one new item, the giant phonon moments of lanthanide frameworks, is not in the section body. The title is generic. → Cut the subsection. Move the lanthanide-moment item into l.114 ("…which the Born charge does not contain; computing them needs the displacement derivatives of the crystal-field states, \cref{app:E.19}"). Pattern 3.7: end the section on l.183's limit box or on l.173.
45. l.107 "The angular momentum is a label of the final state, not a new coupling." → negation framing (pattern 6). → "The angular momentum labels the final state; the coupling is the density coupling of \cref{eq:11.1-S1}."
46. l.116 "The second fails as a conservation law." → unclear (it means L^ph is not conserved). → "The second is not protected: L^ph is not conserved."
47. l.166 "such as the one that cants the spins of the hexaferrite" → the material is hexagonal Lu₁₋ₓScₓFeO₃, a hexagonal ferrite. "Hexaferrite" names a different class (BaFe₁₂O₁₉). → "…of hexagonal Lu₁₋ₓScₓFeO₃".
48. l.166, eq:14.5-GL → ω_M (mode) clashes with 14.3's ω_M, and η_M (damping) with η(v_min). → Use ω_soft and γ_soft (editor note).
49. l.68 caption "schematic; no curve is a computed property of tellurium" → negation. → "Schematic: all curves are model curves, not computed for tellurium."
50. l.88 title "The point-group test for a response odd in q in α-quartz" → "in … in". → "Point-group test for odd responses in α-quartz".
51. l.142 "The avalanche itself is a response of the detector to heat, not a response of the target, and it belongs with …" → negation plus self-narration. → "The avalanche is a thermal response of the detector, treated with the readout models of \cref{chap:20}." (The editor's Alves check on the m_φ-only trigger is content, not prose.)
52. Seam into 14.5 → the opener jumps from magnets to α-quartz without saying why chirality belongs in a magnetic chapter. → Add one clause to l.3: "…unless inversion and time reversal are both broken, which magnetic order does for time reversal."

### 14.6 (see §5 for cuts)
53. **l.3 opener: "Over a record of a second … the spins tip together, and their transverse magnetization grows in proportion to the time. No rate in the sense of the golden rule exists over such a record…"** → contradicts the section. For ²⁰⁷Pb, T₂ = 16.7 ms = 0.016 t_coh (we:14-crossover), so the magnetization stops growing linearly after about 50 ms, and by l.37 the golden-rule mean holds once t ≫ min(t_coh, T₂). The opener also uses negation framing. → "…their transverse magnetization grows in proportion to the time until the spin coherence time T₂ caps it, after 17 ms in PMN-PT; the field's amplitude then changes only on the scale of a second. Whether the golden-rule rate describes such a record depends on the shorter of the two times."
54. **l.88 "The transient form is Eq.~(1) of Budker and collaborators~\cite[Eq.~(1)]{…}, whose amplitude agrees … although their text calls it the splitting. Their envelope … so the printed resonance is half as wide as the solution of the Bloch equation."** → pattern 19 (a reconciliation aimed at a reviewer), pattern 20 risk, and a doubled "Eq.~(1) of … [Eq.~(1)]" (the same doubling appears for Aybas in the next sentence). → Keep one clause: "This is the transient of \cite[Eq.~(1)]{budker…} (whose envelope has a factor 2 error in the detuning) and the steady state of \cite[Eq.~(1)]{aybas…}." Keep the u_sp definition.
55. l.90 "The drive is not a wave of fixed amplitude." → negation opener. → "The drive is the Gaussian field of \cref{eq:14.6-Sphi}, whose complex amplitude …".
56. l.30 "What a target does with the field follows from linear response." → abstract frame (see calibration).
57. fig:14-limit-mperp caption → "Gray" means the fixed-drive curve and also the validity band in the same caption. → Call the fixed-drive curve "Black".
58. **l.222 paragraph after the nuisance table** → a recap of table rows inside a subsection (pattern 26; only the Summary recaps). → Move it into the Summary as its first nuisance sentence, or cut it.
59. tab:14-nuisances basis labels "named" (no size) and "data" → internal status vocabulary (editor note). → "unsized" and "input spread", defined in the caption.
60. tab:14-nuisances row "Conversion of neutron data … 0.83 … computed" → omits 14.4's ten-percent g-uncertainty (0.73 at g = 2.34), which is exactly the nuisance (editor: recheck rows against s14-4/5). → "0.83 at g = 2.2, 0.73 at g = 2.34 (L/S = 0.34): about 10%, data". The row "Chiral frameworks … giant-moment amplitudes" refers to a statement that will only be in 14.5's body if item 44 moves it there.
61. l.28 "Some papers include a factor 2π … \SI{6.6}{s} at \SI{1}{neV}" → an acceptable one-clause literature convention note. App. E.26 uses the other convention (editor note), so fix E.26, not this sentence.
62. Summary l.243 "…that of four interleaved simple-cubic antiferromagnets" → fine in the Summary. It is the fourth statement in the chapter (14.1, 14.2, D.38, here); once 14.2 and D.38 are cut it is the second.

### App. D.38
63. l.3 "This appendix derives them …, and so obtains the results … of \cref{sec:14.1}." → self-narration (pattern 22), mild for an appendix. → "They follow from the operators of \cref{app:D.19} and give \cref{eq:14.1-Safm,eq:14.1-ratio}."
64. l.76 → repeats we:14-nio (ΔS = 0.078, J₂ alone, four sc lattices, grid convergence 5×10⁻⁵). → Replace with "The value for NiO, ΔS = 0.0784, is computed in \cref{we:14-nio}." (or keep it here and cut it from the worked example, but not both).
65. l.38 "since only the term v^M_k a_{k2}a^†_{k2} survives in the vacuum" → the term is (v^M_k)² a_{k2}a^†_{k2}. → Insert the square. (Typo-level; the derivation review should confirm.)

## 4. Chapter-level checks

**Opening:** concrete first sentence (silicon spins paired at 1.17 eV), motivational, and not an outline. Fix items 1–2.

**Summary (s14-6 l.224–253):** it covers all six sections in order, with numbers, and does not list sections mechanically. Problems:
- It sits inside s14-6.tex, which inflates 14.6's word count. Move it, with the nuisance table, to its own file (ch14/summary.tex).
- tab:14-inputs duplicates numbers in tab:14-nuisances and in the sections ("Values as stated in the sections listed in the last column, with their sources there" admits this). Merge it into one table, or cut the "Corrections beyond the model" column, which repeats the nuisance table.
- The 14.5 paragraph (l.251) carries no numbers. Add one: Mn₁₂-acetate line at 1.098 meV holding 90% of 2|S| below 4.2 K, or GaAs ⟨|L^ph|⟩ = 0.12.
- The last sentence repeats the chapter opening's pointer to Chap. 15. Keep one of the two.

**Redundancy across sections (beyond items above):**
- ΔS = 0.078 and the four sc lattices: 14.1 (owner), 14.2 l.38 (cut), D.38 l.76 (cut), Summary (keep).
- W∥/W⊥ = 0.073 and the 7.8% defect: 14.1 we, 14.2 l.3, l.38, l.117, l.119, l.121, 14.4 l.104, 14.6 table, l.222 and the Summary, nine times in total. Keep 14.1, 14.2 l.119 (q-resolved), the table and the Summary.
- One-magnon mass edge: 14.1 eq:14.1-mmin and 14.2 l.51 (item 17).
- Ferromagnet "exact eigenstate, S^z creates nothing": 14.1 l.74, 14.2 l.19, D.38 l.61 (item 15).
- Golden-rule validity: 14.3 l.80 vs 14.6 l.37, which are inconsistent (item 23).

**Seams (each adjacent pair read across the join):**
- 14.1 → 14.2: smooth in topic (anisotropy and thermal magnons, then pairs), but 14.2's opening cref is wrong (item 11).
- 14.2 → 14.3: 14.2 ends on how B₁, B₂ are computed, preceded by a summary signpost (item 19). 14.2 l.113 already sets up the uniform magnon of 14.3, so the join works once 14.2.5 is trimmed.
- 14.3 → 14.4: good; 14.3 l.52 ends by pointing to the g conversion that 14.4 uses.
- 14.4 → 14.5: abrupt (item 52), and 14.4 ends on restatement (item 37).
- 14.5 → 14.6: 14.5 ends on "Open problems" (item 44). 14.6's opener stands on its own, and 14.3 l.80 already forward-points to 14.6.

**Voice consistency across the six writers:** sentence rhythm and "we" usage are uniform. The differences are attribution style (item 22) and percent style (item 7). Openers differ: 14.2 and 14.4 end their openers with "We will …" outlines, while 14.3, 14.5 and 14.6 (apart from its last sentence) do not. Use the 14.3 form: the question and the answer's shape, no plan.

**Citation style:** consistent \cite[Eq.~(n)]. Doubled "Eq.~(1) of X~\cite[Eq.~(1)]" at 14.6 l.88 (×2). "Ref.~\cite" and "Refs.~\cites" appear four times; acceptable. Limit-box header lines follow STYLE (formula plus a one-line source).

**Cross-reference style:** all \cref/\Cref, with no hard-coded numbers in prose. 14.6 l.88's "Eq.~(1)" refers to external equations; fold it into the citation (item 54).

**Captions:** standalone, with units and parameters, except items 30 and 57. fig:14-neutron says "Right:" while its panels are labeled (a)/(b). → Say "(b), right-hand columns". Label `fig:14-limit` (14.3a) is generic; rename it fig:14-limit-absorption for consistency with the siblings.

**Pattern 25 sweep (chapter opening, every section and subsection opener, every caption):** hits are items 12, 27, 33, 34, 38, 45, 49, 51, 53, 55. Clean: the chapter opening, the 14.1, 14.3, 14.5 and 14.6 section first sentences, the subsection openers of 14.1, 14.3.1–3, 14.5.1–5, and 14.6.2–4, and all other captions.

**Pattern 26 sweep (paragraph fact lists; flagged where empty or a subset):** 14.1 l.115 (partial); 14.2 l.38 (second half), l.73 (last sentence), l.117, l.121, l.125 (signpost); 14.4 l.76 (last two sentences), l.114; 14.5 l.188; 14.6 l.222; D.38 l.76. Every other paragraph adds at least one fact, number or step.

## 5. 14.6 budget: proposed cuts (≈6,100 → ≈4,300 words)

| # | Cut | Saves (words, approx.) |
|---|---|---|
| C1 | Move `\section*{Summary}` and tab:14-inputs out of s14-6.tex into ch14/summary.tex (no loss to the chapter) | 950 |
| C2 | Move subsection 14.6.5 "Nuisance table of the magnetic sector" (chapter-wide, not about coherent fields) to the summary file, and cut the recap paragraph l.222 (item 58) | 650 + 110 |
| C3 | l.88 Budker/Aybas reconciliation down to one clause (item 54) | 110 |
| C4 | l.41 photon-counting statistics: keep "Var N = N̄ + N̄²/N_coh; counting searches have N_coh ≫ N̄ (YIG: 3.4×10⁷ coherence times per hour)"; cut the geometric-distribution derivation | 80 |
| C5 | l.30–39 Fejér derivation: state the kernel, the result t ≫ min(t_coh, 1/Γ_T) and the t² regime; move the amplitude-squared step to \cref{app:D.25} | 120 |
| C6 | l.16 sign discussion of k = −m_φv, down to one sentence ("the target receives p_φ = m_φv; the sign matters only for responses odd in q, \cref{sec:14.5}") | 60 |
| C7 | l.28 line-shape statistics: keep Δω_eq = 2.67/t_coh (used later); cut the peak, mean and half-correlation numbers | 40 |
| C8 | l.45–47 NMR background (Heisenberg equation for a spin, equilibrium polarization arithmetic): keep ω_Lar/2π, p_pol and M₀ for ²⁰⁷Pb | 70 |
| C9 | l.107 spin-noise argument: keep the result ("the spin noise does not depend on the polarization, \cite[Eq.~(A1)]{budker…}, so prepolarization raises the signal only") | 80 |
| C10 | l.109 material-inputs paragraph down to one sentence pointing to \cref{app:E.26} | 60 |
| C11 | Merge l.159 and l.171 (Centers comparison) into one paragraph; drop the repeated "counted once" logic | 100 |
| | **Total** | **≈2,400** (≈1,000 within the coherent-field prose, ≈1,400 by moving chapter-level material) |

C1 and C2 alone bring 14.6 to about 4,400. C3–C11 bring it to about 3,700 and also remove the process artifacts.

## 6. 14.1 / 14.2 repeats (brief item)

- ΔS: 14.1 we:14-nio owns ΔS = 0.0784, the J₂-only value and the four sc lattices (Anderson 0.078). 14.2 l.38 repeats all three, so cut it (item 16). 14.2 l.36 legitimately uses ΔS (defined in 14.1) to average w∥; keep it.
- "Four interleaved/interpenetrating simple-cubic lattices": 14.1 l.83, 14.2 l.38, D.38 l.76, Summary l.243. Keep 14.1 and the Summary.
- Also repeated: the extended-zone one-magnon weight (14.2 l.17, item 14), the ferromagnet exactness (item 15), the one-magnon mass edge (item 17), and the sum-rule defect (14.2 l.121, item 19).

## 7. Editor-notes items concerning prose (status)

| Note | Status |
|---|---|
| 14.1: unify w^M_q / w_⊥ | open (item 10) |
| 14.1/14.2: cut the ΔS and four-lattice repeats in 14.2 | open (item 16) |
| 14.1: 4.54 meV "zone-centre" wording | open, pending source check (item 9) |
| 14.2: tag the FSI 0.04 as an estimate | done (l.119 "an estimate"; table "est.") |
| 14.3: Γ_M = 10⁻⁵ω is assumed | partly done (table says "assumed"; text l.75 and l.139 do not), item 24 |
| 14.3: MnF₂ 1.021 vs 1.1 meV | both printed; reason missing (item 32) |
| 14.4: spectroscopic g, not g_J, for Ni²⁺ | done (14.4 l.20, l.35; 14.3 l.52) |
| 14.4: unread sources | citation audit; soften if unverified (item 43) |
| 14.4/map: Limit Check numbering | open; rerun map14.py (item 3) |
| 14.5: rename ω_M in eq:14.5-GL | open (items 29, 48) |
| 14.5: 0.124 vs 0.07 for GaAs | both printed with the reason (l.144); prose acceptable |
| 14.6: recheck nuisance rows against s14-4/s14-5 | one mismatch (item 60) |
| 14.6: "data" basis label | open (item 59) |
| 14.6: over budget | cuts in §5 |
| 14.6 vs 8.2 golden-rule condition | also affects 14.3 l.80 (item 23) |
