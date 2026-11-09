# R16 referee REF-WP8-S-B (hostile, isolated): CW7 §12, the WP8-S ranking synthesis (LE-159)

Under review: returns/R16/CW7.md §12, built on WP8-U-v2.md, WP8-U-table-v3.csv and WP8-F-v2.md; code/CW7/rank.py and the C31 check of code/CW7/checks.py.
Read: those files; CONVENTIONS, DONE (and the brief). Literature: 1910.10716 was fetched with lit.py into literature/papers-r16-REF-WP8-S-B/ (PDF and HTML deleted,
`p.txt` kept for locators). Reruns: `rank.py` (0.08 s) regenerates data/ranking.json identically (git clean); `checks.py` 32/32 PASS (17.8 s). No simulations;
the numpy/scipy checks below take under a second.

## Verdict table
| # | Claim (§12) | Verdict | Reason (section) |
|---|---|---|---|
| V1 | Pool = SURVIVOR + SURVIVOR-COND after the one-rule change, EXCLUDED-RADIO dropped | **STANDS** | 42 materials = 10 S + 32 C of WP8-U-v2 §0 item 2; KTaO₃ and InSb are absent (§A) |
| V2 | rank.py → ranking.json reproduces the §12 numbers | **STANDS WITH CORRECTION** | reproduced, but the ε_eh row and the NR-edge row of §12 do not match the script output (§D, §F) |
| V3 | "robust = same tier at r_mat = 0 (§9)"; Reading (4) "only tier membership two apart is claimed robust" | **FALLS** | rank.py propagates no uncertainty at all; anchored tiers two apart guarantee only Δln ≥ 0.2 − ε, below one c_L step on a ratio at r_mat = 0 (0.26) (§B) |
| V4 | ER low-mass edge row (m_floor, "room-T E_g") | **STANDS WITH CORRECTION** | ordering right; the "room-T" label is false: the Pb-salt gaps are low-T values from the source, Si/Ge/GaSb are room-T, so one column mixes temperatures; at T_op use WP8-F-v2 §1.3 (Si 0.333, Ge 0.212) (§C) |
| V5 | ER threshold in quanta (ε_eh) row | **STANDS WITH CORRECTION** | the script ranks Si at 3.6 (lower end of the dagger-"estimated" range "3.6-3.8") while §12 prints 3.75; at mK Ge (3.37) and Si (3.72) tie (Δln 0.099 < 0.2) (§D) |
| V6 | NR-1ph rate "∝ 1/c_LA" for the light mediator (and heavy at m_χ ≲ 0.1–1 MeV); CsI leads ×6.4 | **FALLS** | light mediator: rate is target-independent at leading order — derived (§E1) and stated by the source the table uses, 1910.10716 Eq. (35) [FT p.10]; the CsI lead rests on one unchecked DFT c_LA (§E2) |
| V7 | NR-1ph edge m_min^{ac}(1 meV): C 3.2; SiC 4.6–4.7; Al₂O₃, AlN 5.3 keV | **STANDS WITH CORRECTION** | c-BN 3.57 and h-BN 3.64 keV are tier 1 in ranking.json (both newly in the pool) and are omitted (§F) |
| V8 | POL row: LiF 19 (Z*), α-SiO₂ 18.5 (ε route, "upper"), …, Al₂O₃ 9.2 (FT 9.4) | **STANDS WITH CORRECTION** | the ε route as coded is not an upper bound (sapphire 9.15 < 9.40, its own check); orientation-inconsistent ε₀/ε_∞; two different scalars ranked in one column; DB-ε sensitivity not propagated (§G) |
| V9 | Migdal nuclear factor ranking and Reading (1) "the Migdal factors favour light ionic fluorides" | **STANDS WITH CORRECTION** (factor) / **FALLS** (reading) | the omitted 𝓠_Mig carries ω⁻⁴ above E_g and plausibly reverses the order; NiO's tier-1 slot is a pseudopotential-valence convention (§H) |
| V10 | MAG row (no ranking, all COND, F^{mag} GAP) | **STANDS** | nothing ranked; consistent with WP8-F-v2 §2.6, §5.1 |
| V11 | Background (S4) row; S4 handling | **STANDS WITH CORRECTION** | matches WP8-U-v2 §2/§4.4, but S4-COND is not carried into the channel rows: TeO₂ is quoted as an NR-1ph "SURVIVOR leader" without its ¹²³Te COND (§A) |
| V12 | Reading (2) "Sapphire and LiF are the only survivors in the leading tiers of two channels (… Al₂O₃ also NR edge)" | **FALLS** | by ranking.json Al₂O₃ is in no leading tier (POL-ε t3, Migdal t2, NR edge t2); among survivors only, Ge and GaAs also appear in ≥ 2 leader lists (§I) |
| V13 | Reading (3) every Pb-salt lead is conditional | **STANDS** | ε_eh [E, GAP-EF outside validated range], PbTe S4-COND, all three SURVIVOR-COND |
| V14 | Status CLOSED-AS-EXACT-GAP with "single missing step = R×2" | **STANDS WITH CORRECTION** | the missing steps are also the uncertainty propagation (V3) and a replacement light-mediator NR scalar (V6); R×2 is not the only one (§J) |
| V15 | Provenance (rubric e) and theory-uncertainty reflection (rubric f) | **STANDS WITH CORRECTION** | §12 carries no per-value tags; rank.py's c_LA preference contradicts V6 as written; WP8-F-v2 §4 nuisances are cited but not applied (§K) |

---
## A. Pool and screening (V1, V11)
ranking.json has 42 per_material entries; verdicts reproduce WP8-U-v2 §2 (10 S, 32 C; NiPS₃, h-BN, c-BN, PE present; KTaO₃, InSb absent). rank.py takes the last
`verdict` row and reads `S4_verdict` into the record but **never uses it** in any ranking or flag. Consequences: TeO₂ (verdict SURVIVOR, S4 COND: ¹²³Te EC
known only as a T½ lower limit, WP8-U-v2 §4.4) is listed in the NR-1ph "SURVIVOR leaders" column as "TeO₂ 2.2" without the caveat, while PbTe's S4-COND is
mentioned only in the ER row. **Correction:** add an S4 flag to every row where an S4-COND material is quoted (NR-1ph: TeO₂, PbTe; POL-ε: TeO₂ t5;
Migdal: Cr₂O₃ t3), or make rank.py print it. The cosmogenic GAP for every material but Si, Ge, NaI, Te is correctly stated in the Background row.

## B. Uncertainty and robustness (V3) — the central defect
1. rank.py (all 170 lines) contains no uncertainty: no band, no r_mat, no nuisance; `ranking()` assigns tiers by `|ln v − ln anchor| ≥ 0.2` with the anchor
   reset only at a tier change. §12's "robust = same tier at r_mat = 0 (§9)" is therefore an assertion with no computation behind it.
2. Anchored tiers: the last member of tier k may sit at ln(anchor) − 0.2 + ε and the first of tier k+2 at ln(anchor) − 0.4, so **two tiers apart guarantees
   only Δln ≥ 0.2 − ε** [D]. At r_mat = 0 (the ranking convention CW7 §9 itself sets) the ratio of two materials each carrying a c_L 20% (WP8-F-v2 §5.2) has
   σ_ln = √2·ln1.2 = 0.26 > 0.2; for POL on the ε route with ±15% DB ε the sapphire sensitivity 1.5 (WP8-F-v2 §2.5) gives 0.21 per material, GaAs-like
   weakly polar crystals up to 6.4 × 0.14 ≈ 0.9. Reading (4) "only tier membership two apart is claimed robust" does not follow.
3. Rubric (f), "could the top-ranked material change within its error band?": yes in at least ER-quanta (Ge/Si at mK, §D), NR-1ph (CsI, §E2), POL (LiF vs
   α-SiO₂: Δln = 0.027; LiF's ε route is GAP because its DB ε₀ failed V2, so LiF and quartz are compared on different scalars), Migdal (LiF/NiO/MgF₂ Δln ≤ 0.16).
   §12 states none of these as "top could change".
**Correction:** either compute the bands (per-material ln σ from the WP8-F-v2 §4/§5.2 nuisances, r_mat = 0 for the ratio, report P(rank change)), or delete
the robustness clause and Reading (4) and say "tiers are resolution bins, not confidence statements".

## C. ER low-mass edge (V4)
Script values reproduced: PbSe 0.0484, PbTe 0.0541, PbS 0.0826, Ge 0.191, GaSb 0.205, Si 0.316, GaAs 0.404 MeV (v_max = 794.5 km/s, CONVENTIONS §8). The
E_g rows are: PbTe 0.19, PbSe 0.17, PbS 0.29 "measured at low T ('*')" [FT 1910.10716 Table I p.2, verified in the fetched text], Si 1.11, Ge 0.67, CaWO₄,
NaI, CsI "T not stated (room T)". §12's header "room-T E_g" is false for the three leaders; the column mixes T. WP8-F-v2 §5.2 requires E_g(T_op) to 1% for
edges, and WP8-F-v2 §1.3 already gives Si 0.333, Ge 0.212 at low T; the table holds Si E_g_T 1.169 (0 K) [FT 2004.10709]. With T_op values the order is
unchanged (Ge and GaSb stay tied, Si and GaAs separate). **Correction:** "m_floor at T_op: Si 0.333, Ge 0.212 [E from FT]; GaSb low-T gap GAP in the table
(room-T 0.205 is a lower value of m_floor); Pb salts low-T [FT]"; drop "room-T".

## D. ER threshold in quanta (V5)
ranking.json: PbTe 1.52, PbSe 1.56, PbS 1.92, GaSb 2.67, Ge 3.0, Si 3.6, GaAs 4.2. Defects:
- `num()` returns the first number of a string, so Si takes 3.6 from "3.6-3.8" [FT 2008.08560 Table I, dagger = "estimated"], ahead of the measured
  3.72 (5 K, 6–70 K) and 3.749 (123 K) [FT 2004.10709] in the same table. §12 prints "Si 3.75", which is not what was ranked. The same parser takes the lower
  end of any range or "<"/"~" string (systematic; it affects every range-valued field read by `get`).
- Ge takes 3.0 from 1901.07569 (T not stated) — the source rank.py itself refuses for Ge E_g (`avoid=("1901.07569",)`). At the operating temperature the table
  has 3.37 ± 0.01 (50 mK, model-dependent) and 3.32 [FT 1602.08005]. Ge 3.37 vs Si 3.72: Δln = 0.099 < δ_rank, **a tie**; §12's ordering "Ge 2.96–3.37; Si 3.75"
  presents Ge ahead without saying the order depends on T and on the Luke-efficiency model.
- GaAs 4.2 is the 25 °C value (Del Sordo) [FT]; the Pb salts and GaSb are GAP-EF [E] predictions — stated, correct.
**Correction:** rank on ε_eh(T_op) with a declared source per material; fix `num()` to reject ranges or take a declared central value; state the Ge/Si tie.

## E. NR single phonon (V6)
**E1. Light mediator [D].** With (1.2′) and (2.3a′), integrating the δ(ω − c q) over ω leaves, for one LA branch, ℛ ∝ ∫_{q₋}^{q₊}dq q F_DM²(q) η(v_min) · πq/(m_u²c)
with v_min = c + q/2m_χ and q₋ = ω_th/c. For F_DM² = (q₀/q)⁴ the integrand is ∝ q⁻²/c, so ℛ ∝ (π/(m_u²c))(c/ω_th − 1/q₊)η ≈ πη(c)/(m_u²ω_th)·(1 − ω_th/(c q₊)):
**c cancels**; with q₊ = ω_LO/c (band top) the bracket is (1/ω_th − 1/ω_LO), again c-free. Hypotheses: c ≪ v (η(c) ≈ η(0)), q₊ < q_BZ, isotropic LA. The
source states the same: "the rate is dominated by the lowest detectable momentum transfer … R ∝ m_χ³σ̄_n(Σf_j)²/(m_cell μ²f_n² ω_min). For f_p = f_n, we
have f_j ∝ A_j ∝ m_cell/m_n, and the dependence on the target properties drops out" [FT 1910.10716 Eq. (35), p.10]. Numerical check (scipy, toy η = v_max − v_min,
ω_th = 1 meV, band top 30 meV): CsI(c = 1.379 km/s)/Si light-mediator ratio 0.67 at 0.3 MeV, 0.88 at 1 MeV — not 6.35. The §12 row "NR-1ph (light mediator;
heavy only …) ∝ 1/c_LA" and Reading (1)'s "the NR-1ph rate favours soft heavy lattices" are wrong for the light mediator, where the material dependence is
only the edge (q₋ ≤ 2m_χ(v − c)) and the band top. The error originates in WP8-F-v2 §0 and §5.1 ("NR-1ph scalar π/(m_u²c_LA)", "light mediator all m_χ"):
the A-free structure-factor coefficient is not a rate scalar once the q-weight is applied.
**Heavy mediator.** The 1/c scaling is 1910.10716 Eq. (37) [FT p.11], valid "Between 10⁻¹ and 1 MeV"; below ≈ 0.1 MeV "the reach ends when the acoustic modes
are no longer kinematically available" (edge-limited, Eq. (36)). So the heavy window is ≈ [0.1, min(0.43 (Si q_BZ), 1)] MeV, not "m_χ ≲ 0.1–1 MeV".
**E2. The CsI lead.** CsI's c_LA = 1.379 km/s is the only value used (`c_LA` [FT 1910.10716 Table I: "0.46" ×10⁻⁵, a DFT number; transcription CONFIRMED in
the fetched text]); CsI has no JARVIS entry (WP8-U-v2 §1.1), hence no Christoffel or Voigt cross-check, while WP8-U-v2 §0 item 7 itself rules 1910.10716 c_LA
"suspect, pending measured C_ij". Measured CsI C₁₁ ≈ 24 GPa with ρ = 4.51 g/cm³ gives c_L[100] ≈ 2.3 km/s [UNVERIFIED, reviewer's recollection], i.e.
8.757/2.3 ≈ 3.8 relative to Si — tier 2, not tier 1. Status of the 1910.10716 entry as a physical sound speed: **UNRESOLVED** (a measured-C_ij source is
needed); the ranking is driven by an unchecked DFT value and §12 does not say so. **Correction:** split the row into "heavy mediator, 0.1 ≲ m_χ ≲ 0.4 MeV
(Si): ∝ 1/c_LA" and "light mediator: material-independent above the edge; rank by the edge (row NR-1ph edge)"; mark CsI "single DFT source, no
cross-check".

## F. NR-1ph edge (V7)
ranking.json m_ac_keV_1meV: C 3.21, c-BN 3.57, h-BN 3.64 (tier 1); SiC 4.64–4.71, Al₂O₃ 5.32, AlN 5.35 (tier 2); Si 6.53 (tier 3). §12 omits c-BN and h-BN,
which the one-rule change brought into the pool (V1); h-BN is layered and its Christoffel mean hides a large directional range. Formula (2.3b) and the
1 meV numbers agree with 1910.10716 Eq. (36) ("m_χ,min ∼ 20 keV (ω_min/meV)(10⁻⁵/c_s)": C 3.3 keV). **Correction:** list c-BN, h-BN (COND) in tier 1.

## G. Polar phonons (V8)
1. **The ε route is not an upper bound as coded.** rank.py: (π/2)(1/ε_∞ − 1/ε₀)ω_max/ρ with ω_max = `omega_O_max` (DFT optical-branch top of 1910.10716) else
   `omega_Gamma_max_DFT`. Σ_νΔ_ν = 1/ε_∞ − 1/ε₀ (WP8-F-v2 (2.5a)) makes it an upper bound only if ω_max ≥ max_ν ω_Lν. For sapphire the FT LO maximum is
   906.6 cm⁻¹ = 112.4 meV [FT 1807.10291 Table II p.31, in the table] > 104 meV; the computed 9.15 is **below** the FT mode sum 9.40, i.e. the "bound" is
   violated by 3% on the one material where it can be tested. CW7-C31 tests |9.15/9.40 − 1| < 5% (agreement), not ub ≥ exact, so it passes a failed bound.
2. **Orientation inconsistency (WP8-U-v2 V4).** For Al₂O₃, α-SiO₂ and MgF₂ (uniaxial) ε₀ is the JARVIS "max principal value" [DB] while ε_∞ is the FT Tr/3
   (1910.10716): Al₂O₃ 11.969 vs FT Tr/3 (2·9.3 + 11.5)/3 = 10.03. With FT-only inputs: 8.74 (ω = 104) and 9.44 (ω = 112.4) meV cm³/g; only the latter is a valid
   bound and it sits 0.4% above the mode sum. Quartz's 18.5 and MgF₂'s 11.9 carry the same max-vs-average bias (upward) and are V4 "orientation-maximal".
3. **Two scalars, one column.** LiF 19 is a single-branch Z* estimate (with ω_LO → `omega_O_max` 77.2 meV because `GAP:omega_L`), α-SiO₂ 18.5 an upper bound for a
   multi-branch crystal; ranking them in one tier says nothing about their order. WP8-F-v2 §2.5: 𝓡_pol ∝ 𝓘_pol/ρ_T is [E] for multi-branch crystals. The
   "Leading tiers" cell should give α-SiO₂ as "≤ 18.5" and not as a tier-1 member.
4. GaAs: ×60 below sapphire agrees with WP8-F-v2 §2.5 (×61–65). STANDS.
**Correction:** ε route with ω_max = max ω_L [FT] where tabulated and the declared orientation (or the (1/3)Σ_iL_ii average with per-axis ε), C31 as an
inequality, α-SiO₂ and MgF₂ as bounds outside the tiering, and the §2.5 ε sensitivities propagated (§B).

## H. Migdal (V9)
1. rank.py's factor is Σ_κ VALENCE(el)²/A_cell; the outputs imply Z_ion(F) = 7, Z_ion(Li) = 1, Z_ion(Ni) = 10. For Ni the valence count is a pseudopotential
   choice: with 3s3p semicore (18 e) NiO goes from 1.82 to 4.82 and leads by ×2.5. §12 must state the convention and that NiO's (and every transition-metal
   oxide's) slot depends on it; WP8-F-v2 (2.7′) defines Z_κ(k) inside the k-integral, so the small-k valence value is a further approximation [E].
2. Reading (1) "the POL and Migdal factors favour light ionic fluorides and oxides" is an overclaim for Migdal. 𝓠_Mig,κ(ω) = ∫d³k Z_κ²L(k,ω)/(3(2π)³ω⁴)
   starts at E_g; the ω⁻⁴ weight alone changes by (14.2/1.11)³ ≈ 2×10³ between the LiF and Si onsets in an integral ∫_{E_g}dω ω⁻⁴ [E, ELF shape ignored],
   against ×3.4 in the nuclear factor (1.93 vs 0.57). The omitted factor is the larger, plausibly of opposite sign in the ordering; §12 marks it "× 𝓠_Mig (GAP)"
   but then draws the reading from the nuclear factor. **Correction:** delete "Migdal" from Reading (1)/(2) or say "at fixed 𝓠_Mig, which is GAP and
   expected to favour narrow gaps".

## I. Reading (2) (V12)
ranking.json tiers for Al₂O₃: POL-ε t3 (α-SiO₂ t1; MgF₂, NaF t2), Migdal t2 (LiF, NiO, MgF₂ t1), NR edge t2 (C, c-BN, h-BN t1): Al₂O₃ is in **no** leading tier.
If "leading" means "first survivor", Al₂O₃ leads POL-ε, NR edge and (tied with γ-LiAlO₂) Migdal-survivors; but then Ge (ER edge, ER quanta, NR-1ph survivor
list "Ge, GaAs 1.8") and GaAs (ER edge, NR-1ph) also lead two channels, so "the only survivors" is false either way. **Correction:** state the definition
and list Al₂O₃, LiF, Ge, GaAs (and NaF for POL), or delete the sentence.

## J. Status (V14)
CLOSED-AS-EXACT-GAP requires "the strongest derived statement plus the single missing step" (DONE.md return type 4). §12 names R×2 as the single step; this
report shows two further missing steps internal to the synthesis: uncertainty propagation (§B) and a corrected NR-1ph light-mediator scalar (§E). Status
should read "synthesis delivered with exact gaps: (i) bands per §B; (ii) NR-1ph light-mediator re-ranking by the edge; (iii) R×2 of the corrected text".

## K. Provenance and theory uncertainty (V15; rubric e, f)
- §12 declares "E for numbers" globally but prints no tag per value. Mixed provenance inside single entries is not shown: Al₂O₃ POL-ε = ε₀ [DB] + ε_∞ [FT DFT]
  + ω [FT DFT] + ρ [E from a_exp]; CsI c_LA [FT DFT]; all other c_LA [E from DB C_ij].
- rank.py prefers `c_LA_recommended`/`c_LA_Christoffel_avg` ([E] from JARVIS C_ij, i.e. DB-level inputs) over `c_LA` [FT DFT-in-paper] for every material that
  has both. WP8-U-v2 V6 ranks "[FT] DFT-from-a-paper > [E] from FT inputs > [DB]". The choice is defensible (the 1910.10716 c_LA "suspect" ruling, §0 item 7)
  but contradicts V6 as written; state it as a declared V6 exception. Effect: ≤ 10% for the checked materials (c_LA_check_1910 0.91–1.10).
- Rankings driven by [E] or GAP values (rubric f): every ε_eh except Si, Ge, GaAs, C, SiC, GaN (GAP-EF [E]); every NR-1ph c_LA ([E] from DB, CsI/CaWO₄ FT DFT);
  POL ε₀ [DB]; Migdal VALENCE convention; MAG all GAP. §12 states some of these per row but not which tier boundaries they move.
- WP6 nuisance types (WP8-F-v2 §4): the type-M Z*/ε_∞/ε₀ rows, the type-T n_A row and the halo band (v_max 2–7% → m_floor 4–14%, common to all materials,
  hence cancelling in the ranking — a statement §12 should make) are not applied. Only "DB c_L +20% ≈ one tier" and "Z* 10% ⇒ ≈ one tier" are quoted.
- Consistency (rubric d): v_max = 794.5 km/s and the 2E_g/v_max² floor agree with CONVENTIONS §8 and WP8-F-v2 §1.3; NOTATION symbols used in §12 (𝓘_pol, 𝓠_Mig,
  𝓈_λ, r_mat) follow the WP8-F-v2 renames; no clash found.

## L. Literature (rubric c)
§12 makes no claim that a paper or database is wrong. Checked against 1910.10716 full text (fetched, PDF deleted): Table I CsI c_LA 0.46×10⁻⁵ (= 1.379 km/s),
Pb-salt E_g "measured at low temperature" — **CONFIRMED** as transcribed; Eq. (35) target-independence of the light-mediator single-phonon rate and Eq. (37)
1/c_s for the heavy mediator at 0.1–1 MeV — used above against §12/WP8-F-v2 §5.1. CsI c_LA as a physical sound speed: **UNRESOLVED** (§E2).

## Required corrections (summary)
1. NR-1ph: light mediator re-ranked by the edge only; heavy mediator 1/c_LA restricted to ≈ 0.1–0.43 MeV (Si); CsI flagged; owed to WP8-F-v2 §0, §5.1 too.
2. Uncertainty: compute bands (r_mat = 0 for ratios) or withdraw the robustness clause and Reading (4).
3. POL: ε route with max ω_L [FT] and consistent orientation; C31 as ub ≥ exact; α-SiO₂, MgF₂ as bounds outside the tiers.
4. ε_eh at T_op; fix `num()` range parsing; Ge/Si tie stated; §12 text = script output.
5. ER edge: E_g(T_op), drop "room-T".
6. Readings (1) (Migdal, NR-1ph clauses) and (2) rewritten; Migdal valence convention (NiO) stated.
7. NR edge: add c-BN, h-BN. S4-COND flags in every channel row (TeO₂). Per-value provenance tags; V6 exception for c_LA declared.
8. Status: exact gaps (i)–(iii) of §J instead of "single missing step R×2".
