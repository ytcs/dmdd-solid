# R16 / CW8-A merge log: verified R14–R16 results merged into the campaign files

Agent CW8-A, brief briefs/R16/CW8-A.md, 2026-11-01. Edited only: LIMITS.md, NOTATION.md, CONVENTIONS.md, state/CORRECTIONS.md, state/SOTA.md, state/LOOSE-ENDS.md,
FRAMEWORK.md, registry.md, and this log. No return, referee report or code was edited; nothing was committed.
Inputs (merge order, later overrides earlier): (1) returns/R14/WP5-AUD.md + referees/R14/REF-WP5-AUD-{A,B}.md as settled in returns/R16/CW5.md §1 (LE-22) and CW5-errata.md;
(2) returns/R16/GAP-EF-v2.md + GAP-EF-v2-errata.md (supersede R14 GAP-EF), EF-LIT.md; (3) returns/R16/CW{2..7}.md through referees/R16/VER-CW{2..7}.md and
CW{2..7}-errata.md (errata re-issued text wins; "unchanged" items from the CW file); (4) returns/R16/WP8-R-v2.md (+ CW6-errata §B4), WP8-U-v3.md, WP8-U-table-v4.csv,
WP8-F-v3.md (WP8-S not merged); (5) returns/R15/CMPMC-AUD.md, returns/R16/CMPMC-DEV.md (CMPMC paer-sota 3d43a02), returns/R15/COMP-PAER.md.
One file outside the list was consulted for exact text only: returns/R13/WP5-v4.md l.952–1124 (the IF-R13-1 replacement text and IF-R13-4/-8 wording), because the brief
names IF-R13-1 and WP5-AUD D-15 points to it.
Format: file → section → source item. Status words: CONVENTIONS §12 as the brief reads it (claims verified R×1 after a return are REFEREED only if the package also
had R×2; otherwise CLAIMED + VERIFIED).

## A. Edits

### A1. state/CORRECTIONS.md
| Section | Edit | Source item |
|---|---|---|
| §18 last row (WP7-E-v3 §5 amendment) | marked **DONE**: WP5-v4 returned and audited; IF-R13-2, -3, -5 resolved; IF-R13-4, -8 stand | WP5-AUD IF-AUD-8; LE-165 |
| §19 (new) header | sources, type key, coordinator-file pointer rule, IF-AUD-n label clash (WP5-AUD vs CMPMC-AUD) | brief; CONVENTIONS §14 |
| §19.1 WP0-v3 | (iv″b); rigour paragraph; Scope of (H2); §9.2 (iii); (2.9) + L9b; (2.9) 1/m_φ² check; (3.5)–(3.6) scalar row; (7.3) pointer; §2 basis 𝒪₂ | CW3-errata §2.2 items 5, 8, 10; CW3 OC-7, OC-9, OC-11; WP8-F-v3 IF-F9; CW7-errata §2.1; WP5-v4 IF-R13-8 via WP5-AUD IF-AUD-8 |
| §19.1′ WP1-v3 | [E11] O(α²) list; [E13] Si window [CALC]; GaAs low-T inputs | IF-CW3-8; COMP-PAER IF-CP-1; IF-CW2-5 |
| §19.6 addenda | IF6-10 pointer; GAP-EF IF-EF2 pointer | COMP-PAER IF-CP-1; GAP-EF-v2 IF-EF2 |
| §19.2 WP2-v3 | §5.2″ core part; §12 item 8; §12 gaps/IF-10/IF-13; L4 add-on AE rule; G3 validity columns; anharmonic template | CW2-errata §2 items 3, 10, 13; IF-CW2-1, IF-CW2-4 |
| §19.3 WP3-v3 | §M4 (iv″b); J8 E^{Mig}_3; IF-13/J3; N1 range; Migdal phase −i; §M9 Si window; §M7 finite-q vertex | CW3-errata item 6; CW2-errata item 12; CW2 OC-11; IF-CW2-6; IF-CW4-4; COMP-PAER IF-CP-1, IF-CP-3 |
| §19.4 WP4-v3 | OW4-1/I1 (G5′) withdrawal; Dirac running α̃; I12/L15 L^{BCS}; 1/(2\|𝐒\|); RG7 t̄_esc; YIG a; η_pb source | CW3-errata items 22, 23; CW4 OC-12 + CW4-errata IF-CW4-1; CW7-errata §2.1 + WP8-F-v3 IF-F8; CW6-errata OC-CW6-7; WP8-U-v3 IF-U7; CMPMC-DEV IF-DEV-1 |
| §19.5 WP5-v4 + WP5 specs | A-4/(W11) D′; A-4/E §6 constraint; A-12; θ_coll σ_ln 0.1; θ_𝒦; quench protocol; B-1; B-2; A-6/C41; §6.3/C35; §1.5 sampler; (W17)/K_ν; (W15); θ_𝔉; §6.4 asymptotics; §6.4(ii)–(iii); Holstein seeds; QD readout; gap-release law; yield row; CMPMC presets | CW5-errata §B OC-1, OC-2, OC-4, OC-9, OC-10; CW5 OC-3, OC-6, OC-8; WP5-AUD §2/D-3, D-5, D-14; CW3 OC-1; CW3-errata items 2, 3; GAP-EF-v2-errata IF-EF1; GAP-EF-v2 IF-EF2; IF-CW4-5, -7; IF-CW5-1; CMPMC-AUD IF-AUD-6 |
| §19.6 WP6-v3 | §5.2 WP5-AUD rows (with σ_ln 0.1 and θ_exc); §6 exact constraint; θ_U, θ_τ, θ_{R-k}; θ_ζ, θ_ζg, θ_pos, F_NR, θ_Ssurf; θ_esc^{film}; magnon/SC/seeding rows; §4.5 G8′; §11 OW6-1/3/6; §4.2 (P) leakage; r_mat; Dirac re-plot; SC Δ nuisance; θ_𝔉; q-resolved S | WP5-AUD D-6, §3.2; CW5 OC-8, IF-CW5-2; CW6-errata OC-CW6-5, OC-CW6-7; CW7-errata §2.1; IF-CW4-6; CW4-errata IF-CW4-1; CW3-errata item 3; IF-CW7-9 |
| §19.7 WP7-B1-v2 | G-A2; G-X6/E10b/A6/I5/E12/E5/E10a pointers; Migdal phase | CW4 OC-2; CW4-errata §B; IF-CW4-4 |
| §19.8 WP7-B2-v2 | §2.2 (i) O(σ_M/M̄); §11 gap pointers; IF-B2-11 | CW2 OC-8; CW2-errata §2; CW4 OC-8, OC-9; IF-CW3-6 |
| §19.9 WP7-D-v2 | §1.5; §1.7/IF-D12; §1.8; IF-D10; §3.4; §4.1; §2.5 massive ν̃; §2.5 charged current | CW3-errata items 13, 15, 20, §1.13; CW3 OC-16…19 |
| §19.10 WP7-T-v2 | G-T5; G-T1 α_ohm; G-T2/§4.2 verdicts; L30 status; IF-T9 | CW5 OC-11; IF-CW5-6; CW5-errata §A21, §A23, L30 row, OC-9 |
| §19.11 WP7-E-v3 | (E7)–(E8); (E13)/§6 constraint; θ_coll; θ_X → θ_exc; N_a; p_surv; G-E4/IF-E7; (B-b); Theorem E-2/G-E2/G-E9; IF-E9; NTL spectrum; gap channel | CW5-errata OC-1; WP5-AUD D-3; CW5 OC-6, OC-8; SOTA R13 pending item; CW6-errata OC-CW6-3, IF-CW6-2; IF-CW5-7; GAP-EF-v2-errata IF-EF4; CMPMC-AUD IF-AUD-5; CMPMC-DEV IF-DEV-3 |
| §19.12 WP8-R v1 | SUPERSEDED by v2; v2 read with CW6-errata §B4 | CW6 OC-CW6-1; CW6-errata §B4 |
| §19.13 WP8-U | v4 rows 1543, 3182 (ZrTe₅), 1619, 3181 (Al), Nb rows; U7/IF-U10/LU3; shear-order fix; reading rule | CW4-errata §B OC-11; IF-CW4-2; CW6-errata OC-CW6-4 vs WP8-U-v3 §10; WP8-U-v3 §0 row 10, §1.3 V5′ |
| §19.14 WP8-F | v3 supersedes; (4.2) tanδ₀; §2.8(d); v3 additions CLAIMED | WP8-F-v3 header; CW5-errata OC-12; WP5-AUD D-17; CW7-errata §5 |
| §19.15 R14/R16 returns | WP5-AUD read through OC-1…OC-8; GAP-EF v1 superseded; CW returns through errata; CW7 §12 not merged | CW5 §1; GAP-EF-v2 header; errata headers; brief item 4 |
| §19.16 renames | θ_X → θ_exc and 33 further N rows (see NOTATION clash table) | NOTATION "Rows added R14–R16" (this merge) |

### A2. LIMITS.md
| Section → row | Edit | Source item |
|---|---|---|
| v3 status preamble | ✎R16 convention; R1-L17 relabel note | brief (two L17 rows) |
| v3 table → L4 | note: LST data cross-check ≤ 1.2% (LU1 merged) | CW7 owed "LIMITS L4" (unchanged by CW7-errata §2.2); WP8-U-v3 §10 |
| v3 → L5 | leading corrections (CW2.3)–(CW2.7); 0.16 [E] stands | CW2-errata §2 item 10 |
| v3 → L7c | (4.8) 2× CONFIRMED, rate unaffected, (4.9) inherits | CW2 OC-1 (unchanged) |
| v3 → L8 | Si window [CALC] pointer | COMP-PAER IF-CP-1 (CLAIMED) |
| v3 → L9b | aγγ tensor form | CW3 OC-11 (unchanged), L9b′ |
| v3 → L15 | resummed L^{BCS} (8.1); y < 3.8 mask | CW4 OC-12; CW4-errata IF-CW4-1; CW7-errata §2.1 |
| v3 → L16 | "re-plot = RG10" replaced | CW4 OC-10 (unchanged) |
| v3 → L17 | relaxed ch = e (CW3.4) text; status | CW3-errata §2.2 item 10 (target: the bounds-table L17) |
| v3 → L23 | (EF7) note; renewal asymptotics | GAP-EF-v2 L23 ✎ (unchanged in errata); CW5-errata §B OC-10 |
| WP7-T → L30 | source (Pushkarov; Andreev–Lifshitz flagged); exponent DERIVED; T < Δ_dfn law | CW5 OC-11; CW5-errata §B L30 row |
| WP7-T → L32 | tanδ₀ values | CW5-errata §B OC-12; L32 row |
| WP7-E → L33, L34 | space-charge field; emission locality | CW6-errata §B2 OC-CW6-8 |
| WP7-E → L36 | κ_cal(r_coll) clause; calibration-energy scope; (B-b) unsupported + widening; p_surv 0.47 (0.4748); TRIM conditional | WP5-AUD L36 ✎; CW6-errata OC-CW6-2; CW5 OC-6; CW5 L36 ✎ (unchanged) |
| WP7-E → L37 | t_win validity; (CW5-4) and (E.3)–(E.6) | WP5-AUD L37 ✎; CW5-errata §B L37; OC-4 |
| WP7-E → L38 | Chain (AUD-1); Validity OC-5 (errata, incl. (E.2)); Status DERIVED + **REFEREED recorded**; g_Luke moved to the Source cell; leading correction c_X, two-bias inversion | WP5-AUD §2, D-3; CW5-errata §B OC-5, A6; CW6-errata B3 CW6-L5 |
| WP7-E → Interfaces | IF-E7 answered; IF-E9 closed at formula level | WP8-R-v2 §6; GAP-EF-v2-errata IF-EF4 |
| WP7 → Numbers carried (isotope) | mK ≥ 6.3×10³ derived; +9% [E]; low-T α GAP | CW2-errata §2 item 7 |
| WP7-B2 → B2-L1, B2-L3, B2-L4, B2-L5 | caveat cells replaced | CW2-errata §2 items 2, 4, 6; CW2 OC-5 (unchanged) |
| WP7-B2 → B2-L6, B2-L7 | Larmor citation [FT]; AFM weight; neutron no-go | CW4 OC-8, OC-9 (unchanged) |
| WP7-B1 → LB1-5, LB1-6, LB1-8, LB1-10, LB1-11, LB1-13 | status / caveat / leading-correction cells | CW4 OC-3, OC-4 (unchanged); CW4-errata §B OC-1, OC-5, OC-6, OC-7 |
| WP7-D → L-D1, L-D3, L-D4, L-D5, L-D8, L-D10, L-D11 | status / caveat cells | CW3-errata §2.2 items 12, 15; CW3 OC-14, OC-16, OC-17, OC-18, OC-19 (unchanged) |
| new section "R14–R16" → preamble | sources, status rule, label decision, not-merged list | brief; CONVENTIONS §13 row 30 (this merge) |
| → L43 | 2303.02196 Si NR yield row, OPEN | WP5-AUD "Proposed LIMITS rows" (new, coordinator assigns) |
| → L44, L45, L46 | α_ohm, renewal, gap release | CW5-errata §B rows "new (α_ohm)", "new (renewal)", "new (gap release)" |
| → L39–L42 | WP8-R-v2 rows; L40 re-issued; L41 + CMPMC-DEV source; L42 merged with CW5 L42 ✎ | WP8-R-v2 "Proposed LIMITS rows"; CW6-errata §B3; CMPMC-DEV IF-DEV-1; CW5-errata §B L42; CW6-errata §B4 §0 row 6 |
| → L-F1…L-F4 | WP8-F-v3 rows | WP8-F-v3 "Proposed LIMITS rows"; CW7-errata §2.3 |
| → LU2′, LU4′, LU5′, LT1–LT3 | WP8-U-v3 §10 rows; LT1–LT3 text from R14 WP8-U-top (as WP8-U-v3 §10 directs: "as there"), LT1 with V5′ | WP8-U-v3 §10; returns/R14/WP8-U-top.md l.396–398 |
| → L-EF1…L-EF5 | GAP-EF-v2 rows (errata re-issued L-EF1–L-EF4) | GAP-EF-v2-errata §3; GAP-EF-v2 (L-EF5) |
| → CW2-L1…L5 | re-issued rows | CW2-errata §2 item 15 |
| → CW3 rows | L-D10′, L-O2, L9b′ (CW3); L-D13, L-D11′, L17′, L-Fano (errata) | CW3 "Proposed LIMITS rows"; CW3-errata §2.5 |
| → CW4-a…g | b, c, d, g re-issued; a, e, f with [FT per VER-CW4] | CW4-errata §B |
| → CW6-L1…L6 | re-issued rows; CW6-L4 absorbs LU3 | CW6-errata §B3 |
| → L-H1…L-H4 | re-issued rows | CW7-errata §2.3 |
| → CMPMC-AUD-L1…L5, CMPMC-DEV-L1…L4 | relabelled from AUD-L, DEV-L | CMPMC-AUD, CMPMC-DEV "Proposed LIMITS rows" |
| → L8-N1, L8-N2, L9-N1 | COMP-PAER rows | COMP-PAER "Proposed LIMITS rows" |
| → Withdrawn list | per package | errata closing tables; WP8-U-v3 §5, §10; WP8-F-v3; CMPMC; COMP-PAER |
| R1 table → L17 | relabelled R1-L17 | brief ("two rows labelled L17"); CW3-errata §2.2 item 10 |

### A3. NOTATION.md
| Section → row | Edit | Source item |
|---|---|---|
| §G → 𝐍 | replaced by the A-2 vector, N_eh derived | WP5-v4 IF-R13-1 (A-2); WP5-AUD D-15, IF-AUD-7 |
| §G → E_st, …, N_trap | N_trap restricted to before t_pr | WP5-v4 IF-R13-1 (A-15) |
| §G → Y_H | Y_H(t_win) = NR/ER heat-signal ratio, exact form | WP5-v4 IF-R13-1 (A-4); CW5-errata OC-1 |
| §C → 𝔉_{Λ₀,ν}, c_ν^F | → 𝔉_b, c_b^F (rate units; (P5) condition) | CW3-errata §2.2 item 4 |
| "Rows added WP7-E" → nuisance row | θ_X → θ_exc (definition: type T on r_g^{NR}, r_g^{ER}) | SOTA R13 pending item; LE-164; CW5 IF-CW5-2; WP8-R-v2 IF-R2 |
| new "Rows added R14–R16" | ≈ 150 symbols in 6 groups (cascade/yields; lattice; architecture; spin/SC/QD; transport; FOM/materials; PAER) | Symbols tables of WP5-AUD, CW2 (+ errata §2 item 14), CW3 (+ errata §2.4), CW4, CW5 (+ errata §E), CW6, CW7 (+ errata Symbols), GAP-EF-v2 (+ errata IF-EF5), WP8-R-v2, WP8-U-v3 §8, WP8-F-v3, CMPMC-AUD, CMPMC-DEV, COMP-PAER |
| new "Clashes resolved (R14–R16)" | 38 renames + ⚠ list + same-object list | grep of NOTATION v4 + all R14–R16 symbol tables (this merge) |
Check: code/NOTATION-APPLY/audit.py 26/26 PASS (rerun after the edits).

### A4. CONVENTIONS.md
| Section → row | Edit | Source item |
|---|---|---|
| §7 | 𝒪₂ sentence → 17th row 𝔳²_s | CW3 OC-9 (unchanged), IF-CW3-5 |
| §13 row 29 | r_mat and profile/envelope, signed-elasticity version | CW7-errata §2.1 (re-issued; supersedes CW7's row 29), IF-CW7-7, IF-ERR7-4; closes LE-160 |
| §13 row 30 | LIMITS labels R14–R16 | GAP-EF-v2 IF-EF7; LE-168; brief (L17, L39–L42); CMPMC/WP5-AUD label clash (this merge) |
| §13 row 31 | status after a single verification (CLAIMED + VERIFIED) | brief ("Statuses follow CONVENTIONS §12 …") |
| "R16 amendments" → [DB] | tag, rank, V1–V6, JARVIS shear order | CW7-errata §2.1 (pointer to WP8-U-v3 §1.3); WP8-U-v3 IF-U11; closes the IF-U1/LE-7 vetting-rule item |
| "R16 amendments" → status word | CLAIMED + VERIFIED | §13 row 31 |
| "R16 amendments" → §7 basis | 17 rows | CW3 §3.1 |
| "R16 amendments" → §11 ref=CDW | adopted (proposed by CW3) | IF-CW3-6 (unchanged in CW3-errata §2.3 except wording), CW3-errata §1.13 LE-81 pitfall (1) |
| "R16 amendments" → WP8 table reading rule | last superseding row wins | WP8-U-v3 header; VER-CW7 §A via CW7-errata §1.1 |

### A5. state/SOTA.md
| Section → line | Edit | Source item |
|---|---|---|
| R5 WP3 "Migdal" line | annotation: 2603.13052 (4.8) CONFIRMED 2×, rate unaffected | CW2 OC-9 (unchanged) |
| R11 REF-WP7-D "UNRESOLVED" line | annotation: SOTA ratings (2109.08168 Eq. (3) REFUTED; PDF Eq. (16); 1306.6089; 2501.05504; 2011.01940) | CW3-errata §2.2 item 21 |
| R13 "Provisional flag" | marked LIFTED | WP5-AUD §5; WP8-F-v3 header; WP8-R-v2 header |
| R13 returns → WP8-R line | annotation: superseded by WP8-R-v2 | CW6 OC-CW6-1 |
| R13 returns → WP8-U, WP8-F lines | annotation: superseded by WP8-U-v3 + table v4 / WP8-F-v3 | WP8-U-v3, WP8-F-v3 headers; CW7-errata §2.1 SOTA text |
| new "R14–R16 consolidated state" | one line per result with status (WP5-AUD, HV verdict, L38, GAP-EF-v2, EF-LIT, CW2…CW7, WP8 block, CMPMC-AUD, CMPMC-DEV, COMP-PAER); IF-R6 statement; WP8 block | WP5-AUD IF-AUD-6 as corrected by CW5 OC-7; GAP-EF-v2 IF-EF6; CW6 OC-CW6-6 (unchanged; shell numbers from CW6-errata B1); CW7-errata §2.1 SOTA text; closure tables; CMPMC/COMP-PAER §0 |
| same block → cross-cutting | JARVIS C₄₄/C₆₆ shear-order swap; CMPMC Kaplan-buffer bug; published-paper errors confirmed (and items checked and not errors) | WP8-U-v3 §0 row 10, §1.3 V5′, §4.1′, CW7-C33/C34; CMPMC-DEV §3 f61d710, IF-DEV-5; CW2 §16, §21; CW3-errata item 21; CW4-errata OC-3, §C; GAP-EF-v2-errata L-EF1; WP8-U-v3 §5; CMPMC-AUD §7 |
| same block → open conflicts, next | pointers | §C below |

### A6. state/LOOSE-ENDS.md
| Section | Edit | Source item |
|---|---|---|
| §1 ledger, ID cell of every row LE-1…179 except LE-173 | status + pointer (178 rows) | as listed in the cells: WP5-AUD; CW5 §1 (LE-22); GAP-EF-v2 + errata; WP8-U-v3; WP8-R-v2; COMP-PAER; CMPMC-AUD/DEV; CW2 §5; CW3-errata §2.1; CW4-errata A17; CW5-errata A0; CW6-errata OC-CW6-9; CW7-errata §0; this merge (LE-164, 165, 166, 168) |
| new §4 | status summary, counts, rows not closed by anything | brief ("List any row that is not closed by anything") |

### A7. FRAMEWORK.md (status updates only)
| Section | Edit | Source item |
|---|---|---|
| after "Order: WP0 first …" | status line WP0–WP6, WP5 v4, CW2–CW7, CW1, M1 tier B/H | WP5-AUD; CW5 §1; COMP-PAER §0; CW closure tables |
| WP7-E "Output" bullet | status: WP5-AUD + WP5-v4 REFEREED; GAP-EF-v2 REFEREED | CW5 §1 "Status"; IF-CW5-9 |
| WP8 bullet | status: WP8-U-v3/F-v3/R-v2; WP8-S not final | WP8-U-v3, WP8-F-v3, WP8-R-v2 headers; CW7-errata §5 |
| WP8-R bullet | status: go/no-go outcome | WP8-R-v2 §0 with CW6-errata §B4 |

### A8. registry.md (status updates only)
| Row | Edit | Source item |
|---|---|---|
| Data-calibrated optical-limit estimate | used in COMP-PAER [E] with ℱ_ρ | COMP-PAER §0, IF-CP-3 |
| ZG supercell route | tier H FORMULATED | COMP-PAER §8 |
| Sector expansions WP1–WP6 | REFEREED; CW2–CW7 CLAIMED + VERIFIED | SOTA; CONVENTIONS §13 row 31 |
| Low-T defect quantum kinetics | covered by WP7-T + CW5 | FRAMEWORK WP7; CW5 §3 |

## B. Checks run once at the end (code/*/checks.py of the merged packages; serial, OMP_NUM_THREADS=1, PYTHONDONTWRITEBYTECODE=1)
| Package | Script | Result | Time |
|---|---|---|---|
| WP5-AUD | code/WP5-AUD/checks.py | 27/27 PASS | 2 s |
| GAP-EF-v2 | code/GAP-EF-v2/checks.py | 32/32 PASS | 20 s |
| CW2 | code/CW2/checks.py | 32/32 PASS | 12 s |
| CW3 | code/CW3/checks.py | 45/45 PASS | 11 s |
| CW4 | code/CW4/checks.py | 24/24 PASS | 2 s |
| CW5 | code/CW5/checks.py | 26/26 PASS | 4 s |
| CW6 (= WP8-R-v2) | code/CW6/checks.py | 62/62 PASS | 7 s |
| CW7 (= WP8-U-v3, table v4, WP8-F-v3) | code/CW7/checks.py | 40/40 PASS | 4 s |
| WP8-R v1 (R13) | code/WP8-R/checks.py | 48/48 PASS | 1 s |
| WP8-U v1 (R13) | code/WP8-U/checks.py | 23 PASS, 0 FAIL, 16 FLAG (as recorded in R13) | < 1 s |
| WP8-F v1 (R13) | code/WP8-F/checks.py | 39/39 PASS | 4 s |
| NOTATION audit | code/NOTATION-APPLY/audit.py | 26/26 PASS | — |
Not run (no checks.py): CMPMC-AUD (code/CMPMC-AUD/run_tests.sh needs a CMPMC build; CMPMC-DEV reports 16/16 ctest at 3d43a02) and COMP-PAER (QE outputs only). `git status`
after the runs showed no file created or modified under code/.

## C. Conflicts not settled (for the coordinator)
1. **ZrTe₅ Δ_D value.** WP8-U-v3 §5 ("the referees agree on the value … Δ_D = 11.75 meV") and table v4 rows 1543/3182 keep "11.75 (exp [52])"; CW4-errata §B OC-11(a)
   (verified against VER-CW4 V11 and re-read in full text) says the 11.75 meV is not in [52] (1603.05351 reports no gap) and the documented value is 11.8 meV (DFT, NR). Both
   agree Δ is the half-gap. WP8-U-v3 is later in the brief's order of authority but did not address CW4's finding. Not settled: OC-11 is recorded as owed against v4
   (CORRECTIONS §19.13) and the conflict is flagged in SOTA. Decide which value the table carries.
2. **WP8-U LU3.** WP8-U-v3 §10 withdraws LU3 until its source is read in full text; CW6-errata OC-CW6-4 (earlier in the order) re-sources it on 2408.04732 [FT] and upgrades its
   status. Settled for LIMITS by authority order plus content: LU3 is withdrawn as a label and its content enters as CW6-L4 (= CMPMC-AUD-L5). Confirm.
3. **Al Δ_BCS in table v4.** v4 row 1619 still carries 0.3 meV (film-like) as the Al value; row 3181 flags it. CW4-errata OC-11(b) adds a bulk 0.18 meV [E] row. Owed
   against v4 (CORRECTIONS §19.13); no conflict of substance, but the table must be updated before WP8-S uses Al.
4. **Status of the ERR-CW7 additions.** The shear-order fix, c_NR1, L-F4 and the polar-bound and 𝓠_Mig changes come from REF-WP8-S-A/B findings applied by ERR-CW7; no
   verifier has read them. Recorded as CLAIMED (R×2 owed, IF-ERR7-6). The coordinator may prefer to count REF-WP8-S as their R×2.
5. **ref=CDW** (CW3 IF-CW3-6) was "proposed"; adopted here as a CONVENTIONS R16 amendment because the verified return depends on it. Revert if the coordinator prefers to
   keep it proposed.
6. **LE-12** default S4 screen (1 /(kg·day·keV) below 1 keV): applied to every survivor by WP8-U-v3, but the closure criterion also asks for the user's confirmation of the default,
   which no input records. Marked CLOSED with that caveat.

## D. Owed edits to files this brief does not authorise (not applied)
- code/ENV.md: CMPMC [CALC] gate paer-sota ≥ 3d43a02, default surfaces diffuse, demo polynomials only with opt-in (CMPMC-AUD IF-AUD-1, CMPMC-DEV IF-DEV-4); check R15-era runs
  for the Kaplan-buffer bug (IF-DEV-5).
- CONTROLS.md C4: with SG15 NC pseudopotentials the plane-wave f-sum reaches only 0.81 → 0.89 of q²/2m_e; a C4 test must add the non-local commutator term and extrapolate in
  N_m (COMP-PAER IF-CP-4).
- returns (never edited): every item in state/CORRECTIONS.md §19.
- briefs/LAUNCHES: R17 R×2 of ERR-CW7 + WP8-U-v3 + WP8-F-v3 (IF-ERR7-6, IF-CW7-8); WP8-S revision reading table v4 (IF-ERR7-1, IF-U13); literature agent items IF-ERR7-5 / IF-U14.

Note: campaign/ is in .gitignore; the eight edited coordinator files are tracked, but this log is untracked and ignored (it needs `git add -f` to be committed). Nothing was committed.
