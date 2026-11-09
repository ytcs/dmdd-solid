# R12 / WP7-B2-v2: lattice, spin, amorphous, defect and Migdal-absorption channels as explicit URF sector treatments (corrected after R11)

Revision agent, coordinator brief R12 (correction round). Supersedes returns/R10/WP7-B2.md (v1, kept as the historical record); this version reads without it.
Applies every verdict of referees/R11/REF-WP7-B2-A.md (items **A-n** = its verdict-table row n, and §-points) and REF-WP7-B2-B.md (items **B-n**, **B-Rn**).
Architecture: returns/R8/WP0-v3.md (cited "WP0 (n.m)", not re-derived). Neighbours: WP2-v3, WP3-v3 §2, §4, WP4-v3 §1–§2, §6, WP5-v3 §3–§4, §6.3, WP6-v3 (5.1).
CONVENTIONS.md, NOTATION v4 + R9 rows; state/CORRECTIONS.md read before every quote (no owed correction touches the sites used). Catalog: literature/CATALOG-A.md §3–§7, §10.
Checks: `code/WP7-B2-v2/checks.py` (sympy + mpmath + a 40-site numpy chain; **39 checks, all PASS, ≈ 6 s**), cited C-n (v1's 31 kept; C3, C4a, C15, C16
corrected; C21–C28 new). Tags per CONVENTIONS §12: [D], [D, sketch], [E], [C]; literature [FT], [ABS], [UNVERIFIED]. All arXiv IDs verified against the arXiv API
(the 19 of v1 and cond-mat/0604205, added in v2). Status: content CLAIMED; the R11 verdicts are applied as listed in the closing table §13.

---
## 0. What changed (v1 → v2) and results at a glance
**Changes (R11).** (1) GaAs "×0.47" **dropped** (A-1c, B-1 FALLS/SWC): the observable vertex for an electron-number scalar is the LO residue Z_κ − Z*_κ/ε_∞ (C21); the rate
relative to the source's own structure is ≈ 0.11 with ≈ 46% change in amplitude per 10% change of Z*/ε_∞ (C3, C28). (2) C^{IR} ∝ ω² **dropped** (A-2d FALLS, B-2b FALLS): C^{IR}(ω)
= A + Bω² (Taraskin et al., cond-mat/0604205 [ABS]); the incoherent estimate is the A term. (3) Overstated "source defects" retracted: the 2308.06314 rigid-ion vertex is
its own stated approximation (footnote 2, with the δZ fix); 2301.07617's κ is self-described as an estimate; phonon angular-momentum non-conservation is known
(Zhang–Niu pseudo-angular momentum [UNVERIFIED citation]) and is used here only to rate a source sentence. (4) Isotope B−L channel: novelty UNRESOLVED; mass-weighted
weight 1.88×10⁻⁴ (C4a); comparison with the EM-like part of B−L through Si's two-phonon ε(ω) added (C27). (5) SMM S⁺ branch and the metastable-well (avalanche) line
D_ZFS(2S−1) − ω_Z (C16). (6) Ni²⁺ neutron bracket ≈ 0.83 (λ_S ≈ 1 for quenched 3d; C24); λ_S = g − 1 only in J multiplets. (7) Magnetic-dipole DM makes single phonons
through the transverse ionic current j_T; u × P is the two-phonon readout operator. (8) X10 screening factor n_r/|ε|² = 1 + (3/2)ω_p²/ω², +1.2×10⁻³ at 1 keV in Si (C15).
(9) B2-L4 wording reconciled with §3. (10) Notation: ω_Lar (not ω_L), 𝔰_net (not m_s), disordered modes labelled ν, B−L ratio ϑ^{BL}_I, linewidths Γ^{ph}_ν. (11) τ strings carry
T; new τ values flagged. (12) Spin-ordered targets removed from the Theorem D GS chain. Plus the minor items (closing table).

| # | Item (catalog) | Result | Tag |
|---|---|---|---|
| 1 | A4 single-phonon absorption | (B2.1.1)–(B2.1.3): WP0 (3.5)–(3.6) with the GS one-phonon S of WP2-v3 (2.2) at k → 0 reproduces 2308.06314 Eqs. (2), (7), (16), (42) (C1). The vertex is invariant under v_κ → v_κ − λM_κ for any λ (coupling-to-mass, = 2308.06314 Eq. (44), CONFIRMED). Electron-scalar: proper vertex Z_κ − Z*_κ, **observable LO residue Z_κ − Z*_κ/ε_∞** (C21); GaAs rate ≈ 0.11 of the rigid-ion-charge structure, highly sensitive (C3) | D |
| 2 | S5, A7 | Random-coupling broadband formula (B2.2.1): exact when the random vertex is independent of the masses (spin orientation), leading order in σ_M/M̄ otherwise. Gives 2411.10542 Eq. (31) (C5); glass dark photon via ε(ω) with C^{IR} = A + Bω² | D / E |
| 3 | Isotope-disorder B−L channel | Broadband one-phonon absorption in monatomic crystals, weight Σx_IM_I(ϑ_I − ϑ̄)²/(M̄ϑ̄²) = 1.88×10⁻⁴ for Si (C4a); additive to the EM-like two-phonon term, estimated larger by ~6×10³ at 50 meV, 293 K (more at mK) [E] (C27). Novelty UNRESOLVED | D / E |
| 4 | L10 scattering S_NN | Exact Gaussian S of a disordered harmonic solid (B2.2.4); WP2-v3 gap 6 closed for S_self and for S_dist at n_ph = 1; S_dist at n_ph ≥ 2 [D, sketch] | D / D, sketch |
| 5 | §10(iii) | 2512.16451 Eq. (12) = n_ph = 0 term of (B2.2.4), configurationally averaged, Born (re-derived, C22). Born on the medium fails at its claimed reach: V_opt/E_kin = 1.9 (v = 10⁻³), 1.3 (v = 1.2×10⁻³) at σ_χN = 4×10⁻³⁸ cm², m_χ = 20 eV (C12, C26) | D / E |
| 6 | L11 solid He | 2409.02439 Eqs. (4)–(5) = quasi-harmonic limit of the SCHA S (B2.4.1); f-sum exact | D / D, sketch |
| 7 | S2 magnons | (B2.5.1) = 2005.10256 Eq. (27), 2001.10666 (C6); Larmor theorem (standard ESR result, cited) as the exact uniform-mode statement (C7); Kittel/Polder factor (C8) | D |
| 8 | S6 neutron-data S | (B2.6.1)–(B2.6.2) = 2504.02927 Eqs. (8), (17), (26) (C9); q̂q̂ part not measured; bracket [λ_S/(g/2)]², ≈ 0.83 for Ni²⁺ (C24) | D |
| 9 | L9, S8 | One-phonon chiral production via density, j_T and orbit–lattice rows; u × P magnetisation is a two-phonon operator (C20); SMM response with both branches (C16); 2601.01043 Eq. (12) misprint and n_r/\|ε\|² factor | D |
| 10 | X10, §10(iv) | Exact crystal identity from WP0 (4.8) (B2.8.1)–(B2.8.2) (C11); medium factor +1.2×10⁻³ at 1 keV in Si (C15) | D |
| 11 | D2, D5 | Seeding formulas (B2.9.1), (B2.10.1); 1705.03016, 1608.02940 are their limits; credits to the sources' own caveats | D / E |
| 12 | Source items | CONFIRMED misprints: 2308.06314 Eq. (48), 2601.01043 Eq. (12) (both need a square); 2512.16451 outside Born at its reach; 2601.01043 ε → 1; 2301.07617 decay "selection rule" not exact. Not defects: 2308.06314 rigid-ion illustration (its footnote 2), 2301.07617 κ (its own estimate) | FT |

---
## 1. A4: single-phonon absorption written out from WP0 (3.5) with WP2-v3 [D]

**Truncation chain.** WP0 (3.5)–(3.6) (absorption, ω = m_φ, k = k_φ ≈ m_φv); rows: nucleon density n_κ (scalar), electron density n_e (scalar), nuclear current j_κ (vector,
B−L), charge (dark photon); sector GS of Theorem D (6.1) with (O′_e)_{GS,GS} = ρ̄_e (WP0 §6.2(ii), WP2-v3 (1.2)); n_A = 0, K = 1ph-coh, n_ph = 1; photon-reducible part
through 𝒟^γ in (3.6). τ: `nB=0|ng=0|nA=0|X=-|nT=0|K=1ph-coh|Mg=-|nD=1` + `T=10mK;ref=normal;scr=ion,ext`. **Spin-ordered targets** (ALP and magnetic-dipole rows of
2308.06314 Table 1 with ordered spins) are **outside** this chain: magnetic insulators fail (H2) of Theorem D (WP0-v3 §6.2, G9). They go through clamped nuclei with
ref = LSWT and the magnon–phonon hybrid modes of WP4-v3 [2.5] (spin-phonon content X^p_h), with the sector question open (OW0-17).
**Formula [D].** Hypotheses: harmonic GS vibrations, k ≪ q_BZ, ω ≪ E_g, non-magnetic insulator. Linearising each row in u (WP2-v3 (1.2), (7.2)) gives ⟨kν|O(k)|0⟩ = √N𝒱_ν(k):

  𝒱_ν(k) = Σ_κ e^{ik·r_κ}e^{−W_κ} v_κ·e*_κν(k)/√(2M_κω_kν),   v_κ = { c_κk (nucleon scalar);  c_ek·(Z_κ𝟙 − Z*_κ) (electron scalar, proper);  −iωc_κε̂ (vector current);  −iωeZ*_κ·ε̂ (photon) }.   (B2.1.1)

  Γ_abs = (y_φ²/2ω)S_OO(k,ω),   S^{(1)}_OO = (2π/Ω)Σ_ν(n_kν+1)|𝒱_ν|²δ(ω − ω_kν);   Γ_net = −(y_φ²/ω)Im[R̃_OO + R̃_{Oμ}𝒟^γ_{μν}R̃_{νO}].   (B2.1.2)

The vector row uses ⟨kν|P_I/M_I|0⟩ = −iω_kν⟨kν|u_I|0⟩ ([H, R_I] = −iP_I/M_I for local H). R̃ is the photon-proper response, i.e. at zero macroscopic field, so Z*_κ (defined at zero
macroscopic field) is the correct input in R̃ (B-R1); the electrons' response to the LO macroscopic field sits in the reducible term.
**Coupling-to-mass [D] (C2).** Acoustic modes cannot absorb: ω_ac(k_φ) = c_νm_φv = m_φ would need c_νv = 1, while c_νv ≪ 1 always (A-1a, B-R1). Every optical mode at k → 0
is orthogonal to √M_κê (WP0 (4.8)(i)), so 𝒱_ν is unchanged under v_κ → v_κ − λM_κ for **any** λ; diatomic 𝒱 ∝ (v₁/M₁ − v₂/M₂)√(M₁M₂/M_cell) (B2.1.3). This is 2308.06314
Eq. (44), "exact for couplings g_Ψ ∝ m_Ψ" [FT, CONFIRMED]; its subtracted form factors use the orthogonal projection λ = Σv·m/Σm², a different (equally valid) λ, so subtracted
form factors are not unique while the vertex is (A-1b).
**Electron-scalar vertex at the observable pole [D] (C21).** A scalar couples to the longitudinal polarisation only. In the full R of WP0 (3.6) the TO pole cancels and the LO pole
remains. One-mode model (R̃_OO = a²P + χ, R̃_Oc = abP − χ, R̃_cc = b²P + χ, P = (ω² − ω_T²)⁻¹, ε_∞ = 1 − v_Cχ): Res_LO R_OO = [a + b(1 − 1/ε_∞)]². With a = Z_κ − Z*_κ (proper) and
b = Z*_κ the observable vertex is

  v_κ^{LO} = c_ek·(Z_κ𝟙 − Z*_κ/ε_∞),   (B2.1.4)

the electrons also screening the LO macroscopic field. GaAs (Z* = 2.1, ε_∞ = 10.9), d ≡ v_Ga/M_Ga − v_As/M_As: −0.00117 (B2.1.4), versus −0.00346 for the source's structure
(rigid ions Q = ±3 in its Eq. (40) and the electronic mixing term −ωq(1 − ε_∞)g_e/e of its Eq. (41), giving Z − Q/ε_∞). Rate ratio ≈ **0.11** (C3) [D for the vertex, E for
inputs]. Because Z_Ga/M_Ga ≈ Z_As/M_As (0.4446 vs 0.4405, C28) the residual is a near-cancellation: +10% in Z*/ε_∞ moves d by 46% (C3); isotopic mean masses (±0.01 u) move it
by ~5% [E]. The number is therefore an order-of-magnitude statement; the qualitative result (strong suppression of electron-scalar absorption in III–V crystals) is robust.
**Literature limit [FT].** 2308.06314 Eq. (16) Π_ΦΦ′ = Ω⁻¹Σ_ν(ΣF·T)2ω_ν/(ω² − ω_ν² + iωγ_ν)(ΣF·T)*, T = ε*/√(2mω_ν) (Eq. (14)); Eq. (2) Γ = −Im Π/m_φ; Eq. (7) with the
photon-mixing term. (B2.1.2) = Eq. (2)+(16) (C1b; −Im of the propagator → πδ as γ_ν → 0, C1a); the reducible part is Eq. (7)'s Π_φAΠ_Aφ/(m² − Π_AA). Photon-like couplings:
R = (g²/e²)(k²/ω²)(ρ_φ/ρ_T)Im(−1/ε) = Eq. (42). Dark photon: 1712.06598 Eqs. (2)–(3) R = ρ⁻¹(ρ_DM/m)κ²_effσ₁ = (ρ_DM/ρ)κ_mix²Im(−1/ε), the WP0 L9b Γ with ε from WP2-v3 (4.2).
**On the source's electron vertex (retracted as a "defect", A-1c(iii), B-12).** 2308.06314 states its rigid-ion assumption and the Born-charge fix in footnote 2 (δn_e =
iq^iδZ^{ik}u^k, δZ = Z* − Q_j) for the photon coupling; its main-text GaAs illustration (N_Ga,e = 28, N_As,e = 36) is rigid-ion. Applying its own prescription to the electron
row and taking the LO residue gives (B2.1.4). Whether its Fig. 2 projection includes δZ cannot be read off the text: UNRESOLVED.
**Leading corrections.** (i) (B2.1.4) sensitivity as above. (ii) Linewidths Γ^{ph}_ν(T) (phono3py): the retarded phonon self-energy, not a constant-width Breit–Wigner,
beyond ~5Γ^{ph}_ν (2603.22390 App. A notes the same for its Eq. (3) [FT]). (iii) Isotope/mass disorder: broadband background (§2.4). (iv) Two-phonon absorption at k → 0:
O(k⁴) for density rows, O(k⁰) for charge via ∂Z*/∂u (WP2-v3 (4.5)), the multiphonon sidebands of measured ε (1712.06598 [FT]).
**Source misprint [FT, CONFIRMED by A and B].** 2308.06314 Eq. (48) prints R ≈ ¼(g_aee/e)(ω/m_e)(ρ_φ/ρ_T)Im(−1/ε), linear in g_aee; its Eq. (49) g_aee ~ 10⁻⁹(100 meV/ω)(κ/10⁻¹⁶)
follows only from the squared form, which gives 3.1×10⁻¹⁰ (C13b): a residual factor ≈ 3, within the source's "∼" (order of magnitude), the linear form giving ~10⁻²⁵.
**Computation specification.** Inputs: DFPT phonons, Z*_κ, ε_∞ (QE/Abinit/VASP + phonopy; 8³ k; Γ plus 4³ q for linewidths); couplings per model. Code: PhonoDark-abs with
the electron-row vertex Z_κ − Z*_κ **and** the mixing term (3.6) evaluated with the same Z* and ε_∞, so that the LO residue (B2.1.4) is produced; patching N_e alone while keeping
rigid Q_j in Π_φA is inconsistent (A §9). Γ^{ph}_ν from phono3py (3×3×3 fc3). Convergence: ω_ν to 0.1 meV, Z* and ε_∞ to 1% (needed because of the near-cancellation),
Γ^{ph}_ν to 10%. Cost: DFPT ≈ 10² CPU·h; fc3 10³–10⁴ CPU·h. Output: ℛ(m_φ) per model, τ above, type-M nuisances on Γ^{ph}_ν and on Z*/ε_∞.

---
## 2. Random couplings and disorder: S5, A7, isotope channel, L10 [D]

**2.1 Random-coupling broadband absorption.** Hypotheses: (R1) harmonic vibrations of a fixed configuration {x⁰_I} (crystal with coupling disorder, or glass), modes ν with
e_Iν normalised over all sites; (R2) the k → 0 vertex is linear in u_I or P_I: ⟨ν|O|0⟩ = Σ_Iv_I·e*_Iν/√(2M_Iω_ν); (R3) after mass subtraction v_I = M_Iv̄ + δv_I with
v̄ = Σv_I/ΣM_I (the M_Iv̄ part drops out exactly for every ν ≠ translation, (B2.1.3); C4b for a random-mass chain), the δv_I are zero-mean, independent between sites and
isotropic. Then (C14)

  ⟨S^{(1)}_OO(k→0,ω)⟩_conf = (2π/V) Σ_I ⟨|δv_I|²⟩ D_I(ω)(n_B(ω)+1)/(2M_Iω),   D_I(ω) ≡ (1/3)Σ_ν|e_Iν|²δ(ω − ω_ν),   ∫D_I = 1.   (B2.2.1)

**Scope (A-2a, B-R2).** (B2.2.1) is exact when δv_I is statistically independent of the masses and force constants that shape e_Iν (nuclear-spin orientation on a fixed
isotope). When the random vertex sits on an isotope (²⁹Si spin carriers in S5; the isotope channel §2.4), δv_I and e_Iν are correlated through M_I: (B2.2.1) is then the
leading term [D at O((σ_M/M̄)⁰)], with O(σ_M/M̄) corrections [E]; the cure is isotope-class-resolved D_κ(ω) from the disordered Hessian. For structural disorder it is the
incoherent estimate (§2.3).
**2.2 S5 (axion–nuclear-spin coupling, absorption).** Chain: WP0 (3.5) with the trace of the nuclear spin-current row, O = Σ_κ tr J_κ (WP0 (2.2), F^Σ_κh^I_κ ≡ λ^I_κ), y_φ = 2g_pm_a
(from −(g/m_N)ȧσ·D, 2411.10542 Eq. (3) [FT]); GS, n_A = 0, K = 1ph-inc; τ `…|K=1ph-inc|…` + `T=10mK;ref=normal;scr=-`. Vertex v_I = −iωλ^I_I𝐉_I; unpolarised ⟨J^αJ^β⟩ =
δ^{αβ}𝒥(𝒥+1)/3 (C19):

  S_OO(ω) = (2π/Ω)Σ_κ x_κ(λ^I_κ)²𝒥_κ(𝒥_κ+1)ωD_κ(ω)/(2M_κ),   ℛ = ρ_aΓ_abs/(ρ_Tm_a) = 2πρ_am_ag_p²Σ_κ ξ_κD_κ(m_a)/M_cell,   ξ_κ ≡ x_κ(λ^I_κ)²𝒥_κ(𝒥_κ+1)/M_κ.   (B2.2.2)

**Literature limit [FT].** 2411.10542 Eqs. (25)–(31), R = 2π(ρ_am_a/Σ_jm_j)g_p²Σ_jξ_jD_j(ω), D_j = (3N)⁻¹Σ|ε|²δ: (B2.2.2) is Eq. (31) exactly (C5). Their k·J = imωJ·x step
(Eqs. (6)–(11)) is the commutator used in §1. Coherent part Eq. (21)/(24) ∝ P_κ² = the polarised term of WP2-v3 (7.1). **Leading corrections:** (i) spin isotope = mass isotope:
vertex–eigenvector correlation O(ΔM/M) (²⁹Si ≈ 3.5%) [E]; (ii) nuclear vs atomic mass in ⟨P_I⟩: O(δM_κ/M_κ) ≈ 3×10⁻⁴ (WP0 §6.2(ii)) [E]; (iii) quadrupole/Zeeman splittings
(≲ μeV) [E]; (iv) polarisation adds the coherent line.
**2.3 A7 (amorphous absorption) and the dark photon.** Chain: WP0 (3.5)–(3.6), charge row, GS of the glass configuration, n_A = 0 plus Γ^{ph}_ν; τ `…|K=1ph-inc|…` +
`T=10mK;ref=glass;scr=ion,ext`. Exact at this level [D] (WP2-v3 (4.2) with the glass Hessian, rank-1 macroscopic ε):

  ε(ω) = ε_∞ + (e²/V)Σ_ν |p_ν|²/(ω_ν² − ω² − iωΓ^{ph}_ν),   p_ν ≡ Σ_I ε̂·Z*_I·e_Iν/√M_I,   Γ_abs = κ_mix²m_φ Im[−1/ε(m_φ)].   (B2.3.1)

ε₂ ∝ C^{IR}(ω)D(ω)/ω with the IR-to-VDOS coupling function C^{IR}(ω) ≡ ⟨|p_ν|²⟩_{ω_ν=ω}, a known object (Galeener–Sen; Taraskin–Elliott [UNVERIFIED citations]). Its low-ω form
is **C^{IR}(ω) = A + Bω²** (Taraskin, Simdyankin, Elliott, Neilson, Lo, cond-mat/0604205 [ABS]: theory, THz data, simulations): A from fluctuating charges obeying only global
neutrality, B from locally neutral units. The incoherent estimate (B2.2.1), A ≈ Σ⟨|δZ*_I|²⟩/(3M_I)-type, is the **A term**, which dominates as ω → 0; local neutrality supplies Bω².
v1's "C^{IR} ∝ ω², (R3) fails at low ω" is withdrawn (A-2d, B-2b). The A/B split is [E] until computed from the glass models of §2.5.
**Literature limit [FT].** 2603.22390 Eq. (2): R = (ρ_A′/ρ_T)κ²Im[−1/ε(ω)] = WP0 L9b; its broadband claim is (B2.3.1) with measured or DFT ε; its crystalline Eq. (3)
(factorised LO/TO, Q = 100) is a rank-1 constant-width form, flagged by the authors far from resonance. Leading correction: ε from (B2.3.1) with Γ^{ph}_ν(T) at mK.
**2.4 Isotope-disorder channel for B−L [D for structure; E for size; novelty UNRESOLVED].** B−L charge per neutral atom: N_I = A_I − Z (nuclear B = A_I, electron L = Z). Decompose
the vector current as **g[N_I·(nuclear current) + (Z·nuclear − electron currents)]** (B-R3b). The second part is EM-like (charge-density pattern, coupling g ↔ κ_mix e); in Si its
one-phonon vertex is Z*_Si = 0, so it absorbs through Si's two-phonon ε(ω) (∂Z*/∂u, WP2-v3 (4.5)) at O(k⁰):

  Γ_EM = (g/e)² m_φ Im[−1/ε(m_φ)]   (photon-like coupling, = WP0 L9b with κ_mix → g/e).   (B2.4.1)

The first part, c_I = gN_I, has the same c/M on both diamond-lattice sites, so (B2.1.3) kills its crystalline single-phonon rate. Isotopes give δv_I = −iωgM_I(ϑ_I − ϑ̄),
ϑ_I ≡ N_I/M_I, ϑ̄ = Σx_IN_I/Σx_IM_I (mass-weighted, as v̄ requires), and (B2.2.1) yields a broadband one-phonon rate (vector DM averaged over polarisations):

  Γ_iso = πg²σ_wD(m_φ)/(2Ω_at),   σ_w ≡ Σ_Ix_IM_I(ϑ_I − ϑ̄)²,   σ_w/(M̄ϑ̄²) = 1.88×10⁻⁴ (natural Si, real masses; C4a).   (B2.4.2)

The two parts reach different final states (one phonon vs two phonons; Z* does not depend on the isotope at leading order), so they **add without interference** [D].
Ratio Γ_iso/Γ_EM = πe²σ_wD(ω)/(2Ω_atω Im(−1/ε)). Both terms are evaluated at the same ω = 50 meV, inside the one-phonon band (the isotope channel vanishes above it): D(50 meV) ≈ 20 eV⁻¹
per mode [E] and Im(−1/ε) ≈ 5×10⁻⁶ from the measured two-phonon absorption α ≈ 0.55 cm⁻¹ at 50 meV, 293 K (Deinzer & Strauch, PRB 69, 045205 (2004), Fig. 3, full text per
VER-WP7-B2-A; at 610 cm⁻¹ = 76 meV the same figure gives α ≈ 9–10 cm⁻¹, Im(−1/ε) ≈ 5.9×10⁻⁵). The ratio is ~6×10³ at 293 K (C27), larger at mK, where the two-phonon difference
processes freeze out: the isotope channel is estimated to exceed the EM-like part inside the one-phonon band (ω ≲ 65 meV) by ≳ 10³–10⁴ [E for D(ω) and the T scaling]; above the one-phonon band only Γ_EM survives. Mass disorder also deforms e_Iν, but the M_Iϑ̄ part still drops out exactly (C4b);
(B2.4.2) is leading order in σ_M/M̄ (§2.1). U(1)_B: δv only from binding-energy differences, (ΔB/A)/m_u ~ 10⁻⁴ [E]. Novelty: not found in the arXiv searches of either
referee or this author; disorder-induced one-phonon IR absorption in homopolar crystals is old solid-state physics; rating UNRESOLVED [E for novelty].
**2.5 L10: configurational averaging of S_NN.** Bloch's identity holds for any Gaussian state, so WP2-v3 (2.1) holds with (Rκ) → I for a disordered harmonic solid [D]:

  S(q,ω) = (1/V)∫dt e^{iωt}Σ_{IJ}c_I*c_Je^{−iq·(x⁰_I−x⁰_J)}e^{−W_I−W_J}exp Φ_IJ(t),   Φ_IJ(t) = Σ_ν[(n_ν+1)(q·e_Iν)(q·e_Jν)*e^{−iω_νt} + n_ν(c.c.)e^{iω_νt}]/(2ω_ν√(M_IM_J)).   (B2.2.4)

S = S_self + S_dist. S_self = WP2-v3 (3.2) with site-resolved w_I(q;ω′) from D_I^{q̂} (all n_ph; (3.5) per site class; f-sum (3.4′) per site) [D]. S_dist at n_ph = 1 contains the
disorder-broadened Brillouin peak at q ≲ 1/d_nn (propagating up to the Ioffe–Regel frequency ≈ ω_BP) and is computed by the direct Hessian sum [D]; at n_ph ≥ 2 it is
⟨e^{−iq·r_IJ}Φ_IJ^n⟩, decorrelating for q ≫ 1/d_nn with leading correction ∝ ∫d³r[g₂(r) − 1]j₀(qr)⟨Φ^n⟩_r [D, sketch]. **WP2-v3 gap 6 is closed for S_self and for S_dist at
n_ph = 1; S_dist at n_ph ≥ 2 remains [D, sketch]** (A-3; B-3 STANDS). Boson peak (excess D(ω)/ω² at ω_BP ≈ 4 meV in a-SiO₂ [E]) enters S_self ∝ q²D(ω)/ω, 2W_I = q·B_I·q,
and (B2.2.1)/(B2.3.1).
**Computation specification (§2).** Glass models by melt-quench MD with an MLIP (a-SiO₂, a-Si, SiN_x; 648–5184 atoms, ≥ 5 quenches), finite-difference Hessian, Z*_I by
DFPT on 192–648-atom subcells or an MLIP charge model that **reproduces site charge fluctuations (the A term), not only local neutrality** (A §9); isotope-resolved Hessians for
§2.4 (natural-Si supercells, 4096 atoms, 10 isotope realisations). Codes: LAMMPS + phonopy (Γ-only supercells); new module (≈ 250 lines) for D_I, C^{IR}, (B2.2.1), (B2.3.1),
(B2.4.2), (B2.2.4) at n_ph ≤ 2; WP2 (3.5) solver for S_self; measured low-T Si ε(ω) (two-phonon band) for (B2.4.1). Convergence: D(ω), C^{IR} to 5% between sizes; finite-size
gap 2πc_ν/L below threshold (L = 5 nm ⇒ ≈ 3 meV); configurational spread → type M. Cost ≈ 10⁴ CPU·h (MLIP) + 10³ (DFPT Z*). Outputs: ε(ω), D_I, C^{IR} (A, B), S(q,ω).

---
## 3. §10(iii): quadratic couplings scattering off density fluctuations in random media [D; E for numbers]

**Chain.** WP0 (3.3), single nucleon-density row ((m_N/Λ²)χ²N̄N acts as 𝒪₁^{(N)} for χ → χ at tree level), Born; S_NN GS; n_ph = 0 term of (B2.2.4); continuum limit
q ≪ 1/d_nn; configurational average. τ `nB=0|ng=0|nA=0|X=-|nT=0|K=el|Mg=-|nD=-` + `T=300K;ref=glass;scr=-` (elastic n_ph = 0 term; T enters only via 2W). CONVENTIONS §11 has no elastic K value: `K=el` is proposed (IF-B2-13).
**Formula [D].** The n_ph = 0 term of (B2.2.4) is 2πδ(ω)V⁻¹|Σ_Ic_Ie^{−W_I}e^{iq·x⁰_I}|²; for q ≪ 1/d_nn, Σ_I → ∫d³r n(r), n = n₀ + δn:

  ⟨S_el(q,ω)⟩ = 2πδ(ω)V⁻¹[n₀²|∫_Vd³r e^{iq·r}|² + ∫∫d³r₁d³r₂e^{iq·(r₂−r₁)}⟨δn(r₁)δn(r₂)⟩],   e^{−2W} → 1.   (B2.3.2)

This is 2512.16451 Eqs. (2), (7)–(10) [FT]. **Eq. (12) re-derived (C22):** ∫d³r e^{iq·r}e^{−r/ξ} = 8πξ³/(1 + q²ξ²)²; times V and δn², divided by N_tot² = n₀²V², V = 4πR³/3,
gives |F_fluc|² = (δn²/n₀²)6ξ³/(R³(1 + q²ξ²)²) (bulk limit, boundary terms dropped) — exactly Eq. (12). The observable (acceleration) is the q-weighted rate of WP0 (3.3).
**Validity [D] and the Born problem (CONFIRMED by both referees).** The homogeneous part is an optical potential V_opt = 2π𝔟_χNn₀/μ_χN (𝔟_χN the χN scattering length,
σ_χN = 4π𝔟_χN², μ_χN ≈ m_χ). Plane-wave Born on the medium requires V_opt ≪ E_kin = m_χv²/2, i.e. σ_χN ≪ σ_crit(v) = m_χ⁴v⁴/(4πn₀²). Ti–6Al–4V (n₀ = 2.69×10²⁴ cm⁻³,
Eq. (14)), m_χ = 20 eV: σ_crit = 1.2×10⁻³⁸ cm² at v = 10⁻³; at the paper's reach σ_χN ≈ 4×10⁻³⁸ cm², V_opt/E_kin = 1.9 (v = 10⁻³), 1.3 (v = 1.2×10⁻³; C26). V_opt/E_kin ∝ v⁻²,
so the criterion must hold over the f(v) weighting of the paper's Eq. (13) (high lab speeds weighted), not at one v (A §3). The paper invokes Born explicitly and has no
refraction/reflection/optical-potential discussion. Below σ_crit, the bulk phase kRV_opt/2E_kin ≫ 1 is a uniform shift that drops out of the fluctuation cross-section in DWBA
(k → k′ = k(1 − V_opt/E_kin)^{1/2}), leaving O(V_opt/E_kin) corrections plus surface refraction; inside one patch the phase is kξV_opt/2E_kin ≈ 0.2V_opt/E_kin [D, sketch]. Above
σ_crit the force is reflection-dominated (repulsive) or refraction-dominated (attractive) and scales with the composition difference of 𝔟̄n₀, not with δn² [D for the scaling].
Whether the paper's bound is too weak or too strong is not determined here [C for any limit].
Other corrections: 2W(q) ≈ q²⟨u²⟩ ≈ 1×10⁻¹¹ at q = 0.1 eV (negligible; v1's 10⁻¹⁷ corrected, C25); Bose enhancement cancels in the net momentum transfer, f(k)(1 + f(k′)) −
f(k′)(1 + f(k)) = f(k) − f(k′) [D]. **Spec:** ⟨δnδn⟩ from tomography or SAXS/USAXS (q = 10⁻²–1 eV); DWBA with V_opt: 1D transfer matrices for a slab, an axisymmetric DWBA for
the MICROSCOPE cylinders (A §9); ≈ 300 lines, CPU minutes. Output: a(σ_χN, m_χ) with Born/DWBA/reflection regimes marked over f(v).

---
## 4. L11: solid helium (quantum crystal) [D; D, sketch where marked]

**Chain.** WP0 (3.3), nucleon density row (c_κ = A_κF^M_κ), GS (E_g ≈ 20 eV), K = 1ph-coh / multi-inc. WP0 τ n_A = 0 assumes η_anh ≪ 1. Solid ⁴He has a Lindemann ratio
δ_Lind = ⟨u²⟩^{1/2}/d_nn ≈ 0.26–0.3 at melting densities (V_m ≈ 21 cm³/mol) [E]: the static-lattice Hessian is not a valid expansion point [E]. Under 1–40 GPa (V_m ≈ 9 → 4 cm³/mol)
δ_Lind ≈ 0.1 [E], and quasi-harmonic DFT matches measured dispersions (2409.02439 Fig. 2 [FT]). τ `nB=0|ng=0|nA=SCHA|X=-|nT=0|K=1ph-coh|Mg=-|nD=-` + `T=1K;ref=normal;scr=-` (IF-B2-3).
**Formula [D within a Gaussian density matrix].** Self-consistent harmonic Gaussian ρ_G: Φ^{(2)}_eff = ⟨∇∇V_pot⟩_{ρ_G}, B_κ = ⟨uu⟩_{ρ_G}, solved self-consistently (variational,
Gibbs–Bogoliubov). Inside ρ_G Bloch's identity is exact, so WP2-v3 (2.1)–(2.2), (3.2), (3.5) hold at all n_ph with eigenpairs of Φ^{(2)}_eff and 2W_κ = q·B_κ·q from ρ_G:

  S^{SCHA}(q,ω) = WP2-v3 (2.1)[Φ^{(2)} → Φ^{(2)}_eff, B_κ → B^{SCHA}_κ],   ∫ωS^{SCHA} = π𝓃_κq²|c_κ|²/M_κ (WP0 (4.6b), exact for any local H and any Gaussian).   (B2.4.1)

Beyond ρ_G [D, sketch]: non-Gaussian cumulants 𝒞₃, 𝒞₄ (WP2-v3 §6); the one–two-phonon interference term ∝ q³Φ^{(3)} [UNVERIFIED: Ambegaokar–Conway–Baym 1965]; the three
exact linear constraints of WP2-v3 (6.1) (L18) bound the anharmonic increment (type T). Exchange tunnelling (μK) and ³He negligible [E].
**Literature limit [FT].** 2409.02439 Eq. (4) S = (π/Ω)Σ_νω_νk⁻¹|Σ_jA_jF_{N_j}m_j^{−1/2}e^{−W_j}e^{iG·x⁰_j}(q·ε*)|²δ(ω_q − ω_νk), Eq. (5) W_j from the same modes, Eq. (2) Γ =
(πσ̄_n/μ²)∫d³q/(2π)³F²S: WP2-v3 (2.2) at n_ph = 1, T = 0, x⁰-phase convention (WP2-v3 (1.3)), i.e. (B2.4.1) with Φ_eff → quasi-harmonic Hessian. **Leading correction:**
SCHA renormalisation (few % in ω at ≥ 1 GPa, O(1) near melting [E]); 2W from PIMD B_κ (≈ 20–30% above harmonic at δ_Lind ≈ 0.1 [E]). **Spec:** MLIP on PBE+D3M at 1–40 GPa;
SSCHA or TDEP on PIMD (i-PI, P = 64, T ≈ 2 K), 128–432 atoms; Φ_eff → phonopy → DarkMAGIC/PhonoDark; multiphonon via WP2 (3.5). Convergence ω_eff 2%, B_κ 3%. Cost ≈ 10⁴ CPU·h
per pressure. Output S(q,ω;P) with δ_Lind flags.

---
## 5. S2: boson absorption into magnons (Kittel and in-field modes) [D]

**Chain.** WP0 (3.5) with the axion-wind spin row (LO −(g_aee/2m_e)(∇φ)·σ → s_e(k), WP0 §2), 𝔇 = (g_aee/m_e)²k^αk^β; clamped nuclei (magnetic insulators are outside
Theorem D, WP0 G9); WP4-v3 [1.1] projection, s_e → Σe^{ik·x}F^{mag}_jλ_{S,j}𝐒_j; ref = LSWT or exact where stated; k = m_av ≈ 0; F^{mag}_j(0) = 1. τ `nB=0|…|K=-|…` +
`T=10mK;ref=LSWT;scr=-`. **λ_{S,j} (A-6, B-R7):** within an LS J multiplet (unquenched 4f) ⟨s⟩ = (g_J − 1)⟨𝐉⟩, λ_{S,j} = g_J − 1 (the (g_j − 1) of 2005.10256 Table 1 [FT]);
for orbitally quenched 3d ions the pseudo-spin is S, λ_{S,j} = 1 − O((λ_SO/Δ_CF)²), and g − 2 is orbital admixture.

  Γ_abs = (g_aee²/2ωm_e²) k^αk^β S_{s^αs^β}(k,ω),   S_{αβ}(k→0,ω) = (2π/Ω)Σ_ν[(n_ν+1)ℰ^{α*}_νℰ^β_ν δ(ω − ω_{0ν}) + absorption term]   (WP4-v3 [2.1]–[2.2]).   (B2.5.1)

**Larmor theorem (standard ESR result; Kanamori–Tachiki 1962, Oshikawa–Affleck PRB 65, 134410 (2002) [UNVERIFIED citations]) applied to (B2.5.1) [D] (C7).** For
H_spin = isotropic exchange − ω_LarΣ_jS^z_j with one λ_S (uniform g), no anisotropy or dipolar field, k → 0: isotropic exchange commutes with 𝐒_tot, so [H, S^∓_tot] = ±ω_LarS^∓_tot and

  S_{k·s}(k→0,ω>0) = (2π/Ω)λ_S²(k_⊥²/2)𝔰_net δ(ω − ω_Lar)/(1 − e^{−βω_Lar}),   Γ_abs = πg_aee²λ_S²𝔰_netk_⊥²/(2m_e²ωΩ)·δ(ω − ω_Lar)/(1 − e^{−βω_Lar}),   (B2.5.2)

𝔰_net = ⟨S^z_tot⟩/N the net (ordered or field-induced) spin per magnetic cell (YIG 𝔰_net = 10 per 20-Fe cell [E]), k_⊥ ⊥ the moment. Exact at **any T**, ordered or paramagnetic
(A §4.1); at B₀ = 0 an antiferromagnet has 𝔰_net = 0 and ω_Lar = 0. AFM and anisotropy-gapped modes (NiO, 2411.11971 Eq. (4) [FT]) need WP4-v3 [2.1] with U^B, V^B. Non-uniform
λ_{S,j}: gapped modes acquire weight ∝ (λ_{S,j} − λ_{S,j′})², since [H_exch, Σ_jλ_{S,j}𝐒_j] ∝ Σ(λ_j − λ_j′)𝐒_j × 𝐒_j′ (2005.10256 Eq. (28) [FT]).
**Kittel/Polder [D] (C8).** Demagnetising factors N_{x,y,z} (HL, μ₀ = 1): ω_{K,x} = gμ_B(B₀ + (N_x − N_z)M_s), ω_{K,y} = gμ_B(B₀ + (N_y − N_z)M_s), ω_K = (ω_{K,x}ω_{K,y})^{1/2};
in (B2.5.2) k_x² → k_x²(ω_{K,y}/ω_{K,x})^{1/2}, k_y² → k_y²(ω_{K,x}/ω_{K,y})^{1/2}, δ(ω − ω_Lar) → δ(ω − ω_K); transverse average (ω_{K,x} + ω_{K,y})/(2ω_K) ≥ 1 (known Polder
physics, applied).   (B2.5.3)
**Literature limit [FT].** 2005.10256 Eq. (27) with f_j = −(i/√2)g_aee(g_j − 1)(√ρ_a/m_e)v_a: one sublattice, γ → 0, = (B2.5.1) (C6a). 2001.10666 Eqs. (25)–(27), (35): coherent
P(t) = |V|²t²/4 is the t ≪ 1/γ regime; its golden-rule rate (π/2)|V|²δ equals (B2.5.2) with g_aee/m_e = 1/f, λ_S = 1 (C6b); its one-spin-per-cell Eq. (13) is the Larmor case.
**Leading corrections:** demagnetisation (B2.5.3); FMR linewidth; exchange dispersion 𝒟_exk²/ω_Lar ~ 10⁻⁸ [E]; λ_S = g_J − 1 ≠ 1 for J-multiplet (4f) ions only; T factor.
**Spec:** J^{ex}, anisotropy, g tensors (DFT+U four-state or INS fits; ESR/FMR), sample shape; Colpa diagonalisation at k = 0 with demag; output ℛ(m_a, B₀). Cost ≪ 1 CPU·h.

---
## 6. S6: spin responses from measured neutron-scattering data [D]

**Chain.** WP0 (3.3)/(3.5) with the electron spin row only; target response from data (data-driven entry, CONVENTIONS §10 last line). τ: kernel slot not applicable; proposed
metadata `src=data` (IF-B2-10; v1's `X=data` withdrawn, B-R12) + `T=T_d→10mK;ref=LSWT`. Neutrons couple to the full magnetisation, transverse to q.
**Formula [D].** One magnetic species, dipole approximation, S_n per formula unit (2504.02927 Eq. (24); N_f units per cell Ω_c):

  P_T^{αβ}(q̂)S_{s^αs^β}(q,ω;T_d) = [λ_SF^{mag}_S(q)/((g/2)F_M(q))]²·4(2π)³m_e²N_fS_n(q,ω)/(γ_n²e⁴Ω_c),   F_M ≈ ⟨j₀⟩ + (1 − 2/g)⟨j₂⟩,   (B2.6.1)

  S(q,ω;T→0) = (1 − e^{−β_dω})S(q,ω;T_d)   (exact if (1 − e^{−βω})S is T-independent, harmonic magnons; ω > 0).   (B2.6.2)

g = 2, quenched orbit: bracket 1. Ni²⁺ (g ≈ 2.2, quenched, λ_S ≈ 1): [1/1.1]² ≈ **0.83** plus the ⟨j₂⟩ term [E] (C24; v1's 1.19 used g − 1 and is withdrawn). J-multiplet ions:
λ_S = g_J − 1.
**Literature limit [FT].** 2504.02927 Eqs. (8), (11), (15), (17) Γ_a = g_ae²m_av^iv^jχ″_ij, (26) S_n = N_f⁻¹(γ_n²e⁴/8m_e²)(Ω_c/(2π)³)P_T^{ij}χ″_ij. Dictionary χ″ = 2(1 − e^{−βω})S_{ss}
(σ = 2s; C9a); Eq. (17) = (B2.5.1) (C9b); Eq. (26) ⇔ (B2.6.1) at g = 2 (C9c). q-sign immaterial for P- or T-even targets (YIG centrosymmetric); else CONVENTIONS §3.
**What the data do not fix [D].** (i) Only P_T^{αβ}S_{αβ}: 𝔇 ∝ P_T couplings (magnetic dipole, anapole) are calibrated; q̂q̂ couplings (pseudoscalar, CP-violating scalar, dark EDM,
axion-wind absorption) need q̂q̂S, absent from unpolarised data; magnetic point group and polarisation analysis reconstruct it; the direction average gives only (2/3)tr S.
(ii) Absorption needs k ≈ 10⁻³m_a, far below neutron Q: use FMR/THz permeability, χ″ = μ_B⁻²Im(−μ⁻¹) (2504.02927 footnote to Eq. (17) [FT]), shape-corrected via (B2.5.3).
(iii) Phonon (nuclear) background at high q: subtract modelled S_NN (WP2) then project onto the PSD cone (WP0 (4.4)), or use spin-polarised neutrons.
**Uncertainty (WP6-v3 (5.1)).** Normalisation type M 10–20% [E]; extrapolation schemes (2504.02927 Fig. 2) type Δ; unmeasured regions type A (PSD only if the fill is PSD);
resolution type E; T-transfer residual (∝ M_s(T_d)/M_s(0) − 1) type M. **Spec:** S_n on (0.1 keV, 1 meV) grids (Horace/Mantid), g, F_M, F^{mag}_S (Wannier spin density);
module (≈ 200 lines) for (B2.6.1)–(B2.6.2), PSD projection, nuisance export; minutes.

---
## 7. L9 and S8: chiral phonons and single-molecule magnets [D]

**Chain.** Production: WP0 (3.3)/(3.5) with density/charge rows (2301.07617 uses the dark-photon 𝒪₁), the transverse ionic current j_T (WP2-v3 (7.2)) and spin/orbital rows
via spin–lattice coupling; GS (non-magnetic hosts; magnetic hosts as §5), n_A = 0, K = 1ph-coh, Λ = (Qν) (WP0 (7.1)). τ `…|K=1ph-coh|…` + `T=10mK;ref=normal;scr=ion`.
Readout: WP0 (7.3) P_casc with WP5 anharmonic down-conversion into a long-lived chiral band and magnetometry.
**(a) Chirality label [D].** L^{ph}_{Qν} = −iΣ_κe*_κν(Q) × e_κν(Q) (real, |L^{ph}| ≤ 1; zero with TR + inversion) — the definition of 2301.07617 Eq. (6), 2511.20461 Eq. (11) [FT]
in campaign normalisation. Chirality-resolved rate Σ_ν∫tr[𝔇ᵀS^{(1)}(q,ω;Qν)]δ(L − L^{ph}_{Qν}).
**(b) Production and readout operators [D] (A-8a, coordinator item).** Magnetic-dipole DM couples to the full ionic current 𝐣(q) = Σ_I(eZ*_I/M_I)P_Ie^{iq·R_I}, whose one-phonon
transverse part (WP2-v3 (7.2), with c_κ → eZ*_κ) gives **single-phonon production at O(q)** through q × 𝐣:

  ⟨Qν|q̂ × 𝐣(q)|0⟩ = −i√N Σ_κ(eZ*_κ/M_κ)√(M_κω_Qν/2) e^{iq·r_κ} q̂ × e*_κν(Q),   Q = q − G,   (B2.7.0)

(overall phase convention-dependent), so chiral modes (L^{ph} ≠ 0) are created singly wherever Σ_κ(Z*_κ/√M_κ)e^{iq·r_κ}q̂ × e*_κν ≠ 0 (polar, IR-active branches). The Born-charge **orbital moment** 𝐌^{ph}(q) = Σ_I(eZ*_I/2M_I)(u_I × P_I)e^{iq·R_I}
(2301.07617 Eq. (7), 2511.20461 Eq. (12) [FT] in operator form) is the O(q·u) piece of that expansion and is bilinear in (b, b†) (C20):

  ⟨Q₁ν₁,Q₂ν₂|𝐌^{ph}(q)|0⟩ = (e/2)Σ_κ(Z*_κ/M_κ)e^{iq·r_κ}δ_{Q₁+Q₂,q+G}(i/2)[(ω₂/ω₁)^{1/2} − (ω₁/ω₂)^{1/2}](e*_{κν₁}(Q₁) × e*_{κν₂}(Q₂)),   (B2.7.1)

(isotropic Z*_κ; overall phase convention-dependent). Hence: the moment is a two-phonon operator — **readout through it is quadratic** (a state property ⟨1|𝐌|1⟩, not a
transition element), and one-phonon production by magnetic-dipole DM proceeds through j_T, not through 𝐌^{ph}. v1's "magnetic-dipole DM produces chiral phonons in pairs" is
withdrawn. Giant moments (4f orbit–lattice) add one-phonon amplitudes ∂⟨s_e, L⟩/∂u in the spin/orbital rows [D, sketch].
**(c) Angular momentum in decay (known physics, applied).** [H, L^{ph}_z] = (i/2)uᵀ[J_z, D^dyn]u for H = ½p·p + ½u·D^dyn·u and L^{ph}_z = uᵀJ_zp (C23; C10 illustrates), so L^{ph} is
conserved only if D^dyn commutes with the on-site rotation generator; crystals conserve only the C_n pseudo-angular momentum (Zhang–Niu [UNVERIFIED citation]). 2301.07617 states
that chirality "adds conservation of phonon angular momentum as a selection rule for phonon decay processes" [FT]: as an exact rule this does not hold (CONFIRMED by both
referees). Its κ = 15% is the source's own declared estimate ("each decay pathway … equally likely") and is **not** a finding of this return (retracted from the v1 list).
URF quantity: κ_URF = Σ_{Qν}w_{Qν}P_casc(band_stable, |L^{ph}| > L_th | Qν) from three-phonon rates Γ_{ν→ν′ν″} (phono3py) with daughter L^{ph}.
**(d) SMMs (S8) [D] (C16).** Dilute non-interacting molecules, H_SMM = −D_ZFSS_z² − ω_ZS_z (2601.01043 Eq. (3) [FT], plus Zeeman), s_e = λ_S𝐒, populations p_m:

  S_{k·s}(k→0,ω) = 𝓃_mol2πλ_S²(k_⊥²/4)Σ_mp_m{[S(S+1) − m(m−1)]δ(ω − D_ZFS(2m−1) − ω_Z) + [S(S+1) − m(m+1)]δ(ω + D_ZFS(2m+1) + ω_Z)} (+ k_z²S^zS^z elastic),   (B2.7.2)

with Γ_abs from (B2.5.1). Ground well m = S: line D_ZFS(2S−1) + ω_Z, weight 2S. **Metastable well m = −S** (the state an avalanche detector is prepared in, 2601.01043 Eqs. (4)–(6),
barrier U − ½ΔE_Zee): S⁺ line at **D_ZFS(2S−1) − ω_Z**, weight 2S (B-R8, A §5.2). Mn₁₂-like S = 10, D_ZFS ≈ 0.05 meV: ≈ 1 meV [E]. Dark-photon absorption: WP0 L9b with the SMM
crystal's ε.
**Literature limits [FT].** 2301.07617/2511.20461 rates: PhonoDark single-phonon rates (2511.20461 Eqs. (3)–(4), (8)) × κ = (a) with κ as an assumed P_casc. 2601.01043: R =
Eqs. (17)–(18) with Eqs. (9)–(10) inserted (⟨nσv⟩ ≈ ε²⟨nσ^γ⟩, σ^γ = α/n, "relative permittivity … approximated as unity"); URF L9b gives R_URF/R_src = n_r/|ε|² (C13c), ≈ 0.25 for
ε ≈ 2.5 at the IR band [E] (ε₂ not small there). **Misprint (CONFIRMED by A and B):** Eq. (12) R ≃ (g_aγγB₀/m_a)(ρ_DM/ρ_T)Im[−1/κ(m_a)] is linear; WP0 (2.9) and its own Eq. (13)
(g_aγγ ~ εm_a/B₀) need (g_aγγB₀/m_a)² (C13a). The avalanche trigger Eq. (6) is a detector response (heat threshold), not a target response (IF-B2-6).
**Spec:** DFPT phonons and Z* (Abinit/QE), L^{ph} on 10×10×20 grids, phono3py fc3 for Γ_{ν→ν′ν″} (MOF cells ≈ 10⁵ CPU·h, the bottleneck), WP5 Monte-Carlo with L^{ph} labels;
(B2.7.0), (B2.7.1) modules (≈ 200 lines). SMM: D_ZFS, g from ESR/CASSCF-SO (≈ 10³ CPU·h/molecule), (B2.7.2) analytic with metastable populations; IR ε from DFPT.

---
## 8. X10 and §10(iv): Migdal-type absorption (scalar–nucleon couplings) [D]

**Chain.** WP0 (3.5) with O = Σ_κc_κn_κ(k) (c_κ = g_pZ_κ + g_n(A_κ − Z_κ)); sector X (electronic excitations, ω = m_φ ≫ ω_max); WP0 (4.8); n_D = 1 (k = m_φv ≪ 1/r).
τ `nB=-|ng=0|nA=0|X=RPA+LFE|nT=0|K=-|Mg=sud|nD=1` + `T=10mK;ref=normal;scr=ext,LFE`. `nB=-` because (B2.8.1)–(B2.8.2) are exact identities with no BO expansion (acceleration form and WP0 (4.8)); no BO order is truncated.
**Exact identities [D].** (i) Acceleration form (C11a): for kinetic P_I²/2M_I and potentials multiplicative in R_I, ⟨f|R_I|i⟩ = ⟨f|∇_{R_I}V_pot|i⟩/(M_Iω_fi²):

  ⟨f|O(k)|i⟩ = ik·Σ_I(c_I/M_I)⟨f|∇_{R_I}V_pot|i⟩/ω_fi² + O(k²)   (any target, any BO order).   (B2.8.1)

(ii) Mass-proportional coupling c_κ = c̃M_κ: O = c̃(ρ_M − m_en_e), ρ_M the mass density of WP0 (4.8); [H, ρ_M(k)] = k·𝐠(k), 𝐠(0) = P_tot, so ⟨f|ρ_M(k)|i⟩ = O(k²) while ⟨f|n_e(k)|i⟩ = O(k):

  ⟨f|O(k)|i⟩ = −c̃m_e⟨f|n_e(k)|i⟩[1 + O(kr_c)]  ⇒  S^X_OO = c̃²m_e²S_ee,   Γ_abs = (y_φ²c̃²m_e²k²/(e²ω))Im[−1/ε(k→0,ω)],   (B2.8.2)

using S_ee = (2k²/e²)Im(−ε_e⁻¹), ε_e = ε at ω ≫ ω_max (WP0 (5.5)(ii)). Atom: (B2.8.1) → c(m_e/m_at)⟨f|Σ_iρ_i|i⟩ (relative coordinates; WP0 §6.2(ii)). Multi-species targets satisfy c ∝ M
only to the mass defect (~10⁻³); the residual and c_κ ∉ ∝ M_κ use (B2.8.1) per species, c̃_κ = c_κ/M_κ, for core shells localised on κ [D for localised cores, E for valence].
**Literature limit [FT].** 2312.10566 Eqs. (13)–(17), σ_φ = g²(m_e²/m_p²)(k/ω)σ_γ/4πα: dilute limit Im(−1/ε) → 𝓃_atσ_γ/ω, c̃ = g/m_p, so (B2.8.2) per atom = σ_φv (C11b).
**Leading correction (corrected, A §6, B-R9).** Medium factor Im(−1/ε)/(Im ε/n_r) = n_r/|ε|² = 1 + (3/2)ω_p²/ω² + … for ε ≈ 1 − ω_p²/ω², with ω_p from all electrons bound below ω:
Si at 1 keV (12 e/atom, ω_p ≈ 29 eV) **+1.2×10⁻³** (C15) [E for the free-electron form]; O(1) near the plasmon and edges, where the ELF must replace σ_γ (the source warns that solid-state
rates "may significantly differ" [FT]). Next: O(kr_c) multipoles (Eq. (15)); valence part for c_κ ∉ ∝ M_κ, interfering with PAER-type amplitudes when c_ec_κ ≠ 0 (WP0 §6.2). §10(iv) is
this entry; it adds to the electron-scalar 𝒯_e channel of WP3-v3 §4(d) without double counting. **Spec:** ELF (WP1 RPA+LFE with cores; Henke/NIST above 30 eV); per-shell c̃_κ.

---
## 9. D2: colour-centre creation (thresholds, yields, interface to WP5-v3) [D for structure; E for numbers]

**Chain.** WP0 (7.3) with seeds Λ from (a) GS S_κκ (recoil E_R, r̂_R; WP2 L6, K = imp at E_R ≫ ω_D) and (b) X-sector e–h/exciton seeds (ER); P_casc from WP5-v3 §3, §4, L22.
τ `…|K=imp|…` + `T=10mK;ref=normal;scr=-` (NR), `X=RPA+LFE` (ER seed).

  dℛ_CC/dt = (ρ_χ/m_χρ_T)∫d³vf_χ∫d³q/(2π)³Σ_Λtr[𝔇ᵀS(q,ω_q;Λ)]Y_CC(Λ),   Y_CC(κ,E_R,r̂) = P_FP(E_R,r̂)p_survp_qf_opt,   Y_CC(eh,E) = ⟨N_x⟩(E)p_FHp_survf_opt.   (B2.9.1)

P_FP: anion displacement probability (smooth, WP5 L22 (a)); p_surv: survival against close-pair recombination; p_q: charge state (F needs a trapped electron); f_opt: read-out
fraction; ⟨N_x⟩: excitons per ER deposit; p_FH: self-trapped exciton → F–H.
**Literature limit [FT].** 1705.03016 Eq. (1) ∂R/∂φ_c = f_PN²N_T(ρ_χ/m_χ)(σ̄_n/16π²μ²)∫dq²∫d³v∫dφ″_q|F_DM|²Θ(q − q_min)f/v, Eq. (2) q_min, Eq. (5) E_r^min = q_min²/2m₁: (B2.9.1)(a)
with S^{GS}_κκ → free nucleus, Y_CC → Θ(E_R − E^min_R(r̂)), p_q = p_surv = f_opt = 1. The source itself states that Eq. (1) counts "a dislocated nucleus … not … a specific defect
type", assumes electron occupation "spontaneous and immediate", and estimates quantum threshold shifts ≲ 15% (its footnote 2) — so p_q, f_opt and the smearing below are
refinements it anticipated (B-R10). **Leading corrections:** (i) seed Doppler width σ_E ≈ [(4/3)E_RE^kin_q̂]^{1/2} ≥ 1 eV (WP5 L22 (a)), ≈ 10% of the 9 eV LiH threshold [E],
consistent with the source's ≲ 15%; its Eq. (6) takes Δp ~ αm_e = 3.7 keV, the H zero-point value is (Mω/2)^{1/2} ≈ 6.9 keV per component (Δp/q_min ≈ 0.05–0.09; C17), conclusion
unaffected [FT, CONFIRMED]; (ii) p_surv < 1 near threshold; (iii) p_q: few e–h at sub-keV E_R, many vacancies stay F⁺ [E]; (iv) aggregates: 2503.20732 reads out F₂⁰ (650 nm) and
F₃⁺ (525 nm) formed in dense recoil tracks (≈ 1200 vacancies/μm, TRIM) [FT]; a sub-GeV recoil makes one or a few vacancies, immobile at mK (WP5 (W12)), so f_opt(aggregates) ≈ 0
and single-F readout is needed [E/C]. ER: 2503.20732 measures a ⁶⁰Co γ response ≈ 1/50 of fast neutrons per dose [FT]; ER threshold = lowest exciton energy (LiF ≈ 13 eV [E]);
p_FH(T) [UNVERIFIED values]. **Spec:** MLIP/DFT MD E_d(r̂) for the anion sublattice (LiF/MgO/LiH; 10⁴ PKA directions, zero-point-sampled), p_surv by MD + kMC, HSE ΔSCF charge
levels, STE → F–H by surface hopping (≈ 10⁵ CPU·h), BSE F-band cross sections. Output Y_CC tables with type-M nuisances.

---
## 10. D5: bond breaking in molecular solids [D for structure; E for numbers]

**Chain.** WP0 (3.3), nucleon row on atom 1 of a molecule, GS (or X for electronic dissociation), WP0 (7.3) with P_casc = cage escape. τ `…|K=imp|…` + `T=10mK;ref=normal;scr=-`.
**Formula [D].** Hypothesis (M): the intermolecular potential is independent of the internal coordinate r, **including its orientation** (free-rotor internal motion; A-11).
With R₁ = R_CM + (m₂/M)r and m₂/M = μ₁₂/m₁ (C18):

  S₁₁^{GS}(q,ω) = ∫(dω′/2π)S_CM(q,ω′)S_int((μ₁₂/m₁)q, ω − ω′),   S_int(p,ω) = 2πΣ_f|⟨f|e^{ip·r}|0⟩|²δ(ω − E_f + E_0);   S^{diss} = S_int on E_f > ΔE_B.   (B2.10.1)

S_CM is the lattice S of the whole molecule (WP2-v3 (3.2)/(5.3), mass M_mol); (M) fails for dissociating fragments in the cage, absorbed into p_esc.
**Literature limit [FT].** 1608.02940 Eq. (4) q_min = (m₁/μ₁₂)(2μ₁₂ΔE_B)^{1/2}, Eqs. (11)–(12) |F_dis|², Eq. (23) classical rate, Eq. (25) quantum rate: (B2.10.1) with S_CM → free
molecular recoil and p_esc = 1; Eq. (23) is the impulse limit of S_int. **Leading corrections:** (i) bound CM: at q_min ~ 10² keV, x_R(CM) ≫ 1, IA with Doppler width from ⟨P_CM²⟩
(plus the internal zero-point spread of its Eqs. (8)–(9)); recoil-free fraction ≈ 0 [E]; (ii) cage escape p_esc < 1 (MD) [E]; (iii) ER into repulsive σ* surfaces (X sector) with
p_diss(Λ) [E]. **Spec:** S_int from Morse/ab initio potentials, S_CM from phonopy/PIMD, p_esc by MLIP MD (10³ trajectories per (E_int, r̂)); ≈ 10³ CPU·h.

---
## 11. Exact remaining gaps
1. **A7/L10:** the A and B coefficients of C^{IR} = A + Bω², and S_dist at n_ph ≥ 2, need the glass models of §2.5; not computed here.
2. **Isotope B−L channel:** the ratio to the EM-like term uses the 293 K two-phonon α at 50 meV (Deinzer & Strauch 2004) and an estimated D(ω); low-T measured ε(ω) and isotope-resolved
   Hessians are needed; O(σ_M/M̄) vertex–eigenvector correlations not computed.
3. **§10(iii) above σ_crit:** the reflection/refraction force on heterogeneous test masses is not computed [C for any bound].
4. **L11 near melting:** no remainder bound beyond the Gaussian at δ_Lind ≈ 0.3.
5. **S2 beyond the Larmor hypotheses:** anisotropic/dipolar/AFM targets need numerical LSWT + demag.
6. **S6 longitudinal part:** no data-only route from unpolarised neutrons.
7. **L9/S8:** κ_URF needs mode-resolved three-phonon decay in MOF cells; giant-moment mechanisms open.
8. **D2:** p_q, p_FH, single-F readout at mK unknown; ER/NR calibrated only at MeV doses.
9. **D5:** p_esc and σ* yields unquantified.
10. **X10 valence for c_κ ∉ ∝ M_κ:** needs non-adiabatic ⟨f|∇_{R_I}V|i⟩ in the crystal (WP3 (W.5)).
11. **A4 in polar crystals:** the electron-scalar rate is a near-cancellation (C3, C28); a reliable number needs Z*, ε_∞ and isotopic masses to ≲ 1%.
12. **Spin-ordered targets:** their sector theorem is open (OW0-17); §1 does not cover them.

---
## 12. Literature (status in this return)
[FT] (read in v1, literature/papers-WP7-B2/, PDFs deleted): 2308.06314, 1712.06598, 2411.10542, 2603.22390, 2512.16451, 2409.02439, 2005.10256, 2001.10666, 2411.11971, 2504.02927,
2301.07617, 2511.20461, 2601.01043, 1705.03016, 2503.20732, 1608.02940, 2312.10566 (equation lists as cited in the sections). [ABS]: cond-mat/0604205 (Taraskin et al., verified
via the arXiv API; DOI 10.1103/PhysRevLett.97.055504). [UNVERIFIED]: Ambegaokar–Conway–Baym (1965); Kanamori–Tachiki (1962); Oshikawa–Affleck (2002); Zhang–Niu (2014/2015);
Galeener–Sen; Taraskin–Elliott (IR coupling). [FT via VER-WP7-B2-A]: Deinzer & Strauch, PRB 69, 045205 (2004), Fig. 3 (Si two-phonon α). Ratings: CONFIRMED 2308.06314 Eq. (44); misprints CONFIRMED by both referees: 2308.06314 Eq. (48),
2601.01043 Eq. (12); validity: 2512.16451 (Born at its reach, CONFIRMED), 2601.01043 (ε → 1, CONFIRMED), 2301.07617 (decay selection rule not exact, CONFIRMED), 1705.03016
Eq. (6) Δp (CONFIRMED, conclusion holds). Not defects: 2308.06314 rigid-ion illustration (footnote 2; Fig. 2 UNRESOLVED), 2301.07617 κ (own estimate). Novelty: isotope channel
UNRESOLVED; C^{IR} low-ω law REFUTED as new (prior art).

---
## 13. Closing table (one row per R11 referee item)
Status: **applied**, **no change** (STANDS), **dropped** (FALLS), **rebutted** (none in v2).
| Item | Verdict | Status | Where |
|---|---|---|---|
| A-1a / B-1 (formulas) | STANDS / SWC | no change; acoustic condition c_νv ≪ 1 fixed | §1 |
| A-1b coupling-to-mass "generalised" | SWC | applied: invariance under any λ; "CONFIRMED" only; projection difference stated | §1 |
| A-1c / B-1 GaAs ×0.47 (coordinator: FALLS) | FALLS (rate) / SWC | **dropped**; LO residue Z − Z*/ε_∞ (C21), ratio ≈ 0.11, sensitivity 46% per 10% (C3, C28); footnote 2 credited; Fig. 2 UNRESOLVED | §1, §0 |
| A-2a / B-2, B-R2 (R3) scope | SWC | applied: exact for mass-independent vertices; leading order in σ_M/M̄ otherwise | §2.1, §2.2 |
| A-2b S5 | STANDS | no change | §2.2 |
| A-2c glass ε | STANDS | no change | §2.3 |
| A-2d / B-2b C^{IR} ∝ ω² | FALLS | **dropped**; A + Bω² (cond-mat/0604205); C^{IR} credited as prior art | §2.3, §11 |
| A-2e / B-2a, B-R3 isotope channel | SWC (novelty UNRESOLVED) | applied: 1.88×10⁻⁴ mass-weighted (C4a); EM-like decomposition and comparison (B2.4.1)–(B2.4.2), C27; "not found [E]" | §2.4 |
| A-3 / B-3 gap 6 | SWC / STANDS | applied A's wording (closed for S_self and S_dist n_ph = 1) | §2.5 |
| A-4 / B-4 §10(iii) | STANDS / SWC | applied: Eq. (12) derived (C22); f(v) criterion (C26); 2W ≈ 10⁻¹¹ (C25); DWBA wording reconciled with B2-L4; axisymmetric DWBA spec | §3, B2-L4 |
| A-5 / B-5 solid He | STANDS | no change; τ with T | §4 |
| A-6 / B-6, B-R6 Larmor, Polder, λ_S | SWC | applied: cited as standard; any T; AFM statement at B₀ = 0; λ_S = g − 1 only for J multiplets; ω_Lar, 𝔰_net | §5 |
| A-7 / B-7, B-R7 Ni²⁺ bracket | SWC | applied: ≈ 0.83 (C24) | §6 |
| A-8a magnetic-dipole single phonons | SWC | applied: j_T one-phonon vertex (B2.7.0); u × P two-phonon readout | §7(b) |
| A-8b / B-8 L^{ph} conservation | STANDS / SWC | applied: Zhang–Niu cited, general identity (C23); κ not a finding | §7(c) |
| A-8c / B-R8 SMM S⁺ branch | SWC | applied: both branches, metastable line D(2S−1) − ω_Z (C16) | §7(d) |
| A-8d 2601.01043 | STANDS | no change; quote fix (Eqs. (17)–(18) with (9)–(10)); 0.25 [E] | §7 |
| A-9 / B-9, B-R9 X10 screening | SWC | applied: 1 + (3/2)ω_p²/ω², +1.2×10⁻³ (C15); mass-defect scope | §8 |
| A-10 / B-10, B-R10 D2 | STANDS / SWC | applied: source caveats credited (footnote 2, "dislocated nucleus", occupation) | §9 |
| A-11 / B-11 D5 | STANDS | applied: (M) includes orientation independence | §10 |
| A-12 / B-12 source-defect list | SWC | applied: Eq. (49) residual ×3; rigid-ion and κ retracted as defects | §1, §7, §12 |
| A-C / B-R11 notation | SWC | applied: ω_L → ω_Lar; m_s → 𝔰_net; mode label ν; B−L ratio ϑ^{BL}; linewidth Γ^{ph}_ν | throughout, symbols |
| A-C spin-ordered in GS chain | SWC | applied: removed; LSWT + WP4 [2.5] route; open sector | §1, §11 |
| A-C / B-R12 τ strings | SWC | applied: T in every τ; `X=data` → `src=data`; `ref=exact(Larmor)` dropped (ref=LSWT + exact statement); `K=1ph-inc` kept in the K slot, `ref=glass` as metadata; IF table extended | all §, IF-B2-2, -3, -10, -11 |
| B-R1 R̃ zero-field statement | SWC | applied | §1 |
| A-§9 PhonoDark-abs consistency, glass charge model | remark | applied in specs | §1, §2.5 |
| Coordinator: copy checks to code/WP7-B2-v2 and re-run | — | applied: 39/39 PASS | header |
**Count:** 31 referee rows (A 22, B 13 + R1–R12 merged where identical); dropped 2 (GaAs ×0.47; C^{IR} ∝ ω²); applied 22; no change 7; rebutted 0.

---
## Symbols introduced/used
Used as in NOTATION v4 + R9 rows and CONVENTIONS: q, k (= k_φ), ω, m_φ, y_φ, Γ_abs, Γ_net, ℛ, ρ_T, ρ_χ, f_χ, 𝔇, S_ab, R, R̃, 𝒟^γ_{μν}, ε, ε_∞, ε₀, ε_e, L, v_C, e² = 4πα,
Ω, N, V, M_κ, M_cell, Z_κ, A_κ, Z*_κ, δρ_κ, F^M_κ, F^Σ_κ, h^I_κ, 𝐈_I, 𝒥_κ, x_κ, P_κ, j_κ, J_κ^{αβ}, s_e^α, n_e, n_κ, ρ_M, m_s (species mass, WP0 (4.8) only), 𝐠, P_tot, ν
(branch/mode), e_κν, ω_Qν, ω_L (LO frequency, unused here), ω_Lar (Larmor), n_{Qν}, n_B, W, 2W_κ, B_κ, D_κ^{q̂}, w_κ, Φ_{κκ′}, Φ^{(n)}, 𝒞_m, n_ph, x_R, η_anh, E^kin_q̂, δM_κ, GS,
X, Λ, P_casc, E_R, E_d, P_FP, p_surv, F^{mag}_j, λ_{S,j}, ℰ^α_ν, U^B, V^B, J^{ex}_ij, 𝐒_j, g_aee, g_aγγ, κ_mix, B₀, σ₁, n_r, ω_p, τ, K, 𝒳, n_A, n_D, T, ref, scr; WP6 types.
Introduced (proposed NOTATION rows; v1 collisions resolved per A-C, B-R6, B-R11):
| Symbol | Meaning | Where |
|---|---|---|
| 𝒱_ν(k) | k → 0 one-phonon absorption vertex of a target row (not 𝒱_a, the DM vertex) | (B2.1.1) |
| v_κ, v_I; v̄; δv_κ, δv_I; v_κ^{LO} | per-site linear vertex; mass-averaged vertex Σv/ΣM; mass-subtracted vertex; LO-residue vertex | (B2.1.1)–(B2.1.4), (B2.2.1) |
| D_I(ω), e_Iν, ω_ν | site-projected VDOS and modes ν of a disordered configuration (ν as in NOTATION, here a configuration-mode index) | §2 |
| λ^I_κ | nuclear spin coupling F^Σ_κh^I_κ (2411.10542's λ_j; decorated to avoid the λ exciton label) | §2.2 |
| ξ_κ | 2411.10542 spin weight (source symbol) | (B2.2.2) |
| C^{IR}(ω), A, B (IR) | IR-to-VDOS coupling function (prior art) and its Taraskin coefficients | §2.3 |
| p_ν | mode effective charge Σ_Iε̂·Z*_I·e_Iν/√M_I (not p(q̂)_{κα}, not p_nn) | (B2.3.1) |
| Γ^{ph}_ν | phonon/vibrational linewidth (replaces v1 γ_λ) | (B2.3.1), §1 |
| ϑ^{BL}_I (= ϑ_I), ϑ̄, σ_w | B−L charge per unit mass N_I/M_I, its mass-weighted mean, weighted variance Σx_IM_I(ϑ_I − ϑ̄)² | §2.4 |
| Ω_at | atomic volume | (B2.4.2) |
| ω_BP, d_nn, g₂(r) | boson-peak frequency; nearest-neighbour distance; pair distribution | §2.3, §2.5 |
| V_opt, 𝔟_χN, σ_crit(v) | optical potential; χN scattering length; Born-validity cross section | §3 |
| δ_Lind, Φ^{(2)}_eff, ρ_G, B^{SCHA}_κ | Lindemann ratio; SCHA force constants; Gaussian trial state; its displacement tensor | §4 |
| 𝔰_net, k_⊥ | net spin per magnetic cell (replaces v1 m_s); k transverse to the moment | §5 |
| ω_{K,x}, ω_{K,y}, ω_K, N_{x,y,z}, M_s | Kittel stiffnesses/frequency, demagnetising factors, saturation magnetisation | (B2.5.3) |
| F_M, F^{mag}_S | neutron magnetic form factor (spin + orbital); spin-only form factor | (B2.6.1) |
| S_n, γ_n, N_f, Ω_c, T_d | 2504.02927 neutron quantities (source notation); data temperature | §6 |
| L^{ph}_{Qν}, 𝐌^{ph}(q), 𝐣(q) | phonon angular momentum (not ℓ_Q); Born-charge orbital moment; ionic current Σ(eZ*/M)Pe^{iq·R} | §7 |
| D_ZFS, ω_Z, 𝓃_mol, p_m | SMM zero-field splitting, Zeeman energy, molecule density, level populations | (B2.7.2) |
| κ_URF | URF chiral-detection branching (source κ is not κ_mix) | §7 |
| c̃, c̃_κ, r_c | coupling per unit mass; core radius | §8 |
| Y_CC, p_q, f_opt, ⟨N_x⟩, p_FH | colour-centre yield factors | (B2.9.1) |
| S_CM, S_int, S^{diss}, p_esc, ΔE_B | molecular structure factors; cage escape; bond energy | (B2.10.1) |

---
## Interface flags
| # | Owner / user | Quantity | This return | Action |
|---|---|---|---|---|
| IF-B2-1 | LIMITS, WP3-v3 §4, WP2-v3 §4 | single-phonon absorption | (B2.1.1)–(B2.1.4); electron-scalar LO residue Z − Z*/ε_∞ | add B2-L1; WP2 cross-reference |
| IF-B2-2 | CONVENTIONS §11, WP6 library | glass reference | metadata `ref=glass` | coordinator |
| IF-B2-3 | CONVENTIONS §11, WP2-v3 §6, L18 | anharmonic order, quantum crystals | `nA=SCHA` (resummation) + cumulant increments, type T | coordinator; WP2 |
| IF-B2-4 | WP2-v3 §12 gap 6 | amorphous S | closed for S_self and S_dist n_ph = 1; n_ph ≥ 2 sketch | WP2 cites |
| IF-B2-5 | WP4-v3 §2, L13 | uniform-mode spin weight | Larmor statement (cited), Polder factor, λ_S rules | WP4 cites |
| IF-B2-6 | WP5-v3, WP7-E | SMM avalanche, chiral-band collection | detector-response functions outside S; metastable-well line | WP5 / WP7-E |
| IF-B2-7 | WP5-v3 §4 | ER colour-centre channel | (B2.9.1)(b); aggregates f_opt ≈ 0 at sub-GeV | WP5 |
| IF-B2-8 | WP3-v3 §2, §4; WP0 §6.2(ii) | Migdal-type absorption | crystal identity (B2.8.1)–(B2.8.2); medium factor +1.2×10⁻³ at 1 keV | WP3 cites |
| IF-B2-9 | SOTA literature list | source items | misprints 2308.06314 Eq. (48), 2601.01043 Eq. (12); 2512.16451 Born validity; 2601.01043 n_r/\|ε\|²; 2301.07617 selection rule. Retracted: rigid-ion "defect", κ | coordinator |
| IF-B2-10 | CONVENTIONS §11, WP6 | data-driven spin S | metadata `src=data` (not an 𝒳 value) | coordinator |
| IF-B2-11 | WP4-v3 §8, OW0-17 | spin-ordered absorption targets | outside Theorem D GS; LSWT + magnon–phonon hybrids | WP4 / WP0 |
| IF-B2-13 | CONVENTIONS §11 | elastic (n_ph = 0) kinematic regime | proposed `K=el` (§3) | coordinator |
| IF-B2-12 | WP6, LIMITS | B−L in Si | isotope one-phonon term + EM-like two-phonon term, additive (B2.4.1)–(B2.4.2) | WP6 library key |

---
## Proposed LIMITS rows
Provisional labels B2-L1…B2-L10 (numbers assigned by the coordinator).
| # | τ / chain (URF) | Source formula [FT] | Status |
|---|---|---|---|
| B2-L1 (A4) | (3.5)–(3.6), GS, n_A = 0, K = 1ph-coh, k → 0, (B2.1.1)–(B2.1.4); T metadata | 2308.06314 Eqs. (2), (7), (14), (16), (40)–(44), Table 1; 1712.06598 Eqs. (2)–(3) | DERIVED ✔ (Eq. (44) CONFIRMED) ✎ (electron row: applies 2308.06314 fn. 2 at the LO residue, Z − Z*/ε_∞; Eq. (48) square) |
| B2-L2 (S5) | (3.5), tr J_κ row, unpolarised spins, (B2.2.1)–(B2.2.2), K = 1ph-inc | 2411.10542 Eqs. (25)–(31) | DERIVED ✔; leading correction O(ΔM/M) vertex–eigenvector correlation |
| B2-L3 (A7) | L9b with the glass ε (B2.3.1); `ref=glass` | 2603.22390 Eq. (2) (Eq. (3) crystalline truncation) | DERIVED ✔; low-ω C^{IR} = A + Bω² (cond-mat/0604205) |
| B2-L4 (§10(iii)) | (3.3), n_N row, n_ph = 0 of (B2.2.4), configurational average | 2512.16451 Eqs. (2), (9)–(12), (14) | ✎ Born plane wave on the medium valid for V_opt/E_kin ≪ 1 over f(v), i.e. σ_χN ≪ σ_crit = m_χ⁴v⁴/(4πn₀²) (μ_χN ≈ m_χ); below it the bulk phase drops out in DWBA (k → k′), leaving O(V_opt/E_kin) plus surface refraction; above it the force is reflection/refraction-dominated |
| B2-L5 (L11) | S^{GS}_κκ, (B2.4.1) SCHA; QH limit | 2409.02439 Eqs. (2), (4)–(5) | DERIVED ✔ (QH limit) + SCHA correction |
| B2-L6 (S2) | (3.5), spin row, k → 0; Larmor statement (cited), Polder (B2.5.3) | 2005.10256 Eq. (27); 2001.10666 Eqs. (25)–(27), (35) | DERIVED ✔; λ_S = g_J − 1 only for J multiplets |
| B2-L7 (S6) | data-driven S_{ss} (B2.6.1)–(B2.6.2) | 2504.02927 Eqs. (8), (11), (15), (17), (26) | DERIVED ✔ + caveats (P_T only; quenched-ion bracket [1/(g/2)]²) |
| B2-L8 (L9/S8) | Λ-resolved one-phonon S (density, j_T); (B2.7.1) two-phonon readout; κ_URF; (B2.7.2) both branches | 2301.07617 Eqs. (6)–(7); 2511.20461 Eqs. (3)–(4), (11)–(12); 2601.01043 Eqs. (3), (9)–(13), (17)–(18) | ✎ (decay selection rule not exact; 2601.01043 Eq. (12) square, n_r/\|ε\|²; metastable line) |
| B2-L9 (X10) | (3.5), n_κ rows, X sector, WP0 (4.8): (B2.8.1)–(B2.8.2) | 2312.10566 Eqs. (13)–(17) | DERIVED ✔; medium factor 1 + (3/2)ω_p²/ω² (≈ 10⁻³ at 1 keV in Si) |
| B2-L10 (D2/D5) | (7.3) seeding with Y_CC (B2.9.1); (B2.10.1) | 1705.03016 Eqs. (1)–(2), (5)–(7); 1608.02940 Eqs. (4), (12), (23), (25) | ✔ limits; ✎ refinements (smooth threshold, survival, charge state, aggregates; bound CM, cage) the sources partly anticipate |

---
## R12 clean-up (coordinator; VER-WP7-B2-A, VER-WP7-B2-B; edited in place)
| Item | Source | Status | Where |
|---|---|---|---|
| Two-phonon comparison redone at 50 meV (α ≈ 0.55 cm⁻¹, Im(−1/ε) ≈ 5×10⁻⁶, ratio ~6×10³ at 293 K, larger at mK); Deinzer & Strauch (2004) cited [FT via VER-A]; "unverified" caveat removed | VER-WP7-B2-A | applied | §0 row 3, §2.4, §11 item 2, §12; C27 |
| Elastic τ label `K=1ph-coh` → proposed `K=el` | VER-WP7-B2-B N1 | applied | §3, IF-B2-13 |
| §8 `nB=-` justified (BO-order-free identities) | VER-WP7-B2-B N1 | applied | §8 |
| checks.py docstring "C21–C30" → "C21–C28" | VER-WP7-B2-B N2 | applied | code/WP7-B2-v2/checks.py |
Checks re-run: 39/39 PASS.
