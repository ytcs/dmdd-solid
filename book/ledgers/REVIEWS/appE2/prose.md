# Appendix E prose review, E.14–E.27 (computational specifications, isolated)

Read against STYLE.md, style-guide.md, prose-review.md (patterns #1–20), REGISTER.md and the prose items of ledgers/REVIEWS/appE/editor-notes.md. Line numbers are those of `tex/appE/E-N.tex`. No tex edited. Word counts are raw `wc -w`, so markup is included.
**Verdict rule.** PASS: at most 3 minor hits per 1,000 words and no systemic pattern. REVISE: the voice is sound, but there are systemic patterns or more hits than that. REWRITE: the structure or voice fails throughout.
**Scope caveat.** Chapters 8–21 are not yet in `tex/`. Duplication with the main text is therefore flagged only where a passage restates what its own `\cref` target promises. Duplication inside App. E is stated as fact.

## Verdicts

| Sect. | Words | Verdict | Main reasons |
|---|---|---|---|
| E.14 Phonon-assisted recoil | 4088 | REWRITE | form-template headings (Inputs and codes / Controls and acceptance / Cost / Pitfalls); 9 process sentences; ordinal list of six controls; Cost and Pitfalls restate E.5 and the section itself |
| E.15 Excitons, core states | 2382 | REVISE | roadmap list omits the 7th subsection; an imperative; process ("has been computed"); colon-reveal |
| E.16 Response libraries | 3276 | REVISE | 8-item roadmap; "two diagnostics" for 3 values; undefined 2W; reviewer-facing aside on Sect. 4.3 |
| E.17 Lattice libraries | 3653 | REVISE | roadmap sentence; "one runs"; process closing; count-teasers; unanchored "It" |
| E.18 Migdal, non-adiabatic | 2077 | PASS | "these four" unanchored; "the converse of each other" is wrong; otherwise clean, with "we" used well |
| E.19 Anharmonic, quantum solids | 2806 | REVISE | garbled cost sentence (l.15); 2 lint sentences that need splitting; process aside |
| E.20 Magnetic, SC, Dirac | 3276 | REVISE | over budget; citation as content (#20); "re-plots" title; restates 14.1/15.1; ε_bg ambiguity |
| E.21 Dopants, color centers… | 2713 | REVISE | title not a short noun phrase; "new module" ×3; "computable and missing"; restates 16.2/16.6 |
| E.22 Defects, TLS | 3373 | REVISE | British "aluminium" ×4; configurational-table rule repeated; code-manual aside; counterfactual paragraph |
| E.23 Recoil partition | 2844 | REVISE | displacement protocol duplicates E.11 with different numbers; "open calculation" process; units |
| E.24 Electron cascades | 3368 | REVISE | two miscounts ("four changes", "three more"); undefined "1.3"; tautology; restates E.13 |
| E.25 Event-level transport | 4467 | REVISE | over budget; ε₀ clash; U_el/U_rel; war-story artifact (l.67); #20; abstract closer |
| E.26 Coherent, fermionic… | 2137 | REVISE | lint title; Fano map misplaced; "respectively"; stray comma; stacked hedge; #20 ×2; no closing |
| E.27 Halo, backgrounds… | 1348 | REVISE | 5 hits in 1348 words, one of them #20; title vague; "saturation 11" elliptical; shell-model values only by citation (#20) |

## Lint (step 1)

| File | Hits | Notes |
|---|---|---|
| E.14–E.27 | LONG-SENT 15/9/7/18/1/5/7/7/1/1/1/1/4/4; TITLE 1 (E.26); EQ-PUNCT 1 (E.18) | 0 blocking. About half of the LONG-SENT hits are artifacts (tables, or a `\section` merged into the first sentence). The real ones are listed per section. E.18 l.53 EQ-PUNCT is a false positive: the `gathered` block ends ", " and the clause "and every Umklapp term" continues it. |

Greps for completeness: no `enumerate`/`itemize` and no `limitbox` in E.14–E.27, so the limit-box rule is not engaged. No `campaign`, SPINE, SEAMS, ledger, TODO or reviewer labels. "pre-registered" (E.14 l.75) and "interim factor" (E.14 l.47, E.16 l.19) are the internal labels that remain. The imperatives addressed to the reader are E.15 l.14 ("run the full coupling, or use…") and E.17 l.41 ("one runs"). "Take a cylindrical Gaussian track" (E.23 l.41) is a mathematical "take", the way Lin uses it, and is fine. User rules: no exercises, checkpoints or steps left to the reader (grep for reader/exercise/checkpoint/left to/can check: none). The general background is succinct, except for the restating passages listed under Length (E.21 l.32, E.22 l.9/l.38, E.25 l.37).

## Chapter-wide findings

1. **Register deficit (REGISTER §4), the same in every section.** Per 10k words: "however" is 0 in all 14 sections (L 8.0); "we" is 0–18 (L ~40 summed); "so" runs 23–52 (L 11); "only" 12–54 (L 11); "gives" up to 44 (E.16; L 7); "must" 30–91, with E.25 at 76 and E.26 at 91. "typical" is 0 in 12 of 14 sections (L 15). The specifications are read as flat obligations joined by "so". Fix: in each subsection, give one reason with "since" or "because", one real contrast with "however" or "but", and one "we" where a choice is made ("we take", "we report"). Cut every second "must" where the sentence reads as well as a statement of fact ("The sum rule holds to 10⁻³" in place of "must hold to"). This item is not counted against each verdict separately.
2. **The template in prose (#10, #11).** Nearly all of the 88 subsections run the quantity → method → acceptance → cost → "enters" slots, and 31 also carry an explicit "On 𝔗 …" sentence. The full order is: "The quantity is … On 𝔗 … The method is … The acceptance tests are … The pitfalls … The cost is … The result enters \cref{…}." Counts per file: "acceptance test" 1–9, "The cost is / costs about" 1–8, "enters \cref" 0–5. It reads as a form filled in prose, which is the recipe-list problem in disguise. Fix: open each subsection with the physical reason the number is needed (E.20 l.3, E.22 l.3 and E.27 l.3 do this well). Merge cost into the method sentence. Let the closing "enters" sentence go where the opener already said where the number goes. Vary the order; acceptance can come before method when the test is what motivates the calculation (E.14 l.53 is the model).
3. **Process artifacts (#19), about 25 hits.** E.14 l.63 "is no longer open", l.67 "has been computed once", l.69 "the first calculation chose", l.71 "one earlier on-axis value … that route has already been taken. What the new calculation adds", l.75 "pre-registered control", l.85 "In the one calculation done so far", l.92 "the old 0.89", l.102 "turn three open rows into established ones"; E.15 l.3 "has been run … only", l.56 "In silicon this has been computed"; E.16 l.40 "which \cref{sec:4.3} did not estimate … stands until it is computed"; E.17 l.85 "no longer carry estimates where a calculation can stand"; E.19 l.46 "and \cref{sec:16.7} labels it so"; E.20 l.52 "and the text states that choice"; E.21 l.14/28/32 "A new module"/"The new module", l.49 "computable and missing"; E.23 l.27 "lists their prediction as an open calculation"; E.25 l.9 "the exciton module is new code", l.67 overflow-list story; E.26 l.31 "never copied from a template". Fix: state the physics or the value. Mark each fix "→" in the per-section lists below.
4. **Count-teasers (#18).** E.14 l.51 "six controls test the physics" is followed by "The optical limit comes first … The second … third … fourth … fifth … A sixth". E.17 l.17 "Three traps are worth naming" and l.81 "Four rules … First, … Second, … Third, … Fourth". E.16 l.36 "Convergence has five parts". E.24 l.13 and l.15 announce counts that are wrong (see E.24). Fix: name the members in the teaser sentence, or drop the number.
5. **Self-reference to "the book" (#15).** E.14 l.3 "The book knows that rate" is anthropomorphic. E.18 l.3, E.20 l.3/32, E.26 l.21 and E.27 l.3 are acceptable. Fix only E.14.
6. **Writer split (voice consistency).** E.14–E.21 write `\dd`, `\Imag` and `$10^3$`. E.23 mixes `\dd` and `\mathrm{d}`, and E.25–E.27 use only `\mathrm{d}` (×6, ×6, ×3); `\mathrm{Im}` (E.26 l.27), `\num{e3}` (E.25 ×19, E.26 ×8) and `E_{\mathrm{g}}` for `\Eg` (E.25 l.47/57, E.26 l.15). The zone point is `\mathrm{\Gamma}` in E.14–E.17 and bare `\Gamma` in E.20/22/25/26; it is upright in both and correct per the Γ ruling, so only the source is inconsistent. Fix: use the macros throughout. Rates are `\varGamma` everywhere, so the ruling is satisfied. 𝔗 is inline `\mathfrak{T}` per the editor note; leave it unless `\Trunc` is adopted.
7. **Closings.** E.14–E.17 and E.19–E.21 end on "The result enters …". E.23 and E.24 end on a good consequence sentence after the table. E.18, E.20, E.21 and E.22 end on a table with no closing line. E.26 ends on a cost. Fix per REGISTER 3.7: E.22 and E.26 need a one-sentence close (proposals below).
8. **Captions and abbreviations in tables.** These tables use abbreviations that their captions do not define. E.20: KK. E.21: CNT. E.22: NEB, SCF, MD. E.23: MLIP-MD, MC, TDDFT. E.24: "Si gate" (jargon), GW+BSE. Fix: spell each out once in the caption ("NEB, nudged elastic band"). The captions otherwise stand alone.
9. **Equation punctuation.** All 29 displays in E.14–E.27 are punctuated as part of the sentence. No action.
10. **Citation style.** It is uniform (`\cite[Eq.~(n)]`, "Ref.~\cite"). Pattern #20 hits: E.20 l.54 "with the parameters of their Tables~1 and 2"; E.25 l.67 "must fall with energy, as in the thin-film calculations of Ref.~\cite{guruswamy…}"; E.26 l.21 the pair tensor given only by "\cite[Eqs.~(3), (5)--(8)]{bauer2026dark}"; E.26 l.21 "rescaled to the book's 0.3", where the source's value is not stated; E.27 l.34 the shell-model ⟨S_p⟩, ⟨S_n⟩ "taken from the nuclear-structure literature". Fix: state the values or the formula in the book's notation. A 3-row table suffices for E.20 (Δ_D, v_D,i, ε_bg,ii per material) and for E.27 (²⁹Si, ⁷³Ge).
11. **American spelling (editor ruling).** "aluminium" appears in E.22 l.7, 13, 17 and 40, against "aluminum" everywhere else. "centre" appears in E.16 l.65 and E.17 l.35 ("one-centre"). Fix: aluminum, one-center. One "respectively" remains (E.26 l.31).

## Opening, transition, summary, seams

- **Appendix opening (appE.tex l.3): PASS.** It frames both parts ("\Crefrange{app:E.14}{app:E.27} turn this around and specify, quantity by quantity…") and says what 𝔗 records, as the editor ruling asks. The **E.13→E.14 transition** therefore needs no bridging paragraph. However, E.14 l.3 should not re-frame the appendix. Cut its last two sentences ("Here we fix what is computed, on which grids, against which controls, and at what cost … We also specify the two smaller calculations …"), a four-part outline that repeats the appE framing.
- **Summary (appE.tex, after `\input{appE/E-27}`): REVISE.** It covers only E.1–E.13 (base calculation, convergence on the quantity used, three bookkeeping rules, silicon uncertainties) and says nothing on the 14 specifications. Add after "The rest are controlled numerically.": "The specifications that follow share one discipline: each calculation is accepted against an exact limit or sum rule and, wherever one exists, a measurement made at the same kinematics, never against the estimate it replaces. Their costs run from seconds (the pair-number library, the Dirac re-plots) to about 10⁶ core-hours (the close-collision kernel), and several of the cheapest, the verified onset of silicon, the boosted-dark-matter recast and the published-limit corrections, decide numbers the chapters quote today."
- **Seams (read across each join).** E.14/15: E.14 closes on a process artifact; fix it (E.14). E.15/16, E.16/17, E.18/19 and E.19/20 are clean. E.17/18: E.17 closes on a process artifact; fix it (E.17). E.20/21 and E.21/22 end on tables, and the next opener is concrete, so they are acceptable. **E.22/23: the same rule appears on both sides of the join.** "One table of configurational energies" is stated in E.22 l.29, E.23 l.21, E.23 l.55 and E.23 l.76. Keep it once, in E.23 l.21, and point to it from E.22 l.29 and E.23 l.55. **E.23/24: parallel formula.** E.23 closes "lists the six calculations", and E.24 opens and closes on "six calculations". Fix: E.24 l.3 "Here we specify six calculations with it." → "With it we specify two cascades, two tests of its approximations, and two sets of inputs." Drop the four sentences that follow and fold the members into the subsection openers, which already name them. E.24/25: clean; the pointer E.24→E.25 is in place. E.25/26: E.25's closer is abstract (see E.25). E.26/27: E.26 has no closing line (see E.26).
- **Redundancy inside App. E (fact).** E.14 l.41 (dynamical quadrupole, "Quantum ESPRESSO does not compute it") and l.96 ("about 10¹⁶ floating-point operations …") restate E.5 l.43 and l.62. E.23 l.19 states a displacement-threshold protocol of its own (300 wedge directions × 20 initial conditions, bisected to 0.5 eV, 3–5 ps runs) beside E.11's (1000 directions, 1-eV steps, 20 ps). The editor ruling keeps one protocol, in E.11, so E.23 should point to it and state only what differs (`t_pr`, DFT spot-check). The 3–5 ps vs 20 ps difference goes to the reader review. E.24 l.11 and l.15 (plasmon not added twice; residue once) restate E.13 l.36 and l.85. E.25 l.11 (Hecht), l.41 (specular, lumped film) and l.67 (Y_qp benchmark) restate E.12 l.57–89. E.22 l.13 (α_ohm = 4K_b, spin counting) restates E.10.
- **Restating the target section (inferred from `\cref`).** E.20 l.36 W∥/W⊥ formula and its three numbers (Sect. 14.1). E.20 l.7, the first three sentences on the conserving form (Sect. 15.1). E.21 l.49, the color-center yield factorization (Sect. 16.6). E.21 l.32, the three Coulomb kernels (Sect. 16.2). E.25 l.37, the definitions of ϖ_O, ϖ_gap and 𝔯_coll (Sects. 19.5, 20.5). E.25 l.29, the collective-release model (Sect. 19.6). Each should become one clause with the `\cref`. The verification is left to the seams review once those chapters exist.

## Length: concrete cuts for the over-budget sections

- **E.14 (4088 → about 3000).** (a) Cut l.3's last two sentences (−70). (b) l.41: keep "the dynamical quadrupole … taken from a long-wave DFPT code (\cref{app:E.5})" and cut the rest (−50). (c) Delete §Pitfalls (l.98–100). Six of its eight items repeat l.41, l.43 (×2), l.45, l.75 and l.79. Move the two new ones (the form-factor estimate is not a lower bound; near onset only the exponent is meaningful) into §Controls (−150). (d) §Cost (l.94–96): replace the E.5 restatement with "The amplitude costs what \cref{app:E.5} estimates." Move the stage costs into a 'cost' column of `tab:E14-params` (−170). (e) l.71: reduce to one sentence ("The bins must contain the joint optimum of \cref{sec:13.9}, 0.407 MeV, so that the edge is the one the rate sees") (−90). (f) Rename the headings by content and merge them: "Quantity and place on the hierarchy" + "Inputs and codes" → "The loss function and its inputs"; "Controls and acceptance" → "Six controls" (or name the first). Net about −550 before the rewrite tightens the prose. If the E.26 Fano map moves here (below), it adds +620, so E.14 ends near 3600. The recommendation is to move it anyway: it is the phonon-assisted sector by E.26's own admission (l.3).
- **E.20 (3276 → about 2800).** (a) l.7: first three sentences → "The conserving density response of \cref{sec:15.1} adds a phase-mode term to the bare bubble." (−60). (b) l.36: cut the W∥/W⊥ formula and its numbers to a `\cref` (−55). (c) l.54: cut the typographical-slip and Table-2 instructions to one clause, and drop "The sources keep the real part … doing both double counts" to a clause (−150). (d) Trim the cost clauses that repeat `tab:E20-params` verbatim (−80). (e) l.11: "The pitfalls are sign and consistency errors." → delete; the sentences that follow say it (−8).
- **E.21 (2713 → about 2350).** (a) l.49: the yield bookkeeping → "The yield factorizes as in \cref{sec:16.6}; two of its factors, p_FH(T) at millikelvin and the close-pair survival p_surv, have not been computed." (−90). (b) l.32: the kernels → `\cref{sec:16.2}` (−45). (c) l.22: the Du et al. erratum → two sentences (−40). (d) l.45: "The final-state interaction … double counts" → keep the bound and the double-counting warning, and cut the method description to one clause (−70). (e) l.55: the kinematics restates Sect. 16.6 → one clause (−60). (f) Use the short title (below).
- **E.22 (3373 → about 2900).** (a) l.9: cut the counterfactual "If both configurations were diagonal … the eigenphase form does." to "The eigenphase form holds for a hop that displaces the scatterer, as for crowdions and hydrogen; a single-center phase-shift sum does not." (−75). (b) l.11 and l.55: reduce the memory arithmetic to the result ("about 7 GB per k point", "about 2.5 GB") (−60). (c) l.55: delete the sentence on the code's real-wavefunction shortcut at Γ (code manual) (−40). (d) l.29: replace the configurational-table rule with a pointer to E.23 (−50). (e) l.29: the Poisson-capture sentence → \cref{eq:E.15-ste} (−35). (f) l.38: the coth derivation of S_pol(T) → state the result and point to App. D (−50). (g) l.13: the spin-counting paragraph → one sentence, pointing to E.10 (−50).
- **E.25 (4467 → about 3700).** (a) l.37: the definitions of ϖ_O, ϖ_gap and 𝔯_coll → one sentence with `\cref{sec:19.5,sec:20.5}` (−170). (b) l.41: the mean-field limit description → one clause (−80). (c) l.67: delete the fixed-length-list overflow story. Keep "The closure counts escaped energy as phonons actually returned to the substrate, so that an escape bin cannot absorb lost energy." (−80). (d) l.43: cost arithmetic → "about 140 core-hours per geometry; a first pass at 10³ phonons per cell takes under an hour" (−60). (e) l.11/l.41/l.67: point to E.12 for the Hecht, specular and lumped-film benchmarks (−60). (f) l.3: delete "Where a quantity needs more, we say so." (−7). (g) l.29: compress the collective-release recap to the two missing inputs (−80). (h) l.9: "with four additions …" — keep, but cut "G4CMP-class codes … new code" (−20).

## Per-section issues (location → problem → fix)

**E.14 — REWRITE** (structure and process, not voice; the physics sentences are good)
- l.3 "The book knows that rate to a factor of ten." → #15 → "That rate is known only to a factor of ten."
- l.5/11/49/94/98 headings "Quantity and place on the hierarchy", "Inputs and codes", "Controls and acceptance", "Cost", "Pitfalls" → form template; "hierarchy" is not the book's word (the label is the "truncation label") → content headings, as in Length (f). "The onset, verified" → "Verification of the onset".
- l.43 "A rule from \cref{app:A.5} decides whether the result means anything:" → dramatic frame (#8) → "One gauge, \cref{app:A.5}: the vertex g, … are rotated with one set of matrices U(k), since …"
- l.51–57 "six controls … comes first … The second … A sixth" → ordinal list (#11, #18) → open each with what it tests: "The optical limit tests the vertex against data. … Switching g off tests the labeling of final states. … A frozen phonon at X tests the adiabatic form …"
- → l.63 "The magnitude of the allowed (2̄00) vertex is no longer open: computed at the class extremum," → "At the class extremum the allowed (2̄00) vertex is Σ|ρ_cv|² = 0.150, the size of an ordinary allowed vertex (\cref{sec:13.9})."
- → l.67 "has been computed once" → delete the clause. → l.69 "the first calculation chose the PBE one because the window branch is better there" → "We use the PBE one, where the window branch is better."
- → l.71 see Length (e). → l.75 "The pre-registered control is the band order before any scissor:" → "The control, checked before any scissor, is the band order:". "may apply with more force" → "applies with more force, since its heavy hole is more anisotropic," (#4).
- → l.85 "In the one calculation done so far, with norm-conserving pseudopotentials," → "With norm-conserving pseudopotentials". → l.92 "how much of the old 0.89 was never missing" → "how much of the 0.89 shortfall is the nonlocal term, not missing bands".
- → l.102 "turn three open rows into established ones" → "replace the three estimated entries of its table with computed ones."
- l.47, "the interim factor of \cref{sec:13.9}" (also E.16 l.19) → internal label → "the factor [0.4, 1.8] that \cref{sec:13.9} assigns to local fields and the pair channel".
- l.96 "of order 50 to 70 core-hours" → REGISTER tic → "50 to 70 core-hours".
- *Calibration.* l.67 "The onset is therefore robust to everything except a systematic error in the transverse-acoustic branch." Lin could have written this: yes. l.43 (above): no. Lin-style rewrite: "Everything here hinges on one gauge: the band sum multiplies matrices in band space, so g, ρ and the energies have to be rotated with the same U(k), or the phases scramble."

**E.15 — REVISE**
- l.3 "This section specifies five excitonic calculations and one core-level one: …" → a mechanical list (#18) that also omits §Spin–orbit mixing → "We need the BSE beyond its resonant form, and with it the exciton series, the phonon replicas, the Migdal lines and the self-trapped exciton; the semicore response and the spin–orbit mixing at the edges complete the set."
- l.14 "Two routes avoid the error: run the full coupling, or use the resonant BSE only for …" → an imperative → "The error is avoided either by the full coupling or by keeping the resonant BSE for the proper ε₂ only and taking the external screening from …"
- l.35 "has one open point that no crystal calculation can test: its completeness." → colon-reveal (#8) → "Whether the replica formula is complete cannot be tested in a crystal." "The cost is minutes to an hour of a scripting language." → "It runs in minutes to an hour on one core."
- → l.56 "In silicon this has been computed: the on-axis zero is lifted" → "In silicon the on-axis zero is lifted".
- l.52 "By analogy with the valence BSE, the cost is of order 10³" → "of order" tic → "∼10³ core-hours per material, by analogy with the valence BSE".
- *Calibration.* l.18 "Even the fine grid cannot resolve the silicon exciton." Yes, a Lin-like short sentence. l.20 "Three checks decide acceptance." No. Rewrite: "The coupling block restores the f-sum rule, so with it on the sum rule should hold to better than a percent."

**E.16 — REVISE**
- l.3 "This section specifies that library and eight calculations built on it or beside it: …" (8 items), then "what is specified here is the content of the tables …" → roadmap (#18) plus meta → cut to "The library and the calculations built on it are specified below; the methods are those of \cref{app:E.6,app:E.7}."
- l.7 "which also fixes the independent-particle spin (triplet) block, a quarter of it" → unanchored (#13) → "…fixes the independent-particle triplet block, which is a quarter of the singlet one".
- l.15 "Two diagnostics come free: the components with ℓ = 1, 2 and 3 must be below 10⁻³" → the count does not match the three values → "Time reversal (ℓ = 1, 3) and cubic symmetry (ℓ = 2) give two free diagnostics: those components must be below 10⁻³ of the isotropic part."
- l.21 "The spec is 2000 to 8000 k points" → jargon → "The model uses 2000 to 8000 k points".
- → l.40 "which \cref{sec:4.3} did not estimate and" and "stands until it is computed" → reviewer-facing (#19) → drop both clauses. The sentence (lint, >45 words) splits at "; A Thomas–Fermi".
- l.52 "above 2W ≈ 0.1 multiphonon terms are added" → 2W is not defined at first use → "above a Debye–Waller exponent 2W ≈ 0.1".
- l.65 "The next rung is the RPA with local fields." → dangling → "Local fields, the next rung of 𝔗, are added at RPA level."
- *Calibration.* l.11 "Two calculations ride on the library." Yes (colloquial, Lin-like). l.36 "Convergence has five parts." No. Rewrite: "Since the inverse fourth moment weights the gap as E_g⁻⁵, every convergence test is run on that moment, not on L itself."

**E.17 — REVISE**
- l.1 title "Lattice libraries and lattice data" → repetitive → "Lattice libraries".
- l.3 "This section specifies the shared harmonic base first, then the libraries built on it, then the extensions beyond it, and last the per-material batch." → roadmap (#18) → delete. The preceding sentence already names the members.
- l.17 "Three traps are worth naming." → filler (#1) → delete; open with "The exponent 2W_κ uses B_κ with the thermal factor 2n + 1;".
- l.29 "It must not be used at finite temperature" → unanchored "It" (#13) → "The lattice sum \cref{eq:E.17-Wn} must not be used …"
- l.41 "In practice one runs at 50 to 100 K" → "one runs" is forbidden (REGISTER §4) → "In practice the runs are at 50 to 100 K, corrected to zero temperature with …"
- l.81 "Four rules make the numbers usable. First, … Fourth," → enumeration in prose → keep the four as sentences and drop the count and the ordinals.
- → l.85 "With these tables the material columns of \cref{sec:21.7} no longer carry estimates where a calculation can stand." → "With these tables every material column of \cref{sec:21.7} rests on a measurement or a calculation."
- *Calibration.* l.11 "the deformation terms dominate the soft limit by two orders of magnitude". Yes. l.7 "and a mismatch between channels computed from different lattices is an error that no single channel reveals". Yes.

**E.18 — PASS**
- l.3 "We specify these four calculations here." → "these four" is unanchored (the four were never listed) → "We specify four calculations: the drag masses, the crystal Migdal rate, the error of the Wannier picture and the matrix elements of couplings not proportional to mass."
- l.33 "the drag mass of the previous subsection" (also E.20 l.38 "the previous subsection") → ordinal reference (#13) → `\cref` to a subsection label.
- l.64 "The pitfalls are the converse of each other." → inaccurate (one pitfall drops terms, the other double counts) → "The two pitfalls err in opposite directions:".
- *Calibration.* l.14 "Above that the computed 𝓘₄ is needed." Yes. l.25 "And in a polar crystal the Q = 0 response must be taken at zero macroscopic field … because the drag mass belongs to the transverse displacement." Yes.

**E.19 — REVISE**
- l.15 "The self-consistent harmonic ladder costs about 10² for the self-consistent harmonic ladder, 10³ for helium at melting and 10⁴ per pressure at high pressure." → garbled → "The self-consistent harmonic runs cost about 10² core-hours per material, 10³ for helium at melting and 10⁴ per pressure at high pressure."
- l.27 and l.59 → lint sentences of over 45 words that need splitting. In l.59, start "Let P_K(u) be the projector …; O is the spin s_e or orbital moment L; R = …" as its own sentence.
- l.46 "It is about 300 lines of code and CPU minutes." → "The code is about 300 lines and runs in CPU minutes." → "and \cref{sec:16.7} labels it so" → delete (#19).
- *Calibration.* l.19 "Time reversal fixes the structure." Yes. l.7 "The calculation has two layers: exact moments, and an approximate real-time response tested against them." Yes.

**E.20 — REVISE**
- l.48 title "Anisotropic ZrTe₅ and the Dirac re-plots" → jargon → "ZrTe₅ and corrected Dirac reaches".
- l.15 "k_F 𝔩_e ≈ 1" → 𝔩_e is not defined at first use → "k_F𝔩_e ≈ 1, with 𝔩_e the elastic mean free path,".
- l.50 vs l.52: "the harmonic mean of the clamped-ion dielectric tensor" vs "the static ε_bg includes the ionic part, and the text states that choice". The two descriptions read as contradictory; this goes to the reader review. → Drop "and the text states that choice" (#19).
- l.54 "with the parameters of their Tables~1 and 2" → #20 → add Δ_D, v_D,i and ε_bg,ii for the three materials to `tab:E20-params` or to a small table. "are kept or explicitly dropped" → this is an instruction to the reviser, not a statement → "are kept".
- *Calibration.* l.3 opening. Yes; the aluminum/WSi contrast is REGISTER 3.5. l.11 "The pitfalls are sign and consistency errors." No. Rewrite: "The sign of i0 on the antiresonant pole is the easiest thing to get wrong: it must be that of the retarded function."

**E.21 — REVISE**
- l.1 `\section[Dopants, color centers and small targets]{Dopants, color centers, molecular and low-dimensional targets}` → the title is a four-item list, not a short noun phrase → use "Dopants, color centers and small targets" for both.
- → l.14 "A new module forms \cref{eq:E.21-gamma}" → "\Cref{eq:E.21-gamma} is formed from …". → l.28 "A new module takes transition densities" → "The transition densities are taken". → l.32 "The new module solves" → "The response is solved".
- → l.49 "Two of these factors are computable and missing" → see Length (a).
- *Calibration.* l.3 "A density-functional transition density between them is therefore not even defined." Yes. l.38 "a table of such ratios is not a rate correction". Yes.

**E.22 — REVISE**
- l.7/13/17/40 "aluminium" → "aluminum".
- l.13 "Two numerical errors are worse." → count-teaser, and "worse" than what is unstated → "Two numerical errors matter more than the spin counting:".
- l.25 "One number settles the verdict." → colon-like drama (#8) → delete; the next sentence stands alone.
- l.27 "The pilot is …"; "Production needs 50 paths per material" → workflow jargon → "A first calculation uses …"; "The full catalogue needs 50 paths per material".
- Closing: the section ends on its table. → add "The release paths and the two-level ensemble are the inputs on which the delayed-release and low-energy-excess estimates of \cref{sec:19.6} stand or fall."
- *Calibration.* l.3 opening. Yes (a vivid physical picture). l.23 "The reorganization energy E_reorg decides the regime." Yes.

**E.23 — REVISE**
- l.3 "gives $64\pm8$~eV" and l.7/66 "50~eV" → bare units → `\SI{64 \pm 8}{eV}`, `\SI{50}{eV}`.
- l.19 → see the redundancy item: point to E.11's protocol and state only what differs.
- → l.27 "and \cref{sec:19.2} lists their prediction as an open calculation" → "and no calculation yet predicts them (\cref{sec:19.2})".
- l.49 "The result enters \cref{sec:19.1} as …, and the kinetics of \cref{app:E.25}." → the verb is missing → "…, and it enters the kinetics of \cref{app:E.25}."
- *Calibration.* l.9, the Massey estimate in numbers. Yes, this is REGISTER 3.1 exactly. l.21 "The difference is large." Yes.

**E.24 — REVISE**
- l.13 "The grid is converged when four changes pass." → five tests follow, plus two closure tests → "The grid is converged when the bin, the energy cap, the matching point, the fit window and the k mesh each pass:".
- l.15 "The pitfalls of \cref{app:E.13} apply, with three more." → four follow → "with four more", or merge the residue item into E.13's.
- l.19 "which shows that they lie outside the range" → the referent of "which" is unclear (#13) → "and \cref{sec:18.4} shows that they lie outside …".
- l.21 "No first-principles Fano factor of any of these materials exists, so the first one will be new." → tautology → delete. "replacing the estimates that the guide of \cref{sec:21.7} must otherwise flag" → "replacing the estimates of \cref{sec:18.4}".
- l.25 "raises ε_eh by 0.084×1.3 = 0.11 eV" → the factor 1.3 is undefined here (ΔA_AB?). This goes to the reader review; for prose, name it: "by 0.084 ΔA_AB with ΔA_AB = 1.3 eV".
- *Calibration.* l.78 "The silicon cascade comes first, because it is the only one with a measurement at the precision that tests a Fano factor". Yes. l.7, the temperature sentence "Temperature enters three times:". Yes.

**E.25 — REVISE**
- l.17 "a field jump $en_s/(\varepsilon_0\varepsilon_0^{\mathrm{SI}})$ … ($\varepsilon_0 = 11.7$)" → ε₀ is used for both the static dielectric constant (as in E.17) and the vacuum permittivity → NOTATION clash; write the jump in the book's units with one symbol and say the static constant is 11.7. This goes to the notation fixer.
- l.81 table "$U_{\mathrm{el}}$ to 5%" vs text $U_{\mathrm{rel}}$ → mismatch → $U_{\mathrm{rel}}$.
- l.43 "the film validation of the last subsection" → ordinal and ambiguous (#13); that subsection comes later → `\cref{…}` to a label on §Validation of the film cascade.
- l.67 → #19 → see Length (c). "as in the thin-film calculations of Ref.~\cite{guruswamy…}" → #20 → give the expected yields at 3, 5, 10 and 40Δ, or the trend in a clause.
- l.92 "What these runs would settle is concrete." → abstract frame (#18) → "The kernels turn the conditional verdicts of \cref{sec:20.5} into numbers for two real detectors; …" (start with the content).
- *Calibration.* l.25 "The test can fail but cannot prove". Yes. l.3 "What is still missing are the event-level numbers on which the readout verdicts … are conditional." No. Rewrite: "What the chapters cannot yet supply are the numbers for one stated detector, and the verdicts of \cref{sec:20.5} wait on them."

**E.26 — REVISE**
- l.1 title "Coherent fields, fermionic absorption and two insertions" (lint TITLE) → once the Fano map has moved to E.14: "Coherent and second-order absorption". If it stays: "Coherent, fermionic and pair absorption".
- l.3 "of the earlier specifications" → meta → "of \crefrange{app:E.14}{app:E.16}". "The last item of this section belongs to the phonon-assisted sector" → move §Fano widths to E.14 (Length, E.14).
- l.9 "The effective electric field at the nucleus that converts … into an energy shift, comes from" → stray comma → delete it. "|2δ_rel| ≈ 0.01 to 0.02 for copper by typical shifts (an estimate)" → stacked hedge (#4) → "≈ 0.01–0.02 for copper (estimated from typical scalar-relativistic shifts)".
- l.21 `\cite[Eqs.~(3), (5)--(8)]{bauer2026dark}` carries the pair tensor (#20) → state the vector-coupling tensor in one display. "The local density must be rescaled to the book's 0.3" → #19/#20 → "The source uses ρ_χ = …; the rate scales as ρ_χ², so its curves move by …"
- l.3 $t_{\mathrm{coh}} = 2\pi/(m_\phi v_0^2)$ → v₀ is not defined in the section and not in NOTATION → "with v₀ the circular velocity of the standard halo".
- l.27 "a Fröhlich LO width of about 3 meV at 0.3 eV … and 20 to 60 meV once Γ–L scattering opens near 0.3 eV" → the two "0.3 eV" clauses collide → "about 3 meV just below the Γ–L onset at 0.3 eV, and 20 to 60 meV above it".
- → l.31 "mid-gap and 3 eV above the conduction minimum respectively, never copied from a template: wrong values give wrong bands without an error message" → "the Fermi level at mid-gap and the frozen window to 3 eV above the conduction minimum, both taken from the ground-state run". Drop the template clause.
- Closing → add "The map fixes the (q, ω) region in which \cref{sec:13.6} quotes the Fano term for GaAs."
- *Calibration.* l.3 opener. Yes. l.7 "The first decision is the regime, and it is made before any material calculation." Yes.

**E.27 — REVISE** (light)
- l.1 title "Halo, backgrounds and figure-of-merit inputs" → "figure-of-merit" is vague → "Halo, background and nuclear-spin inputs".
- l.15 "a GPU job of 10 to 100 GPU-hours" → "10 to 100 GPU-hours".
- l.21 "and saturation 11" → elliptical → "and saturation gives 11".
- l.34 → #20 → give ⟨S_p⟩ and ⟨S_n⟩ for ²⁹Si and ⁷³Ge in two lines.
- l.36 "lose their dependence on the standard halo where they choose to" → awkward → "can be quoted without the standard halo".
- *Calibration.* l.3 "And a spin-dependent coupling to unpolarized nuclei produces no coherent phonon at all." Yes. l.34 "Two pitfalls give zero for the wrong reason." Yes.

## Editor-notes items in this range

American spelling: open (E.22, E.16, E.17), see chapter-wide 11. Rates as `\varGamma`: clean. The zone Γ is upright, with markup inconsistent (chapter-wide 6). 𝔗 is inline and the appE opening states its components, per the ruling. The remaining editor notes concern E.1–E.13 and are not in scope.
