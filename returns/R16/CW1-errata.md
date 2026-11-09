# R16 / ERR-CW1: errata to returns/R16/CW1.md (applies referees/R16/VER-CW1.md)

Brief: campaign/paer/briefs/R16/ERR-CW1.md. Read: returns/R16/CW1.md, referees/R16/VER-CW1.md, CONVENTIONS.md, NOTATION.md (collision check for ς, ε_touch, ∂_{q_z}ρ|_rel, β^{ZP}_2: none occurs; only β_2p (C4 Slater exponent) is near),
returns/R8/WP1-v3.md (§2.3 l.452–461, IF-14, D3), returns/R8/WP3-v3.md §M3(c) (l.115), returns/R15/COMP-PH.md (sound speeds, l.32/64), code/CW1/ (all scripts, inputs, out/*.json).
**Literature:** none new. Every source used here is already [FT] in CW1 or VER-CW1 (2011.12765, 1608.01994); the 2011.12765 numbers in E-13 were re-read in the kept HTML (literature/papers-CW1/2011.12765.html). The Luttinger parameters in E-4 are [E, memory] and marked as such. literature/papers-ERR-CW1/ is not created.
**New [CALC] (regenerated; the CW1 work dirs were gone).** QE 7.6 pw.x, single core, outside the heavy lock, ≈ 2.5 min in total (code/CW1/scripts/run_errata_qe.sh; inputs code/CW1/inputs/errata/; work dir /root/work/CW1).
Si, a_exp = 10.2631 bohr, 40 Ry, SCF 8³. Three variants: **S12** = SG15 Si_ONCV_PBE-1.2 (the CW1 scalar pseudo); **FRav** = Si_ONCV_PBE_FR-1.1 with lspinorb = .false. (j-averaged, the same pseudo family as SOC); **SOC** = FR-1.1, noncollinear + lspinorb.
Each nscf runs on 60 k: Γ, k_c, the on-axis 1.39 keV pair, 3×3×3 stencils (h = 0.02·2π/a) around the hole and the electron of the CW1 mirror-plane optimum, and the q* = 0.90 keV pair.
A second nscf (S12, SOC) is re-centred at the first-step optimum. Analysis: scripts/errata_kset.py, errata_kset2.py, errata_analysis.py → out/errata_qe.json, errata_qe_it2_{S12,SOC}.json.
Ratios: scripts/errata_ratio.py → out/errata_ratio.json, using the committed Wannier TB and the same [E8]/(P.1) models as ratio.py.
**Regeneration control:** S12 reproduces the CW1 pass-5 numbers. Pair energy 0.742228 vs 0.742228 eV, gap 0.556735 vs 0.556732 eV. The mirror-plane top-hole vertex is 2×10⁻¹³ (CW1 2×10⁻¹⁴), the second band 0.06497 vs 0.06496, |∂_{q_z}ρ| = 1.368 vs 1.372 Å. The SOC mirror lift is 1.285×10⁻⁴ vs 1.285×10⁻⁴.
**Checks:** code/CW1/checks.py revised, **52/52 PASS in ≈ 8 s** (one core; no QE calls). CW1.md is not edited: read it together with this file. Nothing committed.
**Merger rule.** For every owed correction, interface flag, LIMITS row and closure-table row listed in §2, use the text given here. Where §2 says "unchanged", use CW1.md.
Amended equations carry a prime: (CW1.4′), (CW1.4b), (CW1.5′). New symbols are listed at the end of §2.

---
## 1. Corrections, one block per verifier row that is not plain STANDS

### E-1. V2, V3, OC-1/2/4/8/9, CW1-L1, VER §0 (Si zero-phonon edge with SOC, re-minimised): STANDS WITH CORRECTION, applied and computed
The verifier's SOC shift is reproduced, and it is pseudo-consistent (CW1-C33). The SOC run is scissored to 1.170 eV against its own Γ₈ gap.
At the CW1 mirror-plane point the SOC pair energy is higher by **+15.52 meV** than FRav (same pseudo family) and +15.65 meV than S12. On the axis (1.39 keV pair) the shift is +0.7/+0.9 meV.
Reason: the off-axis hole sits 61.6 meV below the VBM, beyond Δ_SO = 48.6 meV. It does not share the Δ_SO/3 rise of Γ₈. With SOC it is 77.1 meV below Γ₈ (CW1-C52).
**Re-minimisation on DFT bands (new; the verifier marked it owed).** (CW1.1) is a minimum over (k_e, k_h), with q = k_e − k_h unfolded.
Each band is fitted by a full quadratic (10 parameters, rms 0.25 meV hole / 0.08 meV electron) on its 3³ stencil. m is minimised in 6-D; the stencil is re-centred and the step repeated.
The second step moves the point by ≤ 6×10⁻⁴·2π/a and changes m by < 10⁻⁴ MeV (CW1-C34):
| evaluation (a_exp, DFT, scissor 1.170 eV) | at the CW1 point | re-minimised | |q| (keV) |
|---|---|---|---|
| scalar (PBE-1.2) | 0.4048 | **0.4042** | 1.320 |
| SOC (FR-1.1) | 0.4078 | **0.4072** | 1.327 |
| on-axis local optimum (Wannier, a_PBE; SOC on the axis +0.0002) | 0.4150 | — | 1.39 |
The off-axis optimum still wins with SOC (0.4072 < 0.4152), so V1 stands. The SOC shift of the edge is **+0.0030 MeV**.
**Corrected statement (replaces the §1.2 "So m_χ^{ZP} = 0.400–0.405 MeV …" sentence and the 1s onset):**
"m_χ^{ZP} = **0.405–0.408 MeV** (continuum). The best value is **0.407 MeV** [CALC: PBE+SOC, a_exp, DFT re-minimised locally, rigid scissor to E_g(0) = 1.170 eV].
The band carries a_PBE ↔ a_exp (−0.003) and the unminimised SOC point (+0.0006). The 1s line lowers the onset by 0.0028 MeV (2p 0.0007): bound-line onset **0.402–0.405 MeV** (best 0.404) (CW1-C7).
The global minimum is established on the Wannier TB (scalar, a_PBE; 30 random starts by VER-CW1). The DFT and SOC corrections are local (second order in the displacement)."
Reconciliation (replaces the §1.2 reconciliation sentence): "COMP-PH's 0.4154 is the on-axis local optimum, an upper bound (CW1-C5). COMP-PAER's 0.405–0.408 at a_exp is **kept**.
Its lower end equals the scalar a_exp value here (0.4042–0.4048), and the SOC value 0.4072 lies inside it. CW1 does not replace it; it explains why it lies below the on-axis 0.415."
The table row "DFT at the same fractional point, a_exp | 0.4046" is supplemented by the two re-minimised rows above.
§1.2 "the electron sits … 0.17·2π/a short of k_c": the 0.17 is relative to the Wannier k_c = 0.855. Relative to the DFT a_exp k_c = 0.843 it is **0.155·2π/a** (VER §5).

### E-2. V32, IF-CW1-3 (E_min at q* = 0.90 keV): STANDS WITH CORRECTION, applied
Regenerated at the same fractional point (CW1-C50): the Wannier a_PBE value is 1.6975 eV; DFT a_exp gives 1.7112 eV (scalar) and **1.7274 eV** (SOC; shift +15.9 meV vs FRav, +16.2 vs S12).
The point is not re-minimised. At the main optimum the local k re-minimisation at fixed q is ≈ −1 meV, so E_min^{ZPL}(0.90 keV) ≈ 1.727 eV (a_exp, PBE+SOC), ≤ 1.727 eV.
Re-issued IF-CW1-3 text in §2.

### E-3. V4, OC-5 (M_x and WP3's 1.41 m_e): STANDS WITH CORRECTION, applied
WP3-v3 l.115 gives "m_l + m_hh ≈ 1.41 m_e … both [UNVERIFIED]" and does not say how 1.41 was obtained. CW1's "1.41 m_e used a DOS heavy-hole mass" is an inference and is withdrawn.
M_x = 1.19 m_e is recomputed from the raw QE eigenvalues, independently of masses.py (CW1-C1): m_l 0.923 (quartic fit 0.951, i.e. 3% nonparabolicity), m_hh[100] 0.264, M_x = 1.187 m_e.
These are PBE masses without SOC. §1.3 sentence replaced: "WP3-v3's 1.41 m_e (source not stated in WP3) is withdrawn; along [100] the pair translational mass is m_l + m_hh[100] = 1.19 m_e [CALC, PBE, no SOC]."

### E-4. V5, LE-24 Ge (§1.4): FALLS (the anisotropy sentence), replaced
Delete "and the Si lesson (a warped heavy hole moves the optimum off axis and lowers m by ≈ 4%) applies to Ge as well, whose Γ₈ heavy hole is more anisotropic".
Replacement: "The parabolic interim 0.32 (0.32–0.36) MeV [E] is not a bracket in either direction. It assumes a parabolic pair with the hole at Γ, and only the on-axis value of (CW1.1) is a strict upper bound on the joint minimum.
The Ge heavy hole is **less** warped than Si's: (γ₃ − γ₂)/γ₁ = 0.11 vs 0.26, and m_hh[111]/m_hh[100] = 2.45 vs 2.60 [E, Luttinger parameters from memory] (CW1-C46). The Ge valley axis [111] is already its heavy-hole direction.
Whether the Ge optimum leaves the L axis is therefore not predicted, and no ≈ 4% lowering is transferred.
What does transfer from Si: SOC must be in the bands (in Si it raises the edge by +0.003 MeV, E-1), and the hole must be free in (CW1.1)."
Spec unchanged otherwise (CW1 §1.4: HSE06 + SOC, Wannier 16 spinor WFs, emin_fast.py with nv = 8). Add one convergence line: "the DFT re-minimisation of E-1 (two Newton steps on 3³ stencils, h = 0.02·2π/a) at the Wannier optimum; pass: last step changes m by < 10⁻⁴ MeV."

### E-5. V8, CW1-L3, OC-2 (|ρ|² at the X face; ZPL/PAER at the opening): STANDS WITH CORRECTION, applied (scope in Rebuttal R-5)
At the computed (2̄00)-class edge point, the electron k = (−1, 0.028, 0.023)·2π/a lies on the X face but not on the X–W line. There c₂ is **50 meV** above c₁ (CW1-C41).
At ε_ex < 50 meV only c₁ is reached, and its vertex is 0.0095. The vertex varies quickly near the X–W degeneracy: c₁ gives 0.024 at 0.02·2π/a inside the class.
The c₁ + c₂ sum (0.028) is the relevant vertex once c₂ is open, or near the X–W line where the pair is degenerate.
Corrected §2.3 numbers: ZPL/PAER at the opening (m_χ ≈ 0.50 MeV) is **2.4 (c₁) to 7.0 (c₁ + c₂)** at ε_ex = 1 meV, and 1.6–4.8 at 0.1 eV; 10–11 at 0.05·2π/a inside the class (both bands) (CW1-C41).
OC-2's "|ρ|² ≈ 0.01–0.04" becomes "0.01–0.04 (c₁; 0.028 for c₁ + c₂ at the face point)". The decision of §2.3 stands: comparable at ≈ 0.50 MeV, ZPL leading by ≥ 10 from ≈ 0.51 MeV; the 0.62 MeV fallback stays withdrawn.
SOC on this edge [CALC, regenerated: inputs/errata/nscf_xface_*.in → out/errata_xface_soc.json]: at the same point (a_exp, not re-minimised) the SOC pair is +16.0 meV above FRav. m goes 0.5003 → 0.5027 MeV (+0.0024), and c₂ − c₁ = 51.7 meV with SOC too (CW1-C41).
The opening stays at ≈ 0.50 MeV.

### E-6. V9 (§2.3 "leads robustly"): STANDS as [E], wording applied
"leads robustly from ≈ 0.51 MeV" → "leads from ≈ 0.51 MeV by ≥ 10 pointwise, which is just outside the ×/÷10 band of the PAER side; the statement is [E] with a [CALC] vertex".

### E-7. V10, V11, VER §2 on (CW1.4), CW1-L4, OC-3 (angle-averaged ϖ̄_II and the crossover in m_χ): STANDS WITH CORRECTION, applied, with a quantitative change
Four corrections, all computed (scripts/errata_ratio.py, CW1-C36–C40).
(a) **Cone overlap.** Around one valley axis the four minima lie on a circle of radius ϑ_ZP. Adjacent ellipses touch, on the 45° line, at
  ε_touch = ϑ_ZP²β_θβ_z/(β_θ + β_z) = **0.049 eV** (sympy, CW1-C36),
which is earlier than the axis-crossing energy β_θϑ_ZP² = 0.081 eV quoted in CW1 and by VER (Rebuttal R-3). Above ε_touch, (CW1.4) double counts. It is replaced by
  S̄_II(ε) = 6∫d²θ [|∂_{q_z}ρ|_rel|²|q|²φ_{c*}² + |∂_{k_z}ρ|²(2μ_x(ε − E_{c*})/3)(1 + ζ_S²)] J(ε − E_{c*})𝒮_F(ε − E_{c*}),   c*(θ) = argmin_c E_c(θ),        (CW1.4′)
i.e. each direction is assigned to its lowest cone ("min-of-cones"), E_c = E₀ + β_θθ_c² + β_zφ_c² in each cone's local axes, and the 2-D integral is done on a grid.
(CW1.4′) equals (CW1.4) for ε ≤ ε_touch (to 3×10⁻³). The model energy at the midpoint between two cones, 50.6 meV, agrees with the Wannier E_min there, 51.3 meV (CW1-C37).
(b) **Relaxed-pair q coefficient.** Along the out-of-plane tilt the pair relaxes by centre of mass, k_e* = q m_e/(m_e + m_h) (sympy, CW1-C38). The q coefficient is then
∂_{q_z}ρ|_rel = α m_e/(m_e+m_h) − β m_h/(m_e+m_h), with α the electron-leg and β the hole-leg gradient. Both come from the regenerated stencil as gauge-invariant |ρ|² of the four (±e_z, ±h_z) combinations.
Values: m_zz^h = 0.323, m_zz^e = 0.190, |α| = 1.368 Å, |β| = 1.689 Å, cos∠(α, β*) = −0.994 → **|∂_{q_z}ρ|_rel| = 1.568 Å** (1.540 at the re-minimised point). Hence |ρ|² is ×1.31 relative to the 1.372 Å used, inside VER's band 0.67–1.40.
(c) **Second (mirror-even) heavy hole, omitted in CW1.** On the axis the Δ₅ pair is degenerate. Under a tilt the top band falls (mirror-odd, vertex 0 in the plane), and the second band rises (mirror-even, allowed, linear in the tilt).
Its edge is 0.4150 MeV on axis (Wannier, a_PBE; VER 0.415008), or ≈ 0.4197 with the a_exp/DFT shift found for the first channel (+0.0045, [E] transfer) plus its own SOC shift (+0.0002).
Its pair energy is quadratic in the tilt, E₂ = E₂^{ax} + β^{ZP}_2(α)θ², with **β^{ZP}_2 = 4.51, 2.12, 1.07 eV/rad²** at azimuth α = 0, π/8, π/4 (θ = 0.02 and 0.04 agree to 2%).
Its vertex is the on-axis Δ₅-pair sum g_⊥ = 2.21 Å (out/vertex_offaxis40.json). Assigning all of it to band 2 gives an **upper estimate** of its ZPL:
  S̄₂(ε) = 6[π⟨(β^{ZP}_2)⁻²⟩_α g_⊥²|q|²∫₀^ε u J(ε − u)𝒮_F du + (π/β̄^{ZP}_2)∫₀^ε |∂_kρ|²(2μ_x(ε − u)/3)J𝒮_F(1 + ζ_S²)du],   ⟨·⟩_α = (1/2π)∫dα.                    (CW1.4b)
Validity: the vertex is linear only to θ ≈ 0.07 rad (checked to q_⊥ = 0.046 Å⁻¹); at ε = 0.1 eV the {011}-azimuth cone reaches θ ≈ 0.3 rad, so (CW1.4b) is an extrapolation there [E].
(d) **Edges with SOC** (E-1): E₀ = 1.3546 eV at |q| = 1.327 keV (a_exp, SOC, re-minimised).
**Corrected §3.2 table** (replaces the ϖ̄_II row; the other rows are unchanged and pointwise):
| ε_ex | 1 meV | 14.7 meV | 50 meV | 0.1 eV | 0.2 eV |
|---|---|---|---|---|---|
| ϖ̄_II, (CW1.4) as in CW1, recomputed at the SOC edge (overcount above 0.049 eV) | 1×10⁻⁴ | 0.016 | 0.13 | 0.35 | 0.85 |
| **ϖ̄_II, (CW1.4′), relaxed-pair vertex, SOC edge** | 1×10⁻⁴ | **0.020** | **0.16** | **0.34** | **0.58** |
| angle-averaged SOC piece (lift 1.285×10⁻⁴) | 2×10⁻⁴ | 0.002 | 0.006 | 0.008 | 0.010 |
**Corrected §3.3 (in m_χ).** At fixed m_χ each channel is evaluated at its largest reachable excess energy (pointwise at ε_ex^{max}, an upper estimate of the integrated ratio, as in CW1).
Criteria, as in CW1: "central" = total ZPL/PAER = 1; "at least" = total = 1/3, i.e. ZPL = PAER with the PAER side at 𝔉_ρ/3 (the low end of its band). Interpolating the table:
central ≈ 0.428 (central edge) / 0.424 (low edge) MeV; "at least" ≈ 0.421 / 0.418 MeV.
| m_χ (MeV) | ε₁^{max} (eV) | ϖ̄_II (first hole) | ϖ̄₂ (second hole; edge 0.4197 / 0.4150) | SOC | total (central / low edge) |
|---|---|---|---|---|---|
| 0.41 | 0.015 | 0.021 | 0 / 0 | 0.002 | 0.023 |
| 0.42 | 0.066 | 0.23 | 0.001 / 0.32 | 0.007 | **0.24 / 0.56** |
| 0.43 | 0.115 | 0.38 | 0.80 / 1.74 | 0.008 | **1.19 / 2.14** |
| 0.44 | 0.161 | 0.50 | 2.13 / 3.34 | 0.009 | 2.64 / 3.85 |
Replaces "PAER leads the integrated electronic rate at least to ≈ 0.42 MeV, centrally to ≈ 0.44 MeV; 0.44–0.51 MeV is a two-channel region" with:
"**PAER leads the integrated electronic rate at least to ≈ 0.42 MeV (0.418–0.421) and centrally to ≈ 0.43 MeV (0.424–0.428)**; 0.43–0.51 MeV is a two-channel region. The second (mirror-even) heavy hole, open from 0.415–0.420 MeV, dominates the zero-phonon side above 0.43 MeV.
The allowed-size ZPL opens at ≈ 0.50 (comparable) and leads from ≈ 0.51 MeV. All of this is [E]: vertices [CALC], PAER ×/÷10, the second-hole term an upper estimate."
Remaining biases, now stated: the isotropic μ_x underestimates J (×1.3–1.6, CW1 §3.1); 𝔉_ρ is more plausibly low (ratios more plausibly high); ε_ex^{max} at the optimum |q| slightly underestimates the reachable excess (CW1-C51, < 2 meV at 0.42 MeV); the second-hole vertex is assigned entirely to band 2 (upper estimate).

### E-8. VER §2 (mirror rule convention), CW1-L2: STANDS WITH CORRECTION, applied
Add to §2.2: "Convention. {σ_z|t_d}² = {E|T} with T = σ_z t_d + t_d = (a/2, a/2, 0), a lattice vector (CW1-C48). For k in the plane, a Bloch state's glide eigenvalue is ς_n e^{−ik·T/2}, and the glide parity is ς_n = ±1.
ς_n is defined with k the **reduced-zone** label. Moving k by G = (2̄00)·2π/a multiplies e^{−iG·T/2} = −1, so the label flips across the X face.
With this convention the vertex ρ_mn(k, q) with q, k in the plane is allowed iff ς_m ς_n e^{−iG′·t_d} = +1, where G′ is the Umklapp vector of k + q. 'σ_z-odd relative to Δ₁' in §2.2 means ς_v ς_c = −1 at G′ = 0."
The proof in §2.2 is VER V7's re-derivation; ρ = s_c s_v e^{−iG′·t_d}e^{i(k_c − k_v)·(T/2 − t_d)}ρ with T/2 − t_d = (0, 0, −a/4) gives a unit phase in the plane.

### E-9. V13, OC-6 (LA-kink SOC admixture): STANDS WITH CORRECTION, applied
§4 and §13: "≲ 10⁻⁴" is the on-axis ZPL-vertex transfer. At the mirror-plane optimum the computed lift relative to the allowed partner is 1.285×10⁻⁴/0.0649 = **2.0×10⁻³** (amplitude 4.5%, CW1-C49), WP3's old number.
Replacement: "SOC admixture of the LA kink ≲ 10⁻⁴ (on axis) and ≈ 2×10⁻³ (off-axis mirror-plane geometry) relative weight [E, transfer of the CALC ZPL-vertex lift, CW1 §13]".

### E-10. V14, CW1-L5, LE-28 (TDA): STANDS WITH CORRECTION, applied, and quantified (Rebuttal R-4)
(CW1.5) is the error of a **resonant-only** ε₁, (E₀ + ω)/2E₀ (sympy, CW1-C43). It is not the TDA error.
A standard (retarded) TDA BSE keeps both ±E_λ poles with the TDA eigenvectors, and its ε₁ is then the Kramers–Kronig transform of ε₂^{TDA}.
The coupling-block (beyond-TDA) error is estimated here in a one-oscillator model with coupling kernel K (A = Δ + K, B = K):
  χ^{TDA}(0)/χ^{full}(0) = (Δ + 2K)/(Δ + K),   Ω^{full} = [Δ(Δ + 2K)]^{1/2} = Δ + K − K²/2Δ + …,   residue ratio Δ/Ω,                                    (CW1.5′)
so the coupling error is O(K/(Δ + K)), first order in the coupling block. Here K stands for the whole resonant–antiresonant block B = 2v̄ − W̃: the exchange, plus the direct-W piece W_{cv′,vc′}.
Under the CW1 rule (head removed from the BSE exchange; external screening from RPA+LFE) the exchange left in B is the local-field part. The direct piece is the small interband W_{cv′,vc′}.
Its size is of the order of the Si LFE correction to ε₂, ≈ 10% [E]. Corrected §5 text:
"With E₀ = 4.8 eV … a **resonant-only** ε₁ overstates L by ≈ ×2 [E]. A retarded TDA (both time orderings) has no such error. The remaining coupling-block error is O(K_LF/(Δ + K_LF)) ≈ 10% on the proper ε₂ [E] (CW1.5′)."
The rule (TDA for ε₂, external screening from the full RPA+LFE ε₁) stands. LE-28 spec item (i) becomes: "report S^{TDA,ret} and S^{full} (and S^{res-only} as a control of (CW1.5)) at |q| = 0.5, 0.7, 1.0, 1.4 keV; pass: |S^{TDA,ret}/S^{full} − 1| ≤ 0.15."

### E-11. V19, OC-11, LE-35 (L3 factor): FALLS, withdrawn
WP1-v3 l.458: "with r ≳ 20 the true rate is ≥ (√r − 1)² ≳ 12 times theirs". So 12 is the Cauchy–Schwarz lower bound, not an IP value. In medium r is larger by 2–9 (l.457; D3).
Exact statement (sympy, CW1-C42): true/theirs ∈ [(√r − 1)², (√r + 1)²]. This is 12–42 for the IP r = 20–30 and 28–304 for r × (2–9). Multiplying the bound by 0.7 and the IP r by 1.3 ("8–39") mixes a bound with an estimate.
§12 sentence "Composing the IP range with δ_LF^{jT} ∈ [−0.3, +0.3] gives the stated interval 8–39 [E]; the factor is no longer 'unresolved' in kind, only in value" is **withdrawn**. Replacement:
"L3 is unchanged: ≥ 12× (Cauchy–Schwarz, IP r ≳ 20), larger in medium (r × 2–9), factor UNRESOLVED pending the G10 mixed blocks (CW1.12). The Cauchy–Schwarz band is [(√r − 1)², (√r + 1)²] once r is computed."
(CW1.12) stands as a definition. The exact remaining gap is the G10 run that gives r(q, ω) and δ_LF^{jT}. LE-35 stays CLOSED-AS-EXACT-GAP with the L3 text unchanged; OC-11 is not applied.

### E-12. V21, OC-7, CW1-L6, §13 (Si on-axis SOC lift): STANDS WITH CORRECTION, applied (and Rebuttal R-1)
At the on-axis extremum the hole is at Γ, where bands 5–8 form the Γ₈ quartet (degenerate to < 10⁻⁶ meV). Any single Kramers pair inside it is gauge-dependent: the regenerated runs give 1.0×10⁻⁶ and 1.7×10⁻⁶, against 1.6×10⁻⁶ in CW1.
The gauge-invariant quantity is the quartet sum. The regenerated scalar-equivalent value is **3.58×10⁻⁶** (= the CW1 run's all_valence/2, to 10⁻³; the split-off pair adds 0) (CW1-C15). That is **0.49%** in amplitude relative to 0.150 (CW1-C49).
§13 replacement: "Scalar-equivalent vertices: at the on-axis extremum 3.6×10⁻⁶ (Γ₈ quartet sum/2, gauge invariant) and at the 1.39 keV on-axis pair 2.6×10⁻⁶ (non-degenerate), i.e. 0.4–0.5% in amplitude relative to 0.15.
WP1-v3's '≈ 4% amplitude' overestimates the on-axis lift by ≈ 8–10. At the mirror-plane optimum the lift is 1.3×10⁻⁴ (non-degenerate, regenerated 1.285×10⁻⁴)."
Pitfall line: "compare Kramers-pair sums, and over a degenerate multiplet (Γ₈) the whole multiplet sum; never single spinor bands."

### E-13. V29, CW1-L9, LE-178 (non-adiabatic ZPR): STANDS WITH CORRECTION, applied
Order estimate re-done (CW1-C47): ΔZPR = Ω|g₀|²(2m*)^{3/2}√ω₀/4π with D₀ = 5 eV/Å [E], m* = 0.3–0.5 and ℓ₀ ×1–√2 (mode-mass convention) gives **0.26–1.1 meV**.
Replace "**ΔZPR ≈ 0.2 meV**" by "ΔZPR ≈ 0.3–1 meV [E]". Replace "So in Si the non-adiabatic correction is ≲ 1 meV (≲ 2% of ZPR_g) [E]" by
"So in Si the non-adiabatic correction is **≲ 2 meV [E, own estimate]**; this is not stated in 2011.12765. Its Si table gives AHC −56 meV (present work) and ASC −65 meV (ref. [35] there), re-read in the kept HTML. These differ by source and method, not only by adiabaticity, so their 9 meV difference does not bound non-adiabaticity."
The window impact (≤ 0.002 MeV, from the ≲ 10 meV k-dependence) is unchanged.

### E-14. V31 (c_LA in C26): STANDS, aligned
C26 now uses c_LA[100] = 8.18 km/s [CALC, COMP-PH l.32], as in the text: D/c = **315 keV** (CW1-C26). §26 (ii) "D/c ≈ 300 keV" → "D/c ≈ 315 keV".

### E-15. VER §3 (CLOSED-AS-EXACT-GAP specifications): missing steps and thin specs completed
- **LE-24 Ge:** E-4 (sentence replaced, SOC and re-minimisation lines added). The missing step stays single (QP E^{ZP}(q) on the joint space).
- **LE-26: not a single missing step. All missing steps:** (1) S^{PA}(q, ω) from the amplitude, not (P.1), on the cone bins (CW1 §3.3 spec, unchanged);
  (2) **the ZPL side on the same bins**, now a spec of its own:
  - What: S^{X0}_II on the {001}/{011} cone grid. Inputs: the anisotropic reduced-mass tensor μ(Q) of (CW1.6) at each bin, and the DFT vertex ρ(k_e, k_h) for **both** top heavy-hole bands (the second band is mirror-even, E-7c). Take the pair relaxed per bin and use c₁ and c₂ near the X face.
  - τ: `nB=0|ng=0|X=Wannier-Mott(anisotropic μ(Q), static ε_∞)`.
  - Method: Wannier E-surfaces as in errata_ratio.py; vertices by Miller matching on 3³ stencils per bin (as errata_analysis.py); (CW1.4′)/(CW1.4b) replaced by a direct sum over bins.
  - Convergence: vertex stencil h = 0.01 → 0.02 changes |ρ|² < 2%; angular grid 0.01 → 0.005 rad changes S̄ < 1%; ZPL/PAER per bin stable to 5% under 1.5× the bin count.
  - Pitfalls: band-index ordering is not parity ordering off axis (assign by ς); the Δ₅ degeneracy on axis needs pair sums; SOC on the bands (+15.5 meV at the first-hole bins).
  - Cost: < 1 CPU-h (≈ 10³ k points, NC 40 Ry).
  (3) The isotropic-μ_x bias (×1.3–1.6) is removed by (2).
- **LE-28:** single missing step (beyond-TDA run) stands; item (i) corrected in E-10.
- **LE-30: the control is replaced.** "(W.14) with W off vs (M.1)" only tests the W = 0 limit that the M2 theorem already proves. New control (spec):
  - Model: a 1D two-band chain, N = 8–12 cells, spinless electrons, contact e–h interaction W (inter-orbital on-site), and one Holstein/SSH phonon mode coupled linearly (g).
  - Computed: (i) the exact O(g) phonon-assisted transition amplitude to the (one pair + one phonon) final states, from exact diagonalisation in the 0-, 1- and 2-pair sectors (Lanczos), extracted at g = 10⁻³–10⁻² by a linear fit;
    (ii) the same amplitude from (W.14), built from the model's exact one-pair excitons only.
  - Pass/measurement: agreement to 10⁻⁶ at W = 0, as the M2 theorem requires. For W/E_g = 0.05–0.3 the deviation **is** the two-pair-sector correction, to be compared with the O(E_x^b/E_g) estimate.
  - Convergence: N = 8 → 10 → 12 with finite-size extrapolation; probe q on the N-point mesh; Lanczos residual < 10⁻¹⁰.
  - Pitfall: the 2-pair sector must be in the ED basis (dimension ∝ N⁴), otherwise the test is circular.
  - τ: `ng=1|X=ED(1D)`. Cost: minutes to an hour (Python/scipy sparse).
- **LE-32:** add the convergence criterion: S_HR and ω̄ change < 10% from 64 → 216 atoms (else 512); ΔSCF vs TDDFT relaxation energy agree to 20%.
- **LE-33:** add: k grid 12³ → 16³ changes the (E11) relativistic f-sum shift by < 0.05% (absolute) and S(q, ω) at q = 10, 30 keV by < 2%.
- **LE-35:** single missing step (G10 mixed blocks) stands; the interval statement is withdrawn (E-11).
- **LE-36 Ge:** add a convergence line: ecutwfc 60 → 80 Ry changes the quartet/Kramers-pair vertex sums < 2%; ecutfock 120 → 160 Ry and nqx 3³ → 4³ change E_g(L), E(Γ₇⁻) by < 10 meV; HSE nscf at the (k_v, k_v + q) of the §1.4 minimisation, re-minimised as in E-1.
- **LE-39: correction.** "Lebedev 110 points suffice to ℓ = 8 exactly" is false. The 110-point rule is exact to degree 17 (CW1-C44: x¹⁶ exact, x¹⁸ wrong by 5×10⁻⁷).
  So ∫K₈S is exact only if S has no ℓ ≥ 10 content, and near the edge (E_min minima at ϑ ≈ 0.13–0.34 rad) it has.
  Replacement: "q̂ grid: Lebedev 110 → 230 → 434 points (degree 17 → 25 → 35); pass: S₄, S₆, S₈ change < 1% between the last two. Near the edge, add the adaptive cone grid of LE-26 (2), because S(q̂) has structure on 0.1 rad."
- **LE-41: correction (and Rebuttal R-6).** CW1-C45 checks the meshes. The n = 3 cubic supercell (2π/3a = 0.76 keV) reaches |q| = 0, 0.76, 1.08, 1.32, 1.52 keV, not 0.77/1.16. n = 4 reaches 0, 0.57, 0.81, 0.99, 1.14 keV.
  "δ_LF + δ_pair stable to 5% under n = 3 → 4 at q = 1.15 keV" is impossible (n = 3 and n = 4 share no non-zero q below 2.28 keV).
  Replacement: "Convergence: n = 2 (64 atoms) → n = 4 (512 atoms) at the common |q| = 1.14 keV, change < 5%; plus Λ(|q|) from n = 3 and n = 4 compared after interpolation in |q| (0.76–1.52 keV), difference < 5%.
  Pitfall: at n = 2 the ZG configuration samples only the 2³ phonon mesh, so the n = 2 → 4 change also measures phonon sampling; report both antithetic configurations."
  The n = 4 cost estimate is unchanged; the n = 2 run costs ≈ 10² CPU-h.
- **LE-34, LE-47:** "yes / yes" (VER), unchanged.

### E-16. VER §2 on (CW1.23): STANDS WITH CORRECTION, applied
Add to §23: "The inverse transfer is exact for branch-resolved data. For branch-unresolved data (one spectrum, ≥ 2 replicas) it is ill-posed: the forward map {𝒜_ν} → σ₁ has a null space.
It then needs the branch weights from resolved data (20 K Macfarlane TA/TO) or from COMP-PAER tier H, and the result inherits their error."

### E-17. VER §5 (smaller points)
- §2.1 "for scale, the four-band sum Σ|ρ|² at |q| = 1.155 Å⁻¹ is 0.45" → "… is 0.45 (4 conduction bands, direction-averaged; not comparable one-to-one with the single-band 0.150)".
- §3.3 ε_ex^{max} at the optimum |q| underestimates the reachable excess energy at fixed m_χ (CW1-C51; < 2 meV at 0.42 MeV); the bias makes the ZPL-open region slightly larger than stated. Recorded in E-7.
- §1.2 0.17 → 0.155·2π/a (E-1). C26 constant aligned (E-14). Interface flags carry the SOC numbers (§2).

---
## 2. Re-issued owed corrections, interface flags, LIMITS rows, closure-table rows (merger uses this section; "unchanged" = CW1.md text)

**Owed corrections (target → exact replacement text; not applied here)**
- **OC-1 LIMITS L8 (Note/action, ✎R16 clause)** → "✎R16/CW1 (+ERR-CW1): Si window [CALC]: PAER-only 0.333 (replica) / 0.3374 (continuum) – 0.402–0.405 (1s) / 0.405–0.408 (continuum ZPL; best 0.407, PBE+SOC, a_exp, DFT-re-minimised) MeV.
  The first ZPL is off the valley axis in a {001} mirror plane and second class by the mirror (CW1 §1–§2, errata E-1). PAER leads to ≈ 0.42 (at least) – 0.43 (central) MeV; two-channel ≈ 0.43–0.51.
  The allowed-size ZPL ((2̄00) class, X face) opens at ≈ 0.50 MeV (ZPL/PAER 2–7) and leads from ≈ 0.51 MeV [E, vertex CALC]. 0.547 MeV is the nearest-pocket (2̄00) value. Rate/reach [E] only (L8-N2)".
- **OC-2 WP1-v3 §3.4 "Summary for WP3/WP6" and IF-6 v3 cell** → "Si zero-phonon line opens at 0.405–0.408 MeV (continuum; best 0.407; 1s 0.402–0.405) [CALC, PBE+SOC, a_exp; CW1 §1, errata E-1]. It lies off the valley axis (ϑ_ZP = 0.18 rad, {001} plane, hole off Γ) and is second class by the σ_z mirror.
  An allowed-size zero-phonon channel ((2̄00) class, X face, |ρ|² ≈ 0.01–0.04 for c₁, 0.028 for c₁ + c₂) opens at ≈ 0.50 MeV and leads from ≈ 0.51 MeV. The (2̄00) vertex is not small (Σ_v|ρ|² = 0.150 at its extremum, light hole) [CALC, CW1 §2]. Ge: formulated (CW1 §1.4, errata E-4)."
  Delete "it leads only if |ρ_cv^{(2̄00)}| ≳ η_PA^{1/2}|ρ_cv^{ref}| [E, open …], otherwise the reliably allowed class starts at ≈ 0.62 MeV ((1̄11))" in §3.4, §3.7, IF-6 and R9 N1.
- **OC-3 WP1-v3 §3.7 table [E14] and IF-6b** → replace the ϖ_II table by "ϖ̄_II (angle-averaged, (CW1.4′) of ERR-CW1, relaxed-pair vertex, SOC edge) = 0.020 / 0.16 / 0.34 at ε_ex = E_x^b / 50 / 100 meV, i.e. ≤ 0.34 at 100 meV;
  first heavy hole only, the cone model valid for all three (min-of-cones). Second (mirror-even) heavy hole open from 0.415–0.420 MeV, (CW1.4b), upper estimate. Pointwise at the optimum 0.01–0.04 (k_rel) + 0.03–0.10 (SOC) [vertex CALC, PAER E ×/÷10]".
  Replace the interim sentence by "PAER leads the integrated electronic rate at least to ≈ 0.42 MeV, centrally to ≈ 0.43 MeV; two-channel ≈ 0.43–0.51 (the second heavy hole dominates the ZPL side above 0.43); allowed-size ZPL opens at ≈ 0.50 and leads from ≈ 0.51 MeV (CW1 §3.3, errata E-7)".
- **OC-4 WP3-v3 §M9 window bullets (1)–(3) and IF-8 v3 cell** → (1) "m_χ^{PA} ≲ m_χ < 0.405–0.408 MeV [CALC, PBE+SOC]"; (2) "0.405–0.51 MeV: PAER coexisting with the forbidden-class (mirror) ZPL and, from 0.415–0.420 MeV, the second heavy-hole channel.
  PAER leads to ≈ 0.42–0.43, ϖ̄ per CW1 §3.2 / ERR-CW1 E-7; the allowed-size ZPL opens at ≈ 0.50, comparable"; (3) "above ≈ 0.51 MeV the allowed-size ZPL ((2̄00) class) leads; PAER/ZPL ≲ 0.1 pointwise there, 10⁻²–10⁻⁵ on the axis".
- **OC-5 WP3-v3 §M3(c)** → "Si (M_x = m_l + m_hh[100] = 1.19 m_e [CALC, PBE, no SOC, CW1 §1.3]; 1.41 m_e (source not stated in WP3) is withdrawn): Q_w = 0.31 Å⁻¹ at δ₀ = 0.3 eV".
- **OC-6 WP3-v3 §M3(e), §R1 and the p̄_on table** → "crossover |q| ≈ 1.35 keV [CALC, COMP-PH §4]; the window low-mass end is on axis"; table row "(2̄00) class: LO minimum off axis [CALC, CW1 §4] → p̄_on = 3 (TA, TO, LA, LO)".
  LA kink: "SOC admixture ≲ 10⁻⁴ (on-axis geometry) and ≈ 2×10⁻³ (off-axis mirror-plane geometry) relative weight [E, transfer of the CALC ZPL-vertex lift, CW1 §13 / ERR-CW1 E-9]" (replaces "~2×10⁻³ [E]").
- **OC-7 WP1-v3 §3.2(c) last bullet and §10 item 6** → "SOC lifts the Si on-axis zero to |ρ|² ≈ 3.6×10⁻⁶ at the extremum (Γ₈ quartet sum, gauge invariant) and 2.6×10⁻⁶ at the on-axis pair (0.4–0.5% amplitude), and the mirror-plane zero to 1.3×10⁻⁴ [CALC, CW1 §13, ERR-CW1 E-12]; Ge ≲ 10% [E] (formulated)".
- **OC-8 COMP-PH §0 row "ZPL kinematic edge" and §4 "m_ZPL = 0.4154 MeV"** → "0.4154 MeV is the on-axis local optimum; the joint (q,k) minimum is 0.405–0.408 MeV off axis (best 0.407, PBE+SOC, a_exp; CW1 §1.2, ERR-CW1 E-1)"; and "the allowed/forbidden split … not computed here" → "computed in CW1 §2".
- **OC-9 COMP-PAER §0 item 1, §4 table, IF-CP-1** → COMP-PAER's "first zero-phonon final state 0.405–0.408 MeV (continuum)" is **kept** (now [CALC, CW1/ERR-CW1: 0.407 with SOC, re-minimised]). Add: "allowed class (2̄00): 0.547 MeV is the nearest-pocket assignment; the allowed-size channel opens at ≈ 0.50 MeV on the X face (CW1 §2.3)".
- **OC-10 LIMITS L9b note:** unchanged.
- **OC-11 LIMITS L3 note:** **withdrawn; do not apply.** L3 keeps "≥ 12× (Cauchy–Schwarz, IP r ≳ 20), larger in medium (×2–9 on r), factor UNRESOLVED" (ERR-CW1 E-11).
- **OC-12 SOTA C8 / CONTROLS C8:** unchanged.

**Interface flags**
- **IF-CW1-1** → "(WP3 §M9, WP1 IF-6/6b, WP6 (3.1′)/IF6-10, M1/SOTA, paper): Si window statements change (OC-1…OC-4): PAER-only to 0.402–0.405 (1s) / 0.405–0.408 (continuum) MeV [PBE+SOC]; PAER-leading to ≈ 0.42–0.43; two-channel ≈ 0.43–0.51; allowed-size ZPL opens at ≈ 0.50 MeV (comparable) and leads from ≈ 0.51 MeV."
- **IF-CW1-2:** unchanged, plus "SOC in the bands and the DFT re-minimisation of ERR-CW1 E-1; no anisotropy-based lowering is transferred from Si (E-4)".
- **IF-CW1-3** → "(WP8-F G-F5, COMP-PH §4 window FOM): E^{ZPL}_min(q* = 0.90 keV), minimised over q̂ and k, is 1.697 eV (Wannier, a_PBE, scalar) at ϑ = 0.34 rad (emin_qstar.json), not 1.715 (five directions).
  At a_exp the same point gives 1.711 eV (DFT scalar) and **1.727 eV (DFT, PBE+SOC)**, not re-minimised (≲ −1 meV expected) (out/errata_qe.json). Use 1.727 eV for the a_exp/SOC convention of the campaign and recompute Δm/m (WP8-F §2.7(b))."
- **IF-CW1-4** → "(COMP-PAER tier H owner): the stage-6 output grid must include the {001} mirror-plane cones (§3.3), the **second heavy-hole cone on the axis** (E-7c), and the X-face (2̄00) edge with c₁ and c₂. ZPL vertices with the hole at k_v(q), pair relaxed; bands with SOC."
- **IF-CW1-5** → "(WP6 nuisances, IF-3 of WP1): Si second-class bound-line amplitudes use the mirror-plane vertex with the relaxed-pair q coefficient (|∂_{q_z}ρ|_rel| = 1.57 Å; |∂_{k_z}ρ| = 0.32 Å) and the SOC-lifted 1.3×10⁻⁴.
  The second heavy hole (on-axis edge 0.415–0.420 MeV, g_⊥ = 2.21 Å) adds a linearly vanishing allowed channel (E-7c). The on-axis (n_H² − 1)/(3πa_x⁵n_H⁵) form is the on-axis special case."
- **IF-CW1-6:** unchanged, plus: "LE-35 keeps the CW1 status with the L3 text unchanged; the 'value only' upgrade is withdrawn".

**LIMITS rows (return-local labels)**
| # | Owner | location | chain | status | note |
|---|---|---|---|---|---|
| CW1-L1 | CW1 | §1, (CW1.1); ERR E-1 | [E13] as a joint (q,k) minimum on Wannier/DFT bands | CALC (Wannier TB global; DFT PBE+SOC local re-minimisation, CW1-C33/C34) | Si m_χ^{ZP} 0.405–0.408 (best 0.407; 1s 0.402–0.405) MeV; off axis, {001} plane. Included: SOC +0.003. Validity: rigid scissor; global search on scalar Wannier |
| CW1-L2 | CW1 | §2.2; ERR E-8 | σ_z glide selection, parity ς_n with reduced-zone k | D, CALC-checked | G′ = 0 top-hole vertex zero in {001} planes; (2̄00) allowed |
| CW1-L3 | CW1 | §2.3; ERR E-5 | (CW1.1) restricted to the (2̄00) class | CALC (edge); E (leading) | allowed-size ZPL opens ≈ 0.50 (ZPL/PAER 2.4 (c₁) to 7.0 (c₁ + c₂)), leads from ≈ 0.51 MeV; IF-6 hedge removed |
| CW1-L4 | CW1 | §3, (CW1.3), (CW1.4′), (CW1.4b); ERR E-7 | [E8] ZPL vs COMP-PAER (P.1) in ε₂ units | E (vertex CALC, PAER ×/÷10; second hole upper estimate) | ϖ̄_II ≤ 0.34 at 0.1 eV; PAER leads to ≈ 0.42 (at least) – 0.43 MeV (central) |
| CW1-L5 | CW1 | §5, (CW1.5), (CW1.5′); ERR E-10 | resonant-only vs retarded TDA vs coupling | D (models), size E | resonant-only ε₁ overstates L ≈ ×2; retarded-TDA coupling error O(K_LF/Δ) ≈ 10% on ε₂ |
| CW1-L6 | CW1 | §13; ERR E-12 | noncollinear QE vertex, multiplet sums | CALC (regenerated) | Si SOC lift 3.6×10⁻⁶ (extremum, Γ₈ sum), 2.6×10⁻⁶ (on-axis pair), 1.3×10⁻⁴ (mirror optimum) |
| CW1-L7 | CW1 | §23, (CW1.23); ERR E-16 | WP3 §4(b) inverted | D | exact for branch-resolved data; ill-posed without branch resolution |
| CW1-L8 | — | — | — | — | unchanged |
| CW1-L9 | CW1 | §25, (CW1.25); ERR E-13 | AHC Fan, NA − adiabatic | D; size E; Si ZPR [FT 2011.12765] | Si ΔZPR ≲ 2 meV [E, own estimate; not stated in 2011.12765]; window ≤ 0.002 MeV |

**Closure-table rows (CW1 §0) re-issued; the rows not listed are unchanged**
| Row | Status | One-line result |
|---|---|---|
| LE-24 | CLOSED-AS-EXACT-GAP (Si part CLOSED) | Si first ZPL **0.405–0.408 MeV** (best 0.407, PBE+SOC, a_exp) [CALC] (off axis, {001} mirror plane; on-axis 0.415 is not the minimum); M_x = 1.19 m_e [CALC, no SOC]; Ge formulated (no anisotropy transfer) |
| LE-25 | CLOSED | (2̄00) vertex Σ_v\|ρ\|² = 0.150 [CALC], not small; allowed-size ZPL opens at ≈ 0.50 MeV (ZPL/PAER 2–7), leads from ≈ 0.51 MeV by ≥ 10; 0.62 fallback withdrawn |
| LE-26 | CLOSED-AS-EXACT-GAP (two missing steps, ERR E-15) | ϖ̄_II = 0.020 / 0.16 / 0.34 at E_x^b / 50 / 100 meV ((CW1.4′)); second heavy hole from 0.415–0.420 MeV; PAER leads to ≈ 0.42–0.43; two-channel ≈ 0.43–0.51 MeV |
| LE-28 | CLOSED-AS-EXACT-GAP | resonant-only ε₁ overstates L ≈ ×2 [E]; retarded-TDA coupling error O(K_LF/Δ) ≈ 10% [E]; consistent hybrid rule; spec |
| LE-35 | CLOSED-AS-EXACT-GAP | mixed-block formula (CW1.12); L3 unchanged (≥ 12×, factor UNRESOLVED; Cauchy–Schwarz band [(√r−1)², (√r+1)²]); spec |
| LE-36 | CLOSED-AS-EXACT-GAP (Si part CLOSED) | Si SOC-lifted vertex [CALC]: 3.6×10⁻⁶ at the on-axis extremum (Γ₈ sum; WP1's 4% amplitude → 0.5%), 1.3×10⁻⁴ at the true optimum; SOC raises the Si ZPL edge by +0.003 MeV; Ge spec |
| LE-178 | CLOSED | formula (CW1.25); Si ZPR_g −56 meV [FT 2011.12765]; non-adiabatic term ≈ 0.3–1 meV, ≲ 2 meV [E, own]; window impact ≤ 0.002 MeV |
Counts unchanged: CLOSED 15, CLOSED-AS-EXACT-GAP 11, CANNOT-CLOSE 0. Status upgrades per VER §1: LE-35 "unresolved in kind → value only" withdrawn; all others stand with the wording above.

**Symbols introduced (NOTATION/CONVENTIONS grepped: none of these occurs)**
| symbol | meaning | status |
|---|---|---|
| ς_n | σ_z glide parity of a Bloch state with reduced-zone k in the plane: eigenvalue ς_n e^{−ik·T/2}, T = (a/2, a/2, 0) | **new** |
| ε_touch | excess energy at which adjacent {001} cones touch, ϑ_ZP²β_θβ_z/(β_θ + β_z) | **new** |
| ∂_{q_z}ρ\|_rel | relaxed-pair (centre-of-mass) q coefficient of the second-class vertex out of the mirror plane (CW1's \|∂_{q_z}ρ\| was at fixed k_v) | **new** |
| β^{ZP}_2(α) | angular curvature of the second heavy-hole pair energy at the on-axis edge, azimuth α (cf. CW1's β^{ZP}_θ, β^{ZP}_z) | **new** |

---
## 3. Rebuttals (verifier claims that are wrong or wrongly scoped; numbers conceded where right)

**R-1 (V21, OC-7, CW1-L6: "(1.6–3.6)×10⁻⁶").** The verifier is right that the single pair is gauge-dependent. The proposed range, however, puts a gauge artefact as its lower end.
Two regenerated runs give the single-pair value as 1.0×10⁻⁶ and 1.7×10⁻⁶, with CW1 at 1.6×10⁻⁶; the quartet sum is 3.575×10⁻⁶ in all three (CW1-C15). The quartet sum is the only physical number, and it is a value, not a bound.
Hence "3.6×10⁻⁶ (0.49% amplitude)", with no range (E-12).

**R-2 (VER §0: "m_hh[110] = 2.5 m_e 'flat direction' is a no-SOC object (4×4 k·p with SOC gives ≈ 0.57 m_e)").** False at the point that matters. The SOC DFT hole mass tensor was fitted at the re-minimised optimum (full quadratic on a 3³ stencil, rms 0.25 meV).
Its flat-direction eigenvalue is **m = 2.07 m_e with SOC**, against 2.00 m_e scalar (CW1-C35). The hole is 77 meV below Γ₈, outside the k·p regime where SOC removes the warping.
The SOC and scalar re-minimised optima differ by < 0.002·2π/a, and the SOC re-minimisation lowers m by 0.0006 MeV, not the "≤ −0.002" allowed for (E-1).

**R-3 (V10 and VER §2: "Validity ε ≲ β_θϑ² = 0.081 eV correct").** Not correct. β_θϑ² is where a cone reaches the axis. The four cones of one valley lie on a circle, and adjacent ones touch first, on the 45° line, at ε_touch = ϑ²β_θβ_z/(β_θ + β_z).
Derivation (sympy, CW1-C36): on y = x the cone (x − ϑ, y) has β_θ(x − ϑ)² + β_zx², minimal at x = β_θϑ/(β_θ + β_z) with value ϑ²β_θβ_z/(β_θ + β_z) = 0.0486 eV.
So the 50 meV entry is at the limit and the 0.1 eV entry overcounts by ×1.34 (0.354 → 0.265 at fixed vertex). The corrected (CW1.4′) has no overlap (E-7a). The verifier's "overlap at 0.1 eV" remark is right; the stated validity is not.

**R-4 (V14: "the TDA (coupling-block) error … stays unquantified").** It can be bounded at the same level as (CW1.5). In a one-oscillator model the retarded-TDA/full ratio is (Δ + 2K)/(Δ + K) at ω = 0, with residue ratio Δ/Ω (sympy, CW1-C43).
So the error is first order in the kernel left in the BSE. Under the CW1 rule that kernel is the local-field exchange only, and the error is O(K_LF/(Δ + K_LF)) ≈ 10% [E]. The scope correction (resonant-only ≠ TDA) is conceded (E-10).

**R-5 (V8: "the in-plane X face is the X–W line where c₁/c₂ are degenerate … the '0.0095' is sensitive (×3)").** Partly wrong in scope. The computed edge point has k_e = (−1, 0.028, 0.023)·2π/a: off the z = 0 plane and off the X–W line.
There c₂ lies 50 meV above c₁ (CW1-C41). At the opening (ε_ex < 50 meV) only c₁ is open, so 0.0095 and the ratio 2.4 are the right numbers there. c₁ + c₂ = 0.028 applies only ≥ 50 meV above the opening or nearer the X–W line.
The sensitivity is conceded as a range, 2.4–7.0 (E-5). The decision is unaffected either way.

**R-6 (VER §3 LE-41: "the test must use n = 3 vs n = 6 at a common q, or compare Λ(q) after interpolation").** The mesh facts are right (CW1-C45). The proposed n = 6 (1728 atoms, ≈ 10⁵–10⁶ CPU-h on CW1's n = 3 → 4 scaling) is not needed.
n = 2 and n = 4 share |q| = 1.14 keV, so the common-q test is n = 2 → 4. That is cheaper than the n = 4 run itself, but it confounds supercell-LFE and ZG phonon sampling, which is stated as a pitfall (E-15).

**R-7 (V11: "the second heavy hole … omitted … all inside ×/÷10").** Inside ×/÷10 at 0.42 MeV, yes. It is not negligible, though: computed with (CW1.4b), it is comparable to the first-hole channel at 0.43 MeV and dominates by ×4 at 0.44 MeV (E-7, CW1-C39).
It moves the central PAER-leading end from ≈ 0.44 to ≈ 0.43 MeV. The verifier's verdict (STANDS WITH CORRECTION) is kept, but the correction changes a headline number of LE-26 and OC-1/3/4.

Conceded without rebuttal: V2/V3 (headline number, verified and refined), V4, V5, V9, V13, V19/OC-11, V29, V31, V32, LE-26/30/32/33/36/39 specs, the (CW1.4) relaxed-pair and convention points, and §5.

---
## 4. code/CW1 changes (checks.py: 32 → 52 checks, all PASS, ≈ 8 s, one core)
- **Circular checks removed or labelled.**
  - C1 now recomputes k_c, m_l, m_t, m_hh from the raw QE eigenvalues in masses.json (to 10⁻³) and reports nonparabolicity. Its note no longer asserts the "DOS heavy hole".
  - C4 re-evaluates the committed Wannier TB at the stored optimum: E to 10⁻⁷ eV, m to 10⁻⁷ MeV, |∇m| ≤ 3×10⁻⁷, positive curvature. Before, it only recomputed m from two json numbers.
  - C6, C12, C14, C15 compare against the **regenerated** QE runs, not against their own json.
  - C10, C13 are labelled [consistency; not regenerated]; C18 is labelled [CW1 values, superseded]; C28 is labelled [arithmetic].
- **Tolerances tightened:** C7, C8, C10, C13, C17 (10⁻⁴), C18, C19, C23, C26, C28 (windows of 1–5% around the computed value instead of factor-of-two windows).
- **Fixes:** C26 uses c_LA = 8.18 km/s (V31). C15 tests the Γ₈ quartet sum (gauge invariant) and the regenerated mirror lift. C7/C19 use the SOC re-minimised edge. The nB overflow warning is removed.
- **New checks:**
  - C33 SOC shift (pseudo-consistent); C34 DFT re-minimisation, SOC edge 0.4072, scalar 0.4042; C35 SOC flat hole mass (R-2).
  - C36 cone-touching energy (sympy) and min-of-cones vs closed form (R-3); C37 midpoint model vs Wannier; C38 relaxed-pair split (sympy) and ∂_{q_z}ρ|_rel.
  - C39 second heavy hole, β^{ZP}_2 and the crossover in m_χ; C40 record of the E-7 table; C41 X-face c₁ vs c₁ + c₂ and its SOC shift (regenerated).
  - C42 L3 Cauchy–Schwarz band (sympy); C43 resonant-only / retarded-TDA / coupling (sympy); C44 Lebedev degree; C45 LE-41 meshes.
  - C46 Luttinger warping; C47 ΔZPR range; C48 glide algebra; C49 lift ratios; C50 q* pair; C51 ε_ex^{max} bias; C52 hole depth vs Δ_SO.
- **New files:**
  - scripts: errata_kset.py, errata_kset2.py, errata_analysis.py, errata_ratio.py, errata_xface.py, run_errata_qe.sh
  - inputs: errata/{scf,nscf}_{S12,FRav,SOC}.in, nscf2_{S12,SOC}.in, nscf_xface_{FRav,SOC}.in, k sets and labels
  - outputs: out/errata_qe.json, errata_qe_it2_{S12,SOC}.json, errata_ratio.json, errata_xface_soc.json
  - checks_orig.py is not kept in the package; the CW1 version is CW1.md's record.

---
## 5. Closing table: verifier item → resolution → location
| VER item | verdict | resolution | location |
|---|---|---|---|
| V1 | STANDS | holds with SOC (0.4072 < 0.4152) | E-1; C34 |
| V2 | SWC | applied; computed: 0.405–0.408, best 0.407 (1s 0.402–0.405) | E-1; C33, C34, C7 |
| V3 | SWC | applied; COMP-PAER 0.405–0.408 kept | E-1; OC-8, OC-9 |
| V4 | SWC | applied ("source not stated"; PBE, no SOC); C1 recomputed | E-3; OC-5; C1 |
| V5 | FALLS | sentence replaced (Ge less warped; no transfer) | E-4; C46 |
| V6, V7 | STANDS | — (V7 derivation adopted in the convention) | E-8 |
| V8 | SWC | applied as range 2.4–7.0; SOC shift of the edge computed (+0.0024 MeV); scope rebutted | E-5; R-5; C41 |
| V9 | STANDS [E] | wording applied | E-6 |
| V10 | SWC | applied; validity limit corrected to 0.049 eV | E-7a; R-3; C36 |
| V11 | SWC | applied; computed (SOC edge, relaxed vertex ×1.31, second hole); central end 0.44 → 0.43 MeV | E-7; R-7; C38–C40 |
| V12 | STANDS | — | — |
| V13 | SWC | applied (geometry stated) | E-9; OC-6; C49 |
| V14 | SWC | applied (resonant-only); coupling error quantified | E-10; R-4; C43 |
| V15–V18 | STANDS | — (V18 kept as sketch) | — |
| V19 | FALLS | withdrawn; L3 unchanged; band [(√r−1)², (√r+1)²] | E-11; OC-11; C42 |
| V20 | STANDS | — | — |
| V21 | SWC | applied as the quartet value 3.6×10⁻⁶ (range rebutted) | E-12; R-1; C15, C49 |
| V22–V28 | STANDS | — | — |
| V29 | SWC | applied (≲ 2 meV, own estimate; 0.3–1 meV) | E-13; CW1-L9; C47 |
| V30 | STANDS | — | — |
| V31 | STANDS | C26 aligned (315 keV) | E-14; C26 |
| V32 | SWC | applied; computed 1.727 eV (a_exp, SOC) | E-2; IF-CW1-3; C50 |
| V33 | — | — | — |
| VER §0 SOC shift, re-minimisation owed | — | computed (+15.5 meV pseudo-consistent; re-min −0.0006 MeV) | E-1; C33, C34 |
| VER §0 "SOC flat mass 0.57 m_e" | — | rebutted (2.07 m_e) | R-2; C35 |
| VER §0 save dirs gone | — | vertices regenerated (pass-5 point, mirror rule, gradients, SOC lifts) | header; C6, C12, C14, C15 |
| OC-1…OC-9 | SWC | re-issued in full | §2 |
| OC-10, OC-12 | STANDS | unchanged | §2 |
| OC-11 | FALLS | withdrawn | §2; E-11 |
| VER §1 status upgrades | — | LE-35 upgrade withdrawn; rest stand | §2 closure rows |
| VER §2 (CW1.1), (CW1.5), (CW1.9), (CW1.20), (CW1.25), k_xc | — | no change; (CW1.5) scope per E-10 | E-10 |
| VER §2 mirror-rule convention | — | added (ς_n, reduced-zone k) | E-8; C48 |
| VER §2 (CW1.4) relaxed pair, cone overlap | — | computed; (CW1.4′) | E-7a,b; C36–C38 |
| VER §2 (CW1.12) | — | definition stands; interval withdrawn | E-11 |
| VER §2 (CW1.23) | — | ill-posedness stated | E-16 |
| VER §3 LE-24 Ge | — | E-4 + convergence line | E-4 |
| VER §3 LE-26 | not single | all missing steps stated; ZPL-side spec | E-15 |
| VER §3 LE-28 | — | item (i) corrected | E-10, E-15 |
| VER §3 LE-30 | spec insufficient | new ED control spec | E-15 |
| VER §3 LE-32, LE-33, LE-36 Ge | — | convergence criteria added | E-15 |
| VER §3 LE-35 | — | interval withdrawn | E-11 |
| VER §3 LE-39 | correction | Lebedev 110 → 230 → 434 | E-15; C44 |
| VER §3 LE-41 | correction | meshes corrected; n = 2 → 4 common-q test | E-15; R-6; C45 |
| VER §3 LE-34, LE-47 | yes | unchanged | — |
| VER §4 CW1-L1…L9 | — | re-issued (L8 unchanged) | §2 LIMITS |
| VER §5 C26 constant | — | aligned | E-14 |
| VER §5 0.17·2π/a | — | 0.155 (DFT k_c) | E-1, E-17 |
| VER §5 0.45 label | — | labelled | E-17 |
| VER §5 ε_ex^{max} bias | — | direction stated, computed | E-7, E-17; C51 |
| VER §5 IF SOC numbers | — | IF-CW1-1/3/4/5 re-issued | §2 |
