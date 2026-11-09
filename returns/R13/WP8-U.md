# R13 / WP8-U: the pickable universe of substrate materials and its property table

Agent WP8-U, brief briefs/R13/WP8-U.md. Theory and data compilation only; no first-principles numerics were run. returns/R13/WP8-F.md did not exist
when the property list was fixed, so this return uses the brief's default list (§4, IF-U1). CONVENTIONS.md and NOTATION v4 were read. No earlier return
is quoted for a material value. WP5-v3's Si ε_eh/F_eh is cross-referenced in §6, read only. state/CORRECTIONS.md was opened at WP5: the owed items are
renames (§11) and the WP7-E-v3 §5 amendments, and neither touches that value.

**Deliverables.**
- returns/R13/WP8-U-table.csv: machine-readable, long format, one row per (material, property, value). It has 1980 rows, 47 materials and 11 columns:
  `material, label, group, verdict, property, value, unit, tag, source, locator, note`.
- code/WP8-U/:
  - `materials.py`: registry and DB pointers;
  - `screening.py`: per-criterion evidence;
  - `lit_values.py`: every full-text value, with page/table/line;
  - `fetch_db.py`: the network pull, run once;
  - `build_table.py`: builds the CSV offline;
  - `checks.py`: offline; 23 checks labelled U0–U12 (distinct from CONTROLS C1–C8 and the screening criteria S1–S3), **0 FAIL, 16 FLAG**, < 0.1 s;
  - `data/*.json`: the cached database extracts and the arXiv-verification record.
- Literature: literature/papers-WP8-U/, 15 papers fetched; values are quoted from 11 of them. The pdftotext extracts (`*.txt`) are kept because every `p.N l.M` locator indexes them; PDFs and HTML deleted.

**Tags.** The tags follow CONVENTIONS §12 and brief Rules:
- [FT]: quoted from the full text, with page/table/line in `locator`;
- [DB]: a database entry. JARVIS-DFT `JVASP-n` (dft_3d release 9-24-2025, figshare file 64391379); MP OPTIMADE `mp-n`; Alexandria PBE OPTIMADE
  `agm…`; NIST "Atomic Weights and Isotopic Compositions" (ascii2); IAEA LiveChart ground states (ENSDF, extraction 2023-10-18);
- [E]: a closed-form estimate from tagged inputs. The formula is in `locator`/`note` and recomputed in checks.py;
- [ABS]: title/abstract verified on arXiv or INSPIRE. It is used only for *screening evidence*, never for a property value;
- [UNVERIFIED]: from memory. It appears only in screening evidence, never as a property value;
- **GAP**: written explicitly as a CSV row `GAP:<item>` for every non-excluded material.

Missing values are GAP, not estimates, unless a closed-form [E] is defensible.

**DFT proxies are labelled.** Every database gap, dielectric constant and phonon energy is a DFT number (OptB88vdW / TBmBJ / HSE06 / PBE / DFPT). The
CSV names them `*_DFT`, and `note` says "DFT proxy, not the low-T experimental value". A FOM consumer must prefer the [FT] experimental row when both
exist (IF-U2).

---
## 0. Results at a glance
| # | Item | Result |
|---|---|---|
| 1 | Pool | 47 tabulated materials + 7 proposal families recorded as exclusions only (§3) |
| 2 | Screening | **10 SURVIVOR** (all three criteria S1–S3 PASS), **30 SURVIVOR-COND** (no FAIL, ≥ 1 COND), **3 REFERENCE** (a-SiO₂, solid He, which fails C1, and superfluid He), **4 EXCLUDED** in the table (NiPS₃, h-BN, c-BN, polyethylene) + 7 exclusion families (§3) |
| 3 | Fully screened survivors | Si, Ge, GaAs, Al₂O₃, TeO₂, CaWO₄, Li₂MoO₄, γ-LiAlO₂, LiF, NaF (diamond, 4H/6H-SiC, Al and Nb have one COND each) |
| 4 | Property coverage | Si, diamond and SiC are near-complete (FT). Polar binaries have FT ε_∞, Z̄*, ω_max and c_LA from 1910.10716 plus DB ε₀; oxides with many atoms (Li₂MoO₄, CaWO₄) and magnets are thin. ε_eh and F_eh are measured only for Si (both), Ge, diamond and SiC (ε_eh); every other ε_eh/F_eh is GAP (§4.2) |
| 5 | Radiopurity screen (new, [E] from DB) | intrinsic specific activity from primordial constituents: **KTaO₃ 4.6×10³ Bq/kg (⁴⁰K)**, **InSb 121 Bq/kg (¹¹⁵In)**; Pb/Te/Bi/W/Mo/Zn/Ca salts 10⁻⁵–10⁻² Bq/kg; Si, Ge, C, SiC, GaAs, Al₂O₃, LiF, NaI, CsI: none (§4.3) |
| 6 | Source disagreements found | 2008.08560 Table I: n_e is half of 4 e/atom for C, Si and SiC, and ħω_p(diamond) = 22 eV needs ≈ 2 e/atom. 1910.10716 Table I c_LA exceeds the elastic estimate by 37–64 % for GaN, AlN, ZnO and quartz, and NaCl is off by 36 % the other way (the other entries agree within 19 %). Diamond ω_T is 141 vs 148 meV and Ge E_g 0.54 vs 0.67 eV between papers; 3C-SiC θ_D is 1430 K vs 1200 K for 4H/6H with identical moduli (§6) |
| 7 | Cross-route checks | the LST relation is exact to 3 % on the FT SiC data and the DB LST ω_L matches the FT ω_max to ≤ 6 %. θ_D from the DB moduli matches the FT value to ≤ 10 % (C, Si, Ge, 4H, 6H). ρ(a_exp) matches ρ(FT) to 0.2 % and ρ(MP) matches ρ(JARVIS) to ≤ 5 % (36 non-layered). ω_p(Si, 4 e/atom) = 16.6 eV equals EELS. τ = ℓ/c_s holds (§6) |

---
## 1. Sources and method
**Databases.**
1. **JARVIS-DFT** dft_3d (9-24-2025, 93 902 entries), downloaded from figshare to the scratchpad (not the repo); the extract is in `data/jarvis_extract.json`.
   - Polymorph rule: experimental space group, then the entry with the most populated fields. JARVIS `ehull` is not usable as a tiebreak (it reads
     2.93 eV/atom for every SiC polytype).
   - Failed IR runs (`max_ir_mode` < 20 cm⁻¹) are GAP. When a sibling entry with the same mp-ID has a physical mode, it is used (InSb JVASP-17580,
     α-TeO₂ JVASP-57128).
   - DFPT ε are dropped when OptB88vdW is metallic (GaAs ε₀ = 3098) or for metals.
   - Fields used: `density`, `optb88vdw_bandgap`, `mbj_bandgap`, `hse_gap`, `dfpt_piezo_max_dielectric(_electronic)`, `mepsx/y/z`, `max_ir_mode`,
     `modes` (Γ finite-difference), `bulk_modulus_kv`, `shear_modulus_gv`, `avg_elec/hole_mass` (BoltzTraP, 300 K), `magmom_outcar`, `Tc_supercon`.
2. **OPTIMADE.**
   - MP (`optimade.materialsproject.org/v1`): structures and `_mp_stability` (E_hull); the MP REST API was not used.
   - Alexandria PBE: `_alexandria_band_gap(_direct)` and `_alexandria_magnetization`, for the three pool members absent from JARVIS: CsI (agm002216895),
     Li₂MoO₄ (agm003248806) and YIG (agm003265060).
3. **NIST** isotopic compositions and relative atomic masses; **IAEA LiveChart**: J^π, half-lives and their operators (GT/GE = lower limit).

**[E] closed forms (build_table.py).**
- ρ from the experimental lattice constants: Z_fu·M/(N_A V), with V = a³, (√3/2)a²c or a²c.
- Isotropic Voigt sound speeds: c_L = √((B+4G/3)/ρ), c_T = √(G/ρ).
- θ_D (Anderson): θ_D = (ħ/k_B) v_m (6π²n_at)^{1/3}, with v_m⁻³ = (2c_T⁻³ + c_L⁻³)/3.
- Isotope mass variance: g₂^iso = Σ_i x_i(1 − m_i/m̄)².
- Tamura coefficient for monatomic crystals: τ⁻¹ = A_iso ω⁴, A_iso = V_a g₂^iso/(4π v_m³).
- Single-mode LST ω_L = ω_T(ε₀/ε_∞)^{1/2}, for binary cubic crystals only.
- Valence density 𝓃_e^{val} = ρ N_A n_val/M_fu and ħω_p^{val} = ħ(𝓃_e^{val}e²/ε₀^{SI}m_e)^{1/2}. The valence convention is outer s+p for main-group
  elements and outer s+d for open-d metals; d¹⁰ shells are semicore (`materials.VALENCE`).
- Intrinsic specific activity a_rad = Σ ln2/T_{1/2}·N_iso.

**Literature walk.** The proposal walk ran as two INSPIRE `refersto:recid` walks: 1712.06598 (244 citing papers) and 1910.10716 (145). The titles were
filtered for material keywords (85 hits) and merged with the CATALOG-A lattice/electron/spin rows. Full texts were read for the property sources:
- 1910.10716 [Table I p.2, Table III p.14];
- 2008.08560 [Table I p.5, Table IV p.23];
- 1901.07569 [Table I p.2, pp.4–5, 9];
- 2004.10709 [Table I p.5];
- 1905.13744 [pp.3–4];
- 2210.13516 [Table I p.3];
- 1910.02091 [Fig. 3(d) p.11, Tables 1–2 pp.12–13];
- 2109.04473 [p.2];
- 2310.05815 [pp.1–2];
- 2502.01732 [Table I p.4];
- 2201.04219 [p.2].

The brief's "1909.xxxxx polar materials" paper is **1910.10716** (target comparison; its companion framework paper is 1910.08092). "2002.xxxxx SiC" is
**2008.08560**. All 57 arXiv IDs cited in this file, the CSV and screening.py were verified against the arXiv API (`data/arxiv_verified.json`; checks.py U0b). INSPIRE was used only for the citation walk.

---
## 2. Screening (criteria of brief §1)
**Criteria.**
- S1, thermal cycling 300 K ↔ mK: no harmful transition in 0.01–300 K; hygroscopy; demonstrated mK operation.
- S2, ≥ 1 g detector-grade growth.
- S3, an instrumentable surface.

**Evidence.** The evidence strings are quoted in full in `screening.py` and in the CSV rows `screen_C1..C3` (= S1..S3). Each verdict is PASS, COND or FAIL plus an
evidence tag.

**Verdicts.** S = SURVIVOR, C = SURVIVOR-COND, R = REFERENCE, X = EXCLUDED.

| Material | S1 cycling | S2 growth ≥ 1 g | S3 readout | V |
|---|---|---|---|---|
| Si | PASS: HVeV mK [ABS 2407.08085]; CRESST-III Si [ABS 2212.12513] | PASS: kg-scale FZ/Cz | PASS: QET [ABS 2407.08085]; CCD (CATALOG-A E1); KID [ABS 1203.4549] | S |
| Ge | PASS: EDELWEISS NbSi-TES [ABS 2203.03993] | PASS: HPGe | PASS: charge + NbSi/NTD [ABS 2203.03993, 2211.04176] | S |
| diamond | PASS: two CVD crystals at mK [FT 2310.05815 p.1] | **COND**: 0.175 g each [FT 2310.05815 p.1]; typical 4×4×0.5 mm [FT 1901.07569 p.4] | PASS: W-TES, 16.8 eV threshold [FT 2310.05815 p.1] | C |
| 3C-SiC | PASS [E] | **COND**: "not currently at the same level of fabrication scale" [FT 2008.08560 p.21] | COND: "fairly straightforward" metallisation [FT idem] | C |
| 4H-, 6H-SiC | PASS [E] | PASS: "large boules … commercially viable" [FT 2008.08560 p.21]; 6H "most widely available" [FT p.2]; purity below Si/C [FT p.21] | COND: QET designs and transmission [FT Table IV p.23]; no demonstration read | C |
| GaAs | PASS: cryogenic scintillation/calorimeter [ABS 1802.09171, 2507.07119] | PASS: commercial [E] | PASS: scintillating calorimeter [ABS 2507.07119] | S |
| GaN, AlN, ZnO | PASS (wurtzite) [E] | GaN PASS / AlN, ZnO COND [UNVERIFIED] | COND [E] | C |
| InSb, GaSb | PASS [E] | PASS [UNVERIFIED] | COND [E]; InSb radioactive (§4.3) | C |
| Al₂O₃ | PASS: sapphire cryogenic detectors [ABS INSPIRE]; [ABS 2203.15903] | PASS: ν-cleus cubes [ABS 1704.04320] | PASS: TES [ABS 1704.04320] | S |
| α-SiO₂ | COND: α–β transition far above range [UNVERIFIED]; no mK detector found | PASS [UNVERIFIED] | COND [E] | C |
| a-SiO₂ | PASS [E] | PASS [E] | TLS-dominated phonons; amorphous target proposal [ABS 2603.22390] | R |
| MgO, CaF₂, MgF₂ | PASS [E] | PASS [UNVERIFIED] | COND [E] | C |
| TeO₂ | PASS: CUORE/CALDER mK [ABS 1505.01318] | PASS: kg crystals [ABS 1505.01318] | PASS: NTD; KID light detectors [ABS 2104.06850] | S |
| CaWO₄ | PASS: CRESST-III [ABS 1904.00498] | PASS: in-house Cz, radiopure [ABS 1403.5114] | PASS: W-TES [ABS 1904.00498] | S |
| Li₂MoO₄ | PASS: mK scintillating bolometers [ABS 1307.0134, 2011.13243] | PASS: CUPID-Mo crystals [ABS 1909.02994] | PASS: NTD + light detector [ABS 2011.13243] | S |
| γ-LiAlO₂ | PASS: CRESST-III module [ABS 2207.07640] | PASS [ABS idem] | PASS: TES [ABS idem] | S |
| LiF, NaF | PASS: Kamioka bolometers [ABS astro-ph/0204411, astro-ph/0306365] | PASS | PASS (bolometric) | S |
| NaI | **COND**: hygroscopic; cryogenic NaI operated [ABS 1705.11028] | PASS [ABS 1705.11028] | **COND**: TES not on NaI ("remote TES") [ABS 2307.11066] | C |
| CsI, NaCl | COND: hygroscopic [UNVERIFIED] | PASS [UNVERIFIED]/[E] | COND (remote-TES route) [E] | C |
| ZnS | COND: polytypism [E] | COND | COND | C |
| PbTe, PbS, PbSe | PASS: rocksalt; PbTe only Fm-3m in JARVIS [DB JVASP-1103] | COND: Bridgman [UNVERIFIED] | COND [E]; ²⁰⁴Pb + Pb-contamination note | C |
| SrTiO₃ | **COND**: antiferrodistortive cubic→tetragonal transition (≈ 105 K) [UNVERIFIED]; the I4/mcm low-T phase is in JARVIS [DB JVASP-269]; twin domains | PASS [UNVERIFIED] | COND [E] | C |
| KTaO₃ | PASS: cubic quantum paraelectric [UNVERIFIED]; cryogenic resonator [ABS 2105.06781] | PASS [UNVERIFIED] | COND [E]; **radiopurity-disqualifying** ⁴⁰K (§4.3) | C |
| ZrTe₅ | COND: layered; the anomaly is electronic (Lifshitz) [ABS 1701.04737] | **COND**: mm-scale CVT/flux crystals, ≥ 1 g not shown [E] | COND [E] | C |
| Bi₂Se₃ | COND: layered vdW [E] | PASS [UNVERIFIED] | COND [E] | C |
| Al, Nb | Al PASS: QET Al phonon-absorbing fins at mK [FT 1901.07569 p.4 l.304]; Nb PASS [E] | PASS [E] | **COND**: a bulk target read out by its own quasiparticles is proposed only [FT 1504.07237 p.2, 2109.04473 p.2] | C |
| YIG | PASS: spheres at mK, QUAX [ABS 2001.08940] | **COND**: "readily synthesized with high quality" [FT 1905.13744 p.3]; gram scale not stated | **COND**: cavity magnon readout, not TES/charge [ABS 2001.08940] | C |
| NiO, MnO, Cr₂O₃ | COND: magnetostructural distortion below T_N [UNVERIFIED]; MnO R-3m in JARVIS [DB JVASP-22693] | COND [UNVERIFIED] | COND [E] | C |
| NiPS₃ | COND: vdW layered | **FAIL**: flake crystals [E] | COND | X |
| h-BN / c-BN | COND (anisotropy) / PASS | **FAIL**: mm-scale HPHT/flux crystals / sub-mm grits [UNVERIFIED] | COND | X |
| polyethylene | COND: large contraction [E] | PASS | **FAIL**: no QET-grade collection; H-rich + low-T_c TES only proposed [FT 2201.04219 p.2] | X |
| solid ⁴He | **FAIL** as a substrate: pressurised target [ABS 2409.02439] | – | – | R |
| superfluid ⁴He | reference only (HeRALD [ABS 2307.11877]) | – | – | R |

**Reading.**
- Ten materials are fully screened survivors.
- The large SURVIVOR-COND class fails on demonstration, not on physics. No mK detector, no ≥ 1 g detector-grade growth or no sensor was found in the
  sources read. Its COND entries are the experimental priorities, not exclusions.
- Two SURVIVOR-COND materials carry a **non-screening disqualifier** that WP8-F must see: the intrinsic radioactivity of KTaO₃ and InSb (§4.3).

---
## 3. Exclusions with reasons
| Candidate (source) | Failing criterion | Reason |
|---|---|---|
| NiPS₃ (CATALOG-A spin rows) | S2 | vdW flake crystals; no ≥ 1 g detector-grade growth [E] |
| h-BN, c-BN | S2 | bulk single crystals mm-scale (h) / sub-mm (c) [UNVERIFIED] |
| polyethylene / H-rich crystals: ice, acetylene, anthracene (2201.04219 [FT p.2]) | S3 | TES on H-rich crystals proposed only; light-NR role kept as a GAP-heavy row (PE) |
| halide perovskites MAPbI₃, MAPbBr₃, CsPbI₃ (2502.01732 [FT Table I p.4]) | S1 | phase transitions in 100–330 K and moisture instability [UNVERIFIED]; no mK detector |
| Yb₃PbO, BNQ-TTF (1910.02091 [FT]) | S2 | no detector-grade growth; BNQ-TTF is a soft organic ("Organic materials are soft" [FT p.13 l.727]) |
| aromatic organic crystals (1912.02822, 2103.08601 [ABS]) | S3 (S2 COND) | no cryogenic sensor demonstrated |
| graphene, bilayer graphene, carbon nanotubes (1606.08849, 2312.00866, 2604.21969, 2607.15338 [ABS]) | S2 | not a ≥ 1 g bulk substrate |
| chiral-phonon MOFs (2511.20461 [ABS]) | S2/S3 | no detector-grade crystals |
| flat-band correlated topological candidates (2305.19967 [ABS]) | S2 | candidates only |
| solid He (2409.02439 [ABS]) | S1 | pressurised; kept as REFERENCE |

Superfluid ⁴He is a reference row only, per the brief.

---
## 4. The property table
### 4.1 Survivor summary
The table below is an excerpt of the CSV: the best-tag value for each item. ᶠ = [FT], ᵈ = [DB], ᵉ = [E]; GAP is explicit. Units:
- ρ_T in g/cm³;
- E_g in eV (Δ_D or Δ_BCS for Dirac/superconductor);
- ω_max in meV;
- c in km/s: the c_LA row of 1910.10716 when present, else the measured average phonon speed, else the Voigt c_L;
- θ_D in K;
- ħω_p in eV;
- ε_eh in eV;
- a_rad in Bq/kg (— = no primordial radio-isotope among the constituents).

DFT gaps of magnetic oxides without +U are listed as 0* and are not physical.

| key | v | ρ_T | E_g | ε_∞ | ε₀ | Z̄* | ω_max | c | θ_D | ħω_p | ε_eh | a_rad |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Si | S | 2.33ᶠ | 1.11ᶠ | 10.7ᵈ | 11.7ᶠ | 0ᵉ | 62.3ᶠ | 8.51ᶠ | 645ᶠ | 16.6ᶠ | 3.6–3.8ᶠ | — |
| Ge | S | 5.33ᵉ | 0.67ᶠ | 15.2ᵈ | 16ᶠ | 0ᵉ | 34.8ᶠ | 4.83ᶠ | 374ᶠ | 15.6ᵉ | 3.0ᶠ | — |
| C | C | 3.51ᶠ | 5.47ᶠ | 5.32ᵈ | 5.7ᶠ | 0ᵉ | 161ᶠ | 17.9ᶠ | 2220ᶠ | 31.2ᵉ | ~13ᶠ | — |
| SiC-3C | C | 3.2ᶠ | 2.39ᶠ | 6.5ᶠ | 9.7ᶠ | GAP | 120.5ᶠ | 12.6ᶠ | 1430ᶠ | 23.0ᵉ | 5.7–7.7†ᶠ | — |
| SiC-4H | C | 3.2ᶠ | 3.26ᶠ | 6.6/6.8ᶠ | 9.76/10.32ᶠ | GAP | 119.5, 120.0ᶠ | 13.7ᶠ | 1200ᶠ | 23.0ᵉ | 7.7–7.8ᶠ | — |
| SiC-6H | C | 3.2ᶠ | 3.02ᶠ | 6.6/6.7ᶠ | 9.67/10.03ᶠ | GAP | 119.7, 120.3ᶠ | 13.3ᶠ | 1200ᶠ | 23.0ᵉ | 6.7ᶠ | — |
| GaAs | S | 5.32ᵉ | 1.42ᶠ | 10.9ᶠ | GAP | 2.27ᶠ | 34.9ᶠ | 4.71ᶠ | 331ᵉ | 15.6ᵉ | GAP | — |
| GaN | C | 6.09ᵉ | 3.43ᶠ | 6.1ᶠ | 11.3ᵈ | 2.74ᶠ | 88.9ᶠ | 12.5ᶠ‡ | 620ᵉ | 22.0ᵉ | GAP | — |
| AlN | C | 3.26ᵉ | 6.2ᶠ | 4.54ᶠ | 9.55ᵈ | 2.57ᶠ | 109ᶠ | 17.1ᶠ‡ | 939ᵉ | 23.0ᵉ | GAP | — |
| InSb | C | 5.78ᵉ | 0.24ᶠ | 23.7ᶠ | 22.9ᵈ | 2.40ᶠ | 21.5ᶠ | 3.39ᶠ | 191ᵉ | 12.7ᵉ | GAP | **121ᵉ** |
| GaSb | C | 5.55ᵉ | 0.72ᶠ | 21.6ᶠ | GAP | 1.92ᶠ | 27.3ᶠ | 3.96ᶠ | 252ᵉ | 13.9ᵉ | GAP | — |
| Al₂O₃ | S | 3.99ᵉ | 8.8ᶠ | 3.26ᶠ | 12.0ᵈ | 2.97ᶠ | 104ᶠ | 10.5ᶠ | 1018ᵉ | 27.9ᵉ | GAP | — |
| α-SiO₂ | C | 2.65ᵉ | 9.2ᶠ | 2.41ᶠ | 4.88ᵈ | 3.38ᶠ | 149ᶠ | 17.3ᶠ‡ | 572ᵉ | 24.2ᵉ | GAP | — |
| ZnO | C | 5.67ᵉ | 3.3ᶠ | 6.13ᶠ | 11.4ᵈ | 2.17ᶠ | 63.4ᶠ | 12.5ᶠ‡ | 398ᵉ | 21.5ᵉ | GAP | 2.6e-4ᵉ |
| MgO | C | 3.59ᵉ | 7.83ᶠ | 3.38ᶠ | 10.3ᵈ | 1.97ᶠ | 82.6ᶠ | 9.32ᶠ | 944ᵉ | 24.3ᵉ | GAP | — |
| TeO₂ | S | 5.92ᵈ | 4.64ᵈ | 6.45ᵈ | 28.8ᵈ | GAP | 89.0ᵈ | 3.97ᵉ | 324ᵉ | 23.5ᵉ | GAP | 8.1e-3ᵉ |
| CaWO₄ | S | 6.12ᵉ | 5.2ᶠ | 3.84ᶠ | GAP | 2.84 (Ca), 4.67 (W)ᶠ | 106ᶠ | 4.26ᶠ | GAP | 23.8ᵉ | GAP | 4.3e-5ᵉ |
| Li₂MoO₄ | S | GAP | 4.44ᵈ (PBE) | GAP | GAP | GAP | GAP | GAP | GAP | GAP | GAP | 1.1e-3ᵉ |
| γ-LiAlO₂ | S | 2.58ᵈ | 4.96ᵈ | 2.74ᵈ | 6.67ᵈ | GAP | 102ᵈ | 8.10ᵉ | 687ᵉ | 22.8ᵉ | GAP | — |
| LiF | S | 2.65ᵉ | 14.2ᶠ | 2.02ᶠ | 8.82ᵈ | 1.05ᶠ | 77.2ᶠ | 6.51ᶠ | 746ᵉ | 26.1ᵉ | GAP | — |
| NaF | S | 2.80ᵉ | 11.5ᶠ | 1.78ᶠ | 4.79ᵈ | 0.98ᶠ | 49.9ᶠ | 5.34ᶠ | 510ᵉ | 21.1ᵉ | GAP | — |
| NaCl | C | 2.16ᵉ | 8.75ᶠ | 2.44ᶠ | 5.62ᵈ | 1.09ᶠ | 30.6ᶠ | 3.57ᶠ‡ | 335ᵉ | 15.7ᵉ | GAP | — |
| NaI | C | 3.67ᵉ | 5.8ᶠ | 3.27ᶠ | 7.09ᵈ | 1.20ᶠ | 20.0ᶠ | 2.70ᶠ | 175ᵉ | 12.8ᵉ | GAP | — |
| CsI | C | 4.53ᵉ | 6.14ᶠ | 2.70ᶠ | GAP | 1.22ᶠ | 10.0ᶠ | 1.38ᶠ | GAP | 10.8ᵉ | GAP | — |
| CaF₂ | C | 3.18ᵉ | 11.8ᶠ | 2.26ᶠ | 7.41ᵈ | 2.36ᶠ | 55.6ᶠ | 6.45ᶠ | 518ᵉ | 23.3ᵉ | GAP | 1.1e-5ᵉ |
| MgF₂ | C | 3.17ᵉ | 12.4ᶠ | 1.97ᶠ | 5.51ᵈ | 2.00ᶠ | 73.7ᶠ | 7.29ᶠ | 642ᵉ | 26.0ᵉ | GAP | — |
| ZnS | C | 4.07ᵉ | 3.80ᶠ | 5.91ᶠ | 9.39ᵈ | 2.03ᶠ | 41.0ᶠ | 4.59ᶠ | 361ᵉ | 16.6ᵉ | GAP | 2.2e-4ᵉ |
| PbTe | C | 8.27ᵉ | 0.19ᶠ | 26.3ᶠ | 499ᵈ | 5.69ᶠ | 13.5ᶠ | 3.51ᶠ | 200ᵉ | 14.3ᵉ | GAP | 7.8e-3ᵉ |
| PbS | C | 7.60ᵉ | 0.29ᶠ | 15.0ᶠ | 161ᵈ | 4.45ᶠ | 26.9ᶠ | 4.23ᶠ | 244ᵉ | 16.2ᵉ | GAP | 5.5e-3ᵉ |
| PbSe | C | 8.28ᵉ | 0.17ᶠ | 19.5ᶠ | 174ᵈ | 4.86ᶠ | 17.1ᶠ | 3.81ᶠ | 218ᵉ | 15.5ᵉ | GAP | 4.7e-3ᵉ |
| SrTiO₃ | C | 5.01ᵈ | 2.30ᵈ | 6.34ᵈ | 9.96ᵈ | GAP | 65.6ᵈ | 8.17ᵉ | 688ᵉ | 23.3ᵉ | GAP | — |
| KTaO₃ | C | 6.85ᵈ | 3.33ᵈ | 5.43ᵈ | 386ᵈ | GAP | 65.2ᵈ | 7.39ᵉ | 616ᵉ | 22.6ᵉ | GAP | **4.6e3ᵉ** |
| ZrTe₅ | C | 6.09ᶠ | Δ_D 11.75ᶠ | ε 308/21/126ᶠ (DFPT) | – | GAP | GAP | GAP | GAP | 15.3ᵉ | GAP | 8.8e-3ᵉ |
| Bi₂Se₃ | C | 7.34ᵈ | 0.32ᵈ | 22.5ᵈ | 83.1ᵈ | GAP | 25.3ᵈ | 3.01ᵉ | 187ᵉ | 16.1ᵉ | GAP | 2.1e-3ᵉ |
| Al | C | 2.66ᵈ | Δ_BCS 0.3ᶠ | n/a | n/a | n/a | GAP | 5.89ᵉ | 330ᵉ | 15.7ᵉ | n/a | — |
| Nb | C | 8.44ᵈ | Δ_BCS GAP | n/a | n/a | n/a | GAP | 4.97ᵉ | 220ᵉ | 19.4ᵉ | n/a | — |
| YIG | C | 4.95ᵉ | 0* (PBE) | GAP | GAP | GAP | GAP | GAP | GAP | 25.9ᵉ | GAP | — |
| NiO | C | 6.6ᶠ | 0* | GAP | GAP | GAP | 41.2ᵈ | 6.34ᵉ | 444ᵉ | 34.3ᵉ | GAP | — |
| MnO | C | 5.2ᶠ | 0* | GAP | GAP | GAP | GAP | GAP | GAP | 28.1ᵉ | GAP | — |
| Cr₂O₃ | C | 4.9ᶠ | 0.74ᵈ* | GAP | GAP | GAP | GAP | GAP | GAP | 28.3ᵉ | GAP | 5.8e-3ᵉ |

**Notes on the table.**
- † 3C-SiC ε_eh is estimated by 2008.08560 itself ("Eeh values denoted by † have been estimated as described in the text", Table I caption).
- ‡ The c_LA row of 1910.10716 disagrees with the elastic estimate by 36–64 % (U8 FLAG). Use the CSV `c_L_iso` [E] or a measured value.
- The 1910.10716 ω_O, c_LA, Z̄* and ε_∞ values are **DFT/DFPT numbers quoted from a paper** ([FT] provenance, DFT physics). Its E_g values are
  experimental.
- Pairs such as "119.5, 120.0" are the two symmetry components (A₁/E₁) of the hexagonal polytypes.
- ε₀ for PbTe, PbS, PbSe and KTaO₃ is the DFPT harmonic value of a near-soft TO mode. It is strongly T-dependent (incipient ferroelectrics) and must not
  be used without a measured low-T value (IF-U4).
- Dirac row (ZrTe₅): v_F = (1.3×10⁻³, 6.5×10⁻⁴, 1.6×10⁻³) c (exp) and (1.1×10⁻³, 4.5×10⁻⁴, 1.0×10⁻³) c (DFT); g = g_s g_C = 2 [FT 1910.02091 Tables 1–2].
  The Table 1 column "∆" is labelled "band gaps" in the caption, while p.13 l.730 uses ∆ as the half-gap ("band gap of 10 meV (∆ = 5 meV)"). The CSV
  records it as Δ_D (half-gap) with this ambiguity flagged (IF-U5).
- Superconductors:
  - Al: Δ_BCS = 0.3 meV and E_F = 11.7 eV [FT 2109.04473 p.2], as used by that paper (IF-U6). JARVIS T_c (Al 1.60 K, Nb 10.72 K) is a DFT McMillan
    estimate [DB].
  - Nb: Δ_BCS GAP.
- Magnetic rows:
  - YIG [FT 1905.13744 pp.3–4]: 20 Fe³⁺ per cell, S_j = 5/2, S_cell = 10 per Ω = a³/2, a ≃ 12.56 Å, 𝓃_spin = 20/a³ ≃ (4.6 Å)⁻³, J_eff ≃ −0.35 meV. The
    gapless dispersion is ω ≃ k²/(7 MeV); the magnon gap is GAP.
  - MP mp-4704 (GGA+U) gives a_conv = 12.560 Å, the same as the paper. 1905.13744 therefore used a DFT-relaxed cell, so ρ(12.56 Å) = 4.95 g/cm³ is a
    DFT density (IF-U7).
  - NiO, MnO, Cr₂O₃ [FT 2210.13516 Table I]: magnon speed v_θ = 1.3×10⁻⁴, 2.5×10⁻⁵, 3.5×10⁻⁵ c; c₁ = 0.5, 4.2, 0.3 MeV/Å; Λ_UV = 0.6, 0.5, 0.9 keV.
  - Magnon gaps: GAP for all; NiO has a "tiny gap" that the paper neglects.

### 4.2 Coverage matrix (best provenance per required item)
Codes: F = [FT], D = [DB], E = [E], · = **GAP**, – = not applicable.

Item notes:
- "Z,A,iso" = Z, A and the isotopic abundances x_κ (NIST).
- "nuc_spin" = J^π of every natural isotope with J ≠ 0 (IAEA), listed per element in the CSV `nuclear_spin[El]` rows.
- "isotope_scatt" = g₂^iso, and A_iso for monatomic crystals.
- "radio" = primordial isotopes (IAEA) or an [FT] radiopurity note.

| key | ρ | Z,A,iso | E_g | ε_∞ | ε₀ | Z* | ω_T | ω_L | ω_max | c | θ_D | 𝓃_e,ω_p | m* | ε_eh | F_eh | τ_ph | iso | J | radio | spin |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Si | F | D | F | D | F | E | F | F | F | F | F | F | D | F | F | F | E | D | F | – |
| Ge | D | D | F | D | F | E | · | F | F | F | F | E | · | F | · | F | F | D | F | – |
| C | F | D | F | D | F | E | F | F | F | F | F | F | D | F | · | F | F | D | F | – |
| SiC-3C/4H/6H | F | D | F | F | F | · | F | F | F | F | F | F | D | F | · | · | E | D | D | – |
| GaAs | D | D | F | F | · | F | · | · | F | F | E | E | · | · | · | · | E | D | D | – |
| GaN, AlN | D | D | F | F | D | F | D | · | F | F | E | E | D | · | · | · | E | D | D | – |
| InSb | D | D | F | F | D | F | D | E | F | F | E | E | · | · | · | · | E | D | D | – |
| GaSb | D | D | F | F | · | F | · | · | F | F | E | E | · | · | · | · | E | D | D | – |
| Al₂O₃, α-SiO₂ | D | D | F | F | D | F | D | · | F | F | E | E | · | · | · | · | E | D | D | – |
| ZnO | D | D | F | F | D | F | · | · | F | F | E | E | D | · | · | · | E | D | D | – |
| MgO, CaF₂, NaF, PbS, PbSe | D | D | F | F | D | F | D | E | F | F | E | E | D/· | · | · | · | E | D | D | – |
| TeO₂ | D | D | D | D | D | · | D | · | D | E | E | E | · | · | · | · | E | D | D | – |
| CaWO₄ | D | D | F | F | · | F | · | · | F | F | · | E | · | · | · | · | E | D | D | – |
| Li₂MoO₄ | · | D | D | · | · | · | · | · | · | · | · | · | · | · | · | · | E | D | D | – |
| γ-LiAlO₂ | D | D | D | D | D | · | · | · | D | E | E | E | · | · | · | · | E | D | D | – |
| LiF, NaCl, MgF₂ | D | D | F | F | D | F | ·/D | · | F | F | E | E | · | · | · | · | E | D | D | – |
| NaI, ZnS, PbTe | D | D | F | F | D | F | · | · | F | F | E | E | D | · | · | · | E | D | D | – |
| CsI | E | D | F | F | · | F | · | · | F | F | · | E | · | · | · | · | E | D | D | – |
| SrTiO₃, KTaO₃, Bi₂Se₃ | D | D | D | D | D | · | · | · | D | E | E | E | D | · | · | · | E | D | D | – |
| ZrTe₅ | F | D | F | F | F | · | · | · | · | · | · | E | F (v_F) | · | · | · | E | D | D | – |
| Al / Nb | D | D | F / D | – | – | – | – | – | · | E | E | E | F / · | – | – | · | E | D | D | – |
| YIG | E | D | D | · | · | · | · | · | · | · | · | E | · | · | · | · | E | D | D | F |
| NiO / MnO, Cr₂O₃ | F | D | D | · | · | · | · | · | D / · | F | E / · | E | · | · | · | · | E | D | D | F |

The machine-generated, per-material version is `code/WP8-U/data/coverage.json`.

**Largest GAPs, in priority order for WP8-F.**
1. ε_eh and F_eh outside Si, Ge, diamond and SiC.
2. Phonon lifetimes and isotope rates outside C, Si and Ge. g₂^iso is given for every element; A_iso only for monatomic crystals.
3. Born charges for SiC, the perovskites and the magnets. Z* of SiC is not in 2008.08560 Table I.
4. Every property of Li₂MoO₄ except its PBE gap (it is absent from JARVIS).
5. Magnon gaps.
6. Measured low-T ε₀ for the incipient ferroelectrics.

### 4.3 Radiopurity / cosmogenic notes
- **Intrinsic primordial activity** (IAEA half-lives × NIST abundances, [E]; independently recomputed in checks.py U9):
  - KTaO₃: 4.63×10³ Bq/kg from ⁴⁰K. This is a disqualifier for a low-background target unless the K is isotopically depleted.
  - InSb: 121 Bq/kg from ¹¹⁵In (β⁻, 4.41×10¹⁴ y, 95.7 % abundance).
  - Te, W, Mo, Pb, Bi, Zn, Ca, Cr, Se and Zr compounds: ≤ 10⁻² Bq/kg (ββ/α emitters; several half-lives are lower limits, so the values are upper bounds).
- [FT] notes:
  - 1901.07569 Table I lists ¹⁴C, ³²Si and ⁷⁶Ge as the natural radioactive isotopes of C, Si and Ge.
  - ¹⁴C limits a diamond made from ordinary carbon to gram-day exposures; underground methane with ¹⁴C/C ~ 10⁻¹⁸ gives ≈ 10 events/kg-yr below 100 eV
    [FT 1901.07569 p.9].
  - CaWO₄ radiopurity: [ABS 1403.5114].
- Cosmogenic activation (³H in all targets, ⁶⁸Ge/⁶⁵Zn in Ge, and so on) is not in the sources read: **GAP** (IF-U8). ²¹⁰Pb in lead salts depends on the
  source of the lead [UNVERIFIED]; GAP.

---
## 5. Literature-proposed materials (walk result)
**Carried as table rows.**
- 1910.10716: all 24 of its targets;
- 2008.08560: SiC polytypes;
- 1901.07569: diamond;
- 1905.13744: YIG;
- 2210.13516: NiO, MnO, Cr₂O₃;
- 1910.02091 and 1909.09170: ZrTe₅ (Dirac);
- 1504.07237 and 2109.04473: Al;
- 2207.07640: LiAlO₂;
- 1307.0134 and 2011.13243: Li₂MoO₄.

**Recorded as exclusions (§3).** 2502.01732, 2201.04219, 1912.02822, 2103.08601, 1606.08849, 2312.00866, 2604.21969, 2607.15338, 2511.20461, 2305.19967,
2409.02439.

**Not pursued (out of the substrate scope).**
- Superconducting nanowires as the target itself: 1903.05101, 2110.01586, QROCODILE 2412.16279.
- Molecular targets: 1907.07682.
- Levitated sensors: 2008.13197.

---
## 6. Checks (code/WP8-U/checks.py: 23 PASS, 0 FAIL, 16 FLAG)
**Integrity.**
- U0: provenance integrity. Every value row has a tag and a source; every [FT] row has an arXiv ID and a locator; every [DB] row has an ID.
- U0b: all cited arXiv IDs are verified.

**Physics cross-checks.**
- U1: the LST relation on the FT SiC data, within 3 %: 3C 1.492/1.491; 6H 1.465/1.501; 4H 1.479/1.518.
- U1b: DB-route LST ω_L against the FT ω_max for six binary cubic crystals, within 6 %.
- U2: θ_D from the JARVIS moduli against the measured θ_D: C +0.1 %, Si −1.5 %, Ge −10 %, 4H/6H −3 %.
- U3:
  - ρ(a_exp) = ρ(FT) to 0.2 %;
  - ρ(a_exp) and ρ(JARVIS) agree to ≤ 6.2 % (InSb);
  - ρ(MP structure) and ρ(JARVIS) agree to ≤ 4.9 % for 36 non-layered materials.
- U4: abundance sums = 1; NIST masses agree with the A_j of 1910.10716.
- U5: ħω_p(Si, 4 e/atom) = 16.6 eV equals EELS 16.6 ± 0.1 eV [FT 2004.10709].
- U6: τ_ph = ℓ/c_s for C, Si and Ge [FT 1901.07569 Eq. (4)].
- U7: A_iso is ordered Ge > Si > C, as 1901.07569 pp.4–5 states (Si: A_iso = 1.65×10⁻⁴⁵ s³, ν-form 2.56×10⁻⁴² s³).
- U8: the median |c_L^{Voigt}/c_LA − 1| is 8 %.
- U9: specific activities, recomputed.
- U10: the TBmBJ gap against the experimental gap has a median deviation of 12 % (n = 13).
- U12: the screening is complete.

**FLAGs (findings, not failures).**
1. 2008.08560 Table I prints n_e = 1.0, 3.54 and 1.95 ×10²³ cm⁻³ for Si, C and SiC: ratio 0.50 to 4 e/atom × N. Its ħω_p(diamond) = 22 eV implies
   ≈ 2 e/atom; the free-electron value is 31.2 eV. The Si ħω_p = 16.6 eV is right **for 4 e/atom**, so the n_e column is internally inconsistent with
   the ω_p column. A FOM that scales with 𝓃_e must not take that column.
2. 1910.10716 Table I c_LA against the elastic estimate is −41 % (GaN), −37 % (AlN), −64 % (α-SiO₂) and −53 % (ZnO), all with the Voigt value lower,
   and +36 % for NaCl. The other 17 entries agree to ≤ 19 %. The hexagonal (wurtzite/quartz) c_LA entries and NaCl are suspect.
3. Diamond ω_T is 148 meV (2008.08560) vs 141 meV (1901.07569). Ge E_g is 0.54 eV (1901.07569) vs 0.67 eV (1910.10716, room T).
4. 3C-SiC θ_D = 1430 K vs 1200 K for 4H/6H, while the JARVIS moduli and density are the same for all polytypes: a source-definition spread.
5. "c_s" means the *average phonon speed* in 2008.08560/1901.07569 (Si 5.88 km/s) but the LA speed in 1910.10716 (8.51 km/s). The two must not be mixed.
   They are stored as `c_avg` and `c_LA`.
6. MP and JARVIS densities differ for layered/molecular solids (h-BN −15 %, NiPS₃ −6 %, solid He +8 %): the vdW functional, not an error.

**Cross-reference to WP5-v3.** WP5-v3 quotes Si ε_eh = 3.749 eV and F_eh = 0.119 at 123 K from 2004.11499. The same entries appear in 2004.10709
Table I (row [29]), so the two returns are consistent.

---
## Symbols introduced/used
**Used (NOTATION v4).** ρ_T, E_g, E_dir, ε_∞, ε₀, Z*_κ, ω_L, ω_T, c_ν (here c_LA = c_ν, ν = LA), x_κ (isotope abundance), 𝒥_κ (nuclear spin quantum
number, CSV "J"), A_κ, Z_κ, M_κ, 𝓃_e, ω_p, ε_eh, F_eh, E_d, Δ_BCS, Δ_D, v_F, E_F, g_deg, Ω.

**Introduced (WP8-U; proposed rows).**

| Symbol | Meaning | CSV name |
|---|---|---|
| θ_D | Debye temperature (measured, or elastic/Anderson [E]) | theta_D, theta_D_E |
| ω_max | maximal phonon energy of the crystal (FT: top of the DFT optical range; DB: max Γ mode) | omega_O_max, omega_Gamma_max_DFT |
| c̄_s | average phonon speed as defined in 2008.08560/1901.07569 (≠ c_ν) | c_avg |
| c_L^{iso}, c_T^{iso}, v_m | isotropic Voigt longitudinal/transverse speeds; Debye-mean speed | c_L_iso, c_T_iso |
| Z̄* | Tr Z*_+/3 of the cation(s), 1910.10716 | Zstar_bar |
| 𝔔_pol | the 1910.10716 Eq. (27) optical-phonon quality factor (𝔔 per NOTATION for quality factors) | Q_polar |
| 𝓃_e^{val}, ω_p^{val} | valence electron density (stated valence convention) and its free-electron plasma frequency | n_e_val, omega_p_E |
| g₂^iso | isotope mass-variance parameter Σx_i(1 − m_i/m̄)² | g2_iso[El] |
| A_iso | Tamura coefficient, τ⁻¹ = A_iso ω⁴ | A_iso_Tamura |
| a_rad | intrinsic specific activity from primordial constituents | specific_activity_intrinsic |
| 𝓃_spin | ordered-spin number density (1905.13744 "n_s"; renamed, since n_s and 𝓃_s are taken) | spin_density |
| v_θ, c₁, Λ_UV | AFM magnon speed, EFT spin coefficient, EFT cutoff (2210.13516; source names kept) | magnon_speed, c1_spin, Lambda_UV |
| E_hull | energy above the convex hull (MP OPTIMADE) | E_hull_MP |

---
## Interface flags
- **IF-U1 (WP8-F).** WP8-F.md did not exist when the property list was fixed; it appeared only at the end of this work and was read for §5 only.
  - Its §5.2 list is covered for ρ_T, E_g, ε_∞/ε₀, Z*, ω_T/ω_L, c_LA, ω_max, M/A/Z, 𝓃_e, v_F/Δ_BCS/Δ_D/g_deg, 𝓃_spin, E_d, ε_eh/F_eh,
    intrinsic activity and the pass/fail qualifiers.
  - **Not tabulated here (GAP for WP8-U v2):** E_x^b, E_min(q), L(q,ω)/ε₂(ω), the phonon DOS and ω̄_κ, k_TF, ε_bg, λ_{S,j}/J^{ex}/F^{mag}, EPW g,
    tanδ₀/P̄_STM, Y_mod and ∫Δα_th dT, E_st,1/p_surv, y_ion/QF, and cosmogenic production rates.
  - Its §5.3 vetting rule (ii) is stricter than this return's: max IR mode > 50 cm⁻¹ **and** OptB88 gap > 0.3 eV, against IR ≥ 20 cm⁻¹ and not
    metallic in both OptB88 and TBmBJ here. Under WP8-F's rule the InSb and PbS/PbSe/PbTe DFPT ε rows (OptB88 gap 0.0 for InSb) are to be dropped.
    These rows are tagged [DB] with the functional named, and the coordinator should pick one rule.
  - Its rule (iii), select by space group, is the rule used here (§1).
  - If WP8-F adds a property, `build_table.py` only needs a REQ entry and a source; the coverage matrix and the GAP rows regenerate offline.
- **IF-U2 (WP8-F, all FOM users).** Prefer the [FT] experimental rows over the `*_DFT` [DB] rows for gaps, ε and phonon energies. The DFT gaps
  (OptB88vdW) underestimate by up to ≈ 95 % (GaAs 0.085 vs 1.42 eV); TBmBJ is within a 12 % median (U10).
- **IF-U3 (WP8-F, background-limited FOM).** KTaO₃ (⁴⁰K, 4.6 kBq/kg) and InSb (¹¹⁵In, 121 Bq/kg) are intrinsically radioactive. A background-limited
  reach FOM for them is set by this activity, not by detector backgrounds.
- **IF-U4 (WP2/WP8-F).** The ε₀ of PbTe, PbS, PbSe and KTaO₃ comes from DFPT near a soft mode (161–499 for the lead salts, 386 for KTaO₃) and is not a
  usable low-T value without measured data. The LST and screening inputs for these materials are UNRESOLVED.
- **IF-U5 (WP4).** ZrTe₅ Δ: 1910.02091 Table 1 "∆" is ambiguous (caption "band gaps", text uses ∆ as the half-gap). Before any Dirac FOM, WP4 must fix
  whether Δ_D = 11.75 meV or E_g = 11.75 meV.
- **IF-U6 (WP4).** Al Δ_BCS = 0.3 meV is the value 2109.04473 uses. Bulk-Al literature values differ [UNVERIFIED]; a measured bulk Δ_BCS for Al and Nb is
  GAP.
- **IF-U7 (WP4).** The YIG a = 12.56 Å of 1905.13744 equals the MP GGA+U cell (12.560 Å). If the experimental a is smaller [UNVERIFIED], 𝓃_spin ∝ a⁻³
  rises by the cube of the ratio. This needs an [FT] crystallographic value.
- **IF-U8 (WP7-E/WP8-F).** Cosmogenic activation and ²¹⁰Pb are GAP. The LEE proxies via WP7-E stored energy have no material-specific inputs here
  beyond E_d (C, Si, SiC, [FT 2008.08560]).
- **IF-U9 (coordinator).** 2008.08560 Table I n_e column (FLAG 1) and 1910.10716 Table I hexagonal c_LA (FLAG 2) are source defects that downstream
  returns must not inherit.
- **IF-U10 (WP8-R).** Phonon mfp/lifetime [FT 1901.07569] (C 25.6 cm / 19.2 µs, Si 11.4 cm / 19.4 µs, Ge 6.9 cm / 19.5 µs, boundary-normalised mm crystal)
  and the Al/W transmission tables [FT 2008.08560 Table IV] are the inputs WP8-R needs. A_iso (Si 1.65×10⁻⁴⁵ s³) is [E].

## Proposed LIMITS rows (numbers provisional; the coordinator assigns)
| # | Chain (URF) | Source | Validity | Leading correction | Status |
|---|---|---|---|---|---|
| LU1 | ε(ω) with one polar TO mode → ε₀/ε_∞ = (ω_L/ω_T)² (LST), the q → 0 limit of the WP2 Born-charge dielectric | 2008.08560 Table I [FT] (SiC: 3 %) | one polar mode per direction, harmonic, T → 0 | multi-mode product formula; anharmonic soft modes (IF-U4) | CHECKED (U1, U1b) |
| LU2 | f-sum (CONVENTIONS §13 #12) with an all-valence free-electron gas → ω_p² = 4πα𝓃_e^{val}/m_e | 2004.10709 Table I [FT] (Si EELS 16.6 eV) | sp semiconductors, d semicore excluded | d-electron and core contributions; band (interband) shift | CHECKED (U5); 2008.08560 n_e column fails (IF-U9) |
| LU3 | mass-disorder Born scattering of acoustic phonons → τ⁻¹ = (V_a g₂^iso/4π v³) ω⁴ (Tamura) | Tamura PRB 27, 858 (1983) [UNVERIFIED]; the ordering stated in 1901.07569 [FT] | ω ≪ ω_D, isotropic Debye average | dispersion (Tamura 1984/85, 1911.03482 refs. [38, 39]); anisotropic focusing | ESTIMATED (U7) |
| LU4 | elastic Debye limit θ_D = (ħ/k_B)v_m(6π²n_at)^{1/3} | 2008.08560 / 1901.07569 θ_D [FT] | isotropic, acoustic only | optical-branch weight; elastic anisotropy | CHECKED (U2, ≤ 10 %) |
