# Three-volume edition: notation table (NOTATION.md), GLOSSARY.md, INDEX.md, generated App. B lists

Unit: book/NOTATION.md (source of tex/appB/B-1*.tex), book/GLOSSARY.md, book/INDEX.md. No tex file was edited by hand; tex/appB/B-1.tex, B-1-vol{1,2,3}.tex and B-3.tex were regenerated at the end (last section). Line numbers are those of NOTATION.md before the edit.

## Method

Every symbol of every row (1540 rows) was checked against the math of the tex outside tex/appB and tex/xref, in two ways: the tokenizer of ledgers/check_notation.py (row keys and index-subscript variants), and the row's rendering by gen_B1.py (the tex spelling of the symbol) searched as a normalized string (braces, spacing, \mathrm, \vect, \max/\mathrm{max}, \mathcal/\mathscr folded) with symbol boundaries. Each section was located by its \section label (labels are stable: sec:3.4, app:E.n keep their numbers wherever the file sits now). The same scan of the one-volume tex (commit 7696d03) separated symbols that the edition removed from symbols that the scan cannot see (macros such as \FDM, prose-only rows); every candidate was then checked by grep with spelling variants. A symbol counts as removed only when no spelling of it is left in any chapter, appendix or front file; a symbol whose only remaining hits are other quantities with the same letters (p_Qν for p_Q, v_χ,max for v_χ, the Madelung α_M of E.10, the electronic σ_e of 19.3, the halo v₀) counts as removed.

Removed symbols get first use "— (removed in the three-volume edition)"; gen_B1.py drops such rows. Where only some symbols of a row went, the row was split: the live symbols keep the row (meaning clauses and units of the removed ones taken out, nothing else reworded), and the removed symbols follow in a row of their own with their original clauses. No symbol was respelled.

## Rows marked removed (whole row)

| line | symbol | old first use | evidence |
|---|---|---|---|
| 626 | E_bind | 7.2 | Cooper problem cut from s7-2 (ch07 log) |
| 801 | f^L₁, f^L₂ | 10.3 | no f^L in s10-3 or anywhere |
| 859 | ℛ_IP, ℛ_{RPA+LF}, ℛ_source | 10.9 | used only by the App. F rows of lim:10.9a/b, removed (ch10 log) |
| 931 | 𝐅_e | 12.3 | no bold F_e left (12.3 boost derivation cut) |
| 932 | P̂^W_I | 12.3 | Wannier-boost passage of 12.3 cut (ch12 log) |
| 933 | A^W_cv | 12.3 | same |
| 934 | W_v | 12.3 | same |
| 940 | Z*_at(ω) | 12.6 | free-atom limit cut from 12.6 (ch12 log) |
| 945 | j_ℓ | 12.2 | 12.2 Bessel sentence cut; E.2 writes j_l (row j_l, E.2) |
| 951 | P̂_occ | 12.3 | same |
| 973 | σ_γ | 12.6 | photoabsorption form cut from 12.6 |
| 1075 | q_1BZ | 14.4 | YIG data-analysis note cut from 14.4 |
| 1086 | ω_soft, γ_soft | 14.5 | Ginzburg–Landau oscillator cut from 14.5 |
| 1087 | χ_θ, α_me, α_M, m_P | 14.5 | Røising free energy eq:14.5-GL cut (α_M of E.10 is the Madelung constant) |
| 1462 | v₀ (E.16) | E.16 | two-band test model cut from E.16 (during this pass) |
| 1533 | v_χ | E.16 | boosted recast cut from E.16 (during this pass; v_χ,max of 10.9 is its own row) |
| 1541 | N_src, N_corr | E.20 | rescaling counts cut from E.20 |

## Rows split: removed symbols moved to a row of their own

| line | live symbols (first use) | removed symbols |
|---|---|---|
| 325 | E_HOMO (D.5) | E_LUMO |
| 412 | φ_tot(q, ω) (4.4) | φ_tot,G, φ_ext,G |
| 503 | Ψ^nuc_i(u) (5.1; was 5.1; D.13 (Ψ̃^nuc_i)) | Ψ̃^nuc_i(u) |
| 513 | a_c, K, M₁, M₂, ω_Q±, ω_0+ (5.2) | ω_X |
| 642 | c_kσ, c†_kσ, ψ_σ(r) (7.2 (D.20)) | n_kσ |
| 876 | s_Q (App. C.18 (moved from 11.1); was 11.1) | Δ_C, A_Z, p_Q |
| 877 | v_L, v_T, G_V, G_R (11.3 (moved from 11.1; caption of fig:11-limit-3b); was 11.1) | v_m |
| 884 | c_min (11.3) | q_osc |
| 955 | H_φ, g_φpp, g_φnn, c̃ (12.6) | σ_φ |
| 1000 | x_j, σ_j (13.7) | N_m |
| 1081 | 𝐋^ph_𝐐ν, 𝐋^ph_κ,𝐐ν, L^ph_z, 𝛍^ph_𝐐ν (14.5) | L^ph_x |
| 1106 | 𝔤_I, L^nor (15.1) | 𝔰_BCS |
| 1107 | L^cons, y, 𝔯_ε (15.1, 15.2) | L^bare, δ_𝔰 |
| 1116 | 𝔥(y′), 𝔨(ω), 𝔨̃, δ𝔤(y′) (D.39) | Y_tail |
| 1169 | ω‡, κ_PB, T_×, S_inst, T_frz (16.8) | κ_W |
| 1174 | Π (16.1) (16.1) | V_uc |
| 1182 | Õ, Õ_a, Õ_b, ñ_e, L_eff (16.5) | E_eff |
| 1230 | N_eh^step (18.3) | α_RK |
| 1246 | F_park (18.2) | σ_pair, σ_e, σ_h, F_ren |
| 1269 | ϵ_d, T^(e)_d, U (19.3) | U_FP, U_EDFT, W_max |
| 1288 | ℛ_TLS, ℛ_LEE, p_LEE, U_rel, E_st,0, f_ph (19.6) | E_slope |
| 1298 | N_mix, v_ph (20.2) | r_rms |
| 1535 | N_core, 𝐩_red (E.18) | 𝔯_W(𝐪, ω_e) |

All symbols named as removed in the unit logs were verified: U_FP, U_EDFT, W_max (19.3), E_slope (19.6), F_ren, σ_pair (with σ_e, σ_h of 18.2), κ_W (16.8), α_RK (18.3), E_bind (7.2), P̂^W_I, A^W_cv (12.3), 𝔯_W (E.18), 𝔰_BCS, L^bare, δ_𝔰 (15.1–15.2), the Wannier-boost symbols P̂^W_I, A^W_cv, P̂_occ, W_v, 𝐅_e (12.3): all gone and marked. Two named in the brief are still used and were retargeted, not removed: c̄_LA (still written in C.18 "Sect. 11.1 uses ⟨c_LA⟩, written c̄_LA", a sentence that is now stale, see Open items) and the Debye speeds v_L, v_T, G_V, G_R (moved into the caption of fig:11-limit-3b in 11.3). The elastic Debye temperature θ_D of 11.1 has no row of its own (row Θ_D, ω_D, "5.2 (Θ_D also 16.7)", stays correct); its Debye-mean speed v_m is removed.

## Rows retargeted (first use or meaning)

| line | symbol | old first use | new first use | meaning |
|---|---|---|---|---|
| 586 | Π^b_ν(Q, ω), Π^b | D.17 | 6.4 (moved from D.17, folded into 6.4) | "(D.17 only" → "(6.4 only" |
| 592 | E_band | D.17 | 6.4 (moved from D.17, folded into 6.4) | "(D.17 only" → "(6.4 only" |
| 864 | c̄_LA | 11.1 (also App. C.18) | App. C.18 (moved from 11.1) | unchanged |
| 935 | s^inc_κ(𝐐, ω) | D.33, 12.4 | 12.4 (moved from D.33; named in 12.1) | unchanged |
| 943 | α_pol(ω) | 12.6 | 16.5 (moved from 12.6) | unchanged |
| 1059 | ω_Kit, ω_Kit,i, ω_Kit,x, ω_Kit,y, N^dm_i, N^dm_x, N^dm_y, N^dm_z, H_u | 14.3 | unchanged | note "(ω_K is the Klein phonon energy)" → "(ω_K is the phonon energy of 18.4)" |
| 1191 | R̃^2D, R̃^2D_low, R̃^2D_bg, r_0 | 16.2 | unchanged | note "(r_K is the Klein coefficient of 18.4)" → "(r_K is the phonon number per pair of 18.4)" |
| 1225 | k₂; r_K, ω_K | 18.4 | unchanged | "phonon-loss coefficient and phonon energy of the Klein relation (14/5)E_g + r_Kω_K" → "mean number of phonons emitted above threshold per pair, and their energy ω_K = ω_AB, in ε_eh = E_g + 2Ē_res + r_Kω_K" (eq:18.4-shockley; the Klein relation was cut) |
| 1275 | Y_ph | 19.4 (derived 19.5) | 19.5 (moved from 19.4) | unchanged |

Also retargeted within the split rows above: s_Q (11.1 → App. C.18; Δ_C, A_Z, p_Q removed with the Zener-ratio paragraph), v_L, v_T, G_V, G_R (11.1 → 11.3), Ψ^nuc_i ("5.1; D.13 (Ψ̃^nuc_i)" → 5.1), and the meaning of Π (16.1) ("local to 16.1, D.41" → "D.41 → 16.1"). s^inc_κ follows the ch12 log ("point to sec:12.4 where the symbol is defined"): it is named first in 12.1 and defined in 12.4, D.33 no longer has it.

## First-use notes naming folded appendix sections

In the first-use cells, a parenthetical D.15, D.17, D.18, D.19, D.29, D.41 (folded into 5.6, 6.4, 6.5, 7.1, 10.1, 16.1) or D.14 (now the Fröhlich vertex only; the polar-crystal constants are defined in 5.5) is written "D.n → section"; the leading first-use section did not change. V^L(r) keeps "D.14 (6.2)" (still in D.14). Rows (old line: cell):

- 495 𝒞_κκ′(R, t), 𝒞_κκ′(t): "5.6 (derived D.15)" → "5.6 (derived D.15 → 5.6)"
- 532 𝐮_rel: "5.5 (also D.14, 6.2)" → "5.5 (also D.14 → 5.5, 6.2)"
- 533 C^an_κκ′, C^na_κκ′(Q̂), C₀: "5.5 (derived D.14)" → "5.5 (derived D.14 → 5.5)"
- 534 𝐳_ν: "5.5 (derived D.14)" → "5.5 (derived D.14 → 5.5)"
- 535 E^ad_ℰ(u, ℰ): "5.5 (derived D.14)" → "5.5 (derived D.14 → 5.5)"
- 536 ω_Tν, ω_Lν, ω_0ν: "5.5 (derived D.14)" → "5.5 (derived D.14 → 5.5)"
- 559 Π_ν(Q, ω): "6.4 (derived D.17)" → "6.4 (derived D.17 → 6.4)"
- 585 𝖣_ν(Q, ω), 𝖣: "6.4 (derived D.17)" → "6.4 (derived D.17 → 6.4)"
- 587 ω̃_Qν, ω^ren_Qν: "6.4 (derived D.17)" → "6.4 (derived D.17 → 6.4)"
- 589 ⟨…⟩_FS: "6.4 (derived D.17)" → "6.4 (derived D.17 → 6.4)"
- 593 ê_γ: "6.5 (also D.18)" → "6.5 (also D.18 → 6.5)"
- 594 𝐕̂, H_A: "6.5 (also D.18)" → "6.5 (also D.18 → 6.5)"
- 595 M^±_cvν(k, Q), M^±_cvν(k, q, Q): "6.5 (derived D.18); 13.2 (D.35)" → "6.5 (derived D.18 → 6.5); 13.2 (D.35)"
- 596 κ_ext: "6.5 (also D.18)" → "6.5 (also D.18 → 6.5)"
- 610 J^ex_AA(k), J^ex_AB(k): "7.1 (D.19)" → "7.1 (D.19 → 7.1)"
- 611 A_k, B_k: "7.1 (D.19)" → "7.1 (D.19 → 7.1)"
- 613 N_s: "7.1 (D.19)" → "7.1 (D.19 → 7.1)"
- 614 E_cl, E_gs: "7.1 (E_gs: 7.1, D.19)" → "7.1 (E_gs: 7.1, D.19 → 7.1)"
- 616 ζ_k: "7.1 (D.19)" → "7.1 (D.19 → 7.1)"
- 780 f_crys(q, ω): "10.1 (also D.29)" → "10.1 (also D.29 → 10.1)"
- 789 S̄⁰(q, ω): "10.1 (also D.29)" → "10.1 (also D.29 → 10.1)"
- 957 n_r(ω): "6.5 (moved from 12.6 at the Chap. 6 merge; also D.18)" → "6.5 (moved from 12.6 at the Chap. 6 merge; also D.18 → 6.5)"
- 1141 ε_pub: "16.1 (D.41)" → "16.1 (D.41 → 16.1)"
- 1142 B_D(s): "16.1 (D.41)" → "16.1 (D.41 → 16.1)"
- 1173 ε_D, ε_D,i, R̃_D, R_DD, F_med, ε_bg,xx, ε_bg,yy: "16.1 (D.41)" → "16.1 (D.41 → 16.1)"

## GLOSSARY.md and INDEX.md

Mechanical, pointer column only: D.15, D.17, D.18, D.19, D.29, D.41 (with or without "App.") → 5.6, 6.4, 6.5, 7.1, 10.1, 16.1, duplicates in the cell dropped ("6.4, App. D.17" → "6.4", "5.6 (D.15)" → "5.6"); "App. E.n", "App. D.4", "App. D.5", whose sections now sit in the chapters of Volume III (labels kept), → "E.n", "D.4", "D.5", as GLOSSARY.md already writes them. One hand case: GLOSSARY "C.6 (proof D.15; used 5.6)" → "C.6 (proof and use 5.6)". A dated note before each table says so. Changes: GLOSSARY.md 30 cells, INDEX.md 144 cells. No pointer to a section label that does not exist is left in either file. Entries whose subject was cut inside a surviving section (e.g. Cooper problem in 7.2) were not touched (not a pointer change).

<details><summary>Cells changed</summary>

- GLOSSARY.md:230 "4.9 (D.12; App. E.6)" → "4.9 (D.12; E.6)"
- GLOSSARY.md:393 "5.6 (D.15)" → "5.6"
- GLOSSARY.md:394 "5.6 (D.15)" → "5.6"
- GLOSSARY.md:395 "5.6 (D.15)" → "5.6"
- GLOSSARY.md:405 "D.15" → "5.6"
- GLOSSARY.md:433 "6.4 (D.17)" → "6.4"
- GLOSSARY.md:434 "6.4 (D.17)" → "6.4"
- GLOSSARY.md:436 "6.4 (D.17)" → "6.4"
- GLOSSARY.md:437 "6.4 (D.17)" → "6.4"
- GLOSSARY.md:438 "6.4 (D.17)" → "6.4"
- GLOSSARY.md:439 "6.4 (D.17)" → "6.4"
- GLOSSARY.md:440 "6.4 (D.17)" → "6.4"
- GLOSSARY.md:441 "6.5 (D.18)" → "6.5"
- GLOSSARY.md:443 "6.5 (D.18; 2.4)" → "6.5 (2.4)"
- GLOSSARY.md:444 "6.5 (D.18)" → "6.5"
- GLOSSARY.md:445 "6.5 (D.18)" → "6.5"
- GLOSSARY.md:446 "6.5 (D.18)" → "6.5"
- GLOSSARY.md:447 "6.5 (D.18)" → "6.5"
- GLOSSARY.md:462 "7.1 (D.19)" → "7.1"
- GLOSSARY.md:463 "7.1 (D.19)" → "7.1"
- GLOSSARY.md:464 "7.1 (D.19)" → "7.1"
- GLOSSARY.md:466 "7.1 (D.19)" → "7.1"
- GLOSSARY.md:467 "7.1 (D.19)" → "7.1"
- GLOSSARY.md:468 "7.1 (D.19)" → "7.1"
- GLOSSARY.md:617 "10.1 (D.29)" → "10.1"
- GLOSSARY.md:619 "10.1 (D.29)" → "10.1"
- GLOSSARY.md:851 "16.1 (D.41)" → "16.1"
- GLOSSARY.md:852 "16.1 (D.41)" → "16.1"
- GLOSSARY.md:853 "16.1 (D.41)" → "16.1"
- GLOSSARY.md:1140 "C.6 (proof D.15; used 5.6)" → "C.6 (proof and use 5.6)"
- INDEX.md:70 "App. E.4, 5.2" → "E.4, 5.2"
- INDEX.md:90 "App. E.6, 4.6" → "E.6, 4.6"
- INDEX.md:91 "App. E.8" → "E.8"
- INDEX.md:96 "App. E.2, App. E.7, 3.5" → "E.2, E.7, 3.5"
- INDEX.md:98 "6.4, App. D.17" → "6.4"
- INDEX.md:141 "App. E.12" → "E.12"
- INDEX.md:200 "16.1, App. D.41" → "16.1"
- INDEX.md:223 "App. D.5" → "D.5"
- INDEX.md:240 "App. E.4" → "E.4"
- INDEX.md:247 "App. E.6" → "E.6"
- INDEX.md:261 "App. C.6, 5.6, App. D.15" → "App. C.6, 5.6"
- INDEX.md:290 "App. E.4, 5.5" → "E.4, 5.5"
- INDEX.md:347 "App. E.1" → "E.1"
- INDEX.md:412 "App. E.1" → "E.1"
- INDEX.md:465 "App. E.12, 20.5" → "E.12, 20.5"
- INDEX.md:508 "App. D.5" → "D.5"
- INDEX.md:543 "App. E.3" → "E.3"
- INDEX.md:545 "App. E.9, 7.2" → "E.9, 7.2"
- INDEX.md:568 "App. A, App. E.7, 3.2, 10.1" → "App. A, E.7, 3.2, 10.1"
- INDEX.md:638 "App. D.15" → "5.6"
- INDEX.md:648 "App. D.15" → "5.6"
- INDEX.md:686 "App. E.4, 5.4" → "E.4, 5.4"
- INDEX.md:688 "App. E.1" → "E.1"
- INDEX.md:694 "3.4, App. D.5" → "3.4, D.5"
- INDEX.md:706 "App. E.9" → "E.9"
- INDEX.md:771 "5.6, App. D.15" → "5.6"
- INDEX.md:828 "6.4, App. D.17" → "6.4"
- INDEX.md:844 "App. E.1" → "E.1"
- INDEX.md:855 "App. E.4, App. C.18" → "E.4, App. C.18"
- INDEX.md:862 "3.4, App. D.5" → "3.4, D.5"
- INDEX.md:897 "App. E.5, 3.6" → "E.5, 3.6"
- INDEX.md:907 "App. E.9" → "E.9"
- INDEX.md:908 "6.4, App. D.17" → "6.4"
- INDEX.md:909 "App. E.5" → "E.5"
- INDEX.md:966 "App. E.9, 7.1" → "E.9, 7.1"
- INDEX.md:967 "App. D.4" → "D.4"
- INDEX.md:968 "3.4, App. D.4" → "3.4, D.4"
- INDEX.md:977 "App. E.1" → "E.1"
- INDEX.md:1062 "App. A, App. E.7, 4.3" → "App. A, E.7, 4.3"
- INDEX.md:1069 "App. E.2, App. E.7" → "E.2, E.7"
- INDEX.md:1085 "App. E.13" → "E.13"
- INDEX.md:1134 "App. D.4" → "D.4"
- INDEX.md:1138 "App. E.4, 5.2" → "E.4, 5.2"
- INDEX.md:1146 "App. E.10" → "E.10"
- INDEX.md:1172 "App. E.5, App. D.14, 6.2" → "E.5, App. D.14, 6.2"
- INDEX.md:1173 "App. D.4" → "D.4"
- INDEX.md:1205 "App. E.12" → "E.12"
- INDEX.md:1241 "App. E.11" → "E.11"
- INDEX.md:1271 "App. E.2" → "E.2"
- INDEX.md:1298 "App. E.8" → "E.8"
- INDEX.md:1302 "App. E.3, 4.8" → "E.3, 4.8"
- INDEX.md:1304 "App. E.6" → "E.6"
- INDEX.md:1306 "App. E.3" → "E.3"
- INDEX.md:1316 "6.5, App. D.18" → "6.5"
- INDEX.md:1337 "4.4, App. D.4" → "4.4, D.4"
- INDEX.md:1339 "App. D.4" → "D.4"
- INDEX.md:1341 "App. D.4" → "D.4"
- INDEX.md:1377 "3.4, App. D.5" → "3.4, D.5"
- INDEX.md:1382 "6.5, App. D.18" → "6.5"
- INDEX.md:1385 "7.1, App. D.19" → "7.1"
- INDEX.md:1389 "App. E.13" → "E.13"
- INDEX.md:1391 "App. E.1" → "E.1"
- INDEX.md:1393 "App. E.10, 5.6, 10.5" → "E.10, 5.6, 10.5"
- INDEX.md:1398 "App. E.9" → "E.9"
- INDEX.md:1424 "App. E.13, 18.1" → "E.13, 18.1"
- INDEX.md:1427 "App. E.3, 18.1" → "E.3, 18.1"
- INDEX.md:1440 "16.1, App. D.41" → "16.1"
- INDEX.md:1466 "6.5, App. D.18" → "6.5"
- INDEX.md:1470 "6.5, App. D.18" → "6.5"
- INDEX.md:1481 "App. E.11" → "E.11"
- INDEX.md:1516 "3.4, App. D.5" → "3.4, D.5"
- INDEX.md:1533 "App. E.12, 20.2" → "E.12, 20.2"
- INDEX.md:1547 "3.4, App. D.5" → "3.4, D.5"
- INDEX.md:1569 "App. E.1" → "E.1"
- INDEX.md:1601 "App. E.2" → "E.2"
- INDEX.md:1606 "4.5, App. C.8, 6.4, App. D.17" → "4.5, App. C.8, 6.4"
- INDEX.md:1608 "3.4, App. D.5" → "3.4, D.5"
- INDEX.md:1609 "3.4, App. D.5" → "3.4, D.5"
- INDEX.md:1611 "3.4, App. D.4" → "3.4, D.4"
- INDEX.md:1654 "App. E.1" → "E.1"
- INDEX.md:1708 "7.1, App. D.19" → "7.1"
- INDEX.md:1757 "3.4, App. D.5" → "3.4, D.5"
- INDEX.md:1758 "App. E.6, 4.4, 4.6" → "E.6, 4.4, 4.6"
- INDEX.md:1759 "App. E.2, 3.5" → "E.2, 3.5"
- INDEX.md:1781 "App. E.12, 6.3" → "E.12, 6.3"
- INDEX.md:1814 "App. E.10" → "E.10"
- INDEX.md:1823 "6.4, App. D.17" → "6.4"
- INDEX.md:1844 "App. E.9" → "E.9"
- INDEX.md:1908 "6.4, App. D.17" → "6.4"
- INDEX.md:1937 "App. E.11" → "E.11"
- INDEX.md:1954 "App. E.1, App. C.2" → "E.1, App. C.2"
- INDEX.md:2049 "App. E.2" → "E.2"
- INDEX.md:2069 "App. E.10" → "E.10"
- INDEX.md:2086 "App. E.2" → "E.2"
- INDEX.md:2119 "App. D.4" → "D.4"
- INDEX.md:2121 "App. E.10, App. C.20" → "E.10, App. C.20"
- INDEX.md:2155 "App. E.13" → "E.13"
- INDEX.md:2188 "App. E.2, App. E.7" → "E.2, E.7"
- INDEX.md:2189 "App. E.1" → "E.1"
- INDEX.md:2230 "App. E.12" → "E.12"
- INDEX.md:2269 "App. E.1, 3.5" → "E.1, 3.5"
- INDEX.md:2293 "App. E.3" → "E.3"
- INDEX.md:2358 "App. E.2, 3.5" → "E.2, 3.5"
- INDEX.md:2360 "App. E.2, 3.5" → "E.2, 3.5"
- INDEX.md:2361 "App. E.2" → "E.2"
- INDEX.md:2362 "App. E.2" → "E.2"
- INDEX.md:2363 "App. E.2" → "E.2"
- INDEX.md:2366 "App. E.2" → "E.2"
- INDEX.md:2370 "16.1, App. D.41" → "16.1"
- INDEX.md:2373 "App. E.1" → "E.1"
- INDEX.md:2387 "App. E.8, 5.7" → "E.8, 5.7"
- INDEX.md:2396 "App. E.3, 4.7" → "E.3, 4.7"
- INDEX.md:2397 "App. E.3, 4.7" → "E.3, 4.7"
- INDEX.md:2401 "App. E.3, App. E.13" → "E.3, E.13"
- INDEX.md:2454 "16.1, App. D.41" → "16.1"
- INDEX.md:2608 "App. E.8" → "E.8"
- INDEX.md:2613 "App. E.3, App. E.6, App. E.7, 3.4" → "E.3, E.6, E.7, 3.4"
- INDEX.md:2616 "App. E.3, 3.4" → "E.3, 3.4"
- INDEX.md:2659 "App. D.5" → "D.5"
- INDEX.md:2660 "App. E.12, App. E.13" → "E.12, E.13"
- INDEX.md:2662 "App. E.2, App. E.7, 3.5" → "E.2, E.7, 3.5"
- INDEX.md:2739 "App. D.5" → "D.5"
- INDEX.md:2744 "App. E.1" → "E.1"
- INDEX.md:2745 "App. E.1" → "E.1"
- INDEX.md:2746 "App. E.1" → "E.1"
- INDEX.md:2803 "App. E.8, 6.3, 6.5" → "E.8, 6.3, 6.5"
- INDEX.md:2815 "App. E.9" → "E.9"
- INDEX.md:2820 "App. E.3" → "E.3"
- INDEX.md:2854 "App. E.4, 5.4" → "E.4, 5.4"
- INDEX.md:2871 "App. E.11" → "E.11"
- INDEX.md:2918 "App. E.10, 7.4" → "E.10, 7.4"
- INDEX.md:2942 "App. E.6" → "E.6"
- INDEX.md:2943 "App. E.8" → "E.8"
- INDEX.md:2988 "App. E.10" → "E.10"
- INDEX.md:2989 "App. E.11" → "E.11"
- INDEX.md:3095 "7.1, App. D.19" → "7.1"
- INDEX.md:3113 "App. D.5" → "D.5"
- INDEX.md:3128 "App. D.5" → "D.5"
- INDEX.md:3146 "App. E.2, App. E.7" → "E.2, E.7"
- INDEX.md:3170 "App. E.5, 3.6, 6.5" → "E.5, 3.6, 6.5"
- INDEX.md:3218 "App. E.11" → "E.11"
- INDEX.md:3238 "App. E.8, 6.3" → "E.8, 6.3"
- INDEX.md:3251 "App. E.2" → "E.2"
- INDEX.md:3252 "App. E.10" → "E.10"

</details>

## Generators (run last, 2026-11-12, after a final rescan of the tex found no further removals)

- `python3 figscripts/appB/gen_B1.py`: "rows 1512, dropped 52, no label 0, unrendered 0" (before: 1529 rows, 12 dropped). gen_B1.log: dropped 52 = the 12 earlier dashes + 17 whole rows + 23 split-off rows of this pass; first-use sections with no label: 0; unrendered symbols or characters: 0; scope notes all applied.
- `python3 figscripts/appB/gen_B3.py`: fails as committed (`FileNotFoundError: tex/main.tex`; the one-volume driver no longer exists). It was run unchanged through a wrapper that replaces only its `reading_order()` by the three-volume order of tools/volumes.py (vol1, vol2, vol3; App. A once, App. B skipped): "acronyms 78, unexpanded 0"; gen_B3.log: used but never expanded 0, expanded only after the first use 3 (ANO, PAW, YIG); every first-use label exists. B-3.tex drops DOS, EXCEED-DM, LUMO, NR, NV, WEST, WIMP (no longer in the text) and moves the first use of ANO (E.16 → E.19), PAW (3.5 → 10.6, reading order of the volumes), TRIM (19.4 → 19.5). gen_B3.py itself still needs the fix (read tex/vol*.tex instead of main.tex).
- `python3 tools/split_B1.py`: vol1 806 rows in 11 groups, vol2 570 in 16, vol3 176 in 12 (App. A's 20 rows in each volume); no row dropped, no row without a first-use label.
- Labels: every \labelcref, \ref, \nameref in B-1-vol{1,2,3}.tex and B-3.tex exists. B-1.tex (the one-volume list, not input by the volumes) still has the group heading `Appendix~\ref{app:E}` for the App. E rows, and app:E no longer exists (gen_B1.py groups by letter); harmless for the volumes, fix in gen_B1.py if B-1.tex is ever printed.

## Open items (not changed here)

- tex/appC/C-18.tex: "\Cref{sec:11.1} uses ⟨c_LA⟩, written c̄_LA" is stale (11.1 no longer uses c̄_LA); for the author of C.18. If the sentence goes, c̄_LA (and s_Q) lose their last use and should be marked removed.
- The tex was being edited during this pass (E.16 lost v₀ and v_χ; ch23/s3-4.tex moved back to ch03/). Rerun the scan (method above) and the three generators after the next edit round.
- check_notation.py over ch*/app[ACDEF] reports 31 gaps (symbols in the tex without a row); not part of this pass.
