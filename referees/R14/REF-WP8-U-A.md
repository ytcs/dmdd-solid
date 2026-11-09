# R14 referee REF-WP8-U-A (hostile, isolated): returns/R13/WP8-U.md + WP8-U-table.csv

Read: the return, the CSV, code/WP8-U/* (all), returns/R8/WP0-v3.md, WP2-v3.md, WP5-v3.md (greps at the cited items), CONVENTIONS, NOTATION,
CONTROLS, DONE, LIMITS, STATEMENT. Not read: referees/, state/, briefs/ (except this brief), returns/R14/, WP8-F/WP8-R, LAUNCHES/log.
Full texts fetched with lit.py into literature/papers-r14-REF-WP8-U-A/: 2008.08560, 1910.10716, 1901.07569, 2004.10709, 1910.02091,
2109.04473, 2210.13516, 1905.13744. PDFs and HTML deleted; only pdftotext `.txt` extracts remain. Line numbers below are in those extracts.
`checks.py` rerun: 23 PASS, 0 FAIL, 16 FLAG, 0.11 s, identical to the return. No simulations were run.

## Verdict table
| # | Main claim | Verdict | Reason |
|---|---|---|---|
| V1 | Pool: 47 materials; 10 S / 30 C / 3 R / 4 X (+7 families) | STANDS | CSV `verdict` rows count 10/30/3/4 = 47 |
| V2 | The 10 SURVIVORs pass S1–S3 | STANDS WITH CORRECTION | GaAs S2 PASS rests on an [E] tag (not evidence). By the return's own standard, GaAs is COND (§F3) |
| V3 | Screening FAIL/COND verdicts and exclusions | STANDS WITH CORRECTION | FAIL and COND are given on equivalent evidence (NiPS₃/h-BN vs ZrTe₅; PE vs SiC); S1 PASS [E] vs α-SiO₂ COND (§F3) |
| V4 | CSV provenance (U0) and the 34-row trace | STANDS | 0 mismatches against the cached extracts / full texts (§F1). The extract-vs-live check is limited to MP (§F1) |
| V5 | Source disagreement 1: 2008.08560 Table I n_e is half of 4 e/atom; ħω_p(C) = 22 eV implies ≈ 2 e/atom | STANDS (CONFIRMED) | n_e/N = 2.00, 2.01, 2.03 for Si, C, SiC; 31.16/√2 = 22.0 eV (§C1) |
| V6 | Source disagreement 2: 1910.10716 c_LA for GaN/AlN/quartz/ZnO/NaCl is suspect | STANDS WITH CORRECTION (UNRESOLVED) | Transcription is exact. "Paper wrong" is not settled: no measured source was read. §0 states the magnitude wrongly (§C2) |
| V7 | Other FLAGs (diamond ω_T, Ge E_g, 3C θ_D, c_s naming, MP/JARVIS ρ) | STANDS WITH CORRECTION | The transcriptions are confirmed. "Identical moduli" is false: 3C G_V = 197.6 vs 190.6/190.7 GPa (§C3) |
| V8 | Radiopurity screen (§0 row 5, §4.3, IF-U3) | STANDS WITH CORRECTION | KTaO₃ and InSb arithmetic is right. "Ge: none" is false (⁷⁶Ge). The Te/Pb/Zn/Cr values come from lower-limit half-lives and are printed as activities (§E2) |
| V9 | IF-U1: under WP8-F's quoted rule, the InSb and PbS/PbSe/PbTe ε rows drop | FALLS (as stated) | PbS passes that rule. 11 more materials fail it and are not listed. The return's own "<20 cm⁻¹ = failed run" rule is not applied to ε₀ (§E1) |
| V10 | IF-U4: the soft-mode ε₀ list (Pb salts, KTaO₃) | STANDS WITH CORRECTION | SrTiO₃ ε₀_DFT = 9.96 (cubic Pm-3m) is unflagged. InSb ε₀ᵈ 22.9 < ε_∞ᶠ 23.7 (§E1) |
| V11 | IF-U5: the ZrTe₅ Δ of 1910.02091 is ambiguous | FALLS (REFUTED) | Eq. (1.1) l.67 says "2∆ is the band gap"; l.701–703 say "23.6 meV, which corresponds to ∆ = 11.8 meV". Δ_D = 11.75 meV (§C4) |
| V12 | YIG 𝓃_spin = 20/a³ as an "ordered-spin number density" | STANDS WITH CORRECTION | 1905.13744 l.260–261: S_cell = 10 per Ω = a³/2, so 20/a³ is the net spin density S_cell/Ω. The Fe number density is 40/a³ (§C5) |
| V13 | LU1 (LST) | STANDS WITH CORRECTION | The data are quoted correctly and U1 is reproduced. The chain's source is the derivation in WP2-v3 (4.3), not a data table (§B) |
| V14 | LU2 (valence f-sum → ω_p) | STANDS WITH CORRECTION | ω_p is NOTATION's all-electron symbol. The status is ESTIMATED: one material checked, and the chain is a truncated sum rule, not a consequence of the f-sum (§B) |
| V15 | LU3 (Tamura) | STANDS WITH CORRECTION | The source is [UNVERIFIED], which fails rubric (b). U7's "as 1901.07569 states" overclaims (§B) |
| V16 | LU4 (elastic θ_D) | STANDS | U2 reproduced (C +0.1 %, Si −1.5 %, Ge −10 %, 4H/6H −3 %). The 3C outlier is flagged separately |
| V17 | Cross-route checks U1–U10 (§0 row 7) | STANDS | All reproduced. "ρ(MP)/ρ(JARVIS) ≤ 5 %" = LiF −4.9 % |
| V18 | WP5-v3 cross-reference (Si ε_eh 3.749 eV, F 0.119, 123 K) | STANDS | WP5-v3 l.252/546. 2004.10709 Table I row [29] (txt l.308, l.302) |
| V19 | Consistency with WP0-v3/CONVENTIONS/NOTATION | STANDS WITH CORRECTION | ε_∞ ≠ ε₀ for Si/Ge/C in §4.1; τ_ph is a retired symbol; ω_p clash; SrTiO₃ polymorph rule (§D) |

## A. Rubric (a): DERIVED steps
- The return marks no step DERIVED. Its closed forms are tagged [E] and recomputed in checks.py. I recomputed these independently:
  - ρ(a_exp): Al₂O₃ 3.987, ZnS 4.065, Si 2.329 g/cm³;
  - Voigt c_L, c_T and Anderson θ_D: 6H 12.18 km/s / 1159.9 K, GaAs 4.816 km/s / 331.1 K, γ-LiAlO₂ 8.098 / 4.555 km/s / 686.8 K;
  - 𝓃_e^{val} and ħω_p^{val}: AlN 3.835×10²³ cm⁻³; Nb 19.42 eV; C 31.15 eV; Si 16.63 eV;
  - a_rad: KTaO₃ 4.61×10³ and InSb 121 Bq/kg.
  All agree.
- The Tamura form τ⁻¹ = V_a g₂ω⁴/(4πv_m³) follows from Γ = (π/6)V_a g₂ω²D(ω) with the total Debye DOS D = (ω²/2π²)Σ_j v_j⁻³ = 3ω²/(2π²v_m³).
  The coefficient is right, but the return never derives it and only cites it [UNVERIFIED]. ν-form: 1.645e-45·(2π)⁴ = 2.56e-42 s³ ✓.
- U0b ("all 57 arXiv IDs verified") checks a JSON written by the same agent. It is not independent. My live arXiv spot-check, 8/8 titles match: 2603.22390,
  2607.15338, 2604.21969, 2511.20461, 2507.07119, 2207.07640, astro-ph/0204411, 2105.06781.

## B. Rubric (b): proposed LIMITS rows
- **LU1 (LST).**
  - Data: 2008.08560 Table I (txt l.329–341; HTML table) was read correctly:
    - 3C: ε₀ 9.7, ε_∞ 6.5, ω_TO 98.7, ω_LO 120.5;
    - 6H ⊥: 9.67/6.6, 97.7/119.7;
    - 4H ⊥: 9.76/6.6, 97.0/119.5.
  - U1 reproduced: 1.492/1.491, 1.465/1.501, 1.479/1.518.
  - Correction 1: the ⊥ assignment of the first member of each pair is an assumption the table does not state. With the second member, 6H gives
    (120.3/98.8)² = 1.483, so the 3 % bound survives either way.
  - Correction 2: the chain's derivation is WP2-v3 (4.3) ("One polar branch [D]", ε = ε_∞(ω_L²−ω²)/(ω_T²−ω²)). Cite that, or Lyddane–Sachs–Teller,
    as the source. The table is the test, not the source.
  - Validity "T → 0" is too narrow: LST holds at any T with the renormalised frequencies. The real restriction is undamped, single-mode.
- **LU2 (ω_p).**
  - Correction 1: NOTATION l.191 reserves ω_p for the *all-electron* plasma frequency, and WP0-v3 uses ω_{p,e}. LU2 must read
    (ω_p^{val})² = 4πα𝓃_e^{val}/m_e, the return's own §1 symbol.
  - Correction 2: a valence-only plasma frequency is a *partial* sum rule; it truncates CONVENTIONS §13 #12. It does not follow from the f-sum.
    Status ESTIMATED, not CHECKED: one material (Si, EELS 16.6 ± 0.1 eV, 2004.10709 txt l.324) agrees.
  - Correction 3: the return's own diamond comparison is against a defective source value (§C1), so it is not a second check.
- **LU3 (Tamura).**
  - The source "Tamura PRB 27, 858 (1983) [UNVERIFIED]" fails rubric (b): it was not quoted from the full text. Downgrade to CONJECTURED-source /
    ESTIMATED-form until it is read.
  - U7 says the ordering Ge > Si > C is "as 1901.07569 pp.4–5 states". The text (txt l.307–321) says only that diamond has "a much smaller number of
    isotopic scattering sites … as compared to Si and Ge" and that Ge lifetimes are isotope-limited. It states no Si/Ge ordering. Reword it as
    "consistent with".
- **LU4 (θ_D).** Stands. Validity "isotropic, acoustic only" is right. The leading correction is right, but it should add that the calorimetric θ_D
  in the tables is the T → 0 limit by definition.

## C. Rubric (c): claims that a paper or database is wrong
- **C1. 2008.08560 Table I n_e/ω_p: CONFIRMED.**
  - Printed values: N = 1.76, 0.5, 0.96; n_e = 3.54, 1, 1.95 (10²³ cm⁻³); ħω_p = 22, 16.6, 22.1[33] eV (txt l.315–318; HTML identical).
  - So n_e = 2.0 e/atom in every column, and the text gives no definition (grep: no "electron density" text).
  - ħω_p consistency:
    - Si 16.6 eV needs 4 e/atom (2.00e23 → 16.6 eV);
    - SiC 22.1 eV ≈ 4 e/atom (23.0 eV);
    - C 22 eV = 31.16/√2 (2 e/atom).
  - Therefore the n_e column is internally inconsistent with the Si and SiC ω_p values, and the C ω_p is consistent with the n_e column but not with 4 e/atom.
  - Correction to IF-U9/FLAG 1: say "C ω_p = 22 eV is suspect". Its experimental value is not in the sources read; ~33 eV is [UNVERIFIED].
    The return's "n_e column inconsistent with the ω_p column" is true for Si and SiC only.
- **C2. 1910.10716 Table I c_LA: transcription CONFIRMED; error UNRESOLVED.**
  - The HTML table and lit_values.T1 agree for all 24 rows: c̄_s^{LA} in 10⁻⁵ c (GaN 4.17, AlN 5.70, SiO₂ 5.76, ZnO 4.18, NaCl 1.19).
  - App. A3 (txt l.936–940): c_LA is the DFT ω_LA/q averaged over a 20×20 grid on |q| ≈ 10 eV.
  - The JARVIS moduli (quartz B 39.4, G 44.1 GPa, ρ 2.60) give c_L ≈ 6.1 km/s, against 17.3. That supports the suspicion, but no measured c_L was read.
  - "Anisotropy" (FLAG text in checks.py) cannot produce a factor 2.8, so drop it as an explanation.
  - §0 row 6 is arithmetically wrong. The check prints c_L/c_LA − 1 = −0.41, −0.37, −0.64, −0.53, so c_LA exceeds the elastic estimate by
    **+69, +59, +178, +113 %**, not "37–64 %". FLAG 2 in §6 and note ‡ are worded correctly.
- **C3. Other disagreements.**
  - Confirmed in the full texts:
    - diamond ω_TO = 148 (2008.08560) vs 141 meV (1901.07569 txt l.85);
    - Ge E_g = 0.54 (1901.07569 l.80) vs 0.67 eV (1910.10716);
    - 3C θ_D = 1430 K with ħω_Debye = 122 meV (self-consistent) vs 1200 K / 103 meV for 4H/6H.
  - "Identical moduli": the JARVIS extract gives G_V = 197.62 (3C) vs 190.63/190.73 GPa. Write "near-identical (≤ 4 %)", as checks.py does.
  - The return does not adjudicate Ge 0.54. It should say which value a FOM takes (IF-U2 implies the low-T experimental one, which neither paper gives).
  - The claim that JARVIS `ehull` = 2.93 eV/atom for all SiC polytypes is CONFIRMED against the extract (2.9276/2.928/2.9277).
  - The claim that the GaAs DFPT ε₀ = 3098 was dropped is UNRESOLVED: the extract stores `na`, and 3098 appears nowhere in code/ or data/.
- **C4. 1910.02091 Δ (IF-U5): the ambiguity claim is REFUTED.**
  - Eq. (1.1) (txt l.64–67): "2∆ is the band gap".
  - l.417: "∆ which is half the band gap".
  - l.701–703: "band gap … 23.6 meV, which corresponds to ∆ = 11.8 meV". The Table 1 header "∆ (meV)" is that half-gap.
  - Δ_D = 11.75 meV (Exp. [52]) and 11.8 meV (NR = experimental structure, DFT). Close IF-U5. The CSV value is right; the flag is not.
- **C5. 1905.13744 YIG.**
  - The quotes are verbatim (l.204–207, 260–264: S_j = 5/2, S_cell = (12 − 8)×5/2 = 10 per Ω = a³/2, a ≃ 12.56 Å, n_s = 20/a³ ≃ (4.6 Å)⁻³,
    J_eff ≃ −0.35 meV, ω ≃ k²/(7 MeV)).
  - Since 20/a³ = S_cell/Ω, it is a net spin (ħ-unit) density. The return's definition "ordered-spin number density" is wrong: the Fe density is
    40/a³ and the net moment count is S_cell/Ω. Rename the 𝓃_spin row, or define it as S_cell/Ω.
  - IF-U7's "therefore used a DFT-relaxed cell" is an inference from a coincidence. Tag it [E], not a finding.
- **C6.** The other quotes checked against the full text are exact:
  - 2109.04473 l.121 (Δ = 0.3 meV, E_F = 11.7 eV);
  - 2210.13516 Table I l.151–155;
  - 1910.02091 Fig. 3(d) l.627 (ρ 6.089), Tables 1–2 (v_F, κ tensor, g = 2), "Organic materials are soft" l.727;
  - 1901.07569 Table I (all values used), ¹⁴C note l.548–562;
  - 1910.10716 Table III (all 24 a, c 'exp.' values).
  - IF-U6 should be stronger: 0.3 meV is not the bulk BCS gap of Al (1.764 k_BT_c ≈ 0.18 meV for T_c = 1.2 K [UNVERIFIED]). Any FOM must carry
    the factor ~1.7.

## D. Rubric (d): consistency with WP0-v3, CONVENTIONS, NOTATION
- **D1.** Survivor table §4.1 gives Si ε_∞ = 10.7ᵈ with ε₀ = 11.7ᶠ, Ge 15.2ᵈ/16ᶠ, C 5.32ᵈ/5.7ᶠ. Nonpolar crystals have no ionic part (WP2-v3 l.285
  "zero ionic ε part in Si"; Z̄* = 0ᵉ in the same table), so ε_∞ = ε₀. The DFT ε_∞ must not sit next to the FT ε₀ as if they were distinct quantities.
  Use the FT value for both.
- **D2.** ω_p for a valence quantity (LU2, §4.1 column header "ħω_p") clashes with NOTATION l.191 (all-electron). Use ω_p^{val} throughout.
- **D3.** τ_ph for the phonon lifetime (U6, coverage column) reuses the symbol NOTATION l.234 retired from W0 (renamed t_ph = T/ω_ph). Use τ_life,
  the source name.
- **D4.** The CSV properties `screen_C1..C3` collide with CONTROLS C1–C8, which the return says it avoids (§0 l.17). Rename them `screen_S1..S3`.
  §0 row 2 also says "solid He, which fails **C1**"; it should say S1.
- **D5.** The polymorph rule ("experimental space group", §1) is broken for SrTiO₃: every property row uses JVASP-8082 (Pm-3m, cubic), while the
  screening row says the low-T I4/mcm phase is JVASP-269. At mK, the experimental phase is I4/mcm.
- **D6.** Coverage matrix vs §4.1: Ge and GaAs ρ are "D" in §4.2 but 5.33ᵉ/5.32ᵉ in §4.1. One best-provenance ranking must be used.
- **D7.** 3C-SiC ε_eh 5.7–7.7 is "†, estimated in their text" (caption, txt l.348). §0 row 4 counts SiC among the *measured* ε_eh. Restrict this to 4H/6H.
- Consistent: Ω = a³/2 for YIG; c_ν/c_avg split (CONVENTIONS §13 #9 adopts c_ν); 𝔔_pol for the quality factor; 𝓃_e; Δ_D as the half-gap.

## E. Rubric (e): material values and provenance
- **E1. DFPT ε rows.**
  - The return's own rule says "max_ir_mode < 20 cm⁻¹ = failed IR run → GAP". It is applied to ω_T only. The DFPT ε₀ from the *same* DFPT run is
    kept for 12 materials: NaI 0.28, ZnS 0.77, ZnO 0.75, SrTiO₃ 0.62, γ-LiAlO₂ 1.38, Bi₂Se₃ 3.25, LiF 0.86, PbTe 1.88, KTaO₃ 2.19, NaCl 0.34,
    3C-SiC 3.39, c-BN 2.42, PE 0.31 (cm⁻¹).
  - Either justify the ε₀ of those runs, or apply the rule. Several agree with experiment (LiF 8.82, NaCl 5.62 [UNVERIFIED exp]), so justification is
    possible, but it is owed.
  - **IF-U1 is wrong as stated.** Under the WP8-F rule it quotes (IR > 50 cm⁻¹ and OptB88 gap > 0.3 eV):
    - PbS (66.83 cm⁻¹, 0.564 eV) *passes*;
    - InSb (gap 0.0), PbSe (46.06) and PbTe (1.88) fail;
    - so do NaI, ZnS, ZnO, SrTiO₃, γ-LiAlO₂, Bi₂Se₃, LiF, KTaO₃, NaCl, 3C-SiC, c-BN and PE, which IF-U1 omits.
    - Rewrite the list from data/jarvis_extract.json.
  - **SrTiO₃ ε₀_DFT = 9.963** is listed in §4.1 without a warning. It is the archetypal incipient ferroelectric, the same class the return puts KTaO₃ in.
    ε_ionic = 3.6 from a failed-IR cubic run is unusable. Add SrTiO₃ to IF-U4.
  - **InSb**: ε₀ᵈ 22.9 < ε_∞ᶠ 23.7 in the same row is unphysical. The DFPT came from an OptB88-metallic (gap 0.0) run, admitted by the TBmBJ-only
    metallicity test in build_table.py l.133. Mark the row GAP or flag it.
- **E2. Radiopurity.**
  - (i) §0 row 5 says Ge has "none". The IAEA extract marks ⁷⁶Ge STABLE, while the CSV row 100 [FT 1901.07569] lists ⁷⁶Ge as a natural radioactive
    isotope (2νββ). Using the measured T½ ≈ 1.9×10²¹ y [UNVERIFIED] gives ≈ 7.5×10⁻⁶ Bq/kg. It is negligible, but "none" is false. ¹⁰⁰Mo, ⁴⁸Ca and
    ⁸²Se are included, so the treatment is inconsistent.
  - (ii) The TeO₂, PbTe, PbS, PbSe, ZrTe₅, ZnO, ZnS and Cr₂O₃ values are dominated by GT/GE lower-limit half-lives of decays never observed:
    ¹²³Te > 9.2×10¹⁶ y, ²⁰⁴Pb > 1.4×10¹⁷ y, ⁷⁰Zn > 3.8×10¹⁸ y, ⁵⁰Cr > 1.3×10¹⁸ y.
    - The CSV note says "upper bound", but §0 row 5 and the §4.1 a_rad column print them as activities ("Pb/Te/… salts 10⁻⁵–10⁻² Bq/kg").
    - TeO₂ from ¹³⁰Te + ¹²⁸Te alone is 3.6×10⁻⁵ Bq/kg, 220× below the printed 8.1×10⁻³.
    - PbS/PbSe have no observed primordial decay at all. Print these as "< x".
  - (iii) KTaO₃ 4.63×10³ and InSb 121 Bq/kg are right (recomputed above).
- **E3.** The SiC-6H E_d = "22 (C)" is in 2008.08560 Table I (6H column, HTML table row "Edefect"). It is missing from both the CSV and its GAP rows
  (CSV l.313–315 list GAP:Z*, F_eh, ph_lifetime only). This breaks the "explicit GAP for every item" rule. The 15R "17–30 (C)" is out of scope.
- **E4.** Tags:
  - GaAs S2 "commercial … [E]" and the SiC/GaN/… S1 "PASS [E]" use a step tag (CONVENTIONS §12: [E] = ESTIMATED) as a literature-evidence tag.
    Use [UNVERIFIED] or give a source.
  - Al₂O₃ S1 "[ABS INSPIRE 'Limits on WIMP DM using sapphire cryogenic detectors']" has no identifier.
  - Otherwise, U0 reproduced: 1980 rows, no untagged value. Tags: DB 866, E 347, FT 312, GAP 220.

## F. Rubric (f): sample trace, FLAGs, screening
- **F1. Sample.**
  - Method: Python `random.seed(20261101)`; `random.sample` of 34 from the 1525 FT/DB/E value rows.
  - CSV line numbers: 9, 20, 60, 100, 123, 142, 212, 245, 257, 279, 298, 329, 340, 445, 452, 537, 617, 688, 829, 830, 911, 1004, 1026, 1167, 1271,
    1278, 1296, 1454, 1639, 1649, 1719, 1832, 1860, 1960.
  - Traced:
    - 9 DB/JARVIS rows: field-by-field against jarvis_extract.json;
    - 8 NIST/IAEA rows: abundances and J^π (Si, Cl, N, P, As, Te Z, C mass);
    - 10 FT rows: against the full texts (1910.10716 Tables I/III, 2008.08560 Table I, 1901.07569 Table I);
    - 7 E rows: recomputed (ρ, c_L, c_T, θ_D, 𝓃_e, ω_p, ⟨ε_M⟩ He).
  - **0 mismatches.**
  - Limit: DB rows were traced CSV → cached extract. Extract → live database was checked only for MP mp-5229 (lattice 3.91270131 Å, live OPTIMADE
    2026-11-01, identical). The JARVIS figshare dump was not re-downloaded.
- **F2. The 16 FLAGs.** Each reproduces its printed number.
  - 1 (3C θ_D) stands, with the "identical" correction (§C3).
  - 2–4 (MP/JARVIS ρ, h-BN −15 %, NiPS₃ −6 %, He +8 %) stand. They are vdW-functional effects, not findings.
  - 5–8 (n_e/ω_p) are CONFIRMED (§C1).
  - 9–13 (c_LA) are transcription CONFIRMED and error UNRESOLVED; the §0 magnitude needs correction (§C2).
  - 14–15 (ω_T, Ge E_g) are confirmed disagreements.
  - 16 (c_s naming) stands. It is a real trap: Si c_avg 5.88 vs c_LA 8.51 km/s.
- **F3. Screening.**
  - Survivors:
    - Si, Ge, TeO₂, CaWO₄, Li₂MoO₄, γ-LiAlO₂, LiF and NaF are evidenced at the [ABS] level, with IDs verified.
    - Al₂O₃ stands on 2203.15903/1704.04320 despite the ID-less INSPIRE item.
    - **GaAs S2** = PASS on "[E]" alone. By the return's own handling (diamond COND at 0.175 g; 3C-SiC COND), this is COND unless a ≥ 1 g
      detector-grade crystal is cited (2507.07119's mass was not read). Either cite it or move GaAs to SURVIVOR-COND (9 survivors).
  - Inconsistent FAIL/COND:
    - NiPS₃ S2 FAIL "[E] flakes" and h-BN/c-BN S2 FAIL "[UNVERIFIED]" vs ZrTe₅ S2 COND "[E] mm-scale, ≥ 1 g not shown" (same evidence class);
    - PE S3 FAIL "TES on H-rich crystals proposed only" vs 4H/6H-SiC S3 COND "QET designs … no demonstration read" (also proposal only);
    - α-SiO₂ S1 COND for "no mK detector found", while GaN/AlN/ZnO/InSb/GaSb/MgO/CaF₂/MgF₂/SiC get S1 PASS [E] with no mK detector either.
  - Fix: state one rule. Either a proposal-only or unshown-mass item is COND everywhere (then NiPS₃, h-BN and PE become SURVIVOR-COND), or it is
    FAIL everywhere (then ZrTe₅ is excluded).
  - Exclusion families (§3) are acceptable as [ABS]/[UNVERIFIED]-level screening. The perovskite S1 reason is [UNVERIFIED] only.

## G. Owed corrections (minimal list)
1. §0 row 6 and FLAG text: c_LA exceeds c_L^{Voigt} by 59–178 %. Drop "anisotropy". Write "near-identical moduli" for 3C θ_D.
2. Close IF-U5: Δ_D = 11.75 meV is the half-gap (1910.02091 Eq. (1.1), l.701–703).
3. Rewrite IF-U1 from the extract (PbS passes; 11 omitted materials fail). Apply or justify the <20 cm⁻¹ rule for ε₀. Add SrTiO₃ to IF-U4.
   Flag InSb ε₀ < ε_∞. Use the I4/mcm entry for SrTiO₃ or declare the exception.
4. Radiopurity: add ⁷⁶Ge. Print lower-limit-driven activities as upper bounds in §0 and §4.1.
5. LU1 source → WP2-v3 (4.3)/LST. LU2 → ω_p^{val}, ESTIMATED. LU3 source unverified → read Tamura or downgrade it. U7 "states" → "consistent with".
6. YIG 𝓃_spin = S_cell/Ω (net spin density), not a spin number density.
7. Si/Ge/C ε_∞ = ε₀ (FT). τ_ph → τ_life. `screen_C*` → `screen_S*`. Unify ρ provenance ranking. 3C ε_eh is estimated, not measured.
8. Add SiC-6H E_d "22 (C)" [FT 2008.08560 Table I]. Replace [E] evidence tags in screening with [UNVERIFIED] or a source.
9. GaAs S2: cite ≥ 1 g evidence or move it to SURVIVOR-COND. Unify the FAIL/COND rule (NiPS₃/h-BN/PE vs ZrTe₅/SiC/α-SiO₂).
10. IF-U9: limit the n_e claim to "column = 2 e/atom; C ω_p suspect". IF-U6: note that 0.3 meV is ≈ 1.7× the bulk Al gap [UNVERIFIED].
