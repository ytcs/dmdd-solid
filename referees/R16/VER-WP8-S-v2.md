# R16 verification VER-WP8-S-v2 (hostile, isolated): returns/R16/WP8-S-v2.md + code/REV-WP8-S

Brief briefs/R16/VER-WP8-S-v2.md. Read: the return, rank.py, checks.py, data/ranking_v2.json; REF-WP8-S-A/-B (required corrections, verdict rows);
WP8-U-table-v4.csv (TeO₂, CaWO₄, CsI rows); christoffel_v4.json; WP8-U-v3.md (grep "suspect"); CONVENTIONS row 29. Fetched 1910.10716 (Table I, App. A3);
PDF deleted. Reruns: checks.py **16/16 PASS (1.8 s)**, data/ files byte-identical before and after (md5). Own scripts are in the scratchpad only
(correlated-MC rerun, Christoffel solver, η-weighted rate scan, sympy). Nothing committed.

## Verdict table (scope 1–3)
| # | Item (return locus) | Verdict | Reason |
|---|---|---|---|
| 1 | Heavy-mediator NR-1ph validity window, m_lo = ω_th/(c(v_max − c)) "q³ integral within 1/8"; common windows S 0.030–0.34, 42-pool 0.083–0.27 MeV (§0 row 3, §2.3, B-1) | **STANDS WITH CORRECTION** | The 1/8 estimate ignores η. With the return's own η-weighted (2.3a″) integrand (checks.py `rate`), rate/Si equals 1/c_NR1 to 10% only from ≈ 2.2 m_lo: TeO₂ 0.065 (stated 0.030), CaWO₄ 0.057, Ge/GaAs 0.049, CsI **0.17** (stated 0.083). At 0.030 MeV the true TeO₂/Si ratio is 0.83 (FOM 2.31), below Ge (1.14) and CaWO₄ (1.01). Corrected common windows: **S ≈ 0.065–0.34 MeV; 42-pool ≈ 0.17–0.27 MeV** (§A) |
| 2 | Uncertainty model: r_mat = 0 "the conservative choice", tiers "exact" (§1.3, §1.4, L-S1) | **STANDS WITH CORRECTION** | It is conservative only for *resolved* statements. Tiers are built from marginal 68% intervals, so they cannot see correlation. Under r > 0, "one tier" and "no reading" statements become resolved: Migdal 42-pool NaCl P₁ 0.49 → 0.94, h-BN NR edge 0.60 → 0.96. CONVENTIONS row 29 puts same-method nuisances (DB C_ij, GAP-EF, X_pole) at r_mat = 1, so the r = 1 variant must be printed next to them (§B) |
| 3 | Statement (ii) "Survivors in the leading tier of two channels: Ge" (§5) | **STANDS WITH CORRECTION** (FALLS as literally written) | From the JSON, SURVIVOR Migdal tier 1 = {NaF, Si, LiF, Li₂MoO₄, γ-LiAlO₂, GaAs}. So LiF (POL rate t1 + Migdal t1) and GaAs (POL reach t1 + Migdal t1) are also in two leading tiers. Add "excluding the Migdal row (no reading)" |
| 4 | L-S3: valence-convention shift "×(Z′²/Z²)(n′/n)^{−3/2} on the ion's term" | **STANDS WITH CORRECTION** | sympy: F′/F = [(Z′²+ΣZ_o²)/(Z²+ΣZ_o²)]·(n′/n)^{−3/2}. The density factor multiplies the **whole** FOM. Read as written (on the ion's term only), NiO Ni 10→2 gives ×0.35, not the ×0.832 that the code (correctly) computes. Ni 18 gives ×1.441 ✓ |
| 5 | L-S2 interval-order tiers, DERIVED | STANDS | Transitivity (a_lo > b_hi ≥ b_lo > c_hi) and height layers are antichains. Code heights are valid because a beater always has the larger median. Text says **93** tiers; S2-C4 counts **111** (7 ch × 2 pools, from the JSON): fix the number |
| 6 | Light mediator [D, (2.3a″)]: rate/mass ∝ (1/ω_th)(1 − ω_th/(c q_up)); no ranking; spread ×1.15 | STANDS | sympy: (1/c)∫_{ω_th/c}^{q_u} q⁻² dq = (1/ω_th)(1 − ω_th/(c q_u)) exactly. Spread 1.146 reproduced. Caveat: CsI sets the 0.870 end on the suspect c_LA (row 9) |
| 7 | Edges: ER 2E_g/v², POL 2ω_L/v², NR ω_th/(2c(v−c)), SC 2·2Δ/v² | STANDS | sympy: max_q(qv − q²/2m) = mv²/2; NR edge solved exactly. Al 0.10/0.17 keV, Nb 0.85/0.92 keV, Ge 0.210 MeV recomputed |
| 8 | POL Z* route = single-branch (π/2)Dω_L/ρ with rigid-ion LST; LiF 19.0; sapphire lossless mode sum 9.27, 97% weight at 109–112 meV, lowest LO 0.08% | STANDS WITH CORRECTION (width only) | sympy: the identity is exact. LiF 18.99 recomputed by hand. Mode-sum partial fractions satisfy ΣD_j = 1/ε∞ − 1/ε₀ per axis; branch weights 0.327 + 0.638 = 96.6%, min 0.078% ✓. The sapphire σ (±1%, [9.31, 9.51]) is narrower than the sensitivity to its single ε∞ = 3.2 for both axes: ε∞ = 3.1 gives 9.57 (+3.2%). Widen to ≥ 3% (no reading changes: NaF–Al₂O₃ already tie) |
| 9 | R13: CsI leads the 42-pool heavy NR, P₁ 0.985, "[E]-driven", c_LA "in the 1910.10716 'suspect' class (WP8-U-v3 §5)" | **STANDS WITH CORRECTION** | The transcription is right: fetched 1910.10716 Table I gives c_s^LA = 0.46×10⁻⁵ c = 1.379 km/s, a sphere average of ω_LA/q (App. A3). The citation is wrong: WP8-U-v3 §5 rules **GaN, AlN, ZnO, α-SiO₂, NaCl** suspect, **not CsI** (or CaWO₄), so the 0.30 width is this return's own [E] choice and must be declared as such. Plausibility [UNVERIFIED, not from fetched text]: c_L ≥ √(B/ρ), and CsI's commonly quoted B ≈ 12–13 GPa gives ≥ 1.67 km/s, 1.2σ above the proxy. A tensor-based c ≈ 2.3 km/s would give FOM ≈ 3.8 and a tier shared with Bi₂Se₃/NaI. Phrase R13 as "leader on a single unvalidated DFT c_LA". The P₁ = 0.985 does not measure robustness |
| 10 | R10: TeO₂/CaWO₄ tier 1 (S), P₁ 0.621/0.357; c_NR1(TeO₂) = 3.759; S2-C12b | STANDS (conditional, as flagged) | An independent Christoffel solve on the v4 Voigt tensor (ρ 5.917) gives c_NR1 = 3.763, c̄_LA 4.100, c_LA,max 4.606 ✓ (Si 8.69 on the DB tensor). Risk [UNVERIFIED, memory values]: a CaWO₄ tensor of the commonly quoted size (C11 ≈ 144, C33 ≈ 126 GPa) gives c_NR1 ≈ 4.6 → FOM ≈ 1.9, the Ge/GaAs level. So CaWO₄'s tier-1 place may be a proxy artefact. Gap 2 already names it; R10 should say "CaWO₄ on a 1910.10716 DFT c_LA × cubic branch factor applied to a tetragonal (I4₁/a) crystal" |
| 11 | ER readings R1–R7; Ge ε_eh 3.37 (model-dependent), "a fortiori" on 2.96 | STANDS WITH CORRECTION (text) | Numbers reproduce (S2-C8, C14). Text §1.3 says Si ε_eh "±0.01 as stated", but the code uses σ = 0.02 eV (`0.01/3.72*2`). State the doubling. R5 is correctly flagged [E] |
| 12 | §4 tolerance row ER quanta: "Ge cosmogenics (³H 82, ⁶⁸Ge ≥ 74, ⁶⁵Zn 106) vs Si (³H 124) are within this factor" | STANDS WITH CORRECTION | The ratios 1.104 → 1.22/1.10 are right. The reason is wrong: Ge's listed sum (≥ 262) is ≈ 2.1× Si's 124, which is **above** the 1.22 tolerance. The verdict "would reorder" is therefore more likely, not "within the factor". Restate it as an ROI-dependent comparison |
| 13 | Readings R8, R14–R25; §2 tables; S4 carry | STANDS | 25 rows match a fresh run (S2-C14). S4/²¹⁰Pb flags are on every COND row (S2-C3). Every [E]/GAP-driven reading is flagged, except R13's citation (row 9) |
| — | Scope 2 (paper wrong/misprint) | none claimed | The return makes no such claim. Fetched 1910.10716 confirms the CsI 0.46, CaWO₄ 1.42 (×10⁻⁵ c), CsI E_g 6.14, LiF Z̄* 1.05/ε∞ 2.02/ω_O 33.5–77.2 transcriptions |

## A. Heavy-mediator window (row 1)
Method: checks.py `rate(c, q_BZ, m, heavy)` (CONVENTIONS §8 SHM η, v_min = c + q/2m, q from ω_th/c to min(q_BZ, 2m(v−c))). I scanned m on 60 log points
in 0.01–0.6 MeV, ratio to Si, against 1/c_NR1. First mass at which |ratio/(1/c) − 1| < 0.1:
| material | stated m_lo | 10% agreement | m_hi (stated) |
|---|---|---|---|
| CsI | 0.083 | 0.172 | 0.318 |
| NaI, Bi₂Se₃ | 0.039, 0.040 | 0.086, 0.086 | 0.356, 0.274 |
| PbTe, PbSe, PbS | 0.037, 0.034, 0.031 | 0.080, 0.075, 0.065 | 0.36–0.39 |
| TeO₂, CaWO₄ | 0.030, 0.027 | 0.065, 0.057 | 0.409, 0.339 |
| Ge, GaAs | 0.024 | 0.049 | 0.513, 0.407 |
| Al₂O₃, LiF | 0.011, 0.015 | 0.025 | 0.416, 0.573 |
Sample: TeO₂/Si = 0.092, 0.83, 1.84, 2.31, 2.39 at m = 0.02, 0.03, 0.05, 0.1, 0.25 MeV. CsI/Si = 0.05, 3.37, 6.39 at 0.05, 0.1, 0.25 MeV.
Mechanism: η(v_min) falls steeply toward v_max, so the q-integrand is weighted to low q. Cutting at q_lo = q_up/2 then removes far more than the flat-η 1/8.
REF-B's lower end (≈ 0.1 MeV) was nearer than the return's. **B-1 is only partly resolved.**
Upper end: q_BZ = ħ(6π²/Ω_fu)^{1/3} uses one f.u. per Debye sphere. It is an upper estimate (declared). For the materials that set it, it is high by Z^{1/3}
(TeO₂ Z = 4 f.u. per primitive cell, ×1.59; CaWO₄ Z = 2, ×1.26), so the S upper end can be as low as ≈ 0.27 MeV. Print both numbers.
Required text: §0 row 3 "window ≈ 0.07–0.34 MeV (upper end an f.u.-Debye upper estimate; ≈ 0.27 MeV with primitive cells)". §2.3: replace the m_lo definition
by the η-weighted criterion, or by m_lo ≈ 2.2 ω_th/(c(v_max − c)) [E, 10%], and give the 42-pool window as ≈ 0.17–0.27 MeV.

## B. Correlated-error alternative (scope 0, row 2)
Rerun: rank.run() with its Z() and U() replaced by draws that share one common component across **all** inputs:
z = √r·z_common + √(1−r)·z_own, and U through Φ of such a z. This is a global common-mode variant, cruder than family-wise r_mat = 1.
| quantity | r = 0 | r = 0.5 | r = 0.9 |
|---|---|---|---|
| ER edge / quanta S leader Ge P₁ | 1.000 / 1.000 | 1.000 / 1.000 | 1.000 / 1.000 |
| NR heavy S: TeO₂ / CaWO₄ P₁; P(TeO₂ ≻ CaWO₄) | 0.622 / 0.354; 0.64 | 0.664 / 0.333; 0.67 | 0.698 / 0.302; 0.70 |
| NR heavy all: CsI P₁ | 0.986 | 0.996 | 0.999 |
| NR edge S: Al₂O₃ P₁ / all: h-BN P₁ | 0.945 / 0.609 | 0.990 / 0.729 | 1.000 / 0.955 |
| POL rate S / all: LiF P₁; P(NaF ≻ Al₂O₃) | 0.996 / 0.908; 0.579 | 1.000 / 0.932; 0.585 | 1.000 / 0.946; 0.585 |
| Migdal S max P₁ (NaF) / all (NaCl); P(Si ≻ Ge) | 0.321 / 0.494; 0.953 | 0.375 / 0.650; 0.991 | 0.528 / 0.936; 1.000 |
| PbTe ≻ PbSe (ER quanta) | 0.512 | 0.515 | 0.529 |
Findings.
(i) Every resolved reading (P ≥ 0.94) survives and sharpens. "Conservative for resolved statements" is correct.
(ii) The tiers are identical at every r. They are computed from marginal intervals, so they are correlation-blind. "Tied inside a tier is exact" is a
statement of order theory, not of statistics.
(iii) The "no reading" and "one tier" conclusions are r_mat = 0 artefacts in two places. Migdal (42-pool NaCl → 0.94) and the 42-pool NR edge (h-BN → 0.96)
resolve when the method nuisance (X_pole; DB C_ij) is common, which is CONVENTIONS row 29's own default for same-method nuisances.
Required: (a) §1.3 replace "the conservative choice" by "conservative for resolved orderings; ties and 'no reading' are reported at r_mat = 0 and r_mat = 1".
(b) Add an r_mat = 1 (per family) column for P₁ in §0. (c) §2.7 / R23–R24: the Migdal "no reading" rests on X_pole being independent *and* uncorrelated
with E_g. With a common X_pole, NaCl leads. With E_g-correlated weight, narrow-gap materials rise. Either way the row is prior-driven, which is already said
("GAP-driven"); say also that it is r_mat-driven.
(d) L-S1 "leading correction": "r_mat = 1 variant narrows ratios" should add "and resolves r = 0 ties (Migdal, NR edge 42-pool)".

## C. Closing table (scope 0)
- A-1, A-2, A-3, A-4, A-6, A-7, A-8, A-9, A-10, B-2–B-7, CW7-errata, IF-ERR7-1: resolved as stated; numbers verified by rerun (S2-C1–C15).
- A-5: the referee asked for one tier TeO₂/CaWO₄/Ge/GaAs. The return splits it into t1 {TeO₂, CaWO₄} and t2 {Ge, GaAs} on the MC. This is a defensible departure,
  but CaWO₄ sits in t1 only through the 0.30-wide proxy (row 10). The resolution should say "departs from A-5 on the MC; CaWO₄ proxy-driven".
- B-1: partly. The window is computed but too low by ≈ 2.2× at the lower end (§A).
- B-8 / A-V15: §6 lists six gaps, but none carries a computation specification (scope 4 below). So "exact gaps" is resolved in name only.
- Survivors: all 10 handled in every channel (S2-C2); Li₂MoO₄ only in Migdal ✓. [E]/GAP readings flagged ✓ (R13 citation, row 9). S4 conditions carried ✓.

## D. Scope 4: exact gaps (§6)
No row is labelled CLOSED-AS-EXACT-GAP. Measured against the scope-4 standard, §6 item 1 (L(k, ω) for 𝓠_Mig and w_acc⟨1/ω⟩) names the missing input
but gives none of the following:
- the computation: Im(−1/ε(k, ω)) for k ≲ a few keV, ω up to several ω_p^{val};
- the approximation level: RPA with local fields vs TDDFT kernel, with semicore states for Ga/Ge/W/Pb;
- the method and convergence: bands, k-mesh, G-vectors, broadening, f-sum check to a stated %;
- the pitfalls: missing semicore weight biases ∫L/ω⁴; the scissor shift moves the E_g⁻⁵ tail; anisotropy.
Items 2–6 are data fetches (measured C_ij, low-T gaps, ω_T,min, b_bg, ε_eh) and need only the source class, which IF-S2-2/3 give.
Required: add a one-paragraph specification to item 1, or downgrade "exact gaps" to "remaining inputs".

## E. Scope 5: proposed LIMITS rows
L-S1–L-S3 cite only this return and WP8-F-v3 §2.7, so there is no external full text to check.
- L-S1: validity "inputs independent across materials" contradicts CONVENTIONS row 29 for same-method nuisances. Leading correction: see §B(d).
- L-S2: correct.
- L-S3: correct the formula (row 4). The "pole-dominated L" validity also needs X_pole's lower bound 1 to be labelled [E]. The f-sum gives only the upper bound
  (π/2)ω_p²/E_g⁵ on ∫L/ω⁴. Loss weight above ω_p (an upshifted interband peak) makes X_pole < 1, so [1, 3] is a prior, not a bound.

## F. Other observations (no verdict change)
- NaF POL: the return's 9.69 [8.33, 11.3] rests on FT-DFT + DB inputs. With a commonly quoted measured set (ε∞ ≈ 1.75, ε₀ ≈ 5.1, ω_TO ≈ 244 cm⁻¹)
  [UNVERIFIED, memory], (π/2)Dω_L/ρ ≈ 11.7, at the 84th percentile. The same exercise for LiF gives ≈ 20 vs 19.0. LiF still leads; NaF ≻ Al₂O₃ would firm up.
  Add measured ε pairs of the alkali fluorides to IF-S2-2.
- GaSb ER edge: the [E] shift U[0.03, 0.10] eV is bracketed by Si (0.05), Ge (≈ 0.08) and GaAs (≈ 0.10) [UNVERIFIED, standard values]. GaAs sits at the
  upper edge of the prior. R5's flag is adequate.
- CaWO₄ and CsI c_max for the NR edge reuse the same proxy. The CsI NR-edge 39.4 keV and the light-mediator 0.870 end inherit row 9.

## Required corrections (summary)
1. §0 row 3, §2.3, B-1: heavy-mediator lower window end ≈ 2.2 m_lo (η-weighted). S ≈ 0.065–0.34 MeV; 42-pool ≈ 0.17–0.27 MeV. Give the upper end with primitive cells too.
2. §1.3, L-S1: "conservative" holds only for resolved orderings. Report P₁ at r_mat = 1 (per family) next to r_mat = 0. State that tiers are correlation-blind
   and that the Migdal and 42-pool NR-edge ties resolve at r_mat → 1.
3. §5 (ii): add "excluding Migdal". Otherwise LiF and GaAs are also in two leading tiers.
4. L-S3: (n′/n)^{−3/2} multiplies the whole FOM.
5. R13 / §2.3: CsI (and CaWO₄) are not in WP8-U-v3 §5's suspect list. Declare the 0.30 width as this return's [E] and phrase R13 as a single unvalidated DFT value.
6. §1.4: 93 → 111 tiers. §1.3: Si ε_eh σ = 0.02 eV in code. Sapphire POL width ≥ 3% (ε∞ sensitivity).
7. §4 ER-quanta tolerance: Ge's listed activation sum is ≈ 2.1× Si's, above the 1.22 tolerance. Fix the reason.
8. §6 item 1: add the computation specification (§D) or rename the section.
