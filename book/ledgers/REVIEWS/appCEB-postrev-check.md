# App B, App C.10–C.20, App E.14–E.27: post-revision check (2026-11-07)

Isolated verifier. Inputs: editor-notes (B1–B4, C1–C5, E1–E6), the reviews, revision.md / revision-1.md / revision-2.md.
Nothing edited except this file; nothing committed. Scripts were rerun on scratch copies.
Verdict key: CONFIRMED / CONCERN (minor, fix advised) / WRONG (criterion not met, fix required).

## 1. Rulings: spot checks (52 items)

### App B (B1–B4)
| # | Item | Verdict | Evidence / fix |
|---|---|---|---|
| 1 | gen_B1.py rerun reproduces B-1.tex | CONFIRMED | Scratch copy of tex+NOTATION+ledgers: `cmp` identical, log identical (1494 rows, 0 unrendered) |
| 2 | gen_B3.py rerun reproduces B-3.tex | CONFIRMED | Identical file and log |
| 3 | No section numbers in symbol cells | CONFIRMED | Parse of all 1494 symbol cells: 0 hits |
| 4 | Clash notes gone from meanings | CONFIRMED | No "against two symbols / varphi / entry N"; the one "against" is a meaning (l.1332) |
| 5 | Decimals kept (accuracy.md cases) | CONFIRMED | 2.67, 1.27, 47.5, 30.4, 0.8854, 63.7, 2.8373, 108.3 present. Value parentheses (e.g. E_g "1.11 eV", δM_κ "28.7 m_e") are stripped by design as source/value notes, not by the old decimal bug |
| 6 | Header "Sect." | CONFIRMED | l.14, l.18 |
| 7 | Five first uses (Φ^(n) 5.1, ℓ₀ 5.6, T_d 5.4, r_cl 14.4, Γ₀ 16.8) | CONFIRMED | NOTATION rows and entry 96(a) |
| 8 | h row, v_min row | CONFIRMED | B-1 l.33; NOTATION |
| 9 | Piezoelectric tensor glyph | WRONG | B-1 l.569 and l.918 print `\ee^{p}z_{\alpha\beta\gamma}` / `\ee^{p}z_{zzz}` (upright Euler e, split "pz"). Tex (6.2, 11.8) writes `e^{\mathrm{pz}}_{zzz}`. Fix: add `e^pz` → `e^{\mathrm{pz}}` to the special-symbol map of gen_B1.py; NOTATION row l.900 also lacks a meaning for e^pz_zzz (add "dominant piezoelectric element"), rerun |
| 10 | E_<, E_> (18.1) | WRONG | B-1 l.1235 prints `E_{}<`, `E_{}>`. Fix: generator must accept `<`/`>` as a script (`E_{<}`), rerun |
| 11 | y_χν̃ (10.9) | WRONG | B-1 l.861 `y_{\chi}\tilde{\nu}`; should be `y_{\chi\tilde{\nu}}` (add to the brace map) |
| 12 | 𝔓_t meaning (18.1) | CONCERN | l.1236 renders the convolution ρ_t∗ρ_t∗ρ_t̄ as `\rho_{t*}\rho_{t*}`. Fix: map ∗ to `\ast` between factors (or space it in NOTATION) |
| 13 | Editorial words in B-1 | WRONG | l.911 "σ_lnR the tokenizer's reading of σ_l n R" (internal label). Fix: drop that clause from the 11.7 NOTATION row or add "tokenizer" to EDITORIAL. Also CONCERN: "as printed" in l.1089 (units), l.1145, l.1153 |
| 14 | Text/math splits | CONCERN | l.1428 "$(\vect{k}, j), j = 1$, 2"; l.484 "n = 0$, 1"; l.1342 "stream a" (roman a); l.1594 "exposure k". Fix in the meaning converter or NOTATION spelling |
| 15 | 30-row random sample (seed 7) for bold scalars / wrong glyphs | CONCERN | 27 clean; errors are items 10, 11, 14 (l.1428). No bold scalars found; Q, q stay plain as in NOTATION |
| 16 | Renamed symbols reach B-1 | CONFIRMED | 𝔞_kj (l.1429), d_kink (l.1458), f^L₁ f^L₂, σ_N̂, ξ_a (l.1342), λ_dec (l.1594) |
| 17 | B2 d_kink everywhere | CONFIRMED | `d_{\mathrm{k}}` 0 hits in tex and figscripts; d_kink in C-20 (11), s19-6 (7), s19-summary (1), F-rows (3), limit19_6b.py |
| 18 | B2 f^L in 10.3 | CONFIRMED | s10-3 two lines with f^L; no other Lindhard f₁+if₂; 10.7 keeps f₁+if₂ for atomic scattering factors (correct) |
| 19 | B3 NOTATION errors and duplicates | CONFIRMED | Entry 96(c),(d); only duplicate first cells left are φ₀ (2.1/10.7, older, local) and the `\|`-split artefacts |
| 20 | B4 σ_F italic (B.2) | CONFIRMED | B-2 l.153–158 `\sigma_F` |
| 21 | B4 spin-factor sentence | CONFIRMED | B-2 l.72 agrees with eq:A.7-spin (4π/𝒱 = 2×2π/𝒱 outside the band sum) |
| 22 | B4 B.3 PT, HSE, PBE, SOC | CONFIRMED | B-3 l.54, 75, 77, 87 |

### App C.10–C.20 (C1–C5)
| # | Item | Verdict | Evidence / fix |
|---|---|---|---|
| 23 | C1 C.10 half-line sentence | CONFIRMED | Diverges as ξ→0, ξ⁻³ tail, tighter only at intermediate ξ, ≤ 6.8 % near 0.74 E_R (11.5) |
| 24 | C1 gamma example | CONFIRMED | Recomputed (shape 3, five moments): +4.08 % at +58σ, +1.35 % at +173σ, −3.88 % at −58σ; text 4.1 / 1.3 / 3.9 % |
| 25 | C2 ξ_a, ξ₁ in C.12 | CONFIRMED | No c_a/c₁ left; Ξ* = Σξ_aδ_{w_a} |
| 26 | C2 σ_N̂ in C.14 | CONFIRMED | 15 occurrences of `\sigma_{\hat N}`, no bare σ_N for the width |
| 27 | C2 𝔞_kj in C.16 | CONFIRMED | 4 occurrences; no α_kj anywhere; NOTATION row l.1381 |
| 28 | C3 Rogosinski n+1 → n | CONFIRMED | C.12 sentence present |
| 29 | C3 C.17 corrected sentence | CONFIRMED | "At k = 0 and q = G = (2π/a)(0,2,0), so that … k + q − G is again 0"; f_G cites eq:A.3-periodic |
| 30 | C3 C.19 Berlin et al. | CONFIRMED | per formula unit, σ for σ/2, χ″ = 2(1 − e^{−βω})S with π/V vs 2π/V [Eq. (B4)] |
| 31 | C3 C.20 Fitzgerald factors and Qureshi symbols | CONFIRMED | factor 4 (Eq. 5) and 2 (Eq. 6), lattice sum; γ₀, Δ̃₀ defined in place |
| 32 | C4 prose (C.10/C.13 closes, C.19 subject, C.20 phrases) | CONFIRMED | Closes rewritten; none of the flagged phrases remain |
| 33 | C5 ϱ_MK first use C.10 | CONFIRMED | NOTATION l.867 |

### App E.14–E.27 (E1–E6)
| # | Item | Verdict | Evidence / fix |
|---|---|---|---|
| 34 | E1 E.1 l.147 | CONFIRMED | "bands that pass the check of app:E.14 (…)"; hybrid and 4s shift named as failing; quasiparticle route next, no verdict |
| 35 | E1 E.15 (l.16 BSE, l.58 SOC) | CONFIRMED | No HSE06 reuse; Ge BSE waits for bands that pass; GW next route |
| 36 | E1 E.16 library and loss functions (l.9, l.36) | CONFIRMED | Scissor for Si only; no Ge version until bands pass |
| 37 | E1 E.18 drag masses | CONFIRMED | l.25 Ge sentence; drag masses and Ge Migdal electronic piece on bands that pass |
| 38 | E1 E.23 HSE arm | CONFIRMED | "The hybrid arm serves silicon only"; Ge spread rests on the other two treatments |
| 39 | E1 E.24 l.9 bands | CONFIRMED | Ge enters only after the E.14 check; G₀W₀ named as next route, no result |
| 40 | E1 E.24 l.57 excitons | CONCERN | "The exciton parameters come from G₀W₀ and the BSE … which in silicon and germanium checks …" has no E.14 qualifier for Ge. Fix: add "(for germanium on quasiparticle bands that pass the check of app:E.14)" |
| 41 | E1 grep of tex/ch* for failing Ge routes | CONFIRMED | s3-4, s10-6, s22-1/22-2 describe the failures or ask for quasiparticle bands under the check; none prescribes one. No GW Ge result quoted in E.14–E.27. Note: E.3 tab:E-gw quotes literature GW gaps of Ge (methods review, outside scope; not a spec) |
| 42 | E2 E.18 coherent zero-phonon subsection | CONFIRMED | Bragg process p = q − G, weight e^{−2W(G)}, cross-site S_κκ′ and full S^ee_{q−G,q−G′}; diagonal above 2q_BZ (= s12-4 l.55); boost limit 1/14.9, median 4.5→17.4 eV, ≤15 % only below 0.75 keV, band 0.75 keV–2q_BZ carrying nearly all of the rate to 1 MeV, 33 % at 2, 7 % at 3 MeV: identical to tab:12-nuisances (s12-6 l.178), CLAIMS II-348 and tab:22-calc row. Method, three tests, cost, output and table row present |
| 43 | E3 E.20 ZrTe₅ | CONFIRMED | e20_zrte5_dirac.py rerun: log byte-identical (α̃ 0.1825, Ry_D 0.098 meV, a_D 1449 Å, ratio 27.5); inputs = s16-1 l.64 row; text 0.18 / 0.10 meV / 1.4e3 Å / 27, cutoff 0.191 eV, tab:E20-dirac both rows |
| 44 | E3 E.24 numbers | CONFIRMED | appE3_rev2_numbers.py rerun: log identical. F 0.114 at 2.4σ (as s18-4 l.64), DFT 14 %, A_AB 5.703 eV³, ΔA 1.43, 2.9 %, plasmon 16.4 eV, C/x with C ≈ 0.24, h^{3/2}, GaAs measured ε∞ and LO–TO |
| 45 | E3 E.25 numbers | CONFIRMED | ε₀ = 11.4; 𝓃_sh 6.3–12.6e4 cm⁻² (checked by hand in SI); 3.5e4 V/cm; Summary-of-Ch20 pointer; 0 K Al Voigt 6.63/3.30 km/s, 2.70 g/cm³. ε₀ kept instead of ε_s (ruling wording) with the reason in entry 99(c): acceptable |
| 46 | E3 E.26, E.21, E.23, E.17, E.16 | CONFIRMED | Cu −1.97e-2; (Zα)² 0.155; expansion keeps 2m_χω; \|p−q\|⁻⁵; Fermi factor; Qb@ll plane-wave; 0.41 eV; CsI 4.2 K constants + cold-cell density; minima 0.13–0.22 rad |
| 47 | E4 promises (spot: E.14 PA kinetic row, E.16 2 % f-sum, E.17 PIMD 0.2 %, 8.4 pointer) | CONFIRMED | All present; s8-4 cites app:E.16 for the supercell |
| 48 | E5 recipe template rate | CONFIRMED | Slot openers in E.14–E.27: 24 in 39,065 words = 0.61 per 1,000 (E.1–E.13: 0.6–2.9, mean ≈ 0.86). Per section E.23 is 1.58 (four), the only one above 1.5 |
| 49 | E5 count sentences | CONFIRMED | Remaining "Two/Three/Six …" sentences all carry the right count |
| 50 | E5 E.21 STE, E.27 Gordon | CONFIRMED | "self-trapped exciton" spelled out; no Gordon citation |
| 51 | E6 E.27 notation | CONFIRMED | Uses 𝗄_i, Ξ, 𝖿, λ_i of C.12 (λ_i are C.12's dual weights, l.29); 𝔎_i, 𝔥, ξ_i, μ_i retired, so no rows needed; λ_dec row added (NOTATION l.1334) |
| 52 | E6 NOTATION ξ_a row | CONCERN | Row l.1325 still says "E.27's dual weights ξ_i are the λ_i of C.12"; entry 99(a) calls this obsolete but did not remove it. Fix: delete that clause |

## 2. NOTATION.md integrity
| Item | Verdict | Evidence / fix |
|---|---|---|
| Entries 96–99 present | CONFIRMED | l.2354 (96), 2356 (97), 2358 (99), 2360 (98) |
| Entries in order | WRONG | 99 precedes 98 (the E.14–E.20 reviser appended after 99). Fix: move the entry-98 paragraph above entry 99 |
| No duplicate rows introduced | CONFIRMED | First-cell scan of 1497 rows: only φ₀ (older, local 10.7) |
| check_notation.py on appB, appC, appE, ch10, ch19 = 0 gaps | WRONG | `--files 'appB/*.tex' 'appC/*.tex' 'appE/*.tex' 'ch10/*.tex' 'ch19/*.tex'`: **104 gaps** (B 26, C 30, E 48; ch10, ch19 0). The revisers reported "0 new gaps" against their own baselines, not 0 gaps. Of these: B-1 gaps are partly generator glyph bugs (z_zzz, ρ_t*, items 9–12); E gaps listed in entries 98(d), 99(e) as pre-existing, but p_red, a_D, v_D,x/y/z, ε_bg,zz sit in text rewritten this pass (E.18 coherent subsection, E.20 ZrTe₅); C gaps in C.10 (F_model, w_ξ), C.11, C.12 (w_h, Φ_h, λ_h, ℬ_h, 𝗀_λh), C.13, C.16, C.17, C.19, C.20 (H_FK, H_L). Fix: add rows or declare locals; at least the rewritten-text symbols now |

## 3. Prose regressions
| Item | Verdict | Evidence |
|---|---|---|
| Template ≤ 1.5 per 1,000 words (E.14–E.27) | CONFIRMED | 0.61 (item 48) |
| lint.py --banned BANNED-TERMS.txt, all changed files (B-1..3, C-10..14, 16, 17, 19, 20, E-1, E-14..27, s8-4, s10-3, s19-6, s19-summary, F-rows) | CONFIRMED | 0 blocking; advisories only (336 LONG-SENT, 2 EQ-PUNCT on `gathered`, 3 "landscape" in F-rows, 2 DASH in B-1 preamble) |
| No process or internal labels in the tex | CONCERN | E/C tex clean (only cref labels). B-1 has "tokenizer" (item 13, WRONG) and "as printed" (CONCERN) |

## 4. Build
| Item | Verdict | Evidence / fix |
|---|---|---|
| Errors | CONFIRMED | Fresh outdir /tmp/claude-0/build-appCEB-post: first latexmk stopped at the pass limit (fresh aux, exit 12); second invocation "up-to-date". Final main.log: 0 `!` errors, 1840 pages |
| Undefined citations / references | CONFIRMED | 0 / 0 in the final log; no missing labels to list |
| Overfull > 2 pt in App B, C, E | WRONG | appE/E-14.tex l.78–79: **11.6 pt** (inline Γ_n(k) = −2 Im Σ^FM_nk(ε_nk) in "The width of the pair state …"). Fix: put the definition in a display or rephrase so the formula can break. Others ≤ 1.2 pt (B-1 ×3, C-5, C-13, E-3) |

## Required fixes
1. App B: gen_B1.py/NOTATION fixes for items 9, 10, 11, 13 (piezo e^pz ×2, E_<, E_>, y_χν̃, "tokenizer" clause), then rerun; advised 12, 14 and "as printed".
2. NOTATION: move entry 98 above 99; delete the obsolete ξ_i clause in row ξ_a; add rows or locals for the 104 check_notation gaps, at least p_red, a_D, v_D,i, ε_bg,zz (E.18/E.20 rewritten text) and the B-1 artefacts.
3. App E: E-14 l.78 overfull 11.6 pt; E-24 l.57 Ge qualifier for the G₀W₀+BSE exciton step.
4. App C: content accepted; its 30 check_notation gaps (28 in C.10–C.20, all in text not touched by the renames) go to the App C ledger merge.
