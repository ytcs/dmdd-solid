# R10 / WP7-T: low-temperature defect quantum kinetics in the URF (tunnelling two-level systems, defectons, crowdions, mK kinetics, release kernel)

Theory agent, brief R10/WP7-T. Architecture: returns/R8/WP0-v3.md (cited "WP0 (n.m)", not re-derived). Neighbours: WP2-v3 (phonon vertices), WP4-v3 §6, §8
(defect final states, Theorem D-g), WP5-v3 §3–§4, §6.3 (recoil partition, (W9)–(W12), L22). CONVENTIONS.md, NOTATION v4 + R9 rows; CORRECTIONS.md read
before every quote (no owed correction touches the WP0-v3, WP2-v3, WP4-v3 §6, §8 or WP5-v3 §3–§4 sites used here; WP0-v3 already carries tr[𝔇ᵀS], G1).
Checks: `code/WP7-T/checks.py` (sympy + mpmath, **46 checks, all PASS, ≈ 3 s**), cited WP7T-Cn. Tags per CONVENTIONS §12: [D], [D, sketch], [E], [C];
literature [FT] (read in full text in literature/papers-WP7-T/, PDFs deleted after use), [UNVERIFIED]. Every arXiv ID was verified against the arXiv API.
Status: all content CLAIMED (one return), pending R×2.

---
## 0. Results at a glance
| # | Item | Result | Tag |
|---|---|---|---|
| 1 | Where defects sit in τ | A defect is a reference-state choice (a nuclear configuration family on E^ad_0), sector GS of WP0 Theorem D (6.1) (insulating host) or D-g (metal host, WP4-v3 §8). The double well is **not** a finite n_A order: metadata `ref=def(·)`, new K value `def` proposed (IF-T1) | D |
| 2 | Defect transition vertex | 𝔣_s(q,ω) = core term + elastic-dipole term −2w_s q̂·γ^{def}·q̂ c_l²q²/[ρ(c_l²q² − (ω+i0)²)] from the WP2-v3 (1.2) vertices and the CONVENTIONS §5 phonon propagator; q-independent in the static window (1.4) | D |
| 3 | TLS response | S^{def} rank one per TLS (2.1); STM ensemble **flat in ω**: S^{STM}_ab = (π/2)P̄_STM 𝔣_a*𝔣_b/(1 + e^{−ω/T}) (2.2) | D |
| 4 | Literature limits, TLS | resonant loss 1/𝔔_el = 1705.01108 Eq. (20); 1/𝔔_ph twice that source's value (source slip, C4c); Jäckle rate = 2103.06977 Eq. (7) = 1610.03974 Eqs. (4)–(5); dark-photon absorption on TLS = κ_mix²m_φ tanδ_TLS/ε_r | D |
| 5 | DM rate on TLS | per TLS a cross-section σ̄_e\|𝔣_e\|²(Δ_tun/E)²/4 (m_χ ≪ m_e, heavy mediator, static window); a-SiO2 ≈ 1×10⁻³ /(kg day meV) at m_χ = 1 MeV, σ̄_e = 10⁻³⁸ cm² | D / E |
| 6 | Defectons | S^{dfn} (3.1): localized limit δ(ω); hot band = arcsine convolution; cold band = free gas with m^{dfn} (WP2 L6 form) | D |
| 7 | Crowdions | translation mass M_cr = 2μ_FK a_111 m/π² (C10a); W: zero-point energy ≈ 40% of a 1 meV Peierls barrier → coherent 1D defecton at mK | D / E |
| 8 | mK hop rate | golden rule in Δ_ij with bath spectral density J^{sb} = J_ph + J_el (4.1); limits: Jäckle, Black/Korringa, ohmic T^{2α_ohm−1} (cond-mat/9409105 Eqs. (8)–(9)), Vineyard/Wigner/T_× (2409.02820 Eqs. (1)–(3)) | D |
| 9 | Tunnelling window | relaxing at mK within 1 yr iff λ ≲ 24: H in Nb (λ ≈ 8), W crowdions (band), Si-mass hops with V ≲ 41 meV (1 Å/d)²; Si close Frenkel pairs (λ ≈ 55) frozen | D / E |
| 10 | Release kernel | 1/t for a broad λ ensemble (= STM heat release, 1610.03974 Eq. (6)); t^{−3/2} for correlated Frenkel-pair recombination (1D crowdion and 3D) | D |
| 11 | Energy per event | one phonon at ε (transverse-dominated) for ε < ω_D; energy-conditioned FC occupation ⟨n_k⟩_ε = S_HR,k A(ε−ω_k)/A(ε) for eV releases; photon branch ≈ 5×10⁻¹⁴ of the phonon branch | D |
| 12 | WP5 / WP7-E interface | p_st(E_st \| E_R, r̂_R, c, T) and 𝒦^{rel}(E,t \| c, T), §5 | D (definitions) |

---
## 1. The defect sector in the URF [D]

**1.1 Placement and truncation chain.** No new Hamiltonian: H = H_C of WP0 (1.1). A defect is a family of local minima {i} of the BO ground surface
E^ad_0(R) (configuration energies E^{conf}_i, WP5-v3 §4) that the nuclear state occupies. *Hypotheses (H-def):* (a) dilute, uncorrelated defects (𝓃_D, or
P̄_STM for an ensemble) — interactions are the leading correction; (b) each well is deeper than ħω of its local modes, so below T ≈ ω_loc/10 only the
well ground states |i⟩ matter; (c) for the GS-sector reading, WP0 §6.2 (H2) holds in the host (insulators, amorphous dielectrics); a metal host replaces
it by Theorem D-g (WP4-v3 §8) with the electron bath of §4.1. Truncation: τ = (n_B = 0, n_g = 0, n_A = −, 𝒳 = − or host ε for charge-coupled
vertices, n_T = 0, K = def, 𝔐 = −, n_D = 0 (density rows) or 1 (TLS electric dipole)). The double-well anharmonicity is non-perturbative in u, like a
broken-symmetry reference (WP0 (1.2)): it enters as metadata `ref=def(STM|band|cr)`, not as an order n_A. The two-level thermal populations are exact,
so n_T = 0 carries no thermal truncation. Library string (proposed, IF-T1):
`nB=0|ng=0|nA=-|X=-|nT=0|K=def|Mg=-|nD=0` + `T=20mK;ref=def(STM:Pbar,gamma);scr=-;conv=window`.

**1.2 Two-configuration reduction [D].** Let |L⟩, |R⟩ be the ground states of two wells (overlap O(e^{−λ})). In this space
H_def = ½(Δ_as σ_z + Δ_tun σ_x), E_TLS ≡ √(Δ_as² + Δ_tun²) (1705.01108 Eqs. (1), (5) [FT], source names ε → Δ_as, Δ₀ → Δ_tun). For every target
operator O_a(q) of the WP0 §2 table,

  P_def O_a P_def = ½(O_a^{LL} + O_a^{RR})𝟙 + ½𝔣_a σ_z + O(e^{−λ}O_a),   𝔣_a(q,ω) ≡ O_a^{RR} − O_a^{LL},                                          (1.1)

and in the eigenbasis |⟨e|O_a|g⟩|² = ¼|𝔣_a|²(Δ_tun/E_TLS)², ⟨g|σ_z|g⟩² = (Δ_as/E_TLS)² (WP7T-C1a,b). The dropped ⟨L|O_a|R⟩ is the leading correction;
it matters only for λ ≲ 3.

**1.3 Core and elastic parts of 𝔣_s [D given WP2-v3 (1.2)].** Write R and L configurations as x_I^{R,L} = x⁰_I + u_I^{R,L}. WP2-v3 (1.2) gives the
linear electron vertex iδρ_κ(q)·u_I and the nucleon vertex i c_κ q·u_I (c_κ = A_κF^M_κ); total charge i𝒵_κ(q)·u_I. Split the atoms into a core (the
tunnelling entity, displaced by d) and the host (displaced by the relaxation field u(r)):
- *core:* 𝔣_s^{core}(q) = Σ_{I∈core} c_{s,κ}(e^{iq·x_I^R} − e^{iq·x_I^L}); one atom of species κ moving by d: 2i c_{s,κ} sin(q·d/2) e^{iq·x̄_I};
- *host:* for q ≪ q_BZ all sublattices co-move, so δO_s(q) = w_s · i q·ũ(q), with the acoustic weights
  w_e ≡ Ω^{-1}Σ_κ q̂·(Z_κ𝟙 − Z*_κ)·q̂ = Ω^{-1}Σ_κZ_κ (acoustic sum rule Σ_κZ*_κ = 0, WP0 (4.8)(i)), w_N ≡ Ω^{-1}Σ_κA_κF^M_κ, **w_c = 0** (neutral
  acoustic motion: a total-charge (dark-photon) coupling sees only the defect dipole 𝐩^{def}, n_D = 1).
The relaxation field is the response of the host to the change of elastic-dipole tensor between the configurations. Define the deformation potential by
δΔ_as = 2γ^{def}_{ij}S_ij (strain S), i.e. H_int = γ^{def}:S σ_z, the convention of 1705.01108 Eq. (16) [FT] and of the Jäckle rate (§2.3). Then
the force density is F(q) = −i(−2γ^{def})·q, and ũ(q,ω) = G(q,ω)F with the retarded acoustic propagator built from the CONVENTIONS §5 phonon operators,
G(q,ω) = Σ_ν e_ν(q̂)e_ν(q̂)†/[ρ(c_ν²q² − (ω+i0)²)] (continuum limit NM_cell = ρV). For an isotropic host the transverse branches drop (WP7T-C5a):

  𝔣_s(q,ω) = 𝔣_s^{core}(q) − 2w_s (q̂·γ^{def}·q̂) c_l²q² / [ρc_l²(c_l²q² − (ω+i0)²)].                                                          (1.2)

**1.4 Regimes of (1.2) [D].** (i) *Static window* ω ≪ c_lq, L^{-1} ≪ q ≪ 1/r_core: the host term is −2w_s q̂·γ^{def}·q̂/(ρc_l²), **q-independent**
(WP7T-C5b) and non-analytic at q = 0. The order of limits is the one of WP0 (4.7′): the thermodynamic limit first. At strictly q = 0 the image
relaxation at the surface restores atom-number conservation; that is a qL ~ 1 effect, irrelevant to DM. (ii) *Dynamic regime* ω ≫ c_lq: the host
responds inertially and the term is suppressed by (c_lq/ω)². (iii) *Pole* ω = c_lq: there the DM can emit a real phonon. **Assignment rule [D, sketch]:**
the principal-value part stays in S^{def}; the δ part is the host one-phonon S^{GS} (WP2) followed by resonant absorption of that phonon by the TLS,
which belongs to P_casc (WP0 (7.3)). This is the DC-type rule of CONVENTIONS §10 applied to the phonon pole, and it prevents double counting.
(iv) *Core vs host:* for a single tunnelling atom the core term (∝ q·d) exceeds the host term above q_× ≈ 2w_s|γ^{def}|/(ρc_l²c_{s,κ}d).
*Size [E]:* a-SiO2 (𝓃_at = 6.6×10²² cm⁻³, Z̄ = 10, ρc_l² = 7.4×10¹⁰ Pa) with |γ^{def}| = 1 eV gives |𝔣_e| ≈ 2.9 (WP7T-C14a) and q_× ≈ 0.6 keV (d = 1 Å).
Crystalline anisotropic hosts: replace G by the Christoffel propagator (computation specification, §2.7).

---
## 2. Tunnelling two-level systems as targets

**2.1 One TLS [D].** Chain: WP0 (3.1) with O_a ∈ {n_e, n_κ^F, s_e^β} and the reduction (1.1); sector GS (no electronic excitation). With
p_g − p_e = tanh(E_TLS/2T):

  S^{def}_ab(q,ω) = 𝓃_D · 2π · ¼(Δ_tun/E_TLS)² 𝔣_a*(q,ω)𝔣_b(q,ω) [p_g δ_Γ(ω − E_TLS) + p_e δ_Γ(ω + E_TLS)],                                        (2.1)

δ_Γ a Lorentzian of width Γ₂ = Γ₁/2 + Γ_φ (1705.01108 Eq. (15) [FT]; Γ₁ from §4). It is rank one (PSD, WP0 (4.4)) and obeys WP0 (4.3) for Gibbs p.

**2.2 STM ensemble [D given 1705.01108 Eq. (8)].** For P(E,Δ_tun) = P̄_STM E/(Δ_tun√(E² − Δ_tun²)) (flat in Δ_as and λ), ∫dΔ_tun P (Δ_tun/E)² = P̄_STM
exactly (WP7T-C2). For |ω| inside the TLS band [Δ_tun^{min}, E_max] the p_g term at E = ω and the p_e term at E = −ω combine into one formula:

  S^{STM}_ab(q,ω) = (π/2) P̄_STM ⟨𝔣_a*𝔣_b⟩ / (1 + e^{−ω/T}),     −Im R^{STM}_ab ⊃ (π/4)P̄_STM⟨𝔣_a*𝔣_b⟩ tanh(ω/2T) (WP0 (4.1)).                     (2.2)

**S is flat in ω.** That is the response-function statement of the STM's constant density of states. Detailed balance holds:
S(−ω)/S(ω) = e^{−ω/T}. ⟨·⟩ averages over the γ^{def} orientations.

**2.3 Literature limits [D].** The same two-state vertex driven by a classical long-wavelength field instead of the DM:
- *(a) Resonant acoustic loss.* Strain S₀cos ωt, energy density ½ρc²S₀²: **1/𝔔_ph = πP̄_STMγ²tanh(ω/2T)/(ρc²)** (WP7T-C4a). Source: 1705.01108 Eq. (20)
  [FT] "1/Q_{i,ph} = π|γ|²D₀/(2ρv²)", with D₀ the TLS DOS. Limit: T → 0 and D₀ → P̄_STM (the (Δ_tun/E)² average gives P̄_STM, not the
  log-enhanced D₀ of its Eq. (9)). The source is **half** the derived value (WP7T-C4c). The derived value uses the same δΔ_as = 2γS as the Jäckle rate
  (b), so (a) and (b) are mutually consistent here; which convention the source intended is [C] (gap G-T5). Leading corrections: power saturation
  (1705.01108 Eq. (22)), TLS interactions, and the relaxation (non-resonant) part −2N D² ∂_E tanh·ωτ₁/(1+ω²τ₁²) (2103.06977 Eq. (6) [FT]).
- *(b) Electric loss.* Field E₀, δΔ_as = 2𝐩^{def}·E, orientation average 1/3, HL units: **1/𝔔_el = πP̄_STM p²tanh(ω/2T)/(3ε_r)** (WP7T-C4b) =
  1705.01108 Eq. (20) [FT] at T → 0 with D₀ → P̄_STM, ε_i ≡ ε_r (HL).
- *(c) Relaxation rate.* §4.1(a): the derived Γ₁ = 2103.06977 Eq. (7) [FT] = 1610.03974 Eqs. (4)–(5) [FT] (WP7T-C3a–c).
- *(d) Dark-photon absorption on TLS.* WP0 (3.5)–(3.6) with L9b's Γ_abs = κ_mix²m_φ Im(−1/ε(m_φ)), where ε contains the TLS term ε₂ = ε₁tanδ_TLS,
  tanδ_TLS = 1/𝔔_el: Im(−1/ε) = tanδ_TLS/[ε_r(1 + tan²δ_TLS)] (WP7T-C14g), so

  ℛ_A′ = ρ_φ κ_mix² tanδ_TLS(m_φ, T) / (ρ_T ε_r)      (m_φ in the TLS band, μeV–meV; per unit target mass).                                     (2.3)

  The measured low-power loss tangent (a-SiO2 tanδ ≈ 1.6×10⁻³ at 4.2 K per 1705.01108 §VI [FT]) is therefore a direct target-response input. Corrections:
  the tanh(m_φ/2T) factor, TLS spectral diffusion, and the transverse in-medium mixing of WP4-v3 [5.4]. Saturation is negligible at halo field strengths
  [E]. The coherent-field regime (τ_c) belongs to WP7-D.

**2.4 DM rate and figure of merit [D for the formula; E for numbers].** 𝒪₁ electron coupling, angle average (WP0 (9.2), hypothesis (I)):
dℛ/dω = (ρ_χσ̄_e/(4πm_χρ_Tμ_χe²))∫q dq F_DM² η(v_min) S̄^{STM}(q,ω). *Static window and heavy mediator:* 𝔣_e is q-independent. For m_χ ≫ ω/v²
(≈ 0.1 keV at ω = 1 meV), v_min ≈ q/2m_χ, and ∫q dq η = 2m_χ²⟨|v|⟩ (ξ(0) = ⟨|v|⟩, WP7T-C13b). For m_χ ≪ m_e:

  dℛ/dω ≈ (ρ_χ/m_χ)⟨|v|⟩ σ̄_e · [P̄_STM⟨|𝔣_e|²⟩/4] / [ρ_T(1 + e^{−ω/T})]    (prefactor 1/4, WP7T-C13a),                                         (2.4)

i.e. each TLS is a target of cross-section σ̄_e|𝔣_e|²(Δ_tun/E)²/4. In terms of the universal tunnelling strength C_TLS ≡ P̄_STMγ_l²/(ρc_l²) (≈ 3×10⁻⁴
in glasses [E]): P̄_STM|𝔣_e|²/4 = (Ω^{-1}ΣZ_κ)²C_TLS/(ρc_l²). Validity: the static window needs q ≫ ω/c_l, i.e. m_χ ≫ ω/(c_l v) ≈ 50 keV (ω/1 meV).
*Number:* a-SiO2, m_χ = 1 MeV, σ̄_e = 10⁻³⁸ cm²: ≈ 1.1×10⁻³ events/(kg day meV) over the band ω ≲ 1 meV (WP7T-C14b, P̄ = 1.6×10¹⁹ eV⁻¹cm⁻³ = 10⁴⁴ J⁻¹m⁻³,
C14c) [E]. *Light mediator:* F_DM² ∝ q⁻⁴ pushes the integral to q ≈ ω/c_l, the pole of (1.2). There the sequential DM → phonon → TLS path dominates,
and it is counted as S^{GS} ⊗ cascade (rule §1.4(iii)) [D, sketch]. *Sensor films* (AlOx barriers, a-Si, SiO2 under TES, a-WSi) have 10⁻⁶–10⁻⁹ of
the detector mass, so they are negligible as DM targets. Their roles are (i) an absorber of DM-generated phonons, with mean free path
ℓ_TLS^{-1} = (ω/c)/𝔔_ph = πP̄_STMγ²ω tanh(ω/2T)/(ρc³) from (2.3a), and (ii) a source of delayed release (§4.5) [D].

**2.5 Metastable populations: the target as an energy source [D, sketch].** WP0 (3.1) needs only a stationary state on the measurement time (WP0 §4
hypotheses). After cooldown or irradiation, p_e exceeds its Gibbs value, and (2.1) with non-Gibbs p_e has an unsuppressed ω = −E line: the DM can
trigger a relaxation and gain energy (detailed balance (4.3) does not apply). The triggered rate per defect, ∫d³q/(2π)³tr[𝔇ᵀS](ω = −E), is smaller than the
spontaneous Γ_↓ of §4 by ~ n_χ⟨v⟩σ̄_e|𝔣_e|²/Γ_↓ ≪ 10⁻²⁰ for any Γ_↓ ≳ 10⁻⁸ s⁻¹ [E]. A DM-triggered *avalanche* therefore needs collective defect
coupling, which stays [C] (WP5-v3 R4).

**2.6 Spin rows.** Paramagnetic TLS and defects (E′ centres, P_b dangling bonds, S = ½) couple through the s_e^β row (𝒪₄). The WP4-v3 §6 [6.1] treatment
applies unchanged (Zeeman or hyperfine-split doublets; WP0 (1.2) hyperfine with the WP4-D1 sign). Nothing new is needed.

**2.7 Computation specification (TLS).** *Inputs:* P̄_STM and γ_l, γ_t from acoustic/dielectric data or from DFT/MLIP-sampled amorphous models
(NEB double-well search on 10⁴–10⁵ candidate pairs in 3000–10⁴-atom a-SiO2/AlOx/a-WSi cells; λ, Δ_as, γ^{def} = ½∂Δ_as/∂S by finite strain;
𝐩^{def} by Berry phase); host elastic constants C^{el}_ij → Christoffel G(q,ω); Z_κ, Z*_κ (DFPT). *New module* `tls_response`: evaluates (1.2) on a
Lebedev q̂ grid (≥ 590 points) × log |q| grid (10⁻¹–10⁴ eV, 60 points) × ω grid (10⁻⁷–10⁻² eV, 50 log points), PV prescription at the pole with
analytic subtraction; outputs ΩS̄^{def}(q,ω) tables with τ string §1.1 for the WP6 library. *Convergence:* (Δ_tun/E)² ensemble average to 1% (≥ 10³
sampled TLS per energy decade); pole subtraction stable to 10⁻³. *Cost:* sampling ~10⁴–10⁵ GPU-h (MLIP), tables < 10 CPU-h.

---
## 3. Defectons and crowdions (delocalised defects)

**3.1 Band-defect response [D].** Chain: WP0 (3.1), GS sector, ref = def(band). Tight-binding defecton, Bloch state |k⟩ = N^{-1/2}Σ_r e^{ik·r}|r⟩
(cond-mat/0310283 Eq. (1) [FT]), dispersion ε_D(k) = E^{loc}_D + J^{dfn}ϖ(k): simple cubic ϖ = Σ_i cos k_ia_lat, bcc 4Π_i cos(k_ia_lat/2) (cond-mat/0310283
Eqs. (2)–(4) [FT]; source names Φ → E^{loc}_D, A → J^{dfn}, ω(k) → ϖ(k)). Band width Δ_dfn = zJ^{dfn}, mass m^{dfn} = 1/(J^{dfn}a_lat²) (simple
lattices, same source). To leading order in the overlap, ⟨k+q|O_s(q)|k⟩ = 𝔣^{loc}_s(q), the localized-defect form factor (defect minus perfect
crystal at one site, relaxation field included as in (1.2)). Then

  S^{dfn}_ab(q,ω) = 2π 𝓃_D 𝔣^{loc*}_a 𝔣^{loc}_b ⟨δ(ω − ε_D(k+q) + ε_D(k))⟩_{f_k},     ⟨·⟩ over the thermal occupation f_k (Σf_k = 1).                  (3.1)

*Limits [D].* (i) J^{dfn} → 0: 2π𝓃_D|𝔣^{loc}|²δ(ω), static diffuse (Huang) scattering, with no energy deposit. (ii) T ≫ Δ_dfn (uniform f_k), simple cubic:
the kernel is the convolution over i = x, y, z of arcsine densities 1/(π√(w_i² − ω²)) with half-widths w_i = 2J^{dfn}|sin(q_ia_lat/2)| (normalised,
WP7T-C11a); the energy transfer is ≤ Σw_i ≤ 2Δ_dfn. (iii) T ≪ Δ_dfn, qa_lat ≪ 1: a free gas of mass m^{dfn},
√(m^{dfn}/(2πq²T)) exp[−m^{dfn}(ω − q²/2m^{dfn})²/(2q²T)] (zeroth moment 1, first moment q²/2m^{dfn}, WP7T-C11b,c). This is WP2's free-recoil form (L6)
with M_κ → m^{dfn}. It obeys the per-defecton f-sum q²/2m^{dfn}, which replaces the bare-mass share of WP0 (4.6b) for this sub-sector [D, sketch]. *Sizes
[FT, cond-mat/0310283]:* Δ_dfn ≈ 10⁻⁴ K (³He in ⁴He), ~ K (vacancies in He). As a DM signal (3.1) is negligible except in He targets; its role is kinetic (§4).

**3.2 Crowdions as 1D defectons [D in the Frenkel–Kontorova model; E for numbers].** Crowdion profile u(z;z₀) = (2a₁₁₁/π)arctan e^{−μ_FK(z−z₀)} and
Peierls barrier E_mig ≈ (8V_P π²/(μ_FK²a₁₁₁²))cosech(π²/(μ_FKa₁₁₁)) (1806.11002 Eqs. (2), (6) [FT]; source names V₀ → V_P, μ → μ_FK, a → a₁₁₁). That
is μeV in FK, meV in atomistic/DFT (same source, text). **New [D]:** the translation mass of the crowdion coordinate z₀ is

  M_cr = m Σ_n (∂u_n/∂z₀)² = 2μ_FK a₁₁₁ m/π²     (WP7T-C10a),                                                                                    (3.2)

so M_cr < m for μ_FKa₁₁₁ < π²/2: moving the centre by a₁₁₁ moves many atoms a little. *W [E]:* μ_FKa₁₁₁ = 0.5 gives M_cr ≈ 0.10 m_W,
E_rec = (π/a₁₁₁)²/2M_cr ≈ 0.15 meV and ħω₀/2 ≈ 0.38 meV against E_mig = 1 meV (WP7T-C10b). The zero-point energy is ~40% of the barrier, so the
crowdion is a coherent 1D defecton along ⟨111⟩ at mK, with a (sub-)meV band (for the FK μeV barrier, a nearly free 1D particle). The leading couplings
are Rayleigh phonon scattering and, in the normal state, the electron bath α_ohm (§4.1(c)). In superconducting W, Nb, Al films below T_c the electron
channel freezes out (§4.1(b)). *Al:* the self-interstitial is a ⟨100⟩ dumbbell with migration ≈ 0.1 eV [UNVERIFIED]; λ ≈ 50 (method of WP7T-C14e),
frozen at mK. 1D glide of interstitial clusters in fcc is [C]. *a-WSi:* no lattice defecton; rearrangements are TLS-like (§2) [E].

**3.3 Light interstitials [E].** H in Nb (d = 1.17 Å, V = 0.1 eV): λ ≈ 8 (WP7T-C14e), quantum. Trapped H forms TLS whose isotope dependence
(H → D: V_eff ratio 2 at equal λ) is 1610.03974 Eqs. (9)–(11) [FT]. Nb cavities, NbTi wiring and Nb films are therefore TLS hosts of the §2 type, with
the electron bath of §4.1(b) above T_c. μ⁺ is the light analogue (not computed).

**3.4 Computation specification (defectons).** DFT (PBE/SCAN) supercells (128–512 atoms) for E^{loc}_D, the hopping J^{dfn} (from the tunnel splitting of
the symmetric double well by path-integral (RPMD) or instanton splitting methods), and 𝔣^{loc}_s(q) (charge-density difference; nucleon form factor).
Crowdions: NEB Peierls profile along ⟨111⟩ (W, Mo, Fe; 1–5 meV resolution 0.1 meV), M_cr from (3.2) checked against the NEB path metric, then the 1D
Schrödinger band (Mathieu solver). Output: ε_D(k), m^{dfn}, S^{dfn} tables. Cost ~10⁵ CPU-h per material.

---
## 4. Defect kinetics at mK (quantum tunnelling versus Arrhenius)

**4.1 General hop rate [D].** A hop i → j releases ε_ij = E^{conf}_i − E^{conf}_j and has tunnelling element Δ_ij = ω₀e^{−λ_ij},
λ_ij = d√(2M_effV)/ħ (WKB, 1705.01108 Eqs. (6)–(7) [FT]; for the symmetric bounce 𝒮_inst(T → 0) = 2λ_ij). The bath couples as ½σ_zΣ_kλ^{sb}_k B_k with
spectral density J^{sb}(ω) ≡ πΣ_k(λ^{sb}_k)²δ(ω − ω_k) = J_ph + J_el,

  J_ph(ω) = (ω³/πρ)(γ_l²/c_l⁵ + 2γ_t²/c_t⁵)   (from §1.3, δΔ_as = 2γS),      J_el(ω) = 2πα_ohm ω   (normal metal; cutoff ω_co).                         (4.1)

To second order in Δ_ij (golden rule in the tunnelling term; non-interacting-blip approximation), the rate is

  Γ_{i→j}(T) = (Δ_ij²/4)∫dt e^{iε_ijt} e^{−𝒬(t)},   𝒬(t) = (1/π)∫₀^∞dω J^{sb}(ω)ω⁻²[coth(ω/2T)(1 − cos ωt) + i sin ωt].                          (4.2)

This is the WP5-v3 Theorem C form: a master-formula rate (WP0 (3.1) type) in which the defect is a target-internal projectile and the bath response is
the overlap correlator e^{−𝒬}. Detailed balance Γ_{i→j}/Γ_{j→i} = e^{ε/T} is built in. *Limits:*
- **(a) One phonon (insulators; STM).** At weak coupling, in the eigenbasis: Γ₁ = (Δ_tun/E)²J_ph(E)coth(E/2T)/2. Derived explicitly from the CONVENTIONS §5
  displacement field and δΔ_as = 2γS (WP7T-C3a,b). This is **2103.06977 Eq. (7) [FT]**, τ₁,ph⁻¹ = (γ_l²/v_l⁵ + 2γ_t²/v_t⁵)(Δ/E)²E³coth(E/2k_BT)/(2πρħ⁴),
  and 1610.03974 Eqs. (4)–(5) [FT] (8π³/ρh⁴ = 1/2πρħ⁴, C3c). *Source discrepancy:* 2103.06977 Eq. (2) writes H_int = ½(γ·S)σ_z, which would give
  Eq. (7)/4 (C3d). Its Eq. (7) corresponds to δΔ_as = 2γS. Corrections: two-phonon (Raman) Γ ∝ T⁷-type, multi-phonon above ~2 K (∝ T⁵ fit, same source), and
  film confinement (quasi-1D phonon bath, 2009.03804 Eq. (3) [FT]).
- **(b) Normal and superconducting metals (Black/Korringa).** For α_ohm → 0, Γ₁ = πα_ohmΔ_tun²coth(E/2T)/E (WP7T-C6c,d) = **2103.06977 Eq. (8) [FT]**
  with W_el² = 4α_ohm = 2009.03804 Eq. (4) [FT] up to its coupling normalisation K = (n₀VΩ)². Superconducting: × 2/(1 + e^{Δ_BCS/T}) (2103.06977
  Eq. (9) [FT], E ≪ Δ_BCS), so at mK in Al/Nb/W films the electron channel is exponentially frozen (reference BCS, Theorem D-g).
- **(c) Finite ohmic coupling (normal metals).** With e^{−𝒬} = [(πT/ω_co)/sinh(πT|t|)]^{2α_ohm}e^{−iπα_ohm sgn t} (scaling limit, ω_co ≫ T, ε):

  Γ_{i→j} = (Δ_ij²/4ω_co)(2πT/ω_co)^{2α_ohm−1} |Γ(α_ohm + iε_ij/2πT)|² e^{ε_ij/2T}/Γ(2α_ohm)     (WP7T-C6b, numerical check of (4.2)).                 (4.3)

  At ε = 0, Γ_{i→j} + Γ_{j→i} = 2cos(πα_ohm)G(0) of **cond-mat/9409105 Eqs. (8)–(9) [FT]** (K → α_ohm, Θ = 2πT; WP7T-C6a). For α_ohm < ½ the rate ∝ T^{2α_ohm−1}
  **rises as T falls** (anti-Arrhenius). For T ≪ ε it tends to the T-independent πΔ²(ε/ω_co)^{2α_ohm−1}/(2Γ(2α_ohm)ω_co). Below the scale of the
  renormalised splitting Δ̃ = Δ(Θ/ω_co)^{α_ohm}[Γ(1−2α_ohm)cos πα_ohm]^{1/2} (same source, after Eq. (10)) the motion becomes coherent (band, §3).
  Leading correction: electron-assisted tunnelling Δ₁ (same source, Eq. (7)), which dominates the relaxation at the lowest T.
- **(d) Arrhenius limit.** For T > T_× = ω_bar/2π (WP5-v3 §4), **2409.02820 Eq. (1) [FT]** k_TST = κZ‡e^{−βV‡}/(2πβħZ_r) with κ = 1 and classical
  harmonic partition functions is Vineyard, Γ = (Πω_i^{(min)}/Πω^{(TS)})e^{−E_bar/T}/2π, the WP5-v3 (W12) rate (WP7T-C7a). The leading quantum
  correction is Wigner's κ_W = 1 + (βħω_bar)²/24 (Eq. (2)), the first term of κ_PB = (βħω_bar/2)/sin(βħω_bar/2) (Eq. (3), WP7T-C7b), which diverges at
  T_× (C7c). Below T_×, instanton theory (Eq. (4)) gives thermally assisted tunnelling. At T ≪ ω_wells the reactant well is in its ground state and (4.2)
  with Δ = ω₀e^{−λ} takes over [D, sketch: the T → 0 instanton rate of a dissipative two-well system is the golden rule in Δ].
- **(e) Band defects.** Defecton diffusion with phonon (Rayleigh) scattering: D_T ~ a_lat c(Δ_dfn/θ_p)²(θ_p/T)⁹, θ_p = c/2a_lat; defecton–defecton
  D ~ J^{dfn}a_lat²/(xσ) (cond-mat/0310283 Eqs. (11)–(12) [FT]). [D, sketch] of the T⁻⁹: thermal phonon number ∝ T³, Rayleigh cross-section ∝ T⁴, and
  (θ_p/T)² collisions per velocity reversal give 1/τ_tr ∝ T⁹ at Δ_dfn ≪ T.
**mK temperature dependence (summary) [D]:** downhill hops with ε ≫ T are T-independent (spontaneous emission ∝ Δ²ε for phonons, ∝ Δ²ε^{2α_ohm−1} for
electrons); uphill hops carry e^{−ε/T}; near-degenerate hops (ε ≲ T) go ∝ T (one phonon) or ∝ T^{2α_ohm−1} (metals); band defects go ∝ T⁻⁹. **None is
e^{−E_bar/T}**: classical TST predicts zero events at mK (WP5-v3 §4), the quantum rates do not.

**4.2 The mK tunnelling window [D for the criterion; E for numbers].** With ω₀ ~ 10¹³ s⁻¹, Γ ~ ω₀e^{−2λ} ≥ 1 yr⁻¹ needs **λ ≲ 24** (WP7T-C14d). For a
Si-mass entity this is V ≲ 41 meV (1 Å/d)². Estimates: H in Nb λ ≈ 8 (relaxes in ≪ 1 s); W crowdion band (§3.2); Si close Frenkel pair (d = 1.5 Å,
V = 0.1 eV) λ ≈ 55, frozen; Al self-interstitial λ ≈ 50, frozen (WP7T-C14e) [E]. The population that relaxes at mK is therefore light species,
crowdions, low-barrier close pairs, and TLS-like pockets in amorphous regions (2408.07518 [ABS] via WP5-v3; not re-read).

**4.3 Correlated Frenkel-pair recombination [D].** (a) *1D crowdion:* coherent band motion is ballistic, t = d/v_g with v_g ≤ a₁₁₁Δ_band. With scattering
the motion is diffusive along the string, and the first-passage density to the vacancy at distance d is f(t) = d(4πDt³)^{−1/2}e^{−d²/4Dt} (normalised;
tail ∝ t^{−3/2}; WP7T-C9a,b). Recombination is certain if the vacancy lies on the string within the capture width; otherwise the crowdion escapes by a
direction change (rare, 1806.11002 text [FT]) to traps. (b) *3D hopping:* eventual capture r_c/r₀ (survival 1 − r_c/r₀), capture-time tail ∝ t^{−3/2}
(WP7T-C9c,d). **Discriminant [D, given the hop statistics]:** correlated recombination gives a t^{−3/2} release law, broad-λ relaxation gives 1/t (§4.5),
narrow barrier sets give exponentials (WP5-v3 §4). Uncorrelated recombination (second order in N_i) gives (1 + t/t₀)⁻² [D, sketch].

**4.4 Energy per event and its spectrum [D].** (a) *ε < ω_D (TLS-like hops, crowdion steps):* one phonon at ε. Branch weights ∝ γ_ν²/c_ν⁵, so transverse
phonons dominate by ~2⁵ for c_l ≈ 2c_t (2103.06977 text [FT]). In normal metals a fraction J_el/(J_el + J_ph) goes to an e–h pair of energy ε (electron
heat). The photon branch is suppressed: Γ_rad/Γ_ph = (8π/3)αd²ρc_t⁵/γ² (HL, 𝐩^{def} = e d, one transverse branch) ≈ 5×10⁻¹⁴ for d = 1 Å, γ = 1 eV in a-SiO2 (WP7T-C14f,h) [E]. (b) *ε ≫ ω_D (Frenkel-pair
recombination, E_st ~ eV):* nonradiative multiphonon emission. With the generating function A(ε) = ∫(dt/2π)e^{iεt}exp Σ_kS_HR,k(e^{−iω_kt} − 1) (the
WP4-v3 [6.3] form), the energy-conditioned first-generation occupation is

  ⟨n_k⟩_ε = S_HR,k A(ε − ω_k)/A(ε)     (exact for linear displaced oscillators; WP7T-C12),                                                       (4.4)

so the release spectrum is dN/dω′ = Σ_k⟨n_k⟩_εδ(ω′ − ω_k), concentrated in the accepting (local, zone-edge) modes. It then down-converts in the WP5
cascade. *Radiative branch* (charged centres, colour centres; delayed luminescence in NaI(Tl), 2210.04128 [FT, qualitative only]): photon spectrum
A_rad(ω) with ZPL weight e^{−S_HR} plus sideband, and branching Γ_rad/(Γ_rad + Γ_nr) from the WP4-v3 §6 inputs. The hand-over to WP5/WP7-E is the pair
(dN/dω′, photon fraction) per release class.

**4.5 Heat-release limit [D].** For an ensemble flat in (Δ_as, λ) (1610.03974 Eq. (1) [FT]) quenched from T₁ to T₀, the TLS with Δ_tun ≪ E relax with
Γ ∝ e^{−2λ}. Then ∫dλ Γe^{−Γt} = (1 − e^{−Γ_max t})/2t (WP7T-C8b) and the stored excess is ∫₀^∞E[f(E,T₁) − f(E,T₀)]dE = π²(T₁² − T₀²)/12 (C8a), so

  Q̇(t) = (π²/24) P̄_STM V (T₁² − T₀²)/t     (WP7T-C8c) = 1610.03974 Eq. (6) [FT].                                                               (4.5)

Leading corrections: the cutoffs Γ_min, Γ_max (the 1/t holds for Γ_max⁻¹ ≪ t ≪ Γ_min⁻¹); thermally activated freezing at T* (1610.03974 Eqs. (7)–(8));
Δ_tun/E ≠ 0; TLS interactions (2210.04128 discussion). The same algebra with E^{conf} releases gives WP5-v3's 1/t law, now **at mK through tunnelling**
rather than through activation.

**4.6 Computation specification (kinetics).** *Barriers and λ:* NEB on the WP5-v3 §3.4 MLIP for every end state of the partition tables. Multidimensional
λ from ring-polymer instantons (corner cutting), checked against WKB along the MEP for 50 paths with DFT. *Bath:* γ^{def} by finite strain;
α_ohm from the defect phase-shift difference (gap G-T1); superconducting gap from WP4. *Rates:* (4.2) with J^{sb} evaluated by direct quadrature
(Filon, 10⁴ points in t, ω_co = ω_D). *Kinetic MC:* WP5-v3 (W12) with these Γ_ij at T = 10–100 mK, 10⁶ seeds. *Output:* ℛ_rel(E,t,T) with nuisances
θ_λ (λ spread) and θ_γ. *Cost:* ~10⁴ GPU-h (instantons) + 10³ CPU-h (KMC).

---
## 5. Defect creation by DM: interface to WP5-v3 and WP7-E

**5.1 Seeds and configurations.** The NR seed is WP5-v3 (W9). Displacement is set by P_FP(E_R, r̂_R) and E_d of WP5-v3 (W10), stored energy
E_st = E^ad_0(R_final) − E^ad_0(R_I(0)) at t_pr (WP5-v3 §3.2). ER seeds cannot displace atoms (≤ 0.78 meV transfer, WP5-v3 §4). Configuration classes c:
| host | interstitial configuration | mK mobility (§4.2) | release law |
|---|---|---|---|
| W, Mo (bcc) | ⟨111⟩ crowdion | coherent 1D defecton (§3.2) | ballistic/diffusive recombination, t^{−3/2} |
| Al (fcc) | ⟨100⟩ split dumbbell | frozen (λ ≈ 50) [E] | none at mK (permanent E_st) |
| Si, Ge | ⟨110⟩ split, tetrahedral, hexagonal (charge-state dependent) [UNVERIFIED geometry] | frozen except close pairs with V ≲ 41 meV(1 Å/d)² | 1/t (broad λ) + t^{−3/2} (correlated) |
| amorphous (a-WSi, AlOx, SiO2) | rearranged pockets / new TLS [C] | TLS-like | 1/t, (4.5) |

**5.2 Stored-energy distribution [D as a definition].**

  p_st(E_st | E_R, r̂_R, T) = Σ_c P(c | E_R, r̂_R) p_c(E_st),   p_c split into λ-classes {relaxing (λ ≤ 24), frozen},                               (5.1)

tabulated from the WP5-v3 §3.4 partition runs (quenched end states labelled by c and by the λ of their lowest exit path). The frozen part is the
permanent heat deficit of WP5-v3 (W11). The relaxing part feeds (5.2).

**5.3 Release-time kernel [D given §4].**

  𝒦^{rel}(E,t | c, T) = Σ_paths 𝒫_path Γ_path(T) e^{−Γ_path t} δ(E − ε_path),   dℛ_rel/dE dt = ∫dt′ Σ_c ℛ_seed,c(t′) 𝒦^{rel}(E, t − t′ | c, T),       (5.2)

with Γ_path from (4.2)–(4.3) (or (4.1)(d) above T_×), ε_path the configuration-energy drop, and each event dressed by the §4.4 spectrum. Closed forms:
broad λ → 1/t; correlated recombination → t^{−3/2} (§4.3); single path → exponential. ℛ_seed,c contains DM (needs E_R ≥ E_d, m_χ ≳ few 100 MeV in
Si, catalog D1), radiogenic and cosmogenic recoils. The kernel is seed-independent, so a calibration source fixes it for the DM case. **Hand-over to WP7-E:**
{p_st, 𝒦^{rel}, dN/dω′ and the photon fraction per class}, with the τ string §1.1 and T as metadata.

**5.4 Computation specification.** Reuse the WP5-v3 §3.4 MLIP-MD partition tables (E_R ∈ [E_d, 10 keV], 100 directions × 100 seeds). Label the end states by
c (Wigner–Seitz / common-neighbour analysis) and compute their exit-path λ (§4.6). Fit P(c|E_R, r̂_R) and p_c(E_st) as histograms (0.1 eV bins, ≥ 10³
events per E_R point). Output 𝒦^{rel} per (c, T ∈ {10, 20, 50, 100} mK). Convergence: E_st mean to 0.1 eV and λ-class fractions to 5%. Cost: dominated by
WP5's 10⁴–10⁵ GPU-h; labelling and λ add ~10⁴ GPU-h.

---
## 6. Exact remaining gaps
- **G-T1.** No first-principles α_ohm for crowdions, H, or TLS in W/Al/Nb/WSi. It needs the defect's partial-wave phase-shift change at E_F (Yamada-type
  formula α_ohm = Σ_l(2l+1)(δ_l^R − δ_l^L)²/π² [UNVERIFIED, from memory]), i.e. a DFT scattering calculation of the two configurations. Without it (4.3) is a
  one-parameter family.
- **G-T2.** The mK fate of Si/Ge close Frenkel pairs depends on multidimensional λ with zero-point motion, and on charge-state-driven (athermal) migration
  under ionization, which (4.2) does not contain (it is an X-sector process). That needs excited-state surfaces (WP3/WP5 R3).
- **G-T3.** P̄_STM, γ^{def} and 𝐩^{def} for specific sensor films are material inputs. The STM universality is an assumption, not derived.
- **G-T4.** Interacting TLS, spectral diffusion and avalanche release (WP5-v3 R4, 2210.04128) remain [C]. (5.2) is the non-interacting (Markov) truncation.
- **G-T5.** Andreev–Lifshitz (1969) is not on arXiv. It is quoted only through cond-mat/0310283 [FT]. The phonon-loss factor ½ in 1705.01108 Eq. (20)
  (§2.3(a)) cannot be checked against the Phillips/Hunklinger originals (not on arXiv).
- **G-T6.** Crowdion-like 1D motion in fcc Al and the Al self-interstitial barrier need DFT (the 0.1 eV used is [UNVERIFIED]).

## 7. Checks (code/WP7-T/checks.py, 46/46 PASS)
C1 two-state matrix elements; C2 STM average = P̄; C3 Jäckle from CONVENTIONS phonons (+ coth, 1610.03974 prefactor, source slip); C4 1/𝔔_ph, 1/𝔔_el,
factor ½ in the source; C5 dynamic elastic vertex (transverse drop, static limit); C6 ohmic NIBA: closed form vs cond-mat/9409105 Eqs. (8)–(9), numerical
quadrature of (4.2) (three cases), Korringa limit, one-boson limit; C7 Vineyard from 2409.02820 Eq. (1), Wigner series, T_× pole; C8 heat release (4.5);
C9 1D first passage and 3D Smoluchowski; C10 crowdion mass (3.2), W numbers; C11 defecton kernels; C12 FC conditional occupation (4.4); C13 rate prefactor,
ξ(0) = ⟨|v|⟩; C14 numbers (a-SiO2 vertex and rate, P̄ units, tunnelling window, λ estimates, photon suppression (C14f,h), Im(−1/ε)).

---
## Symbols introduced/used (against NOTATION v4 + R9 rows)
| Symbol | Meaning | Status vs NOTATION |
|---|---|---|
| Δ_as, Δ_tun, E_TLS = √(Δ_as² + Δ_tun²) | TLS asymmetry, tunnel splitting, level splitting | **new** (source ε, Δ₀ clash with ε (dielectric), Δ₀ → δ_v,0) |
| P_def, \|L⟩, \|R⟩, \|g⟩, \|e⟩ | two-configuration projector and states | new (local) |
| 𝔣_s(q,ω), 𝔣_s^{core}, 𝔣^{loc}_s | defect transition vertex (1.1)–(1.2); core part; localized-defect form factor | **new** (f is crowded) |
| γ^{def}_ij | defect deformation potential, δΔ_as = 2γ^{def}:S | **new** (γ_rel, γ_OA, γ_c taken) |
| 𝐩^{def} | defect electric dipole, δΔ_as = 2𝐩^{def}·E | **new** (p = momentum) |
| w_e, w_N, w_c | acoustic species weights Ω^{-1}Σ_κ(·) | **new** (w_κ is WP2's one-phonon measure; subscripts e, N, c distinguish) |
| G(q,ω) | retarded continuum acoustic displacement propagator | new (local; G_LF, 𝒢 distinct) |
| P̄_STM, C_TLS | STM spectral density (per energy per volume); tunnelling strength P̄γ_l²/(ρc_l²) | **new** (P₀, P₀ (O4), P_0 taken) |
| 𝔔_ph, 𝔔_el; tanδ_TLS | resonant quality factors; TLS loss tangent | **new** (Q = phonon wavevector) |
| ℓ_TLS | TLS-limited phonon mean free path | new (ℓ_mfp is the electron mfp) |
| Γ₁, Γ₂, Γ_φ, Γ_↓, Γ_↑ | TLS relaxation, decoherence, dephasing, emission, absorption rates | new (Γ_χ, Γ^{ph} distinct by decoration) |
| J^{dfn}, Δ_dfn, ϖ(k), E^{loc}_D, ε_D(k), m^{dfn} | defecton hopping, band width, lattice function, localized energy, dispersion, mass | **new** |
| a₁₁₁, μ_FK, V_P, M_cr, E_mig, E_rec | crowdion string spacing, inverse width, FK lattice amplitude, translation mass, Peierls barrier, recoil scale | **new** |
| λ_ij (λ), ω₀, d, M_eff | WKB tunnelling exponent, attempt frequency, well distance, tunnelling mass | **new** (λ bare is the exciton label: always with the subscript ij or the word "exponent"; flag IF-T4) |
| λ^{sb}_k, J^{sb}(ω), J_ph, J_el, 𝒬(t) | bath couplings, spectral density, its phonon/electron parts, overlap exponent | **new** (J^{ex}, J^{(sh)} distinct) |
| α_ohm, ω_co | ohmic (Kondo-type) coupling; bath cutoff | **new** (K is reserved for τ; α bare only for the fine-structure constant) |
| p_st, c (class), 𝒦^{rel}, 𝒫_path, ε_path, ℛ_seed,c | stored-energy distribution, configuration class, release-time kernel, path probability, path energy, seed rate | **new** (c as a class label only inside p_st, 𝒦^{rel}; bare c remains a band subscript) |
| A(ε), ⟨n_k⟩_ε | FC generating line shape; energy-conditioned occupation | new (A(ε) local; A₁, A₂ distinct) |
| used unchanged | E^{conf}_i, Γ_ij, T_×, ω_bar, E_bar, 𝒮_inst, N_i, 𝔰_i, ℛ_rel, E_st, E_d, P_FP, E^{form}_{V,I}, t_pr (WP5 rows); S_HR,k, 𝓃_D, Z*_κ, δρ_κ, c_κ, F^M_κ, C^{el}_ij, Δ_BCS, a_lat, κ_mix, η, ξ, σ̄_e | NOTATION rows |

## Interface flags
| # | Owner / user | Item | Action |
|---|---|---|---|
| IF-T1 | CONVENTIONS §11, WP6 library | defect sector in τ | add K value `def` and `ref=def(STM\|band\|cr)` metadata; the double well is not an n_A order (§1.1) |
| IF-T2 | WP5-v3 §4, (W12) | sub-T_× rates | replace "Γ_ij ∝ e^{−𝒮_inst}" by (4.2)–(4.3) with the bath J^{sb}; T-independent or power-law at mK; Vineyard only above T_× (§4.1) |
| IF-T3 | WP7-E | release model | consume p_st (5.1), 𝒦^{rel} (5.2), dN/dω′ (4.4); laws 1/t, t^{−3/2}, exponential as derived discriminants |
| IF-T4 | NOTATION | new rows | the §Symbols "new" rows; λ_ij needs its subscript to avoid the exciton label λ |
| IF-T5 | WP2-v3 (1.2), WP4-v3 §6 | defect vertices | (1.2) adds the dynamic elastic-dipole term to the [6.1] defect response (host phonon propagator, PV/δ split at the phonon pole) |
| IF-T6 | WP7-D | dark photon on TLS | (2.3) is the incoherent golden-rule limit of the coherent-field absorption on a TLS dielectric |
| IF-T7 | WP4-v3 §4.5 (films) | TLS in a-WSi, AlOx | the TLS phonon mean free path ℓ_TLS and the delayed release (4.5) enter the film phonon budget |
| IF-T8 | LIMITS, CATALOG-B G12 | TLS / kinetics rows | L25–L32 below (numbers provisional; the coordinator assigns) |

## Proposed LIMITS rows
| # | τ / chain (URF) | source formula [FT] | status |
|---|---|---|---|
| L25 | (2.1)–(2.2) driven by a classical strain or E field, ref = def(STM): resonant TLS loss 1/𝔔_ph = πP̄γ²tanh/(ρc²), 1/𝔔_el = πP̄p²tanh/(3ε_r) | 1705.01108 Eq. (20) (T → 0, D₀ → P̄; phonon form ½ of derived, G-T5); 2103.06977 Eqs. (4)–(6) | DERIVED (phonon factor ✎) |
| L26 | (4.2), one boson, weak coupling: Γ₁ = (Δ/E)²J^{sb}(E)coth/2 with J_ph (Jäckle) and J_el (Black), × 2/(1 + e^{Δ_BCS/T}) | 2103.06977 Eqs. (7), (8), (9); 1610.03974 Eqs. (4)–(5); 2009.03804 Eq. (4) | DERIVED (2103.06977 Eq. (2) coupling ✎) |
| L27 | (4.2) with ohmic J_el, scaling limit (4.3): T^{2α_ohm−1} | cond-mat/9409105 Eqs. (8)–(9) (and Δ̃ after Eq. (10)) | DERIVED |
| L28 | T > T_×: TST → Vineyard (WP5 (W12)), Wigner κ_W, κ_PB, crossover T_× = ω_bar/2π; instanton below | 2409.02820 Eqs. (1)–(4) | DERIVED |
| L29 | (4.2) + flat P̄(Δ_as, λ): STM heat release Q̇ = (π²/24)P̄V(T₁² − T₀²)/t | 1610.03974 Eq. (6) (Eqs. (7)–(8) for T*) | DERIVED |
| L30 | (3.1) ref = def(band): defecton dispersion; quantum diffusion D_T ∝ T⁻⁹, D ∝ 1/(xσ) | cond-mat/0310283 Eqs. (1)–(4), (7), (11)–(12) | DERIVED (dispersion, kernel); [D, sketch] (T⁻⁹) |
| L31 | (3.2) crowdion: FK profile and Peierls barrier; translation mass M_cr = 2μ_FKa₁₁₁m/π² (new) | 1806.11002 Eqs. (2), (3), (6) | DERIVED in FK; numbers [E] |
| L32 | WP0 (3.5)–(3.6), L9b with ε ⊃ TLS: ℛ_A′ = ρ_φκ_mix²tanδ_TLS/(ρ_Tε_r) | 1705.01108 Eq. (20) (electric) via L25 | DERIVED |
