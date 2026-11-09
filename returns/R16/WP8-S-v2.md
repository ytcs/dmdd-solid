# R16 / WP8-S-v2: the optimal substrate per interaction channel, with propagated uncertainties (standalone revision of CW7 §12)

Agent REV-WP8-S, brief briefs/R16/REV-WP8-S.md. This return **replaces** returns/R16/CW7.md §12 (LE-159), which stays the record. It absorbs every item of
referees/R16/REF-WP8-S-A.md (V1–V15, required corrections 1–10) and REF-WP8-S-B.md (V1–V15, required corrections 1–8), the ERR-CW7 refinements
(returns/R16/CW7-errata.md §3 (a)–(d), IF-ERR7-1) and the WP8-F-v3 interface IF-F1′ / WP8-U-v3 IF-U13. Closing table: §8.
**Inputs (current only).** returns/R16/WP8-F-v3.md (FOMs, §0, §2.3 (2.3a″), §2.5, §2.7 (2.7′), §4, §5); returns/R16/WP8-U-v3.md and WP8-U-table-v4.csv
(properties, verdicts, S4, `GAP:channel_inputs`; reading rule of WP8-U-v3 §0); code/CW7/data/christoffel_v4.json (the Voigt-ordered tensors of WP8-U-v3 §4.1′);
returns/R16/GAP-EF-v2.md with GAP-EF-v2-errata.md (ε_eh, F_eh: the errata leave the §3 table unchanged, IF-EF3 row), read from code/GAP-EF-v2/data/results.json.
Also read: CW7.md §9–§13, CONVENTIONS (§8, §12, §13 and row 29 as re-issued in CW7-errata §2.1), NOTATION (greps), state/CORRECTIONS.md (no WP8 section),
R13 WP8-F §5.2 (definition of δ_rank); state/CORRECTIONS.md §19.13–§19.16 (owed v4 rows for Al/Nb Δ; renames). Not used: the v3 CSV, WP8-U-v2, WP8-F-v2.
**Deliverables.** This file; code/REV-WP8-S/rank.py (from code/CW7/rank.py, rewritten) → code/REV-WP8-S/data/ranking_v2.json (+ rank_stdout.txt);
code/REV-WP8-S/checks.py, **16/16 PASS in ≈ 2 s**, cited S2-Cn. code/CW7/data/ranking.json is untouched (S2-C15). Nothing committed.
**Numerics.** One Monte Carlo, N_MC = 20 000 draws per input, ≈ 2 s; no other computation. Every number below is **[E]** from the tagged inputs named in its row.
**Literature.** None fetched: no claim here says a paper or database is wrong, and every locator is quoted from WP8-U-v3 / GAP-EF-v2 / WP8-F-v3 full-text
reads. The low-T gaps of GaAs and GaSb stay GAP (IF-U14); they enter as a declared [E] shift (§1.3).
**Status.** CLAIMED (synthesis with propagated bands; awaits R×2, IF-S2-5). The R16 "single missing step = R×2" is withdrawn (REF-B §J): exact gaps in §6.

---
## 0. Results at a glance
| # | Channel (validity) | SURVIVOR leader, P(first) among the 10 | 42-pool leader, P(first) | What drives it |
|---|---|---|---|---|
| 1 | ER low-mass edge, m_floor = 2E_g(T_op)/v_max² | **Ge 0.210 MeV, P = 1.000** (then Si 0.333, GaAs 0.423, each resolved) | PbSe 0.0484 MeV, P = 1.000 (COND; S4-COND ²¹⁰Pb) | measured gaps [FT]; GaAs, GaSb carry an [E] room→0 K shift |
| 2 | ER threshold in quanta, ε_eh(T_op) | **Ge 3.37 eV, P = 1.000** (Si 3.72, GaAs 4.34) | Pb salts one tier: PbTe 0.46, PbSe 0.44, PbS 0.10 | Ge: model-dependent 50 mK fit [FT]; Pb salts GAP-EF [E] outside the validated range |
| 3 | NR-1ph, heavy mediator, 1/c_NR1 (window ≈ 0.03–0.34 MeV) | **TeO₂ / CaWO₄ one tier**: P = 0.621 / 0.357 | CsI 6.39× Si, P = 0.985 | TeO₂: DB tensor + DFT-proxy ρ, S4-COND; CaWO₄, CsI: one suspect DFT c_LA [E wide] |
| 4 | NR-1ph, light mediator | **no ranking**: target-independent above the edge (material factor spread ×1.15) | – | WP8-F-v3 (2.3a″), L-F4 |
| 5 | NR-1ph edge, m_min^{ac}(1 meV) with c_LA,max | **Al₂O₃ 5.16 keV, P = 0.943** | hBN 2.95 keV, P = 0.604 (C, PE, cBN same tier) | DB tensors [E] |
| 6 | POL rate, 𝓘_pol/ρ_T (band-uniform regime) | **LiF 19.0 meV cm³/g, P = 0.995** (NaF, Al₂O₃ one tier) | LiF, P = 0.909 | LiF: Z* route on 1910.10716 DFPT inputs [FT, DFT] |
| 7 | POL reach (mass edge), 2ω_L/v_max² | **GaAs 9.94 keV, P = 1.000** (Al₂O₃ last, 31.1 keV) | CsI 2.85 keV, P = 0.997 | reverses the rate order |
| 8 | Migdal, Σ_κ Z_ion,κ² 𝓠_Mig/A_cell (plasmon pole) | **no reading**: max P(first) 0.315 (NaF) | max 0.499 (NaCl) | 𝓠_Mig needs L(k, ω) (GAP); pole prior [E] |
| 9 | MAG, SC edge, S4 rows | not ranked (all COND; F^{mag} GAP); SC edge Al 0.10–0.17 keV, Nb 0.85–0.92 keV (separate physics); S4 carried into every row | | |
Tiers are heights of the interval order of the 68% intervals (§1.4); "P" is the Monte Carlo probability of ranking first. Every channel lists its
not-ranked materials with the reason (§3); Li₂MoO₄ enters only the Migdal row.

---
## 1. Method
### 1.1 Pool and reading rules
- **Pool** = the v4 `verdict` column, SURVIVOR + SURVIVOR-COND: **42 = 10 S + 32 C**; KTaO₃, InSb (EXCLUDED-RADIO), the REFERENCE and NOT-SCREENED rows are out (S2-C1).
- **Reading rule** (WP8-U-v3 §0): for a (material, property) with several rows, the last row whose note says "supersedes" wins; a `GAP:eps_0_DFT_vetted` row voids the DB ε₀ it names.
- **Parser.** `num1()` accepts one number (optionally "~"); ranges, lists and bounds return None and must be resolved by a declared selection. This fixes the
  R16 `num()` that read "3.6-3.8" as 3.6 (REF-B §D; S2-C8). Every multi-valued input below is selected explicitly, with its locator and temperature.
- **Two pools are reported throughout:** the 10 SURVIVORs and the 42-pool. COND materials carry their S4 and screening conditions in every row.

### 1.2 One scalar per channel (WP8-F-v3 §5.1)
| Channel | Scalar (better) | Formula and validity | Inputs (provenance rule) |
|---|---|---|---|
| ER edge | m_floor (low) | 2E_g(T_op)/v_max², v_max = 794.5 km/s (CONVENTIONS §8) | measured E_g only (V1); T_op ≈ mK (§1.3) |
| ER quanta | ε_eh (low) | asymptotic pair energy; near threshold the weight is P(N_eh\|q, ω) (WP8-F-v3 §2.1(d)) | measured at T_op > measured at room T + shift > GAP-EF-v2 [E] |
| NR-1ph heavy | 1/c_NR1 rel. Si (high) | (2.3a″), F_DM = 1: ∝ 1/c_NR1, c_NR1 ≡ ⟨Σ_ν(q̂·ê_ν)²/c_ν⟩⁻¹, for m_lo ≲ m_χ ≲ q_BZ/(2v_max) | `c_nr1` of christoffel_v4.json (= v4 `c_NR1_heavy`) |
| NR-1ph light | none | target-independent above the edge, ∝ 1/ω_th (2.3a″), L-F4 | residual factor 1 − ω_th/(c q_BZ) only |
| NR edge | m_min^{ac}(1 meV) (low) | ω_th/(2c(v_max − c)), c = c_LA,max (2.3b) | `cLA_max` of christoffel_v4.json |
| POL rate | 𝓘_pol/ρ_T (high) | (2.5a)/(2.5b); equals the rate only for a band-uniform weight, m_χ ≫ 2ω_L,max/v_max² (§2.5 of WP8-F-v3) | one consistent ε model per entry (§2.6) |
| POL reach | 2ω_L/v_max² (low) | lowest polar branch carrying ≥ 5% of 𝓘_pol | the same ε model |
| Migdal | Σ_κ n_κZ_ion,κ²/M_fu × ∫L/ω⁴ (high) | (2.7′) with the plasmon pole ∫L/ω⁴ = (π/2)(ω_p^{val})⁻³ × X_pole, X_pole ∈ [1, 3] log-uniform [E]; Z_ion and n_e^{val} from one split | VALENCE (code/WP8-U) = the n_e^{val} count of every v4 row (S2-C11) |

### 1.3 Provenance-based uncertainties (σ_ln unless stated; the derivation is in rank.py `SIG`)
| Provenance | Width | Basis |
|---|---|---|
| [FT] measured, stated error | as stated (Si ε_eh ±0.01, 4H-SiC ±0.02, sapphire modes < 0.5%) | source |
| [FT] measured, no stated error | E_g 1%; ε_eh by the spread of the [FT] values (Ge 0.05 eV: the 3.37 and 3.32 fits; GaAs 1.5%: 4.2–4.3; GaN 0.075: 9.59 vs 8.9) | needed accuracy (WP8-F-v3 §5.2) or source spread |
| room-T value used at T_op | E_g + δ_TE_g, δ_TE_g ∈ U[0.03, 0.10] eV; ε_eh + k·δ_TE_g, k ∈ U[1.6, 2.8] | Si 1.127 → 1.169 eV and Ge 0.67 → 0.73 eV (77 K) in the table; k from GAP-EF-v2 (1.61) to Klein (2.8) |
| [FT] DFT-in-paper (1910.10716) | Z*, ε_∞ 0.07; ω 0.05; c_LA ("suspect", WP8-U-v3 §5) **0.30** | family, no stated errors [E] |
| [DB] JARVIS, by family | ρ_DFT **0.030** (rms of ln ρ_DFT/ρ_best over the table); C_ij speeds **0.086** (17 `c_LA_check_1910` rows + the like-for-like DB/FT 1.20, 1.08 of WP8-F-v3 §2.3(b)); ε **0.14** (ln 1.15, WP8-F-v3 §2.5); ω 0.05 | derived from the table where both exist |
| [E] GAP-EF-v2 | split-lognormal with the §3 band as ±1σ (the band already holds the full validation range −6.5/+24.6%, so this is wide) | GAP-EF-v2 §3 |
| [E] plasmon pole (Migdal) | X_pole ∈ [1, 3] log-uniform per material | WP8-F-v3 §2.7: the interband weight below ω_p raises ∫L/ω⁴; ≤ (π/2)ω_p²/E_g⁵ |
| halo | v_max σ_ln 0.045 (2–7%), **one common draw** (r = 1) | WP8-F-v3 §4 |
**Correlation.** Material inputs are independent across materials (r_mat = 0). By CONVENTIONS row 29 (CW7-errata §2.1) this is the conservative choice for a
ranking when the elasticities have the same sign, which holds for every pair compared here (one scalar per channel, same functional). The halo band is
common: it scales every edge by the same factor (68%: ×0.92–1.09) and leaves every per-draw order unchanged (S2-C7), so the ranking samples use v_max = 794.5 km/s.
Theory (WP6-type) nuisances enter where WP8-F-v3 §4 sizes them on the scalar: the ε-route sensitivities (1.5× the DB ε width), the two-route spread for POL,
the [E] pole prior for Migdal; the near-edge ×e^{±0.75} ER row acts on the rate near the floor, not on the floor itself, and is not applied to m_floor.

### 1.4 Propagation, probabilities, tiers
- Monte Carlo, 20 000 draws per input (seed 20261101). Per channel and pool: median and 16/84 percentiles of the FOM; **P(first)** = fraction of draws in which the
  material is best; **rank interval** = 16/84 percentiles of its rank; P(A ≻ B) for adjacent pairs.
- Independent route: for lognormal inputs P(A ≻ B) = Φ(Δln/√(σ_A² + σ_B²)) (linearised log-error). It agrees with the MC to < 0.012 on six pairs (S2-C6).
- **Tiers.** A ≻ B iff A's 68% interval lies wholly on the better side of B's. This is an interval order, hence transitive; a material's tier is its height
  (1 + the longest chain of materials above it). Each tier is an antichain: no member resolves any other, so "tied inside a tier" is exact and no tier is anchored
  on its first member (REF-A §1(b); S2-C4). A wide interval can sit in a higher tier than a narrower one with a better median (CaWO₄ in NR rows): that is the rule, not a defect.
- **Rank intervals** of the SURVIVOR tables are printed in §2; the 42-pool leaders: PbSe 1–1 (ER edge), PbTe and PbSe 1–3 (ER quanta), CsI 1–1 (NR heavy),
  h-BN 1–2 (NR edge), LiF 1–1 (POL rate), CsI 1–1 (POL reach), NaCl 1–4 (Migdal); all others in data/ranking_v2.json (`rank_68`).
- **δ_rank.** R13 WP8-F §5.2 defined δ_rank = 0.2 in ln FOM as a fixed resolution [E]. It is **superseded** here as a tiering rule by the interval order; it survives
  only in the R13 needed-accuracy definition (needed accuracy = δ_rank/|∂ln FOM/∂ln x|). REF-A §1(c)'s citation defect is thereby closed.

---
## 2. Channel rows
Tags per value: ᶠ [FT], ᵈ [DB], ᵉ [E]. "†" = S4-COND. The full per-material records (inputs, medians, intervals, P, rank intervals, tiers) are in data/ranking_v2.json.

### 2.1 ER low-mass edge, m_floor = 2E_g(T_op)/v_max² (MeV)
| SURVIVOR | m_floor [68%] | tier | P₁ | rank 68% | E_g input (T) |
|---|---|---|---|---|---|
| Ge | 0.210 [0.208, 0.212] | 1 | 1.000 | 1–1 | 0.73ᶠ eV at 77 K [FT] (1909.05806 p.15, as read by GAP-EF-v2 §2) + 0–15 meV to 0 K |
| Si | 0.333 [0.330, 0.336] | 2 | 0.000 | 2–2 | 1.169ᶠ (0 K) [2004.10709 Table I p.5] |
| GaAs | 0.423 [0.416, 0.430] | 3 | 0.000 | 3–3 | 1.42ᶠ (room T) + [E] shift |
| CaWO₄, Al₂O₃, NaF, LiF | 1.50, 2.52, 3.29, 4.06 | 4–7 | 0 | 4–4, 5–5, 6–6, 7–7 | room-T gaps [1910.10716] + shift |
**42-pool tiers:** t1 PbSe† 0.0484 (P₁ 1.00); t2 PbTe† 0.0541; t3 PbS† 0.0826 (all three low-T gaps ᶠ, COND, ²¹⁰Pb); t4 Ge 0.210; t5 GaSb 0.224; t6 Si 0.333;
t7 GaAs 0.423; t8 SiC-3C 0.699; t9 SiC-6H 0.879; t10 SiC-4H 0.947, ZnO 0.958; t11 GaN 0.977; t12 ZnS 1.08; t13 CaWO₄ 1.50; t14 C 1.56; t15 NaI 1.67;
t16 CsI 1.77, AlN 1.78; t17 MgO 2.25; t18 NaCl 2.51, Al₂O₃ 2.52; t19 SiO₂-q 2.64; t20 NaF 3.29; t21 CaF₂ 3.38; t22 MgF₂ 3.55; t23 LiF 4.06.
**Temperature.** All gaps are at T_op: Si at 0 K [FT]; Ge at 77 K [FT] (the 0.67 eV room-T value of R16 is dropped); the Pb salts, C, GaN, ZnS are the low-T values of 1910.10716 ('*') [FT];
every other gap is a room-T value shifted by δ_TE_g ∈ [0.03, 0.10] eV [E]. **Flag:** Ge ≻ GaSb (P = 0.989) rests on that [E] shift; unshifted (0.72 < 0.73 eV) it reverses.
**SC edge line (not ranked against gapped targets; Cooper-pair breaking, screened Lindhard ER):** m_floor = 2·2Δ/v_max²: Al 0.10 keV (bulk Δ = 0.18ᵉ meV from the
measured T_c, owed v4 row of state/CORRECTIONS §19.13, CW4-errata OC-11(b)) to 0.17 keV (0.3ᶠ meV, the film-like working value of 2109.04473, the IF-U6 factor 1.7);
Nb 0.85–0.92 keV (Δ = 1.50–1.61ᶠ meV, 1805.06359 p.3 secondary, CW4-errata OC-11(c); the v4 row 1.63ᵉ is the DFT-T_c value).
**Not ranked (GAP: no measured E_g, V1):** TeO₂, Li₂MoO₄, γ-LiAlO₂ (S); SrTiO₃, ZrTe₅, Bi₂Se₃, YIG, NiO, MnO, Cr₂O₃, NiPS₃, h-BN, c-BN, PE (C). Bi₂Se₃ (DFT 0.32 eV)
and ZrTe₅ (0.014 eV) would enter the leading tiers on any measured gap of that size.

### 2.2 ER threshold in quanta, ε_eh at T_op (eV)
| SURVIVOR | ε_eh [68%] | tier | P₁ | rank 68% | value used, temperature, source |
|---|---|---|---|---|---|
| Ge | 3.37 [3.32, 3.42] | 1 | 1.000 | 1–1 | 3.37 ± 0.01ᶠ at 50 mK, model-dependent (Luke efficiency free) [1602.08005 p.12]; 3.32ᶠ (p.11) sets the width |
| Si | 3.72 [3.70, 3.74] | 2 | 0.000 | 2–2 | 3.72ᶠ at 5 K and 6–70 K [2004.10709 Table I p.5] (3.749 is 123 K; "3.6-3.8" is not parsed) |
| GaAs | 4.34 [4.26, 4.42] | 3 | 0.000 | 3–3 | 4.2ᶠ at 25 °C [Del Sordo 2009, compilations 4.2–4.3] + room→T_op shift [E] |
| TeO₂† | 9.68 [9.06, 12.2] | 4 | 0.000 | 4–5 | GAP-EF-v2 9.69 (9.06–12.19)ᵉ on the DB TBmBJ gap (0 K DFT proxy); ρ DFT proxy |
| CaWO₄ | 10.9 [10.1, 13.6] | 4 | 0.000 | 4–5 | GAP-EF-v2 10.69 (9.99–13.45)ᵉ, room-T gap + shift (EF-LIT's 29.8 eV is a model value, not used) |
| Al₂O₃, NaF, LiF | 16.7, 20.7, 25.2 | 5, 5, 6 | 0 | 6–7, 7–8, 7–8 | GAP-EF-v2ᵉ, room-T gaps + shift (Al₂O₃'s 27 eV vendor value not used) |
| Li₂MoO₄, γ-LiAlO₂ | not ranked | – | – | – | no measured ε_eh, no GAP-EF input (E_g, ω₀ GAP) |
**42-pool tiers:** t1 PbTe† 1.52 (P₁ 0.46), PbSe† 1.56 (0.44), PbS† 1.92 (0.10) [all GAP-EF-v2ᵉ on low-T gaps, λ_ph ≫ 100: outside the fit domain and the validated
range]; t2 GaSb 2.83ᵉ, Ge 3.37; t3 Si 3.72; t4 GaAs 4.34; t5 SrTiO₃ 5.70ᵉ (DB gap), SiC-6H 6.85ᶠ, SiC-3C 7.04ᶠ, ZnO 7.49ᵉ; t6 ZnS 7.96ᵉ, SiC-4H 7.97ᶠ; t7 TeO₂† 9.68ᵉ,
GaN 9.74ᶠ (EBIC 9.59 + shift), CaWO₄ 10.9ᵉ, NaI 11.1ᵉ; t8 CsI 11.4ᵉ (v2 value 11.21, not the CSV's 11.5), AlN 12.5ᵉ, C 13.1ᶠ; t9 MgO, NaCl, Al₂O₃, SiO₂-q (prediction; the
measured 18.0 eV is amorphous oxide); t10 NaF, CaF₂, MgF₂, LiF.
**Temperature of each value:** measured values at the temperature stated; GAP-EF-v2 predictions refer to the temperature of their E_g input (GAP-EF-v2 §5 (p6)): low T for the
Pb salts, C, GaN, ZnS; 0 K DFT for TeO₂, SrTiO₃; room T for the rest, shifted to T_op as in §1.3. **F_eh** (resolution, not ranked): Si 0.119ᶠ (123 K), Ge 0.14ᶠ (50 mK,
model-dependent), 4H-SiC 0.1ᶠ (conflict with ≤ 0.04, GAP-EF-v2 §2); others GAP-EF-v2ᵉ 0.082–0.168 (in data/ranking_v2.json).
**Not ranked:** Li₂MoO₄, γ-LiAlO₂ (S); ZrTe₅, Bi₂Se₃, Al, Nb, YIG, NiO, MnO, Cr₂O₃, NiPS₃, h-BN, c-BN, PE (C).

### 2.3 NR single phonon, heavy mediator: FOM = c_NR1(Si)/c_NR1 (rate per mass relative to Si)
| SURVIVOR | FOM [68%] | tier | P₁ | rank 68% | c_NR1 (km/s), provenance |
|---|---|---|---|---|---|
| TeO₂† | 2.31 [2.12, 2.52] | 1 | 0.621 | 1–2 | 3.76ᵉ from the Voigt-ordered DB tensor; ρ DFT proxy; S4-COND (¹²³Te) |
| CaWO₄ | 2.07 [1.53, 2.79] | 1 | 0.357 | 1–4 | proxy 4.21 = 1910.10716 c_LA 4.26ᶠ (DFT-in-paper) × the median cubic branch factor 0.99; σ_ln 0.30 because there is no JARVIS tensor (no Christoffel cross-check, no branch-mixing value) |
| Ge, GaAs | 1.82, 1.82 [1.67, 1.98] | 2 | 0.011 each | 2–4, 2–4 | 4.78ᵉ, 4.78ᵉ (P(Ge ≻ GaAs) = 0.503) |
| NaF | 1.46 [1.34, 1.59] | 3 | 0 | 4–5 | 5.97ᵉ |
| LiF, γ-LiAlO₂, Si | 1.17, 1.08, 1.00 | 4 | 0 | 6–7, 6–8, 7–8 | 7.42ᵉ, 8.05ᵉ (ρ proxy), 8.69ᵉ |
| Al₂O₃ | 0.81 [0.74, 0.88] | 5 | 0 | 9–9 | 10.74ᵉ |
| Li₂MoO₄ | not ranked | – | – | – | no elastic tensor (GAP) |
**42-pool tiers:** t1 CsI 6.39 (P₁ 0.985; proxy from the 1910.10716 DFT c_LA 1.379 km/s, "suspect", no JARVIS entry: **[E]-driven**); t2 Bi₂Se₃ 3.04, NaI 2.98, PbTe† 2.80,
PbSe† 2.60, CaWO₄ 2.07; t3 PbS† 2.37, TeO₂† 2.31, GaSb 2.19; t4 Ge, GaAs, NaCl, PE, Nb, ZnS (1.61–1.82); t5 Al, ZnO, NaF, SiO₂-q, NiO, CaF₂, h-BN (1.28–1.48);
t6 GaN, LiF, MgF₂, γ-LiAlO₂, SrTiO₃, Si (1.00–1.18); t7 MgO, AlN, Al₂O₃; t8 SiC (3 polytypes) 0.72; t9 c-BN 0.54, C 0.48.
**Proxy width (R10).** CaWO₄'s tier-1 place does not hinge on the 0.30 width: at the DB-family width with branch mixing (σ_ln 0.10) its 68% interval [1.87, 2.28]
still overlaps TeO₂'s [2.12, 2.52], and P(TeO₂ ≻ CaWO₄) = 0.807 (S2-C12b). For CsI the same proxy sits in the 1910.10716 "suspect" class (WP8-U-v3 §5).
**Validity window [E].** Per material m_lo = ω_th/(c_NR1(v_max − c_NR1)) (q₋ = q_up/2, the q³ integral within 1/8 of its m_χ³ form) to m_hi = q_BZ/(2v_max), with
q_BZ = ħ(6π²/Ω_fu)^{1/3} (an upper estimate; one f.u. per Debye sphere; Si 0.53 MeV here vs 0.43 MeV with the primitive cell). Common window of the ranked set:
**SURVIVORs 0.030–0.34 MeV; 42-pool 0.083–0.27 MeV** (CsI sets the lower end, Bi₂Se₃ the upper). Outside it the heavy-mediator rate is edge-limited (below) or
Umklapp/incoherent (above), and this row does not apply. The scalar is c_NR1, not c̄_LA (TeO₂ 3.76 vs 4.10; h-BN 6.80 vs 15.5): REF-A §5(b).
**Light mediator [D, WP8-F-v3 (2.3a″), L-F4].** Target-independent per mass above the edge; the only material factor is 1 − ω_th/(c q_BZ), which spans 0.870 (CsI) –
0.996 over the 36 materials with a tensor or proxy: ×1.15, inside the uncertainties. **No light-mediator rate ranking**; the material enters through the edge (§2.4).
S2-C12: the (2.3a″) integral with the CONVENTIONS §8 SHM η reproduces the factor ratio (Si/CsI 1.136 vs 1.136) and, for the heavy mediator at 0.25 MeV, CsI/Si 6.39
vs 1/c_NR1 6.37.
**Not ranked:** Li₂MoO₄ (S); ZrTe₅, YIG, MnO (V5 fails), Cr₂O₃, NiPS₃ (C).

### 2.4 NR single-phonon edge, m_min^{ac}(ω_th = 1 meV) with c = c_LA,max (keV)
| SURVIVOR | edge [68%] | tier | P₁ | rank 68% | c_LA,max (km/s) |
|---|---|---|---|---|---|
| Al₂O₃ | 5.16 [4.74, 5.61] | 1 | 0.943 | 1–1 | 11.12ᵉ (P(Al₂O₃ ≻ Si) = 0.951) |
| Si, γ-LiAlO₂, LiF | 6.29, 6.80, 7.38 | 2 | 0.047, 0.008, 0.001 | 2–3, 2–4, 3–4 | 9.09ᵉ, 8.41ᵉ, 7.74ᵉ |
| NaF | 8.82 | 3 | 0 | 5–5 | 6.47ᵉ |
| CaWO₄ | 12.8 [9.5, 17.2] | 3 | 0.002 | 6–9 | proxy (wide) |
| GaAs, Ge, TeO₂† | 11.2, 11.3, 12.4 | 4 | 0 | 6–8, 6–8, 7–9 | 5.06ᵉ, 5.02ᵉ, 4.61ᵉ |
**42-pool tiers:** t1 h-BN 2.95 (P₁ 0.60), C 3.15 (0.24), PE 3.30 (0.11), c-BN 3.45 (0.04); t2 SiC ×3 4.40–4.41, Al₂O₃ 5.16; t3 AlN 5.22, MgO 5.71; t4 Si … LiF; …; t10 CsI 39.4.
h-BN (19.6 km/s in-plane) and PE (17.6 km/s along the chain) reach this edge only for q in the stiff direction (layered/chain tensors, DB): **[E]-driven and
direction-specific.** The edge ordering is opposite to the heavy-mediator rate ordering, as stated in WP8-F-v3 §2.3(b). Not ranked: as §2.3.

### 2.5 POL rate, 𝓘_pol/ρ_T (meV cm³/g), one consistent ε model per entry
| SURVIVOR | 𝓘_pol/ρ_T [68%] | tier | P₁ | rank 68% | route (one model) |
|---|---|---|---|---|---|
| LiF | 19.0 [15.5, 23.3] | 1 | 0.995 | 1–1 | Z* route (2.5b): Z̄* 1.05, ε_∞ 2.02, ω_O,max 77.2 meV, all 1910.10716 DFPTᶠ (DB ε₀ fails V2); rigid-ion LST cross-check with these inputs: ω_T = 31.0 meV [E] (REF-A §6(d): ≈ 32) |
| NaF | 9.69 [8.33, 11.3] | 2 | 0.004 | 2–3 | Z* route 9.95ᶠ and same-run DB triple (ε_∞, ε₀, ω_T) + LST 9.47ᵈ (single branch: exact); geometric mean, half-spread added |
| Al₂O₃ | 9.41 [9.31, 9.51] | 2 | 0.000 | 2–3 | lossless axis-averaged mode sum 9.27 [FT 1807.10291 Table II p.31, Eq. (40)] × damping 1–1.03 |
| GaAs | 0.148 [0.143, 0.154] | 3 | 0 | 4–4 | measured ε pair 10.89/12.9 [FT 1807.10291 Table I] + LST: 0.144–0.153 (WP8-F-v3 §2.5) |
| Si, Ge | not ranked | – | – | – | non-polar (Z* = 0 [D]); quadrupolar coupling, 𝒬_κ GAP |
| TeO₂† | bound only: ≤ 5.88 | – | – | – | DB triple, multi-branch, no ω_T,min; orientation-maximal (V4) |
| CaWO₄, Li₂MoO₄, γ-LiAlO₂ | not ranked | – | – | – | no Z* route (not 1:1) and no V2-valid ε pair |
**42-pool tiers:** t1 LiF 19.0 (P₁ 0.909); t2 NaF 9.69, Al₂O₃ 9.41, CaF₂ 8.79ᵈ (single T1u branch, exact LST), MgO 7.97 (two routes 7.57/8.42), SiO₂-q 5.81 (P₁ 0.073;
interval 1.6–22 from one DB ε pair, ω_O,min to ω_T,max√(ε₀/ε_∞), orientation-maximal), MgF₂ 5.26 (P₁ 0.010; same construction); t3 NaCl 5.75, AlN 5.58; t4 SiC ×3 2.86–3.00
(measured per-axis pairs, 2008.08560); t5 GaN 1.66, NaI 1.65, ZnO 1.35; t6 ZnS 0.98, CsI 0.87; t7 PbS† 0.33; t8 GaAs 0.148, PbSe† 0.138; t9 PbTe† 0.094; t10 GaSb 0.024.
Bound only: TeO₂ ≤ 5.88, h-BN ≤ 7.97.
**What changed from R16.** The mixed-input "upper" route (ε_∞ FT Tr/3 with a DB max-principal ε₀ and a 104 meV DFT ω) is gone: it gave 9.15 for sapphire, below the
lossless mode sum 9.27 (S2-C10; the consistent bound is 9.52). No bound is ranked against central values: SiO₂-q and MgF₂ enter as intervals, TeO₂ and h-BN as bounds only.
GaAs: the measured-pair range is used; the Z* route (0.170) is its cross-check, 6–9% high from the DFT Z̄* (WP8-F-v3 §2.5). **Validity:** 𝓡_pol ∝ 𝓘_pol only for
m_χ ≫ 2ω_L,max/v_max² (≈ 3× the edge or more); within 3× of the edge per-branch K_ν weights change ratios by up to ×13 (WP8-F-v3 §2.5).

### 2.6 POL reach: mass edge 2ω_L/v_max² (keV), lowest branch with ≥ 5% of 𝓘_pol
| SURVIVOR | edge [68%] | tier | P₁ | rank 68% | ω_L used |
|---|---|---|---|---|---|
| GaAs | 9.94 [9.46, 10.4] | 1 | 1.000 | 1–1 | 34.9ᶠ meV (1910.10716; LST with ω_TO 33.3 [UNVERIFIED] gives 36.2) |
| NaF | 14.2 | 2 | 0 | 2–2 | 49.9 meV |
| LiF | 22.0 | 3 | 0 | 3–3 | 77.2ᶠ meV (DFT max; a Γ-point ω_LO would lower it) |
| Al₂O₃ | 31.1 | 4 | 0 | 4–4 | 109.2 meV (e-ray 881.1 cm⁻¹ᶠ: 97% of 𝓘_pol is at 109–112 meV; the lowest LO, 387.6 cm⁻¹, carries 0.08%) |
**42-pool tiers:** t1 CsI 2.85 (P₁ 0.997); t2 MgF₂ 3.45 (ω_O,min, a lower estimate of the lowest LO); t3 PbTe† 3.84, SiO₂-q 3.90 (lower estimate); t4 PbSe† 4.55; t5 NaI 5.70;
… ; t14–t15 AlN, Al₂O₃, SiC ×3 (31–34). The reach order is the reverse of the rate order (soft polar lattices win), as REF-A §6(f) required.

### 2.7 Migdal: Σ_κn_κZ_ion,κ²/M_fu × (ω_p^{val})⁻³ × X_pole, relative to the Si pole value
| SURVIVOR | FOM [68%] | tier | P₁ | rank 68% | ΣZ²/A, ħω_p^{val} (eV) |
|---|---|---|---|---|---|
| NaF | 1.77 [1.22, 2.57] | 1 | 0.315 | 1–4 | 1.19, 21.1 |
| Si | 1.74 [1.19, 2.52] | 1 | 0.296 | 1–5 | 0.57, 16.6 |
| LiF | 1.50 [1.04, 2.19] | 1 | 0.144 | 2–6 | 1.93, 26.1 |
| Li₂MoO₄, γ-LiAlO₂ | 1.46, 1.46 | 1 | 0.120, 0.122 | 2–6, 2–6 | 1.05, 21.6; 1.24, 22.8 (ρ proxy) |
| GaAs | 0.85 | 1 | 0.001 | 5–9 | 0.235, 15.6 |
| Ge, Al₂O₃, TeO₂†, CaWO₄ | 0.81, 0.79, 0.72, 0.66 | 2 | 0 | 5–9, 5–9, 6–10, 7–10 | |
**42-pool:** t1 NaCl 3.08 (P₁ 0.50), PE 2.37 (0.18), NaI 2.22 (0.13), CsI 2.14 (0.11), NaF, Si, NiPS₃, LiF, γ-LiAlO₂; t2 26 materials; t3 ZnO … Nb. All 42 are ranked (ρ known for all).
**Reading of this row.** The nuclear factor alone (LiF 1.93 vs Si 0.57, ×3.4) is cancelled by the pole factor (ω_p ratio cubed, ×3.9): the R16 "Migdal favours light
fluorides" is withdrawn (REF-A §7, REF-B §H). Low valence density (NaCl, PE, iodides) gains through ω_p⁻³; narrow gaps gain through the interband weight, which the
uniform [1, 3] prior does not correlate with E_g. **The row is GAP-driven** (𝓠_Mig needs L(k, ω): `GAP:L_eps2_data`); the f-sum bound (π/2)ω_p²/E_g⁵ is in the JSON.
**Valence convention (NiO).** Z_ion,κ = the WP8-U VALENCE count (Ni 10 = 3d⁸4s², Mn 7, Cr 6, Fe 8, W 6, Pb 4, Ga 3), and n_e^{val} counts the same electrons for every
pool material (S2-C11). With one split the Ni convention moves the NiO FOM by ×0.83 (Ni 2) or ×1.44 (Ni 18), against ×0.29 / ×2.65 for the nuclear factor alone:
the R16 ×25 sensitivity was an artefact of changing Z_ion without L.

### 2.8 MAG, background (S4) rows
- **MAG** (not a ranking): 𝓈_λ⟨|F^{mag}|²⟩/ρ_T with F^{mag} GAP; all candidates COND. YIG: ferrimagnet, gapless acoustic branch **quadratic**, so the FM edge algebra of
  WP8-F-v3 §2.6(b) applies, not (2.3b) (REF-A V10); NiO, MnO, Cr₂O₃ gapped AFM (0.70–5.3 meV), edge 2Δ_mag/v_max²; Cr₂O₃ S4-COND; YIG a_exp GAP.
- **Background (S4)** row: KTaO₃, InSb excluded; S4-COND carried into every channel row above: TeO₂ (¹²³Te), PbTe (EC limit and ²¹⁰Pb), PbS, PbSe (bulk ²¹⁰Pb:
  a(²¹⁰Pb) ≲ 1.5 mBq/kg needed, WP8-U-v3 §4.4), ZrTe₅ (¹²³Te), Cr₂O₃ (⁵⁰Cr). Cosmogenic production [FT] only for Si, Ge, NaI, Te (CaWO₄ ³H inferred, rate GAP).

---
## 3. Not ranked (GAP) per channel (machine list: `not_ranked` in data/ranking_v2.json; S2-C2)
| Channel | SURVIVOR | SURVIVOR-COND | Reason |
|---|---|---|---|
| ER edge | TeO₂, Li₂MoO₄, γ-LiAlO₂ | SrTiO₃, ZrTe₅, Bi₂Se₃, YIG, NiO, MnO, Cr₂O₃, NiPS₃, h-BN, c-BN, PE; Al, Nb → SC line | no measured E_g (V1) |
| ER quanta | Li₂MoO₄, γ-LiAlO₂ | ZrTe₅, Bi₂Se₃, Al, Nb, YIG, NiO, MnO, Cr₂O₃, NiPS₃, h-BN, c-BN, PE | no ε_eh and no GAP-EF input |
| NR heavy, NR edge | Li₂MoO₄ | ZrTe₅, YIG, MnO, Cr₂O₃, NiPS₃ | no elastic tensor (MnO: V5) |
| POL rate, reach | Si, Ge (non-polar); TeO₂ (bound ≤ 5.88); CaWO₄, Li₂MoO₄, γ-LiAlO₂ | C (non-polar); Al, Nb (metals); h-BN (bound ≤ 7.97); SrTiO₃, ZrTe₅, Bi₂Se₃, YIG, NiO, MnO, Cr₂O₃, NiPS₃, c-BN, PE | no Z* route and no V2-valid ε pair |
| Migdal | – | – | all 42 ranked (Li₂MoO₄ only here) |
CaWO₄ and CsI are ranked in the NR rows only through a declared proxy (wide σ); S2-C2 verifies that every one of the 42 is either ranked or listed in every channel.

## 4. Backgrounds
**The tiers ignore backgrounds except through S4.** Every scalar above is a signal (background-free) scalar or an edge. In the background-limited regime the reach
goes as 𝓡/√(b_bgΔE), at the systematics floor as 𝓡/(f_sys b_bgΔE_ROI) (WP8-F-v3 §3), so a leader A keeps its place against B only if b_A/b_B < (𝓡_A/𝓡_B)² (resp. < 𝓡_A/𝓡_B).
b_bg is GAP for every material except Si, Ge, NaI and Te (cosmogenics, WP8-U-v3 §4.4). Background tolerances of the SURVIVOR leaders (medians):
| Channel | Leader vs runner-up | 𝓡 ratio | b ratio tolerated (bg-limited / systematics floor) | Would it reorder? |
|---|---|---|---|---|
| POL rate | LiF vs NaF | 1.96 | 3.9 / 2.0 | only if LiF's b_bg exceeds NaF's by > 3.9; ⁶Li(n,α)³H activation in LiF, Li₂MoO₄, γ-LiAlO₂ is a candidate [UNVERIFIED], GAP |
| ER quanta | Ge vs Si | 1.10 (in 1/ε_eh) | 1.22 / 1.10 | **yes, plausibly**: Ge cosmogenics (³H 82, ⁶⁸Ge ≥ 74, ⁶⁵Zn 106 /(kg·d)) vs Si (³H 124) are within this factor; decided by exposure history |
| NR heavy | TeO₂ vs CaWO₄ | 1.12 | 1.25 / 1.12 | **yes**: TeO₂ ¹²³Te (COND) and cosmogenic Sb/Ag/Co vs CaWO₄ W/Ta EC and inferred ³H, all GAP |
| Migdal | NaF vs Si | 1.02 | 1.04 / 1.02 | no ranking to reorder |
In the 42-pool every channel led by a Pb salt (ER edge, ER quanta; Pb salts high in NR heavy) reorders under background-limited reach unless the lead is low-²¹⁰Pb:
modern lead is typically far above 1.5 mBq/kg [UNVERIFIED], which would push the Pb salts below Ge and Si by orders of magnitude in b_bg. The edges (ER floor, NR edge,
POL reach) are kinematic and do not move with b_bg, but the sensitivity just above them does, by the same tolerance rule.

## 5. Readings (only those that survive the uncertainty analysis; each with its probability)
The table is machine-checked against data/ranking_v2.json (S2-C14). Pool "S" = the 10 SURVIVORs.
| # | Channel | Pool | Material | Quantity | Value | vs | Statement and flags |
|---|---|---|---|---|---|---|---|
| R1 | ER_edge | S | Ge | P_first | 1.000 | – | Ge has the lowest ER floor among survivors (0.210 MeV), on measured gaps [FT] |
| R2 | ER_edge | S | Ge | P_pair | 1.000 | Si | Ge ≻ Si; and Si ≻ GaAs (R3) |
| R3 | ER_edge | S | Si | P_pair | 1.000 | GaAs | GaAs's room-T gap [E shift] cannot close the gap to Si |
| R4 | ER_edge | all | PbSe | P_first | 1.000 | – | the Pb salts hold the three lowest floors (COND; S4-COND ²¹⁰Pb) |
| R5 | ER_edge | all | Ge | P_pair | 0.989 | GaSb | **[E]-driven**: rests on GaSb's room→0 K shift |
| R6 | ER_quanta | S | Ge | P_first | 1.000 | – | Ge needs the fewest eV per pair at T_op; **conditional** on the model-dependent 50 mK fit (3.37); on the 77 K value 2.96 it holds a fortiori |
| R7 | ER_quanta | S | Si | P_pair | 1.000 | GaAs | Si ≻ GaAs at T_op (GaAs a 25 °C value + shift) |
| R8 | ER_quanta | all | PbTe | tier | 1 | – | PbTe, PbSe, PbS are one tier and lead (P₁ 0.46/0.44/0.10): **[E]**, GAP-EF outside its validated range |
| R9 | ER_quanta | all | PbTe | P_pair | 0.514 | PbSe | PbTe vs PbSe unresolved |
| R10 | NR_heavy | S | TeO2 | tier | 1 | – | TeO₂ and CaWO₄ share tier 1 (P₁ 0.621 + 0.357 = 0.978); **[DB]/[E]-driven** (DB tensor, ρ proxy; one DFT c_LA); TeO₂ S4-COND |
| R11 | NR_heavy | S | TeO2 | P_pair | 0.976 | Ge | the soft oxide lead over Ge/GaAs survives the DB width |
| R12 | NR_heavy | S | Ge | P_pair | 0.503 | GaAs | Ge and GaAs are indistinguishable |
| R13 | NR_heavy | all | CsI | P_first | 0.985 | – | **[E]-driven** (single suspect DFT c_LA); window 0.083–0.27 MeV |
| R14 | NR_edge | S | Al2O3 | P_first | 0.943 | – | sapphire has the lowest NR-1ph edge among survivors |
| R15 | NR_edge | S | Al2O3 | P_pair | 0.951 | Si | |
| R16 | NR_edge | all | hBN | P_first | 0.604 | – | h-BN, C, PE, c-BN one tier; h-BN, PE directional (stiff axis only) |
| R17 | POL_rate | S | LiF | P_first | 0.995 | – | LiF leads POL among survivors; Z* route on FT DFT inputs |
| R18 | POL_rate | S | LiF | P_pair | 0.996 | NaF | |
| R19 | POL_rate | S | NaF | P_pair | 0.577 | Al2O3 | NaF and Al₂O₃ tie |
| R20 | POL_rate | all | LiF | P_first | 0.909 | – | the remaining 0.09 is mostly SiO₂-q's wide DB interval (0.073) |
| R21 | POL_edge | S | GaAs | P_first | 1.000 | – | the POL reach (lowest mass) is GaAs's, the reverse of the rate order |
| R22 | POL_edge | all | CsI | P_first | 0.997 | – | |
| R23 | Migdal | S | NaF | P_first | 0.315 | – | **no Migdal reading**: no survivor exceeds P₁ 0.32; GAP-driven |
| R24 | Migdal | all | NaCl | P_first | 0.499 | – | the 42-pool maximum is 0.50 (NaCl); GAP-driven |
| R25 | Migdal | S | Si | P_pair | 0.953 | Ge | Si ≻ Ge under the uniform pole prior; **GAP-driven** (Ge's narrower gap adds interband weight the prior ignores) |
**Statements.** (i) No material leads every channel; among survivors the leaders are Ge (ER floor, ER quanta), {TeO₂, CaWO₄} (heavy-mediator NR-1ph, one tier),
Al₂O₃ (NR edge), LiF (POL rate), GaAs (POL reach); there is no Migdal leader and no light-mediator NR-1ph ranking. (ii) Survivors in the leading tier of two
channels: Ge (ER floor and quanta, both P = 1.000). Al₂O₃ leads one channel (NR edge, P = 0.943) and ties NaF for second in POL. The R16 Reading (2) ("sapphire and LiF
are the only survivors leading two channels") is withdrawn. (iii) Every Pb-salt lead is conditional: ε_eh [E] outside the validated cascade range, SURVIVOR-COND
screening, and S4-COND through bulk ²¹⁰Pb. (iv) The R16 rule "adjacent tiers swap under one DB step, only two apart is robust" is replaced by the probabilities above.

## 6. Exact remaining gaps
1. **L(k, ω) data or computation** for 𝓠_Mig (Migdal) and the ER w_acc⟨1/ω⟩ (`GAP:L_eps2_data`): the Migdal row cannot be ranked without it.
2. **Measured C_ij** for TeO₂, CaWO₄, CsI (IF-U14): the heavy-mediator tier 1 (S) and the 42-pool leader rest on DB or one suspect DFT value.
3. **Low-T gaps of GaAs, GaSb** and the remaining room-T gaps (`GAP:E_g_Top`): they replace the [E] shift (decides Ge vs GaSb).
4. **ω_T,min / mode sums** for the multi-branch polar crystals (TeO₂, h-BN, SiO₂-q, MgF₂, CaWO₄), and measured ε₀ for LiF (V2 GAP).
5. **b_bg** (cosmogenic production for every survivor but Si, Ge, NaI, Te; ²¹⁰Pb of available lead; ⁶Li activation) for the background-limited ranking (§4).
6. **E_g, ε_eh** for TeO₂, Li₂MoO₄, γ-LiAlO₂ (measured); F^{mag} for MAG; R×2 of this return (IF-S2-5).

## 7. Checks (code/REV-WP8-S/checks.py; 16/16 PASS, ≈ 2 s)
| # | Tests |
|---|---|
| S2-C1 | pool = 42 (10 S + 32 C) from the v4 verdict column; EXCLUDED-RADIO out |
| S2-C2 | coverage: each of the 42 ranked or listed with a reason in all 7 channels; Li₂MoO₄ only in Migdal; v4 `GAP:channel_inputs` honoured |
| S2-C3 | S4 flags on TeO₂, PbTe, PbS, PbSe (²¹⁰Pb), ZrTe₅, Cr₂O₃, none on Si, Ge, GaAs, LiF, NaF |
| S2-C4 | tiers recomputed from the JSON intervals: interval order transitive, 93 tiers all antichains, tier = height |
| S2-C5 | ΣP(first) = 1 per channel and pool; the P(first) maximum is in tier 1 |
| S2-C6 | MC P(A ≻ B) = linearised Φ(Δln/√(σ_A² + σ_B²)) to < 0.012 on six pairs (independent route) |
| S2-C7 | the common halo draw leaves every per-draw order unchanged (ER edge, NR edge) |
| S2-C8 | ε_eh ranked at T_op (Si 3.72, Ge 3.37, GaAs > 4.2); ranges are not parsed as their first number |
| S2-C9 | GAP-EF-v2 values (CsI 11.21, bands) used, not the R14 copies in the v4 CSV |
| S2-C10 | sapphire ranked value = lossless mode sum 9.27 ≤ consistent bound 9.52; R16 mixed route 9.15 below it; GaAs range; bound-only entries |
| S2-C11 | Z_ion and n_e^{val} share one split for all 42; NiO ×0.832 (one split) vs ×0.294 (nuclear factor alone) |
| S2-C12 | light mediator: (2.3a″) integral with the CONVENTIONS §8 SHM η: ratio = residual-factor ratio; spread ×1.15 → no rate row; heavy CsI/Si vs 1/c_NR1 |
| S2-C12b | R10 sensitivity: CaWO₄ at the DB-family width (0.10) instead of 0.30 stays in TeO₂'s tier; P(TeO₂ ≻ CaWO₄) = 0.807 |
| S2-C13 | every ordering stated in §0 and §5 (ten assertions) |
| S2-C14 | the 25 rows of §5 equal a fresh run (P to 0.006, tiers exactly) |
| S2-C15 | code/CW7/data/ranking.json unchanged; runtime < 120 s |

## 8. Closing table (one row per referee item; A = REF-WP8-S-A "Required corrections" 1–10 with its verdict rows V1–V15; B = REF-WP8-S-B "Required corrections" 1–8 with V1–V15; then the errata and interface items)
| Item | Request | Resolution | Where |
|---|---|---|---|
| A-1 (V1, V14) | implement or drop "robust = same tier at r_mat = 0"; pairwise ties within the SURVIVOR set; δ_rank citation | implemented: MC bands, P(first), rank intervals at r_mat = 0; tiers = heights of the 68%-interval order (antichains), computed separately for the SURVIVOR set; δ_rank superseded, R13 WP8-F §5.2 cited | §1.3–§1.4; S2-C4–C6 |
| A-2 (V2) | "not ranked (GAP)" list per channel (Li₂MoO₄); Al, Nb SC edge or exclude | §3 list for all 7 channels; Li₂MoO₄ ranked only in Migdal (CW7-errata §3(c)); SC line with the owed Al/Nb Δ values | §2.1, §3; S2-C2 |
| A-3 (V3) | ER edge on E_g(T_op), relabel, Si 0.333 | Si 0.333 (0 K), Ge 0.210 (77 K [FT]), Pb salts/C/GaN/ZnS low T, others room T + [E] shift; label "T_op" | §2.1 |
| A-4 (V5) | ε_eh by V6 and T_op; print what is ranked | T_op selection with source and temperature per value; printed = ranked (S2-C14) | §2.2; S2-C8 |
| A-5 (V6, V7) | NR-1ph one tier TeO₂/CaWO₄/Ge/GaAs; ⟨Σ(q̂·ê)²/c⟩; rebuild uniaxial C_ij; TeO₂ DB provenance and S4 | c_NR1 from the Voigt-ordered christoffel_v4.json; TeO₂, CaWO₄ tier 1, Ge ≡ GaAs tier 2 (P 0.503); TeO₂ flags in row; light mediator unranked (B-1) | §2.3–§2.4; S2-C12, C12b |
| A-6 (V8) | drop "upper"; consistent ε pair; V4 labels; intervals not bounds vs centrals; POL edge row; GaAs 0.170 vs 0.144–0.153 | one ε model per entry; sapphire lossless mode sum 9.27; SiO₂-q, MgF₂ intervals and TeO₂, h-BN bounds, labelled orientation-maximal; reach row; GaAs measured range, Z* 0.170 as cross-check (DFT Z̄* 6–9% high); LiF LST ω_T 31.0 meV | §2.5–§2.6; S2-C10 |
| A-7 (V9) | Migdal out of the readings; 𝓠_Mig ∝ ω_p⁻³ and E_g; NiO convention | pole factor with one valence split, [E] prior, "no reading"; f-sum bound in the JSON; NiO ×0.83/×1.44 with one split | §2.7, §5 R23–R25; S2-C11 |
| A-8 (V11, V12, V13) | withdraw Reading (2); ²¹⁰Pb in Reading (3); CsI radio question | Reading (2) withdrawn; ²¹⁰Pb S4-COND in every Pb-salt row and in §5 (iii); CsI S4 row PASS (intrinsic), cosmogenic Cs/I GAP carried in §4 | §2, §4, §5; S2-C3 |
| A-9 (V14) | background-free statement; theory nuisances onto tiers | §4 statement with tolerances and the channels that reorder; WP8-F-v3 §4 nuisances on the scalars, halo common and order-preserving | §1.3, §4; S2-C7 |
| A-10 (V10) | YIG acoustic branch quadratic | MAG row | §2.8 |
| A-V4, A-V15 | Z/A not a ranking variable; additions to the exact gap | Z/A not ranked; six exact gaps | §1.2, §6 |
| B-1 (V6) | light mediator re-ranked by the edge only; heavy 1/c window ≈ 0.1–0.43 MeV; CsI flagged | no light-mediator rate row (factor spread ×1.15); heavy windows per material and common (S 0.030–0.34, 42-pool 0.083–0.27 MeV); CsI [E]-driven | §2.3; S2-C12 |
| B-2 (V3) | compute bands (r_mat = 0) or withdraw robustness and Reading (4) | bands computed; Reading (4) replaced by probabilities | §1.4, §5 (iv) |
| B-3 (V8) | POL ε route with max ω_L and consistent orientation; C31 as ub ≥ exact; α-SiO₂, MgF₂ as bounds | as A-6; the bound inequality is S2-C10 | §2.5 |
| B-4 (V5) | ε_eh at T_op; `num()` ranges; Ge/Si tie stated; text = script | `num1`; Ge 3.37 vs Si 3.72 resolved under the stated widths (P = 1.000) and flagged model-dependent; text checked against the JSON | §2.2, §5 R6; S2-C8, C14 |
| B-5 (V4) | ER edge E_g(T_op), drop "room-T" | as A-3 | §2.1 |
| B-6 (V9, V12) | Readings (1)/(2) rewritten; Migdal valence convention | §5 statements (i)–(iv); NiO convention stated | §2.7, §5 |
| B-7 (V7, V11, V15) | NR edge: c-BN, h-BN; S4-COND in every row; per-value tags; V6 exception | c-BN, h-BN, PE, C tier 1 in the 42-pool with the directional flag; S4 flags in rows; tags per value; c_NR1 from DB tensors as the WP8-U-v3 §1.3 V6 exception, 1910.10716 c_LA only as a flagged proxy | §2; S2-C3 |
| B-8 (V14) | status: exact gaps instead of "single missing step R×2" | §6 | §6 |
| B-V1, B-V2, B-V10, B-V13 | pool 42; script reproduces text; MAG; Pb-salt conditionality | pool 42 (S2-C1); S2-C14; MAG unchanged; §5 (iii) | §1.1, §2.8, §5 |
| CW7-errata §3 (a)–(d) | Eq. (35) on p.9; lossless 9.27 vs damped 9.40 vs bound 9.52; Li₂MoO₄ in Migdal; TeO₂ c_NR1 3.759 | all used as stated there | §2.3, §2.5, §3 |
| IF-ERR7-1 | v4 table; light NR unranked, heavy `c_NR1_heavy`; POL consistent bound; Migdal × 𝓠_Mig pole; `GAP:channel_inputs`; Pb salts ²¹⁰Pb | all applied | §1–§3 |
| WP8-F-v3 IF-F1′ | §5 scalars with the v3 validity ranges; "rank with δ_rank = 0.2" | applied with the interval-order rule in place of δ_rank | §1.2, §1.4 |
| WP8-U-v3 IF-U13, IF-U3′ | read v4; not-ranked lists; ²¹⁰Pb; c_NR1_heavy; background-limited FOMs with b_bg | applied; the background-limited ranking stays GAP (b_bg), tolerances given | §3, §4 |
| Brief 1–6 | uncertainty propagation; FOM fixes; completeness; readings; checks; closing sections | done | §1–§8, code/REV-WP8-S |

## Symbols introduced/used
| Symbol | Meaning | Status |
|---|---|---|
| P₁ (P(first)), P(A ≻ B) | MC probability that a material ranks first in a channel and pool; that A beats B | new (local) |
| rank_68 | 16–84% interval of a material's rank | new (local) |
| tier | height in the interval order of the 68% FOM intervals (A ≻ B iff the intervals are disjoint with A better) | redefined (R16: anchored at δ_rank) |
| δ_rank | R13 ranking resolution 0.2 in ln FOM (R13 WP8-F §5.2) | superseded as a tiering rule; kept in the needed-accuracy definition |
| m_floor | 2E_g(T_op)/v_max² | as CW7 §12, now at T_op |
| X_pole | true/pole ratio of ∫L/ω⁴ (Migdal), log-uniform [1, 3] [E] | new (local) |
| δ_TE_g | room-T → 0 K gap shift, U[0.03, 0.10] eV [E] | new (local; Δ avoided: Δ_ν, Δ_BCS, Δ_mag) |
| m_lo, m_hi | heavy-mediator NR-1ph validity window | new (local) |
| used | c_NR1, c_LA,max, 𝓘_pol, 𝓠_Mig,κ, ω_p^{val}, Z_ion,κ, m_min^{ac}, ε_eh, F_eh, ρ_T, r_mat, v_max, 𝓡, 𝓩_B, b_bg, f_sys, ΔE_ROI, K^{lm}_ν, 𝓈_λ, Δ_mag, Δ_BCS | NOTATION v4 + WP8-F-v3 / WP8-U-v3 Symbols, read through state/CORRECTIONS §19.16 (K_ν → K^{lm}_ν) |

## Interface flags
| # | Owner | Item | Action |
|---|---|---|---|
| IF-S2-1 | coordinator / SOTA | WP8-S block → "WP8-S-v2 (R16 REV-WP8-S) supersedes CW7 §12: propagated bands, P(first), interval-order tiers" | apply |
| IF-S2-2 | literature agent (IF-U14, IF-ERR7-5) | measured C_ij of TeO₂, CaWO₄, CsI; low-T gaps of GaAs, GaSb; ε_eh of TeO₂, Li₂MoO₄, γ-LiAlO₂; ²¹⁰Pb of available lead; ⁶Li activation | fetch |
| IF-S2-3 | WP8-U | E_g, ω₀ for Li₂MoO₄, γ-LiAlO₂; ω_T,min of the multi-branch polar crystals (JARVIS `min_ir_mode`) | add rows |
| IF-S2-4 | COMP / WP1 | L(k, ω) for the survivors (Migdal 𝓠_Mig, ER w_acc) | library output |
| IF-S2-5 | referees (R17) | R×2 of this return and code/REV-WP8-S | launch |
| IF-S2-6 | NOTATION | tier (interval order), P₁, rank_68; δ_rank status | add rows |

## Proposed LIMITS rows (numbers provisional; the coordinator assigns)
| # | Chain (URF) | Source | Validity | Leading correction | Status |
|---|---|---|---|---|---|
| L-S1 | WP8-F-v3 §5.1 scalars × provenance widths (§1.3) → MC → P(first), rank intervals, interval-order tiers | this return; code/REV-WP8-S | inputs independent across materials (r_mat = 0, same-sign elasticities); one scalar per channel in its validity window | [E] widths of the DB families; correlated method errors (r_mat = 1 variant narrows ratios) | CROSS-CHECKED (MC vs linearised log-error, S2-C6) |
| L-S2 | interval order on 68% intervals → tiers as heights (antichains) | order theory [D] | any family of intervals | choice of 68% (95% merges tiers) | DERIVED (S2-C4) |
| L-S3 | (2.7′) + plasmon pole with one Z_ion/n_e^{val} split → valence-convention shift ×(Z′²/Z²)(n′/n)^{−3/2} on the ion's term | WP8-F-v3 §2.7 | pole-dominated L; small-k Z_ion | interband weight ∝ E_g⁻⁵ at most (f-sum bound) | DERIVED for the scaling (S2-C11); ranking GAP |
