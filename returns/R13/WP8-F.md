# R13 / WP8-F: figures of merit per interaction channel

Derivation agent, brief briefs/R13/WP8-F.md. Inputs: STATEMENT v2, FRAMEWORK (WP8 bullet), LIMITS.md (v3 table, WP7 rows incl. WP7-E L33–L38 with
the **coordinator-corrected L36**), CATALOG-A, CONVENTIONS (incl. R13 amendments, §13 rows 23–28), NOTATION v4 + R9/WP7/WP7-E rows,
state/CORRECTIONS.md (§0, §17, §18 read; no owed item changes a site used here except the WP7 renames, which are applied: c_ν, 𝓃_e, ε_bg,
κ_mix, κ_cal, g_Luke, y_ion, δ_coll, r_coll), returns/R8/WP0-v3, WP1-v3, WP2-v3, WP3-v3, WP4-v3, **WP5-v3 read with WP7-E-v3 §5** (WP5-v4 not
used), WP6-v3, returns/R12/WP7-*-v2/v3. Checks: `code/WP8-F/checks.py` (numpy + sympy + scipy, **39 checks, all PASS, ≈ 2 s**), cited
WP8F-Cn. Tags per CONVENTIONS §12; material provenance tags [FT] (full text, page = PDF page), [DB] (JARVIS-DFT OPTIMADE entry and field),
[E], [UNVERIFIED]. **No ranking of materials is made here** (that is WP8-U); material numbers are illustrations of the scalings.
**Provisional flag (coordinator, 2026-11-01).** Every FOM that uses a yield or an energy-partition quantity (ε_eh, F_eh, η_pb, y_ion, E_st, the
LEE proxies of §2.8) is **provisional pending the joint WP5 + WP7-E audit**; such rows carry "(prov.)".
Status: CLAIMED (one return), pending R×2. **Novelty:** the FOM reductions are standard limits of refereed campaign formulas; the KK bracket (8.1)
and the per-mass statements (2.3a), (2.5b) are re-derivations, novelty not searched (UNRESOLVED).

---
## 0. Results at a glance (one row per FOM class)
| Class | Rate FOM 𝓡 (material functional × kinematic factor) | Reach edge set by the material | Screening | Background proxies | Dominant m_χ [E] |
|---|---|---|---|---|---|
| ER-ρ (O₁, e–h, plasmon) | (1/ρ_T)∫dω∫dq q³F_DM²η L(q,ω)/(2πα) | m_min of WP6-v3 (3.1′), floor 2E_x/v_max² | L = Im[−1/ε] (total ε), not 1/\|ε\|² pointwise | ³H, ³²Si, ¹⁴C; dark counts; LEE (prov.) | 0.2 MeV–1 GeV |
| ER-light (F_DM ∝ q⁻²) | (1/ρ_T)∫dω L(q→0,ω)·ln(q₊/q₋) | same; lower gaps win doubly | optical ELF | as above | 0.2–10 MeV |
| ABS (A′, ALP, scalar) | A′: L(0,m_φ)/ρ_T; ALP: m_φ² ε₂(m_φ)/ρ_T (SOC = 0); scalar: Im Π_φφ/ρ_T | support of ε₂: E_g (direct/indirect + phonon), ω_TO…ω_LO, TLS | A′: total ε; ALP: none at LO; Dirac ×ε_bg | Compton, β; LEE | m_φ = ω, meV–keV |
| NR-1ph (nucleon) | coherent LA: π q/(m_u²c_LA) per mass (A-free); optical (A₁ − A₂)²-suppressed | ω ≤ 2m_χc_LA(v_max − c_LA) | R_NN (ion + electron) | neutrons, LEE | 10 keV–10 MeV |
| NR-mph / impulse | (1/ρ_T)Σ_κ(2π/Ω)A_κ²e^{−2W}Σ_n w^{*n}/n!; impulse ∝ A per mass | ω_max^ph, ω̄_κ; free NR: m_min ≈ √(M_κE_th/2)/v_max | R_NN | neutrons, coherent ν, LEE | 1 MeV–10 GeV |
| POL (A′-mediated, charge) | 𝓘_pol/ρ_T, 𝓘_pol ≡ ∫dω L(0,ω) over the ionic band = Σ_ν(πω_Lν/2)Δ_ν | 2ω_LO/v_max² (≈ 10–32 keV) | built in (Z*/ε_∞, LO) | as NR-1ph | 10 keV–10 MeV |
| MAG (e-spin) | (𝓃_S/ρ_T)·\|F^{mag}\|²·∫(kinematics) | Δ_mag (anisotropy/Kittel gap), ω_max^mag | none at SOC = 0 | as ER, + magnetic noise | keV–MeV |
| PAER / Migdal | PAER: (1/ρ_T)∫L^{PA}; Migdal: (Z_κ²/A_κ)·𝓜_Mig(ω) per mass (m_n ≪ m_χ ≪ M_κ) | PAER: E_g + ω_TA(Q*) (Si 0.333–0.337 MeV); Migdal: E_g at q_N | total ε in both ELFs | as ER + NR | PAER 0.33–0.54 MeV (Si); Migdal 10 MeV–1 GeV |
| TLS / defects | A′→TLS: tanδ₀/(ρ_Tε_r); DM–TLS: P̄_STM-weighted (WP7-T §2.4); F-centre: Y_CC | ω ≲ 0.1 meV (TLS); E_d (damage) | TLS: medium ε_r | **P̄_STM is also the TLS-LEE source** | keV–MeV (TLS), ≳ 100 MeV (damage) |
Scalar reach FOMs (§3): background-free 𝓩_0 = ϵ_cut𝓡 (σ_lim ∝ 1/(𝓩_0MT)); background-limited 𝓩_B = [∫dE 𝓻_s²/b_bg]^{1/2} (σ_lim ∝ 1/(𝓩_B√MT));
systematics floor σ_lim → Z f_sys b_bg/𝓡, exposure-independent (WP8F-C10).

---
## 1. General reduction from the master formula
**(1.1) Factorisation [D].** WP0-v3 (3.4), per unit target mass, with the DM tensor (2.3) and the velocity kernel 𝒢 = f̂^{(0)}/q (CONVENTIONS §8):

  dℛ/dω = (ρ_χ/m_χ) · (1/ρ_T) ∫d³q/(2π)³ ∫d³v f_χ(v) tr[𝔇ᵀ(q,v)S(q,ω)] δ(ω − ω_q).                                        (1.1)

For one operator row a (or a set of rows with a common 𝔇 up to a q-dependent factor), 𝔇_aa = |𝒱_a|² F_DM,a²(q) c_a, and isotropic S̄_aa:

  dℛ/dω = (ρ_χ/m_χ) |𝒱_a(q₀)|² · ∫dq q²/(2π²) · [F_DM,a²(q) η(v_min(q,ω))/(2q)] · [S̄_aa(q,ω)/ρ_T].                            (1.2)

The **material functional** is S̄_aa(q,ω)/ρ_T; the **kinematic factor** 𝒦_a(q,ω; m_χ) ≡ q F_DM,a² η(v_min)/(4π²) depends only on the DM and halo. **Rate FOM
[new]:** 𝓡_a(m_χ) ≡ ∫_{ω ≥ E_th^det}dω∫dq 𝒦_a S̄_aa/ρ_T at fixed |𝒱_a(q₀)|², ρ_χ = 0.3 GeV/cm³ and the 2105.00599 halo. For non-diagonal 𝔇 (𝒪₃-type couplings
with SOC, WP0-v3 (3.3) index order) the material functional is the matrix S/ρ_T contracted with 𝔇ᵀ; the FOM is then a tr[𝔇ᵀS]/ρ_T functional, not a single
response, and is ranked per coupling. 1/ρ_T = Ω/M_cell turns per-cell responses into per-mass ones (WP8F-C1).
**(1.2) Reach edge [D].** The edge mass is WP6-v3 (3.1′): m_min = min_q q²/[2(qv_max − E_th(q))], v_max = 794.5 km/s. It equals 2E_th/v_max² only for a
q-independent onset (3.1). Vocabulary (WP6-v3 (3.1) consequences (i)): 2E_g/v_max² is the **continuum floor** (Si 0.3332, Ge 0.212 MeV, WP8F-C16), 2E_x/v_max²
the **floor of the total S̄** (Si 0.329), and channel edges lie above floors (Si PAER 0.333–0.337 MeV [E]). Near the edge the rate is
ℛ ∝ δ_v,0^{7/2+k_tail+p̄_on} (WP6-v3 (3.3)), so the **near-edge rate** carries a log-sensitivity to E_th of ≈ 132 at m_χ = 1.05 m_min (p̄_on = 3, k_tail = 0;
WP8F-C14b), valid only in the window Δm_χ/m_min ≲ 1–5%.
**(1.3) Rate versus reach FOMs [D].** 𝓡 governs at fixed exposure and fixed background; m_min (or the absorption support) governs where 𝓡 = 0. Which
one controls a ranking depends on the experiment class (§3). Every per-mass FOM is linear in 1/ρ_T: a 10% density error is a 10% FOM error.

---
## 2. FOM classes
Each class gives (a) rate FOM, (b) edge, (c) screening, (d) background-relevant quantities, (e) scaling with elementary inputs and dominant mass range.

### 2.1 ER scattering through the loss function (O₁; Cat. E1–E3, E7, E13; LIMITS L1, L2, L10, L11, L17)
**(a) [D]** Density row, total-charge-like screening with clamped nuclei or ω ≫ ω_max (WP0-v3 (5.5)(i)/(ii)): S̄_ee = q²L̄/(2πα(1 − e^{−βω})), L ≡ Im[−(ε^{-1})₀₀]
(CONVENTIONS §6). With F_DM = 1 (heavy) and (αm_e/q)² (light), (1.2) gives the q-weights (WP8F-C7a)

  𝓡_ER,heavy = (1/2πα)(1/ρ_T)∫dω∫dq q³ η L(q,ω)/(4π²),   𝓡_ER,light = ((αm_e)⁴/2πα)(1/ρ_T)∫dω∫dq η L(q,ω)/(4π² q).            (2.1a)

If L(q,ω) varies slowly for q ≲ q_c(ω), 𝓡_ER,light ≈ (·)∫dω L(0,ω)·η̄·ln(q₊/q₋): the **light-mediator ER FOM is the optical ELF per mass** [D for the
reduction; the slow-variation hypothesis is the stated condition]. **Ceiling [D] (L17):** ∫₀^∞ dω ωL = (π/2)ω_p² with ω_p² = e²𝓃_e/m_e, so per mass
(π/2)(4πα/m_e)(Z/A)/m_u: **Z/A ∈ [0.40, 0.50] for inorganic targets, spread ×1.24 (organics ×1.34)** (WP8F-C7b,c). The total f-sum per mass is nearly
universal; the FOM is set by **how much ELF weight sits at ω ≤ ω_max(q) = qv_max − q²/2m_χ**. L17's sum-rule bound holds only where its static step
1 − ε_ch⁻¹(q,0) ≤ 1 holds (ch = c, or clamped ch = e); for electron-only coupling in a relaxed polar lattice it fails (×2.30 GaAs-like, WP0-v3 G6).
**(b)** E_th(q) = E_min(q) (indirect onset), m_min by (3.1′); total-S̄ floor 2E_x/v_max². Lower gaps lower the edge linearly (dm_min/m_min = dE_th/E_th).
**(c) [D]** Screening is L itself. The pointwise factor 1/|ε|² (Si 0.117 at q = 2 keV, 0.451 at q = αm_e) is **not** the rate ratio (×1.4–2.5 IP over
screened, 2101.08275; L1 note, WP1 IF-16). A low ε₁ (Dirac, narrow-gap with small ε_∞) raises L at fixed ε₂, L = ε₂/|ε|². Metals and superconductors
(Lindhard limit L10/L15) [D, sketch]: L ≈ (πω/2qv_F)(q²/k_TF²)/(1 + q²/k_TF²)² for ω < qv_F, i.e. L ≈ πωq/(2v_Fk_TF²) at q ≪ k_TF, so the heavy-weighted 𝓡 ∝ ∫q⁴dq/(k_TF²v_F) (strong screening;
BCS coherence factors and the [4.2′] first-order term ≤ 16% at y_BCS = 5, WP4-v3).
**(d) (prov.)** Threshold in quanta: N_eh via ε_eh (Si 3.749 ± 0.001 eV, F_eh 0.119 ± 0.002 at 5.9 keV, 123 K; 2004.11499 [FT via WP5-v3 §6.4]); a
charge readout needs ω ≥ E_g, a phonon (NTL) readout needs g_Luke-gain. Backgrounds per mass: cosmogenic ³H (Si: production "roughly 124 atoms/kg/day"
at sea level, "0.002 events/kg/keV/day for each day of sea-level exposure" in 0–5 keV, 2506.06568 p.1 [FT]; our β-shape estimate 0.0019, WP8F-C13;
³H half-life 12.32 y [UNVERIFIED, standard];
Ge: ³H production natGe 75 ± 26 kg⁻¹d⁻¹ calc., measured 82 ± 21 and 76 ± 6, 1706.05818 Table 1 p.12, Table 2 p.14 [FT]; NaI 83 ± 27 [FT, ibid.]);
intrinsic ³²Si, ¹⁴C (organics) [UNVERIFIED]; dark current/leakage (detector); LEE (§2.8).
**(e)** 𝓡_ER,heavy ∝ (Z/A)·w_acc, w_acc ≡ fraction of ∫ωL below ω_max; light: ∝ L(0,ω ≳ E_g)/ρ_T. Dominant m_χ: from m_min (Si 0.33 MeV, Ge 0.21 MeV
[D]; narrow-gap 2E_g/v² ≈ 0.03 MeV per 0.1 eV) to ≈ 1 GeV, where NR/Migdal take over [E].
**Non-density NR-EFT rows (L3) [D].** j_L is screened like n; j_T through LFE; spin rows unscreened at SOC = 0 (triplet ladder + f_xc^T, ×1.3–2 within
~1 eV of the edge). FOMs per operator class: S_{s^αs^β}/ρ_T (= (δ_αβ/4)S^{IP}_nn/ρ_T at IP), S_{j_Tj_T}/ρ_T. The 𝒪₈ factor ≥ 12× (IP 20–30) is UNRESOLVED
(§4).

### 2.2 Absorption (Cat. A1–A8, A12; LIMITS L9, L9b, L16, B2-L3, L32)
**(a) [D]** WP0-v3 (3.5): Γ_net = −(y_φ²/ω)Im R_OO(k_φ,ω), ℛ = ρ_φΓ_net/(ρ_Tm_φ), with the photon-reducible part (3.6). Per class:
- *Dark photon* (total charge): Γ = κ_mix²m_φ Im[−1/ε(m_φ)] (B2-L3 form), hence **ℛ_A′ = (ρ_φ/ρ_T)κ_mix² L(0,m_φ)**; identical to κ_eff²σ₁ with
  κ_eff² = κ_mix²/|ε|² (WP8F-C11). **FOM_A′(m_φ) = L(0,m_φ)/ρ_T** (same functional as ER-light at fixed ω). Anisotropic targets: polarisation-averaged
  (1/3)Σ_i L_ii (1807.10291 Eq. (40) structure for sapphire [FT p.31]).
- *ALP–electron* (tr J_e row, = current only at SOC = 0, L9b): FOM_ALP ∝ m_φ²ε₂(m_φ)/ρ_T (source prefactor of 2106.12586 [UNVERIFIED], not needed for ratios); **no in-medium 1/|ε|²** at leading order (mixing suppressed); with SOC the spin-current row departs from j by R̃_{s,c} ≠ 0 (Si ≲ 2%, Ge ≲ 10%).
- *Scalar* (n_e suppressed by charge conservation; NLO kinetic row 𝒯_e): FOM_φ = Im Π_φφ(m_φ)/ρ_T with the photon-reducible part (3.6) [D, sketch:
  no closed form beyond (3.5)–(3.6)].
- *ALP in B₀*: dark photon with κ_mix m_φ² → g_aγγB₀m_φ (WP0-v3 (2.9)): FOM_A′ applies, × B₀².
**(b)** The mass reach is supp ε₂(ω) (or of Im R_OO): electronic E_g (indirect edge phonon-assisted, L9: E_g^{ind} ± ω_Q); the polar band [ω_TO,min,
ω_LO,max] (§2.5); TLS below ω ~ T (§2.7); dopants 10–50 meV (LB1-11). Direct and phonon-assisted parts must not be double counted against measured data
(WP3 N4).
**(c)** Dark photon: total ε (incl. ions). **Dirac/narrow-gap: the background dielectric ε_bg enters the total ε; sources' absorption rates are ×ε_bg too large**
(L16, REFEREED R×2 FT; WP4-v3 §5.5). Superconductors: Mattis–Bardeen ε₂ with metallic |ε|² ≈ ω_p⁴/ω⁴ makes FOM_A′ ∝ ω⁴ε₂/ω_p⁴ (finite bodies and films: the
depolarisation/orientation factors of WP7-D IF-D9 apply).
**(d)** Flat Compton and β backgrounds per mass at the line energy; the signal is a line of width set by the halo (δω/ω ~ 10⁻⁶), so 𝓩_B uses the
detector resolution σ_E as the window (§3): 𝓩_B ∝ FOM_A′/√(b_bg σ_E) [D].
**(e)** In-gap transparency (ε₂ → 0) kills the FOM below the edge; above it, FOM_A′ ∝ ε₂/(|ε|²ρ_T): low ε₁ and low ρ_T win. m_φ = ω: meV (phonons) to keV.

### 2.3 Single-phonon nuclear recoil (nucleon coupling; Cat. L1, L2, L8; LIMITS L4, L19)
**(a) [D]** WP2-v3 (2.2), n_ph = 1, c_κ = A_κF^M_κ (**no Z*/ε_∞ factor**, WP2-v3 (4.4)). For q ≪ q_BZ, G = 0 and the rigid acoustic eigenvector
e_κ = √(M_κ/M_cell) q̂ (WP8F-C1a,b):

  S^{(1)}_LA/ρ_T = π q² A_cell²/(M_cell² ω) δ(ω − c_LA q)  →  (π q/(m_u² c_LA)) δ(ω − c_LA q)   (M_κ = A_κm_u),                       (2.3a)

**independent of A and of the composition** for c_κ ∝ A_κ (f_p = f_n) and M_κ = A_κm_u: the coherent A² gain is cancelled exactly by the per-mass normalisation. The only material parameter left is
the sound speed c_LA (and its anisotropy). The optical branch at q ≪ q_BZ couples through the mass-weighted difference ∝ (A₁/M₁ − A₂/M₂)-type
combinations, ≈ 0 for c_κ ∝ M_κ (WP2-v3 (2.2) at Γ; [D]); it reopens through Umklapp (q ~ q_BZ) and through the electron row (§2.5).
**(b) [D]** ω = c_LAq ≤ qv − q²/2m_χ requires v > c_LA and gives ω_max = 2m_χc_LA(v_max − c_LA), so

  m_min^{ac} = ω_th/(2c_LA(v_max − c_LA))   (WP8F-C2).                                                                              (2.3b)

**Opposite roles of c_LA:** the rate coefficient ∝ 1/c_LA, the edge ∝ 1/c_LA. Illustration [DB-derived, isotropic Voigt average of JARVIS K, G, ρ
(OptB88vdW): `bulk_modulus_kv`, `shear_modulus_gv`, `density`]: c_L = 18.0 (C, JVASP-91), 12.3 (3C-SiC, JVASP-8158), 10.8 (Al₂O₃, JVASP-32), 8.7 (Si,
JVASP-1002), 4.8 (GaAs, JVASP-1174; Ge, JVASP-890), 2.9 km/s (NaI, JVASP-1996); m_min^{ac}(1 meV) = 3.2, 4.7, 5.3, 6.5, 11.8, 19.3 keV (WP8F-C12). Cross-check:
the DB c_T–c_L range of GaAs (2.9–4.8) brackets "c_s ∼ 4000 m/s in GaAs and c_s ∼ 10⁴ m/s in sapphire" (1807.10291 p.6 [FT]) (WP8F-C12a,b).
**(c)** R_NN = R̃_NN + R̃_Ncε⁻¹v_CR̃_cN (WP0-v3 (5.3)): ionic screening enters via the NA eigenvectors; no external dielectric factor.
**(d)** Neutron (radiogenic, cosmogenic) NR, coherent ν (high-mass end), LEE (§2.8) at ω ≲ 100 meV. Phonon-sensor thresholds are set by the detector,
not the FOM.
**(e)** 𝓡_1ph ∝ 1/(m_u²c_LA) × halo kinematics; dominant m_χ ≈ 10 keV–10 MeV [E] (Umklapp dominates the heavy-mediator rate above ~1 MeV, 1910.08092 p.30
[FT] text). Cubic isotropy theorem (WP2-v3 (8.2)): no harmonic incoherent modulation in Si/Ge/GaAs; anisotropic c_ν (sapphire, SiC) is the modulation
input (L19).

### 2.4 Multiphonon to impulse nuclear recoil (Cat. L3–L7; LIMITS L5, L6, L18)
**(a) [D]** WP2-v3 (3.1)–(3.2): S_inc/ρ_T = (2π/M_cell)Σ_κ|c_κ|²e^{−2W_κ}Σ_{n≥1}w_κ^{*n}/n!, w_κ = (q²/2M_κ)D_κ^{q̂}(ω′)[n_B + 1]/ω′. The first moment per mass is
(2π/M_cell)Σ_κA_κ²q²/(2M_κ) = πq²/m_u² (M_κ = A_κm_u): **composition-free**, as in (2.3a); the zeroth moment at large q (e^{−2W} → 0) is
(2π/M_cell)Σ_κA_κ² = (2π/m_u)Σ_κA_κ²/A_cell ≈ 2π⟨A⟩/m_u (WP8F-C1c): **impulse-limit FOM per mass ∝ A** at fixed ω-integrated detection (coherent A² × 1/A per mass), × μ_χN² F_Helm² at
m_χ ≳ M_κ. In between, the fraction of the f-sum above threshold at fixed q is the Poisson tail P[Pois(2W_κ) ≥ ⌈ω_th/ω_max^ph⌉] (WP2-v3 (3.4′)),
2W_κ ≈ q²/(2M_κω̄_κ) (ω̄_κ the first DOS moment): the multiphonon FOM rises with **low M_κω̄_κ** (soft, light lattices reach the threshold with fewer q).
**(b) [D]** Phonon-band edge ω_max^ph (largest phonon energy) for n_ph = 1; free NR m_min = √(M_κE_th/2)/v_max (m_χ ≪ M_κ; WP8F-C9): at E_th = 10 eV,
104 (O), 137 (Si), 220 MeV (Ge). In charge readouts E_th is in nuclear-recoil energy (E_th^{ee}/QF; QF is (prov.)).
**(c)** As §2.3. **(d)** As §2.3, plus the NR partition (WP5 L20–L22; prov.). **(e)** ∝ A (impulse), ∝ (M_κω̄_κ)⁻ⁿ in the n-phonon window; dominant
1 MeV–10 GeV [E]. Anharmonic corrections (L18) enter with type T (θ_A scaled by η_anh = 0.01–0.03); 2309.10839 reports up to ~10² at MeV masses
[ABS, via CATALOG-A], so the multiphonon FOM is the class with the largest theory spread at fixed ω_th (§4).

### 2.5 Polar phonons, phonon polaritons and dark-photon mixing (Cat. L2, A4, A5; LIMITS L4, B2-L1)
**(a) [D]** WP2-v3 (4.2) is exact at rank 1 (total ε ≡ Born-charge one-phonon formula). For the dark-photon-mediated (charge) coupling with F_DM = (αm_e/q)²,
WP2-v3 (4.3) gives Γ_χ ∝ e_χ²e²·ω_L(1/ε_∞ − 1/ε₀) per branch, and in general

  𝓡_pol ∝ 𝓘_pol/ρ_T,   𝓘_pol ≡ ∫_{ionic band}dω L(0,ω) = Σ_ν(πω_Lν/2)Δ_ν,   Σ_νΔ_ν = 1/ε_∞ − 1/ε₀,                                   (2.5a)

the same functional as integrated dark-photon absorption over the band (§2.2). For a diatomic polar crystal (WP8F-C3)

  ω_L(1/ε_∞ − 1/ε₀) = e²Z*²/(Ω μ_red ε_∞² ω_L)   ⇒   per mass 𝓘_pol/ρ_T = (π/2)e²Z*²/(M_cell μ_red ε_∞² ω_LO).                          (2.5b)

**Scaling:** ∝ Z*²/(ε_∞²M_cellμ_redω_LO): light, ionic (large Z*), low-ε_∞ crystals win. **Si, Ge: Z* = 0, vertex quadrupolar, S ∝ q⁴** (WP2-v3 (4.5)).
**(b)** Edge 2ω_LO/v_max² (one branch) or 2ω_L,ν/v_max² for the lowest polar branch reached: GaAs ≈ 9.7 keV (ω_LO ≤ 34 meV, "the highest phonon energy in
GaAs", 1910.08092 p.30 [FT]); sapphire 13.7–32.0 keV from 387.6–906.6 cm⁻¹ (1807.10291 Table II p.31 [FT]) (WP8F-C17).
**(c)** Built in (total ε). Electron-only scalar row: LO residue Z_κ − Z*_κ/ε_∞ with near-cancellation, GaAs ≈ 0.11 of the source structure, **46% per 10%
in Z*/ε_∞** (B2-L1): that FOM is an order-of-magnitude quantity only.
**(d)** As §2.3. **(e)** Numbers [FT]: GaAs (ε_∞ 10.89, ε₀ 12.9, ρ_T 5.32 g/cm³; 1807.10291 Table I p.11) gives 𝓘_pol/ρ_T ≤ 0.144 meV cm³/g; sapphire ordinary ray
(ε_∞ 3.2 Table I; four modes Table II with widths) 9.40 meV cm³/g, ×65 GaAs (WP8F-C15). FT-vs-FT check: multi-mode LST from Table II reproduces Table I's
ε₀ to 5% (9.78 vs 9.3 ⊥; 12.10 vs 11.5 ∥) (WP8F-C5). Dominant m_χ 10 keV–10 MeV [E]. **DB-only bracket:** (8.1) below.

### 2.6 Magnons (e-spin coupling; Cat. S1, S2, S6; LIMITS L13, B2-L6, B2-L7)
**(a) [D]** WP4-v3 [2.1]–[2.2] in (3.3): Σ𝔇S = (2π/Ω)Σ_ν⟨|Σ_α𝒱_{s^α}ℰ^α_ν|²⟩δ(·), ℰ ∝ λ_{S,j}F^{mag}_j√(|𝐒_j|/2)(U^B, V^B). One sublattice gives 1905.13744
Eq. (12) with n_s = |𝐒|/Ω [FT-R7 via WP4-v3]. Per mass:

  𝓡_mag ∝ 𝓃_S/ρ_T × ⟨|F^{mag}(q)|²⟩_q × (Bogoliubov weight),   𝓃_S ≡ Σ_j λ_{S,j}²|𝐒_j|/Ω.                                              (2.6)

**(b)** Δ_mag (k → 0 gap: anisotropy, Kittel ω = γB in a field) and ω_max^mag (zone boundary ~ 2zJ^{ex}|𝐒| [E]); edge 2Δ_mag/v_max² for a gapped branch,
or the acoustic-magnon analogue of (2.3b) with the spin-wave velocity for gapless FM/AFM branches [D, by the same algebra].
**(c)** Not Coulomb-screened at SOC = 0; with SOC R̃_{s,c} ≠ 0 at relative order (λ_SO/Δ_CF)² [E]. **(d)** Same as ER plus magnetic-field noise; the
quasi-static field B₀ is an experimental knob (S2). **(e)** ∝ 𝓃_S λ_S²/ρ_T; |F^{mag}|² ≈ 0.5 at 0.5 keV for Fe³⁺ (WP4-v3 §2.1 [E]) bounds the useful
q, so m_χ ≈ keV–MeV; two-magnon O(1/(2|𝐒|)) (0.2 YIG, 0.5 for |𝐒| = ½) adds a continuum (WP4-v3 [2.4]); Si/Ge have no magnon FOM. Absorption into the
Kittel mode (B2-L6): FOM ∝ 𝓃_S/ρ_T × (linewidth-limited resonant enhancement); λ_S = g_J − 1 only for J multiplets. Data route (B2-L7, `src=data`): P_T
only, quenched-ion bracket ≈ 0.83 for Ni²⁺.

### 2.7 PAER and Migdal (Cat. X2–X7, §11; LIMITS L7a–d, L8, L12)
**PAER (a) [D]** WP0-v3 (5.6): S^{X+}_ee = (2q²/e²)L^{PA}; FOM 𝓡_PAER = ER functional (2.1a) with L → L^{PA}, inputs: screened e–ph vertex g (EPW
convention), indirect band structure, ω_ν(Q). **(b)** Edge E_g + ω_TA(Q*) (continuum, Si ≈ 0.337) or E_x + ω_TA(Q*) (replica, ≈ 0.333 MeV) [E]; the
**PAER window** [m_PAER, m_ZPL] (Si PAER-only ≈ 0.333–0.42 MeV; Ge ≈ 0.213–0.32 MeV; WP6-v3 (3.1) (iii)) requires an indirect gap with E_min(q) of the
zero-phonon line well above E_g^{ind} + ω_ν: **window FOM** Δm_PAER/m ≡ (2E_min^{ZPL}(q*) − 2(E_g + ω_TA))/(2(E_g + ω_TA)). Direct-gap materials have no
PAER window. **(c)** External ε̃⁻¹ with LFE, DFPT g, pair channel W^{scr} (X2 (2.2)): interim factor [0.4, 1.8], median 0.85, σ_ln 0.75.
**(e)** Onset exponent p̄_on = 3 (13/2 + k_tail edge exponent), so the near-edge PAER FOM inherits the 0.15%-level E_th sensitivity (WP8F-C14b).
**Migdal (a) [D]** L7b (WP3-v3 §2; 2011.09496 Eq. (6) [FT]): dP/dω = 4α∫d³k/(2π)³ Z_κ(k)²|v_N·k|²Im[−1/ε(k,ω)]/(ω⁴k²). With the free-NR cross section at fixed σ_n,
dσ/dE_N = M_κA_κ²σ_n/(2μ_n²v²), and E_N ≤ 2μ_N²v²/M_κ, the per-mass rate (flux ρ_χ/m_χ excluded, as in 𝓡) integrates to (WP8F-C8)

  𝓡_Mig ∝ (A_κ²/M_κ³) μ_N⁴/μ_n² · Z_κ² 𝓜_Mig(ω),   𝓜_Mig(ω) ≡ ∫d³k L(k,ω)/(3(2π)³ω⁴).                                          (2.7)

In the regime m_n ≪ m_χ ≪ M_κ (μ_n ≈ m_n, μ_N ≈ m_χ) this is ∝ m_χ⁴/(A_κm_u³m_n²) × Z_κ²𝓜_Mig; for m_χ ≲ m_n, μ_n ≈ m_χ and the power drops to m_χ².
The m_χ power depends on what is held fixed (σ_n here); the **material scaling Z_κ²𝓜_Mig/A_κ per mass** does not. **Light nuclei win** (1/A per mass at fixed m_χ), × the ELF moment weighted by ω⁻⁴ (low gaps, low screening). **(b)** ω ≥ E_g (ionisation), and the NR
must be in the impulse regime for (2.7): onset 91.5/112 keV (m18) in Si/Ge for x_R; small-q EFT (L7c) below, with (4.8) 2× UNRESOLVED. **(c)** Total ε in
L; boost mass M_κ + δM_κ (crystal). **(d)** As ER + NR. **(e)** Dominant 10 MeV–1 GeV [E]; soft-limit modulation vanishes in cubic crystals (no ℓ = 2
moment, WP3-v3 §2 L7b (v)).

### 2.8 TLS, defects and the low-energy-excess proxies (Cat. L10, A7, D1–D5; LIMITS L25–L32, L33–L38, B2-L10)
**(a) [D]** (i) *Dark photon → TLS* (L32): ℛ_A′ = ρ_φκ_mix²tanδ₀tanh(m_φ/2T)/(ρ_Tε_r): **FOM_TLS,abs = tanδ₀/(ρ_Tε_r)** — a clean scalar; the tanδ₀ input is
material- and preparation-specific (1705.01108 quotes 1.6×10⁻³ for AlOx and 2.5×10⁻⁵ for a-Si:H at 4.2 K; neither is an a-SiO₂ value, L32 caveat).
(ii) *DM–TLS scattering* (WP7-T §2.4): a-SiO₂, m_χ = 1 MeV, σ̄_e = 10⁻³⁸ cm²: ≈ 3.7×10⁻² /(kg·day·meV) over ω ≲ 0.1 meV **[E, ×3]**, host + core
incoherent; inputs P̄_STM, deformation coupling, δρ_κ (DFPT), ρ_T, c_ν; priority/novelty UNRESOLVED (G-T7). (iii) *Defect creation and readout*: E_d
threshold and colour-centre yield Y_CC (B2-L10); single-F readout at mK and σ* yields unquantified.
(iv) *Amorphous broadband absorption* (B2-L3): glass ε with C^{IR} = A^{IR} + B^{IR}ω² (A^{IR}, B^{IR} not computed).
**(b)** TLS: ω ≲ T…0.1 meV; damage: E_d ≈ 10–50 eV (Cat. D1).
**(c)** Medium ε_r for the electric TLS coupling; strain coupling unscreened.
**(d) LEE / stored-energy proxies (prov.; WP7-E-v3 §3.2–§3.3, L29, L36–L38) [D for structure, E for numbers].** Three event classes of (E14):
- 𝓟_st (event-seeded): stored power ∝ ℛ_NR,bg × ⟨E_st⟩/E_R × E_R. Data caps (95% C.L., under (B-a)–(B-d)): **⟨E_st⟩/E_R ≤ 0.055 (Si) / 0.064 (Ge);
  p_surv·E_st,1/E_d ≤ 0.21 / 0.20; p_surv ≲ 0.47 / 0.66** (each ≤ 1% wider with ΔZPE) (L36 as corrected). The Si datum is degenerate between E_st and
  collection (r_coll = 1.144 alone reproduces η^φ_NR = 0.952; L38), so 𝓟_st is an **upper-bound proxy**, not a measured property. Single Frenkel-pair
  releases are visible only for E_thr^det ≤ ϵ_collE_st,1 ≈ 2.7 eV; pocket recrystallisation (N_a ≳ 270 at 16.3 eV) is collective.
- 𝓟_TLS (cooldown-seeded): Q̇ = (π²/24)P̄_STMV(T_hi² − T_lo²)/t (L29), valid for Γ_max⁻¹ ≪ t ≪ Γ_min⁻¹: ∝ P̄_STM × amorphous volume (oxides, films,
  glue). **P̄_STM enters the TLS signal FOM (i)–(ii) with + sign and the LEE background with − sign**; a ranking that uses one must use both.
- 𝓟_σ (stress-seeded): mismatch stress ∝ Y_mod·∫Δα_th dT between absorber, film and holder/glue (2208.02790 stress dependence vs 2202.05097 null, both
  [FT via WP7-E-v3]; reading [C]). Inputs: Young's modulus Y_mod and integrated thermal contraction of each layer to mK.
**(e)** FOM_TLS,abs ∝ tanδ₀/(ρ_Tε_r); 𝓟_TLS ∝ P̄_STM; 𝓟_st ∝ E_st,1p_surv/E_d (prov.). These proxies rank backgrounds, they do not predict a rate.

**Radiopurity and activation (all classes; background-relevant quantities) [structure D; values as tagged].** Per element of the formula unit: (i)
natural-abundance radioisotopes that no purification removes (⁴⁰K, ⁸⁷Rb, ¹¹³Cd, ¹¹⁵In, ¹³⁸La, ¹⁷⁶Lu, ¹⁸⁷Re; [UNVERIFIED] list, specific activities to be
tabulated by WP8-U from NNDC/NIST); (ii) cosmogenic production per kg-day at sea level (³H above; ⁷Be, ²²Na in Si; ⁶⁸Ge, ⁶⁵Zn in Ge [UNVERIFIED]); (iii)
²¹⁰Pb/U/Th surface and bulk contamination (process, not material). Each enters 𝓩_B through b_bg in the ROI: e.g. ³H per exposure day contributes
≈ 0.002 /kg/keV/day in Si below 5 keV, set against the FOM in the same window.

---
## 3. Projected reach: background-free and background-limited scalars [D]
With exposure MT, signal rate density 𝓻_s(E) = σ·𝓡-density (linear in the coupling², σ), background rate density b_bg(E) per mass, ROI efficiency
ϵ_cut (WP8F-C10):
- **Background-free** (MT∫b_bg ≪ 1): N_s = 2.303 at 90% C.L. ⇒ σ_lim = 2.303/(𝓩_0 MT), **𝓩_0 ≡ ϵ_cut 𝓡** (the rate FOM above threshold). Reach is then
  rate-limited, and m_min (where 𝓡 → 0) governs the low-mass end.
- **Background-limited** (Poisson, s ≪ b): Asimov Z² = 2Σ[(s + b)ln(1 + s/b) − s] → Σs²/b ⇒ σ_lim = Z/(𝓩_B√MT), **𝓩_B ≡ [∫dE 𝓻̂_s(E)²/b_bg(E)]^{1/2}**
  (𝓻̂_s = 𝓻_s/σ); flat shapes give 𝓩_B = 𝓡/√(b_bg ΔE). Shape differences (absorption lines, ER edges, NR exponentials) enter only here.
- **Systematics-limited** (fractional background uncertainty f_sys, MT f_sys²b_bg ≫ 1): σ_lim → Z f_sys b_bg/𝓡, **exposure-independent** (WP8F-C10d). The LEE
  (§2.8) and ³H are of this type until modelled.
Which governs: background-free while N_b ≡ MT∫b_bg dE ≪ 1 (rank by 𝓩_0); crossover at N_b = O(1); then rank by 𝓩_B ∝ 𝓡/√b_bg; once
f_sys²N_b ≳ 1, by 𝓡/(f_sys b_bg). **One scalar per channel** (Table §5.1): 𝓩_0 = ϵ_cut𝓡_class above E_th^det; 𝓩_B = 𝓡_class/√(b_bg ΔE_ROI) with the class
ROI (ER: [E_g, E_g + 10 ε_eh]; ABS: [m_φ ± 2σ_E]; NR-1ph: [ω_th, ω_max]; POL: ionic band; MAG: [Δ_mag, ω_max^mag]; TLS: [0, 0.1 meV]).

---
## 4. Uncertainty inherited by each FOM
**(4.1) WP6-v3 nuisance types (5.2) per class** (types M, A, E, Δ, T; no new types):
| FOM | Nuisances (WP6-v3 (5.2) row → type, prior) | Effect on the FOM |
|---|---|---|
| ER-ρ, ER-light | kernel ladder 𝒳 (M, central ×1.61, σ_ln 0.22 near the edge; bound-exciton lines A, σ_ln 0.5); XC/gap (E: 1 meV scissored, 60 meV unrenormalised); screened rows (M); q_max tail (closed); k-grid (half-normal M) | near-edge FOM ×e^{±0.22}; m_min ±0.1% (scissored) to ±5% (clamped gap) |
| ER near-edge, PAER | gap convention E; edge construction Δ + E (σ_E ≈ 2 meV on ω_TA(Q*)); n_g = 2 A with [0.4, 1.8] (median 0.85, σ_ln 0.75); thermal order A | PAER FOM ×e^{±0.75}; near-edge rate log-sensitivity ≈ 132 × δE/E |
| ABS (A′, ALP) | measured σ₁ (no model nuisance if data are used, `src=data`); ε_bg (Dirac, L16 factor); SOC split for ALP (≲ 2% Si, ≲ 10% Ge) | DB ε₂ from DFT carries the XC/gap E-type row |
| NR-1ph, POL | n_A = 0 harmonic (T, η_anh small at T = 0); Born-charge/ε_∞ inputs as M on scalars (Z*², ε_∞⁻² → ×2 log-sensitivity) | (2.5b): δln𝓘 = 2δlnZ* − 2δlnε_∞ |
| NR-mph | phonon order K (one-sided M, P[Pois(2W) ≥ N]); anharmonic T (θ_A, θ_δ) | the largest spread (source: up to ~10², [ABS]) |
| Migdal | n_B (negligible); impulse/EFT regime choice Δ; ELF from 𝒳 rung (M) | ∝ 𝓜_Mig, inherits ER-ρ rows |
| MAG | none in WP6-v3 (5.2) beyond XC; LSWT validity 1/(2\|𝐒\|), F^{mag} form factor → **new M-type row proposed** (IF-F4) | ×(1 ± 0.2…0.5) [E] |
| SC targets | WP6-v3 SC row: first-order screening term in central, residual M ≤ 16% at y_BCS = 5 | — |
| All yield-dependent (prov.) | yield/cascade Δ + M (ε_eh 𝒩(3.75, 0.05) eV); F_eh M; θ_st, θ_coll joint (WP7-E §6, degenerate via η^φ_NR); θ_tr^{pr} T (f₀ = 10⁻³) | threshold in quanta; LEE proxies |
| Halo | separate band (not profiled): v_max ±1.8% annual, v_esc 2–7% | m_min ±3.6% annual; 4–14% from v_esc |
**(4.2) UNRESOLVED LIMITS rows touching each class** (the FOM inherits the stated factor until resolved):
ER: L3 (𝒪₈ ≥ 12×, IP 20–30, factor UNRESOLVED), L11 (×1.4 replaces ×(5/1.9)²), LB1-5 (QD prefactor; depolarisation size/sign), LB1-11 (Eq. (12) 3q̃² impact),
LB1-13 (relativistic (1 − ω²/Q²)² impact on limits), L-D8 (Xe single-point ratios; "paper wrong" UNRESOLVED). ABS: L9b (1608.01994 O(1) only within ≈ 20–25 meV),
L-D1 (amplitude factor 2), L-D10 (attribution). POL: B2-L1 (2308.06314 Fig. 2 projection; GaAs electron row order of magnitude only). NR: L5/2011.09477 and
1911.03482 agreements UNRESOLVED as quotes; B2-L4 (Born validity: V_opt/E_kin = 1.3–1.9 at the source's reach); isotope B−L channel novelty. Migdal: L7c
((4.8) 2×). TLS: DM–TLS novelty (G-T7), tanδ₀ of a-SiO₂ not quoted. Defects/LEE (prov.): L36 TRIM inference UNRESOLVED; L38 degeneracy (IF-E8).

---
## 5. Interface to WP8-U: properties to tabulate
**(5.1) One scalar per channel (definitions for WP8-U; each evaluated per material).**
| Channel | 𝓩_0 (background-free) | 𝓩_B (background-limited) | Edge |
|---|---|---|---|
| ER-ρ heavy / light | ϵ_cut𝓡_ER,heavy / light (2.1a) | 𝓡/√(b_bg ΔE_ROI) | m_min (3.1′) |
| ABS A′ / ALP | L(0,m_φ)/ρ_T / m_φ²ε₂(m_φ)/ρ_T | ÷√(b_bg σ_E) | supp ε₂ |
| NR-1ph | π/(m_u²c_LA) × halo integral | ÷√(b_bg(ω_th…ω_max)) | (2.3b) |
| NR-mph / impulse | Poisson-tail fraction × ⟨A⟩ | ÷√b_bg | ω_max^ph; √(M_κE_th/2)/v_max |
| POL | 𝓘_pol/ρ_T (2.5a) | ÷√b_bg(ionic band) | 2ω_LO,ν/v_max² |
| MAG | 𝓃_S⟨\|F^{mag}\|²⟩/ρ_T | ÷√b_bg | Δ_mag, spin-wave velocity |
| PAER | 𝓡_PAER, window Δm_PAER/m | ÷√b_bg | E_g + ω_TA(Q*) |
| Migdal | Z_κ²𝓜_Mig/A_κ | ÷√b_bg | E_g at impulse onset |
| TLS abs / DM–TLS | tanδ₀/(ρ_Tε_r) / P̄_STM-weighted (WP7-T) | ÷√(b_bg incl. 𝓟_TLS) | T, 0.1 meV |
**(5.2) Property list with units and needed accuracy.** Needed accuracy = δ_rank/|∂ln FOM/∂ln x| with ranking resolution δ_rank = 0.2 in ln FOM [E]
(WP8F-C14); "DB accuracy" is the observed scatter of the JARVIS fields against [FT]/campaign values in this return.
| Property | Unit | Enters | \|∂lnFOM/∂lnx\| | Needed | DB accuracy observed / source |
|---|---|---|---|---|---|
| ρ_T | g/cm³ | all per-mass FOMs | 1 | 20% (5% for ER near edge) | JARVIS `density` OptB88: Si 2.25, Ge 5.054, GaAs 5.102 vs FT 5.32: −4% [DB vs FT]; use measured |
| E_g (indirect, direct), E_x^b, E_min(q) | eV | ER, PAER, ABS edges | 1 (edge); ≈ 132 near edge | 1% (edge); 1–2 meV (near-edge, PAER) | JARVIS `optb88vdw_bandgap` Si 0.731, GaAs 0.085; `mbj_bandgap` 1.277/1.321; HSE 1.22 (Si): DB gaps fail the near-edge need; use measured E_g(T_op) (WP6 E-row) |
| ε_∞ (tensor), ε₀ (tensor) | — | POL (2.5), ER screening, ABS | 2 (POL) | 10% | JARVIS `mepsx` Si 10.74, `epsx` 13.49 vs 11.7 (WP1-v3): ±15%; GaAs `dfpt_..._electronic` = 3097.9 (metallic OptB88 gap): **unusable**; vet per entry |
| Z*_κ (tensor), ω_TO,ν, ω_LO,ν | e; meV | POL, ABS phonon band, B2-L1 | 2 (Z*); 1 (ω_LO) | 10%; 0.5–1 meV for edges | JARVIS `max_ir_mode` zincblende = 1.77 cm⁻¹ (GaAs) — acoustic, not optical: **unusable**; Al₂O₃ 613.17 cm⁻¹ vs FT TO 633.6: −3% |
| L(q,ω), ε₂(ω) (measured or computed) | — | ER, ABS, Migdal, PAER | 1 | 20% in the accessible window | measured optical data preferred (`src=data`); never add computed sideband to data (WP3 N4) |
| c_LA, c_TA (directional) | km/s | NR-1ph rate and edge | 1 | 20% (rate), 5% (edge at fixed ω_th) | JARVIS K, G (Voigt): GaAs 2.9–4.8 bracket FT 4.0; anisotropy needs the elastic tensor (`elastic_tensor`) |
| phonon DOS D_κ(ω), ω̄_κ, ω_max^ph | meV⁻¹; meV | NR-mph, PAER, TLS host | 1–n (Poisson tail) | 10% in ω̄ | DFPT (JARVIS `modes`) or INS data |
| M_κ, A_κ, Z_κ, composition | u | all | 1 | exact (isotopic composition for B−L) | standard atomic weights |
| 𝓃_e (valence/core split), Z/A | Å⁻³ | ER ceiling, L17 | 1 | 5% | from composition (WP8F-C7) |
| v_F, k_TF, Δ_BCS (metals/SC) | km/s; keV; meV | ER-SC, ABS-SC | 2 (k_TF), 1 (v_F) | 10% k_TF | literature |
| ε_bg, v_F, g_deg, Δ_D (Dirac) | —; km/s; —; meV | ER/ABS Dirac (L16) | 2 (ε_bg) | 10% | literature |
| 𝓃_S, λ_{S,j}, \|𝐒_j\|, J^{ex}, Δ_mag, F^{mag}(q) | Å⁻³; meV | MAG | 1 | 20%; Δ_mag 5% | DFT+U / neutron data |
| e–ph matrix elements g (EPW), ω_ν(Q*) | meV | PAER | 2 | 10%; ω_TA(Q*) ±2 meV | EPW/ZG (tier H, pre-registered) |
| tanδ₀(T, ω), ε_r, P̄_STM, TLS deformation coupling | —; J⁻¹m⁻³ | TLS signal **and** 𝓟_TLS | 1 | factor 2 (log-normal) | preparation-specific; measured |
| E_d, E_st,1, p_surv (prov.) | eV | damage threshold, 𝓟_st | 1 | 20% | MD; data caps L36 (one-sided) |
| ε_eh, F_eh, y_ion, QF (prov.) | eV | thresholds in quanta | 1 | 2% (ε_eh) | WP5-v3 / WP7-E-v3 |
| Y_mod, ∫Δα_th dT (absorber, film, holder) | GPa; — | 𝓟_σ | 1 | 30% | literature |
| intrinsic radioisotope abundances/activities; cosmogenic production (kg⁻¹d⁻¹) | Bq/kg; kg⁻¹d⁻¹ | b_bg in 𝓩_B | ½ | 50% (√ inside 𝓩_B) | NNDC/NIST [UNVERIFIED here]; ³H FT values §2.1 |
| thermal-cycling survival, gram-scale synthesis, sensor compatibility | pass/fail | FRAMEWORK qualifiers 1–3 | — | — | WP8-U |
**(5.3) DB vetting rules found here [D from the pulled data].** (i) OptB88vdW gaps are unusable for edges (Si 0.731 eV); MBJ within ≈ 10%. (ii) DFPT
dielectric and IR-mode fields are invalid when the OptB88 gap is ≈ 0 (GaAs) or the listed "max IR mode" is ≤ 5 cm⁻¹ (acoustic) — require ω_max,IR > 50 cm⁻¹
and gap > 0.3 eV. (iii) Several formulae return a non-ground polymorph first (NiO ehull 0.128; MgO JVASP-116 ehull 0.030 behind an I4/mmm entry; NaI P6₃/mmc
before rocksalt): select by space group and ICSD tag. (iv) CsI and Y₃Fe₅O₁₂ are absent from the JARVIS OPTIMADE dft_3d results queried (empty responses).

---
## 6. Literature (IDs verified against the arXiv API, 2026-11-01; PDFs fetched into literature/papers-WP8-F/ and deleted)
| ID | Used for | Status |
|---|---|---|
| 1807.10291 (Directional detection of light DM with polar materials) | GaAs/sapphire ρ_T, ε₀, ε_∞ (Table I p.11); sapphire modes (Table II p.31); c_s (p.6); Eq. (40) | [FT] |
| 1910.08092 (Multi-channel direct detection: theoretical framework) | "34 meV, the highest phonon energy in GaAs"; Umklapp dominance above ~1 MeV (p.30) | [FT] |
| 1706.05818 (Cosmogenic production of tritium in DM detectors) | ³H rates Ge, NaI (Tables 1–2, pp.12, 14) | [FT] |
| 2506.06568 (Removal of spallation-induced tritium from silicon) | Si ³H 124 atoms/kg/day; 0.002 /kg/keV/day per exposure day (p.1) | [FT] |
| 2205.02250 | fetched; long-wavelength approximation wording only (§III A) | [FT], no number used |
| JARVIS-DFT OPTIMADE (jarvis.nist.gov/optimade/jarvisdft) | JVASP-1002, -890, -91, -1174, -8158, -32, -39, -30, -116, -1996, -1130, -20800, -23, -1702, -1189, -14615, -14818, -1044 | [DB] |
Cited through campaign returns (quotes not re-read here), IDs also API-verified 2026-11-01: 2004.11499, 1705.01108, 2208.02790, 2202.05097, 1905.13744, 2308.06314,
2309.10839, 2101.08275, 1610.03974, 2106.12586, 2110.01587, 2011.09496.
Sources' halos (1807.10291: v₀ = 220, v_esc = 500 km/s; 1905.13744 similar) are not the campaign halo (CONVENTIONS §8); no source rate is reused here.

## 7. Exact remaining gaps
- G-F1: no closed form for the scalar-absorption FOM beyond (3.5)–(3.6) (needs Π_φφ, Π_φA per material).
- G-F2: the multiphonon FOM needs the anharmonic spread computed (L18 type T) before ranking at ω_th ≳ ω_max^ph.
- G-F3: LEE proxies are bounds (𝓟_st) or structure only (𝓟_σ); no predictive LEE rate exists (WP7-E G-E2) (prov.).
- G-F4: magnon FOM uncertainty has no WP6 row (IF-F4).
- G-F5: the PAER window FOM needs E_min^{ZPL}(q*) and ω_ν(Q*) ab initio (tier H).

## 8. The DB-only polar bracket [D]
**(8.1)** For a lossless factorised ε(ω) = ε_∞Π_ν(ω_Lν² − ω²)/(ω_Tν² − ω²) with interlaced ω_T1 < ω_L1 < ω_T2 < …, the Kramers–Kronig identity at ω = 0 for
1/ε gives ∫₀^∞dω L/ω = (π/2)(1/ε_∞ − 1/ε₀) over the ionic band (WP8F-C4b,c), and with ω_Lν ∈ [ω_T,min, ω_T,max√(ε₀/ε_∞)] (each ratio ω_Lν/ω_Tν ≥ 1, product
√(ε₀/ε_∞) by LST):

  (π/2)(1/ε_∞ − 1/ε₀) ω_T,min ≤ 𝓘_pol ≤ (π/2)(1/ε_∞ − 1/ε₀) ω_T,max √(ε₀/ε_∞).                                                        (8.1)

It needs only the DFPT fields ε_∞, ε₀ and the IR-mode range. Checked on sapphire with FT modes and widths (o: 15.8 ≤ 37.4 ≤ 45.4 meV; e: 17.8 ≤ 39.2 ≤ 50.7)
(WP8F-C6); from JARVIS [DB] per mass (meV cm³/g): Al₂O₃ JVASP-32 [4.2, 13.6] (contains the FT 9.40, WP8F-C6x), AlN JVASP-39 [4.2, 6.6], MgO JVASP-116
[4.7, 8.5], GaN JVASP-30 [1.3, 1.8] (fields `dfpt_piezo_max_dielectric_electronic`, `_ionic`, `min_ir_mode`, `max_ir_mode`). Damping moves 𝓘_pol by < 1%
(WP8F-C4a). Validity: harmonic, one principal axis at a time, IR modes = TO modes.

---
## Symbols introduced/used
| Symbol | Meaning | Status |
|---|---|---|
| 𝓡_a, 𝓡_class (𝓡_ER,heavy, 𝓡_ER,light, 𝓡_1ph, 𝓡_pol, 𝓡_mag, 𝓡_PAER, 𝓡_Mig) | rate FOM per class at fixed coupling, per target mass | **new** |
| 𝒦_a(q,ω;m_χ) | kinematic factor qF_DM,a²η/(4π²) | **new** (not 𝒢) |
| 𝓩_0, 𝓩_B | background-free and background-limited reach scalars | **new** |
| 𝓻_s, 𝓻̂_s, b_bg, ϵ_cut, f_sys, ΔE_ROI, δ_rank | signal and background rate densities per mass, cut efficiency, fractional background systematic, ROI width, ranking resolution | **new** |
| 𝓘_pol, Δ_ν | integrated ionic-band ELF ∫L dω; per-branch weight of 1/ε_∞ − 1/ε₀ | **new** |
| 𝓜_Mig(ω) | ω⁻⁴-weighted ELF moment of the Migdal soft limit | **new** |
| 𝓃_S | spin weight density Σ_jλ_{S,j}²\|𝐒_j\|/Ω (1905.13744's n_s for one sublattice, λ_S = 1) | **new** |
| Δ_mag, ω_max^mag, ω_max^ph, ω_T,min/max, μ_red, Y_mod, Δα_th | magnon gap, magnon/phonon band tops, IR-mode range, reduced cell mass, Young's modulus, thermal contraction | **new** |
| m_min^{ac}, Δm_PAER/m, w_acc | acoustic edge (2.3b); PAER window FOM; accessible f-sum fraction | **new** |
| 𝓟_st, 𝓟_TLS, 𝓟_σ | LEE proxies (event-, cooldown-, stress-seeded) (prov.) | **new** |
| used unchanged | ρ_T, ρ_χ, ρ_φ, Ω, M_cell, M_κ, A_κ, Z_κ(k), Z*_κ, ε_∞, ε₀, ε₂, ε_bg, L, L^{PA}, S, S_ab, 𝔇, 𝒱_a, F_DM, η, v_max, m_min, E_th, E_g, E_x, E_min(q), δ_v,0, p̄_on, k_tail, c_ν (c_LA, c_TA), D_κ^{q̂}, w_κ, 2W_κ, ω̄_κ (WP2 "ω̄_d" source), κ_mix, g_aee, g_aγγ, y_φ, Π_φφ, R̃_{s,c}, λ_{S,j}, 𝐒_j, F^{mag}_j, U^B, V^B, P̄_STM, tanδ₀, ε_r, Y_CC, E_d, E_st, E_st,1, p_surv, η^φ_NR, r_coll, δ_coll, ε_eh, F_eh, y_ion, g_Luke, Q̇, T_hi, T_lo, Δ_BCS, y_BCS, v_F, k_TF, 𝓃_e, ω_p, θ_* | NOTATION v4 + R9/WP7/WP7-E rows |
| WP8F-C1…C17, (1.1)–(8.1), G-F1…G-F5, IF-F1…IF-F7 | labels (prefix WP8-F) | labels |

## Interface flags
| # | Owner | Item | Action |
|---|---|---|---|
| IF-F1 | WP8-U | §5.1 scalars, §5.2 property list, §5.3 DB vetting rules | tabulate; rank per channel with δ_rank = 0.2 and report rank stability under §4 nuisances |
| IF-F2 | WP8-U | the P̄_STM double role (signal + 𝓟_TLS), and c_LA double role (rate vs edge) | rank on 𝓩_B with b_bg including 𝓟_TLS; report both 𝓡 and m_min |
| IF-F3 | WP5-v4 / joint WP5 + WP7-E audit | all (prov.) rows (ε_eh, F_eh, y_ion, QF, E_st caps, 𝓟_st) | confirm or replace before WP8-U uses them |
| IF-F4 | WP6 | magnon FOM nuisance (LSWT 1/(2\|𝐒\|), F^{mag}(q)) | add an M-type row to (5.2) |
| IF-F5 | WP8-R | c_ν, D_κ(ω), film/substrate acoustic mismatch inputs of §5.2 | shared property table |
| IF-F6 | coordinator / NOTATION | §Symbols "new" rows | add rows (𝓡, 𝓩_0, 𝓩_B, 𝓘_pol, 𝓜_Mig, 𝓃_S, 𝓟_*) |
| IF-F7 | coordinator | JARVIS fields that failed vetting (GaAs DFPT, zincblende max_ir_mode) | note in WP8-U brief: DB values need the §5.3 filters |

## Proposed LIMITS rows (numbers provisional; the coordinator assigns)
| # | Chain (URF) | Source formula | Validity | Leading correction | Status |
|---|---|---|---|---|---|
| L-F1 | WP2-v3 (2.2), n_ph = 1, G = 0, rigid acoustic e_κ, ÷ρ_T → (2.3a) π q/(m_u²c_LA) | per-mass statement of the coherent acoustic rate; 2205.02250 §III A long-wavelength form [FT] | q ≪ q_BZ; c_κ ∝ A_κ with M_κ = A_κm_u; harmonic | binding mass defect O(10⁻³); dispersion ω_LA(Q) ≤ c_LAQ; Umklapp | CLAIMED (WP8F-C1) |
| L-F2 | WP2-v3 (4.2)–(4.3) + LST → (2.5b); KK of 1/ε at ω = 0 → bracket (8.1) | 1807.10291 Eq. (32) one-branch \|ℳ\|² (via WP2-v3) | rank-1 macroscopic ε; lossless factorised ε; interlaced modes | damping < 1% (C4a); anisotropy per principal axis; quadrupolar terms in Z* = 0 crystals | CLAIMED (WP8F-C3–C6) |
| L-F3 | L7b soft limit × free-NR dσ/dE_N at fixed σ_n → (2.7) ∝ (A_κ²/M_κ³)μ_N⁴/μ_n², i.e. Z_κ²𝓜_Mig/A_κ per mass | 2011.09496 Eq. (6) [FT via WP3-v3] | impulse regime; soft limit; m_χ power stated for m_n ≪ m_χ ≪ M_κ | small-q EFT (L7c) below the impulse onset; boost mass δM_κ | CLAIMED (WP8F-C8) |
