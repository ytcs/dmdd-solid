# R16 / ERR-CW2: errata to returns/R16/CW2.md (applies referees/R16/VER-CW2.md)

Brief: campaign/paer/briefs/R16/ERR-CW2.md. Read: returns/R16/CW2.md, referees/R16/VER-CW2.md, CONVENTIONS.md, NOTATION.md (rows for 𝓃_e, 𝓃^{(κ)}_G; no 𝓃̂, ρ^{nuc}, R^{nuc} rows exist),
returns/R12/WP7-B2-v2.md (§2.3 definition of C^{IR}, §7(b)–(c) giant moments and κ_URF), code/CW2/ (checks.py, atomic_contact.py, ld1/results.json).
Literature (lit.py → literature/papers-ERR-CW2/, HTML kept, PDFs deleted): 1406.1074 [FT] (TRPMD; short-time order of RPMD), 2011.14986 [FT] (TD-SCHA). Nothing else fetched.
New [CALC]: code/CW2/atomic_contact_errata.py (QE 7.6 ld1.x, all-electron atoms, rel = 0/1/2 × xmin = −7/−8, < 1 min single core) → code/CW2/ld1/results-errata.json.
Checks: code/CW2/checks.py revised, **32/32 PASS in ≈ 13 s** (one core, OMP_NUM_THREADS=1). CW2.md is not edited: read it together with this file. Nothing committed.
**Merger rule.** For each owed correction, interface flag and LIMITS row listed in §2, use the text given here. Where it says "unchanged", use CW2.md. Equations amended here carry a prime: (CW2.12′), (CW2.20′), (CW2.23′), (CW2.27′).

---
## 1. Corrections, one block per verifier row that is not plain STANDS

### E-1. OC-2, status LE-68, CW2 §21 (2308.06314 Fig. 2 rigid-ion factor): STANDS WITH CORRECTION, applied
The verifier's numbers are reproduced (CW2-C14). The rigid-ion vertex is v^{rig}_κ = Z_κ − Q_κ/ε_∞ with Q_Ga = +3, Q_As = −3. The rate factor (d_rig/d)² is **6.8** with the LST value Z* = 2.160 and **8.6** with Z* = 2.1.
Replace in §21 "its electron-scalar rate is high by ≈ 1/0.11 ≈ 9 and its g_e reach optimistic by ≈ 3" with "its electron-scalar rate is high by **≈ 7–9** (6.8 at the LST Z* = 2.16, 8.6 at Z* = 2.1),
and its g_e reach is optimistic by **≈ 2.6–2.9**. This is an order-of-magnitude statement (§20 near-cancellation)". The §20 pitfall "rigid-ion Q_j changes d by 3×" becomes "by 2.6× (LST Z*) to 2.9× (Z* = 2.1)". The status (RESOLVED) and the caveat on later commits stand.

### E-2. OC-3, CW2 §9 table (L shell): STANDS WITH CORRECTION, applied
(a) The §9 AE values are **NR** (rel = 0). (b) "Above ≈ 100 keV the hydrogenic 1s² form is accurate to < 1%" holds for 𝔯, not for 𝔯 − 1. At 300 keV (Si) 𝔯 differs by −0.58% but 𝔯 − 1 by −1.21%; at 102 keV both are ≤ 0.1% (CW2-C27).
(c) The relativistic change of 𝔯 − 1 is −6…−7% (Si) and −28…−33% (Ge/Ga/As) when 𝔯 is normalised to the point-nucleus density at r_min (CW2-C27). That change is almost entirely in the denominator 𝓃_e(R_κ), not in Δ𝓃_κ(q). The physical, finite-nucleus value is −6…−7% (Si) and −23…−30% (Ge/Ga/As) [E]. See E-6, E-7 and Rebuttal R-1. Re-issued text: §2, OC-3.

### E-3. OC-4, LE-64 (CW2.20): polarisation weights — STANDS WITH CORRECTION, applied
WP7-B2-v2 §2.3 defines C^{IR}(ω) ≡ ⟨|p_ν|²⟩_{ω_ν=ω}, a conditional average over the modes at fixed ω. At fixed ω, branch ν holds a fraction ∝ ω²/c_ν³ of the modes. Hence

  C^{IR}(ω) = Σ_ν ŵ_ν 𝒮^{(ν)}_Z(ω/c_ν)/M̄,   ŵ_ν = c_ν⁻³/Σ_{ν′}c_{ν′}⁻³   (1L + 2T: ŵ_L = c_L⁻³/(c_L⁻³ + 2c_T⁻³), ŵ_T = c_T⁻³/(c_L⁻³ + 2c_T⁻³) each),
  A^{IR} = Σ_ν ŵ_ν 𝒮^{(ν)}_Z(0⁺)/M̄,   B^{IR} = Σ_ν ŵ_ν 𝒮^{(ν)″}_Z(0)/(2M̄c_ν²),                                                                         (CW2.20′)

with 𝒮^{(ν)}_Z(k) ≡ N⁻¹⟨|Σ_I ε̂·Z*_I·ê_ν e^{ik·x_I}|²⟩ averaged over k̂ (and over ε̂ for an isotropic glass). The 1/3 from the ε̂ average sits inside 𝒮^{(ν)}_Z. It is not a branch weight.
"ŵ^{pol}_ν the polarisation weights (1/3 each for an isotropic glass)" is withdrawn. For an isotropic scalar charge field the 𝒮^{(ν)}_Z(0⁺) do not depend on ν and Σŵ_ν = 1, so A^{IR} is unchanged. B^{IR} changes: with c_L = 2c_T the 1/3 form is low by 21% (CW2-C25).
CW2-C25 is a 96³ plane-wave Monte Carlo with a locally neutral dipolar charge field. The conditional mode average equals the ensemble value to 0.4%, and the k² law equals the c⁻³-weighted (CW2.20′) to 0.4%.
CW2-C11 is a single-branch 1D test and cannot see the weights.
**Leading correction (previously unstated).** Below the Ioffe–Regel frequency the modes are plane waves only up to Rayleigh scattering, with linewidth ∝ ω⁴. The relative correction to (CW2.20′) is O(Γ_R(ω)/ω) ∝ ω³ [E]. Boson-peak (non-plane-wave) modes come at higher ω.
The spec of §17 is unchanged, plus one item: the c_ν come from the same configurations (elastic constants or the k → 0 slope of the Hessian dispersion), and ŵ_ν is computed from them.

### E-4. OC-6, LE-52, LE-70 (Markov–Krein band in the tails): STANDS WITH CORRECTION, applied
The tail behaviour, exactly: ϱ(ξ) ≃ (𝔨₄ + 2𝔨₂² − 𝔨₃²/𝔨₂)/(ξ − 𝔨₁)⁴ for |ξ − 𝔨₁| → ∞. For a Gaussian this is 2𝔨₂²/(ξ − 𝔨₁)⁴, and ϱ = 2/3 at the mean (sympy, CW2-C22).
Beyond the outer canonical nodes the band is [0, ϱ(ξ)]. It is an absolute power-law upper bound with no lower bound. For a Gaussian at 𝔨₁ − 4σ the band is [0, 7.7×10⁻³] against the true F = 3.2×10⁻⁵ (CW2-C22).
- In §5, replace "The band is wide at the peak (ϱ = 2/3 at the mean of a Gaussian) and narrow in the tails (ϱ ~ 𝔨₂²/(ξ − 𝔨₁)⁴), the threshold region that sets low-mass reach" with:
  "The band is absolute in the CDF. It is wide at the peak (ϱ = 2/3 at the mean of a Gaussian) and narrow in absolute terms in the tails, ϱ ≃ (𝔨₄ + 2𝔨₂² − 𝔨₃²/𝔨₂)/(ξ − 𝔨₁)⁴. There it is only an upper bound, a power law, while true threshold tails fall like Gaussians or exponentials.
  It is therefore not a relative bound on tail rates, gives no lower bound on them, and does not by itself set low-mass reach."
- In §23, replace the last clause "the band is wide at the peak, so it bounds threshold-limited (tail) rates, not line shapes" with "the band is wide at the peak and is an absolute upper bound in the tails. It bounds bin-integrated rates in the bulk of S to ±ϱ in the CDF.
  It bounds threshold-tail rates from above only, with no relative accuracy, and does not bound line shapes."
- The remainder inequality |F_exact − F_SCHA| ≤ |F_SCHA − F_canon| + ϱ stands (triangle inequality).

### E-5. LE-51 (§4): label of the core part, ecutrho, missing steps — STANDS WITH CORRECTION, applied (and Rebuttal R-3)
(a) **Label.** Core negligibility is [D] for a hydrogenic core (CW2-C3) times an [E] residual field (≈ 10⁻² a.u. per unit displacement in Si). For real cores it is **[E]**, not [D].
(b) **ecutrho.** |G|_max = 1.5 × 20 keV = 30 keV = 8.05 a₀⁻¹ ⇒ ecutrho ≥ **65 Ry** (CW2-C24; the "≈ 260 Ry" corresponds to 60 keV). This is the q-range requirement. The actual ecutrho is the larger of it and what the PAW dataset needs (≥ 4–8 × ecutwfc).
(c) **Added pitfall.** The PAW all-electron density reconstructed on the FFT grid (pp.x plot_num = 21) aliases the core-region components onto the grid. Fourier components above ≈ 10 keV must therefore be taken as smooth-part FFT plus one-centre (augmentation-sphere) radial transforms per atom, not from the gridded AE density.
(d) **Core polarisation is not covered by the AE spec** (Rebuttal R-3). Added sub-spec:
  - Computed: Δ^{core}_κ(q) = E^{res}_κ·χ^{core}_κ(q). Here χ^{core}_κ(q) is the ℓ = 1 Fourier transform of the core first-order density per unit uniform field, and E^{res}_κ = Φ^{on}_κu/(Z_κe) is the residual field at the nucleus per displacement [E for this identification].
  - Method: Dalgarno–Lewis/Sternheimer radial equations on the ld1.x AE core orbitals (1s–2p for Si; up to 3d for Ge/Ga/As), minutes of CPU time. Alternatively LAPW with every shell as a band state (local orbitals for 1s–3d).
  - Convergence: radial grid as in §9, and the ℓ = 1 sum rule ∫χ^{core}·r d³r = core dipole polarisability.
  - Pitfall: a frozen-core PAW or spherical-core LAPW run gives Δ^{core} ≡ 0 by construction.
**Missing steps (all):** (1) the magnitude of Δ^{val} for 3 ≲ |q| ≲ 20 keV (spec §4 with (b), (c)); (2) the core-polarisation magnitude for real cores (sub-spec (d)). Status: CLOSED-AS-EXACT-GAP (unchanged).

### E-6. LE-54 (§7) and VER §0: r_min bias and relativistic scoping — STANDS WITH CORRECTION, applied
(i) **r_min bias [CALC].** The "𝓃_e(0)" of §7 is n(r_min), r_min = e^{xmin}/Z. The NR Kato cusp n(r) ≈ n(0)(1 − 2Zr) puts it low by 2Zr_min = 2e⁻⁷ = **1.82×10⁻³** for every species.
  Changing xmin from −7 to −8 moves n(r_min) by exactly the cusp (to 0.2%), and n(0) = n(r_min)(1 + 2Zr_min) then agrees between the two grids to 3×10⁻⁶ (CW2-C23).
  - NR values: **𝓃_e(0) = 1769.5 (Si), 22499.0 (Ge), 20415.5 (Ga), 24720.6 (As) a₀⁻³**.
  - Hence (CW2.13): **E^{Mig}_3/E_R = 1501 (Si), 16867 (Ge), 15445 (Ga), 18527 (As) eV²** (NR, PBE, point nucleus).
  - The quoted controls "N_el to 10⁻⁵, dx 3×10⁻⁸" are not the accuracy of 𝓃_e(0), because the dx test keeps xmin fixed. 𝔨₃^X/𝔨₃^{GS} = 7.7×10⁵ is unchanged at this precision.
(ii) **Relativistic densities [CALC + E].** The scalar-relativistic and Dirac point-nucleus densities diverge as r^{2(γ−1)}, with fitted log slopes 2(γ−1) to < 1% (Ge −0.0553; CW2-C23). Their values at r_min are therefore grid-dependent.
  Ge (Dirac) is +49.7% above NR n(0) at xmin = −7 and +58.3% at xmin = −8. The "+7.8% (Si), +49% (Ge), +46% (Ga), +53% (As)" of §7 are withdrawn as atomic properties.
  The physical quantity is ∫𝓃_e ρ^{nuc}_κ (see (iii)). Estimated by the Dirac density at the uniform-sphere radius R^{nuc} = √(5/3) r_rms (r_rms = 0.836A^{1/3} + 0.570 fm [UNVERIFIED parametrisation]) and the sphere average of the point profile [E], it is:

| | Si | Ge | Ga | As |
|---|---|---|---|---|
| ∫𝓃_eρ^{nuc} / 𝓃_e^{NR}(0) [E] | 1.077–1.081 | 1.40–1.43 | 1.37–1.40 | 1.43–1.45 |
| E^{Mig}_3/E_R, relativistic finite nucleus [E] (eV²) | ≈ 1620 | ≈ 2.36–2.40×10⁴ | ≈ 2.12–2.16×10⁴ | ≈ 2.64–2.69×10⁴ |

  So the NR coefficients are **low by ≈ 8% (Si) and ≈ 37–45% (Ge/Ga/As) [E]**; the verifier's "≈ 40–50%" is refined by the Dirac runs. Dirac versus scalar-relativistic at the same r adds +0.15–0.4%, the p_{1/2} contact contribution [CALC].
(iii) **Scope of what is owed (verifier §0(ii) accepted).** 𝔨₃ comes from the nuclear double commutator with H = Σ_κP_κ²/2M_κ + H_el(R). With Dirac–Coulomb electrons, H_el depends on R only through V_eN, because the kinetic term cα·p + βm is R-independent. So (5.2′) and (CW2.13) keep their form.
  For a finite nucleus, ∇²_R V_eN = Ze²ρ^{nuc}(r − R) (HL), hence Ze²𝓃_e(R)/3 → Ze²∫d³r 𝓃_e(r)ρ^{nuc}_κ(r − R)/3. What is owed is a relativistic finite-nucleus density averaged over ρ^{nuc}_κ, not a new derivation. Breit (magnetic e–N) terms are a smaller correction [E].
  §7 "Relativistic flag" is replaced by (ii)–(iii). IF-CW2-2 is re-issued in §2.

### E-7. LE-56 (§9): "single missing step" — STANDS WITH CORRECTION, applied (scoping in Rebuttal R-1)
**Missing steps (all), for every species:**
1. Crystal valence anisotropy (T_d, ℓ = 3): ≤ 1.3×10⁻³ in 𝔯 (Si) [E] (as in CW2).
2. **Relativistic finite-nucleus contact density** ∫𝓃_eρ^{nuc} in the normalisation 𝓃_e(R_κ): +8% (Si), +37–45% (Ge/Ga/As) [E] (E-6). This is the LE-54 missing step and is shared with it.
3. **Relativistic change of Δ𝓃_κ(q) itself:** +0.4…1.5% (Si) and +2.0…5.7% (Ge/Ga/As) over 10–300 keV [CALC, Dirac point nucleus] (CW2-C23).
   This value is independent of xmin to 10⁻⁵ and of the nuclear model to < 10⁻⁴: the r < R^{nuc} part of 6∫𝓃 j₂(qρ)dρ/ρ is 𝓃q²R²/5 (sympy), ≤ 3×10⁻⁵ of Δ𝓃 at 300 keV. Step 3 is therefore effectively done.
4. Breit/QED corrections to the density: smaller [E].
The physical 𝔯 − 1 = (𝔯 − 1)_{NR}(1 + δ_Δ)/(1 + δ_n) is lower than the NR table by 6–7% (Si) and 23–30% (Ge/Ga/As) [E], with the larger reduction at low q.
**Spec level** (replaces "GS density, PBE, AE"): AE, PBE. Δ𝓃_κ(q) from a Dirac (or scalar-relativistic) point-nucleus atom plus the crystal valence part. 𝓃_e(R_κ) as ∫𝓃_eρ^{nuc}_κ from a finite-nucleus Dirac atomic calculation, for **all** species (Si +8% included).
  - Method for step 2: a finite-nucleus Dirac–Kohn–Sham or Dirac–Hartree–Fock atom (e.g. GRASP2018 or DIRAC [UNVERIFIED tool names as to options], or ld1.x patched with a uniform-sphere V_eN), with a Fermi or uniform ρ^{nuc} of measured r_rms.
  - Convergence: r_min ≤ R^{nuc}/100; nuclear model (Fermi vs uniform) < 1% [E]; functional (PBE vs PZ, as §7: ≤ 0.9%).
  - Pitfalls: point-nucleus relativistic densities at r_min are grid artefacts. The p_{1/2} contribution must be kept (Dirac). Never apply the relativistic change of the ratio 𝔯 − 1 on top of an NR 𝓃_e(R_κ) (R-1).
  - Cost: minutes per atom.
Status: CLOSED-AS-EXACT-GAP. The exact remaining gap is steps 1 and 2 (step 3 is done).

### E-8. LE-53 (CW2.12): exactness claim false — STANDS WITH CORRECTION, applied (with an exact replacement)
The parenthetical "(CW2.12) is exact when B_IJ is uniaxial about r̂_IJ, which the configurational average at fixed r enforces for the averaged moments …" is **withdrawn**. The verifier's counterexample is reproduced: B = diag(B_T, B_T, B_L) + ε(x̂ẑ + ẑx̂) gives an excess **4ε²/15** at qr = 0 (sympy, CW2-C21). The excess survives the average over rotations about r̂.
**Exact replacement.** Decompose the symmetric part of B_IJ about r̂ = r̂_IJ:
- B_L = r̂·B·r̂;
- b = P_⊥B r̂ (longitudinal–transverse vector);
- B_T = ½ tr(P_⊥BP_⊥);
- τ = P_⊥BP_⊥ − B_TP_⊥, with |τ|² ≡ ½ tr τ²;
- μ = q̂·r̂, Δ ≡ B_L − B_T, A₀ ≡ B_T + Δμ².
The average over the azimuth of q̂ about r̂ is then exact:

  ⟨(q̂·B·q̂)²⟩_φ = A₀² + 2μ²(1 − μ²)|b|² + ½(1 − μ²)²|τ|²,
  ⟨(q̂·B·q̂)³⟩_φ = A₀³ + 3A₀[2μ²(1 − μ²)|b|² + ½(1 − μ²)²|τ|²] + 3μ²(1 − μ²)² b·τ·b,                                                                  (CW2.12′a)

and only even powers of μ occur. Replacing μ^{2k} → (−1)^k j₀^{(2k)}(qr) (CW2-C18) gives, for n = 2,

  𝔚^{(2)}_dist(q) = (𝓃_at c²e^{−2W}q⁴/2)∫4πr²dr g₂(r){⟨B_T²⟩j₀ − 2⟨ΔB_T⟩j₀^{(2)} + ⟨Δ²⟩j₀^{(4)} − 2⟨|b|²⟩[j₀^{(2)} + j₀^{(4)}] + ½⟨|τ|²⟩[j₀ + 2j₀^{(2)} + j₀^{(4)}]}(qr),     (CW2.12′b)

with ⟨·⟩ = ⟨·⟩_r (configurational, pairs at distance r). The n = 3 form follows from (CW2.12′a) in the same way: products of ⟨A₀ |b|²⟩_r, ⟨A₀|τ|²⟩_r and ⟨b·τ·b⟩_r enter. (CW2.12) is the special case b = 0, τ = 0.
CW2-C21 checks (CW2.12′a) symbolically and against a direct q̂ average of e^{−iq·r}(q̂·B·q̂)^n for random B and r̂ (n = 2, 3, qr = 1.7–11) to 3×10⁻¹³. The spec of §6 is unchanged; it bins ⟨|b|²⟩_r, ⟨|τ|²⟩_r, ⟨b·τ·b⟩_r and their products with A₀ next to ⟨Δ^kB_T^{n−k}⟩_r. The direct pair sums are exact and remain the reference.

### E-9. LE-66 (§19, (CW2.23)): frequency shift and convergence — STANDS WITH CORRECTION, applied
**Statement corrected (verifier §6 minor).** Thermal frequency shifts between 293 K and T → 0 (|s| ≲ 1% [E]) and the narrowing of anharmonic widths can make α(ω; 0) exceed α(ω; 293 K) pointwise near a sharp two-phonon feature. CW2-C13 shows an isolated 25 + 25 meV overtone moved out of a 0.2 meV bin. What holds for every bin [ω₁, ω₂] is

  ∫_{ω₁}^{ω₂} α(ω; T → 0)dω ≤ ∫_{ω₁/(1+|s|) − Γ_293}^{ω₂(1+|s|) + Γ_293} α(ω; 293 K)dω,                                                                  (CW2.23′)

with T-independent second-order dipoles. Each T = 0 sum line has a 293 K partner of weight 1 + n₁ + n₂ ≥ 1 inside the widened bin, and difference lines only add. Γ_293 is the 293 K anharmonic width. CW2-C13 checks it on a 120-mode model spectrum.
Consequence: Γ_iso/Γ_EM (mK, 50 meV) ≥ 6.3×10³ holds to the extent that the 293 K curve is flat over 50 meV × (1 ± 1%) ± Γ_293. Otherwise the bound reads 6.3×10³ × α_293(50 meV)/max over that window [E].
**Missing steps (all):** (1) the T = 0 two-phonon ε₂(ω) (or cold data), the GAP; (2) the 293 K → 0 K frequency shift and width change, needed for any pointwise use; (3) the [E] on D(50 meV) in Γ_iso (B2.4.2).
**Spec, convergence block (added).**
- Supercells: 2×2×2 conventional (64 atoms) and 3×3×3 (216), testing the range of ∂Z*/∂u. Accept when ε₂ changes < 10% in 40–60 meV. T_d symmetry needs one atom and one direction.
- Displacements u = ±0.005, ±0.01, ±0.02 Å. Central differences; linearity of ∂Z*/∂u to < 2% (Z*_Si = 0 at u = 0, so the first order is linear in u).
- DFPT inside: ecutwfc 80 Ry; k-mesh 4³ (64 atoms) and 2³ (216 atoms) with a 6³ / 3³ check; epsil; tr2_ph 10⁻¹⁶.
- Two-phonon sum: 32³ vs 48³ Q-mesh; Gaussian δ with σ = 0.25, 0.5, 1 meV extrapolated to 0, or tetrahedra.
- **Validation:** α(ω, 293 K) with the 293 K sum + difference weights (and quasi-harmonic 293 K frequencies) must reproduce the measured 293 K curve (Deinzer–Strauch [FT via VER-WP7-B2-A]) to ≤ 20% in 40–60 meV before the T = 0 curve is used.
- Cost [E, ∝ N_at³]: 64 atoms, 6 runs × ≈ 20 CPU·h ≈ 1.2×10² CPU·h; 216 atoms, 2 runs × ≈ 10³ CPU·h ≈ 2×10³ CPU·h.
Status: CLOSED-AS-EXACT-GAP (unchanged).

### E-10. LE-67 (§20): one Z* throughout — STANDS WITH CORRECTION, applied
C14 now uses the LST value it computes (CW2-C14). **Z* = 2.160:**
- d = **−1.33×10⁻³**;
- +10% in Z*/ε_∞ → **+41%** in d;
- +0.01 u in M_Ga → **+4.8%**;
- a 20% rate needs **δ(Z*/ε_∞) ≤ 4.8×10⁻³ (2.4%)** and **δM_Ga ≤ 0.021 u**.
With Z* = 2.1 the values are d = −1.18×10⁻³, +45%, +5.4% and 2.2%. The two Z* inputs differ by 27% in rate, beyond the 20% target. This reinforces §20's conclusion: Z*/ε_∞ must come from measured low-T ω_L, ω_T, ε_∞ through (CW2.24), not from DFPT.

### E-11. LE-72 (§25): κ_URF algebra and giant-moment spec — STANDS WITH CORRECTION (κ_URF half), applied; giant-moment half: spec supplied
**(a) (CW2.27) corrected.** For non-terminal λ, with competing channels:

  𝒩_χ = (𝟙 − M)⁻¹b,   M_{λλ′} = [Σ_{λ″}(1 + δ_{λ′λ″})Γ^{u}_{λ→{λ′λ″}} + Γ^{iso}_{λ→λ′}]/Γ^{all}_λ,   Γ^{all}_λ = Γ^{3ph}_λ + Γ^{iso}_λ + Γ^{loss}_λ.                                   (CW2.27′)

- Γ^{u}_{λ→{λ′λ″}} is the three-phonon rate into the **unordered** pair, and Γ^{3ph}_λ = Σ_{λ′≤λ″}Γ^u.
- Γ^{iso} is elastic isotope (Tamura) scattering.
- Γ^{loss} is boundary escape, absorption and sensor capture.
- The terminal chiral-stable set is 𝒞 = {λ: |L^{ph}_λ| > L_th and Γ^{3ph}_λ + Γ^{iso}_λ < 1/t_obs}. For λ ∈ 𝒞, b_λ = 1 and the row M_{λ·} = 0; otherwise b_λ = 0.
- The decay probability the verifier asked for is Γ^{3ph}_λ/Γ^{all}_λ, built into the normalisation. A chiral-stable phonon is counted once and never also through its daughters.
- In an ordered-pair convention (Γ^{ord}_{λ′λ″} symmetric, Γ^{3ph}_λ = ½Σ_{ordered}Γ^{ord}), M_{λλ′} = [Σ_{λ″}Γ^{ord}_{λ→λ′λ″} + Γ^{iso}_{λ→λ′}]/Γ^{all}_λ **without** (1 + δ); the two forms are identical (CW2-C16b).
- The code must state which convention its rates use (Rebuttal R-2).
- "M nilpotent in energy order" holds only without Tamura scattering. With it, M is not nilpotent, and 𝟙 − M is invertible because Γ^{3ph} + Γ^{loss} > 0 on every closed elastic set, giving spectral radius < 1.
- A closed set of non-terminal states with Γ^{3ph} = Γ^{loss} = 0 has no finite count and must be assigned to 𝒞 or to loss through t_obs.
- CW2-C16b checks this by Monte Carlo of the binary branching process with Tamura and loss: the exact value 1.0215 is matched by MC 1.0304 ± 0.0064. In the same model, a G3ph-only-normalised ordered (1 + δ) reading gives 2.04: an O(1) error in this toy model, not a general factor.
- Spec additions: inputs Γ^{loss}_λ (geometry, sensor coverage) and t_obs. Convergence is unchanged (grid, fc3 cutoff, smearing), plus the sensitivity to t_obs.
**(b) Giant-moment (4f orbit–lattice) amplitudes: derivation and spec (replaces the one-line pointer).**
- *Derivation [D]* (adiabatic in the crystal-field manifold, first order in u). Let H_CF(u) act on the 4f ground multiplet (or the full spin–orbit manifold) and let P_g(u) project on the ground Kramers doublet. The DM-coupled spin and orbital rows (WP7-B2-v2 §7(b)) see O_eff(u) = P_g(u) O P_g(u), with O ∈ {s_e, L}. Then

  𝒜^{O}_{Qν} ≡ ⟨1_{Qν}|O_eff|0⟩ = Σ_{κα} [∂_{u_{κα}}(P_gOP_g)] e_{κν,α}(Q)/√(2NM_κω_{Qν}),   ∂P_g = R ∂H_CF P_g + P_g ∂H_CF R,   R = Σ_{c∉g}|c⟩⟨c|/(E_g − E_c).   (CW2.28)

  The formula is gauge-invariant within the degenerate doublet (no eigenvector derivatives). CW2-C26 checks it against finite differences for J = 15/2 with random time-reversal-even crystal fields.
  The non-adiabatic correction is O(ω_{Qν}/Δ_CF). For ω ≈ Δ_CF the resonant form ⟨c, 0|∂H_CF·u|g, 1⟩/(E_c − E_g − ω) replaces (CW2.28).
- *Spec.*
  - Computed: ∂B^q_k/∂u (k = 2, 4, 6; 27 Stevens parameters) and ∂g/∂u per symmetry-adapted displacement of the cluster atoms, then 𝒜^{s_e}, 𝒜^{L} by (CW2.28) with the phonon eigenvectors of the host (fc2 stage of (a)).
  - Level: adiabatic CF manifold, first order in u. CASSCF(n_f, 7), state-averaged over all roots of the ground term (Dy³⁺: 21 sextets; +224 quartets for the J-mixing test). Spin–orbit by RASSI-SO. CF splittings corrected by NEVPT2/CASPT2. DKH2 scalar relativity. ANO-RCC-VTZP on Ln, VDZP on the first shell, VDZ beyond.
  - Method: OpenMolcas (or ORCA) [UNVERIFIED as to version]; embedded cluster (Ln + first coordination sphere + whole bonded ligands) in Ewald point charges, with ab initio model potentials on boundary cations. SINGLE_ANISO extraction of B^q_k and g. Central differences ±0.01 Å.
  - Convergence:
    - displacement 0.005/0.01/0.02 Å, linearity < 2%;
    - active space 4f → 4f + 5d or + ligand σ orbitals (RAS), ∂B^q_k change < 10%;
    - SA roots sextets-only vs all;
    - cluster first vs second coordination shell;
    - embedding point charges vs AIMP;
    - basis VDZP → VTZP.
  - Cost [E]: 0.5–2 CPU·h per geometry × 6N_cl (N_cl ≈ 30–60) ≈ 10²–10³ CPU·h per inequivalent site.
  - Pitfalls:
    - derivatives of individual doublet eigenvectors are gauge artefacts; use projectors (CW2.28);
    - roots can flip under displacement, so track them by overlap;
    - CASSCF alone misplaces Δ_CF by tens of percent [E], and Δ_CF enters R;
    - s_e ≠ (g_J − 1)J once J-mixing matters, so use the full SO states;
    - the DM couples to s_e with λ_S, and to L only in the orbital rows: keep 𝒜^{s_e} and 𝒜^{L} separate.
- *Exact remaining gap:* the ab initio values of ∂B^q_k/∂u for a chosen 4f host, and hence 𝒜^{O}_{Qν}.
**Status.** LE-72: CLOSED-AS-EXACT-GAP (both halves). The verifier's CANNOT-CLOSE for the giant-moment half was conditional on a spec, which is now supplied.

### E-12. LE-52 (§5): convergence block (spec thin) — STANDS WITH CORRECTION, applied
Added to the §5 Spec:
- **Systems and cells.** KTaO₃, SrTiO₃: n×n×n cubic cells, n = 4, 6, 8 (320, 1080, 2560 atoms), even n for the R-point soft mode. LiH: 4³–6³ conventional (512–1728 atoms). Accept when F_s(q,t) changes < 2% for t ≤ t_max and the finite-size gap 2πc/L lies below the lowest ω bin of interest. (Solid He: §23.)
- **Beads.** P with βω_max/P ≲ 0.3. For SrTiO₃ at 50 K (ω_max ≈ 100 meV) P ≈ 80; P doubled until 𝓂₂ (static) changes < 1%. PIGLET/GLE may be used for the static moments (CW2.10) but **not** in the dynamics: it alters the dynamics.
- **Thermostat (TRPMD).** Langevin friction on the internal ring-polymer modes only, γ_k = λω_k, with λ = ½ (optimal damping) and checks at λ = ¼, 1 [FT 1406.1074: internal-mode thermostat preserves RPMD's exact limits]. Centroid not thermostatted during the dynamics. Initial conditions from an NVT PIMD run.
- **Time step.** Δt ≤ 0.1/ω_P of the stiffest free ring-polymer mode (typically 0.1–0.25 fs for P ≈ 80 at 50 K); centroid energy drift < 10⁻⁴ per ps.
- **Length.** t_max ≥ 20π/δω (δω = 0.5 meV ⇒ ≈ 80 ps) at q ≲ q_BZ; shorter at large q where F_s decays (impulse regime). ≥ 100 independent initial conditions, giving < 1% statistical error on bin integrals.
- **Cross-checks.** TRPMD vs CMD (adiabatic CMD, Δt reduced 3×): their difference is the method nuisance. Both must lie inside the moment band (CW2.11) built from the exact PIMD moments. Violations are flagged (CW2.10 test).
- **SSCHA ladder.** Static SCHA (free-energy Hessian), then the dynamical ansatz 𝒢⁻¹(ω) = 𝒢⁽⁰⁾⁻¹ − Π(ω) at bubble level (D⁽⁴⁾ = 0), then full TD-SCHA (D⁽⁴⁾ included). The bubble–full difference is the order test [FT 2011.14986].
- **Cost [E].** MLIP 10⁻⁴–10⁻³ CPU·s per atom·bead·step: 1080 atoms × 80 beads × 4×10⁵ steps ≈ 10³–10⁴ CPU·h per (material, T); CMD ≈ 3×; SSCHA/TD-SCHA ≈ 10² CPU·h with the same MLIP.
- **Added pitfalls.**
  - RPMD's short-time error is O(t³) for non-linear operators such as e^{iq·u}, against O(t⁷) for the position autocorrelation [FT 1406.1074]. Beyond 𝓂₂ even the short-time moments are not guaranteed, so the (CW2.10) test is mandatory.
  - TD-SCHA "can excite only up to two phonons simultaneously" [FT 2011.14986]. Multiphonon S(q,ω) at q ≫ q_BZ is then available only by inserting the TD-SCHA one-phonon 𝒢 into the Gaussian form (dressed W₂, §12), which misses W₃ and W₄.
  - TRPMD/CMD give Kubo-transformed correlations. S = [βω/(1 − e^{−βω})]S̃ amplifies errors by βω, so these methods are usable only at T ≳ ω/10 [E] and **not at the 10 mK target**.
**Missing steps (all):** (1) real-time quantum dynamics of the anharmonic lattice for the pointwise S (as in CW2); (2) a T → 0 method for the non-linear operator e^{iq·u} beyond two phonons. Kubo-based methods fail at mK, and TD-SCHA is limited to two phonons. Until then the mK S is bounded by the band (CW2.11) only.
Status: CLOSED-AS-EXACT-GAP (unchanged).

### E-13. OC-10 / LE-49 "0.16 [E] superseded": STANDS WITH CORRECTION, applied
In §2, "the [E] 0.16 is superseded by ℛ₂ (§1)" becomes "the [E] 0.16 stands until ℛ₂ (CW2.4) is computed for the crystal. Only the 1D illustration ℛ₂ = −0.34 exists". Re-issued as OC-10 in §2.

### E-14. VER §6 minor items
- **§9 notation collision.** In (CW2.16) the Fourier coefficient is renamed **𝓃̂_G ≡ Ω⁻¹∫_Ω d³r e^{−iG·r}n_e(r)**, so that n_e(r) = Σ_G 𝓃̂_G e^{iG·r}. In the CONVENTIONS §2 sign this is n_e(q = −G)/Ω, and 𝓃̂_0 = 𝓃_e is the mean density.
  (CW2.16) reads Δ𝓃_κ(q) = 3Σ_G 𝓃̂_G e^{iG·R_κ}[(q̂·(q − G)^)² − 1/3]. The "uniform term 2𝓃_e" is 2𝓃̂_0 = 2𝓃_e (mean), 2𝓃̂_0/𝓃_e(R_κ) = 1.2×10⁻⁴ (Si). 𝓃_e(R_κ) keeps its NOTATION meaning (contact density).
  The NOTATION row is requested in §2. There is no collision: no 𝓃̂ row exists, and 𝓃^{(κ)}_G (conditional density) is a different object.
- **§19 quasi-harmonic shift.** Applied as E-9.
- **§16 HTML equation number.** Irrelevant. No change.

---
## 2. Re-issued owed corrections, interface flags and LIMITS rows (merger uses only this section where it says "replace")

1. **OC-1 (LIMITS L7c)**: unchanged.
2. **OC-2, LIMITS B2-L1, last column**, replace "2308.06314 Fig. 2 projection **UNRESOLVED**" → "2308.06314 Fig. 2 uses the rigid-ion vertex (N_Ga,e = 28, N_As,e = 36; Q_j = ±3 in Π_ϕA), no δZ
   (RESOLVED, R16 CW2 §21 with CW2-errata E-1: Eqs. (40)–(41); PhonoDark-abs 0cbb3d5 pda/couplings.py l.32–43, pda/selfenergy.py l.183). Its GaAs electron-scalar rate is high by ≈ 7–9
   ((d_rig/d)² = 6.8 at the LST Z* = 2.16, 8.6 at Z* = 2.1), and its g_e reach is optimistic by ≈ 2.6–2.9; order of magnitude (near-cancellation)".
3. **OC-3, state/CORRECTIONS.md, WP2-v3 §5.2″ (Core part)**, replace "The L shell roughly doubles the O(q²) coefficient [E] (its 8 electrons at ≈ 4× the radius), so the hydrogenic numbers are
   a lower bound on the deviation." → "All-electron atomic densities (NR, PBE; R16 CW2 §9, CW2-errata E-2, E-7, [CALC]):
   - 𝔯 − 1 = 0.59, 4.21, 9.98, 28.7, 92.0% (Si) at 10, 30, 51.1, 102, 300 keV.
   - The L shell raises the O(q²) coefficient by ≈ 1.6× and is negligible above ≈ 100 keV. There hydrogenic 1s² gives 𝔯 to < 1% (−0.6% at 300 keV; 𝔯 − 1 to −1.2%), which is not a bound.
   - Relativity changes Δ𝓃_κ(q) by +0.4–1.5% (Si) and +2–6% (Ge/Ga/As) [CALC, Dirac], and 𝓃_e(R_κ) by +8% (Si) and +37–45% (Ge/Ga/As) [E, finite nucleus]. The physical 𝔯 − 1 is therefore lower than NR by ≈ 6–7% (Si) and ≈ 23–30% (Ge/Ga/As) [E].
   - Correct 𝓃_e(R_κ) and Δ𝓃_κ separately."
   Same section, §12 item 8 → "spherical part [CALC, NR, CW2 §9]; crystal valence anisotropy and the relativistic finite-nucleus 𝓃_e(R_κ) open (CW2-errata E-7)".
4. **OC-4, LIMITS B2-L3, last column**, replace "A^{IR}, B^{IR} not computed (gap 1)" → "A^{IR} = Σ_νŵ_ν𝒮^{(ν)}_Z(0⁺)/M̄, B^{IR} = Σ_νŵ_ν𝒮^{(ν)″}_Z(0)/(2M̄c_ν²), ŵ_ν = c_ν⁻³/Σ_{ν′}c_{ν′}⁻³
   (mode fraction at fixed ω; the 1/3 field-polarisation average is inside 𝒮^{(ν)}_Z), from static configurations (R16 CW2 (CW2.20′), CW2-errata E-3). Valid below the Ioffe–Regel frequency (plane-wave modes); leading correction Rayleigh
   scattering, relative O(ω³) [E]. Values need the glass Z* charge model (spec CW2 §17). S_dist at n_ph ≥ 2: (CW2.12′) (CW2-errata E-8)".
5. **OC-5 (LIMITS B2-L4)**: unchanged.
6. **OC-6, LIMITS B2-L5, last column**, replace "no remainder bound beyond the Gaussian near melting (δ_Lind ≈ 0.3)" → "remainder bounded in the CDF by the Markov–Krein band of the exact static
   moments (R16 CW2 (CW2.10)–(CW2.11), CW2-errata E-4). The band is absolute: ϱ = 2/3 (Gaussian) at the peak, and in the tails an upper bound only, ϱ ≃ (𝔨₄ + 2𝔨₂² − 𝔨₃²/𝔨₂)/(ξ − 𝔨₁)⁴.
   It is no relative bound on threshold-tail rates; PIMD moments specified".
7. **OC-7, LIMITS "Numbers carried", isotope bullet** (re-issued because (CW2.23) is amended), append: "At mK Γ_iso/Γ_EM ≥ 6.3×10³ at 50 meV (derived: bin-integrated α(T→0) ≤ α(293 K) over the bin widened by the
   ≈ 1% thermal frequency shift and the 293 K width, R16 CW2 (CW2.23′), CW2-errata E-9). This holds pointwise to the extent α_293 is flat over 50 meV × (1 ± 1%). O(σ_M/M̄) correction κ^M_1h_iso ≈ +9% at 50 meV [E, Debye]
   (CW2.22); low-T measured α: GAP."
8. **OC-8 (CORRECTIONS WP7-B2-v2 §2.2)**: unchanged.
9. **OC-9 (SOTA, 2603.13052)**: unchanged.
10. **OC-10, state/CORRECTIONS.md, WP2-v3 §12 gaps 1–3, IF-10, IF-13; LIMITS L5 "Leading corrections"**, append: "exact ω-integrated coherent weight (R16 CW2 (CW2.3)–(CW2.4)), certified pointwise band
    (CW2.5)–(CW2.6), T > 0 resummed form (CW2.7) (second-order TDS 1/|q − G|). The ≈ 0.16 [E] stands until ℛ₂ (CW2.4) is computed for the crystal (only a 1D illustration, ℛ₂ = −0.34, exists)".
11. **OC-11 (CORRECTIONS WP3-v3 IF-13 / J3)**: unchanged.
12. **IF-CW2-2 (re-issued)**: Owner WP3, WP0 (J8, (4.7′)), CW1. Quantity: E^{Mig}_3, 𝔨₃^X. This return: closed form (CW2.13), [CALC] NR coefficients at r = 0: 1501 (Si), 16867 (Ge), 15445 (Ga), 18527 (As) eV² × E_R. These are low against the relativistic
    finite-nucleus value by ≈ 8% (Si) and ≈ 37–45% (Ge/Ga/As) [E] (CW2-errata E-6). Action: WP3 quotes (CW2.13) with ⟨𝓃_e⟩_{ρ^{nuc}}. (5.2′) is unchanged for Dirac–Coulomb electrons, so only the relativistic finite-nucleus density is owed (spec E-7).
13. **IF-CW2-9 (re-issued)**: Owner WP2 (L4 add-on), CW1. Quantity: pseudo vs AE densities, and relativity. This return: NC pseudo-densities invalid above q_c ≈ 10 keV (stack B). PAW frozen-core and spherical-core LAPW give no core polarisation (E-5).
    For Z ≳ 30 the contact density needs a relativistic finite nucleus (+37–45%), while Δ𝓃_κ(q) changes by only +2–6% (E-7). Action: every finite-q charge vertex or Δ𝓃 above q_c uses AE, and every 𝓃_e(R_κ) uses ∫𝓃_eρ^{nuc}.
14. **NOTATION rows requested (addition to the CW2 Symbols table):**

| Symbol | Meaning | Where |
|---|---|---|
| 𝓃̂_G | Fourier expansion coefficient of the crystal electron density, Ω⁻¹∫_Ω e^{−iG·r}n_e; 𝓃̂_0 = 𝓃_e | (CW2.16) as renamed, E-14 |
| ρ^{nuc}_κ, R^{nuc}_κ | normalised nuclear charge distribution; its uniform-sphere radius √(5/3)r_rms | E-6 |
| ŵ_ν | branch mode fraction at fixed ω, c_ν⁻³/Σc⁻³ (replaces ŵ^{pol}_ν) | (CW2.20′) |
| b, τ (pair tensors) | longitudinal–transverse vector and traceless transverse part of B_IJ about r̂_IJ | (CW2.12′) |
| Γ^{u}, Γ^{iso}, Γ^{loss}, Γ^{all}, 𝒞, t_obs | unordered-pair 3-phonon, Tamura, loss and total rates; chiral-stable terminal set; observation time | (CW2.27′) |
| P_g, 𝒜^{O}_{Qν}, B^q_k | ground-doublet projector; one-phonon giant-moment amplitude; Stevens CF parameters | (CW2.28) |

15. **Proposed LIMITS rows (re-issued with validity and leading-correction columns; sources not read in full text are marked "classical, not verified")**

| # | τ / chain | Source formula | Validity | Leading correction | Status |
|---|---|---|---|---|---|
| CW2-L1 | J8 with WP2 (5.2′): E^{Mig}_3 = (q²/2M²)[Ze²⟨𝓃_e⟩_{ρ^{nuc}}/3 − ∂²E^ad] (CW2.13) | WP3-v3 J8, WP2-v3 (5.2′) (campaign) | leading BO; cubic site; Dirac–Coulomb electrons, NR nuclei; vibrationally averaged | relativistic finite-nucleus contact density: +8% (Si), +37–45% (Ge/Ga/As) [E] over the NR coefficients; then O(𝔨₁/ΔE₃, ⟨ω_ph⟩/ω_e) (J8) | DERIVED (campaign); [CALC] NR coefficients (E-6) |
| CW2-L2 | T > 0 coherent n_ph = 2 near G, (CW2.8) | second-order thermal diffuse scattering ∝ 1/\|q − G\| (classical, not verified; Warren 1969 [UNVERIFIED]) | T ≫ ω of the soft pair, q → G; c_min bound | regular part, O((T/ω̄)²) relative | DERIVED (campaign) as bound |
| CW2-L3 | single-isotope LDOS (CW2.21) | Lifshitz mass-defect Green function (classical, not verified) | exact for one defect, harmonic | pair terms O((δ^M)²x) | DERIVED (campaign), C12 |
| CW2-L4 | GaAs Z*/ε_∞ from LO–TO (CW2.24) | Lyddane–Sachs–Teller / Born–Huang (classical, not verified) | one TO/LO pair (cubic, two atoms), HL | T-dependence of ε_∞ (2–3% [E]) and of ω_L, ω_T: use low-T data | DERIVED (campaign); inputs [FT] to collect |
| CW2-L5 | moment band (CW2.11) for any S | Markov–Krein (classical, not verified; Akhiezer 1965 [UNVERIFIED]) | exact 𝓂₀–𝓂₄ | absolute CDF bound; tails power law ϱ ≃ (𝔨₄ + 2𝔨₂² − 𝔨₃²/𝔨₂)/(ξ − 𝔨₁)⁴, no relative tail bound | DERIVED (campaign) as applied, C4, C22 |

---
## 3. Rebuttals (verifier claims that are wrong or wrongly scoped; numbers conceded where right)

**R-1. "SR lowers 𝔯 − 1 by ≈ 30% (Ge/Ga/As)" as a second, much larger missing step of LE-56 (VER §0(iii), §4 LE-56, OC-3) — scope rebutted, numbers conceded.**
𝔯 − 1 = Δ𝓃_κ(q)/𝓃_e(R_κ) is a ratio. The [CALC] runs separate the two parts (CW2-C23):
- The numerator Δ𝓃_κ(q) changes Dirac/NR by only +0.4…1.5% (Si) and +2.0…5.7% (Ge/Ga/As). It is xmin-independent to 10⁻⁵ and nucleus-independent to < 10⁻⁴: sympy gives 6∫₀^R 𝓃 j₂(qρ)dρ/ρ = 𝓃q²R²/5, which is 3×10⁻⁵ of Δ𝓃 at 300 keV.
- The rest of the "−30%" is the r_min-dependent point-nucleus 𝓃_e(r_min) in the denominator, i.e. the LE-54 contact-density step (E-6).
The observable is E^{Mig}_3(q) ∝ 𝓃_e(R_κ) + Δ𝓃_κ(q) = 𝓃_e(R_κ)𝔯_κ(q). The relativistic correction therefore lives almost entirely in the q-independent term.
For LE-56 proper (the q-dependence), the relativistic step is a 2–6% effect and is now [CALC]. Applying the "−30%" to 𝔯 − 1 while keeping an NR 𝓃_e(R_κ) would understate Δ𝓃 by ≈ 30%.
The verifier's quoted value is itself at r_min. At the finite-nucleus radius it is −23…−30% (E-7), and the contact excess is +37–45% rather than "+40–50%".

**R-2. LE-72: "Σ_{λ″} must be over unordered pairs" — the double-count risk is conceded, the remedy is not.**
In (CW2.27) λ′ is fixed and λ″ runs over all states. With Γ defined per unordered pair, each pair {λ′, λ″} then appears exactly once, and (1 + δ_{λ′λ″}) counts the two daughters of a {λ′, λ′} decay. That is correct.
A sum "over unordered pairs" at fixed λ′ is not defined. The double count arises only if ordered-pair rates (Γ^{ord}_{aa} = 2Γ^u_{aa}) are combined with (1 + δ); then the form without (1 + δ) is the right one.
CW2-C16b shows the unordered (1 + δ) form and the ordered form without (1 + δ) give identical M and match Monte Carlo. The real defect of (CW2.27) was the missing competition (Γ^{all} normalisation, terminal set), corrected in (CW2.27′).

**R-3. LE-51: "The AE spec covers both" (core and valence) — rebutted.**
In a frozen-core PAW calculation the core density is rigidly attached to its nucleus; a spherical-core LAPW gives the same. Under a displacement u it is n_core(r − u), whose linear term is exactly the subtracted rigid-shift term q f^{core}_κ in Δ_κ ≡ δρ_κ − q f^{at}_κ (CW2.9).
Hence Δ^{core} ≡ 0 by construction in both. The ℓ = 1 core deformation of CW2-C3 (the q⁻⁵ tail) needs a polarisable core. E-5(d) adds that sub-spec. The verifier's conclusion (core part [E], not [D]) is conceded.

**R-4. LE-52 table vs §3 of VER (ϱ prefactor) — precision, no change of conclusion.**
VER writes ϱ ~ 𝔨₂²/(ξ − 𝔨₁)⁴ in the table and ϱ ≈ 2𝔨₂²/(ξ − 𝔨₁)⁴ in §3. The exact asymptote is (𝔨₄ + 2𝔨₂² − 𝔨₃²/𝔨₂)/(ξ − 𝔨₁)⁴ (sympy, CW2-C22), which reduces to 2𝔨₂²/(ξ − 𝔨₁)⁴ for a Gaussian. The verifier's conclusion (absolute bound, not relative) is conceded and applied (E-4).

Rebuttal count: 3 scope rebuttals (R-1, R-2, R-3) and 1 precision note (R-4). No verifier number was found wrong. Every STANDS WITH CORRECTION item is applied, and no item is conceded silently.

---
## 4. code/CW2 changes (checks.py: 24 → 32 checks, all PASS, ≈ 13 s)
- **Tightened** to the achieved precision:
  - C1a, C1c: 2×10⁻³ and 10⁻³ → 10⁻¹⁰ (machine precision; CW2.md's "10⁻⁶", "10⁻⁵" understate the agreement).
  - C4: 2×10⁻³ → 10⁻⁹ (exact: the empirical law has exactly the moments used).
  - C5: coefficients to ±0.5 eV² and ratio window 7.6–7.8×10⁵.
  - C6: 0.494 ± 0.005 and 0.90 ± 0.01.
  - C7: 10⁻² → 10⁻³.
  - C8: λ₃ exponent ∈ [1.95, 2.08] and quartic contraction to 10⁻⁵.
  - C9: S₄₀/S₀₀ ∈ [2.05, 2.25]%.
  - C11: 10%/20% → 2%/5%.
  - C12b: κ^M_1 and h_iso(50 meV) now checked (−0.0536, −1.718).
- **Circular or trivial checks replaced:**
  - C13 asserted only n_B > 0. It now tests (CW2.23) and (CW2.23′) on a model two-phonon spectrum, including the failure of the pointwise form under a 1% shift.
  - C15 evaluated the closed-form slab reflectance it claimed to verify. It now builds R from 2×2 transfer matrices, matching the closed form to 10⁻¹², with ⟨R⟩ = 2R/(1+R) to 10⁻⁹.
  - C14 mixed Z* = 2.1 (d) with the LST 2.16 it printed. It now uses one Z*.
- **New checks per correction:**
  - OC-2/LE-68/LE-67 → C14;
  - OC-3 → C27;
  - OC-4/LE-64 → C25;
  - OC-6/LE-52/LE-70 → C22;
  - LE-51 → C24;
  - LE-53 → C21;
  - LE-54/LE-56/§0 → C23 (reads ld1/results-errata.json);
  - LE-66/§19 → C13;
  - LE-72 → C16b (κ_URF), C26 (giant moments).
- `OMP_NUM_THREADS=1` is set in-script: the unpinned BLAS ran the old file in 50–97 s.
- **New file** code/CW2/atomic_contact_errata.py → code/CW2/ld1/results-errata.json ([CALC]; inputs embedded per run). atomic_contact.py and ld1/results.json are untouched.

---
## 5. Closing table: verifier item → resolution → location

| VER item | Verdict | Resolution | Location |
|---|---|---|---|
| OC-1 | STANDS | none; text unchanged | §2.1 |
| OC-2 (and status LE-68) | SWC | factor ≈ 7–9, g_e ≈ 2.6–2.9; re-issued | E-1, §2.2, C14 |
| OC-3 | SWC | NR label; < 1% for 𝔯 only; relativistic split into 𝓃_e and Δ𝓃; re-issued | E-2, E-7, R-1, §2.3, C23, C27 |
| OC-4 | SWC | ŵ_ν = c_ν⁻³/Σc⁻³ (CW2.20′); re-issued | E-3, §2.4, C25 |
| OC-5 | STANDS | unchanged | §2.5 |
| OC-6 | SWC | absolute band, tail asymptote; re-issued | E-4, §2.6, C22 |
| OC-7 | STANDS | re-issued only because (CW2.23) became (CW2.23′) (VER §6) | E-9, §2.7, C13 |
| OC-8, OC-9, OC-11 | STANDS | unchanged | §2.8, 2.9, 2.11 |
| OC-10 | SWC | "0.16 [E] stands until ℛ₂ is computed"; re-issued | E-13, §2.10 |
| Status LE-63 | STANDS | none | — |
| LE-48, LE-49, LE-50 | STANDS | none (LE-49's 0.16 sentence via OC-10) | E-13 |
| LE-51 | SWC | ecutrho 65 Ry; core [E]; aliasing pitfall; core-polarisation sub-spec; missing steps listed | E-5, R-3, C24 |
| LE-52 | SWC | tail wording; full convergence block; mK/Kubo and 2-phonon limits; missing steps | E-4, E-12, C22 |
| LE-53 | SWC | exactness withdrawn; exact (CW2.12′) for n = 2, 3 | E-8, C21 |
| LE-54 | SWC | n(0) via cusp (+0.18%); relativistic values r_min-dependent; finite-nucleus [E]; scope per VER §0(ii) | E-6, C23 |
| LE-55 | STANDS | none | — |
| LE-56 | SWC | all four missing steps; Δ𝓃 relativity [CALC]; spec level | E-7, R-1, C23, C27 |
| LE-57, 58, 60, 61 | STANDS | none | — |
| LE-59, LE-62, LE-65, LE-69, LE-71 | STANDS | none | — |
| LE-64 | SWC | as OC-4; Rayleigh leading correction stated | E-3, C25 |
| LE-66 | SWC | (CW2.23′) bin form; convergence block; validation vs 293 K; missing steps | E-9, C13 |
| LE-67 | SWC | one Z*: d = −1.33×10⁻³, +41%, 2.4%, 0.021 u | E-10, C14 |
| LE-70 | SWC | as LE-52 (§23 sentence replaced) | E-4, C22 |
| LE-72 | SWC (κ_URF); CANNOT-CLOSE unless spec (giant moments) | (CW2.27′) with competition and convention; nilpotency fixed; giant-moment derivation (CW2.28) and spec ⇒ CLOSED-AS-EXACT-GAP | E-11, R-2, C16b, C26 |
| VER §0 convergence overstatement | — | n(r_min) vs n(0) quantified; the dx test cannot see it | E-6(i), C23 |
| VER §0(i) SR values inside the nucleus | — | conceded; finite-nucleus [E] 1.08 / 1.37–1.45 | E-6(ii), C23 |
| VER §0(ii) "Dirac current" overstated | — | conceded; only ⟨𝓃_e⟩_{ρ^{nuc}} owed | E-6(iii) |
| VER §0(iii) scope omissions | — | applied with R-1 scoping; IF-CW2-2, IF-CW2-9 re-issued | E-7, §2.12–13 |
| VER §2a, §2b | CONFIRMED / RESOLVED | factor as E-1 | E-1 |
| VER §4 table (5 gap rows) | — | missing steps enumerated for all five; specs completed | E-5, E-12, E-7, E-9, E-11 |
| VER §5 LIMITS format, sources, L1–L5 | — | columns added; "classical, not verified"; L1 leading correction | §2.15 |
| VER §6 §9 notation | — | 𝓃̂_G | E-14, §2.14 |
| VER §6 §19 shift | — | (CW2.23′) | E-9 |
| VER §6 §16 HTML number | — | no change | — |

**Counts after errata.**
- Ledger rows (CW2 §0): CLOSED 20, CLOSED-AS-EXACT-GAP 5 (LE-51, 52, 56, 66, 72), CANNOT-CLOSE 0. These are unchanged; the LE-72 giant-moment half is restored to CLOSED-AS-EXACT-GAP by the E-11(b) spec.
- Verifier rows: 17 STANDS (no action; OC-7 re-issued for consistency) and 16 STANDS WITH CORRECTION (all applied). FALLS 0. Rebuttals 3, plus 1 precision note.
