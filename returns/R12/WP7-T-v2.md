# R12 / WP7-T-v2: low-temperature defect quantum kinetics in the URF (TLS, defectons, crowdions, mK kinetics, release kernel), corrected standalone version

Revision agent, R12 correction round. Supersedes returns/R10/WP7-T.md (v1, kept as the historical record). Applies every verdict of the two R11 referees
(referees/R11/REF-WP7-T-A.md, items A#n / A§n; REF-WP7-T-B.md, items B#n / C-n), plus the coordinator's list. Closing table: §8.
Architecture: returns/R8/WP0-v3.md (cited "WP0 (n.m)", not re-derived). Neighbours: WP2-v3 (1.2) (phonon/charge vertices), WP4-v3 §6, §8, WP5-v3 §3–§4, §6.3
((W9)–(W12), L22), WP7-E (R10) (E5)–(E6), IF-E2. CONVENTIONS.md, NOTATION v4 + R9 rows. CORRECTIONS.md was read before every quote; none of its items
touches the sites used here.
Checks: `code/WP7-T-v2/checks.py` (sympy + mpmath; **51 checks, all PASS, ≈ 8 s** after the R12 clean-up; cited WP7T-Cn). v1's vacuous C3d, C4c, C7c, C13a, C14f and the vestigial C14c are
removed (B C-15; VER-B N3). Three remaining checks are only unit or arithmetic conversions: C3c, C14b′ and the numbers in C14d.
**R12 clean-up** (VER-WP7-T-A/B; coordinator energy convention) edited in place: table §9.
Tags (CONVENTIONS §12): [D], [D, sketch], [E], [C]; literature [FT] (full text in literature/papers-WP7-T/, PDFs deleted), [ABS], [UNVERIFIED].
arXiv IDs were verified against the API (v1). Status: CLAIMED, pending R×2. **No novelty is claimed in this return.** The priority of DM–TLS scattering is
UNRESOLVED (A§4).

---
## 0. Results at a glance (v2)
| # | Item | Result | Tag |
|---|---|---|---|
| 1 | Placement in τ | Configuration family on E^ad_0, sector GS (insulator) or D-g (metal). Double well = metadata `ref=def(STM\|band\|cr)`. **K = −** (v1's K=def withdrawn). 𝒳 = −. **scr = DFPT** (vertex already self-consistent; §1.5) | D |
| 2 | Vertex 𝔣^{def}_s | core + elastic-dipole term **+2**w_s q̂·γ^{def}·q̂/[ρ(c_l²q² − (ω+i0)²)]·q². v1's overall host sign is corrected (C5c). Static window: q ≪ min(q_×, 1/r_core) | D |
| 3 | Pole rule | double pole: (π/η)δ part → S^{GS} ⊗ P_casc; finite δ (Fano-type) part exported with it; **Hadamard fp** and PV parts → S^{def} (C5d) | D |
| 4 | TLS response | rank one per TLS; STM ensemble flat in ω: (π/2)P̄𝔣*𝔣/(1+e^{−ω/T}) (one-sign STM convention) | D |
| 5 | Literature limits | 1/𝔔_el = 1705.01108 Eq. (20). 1/𝔔_ph = 2103.06977 Eqs. (4), (12), (13), (15) (C4c); the factor ½ in 1705.01108 Eq. (20) is a **settled** source slip. Jäckle/Black rates; α_ohm = 4K₂₀₀₉ | D |
| 6 | DM rate on TLS | (1 + m_χ/m_e)² restored. a-SiO2, m_χ = 1 MeV, σ̄_e = 10⁻³⁸ cm², one boosted-SHM halo: host 1.0×10⁻², plus core (Re(a*B) = 0, exact sum) ≈ 3.7×10⁻² /(kg day meV) over ω ≲ 0.1 meV | D / E |
| 7 | Crowdions | M_cr = 2μ_FKa₁₁₁m/π² is the **textbook FK/sine-Gordon kink mass** (Braun–Kivshar; Kosevich) (C10c). W band ≈ 0.024 meV (C10d). Coherence at mK **[C]** | D / E / C |
| 8 | mK hop rate | (4.2) with J^{sb} = J_ph + J_el + local modes; weak-coupling energy-gap law vs strong-coupling (Marcus/instanton) | D |
| 9 | Tunnelling window | Phillips/Jäckle convention λ_P = (d/2)√(2MV): H/Nb 4.1, Si close pair 27.5 (quartic 37), Al 25. "Frozen" verdicts **withdrawn → OPEN [E]** | E |
| 10 | Release laws | 1/t (broad λ) = STM heat release; 3D correlated recombination t^{−3/2}. 1D crowdion recombination is drift-dominated (v1's t^{−3/2} withdrawn) | D / C |
| 11 | Release-path sum rule | **Theorem T-1** [D]: ∫dt∫dE E𝒦^{rel} = E_st − ⟨E_st^{unrel}(t_obs)⟩, an identity of any closed linear single-seed master equation (W12), also with time-dependent rates; configurational energies, ΔZPE in ℋ_ph. Closes WP7-E IF-E2 (C16, C16b) | D |

---
## 1. The defect sector in the URF [D]

**1.1 Placement and truncation chain.** H = H_C (WP0 (1.1)), with no new Hamiltonian. A defect is a family of local minima {i} of E^ad_0(R) (energies
E^{conf}_i, WP5-v3 §4).

*Hypotheses (H-def).*
- (a) Defects are dilute and uncorrelated (density 𝓃_D, or P̄_STM for an ensemble).
- (b) Wells are deep: below T ≈ ω_loc/10 only the well ground states |i⟩ are populated.
- (c) WP0 §6.2 (H2) holds in the host. For a metal host it is replaced by Theorem D-g (WP4-v3 §8) with the electron bath of §4.1.

*Truncation (A#1, B#1 applied).* τ = (n_B = 0, n_g = 0, n_A = −, 𝒳 = −, n_T = 0, **K = −**, 𝔐 = −, n_D = 0 for density rows, 1 for the TLS dipole).
- The double well is non-perturbative in u, so it enters as metadata `ref=def(STM|band|cr)`, not as an n_A order.
- K stays the kinematic slot (CONVENTIONS §11); v1's `K=def` is withdrawn.
- Screening is `scr=DFPT` (§1.5).
- Convention `conv=DC` (§1.4).

Library string: `nB=0|ng=0|nA=-|X=-|nT=0|K=-|Mg=-|nD=0` + `T=20mK;ref=def(STM:Pbar,gamma);scr=DFPT;conv=DC`.

**1.2 Two-configuration reduction [D].** Take |L⟩, |R⟩ well ground states. In their span, H_def = ½(Δ_as σ_z + Δ_tun σ_x) with E_TLS = √(Δ_as² + Δ_tun²)
(1705.01108 Eqs. (1), (5) [FT]; source names ε → Δ_as, Δ₀ → Δ_tun). For every row O_a of the WP0 §2 table:

  P_def O_a P_def = ½(O_a^{LL} + O_a^{RR})𝟙 + ½𝔣^{def}_a σ_z + O(e^{−λ}O_a),   𝔣^{def}_a(q,ω) ≡ O_a^{RR} − O_a^{LL},                                  (1.1)

with |⟨e|O_a|g⟩|² = ¼|𝔣^{def}_a|²(Δ_tun/E_TLS)² and ⟨g|σ_z|g⟩² = (Δ_as/E_TLS)² (C1a,b). The decoration "def" is mandatory: 𝔣_Lin is taken (B §d).
The ⟨g|σ_z|g⟩ part gives a quasi-elastic relaxation line at |ω| ≲ Γ₁, with weight ∝ (Δ_as/E)²sech²(E/2T). DM cannot reach it above any threshold,
so it is dropped (A#3).

**1.3 Vertex [D given WP2-v3 (1.2)].** WP2-v3 (1.2) gives the linear vertices: electron iδρ_κ(q)·u_I (δρ_κ → q·(Z_κ𝟙 − Z*_κ) as q → 0), nucleon
i c_κ q·u_I with c_κ = A_κF^M_κ, and total charge i𝒵_κ·u_I.
- *Core term:* 𝔣^{def,core}_s = Σ_{I∈core} c_{s,κ}(e^{iq·x_I^R} − e^{iq·x_I^L}). For one atom displaced by d it is 2i c_{s,κ}sin(q·d/2)e^{iq·x̄}.
- *Host term* (q ≪ q_BZ, all sublattices co-moving): δO_s = w_s i q·ũ(q). The weights are w_e = Ω⁻¹Σ_κZ_κ (from Σ_κZ*_κ = 0, WP0 (4.8)(i)),
  w_N = Ω⁻¹Σ_κA_κF^M_κ, and **w_c = 0** (a dark photon sees only 𝐩^{def}).

*Sign (B C-9; v1 corrected).* A force pair ±F at ±a/2 (expansion for F > 0) gives f(q) = iD·q with D = F⊗a. Its energy in an external strain is
E_int = −D:S. Deformation potential: δΔ_as = 2γ^{def}:S, i.e. H_int = γ^{def}:Sσ_z, the convention of 1705.01108 Eq. (16) and of the Jäckle rate.
Hence D_R − D_L = −2γ^{def}. The static density response is δn = i n₀q·ũ = −n₀q̂·D·q̂/(ρc_l²) (C5c). With the retarded propagator
G(q,ω) = Σ_νe_νe_ν†/[ρ(c_ν²q² − (ω+i0)²)] (CONVENTIONS §5 phonons, continuum NM_cell = ρV), only the longitudinal branch survives (C5a):

  𝔣^{def}_s(q,ω) = 𝔣^{def,core}_s(q) + 2w_s (q̂·γ^{def}·q̂) q² / [ρ(c_l²q² − (ω+i0)²)].                                                            (1.2)

The c_l² factors of v1 cancel (A§1.1). v1 printed the host term with a minus sign; that came from the opposite sign convention for f. Physically, γ > 0 means
R is compressed relative to L, so the host δn_e is **positive** (C5c). The relative sign of the core and host terms is now fixed for interference studies.

**1.4 Regimes and the pole rule [D].**
- (i) *Static window.* ω/c_l ≪ q ≪ min(q_×, 1/r_core) (A§1.6, B C-3), with q_× ≈ 2w_s|γ|/(ρc_l²c_{s,κ}d) (≈ 0.6 keV for a-SiO2, d = 1 Å).
  - Here the host term is 2w_s q̂·γ·q̂/(ρc_l²), q-independent.
  - It is non-analytic at q = 0; the thermodynamic limit is taken first, as in WP0 (4.7′).
  - For q ≳ 1/r_core, continuum elasticity fails. The full sum Σ_I δρ_κ(q)·u_I over the computed relaxation field replaces w_s (spec §2.7).
- (ii) *Dynamic regime* ω ≫ c_lq: the host term is suppressed by (c_lq/ω)².
- (iii) **Pole (A#2, B#4 FALLS → rewritten).** Write x ≡ c_l²q² − ω² and η ≡ ωΓ_ph, where the phonon width Γ_ph = c_l/ℓ_TLS + anharmonic.
  Let B be the host-term numerator and a the core amplitude. Then

  |a + B/(x − iη)|² = |a|² + (π|B|²/η)δ(x) + |B|² fp(1/x²) + 2Re(a*B) PV(1/x) − 2π Im(a*B) δ(x) + O(η)     (C5d).                                    (1.3)

  The assignment (CONVENTIONS §10, the DC rule transposed to the phonon pole) is as follows:
  - the (π|B|²/η)δ term is real-phonon emission (S^{GS} of WP2) followed by absorption, which belongs to P_casc (WP0 (7.3));
  - the finite δ term −2πIm(a*B)δ(x) is the Fano-type core–host interference; it is exported with the cascade seed, like 𝔉 (O4-d7);
  - **fp(1/x²)** and PV parts stay in S^{def}.
  v1's "PV part" of a double pole was undefined.

**1.5 Screening: rebuttal of "add ε_e⁻¹" (A§1.3, B C-8) [D].** In the GS sector, ⟨f|n_e(q)|i⟩ = ⟨χ_f|ρ̄_e(q;R)|χ_i⟩ + O(κ_BO²) (WP0 §6.2(ii)). Here ρ̄_e
is the self-consistent adiabatic density, so δρ_κ = ∂ρ̄_e/∂u_κ is the DFPT-screened vertex.
- Equivalently, to first order in an external potential φ coupled to electrons, two quantities are equal by the symmetry of the static response R:
  the force on nucleus κ, ∫(−∂_{u_κ}V_eN)Rφ, and ∫φ δρ_κ.
- So the screening ε_e⁻¹ is already inside δρ_κ. A second ε_e⁻¹(q,ω) would screen twice, against CONVENTIONS §7 ("screening is applied once: DFPT g").
- **Scope (R12, VER-A §2):** this holds only if δρ_κ(q) is the **full finite-q (improper) DFPT response, including the G = 0 macroscopic Hartree
  component**, not one reconstructed from Born charges (Z*_κ is defined with the macroscopic field removed, i.e. proper). For the neutral acoustic host
  term the two agree (Σ_κZ*_κ = 0, no macroscopic field). For a core atom with Z*_κ ≠ 0 (O in SiO2) at q ≲ q_BZ the dipolar part is reduced by the
  macroscopic screening (≈ 1/ε_∞ at q → 0, → 1 at q ≫ q_BZ); the rigid-ion core of §2.4 omits this.
- The τ string therefore carries scr=DFPT, not scr=−.
- Leading corrections: (a) non-adiabatic, O(κ_BO²ω/δ); (b) the acoustic-sum-rule weight w_e needs q ≪ q_BZ, which is marginal at q ~ keV (B C-8).
  For q ≳ q_BZ use the full Σ_κ δρ_κ(q) (§2.7).

---
## 2. Tunnelling two-level systems as targets

**2.1 One TLS [D].** Chain: WP0 (3.1), rows {n_e, n_κ^F, s_e^β}, (1.1), sector GS:

  S^{def}_ab(q,ω) = 𝓃_D 2π ¼(Δ_tun/E_TLS)² 𝔣^{def*}_a𝔣^{def}_b [p_gδ_Γ(ω − E_TLS) + p_eδ_Γ(ω + E_TLS)],   p_g − p_e = tanh(E_TLS/2T).                   (2.1)

- The width Γ₂ = Γ₁/2 + Γ_φ (1705.01108, text above its Eq. (15) [FT]; A§2).
- (2.1) is rank one and PSD, and obeys WP0 (4.3).

**2.2 STM ensemble [D].** Take P(E,Δ_tun) = P̄_STM E/(Δ_tun√(E² − Δ_tun²)) (1705.01108 Eq. (8); 2103.06977 Eq. (12) [FT]). This is the **one-sign**
convention, Δ_as ≥ 0; a two-sign convention doubles every rate (A§1.4). Then ∫dΔ P(Δ/E)² = P̄_STM (C2), and inside the TLS band

  S^{STM}_ab(q,ω) = (π/2)P̄_STM⟨𝔣^{def*}_a𝔣^{def}_b⟩/(1 + e^{−ω/T}),   −Im R^{STM}_ab = (π/4)P̄_STM⟨𝔣*𝔣⟩tanh(ω/2T)   (WP0 (4.1)).                   (2.2)

The band in a-SiO2 extends to ≈ 0.1 meV only: C ∝ T below ~1 K, and soft modes take over above (B C-14) [E].

**2.3 Literature limits [D].**
- **(a) Acoustic loss.** 1/𝔔_ph = πP̄_STMγ²tanh(ω/2T)/(ρc²) (C4a).
  - The same result follows from **2103.06977 Eqs. (4), (12), (13), (15) [FT]** read literally (C4c): χ″_res = 4NM²tanh·πδ (τ₂ → ∞), M = γΔ/2E,
    tanδ = ⟨χ⟩″/(ρv²).
  - 1705.01108 Eq. (20) [FT], π|γ|²D₀/(2ρv²), is therefore ½ of the value implied by its own Eq. (16) and by its electric form. This is a source slip,
    CONFIRMED by both referees and now **settled**; v1's G-T5 clause is withdrawn.
  - Eq. (20) also has D₀ (log-enhanced, its Eq. (9)) where the (Δ/E)² weight gives P₀, and it carries no tanh.
  - Corrections: saturation (1705.01108 Eq. (22)), the relaxation part (2103.06977 Eq. (6)), TLS interactions.
- **(b) Electric loss.** 1/𝔔_el = πP̄_STMp²tanh(ω/2T)/(3ε_r) (HL; C4b) = 1705.01108 Eq. (20) at T → 0 with D₀ → P̄.
- **(c) Relaxation rate.** §4.1(a): 2103.06977 Eq. (7) and 1610.03974 Eqs. (4)–(5) (C3a–c).
  - 2103.06977's text "δε = γ·S, H_int = ½(γ·S)σ_z" is a notation slip: its Eqs. (4)–(7) all need δε = 2γS. CONFIRMED by both referees from their own
    derivations; v1's tautological C3d is removed.
- **(d) Dark photon on TLS.** WP0 (3.5)–(3.6), L9b: Γ_abs = κ_mix²m_φIm(−1/ε), and Im(−1/ε) = tanδ/[ε₁(1 + tan²δ)] (C14g). With
  **tanδ_TLS(m_φ,T) ≡ tanδ₀ tanh(m_φ/2T)**, where tanδ₀ is the T → 0, low-power value:

  ℛ_A′ = ρ_φκ_mix² tanδ₀ tanh(m_φ/2T)/(ρ_Tε_r),                                                                                                    (2.3)

  with no second tanh (A§1.5).
  - *Input (misquote corrected, A§2, B C-6):* 1705.01108 §VI [FT] quotes tanδ ≈ 1.6×10⁻³ for **thin plasma-oxidised AlOx** (Deng et al.), with no
    temperature stated, and tanδ = 2.5×10⁻⁵ at 4.2 K for **a-Si:H** (Bruno et al.).
  - The 4.2 K value is thermally saturated (tanh ≈ 0.03 at 5 GHz). Neither number is an a-SiO2 tanδ₀.
  - Remaining corrections: spectral diffusion; transverse in-medium mixing (WP4-v3 [5.4]).

**2.4 DM rate [D for the formula; E for numbers] (A#5, B#8 applied).** Start from WP0 (9.2) with 1/μ_χe². With ∫q dq η(q/2m_χ) = 2m_χ²⟨|v|⟩ (C13b):

  dℛ/dω = (ρ_χ/m_χ)⟨|v|⟩σ̄_e (1 + m_χ/m_e)² P̄_STM⟨|𝔣^{def}_e|²⟩ / [4ρ_T(1 + e^{−ω/T})],                                                            (2.4)

i.e. per TLS a cross-section σ̄_e(1 + m_χ/m_e)²|𝔣^{def}_e|²(Δ_tun/E)²/4.
- *Validity:* m_χ ≫ ω/⟨v⟩² ≈ 0.1 keV (ω = 0.1 meV) for v_min ≈ q/2m_χ, and the Born and 𝒪₁ hypotheses of WP0 §9.1.
  - *Host-only q-independence* needs the §1.4(i) window: ω/(c_l v) ≪ m_χ ≲ q_×/(2v) ≈ 0.3 MeV (d = 1 Å).
  - Outside it, ⟨|𝔣|²⟩ = ⟨|𝔣^{core} + 𝔣^{host}|²⟩.
- *Inputs made consistent (A§1.6, B C-14).* C_TLS = 3×10⁻⁴ and γ_l = 1 eV imply **P̄_STM = 1.4×10²⁰ eV⁻¹cm⁻³ = 8.6×10⁴⁴ J⁻¹m⁻³** (C14b′), the a-SiO2
  literature order [E]. v1's parenthetical 10⁴⁴ J⁻¹m⁻³ (SiN-like) is withdrawn.
- *Number at m_χ = 1 MeV, σ̄_e = 10⁻³⁸ cm², a-SiO2:*
  - host term with (1 + m_χ/m_e)² = 8.74: 9.6×10⁻³ /(kg day meV) at the v1 halo ⟨|v|⟩ = 330 km/s;
  - *Halo (R12, VER-A N2, VER-B 3(i)):* one halo for both terms, a boosted Maxwellian (v₀ = 238, v_E = |v_⊙| = 250.5 km/s, no escape cut) [E], whose
    ⟨|v|⟩ = ξ(0) = 358 km/s rescales the host term to **1.0×10⁻²** /(kg day meV);
  - plus a one-O core (d = 1 Å, f ≈ Z = 8). **Core and host add incoherently for every orientation, not only on average** (R12, VER-A N1): with the
    origin at the defect centre x̄, the core amplitude 2if sin(q·d/2) is purely imaginary while the static host term is real, so Re(a*B) ≡ 0 and the
    PV cross term of (1.3) vanishes in the static window (only the Fano δ term survives, at the pole). R_core = 2.6 (orientation-averaged 2f²(1 − sin qd/qd));
  - total ≈ **3.7×10⁻²** /(kg day meV) over ω ≲ 0.1 meV (C14b) [E, factor ~3].
  - *Core caveats (R12, VER-B N4):* (i) rigid-ion core f = Z_O = 8, not the DFPT δρ_κ that §1.5/§2.7 prescribe: valence redistribution of 6 of the 8
    electrons and the macroscopic screening of the O dipole (§1.5 scope) are O(1) effects at q ≈ 1–2 keV; (ii) one geometry (one O moving 1 Å);
    (iii) off-centre cores restore a nonzero Re(a*B). No extra screening factor on the host term (§1.5).
- *Light mediator:* F_DM² ∝ q⁻⁴ drives q → ω/c_l. The (π/η)δ part of (1.3) dominates and belongs to S^{GS} ⊗ cascade [D, sketch].
- *Sensor films* (AlOx, a-Si, SiO2 under TES, a-WSi) are negligible as targets.
  - They absorb phonons: ℓ_TLS⁻¹ = (ω/c)/𝔔_ph = πP̄γ²ω tanh(ω/2T)/(ρc³), from §2.3(a).
  - They are also delayed-release sources (§4.5).

**2.5 Metastable populations [D, sketch].** WP0 (3.1) needs only stationarity on the measurement time. A non-Gibbs p_e gives an unsuppressed ω = −E line,
so DM can trigger relaxation.
- With σ̄_e = 10⁻³⁸ cm², m_χ = 1 MeV and Γ_↓ = 10⁻⁸ s⁻¹ (v1 halo ⟨|v|⟩ = 330 km/s), the triggered/spontaneous ratio n_χ⟨v⟩σ̄_e(1+m_χ/m_e)²|𝔣|²/(4Γ_↓) ≈ 2×10⁻¹⁹ (A#13, B#9).
- Avalanches need collective coupling, which stays [C] (WP5-v3 R4).

**2.6 Spin rows.** Paramagnetic defects (E′, P_b): WP4-v3 §6 [6.1] applies unchanged.

**2.7 Computation specification (TLS) (fixed per A#2, B#20, C-14).**
- *Sampling:* the TLS with |Δ_as| < 1 meV and λ_P < 20 number ~10⁻⁵ per atom. Obtaining ≥ 10³ TLS per energy decade needs ≳ 10⁸ minimum pairs.
  - Method: landscape filtering / swap-MC preselection on MLIP models (a-SiO2, AlOx, a-WSi; 10³–10⁴-atom cells, ≳ 10⁴ quenched glasses).
  - NEB on the pairs with ΔE < 5 meV; λ_P from the instanton path; γ^{def} by finite strain; 𝐩^{def} by Berry phase.
- *Vertex:* core plus the computed relaxation field Σ_Iδρ_κ(q)·(u_I^R − u_I^L), with δρ_κ from DFPT (no extra ε⁻¹, §1.5). Christoffel G(q,ω) from C^{el}_ij.
- *Module `tls_response`:* (1.3) on Lebedev q̂ (≥ 590) × log|q| (10⁻¹–10⁴ eV, 60) × ω (10⁻⁷–10⁻³ eV, 50).
  - The **Hadamard fp** is implemented by subtraction, fp∫φ/x² = ∫[φ(x) − φ(0) − xφ′(0)θ(1−|x|)]/x² dx, with PV for the cross term.
  - The (π|B|²/η)δ and Fano δ terms are exported to the cascade.
- *Outputs:* ΩS̄^{def} tables with the §1.1 τ string.
- *Convergence:* the ensemble average to 1%; the fp subtraction stable to 10⁻³ under halving of the inner interval.
- *Cost:* 10⁵–10⁶ GPU-h (sampling), < 10 CPU-h (tables).

---
## 3. Defectons and crowdions

**3.1 Band-defect response [D; dispersion quoted].** Bloch defecton |k⟩ = N^{−1/2}Σ_r e^{ik·r}|r⟩ with dispersion ε_D(k) = E^{loc}_D + J^{dfn}ϖ(k). This is quoted
from cond-mat/0310283 Eqs. (1)–(4) [FT], not derived (A#6): Δ_dfn = zJ^{dfn}, m^{dfn} = 1/(J^{dfn}a_lat²). Then

  S^{dfn}_ab(q,ω) = 2π𝓃_D 𝔣^{def,loc*}_a𝔣^{def,loc}_b ⟨δ(ω − ε_D(k+q) + ε_D(k))⟩_{f_k}.                                                              (3.1)

Limits:
- (i) J^{dfn} → 0: δ(ω), static diffuse scattering.
- (ii) T ≫ Δ_dfn, simple cubic: a convolution of arcsine kernels with half-widths w_i = 2J^{dfn}|sin(q_ia_lat/2)| (C11a). Their sum is Σw_i ≤ 6J^{dfn} = Δ_dfn
  (v1's "2Δ_dfn" corrected, A§1.7).
- (iii) T ≪ Δ_dfn, qa ≪ 1: free gas of mass m^{dfn} (C11b,c), the WP2 L6 form with M_κ → m^{dfn}.
- *f-sum (A#6, B C-10):* WP0 (4.6) is an exact commutator and stays unchanged. The band carries the partial first moment |𝔣^{def,loc}|²q²/2m^{dfn},
  redistributed from the host phonon part; it replaces nothing.
- *Localisation (B C-11):* a defecton cannot cross energy gradients |∇φ|a > Δ_dfn (cond-mat/0310283 Eq. (17) [FT]). All defectons are localised above
  x_c = (Δ_dfn/(nV₀))^{3/(1+n)} (Eq. (18)).

**3.2 Crowdions (A#7, B#11–12, C-5, C-11 applied) [D in FK; E; C].**
- *Profile and barrier:* u(z;z₀) = (2a₁₁₁/π)arctan e^{−μ_FK(z−z₀)} and E_mig ≈ (8V_Pπ²/μ_FK²a₁₁₁²)cosech(π²/μ_FKa₁₁₁) (1806.11002 Eqs. (2), (6) [FT]).
  E_mig is µeV in FK and meV atomistically (same source).
- *Mass:* the translation mass M_cr = mΣ_n(∂u_n/∂z₀)² = 2μ_FKa₁₁₁m/π² (C10a) equals E₀/c_s² identically (C10c). This is the **standard sine-Gordon /
  Frenkel–Kontorova kink rest mass** (O. M. Braun, Yu. S. Kivshar, *The Frenkel–Kontorova Model*, Springer 2004; A. M. Kosevich, *The Crystal Lattice*,
  Wiley 2006; refs [3], [1] of 1806.11002) [UNVERIFIED page numbers]. It is re-derived here, **not new**.
- *W [E]:* the inputs mix models. M_cr from FK at μa = 0.5 (0.10 m_W) is combined with the atomistic E_mig = 1 meV, which FK itself does not give
  (A§1.8). As a Mathieu problem (depth/E_rec = 6.8), the ground band width is **0.024 meV ≈ 0.28 K** (C10d; both referees, 0.024–0.03 meV). v1's
  "(sub-)meV band" is withdrawn.
- *Coherence at mK is [C],* because three effects remain:
  - bulk α-W has T_c ≈ 15 mK, so it is normal at 20–100 mK and the electron bath α_ohm (G-T1) acts;
  - polaron band narrowing is not estimated;
  - the parent vacancy's interaction φ exceeds the band within R₀ = a_lat(V₀/Δ)^{1/n} (cond-mat/0310283 Eq. (20) [FT]; confinement criterion Eq. (17)),
    ≈ 34 a_lat for n = 3, V₀ ≈ 1 eV [E, assumed elastic interaction constant], Δ = 25 µeV, so the crowdion is localised near its vacancy.
- *Prior work* (cited, not read): Arakawa et al., "Quantum de-trapping and transport of heavy defects in tungsten", Nat. Mater. (2020) [UNVERIFIED, title
  via REF-A]; Derlet, Nguyen-Manh, Dudarev, PRB 76, 054107 (2007); Dudarev, Phil. Mag. 83, 3577 (2003) [UNVERIFIED].
- *Al:* ⟨100⟩ dumbbell, migration ≈ 0.1 eV [UNVERIFIED]. λ_P ≈ 25 (C14e) is at the window edge; see §4.2. Bulk Al is superconducting at mK
  (T_c = 1.2 K), so its electron channel is frozen.

**3.3 Light interstitials [E].** H in Nb: λ_P ≈ 4.1 (C14e). Trapped H forms TLS (1610.03974 Eqs. (9)–(11) [FT]).

**3.4 Spec.** As in v1: DFT supercells for E^{loc}_D, J^{dfn} (RPMD/instanton splittings), 𝔣^{def,loc}; NEB Peierls profiles; 1D Mathieu band; ~10⁵ CPU-h
per material. Add: polaron narrowing from the phonon-dressed hopping, e^{−Σ_kS_HR,k}, and strain-disorder maps (Eq. (17) criterion).

---
## 4. Defect kinetics at mK

**4.1 General hop rate [D].** A hop i → j releases ε_ij and has tunnelling element Δ_ij = ω_well e^{−λ_ij}.
- **λ convention (A#9, B C-7):** the Phillips/Jäckle λ_P = (d/2ħ)√(2M_effV), as in 2103.06977 §II [FT] and 1610.03974 Eq. (13) for two intersecting
  harmonic wells (λ₀ = V/E₀ = Mωd²/4ħ).
  - 1705.01108 Eq. (7) (d√(2MV)/ħ) is 2λ_P. A quartic barrier gives (4/3)λ_P.
  - 𝒮_inst(T → 0) = 2λ holds when λ is the true WKB integral.
- *Notation:* ω_well is the well frequency (NOTATION's ω₀ is the Einstein frequency); the attempt rate is Γ_att (WP5 row).
- *Bath:* ½σ_zΣλ^{sb}_kB_k, J^{sb} ≡ πΣ(λ^{sb}_k)²δ(ω − ω_k) = J_ph + J_el + J_loc, with

  J_ph = (ω³/πρ)(γ_l²/c_l⁵ + 2γ_t²/c_t⁵),   J_el = 2πα_ohmω,   J_loc = πΣ_kS_HR,kω_k²δ(ω − ω_k) (local/optical accepting modes).                         (4.1)

  Golden rule in Δ (NIBA), a WP5-v3 Theorem C instance:

  Γ_{i→j} = (Δ_ij²/4)∫dt e^{iε_ijt}e^{−𝒬(t)} = (πΔ_ij²/2) A_T(ε_ij),   𝒬(t) = (1/π)∫dω J^{sb}ω⁻²[coth(ω/2T)(1 − cos ωt) + i sin ωt],                  (4.2)

  where A_T is the finite-T Franck–Condon line shape of the bath.
- **Energy convention (coordinator decision, campaign-wide; R12):** E^{conf}_i and ε_ij = E^{conf}_i − E^{conf}_j are **configurational** (classical minima
  of E^ad_0, as WP5-v3 defines E_st). The quantum energy actually released by a hop is ε_ij + ΔZPE_ij, ΔZPE_ij = ZPE_i − ZPE_j of the local modes
  (~10–100 meV for interstitials). ΔZPE is carried as an explicit correction in the phonon reservoir ℋ_ph, never in E_st. The argument of A_T in (4.2)
  is the quantum release ε_ij + ΔZPE_ij.

*Limits:*
- **(a) One phonon (Jäckle):** Γ₁ = (Δ_tun/E)²J_ph(E)coth(E/2T)/2 = 2103.06977 Eq. (7) (C3a,b) = 1610.03974 Eqs. (4)–(5) (C3c).
  - Branch ratio transverse:longitudinal = 2(γ_t/γ_l)²(c_l/c_t)⁵ ≈ 64(γ_t/γ_l)² (A#11).
- **(b) Metals (Black):** Γ₁ = πα_ohmΔ²coth/E (C6c,d) = 2103.06977 Eq. (8) with W_el² = 4α_ohm, and 2009.03804 Eq. (4) with **α_ohm = 4K** (C6e).
  - Superconducting case: × 2/(1+e^{Δ_BCS/T}) (2103.06977 Eq. (9), E ≪ Δ_BCS).
- **(c) Finite ohmic coupling:** (4.3) of v1, k_f = (Δ²/4ω_co)(2πT/ω_co)^{2α−1}|Γ(α + iε/2πT)|²e^{ε/2T}/Γ(2α) (C6b, numerical quadrature of (4.2)).
  - It equals cond-mat/9409105 Eqs. (8)–(9) at ε = 0 (C6a). The rate ∝ T^{2α−1}, anti-Arrhenius.
  - *Coherence criterion (A§1.9, restated from the same source's Eq. (10) [FT]):* coherent motion requires Δ̃₀(T) = Δ₀(Θ/ω_co)^α[Γ(1−2α)cos πα]^{1/2}
    to exceed γ₀/2, γ₀ = αΘ, Θ = 2πT (underdamped form of Eq. (10); R12, VER-B N2). Otherwise the motion is incoherent hopping.
- **(d) Arrhenius:** 2409.02820 Eq. (1) with κ = 1 and classical harmonic Z gives Vineyard (WP5-v3 (W12)) (C7a). Wigner κ_W is the first term of κ_PB
  (Eqs. (2)–(3)) (C7b). κ_PB diverges at T_× = ω_bar/2π. Instanton (Eq. (4)) applies below T_×.
- **(e) Band defects:** D_T ∝ T⁻⁹ (cond-mat/0310283 Eq. (12) and its text, "D ∼ 1/(N_phσT²)") [D, sketch]; D ∝ 1/(xσ) (Eq. (11)).

**4.2 eV releases and the mK window (A#9, A§1.10, B C-7) [D for the criteria; E for numbers].** For ε ≫ ω_D there is no one-phonon δ(ε − ω), so A_T(ε)
decides the rate.
- *Weak coupling* (S = Σ S_HR,k ≲ 1, genuine two-state hops): the energy-gap law. At T ≪ ω_p, A(ε)ω_p = e^{−S}S^p/p! with p = ε/ω_p.
  - Example: ε = 1 eV, ω_p = 60 meV, S = 1 gives 1.0×10⁻¹⁵, an extra Δλ ≈ 17 in the exponent (C15a).
- *Strong coupling* (the reaction coordinate itself accepts ε; reorganisation E_reorg = ΣS_kω_k ~ ε): A_T is a Gaussian centred at E_reorg with variance
  ΣS_kω_k² (C15b), so there is no gap suppression near ε ≈ E_reorg.
  - Then the two-state reduction is not controlled. The rate is the T → 0 instanton (2409.02820 Eq. (4)) on the full PES with the product continuum
    explicit [D, sketch].
- *Window:* relaxation within t_obs requires

  2λ_P + ln[1/(ω_well A_T(ε))] ≲ ln(Γ_att t_obs).                                                                                                    (4.3)

  For **ε ~ meV** (where ω_well A_T ≈ 1) this reduces to λ_P ≲ 23.6 (Γ_att = 10¹³ s⁻¹, 1 yr), i.e. V ≲ 166 meV(1 Å/d)² for a Si-mass entity (C14d).
  For one-phonon relaxation A_T = J_ph(ε)/(πε²) ∝ ε, so at ε ~ 10 µeV the bound is ≈ 2 lower in λ_P (R12, VER-A N3).
- *Revisited verdicts (λ_P from C14e; V, d inputs [E]):*
  - H/Nb, λ_P ≈ 4.1: relaxes.
  - Si close pair (d = 1.5 Å, V = 0.1 eV): λ_P ≈ 27.5 (harmonic) to 37 (quartic), with ε ~ eV.
  - Al SIA, λ_P ≈ 25.
  - **v1's "frozen" verdicts for Si close pairs and Al are withdrawn: OPEN [E].** They require V, d, the barrier shape and S_HR,k of the actual path (spec
    §4.6). Weak-coupling eV releases add Δλ ~ 10–20 (likely frozen); strong-coupling ones do not.

**4.3 Correlated recombination [D / C].**
- (a) *3D hopping:* eventual capture r_c/r₀; capture-time tail ∝ t^{−3/2} (C9c,d). This stands.
- (b) *1D crowdion (B C-11, withdrawn → [C]):* near its own vacancy the strain energy gradient exceeds the band width (§3.2), so motion is phonon/electron-
  assisted descent, i.e. drift-dominated. The arrival-time distribution is peaked (≈ d/v_drift), not the force-free t^{−3/2}. The force-free first-passage
  density (C9a,b) applies only beyond ~30 a_lat, where the field is below Δ_dfn.
- (c) Uncorrelated (bimolecular) recombination: (1 + t/t₀)⁻² [D, sketch].
- Discriminants: 1/t (broad λ), t^{−3/2} (3D correlated), peaked (1D drift), exponential (single path).

**4.4 Energy per event [D].**
- (a) ε < ω_D: one phonon at ε, branch ratio as in §4.1(a). In normal metals a fraction J_el/(J_el + J_ph) goes to electron heat.
  - Photon/phonon ratio = (8π/3)αd²ρc_t⁵/γ² ≈ 5×10⁻¹⁴ (one transverse branch; C14h).
- (b) ε ≫ ω_D: ⟨n_k⟩_ε = S_HR,kA(ε − ω_k)/A(ε) (C12). This holds **at T = 0, i.e. for T ≪ ω_k** (A#11, B#17), always true at mK for ω_k ≳ 1 meV up to
  e^{−ω_k/T}.
  - At T ~ ω_k the generating function has absorption terms and this simple form fails.
  - Radiative branch: ZPL e^{−S_HR} + sideband with the same A; branching from WP4-v3 §6 inputs. The qualitative NaI(Tl) context is 2210.04128 [FT].

**4.5 Heat-release limit [D].** Q̇ = (π²/24)P̄_STMV(T₁² − T₀²)/t (C8) = 1610.03974 Eq. (6) [FT], for Γ_max⁻¹ ≪ t ≪ Γ_min⁻¹. Freezing at T*: its Eqs. (7)–(8).

**4.6 Computation specification (kinetics) (A#12, A§5 applied).**
- *Paths:* NEB on the WP5-v3 §3.4 MLIP end states, then multidimensional λ by ring-polymer instantons (corner cutting), with 50 paths checked against DFT.
  The λ_P convention is recorded.
- *Bath:* J_ph from γ^{def} (finite strain); **J_loc from S_HR,k of the path's local/optical modes** (constrained relaxation + supercell phonons, as WP4-v3 §6).
- *Rates:* (4.2) with A_T by FFT of e^{−𝒬}. For ε ≫ ω_D and E_reorg ≳ ε, use the T → 0 instanton with an explicit product continuum instead.
- *α_ohm (G-T1)* is a **prerequisite** for every normal-metal host, not a nuisance.
- *KMC:* (W12) with these Γ_ij at 10–100 mK, 10⁶ seeds. *Outputs:* ℛ_rel(E,t,T), with nuisances θ_λ (convention and shape, a ×4/3–×2 band in the
  exponent) and θ_S (S_HR,k).
- *Cost:* ~10⁴–10⁵ GPU-h.

---
## 5. Defect creation by DM: interface to WP5-v3 and WP7-E

**5.1 Seeds and classes.** Seeds come from WP5-v3 (W9), (W10) (P_FP, E_d) and §3.2 (E_st). ER cannot displace atoms (WP5-v3 §4).
| host | interstitial configuration | mK mobility | release law |
|---|---|---|---|
| W, Mo | ⟨111⟩ crowdion | band 0.024 meV [E]; coherence [C]; normal-metal bath above 15 mK | drift-dominated correlated recombination [C] |
| Al | ⟨100⟩ dumbbell | OPEN (λ_P ≈ 25) [E]; electron channel frozen (SC) | (4.2)/(4.3) |
| Si, Ge | ⟨110⟩ split, T, H sites [UNVERIFIED] | OPEN (λ_P 27–37, eV releases) [E] | 1/t + t^{−3/2} (3D) |
| amorphous films | rearranged pockets / new TLS [C] | TLS-like | 1/t (4.5) |

**5.2 Stored-energy distribution [D, definition].**

  p_st(E_st | E_R, r̂_R, T) = Σ_cP(c|E_R, r̂_R) p_c(E_st).                                                                                                (5.1)

The released / unreleased-by-t_obs split (§5.3 naming) is now by the **computed** Γ(ε, λ_P, S_HR) of (4.3) on t_obs, not by v1's λ ≤ 24 cut (A#12, B#19).

**5.3 Release kernel and the release-path sum rule.** Define 𝒦^{rel} as the expected hop-event density per seed of class c (started at E^{conf}_c):

  𝒦^{rel}(E,t|c,T) ≡ Σ_{i≠j} N_i(t|c) Γ_ij(T) δ(E − (E^{conf}_i − E^{conf}_j)),   N_i from WP5-v3 (W12) with 𝔰_i = δ_{ic}δ(t).                             (5.2)

Its normalisation ∫∫𝒦 = ⟨N_hop⟩ is the expected number of hops, not 1. The single-path form Σ𝒫Γe^{−Γt}δ(E − ε) is its one-hop special case.

**Theorem T-1 (release-path sum rule; closes WP7-E IF-E2) [D].**

  ∫₀^{t}dt′∫dE E 𝒦^{rel}(E,t′|c,T) = E^{conf}_c − Σ_iN_i(t|c)E^{conf}_i,   hence at t_obs:   Σ_path𝒫_pathε_path = E_st − ⟨E_st^{unrel}(t_obs)⟩ ≡ E_st^{rel}.    (5.3)

*Proof.* From (W12), d/dt Σ_iN_iE^{conf}_i = Σ_{ij}(Γ_jiN_j − Γ_ijN_i)E^{conf}_i = −Σ_{ij}Γ_ijN_i(E^{conf}_i − E^{conf}_j) = −∫dE E𝒦^{rel}. Integrate over
t. ∎ No detailed balance and no rate model are needed (C16, an exact absorbing-chain check).

WP7-E (E6) therefore holds as an **identity**, not an external constraint, provided five conditions hold:
- (i) every hop is in 𝒦^{rel}, uphill hops with ε < 0 (heat absorbed);
- (ii) p_st and the path tables use one E^{conf} table from the same end states;
- (iii) photon-branch releases are kept in E, routed to E_esc/E_sig by WP7-E;
- **(iv) total probability is conserved, Σ_iN_i(t) = 1: a closed, linear, single-seed chain** with no loss to unlisted states. Bimolecular or
  uncorrelated recombination with other defects ((1 + t/t₀)⁻², §4.3(c)) is outside the per-seed kernel and is excluded; it needs the pair-state space;
- **(v) energies are configurational** (§4.1 energy convention): E^{conf}_i and ε_path are classical configuration-energy differences, and the
  zero-point change ΔZPE of every hop is carried as an explicit correction in ℋ_ph, not in E_st or 𝒦^{rel}.

*Time-dependent rates.* The proof uses only the master equation at each instant, so T-1 holds unchanged for time-dependent (stimulated) rates Γ_ij(t),
e.g. during a heat pulse or under illumination (C16b).
*Normalisation.* If WP7-E uses a normalised kernel 𝒦̂^{rel} ≡ 𝒦^{rel}/⟨N_hop⟩ (unit time–energy integral), the sum rule reads ⟨N_hop⟩∫∫E𝒦̂^{rel} = E_st^{rel}.
*Naming (R12, VER-B §4).* E_st^{unrel}(c,T,t_obs) ≡ Σ_iN_i(t_obs|c)E^{conf}_i − E^{conf}_0 is the stored energy **unreleased by t_obs**; it includes
populations still relaxing. "Frozen" is reserved for the t_obs → ∞ limit, E_st^{frz} ≡ E_st^{unrel}(t_obs → ∞). In (5.3) and WP7-E (E6), E_st^{frz} at
finite t_obs is to be read as E_st^{unrel}(t_obs). E_d never enters (WP7-E Theorem E-1).

**5.4 Hand-over and calibration (B C-13).** WP7-E receives {p_st, 𝒦^{rel}, dN/dω′, photon fraction} per class, with (5.3) and the τ string.
- 𝒦^{rel}(·|c,T) is seed-independent per class, but P(c|E_R, r̂_R) and the local strain are not.
- So a calibration fixes the DM case only with **near-threshold recoils** (E_R ≲ few E_d), not keV cascades.

**5.5 Spec.** v1 §5.4 (WP5 partition tables, class labelling, λ per exit path), with the §4.6 changes. Cost dominated by WP5 (10⁴–10⁵ GPU-h) + 10⁴ GPU-h.

---
## 6. Exact remaining gaps
- **G-T1.** No first-principles α_ohm (crowdion/H/TLS in W, Al, Nb, WSi). It needs DFT scattering phase shifts of the two configurations (Yamada-type
  α_ohm = Σ_l(2l+1)(δ_l^R − δ_l^L)²/π² [UNVERIFIED]). It is a prerequisite for normal-metal hosts (bulk W above 15 mK).
- **G-T2.** S_HR,k, barrier shape and λ_P of real eV-release paths (Si/Ge close pairs, Al SIA). Also athermal ionisation-driven migration (X-sector; WP3/WP5
  R3).
- **G-T3.** P̄_STM, γ^{def}, 𝐩^{def} of specific films; STM universality is assumed.
- **G-T4.** Interacting TLS, spectral diffusion, avalanches [C] (WP5-v3 R4). This return does not close CATALOG-B G12.
- **G-T5 (narrowed).** The 1/𝔔_ph factor is settled (§2.3(a)). What remains: Andreev–Lifshitz (1969) is not on arXiv and is quoted via
  cond-mat/0310283 only.
- **G-T6.** Crowdion polaron narrowing and strain localisation (W); fcc Al SIA barrier and 1D cluster glide (DFT).
- **G-T7.** The DM–TLS priority search (A§4) is UNRESOLVED.

## 7. Checks (code/WP7-T-v2/checks.py, 51/51 PASS after the R12 clean-up)
- Kept from v1: C1–C3c; C4a,b; C5a,b; C6a–d; C7a,b; C8; C9; C10a,b; C11; C12; C13b; C14a, c, g, h.
- New or changed:
  - C4c: 2103.06977 Eqs. (4)+(12)+(13)+(15) chain.
  - C5c: sign from an explicit force pair and E_int = −D:S.
  - C5d: Lorentzian = (π/η)δ + Hadamard fp + O(η).
  - C6e: α_ohm = 4K, W_el² = 16K.
  - C10c: M_cr = E₀/c_s² (FK kink mass).
  - C10d: Mathieu band 0.0246 meV.
  - C14b, b′: (m/μ)², core term (exact sum), one boosted-SHM halo, consistent P̄.
  - C14d,e: λ_P window and estimates.
  - C15a,b: energy-gap law vs the Gaussian strong-coupling limit.
  - C16: Theorem T-1 on an absorbing chain; C16b: T-1 with time-dependent rates and ΣN_i = 1 (R12).
  - C5a, C5b relabelled: they test the contraction only; the physical sign is C5c (R12, VER-B N1).
- Removed: C3d, C4c (old), C7c, C13a, C14f, C14c (R12).

---
## 8. Closing table (one row per referee item)
| Item | Verdict | Action (location) |
|---|---|---|
| A#1, B#1 | SWC | K=def withdrawn; K = −, 𝒳 = −, ref=def(·), scr=DFPT with derivation, conv=DC (§1.1, §1.5) |
| A#2, B#4, C-4 | SWC / FALLS | pole rule rewritten with Hadamard fp, (π/η)δ and Fano δ to the cascade (1.3), C5d; §2.7 implements fp |
| A§1.3, B C-8 | correction | **rebutted with derivation**: the GS vertex δρ_κ is already DFPT-screened, so ε_e⁻¹ would double count (§1.5); q ≳ q_BZ weight caveat applied |
| B C-9 | correction | host sign fixed: v1 sign wrong, now +2w q̂γq̂ (C5c, (1.2)) |
| A#3 | STANDS | quasi-elastic σ_z part stated and dropped; one-sign STM convention stated (§1.2, §2.2) |
| A#4, B#6, B#7, C-1 | SWC, CONFIRMED | 1/𝔔_ph source ½ settled via 2103.06977 Eqs. (4), (12), (13), (15) (C4c); G-T5 narrowed |
| A§2, C-6 | misquote | tanδ: AlOx 1.6×10⁻³ (no T), a-Si:H 2.5×10⁻⁵ at 4.2 K (saturated) (§2.3(d)) |
| A§1.5 | double tanh | (2.3) written with tanδ₀·tanh only |
| A#5, B#8, C-2, C-3 | SWC | (1+m_χ/m_e)²; window q ≪ min(q_×, 1/r_core); core term included incoherently; number 2.4×10⁻² [E, ×3] (§2.4, C14b); R12: 3.7×10⁻² with one halo (§9) |
| A§1.6 P̄, C-14 | inconsistency | P̄ = 8.6×10⁴⁴ J⁻¹m⁻³ consistent with C_TLS, γ (C14b′); band ω ≲ 0.1 meV; sampling ≳ 10⁸ pairs (§2.7) |
| A§1.6 minor | — | ω/⟨v⟩² threshold; "§2.3(a)" reference fixed |
| A#13, B#9 | SWC | ≈ 2×10⁻¹⁹ with σ̄_e, m_χ, Γ_↓ stated (§2.5) |
| A#6, B#10, C-10 | SWC | dispersion "quoted"; f-sum wording fixed; Σw_i ≤ Δ_dfn (§3.1) |
| A#7, B#11, C-5 | novelty REFUTED | "new" dropped; Braun–Kivshar/Kosevich credited; C10c identity (§3.2, L31) |
| A§1.8, B#12, C-11 | SWC → [C] | W band 0.024 meV (C10d); bulk W normal above 15 mK; polaron and strain localisation; coherence [C]; prior literature cited (§3.2) |
| B#16, C-11 | SWC | 1D t^{−3/2} withdrawn (drift-dominated, peaked); 3D kept (§4.3) |
| A#8, B#13, C-12 | STANDS | α_ohm = 4K (C6e); coherence criterion restated from cond-mat/9409105 Eq. (10) (§4.1(c)) |
| A#9, A§1.10, B#15, C-7 | SWC | Phillips λ_P adopted; energy-gap law vs strong coupling; window (4.3); frozen verdicts withdrawn → OPEN (§4.2) |
| A#10, B#18 | STANDS | unchanged (§4.3, §4.5) |
| A#11, B#17 | SWC | (4.4) restricted to T ≪ ω_k; transverse factor 64(γ_t/γ_l)²; C14f deleted (§4.1(a), §4.4) |
| A#12, A§5, B#19 | SWC | J_loc (S_HR,k) added to the bath; computed-Γ class split; α_ohm prerequisite (§4.6, §5.2) |
| B C-13 | overclaim | calibration needs near-threshold recoils (§5.4) |
| B#20 | §2.7 INSUFFICIENT | fp, sampling and vertex fixed (§2.7) |
| B#21, C-15 | checks | vacuous checks removed; new non-trivial checks; 51/51 (§7) |
| A§2 Γ₂ location | minor | "text above Eq. (15)" (§2.1) |
| A§6 notation | — | ω₀ → ω_well and Γ_att; 𝔣 → 𝔣^{def} (𝔣_Lin clash); 𝒳 rung only |
| A§4 priority | UNRESOLVED | no novelty asserted (header, G-T7) |
| A§5 IF-T8 | wording | no CATALOG-B G12 closure claimed (G-T4, IF-T8) |
| coordinator: IF-E2 | new | Theorem T-1 (5.3), C16 |

---
## 9. R12 clean-up (VER-WP7-T-A, VER-WP7-T-B; coordinator; edited in place)
| Item | Change (location) |
|---|---|
| Screening rebuttal (A §2, B §2) | accepted by both; scope added: δρ_κ = full finite-q improper DFPT response incl. G = 0, not rebuilt from Z* (§1.5) |
| T-1 condition (iv) (A §3, B §4) | Σ_iN_i = 1, closed linear single-seed chain; bimolecular excluded (§5.3) |
| T-1 normalisation (coordinator) | ⟨N_hop⟩∫∫E𝒦̂^{rel} = E_st^{rel} for a unit kernel (§5.3, IF-T3) |
| T-1 time-dependent rates (coordinator) | stated; C16b (§5.3, §7) |
| "frozen" at finite t_obs (B §4) | renamed E_st^{unrel}(t_obs); frozen = t_obs → ∞ (§5.3, (5.3), Symbols) |
| Energy convention, condition (v) (coordinator, campaign-wide; A §3 (v)) | configurational energies; ΔZPE carried explicitly in ℋ_ph, not in E_st; A_T argument ε + ΔZPE (§4.1, §5.3) |
| A N1 | incoherent sum exact: Re(a*B) ≡ 0 for every orientation (core imaginary, host real about x̄); PV cross term vanishes in the window (§2.4) |
| A N2, B 3(i) | one halo (boosted Maxwellian, v_E = 250.5 km/s): ⟨|v|⟩ = 358 km/s, R_core = 2.6, host 1.0×10⁻², total 3.7×10⁻² [E, ×3] (§2.4, §0 row 6, C14b) |
| A N3 | λ_P ≲ 23.6 only for ε ~ meV; ≈ 2 lower at ε ~ 10 µeV (§4.2) |
| A N4 | radius R₀ = a(V₀/Δ)^{1/n} is cond-mat/0310283 Eq. (20); V₀ ≈ 1 eV stated [E]; ≈ 34 a_lat (§3.2) |
| A N5 | IF-T9 declares the signed (non-PSD) exported seed weight; WP5 must not clip |
| B N1 | C5a/b relabelled (contraction only; sign in C5c) |
| B N2 | coherence Δ̃₀ > γ₀/2 (§4.1(c)) |
| B N3, A (C14c) | C14c removed |
| B N4, B 3(ii) | §2.4 lists the rigid-ion core, macroscopic-screening and halo caveats |
| Checks | 51/51 PASS (C14c removed, C16b added) |

---
## Symbols introduced/used (against NOTATION v4 + R9 rows)
| Symbol | Meaning | Status |
|---|---|---|
| Δ_as, Δ_tun, E_TLS | TLS asymmetry, tunnel splitting, splitting | new (source ε, Δ₀ clash) |
| 𝔣^{def}_s, 𝔣^{def,core}_s, 𝔣^{def,loc}_s | defect vertex (1.1)–(1.2); core; localised form factor | new (decoration mandatory: 𝔣_Lin taken) |
| γ^{def}, 𝐩^{def}, D (force-dipole tensor, local §1.3) | deformation potential (δΔ_as = 2γ:S); dipole; elastic dipole (D_R − D_L = −2γ) | new (D is local to §1.3; D^n, D_κ are distinct) |
| w_e, w_N, w_c | acoustic species weights | new |
| G(q,ω), x, η, B, a (local to (1.3)) | acoustic propagator; pole variable; width ωΓ_ph; host/core amplitudes | local |
| P̄_STM, C_TLS, tanδ₀, tanδ_TLS, 𝔔_ph, 𝔔_el, ℓ_TLS | STM density (one-sign), tunnelling strength, loss tangents, quality factors, TLS phonon mfp | new |
| Γ₁, Γ₂, Γ_φ, Γ_↓, Γ_↑, Γ_ph | TLS rates; phonon width | new |
| J^{dfn}, Δ_dfn, ϖ, E^{loc}_D, ε_D, m^{dfn} | defecton parameters | new |
| a₁₁₁, μ_FK, V_P, M_cr, E_mig, E_rec | crowdion (FK) parameters; M_cr = FK kink mass | new |
| λ_ij, λ_P, ω_well, d, M_eff | tunnelling exponent (Phillips convention), well frequency, distance, mass | new (λ with subscript; ω₀ avoided) |
| λ^{sb}_k, J^{sb}, J_ph, J_el, J_loc, 𝒬(t), A_T(ε) | bath couplings and spectral densities; overlap exponent; finite-T FC line shape | new |
| α_ohm, ω_co | ohmic coupling (= 4K₂₀₀₉), cutoff | new |
| p_st, c (class), 𝒦^{rel}, 𝒦̂^{rel}, ⟨N_hop⟩, E_st^{rel}, E_st^{unrel}(t_obs), E_st^{frz}, ΔZPE_ij | stored-energy distribution, class, hop-event kernel (5.2) and its unit-normalised form, hop number, released / unreleased-by-t_obs / frozen (t_obs → ∞) stored energy, zero-point change of a hop (carried in ℋ_ph) | new (E_st^{frz}, E_st^{rel} as in WP7-E; E_st^{unrel} new) |
| used unchanged | E^{conf}_i, Γ_ij, Γ_att, T_×, ω_bar, E_bar, 𝒮_inst, N_i, 𝔰_i, ℛ_rel, E_st, E_d, P_FP, S_HR,k, 𝓃_D, Z*_κ, δρ_κ, c_κ, F^M_κ, C^{el}_ij, Δ_BCS, κ_mix, η, ξ, σ̄_e | NOTATION rows |

## Interface flags
| # | Owner / user | Item | Action |
|---|---|---|---|
| IF-T1 | CONVENTIONS §11, WP6 | defect sector in τ | `ref=def(STM\|band\|cr)` metadata only; K, 𝒳 unchanged; scr=DFPT |
| IF-T2 | WP5-v3 §4, (W12) | sub-T_× rates | use (4.2) with J_ph + J_el + J_loc; energy-gap / strong-coupling split; window (4.3) |
| IF-T3 | WP7-E | release model | Theorem T-1 (5.3) makes (E6) an identity under (i)–(v); 𝒦^{rel} = hop-event density (5.2), ∫∫𝒦 = ⟨N_hop⟩ (normalise by ⟨N_hop⟩ if a unit kernel is used); E_st^{frz} at finite t_obs → E_st^{unrel}(t_obs); ΔZPE in ℋ_ph; closes IF-E2 |
| IF-T4 | NOTATION | new rows | §Symbols "new"; 𝔣^{def} decoration; λ_P convention |
| IF-T5 | WP2-v3 (1.2), WP4-v3 §6 | defect vertices | host term with corrected sign (1.2); pole rule (1.3) for the [6.1] responses |
| IF-T6 | WP7-D | dark photon on TLS | (2.3) is the incoherent limit; tanδ₀ input caveats |
| IF-T7 | WP4-v3 §4.5 | films | ℓ_TLS and delayed release in the film phonon budget |
| IF-T8 | LIMITS | rows | L25–L32 below (numbers provisional); no closure of CATALOG-B G12 |
| IF-T9 | CONVENTIONS §10, WP5 | DC at phonon poles | (1.3) extends the DC rule (fp + PV to the response; δ parts to the cascade) to phonon-mediated defect vertices. **The exported seed weight (π\|B\|²/η)δ − 2πIm(a*B)δ is signed (not PSD)**, as allowed by O4-d7 / CONVENTIONS §13 item 20; WP5 must not clip negative weights |

## Proposed LIMITS rows
| # | τ / chain | source formula [FT] | status |
|---|---|---|---|
| L25 | (2.1)–(2.2) driven by classical strain/E field, ref=def(STM) | 1705.01108 Eq. (20) (T → 0, D₀ → P̄; phonon form = ½ of 2103.06977 Eqs. (4)+(12)+(13)+(15) and of the derived value, settled) | DERIVED ✎ |
| L26 | (4.2), one boson: Jäckle (J_ph), Black (J_el), × 2/(1+e^{Δ_BCS/T}) | 2103.06977 Eqs. (7)–(9); 1610.03974 Eqs. (4)–(5); 2009.03804 Eq. (4) with α_ohm = 4K | DERIVED (2103.06977 Eq. (2) text ✎) |
| L27 | (4.2), ohmic scaling limit; T^{2α−1}; coherence Δ̃₀ > αΘ | cond-mat/9409105 Eqs. (8)–(10) | DERIVED |
| L28 | T > T_×: TST → Vineyard; Wigner; κ_PB pole; instanton below | 2409.02820 Eqs. (1)–(4) | DERIVED |
| L29 | flat P̄(Δ_as, λ): Q̇ = (π²/24)P̄V(T₁² − T₀²)/t | 1610.03974 Eqs. (1), (6)–(8) | DERIVED |
| L30 | (3.1) ref=def(band); D_T ∝ T⁻⁹, D ∝ 1/(xσ); localisation Eqs. (17)–(18) as leading correction | cond-mat/0310283 Eqs. (1)–(4), (7), (11)–(12), (17)–(18) | DERIVED (kernel) / [D, sketch] (T⁻⁹) |
| L31 | crowdion FK profile, Peierls barrier, kink mass (textbook; Braun–Kivshar) | 1806.11002 Eqs. (2), (3), (6) | DERIVED ✎ (not new); W numbers [E] |
| L32 | WP0 (3.5)–(3.6), L9b with ε ⊃ TLS: ℛ_A′ = ρ_φκ²tanδ₀tanh(m_φ/2T)/(ρ_Tε_r) | 1705.01108 Eq. (20) (electric) via L25 | DERIVED ✎ (single tanh; tanδ input caveats) |
