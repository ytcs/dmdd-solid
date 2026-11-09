# Ch4 revision ledger (2026-11-02)

One row per review item: item → fix → location. "Declined" and "Deferred" rows give the reason. Files: tex/ch04/s4-1…s4-9,
tex/appD/D-6…D-12, plus the named lines of C.5–C.7, A.7, E.6, macros.tex, SPINE.md and figscripts fig4_1.py, fig4_3.py.
Build: /tmp/build-ch04rev (wrapper main without ch05, which a concurrent edit leaves with undefined macros \ZRAWTEXT etc. in s5-5.tex).

## Editor rulings (brief) and editor-notes.md

| # | Item | Fix | Location |
|---|---|---|---|
| R1 | K^x relabel | D.12: orbital-basis kernel is K^x_full (eq:D.12-kernels, eq:D.12-BSE, spin, eq:D.12-blocks); split K^x_full = K^x_0 + K^x introduced once in the transition-basis section; eq:D.12-eig is H^exc with K^x; eq:D.12-crystal defines K^x (G≠0), K^x_full (all G) and K^d; response section: eq:D.12-Rexc = R̄₀₀ from H^exc, R₀₀ by rank-one closure, eq:D.12-S with E^full, A_full; eq:D.12-eps2 unbarred. K̄^x, Ā, Ē removed | D-12 |
| R1 | 4.9 equality with D.12 | now true as written (eq:4.9-bse = eq:D.12-eig with eq:D.12-crystal) | s4-9 l.27 |
| R1 | K^d index order (general form) | ρ_cc′(k′+q,p+G) W_GG′(p,0) ρ_vv′(k′,p+G′)*, p = k − k′; one-line derivation from eq:D.12-kernels added; "p = k′ − k" prose fixed | D-12 eq:D.12-crystal; s4-9 eq:4.9-kernels, WM paragraph |
| R1 | E.6 conjugate | \|Σ A ρ*\|² | E-6 (oscillator-strength sentence) |
| R2 | eq:4.7-ImSigma | −π𝖠/\|𝖦^R\|² | s4-7 |
| R2 | +i/V response rule | keyresult last sentence; D.11 T = 0 section with the counting (−i/V)(−i)^n i^{2n+2} = (i/V) i^n and the bubble check | s4-8 keyresult; D-11 |
| R3 | Bruus–Flensberg chapters | cited without chapters (TOC not verifiable: 403/503 earlier, arXiv/OUP not reachable now); also 4.1's "Chap. 6" left as is (not in ruling) | s4-7 l.3, s4-8 l.3, D-11 l.3 |
| R4 | Mermin causality | new subsection "Causality" in D.9: zero of the denominator ⇔ free mode; w_k-weighted norm F, dF/dt = −2γ[F − \|S\|²/W] ≤ 0 (Cauchy–Schwarz); w_k = 0 modes decay; z = 0 removable. Grid scan not included (process artifact) | D-9; pointer s4-5 after eq:4.5-mermin |
| R5 | WE 4.1 renames | λ → λ_osc, Δ → Δ_tl, M → M_osc ("a particle of mass M_osc") | s4-1 WE 4.1/4.2, Fig. 4.1 caption; s4-2 l.84; s4-3 l.60 and Fig. 4.3 caption; s4-4 WE 4.9; fig4_1.py, fig4_3.py relabeled and rerun |
| R5 | \SpecA | macro added; used for 𝖠 | macros.tex; s4-7, D-10 (s4-8 has none) |
| R5 | g_deg = 2 throughout Ch4 | eq:4.6-R0 g_deg/V, prose, E.6 pointer; D.12 "with two spins" → g_deg = 2 | s4-6 l.11–21; D-12 |
| R5 | notation drifts | see derivation-1 / derivation-2 rows; rows proposed | SEAMS 4.1, 4.3–4.9 |
| R6 | numerical-check sentences | cut: 4.3 (10⁻⁶ gas), 4.4 ("agree, as they must"), 4.5 (perfect screening 10⁻⁵, Mermin f-sum 2×10⁻⁵), 4.7 (10⁻⁶ sum rule, 2000-state diagonalization), 4.8 (2×10⁶ frequencies), D.7 (code-test aside), D.8 (10⁻⁶), D.9 (10⁻⁴), D.10 (three paragraphs), D.12 (four-orbital check). Kept: 4.5 plasmon share; WE 4.9 Monte Carlo; 4.7 residue physics | as listed |
| R6 | "In this section we" / 4.8 list opening | 4.5, 4.6, 4.9 rewritten as one "we will" clause after the motivation; 4.8 roadmap shortened | openers |
| R6 | 4.6 title | "Local fields and exchange–correlation kernels" | s4-6 l.1 |
| R6 | 4.6 → 4.7 join | 4.7 opens: "The last rung of 4.6 needs quasiparticle energies and a screened interaction, and both are properties of one added electron." | s4-7 l.3 |
| R7 | Fig. 4.7 caption, WE 4.11 | not touched (figure-pass agent) | s4-6 |
| R7 | Fig. 4.11 double counting in the text | new paragraph before the figure says the fitted bands contain the excitonic shift and the figure tests shape and weight | s4-9 Fig. 4.11 paragraph |
| R7 | published BSE spectra | Albrecht 1998 (both peaks at measured energies, measured E₁/E₂ ratio, slight overestimate of heights; checked in sources/E-b/cond-mat_9803194.txt) and Reining 2002 Fig. 1 | s4-9 |
| R7 | published ε∞ values | **Declined (numbers)**: the values 13.9/12.7/13.3 could not be verified from any accessible full text (arXiv API down; Gajdoš 2006, Hybertsen–Louie 1987, Baroni–Resta 1986 not open); printing them unsourced would breach the citation rule. The trend is stated with a source instead (LF move weight up, Albrecht/Louie; by eq:4.4-inverse that lowers ε∞; ALDA ≈ RPA+LF, Onida/Botti/Reining). One-line insertion if the editor supplies a source | s4-6 Fig. 4.7 paragraph |
| R7 | "17 % → 11.9" | made moot: the model ratio is no longer applied to the WE 4.11 value (which the figure pass is replacing); text says the ratio is an upper estimate of what the attraction adds | s4-9 |
| R7 | ε∞ model triple six times | kept in WE 4.11/Fig. 4.7 only; pointers to we:4-siepsinf at 4.6 Fig. paragraph, ALDA paragraph, spread subsection; 4.9 ladder; Summary | s4-6, s4-9 |
| R8 | A.7 "first term" | "resonant term" | A-7 l.17 |
| R9 | exciton summary | "measured 14.7 meV is not a prediction: it fixes μ_x = 0.15 m_e and the radius 4.2 nm"; GaAs 3.7 vs 4.2 meV with ε₀; α/ε∞ | s4-9 Summary |
| R10 | WRONG/GAP items | see derivation reports below | — |
| EN | Kubo isolated/isothermal | "isolated from any bath, Kubo's isolated response" | s4-1 static limit |
| EN | 4.3 Bunge, TRK split | checked by derivation-1; no change | — |
| EN | 4.4 ε₂ sum-rule pointer, Ē move, ω_res | already done; Ward identity now named in 4.4 for 4.8's reference | s4-4 |
| EN | 4.7 high-ω Σ wording vs 3.4 | unchanged: 4.7 says "mean-field (Hartree and exchange) potential of 3.4, built with the exact occupations", consistent with 3.4's HF | — |
| EN | SPINE figure list (fig4_3b, fig4_8b, fig4_9b) | added | SPINE.md 4.3, 4.7, 4.8 entries |
| EN | SPINE ε₀/ε∞ forward note backwards | fixed ("matters when E_x^b is small against optical-phonon energies") | SPINE.md 4.9 entry |
| EN | 4.6 trend stated with a source | done (R7 row) | s4-6 |
| EN | 6.3 must cite we:4-einstein | **Declined**: Chap. 6 is outside this revision | — |
| EN | C.6 Mermin attribution, E.4 Z*, C_F, E.6 exciton numbers | already done by the editor; no change | — |

## derivation-1.md (4.1–4.5, D.6–D.9, C.5–C.7)

| Item | Fix | Location |
|---|---|---|
| WRONG plasmon limit-box caption | "below 1.6×10⁻³, and below 3×10⁻⁴ for q < 0.30 k_F" | s4-5 Fig. 4.plasmon-limit |
| GAP 4.1 l.51 dimension | R(q,ω) eV², R(q,t) eV³ | s4-1 |
| GAP 4.1 l.112 isolated | reworded (EN row) | s4-1 |
| GAP 4.2 l.111 elastic term | many-body diagonal f = i, with cross terms; single-particle γ′ = γ terms vanish at T = 0 | s4-2 |
| GAP 4.3 gap bound | clause "to the accuracy with which the valence electrons carry their own f-sum (about 2 percent in silicon)" | s4-3 WE 4.6 |
| 4.3 l.176 "26 eV" | 26.5 eV | s4-3 |
| GAP 4.4 Knapen attribution | "unsymmetrized counterpart of the symmetrized matrix of Eqs. (A5)–(A7)" | s4-4 |
| GAP 4.5 Mermin causality | R4 | D-9, s4-5 |
| 4.5 l.168 1.8 → 1.9 | done | s4-5 WE 4.10 |
| 4.5 l.172 ε₂ = 0.22 | 0.224 (width 3.5 eV consistent) | s4-5 |
| Fig. 4.3b "10⁻¹¹" (not reproduced) | kept (caption of a figure that demonstrates the KK test; quadrature-dependent number is the figure's own) | s4-3 |
| Γ_w upright | \varGamma in 4.1 text/caption; fig4_1.py labels italic | s4-1, fig4_1 |
| bare n_B | n_B(ω₀) | s4-1 WE 4.1/4.2, s4-2 l.84 |
| bare η (switching) | η_b | s4-1 |
| bare η (hydrogen) | ξ_C, the Coulomb parameter of 2.2 (identical quantity) | s4-3 WE 4.5 |
| τ = t − t′ | s | s4-1 |
| κ in D.8 | k̃ | D-8 |
| ν, ν_± | **kept**, local-variable row proposed (C.8, which this revision may not touch beyond named lines, shares the Lindhard variables; ν as phonon branch never appears here) | SEAMS 4.5 |
| y two meanings | 4.1 rewritten with Re z, Im z; y = q/2k_F kept (shared with C.8-FL), row proposed; C.5's Im z = y untouched (not named for C.5) | s4-1; SEAMS 4.5 |
| bare u | row proposed (local cosine); slab displacement renamed s | s4-5; SEAMS 4.4 |
| α_pl, Ē rows | proposed | SEAMS 4.4, 4.5 |
| length conventions | 4.4 says "a length 1/q of 1.6 Å"; 4.2 already says 2π/q₀ | s4-4 |
| s4-4 l.185 projectile M | M₁ | s4-4 |
| C.6 M for the oscillator mass | **Kept**: C.6's oscillator is a ²⁸Si nucleus (M = 26.06 GeV), i.e. the generic nuclear mass of entry 24 | — |

## derivation-2.md (4.6–4.9, D.10–D.12)

| # | Item | Fix | Location |
|---|---|---|---|
| 1 | eq:4.7-ImSigma | R2 | s4-7 |
| 2 | +i/V | R2 | s4-8, D-11 |
| 3 | Bruus–Flensberg | R3 | s4-7, s4-8, D-11 |
| 4 | D.10 "10⁻⁵" | moot: the sentence is cut (R6) | D-10 |
| 5 | D.12 vs 4.9 relabel | R1 | D-12, s4-9 |
| 6 | K^d convention | R1 | D-12, s4-9 |
| 7 | spin factor 4.6 | R5 | s4-6 |
| 8a | bare ξ = ξ_{k−Q} | ξ′ (local, row proposed) | s4-8 boson Σ and cutting rule |
| 8b | E_k orbital energy | removed; ξ_k measured from μ_ch | s4-7 l.14, WE 4.7 |
| 8c | E_d clash | **kept and flagged** (Fig. 4.8b axis is labeled E_d) | SEAMS 4.7 |
| 8d | missing rows | proposed (𝖣₀, 𝖫/𝖫⁰, 𝖥^R, E_qp, Γ_qp, Γ_em/out/in, ω_Ein, ω_Q, V_k, B, K^x_full, ℓ_b, E_c, IP superscript left as a label) | SEAMS 4.7–4.9 |
| 9 | eq:A.5-optical vs eq:3.2-optical | D.12 now cites eq:3.2-optical | D-12 |
| 10 | E.6 conjugate | R1 | E-6 |
| 11 | 6.27 keV | 6.26 keV = 1.75 k_F in WE 4.10 and Summary; the duplicate in the 4.5 body is now a pointer to the WE | s4-5, s4-9 |
| — | typo "and and" (WE 4.11) | **Deferred** to the figure-pass agent, who owns WE 4.11 | s4-6 |
| — | 4.9 l.27 q_r wording | "the kernels are written with q_r in place of q, and the omitted term of K^x is then the one at G = G_q" | s4-9 |
| — | GaAs 3.73/15.0 | 3.74 meV, 14.9 nm | s4-9 WE |
| — | Summary 14.7 meV as prediction | R9 | s4-9 |

## prose.md

| Section | Item | Fix / reason |
|---|---|---|
| 4.1 | Γ sweep, p_i undefined, comma splice, G parenthesis, renames | done |
| 4.1–4.4, 4.7, 4.8 | "The treatment follows Refs." tic | **Declined**: one attribution sentence per section is the book's practice for sections that follow a textbook; 4.5, 4.6, 4.9 cite at point of use. Editor may rule |
| 4.2 | "the one", "the code", "it", double Van Hove credit, signpost l.25, opener repeat of 4.1 | done; "typical" added at q₀ |
| 4.3 | TRK authors, outline opener, "Nobody knows", "it and", Henke sentence, recap close, 10⁻⁶ line, η, "of order", "essentially" | done |
| 4.3 | 4.2 l.22 ω_q undefined | defined at eq:4.2-rate |
| 4.4 | "modelling", "of a few", "ahead of time", "Gaussian sources", "as they must", "transfer", caption "(dashed)", "of the order of" | done |
| 4.5 | f-sum self-contradiction, opener, three verification lines (two cut, l.117 kept), "It also", duplicate plasmon verdict (body now points to WE), parse of l.172, "one percent" vs "two percent" (now 1.2 % peak, 1.9 % zero), limit-box cite, u → s | done |
| 4.6 | title, "In this section we", ε∞ triple, ladder duplicate (rung list now only in 4.9; 4.6 keeps the spread statement), l.138 restatement merged, "honestly", TDDFT abbreviation, g_deg, register (2 however, 3 we will/can) | done |
| 4.6 | "and and"; 113-vector and 8³/20³ convergence sentence | **Deferred**: inside WE 4.11 (figure-pass agent) |
| 4.7 | "therefore" chain, "and…and", 1.17 vs 1.11, 10⁻¹³⁶, 2000 states, 10⁻⁶, "the result is the following", \SpecA, percent style (word "percent" chapter-wide now) | done |
| 4.8 | roadmap, ordinal "first term", "and…and", "with…with", 10⁻⁹ line, ℓ(x), "we arrive at the result" | done |
| 4.9 | "labelled", opener, count-teasers (three approximations named; "two limits" → "We can now see how…"), false D.12 equality, a undefined, LO–TO pointer, ladder subsection title "The completed ladder", Van Hove, α/ε∞, "about 1.26 keV" → "about 1 keV", ε∞ triple in Summary, "only" tics (four cut), register (4 however, 3 we will/can) | done |
| 4.9 | Fig. 4.11 caption trim "(20,736 transitions)" | **Declined (optional)**: the count lets the caption stand alone as a model specification |
| D.8 | ordinal "first term"; 10⁻⁶ line | done |
| D.9 | verbatim repeats of 4.5 (now points to 4.5), "+ c.c." in math, \vect{j}_e | done |
| D.10 | three verification paragraphs | cut |
| D.11 | Bruus chapters | R3 |
| D.12 | K̄^x naming, eq:A.5-optical, verification paragraph | done |
| C.5 | Kramers cite; v_C | done |
| C.6 | Bloch sentence | done |
| C.7 | v_C | done |
| D.7 | code-test aside | cut |
| Ch. | sec:4.8-removal label outside scheme | **Declined for now**: renaming touches 4.4 and 4.8 cross-refs only, but the label is invisible in print; listed in SEAMS 4.8 for the next renumbering |
| Ch. | 4.6 l.134 G_LF behavior | "beyond q ∼ k_F it stops growing and stays of order one" |

## reader-a.md

| Item | Fix |
|---|---|
| 4.4 transverse tensor too compressed | diamagnetic and paramagnetic parts written out with a displayed sum |
| 4.4 Ward identity by parts | named as a Ward identity (charge conservation); steps unchanged (reader reproduced them) |
| 4.6 "wings" undefined | defined at first use |
| 4.7 "no such expansion" assertion | pointer to D.11 |
| 4.8 sign rules | pointer to D.11 before the rules box |
| 4.9 K^x notation | R1 |
| 4.9 Woodbury step | two-line reduction displayed |
| 4.9 LO–TO | glossed with \cref{sec:5.5} (D.12 glossed too) |
| typos ("and and", "(dashed)", TRK authors) | "(dashed)" and TRK done; "and and" deferred (WE 4.11) |
| 17 % → 11.9 | R7 |
| Fig. 4.7: mark the DM window | **Deferred** to the figure-pass agent (Fig. 4.7 is being regenerated) |

## reader-b.md

| Item | Fix |
|---|---|
| 4.3 relativistic f-sum vs Dirac | sentence added: the 1/m_e expansion is the positive-energy statement; with the full Dirac H the double commutator vanishes and pairs at ∼2m_e carry the sum |
| 4.7 l.163, D.11 l.39 overstatement | "no expansion of this single-exponential form"; D.11 mentions the forward-and-back contour |
| 4.1 φ₀ coupling absorbed | coupling constant named and set to one |
| wings, LO–TO, Mermin causality, K^x, ℓ clash, μ_x as measured | done (see above) |
| ε both dielectric matrix and band energy ε_{nk} | **Declined**: NOTATION fixes ε_{nk} for band energies and ε_GG′/ε_mac for the dielectric function; subscripts disambiguate |
| 4.7 R(z) level-shift name | name dropped; "the slope of the level-shift function" |
| 4.9 81 meV grid-dependent | said so, with the reason |
| 4.2 S^st as probability; hidden δ(q) | "total weight per electron… not a probability"; g_pair − 1 form at q ≠ 0 |
| Fig. 4.11 double counting before the figure | R7 |
| ½ m_χ v² reminder | added in 4.6 spread subsection and 4.9 ladder (3.5 eV at 1 MeV) |

## Additions after the final check

| Item | Fix / note |
|---|---|
| g_deg in the 4.6 head formulas | eq:4.6-head, eq:4.6-eps2, eq:4.6-static now carry g_deg (were 2, 2π, 4). 4.2 WE ("with two spins … 4π") and D.8 ("with the two spins") are counting statements and keep the explicit 2 |
| D.9 proof symbols | local ς = Σδϱ_k, w_tot = Σw_k, Φ_ϱ (norm); 𝒮 is avoided (transition sum) — local, no NOTATION row needed |
| **Coordination (figure pass)** | s4-6 passages outside the protected zone still carry the empirical-pseudopotential model's numbers and wording and go stale with the QE figure: opener l.3 ("band energies fitted to experiment", "within a few percent of 11.7", "about a tenth", "about half"), the Fig. 4.7 paragraph (4.26, 41, 46, 15, 36, 34, 4.32, 13; "empirical pseudopotential bands … no scissor is needed"), the panel-(b) paragraph (10–35 %, 7.6 → 3.4), and the "about a tenth / about a quarter" of the spread subsection. To be revised with WE 4.11 by whoever finishes the figure pass. 4.9's Fig. 4.11 numbers are its own model and stay |
| SEAMS 4.7 \SpecA | a macro note, not a new row (NOTATION l.321 has 𝖠) |
