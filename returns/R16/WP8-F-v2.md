# R16 / WP8-F-v2: figures of merit per interaction channel (standalone revision after R14)

Agent CW7 (brief briefs/R16/CW7.md, row LE-21; with LE-155, LE-156, LE-157 of the same package). This file replaces returns/R13/WP8-F.md as the
authoritative WP8-F text (R13 stays the historical record). It absorbs referees/R14/REF-WP8-F-A.md (F1–F19, §B), REF-WP8-F-B.md (required corrections
1–13) and the WP8-F rulings F-a…F-i and D-11, D-12, D-13, D-17 of returns/R14/WP5-AUD.md §5.2/§6; the closing table is §9. Inputs as R13 plus WP5-v4,
WP5-AUD, GAP-EF, WP8-U-v2 (this round). Numeric checks of the corrections: code/CW7/checks.py (CW7-C20–C27; the R13 code/WP8-F/checks.py 39/39 still
passes and is not edited). Tags per CONVENTIONS §12. **1807.10291 is cited with PDF v1 page and equation numbers throughout** (the arXiv-HTML numbering
is shifted: PDF Eqs. (21)–(22) = HTML (31)–(32)). **Yield rows:** the R13 "(prov.)" flag is **lifted** — WP5-AUD §5.2 released them with the text
corrections F-a…F-i, which are applied below (IF-F3 answered). Status: CLAIMED (revised after R×2); the corrected statements carry the referees' checks.

---
## 0. Results at a glance (one row per FOM class; corrected)
| Class | Rate FOM 𝓡 (material functional × kinematic factor) | Edge set by the material | Screening | Dominant m_χ [E] |
|---|---|---|---|---|
| ER-ρ (O₁) | (1/ρ_T)∫dω∫dq q³F_DM²η L(q,ω)/(2πα) | (3.1′) of WP6-v3; floor 2E_x/v_max² | L with ε_e, = total ε at clamped nuclei or ω ≫ ω_max (the ER window) | 0.2 MeV–1 GeV |
| ER-light | (1/ρ_T)∫dω L(q→0,ω)·η̄ ln(q₊/q₋) [D under slow variation; E above ≈ 0.5 MeV in Si] | same | optical ELF | 0.2–10 MeV |
| ABS | A′: L(0,m_φ)/ρ_T; ALP (e): m_φ²ε₂/ρ_T; ALP in B₀: g²B₀²L_∥/(ρ_Tm_φ²); scalar: −Im R̃_{𝒯𝒯}(0,m_φ)/ρ_T (§2.2, closed form) | supp ε₂ | A′ total ε; ALP none at LO; scalar: none for non-polar point groups | m_φ = ω |
| NR-1ph | πqΣ_ν(q̂·ê_ν)²/(m_u²c_ν(q̂)) per mass, A-free; light mediator all m_χ, heavy mediator m_χ ≲ 0.1–1 MeV | (2.3b) | R_NN | 10 keV–1 MeV (heavy) |
| NR-optical (in 1BZ) | O(q⁴a²) intra-cell-phase term, composition-dependent (2205.02250 Eq. (31)) | 2ω_LO/v_max² | R_NN | 0.1–10 MeV |
| NR-mph / impulse | Poisson tail with 2W_κ = (q²/2M_κ)⟨ω⁻¹⟩; impulse ∝ A (far above threshold) | ω_max^ph; √(M_κE_th/2)/v_max | R_NN | 1 MeV–10 GeV |
| POL | Σ_ν(πω_Lν/2)Δ_ν𝒦_ν/ρ_T; ∝ 𝓘_pol/ρ_T only for a band-uniform weight [E otherwise] | 2ω_LO,ν/v_max² | built in | 10 keV–10 MeV |
| MAG | (𝓈_λ/ρ_T)⟨\|F^{mag}\|²⟩ × kinematics | Δ_mag; AFM linear, FM quadratic dispersion (§2.6) | none at SOC = 0 | keV–MeV |
| PAER | (1/ρ_T)∫L^{PA} (ER functional) | E_g + ω_TA(Q*) (Si 0.337 continuum; 0.333 replica) | ε̃⁻¹ + DFPT g + W^{scr} | PAER-only 0.333–0.42, leading to ≈ 0.43, shared to 0.54 MeV (Si) |
| Migdal | Σ_κ𝓠_Mig,κ(ω)/A_cell per mass, 𝓠_Mig,κ ≡ ∫d³k Z_κ(k)²L(k,ω)/(3(2π)³ω⁴) | E_g with impulse onset 17–21 MeV (Si/Ge); kinematic floor 2E_g/v_max² | total ε | ≈ 20 MeV–1 GeV |
| TLS / defects | A′→TLS tanδ₀/(ρ_Tε_r); DM–TLS P̄_STM-weighted; damage E_d | ω ≲ 0.1 meV; E_d | ε_r | keV–MeV; ≳ 100 MeV |
Reach scalars (§3): 𝓩_0 = ∫ϵ(E)𝓻̂_s dE (σ_lim = Z_0/(C_χ𝓩_0MT)); 𝓩_B = [∫dE 𝓻̂_s²/b_bg]^{1/2} (σ_lim = Z/(C_χ𝓩_B√MT)); systematics floor σ_lim → Z f_sys b_bgΔE_ROI/(C_χ𝓡).

---
## 1. General reduction from the master formula
**(1.1) [D]** WP0-v3 (3.4) per unit target mass: dℛ/dω = (ρ_χ/m_χ)(1/ρ_T)∫d³q/(2π)³∫d³v f_χ tr[𝔇ᵀS]δ(ω − ω_q).
**(1.2) Hypothesis added (REF-WP8-F-A F1, -B V1).** With 𝔇 = 𝔇^{(0)} + 𝔇^{(1)}·v_T + v_T·𝔇^{(2)}·v_T (WP6-v3 (1.2)) and the isotropic reduction (I), WP6-v3 (1.4) gives

  dℛ/dω = (ρ_χ/(4π²m_χρ_T))∫q dq [A^{(0)}η(v_min) + A^{(2)}ξ(v_min)],   A^{(0)} = Σ𝔇^{(0)}_abS̄_ab,  A^{(2)} = ½Σtr_T[𝔇^{(2)}_ab]S̄_ab.   (1.2′)

For one operator row with 𝔇^{(0)}_aa = |𝒱_a(q₀)|²F_DM,a²(q) (the R13 symbol c_a is dropped) the **kinematic factors** are 𝒦^{kin,(0)}_a = qF_DM,a²η/(4π²) and
𝒦^{kin,(2)}_a = qF_DM,a²ξ/(4π²), ξ(u) = 2∫_u^∞u′η(u′)du′. Rows with 𝔇^{(2)} ≠ 0 (𝒪₃, 𝒪₇, 𝒪₈, …) are ranked with 𝒦^{kin,(2)}, not η. The rate FOM is
𝓡_a(m_χ) ≡ ∫_{ω≥E_th}dω∫dq 𝒦^{kin}_aS̄_aa/ρ_T at fixed |𝒱_a(q₀)|²; |𝒱|² = πσ̄_e/μ_χe² gives the flux factor **C_χ ≡ ρ_χπ/(m_χμ_χe²)** outside 𝓡.
**(1.3) Edges [D].** m_min = min_q q²/[2(qv_max − E_th(q))] (WP6-v3 (3.1′)); continuum floor 2E_g/v_max² (Si 0.333 MeV with the low-T gap, Ge 0.212), total-S̄
floor 2E_x/v_max². Near-edge log-sensitivity (7/2 + k_tail + p̄_on)·½√(m_min/m)/(1 − √(m_min/m)) at m = 1.05 m_min: **≈ 132 for the continuum edge
(p̄_on = 3), ≈ 101 for the exciton-replica edge (p̄_on = 3/2)** (CW7-C23). The E_th need is therefore ≥ 0.15% (continuum; ≈ 0.2% replica) **within the
validity window Δm/m ≤ 5%** — a needed accuracy, not a sensitivity (REF-WP8-F-A F2, -B V2).

## 2. FOM classes
### 2.1 ER through the loss function
**(a) [D]** S̄_ee = q²L̄/(2πα(1 − e^{−βω})); (2.1a) 𝓡_ER,heavy = (1/2πα)(1/ρ_T)∫dω∫dq q³ηL/(4π²), 𝓡_ER,light = ((αm_e)⁴/2πα)(1/ρ_T)∫dω∫dq ηL/(4π²q).
Light-mediator reduction: 𝓡_ER,light ≈ (·)∫dω L(0,ω)η̄ ln(q₊/q₋) **where η̄ is defined as the dq/q-weighted mean of η(v_min(q,ω))** (a definition, not a derived
constant). It is [D] under slow variation of L for q ≲ q_c(ω); in Si for m_χ ≳ 0.5 MeV more than half of the log sits at q ≳ 1 keV where L(q,ω) ≠ L(0,ω), so
it is [E] there (REF-WP8-F-B V4). **Ceiling [D] (L17)** ∫ωL = (π/2)ω_p²: Z/A ∈ [0.40, 0.50] **for the 12 listed solids**; over solids including hydrides and
heavy metals 0.39–0.56 (Pb 0.396, LiH 0.503, H₂O 0.555; CW7-C26). The heavy-weighted 𝓡 uses ∫L dω, the ceiling ∫ωL dω, so 𝓡_ER,heavy ∝ (Z/A)w_acc⟨1/ω⟩_acc
[E] (REF-WP8-F-B V3). Lindhard metals: L ≈ (πω/2qv_F)(q²/k_TF²)/(1 + q²/k_TF²)²; only the **1/(k_TF²v_F) scaling** of 𝓡 is stated, the q-powers depend on the
ω-range min(qv_F, qv_max − q²/2m_χ) (REF-WP8-F-A F3).
**(c)** L is built with ε_e (electron-only coupling), equal to the total/clamped ε only at clamped nuclei or ω ≫ ω_max (WP0-v3 (5.5)); true in the ER window
ω ≥ E_g (REF-WP8-F-A F4). 1/|ε|² pointwise is not the rate ratio (×1.4–2.5, 2101.08275).
**(d) Thresholds in quanta (WP5-AUD F-a).** Near threshold the event weight is P(N_eh|q,ω) (WP5 (W5)–(W6); WP5-AUD §2 output P_n(q,ω,T); continuous form
CW7 LE-153); the L21 step model is exact only in the forced region. ε_eh and F_eh are asymptotic (≳ 50 eV) and T-dependent beyond E_g(T). Measured charge:
N^{meas} = Σ𝔮_i with F^{obs}_{meas}. Values: Si ε_eh 3.749 ± 0.001 eV, F_eh 0.119 ± 0.002 (5.9 keV, 123 K; 2004.11499 [FT via WP5-v3/v4]); other
survivors: WP8-U-v2 §4.2. Backgrounds: ³H in Si "roughly 124 atoms/kg/day", "0.002 events/kg/keV/day for each day of sea-level exposure", half-life 12.3 y
[FT 2506.06568 p.1]; Ge 75 ± 26 (calc.), measured 82 ± 21 and 76 ± 6 (neutron-only, hence lower limits) [FT 1706.05818 Tables 1–2]; NaI 83 ± 27 (calc.);
full sea-level production tables: WP8-U-v2 §4.4.
**Non-density rows (L3).** j_L screened like n; j_T through LFE; spins unscreened at SOC = 0 (triplet ladder ×1.3–2 near the edge); velocity-dependent rows use
𝒦^{kin,(2)} (1.2′). The 𝒪₈ factor ≥ 12× (IP 20–30) stays UNRESOLVED.
### 2.2 Absorption
**(a) [D]** Γ_net = −(y_φ²/ω)Im R_OO(k_φ,ω) with the photon-reducible part (WP0-v3 (3.5)–(3.6)).
- Dark photon: ℛ_A′ = (ρ_φ/ρ_T)κ_mix²L(0,m_φ); FOM_A′ = L(0,m_φ)/ρ_T; anisotropic: (1/3)Σ_iL_ii, as 1807.10291 Eq. (40) **[FT p.30]** for sapphire.
- ALP–electron: FOM ∝ m_φ²ε₂(m_φ)/ρ_T (Γ ∝ m_a²σ₁ = m_a³ε₂, confirmed by REF-WP8-F-A F5); no in-medium 1/|ε|² at LO; SOC split ≲ 2% Si, ≲ 10% Ge.
- **ALP in B₀** (WP0-v3 (2.9): κ_mix m_φ² → g_aγγB₀m_φ, κ_eff = g_aγγB₀/m_φ): **ℛ = ρ_φg_aγγ²B₀²L_∥(0,m_φ)/(ρ_Tm_φ²)**, L along B₀, not polarisation-averaged
  (REF-WP8-F-A F5, -B V5b). WP0-v3 (2.9)'s source-prefactor check (O6) stays open.
- **Scalar (closed form, CW7 LE-155 — closes G-F1).** The NR reduction of y_φφψ̄ψ is y_φφ(n_e − 𝒯_e), 𝒯_e = Σ_i{p_i², e^{ik·r_i}}/(4m_e²). At k → 0, n_e conserves
  and drops; Γ_φ = −(y_φ²/m_φ)Im[R̃_{𝒯𝒯} + R̃_{𝒯n}v_Cε⁻¹R̃_{n𝒯}](k_φ → 0, m_φ), and the mixing term vanishes at k → 0 for every non-polar point group (no ℓ = 1
  invariant, WP6-v3 (1.5)/C28), so **FOM_φ = −Im R̃_{𝒯𝒯}(0,m_φ)/ρ_T** (> 0 for ω > 0) there, with the IP closed form Im R⁰_{𝒯𝒯} = −(2π/V)Σ_{cvk}|Σ_m p_cm·p_mv/(2m_e²)|²δ(m_φ − ε_ck + ε_vk)
  and the sum rule Σ_f(E_f − E_i)|𝒯_fi|² = ⟨|∇V|²⟩/(2m_e³) per electron (CW7-C12, C13), which is core-dominated.
**(b)** supp ε₂: indirect edge E_g^{ind} ± ω_Q (L9), polar band, TLS, dopants; never add a computed sideband to measured data (WP3 N4).
**(c)** Dark photon: total ε. Dirac/narrow gap: sources ×ε_bg too large — CONFIRMED in full text for 1708.08929 (REF-WP8-F-A §C); 1910.02091 via LIMITS L16 (R×2).
Superconductors: Mattis–Bardeen with |ε|² ≈ ω_p⁴/ω⁴; films: WP7-D IF-D9 factors.
### 2.3 Single-phonon nuclear recoil
**(a) [D]** WP2-v3 (2.2), n_ph = 1, c_κ = A_κF^M_κ. For q ≪ q_BZ, G = 0 and acoustic eigenvectors e_κν = √(M_κ/M_cell)ê_ν(q̂) (REF-WP8-F-A F6):

  S^{(1)}_ac/ρ_T = Σ_ν π q (q̂·ê_ν)² δ(ω − c_ν(q̂)q)Θ(ω_LO − ω)/(m_u²c_ν(q̂))   (M_κ = A_κm_u, c_κ ∝ A_κ),                                   (2.3a′)

equal per mass to **2205.02250 Eq. (30) with eigenvector Eq. (27)** [FT p.7–8] (m_p ↔ m_u: 1.5% in 1/m²; A-freedom holds to M_κ = A_κm_u, ≤ 0.8%). Pure LA along
q̂ recovers π q/(m_u²c_LA). **Validity:** q_max = 2m_χv_max < q_BZ, i.e. the A-free FOM holds for the **light mediator at all m_χ above the edge** and for the
**heavy mediator only at m_χ ≲ 0.1–1 MeV** (Si q_BZ ≈ 2.3 keV ⇒ m_χ ≲ 0.43 MeV); above, Umklapp and the incoherent composition-dependent form (2205.02250 Eq. (33))
govern ("For mχ = 1 MeV and 10 MeV, Umklapp processes dominate the rate in the heavy mediator case", 1910.08092 p.30 [FT]) (REF-WP8-F-B 1, V6).
**(a′) Optical branch in the 1BZ (R13 statement FALLS; REF-WP8-F-A F7, -B §2(ii)).** The q-linear coupling is ∝ √(M₁M₂/M_cell)(A₁/M₁ − A₂/M₂), ≈ 0 for A ∝ M even
when A₁ ≠ A₂ (R13 §0's "(A₁ − A₂)²" is withdrawn). The leading in-1BZ term comes from the intra-cell phase e^{iq·r_κ}:

  S_LO ≈ (2π/Ω_c) q⁴a²A₁A₂/(32 ω_LO m_p(A₁ + A₂)) δ(ω − ω_LO)   [FT 2205.02250 Eq. (31) p.8, "(q·r₂)² ≈ q²a²/16"],                         (2.3c)

O((qa)²) relative to the acoustic coupling and composition-dependent (A₁A₂/A_cell); the angle average is checked in CW7-C21.
**(b) [D]** m_min^{ac} = ω_th/(2c_LA(v_max − c_LA)) (2.3b); both rate coefficient and edge scale as 1/c_LA (soft lattices: larger rate, worse edge); near m_min^{ac}
the q-range [ω_th/c_LA, 2m_χ(v − c_LA)] adds c_LA dependence. **DB vs FT:** "the longitudinal sound speed is c_s ∼ 4000 m/s in GaAs and c_s ∼ 10⁴ m/s in
sapphire" [FT 1807.10291 p.6]; like for like c_L^{DB}/c_L^{FT} = 1.20 (GaAs, at the edge of the 20% need) and 1.08 (sapphire). The R13 "c_T–c_L brackets c_s"
check (WP8F-C12a) is withdrawn (REF-WP8-F-A F8, -B V7b).
### 2.4 Multiphonon to impulse
**(a) [D]** S_inc/ρ_T = (2π/M_cell)Σ_κ|c_κ|²e^{−2W_κ}Σ_{n≥1}w_κ^{*n}/n!; first moment per mass πq²/m_u² (composition-free); zeroth moment at large q ≈ 2π⟨A⟩/m_u.
**Correction (REF-WP8-F-A F9):** 2W_κ = (q²/2M_κ)⟨ω⁻¹⟩_{D_κ} (T = 0; WP2-v3 (3.1); 2205.02250 Eq. (24) [FT p.6]), so the Poisson-tail FOM uses
**ω̄_κ ≡ ⟨ω⁻¹⟩⁻¹**; the first moment underestimates 2W by Jensen (×9/8 for a Debye DOS, CW7-C22). Impulse: ∝ A × μ_χN² in both limits m_χ ≶ M_κ **far above
√(M_κE_th/2)/v_max**; near the NR edge q ≥ √(2M_κE_th) favours light nuclei (REF-WP8-F-B V8).
**(b)** ω_max^ph; free-NR m_min = √(M_κE_th/2)/v_max (104/137/220 MeV for O/Si/Ge at 10 eV). Charge readout: E_th^{nr} as the mean E_th^{ee}/QF with
QF = y_ion = 𝔶⟨𝔮⟩_NR/⟨𝔮⟩_ER; phonon readout E_th^{nr} = E_th^{ee}(1 + r_collg_Luke)/(Y_H + r_collg_Luke y_ion); below 350 eV measured yields (2303.02196) until
WP5 B-2 (WP5-AUD F-c). (d) NR partition: WP5 L20–L22 read with WP5-v4 A-8, A-9 (F-d). Anharmonic spread: type T (L18), the largest at fixed ω_th (G-F2).
### 2.5 Polar phonons
**(a) [D]** (2.5a) 𝓘_pol ≡ ∫_{band}L(0,ω)dω = Σ_ν(πω_Lν/2)Δ_ν, Σ_νΔ_ν = 1/ε_∞ − 1/ε₀; diatomic (2.5b) per mass 𝓘_pol/ρ_T = (π/2)e²Z*²/(M_cellμ_redε_∞²ω_LO).
**Rate ≠ 𝓘_pol (REF-WP8-F-A F10(i), -B V9):** with the light-mediator kernel 𝓡_pol = Σ_ν(πω_Lν/2)Δ_ν𝒦_ν, 𝒦_ν ∝ η̄_ν ln(q₊/q₋(ω_Lν)); sapphire at 1 MeV has
ln(2m_χv_max²/ω) = 5.68 (48 meV) vs 4.83 (112 meV) (CW7-C23). "𝓡_pol ∝ 𝓘_pol/ρ_T" is exact for one branch at fixed m_χ, and [E] otherwise
(band-uniform weight for m_χ ≫ 2ω_L,max/v_max²).
**GaAs (F10(ii), B §3(iii)).** "≤ 0.144" is withdrawn: 34 meV is a DFT range (1910.08092 p.30); with LST and the FT ε of 1807.10291 Table I (ω_LO/ω_TO = 1.088,
CW7-C25) 𝓘_pol/ρ_T ≈ 0.144–0.153 meV cm³/g, edge ≈ 9.7–10.3 keV, sapphire/GaAs ≈ ×61–65 (the upper ends use a measured ω_TO ≈ 33.3 meV [UNVERIFIED]).
**Sensitivities (F10(iii), F16, B §3(iv)).** On the ε route ∂ln𝓘/∂lnε_∞ = −ε₀/(ε₀ − ε_∞), ∂ln𝓘/∂lnε₀ = ε_∞/(ε₀ − ε_∞): GaAs −6.4/+5.4, AlN 1.9/0.9,
sapphire(o) 1.5/0.5, MgO 1.4/0.4 — weakly polar crystals need ε to ≈ 3%, which the ±15% DB ε fields cannot give. On the Z* route at fixed ω_T,
∂ln𝓘/∂lnZ* = 2 − (ω_L² − ω_T²)/ω_L² = 1.84 (GaAs): the R13 "×2" is an upper bound (conservative). Si, Ge: Z* = 0, quadrupolar vertex, S ∝ q⁴; the needed
input is the dynamical quadrupole 𝒬_κ (WP2-v3 (4.5)), now a §5 property.
### 2.6 Magnons
**(a) [D]** 𝓡_mag ∝ (𝓈_λ/ρ_T)⟨|F^{mag}(q)|²⟩(Bogoliubov weight), **𝓈_λ ≡ Σ_jλ_{S,j}²|𝐒_j|/Ω** (renamed from 𝓃_S, which clashed with 𝓃_s; for one sublattice with λ = 1 it is
1905.13744's n_s = S_cell/Ω, WP8-U-v2 s_spin). **(b) Edges:** gapped branch 2Δ_mag/v_max²; gapless **AFM** (linear, speed v_θ): the (2.3b) algebra with c → v_θ [D];
gapless **FM** (ω = 𝔇_swq²): q ≤ v/(𝔇_sw + 1/2m_χ), ω_max = 𝔇_swv²/(𝔇_sw + 1/2m_χ)² — not the (2.3b) algebra (REF-WP8-F-B V11; CW7-C24).
**(e) Corrections (REF-WP8-F-A F12).** The heuristic LSWT parameter 1/(2|𝐒|) is 0.2 at |𝐒| = 5/2 and **1 at |𝐒| = ½** (owed also to WP4-v3 §2.1(c), [2.2](b)).
A Heisenberg FM has S^{(2m)} ≡ 0 at T = 0; the two-magnon continuum exists for AFM/ferri only. The computed local two-/one-magnon weight ratio
r_2m = ΔS(1 + ΔS)/(S(1 + 2ΔS)) is 0.146/0.049/0.029 at S = ½, 3/2, 5/2 for the simple-cubic AFM (ΔS = 0.078; CW7-C14), far below 1/(2S); the WP6 nuisance
row is CW7 LE-156. Si/Ge have no magnon FOM. Absorption into the Kittel mode (B2-L6) and the data route (B2-L7, `src=data`) as R13.
### 2.7 PAER and Migdal
**PAER.** 𝓡_PAER = (2.1a) with L → L^{PA}; window FOM Δm_PAER/m = (2E_min^{ZPL}(q*) − 2(E_g + ω_TA))/(2(E_g + ω_TA)); Si: PAER-only 0.333–0.42, PAER-leading to
≈ 0.43, shared 0.43–0.54, allowed ZPL above ≈ 0.54 MeV (WP6-v3 (3.1)(iii); REF-WP8-F-A F13); Ge 0.213–0.32. Onset exponents §1.3. Interim pair-screening factor
[0.4, 1.8] (median 0.85, σ_ln 0.75). E_min^{ZPL}(q*), ω_ν(Q*) ab initio: COMP-PH/COMP-PAER (G-F5).
**Migdal (REF-WP8-F-A F14, -B §4).** 2011.09496 Eq. (6) [FT]: dP/dω = 4α∫d³k/(2π)³ Z_ion(k)²|v_N·k|²Im[−1/ε(k,ω)]/(ω⁴k²), "only valid for k in the first
Brillouin zone". With Z_κ(k) inside the k-integral and an isotropic L, **𝓠_Mig,κ(ω) ≡ ∫d³k Z_κ(k)²L(k,ω)/(3(2π)³ω⁴)** (renamed from 𝓜_Mig, which clashed with the
moment matrices). Per mass for a compound the nuclei per unit mass are 1/M_cell, so

  𝓡_Mig ∝ (2σ_nv²/(m_n²m_u³)) μ_N⁴-scaling × Σ_κ𝓠_Mig,κ(ω)/A_cell   (CW7-C20: two species give Σ_κZ_κ²/(A₁ + A₂)),                     (2.7′)

for any m_χ ≪ M_κ (material scaling); the power is m_χ⁴ only for m_χ ≫ m_n and m_χ² for m_χ ≲ m_n (the dominant range). Hypotheses added: ω ≪ μ_Nv²/2
(otherwise the E_N² weight carries [(1 + √(1 − 2ω/μ_Nv²))/2]⁴ = 0.93 and 0.72 at 2ω/μ_Nv² = 0.07 and 0.29), soft limit |k| ≪ |q_N|, impulse regime — onset
q ≳ 91.5/112 keV, i.e. m_χ ≳ 17.3 (Si)/21.1 (Ge) MeV (L7c below). "Light nuclei win" holds at fixed valence ion charge Z_κ(k) (not nuclear Z). Kinematic floor
2E_g/v_max². **Calibration rule (WP5-AUD F-e):** neutron-calibrated yields contain Migdal: Y_tot = Y_casc[S^{GS}] + ∫P_casc dP_Mig, never Y_casc + Migdal.
### 2.8 TLS, defects, LEE proxies
(i) A′→TLS: FOM tanδ₀/(ρ_Tε_r) (L32). (ii) DM–TLS: a-SiO₂ ≈ 3.7×10⁻² /(kg·day·meV) [E, ×3] (WP7-T §2.4). (iii) Defect creation E_d; colour-centre yield Y_CC.
**(d) LEE proxies (WP5-AUD F-f, F-g, D-12, D-13, D-17).** Data caps (95% C.L., (B-a)–(B-d)) ⟨E_st⟩/E_R ≤ 0.055 (Si)/0.064 (Ge), p_surv·E_st,1/E_d ≤ 0.21/0.20,
p_surv ≲ 0.475/0.66, **valid only at the calibration energies** (Si 10–100 keV; Ge 103 keV ²⁰⁶Pb, surface); the event-seeded release power is ≤ 𝓟_st by T-1;
the Si datum is degenerate between E_st and collection (r_coll = 1.144 alone reproduces η^φ_NR = 0.952), joint profile via WP5-AUD (AUD-1). Single Frenkel-pair
releases visible only for E_thr^{det} ≤ 2.1–2.7 eV (ϵ_coll = 0.3 [E], E_st,1 = 7–9 eV); pocket recrystallisation N_a ≳ 270–540 (0.2–0.1 eV/atom). 𝓟_TLS ∝ P̄_STM
(enters signal + and background −); 𝓟_σ ∝ Y_mod∫Δα_thdT [C]. **Radiopurity:** the R13 [UNVERIFIED] list is extended (¹⁸⁰W, ¹¹⁶Cd, ¹³⁰Te, ¹⁴⁷Sm, ¹⁵²Gd, ¹⁷⁴Hf,
¹⁹⁰Pt, ⁵⁰V, Th, U; REF-WP8-F-B §6.7) and replaced for the survivors by WP8-U-v2 §4.4 (S4 values, cosmogenic production tables).
### 2.9 Inelastic and exothermic DM (new class statement; REF-WP8-F-B §6.5)
Δ_χ enters only through v_min = (ω + Δ_χ)/q + q/2m_χ (CONVENTIONS §3), so every functional above applies with E_th → E_th + Δ_χ in the edge (m_min of (3.1′) with
the shifted onset) and, for Δ_χ < 0, with reach into ω < 0 weighted by detailed balance; Δ_χ is DM-side and adds no material property.

## 3. Reach scalars [D] (REF-WP8-F-A F15, -B V15)
Signal s = σC_χ𝓡MT; background b = MT∫b_bg dE. Background-free (MT∫b_bg ≪ 1): σ_lim = Z_0/(C_χ𝓩_0MT), 𝓩_0 = ∫ϵ(E)𝓻̂_s(E)dE (= ϵ_cut𝓡 for a flat efficiency),
Z_0 = 2.303 at 90% C.L. Background-limited: exclusion Asimov 2[s − b ln(1 + s/b)] → Σs²/b (the discovery form has the same limit), σ_lim = Z/(C_χ𝓩_B√MT), with
**one C.L. throughout: Z = 1.28 (90% one-sided)**; flat shapes 𝓩_B = 𝓡/√(b_bgΔE); a halo-width line: ∫𝓻̂²/b = 𝓡²/(2√πσ_Eb). Systematics floor:
**σ_lim → Z f_sys b_bgΔE_ROI/(C_χ𝓡)**, exposure-independent (CW7-C27; R13 omitted ΔE_ROI). Class ROIs as R13 (ER [E_g, E_g + 10ε_eh], ABS [m_φ ± 2σ_E], …) [E].

## 4. Uncertainty inherited by each FOM (WP6-v3 (5.2) types; new rows from CW7)
| FOM | Nuisances (type, prior) | Effect |
|---|---|---|
| ER-ρ, ER-light | 𝒳 ladder M ×1.61 σ_ln 0.22; exciton lines A σ_ln 0.5; XC/gap E; screened rows M; k-grid half-normal M | near-edge ×e^{±0.22}; m_min ±0.1–5% |
| ER near edge, PAER | gap E; edge Δ + E (σ_E ≈ 2 meV on ω_TA(Q*)); n_g = 2 A [0.4, 1.8]; thermal A | ×e^{±0.75}; log-sensitivity 132 (101 replica) |
| ABS | `src=data` none; ε_bg (L16); SOC split (ALP); scalar: core reconstruction of 𝒯 (M, CW7 LE-155) | DB ε₂ carries the XC/gap E row |
| NR-1ph, POL | n_A = 0 T; Z*, ε_∞, ε₀ as M on scalars with the §2.5 sensitivities (ε route up to 6.4) | (2.5b)/(2.5a) |
| NR-mph | K one-sided M; anharmonic T (θ_A, θ_δ) | largest spread (up to ~10², [ABS]) |
| Migdal | impulse/EFT Δ; ELF 𝒳 M; Z_κ(k) profile M (new) | ∝ 𝓠_Mig |
| MAG | **θ_mag** (A on S^{(2m)} for AFM/ferri, 0 for FM; residual M with r = r_2m/(2S)); **θ_Fmag** (M, σ_ln 0.2 [E]) — CW7 LE-156 | ×(1 ± r_2m) |
| SC | **θ_BCS one-sided M**: s = s_c e^{−\|θ\|σ_BCS(y)}, σ_BCS = 0.09 (y = 5), 0.03 (y = 10); cells with 2(Δ_BCS/qv_F)𝔰_BCS > 0.3 (y ≲ 3.5 at the edge) masked — CW7 LE-157 | downward only |
| Yield (released) | Δ {step, R&K, URF} + M; ε_eh 𝒩(3.75, 0.05) eV (Si); others: GAP-EF band as M; F_eh M; θ_st, θ_coll joint via (AUD-1), r_coll σ_ln 0.2 (WP5-AUD D-4); θ_tr^{pr} T | threshold in quanta; LEE caps |
| Halo | separate band: **v_max 2–7% (from v_esc)**, ±1.8% annual | m_min 4–14%, ±3.6% |
UNRESOLVED LIMITS rows touching each class: as R13 §4.2 (L3, L11, LB1-5, LB1-11, LB1-13, L-D8, L9b, L-D1, L-D10, B2-L1, L5, B2-L4, L7c, G-T7, L36, L38).

## 5. Interface to WP8-U: one scalar per channel and the property list
**(5.1)** As R13 §5.1 with the corrected functionals of §§2–3: NR-1ph scalar π/(m_u²c_LA) restricted as in §2.3; POL scalar 𝓘_pol/ρ_T [E] multi-branch;
Migdal Σ_κ𝓠_Mig,κ/A_cell; MAG 𝓈_λ⟨|F^{mag}|²⟩/ρ_T; ALP-in-B₀ L_∥/(ρ_Tm_φ²).
**(5.2) Needed accuracies, corrected.** ρ_T: 20% (the R13 "5% near edge" belongs to E_g). ε_∞, ε₀: 10% on the Z* route, ≈ 3% on the ε route for weakly polar crystals.
c_L: 20% rate, 5% edge (DB vs FT +20% GaAs). E_g(T_op): 1% edges, 1–2 meV near-edge. ω̄_κ ≡ ⟨ω⁻¹⟩⁻¹: 10%.
**Added properties (REF-WP8-F-A F17, -B §6):** Z_κ(k) ion-core charge profile (Migdal); nuclear spin content (abundance of spin-carrying isotopes, ⟨S_p⟩, ⟨S_n⟩) —
the spin-dependent nucleon FOM class is **out of scope of this return and recorded as exact gap G-F6**; μτ / trapping / collection (Hecht, Ramo, r_coll; L33–L35);
SOC strength or R̃_{s,c} (ALP, spin rows); nuclear radius / Helm parameters (impulse); E_g(T_op), E_x^b(T_op), ε_eh(T), ω_TA(Q*) at T_op; dynamical quadrupoles 𝒬_κ;
Ω, a, q_BZ, r_κ (validity of (2.3a′), the (2.3c) term). The WP8-U-v2 table carries each as a value or GAP.
**(5.3) DB vetting:** replaced by the single rule set V1–V6 of WP8-U-v2 §1.3 (rule (i) "MBJ within ≈ 10%" REFUTED: GaAs −13%, Ge −19%; rule (ii) failures also NaI
JVASP-1996 0.28 cm⁻¹ and SiC JVASP-8158 3.39 cm⁻¹; "metallic" GaAs is near-metallic 0.085 eV).

## 6. Literature (IDs verified against the arXiv API; code/CW7/data/arxiv_verified.json)
R13 list kept (1807.10291, 1910.08092, 1706.05818, 2506.06568, JARVIS). **2205.02250** is now a source formula (Eqs. (24), (27), (30), (31), (33), pp.6–8 [FT, read here
and by both referees]), not "wording only". 2011.09496 Eq. (6) and its 1BZ statement [FT via REF-WP8-F-A]. 1708.08929 Eqs. (2.4)–(2.6), (4.4)–(4.5) [FT via REF-WP8-F-A].
Sapphire ρ_T = 3.98 g/cm³ is [FT 1807.10291 Table I p.11]; its e-ray widths are "adopted" from the o-ray in the source (Table II p.31).

## 7. Exact remaining gaps
- G-F1 **CLOSED** (closed form + computation specification: CW7 LE-155).
- G-F2: anharmonic spread of the multiphonon FOM (L18 type T) at ω_th ≳ ω_max^ph.
- G-F3: LEE proxies are bounds (𝓟_st, calibration energies only) or structure (𝓟_σ); no predictive LEE rate (WP7-E G-E2).
- G-F4 **CLOSED** (WP6 row: CW7 LE-156).
- G-F5: E_min^{ZPL}(q*), ω_ν(Q*) ab initio (LE-16/LE-17).
- G-F6 (new): spin-dependent nucleon FOM class (𝒪₄-type rows with I_κ of WP0-v3 (2.2)): the strongest statement is S_{I I} = spin-weighted single-phonon/impulse
  responses with ⟨S_{p,n}⟩; missing step: the per-isotope spin matrix elements and their phonon form factor; spec: tabulate odd-A abundances × ⟨S_{p,n}⟩ (shell-model
  literature) and reuse WP2-v3 (2.2) with c_κ → spin weights.

## 8. The DB-only polar bracket [D] (validity corrected)
(8.1) (π/2)(1/ε_∞ − 1/ε₀)ω_T,min ≤ 𝓘_pol ≤ (π/2)(1/ε_∞ − 1/ε₀)ω_T,max√(ε₀/ε_∞) holds for a lossless factorised ε **on one principal axis**. The JARVIS
`dfpt_piezo_max_dielectric_*` and IR-mode fields are tensor maxima: the bracket is **rigorous only for cubic entries (MgO [4.7, 8.5] meV cm³/g)** and
"orientation-maximal" for Al₂O₃ (JVASP-32 total 11.97 ≈ 3.204 + 8.803 is the e-ray-like value; FT ε₀∥ 11.5), AlN and GaN; "contains the FT 9.40" is a consistency
observation, not a test (REF-WP8-F-A F11, -B V10).

## Symbols introduced/used
| Symbol | Meaning | Status |
|---|---|---|
| 𝒦^{kin,(0)}_a, 𝒦^{kin,(2)}_a | kinematic factors qF²η/(4π²), qF²ξ/(4π²) | renamed from 𝒦_a (clash with cascade kernels 𝒦_c) |
| C_χ | flux factor ρ_χπ/(m_χμ_χe²) outside 𝓡 | new |
| 𝓠_Mig,κ(ω) | Z_κ(k)²-weighted ω⁻⁴ ELF moment | renamed from 𝓜_Mig (clash with 𝓜¹_ab) |
| 𝓈_λ | Σ_jλ_{S,j}²\|𝐒_j\|/Ω | renamed from 𝓃_S (clash with 𝓃_s) |
| w^{pol}_ν | per-branch weight of 1/ε_∞ − 1/ε₀ (R13 "Δ_ν") | renamed (clash with Δ_χ, Δ^τ_k); used as Δ_ν in quoted R13 equations only |
| ω̄_κ | ⟨ω⁻¹⟩⁻¹ of D_κ | definition fixed (NOTATION ω̄ row) |
| 𝔇_sw, v_θ | FM spin-wave stiffness, AFM magnon speed | new / source |
| θ_mag, θ_Fmag, θ_BCS | magnon and SC nuisances | new (CW7) |
| 𝓡_a, 𝓩_0, 𝓩_B, 𝓻_s, 𝓻̂_s, b_bg, ϵ_cut, f_sys, ΔE_ROI, δ_rank, 𝓘_pol, Δ_mag, ω_max^{mag,ph}, m_min^{ac}, Δm_PAER/m, w_acc, 𝓟_* | as R13 | R13 rows (IF-F6) |
| used | ρ_T, S, L, L^{PA}, 𝔇^{(n)}, A^{(n)}, η, ξ, v_max, E_th, p̄_on, c_ν, ê_ν, q_BZ, r_κ, 𝒬_κ, R̃_{𝒯𝒯}, 𝒯_e, g_aγγ, B₀, y_φ, Z_κ(k), μ_N, 𝔰_BCS, y_BCS, r_coll, ϵ_coll, θ_* | NOTATION v4 + WP7/WP7-E rows |

## Interface flags
| # | Owner | Item | Action |
|---|---|---|---|
| IF-F1′ | WP8-S (CW7 LE-159) | §5 scalars with the corrected validity ranges | rank with δ_rank = 0.2 |
| IF-F3 | WP5-AUD | yield rows | **answered**: released with F-a…F-i applied |
| IF-F4 | WP6 | magnon row | **answered** by CW7 LE-156 (owed WP6 text) |
| IF-F6′ | NOTATION | the renames of the Symbols table | add rows |
| IF-F8 | WP4 | 1/(2\|𝐒\|) = 1 at \|𝐒\| = ½ in WP4-v3 §2.1(c), [2.2](b) | owed correction |
| IF-F9 | WP0 | ALP-in-B₀ prefactor (O6), 1/m_φ² dependence | check WP0-v3 (2.9) |

## Proposed LIMITS rows (corrected; numbers provisional)
| # | Chain (URF) | Source formula | Validity | Leading correction | Status |
|---|---|---|---|---|---|
| L-F1 | WP2-v3 (2.2), n_ph = 1, G = 0, acoustic e_κν = √(M_κ/M_cell)ê_ν, ÷ρ_T → (2.3a′) | **2205.02250 Eq. (30) with Eq. (27)** [FT p.7–8], incl. Θ(ω_LO − ω) | q ≪ q_BZ (heavy mediator m_χ ≲ 0.1–1 MeV; light all m_χ); e^{−2W} ≈ 1; harmonic; c_κ ∝ A_κ | O((q·r_κ)²) intra-cell phase (Eq. (31)); dispersion ω_LA ≤ c_LAQ; m_p vs m_u 1.5%; mass defect | CROSS-CHECKED (C1a,b; referees) |
| L-F2 | WP2-v3 (4.2)–(4.3) + LST → (2.5b); KK of 1/ε at ω = 0 → (8.1) | **1807.10291 PDF v1 Eqs. (21)–(22) p.17, rate (24)** (= HTML (31)–(32)) | rank-1 ε, q ≪ q_BZ, ω ≪ E_g; lossless factorised ε per principal axis; band-uniform kinematic weight for 𝓡 ∝ 𝓘 | damping < 1%; per-branch ln(q₊/q₋(ω_Lν)) weights; quadrupoles where Z* = 0 | CROSS-CHECKED |
| L-F3 | L7b soft limit × free-NR dσ/dE_N at fixed σ_n → (2.7′) Σ_κ𝓠_Mig,κ/A_cell per mass | 2011.09496 Eq. (6) [FT], Z_ion(k) inside | k ∈ 1BZ; isotropic L; \|k\| ≪ \|q_N\|; m_χ ≪ M_κ; ω ≪ μ_Nv²/2; impulse onset 17–21 MeV | L7c below the onset; boost mass δM_κ; [(1 + √(1 − 2ω/μ_Nv²))/2]⁴ | CROSS-CHECKED (C8, CW7-C20) |

## 9. Closing table (A = REF-WP8-F-A, B = REF-WP8-F-B "Required corrections", AUD = WP5-AUD §5.2)
| Item | Request | Status | Where |
|---|---|---|---|
| A-F1 | v-independent 𝔇 hypothesis; c_a | APPLIED | §1.2 (1.2′) |
| A-F2 | replica exponent 3/2 (≈ 101); "sensitivity" wording | APPLIED | §1.3 |
| A-F3 | Z/A scope; η̄ a definition; Lindhard scaling only | APPLIED | §2.1 |
| A-F4 | §0 "total ε" condition | APPLIED | §0, §2.1(c) |
| A-F5 | ALP in B₀: g²B₀²/m_φ²; O6 | APPLIED | §2.2 |
| A-F6 | pure-LA hypothesis; Σ_ν(q̂·ê_ν)² | APPLIED | (2.3a′) |
| A-F7 | optical branch (FALLS) | APPLIED | (2.3c) |
| A-F8 | c_L like-for-like (+20%) | APPLIED | §2.3(b) |
| A-F9 | 2W with ⟨ω⁻¹⟩; impulse both limits | APPLIED | §2.4 |
| A-F10 | 𝓡_pol kinematic weight; GaAs "≤"; fixed-ω_LO derivatives | APPLIED | §2.5 |
| A-F11 | DB bracket axes | APPLIED | §8 |
| A-F12 | 1/(2\|𝐒\|) = 1 at ½; FM two-magnon ≡ 0 | APPLIED (+ IF-F8 to WP4) | §2.6 |
| A-F13 | PAER range wording | APPLIED | §0, §2.7 |
| A-F14 | Z_κ(k) inside; 1BZ; regime label; Migdal edge | APPLIED | §2.7, L-F3 |
| A-F15 | floor dimension; one C.L.; E-dependent ϵ | APPLIED | §3 |
| A-F16 | ε-route sensitivity; ρ_T need | APPLIED | §2.5, §5.2 |
| A-F17 | six missing properties | APPLIED (SD-NR class → G-F6) | §5.2, §7 |
| A-F18 | MBJ "≈ 10%" | APPLIED (withdrawn) | §5.3 |
| A-F19 | ³H T½ [FT]; NaI calc.; Eq. (40) p.30; one numbering | APPLIED | header, §2.1(d), §2.2 |
| A-§B | L-F1/2/3 sources and validity; §6 wording on 2205.02250 | APPLIED | LIMITS rows, §6 |
| A-§E | added checks (S_LO phase term, ⟨ω⁻¹⟩, per-branch K) | APPLIED | CW7-C21, C22, C23 |
| B-1 | optical term; heavy-mediator restriction | APPLIED | §2.3 |
| B-2 | C12a → c_L only | APPLIED | §2.3(b) |
| B-3 | Migdal Σ/A_cell; m_χ ≪ M_κ; ω ≪ μ_Nv²/2; ≈ 20 MeV | APPLIED | §2.7 |
| B-4 | GaAs LST ω_LO, drop "≤" | APPLIED (range, measured ω_TO [UNVERIFIED] flagged) | §2.5 |
| B-5 | (8.1) cubic only | APPLIED | §8 |
| B-6 | 𝓡_pol log weight | APPLIED | §2.5 |
| B-7 | ALP–photon B₀²/m_φ², L_∥ | APPLIED | §2.2 |
| B-8 | FM edge quadratic | APPLIED | §2.6 |
| B-9 | floor ×ΔE_ROI; flux factor | APPLIED | §1.2, §3 |
| B-10 | v-independent 𝔇; 𝒦 for v_T rows | APPLIED | (1.2′) |
| B-11 | Z/A; ⟨1/ω⟩ in w_acc | APPLIED | §2.1 |
| B-12 | property items 1–6; IF-F7 (NaI, SiC); rule (i) withdrawn | APPLIED | §5.2–5.3 |
| B-13 | tags/pages; [DB] tag; renames | APPLIED ([DB] owed to CONVENTIONS) | §6, Symbols |
| B-V4, B-V8, B-§2(v), B-§9 | ER-light [E] above 0.5 MeV; impulse near edge; c_LA near m_min; halo label, "ω̄_κ not in NOTATION" | APPLIED | §2.1, §2.4, §2.3, §4, Symbols |
| AUD F-a | threshold in quanta via P(N_eh\|q,ω) | APPLIED | §2.1(d) |
| AUD F-b, F-d | consistent | NO CHANGE | §2.1(d), §2.4 |
| AUD F-c | E_th^{nr} with y_ion, phonon readout formula | APPLIED | §2.4(b) |
| AUD F-e | Migdal in neutron-calibrated yields | APPLIED | §2.7 |
| AUD F-f, D-17 | caps at calibration energies; release ≤ 𝓟_st | APPLIED | §2.8(d) |
| AUD F-g, D-12, D-13 | 2.1–2.7 eV; N_a 270–540; 0.475 | APPLIED | §2.8(d) |
| AUD F-h | joint profile (AUD-1); r_coll σ_ln 0.2 | APPLIED | §4 |
| AUD F-i | sources WP5-v4 + AUD; y_ion/QF as ⟨𝔮⟩ ratios | APPLIED | §2.4(b), §4 |
