# Language audit, Part I (tex/front, tex/ch01–ch08): reviser log

Brief: briefs/reviews/language-audit.md, reviser role. Ledger: ledgers/REVIEWS/language/partI.md. Edits were made only in tex/front, tex/ch01–ch08 and figscripts/ch01, figscripts/ch04, with one exception: the editor's ruling (d) needed one sentence in ch08/s8-5, which is in Part I. Each replacement was an exact string match that occurred once in its file.

## Editor rulings on the physics doubts

**(a) Silicon gap (P1, P5).** Part I now uses the low-temperature gap, 1.17 eV, for every threshold and kinematic number, as Ch. 10 and Sect. 13.1 do. The dependent numbers were recomputed (scratch check plus the figscripts):
- s1-3 we:1-mmin: m_min = 2×1.17/7.023e-6 = 3.33e5 eV = 0.333 MeV, optimal q = 0.88 keV. The 1.11 eV used in many projections is now stated as such, "close to the room-temperature gap", and gives 0.32 MeV, 5 % lower. Phonon/electronic reach ratio: 1.17/0.030 = 39 (was 37).
- s1-3 fig:1-kinematics caption: "the low-temperature band gap, 1.17 eV"; the citation is now Ramanathan Eq. (11) instead of Essig Eq. (5.2). figscripts/ch01/fig1_5.py: E_GAP = 1.17, source block updated, figure regenerated.
- s1-3:112: the roots at 1 MeV are 0.49–4.8 keV (now the same as s3-3 we:3-kc), at 10 MeV 0.45–53 keV. A free Si nucleus receives 1.17 eV for m_χ ≳ 47 MeV (was 45).
- s1-3:121: q ≥ 1.17 eV/v_max = 0.44 keV = 0.12 q0.
- s1-3 edge recovery (η at the most favorable speed, relative to η(0), computed with the D.1 closed form of fig1_6.py): 6.0e-5 at 0.35 MeV, 1.1e-3 at 0.4, 0.76 % at 0.5, 12 % at 1, 84 % at 10 MeV. The old phrase "over the first factor of two … more than three orders of magnitude" no longer holds once 0.35 MeV is only 5 % above m_min. It now reads "Between 0.35 MeV, 5 % above m_min, and 2m_min the halo supply grows by a factor of more than 500" (from 6.0e-5 to 3.3e-2). The 560 km/s and 7 % figures do not depend on E_g and are unchanged.
- s1-4: the momentum-transfer range starts at 0.44 keV = 0.12 q0. In the lim:1.4a caption the marker is at 0.12 q0, and the light-limit bound is m_V ≤ 0.028 q0 = 0.10 keV (was 0.026 q0); the heavy bound, 4.5 q0 = 17 keV, is unchanged. figscripts/ch01/fig1_7.py: X_GAP from 1.17, figure regenerated, printed bounds 4.54 and 0.0276.
- s1-5: the pair examples give ⌊1.06⌋ and ⌊2.45⌋ (the pair counts are unchanged). The thresholds are 1.17, 4.77 and 8.37 eV, and the threshold masses 0.33, 1.36 and 2.38 MeV. Toy rate (we:1-limit): ln(30/1.17) = 3.24, R/σ = 2.305e34, r = 7.28e41, N_sig = 73, σ_lim = 3.2e-42 (3.2e-43 for ten times the exposure). ch02/s2-1:3 now says 73 events to match. In the fig:1-exclusion caption and text the threshold is 1.17 eV and m_min 0.33 MeV, with the light minimum at 2.1 MeV (was 2.0), the heavy minimum still at 9.7 MeV, ratios 49 and 1.5 (were 46 and 1.4), and the two-pair wall at 0.33 → 1.36 MeV. figscripts/ch01/fig1_9.py: EG = 1.17, figure regenerated. Summary: "0.33 MeV for the low-temperature silicon gap".
- s3-3 we:3-kc: the parenthetical comparison with the 1.11 eV roots of Sect. 1.3 is replaced by "as in Sect. 1.3".
- s4-3 we:4-gasfsum: E_g = 1.17 eV, the crossover is 3m_eE_g/2k_F = 0.25 keV (was 0.24), and the ratio at q = 0.1 keV is 0.40 (was 0.42). figscripts/ch04/fig4_3.py: assertions updated, and the script reruns cleanly (251.2 eV, 0.398).
- s4-4:134: "the gap of 1.17 eV".
- Kept at 1.11 eV, because the text means room temperature: s4-2:82 and s4-7:121 already said "at 300 K". The s4-4 fig:4-loss caption (data taken at 300 K) now reads "Dotted: the room-temperature gap, 1.11 eV, to match the data", and the fig4_5.py source note says the same. The figure is not regenerated (the marker is unchanged).
- **Logged for the editor (not changed):** the room-temperature gap itself is quoted two ways. It is 1.11 eV at 300 K in s4-2:82, s4-4 (caption) and s4-7:121 (which cites app:E.1), and 1.12 eV at 300 K in s1-3:68, s2-4:3, ch06:3, s6-5:114 and appE/E-13:85 (Ramanathan Table I).

**(b) Shallow donor (P2), s7-4:7.** The sentence now reads: "… uses four of its five valence electrons in the bonds. The fifth is bound to the ion core and its one extra positive charge, in a hydrogenic donor level just below the conduction band, built from conduction-band states." This also covers ledger item 28.

**(c) Ch. 6 opening (P3).** The ~60 meV zero-point shift now points to \cref{sec:6.3}.

**(d) Excitonic change of ε∞ (P4).** s4-9 now reads "the attraction raises it by 17 percent above the local-field value of 10.22, to about 11.9". s8-5 now reads "the local fields lower ε∞ by 11 %, from 11.45 to 10.22; the adiabatic kernel restores about half of that, to 10.81; and the attraction, added to the local fields, raises the local-field value by 17 %, to ≈ 11.9". Both now use the same reference value, and the numbers agree: 11.9/10.22 = 1.164, and fig4_11.py checks st["bse"]/st["lf"] − 1 = 0.17. Nothing is left to log.

## Ledger items

MUST, all applied: 2, 3, 4, 5, 9, 14, 16, 18, 19, 26, 29, 30, 34, 35, 36, 39, 43, 45, 46, 47, 57, 58, 60, 63.
- 39: the subsection "The ladder of approximations" in Sect. 4.9 is retitled "Levels of approximation". It had no label. The section title and \label{sec:4.9} are unchanged.
- 43: the s4-9 closing paragraph keeps the silicon numbers and the final clause. The procedural restatement is replaced by "As in \cref{sec:4.6}, the spread is an estimate, not a bound. Light dark matter samples the first eV above the gap; for it the attraction is the leading correction, …".
- 5 together with 6/52: the ch08 opening now starts with the question (magnetic moment; absorbed fermion). The "Behind all of them stands …" sentence is deleted, and the "A slow particle sees …" sentence is cut from the opening; it stays at s8-1:3, so "therefore" is dropped from the next sentence. Before "\Cref{chap:4} took …" the words "So far" are added.

OPTIONAL, applied: 1, 6 (by cutting, see 52), 7, 8, 10, 11, 12, 13, 15, 17, 20, 21, 22, 23, 24, 25, 27, 28 (superseded by ruling b), 31, 32, 33, 37 (caption cut to one clause), 38 (s5-7 label dropped; s7-3 → "Size of the Dirac screening.", s7-4 → "Detection fraction."), 40 (Ch. 7 → "Magnets, superconductors, Dirac materials and defects"), 44, 48, 49, 50, 51, 52, 53, 54, 55 (the separation and halo sentences of s1-1:12 cut; the 10^23 sentence kept without "by contrast"), 56, 59 (all 7 sites), 61, 62, 64, 65, 66 (all 3), 67, 68, 69 (all 3), 70, 71, 72, 73 (the s8-1:26 site; ch02:3 kept), 74.

OPTIONAL, not applied:
- 41 and 42 (retitling Sects. 8.8 and 8.5). "Expansion hierarchy" is a term used book-wide (appE/E-1, ch10/s10-1, appB/B-1 symbol table), and "Uncertainty structure" is a box title in figscripts/ch08/map08.py. Renaming them would mean edits outside Part I.
- MONOTONY hits in s4-6 and s4-7 (not listed in the ledger).

## Checks
- Lint (lint.py --banned BANNED-TERMS.txt on tex/front and tex/ch01–ch08): 215 hits, **0 blocking** (152 LONG-SENT, 59 EQ-PUNCT, 2 PERIPHRASIS technical, 2 MONOTONY).
- Build (latexmk -pdf, outdir /tmp/claude-0/build-lang1): completed in one run, **0 LaTeX errors, 0 undefined references or citations**, no rerun warning. The new titles appear in main.toc.
- Nothing committed.
