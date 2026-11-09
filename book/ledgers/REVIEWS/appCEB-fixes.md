# App B, C, E post-revision fixes (2026-11-07)

Input: ledgers/REVIEWS/appCEB-postrev-check.md. Nothing committed. NOTATION clash entry 100 records the notation side.

| # | Item (check ref.) | Status | What was done |
|---|---|---|---|
| 1 | Piezo tensor `\ee^{p}z` (B item 9) | done | gen_B1.py EXPLICIT: e^pz_αβγ, e^pz_zzz → `e^{\mathrm{pz}}_{…}` (as 6.2, 11.8). NOTATION row 11.8: e^pz_zzz gets "dominant piezoelectric element" and its unit |
| 2 | `E_{}<`, `E_{}>` (item 10) | done | take_script reads a run of < / > as a script: `E_{<}`, `E_{>}`, and `\mathcal{V}_{<>}` (same bug, 18.2 row) |
| 3 | `y_{\chi}\tilde{\nu}` (item 11) | done | EXPLICIT → `y_{\chi\tilde{\nu}}` |
| 4 | `\rho_{t*}` (item 12) | done | ∗ ends a script and maps to `\ast`: `\rho_{t}\ast\rho_{t}\ast\rho_{\bar t}` (also X_sig = 𝒢_rd ∗ Φ) |
| 5 | "tokenizer's reading" (item 13) | done | σ_ℛ removed from the 11.7 row (σ_ln ℛ has its own 10.10 row); checker accepts σ_ℛ globally |
| 6 | "as printed" ×3 (item 13) | done | 𝒮_φ, 𝒮_sig, 𝒮_n units now eV⁻²; (readout unit)² × time; v_C^2D… units "(2D, 1D)"; E_r, q̃ meaning trimmed |
| 7 | Text/math splits (item 14) | done | "(n = 0, 1, 2)" and "(𝐤, j), j = 1, 2" one math group (value-list rule); "stream $a$" (RAW_FIX); "exposure $k$" was already math |
| 8 | Further B.1 glyph bugs found by the checker | done | TEXT_FIX: v_C R v_C, 𝐮·J_z 𝐩, exp(α_d d† − α_d* d), ρ_χ σ̄_e η/m_χ, f^(𝔬)_{0𝔵}; EXPLICIT: A^λ_𝔬𝔵, F_𝔬𝔵, f^(𝔬)_0𝔵, φ_c𝔬′, φ_c𝔬‴, φ_v𝔬″, ρ^(𝔬′)_0𝔵′; bare 𝔫 dropped from the 20.3 meaning; "kernels" clause of the 16.2 row reworded |
| 9 | E-14 l.78 overfull 11.6 pt | done | Γ_n(𝐤) = −2 Im Σ^FM moved to an unnumbered display; sentence split |
| 10 | E-24 l.57 Ge qualifier | done | "(for germanium on quasiparticle bands that pass the check of \cref{app:E.14})" added to the G₀W₀+BSE exciton step |
| 11 | NOTATION entries 98/99 order | done | 98 now precedes 99 |
| 12 | ξ_a row, obsolete E.27 clause | done | clause deleted |
| 13 | 104 check_notation gaps (B 26, C 30, E 48) | done | 33 new rows (C.9–C.20, E.14–E.25), exact tex spellings, listed in entry 100(b). check_notation.py on appB, appC, appE: **0 gaps**. Whole book: 127 → 34 gaps, none new (remaining are appF/other dirs) |
| 14 | Checker exceptions (false positives) | done | ledgers/check_notation.py, file-keyed, each with a reason: B-1 ΔE_Zee, ΔE_zp, ΔE_zp,ij, ΔF_LZ, Δω_eq (Δ splits), F_ρσ (dual of F_μν), b_x, b_y (b_𝐤x, b_𝐤y with 𝐤 dropped), y_χν (tilde dropped), 𝒦_tint, χ̄_2 (quoted, 10.9); B-2 literature column λ_TF, g_χ, Ω_D, Ω_OD, V_cell; C-11 𝔊_x′j; C-13 I_C, I_D, ℓ_C, ℓ_D, u_D (material labels on new row I_a, ℓ_a, u_a); C-15 ū; C-17 σ_d (Schoenflies), f_mxG (f_𝐆 at 𝗆_x𝐆); C-19 s_⊥,P̂; E-14 Ẽ (Ẽ_m of 8.6, label dropped); E-19 𝒩^ch_λ′; E-21 𝐤_ι′; global σ_ℛ. Also \mathsf{M} read as 𝖬 |
| 15 | Clash entry 100 | done | Records items 1–14 and four clashes left in the tex: C.9 F̃_μν vs dual F̃^μν (1.4); E.14 ω_LO vs ω_L (6.2); E.24 italic x_e vs bold 𝐱_e; E.23 λ_tr vs λ_tr of 15.4 |
| 16 | Rerun gen_B1.py | done | 1527 rows, 12 dropped, 0 unlabeled, 0 unrendered |
| 17 | Build | done | /tmp/claude-0/build-fixCEB: latexmk exit 0, 0 errors, 0 undefined refs/cites, no rerun warnings, 1842 pages. Overfull in App B/C/E: max 1.15 pt (B-1 ×3, E-3 1.03 pt); none > 2 pt |

Files touched: figscripts/appB/gen_B1.py, tex/appB/B-1.tex (regenerated), figscripts/appB/gen_B1.log, tex/appE/E-14.tex, tex/appE/E-24.tex, NOTATION.md, ledgers/check_notation.py. Not touched: tex/appF, tex/front, App F rows.
