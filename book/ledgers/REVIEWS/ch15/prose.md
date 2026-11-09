# Ch. 15 prose review (isolated): style, register, arrangement

Scope: tex/ch15/ch15.tex, s15-1 … s15-4, s15-summary; tex/appD/D-39.tex, D-40.tex. Checked against STYLE.md, style-guide.md, prose-review.md (patterns 0–26), REGISTER.md and editor-notes.md. Line numbers are those of each file. The tex was not edited.

## Verdicts

| Unit | Verdict | Main reason |
|---|---|---|
| Chapter opening (ch15.tex) | REVISE | ends in three orienting sentences (a section outline); one ~400-word paragraph |
| 15.1 Pair breaking by dark matter | REVISE | pre-empts 15.2's edge results; ~900 words of algebra in the main text; unresolved 9.4/9.2 and italic v_F; the term "kinematic edge" is used before it is defined |
| 15.2 Closed forms at the pair-breaking edge | REVISE | disorder subsection uses 15.3's definitions before they appear; undefined "masked cells"; a process-artifact caption sentence; looped restatement in the last three paragraphs |
| 15.3 Films and disorder | REVISE | gives the same edge numbers as 15.2 in a different normalization (a mismatch in WE 15-film); f_L derived a second time; the branch-cut subsection mostly repeats earlier material |
| 15.4 Absorption in superconductors and metals | REVISE | last subsection title does not cover its content; "as cited by … Ref. [29]"; a new large claim stated without its conditions; a derivation gestured at ("would") |
| Summary | PASS (minor) | "density matrix" is ambiguous; table labels "scattering" and "named, open" |
| App. D.39 | PASS (minor) | symbol reuse (T, h, g); conserving subsection duplicates 15.2.2; second quadrature recipe |
| App. D.40 | PASS | appendix roadmap opening is acceptable; two long sentences |

## 1. Lint (lint.py with BANNED-TERMS.txt)

0 blocking hits in every file. Banned terms: none.
- EQ-PUNCT: s15-1 l.59, 90, 118; s15-4 l.22, 61; D-40 l.15. **All false positives**: the comma or full stop is present on the last line of a `gathered`/`aligned` block. No action.
- LONG-SENT (>45 words): s15-1 1 (caption of lim:15.1a); s15-2 4 (two are captions, one is the table caption, one is the sentence opening 15.2.4, l.100); s15-3 1 (caption of tab:15-disorder); s15-4 13; summary 4 (two in table cells); D-39 2; D-40 8. The prose sentences worth splitting are listed under each section below. s15-4 has three times the long-sentence count of any other section.

## 2. Chapter-wide findings

**C1. Number lists paired with lists of y (systemic; REGISTER §4 bans "respectively" pairings, and these are the same construction without the word).** E.g. s15-1 l.136 "0.868, 1.001, 1.072, 1.068 and 1.023 times … at y = 2.2, 2.5, 3, 5 and 10, where the bare bubble gives 0.323, 0.440, 0.565, 0.794 and 0.934"; also s15-1 l.101, 115, 130; s15-2 l.33, 63, 84; s15-3 l.102; summary l.3, 5. → Fix: wherever tab:15-edge already holds a list, quote at most two anchor values in prose ("0.87 at y = 2.2, rising to 1.07 by y = 3") and point to the table.

**C2. Register tics (per 10k words; Lin's rate in brackets).** "so" 29/43/20/28 in 15.1/15.2/15.3/15.4 [11]; "gives" 34/39/18/28 [7]; "only" 32/23/25/42 [11]; "therefore" 8/4/10/17 [3]. "however" is 0 and "typical(ly)" is 0 in the whole chapter [8; 15]. "we will/can/see/have" occurs once per section [≥12]. → Fix: in each section, turn half of the "gives" into "is"/"leads to" and half of the "so" into "since"/"because"; add a "however" at each real contrast. Candidates: s15-1 l.136 ("The first-order coefficient returns only at large momentum transfers" → "However, …"); s15-2 l.63; s15-3 l.90; s15-4 l.86.

**C3. Two different "edges" (clarity).** "Pair-breaking edge" means ω = 2Δ; "kinematic edge" means the line q = ω/v_max. 15.2's title and key result say "pair-breaking edge" but are about the kinematic edge. "Kinematic edge" is first used without definition at s15-1 l.7 and l.101 and is defined (\emph) only at s15-2 l.3. → Fix: define it at its first use in 15.1 ("the kinematic edge, the smallest momentum transfer q = ω/v_max that can deposit ω"). Retitle 15.2 "Screening at the kinematic edge" and rename its key result and lim:15.2a to match.

**C4. Same quantity, different printed values or symbols (one symbol, one value).**
- k_TF: 4.05 keV (s15-1 l.18, 162) vs 4.08 keV (s15-3 l.116).
- ω_p (free electrons): 15.78 eV (s15-4 l.18, fig caption l.91, summary table) vs 15.7 eV (s15-3 l.116).
- The clean-limit criterion: ℓ_e ≫ v_F/Δ = 7.3 μm (s15-1 l.150, summary table l.48); ℓ_e ≥ 10 μm (s15-2 l.84, 104); ℓ_e ≫ ξ_coh = 2.3 μm (s15-3 l.3, 19). State the criterion once, in 15.3.1, and refer to it.
- v_F is italic in 15.1 (70 instances) and upright everywhere else (editor note, unresolved).
- ε^bare (15.1) vs ε_BCS (lim:15.2a l.68) vs ε^BCS(q, z) for the full superconducting function (s15-3 l.131). Use ε^bare and ε^cons; editor note "L^BCS → L^bare/L^cons" is not yet done.
- ω_AB (s15-1 l.78, s15-3 l.135) clashes with the NOTATION entry for Alig–Bloom; f_L(ν) with ν = ω/qv_F clashes with the phonon branch ν (editor notes, unresolved).
- "percent" (all sections) vs "per cent" (s15-2 l.102). The book is American: use "percent". Words vs \SI: "forty percent" (s15-1 l.101, summary l.3) vs \SI{40}{\percent} elsewhere. Use \SI.

**C5. Standalone scrub / process language (pattern 19).**
- "masked", "cells" (s15-2 l.3, 95, 104; summary l.5, table l.23): "mask" occurs nowhere else in the book and is never defined. It is a campaign term. → Fix: define it in prose once ("we drop the energies y < 3.8 from the signal region of a rate calculation"), or say "excluded from the signal region", and drop "cell".
- tab:15-edge caption (s15-2 l.36): "The impurity columns are evaluated at v_max/v_F = 0.39, at which the clean column changes by at most 0.004." This is bookkeeping about how the data were generated. → Recompute at 0.397 and delete the sentence.
- s15-4 l.130: "the calculation specified in \cref{app:E.20} reports the result with and without it, so that their difference measures it." → "\Cref{app:E.20} computes the rate with and without this factor."
- summary table l.29: "named, open" → "size unknown".
- s15-2 l.78: "takes milliseconds per point" is a remark about the code; cut it.

**C6. "Specified in app:E.20" five times** (s15-1 l.80; s15-2 l.78; s15-3 l.147; s15-4 l.130, 132). Keep one pointer per section in the computational passage. 15.2's pointer repeats 15.1's: delete it.

## 3. Overlaps between 15.1, 15.2 and 15.3: one proposed home for each

**O1. Conserving algebra and edge values.** Today the same content appears in four places. The vertex fraction 𝔳 and the conserving edge ratios 0.868…1.023 with the bare 0.323…0.934 are in s15-1 l.101 and l.136. The general resummed form 𝔤(1+𝔯²)/[(1+δ)²+𝔤²𝔯²] with 𝔤 = 𝔤_I(1+𝔳) is in s15-2 l.57–63 and again in D-39 l.27. The y = 3 values (𝔳 = 0.202, 1+δ = 0.577) are in D-39 l.27 and WE 15-edge. There are two different quadrature recipes: Gauss–Legendre with clustered nodes at s15-1 l.101, and the substitution s* ∓ t² with adaptive quadrature at D-39 l.27. Gan's (Δ/qv_F)² estimate is assessed twice (s15-1 l.101 end; s15-2 l.65) and its coefficient 11–27 a third time (s15-2 l.100).
→ **Home:** eq:15.2-cons with tab:15-edge (15.2.2) for all edge values and for the assessment of Gan's estimate; D.39 for the algebra and the single quadrature recipe.
→ 15.1 keeps the definition of 𝔳, its maximum ("up to +0.40 at y = 2.2"), the non-monotonic q dependence and the large-q coefficient check (0.954/1.048/1.053). Cut the five-value lists at l.136 and the Gan sentence at the end of l.101. Replace the quadrature clause at l.101 by "(computed in \cref{app:D.39})".
→ D.39 "The conserving response": replace the restated definitions with "with 𝔤 and δ of \cref{eq:15.2-cons}". Keep the substitution and the y = 3 check.

**O2. Mean-free-path passages.** These are s15-1 l.150 (clause in the limit box) and l.155; s15-2 15.2.3 (l.82–84); s15-2 l.100, 102, 104 (factor 4.6, 300 nm, 6 %, 10 μm, each repeated); s15-3 l.104; WE 15-film l.122; WE 15-edge l.93. 15.2.3 uses ℓ_e, γ_rel, the Mermin function, "diffusive" and the 30 nm film "(\cref{sec:15.3})" before 15.3 defines any of them. This breaks the arrangement rule against forward references for definitions. The opener of 15.3 (l.3) then says that 15.1 and 15.2 "assume exactly" a clean crystal, which 15.2.3 has just contradicted.
→ **Home:** 15.3.3 "The superconducting film". Move s15-2 l.82–84 there, in place of s15-3 l.104, so that the Born-scattering conserving results lead into the local Mattis–Bardeen limit. Keep the impurity columns of tab:15-edge, but use **one normalization** in the table and in both texts. Recommended: L_s/L_n at the same scattering rate, since 𝔤_I has no meaning in the dirty limit. Today 15.2 says 0.87 → 0.60 → 0.19 (÷𝔤_I L^nor) and 15.3 says 1.30 → 0.90 → 0.28 (÷L_n) for the same points. s15-3 l.102 cites "1.30 … (\cref{sec:15.2})", a number 15.2 never prints. WE 15-film l.122 says "the 30 nm column of tab:15-edge has 1.26", but the column shows 1.091.
→ 15.2 keeps the relaxation-rate nuisance and the second reason for the mask as one sentence each, pointing to 15.3.3. 15.1 keeps the single clause at l.155.
→ Also: the impurity-dressed conserving response (s15-2 l.82, "impurity ladder in the bubble and in the pair channel together") is derived nowhere in the book and has no pointer to a derivation. User rule: nothing is left to the reader. Add a derivation pointer (an App. D section) or state the construction in full.

**O3. Anderson–Bogoliubov pole and the absence of loss weight below 2Δ.** s15-1 l.78; s15-2 l.65 (second half); s15-3 l.135 (first three sentences); D-39 l.29–33. → **Home:** the statement in 15.1 l.78, the proof in D.39. 15.2 keeps the pole positions (1.921/1.963/1.991 Δ) as the reason the ladder is large, plus one clause "(no weight below 2Δ, \cref{app:D.39})". Delete the repeat in 15.3.

**O4. f_L(ν) is defined twice:** eq:15.2-Lin (s15-2 l.9) and eq:15.3-fL (s15-3 l.43–49, with its derivation). → **Home:** 15.2, its first use. Move the one-line derivation from ν± there. 15.3 cites eq:15.2-Lin and adds only the continuation to the complex argument ν_γ.

**O5. Logarithm at y → 2.** s15-1 l.130–132 (numbers); s15-2 l.29 (last sentence); D-39 l.23 (derivation). → Keep 15.1 and D.39. In 15.2, keep only the asymptotic form (π/2)ln[1/(y−2)] with a pointer.

**O6. Small repeats.** The film-gap convention (s15-1 l.159 and s15-3 l.39): keep 15.1. The thermal-quasiparticle factor e^{−208} (s15-2 l.100, s15-3 l.135, s15-4 l.71): keep 15.2. "The condensate short-circuits a slow potential" (s15-2 l.84 and s15-3 l.102): keep 15.3.

**O7. Two limit checks plot nearly the same curves** (lim:15.1a and lim:15.2a, both on the kinematic edge against y, with bare, 𝔤_I L^nor and conserving). → Give them distinct jobs. 15.1a: the gap and the normal screening (Lindhard and 𝔤_I L^nor against the conserving result, edge and 4× edge). 15.2a: the screening resummation (bare direct, resummed with both prescriptions, first order). Drop the bare bubble from 15.1a or the 𝔤_I L^nor curve from 15.2a.

## 4. Seams between adjacent sections

- **Opening → 15.1:** both say "three forms of the loss function in current use" (ch15 l.2; s15-1 l.3). Name the three forms once, in 15.1, and cut the clause from the opening.
- **15.1 → 15.2:** 15.1 l.134–136 already gives 15.2's results: the expansion fails at y = 2.2 and the conserving edge values. 15.2's opener (l.3) then re-motivates them. After O1, 15.1 ends its screening discussion with "near the edge the expansion fails (\cref{sec:15.2})", and 15.2's opener carries the stakes.
- **15.2 → 15.3:** contradiction (O2). After the move, s15-3 l.3 can stand as written.
- **15.3 → 15.4:** 15.3 uses the Mattis–Bardeen conductivity "which \cref{sec:15.4} derives" (l.96), so the result comes before its tools. This is acceptable as a pointer, but write "derived in \cref{sec:15.4-MB} and \cref{app:D.40}". The jump from WSi to dark-photon absorption needs no bridge; the opener of 15.4 is concrete.
- **15.4 → Summary:** clean.

## 5. Section-by-section issues (location → problem → fix)

### Chapter opening (ch15.tex)
- l.2 → orienting tail of three sentences, a section outline ("We put … follow … and treat the edge, the films and the absorption of bosonic dark matter in turn. The quasiparticles … \cref{sec:20.4}. \Cref{fig:15-map} shows how the sections connect, and the chapter summary collects …"). STYLE allows at most one. → Keep "\Cref{fig:15-map} shows how the sections connect." Cut the rest, and move the pointer to Sect. 20.4 to 15.1 or to the summary.
- l.2 → the question is stated twice ("The question of this chapter is whether the closed form can be trusted: can the rate … be computed as reliably …?"). → "Whether the rate of breaking pairs can be computed as reliably as the semiconductor rates of \cref{chap:10} is the question of this chapter."
- l.2 → "each electron of a Cooper pair is bound by Δ_BCS" is loose physics. → "In aluminum the gap is Δ_BCS = 0.18 meV, so breaking a pair costs 0.36 meV, …"
- l.2 → one paragraph of ~400 words. → Break after "…the clean bulk crystals of the BCS model." (stakes; then what goes wrong).
- Pattern 25 (sentence by sentence): no periphrasis and no stacked negations. Map caption (l.7): stands alone; pass.

### 15.1
- l.7 (and l.101) → "kinematic edge" is used before it is defined (C3).
- l.33 → "The modulus of the last follows from …": an ordinal reference (pattern 13). → "The modulus of the mixed product follows from …". l.35 → "the sum of the first factor's terms is half of …" → "EE' + ξξ' + Δ² is half of …".
- l.22–76 → ~900 words of algebra (hyperbolic substitution, partial fractions, analytic continuation) in the main text. Style guide: long derivations go to Appendix D. Editor note "possible duplicate pair-function reduction in D.39": checked; D.39 does **not** repeat it, so there is no duplicate. → Move l.41 (from "Write ξ = Δ sinh a") through the continuation formulas to a D.39 subsection "The pair function F_μ". Keep eq:15.1-bubble, eq:15.1-ident, eq:15.1-F, eq:15.1-bubbles and the key result.
- l.76 → "numerically the ratio is one to 10^{−5}" → "they agree to one part in 10^5".
- l.80 → "is specified as a calculation in \cref{app:E.20}" → "\Cref{app:E.20} sets out the calculation on the full (q, ω) grid with impurity scattering; the clean limit needs only 𝒩_F, v_F and Δ_BCS."
- l.101 → "The ladder raises the absorption above the bare bubble by up to forty percent near the edge." This restates +0.40 from the sentence before (pattern 26). → Delete it, or merge as "…+0.40 at y = 2.2, the largest value, …".
- l.112 → the first sentence restates the caption. → Open with the content: "At q = 0.3 eV (v_F q = 11 Δ) every reachable energy lies within 4.4 Δ of zero, and …".
- l.134 → "The correction is of first order in Δ/qv_F, not second." restates the box heading. → "Being of first order, the correction is at most 2(v_max/v_F)𝔰_BCS(y)/y at the kinematic edge, …".
- l.140 → "At the kinematic edge … both are functions of y": "both" after three truncations is ambiguous. → "all three controlling parameters are functions of y".
- l.147 (caption lim:15.1a) → "The bare bubble reaches 10 % only at y ≥ 9.4" is unclear, and 15.2 and the editor note give 9.2. → "The bare bubble comes within 10 % of the conserving result only for y ≥ 9.2."
- l.153 → "The Lindhard function, which knows nothing of the gap": anthropomorphic (pattern 15). → "The Lindhard function, which has no gap,".
- l.171 → "doubling both grids leaves the printed digits unchanged" is a convergence assurance. It is acceptable in a worked example, but borderline pattern 19. Optional cut.
- Calibration (REGISTER §6.13). (a) Opener l.3: Lin could write it; yes. (b) l.101, "Its relative size is the vertex fraction … which follows from \cref{eq:15.1-Rcons} by Gauss–Legendre quadrature over μ, with the nodes concentrated where …": no; procedure in the main text. As Lin: "The ladder also changes the absorptive part, and near the edge it changes it a lot: at the kinematic edge it adds 40 percent at y = 2.2 and 20 percent at y = 3, but only 0.3 percent at y = 10." (c) l.35, the derivation narration: no. Fix by the move to D.39 above.

### 15.2
- Title → "Closed forms at the pair-breaking edge" names the method, and the wrong edge (C3). → "Screening at the kinematic edge".
- l.3 → "That momentum transfer is not a corner case.": negation withholding (pattern 25). → "Most scatters near threshold have that momentum transfer."
- l.3 → "This section gives it in closed form …": self-narration (pattern 22). → "We give it in closed form …". "The comparison fixes the nuisances and the masked cells …" (C5).
- l.33 → "the two numbers being the two prescriptions": an awkward pairing. → "0.33 (Kramers–Kronig integral to infinity) to 0.40 (cut at qv_F) at y = 2.2", then refer to the table for the rest (C1).
- l.63 → "The superconductor does not screen more weakly than the normal metal in the sense that matters for the rate": a stacked negation (pattern 25). → "The superconductor screens about as strongly as the normal metal: |ε^cons|/|ε_Lin| = 1.27, 1.06 and 0.99 …".
- l.68 → ε_BCS (C4).
- l.78 → the paragraph after the box adds almost nothing (pattern 26). "1.5 %" repeats l.31, "9.2" repeats the box, and "closer … at every y ≥ 2.25" repeats l.63. → Delete the paragraph, and put its one useful sentence ("below y = 9.2 a rate needs \cref{eq:15.2-cons} or 𝔤_I L^nor") into the box's closing sentence.
- l.82 → "\Cref{tab:15-edge} gives two columns, and the full set of mean free paths behaves as follows.": empty signposting (pattern 1). Moot after O2; otherwise cut.
- l.95 → "The cell y = 3 on the edge is controlled." (C5). → "At y = 3 the edge value is known to 6 percent."
- l.100 → long sentence (lint). Also "Three effects lie outside the model. Disorder is computed above. … And the film geometry …" is a count-teaser (pattern 18). → "Outside the model lie disorder (\cref{sec:15.3-sc}), the frequency dependence of the gap in strong coupling, small in aluminum (2Δ/T_c = 3.54 against 3.53) and not sized here, and the film geometry once 1/q, about a micrometer on the edge, exceeds the thickness."
- l.100 → "Its coefficient of 11 to 27 is why …" is the third statement of the coefficient (O1). Cut.
- l.102 → "per cent" (C4). Also "is not a template for it, because …" reads as an answer to a reviewer. → "The conserving value lies outside the spread of the two Kramers–Kronig prescriptions at every y of \cref{tab:15-edge}, so that spread cannot serve as the template."
- l.104 → repeats the factor 4.6, 300 nm, 6 % and 10 μm from l.84 and l.102 (pattern 26). → Keep the boundary 3.8 and its first reason; cite 15.3.3 for the second.
- Calibration. (a) WE 15-edge: yes, this is Lin's estimate-then-check style. (b) l.29, "The ratio δ_𝔰 is the shift of the real part relative to the normal real part, and 𝔯_ε measures how far …": symbol-by-symbol narration (REGISTER §4). As Lin: "Two things pull the loss function below 𝔤_I L^nor: the gap stiffens the real part of ε, and the same case-I factor that raises Im ε also raises |ε|." (c) l.100: no (see above).

### 15.3
- l.3 → seam contradiction (O2).
- l.39 → the film-gap repeat (O6). Cut "Thin aluminum films … (\cref{sec:1.5})."
- l.43–49 → f_L derived a second time (O4).
- l.63 → "The loss function does not care which of the two holds.": anthropomorphic (pattern 15). → "The loss function is the same in both regimes."
- l.88 → "Electrons in films matter for keV-mass dark matter, not for MeV-mass …" is vague. → "Collisions in a film change the loss function for keV-mass dark matter; at the momentum transfers of MeV-mass dark matter the film electrons are ballistic."
- l.90 → "the substitution that \cref{sec:4.5} showed to destroy electrons": figurative. → "…showed not to conserve electron number". Also, "A width added as ω → ω + iγ_rel, as in Ref. [Eq. (S.13)], is this substitution" implies QROCODILE used it; editor note says the implementation was inferred. → "If the width is added as ω → ω + iγ_rel, as in Ref. [Eq. (S.13)], it is this substitution."
- l.92 → "The width of a plasmon is not the rate γ_rel that enters here.": negation opener. → "The plasmon width and the relaxation rate are different numbers: …".
- l.96 → "In a dirty film the pair-breaking edge looks different from the clean edge": a gesture (pattern 0). → "In a dirty film the loss function starts from zero at 2Δ_BCS, with the case-II factor, where the clean edge of \cref{sec:15.2} jumps."
- l.102 → the paragraph first announces two reasons and then restates each. → Drop "Near the threshold the ratio is small because … and because …" and keep the two explanatory sentences. The last sentence cites a number 15.2 does not print (O2).
- l.104 → wrong normalization (O2).
- l.116 → k_TF = 4.08, ω_p = 15.7 (C4). l.122 → "the 30 nm column … has 1.26" while the table shows 1.091 (O2).
- l.127 → "needs four measured properties", but five are named (resistivity, gap, thickness, dielectric constants of the neighbors, k_F ℓ_e), and k_F ℓ_e follows from the resistivity. The paragraph also sits mid-section although the opener promised it as the close. → Drop the count, and move the paragraph to the end of 15.3 after the WSi subsection.
- 15.3.5 l.131–135 → general background (analyticity, KK, oddness under inversion) that repeats Ch. 4. Para 3 repeats O3 and O6. l.133: "the retarded branch, the retarded rather than the time-ordered bubble, and a relaxation that keeps the response analytic, conserving and dissipative … Third, a relaxation rate must enter through a construction that keeps the response analytic, conserving and dissipative" (a triad repeated verbatim). → Reduce to one paragraph of three concrete warnings: the logarithm branch (seven orders of magnitude), the time-ordered bubble at ω < 0 and T > 0, and the local-field factor that makes L negative. Fold it into 15.3.2 and drop the subsection.
- l.145 → "Electrons that diffuse slowly also repel each other more strongly …, an effect absent from BCS theory": the field's term is missing and there is no citation (editor note). → Name it: the Altshuler–Aronov enhancement of the Coulomb repulsion in diffusive metals and its suppression of T_c (Finkel'stein), with a credit citation. The last sentence repeats q ℓ_e ≈ 10^{−4} and ℓ_e/ξ ≈ 0.02 from the same paragraph and the table (pattern 26). Cut it.
- l.147 → "…are open; mean-field BCS theory cannot supply them, and that calculation can." This is over-confident about a calculation not yet done (pattern 14). → "…are open; the calculation of \cref{app:E.20} is designed to supply them."
- Calibration. (a) l.79, the Landau damping and Joule heat picture: yes, this is the best register in the chapter. (b) l.19, the three-ratio paragraph: yes. (c) l.133: no. As Lin: "Of course, a causal response is not enough: the Lindhard function at ω + iγ is causal and still loses electrons, and taking the wrong branch of its logarithm costs seven orders of magnitude in the aluminum rate."

### 15.4
- l.3 → "the two processes carry opposite ones" is vague (case I and case II are not opposites). → "the phonon-assisted process carries the case-I factor and the impurity-assisted one the case-II factor". "turns out to break pairs" uses the crutch "turns out" (REGISTER §4). The opener also states a new, unverified, large claim (editor TOP PRIORITY) without its conditions (pattern 14, under-qualification). → "In a clean singlet superconductor without spin–orbit coupling, the spin current, which absorbs the axion-like particle, breaks pairs without a third body." The same applies at summary l.9 and l.11.
- l.20 → a 60-word sentence (lint). → Split after "(α, ᾱ)": "Its pair-creation amplitude then carries u_α v_β − v_α u_β, the case-II factor of …, which vanishes …".
- l.34 → "A detector that wants only the intrinsic absorption": anthropomorphic. → "Intrinsic absorption dominates only in a pure sample, as …".
- l.71 → "is the result of Allen as cited by Hochberg, Lin and Zurek [Eq. (17) and Ref. [29]]". Sending the reader to a source's reference list is pattern 20, and "as cited by" is second-hand credit. → "is due to Allen~\cite{allen1971electron} and is used by Hochberg, Lin and Zurek~\cite[Eq.~(17)]{hochberg2016absorption}". "Two of those hypotheses have sizes." → "Two of those hypotheses can be sized."
- l.86 → long sentence (lint), "The phonon-assisted conductivity … grows as ω³ … while …". Split at "while".
- l.102 → "the rate reaches 90 % of the normal-metal value at 11.4 Δ" repeats the box and caption (pattern 26). Cut from the worked example.
- l.114 → "The physical picture is simple." is filler (pattern 0). Delete it; the picture follows.
- l.124 → long sentence: split at "and since".
- l.126 → "The numbers are large." is an evaluation without a referent. → Open with the number: "At 1 meV \cref{eq:15.4-sJ} gives σ₁^𝒥 = 3.30×10⁴ eV, 6×10⁶ times …". Also split the long ALP sentence at the semicolon.
- 15.4.4 title "Strong-coupling corrections" covers only paragraph 1. Paragraph 2 is the first-principles transport function and its umklapp failure, and paragraph 3 is scalar absorption. → Retitle "Strong coupling and the transport function" and move the scalar paragraph to the end of 15.4.3, or give it a run-in heading.
- l.130 → "A full derivation would write the conductivity with Eliashberg Green's functions … At one-phonon order no renormalization factor appears": the result is asserted after a derivation that is only gestured at. User rule: nothing is left to the reader. → Either write the one-phonon step (App. D.40) or state it as an open assumption. Also C5.
- Calibration. (a) l.48, "Phonon-assisted absorption has the coherence factor of the density, impurity-assisted absorption that of the current: the third body decides.": yes. (b) l.114, the pair-pulling picture: yes. (c) l.38, "That is two hundred times the 0.15 eV …, and 58 times less than k_F …, so only long-wavelength acoustic phonons take part near the edge": acceptable; Lin would hedge "∼ 30–60 eV". Keep.

### Summary
- l.9 → "is the density matrix in Nambu space": ambiguous, since "density matrix" means ρ. → "has the Nambu matrix η of the density".
- l.3–11 → C1 lists. The summary is the sanctioned recap, so this is acceptable, but trim the five-value lists to anchors.
- Table l.29 → "Energy dependence of the gap (strong coupling), scattering": the trailing "scattering" is cryptic. → "… in scattering". "named, open" → "size unknown" (C5).
- tab:15-inputs l.48 → the clean criterion 7.3 μm vs 15.3 (C4).
- Captions of both tables stand alone. Pass.

### App. D.39
- l.1 → the long title "The resummed BCS loss function" → "…of the bare quasiparticle bubble" (C4).
- l.23 → T = 10^4 for an integration cutoff collides with the temperature T. l.19 h(y') and l.29 h(ω) are two meanings of h in one appendix, and g = h − … collides with 𝔤 and g_ν. → Rename to y_c, h₁/h₂, g̃.
- l.27 → duplicates 15.2.2, and its quadrature recipe differs from s15-1 l.101 (O1).

### App. D.40
- l.3 → the roadmap sentence is acceptable in an appendix. l.93 → "The paired state is built from …" duplicates s15-4 l.20 almost word for word. Shorten the main-text version to the result and the pointer.

## 6. Pattern 25 sweep (chapter opening, section openers, subsection openers, captions)
Flagged above: s15-2 l.3 "not a corner case"; s15-2 l.63 "does not screen more weakly"; s15-3 l.92 "is not the rate"; s15-3 l.96 "looks different"; s15-3 l.145 "out of reach of mean-field BCS" (acceptable, but "lies outside" is plainer); s15-4 l.114 "simple"; s15-4 l.126 "large". No figurative stand-ins ("pull", "silence", "fingerprint") anywhere. All eight captions are clean.

## 7. Pattern 26 (looped restatement): paragraphs whose new-fact list is empty or a subset of earlier ones
s15-2 l.78 (empty: delete); s15-2 l.104 (mostly a subset of l.84 and l.102); s15-3 l.104 (subset of s15-2 l.84 in other units); s15-3 l.135 (subset of 15.1, 15.2 and D.39); s15-3 l.145 last sentence; s15-1 l.101 one sentence; s15-4 l.102 last sentence. Subsection endings: 15.1.2 (l.80) and 15.2.2 (l.78) end on pointers or recaps, not facts. The rest end on a new fact.

## 8. Rules checked and found clean
No exercises, checkpoints or tasks for the reader. No "you", no "I", no contractions. All cross-references use \cref, with no hard-coded numbers. Citations use \cite[Eq.~(n)] with locators, except two "[supplement]" locators (s15-3 l.90, 113; acceptable). No "see Ref. X for". Limit Check boxes are self-contained comparison plots with one sentence on the breakdown, and no Source/Chain list. Titles are noun phrases, apart from the two flagged (15.2, 15.4.4). There are no em dashes, and no "thereby", "whereby", "in order to", "i.e." or "e.g.".

## 9. Editor-notes items that concern prose: status
- 15.1 "9.4 → 9.2": **open** (lim:15.1a caption, l.147).
- ω_AB rename; v_F upright; the clash of f_L(ν) with ν; L^BCS → L^bare/L^cons: **open** (C4).
- 15.2 caption "0.39, not 0.397": **open**, now flagged as a process artifact (C5).
- 15.3 "decide whether to merge the two mean-free-path passages": **decided here**, home 15.3.3 (O2).
- ω_p 15.78 vs 15.7, k_TF 4.05 vs 4.08: **open** (C4).
- "Possible duplicate pair-function reduction in D.39 vs 15.1": **checked, no duplicate**; the real duplicate is the conserving-response subsection and its quadrature recipe (O1).
- The QROCODILE width implementation was inferred, and the WSi interaction-disorder statement has no citation: prose fixes are given at s15-3 l.90 and l.145.
- 15.4 spin-current claim unverified: the prose under-qualifies it (s15-4 l.3; summary l.9, l.11). The physics verification is outside this review.
