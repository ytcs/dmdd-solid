# Ch13 editor notes
## From the 13.1 writer
- GaAs has its own phonon-assisted-only window, 0.433 MeV to 0.517–0.560 MeV. The research note's 0.51 MeV used an L-valley energy of 1.71 eV; the book uses 1.815 eV. 13.9 reconciles the two.
- Q* intermediate values differ between E.14 (14.72 meV at 0.510 Å⁻¹) and 13.1 (14.79 meV at 0.53 Å⁻¹); the onsets agree. Align the lattice constant and scaling rule at review, or in App E pass 2.
- map13.py hard-codes the Limit Check numbers. Rerun it after Ch13 is complete.
- The Si zero-phonon threshold along the valley axis is printed only as an upper value (0.420–0.425 MeV); the joint minimum goes to 13.9. The Ge zero-phonon edge is still unknown (DC-2).
## From the 13.3 writer
- 13.3 assumes the window margin δ_w = 0.3 eV; 13.6 must confirm it, since the bounds 0.31 Å⁻¹ and |q| ≤ 1.33 keV depend on it.
- Zero-phonon edge at 1 keV: 0.60 eV above the gap from the 48³ PBE bands, against 0.73 eV from the parabola. Keep both, labelled.
- Pair mass: 13.1 and 13.3 use 1.19 mₑ, 3.3 prints 1.2. Fine as rounding; state 1.19 where it is used.
- D-35 holds overfull boxes in the 13.2 writer's part (l.34–38, 74–75); fix at review if 13.2 doesn't.
## From the 13.5 writer
- Only the TA:TO 5.5:4.0 ratio is sourced (Rajkanan, via Stanford); the edge model uses one scale fitted to Franta 300 K. Get Rajkanan's other coefficients if they can be had.
- Stanford's branch strength is temperature dependent: the 77 K factors become 2.3/1.7/1.3/1.1 (crossing 18 meV) against 2.6/1.9/1.5/1.3 (23 meV). Decide which to print, or print both as a band.
- Cold threshold: 1.1875 eV (E_g(0) = 1.1692) vs 6.5's 1.1883/1.1736; align at review. Transferring the 300 K data leaves a spurious ≈1.4 cm⁻¹ absorption below the edge; state it.
- "TA-only is an upper bound" holds only to two digits (1.48 vs 1.47 at 50 meV); soften the wording.
## From the 13.6 writer
- δ_w = 0.3 eV CONFIRMED: every controlling ratio is ≤ 0.21. The |q| bound is 1.33 keV for parabolic valleys and 1.27 keV from the computed bands; label both.
- Light pass on 8.5: it says θ_ep reaches 1 at 0.25 eV and calls θ_ep ≪ 1 "the window", which conflicts with 0.3 eV taken literally. Reword it to match 13.6.
- SPINE says the GaAs Fano map is in E.26; it is in E.14 (13.6 cites E.14). Fix SPINE.
- App E pass 2: E.17 l.13 should point deformation tensors to 13.6/D.37, not sec:11.3.
- The Si pair widths are a deformation-potential estimate (Li et al., Table III). If their density of states is per spin, the widths halve and the conclusion holds.
## From the 13.4 writer
- Light pass on 8.8: it says the pair-channel size is "computed only in 13.4", but 13.4 gives only the two solvable limits (rate factor 0.07–0.12 vs about 1) with the sign not derived. Repoint 8.8 to App. E.16 and the deferred calculation.
- App E pass 2: E.14 writes the pair momentum as bold P, which collides with polarization; E.16 uses bare Λ for the screening ratio, which collides with the final-state class. Rename both.
- Convention from 13.4 on: L^PA and ε₂^PA denote the screened quantities; 13.3's are the independent-particle values. Check that 13.5 follows this; update NOTATION at the merge. New glyph ς for the second-order source.

## 13.8 drafted (2026-11-06; ~3,570 words; build clean; lint 0 blocking)
- E.15 l.35 says the 13.2 band sum "uses intermediate states with two pairs"; this contradicts 13.2 (one pair per intermediate state). Reword E.15: two-pair states enter via the interaction beyond Tamm–Dancoff (as in 13.8).
- Cold excitonic edge: 1.1736 eV (6.5, 10.7; E_g = 1.17) vs 1.1728 eV (13.5's E_g(0) = 1.1692). 13.8 prints both with one reconciling sentence; align book-wide at the Ch13 review.
- Known shortfalls of the 300 K one-scale fit are stated in the text. The cold check rests on Stanford et al.'s 0.5 K figure, with 1.2 eV a 6 meV extrapolation below their lowest diode energy.
- NOVELTY N7: 2106.12586 Sect. V (Eq. 72) already has phonon-assisted kinetic absorption, intraband, in a superconductor. Prior art credited; the claim is narrowed to the interband edge of an insulator. Update state/NOVELTY.md N7.
- The ALP singlet–triplet difference is unsized: a candidate row for the 13.9 nuisance table.

## 13.9 drafted (2026-11-06; ~6,480 words incl. ~1,200 summary; nuisance table 22 rows; build clean)
- Editor items (a)–(d) closed in text. GaAs 0.43 → 0.52–0.56 MeV (E_L = 1.815 eV).
- New keyresult eq:13.9-medge: the onset exponent in mass is p_on + 7/2 (13/2 independent pairs; 6 excitonic continuum; 5 replica).
- VERIFY: the 1.71 eV room-temperature GaAs L energy is attributed to Vurgaftman et al. from recalled Varshni parameters. Check the locator or delete the sentence.
- E.14 l.62: Ge heavy hole "more anisotropic" is wrong per the CW1 errata (it is less warped; nothing transfers from Si). Fix E.14.
- Recheck the 13.7/13.8 summary paragraphs against the final s13-7/s13-8.
- CONFLICT: 13.7 gives the nonadiabatic ZPR correction as 8 meV; SPINE/research say ≲ 2 meV (window effect ≤ 0.002 MeV). 13.9 follows 13.7. Resolve at review.
- 13.7 Fig caption has the joint minimum at 1.29 keV (Wannier, no SOC); 13.9 prints 1.33 keV (SOC, re-minimised). Align.
- Glide parities on axis (light hole odd; heavy-hole pair even + odd) are inferred. A derivation reviewer must confirm.
- Rerun map13.py now that 13.7 exists.

## 13.7 drafted (2026-11-06; ~3,650 words; Limit Check 13.7a in a model crystal; 2 F rows; build clean)
- ZPR conflict RESOLVED: the nonadiabatic correction is 8 meV (Poncé et al. 1504.05992 Table VI: −64.3 adiabatic vs −56.2 nonadiabatic; 6.0 meV VBM + 2.1 meV CBM). This matches 6.3 and E.8. CW1's ≲ 2 meV used a 0.12 eV vertex; 9 meV (Miglio) mixes methods. The window bound ≤ 0.002 MeV still holds, because the window uses the measured gap. TODO: update SPINE 13.7 LO(iii), the SPINE limits row CW1-L9 and state/CORRECTIONS to 8 meV.
- The q joint minimum is aligned to 1.33 keV. New 300 K values: ZP edge 0.397–0.400 (best 0.399), 1s 0.394–0.397, onset 0.3243 MeV; window width 0.0742 MeV; frozen below ~20 K. Check that 13.9 does not contradict these.
- Limit Check 13.7a uses a model crystal (no Si supercell series in the sources). Rerun map13.py.

## Ch13 review rulings (2026-11-06; five reports: derivation-1/2, prose, reader-a/b — all MINOR GAPS / REVISE, no REWRITE)
- R1. Summary: the external screening factor is the macroscopic 1/30–1/38 (13.4), not the head-only 1/40–1/48 (flagged by 3 reports).
- R2. Interim factor [0.4, 1.8]: its inputs (pair ≤ ±0.5, unsigned LF ≤ ±0.2) are contradicted by 13.4's derived pair-channel limit 0.07–0.12 and signed LF +25–31 %. Redefine it as the correction relative to the rate normalised to the measured optical edge, which already contains the pair channel at q = 0. Rebuild its range in a script (figscripts/ch13/interim13.py) from 13.4's derived pieces, with every assumption stated. Adopt the rebuilt range in 13.4, 13.9 (text, Table 13.1, nuisance table), E.14 and E.16, and keep it tagged as an estimate. If no defensible range follows, print the derived components and call the remainder an unsized nuisance.
- R3. GaAs 1.71 eV sentence (13.9): DELETE. The attribution cannot be checked (Vurgaftman is closed access).
- R4. WE 13.2 two-band chain: the numbers are right (derivation-1 brute force, 924 states), but the text must state the twist (~0.31 rad) and the phonon-vertex phase convention, and say that the other convention gives 1.6 instead of 2.4. 13.8's quote of the factor names the convention.
- R5. Cold Si absorption data: 13.8 (Stanford 0.5 K) and 13.9 (Macfarlane) differ by ×2 at 1.25 eV. Use the 13.5 dataset as primary in both, quote the other as the spread, and add a nuisance row. Align the cold excitonic edge to one value book-wide (1.1736 vs 1.1728), stating the E_g it uses.
- R6. Remove production-status wording ("interim", "computed once", "has not been run", "derived here", "to our knowledge"). State status in the book's public vocabulary only (STYLE/PARTII); the table status labels follow the same rule. 13.7 must not rebut an estimate the book never states: present 8 meV positively.
- R7. 8 meV split: 6.1 meV VBM / 1.9 meV CBM (Poncé Table VI: VBM 40.87 → 34.75, CBM −23.28 → −21.43). Fix the text and fig13_7.py.
- R8. Table 13.1: the upper end 0.420 of the second heavy hole is an estimate, so tag it. The GaAs row keeps the book value 0.43 → 0.52–0.56 MeV (E_L = 1.815 eV); the coordinator updates CORRECTIONS and CONTROLS.
- R9. |q| bound: 1.33 keV (parabolic) and 1.27 keV (computed bands), labelled everywhere; δ_w is defined at first use in 13.3 by forward \cref to 13.6. Two-branch vs TA-only factors are labelled (13.5, 13.8). "Halves |M|²" applies to one sign of Q only.
- R10. Appendix fixes: E.14 l.62 (the Ge heavy hole is less warped; nothing transfers from Si); E.15 l.35 (13.2 has one pair per intermediate state; two-pair states enter via the interaction beyond Tamm–Dancoff).
