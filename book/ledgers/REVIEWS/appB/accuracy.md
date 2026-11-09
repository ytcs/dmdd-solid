# Appendix B accuracy review (2026-11-07)

Isolated reviewer. Read: tex/appB/*.tex, figscripts/appB/gen_B1.py, gen_B3.py and both logs, NOTATION.md, STYLE.md, writer-notes.md;
greps of tex/ch*/ and tex/app*/; build /tmp/claude-0/build-appB/main.pdf (02:06, newer than B-1/B-2/B-3). Nothing edited.
Verdict: B.2 is sound (2 FIX, 2 minor). B.3 is sound (3 minor FIX). B.1 has generator defects: 13 multi-symbol rows have
symbols and meanings out of step, 26 symbol cells contain a section number, 3 process notes remain, and there are typography
errors. These come from gen_B1.py, so fix them there and rerun; do not hand-edit B-1.tex.

## 1. B.2 (tab:B-literature and conventions)

Every "Here" symbol was grepped in its stated section. All are used with the stated meaning there unless listed below.

| Row / item | Verdict | Note / correction |
|---|---|---|
| χ_AB, χ, C^R_AB → R_ab (4.1) | OK | 4.1 eq:4.1-kubo has −(i/𝒱)Θ⟨[…]⟩; "1/𝒱 omitted" is right for Bruus-type C^R |
| Π → R̃ (4.4) | OK | 4.4 l.12 "Coulomb-proper (or irreducible) response R̃_ee"; ε = 1 − v R̃ has the same sign as the usual Π |
| W, Im(−1/ε) → L (4.4) | OK | eq. at 4.4 l.83 |
| W (GW) → W^scr (4.8) | OK | first named in 3.4 and defined in 4.8; the column means "defined", so 4.8 is right |
| −2 Im G^R → 𝖠 (4.7) | OK | 4.7 l.46 says exactly this (normalized to 1 against 2π) |
| G(r,t) → 𝒢_VH (4.2), λ_TF → 1/k_TF, κ → ε_bg (7.3 l.72), α(ω) → α_abs (6.5) | OK | |
| ε, κ, χ → ζ; g → y (1.4); n_χ → 𝓃_χ; k → q; dΩ → dΩ_q (2.2 l.10); Q → N_eh (1.5) | OK | Table uses \epsilon but the paragraph uses \varepsilon for Essig et al.: use one glyph (minor) |
| σ_e → σ_F (10.9) | FIX | tex writes italic `\sigma_F` (10.9-fermionic, l.157, 164) and NOTATION l.850 writes σ_F; B.2 prints `\sigma_{\mathrm{F}}`. Match the tex (or change the tex to upright, as STYLE requires, and print it upright here) |
| q,k → Q (5.2); Helm/Woods–Saxon (2.2 l.207–212); Lamé → C12, C44 (C.18 l.40) | OK | |
| λ → λ_ep (6.4); μ* → μ*_C, Z, Δ → Z^El, Δ^El (E.9 l.75–76) | OK | |
| μ → μ_ch; N(0) → 𝒩_F per spin (2.5 l.139: m k_F/2π² is per spin) | OK | |
| v_F → v_D (7.3); χ_nl → ψ̃_nl (2.2 l.132, 150); T_s → K_s (3.4 l.37); V_2 → V_cov (3.2 l.153) | OK | |
| Ω, Ω_I, Ω_D+Ω_OD → Ω_W, Ω_W^I, Ω̃_W (3.6 l.44, 75); V_cell → Ω (3.1 l.16) | OK | Marzari–Vanderbilt notation stated correctly |
| χ, χ⁰, α → R^U, R^{U,0}, δV^U (E.9 l.18–20) | OK | Cococcioni–de Gironcoli notation stated correctly |
| α, K → α_ohm (16.8 l.23–25); e (Gaussian) → e_G (A.2 l.26–28); k → s (C.8 l.38, 44) | OK | |
| Fourier convention | OK | Matches eq:A.3-space/-time/-ne (A.3 l.5–20). The time convention, analyticity and the engineering e^{+iωt} conjugation match A.3 |
| Mixing-term sign | OK | Matches A.9 l.43 and 1.4 l.76–79 (L ⊃ −ζe A′J_em, J_em counts the electron as −1, so y_e = −ζe). The Lin and Essig equation numbers are as A.9 states; the sources themselves were not re-read offline |
| Units of charge | OK | Matches A.2 eq. l.28 (e² = 4πe_G² = e_SI²/ε0) |
| S(q,ω) normalisation | OK/FIX | 2π/𝒱, dimension eV² and the f-sum π𝓃_e q²/m_e over the real line match eq:A.7-S and eq:A.7-fsum. The many-body form S/(2π𝓃_e) with moment q²/2m_e matches A.7 l.78. FIX the wording "the book includes the spin factor 2 inside S … Refs. … write it outside their band sums": the book also writes 4π/𝒱 outside its band sum (eq:A.7-spin). The real difference is whether the quantity called S (or f_crystal) includes the 2. Say that, as A.7 l.64 does |

## 2. B.3 expansions (gen_B3.py EXPANSION_FALLBACK and DEFINED_IN_TEXT)

All 47 fallback expansions are standard. The usage was checked in context for LF, IP, NR, PT, SOC, FP, ML, KK, EPW and HSE06.

| Item | Verdict | Note |
|---|---|---|
| LF "local fields" | OK | 8.5 l.91: "RPA + LF" = RPA "with local fields" (eq:4.6-rpaLF). Clearer: "local fields (crystal local-field effects)" |
| EPW "Electron–Phonon Wannier (code)" | OK | official name |
| HSE06 "Heyd–Scuseria–Ernzerhof hybrid functional, 2006 parametrization" | OK | Krukau et al. 2006; matches use in 10.6, E.14 |
| SOC "spin–orbit coupling" | OK | Not a defect: 8.4 table caption l.78 expands it ("SOC: spin–orbit coupling."). The script's caption regex misses the colon form, so drop SOC from the writer's unexpanded list |
| PT "parity and time reversal" | FIX (minor) | D.28 l.93 defines 𝖯𝖳 as the *product* of inversion and time reversal. Use "product of inversion (parity) and time reversal" |
| HSE "Heyd, Scuseria and Ernzerhof"; PBE "Perdew, Burke and Ernzerhof" | FIX (minor) | These name people, not the thing named. Write "hybrid functional of Heyd, Scuseria and Ernzerhof" and "generalized-gradient functional of Perdew, Burke and Ernzerhof", to match the HSE06 and PBE0 rows |
| CODATA "Committee on Data of the International Science Council" | OK | the current official name |
| NR "nonrelativistic" | OK | its only prose use is F-rows l.142 ("NR recoil"); NR/ER as recoil labels occur only inside math |
| ANO-RCC, CASSCF, DAMIC, EXCEED-DM, G4CMP, GIPAW, GPAW, GRASP, JARVIS, SALMON, TRIM, WEST, X2C, ZG, TB09, PBE0, SCAN, FIRE, ACE | OK | standard |
| First-use column | OK | spot-checked: BCS 1.5, CCD 1.5 table, DFT 7.1 (first prose use), RPA 8.5, CODATA A.1, QED 6.3 |

## 3. B.1 (sample of 62 rows, one row in 24 across all groups, plus targeted checks)

Symbol, meaning and units match NOTATION and the home section in about 40 of the 62 rows. The defects below are generator
defects that recur throughout the table; counts are for the whole table.

**3a. Wrong first use (sample and targeted)**
- Φ^(n) (force constants): first used in 5.1 (l.67), not 5.2. FIX.
- ℓ₀: used in 5.6, 8.6, 11.5 and 12.1 before C.6, so first use is 5.6, not C.6. The 11.5 row (NOTATION l.887) is the same quantity (see §4).
- T_d, O_h (Schoenflies): used in 5.4 (and 7.4, where row 623 refers to it), so first use is 5.4, not C.3.
- r_cl: used in 14.4 before C.19, so first use is 14.4.
- Γ₀: first use 16.8 (Γ = Γ₀e^{−V_b/T} in 16.8), not 19.6 / E.11 (see §4).
- v_min, η(v_min): listed at 1.1 where they are only named; defined in 1.3. Acceptable under "first use"; consider 1.3.

**3b. Multi-symbol rows whose meanings fall out of step with the symbols (WRONG).** In clean_meaning, PROCESS_CLAUSE also
deletes every clause containing a number like "2.67" or "1.27", because its section-number regex matches decimals. When this
happens in a multi-symbol row, the remaining meanings shift onto the wrong symbols. Rows (NOTATION line) whose printed meaning
is wrong: 1088 F_φ, Δω_eq, Φ (Δω_eq gets Φ's meaning); 1104 𝔰_BCS, 𝔤_I, L^nor; 1108 F_μ, 𝔭_μ, 𝔭, ω_μ, s_*; 1222 k₂; r_K, ω_K;
1313 t_SH … 𝔫 (the t̄ symbols get the 𝔫 meaning); 1319 O_obs, 𝒮_sep, …; 1322 Γ_{N_eh}, ℛ, ℛ̄; 1326 δ_dec, δ_E (δ_E's meaning
"declination of v_⊙, 47.5°" is lost); 1341 λ_A, m_th^CC, … (λ_A gets "threshold mass"); 1344 S^CC_ab, ρ^CC, …; 1495 V_ZBL,
a_U, Z₁, Z₂; 440 𝖦^R, 𝖦^A, 𝖦, 𝖦₀ (𝖦₀ undefined); 1182 Δ̃₀, W_el, Q_TLS, 𝒪 (𝒪 undefined). Also dropped: 836 K̄_pair, 1252 M,
1292 φ_*, 1320 t_rel, 1333 (one clause). FIX: run PROCESS_CLAUSE section matching only on true pointers ("of 3.3", "(3.3)"),
never on numbers with units or bare values. In a multi-symbol row, never drop a clause unless the symbol count still matches.

**3c. Misleading one-symbol cuts (FIX).** 76 E_g prints "indirect (fundamental) band gap; qualitative, precise"; cut to
"Indirect (fundamental) band gap". 73 θ prints only "angle between q and v"; add "elsewhere an integration angle defined where
used". 447 ω_Ein loses "Einstein" and the phonon-spectrum meaning (⟨ω⁻¹⟩⁻¹, 30.4 meV in Si, 6.3); keep both. The other cuts
(ω, N, Γ_w, E_cut, H_N, B, S⁰, …) are harmless.

**3d. Leftover editorial text in B-1.tex (FIX).**
- 26 symbol cells carry a section number: `$H_{\mathrm{e}} (5.6)$`, `$Q (7.4)$`, `$\vect{d} (7.4)$`, `$N_{\mathrm{v}} (12.6)$`,
  `$b (13.2)$`, `$\theta_{E} (14.3)$`, `$\Phi (14.5)$`, `$g_{d} (14.6)$`, `$\Pi (16.1)$`, `$x (16.1)$`, `$m_{h} (16.2)$`, `$f (16.2)$`,
  `$y (16.5)$`, `$\tilde{k} (16.5)$`, `$\Omega (16.8)$`, `$g(\omega) (16.7)$`, `$\mathcal{O} (16.7)$`, `$\gamma_{0} (16.8)$`,
  `$\omega_{\mathrm{max}} (17.1)$`, `$B (17.2)$`, `$\vect{K} (17.4)$`, `$\omega_{\mathrm{top}} (21.3)$`, `$g (21.5)$`, `$E_{e} (21.7)$`,
  `$q_{\nu} (21.7)$`, `$s (D.22)$`, `$E_{\mathrm{qp}}(nk) (E.3)$`. render_symbol must strip "(N.M)".
- Clash notes: B-1 l.749 "(C^cross against C^an and 𝒞′_κκ)"; l.1103 "(the product 𝔤_I L^nor is two symbols)"; l.1580
  "(Γ_L against g_Luke, the Luke gain)". Add "against" and "two symbols" to EDITORIAL.
- h row: "(H_Hub,0 = 100h km s⁻¹ Mpc⁻¹)" names a symbol the book no longer uses (dropped row), with h set upright in text.
  Write "H₀ = 100 h km s⁻¹ Mpc⁻¹ is the Hubble rate today" in math, or "Hubble rate today in units of 100 km s⁻¹ Mpc⁻¹".
- v_min row: "… |(ω + Δ_χ)/q + q/2m_χ| ≥ 0" (inherited from NOTATION l.60) is meaningless. Write "v_min = |…|" and fix NOTATION too.
- No ⚑, no dates, no eq:/tab:/fig: labels and no "(\epsilon)" note survive (grep clean). "row" in "target row" is book terminology, not a process word.

**3e. Typography against the tex (FIX in the generator).**
- Bold lost inside meanings: q, k, Q, G, R, r are printed plain where the tex has `\vect` (e.g. L(q,ω), R_{GG′}: n_e(q+G),
  e_κν(Q), cos(Q_CDW·r + φ), |w| ~ e^{−|R|/ξ_W}). NOTATION writes 𝐪 for some of these; the generator drops it.
- Primes after the subscript, 14 rows: `R_{\vect{G}\vect{G}}'`, `S^{ee\prime}_{\vect{G}\vect{G}}`, `\tilde\omega_{\vect{G}\vect{G}}'`,
  `_{\kappa\kappa}'` ×8, etc. These must be `_{\vect{G}\vect{G}'}`.
- Σ as a sum is printed as the letter `\Sigma` (77 times) instead of `\sum`; one `\Sigma_{}\langle ij\rangle` (H_H row) is broken.
- Imaginary unit: `\ee^{iq…}`, `\ee^{-im_\phi t}` and "2i" use italic i; the book uses `\ii` (12 occurrences).
- Upright operators printed italic: `$Si(z)$` (tex `\operatorname{Si}`), `$PV$`, `$fp$` (tex `\operatorname{PV}`, `\operatorname{fp}`),
  `$ZPR$`, `$ZPR^{na}$`, `$ZPR^{ad}$` (tex `\mathrm{ZPR}`). Text-mode "Re z, Im z" in the z row.
- Broken text/math splits: j₁ "(sin $x - x$ cos $x)/x^2$"; "rows a, $b$" and "groups A, $B$" (l.705, 837, 912, 1073); "{e, $p$, n}"
  (c_i^(s), braces lost); "1/(1 $- R'(z_p)$)" (r_p); "2(N $- N_{obs,j}$ ln $N$)" (ℓ_j); "P_d(y) = 2y p(y)"; "ka*"; "$\hat q (i = 1$, 2)".
- Units broken: K_η "$\mathrm{km}$ $s^{-1})^{-1}$" (should be (km s⁻¹)⁻¹); 𝓜^k "$eV^{k+3}$" italic; S^ee_GG′ "eV⁻¹ Å⁻³"
  has no natural-unit entry (give "eV²; eV⁻¹ Å⁻³", or note it is the conventional form of the book's eV²).
- CDW phase: the tex has `\varphi` (22.3 l.95), but GREEK maps both φ and ϕ to `\phi`, so B.1 prints `\phi`, the dark-matter field. Map ϕ → `\varphi`.
- :…: is `\cdots` in the tex (2.3 l.177) and `\dots` in B.1 (minor). v_c(r): the tex writes v_c without (r) (1.1 l.20) (minor).

**3f. Rows checked and OK (sample):** m_χ, v_max, a, J^μ_em (1.4; eV³), A_mod (1.5, 0.185, dimensionless), w(x) (2.4), N (3.1),
ε⁰_k (3.2), V_KS/v_xc/E_xc (3.4), ψ_A/ψ_B (3.5; eV^{3/2}), ξ_W (3.6), u (4.2), Δ_cvk (4.6), B(q,ω) (4.8; eV⁻², as W), g_ph,κ
(5.3), E^ad_ℰ (5.5), H_ep (6.1), M_ν (6.5), α̃ (7.3), 𝒯_e (8.1), ϱ̂_χ (8.2, tex `\op{\varrho}_\chi`), x_R (8.5), ω_th (9.2),
j_L/j_T (10.4), f₁,f₂ (10.7), E_χ (10.9), S^self (11.6), ω_TA,LA(Q*) (13.1), ΔE_g(T) (13.5), Ω_ion (14.1), M^N_A (15.1), ζ^lim
(16.1), P̄ (16.7), ρ_∞ (18.2, Rényi 0.7476), F_meas (18.5), f_top (20.2), r_χ, r_e (A.3; eV⁻¹), ≻ (C.13), r_cl value, k̃ (D.8),
Δ_gauge (E.2), N_conf, N_eff (E.8), r_min (E.11).

## 4. Notation clashes (writer-notes §1, plus three found here)

Classes: a = the two meanings can meet in one section, so rename; b = acceptable local reuse, list both meanings in B.1 with a
scope note; c = NOTATION error (same quantity, wrong row or spelling). Files are the tex files that use the symbol.

| Clash | Class | Action | Files |
|---|---|---|---|
| E_p: relativistic energy (2.1) vs on-site p energy (3.2) | b (+c) | The tex already differs: 2.1 has `E_{\vect{p}}`, 3.2 has italic `E_p`. NOTATION l.305 says "upright s, p", which the tex does not do: fix NOTATION or set `E_{\mathrm{s}}, E_{\mathrm{p}}` in 3.2 | ch02/s2-1, ch03/s3-2 |
| G_V: pair coupling (10.8) vs Voigt shear modulus (11.1) | b | Different chapters with the same spelling `G_{\mathrm{V}}`; scope notes. Optional cheap rename in 11.1: G_Voigt, G_Reuss | ch10/s10-8, ch11/s11-1 |
| s: spin projection (2.3) vs elliptic modulus (C.8) | b | Spin s is a label only; s is a quantity only in C.8 (and the C.6 width, D.22 row) | ch02/s2-3, appC/C-8 |
| ω_p: plasma (italic p, book-wide) vs phonon at crossing (14.2, `\omega_{\mathrm{p}}`) | b | Ch14 has no plasma frequency. Note the precedent of ω_acc "renamed from ω_p" (l.1283): a rename to ω_ph^× would be consistent | ch14/s14-2 |
| v_T: transverse DM velocity (`v_{\mathrm{T}}`, 8.1/8.2/10.9/21.1) vs transverse sound speed (italic v_T, 11.1) | b | Spellings differ; 11.1 has no transverse DM velocity. Note: 20.5 calls sound speeds c_LA, c_T | ch11/s11-1; ch08/s8-1, s8-2, ch10/s10-9, ch21/s21-1 |
| v₀: halo speed (1.2, book-wide) vs Coulomb head (D.7, D.36) | b (+c) | Head only in D.7, D.36. A third meaning, the contact kernel v₀ of E.16, has no NOTATION row (c): add it or rename it v_ct | appD/D-7, D-36, appE/E-16 |
| e: elementary charge vs electron Dirac field (22.3 eq. l.42) | b | 22.3 uses α, not e, as the charge. Scope note "22.3 only" (NOTATION already has it) | ch22/s22-3 |
| φ: absorbed DM field vs CDW phase (22.3) | c | The tex uses `\varphi` for the phase (22.3 l.95); NOTATION l.1342 should spell it ϕ (varphi), and gen_B1 must render it `\varphi` | ch22/s22-3 |
| ψ: Dirac field / wavefunction vs log-template (8.8) | b | 8.8 has no wavefunction; scope note | ch08/s8-8 |
| ϵ: E − m_e (3.5) vs collection efficiency (19.5) | b | Both `\epsilon`, far apart; scope note | ch03/s3-5, ch19/s19-5 |
| Φ: two-component state (3.5) vs field amplitude (14.6) | b | Also the scaling function Φ (14.5) and the Slater determinant (D.4, D.5). 14.5 and 14.6 are adjacent: consider renaming the 14.5 scaling function | ch03/s3-5, ch14/s14-5, s14-6 |
| θ_s: scattering angle (2.2) vs CM scattering angle (19.3) | c | Same quantity (CM angle = angle between relative momenta). Keep l.157 (2.2); remove θ_s from l.1265 | ch02/s2-2, ch19/s19-3 |
| L_e: electron-channel loss (italic e) vs extraordinary-ray loss (`L_{\mathrm{e}}`, 11.8; writer says 11.2) | b | The electron-channel loss is not used in 11.8; scope note. Optional: L_ord, L_ext | ch11/s11-8; appA/A-7, ch04/s4-4, ch08/s8-4, ch10/s10-2 |
| c_L: plate speed (`c_{\mathrm{L}}`, 11.8) vs Lindhard constant (italic, 19.3) | b | scope note | ch11/s11-8, ch19/s19-3 |
| ω_max: ion→electron max (19.2) vs phonon-band top (11.3, 11.5, 11.6, 17.1, 21.2, D.46, E.9, E.17–E.20) | b | 19.2 is local (3 uses), but the phonon meaning is book-wide, so a rename to ω_max^{N→e} is advised. Also: rows l.1204 and l.1484 are duplicates (keep l.1204, first use 11.3) | ch19/s19-2 |
| Γ_abs: per quantum of DM field vs per phonon in the film solve (20.5) | b | Ch20 only; scope note (optional Γ_abs^film) | ch20/s20-5 |
| Γ₀: tunneling prefactor (19.6) vs attempt rate (E.11) | c | Same quantity (attempt-rate prefactor of Γ = Γ₀e^{−V_b/T}), also 16.8 and E.22. One row, first use 16.8 | ch16/s16-8, ch19/s19-6, appE/E-11, E-22 |
| T_d: point group (italic; 5.4, 7.4, 10.7, C.3, C.17) vs neutron temperature (`T_{\mathrm{d}}`, 14.4) vs damage energy (`T_{\mathrm{d}}`, 16.6, 19.3, 19.4) | b | Upright T_d carries two meanings in separate chapters. Rename the 14.4 temperature to T_meas (3 uses) to free T_d for Lindhard | ch14/s14-4 |
| U: molecular-magnet barrier (14.5) vs Sarkis binding energy (19.3) | b | Bare U is local everywhere (also unitaries); scope notes | ch14/s14-5, ch19/s19-3 |
| N_X: excitons per recoil (`N_{\mathrm{X}}`, 16.6, 22.2) vs bound pairs at readout (italic N_X, 18.5) | b | Related, but different stages; scope notes. Optionally make 18.5 N_X^ro | ch18/s18-5 |
| Ξ: deformation constant (6.2, 6.3, 13.6, 20.1, E.17, E.18) vs velocity measure (C.12, 21.2, D.46) | b | Never in one section; scope notes | — |
| ξ: energy mismatch (2.1, 2.4) vs one step ln(x_{j+1}/x_j) (D.44) | b | The writer's "rate exponent" is ϰ, not ξ. Scope note | appD/D-44 |
| ν: Lindhard reduced frequency (4.5, D.8) vs phonon branch (5.2 on) | b | NOTATION already marks it local | ch04/s4-5, appD/D-8 |
| σ_ω: impulse width (11.4) vs Doppler width (16.6) | c | Same quantity: (4E_R E^kin)^{1/2} = (E_R⟨ω⟩)^{1/2} for a harmonic site. Keep l.883 (11.4); 16.6 refers to it | ch11/s11-4, s11-5, ch16/s16-6, ch19/s19-1, appD/D-32 |
| Θ_D: l.485 vs l.1164 | c | Same meaning; keep l.485 (5.2), drop Θ_D from l.1164 | — |
| α_M: magnetoelectric coefficient (14.5) vs Madelung constant (E.10) | b | scope notes | ch14/s14-5, appE/E-10 |
| γ_n: mode width (11.8, 14.6) vs neutron moment (C.19) | b | scope notes | appC/C-19 |
| ℓ₀: l.887 vs l.1356 | c | Same quantity (2Mω₀)^{−1/2}; one row, first use 5.6 | ch05/s5-6, ch08/s8-6, ch11/s11-5, ch12/s12-1, appC/C-6 |
| d_k: spin–boson bath operators (italic k) vs kink width `d_{\mathrm{k}}`, both in C.20 | **a** | They meet in C.20. Rename the kink width to `d_{\mathrm{kink}}`, as NOTATION l.1409 already plans | appC/C-20 (11), ch19/s19-6 (7), ch19/s19-summary (1), appF/F-rows (3) |
| ω_k: bath (C.20) vs vibronic mode (E.10) | b | Separate appendices; ω_k is a generic mode energy elsewhere | appC/C-20, appE/E-10 |
| z_p: D.3 vs 4.1 | c | Same object (a pole of the continuation, both `z_{\mathrm{p}}`); one row at 4.1 | ch04/s4-1, appD/D-3 (C.5 writes italic z_p: align) |
| 𝗍: test statistic (14.6) vs −2 ln likelihood ratio (C.14, 8.8) | c | 14.6 uses "the likelihood ratio 𝗍 of eq:C.14-ratio": the same symbol. One row (first use 8.8) | — |
| j_L: longitudinal current (`j_{\mathrm{L}}`) vs spherical Bessel with index L (E.2, E.7) | b | Spellings differ; scope note | appE/E-2, E-7 |
| New: f₁, f₂: Lindhard bracket f₁ + if₂ (10.3) vs atomic scattering factors (10.7, 17.5) | **a** | Same chapter, and both feed ε. Rename the 10.3 bracket (2 uses) to f^L_1 + i f^L_2. NOTATION l.826's pointer to 4.5 is stale (4.5 has no f₁) | ch10/s10-3 |

Duplicates (writer-notes §2) and the row to keep:

| Symbol | Keep | Note |
|---|---|---|
| M_cell | l.475 (1.5) | drop from l.1049 |
| N_at | merge into l.1414 | l.402 (4.2, atoms of a gas sample) becomes a scope note "(4.2: atoms of the sample)"; first use 4.2 |
| V_b | l.1166 (16.7) | drop from l.1500 |
| V_bias | l.123 (1.5) | drop from l.1276 |
| c_k | l.732 (8.5) | merge l.884 as "also 11.4, 11.5, 12.5, D.32"; units eV^k |
| m_h | l.311 (3.3) | units "eV; m_e" (l.458 has eV, l.311 has m_e) |
| E_el | not a duplicate | l.526 is the electronic energy of a configuration; l.1264 is the energy a recoil gives to electrons: b, with scope notes |
| b_br | l.1168 (16.8) | drop from l.1285 |
| N_casc | l.1168 (16.8) | l.1285 is the same; l.1513 (E.13, number of simulated cascades) is a different meaning: b |
| 𝗀_λ | l.1372 meaning, first use 21.2 | drop from l.1324 |
| ϵ_Luke | l.1274 (19.5) | drop from l.1316 |
| Δ_w | l.151 (2.1) | drop l.217 or fold "also 2.4" |
| Ω_at | l.891 (11.6) | drop from l.1502 |
| Added: ω_max l.1204/l.1484; Θ_D; θ_s; z_p; ℓ₀; σ_ω; Γ₀; 𝗍 | see clash table | |

## 5. Build

- App B is printed pp. 1305–1363 (PDF pp. 1317–1375); the PDF is newer than all appB tex. No "??" and no undefined references in App B.
- The log has three overfull hboxes in B-1, all ≤ 1.2 pt: B-1 l.121 and l.768 (units "cm⁻² kg⁻¹ yr⁻¹" in the 0.14\textwidth
  column) and l.1353 (21.7 row, from the "(21.7)" in its symbol cell). These are cosmetic. The longtable breaks cleanly; group
  headings and the repeated header are correct on every page checked.
- Cosmetic: the 0.06\textwidth "First use" header wraps to two lines ("First / use"). Use a shorter heading ("Sect.") or a
  wider column. B-2: one Underfull \vbox at the page break; B.2 and B.3 have no overflow.
