# Chapter 19 revision (2026-11-06; brief briefs/reviews/ch19-revise.md)

Files changed: tex/ch19/ch19.tex, s19-1 … s19-6, s19-summary; tex/appD/D-45.tex; tex/appF/F-rows.tex (Ch19 rows); narrow edits in
tex/appE/E-11.tex, E-23.tex, E-25.tex; NOTATION.md (Ch19 block, clash entry 91). Scripts rerun: bal19_5.py (rewritten calibration
part), def19_4.py (Part B rewritten, limit19_4b removed), lind19_3.py (exponent scan added), bethe19_3.py (Ī lines), rec19.py
(period, polar angle, P_Mig, ZPE, Migdal edge), limit19_6b.py (R₀), map19.py (Limit Check tags). Logs: figscripts/ch19/*.log.
Figures regenerated: fig19_4, limit19_5a, limit19_5b (now two panels), limit19_3a, fig19_3, limit19_3b, limit19_4a, limit19_6b, map19.
figures/ch19/limit19_4b.pdf is no longer referenced (left on disk). No QE run.

## Substantive rulings (done first)

| Item | Status | How |
|---|---|---|
| R1 ε_eh/ε_cal | done | bal19_5.py keeps g_Luke = eV/ε_eh (3.75 eV, Luke phonons) and g_cal = eV/ε_cal (3.82 eV, CDMS scale and subtraction). eq:19.5-identity, -calib, -first, -bound, -widen, -linear and D.45 (identity, linear form, first order, bound, widening, two-bias Cramer, limits) rewritten with both gains; sympy checks (a)–(h) in the log, 2×10⁵-point scan under (a)–(e). The "does not depend on ε_eh" clause is deleted. New numbers (log §3–5): pair-energy offset −0.0064 at 4 V; stored alone 0.042 (edge 0.049); collection alone 𝔯 = 1.128 (band 1.099–1.152); half mixture 𝔯 = 1.064; two-bias at 40 V 0.919 / 0.947 / 0.932, difference 0.028 = 3.6 half-widths, ±0.005 → 𝔯′ ±0.020–0.025, high-bias limit 0.912; C_cal 0.651 (4 V), 0.382 (40 V), 0.62–0.74 over 10–100 keV; first order ≤ 3.0×10⁻³ for deficits in [0, 0.05]; widening 0.042/0.058/0.075 at 𝔯 = 1/0.95/0.9 (95 % bound 0.081 at 0.9); gap offset ρ_g − 1 = 0.21 (0.0037 per 0.02). Bound stated with fifth condition (e) ε_eh ≤ ε_cal (0.055) and the book-ε value 0.049. |
| R2 y_C | done | f_ion = y_C(20 keV) = 0.324 (Eq. (4) of 1803.02903, a = 0.247 keV⁻¹), 75 % relative to y_C (0.75 × 0.497 = 0.373 → 0.956); Lindhard 0.346 given as the variant (𝔯 = 1.134, stored 0.0422). One script (bal19_5.py) holds every 𝔯 value; def19_4.py no longer computes any. Damage fractions 1 − y_C (0.731, 0.503) used for Table 19.1. |
| R6 structure | done | 19.4-calib now holds the two data sets and the definitions of Y_ph/f_DF in words, pointing to 19.5-yield; eq:19.4-fDF, eq:19.4-bound, the C_cal paragraph and the (a)–(d) list are removed from 19.4. The bound, its widening and conditions (a)–(e) live once in 19.5 (description list); Table 19.1 caption points there. Limit Checks 19.4b and 19.5b merged into lim:19.5b ("Stored energy from the phonon-yield ratio", panels: Y_ph and the 95 % bound vs 𝔯_coll, with the ε_cal = ε_eh curve and the Ge point); 19.4 keeps lim:19.4a only (Limit Checks now print 19.1–19.7; map tags updated). 19.6 quotes the bounds with their conditions and the 𝔯 = 0.9 value, adds the grown-in/frozen-in defect term E_st,0 to eq:19.6-leebound, and states the mounting assumption. Ge: 0.3 is the observed surface yield (lower edge), T_d/E_R ≤ 0.7, so the 0.23 entry is "≥ 0.23, not conservative" (0.27 at 0.6); Pb in Ge outside the self-recoil form. |

## Other rulings

| Item | Status | How |
|---|---|---|
| R3 Lindhard band | done | 19.3: band presented as a sensitivity; exponent scan −11 / +13 / +40 % at 1 keV (0.30 / 0.363 / 0.40; lind19_3.log, +39.7 printed as 40); ε^{1/6} law tied to the x^{1/3} continuation; Thomas–Fermi x^{1/2} tail keeps y_L finite; "whole cross-section continued below ε_L = 2×10⁻³ (≈ 80 eV)". Limit-box sentence softened ("comparable to the sensitivity"); nuisance row, summary and F row corrected. |
| R4 WE 19-lnI | done | 174 eV variant and "L shell 2/3, valence 1/6" removed; Ī = 161 eV, 7 % below the adopted 173.0 eV (PDG atomic table), rescaling invariance stated; 61 %/28 % oscillator strength; valence-only 19.5 eV. bethe19_3.log prints the unit-dependent variant as "not used". Franta/Henke re-description replaced by a pointer to 10.7. Editor-note claim "L shell 2/3" withdrawn (summary and F row fixed). |
| R5 numbers | done | free-gas fraction vanishes at 336 eV (text, Fig. 19.2b caption); period 65 fs (19.1 WE, E.11 ×2; rec19.log 64.5/65.0 fs); 1.6° per transverse component, 2.3° polar (rec19.log); 1.9 % at 500 eV with exact bracket (19.1; rec19.log); Migdal 2.3–4.4×10⁻⁴ with the energy-only/full-band remark (19.2, summary, nuisance, F row); ZPE 61 meV per atom, ΔE_zp ≈ 0.07 eV, sign stated (either), bound for either sign 0.056/0.065; 2U: "vanishes near 2U … with the fitted correction terms 298 eV"; f_ret = 0.525 → 1.156; 0.020–0.025 (was 0.02); 58 µs (p. 2 of 2007.14289); Si M: Ch19 uses the natural mixture 26.16 GeV throughout, now labelled ("natural isotope mixture, as in 5.3"), consistent with 5.3/5.6/11/12; Ch1/8/C.6/D.13 use ²⁸Si 26.06 GeV (book-wide note below); U_FP called "Frenkel-pair creation energy" by its authors, a threshold average, three times the 6.8–9.7 eV configurational energy; 19.6 electron recoils "below 0.14 MeV"; R₀ = a(3V₀/Δ)^{1/4} from the stated gradient criterion, 12–22 spacings (limit19_6b.log; source form printed as a variant); 19.4 C_cal sentence removed with the machinery (19.5 has the correct sign); flashing defined (infrared exposure that neutralizes ionized traps, Sect. 2 of 1803.02903); ω_p → ω_acc; "bracket" → "D/D_9 expands". |
| R7 prose | done | 1.144 sentence, "two-standard-deviation edge" sentence and the g_L parenthetical removed; count announcements named (19.1 l42, 19.3 l80, 19.4 Ge, 19.5 conditions/offset/handles, 19.6 sum rule, families, four facts, three effects, consequences, hypotheses, regimes); four-verb outline sentences cut in 19.2–19.5 openers (19.3–19.5 end on the question with one "we will"); repeats cut (threshold ≠ stored in 19.4/19.5, tunnelling in 19.4/19.5, "one table" in 19.4, friction in 19.1, E.23 pointer in 19.2, Lindhard-as-partition in 19.1, 0.72 eV in 19.4, 23.6 in 19.6 opener/open problems); empty paragraphs removed (19.2 l109, 19.6 l186/l190 reduced to one pointer sentence/cut, 19.1 l134 trimmed); "lattice heat" → "heat" (opener, 19.1 l9, E.23); condition lists split (19.5 description list); provenance chains as "as quoted by" (Nordlund, Sarkis ×2, Sorensen) and the Vutha/Sarkis convention notes reduced to citations; D.45 retitled "Energy balance and calibration algebra". Register: "however" added (19.1, 19.2, 19.4, 19.5 ×2, 19.6), "we will/we can" (19.1, 19.2, 19.3, 19.4, 19.5, 19.6), several "so"/"gives"/"only" chains replaced by "since", "as a result", "leads to"; "only" in 19.5 from 53 to 2 per 10k. Lint: 0 blocking; remaining warn hits are long sentences in captions/tables and the known EQ-PUNCT false positives. |
| R8 notation | done | g_Luke (visible rename; only Ch19, D.45, F rows used the symbol; E.12 uses the words); g_cal, ε_cal new. Doubles resolved: x → χ_g (gap multiplier), e → e_st, b(t) → f_ret, bare ϵ → ϵ_abs, ω_p → ω_acc, p → n_q, ⟨q²⟩ → Γ_k², E_φ unified, Z → Z_κ in 19.3, bare ℓ (path) → x in 19.3, D.45 s → k_cal; also Y, σ → Y_mod, σ_str (19.6). NOTATION: ~70 new symbols in 12 new rows plus revised rows (C_cal, Y_ph first use, f_DF, p_FP row's E.23 note); clash entry 91. check_notation (ch19 + D-45): 9 residual tokens, all Δ-split names, the joint subscript d_NR,ER or WE-local labels (listed in entry 91). |

## Report items not covered by a ruling

| Report item | Status |
|---|---|
| deriv-1 50 eV EPM point near the basis cutoff | done (plane-wave cutoff named in the understatement clause) |
| deriv-1 Born parameter screening | done (unit charge already exceeds one) |
| deriv-1 "the same electron gas" = Mermin | done |
| deriv-1 NOTATION missing rows 19.1–19.3 | done (entry 91) |
| deriv-2 Sassi range "up to 200 eV" | done ("up to a few hundred eV"; Fig. 1 axis runs to 500 eV) |
| deriv-2 WE 19.4 "logarithmically" | done (linear in ln Y against ln E) |
| deriv-2 two-bias hypotheses (ε) | done (same ε_cal at both biases, ε_eh known) |
| deriv-2 19.6 "below one spacing … half" | done ("well below", half near 0.4 a_ch; limit19_6b.log 0.48) |
| deriv-2 condition (c) gloss | done ((1 + f g_cal)/(1 + g_cal), the C_cal value at 𝔯 g_Luke = g_cal) |
| prose C8 Sarkis naming; "Ref.~\cite" nouns; Lindhard 1963 credit in lim:19.3a | done |
| prose C9 percent style | done |
| prose C10 seam 19.2→19.3 (1.5 twice), 19.3 ending on scope note | done |
| prose C11 Bethe motivation; Franta pointer | done |
| prose 19.6 max-entropy paragraph as subsection end | done (moved before the scaling paragraph; subsection ends on "no free parameter") |
| prose captions (lim 19.3a x-axis; lim 19.4b admission) | done / box removed |
| prose summary: double-counting rule, "nonperturbative", "tenth of an atomic mass" | done |
| reader-a "Migdal yield per recoil" | done ("number of Migdal pairs per recoil") |
| reader-a/b Ehrenfest, surface hopping, multireference, NEB, KMC, athermal sensor glosses | done |
| reader-b PN barrier formula in 19.6 | done (C.20 formula restated) |
| reader-b first-order "between 0 and 0.05" | done |
| reader-b two "1.49 Å" | done (cage amplitude vs closest approach) |
| reader-b t_pr in Fig. 19.1 caption before definition | done (points to 19.1-partition) |
| reader-b 0.8 vs 0.70 in Table 19.1 | done (both columns: 0.8 and, in parentheses, 0.70) |
| reader-a 0.78 at 2.9 eV (0.777) | unchanged (rounds to 0.78) |
| reader-a S_pol defined in an appendix | unchanged (pointer to E.22 kept; one-line gloss would need a new symbol definition) |
| deriv-1 Ch12 s12-1 l133 "3 % at 500 eV" | not in scope (Ch12 file); listed below |
| Editor note: Limit Check numbering | checked: limitbox is numbered within the chapter in every chapter (preamble), so Ch19 prints 19.1–19.7; no change needed |
| Editor note: thomas1925zahl as TF | Ch19 cites thomas1927calculation/fermi1928statistische; other chapters not checked here (listed below) |

## Build

`latexmk -pdf -outdir=/tmp/claude-0/build-ch19rev main.tex`: exit 0; 0 LaTeX errors, 0 undefined citations; 59 undefined references, none to a Ch19 or D.45 label (forward references elsewhere in the book). No overfull boxes in the Ch19 files.

## Changes owed in the campaign ledgers (not edited here)

**state/CORRECTIONS.md**
1. Ch19/WP calibration chain: the CDMS II Si reconstruction adopts ε_cal = 3.82 eV for both phonon scale and Luke subtraction while Luke phonons follow ε_eh = 3.75 eV (DC-67: 3.7468). Superseded: 𝔯_coll = 1.154 (and 1.144), "stored energy alone gives 0.952 at both biases", "two readings differ by 0.033", stored-only 0.048 as the r = 1 reading. Current: stored alone 0.042 (0.049 at the 95 % edge), 𝔯_coll = 1.128 (1.099–1.152; Lindhard f_ion 1.134), 40 V: 0.919 / 0.947 / 0.932, difference 0.028; offset −0.0064 at 4 V.
2. f_ion for the CDMS II Si datum is y_C (0.324 at 20 keV, 0.269/0.497 at 10/100 keV), not Lindhard (0.346); the source's 75 % collection is relative to y_C.
3. Stored-energy bound: 0.055 (Si) needs a fifth condition ε_eh ≤ ε_cal; 0.049 with the book ε; 0.056/0.065 for either sign of ΔE_zp; Si 0.081 at 𝔯_coll = 0.9 (was 0.086).
4. p_surv E_FP/E_d readings: Si 0.19 (10 keV) / 0.27 (100 keV) with y_C damage fractions (was 0.20/0.28), 0.21/0.31 with ξ_d = 0.70; Ge ≥ 0.23, not conservative (T_d/E_R ≤ 0.7); close pairs p_surv ≤ 0.90–1.00, separated ≤ 0.70–0.84 (was 0.95–1.04 / 0.73–0.88); 300 eV extrapolation 6.6 % (was 6.9 %).
5. ρ_g − 1 for the whole silicon deficit: 0.21 beyond the pair-energy offset (was 0.24/0.254); E.25 edited.
6. Zero-point energy per Si atom 61 meV (31 meV is the potential half); ΔE_zp per point defect ≈ 0.07 eV, either sign.
7. Si mean excitation energy from the measured loss function: 161 eV; the 174 eV "exact f-sum" variant and the "L shell two thirds" share are unit-dependent and withdrawn (editor note on 19.3 withdrawn).
8. Lindhard soft-collision "13 % band" is a sensitivity: −11/+13/+40 % at 1 keV for exponents 0.30/0.363/0.40.
9. Ch12 s12-1 l.133: "3 % at 500 eV" is the soft-limit value; 1.9 % with the exact bracket (owed at the next Ch12 pass).
10. Shortest Si phonon period 65 fs (E.11 corrected; any other 67 fs, e.g. in SEAMS or SPINE, to follow).
11. Defecton localization radius R₀ = a(3V₀/Δ)^{1/4} from the gradient criterion (12–22 spacings for the crowdion), not Pushkarov's Eq. (20) form (18–43).
12. Migdal part of the measured Si yield: 2.3–4.4×10⁻⁴ (model-free edge to one-sided split).
13. Sarkis et al. 2022 U_FP = 23.6 eV is a threshold average ("Frenkel-pair creation energy"), not a formation energy.
14. Book-wide Si nuclear mass: ²⁸Si 26.06 GeV in Ch1, Ch8, C.6, D.13; natural 26.16 GeV in Ch5, 11, 12, 19. Ch19 labels its choice; a book-wide ruling is owed (effect ≤ 0.4 % on threshold masses).
15. Luke gain symbol g_L → g_Luke (book-wide; only Ch19, D.45, App. F used it).

**state/SOTA.md**
- IF-E8: keep 0.055/0.064 but add condition (e) ε_eh ≤ ε_cal, the book-ε value 0.049, and 0.056/0.065 for either ΔZPE sign; 𝔯_coll(collection only) 1.128; Si bound 0.081 at 𝔯 = 0.9; Ge p_surv-bound "≥ 0.23, not conservative".
- Binary threshold entries (l.111, 251, 302, 349): 352/395 eV → 352/399 eV (336/387 eV with v_N²).
- Two-bias proposal: 40 V readings 0.919 vs 0.947 (difference 0.028).
- Lindhard soft-collision sensitivity as in CORRECTIONS 8.

**LOOSE-ENDS**
- Sect. 20.5-sign now carries the sign of 𝔯_coll − 1 (19.5 points to it); the detector-specific number for the CDMS II geometry and ρ_g remains with App. E.25.
- SPINE: 19.1 title ("Nuclear recoil on the Born–Oppenheimer surface"); LO(i) and E.23 395 → 399 eV; 19.6 "T below the band width" → T ≥ 0.28 band widths; collection ratio 1.144 → 1.128.
- Check other chapters that cite thomas1925zahl for Thomas–Fermi screening.
- check_notation.py splits Δ-prefixed names (ΔE_zp, ΔF_LZ) and joint subscripts (d_NR,ER) into false gaps; teach it or file-key them.
- Any future calibration that subtracts Luke phonons with an adopted ε should carry g_cal ≠ g_Luke (Ch20 readout chapter).

**NOVELTY**
- Book-phase finding: the CDMS II silicon phonon-yield ratio carries a pair-energy offset (ε_cal = 3.82 vs ε_eh = 3.75 eV) of −0.0064 at 4 V, an eighth of the measured deficit, which grows tenfold at 40 V; the stored-energy bound needs ε_eh ≤ ε_cal and tightens to 0.049 with the measured ε.
- The Lindhard ε^{1/6} law is a property of the x^{1/3} continuation; the Thomas–Fermi tail gives a finite y_L as ε → 0 (presented as a remark, not a claim of novelty unless the editor finds no source).

**DEFERRED-COMPUTE**
- No new deferred runs. The transport calculation of App. E.25 now also needs the reconstruction's adopted pair energy as an input (note only). All F-row Fsize entries of Ch19 are sized.

## Coordinator item (Ch20 hand-over)
- 19.5 condition (b): the "transport puts 𝔯_coll at or slightly below one" sentence is replaced by one clause pointing to \cref{sec:20.5-sign}: 0.935–0.998 with sub-gap Luke phonons lost, up to 1.04–1.09 through the film yield near threshold (2Δ–4Δ), so the sign is not fixed by transport alone. Matching edits in 19.4 ("which transport gives when sub-gap Luke phonons are lost"), 19.6, the summary and the App. F row. The campaign toy range 0.87–0.98 appears nowhere in Ch19.
- Collection-only value now in 19.5: 𝔯_coll = 1.128 (band 1.099–1.152; Lindhard variant 1.134), i.e. Luke phonons collected 13 % better than the primaries; 20.1's "about 13 %" is consistent.

## Post-check fixes (postrev-check.md, ACCEPT WITH FIXES)
1. 19.5 condition (b): 1.04–1.09 now attributed to the pair-breaking threshold of a second, higher-gap film (about 3 meV) in the two-film geometry of \cref{sec:20.5-sign}, not to the Al yield between 2Δ and 4Δ.
2. 19.5 WE (collection alone), summary and nuisance row: 𝔯_coll = 1.128 (band 1.099–1.152) lies above the largest transport value of 20.5 (1.09); collection alone is "disfavored on present (transport) estimates", conditional on 20.5.
3. E-23: 395 → 399 eV (two places).
4. NOTATION.md: E.12 row and entry 55 now name g_Luke.
5. 0.049 worded as the bound under (a)–(d) with ε_eh = 3.75 eV, attained at 𝔯_coll = 1 (19.4, 19.5, summary row, F row).
Optional items done: (e) for Ge refers to the Ge analysis's adopted pair energy, not evaluated (19.5 list); the Lindhard attribution follows the source ("overestimates the low-energy data that analysis cites", plus its ~5 % remark, covered by the Lindhard variant); r′ shift printed as 0.020–0.026 (19.5, F row).
Rebuild after the post-check fixes (/tmp/claude-0/build-ch19rev): latexmk exit 0, 0 LaTeX errors, 0 undefined citations.

## Ch19 amendment (2026-11-06; Ch20 R1 rework, ledgers/REVIEWS/ch20/postrev-check-2.md ACCEPT)
Text from the "Exact Ch19 pointer text" of ch20/revision.md, adapted to each location.
- s19-5.tex l.151 (condition (b)): "0.935 to 0.998 … can raise it to 1.04–1.09, and a sensor … removes the loss" → sign
  not fixed by the balance law; mean-field estimate 0.81–1.02 (0.82–1.01 at the mean Luke energy of Si electrons at
  1 V/cm), one or two films down to 60 nm, energy conserved; up to 1.5 only for a selective sink not identified in a detector.
- s19-5.tex l.193 (collection alone): "above the largest transport value 1.09 … disfavored" → band 1.099–1.152 / 1.134
  first, then 0.81–1.02 with energy conserved; 1.128 not reached by the transport estimate, not excluded until computed
  kernels test real detectors (app:E.25); the two-bias measurement of sec:19.5-inversion decides.
- s19-5.tex eq:19.5-bimol and l.80: track time t_0 → t_rel (6 occurrences; t_0 is the pair-breaking time of 20.3/20.4).
- s19-4.tex l.90: "which transport gives when sub-gap Luke phonons are lost" → "where the mean-field transport estimate
  lies in most configurations (0.81–1.02, sec:20.5-sign)".
- s19-summary.tex l.9 (text) and l.33 (nuisance row): "above … 1.09, disfavored" → not reached by the mean-field estimate
  (0.81–1.02 with energy conserved; up to 1.5 only for a selective sink), not excluded until computed detector kernels;
  the second bias decides.
- appF/F-rows.tex Ch19 row (l.800): "0.935–0.998 … up to 1.04–1.09" → the band, the selective-sink clause and the
  conclusion. (Ch20 rows l.898/899: conclusion appended; "+0.09" qualified as the deleted-phonon value.)
- s19-6.tex: no occurrence. Grep of ch19 for "disfavo", "1.09", "0.935", "1.04", "0.998", "t_0": none left (1.099, 1.047 unrelated).
Ledgers: state/CORRECTIONS.md (pending row → final statement; rows 656/657 conclusion updated; new row on the first-pass
film-escape values), state/SOTA.md (Ch19 calibration note; pending notes → final band).
Build /tmp/claude-0/build-amend: latexmk exit 0, 0 LaTeX errors, 1706 pages.
