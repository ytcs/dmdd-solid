# Ch. 3 prose review (style and prose, isolated)

Scope: tex/ch03/ch03.tex, s3-1 … s3-6 (with the Summary), App. C.1–C.8, D.4–D.5. Checked against STYLE.md, style-guide.md, prose-review.md and REGISTER.md. Figs. 3.6–3.8 are judged for pedagogy only. Format: `file:line → problem → fix`.

## Verdicts
| Section | Words | Verdict | Deciding issues |
|---|---|---|---|
| 3.1 Lattices and reciprocal space | 3.4k | REVISE | gap value 1.11 vs 1.17 (A2); stale Γ sentence; false "always dΩ_q" |
| 3.2 Bloch states and band structure | 5.1k | REVISE | (200) contradiction (A1); two sentences that need a second reading; φ_j and velocity hat |
| 3.3 Si, Ge and GaAs | 4.2k | REVISE | lattice-constant labels (A3); κ clash (A4); text tied to the regenerated figures (F) |
| 3.4 Many electrons and DFT | 3.5k | REVISE | (200) contradiction (A1); text tied to Fig. 3.8 (F) |
| 3.5 Plane waves, pseudopotentials, core | 4.3k | PASS | minor hits only, below 3 per 1000 words |
| 3.6 Wannier functions (+ Summary) | 4.7k | REVISE | "keyresult" in the prose; Summary placement and consistency; two overloaded paragraphs |
| App. C.1, C.3, C.4, C.5, C.6, C.7, C.8 | — | PASS | minor items below |
| App. C.2 | — | REVISE | lattice sum duplicates §3.1 (editor note) |
| App. D.4, D.5 | — | PASS | minor items below |

No section needs REWRITE. The voice is consistent across the six writers: "we" for author and reader, no "you", no "I", no exercises, checkpoints or tasks left to the reader, no em-dash overuse, no "see Ref. X for …", and nothing banned (grep and lint both clean).

## 0. Lint record (lint.py --banned BANNED-TERMS.txt)
- 0 blocking hits in every file. Total hits: ch03.tex 0, s3-1 5, s3-2 5, s3-3 7, s3-4 4, s3-5 2, s3-6 4, C.1 1, C.2 1, C.3 0, C.4 0, C.5 1, C.6 3, C.7 1, C.8 2, D.4 0, D.5 4.
- EQ-PUNCT (s3-1:127,146,150; s3-2:144,172,193,209; s3-3:20,178,208; s3-4:44,123,138; s3-6:64; C.2:31; D.5:54,85): all false positives on reading. Each one either has its period inside a `cases`, `aligned` or `gathered` block, or is a display in the middle of a sentence that continues in prose ("for some …", "for every …"). There is one real case, which lint does not flag (D.4 below). Also clean on reading: inflated adjectives, reflexive triads, stacked hedges, restating paragraphs, bullets used for argument; no `limitbox` occurs in the scope (grep).
- LONG-SENT: every hit is inflated by inline math or by an EQN placeholder. The only one that needs a rewrite is s3-5:158 (B-3.5).

## A. Contradictions across sections and notation clashes (copy-editor catches)
- **A1 (200) component.** s3-1:215 and C.17:3,76 say that (200) vanishes exactly, by the glide symmetry, for every function with the symmetry of the crystal, and that only (222) returns through the bond charge. Three places say otherwise.
  - s3-2:153: "provides the potential of silicon with its (200) and (222) components". Fix: "gives the potential of silicon its (222) component; (200) stays zero by the glide symmetry (\cref{app:C.17})".
  - s3-4:54: "gives $V_{\mathrm{KS}}$ exactly these components". Fix: "gives $V_{\mathrm{KS}}$ a (222) component, which the basis structure factor removes from the nuclear part; the (200) component vanishes for any crystal-symmetric potential (\cref{app:C.17})".
  - s3-2:77: "for spherical atomic potentials $U_{\vect{G}_{200}} = 0$" implies that a non-spherical potential could give a nonzero value. Fix: "and $U_{\vect{G}_{200}} = 0$ exactly, by the glide symmetry (\cref{app:C.17})".
- **A2 Gap value.** s3-1:177 (we:3-scales) uses "$\Eg = \SI{1.11}{eV}$", but s3-3:24 says the book uses 1.17 eV and that 1.11 eV is the value used in projections. Fix: recompute the worked example at 1.17 eV, or write "the projection value $\Eg = \SI{1.11}{eV}$ (\cref{we:1-mmin})". s3-3:193 already does the latter.
- **A3 Lattice constants (editor note).** s3-3:33,35 and the caption of tab:3-materials call the Ge and GaAs values "extrapolated to zero temperature", and s3-3:35 gives GaAs as 5.648. The ruling is room temperature throughout: Si 5.431, Ge 5.658, GaAs 5.653 Å, in one sourced table. Fix the GaAs value and the labels; 5.658 for Ge is already the room-temperature value.
- **A4 Symbols to rule at the batch review (recommendations).**
  - s3-3:77: bold $\vect{\kappa} = \vect{k} - \vect{k}_0$ clashes with κ, the basis index (s3-1:21), which s3-3:135 uses in the same section ($w_\kappa$, $\xi_{\mathrm{SO},\kappa}$). Use $\delta\vect{k}$, as the editor suggests.
  - s3-2:106: atomic orbitals $\varphi_j$ → $\varphi^{\mathrm{at}}_j$ (approved).
  - s3-6:23 uses $\varphi_n(\vect{k})$ for a phase and s3-6:33 uses $\varphi^{\mathrm{tr}}_n$ for trial orbitals. Write the phase as $\theta_n(\vect{k})$, or keep the superscript discipline.
  - Velocity hat: s3-2:209,213,217,226 and s3-4:107 write `\op{\vect{v}}`, but A.5:38 writes a bare $\vect{v}$. Default to A.5 and drop the hat.
- **A5 Stale typography sentence.** s3-1:101: the zone points are upright "to keep them apart from the rates $\Gamma$ of \cref{chap:2}". After the \varGamma sweep (which a grep confirms is done in ch03) this should read "from the italic rates $\varGamma$ of \cref{chap:2} and the loss function $L$ …", or the clause can be cut.
- **A6 False claim of uniqueness.** s3-1:19: "the solid angle is always $\dd\Omega_q$", but C.3:7 writes $\dd\Omega_{\hat n}$. Fix: "a solid angle always carries a subscript, as in $\dd\Omega_q$".
- **A7 Inconsistent CBM position.** The caption of Fig. 3.12 (s3-6:143) says the PBE gap is "at $0.85\,(2\pi/a)$", but s3-4:66 gives the PBE CBM at 0.840. Fix the caption to 0.84.

## B. Section issues

### 3.1
- l.3: the opener is concrete (a kilogram of silicon, two consequences named in the sentence). OK.
- l.26: "The index $\kappa$ is the basis-site index $\kappa$ of $Z_\kappa$" repeats κ. → "This is the κ that labels $Z_\kappa$ and $n_\kappa(\vect{k})$ in \cref{sec:2.3}; two sites of one element still carry different κ."
- l.139: "A sum of $N$ phases is of order $N$ when …" restates the keyresult and uses the tic "of order". → "Physically, the $N$ phases add up only when they agree at every site, and cancel otherwise."
- l.141: "fill exactly four bands~\cite[Sect.~4.1]{essig2016direct}" credits a counting fact to a dark-matter paper. Drop the citation or move it to Ashcroft–Mermin.
- l.220: the closing rhetorical question, "What do the electrons do …?", is borderline pattern 8. Acceptable as the hand-off, but a statement is better: "\Cref{sec:3.2} labels the electron states in this potential by …".
- Calibration (REGISTER §6.13). Lin could have written l.170 ("The momentum transfer itself is never reduced to the first zone") and l.206. She would not write l.26, so that one is rewritten above.

### 3.2
- l.3 opener: it is concrete, but three outline sentences follow ("We will derive … We will then compute … We follow"). Keep one (see C).
- l.122: "The result is exact only if … Its value is that …" is flat. Calibration rewrite: "Of course, the result is only as good as the basis, which in practice is a few orbitals per atom; the payoff is that a handful of numbers fix the band structure."
- l.277 needs a second reading: "This value of $q$ marks a scale: from this particular $k$ the transition deposits \SI{1.6}{eV}, which needs $q \ge \SI{0.61}{keV}$". → "This $q$ marks a scale, since the vertex here is evaluated at fixed $k$. The transition it describes actually costs \SI{1.6}{eV} and needs $q \ge \SI{0.61}{keV}$."
- l.279: "Band 1 keeps a quarter … The other half" is unanchored, because band 2's quarter is never stated. → "Band 2 receives a quarter of the probability and band 1 keeps another quarter; the remaining half, from …".
- l.268: "15 to 20 percent" → `\SIrange{15}{20}{\percent}`. The same applies across the chapter (C).
- Lin could have written l.100 ("Silicon is not in the regime where these estimates are quantitative … What survives is the mechanism") and l.266 ("Parametrically, then, …").

### 3.3
- l.3: three outline sentences, opening "In this section we locate …" (pattern 1). → keep the motivation and one sentence: "We will locate these band edges, derive the effective mass and spin–orbit splitting, and compare the smallest pair energy at each $q$ with what the halo delivers."
- l.111: "which we call $|X\rangle$" is the "we call" tic. → "denoted $|X\rangle$".
- l.203: "half way" → "halfway". The same line packs three conclusions into four sentences; split before "Slightly below".
- Redundancy: the Kane estimate with a 0.5 eV gap, giving $0.025\,m_e$, appears in l.149 and again in s3-4:95. Keep it in one place and point to it from the other.
- Calibration: Lin could have written l.73 ("so a cold crystal holds no thermally excited carriers at all") and l.215 ("buys less reach than its value suggests"). l.182 is a "so"/"because" chain. Rewrite: "In silicon it cannot. At that momentum transfer $E_{\mathrm{min}}$ is well above $\Eg$, and the true threshold of the indirect gap lies above $m_{\mathrm{min}}$."

### 3.4
- l.3 opener: concrete, and it states why the problem matters (0.15 vs 0.33 MeV). Good.
- l.30: "It knows nothing about the nuclei" is anthropomorphic (pattern 15; the same phrase appears in D.5:26). → "It does not depend on the nuclei".
- l.64: "Each step up this ladder" refers to a ladder that was never introduced. → "Each step from LDA to GGA to hybrids costs more".
- l.82 and D.5:89 contain the same sentence almost word for word (the godby1986 one). Keep it in 3.4 and cut it to a pointer in D.5.
- l.89, Fig. 3.8 caption: "(every listed value)" is unclear. → "(all values listed there)". On pedagogy: panel (a) mixes a Gaussian-basis LDA calculation with a separate $G_0W_0$ calculation and says so, which is acceptable.
- l.107: "Energies and densities are straightforward" is vague ("densities" means the vertex). → "Energies and the density vertex are easy."
- l.154: `\cref{sec:1.3-edge}` resolves, but the label does not follow the STYLE form (sec:N.M). Note only.
- Lin could have written l.20 ("In a crystal the frozen-orbital hypothesis costs nothing."), l.93 (the physical picture, with "But the other electrons are frozen.") and l.146.

### 3.5 (PASS; minor fixes)
- l.3: "the few-keV transfers" uses bare "transfers" (REGISTER term 6). → "the few-keV momentum transfers".
- l.17: "would be reached if the two states have" → "had".
- l.43: "the f-sum rule" → "the $f$-sum rule", as in s3-4:18,134. C.5:28,74 should follow.
- l.47: "below 2 keV" → `\SI{2}{keV}`; "ten percent" → `\SI{10}{\percent}`.
- l.83: "The reconstruction raises the heavy-mediator rate" gives no size (pattern 12). Give the factor from Griffin et al. (Sect. 3.1) at a stated threshold, in the book's own words.
- l.158 is a garden-path sentence: "every shell dark matter lighter than \SI{0.3}{GeV} can reach, which excludes only …". → "Dark matter lighter than \SI{0.3}{GeV} reaches every shell except silicon $1s$ and germanium $2p$ and below. Each shell it reaches needs relativistic corrections of at most a few percent in energy, and less in its states."
- l.29 (Hamann–Schlüter–Chiang conditions) reads as a list of conditions in Giustino's register. Calibration rewrite: "Two conditions do the work: the pseudo and true states must agree beyond $r_c$ at the reference energy, and they must hold the same charge inside it; the rest follows."
- The "about" count (32 per 10k words) is mostly the preposition ("about the nucleus"), so it is not the hedge tic. Lin could have written l.47 ("… and at large $q$ the pseudo answer is wrong").

### 3.6 (and Summary)
- l.161: "The keyresult requires the supercell …" leaks a LaTeX environment name into the prose. → "The exactness condition of \cref{eq:3.6-exact} requires …".
- l.93 does three jobs: the disentanglement theory, the figure result, and the false-minimum remark. Split before "\Cref{fig:3-wf} shows". If the derivation reviewer does not confirm the away-from-bond orientation (editor note), the text here, the Fig. 3.11 caption, the l.138 error figures and the Summary must revert to the standard bond-pointing picture.
- l.138 also does three jobs (silicon convergence, analytic derivatives, interband velocities). Split at "Derivatives come for free."
- l.149: "That is the rule of \cref{app:A.5}. Its reason takes a few lines." is signposting (pattern 1). → "That is the rule of \cref{app:A.5}, and the reason is short."
- Summary: it is `\section*{Summary}` inside s3-6.tex, not a section of its own, so a partial build that omits s3-6 has no summary (STYLE l.8). Move it to its own file, input from ch03.tex after s3-6.
- Summary l.180: "At momentum transfers of several keV and above, the density vertex depends on the oscillations …". s3-5:83 says the pseudo vertex is accurate only "below about \SI{1}{keV}". → "Above about a keV, …".
- Summary against the accepted 3.5 (editor request): the $(Z\alpha)^2$ scaling, the 0.3 GeV statement and the PAW and semicore content all agree. The only mismatch is the one at l.180.
- Lin could have written l.3 (the opener) and l.127 ("The coarse grid does not lose the hoppings; it folds them"). l.149 is dense and in Giustino's register; the rewrite above is the minimum change.

## C. Chapter as a whole
- **Opening (ch03.tex:3).** It is motivational and concrete: the 3.3 Å wavelength against the 2.35 Å bond, and the link from Chap. 2's open question to bands, gaps and the threshold. It closes with one orienting sentence and gives no section list. PASS (STYLE l.40). Optional: "about \SI{1.1}{eV}" could read "\SI{1.17}{eV}", to match 3.3.
- **Section openers.** Sections 3.2, 3.3, 3.5 and 3.6 each follow a good concrete first sentence with two or three "We will …" or "In this section we …" sentences. STYLE allows one. Merge each tail into a single sentence; 3.3:3 is the worst case.
- **Summary.** It covers every section in connected prose, and its closing pointer to Chap. 4 is good. Fix the placement and l.180 as above.
- **Redundancy across sections.**
  - The (200)/(222) extinction story appears in 3.1, 3.2 and 3.4; once A1 is fixed, 3.2 and 3.4 should only point to the 3.1 worked example.
  - Photon and absorbed-dark-matter kinematics appear in s3-2:259 and s3-3:184; keep 3.3 and shorten 3.2 to a clause.
  - The Kane mass at a 0.5 eV gap appears in s3-3:149 and s3-4:95.
  - The LDA lattice constant 5.401 Å appears in s3-1:49 and s3-4:56; the second is acceptable as a pointer.
  - The Hartree–Fock gap picture appears in s3-4:22 and l.93, and the second does not point back to the first. Add "as anticipated above".
- **Seams.**
  - 3.1→3.2: a rhetorical hand-off, then a concrete opener (B-3.1).
  - 3.2→3.3 ("is the subject of Sect. 3.3" → VBM/CBM numbers): clean.
  - 3.3→3.4 ("at the price of a gap that comes out too small" → "puts the gap at about 0.5 eV"): clean, though the point is made twice in a row. Trim the last clause of 3.3:218 to "and the next section obtains it from the many-electron problem."
  - 3.4→3.5 and 3.5→3.6: clean.
- **Register calibration across the chapter (per 10k words; Lin's rate in brackets).**
  - Tics: "so" 17–28 (L 11), "only" 16–30 (L 11) and "gives" 6–16 (L 7) in 3.2–3.6.
  - Missing hedges and connectives: "typical(ly)" 0–3 (L 15); "for instance/example" 0 in 3.2–3.6; "of course" 0; "we can/we see" nearly 0.
  - Good signs: "however" is present in every section, "since" is at a healthy 7–26, and there are no "thereby", "whereby", "respectively", "in order to", "i.e." or "e.g.".
  - Action at revision: replace about a third of the chained "so" and "only" with "since" or "as a result", and turn the bare "of order" estimates into "typical"/"∼" hedges in 3.2 and 3.5.
- **Number style.** "85 percent" (3.3:3), "two percent" (3.6:3), "about one percent" (3.3:142), "15 to 20 percent" (3.2:268) and "ten percent" (3.5:47) sit beside `\SI{…}{\percent}` elsewhere. Use `\SI` throughout.
- **Citations.** The numeric style is uniform and equation-specific citations are used for formulas. All citations attribute and none carries content; the literature-notation mapping in s3-2:190 is allowed by REGISTER §7.
- **Cross-references.** All use \cref; there are no hard-coded numbers. The only nonstandard label is sec:1.3-edge.
- **Titles.** All are short noun phrases. "Silicon, germanium and gallium arsenide" is long but names the content; OK.

## D. Appendices
- **C.1** PASS. l.18: "Three members recur in this book:" names its members in the same sentence, so it is not a count-teaser. OK.
- **C.2** REVISE (editor note). l.28–42 re-derive the reciprocal lattice, the Born–von Karman grid, the geometric sums and the counting from s3-1:51–124. Cut the subsection to a pointer to \cref{eq:3.1-latticesum}. Keep the infinite-crystal form (s3-1:139 points here for it), eq. C.2-unfold and the grid-error material. l.3 ("which also yields the lattice sum that \cref{sec:3.1} uses") then reads backwards. → "… and gives the infinite-crystal form of the lattice sum of \cref{sec:3.1}."
- **C.3** PASS. l.79: "$\sim q_0/2$ in the units of \cref{sec:1.3}" → "$\sim q_0/2$ (\cref{sec:1.3})".
- **C.4** PASS.
- **C.5** PASS. Write "$f$-sum" at l.28 and l.74.
- **C.6** PASS. l.83 has three clauses joined by semicolons: "which is Bloch's identity; \cref{app:D.15} gives a proof; the identity is due to Bloch, and Mermin …". → "This is Bloch's identity, proved in \cref{app:D.15}; Mermin gave a short alternative derivation~\cite{mermin1966short}."
- **C.7** PASS. The opener is four parallel sentences ("Positive semidefiniteness bounds … Block inversion turns …"), mechanical but informative.
- **C.8** PASS. In l.44, "The reference writes $k$" → "The DLMF writes $k$".
- **D.4** PASS.
  - l.33: "the result takes its canonical form." comes before a display. → end with a colon, or make the display part of the sentence. This is a real equation-punctuation hit that lint missed.
  - l.86: "(\cref{sec:4.2})" for the valence $k_{\mathrm{F}}$ and $E_{\mathrm{F}}$ of silicon; everywhere else these are credited to \cref{sec:2.5}. → \cref{sec:2.5}.
- **D.5** PASS.
  - l.82: HOMO and LUMO are not defined at first use. → "the highest occupied (HOMO) eigenvalue … lowest unoccupied (LUMO)", or write $E_{\mathrm{ho}}$ and $E_{\mathrm{lu}}$ in words.
  - l.89: trim the duplicate of s3-4:82 to "This is the band-gap problem of \cref{sec:3.4}".

## E. Text tied to the regenerated Figs. 3.6–3.8 (pedagogy only; re-sync the numbers after regeneration)
- Pedagogy: all three captions stand alone, saying what is plotted, the units, the method and the measured comparison. Panel (b) of Fig. 3.6 (E_min against the kinematic curves) is the strongest teaching figure in the chapter.
- If the figures move to QE PBE + scissor (the editor's default), the sentence at s3-3:44, "The bands … come from the oldest quantitative method for them, the empirical pseudopotential", and the rest of that paragraph must be rewritten. If the empirical model is kept, label it in the text as a pedagogical model.
- These sentences quote model numbers and must be re-synced: s3-3:102 (0.853, 0.872/0.184, "113 bands", 3.73 eV, 2.27 of 5.43), s3-3:120 (E_P = 18.3, 0.0718/0.0721), s3-3:175 (1.26 eV near 3.4 keV, 2.2 eV), s3-3:203 ("about \SI{2.0}{eV} in the band model"), s3-3:215 ("in every direction of Fig. 3.6(b)"), s3-4:84 (0.54 eV at 0.84; "0.53 to 0.64 eV"), and the captions of Figs. 3.6, 3.7 and 3.8.

## F. Editor-notes items that concern prose
- Γ sweep: done in ch03 (no rate is written with \Gamma); fix the wording at s3-1:101 (A5).
- C.2 → pointer to §3.1: see D.
- Ge/GaAs lattice constants, room temperature, one table: see A3. The ε∞ value of 11.7 is fine.
- Si gap 1.17 / 1.12 eV: correct in 3.3; s3-1:177 still uses 1.11 (A2).
- φ^at_j and the velocity hat: A4 (A.5 convention, no hat).
- E_qp is already used at s3-4:75. H_Dar is already used at s3-5:133; renaming D.6's term is left to the Ch3/Ch4 revision.
- Si 2p doublet: s3-5:101 gives 99.4 and 99.8 eV explicitly, and l.142 says "a few tenths of an eV". The two are consistent; keep them.
- 3.6 Wannier orientation and interpolation errors: these are for the derivation reviewer. If they are not confirmed, revert the prose as in B-3.6.
- New 3.6 symbols (Ω_W^I, M_mn, λ_Δk, φ^tr, A^pr, L_sc, ξ_W, …) are each defined at first use in the prose, except for the phase clash between φ_n(k) and φ^tr (A4).
