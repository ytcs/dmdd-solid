# R6 / WP4-v2: spin, superconducting and special targets (corrected standalone version)

Revision agent, brief R6/REV-WP4. Supersedes returns/R5/WP4.md (v1), which stays as the historical record. Applies every owed item of
state/CORRECTIONS.md §10 (WP4), the global renames of §0, the WP0-v2 interface flags addressed to WP4 (F5, F11), and the corrections found
in this revision (closing table, §13). Conventions: CONVENTIONS.md; symbols: NOTATION v4; architecture: returns/R6/WP0-v2.md, cited as
WP0-v2 (s.n). Checks: `code/WP4-v2/checks.py`: sympy only (exact algebra; `Integral.evalf` for 1-D quadratures), 23 checks, all PASS,
< 5 s; cited WP4v2-Kn (K1–K10 keep their v1 meaning). No numerical simulation was run.
Tags: **[D]** derived (hypotheses stated), **[D, sketch]**, **[E]** estimated, **[C]** conjectured; literature **[FT]** full text (read by
v1, 2026-10-31; not re-read here), **[ABS]** abstract/title. WP4 equations are **[s.n]** (v1 numbers kept; new ones appended).
Status: CLAIMED, pending R×2. The L16 ε_bg² statement against 1708.08929/1910.02091 is **not a claim** until the referee full-text check
(§5.3; CORRECTIONS §10, SOTA).

---
## 0. Results at a glance
| Item | Result | Tag |
|---|---|---|
| L13 magnons | 1905.13744 Eqs. (5)–(12) and 2009.13534 Eq. (38) follow from WP0-v2 (3.3) restricted to the spin row of WP0-v2 (2.2), by a 6-step chain (§2.1). Leading correction: magnetic form factor \|F^{mag}_j(q)\|² ≈ 0.5 at q ≈ 0.5 keV (Fe³⁺), set to 1 in both sources. Next: two-magnon, O(1/(2\|𝐒_j\|)) | D / E |
| Two-magnon | Closed-form longitudinal S^{(2m)}_αβ [2.4]: zero for a Heisenberg FM at T = 0; O(S⁰) vs O(S) for AFM/ferri; decouples ω from q (reaches ω ≤ qv, not only ω_{kν}) | D |
| Magnon–phonon | Joint Colpa problem [2.5]: each hybrid h is shared between S_ss and S_NN by its content X^{m,p}_h | D |
| Chiral / nonreciprocal | Γ_χ(v) ≠ Γ_χ(−v) for density coupling iff S(q,ω) ≠ S(−q,ω), which needs P **and** T broken [3.1]. Chiral T-even targets: enantiomer difference only via 𝒪₅×𝒪₈ interference, Γ^R_χ − Γ^L_χ = 2∫(q²/m_e)Re(c₅*c₈)γ^R_OA/(4m_χm_e)² [3.3] (v1 factor and sign corrected, K12) | D |
| L15 superconductors | Chain WP0-v2 (3.3) → Nambu–Eliashberg → BCS → conserving GRPA → bare bubble (2609.06423 Eq. (8)) → Lindhard (2101.08263 Eq. (S.13)) → 2101.08263 Eq. (3), 1512.04533 Eq. (14). **Bare BCS bubble violates the f-sum at q → 0 (K2).** DM region: L^{BCS} = 𝔤_I(ω/Δ_BCS)L^{nor} [4.2], with the **new closed form** 𝔤_I(y_BCS) = (1 + 2/y_BCS)E(k) − 4K(k)/(y_BCS + 2), k = (y_BCS − 2)/(y_BCS + 2) (K4) | D |
| Source defects | 2101.08263 Eq. (3): Re ε is k_TF²/q², not k_TF²/2q² (K1). 1512.04533 Eq. (13): e₋ lacks a 4 (K7). 2609.06423 Eqs. (4), (7): time-ordered, not retarded | D |
| Films / disorder (G9) | Mermin relaxation [4.3]; L ratio ballistic/diffusive = πqℓ_mfp/6 (K11). Drude ε (QROCODILE, WSi) is exact for qℓ_mfp ≲ 1 and underestimates L by πqℓ_mfp/6 for qℓ_mfp ≫ 1 (conservative for their limit) | D / E |
| L16 Dirac | ε = ε_bg − v_CR̃_D; 2101.08263 Eq. (4) recovered exactly (K5); anisotropic background enters as q̂·ε_bg·q̂ [5.2]. Conditional statement on 1708.08929/1910.02091 (factor ε_bg²): **pending referee FT check** | D (conditional) |
| Dopants / NV (G12) | [6.1]–[6.3]: dilute centres, host-screened transition densities, FC ZPL + sideband; Theorem D for a localised gapped centre | D + spec |
| Exothermic DM into modes | [7.2] Γ^{(ν)}_χ = (m_χq_ν*/πΩ)⟨𝔇\|ℰ_ν(q*)\|²⟩: lines at mode energies on the shell \|q\| = q_ν*, halo-independent to O(v/v*) | D |
| Gapless Theorem D (F5) | **Theorem D-g** (§8): quasiparticle-number sectors (n_qp, n_ph); per-sector PSD and completeness [D given the dressing]; existence of the dressing and the bin condition [C] | D / C |
| WP0 defects | The six v1 items (WP4-D1…D6) are applied in WP0-v2 (#1, 11, 12, 30, 31); D2's replacement is §8 | — |

---
## 1. Broken-symmetry reference states in the URF

**(1.1) [D]** WP0-v2 §1.2 places magnetic order and superconductivity in the *reference state*, not in H. Hypotheses:
- (R1) the Gibbs state is replaced by a symmetry-broken state selected by an infinitesimal field. WP0-v2 (3.1)–(4.6) need only
  stationarity and hold unchanged;
- (R2) a mean-field quasiparticle basis (spin-wave bosons a_{kν}, or Bogoliubov fermions) diagonalises the quadratic part of H;
- (R3) the response is **conserving** (Baym–Kadanoff: vertex from the same functional as the self-energy). Under (R3) WP0-v2 (4.6) (f-sum)
  and (4.8) (Ward) hold order by order; a bare bubble in a broken-symmetry basis violates them (§4.2, K2). The reference is τ metadata
  `ref ∈ {LSWT, BCS, …}`, not a finite order (CONVENTIONS §11).

**(1.2) Low-energy projection [D].** Let 𝒫_L project on the low-energy manifold (spin multiplets of a Mott insulator; Bogoliubov sector
|ξ^{BCS}_k| ≲ E_cut of a superconductor). For ω below the gap to the complement (Δ_Mott, or E_cut ≫ Δ_BCS):
  S_ab(q,ω) = S_ab[𝒫_L O_a 𝒫_L, H_L](q,ω) + O((ω/Δ_Mott)·w_⊥),                                                                    [1.1]
H_L the Schrieffer–Wolff Hamiltonian, w_⊥ the spectral weight of O_a outside 𝒫_L. The projected operator carries form factors: for a
magnetic ion 𝒫_L s_e^α(q)𝒫_L = Σ_{Rj} e^{iq·x_{Rj}} F^{mag}_j(q) λ_{S,j} 𝐒^α_{Rj}, F^{mag}_j(q) = ∫d³r e^{iq·r}ρ^s_j(r)/(2|𝐒_j|) (normalised
spin density of the magnetic orbitals; |𝐒_j| is the spin quantum number). At SOC = 0 the transverse spin channel is not Coulomb-screened
but f_xc^T-renormalised (WP0-v2 (5.3)): the LSWT magnon is the pole of R̃_s = R⁰ + R⁰f_xc^TR̃_s projected on 𝒫_L.

**(1.3) Spectral budget [E].** The spin f-sum WP0-v2 (4.6)(e), 𝓜¹_{s^zs^z} = 𝓃_eq²/(4m_e), is shared between the magnon sector and the
electronic interband sector. The magnon share is the Hohenberg–Brinkman exchange moment ~ z_exJ^{ex}|𝐒|²(qa_lat)² per magnetic site, so
  ratio ≈ 4 z_ex J^{ex} |𝐒|² m_e a_lat² (𝓃_mag/𝓃_e) = 0.084 × z_ex|𝐒|²𝓃_mag/𝓃_e   (J^{ex} = 10 meV, a_lat = 4 Å; K14).
v1 quoted 2% for the prefactor (a factor 4 dropped). YIG (z_ex = 6, |𝐒| = 5/2, 𝓃_mag/𝓃_e = 5/343 all-electron): ≈ 5%. Magnons carry a small
share of the spin weight, so WP0-v2 §9.2 (v) (L17′) spin-channel bounds are loose for magnon targets unless restricted to 𝒫_L.

---
## 2. Magnetic targets

### 2.1 L13: magnon rate (1905.13744; 2009.13534)
**Source formulas [FT]** (source notation and units; quoted, not campaign symbols).
- 1905.13744 Eq. (5): ℳ_{ν,k}(q) = δ_{q,k+G}(1/√N Ω)Σ_α⟨s_f|Ô^α_χ(q)|s_i⟩ε^α_{ν,k,G}.
- 1905.13744 Eq. (6): ε_{ν,k,G} = Σ_j √(S_j/2)(V_{jν,−k}r_j* + U*_{jν,k}r_j)e^{iG·x_j}.
- 1905.13744 Eqs. (9)–(10): R = (ρ_χ/ρ_T m_χ)∫d³v f Σ_νΣ_k Γ_{ν,k}, Γ = 2πΣ_{q=k+G}|ℳ|²δ(E_i − E_f − ω_{ν,k}).
- 1905.13744 Eq. (12): R ≃ (n_s/ρ_T)(ρ_χ/m_χ)∫d³v f∫d³q/(8π²) tr(ρ̂_χÔ⁺Ô^{†−})δ(⋯) (one-sublattice FM).
- 2009.13534 Eq. (38): Γ(v) = (1/Ω)∫d³q/(2π)³Σ_ν 2πδ(ω_{ν,k} − ω_q)½|Σ_j e^{iG·x_j⁰}√S_j(U*_{jν,k}r_j + V_{jν,−k}r_j*)·f_j(−q,v)|².
- 2009.13534 Eq. (34): f_j from c_{3a,4,6,7a,9,10,12a–15a} with weight λ_{S,j}, plus orbital terms with λ_{L,j}.
Halo values in 1905.13744 (ρ_χ = 0.3 GeV/cm³, v₀ = 220, v_esc = 500, v_E = 240 km/s) are **the source's conventions**, not the campaign halo
(CONVENTIONS §8: 2105.00599, v₀ = 238, v_esc = 544, v_E^ref = 250.5 km/s). No rate is evaluated here.

**Truncation chain from WP0-v2 (3.3) [D].**
1. Operator restriction: 𝔇_ab ≠ 0 only on the spin row a = (e, α) of WP0-v2 (2.2) (plus orbital density if λ_{L,j} ≠ 0). Matching
   WP0-v2 (2.2) maps 𝒱_{s^α} ↔ f_j^α/λ_{S,j}.
2. Clamped nuclei (n_B = 0); phonons enter only through §2.3.
3. Projection [1.1] onto each ion's ground multiplet (gap Δ_Mott; YIG ≈ 2.8 eV [E]); H_L is the spin Hamiltonian (J^{ex}_ij, anisotropy,
   DMI) and s_e^α(q) → Σ e^{iq·x_{Rj}}F^{mag}_jλ_{S,j}(R_j𝐒′_{Rj})^α, R_j the local frames of 2009.13534 Eq. (35).
4. **F^{mag}_j(q) → 1** (both sources).
5. Holstein–Primakoff to O(|𝐒|^{1/2}): 𝐒′^+ ≈ √(2|𝐒_j|)a, 𝐒′^− ≈ √(2|𝐒_j|)a†; spin operator linear in magnon operators.
6. Colpa/Toth–Lake Bogoliubov diagonalisation (Bloch transform with full positions x_{Rj}, as in 2009.13534), T = 0.
Result:
  ⟨ν,k|s_e^α(q)|0⟩ = √N ℰ^α_ν(q)δ_{q,k+G},   ℰ^α_ν(q) = Σ_j λ_{S,j}F^{mag}_j(q)e^{iG·x_j}√(|𝐒_j|/2)(U^{B*}_{jν,k}r^α_j + V^B_{jν,−k}r^{α*}_j),     [2.1]
  S_αβ(q,ω) = (2π/Ω)Σ_ν{(n_ν+1)ℰ^{α*}_ν(q)ℰ^β_ν(q)δ(ω − ω_{kν}) + n_ν 𝒜̄^{1m*}_{α,ν}𝒜̄^{1m}_{β,ν} δ(ω + ω_{−k,ν})},   𝒜̄^{1m}_{α,ν} ≡ ⟨0|s_e^α(q)|ν,−k⟩/√N.   [2.2]
(v1 wrote the absorption term with ℰ_ν(q) and ω_{kν}; the absorbed magnon carries −k.) Inserted in WP0-v2 (3.3):
Σ𝔇_{αβ}S_{αβ} = (2π/Ω)Σ_ν⟨|Σ_α𝒱_{s^α}ℰ^α_ν|²⟩_{DM spin}δ(…). At F^{mag}_j = 1, n_ν = 0 this is 2009.13534 Eq. (38) term by term, and
1905.13744 Eqs. (5)–(10) after Σ_k → NΩ∫d³k/(2π)³ (their 1/√N Ω = V^{-1}√N, V = NΩ). For one sublattice, U^B = 1, V^B = 0, r = (1, i, 0):
Γ_χ = ((|𝐒|/Ω)/8π²)∫d³q|O⁺|²δ, i.e. 1905.13744 Eq. (12) with their n_s = |𝐒|/Ω (K6).

**Validity [D/E].** (a) ω ≪ Δ_Mott. (b) q ≲ q_ff where |F^{mag}_j|² ≳ 0.9: Fe³⁺ 3d, q ≲ 1 Å⁻¹ ≈ 0.2 keV [E]; 1905.13744 notes the breakdown
"beyond 10 MeV". (c) 1/(2|𝐒_j|) ≪ 1: 0.2 for YIG, 0.5 for |𝐒| = ½ (α-RuCl₃: LSWT qualitative only). (d) T ≪ ω_thr and T ≪ T_N (560 K YIG).
(e) Commensurate order (assumed by 2009.13534). (f) SOC small so that R̃_{s,c} ≈ 0; otherwise the spin coupling is Coulomb-screened by
WP0-v2 (5.3) at relative order (λ_SO/Δ_CF)² [E]. Si/Ge are non-magnetic: L13 has no Si/Ge numbers.

**Leading corrections [D for the form; E for size].** (i) Form factor: multiply [2.1] by F^{mag}_j(q). Fe³⁺: ⟨j₀⟩ ≈ 0.7 at q ≈ 2.5 Å⁻¹
≈ 0.5 keV, so |F^{mag}|² ≈ 0.5 [E]; the suppression grows fast for m_χ ≳ 0.3 MeV (q_max = 2m_χv_max ≳ 1.5 keV). Dominant correction.
(ii) Two-magnon, O(1/(2|𝐒|)): [2.4]. (iii) Magnon–phonon hybridisation near crossings: [2.5]. (iv) SOC ions: λ_{L,j} terms and non-dipole
orbital form factors (RG8).

**Source discrepancies.** 2009.13534 Eq. (36) labels S′^x = (2S − a†a)^{1/2}a, S′^y = a†(2S − a†a)^{1/2}: these are S′^±, since S′^x is
Hermitian. Eq. (38) is consistent with the ± reading (notational only). **Status: DERIVED.**

### 2.2 Two-magnon continua (catalog §12.6 gap) [D]
Hypotheses: LSWT reference (steps 1–4, 6 of §2.1) with HP kept to the next order. 𝐒′^z_{Rj} = |𝐒_j| − a†_{Rj}a_{Rj} is bilinear; the
transverse components are odd in magnons. At O(S⁰) the two-magnon amplitude is purely longitudinal:
  ⟨νk₁;ν′k₂|s_e^α(q)|0⟩ = −δ_{k₁+k₂,q+G}Σ_j λ_{S,j}F^{mag}_j e^{iG·x_j}R_j^{αz}[U^{B*}_{jν,k₁}V^B_{jν′,−k₂} + U^{B*}_{jν′,k₂}V^B_{jν,−k₁}]/√(1+δ_{νk₁,ν′k₂}),  [2.3]
  S^{(2m)}_αβ(q,ω) = (2π/V)Σ_{k₁,ν≤ν′}𝒜^{2m*}_α𝒜^{2m}_β δ(ω − ω_{k₁ν} − ω_{q−k₁,ν′}),   𝒜^{2m}_α ≡ the amplitude [2.3].                       [2.4]
- (a) Heisenberg FM: V^B ≡ 0, so S^{(2m)} ≡ 0 at T = 0 (conservation of total S^z) (K10).
- (b) AFM/ferri: |U^BV^B| = O(1) while the one-magnon weight is ∝ |𝐒|: ratio O(1/(2|𝐒|)), 0.2 YIG, 0.5 for |𝐒| = ½ (K10).
- (c) At fixed q the continuum spans ω ∈ [min_k(ω_k + ω_{q−k}), 2ω_max^{mag}], so a DM with ω ≤ qv can deposit ω ≫ ω_{kν}(q) at small q.
- (d) T > 0: the difference process (absorb a thermal magnon) adds weight ∝ n_ν.
- (e) Sum rule [D, sketch]: one- plus two-magnon weight reproduces ⟨𝐒²⟩ = |𝐒|(|𝐒|+1) per site at O(S⁰).
*Leading correction:* magnon–magnon final-state interaction, O(1/|𝐒|²) relative; two-magnon bound states in anisotropic magnets [C] (RG3).
*Specification.* J^{ex}_ij, anisotropy, DMI from DFT+U (QE/VASP; four-state mapping or TB2J); F^{mag}_j from Wannier projection of the DFT
spin density; Colpa/Toth–Lake (SpinW algorithm) on a k-grid; [2.4] is one k-sum per (q, ν, ν′), cost ∝ N_k N_sub² per q (YIG N_sub = 20,
N_k = 40³: ≈ 3×10⁷ operations per q). Convergence: ⟨𝐒²⟩ sum rule to 1%. Output S^{(2m)}_αβ(q,ω) tables; ≈ 300-line module on the LSWT
codes of 1905.13744 / 2009.13534.

### 2.3 Magnon–phonon coupling [D]
Expand the exchange to first order in displacements: H_mp = Σ_{ij,κα}(∂J^{ex}_ij/∂u_{κα})u_{κα}𝐒_i·𝐒_j. In LSWT plus harmonic phonons this is
a quadratic boson form in Ψ = (a_k, b_Q, a†_{−k}, b†_{−Q}) (magnon a, phonon b, CONVENTIONS §5); Colpa diagonalisation with metric
diag(1,1,−1,−1) gives hybrid modes h with magnon content X^m_h and phonon content X^p_h:
  S_ss(q,ω) ⊃ (2π/Ω)Σ_h|Σ_ν X^m_{hν}ℰ_ν(q)|²δ(ω − ω_h),   S_NN(q,ω) ⊃ (2π/Ω)Σ_h|Σ_ν X^p_{hν}ℱ_ν(q)|²δ(ω − ω_h),            [2.5]
ℱ_ν the one-phonon amplitude of §7. S_sN ≠ 0 enters WP0-v2 (3.3) when 𝔇_{sN} ≠ 0. Away from crossings the mixing is g_mp/|ω_{kν} − ω_{Qν′}|.
The parametric suppression q²/(M_κω) of phonon excitation by spin couplings (2009.13534 §II.3 [FT]) is the off-resonant limit of [2.5].
*Specification.* ∂J^{ex}/∂u by finite displacements (phonopy displacements of a DFT+U supercell, re-extracting J^{ex}): 6N_atom supercell
runs; NiO (4-atom AFM cell) ~10³ CPU-h, YIG (80 atoms) ~10⁵ CPU-h [E]. Phonons from phonopy/DFPT; output ω_h, X^{m,p}_h → [2.5].
Convergence: mixing at crossings stable to 5% under supercell size.

---
## 3. Chiral and nonreciprocal responses (catalog §12.6 gap)

**(3.1) Reciprocity theorem [D].** Hypotheses: unpolarised DM, density coupling only (𝔇 = |Ṽ|²), Born, campaign sign of q (CONVENTIONS §3).
Relabel q → −q in WP0-v2 (3.3):
  Γ_χ(v) − Γ_χ(−v) = ∫d³q/(2π)³|Ṽ(q)|²[S(q,ω_q) − S(−q,ω_q)],   ω_q = q·v − q²/2m_χ.                                            [3.1]
Time reversal maps n_e(q) → n_e(−q) and leaves the Gibbs state invariant, so S(q,ω) = S(−q,ω); inversion gives the same (WP0-v2 (4.3)).
**A v-odd rate (odd under reversal of the DM wind) requires P and T both broken** (magnetoelectric, noncentrosymmetric magnets). Its
source is the q-linear magnetochiral response
  S(q,ω) − S(−q,ω) = 2q·𝐛_NR(ω) + O(q³),   𝐛_NR a polar, T-odd vector (axial × polar order parameters).                            [3.2]
Here the KKL sign (n_{−k}) would flip the odd part: the campaign sign is binding (CONVENTIONS §3).

**(3.2) Chiral, T-even targets [D].** S_nn is reciprocal, so only operator interference survives. Write 𝔇 = 𝔇^S + i𝔇^A, S = S^S + iS^A
(real symmetric / real antisymmetric parts); then Σ_ab𝔇_abS_ab ⊃ −Σ_ab𝔇^A_abS^A_ab. Natural optical activity is the antisymmetric current
response S^A_{j^αj^β} = ε_{αβγ}q^γγ_OA(q,ω) + O(q³) (P-odd, T-even). From WP0-v2 (2.2): 𝒱^{(5)}_{j^δ} = −iε_{αγδ}𝐒_χ^αq^γc₅/(4m_χm_e²) and
𝒱^{(8)}_{j^δ} = −𝐒_χ^δc₈/(4m_χm_e), with (2j_χ+1)^{-1}tr(𝐒_χ^α𝐒_χ^β) = δ_{αβ}/4. The odd part of tr[𝔇S] is +q²Re(c₅*c₈)γ_OA/(m_e(4m_χm_e)²)
(K12, exact contraction), hence
  Γ^R_χ − Γ^L_χ = 2∫d³q/(2π)³ (q²/m_e) Re(c₅*c₈)/(4m_χm_e)² γ^R_OA(q,ω_q) × (1 + O(q²)),   γ^L_OA = −γ^R_OA.                      [3.3]
(v1 printed −∫(q²/m_e)…, i.e. a factor −½; the structure was right.) 𝒪₈ is P-odd and 𝒪₅ P-even, so **an enantiomer difference measures
P-violating DM interactions** (e.g. anapole × magnetic dipole). Spin analogue: chiral phonons (2301.07617, 2511.20461 [ABS]) enter as an
antisymmetric spin–lattice response S^A_{s,κ}, contracted with 𝔇^A_{s,n} from 𝒪₁×𝒪₃ interference (∝ i(q × v_χ)); needs SOC [D].
*Specification.* (i) Nonreciprocal S: noncollinear-SOC DFT (QE), RPA+LFE response at ±q (Yambo, or an EXCEED-DM-type IP code); cost 2× the
anisotropic tables of G11; output the odd part [3.2] per q-direction. (ii) γ_OA(ω) at linear q from DFPT natural optical activity (ABINIT,
Zabalo–Stengel) [E for availability]; finite-q γ_OA beyond linear order is RG4. Convergence: the odd part vanishes to noise in a
centrosymmetric control (Si). WP6 consequence: the odd-ℓ harmonics of S must be kept in the halo functional for such targets (flag I4).

---
## 4. Superconductors and thin films

### 4.1 L15: source formulas [FT] (source notation; Δ ≡ Δ_BCS, W ≡ L of the campaign)
- 2609.06423 Eq. (6): T-matrix element ∝ (u_{p₁}v_{p₂} + v_{p₁}u_{p₂})V^{χe}.
- 2609.06423 Eq. (7): Π_QP(Q,ω) = (1/2V)Σ_p(1 − (ε_pε_{p+Q} − Δ²)/(E_pE_{p+Q}))[1/(ω − E_p − E_{p+Q} + i0⁺) − 1/(ω + E_p + E_{p+Q} − i0⁺)].
- 2609.06423 Eq. (8): ε_BCS = 1 − (4πα/Q²)Π_QP. Eq. (9): Γ = ∫dω∫_{Q⁻}^{Q⁺}Q³dQ/(2π)³|V^{χe}|²/(αv_χ)·Im ε_BCS/|ε_BCS|².
- 2101.08263 Eq. (1): Γ = ∫d³q/(2π)³|V|²[2(q²/e²)Im(−1/ε)]. Eq. (3): ε_RPA ≈ λ_TF²/2q² + i3πω_p²ω/(2q³v_F³).
- 2101.08263 Eqs. (S.13)–(S.16): Lindhard with ω → ω + iΓ_p and the "causal" branch; Eq. (S.30): S = (2q²/e²)Im ε.
- 1512.04533 Eq. (11): S(E_D,q) = 2∫d³p₂d³p₄(2π)⁴δ⁴(⋯)f₂(1 − f₄); Eq. (12): S = (m_e²T/π|q|)[z/(1 − e^{−z})](1 + ξ/z);
  Eq. (14): S ≃ (m_e²E_D/π|q|)Θ(|q|v_F − |E_D|).

### 4.2 Truncation chain and the conserving response [D]
1. WP0-v2 (3.3) with one density operator, then WP0-v2 (5.4)/(5.5) at clamped nuclei: exact for a dark photon (total charge), and for
   electron-only coupling at ω ≫ ω_D up to O(κ_BO⁴). Ions enter only through pairing.
2. Reference: Nambu–Eliashberg with Δ_BCS(iν) from α²F and μ*. BCS limit: Δ_BCS constant, λ_ep T_c/ω_D → 0, ω ≪ ω_D.
3. **Conserving response (R3)**: Coulomb RPA plus the pairing-channel ladder (generalised RPA),
  R̃^{GRPA}(q,ω) = Π^N₃₃ + Π^N₃₂[Π^N₂₂(0,0) − Π^N₂₂(q,ω)]^{-1}Π^N₂₃ (+ amplitude channel Π^N₃₁…, zero under particle–hole symmetry),
  ε(q,ω) = ε_bg − v_C(q)R̃^{GRPA}(q,ω),   S_ee = (2q²/e²)(1 − e^{−βω})^{-1}Im[−1/ε],                                                [4.1]
  Π^N_ij = −TΣ_νV^{-1}Σ_k tr[τ^N_iG^N(k+q,iν+iΩ)τ^N_jG^N(k,iν)] continued iΩ → ω + i0 (retarded, CONVENTIONS §2); Π^N₂₂(0,0) = 2/g_pair by
  the gap equation (Goldstone).
   - **K2:** at q = 0 per k, Π^N₃₃ = 4Δ_BCS²/(E_k(4E_k² + Ω²)), Π^N₃₂ = −2Δ_BCSΩ/(E_k(⋯)), Π^N₂₂ − Π^N₂₂(0) = −Ω²/(E_k(⋯)), so R̃^{GRPA}(0,ω) ≡ 0 after
     the k-sum for every ω; the bare Π^N₃₃(0,ω) ≠ 0.
   - **The bare bubble 2609.06423 Eq. (7) violates particle conservation:** its coherence factor → Δ_BCS²/E_k² ≠ 0 at Q → 0 (K3), giving a
     spurious 1/Q² term in ε_BCS and pair-breaking weight at ω > Qv_F (the "Im ε_BCS finite above the red curve" region of their Fig. 2),
     which the conserving theory suppresses by (Qv_F/ω)² [E].
   - The DM region (ω < qv_max < qv_F) never enters that region, so their DM conclusion stands. There the vertex correction is
     O((Δ_BCS/v_Fq)²) ≤ (v_max/2v_F)² = 0.04 for Al (K16) [E for size; RG1].
4. Drop the pairing vertex: [4.1] → 2609.06423 Eq. (8).
5. Δ_BCS → 0: Lindhard (2101.08263 Eq. (S.13) with Γ_p → 0) on the retarded branch; T → 0 and the free gas give 2101.08263 Eq. (S.34)
   = 1512.04533 Eq. (14) via (S.30), which is WP0-v2 (4.1) at T = 0. At T > 0, 1512.04533 Eq. (12)'s z/(1 − e^{−z}) is exactly the
   (1 − e^{−βω})^{-1} of WP0-v2 (4.1) [D].
6. ω ≪ qv_F, q ≪ k_F: 2101.08263 Eq. (3) with Re ε = **k_TF²/q²** (K1: the Lindhard bracket → 1).

**(4.3) DM-region closed form [D].** Hypotheses: clean; T = 0; quasiclassical (Δ_BCS/E_F → 0, N(0) constant over ω); bare or GRPA bubble
(equal to O(Δ_BCS²/v_F²q²)); 2Δ_BCS < ω < qv_F − q²/2m_e (Lindhard Q₊ < 1, where all DM kinematics lies). Then ξ′ − ξ = v_Fq cosθ_k + q²/2m_e
is satisfiable for every pair (E₁, E₂) with E₁ + E₂ = ω, the ξξ′ term of the coherence factor averages out, and
  Im ε^{BCS}(q,ω) = 𝔤_I(ω/Δ_BCS) Im ε^{nor}(q,ω),   Re ε^{BCS} = Re ε^{nor}[1 + O(Δ_BCS²/v_F²q²)],   so L^{BCS} = 𝔤_I L^{nor}[1 + O(Δ_BCS²/v_F²q²)],
  𝔤_I(y_BCS) = (1/y_BCS)∫₁^{y_BCS−1}dy′_BCS[y′_BCS(y_BCS−y′_BCS) + 1]/√((y′_BCS² − 1)((y_BCS−y′_BCS)² − 1)) = (1 + 2/y_BCS)E(k) − 4K(k)/(y_BCS + 2),   k = (y_BCS − 2)/(y_BCS + 2),        [4.2]
with E, K complete elliptic integrals of modulus k. The closed form is new here [D]: 𝔤_I = 𝔤_II + (2/y_BCS)∫dy′_BCS/√(⋯), the last integral is
4K(k)/(y_BCS + 2), and 𝔤_II (numerator y′_BCS(y_BCS−y′_BCS) − 1) is the Mattis–Bardeen form (1 + 2/y_BCS)E(k) − (4/y_BCS)K(k) (K4: both to 10⁻¹²). Values:
𝔤_I(2⁺) = π/2 exactly (a step), 1.418 (2.5), 1.211 (4), 1.151 (5), 1.050 (10), 1.001 (100). Hence **rate_BCS/rate_Lindhard = 𝔤_I(ω/Δ_BCS)** in
the DM region: the analytic form of 2609.06423's "agreement for ω ≳ 5Δ" (15% at 5Δ_BCS). The same ξ-decoupling in the dirty limit
(ℓ_mfp ≪ ξ_coh) gives MB for the transverse/absorption channel: **one mechanism, momentum relaxation on the scale of Δ_BCS (Doppler v_Fq or
disorder), gives both 𝔤_I and MB [D].**
*Validity with numbers* (Al: Δ_BCS = 0.17 meV, E_F = 11.7 eV, v_F = 6.8×10⁻³; WSi: Δ_BCS = 0.26 meV, E_F = 7.0 eV, as 2609.06423):
v_max/v_F = 0.39 so ω < qv_F always; q ≥ 2Δ_BCS/v_max ≈ 0.13 keV ≪ k_F = 3.5 keV; Δ_BCS/E_F ≈ 1.5×10⁻⁵; qξ_coh ≥ 2v_F/(πv_max) = 1.6
(ξ_coh = v_F/πΔ_BCS; K16), so the regime q ≲ 1/ξ_coh is **not reachable** for halo DM with ω ≥ 2Δ_BCS in clean Al (answers WP5 gap R5).
T ≪ Δ_BCS: thermal QPs ∝ e^{−Δ_BCS/T} ~ e^{−200} at 10 mK. Clean limit qℓ_mfp ≫ 1 (§4.5). Si/Ge are not superconductors.
*Leading corrections beyond L15 [D for the form; E for size].* (i) Non-thermal QPs, x_qp ~ 10⁻⁸–10⁻⁶ in Al films: replace p_i by a
generalised Gibbs state; adds a sub-gap scattering channel ω < 2Δ_BCS with case-I factor ½(1 − Δ_BCS²/E₁E₂), rate ∝ x_qp; WP0-v2 (4.1) holds with
f_qp. (ii) Strong coupling (complex Δ_BCS(ω), Eliashberg): Holstein phonon-assisted absorption above 2Δ_BCS + ω_{Qν} (the WP3 X+ analogue;
sector (2, ≥1) of §8). (iii) Plasmon tail and GSRF local fields (2101.08263 Eq. (S.19)): a Mermin-type relaxation (§4.5); damped complex
G_LF violates positivity WP0-v2 (4.4), as 2101.08263 notes [FT]. (iv) The GRPA vertex [4.1].
*Source discrepancies [D].* (a) 2101.08263 Eq. (3): Re ε should read λ_TF²/q² (= k_TF²/q²) given their Eqs. (S.14) (λ_TF = √3ω_p/v_F) and
(S.15) (K1); a factor 4 in the illustrative scaling W ~ ωq; numerics use (S.13), unaffected. (b) 1512.04533 Eq. (13) [(3.3) in the arXiv
PDF]: e₋ = (E_D − q²/2m)²/(q²/2m) should be (E_D − E_q)²/(4E_q) (K7; agrees with 2101.08263 Eq. (S.34)); affects T > 0 and edges, not
Eq. (14). (c) 2609.06423 Eqs. (4)/(7): −i0⁺ on the negative-energy pole is time-ordered, not retarded: harmless for ω > 0 at T = 0, wrong
for ω < 0, KK, sum rules and T > 0. (d) 2101.08263 attributes W(q,−ω) = −W(q,ω) to causality; it follows from WP0-v2 (4.3) with inversion
or T (causality alone gives ε(q,−ω) = ε(−q,ω)*); it fails in P- and T-broken superconductors ([3.1]). (e) 2609.06423 Eq. (9) prefactor is
consistent with WP0-v2 (3.3) (K8). **Status: DERIVED** (the step to a conserving theory and the correction sizes are E).

### 4.4 Branch cut / causality (2101.08263) [D]
WP0-v2 (4.1)–(4.2) fix the analytic structure without complex logarithms: Im ε = −v_C Im R̃ = (v_C/2)(1 − e^{−βω})S^{prop} with
S^{prop} ≥ 0 a phase-space integral (their (S.31)/(S.34)); Re ε = ε_bg + KK[Im ε] (R^∞ = 0 for densities). The earlier "acausal branch" is a
non-retarded continuation, as (c) above; its rate is off by up to 10⁷ (2101.08263 SM [FT]) because it puts negative-frequency weight at
ω > 0. The ω + iΓ_p prescription of (S.13) is **not conserving**; the conserving relaxation form is Mermin's [4.3].

### 4.5 Film geometry and disorder (G9)
**[D, relaxation-time approximation]** Mermin's conserving relaxation, γ_rel = 1/(relaxation time):
  ε_Mer(q,ω) = 1 + (ω+iγ_rel)[ε_Lin(q,ω+iγ_rel) − 1] / {ω + iγ_rel[ε_Lin(q,ω+iγ_rel) − 1]/[ε_Lin(q,0) − 1]}.                          [4.3]
For ω ≪ γ_rel (DM ω ~ meV vs γ_rel ~ 0.1 eV in films) and q ≪ k_TF: diffusive (qℓ_mfp ≪ 1) L = ω/(k_TF²D_diff) = 3ω/(k_TF²v_Fℓ_mfp), exactly
the Drude ωγ_rel/ω_p² (k_TF²D_diff = ω_p²/γ_rel), for any ω/(D_diffq²) (K11); ballistic (qℓ_mfp ≫ 1) L = πωq/(2k_TF²v_F). So
  L_Mer/L_Drude → 1 (qℓ_mfp ≲ 1),   → πqℓ_mfp/6 (qℓ_mfp ≫ 1)   (K11).                                                               [4.4]
- QROCODILE's Drude ε for WSi (2412.16279 [ABS], via catalog G9) is the qℓ_mfp ≲ 1 limit and **underestimates** L by πqℓ_mfp/6 at DM
  momenta: amorphous WSi, ℓ_mfp ≈ 0.3–1 nm, q = 1–5 keV, qℓ_mfp ≈ 1.5–25 [E]; the shift (×1–10) is conservative for their limit.
- Al films (ℓ_mfp ≳ 10 nm): qℓ_mfp ≳ 50, Lindhard holds. BCS: [4.2] with ε^{nor} → ε_Mer; in the dirty regime the ξ-decoupling holds
  independently of v_Fq (Anderson theorem).
**Film geometry [D for independent electrons in a slab; C with images].** DM states are plane waves, so the golden rule needs only the
diagonal S(q,q;ω). For a slab of thickness d_film:
  S_film(q_∥,q_z,ω) = ∫(dq′_z/2π) d_film sinc²[(q_z−q′_z)d_film/2] S_bulk(q_∥,q′_z,ω) + S_surf,                                       [4.5]
S_surf the image/surface-mode term (specular model). Relative correction O(1/qd_film) [E]: 10% at q = 0.2 keV, d_film = 10 nm; ≲ 2% for
q ≳ 1 keV. Surface plasmons (ω_p/√2 ≈ 10 eV) lie outside DM kinematics.

### 4.6 Quasiparticle generation (G9; WP5 hand-over) [D for the seed; spec for the cascade]
Prompt final state Λ = (E₁, E₂), the (2,0) sector of §8 (WP0-v2 (7.1)). From [4.2] at fixed (q,ω):
  P(E₁|ω) = [E₁E₂ + Δ_BCS²]/[√(E₁² − Δ_BCS²)√(E₂² − Δ_BCS²)] / [ω 𝔤_I(ω/Δ_BCS)],   E₂ = ω − E₁,   E₁ ∈ [Δ_BCS, ω − Δ_BCS]  (normalised, K15).  [4.6]
For ω ≫ Δ_BCS this is flat: a normal-state hot e–h pair (agrees with WP5 §5). Cascade: Chang–Scalapino/Kaplan kinetic equations with
coherence factors, QP scattering (1 − Δ_BCS²/E₁E₂), recombination and pair-breaking (1 + Δ_BCS²/E₁E₂), kernels α²F(ω′) from EPW (Al: fine grids
60³/30³, ~10³ CPU-h); phonon escape into the substrate by acoustic mismatch with transmission t_esc (input). Outputs: pair-breaking
efficiency **η_pb = Δ_BCS⟨N_qp⟩/ω**, with **N_qp the number of quasiparticles (not pairs; NOTATION v3)**: = 2Δ_BCS/ω for ω < 3Δ_BCS (N_qp = 2), → 1 at ω = 2Δ_BCS⁺ (WP5 (W13)). v1's 2Δ_BCSN_qp/ω double-counted (η_pb = 2 at threshold); the factor 2 is dropped (WP5-revision flag I1), its
variance (F_qp), time constants. Convergence: energy grid ≤ Δ_BCS/20; closed-system energy conservation to 10⁻⁴. t_esc is
phenomenological (RG7).

---
## 5. Dirac and narrow-gap materials: L16

### 5.1 Source formulas [FT] (source notation: κ ≡ ε_bg, Λ ≡ Λ_D, g ≡ g_deg, W ≡ L)
- 2101.08263 Eq. (4): W_Dirac = (e²/12πκ²v_F)Θ(ω − v_Fq)Θ(ω_max − ω). SM §F: Im ε_Dirac = (e²/12πv_F)√(1 − 4Δ²/s)(1 + 2Δ²/s)Θ(s − 4Δ²),
  s = ω² − v_F²q², W = that/κ².
- 1708.08929 Eq. (2.6): (ε_r)_Dirac = 1 + (e²g/4π²κv_F)∫₀¹dx x(1−x)ln[(2v_FΛ)²/(Δ² − x(1−x)s)] + i(e²g/24πκv_F)√(⋯)(⋯)Θ(⋯).
- 1708.08929 Eq. (3.7): ⟨|ℳ|²⟩ ≃ 16m_e²m_χ²g_D²e²ε²/((q² − m_{A′}²)²|ε_r|²); Eq. (3.11): F_med = 1/ε_r, σ̄_e defined in vacuum.
- 1910.02091 Eqs. (2.5)/(2.7): F_med = q²/(q² − Π⁰⁰); Eq. (3.13): Π_ii/κ → Π_ii/κ_ii;
  Eq. (3.14): F_med = [1 + (q_x²v_{F,z}²/κ_xx + q_y²v_{F,y}²/κ_yy + q_z²v_{F,z}²/κ_zz)π(q̃²)/q²]^{-1}.

### 5.2 Truncation chain from WP0-v2 [D]
1. WP0-v2 (3.3) with a density coupling, then (5.3)/(5.4): S = (2q²/e²)Im[−ε^{-1}] with the **total** ε (dark photon); for an electron scalar
   at clamped nuclei the same by (5.5).
2. Clamped nuclei: for ω above the polar-phonon band this holds to O(κ_BO⁴); otherwise ε_bg → ε_bg(ω) with ionic poles.
3. Split R̃ = R̃_D + R̃_bg: Dirac bands within Λ_D plus all remote bands. For ω ≪ E_bg (remote gap) and q ≪ 2π/a_lat,
   1 − v_CR̃_bg(q,ω) → ε_bg (static, local background; LFE neglected).
4. Two-band k·p to O(k): massive Dirac Hamiltonian with v_F and half-gap Δ_D. 5. R̃_D at IP (= RPA) level, T = 0, |E_F| < Δ_D. 6. Isotropy.
Result:
  ε = ε_bg − v_CR̃_D = ε_bg ε_r,   ε_r = 1 + δε_D/ε_bg,   L = Im δε_D/|ε_bg + δε_D|² → Im δε_D/ε_bg²  (|δε_D| ≪ ε_bg),            [5.1]
Im δε_D = (e²g_deg/24πv_F)√(1 − 4Δ_D²/𝓈)(1 + 2Δ_D²/𝓈)Θ(𝓈 − 4Δ_D²), 𝓈 = ω² − v_F²q². For g_deg = 2, Δ_D = 0 this is e²/12πv_F (K5: direct
two-band Lindhard integral). Hence 2101.08263 Eq. (4) and its gapped SM form, **exactly** [D].
**Anisotropy [D].** The background enters the longitudinal ε as q̂·ε_bg·q̂, not term by term inside Π⁰⁰:
  ε(q,ω) = q̂·ε_bg·q̂ − v_C R̃_D(q̃,ω),   R̃_D ∝ (Σ_i q_i²v_{F,i}²)π(q̃²)/(v_{F,x}v_{F,y}v_{F,z})  (no ε_bg inside).                     [5.2]
1910.02091 Eq. (3.14) equals ε_bg,eff/ε only for isotropic ε_bg and has a typo (q_x²v_{F,z}² for q_x²v_{F,x}²). ZrTe₅ clamped-ion
ε_bg = (187.5, 9.8, 90.9) (1708.08929 table [FT]): the background alone gives a directional rate ratio (ε_bg,xx/ε_bg,yy)² ≈ 366 (K21) between
q ∥ x and q ∥ y, before the Dirac anisotropy: a large daily-modulation lever arm, misrepresented by the harmonic mean (1708.08929) or the
per-component rule (1910.02091) [D for the structure; E for the impact].

### 5.3 The ε_bg² question: conditional statement, pending referee FT check
*Campaign convention (CONVENTIONS §9):* σ̄_e is defined in vacuum and all screening lives in S; under it the URF rate for a dark photon or an
electron scalar is [5.1], with 1/ε_bg² [D]. *Conditional statement [D, conditional]:* **if** 1708.08929 and 1910.02091 use F_med = 1/ε_r = ε_bg/ε
with σ̄_e in vacuum for a total-charge coupling (their Eqs. (3.7), (3.11), (2.5)/(2.7), (3.14) as read in v1), **then** their rate is ε_bg²
times [5.1] for the same Dirac model (= 1600 at their benchmark ε_bg = 40). That rate corresponds to a DM coupled *only* to the Dirac-band
charge (R_DD = R̃_Dε_bg/ε, S ∝ Im[R̃_D/ε_r], rank-one WP0-v2 (5.3)); a kinetically mixed dark photon couples to all charges and the remote-band
polarisation screens it by 1/ε_bg. The ε_bg²-growth of 1708.08929 Eq. (3.14) (∝ κ²v_F²I) then reflects absorbing the "1" of ε_r into
Λ′ = Λ_D exp(12π²ε_bgv_F/g_dege²). **No claim against the published limits is made** until the referee full-text check (SOTA, HIGH
PRIORITY): it must confirm (i) the coupling (total charge vs Dirac-band only), (ii) where σ̄_e is defined, (iii) whether the plotted limits
use F_med = 1/ε_r. 2101.08263 Eq. (4) agrees with the URF in any case. 1910.02091 Eq. (3.14) typo: as in §5.2.

### 5.4 Validity and corrections
*Validity with numbers.* Benchmark Λ_D = 0.2 keV, v_F = 4×10⁻⁴, ε_bg = 40: q ≤ Λ_D; ω ≤ ω^D_max ≈ 2v_FΛ_D = 0.16 eV; α̃ = αg_deg/(ε_bgv_F) = 0.91
(K17), marginal for RPA; |E_F| < Δ_D, T ≪ Δ_D; ω ≪ E_bg; q ≪ 2π/a_lat for ε_bg(q) ≈ ε_bg(0). Si/Ge are not Dirac materials. Narrow-gap
generalisation: the Kane model, whose 2-band limit is Dirac with v_F = √(E_g/2m*); split-off bands correct it at O(E_g/Δ_SO) [D].
*Leading corrections [D for the form; E for size].* (i) Charge renormalisation Re δε_D/ε_bg = (α̃/6π)ln(4Λ_D²v_F²/𝓈) = 0.27 at √𝓈 = 10 meV
(K17): rate factor (1.27)^{-2} ≈ 0.62, so [5.1] must keep it (v1 "≈ 50%" sharpened). (ii) Excitonic (BSE rung): near 2Δ_D the Sommerfeld
factor 𝒮_F^D = πζ_S^D/(1 − e^{−πζ_S^D}), ζ_S^D = α/(ε_bgv_Fb_D), b_D = √(1 − 4Δ_D²/𝓈): O(1) near threshold. (iii) Dynamic ionic background ε_bg(ω)
near polar phonons. (iv) Doping (E_F in a band): intraband Lindhard term with k_TF² = e²N(E_F)/ε_bg, removing the weak-screening advantage
for ω ≲ v_Fk_F. (v) Band curvature beyond Λ_D. **Status: DERIVED** (§5.2); §5.3 conditional.

---
## 6. Dopants and colour centres as final states (G12, electronic part) [D]
Hypotheses: dilute uncorrelated centres, 𝓃_D a*³ ≪ 1 (Si:P a* ≈ 2–2.5 nm [E], 𝓃_D ≪ 10¹⁹ cm⁻³, below the metal–insulator transition); host
screening dominates; the centre is non-degenerate and gapped, so WP0-v2 Theorem D (H2) holds locally. Per centre, with WP0-v2 (7.2)
RPA+LFE external screening:
  S^D_ab(q,ω) = 𝓃_D Σ_f 2π⟨i|Õ_a(q)†|f⟩⟨f|Õ_b(q)|i⟩δ(ω − E_f + E_i),   ñ_e(q) = Σ_G (ε^{-1}_host)_{G0}(q,ω) n_e(q+G),                  [6.1]
with Õ = O for spin and transverse operators except as screened by WP0-v2 (5.3) (j_T via local fields, spins f_xc^T-renormalised). The
weight is the retarded out-state form (WP0-v2 (7.2), CC-1); defect transitions lie below the host gap, where R_host(q,ω) is Hermitian, so
in- and out-state labellings coincide (WP0v2-C10e) and non-centrosymmetric hosts need no extra care.
- *Shallow donor, effective mass, single valley.* Plane-wave final states:
  |⟨k|e^{iq·r}|1s⟩|² = (64πa*³/V)/[1 + |k−q|²a*²]⁴ × 𝒮_F(k),   𝒮_F = 2πζ_S/(1 − e^{−2πζ_S}),   ζ_S = m*α/(ε₀k)  (Coulomb final state).   [6.2]
  Multivalley: ψ = Σ_ι a^{val}_ι F^{env}_ι(r)φ_{k_ι}(r); intervalley (g/f) terms at q ≈ k_ι − k_ι′ (keV scale) are reachable by MeV DM.
  Si:P (E_b^D = 45.6 meV): m_χ ≥ 2E_b^D/v_max² = 13.0 keV and q_min = E_b^D/v_max = 17 eV ~ 1/a* ≈ 80 eV (K18; v_max = 794.5 km/s): the form
  factor is well matched. Screening ε₀(Si) = 11.7 gives 1/ε₀² = 1/137 for density coupling. Ge donors: E_b^D ≈ 10–13 meV, a* ≈ 4–6 nm [E].
- *Deep centre (NV⁻ in diamond).* Adiabatic Condon approximation with the WP0-v2 Theorem D X0/X+ sectors:
  S^{NV}(q,ω) = 𝓃_NV 2π|⟨³E|ñ_e(q)|³A₂⟩|² ∫(dt/2π)e^{i(ω−E_ZPL)t} exp{Σ_k S_HR,k(e^{−iω_kt} − 1)},   E_ZPL = 1.945 eV.                 [6.3]
  ZPL weight e^{−S_HR} ≈ 3–4% for S_HR ≈ 3.5 [E]: the FC reduction of CONVENTIONS §10 (S_HR from g_cc − g_vv for an electronic ZPL); the
  rest is the X+ sideband. The density operator conserves spin, so ³A₂ → ³E is allowed. Spin couplings (𝒪₄) drive m_s = 0 → ±1 within ³A₂
  (2.87 GHz); since s_e(q) ≠ total spin at q ≠ 0, ΔS = 1 triplet → singlet transitions are allowed with amplitude ∝ q·r_tr (transition-
  density size r_tr) [D]. Kinematics: m_χ ≥ 0.55 MeV, q ≥ 0.73 keV (K18).
- *Leading corrections:* Herzberg–Teller (∂ transition density/∂u, as D1 §4); dynamic Jahn–Teller in ³E (E⊗e), breaking [6.3]'s linear
  coupling; central-cell/valley-orbit terms for shallow donors (EMT error ~ 10–30% in E_b^D for Si:P [E]).
*Specification.* Shallow donors: multivalley EMT envelopes with a DFT central-cell correction, or a direct DFT supercell (QE, 512–4096 Si
atoms, linear-scaling or unfolding); ⟨f|e^{iq·r}|i⟩ by Wannier interpolation of host conduction states on Δk ≲ 1/3a*; host ε^{-1}_{G0}(q,ω ≈ E_b^D)
from Yambo RPA+LFE; ~10⁴ CPU-h; convergence E_b^D to 1 meV and the q-integrated oscillator strength (partial f-sum) to 2%. NV: HSE supercell
(QE/VASP, 512–1000 atoms), ΔSCF for ³E; ΔQ and S_HR,k from constrained relaxation plus supercell phonons (phonopy), Alkauskas-type generating
function; finite-q ⟨³E|n_e(q)|³A₂⟩ from KS orbitals; singlets by quantum embedding (QDET/CRPA, WEST); ~10⁵ CPU-h; finite-q multiplet transition
densities need a new embedding module (RG5). Output: S^D(q,ω) tables per defect, rate per (𝓃_D × mass).

---
## 7. Inelastic and exothermic DM into collective modes (catalog §9 I4 gap) [D]
WP0-v2 (2.1) contains Δ_χ; only the kinematics is new. Δ_χ < 0, target mode with ω_ν(q) ≤ |Δ_χ|:
  ω = |Δ_χ| + q·v − q²/2m_χ = ω_ν(q)  ⇒  |q| = q_ν*[1 + O(v/v*)],   q_ν* = √(2m_χ(|Δ_χ| − ω_ν)),   v* = q_ν*/m_χ.                    [7.1]
For v ≪ v* and ω_ν slowly varying on the shell, ∫q²dq δ(⋯) = m_χq_ν* (K9), so with S = (2π/Ω)|ℰ_ν|²δ (K13):
  Γ^{(ν)}_χ = (m_χq_ν*/πΩ)⟨Σ_ab𝔇_ab(q*)ℰ^{a*}_νℰ^b_ν⟩_{q̂ on the shell},                                                         [7.2]
ℰ_ν = ℰ^α_ν of [2.1] for magnons; for phonons ℱ_ν = Σ_κ A_κF^M_κ(q)(2M_κω_{Qν})^{-1/2}e^{−W_κ(q)}(q·e_κν(Q))e^{iq·r_κ}, with the
CONVENTIONS §5 eigenvectors (u_{Rκ} ∝ e_κν(Q)e^{iQ·R}); v1 wrote e^{iG·r_κ}, which belongs to full-position Bloch phases (WP2 (2.2)) (K20; flag I3).
- The deposited-energy spectrum is the mode spectrum on |q| = q* (mod G): a shell DOS, i.e. lines, Doppler-broadened only by
  (∂ω_ν/∂q)q*v/v* ≪ ω_ν. The rate per DM is v-independent at leading order: **halo-independent to O(v/v*)**.
- When x_R = q*²/(2M⟨ω⟩) ≳ 1 (Table 6.1 of WP0-v2), one-phonon is FC-suppressed and the full S^{GS}_κκ (multiphonon/impulse, WP2, L5–L6) is
  needed. Example: m_χ = 1 MeV, |Δ_χ| = 1 eV: q* = 1.4 keV ≈ the Si zone, one-phonon dominated [E]. Magnons are cut by F^{mag}_j(q*).
- Endothermic (Δ_χ > 0) needs ½μ_χv² > Δ_χ + ω_ν: relevant only for Δ_χ ≲ meV × (m_χ/MeV).
*Specification.* Kinematic module on PhonoDark-type one-phonon tables (WP2) and the magnon tables (§2): shell integration with Lebedev grids
(≥ 590 points), converged to 1%; output dℛ/dω vs (m_χ, Δ_χ); the multiphonon branch reuses WP2's S^{GS}_κκ. Cost negligible.

---
## 8. Theorem D-g: final-state sectors for gapless targets (flag F5; replaces WP0-v2 §6.2 where (H2) fails)
WP0-v2 §6.2 (H2) fails on the Fermi surface of metals, superconductors (Δ_BCS ≪ ω_D inverts the adiabatic hierarchy) and semimetals
(WP4-D2, applied as a scope statement in WP0-v2). Adiabatic projectors 𝒫₀ do not exist there; quasiparticle numbers replace them.
*Hypotheses.* (G1) A fermionic quasiparticle reference: Fermi liquid, BCS/Eliashberg, or Dirac/Weyl semimetal; dressed QP operators with
residue Z_qp > 0 and on-shell width Γ_qp(E). (G2) Migdal: ω_D/E_F ~ κ_BO² ≪ 1; vertex corrections O(ω_D/E_F). (G3) T ≪ Δ_BCS (SC) or
T ≪ ω (metal). (G4) The response is conserving (R3).
*Construction.* A dressing unitary U_qp (Landau/Migdal–Eliashberg) maps bare fermions and phonons onto QPs and dressed phonons with number
operators N̂_qp, N̂_ph. Sectors 𝒬^{D-g}_{n,m} = spectral projectors of (U_qpN̂_qpU_qp†, U_qpN̂_phU_qp†) on final states (net change from the
reference): an orthogonal resolution of 1.
*Theorem D-g.* (a) [D given U_qp] S_ab = Σ_{n,m} S^{(n,m)}_ab, each restriction of WP0-v2 (3.1) by orthogonal projectors: Hermitian PSD,
complete, no double counting (the algebra of WP0-v2 §6.2 (i)). For bilinear operators (density, spin, current) acting on a BCS reference,
n ∈ {0, 2} at leading order (pair breaking changes n by 2).
(b) [C] *Sector dictionary (SC).* (0, m): phonons with no broken pairs (electron-following, Bohm–Staver-screened ions; GS analogue); stable
only for ω_{Qν} < 2Δ_BCS, since higher phonons break pairs. (2, 0): conserving GRPA pair-breaking spectrum [4.1]–[4.2] with 𝔤_I (X0
analogue; prompt seed [4.6]). (2, ≥1): Holstein phonon-assisted absorption (X+ analogue, §4.3 (ii)). (0, 0) collective: the phase mode is
lifted to ω_p by Coulomb, the amplitude (Higgs) mode decouples from density at particle–hole symmetry, so no sub-gap n = 0 line at leading
order [D within GRPA]. Normal metals: n counts e–h pairs; phonons Landau-damp into pairs at rate ~ λ_epω_{Qν}, so (0, m) and (2, m−1)
mix within that width.
(c) [C] *Bin condition (replaces (H5)).* The split is unique, and each S^{(n,m)} PSD as a measured spectrum, on energy bins wider than the
decay width of the sector label: Γ_qp(ω) + Γ_ph. Fermi liquid Γ_qp ∝ ω²/E_F (fine for ω ≪ E_F); SC: (2,0) stable until recombination
(≫ 1/Δ_BCS); Dirac semimetal (marginal) Γ_qp ~ α̃²ω, so a unique split needs α̃² ≪ 1: **at the 1708.08929 benchmark α̃ = 0.91 the split is not
unique** and only totals are quotable [E]. Outside the bin condition a declared convention is needed, as DC in WP0-v2 (6.3).
(d) [D] Σ_{n,m}𝓜¹ = 𝓃_eq²/m_e under (G4) (WP0-v2 (4.6)); per-sector first moments are not separately fixed; the bare bubble violates the total
(K2), so a non-conserving (2,0) cannot be paired with any (0,m).
(e) [C] For gapped insulators (Δ_ad ≫ ω_ph) the sectors (0,m)/(2,0)/(2,≥1), with n counting e–h pairs, coincide with GS/X0/X+ of Theorem D
to O(κ_BO^{n+1}).
*Status:* (a), (d) DERIVED given U_qp; existence of U_qp with a controlled error beyond perturbation theory (no gap, hence no space-adiabatic
theorem) and (b), (c), (e) CONJECTURED. Open item OW4-1 (= WP0-v2 OW0-9).

---
## 9. WP0 defects reported by v1, and their status
| v1 label | Defect | Status in WP0-v2 |
|---|---|---|
| WP4-D1 | Hyperfine contact 2× too large; sign +, g_I signed: H_FC = +(2/3)g_eμ_Bg_Iμ_N s·𝐈δ³ = +(1/3)…σ·𝐈δ³ from −𝛍_e·B, 𝛍_e = −g_eμ_B s (K19) | applied, (1.2) (#1) |
| WP4-D2 | (H2) fails for every gapless target | scope applied, §6.2 (#12); replacement = §8 here (F5) |
| WP4-D3 | L15 pointer must be the conserving GRPA [4.1] | applied, L15 (#30) |
| WP4-D4 | Table 6.1: SC (Δ_BCS/E_F, (T_c/ω_D)²ln, 1/k_Fℓ_mfp, Δ_BCS/v_Fq ≤ 0.2) and magnet (1/(2\|𝐒_j\|), (t/U)², q·r_3d) parameters | applied (#11) |
| WP4-D5 | L16 pointer must include ε_bg inside the total ε [5.1] | applied, L16 (#30) |
| WP4-D6 | Converse of "L odd in ω with inversion or TR": P,T-broken targets have nonreciprocal S and a v-odd rate [3.1] | applied, (4.3), L19 (#31) |

---
## 10. Exact remaining gaps
- RG1. Magnitude of the GRPA vertex correction in the DM region (formula [4.1]; ≤ 4% for Al by K16, not computed).
- RG2. Amorphous films (WSi): ab initio ε(q,ω) of the disordered film beyond relaxation time, and Δ_BCS inhomogeneity (candidate route:
  MD-quenched ≥ 500-atom supercells + Kubo–Greenwood/RPA, Bogoliubov–de Gennes on top).
- RG3. Two-magnon final-state interactions at O(1/|𝐒|²) and bound states in anisotropic magnets.
- RG4. Finite-q optical activity γ_OA(q,ω) beyond linear order (DFPT gyrotropy is O(q)).
- RG5. Finite-q multiplet transition densities for colour centres in embedding codes.
- RG6. Dirac targets at α̃ ≳ 1 (beyond one-loop RPA); BSE/Sommerfeld rung not computed.
- RG7. Phonon interface transmission t_esc in the QP cascade (phenomenological).
- RG8. Non-dipole orbital magnetic form factors for SOC ions (λ_{L,j} ≠ 0).
- OW4-1. Theorem D-g beyond conjecture (§8): existence of U_qp with error bounds; the Dirac bin condition at α̃ ~ 1.
- OW4-2. Referee FT check of §5.3 (ε_bg² question), HIGH PRIORITY.

---
## 11. Contested corrections
None. Every item of CORRECTIONS §10 (and the §0 renames that touch WP4) is applied as owed. Two applications need a remark, not a
contest: (i) "W (quoted ELF) → L" is applied in campaign text; source formulas keep W, flagged in each source header (NOTATION §K).
(ii) "S_k → S_HR,k" keeps NOTATION's mode index k in [6.3]; there k labels a local vibrational mode, not an electron crystal momentum.

---
## 12. Interface flags
| # | Owner | Quantity | Recorded form | Mismatch / action |
|---|---|---|---|---|
| I1 (F5) | WP4 → WP0 | gapless sectors | WP0-v2 §6.2 scope; "[C], owned by WP4" | §8 Theorem D-g: (a),(d) [D given U_qp], rest [C]. WP0 to cite §8 at its next revision |
| I2 | WP5 | QP efficiency | WP5 (W13) η_pb = Δ_BCS⟨N_qp⟩/ω; WP5-revision flag I1 | v1 [4.6] (2Δ_BCSN_qp/ω) gave η_pb = 2 at ω = 2Δ_BCS. **Resolved: N_qp counts quasiparticles (NOTATION v3), not pairs; the factor 2 is dropped**, η_pb = Δ_BCS⟨N_qp⟩/ω ≤ 1 (= 1 at ω = 2Δ_BCS). No mismatch remains. WP5 R5 (q ≲ 1/ξ_coh) is outside halo kinematics in clean Al (§4.3, K16) |
| I3 | WP2 | one-phonon amplitude phase | WP2 (2.2): full-position Bloch phases, e^{iG·r_κ} | **CLOSED** (coordinator audit A13): WP2-v2 IF-9 states the CONVENTIONS §5 eigenvector convention, phase e^{iq·r_κ}, matching [7.2] (K20) |
| I4 | WP6 | halo functional for P,T-broken targets | WP6 (1.5): cubic, first anisotropy ℓ = 4 | v-odd rate [3.1] adds odd ℓ (ℓ = 1 first); WP6 must not symmetrise f̂ for such targets |
| I5 | WP1, WP0 | external weight for defects | WP0-v2 (7.2), CC-1, F1 | [6.1] uses the retarded out-state weight; below the host gap in/out coincide (no GaAs-type issue) |
| I6 | NOTATION | n_D | §H defect density; §E/τ multipole order n_D | same letter, two meanings in NOTATION v3; WP4 uses n_D only as defect density, τ's n_D never appears here. Propose 𝓃_D for the density. **Applied** (NOTATION v4 §H; CORRECTIONS §17): 𝓃_D, 𝓃_NV in §6 |
| I7 | NOTATION | new WP4 symbols | — | rows proposed in §15 (τ^N_i, G^N, g_pair, x_qp, ε^{BCS}, ε^{nor}, E_cut, w_⊥, q_ff, z_ex, a_lat, 𝓃_mag, N_sub, d_film, r_tr, b_D, ω^D_max, E_bg, m*, ι, a^{val}_ι, F^{env}_ι, S^S, S^A, γ^{R,L}_OA, 𝒬^{D-g}_{n,m}, N̂_qp, N̂_ph, U_qp, Z_qp, Γ_qp) |
| F11 | all | static DFPT error | X2: O(ω_Q²/E_g²) | not used in WP4 (no DFPT-screened g enters); no action |
Consistency notes (no mismatch): L13/L15/L16/L19 pointers in WP0-v2 (9.7) match §2.1, §4.2, §5.2, §3; spin screening in §2.1(f) and §1.2
matches WP0-v2 (5.3); [3.1] uses the campaign sign of q (CONVENTIONS §3); isotropic halo factor η(v_min)/(2q) (WP0-v2 (9.2)) wherever a
velocity integral appears; σ̄_e in vacuum (CONVENTIONS §9).

---
## 13. Corrections applied (closing table)
| # | Correction (ID / source) | Where applied | How |
|---|---|---|---|
| 1 | CORRECTIONS §10: §2.1 halo values are source conventions (W) | §2.1 | flagged as 1905.13744's own; campaign halo (CONVENTIONS §8) named; no rate evaluated |
| 2 | CORRECTIONS §10: L16 κ² claim needs referee FT check first (W; SOTA HIGH PRIORITY) | §0, header, §5.3, OW4-2 | restated as a conditional statement with the three items to check; "no claim" |
| 3 | §10 rename Δ → Δ_BCS / Δ_D (N) | §1, §4, §5, §8 | throughout; Δ kept only inside quoted source formulas |
| 4 | Δ_c → Δ_Mott (N) | §1.2, §2.1 | [1.1], chain step 3, validity (a) |
| 5 | u_k, v_k → u^B_k, v^B_k; U, V → U^B, V^B (N) | §2.1–§2.2 | [2.1], [2.3]; source quotes keep U, V |
| 6 | λ (hybrid) → h (N) | §2.3 | X^{m,p}_h, ω_h in [2.5] |
| 7 | g_I, g_II → 𝔤_I, 𝔤_II (N) | §4.3, §4.6, §8 | [4.2], [4.6] |
| 8 | E^b_ν → ℰ^α_ν (N; Cartesian a/b → α/β, WP0-v2 #36) | §2, §7 | [2.1], [2.2], [7.2] |
| 9 | F_j → F^{mag}_j (N) | §1.2, §2, §7 | throughout |
| 10 | J_ij → J^{ex}_ij (N) | §1.3, §2 | throughout |
| 11 | κ → ε_bg (N; also §0 global) | §4.2, §5 | [4.1], [5.1], [5.2]; source quotes keep κ |
| 12 | Λ → Λ_D (N; §0 global) | §5 | throughout |
| 13 | g (Dirac) → g_deg (N) | §5 | [5.1], α̃ |
| 14 | s → 𝓈 (N) | §5 | [5.1], §5.4 |
| 15 | 𝐠, γ(ω) → 𝐛_NR, γ_OA (N) | §3 | [3.2], [3.3] |
| 16 | γ, ℓ, D → γ_rel, ℓ_mfp, D_diff (N); τ (relaxation time) removed | §4.3–§4.5 | [4.3], [4.4] |
| 17 | ε_M, ε_L → ε_Mer, ε_Lin (N; §0 global) | §4.5 | [4.3] |
| 18 | E_b (donor) → E_b^D (N) | §6 | [6.2], K18 |
| 19 | S_k → S_HR,k (N) | §6 | [6.3] |
| 20 | S_C, ζ → 𝒮_F, ζ_S (N) | §6 | [6.2] |
| 21 | η (Dirac Sommerfeld) → ζ_S (N); β there → b_D (collision with 1/T) | §5.4 | correction (ii) |
| 22 | η_esc → t_esc (N) | §4.6, RG7 | — |
| 23 | μ_e → 𝛍_e (N) | §9 | WP4-D1 row |
| 24 | W (quoted ELF) → L (N) | §0, §4, §5 | campaign text uses L; quotes keep W with a header note |
| 25 | K1–K10, D1–D6, RG1–RG8 → WP4-… (N; CONVENTIONS §14) | throughout | checks WP4v2-Kn; defects WP4-Dn; RGn within WP4 |
| 26 | §0 global v_k, v_q → v_C(k) | §4.2, §4.4, §5.2 | [4.1], [5.1], [5.2] |
| 27 | §0 global O_i → 𝒪_i; c₅, c₈ → c_i^{(s)} | §3, §6 | [3.3], NV spin couplings |
| 28 | §0 global M¹ → 𝓜¹; n_e (number density) → 𝓃_e | §1.3 | spectral budget |
| 29 | §0 global λ_TF → k_TF (NOTATION §K) | §4.2, §4.5 | step 6, [4.4]; quotes keep λ_TF |
| 30 | v1 citations of WP0 v1 → WP0-v2 numbers (brief) | throughout | (3.3), (4.6)(e), (5.3)–(5.5), (7.2), §9.2 (v), Table 6.1, (9.2), (9.7) |
| 31 | WP0-v2 F5: gapless Theorem D owned by WP4 | §8 | Theorem D-g with tags; OW4-1 |
| 32 | WP0-v2 F11: DFPT error order | §12 | not applicable to WP4 (stated) |
| 33 | Self-found: chiral [3.3] factor −½ and sign (S) | §3 | exact contraction, K12: Γ^R_χ − Γ^L_χ = +2∫(q²/m_e)Re(c₅*c₈)γ^R_OA/(4m_χm_e)² |
| 34 | Self-found: spectral budget prefactor 2% → 8.4% (S, [E]) | §1.3 | K14; YIG ≈ 5% |
| 35 | η_pb = 2Δ_BCSN_qp/ω → Δ_BCS⟨N_qp⟩/ω (S; self-found and WP5-revision flag I1 via coordinator; WP5 (W13)) | §4.6 | N_qp counts quasiparticles, not pairs (NOTATION v3); factor 2 dropped; η_pb(2Δ_BCS⁺) = 1; K15 note; flag I2 |
| 36 | Self-found: one-phonon phase e^{iG·r_κ} → e^{iq·r_κ} under CONVENTIONS §5 (S/convention) | §7 | K20; flag I3 |
| 37 | Self-found: [2.2] absorption term carries ⟨0|s(q)|ν,−k⟩ and ω_{−k,ν} (S) | §2.1 | [2.2] |
| 38 | Self-found: charge-renormalisation rate effect "≈ 50%" → factor 0.62 (W) | §5.4 | K17 |
| 39 | Self-found: q_min(Si:P) 18 → 17 eV; NV 0.6 → 0.55 MeV with v_max^ref = 794.5 km/s (W) | §6 | K18 |
| 40 | Self-found: two-magnon sum rule (e) was tagged [D] without derivation (W) | §2.2 | retagged [D, sketch] |
| 41 | New: closed form 𝔤_I(y_BCS) = (1 + 2/y_BCS)E(k) − 4K(k)/(y_BCS + 2) | §4.3 | derived; K4 to 10⁻¹² and exact 𝔤_I(2⁺) = π/2 |
| 43 | Flag I3 closed (coordinator audit A13; WP2-v2 IF-9) | §12 | WP2-v2 now uses e^{iq·r_κ}, matching [7.2]; no mismatch remains |
| 42 | Checks: mpmath quadratures replaced by sympy (brief: sympy only); 13 checks added (K11–K21) | code/WP4-v2 | 23/23 PASS |
| 44 | NOTATION v4 renames (CORRECTIONS §17) | §2.1–§2.2, §4.3, §5.4, §6, §8, §12 I2/I6/I7, §15, §0 L15 row, row 41 | 𝒜^α → 𝒜^{2m}_α; 𝒜̄^α_ν → 𝒜̄^{1m}_{α,ν}; y, y′ → y_BCS, y′_BCS; ξ₀ → ξ_coh; §5.4 (ii) 𝒮_F, ζ_S → 𝒮_F^D, ζ_S^D ([6.2] keeps 𝒮_F, ζ_S); n_D → 𝓃_D, n_NV → 𝓃_NV; 𝒬_{n,m} → 𝒬^{D-g}_{n,m}; §15 updated to v4. Notational only |
**Count:** 43 entries (#43: flag I3 closed): 32 owed corrections applied (2 CORRECTIONS §10 W items, 27 renames from §10/§0, the WP0-v2 citation map, F5, F11),
8 self-found corrections (#33–40), 1 new result (#41), 1 check-script update (#42). Contested: 0. Interface flags: I1–I7 (I3 closed; F11 n/a). Row 44 (NOTATION v4 renames) is notational and outside this count.

---
## 14. Literature
Read in full text by v1 (2026-10-31; IDs verified against the arXiv API; not re-read in this revision): 1905.13744 (Eqs. 1–13); 2009.13534
(Eqs. 32–38); 1512.04533 (Eqs. 11–14; PDF Eq. 3.3); 2101.08263 (Eqs. 1–4, S.10–S.34, SM §F); 2609.06423 (Eqs. 1–10); 1708.08929 (Eqs. 2.1–2.8,
3.2–3.14, A.8–A.9, ε_bg table); 1910.02091 (Eqs. 2.1–2.18, 3.1–3.14). Title only [ABS]: 2212.04504, 1901.07569, 2210.13516, 2301.07617,
2511.20461, 1004.0937, 2412.16279, 1504.07237, 2005.10256, 2501.18120, 2308.06314, 1604.06800, 2210.06490. No DM calculation of two-magnon
continua, a conserving BCS dielectric function, exothermic DM into collective modes, or NV final states was found by v1's searches.

---
## 15. Symbols introduced/used
All symbols follow NOTATION v4 and CONVENTIONS; **no deviations** (v4 renames: CORRECTIONS §17, closing-table row 44). Source formulas (§2.1, §4.1, §5.1) keep their own notation, as
NOTATION §K allows (κ, Λ, g, Δ, W, λ_TF, S_j, U, V, n_s, ε_r, Π_QP, Γ_p, f_j, s_f, s_i).
*Used as defined in NOTATION/CONVENTIONS:* q, ω, ω_q, Δ_χ, v, v_χ, v_max, v*, q_ν*, m_χ, μ_χe, ρ_χ, ρ_T, Ω, N, V, 𝒪_i, c_i^{(s)}, 𝒱_a, 𝔇_ab, 𝔇^S,
𝔇^A, Ṽ, σ̄_e, 𝐒_χ, j_χ, Γ_χ, ℛ, S, S_ab, S^{prop}, R, R̃, R⁰, R̃^{GRPA}, Π^N_ij, ε, ε_e, ε₀, ε_bg, ε_r, ε_Mer, ε_Lin, v_C, L, f_xc^T, G_LF, 𝓜¹,
𝓃_e, n_e(q), s_e^α, j_e^α, j_T, O_a, s_i, H_hf, g_e, g_I, μ_B, μ_N, 𝛍_e, 𝐈_I, κ, κ_BO, M_κ, A_κ, F^M_κ, W_κ, b_{Qν}, ω_{Qν}, e_κν(Q), r_κ, R,
x_R, S^{GS}_κκ, GS, X0, X+, Δ_ad, Λ, τ, n_B, 𝒮_F, ζ_S ([6.2]), 𝒮_F^D, ζ_S^D (Dirac, §5.4), ξ_coh, Δ_BCS, Δ_D, Δ_Mott, Δ_SO, E_k, ξ^{BCS}_k, u^B_k, v^B_k, U^B, V^B, X^{m,p}_h, 𝔤_I, 𝔤_II,
ℰ^α_ν, ℰ_ν, ℱ_ν, 𝐒_j, λ_{S,j}, λ_{L,j}, R_j, r_j, F^{mag}_j, J^{ex}_ij, g_mp, a_{kν}, n_ν, v_F, k_F, k_TF, E_F, N(0), γ_rel, ℓ_mfp, D_diff,
Λ_D, g_deg, α̃, 𝓈, 𝐛_NR, γ_OA, 𝓃_D, a*, E_b^D, E_ZPL, S_HR, S_HR,k, N_qp, η_pb, t_esc, F_qp, ω_p, T_c, ω_D (Debye, as in WP0-v2 §6.2),
E_g, η(v_min).
*Introduced here (new objects, no collision; NOTATION v4 §M rows, requested as flag I7):*
| Symbol | Meaning | Where |
|---|---|---|
| τ^N_i, G^N(k,iν), g_pair | Nambu Pauli matrices; Nambu Green function; BCS pairing coupling (Π^N₂₂(0,0) = 2/g_pair) | [4.1] |
| ε^{BCS}, ε^{nor} | superconducting and normal-state dielectric functions (campaign objects; "ε_BCS" only in the 2609.06423 quote) | [4.2] |
| L^{BCS}, L^{nor} | their loss functions | [4.2] |
| y_BCS, y′_BCS | ω/Δ_BCS and the integration variable in 𝔤_I, 𝔤_II (v3 names y, y′) | [4.2] |
| E₁, E₂ | the two Bogoliubov QP energies of the prompt pair | [4.2], [4.6] |
| x_qp, f_qp | non-thermal QP density fraction; QP distribution | §4.3 |
| λ_ep, α²F, μ* | e–ph coupling constant, Eliashberg function, Coulomb pseudopotential | §4.2 |
| E_cut, w_⊥ | Bogoliubov-sector cutoff; spectral weight outside 𝒫_L | [1.1] |
| 𝒫_L, H_L | low-energy projector; Schrieffer–Wolff Hamiltonian (𝒫 decorated by L; distinct from 𝒫₀, 𝒫_⊥) | [1.1] |
| q_ff | momentum below which \|F^{mag}_j\|² ≳ 0.9 | §2.1 |
| z_ex, a_lat, 𝓃_mag, N_sub | exchange coordination; lattice constant; magnetic-ion density; magnetic sublattices per cell | §1.3, §2.2 |
| 𝐒′_{Rj}, x_{Rj} | spin in the local frame; magnetic-ion position (cell R, site j) | §2.1 |
| 𝒜^{2m}_α, 𝒜̄^{1m}_{α,ν} | two-magnon amplitude; one-magnon absorption amplitude (v3 names 𝒜^α, 𝒜̄^α_ν) | [2.2], [2.4] |
| ω_{kν}, ω_h | magnon and hybrid-mode frequencies | §2 |
| S^S_ab, S^A_ab | real symmetric and antisymmetric parts of S_ab (S = S^S + iS^A) | §3.2 |
| γ^R_OA, γ^L_OA, Γ^R_χ, Γ^L_χ | optical activity and rate of the two enantiomers | [3.3] |
| d_film, S_film, S_bulk, S_surf | slab thickness; slab, bulk and surface DSFs | [4.5] |
| R̃_D, R̃_bg, δε_D, E_bg, b_D, ω^D_max | Dirac and background proper responses; Dirac part of ε; remote gap; pair velocity; Dirac ω cutoff | §5 |
| m*, ι, a^{val}_ι, F^{env}_ι, k_ι | effective mass; valley index; valley amplitude; envelope; valley momentum | [6.2] |
| S^D_ab, ñ_e, Õ_a, ε_host, 𝓃_NV, r_tr | defect response; host-screened operators; host dielectric; NV density; transition-density size | §6 |
| Γ^{(ν)}_χ | rate per DM into mode ν (exothermic) | [7.2] |
| 𝒬^{D-g}_{n,m}, N̂_qp, N̂_ph, U_qp, Z_qp, Γ_qp, Γ_ph, S^{(n,m)}_ab | Theorem D-g projectors, number operators, dressing, QP residue and width, phonon width, sector spectra | §8 |
Labels: WP4v2-K1…K21 (checks), I1–I7 (flags), OW4-1, OW4-2 (open items); RG1–RG8 and WP4-D1…D6 keep their v1 meaning.
