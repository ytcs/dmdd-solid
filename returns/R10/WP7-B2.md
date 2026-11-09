# R10 / WP7-B2: lattice, spin, amorphous, defect and Migdal-absorption channels as explicit URF sector treatments

Theory agent, brief R10/WP7-B2. Architecture: returns/R8/WP0-v3.md (cited "WP0 (n.m)", not re-derived). Neighbours: WP2-v3 (lattice sector), WP3-v3 §2, §4
(Migdal, absorption), WP4-v3 §1–§2, §6 (spin targets, defects), WP5-v3 §3–§4, §6.3 (recoil partition, defects, L22), WP6-v3 (5.1) (nuisance types).
CONVENTIONS.md, NOTATION v4 + R9 rows; state/CORRECTIONS.md read before every quote (no owed correction touches the WP0-v3, WP2-v3 §1–§3, §7, WP3-v3 §4,
WP4-v3 §1–§2, §6 or WP5-v3 §3–§4 sites used here; WP0-v3 already carries tr[𝔇ᵀS], G1). Catalog rows: literature/CATALOG-A.md §3–§7, §10.
Checks: `code/WP7-B2/checks.py` (sympy + mpmath + a 40-site numpy chain; **31 checks, all PASS, ≈ 5 s**), cited WP7B2-Cn. Tags per CONVENTIONS §12:
[D], [D, sketch], [E], [C]; literature [FT] (read in full text in literature/papers-WP7-B2/, PDFs deleted after use), [ABS], [UNVERIFIED]. All 19 arXiv IDs used
were verified against the arXiv API (export.arxiv.org id_list: titles and first authors match CATALOG-A). Status: all content CLAIMED (one return), pending R×2.

---
## 0. Results at a glance
| # | Item (catalog) | Result | Tag |
|---|---|---|---|
| 1 | A4 single-phonon absorption | (B2.1.1)–(B2.1.3): WP0 (3.5)–(3.6) with the GS one-phonon S of WP2-v3 (2.2) at k → 0 reproduces 2308.06314 Eqs. (2), (7), (16), Table 1 term by term (C1). **Coupling-to-mass rule** (2308.06314 Eq. (44)) is exact for any basis: only δv_κ = v_κ − M_κv̄ couples (C2). The electron-scalar vertex is q·(Z_κ𝟙 − Z*_κ), not the rigid-ion N_{j,e}: GaAs rate ×0.47 (C3) | D |
| 2 | S5, A7, L10 (absorption) | **Random-coupling broadband theorem** (B2.2.1): for site couplings with independent zero-mean (mass-subtracted) parts, ⟨S^{(1)}(k→0,ω)⟩ = (2π/V)Σ_I⟨\|δv_I\|²⟩D_I(ω)(n+1)/(2M_Iω). Gives 2411.10542 Eq. (31) exactly (C5); a-SiO₂/dark photon via ε(ω) of the glass; a **new** isotope-disorder channel for B−L in monatomic crystals (Si: σ_γ²/γ̄² = 1.8×10⁻⁴, C4) | D |
| 3 | L10 scattering (S_NN) | Exact Gaussian S for a disordered harmonic solid (B2.2.4) and its configurational average (self + distinct); closes WP2-v3 gap 6 at formula level; boson-peak entry points | D / D, sketch |
| 4 | §10(iii) | 2512.16451 Eq. (12) = n_ph = 0 term of (B2.2.4), configurationally averaged, Born [D]. **Born fails at its claimed reach**: optical potential V_opt/E_kin = 1.9 at σ_χN = 4×10⁻³⁸ cm², m_χ = 20 eV; validity needs σ_χN ≪ 1.2×10⁻³⁸ cm² (C12) | D / E |
| 5 | L11 solid He | 2409.02439 Eqs. (4)–(5) = WP2 (2.2) quasi-harmonic; URF replacement: self-consistent harmonic S (all n_ph, Bloch exact in the Gaussian) + cumulant and one–two-phonon interference corrections; f-sum exact | D / D, sketch |
| 6 | S2 magnon absorption | (B2.5.1) reproduces 2005.10256 Eq. (27) and 2001.10666 Eqs. (25)–(27), (35) (C6). **Larmor theorem** (B2.5.2): isotropic exchange + uniform g ⇒ all k → 0 transverse weight in one line at ω_L, weight ∝ net spin, to all orders in 1/S (C7). Kittel/Polder ellipticity factor (B2.5.3) ≥ 1 (C8) | D |
| 7 | S6 neutron-data S | (B2.6.1): neutrons give P_T^{αβ}S_{s^αs^β} up to [λ_S F/((g/2)F_M)]²; 2504.02927 Eqs. (8), (17), (26) reproduced (C9). The q̂q̂ part needed for absorption/pseudoscalar couplings is **not measured**; absorption needs permeability data | D |
| 8 | L9, S8 chiral phonons, SMMs | Born-charge phonon magnetization is **quadratic** in phonon operators ⇒ no one-phonon production through it (C20); the Zhang–Niu phonon angular momentum is **not conserved** by a crystal harmonic H (C10), so 2301.07617's κ = ⟨‖S‖⟩ is an estimate. SMM spin line D_ZFS(2S−1) + ω_Z, weight 2S (C16). 2601.01043 Eq. (12) lacks a square (C13a); its absorption rate needs ×n_r/\|ε\|² (C13c) | D |
| 9 | X10, §10(iv) | **Exact crystal identity** (B2.8.2): for c_κ ∝ M_κ, ⟨f\|O\|i⟩ = −c̃ m_e⟨f\|n_e(k)\|i⟩[1 + O(kr)] from WP0 (4.8) ⇒ Γ = y²c̃²m_e²k² Im[−1/ε]/(e²ω); reduces to 2312.10566 Eq. (17) (C11); acceleration form exact for any c_κ (C11a) | D |
| 10 | D2 colour centres | (B2.9.1) seeding formula; 1705.03016 Eq. (1) is its sharp-threshold, free-nucleus limit; corrections: seed Doppler width, survival, charge state, aggregate formation (single vacancies at sub-GeV, not F₂⁰/F₃⁺) | D / E |
| 11 | D5 bond breaking | (B2.10.1) CM ⊗ internal factorisation; 1608.02940 Eqs. (23), (25) are its gas limit; solid corrections: lattice-bound CM, cage escape | D / E |
| 12 | Source defects | 2308.06314 Eq. (48) and 2601.01043 Eq. (12) printed linear in the coupling (their Eqs. (49), (13) use the square; C13); 2512.16451 outside Born at its reach; 2308.06314 electron-scalar vertex rigid-ion | D + FT |

---
## 1. A4: single-phonon absorption written out from WP0 (3.5) with WP2-v3 [D]

**Truncation chain.** WP0 (3.5)–(3.6) (absorption, ω = m_φ, k = k_φ ≈ m_φv); operator rows: nucleon density n_κ (scalar), electron density n_e (scalar), nuclear
current j_κ (vector, B−L), charge (dark photon), spin rows for ordered targets; sector GS of Theorem D (6.1) with (O′_e)_{GS,GS} = ρ̄_e (WP0 §6.2(ii), WP2-v3 (1.2));
n_B = 0 for the vertex, n_A = 0, K = 1ph-coh, n_ph = 1; photon-reducible part through 𝒟^γ in (3.6). τ: `nB=0|ng=0|nA=0|X=-|nT=0|K=1ph-coh|Mg=-|nD=1` + `ref=normal;scr=ion`.

**Formula [D].** Hypotheses: harmonic GS vibrations, k ≪ q_BZ, ω ≪ E_g. Linearising each row in u (WP2-v3 (1.2), (7.2)) gives ⟨kν|O(k)|0⟩ = √N 𝒱_ν(k) with

  𝒱_ν(k) = Σ_κ e^{ik·r_κ}e^{−W_κ} v_κ·e*_κν(k)/√(2M_κω_kν),   v_κ = { c_κk (nucleon scalar);  c_e k·(Z_κ𝟙 − Z*_κ) (electron scalar);  −iωc_κε̂ (vector current);  −iωeZ*_κ·ε̂ (photon) }.   (B2.1.1)

  Γ_abs = (y_φ²/2ω)S_OO(k,ω),   S^{(1)}_OO = (2π/Ω)Σ_ν(n_kν+1)|𝒱_ν|²δ(ω − ω_kν);   Γ_net = −(y_φ²/ω)Im[R̃_OO + R̃_{Oμ}𝒟^γ_{μν}R̃_{νO}].   (B2.1.2)

The vector row uses ⟨kν|P_I/M_I|0⟩ = −iω_kν⟨kν|u_I|0⟩ (exact for local H, [H, R_I] = −iP_I/M_I). Spin-ordered targets add v_κ ∝ ω²𝐒_κ (2308.06314 Table 1 [FT]).
The electron-scalar vertex is the GS adiabatic density: δρ_κ → q·(Z_κ𝟙 − Z*_κ) at q → 0 (WP2-v3 (1.2), (4.4)), i.e. electrons follow each ion with Z_κ − Z*_κ.

**Coupling-to-mass rule [D] (C2).** Acoustic modes cannot absorb (ω = c_νk ≪ m_φ for c_ν ≪ v). Every optical mode at k → 0 is orthogonal to the mass-weighted
translation √M_κ ê (WP0 (4.8)(i)), so with v̄ ≡ Σ_κv_κ/Σ_κM_κ

  𝒱_ν(k→0) = Σ_κ (δv_κ·e*_κν)/√(2M_κω_ν),   δv_κ ≡ v_κ − M_κv̄;   diatomic: 𝒱 ∝ (v₁/M₁ − v₂/M₂)√(M₁M₂/M_cell).   (B2.1.3)

This is 2308.06314 Eq. (44) and their subtraction F_j → F_j − m̂_jΣF·m̂ [FT, CONFIRMED], derived here for any basis and any row. U(1)_B (c ∝ A ≈ M/m_u) is
absorbed only through mass defects and isotopes (§2).

**Literature limit [FT].** 2308.06314 Eq. (16): Π_ΦΦ′ = Ω⁻¹Σ_ν(ΣF·T)2ω_ν/(ω² − ω_ν² + iωγ_ν)(ΣF·T)*, T = ε*/√(2mω_ν) (Eq. (14)); Eq. (2) Γ = −Im Π/m_φ; Eq. (7)
(rate with the photon-mixing term). With y_φO ↔ g, (B2.1.2) = Eq. (2)+(16) (C1b; −Im of the propagator → πδ as γ_ν → 0, C1a); the reducible part is Eq. (7)'s
Π_φAΠ_Aφ/(m² − Π_AA). Photon-like couplings: (B2.1.2) with WP0 (5.4) gives R = (g²/e²)(k²/ω²)(ρ_φ/ρ_T)Im(−1/ε), = Eq. (42). Dark photon: 1712.06598 Eqs. (2)–(3)
R = ρ⁻¹(ρ_DM/m)κ²_effσ₁ = (ρ_DM/ρ)κ_mix²Im(−1/ε), i.e. ρ_DMΓ/(ρm) with the WP0 L9b Γ = κ_mix²m Im(−1/ε), ε from WP2-v3 (4.2).
**Leading corrections.** (i) Electron scalar: 2308.06314 uses N_{j,e} = 28, 36 for GaAs (Ga³⁺, As³⁻, text after Eq. (44)); the URF vertex Z_κ − Z*_κ = 28.9, 35.1
(Z* = ±2.1, 1712.06598 [FT]) changes δv by 0.68 and the **rate by ×0.47** (C3) [D for the vertex, E for the static Z*]. (ii) Finite linewidths γ_ν(T) (phono3py)
control off-resonant tails; the self-energy form must be the retarded Π^{ph}(ω), not a constant-γ Breit–Wigner, beyond ~5γ_ν (2603.22390 App. A says the same of its
Eq. (3) [FT]). (iii) Isotope/mass disorder opens a broadband background under the lines (§2). (iv) Two-phonon absorption at k → 0 (Q, −Q pairs): O(k⁴) for density
rows, O(k⁰) for charge via ∂Z*/∂u (WP2-v3 (4.5)); these are the "multiphonon sidebands" in measured ε (1712.06598 [FT]).
**Source defect [FT].** 2308.06314 Eq. (48) prints R ≈ ¼(g_aee/e)(ω/m_e)(ρ_φ/ρ_T)Im(−1/ε), linear in g_aee (confirmed in the PDF); its Eq. (49) g_aee ~ 10⁻⁹(100 meV/ω)
(κ/10⁻¹⁶) follows only from the squared form ¼(g_aee/e)²(ω/m_e)² (C13b). Misprint, numerics unaffected.

**Computation specification.** Inputs: DFPT phonons, Z*_κ, ε_∞ (QE ph.x / Abinit / VASP+phonopy; 8³ k, Γ-point plus 4³ q for linewidths); couplings c_κ per model.
Code: PhonoDark-abs (2308.06314) with the vertex (B2.1.1) (electron scalar: replace N_{j,e} by Z_κ − Z*_κ, ≈ 20 lines); γ_ν(ω,T) from phono3py (fc3 on 3×3×3 supercells).
Convergence: ω_ν to 0.1 meV, Z* to 1%, γ_ν to 10%. Cost: DFPT ≈ 10² CPU·h; fc3 ≈ 10³–10⁴ CPU·h. Output: R(m_φ) per model, τ string above, nuisance type M on γ_ν.

---
## 2. Random couplings and disorder: S5, A7, L10 [D]

**2.1 Theorem (random-coupling broadband absorption).** Hypotheses: (R1) harmonic vibrations of a fixed configuration {x⁰_I} (crystal with coupling disorder, or a
glass), modes λ with e_Iλ normalised over all sites; (R2) the k → 0 vertex is linear in u_I or P_I: ⟨λ|O|0⟩ = Σ_I v_I·e*_Iλ/√(2M_Iω_λ); (R3) after the mass
subtraction v_I = M_Iv̄ + δv_I (the M_Iv̄ part drops out exactly for every λ ≠ translation, (B2.1.3); C4b for a random-mass chain), the δv_I are zero-mean,
independent between sites, isotropic and independent of the eigenvectors. Then (C14)

  ⟨S^{(1)}_OO(k→0,ω)⟩_conf = (2π/V) Σ_I ⟨|δv_I|²⟩ D_I(ω)(n_B(ω)+1)/(2M_Iω),   D_I(ω) ≡ (1/3)Σ_λ|e_Iλ|²δ(ω − ω_λ),   ∫D_I = 1.   (B2.2.1)

No momentum conservation survives: every mode at ω absorbs (broadband), weighted by the site-projected DOS. (R3) is exact for unpolarised nuclear spins (S1–S3 of
WP2-v3 (7.1)); for structural disorder it is the incoherent approximation and is corrected below.

**2.2 S5 (axion–nuclear-spin coupling, absorption form).** Chain: WP0 (3.5) with the trace of the nuclear spin-current row, O = Σ_κ tr J_κ (WP0 (2.2), F^Σ_κh^I_κ ≡ λ_κ),
y_φ = 2g_pm_a (from −(g/m_N)ȧσ·D, 2411.10542 Eq. (3) [FT]); GS, n_A = 0, K = 1ph-inc. Vertex v_I = −iωλ_I𝐉_I; unpolarised ⟨J^αJ^β⟩ = δ^{αβ}𝒥(𝒥+1)/3 (C19). (B2.2.1):

  S_OO(ω) = (2π/Ω) Σ_κ x_κλ_κ²𝒥_κ(𝒥_κ+1) ωD_κ(ω)/(2M_κ),   ℛ = ρ_aΓ_abs/(ρ_Tm_a) = 2πρ_am_ag_p² Σ_κ ξ_κD_κ(m_a)/M_cell,   ξ_κ ≡ x_κλ_κ²𝒥_κ(𝒥_κ+1)/M_κ.   (B2.2.2)

**Literature limit [FT].** 2411.10542 Eqs. (25)–(31): Γ = 4πm_a²ωa₀²g_p²NΣ_jξ_jD_j(ω), Eq. (31) R = 2π(ρ_am_a/Σ_jm_j)g_p²Σ_jξ_jD_j(ω), D_j = (3N)⁻¹Σ|ε|²δ (Eq. (29)).
(B2.2.2) is Eq. (31) exactly (C5). Their matrix-element step k·J = im ω J·x (Eqs. (6)–(11)) is the commutator used for the vector row in §1. Coherent part: Eq. (21)/(24)
∝ P_κ², = the polarised term of WP2-v3 (7.1). **Leading corrections:** (i) isotope mass disorder: the spin isotope's local DOS differs by O(ΔM/M) (²⁹Si 3.5%; WP2-v3
(7.1) caveat) [E]; (ii) the GS matrix element of P_I uses the nuclear mass, the phonon the atomic mass: relative O(δM_κ/M_κ) ≈ 3×10⁻⁴ (WP0 §6.2(ii)) [E];
(iii) quadrupole/Zeeman splitting of the final spin states (≲ μeV ≪ ω) lifts the spin-closure step only at O(μeV/ω) [E]; (iv) polarisation P_κ adds the coherent line.

**2.3 A7 (amorphous absorption) and the dark photon.** Chain: WP0 (3.5)–(3.6) at k → 0, charge row, GS of the glass configuration, n_A = 0 (plus γ_λ), 𝒳 irrelevant
(ε_∞ clamped). Exact at this level [D] (WP2-v3 (4.2) with the glass Hessian, macroscopic rank-1 ε):

  ε(ω) = ε_∞ + (e²/V)Σ_λ |p_λ|²/(ω_λ² − ω² − iωγ_λ),   p_λ ≡ Σ_I ε̂·Z*_I·e_Iλ/√M_I,   Γ_abs = κ_mix²m_φ Im[−1/ε(m_φ)].   (B2.3.1)

Writing ε₂ ∝ C^{IR}(ω)D(ω)/ω with C^{IR}(ω) ≡ ⟨|p_λ|²⟩_{ω_λ=ω} (IR-to-VDOS coupling function) shows the broadband: every glass mode with p_λ ≠ 0 absorbs. (B2.2.1)
is the incoherent estimate C^{IR} ≈ Σ⟨|Z*_I|²⟩/(3M_I); **local charge neutrality** (Σ Z*_I over a structural unit ≈ 0, acoustic sum rule Σ_IZ*_I = 0) correlates the δv_I,
so (R3) fails at low ω: modes that translate a neutral unit rigidly over a size ξ_u have p_λ ∝ ωξ_u/c_ν, giving C^{IR} ∝ ω² below the boson peak [D, sketch].
**Literature limit [FT].** 2603.22390 Eq. (2): R = (ρ_A′/ρ_T)κ²Im[−1/ε(ω)] = WP0 L9b; its broadband claim is (B2.3.1) with measured or DFT ε. Its crystalline Eq. (3)
(factorised LO/TO form with Q = 100) is a rank-1, constant-width truncation, flagged by the authors themselves far from resonance [FT]. Leading correction: compute ε
from (B2.3.1) with γ_λ(T) at mK rather than room-temperature IR data (T-transfer as WP3-v3 §4(b)).

**2.4 Isotope-disorder channel (new) [D; E for size].** For a vector coupling to B−L (c_I = g(A_I − Z_I)) in a monatomic crystal (Si, Ge), both basis sites carry the same c/M,
so by (B2.1.3) the k → 0 single-phonon rate of §1 vanishes identically. Isotopes give δv_I = −iωg M_I(γ_I − γ̄), γ_I = (A_I − Z)/M_I, and (B2.2.1) yields a broadband rate
∝ M̄σ_γ²D(ω)ω over the whole phonon band. Natural Si: σ_γ²/γ̄² = 1.8×10⁻⁴ (C4a). Equivalent statement: absorption on the isotope-disorder ("impurity") modes. The
mass disorder also deforms e_Iλ, but the M_Iγ̄ part still drops out exactly (orthogonality, C4b). U(1)_B: δv from binding-energy differences only, (ΔB/A)/m_u ~ 10⁻⁴ [E].

**2.5 L10: configurational averaging of S_NN (closes WP2-v3 gap 6 at formula level).** Bloch's identity holds for any Gaussian (harmonic) state, so WP2-v3 (2.1)
holds with (Rκ) → I for a disordered harmonic solid [D]:

  S(q,ω) = (1/V)∫dt e^{iωt}Σ_{IJ} c_I*c_J e^{−iq·(x⁰_I−x⁰_J)}e^{−W_I−W_J}exp Φ_IJ(t),   Φ_IJ(t) = Σ_λ[(n_λ+1)(q·e_Iλ)(q·e_Jλ)*e^{−iω_λt} + n_λ(c.c.)e^{iω_λt}]/(2ω_λ√(M_IM_J)).   (B2.2.4)

Configurational average: S = S_self + S_dist. S_self is WP2-v3 (3.2) with site-resolved w_I(q;ω′) built from D_I^{q̂} (all n_ph; (3.5) per site class; f-sum (3.4′)
per site, exact). S_dist at n_ph = 1 contains the broadened Brillouin (sound) peak at q ≲ 1/d_nn, propagating up to the Ioffe–Regel frequency (≈ ω_BP); at n_ph ≥ 2 it is
⟨e^{−iq·r_IJ}Φ_IJ^{n}⟩, which decorrelates for q ≫ 1/d_nn, with leading correction weighted by the pair distribution, ∝ ∫d³r[g₂(r) − 1]j₀(qr)⟨Φ^{n}⟩_r [D, sketch]. No
j_BZ basis terms arise (WP2-v3 (2.4) is replaced by g₂). **Boson peak** (excess D(ω)/ω² at ω_BP ≈ 4 meV in a-SiO₂ [E]) enters three places: the one-phonon S_self ∝
q²D(ω)/ω, the DW exponent 2W_I = q·B_I·q (B_I ∝ ∫D_I coth(βω/2)/ω), and (B2.2.1)/(B2.3.1) through D(ω)C^{IR}(ω).

**Computation specification (§2).** Inputs: glass models by melt-quench MD with an MLIP (a-SiO₂, a-Si, SiN_x; 648–5184 atoms, ≥ 5 independent quenches), Hessian
by finite differences, Z*_I by DFPT on 192–648-atom subcells or an MLIP charge model; spin isotopes x_κ, λ_κ (2411.10542 Table 1 [FT]). Codes: LAMMPS + phonopy
(Γ-only, supercell), new module (≈ 250 lines) for D_I, C^{IR}, (B2.2.1), (B2.3.1), (B2.2.4) at n_ph ≤ 2, WP2 (3.5) solver for the self term. Convergence: D(ω) and C^{IR}
to 5% between sizes; finite-size gap 2πc_ν/L must lie below the threshold (L = 5 nm ⇒ ≈ 3 meV); configurational spread → type-M nuisance. Cost ≈ 10⁴ CPU·h (MLIP)
+ 10³ (DFPT Z*). Outputs: ε(ω), D_I(ω), C^{IR}(ω), S(q,ω) tables, τ `K=1ph-inc;ref=glass` (metadata value `glass` proposed, IF-B2-2).

---
## 3. §10(iii): quadratic couplings scattering off density fluctuations in random media [D; E for numbers]

**Chain.** WP0 (3.3), single nucleon-density row (a contact χχN̄N vertex, (m_N/Λ²)χ²N̄N, acts as 𝒪₁^{(N)} for χ → χ at tree level), Born; S_NN GS sector; n_ph = 0
(elastic) term of (B2.2.4); continuum limit q ≪ 1/d_nn; configurational average.
**Formula [D].** The n_ph = 0 term of (B2.2.4) is 2πδ(ω)V⁻¹|Σ_Ic_Ie^{−W_I}e^{iq·x⁰_I}|²; with q ≪ 1/d_nn, Σ_I → ∫d³r n(r), and n = n₀ + δn:

  ⟨S_el(q,ω)⟩ = 2πδ(ω)V⁻¹[n₀²|∫_V d³r e^{iq·r}|² + ∫∫d³r₁d³r₂ e^{iq·(r₂−r₁)}⟨δn(r₁)δn(r₂)⟩],   e^{−2W} → 1.   (B2.3.2)

This is 2512.16451 Eqs. (2), (7)–(10) [FT]; with the Debye random medium Eq. (11) it gives Eq. (12), |F_fluc|² = (δn²/n₀²)6ξ³/(R³(1 + q²ξ²)²) (standard algebra,
not re-checked symbolically). The acceleration observable is the q-weighted rate of WP0 (3.3).
**Validity [D] and the Born problem.** The homogeneous part acts as an optical potential V_opt = 2π𝔟_χN n₀/μ_χN (𝔟_χN the χN scattering length, σ_χN = 4π𝔟²).
Born on the medium requires V_opt ≪ E_kin = m_χv²/2, i.e. σ_χN ≪ σ_crit = m_χ⁴v⁴/(4πn₀²). Ti–6Al–4V (n₀ = 2.69×10²⁴ cm⁻³, 2512.16451 Eq. (14)), m_χ = 20 eV, v = 10⁻³:
σ_crit = 1.2×10⁻³⁸ cm², while the paper's MICROSCOPE reach is σ_χN ≈ 4×10⁻³⁸ cm², where V_opt/E_kin = 1.9 (C12) [E for inputs]. There, for a repulsive coupling
DM with v ≲ 1.4×10⁻³ is totally reflected; for attraction it is strongly refracted. Even for V_opt ≪ E_kin the phase kR V_opt/2E_kin across a cm body is ≫ 1, so the
fluctuation term must be computed in distorted waves (DWBA) with the in-medium k′ = k(1 − V_opt/E_kin)^{1/2} [D, sketch]. The paper does not discuss this (searched
the full text for refraction/reflection/optical potential). Consequence: the claimed MICROSCOPE limit lies outside the validity of its Eq. (12); near and above σ_crit
the force is reflection-dominated and scales with the composition difference of 𝔟̄n₀, not with δn² [D for the scaling, C for any limit].
Other corrections: inelastic weight 2W(q) ~ q²⟨u²⟩ ~ 10⁻¹⁷ at q ~ 0.1 eV (negligible); Bose enhancement of final states cancels in the net momentum transfer,
f(k)(1 + f(k′)) − f(k′)(1 + f(k)) = f(k) − f(k′) [D]. **Spec:** correlation function ⟨δnδn⟩ from tomography or SAXS/USAXS (q = 10⁻²–1 eV); DWBA code for a slab/
cylinder with V_opt (1D transfer matrices along the wind, ≈ 200 lines); minutes of CPU. Output: a(σ_χN, m_χ) with the Born/DWBA/reflection regimes marked.

---
## 4. L11: solid helium (quantum crystal) [D; D, sketch where marked]

**Chain.** WP0 (3.3), nucleon density row (c_κ = A_κF^M_κ), GS (He is a wide-gap insulator, E_g ≈ 20 eV), K = 1ph-coh / multi-inc. The WP0 τ entry n_A = 0 assumes
η_anh ≪ 1 (Table 6.1). In solid ⁴He the Lindemann ratio δ_Lind = ⟨u²⟩^{1/2}/d_nn ≈ 0.26–0.3 at melting densities (V_m ≈ 21 cm³/mol) [E]; the static-lattice Hessian is
then not a valid expansion point (the harmonic approximation fails, including unstable modes at low density) [E]. Under 1–40 GPa (V_m ≈ 9 → 4 cm³/mol) δ_Lind drops to
≈ 0.1 [E], and quasi-harmonic DFT matches the measured dispersions (2409.02439 Fig. 2 [FT]).
**Formula [D within a Gaussian density matrix].** Replace the static-lattice Hessian by the self-consistent harmonic (SCHA) Gaussian ρ_G: Φ^{(2)}_eff = ⟨∇∇V_pot⟩_{ρ_G},
B_κ = ⟨uu⟩_{ρ_G} solved self-consistently (variational, Gibbs–Bogoliubov). Inside ρ_G Bloch's identity is exact, so WP2-v3 (2.1)–(2.2), (3.2), (3.5) hold at all n_ph with
(ω_Qν, e_κν) → eigenpairs of Φ^{(2)}_eff and 2W_κ = q·B_κ·q from the same ρ_G:

  S^{SCHA}(q,ω) = WP2-v3 (2.1)[Φ^{(2)} → Φ^{(2)}_eff, B_κ → B^{SCHA}_κ],   ∫ωS^{SCHA} = π𝓃_κq²|c_κ|²/M_κ (WP0 (4.6b), exact for any Gaussian).   (B2.4.1)

Beyond ρ_G [D, sketch]: (a) non-Gaussian displacement cumulants 𝒞₃, 𝒞₄ in the DW and multiphonon kernel (WP2-v3 §6); (b) the one–two-phonon interference term of the
anharmonic one-phonon cross-section, ∝ q³Φ^{(3)}, odd in the cubic vertex (known for quantum crystals [UNVERIFIED: Ambegaokar–Conway–Baym 1965]); (c) the three exact
linear constraints of WP2-v3 (6.1) (L18) bound the anharmonic increment (type T nuisance, WP6-v3 (5.1″)). Exchange tunnelling (μK) and ³He are negligible [E].
**Literature limit [FT].** 2409.02439 Eq. (4): S = (π/Ω)Σ_ν ω_νk⁻¹|Σ_jA_jF_{N_j}m_j^{−1/2}e^{−W_j}e^{iG·x⁰_j}(q·ε*)|²δ(ω_q − ω_νk), Eq. (5) W_j from the same harmonic
modes, Eq. (2) Γ = (πσ̄_n/μ²)∫d³q/(2π)³F²S. This is WP2-v3 (2.2) at n_ph = 1, T = 0, with c_κ = A_κF_N and the x⁰-phase convention (WP2-v3 (1.3) maps it), i.e.
(B2.4.1) with Φ_eff → quasi-harmonic DFT Hessian. **Leading correction:** ω²_eff − ω²_QH ∝ ⟨Φ^{(4)}⟩B + O(Φ^{(3)2}) (SCHA renormalisation), a few % in ω at ≥ 1 GPa and
O(1) near melting [E]; 2W from PIMD B_κ instead of harmonic B_κ (the zero-point B is ≈ 20–30% above harmonic at δ_Lind ≈ 0.1 [E]); daily modulation of hcp-α He
inherits Φ_eff anisotropy. **Spec:** MLIP trained on PBE+D3M (the source's XC) at 1–40 GPa; SSCHA (or TDEP on PIMD trajectories, i-PI, P = 64 beads at T ≈ 2 K) on
128–432-atom cells; Φ_eff → phonopy → DarkMAGIC (the source's code) or PhonoDark; (B2.4.1) multiphonon via WP2 (3.5). Convergence: ω_eff to 2%, B_κ to 3%,
supercell and bead extrapolation. Cost ≈ 10⁴ CPU·h per pressure. Output S(q,ω;P) with δ_Lind flags; τ `nA=SCHA` (a resummation, not a finite order: IF-B2-3).

---
## 5. S2: boson absorption into magnons (Kittel and in-field modes) [D]

**Chain.** WP0 (3.5) with the axion-wind spin row (LO −(g_aee/2m_e)(∇φ)·σ → s_e(k), WP0 §2), 𝔇 = (g_aee/m_e)²k^αk^β; clamped nuclei; WP4-v3 [1.1] projection onto
the magnetic multiplets, s_e → Σe^{ik·x}F^{mag}_jλ_{S,j}𝐒_j; ref = LSWT (WP4-v3 [2.1]–[2.2]) or exact where stated; k = m_av ≈ 0. Within a J multiplet ⟨s⟩ = (g_j − 1)⟨𝐉⟩
(Landé projection), so λ_{S,j} = g_j − 1, matching the (g_j − 1) of 2005.10256 Table 1 [FT]. F^{mag}_j(k → 0) = 1 exactly.

  Γ_abs = (g_aee²/2ωm_e²) k^αk^β S_{s^αs^β}(k,ω),   S_{αβ}(k→0,ω) = (2π/Ω)Σ_ν[(n_ν+1)ℰ^{α*}_νℰ^β_ν δ(ω − ω_{0ν}) + absorption term]   (WP4-v3 (2.1)–(2.2)).   (B2.5.1)

**Larmor theorem [D] (C7).** Hypotheses: H_spin = isotropic exchange (any J^{ex}_ij, any lattice, any order) − ω_LΣ_jS^z_j with one g (λ_{S,j} = λ_S), no anisotropy,
no dipolar/demagnetising field, k → 0. Then [H, S^∓_tot] = ±ω_LS^∓_tot exactly, so S^-_tot creates only states at ω_L, with total weight ⟨[S^+_tot, S^-_tot]⟩ = 2⟨S^z_tot⟩:

  S_{k·s}(k→0,ω>0) = (2π/Ω) λ_S² (k_⊥²/2) m_s δ(ω − ω_L)/(1 − e^{−βω_L}),   Γ_abs = πg_aee²λ_S²m_s k_⊥²/(2m_e²ωΩ) · δ(ω − ω_L)/(1 − e^{−βω_L}),   (B2.5.2)

m_s = ⟨S^z_tot⟩/N the net spin per magnetic cell (ferrimagnet: the net moment; YIG m_s = 10 per 20-Fe cell [E]), k_⊥ = k transverse to the magnetisation. Exact to all
orders in 1/(2|𝐒|) and for any T below the ordering temperature; it reduces to LSWT for a single sublattice. Antiferromagnets (m_s = 0) have zero uniform weight under
these hypotheses; the AFM (NiO) and anisotropy-gapped modes need H beyond them (2411.11971 Eq. (4) [FT]; WP4-v3 [2.1] with U^B, V^B). With non-uniform λ_{S,j}
(different g_j), gapped modes acquire weight ∝ (λ_{S,j} − λ_{S,j′})²: 2005.10256 Eq. (28) [FT], here exact as [H_exch, Σ_jλ_{S,j}𝐒_j] ∝ Σ(λ_j − λ_j′)𝐒_j × 𝐒_j′.
**Kittel/Polder (in-field uniform mode of an ellipsoid) [D] (C8).** With demagnetising factors N_x, N_y, N_z (HL, μ₀ = 1), ω_{K,x} = gμ_B(B₀ + (N_x − N_z)M_s),
ω_{K,y} = gμ_B(B₀ + (N_y − N_z)M_s): ω_K = (ω_{K,x}ω_{K,y})^{1/2}, the mode is elliptic, and in (B2.5.2) k_x² → k_x²(ω_{K,y}/ω_{K,x})^{1/2}, k_y² → k_y²(ω_{K,x}/ω_{K,y})^{1/2},
m_s δ(ω − ω_L) → m_s δ(ω − ω_K). Averaged over transverse directions the factor is (ω_{K,x} + ω_{K,y})/(2ω_K) ≥ 1.   (B2.5.3)
**Literature limit [FT].** 2005.10256 Eq. (27): R = (2ω/m_cell)∫d³v f Σ_ν ω_νγ_ν/((ω² − ω_ν²)² + (ωγ_ν)²)|Σ_j√S_j f_j·(U*r_j + V r*_j)|², f_j = −(i/√2)g_aee(g_j − 1)
(√ρ_a/m_e)v_a (Table 1). One sublattice, γ → 0: (B2.5.1) = Eq. (27) (C6a). 2001.10666 Eqs. (25)–(27): V = (sN/2)^{1/2}m_aa₀v_a⁺/f, Eq. (35) P(t) = |V|²t²/4 on
resonance; this coherent growth is the t ≪ 1/γ, t ≪ τ_a regime; for t ≫ 1/γ its golden-rule rate (π/2)|V|²δ equals (B2.5.2) with g_aee/m_e = 1/f, λ_S = 1 (C6b).
Its effective one-spin-per-cell Hamiltonian, Eq. (13), is exactly the Larmor case. **Leading corrections:** demagnetisation ellipticity (B2.5.3); magnon damping
(Lorentzian, measured FMR linewidth); exchange dispersion ω(k) = ω_L + 𝒟_ex k² (relative 𝒟_exk²/ω_L ~ 10⁻⁸ [E]); orbital moments (λ_S = g − 1 ≠ 1); T factor.
**Spec:** inputs J^{ex}, anisotropy, g tensors (DFT+U four-state or INS fits; ESR/FMR), sample shape; codes: SpinW-type Colpa diagonalisation (2005.10256 App. C
algorithm) at k = 0 with the dipolar/demag term; output ℛ(m_a, B₀) with linewidths. Cost negligible (≪ 1 CPU·h). τ: `ref=LSWT` or `ref=exact(Larmor)`.

---
## 6. S6: spin responses from measured neutron-scattering data [D]

**Chain.** WP0 (3.3)/(3.5) with the electron spin row only (𝔇 on s_e^α); target response taken from data instead of a computed τ point (a data-driven entry like
measured ELF, CONVENTIONS §10 last line). Neutrons couple to the full magnetisation (spin + orbital) through the dipolar interaction, transverse to q.
**Formula [D].** For one magnetic species in the dipole approximation, with S_n the per-formula-unit structure factor of 2504.02927 Eq. (24) (N_f units per cell Ω_c):

  P_T^{αβ}(q̂)S_{s^αs^β}(q,ω;T_d) = [λ_SF^{mag}_S(q)/((g/2)F_M(q))]² · 4(2π)³m_e²N_f S_n(q,ω)/(γ_n²e⁴Ω_c),   F_M ≈ ⟨j₀⟩ + (1 − 2/g)⟨j₂⟩,   (B2.6.1)

  S(q,ω;T→0) = (1 − e^{−β_dω})S(q,ω;T_d)   (exact if the spectral function (1 − e^{−βω})S is T-independent, harmonic magnons; ω > 0).   (B2.6.2)

g = 2, quenched orbit: the bracket is 1. Ni²⁺-like g ≈ 2.2: [(1.2)/(1.1)]² ≈ 1.19 plus the ⟨j₂⟩ term [E].
**Literature limit [FT].** 2504.02927 Eq. (8) χ″_ij = (π/V)Σ⟨e|s^j_e(q)|e′⟩⟨e′|s^i_e(−q)|e⟩δ (s_e = σ density, T = 0), Eq. (11) Γ_s = ∫d³q/(2π)³𝓕^{ij}χ″_ij, Eq. (15)
Γ_a = 𝓕^{ij}χ″_ij/2m_χ, Eq. (17) Γ_a = g_ae²m_av^iv^jχ″_ij, Eq. (26) S_n = N_f⁻¹(γ_n²e⁴/8m_e²)(Ω_c/(2π)³)P_T^{ij}χ″_ij. Dictionary: χ″ = 2(1 − e^{−βω})S_{ss} (σ = 2s, Kubo sign,
WP0 (4.1); C9a); Eq. (17) = (B2.5.1) (C9b); Eq. (26) ⇔ (B2.6.1) at g = 2 (C9c). Index order and the q-sign of their s(−q) are immaterial for P- or T-even targets
(YIG is centrosymmetric); for P,T-broken magnets use CONVENTIONS §3.
**What the data do not fix [D].** (i) Neutrons give only P_T^{αβ}S_{αβ}. Couplings with 𝔇 ∝ P_T (magnetic dipole, anapole: 2504.02927 Table 1) are calibrated directly;
q̂q̂ couplings (pseudoscalar mediator, CP-violating scalar, dark EDM, and axion-wind absorption, where v^iv^j ∥ q̂q̂) need q̂^αq̂^βS_{αβ}, which unpolarised data do not
contain. Reconstruction uses the magnetic point group (S(gq) = gS(q)gᵀ) and polarisation analysis; the direction average gives only ⟨tr P_TS⟩ = (2/3)tr S.
(ii) Absorption needs k = m_av ≈ 10⁻³m_a, far below neutron Q (≥ 0.1 keV): use FMR/THz permeability, χ″ = μ_B⁻²Im(−μ⁻¹) (2504.02927 footnote to Eq. (17) [FT]),
corrected for the sample shape (B2.5.3). (iii) At high q the magnetic signal sits on phonon (nuclear) scattering; subtracting a modelled S_NN (WP2) must be followed by
projection onto the PSD cone (WP0 (4.4)); spin-polarised neutrons separate it directly.
**Uncertainty (WP6-v3 (5.1) types).** Absolute normalisation (vanadium/phonon calibration) type M, 10–20% [E]; angular/|q| extrapolation schemes (none/angular/magnitude,
2504.02927 Fig. 2) type Δ; unmeasured (q,ω) regions type A (support-opening, PSD only if the filled-in increment is PSD); energy resolution type E; T-transfer (B2.6.2)
residual (magnon renormalisation ∝ M_s(T_d)/M_s(0) − 1) type M. **Spec:** inputs: S_n(q,ω) on (Δq, Δω) = (0.1 keV, 1 meV) grids (Horace/Mantid), g, F_M, F^{mag}_S
(Wannier spin density); new module (≈ 200 lines): (B2.6.1)–(B2.6.2), PSD projection, nuisance export. Cost: minutes. Output: S^{data}_{ss}(q,ω) with band, τ `X=data`.

---
## 7. L9 and S8: chiral phonons and single-molecule magnets [D]

**Chain.** Production: WP0 (3.3)/(3.5) with the density/charge rows (2301.07617 uses the dark-photon 𝒪₁), the transverse nuclear current j_T (WP2-v3 (7.2)) and spin
rows via spin–phonon coupling; GS, n_A = 0, K = 1ph-coh, final states resolved by Λ = (Qν) (WP0 (7.1)). Readout: WP0 (7.3) P_casc with WP5 anharmonic down-conversion
into a long-lived chiral band and magnetometry of its moment.
**(a) Chirality label [D].** With CONVENTIONS §5 eigenvectors, the mode angular momentum is L^{ph}_{Qν} = −iΣ_κ e*_κν(Q) × e_κν(Q) (real, |L^{ph}| ≤ 1); TR + inversion
allow real e and give L^{ph} = 0. The chirality-resolved rate is Σ_ν∫ tr[𝔇ᵀS^{(1)}(q,ω;Qν)] δ(L − L^{ph}_{Qν}), S^{(1)}(·;Qν) the one-phonon term of WP2-v3 (2.2).
This is 2301.07617 Eq. (6) and 2511.20461 Eq. (11) [FT] in campaign normalisation.
**(b) Magnetisation is a two-phonon vertex [D].** The Born-charge phonon magnetisation (2301.07617 Eq. (7), 2511.20461 Eq. (12) [FT]) in operator form is
𝐌^{ph}(q) = Σ_I(eZ*_I/2M_I)(u_I × P_I)e^{iq·R_I}: bilinear in (b, b†) (C20). Hence ⟨Qν|𝐌^{ph}(q)|0⟩ = 0, and a DM coupling to the phonon magnetisation (magnetic-dipole DM,
𝒪₄-type through 𝐌) produces chiral phonons in pairs at T = 0:

  ⟨Q₁ν₁,Q₂ν₂|𝐌^{ph}(q)|0⟩ = (e/2)Σ_κ(Z*_κ/M_κ)e^{iq·r_κ}δ_{Q₁+Q₂,q+G}·(i/2)[(ω₂/ω₁)^{1/2} − (ω₁/ω₂)^{1/2}](e*_{κν₁}(Q₁) × e*_{κν₂}(Q₂)),   (B2.7.1)

(isotropic Z*_κ; u from CONVENTIONS §5, P_I = M_Iu̇_I, created momenta summing to q; the overall phase is convention-dependent; the amplitude vanishes for ω₁ = ω₂), i.e. an n_ph = 2 term of WP2 (2.2) type. One-phonon production through a moment needs a
vertex linear in u: orbit–lattice coupling ∂_u(crystal field)·𝐋 of unquenched (4f) ions, the "giant moment" mechanisms 2301.07617 cites; then the spin/orbital rows
carry the one-phonon amplitude ∂⟨s_e⟩/∂u [D, sketch].
**(c) No angular-momentum selection rule in decay [D] (C10).** For H = ½p·p + ½u·D^dyn·u (mass-weighted), [H, L^{ph}_z] = 0 iff D^dyn commutes with the on-site
rotation generator J_z ⊗ 𝟙, true for isotropic central springs and false for a generic crystal Hessian. Only the C_n pseudo-angular momentum at C_n-invariant Q is
conserved (mod n). So "angular momentum conservation" does not force decay into chiral daughters; 2301.07617's κ = ⟨‖S‖⟩ ≈ 15% (stable-band average circular
polarisation) is an estimate [E], not a branching ratio. URF replacement: κ_URF = Σ_{Qν}w_{Qν}P_casc(band_stable, |L^{ph}| > L_th | Qν) with three-phonon rates
Γ_{λ→λ′λ″} (phono3py) and L^{ph} of each daughter.
**(d) SMMs (S8) [D] (C16).** Dilute, non-interacting molecules with H_SMM = −D_ZFSS_z² − ω_ZS_z (2601.01043 Eq. (3) [FT], plus Zeeman) and s_e = λ_S𝐒 (WP4-v3 [1.1]):

  S_{k·s}(k→0,ω) = 𝓃_mol2πλ_S²(k_⊥²/4)Σ_m p_m[S(S+1) − m(m−1)]δ(ω − D_ZFS(2m−1) − ω_Z) (+ k_z²S^zS^z elastic),   (B2.7.2)

with Γ_abs from (B2.5.1). At T → 0 one line at D_ZFS(2S−1) + ω_Z with weight 2S (Mn₁₂-like S = 10, D_ZFS ≈ 0.05 meV: ≈ 1 meV [E]). Dark-photon absorption is
WP0 L9b with the SMM crystal's ε (vibrational IR bands).
**Literature limits [FT].** 2301.07617/2511.20461 rates: PhonoDark single-phonon rates (2511.20461 Eqs. (3)–(4), (8)) × κ: = (a) with κ as an assumed P_casc. 2601.01043:
Eqs. (9)–(10) R = (ρ/m ρ_T)κ²α (α the photon absorption coefficient, "relative permittivity approximated as unity"); URF L9b gives R_URF/R_src = n_r/|ε|² (C13c; ≈ 0.25
for ε ≈ 2.5 [E]). Eq. (12) prints R ≃ (g_aγγB₀/m_a)(ρ_DM/ρ_T)Im[−1/κ(m_a)] (confirmed in the PDF); the correct form is WP0 (2.9), (g_aγγB₀/m_a)², which is what its
Eq. (13) g_aγγ ~ εm_a/B₀ assumes (C13a). Misprint. Its avalanche trigger Eq. (6) is a detector response (heat threshold), not a target response (IF-B2-6).
**Spec:** (a)–(c): DFPT phonons and Z* (Abinit/QE), L^{ph}_{Qν} on 10×10×20 grids, phono3py fc3 for Γ_{λ→λ′λ″} (MOF cells: ≈ 10⁵ CPU·h, the bottleneck), WP5 Monte-Carlo
down-conversion with L^{ph} labels; (b) n_ph = 2 module from (B2.7.1) (≈ 150 lines). SMM: D_ZFS, g from ESR/ab initio (CASSCF-SO, ≈ 10³ CPU·h/molecule), (B2.7.2)
analytic; IR ε from DFPT of the molecular crystal. Output: chirality-resolved rates and κ_URF, SMM line strengths.

---
## 8. X10 and §10(iv): Migdal-type absorption (scalar–nucleon couplings) [D]

**Chain.** WP0 (3.5) with O = Σ_κc_κn_κ(k) (scalar–nucleon, c_κ = g_pZ_κ + g_n(A_κ − Z_κ)); final sector X (electronic excitations, ω = m_φ ≫ ω_max), the X-sector of
S_κκ in Theorem D (6.1); WP0 (4.8) Ward identity; dipole order n_D = 1 in k (k = m_φv ≪ 1/r).
**Exact identities [D].** (i) Acceleration form (C11a): for H with kinetic P_I²/2M_I and potentials multiplicative in R_I, ⟨f|R_I|i⟩ = ⟨f|∇_{R_I}V_pot|i⟩/(M_Iω_fi²), so

  ⟨f|O(k)|i⟩ = ik·Σ_I (c_I/M_I)⟨f|∇_{R_I}V_pot|i⟩/ω_fi² + O(k²)   (any target, any BO order).   (B2.8.1)

(ii) Mass-proportional coupling c_κ = c̃M_κ (single species, or c ∝ M): O = c̃(ρ_M − m_en_e) with ρ_M the mass density of WP0 (4.8); [H, ρ_M(k)] = k·𝐠(k), 𝐠(0) = P_tot,
so ⟨f|ρ_M(k)|i⟩ = O(k²) for internal excitations, while ⟨f|n_e(k)|i⟩ = O(k):

  ⟨f|O(k)|i⟩ = −c̃ m_e ⟨f|n_e(k)|i⟩[1 + O(kr_c)]  ⇒  S^X_OO(k,ω) = c̃²m_e²S_ee(k,ω),   Γ_abs = (y_φ²c̃²m_e²k²/(e²ω)) Im[−1/ε(k→0,ω)].   (B2.8.2)

The last step uses S_ee = (2k²/e²)Im(−ε_e⁻¹) with ε_e = ε at ω ≫ ω_max (WP0 (5.5)(ii)). For an isolated atom (B2.8.1) reduces to the boost amplitude c(m_e/m_at)⟨f|Σ_iρ_i|i⟩
in relative coordinates (WP0 §6.2(ii); the m_at vs M_N bookkeeping cancels exactly between the lab dipole and the relative dipole). For c_κ not ∝ M_κ, (B2.8.1) gives per
species c̃_κ = c_κ/M_κ for core shells localised on κ (⟨f|∇_{R_I}V|i⟩ ≈ −m_eω²⟨f|Σ_{i∈I}r_i|i⟩): Γ ≈ Σ_κ(y_φ²c̃_κ²m_e²k²/e²ω)Im(−1/ε)|_{κ shells} [D for localised
cores, E for valence].
**Literature limit [FT].** 2312.10566 Eq. (13) M^{(N)} ≈ −i(g_φnA/√(2ω))(m_e/m_at)⟨f|k·R|i⟩, Eq. (14) σ_φ = πg²(m_e²/m_p²)(k/3)Σ|⟨f|R|i⟩|², Eq. (16) σ_γ = (4π²α/3)ωΣ|⟨R⟩|²,
Eq. (17) σ_φ = g²(m_e²/m_p²)(k/ω)σ_γ/4πα. In the dilute limit Im(−1/ε) → Im ε = 𝓃_atσ_γ/ω and c̃ = g/m_p, so (B2.8.2) per atom = σ_φv of Eq. (17) (C11b).
**Leading correction:** medium screening, Im(−1/ε)/(Im ε/n_r) = n_r/|ε|² = 1 − O(ω_p²/ω²): 3×10⁻⁴ at 1 keV in Si (C15), O(1) near the plasmon and edges, where
2312.10566's photoionisation relation must be replaced by the ELF (the source says solid-state effects "may significantly differ" [FT]). Next: O(kr_c) multipoles (their
Eq. (15)); for c_κ ∉ ∝ M_κ the valence part, which interferes with PAER-type amplitudes when c_ec_κ ≠ 0 (WP0 §6.2 dictionary). §10(iv) is this entry; its rate adds to,
and never double-counts, the electron-scalar 𝒯_e channel of WP3-v3 §4(d) (different coupling).
**Spec:** measured or computed ELF (WP1 RPA+LFE with cores; Henke/NIST data above 30 eV); per-shell c̃_κ weights; trivial cost. Output ℛ(m_φ) for g_p, g_n.

---
## 9. D2: colour-centre creation (thresholds, yields, interface to WP5-v3) [D for structure; E for numbers]

**Chain.** WP0 (7.3) with seeds Λ from (a) GS S_κκ (nuclear recoil, E_R, r̂_R; WP2 L6 K = imp at E_R ≫ ω_D) and (b) X-sector e–h/exciton seeds (ER); P_casc from WP5-v3
§3 (BO-surface MD partition), §4 (defects, annealing), L22 (E_d).

  dℛ_CC/dt = (ρ_χ/m_χρ_T)∫d³v f_χ∫d³q/(2π)³ Σ_Λ tr[𝔇ᵀS(q,ω_q;Λ)] Y_CC(Λ),   Y_CC(κ,E_R,r̂) = P_FP(E_R,r̂)p_surv p_q f_opt,   Y_CC(eh,E) = ⟨N_x⟩(E)p_FH p_surv f_opt.   (B2.9.1)

P_FP: displacement probability of an anion (smooth, WP5 L22 (a)); p_surv: survival against close-pair recombination; p_q: charge state (an F centre needs a trapped
electron; F⁺ otherwise); f_opt: fraction in the read-out species; ⟨N_x⟩: excitons per ER deposit (WP5 cascade); p_FH: self-trapped-exciton → F–H conversion.
**Literature limit [FT].** 1705.03016 Eq. (1) ∂R/∂φ_c = f_PN²N_T(ρ_χ/m_χ)(σ̄_n/16π²μ²)∫dq²∫d³v∫dφ″_q|F_DM|²Θ(q − q_min)f/v, Eq. (2) q_min = [2m₁ΔE_B(1 + a sin cos)]^{1/2},
Eq. (5) E_r^min = q_min²/2m₁. This is (B2.9.1)(a) with S^{GS}_κκ → free nucleus (K = imp, δ(ω − q²/2M)), Y_CC → Θ(E_R − E^min_R(r̂)), "electron occupation spontaneous and
immediate" (p_q = 1) and p_surv = f_opt = 1. **Leading corrections:** (i) seed Doppler width (IA): σ_E ≈ [(4/3)E_RE^kin_q̂]^{1/2}, ≥ 1 eV (WP5 L22 (a)), a 10% smearing of
the 9 eV LiH threshold [E]; their quantum criterion Eq. (6) uses Δp ~ αm_e = 3.7 keV, while the H zero-point momentum is (Mω/2)^{1/2} ≈ 6.9 keV (Δp/q_min = 0.05; C17):
the classical conclusion stands; (ii) p_surv < 1 near threshold (close Frenkel pairs; MD), (iii) p_q: at sub-keV E_R the recoil's own ionisation is a few e–h, so many
vacancies stay F⁺ [E]; (iv) aggregates: 2503.20732 [FT] reads out F₂⁰ (650 nm) and F₃⁺ (525 nm), formed in dense neutron-recoil tracks (≈ 1200 vacancies/μm, TRIM); a
sub-GeV DM recoil (E_R ~ 10–100 eV) makes one or a few vacancies, and at mK vacancies do not migrate (WP5 (W12) frozen), so f_opt for aggregate centres ≈ 0 and the readout
must target isolated F centres [E/C]. ER: 2503.20732 measures a ⁶⁰Co γ fluorescence response ≈ 1/50 of fast neutrons per dose [FT], the only ER/NR calibration point;
the ER threshold is the lowest exciton energy (LiF ≈ 13 eV [E]), with p_FH(T) of alkali halides [UNVERIFIED for values]. Interface: WP5-v3 §4 notes ER defect creation
needs electronic bond breaking and is "candidate-dependent for ionic targets"; (B2.9.1)(b) is that channel (IF-B2-7).
**Spec:** MLIP/DFT MD threshold surface E_d(r̂) for the anion sublattice of LiF/MgO/LiH (10⁴ PKA directions, 10 ps, T = 0 and zero-point-sampled initial states), p_surv
by MD + kMC, defect charge levels (HSE ΔSCF), STE → F–H by excited-state MD (surface hopping, ≈ 10⁵ CPU·h), F-band optical cross sections (BSE) for f_opt. Output:
Y_CC(E_R, r̂) and Y_CC(eh, E) tables with type-M nuisances.

---
## 10. D5: bond breaking in molecular solids [D for structure; E for numbers]

**Chain.** WP0 (3.3), nucleon row on atom 1 of a molecule, GS sector (or X for electronic dissociation), WP0 (7.3) with P_casc = cage escape.
**Formula [D].** Hypothesis (M): the intermolecular potential does not depend on the internal coordinate r (rigid-molecule crystal). With R₁ = R_CM + (m₂/M)r and
m₂/M = μ₁₂/m₁ (C18), e^{iq·R₁} factorises and

  S₁₁^{GS}(q,ω) = ∫(dω′/2π) S_CM(q,ω′) S_int((μ₁₂/m₁)q, ω − ω′),   S_int(p,ω) = 2πΣ_f|⟨f|e^{ip·r}|0⟩|²δ(ω − E_f + E_0);   S^{diss} = S_int restricted to E_f > ΔE_B.   (B2.10.1)

S_CM is the lattice S of the whole molecule (WP2-v3 (3.2)/(5.3), mass M_mol); the bond-breaking rate is (3.4) with S^{diss} and P_casc(break | f) = p_esc.
**Literature limit [FT].** 1608.02940 Eq. (4) q_min = (m₁/μ₁₂)(2μ₁₂ΔE_B)^{1/2}, Eq. (11) F(q,q̃) = ∫d³r e^{i(μ₁₂/m₁)q·r}Ψ*_q̃Ψ_i, Eq. (12) |F_dis|², Eq. (23) classical rate with
Θ(q − (2m₁²ΔE_B/μ₁₂)^{1/2}), Eq. (25) quantum rate with |F_dis|². These are (B2.10.1) with S_CM → free recoil of the molecule (gas) and p_esc = 1; Eq. (23) is the further
impulse limit of S_int (Eq. (17): support at q ≈ (m₁/μ₁₂)q̃). **Leading corrections:** (i) in the solid the CM is bound (ω_lat ~ 5–10 meV): at q ≈ q_min ~ 10² keV,
x_R(CM) ≫ 1, so the IA applies with a Doppler width from ⟨P_CM²⟩ (plus the internal zero-point spread of their Eqs. (8)–(9)); the recoil-free fraction e^{−2W_CM(q_min)} ≈ 0
[E]; (ii) cage effect: fragments recombine unless they escape the molecular cage, p_esc < 1 (MD) [E]; (iii) electronic channel: ER into repulsive σ* surfaces (X sector,
reflection-principle FC envelope) with yield p_diss(Λ), a lower-threshold channel in many molecular crystals [E]. **Spec:** S_int from the molecular potential (Morse or
ab initio, 1608.02940's improved Born), S_CM from phonopy/PIMD of the molecular crystal, p_esc by MLIP MD (10³ trajectories per (E_int, r̂)); ≈ 10³ CPU·h. Output:
dℛ/dE_int and break yields.

---
## 11. Exact remaining gaps
1. **A7/L10 beyond the incoherent estimate:** C^{IR}(ω) and the distinct (pair) terms of (B2.2.4) need the glass Hessians of §2.5; the low-ω law C^{IR} ∝ ω² is
   [D, sketch] (local neutrality), not proven. No glass-model computation is done here (theory only).
2. **§10(iii) above σ_crit:** the reflection/refraction-dominated force on heterogeneous test masses is not computed; only its scaling is stated [C for any bound].
3. **L11 near melting:** beyond-Gaussian effects (cumulants, interference term) have only a structure; no bound on the remainder at δ_Lind ≈ 0.3 is derived.
4. **S2 beyond the Larmor hypotheses:** anisotropic, dipolar and AFM targets need numerical LSWT + demag; no closed form beyond (B2.5.3).
5. **S6 longitudinal component:** no data-only route to q̂q̂S_{ss} from unpolarised neutrons; requires polarisation analysis or symmetry plus modelling.
6. **L9/S8:** κ_URF needs mode-resolved three-phonon decay in MOF cells (cost-limited); the microscopic origin of giant phonon moments is open (as the sources state).
7. **D2:** p_q, p_FH and single-F readout efficiency at mK are not known from first principles; the ER/NR ratio is calibrated only at MeV doses (2503.20732).
8. **D5:** p_esc in molecular crystals and the ER σ* channel yields are unquantified.
9. **X10 for c_κ ∉ ∝ M_κ in valence:** (B2.8.1) is exact, but its valence evaluation needs non-adiabatic ⟨f|∇_{R_I}V|i⟩ in the crystal (WP3 (W.5) machinery).

---
## 12. Literature (status in this return)
[FT] read in full text (literature/papers-WP7-B2/): 2308.06314 (Eqs. (2), (7), (14), (16), (37)–(44), (48)–(49), Table 1), 1712.06598 (Eqs. (2)–(3)), 2411.10542 (Eqs. (3)–(31)),
2603.22390 (Eqs. (2)–(3), App. A–B), 2512.16451 (Eqs. (1)–(14), App. A), 2409.02439 (Eqs. (1)–(6)), 2005.10256 (Eqs. (2)–(9), (19)–(29), Table 1), 2001.10666 (Eqs. (1)–(35)),
2411.11971 (Eqs. (4)–(7a)), 2504.02927 (Eqs. (1)–(33), Table 1), 2301.07617 (Eqs. (1)–(7)), 2511.20461 (Eqs. (1)–(12)), 2601.01043 (Eqs. (1)–(18)), 1705.03016 (Eqs. (1)–(8)),
2503.20732 (Eq. (1), §II), 1608.02940 (Eqs. (1)–(25)), 2312.10566 (Eqs. (1)–(17)). Verified against the arXiv API but not used beyond the catalog: 2104.13926, 1606.02201.
Claims rated here: CONFIRMED 2308.06314 Eq. (44) (generalised); misprints found: 2308.06314 Eq. (48), 2601.01043 Eq. (12) (both linear in a coupling that must be
squared; numerics follow the squared forms); validity issues: 2512.16451 (Born at its reach), 2301.07617 κ (estimate), 2601.01043 Eqs. (9)–(10) (ε → 1, α vs σ₁),
2308.06314 rigid-ion electron vertex, 1705.03016 Eq. (6) (Δp underestimated, conclusion unaffected). [UNVERIFIED]: Ambegaokar–Conway–Baym interference term (§4).

---
## Symbols introduced/used
Used as in NOTATION v4 + R9 rows and CONVENTIONS: q, k (absorbed-boson momentum, = k_φ), ω, m_φ, y_φ, Γ_abs, Γ_net, ℛ, ρ_T, ρ_χ, f_χ, 𝔇, S_ab, R, R̃, 𝒟^γ_{μν}, ε,
ε_∞, ε₀, ε_e, L, v_C, e² = 4πα, Ω, N, V, M_κ, M_cell, Z_κ, A_κ, Z*_κ, δρ_κ, 𝒵_κ, F^M_κ, F^Σ_κ, h^I_κ, 𝐈_I, 𝒥_κ, x_κ, P_κ, o_{Rκ}, j_κ, J_κ^{αβ}, s_e^α, n_e, n_κ, ρ_M,
𝐠, P_tot, e_κν, ω_Qν, b_{Qν}, n_{Qν}, n_B, W, 2W_κ, B_κ, D_κ^{q̂}, w_κ, Φ_{κκ′}, Φ^{(n)}, 𝒞_m, S^{(n_ph)}, n_ph, j_BZ, x_R, κ_BO, η_anh, E^kin_q̂, δM_κ, GS, X, X0,
X+, Λ, P_Λ, P_casc, E_R, E_d, P_FP, p_surv (WP5), 𝓃_D, F^{mag}_j, λ_{S,j}, ℰ^α_ν, U^B, V^B, a_{kν}, n_ν, J^{ex}_ij, 𝐒_j, g_e, μ_B, g_aee, g_aγγ, κ_mix, B₀, σ₁, n_r,
ω_p, m_e, m_χ, μ_χN, σ̄_n, τ, K, 𝒳, n_A, n_D, T, ref, scr; WP6 nuisance types M, A, E, Δ, T.
Introduced here (proposed NOTATION rows; collisions checked against v4 + R9):
| Symbol | Meaning | Where |
|---|---|---|
| 𝒱_ν(k) | k → 0 one-phonon absorption vertex of a row (B2.1.1) (not 𝒱_a, the DM vertex: decorated by the branch index ν and argument k only) | §1 |
| v_κ, v_I; v̄; δv_κ, δv_I | per-site linear vertex vector; mass-averaged vertex Σv/ΣM; mass-subtracted vertex | (B2.1.1), (B2.1.3), (B2.2.1) |
| c̃, c̃_κ ≡ c_κ/M_κ | coupling per unit mass (scalar–nucleon) | §8 |
| D_I(ω) | site-projected vibrational DOS (1/3)Σ_λ\|e_Iλ\|²δ(ω − ω_λ) of a disordered solid (= D_κ^{q̂} for cubic crystal sites) | (B2.2.1) |
| e_Iλ, ω_λ, λ (mode label) | eigenvector/frequency of mode λ of a disordered configuration (λ here is a mode index, not the WP3 exciton label; always with e or ω) | §2 |
| ξ_κ | 2411.10542 spin weight x_κλ_κ²𝒥_κ(𝒥_κ+1)/M_κ (source symbol, used only in (B2.2.2)) | §2.2 |
| C^{IR}(ω) | IR-to-VDOS coupling function ⟨\|p_λ\|²⟩_{ω_λ=ω} | (B2.3.1) |
| p_λ | mode effective charge Σ_Iε̂·Z*_I·e_Iλ/√M_I (not p(q̂)_{κα}, the crystal mode-charge vector, nor p_nn) | (B2.3.1) |
| γ_I, γ̄, σ_γ² | B−L charge per unit mass (A_I − Z)/M_I, its mean and variance (isotope channel only; distinct from γ_rel, γ_OA, γ_c by the subscript) | §2.4 |
| ω_BP, ξ_u, d_nn, g₂(r) | boson-peak frequency; neutral structural-unit size; nearest-neighbour distance; pair distribution | §2.3, §2.5 |
| V_opt, 𝔟_χN, σ_crit | optical potential, χN scattering length, Born-validity cross section | §3 |
| ⟨δn δn⟩, n₀, ξ (source) | 2512.16451 density-fluctuation correlator, mean nucleon density, correlation length (source notation, §3 only) | §3 |
| δ_Lind, Φ^{(2)}_eff, ρ_G, B^{SCHA}_κ | Lindemann ratio; self-consistent force constants; Gaussian trial density matrix; its displacement tensor | §4 |
| m_s, ω_L, k_⊥ | net spin per magnetic cell; Larmor frequency gμ_BB₀; k transverse to the magnetisation | §5 |
| ω_{K,x}, ω_{K,y}, ω_K, N_x,y,z, M_s | Kittel stiffnesses, Kittel frequency, demagnetising factors, saturation magnetisation | (B2.5.3) |
| F_M, F^{mag}_S | neutron magnetic form factor (spin + orbital); spin-only form factor | (B2.6.1) |
| S_n, γ_n, N_f, Ω_c, T_d | 2504.02927 neutron structure factor, neutron g-factor, formula units per cell, cell volume, data temperature (source notation) | §6 |
| L^{ph}_{Qν}, 𝐌^{ph}(q) | phonon angular momentum (not ℓ_Q, the zero-point length); Born-charge phonon magnetisation operator | §7 |
| D_ZFS, ω_Z, 𝓃_mol | SMM zero-field splitting, Zeeman energy, molecule density | (B2.7.2) |
| κ_URF | URF chiral-detection branching (replaces 2301.07617's κ, which is not κ_mix) | §7 |
| Y_CC, p_q, f_opt, ⟨N_x⟩, p_FH | colour-centre yield; charge-state factor; optically active fraction; excitons per deposit; STE → F–H probability | (B2.9.1) |
| S_CM, S_int, S^{diss}, p_esc, ΔE_B | molecular CM and internal structure factors; dissociative part; cage-escape probability; bond energy (1608.02940) | (B2.10.1) |
| r_c | core radius in the multipole remainder O(kr_c) | (B2.8.2) |
Deviation flagged: the source symbols κ (2301.07617 detection fraction; 2601.01043 dielectric function and kinetic mixing ε) are quoted only inside source formulas.

---
## Interface flags
| # | Owner / user | Quantity | Recorded form | This return | Action |
|---|---|---|---|---|---|
| IF-B2-1 | LIMITS, WP3-v3 §4 (L9b), WP2-v3 §4 | absorption into single phonons | not an entry (only dark photon via L9b) | (B2.1.1)–(B2.1.3), coupling-to-mass rule for any row; electron-scalar vertex Z_κ − Z*_κ | add row B2-L1; WP2 §4 cross-reference |
| IF-B2-2 | CONVENTIONS §11, WP6 library | glass reference | no value | metadata `ref=glass` (configuration-averaged GS) | coordinator |
| IF-B2-3 | CONVENTIONS §11, WP2-v3 §6, L18 | anharmonic order for quantum crystals | n_A finite order | `nA=SCHA` (Gaussian resummation) + cumulant increments; T-type nuisance | coordinator; WP2 |
| IF-B2-4 | WP2-v3 §12 gap 6 | amorphous S | open | (B2.2.4) + configurational average + spec §2.5 | WP2 next revision cites |
| IF-B2-5 | WP4-v3 §2, L13 | uniform-mode spin weight | LSWT only | Larmor theorem (B2.5.2) exact; Polder factor (B2.5.3); λ_{S,j} = g_j − 1 | WP4 cites |
| IF-B2-6 | WP5-v3 (heat), WP7-E | SMM avalanche trigger, chiral-band collection | none | detector-response functions outside S; P_casc inputs listed in §7 | WP5 / WP7-E |
| IF-B2-7 | WP5-v3 §4 ("ER defect creation … WP4") | ER colour-centre channel | qualitative | (B2.9.1)(b) Y_CC(eh,E) = ⟨N_x⟩p_FHp_survf_opt; NR f_opt ≈ 0 for aggregates at sub-GeV | WP5 next revision |
| IF-B2-8 | WP3-v3 §2, §4; WP0 §6.2(ii) | Migdal-type absorption | atomic only (catalog X10) | exact crystal identity (B2.8.1)–(B2.8.2) via WP0 (4.8); ELF replaces σ_γ near edges | WP3 cites |
| IF-B2-9 | SOTA literature list | source misprints / validity | — | 2308.06314 Eq. (48), 2601.01043 Eq. (12) misprints; 2512.16451 Born validity; 2601.01043 n_r/\|ε\|² | coordinator (SOTA) |
| IF-B2-10 | WP1/WP4 (spin data), WP6 | data-driven spin S | none | (B2.6.1)–(B2.6.2), longitudinal-part caveat, nuisance types | WP6 library key `X=data` |

---
## Proposed LIMITS rows
Provisional labels B2-L1…B2-L10 (numbers to be assigned by the coordinator; other R10 returns may also propose rows).
| # | τ / chain (URF) | Source formula [FT] | Status |
|---|---|---|---|
| B2-L1 (A4) | (3.5)–(3.6), GS, n_A = 0, K = 1ph-coh, k → 0, vertex (B2.1.1); coupling-to-mass (B2.1.3) | 2308.06314 Eqs. (2), (7), (16), (40)–(44), Table 1; 1712.06598 Eqs. (2)–(3) | DERIVED ✔ (Eq. (44) generalised) ✎ (electron scalar Z − Z*; Eq. (48) square) |
| B2-L2 (S5) | (3.5), tr J_κ row, unpolarised spins, (B2.2.1)–(B2.2.2), K = 1ph-inc | 2411.10542 Eqs. (25)–(31) | DERIVED ✔ |
| B2-L3 (A7) | L9b with the glass ε (B2.3.1); incoherent estimate (B2.2.1); `ref=glass` | 2603.22390 Eq. (2) (Eq. (3) crystalline truncation) | DERIVED ✔ (formula) |
| B2-L4 (§10(iii)) | (3.3), n_N row, n_ph = 0 of (B2.2.4), configurational average, Born | 2512.16451 Eqs. (2), (9)–(12) | ✎ (valid only for σ_χN ≪ σ_crit = m_χ⁴v⁴/4πn₀²) |
| B2-L5 (L11) | S^{GS}_κκ, (B2.4.1) SCHA; quasi-harmonic limit | 2409.02439 Eqs. (2), (4)–(5) | DERIVED ✔ (QH limit) + correction |
| B2-L6 (S2) | (3.5), spin row, k → 0; Larmor (B2.5.2), Polder (B2.5.3) | 2005.10256 Eq. (27); 2001.10666 Eqs. (25)–(27), (35) | DERIVED ✔ |
| B2-L7 (S6) | data-driven S_{ss} (B2.6.1)–(B2.6.2) | 2504.02927 Eqs. (8), (11), (15), (17), (26) | DERIVED ✔ + caveats (P_T only; g ≠ 2) |
| B2-L8 (L9/S8) | one-phonon Λ-resolved S + κ_URF; (B2.7.1) two-phonon magnetisation; (B2.7.2) SMM | 2301.07617 Eqs. (6)–(7); 2511.20461 Eqs. (3)–(4), (11)–(12); 2601.01043 Eqs. (3), (9)–(13) | ✎ (κ estimate; 2601.01043 Eq. (12) square, n_r/\|ε\|²) |
| B2-L9 (X10) | (3.5), n_κ rows, X sector, WP0 (4.8): (B2.8.1)–(B2.8.2) | 2312.10566 Eqs. (13)–(17) | DERIVED ✔ (+ ELF correction near edges) |
| B2-L10 (D2/D5) | (7.3) seeding with Y_CC (B2.9.1); (B2.10.1) | 1705.03016 Eqs. (1)–(2), (5)–(7); 1608.02940 Eqs. (4), (12), (23), (25) | ✎ (smooth threshold, survival, charge state; solid-state CM, cage) |
