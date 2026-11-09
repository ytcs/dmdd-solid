# Ch18 post-revision check (R1–R8 + R19 FBC integration)

Isolated verifier, 2026-11-06. Read: tex/ch18/*.tex, appD/D-43, D-44; figscripts/ch18 logs; ledgers/REVIEWS/ch18/*;
returns/R19/FBC-v2.md (incl. "Quotable"), VER-FBC-v2.md; NOTATION.md (Ch18 block, entry 89).
Runs (in a scratch copy, so the repo is untouched; `git status` is clean): fbc18.py (log identical); si_cascade18.py (log identical
apart from the timing line); casc18_3.py (identical apart from the timing line); casc18_3.py with both guards disabled (same log).

**Verdict: ACCEPT WITH FIXES.** Fixes F1–F3 below are wording only. No number is wrong.

## 1. R1: one Si parameter set
- CONFIRMED. A_AB = 5.703 eV³ and E_g = 1.160 eV are used everywhere, 18.1 included (caption fig:18-tree, l.122), and in
  si_cascade18.py, which every script imports. The continuum calibration reproduces: A_AB = 5.7032. The h^{3/2} Richardson
  extrapolation gives ε = 3.74898/3.74897 eV, and 5.674 maps to 3.7467 eV.
- CONFIRMED. The decomposition is 0.0922 + 0.2898 − 0.2678 = 0.1142 (two solvers agree, and the E_<−E_> route equals the
  remainder to 1e-14). The 2.4σ follows: (0.119 − 0.11419)/0.002 = 2.40. (R1 wrote "2.5σ unchanged", but that was the grid
  value; 2.4σ is the correct continuum figure, and FBC-v2 still says 2.5σ.)
- CONFIRMED. 18.1 on the new set: 12.991 pairs, 3.85 eV per pair, var/mean 0.119, heat 34.93 eV, p_ii = ½ at 5.889 eV.
  10 eV seeds: 2.985 / 2.691 / 3.003; P(2) 4.5 / 36 / 14 %. All match fig18_1.log.
- Grep for old values: 5.674, 3.029, 3.018, 3.725 and 24.5 are absent. "5.2" survives only as the R&K literature value
  (18.4 l.14: "10 % above"; 5.703/5.2 = 1.097, correct) and as the R&K plane points (fig:18-limit-b). Both are legitimate.
  "1.17 eV" survives in ch18.tex l.2 and in WE 18-capture. Both are the millikelvin gap (tab:18-pairs "low" row), not the old
  calibration. CONCERN (optional): add "(millikelvin)" after "1.17 eV gap" in ch18.tex.

## 2. R2–R4
- b_N: CONFIRMED. 0.008 (uniform split) and 0.35 (one-sided split) are subtracted at the grid's own ε (casc18_3.log: 0.346/0.008).
  They are given in 18.3-limits; 18.2 points to that section; the nuisance row repeats them.
- 18.5 timeline: CONFIRMED. r_gap = ½ at 0.8326 µs, with phonons at 0.4448; 1 % at 4.41 µs; at 1 µs the held fraction is
  0.420 plus 0.056 trapped or radiated (end18_5.log). Also consistent: the r_gap bound of 1.7 % and the asymptotic
  0.050 / 0.009 / 0.941.
- Limit Check 18.4b: CONFIRMED. At A = 1 the planes miss by 7.4 % (ε) and 6.4 % (F); at A = 12 by 3.9 % and 4.3 %. "6 to 7 %"
  and "4 %" fit. The 1.2 % / 2.4 % / slope 1.70 also match limit18_4b.log.
- Quartz: CONFIRMED in the 18.4-range "good to 7 %" sentence, in the validated list and in the summary.
- Residuals: CONFIRMED. All seven recomputed as model/measured − 1: −4.9, −11.3, +7.0, −3.4, −19.8, −12.3, −3.5. Range
  −19.8 to +7.0 %, mean −6.9 %, rms 10.47 %. The convention is stated in both table captions and in the nuisance row.
- Klein box: CONFIRMED. The vertical line is labeled as the θ = 3/2 cascade recalibrated to A_AB = 5.629, λ = 3.61; the text
  contrasts it with the calibrated θ = 1 model (Klein form 11 % above; log 1.1137).
- λ_AB wording: CONFIRMED and more precise than the ruling. The text gives (105/2π)(2 − w)^{1/2}λ = 23.3λ (log 23.31λ). R4's
  "≈ 23.6" drops the phonon shift w; 23.3 is the correct value for this kernel. Keep it.
- Second-moment recursion: CONFIRMED. 18.2 l.26 lists the four terms and cites eq:D.43-m2, which is written out in D.43.
- Fourth LO condition: CONFIRMED (18.1 l.50: the ionic part of W^scr is restricted to the same model as g^L).
- Hole-band cut x^{-3/2}: CONFIRMED in 18.2 l.145 (P_e ∝ y² for y ≫ B_h) and in D.44 l.126.
- Also checked: the x₁ = E statement (18.2 l.143); the seed-term condition (18.3 l.32, "one value on the whole support");
  the Pauli DOS (m_d = 1.064, 7.5e21, fills < 1e-2); "< 1e-4 within a few phonon steps" (p_ii(1.349 eV) = 2.7e-5);
  β splits up to 0.67 (log 0.674); the sensitivity slopes 0.076 / 0.0013, which follow from +1.16 % / +0.65 %.

## 3. FBC integration
Run: `python fbc18.py` reproduces fbc18.log byte for byte. The log matches fbc18_data.json and FBC-v2 §5–§7.

Quotable-list audit of every full-band number in 18.1, 18.3, 18.4 and the summary/nuisance table:
- ε 4.15 [3.95, 4.73] + ≥ ±0.4 eV: CONFIRMED (18.4 l.16, summary, nuisance row). The caveats in the text: EPM bands,
  deformation-potential phonons, diagonal static Cappellini (18.3); the missing plasmon channel (18.4 l.64). 4.11 eV
  (NF-like) and "0.6 eV unexplained" come from FBC-v2 key result #1 / VER §7.
- F 0.114 [0.101, 0.115], no structural claim: CONFIRMED. 18.4 l.64 says explicitly "does not show that the gap … is
  structural"; 18.2 l.51 and the summary make no claim.
- P(≥2, 5 eV) 0.097 [0.030, 0.173]: CONFIRMED (18.3 l.71, summary, nuisance). Heavy seed; the grid term is included.
- Overcount ~10×, ≥ 6×: CONFIRMED. 30× is given only with its corner (Resta + holes × 3 + lowest R_x), as the list requires.
  WE 18-step5 says "about ten".
- Heat 71.6 % [70.2, 75.0]: CONFIRMED (18.4 l.16). No above-threshold/residual split is quoted.
- R_x: see the decision below.
- Photon vs DM: CONFIRMED. No full-band number is given; 18.3 l.71 says it is unresolved.
- Not quoted, as required: the "≈ 3.9 eV" reconciliation, "static screening bounds the rate", mK vs 123 K 0.016, split
  agreement 0.029.
- Matched distances 0.12–0.20 at 6–8 eV: not in the Quotable list, but it is FBC-v2 §6's own wording ("structural residual …
  0.12–0.20 at 6–8 eV"), and VER §A6 reproduces it (0.146/0.159/0.204 for the DM seed, 0.121–0.174 for the computed split).
  The R-K α = 1 range 0.11–0.12, the equal split 0.45–0.50 and the step model 0.79–0.83 match the log. CONFIRMED.
- CONCERN (outside the list), 18.1 l.106:
  (a) "tripling … lowers ε from 4.15 to 3.73 eV; doubling above 5 eV leaves it unchanged": a v2 diagnostic (FBC-v2 key
      result #3, table §2). Acceptable as a diagnostic.
  (b) "at 4 eV … 0.99 without phonon emission and 0.008 with it": both are **v1** runs (FBC.md l.261; fbc18_data
      v1_nophonon 0.9866, v1_primary 0.0080). The v2 primary at 4 eV gives 0.007 (FBC-v2 §5). See F2.
  (c) memory "at most 0.015 in d_TV" (also 18.5 l.125 and the nuisance row): the list files it under "Qualitative only
      (model-internal)". The text always carries the model-internal caveat, so this is tolerable. Editor's call; a
      qualitative wording would follow the list exactly.

Hole R_x, 0.51–0.68 (book) against 0.51–0.65 (verifier): **the book is right.** In rx_v2.npz (= fbc18_data.json "rx"), the
hole R_x in 1-eV blocks from 3 eV is 0.62 0.62 **0.68** 0.61 0.60 0.57 0.54 … 0.51. On the 0.25 eV bins it reaches 0.678 at
5.375 eV and 0.701 at 5.625 eV. FBC-v2 §2's "0.64 to 0.51" (hence the verifier's 0.65) reads the end points and misses the
bump at 5–6 eV. The electron range 0.66–0.84 uses the same 1-eV-block convention, so 0.51–0.68 is consistent. This agrees
with the editor-notes ruling. Both ranges sit inside Kotani's 0.5–1.

Overclaiming / working model:
- CONFIRMED. The energy-only cascade stays the calibrated working model (18.3 l.71: "remains the working model … calibrated
  and fast"), with its measured distance 0.12–0.20 in d_TV in the nuisance table and the summary. The full band is
  "reference", "no fitted constant", and is placed above the measurement, with NF below it.
- CONCERN (wording; see F3): "and the full band measures its error" (18.3 l.71) and "tests both reductions where they
  matter" (18.1 l.106) slightly overstate a model-class result whose own ε misses by +10.7 % and whose memory bound is
  model-internal.
- CONCERN (see F1): FBC-v2 IF-FBC-5 and VER §B2 say the photon seed itself is not k-converged (it moves 0.11–0.14 between
  12³/20³/28³). The book's photon seed is the same kind of object (EPM optical limit, NK24), and its photon-vs-DM bound of
  0.062 is printed without a grid caveat in 18.3 l.110, in the summary and in the nuisance row. The caveat in 18.3 l.71
  speaks only of the full band.

## 4. casc18_3.py guards
- CONFIRMED. Gat raises above the grid top (l.125), and pair() refuses NZ < ⟨N⟩ + 10σ (l.143). The docstring states both.
  The rerun reproduces casc18_3.log. A copy with both guards turned into no-ops gives the same log line for line (apart from
  the timing line), so every printed ≤ 21 eV / ≤ 51 eV number is unchanged. Every 18.3 number spot-checked against the log
  agrees: 0.414/0.547/0.039, 2.626, 0.314 = 0.283 + 0.031, 0.176, 1.735, 0.831/0.169, 5.91, 0.062 at 5.67, 0.21/0.39/0.67/
  0.86, 4.37/12.95, 0.36, 0.79/0.45.

## 5. Prose
- CONFIRMED. No process sentences are left ("we found/could", numerical-check reports, erratum: none). The 18.4-rk cross-check
  now reads as physics ("two codes solve the same model"). Minor: its "Of course" is register.
- CONFIRMED. Titles changed: 18.3 "Seed distributions and the step model", 18.4 "Calibrated pair energies", 18.5 "Capture and
  excitons", "Constant term and the renewal bound", "Unknown rates and unsized truncations", "Pair number at the readout".
  No "??", no source equation numbers in the prose, US spelling.
- Repeats: the 50 eV numbers appear in the 18.1 opening (rounded) and the caption (exact); acceptable. The measured Si pair
  energy and F are also quoted in 18.2 l.3 (with \cref{tab:18-pairs}) and 18.5 l.39 (with a pointer); acceptable.
- Summary: CONFIRMED. It has the linear law (1.61E_g + k₂, k₂ 1.2–2.5, Si 1.88), the validated range (−19.8 to +7.0 %, rms
  10.5 %, quartz), the seed error 0.062, the book-value decomposition 0.092 + 0.290 − 0.268 = 0.114, and the full-band
  sentences and rows (P(≥2) band, ~10×/≥ 6×, 0.12–0.20, ε band + 0.4 eV, F band, 0.6 eV). No old-parameter numbers. All
  sizes recheck against the sections (0.54 % [0.32, 0.77], 2.5/1.1 %, 25 meV/7.2 meV, 0.39 %, 20 cm).
- 18.2, 18.4, 18.5 numbers recheck against limit18_2a/b/c, fig18_2, num18_2, table18_4, limit18_4a/b/c and end18_5 logs with
  no mismatch.

## 6. Notation
- CONFIRMED. NOTATION.md A_AB row: eV³, 5.703, the source's eV² flagged as a misprint (l.1434). Entry 89 lists the new rows,
  and they exist: λ_AB/w_AB, B_h, b_N/c_N, M_t, Ē_res, k₂/r_K/ω_K, E_np…, f_cap…, N_X/F_heat/p_ns, the 18.5 rates, r_gap/
  w_k/γ_k/b_*, p_ii, 𝔓_t, d_TV.
- The FBC text introduces no new symbol: R_x is written out as "exchange factor", and z_qp and d_TV already exist. No row
  is needed.

## Fixes
- **F1 (seed-grid caveat, IF-FBC-5).** In 18.3 l.110, after "stays within 0.062 of the dark-matter seed everywhere", add:
  "on the grid used; the optical-limit seed is not converged in k, and in the full-band stage it moves by 0.1 between
  grids, so this bound carries a grid uncertainty of its own order". Carry a short "(grid-limited)" into the summary
  sentence and into the nuisance row "d_TV ≤ 0.062".
- **F2 (v1 numbers in 18.1 l.106).** Either replace "0.99 without phonon emission and 0.008 with it" with "nearly all without
  phonon emission and below 0.01 with it", or keep 0.99 and give the v2 value 0.007. Both originals come from the
  superseded v1 runs and are not in the Quotable list.
- **F3 (tone).** In 18.3 l.71, "and the full band measures its error" → "and the full band, within its own model class,
  gives a measure of its kernel-shape error". In 18.1 l.106, "tests both reductions where they matter" → "probes both
  reductions where they matter".
- Optional: "(millikelvin)" after "1.17 eV gap" in ch18.tex l.2; a qualitative wording of the 0.015 memory bound, per the
  Quotable list.
