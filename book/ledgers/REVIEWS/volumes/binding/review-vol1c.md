# Binding round, independent review: block vol1c (App. A, B prose, C, D)

Base 60cc72c. Files: tex/appA/*.tex, tex/appB/appB.tex, B-2.tex, B-3.tex, tex/appC/*.tex, tex/appD/*.tex. B-1*.tex not touched (generated). The diff was read sentence by sentence (sentence-level diff of every changed paragraph, each read in its paragraph) before the editors' logs were opened. The logs were used afterwards only to check the stated interpretations and the open items.

## Verdict table

| Block | Changed sentence groups checked | Accepted | Fixed | Reverted |
|---|---|---|---|---|
| App. A | 58 | 55 | 3 | 0 |
| App. B (appB.tex, B-2) | 3 | 2 | 1 | 0 |
| App. C | 189 | 186 | 3 | 0 |
| App. D | 295 | 289 | 6 | 0 |
| **Total** | **545** | **532** | **13** | **0** |

A "sentence group" is one old/new pair from the sentence-level diff (a split counts once). Most of the editors' changes are correct and keep the physics; the interpretations I checked against the physics all hold. These include A-6:70 (the first-moment sum rule fixes the mean energy of the whole scattering weight, not of the elastic share), D-23:46 (the clause "differs from −α/ε₀r" belongs to the donor potential, not to δU), D-28:97 (the zeroth Fan–Migdal moment is the squared norm of H_ep|nk⟩) and A-8:13 (see the open items). Where the editors erred, the error was mostly over-construction: a split that left a sentence opening on a pointer, a new demonstrative noun ("this procedure", "this causal form"), or a repaired sentence that then read two ways.

## Fixes to the editors' sentences (Job 1)

| file:line | editor text | my text | reason |
|---|---|---|---|
| A-4:18 | "…where \|ĩ⟩ and \|f̃⟩ are the time-reversed states. They have the same energies as the original states, and the sum over them runs over the same states as the original sum, so S(q,ω)=S(−q,ω)." | "…where \|ĩ⟩ and \|f̃⟩ are the time-reversed states, which have the same energies as the original states. The sum over the time-reversed states runs over the same set of states as the original sum, so…" | the split created a sentence that opens on *They*; *them* had two candidates |
| A-5:10 | "Ref. [Eq. (29)] uses both normalizations." | "Ref. [Eq. (29)] uses the normalizations of \cref{eq:A.5-bloch}." | "uses both" reads as "uses each of two, alternately"; the base claim was "this is the convention of" |
| A-8:25 | "This procedure gives the daily modulation of Sect. 1.2." | "Keeping the full kernel gives the daily modulation of Sect. 1.2." | *this procedure* is a new name for a proposition |
| B-2:64 | "A formula taken from a paper must be converted to these four conventions before it is combined with the formulas of this book." | "Before a formula taken from a paper is combined with the formulas of this book, it must be converted to the book's choice of these four conventions." | a formula is converted to the book's *choice* of a convention, not to "a convention" |
| C-1:101 | "…and App. C.5 the analyticity that this causal form implies." | "…and App. C.5 the analyticity that \cref{eq:C.1-causal} implies." | *this causal form*: a new name with no antecedent noun |
| C-9:67 | "Because absorption has no static limit, Sect. 1.4 treats scattering and absorption separately." | "\Cref{sec:1.4} therefore treats scattering and absorption separately." | repeated the paragraph's first sentence word for word (over-repair) |
| C-12:3 | "Sect. 21.2 needs a limit that should hold for every velocity distribution, and that limit is then the largest value of a linear quantity…" | "Sect. 21.2 needs a limit that should hold for every velocity distribution. Because every rate is linear, this limit is the largest value of a linear quantity…" | *then* no longer had a condition to refer to (in the base it followed from linearity) |
| D-11:97 | "In the Hartree diagram the interaction line carries k=0 into a closed loop, and the Hartree diagram is (…) = v_C(0)N_e/V by …, the electrostatic potential…, and it is absent in jellium…" | split after "closed loop."; "The Hartree diagram is (…)…, and it is absent in jellium…" | three coordinated clauses with a long display in the middle |
| D-13:41 | "The first-order relative correction is m_e/M … and it comes entirely from the off-diagonal coupling at second order" | "The leading relative correction is m_e/M …" | "first-order … at second order" in one sentence reads as a contradiction; "leading" is what the base meant |
| D-16:11 | "…returns with g_nm(k+Q,−Q) B_{−Q}, whose vertex is g_mn(k,Q)* by eq:A.6-herm." | "…returns with g_nm(k+Q,−Q) B_{−Q}; by eq:A.6-herm, the return vertex g_nm(k+Q,−Q) equals g_mn(k,Q)*." | *whose vertex* names the vertex of a vertex |
| D-21:42 | "…induces, δH = (…). $\delta H$ is the mean-field term of H_int at wavevector q, and the quasiparticles respond…" | "…induces, δH = (…), which is the mean-field term of H_int at wavevector q. The quasiparticles respond…" | a sentence that opens on a symbol; the "and" joined two claims of different kinds |
| D-26:108 | "…= −(e²q²/3m_e)[…], and the two terms cancel at order q², as they must." | "…and the terms of order q² of m_e M³_ee and Σ_κ M_κ M³_eκ cancel, as they must." | *the two terms* reads as the two terms of the bracket just written; the intended pair is the one named in the previous paragraph |
| D-28:97 | "The squared norm is −π⁻¹∫dω Im Σ^FM…" | "This squared norm is −π⁻¹∫dω Im Σ^FM…" | "the squared norm" occurs twice in the paragraph for two different states; the demonstrative binds it to the nearest |

Accepted with comment (no change): A-5:48 "is gauge independent only under a condition:" (stiff but faithful); A-6:31 "this polarization vector satisfies" (the repeated noun is heavy, but *which* in the base had two candidates); C-3:83 "even though T_d lacks inversion" (repeats the previous sentence, but replaces "all the same"); D-3:42 "Define … for Re s > 0 it lies in the upper half plane. Then" ("Re s > 0" is stated two sentences earlier, so nothing is added); D-11:43 (the new sentence repeats the definition rather than pointing to it; acceptable).

## Recall (Job 2)

Sampled unchanged paragraphs: about 1 in 8 of the unchanged paragraphs of every file, spread evenly (66 paragraphs). On top of that came every ranker-flagged pronoun or definite sentence in unchanged paragraphs of all of App. A and of the files the ranker flags most densely (C-3, C-15, C-17, D-13, D-21, D-27).

| Appendix | Words sampled | Misses | Per 1000 words |
|---|---|---|---|
| App. A | 951 | 0 | 0.0 |
| App. B | 31 | 0 | 0.0 |
| App. C | 2861 | 5 | 1.7 |
| App. D | 1865 | 1 | 0.5 |
| **Total** | **5708** | **6** | **1.1** |

No appendix exceeds 2 per 1000 words, so none needs a second pass. App. C is the closest to the limit.

Misses fixed:

| file:line | text | fix | failure |
|---|---|---|---|
| C-13:3 | "The mathematics is that of an interval order, …, and of the heights of its elements." | "The construction uses an interval order, a partial order built from intervals, and the heights of its elements." | *that of* with no coordinated antecedent |
| C-17:15 | "GaAs has 4̄3m (T_d), that of the regular tetrahedron." | "…, the full symmetry of the regular tetrahedron." | *that of* pointing to a noun of the previous sentence |
| C-17:78 | "…commutes with the Hamiltonian, so the states can be chosen as its eigenstates." | "…as eigenstates of $g$." | *its*: nearest candidate is the Hamiltonian; intended g |
| C-19:14 | "a pattern of magnetic poles whose demagnetizing field cancels it exactly" | "…cancels the magnetization exactly" | *it*: pattern or magnetization |
| C-20:7 | "Their energies differ by the asymmetry Δ_as" | "The energies of the two configurations differ by the asymmetry Δ_as" | *Their*: Pauli matrices (nearest) or configurations |
| D-27:36 | "the response is bilinear in its two rows" | "the response of $n_e$ is bilinear in its two rows, $-n_Z$ and $\sum_\kappa Z_\kappa n_\kappa$" | *its*: the response or the electron density; "its two rows" not named |

## Open items (OPEN.md, this block)

- **A-8:13 "one or the other" → "the annual mean of |v_E(t)| or |v_⊙|".** Confirmed. The previous sentence compares exactly these two scalars. The other candidate pair (the time-dependent v_E(t) versus a fixed speed) is a function against a number, and papers do not quote a function as "v_E". Kept.
- **C-4:76 "keeps the delta limit of eq:C.4-SP at its value at x₀".** Stays. By the subject rule *its* binds to "a width that depends on energy", and that is the grammatical parse. The δ term carries no Γ, so the two readings (the width evaluated at x₀; the limit unchanged) state the same thing. Rewording would commit to one reading and could drop the "at x₀" qualifier.
- **C-12:61 "the resulting leakage" versus Sect. 21.2 "leakage".** No clash; stays. In Sect. 21.2 (s21-2:99–116, eq:21.2-fsleak) "leakage" is the weight misassigned between bins because a truncated kernel is negative. That is exactly the consequence of a negative k_i that C-12:61 describes, so the two uses name one object.
- **D-24:97 "This is the order-v² term" (antecedent a formula fragment).** Fixed: "The element $(1/8m_e^2)(-K^2)$ is the order-$v^2$ term of the scalar bilinear in eq:D.24-S-V0, and with H = −L it gives eq:8.1-scalar." The sign and size match D-24:33, where the scalar "loses K²/8m²". No new symbol was introduced: the expression is copied from the preceding sentence.
- **App. B generator (six proposed wordings, appA-appB.md).** Verdicts follow.

| Location | Proposed | Verdict |
|---|---|---|
| B-1 intro (all volumes): "…the last column gives that section." | "Each symbol is listed once, under the chapter or appendix of its first use; the last column gives the section of its first use." | **Accept.** |
| B-1-volN intro: "a symbol first used in another volume is listed there" | "…is listed in the list of symbols of that volume" | **Accept with change.** "Listed in the list" is clumsy; use "…is listed in the notation appendix of that volume". |
| ϑ_X cell: "ϑ_X that of the many-body approximation" | "ϑ_X the nuisance parameter of the many-body approximation" | **Accept.** It matches the head "Nuisance parameter of truncation k". |
| δ_X cell: "δ_X that of the many-body approximation" | "δ_X the fractional size for the many-body approximation" | **Accept with change.** The head has three nouns (difference, fractional size, template), and δ_X pairs with δ_k, which is both the fractional size and the template. Use "δ_X the fractional size for the many-body approximation, the template of ϑ_X", which keeps both roles. |
| n_2D cell: "Areal density; that of the heavy band" | "Areal density; areal density of the heavy band" | **Accept with change.** Use "heavy-band areal density", parallel to the neighbouring "heavy-carrier density" and "heavy Fermi velocity" in the same cell. |
| z_qp cell: "z_qp(n,k) that of the one-electron state nk" | "z_qp(n,k) the residue of the one-electron state nk" | **Accept.** |

## Proposed errata

None. No change in this block, and no unchanged sentence I read, misstates a quantity.

## Checks

- `python3 tools/invariant.py 60cc72c` on all block files: 0 STOP (notes only). One STOP from my first A-4 fix (a new `|f\rangle`) was removed by rewording.
- Lint on every file I changed: no hits from my edits. The remaining LONG-SENT and EQ-PUNCT hits are present at the base or are merges of displayed equations; D-28 "Consider any two definitions…" is long, but it is the editor's sentence and parses in one pass.
- `tools/chapcheck.sh appA|appC|appD /tmp/binding-review-vol1c-<app>`: exit 0 for all three, 0 undefined references and 0 multiply defined labels. appA has 2 overfull hboxes > 5pt, which the editor's log records as also present at the base (A-6 l. 22, A-7 l. 64). appD has 2, at D-3 ll. 46–48 and D-11 ll. 50–51; neither paragraph was touched in this review.
