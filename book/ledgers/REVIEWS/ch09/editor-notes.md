# Ch09 editor notes

## Writer reports (pre-review)
### 9.1 (atlas table, opening)
- Table 9.1 has 24 rows × 6 columns, plus a sector column; 54 of 144 cells have a home. It differs from the SPINE in seven places, all following the accepted text (SEAM 9.1). Accepted.
- Q1, provisional ruling: give the cells that symmetry allows but no section computes (core spin flip, spin-coupled pair breaking, spin-dependent Migdal, Dirac spin) a distinct mark (e.g. "○", meaning allowed at leading order, not computed in this book). Cross-check them against tab:22-gaps. Reviewers should confirm.
- Q2 and Q3: the 10.2 acoustic peak is mentioned in the prose only; the free-recoil × e-density cell is empty. Reviewers to check.
- Q4: check that 16.8 covers defectons. If it does not, re-gloss the row.
- Q5: table numbering depends on float order; check the build.
- The build shows overflow in s9-2 (float 62 pt too tall, a 47 pt overfull box) and in s9-3 (13 and 10 pt). The writers or the reviser must fix these.
### 9.3 (q–ω plane)
- Fig. 9.2 uses cached data only and reproduces the book's own values. The section adds two tables to the plan: tab:9-overlaps and tab:9-supports.
- It follows the book over the SPINE: in silicon the phonon-assisted region (from 1.18 eV) does not overlap the multiphonon band, which reaches the gap only above about 212–247 keV. Interference is written as cross terms within one sector plus the Fano term, as in 8.6 and 17.4. Accepted. SPINE to be corrected at merge.
- For 3.25–4.96 keV the minimum pair energy is bounded above only, at 2.07 eV. Acceptable as stated.
- NiO band top 118 meV vs 14.2's 236 meV: reviewers to confirm that 236 = 2 × band top, and that the prose states the convention.
- WE 9.3 is direction-dependent. Reviewers to check against 13.6.
### 9.2 (kinematic map)
- General formula eq:9.2-mch, five cases, eq:9.2-halo scaling. Table 9.2 takes each edge from its home section; Ge 0.32 MeV is labelled an estimate.
- Q3, ruling: three edges are new, computed and logged in fig9_1.log (Al acoustic 8.6 keV from the 0 K constants of 20.3; ZrTe₅ floor 6.72 keV; Si 2p 28.7 MeV). They may stay. A derivation reviewer must recompute them.
- Q2: NiO magnon edge 7.3 keV (14.1 text, tab:17-endo) vs 7.2 keV (NOTATION, SEAM 14.1). The tex governs; fix NOTATION at merge.
- Q1 goes to the light pass: s16-1 l.15 has ZrTe₅ pairs at 31 meV (old half-gap); the correct value is 23.6 meV. Part of LE-186.
### 9.4 (Limit Checks and 𝔗), Summary
- 75 Limit Checks in Ch10–17: 27 are on a 𝔗 component (many-body 12, lattice 6, anharmonic 3, Migdal 3, multipole 2, thermal 1) and 48 are off-label (long-wavelength 5, halo 9, DM-side 5, target-model 29). App F has 90 rows for these chapters. The script fig9_3.py reads the tex and generates tab9-3.tex.
- SPINE differences accepted: the title; the reading of a box is given in 9.4 because the front matter lacks it (consider a front-matter pointer at the final pass); app:F replaces F.1; file names s9-*.
- Q1: the classification calls (Markov–Krein band → anharmonic; 10.2 loss-function boxes → lattice; colour centres → lattice; the target-model group). Reviewers to check. Rerun the script if any call moves.
- Q2: the two F rows for 14.3a lack a 𝔗 placement. Add one at the App F completion.
- The summary was drafted while 9.2 was incomplete. The reviser must recheck it against final 9.2.
- Final-pass item: rerun fig9_3.py whenever a Part II box is added or moved (printed numbers come from main.aux).

## Rulings (Ch9 block), after five reviews
Verdicts: prose REVISE ×5, plus PASS for tab9-3 and the summary; readers a, b, c MINOR GAPS; derivation-1 and -2 found the algebra correct, every table number reproduced, and a few cells and classifications wrong.

- **R1 Atlas (tab:9-atlas).**
  - Fill the three wrong "—" cells: core × dark-photon absorption → 10.7; chiral × dark-photon absorption → 14.5; body acoustic modes × dark-photon absorption → 11.8.
  - Mobile-defects row → 19.6, and its gloss loses "defectons" unless a section treats them.
  - Single-phonon × e-density stays 11.2, with a pointer in the cell or note to the 10.2 acoustic peak.
  - Adopt a distinct mark (○: allowed at leading order, computed in no section) for the eight cells derivation-1 lists: core spin flip, spin-coupled pair breaking, spin-dependent Migdal, Dirac spin, phonon-assisted × spin, free recoil × e-density, dopants × spin, Frenkel × spin. Define it in the caption.
  - Count cells with a small logged script (figscripts/ch09/atlas9_1.py). Every count in the text and summary comes from its log.
- **R2 Ch22 gap table (narrow edit allowed).** Add ONE grouped row to tab:22-gaps in tex/ch22/s22-2.tex: the eight ○ cells, class unsized, missing step a calculation, section sec:9.1. Rerun gaps22_2.py and update every count in s22-1, s22-2 and s22-summary from its log (expected 74 rows; unsized 39; calculation 56). Change nothing else in Ch22.
- **R3 Section 9.2.**
  - Al edge: quote the fastest-direction speed ([111], 6.67 km/s at the 0 K density) as the other edges do. The edge stays 8.6 keV; fix the captions.
  - ZrTe₅ lightest mass: 7.1 keV along the slow axis, not 8.0.
  - Either place the random-coupling channels of 11.6 and the two-magnon channel of 14.2 on the map, or state in one sentence why the map omits them and what masses they reach.
  - Free-nucleus gap mass: 46.8 MeV with the reduced mass, used identically in 9.2, 9.3 and the summary.
  - Plasmon: use one dispersion throughout (the book's Ch10 form; the caption's 2.24 keV reproduces from it). Phase speed 9.2e-3 (3.5 v_max).
  - Free-recoil halo shift 3.1 %. fig9_1.py uses Ge q = 1898 eV so its log prints 0.420.
  - Explain the Si 2p "opening momentum" formula in one line.
  - Halo exponent > 2 only at a stationary minimum: state the condition.
- **R4 Section 9.4.**
  - "80 formulas in 75 boxes", consistently.
  - Reclassify 11.5c (Markov–Krein; correction 1/ξ skewness) → target model; 10.3a (electron gas → crystal, led by the gap) → target model; 12.4b (2⟨ω²⟩/ω_e²) → n_B, as 8.5 assigns. Rerun fig9_3.py and take all counts from its log.
  - App F: name the Limit Check in column 1 of the 23 boxed rows (all of Ch10, 11.1–11.2) in tex/appF/F-rows.tex (narrow edit), so 9.4's statement holds; otherwise soften it.
  - The summary's definition of a Limit Check covers off-label boxes.
  - "Every Migdal formula" excludes 12.6a.
- **R5 WE 9.1.** Three cells (10.9 plus two 17.3). Add dark-photon-mediated nuclear recoil and complete the nuclear-column count.
- **R6 Section 9.3 and physics wording.**
  - The GaAs Fano size cites 13.6's estimate.
  - NiO 4.54 meV is measured (fix tab:9-supports).
  - WE 9.3 [111] lies inside the window by 11 meV: say so.
  - Si direct gap: one value book-wide (use Ch3/Ch10's accepted number; the 3.4 vs 3.17 eV mismatch).
  - Cite "the published tables" in 9.3 or remove the phrase.
  - Explain why a phonon ≤ 15 meV suffices at the 0.3332 MeV onset, given the 1.1728 eV state.
  - Reconcile the three "free recoil" criteria (2.3, 4, 9 phonon energies), or name which applies where.
  - Correct the free-nucleus absorption argument (momentum mismatch at q ≈ ω).
  - "Closed" channels must agree with the atlas.
  - Gloss "dark Compton" correctly (10.8).
  - The NiO branch wording per derivation-2.
- **R7 Prose.**
  - Make the opening's second paragraph motivation, not an outline.
  - Remove process artifacts: the ZrTe₅ parameter-row bookkeeping, the "Status:" line in the Table 9.2 caption, 9.4's misprint assurance and "the box leaves out…" sentences.
  - Define g₃₃, g_c, ⟨ω⟩, δM_κ and q₀ at first use, or remove them; c → c_ν; ω_th defined for every channel; gloss the 𝔗 components in 9.4.
  - Use \cref for Appendix F in the title and summary.
  - Cut the five facts told 3–5 times to one statement plus pointers, and delete the three looped paragraphs.
  - Register: restore normal connectives; reduce "only" and "therefore".
- **R8 Notation (record in NOTATION.md).** m_min^ch, E_ch(q), q̄; the ○ mark; no bare m_min.
