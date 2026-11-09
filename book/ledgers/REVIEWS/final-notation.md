# Final notation pass (2026-11-07; NOTATION clash entry 105)

Checker: `python3 ledgers/check_notation.py --files 'ch*/*.tex' 'app*/*.tex' 'front/*.tex'`. Before: 34 gaps. After: 0 gaps.
Fixes: 1 = NOTATION row (book's own symbol, defined in place); 2 = F row rewritten in the home section's symbol; 3 = file-keyed
exception in check_notation.py (literature notation quoted on purpose, or a label/tokenizer split on an existing row).

| Symbol | Where | Fix | What was done |
|---|---|---|---|
| a_Born | s8-2 (Limit Check 8.2a), F row 8.2a | 1 | New row after δ_Born: first-Born zero-energy scattering length of the Yukawa potential, magnitude \|f(0)\| = μ_χT y_χy_T/(2πm_V²); eV⁻¹; first use 8.2 |
| ℛ_RPA+LF | F row 10.9a | 1 | New row ℛ_IP, ℛ_{RPA+LF}, ℛ_source (10.9): unscreened and screened crystal rates (y axis of the plot); kg⁻¹ yr⁻¹ |
| ℛ_source | F row 10.9b | 1 | Same row: rate of the published boosted density row |
| 𝒰, 𝒰^*, 𝒰^† | D-2 | 1 | Row 𝒰_{γγ̃} widened to 𝒰_{γγ̃}, 𝒰 (the unitary matrix itself, with 𝒰*, 𝒰†); D.2 |
| K̃ | D-3 | 1 | Row K(t − t′), R(z) widened to K(t − t′), K̃(s), R(z): Laplace transform Σ_f\|H′_fi\|²/(s + iξ_f); eV; D.3 |
| k_φ | F row 11.8c | 2 | `$k_\phi \to 0$` → `$\vect{p}_\phi \to 0$` (row 𝐩_φ; 11.8 writes the boson momentum p_φ ≈ m_φv) |
| v_F,x, v_F,z, κ_xx | F row 16.1a | 2 | Misprint of the source's Eq. (3.14) restated as D.41 states it: `$q_x^2v_z^2/\varepsilon_{\mathrm{bg},xx}$ for $q_x^2v_x^2/\varepsilon_{\mathrm{bg},xx}$` (rows v_i, ε_bg,ii) |
| M_χ | F row 16.3a | 2 | Second source's misprint `$E_r = k'^2/2M_\chi$` → `$E_r = k'^2/2\mchi$` (the book's m_χ) |
| n_ph | F row 16.7c | 2 | `$\mathcal{K}$ = elastic, $n_{\mathrm{ph}} = 0$` → `$\mathcal{K}$ = elastic` (n_ph is not a component of 𝔗; 𝒦 = elastic says no phonon) |
| n_eh | F row 20.5 | 2 | `n_{\mathrm{eh}}`, `Y E_R` → `N_{\mathrm{eh}}`, `Y_qE_R` (as 19.2 and 20.5 write it; bare Y not used, clash 65) |
| σ̄_n | F row 11.1b | 3 | Literature: Griffin et al.'s σ̄_n named in the Source column (book: σ_p) |
| V_cell | F row 11.2a | 3 | Literature: Knapen et al.'s C_F² ∝ 1/V_cell (book: Ω; as D.29, B.2) |
| f̄_d, m_d, D_d | F row 11.3a | 3 | Literature: the row's explicit map to c_κ, M_κ, g_ph,κ/3 |
| Δ_d | F row 11.4a | 3 | Literature: "σ_ω² … = Δ_d² of the source"; replacing it by σ_ω would void the identification |
| σ_NC | F row 11.4b | 3 | Literature: "their σ_NC" (Dror et al.) |
| f̂_ℓm, T_ℓm, W_ℓm, D_d^ij | F row 11.7a | 3 | Literature: the row's explicit map "their f̂_ℓm and T_ℓm (or W_ℓm) → 2πℋ_ℓ, S_ℓm; their D^ij_d → D_κ" |
| Y_ℓ0 | F row 11.7a | 3 (local) | Y_ℓm of 11.7 at m = 0 |
| F_M | F row 12.4a | 3 | Literature: Berghaus et al. Eq. (4.8), F_{1,1} = F_M → A² |
| ε_S | F row 14.6a | 3 | Literature: Budker et al.'s shift d_nε_SE* (book: Δε = d_nE*) |
| ω_eq | F row 14.6c | 3 (local) | Δω_eq already as in 14.6 (tokenizer splits Δ), as the 14.6, 17.2, B.1 entries |
| Z_r, k_inst | F row 16.8c | 3 | Literature: "Published form: kZ_r = …, and k_inst of the source's Eq. (4)" |
| F_unc | F rows 18.2b, 18.2c | 3 | Literature: Subashiev's published F_unc (book: F_ren) |
| E_zp | F row 19.5a | 3 (local) | ΔE_zp already as in 19.5 (tokenizer splits Δ) |
| Γ_md | F row 20.2b | 3 | Literature: "written with Γ_md … in the source" (book: g_md) |

Totals: 7 symbols by rows (fix 1), 7 by F-row edits (fix 2), 20 by exceptions (fix 3; 17 literature, 3 local).

Note on the brief's examples: ω_eq and Δ_d were listed as fix-2 examples. App. F already writes Δω_eq exactly as 14.6 does (the
gap is the tokenizer's Δ split), and Δ_d is a deliberate "of the source" identification, so both are exceptions instead.

Follow-up: App. B.1 regenerated (figscripts/appB/gen_B1.py: 1529 rows, 0 unrendered). Full book rebuilt
(1842 pp; 0 errors, 0 undefined citations or references, largest overfull box 4.93 pt) and copied to releases/book-full.pdf.
