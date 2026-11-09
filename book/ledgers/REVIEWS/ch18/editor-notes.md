# Chapter 18 editor notes
- Duplicate label fig:18-limit-a exists in two Ch18 files (parallel writers). Rename at review.

## 18.1 drafted (2026-11-06; ~3,940 words; D.43 ~1,540; Part III heading, Ch18 opening, map)
- D.43 written entirely by 18.1 (incl. ε_eh/F_eh as moments, the 𝒱_<, 𝒱_>, 𝒱_<> decomposition). 18.2 cites eq:D.43-moments/-decomp; unify the heat symbols (E_heat, E_<, E_>).
- Model numbers (random-k, A_AB = 5.2, E_g = 1.17): "two or three pairs", 13 pairs/35 eV. Label them as model at review.
- Si plasmon 16.4 eV (4.8) vs 16.6 eV (E.13, E.24): align book-wide (light pass). E.24 vs campaign (WP5, GAP-EF) disagree on the random-k error near threshold: 18.5 holds it as open.
- Kane 1967 cited "as quoted by" Kotani–van Schilfgaarde.
- PRIORITY derivation: eq:18.1-ii (the impact-ionization kernel as the master formula with anti-Hermitian W^scr), θ_ii = (2m_e*+m_h*)/(m_e*+m_h*), the LO double-count matching conditions, the backward equation and the energy identity, and the seed split (2.997 vs 2.712 at 10 eV).
- Rerun map18.py once 18.2–18.4 boxes are fixed.

## 18.5 + summary drafted (2026-11-06; ~3,270 + 1,410 words; tab:18-nuisances 16 rows; fig:18-end)
- Key result eq:18.5-Eg: each captured electron raises the non-pair energy by exactly E_g (heat / trapped electron / unpaired hole). Binomial thinning ε/(1−f), (1−f)F + f. A 0.56 % loss alone explains cascade F 0.114 vs measured 0.119. Heat-based Fano F(1 − E_x^b/E_g)² (−2.5 % Si, −1.3 % Ge). Unsplit excitons: F_meas = (1−p_ns)F + p_ns; field separation radius r_𝓔 = 0.56 µm at 4 V/cm. PRIORITY derivation.
- Fig. 18.4 rates are illustrative (no open mK sources), except the 200–300 ns bound-exciton Auger lifetime (as quoted by Lo et al., from Schmid 1977).
- ε_s: 11.4 (liquid-He, from 7.4) vs 11.7 (4.9 exciton). Align book-wide (light pass).
- The summary was drafted from partial 18.2–18.4 and omits 18.4's linear law (1.61E_g + k₂): recheck at review.
- The lint flags labels containing "ledger" (sec:18.2-ledger): rename.

## 18.2 drafted (2026-11-06; ~3,755 words; D.44 ~1,150; Limit Checks 18.2a–c; 4 F rows)
- Fano decomposition at the book gap 1.160 eV: 0.092 + 0.291 − 0.269 = 0.114. SPINE and s18-summary l.5 print 0.091 + 0.288 − 0.265 (research value at 1.164 eV): use the book values.
- Limit Check 18.2a is plotted against ω/E_g (approach to the cascade moments) instead of the planned phonon-loss parameter (that is in Fig. 18.2). Rule at review.
- λ_AB, w_AB are defined in 18.2; 18.4 re-displays them (eq:18.4-reduced): point back.
- 0911.1532 misprints: ρ∞ 0.7475987 vs 0.747597920; renewal 0.0439766 → 0.04439766. Logged in an F row.
- Writer reported ceperley1980ground as corrupted; checked: the entry is correct (the reporter likely misread a neighbouring entry). No action.

## 18.3 drafted (2026-11-06; ~3,160 words; Limit Check 18.3a; 1 F row)
- WE 18.3 at 5 eV: the step model says 2 pairs always, while the cascade gives P(2) = 0.170 for a DM seed, so the step model overcounts by 5.9× above a two-pair threshold. Step within 0.1 TV only below 4.37 eV (up to 0.86 at 4.91 eV). Photon vs DM seed ≤ 0.062: this sizes the photon-calibration error left open in 8.7. PRIORITY derivation.
- Two Si parameter sets in Ch18: 18.1 (A_AB = 5.2, E_g = 1.17, Ramanathan–Kurinsky) vs 18.2–18.3 (5.674 eV³, 1.160 eV calibrated). Ruling at review: one set (the calibrated one), with 18.1 rerun (shift < 0.03).
- b_N for an all-on-one-carrier seed: 0.345 (18.2 log) vs 0.352 (18.3); the text says 0.35. Reconcile.
- Band seeds come from a 0.82 eV-gap EPM model, used at the same energy above the gap (stated).
- The fig:18-limit-a clash is resolved on the 18.3 side (now fig:18-limit-seed); 18.4 keeps fig:18-limit-a.

## 18.4 drafted (2026-11-06; ~3,840 words; Limit Checks 18.4a–c; Table 18.1; validated-range table; 3 F rows)
- Si Fano 0.114 vs measured 0.119: 2.5σ (book gap 1.160 eV; SPINE says 2.6σ from 1.164). Update SPINE/CLAIMS. Ge ε −5 %, GaAs −6 %.
- The Klein relation is derived as Shockley energy balance plus two assumptions; the uniform-population assumption overstates the phonon-free ε by 36–39 %; Klein is within 10 % of the cascade for λ_AB 0.65–84 (near Si by coincidence). PRIORITY derivation.
- Linear law ε ≈ 1.61 E_g + k₂ (k₂ 1.2–2.5 eV; 1.87 for Si): an observed fit.
- Validated range: residuals −6.6 to +24.5 % (rms 12.2 %) over seven crystals; λ_AB 0.007–14, w_AB 0.016–0.054. Halides, fluorides, lead salts and InSb lie outside, so their pair energies are estimates for 21.7.
- Second-hand measurements (GaAs ~4.2 eV via Nielsen–Fischetti; SiC, SiO₂, GaN) are attributed "quoted by".
- Pending: the R19 FBC full-band cascade may upgrade 18.1/18.3/18.4 after the Ch18 review. The review treats the energy-only cascade as the current result.

## Ch18 review rulings (2026-11-06; five reports: derivation-1/2, prose, reader-a/b — MINOR GAPS / REVISE, no REWRITE)
- R1. One Si parameter set, continuum-calibrated: A_AB = 5.703 eV³ at E_g = 1.160 eV (5.674 was a grid value ~0.5 % low). Recalibrate in one shared module (casc18_4.py or a new si_cascade18.py), rerun every Ch18 script, and update every printed number (decomposition 0.092 + 0.290 − 0.268 = 0.114; 2.5σ unchanged). 18.1 runs on this set (50 eV: ~13.00 pairs; p_ii = ½ crossing ~5.9 eV; 10 eV seed means shift < 0.03). Remove 18.3's reconciling sentence. The fit is derived once, in 18.4. 18.2/18.3 use it with a forward \cref and do not credit it to 18.2. NOTATION: A_AB in eV³ (R&K's eV² is their misprint).
- R2. b_N: subtract ω/ε with the grid's own ε. All-on-one-carrier 0.345; uniform split 0.008 (not 0.015). Give it once, in 18.3; elsewhere point to it.
- R3. Number fixes:
  - s18-1: all-to-electron 3.018 (3.029 was a 2.8σ fluctuation); A_AB = 5.2 at 1.17 eV gives 3.725 eV (R&K tuned it at 300 K). This becomes moot once R1 removes the old set.
  - s18-3 l.99: the beta splits reach 0.674 with the α → 0 split.
  - s18-2 l.49: just above threshold the phonon competition is below 1e-4 within a few phonon steps, not "a few percent".
  - s18-5 l.110: at 0.83 µs half the gap energy is still held (phonons 0.445); 1 % held at 4.4 µs; the "42 % missed at 1 µs" must include the 5.6 % already trapped or radiated.
  - Limit box 18.4b: the planes miss by 6–7 % at A_AB = 1 (4 % at A_AB = 12).
  - s18-4 l.178: add quartz to the validated list.
  - Fig. 18-limit-b caption: "constant at the 2 % level" is the variation of F over their plane.
  - r_gap bound ≈ 1.7 % (include the bound-exciton localization energy); "half returned" → state the 5 % trapped.
  - One residual convention: model/measured − 1, signed.
  - Full-band "15 %" is against 3.749, or restated.
  - Ge exciton binding ≈ 4.2 meV; grid step one value; table means (8.0 %, Ge 5.3 %); "highest optical" phonon consistently.
  - The 18.4 sensitivity percentages must follow from the quoted slopes; source b_N or drop it.
  - The Klein-box "silicon" point: say it is the θ = 3/2 model or use the calibrated θ = 1 point.
- R4. Derivation gaps:
  - eq:18.2-tagged / eq:18.14: the sum runs over the ionization events along the unit's chain, at the energy where each happens; state the x₁ = E assumption.
  - Add the second-moment recursion to 18.2 (or point to D.43 explicitly) so the three variance terms can be checked.
  - λ_AB wording: the phonon/ionization ratio one gap above threshold is ~23.6 λ_AB.
  - The LO double-count paragraph gets the fourth condition (the ionic part of W^scr restricted to the same model as g^L).
  - The hole-band cut: the phonon ratio falls as x^{-3/2}, not x^{-3}. Fix the D.44/s18-2 wording (the proof holds). Rerun the Ge renewal marker with the cut.
  - "seed term vanishes only for a single split" → the correct condition.
  - The Pauli-blocking check uses the right DOS.
- R5. Prose:
  - Remove process sentences (numerical-check reports, "we could trace", "we found no", the erratum paragraph). 18.4.2: keep only the physics and move the numerics cross-check to the F row/log.
  - Cut repeats: the 50 eV numbers once in 18.1; the measured Si values quoted once (18.4) and pointed to elsewhere; 18.3 l.102.
  - Retitle 18.3, 18.4, 18.5, the two "Open problems" subsections and "Observable law of a marked event".
  - US spelling; "random-$k$"; no source equation numbers in prose; "box" only for Limit Checks; define R, E_v and Shockley's symbols.
  - F_park cites one equation.
  - Punctuate eq:18.5-rates.
  - Register (gives/only/therefore overuse).
  - The 19–21 references print "??": plain prose until those chapters exist.
- R6. Summary: add the linear law (1.61E_g + k₂) and the validated range (−6.6 to +24.5 %, quartz included), the photon-vs-DM seed error (0.062), and the book-value decomposition. Remove old-parameter numbers. Recheck it against the final sections.
- R7. Notation: add the missing 18.4/18.5 rows (Ē_res, B_h, …); A_AB unit fix.
- R8. Pending, not this pass: the R19 full-band cascade (FBC) may later replace the energy-only cascade in 18.1/18.3/18.4. Do not anticipate it.
- casc18_3.py fails above ~55 eV (Gat extrapolates linearly beyond the 53 eV grid top; NZ = 32 aliasing above ~85 eV). The book uses ≤ 51 eV, so nothing printed is affected. Fix: clip E in Gat; NZ ≥ ⟨N⟩ + 10σ. (REF-FBC-B)
- FBC integration done; the hole exchange factor 0.51–0.68 above 3 eV (log value, accepted over the verifier's 0.65).
