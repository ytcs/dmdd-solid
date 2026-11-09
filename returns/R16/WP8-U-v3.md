# R16 / WP8-U-v3: the pickable universe of substrate materials and its property table (standalone revision after R14 and the R16 verification)

Agent ERR-CW7 (brief briefs/R16/ERR-CW7.md), on the text of WP8-U-v2 by agent CW7 (brief briefs/R16/CW7.md, rows LE-19, LE-176, LE-177). This file replaces
returns/R16/WP8-U-v2.md, returns/R13/WP8-U.md and returns/R14/WP8-U-top.md as the authoritative WP8-U text; all three remain the historical record.
**v3 absorbs** referees/R16/VER-CW7.md §A, §B8, §B9 (the 55 [E]-evidence screening rows, the 13 contradictory keys, the TeO₂ ρ proxy, V1–V6, CaWO₄ ³H, Ge
L-lines, PbTe/PbS shifts) and the table-level findings of referees/R16/REF-WP8-S-A.md and -B.md (JARVIS shear-order defect of every non-cubic elastic tensor,
GAP-input dropouts per channel, ²¹⁰Pb in lead salts); closing rows in §9 (v3 block). Companion: returns/R16/CW7-errata.md. The v2 text follows,
amended in place. v2 header: It absorbs referees/R14/REF-WP8-U-A.md and REF-WP8-U-B.md (closing table, §9), the
WP8-U-TOP top-up (S4, ε_eh/F_eh, source disputes, §5.2 coverage), the GAP-EF predictions (IF-EF3) and the WP5-AUD release of the yield rows (IF-AUD-5).
CONVENTIONS (incl. R13 amendments, [CALC] tag), NOTATION v4 and state/CORRECTIONS.md (§0 global renames; no WP8 section) were read.
**Deliverables.** returns/R16/WP8-U-table-v4.csv (3421 rows, same 11 columns), built offline by `code/CW7/build_v4.py` from the v3 table
(returns/R16/WP8-U-table-v3.csv: 3311 rows = the 2997 v2 rows verbatim + 314 R16 rows, built by `code/CW7/build_v3.py`). v4 = v3 − 13 superseded screening
rows (recorded verbatim in code/CW7/data/v4_changes.json), with 44 screening rows retagged, the `verdict` column set to the final verdict, one row corrected
(CaWO₄ `cosmo_identified`), + 123 new rows. Checks in `code/CW7/checks.py` (cited CW7-Cn; C28–C30, C33–C35 are the table checks; 40/40 PASS). Full texts fetched with lit.py into
literature/papers-CW7/ (page = PDF page; PDFs deleted, `.txt` extracts kept for the locators). No first-principles numerics were run.
**Tags** (CONVENTIONS §12): [FT] full text with locator; [DB] database entry (JARVIS-DFT dft_3d 9-24-2025 `JVASP-n`, MP/Alexandria OPTIMADE, NIST, IAEA;
the tag is the WP8 data convention, owed to CONVENTIONS §12 as an amendment, §10 Owed); [E] closed form from tagged inputs (formula in `locator`); [D] an
exact identity (e.g. Z* = 0 in a non-polar crystal, WP2-v3 (4.5)); [UNVERIFIED] memory; **GAP** an explicit `GAP:<item>` row with its reason.
A row that replaces a value has a `note` beginning "supersedes R13/R14 <property>=<value>" (v3) or "v4 …" (v4). **Reading rule (v4): for any
(material, property) with several rows, the last row whose note says "supersedes" wins; the screening keys `screen_S1–S3` and `verdict` are unique, and the
`verdict` column of every row is the material's final verdict** (VER-CW7 §A; CW7-C29).

---
## 0. Results at a glance
| # | Item | Result |
|---|---|---|
| 1 | Pool | 54 table keys: 47 screened materials, 4 detector references (CdTe, CZT, HgI₂, TlBr; NOT-SCREENED), Ir (sensor film), 2 law rows; 7 proposal families excluded (§3) |
| 2 | Screening (one rule, §2) | **10 SURVIVOR** (Si, Ge, GaAs, Al₂O₃, TeO₂, CaWO₄, Li₂MoO₄, γ-LiAlO₂, LiF, NaF), **32 SURVIVOR-COND** (incl. NiPS₃, h-BN, c-BN, PE moved from EXCLUDED), **2 EXCLUDED-RADIO** (KTaO₃, InSb; S4), 3 REFERENCE |
| 3 | GaAs S2 | PASS on full text: "a 4.3 g GaAs (GaAs-1)" and a 3.5 g crystal operated as mK scintillating calorimeters [FT 2507.07119 p.1–2] |
| 4 | ε_eh, F_eh | measured [FT] for Si, Ge (77 K, 50 mK), diamond, 3C/4H/6H-SiC, GaAs, GaN, a-SiO₂ (+ CdTe, CZT, HgI₂, TlBr); F_eh for Si, Ge, 4H-SiC, CZT. Every other survivor: GAP-EF one-parameter prediction [E] with band (§4.2) |
| 5 | Low-T ε₀ of soft-mode crystals (LE-176) | SrTiO₃ ≈ 2×10⁴ (0.3 K, model-inferred from a fitted χ⁻¹) and 2.3×10⁴ (4 K); KTaO₃ ≈ 5×10³ (0.3 K, fitted); PbTe > 10³ [FT]; PbS, PbSe: no measured low-T value read (DFPT 161, 174 pass V2). The quantum-paraelectric DFPT ε₀ (SrTiO₃, KTaO₃, PbTe) are unusable; the POL/ER FOMs are insensitive to ε₀ to O(ε_∞/ε₀): PbTe 2.8–5.6%, PbS 10.3% (§4.3) |
| 6 | Cosmogenics (LE-177) | sea-level production rates [FT]: Si (³H, ⁷Be, ²²Na), Ge (³H, ⁴⁹V, ⁵⁵Fe, ⁶⁵Zn, ⁶⁸Ge ≥ 74), NaI (I, Te, ²²Na), natTe (ACTIVIA, calc.); CaWO₄ ¹⁷⁹Ta, ¹⁸¹W observed and ³H inferred, rate GAP; all others GAP with the computation specification (CW7 LE-177; Geant4 convergence target in CW7-errata §1.11). ²¹⁰Pb: a material property of the lead salts (S4 condition a(²¹⁰Pb) ≲ 1.5 mBq/kg [E], §4.4); otherwise process/surface (GAP) |
| 7 | Source disputes | 2008.08560 n_e column = 2 e/atom × N (CONFIRMED by both referees; use 4 e/atom); 1910.10716 hexagonal/NaCl c_LA **suspect, pending measured C_ij** (both routes are DFT); 1910.02091 Δ = half-gap (IF-U5 closed) |
| 8 | Vetting | one DB rule set **V1–V6** (§1.3) replaces the R13 and WP8-F §5.3 variants: ε₀ dropped for 13 failed-IR runs + InSb (CW7-C30); **V5′**: JARVIS elastic tensors re-indexed (§4.1′) |
| 9 | Table rules (v4) | screening keys unique (13 duplicates resolved), no [E] screening evidence (55 rows: 44 retagged [UNVERIFIED], 11 dropped), `verdict` column = final verdict, "last superseding row wins" (CW7-C29) |
| 10 | Elastic tensors (REF-WP8-S-A §5c) | the JARVIS shear order is (xy, yz, zx); every non-cubic C_ij, Christoffel speed and NR edge of R14–R16 was built with C₄₄ ↔ C₆₆ swapped and C₁₄ misplaced. Rebuilt: the [001] TA pair is degenerate in all 13 uniaxial entries; TeO₂ c̄_LA 4.05 → 4.10 km/s; new `c_NR1_heavy` (§4.1′; CW7-C33, C34) |
| 11 | Channel coverage (REF-WP8-S-A §2) | `GAP:channel_inputs` rows: Li₂MoO₄ enters only the Migdal nuclear factor; TeO₂, SrTiO₃, γ-LiAlO₂ have no measured E_g; Al, Nb need a 2Δ_BCS edge line (§4.5) |

---
## 1. Sources and method
### 1.1 Databases and closed forms
JARVIS-DFT dft_3d (9-24-2025; cached extract code/WP8-U/data/jarvis_extract.json, WP8-U-TOP data/jarvis_top.json); MP and Alexandria OPTIMADE
(structures, E_hull; CsI, Li₂MoO₄, YIG absent from JARVIS); NIST isotopic compositions; IAEA LiveChart (ENSDF 2023-10-18). Closed forms [E], recomputed
in code/WP8-U/checks.py, code/WP8-U-TOP/checks.py and by both referees: ρ from a_exp (Z_fu M/N_A V); Voigt c_L, c_T; Christoffel sphere-mean c̄_LA^{Chr}
(the 1910.10716 App. A3 definition); Voigt–Reuss–Hill Y_mod; Anderson T_D (renamed from θ_D, §8); g_iso = Σx_i(1 − m_i/m̄)²; single-mode LST
ω_L = ω_T(ε₀/ε_∞)^{1/2}; diatomic rigid-ion Z*_LST; 𝓃_e^{val}, ω_p^{val} (4 e/atom for group-IV, outer s+p, d¹⁰ semicore); a_rad = Σ ln2 N_iso/T½;
S4 sub-keV rates (β shapes, Klein–Nishina T → 0, pile-up).
### 1.2 Literature
Property sources read in full text: 1910.10716, 2008.08560, 1901.07569, 2004.10709, 1905.13744, 2210.13516, 1910.02091, 2109.04473, 2310.05815,
2502.01732, 2201.04219 (R13); 2610.16949, 2311.05011, 2311.03902, 1308.2886, 1602.08005, 1706.05818, 2506.06568, 1705.06594, 1806.07968, 2609.20122,
2010.08926, 1704.01758, 1807.10291 and six Europe PMC texts DS09, WBG24, GAN20, CZT23, SEL26, BV25 (R14); 2507.07119, 2007.10584, 1607.04560, 1411.0106,
1411.5947, 1908.06755, 0903.1445, 1607.08146, 1003.5140 (this revision). Citation walks (INSPIRE refersto) as in R13. All arXiv IDs cited here are
verified against the API (code/CW7/data/arxiv_verified.json, CW7-C32).
### 1.3 One database vetting rule set (closes IF-U1, IF-F7, IF-T6; REF-WP8-U-A E1, REF-WP8-U-B C1–C2, REF-WP8-F-B §8)
- **V1 gaps.** No DFT gap (OptB88vdW, TBmBJ, HSE, PBE) is used for an edge. WP8-F §5.3(i) "MBJ within ≈ 10%" is withdrawn: −13% GaAs, −19% Ge (REF-WP8-F-B V17).
- **V2 DFPT ε and IR modes.** A DFPT ε₀ or IR mode is GAP if `max_ir_mode` < 20 cm⁻¹ (failed IR run) **or** the OptB88vdW ground state is metallic (gap < 0.05 eV),
  whatever TBmBJ says. Applied to ε₀ as well as ω_T: 14 `GAP:eps_0_DFT_vetted` rows (SiC-3C, InSb, ZnO, γ-LiAlO₂, LiF, NaCl, NaI, ZnS, PbTe, SrTiO₃, KTaO₃,
  Bi₂Se₃, c-BN, PE; CW7-C30). A quantum-paraelectric crystal's DFPT ε₀ (SrTiO₃, KTaO₃, PbTe) is unusable even when the run passes (§4.3).
- **V3 polymorph.** Experimental space group at the operating temperature; declared exception SrTiO₃ (properties from cubic Pm-3m JVASP-8082; mK phase
  I4/mcm, JVASP-269), recorded as a `polymorph_note` row.
- **V4 tensor maxima.** `dfpt_piezo_max_dielectric_*` and `min/max_ir_mode` are maxima over directions: rigorous only for cubic entries; for uniaxial
  crystals any bracket built from them is labelled "orientation-maximal" (REF-WP8-F-A F11, -B V10).
- **V5 elastic tensors** must be positive definite (MnO JVASP-7870 fails; IF-T6). DB shear moduli of Al and Nb (C₄₄ 16.2, 6.6 GPa) are used at ±40% only (IF-T3).
- **V5′ shear order (v3).** JARVIS `elastic_tensor` lists the shear rows as (xy, yz, zx); the Voigt order is (yz, zx, xy). Proof [D]: hexagonal and trigonal
  symmetry force C₆₆ = (C₁₁ − C₁₂)/2, and JARVIS index 3 satisfies it in all 10 such entries to 0.05 GPa (GaN 107.2 vs 107.15; SiC-4H 193.7; Al₂O₃ 158.3 vs 158.25),
  while index 3 = C₄₄ would not. Re-index (Voigt index I ← JARVIS index (0, 1, 2, 4, 5, 3)_I) before any Christoffel, edge or C_ij use (CW7-C33).
- **V6 provenance ranking.** For one property: [FT] measured > [FT] DFT-from-a-paper > [E] from FT inputs > [DB]. The summary (§4.1) uses this ranking
  everywhere (REF-WP8-U-A D6: Ge, GaAs ρ are [E] from a_exp, not [DB]). **Declared exception:** sound speeds use the Christoffel mean [E from DB C_ij] ahead of
  1910.10716's c_LA [FT, DFT-in-paper] where both exist, because §5 rules the latter "suspect"; spread ≤ 10% where checked (`c_LA_check_1910` 0.91–1.10).

---
## 2. Screening
**Criteria.** S1 thermal cycling 300 K ↔ mK (no harmful transition in 0.01–300 K, not hygroscopic, **demonstrated mK operation**); S2 ≥ 1 g detector-grade
growth; S3 an instrumentable surface; S4 intrinsic radioactivity ≤ 1 /(kg·d·keV) below 1 keV (coordinator default, reversible, not yet confirmed by the user).
**One rule (REF-WP8-U-A F3; REF-WP8-U-B V2).** FAIL needs positive evidence that the criterion cannot be met. An item shown only as a proposal, with an unshown
mass, or on [E]/[UNVERIFIED] evidence is COND everywhere. [E] is a step tag and is no longer used as screening evidence; such entries read [UNVERIFIED].
**Applied in the table (v4):** every `screen_S*` cell that rested on [E] reads [UNVERIFIED], and a PASS/FAIL on that evidence alone reads COND (44 cells;
no SURVIVOR verdict changes; Al₂O₃ S2 keeps PASS on [ABS 1704.04320]); the R13-rename rows superseded by an explicit COND/PASS row are dropped (13 keys).
Consequences: NiPS₃, h-BN, c-BN and polyethylene move EXCLUDED → SURVIVOR-COND; S1 of GaN, AlN, ZnO, GaSb, MgO, CaF₂, MgF₂, SiC (3C/4H/6H) and α-SiO₂ is
COND (no mK operation read), verdicts unchanged; the ID-less "[ABS INSPIRE '…']" items are dropped where another ID'd item supports the cell (Al₂O₃ S1:
2203.15903). Locator fix: the 2008.08560 "fabrication scale", "fairly straightforward", "large boules" quotes are on PDF p.20, not p.21.
| Material | S1 | S2 | S3 | S4 | Verdict |
|---|---|---|---|---|---|
| Si, Ge | PASS [ABS 2407.08085, 2212.12513; 2203.03993] | PASS | PASS | PASS (³H cosmogenic column) | S |
| GaAs | PASS [FT 2507.07119 p.1–2] | **PASS [FT 2507.07119: 4.3 g, 3.5 g]** | PASS [ABS 2507.07119] | PASS | S |
| Al₂O₃, TeO₂, CaWO₄, Li₂MoO₄, γ-LiAlO₂, LiF, NaF | PASS [ABS, IDs in CSV] | PASS ([ABS]; LiF, NaF, Al₂O₃ mass from titles only) | PASS | PASS (TeO₂ COND: ¹²³Te) | S |
| diamond, SiC, GaN, AlN, ZnO, GaSb, α-SiO₂, MgO, CaF₂, MgF₂, NaI, CsI, NaCl, ZnS, Pb salts, SrTiO₃, ZrTe₅, Bi₂Se₃, Al, Nb, YIG, NiO, MnO, Cr₂O₃ | as R13 / COND ([E] cells read [UNVERIFIED]) | as R13 | as R13 | PbTe, ZrTe₅, Cr₂O₃ COND; **Pb salts ²¹⁰Pb COND (§4.4)** | C |
| NiPS₃, h-BN, c-BN, PE | COND | COND (no ≥ 1 g shown) | COND (PE: TES on H-rich crystals proposed only [FT 2201.04219 p.2]) | PASS | **C** (was X) |
| KTaO₃, InSb | – | – | – | **FAIL**: 1.8×10⁵ (⁴⁰K) and 4.8×10³–3.9×10⁴ (¹¹⁵In) /(kg·d·keV) | EXCLUDED-RADIO |
| a-SiO₂, solid ⁴He, superfluid ⁴He | reference rows | | | | R |

## 3. Exclusions (families; unchanged in kind, provisional where the evidence is [UNVERIFIED])
Halide perovskites (S1, [UNVERIFIED] transitions; provisional), Yb₃PbO/BNQ-TTF (S2, [FT 1910.02091 p.13]), aromatic organics (S3), graphene/CNT (not a
≥ 1 g bulk substrate), chiral-phonon MOFs, flat-band candidates, solid He as a substrate (pressurised; REFERENCE). Out of scope: SNSPD targets, molecules,
levitated sensors (R13 §5).

---
## 4. The property table
### 4.1 Survivor summary (best provenance per V6; full rows in the v4 CSV)
Units: ρ_T g/cm³; E_g eV (measured, room T unless the CSV says low T); ω_max meV; c̄_LA km/s (`c_LA_recommended` or the Christoffel mean; R13 c_LA where it agrees
within 20%); ħω_p^{val} eV; ε_eh eV (measured, else GAP-EF [E]); a_rad Bq/kg ("<" = bound from unobserved decays). ᶠ [FT], ᵈ [DB], ᵉ [E].
| key | v | ρ_T | E_g | ε_∞ | ε₀ | Z̄* | ω_max | c̄_LA | ħω_p^{val} | ε_eh | a_rad |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Si | S | 2.33ᶠ | 1.12ᶠ | 11.7ᶠ (= ε₀) | 11.7ᶠ | 0 [D] | 62.3ᶠ | 8.76ᵉ | 16.6ᶠ | 3.749ᶠ (123 K) | — |
| Ge | S | 5.33ᵉ | 0.67ᶠ | 16.0ᶠ (= ε₀) | 16.0ᶠ | 0 [D] | 34.8ᶠ | 4.82ᵉ | 15.6ᵉ | 2.96ᶠ (77 K); 3.37ᶠ (50 mK) | ⁷⁶Ge (2νββ), GAP |
| GaAs | S | 5.32ᵉ | 1.42ᶠ | 10.89ᶠ | 12.9ᶠ | 2.27ᶠ | 34.9ᶠ | 4.84ᵉ | 15.6ᵉ | 4.2ᶠ | — |
| Al₂O₃ | S | 3.99ᵉ | 8.8ᶠ | 3.2/3.26ᶠ | 11.5 ∥ / 9.3 ⊥ᶠ | 2.97ᶠ | 104ᶠ | 10.8ᵉ | 27.9ᵉ | 16.5 (15.5–19.6)ᵉ | — |
| TeO₂ | S | 5.92ᵈ (DFT proxy) | GAP (DFT only) | 6.45ᵈ | 28.8ᵈ | GAP | 89.0ᵈ | 4.10ᵉ | 23.5ᵉ | 9.7 (9.1–11.4)ᵉ | < 8.1×10⁻³ᵉ |
| CaWO₄ | S | 6.12ᵉ | 5.2ᶠ | 3.84ᶠ | GAP | 2.84/4.67ᶠ | 106ᶠ | 4.26ᶠ | 23.8ᵉ | 10.7 (10.0–12.6)ᵉ | 4.3×10⁻⁵ᵉ |
| Li₂MoO₄ | S | 3.04ᶠ | GAP | GAP | GAP | GAP | GAP | GAP | 21.6ᵉ | GAP | 1.1×10⁻³ᵉ |
| γ-LiAlO₂ | S | 2.58ᵈ (DFT proxy) | GAP | 2.74ᵈ | GAP (V2) | GAP | 102ᵈ | 8.11ᵉ | 22.8ᵉ | GAP | — |
| LiF | S | 2.65ᵉ | 14.2ᶠ | 2.02ᶠ | GAP (V2) | 1.05ᶠ | 77.2ᶠ | 7.47ᵉ | 26.1ᵉ | 25.1 (23.4–30.7)ᵉ | — |
| NaF | S | 2.80ᵉ | 11.5ᶠ | 1.78ᶠ | 4.79ᵈ | 0.98ᶠ | 49.9ᶠ | 6.03ᵉ | 21.1ᵉ | 20.5 (19.2–25.0)ᵉ | — |
c̄_LA of non-cubic entries are the v4 re-indexed values (§4.1′; Al₂O₃ 10.78 and γ-LiAlO₂ 8.11 unchanged at this precision, TeO₂ 4.05 → 4.10); the heavy-mediator
NR-1ph speed c_NR1 = ⟨Σ_ν(q̂·ê_ν)²/c_ν⟩⁻¹ is in the `c_NR1_heavy` rows (Si 8.69, Ge 4.78, GaAs 4.78, Al₂O₃ 10.74, TeO₂ 3.76, γ-LiAlO₂ 8.05 km/s).
SURVIVOR-COND rows: as R13 §4.1 with the v3/v4 supersessions (SiC c_s relabelled; GaN, AlN, ZnO, α-SiO₂, NaCl c̄_LA = 7.38, 10.71, 5.91, 6.23, 4.86 km/s; C, Si,
SiC 𝓃_e^{val} at 4 e/atom and diamond ħω_p^{val} = 31.2 eV; SrTiO₃/KTaO₃/Pb-salt ε₀ per §4.3; magnon gaps per WP8-U-TOP §5.1; YIG s_spin = S_cell/Ω).
Diamond: non-polar, TO = LO at Γ; use ω_max = 161–163 meV and no ω_T (REF-WP8-U-B C9). Ge E_g = 0.54 eV (1901.07569) matches no tabulated gap [UNVERIFIED]
and is not offered (C8). Al Δ_BCS = 0.3 meV is 2109.04473's working value; 1.764k_BT_c ≈ 0.18 meV [UNVERIFIED] — a factor ≈ 1.7 flag, not a value (IF-U6).
### 4.1′ Elastic tensors after the shear-order fix (REF-WP8-S-A §5c; v4 rows `C_ij_Voigt_DFT_v4`, `c_LA_Christoffel_avg`, `c_dir_100_001`, `c_NR1_heavy`, `c_LA_max_dir`)
| Entry (class) | C₄₄ / C₅₅ / C₆₆ (GPa, Voigt) | C₁₄ | [001] T (km/s), R14–R16 → v4 | c̄_LA, R14–R16 → v4 | c_NR1 | c_LA,max |
|---|---|---|---|---|---|---|
| TeO₂ (tetragonal) | 29.1 / 28.8 / 72.7 | 0 | 2.22/3.51 → 2.21/2.22 | 4.05 → 4.10 | 3.76 | 4.61 |
| Al₂O₃ (trigonal) | 140.9 / 140.9 / 158.3 | −20.8 | 6.02/6.39 → 6.03/6.03 | 10.77 → 10.78 | 10.74 | 11.12 |
| α-SiO₂ (trigonal) | 55.6 / 55.6 / 34.4 | 14.5 | 3.64/4.62 → 4.62/4.62 | 6.19 → 6.23 | 6.01 | 6.92 |
| MgF₂ (tetragonal) | 54.4 / 54.4 / 98.0 | 0 | 4.18/5.61 → 4.18/4.18 | 7.62 → 7.64 | 7.45 | 8.27 |
| γ-LiAlO₂ (tetragonal) | 60.7 / 60.7 / 63.6 | 0 | 4.85/4.96 → 4.85/4.85 | 8.11 → 8.11 | 8.05 | 8.41 |
| GaN, AlN, ZnO, SiC-4H (hexagonal) | C₆₆ = (C₁₁ − C₁₂)/2 at JARVIS index 3 | 0 | degenerate in v4 | 7.38, 10.71, 5.91, 12.20 | 7.35, 10.69, 5.90, 12.14 | 7.93, 10.98, 6.19, 13.05 |
| h-BN; PE (layered; orthorhombic) | 5.5/5.5/342.7; 8.8/2.4/4.0 | 0 | – | 15.87 → 15.49; 9.40 → 9.38 | **6.80; 4.89** | 19.6; 17.6 |
The residual TeO₂ asymmetry (C₄₄ 29.1 vs C₅₅ 28.8, C₁₁ 56.3 vs C₂₂ 56.9) is numerical noise of the DFT cell (0.5%). The c̄_LA changes are ≤ 2%, but the
heavy-mediator scalar c_NR1 differs from c̄_LA by branch mixing (TeO₂ −8%, α-SiO₂ −4%, h-BN −56%): rank on c_NR1, not c̄_LA (WP8-F-v3 §5.1). The NR-1ph edge of
an anisotropic crystal is set by c_LA,max (fastest direction with (q̂·ê_LA)² ≠ 0): Al₂O₃ 5.16 keV at 1 meV vs 5.32 keV with c̄_LA [E].
### 4.2 ε_eh and F_eh (closes LE-8 for the survivors)
Measured values with method and temperature: WP8-U-TOP §2.1 (all [FT], kept verbatim in v3). For the survivors without a measurement the v3 table carries
`eps_eh_pred_GAPEF` and `F_eh_pred_GAPEF` [E] from GAP-EF §3 (one calibrated parameter 𝒜_ph; band = variant spread ⊕ validation range; the polar/stiff
wide-gap materials are under-predicted, so the upper half of each band is the likelier). The empirical bracket [1.54E_g + 1.89, (14/5)E_g + 0.5] is kept as a
second, model-free row. Both are **released for FOM use by WP5-AUD §5.2 with its text corrections** (IF-AUD-5): ε_eh and F_eh are asymptotic (≳ 50 eV);
near threshold the threshold-in-quanta uses P(N_eh|q,ω) (WP5 (W5)–(W6); continuous form: CW7 LE-153).
### 4.3 Soft-mode crystals (LE-176)
| Material | DFPT ε₀ [DB] | Measured low-T ε₀ [FT] | Use |
|---|---|---|---|
| SrTiO₃ | 9.96 (failed IR, V2) | χ⁻¹ = 5×10⁻⁵ at 0.3 K, a fit parameter of the equation of state (polarisation in a field) ⇒ ≈ 2×10⁴, model-inferred [0903.1445 Table 1 p.6]; 23,000 at 4 K (quoted) and 27,400 (device extraction) [1607.08146 p.1–2] | measured value; added to IF-U4 |
| KTaO₃ | 386 (failed IR) | χ⁻¹ = 2×10⁻⁴ at 0.3 K ⇒ ≈ 5×10³ [0903.1445 Table 1 p.6] | EXCLUDED-RADIO anyway |
| PbTe | 499 (failed IR) | "> 1000" at low T [1003.5140 p.11] | lower bound |
| PbS, PbSe | 161, 174 (pass V2: IR 66.8, 46.1 cm⁻¹) | GAP (not in the texts read) | not quantum paraelectrics; DFPT value usable with its DB width; FOMs insensitive (≤ 10.3%, below) |
**Why these FOMs survive the missing ε₀ [D] (CW7 LE-176).** The polar weight is Σ_νΔ_ν = 1/ε_∞ − 1/ε₀, so ∂ln(Σ_νΔ_ν)/∂lnε₀ = ε_∞/(ε₀ − ε_∞) → 0 for
ε₀ ≫ ε_∞: replacing the DFPT ε₀ by the measured one moves it by **2.8–5.6%** (PbTe, ε₀ from 1000 to ∞; "> 1000" is a bound), 1.3% (KTaO₃), **10.3%** (PbS,
ε₀ → ∞) — but by ×2.75 for SrTiO₃'s failed-run 9.96 (CW7-C17). In the rigid-ion model ε₀ = ε_∞ + S_osc/ω_T² → ∞ as the soft ω_T → 0 while ω_L² → S_osc/ε_∞
stays finite (CW7-C18), so ω_LO, ε_∞ and Z* — the inputs of (2.5b) — are regular. Not covered: absorption
at m_φ ≈ ω_TO(soft), which is ε₀- and T-sensitive and needs measured ε(ω, T).
### 4.4 Radiopurity, S4 and cosmogenic activation (LE-177)
S4 (WP8-U-TOP §6, unchanged; validation T8 reproduced as CW7-C19): KTaO₃ and InSb FAIL; TeO₂, PbTe, ZrTe₅, Cr₂O₃ COND (¹²³Te/⁵⁰Cr EC known only as T½ lower
limits). Corrections: ⁷⁶Ge is a primordial 2νββ emitter (activity GAP, negligible); the a_rad of TeO₂, PbTe, PbS, PbSe, ZrTe₅, ZnO, ZnS and Cr₂O₃ are printed
as upper bounds ("<"); TeO₂ from observed 2νββ emitters alone is 3.6×10⁻⁵ Bq/kg. Sea-level production rates [FT]:
| Target | Nuclide: rate (atoms or nuclei /(kg·d)) | Source |
|---|---|---|
| Si | ³H 112 ± 24 (n) / 124 ± 25 (all); ⁷Be 8.1 ± 1.9 / 9.4 ± 2.0; ²²Na 43.0 ± 7.2 / 49.6 ± 7.4 | 2007.10584 p.1 |
| Ge | ³H 82 ± 21 (text; 82 ± 12 fit errors, Table p.28); ⁴⁹V 2.8 ± 0.6; ⁵⁵Fe 4.6 ± 0.7; ⁶⁵Zn 106 ± 13 (text; ±10 table); ⁶⁸Ge ≥ 74 (90% C.L.; Table p.28: 202 ± 16 fit, 84 ± 3 under a saturation assumption) | 1607.04560 p.2, p.21, p.28 |
| NaI | ¹²⁶I 283 ± 36; ¹²⁵I 220 ± 10; ¹²⁷ᵐTe 10.2; ¹²⁵ᵐTe 28.2; ¹²³ᵐTe 31.6; ¹²¹ᵐTe 23.5; ¹²¹Te 9.9 ± 3.7; ²²Na 45.1 ± 1.9 | 1411.0106 Table 6 p.15 |
| natTe (TeO₂) | saturation activity, calc. (ACTIVIA): ¹²⁴Sb 182, ¹¹⁰ᵐAg 2.39, ⁶⁰Co 0.81, ²²Na 1.01 µBq/kg of Te | 1411.5947 Table 4 p.10 |
| CaWO₄ | ¹⁷⁹Ta, ¹⁸¹W (EC) observed in data; ³H **inferred** from the ¹⁸¹W activity ('It is hard to be observed experimentally … the observed ¹⁸¹W should be accompanied by a ³H component'); rate GAP | 1908.06755 p.4, p.11 |
| all other survivors | `GAP:cosmo_production` (computation specification: CW7 LE-177) | – |
**EC lines.** L- and M-shell captures give lines at ≈ 1 and 0.1 keV [FT 1607.04560 p.3], but the Ge L-lines are at 1.1–1.3 keV (⁶⁵Zn, ⁶⁸Ge) [p.10], above
the < 1 keV ROI: only M-lines and resolution tails of the L-lines enter the sub-keV rate (v4 `cosmo_EC_lines_subkeV`).
²¹⁰Pb, U/Th: `GAP:Pb210_U_Th` for every non-lead material (process and surface contamination). **For PbS, PbSe, PbTe, ²¹⁰Pb is a bulk material property
(the element carries it) and an S4-type condition (REF-WP8-S-A §8) [E]:** with ²¹⁰Bi in equilibrium, a bulk calorimetric deposit is ≥ 46.5 keV for the 84%
branch (de-excitation absorbed), so the sub-keV rate comes from the 16% ground-state branch (Q = 63.5 keV, f_<1 keV = 0.044) and ²¹⁰Bi (Q = 1162 keV,
f = 9.7×10⁻⁴): 689 /(kg·d·keV) per Bq/kg (allowed shape × non-relativistic Fermi function; decay scheme [UNVERIFIED]; CW7-C35). S4 (≤ 1 /(kg·d·keV)) then
needs **a(²¹⁰Pb) ≲ 1.5×10⁻³ Bq/kg of compound** (1.7–2.3 mBq per kg of Pb). Modern lead is typically far above this and only selected low-²¹⁰Pb lead may meet it
[UNVERIFIED]. v4 rows `S4_cond_Pb210`; the Pb salts are S4-COND until the lead's ²¹⁰Pb is measured.
### 4.5 Channel coverage (REF-WP8-S-A §2; v4 `GAP:channel_inputs`, code/CW7/data/coverage_v4.json)
A ranking that takes one scalar per channel silently drops every material whose input is GAP. Each such material must be listed as "not ranked (GAP)":
| Missing channel input | SURVIVOR | SURVIVOR-COND |
|---|---|---|
| measured E_g (ER edge) | TeO₂, Li₂MoO₄, γ-LiAlO₂ | SrTiO₃, ZrTe₅, Bi₂Se₃, YIG, NiO, MnO, Cr₂O₃, NiPS₃, h-BN, c-BN, PE; Al, Nb (superconductors: the floor is 2Δ_BCS, a separate SC-edge line) |
| ε_eh (threshold in quanta) | Li₂MoO₄, γ-LiAlO₂ | ZrTe₅, Bi₂Se₃, Al, Nb, YIG, NiO, MnO, Cr₂O₃, NiPS₃, h-BN, c-BN, PE |
| c_LA (NR-1ph) | Li₂MoO₄ | ZrTe₅, YIG, MnO (V5 fails), Cr₂O₃, NiPS₃ |
| Z* or a V2-valid ε pair (POL) | Li₂MoO₄, γ-LiAlO₂ | SrTiO₃, ZrTe₅, Bi₂Se₃, Al, Nb, YIG, NiO, MnO, Cr₂O₃, NiPS₃, c-BN, PE |
Li₂MoO₄ thus enters only the Migdal nuclear-factor row (Σ_κZ_ion,κ²/A_cell = 1.05), not "no channel" (REF-WP8-S-A §2 overstated this).

---
## 5. Source disagreements (adjudicated)
- **2008.08560 Table I n_e: CONFIRMED** (both referees, WP8-U-TOP T5). The column is 2 e/atom × N for C, Si, SiC; its Si (16.6 eV) and SiC (22.1 eV, measured) ħω_p
  need 4 e/atom; its diamond 22 eV is the plasma energy of the 2 e/atom column and is suspect (no measured diamond EELS value in the texts read). Use
  `n_e_val_recommended`. Wording: "column = 2 e/atom; C ω_p suspect" (REF-WP8-U-A C1).
- **1910.10716 Table I c_LA (GaN, AlN, ZnO, α-SiO₂, NaCl): SUSPECT, pending measured C_ij.** The size is +69, +59, +178, +113% above the Voigt c_L and −26% for NaCl
  (R13 §0's "37–64%" was wrong). The Christoffel recomputation (WP8-U-TOP §3.2) shows them outside every propagation direction, but both routes are DFT, so
  "source defect" (R13 IF-U9) is withdrawn in favour of "suspect" (REF-WP8-U-B L2). "Anisotropy" is dropped as an explanation (REF-WP8-U-A C2).
- **1910.02091 Δ: half-gap, IF-U5 CLOSED.** Eq. (1.1) "2Δ is the band gap"; the text "band gap … 23.6 meV, which corresponds to Δ = 11.8 meV"; the Table 1 caption word
  "band gaps" is loose. The referees agree on the value (REF-WP8-U-A C4 "refuted"; REF-WP8-U-B L3 "caption vs text confirmed"): Δ_D = 11.75 meV.
- **Diamond ω_T, Ge E_g, 3C T_D**: transcriptions confirmed; adjudication in §4.1; 3C vs 4H/6H T_D: "near-identical moduli (G_V 197.6 vs 190.7 GPa)", cause UNRESOLVED.
- **2008.08560 "c_s" (FLAG 5) FALLS for SiC**: undefined in the paper and above the Voigt c_L, hence not an average phonon speed; kept as `c_avg` only for C and Si,
  where 1901.07569 defines it (REF-WP8-U-B V8, C3).
- **YIG 1905.13744 n_s = 20/a³ = S_cell/Ω**: a net spin density (ħ units), renamed s_spin; the Fe density is 40/a³. "a = 12.56 Å matches the MP GGA+U cell; provenance
  unstated" (inference tagged [E], REF-WP8-U-A C5, -B L4). IF-U7 stays open (experimental a GAP).
- **JARVIS GaAs "ε₀ = 3098"**: the extract holds `dfpt_piezo_max_dielectric_electronic` = 3097.9 (an ε_∞ field) with `dfpt_piezo_max_dielectric` = na
  (REF-WP8-U-B L5 is right; REF-WP8-U-A C3's "appears nowhere" searched the wrong field). The OptB88 gap is 0.085 eV ("near-metallic", above the V2
  cut of 0.05 eV); the run fails V2 through max_ir_mode = 1.77 cm⁻¹.

## 6. Checks (code/CW7/checks.py; the R13/R14 checks U0–U12, T0–T15 are unchanged and rerun by their own scripts)
- CW7-C28: LST on SiC with the A₁ = ∥, E₁ = ⊥ assignment that the A₁/E₁ note implies: residual ≤ 1.2% (R13 U1 paired the components backwards; its "≤ 3%" becomes ≤ 1.2%).
- CW7-C29 (v4): screening keys unique; no [E] screening evidence (44 retagged + 11 dropped = the 55 of VER-CW7 §A); verdict column = final verdict; the 13
  dropped rows recorded verbatim; every new row tagged with a source. (The R16 C29, "2997 v2 rows verbatim in v3", held and is superseded by this check.)
- CW7-C33: JARVIS shear order (C₆₆ = (C₁₁ − C₁₂)/2 at index 3 in all hexagonal/trigonal entries); [001] TA degeneracy ≤ 0.5% in all 13 uniaxial entries after re-indexing.
- CW7-C34: Σ_ν(q̂·ê_ν)² = 1; TeO₂ c_NR1 3.78 (R16 tensor; REF-WP8-S-A 3.77) → 3.76. CW7-C35: ²¹⁰Pb sub-keV rate per Bq/kg and the S4 threshold.
- CW7-C30: rule V2 removes exactly the referees' 13 failed-IR ε₀ rows plus InSb.
- CW7-C17–C19: soft-mode insensitivity (PbTe 2.79–5.57%, PbS 10.31%), rigid-ion regularity, cosmogenic activity with f_<1 keV(³H) = 0.0892 computed (³H Si: 0.169 at 100 d, 11.06 at saturation /(kg·d·keV)).
Recorded corrections to the R13 checks: U2's "≤ 10%" omits 3C-SiC (−17.5%); there is no U11; U6 is a transcription check (τ_life = ℓ/c_s is the paper's
definition); U7 "as 1901.07569 states" → "consistent with 1901.07569"; the A_iso(Si) = 1.65×10⁻⁴⁵ s³ uses V_a from the JARVIS density (1.59×10⁻⁴⁵ with a_exp),
and A_iso(Ge) is high by up to ≈ 37% from the −10% T_D route (REF-WP8-U-B C7).

## 7. Interface flags
| # | Owner | Item | Action |
|---|---|---|---|
| IF-U2′ | WP8-F, WP8-S | V6 provenance ranking; measured E_g(T_op) only for edges | adopt (WP8-F-v3 §5) |
| IF-U3′ | WP8-S | S4 verdicts; cosmogenic columns reducible (exposure history), not verdicts | rank background-limited FOMs with b_bg including them |
| IF-U4′ | WP2 / WP8-F | soft-mode ε₀: SrTiO₃ added; measured values §4.3; m_φ ≈ ω_TO(soft) absorption needs ε(ω, T) data | use §4.3 |
| IF-U7 | WP4 | YIG experimental a (s_spin ∝ a⁻³) | open (GAP) |
| IF-U11 | coordinator | [DB] tag and the V1–V6 rules into CONVENTIONS (§12 amendment) | owed text in CW7 "Owed corrections" |
| IF-U12 | coordinator / NOTATION | renames of §8 | add rows |
| IF-U13 | WP8-S | read v4, not v3; list "not ranked (GAP)" per channel (§4.5); Pb salts S4-COND (²¹⁰Pb); NR-1ph heavy scalar `c_NR1_heavy` | apply |
| IF-U14 | literature agent | measured C_ij (TeO₂, CsI, CaWO₄, hexagonal set); low-T E_g (Ge, GaAs, GaSb: `GAP:E_g_Top`); ²¹⁰Pb of available lead | fetch |

## 8. Symbols introduced/used
**Renamed here (collisions found by the referees):** θ_D → **T_D** (Debye temperature; θ_k is the nuisance family); c₁ → **c₁^{spin}** (source-only, 2210.13516);
τ_ph → **τ_life** (source-only lifetime; t_ph = T/ω_ph); g₂^iso → **g_iso** (g₂(r) is the pair distribution); ħω_p (valence) → **ħω_p^{val}** (ω_p is all-electron);
𝓃_spin → **s_spin ≡ S_cell/Ω**; ω_max (FT, top of the optical range) and **ω_Γ,max^{DFT}** (max Γ mode) kept distinct; CSV `screen_C1–3` → `screen_S1–3`.
**Used:** ρ_T, E_g, ε_∞, ε₀, Z*_κ, Z̄*, ω_T, ω_L, c_ν (c_LA), c̄_LA^{Chr}, Y_mod^{H}, M_κ, A_κ, Z_κ, x_κ, 𝒥_κ, 𝓃_e, 𝓃_e^{val}, ε_eh, F_eh, ε_eh^{br}, E_d, Δ_BCS, Δ_D,
Δ_mag, v_F, E_F, k_TF, g_deg, a_rad, 𝓇^{int}_{<1}, 𝓇^{cos}_{<1}, P_pu, Z*_LST, A_iso, Ω, μ_red, χ (static susceptibility, source symbol in §4.3 only).
**New in v3:** c_NR1 ≡ ⟨Σ_ν(q̂·ê_ν)²/c_ν(q̂)⟩⁻¹ (heavy-mediator NR-1ph speed, WP8-F-v3 (2.3a″)); c_LA,max (largest LA phase speed over directions); a(²¹⁰Pb) (specific activity of ²¹⁰Pb).

## 9. Closing table (one row per referee item; A = REF-WP8-U-A §G, B = REF-WP8-U-B "Required changes" and §C)
| Item | Request | Status | Where |
|---|---|---|---|
| A-G1 | c_LA magnitudes 59–178%; drop "anisotropy"; "near-identical moduli" | APPLIED | §5 |
| A-G2 | close IF-U5 (Δ_D half-gap) | APPLIED (adjudicated with B-L3) | §5; CSV `Delta_D_definition` |
| A-G3 | rewrite IF-U1 from the extract; IR rule on ε₀; SrTiO₃ in IF-U4; InSb ε₀ < ε_∞; SrTiO₃ polymorph | APPLIED | §1.3 V2–V3, §4.3; CW7-C30 |
| A-G4 | ⁷⁶Ge; lower-limit activities as bounds | APPLIED | §4.4; CSV `_ub` rows |
| A-G5 | LU1 source WP2-v3 (4.3)/LST; LU2 ω_p^{val} ESTIMATED; LU3 source; U7 wording | APPLIED (LU3 withdrawn) | §10, §6 |
| A-G6 | YIG density = S_cell/Ω | APPLIED | §5, §8 |
| A-G7 | ε_∞ = ε₀ for Si/Ge/C; τ_ph; screen_S; one ρ ranking; 3C ε_eh estimated | APPLIED | §4.1, §8, V6; CSV |
| A-G8 | SiC-6H E_d 22 (C); [E] screening tags | APPLIED | CSV; §2 |
| A-G9 | GaAs S2 evidence; one FAIL/COND rule | APPLIED (S2 PASS [FT]; COND rule) | §2 |
| A-G10 | IF-U9 wording; IF-U6 factor 1.7 | APPLIED (as a flag) | §5, §4.1 |
| A-C3 | GaAs 3098 "UNRESOLVED" | RESOLVED (field = electronic; B-L5) | §5 |
| B-1 | c_LA magnitudes; "suspect" | APPLIED | §5 |
| B-2 | SrTiO₃ ε₀ GAP + IF-U4; IR gate on ε₀; list | APPLIED (measured value added) | §1.3, §4.3 |
| B-3 | metallic rule = code | APPLIED (V2 uses OptB88 alone) | §1.3 |
| B-4 | SiC c_s relabel; summary speed column | APPLIED | §4.1, §5 |
| B-5 | ⁷⁶Ge | APPLIED | §4.4 |
| B-6 | U1 component assignment | APPLIED (≤ 1.2%) | §6, CW7-C28 |
| B-7 | withdraw LU3; LU1 → L4 ✔ note; LU2 partial sum rule; LU4 Anderson + Voigt sign | APPLIED | §10 |
| B-8 | renames T_D, c₁, τ_ph, g₂, ω_p^{val}; [DB]/"CHECKED" vocabulary | APPLIED; vocabulary owed to CONVENTIONS | §8, §10, IF-U11 |
| B-9 | 𝓃_spin; IF-U7 provenance | APPLIED | §5 |
| B-10 | GaAs S2; INSPIRE IDs; p.21 → p.20 | APPLIED | §2 |
| B-C7 | A_iso(Ge) bias, V_a provenance | APPLIED (recorded) | §6 |
| B-C8, B-C9 | Ge 0.54 eV; diamond ω_T | APPLIED | §4.1 |
| B-V7, B-V15, B-(e)(iii), (e)(v) | 3C T_D outlier; no U11; empty ρ locators; TeO₂ ρ is a DFT proxy | APPLIED (recorded; TeO₂ ρ shown ᵈ) | §6, §4.1 |
| B-V2 | h-BN/c-BN, perovskites excluded on [UNVERIFIED] | APPLIED (h-BN, c-BN → COND; perovskites provisional) | §2, §3 |
| **v3 block** | | | |
| VER-CW7 §A (A-G8 / B-(e)(ii)) | 55 [E] screen_S rows; 13 contradictory keys | APPLIED in v4 (44 retagged, 13 dropped, verdict column; reading rule) | header, §0 row 9, §2; CW7-C29 |
| VER-CW7 §A (B-(e)(v)) | TeO₂ ρ DFT-proxy flag | APPLIED (TeO₂, γ-LiAlO₂) | §4.1; v4 `flag_rho_T_DFT_proxy` |
| VER-CW7 §A minor | "V1–V5" → V1–V6 | APPLIED | §0 row 8 |
| VER-CW7 §A note | CaWO₄ ³H "observed" | CORRECTED ("inferred", 1908.06755 p.4) | §4.4; v4 row |
| VER-CW7 §B8 | PbTe 2.8–5.6%, PbS 10.3%, χ⁻¹ fit parameter, PbS/PbSe "unusable" | APPLIED | §0 row 5, §4.3 |
| VER-CW7 §B9 | Ge L-lines above the ROI | APPLIED | §4.4; v4 `cosmo_EC_lines_subkeV` |
| REF-WP8-S-A §5c | uniaxial C_ij symmetry breaking | RESOLVED (JARVIS shear order; re-indexed; V5′) | §1.3, §4.1′; CW7-C33 |
| REF-WP8-S-A §5b | rank on ⟨Σ(q̂·ê)²/c⟩ | APPLIED (`c_NR1_heavy`) | §4.1′; CW7-C34 |
| REF-WP8-S-A §2 | GAP-input dropouts (Li₂MoO₄) | APPLIED (coverage rows; Li₂MoO₄ in the Migdal row only) | §4.5 |
| REF-WP8-S-A §8 | ²¹⁰Pb condition on the Pb salts | APPLIED (S4-COND, threshold [E]) | §2, §4.4; CW7-C35 |
| REF-WP8-S-A §3 | low-T E_g rows | GAP rows added (Ge, GaAs, GaSb) | v4 `GAP:E_g_Top` |
| REF-WP8-S-B §K | V6 exception for c_LA | DECLARED | §1.3 V6 |

## 10. Proposed LIMITS rows (supersede R13 LU1–LU4 and R14 LT1–LT3 as proposals; the coordinator assigns)
| # | Chain (URF) | Source | Validity | Leading correction | Status |
|---|---|---|---|---|---|
| L4 ✔ (was LU1) | data note on L4: WP2-v3 (4.3) one polar branch → LST ε₀/ε_∞ = (ω_L/ω_T)² (Lyddane–Sachs–Teller 1941 [UNVERIFIED citation]) | 2008.08560 Table I [FT] as test: ≤ 1.2% (CW7-C28) | undamped single mode per axis, any T with renormalised ω | multi-mode product; soft modes (§4.3) | CROSS-CHECKED (data) |
| LU2′ | partial (valence) f-sum: ∫_{val}ωL dω ≈ (π/2)(ω_p^{val})², (ω_p^{val})² = 4πα𝓃_e^{val}/m_e, + free-electron pole for the valence block | 2004.10709 Table I (Si EELS 16.6 ± 0.1 eV) [FT] | sp semiconductors; core/semicore spectrally separated | interband shift of the peak position (not of ω_p); d and core weight | ESTIMATED (one datum) |
| LU4′ | elastic Debye limit, Anderson convention (n_at over all atoms) T_D = (ħ/k_B)v_m(6π²n_at)^{1/3} with Voigt moduli | 2008.08560, 1901.07569 T_D [FT] as tests (C, Si, Ge, 4H/6H ≤ 10%; 3C −17.5%) | isotropic, acoustic; calorimetric T_D is the T → 0 value | Voigt ≥ Hill ≥ Reuss: T_D^{Voigt} is an upper estimate; optical-branch weight | CROSS-CHECKED (data) |
| LT1–LT3 | as WP8-U-TOP (Christoffel c̄_LA; rigid-ion Z*_LST; β + KN sub-keV S4); **LT1 now with the Voigt-ordered tensor (V5′)** | as there | as there | as there (LT1: non-cubic values of R14–R16 superseded by §4.1′) | as there |
| LU5′ (new) | ²¹⁰Pb–²¹⁰Bi sub-keV rate in a bulk lead compound: 16% g.s. β branch + ²¹⁰Bi β, allowed shape × Fermi function → 689 /(kg·d·keV) per Bq/kg | decay scheme [UNVERIFIED] | bulk containment of the 46.5 keV de-excitation; secular equilibrium | first-forbidden shape factors; relativistic Fermi function at Z = 83 | ESTIMATED (CW7-C35) |
LU3 (Tamura isotope scattering) is **withdrawn** until its source is read in full text (REF-WP8-U-B V12).
