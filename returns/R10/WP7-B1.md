# R10 / WP7-B1: electronic, low-dimensional and molecular channels as explicit URF sectors (E5, E8, E9, E10, E12, X6, X8, A2, A6, I3, I5)

Theory agent, brief R10/WP7-B1. Architecture: returns/R8/WP0-v3.md (cited "WP0 (n)"; not re-derived). Neighbours: WP1-v3, WP3-v3, WP4-v3, WP6-v3
(read through state/CORRECTIONS.md; no owed correction there touches the sites quoted here). Conventions: CONVENTIONS.md; symbols: NOTATION v4 + R9 rows,
new symbols in §15. Tags: [D] derived (hypotheses stated), [D, sketch], [E], [C]; literature [FT] / [ABS] / [UNVERIFIED].
Checks: `code/WP7-B1/checks.py`, **28/28 PASS, ≈ 10 s** (sympy exact; mpmath/scipy quadrature in C6a, C9b, C10), cited WP7B1-Cn.
Literature: every arXiv ID below was verified against the arXiv API (id_list query, titles and authors) in this session; the 20 papers marked [FT] were
fetched with lit.py into literature/papers-WP7-B1/ and read in the HTML full text (PDFs deleted at the end). Status of everything new: CLAIMED.

---
## 0. Results at a glance
| Item | Truncation of WP0-v3 | Main result | Literature limit [FT] | New finding |
|---|---|---|---|---|
| E5 Frenkel | n_e row, X0 (+Condon X+), 𝒳 = BSE in a molecular basis, zero intermolecular overlap | (E5.2) exciton-coherent S; binned = incoherent molecule sum exactly (C1a) | 1912.02822 (11),(13),(16)–(19); 2103.08601 (8),(9) | incoherent sum is exact for bins ≫ Davydov splitting (unitarity) |
| E8 low-dim/exotic plasmons | n_e row, X0, d = 1, 2, RPA (exact for linear 1D bands), multi-component RPA | (E8.1) 1D, (E8.2) 2D, (E8.3) demon weight (q²/(q²+k_TF²))² | 2607.15338 (3)–(6); 2312.00866 (13)–(19); 2507.07164 (1)–(3) | f-sum forces g_LL v_LL = v_F (C2a,d); neutral demon invisible at q ≪ k_TF (C3) |
| E9 heterostructures | n_e row, RPA with G_z local fields (sheets) or local ε_A,B (thick layers) | (E9.1) layered-sheet stack, exact q_z dependence; (E9.3) Rytov | 2110.01587 (16) | their (16) is the exact kL → 0 EMT at any filling (C4c) |
| E10 quantum dots | WP4 [6.1] with the dot as the centre; EFA; dielectric confinement | (E10.1)–(E10.3); multipole local field (C5) | 2208.05967 (6),(10)–(12),(16) | absorption local-field factor 9\|ε_in\|²/\|ε_in+2ε_out\|² (≈ ×6 for PbS in solvent [E]) |
| E12 graphene/CNT | 2D/1D Dirac + substrate V_2D + Keldysh background, RPA; vacuum-ejection IP limit | (E12.1) closed-form sheet S | 1606.08849 (5),(7); 2312.00866 (13)–(19) | substrate enters only through V_2D (C6b) |
| X6 Wannier/brems Migdal | WP3 (W.5) T0–T5(imp), valence; Wannier: rigid-WF following (H_W) | both pictures are truncations of (W.5) | 2011.13352 (1),(7),(11),(12) (C7); 1912.13484 (2.7)–(2.8) | Wannier picture ⇔ (H_W); its drag mass is N_e^W m_e |
| X8 bound Migdal | (W.5) with ω_e on bound (exciton/atomic) lines | (X8.1)–(X8.2) | 2604.26773 (1),(6) | C8 exact hydrogenic 1s→2p |
| A2 SC/metal absorption | WP0 (3.5), sector (2,1) of WP4 Theorem D-g, n_g = 2 | (A2.1) Allen–Holstein; (A2.2) SC: 𝔤_I (case I), not MB | 1604.06800 (8),(13),(16),(17),(19),(20) (C9) | 1604.06800 (17) = x 𝔤_I exactly (Landen, C9b) |
| A6 dopant absorption | WP0 (3.5)–(3.6) at k → 0 + WP4 [6.1] | (A6.1)–(A6.2) | 2212.04504 (9),(10),(12) | their (12) misprints 3q̃ for 3q̃² (C10); missing Lyman lines |
| I3 inelastic DM–e | WP0 (2.1) Δ_χ ≠ 0, S unchanged | (I3.1); exothermic shell (I3.2), light-mediator edge (I3.3) | 2203.06664 (11),(16),(20) | shell rate halo-independent to O(v²/v_Δ*²) (C11) |
| I5 boosted / reflected | relativistic DM-side 𝔇, NR target rows | (I5.1) density row with (1 − ω²/q²); transverse row | 2401.11971 (4)–(6); 2607.09352 (9)–(11) | 2401.11971 (5) lacks (1 − ω²/q²)² (C12c) |

---
## 1. Two embedding lemmas used throughout [D]
**(1.1) Low-dimensional units.** Hypotheses: electrons confined to identical units of dimension d ∈ {1, 2} (wires along ẑ, sheets ⊥ ẑ) with a
q-independent transverse profile (form factor F_⊥(q_⊥) = ∫d^{3−d}r_⊥ e^{iq_⊥·r_⊥}ϱ_⊥(r_⊥), ϱ_⊥ normalised); no inter-unit tunnelling; inter-unit Coulomb
coupling either negligible (q_⊥d_u ≫ 1, d_u the unit spacing) or restored by (E9.1). Then the unreduced-q response (WP0 (3.1)) is
  S(q,ω) = 𝓃_u |F_⊥(q_⊥)|² S_d(q_∥,ω),   𝓃_u = units per unit (3 − d)-dimensional transverse measure,                                    (1.1)
with S_d the d-dimensional response normalised as (3.1) per unit d-volume. Proof: n_e(q) = Σ_u e^{iq_⊥·r_u}F_⊥(q_⊥)n_d,u(q_∥); cross-unit terms
average to zero for uncorrelated units. The rate is WP0 (3.4) with ρ_T → the unit mass per d-volume (2607.15338 reports per tube length, 2312.00866 per area).
**(1.2) Finite centres in a host** = WP4-v3 [6.1] (dilute, host-screened, retarded out-state weight (ε^{-1}_host)_{G0}); used for E10 and A6.

---
## 2. E5: Frenkel excitons in organic and molecular crystals
**Truncation chain.** WP0 (3.3) with the n_e row (spin rows for triplets) → sector X0 at n_B = 0, n_g = 0 (Condon; the vibronic X+ progression is
re-added in (E5.3)) → 𝒳 = BSE (WP1-v3 [E7]) written in a localised molecular-orbital basis → Frenkel limit: intermolecular orbital overlap → 0,
which deletes charge-transfer pairs and the intermolecular direct W^{scr} terms and keeps the intermolecular BSE **exchange** term (Coulomb coupling of
molecular transition densities). τ: `nB=0|ng=0|nA=0|X=BSE|nT=0|K=-|Mg=-|nD=-`, ref = normal, scr = ext, LFE.
**(E5.1) Frenkel Hamiltonian [D, given the Frenkel limit].** Molecules 𝔬 = 1…N_mol per cell at r_𝔬 with orientation 𝖱_𝔬; singlet transitions 0 → 𝔵 with
energies E_𝔵 and form factors f^{(𝔬)}_{0𝔵}(q) ≡ ⟨𝔵|Σ_{i∈𝔬}e^{iq·(r_i−r_𝔬)}|0⟩ = f_{0𝔵}(𝖱_𝔬^{-1}q) (singlet √2 included, as in 1912.02822 Eq. (10)). At
exciton momentum Q = q_r,
  H^F_{𝔬𝔵,𝔬′𝔵′}(Q) = E_𝔵δ_{𝔬𝔬′}δ_{𝔵𝔵′} + 𝔍^F_{𝔬𝔵,𝔬′𝔵′}(Q),  𝔍^F(Q) = Σ′_R e^{iQ·R}∫∫ρ^{(𝔬)}_{0𝔵}(r)* v_C(r − r′ − R) ρ^{(𝔬′)}_{0𝔵′}(r′),          (E5.1)
with eigenvectors A^{F,λ}_{𝔬𝔵}(Q), energies E_λ(Q); the G = 0 (macroscopic) part of 𝔍^F is removed, because WP0 (5.1) puts that Coulomb line in ε (the
L–T split of the Davydov components is then produced by (ε^{-1})_{00}).
**(E5.2) Response [D].** With the out-state weights of WP0 (7.2), w_{𝔬𝔵}(q) ≡ e^{iq·r_𝔬}Σ_G(ε̃^{-1})_{G0}(q,ω) f^{(𝔬)}_{0𝔵}(q+G) → e^{iq·r_𝔬}f^{(𝔬)}_{0𝔵}(q) for qa ≫ 1:
  S^F(q,ω) = (2π/Ω) Σ_λ |Σ_{𝔬𝔵} A^{F,λ}_{𝔬𝔵}(q_r)* w_{𝔬𝔵}(q)|² δ(ω − E_λ(q_r)).                                                         (E5.2)
*Binning theorem [D] (WP7B1-C1a, C1a′).* A^F(Q) is unitary, so for any ω bin containing every λ of the manifold that the w_{𝔬𝔵} feed (bin ≫ exciton
bandwidth + Davydov splitting, and 𝔍^F ≪ E_𝔵 − E_𝔵′ between manifolds):
  ∫_bin S^F dω = (2π/Ω) Σ_{𝔬𝔵∈bin} |w_{𝔬𝔵}(q)|²   (exactly, interference terms cancel).                                                   (E5.2′)
This is the incoherent molecule sum used by 2103.08601 ("we treat the scattering as incoherent between different molecules"); the theorem shows it
is exact in bins, not an approximation that needs q ≫ 1/a, and that coherence shows only at resolution ≲ 𝔍^F.
**(E5.3) Vibronic dressing [D, Condon].** Each line E_𝔵 becomes the Huang–Rhys progression of WP4-v3 [6.3] (X0 weight e^{−S_HR,𝔵}, rest X+); the
ω-integrated weight is unchanged (FC completeness), so (E5.2′) is the Condon-integrated sum (CONVENTIONS §10 DW = FC only).
**Literature limit.** 1912.02822 [FT]: Eq. (11) (σv)_{i→j} = ∫d³q/(2π)³ 2πδ(ΔE_ij − ω)|ℳ_free|²|f_ij(q)|²/(16m_χ²m_e²), Eq. (13) |ℳ_free|²/(16m_χ²m_e²) ≡
πσ̄_eF_DM²/μ_χe², Eq. (19) R = ξN_Bρ_χσ̄_e/(8πm_χμ_χe²)Σ∫(d³q/q)η(v_min^{ij})F_DM²|f_ij|². From (E5.2′) with one molecule (𝓃_mol S = 2π𝓃_molΣ|f|²δ), WP0 (3.3)
and isotropic η: prefactor π·2π/((2π)³·2) = 1/(8π) and 𝒢 = η/2q (C1b, C1c) give Eq. (19) exactly (ξ = detection efficiency, a WP5 factor). 2103.08601 [FT]
Eq. (8) (d³q/4π, same factor, C1b) with Eq. (9) (f_{g→s_n} = √2Σd^{(n)}_{ij}⟨Ψ_j|e^{iq·r}|Ψ_i⟩) and the sum over four rotated molecules = (E5.2′).
Source conventions: both write ω = q²/2m_χ − q·v (opposite sign of q, immaterial for |f|²); 1912.02822 uses an isotropic speed distribution.
**Leading corrections.** (i) Exciton dispersion/Davydov splitting: line positions move by ~𝔍^F (small in t-stilbene per the source; 10–100 meV in
acenes [E]); visible only in bins ≲ 𝔍^F. (ii) Screening for q ≲ 1/a_mol: (ε̃^{-1})_{G0} (Lorentz-type local field of the molecular crystal) [E: tens of %
at q ≲ 1 keV]. (iii) Charge-transfer excitons (overlap ≠ 0): beyond Frenkel. (iv) Triplets: zero in S_nn; reachable through s_e rows (WP1-v3 §3.2(a)).
(v) Hückel/PPP orbitals vs TDDFT/GW-BSE molecular states: form-factor error not quantified [C]. (vi) Ionisation continuum (neglected by 1912.02822).
**Computation specification.** Inputs: crystal structure (CSD), molecular geometry, molecular excited states (TDDFT or GW-BSE: PySCF/ORCA/Q-Chem for the
molecule; BerkeleyGW or Yambo periodic BSE for the crystal, ~10² atoms/cell). New module `frenkel-ff`: transition densities on a real-space grid
(Δr ≤ π/q_max ≈ 0.4 a₀ for q_max = 30 keV), FFT to f_{0𝔵}(q); 𝔍^F(Q) by Ewald with G = 0 removed; diagonalise (E5.1); tabulate (E5.2) on |q| ∈ [0, 30] keV ×
590 Lebedev directions. Convergence: per-molecule partial f-sum to 2%; |f|² at q = αm_e to 5% against basis; ~30 states up to 10 eV. Cost: molecule
minutes; periodic BSE 10³–10⁴ CPU-h; tables ~10 CPU-h. Outputs: ΩS(q,ω) with τ string; per-orientation tables (daily modulation); S_HR,𝔵 and Λ = (𝔬, 𝔵)
seeds for the WP5 scintillation yield (radiative efficiency is a WP5 input, not part of S).

---
## 3. E8: exotic and low-dimensional plasmons
**Truncation chain (common).** WP0 (3.3) n_e row → X0, n_B = 0 → (1.1) with d = 1 or 2 → 𝒳 = RPA on the projected low-energy bands (WP4-v3 §5.2 steps
3–5 analogue: remote bands as background). τ: `X=RPA`, ref = normal (CDW: ref = CDW, §3(d)).
**(a) 1D Luttinger modes (metallic nanotubes) [D].** Hypotheses: N_ch linear channels (CNT: N_ch = 4, spin × valley) with velocity v_F; only forward
density–density scattering (g₂ = g₄ = v_C^{1D}; backscattering and umklapp dropped); T = 0. The linear 1D bubble is R⁰ = N_ch v_Fq²/(π(ω² − v_F²q²)) and
  S_wire(q_∥,ω) = N_ch g_LL(q_∥) |q_∥| δ(ω − v_LL|q_∥|),  v_LL = v_F/g_LL,  g_LL = [1 + N_ch v_C^{1D}(q_∥)/(πv_F)]^{-1/2},                       (E8.1)
v_C^{1D}(q_∥) = 2αI₀(q_∥r_t)K₀(q_∥r_t)/ε_env for a cylindrical shell of radius r_t [D, sketch] (→ 2α ln(2/q_∥r_t) − 2αγ_E as q_∥r_t → 0). Pole and residue: C2b, C2c.
Embedding: S(q,ω) = 𝓃_t|J₀(q_⊥r_t)|²S_wire(q_∥,ω) by (1.1) (m = 0 azimuthal harmonic; m ≠ 0 are inter-subband). **f-sum constraint [D]:** WP0 (4.6)
projected on linear bands (Schwinger term) gives ∫ωS_wire dω = N_ch v_Fq²; (E8.1) saturates it iff g_LL v_LL = v_F (C2d), which holds for every
density–density interaction (C2a). A phenomenological (g, v) pair with gv ≠ v_F violates (4.6).
*Literature limit.* 2607.15338 [FT] Eq. (3) (g = √((2πv_F + g₄ − g₂)/(2πv_F + g₄ + g₂)), v = √((v_F + g₄/2π)² − (g₂/2π)²)), Eq. (4) S_1D = g|q|δ(ω − v|q|),
Eqs. (5)–(6) rate per tube length with |F_⊥|². (E8.1) at N_ch = 1, g₂ = g₄ = v_C^{1D} reproduces Eqs. (3)–(4) exactly (C2a–c): RPA coincides with their
bosonised result for this model; their stated group velocity v_g = v_F/g [FT] is the f-sum condition. Leading corrections: inter-tube Coulomb in a forest
(lattice-of-wires version of (E9.1)) when q_⊥d_t ≲ 1; band curvature and subbands at ω ~ v_F/r_t; backscattering g₁; plasmon damping (contacts, disorder).
**(b) 2D sheet plasmons [D].** Sheet between media ε₁, ε₂: v_C^{2D}(q_∥) = e²/(q_∥(ε₁ + ε₂)) (image solution, C6b); S_sheet = −2Im[R̃^{2D}/(1 − v_C^{2D}R̃^{2D})]
(T = 0); for a parabolic gas R̃^{2D} → 𝓃_{2D}q²/(m*ω²) gives ω_pl² = e²𝓃_{2D}q_∥/(m*(ε₁ + ε₂)) (C6c). *Literature limit:* 2312.00866 [FT] Eqs. (13)–(14)
S = (1/d)S_2D sinc²(q_zd/2), Eq. (17) 1/ε = 1 + v_Cχ_2D with v_C = e²/(2ε_rq), ε_r = 1, Eqs. (18)–(19) RPA: = (E8.2) at ε₁ = ε₂ = 1:
  S_sheet(q_∥,ω) = −2 Im R̃^{2D}_{low}(q_∥,ω) / |1 + r_K q_∥ − v_C^{2D}(q_∥)R̃^{2D}_{low}(q_∥,ω)|²,                                             (E8.2)
where r_Kq_∥ ≡ −v_C^{2D}R̃^{2D}_{bg} is the static remote-band (Keldysh) term and R̃_low the projected bands [D: algebra as WP4-v3 [5.1], Im R = Im R̃_low/|D|²].
Leading correction to 2312.00866: a SiO₂ substrate halves v_C^{2D} up to (1 + ε_sub)/2 ≈ 2.4 [E], and r_K ≠ 0.
**(c) Demons / acoustic plasmons [D].** Two carrier species, light (static screening k_TF,1, valid for ω ≪ q v_F,1) and heavy (dynamic, ω ≫ q v_F,2):
ε = ε_bg + k_TF,1²/q² − ω_{p,2}²/ω² (ε_bg = 1 below). The acoustic zero ω_a = ω_{p,2}q/(q² + k_TF,1²)^{1/2} carries a share
  w_a(q) = (q²/(q² + k_TF,1²))²                                                                                                          (E8.3)
of the heavy component's f-sum in L (C3a,b). A density probe (DM couples to all electrons with one sign) sees the Pines demon only at O(q⁴/k_TF⁴):
it is neutral at q → 0. *Literature limit:* 2507.07164 [FT] Eqs. (1)–(2) Γ(v) = ∫d³q/(2π)³|ℱ|²(q²/2πα)𝒲, Eq. (3) Γ_abs = κ²m_χ𝒲 (L0/L9b form): the
ab initio ELF contains (E8.3) automatically; (E8.3) is its two-component RPA limit and explains why acoustic features add little at q ≪ k_TF.
**(d) CDW plasmons [D for the structure; gap for the collective modes].** The low-energy "CDW plasmon" of TiSe₂ (2507.07164) is the intraband plasmon of
the reconstructed pockets: RPA+LFE on the CDW supercell reference, no new formula. The phason/amplitudon need a conserving response on the
broken-symmetry reference (as BCS needs GRPA, WP4-v3 [4.1]) and, for a Peierls CDW, the coupled electron–lattice mode: exact remaining gap §13 (G-E8).
**Computation specification (a–c).** Inputs: TB/DFT (Wannier90) bands of the tube or sheet; environment ε(ω) (substrate polar phonons); geometry
(r_t, spacing). New module `lowd-rpa`: d = 1, 2 RPA with arbitrary v_C^{(d)}(q), inter-unit lattice sums, F_⊥; grids q_∥ ∈ [10⁻⁴, 10] keV log (200 pts),
ω to v_F/r_t (1D) or 2 eV (2D) with ≥ 2000 pts; convergence f-sum (C2d) to 10⁻³; cost < 1 CPU-h (plus 10²–10³ CPU-h DFT bubbles for real sheets).
Outputs: S(q_∥, q_⊥, ω) tables (directional), w_a(q).

---
## 4. E9: heterostructures and layered stacks
**Truncation chain.** n_e row → X0 (or ionic layers through ε_i(ω)) → RPA with the **G_z local fields of the stacking axis kept** (DM q_z is unreduced;
the superlattice G_z = 2πn/a_s couple q_z to q_z + G_z) → locality hypotheses below.
**(E9.1) Stack of thin sheets [D].** Hypotheses: sheets of thickness ≪ 1/q, period a_s, no interlayer tunnelling, sheet-local proper response R̃^{2D},
uniform background ε_b between sheets. The sheet form factor is 1 for every G_z, so R̃_{G_zG_z′} = R̃^{2D}/a_s is rank one and the Dyson equation WP0 (5.1)
closes:
  S(q,ω) = −(2/a_s)(1 − e^{−βω})^{-1} Im[R̃^{2D}/(1 − v_C^{L}R̃^{2D})],   v_C^{L}(q_∥,q_z) = (1/a_s)Σ_{G_z}v_C(q+G_z)/ε_b = (e²/2ε_bq_∥) sinh(q_∥a_s)/(cosh(q_∥a_s) − cos(q_za_s))   (E9.1)
(lattice sum C4a). Limits (C4b): a_s → ∞ gives the isolated sheet (E8.2); q_∥a_s, q_za_s ≪ 1 give 3D jellium with 𝓃 = 𝓃_{2D}/a_s. The q_z dependence is the
band of layer plasmons, a q_z-periodic structure invisible to any local effective medium. **Finite stack (N_lay sheets) [D]:** replace by the layer
matrix v_{ll′} = (e²/2ε_bq_∥)e^{−q_∥|l−l′|a_s} and S per area = −2Im Σ_{ll′}e^{−iq_z(l−l′)a_s}[R̃^{2D}(1 − vR̃^{2D})^{-1}]_{ll′}, times |F_z(q_z)|². N_lay = 1 in vacuum
is the thin-film case of WP4-v3 [4.5] with its image term now [D] (flag IF-B1-2).
**(E9.2) Thick layers with local ε_A(ω), ε_B(ω), filling f_fill [D].** For ka_s ≪ 1 the stack is the uniaxial medium ε_∥ = f_fillε_A + (1 − f_fill)ε_B,
ε_⊥^{-1} = f_fill/ε_A + (1 − f_fill)/ε_B, and L = Im[−1/(k̂·ε_eff·k̂)].
**(E9.3) Beyond ka_s ≪ 1 [D].** Transfer matrices of (φ, εφ′) give the collective-mode condition cos(q_⊥a_s) = cosh(k_∥d_A)cosh(k_∥d_B) +
½(ε_A/ε_B + ε_B/ε_A)sinh(k_∥d_A)sinh(k_∥d_B) (Rytov form), whose k → 0 limit is ε_∥k_∥² + ε_⊥q_⊥² = 0 (C4d); poles of L lie on it.
**Literature limit.** 2110.01587 [FT] Eq. (16): ε_L^{-1} ≃ ((1 − d/L)ε₁ + (d/L)ε₂)/(ε₁ε₂ + (1 − d/L)(d/L)(ε₁ − ε₂)²k_z²/k²), stated "in the d/L ≪ 1 limit". (E9.2)
equals it identically for every d/L (C4c): it is the exact long-wavelength EMT, valid for ka_s ≪ 1 at any filling. (Their k_z is in-plane, layers ⊥ x.)
Leading correction: O((ka_s)²) from (E9.3); dielectric non-locality ε_i(k) when k ≳ 1/d_i (their own remark at m_χ ≳ MeV); interface states.
2603.15581 [FT] gives no rate formula; its "dispersion filter" (carrier transfer to the other layer only for the right (q,ω)) is the Λ-resolved response
WP0 (7.1)–(7.2) with Λ = (layer of electron, layer of hole) [D as definition]; a layer-resolved pair weight needs layer-projected Bloch states.
**Computation specification.** Inputs: monolayer R̃^{2D}(q_∥,ω) (Yambo with 2D Coulomb cutoff, or Wannier bubble), interlayer spacing, ε_b(ω) (hBN etc.),
ε_i(q,ω) for thick layers (GPAW/Yambo). Codes: `lowd-rpa` (stack mode: closed form (E9.1) and N_lay × N_lay matrix), transfer-matrix solver for (E9.3).
Grids: q_∥ ∈ [10⁻⁴, 10] keV, q_z unreduced to q_max with ≥ 64 points per 2π/a_s. Convergence: per-layer f-sum; finite N_lay → (E9.1) to 1% (N_lay ≈ 50).
Cost: minutes (model) to 10³ CPU-h (DFT bubbles). Outputs: S(q_∥,q_z,ω) (directional), Λ-resolved layer tables.

---
## 5. E10: quantum dots (finite systems in a matrix)
**Truncation chain.** (1.2) with the dot as centre: dilute dots (volume fraction ϕ_QD = 𝓃_QD(4π/3)R_QD³ ≪ 1, no inter-dot transfer) → X0 + vibronic X+ →
𝒳: envelope-function approximation (EFA) for the confined levels, RPA dielectric confinement for screening; strong confinement R_QD ≪ a_x (electron
and hole uncorrelated up to O(R_QD/a_x) Coulomb shifts).
**(E10.1) Response [D].** S^{QD}(q,ω) = 𝓃_QD Σ_f 2π|⟨f|ñ_e(q)|0⟩|²δ(ω − E_f + E_0), spin factor 2 at SOC = 0, with EFA matrix elements
⟨c,ψ^e_{nℓm}|e^{iq·r}|v,ψ^h_{n′ℓ′m′}⟩ ≃ ρ_cv^{cell}(q)⟨ψ^e|e^{iq·r}|ψ^h⟩ (q ≪ 1/a_lat; ρ_cv^{cell} the band-edge Bloch form factor) and
E_f = E_g + ε^e_{nℓ} + ε^h_{n′ℓ′} − O(α/(ε_inR_QD)) [E for the Coulomb shift].
**(E10.2) Dielectric confinement [D] (C5).** For qR_QD ≪ 1 each multipole of the DM vertex, e^{iq·r} = 4πΣi^ℓj_ℓ(qr)Y*_ℓm(q̂)Y_ℓm(r̂), acts inside the dot with
  ñ_e: j_ℓY_ℓm → 𝔣^{loc}_ℓ j_ℓY_ℓm/ε_out,   𝔣^{loc}_ℓ = (2ℓ + 1)ε_out/(ℓε_in + (ℓ + 1)ε_out)                                                (E10.2)
(quasi-static, local ε_in, ε_out; the total inside potential is φ_ext(2ℓ+1)/(ℓε_in + (ℓ+1)ε_out)); ℓ = 1 gives 3/(ε_in + 2ε_out); ℓ = 0 is screened by
ε_out only. For qR_QD ≫ 1 the weights tend to the bulk (ε̃^{-1}_in)_{G0}.
**(E10.3) Bulk limit and absorption [D].** When the level spacing ≪ bin and qR_QD ≫ 1, Σ_f → bulk joint DOS: S^{QD} → ϕ_QD S^{bulk}(q,ω; E_g → E_g^{QD}) (scissor).
For absorption (k_φR_QD ≪ 1) the dilute Maxwell–Garnett medium gives Γ_abs = κ_mix²m_φ Im[−1/ε_eff], with the dot part
  Im[−1/ε_eff] ⊃ 9ϕ_QD Im ε_in/|ε_in + 2ε_out|²   (ε_out real),                                                                               (E10.3)
from ε_eff = ε_out(1 + 3ϕβ/(1 − ϕβ)), β = (ε_in − ε_out)/(ε_in + 2ε_out) (the ℓ = 1 case of (E10.2)).
**Literature limit.** 2208.05967 [FT] Eq. (6) dR/dlnE_r = N_tρ_χσ̄_e/(8m_χμ_eχ)∫q dq η F_DM²|f_QD|², Eqs. (10)–(12) (bulk QE-dark form factor with the gap
scissored to ΔE_QD) = the bulk limit of (E10.3) with N_t ↔ ϕ_QD (dictionary WP1-v3 [E12]); valid where they use it: for ω ≥ 2.5 eV, q ≥ ω/v_max ≈ 0.9 keV,
qR_QD ≳ 8 for d = 3.3 nm [E]. Their absorption Eq. (16) σ_A′v = κ²σ_A/|ε|² uses bulk PbS σ_A and ε ("measured for bulk PbS"): for dots in solvent
(E10.3) differs by the factor 9|ε_in|²/|ε_in + 2ε_out|² [D], ≈ 6 for ε_in ≈ 17 (PbS near 1 eV) and ε_out ≈ 2 [E inputs]: their dark-photon reach is
conservative by about this factor in the quasi-static regime. Leading corrections: confinement O(1/qR_QD) [E]; ligand/surface states; size dispersion
(E_g^{QD} spread; their Eq. (11)); exciton correlation when R_QD ≳ a_x.
**Computation specification.** Inputs: dot size distribution, bulk bands (QE) and k·p masses; ε_in(ω) (bulk or size-corrected), ε_out (solvent).
Codes: EFA spherical-well solver (j_ℓ roots, ℓ ≤ 20, n ≤ 10) for E_f and ⟨ψ^e|e^{iq·r}|ψ^h⟩ by radial quadrature; QE-dark/QCDark2 bulk tables above
2.5 eV; atomistic check by tight binding or DFT on ≤ 2000-atom clusters. Convergence: discrete → bulk crossover (bin 50 meV) to 5%; f-sum of the dot.
Cost: EFA negligible; clusters 10⁴ CPU-h. Outputs: S^{QD}(q,ω) (discrete + bulk), absorption with (E10.3), Λ = (e, h envelopes) seeds for WP5 (MEG).

---
## 6. E12: graphene and carbon nanotubes
**Truncation chain.** n_e row → X0, n_B = 0 → (1.1) d = 2 (sheet) or d = 1 (tube) → low energies: massless (or gated, gapped) Dirac k·p within Λ_D,
remote σ bands as the static Keldysh term, substrate through v_C^{2D} (the 2D analogue of WP4-v3 [5.1], L16) → 𝒳 = RPA. High energies (vacuum
ejection): IP with a vacuum-continuum final-state projector (WP0 (7.1)).
**(E12.1) Undoped sheet on a substrate [D].** Im R̃_D = −(g_deg/16)q_∥²/√𝓈 Θ(𝓈), 𝓈 = ω² − v_F²q_∥² (C6a, quadrature to 10⁻⁷; Re R̃_D = 0 for 𝓈 > 0 as the
continuation of the same analytic function, [D, sketch]). Inserting in (E8.2):
  S_sheet(q_∥,ω) = (g_deg/8)(q_∥²/√𝓈) / [(1 + r_Kq_∥)² + (παg_deg q_∥/(4(ε₁ + ε₂)√𝓈))²],   ω > v_Fq_∥,                                        (E12.1)
and S(q,ω) = |F_z(q_z)|²S_sheet per area (1.1), F_z the out-of-plane π-density form factor. Directionality: S depends on q_∥ and q_z separately, so the
rate modulates daily with the angle between the DM wind and the sheet normal [D]. CNTs: (E8.1) (metallic) or the 1D massive-Dirac interband bubble
(semiconducting; gap §13).
**(E12.2) Vacuum ejection [D, IP].** S(q,ω;Λ = vac) = 2(2π/V)Σ_{iℓ,k_f}|⟨k_f|e^{iq·r}|ψ_{iℓ}⟩|²δ(ω − k_f²/2m_e − Φ_wf − E_i(ℓ)), with plane-wave final
states ⟨k_f|e^{iq·r}|ψ_{iℓ}⟩ = Ψ̃_i(ℓ, q − k_f).
**Literature limits.** 1606.08849 [FT] Eq. (5) vσ_i(ℓ) = (σ̄_e/μ_eχ²)∫d³k_f/(2π)³ d³q/(4π)|F_DM|²|Ψ̃_i(ℓ, q − k_f)|²δ(k_f²/2m_e + E_i(ℓ) + Φ + q²/2m_χ − q·v),
Eq. (7) R = 2Σ_i(ρ_χ/m_χ)N_CA_uc∫d²ℓ/(2π)²d³v g(v)vσ_i: = (E12.2) via WP0 (3.3) (the d³q/4π factor as in C1b). Leading corrections: (i) plane waves are
not orthogonal to ψ_{iℓ}: the OPW replacement |k_f⟩ → |k_f⟩ − Σ_occ|ψ⟩⟨ψ|k_f⟩ removes a spurious q-independent (monopole) piece [D]; (ii) final-state
interaction with the sheet potential and image (Sommerfeld-type) [C size]; (iii) 1706.02487 [FT] Eq. (23) applies the same to nanotubes; its text
defines E_r = k′²/2M_χ, which must read k′²/2m_e (misprint, does not affect the k′-integral as written). 2312.00866 [FT] Eqs. (13)–(19) (BLG) =
(E8.2)/(E12.1)-type at ε₁ = ε₂ = 1, r_K = 0, with a step-profile F_z = sinc(q_zd/2); corrections: substrate (factor in v_C^{2D}), Keldysh term, and an
F_z from the actual 2p_z transition densities.
**Computation specification.** Inputs: Wannier (π + σ) TB or DFT (QE + Wannier90) bands; gate field (BLG U); substrate ε(ω) with polar phonons.
Codes: `lowd-rpa`; Yambo with slab cutoff as cross-check; vacuum ejection with OPW (new, small). Grids: k 600² near K (Dirac part), q_∥ down to 10⁻⁴ keV;
k_f to 100 eV. Convergence: C6a-type Dirac check to 10⁻⁴; f-sum of the sheet. Cost ~10 CPU-h (low energy), 10² CPU-h (ejection). Outputs:
S_sheet(q_∥,ω), F_z(q_z) per band, Λ-resolved (k̂_f) ejection tables for directional readout.

---
## 7. X6: the Wannier and bremsstrahlung pictures of Migdal as limits of WP3-v3 (W.5)
**(a) Bremsstrahlung-like picture [D].** Chain: (W.5) with T0 (leading non-adiabatic), T1 (Condon), T2 (GS vibrational final states), T3 (RPA+LFE on the
(p, ω_e) lines), **G ≠ G′ kept** (T4 not taken), T5 = imp (S^{GS}_κκ → δ(ω_ph − |q − p − G|²/2M_κ), soft |p| ≪ q), valence only (U_κ(p) = Z_ione²/p²),
isotropic target (⟨[q̂·(p+G)][q̂·(p+G′)]⟩ = (p+G)·(p+G′)/3), and S^{ee}_{GG′} = (2|p+G||p+G′|/e²)Im[−ε̃^{-1}_{GG′}] (symmetrised form; needs R_{GG′} = R_{G′G},
TR + inversion, otherwise the anti-Hermitian part). Then dP/dω = 4αZ_ion²q²ℱ(ω)/(3M_κ²ω⁴Ω) and the rate prefactor is that of 2011.13352 (C7).
*Literature limit.* 2011.13352 [FT]: Eq. (1) amplitude with the bracket [1/(p_N²/2m_N + ε_ij − |p_N + k|²/2m_N) − 1/(ε_ij + k²/2m_N)] (= WP3-v3 L7c exact-impulse
bracket), Eq. (7) and (10) (HEG), Eq. (11) R = (ρ_χ/m_χ)(2A²σ_χnZ_ion²αN_T/(3μ_χn²Ωm_N²))∫d³v f/v∫p_N³dp_N∫dω ℱ(ω)Θ/ω⁴, Eq. (12) ℱ(ω) = Σ_{GG′}∫_1BZ Ωd³k/(2π)³
[(k+G)·(k+G′)/(|k+G||k+G′|)]Im[−ε̃^{-1}_{GG′}(k,ω)]: identical to the chain above (C7). Their Eqs. (14)–(15) (first order in α) are the IP limit.
Leading corrections: cores (L7a per shell; dominant for the ω_e³ moment, WP3-v3 J8); anisotropy (cubic: first ℓ = 4); lattice binding below
q ≈ 2√(2Mω̄) (L7c); exact-bracket recoil ≲ 10⁻³ (WP3-v3 §2).
**(b) Wannier picture [D, sketch].** WP0 §6.2(ii): A^{Mig}_f ∝ (q/M_κ)·⟨a|∇_{R_0}V_pot|0⟩/ω_e², and for local H ⟨a|Σ_i∇_iV_pot|0⟩ = m_eω_{a0}²⟨a|Σ_ir_i|0⟩.
*Hypothesis (H_W), rigid Wannier following:* the force operator of nucleus 0 acts as the electronic translation generator restricted to the Wannier
functions centred on site 0, ∇_{R_0}V_pot → −Σ_i∇_iV_pot 𝒫^W_0. (H_W) obeys the acoustic sum rule (Σ_sites 𝒫^W = 1 in the band subspace, WP0 (4.8)(i)).
Under (H_W) the amplitude becomes (m_eq/M_κ)·⟨a|r𝒫^W_0|0⟩, the first order of the boost restricted to site-0 Wannier functions, and to all orders the
sudden boost of 1912.13484 [FT] Eq. (2.7) |ik⟩_struck = N^{-1/2}(Ĝ_0(−q_e)|0i⟩ + Σ_{R≠0}e^{ik·R}|Ri⟩) and Eq. (2.8)
_struck⟨i′k′|ik⟩ = N^{-1}Σ_R⟨0i′|e^{iq_e·r} − 1|Ri⟩e^{ik·R}, q_e = (m_e/m_N)q. Consequences [D]: (i) exact for one atom and for core shells (r_core ≪ bond length);
(ii) its drag mass (WP3-v3 J3) is δM^W = N_e^W m_e per site (electrons in site-0 WFs), i.e. the "all electrons dragged" trace estimate of WP3-v3, not the
DFPT tensor δM_κ; (iii) for valence (bond charge shared) (H_W) fails at O(1) in principle; the correction is (q/M_κ)·⟨a|(∇_{R_0}V^{scf} + Σ_i∇_iV𝒫^W_0)|0⟩/ω_e²,
computable with DFPT. 2011.13352 argues the same failure for itinerant electrons [FT]. Its size is not computed (gap G-X6).
**Computation specification.** The WP3-v3 §8 G6 code path (one code for L7a–d) plus a Wannier branch: MLWFs (Wannier90, k 16³, atom- or bond-centred),
DFPT ∇_RV matrix elements on the same U(k) (CONVENTIONS §4 gauge rule), evaluation of the (W.5) amplitude and of its (H_W) truncation side by side;
ε̃^{-1}_{GG′}(p,ω) from Yambo/BerkeleyGW (100–300 G), p ≤ 30 keV. Convergence: δM sum rule (J3) and P_Mig ≤ 10⁻³ cross-checks. Cost ≈ 10³ CPU-h.
Outputs: S^X(q;ω_ph,ω_e) for Si/Ge/diamond; the (H_W)/(W.5) ratio per q as the X6 nuisance (type M).

---
## 8. X8: Migdal electronic excitation without ionisation (bound final states)
**Truncation chain.** WP3-v3 (W.5) with ω_e restricted to bound electronic final states: excitons (𝒳 = BSE in S^{ee}_{GG′}, lines below E_min(p),
support-opening ⇒ nuisance type A, WP0 (8.1)) or atomic/molecular/defect levels; the δ(ω_ph) part is X0 (zero-phonon Migdal), the rest X+.
**(X8.1) Crystal (exciton lines) [D].** Insert the BSE spectral form of WP1-v3 [E7], generalised to G, G′,
S^{ee,x}_{GG′}(p,ω_e) = (4π/V)Σ_λ ρ_{λ0}(p+G)*ρ_{λ0}(p+G′)δ(ω_e − E_λ(p_r)), ρ_{λ0}(p+G) = Σ_{cvk}A^{λ*}_{cvk}ρ̃_cv(k,p+G), into (W.5). Size [E]: by WP1-v3 [E8]/C8a
the bound weight equals the free-continuum weight within ≈ 8E_x^b of the edge, so bound Migdal is a fraction ~E_x^b/ω_e of the near-edge Migdal
spectrum: negligible in Si/Ge (E_x^b ≈ 15/4 meV), relevant in wide-gap ionic scintillators with large E_x^b, where it is optically detectable.
**(X8.2) Isolated atom [D].** Chain T0 + T6 (one nucleus) + free recoil: U_n is the Galilean boost (WP0 §6.2(ii)), so S^X_κκ = S^{GS}_free(q,ω_ph)Σ_f
P^{Mig}_f(q)δ(ω_e − E_f), P^{Mig}_f = |⟨Ψ_f|e^{iq_e·Σ_kr_k}|Ψ_i⟩|², q_e = m_eq/m_A (CONVENTIONS §13 item 22). Exact hydrogenic check (C8):
P(1s → 2p₀) = (2¹⁵/3¹⁰)(q_ea)²/(1 + 4(q_ea)²/9)⁶, whose dipole limit is (2¹⁵/3¹⁰)(q_ea)².
**Literature limit.** 2604.26773 [FT] Eq. (1) P_fi = |⟨Ψ_f|e^{iq_e·Σr_k}|Ψ_i⟩|², Eq. (6) d²R/dE_RdE_EM = (dR_N/dE_R)Σ_iP^{(i)}_exc(E_R)δ(E_EM − E_exc^{(i)}) = (X8.2)
integrated against the free recoil (their Eq. (7) dR_N/dE_R is the S^{GS} part). Their sign q_e = −m_ev_N is the opposite boost phase (immaterial,
NOTATION §K). Leading corrections: liquid/solid He environment (excimer formation: X+ with medium recoil; atomic wavefunctions in the condensed phase)
[C]; boost mass m_A vs m_N (O(Zm_e/M)); multi-electron correlation (their MCHF vs dipole: source-internal).
**Computation specification.** Atoms: GRASP2018/MCHF transition elements (as the source), n ≤ 5. Crystals: finite-p BSE over the BZ (p 8³–12³, G ≤ 50,
λ ≤ 20 per p) inside the G6 path; convergence: exciton-line weights against the [E8] Wannier–Mott limit; cost ≈ 10⁴ CPU-h (like WP3-v3 G5).
Outputs: line tables (E_λ(p), weights) of S^X below E_min, Λ = (λ, p) seeds for WP5 (radiative branching).

---
## 9. A2: absorption in superconductors and metals (Holstein, Mattis–Bardeen, WP4-v3 consistency)
**Truncation chain.** WP0 (3.5)–(3.6) at k_φ → 0 (dark photon: Γ = κ_mix²m_φIm(−1/ε), L9b; ALP: tr J_e; scalar: 𝒯_e) → metals violate (H2): sectors
are the quasiparticle-number sectors of WP4-v3 Theorem D-g; the Holstein process is sector (2, 1) (one e–h or QP pair + one phonon), n_g = 2 →
Fermi-surface (Migdal) approximation, ω ≫ 1/τ_imp, T = 0. In a clean BCS superconductor the zero-phonon absorption at k_φ → 0 vanishes
(R̃^{GRPA}(0,ω) ≡ 0, WP4-v3 K2), so all sub-interband absorption is disorder-assisted (MB) or phonon-assisted (Holstein).
**(A2.1) Normal metal [D, sketch].** From the velocity-form PA amplitude of WP3-v3 (M.17) restricted to intraband Fermi-surface states, A₁^v + A₂^v →
g·ê·(v_{k+Q} − v_k)/ω; the Fermi-surface average of |ê·Δv|² gives the transport weight (1 − cos θ) and the pair phase space gives (ω − ω_ph):
  σ₁^{(2,1)}(ω) = (ω_p²/ω²) γ_H(ω),   γ_H(ω) = (2π/ω)∫₀^ω dω_ph (ω − ω_ph) α²F_tr(ω_ph),   ε₂ = σ₁/ω,                                       (A2.1)
and Γ_abs = κ_mix²m_φIm(−1/ε) = κ_mix²σ₁/|ε|² exactly (κ_eff² = κ_mix²/|ε|² since Π^{med}_γ = m²(1 − ε)).
**(A2.2) Superconductor [D, sketch].** With intermediate states off shell by ≳ ω_ph ≫ Δ_BCS, the effective pair-creation vertex i[j, g]/ω is
time-reversal even, so the final QP pair carries the case-I (density-type) coherence factor, and the ξ-integrated pair density at energy
x = ω − ω_ph is x𝔤_I(x/Δ_BCS) (WP4-v3 [4.2]):
  σ₁^{S,(2,1)}(ω) = (ω_p²/ω²)(2π/ω)∫₀^{ω−2Δ_BCS}dω_ph α²F_tr(ω_ph)(ω − ω_ph)𝔤_I((ω − ω_ph)/Δ_BCS),   𝔤_I(y) = E(√(1 − 4/y²)).                (A2.2)
The identity 𝔤_I(y) = E(√(1 − 4/y²)) (modulus) follows from WP4-v3 [4.2] by the Landen transformation and is checked by quadrature (C9b). The
elastic (impurity, ω_ph → 0) limit is instead Mattis–Bardeen, case II, x[E(k′) − b²K(k′)], b = 2Δ_BCS/x, k′ = √(1 − b²) (= WP4-v3 𝔤_II, C9b), because there
the intermediate states are off shell by only ~ω ~ 2Δ_BCS and the exact-eigenstate (current-vertex) argument applies. The two differ only within a
few Δ_BCS of the onset (𝔤_I → π/2, MB → 0 at x → 2Δ_BCS).
**Literature limit.** 1604.06800 [FT]: Eq. (8) photon rate (n_ee²/m_e*ω²)(1/τ(ω)), Eq. (13) σ₁ ≈ ω_p²/(ω²τ), Eq. (16) 1/τ_Φ = (4/5)πλ_trω_D(1 − (5/6)ω_D/ω)
(ω ≥ ω_D), (2/15)πλ_trω⁵/ω_D⁴ (ω < ω_D), Eq. (17) τ^N/τ^S = ∫₀^{ω−2Δ}dΩ(ω−Ω)Ω⁴E[(1 − 4Δ²/(ω−Ω)²)^{1/2}]/∫₀^ωdΩ(ω−Ω)Ω⁴, Eqs. (19)–(20) R = ρ^{-1}(ρ_DM/m_DM)κ_eff²σ₁.
(A2.1) with a Debye α²F_tr = 2λ_trω_ph⁴/ω_D⁴ gives Eq. (16), both branches (C9a); (A2.2) with the same α²F_tr gives Eq. (17) exactly (C9b): their
coherence factor is case I, consistent with (A2.2). Leading corrections: strong coupling (Eliashberg Δ(ω), mass renormalisation 1 + λ) [E: tens of %
for λ ≈ 0.4]; anisotropic/multiband α²F; interband above ~0.5 eV (Al: data); T > 0 phonon absorption (n_B(ω_ph) term); ω ≫ 1/τ_imp.
**WP4-v3 consistency.** (i) Seeds: Λ = (E₁, E₂, ω_ph) with P(E₁|ω, ω_ph) = WP4-v3 [4.6] at ω → ω − ω_ph; (ii) η_pb (WP4-v3 §4.6) is computed with the
QP energy ω − ω_ph, the phonon energy going first to the phonon system; (iii) WP4-v3's sentence "one mechanism … gives both 𝔤_I and MB" is refined:
elastic momentum relaxation gives MB, phonon-assisted relaxation (ω_ph ≫ Δ_BCS) gives 𝔤_I (flag IF-B1-1).
**Computation specification.** Inputs: EPW α²F_tr (Al: k 60³ / q 30³ fine grids as WP4-v3 §4.6) or the resistivity λ_tr; Δ_BCS(T); optical data
0.2–3 eV for validation. Code: σ₁ module (A2.1)–(A2.2), ω_ph step ≤ Δ_BCS/20; convergence: σ₁^N vs Al data to 20%; cost ~10³ CPU-h (EPW) else seconds.
Outputs: σ₁(ω; T) normal/SC, (2,1) seeds.

---
## 10. A6: dopant absorption (hydrogenic, k ≈ 0)
**Truncation chain.** WP0 (3.5)–(3.6) at k_φ → 0 (total-charge ε for a dark photon; WP0 (5.4)) → (1.2) dopant response S^D (WP4-v3 [6.1]) → EMT
(single-valley hydrogenic envelope, a* ≫ a_lat) with host screening and the out-state local-field weight → X0 lines and continuum (+ small X+ sidebands).
**(A6.1) Absorption [D].** For 𝓃_D a*³ ≪ 1 and |δε_D| ≪ ε_host,
  Γ_abs = κ_mix² m_φ ε₂^D(m_φ)/|ε_host(m_φ)|²,   ε₂^D(ω) = lim_{q→0}(e²/2q²)S^D(q,ω) = 4π²α 𝓃_D |𝔣^{loc}_D|² Σ_f |⟨f|q̂·r|i⟩|² δ(ω − E_f + E_i),        (A6.1)
where 𝔣^{loc}_D = lim_{q→0}Σ_G(ε^{-1}_host)_{G0}ρ_fi(q+G)/[(ε^{-1}_host)_{00}ρ_fi(q)] is the local-field ratio (the source's E_eff/E_0); one donor electron, f runs
over orbital final states (no spin factor 2). Final states: (a) bound 1s → n_Hp lines at ω = E_b^D(1 − 1/n_H²) (Lyman series; hydrogenic oscillator strengths, multivalley
corrections) — type-A support; (b) the continuum ω > E_b^D.
**(A6.2) Hydrogenic generalised oscillator strength [D, C10].** Summed over final directions, Σ|⟨k_f|e^{iq·r}|1s⟩|² ∝ q̃²(3q̃² + k̃² + 1)exp[−(2/k̃)atan2(2k̃, q̃² − k̃² + 1)]
/[((q̃+k̃)² + 1)³((q̃−k̃)² + 1)³(1 − e^{−2π/k̃})], q̃ = qa*, k̃ = k_fa*; checked against a direct partial-wave sum with exact Coulomb waves (C10).
**Literature limit.** 2212.04504 [FT]: Eq. (9) Γ(v) = ∫d³q/(2π)³|V|²(q²/2πα)𝒲, Eq. (10) 𝒲 = (2π)²α𝓃_D/(q²|ε|²)Σ_{ξ,k}δ(E_k − E_i − ω)|⟨ξk|ρ̂(q)|i⟩|², Eq. (12) the closed
form with a heuristic (E_eff/E_0)², and below it "R_χ = κ²(ρ_χ/ρ_T)𝒲(q = 0, m_χ)". The absorption sentence is (A6.1) per unit mass (Γ_abs ρ_χ/(m_χρ_T)) with
𝒲 = ε₂^D/|ε|² [D]; Eq. (10) is (1.2) with RPA host screening. Findings: (i) **Eq. (12) prints (3q̃ + k̃² + 1); the hydrogenic GOS has (3q̃² + k̃² + 1)**
(C10: the printed form is off by ×2.2 between q̃ = 0.5 and 2 at k̃ = 1); the absorption limit q̃ → 0 is unaffected, the scattering 𝒲 is affected as
printed (their numerics not checked); (ii) the bound Lyman lines (a) are absent (they treat ionisation only); (iii) at their 𝓃_D = 1.8×10¹⁸ cm⁻³, a* = 23 a.u.
gives 𝓃_D^{1/3}a* ≈ 0.15 (𝓃_Da*³ ≈ 3×10⁻³), below the Mott value ≈ 0.26 [E]: (1.2) holds, with impurity-band broadening as a correction. Leading corrections: computed
𝔣^{loc}_D instead of (E_eff/E_0)²; central cell and valley–orbit (EMT error 10–30% in E_b^D, WP4-v3 §6); phonon sidebands (S_HR ≪ 1 for shallow donors) [E].
**Computation specification.** As WP4-v3 §6 (multivalley EMT + central-cell DFT, or 512–4096-atom supercells; ~10⁴ CPU-h) plus Yambo RPA+LFE
ε^{-1}_host,G0(q → 0, ω ≈ E_b^D) for 𝔣^{loc}_D; convergence: donor TRK sum (Σf = 1 in m* units) to 2%, E_b^D to 1 meV. Outputs: ε₂^D(ω) lines + continuum,
absorption reach per 𝓃_D, the C10 GOS for scattering tables.

---
## 11. I3: inelastic DM–electron scattering (Δ_χ ≠ 0) in crystals
**Truncation chain.** WP0 (2.1) with Δ_χ ≠ 0; (3.3)–(3.4) unchanged; S_ab unchanged (any τ). For a pseudo-Dirac vector current the off-diagonal
χ₁ → χ₂ NR vertex is 𝒪₁ with the elastic coefficient up to O(Δ_χ/m_χ) [D], so 𝔇 is unchanged.
**(I3.1) General rate [D].** dℛ/dω = (ρ_χσ̄_e/(4πm_χρ_Tμ_χe²))∫q dq F_DM²η(|v_min|)S̄(q,ω), v_min = (ω + Δ_χ)/q + q/2m_χ (WP0 (9.2) with WP6-v3 (1.3) Θ(v − |u|)).
**(I3.2) Exothermic shell [D] (C11).** For Δ_χ < 0, at fixed ω < |Δ_χ| and any target, ∫d³q δ(ω − |Δ_χ| − q·v + q²/2m_χ)F(|q|) = 4πm_χF·(q_Δ*² + m_χ²v²)^{1/2}
for constant F, q_Δ* = √(2m_χ(|Δ_χ| − ω)), exactly. Hence
  dΓ_χ/dω = (m_χq_Δ*/(2π²)) |Ṽ(q_Δ*)|² S̄(q_Δ*, ω) [1 + O(v²/v_Δ*²)],   v_Δ* = q_Δ*/m_χ,                                                  (I3.2)
halo-independent up to O(v²/v_Δ*²) (the window is symmetric in |q|; with S(q) = S(−q) the anisotropic O(v) term also cancels) [D]. The rate samples S̄ along
the parabola q_Δ*(ω). This sharpens WP4-v3 [7.2]'s O(v/v*) to O(v²/v*²) for ω-integrated rates (flag IF-B1-5).
**(I3.3) Light-mediator edge [D].** As ω → |Δ_χ|, S̄ → (q²/2πα)L(0,ω) (optical limit, CONVENTIONS §6), so with |Ṽ|² = πσ̄_e(αm_e)⁴/(μ_χe²q⁴),
dΓ_χ/dω → m_χσ̄_eα³m_e⁴L(0,ω)/(4π²μ_χe²q_Δ*) ∝ (|Δ_χ| − ω)^{-1/2}: an absorption-like edge fixed by the optical ELF. The shell condition v ≪ v_Δ* fails
for |Δ_χ| − ω ≲ m_χv²/2, where the exact window (C11 with F ∝ q⁻²) regularises the edge to a halo-dependent logarithm.
**Literature limit.** 2203.06664 [FT] Eq. (11) v_min = |(ΔE_e + δ)/q + q/2m_χ| (δ ≡ Δ_χ), Eq. (15) η, Eq. (16) dR_c/dE_e = (ρ_χ/m_χ)(1/m_T)σ̄_eα(m_e²/μ²)∫dq F_DM²|f_c|²η,
Eq. (20) |f_c|²: = (I3.1) by the |f_crys|² dictionary (WP1-v3 [E12]; WP0 (9.2) L1 chain), including the absolute value. Leading corrections: screening
(their |f_c|² is IP; L2/L3); for |Δ_χ| ≳ 10 eV and q_Δ* ≳ keV, core shells (L1 per shell); the edge region (I3.3).
**Computation specification.** WP6 library tables S̄(q,ω) plus a Δ_χ axis; shell integrator (WP4-v3 §7 Lebedev ≥ 590, extended to continuum S) and the
exact-window form near the edge; convergence 1%, validated by C11; cost negligible. Outputs: dℛ/dω vs (m_χ, Δ_χ, σ̄_e).

---
## 12. I5: boosted and solar-reflected DM
**Truncation chain.** WP0 (3.3) with relativistic DM kinematics ω = E_χ − E′_χ, E_χ = √(p_χ² + m_χ²), and a DM-side tensor 𝔇 built from relativistic DM
currents; target rows unchanged (NR electrons; valid while ω, q ≪ m_e, i.e. the O(v_e¹) Foldy–Wouthuysen truncation of WP0 §1.2 holds on the target side).
**Where the NR basis fails [D].** WP0 (2.2) expands the DM vertex in v^⊥ and treats the mediator as instantaneous (ω ≪ q). For a vector mediator of mass
m_V coupling to the DM vector current J^μ_χ and to the conserved electron current, current conservation on both sides gives (C12c)
  ℳ ∝ [J⁰_χ ρ_e (1 − ω²/q²) − J_{χ,T}·j_{e,T}] / (q² − ω² + m_V²),                                                                       (I5.0)
so (i) the density row carries the retardation factor (1 − ω²/q²) ≤ 1 (and is exactly Coulomb, 1/q², for m_V → 0); (ii) a transverse row j_T appears
with DM-side weight O(v_χ) (target side O(v_e)), propagating with 1/(q² − ω² + m_V²) (in medium: the transverse 𝒟^γ of WP0 (3.6)); (iii) all corrections
are O(v_χ²), since ω/q ≤ v_χ. The NR basis is accurate to ~1% for v_χ ≲ 0.1 [E].
**(I5.1) Density row [D] (C12a,b).** Spin-averaged Dirac DM, (1/2)Tr[(p̸′ + m_χ)γ⁰(p̸ + m_χ)γ⁰] = (2E_χ − ω)² − q², so
  𝔇_{nn}(q,ω;p_χ) = (πσ̄_e/μ_χe²) [(2E_χ − ω)² − q²]/(4E_χ(E_χ − ω)) · (1 − ω²/q²)² · [(q₀² + m_V²)/(q² − ω² + m_V²)]²,                         (I5.1)
→ |Ṽ|² of WP0 (2.2) for v_χ → 0. The transverse row adds 𝔇_{j_Tj_T}S_{j_Tj_T}, relative size O(v_χ²⟨v_e²⟩) [E: ≲ 10⁻⁴ for valence], except near the light cone
of the medium (v_χ > 1/n_r), where the in-medium transverse pole opens a Cherenkov-type channel (the transverse-photon-improper part of WP0 (3.6) in
scattering) [D for the structure; C for the size].
**Literature limits.** 2401.11971 [FT] Eq. (4) Γ(p_χ) = ∫d³Q/(2π)³|V(Q,ω)|²[2(Q²/e²)Im(−1/ε(Q,ω))], Eq. (5) |V|² = πσ̄_χe[(2E_χ − ω)² − Q²]/(4μ_χe²E_χ(E_χ − ω))|F_DM(q)|²
with F_DM at q² = Q² − ω², Eq. (6) flux convolution with E_χ/p_χ: equals (I5.1) except for the factor (1 − ω²/Q²)², which their Eq. (5) lacks (their
electron current is taken as pure J⁰, which is not conserved). Their rate is too large by (1 − ω²/Q²)^{-2} ≤ (1 − v_χ²)^{-2}, i.e. ≤ 1.78 at v_χ = 0.5 and
large near ω → Q for light mediators [D, C12c]. 2607.09352 [FT] Eq. (9) dΦ_χ/dv, Eq. (10) dR/dE_e ∝ ∫(dq/q²)η F_DM²|F_c|²|ε^{-1}|², Eq. (11)
η = ∫_{v_min}dv v^{-2}dΦ_χ/dv: SRDM speeds keep v_χ ≲ 10⁻¹, so the NR basis holds and (11) is WP0 (9.2) with ρ_χf_χ(v)/m_χ → dn_χ/d³v = (dΦ_χ/dv)/(4πv³)
for an isotropic flux [D]. Two caveats: the reflected flux is anisotropic (θ_iso), so hypothesis (I) of WP0 §9.1 holds only for an angle-averaged S;
and |F_c|²|ε^{-1}|² with a jellium Mermin ε and the QCDark IP form factor is not one 𝒳 rung: S = S⁰/|ε|² is exact only for ε = 1 − v_CR⁰ built from the
same R⁰ (WP1-v3 [E1]), so the f-sum is not guaranteed (use RPA+LFE on the same bands, as in their QCDark2 comparison). 2501.07591 [ABS].
**Computation specification.** Inputs: flux tables dΦ_χ/dT_χdΩ (external CRDM/solar-reflection codes); full-vector S(q,ω) to q ≈ 100 keV, ω ≤ 10 keV
(all-electron ELF with cores: Yambo/GPAW + shell tables); new DM-side module for (I5.0)–(I5.1) (density + transverse rows, in-medium propagators).
Grids: q log 0.1–500 keV, ω 1 eV–10 keV, flux directions 590. Convergence: f-sum per q to 2%. Cost ~10³ CPU-h (library extension). Outputs: dℛ/dω vs
(m_χ, σ̄_e, flux model), directional.

---
## 13. Exact remaining gaps (why not done)
- **G-E8 (CDW collective modes):** phason/amplitudon coupling to n_e near ±Q_CDW needs a conserving (Ward-identity) response on the CDW mean field and,
  for Peierls CDWs, the coupled electron–phonon mode; Theorem D-g does not cover bosonic collective sectors (as for magnons, OW0-17). Not derivable
  from WP0–WP6 without that reference-state theory.
- **G-E5:** charge-transfer excitons (finite intermolecular overlap) and the accuracy of Hückel/PPP form factors against BSE are unquantified [C].
- **G-E10:** inter-dot (Förster) coupling in dense films and the R_QD ~ a_x crossover; ligand-state contributions.
- **G-E12:** semiconducting-CNT 1D massive-Dirac RPA (van Hove edges) not written; OPW and final-state-interaction sizes for vacuum ejection not computed.
- **G-X6:** size of the non-rigid Wannier correction (needs the DFPT vs (H_W) comparison of §7(b)).
- **G-X8:** crystal exciton Migdal never computed (finite-p BSE over the BZ).
- **G-A2:** (A2.2) rests on the off-shell T-parity argument [D, sketch]; an explicit Nambu second-order calculation (and Eliashberg strong coupling)
  is owed.
- **G-A6:** impurity band near the MIT; valley–orbit structure of the lines.
- **G-I5:** Cherenkov-type transverse channel size; anisotropic-flux contraction with full-vector S.

---
## 14. Literature (arXiv API verified; [FT] = HTML full text read this session)
[FT]: 1912.02822, 2103.08601, 2607.15338, 2507.07164, 2510.18338 (fetched; ELF-type, not quoted), 2110.01587, 2603.15581, 2208.05967, 1606.08849,
1706.02487, 2312.00866, 1912.13484, 2011.13352, 2604.26773, 1604.06800, 2212.04504, 2203.06664, 2006.11938 (fetched; atomic, not quoted), 2401.11971,
2607.09352. [ABS] (title/authors via API only): 2512.18010, 2607.12036, 2608.01305, 2608.18204, 2303.15497, 2604.21969, 2106.12586 (App. A.3 not
re-read; WP3-v3 has it [FT]), 2210.15474, 2112.06930, 2501.07591. Source discrepancies found: 2212.04504 Eq. (12) (3q̃ → 3q̃²); 2401.11971 Eq. (5)
(missing (1 − ω²/Q²)²); 2208.05967 Eq. (16) (bulk ε for dots in solvent, conservative ×~6 [E]); 1706.02487 (E_r = k′²/2M_χ → k′²/2m_e); 2607.09352
Eq. (10) (mixed 𝒳). 2110.01587 Eq. (16) is exact beyond its stated d/L ≪ 1 (a strengthening, not an error).

---
## 15. Symbols introduced/used (against NOTATION v4 + R9)
Used as in NOTATION: S, S_ab, R, R̃, R⁰, ε, ε̃, L, v_C, ρ_cv, ρ̃_cv, A^λ_{cvk}, E_λ, λ, E_x^b, a_x, 𝒮_F, ζ_S, S_HR, W^{scr}, Λ, P_Λ, τ, 𝒳, GS/X0/X+, 𝔇, Ṽ, σ̄_e,
F_DM, η, v_min, Δ_χ, κ_mix, Π^{med}_γ, 𝒟^γ, 𝔤_I, 𝔤_II, Δ_BCS, y_BCS, α²F, λ_ep, ω_D, E_1/E_2, 𝓃_D, a*, E_b^D, m*, ε_bg, v_F, g_deg, 𝓈, Λ_D, 𝔣_Lin, γ_rel, d_film, S_film,
U_κ(p), Z_κ(p), δM_κ, P_Mig, q_e (Table 6.1), ω_e, ω_ph, Ψ^{vib}, n_H, E_e/E_h, 𝓃_e, ω_p, k_TF, ε_∞, n_r, σ₁, a_lat, q_BZ.
New (proposed NOTATION rows; none collides with an existing row):
| Symbol | Meaning | Where |
|---|---|---|
| 𝔬, r_𝔬, 𝖱_𝔬, N_mol | molecule-in-cell label, its position, orientation, number per cell (κ stays the nuclear species) | (E5.1) |
| 𝔵, E_𝔵, f^{(𝔬)}_{0𝔵}(q) | molecular singlet excited state, its energy, molecular form factor (√2 included) | (E5.1) |
| H^F, 𝔍^F(Q), A^{F,λ}_{𝔬𝔵}(Q), w_{𝔬𝔵}(q) | Frenkel Hamiltonian, exchange (transition-density Coulomb) coupling, Frenkel envelope, screened molecular vertex | (E5.1)–(E5.2) |
| 𝓃_mol, 𝓃_u, 𝓃_t | molecule number density; unit density (1.1); tube areal density | §2, (1.1), (E8.1) |
| F_⊥(q_⊥), F_z(q_z), ϱ_⊥ | transverse form factors and profile of a low-dimensional unit | (1.1), (E12.1) |
| S_d, S_wire, S_sheet | d-dimensional, wire and sheet responses (per unit d-volume) | (1.1), (E8.1), (E8.2) |
| N_ch, g_LL, v_LL, r_t, ε_env | 1D channels; Luttinger charge parameter and velocity; tube radius; environment dielectric constant | (E8.1) |
| v_C^{1D}, v_C^{2D}, v_C^{L}(q_∥,q_z) | wire, sheet and layered-stack Coulomb kernels | (E8.1), (E8.2), (E9.1) |
| R̃^{2D}, R̃^{2D}_{low}, R̃^{2D}_{bg}, r_K | sheet proper response, its low-energy and remote parts; Keldysh length (r_Kq ≡ −v_C^{2D}R̃^{2D}_{bg}) | (E8.2) |
| k_TF,1, ω_{p,2}, ω_a, w_a(q) | light-species TF momentum, heavy-species plasma frequency, acoustic (demon) mode and its f-sum share | (E8.3) |
| a_s, ε_b, N_lay, f_fill, ε_A, ε_B, d_A, d_B, ε_∥, ε_⊥ | stack period, interlayer background, layer number, filling, layer dielectrics and thicknesses, EMT tensor components | §4 |
| R_QD, ϕ_QD, 𝓃_QD, ε_in, ε_out, E_g^{QD}, 𝔣^{loc}_ℓ, ρ_cv^{cell} | dot radius, volume fraction, density, inside/outside dielectric, confined gap, multipole local-field factor, band-edge cell form factor | §5 |
| 𝒫^W_0, (H_W), δM^W, N_e^W | site-0 Wannier projector, rigid-Wannier hypothesis, its drag mass, electrons in site-0 WFs | §7 |
| P^{Mig}_f(q) | Migdal transition probability to bound final state f | (X8.2) |
| γ_H(ω), α²F_tr, λ_tr | Holstein rate, transport Eliashberg function, transport coupling | (A2.1) |
| 𝔣^{loc}_D, ε₂^D | donor local-field ratio (source E_eff/E_0); dopant ε₂ | (A6.1) |
| q_Δ*, v_Δ* | exothermic shell momentum and velocity (q_ν* stays the mode shell) | (I3.2) |
| E_χ, p_χ, J^μ_χ, Φ_χ | DM energy, momentum, vector current, flux | §12 |
Source-only (NOTATION §K style): g, v (2607.15338 Luttinger) → g_LL, v_LL; κ (2208.05967, 1604.06800 mixing) → κ_mix; δ (2203.06664) → Δ_χ; Q (2401.11971
three-momentum) → q; Ω (1604.06800 phonon energy) → ω_ph; E_I (2212.04504) → E_b^D; n_D → 𝓃_D; W, 𝒲 → L or ε₂/|ε|² as stated.

---
## 16. Interface flags
| # | Owner / user | Quantity | Recorded form | Form here / action |
|---|---|---|---|---|
| IF-B1-1 | WP4-v3 §4.3, L15, L9b | coherence factor of absorption in SC | "one mechanism gives both 𝔤_I and MB" | elastic (disorder) → MB (case II); phonon-assisted with ω_ph ≫ Δ_BCS → 𝔤_I (case I) (A2.2); 1604.06800 (17) = x𝔤_I (C9b) |
| IF-B1-2 | WP4-v3 [4.5] (film S_surf "[C with images]") | thin film / sheet response | specular-model estimate | thin sheets and stacks: exact (E9.1) and finite-N_lay matrix [D] |
| IF-B1-3 | WP4-v3 L16, LIMITS L16 | 2D Dirac background | 3D ε_bg rule | 2D: substrate only through v_C^{2D} = e²/(q(ε₁+ε₂)), remote bands only through r_K; never rescale the vertex (same ε_bg-type pitfall) |
| IF-B1-4 | WP3-v3 (W.5), WP6 nuisance typing | bound lines in S^{ee}_{GG′} | continuum Migdal | exciton lines are part of X Migdal (X8.1), type A; X0 for the δ(ω_ph) part |
| IF-B1-5 | WP4-v3 [7.2], WP6 | exothermic shell accuracy | O(v/v*) | O(v²/v*²) for ω-integrated rates (C11); light-mediator edge (I3.3) halo-dependent within m_χv²/2 |
| IF-B1-6 | WP0-v3 §2, WP6, CONVENTIONS §7 | DM vertex for relativistic DM | NR 𝒱_a | (I5.0)–(I5.1): retardation (1 − ω²/q²) in the density row, F_DM at q² − ω² in the propagator, transverse row; NR basis valid for v_χ ≲ 0.1 |
| IF-B1-7 | WP5-v3 seeding (WP0 (7.3)) | new Λ classes | — | Frenkel (𝔬, 𝔵) with radiative yield; QD (e, h envelopes, MEG); Holstein (E₁, E₂, ω_ph); layer-resolved pairs; bound-Migdal (λ, p) |
| IF-B1-8 | NOTATION | rows of §15 | — | add |
| IF-B1-9 | WP6 library | τ strings | — | E8/E9/E12 entries: `X=RPA` with metadata `geom=1D|2D|stack`; E5 `X=BSE;basis=molecular`; A2 sector `(2,1)`, ref = BCS |

---
## 17. Proposed LIMITS rows (numbering to be assigned by the coordinator; sources read [FT])
| # | Source formula | τ / chain (URF) | Status | Leading correction |
|---|---|---|---|---|
| LB1-1 | 1912.02822 Eqs. (11), (13), (16)–(19); 2103.08601 Eqs. (8), (9) | (3.3) n_e → X0 → 𝒳 = BSE molecular basis → Frenkel → (E5.2′) binned; C1 | DERIVED | Davydov/exciton coherence at resolution ≲ 𝔍^F; q ≲ 1/a_mol local fields; CT excitons |
| LB1-2 | 2607.15338 Eqs. (3)–(6) | (1.1) d = 1 → linear bands → RPA (E8.1); C2 | DERIVED (f-sum fixes gv = v_F) | inter-tube Coulomb; subbands; backscattering |
| LB1-3 | 2312.00866 Eqs. (13)–(19); 2507.07164 Eqs. (1)–(3) | (1.1) d = 2 → RPA (E8.2); demon (E8.3); C3, C6 | DERIVED | substrate v_C^{2D}, Keldysh r_K, F_z profile |
| LB1-4 | 2110.01587 Eq. (16) | RPA with G_z local fields, ka_s → 0 → exact EMT (E9.2); C4c | DERIVED (exact at any filling) | O((ka_s)²) from (E9.3); ε_i(k) non-locality |
| LB1-5 | 2208.05967 Eqs. (6), (10)–(12); Eq. (16) | (1.2) dot centre → EFA → bulk limit (E10.3); absorption with 𝔣^{loc}_1 | DERIVED (✎ absorption local field) | O(1/qR_QD); 9\|ε_in\|²/\|ε_in+2ε_out\|² in absorption |
| LB1-6 | 1606.08849 Eqs. (5), (7); 1706.02487 Eq. (23) | (7.1) Λ = vac, IP, plane-wave final state (E12.2) | DERIVED | OPW orthogonalisation; final-state interaction |
| LB1-7 | 2011.13352 Eqs. (1), (7), (11), (12) | (W.5) T0–T3, LFE kept, T5 = imp, valence, isotropic; C7 | DERIVED | cores (L7a); anisotropy; lattice binding |
| LB1-8 | 1912.13484 Eqs. (2.7)–(2.8) | (W.5) amplitude under (H_W) | DERIVED under (H_W) [D, sketch] | non-rigid Wannier correction (DFPT) |
| LB1-9 | 2604.26773 Eqs. (1), (6) | (W.5) T0 + T6, free recoil, bound f (X8.2); C8 | DERIVED | condensed-phase environment; m_A boost mass |
| LB1-10 | 1604.06800 Eqs. (8), (13), (16), (17), (19)–(20) | (3.5), sector (2,1), n_g = 2, Fermi surface (A2.1)–(A2.2); C9 | DERIVED [D, sketch for (A2.2)] | strong coupling; interband; MB for the elastic part |
| LB1-11 | 2212.04504 Eqs. (9), (10), (12) + absorption sentence | (3.5)–(3.6) k → 0 + (1.2) EMT (A6.1); C10 | DERIVED (✎ Eq. (12) 3q̃²; Lyman lines added) | computed 𝔣^{loc}_D; central cell; impurity band |
| LB1-12 | 2203.06664 Eqs. (11), (15), (16), (20) | (2.1) Δ_χ, (9.2) with \|v_min\| (I3.1); shell (I3.2) C11 | DERIVED | screening (IP source); edge (I3.3) |
| LB1-13 | 2401.11971 Eqs. (4)–(6); 2607.09352 Eqs. (9)–(11) | (3.3) relativistic 𝔇 (I5.1) / NR with SRDM flux | DERIVED (✎ 2401.11971 needs (1 − ω²/Q²)²) | transverse row; anisotropic flux; consistent 𝒳 for S |
