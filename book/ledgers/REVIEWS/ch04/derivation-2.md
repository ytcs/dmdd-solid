# Ch4 part 2 (4.6–4.9, D.10–D.12): derivation check
Verifier: isolated derivation pass (long-form-writing SKILL §5). Algebra was redone in sympy and the numbers in numpy/scipy. The scripts were session-local and are not retained. No QE runs.
Sources were fetched with lit.py into sources/review-ch04b/ and the PDFs deleted afterwards: arXiv 2004.10709, cond-mat/9712013, 1807.10291, 2006.09440, cond-mat/0109434, 2101.08275, cond-mat/9803194.
Conventions checked against NOTATION: HL charge e² = 4πα, v_C = e²/k², 𝒩_F per spin, ρ_mn(k,q) = ⟨m,k+q|e^{iq·r}|n k⟩, ω_p² = e²𝓃_e/m_e.
Legend: CHECKED / WRONG / GAP / FIG-PASS (not checked; re-check after the figure pass). "Known" means the item is already in editor-notes.md.

## Summary of findings (action items)
1. **WRONG, 4.7 l.89, eq:4.7-ImSigma.** The text has Im Σ^R = −π𝖠|𝖦^R|². It must be **Im Σ^R = −π𝖠/|𝖦^R|²**. Derivation: Im(−1/𝖦) = Im𝖦/|𝖦|² = −π𝖠/|𝖦|² (checked in sympy). The sign conclusion (≤ 0) is unaffected. The sentence before it ("has the imaginary part Im𝖦^R/|𝖦^R|²") is already right; only the display is wrong.
2. **GAP, 4.8 keyresult (Feynman rules), last sentence.** The zero-temperature rules list the changes for 𝖦 but not for the response. For the time-ordered response R^T = −(i/V)⟨T O_a†(t)O_b⟩, the prefactor becomes **+i/V** instead of −1/V. Derivation: (−i)(−i)^n i^{2n+2} = i·i^n, and the iⁿ goes into the lines. Check: R⁰ = (i/V)(−1)Σ∫dω/2π 𝖦₀𝖦₀, which is the Fetter–Walecka Π⁰ = −2i∫𝖦₀𝖦₀. Add a clause to the rules: "and the response carries +i/V in place of −1/V". D.11 (§ "The rules at zero temperature") does not cover the response either; add one line there.
3. **WRONG (known, confirmed), D.11 l.3, Bruus–Flensberg chapters.** Oxford Academic lists "Imaginary-Time Green's Functions" as Chap. 11 (pp. 184–203) of the 2004 edition, which has 19 chapters. Under that numbering D.11's "Chaps. 10 and 11" should read **Chaps. 11–13** (imaginary time, external-potential diagrams with Wick's theorem, and pair-interaction (Coulomb) diagrams, which is what D.11 derives). 4.7's "8, 9 and 11" is then correct. 4.8's "12–14 and 17" (external-potential and pair-interaction diagrams, RPA, phonons) matches the editor's ruling. The full TOC page could not be fetched (403/503), so this rests on the OUP chapter page and the search listing.
4. **WRONG (minor number), D.10 l.67.** The text says the direct Matsubara sum "agrees with the closed form to 10⁻⁵, the size of the truncation error". Recomputed with |j′| ≤ 2×10⁶, T = 20 meV, ξ = −11 and 27 meV, j = 0, 1, 3: the difference is **1.27×10⁻⁶ eV⁻¹** absolute (relative 1.1×10⁻⁷ to 1.1×10⁻⁶). This equals the analytic tail 1/(2π²TN). Replace with "to about 10⁻⁶ (relative), the size of the truncation error".
5. **WRONG (known, pending relabel), D.12 vs 4.9.** D.12 defines K^x with the G = 0 term (eq:D.12-crystal sums over all G) and K̄^x without it. 4.9 says "eq:4.9-bse is eq:D.12-eig with the kernels of eq:D.12-crystal", but eq:4.9-kernels uses G ≠ 0. These disagree until the ruled relabel is done (K̄^x → K^x, K^x → K^x_full). Places to change: eq:D.12-crystal, l.83 ("With K^x replaced by its local-field part K̄^x"), l.114, eq:D.12-eps2 (Ā, Ē). Also l.114 must say that eq:D.12-Rexc "with the full kernel" uses K^x_full.
6. **WRONG (convention), D.12 eq:D.12-crystal and 4.9 eq:4.9-kernels (K^d).** Expanding eq:D.12-kernels with D.12's own convention, W(r,r′) = V⁻¹Σ e^{i(p+G)·r}W_GG′(p)e^{−i(p+G′)·r′}, gives with no symmetry assumption **K^d = V⁻¹Σ_GG′ ρ_cc′(k′+q, p+G) W_GG′(p,0) ρ_vv′(k′, p+G′)*, p = k − k′** (the standard order). The printed form, with p̃ = k′ − k, equals this with W_{−G,−G′}(−p) = W_GG′(p)* (static time reversal plus Hermiticity) in the W slot. So it is right only when W_GG′ is real, i.e. with inversion symmetry: true for Si, false for GaAs (WE 4.10, E.6). W(r,r′) = W(r′,r) is not sufficient. Rewrite both displays in the standard order.
7. **GAP (known: spin factor), 4.6 l.11/l.14.** eq:4.6-R0 still has a plain "2/V" and the prose says "a factor of two". The 4.9 ruling is g_deg = 2 throughout Ch4. NOTATION's g_deg row ("first use 7.3", meanings "of χ … spin × cone") must gain the meaning "spin degeneracy of the bubble and the singlet exciton (4.6, 4.9; E.6)", with first use 4.6.
8. **Notation drift (NOTATION).**
   - (a) 4.8 l.86 and l.163 define a bare local ξ = ξ_{k−Q}. Bare ξ is reserved for the energy mismatch (row 135). Write ξ_{k−Q} out, or use a decorated local symbol.
   - (b) 4.7 l.14 and WE 4.7 use E_k for the orbital energy. The NOTATION row 381 E_k is the Bogoliubov energy (7.2). The row ξ_k (from the Fermi level) has its first use in 4.7, not 7.2.
   - (c) WE 4.7 uses E_d for the level energy, which clashes with row 392 (E_d = displacement threshold, 7.4). Rename it (e.g. E_lev) or flag the clash.
   - (d) Symbols with no NOTATION row: 𝖣₀ (boson propagator), 𝖫/𝖫⁰ (pair propagator), 𝖥^R, E_qp, Γ_qp, Γ_em, Γ_out/Γ_in, ω_Ein (accepted by the editor, row still missing), ω_Q (generic boson energy; entry 27 reserves ω_Qν for phonons), V_k (hybridization), B(q,ω′) (spectral weight of W^scr), K̄^x/K^x_0 (until the relabel), ℓ(x), E_c (band bottom in WE 4.8, rename or row), the IP superscript of ε₂^IP.
9. **Cross-reference consistency.** D.12 l.123 cites eq:A.5-optical for the optical vertex, while 4.6 and 4.9 cite eq:3.2-optical for the same formula. Use one label.
10. **Known, outside these files.** E.6 (eq. after E.6-Hexc) still writes the oscillator strength |Σ A ρ|² without the conjugate. D.12 and 4.9 have |Σ A ρ*|², which is correct.
11. **WRONG (tiny, belongs to 4.5), 4.9 summary l.158.** "6.27 keV": ω_p/v_max with v_max = 794.5 km/s (NOTATION) is 16.596 eV / 2.6502×10⁻³ = **6.26 keV** (1.755 k_F). The value 6.27 comes from rounding v_max to 0.379 v_F. Fix in 4.5 and the summary together.

## 4.6
- l.11, resonant and antiresonant terms, Pauli cancellation f_n(1−f_m) − f_m(1−f_n) = f_n − f_m: CHECKED.
- eq:4.6-R0 (Adler–Wiser): sign, conjugation and Lehmann matrix-element ordering all agree with eq:4.4-RGG and eq:4.1-lehmann. Dimension [E²]. CHECKED. Equals eq:E.6-R0 with g_deg = 2. Spin factor: see item 7.
- eq:4.6-head, from the pairs (v,c) and (c,v) with ρ_cv = q·v_cv/Δ: CHECKED. O(q²) as D.7 requires: CHECKED.
- eq:4.6-eps2, ε₂ = −v_C Im R₀₀ = (2πe²/V)Σ|q̂·v|²/Δ² δ: CHECKED. Equals the Gaussian textbook 8π²e_G²/(Vω²)Σ|e·v|²δ.
- eq:4.6-static, bracket = −2/Δ at ω = 0 (sympy): CHECKED. Kramers–Kronig consistency with eq:4.6-eps2, 1 + (2/π)∫ε₂/ω: CHECKED.
- l.39, scissor leaves ρ_cv unchanged, so the terms scale as |ρ/q|²/Δ: CHECKED. "PBE 13.04 vs 11.7" agrees with 3.4/E.1: CHECKED.
- eq:4.6-rpa, eq:4.6-rpaLF (= eq:D.7-macbar): CHECKED. Harmonic-mean capacitor argument: CHECKED.
- l.62–71 and Fig. 4.7 numbers: FIG-PASS. These are 4.26, 41, 46, 15, 36, 34, 4.32, 13, 11.45, 10.22, 10.81, 37, "two to three orders", 10–35 %, 7.6 → 3.4, "about a tenth", "about half", and in l.3 "within a few percent".
- l.71, Knapen et al.: "small difference in rate with or without LFE" (Si, Ge). Their Sec. III B and App. B (Fig. 5) say exactly this: CHECKED.
- l.62, Albrecht 1998: LF moves strength to higher energy and weakens E₁ (their text): CHECKED. Louie 1975: paywalled, attribution only.
- eq:4.6-fxc, eq:4.6-tddft and R̃ = (1 − R⁰f_xc)⁻¹R⁰ from R = R̃ + R̃vR: CHECKED.
- eq:4.6-alda, local and instantaneous kernel, negative: CHECKED. Head and wings drop out as q → 0 (O(q²) and O(q)): CHECKED.
- l.108, Reining 2002, long-range kernel −α/q² (their abstract and Eq. context): CHECKED. NOTATION α_xc row exists (E.6); the text writes α_xc: CHECKED.
- eq:4.6-GLF, f_xc = −v_C G_LF, from equating the two forms of ε: CHECKED.
- eq:4.6-compress, ∂μ/∂n = 1/(2𝒩_F) + f_xc(q→0): CHECKED (R⁰ = −2𝒩_F, 𝒩_F per spin).
- l.128–130, ε_x = −3e²k_F/16π² (HL), v_x = 4ε_x/3, f_x = v_x/3n = −e²/4k_F², G = q²/4k_F² (sympy): CHECKED.
- l.132, Perdew–Zunger at r_s = 2 gives coefficient 0.2674 (0.267): CHECKED. k_TF²/k_F² = 1.3304 (1.33): CHECKED. Compressibility ratio 1/(1 − 0.267×1.33) = 1.552 (1.55): CHECKED.
- l.134, q₀/k_F = 1.045 (1.04): CHECKED. G_LF(q₀) = 0.292 (0.29): CHECKED. Static Lindhard ε(q₀,0) = 2.1007: CHECKED. With G_LF: 2.622 (2.62): CHECKED. Ratio 1.25 ("a quarter"): CHECKED.
- l.140, "ten percent", "25 percent": FIG-PASS (derived from the rung values).
- WE 4.11 (we:4-siepsinf): FIG-PASS, except the following. 13.04/11.7 = 1.115 (11 %): CHECKED. PBE gap 0.602/1.17 = 0.51 ("about half"): CHECKED. (11.45/10.22)² = 1.255: arithmetic CHECKED, inputs FIG-PASS.
- Dimensions: eq:4.6-R0 [E²] (1/V × 1/E); eq:4.6-eps2 and eq:4.6-static dimensionless (e²/V × E⁻² × E⁻¹, with v_cv dimensionless); f_xc and v_C [E⁻²]; eq:4.6-compress [E⁻²] on both sides (𝒩_F [E²]): CHECKED.
- Typo l.143: "and and with 113 vectors".

## 4.7
- eq:4.7-GR and 𝖦^R(0⁺) = −i: CHECKED. eq:4.7-G0: CHECKED.
- eq:4.7-lehmann and eq:4.7-A, signs of both terms: CHECKED. Normalization, and the removal part = 𝖠n_F via relabeling and detailed balance: CHECKED. eq:4.7-occ: CHECKED.
- eq:4.7-GT and eq:4.7-GTlehmann, i∫_{−∞}^0 e^{i(ω+E)t+0t} = 1/(ω+E−i0): CHECKED.
- l.72, Im𝖦(z) = −Im z∫𝖠/|z−ω′|² < 0 (no zeros in the UHP): CHECKED. eq:4.7-dyson: CHECKED.
- **eq:4.7-ImSigma: WRONG (item 1).**
- l.92, high-frequency limit Σ → m₁ − ξ = ⟨{[c,H_int],c†}⟩: CHECKED.
- eq:4.7-qp, expansion, z_qp and Γ = −2z ImΣ: CHECKED. Time form −iz e^{−iEt−Γt/2}: CHECKED.
- l.114, phase-space triangle ξ²/2: CHECKED. Luttinger attribution: CHECKED (standard).
- eq:4.7-G0W0, linearized QP equation: CHECKED. Ramanathan Eq. (11), E_g(0) = 1.1692 eV (→ 1.17): CHECKED against source. 0.602 eV agrees with E.1: CHECKED.
- WE 4.7 (we:4-level):
  - Equations of motion and eq:4.7-Sigmad: CHECKED. Equals D.3's R(z) at z = ω − E_d: CHECKED.
  - slope 2Γ/(πE_w) = 0.006366 (0.0064), z = 1.0064, peak 2/(πΓ) = 63.66 eV⁻¹: CHECKED.
  - Exact/Lorentzian ratio 1.0103 at Γ and 1.0130 at 10Γ (1.0 %, 1.3 %): CHECKED.
  - ∫𝖠 = 1 + 4×10⁻⁸ on the grid (< 10⁻⁶): CHECKED. Lorentz weight outside the band 0.006366: CHECKED.
  - Bound states at δ ≈ 10^{−136.4} eV: CHECKED. ⟨d†d⟩ = 0.78749 (0.787) and n_F(E_d) = 0.8176 (0.818): CHECKED.
- Fig. 4.8b caption, continuum Σ_d and the same numbers: CHECKED.
- eq:4.7-Gmats and l.175 transform −(1 + e^{−βE})/(iω − E) (sympy): CHECKED. eq:4.7-continuation: CHECKED.
- l.193, Res n_F = −T, jump −2πi𝖠: CHECKED. Fig. 4.9 caption (contour orientations): CHECKED.
- eq:4.7-Rmats, bosonic transform (e^{−βE} − 1)/(iω − E), β term: CHECKED. eq:4.7-Rcont: CHECKED.
- Kubo attribution (isolated vs isothermal; the extra β term) is consistent with Kubo 1957 §(isothermal/adiabatic susceptibilities). Paywalled, so attribution only: CHECKED (known).
- eq:4.7-bubble, sign and frequency sum (sympy residues): CHECKED.
- Dimensions: 𝖦(ω) and 𝖠 [E⁻¹]; Σ [E]; 𝖦(iω) [E⁻¹]; R(iω) [E²]: CHECKED.
- Citations: Fetter–Walecka Chap. 3 (fermion Green's functions, field theory) and Chap. 7 (finite temperature); Mahan 3rd ed. Chap. 2 (T = 0) and Chap. 3 (T ≠ 0): CHECKED from the standard TOCs (books, not fetched).

## 4.8
- eq:4.8-contract and the rules list (Matsubara): CHECKED against D.11 counting. Line −v/V, loop −1, response −1/V: CHECKED.
- T = 0 rules: 𝖦 part (iv/V per line, ∫dω/2π, 𝖦₀ with i0 sgn ξ) CHECKED. **Response prefactor: GAP (item 2).**
- l.32, sign bookkeeping for R, (−1)^n into the lines, 2n + 2 contractions: CHECKED.
- eq:4.8-bubble: CHECKED. l.52, two-loop first-order term = +R⁰v_C R⁰: CHECKED. eq:4.8-chain: CHECKED.
- §4.8-removal (thermodynamic-limit argument, 1/N): CHECKED, qualitative and consistent with D.7.
- Boson self-energy, residues at ±ω_Q and at iω − ξ, n_B(iω^F − ξ) = −(1 − n_F) (sympy, full expression): CHECKED. eq:4.8-sigmaboson: CHECKED.
- l.98, T = 0 limit and correspondence with eq:4.7-Sigmad (V_k ↔ g/√V): CHECKED.
- WE 4.8 (we:4-einstein):
  - ℓ(x) and Im ℓ = −π in the band: CHECKED. n_F(E_c) = 3.98×10⁻⁹ (≤ 4×10⁻⁹): CHECKED.
  - ReΣ(E_c) = −9.141 meV, slope −0.05005, z = 0.952: CHECKED. Self-consistent shift −8.734 meV: CHECKED.
  - T = 25.852 meV, n_B = 0.1089: CHECKED. z(300 K) = 0.9530, Γ_qp = 2.075 meV (prints 2.08), τ = 0.317 ps: CHECKED.
  - Shift −11.090 meV: CHECKED. Ratio to (2n_B+1)×T = 0 value 0.9963 (0.4 %): CHECKED. In-band width 24.35 meV (24.4): CHECKED.
  - Caption Γ_em n_B = 2.18 meV (2.2): CHECKED. Direct bosonic sum (2×10⁶ frequencies) agrees to machine precision (≤ 10⁻⁹ claimed): CHECKED.
- eq:4.8-W, W = v + vRv = ε⁻¹v; crystal W_GG′ = ε⁻¹_GG′ v(|q+G′|): CHECKED.
- eq:4.8-GWmats and eq:4.8-GW: consistent with rule factors. Aryasetiawan–Gunnarsson Eqs. (60) Σ = iGW and (61) (with ω+ω′, equivalent by the evenness of time-ordered W), and Hedin's equations (43)–(46) with the vertex (45): CHECKED against source.
- l.143, B = −ImW^R/π = v_C L/π: CHECKED. Free-boson B reproduces 𝖣₀: CHECKED. Spectral Σ formula reduces to eq:4.8-sigmaboson for a single boson: CHECKED.
- eq:4.8-lifetime, (1 − e^{−βω′})(n_B + 1 − n_F) = 1 − n_F + e^{−βω′}n_F (sympy), with 2L/v = (1 − e^{−βω})S from eq:4.4-SL: CHECKED. Dimensions: [v²][q³][S] = E⁻⁴·E³·E² = E: CHECKED.
- eq:4.8-cutsigma, the occupation splits and Γ_in = e^{−βω}Γ_out for both deltas (sympy): CHECKED. Cutting-rule keyresult: CHECKED.
- WE 4.9 (we:4-cut), Pauli difference = (1 − e^{−βω})n(1 − n′): CHECKED.
  - k_F = 3.569 keV, E_F = 12.46 eV (12.5), q₀ = αm_e = 3.729 keV, ω₊ = 39.65 eV (39.7): CHECKED.
  - Unblocked fraction 3x/4 − x³/16 = 0.712: CHECKED (formula).
  - The MC histogram "0.6 % rms" and "10⁻⁴" were not rerun (stochastic, figure-script output); the closed form was CHECKED.
- Dimensions: [g]² = E⁻¹ from H_int = V^{−1/2}Σ g c†cφ, so (|g|²/V)/E = E in eq:4.8-sigmaboson; 𝖣₀ [E⁻¹]; (W/V)·T·𝖦 = E in eq:4.8-GWmats; B [E⁻¹]: CHECKED.
- l.155, plasmon 16.4 eV: consistent with 4.4: CHECKED.

## 4.9
- eq:4.9-bse and eq:4.9-kernels: index placement checked against D.12 (see items 5 and 6). Sign (+g K^x − K^d) and singlet g_deg = 2: CHECKED.
- Sell 1972, GaAs 4.2 meV, and Shaklee–Nahory 1970, Si 14.7 meV: values standard. Paywalled, so attribution only.
- l.29, e²/(4πε∞r) (HL): CHECKED. l.31, ω_p = 16.596 eV (16.6) from 𝓃_e = 32/a³: CHECKED.
- l.33, K^d → 0 gives D + gXXᵀ, and Woodbury gives R̄ = R⁰ + R⁰v̄R̄: CHECKED.
- Wannier–Mott:
  - K^d ≈ e²/(Vε∞|k−k′|²): CHECKED. FT e²/(εk²) → α/(εr) with e² = 4πα: CHECKED.
  - eq:4.9-envelope and eq:4.9-WM (μα²/2ε², a_x = ε a₀ m_e/μ, Ry = 13.606 eV): CHECKED. |F_ns(0)|² = 1/(πa³n³): CHECKED.
- l.68, Si estimate:
  - ⟨1/m⟩ with 0.916/0.191 gives 0.2595 m_e (0.26): CHECKED. m_hh 0.277/0.718 (tab:3-materials): CHECKED.
  - E_b = 13.3 to 18.9 meV ("13 to 19"): CHECKED. μ_x = 0.1479 (0.148), a_x = 4.19 nm, a_x/a = 7.7 ("nearly eight"): CHECKED.
  - 1/a_x = 0.0239 Å⁻¹, |G₁₁₁| = 2.004 Å⁻¹, ratio 1.2 %: CHECKED. Matches the fixed E.6 (μ_x 0.15, a_x 4.2 nm): CHECKED.
- WE 4.10 (GaAs):
  - γ₁ = 6.98 is consistent with tab:3-materials (m_hh = 0.350, m_lh = 0.090 along [100] give γ₁ = 6.98). m_e/μ = 21.905, μ = 0.04565: CHECKED.
  - E_b(10.89) = 5.24 meV, a_x = 12.6 nm, 22 a: CHECKED. E_b(12.9) and a_x: the printed 3.73 meV and 15.0 nm follow only from the unrounded μ = 0.04565. **WRONG (minor):** with the printed inputs (μ = 0.0457, a₀ = 0.529 Å) a reader gets **3.74 meV** and **14.9 nm**. Either print μ_x = 0.04565 or change the values to 3.74 and 14.9.
  - 5.24/4.2 = 1.25 ("a quarter"), remainder 0.47 meV (0.5), 35/4.2 = 8.3 ("eight times"): CHECKED.
  - Griffin et al. Table I, GaAs ε₀ = 12.9 and ε∞ = 10.89: CHECKED against source. Fig. 2 (phonon spectra; GaAs optical branch ~33–36 meV): CHECKED. Baldereschi–Lipari: attribution only.
- eq:4.9-dispersion, centre-of-mass separation (sympy): CHECKED.
- eq:4.9-epsmac and eq:4.9-eps2:
  - Prefactors g e²/(Vq²), π…δ, 2g…/E_λ: CHECKED. Reduce to eq:4.6-eps2 and eq:4.6-static without kernels: CHECKED.
  - Matches eq:D.12-eps2 and the 8π²α/(Ωω²) reduction: CHECKED.
- eq:4.9-elliott, Σ_k A_k = V^{1/2}F(0): CHECKED. Elliott attribution: CHECKED (standard).
- eq:4.9-S, S = (2q²/e²)ε₂/|ε|² at T = 0: CHECKED. WM line form 2πg|ρ|²|F|²/|ε|²: CHECKED.
- l.140, 14.7/1170 = 1.26 % (1.3): CHECKED.
- l.116–127 and Fig. 4.11 numbers: FIG-PASS. These are 81 meV, 3.4 %, 3.13 eV, 34 at 3.36 eV, 3.88 eV, 0.36 eV, +17 %, the "11.9" ε∞ estimate, 36 % at 3 eV, 3.5 % at 4–6 eV, and l.146 "a third", "13 to 34".
- l.27, "q = q_r + G_q … omitted term at G = G_q": correct only when the kernel is written with q_r. GAP (wording): say "with q_r in eq:4.9-kernels, the omitted term is G = G_q".
- Dimensions: K^x, K^d, H^exc [E] (v_C/V); eq:4.9-epsmac and eq:4.9-eps2 dimensionless; eq:4.9-S and the WM line form [E²] (|F(0)|² = E³); eq:4.9-WM energy and length: CHECKED.
- Summary (l.150–168):
  - Restated part-1 values: k_TF/(ε∞−1)^{1/2} = 1.258 keV (1.26), ω_p 16.6, ε(q₀) = 2.10: CHECKED. q_c = 2.60 keV: taken from 4.5, not recomputed.
  - 6.27 keV: item 11. Part-2 values: as above, or FIG-PASS.
  - l.166, "E_x^b = μα²/2ε∞²: 14.7 meV … in silicon" presents the measured value as the formula's output. Suggest "measured 14.7 meV (radius 4.2 nm from the formula)".

## D.10
- Antiperiodicity by the cyclic trace (each cycling step redone): CHECKED. Fourier bracket 1 ∓ e^{−inπ}: CHECKED.
- l.23, symmetric value n − ½ (also TΣ_sym 1/(iω−ξ) = −½tanh(βξ/2)): CHECKED.
- eq:D.10-occ, contour orientation and arcs: CHECKED. Level check: Matsubara sum 0.787488 vs integral 0.787488: CHECKED.
- eq:D.10-R0, τ evolution, n_k(1 − n_{k+q}), numerator identity: CHECKED. Im part: CHECKED.
- eq:D.10-sum, residues with the fermionic eq:C.5-matsum sign (sympy): CHECKED. **Numerical-check wording: item 4.**
- Continuation and uniqueness: CHECKED. The six-level check was not rerun; it is consistent with eq:4.7-Rmats, which was verified analytically.

## D.11
- U_I(τ) derivative, ordered exponential, e^{−βH} = e^{−βH₀}U, c(τ) = U⁻¹c_I U: CHECKED. eq:D.11-Gexp: CHECKED.
- eq:D.11-GT (Gell-Mann–Low; assumptions stated): CHECKED.
- Gaudin proof: (−1)^j signs, A₁e^{−βH₀} = e^{−βξ₁}e^{−βH₀}A₁, ⟨cc†⟩ = 1 − n_F, boson 1 + n_B (sympy): CHECKED.
- Linked-cluster binomial factorization: CHECKED.
- Sign rule: open line (−1)^{m+1}, loop (−1)^m·(−1), total (−1)^n(−1)^F, hence −v/V per line: CHECKED. n!2ⁿ and frequency/momentum counts (n + 1 factors β): CHECKED.
- Hartree (+v(0)N_e/V) and eq:D.11-fock: CHECKED.
- Boson: 𝖣₀(τ) and eq:D.11-D0 transform (sympy): CHECKED. (−1)^m(−1)^F counting and eq:D.11-boson: CHECKED. Static attraction −2|g|²/ω_Q: CHECKED.
- T = 0: −i(−i)ⁿi^{2n+1}(−1)^F = iⁿ(−1)^F: CHECKED. Fock contour gives −Θ(−ξ): CHECKED. 𝖣₀(ω) = 2ω_Q/(ω² − ω_Q² + i0): CHECKED. Response prefactor missing: item 2.
- **Bruus–Flensberg chapter numbers: item 3.**

## D.12
- eq:D.12-L and eq:D.12-R (n(q)† = Σρ*c†_n c_m): CHECKED. eq:D.12-L0, contraction sign → 𝖦_m(τ)𝖦_n(−τ), and frequency sum: CHECKED.
- First order: L⁽¹⁾ = +∫⟨…H…⟩. Exchange (two loops) +L⁰v_{mn′,nm′}L⁰. Direct (one loop) −L⁰v_{mn′,m′n}L⁰. Index matching to eq:D.12-kernels: CHECKED.
- Exchange reproduces the RPA chain with + sign: CHECKED.
- Static ladder and eq:D.12-BSE: CHECKED. Spin singlet gK^x − K^d and triplet −K^d: CHECKED.
- eq:D.12-Lsol (F² = 1) and the eq:D.12-blocks structure: CHECKED.
- Blase et al. Eq. (18) (R, C; −C*, −R*) and Eq. (20) (κ(ia|jb) − W, κ = 2 singlet): CHECKED against source.
- eq:D.12-crystal: K^x CHECKED (but item 5); K^d item 6. 1/V scaling: CHECKED.
- eq:D.12-Rexc and eq:D.12-S (S = −2ImR at T = 0): CHECKED.
- Rank-one head closure: CHECKED. eq:D.12-epsmac (= eq:D.7-macbar): CHECKED. eq:D.12-eps2 and its 8π²α/(Ωω²) reduction: CHECKED.
- l.130, four-spin-orbital numerical check: not rerun. The stated outcome (quadratic error with the correct signs and indices) is consistent with the analytic check above.
