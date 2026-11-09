# Ch15 part 2: derivation check (15.3, 15.4, summary, D.40, ch15.tex)
Reviewer: derivation verifier (isolated), 2026-11-06. Scope: tex/ch15/ch15.tex, s15-3.tex, s15-4.tex, s15-summary.tex, tex/appD/D-40.tex.
Method: sympy for each algebraic step (scratchpad sym.py); my own implementation, written without the figscripts, for every number (num.py, sc.py: Lindhard/Mermin, Mattis–Bardeen σ₁/σ₂ via my own Kramers–Kronig, closed forms against direct quadrature, Holstein ratios, rates). Figscripts logs used only to locate discrepancies. Sources read: 1604.06800 (HLZ), 2101.08263 (+SM), 2412.16279 (+SM), 1607.07854 (Zhang Table I), cond-mat/9604124 (Savrasov Table IV), 2110.01587 (Lasenby–Prabhu), 2609.06423 (Gan). Allen 1971, Anderson 1959 and Mattis–Bardeen 1958 are closed access and were not read.
Verdict key: CHECKED = redone and agrees; WRONG = error, correction given; GAP = correct but missing a qualifier, a source, or a size.

## A. Priority items (editor notes and brief)

A1. eq:15.3-sheet and the factor [(ε_a+ε_b)/(q_∥d)]² — CHECKED, with a GAP on its size and its source.
 - Derivation redone. The 2D Fourier transform of 1/4πr is 1/2q (sympy), and image charges turn 2 into ε_a+ε_b. The ratio of the sheet kernel to the bulk kernel is q_∥d/(ε_a+ε_b) (sympy), and the enhancement holds while |ε_sh| ≫ 1. At the WE point, (qd/2)|ε−1| = 4.46e5.
 - 540: (2/0.08605)² = 540.2 CHECKED. The bulk ε and the q value it uses are recomputed in A3.
 - Literature, against the editor note "not found stated": the result is the kd ≪ 1 limit of Lasenby & Prabhu, arXiv:2110.01587 Eq. (19) (slab in vacuum, k in plane; bib key lasenby2022dark already exists). I checked numerically that Im R(LP)/Im R(sheet) → 1 + O(kd) for ε = 3e5+1e7i, 10+5i, −50+2i and 2+0.1i.
 - GAP (size): the next order is +qd. The exact slab of LP Eq. (19) gives 588 at qd = 0.086 with the WE ε, which is 9 % above 540. Correction: "≈ 540 to leading order in qd (588 for the exact slab, Lasenby and Prabhu Eq. (19))", and cite lasenby2022dark in 15.3-sheet. In the summary table row, say "×540 (leading order in qd)".
 - WRONG (paraphrase of QROCODILE): the SM says the anisotropy "becomes very large at q ∼ O(1/nm), about 100 eV, and already appears significant at q ∼ 1 keV for energies above 4 eV". The book's "finds the anisotropy setting in at q ∼ 1 nm⁻¹" should read "finds it very large at q ∼ 1 nm⁻¹ and already significant at q ∼ 1 keV (ω > 4 eV)". "Poisson's equation" is acceptable (the SM says Maxwell's equations for the potential, electrostatic). The model is "a single layer of WSi in vacuum" with a Drude ε. CHECKED.

A2. Dirty-film loss = ε₀ωρ_el and the ×24 — CHECKED.
 - eq:15.3-rho: σ = n e² l/(ħk_F) gives ρl = 3π²ħ/(e²k_F²) = 3.972e-16 Ω m², ρ(50 nm) = 0.794 μΩ cm, γ_rel = 26.32 meV, D = 5.634e-4 eV⁻¹ = 333 cm²/s.
 - Diffusive limit, by sympy from eq:15.3-mermin: the numerator is iq²D, the denominator ω+iq²D, and the result is eq:15.3-diff. L = ω/(k_TF²D) = ωγ/ω_p² exactly when |ε| ≫ 1. In SI, L = ε₀ωρ: units F·Ω = s, so L is dimensionless. Value 9.6174e-8.
 - WE numbers (all mine): ν_γ = 0.39733+11.6211i; 𝔣_L = (2.4488+0.1669i)e-3, within 0.44 % of the tail; ε_Mer = (0.3937+10.362i)e7; diffusion pole (0.7467+10.344i)e7; Dq² = 0.0650 meV; L_Mer = 9.636e-8 (+0.197 % over Drude).
 - Clean finite-q Lindhard (my code): ε = (1.1997+0.8989i)e8 and L = 4.000e-9, so the ratio is 24.09. The asymptote 6/πql is 22.19, and ω/qv_F = 0.397. All CHECKED.
 - Ballistic limit, by sympy: the fraction is 1 + iπω/2qv_F with γ cancelling, L = πωq/(2k_TF²v_F), and the ratio to the diffusive form is πql/6. CHECKED.
 - Fig. 15.2b thresholds — WRONG (grid artefact of film15.py, 40 points per decade). A root-finder gives L_Mer/L_D = 1.1 at ql = 0.642 (book 0.63) and the ballistic 10 % point at ql = 9.82 (book 10). Correct s15-3 l.79 to "q𝔩_e ≤ 0.64 … only from q𝔩_e = 9.8" and the summary table row to "0.64 < q𝔩_e < 9.8". At ql = 1.5 the ratio is 1.425, 1.81× the ballistic value: CHECKED.
 - The 1/l_e = 3.947 eV edge, reached by m_χ ≥ 745 eV ("0.75 keV"): CHECKED.

A3. Lindhard at ω+iγ_rel gives twice the Drude tail — CHECKED (Mermin settles it).
 - sympy: ε−1 = −ω_p²/(ω+iγ)² = (ω_p²/γ²)(1 + 2iω/γ + …), so L = 2ωγ/ω_p².
 - Numerically naive/Drude = 2.0000 at ql = 0.01 and 0.086, and 2.001 at 0.3. The Mermin form returns exactly the Drude tail (A2), so the factor of 2 is the number non-conservation of the bare substitution.
 - WE: ε_naive = (3.527+0.0240i)e5 and L = 1.923e-7, giving naive/Mermin 1.996, Im ratio 431 and |ε| ratio 29.3. CHECKED.
 - Attribution: HLZ-2021 Eq. (S.13) is Lindhard at ω+iΓ_p with a principal Log (read). QROCODILE SM: "We approximate ε by the Lindhard dielectric function … plasmon width Γ = 0.1 E_F", E_F = 7 eV, ω_p ≈ 10.8 eV. The implementation is not stated, and the book's hedged wording ("A width added as ω → ω+iγ … is this substitution") is correct. CHECKED.
 - Plasmon fit: 2101.08263 Fig. S1 gives (ω_p, Γ_p) = (14.9, 0.863) eV for a Fröhlich model with ω_g = 0, c = 1, which is Drude. 0.863/0.02632 = 32.8 ("33"). CHECKED.

A4. Mattis–Bardeen dirty-limit ratio (eq:15.3-MB) — CHECKED.
 - σ₂ by my own Kramers–Kronig from σ₁ = σ_n𝔤_II plus the condensate δ. Missing weight ∫₀^∞(1 − σ₁/σ_n)dω = 4.934802Δ = (π²/2)Δ (exact to 1e-11); σ₂/σ_n(2Δ) = 1.000.
 - L_s/L_n = 0.0451, 0.2352, 0.7440, 1.3024, 1.2587, 1.0742 at y = 2.05, 2.2, 2.5, 3, 5, 10, with σ₁ = 0.1395 and σ₂ = 0.7573 at y = 2.2. All match the text.
 - Clean conserving 0.868×1.5002 = 1.302; 1 μm 0.900; 30 nm 0.281; y = 3 range 1.333–1.417 (book table) — CHECKED.
 - GAP (l.104, "because D q² is not yet small"): at 30 nm and y = 2.2, D q² = 0.042Δ (book v_F). REF-DC-41 §4 attributes the 20 % excess to finite Dq² "not proved" and records a numerical floor. State the number and that the attribution is unproven.
 - GAP (DC-41 provenance): REF-DC-41 converts Γ to ℓ_mfp with v_F = 6.8e-3. With the book's 6.67e-3 its "30 nm" and "1 μm" are 29.4 nm and 0.98 μm. This is negligible, but the caption could say so. DC-RESULTS quoting rule (ℓ scope in the same sentence) is respected in 15.3. CHECKED.
 - Overlap with 15.2: the numbers are identical, so merging is an editorial decision.

A5. D.40 Nambu forms and amplitude collapse — CHECKED.
 - eq:D.40-O: the relabeling k → −k with Σf_k = 0 gives the unit matrix for odd weight and spin-independent s, and η for odd weight with s = ±½. Checked by hand and with the matrix algebra MᵀAM (sympy). eq:D.40-bogo reproduces exactly (u²+v² on the diagonal for the unit matrix; (u²−v², 2uv) for η).
 - Exact-state version: V_{ᾱβ̄} = −V_{βα} turns the spin-down term into Σ V_αβ c_ᾱ c†_β̄, the unit matrix. The pair amplitude is V_αβ(u_αv_β − v_αu_β), squared ½[1 − (ξξ′+Δ²)/EE′] (case II). The spin current, which is even under time reversal, gives the case-I combination. CHECKED.
 - eq:D.40-T: with O diagonal, T = J_iH/ω + J_fH/(−ω) = −(J_f − J_i)H/ω (sympy). Denominators: the second ordering has the boson still present, so E_i + ω − (E_m + ω) = E_i − E_m. CHECKED.
 - Phonon vertex coefficients: c†_{k+Q↑}c_{k↑} → u′v, and c†_{−k↓}c_{−k−Q↓} → +uv′ (sign checked). With g(−k−Q,Q) = g(k,Q) the sum is case I. Each (↑p, ↓r) final state is labelled once by (k, Q) = (−r, p+r), so there is no double counting. CHECKED.

A6. Case-I coherence factor and recovery of Allen and HLZ — CHECKED.
 - ∫dξdξ′ ½(1+Δ²/EE′)δ(x−E−E′) = 2x𝔤_I: the normal-state limit is 2x (two spin orientations). The conductivity prefactor collapses to (ω_p²/ω²)(2π/ω)∫α²F_tr(ω−ω′)𝔤_I.
 - For a spherical Fermi surface, eq:15.4-a2Ftr is eq:6.4-a2F weighted by 1 − cosθ ([ê·Δv]² → 2v²(1−cosθ)/3 over 2v²/3). The normal limit is Allen's 1/τ(ω) = (2π/ω)∫(ω−Ω)α²F_tr (the standard form; Allen 1971 itself not read).
 - Debye law, sympy: λ_tr = 2∫α²F/ω′ holds, and γ_H = (2π/15)λω⁵/ω_D⁴ (ω < ω_D) and (4π/5)λω_D(1 − 5ω_D/6ω) (ω ≥ ω_D) are exactly HLZ Eq. (16) (read).
 - Closed forms of D.40 (𝔤_I, 𝔤_II): the derivation steps are redone, and both forms agree with direct quadrature to ≤ 4e-16 at y = 2.2, 3, 4, 10. New check: 𝔤_I(y) = E(√(1−4/y²)) to 1e-15 at y = 2.0001–100, which is exactly the kernel of HLZ Eq. (17) (read: "E(1 − 4Δ²/(ω−Ω)²)^{1/2}"). The Landen statement of D.40 is CHECKED.
 - 𝔤_I(4) = 1.2111 and 𝔤_II(4) = 0.6719; 𝔤_II reaches 0.9 at y = 8.129 ("8.1"). CHECKED.
 - Interband threshold "≈ 0.5 eV" (HLZ p.4) CHECKED. λ_tr 0.39 (from resistivity with the computed ω_p) and 0.37 (computed), and ω_p = 12.29 eV: Savrasov Table IV and its caption, CHECKED. ω_D = 0.037 eV (HLZ) CHECKED. HLZ themselves use ω_p = 12.2 eV and Δ ≃ 0.3 meV.

A7. Impurity-assisted absorption (MB keyresult) — CHECKED.
 - σ_dc = ω_p²/γ = 9459.6 eV (with 15.78 eV), 0.786 μΩ cm; σ₁^MB(1 meV) = 7649 eV, 1.38e6× σ₁^S ("1.4e6"). "146 gaps" = 26.32/0.18. CHECKED.
 - Inconsistency (known editor item, root cause identified): 15.3 builds the same film with ω_p = 15.70 eV (0.794 μΩ cm) and 15.4 with 15.78 eV (0.786 μΩ cm). See C1.

A8. Limit Check 15.4a and the numbers around it — CHECKED. All recomputed with my own integrator:
 - σ_S/σ_N = 0.4209 at 1 meV (ω′⁴ law) and 0.7330 (ω′² law).
 - 90 % at 11.390Δ = 2.050 meV; ω′² law 7.381Δ.
 - Crossing of 1 at 16.17Δ; maximum 1.0466 at 31.0Δ.
 - Case II reaches 90 % at 53.70Δ.
 - Near-edge δ⁵ form low by 0.21 %, 0.83 % and 2.06 % at y = 2.05, 2.2, 2.5. The text's "within 0.2 and 2.1 %" CHECKED; σ₁^S(2.2Δ) = 4.386e-8 eV and σ₁^N = 8.18e-4 eV CHECKED.
 - "Factor 2.4 at 1 meV" = 1/0.421. CHECKED.
 - WE 15.4: γ_H = 8.717e-11 eV, σ^N = 0.01317 eV, σ^S = 5.541e-3 eV, ε₁ = −1.510e8, 1/|ε|² = 4.383e-17, L = 2.429e-16. Rate 1.294e18 ζ² /kg/yr from eq:10.7-dp (ρ_χ/ρ_T)ζ²L·c²/ħ, giving ζ₃ = 1.52e-9; normal metal 3.07e18 and 9.88e-10. All CHECKED.
 - Momenta: 0.64 meV/c_L = 30.5 eV and /c_T = 59.4 eV, k_F/59.4 = 58. CHECKED for the stated C₁₁, C₄₄, but see C3 (superseded elastic constants).
 - GAP (ladder size, l.71): (Δ/v_FQ)² grows as Q → 0, so the value at the most energetic phonon (2.5e-4 at y = 2.2) is the minimum, not the size. Weighting by α²F ∝ ω′⁴ gives (5/3)×2.5e-4 = 4e-4 at y = 2.2 (1.3e-6 at 1 meV). Correction: "4×10⁻⁴ averaged over the ω′⁴ weight (2.5×10⁻⁴ for the most energetic phonon)".
 - Fig. 15.3a ratios 1.62 (0.1 eV) and 1.32 (0.3 eV) agree with the log. The impurity curve was not recomputed beyond these points.

A9. Summary nuisance table against the sections — mostly CHECKED. Discrepancies:
 - Row "Pair-field ladder dropped": "bare loss function down to 0.53 of the conserving one" holds only for y ≥ 3 (s15-1 l.136 "for y ≥ 3": 0.565/1.072 = 0.527). At y = 2.2 on the edge it is 0.323/0.868 = 0.37 (0.30 at y = 2.02, limit15_1a.log). GAP: add "for y ≥ 3; 0.37 at y = 2.2".
 - Row "Gap of the sensor": ×1.23 light CHECKED (we15_1.log 1.232, s15-1 l.169). ×1.13 heavy matches the log (1.128) but is printed in no section. GAP: add it to s15-1 l.169 or drop it from the table.
 - Row "Collisions": 0.63/10 → 0.64/9.8 (A2).
 - Row "Sheet": add "leading order in qd" (A1).
 - Row "Relaxation rate" CHECKED: 4.6 = 0.868/0.187; spread at y ≥ 3 = 1.068/1.008 → 5.95 % "below 6 %".
 - Row "Thermal": e^{−208} needs Δ = 1.764 T_c = 0.1794 meV (208.2). With Δ = 0.18 meV exactly it is e^{−208.9}. Consistent with 7.2; CHECKED.
 - Row "Energy dependence of the gap": 3.540 against 3.528. CHECKED.
 - Rows "α²F_tr shape", "×0.52", "1.4e6", "WSi k_Fl 1.8–5.5", "edge remainder" CHECKED.
 - Inputs table: mixes the mass conventions (v_F = 6.67e-3 implies m* = 1.0132; k_TF = 4.05 keV and ω_p = 15.78 eV use m_e; WE 15.3 uses 4.08 keV and 15.70 eV). See C1.
 - Inputs table: the clean criterion "𝔩_e ≫ v_F/Δ = 7.3 μm" against 15.3's ξ_coh = v_F/πΔ = 2.33 μm. Pick one; 15.3 defines clean as 𝔩_e ≫ ξ_coh.
 - Inputs table: c_LA = 6.29 km/s. See C3.
 - Summary prose: all numbers CHECKED (𝔤_I 1.500/1.322/1.151/1.051; 0.749; 17 %; 8.2; 8 %; 24; 0.235; 540; 11.4Δ; 0.42; 1.5e-9; 1.4e6; 87 %; 5.1e-13/5.6e-9; 11.5 meV). The paragraph-3 sheet sentence needs the same "leading order" qualifier.

A10. Spin-current pair breaking (reviewed separately; only what I noticed).
 - The numbers redo exactly: σ^J(1 meV) = 3.296e4 eV; σ^J(0.72 meV) = 9.513e4 eV; ∫σ^J = (π/2)ω_p² (sympy); fractions 0.866 and 0.995; crossing with σ₁^N at 11.52 meV.
 - ALP at 0.72 meV, from eq:10.7-alp (identical to HLZ Eq. (22), read): rate 1.143e25 g², so g₃ = 5.12e-13 and 0.114 events at 1e-13. The phonon-only route gives σ₁^S = 7.86e-4 eV, 9.44e16 g² and g₃ = 5.64e-9.
 - New exact identity: ∫₂^∞(𝔤_I(y) − 1)dy = 2 (to 1e-11). The dirty-film spin weight above 2Δ therefore exactly replaces the normal weight in (0, 2Δ). The "0.05 %" (I get 0.9995) comes from the Drude curvature and the 50 eV cutoff, not from the coherence factor. Suggest stating the identity.
 - Algebraic origin, for the separate check: in the reduced BCS Hamiltonian [𝒥^{zz}, b†_k b_k′] = (v_k − v_k′) b†_k b_k′ ≠ 0, while the charge current commutes. The effect is therefore the non-conservation of P↑ − P↓ by the ↑↓ pairing interaction (the same physics as spin drag). This supports the text's Fermi-liquid caveat. I did not check the ALP NR operator, spin–orbit coupling or the literature.

## B. Line-by-line, other items

s15-3
 - l.3: "QROCODILE nanowires": the SM describes "microwires" of width 1 μm (the device class is SNSPD). Minor GAP; say "wires".
 - l.12: ⟨s²⟩ = 2𝔩_e² and ⟨r²⟩ = 2𝔩_e²γt = 6Dt. CHECKED.
 - l.17, Tab. 15.3 (Al): ξ = 2327 nm; 𝔩/ξ = 0.0215; k_F𝔩 = 875; edge q = 0.1358 eV with q𝔩 = 0.0344; q𝔩 = 253 at 1 keV. CHECKED.
 - l.39: thin-film 2Δ = 0.6 meV is consistent with the 0.30 meV film convention. Anderson attribution: credit only (not read).
 - l.43–49: bracket derivative 2 − 2νℓ (sympy); large-ν series −x²/3 − x⁴/5. The sign of R⁰ = −2𝒩_F𝔣_L is consistent with k_TF² = 2e²𝒩_F. The Mermin combination (sympy) is CHECKED.
 - l.56: bound on |ν_γ| CHECKED.
 - l.63: Drude limit k_TF²D = ω_p²/γ CHECKED.
 - l.65: on the retarded branch ℓ(ν) ≃ −iπ + 2ν (principal log with Im ν > 0) CHECKED.
 - l.88: "24 times … 22 … 0.40 … 3.9 eV … 0.75 keV" CHECKED.
 - l.96: σ₂ carries (π²/2)Δσ_n (A4) CHECKED.
 - l.108: ω_p/√2 = 11.1 eV CHECKED.
 - l.113 and WE: 1/q = 581 nm; qd = 1 at 3.947 eV CHECKED.
 - l.122: D q² = 0.361Δ; L_s(y=5) = 1.2587 × 9.636e-8 = 1.213e-7; the 30 nm column gives 1.091 × 1.1507 = 1.255 ("1.26"); spread 1.216–1.259, 3.5 %. CHECKED.
 - l.131: oddness of Im R from reality plus R(−q) = R(q) CHECKED.
 - l.133: "seven orders of magnitude" (2101.08263 SM, read) CHECKED; Fig. S4 damped GSRF negative at small ω CHECKED.
 - l.135: ω_AB clash with NOTATION (known editor item). The y ≈ 2.3 statement belongs to 15.1/15.2 and was not verified here.
 - l.139, WSi (Zhang Table I, read): R_s 326–417 Ω → ρ = 163–208.5 μΩ cm ("209" rounds half up; fine); ratio to the Al film 205–263; D 0.70–0.75; ξ 7.0–7.4; T_c 3.83–4.08. CHECKED.
 - l.139, GAP: 2𝒩_F = (2.6–4.1)e47 are Zhang's tabulated N₀. The book's stated Einstein relation with ρ = R_s d reproduces the x = 0.75 and 0.80 rows to 3 %, but not the x = 0.85 rows (4.1 → 3.27e47, 3.8 → 2.97e47; 25 % inconsistency inside the source). Either write "Zhang et al. tabulate" or quote the recomputed (2.7–3.3)e47, which changes "2.3–3.6 times" to 2.4–2.9 times.
 - l.139: T_c 1.73 K, W₄₅Si₅₅ and 2 nm (QROCODILE) CHECKED.
 - l.139, GAP: Gan et al. use Δ = 0.26 meV and E_F = 7.0 eV for WSi. 0.263 meV is the book's 1.764 T_c, not Gan's number; reword.
 - l.141–143: k_F = 2674.7 eV; v_F = 5.234e-3; 2𝒩_F = 1.125e47; 𝔩 = 0.134/0.143 nm; k_F𝔩 = 1.81/1.94; ω_p = 10.77 eV; γ = 2.54/3.25 eV; 𝔩 = 0.406/0.318 nm; k_F𝔩 = 5.51/4.30; 2π/k_F = 0.464 nm; 3.6–11×; q/k_F 0.37–1.87; q𝔩 0.68–3.39; edge q = 0.198 eV; L = 1.153e-5 and 1.475e-5. All CHECKED.
 - l.145: the interaction–disorder sentence (Altshuler–Aronov/Finkel'stein physics) has no citation. GAP (known editor item).

s15-4
 - l.3: m v = 1 μeV; ω/v_F = 0.150 eV, 1.5e5×. CHECKED.
 - l.3, GAP (completeness, my estimate, not in the text): "that conductivity comes from these two processes" omits electron–electron (Gurzhi umklapp) absorption, 1/τ_ee(ω) ∝ ω² + (2πT)². With A ≈ 3×10⁻⁶ μΩ cm K⁻² for Al [from memory, UNVERIFIED], γ_ee(1 meV) ≈ 2×10⁻⁷ eV against γ_H = 8.7×10⁻¹¹ eV. In the superconductor this channel needs ≥ 4Δ. If the coefficient holds, it dominates the "intrinsic" σ₁ near 1 meV. Size it or name it as an open nuisance row.
 - l.13–18: eq:15.4-wp is consistent with ω_p² = e²n/m for free electrons (2e²𝒩_F v_F²/3 = e²k_F³/3π²m). 15.78 eV CHECKED.
 - l.32: "No ladder corrects eq:15.4-MB" (odd × even bubbles vanish for s-wave) CHECKED.
 - l.59: the λ_tr definition is consistent with eq:6.4-lambda. CHECKED.
 - l.73: fourth power = ω′² (Debye α²F) × Q² (1 − cosθ). CHECKED.
 - l.86: "1.6 at 0.1 eV, 1.3 at 0.3 eV" CHECKED; σ₁^N ∝ ω³ below ω_D and ω⁻² above. CHECKED.
 - l.104: L = σ₁ω³/ω_p⁴ follows from σ₂ = ω_p²/ω. CHECKED.
 - l.126: "6e6 times" = 5.95e6 CHECKED.
 - l.130, GAP (minor): the text names "the mass enhancement 1+λ_ep", then uses 1/(1+λ_tr) = 0.719 (square 0.518). With λ_ep = 0.44 it would be 0.48. The optical mass is 1+λ_tr in Allen's theory, so 0.52 is defensible, but say which mass is meant.
 - l.132: λ_tr 0.319 and λ_ep 0.436 for the model; ×1.25e4 below 1 meV (a2ftr15.log; not recomputed). Consistent.
 - Dimensional analysis: eqs 15.4-wp, -MB, -T (T dimensionless, σ₁ = (πe²/ωV)Σ|T|²δ has units of eV), -a2Ftr (dimensionless), -holstein (eV), -sJdef and -sJ (eV) all CHECKED.

D.40
 - l.31: δ(ω−2E) with weight E/2|ξ| at each root; Σ_k → V𝒩_F∫dξ (one pair state per k). This gives eq:D.40-sJ, and the cosh integral gives (π/2)ω_p² tanh t. CHECKED.
 - l.62–72: prefactor chain to eq:15.4-holstein CHECKED (A6).
 - l.89: the "10⁻⁷" quadrature agreement is conservative (I get 1e-16). CHECKED.

ch15.tex opening
 - m_min = 2(0.36 meV)/v_max² = 102.5 eV ("0.10 keV").
 - The Si gap over 2Δ is 3.1–3.2e3 ("three thousand").
 - m_min(Si) = 0.32–0.33 MeV ("a third").
 - "Up to a factor of three" (0.323 against 0.868–1) CHECKED.

## C. Convention and notation drift (against NOTATION and state/)

C1. Al electron gas (known editor items; root cause). v_F = 6.67e-3 with k_F = 1.75 Å⁻¹ implies m* = 1.0132 (the editor note says 1.012). This splits the book into an m* branch (15.3: k_TF 4.08 keV, ω_p 15.70 eV, 0.794 μΩ cm) and an m_e branch (15.1 WE, the inputs table and 15.4: k_TF 4.05 keV, ω_p 15.78 eV, 0.786 μΩ cm). 6.4's E_F = 11.7 eV gives 6.77e-3, and Gan uses 6.75e-3. Pick one mass and recompute: the 15.3 WE numbers move by ≤ 1 % (L ∝ 1/ω_p²).
C2. NOTATION gaps. Symbols used in 15.3/15.4/D.40 with no NOTATION row: D_diff, ξ_coh, ρ_el, d_film, ε_sh, ε_a, ε_b, 𝔣_L, ν_γ, ω_p^intra, σ₁^𝒥, γ_H, α²F_tr, λ_tr, 𝔤_II, σ_n, σ_dc, L_s, L_n, N^El, P^El, J_i, J_f, V^e_αβ. Clashes: ν (reduced frequency) is NOTATION-local to 4.5/D.8 and is used here too (known item); y = ω/Δ has a NOTATION row (15.2), which is fine.
C3. Sound speeds and naming. 15.4 writes c_L, c_T; NOTATION renamed c_L → c_LA (clash 72), with c_TA/c_T. The values come from room-temperature Kittel constants (C₁₁ 106.8, C₄₄ 28.2 GPa). state/CORRECTIONS.md §19.13(g) says state/DATA-ADDENDA.csv supersedes the v4 Al sound-speed rows with the 0 K Kamm–Alers values C₁₁ 114.3, C₄₄ 31.6 GPa, which give c[100] = 6.51 and 3.42 km/s. With them, s15-4 l.38 becomes 29.5 or 56.1 eV and "61 times", and the inputs-table c_LA becomes 6.51 (not 6.29). This is a superseded-value use, but the conclusions are unaffected.
C4. Factors of 2, π and signs. Spin counting (2𝒩_F, the "2x" pair spectrum), f-sum (π/2)ω_p², σ₁ = πe²/(ωV)Σ|T|², and the HL e² = 4πα in k_TF² = 4αmk_F/π are all consistent. The only π-drift found is the clean criterion v_F/Δ against v_F/πΔ (A9).
C5. SOTA.md l.674 already records the spin-current result as "verified" and "~10⁴ in g_aee" (5.6e-9/5.1e-13 = 1.1e4), which is consistent. The editor note says no downstream use until the separate check; SOTA's "verified" should wait for spincurrent-check.md.
C6. DC-RESULTS/R18: DC-41 is the only item bearing on these files. Its table values are used correctly with the ℓ scope; the v_F = 6.8e-3 conversion is noted in A4. No other DC item touches 15.3/15.4/D.40.

## D. Part II editor notes
No item in ledgers/REVIEWS/partII/editor-notes.md concerns 15.3, 15.4, the summary or D.40. The two Ch15 items there (7.2 density-jump corrections; the E.26 axioelectric pointer) belong to 15.1/15.2 and App. E.

## Summary of corrections (WRONG/GAP to act on)
1. Sheet: cite Lasenby–Prabhu 2110.01587 Eq. (19); 540 is leading order (exact slab 588, +qd), in 15.3, WE and summary.
2. QROCODILE anisotropy paraphrase (very large at 1 nm⁻¹, significant already at 1 keV).
3. Mermin/Drude thresholds 0.64 and 9.8 (s15-3 l.79 and table row).
4. Table row "down to 0.53" needs "for y ≥ 3" (0.37 at y = 2.2); ×1.13 heavy is unsourced in the sections.
5. Ladder correction size 4e-4 (weighted), not 2.5e-4.
6. WSi DOS: Zhang's x = 0.85 N₀ inconsistent with the Einstein relation (recomputed 2.7–3.3e47, 2.4–2.9×); Gan's gap is 0.26 meV.
7. Al mass convention (C1); superseded sound speeds (C3); NOTATION rows (C2); clean criterion v_F/Δ against v_F/πΔ.
8. Name or size e–e (Gurzhi) absorption as a third intrinsic channel (estimate unverified).
9. State the D q² = 0.04Δ number and REF-DC-41's "not proved" at s15-3 l.104.
