# Light pass, part B (Chapters 13–22), 2026-11-07

Brief: briefs/reviews/lightpass-B.md with lightpass-common.md. Build: latexmk, outdir /tmp/claude-0/build-lp-B (result at the end). Lint (skills/long-form-writing/scripts/lint.py, BANNED-TERMS.txt) on every changed tex file: 0 blocking.

| item | status | where |
|---|---|---|
| 1. 14.2 X_αβ → u_αβ | done | tex/ch14/s14-2.tex:78, 80, 83, 85 (X_αβ, X_αα, X_xz, X_yz, X_αz). NOTATION entry 102(a): row X_αβ, f_me and App. B.1 still print X_αβ; append-only rule, so the row edit is left to the App. B owner. check_notation ch14: 0 gaps |
| 2a. Ch15 Al speeds 6.47/3.40 | already labelled [100] in 15.1 (s15-1.tex:7) and 15.4 (s15-4.tex:38), where they set order-of-magnitude phonon momenta; done in the summary table | tex/ch15/s15-summary.tex:49: "(along [100], 0 K; isotropic 6.63 and 3.30 km/s, Sect. 20.3)" |
| 2b. s16-8 caption | done, with the full isotropic set 6.63/3.30 km/s, 2.70 g/cm³ (c_LA too, so the set is not mixed), pointer 15.4 → 20.3 | tex/ch16/s16-8.tex:51; figscripts/ch16/tls16_8.py (constants, docstring), fig16_8.py (rerun; fig16_8.log, fig16_8.pdf). Numbers that moved, text updated: transverse/longitudinal weight 50 → 65 (s16-8.tex:19), one-phonon rate 1.8×10⁵ → 2.1×10⁵ s⁻¹ below 50 mK and 2.1×10⁵ → 2.5×10⁵ at 0.1 K (s16-8.tex:19, 28). Crossover 0.21 K and the 1.5 K Born point unchanged. Only fig16_8.py imports these constants |
| 3. Fig. 15.3b, Ch17 11.5 meV | done | figscripts/ch15/fig15_3.py now plots the direct term × 1/(1 + λ_ep) = 0.699; log prints both crossings (bare 11.5, plotted 10.9 meV). Caption tex/ch15/s15-4.tex:91; text s15-4.tex:126 drops the "11.5 meV for the bare form" parenthesis. Ch17: s17-2.tex:29 caption (factor, 10.9 meV); figscripts/ch17/abs17_2.py also carried the bare form (curve to 11.5 meV, table values) and now carries the factor (rerun, abs17_2.log/.err; err unchanged): table s17-2.tex:44 aluminum 5.1 → 6.1×10⁻¹³ (the 15.4 value already quoted in s17-2 text), s17-2.tex:45 7.6 → 9.1×10⁻¹² at 10 meV. Same "0.36 to 11.5 meV" in tex/ch21/s21-7.tex:91 → 10.9 |
| 4a. s16-1 ZrTe₅ pair cost | done | tex/ch16/s16-1.tex:15: 31 → 23.6 meV |
| 4b. minimum 9 vs 9.5 keV | done: home section 16.1 (WE 16.1, we16_1.log "at 9 keV"; digitized point 9.46 keV) governs | tex/ch21/s21-5.tex:106: "near 9.5 keV" → "near 9 keV" (fig21_5.log prints 9.5 with one decimal; same point) |
| 5. 17.1 "tables' gap 1.11 eV" | done as wording (Ch21 21.6 and 10.10 usage: the tables are scissored to 1.17 eV; 1.11 eV is the step-model gap of their package) | tex/ch17/s17-1.tex:15 (rates counted from 1.11 eV; onset 0.333 → 0.316 MeV), s17-1.tex:20 caption; same claim in s17-3.tex:82 (caption) and s17-5.tex:40. Scripts not rerun: sectors17.py and exo17_3.py take the threshold from figscripts/ch10/rate10_2.py (EG = 1.11, part A's file). If part A changes EG to 1.17, rerun sectors17.py and exo17_3.py and drop the 1.11 wording |
| 6. 21.7 Fermi function | done | tex/ch21/s21-7.tex:106: "the traditional relativistic Fermi function of a point charge, with the prefactor 4, evaluated at the nuclear radius r_A" [Hayen Eq. (6)] |
| 7. 22.2 (Zα)² xenon | done | tex/ch22/s22-2.tex:56: 0.13 → 0.155 ((54/137.036)² = 0.1553) |
| 8. Ge PAER edges (DC-4) | done: shown to be one quantity | tex/ch13/s13-9.tex:108: the computed branch (6.70 meV at Q*, 6³ grid, stated soft by 13.5 % at X, 11.6 % at L) places the onset at 0.21380 MeV (free pair) and 0.21264 MeV (1s exciton, binding 4.0 meV, estimated), both inside the 0.2119–0.2141 MeV bracket, and INS scaling moves them by ≤ 0.0003 MeV. The bracket stays as quoted in 13.1, 13.9 table, 17.1, 22.1, 22.2. No other TA frequency of Ge is quoted in Ch13–22 |
| 9. SEAMS/18.3 | done | ledgers/SEAMS/18.3.md:30, 32: 0.015 → 0.008 |
| 10. Acronyms first used in Ch13–22 | done | YIG s14-1.tex:27; SCF s16-6.tex:32; JARVIS s17-6.tex:27; CDMS s18-5.tex:43; TRIM s19-4.tex:113; G4CMP s20-1.tex:161; TB09 s21-6.tex:64; CVD s21-7.tex:9 (used once: written out, acronym dropped). gen_B3.py's matcher still lists G4CMP and TB09 as never expanded (their expansions do not spell the letters, "Geant4", "Tran and Blaha (2009)"); the fallback expansions apply |
| 11. DC-RESULTS sweep | see below | |

## DC-RESULTS sweep, Ch13–22
- DC-83, DC-5: no change (text stands).
- DC-41: already applied. 15.2 table, 15.3 (s15-3.tex:99), 15.1 (s15-1.tex:128, "clean"), the summary and 21.4 (s21-4.tex:91) state the ℓ_mfp scope with the edge values; no "screens less"; nothing says the clean table holds for films.
- DC-93: already applied. Ch17 (s17-5.tex:118, 149, 165) and Ch21 (s21-7.tex:3, 13, 51, 130) use the measured 4.2 K tensor; the B-floor appears only as a check against the tabulated speed. The FOM 3.73 [3.65, 3.80] is the book's own rerun with the measured tensor (guide21_7.log, fom17_5.py), not a rescaling, and lies in DC-93's 3.7–3.9; it is quoted as computed, so no "≈" was added.
- DC-49/54/36: no withdrawn number in Ch13–22. 16.1's ×1832 for Yb₃PbO is stated as a model statement (s16-1.tex:73); 16.7 quotes no a_sat and no reflection bound.
- DC-2, DC-2-alpha: already soft (13.1, 13.9, 22.1:97); no claim that hybrid+SOC bands give the Ge edge.
- DC-91: Ch17/Ch21 quote no DC-91 number. LiF, NaF enter through Griffin's computed Z*, ε∞, ω (s17-6.tex:31), consistent with DC-91 (ε∞ 2.04/1.88, Z* 1.054/1.02; ω_max 78.3/49.4 ± 1–2 meV); their sound speeds are database tensors, not DC-91's; SiC uses measured dielectric constants. No change.
- DC-4: item 8.
- DC-67: no library table, coverage or accuracy claim; 21.6 describes library checks as a specification. No x^(−1/2) tail law in Ch18. Not changed, for the editor: REF-DC-67 §8 item 6 quotes "A ≈ 5.62 eV³ in the continuum, F ≈ 0.114, about 2.5σ", while Ch18's own continuum calibration (si_cascade18.log) gives A_AB = 5.703 eV³, ε 3.7490, F 0.11419, 2.40σ, quoted as 2.4σ in s18-4.tex:54, 64 and s18-summary.tex:9, 31. DC-67's ε 3.7468 / F 0.11398 are the continuum values at the earlier grid calibration A = 5.674 (si_cascade18.log line 8). Aligning would change A_AB book-wide (NOTATION entry 89), beyond a last digit.

## Side effect to note
Running figscripts/appB/gen_B3.py to check item 10 rewrote tex/appB/B-3.tex and gen_B3.log (the script writes both). B-3.tex is generated from the tex, so it now carries the new first-use expansions; no hand edit was made to tex/appB.

## Build
latexmk -pdf, outdir /tmp/claude-0/build-lp-B, run twice (the first run stopped on a citation from appC/C-18.tex, part A's file, that resolved after the bibliography pass): final rc 0, 0 errors, 0 undefined references or citations.

## Editor rulings on the open items (2026-11-07)
- REF-DC-67 (A ≈ 5.62 eV³, 2.5σ) vs Ch18 (A_AB = 5.703 eV³, 2.4σ): no change. Ch18's continuum-calibrated set (E_g = 1.160 eV) is the book's calibration. The DC-67 values belong to the exact-ω₀, h → 0 run with a different setup. The book quotes ε and F only, where they agree within the stated precision.
- B-3.tex regenerated by gen_B3.py: accepted. App B is regenerated at the end anyway. The G4CMP and TB09 flags are false positives of the script; fix the script's matcher at the final regeneration.
- X_αβ → u_αβ in App B.1: picked up when gen_B1.py is rerun at the end.
- Item 5 waits on part A's threshold decision (1.11 vs 1.17 eV). If ch10's script changes, rerun sectors17.py and exo17_3.py.
