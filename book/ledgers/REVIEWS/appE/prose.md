# Appendix E prose review (E.1–E.13, isolated)

Read against STYLE.md, style-guide.md, prose-review.md (patterns #1–20) and REGISTER.md. Line numbers are those of each `tex/appE/E-N.tex`. No tex edited.
**Verdict rule.** PASS means at most 3 minor hits per 1,000 words and no systemic pattern. REVISE means the voice is sound but there are systemic patterns or more hits than that. REWRITE means systemic voice failure. The sections run 2,189–4,215 words.

## Verdicts

| Sect. | Words | Verdict | Main reasons |
|---|---|---|---|
| E.1 DFT in practice | 4119 | REVISE | outline opener, a doubled phrase, the verbatim block restates its lead sentence, Pitfalls restate |
| E.2 Pseudopotentials | 3369 | REVISE | triad outline opener, imperative recipe (l.104), vague quantifiers, Pitfalls restate |
| E.3 Quasiparticle corrections | 3265 | REVISE | reuses the E.1 hook, recap opener, a restating sentence, Pitfalls entirely restate |
| E.4 DFPT in practice | 4215 | REVISE | outline opener, imperatives, count-teasers, two adjacent sentences say the same thing |
| E.5 Wannier functions | 3492 | REVISE | six-item enumerate, abstract opener, imperatives, Pitfalls restate |
| E.6 Dielectric response | 2939 | REVISE | abstract opener, count-teasers, false contrast, undefined N, Pitfalls restate |
| E.7 Crystal form factors | 3775 | REVISE | title, four-"how" opener, PAW/velocity/scissor re-derived from E.2/E.3, backward seam |
| E.8 Anharmonic, finite T | 3328 | REVISE | five-item outline opener, misplaced Pitfalls, detector tic, backward close |
| E.9 Magnetic, superconducting | 2363 | REVISE | British spelling, a citation carries content (#20) twice, "gives" 47/10k |
| E.10 Defects | 2189 | REVISE | outline opener, the displacement-threshold protocol duplicates E.11 with conflicting numbers, #20 |
| E.11 MD and learned potentials | 3614 | REVISE | uncaptioned table, upright Γ, rhetorical question, unclear splice rule, ordinal miscount |
| E.12 Transport Monte Carlo | 2959 | REVISE | upright Γ, #20 twice, imperative, \cite\cite, Pitfalls restate |
| E.13 Hot-carrier cascades | 2726 | REVISE | upright Γ, undefined χ, z_qp unsourced, ambiguous factor, garbled pitfall |

No section needs REWRITE. The four writers share one register: plain, numerical and in the field's terms. Most fixes are sentence-level, plus the systemic items below.

## Lint (step 1)

| File | Hits | Notes |
|---|---|---|
| E.1–E.13 | LONG-SENT 3/2/1/7/3/8/8/12/10/10/6/7/4 | About 70% are artifacts: tables, verbatim and equations counted as one sentence. The real ones are listed per section below (E.8 l.3, E.10 l.3, E.4 l.3, E.7 l.3). |
| E.4:98, E.9:12, E.9:58, E.10:61, E.13:45 | EQ-PUNCT | False positives: in each case the display runs into the following clause ("to the energy functional", "in the convention…", "for 64, 216…", "where…"). No change. |
| E.7:1 | TITLE | Real; see E.7. |
| all | 0 blocking | — |

## Systemic findings (each stated once; per-section tables do not repeat them)

| # | Pattern | Where | Fix |
|---|---|---|---|
| S1 | **Pitfalls subsections restate their own section** (#5). Nearly every sentence repeats an earlier paragraph. | E.1 l.155–163; E.2 l.108; E.3 l.92 (entirely); E.4 l.169; E.5 l.94; E.6 l.90; E.7 l.127; E.8 l.91; E.11 l.112; E.12 l.99; E.13 l.85 | Cut each to the items that appear nowhere earlier (E.1: smearing hides a metal; E.4: Voigt row order; E.8: Q=−Q modes split degeneracies; E.12: Debye-frequency start; E.13: "two models … not independent support"). Keep the closing pointer sentence. The cross-cutting lessons go to the proposed summary. |
| S2 | **Outline openers** (#18; STYLE "concrete openings"): a colon followed by a list of the section's subsections. | E.1 l.3; E.2 l.3; E.4 l.3; E.5 l.3; E.6 l.3; E.7 l.3; E.8 l.3; E.9 l.3; E.10 l.3; E.11 l.3 (mild) | Keep the concrete first sentences (all good). Replace the list with one sentence that says what the reader will be able to compute or trust. Rewrites are in the section tables. |
| S3 | **Template phrase across writers**: "This section explains how such numbers are computed:" | E.8 l.3, E.9 l.3, E.10 l.3; variants in E.5 l.3 and E.7 l.3 ("This section is about…") | Covered by S2; vary the replacements. |
| S4 | **Hierarchy paragraph handled inconsistently**: some sections give it a heading, others fold it into another subsection. | Headed "Place in the expansion hierarchy" (E.4, E.11, E.12, E.13) or "Place on the hierarchy" (E.8, E.9, E.10); folded into "What is computed" or "Quantity and order" in E.1, E.3, E.5, E.6, E.7 | Use one heading everywhere, e.g. "Place on the hierarchy", or fold it in everywhere. |
| S5 | **Clause titles** (#16): "What is computed" (E.1, E.3, E.5, E.6, E.11, E.12, E.13), "What a pseudopotential replaces" (E.2), "What one linear-response run delivers" (E.4), "Quantity and order" (E.7, vague) | — | Use noun phrases: "Computed quantities", "The frozen core", "Outputs of a linear-response run", "The density vertex". |
| S6 | **Register: connectives and crutches** (REGISTER Sect. 4, per 10k words) | "however" is 0 in 10 of 13 sections (E.1 7, E.4 5; L 8.0). "we will/can/see/find" is 0–6 (L 12–14). "must" runs 13–46 (E.5 46, E.6 41, E.2 33): the recipe voice. "gives" is high in E.9 (47), E.8 (36), E.10 (32) and E.1 (32), against L 7. "so" is 24–33 in E.1–E.7 (L 11). "about" is 51 in E.13 and 37 in E.3 (L 5). "of order" is 17 in E.1 and 13 in E.7 (L 0). "a few" is 36 in E.11 and 26 in E.5 (book already high). | Turn about half of the "must" into statements of consequence ("a test against $q^2/2m_e$ alone confuses the two effects"). Use "however" or "but" for the real contrasts that are already there (for example E.6 l.46 "by contrast"). Replace "gives" with "is", "leads to" or "puts". Use "∼" or "typical" for "of order" and "about". |
| S7 | **Γ for rates** (STYLE: rates are `\varGamma`) | E.5 l.73 Γ_w; E.11 l.102 Γ, Γ_0; E.12 Γ_iso, Γ_anh, Γ_L (l.22–43, 67); E.13 Γ_ii, Γ_ph, Γ_tot, Γ_max (l.13–85) | Change to `\varGamma`. |
| S8 | **Unit conventions** in a natural-units book | ħ is restored in E.13 l.17 ("ħΓ = 0.066 eV") and E.4 l.107; k_B appears in E.11 l.44, 89, 102, while E.8 writes T | Write "the width $\varGamma = \SI{0.066}{eV}$" and drop k_B, or say once "with $k_{\mathrm{B}}$ restored". |
| S9 | **Spelling** (American) | aluminium E.9 l.3, 92, 93; tunnelling E.9 l.93, E.10 l.50, 52, E.11 l.18, 102; labelled E.7 l.96, E.8 l.74; label `eq:E.2-onecentre` | aluminum, tunneling, labeled; the label rename is optional. |
| S10 | **Citation and typography style** | Adjacent `\cite\cite` in E.3 l.11, E.12 l.26, 73, E.13 l.38, against "\cite[..]{a}, \cite[..]{b}" in E.4 l.13. "f-sum" in E.5 (2), E.6 (5), E.7 (2) against "$f$-sum" in E.2/E.3. `\hline` tables in E.11–E.13 against `\toprule` in E.1/E.3. Labels `tab:E.11-si`, `tab:E.12-*`, `tab:E.13-si` against `tab:E-functionals`. Abstracts cited (E.8 l.63, E.10 l.32). | One form each: `\cite[…]{a}, \cite[…]{b}`, `$f$-sum`, booktabs, `tab:E-short`, section numbers instead of "abstract". |
| S11 | **Procedure addressed to the reader** (brief) | Fix (E.4 l.7), Replace (E.4 l.97), Take (E.4 l.131, E.5 l.54, E.12 l.65), Fold / form… and transform (E.7 l.22, 29), "compute g … and compare" (E.5 l.30), "reconstruct…, check…, and treat" (E.2 l.104) | Rewrites in the section tables. Mathematical "Define …" and "write r = …" (E.7 l.47, 78) are standard and acceptable. |

**Scrub and cross-references.** No internal or process labels (SPINE, SEAMS, ledger, TODO, draft, reviewer): clean. No hard-coded numbers outside `\cite[...]` brackets: clean. No exercises or checkpoints. Limit boxes: none in App E, so not applicable.

## Per-section issues (location → problem → fix)

**E.1** | l.3 "specified fully so that it can be reproduced" → an assurance (#19) → cut the clause: "The worked numbers come from one calculation: the PBE functional, …".
| l.3 "Here we will follow … the functional, the plane-wave cutoff, …, and the effective masses." → S2 → "Here we will follow one calculation of silicon from its input to its bands and masses, and see which of its numbers can be used as they stand."
| l.20 "of a set of 40 semiconductors and insulators … over some forty semiconductors and insulators" → doubled phrase (#17) → "Against the low-temperature gaps of 40 semiconductors and insulators, HSE has a mean absolute error of 0.37 eV, falling to…".
| l.20, 41, 150, 163 "0.2 to 0.6 percent" next to `\SI{3.6}{\percent}` → mixed forms → use one throughout.
| l.12 "Its outputs, ground-state quantities, eigenvalues and states, and the responses built from them, deserve…" → stacked appositives → "The outputs deserve different levels of trust: ground-state quantities, eigenvalues and states, and responses built from both."
| l.41 "For the purposes of this book," → #17 → "In this book".
| l.138–147 the verbatim block repeats l.138's sentence item by item → list in place of prose → delete the block (keep the sentence) and move "240 Ry for the density, stop at 1e-12 Ry" into it.
| l.161 "For an insulator, fixed occupations should be used and the gap checked at the end." → restates the previous sentence and is advice → cut.
| l.163 the close points to E.3 and skips E.2 → seam → add: "…which \cref{app:E.3} supplies; the pseudopotential behind every number here is tested first, in \cref{app:E.2}."

**E.2** | l.3 "Here we will see how a pseudopotential is constructed and tested, what it does to the cutoff, and what it does to…" → S2, triad (#3) → "What it costs is the true region near the nucleus, exactly where a heavy-mediator rate looks at momentum transfers of tens of keV." (then keep "The last point…").
| l.42 "noticeably increased the differences" and l.81 "raises the electron-recoil rate considerably" → vague quantifiers (#12) → give the factor read from the cited table or figure.
| l.44 "and the rest of this section is about it" → #1 → cut.
| l.104 "The robust procedure is the one of Griffin and coworkers: reconstruct…, check…, and treat…" → #2 ("robust"), S11 → "Griffin and coworkers handle this range by reconstructing the all-electron states up to a cutoff set by the largest q needed, checking them against atomic orbitals for the shallowest core shell, and treating deeper shells as atomic orbitals."

**E.3** | l.3 repeats the E.1 hook (0.60 vs 1.17 eV, same citation), then two recap sentences ("That section explained…", "\Cref{sec:4.8} defined…") → #18 recap opener → open with the new number: "A one-shot $GW$ calculation started from LDA puts the silicon gap at 1.24 to 1.29 eV, where LDA gives about 0.5 eV and experiment 1.17 eV." Merge the two recaps into one clause.
| l.7 "changes the input of every later step, the threshold…, the energy denominators of a response, the screening, but it does not change its approximation level" → stacked appositives → put the list in parentheses: "changes the inputs of every later step (the threshold, the energy denominators, the screening) but not its approximation level".
| l.21 "The calculation runs from the Kohn–Sham states through … to the self-energy and the corrected energies." → restates the previous sentence (#5) → delete.
| l.23–34 "It starts…", "Next comes…", "supplied next", "is then evaluated", "The last step" → recipe sequencing → open each paragraph with its quantity ("The screening is built from…", "The frequency dependence comes from…").
| l.87 (WE) "needs two corrections. The calculations … omit spin–orbit coupling … The other is…" → ordinal with no "one" (#13) → "Two corrections separate it from the measurement: spin–orbit coupling, which …, and the zero-point renormalization, which …".

**E.4** | l.3 "Here we treat it as a tool: what a run returns, which approximation…, …, and where it typically goes wrong." → S2 → "Here we use it: the run that gives a phonon also gives the Born charges, ε∞ and the elastic constants, and, extended slightly, the empty-state changes a phonon-assisted amplitude needs (\cref{sec:13.2})." (merge with the next two sentences.)
| l.7 "Fix a phonon wavevector…" → S11 → "One perturbation is labeled by a phonon wavevector Q, a nucleus κ and a direction α."
| l.20 "A converged run returns three kinds of object. The first is … The second … The third…" → count-teaser and ordinals (#18) → "A converged run returns the screened potential, from which the vertex g follows; the dynamical matrix; and, at Q = 0, the response to a uniform field."
| l.65 "Two checks come for free." → #18 → "The acoustic sum rule for charges and the measured ε∞ cost nothing to check." l.65 "To see the direction, write" → "The direction follows from".
| l.97 "and it is worth knowing how badly. Replace the sum…" → #1, S11 → "How badly follows from replacing the sum over the grid cell around Γ by an integral over a sphere…".
| l.131 "One way out is to split the space. Take a window 𝒲…" → S11 → "One way out splits the space: a window 𝒲 … is summed explicitly…".
| l.147 "Finite strains are the most robust. One applies strains…" → #2 → "Finite strains are the most reliable: strains of a few tenths of a percent of both signs are applied, …".
| l.153 "Finally, the lattice constant is a parameter too:…" directly followed by l.155 "The lattice constant is a parameter in its own right." → #5 → delete the l.153 sentence and move its clause ("computed at the theoretical equilibrium … so that the forces vanish") into l.155.
| l.164 "The overestimate, about 10 percent" (12.89) against E.1 l.159 "11 percent" (13.04) → ambiguous → "10 percent for 12.89, 11 percent for 13.04".

**E.5** | l.3 "This section is about doing it: choosing…, testing…, interpolating…, counting…, and the route of…" → S2 → "In practice the work is in choosing and testing the Wannier functions and keeping every interpolated quantity in one gauge; the result is a rate whose fine-grid vertices, 270 TB of them, are never stored."
| l.30 "A practical test … is mandatory…: compute g directly … and compare." → S11 → "For a new material, the same comparison of g from direct DFPT at a few (k, Q) off the coarse grid is the only evidence that the interpolation converges."
| l.54 "Take the setup of Ref." → "The setup of Ref.~\cite{…} has $N_W = 26$ Wannier functions, …".
| l.79–87 six-step enumerate → list in place of argument (#11; editor note) → replace with: *"The calculation chains the steps above, and each link has its own check. It starts from the ground state and DFPT on a coarse wavevector grid (\cref{app:E.4}), with the frequencies checked against neutron data and the Born charges against zero. Bands on a coarse k grid fine enough to place the conduction minimum fix the Wannier manifold, whose frozen window covers the final and intermediate states and whose bands are tested off the grid. The coarse-grid vertices g are rotated into the Wannier gauge with their dipole and quadrupole parts removed. For each target q, ρ_mn(k, q) is computed from the plane-wave coefficients and rotated with the same U(k), and both are tested against direct values off the grid. For each q the window is the range ω < E_min(q) with no zero-phonon final state (\cref{sec:13.1}), cut to the fine-grid pockets of states that can contribute (its edges are in \cref{sec:13.9}). In that window the four-path amplitude is summed over the Wannier manifold, with the remainder from \cref{eq:E.4-dpsiperp}, into the phonon-assisted loss function on a grid in (|q|, ω)."*
| l.94 "of three kinds. The first … The second … The third…" → the ordinals of S1 → after cutting, keep only the coarse-grid and resolution warning and the close.

**E.6** | l.3 "This section turns each rung into a calculation with stated inputs, convergence parameters and cost, and it closes with…" plus a list of rungs → S2 → "Each rung of \cref{sec:4.6,sec:4.9} becomes a calculation with its own inputs and cost, and the rung chosen moves both the peak and the weight near the gap that light dark matter sees."
| l.9 $N$ in eq:E.6-R0 is not defined → first-use → add "N the number of k points".
| l.30 "Five parameters control…, and they interact." → count-teaser → "The wavefunction cutoff, the local-field cutoff, the band count, the k grid and the gap control … and interact."
| l.40 "This is not an error to be fixed but the f-sum rule of a nonlocal operator" → false contrast (#6) → "The excess is the $f$-sum rule of a nonlocal operator, the scissor, and…".
| l.52 "Two limits of the same calculation serve chapters far apart." → #18 → "Bosonic absorption (\cref{sec:10.7}) and the crystal Migdal response (\cref{sec:12.3}) take opposite limits of one calculation."
| l.68 "Two practical lessons from that calculation carry over." → #18 → name them in the sentence.
| l.70 "ε∞ ≈ 12" → editor ruling → 11.7. l.72, 74 "GW" → "$GW$".
| l.90 "The recurring errors are few." followed by eight → self-contradiction plus S1 → resolve under S1.

**E.7** | l.1 title "Crystal form factors and the density vertex" → #16, lint → "Crystal form factors".
| l.3 "This section is about how those numbers are produced: how…, how…, how…, and how…" plus three pointer sentences → S2 → "Each term is an overlap of two sets of plane-wave coefficients. The work is in restoring the core region the pseudopotential removed, adding the core shells, and knowing when the sum has converged." Keep one pointer sentence.
| l.22 "Fold k+q back into the zone," and l.29 "form the product … and transform it" → S11 → "With k+q folded back as k′+G_U, …"; "the product … is formed on the real-space grid and transformed".
| l.52 $\beta^{\mathrm{KB}}_{\kappa j}$, $D^{\mathrm{KB}}_j$ against E.2's $\tilde p_{\kappa i}$, $D_{\kappa,ij}$ for the same separable form → one symbol, one meaning → use E.2's.
| l.65–83 PAW, and l.42–61 velocity and scissor: see the redundancy table (R1–R3).
| l.85 "well above the pseudo rate" → #12 → give the factor from Griffin Fig. 5.
| l.96 "about 50 keV" against E.2 l.81 (reconstruction to 2 keV, ≈45 keV) → reconcile.
| l.137 the close calls E.6 the "next corrections", but E.6 comes before E.7 → seam → "…use the same vertices as input; \cref{app:E.6} treated them." Reordering E.6 and E.7 is the structural alternative (an editor's call).

**E.8** | l.3 "This section explains how such numbers are computed: the quasi-harmonic…, the self-consistent…, …, and the special-displacement method…" (lint long sentence) plus three pointer sentences → S2 → "We will see how a gap shift of tens of meV and the phonon shifts behind it are computed: some methods average the energy surface itself, and others average an electronic property over the zero-point distribution of the nuclei." One pointer sentence.
| l.37 "the method of choice" → cliché → "it is needed for light atoms, soft modes and quantum crystals".
| l.89–91 Pitfalls sit before the worked example (after it in E.1–E.7) → order → move them after we:E-zpr, cut per S1.
| l.96 "For a detector the conclusion is practical." and E.9 l.95 "For a detector the consequence is clear:" → shared tic (#9) → cut both frames and state the conclusion.
| l.99 the close calls E.5 "the next step" (E.5 is earlier) → seam → end on l.96's last sentence, or "…which is why the edges of \cref{chap:13} use the Wannier route of \cref{app:E.5}".

**E.9** | l.3 "This section explains how the exchange constants … are obtained … and how Eliashberg theory…" → S2/S3 (mild) → "We will see how DFT+U total energies, spin spirals and Green's functions give J^ex_ij, and how the Eliashberg equations turn α²F into a gap."
| l.55 "Antiferromagnets need one cone angle per sublattice and the pair energies of Ref.~\cite[Eq.~(8)]{jacobsson2013exchange}" → citation as content (#20) → state the two-sublattice relation in the book's convention.
| l.62 LKAG "in the convention of its source" → leaves the conversion to eq:E.9-heis to the reader → give the factor that converts it, as l.46 does for Fischer.
| l.95 "For a detector the consequence is clear:" → see E.8.

**E.10** | l.3 "This section explains how they are computed: supercell…, the correction…, excited states…, molecular dynamics…, and the coupling…" → S2 → "Both come from supercells whose defect must be isolated from its own images, electrostatically for charged states and dynamically for a recoil." One pointer sentence.
| l.23–24 "A supercell … is built…, the host total energy is computed, the defect is introduced, and the positions are relaxed" → a passive recipe → "The defect is relaxed in a near-cubic supercell at the host volume; the work lies in the number of charge and spin states, which must all be tried, since…".
| l.44–48 the displacement-threshold protocol duplicates E.11 l.77–85 with conflicting numbers ("about 4000 atoms … about 10 ps" against 4096 atoms and 20 ps); l.48's zero-point sentence repeats E.11 l.18 → redundancy → cut to two sentences (definition, 17.5–63.5 eV range, SW choice) plus "\cref{app:E.11} gives the protocol".
| l.46 "the DFT values themselves … come from Holmström, Kuronen and Nordlund" → #20 → state the average and ⟨100⟩, ⟨111⟩ values.

**E.11** | l.1 title has six words and a conjunction → #16 → "Recoil molecular dynamics" (the running head already exists).
| l.56 "How close do the atoms get?" → rhetorical question (#8) → "In a head-on collision …, the turning point r_min solves…".
| l.57–64 an in-text tabular with no number or caption → captions → fold the three missing rows into tab:E.11-si (which already has r_min at 20, 100 and 1000 eV), or number and caption it.
| l.73 "the switch has to be complete above the r_min of a 20 eV collision" against l.73 "complete below about 1 Å" → contradictory wording → "the machine-learned energy must be fully restored above the r_min of a 20 eV collision, 1.49 Å".
| l.100 "far more distinct close pairs than intuition would" → #12 → give the number from the census.
| l.112 "The second… third… fourth… The last two" → miscount, five and six are never named (#13) → "Two physical omissions remain:…".
| l.119 caption "The splice and time-step entries are derived in the text from…; the others are from the cited studies." → bookkeeping (#19) → cut; the citations in the cells already attribute.

**E.12** | l.33 "have known energy distributions of the daughters…~\cite[Eq.~(9)]{leman2012invited}" and l.71 "drawn from the accompanying angular distribution~\cite[Eq.~(9)]{kelsey2023g4cmp}" → #20 → state each distribution in one line, or say what it depends on.
| l.65 "Take a carrier with an isotropic mass…" → S11 → "For a carrier with an isotropic mass m and momentum k, …, the emission rate is".
| l.87 "several checks … The first … The fourth" → #18 (mild) → "Energy, charge, rate and step closure can be checked on every run at no cost."

**E.13** | l.13 "Three ingredients are needed. The first … The second … The third…" → #18 → "The cascade needs the quasiparticle bands up to tens of eV, the impact-ionization rate Γ_ii with its product distribution, and the phonon rate Γ_ph with its final states."
| l.23 Ω = 40.0 Å³ against 40.05 in E.1, E.6, E.7 → 40.05.
| l.36 "z_qp the quasiparticle residue, about 0.8" → unsourced (editor note) → "0.7 to 0.8 in semiconductors (\cref{eq:E.3-qp})", which carries E.3's source, or cite Hybertsen–Louie.
| l.38 "For weak Im χ" → χ is undefined, and the book uses R and ε⁻¹ → "For weak $\Imag W^{\mathrm{scr}}$".
| l.38 "reduces the rate by at most 0.75" → ambiguous → "multiplies the rate by no less than 0.75".
| l.85 "the GW rate already contains plasmon emission, and the phonon rate … must not be supplemented by a phenomenological phonon channel" → mixes two separate rules → "the $GW$ rate already contains plasmon emission, so no plasmon channel is added; the first-principles phonon rate likewise replaces, and is not added to, a phenomenological one."
| l.112 "is not a better ε_eh for silicon…, but a prediction…" → #6 (mild) → "What a first-principles cascade adds is a prediction for the materials of \cref{chap:17}…".

## Chapter-level checks

**Opening (appE.tex has none).** The appendix will hold two parts, the methods (E.1–E.13) and the per-quantity specifications (E.14–E.27, formerly E′), so the opening frames both. Proposed text, about 140 words; it avoids the 0.6 vs 1.17 eV hook that E.1 and E.3 already use:
> A dark-matter rate in silicon needs a few dozen numbers about the crystal: a gap good to tens of meV, a loss function out to 100 eV, density vertices at momentum transfers of tens of keV, electron–phonon couplings on grids of $10^9$ points, and the energy a struck atom leaves behind. Almost none of them is measured everywhere it is needed. Each is computed by a method with its own approximation, numerical parameters and typical failure. The first part of this appendix follows each method through one calculation, almost always of silicon, so that a number in the text can be traced to what it neglects and to the check that would expose it. The second part turns this around and specifies, quantity by quantity, the calculation behind each number the chapters use, with its inputs, its method and its convergence targets.

The two orienting sentences go one over STYLE's limit of one; that is justified because the appendix has two parts. In the final text, refer to the parts with \cref ranges, not section lists.

**Summary (none; STYLE asks every chapter to close with one).** Add a short closing section. It is also the right place for the lessons the S1 Pitfalls repeat. Sketch, 78 words:
> Every method here starts from one base calculation, at clamped nuclei with independent particles, and moves one entry of the truncation label at a time. Every numerical parameter is converged on the quantity used, not on the total energy. For silicon the dominant theory uncertainties are few: the gap (∼0.1 eV), the screening (ε∞ 13.0 computed against 11.7 measured), the vertex beyond $q \sim 1/r_c$, and, for recoils, the interatomic potential. The rest are controlled numerically.

**Cross-section redundancy** (keep one statement and point to it from the others).

| # | Content | Occurs | Keep | Elsewhere |
|---|---|---|---|---|
| R1 | PAW reconstruction of ρ_mn, derived in full twice with different symbols (φ against \varphi, ψ̃ against ψ^PS) | E.2 l.57–75 (eqs PAW, rhoPAW, onecentre); E.7 l.65–83 (eqs paw, pawO, radial) | E.2 | E.7: one paragraph citing eq:E.2-rhoPAW; keep the radial-grid remark and eq:E.7-radial |
| R2 | Nonlocal velocity v = p/m + i[V_NL, r] | E.1 l.133, E.2 l.100, E.4 l.33, E.6 l.90, E.7 l.42–52 | E.7 (with its derivation) | E.2 and E.4: one clause plus \cref{eq:E.7-vNL} |
| R3 | Scissor rescaling of velocities and the f-sum excess | E.3 l.13, 71–76; E.5 l.43; E.6 l.40; E.7 l.56–61 (eq:E.7-scis re-derives eq:E.3-vrescale) | E.3 | E.7: cite eq:E.3-vrescale and keep the 1.29 / 66 % silicon number |
| R4 | Nonlocal f-sum rule | E.2 l.85–98; E.5 l.88; E.7 l.115–121 | E.7 (the more general form, with group velocity) | E.2 derives the q→0 core and points to it; E.5 gets one clause |
| R5 | Germanium band order not fixed by a scissor | E.1 l.157; E.3 l.17, 57, 92; E.7 l.127 | E.1 (the numbers) and E.3 l.57 (the core) | E.3 l.17, E.7: one clause |
| R6 | Zero-point renormalization double-counted by a scissor | E.3 l.17, 92; E.8 l.91, 96; E.5 l.75 | E.8 | E.3 l.17: one clause plus \cref{we:E-zpr} |
| R7 | Si ε∞ 13.04 against 11.7 and the overscreening argument | E.1 l.85, 159; E.3 l.15; E.4 l.70, 164 | E.4 l.65–70 | E.1 l.159 shortened |
| R8 | Lattice constant and Grüneisen parameters of opposite sign | E.4 l.155; E.8 l.24 | E.8 | E.4: one sentence |
| R9 | Displacement-threshold protocol (conflicting 10 ps vs 20 ps, ≈4000 vs 4096 atoms) | E.10 l.44–48; E.11 l.18, 77–85 | E.11 | E.10 cut (see E.10) |
| R10 | "Converge on the quantity used, not the total energy" | E.1 l.163; E.4 l.153; E.6 l.26 | the summary | — |

**Seams** (each pair of adjacent sections read across the join).

| Join | Reading | Fix |
|---|---|---|
| E.1→E.2 | E.1 points to E.3 and E.2 opens on the 1s orbital: abrupt | close of E.1 (see E.1) |
| E.2→E.3 | "the subject of \cref{app:E.3}", and E.3 opens on the gap: good, except that E.3 reuses E.1's hook | E.3 l.3 |
| E.3→E.4 | E.3 closes on the BSE of E.6; E.4 opens on phonons. Acceptable (a new topic) | none |
| E.4→E.5, E.5→E.6 | explicit hand-offs: good | none |
| E.6→E.7 | E.7 is the input of E.6 but follows it; its close points "next" to E.6 | E.7 l.137 |
| E.7→E.8, E.8→E.9 | E.8 closes backward on E.5 as "next step" | E.8 l.99 |
| E.9→E.10, E.10→E.11 | the E.10 close hands off to E.11 cleanly, but its own threshold subsection already said E.11's content | R9 |
| E.11→E.12, E.12→E.13 | independent topics with clean closes. E.13 (Chap. 18) after E.12 (Chap. 20) is out of chapter order, but readable | none |

**Captions.** tab:E-functionals, E-cutoff, E-gw, E.12-rates, E.12-si and E.13-si stand alone. The E.11 l.57 tabular has no caption (E.11). The tab:E.11-si caption carries bookkeeping (E.11).
**Citations.** Attribution style is good in most places, and equation-level references are frequent. The #20 cases are E.9 l.55, E.10 l.46, E.12 l.33 and l.71. Format: S10.

## Editor-notes items concerning prose

- E.5 enumerate: flagged; prose rewrite given (E.5).
- E.6 about 70 words under the floor: agreed, no padding. The S1 cut lowers it further, which is acceptable for an appendix.
- E.3 "about 0.5 eV": present (l.3) and fine. The table keeps 0.52 and E.1 0.51, as ruled.
- E.13 z_qp ≈ 0.8 without a source: still open (E.13 l.36), with a fix given.
- 𝔗 written inline as `\mathfrak{T}` in E.1, E.4–E.8, E.10–E.13: consistent throughout; leave unless `\Trunc` is adopted.
- E.11 running head: present. Shortening the full title is still advised (E.11 l.1).
- Grüneisen symbol: `\gamma^{\mathrm{G}}` used in E.8; E.4 has words only. Resolved.
- Si ε∞ = 11.7 ruling: E.4 complies; E.6 l.70 "≈ 12" should read 11.7.

## Register calibration (2–3 passages per section; could Lin, or Kahn and Lin, have written them?)

| Sect. | Passages checked | Verdict | Rewrite of one sentence |
|---|---|---|---|
| E.1 | l.3 opener; l.79 "two pitfalls"; l.150 mass vs gap | yes, no, yes | l.79 → "Two things go wrong with the cutoff: different quantities converge at different rates, and the stress picks up a Pulay term." |
| E.2 | l.3 1s-orbital estimate; l.44 "necessary but not sufficient"; l.104 recipe | yes, yes, no | l.104 → see E.2 table |
| E.3 | l.11 "better than it looks"; l.21 recipe colon; l.87 SOC averaging | yes, no, yes | l.21 → "The workhorse for semiconductors is the one-shot $G_0W_0$ of Hybertsen and Louie: build G and W once from Kohn–Sham states, and correct the energies to first order." |
| E.4 | l.3 "Every number that…"; l.97 "worth knowing how badly"; l.149 Voigt "catches many users" | yes, no, yes | l.97 → "The catch is the zone center, where the acoustic frequencies vanish as cQ and the summand of \cref{eq:E.4-B} blows up." |
| E.5 | l.56 "Nobody stores it."; l.30 "mandatory … compute and compare"; l.62 window count | yes, no, yes | l.30 → see E.5 table |
| E.6 | l.48 "good news for the loss function"; l.40 "not an error to be fixed but"; l.70 exciton estimate | yes, no, yes | l.40 → see E.6 table |
| E.7 | l.3 four-"how" opener; l.89 kinematics of the 2p shell; l.134 "Kinematics tells us where to look" | no, yes, yes | l.3 → see E.7 table |
| E.8 | l.3 "deep in the zero-point regime, where none … are thermal"; l.37 "most common error in reading SCHA output"; l.96 "conclusion is practical" | yes, yes, no | l.96 → "So the window and threshold calculations of \cref{chap:13} take the measured gap and do not add the renormalization again." |
| E.9 | l.34 "is not a number"; l.25 "changes the physics"; l.80 "the weak point" | yes, yes, yes | (none needed; the best-calibrated section) |
| E.10 | l.3 T-center hook; l.65 "the correction, not the cell, converges the result"; l.23 passive recipe | yes, yes, no | l.23 → see E.10 table |
| E.11 | l.3 recoil picture; l.44 "zero for every practical purpose"; l.56 rhetorical question | yes, yes, no | l.56 → see E.11 table |
| E.12 | l.3 "The sensors … see neither the deposit nor the cascade"; l.89 "cannot be distinguished from one with an energy leak"; l.87 "worth only what its checks show" | yes, yes, yes | l.87 → "A transport run is only as good as its checks, and four of them cost nothing." (names follow) |
| E.13 | l.3 50 eV → 13 pairs; l.54 "The catch for a cascade is the energy range"; l.13 three ordinals | yes, yes, no | l.13 → see E.13 table |

Overall the physical-picture and estimate sentences match the models well (E.9, E.12 and E.13 are best). The gap is the connective tissue (S6) and the recipe voice of the "must" sentences and Pitfalls lists.
