# Chapter 21 post-revision check (2026-11-07)

Scope: tex/ch21/*.tex, appD/D-46.tex, D-47.tex, ch10/s10-10.tex, appE/E-27.tex, Ch21 rows of appF/F-rows.tex, against rulings R1-R8 (editor-notes.md), the five reports and revision.md. Independent checks: own Python re-derivations (noted), figscripts/ch21/*.log, figscripts/ch10/nuis10_10.log, figscripts/ch18/casc18_3.json.

Verdict: FIXES NEEDED (minor). Every ruling is applied and every changed number traces to a log. Two short text fixes (C1, C2), one script-provenance fix (C3); C4, C5 optional.

## 1. Rulings

| Item | Status | Evidence / fix |
|---|---|---|
| R1 exactness of σ_β²t′/2 for one bin | CONFIRMED | Own derivation: one bin, S = σ s₀e^{−σ_βϑ}; the profile gives ϑ̂ = ½σ_β ℓ′(N) S exactly; the Neyman probability depends only on N, so at the limit S(ϑ̂) = s_up and y = ½σ_β² ℓ′ s_up = ½σ_β² t′ with no higher orders. Own numerics (zero counts, σ = 0.3): Neyman exact 1.23027 vs e^{σ²N90} 1.23027. we21_4.log Part 3 agrees for (N_obs,b) = (0,0),(0,1),(1,1),(2,2). |
| R1 WE 21.4 numbers | CONFIRMED | e^{0.393²·2.3026} = 1.4271; 1.242e-41 × 1.427 = 1.772e-41 → "1.77e-41". One-sided σ = 0.306: 1.2406 → 1.540e-41 → "1.54e-41". Detector σ = 0.404 → 1.457; 1.223 on b = 1 (e^{0.393²·1.303}). All in we21_4.log and fig21_4.log (3 MeV row). |
| R1 D.47 fixed-threshold subsection | CONFIRMED | x_p − x₀ = ¼σ²Q′ derived correctly ("charges half"). Own numerics, zero counts, t* = 4.605: exact 1.1039 / 1.2930 vs second order 1.1092 / 1.3335 at σ = 0.3 / 0.5; D.47's 1.104, 1.109, 1.230 match. μ removed; typo "t′ = 2N^up = 2.61" fixed. |
| R1 three-coefficient comparison removed; summary and nuisance table | CONFIRMED | No 1.101/1.103 left; s21-summary l.9 and tab:21-nuisances row "Statistical construction" carry 1.427 and "half the exponent"; 21.5 WE's 1.12 (= 1.1215 in we21_5.log) is identified as eq:21.4-profile. |
| R2 cascade bins from casc18_3.json | CONFIRMED | hib21.pbin loads ch18/casc18_3.json key DM/P (E_g 1.160, ε 3.749 eV, matching s18-2/s18-3). Round-off <1e-6 zeroed. |
| R2 σ_lim, bound, costs | CONFIRMED | we21_2.log / fig21_2.log: σ_lim 3.7213e-42 (one-pair bin), bound(500) 3.6140e-20, min cost 2.1227 at 378.75 km/s (text "2.12 at 379"; derivation-1's "×2.13" was approximate), 2 MeV 3.7021 at 558.5 ("3.70 at 559"); crossover 532.6; 474.3/614.4; ×12.45 at 600, ×77.1 at 700; columns 2.90 and 252 ("2.9 and 250"). WE 21.2: A_i 9.41/8.07/1.82e19, ξ₁ 6.03e-23, counts 3.40/2.92/0.66, λ₁ 1.06e-20, 3.96 × 1.10 = 4.35 all match. Summary, tab:21-nuisances, 21.5 recast (1.271/1.204/1.154; 1.156/1.432/4.0) match stats21_5.log. |
| R2 leakage factor | CONCERN (C2) | 2·0.0637/3.749 = 0.0340 as ruled. But the cascade bins are not ε_eh wide: ∫P_i dω from casc18_3.json = 3.604 (N=2), 3.687 (N=3), 3.617 (N=4) eV, so 2ω_max/Δ_i = 0.0353/0.0346/0.0352. "At most 0.034 ϱ" understates by ~4 % for the cascade. Fix: in s21-2 l.115 write "Δ_i ≈ 3.6–3.7 eV for the cascade bins above one pair (ε_eh = 3.749 eV far above threshold), so 2ω_max/Δ_i ≤ 0.035"; change 0.034 → 0.035 in s21-2, s21-4 l.30, s21-6 l.21, summary l.5 and tab row; add the line to limit21_2a.log. |
| R2 two-table reconciliation / step model once | CONFIRMED | s21-2 l.44 (step "overcounts that bin about tenfold near 5 eV"), tab:21-nuisances "Pair-bin model" row; step model is quoted only as comparison. |
| R3 June | CONFIRMED | s21-1 l.92, 21.4 halo paragraph, summary: exposure average is the basis; "June Earth speed"; no "June escape speed". |
| R4 double count removed in Ch21 | CONFIRMED | nuis21.py EG_TAB = 1.17, no 0.06 eV shift; we21_4.log central 1.855e4 → 1.242e-41, band 8.380e-42–1.839e-41, ×1.345 over RPA. Fig. 21.4 caption ω ≥ 1.17 eV; text 3.4/1.48/1.43, 1.14/3.59/7.04 MeV, 1.10/1.46 match fig21_4.log. No 1.30e-41, 1.93e-41, 8.8e-42 (as band), 1.048 left. RPA 9.23e-42 is unchanged by R4 (it never carried the factor) and is correctly kept. |
| R4 Section 10.10 | CONFIRMED | l.3 and l.19 rewritten (scissor to measured T = 0 gap 1.17 eV; 1.11 eV identified as step-model constant; m_min 0.333). WE 10.band3: 1.85e4, "about 51" (50.8), 10 % below 3 eV, LF +0.066/+0.064, σ 0.393, band 1.25e4–2.75e4, ϑ_X = 1 → 2.37e4, light 6.0e3 and 1.67, gap −7.5/+8.0 %: all in nuis10_10.log. Summary l.118 1.85e4. No 1.77e4 left in ch10. |
| R5 ²¹⁰Pb budget | CONFIRMED | Own computation with eq:21.7-fermi (prefactor 4, r_A = 1.2A^{1/3} fm): f_β(Pb gs, Z_d 83) 0.04447, f_β(Bi, Z_d 84) 1.2635e-3; 86400(0.16·0.04447 + 1.2635e-3) = 723.9; split 614.7 + 109.2 (Bi 15.1 %); 1/723.9 = 1.381 mBq/kg; PbSe 1.38/0.724 = 1.91. Ratio to nonrelativistic 689.1 = 1.050 ("5 %"). Z_d attribution correct. |
| R5 script prefactor | CONCERN (C3) | guide21_7.py fermi_rel uses 2(1+γ), the printed Eq. (6) of hayen2018high uses 4. The constant cancels in f_β (verified: identical to 1e-15), so no number changes. Fix: set the prefactor to 4 in fermi_rel (or note in its docstring that it cancels) so the script reproduces the printed equation. |
| R6 items | CONFIRMED | ZrTe₅ 5091 at 20 keV ("5100 to 6400"); dominant swap only at 3.59 MeV; tabulation spread as standard normal with stated prior (once, 21.4-like); 600 TB gone; 1.04–4.5 clause gone; 21.3 "−6.0 and +6.6 percent, −71 or +78 meV" = fig21_3.log l.82–83; LC 21.1a convention "exceeds by less than 10 %" up to 735.6 (limit21_1a.log) in caption, summary, F row; LC 21.2a title, Fox–Liu–Weiner (A1), "up to 15 %" from 340 km/s; keyresult condition; ω_max 63.7; envelope theorem and stochastic ordering defined; v_max^{2p_on+8}. |
| R7 prose | CONFIRMED | "no resolved leader"; union bound, E.27 pointer, tabulation spread each once; eq:21.7-pb210 ends with a period. |
| R8 notation | CONFIRMED | ξ_a for stream weight, δ_cert/δ_dec, μ absent from D.47, E.27 states the kernel relation (𝔎_i = 𝗄_i, F = Ξ). |

## 2. Numbers and stale values

Greps over the scope: 1.30e-41, 1.53e-41, 1.93e-41, 9.2e-42, 1.77e4, 1.048 (as cold gap), 1.101/1.103, "sixth" (as Bi share): none. Remaining hits are legitimate: 9.23e-42 (RPA, unchanged), 8.8e-42 (s21-5 l.106, Dirac gapless recast, unrelated), 689 (s21-7 l.116, the nonrelativistic comparison only), 1.60e5 (s21-1 l.3, WE 10.1 at 10 MeV with 1.11 eV threshold, unchanged and consistent with nuis10_10.log gate line), 1.11 eV (s21-1 l.80 Essig QEdark table convention; s21-6 l.53/70 and s10-10 l.19 naming it the step-model constant; s21-7 l.77 a ratio), 3.6 eV (step-model constant, s21-6 l.70, s10-10 l.19). No step-model bins used as Ch21's own.

| Item | Status | Fix |
|---|---|---|
| C1 summary range | CONCERN | s21-summary l.21: "the statistical construction and the treatment of shared nuisances move limits by five to forty percent", but the construction row gives 1.427 (43 %). Fix: "by five to forty-five percent" (or "by 5 to 43 percent"). |

## 3. Regressions

| Item | Status | Note / fix |
|---|---|---|
| Lint (BANNED-TERMS.txt) | CONFIRMED | 74 hits, 0 blocking (LONG-SENT warnings; two "landscape" false positives; two EQ-PUNCT false positives at s21-3 l.62 and s10-10 l.69, both end in a period). |
| Process words / left to the reader | CONFIRMED | No revis-/ruling/earlier-version/exercise/DC-/REF- strings in scope. |
| C4 house form in E.27 | CONCERN (optional) | E-27 l.7, 13, 17 "non-negative" against STYLE "nonnegative" (R7). Fix: replace the three. |
| C5 s21-2 l.110 | CONCERN (optional) | "each bin probability rises and falls once": stochastic ordering gives a difference of two nondecreasing functions (TV ≤ 2), not unimodality. Fix: "each bin probability is a difference of two nondecreasing functions with values in [0,1], so its total variation is at most 2". (Checked: casc18_3 DM P(N ≥ n|E) nondecreasing to 1e-6.) |

## 4. Build

`latexmk -pdf -interaction=nonstopmode -outdir=/tmp/claude-0/build-ch21post main.tex`: 0 LaTeX errors, 0 undefined citations, 1748 pages. Undefined references only app:B.2 (5), sec:9.1, sec:9.2 (4), sec:9.4 (known). latexmk stopped after its fifth pass with a biblatex "Please rerun LaTeX"; one further pdflatex pass is clean (no rerun warning, 0 errors, 0 undefined citations). CONFIRMED.

## Fix list

1. C1: s21-summary l.21 "five to forty percent" → "five to forty-five percent".
2. C2: leakage factor for cascade bins is 0.035 (Δ_i = 3.60–3.69 eV), not 0.034; update s21-2 l.115 wording and the 0.034 occurrences (s21-2, s21-4 l.30, s21-6 l.21, summary l.5, tab row); log the Δ_i in limit21_2a.
3. C3: guide21_7.py fermi_rel prefactor 2(1+γ) → 4 to match eq:21.7-fermi (no number changes).
4. Optional: C4 (E.27 "non-negative"), C5 (s21-2 "rises and falls once").
