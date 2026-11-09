# R16 / CW4-errata: verification corrections to returns/R16/CW4.md (VER-CW4)

Errata agent ERR-CW4, brief briefs/R16/ERR-CW4.md, 2026-11-01. **Read together with returns/R16/CW4.md**, which is not edited (returns are the record).
Where this file gives replacement text, the replacement supersedes the CW4.md text at that site. The merger uses **only §B of this file** for the owed
corrections, interface flags and proposed LIMITS rows. Everything not named here stands as written in CW4.md (VER-CW4 §6, last line).
Read: returns/R16/CW4.md, referees/R16/VER-CW4.md, CONVENTIONS.md (§§10–14, R8/R13 amendments), NOTATION.md, code/CW4/checks.py (original),
returns/R14/WP8-U-table-v2.csv and returns/R16/WP8-U-table-v3.csv (rows cited), returns/R16/WP8-U-v2.md (header).
Literature (lit.py → literature/papers-ERR-CW4/, full text read, PDFs and HTML deleted afterwards, `.txt` extracts kept for the locators): 1910.02091 (v2),
1603.05351, 2401.11971 (v2), 2109.04473 [FT]. Facts that only VER-CW4 read are tagged **[FT per VER-CW4 Vn]**.
Checks: `python3 code/CW4/checks.py` gives **24/24 PASS in ≈ 1.5 s** (sympy exact algebra, scipy quadrature, numpy). The labels are CW4-Kn, with the changes listed in §D.
No heavy numerics were run. Tags are as in CONVENTIONS §12. Equation labels of this file are ERR-CW4 (E.n). Status of everything new: CLAIMED.

---
## A. Corrections, by verifier row

### A1. VER-CW4 V1, scope 5 CW4-b, §6 item 7: Allen attribution
**Stands; wording fixed.** Every occurrence of "result = Allen, PRB 3, 305 (1971)" (CW4 §12, OC-1, CW4-b) becomes "result = Allen (1971) **as cited by 1604.06800
Ref. [29]** (Allen not read; closed access)". The derivation and the [D] upgrade of LB1-10 are unchanged. Replacement texts: §B OC-1 and §B CW4-b.

### A2. VER-CW4 V5, §6 item 1: OPW size (LE-113, CW4 §17), **FALLS (numbers) → re-derived**
CW4 sampled two q per energy. It reported "−25 to −35 % for E_kin ≳ 50 eV", which is false away from those points. I reran the K4 functions on the full
grid (deterministic Fibonacci set of 2×10⁴ final directions; q along the orbital axis ẑ, in-plane x̂, and at 45°). The result (CW4-K4, errata version)
agrees with the independent VER-CW4 V5 rerun to ≤ 3 %, which is the Monte-Carlo noise of that rerun.
**Replacement for the "OPW size" paragraph of CW4 §17 [E, CALC, CW4-K4].** Model: C 2p_z Slater orbital (β_2p = 1.568/a₀ = 5.85 keV), M_PW = Ψ̃(k_f − q),
M_OPW = M_PW − Ψ̃(k_f)⟨ψ|e^{iq·r}|ψ⟩. The final-direction-averaged ratio |M_OPW|²/|M_PW|² has the following range, min–max over the three q directions:

| E_kin (k_f) | q = 5 | 7.5 | 15 | 25 | 40 keV |
|---|---|---|---|---|---|
| 10 eV (3.2 keV) | 0.70–1.22 | 0.74–3.02 | 2.09–67.4 | 6.87–275 | 7.52–509 |
| 50 eV (7.1 keV) | 0.66–0.96 | 0.73–1.00 | 0.65–0.91 | 0.94–1.51 | 1.16–4.28 |
| 100 eV (10.1 keV) | 0.67–0.97 | 0.90–1.11 | 0.91–0.98 | 0.73–0.93 | 0.39–0.92 |

Heavy-mediator kinematics reach q ≈ 2m_χv_max ≈ 50 keV at m_χ = 10 MeV, so every column is in range. Both the size and the sign of the correction depend on
q and on direction at every energy. The factor is 0.4–4.3 at 50–100 eV and 0.7 to ~5×10² at 10 eV. *Clarification (VER-CW4 V5):* the Bethe ridge of this
model is at q ≈ k_f, which is 3.2, 7.1 and 10.1 keV at 10, 50 and 100 eV. The large ratios occur for q ≫ k_f. There |M_PW|² falls as p⁻¹⁰, so they act on a
strongly suppressed term. A ratio table is therefore not a rate correction. Only the halo- and direction-weighted rate ratio is.
**Specification (closure of the size; book appendix "Wannier/EPW → response").** *What:* the rate-weighted factor
R_OPW(E_kin) = ∫ dq q η F²_DM Σ_occ|M_OPW|² / ∫ dq q η F²_DM Σ_occ|M_PW|² for graphene, per occupied orbital and in total. *Approximation:* frozen orbitals, a single
final continuum orthogonalised to **all** occupied states (C 1s, σ 2s/2p, π 2p_z), no FSI (FSI is the separate factor below; it is not multiplied in as an
independent factor). τ = `nB=0|ng=0|X=IP`, geom = 2D. *Method:* QE scf (SG15 C) → Wannier90 MLWFs of the occupied manifold (+ 1s from the pseudo-atom
reconstruction or an all-electron atomic orbital) → plane-wave transforms Ψ̃_n(p) and the overlaps ⟨ψ_n|e^{iq·r}|ψ_m⟩ by FFT → the K4 integrals with a 2×10⁴
Fibonacci final-direction set, q on a log grid 1–60 keV, campaign SHM halo (CONVENTIONS §8). *Convergence:* R_OPW stable to 1 % under direction doubling, a
doubled q grid and MLWF spread minimisation. The orthogonality Σ_n|⟨ψ_n|χ_k⟩|² = 0 holds to 10⁻⁶. *Pitfalls:* do not quote ratios where |M_PW|² is suppressed. The
pseudopotential core is missing, so the 1s overlap must come from an all-electron orbital. OPW is not a scattering state of the hole potential, so do not combine
it with a Sommerfeld factor without a common final state. *Cost:* CPU-minutes.
The FSI paragraph and (17.1) stand (VER-CW4 V5, V24). Replacement OC-5: §B.

### A3. VER-CW4 V6 = V25, scope 5 CW4-d, §6 item 2: (H_W) ordering and the error bound (LE-115, CW4 §19)
**(a) Ordering word.** OC-6 says "with Hermitian ordering". This is a slip, because the same sentence rejects the symmetrised ordering. It must say **"with ket-side
ordering"**. The CW4 §19 text and K7b already say this.
**(b) Remainder.** The first equality of (19.2) is exact. The second, "[1 + O(W_𝒲/ω_cv)]" with "relative error ≤ 2W_𝒲/ω_cv + (W_𝒲/ω_cv)²", bounds each
v′ term, not the sum. Replacement for that part of (19.2) and the following parenthesis:
  |A^{(H_W)}_a − (m_eq/M_κ)⟨c|r p^W_0|v⟩| ≤ (m_eq/M_κ)(2W_𝒲/ω_cv + W²_𝒲/ω²_cv) Σ_{v′∈𝒲}|r_cv′(p^W_0)_{v′v}|,                                    (E.1)
[D]: (ε_c − ε_v′)²/ω²_cv = (1 + δ)², δ = (ε_v − ε_v′)/ω_cv and |δ| ≤ W_𝒲/ω_cv. **No relative bound on the sum exists.** CW4-K7c gives a site projector with
⟨c|r p^W_0|v⟩ = 0 but A^{(H_W)} ≠ 0. For Si valence (W_𝒲 ≈ 12 eV) the coefficient 2W/ω + W²/ω² is 1.56 at ω_e = 20 eV and 0.25 at 100 eV. These numbers
replace the "flat-band error bound O(1) to 0.25", which is now an absolute statement in units of Σ|r p|. Consequence (i) of CW4 §19 (exact iff flat) and the
ordering result (ii) are unchanged.
**(c) Missing pitfall (scope 4, LE-115).** (W.5) takes the matrix element of the **bare** ∇_{R_0}V between the many-body states. The static DFPT dvscf is screened
with ε⁻¹(ω = 0), which is the wrong screening for transitions at ω_e = 20–100 eV. Replacement for the *Method/Convergence/Pitfalls* of the CW4 §19 spec:
*Method:* QE scf/nscf → ph.x with the **bare** perturbation only (the ionic dV_bare/du of the displaced site, without the induced Hartree+xc part) → Wannier90
valence MLWFs (k 16³, same U(k) gauge) → ⟨c|∂_{R_0}V_bare|v⟩ screened by the RPA+LFE response at ω_e. This is the same screening as for the (p, ω_e) lines, so
A^{DFPT} = Σ_G(ε⁻¹)_{0G}(q, ω_e)-weighted bare vertex. It is compared with (19.1)–(19.2) side by side. The static dvscf vertex is kept only as a labelled
variant, and the difference is reported as a screening nuisance kept apart from 𝔯_W. *Convergence:* the acoustic sum rule Σ_κ∂_{R_κ}V^{scf} = −Σ∇V_KS to 10⁻³.
This holds for the *static* self-consistent response only and validates the gauge and the k mesh, not the dynamical screening. The δM sum rule (WP3 J3)
holds as before. *Pitfalls:* as in CW4 §19, and in addition: a static-dvscf ratio mixes screening and non-rigidity in 𝔯_W. The bound (E.1) is absolute.
Replacement OC-6 and CW4-d: §B.

### A4. VER-CW4 V7, §6 item 3: impact on 2401.11971 (LE-114, CW4 §18)
**Stands with correction.** I read 2401.11971 [FT] (v2, pp.1–2): it is a cosmic-ray-boosted DM paper ("we consider the cosmic ray boosted DM (CRDM)"), and Eq. (5)
evaluates F_DM at "q² = −(ω² − Q²)". (18.1) is exact for the density row. The bound [(1 − v²_χ,max)², 1] needs only ω ≤ v_χQ. That inequality follows from the
convexity of E(p) and holds for relativistic DM (CW4-K11(iii)). The bound is vacuous for v_χ → 1: (1 − 0.99²)² = 4×10⁻⁴. The transverse row (up to ~8 %,
B1 §12) is not part of R_URF. Replacement for the last sentence of the CW4 §18 "Exact ratio" paragraph: "Since ω ≤ v_χQ, for SRDM (v_χ ≲ 0.1) the change is
≤ 2 %. For the source's CRDM flux (v_χ → 1) the bound is vacuous, and **the impact on 2401.11971's limits is UNRESOLVED** until the recast specified below is run.
The transverse row is a separate addition." The CW4 §18 closure-table status changes from "exact ratio + bound" to "exact density-row ratio + bound;
impact UNRESOLVED (recast specified)". K11 was a tautology (VER-CW4 V7). It is replaced by a derivation of (1 − ω²/Q²) from the contraction of two conserved
currents in the density row (J·j = ρJ⁰(1 − ω²/Q²)), its Coulombic m_V → 0 limit, and the kinematic bound (§D). Replacement OC-7: §B.

### A5. VER-CW4 V8, §6 item 5: Kanamori–Tachiki (CW4 §20)
Replacement for the last sentence of the CW4 §20 "Citation" paragraph: "Kanamori and Tachiki (1962) are cited there (Ref. 47, at App. Eq. (A11)) for the first
term of the **resonance shift**, not for the Larmor statement and not for linewidth theory. They should not be cited for Larmor [FT per VER-CW4 V8]." OC-8 is
unaffected. The symbolic closure of (20.1), S(u − v)² = S√((A − B)/(A + B)), is now CW4-K8 (sympy). VER-CW4 could check it only numerically.

### A6. VER-CW4 V10, V18: Δ_D in CW4 §6
CW4 §6 (ii) and K10 used Δ_D = 11.75 meV, the value whose provenance §10 itself withdraws. Replacement: "for ZrTe₅ (Δ_D = 11.8 meV [FT 1910.02091 p.12,
DFT-NR], v_F = 1.3×10⁻³ along x, isotropised ε_bg = 25.3, α̃ = 0.44) Ry_D ≈ 0.145 meV [E; isotropic: an anisotropic mass needs the (v_F,i, ε_bg,ii)
average]". The number is unchanged at three digits (0.1452 vs 0.1447 meV, CW4-K10). K10 now also checks Ry_D against the independent hydrogenic 1/(2μa²).

### A7. VER-CW4 V11, §6 item 6: ZrTe₅ provenance (CW4 §10, OC-11)
Read here [FT 1603.05351 Table I, p.10 of the PDF]: the Fermi velocities are given **per plane**: b-c 1.94, a-c 4.89, a-b 4.03 (×10⁵ m/s). In units of c these
are 6.47×10⁻⁴, 1.631×10⁻³ and 1.344×10⁻³. They reproduce the 1910.02091 Table 1 "Exp. [52]" entries v_F,y = 6.5×10⁻⁴, v_F,z = 1.6×10⁻³ and v_F,x = 1.3×10⁻³
to the printed digits (CW4-K14). The numbers are [FT]. The axis assignment (x ↔ a-b, y ↔ b-c, z ↔ a-c) is 1910.02091's reading [E, source's], not [52]'s.
[52] calls ZrTe₅ an "ideal platform to study 3D massless Dirac and Weyl fermions" (abstract, p.1), which is consistent with it giving no gap. Addendum to CW4 §10: "The 'Exp. [52]'
velocities are genuine [52] Table I values (plane-resolved, axis assignment by 1910.02091); only Δ = 11.75 meV lacks provenance." 1910.02091 Table 1 (re-read
here [FT]) is as quoted in CW4 §10. Replacement OC-11: §B (it also retargets the table, A8).

### A8. VER-CW4 V12, §6 items 4 and 6: Al tag; table targets (CW4 §11, IF-CW4-2, OC-11)
**Tag.** In CW4 §11 and IF-CW4-2, "0.18 meV [D from FT T_c]" becomes "**0.18 meV [E]** (weak-coupling BCS ratio 1.764k_BT_c with the [FT] T_c = 1.2 K of
2305.06084; the ratio is a model, not a derived Al property)". 2109.04473 p.2 (read here [FT]): "∆ is half of the superconducting gap" and "For aluminum (Al), with
∆ = 0.3 meV". So the WP8-U 0.3 meV is that paper's half-gap, ≈ 1.7× the bulk value (finding CONFIRMED).
**Targets (refinement of VER-CW4; see §C R2).** VER-CW4 named R14 WP8-U-table-v2.csv. A parallel R16 return (CW7, returns/R16/WP8-U-v2.md) publishes
WP8-U-table-v3.csv, which "replaces" v2 (the 2997 v2 rows verbatim + 314 new rows). Rows 1543 (ZrTe₅ Delta_D), 1619 (Al Delta_BCS, 0.3 meV, FT 2109.04473)
and 2395 (Nb Delta_BCS_E, 1.63 meV = 1.764k_B × 10.72 K, JARVIS DFT T_c) are identical in v2 and v3 (CW4-K14). v3 adds rows **3194** (Al `flag_Delta_BCS`:
"1.764 k_B T_c ~ 0.18 meV … [UNVERIFIED]") and **3195** (ZrTe₅ `Delta_D_definition`: "IF-U5 closed: Delta_D = 11.75 meV is the half-gap"), which also need the
correction. OC-11 is therefore written for **whichever table is authoritative at merge (v3 if CW7 is accepted, else v2)**, with the add-don't-overwrite rule of
VER-CW4 V12 applied to Al as well as Nb.

### A9. VER-CW4 V13: IF-CW4-1 wording
"WP4-K34's Re ε^{nor} = k_TF²/q² is 16 % high at the edge" becomes "WP4-K34's Re ε^{nor} = k_TF²/q² is **19 % above** the edge value 0.839k_TF²/q²
(Re 𝔣_Lin(0.39) = 0.839, CW4-K2)". Replacement IF-CW4-1: §B.

### A10. VER-CW4 V15, §6 item 8: validity of the local-gap form (2.1) (LE-98, CW4 §2)
Replacement for the sentence "where the second form holds … Anderson theorem …" of CW4 §2:
"Define ℓ_Δ as the length over which the BdG gap Δ(r) varies. The second form is the local-density (adiabatic) approximation for the gap. It holds for
**ξ_coh ≪ ℓ_Δ**: each pair sees a locally uniform gap, P_Δ(Δ) is the volume distribution of the local gap from BdG, and the case-I factor is applied locally.
Here L^{nor}_Δ(q,ω) is the configuration-averaged normal-state loss of the cell regions whose local gap is Δ, normalised so that ∫dΔ P_Δ L^{nor}_Δ = ⟨L^{nor}⟩_conf
(the first form at T > T_c). If the normal loss and the local gap are uncorrelated, L^{nor}_Δ = ⟨L^{nor}⟩ and the form reduces to ⟨𝔤_I(ω/Δ)⟩_{P_Δ}⟨L^{nor}⟩. In the
opposite limit **ξ_coh ≫ ℓ_Δ** the gap self-averages, P_Δ → δ(Δ − Δ̄), and (2.1) reduces to 𝔤_I(ω/Δ̄)⟨L^{nor}⟩ (Anderson theorem: for ℓ_mfp ≪ ξ_coh, disorder does
not change the case-I form, WP4 §4.5). Between the limits neither form is controlled. The BdG output (the correlation function of Δ(r)) gives ℓ_Δ, which
decides the case. The 𝔤_I factor is the first-order [4.2′] form. Near the kinematic edge it must be replaced, locally, by the resummed CW4 (8.1)
(see CW4 §8 for why [4.2′] fails there)." In (2.1), L^{nor}_loc is renamed L^{nor}_Δ with this definition. The rest of §2, including the spec, stands.

### A11. VER-CW4 V16, scope 4 LE-99: two-magnon pitfalls (CW4 §3)
Append to the CW4 §3 *Pitfalls*: "(a) **Identical-boson pair counting:** for ν = ν′ the labels (k, q − k) and (q − k, k) are one state. Either sum over
unordered pairs with the normalised basis, or keep the ordered sum with a factor ½ in 𝒢₂ and a symmetrised 𝒜^{2m}. Otherwise the free two-magnon weight is
doubled: ‖Σ_kA_k a†_k a†_{q−k}|0⟩‖² = 2Σ_k|A_k|² for symmetric A (CW4-K17). (b) The Dyson–Maleev vertex is non-Hermitian. In the linear solve of (3.1) use the
Hermitian HP quartic vertex, or a biorthogonal DM treatment. On-shell agreement does not make the off-shell ladder Hermitian." LE-99 otherwise stands.

### A12. VER-CW4 scope 4 LE-102, V18, §6 item 9: k-resolution, threshold, method (CW4 §6) (thin spec → complete)
The k-grids of CW4 §6 cannot resolve the bound series. For ZrTe₅, a_D = 2v_F²ε_bg/(αΔ_D) ≈ 2.0×10³ Å (1/a_D ≈ 5×10⁻⁴ Å⁻¹, CW4-K10, isotropised). The
"60³ inside Λ_D" grid has Δk = 2Λ_x/60 = 7.7×10⁻³ Å⁻¹ (Δk·a_D ≈ 15), and an ab initio 24³ BZ mesh has Δk ≈ 1.9×10⁻² Å⁻¹ (Δk·a_D ≈ 37). Both are coarser
than the 1s exciton itself. **Replacement for the "Missing step" and "Specification" of CW4 §6:**
**Exact remaining gap (all missing steps).** (1) Band parameters (v_F,i, Δ_D, ε_bg,ii, Λ_i) with uncertainties from ab initio. (2) The threshold region
|√𝓈 − 2Δ_D| ≲ 10 Ry_D from the analytic anisotropic Elliott–Sommerfeld solution. (3) The ladder (BSE) away from threshold on the k·p model. (4) An estimate of
the beyond-ladder terms (self-energy + vertex) at α̃ ~ 1. **No controlled method exists for step (4).** Neither GW+BSE nor functional RG is controlled at
α̃ ~ 1, so step (4) is a nuisance estimate and not a computation that closes the row.
**Specification (GW/BSE appendix).** *What:* L(q,ω) of the anisotropic massive-Dirac model of ZrTe₅ for |q| ≤ Λ_D and 2Δ_D ≤ √𝓈 ≤ 2Δ_D + 50 meV, plus the
bound-state energies and weights. *Approximation:* 𝒳 = static-screened ladder (BSE) on G₀W₀-corrected k·p bands. W = Coulomb/(ε_bg,ij + Dirac RPA
polarisation), with remote bands only in ε_bg (no double counting). The ladder is the controlled O(α̃) rung and is uncontrolled beyond it. *Method:* (1) QE + Yambo
**G₀W₀** with SOC (12-atom cell, k 12×12×4 BZ mesh plus a non-uniform refinement near Γ), used **only** to fit the k·p parameters and ε_bg,ii. Ab initio BSE is not used
for the threshold, because it cannot resolve a_D. (2) Threshold: analytic Elliott–Sommerfeld for the anisotropic non-relativistic pair (reduced masses
μ_i = Δ_D/(2v²_F,i), ε_ii), with the anisotropic hydrogen problem solved variationally or on a radial grid. This gives the Rydberg series and 𝒮_F^D. (3) Away from
threshold: BSE on the model on a **log-graded radial k grid** from k_min ≤ 0.1/a_D (5×10⁻⁵ Å⁻¹) to Λ_D (≈ 200 radial × 590 Lebedev directions). The analytic
and BSE results are matched on 5–10 Ry_D. (4) Beyond ladder: the evGW–G₀W₀ spread of v_F,i and Δ_D propagated through (2)–(3), reported as a type-M nuisance.
*Convergence:* Ry_D and the first three bound-state energies to 5 % under k_min → k_min/2 and doubled radial points. The continuum 𝒮_F^D to 2 % across the
matching window. The f-sum of the model to 10⁻³. *Pitfalls:* the cutoff scheme (WP4 §5.4 (i)). Double counting of ε_bg if remote bands are also in the GW W. The ionic
ε_bg(ω) near polar phonons: use ε₀ (with the ionic part) when Ry_D ≪ ω_LO, as here (0.15 meV against meV-scale optical phonons), and ε_∞ in the opposite
limit (state which). A uniform grid in Λ_D gives a spurious "no bound state" result. The isotropised ε_bg used in (6.1) differs from the anisotropic Rydberg [E].
*Cost:* model and analytic stages CPU-minutes. G₀W₀ 10⁴ CPU-h (GPU fork).

### A13. VER-CW4 V20: strong-coupling clause of (12.1) (LE-108, CW4 §12)
**The N_sN_s′ + P_sP_s′ part stands as [D, sketch].** In the BCS limit, N_sN_s′(1 + Δ²/EE′) = N_sN_s′ + P_sP_s′ = (EE′ + Δ²)/√((E² − Δ²)(E′² − Δ²)), which is
the case-I integrand of K1d (CW4-K16). **The clause "plus the mass renormalisation 1/(1 + λ_tr) in the current eigenvalues" is WITHDRAWN.** It was asserted,
not derived. In the normal-state limit the Allen form with the bare current and α²F_tr has no such factor at one-phonon order. Replacement for the CW4 §12
"Strong coupling" sentence: "Replacing the BCS spinors by Eliashberg spectral functions, the pair weight becomes ∫dE[N_s(E)N_s(E′) + P_s(E)P_s(E′)] [D, sketch].
Exact remaining gap, all steps: (i) write σ₁ by Kubo with Eliashberg Nambu Green functions and the bare current vertex (Migdal: vertex corrections
O(ω_D/E_F)); (ii) isolate the one-phonon-emission (Holstein) term at ω > 2Δ + ω_ph; (iii) show that its pair weight is N_sN_s′ + P_sP_s′ with E, E′ the
quasiparticle energies on the real axis; (iv) determine which renormalisation factors Z(E) survive in the current eigenvalues. Step (iv) decides whether any
λ-dependent factor appears. No factor is asserted." The CW4 §12 spec stands. OC-1's appended "strong coupling: N_sN_s′ + P_sP_s′ ([D, sketch])" does not
mention λ_tr, so it is unchanged in substance (OC-1 is re-issued only for A1).

### A14. VER-CW4 V21, §6 item 8: valley–orbit momenta (LE-109, CW4 §13)
Replacement for "intervalley (g, f) terms at q ≈ |k_ι − k_ι′| ≈ 2–3 keV" in CW4 §13 [D, CW4-K15; a = 5.431 Å, 2π/a = 2.283 keV, k₀ = 0.85·2π/a = 1.94 keV]:
"intervalley terms sit at q = k_ι − k_ι′ + G. **g-process** (opposite valleys): 2k₀ = 3.88 keV, or 0.685 keV after umklapp (|2k₀ − 4π/a| = 0.3·2π/a), next 3.60 keV.
**f-process** (perpendicular valleys): √2k₀ = 2.74 keV, and **2.33 keV** with G = (2π/a)(1, −1, ±1) (|q|² = 1.045(2π/a)²). All of these are reachable by MeV DM,
and the 𝒰_{ι′ι}(G) of (13.1) fix their relative weights." The original "2–3 keV" is right for f and wrong for g. VER-CW4's f value omits the umklapp term (§C R1).

### A15. VER-CW4 V23: CT form factor at q = 0 (LE-112, CW4 §16)
Append after (16.1): "For orthogonalised orbitals f_C(0) = ⟨C|N_e|0⟩ = 0 (charge conservation), as the difference form e^{iq·r_𝔬} − e^{iq·r_𝔬′} implies. CT lines
therefore enter S at O(q²d²_𝔬𝔬′) for qd_𝔬𝔬′ ≪ 1."

### A16. VER-CW4 V24, §6 item 8: tube kernel (CW4 §17)
"RPA with the tube Coulomb kernel (uniform cylinder of radius R_tube …)" becomes "(**cylindrical charge shell** of radius R_tube, HL units)". The kernel
V_1D = 2αI₀(qR_tube)K₀(qR_tube) is the ring average of the 1D transform 2K₀ of the Coulomb potential (Graf addition theorem, CW4-K3b). Same change in the
CW4-c row (§B).

### A17. VER-CW4 V28, §6 item 8: closure counts (CW4 §0)
Replacement for the "Counts:" line of CW4 §0: "Counts (21 rows): **CLOSED 16** (LE-97, 98, 100, 101, 103–106, 108–114, 116), of which **4 carry an exact-gap
remainder** (LE-97 magnitude, LE-104 O(Δ²/q²v_F²) + KK tail, LE-109 impurity band, LE-110 depolarisation size). **CLOSED-AS-EXACT-GAP 4** (LE-99, 102, 115,
117). **Split 1** (LE-107: Nb CLOSED, Al CLOSED-AS-EXACT-GAP). CANNOT-CLOSE 1 part (the Allen equation numbers of LE-108)." These counts are parsed from the
table (CW4-K18). Per A4, LE-114's status reads "CLOSED (exact density-row ratio + bound; CRDM impact UNRESOLVED, recast specified)". It is still CLOSED as a
compute-formulate row, because the recast is specified.

---
## B. Re-issued owed corrections, interface flags and LIMITS rows (merger: use this section only)

| OC | Status in errata |
|---|---|
| 1 | **re-issued** (A1) |
| 2, 3, 4 | unchanged (CW4 text) |
| 5 | **re-issued** (A2) |
| 6 | **re-issued** (A3) |
| 7 | **re-issued** (A4) |
| 8, 9, 10 | unchanged (CW4 text) |
| 11 | **re-issued** (A7, A8) |
| 12 | unchanged (CW4 text) |

- **OC-1.** **LIMITS LB1-10, Status cell** → "DERIVED, REFEREED; (A2.2) **[D]** by explicit Nambu second order (R16 CW4 §12: [j(q=0), H_BCS] = 0, amplitude
   −ê·(v_{k+Q} − v_k)g(u′v + v′u)/ω, case I); result = Allen (1971) as cited by 1604.06800 Ref. [29] (Allen not read; closed access; no equation numbers)".
   Leading-correction cell: append "strong coupling: N_sN_s′ + P_sP_s′ (CW4 §12, [D, sketch]; renormalisation factors open, CW4-errata A13)".
- **OC-5.** **LIMITS LB1-6, Leading-correction cell** → "OPW orthogonalisation (C 2p_z model, [E], CW4 §17 + CW4-errata A2): |M_OPW|²/|M_PW|² = 0.4–4.3 at 50–100 eV and
   0.7 to ~5×10² at 10 eV over q = 5–40 keV, q- and direction-dependent (large values only where |M_PW|² is suppressed, q ≫ k_f); sign of the rate-weighted
   factor not fixed without all occupied orbitals (spec CW4-errata A2); FSI factor between 1 and the unscreened Sommerfeld 2.6–7.3 (100–10 eV) [E];
   semiconducting CNT: 1D massive-Dirac RPA CW4 (17.1) with the cylindrical-shell kernel 2αI₀K₀".
- **OC-6.** **LIMITS LB1-8, Status cell** → "**[D]** under (H_W) with **ket-side ordering**: A^{(H_W)} = (m_eq/M_κ)Σ_{v′∈𝒲}[(ε_c − ε_v′)²/ω²_cv]r_cv′(p^W_0)_{v′v} exactly
   (CW4 (19.2)); |A^{(H_W)} − (m_eq/M_κ)⟨c|r p^W_0|v⟩| ≤ (m_eq/M_κ)(2W_𝒲/ω_cv + W²_𝒲/ω²_cv)Σ_{v′}|r_cv′(p^W_0)_{v′v}| (absolute; no relative bound on the sum,
   CW4-errata (E.1)); ket-side ordering fixed by the acoustic sum rule (the symmetrised ordering gives half the boost and is rejected); phase −i relative to the
   boost; non-rigid ratio 𝔯_W = exact gap G-X6, specified with the bare vertex screened at ω_e (CW4 §19 + CW4-errata A3)".
- **OC-7.** **LIMITS LB1-13, Status cell** → keep "**impact on its limits UNRESOLVED**" and append: "density-row ratio R_URF/R_src = ⟨(1 − ω²/Q²)²⟩_src ∈
   [(1 − v²_χ,max)², 1] exactly (CW4 (18.1)); ≤ 2 % for v_χ ≲ 0.1; for the source's CRDM flux (v_χ → 1) the bound is vacuous; transverse row (B1 §12) not
   included; recast specified (CW4 §18)".
- **OC-11.** **WP8-U table (v3 if CW7 is accepted, else R14 v2; rows identical, CW4-K14).**
   (a) **ZrTe5 Delta_D row (l.1543), note** → "half-gap per 1910.02091 Eq. (1.1) and p.12 (gap 23.6 meV ↔ Δ = 11.8 meV); 'Exp. [52]' = 1603.05351, which
   reports no gap (massless-Dirac SdH paper) [attribution UNVERIFIED]; its Table I v_F (plane-resolved, 4.03/1.94/4.89 ×10⁵ m/s) are the 'Exp.' velocities;
   use 11.8 (DFT, NR)". **v3 only, l.3195 `Delta_D_definition`, note** → replace "Delta_D = 11.75 meV is the half-gap" by "the Table 1 Δ column is the half-gap;
   documented value 11.8 meV (DFT, NR); 11.75 meV attributed to [52] but not found there (CW4 §10)".
   (b) **Al:** keep l.1619 (0.3 meV, FT 2109.04473) and change its note to "source working value: 2109.04473 p.2 '∆ is half of the superconducting gap',
   ∆ = 0.3 meV; ≈ 1.7× bulk (film-like)". **Add** a row `Al,Al,superconductor,SURVIVOR-COND,Delta_BCS_bulk_E,0.18,meV,E,arXiv:2305.06084,p.1-2 (T_c = 1.2 K),
   "1.764 k_B T_c (weak-coupling BCS); film 30 nm: 0.209 meV (0706.4150 Table 1); primary bulk tunnelling value not located (CW4 §11)"`. **v3 only, l.3194
   `flag_Delta_BCS`** → tag E (not [UNVERIFIED]), source "arXiv:2305.06084 T_c; CW4 §11".
   (c) **Nb:** keep l.2395 (`Delta_BCS_E` 1.63 meV, DFT T_c). **Add** a row `Nb,Nb,superconductor,SURVIVOR-COND,Delta_BCS_FT,1.50-1.61,meV,FT,arXiv:1805.06359,
   p.3,"secondary (review-level) quote, orientation-dependent; 2Δ/k_BT_c = 3.74-4.04 with T_c 9.25-9.3 K (p.5)"`.

**Interface flags.** IF-CW4-1 and IF-CW4-2 are re-issued. IF-CW4-3 to IF-CW4-8 are unchanged.
- **IF-CW4-1** (WP4 / WP5 / WP6, L^{BCS} at the edge) → "use (8.1) and the §8 table instead of [4.2′] + 'exclude y ≲ 3.5'; type-Δ nuisance from the KK-∞/cut
  spread; WP4-K34's Re ε^{nor} = k_TF²/q² is 19 % above the edge value 0.839k_TF²/q²".
- **IF-CW4-2** (WP8-U, coordinator, Al Δ_BCS) → "table value 0.3 meV (2109.04473, the source's half-gap) is ≈ 1.7× bulk; use 0.18 meV **[E]** (1.764k_BT_c, FT
  T_c 1.2 K) for bulk Al (WP4 already uses 0.17 meV); Nb 1.50–1.61 meV [FT 1805.06359 p.3, secondary]; table rows per OC-11 (v3/v2)".

**Proposed LIMITS rows.** CW4-b, CW4-c, CW4-d and CW4-g are re-issued. CW4-a, CW4-e and CW4-f are unchanged in substance, but their sources 2609.06423 (CW4-a) and
2504.02927 (CW4-f) are not in CW4's literature list, so their "Source [FT]" cells read **[FT per VER-CW4]** (VER-CW4 read them).
| # | Owner | Location | Source [FT] | Chain | Status | Leading correction; caveats |
|---|---|---|---|---|---|---|
| CW4-b | CW4 / WP7-B1 | §12 (12.1) | 1604.06800 Eqs. (16)–(17) (Allen 1971 via its Ref. [29]) | (3.5), sector (2,1), q_φ = 0, mean-field BCS, T-even g | DERIVED | Eliashberg N_sN_s′ + P_sP_s′ [D, sketch], renormalisation factors open (errata A13); GRPA dressing O(Δ²/(v_FQ)²) |
| CW4-c | CW4 / WP7-B1 | §17 (17.1) | — | 1D massive Dirac, RPA with the cylindrical-shell kernel 2αI₀K₀ | DERIVED (K3, K3b) | excitons (BSE); inter-subband via F_⊥ |
| CW4-d | CW4 / WP7-B1 | §19 (19.1)–(19.2) | 1912.13484 Eqs. (2.7)–(2.8) [FT per VER-CW4] | (W.5) T0, one-body local h, occupied-manifold MLWF projector on the ket side | DERIVED; DFPT ratio = gap | **absolute** bound (2W_𝒲/ω_cv + W²_𝒲/ω²_cv)Σ\|r p\| (errata (E.1)); nonlocal V_NL commutator; bare vertex screened at ω_e, not static dvscf |
| CW4-g | CW4 / WP7-B1 | §14 (14.1)–(14.2) | 2208.05967 Eqs. (6), (10), (12); 1509.01598 Eqs. (3.9), (3.13), (3.17) | WP0 (9.2) per cell | DERIVED (K6); **source Eq. (6) wrong by μ_eχ/(4E_r) with Eq. (10), dimensionally inconsistent with Eq. (12) (CONFIRMED, VER-CW4)** | Fig. 4 numerics not re-run (QEdark origin [E]) |

---
## C. Rebuttals and refinements of VER-CW4

**R1 (VER-CW4 V21 / §3, f-process momentum): partial rebuttal.** VER-CW4 gives "f-process at √2k₀ = 2.7 keV" and calls CW4's "≈ 2–3 keV" wrong only for g.
In the G-sum of (13.1) the f-process also appears with umklapp. In exact rationals (units 2π/a, k₀ = 17/20): k_ι − k_ι′ = (17/20, −17/20, 0). With
G = (1, −1, 1), q = (−3/20, 3/20, −1), so |q|² = 9/400 + 9/400 + 1 = 209/200 = 1.045 and |q| = 1.0223·2π/a = **2.33 keV** < √2k₀ = 2.74 keV (sympy, CW4-K15).
G = (1, −1, ±1) is in the fcc reciprocal lattice (all odd). The lowest f-type transfer is therefore 2.33 keV. The verifier's g values (3.88 and 0.685 keV) are
reproduced exactly: (2k₀, 0, 0) − (2, 0, 0) = (−3/10, 0, 0). The CW4 statement stays corrected for g as in A14. For f, both 2.33 and 2.74 keV lie in the
original "2–3 keV".
**R2 (VER-CW4 V11, V12 / §6 item 6, target file): refinement.** The verifier retargets OC-11 to R14 v2. It did not read the other R16 returns, so it could not
see that CW7 issues WP8-U-table-v3.csv as v2's replacement, with two further affected rows (3194, 3195). Row 3195 restates the unsupported 11.75 meV as the
half-gap. A correction against v2 alone would leave v3 wrong. OC-11 (§B) covers both versions (row identity checked, CW4-K14).
**No other verifier claim is contested.** I re-derived and accept: V5's numbers (reproduced to ≤ 3 %, CW4-K4); V6's absolute bound (CW4-K7c, including a
counterexample to any relative bound); V7's vacuity (CW4-K11); V12's tag; LE-102's a_D (1.96×10³ Å, CW4-K10); V13's 19 %; V28's counts (CW4-K18). Scope 2
row "1910.02091 typo in (3.13)–(3.14), not re-checked": re-read here [FT 1910.02091 v2]. Eq. (3.14) prints the denominator term with "v_F,z" against q_x²κ_xx, so
the typo is confirmed in (3.14). In the text extract the (3.13) 00 entry is not legible, so it is left as R8 recorded it.

---
## D. Changes to code/CW4/checks.py (24 checks, ≈ 1.5 s)
| Label | Change | Why / correction checked |
|---|---|---|
| K1a | **replaced**: the commutator [v·τ⁰, h] (scalar × identity, trivially zero) → Fock-space [v(n₁ − n₂), H_BCS] = 0 with Jordan–Wigner operators, plus the control [n₁ + n₂, H_BCS] ≠ 0 and Ψ†τ⁰Ψ = n₁ − n₂ + 1 | circular check removed (V1) |
| K1c, K1d | 6 sample points at 10⁻¹³; algebraic-weight quadrature, 10⁻¹⁰ (was 10⁻⁶) | tighten |
| K2 | adds a sympy derivation of (8.1) from Im ε/\|ε\|² and its first-order reduction to [4.2′]; the whole §8 table to ±0.006 (was "in (0,1)"); Re 𝔣_Lin = 0.839, 𝔯 = 0.730, 1/0.839 = 1.191 | tighten; V13 / A9 |
| K3b | **new**: ring average ⟨K₀(q\|R − R′\|)⟩ = I₀K₀ (10⁻⁸) | V24 / A16 |
| K4 | full 3 × 5 × 3-direction grid, deterministic 2×10⁴ directions; must match VER-CW4 V5 (8 %) and the A2 table; Sommerfeld 7.33/3.41/2.57 (was "finite and > 0") | V5 / A2 |
| K5 | the §13 table to ±0.01 (was 0.4 < a < 2) | tighten |
| K6 | **replaced** the typed-in dimensions with a dimension table applied to (14.1), (14.2), Eq. (6)+(10), Eq. (6)+(12); adds a sympy angular δ-integral of 1509.01598 (3.9) giving 1/(qv); depolarisation criterion as an exact polynomial identity (was 2000 random samples); μ/(4E_r) = 4.05×10⁴ | circular check removed (V2) |
| K7c | **new**: absolute bound (E.1) on 500 random site projectors; cancellation counterexample to a relative bound | V6 / A3 |
| K8 | adds the sympy closure (u − v)⁴ = (A − B)/(A + B) | V8 |
| K9 | adds ×1600/×6.3 and ×640/×5.0 | (9.1) numbers |
| K10 | Ry_D/Δ_D = 0.052 to 10⁻³ against the independent 1/(2μa²); ZrTe₅ with Δ_D = 11.8 meV; a_D and Δk·a_D for both spec grids (was 0 < Ry < 0.1) | V10, V18, LE-102 / A6, A12 |
| K11 | **replaced** (was a tautology): conserved-current contraction → (1 − ω²/Q²); m_V → 0 Coulombic; ω ≤ v_χQ on 10⁵ relativistic samples; vacuity at v_χ → 1 | V7 / A4 |
| K13 | J_F = 5.6×10⁻⁵ eV to 2 % (was J < 10⁻³) | tighten |
| K14 | **replaced** (was 23.6/2 = 11.8): finds the CSV rows by content in v2/v3 (pre-merge l.1543, 1619, 2395; v3 l.3194/3195), so it survives the OC-11 row insertions; [52] v_F → units of c vs the 1910.02091 "Exp." row; Al and Nb numbers | V11, V12 / A7, A8 |
| K15 | **new**: Si g/f momenta with umklapp, exact rationals | V21 / A14, R1 |
| K16 | **new**: N_sN_s′ + P_sP_s′ = BCS case-I integrand | V20 / A13 |
| K17 | **new**: identical-boson pair counting (Fock space, 4 modes) | V16 / A11 |
| K18 | **new**: closure counts parsed from CW4 §0 | V28 / A17 |
K3, K7, K7b, K12 are unchanged. Run: `cd code/CW4 && python3 checks.py` → "24/24 PASS".

---
## E. Closing table (verifier item → resolution → location)
| VER-CW4 item | Resolution | Location |
|---|---|---|
| V1 OC-1/2, LB1-10 | stands; Allen attribution "via 1604.06800 Ref. [29]"; K1a de-circularised | A1; §B OC-1, CW4-b; K1a |
| V2 OC-3, LB1-5 | stands; K6 made non-circular | OC-3 unchanged; K6 |
| V3 depolarisation, Ref. [139] | stands (already "metadata level") | OC-3 unchanged |
| V4 LB1-11 | stands; K5 tightened | OC-4 unchanged; K5 |
| V5 OPW numbers (FALLS) | re-derived on the full grid; replacement text + table + spec; FSI and (17.1) stand | A2; §B OC-5; K4 |
| V6 = V25 LB1-8 | "ket-side ordering"; absolute bound (E.1); Si numbers restated | A3; §B OC-6, CW4-d; K7c |
| V7 LB1-13 | impact on CRDM limits UNRESOLVED kept; K11 replaced | A4; §B OC-7; K11 |
| V8 B2-L6 | stands; Kanamori–Tachiki = resonance shift; (20.1) closed in sympy | A5; OC-8 unchanged; K8 |
| V9 B2-L7 | stands | OC-9 unchanged |
| V10 L16 | stands; §6 Δ_D → 11.8 meV | A6; OC-10 unchanged; K9, K10 |
| V11 ZrTe₅ | v_F provenance added (FT here); retargeted to v3/v2 incl. l.3195 | A7, A8; §B OC-11(a); K14 |
| V12 Al/Nb | Al tag [E]; add-don't-overwrite rows for Al and Nb; v3 l.3194 | A8; §B OC-11(b,c), IF-CW4-2; K14 |
| V13 OC-12 / IF-CW4-1 | stands; "19 % above" | A9; OC-12 unchanged; §B IF-CW4-1; K2 |
| V14 (1.1) | stands | — |
| V15 (2.1) | both limits stated; L^{nor}_Δ defined; (8.1) locally | A10 |
| V16 (3.1) | pair-counting and DM-vertex pitfalls added | A11; K17 |
| V17 (5.1) | stands | — |
| V18 (6.1) | formula stands; ZrTe₅ value [E], Δ_D = 11.8 | A6, A12; K10 |
| V19 (7.1) | stands ([UNVERIFIED] citation kept) | — |
| V20 (12.1) strong coupling | N_sN_s′ + P_sP_s′ kept [D, sketch]; 1/(1 + λ_tr) **withdrawn**; all missing steps listed | A13; §B CW4-b; K16 |
| V21 (13.1) | g momenta corrected; f umklapp 2.33 keV added | A14; §C R1; K15 |
| V22 (15.1) | stands; K13 tightened to 5.6×10⁻⁵ | K13 |
| V23 (16.1) | f_C(0) = 0 note added | A15 |
| V24 (17.1) | "cylindrical charge shell" | A16; §B CW4-c, OC-5; K3b |
| V26, V27 | stand (= V8, V9) | — |
| V28 counts | 16 CLOSED (4 with remainders), 4 EG, 1 split | A17; K18 |
| Scope 2 (all rows) | confirmations accepted; 1910.02091 (3.14) typo now [FT] here | §C |
| Scope 4 LE-99 | pitfalls added | A11 |
| Scope 4 LE-102 (thin spec) | spec completed: all missing steps, analytic threshold, log grid, G₀W₀ only for parameters, uncontrolled at α̃ ~ 1 | A12; K10 |
| Scope 4 LE-107 | tag [E] | A8 |
| Scope 4 LE-115 | bare-vertex/ω_e screening pitfall; ASR scope stated | A3(c); §B OC-6, CW4-d |
| Scope 4 LE-117, remainders | stand | — |
| Scope 5 CW4-a, e, f | stand | §B (unchanged) |
| Scope 5 CW4-b, d, g | re-issued | §B |
| §6 items 1–9 | 1 → A2; 2 → A3; 3 → A4; 4 → A8; 5 → A5; 6 → A7/A8; 7 → A1; 8 → A10, A14, A16, A17; 9 → A11, A12, A3(c) | A, B |
