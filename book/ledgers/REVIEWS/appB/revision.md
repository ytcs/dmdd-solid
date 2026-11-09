# Appendix B revision (2026-11-07)

Inputs: accuracy.md, editor-notes.md (rulings B1–B4), writer-notes.md, STYLE.md, NOTATION.md. Nothing committed.
All NOTATION changes are recorded in clash entry 96. It sits before entry 97, which the App. C.10–C.20 reviser wrote while this
revision ran (that reviser also edited NOTATION.md and C-20.tex; their changes were kept, and they left d_kink to this revision).

| Item | Status | How |
|---|---|---|
| **B1** decimal-vs-section filter | done | gen_B1.py: PROCESS_CLAUSE treats a section number as editorial only as a pointer ("also/see/cf. 3.3", "(3.3)"), never before a unit, "/", "×" or a digit. Pointers after of/in/from are cut out of the clause (remove_pointers), and a clause is dropped only if qualifiers alone are left ("qualitative, precise"). A multi-symbol row keeps its clause count. Equation labels ("of eq:20.3-avg") are cut from the clause rather than dropping it. The 3b rows now print matching meanings: F_φ/Δω_eq/Φ, 𝔰_BCS/𝔤_I/L^nor, F_μ…, k₂; r_K, ω_K, t_SH…𝔫, O_obs…, Γ_{N_eh}…, δ_dec/δ_E (47.5°), λ_A (1.27), S^CC…, V_ZBL…, 𝖦₀ ("subscript 0 without interactions"), Δ̃₀…𝒪, K̄_pair, φ_*, t_rel. Decimal values: none lost against the first rerun (only section numbers went); spot values 2.67, 1.27, 47.5, 30.4, 0.8854, 63.7, 2.8373, 108.3 are in the PDF |
| B1 section numbers in symbol cells | done | SECNOTE_RE drops "(N.M)" and "(N.M, X.n)" from symbol cells; 0 left (grep of B-1.tex and of the pdftotext of App. B) |
| B1 clash notes | done | EDITORIAL gains "against", "two symbols", "varphi"; the three notes are gone. The one remaining "against" is a meaning ("contrast of soft against hard primaries") |
| B1 primes | done | take_script keeps a prime with an index list (R_{𝐆𝐆′}, D_{κκ′}), and with a one-letter index when the tex writes it so (τ_{κ′}, E_{L′}) |
| B1 Σ as a sum | done | In meanings Σ is `\sum` unless it is the self-energy (superscript, Σ₁/Σ₂, Σ_x(…)/Σ_c(…), standing alone); the symbol column keeps `\Sigma`; Σ_⟨ij⟩ reads as one script; a sum's index stops before δ |
| B1 bold vectors | done | Per first-use file the generator counts `\vect{q}` vs bare q (q, k, Q, G, R, r, p, K) and bolds the letter in meanings where the tex is mostly bold. It never bolds before a power, a hat or after "/", or inside a literal set. A subscripted letter is bolded when the tex prints that symbol bold (𝐐_CDW, 𝐆_U, 𝐪_r). This is a heuristic: a few scalar uses in bold-majority sections may still print bold |
| B1 upright i | done | `\ii` in e^{iq·r}, e^{−im_φt}, 2i, ib_y, iω^F_j, i0⁺, −i∇, ⟨f\|iT\|i⟩, ψ̄iγ⁵ψ; never inside an index |
| B1 Si/PV/fp/ZPR | done | `\operatorname{Si}` (before an argument), `\operatorname{PV}`, `\operatorname{fp}`, `\mathrm{ZPR}` and `\mathrm{ZPR}^{\mathrm{na}}`; "Re z, Im z" now `\Real z, \Imag z` |
| B1 text/math splits | done | j₁ (sin x − x cos x)/x², rows a, b, groups A, B, s ∈ {e, p, n}, r_p 1/(1 − R′(z_p)), ℓ_j 2(N − N_obs,j ln N), P_d(y) = 2y p(y), ka*, ê_i ⊥ q̂ (i = 1, 2), diag(…), F_L, small-ω, Order-n, ∫P_d dy, sector sets {ad, 0, +} and {prim, Luke, gap} |
| B1 units | done | (km s⁻¹)⁻¹ and (km s⁻¹)⁻²; eV^{k+3} upright; "eV⁻² (eV Å³)", "eV⁻¹ (e Å)", "length⁻²". S^ee_GG′ now "eV²; eV⁻¹ Å⁻³" (NOTATION row) |
| B1 CDW φ → `\varphi` | done | GREEK maps ϕ to `\varphi`; NOTATION spells the 22.3 phase ϕ (Δ_CDW and 𝓃̄_e rows) |
| B1 h row, v_min "≥ 0" | done | NOTATION: h is "the Hubble rate today in units of 100 km s⁻¹ Mpc⁻¹"; v_min = \|(ω + Δ_χ)/q + q/2m_χ\| |
| B1 3c cuts | done | E_g "Indirect (fundamental) band gap"; θ keeps "an integration angle elsewhere…"; ω_Ein keeps "(Einstein)" and the phonon-spectrum meaning (30.4 meV). Citation parentheses now need a year, "et al." or two names. The one-symbol cut is at 150 characters (was 90) |
| B1 five first uses | done | NOTATION: Φ^(n) 5.1, ℓ₀ 5.6, T_d/O_h 5.4, r_cl 14.4, Γ₀ 16.8 |
| B1 header | done | "Sect." (no wrap) |
| B1 rerun | done | `python3 figscripts/appB/gen_B1.py`: 1494 rows, 0 unrendered, 0 missing labels, all 36 scope notes applied. Deterministic (two reruns give the same md5). B-1.tex was not edited by hand |
| **B2** kink width → d_kink | done | `d_{\mathrm{k}}` → `d_{\mathrm{kink}}`: C-20 (11), s19-6 (7), s19-summary (1), F-rows (3), the axis and legend labels and docstring of figscripts/ch19/limit19_6b.py (rerun: log identical apart from the name; PDF rewritten). The italic bath operators d_k are unchanged. NOTATION row c_ch, ω_s, d_kink |
| B2 Lindhard bracket of 10.3 | done | s10-3: f₁ + if₂ (three uses, l.15, l.41) → `f^{\mathrm{L}}_1 + \ii f^{\mathrm{L}}_2`. New row f^L₁, f^L₂ (10.3; its q ≪ k_F limit is 𝔣_L of 15.2). The f₁, f₂ row loses the stale 4.5 pointer. A grep of Ch10, App C and App E finds no other use; 10.7 keeps f₁, f₂ (atomic scattering factors) |
| **B3** nine NOTATION errors | done | θ_s, Γ₀, σ_ω, Θ_D, ℓ₀, z_p, 𝗍 one row each (entry 96(c)); CDW ϕ; new row v₀ (E.16). C-5 now prints upright z_p (as 4.1, D.3). E_s, E_p: the row says italic s, p, as 3.2 prints them |
| B3 duplicates | done | M_cell, N_at, V_b, V_bias, c_k, m_h, b_br/N_casc, 𝗀_λ, ϵ_Luke, Δ_w, Ω_at, ω_max (17.1/E.9 → one row, first use 11.3), kept as accuracy.md names (entry 96(d)). E_el is off the list (local reuse, scope note) |
| B3 scope notes | done | gen_B1.py SCOPE (36 entries) prints "(in Sect./Chap./Appendix N)" on the local meaning of each accepted clash (E_p, G_V, s, ω_p, v_T, v₀, the 22.3 rows, ψ, ϵ, Φ, L_e, c_L, ω_max, Γ_abs, T_d, U, N_X, Ξ, ξ, ν, α_M, γ_n, ω_k, j_L, E_el, N_casc). The log lists them; labels are checked |
| **B4** B.2 σ_F | done | B-2: `\sigma_F` (italic, as 10.9 and NOTATION); the ε, κ, χ → ζ row uses `\varepsilon` like the paragraph |
| B4 spin-factor sentence | done | B-2: the book's S is summed over spin, and eq:A.7-spin carries 4π/𝒱 = 2 × 2π/𝒱 outside the band sum, as Refs. Essig and Catena also do. The difference between sources is whether the quantity called S (or the crystal form factor) includes the 2. This matches A.7 |
| B4 B.3 | done | gen_B3.py: PT "product of inversion (parity) and time reversal"; EXPANSION_OVERRIDE HSE "hybrid functional of Heyd, Scuseria and Ernzerhof", PBE "generalized-gradient functional of Perdew, Burke and Ernzerhof"; LF "local fields (crystal local-field effects)". The caption regex now reads "SOC: spin–orbit coupling", so SOC is expanded from the text. Rerun done |
| Clash entry 96 | done | NOTATION.md, before entry 97 |
| check_notation | done | `--files ch10 ch19 appC appF`: 0 new gaps. Measured against copies of the same files with the renames undone and the pre-revision table. The 62 gaps it lists are older (App. F; App. C sections under the concurrent revision) |
| Build | done | `latexmk -pdf -interaction=nonstopmode -outdir=/tmp/claude-0/build-appBrev main.tex`: exit 0, 0 LaTeX errors, no undefined references or citations. The first run stopped at the latexmk run limit because other sessions were editing appE files; the rerun was clean. App B has three overfull hboxes of 1.2 pt or less, all cosmetic, as before |
| pdftotext of App B (PDF pp. 1319–1377) | done | No "(N.M)" in symbol cells, no clash notes, no placeholders, decimals present (see B1) |

Not done or left open:
- d_kink first use stays C.20, although 19.6 uses it first in reading order. The same holds for the other C.20 chain symbols.
- Remaining generator heuristics, all cosmetic: the bold-vector rule can bold a scalar in a bold-majority section, for example 𝐩_j^α in 8.1. ρ_{t*} in 18.1 and D^{dyn,el} (italic el) come from ambiguous NOTATION spellings.
