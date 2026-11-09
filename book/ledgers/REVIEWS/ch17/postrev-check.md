# Ch17 post-revision check (revision + Ch12 Migdal erratum pass)

Verifier: isolated, 2026-11-06. No tex or script edited, nothing committed. Light Python only (Christoffel ranges, ratios).
Sources: tex/ch17/*.tex, figscripts/ch17 logs (exo17_3, abs17_2, check17, interf17_4, sectors17, rank17_6), figscripts/ch16/zrte5_16.log,
figscripts/ch12/migdal_{coh,rates}12.log, ch17 review ledgers, ch12/erratum-migdal.md.

## Verdict: ACCEPT WITH FIXES (F1–F7 below; all are wording or typography, no number is wrong except one table rounding)

## 1. R1 numbers
- WE 17.4 GaAs 403/521: CONFIRMED. F^fol = Z − Z* (28.89 Ga, 35.11 As); (Z² + F²)/Z*² = (961 + 834.6)/4.452 = 403.3 and
  (1089 + 1232.7)/4.452 = 521.5; Z²/Z*² = 215.9/244.6 (interf17_4.log). s17-4 l.101 states both correctly.
- 31× vs 37×: **reviser is right (CONFIRMED 31).** exo17_3.log: elastic one-phonon rate 975.9, "check: rate ratio exact(10 eV)/elastic =
  31.05"; grid point 10.27 eV gives 3.163e4/975.9 = 32.4. The text defines the factor as the exact single-phonon rate at 10 eV over the elastic
  single-phonon rate at 1 MeV (s17-3 l.86–88), which is 31. The ruling's 37 is 3.2e4/871, i.e. [D3]'s misread elastic rate. Summary also says 31.
  Side numbers confirmed: 1.12/1.39 at 0.12 eV (1097/975.9, 23.19/16.73); gain 3e6 at 80 eV (5.27e7/16.73 = 3.2e6).
- WE 17.2: CONFIRMED. α = ωε₂/(n_r ħc) = 1.1728 eV/1.9733e-5 eV·cm × 2.54e-4/3.48 = 4.34 cm⁻¹ (4.58 with √ε∞ = 3.30). Square-root onset:
  2.147 α_Si = 10 → Δ = (4.66/13.3)² = 0.1227 eV; the full edge of eq:13.8-edge gives 40.4 meV (abs17_2.log l.49). Text (s17-2 l.74) states
  40 meV as the full edge and 0.12 eV for the square-root onset alone: correct explanation. 0.012/1.2 meV handovers also reproduce.
- NiO 3.1: CONFIRMED. 8213/2617 = 3.14 (shell over elastic); 3.768 × (0.599/0.885 = 0.676) × (1.149/1.010 = 1.137) = 2.898; remainder
  3.139/2.898 = 1.083 = "8 %", attributed to the elastic halo weighting (exo17_3.log). Wording fine.
- tab:17-endo NiO 7.31/8.20/316 keV: CONFIRMED (exo17_3.log, c_M = 1.36e-4, ω_th = 5 meV; 316.40 keV). "32 / 46" CONFIRMED (32.2, 45.6).
- Electron-only acoustic peak 7×10⁵: CONFIRMED. sectors17.log ratio 4.41e4 × 16.73 = 7.38e5 → "7×10⁵" (opening, 17.1, summary).
- Also checked: CsI 25 % (1.726/1.379 = 1.252), η shift 7 % (1 − 0.9328), 410 MeV (413.6), 10.35 keV everywhere (grep: no 10.3/10.4 left).

## 2. R2/R3
- ZrTe₅: CONFIRMED. zrte5_16.log: ζ(100 meV) 1.25e-15, factor 6.292–6.395 ("6.3 to 6.4"), cone end 2Λ̃ = 0.382 eV; abs17_2.log identical;
  15.6 meV row 1.22e-15 (2.5 %), onsets 23.6/31.2 meV. Text, tab:17-abs-decades, coverage paragraph, summary, nuisance row agree.
- Counting vs linear: CONFIRMED. Key result now states "detection band is the line width Δω_eq", the (B/Δω_eq)^(−1/2) penalty and Lamoreaux's
  (Q_c/2πQ_a)^(1/2); no coherent-overtakes claim remains; e^{1/2} = 1.65, e^{1/4} = 1.28 correct.
  CONCERN (minor, F6): s17-2 l.94 "the gray band m_φ < T is where the advantage of counting has vanished" — at m_φ = T the advantage is still
  1.65 in signal; say "has fallen below e^{1/2} and tends to one". The summary's "vanishes well below T" is right.

## 3. R5/R6
- Diamond/Si "above 14 keV": CONFIRMED. check17.log crossing 14.0 keV = 2.19 Si edges (6.39 keV); R_C/R_Si = 3.09 at 10 keV, so below 14 keV
  diamond's rate is larger and the FOM order (0.493) is wrong there; the sentence ("the cut of the softer crystal reverses the order") is right.
- Pole-factor dispersion LiF/Si 1.37–1.72: CONFIRMED. Bohm–Gross ∫p²dp ω_p²/ω_pl⁵ ∝ v_F⁻³ ∝ ω_p⁻²; free-particle ω_pl² = ω_p² + (p²/2m)²
  gives ω_p^(−3/2). 3.384 × (26.1/16.6)^(−n): n = 3 → 0.87, n = 2 → 1.37, n = 1.5 → 1.72; Ge 0.387 × (15.6/16.6)^(−n) = 0.47/0.44/0.42.
  Remark (no fix needed): the "all p" integral extends the pole beyond its Landau-damping cutoff (2.3 keV in Si); "factor of two in its
  scaling" is the honest reading, and the text says so.
- X_pole "device": CONFIRMED honest in s17-6 l.93 (Si's own X ≈ 25 from the 4 % plasmon share, gap dependence, "artifacts of the prior"),
  tab:17-widths caption, tab:17-rank caption ("include √3 = 1.73 … carry no ordering information"; NaF 1.77/1.73 = +2.4 % consistent), row label
  "pole factor times X_pole", nuisance row. CONCERN (F5): "Any wider or crystal-dependent prior widens the intervals further, so the absence
  of a reading … is robust" is not right for a crystal-dependent prior: X grows as the gap shrinks (17.5 gap limit: Si/LiF 3.2e4), so such a
  prior shifts medians systematically toward small-gap crystals and could *create* a (Si-favoring) reading, not just widen. Replace with: "A wider
  prior only widens the intervals; a gap-dependent one would favor small-gap crystals (17.5), so the order is open, not merely unresolved."
  The 17.5 dispersion factor (LiF 0.87 vs 1.37–1.72) is also absent from the Migdal row's inputs; one clause pointing to it would help.
- 17.6.1/17.6.5 rewrites: CONFIRMED. Process sentences gone; CaWO₄ tensor only by pointer to tab:17-speeds; rms 0.064 / mean −0.048 of
  ln(db/meas) reproduce (−2.9, −10.1, −1.0 %); 134 and 64 (18.99/0.1415, 9.12/0.1415); diamond 1.66 (5.16/3.11); LiF ×1.9 to next tier.
- tab:17-speeds (Griffin audit): CONFIRMED with one rounding. Christoffel over 4e4 directions: GaN 7.63–8.08, AlN 10.52–11.02, ZnO 6.03–6.10,
  CaWO₄ 4.36–5.17 (mean 4.65; 4.257/4.646 = −8.4 %), CsI [100] 2.458, [111] 2.369. WRONG (minor, F4): ZnO tabulated/range = 12.53/6.10 = 2.05,
  table prints 2.06.
- tab:17-crossover (Migdal crossover): numbers unchanged from sectors17.log (0.178 … 5.33 eV; 2.8–2.9 ω_max: 0.178/0.0637 = 2.79,
  0.187/0.0637 = 2.94). CONFIRMED; erratum handling see §4.

## 4. Ch12 erratum in Ch17
- 17.1 qualifier (s17-1 l.39): CONFIRMED in substance. "Up to 1 MeV its rate comes from momentum transfers between about 0.75 keV and 2q_BZ …
  unsized factor … from 3 MeV on ≤ 7 %" matches migdal_rates12.log (f(0.75 ≤ q < 2q_BZ) = 0.998, 0.998, 1.000, 1.000 at 0.42, 0.5, 0.7, 1 MeV;
  f(q<1 keV) = 1 at 0.36 MeV, so it holds down to threshold; 0.327 at 2, 0.074 at 3 MeV). CONCERNS:
  (a, F2) "where the diagonal soft limit … is not the coherent response" overstates: in 0.75 keV–2q_BZ neither form is validated. Write
  "is not known to equal the coherent response".
  (b, F2) The erratum asked to say the factor can be a large *suppression* near threshold (the exact small-q spectrum sits at the plasmon,
  beyond the 1.2–1.8 eV open there; migdal_rates12.log: identity-form rate 0 below 1 keV at 0.36 MeV). Add one clause; "unsized" alone hides
  the likely direction.
  (c) The "29 % of whose rate comes from q < q_BZ" reads as if only 29 % is affected; the band holds 100 % at 1 MeV. Reorder: "… the 1 MeV
  column, all of whose rate lies in that band (29 % below q_BZ)".
- Nuisance row (tab:17-nuisances): CONFIRMED (14.9×, 0.75 keV, nearly all up to 1 MeV, 29 %, 7 % at 3 MeV). Add "33 % at 2 MeV" as in
  tab:12-nuisances (F3, optional but the fig caption depends on it).
- Silent reliance elsewhere: CONCERN (F1). s17-1 l.17: "Since the sum rule eq:12.4-harm holds at every momentum transfer, the lattice only has
  to conserve energy" — after the erratum this holds at every q only in the incoherent form; add "(in its incoherent form; below 2q_BZ see the
  qualifier below)". Same section l.22 "lattice exceeds Migdal by 6×10⁷ at 1 MeV" precedes the qualifier and inherits the factor (covered if F1
  points forward). fig:17-sectors caption says "below 1 MeV"; at 2 MeV a third of the rate is in the band → "below about 2 MeV (7 % at 3 MeV)"
  (F3). tab:17-crossover thresholds: no fix needed (lattice side falls ×65 per 0.1 eV; erratum agrees), and the 1 MeV column is qualified; the
  3 MeV column (7 %) is within the stated "≤ 7 %". WE 17-crossover (10 MeV): band share 0.000 — no reliance. 17.4 window row keeps
  "order of magnitude only" (Si window 0.9–1.3 keV outside the 0.75 keV domain): CONFIRMED. 17.5/17.6 pole factor: impulse regime,
  electron momentum p not nuclear q — unaffected: CONFIRMED. Summary 17.1 paragraph carries no qualifier; acceptable (it quotes no
  sub-MeV Migdal rate), optional clause.
- Typography from the erratum pass (F7): s17-1 caption "…\cref{tab:17-nuisances}.One-phonon" and l.39 "…(\cref{tab:17-nuisances}).\Cref{…}"
  lack a space (LaTeX prints no space after the period).
- Ch12 qualifier text: CONFIRMED physically. s12-4 key result gives the q ≪ q_BZ limit (m_e/M)²(2q²/e²)L/(2πn_κ) with L the head of −ε⁻¹,
  1/14.9, medians 17.4 vs 4.5 eV, "between the two not computed"; s12-3 opening "q ≳ 2q_BZ"; Bragg-check sentence limited to the diagonal,
  direction-averaged sum; tab:12-nuisances row "within 15 % only for q ≤ 0.75 keV … ≤ 0.2 % of the rate … nearly all up to 1 MeV, 33 % at 2,
  7 % at 3 MeV" matches migdal_coh12.log (coh/ident 1.029 at 0.5, 1.152 at 0.75, 1.381 at 1.0 keV) and migdal_rates12.log. Nit: 1.152 is
  15.2 %, so "within about 15 %" is the exact reading. s12-4 l.5 phrase "the incoherent lattice factor, which is the coherent zero-phonon
  process … averaged over directions" conflates the factor with its zero-phonon part; optional rewording ("whose zero-phonon part equals …").

## 5. Notation renames
CONFIRMED. grep over tex/ch17: no σ_n, ω_top, ω_×, bare F_κ, bare σ_j; σ_p (8 uses), ω_max, ω_th^× (6, s17-1 incl. fig caption and WE),
F^fol_κ (s17-4), σ^prov_j (s17-6); n_B only as Bose function with argument. NOTATION.md rows 1198–1211 present with clash notes.

## 6. Summary and nuisance table vs final sections
CONFIRMED: 31×, 1810/842, 0.178/0.307/5.33 eV, 7×10⁵, 10.35 keV, 0.38–1.17 eV gap, e^{m/2T} with band condition, 5.47e-4, 5.7e5, dispersion
1.4–1.7, 1.73/0.46 vs 1.69/0.49, 0.968, 0.315, 0.884 → 0.741, 0.968 → 0.781, NaF 0.315 → 1.000, GaSb 0.973/0.837; TeO₂ vs CaWO₄
0.987 → 0.956 (rank17_6.log MC 0.987). No disagreement found.

## Fixes
- F1 s17-1 l.17: qualify "eq:12.4-harm holds at every momentum transfer" (incoherent form; pointer to the Migdal qualifier).
- F2 s17-1 l.39: "not known to equal the coherent response"; add that near threshold the factor is likely a large suppression (plasmon-shaped
  exact spectrum); make clear the whole 1 MeV rate lies in the band (29 % below q_BZ).
- F3 fig:17-sectors caption "below about 2 MeV" (or "up to 1 MeV fully, a third at 2 MeV"); optionally "33 % at 2 MeV" in the nuisance row.
- F4 tab:17-speeds ZnO 2.06 → 2.05.
- F5 s17-6 l.93: replace the "crystal-dependent prior widens the intervals … robust" clause (a gap-dependent X favors small-gap crystals).
- F6 s17-2 l.94: "advantage has vanished" → "has fallen below e^{1/2} and tends to one".
- F7 s17-1 caption and l.39: missing spaces after "." before "One-phonon" and "\Cref".
