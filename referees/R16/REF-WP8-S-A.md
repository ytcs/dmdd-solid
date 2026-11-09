# R16 referee REF-WP8-S-A: CW7 §12 (WP8-S ranking synthesis), hostile and isolated

Brief briefs/R16/REF-WP8-S-A.md. Read: returns/R16/CW7.md (§12 and the sections it rests on, §9–§11, §13), WP8-U-v2.md, WP8-F-v2.md,
WP8-U-table-v3.csv; code/CW7/rank.py, checks.py (C31), code/WP8-U/materials.py (`VALENCE`, imported by rank.py); CONVENTIONS (v_max §8), DONE.
Not read: referees/, state/, briefs/ (except my own), LAUNCHES/log, other R16 returns.
**Reruns.** rank.py was run from a scratch copy that writes to the scratchpad; its output is byte-identical (`cmp`) to code/CW7/data/ranking.json.
checks.py: 32/32 PASS in 11 s. Note: checks.py re-runs rank.py and **rewrites** code/CW7/data/ranking.json; I checked the file was byte-identical afterwards
and git shows no change. Every number I introduce is [E] from v3-table inputs, with its formula, unless marked [UNVERIFIED]. No full-text fetch was needed
(rubric (c): §12 claims no published paper or database is wrong), so no papers folder was created.

## Verdict table (one row per main claim of §12)
| # | Claim (§12) | Verdict | Reason (details in the numbered section) |
|---|---|---|---|
| V1 | Method: tiers δ_rank = 0.2 in ln FOM, "ties inside a tier"; "robust = same tier at r_mat = 0 (§9)" | **FALLS** (robustness), **STANDS WITH CORRECTION** (tiers) | rank.py takes no uncertainties and computes no r_mat bands. Its tiering is anchor-based, so ties are not transitive. δ_rank is cited to "WP8-F §5.2", which does not define it (§1) |
| V2 | The pool is SURVIVOR + SURVIVOR-COND, with EXCLUDED-RADIO dropped | **STANDS WITH CORRECTION** | KTaO₃ and InSb are correctly dropped. But any material with a GAP input drops out of a channel without notice: the SURVIVOR Li₂MoO₄ is in no channel, and the ER edge omits Bi₂Se₃, ZrTe₅, SrTiO₃, TeO₂, γ-LiAlO₂, Al and Nb (§2) |
| V3 | ER low-mass edge, "m_floor = 2E_g/v_max² (room-T E_g)", leaders PbSe, PbTe > PbS > Ge, GaSb > Si > GaAs | **STANDS WITH CORRECTION** | The E_g inputs mix temperatures: the Pb salts are "measured at low T", Si, Ge, GaAs and GaSb are room T. WP8-F-v2 §5.2 requires E_g(T_op). The tiers survive with the values available (§3) |
| V4 | ER ceiling Z/A is "not a ranking variable" | **STANDS** | correct, and stated as such |
| V5 | ER threshold in quanta: Pb salts 1.5–1.9, GaSb 2.7, Ge 2.96–3.37, Si 3.75, GaAs 4.2 | **STANDS WITH CORRECTION** | The script uses Si 3.6 and Ge 3.0, not the values the text prints. V6 provenance is not applied. The Pb-salt GAP-EF bands overlap (§4) |
| V6 | NR-1ph rate ∝ 1/c_LA. SURVIVOR leaders TeO₂ 2.2, CaWO₄ 2.1, Ge, GaAs 1.8 | **STANDS WITH CORRECTION** | The four survivors span ln 0.18 < δ_rank, so they are one tie. The scalar is 1/c̄_LA, not the FOM's ⟨Σ_ν(q̂·ê_ν)²/c_ν⟩. A systemic C_ij-ordering defect breaks the axial symmetry of every uniaxial entry. TeO₂ is DB-driven and S4-COND, and its row says neither (§5) |
| V7 | NR-1ph edge: C 3.2, SiC 4.6–4.7, Al₂O₃ and AlN 5.3 keV. Survivors Al₂O₃ 5.3, Si 6.5 | **STANDS WITH CORRECTION** | Reproduced. Same C_ij defect for Al₂O₃ and AlN. The rate-vs-edge opposition is stated, which is correct (§5) |
| V8 | POL: LiF 19 (Z*), α-SiO₂ 18.5 (ε, upper), MgF₂ 11.9, NaF 9.9–10, Al₂O₃ 9.2 (FT 9.4), CaF₂ 8.5, MgO 7.2–7.6. Survivors LiF, NaF, Al₂O₃ | **FALLS as stated, restate** | The "upper" ε-route falls below the FT sapphire value (9.15 < 9.40), which refutes the bound. Its inputs mix sources. V4 labels are missing. A bound is ranked against central values. No POL reach ranking is given. The robust survivor of the claim is that LiF leads the survivors (§6) |
| V9 | Migdal nuclear factor Σ Z_ion²/A_cell: LiF 1.93, NiO 1.82, MgF₂ 1.64, …; survivors LiF, LiAlO₂, Al₂O₃ | **STANDS WITH CORRECTION** as a labelled factor. **FALLS** as used in Reading (1)–(2) | A plasmon-pole estimate of 𝓠_Mig alone cancels LiF's ×3.4 advantage over Si, before the E_g-dependent interband weight is counted. NiO ranks on a convention (Ni valence 10) (§7) |
| V10 | MAG row (no ranking; all COND; F^{mag} GAP) | **STANDS** | It is not a ranking and says so. "YIG gapless acoustic": the ferrimagnet branch is quadratic (WP8-F-v2 §2.6(b)), so the AFM (2.3b) edge algebra does not apply. Add this |
| V11 | Background (S4) row; Reading (3) "every Pb-salt lead is conditional on ε_eh … and soft-mode inputs" | **STANDS WITH CORRECTION** | It omits ²¹⁰Pb, which WP8-U-v2 §4.4 itself makes source-dependent for lead salts. That is an S4-type condition on the very materials that top three channels (§8) |
| V12 | Reading (1) "No material leads every channel …; POL and Migdal favour light ionic fluorides/oxides; NR-1ph rate favours soft heavy lattices (TeO₂, CaWO₄)" | **STANDS WITH CORRECTION** | The first clause stands. The Migdal clause falls (V9). The TeO₂/CaWO₄ clause is a tie with Ge and GaAs (V6) |
| V13 | Reading (2) "Sapphire and LiF are the only survivors in the leading tiers of two channels (POL + Migdal; Al₂O₃ also NR edge)" | **FALLS** | It rests on Migdal (V9). Al₂O₃ is t3 on the ε route and tied with NaF among survivors. Defensible restatement: LiF leads POL; Al₂O₃ leads the NR edge among survivors (§9) |
| V14 | Reading (4): adjacent tiers swap under one DB-accuracy step, so only membership two tiers apart is robust | **STANDS WITH CORRECTION** | The rule is sound but is not applied: several "leader" lists violate it (V6, V8). It also omits the theory (WP6-type) nuisances and the background regime (§10) |
| V15 | Exact remaining gap: R×2 of §12, plus the listed secondary inputs | **STANDS** | Add to it: the C_ij re-ordering, E_g(T_op) inputs, ²¹⁰Pb for Pb salts, and the ⟨1/c⟩ FOM (§11) |

---
## 1. Method and tiering (V1, V14)
(a) **The robustness test was not executed.** §12 defines "robust = same tier at r_mat = 0 (§9)", but rank.py has no uncertainty input anywhere and no band
computation. The "Robustness / caveat" column is prose. CW7-C31 tests only (i) the sapphire ε-route against 9.40 within 5% and (ii) the GaAs ε-route in
[0.14, 0.16]. It checks no ordering, so "32/32 PASS" verifies no tier. **Correction:** either implement the r_mat = 0 band (each scalar's needed accuracy
from WP8-F-v2 §5.2 as σ_ln, independent across materials, plus the r = 1 common nuisances) and report P(tier change), or delete the robustness definition and
call the column qualitative.
(b) **Ties are not transitive.** `ranking()` opens a new tier when |ln v − ln v_anchor| ≥ 0.2, where the anchor is the first member of the current tier. Members
on opposite sides of a boundary can then be closer than δ_rank. From the rerun: NaF 9.87 (t2) vs Al₂O₃ 9.15 (t3), Δln = 0.076; TeO₂ 2.16 (t3) vs Ge 1.82 (t4),
Δln = 0.171; MgF₂ 1.64 (t1) vs α-SiO₂ 1.46 (t2), Δln = 0.116. Tier labels also depend on which COND materials are in the list, so the "SURVIVOR leaders" columns
inherit anchors from non-survivors. **Correction:** use pairwise resolution (A ≻ B only if Δln ≥ δ_rank) and recompute the tiers within the SURVIVOR set.
(c) **Provenance of δ_rank.** rank.py's docstring cites "WP8-F §5.2". WP8-F-v2 §5.2 lists needed accuracies, not δ_rank. δ_rank appears only in the IF-F1′
row and the Symbols row ("as R13"). Cite the R13 definition, or derive it, for example as the smallest needed accuracy, ln 1.2 ≈ 0.18.

## 2. The ranked set (V2)
EXCLUDED-RADIO is dropped and the four re-admitted COND materials are present, both correct. But rank.py silently omits a material from any channel whose
input is None. From `per_material`:
- **Li₂MoO₄** (a SURVIVOR) has no E_g, c_LA, ε or ε_eh, so it appears in **no** channel;
- the ER edge also omits **TeO₂** (E_g GAP: the table has only DFT gaps, which V1 forbids), γ-LiAlO₂, SrTiO₃, Bi₂Se₃, ZrTe₅, NiO, MnO, Cr₂O₃, c-BN, h-BN and PE;
- for the superconductors Al and Nb, the floor is the pair-breaking 2Δ and needs another formula, not "GAP".
Bi₂Se₃ (DFT gap 0.32 eV [DB]) and ZrTe₅ (0.014 eV [DB]) would, on any measured gap of that size, enter the leading ER-edge tiers. "PbSe 0.048, PbTe 0.054
lead" therefore holds only among materials with a measured E_g. **Correction:** add to each channel row a "not ranked (GAP)" list, and give a separate
SC-edge line (2Δ_BCS-based) for Al and Nb, or exclude them explicitly.

## 3. ER low-mass edge (V3)
The CSV notes say the Pb-salt gaps (0.19, 0.17, 0.29 eV, 1910.10716 Table I) are "measured at low T ('*')". Si 1.11, Ge 0.67, GaAs 1.42 and GaSb 0.72 are
"T not stated (room T)". The label "(room-T E_g)" is therefore wrong for the leading tier, and the column mixes temperatures. WP8-F-v2 §5.2 asks for
E_g(T_op) at 1%. The Si 0 K value 1.169 eV is in the table [FT 2004.10709 Table I p.5] and gives 0.333 MeV. rank.py nevertheless uses 1.11, so it prints
0.316 MeV for Si. The ordering survives: the semiconductors' gaps rise on cooling while the Pb-salt values are already low-T, so the separation of the tiers
only widens. **Correction:** rank on E_g(T_op), using the `E_g_T` row where it exists. Add `GAP:E_g_lowT` for Ge, GaAs and GaSb (low-T values are known in the
literature but not in the table). Relabel the column. v_max = 794.5 km/s matches CONVENTIONS §8 (checked).

## 4. ER threshold in quanta (V5)
rank.py takes the first [FT] `eps_eh` row. For Si that is "3.6-3.8" [2008.08560], parsed as 3.6. For Ge it is 3.0 [1901.07569]: rank.py excludes 1901.07569
for E_g only, not for ε_eh. The §12 table prints Si 3.75 and Ge 2.96–3.37, so the printed values are not the ranked ones. The v3 table holds the operating-T
values 3.72 (5 K) and 3.749 (123 K) [FT 2004.10709], and 3.37 (50 mK) [FT 1602.08005]. **Correction:** select ε_eh by V6 and by T_op, and print what is
ranked. The Pb-salt t1/t2 split (PbTe 1.52, PbSe 1.56 | PbS 1.92; Δln = 0.21–0.23) sits inside overlapping GAP-EF bands (PbTe 1.19–1.76, PbS 1.57–2.22). It is
not resolved, and the whole Pb-salt column is [E] outside the GAP-EF validation range, which §12 does state. GaSb 2.67 (2.48–3.09) [E] is tied with Ge.
The row's own caveat is right: near threshold the quantity is P(N|q,ω), not ε_eh.

## 5. NR single-phonon rate and edge (V6, V7)
(a) **Tie.** Survivor values relative to Si: TeO₂ 2.16, CaWO₄ 2.06, Ge 1.82, GaAs 1.81. The span is ln(2.16/1.81) = 0.18, below δ_rank and below the c_L
need (20%, WP8-F-v2 §5.2). These four are one tier. "Favours soft heavy lattices (TeO₂, CaWO₄ among survivors)" is not resolved.
(b) **Wrong scalar.** WP8-F-v2 (2.3a′) gives a per-mass coefficient Σ_ν(q̂·ê_ν)²/c_ν(q̂), angle-averaged, i.e. ⟨Σ_ν(q̂·ê_ν)²/c_ν⟩. rank.py uses
1/c̄_LA with c̄_LA the sphere-mean LA speed. By Jensen and branch mixing these differ, and the difference grows with anisotropy. For TeO₂, using the table's
own C_ij (numpy, 4000 directions, ρ 5.917 [DB]): c̄_LA = 4.04 (which reproduces the table's 4.05), while ⟨Σ(q̂·ê)²/c⟩⁻¹ = 3.77 km/s [E], a 7% shift. That is
below one tier, but it is systematic and sign-definite: it favours anisotropic crystals. **Correction:** rank on the FOM's own average.
(c) **Systemic C_ij defect** (a fact about the campaign's processing, derivable from the v3 table alone). In a crystal with a 3- or 4-fold c-axis, the two
transverse speeds along [001] are degenerate (both equal √(C₄₄/ρ)). The `c_dir_100_001` rows violate this:
TeO₂ [001] T 2.22/3.51, MgF₂ 4.18/5.61, α-SiO₂ 3.64/4.62, Al₂O₃ 6.02/6.39, γ-LiAlO₂ 4.85/4.96 km/s.
The listed DB tensors (e.g. TeO₂ "C44=72.7; C66=28.8") were therefore assembled with C₄₄ ≠ C₅₅. A likely cause is an index-ordering mismatch with the
database's shear ordering (xy, yz, zx) [UNVERIFIED]. The trigonal entries also list no C₁₄. For TeO₂, using C₄₄ = C₅₅ = 28.8 and C₆₆ = 72.7 moves c̄_LA from
4.04 to 4.10 km/s [E]. The rate effect is ≲ 2–7%, so no tier changes at present. But every non-cubic `c_LA_Christoffel_avg`, `c_dir` and edge value
(Al₂O₃'s 5.3 keV, the survivor NR-edge leader, included) rests on an unsymmetric tensor. **Correction:** rebuild the tensors in the symmetric Voigt
convention, add C₁₄ for the trigonal classes, check the degeneracy along [001], and re-run.
(d) **Provenance.** TeO₂ enters with ρ [DB] 5.917 and c_LA [E from DB C_ij]. The row's caveat names GaAs's +20% DB error but not that the TeO₂ lead is wholly
DB-driven. CaWO₄'s c_LA is [FT 1910.10716], a source WP8-U-v2 §5 calls "suspect, pending measured C_ij" for the hexagonal and NaCl rows. TeO₂ is S4-COND
(¹²³Te), and that is not carried into its NR-1ph row.
(e) **Edge.** m_min^{ac} = ω_th/(2c(v_max − c)) reproduces C 3.2, Si 6.5 and Al₂O₃ 5.3 keV [E]. The stated opposition of rate and edge is correct.

## 6. Polar phonons (V8)
(a) **The "upper" route is not an upper bound.** (π/2)(1/ε_∞ − 1/ε₀)ω_max/ρ bounds Σ_ν(πω_Lν/2)Δ_ν/ρ from above only if ω_max ≥ max ω_Lν and ε_∞, ε₀ are
one consistent pair. For Al₂O₃ it gives 9.15 < 9.40, the FT mode sum. CW7-C31 records this as agreement ("< 5%") when it refutes the label. The table
shows two causes. First, ω_max = 104 meV is the DFT optical range of 1910.10716 [FT], while WP8-F-v2 §2.5 itself uses a 112 meV sapphire branch. Second,
ε₀ = 11.969 is the DB *max principal* DFPT value (OptB88vdW) while ε_∞ = 3.26 is the FT Tr/3 value of a different calculation. With the consistent DB pair
(3.204, 11.969) the result is 9.37 at 104 meV and 8.25 at the DB ω_max of 91.67 meV [E]. The same mixing affects α-SiO₂ (18.5 mixed vs 17.1 with the DB pair
[E]) and MgF₂ (11.9 vs 11.45 [E]).
(b) **V4 labels.** α-SiO₂ and MgF₂ are uniaxial and use DB tensor maxima. V4 (WP8-U-v2 §1.3) requires the label "orientation-maximal". α-SiO₂ is labelled
"upper" and MgF₂ is unlabelled.
(c) **A bound ranked against central values.** Putting LiF 19 (Z* route, a central diatomic value) and α-SiO₂ 18.5 (a bound) in the same tier is an artefact. A
multi-branch crystal with strong low-ω modes lies below its ω_max bound by ⟨ω_L⟩_Δ/ω_max < 1. **Correction:** rank the ε-route materials by the WP8-F-v2 (8.1)
bracket (rigorous for cubic only), shown as intervals, and drop α-SiO₂ and MgF₂ from "leading" until a mode sum exists.
(d) **What survives.** Among survivors LiF leads: 19 vs NaF 9.9, Δln = 0.65. The LiF value has only the Z* route, because its ε₀ is V2-GAP. ∂ln𝓘/∂lnZ* ≤ 2
(WP8-F-v2 §2.5), so a 10% Z* error gives ≤ 0.2 in ln, far below 0.65. The LiF inputs (Z* 1.05, ε_∞ 2.02, ω 77.2 meV) are DFT values from 1910.10716 [FT], and
ω is the "max phonon energy", not a Γ-point ω_LO. LST with these inputs gives ω_T ≈ 32 meV [E], a cross-check worth stating. NaF (Z* 9.95, ε 9.87) and
Al₂O₃ (FT 9.40) are one tier, Δln ≤ 0.06.
(e) **GaAs.** The Z* route gives 0.170 (C31 output), outside WP8-F-v2 §2.5's 0.144–0.153. Either the range or the Z* inputs need a sentence. The
"×60 below sapphire" figure stands only on the ε route.
(f) **Reach not ranked.** WP8-F-v2 §0 gives the POL edge as 2ω_LO,ν/v_max². That ordering is the reverse of the rate ordering (soft polar lattices win: the
GaAs edge is ≈ 10 keV, against ≈ 2·77 meV/v_max² ≈ 22 keV for LiF [E]). §12 omits it, although it gives the analogous NR-1ph edge row. **Correction:** add a
"POL edge" row.

## 7. Migdal (V9)
The row is honestly labelled "nuclear factor only; × 𝓠_Mig (GAP)". Reading (1)–(2), however, treat it as a channel ranking. The omitted factor is not O(1)
across this pool. 𝓠_Mig,κ ∝ ∫dω L/ω⁴ (WP8-F-v2 (2.7′)). With the f-sum-normalised plasmon pole L = (π/2)ω_p δ(ω − ω_p), this is (π/2)ω_p⁻³. Using the
table's ħω_p^{val} (Si 16.6 [FT], Ge 15.6, LiF 26.1, Al₂O₃ 27.9 [E]), the ratio 𝓠(Si)/𝓠(LiF) is (26.1/16.6)³ = 3.9 [E]. LiF's nuclear advantage is
1.93/0.57 = 3.4. The pole estimate alone already reverses the order (LiF/Si net 0.87 [E]). On top of that, interband weight at ω ≥ E_g, weighted by ω⁻⁴, adds
far more for Si (E_g 1.1 eV) and Ge (0.67 eV) than for LiF (14.2 eV). The sign of "Migdal favours light ionic fluorides" is therefore probably wrong, and in
any case unsupported. The f-sum bound ∫L/ω⁴ ≤ (π/2)ω_p²/E_g⁵ makes the E_g⁻⁵ suppression of wide-gap targets explicit [D]. Separately, NiO's t1 place
(1.82) comes from `VALENCE["Ni"] = 10`, i.e. counting 3d⁸4s² in Z_ion. Whether 3d counts in Z_ion(k) or in L is a convention of 2011.09496's split, and it
changes NiO by ×(10/2)² on that ion. Mn = 7, Cr = 6 and Fe = 8 are likewise convention-driven. **Correction:** keep the row as a factor, delete the Migdal
clauses of Reading (1)–(2), and state the 𝓠_Mig dependence (∝ ω_p⁻³ at the pole, with E_g-controlled interband weight).

## 8. Background, S4 and the Pb salts (V11)
The pool handling of S4 is correct: KTaO₃ and InSb are out, and TeO₂, PbTe, ZrTe₅ and Cr₂O₃ are COND. But the Pb salts top three channels (ER edge, ε_eh, and
NR-1ph among the COND materials), and WP8-U-v2 §4.4 itself says ²¹⁰Pb "for lead salts … depends on the lead source" (`GAP:Pb210_U_Th`). For a lead
compound, ²¹⁰Pb is in the bulk through the element. It is not only process or surface contamination. Modern lead typically carries enough ²¹⁰Pb to exceed
the S4 default by orders of magnitude, and only selected (ancient) lead might not [UNVERIFIED: order of magnitude, from memory]. **Correction:** Reading (3)
should add "and on low-²¹⁰Pb lead (S4-type condition, GAP)" for PbS, PbSe and PbTe. CsI (NR-1ph t1, 6.4) carries a Cs radio-contaminant question of the same
kind that the table does not address; flag it or show that the S4 row covers it.

## 9. Readings (V12, V13)
Reading (2) falls. "LiF and sapphire lead two channels" needs Migdal (§7). Al₂O₃ is not a POL leader: it is t3 on the ε route and tied with NaF behind LiF.
A defensible restatement: among SURVIVORs, LiF leads POL robustly (§6d); Ge leads the ER edge (then Si, GaAs); Al₂O₃ leads the NR edge (subject to §5c);
the NR-1ph rate is a four-way tie (TeO₂, CaWO₄, Ge, GaAs). Reading (1)'s first clause, "no material leads every channel", stands on any of these numbers.

## 10. Uncertainty, regime and theory nuisances (V14; rubric (f))
- **Rate vs reach / background regime.** Every §12 scalar is a rate (signal) scalar or an edge. WP8-F-v2 §3 shows that in the background-limited regime the
  reach goes as 𝓡/√(b_bgΔE), and at the systematics floor as 𝓡/(f_sys b_bgΔE_ROI). b_bg is GAP for every survivor except Si, Ge, NaI and Te (cosmogenics,
  CW7 §11), and Si ³H at saturation is 11.06 /(kg·d·keV) [E, CW7-C19], above the S4 default. §12 must state once that its tiers are background-free rankings
  and can be reordered by 𝓩_B.
- **Theory nuisances (WP6 types, WP8-F-v2 §4).** §12 uses only DB-accuracy steps. The theory widths that sit at or above δ_rank are not mapped onto tiers:
  ER near-edge ×e^{±0.75}; the Z*/ε M-type rows with ε-route sensitivities up to 6.4 (GaAs); the GAP-EF band on ε_eh; the Z_κ(k) profile M row for Migdal.
  The halo band (v_max 2–7%) is common to all materials (r = 1), shifts every edge by the same factor, and does not reorder. Say so.
- **[E]/GAP-driven leads, stated or not.** Stated: the Pb-salt ε_eh and the POL Z* (DFT) values. Not stated: the TeO₂ NR-1ph lead (DB ρ, DB C_ij), the
  α-SiO₂ and MgF₂ POL values (DB ε₀ maxima), the NiO and MgF₂ Migdal factors (valence convention), and the CsI and NaI c_LA values.
- Could the top survivor change within its band? ER edge (Ge): no, since Δln(Si/Ge) ≈ 0.5. POL (LiF): no (§6d). NR-1ph: yes, it is a tie. NR edge (Al₂O₃ vs
  Si, Δln 0.20): marginal, and it depends on §5c. Migdal: undetermined (§7).

## 11. Rubric items (a)–(e)
(a) DERIVED steps: the functionals are WP8-F-v2's. §12 adds only the tiering rule and the scalar choices. The tiering (§1) and the NR-1ph scalar (§5b) do not
match their stated definitions; there are no other derivations. (b) §12 proposes no LIMITS rows: N/A. (c) No claim that a paper or database is wrong: N/A.
The §5c finding concerns the campaign's tensor assembly. (d) Consistency: v_max = 794.5 km/s (CONVENTIONS §8) ✓; the symbols δ_rank, 𝓘_pol, m_min^{ac},
𝓠_Mig,κ, ρ_T and ε_eh are used as in WP8-F-v2 ✓; δ_rank provenance needs fixing (§1c). (e) Provenance tags: all §12 numbers are [E], as declared. The printed
ε_eh values do not match the ranked ones (§4). The V4 labels are missing (§6b). The "(room-T E_g)" label is wrong (§3).
**Additions to the exact remaining gap (V15):** symmetric C_ij rebuild with C₁₄ (§5c); E_g(T_op) rows (§3); `GAP:Pb210` for the Pb salts as an S4 condition
(§8); the ⟨Σ(q̂·ê)²/c⟩ NR-1ph scalar (§5b); the POL mode sums or brackets for the multi-branch ε-route materials (§6); a 𝓠_Mig estimate before any Migdal
reading (§7); the background-limited reading (§10).

## Required corrections (summary)
1. Implement or drop "robust = same tier at r_mat = 0". Use pairwise ties within the SURVIVOR set. Fix the δ_rank citation.
2. Add a "not ranked (GAP)" list to each channel (Li₂MoO₄ is in no channel). Give Al and Nb an SC edge or exclude them.
3. ER edge: use E_g(T_op), relabel the column, and print Si 0.333.
4. ε_eh: select by V6 and T_op, and print the values that are ranked.
5. NR-1ph: treat TeO₂, CaWO₄, Ge and GaAs as one tier. Use ⟨Σ(q̂·ê)²/c⟩. Rebuild the uniaxial C_ij. State the DB provenance and S4-COND for TeO₂.
6. POL: drop "upper" for the mixed-input ε route (Al₂O₃ refutes it). Pair ε_∞ and ε₀ consistently. Add V4 labels. Rank intervals, not bounds against
   central values. Add the POL edge row. Reconcile GaAs 0.170 with 0.144–0.153.
7. Migdal: remove it from Reading (1)–(2). State the ω_p⁻³/E_g dependence of 𝓠_Mig and the valence convention behind NiO.
8. Reading (2): withdraw it and restate as in §9. Reading (3): add the ²¹⁰Pb condition.
9. State that the tiers are background-free rankings, and map the WP8-F-v2 §4 theory nuisances onto the tiers.
10. MAG: YIG's acoustic branch is quadratic (FM-type edge algebra).
