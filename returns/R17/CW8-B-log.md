# R17 / CW8-B log: framework bookkeeping closures (LE-164 remainder, 167, 169, 170, 174, 175)

Date 2026-11-01. Brief: briefs/R17/CW8-B.md. No literature download was needed: no new arXiv ID was introduced, every cited ID was already in the ledgers, and no PDFs were fetched, so none had to be deleted. No commit was made. Shared files (LIMITS.md, state/LOOSE-ENDS.md) were changed only by exact-string Edit replacements, each made right after re-reading its region. The one exception: state/CORRECTIONS.md §19.17 had three in-cell text fixes applied by a scripted exact-string replace (count-checked).

## Edits (file → section → source)
| # | File | Section | Edit | Source |
|---|---|---|---|---|
| 1 | NOTATION.md | new "Rows added R17" (end of file) | 14 rows: 𝒦_cap, 𝔱 = tr_j / pl, Γ_pl, ℋ_eff, R_final^{min}/𝔅₀^{min}, P(𝐌,t\|Λ), Γ^{out}/Γ^{in}, α_E, 𝓃_pair, ℋ_nuc, U_FP/U_EDFT (source-only), 𝓜⁰_GS/𝓜¹_GS/𝓜¹_X, F_loss, θ_Z/θ_dense; clash table (n_pair → 𝓃_pair vs C4 n_pair; a_X → a_x; W_{GG′} → W^{scr}_{GG′}; Z_qp same object; c_ν^F → §E c_b^F) | WP5-v4 "Symbols introduced/used" (R13 and R8 tables); WP5-AUD Symbols; GAP-EF-v2 (EF13) for ℋ_eff |
| 2 | state/CORRECTIONS.md | §19.5 (2 rows appended) | WP5-v4 renames (N); IF-R8-7 none owed | NOTATION R17; WP5-v4 IF-R8-7, WP4-v3 K27/I2 |
| 3 | LIMITS.md | v3 header bullets | R17 bullet (✎R17 meaning, register pointer) | this pass |
| 4 | LIMITS.md | L20 Note | E_R,th 352/395 eV soft pointer (IF-R8-8); ✎R17 A-8 implicit assumptions | WP5-v4 "Proposed LIMITS rows" L20; WP5-AUD §1.1 A-8 |
| 5 | LIMITS.md | L21 Note | ✎R17 marked observable law, t_pr marginal | WP5-v4 proposed L21 (A-16); WP5-AUD §1.1 |
| 6 | LIMITS.md | L22 Note | ✎R17 f_DF combination with κ_cal(r_coll), OC-1 D′, bound only under (B-a)–(B-d), quench | WP5-v4 proposed L22 (A-9); WP5-AUD D-3, D-13; CW5-errata OC-1; CW6-errata OC-CW6-2 |
| 7 | LIMITS.md | L23 Note | ✎R17 (W14) validity per A-10, ℋ_eff, F_meas^{obs} | WP5-v4 proposed L23; WP5-AUD §1.1 A-10 |
| 8 | LIMITS.md | WP7-E subsection, new bullet before "Interfaces" | WP5 (W11) pointer to L37/L38 | WP5-v4 proposed row (W11); WP5-AUD (AUD-1); CW5-errata OC-1 |
| 9 | LIMITS.md | new "H6 exact-gap register (R17)" before the R1 table | 16 keyed rows (19 labels): derived statement, missing step, spec, LE row | CW3 §4.4–§4.10 (+errata), CW4 §12, §14, §19 (+errata A3, A13), CW5 §2.7, §3.1, §3.7 (+errata §A12, A0), GAP-EF-v2 §1.8–§1.10 |
| 10 | CONVENTIONS.md | §7 DM-side tensor bullet (R17 text) + new "R17 amendments" | 𝔘_C added as a two-body row (C, 𝔘); 𝔇^F, 𝔇^{pair} recorded as DM-side tensors, no target row | WP7-D-v2 §1.2, (D.8), §2.1 (F.1)–(F.2), (T.1)–(T.2), IF-D2; CW3-errata §2.2 item 20; WP0-v3 (1.1) |
| 11 | state/CORRECTIONS.md | new §19.17 | LE-174 routing table, 25 flags (18 with adoption text, 7 none owed) | WP7-D-v2, WP7-B1-v2, WP7-B2-v2, WP7-T-v2 "Interface flags"; WP8-F IF-F2/F5; WP8-U IF-U2/IF-U2′; WP5-v4 IF-R13-4 |
| 12 | state/SOTA.md | l.110 (F ≈ 0.121), l.116 (½εS_e), l.201 (η_pb) | [superseded R8 …] annotations | WP5-v4 IF-R8-8, IF-R8-7 |
| 13 | state/LOOSE-ENDS.md | §1b table | replaced by the R17 re-audit (status per LE row) | §1 status cells; AUDIT.md §7–§8; SOTA WP7 merge block (catalog A 77 · C 14) |
| 14 | state/LOOSE-ENDS.md | §1 ID cells LE-164, 167, 169, 170, 174, 175 | CLOSED with pointers | this pass |
| 15 | state/LOOSE-ENDS.md | §4 end | dated R17 closure line (counts sentence left to CW8-LIT) | this pass |

## Checks
- IF-R8-7: N_qp = 2 for ω < 4Δ_BCS appears in WP4-v3 §4.6 K27 and I2, in WP5-v4 §5 and in LIMITS L41. It was missing only from SOTA (now annotated). Consistent.
- IF-R8-8: 352/395 eV soft is in SOTA l.111 and LIMITS L22 (and now L20). The L20 ½εS_e replacement and the L23 "no evidential weight" were already in LIMITS. SOTA l.110 and l.116 were stale and are now annotated. Born ≈ 15/35 is in SOTA l.302/349. Consistent.
- Collision check (grep NOTATION) for every new symbol: the only hard collision was n_pair (C4); a_X duplicated a_x. ⚠ marks were added where a decorator rule applies.
- code/NOTATION-APPLY/audit.py checks physics prefactors, not symbols. It is unaffected (26/26 PASS before the edits).

## Open judgement calls (for the coordinator)
- 𝔘_C was put inside the basis as a two-body row, not left outside. The alternative: keep the basis one-body and treat 𝔘_C as a WP7-D-local operator.
- L30 register (a): the spec "evaluate the CW5-C4 integral coefficient" is stated in this pass. It is not in the return.
- CONVENTIONS §7: "R̃_{𝔘c} ≠ 0" is not derived anywhere, so the text is conditional ("applies if").
- §19.17 adoption texts restate the flag cells. They are reading rules, not new derivations.
