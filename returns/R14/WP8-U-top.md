# R14 / WP8-U-TOP: top-up of the WP8-U property table

Agent WP8-U-TOP, brief briefs/R14/WP8-U-TOP.md, plus the coordinator addition S4 (intrinsic radioactivity; reversible default,
not yet confirmed by the user). Theory and data compilation only: no DFT, DFPT, MD or Monte Carlo was run. The closed forms are
the Christoffel eigenproblem, the Voigt–Reuss–Hill moduli, the diatomic rigid-ion relation, β shapes and the Klein–Nishina limit,
all in numpy. The R13 files (returns/R13/WP8-U.md, WP8-U-table.csv) are read only and were not edited. CONVENTIONS (incl. R13
amendments) and NOTATION v4 (incl. "Rows added WP7-E") were read. WP8-F.md §5 was read for the property list. No other return is
quoted for a material value.

**Deliverables.**
- returns/R14/WP8-U-table-v2.csv. It has 2997 data rows: the 1980 R13 rows (verbatim except §6) plus 1017 new rows, with the same
  11 columns. New-material rows: CdTe, CZT, HgI₂, TlBr (detector references, `NOT-SCREENED`), Ir (sensor film), `ALL` (laws and
  definitions).
- code/WP8-U-TOP/:
  - `fetch_db.py`: the network step, run once. It writes the JARVIS extract and the arXiv verification;
  - `lit_values.py`: every full-text value with its locator;
  - `build_v2.py`: builds the CSV offline;
  - `checks.py`: 20 checks T0–T15, **20 PASS, 0 FAIL**, ≈ 1 s;
  - `data/`: jarvis_top.json, arxiv_verified.json, s4.json, s4_fractions.json, christoffel.json, zstar_validation.json.
- Literature: literature/papers-WP8-U-TOP/ holds the pdftotext extracts and the Europe PMC JATS XML of the non-arXiv full texts. The
  PDFs and HTML are deleted. All 21 arXiv IDs cited were verified against the arXiv API (T1).

**Tags** (as R13).
- [FT]: full text, with the page or table in `locator`. arXiv pages are PDF pages. Non-arXiv full texts were read as Europe PMC
  XML:
  - DS09 = Del Sordo et al., Sensors 9, 3491 (2009), PMC3297127;
  - WBG24 = Materials 17, 1147 (2024), PMC10934017;
  - GAN20 = Micromachines 11, 519 (2020), PMC7281217;
  - CZT23 = Sensors 23, 2167 (2023), PMC9960822;
  - SEL26 = J. Synchrotron Rad. (2026), PMC12809242;
  - BV25 = Nanomaterials 15, 635 (2025), PMC12073746.
- [DB]: JARVIS-DFT dft_3d 9-24-2025 `JVASP-n`, the same dump WP8-U used; also NIST and IAEA, as in R13.
- [E]: a closed form; the formula is in `locator`.
- GAP: a row `GAP:<item>` with the reason.
- Supersession: a new row whose value replaces an R13 value has a `note` that begins "supersedes R13 <property>=<value>".

---
## 0. Results at a glance
| # | Item | Result |
|---|---|---|
| 1 | §5.2 coverage | 40 screened materials × 27 WP8-F items: every cell is now a value or an explicit GAP with a reason (T13). New values: directional c_LA/c_TA and Y_mod for 33 materials [E from DB C_ij]; Z/A for all; Z*_LST for SiC; GaAs ε₀, ω_T, ω_L; sapphire mode tables; E_d for 5 materials; ρ and 𝓃_e for Li₂MoO₄; magnon gaps for 4 magnets |
| 2 | ε_eh, F_eh | Measured ε_eh, method and T, now for Si, Ge (77 K and 50 mK), diamond (4 measurements), 3C-, 4H- and 6H-SiC, GaAs, GaN, a-SiO₂, CdTe, CZT, HgI₂ and TlBr. F_eh for Si, Ge (77 K), 4H-SiC (0.100, ≤ 0.04 in tension) and CZT (0.1). **AlN has no measurement**: 12.2 eV is a calculation and 14.4 eV an empirical law. Al₂O₃, LiF, MgO, NaF, the alkali halides and scintillators: no measurement; an empirical [E] bracket is given, and it contains 12 of 13 measured values (HgI₂ is the exception, T7) |
| 3 | 2008.08560 n_e | The column is **2 e/atom × N** for C, Si and SiC (ratios 2.01, 2.00, 2.03, T5a). Its diamond ħω_p = 22 eV is the plasma energy of that wrong n_e (22.09 eV, T5b). **Use 𝓃_e^{val} = 4 e/atom × N** (C 7.04, Si 2.00, SiC 3.84 ×10²³ cm⁻³) and ħω_p(diamond) = 31.2 eV [E]. The measured SiC 22.1 eV agrees with 4 e/atom to 4 % |
| 4 | 1910.10716 c_LA | Recomputed with the paper's own definition (the sphere mean of ω_LA/q) from DB elastic tensors: 13 of 22 agree within 10 % and 17 of 22 within 16 %. **GaN ×1.69, AlN ×1.60, ZnO ×2.12, α-quartz ×2.79 and NaCl ×0.73 are outside every propagation direction** (T3c). They are source defects; WP8-F should use `c_LA_recommended` |
| 5 | G-R5 | Al (JVASP-816) and Ir (JVASP-901) moduli [DB]: Al B_V 69.9, G_V 16.8 GPa; Ir B_V 348.1, G_V 217.0 GPa. Al (and Nb) DB C₄₄ look too soft (IF-T3). Kaplan 1979 is closed access and was not read |
| 6 | Magnets, oxides | Measured zone-centre magnon gaps: Cr₂O₃ 0.696 meV, MnO 0.82 THz (3.39 meV), NiO 1.15/1.29 THz (4.76/5.33 meV). YIG: acoustic branch gapless, optical gap ≈ 30 meV, ω_max^mag ≈ 90–100 meV, J₁…J₆ [FT]. **CaWO₄ and Li₂MoO₄ ε₀, ω_LO/TO, Z\* stay GAP**: no DB entry and no full text found |
| 7 | **S4 (new)** | Intrinsic sub-keV rate: **KTaO₃ 1.8×10⁵ /(kg·d·keV)** (⁴⁰K β 1.5×10⁵ + 1461 keV Compton 3.2×10⁴) and **InSb 4.8×10³–3.9×10⁴** (¹¹⁵In shape bracket). Both **FAIL → EXCLUDED-RADIO**. TeO₂, PbTe, ZrTe₅ and Cr₂O₃ are COND: ¹²³Te/⁵⁰Cr EC have only half-life lower limits. All others PASS (≤ 2×10⁻⁴). Cosmogenic ³H (reducible): Si 0.17 / Ge 0.10 / NaI 0.11 after 100 d at sea level, and 11 / 6.7 / 7.4 /(kg·d·keV) at saturation, which is above the budget |

---
## 1. Diff of WP8-F §5.2 against the R13 table
Coverage key: a value row exists (✓), partly (∂), or an explicit GAP row with reason. "40" = all SURVIVOR and SURVIVOR-COND
materials. The CSV names are listed; T13 checks that every material has at least one of them.
| WP8-F §5.2 property | R13 | v2 action (CSV name) | Status after v2 |
|---|---|---|---|
| ρ_T | ✓ (Li₂MoO₄ GAP) | Li₂MoO₄ `rho_T` 3.04 g/cm³ [FT 1704.01758 p.22] | ✓ 40 |
| E_g | ✓ | none | ✓ (magnets: DFT 0* only) |
| E_x^b, E_min(q) | absent | `GAP:E_x_b`, `GAP:E_min_q` | GAP 38. E_min(q) needs a band structure (tier H) |
| ε_∞, ε₀ (tensor) | scalars; GaAs ε₀ GAP | GaAs `eps_0` 12.9, `eps_inf` 10.89 [FT 1807.10291 Table I p.11]; sapphire `eps_0_par/perp` 11.5/9.3 | ∂: tensors only for SiC and sapphire [FT] and ZrTe₅ [FT]; CaWO₄ and Li₂MoO₄ ε₀ GAP |
| Z*_κ (tensor) | Z̄* for 21; SiC GAP | SiC `Zstar_LST` 2.68/2.67/2.63 e [E]; `GAP:Zstar_tensor` | ∂: scalar only |
| ω_TO,ν, ω_LO,ν | partly | GaAs `omega_T_LST` 32.07, `omega_L` 34.9 meV; sapphire `omega_TO_LO_o/e` (4 + 2 modes) [FT 1807.10291 Table II p.31] | ∂ |
| L(q,ω), ε₂(ω) | absent | `GAP:L_eps2_data` | GAP 40: needs `src=data` pointers (IF-T5) |
| c_LA, c_TA (directional) | c_LA, c_L^iso | `c_LA_Christoffel_avg`, `c_TA_Christoffel_avg`, `c_dir_100_001` [E from DB C_ij]; `c_LA_recommended` (§3.2) | ✓ 33; GAP 7 (MnO non-PD tensor; CaWO₄, Li₂MoO₄, CsI, ZrTe₅, YIG, Cr₂O₃ have no tensor) |
| D_κ(ω), ω̄_κ, ω_max^ph | ω_max | `omega_bar_Debye_E` = (3/4)k_Bθ_D [E, acoustic Debye only]; `GAP:phonon_DOS` | ∂: the partial DOS is GAP 40 |
| M_κ, A_κ, Z_κ | ✓ | none | ✓ |
| 𝓃_e, Z/A | 𝓃_e | `Z_over_A` [E] for all; Li₂MoO₄ `n_e_val` 3.37×10²³ cm⁻³; C/Si/SiC `n_e_val_recommended` (§3.1) | ✓ |
| v_F, k_TF, Δ_BCS | Al Δ_BCS, E_F [FT] | Al, Nb `v_F_free_E`, `E_F_free_E`, `k_TF_free_E` [E]; Nb `Delta_BCS_E` 1.63 meV (from the DFT T_c) | ∂ (free-electron) |
| ε_bg, v_F, g_deg, Δ_D (Dirac) | ZrTe₅ v_F, Δ_D, g | `GAP:eps_bg` (ZrTe₅, Bi₂Se₃) | ∂ |
| 𝓃_S, λ_S, \|𝐒\|, J^ex, Δ_mag, F^mag | YIG 𝓃_spin; AFM v_θ | magnon gaps and YIG J₁…J₆ (§5.1) | ∂: F^mag GAP; YIG a_exp GAP (IF-U7 open) |
| EPW g, ω_TA(Q*) | absent | `GAP:EPW_g_omegaTA_Qstar` | GAP 38 (tier H) |
| tanδ₀, ε_r, P̄_STM | absent | `GAP:tan_delta0_PSTM` | GAP 40 (depends on preparation) |
| E_d, E_st,1, p_surv (prov.) | E_d for C, Si, SiC | `E_d` Si 13, GaAs 10, SiC C 20 / Si 35, GaN Ga 45 / N 109, diamond 35 eV [FT GAN20 Table 1]; `GAP:E_st1_p_surv` | ∂ |
| ε_eh, F_eh, y_ion, QF (prov.) | Si, Ge, C, SiC | §2; `GAP:y_ion_QF` | ∂ (§2) |
| Y_mod, ∫Δα_th dT | absent | `Y_mod_Hill` [E from DB] for 33 + Ir; `GAP:alpha_th_integral` | ∂ |
| radioisotopes, cosmogenics | primordial a_rad | S4 rows (§6); ³H for Si, Ge, NaI [FT]; `GAP:S4_cosmo` for 37 | ∂ |
| qualifiers | S1–S3 | S4 added (§6) | ✓ |

**WP8-F §5.3 vetting rules.** No DFPT row is added here, so rule (ii) (IR > 50 cm⁻¹ and OptB88 gap > 0.3 eV) does not touch any v2
row. The R13 InSb and Pb-salt DFPT ε rows are still flagged by IF-U1. One new defect was found: the JARVIS MnO (JVASP-7870)
elastic tensor is not positive definite, so it is flagged and no speeds are derived from it (T15).

---
## 2. Pair-creation energy ε_eh and Fano factor F_eh
### 2.1 Measured values (all [FT]; T = room temperature unless stated)
| Material | ε_eh (eV) | T | Method | F_eh | Source / locator |
|---|---|---|---|---|---|
| Si | 3.62 | 25 °C | compilation; reference for the SiC comparison method | 0.119 at 123 K (R13, via WP5-v3) | DS09 Table 1; 2311.03902 Table 1 p.2 |
| Ge | 2.96; "∼3" | 77 K (the DS09 header reads 25 °C; Ge spectrometers run at 77 K, read [C]) | compilation | **0.13 at 77 K** ("F = 0.13 [17]", secondary, from Klein) | DS09 Table 1; 1602.08005 p.9 |
| Ge | **3.37 ± 0.01**; 3.32 (+0.84 −0.97) | 50 mK | fit of the EDELWEISS E_p/E_Q versus bias; CDMSlite resolution + Fano model | 0.14 (+0.02 −0.03), model-dependent | 1602.08005 p.12 §2.1.4; p.11 §2.1.3 |
| diamond | 13.1 ± 0.2; 13.25 ± 0.50; 13.05 ± 0.20; 12.82 ± 0.13 | RT | α; continuous X-ray (×2); transmission X-ray detector | GAP (Shimaoka 2016 seen as a title only) | 2311.05011 PDF p.30; GAN20 Table 1 ("13") |
| 3C-SiC | 6.90 | RT | electrons (Makarov 1975) | GAP | 2610.16949 Table II PDF p.23 |
| 4H-SiC | **7.83 ± 0.02**; 7.82 ± 0.02; earlier 7.28–8.6 and one outlier 5.05 | 25 °C; 23 °C | α against Si (3.62); α with charge injection | **0.100** (X-ray linewidth), **≤ 0.04** (X-ray upper limit), 0.128 (Klein model) | 2311.03902 Tables 1–2 p.2, p.4 |
| 4H-SiC | dε/dT: −0.27 eV over 23 → 500 °C (about twice the E_g shift) | 23–500 °C | α, Am-241 | – | 1308.2886 p.10 |
| 6H-SiC | 6.7 (R13) | RT | – | GAP | 2008.08560 Table I |
| GaAs | 4.2; 4.2; 4.3 | 25 °C | compilations | GAP | DS09, WBG24, GAN20 Table 1 |
| GaN | 8.9; 8.9 | RT | compilations (2610.16949 Fig. 6 cites Sellin & Vaitkus 2006) | GAP | WBG24, GAN20 Table 1 |
| a-SiO₂ | 18.0 (one sample 16.4) | RT | films, recombination-model fit (Ausman 1975) | GAP | 2610.16949 Table II, p.24 |
| CdTe / CZT | 4.43 / 4.6; 4.46 (+20 °C) | 25 °C | compilations | CZT **0.1** (Redus 1997, as cited); 0.089 (an assumed value) | DS09; CZT23 Table 1 caption; SEL26 fn. 5 |
| HgI₂ / TlBr | 4.2 / 6.5 | 25 °C | compilation | GAP | DS09 Table 1 |
| semiconductors (generic) | – | – | – | "0.06 – 0.14" | DS09 §2 |

**AlN has no measurement.** 2610.16949 Table II gives "Expt. –". Its 12.2 eV is a first-principles DFT+MC number (theory), and
BV25's 14.4 eV is "estimated based on the relation (2.15Eg+1.23)". Both are in the CSV under distinct names (`eps_eh_calc`,
`eps_eh_empirical`) and must not be used as a measurement.

### 2.2 Materials without a measurement: empirical bracket [E]
`eps_eh_bracket_E` = [1.54E_g + 1.89, (14/5)E_g + 0.5] eV. These are the two laws quoted in 2610.16949 PDF p.4: the recent
wide-gap fit and Klein 1968. Check T7: the bracket contains 12 of the 13 measured values in §2.1 (1 % tolerance, E_g at the
measurement temperature). The exception is HgI₂ (4.2 eV against 5.2–6.5).

Bracket values:
- AlN 11.4–17.9; Al₂O₃ 15.4–25.1; α-SiO₂ 16.1–26.3; ZnO 7.0–9.7; MgO 13.9–22.4; TeO₂ 9.0–13.5; CaWO₄ 9.9–15.1;
- LiF 23.8–40.3; NaF 19.6–32.7; NaCl 15.4–25.0; NaI 10.8–16.7; CsI 11.3–17.7; CaF₂ 20.1–33.6; MgF₂ 21.0–35.2;
- ZnS 7.7–11.1; SrTiO₃ 5.4–6.9; KTaO₃ 7.0–9.8; GaSb 2.5–3.0.

Caveats on the bracket:
- It is the spread between two empirical laws, not an error bar. It is narrow near E_g ≈ 1.1 eV, where the two lines cross.
- It is untested above E_g ≈ 9 eV and for ionic crystals (no alkali halide or fluoride is among the 13).
- Its width (factor ≈ 1.6 at wide gap) misses WP8-F's 2 % need by far. ε_eh outside the semiconductors of §2.1 stays an
  experimental priority.

**GAP (no usable gap for the bracket).** InSb and the Pb salts (E_g < 0.3 eV); ZrTe₅ and Bi₂Se₃ (Dirac); the magnets (only DFT
0* gaps); Li₂MoO₄ and γ-LiAlO₂ (only PBE/OptB88 gaps, which underestimate, IF-U2).

**Scintillators (CaWO₄, Li₂MoO₄, NaI, CsI).** Their charge is not read out, so ε_eh is not directly measured: the observable is the
light yield. The bracket row says so, and the light-yield-inferred energy per pair is not tabulated here (GAP).

**F_eh.** It is measured only for Si, Ge (77 K), 4H-SiC (with 0.100 and ≤ 0.04 in mutual tension) and CZT. Every other screened
material carries `GAP:F_eh_v2`, with the generic range 0.06–0.14 noted. All ε_eh/F_eh rows inherit WP8-F's **(prov.)** flag.

---
## 3. The two source disagreements
### 3.1 2008.08560 Table I n_e (C, Si, SiC)
- Table I p.5 lists N = 1.76, 0.5 and 0.96 ×10²³ cm⁻³ (the atom density) and n_e = 3.54, 1, 1.95. The ratios n_e/N are 2.01,
  2.00 and 2.03 (T5a), so **n_e counts 2 e/atom**. The paper's text gives no definition of n_e (full-text grep).
- Its ħω_p column mixes two conventions:
  - Si 16.6 eV = the free-electron value for 4 e/atom (16.61 eV, T5b), equal to EELS (R13 U5);
  - diamond 22 eV = the free-electron value of its own n_e = 3.54 (22.09 eV), i.e. of 2 e/atom;
  - SiC 22.1 eV is a measurement (its ref. [33]) and agrees with 4 e/atom (23.0 eV) to 4 %.
- **Decision for WP8-F.** Use `n_e_val_recommended` = 4 e/atom × N: C 7.04, Si 2.00, SiC 3.84 ×10²³ cm⁻³. For diamond, ħω_p =
  31.2 eV [E, free-electron 4 e/atom]; a measured EELS diamond value is GAP in the sources read. The n_e and diamond ħω_p
  entries of 2008.08560 must not enter the f-sum ceiling (L17) or any 𝓃_e-scaled FOM.
- *Why:* the f-sum counts all valence electrons (CONVENTIONS §6, §13 #12). Two independent measured plasmon energies (Si EELS
  16.6, SiC 22.1) require ≈ 4 e/atom, while the 2 e/atom column reproduces only the paper's own unmeasured diamond entry.

### 3.2 1910.10716 Table I c_LA
- Definition (1910.10716 p.13, App. A3): c_LA "was calculated by averaging ω_LA/q over a uniform 20 × 20 grid on the surface of a
  sphere in reciprocal space with radius q ≈ 10 eV", from phonopy frozen-phonon dispersions (App. A2).
- This return recomputes the same average from the Christoffel equation with the JARVIS elastic tensor [E from DB], on a
  2000-point sphere. Ratio = 1910.10716 / Christoffel:

| Material | ratio | Material | ratio | Material | ratio |
|---|---|---|---|---|---|
| C | 1.00 | Ge | 1.00 | Si | 0.97 |
| GaAs | 0.97 | InSb | 0.98 | GaSb | 0.98 |
| Al₂O₃ | 0.98 | MgO | 0.96 | MgF₂ | 0.96 |
| CaF₂ | 0.94 | NaI | 0.91 | PbTe/PbSe/PbS | 1.05/1.08/1.10 |
| LiF | 0.87 | NaF | 0.88 | ZnS | 0.84 |
| **GaN** | **1.69** | **AlN** | **1.60** | **ZnO** | **2.12** |
| **α-SiO₂** | **2.79** | **NaCl** | **0.73** | | |

- **Reading.**
  - The method reproduces the paper to ≤ 4 % for C, Si, Ge, GaAs, InSb, GaSb, Al₂O₃, MgO and MgF₂, so the definition and the DB
    route agree.
  - For GaN, AlN, ZnO and α-quartz the quoted value exceeds the *largest* directional c_L by > 30 % (T3c). No orientation, and
    hence no averaging convention, recovers it. NaCl lies below the smallest directional c_L.
  - These five are source defects. A probable cause is a branch mis-assignment or non-analytic-correction artefact in the
    frozen-phonon interpolation of polar non-cubic cells [C]. It is not established.
  - LiF, NaF and ZnS (12–16 %) are within the DFT functional spread.
- **Decision for WP8-F.**
  - Use `c_LA_recommended` (the Christoffel average) for GaN 7.38, AlN 10.71, ZnO 5.91, α-SiO₂ 6.19 and NaCl 4.86 km/s. These
    supersede the R13 c_LA rows.
  - Keep 1910.10716 where `c_LA_check_1910` is within 20 %.
  - The needed accuracy is 20 % for the rate and 5 % for the edge (WP8-F §5.2). The edge therefore needs measured C_ij,
    preferably at low temperature: the DB tensors are 0 K OptB88vdW numbers.
  - The R13 `c_L_iso` (Voigt) rows agree with the Christoffel averages to a few % (the WP8-U FLAG 2 direction is confirmed).

---
## 4. WP8-R G-R5: Al and Ir elastic moduli; Kaplan 1979
| Metal | DB entry | C₁₁, C₁₂, C₄₄ (GPa) | B_V, G_V (GPa) | Y_mod,Hill (GPa) | c_LA, c_TA sphere mean (km/s) | ρ (g/cm³) |
|---|---|---|---|---|---|---|
| Al | JVASP-816 | 93.4, 58.2, 16.2 | 69.93, 16.76 | 46.5 | 5.89; 2.48/2.53 | 2.663 |
| Ir | JVASP-901 | 577.7, 233.3, 246.8 | 348.1, 216.96 | 532.1 | 5.42; 3.00/3.28 | 21.798 |

- Provenance: [DB] for the tensor and the moduli; [E] for Y and the speeds. This replaces WP8-R's [UNVERIFIED] tag with a database
  value.
- Measured moduli are GAP in the full texts read. A memory comparison, for plausibility only [UNVERIFIED], suggests Al
  Y ≈ 70 GPa and C₄₄ ≈ 28 GPa. That would put the DB Al shear stiffness ≈ 40 % low; the same pattern holds for Nb (C₄₄ = 6.6 GPa
  in JVASP-934). Ir looks plausible.
- **Recommendation for WP8-R:** do not use the DB Al/Nb shear moduli in AMM transmission at better than ±40 % until a measured
  tensor is tabulated (IF-T3).
- Kaplan, JLTP 37, 343 (1979), doi:10.1007/BF00119193: Unpaywall reports it as closed access. **Not accessed**; G-R5 stays open for
  the tabulated transmissions.

---
## 5. Thin entries
### 5.1 Magnets [FT]
| Material | Zone-centre gap Δ_mag | ω_max^mag | Other | Source |
|---|---|---|---|---|
| YIG | acoustic ("ferromagnetic") branch gapless at B₀ = 0 (Kittel, tunable by B₀); first optical gap ≈ 30 meV | ≈ 90 meV predicted, modes seen up to nearly 100 meV | J₁ 6.8(2), J₂ 0.52(4), J₃a 0.0(1), J₃b 1.1(3), J₄ −0.07(2), J₅ 0.47(8), J₆ −0.09(5) meV | 1705.06594 pp.2–3 |
| NiO | 1.15 THz (mode B) and 1.29 THz (mode A) = 4.76 and 5.33 meV; further modes < 0.5 THz | GAP | – | 1806.07968 pp.3–4 |
| MnO | 0.82 THz = 3.39 meV (high branch); low branch in the microwave range | GAP | – | 2609.20122 p.1 |
| Cr₂O₃ | 0.696 meV | GAP | – | 2010.08926 p.2 |

- These close R13 "magnon gaps GAP". F^mag(q) stays GAP.
- The YIG experimental lattice constant remains GAP: 1705.06594 does not state it. IF-U7 (𝓃_S ∝ a⁻³) therefore stays open.
- A spin-wave edge for YIG must use the gapless branch, with the WP8-F §2.6(b) acoustic-magnon analogue.

### 5.2 Many-atom oxides and polar inputs
- **CaWO₄.**
  - JARVIS JVASP-88542 has no DFPT, IR or elastic fields ('na').
  - No full-text infrared or dielectric study was found on arXiv or in Europe PMC.
  - ε₀, ω_LO/TO and the Z* tensor are `GAP:eps0_omegaLO_TO`. The R13 [FT] ε_∞ 3.84 and Z̄* 2.84 (Ca) / 4.67 (W) are DFT numbers
    from 1910.10716.
- **Li₂MoO₄.**
  - It is absent from JARVIS.
  - ρ_T = 3.04 g/cm³ [FT 1704.01758 p.22]. 𝓃_e^{val} = 3.37×10²³ cm⁻³ and ħω_p^{val} = 21.6 eV [E, 32 e/f.u.].
  - ε, phonons, elastic constants and ε_eh are GAP. Sources not found: ρ, ε and phonons are not on arXiv and not in Europe PMC
    full text.
- **SiC Born charge (fills R13 GAP:Z\*).**
  - Z*_LST = 2.68 (3C), 2.67 (4H ⊥), 2.63 (6H ⊥) e [E].
  - Formula: diatomic rigid-ion relation ε₀ − ε_∞ = Z*²e²/(ε₀^{SI}Ω μ ω_T²), with the 2008.08560 Table I ε₀, ε_∞, ω_TO and ρ = 3.21.
  - The same formula with 1910.10716's own ε_∞ and ω_O range reproduces its Z̄* for 13 cubic diatomics: median 1.6 %, maximum
    12 % (CsI) (T6).
- **GaAs.**
  - ε₀ 12.9 and ε_∞ 10.89 [FT 1807.10291 Table I p.11] fill R13 GAP:eps_0.
  - ω_L = 34.9 meV (1910.10716, DFT) and ω_T,LST = 32.07 meV [E]. ω_T,LST agrees with 1910.10716's ω_O min of 31.8 meV to 1 % (T12).
- **Sapphire.** TO/LO modes, ordinary 4 and extraordinary 2, [FT 1807.10291 Table II p.31] give per-branch inputs for WP8-F (2.5a).

### 5.3 Other fills
- E_d (GAN20 Table 1) is per sublattice where given; the R13 diamond 38–48 eV [2008.08560] and the 35 eV compilation coexist.
- Z/A spans 0.40–0.50 for inorganic targets. This is consistent with WP8-F's statement.
- Free-electron metal parameters [E]:
  - Al: E_F 11.55 eV (2109.04473 uses 11.7, T11), v_F 2016 km/s, k_TF 4.04 keV.
  - Nb (scale only, d-band metal): E_F 15.4 eV, v_F 2325 km/s, k_TF 4.34 keV.
  - Nb Δ_BCS,E = 1.764k_BT_c = 1.63 meV uses the DFT McMillan T_c (10.72 K); the measured value stays GAP (IF-U6).
- `omega_bar_Debye_E` = (3/4)k_Bθ_D: the acoustic-Debye first moment. WP8-F's ω̄_κ needs the partial DOS (GAP).

---
## 6. S4: intrinsic radioactivity (coordinator addition)
**Criterion.** A material FAILS S4 if its intrinsic sub-keV rate exceeds **1 event/(kg·day·keV) below 1 keV**. The rate counts β
self-deposits plus the Compton continuum of intrinsic γ lines. A FAIL is marked EXCLUDED-RADIO. This is a reversible default
(coordinator, not yet confirmed by the user).

**Estimate [E] (build_v2.py §9).**
- Activities: the R13 a_rad per isotope (IAEA half-lives × NIST abundances).
- β shapes: allowed, or unique-n-th-forbidden, shape factor Σ_k p^{2k}q^{2(n−k)}/[(2k+1)!(2n−2k+1)!], times the non-relativistic
  Fermi function.
  - ⁴⁰K: unique 3rd forbidden, BR_β 0.893, Q 1311 keV; f(< 1 keV) = 4.13×10⁻⁴.
  - ¹¹⁵In: 4th-forbidden non-unique, Q 497 keV. The shape is unknown, so it is bracketed between unique-4th (f = 4.5×10⁻⁴) and
    allowed (f = 3.7×10⁻³).
  - ³H: allowed, Q 18.59 keV; f(< 1 keV) = 0.0892.
- γ (⁴⁰K, 1461 keV, BR 0.107): Klein–Nishina dσ/dT at T → 0, 2πr_e²/(m_e k²) (checked against the full formula, T10), × 𝓃_e × the
  mean chord 4V/S of a 1 kg cube.
- 2νββ: the Primakoff–Rosen summed spectrum.
- α: deposits ≫ 1 keV, so 0.
- EC isotopes with only a half-life lower limit (¹²³Te, ⁵⁰Cr): the bound assumes every capture is in the window, which gives COND.
- Pile-up at 1 kg: P = 1 − e^{−2Aτ}, with τ = 1 ms (phonon/TES) and 10 µs (fast charge).

**Validation of the shape machinery (T8).**
- Ge ³H at saturation: 7.13 against 7.2 /(kg·keV·d) in 1–7 keV [FT 1706.05818 p.20].
- NaI ³H: 7.89 against 7.9.
- Si: 0.00187 against "0.002 events/kg/keV/day for each day of sea-level exposure" (0–5 keV) [FT 2506.06568 p.1].
- Coordinator's rough numbers: KTaO₃ ~10⁵ and InSb ~5×10³. These are reproduced as 1.8×10⁵ and as the lower edge of the
  4.8×10³–3.9×10⁴ bracket.

| Material | Intrinsic sub-keV rate /(kg·d·keV) | Pile-up P at 1 kg (1 ms; 10 µs) | Cosmogenic ³H, 100 d / saturation | S4 |
|---|---|---|---|---|
| KTaO₃ | **1.8×10⁵** (⁴⁰K β 1.47×10⁵ + Compton 3.2×10⁴; A = 4.63 kBq) | **1.0; 0.088** | GAP | **FAIL → EXCLUDED-RADIO** |
| InSb | **4.8×10³ – 3.9×10⁴** (¹¹⁵In; A = 121 Bq) | 0.22; 2.4×10⁻³ | GAP | **FAIL → EXCLUDED-RADIO** |
| TeO₂ / PbTe / ZrTe₅ | ≤ 1.4×10⁻⁶ (2νββ, α), plus an ¹²³Te EC bound ≤ 693 / 330 / 760 | ≤ 2×10⁻⁵ | GAP | COND (only a T½ lower limit; measured ¹²³Te EC branching needed) |
| Cr₂O₃ | ⁵⁰Cr 2EC bound ≤ 503 | 1.2×10⁻⁵ | GAP | COND (same reason) |
| ZnO, ZnS, Li₂MoO₄, CaWO₄, CaF₂, PbSe, Bi₂Se₃ | 10⁻⁸ – 2×10⁻⁴ | ≤ 2×10⁻⁶ | GAP | PASS |
| Si | 0 | 0 | 0.17 / **11** | PASS (intrinsic); cosmogenic FAIL at saturation |
| Ge | 0 | 0 | 0.10 / **6.7** | PASS; cosmogenic FAIL at saturation |
| NaI | 0 | 0 | 0.11 / **7.4** | PASS; cosmogenic FAIL at saturation |
| all others | 0 (no primordial isotope) | 0 | GAP | PASS |

**Reading.**
- Intrinsic isotopes are irreducible: no purification removes ⁴⁰K or ¹¹⁵In except isotopic depletion. KTaO₃ is also paralysed by
  pile-up at 1 ms. KTaO₃ and InSb therefore leave the survivor pool. In v2, their `verdict` column and verdict row are changed;
  the verdict row note reads "supersedes R13 verdict=SURVIVOR-COND".
- Cosmogenic activation is **reducible**, through underground growth, fabrication and storage, and in Si through H out-diffusion
  (2506.06568). It is therefore reported as a column (`S4_cosmo_*`), not as a verdict. At 100 d of sea-level exposure, ³H passes
  the budget in Si, Ge and NaI; at saturation it fails by ×7–11.
- The other cosmogenics (³²Si, ²²Na, ⁷Be in Si; ⁶⁸Ge/⁶⁸Ga, ⁶⁵Zn, ⁵⁵Fe in Ge; their L/M-shell EC lines at 0.1–1.3 keV) are GAP. Their
  production rates are not in the full texts read [UNVERIFIED list]. The ³H scale of 32–228 atoms/(kg·d) over Na, I, Ge, Ar and Ne
  [FT 1706.05818 Table 1] is noted on the 37 `GAP:S4_cosmo` rows.
- Scope:
  - The budget applies to the intrinsic sub-keV region only. Surface ²¹⁰Pb, U/Th contamination and detector effects are not
    material properties, so they are excluded (WP8-F §2.8 (iii)).
  - Compton from external γ is excluded.
  - Pile-up is reported, not used in the verdict, except as supporting KTaO₃.

---
## 7. Checks (code/WP8-U-TOP/checks.py: 20 PASS, 0 FAIL)
**Integrity.**
- T0: provenance tags, locators and DB IDs on every new row.
- T1: all cited arXiv IDs verified (CSV and this file).
- T2: the R13 rows are preserved; the only changed cells are the verdict of the S4 failures.

**Sound speeds and moduli.**
- T3a: the Christoffel solver gives the isotropic limit exactly.
- T3b: the 1910.10716 c_LA outlier set is exactly {GaN, AlN, ZnO, α-SiO₂, NaCl}, and 13 of 22 agree within 10 %.
- T3c: the hexagonal outliers exceed every directional c_L by > 30 %, and NaCl lies below the minimum.
- T4: the VRH Young modulus is exact in the isotropic limit.

**Electron density and plasma energy.**
- T5a: the 2008.08560 n_e/N ratio is 2.0.
- T5b: ħω_p is 16.61 eV (Si, 4 e/atom) and 22.09 eV (diamond, from the paper's n_e); SiC 22.1 eV agrees with 4 e/atom to 4 %.

**Born charges.**
- T6: Z*_LST reproduces 1910.10716 Z̄*: median 1.6 %, maximum 12 %.

**ε_eh bracket.**
- T7: 12 of 13 measured values lie inside; HgI₂ is the exception.

**β shapes and Compton.**
- T8: the ³H shape reproduces three full-text background rates to ≤ 7 %.
- T9: the β normalisation and the unique-3rd coefficients 1:7:7:1 are right.
- T10: the Klein–Nishina T → 0 limit agrees with the full formula.

**Other closed forms.**
- T11: Al E_F agrees with 2109.04473 to 1.3 %.
- T12: GaAs ω_T,LST agrees with 1910.10716 to 1 %.

**Coverage and verdicts.**
- T13: §5.2 coverage is complete (value or GAP).
- T14: the S4 FAIL set is {KTaO₃, InSb}, and their verdict is propagated.
- T15: the non-positive-definite MnO tensor is flagged.

---
## 8. Literature (IDs verified 2026-11-01 against the arXiv API)
**arXiv, [FT].** 2610.16949 (ε_eh compilation, Table II; laws, p.4); 2311.05011 (diamond ε_eh); 2311.03902 (4H-SiC ε_eh, F, Tables 1–2); 1308.2886 (SiC ε(T)); 1602.08005 (Ge ε, F at 77 K and 50 mK); 1706.05818 (³H rates); 2506.06568 (Si ³H); 1705.06594 (YIG magnons); 1806.07968 (NiO AFMR); 2609.20122 (MnO AFMR); 2010.08926 (Cr₂O₃ gap); 1704.01758 (Li₂MoO₄ ρ); 1807.10291 (GaAs, sapphire ε and modes); 1910.10716 (c_LA definition p.13, ω_O); 2008.08560 (Table I).

**arXiv, cited through R13 rows only.** 2004.11499, 1901.07569, 1905.13744, 2004.10709, 2210.13516, 2109.04473.

**Non-arXiv full texts.** DS09, WBG24, GAN20, CZT23, SEL26 and BV25 (Europe PMC XML, see the header).

**Not accessed.** Kaplan 1979 (closed); Owens & Peacock, NIM A 531, 18 (2004) (closed, per Unpaywall); Bertuccio & Maiocchi
(2002, GaAs ε); Redus 1997 (CZT F); Shimaoka 2016 (diamond F). The last three are known only through citing texts.

**Walk.** The arXiv API is thin on detector-materials literature, so the ε_eh search was completed through Europe PMC full-text
search ("pair creation energy", "Fano factor" × material). INSPIRE was not needed: no citation walk.

---
## Symbols introduced/used
**Used (NOTATION v4 and the WP7-E rows).** ρ_T, E_g, E_x^b, E_min(q), ε_∞, ε₀, Z*_κ, ω_L, ω_T, c_ν (c_LA, c_TA), D_κ(ω), ω̄_κ,
M_κ, A_κ, Z_κ, 𝓃_e, ω_p, v_F, k_TF, E_F, Δ_BCS, Δ_D, ε_bg, g_deg, 𝐒_j, λ_{S,j}, J^{ex}_{ij}, F^{mag}_j, g_{mnν}, ε_eh, F_eh, y_ion,
E_d, E_st,1, p_surv, tanδ₀, ε_r, P̄_STM, Ω, μ_red. Also, from WP8-F (new there): 𝓃_S, Δ_mag, ω_max^mag, ω_max^ph, Y_mod, Δα_th,
b_bg. From WP8-U (proposed there): θ_D, c_L^{iso}, 𝓃_e^{val}, a_rad, 𝓃_spin.

**Introduced (WP8-U-TOP; proposed rows).**
| Symbol | Meaning | CSV name |
|---|---|---|
| c̄_LA^{Chr}, c̄_TA^{Chr} | sphere-mean Christoffel phase speeds from C_ij (the 1910.10716 App. A3 definition) | c_LA_Christoffel_avg, c_TA_Christoffel_avg |
| Y_mod^{H} | Voigt–Reuss–Hill Young modulus | Y_mod_Hill |
| Z*_LST | diatomic rigid-ion Born charge from (ε₀, ε_∞, ω_T, Ω, μ_red) | Zstar_LST |
| ε_eh^{br} | empirical bracket [1.54E_g + 1.89, (14/5)E_g + 0.5] | eps_eh_bracket_E |
| 𝓇_{<1}^{int}, 𝓇_{<1}^{cos} | intrinsic and cosmogenic rate density below 1 keV, /(kg·d·keV) | S4_intrinsic_sub1keV, S4_cosmo_3H_* |
| P_pu, τ_res | pile-up probability at 1 kg; resolving time | S4_pileup_1kg |
| f_{<1}(β) | fraction of a β spectrum below 1 keV | data/s4_fractions.json |
| S4 | the fourth screening criterion (intrinsic radioactivity) | S4_verdict |
| T0–T15 | check labels (always prefix WP8-U-TOP-) | – |

No new symbol clashes with NOTATION. Δ_mag carries ⚠ against Δ_BCS and Δ_D, which keep their subscripts.

## Interface flags
- **IF-T1 (WP8-F, all FOM users).**
  - Adopt `n_e_val_recommended` (4 e/atom) for C, Si and SiC, and ħω_p(diamond) = 31.2 eV [E].
  - Adopt `c_LA_recommended` for GaN, AlN, ZnO, α-SiO₂ and NaCl.
  - The R13 1910.10716 c_LA rows of those five, and the 2008.08560 n_e column, are superseded (closes IF-U9).
- **IF-T2 (coordinator, WP8 ranking).** S4 moves KTaO₃ and InSb to EXCLUDED-RADIO. TeO₂, PbTe, ZrTe₅ and Cr₂O₃ are S4-COND:
  ¹²³Te/⁵⁰Cr EC have only lower half-life limits, and their sub-keV branching is the open input. The criterion is a reversible
  default pending the user's confirmation; reverting it means dropping the S4 rows and restoring the two verdict cells.
- **IF-T3 (WP8-R).** Al and Ir moduli are now [DB] (§4). The Al and Nb DB shear stiffness is suspect (C₄₄ 16.2 and 6.6 GPa); use it
  at ±40 % until measured C_ij are tabulated. Kaplan 1979 was not accessed.
- **IF-T4 (WP5 / joint WP5 + WP7-E audit).**
  - The measured ε_eh/F_eh (§2.1) carry method and temperature.
  - Ge has both 77 K and 50 mK values (2.96 against 3.37 eV), which matters for the mK-bolometer threshold in quanta.
  - 4H-SiC F has 0.100 and ≤ 0.04 in tension.
  - AlN has no measurement.
  - All rows remain (prov.) per WP8-F.
- **IF-T5 (WP8-F).**
  - Still GAP for every material: L(q,ω)/ε₂ data pointers, the partial phonon DOS, tanδ₀/P̄_STM, EPW g/ω_TA(Q*), ∫Δα_th dT,
    E_st,1/p_surv, y_ion/QF, the Born tensors, and the non-³H cosmogenics.
  - Also GAP: CaWO₄ and Li₂MoO₄ ε₀/ω_LO/TO/Z*, and ε_eh for scintillators, ionic crystals and wide-gap oxides (bracket only).
  - These are measurement or tier-H priorities, not table work.
- **IF-T6 (WP8-U v3).** The JARVIS MnO tensor is not positive definite (a mechanically unstable DFT cell). Add it to WP8-F's §5.3
  vetting rules as rule (v): require positive-definite C_ij.
- **IF-T7 (coordinator).** Five non-arXiv full texts (Europe PMC XML) and the detector-reference materials (CdTe, CZT, HgI₂, TlBr) were
  added to the CSV as `NOT-SCREENED`. They are not candidates.

## Proposed LIMITS rows (numbers provisional; the coordinator assigns)
| # | Chain (URF) | Source | Validity | Leading correction | Status |
|---|---|---|---|---|---|
| LT1 | long-wavelength acoustic branch of WP2-v3 (2.2) → Christoffel eigenproblem ρω² = C_ijkl q_j q_l → sphere mean c̄_LA (the 1910.10716 App. A3 definition) | 1910.10716 p.13 [FT]; JARVIS C_ij [DB] | q ≪ q_BZ (q ≈ 10 eV), harmonic, 0 K tensor | dispersion at finite q; T-dependence of C_ij; DFT functional (≤ 10–15 %) | CHECKED (T3a–c; 13/22 ≤ 10 %) |
| LT2 | WP2-v3 (4.2)–(4.3) rank-1 polar ε, one TO branch → ε₀ − ε_∞ = Z*²e²/(ε₀^{SI}Ωμ_redω_T²) | 1910.10716 Table I [FT] consistency | diatomic, isotropic (or one principal axis), rigid ion | multi-mode crystals (sum over ν); electronic-polarisation (shell) corrections | CHECKED (T6, median 1.6 %) |
| LT3 | β self-deposit + KN Compton → sub-keV intrinsic rate (S4) | 1706.05818 p.20, 2506.06568 p.1 [FT] (³H validation) | bulk emitter, full containment of β; single Compton deposit at T → 0; 1 kg cube | forbidden shape factors (¹¹⁵In bracket ×8); atomic exchange/screening at E < 1 keV; multiple scattering | ESTIMATED (T8–T10) |
