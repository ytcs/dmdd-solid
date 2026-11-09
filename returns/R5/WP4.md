# R5 / WP4: spin, superconducting and special targets

Isolated theory agent. Read scope as in the brief. No numerical simulations were run. The identity checks are in
`code/WP4/checks.py`: K1–K10, all PASS, < 2 s (sympy residues, plus mpmath quadratures of one-dimensional integrals).
`code/WP4/html2txt.py` converts arXiv HTML to text. Full texts (FT) were fetched with lit.py into
`literature/papers-WP4/` and deleted at the end. All IDs were verified against the arXiv API (§10).
Tags: **[D]** DERIVED (hypotheses stated), **[E]** ESTIMATED, **[C]** CONJECTURED. WP4 equations are written **[s.n]**;
WP0 equations are written WP0 (s.n), with notation from WP0 §10. Units: ħ = c = k_B = 1, e² = 4πα (HL), v_q = e²/q².

---
## 0. Results at a glance

| Item | Result | Tag |
|---|---|---|
| L13 magnons | 1905.13744 Eqs. (5)–(12) and 2009.13534 Eq. (38) recovered from WP0 (3.3) restricted to the spin row of WP0 (2.2). The truncation chain has 6 steps (§2.1). Leading correction: the magnetic form factor \|F_j(q)\|², which is about 0.5 at q ≈ 0.5 keV for Fe³⁺ and is set to 1 in both sources. Next: two-magnon, O(1/2S) | D / E |
| Two-magnon (gap) | Closed-form longitudinal two-magnon S_ab [2.4]. It vanishes identically for a Heisenberg FM at T = 0 and is O(S⁰) against O(S) for AFM/ferri. It decouples ω from q, so it reaches ω up to qv rather than ω_ν(q) | D |
| Magnon–phonon (gap) | Joint magnon+phonon Colpa problem [2.5]. Each hybrid mode is shared between S_ss and S_NN according to its magnon/phonon content | D |
| Chiral / CD (gap) | Theorem [3.1]: for pure density coupling, Γ(v) ≠ Γ(−v) iff S(q,ω) ≠ S(−q,ω), which needs P **and** T broken. A chiral, T-even target is invisible to density coupling and shows an enantiomer difference only through operator interference ∝ Re(c₅*c₈), i.e. a P-odd DM interaction [3.3] | D |
| L15 superconductors | Chain from WP0 (3.3) via Nambu–Eliashberg → BCS → conserving generalised RPA (GRPA) → bare bubble (2609.06423 Eq. 8) → Lindhard (2101.08263 S.13) → 2101.08263 Eq. (3) and 1512.04533 Eq. (14). **The bare BCS bubble violates the f-sum at q → 0 (K2)**. In the DM region, closed form W_SC = g_I(ω/Δ) W_N, with g_I(2Δ⁺) = π/2 and g_I(5Δ) = 1.15 (K4) | D |
| Source defects | 2101.08263 Eq. (3): Re ε should be λ_TF²/q², not λ_TF²/2q² (K1), a factor 4 in W in that illustration. 1512.04533 Eq. (13) [(3.3) in the PDF]: e₋ lacks a factor 4 (K7). 2609.06423 Eqs. (4), (7): time-ordered, not retarded (−i0 on the negative pole) | D |
| Branch cut (2101.08263) | Resolved at master level: build Im ε from S ≥ 0 via WP0 (4.1), and Re ε by WP0 (4.2). No complex logarithm is needed | D |
| Films / disorder (G9) | Mermin (conserving) relaxation. Ratio of W in the ballistic (Lindhard) limit to the diffusive (= Drude) limit: πqℓ/6. QROCODILE's Drude ε for WSi is exact for qℓ ≲ 1 and underestimates W by πqℓ/6 for qℓ ≫ 1 | D / E |
| L16 Dirac | Chain from WP0 (5.3) with R̃ = R̃_Dirac + R̃_bg. 2101.08263 Eq. (4) is recovered exactly (K5). **1708.08929 Eqs. (3.7)/(3.11) and 1910.02091 Eqs. (2.5)/(2.7)/(3.14) omit the background screening 1/κ² of a total-charge (dark-photon) coupling; rate ratio κ² = 1600 at their benchmark.** The anisotropic κ must enter as q̂·κ·q̂ | D |
| Dopants / NV (G12) | Formula [6.1]–[6.4]: dilute defects, host-screened transition densities, and the Franck–Condon ZPL + sideband. This is WP0 Theorem D for a localised gapped centre. Codes and specification are given | D + spec |
| Exothermic into collective modes (gap) | [7.2]: Γ_ν = (m_χ q_ν*/πΩ)⟨𝔇\|ℱ_ν(q*)\|²⟩, q_ν* = √(2m_χ(\|Δ_χ\| − ω_ν)). The signal is lines at mode energies on the shell \|q\| = q*. It is halo-independent to O(v/v*) | D |
| WP0 defects | 6 items (§8). Hyperfine factor 2 and sign; Theorem D excludes all gapless WP4 targets; the L15 pointer is non-conserving; the L16 pointer misses the background κ | D |

---
## 1. Broken-symmetry reference states in the URF

**(1.1) [D]** WP0 §1.2 already places magnetic order and superconductivity in the *reference state*, not in H. Hypotheses:
- (R1) the Gibbs state is replaced by a symmetry-broken state, selected by an infinitesimal field. WP0 (3.1)–(4.6) only need
  stationarity, so they hold unchanged;
- (R2) a mean-field quasiparticle basis (spin-wave bosons or Bogoliubov fermions) diagonalises the quadratic part of H;
- (R3) the response is computed in a **conserving** approximation (Baym–Kadanoff): the vertex is derived from the same functional as
  the self-energy. Under (R3), WP0 (4.6) (f-sum) and WP0 (4.8) (Ward) are preserved order by order. A bare bubble in a broken-symmetry
  basis violates them (§4.2, K2).
**(1.2) Low-energy projection [D].** Let 𝒫_L project onto the low-energy manifold: the spin multiplets of a Mott insulator, or the
Bogoliubov sector |ξ| ≲ ω_c of a superconductor. For ω below the gap to the complement (the charge gap Δ_c, or ω_c ≫ Δ):
  S_ab(q,ω) = S_ab[𝒫_L O_a 𝒫_L, H_L](q,ω) + O((ω/Δ_c)·w_⊥),                                                                          [1.1]
where H_L is the Schrieffer–Wolff effective Hamiltonian and w_⊥ is the spectral weight of O_a outside 𝒫_L. The projected operator
carries form factors: for a magnetic ion, 𝒫_L s_e(q)𝒫_L = Σ_{lj} e^{iq·x_lj} F_j(q) λ_{S,j} S_lj, with F_j(q) = ∫d³r e^{iq·r} ρ^s_j(r)/(2S_j)
the normalised spin density of the magnetic orbitals.

**(1.3) Spectral budget [E].** The spin f-sum WP0 (4.6e), M¹_{szsz} = n_e q²/4m_e, is shared between the low-energy (magnon) sector and
the electronic interband sector. The magnon share is the Hohenberg–Brinkman exchange moment, ~ zJS²(qa)² per magnetic site. Their ratio
is ~ 4zJ S² m_e a² (n_mag/n_e). For J ≈ 10 meV and a ≈ 4 Å this is ≈ 2% × zS²n_mag/n_e. Magnons therefore carry a small share of the
spin weight, and WP0 (9.2 v) L17′ bounds on the spin channel are loose for magnon targets unless restricted to the projected manifold.

---
## 2. Magnetic targets

### 2.1 L13: magnon rate (1905.13744; 2009.13534)

**Source formulas (FT).**
- 1905.13744 Eq. (5): ℳ_{ν,k}(q) = δ_{q,k+G} (1/√N Ω) Σ_α ⟨s_f|Ô^α_χ(q)|s_i⟩ ε^α_{ν,k,G}.
- 1905.13744 Eq. (6): ε_{ν,k,G} = Σ_j √(S_j/2)(V_{jν,−k} r_j* + U*_{jν,k} r_j) e^{iG·x_j}.
- 1905.13744 Eqs. (9)–(10): R = (ρ_χ/ρ_T m_χ)∫d³v f Σ_ν Σ_k Γ_{ν,k}, with Γ = 2πΣ_{q=k+G} \|ℳ\|²δ(E_i − E_f − ω_{ν,k}).
- 1905.13744 Eq. (12): R ≃ (n_s/ρ_T)(ρ_χ/m_χ)∫d³v f ∫ d³q/(8π²) tr(ρ̂_χ Ô⁺Ô^{†−}) δ(⋯) (one-sublattice FM).
- 2009.13534 Eq. (38): Γ(v) = (1/Ω)∫d³q/(2π)³ Σ_ν 2πδ(ω_{ν,k} − ω_q) ½\|Σ_j e^{iG·x_j⁰}√S_j(U*_{jν,k} r_j + V_{jν,−k} r_j*)·f_j(−q,v)\|².
- 2009.13534 Eq. (34) gives f_j: the EFT coefficients c_{3a,4,6,7a,9,10,12a–15a} with weight λ_{S,j}, plus the orbital terms with λ_{L,j}.

**Truncation chain from WP0 (3.3) [D].**
1. Operator restriction. 𝔇_ab is non-zero only for the spin row a = (e,b) of WP0 (2.2), plus the orbital density if λ_L ≠ 0.
   Matching WP0 (2.3) maps 𝒱_{s^b} ↔ f_j^b/λ_{S,j}.
2. Clamped nuclei (n_B = 0). Phonons enter only through §2.3.
3. Projection [1.1] onto the ground multiplet of each ion (Mott gap Δ_c; YIG Δ_c ≈ 2.8 eV [E]). H_L is the spin Hamiltonian, and
   s_e^b(q) → Σ e^{iq·x_lj}F_j λ_{S,j}(R_j S′_lj)^b, with R_j the local frames of 2009.13534 Eq. (35).
4. **Dipole/contact form factor F_j(q) → 1.** This is the approximation both sources make.
5. Holstein–Primakoff to O(S^{1/2}): S′^+ ≈ √(2S) a and S′^− ≈ √(2S) a†. The spin operator is then linear in bosons.
6. Colpa/Toth–Lake Bogoliubov diagonalisation, T = 0.

The result is
  ⟨ν,k|s^b(q)|0⟩ = √N E^b_ν(q) δ_{q,k+G},   E^b_ν(q) = Σ_j λ_{S,j}F_j(q) e^{iG·x_j} √(S_j/2) (U*_{jν,k} r^b_j + V_{jν,−k} r^{b*}_j),            [2.1]
  S_ab(q,ω) = (2π/Ω) Σ_ν E^{a*}_ν E^b_ν [(n_ν+1)δ(ω − ω_{νk}) + n_ν δ(ω + ω_{νk})].                                                       [2.2]
Inserting this in WP0 (3.3) gives Σ_ab 𝔇_ab S_ab = (2π/Ω)Σ_ν ⟨\|Σ_b 𝒱_b E^b_ν\|²⟩_{DM spin}δ. At F_j = 1 and n_ν = 0 this is 2009.13534 Eq. (38)
term by term, and 1905.13744 Eqs. (5)–(10) after Σ_k → NΩ∫d³k/(2π)³ (1/√N Ω from V^{-1}√N, with V = NΩ). For n = 1, U = 1, V = 0 and
r = (1,i,0): Γ = (n_s/8π²)∫d³q \|O⁺\|²δ, i.e. 1905.13744 Eq. (12) (check K6).

**Validity [D/E].**
- (a) ω ≪ Δ_c.
- (b) q ≲ q_F, where \|F_j(q)\|² ≳ 0.9. For Fe³⁺ 3d this is q ≲ 1 Å⁻¹ ≈ 0.2 keV [E]. 1905.13744 itself notes the breakdown "beyond
  10 MeV" (q ≳ inverse ionic radius).
- (c) 1/(2S) ≪ 1: 0.2 for S = 5/2 (YIG) and 0.5 for S = ½ (α-RuCl₃, where LSWT is only qualitative). (d) T ≪ ω_thr, and T ≪ T_N (560 K for YIG).
- (e) A commensurate order (2009.13534 assumes this).
- (f) SOC small enough that R̃_{s,c} ≈ 0. Otherwise the spin coupling is Coulomb-screened by WP0 (5.3), at relative order
  (λ_SO/Δ_CF)² [E].
These items are not Si/Ge numbers: Si/Ge are non-magnetic, and L13 does not apply to them.

**Leading corrections [D for the form; E for size].**
- (i) Form factor: multiply [2.1] by F_j(q). For Fe³⁺, ⟨j₀⟩ ≈ 0.7 at q ≈ 2.5 Å⁻¹ ≈ 0.5 keV, so the rate suppression \|F\|² ≈ 0.5 [E].
  The suppression grows rapidly at m_χ ≳ 0.3 MeV, where q_max ≈ 2m_χ v ≳ 1.5 keV. This is the dominant correction.
- (ii) Two-magnon, O(1/2S): [2.4]. (iii) Magnon–phonon hybridisation near crossings: [2.5].
- (iv) For SOC ions, λ_L terms and non-dipole orbital form factors.

**Discrepancies found in the sources.**
- 2009.13534 Eq. (36) labels the Holstein–Primakoff operators S′^x = (2S − a†a)^{1/2}a and S′^y = a†(2S − a†a)^{1/2}. These are S′^±,
  since S′^x must be Hermitian. Eq. (38) is consistent with the ± reading, so this is notational only.
- Halo conventions differ from NOTATION: ρ_χ = 0.3 GeV/cm³, v₀ = 220, v_esc = 500, v_E = 240 km/s (1905.13744).
**Status: DERIVED.**

### 2.2 Two-magnon continua (catalog §12.6 gap)

**[D]** Hypotheses: LSWT reference (steps 1–4 and 6 of §2.1), with HP kept to the next order. The longitudinal local component
S′^z_lj = S_j − a†_lj a_lj is bilinear in bosons. The transverse components are odd in bosons (one or three magnons). So at
O(S⁰) the two-magnon amplitude is purely longitudinal:
  ⟨νk₁; ν′k₂| s^b(q)|0⟩ = −δ_{k₁+k₂,q+G} Σ_j λ_{S,j}F_j(q) e^{iG·x_j} R_j^{bz} [U*_{jν,k₁}V_{jν′,−k₂} + U*_{jν′,k₂}V_{jν,−k₁}]/√(1+δ_{νk₁,ν′k₂}),     [2.3]
  S^{(2m)}_ab(q,ω) = (2π/V) Σ_{k₁,ν≤ν′} 𝒜^{a*}𝒜^b δ(ω − ω_{νk₁} − ω_{ν′,q−k₁}),   𝒜^b ≡ the amplitude [2.3].                         [2.4]
Properties:
- (a) For a Heisenberg FM, V ≡ 0, so S^{(2m)} ≡ 0 at T = 0. This is consistent with conservation of total S^z (K10).
- (b) For AFM/ferri, \|UV\| = O(1) while the one-magnon weight is ∝ S. The ratio is therefore O(1/2S): 0.2 for YIG and 0.5 for S = ½ [D].
- (c) The continuum at fixed q spans ω ∈ [min_k(ω_k + ω_{q−k}), 2ω_max]. A DM with ω ≤ qv can therefore deposit ω ≫ ω_ν(q) at small q,
  which one magnon cannot do.
- (d) At T > 0, the difference process (b†b, absorbing a thermal magnon) adds weight ∝ n_ν [D].
- (e) Sum-rule check: the one-magnon + two-magnon weight reproduces ⟨S²⟩ = S(S+1) per site at O(S⁰).

*Leading correction:* the magnon–magnon final-state interaction, O(1/S²) relative; it gives two-magnon bound states in anisotropic
magnets [C].

**Computation specification.**
- Inputs: J_ij, anisotropy and DMI from DFT+U (QE or VASP; four-state energy mapping or TB2J), and F_j(q) from Wannier projection of the
  DFT spin density.
- Diagonalisation: Colpa/Toth–Lake (SpinW algorithm) on a k-grid.
- [2.4] is a single k-sum per (q, ν, ν′). Cost ∝ N_k n² per q (YIG: n = 20, N_k = 40³ gives ≈ 3×10⁷ operations per q, negligible).
- Convergence: the ⟨S²⟩ sum rule to 1%. Output: S^{(2m)}_ab(q,ω) tables. New module of about 300 lines on top of the LSWT code of
  1905.13744 and 2009.13534.
### 2.3 Magnon–phonon coupling

**[D]** Expand the exchange to first order in the displacements: H_mp = Σ_{ij,κα} (∂J_ij/∂u_κα) u_κα S_i·S_j. In LSWT plus harmonic phonons
this is a quadratic boson form in Ψ = (a_k, b_k, a†_{−k}, b†_{−k}). Colpa diagonalisation with metric diag(1,1,−1,−1) gives hybrid modes
λ with magnon content X^m_λ and phonon content X^p_λ. Then
  S_ss(q,ω) ⊃ (2π/Ω)Σ_λ \|Σ_ν X^{m}_{λν} E_ν(q)\|²δ(ω − ω_λ),   S_NN(q,ω) ⊃ (2π/Ω)Σ_λ \|Σ_ν X^{p}_{λν} ℱ^{ph}_ν(q)\|²δ(ω − ω_λ),      [2.5]
and the cross term S_sN ≠ 0 enters WP0 (3.3) when 𝔇_{sN} ≠ 0 (DM coupling to both spin and nucleons). Away from crossings the mixing is
g_mp/\|ω_m − ω_ph\| [D]. The parametric suppression q²/(m_ion ω) of phonon excitation by spin couplings (2009.13534 §II.3, FT) is the
off-resonant limit of [2.5].

*Specification.* ∂J_ij/∂u from finite displacements: phonopy displacements of a DFT+U supercell, re-extracting J at each.
- Cost: 6N_atom supercell calculations. NiO (4-atom AFM cell): ~10³ CPU-h. YIG (80 atoms): ~10⁵ CPU-h [E].
- Phonons from phonopy/DFPT. The output is hybrid ω_λ, X^{m,p}, entered into [2.5].
- Convergence: the mixing at crossings, stable to 5% under the supercell size.

---
## 3. Chiral and circular-dichroism responses (catalog §12.6 gap)

**(3.1) Reciprocity theorem [D].** Hypotheses: unpolarised DM, density coupling only (𝔇 = \|Ṽ\|²), Born. Relabel q → −q in WP0 (3.3).
Then
  Γ(v) − Γ(−v) = ∫d³q/(2π)³ \|Ṽ(q)\|² [S(q,ω_q) − S(−q,ω_q)],   ω_q = q·v − q²/2m_χ.                                                  [3.1]
Time reversal maps n(q) → n(−q) and leaves the Gibbs state invariant, so S(q,ω) = S(−q,ω). Inversion gives the same. So **a v-odd rate
(a modulation term that is odd under reversal of the DM wind) requires both P and T broken**: magnetoelectric or noncentrosymmetric
magnets. The odd part is the q-linear nonreciprocal (magnetochiral) response
  S(q,ω) − S(−q,ω) = 2 q·𝐠(ω) + O(q³),   𝐠 a polar, T-odd vector (axial × polar order parameters).                               [3.2]
**(3.2) Chiral, T-even targets [D].** Here S_nn is reciprocal, so only operator interference survives. Write 𝔇 = 𝔇^S + i𝔇^A and
S = S^S + iS^A, with real symmetric and real antisymmetric parts. Then tr(𝔇S) ⊃ −Σ 𝔇^A_ab S^A_ab. Natural optical activity is the
antisymmetric current response S^A_{j^aj^b} = ε_abc q^c γ(ω) + O(q³), which is P-odd and T-even. With WP0 (2.3), the products that give
𝔇^A_{j^aj^b} ∝ ε_abc q^c after the DM-spin trace are O₅ × O₈ interference (𝒱^{(5)}_{j^d} = −iε_{acd}S_χ^a q^c/m_e and
𝒱^{(8)}_{j^e} = −S_χ^e, giving tr(S^aS^e) = δ_ae/4). Hence
  Γ_R − Γ_L = −2∫d³q/(2π)³ (q²/2m_e) Re(c₅*c₈)/(4m_χm_e)² γ_R(q,ω_q) × (1 + O(q²)),   γ_L = −γ_R.                                   [3.3]
Since O₈ is P-odd and O₅ is P-even, **an enantiomer difference measures P-violating DM interactions** (for example an anapole plus a
magnetic dipole). Spin analogue: chiral phonons (2301.07617, 2511.20461 [ABS]) enter as an antisymmetric spin–lattice response
S^A_{s,κ}, contracted with 𝔇^A_{s,n} from O₁ × O₃ interference (∝ i(q × v_χ)). This needs SOC [D].

**Specification.**
- (i) Nonreciprocal S: noncollinear-SOC DFT (QE), then RPA+LFE response at ±q (Yambo, or an EXCEED-DM-type IP code). Cost 2× the
  anisotropic tables of G11. Output: the odd part [3.2] per q-direction.
- (ii) Optical activity: γ(ω) at linear q from DFPT natural optical activity (ABINIT; Zabalo–Stengel formalism) [E for availability].
  Finite-q γ(q,ω) beyond linear order is an exact remaining gap (RG4).
- Convergence: the odd part must vanish to numerical noise in a centrosymmetric control (Si).

---
## 4. Superconductors and thin films

### 4.1 L15: source formulas (FT)
- 2609.06423 Eq. (6): T-matrix element ∝ (u_{p₁}v_{p₂} + v_{p₁}u_{p₂}) V^{χe}.
- 2609.06423 Eq. (7): Π_QP(Q,ω) = (1/2V)Σ_p (1 − (ε_pε_{p+Q} − Δ²)/(E_pE_{p+Q}))[1/(ω − E_p − E_{p+Q} + i0⁺) − 1/(ω + E_p + E_{p+Q} − i0⁺)].
- 2609.06423 Eq. (8): ε_BCS = 1 − (4πα/Q²)Π_QP. 2609.06423 Eq. (9): Γ = ∫dω∫_{Q⁻}^{Q⁺} Q³dQ/(2π)³ \|V^{χe}\|²/(α v_χ) · Im ε_BCS/\|ε_BCS\|².
- 2101.08263 Eq. (1): Γ = ∫d³q/(2π)³ \|V\|²[2(q²/e²) Im(−1/ε)]. 2101.08263 Eq. (3): ε_RPA ≈ λ_TF²/2q² + i 3πω_p²ω/(2q³v_F³).
- 2101.08263 Eqs. (S.13)–(S.16): Lindhard with ω → ω + iΓ_p, and the "causal" branch. 2101.08263 Eq. (S.30): S = (2q²/e²) Im ε.
- 1512.04533 Eq. (11): S(E_D,q) = 2∫d³p₂d³p₄(2π)⁴δ⁴(⋯)f₂(1 − f₄). 1512.04533 Eq. (12): S = (m_e²T/π\|q\|)[z/(1 − e^{−z})](1 + ξ/z).
- 1512.04533 Eq. (14): S ≃ (m_e²E_D/π\|q\|)Θ(\|q\|v_F − \|E_D\|).

### 4.2 Truncation chain and the conserving response [D]

1. WP0 (3.3) with a single density operator, then WP0 (5.4)/(5.5) at clamped nuclei. This holds for a dark photon (total charge), and
   for electron-only coupling at ω ≫ ω_D (up to O(κ_BO⁴)). The ions enter only through pairing.
2. Reference state: Nambu–Eliashberg with Δ(iν) from α²F and μ*. BCS limit: Δ constant, λ_ep T_c/ω_D → 0, ω ≪ ω_D.
3. **Conserving response (R3).** Coulomb RPA together with the pairing-channel ladder (generalised RPA):
  R̃^{GRPA}_ρρ(q,ω) = Π₃₃ + Π₃₂ [Π₂₂(0,0) − Π₂₂(q,ω)]^{-1} Π₂₃ (+ amplitude channel Π₃₁…, zero under particle–hole symmetry),
  ε(q,ω) = ε_bg − v_q R̃^{GRPA}_ρρ,   S_ee = (2q²/e²)(1 − e^{−βω})^{-1} Im[−1/ε].                                                  [4.1]
  Here Π_ij = −TΣ_ν V^{-1}Σ_k tr[τ_iG(k+q,iν+iΩ)τ_jG(k,iν)] is continued as iΩ → ω + i0, and Π₂₂(0,0) = 2/g by the gap equation
  (Goldstone).
   - **Check K2:** at q = 0 per k, Π₃₃ = 4Δ²/(E(4E² + Ω²)), Π₃₂ = −2ΔΩ/(E(⋯)) and Π₂₂ − Π₂₂(0) = −Ω²/(E(⋯)). So R̃^{GRPA}(0,ω) ≡ 0
     after the k-sum, for any ω. The bare Π₃₃(0,ω) ≠ 0.
   - **The bare bubble 2609.06423 Eq. (7) therefore violates particle conservation.** Its coherence factor tends to Δ²/E² ≠ 0 at
     Q → 0 (K3). This gives a spurious 1/Q² term in ε_BCS and pair-breaking weight at ω > Qv_F. That weight is the "Im ε_BCS
     finite above the red curve" region of their Fig. 2, which in the conserving theory is suppressed by (Qv_F/ω)² [E].
   - The DM region (ω < qv_χ < qv_F) never enters that region, so their DM conclusion stands. The vertex correction there is
     O(Δ²/(v_Fq)²) ≤ (v_χ/2v_F)² ≈ 0.5–4% for Al [E] (formula [4.1]; magnitude not computed: RG1).
4. Drop the pairing vertex: [4.1] → 2609.06423 Eq. (8).
5. Δ → 0: Lindhard (2101.08263 S.13 with Γ_p → 0), on the retarded branch. T → 0 and the free gas then give 2101.08263 S.34 =
   1512.04533 Eq. (14) through S.30. That relation is WP0 (4.1) at T = 0. At T > 0, 1512.04533 Eq. (12)'s factor z/(1 − e^{−z}) is exactly
   (1 − e^{−βω})^{-1} of WP0 (4.1) [D].
6. ω ≪ qv_F and q ≪ k_F give 2101.08263 Eq. (3), with Re ε = **λ_TF²/q²** (K1: the Lindhard bracket → 1).

**(4.3) DM-region closed form [D].** Hypotheses:
- clean; T = 0; quasiclassical (Δ/E_F → 0; N(ξ) constant over ω); bare or GRPA bubble (they are equal to O(Δ²/v_F²q²));
- 2Δ < ω < qv_F − q²/2m_e, the Lindhard Q₊ < 1 region where all DM kinematics lies.

The constraint ξ′ − ξ = v_Fqμ + q²/2m is then satisfied for every pair (E, E′) with E + E′ = ω. The ξξ′ term of the coherence factor
averages out, and
  Im ε_SC(q,ω) = g_I(ω/Δ) Im ε_N(q,ω),   g_I(x) = (1/x)∫₁^{x−1}de [e(x−e)+1]/√((e²−1)((x−e)²−1));   Re ε_SC = Re ε_N[1 + O(Δ²/v_F²q²)].    [4.2]
g_I is the case-I (density) analogue of Mattis–Bardeen. The case-II function g_II (numerator e(x−e) − 1) equals the MB closed form
(1 + 2/x)E(k) − (4/x)K(k), with k = (x − 2)/(x + 2), to 10⁻⁶ (K4). Values: g_I(2⁺) = π/2 (a step), g_I(2.5) = 1.42, g_I(4) = 1.21,
g_I(5) = 1.15, g_I(10) = 1.05, g_I(100) = 1.001. So **rate_BCS/rate_Lindhard = g_I(ω/Δ)** in the DM region. This is the analytic form of the
"agreement for ω ≳ 5Δ" of 2609.06423 (15% at 5Δ). The same ξ-decoupling applies in the dirty limit (ℓ ≪ ξ₀), where it gives MB for the
transverse/absorption channel. **One mechanism, momentum relaxation on the scale of Δ (by Doppler v_Fq or by disorder), gives both g_I and MB [D].**

**Validity with numbers (Al: Δ = 0.17 meV, E_F = 11.7 eV, v_F = 6.8×10⁻³; WSi: Δ = 0.26 meV, E_F = 7.0 eV, as in 2609.06423).**
- v_χ/v_F ≤ 0.38, so the region ω < qv_F always holds. q ≥ 2Δ/v_max ≈ 0.13 keV ≪ k_F = 3.5 keV. Δ/E_F ≈ 1.5×10⁻⁵.
- T ≪ Δ: thermal quasiparticles are ∝ e^{−Δ/T} ~ e^{−200} at 10 mK. Clean limit: qℓ ≫ 1 (§4.5).
These are not Si/Ge items: Si/Ge are not superconductors.

**Leading corrections beyond L15 [D for the form; E for size].**
- (i) Non-thermal quasiparticles. Measured x_qp ~ 10⁻⁸–10⁻⁶ in Al films. Replace p_i by a generalised Gibbs state. This adds a sub-gap
  scattering channel ω < 2Δ with case-I factor ½(1 − Δ²/EE′), and the rate is ∝ x_qp. WP0 (4.1) then holds with f_qp in place of the
  Fermi function.
- (ii) Strong coupling: Δ(ω) complex (Eliashberg). This adds Holstein phonon-assisted absorption above 2Δ + ω_ph (the WP3 X+ analogue).
- (iii) Plasmon tail and GSRF local fields (2101.08263 S.19). These are a Mermin-type relaxation (§4.5); damped complex G violates
  positivity WP0 (4.4), as 2101.08263 itself notes (FT).
- (iv) The GRPA vertex [4.1].

**Discrepancies in the sources [D].**
- (a) 2101.08263 Eq. (3): Re ε should read λ_TF²/q², given their own S.14 (λ_TF = √3ω_p/v_F) and S.15 (K1). In the illustrative scaling
  W ~ ωq this is a factor 4. The numerics use S.13 and are unaffected.
- (b) 1512.04533 Eq. (13) [(3.3) in the arXiv PDF]: e₋ = (E_D − q²/2m)²/(q²/2m) should be (E_D − E_q)²/(4E_q) (K7; it agrees with
  2101.08263 S.34). This affects T > 0 and the edges, not the T → 0 limit Eq. (14).
- (c) 2609.06423 Eqs. (4)/(7) use −i0⁺ on the negative-energy pole. That is time-ordered, not retarded. It is harmless for ω > 0 at T = 0,
  but wrong for ω < 0, for KK, for sum rules and at T > 0.
- (d) 2101.08263 attributes W(q,−ω) = −W(q,ω) to causality. In the URF it follows from WP0 (4.3) together with inversion or T. Causality
  alone gives ε(q,−ω) = ε(−q,ω)*. In P- and T-broken superconductors (noncentrosymmetric, magnetic) it fails; see [3.1].
- (e) 2609.06423 Eq. (9) prefactor: consistent with WP0 (3.3) (K8).
**Status: DERIVED** (the step to a conserving theory, and the leading-correction sizes, are E).

### 4.4 The branch cut / causality issue (2101.08263) [D]
WP0 (4.1)–(4.2) fix the analytic structure without complex logarithms:
- Im ε(q,ω) = −v_q Im R = (v_q/2)(1 − e^{−βω})S(q,ω), with S ≥ 0 a phase-space integral (S.31/S.34); Re ε = 1 + KK[Im ε], with R^∞ = 0 for density.
The "acausal branch" of the earlier work corresponds to a non-retarded continuation, analogous to (c) above. Its rate is off by up to 10⁷
(2101.08263 SM, FT) because it puts negative-frequency weight at ω > 0. The ω + iΓ_p prescription of S.13 is **not conserving**. The
conserving relaxation form is Mermin's [4.3].

### 4.5 Film geometry and disorder (G9)

**[D, relaxation-time approximation]** Mermin's conserving relaxation, with γ = 1/τ:
  ε_M(q,ω) = 1 + (ω+iγ)[ε_L(q,ω+iγ) − 1] / {ω + iγ[ε_L(q,ω+iγ) − 1]/[ε_L(q,0) − 1]}.                                                 [4.3]
For ω ≪ γ (DM: ω ~ meV against γ ~ 0.1 eV in films), with q ≪ k_TF, the two limits are:
- diffusive (qℓ ≪ 1): W = 3ω/(k_TF²v_Fℓ). This is exactly the Drude result ωγ/ω_p² (since k_TF²D = ω_p²/γ); ballistic (qℓ ≫ 1): W = πωq/(2k_TF²v_F).
So
  W_M/W_Drude → 1 (qℓ ≲ 1),   → πqℓ/6 (qℓ ≫ 1).                                                                               [4.4]
- QROCODILE's Drude ε for WSi (2412.16279, via catalog-analysis G9) is the qℓ ≲ 1 limit of the URF. It **underestimates** the scattering
  W by πqℓ/6 at DM momenta. For an amorphous WSi with ℓ ≈ 0.3–1 nm and q = 1–5 keV, qℓ ≈ 1.5–25 [E]. The shift is conservative
  for the limit, of order 1–10.
- For Al films (ℓ ≳ 10 nm), qℓ ≳ 50 and Lindhard holds.
- BCS: [4.2] applies with ε_N → ε_M. In the dirty regime the ξ-decoupling holds independently of v_Fq (Anderson theorem for Δ).

**Film geometry [D for independent electrons in a slab; C with images].** The DM states are plane waves, so the golden rule needs only the
diagonal S(q,q;ω). For a slab of thickness d:
  S_film(q_∥,q_z,ω) = ∫(dq′_z/2π) d·sinc²[(q_z−q′_z)d/2] S_bulk(q_∥,q′_z,ω) + S_surf,                                                 [4.5]
with S_surf the image/surface-mode term (specular-reflection model). The relative correction is O(1/qd) [E]: 10% at q = 0.2 keV and
d = 10 nm, and ≲ 2% for q ≳ 1 keV. Surface plasmons (ω_p/√2 ≈ 10 eV) lie outside DM kinematics.

### 4.6 Quasiparticle generation (G9, measured signal; WP5 hand-over) [D for the seed; spec for the cascade]

The prompt final state Λ = (E₁, E₂) of WP0 (7.1). From [4.2] at fixed (q,ω):
  P(E₁|ω) = [E₁E₂ + Δ²]/[√(E₁²−Δ²)√(E₂²−Δ²)] / [ω g_I(ω/Δ)],   E₂ = ω − E₁,   E₁ ∈ [Δ, ω−Δ].                                          [4.6]
The cascade uses the Chang–Scalapino/Kaplan kinetic equations with coherence factors:
- QP scattering: (1 − Δ²/EE′); recombination and pair-breaking: (1 + Δ²/EE′); kernels α²F(Ω) from EPW (Al: fine grids 60³/30³, ~10³ CPU-h);
- phonon escape into the substrate by acoustic mismatch, with transmission η_esc as input.
Outputs: the pair-breaking efficiency η_pb(ω) = 2ΔN_qp/ω, its variance (the QP Fano factor), and the time constants. Convergence: energy
grid ≤ Δ/20; energy conservation of the closed system to 10⁻⁴. The interface transmission is phenomenological (RG7).

---
## 5. Dirac and narrow-gap materials: L16

**Source formulas (FT).**
- 2101.08263 Eq. (4): W_Dirac = (e²/12πκ²v_F)Θ(ω − v_Fq)Θ(ω_max − ω).
- 2101.08263 SM §F: Im ε_Dirac = (e²/12πv_F)√(1 − 4Δ²/s)(1 + 2Δ²/s)Θ(s − 4Δ²), with s = ω² − v_F²q², and W = that/κ².
- 1708.08929 Eq. (2.6): (ε_r)_Dirac = 1 + (e²g/4π²κv_F)∫₀¹dx x(1−x) ln[(2v_FΛ)²/(Δ² − x(1−x)s)] + i(e²g/24πκv_F)√(⋯)(⋯)Θ(⋯).
- 1708.08929 Eq. (3.7): ⟨\|ℳ\|²⟩ ≃ 16m_e²m_χ²g_D²e²ε²/((q² − m_{A′}²)²\|ε_r\|²). 1708.08929 Eq. (3.11): F_med = 1/ε_r, with σ̄_e defined in vacuum.
- 1910.02091 Eqs. (2.5)/(2.7): F_med = q²/(q² − Π⁰⁰). 1910.02091 Eq. (3.13): Π_ii/κ → Π_ii/κ_ii.
- 1910.02091 Eq. (3.14): F_med = [1 + (q_x²v_{F,z}²/κ_xx + q_y²v_{F,y}²/κ_yy + q_z²v_{F,z}²/κ_zz)π(q̃²)/q²]^{-1}.

**Truncation chain from WP0 [D].**
1. WP0 (3.3) with a density coupling, then WP0 (5.3)/(5.4): S = (2q²/e²)Im[−ε^{-1}] with the **total** ε (dark photon). For an electron
   scalar at clamped nuclei it is the same, by WP0 (5.5).
2. Clamped nuclei. For ω above the polar-phonon band this holds to O(κ_BO⁴). Otherwise κ → κ(ω) includes the ionic poles.
3. Split R̃ = R̃_D + R̃_bg: the Dirac bands within the cutoff Λ, plus all remote bands. For ω ≪ E_bg (remote gap) and q ≪ 2π/a,
   1 − v_qR̃_bg(q,ω) → κ (a static, local background; LFE neglected).
4. Two-band k·p to O(k): the massive Dirac Hamiltonian with v_F and Δ.
5. R̃_D at the IP (= RPA) level, T = 0, μ in the gap.
6. Isotropy.

The result is
  ε = κ − v_qR̃_D = κ ε_r,   ε_r = 1 + δε_D/κ,   W = Im δε_D/\|κ + δε_D\|²  →(\|δε_D\| ≪ κ)  Im δε_D/κ²,                                     [5.1]
with Im δε_D = (e²g/24πv_F)√(1−4Δ²/s)(1+2Δ²/s)Θ(s−4Δ²). For g = 2 and Δ = 0 this is e²/12πv_F (check K5: a direct two-band Lindhard
integral). Hence 2101.08263 Eq. (4) and its gapped SM form, **exactly** [D].

**The κ² discrepancy [D].**
- 1708.08929 and 1910.02091 use F_med = 1/ε_r = κ/ε, with σ̄_e in vacuum. Their rate is therefore κ² times [5.1] for the same Dirac
  model. That is the rate for a DM coupled *only* to the Dirac bands' charge: then R_DD = R̃_D κ/ε, so S ∝ Im[R̃_D/ε_r]
  (WP0 (5.3), rank one).
- A kinetically mixed dark photon couples to all charges. The remote-band polarisation screens the DM–electron potential by 1/κ, as for
  any test charge in a dielectric. The κ²-free form is outside the URF for a dark photon or an electron scalar.
- The κ² growth of 1708.08929 Eq. (3.14) (∝ κ²v_F²I) is an artefact: there the "1" of ε_r is absorbed into Λ′ = Λexp(12π²κv_F/ge²).
- Benchmark (κ = 40, v_F = 4×10⁻⁴, g = 2): rate ratio κ² = 1600. 2101.08263 Eq. (4) agrees with the URF.

**Anisotropy [D].** The background enters the longitudinal ε as q̂·κ·q̂, not term by term inside Π⁰⁰:
  ε(q,ω) = q̂·κ·q̂ − v_q R̃_D(q̃,ω),   R̃_D ∝ (Σ_i q_i²v_{F,i}²)π(q̃²)/(v_{F,x}v_{F,y}v_{F,z}) (no κ inside).                          [5.2]
1910.02091 Eq. (3.14) equals κ_eff/ε only for isotropic κ, and contains a typo (q_x²v_{F,z}² for q_x²v_{F,x}²). For ZrTe₅, the clamped-ion
κ = (187.5, 9.8, 90.9) (1708.08929 Table, FT). The background alone gives a directional rate ratio (κ_xx/κ_yy)² ≈ 370 between q ∥ x and
q ∥ y, before the Dirac anisotropy. This is a large daily-modulation lever arm that the harmonic mean (1708.08929) or the per-component
rule (1910.02091) misrepresent [D for the structure; E for the impact].

**Validity with numbers.** Benchmark: Λ = 0.2 keV, v_F = 4×10⁻⁴, κ = 40.
- q ≤ Λ (0.2 keV), and ω ≤ ω_max ≈ 2v_FΛ ≈ 0.16 eV. α̃ = αg/κv_F = 0.91 (benchmark), which is marginal for RPA. |μ| < Δ and T ≪ Δ.
- ω ≪ E_bg, and q ≪ 2π/a for κ(q) ≈ κ(0).
Si/Ge are not Dirac materials, so L16 has no Si/Ge numbers. The narrow-gap generalisation is the Kane model: the 2-band Dirac form is
its limit with v = √(E_g/2m*), and remote (split-off) bands correct it at O(E_g/Δ_SO) [D].

**Leading corrections [D for the form; E for size].**
- (i) Charge renormalisation: Re δε_D/κ = (α̃/6π)ln(4Λ²v_F²/s), about 0.26 at √s = 10 meV. This is a ≈ 50% rate correction, and
  [5.1] must keep it, not set ε ≈ κ.
- (ii) Excitonic (BSE rung): near 2Δ the Sommerfeld factor πη/(1 − e^{−πη}), with η = α/(κv_Fβ) and β = √(1 − 4Δ²/s). This is
  O(1) near threshold.
- (iii) Dynamic ionic background κ(ω) near polar phonons.
- (iv) Doping (μ ≠ 0): an intraband Lindhard term with k_TF² = e²N(μ)/κ, which removes the weak-screening advantage for ω ≲ v_Fk_F.
- (v) Band curvature beyond Λ.
**Status: DERIVED.**

---
## 6. Dopants and colour centres as final states (G12, electronic/dopant part)

**[D]** Hypotheses:
- dilute, uncorrelated centres, n_D a*³ ≪ 1 (Si:P: a* ≈ 2–2.5 nm [E], so n_D ≪ 10¹⁹ cm⁻³; below the metal–insulator transition);
- host screening dominates (defect weight ≪ host); the centre is non-degenerate and gapped, so WP0 Theorem D (H2) holds locally.

Per centre, with WP0 (7.2) RPA+LFE external screening:
  S^D_ab(q,ω) = n_D Σ_f 2π ⟨i|Õ_a(q)†|f⟩⟨f|Õ_b(q)|i⟩ δ(ω − E_f + E_i),   ñ(q) = Σ_G (ε_host^{-1})_{G0}(q,ω) n(q+G),                          [6.1]
with Õ = O for spin and transverse operators (WP0 (5.3)).

- *Shallow donor, effective mass, single valley.* Plane-wave final states give
  \|⟨k|e^{iq·r}|1s⟩\|² = (64π a*³/V)/[1 + \|k−q\|²a*²]⁴ × S_C(k),   S_C = 2πζ/(1 − e^{−2πζ}),   ζ = m*α/(ε₀ k)  (Coulomb final state).   [6.2]
  - Multivalley: ψ = Σ_v α_v F_v(r)φ_{k_v}(r). Intervalley (g/f) terms sit at q ≈ k_v − k_v′ (keV scale) and are reachable by MeV DM.
  - Kinematics for Si:P (E_b = 45.6 meV): m_χ ≥ 2E_b/v_max² ≈ 13 keV, and q_min ≈ E_b/v_max ≈ 18 eV ~ 1/a* ≈ 80 eV [E]. The
    form factor is well matched.
  - Screening ε₀(Si) = 11.7 gives a 1/137 suppression for density coupling.
  - Ge donors: E_b ≈ 10–13 meV and a* ≈ 4–6 nm [E].
- *Deep centre (NV⁻ in diamond).* Adiabatic Condon approximation with the WP0 Theorem D X0/X+ sectors:
  S^{NV}(q,ω) = n_NV 2π\|⟨³E|ñ(q)|³A₂⟩\|² ∫(dt/2π) e^{i(ω−E_ZPL)t} exp{Σ_k S_k(e^{−iω_kt} − 1)},   E_ZPL = 1.945 eV.                       [6.3]
  - The ZPL weight is e^{−S_HR}, about 3–4% for S_HR ≈ 3.5 [E]. This is exactly the FC/DW reduction of WP0 SOTA terminology. The rest
    is the phonon sideband (X+).
  - The density operator conserves spin, so ³A₂ → ³E is allowed.
  - Spin couplings (O₄) drive m_s = 0 → ±1 within ³A₂ (2.87 GHz). Because s(q) ≠ total spin at q ≠ 0, ΔS = 1 triplet → singlet
    transitions are allowed, with amplitude ∝ (q·d) for transition-density size d [D].
  - Kinematics: m_χ ≳ 0.6 MeV, q ≳ 0.75 keV.
- *Leading corrections:*
  - Herzberg–Teller (∂ transition density/∂Q, as in D1 §4);
  - dynamic Jahn–Teller in ³E (E⊗e), which breaks [6.3]'s linear coupling;
  - central-cell/valley-orbit terms for shallow donors (EMT error ~ 10–30% in E_b for Si:P [E]).

**Computation specification.**
- *Shallow donors:*
  - multivalley EMT envelopes with a DFT central-cell correction, or a direct DFT supercell (QE, 512–4096 Si atoms; linear-scaling or
    unfolding);
  - ⟨f|e^{iq·r}|i⟩ through Wannier interpolation of the host conduction states on Δk ≲ 1/3a*;
  - host ε^{-1}_{G0}(q,ω ≈ E_b) from Yambo RPA+LFE.
  Cost ~10⁴ CPU-h. Convergence: E_b to 1 meV, and the q-integrated oscillator strength (a partial f-sum) to 2%.
- *NV:*
  - HSE supercell (QE or VASP, 512–1000 atoms), ΔSCF for ³E;
  - ΔQ and S_k from constrained relaxation plus supercell phonons (phonopy), with an Alkauskas-type generating function;
  - finite-q transition densities ⟨³E|n(q)|³A₂⟩ from Kohn–Sham orbitals;
  - singlets through quantum embedding (QDET/CRPA, WEST).
  Cost ~10⁵ CPU-h. Finite-q multiplet transition densities in embedding codes need a new module (RG5).
- *Outputs:* S^D(q,ω) tables per defect, and the rate per (n_D × mass).

---
## 7. Inelastic and exothermic DM into collective modes (catalog §9 I4 gap)

**[D]** WP0 (2.1) already contains Δ_χ, so only the kinematic evaluation is new. Take Δ_χ < 0 and a target mode with ω_ν(q) ≤ ω_max:
  ω = \|Δ_χ\| + q·v − q²/2m_χ = ω_ν(q)  ⇒  \|q\| = q_ν*[1 + O(v/v*)],   q_ν* = √(2m_χ(\|Δ_χ\| − ω_ν)),   v* = q*/m_χ.                        [7.1]
For v ≪ v* and ω_ν slowly varying on the shell, the Jacobian is ∫q²dq δ(⋯) = m_χq* (K9). Then
  Γ_ν = (m_χ q_ν*/πΩ) ⟨Σ_ab 𝔇_ab(q*) ℰ^{a*}_ν ℰ^b_ν⟩_{q̂ on the shell},                                                              [7.2]
where ℰ_ν = E_ν for magnons [2.1] and the phonon amplitude ℱ_ν = Σ_κ A_κF_κ(q)(2M_κω_ν)^{-1/2}e^{−W_κ}(q·e_κν)e^{iG·x_κ} for phonons (WP2).
- The deposited-energy spectrum is the mode spectrum on the sphere \|q\| = q* (mod G): a shell DOS, i.e. lines.
- The lines are Doppler-broadened only through ∂ω_ν/∂q·q*v/v* ≪ ω_ν.
- The rate per DM is v-independent at leading order, so the result is **halo-independent to O(v/v*)**.
- When q*²/2Mω̄ ≳ 1 (x_R of WP0 (6.1)), one-phonon is DW-suppressed and the full S_NN (multiphonon/impulse, WP2 L5–L6) must be used.
  Example: m_χ = 1 MeV and \|Δ_χ\| = 1 eV give q* = 1.4 keV ≈ the Si zone, one-phonon dominated [E]. Magnons are cut by F_j(q*).
- Endothermic (Δ_χ > 0) needs ½μv² > Δ_χ + ω_ν and is relevant only for Δ_χ ≲ meV×(m_χ/MeV).

*Specification.* A new kinematic module on top of PhonoDark-type one-phonon tables (WP2) and the magnon tables (§2):
- shell integration with Lebedev angular grids (≥ 590 points), converged to 1%; output dR/dω versus (m_χ, Δ_χ);
- the multiphonon branch reuses the WP2 S_NN.
The cost is negligible next to the response tables.

---
## 8. WP0 defects

- **D1. Hyperfine (WP0 (1.2) asked WP4 to fix the sign) [D].**
  - H_FC = −μ_e·B_contact with B_contact = (2/3)μ_N δ³(r) (HL, μ₀ = 1) and μ_e = −g_eμ_B s (g_e = +2.0023). This gives
    H_FC = **+**(2/3)g_eμ_Bg_Iμ_N s_i·𝐈_I δ³(r_i − R_I) = +(1/3)g_eμ_Bg_Iμ_N σ_i·𝐈_I δ³.
  - WP0 writes (2/3)…σ_i·𝐈_I, a factor 2 too large. The sign is positive with g_I carrying the sign of the nuclear moment.
- **D2. Theorem D (WP0 §6.2) hypothesis (H2) fails for every gapless WP4 target** (metals, superconductors and semimetals, where
  Δ_ad = 0 on the Fermi surface). In superconductors Δ ≪ ω_D, the reverse of the adiabatic hierarchy.
  - The decomposition for these targets must use quasiparticle-number sectors (Bogoliubov QPs and phonons, via Migdal–Eliashberg with
    small parameter ω_D/E_F ~ κ_BO²), not adiabatic projectors [D that (H2) fails; C for the replacement].
  - It does apply to magnetic insulators, gapped Dirac materials (if Δ ≫ ω_ph) and deep defects.
- **D3. L15 pointer (WP0 §9.3).** "RPA with coherence factors" must be the conserving GRPA [4.1]. The bare version violates WP0 (4.6) at
  q → 0 (K2).
- **D4. WP0 table 6.1, row "1/S, Δ/E_F".** The controlling parameters for superconductors are:
  - Δ/E_F (quasiclassical, ~10⁻⁵);
  - (T_c/ω_D)² ln (Eliashberg versus BCS);
  - 1/k_Fℓ (disorder; O(1) in amorphous WSi);
  - Δ/v_Fq (vertex correction, ≤ 0.2).
  For magnets: 1/2S, (t/U)², and the form-factor variable q·r_3d.
- **D5. L16 pointer.** "Low-energy Dirac H + RPA (5.4)" must include the remote-band background inside the total ε [5.1]. Otherwise it
  reproduces the κ² error of 1708.08929/1910.02091.
- **D6. WP0 (9.3)/(4.3), "with inversion or TR, L is odd in ω".** Correct, but WP0 does not flag the converse: P- and T-broken targets
  have nonreciprocal S and a v-odd rate [3.1]. This should be added to the L19 (anisotropy/modulation) pointer.
---
## 9. Exact remaining gaps

- RG1. The magnitude of the GRPA vertex correction in the DM region (the formula [4.1] is given; the estimate is ≤ 4% for Al, not
  computed).
- RG2. Amorphous films (WSi): the ab initio ε(q,ω) of the disordered film beyond the relaxation-time approximation, and Δ inhomogeneity
  (no first-principles route yet; a candidate is MD-quenched supercells of ≥ 500 atoms plus Kubo–Greenwood/RPA, with
  Bogoliubov–de Gennes on top).
- RG3. Two-magnon final-state interactions at O(1/S²), and bound states in anisotropic magnets.
- RG4. Finite-q optical activity γ(q,ω) beyond linear order. Existing DFPT gyrotropy is O(q).
- RG5. Finite-q multiplet transition densities for colour centres in quantum-embedding codes (a new module).
- RG6. Dirac targets at α̃ ≳ 1 (beyond one-loop RPA). The BSE/Sommerfeld rung is not computed.
- RG7. The phonon interface transmission η_esc in the QP cascade is phenomenological.
- RG8. Non-dipole orbital magnetic form factors for SOC ions (λ_L ≠ 0).

---
## 10. Literature (IDs verified against the arXiv API, 2026-10-31)
FT read: 1905.13744 (Eqs. 1–13); 2009.13534 (Eqs. 32–38); 1512.04533 (Eqs. 11–14; PDF Eq. 3.3); 2101.08263 (Eqs. 1–4, S.10–S.34,
SM §F); 2609.06423 (Eqs. 1–10); 1708.08929 (Eqs. 2.1–2.8, 3.2–3.14, A.8–A.9, κ table); 1910.02091 (Eqs. 2.1–2.18, 3.1–3.14).
Title check only: 2212.04504, 1901.07569, 2210.13516, 2301.07617, 2511.20461, 1004.0937, 2412.16279, 1504.07237, 2005.10256,
2501.18120, 2308.06314, 1604.06800, 2210.06490. PDFs/HTML deleted after reading. Neither a few lit.py searches nor the catalogs
(catalog-processes §12) found a DM calculation of two-magnon continua, a conserving BCS dielectric function, exothermic DM into
collective modes, or NV final states.

## 11. Symbols introduced/used
Conventions followed: q is transferred to the crystal; S_ab = (2π/V)Σ⟨i|O_a†|f⟩⟨f|O_b|i⟩δ (WP0 (3.1)); HL units, e² = 4πα; R (not χ) is the
retarded response. Halo: no rate was evaluated here. Halo values quoted from sources (§2.1) are the sources' own, flagged as deviating
from the campaign halo (2105.00599). Wherever a velocity integral appears, the isotropic factor is η(v_min)/(2q) (WP0 (9.1)).

| Symbol | Meaning | WP0 §10 status |
|---|---|---|
| S_ab, R_ab, R̃_ab, 𝔇_ab, 𝒱_a, ε, ε_e, L/W | as in WP0 | same. W ≡ the source's name for L (2101.08263); used only when quoting |
| s_e^b, n_e, j_e | electron spin density, density, current | same |
| Δ_χ | DM mass splitting (§7) | same |
| Δ | superconducting gap (half the gap for Dirac, as in the sources) | **NEW**. Collides in letter with WP0's retired "Δ = denominators". Proposal: Δ_sc and Δ_D if the reconciliation wants it unique |
| E_k, ξ_k, u_k, v_k | Bogoliubov energy, normal-state energy from E_F, coherence factors | **NEW**. v_k collides with velocity v; written only with a subscript k, following WP0's band-index rule |
| Π_ij, R̃^{GRPA} | Nambu bubbles (τ_i, τ_j); conserving density response [4.1] | NEW (Π ≡ R̃ at IP level, as in WP0) |
| g_I, g_II | case-I and case-II pair-breaking functions [4.2] | NEW |
| E^b_ν(q), ℰ_ν, ℱ_ν | one-magnon / collective-mode / one-phonon amplitudes | NEW (ℱ_ν follows the WP2 convention) |
| U, V (Bogoliubov), X^{m,p}_λ | Colpa blocks; hybrid-mode content | NEW. V collides with volume V; written only with indices |
| S_j, S′, R_j, r_j, λ_{S,j}, λ_{L,j} | ionic spin (bold in WP0 v2), local frame, as in 2009.13534 | spins should be bold **S** per WP0 §10; plain here in source quotes |
| F_j(q) | magnetic form factor | NEW. Distinct from F_DM, F^M_κ, F^Σ_κ |
| n_ν | Bose occupation of a magnon or hybrid mode | as for n_{Qν} |
| κ, κ_ij, ε_r = ε/κ, α̃ | remote-band background dielectric, relative permittivity, effective coupling | **NEW; κ collides with WP0 species index κ and with κ_BO**. Proposal: ε_bg, ε_bg,ij |
| v_F, k_F, λ_TF (= k_TF), ω_p, E_F, N(0) | metal parameters | NEW. v_F is subscripted, so no clash with v |
| γ = 1/τ, ℓ, D, ε_M, ε_L | relaxation rate, mean free path, diffusion constant, Mermin and Lindhard ε | NEW. τ collides with the truncation multi-index τ of WP0 (6.1); only γ is used in formulas |
| Λ | Dirac cutoff momentum | **collides with WP0 Λ (final-state class)**. Proposal: Λ_D |
| q_ν*, v* | exothermic shell momentum and velocity [7.1] | NEW |
| n_D, a*, S_HR, E_ZPL, S_k | defect density, effective Bohr radius, Huang–Rhys factor (WP0 v2 name), ZPL, mode Huang–Rhys | S_HR as in WP0 v2; S_k = per-mode S_HR |
| g (Dirac), g_s, g_C | spin × cone degeneracy | **collides with e–ph g_{mnν}**. Proposal: g_deg |
| 𝐠(ω), γ(ω) | nonreciprocal vector [3.2]; optical-activity scalar [3.3] | NEW. γ(ω) is distinct from γ = 1/τ only by its argument. Proposal: γ_OA |
