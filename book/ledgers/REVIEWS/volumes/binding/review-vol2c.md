# Binding review, block vol2c (Chaps. 14-17)

Reviewer: independent, against `git diff -U0 60cc72c` on tex/ch14-ch17 (no generated files in these chapters). Every changed sentence was read in a sentence-aligned word diff and then in context in the current file. Read in full: all of ch14 (every section file), s15-2, s15-3 and s15-4 (most of each), and the opening paragraphs of every ch16 and ch17 section. Read in context only (the edited paragraphs and their neighbours): the rest of ch15, ch16 and ch17. The editors' logs were not consulted before the verdicts below were formed. The ranker was run with `--summary` on all 33 files: every file has 14-28 flagged sentences per 1000 words, with no outlier, and the highest are ch16.tex, ch17.tex, s16-9, s17-6, s16-1 and s17-4. The recall top-up was weighted toward these files.

## Verdict

| Chapter | changed sentence groups checked | accepted | fixed | reverted |
|---|---|---|---|---|
| ch14 | 163 | 157 | 6 | 0 |
| ch15 | 108 | 106 | 2 | 0 |
| ch16 | 216 | 215 | 1 | 0 |
| ch17 | 200 | 197 | 3 | 0 |
| total | 687 | 675 | 12 | 0 |

Overall the editors' work is sound. Most rebindings are correct and faithful; several interpretations were checked against the physics and hold (for example s17-4:11, the force in the frame of the nuclei is m_e times the acceleration *of the nuclei*; s17-5:172, the LiF cell holds four *formula units*, which reproduces omega_p^val = 26.1 eV; s17-5:174, Ge 0.47 is indeed the pole-limit value; s14-1:104, "defect of 3.1 %" = overcount Delta S/|S| = 0.078/2.5; s14-3:107, 20 Fe in the primitive cell of four formula units). Errors were mostly over-repair (robotic repetition) and a few new constructions that need two parses.

## Fixes and reverts

| file:line | editor text | my text | reason |
|---|---|---|---|
| ch14/s14-1:74 | "is $1+2\Delta S$, the same statement as the value of $W_\perp$ in \cref{eq:14.1-ratio}, and the zone average gives a check" | "is $1+2\Delta S$, which restates $W_\perp$ of \cref{eq:14.1-ratio}, and this zone average gives a check" | "a statement as a value" does not parse; repeated noun phrase |
| ch14/s14-1:76 | "The fraction $\Delta S/\|S\|$ is an estimate of the leading correction" (directly after "...too large by the fraction $\Delta S/\|S\|$.") | "This fraction is an estimate of the leading correction" | over-repair: one candidate in the previous sentence |
| ch14/s14-1:104 | "on the same lattice linear spin-wave theory overcounts" | "on the same lattice, linear spin-wave theory overcounts" | garden path ("lattice linear ...") |
| ch14/s14-2:37 | "as a rate for light dark matter requires, since light dark matter samples only small $q$" | "as the rate requires: light dark matter samples only small $q$" | robotic repetition; the inserted domain was redundant |
| ch14/s14-5:105 | "and with both time reversal and inversion $\vect{L}^{ph}$ vanishes" | "... inversion, $\vect{L}^{ph}$ vanishes" | the edit made the PP run into the subject |
| ch14/s14-6:115 | "...a complex Gaussian variable, with independent real and imaginary parts of equal variance, and the sum of signal and noise is again a complex Gaussian variable with independent real and imaginary parts of equal variance" | "..., and so is the sum of signal and noise" | robotic triple-length repetition |
| ch15/s15-3:105 | "With the normalization of \cref{tab:15-edge}, division by $\mathfrak g_I$, \cref{eq:15.3-MB} gives" | "In the normalization of \cref{tab:15-edge}, that is divided by $\mathfrak g_I$, \cref{eq:15.3-MB} gives" | defining apposition ("division by") reads as a second subject |
| ch15/s15-3:138 | "The configurational average of the loss function and the loss function of the averaged $\varepsilon$ are both open for amorphous WSi..." | "For amorphous WSi at momentum transfers of a keV, neither the average nor the loss function of the averaged $\varepsilon$ is known." | open item; editor's reading kept (see below), heavy subject removed |
| ch16/s16-7:144 | "...that the two-level system absorbs later, and this two-step process belongs" | "...absorbs later; this two-step process belongs" | three-way "and" chain; scope |
| ch17/ch17.tex:2 | "and its design starts from the coupling instead of the excitation" | "and the question it faces starts from the coupling instead of the excitation" | fidelity: base said the *question* runs from coupling to excitation; "its design starts" was a new claim |
| ch17/s17-1:44 | "since the whole Migdal rate at 1 MeV comes from momentum transfers between about 0.75 keV and $2q_{BZ}$ (29 % of it from below $q_{BZ}$)" | "... comes from this range of momentum transfers (29 % ...)" | verbatim repeat of the range stated three sentences earlier |
| ch17/s17-4:89 | "In the window \cref{eq:17.4-lock} sets the scale" | "In the window, \cref{eq:17.4-lock} sets the scale" | garden path ("the window eq.") |

Fixes in text the editors did not change (base text in the second column):

| file:line | base text | my text | reason |
|---|---|---|---|
| ch14/s14-1:9 (open) | "changes sign under a reciprocal vector of the sublattice that maps A onto B" | "changes sign when $\vect{q}$ is shifted by a reciprocal vector $\vect{G}$ of the sublattice for which that phase is negative" | attachment; no reciprocal vector maps A onto B |
| ch14/s14-5:17 (open) | "The current block is the first that differs." | "For the current block, unlike the density block, the two relations differ." | relational word without comparand |
| ch14/s14-5:184, tab:14-nuisances (open) | "Magnetic anisotropy near the gap" | "Magnetic anisotropy near the mass edge" | name used in s14-1 for the same row |
| ch17/s17-1:9 (open) | "Below the lattice ceiling ... Above it ... at the lattice ceiling" | "Below the lattice ceiling, the larger of $\omega_{max}$ for one phonon and $E_R^{max}$ for a free recoil, ... Above the lattice ceiling ... at the lattice ceiling" | definite before introduction |
| ch17/s17-5:26, tab:17-fom (open) | "$L(q,\omega)$ in the window" | "$L(q,\omega)$ in the kinematic window" | unified name |
| ch17/s17-6:31 (open) | "not ranked in the two nuclear channels" | "not ranked in the two channels that need one, the heavy-mediator single-phonon rate and the nuclear edge" | unnamed set |
| ch14/s14-6:165 (recall) | "Both curves follow from the Neyman construction" | "The Rayleigh and fixed-power curves both follow ..." | "both" picks from two earlier sentences |
| ch15/s15-4:38 (recall) | "29.7 or 56.4 eV. This is two hundred times the 0.15 eV ..., and 61 times less than $k_F$" | "The smaller value is two hundred times ..., and the larger is 61 times less than $k_F$" | "this" bound to two different values (29.7/0.15 = 198, 3450/56.4 = 61) |
| ch15/s15-1:27 (recall) | "this phase reproduces" | "this choice of phase reproduces" | second candidate: "the phase operator" |
| ch15/s15-1:100 (recall) | "At 1 eV all three agree" | "At 1 eV the three loss functions agree" | set spread over three caption sentences |
| ch16/s16-3:110 (recall) | "Gray: both ratios within" | "Gray: the ratios for $qR = 3$ and 8 both within" | same |
| ch15/s15-4:161,162, nuisance table (recall, tables) | "the phonon-assisted part near the edge"; "Scalar absorption near the edge" | "... near the pair-breaking edge" (both cells) | the caption defines "edge" as the kinematic edge; these cells mean the pair-breaking edge |

## Open items

- **ch14 s14-1:9** "changes sign under a reciprocal vector of the sublattice that maps A onto B": fixed. The relative clause attached to "the sublattice", and no reciprocal vector maps A onto B. New: "changes sign when $\vect{q}$ is shifted by a reciprocal vector $\vect{G}$ of the sublattice for which that phase is negative". This is the same physics, since J_AB(q+G) = e^{iG.delta_0} J_AB(q). (An explicit "= -1" was refused by the guard as a new math item, so the wording is in prose.)
- **ch14 s14-5:17** "The current block is the first that differs": fixed to "For the current block, unlike the density block, the two relations differ." The comparand is the density block of the previous sentence.
- **ch14 tab:14-nuisances** "Magnetic anisotropy near the gap": changed to "near the mass edge". This matches s14-1:126, where "Near its gap" became "Near the mass edge" and the row's numbers are the rates at 10 and 30 keV near the mass edge. The guard is clean.
- **ch15 s15-2** display in the subject ("the ratio of imaginary to real part, [display], is not small"): this stays. Moving the predicate before the display requires changing the display's punctuation from "," to ".", which the guard refuses (STOP on the display), so I reverted my attempt. The sentence parses, because the display only names the ratio.
- **ch15 s15-3 "Both are open"**: the editor's reading (the configurational average of the loss function, and the loss function of the averaged epsilon) is supported by "at momentum transfers of a keV", which does not apply to the gap distribution. I kept that reading and shortened the sentence (row above).
- **ch16 ch16.tex:2 "the dark-photon rate on a glass is its measured loss tangent"**: this is a physics statement, not a wording problem. It is a proposed erratum (below) and I left the text unchanged. The names 'published form', 'total-eps rate' and 'local-field ratio' were checked: no "published rule", "published construction" or "true rate" is left in ch16.
- **ch17 'lattice ceiling' (s17-1:9)**: fixed. It is now introduced where it is used: "Below the lattice ceiling, the larger of $\omega_{max}$ for one phonon and $E_R^{max}$ for a free recoil, ...". The next two uses now say "the lattice ceiling" explicitly instead of "Above it".
- **ch17 tab:17-fom** cell "$L(q,\omega)$ in the window": changed to "in the kinematic window", the name that s17-5 uses (guard clean).
- **ch17 s17-6:31** "not ranked in the two nuclear channels": fixed to "not ranked in the two channels that need one, the heavy-mediator single-phonon rate and the nuclear edge". This matches the "Not ranked" column of tab:17-rank.
- **ch17 unified names** ('kinematic window', 'remainder', 'the two couplings'): checked. "remainder" in s17-4:87 is the separate object $\delta\tilde V_\kappa$ and is correctly kept apart from "the correction $O(q/q_{BZ})$".

## Proposed erratum (for the errata review)

- **Location:** tex/ch16/ch16.tex, line 2 (chapter opening).
- **Old:** "The dark-photon rate on a glass is its measured loss tangent, which changes seventeenfold between preparations,"
- **New:** "The dark-photon rate on a glass is proportional to its measured loss tangent, which changes seventeenfold between preparations,"
- **Reasoning:** the old text says that a rate (events per mass and time) *is* a dimensionless loss tangent. Sect. 16.7 says that the rate is fixed by two measured numbers, the low-power loss tangent and the permittivity (s16-7:94). The summary gives it as proportional to $\zeta^2\tan\delta_0\tanh(m_\phi/2T)/\varepsilon_r$. The factor 17 is the ratio of the loss tangents (3e-4 against 5e-3; s16-7:105, "raises it by 16.7"), so "proportional to" keeps the number and the claim correct. "is fixed by its measured loss tangent and permittivity" would also be acceptable.

## Recall (paragraphs the editors did not change)

The sample is about 1 in 7 of the unchanged prose paragraphs of more than 40 words in every file, chosen by seeded random draw, captions included. For ch15 I added five more unchanged paragraphs because the first sample was small.

| Chapter | paragraphs sampled | words | misses | per 1000 words |
|---|---|---|---|---|
| ch14 | ch14.tex:7; s14-1:120; s14-2:21,85; s14-3:18,153; s14-4:111; s14-5:99,120; s14-6:88,165; summary:11; prose cells of tab:14-nuisances (besides the open item) | ~1600 | 1 | 0.6 |
| ch15 | ch15.tex:9; s15-1:27,41,100; s15-2:20; s15-3:23,91,97; s15-4:38,40,96; summary:5; prose cells of the s15-4 nuisance table | ~1670 | 5 | **3.0** |
| ch16 | s16-1:58; s16-2:16,72; s16-3:59,110; s16-4:7,103; s16-5:17,62; s16-6:52,99; s16-7:3,13,78,173; s16-8:14,130; s16-9:37,52; summary:7; pointer-word grep of the prose cells of tab:16-inputs | ~1870 + cells | 1 | 0.5 |
| ch17 | s17-1:73; s17-2:29,62; s17-3:12,52; s17-4:53,101; s17-5:40,118; s17-6:7,27,35; summary:5; prose cells of tab:17-fom and tab:17-rank (besides the open item) | ~1900 | 0 | 0 |

I fixed every miss:
- s14-6:165 (caption): "Both curves follow" → "The Rayleigh and fixed-power curves both follow". "Both" picked from two earlier sentences.
- s15-4:38: "...29.7 or 56.4 eV. This is two hundred times ..., and 61 times less than k_F". "This" pointed to the smaller value in one clause and to the larger in the other (29.7/0.15 = 198; 3450/56.4 = 61). Now: "The smaller value is ..., and the larger is ...".
- s15-1:27: "this phase reproduces" had two candidates: the phase factor and the "phase operator" two sentences earlier. Now: "this choice of phase reproduces".
- s15-1:100 (caption): "all three agree" → "the three loss functions agree".
- s16-3:110 (caption): "Gray: both ratios within" → "Gray: the ratios for $qR = 3$ and 8 both within".

**ch15 exceeds 2 misses per 1000 words (3.0 in a sample of about 1670 words). That chapter gets a second pass.** ch14, ch16 and ch17 stay below the threshold.

Note for the ch15 second pass: s15-1:3 defines two edges, the *kinematic edge* $q = \omega/v_{max}$ and the *pair-breaking edge* $\omega = 2\Delta_{BCS}$. Bare "the edge" is used for both: the kinematic edge in s15-1:93,108,115,121, s15-2:16,20,55,57,75 and the s15-4 table caption; the pair-breaking edge in ch15.tex:4, s15-4:32,38,83,86,124,128,132,134 and summary:3,7. In s15-2:73 one paragraph uses both: "moves the edge" means the pair-breaking edge, and "the edge remainder" belongs to the kinematic edge. Also check s15-1:137 ("comes from the edge") and s15-3:136 ("would give the edge"). This is the "one name, two referents" risk of the calibration. I fixed only the two table cells that contradict their own caption.

## Checks

- `python3 tools/invariant.py 60cc72c tex/ch14/*.tex tex/ch15/*.tex tex/ch16/*.tex tex/ch17/*.tex`: 0 files with a stop (only notes).
- Lint on every file I changed: 0 blocking. The LONG-SENT warnings are in captions and tables that were long in the base.
- `tools/chapcheck.sh chNN /tmp/binding-review-vol2c-chNN`: exit 0 for ch14, ch15, ch16 and ch17, with 0 undefined references and 0 multiply defined labels. Overfull hboxes > 5pt: ch14 1, ch15 3, ch16 3, ch17 0; I did not check whether these were already present at the base.
