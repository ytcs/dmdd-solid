# Ch9 prose review (style, register, standalone scrub)

Scope: tex/ch09/ch09.tex (opening), s9-1 … s9-4, tab9-3.tex, s9-summary.tex. Checked against STYLE.md, style-guide.md, prose-review.md (patterns 0–26), REGISTER.md and ledgers/REVIEWS/ch09/editor-notes.md. No tex edited. Line numbers are file lines.

## Verdicts

| Unit | Verdict | Non-minor reason |
|---|---|---|
| Chapter opening (ch09.tex) | REVISE | paragraph 2 is a section-by-section list framed as three questions |
| 9.1 Excitation–interaction matrix | REVISE | caption of Table 9.1 says "---" = no channel, but the text puts symmetry-allowed cells under "---"; mobile defects filed under "order in the coupling"; WE count "two of the last" is three; looped paragraph l.101 |
| 9.2 Kinematic map | REVISE | process artifacts (ZrTe₅ parameter row, Table 9.2 caption); ω_th defined narrowly then used for all channels; bare c for a sound speed next to "units of the speed of light"; 45 vs 46.7 MeV; two looped sentences |
| 9.3 Momentum–energy plane | REVISE | "the published tables" uncited in caption and text; undefined g₃₃, g_c, ⟨ω⟩, δM_κ, q_BZ in text; third telling of the absorption-at-q≈0 argument |
| 9.4 Limit Checks and 𝔗 | REVISE | "recover 90 … give 75 of them a box" contradicts l.54 (80 rows in 75 boxes); process artifacts l.7, l.15; label components n_B, n_g, 𝒳, 𝒦, 𝔐 used without glosses; hard-coded "Appendix F" in a title |
| tab9-3.tex | PASS | minor only |
| Summary | PASS | minor only (hard-coded "Appendix F") |

The four writers share one voice: declarative, number-led, the book's terms of art (momentum transfer, threshold, reach, phonon-assisted, Migdal effect, loss function, heavy and light mediator). No section needs a REWRITE. The common weakness is the register's connective tissue (Sect. 3 below) and a handful of facts told three to five times across sections (Sect. 2).

## 1. Lint (lint.py --banned BANNED-TERMS.txt)

No blocking hits, no banned terms, no PERIPHRASIS or EQ-PUNCT hits.
- s9-1: 4 (1 DASH, 3 LONG-SENT) · s9-2: 6 LONG · s9-3: 6 LONG · s9-4: 0 · tab9-3: 1 LONG · summary: 0.
- s9-1 l.20 DASH is a false positive: the "---" cell marks of the tabular. Most LONG-SENT hits are captions or table rows merged by the parser.
- Genuine long sentences (> 45 words, math collapsed): s9-1 l.21 ("They keep the target rows and change the kinematics: …", ~75 words, four items); s9-1 l.95 ("These are the endothermic threshold …", ~60); s9-2 l.69 ("At a common threshold of 1 meV …", ~50); s9-2 l.89 ("Differentiating … leaves only the explicit dependence", ~45 with a nested condition); s9-3 l.16 ("That is the momentum at which the impulse approximation of …, the treatment of a nucleus kicked so hard that …, takes over …", stacked appositive). Split each; for s9-3 l.16: "At that momentum the impulse approximation of \cref{sec:11.4} takes over from the sum over phonon numbers. It treats the nucleus as kicked so hard that its spectrum is a Gaussian of width $(E_R\langle\omega\rangle)^{1/2}$ about $E_R = q^2/2M$, with $\langle\omega\rangle$ the mean phonon energy."

## 2. Chapter-level checks

**Opening (ch09.tex l.2–4).** Paragraph 1 is right: concrete (1 MeV → 3.5 eV, 1.17 eV gap, 64.1 meV phonon, Al 0.36 meV), motivational, tied to Chap. 8, and it ends on the stake (double counting, or a channel missed). Paragraph 2 breaks STYLE ("at most one closing sentence orients the reader; never a section-by-section list"): its three questions are 9.1, 9.2 and 9.3 in order, and "the chapter ends by placing each of them on the expansion hierarchy" is 9.4.
- Fix: keep one orienting sentence, e.g. "Before any rate is computed, we therefore fix for each pairing of an excitation with a coupling the section that computes it, the lightest dark-matter mass it reaches and where its final states lie on the $(q,\omega)$ plane; \cref{chap:17} later reads the same table along its columns." Drop "The answers form a matrix …" and the Limit-Check sentence (9.4 has its own concrete opener).
- l.2 "to kick a nucleus whose electrons are occasionally left behind excited" is periphrasis (pattern 25) for a named effect. Write "or, if it couples to nucleons, to make a nucleus recoil, which now and then leaves its electrons excited (the Migdal effect)".
- l.2 "or enter none" has no example; either give one (a cell no section treats) or cut "or enter none".
- l.2 "the list of possibilities grows with the target" is low content (pattern 0); the next sentence already shows it. Cut.
- ch09.tex l.8 source comment "% Sections are \input here in order." sits between two inputs; delete (source hygiene, not printed).

**Summary.** One paragraph per section, recap only, numbers match the sections (6.12 keV, 0.405–0.408 MeV, 27/48, 6 of 90). Two fixes:
- l.9 "Appendix F records …" hard-codes the letter: write "\Cref{app:F} records …".
- l.5 "the phonon-assisted onset at 0.333 MeV": 9.2 gives 0.3332 (exciton) and 0.3374 MeV (free pair). Write "the phonon-assisted onset just above the floor, 0.333 MeV".
- The editor note says the summary was drafted before 9.2 was final. Rechecked: every 9.2 claim in it is still in 9.2; it omits the Migdal edge at the floor and the halo percentages, which is acceptable.

**Redundancy across sections.** Five facts are told three or more times. Keep the first full statement and cut the rest to a clause or a \cref.
1. Absorption at q ≈ 0 excludes acoustic phonons and free nuclei: s9-1 l.91 (full argument), s9-2 l.35 ("An acoustic phonon at $q = m_\phi v$ … cannot absorb the boson"), s9-3 l.104 (whole paragraph), Summary. Cut s9-3 l.104 to one clause in the 9.3-others opener ("absorption samples only the point $q \approx 10^{-3}\omega$, \cref{sec:9.1-empty}"); cut the s9-2 sentence to a \cref.
2. Silicon Z* = 0, so no dark-photon single phonon: s9-1 l.97, WE 9.1 l.108 and l.110, s9-2 l.35, s9-3 Table 9.3 row 1 and l.54, Summary. Keep s9-1 l.97 and s9-3 region 1 (where the cross-term reading is new); in s9-2 l.35 cut "since its two atoms are identical and their Born charges vanish (\cref{sec:5.5})" to "(\cref{sec:9.1-empty})"; in WE 9.1 keep it once (l.108) and replace the l.110 repeat by "nothing in silicon".
3. Acoustic edge above the floor by v_max/4c because of backscattering: s9-2 l.20, l.39, WE 9.2 l.84, Summary. In WE 9.2 keep the numbers and drop "lower by 21.5" (already in l.20).
4. Aluminum "sixty times" below the silicon acoustic edge: s9-2 l.3 and l.69. Cut the l.69 sentence "Aluminum pair breaking is the lowest of all the scattering edges, sixty times below …".
5. The silicon indirect-gap window 0.3332–0.405 MeV: s9-2 l.26 and l.71. In l.71 keep only the new facts (germanium upper end unknown; GaAs ends at the L valleys; pair detectors reach the floor only through phonon-assisted scattering).

**Seams.**
- Opening → 9.1: clean; the 9.1 opener names the 24 × 6 table at once.
- 9.1 → 9.2: 9.1 ends on the dark-photon sector split, 9.2 opens on Al pair breaking. No bridge, but the opener is concrete and 9.2 l.3 points back to Table 9.1. Acceptable.
- 9.2 → 9.3: the order runs against the logic that 9.3 l.58 itself states ("The lightest mass whose curve touches a region is the minimum mass of that channel, the quantity that \cref{sec:9.2} draws"). 9.2 uses the shapes E_ch(q) before 9.3 draws the supports. Swapping the sections is not required; at least cut the l.58 back-reference to "(\cref{sec:9.2})" and make the two sections use one name for the quantity (see 9.3 item 9).
- 9.3 → 9.4: 9.3 ends on the quasiparticle-sector caveat, 9.4 opens on the free-recoil Limit Check. Abrupt, but the opener is concrete. The chapter opening promises that "the same matrix also locates the literature formulas"; 9.4 uses the label 𝔗, not the matrix, until its last sentence. Align the opening sentence with what 9.4 does.

**Map role (Part I → Part II).** No Part II derivation is re-done; Part II numbers are quoted with their home sections. Two places quote more Part II results than a map needs: WE 9.4 l.41–45 (0.05, 0.22, 0.47; "more than 10⁴"; x_R ≥ 2.3, q ≥ 70 keV), and s9-3 l.54 (the coupling-in-proportion-to-mass cancellation). Keep the placements and one number per rate; the rest belongs to the Limit Checks. WE 9.2 l.80 (the acoustic-sum-rule error, 29 % at 0.02·2π/a) is Chap. 5 material; cut to "the edge needs slopes that obey the acoustic sum rule (\cref{sec:5.4})".
Forward pointers: nearly all carry a one-line gloss ("\cref{sec:10.6}, which treats ionization of the core and semicore shells"). Unglossed at first use: s9-1 l.91 and l.110 \cref{sec:11.8}. Add the gloss there ("absorption on phonons and on the acoustic modes of a finite body").

## 3. Register (REGISTER.md)

Counts over the chapter (14,200 words incl. tables), per 10k with Lin's rate in brackets: "however" 0 [8.0]; "we will/we can/we see" 0.7 [29]; "note that" 0 [6.1]; "for example/for instance" 0.7 [9.5]; "typical(ly)" 0 [15.3]; "since" 4.2 [13.9]; "only" 39 [11]; "therefore" 9.2 [2.9]; "of order" 2.8 [0]. No "i.e.", "e.g.", "respectively", "in order to", "thereby".
- "only" at 3.5× Lin's rate is the chapter's tic (s9-2 and s9-3 have 16 each). Many are negation-flavored restrictions: s9-2 l.3 "takes up the gap only from about 45 MeV", l.28 "free only when", l.71 "reaches its floor only through", s9-3 l.3 "it can only make phonons", l.30 "in two ways only". Cut half; recast as positive conditions ("from 46.7 MeV", "once it exceeds").
- "therefore" 13 times: s9-1 l.77, l.89, l.91, l.95; s9-2 l.12, l.35, l.71, l.73 (twice in l.71–73); s9-3 l.16, WE l.65. Replace about half with "since …" clauses or "as a result".
- Zero "however" and zero "typical" in 14k words. Add where a real contrast or a hedge exists: s9-2 l.22 "The narrow-gap III–V semiconductors, however, …"; s9-2 l.39 "Collective modes … open at typically 0.1–20 keV".
- "we call" twice in one paragraph (s9-2 l.12: "We call $\bar q$ …", "which we call the floor"); REGISTER lists "we call" as a tic. Write "Let $\bar q$ be the momentum at which …" and "the threshold mass of \cref{eq:1.3-mmin}, the floor below which no channel lies".

**Calibration (2–3 passages per section; could Lin, or Kahn and Lin, have written it?)**
- 9.1 l.89 (density cannot create a magnon): yes. l.75 (sectors add …): yes. l.21 (six columns, operator by operator): no; it narrates the formalism symbol by symbol. Target for its first sentence: "The first column is the one most models use: anything whose leading target operator is the electron density $n_e$, a heavy or light mediator alike."
- 9.2 l.20 "The reason is momentum. A phonon of energy ω_th carries ω_th/c, and the dark matter hands over that much momentum only by backscattering": yes (move 3.5). l.24 (ZrTe₅ parameter rows): no. Target: "For ZrTe₅, with $\Delta_{\mathrm{D}} = \SI{11.8}{meV}$ and $v_{\mathrm{D}}/v_{\mathrm{max}}$ between 0.17 and 0.42, the edge is 7.1–9.6 keV depending on direction, a little above the flat-continuum value of 6.72 keV." l.96 (percent catalogue): borderline; a verdict sentence first would fix it: "The halo matters at the few-percent level: …".
- 9.3 l.54 "Omitting the cross term there would make a vanishing rate look like the sum of two large ones": yes. l.16 impulse sentence: no (see Sect. 1 rewrite). l.7: no (see 9.3 item 2).
- 9.4 WE l.41: yes, close to Lin's estimate-then-check. l.15–17 (what the box leaves out, how status is read): no; bureaucratic. Target: "The plot also tells us how far to trust the formula: inside the gray band it agrees with the fuller result to the stated tolerance, and that statement is only as good as the fuller result."

## 4. Issues by section (location → problem → fix)

### 9.1
1. l.15 last sentence "We build the two axes from \cref{chap:8}, give each row its sector …, explain the empty cells, and then show how a dark-matter model selects its cells" → subsection list in prose (pattern 18). → Cut; the preceding sentence about double counting is the motivation.
2. Table 9.1 caption "--- no channel at leading order" vs l.97 "A spin coupling can flip the spin of a core electron, break a Cooper pair or accompany a Migdal transition; these cells are allowed by symmetry, but the book does not compute them, and they are entered as empty." → the table contradicts its own caption (editor-notes 9.1 Q1). → Adopt the provisional "○" mark (allowed at leading order, not computed in this book), add it to the caption key, and change l.97 to "… they are marked ○". Cross-check against tab:22-gaps.
3. Table 9.1 caption, sector key "ad electron-following, 0 zero-phonon electronic, $+$ phonon-dressed electronic; ad$^{\mathrm{s}}$ …" → comma-separated key is hard to parse; "ALP" and "abs." in the header are never expanded. → Use "ad: electron-following; 0: zero-phonon electronic; +: phonon-dressed …" and add "ALP: axion-like particle; abs.: absorption".
4. l.23 last sentence "The remaining rows name excitations that no earlier chapter introduces, and each carries a one-line description in the table together with the section that treats it." → describes the table's typography (pattern 0). → Cut, or keep "Rows that no earlier chapter introduces carry a one-line description."
5. l.71 "Three processes are not one excitation and have no row. … Processes second order in the coupling are the third (\cref{sec:9.1-empty})." → count-teaser, and the paragraph then moves to the 17.3 entries and to nuclear-spin couplings: three jobs in one paragraph. → Split: (a) "Coherent scattering off a random medium and dark-photon absorption by the vibrations of a glass are not single excitations; \cref{sec:16.7} treats them with the two-level systems, and second-order processes have no row (\cref{sec:9.1-empty})." (b) The 17.3 and 11.6 explanations as a second paragraph, or as caption notes.
6. l.87 "Four reasons account for nearly all of the 90 empty cells." → count-teaser (pattern 18), mitigated by the run-in heads. → "Operator content, the kinematics of absorption, the order in the coupling and the absence of a new response account for nearly all of the 90 empty cells."
7. l.93 "The same holds for mobile defects, defectons and crowdions, which dark matter does not create at leading order." → files a row of all-empty cells under "Order in the coupling", but defect motion is not a second-order process (editor-notes Q4). → Move to its own sentence after the four reasons: "The row of mobile defects is empty by construction: dark matter does not create defectons or crowdions; the row records that they release the energy of earlier excitations late, through the kinetics of \cref{sec:16.8,sec:19.6}." Confirm 16.8 covers defectons (Q4).
8. Free-recoil row × electron-density cell is empty, and none of the four reasons explains it (editor-notes Q3), while l.79 gives the multiphonon row a density entry through the following cloud. → Add one clause to l.79 or l.95 saying why the cloud-carried charge of a freely recoiling atom is counted in the multiphonon cell (11.3) and not in the recoil row.
9. l.101 "A dark-matter model selects its cells in three steps. …" → restates l.21 (column assignment) and l.87 (selection rules); no new fact (pattern 26). → Delete; open the subsection with l.103 "A heavy scalar mediator coupled to electrons enters only the density column: …".
10. WE 9.1 l.114 "the eleven cells of the vector column and two of the last" → l.112 lists three last-column cells (pairs in 10.9; plasmons and optical phonons in 17.3). → "three of the last", or say that the two 17.3 cells count as one formula.
11. WE 9.1 l.110 "$\vect{B}' = \ii\vect{p}_\phi\times\hat{\vect{e}}\,A'$" → $\hat{\vect{e}}$ and $A'$ are not defined. → "with $\hat{\vect{e}}$ the polarization and $A'$ the field amplitude".
12. l.21 and l.95 long sentences → see Sect. 1.
13. l.79 "of order" → "∼" or "about" (register tic).
14. Title "Leading-order selection of a cell" → gestures; the content is why 90 cells are empty. → "Empty cells and selection rules".

### 9.2
1. l.3 "a free silicon nucleus takes up the gap only from about \SI{45}{MeV}" → periphrasis plus negation (pattern 25), and with $\Eg = 1.17$ eV the value is 46.7 MeV (s9-3 l.18; Sect. 1.3 used 1.11 eV). → "a free silicon nucleus receives 1.17 eV from 46.7 MeV".
2. l.3 "\SI{0.10}{keV}" → write "\SI{100}{eV}" here and in Table 9.2, or keep keV in the table only.
3. l.7 "we write $\omega_{\mathrm{th}}$ for the threshold $E_{\mathrm{th}}$ of \cref{sec:1.3} wherever the excitation is a phonon or a magnon" → ω_th is then used for every channel (floor, pairs, Fig. 9.1). → "we write $\omega_{\mathrm{th}}$ for the threshold $E_{\mathrm{th}}$ of \cref{sec:1.3}." Update NOTATION l.771 ("used in phonon formulas") to match.
4. l.12 "We call $\bar q$ …" and "which we call the floor" → register tic; "the floor" is a second name for the threshold mass m_min of Sect. 1.3, and can be confused with the neutrino floor. → See Sect. 3; keep "floor" but tie it once to m_min: "the threshold mass $m_{\mathrm{min}}$ of \cref{eq:1.3-mmin}, which we refer to as the floor".
5. l.16–20, the unnumbered display, Fig. 9.1 caption "$\omega_{\mathrm{th}}/[2c(v_{\mathrm{max}} - c)]$", and WE l.76 "In units of the speed of light, $c = 9.35/299792$" → bare c for a sound speed (NOTATION entry 66: bare c is the speed of light). The WE sentence uses c for a sound speed while naming the speed of light. → Use $c_\nu$ for phonons and $c_{\mathrm{M}}$ for magnons; for the general branch write $v_{\mathrm{b}}$ or $c_{\mathrm{ch}}$ (propose to NOTATION). Also the display gives bare $m_{\mathrm{min}}$, which NOTATION reserves for the threshold mass: write $m_{\mathrm{min}}^{\mathrm{ch}}$.
6. l.22 "Two entries of \cref{tab:9-atlas} are closed this way." → both cells are populated in Table 9.1, so the reader is confused. → "Two populated cells of \cref{tab:9-atlas} are closed this way to halo dark matter in elastic scattering."
7. l.24 "ZrTe$_5$ with the half-gap … of the measured crystal structure, the parameter row that \cref{sec:16.1} adopts for its Dirac-pair rates, …; \cref{we:7-zrte5} used the row of the relaxed cell, $\Delta_{\mathrm{D}} = \SI{15.6}{meV}$." → bookkeeping about which parameter set was adopted (pattern 19). → See Sect. 3 rewrite; if the 15.6 meV value must be mentioned, one clause as a fact about the literature: "(the relaxed cell gives 15.6 meV)".
8. l.24 "A magnon with a gap has the same shape. … at \SI{1.1}{meV} in MnF$_2$ …, and far-infrared absorption places a zone-center magnon of NiO at \SI{4.54}{meV}" → no edge follows; the paragraph stops on two energies. Also Table 9.4 calls the same 4.54 meV "(model)". → Give the edge for one case (or say it sits on the floor because c_M ≪ v_max), and make "measured" vs "model" agree between 9.2 and Table 9.4.
9. l.26 "from two independent calculations" → reviewer-facing provenance (pattern 19). → Cut; the range itself carries the information.
10. l.39 "five and a half decades apart" repeats l.35. → Cut the l.39 clause.
11. l.69 last sentence and l.71 second sentence → looped (Sect. 2, items 4–5).
12. Table 9.2 caption "Three entries follow here from \cref{eq:9.2-mch}: the acoustic edge of aluminum, with the longitudinal speed 6.63 km/s that \cref{sec:20.3} uses for phonons entering aluminum films; the floor of ZrTe$_5$; and the silicon $2p$ edge, from the opening momentum of \cref{sec:10.6}. Status: computed, unless marked as an estimate." → provenance bookkeeping and a "Status:" label (patterns 19, scrub). → "Entries without a section are computed here from \cref{eq:9.2-mch} (Al: $c_{\mathrm{LA}} = \SI{6.63}{km.s^{-1}}$; Si $2p$: opening momentum \SI{38}{keV}). Estimates are marked." The "Section" column then lists "this section" for the three.
13. l.96 "$-6.0$ and $+6.6$ percent", "$-3.9$ percent" next to \SI{6.3}{\percent} → mixed style. → \SI{}{\percent} throughout.
14. Title "Five targets on one map" → mild gesture. → "Edges of five targets".
15. Opener l.3 last sentence ("We derive …, place …, and list …") → acceptable as the one orienting sentence; keep.

### 9.3
1. l.3 "Give silicon a momentum $q = \SI{50}{keV}$ … and it can only make phonons." → imperative address and "can only" (STYLE: no address; pattern 25 lite). → "At $q = \SI{50}{keV}$ and $\omega = \SI{50}{meV}$ silicon has phonon final states and nothing else. At \SI{1}{keV} and \SI{1.3}{eV} its only final state is a pair together with a phonon; at \SI{1}{keV} and \SI{3}{eV} a pair without a phonon is open as well."
2. l.7 "so the step from kinematics to excitations can be read off directly" → no content (pattern 0). → Cut.
3. l.3 "we draw the region that holds most of the weight and say how it was chosen" → self-narration (pattern 22). → "we draw the region that holds 90 % of the weight (Fig. 9.2 caption)".
4. Fig. 9.2 caption "the random-phase loss function with local fields of the published tables (gap set to \SI{1.11}{eV} …)"; l.22 "In the published silicon tables"; WE l.65 "the loss function of the tables" → which tables? The reader must look elsewhere (pattern 20, standalone). → Cite once in the caption and write "the tables of \cref{sec:10.2}" in the text.
5. Fig. 9.2 caption "energy transfer $\omega$" → the book's term is energy deposited (REGISTER term 8; opening uses "energy deposit"). → "energy deposited $\omega$".
6. l.16 "at $q_{\mathrm{BZ}}$", "$\langle\omega\rangle$" → q_BZ is defined only in the caption; ⟨ω⟩ nowhere. → "at the zone radius $q_{\mathrm{BZ}} = \SI{2.25}{keV}$"; define ⟨ω⟩ as the mean phonon energy (Sect. 1 rewrite).
7. WE l.67 "$\langle\omega_e\rangle \approx \SI{6}{eV}$ and $\delta M_\kappa/M_\kappa = 2.7\times10^{-4}$" → neither is glossed. → "with $\langle\omega_e\rangle$ the mean electronic excitation energy and $\delta M_\kappa$ the electronic mass that moves with the nucleus (\cref{sec:8.6})" (check the gloss against NOTATION).
8. Table 9.4 "$q\,g_{33} = 7\times10^{-5}$" and "$\omega = v_{\mathrm{D}}q_\parallel/g_c$" → $g_{33}$ and $g_c$ undefined; the table is not readable on its own. → Add to the caption: "$g_{33}$: gyration-tensor component; $g_c$: Luttinger parameter of the nanotube" (or the book's names).
9. l.58 "the minimum mass of that channel"; 9.2 "lightest mass", "edge", "threshold mass", "floor" → one quantity under four names. → Use "lightest mass" (or "edge") in both sections; reserve "threshold mass" for m_min of Sect. 1.3.
10. l.54 "Its practical consequence is a rule for the plane" → unanchored "Its" (pattern 13). → "The practical consequence of region 4 is a rule for the plane".
11. l.54 "an open question that \cref{app:E.14} specifies a calculation for" → awkward. → "an open question; \cref{app:E.14} specifies the calculation that would settle it".
12. l.104 → redundant (Sect. 2, item 1).
13. Title "The other targets of the atlas" → gestures ("other"). → "Supports in other materials".
14. tab:9-overlaps caption is self-contained (defines S^A_{eκ}, the dark-photon coupling, scope). Keep.

### 9.4
1. l.3 "The channel chapters recover 90 published formulas as limits of their own results, and give 75 of them a box of the same kind." vs l.54 "Eighty belong to the 75 Limit Checks, since a box may compare two formulas" → 80 formulas are boxed, not 75. → "… recover 90 published formulas as limits of their own results and test 80 of them in 75 boxes of the same kind."
2. l.7 "Where the published form differs from the book's by a convention, a normalization or a misprint, the box states the book's form and the citation gives the source equation for credit. Everything needed to evaluate the formula is in the box or in the equations it cites from the book." → assurance aimed at a reviewer (pattern 19); the first sentence of the paragraph already says the formula is in the book's notation. → Cut both sentences.
3. l.13 "It names the physics that a user of the formula outside its range would miss." → restates the sentence before it (pattern 5). → Cut.
4. l.15 "The box leaves out the approximation chain, the formal record and the status of the formula." → negation-framed triad that answers a design directive. → State where each lives, positively: "The approximation chain, from the book's general result to the formula, is derived in the running text next to the box. The formal record (chain, conditions, plot specification, size of the leading correction) is the formula's row in \cref{tab:F-rows}. The status is read from the plot itself:" then l.17.
5. l.21 "Clamped nuclei put it at $n_B = 0$; …" and l.34 "None of the boxes has its leading correction on $n_B$ or $n_g$" → the chapter is a map, but the eight components are never glossed here (𝒳, 𝒦, 𝔐, n_B, n_g, n_A, n_D, n_T). Fig. 9.3 shows them without words. → At first use give a one-line gloss of each, e.g. "$n_B$, the order in the nuclear boost; $n_g$, the order in the electron–phonon vertex; …" (from \cref{sec:8.5}), or add the glosses to the Fig. 9.3 caption.
6. WE l.41 "plots the rate weight against $q/q_0$" → $q_0$ undefined. → "against $q/q_0$, with $q_0 = \alpha m_e$ the reference momentum" (confirm the definition used in lim:10.1a).
7. l.21 "Almost every row of \cref{tab:F-rows} states the placement" → bookkeeping about the appendix. → Cut, or "Each row of \cref{tab:F-rows} ends its approximation chain with this placement."
8. l.52 (six columns of tab:F-rows) → a column-by-column description of another table (pattern 0, translated-from-formalism). → Keep only the reader-relevant facts: bold sizes, and "unsized" marks a correction the book names but does not size; move the rest to App. F's own introduction.
9. Title "The record of Appendix F" and l.50 → hard-coded appendix letter in a title, and gesturing. → "The formal record of the limits"; in text use \cref{app:F}.
10. "box" is used about 30 times for the Limit Check. STYLE bans "limit box", not "box", but repeated bare "box" reads as internal jargon. → Use "Limit Check" at each paragraph's first mention, "the box" only within a paragraph.
11. Fig. 9.3 caption "grouped by the value at which the formula sits (italic)" → unclear. → "grouped by the formula's value of that component, printed in italic (e.g. IP, impulse)".
12. l.34–36 count paragraphs: list-like but each count is a fact; acceptable for a map. The closing explanation l.36 ("A magnon rate truncates in $1/|\vect{S}|$ …") is the right ending.
13. Citations: WE l.45 "\cite{lewin1996review}" lacks the equation number STYLE asks for. → add the equation numbers of the rate and of the Helm form factor actually used. l.43 "\cites[…]{knapen2021dark}[…]{hochberg2021determining}" fine.

### tab9-3.tex (generated)
- Caption stands alone (defines both columns and the qualifier kinds). Counts verified against the text: on-label 27 = 𝒳 12, 𝒦 6, n_A 3, 𝔐 3, n_D 2, n_T 1; qualifiers 48 = 5 + 9 + 5 + 29; per chapter 8/15, 7/20, 7/9, 0/8, 2/17. All match s9-4 l.34–36 and the editor notes.
- Minor: rows print in source order, so 11.5c precedes 11.5b and 16.7d precedes 16.7c. Sort by label in fig9_3.py.
- Minor: lim:10.9a "Inelastic electron recoil" has controlling parameter Δ_χ but leading correction 𝒳: IP → RPA + LF; a reader expects the axis variable to drive screening. Confirm with the box (derivation reviewer).

## 5. User rules and scrub

- No exercises, checkpoints or "left to the reader" anywhere. "\cref{app:E.14} specifies the band calculation that would fix it" (s9-2 l.26; s9-3 l.54) states an open item, not a task. Pass.
- Citations attribute only: pass except the "published tables" item (9.3 item 4) and the bare lewin cite (9.4 item 13). s9-2 l.14 and l.20 cite kahn2022searches for commonplaces with equation numbers; acceptable.
- \cref throughout; \ref only inside tables (correct). Hard-coded "Appendix F" twice (s9-4 l.50, summary l.9).
- Process artifacts (pattern 19): 9.2 items 7, 9, 12; 9.4 items 2, 4, 7. No internal labels (SPINE, SEAM, LE-numbers, "writer") in printed text.
- Limit Checks: 9.4 describes them as self-contained comparison plots without a Source/Chain/Validity list, as STYLE requires; "Limit Check" naming correct, no bare "Limit N.M".
- Pattern 25, read sentence by sentence in the chapter opening, all four section openers, every subsection opener and every caption: hits only at opening l.2 ("kick a nucleus whose electrons are … left behind excited"), s9-2 l.3 ("takes up the gap only from"), s9-3 l.3 ("can only make"). Captions clean.
- Pattern 26, paragraph fact lists: every paragraph adds at least one fact except s9-1 l.101 (subset of l.21 + l.87), s9-3 l.104 (subset of s9-1 l.91), s9-4 l.13 second sentence. Partly looped: s9-2 l.69 last sentence, s9-2 l.71 sentence 2, s9-2 l.39 "five and a half decades". Subsection endings: all end on a new fact or a pointer, except 9.1-models, whose WE ends on "only the sector split … keeps them apart", a restatement of l.75 that is acceptable inside a worked example.
- Equation punctuation: all displays punctuated (eq:9.2-mch, the unnumbered edge, eq:9.2-abs, eq:9.2-halo, WE displays). eq:9.2-abs is trivial ($m_\phi = \omega$) but referenced; keep.

## 6. Editor-notes items concerning prose

- 9.1 Q1 (○ mark): not adopted in the tex; caption contradiction (9.1 item 2). Adopt.
- 9.1 Q2 (10.2 acoustic peak only in prose): present in 9.4 WE l.43; fine as prose.
- 9.1 Q3 (free recoil × e-density empty): unexplained (9.1 item 8).
- 9.1 Q4 (16.8 covers defectons): prose misfiles the row (9.1 item 7); content check left to the derivation reviewer.
- 9.3 NiO 118 vs 236 meV: resolved; Table 9.4 states "twice the band top". But "gap 4.54 meV (model)" conflicts with 9.2 "far-infrared absorption places" (9.2 item 8).
- 9.3 "bounded above only at 2.07 eV": s9-3 l.20 says "an upper value for the onset over all directions". Clear.
- 9.4: the reading of a box is given in 9.4 because the front matter lacks it. Accepted; 9.4 items 2–4 remove the defensive sentences that the arrangement invited.
- Summary drafted before final 9.2: rechecked (Sect. 2).
