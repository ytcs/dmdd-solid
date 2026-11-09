# R14 referee REF-WP8-U-B (hostile, isolated): returns/R13/WP8-U.md + WP8-U-table.csv + code/WP8-U/

Read: the return, its CSV and code/WP8-U/ (all six .py files plus data/*.json); CONVENTIONS, NOTATION, CONTROLS, DONE, LIMITS, STATEMENT;
R8/WP0-v3 and R8/WP2-v3 (grep only), R8/WP5-v3, R13/WP5-v4 (cross-reference lines only). Nothing else. Full texts fetched with lit.py into
literature/papers-r14-REF-WP8-U-B/: 2008.08560, 1910.10716, 1901.07569, 2004.10709, 1905.13744, 1910.02091. PDFs, HTML and graph files
are deleted; the pdftotext extracts (`*.txt`) are kept because the locators below index them. checks.py rerun: **23 PASS, 0 FAIL, 16 FLAG,
0.11 s**, which reproduces §6 exactly. No simulations were run; the numpy/arithmetic checks took < 1 s.

## Verdict table
| # | Main claim | Verdict | Reason |
|---|---|---|---|
| V1 | Pool of 47 materials, screening S1–S3: 10 SURVIVOR, 30 COND, 3 REF, 4 EXCLUDED (§2) | STANDS WITH CORRECTION | 9 of 10 SURVIVORs carry tagged evidence. GaAs S2 PASS rests on "[E]" (an unsourced assertion, not an estimate): by the return's own YIG/ZrTe₅ standard it is COND. Two `[ABS INSPIRE '…']` items have no ID. The 2008.08560 "p.21" locators are p.20 (§F) |
| V2 | Exclusions (§3) | STANDS WITH CORRECTION | the reasons are correct in kind, but h-BN/c-BN and the halide perovskites are excluded on [UNVERIFIED] evidence only. Mark them provisional |
| V3 | Property table (1980 rows) is faithfully transcribed and tagged (§4) | STANDS WITH CORRECTION | 34 random rows: 0 value mismatches. But: SrTiO₃ ε₀ = 9.96 [DB] is unphysical and contradicts the return's own rules (§C1); the InSb DFPT ε rows contradict §1's stated metallic rule (§C2); the summary "c" column mixes c_LA with SiC c_s (§C3); 𝓃_spin is mislabelled (§C4) |
| V4 | Radiopurity screen (§4.3, U9) | STANDS WITH CORRECTION | KTaO₃ 4.63×10³ and InSb 121 Bq/kg are reproduced by hand. Ge "none" is wrong by the return's own CSV: row 73 says no primordial isotope [DB], row 100 says ⁷⁶Ge is radioactive [FT 1901.07569]. The cached IAEA extract lists ⁷⁶Ge as STABLE (§C5) |
| V5 | 2008.08560 Table I n_e column is defective (FLAG 1, IF-U9) | STANDS. Literature claim **CONFIRMED** | n_e = 2N exactly for C, Si and SiC. ħω_p(Si) = 16.6 and ħω_p(SiC) = 22.1 eV need 4 e/atom; ħω_p(C) = 22 eV is consistent with the printed n_e (2 e/atom) (§L1) |
| V6 | 1910.10716 Table I c_LA for GaN, AlN, ZnO, α-SiO₂ and NaCl is a "source defect" (FLAG 2, IF-U9) | STANDS WITH CORRECTION. Literature claim **UNRESOLVED** | the transcription is correct. The size of the disagreement is misstated: c_LA exceeds Voigt by 59–178 %, not "37–64 %". The only evidence is DFT Voigt moduli, so "source defect" (IF-U9) overclaims; "suspect" (FLAG 2) is the defensible word (§L2) |
| V7 | Other source disagreements (diamond ω_T, Ge E_g, 3C θ_D; FLAGs 3–4) | STANDS | all four quotes are verified in the full text. Add that the θ_D "≤ 10 %" agreement in §0 row 7 leaves out 3C (−17.5 %) |
| V8 | FLAG 5: "c_s" in 2008.08560 is the *average phonon speed* | FALLS for the SiC entries | 2008.08560 never defines c_s. For all three SiC polytypes it exceeds the Voigt c_L (12.6/13.73/13.3 vs 12.29/12.18/12.18 km/s), which an average over 2 TA + 1 LA cannot do (§C3). It holds for C and Si only, where the values are copied from 1901.07569, which does define it |
| V9 | Cross-route checks U1–U10 (§6) | STANDS WITH CORRECTION | U1 assigns the TO/LO components backwards relative to the return's own A₁/E₁ note; with the correct assignment the residual is ≤ 1.2 %, not ≤ 2.6 % (§C6). "LST exact to 3 %" is self-contradictory wording. U7's attribution to 1901.07569 overclaims. U6 is a transcription check (τ = ℓ/c_s is the paper's definition) |
| V10 | LU1 (LST) proposed LIMITS row | STANDS WITH CORRECTION | the chain is already L4 / WP2-v3 (4.3) [D], so the row is redundant. Its "source" is a data table, not the formula's origin (Lyddane–Sachs–Teller 1941, uncited). "CHECKED" is not a CONVENTIONS §12 status |
| V11 | LU2 (plasma frequency from the f-sum) | STANDS WITH CORRECTION | the f-sum gives the **all-electron** ω_p (WP0-v3 (4.6a); NOTATION ω_p). The ω_p^{val} row needs a partial (valence-only) sum rule, which is neither written nor exact. A single-datum (Si) "CHECKED" |
| V12 | LU3 (Tamura isotope scattering) | **FALLS** as a LIMITS row | its source is [UNVERIFIED], so it fails rubric (b) by construction. The [E] tool may stay; Ge A_iso inherits ≈ +37 % from the −10 % θ_D (§C7) |
| V13 | LU4 (elastic Debye θ_D) | STANDS WITH CORRECTION | Anderson (1963) is uncited, and the cited "sources" are data. The sign of the leading correction is missing: Voigt moduli are an upper bound, so θ_D^{Voigt} is biased high for anisotropic crystals (TeO₂, the hexagonal crystals) |
| V14 | Notation and tag consistency (§ Symbols, Tags) | STANDS WITH CORRECTION | the collisions θ_D/θ_k, c₁ (DM coupling), τ_ph (renamed t_ph; τ is the truncation index), g₂^iso/g₂(r) and ħω_p (all-electron) are unresolved. [DB] and "CHECKED" are not in CONVENTIONS §12; [E] is used for exact identities (ρ(a), Z*(Si) = 0, which is [D] per WP2-v3 (4.5)) |
| V15 | Checks reproduce: 23 PASS / 0 FAIL / 16 FLAG | STANDS | reproduced. Labels run U0–U12 but there is no U11 (the YIG line is unlabelled) |

---
## (c) Literature-is-wrong claims (full text)
**L1. 2008.08560 Table I n_e. CONFIRMED.**
- Source (Table I, p.5, txt l.315–318): N = 1.76, 0.5, 0.96 and n_e = 3.54, 1, 1.95 (10²³ cm⁻³) for C, Si and SiC; ħω_p = 22, 16.6, 22.1[33] eV.
- Check with ħω_p = 3.713×10⁻¹¹√(n/cm⁻³) eV: n_e = 1.0×10²³ → 11.7 eV (≠ 16.6), 2.0×10²³ (4 e/atom) → 16.6 eV; 1.95×10²³ → 16.4 eV (≠ 22.1), 3.84×10²³ → 23.0 eV;
  3.54×10²³ → 22.1 eV, so the diamond pair is self-consistent at 2 e/atom (4 e/atom would give 31.2 eV).
- The return's statement is accurate. Its summary wording "the n_e column is internally inconsistent with the ω_p column" holds for Si and SiC only; for C both columns are at 2 e/atom.

**L2. 1910.10716 Table I c_LA. UNRESOLVED.**
- Source (p.2, l.73–101; App. A3 p.13 l.936–939): c_LA is in units of 10⁻⁵ c, the DFT ω_LA/q averaged over a q ≈ 10 eV sphere. The values are GaN 4.17, AlN 5.70, SiO₂ 5.76, ZnO 4.18 and NaCl 1.19. They convert to 12.50, 17.09, 17.27, 12.53 and 3.57 km/s, exactly as in the CSV.
- U8 prints c_L^{Voigt}/c_LA − 1 = −0.41, −0.37, −0.64, −0.53 and +0.36. So c_LA/c_L^{Voigt} − 1 = **+69 %, +59 %, +178 %, +113 %** for GaN, AlN, SiO₂ and ZnO, and −26 % for NaCl.
- §0 row 6 ("exceeds … by 37–64 %") and §4.1 ‡ ("36–64 %") are wrong. Write: "c_LA exceeds the Voigt c_L by 59–178 % (GaN, AlN, ZnO, α-SiO₂) and is 26 % below it for NaCl."
- The comparison is DFT (JARVIS OptB88) against DFT (VASP), with no measured c_L read in full text. A quartz c_LA close to diamond's 17.9 km/s is implausible [UNVERIFIED], but no measured elastic constant was read in full text, so this stays UNRESOLVED.
- IF-U9 must say "suspect, pending a measured c_L", not "source defect".

**L3. 1910.02091 Table 1 "∆" caption vs text. CONFIRMED.**
- Caption (l.694): "band gaps".
- Text (l.67): "2∆ is the band gap"; l.417: "∆ which is half the band gap"; l.730: "band gap of 10 meV (∆ = 5 meV)".
- ZrTe₅ Exp. [52]: ∆ = 11.75 meV. v_F(exp) = (1.3×10⁻³, 6.5×10⁻⁴, 1.6×10⁻³) c and NR = (1.1×10⁻³, 4.5×10⁻⁴, 1.0×10⁻³) c, as transcribed.
- IF-U5 stands.

**L4. 1905.13744 YIG used a DFT cell (IF-U7). UNRESOLVED.**
- The text (l.261) gives only "a ≃ 12.56 Å", uncited. Inferring "therefore DFT-relaxed" from the coincidence with MP's 12.560 Å is not evidence of provenance.
- Correct IF-U7 to "a matches the MP GGA+U cell; provenance unstated".
- See §C4 for the 𝓃_spin label.

**L5. JARVIS statements** (data/jarvis_extract.json): "ehull 2.93 eV/atom for every SiC polytype" confirmed (2.928, 2.9277, 2.9276; SrTiO₃ 1.55 and KTaO₃ 2.19 show ehull is unusable generally). "GaAs ε₀ = 3098" is misnamed: 3097.9 is `dfpt_piezo_max_dielectric_electronic` (ε_∞); ε₀ is `na`.

---
## Corrections (material values, rules and checks)
**C1. SrTiO₃ ε₀ = 9.96 [DB] (summary table; CSV `eps_0_DFT`).**
- JVASP-8082 has `max_ir_mode` = 0.62 cm⁻¹, the "failed IR run" of §1. build_table.py l.140 gates only ε₀ < 1000 and the metallic flag, never the IR flag, so ε₀ survives a failed run.
- ε₀ − ε_∞ = 3.6 is far below the quantum-paraelectric value [UNVERIFIED magnitude, ≳10⁴ at low T].
- §2 itself states the cubic → tetragonal transition at ≈ 105 K and names the I4/mcm entry JVASP-269. Using Pm-3m (JVASP-8082) violates the §1 polymorph rule (experimental low-T space group).
- Required changes:
  - SrTiO₃ ε₀ → GAP, and add SrTiO₃ to IF-U4;
  - apply the IR flag to ε₀ as well;
  - list the other failed-IR runs that keep ε₀: NaI 0.28, NaCl 0.34, LiF 0.86, γ-LiAlO₂ 1.38, KTaO₃ 2.19, Bi₂Se₃ 3.25 and 3C-SiC 3.39 cm⁻¹.

**C2. InSb ε rule.**
- §1 says "DFPT ε are dropped when OptB88vdW is metallic". build_table.py l.133 drops them only if OptB88 < 0.05 **and** TBmBJ ≤ 0.05 eV.
- InSb (OptB88 0.0, TBmBJ 0.134) therefore keeps ε₀ = 22.9 and ε_∞ = 20.4 from a metallic-ground-state DFPT run, and U1b uses them.
- IF-U1 describes the code rule; §1 must be corrected to match it, or the rows dropped.

**C3. Speed column.**
- §4.1 "c" gives Si/Ge/C c_LA (1910.10716) next to SiC c_s (2008.08560) and Voigt c_L for the DB-only materials. This is the mixing that FLAG 5 forbids.
- The SiC c_s values exceed even the Voigt c_L (above). The CSV note "'cs' average phonon speed (measured)" on SiC rows 212, 261 and 310 is unsupported: 2008.08560 calls it only "cs (m/s)" / "sound speed" (p.4 l.305).
- U2 shows the 4H/6H moduli within 3 %, so this conclusion is robust. Relabel the SiC rows as `c_s (2008.08560, undefined)` and put c_L_iso in the summary column.

**C4. 𝓃_spin label.**
- 1905.13744 l.259–261: "S_cell = (12 − 8) × 5/2 = 10 per … Ω = a³/2, i.e. n_s = 20/a³".
- 20/a³ = S_cell/Ω is a net spin density (units of ħ per volume). It is not the "ordered-spin number density": the Fe density is 40/a³.
- Rename it to 𝓈_spin, or define 𝓃_spin as S_cell/Ω explicitly.

**C5. Ge radioactivity.**
- The IAEA extract row (Ge, 76) has `half_life: STABLE`, so the code reports "none". CSV row 100 [FT 1901.07569 Table I] lists ⁷⁶Ge as a natural radioactive isotope.
- The summary "—" for Ge and the §4.3 list "Si, Ge, … none" must become "⁷⁶Ge (2νββ)". The activity is GAP, or [E] from a cited half-life (≈ 10⁻⁵ Bq/kg [UNVERIFIED]).
- U9 is not independent of this extract, so it cannot catch the omission.

**C6. U1 component assignment.**
- §4.1 states the pairs are (A₁, E₁). In C₆ᵥ, A₁ ∥ c and E₁ ⊥ c [D, group theory], yet checks.py pairs the first component with ε⊥.
- Correct assignment, (ω_L/ω_T)² vs ε₀/ε_∞: 4H ∥ 1.5177/1.5176 (0.01 %), ⊥ 1.4752/1.4788 (0.2 %); 6H ∥ 1.5011/1.4970 (0.3 %), ⊥ 1.4826/1.4652 (1.2 %); 3C 0.07 %.
- Either the A₁/E₁ note or the checks.py label is wrong. The LU1 "SiC 3 %" becomes ≤ 1.2 %.

**C7. A_iso(Ge).**
- Hypothesis: the −10 % θ_D_E deficit (U2) is in v_m and n_at^{1/3}. Since θ_D ∝ v_m n^{1/3} and A_iso = V_a g₂/(4πv_m³) ∝ v_m⁻³, the [E] A_iso(Ge) = 3.23×10⁻⁴⁴ s³ is high by up to (1/0.90)³ − 1 ≈ 37 %.
- The DFT density (ρ_JARVIS/ρ_exp = 5.054/5.33 = 0.948) absorbs part of this.
- I reproduced Si A_iso = 1.646×10⁻⁴⁵ s³ only with V_a from ρ_JARVIS (with V_a from a_exp it is 1.59×10⁻⁴⁵). Neither the locator nor the note says this.
- U7 says 1901.07569 pp.4–5 "states" the ordering Ge > Si > C. The text (l.311–321) says only that Ge is isotope-limited and that diamond has fewer stable isotopes "as compared to Si and Ge". No Ge > Si ordering is stated.

**C8. Ge E_g = 0.54 eV (1901.07569 Table I l.79).** The disagreement is real. Add that 0.54 eV matches no tabulated Ge gap [UNVERIFIED], so the CSV must not offer it as an alternative.

**C9. Diamond ω_T.** Diamond is non-polar, so TO = LO at Γ, and both papers list ω_LO = 163 meV. A "ω_TO" of 141 or 148 meV is not a Γ-point value. FLAG 3 should tell consumers to use ω_max = 161–163 meV and no ω_T at all.

---
## (b) Proposed LIMITS rows
- **LU1.**
  - The chain "ε with one polar TO mode → LST" is WP2-v3 (4.3) [D], which already sits in LIMITS L4 (DERIVED, REFEREED).
  - The proper action is a ✔ data cross-check note on L4: 2008.08560 Table I + JARVIS, ≤ 1.2 % with the correct assignment (C6).
  - Validity: correct. Leading correction: correct, and IF-U4 (soft modes) is apt.
  - Missing: the original LST citation.
- **LU2.**
  - Chain: CONVENTIONS §6 / WP0-v3 (4.6a) fixes ∫ωL = (π/2)ω_p² with **all** electrons, cores included. Equating the EELS peak with ω_p^{val} needs:
    - (i) a valence/core spectral separation (partial f-sum, approximate);
    - (ii) a free-electron pole for the valence part.
    Neither is written. As stated, "ω_p² = 4πα𝓃_e^{val}/m_e" relabels the symbol.
  - The source quote is correct: 2004.10709 Table I, "~ω_pl 16.6 ± 0.1 eV, EELS [35]" (l.324), with footnote d: "not an exhaustive survey … some uncertainty in this value". One datum is a consistency check, not a validation.
  - Leading correction "interband shift": correct, but it must be stated as a shift of the peak position, not of ω_p.
- **LU3. FALLS.**
  - Its source is "Tamura PRB 27, 858 (1983) [UNVERIFIED]", and rubric (b) needs a full-text quote.
  - The formula and the validity/correction statements are standard in form but undemonstrated here. Status "ESTIMATED" is a step tag, not a LIMITS status.
  - Re-propose after a full-text read, quoting the source's ⟨v⁻³⟩ convention. The return's v_m⁻³ = (2c_T⁻³ + c_L⁻³)/3 must be shown to equal it.
- **LU4.**
  - Formula: Anderson's (uncited). The cited "sources" are measured θ_D tables, which test the formula.
  - "CHECKED (U2, ≤ 10 %)" leaves out 3C-SiC (−17.5 %).
  - Validity "isotropic, acoustic only" is correct.
  - Leading correction: add the sign. Voigt ≥ Hill ≥ Reuss, so θ_D^{Voigt} is an upper estimate. Using n_at for all atoms (including optical branches) is the Anderson convention; this should be said.

---
## (d) Consistency with WP0-v3, CONVENTIONS, NOTATION
- **ω_p.** NOTATION: "ω_p, ω_{p,e} | all-electron plasma frequency". The §4.1 column "ħω_p" holds valence values (Si 16.6, Ge 15.6). Rename the column ħω_p^{val} throughout, including LU2.
- **New symbols that collide.**
  - θ_D (the θ_k nuisance family, NOTATION l.236, 447, 639);
  - c₁ = "EFT spin coefficient" (c₁ is the DM coupling in CONVENTIONS §7/§9; σ̄_e ∝ |c₁|²);
  - τ_ph = "phonon lifetime" (NOTATION l.234 renamed W0 "τ_ph" → t_ph; τ is the CONVENTIONS §11 multi-index). Use t_life or τ_life as a source-only symbol;
  - g₂^iso (B2 g₂(r) is the pair distribution, NOTATION l.535);
  - Λ_UV (Λ is the final-state class; acceptable only with a source-only mark, as for Λ_D).
- **ω_max** has two definitions under one symbol: "top of the DFT optical range" (FT) and "max Γ mode" (DB). CONVENTIONS §6 already uses ω_max as the lattice maximum. Keep one definition and suffix the other.
- **Tags.** [DB] is not in CONVENTIONS §12. If the brief defines it, cite the brief rule; otherwise it is a §12 amendment owed to the coordinator. "CHECKED" and "ESTIMATED" as LIMITS statuses are not §12 claim statuses.
- **[E]** in §12 means "order-of-magnitude or model number". The return applies it to exact identities: ρ from a_exp, Z̄*(Si) = 0 (which is [D], WP2-v3 (4.5)) and the g₂ sums.
- **WP5 cross-reference.** WP5-v3 l.252 (ε_eh = 3.749 eV, F_eh = 0.119 at 123 K, 2004.11499) equals 2004.10709 Table I row [29] (l.301, 308), and [29] = Rodrigues et al. skipper-CCD (l.749). It is consistent.

---
## (e) Provenance tags
- The tag set is complete: U0 passes, and every sampled row has a tag, a source and a locator or ID.
- Defects:
  - (i) the `[ABS INSPIRE '<title>']` items (Al₂O₃ S1, GaAs S3) have no record ID, so U0b does not cover them;
  - (ii) GaAs S2, Al₂O₃ S2 ("kg-scale … commercial [E]") and NaCl S2 use [E] for factual assertions, which should be [UNVERIFIED];
  - (iii) the [E] `rho_T_from_a_exp` rows have an empty locator, and the a_exp source (1910.10716 Table III p.14, verified: ZnO 3.250/5.207 Å, l.989) is only in the a_exp row;
  - (iv) A_iso's V_a provenance (DFT density) is unstated (C7);
  - (v) the summary marks TeO₂ ρ 5.92ᵈ as a ρ_T value, but it is a DFT (OptB88) density. It should be flagged as a `*_DFT` proxy, as §1 requires.

---
## (f) CSV trace, FLAGs, screening
**Sample.**
- Python `random.seed(1414)`, `random.sample` of 34 rows from the 1525 rows tagged FT/DB/E. The screening, verdict, GAP and "-" rows are excluded and reviewed separately below.
- DB rows were traced to the return's cached `data/*.json` (JARVIS, NIST, IAEA), not to the live databases.
- FT rows were traced to my own pdftotext at page/table level. The return's "l.M" indexes its own extracts and was not checked.
- E rows were recomputed.

| CSV line | material / property | value | trace | result |
|---|---|---|---|---|
| 8, 1249, 1631 | A[Si], A[S], A[Nb] | 28.0855, 32.0648, 92.9064 | NIST json Σx m | ✓ |
| 510, 655, 1630 | Z[Ga], Z[O], Z[Nb] | 31, 8, 41 | NIST json | ✓ |
| 13, 1451 | db_ids Si, SrTiO₃ | JVASP-1002/mp-149; JVASP-8082/mp-5229 Pm-3m | jarvis json | ✓ (SrTiO₃ polymorph: C1) |
| 24, 83, 197 | c_L_iso Si, c_T_iso Ge, c_L_iso 3C | 8.734, 2.949, 12.29 | √((B+4G/3)/ρ), √(G/ρ) from JVASP-1002/890/8158 | ✓ |
| 150 | C c_avg | 13.36 | 2008.08560 Table I p.5 "13360" | ✓ |
| 225, 976, 1749, 1788 | isotopes Si, Na, Mn, Cr | x and J^π | NIST + IAEA json | ✓ |
| 765, 899 | nuclear_spin Te, O | ¹²³Te, ¹²⁵Te 1/2⁺; ¹⁷O 5/2⁺ | IAEA json | ✓ |
| 287, 942 | TBmBJ 6H, LiF | 3.077, 11.219 | JVASP-182 (nat 12 = 6H), JVASP-1130 | ✓ |
| 334 | GaAs OptB88 gap | 0.085 | JVASP-1174 | ✓ |
| 311 | 6H n_e_val | 3.8449×10²³ | 3.2·N_A·8/40.096 | ✓ |
| 484, 576 | G_V InSb, Al₂O₃ | 19.76, 156.49 | JVASP-17580, -32 | ✓ |
| 488 | InSb ω_L_LST | 21.04 meV | 160.09 cm⁻¹ × √(22.918/20.391) | ✓ arithmetic; input violates the §1 rule (C2) |
| 997 | NaF ω_L_LST | 50.97 meV | 255.53 cm⁻¹ × √(4.7895/1.8506) | ✓ |
| 702 | ZnO ρ(a_exp) | 5.6741 | 1910.10716 Table III a, c = 3.250, 5.207 | ✓ (empty locator, e-iii) |
| 952, 955 | LiF E_g, ε_∞ | 14.2, 2.02 | 1910.10716 Table I l.96 | ✓ |
| 1222 | MgF₂ c_LA | 7.285 | 2.43×10⁻⁵ c | ✓ |
| 1165 | CaF₂ ε_∞ DFT | 2.259 | JVASP-20800 | ✓ |
| 1252, 1795 | g₂ S, O | 1.651×10⁻⁴, 3.359×10⁻⁵ | Σx(1 − m/m̄)² | ✓ |
| 1537 | ZrTe₅ ρ DFT | 5.859 | JVASP-86924 | ✓ |

**Totals.** 34/34 values match, 0 mismatches; two traced rows carry rule defects (488, 1451).

**Targeted FT checks outside the sample** (all match): SiC ε, ω, E_g, ε_eh, θ_D (2008.08560 Table I); §4.1 c_LA conversions (Si 8.51, Ge 4.83, C 17.93, GaAs 4.71, CaWO₄ 4.26, CsI 1.38, Al₂O₃ 10.52); 1901.07569 Table I (ℓ, τ_life, ε_eh(Ge) = 3.0) and p.9 ¹⁴C ("about 10 events per kg-year"); 1910.02091 Table 1; 1905.13744 p.4.

**FLAG review (16).**
| FLAG | Verdict |
|---|---|
| 3C θ_D (1) | verified (1430 vs 1200 K; ħω_D 122 vs 103 meV, internally consistent). "Same moduli" overstated: G(3C) 197.6 vs 190.7 GPa. Cause UNRESOLVED |
| MP/JARVIS ρ: NiPS₃, h-BN, solid He (3) | reproduced; acceptable as flags. Solid He has no meaningful OptB88 density at all |
| 2008.08560 n_e/ω_p (4) | CONFIRMED (L1) |
| 1910.10716 c_LA (5) | UNRESOLVED; magnitudes misquoted (L2) |
| Diamond ω_T (1) | verified (148 at 2008.08560 l.333; 141 at 1901.07569 l.84); add C9 |
| Ge E_g (1) | verified (0.54 at l.79; 0.67 at 1910.10716 l.75); add C8 |
| c_s naming (1) | FALLS for SiC (V8, C3) |

**Two named disagreements:** 2008.08560 n_e CONFIRMED; 1910.10716 c_LA UNRESOLVED.

**Screening of the 10 SURVIVORs.**
- Si, Ge, Al₂O₃, TeO₂, CaWO₄, Li₂MoO₄, γ-LiAlO₂, LiF and NaF have ID'd [ABS] evidence on all three criteria. The titles in data/arxiv_verified.json match the claims: astro-ph/0204411 "LiF bolometer at Kamioka", astro-ph/0306365 "NaF Bolometer", 2207.07640 "lithium aluminate targets in CRESST-III", 2203.15903 "Large-mass, low-threshold sapphire detector".
- The ≥ 1 g mass is not visible in the titles for LiF, NaF and Al₂O₃ (ν-cleus is "gram-scale"), so those S2 PASSes are [ABS]-plausible, not demonstrated.
- **GaAs:** S1 and S3 are supported (1802.09171 "Cryogenic Scintillation Properties of n-Type GaAs…", 2507.07119 "First measurement of GaAs as a scintillating calorimeter"). S2 is "[E]". Downgrade it to COND, or give the crystal mass from the full text.
- 2008.08560 locators: the "fabrication scale", "fairly straightforward" and "large boules … commercially viable" quotes are verified at l.1667–1686, which is p.20, not p.21. "6H … most widely available" is p.2 ✓, and Table IV is p.23 ✓.

**Exclusions.**
- NiPS₃ (S2 [E]), polyethylene (S3 [FT 2201.04219], not re-read) and solid He (S1 [ABS]): acceptable.
- h-BN/c-BN and the halide perovskites: exclusion on [UNVERIFIED] only. Mark them provisional.
- SrTiO₃ is kept as COND on S1. Consistent.

## Required changes (summary)
1. §0 row 6, §4.1 ‡ and IF-U9: rewrite the c_LA magnitudes as 59–178 % / −26 %, and the status as "suspect", not "source defect" (L2).
2. SrTiO₃ ε₀ → GAP, plus IF-U4. Apply the IR-failure gate to ε₀ and list the seven other failed-IR ε₀ rows. Use the low-T polymorph or flag the choice (C1).
3. Make the §1 metallic rule match the code, or drop InSb ε (C2).
4. Relabel the SiC c_s rows and fix the summary speed column (C3, V8).
5. Ge ⁷⁶Ge into §4.3, the summary and CSV row 73 (C5).
6. Swap the U1 component assignment or the A₁/E₁ note; LU1 becomes ≤ 1.2 % (C6).
7. Withdraw LU3 until its source is read in full text. Merge LU1 into L4 as a ✔ note. Rewrite the LU2 chain via a partial sum rule with ω_p^{val}. Add Anderson and the Voigt sign to LU4.
8. Rename θ_D, c₁, τ_ph, g₂^iso and ħω_p (→ ħω_p^{val}); resolve the [DB] / "CHECKED" vocabulary with the coordinator.
9. Rename 𝓃_spin, or define it as S_cell/Ω (C4). Reword IF-U7 provenance (L4).
10. Downgrade GaAs S2 to COND, or source it. Give IDs for the INSPIRE items. Correct the p.21 → p.20 locators.
