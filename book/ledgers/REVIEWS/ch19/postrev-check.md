# Ch19 post-revision check (isolated verifier, 2026-11-06)

Scope: tex/ch19/*.tex (with the summary), tex/appD/D-45.tex, the narrow edits to E-11/E-23/E-25, the Ch19 F rows, figscripts/ch19 (bal19_5, def19_4, lind19_3, rec19, limit19_6b logs), the review ledgers and rulings R1–R8, and tex/ch20/s20-5.tex.
Method: an independent sympy and numeric rederivation in my scratchpad (no script was edited), checked against the source text sources/19.4/1803.02903.txt and the logs.

## 1. R1/R2 recalibration

| Item | Verdict | Note |
|---|---|---|
| Two-gain model (g_Luke = eV/3.75 for the Luke phonons, g_cal = eV/3.82 for the scale and subtraction) | CONFIRMED | Source Eq. (1) and fn. 2: E_R = E_φ − E_Q eV_b/ε with ε = 3.82 eV. The phonon scale is set by ER with y = 1, E_φ = E_R(1 + eV/ε). The physical Luke energy is n_Q eV = ω eV/ε_eh, and E_Q is photon-calibrated (= ω for ER). Hence Y = (1+g_cal)[(1−δ)(1−d_NR) + r g_Luke f]/(1 − d_ER + r g_Luke) − f g_cal, which is eq:19.5-identity. η_NR (= Y_ph) is the linear rescaling of the true NR energy, 95.2^{+0.9}_{−0.7} % at 95 % C.L. (source l.784): confirmed. |
| Sympy | CONFIRMED | The identity at r = 1, d = 0 reduces to 1 + (g_cal − g_Luke)(1−f)/(1+g_Luke). eq:19.5-widen and the collection-alone formula for r follow exactly. The D.45 algebra (l.36–76) matches. |
| Offset at 4 V | CONFIRMED | 0.006394, which rounds to 0.0064 (0.0067 with DC-67's 3.7468 eV). |
| Stored alone | CONFIRMED | 0.04200, edge 0.04907, so 0.042 / 0.049. Lindhard f = 0.346 gives 0.0422. |
| Collection alone | CONFIRMED | 𝔯 = 1.1284; the band (Y = 0.961 / 0.945) is 1.0992–1.1517; Lindhard gives 1.1337. |
| Mixture, widening | CONFIRMED | Half mixture: 0.0210 at 𝔯 = 1.0642. Central value 0.0584 / 0.0747 at 𝔯 = 0.95 / 0.9; 95 % bound 0.0814 at 0.9. |
| 40 V | CONFIRMED | 0.91886 / 0.94737 / 0.93233, difference 0.0285 (3.56 half-widths); high-bias limit 0.9121. |
| C_cal | CONFIRMED | 0.651 (4 V) and 0.382 (40 V); 0.623–0.740 for f = 0.269–0.497. |
| Energy dependence | CONFIRMED | 0.948 / 0.964 / 0.956 (0.75 y_C); stored alone 0.9515–0.9536. |
| Gap offset | CONFIRMED | ρ_g − 1 = 0.212 matches δ = 0.042; slope 0.0037 per 0.02. |
| Bound 0.055 under (e); 0.049 with the book ε | CONFIRMED, with a wording CONCERN | 0.049 is a genuine bound, not just a point value. Under (a)–(d) with ε_eh known, the first term of eq:19.5-bound grows with 𝔯, so the maximum e_st over 𝔯 ≥ 1 is at 𝔯 = 1, δ = x = 0. As written, "at 𝔯_coll = 1" in 19.4 l.90, 19.5 and F row 800 reads as a single-point reading. **Fix:** "0.049 under (a)–(d) with ε_eh = 3.75 eV (attained at 𝔯_coll = 1 with no other deficit)". |
| ΔE_zp widening | CONFIRMED | 8.1e-4 (Si, 10 keV) → 0.056; 1.4e-3 (Ge) → 0.065. |
| y_C(20 keV) = 0.324 | CONFIRMED | Source Eq. (4), a = 0.247 keV⁻¹, k = 0.146. y_C = 0.3236 (y_L = 0.3463); 0.2692 and 0.4969 at 10 and 100 keV. The source's "~75 %" collection is relative to y_C (Fig. 12 caption): confirmed. |
| WE wording on Lindhard | minor CONCERN | "which that analysis finds too high below 20 keV" (19.5 WE): the source says that Lindhard over-estimates the low-energy data of its Ref. [27] and that the CDMS data are consistent with y_C below 20 keV. The source also says the fit improves if y_C is ~5 % low at 10–20 keV, i.e. f ≈ 0.34, which is near the Lindhard variant. **Fix:** "which overestimates the low-energy data that analysis cites"; optionally note the 5 % remark and that the Lindhard variant (1.134 / 0.0422) covers it. |
| Ge and condition (e) | minor CONCERN | Tab. 19.1 and the nuisance row apply "(a)–(e)" to Ge, but (e) is stated with the Si 3.75/3.82 eV and the Ge reconstruction's adopted ε is not discussed. **Fix:** one clause in the 19.5 description list or the table caption: (e) for Ge refers to the Ge analysis's adopted pair energy, and its offset is not evaluated. |
| r′ sensitivity "0.020 to 0.025" | nit | Log: −0.0198/+0.0205 (stored) and −0.0246/+0.0256 (collection). Print "0.020 to 0.026". |

## 2. R6 structure

| Item | Verdict | Note |
|---|---|---|
| Machinery and (a)–(e) only in 19.5; 19.4 points | CONFIRMED | 19.4-calib/-bounds give the data, the definitions in words and the result. eq:19.4-fDF, eq:19.4-bound, the C_cal paragraph and the (a)–(d) list are gone, and no reference to them remains (grep). The description list is in 19.5 l.~142–148. |
| Merged lim:19.5b | CONFIRMED | Two panels (Y_ph; 95 % bound vs 𝔯) with the ε_cal = ε_eh curve, the f band and the Ge point. lim:19.4b and limit19_4b are unreferenced. The log values match the caption (dot at 1.1283; 0.0814 at 0.9; Ge 0.0638). |
| Ge "≥ 0.23, not conservative" | CONFIRMED | 2(0.0638)/(0.8 × 0.7) = 0.228; screened 0.261; 0.266 at T_d/E_R = 0.6. The Pb-in-Ge caveat is stated. |
| Grown-in defect term | CONFIRMED | E_st,0 term added in eq:19.6-leebound, with the mounting assumption. The 19.6 bounds quote their conditions and 0.081 at 𝔯 = 0.9. |
| 19.5 → sec:20.5-sign | **WRONG (attribution)** | 19.5 l.151: "the quasiparticle yield of the film near threshold, between 2Δ_BCS and 4Δ_BCS, can raise it to 1.04–1.09". In 20.5 (l.72–76), the 1.04 / 1.09 values come from the two-film geometry. They arise once the Luke spectrum reaches the ~3 meV threshold of the niobium-like film, converted with 2Δ_s/E_ath near one. Near the Al threshold the single-film near-gap gain is −0.048 to +0.06. Δ_BCS in 19.5 is aluminum's (0.36 meV). **Fix:** "...but near the pair-breaking threshold of a second, higher-gap film (about 3 meV in the two-film geometry of \cref{sec:20.5-sign}) the film yield can raise it to 1.04–1.09". The 0.935–0.998 range, "sign open" and the sub-gap-loss wording are consistent. |
| 1.128 vs the 20.5 range | CONCERN | 20.5 l.78 states that the CDMS collection-alone 𝔯 is "more than 0.1 above one, outside every value of this estimate" (max 1.09). Neither 19.5 nor the summary says so. The summary ("1.128, a value whose sign relative to one depends on the film yield") reads as if 1.128 were reachable. **Fix:** add a clause in the 19.5 WE (collection alone) and the summary: "above the largest transport value of \cref{sec:20.5-sign}, 1.09". |

## 3. R3–R5

| Item | Verdict | Note |
|---|---|---|
| Soft-collision band as a sensitivity | CONFIRMED | 19.3 l.76: −11 / +13 / +40 % (log −10.5 / +13.2 / +39.7). The ε^{1/6} law is tied to x^{1/3}, and the TF x^{1/2} tail gives a finite y_L (l.61; 2/(λJ) = 3.29). The nuisance row, summary and F row agree. Ruling R3's "+39" is a rounding slip; 40 is right. |
| L shell 2/3 and 174 eV withdrawn; 161 eV | CONFIRMED | Σ = 5.082 gives Ī = 161.1 eV, against 173.0 eV adopted. No "174" or "two thirds" in Ch19/F. "61 % of the oscillator strength" is a different, correct statement. |
| 336 eV | CONFIRMED | 352 × (1 − 0.044) = 336.5 (text l.27/49, Fig. 19.2 caption). 352 / 399 eV recomputed with M = 26.16 / 67.65 GeV. |
| 65 fs | CONFIRMED | 2πħ/64.1 meV = 64.5 fs (19.1, E-11). |
| 2.3° | CONFIRMED | √2 × 1.6°. |
| 1.9 % | CONFIRMED | 3.03 % × 0.62 = 1.88 % (rec19.log). |
| Migdal 2.3–4.4e-4 | CONFIRMED | 0.038 × 6.07e-3 × {1, 1.69, 1.92} = 2.31 / 3.90 / 4.43e-4. |
| 61 meV, ΔE_zp sign | CONFIRMED | 3 × 40.9/2 = 61.4 meV. Estimate 0.07 eV; both signs stated. |
| R₀ | CONFIRMED | Criterion 3V₀(a/r)⁴ > Δ (19.6 l.97) gives a(3V₀/Δ)^{1/4} = 11.6–21.9 for 13–166 µeV. |
| Electron-recoil displacement onset | CONFIRMED | 2E(E + 2m_e)/M = 12.5 eV at E = 0.141 MeV. 19.6 now says "below 0.14 MeV cannot displace". |
| Sarkis U_FP | CONFIRMED | Called "Frenkel-pair creation energy" by its authors, a threshold average, three times the configurational 6.8–9.7 eV. |
| C_cal sign | CONFIRMED | Removed from 19.4. The 19.5 sign (−C_cal d_ER) matches ∂Y/∂B < 0 in D.45. |
| Others | CONFIRMED | 298 eV (log 297.6); 58 µs; f_ret 0.525 gives 1.156; flashing defined. |

## 4. Consistency and stale strings

| Item | Verdict | Note |
|---|---|---|
| Summary and nuisance table vs sections/logs | CONFIRMED | Matches on 0.006 / 0.0064; 0.042 / 1.128 / 1.099–1.152 / 1.134; 0.058 / 0.075; 0.947; 0.028; 0.055 / 0.049 / 0.064; 0.056 / 0.065; 0.081; ρ_g 0.21; 0.0037; 1.407; 3.5–4.1 %; Migdal; Lindhard sensitivity. The ε_eh = 3.75 / ε_cal = 3.82 split is uniform across 19.4, 19.5, 19.6, the summary, F row 800 and D.45. |
| Tab. 19.1 | CONFIRMED | 0.19 (0.21) / 0.27 (0.31) with y_C damage fractions 0.731 / 0.503; p_surv 0.90–1.00 and 0.70–0.84; 6.6 % at 300 eV; m_χ ≥ 0.770 GeV. |
| Grep for 1.154, 1.144, 0.952-as-40V, 0.9195, 0.086, 174 eV, two-standard-deviation, "does not depend on ε_eh" | CONFIRMED (clean) | The remaining 0.952 / 0.048 hits are the measured Y_ph / f_DF, which is correct. |
| **395 eV** | **WRONG (stale)** | tex/appE/E-23.tex l.3 ("below its threshold of 395 eV") and l.27 ("dense near 352 and 395 eV"). Editor note 19.2 asked for this. The revision filed it under LOOSE-ENDS although E-23 was already open for narrow edits. **Fix:** 395 → 399 at both places (254 eV is still below threshold). |
| g_L (Luke) | CONFIRMED in tex; stale in NOTATION.md | No tex file uses g_L for the Luke gain. The remaining g_L hits (16.6, 19.3, F row 771) are Lindhard's function. Ch20's local g = f_det g_Luke is defined in place. NOTATION.md l.1449 (E.12 row: "Γ_L against g_L, the Luke gain") and l.1579 (entry 55: "g_Luke is g_L") are stale. **Fix:** g_L → g_Luke in both rows. |

## 5. Si mass

CONFIRMED. 28.0855 u × 0.931494 = 26.161 GeV, labelled "natural isotope mixture" in 19.1 l.81 and 19.4 WE, and used throughout Ch19; the 352 eV threshold needs 26.16 to reproduce. Ch5.3, 5.6, 11.4 and 12.5 also use 26.16 (labelled or "natural"). Ch1.3, 5.1 and D.13 use 26.06 GeV, labelled as the ²⁸Si atomic mass (27.9769 u). Each use matches its label. The book-wide ruling (CORRECTIONS 14) is still owed; the effect is ≤ 0.4 %.

## 6. Notation

CONFIRMED for tex: g_Luke, g_cal and ε_cal are used consistently in Ch19, D.45, the F rows and Ch20. Only the NOTATION.md residue in item 4 remains.

## Verdict

ACCEPT WITH FIXES:
1. 19.5 l.151: attribute 1.04–1.09 to the second film's ~3 meV threshold (two-film geometry), not to "2Δ_BCS–4Δ_BCS" of aluminum.
2. 19.5 WE and summary: say that 1.128 lies above the largest transport value of 20.5 (1.09).
3. E-23 l.3 and l.27: 395 → 399 eV.
4. NOTATION.md l.1449 and l.1579: g_L (Luke) → g_Luke.
5. Wording: 0.049 is a bound under (a)–(d) with known ε (19.4 l.90, 19.5, F row 800). Optional: the Ge (e) clause, the Lindhard-overestimate phrasing, and 0.020–0.026.
