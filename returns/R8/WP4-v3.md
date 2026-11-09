# R8 / WP4-v3: spin, superconducting and special targets (corrected standalone version after the R7 hostile review)

Revision agent, brief R8/REV3-WP4. Supersedes returns/R6/WP4-v2.md (v2), which stays as the historical record (v1: returns/R5/WP4.md).
v3 applies every verdict of the two isolated R7 referee reports, referees/R7/REF-WP4-A.md (cited **A-Vn**) and REF-WP4-B.md (cited
**B-Vn**), and the coordinator's R7 notes in state/SOTA.md. The v2 corrections (CORRECTIONS §10, §17; WP0-v2 flags F5, F11) remain applied.
The referee closing table is §13. Rebuttals (to be returned to the referee concerned) are in §11. Referee disagreements, each settled by a
derivation, are in §11A.
Conventions: CONVENTIONS.md. Symbols: NOTATION v4. Architecture: returns/R6/WP0-v2.md, cited as WP0-v2 (s.n).
Checks: `code/WP4-v3/checks.py`. Sympy only (exact algebra; `Integral.evalf` for 1-D quadratures; evalf of closed-form 2×2 matrix
functions; mpmath, sympy's numerical backend, for small exact model matrices). 36 checks, all PASS, in < 30 s. They are cited WP4v3-Kn. K1–K21 keep their v2 meaning: K11 is rebuilt as a derivation and K15,
K16, K17, K21 are extended. K22–K32 are new; K33–K34 were added in the R9 clean-up (§16). No numerical simulation was run.
Tags: **[D]** derived (hypotheses stated); **[D, sketch]**; **[E]** estimated; **[C]** conjectured. Literature: **[FT-R7×2]** a full-text
statement CONFIRMED by both R7 referees; **[FT-R7]** CONFIRMED by one referee; **[UNRESOLVED]** quoted from v1's reading but not rated by
a referee. REFUTED literature claims are dropped (§14). WP4 equations are **[s.n]**: v1/v2 numbers are kept and new ones appended.
Status: CLAIMED, R×2 done on v2; v3 corrections pending coordinator acceptance. **The L16 ε_bg² finding against 1708.08929 and 1910.02091 is
REFEREED (R×2 CONFIRMED against the full text) and is stated as a firm claim in §5.3. The new absorption finding (a factor ε_bg) is in §5.5.**
**R9 clean-up (edited in place):** the new items of referees/R8/VER-WP4-A.md and VER-WP4-B.md and the WP4 rows of returns/R8/AUDIT-2.md are
applied; closing table §16.

---
## 0. Results at a glance
| Item | Result | Tag |
|---|---|---|
| **L16 Dirac, scattering (REFEREED)** | 1708.08929 Eqs. (3.7), (3.11), (3.14) and 1910.02091 Eqs. (2.7), (3.14) overstate the dark-photon scattering rate by **ε_bg² exactly**, for any δε_D. That is ×1600 at their benchmark ε_bg = 40, ×640 for the ZrTe₅ curve of the source's isotropised model (harmonic mean 25.3), and (q̂·ε_bg·q̂)² per direction in the anisotropic case. Cause: F_med = 1/ε_r = ε_bg/ε applied with a vacuum σ̄_e and a bare vertex e. The explicit ε_bg² prefactor of 1708.08929 Eq. (3.14) *is* the omitted 1/ε_bg². The Λ′_D rewrite is common to both theories (§5.3, K22, K23) | D + FT-R7×2 |
| **L16 / L9b Dirac, absorption (new)** | The same omission makes the dark-photon *absorption* rates of 1708.08929 Eqs. (4.4)–(4.5) and 1910.02091 Eqs. (2.25)–(2.27) too large by **ε_bg** (by ε_bg,ii per principal polarisation). Correct rate: κ_mix²m_φ Im(−1/ε) with the total ε (= WP0-v2 L9b) (§5.5, K24) | D (source eqs per A, B) |
| L16 Dirac, structure | ε = ε_bg − v_CR̃_D. 2101.08263 Eq. (4) is recovered exactly (K5). The anisotropic background enters as q̂·ε_bg·q̂ [5.2]. The q ∥ y rate is the larger: (ε_bg,xx/ε_bg,yy)² = 366 with the 1708.08929 table, 221 with the 1910.02091 values (K21). Typo q_x²v_{F,z}² in 1910.02091 Eqs. (3.13) and (3.14). Charge renormalisation 0.27–0.35, i.e. a rate factor 0.62–0.55, depending on the cutoff scheme (K17) | D |
| L13 magnons | 1905.13744 Eqs. (5)–(12) and 2009.13534 Eq. (38) follow from WP0-v2 (3.3) restricted to the spin row of WP0-v2 (2.2), by a 6-step chain (§2.1). Leading correction: the magnetic form factor, \|F^{mag}_j(q)\|² ≈ 0.5 at q ≈ 0.5 keV (Fe³⁺), which both sources set to 1. Next: two-magnon, O(1/(2\|𝐒_j\|)) | D / E |
| Two-magnon | Closed-form longitudinal S^{(2m)}_αβ [2.4]. It is zero for a Heisenberg FM at T = 0, and O(S⁰) against O(S) for AFM/ferri. It decouples ω from q, so it reaches ω ≤ qv, not only ω_{kν} | D |
| Magnon–phonon | Joint Colpa problem [2.5]: each hybrid h is shared between S_ss and S_NN according to its content X^{m,p}_h | D |
| Chiral / nonreciprocal | Γ_χ(v) ≠ Γ_χ(−v) for a density coupling *requires* S(q,ω) ≠ S(−q,ω), which needs P **and** T broken [3.1]. This is a necessary condition only. For the density channel the odd part is O(q³) [3.2′] (K26), not O(q). Chiral T-even targets: Γ^R_χ − Γ^L_χ = 2∫(q²/m_e)Re(c₅*c₈)γ^R_OA/(4m_χm_e)² [3.3]. The sign of γ_OA is defined by S = S^S + iS^A, with the contraction Σ_ab𝔇_abS_ab (K12) | D |
| L15 superconductors | Chain WP0-v2 (3.3) → Nambu–Eliashberg → BCS → conserving GRPA → bare bubble (2609.06423 Eq. (8)) → Lindhard → 2101.08263 Eq. (3), 1512.04533 Eq. (14). The bare BCS bubble violates the f-sum at q → 0 (K2). 2609.06423 itself identifies the missing phase term Π_θ and bounds it by Δ²/(v_FQ)² ≤ 1/25 (credited, §4.2). DM region: L^{BCS} = 𝔤_I(ω/Δ_BCS)L^{nor} [4.2], with the case-I closed form 𝔤_I = (1 + 2/y_BCS)E(k) − 4K(k)/(y_BCS + 2) (K4), known from P. B. Allen, PRB 3, 305 (1971) (not new; credited). 𝔤_I is the production-rate ratio Im ε^{BCS}/Im ε^{nor}. It is *not* 2609.06423's 5Δ screening statement (v2 claim withdrawn). **New screening correction [4.2′]:** Re ε^{BCS}/Re ε^{nor} − 1 = (Δ_BCS/qv_F)𝔰_BCS(ω/Δ_BCS) is *first* order, not O(Δ²/v_F²q²) as v2 asserted, with 𝔰_BCS(0) = 0 by an exact sum rule (K32). The term **lowers** L (𝔰_BCS > 0). At the Al kinematic edge its effect is 8–16% at ω = 5Δ_BCS [E, KK-cutoff spread], and the expansion **fails** for ω ≲ 3.5Δ_BCS there (\|δL/L\| ≈ 1.42/0.88/0.53 at y_BCS = 2.2/2.5/3; K34) | D / D, sketch |
| Source defects | 2101.08263 Eq. (3): Re ε is k_TF²/q², not k_TF²/2q² (K1). 1512.04533 Eq. (13): e₋ lacks a 4 (K7). Both FT-R7×2. 2609.06423 Eqs. (4), (7): time-ordered, which equals retarded for ω > 0 at T = 0 (K25). **Not a defect** (v2 claim withdrawn) | D + FT |
| Films / disorder (G9) | Mermin [4.3] reduces to the diffusive form and to the ballistic Lindhard form; ballistic/diffusive L ratio = πqℓ_mfp/6 for q ≪ k_F, k_TF (K11, now derived from [4.3]). **The v2 QROCODILE statement is withdrawn**: their bulk rate uses Lindhard with ω + iΓ, and Drude only for thin-layer anisotropy. Amorphous WSi (k_Fℓ_mfp ~ 1, q ~ k_F) is outside the RTA–Mermin validity (K31) | D |
| Dopants / NV (G12) | [6.1]–[6.3]: dilute centres, host-screened transition densities, FC ZPL + sideband; Theorem D for a localised gapped centre | D + spec |
| Exothermic DM into modes | [7.2] Γ^{(ν)}_χ = (m_χq_ν*/πΩ)⟨𝔇\|ℰ_ν(q*)\|²⟩: lines at mode energies on the shell \|q\| = q_ν*, halo-independent to O(v/v*). Worked example moved inside validity: (1 MeV, 50 eV), with v_max/v* = 0.27 (K29) | D |
| Gapless Theorem D (F5) | **Theorem D-g** (§8): quasiparticle-number sectors (n_qp, n_ph). (a) is now [D given U_qp and (G5′)], with the state-restricted cross-term bound [8.1′], \|C_cross\| ≤ c_g𝔥_off(ψ_b)‖O_a\|i⟩‖‖O_b\|i⟩‖/Δω_bin² (K30, K33). On few-quasiparticle states 𝔥_off ~ √(ΓW_c/2π) ≫ Γ [E] (R9). The bin condition (c) stays [C]. Exact completeness holds only in the conserved-number limit. Magnetic insulators are not covered (OW4-4) | D / C |
| QP generation | η_pb = Δ_BCS⟨N_qp⟩/ω. N_qp = 2 (η_pb = 2Δ_BCS/ω) for all ω < **4**Δ_BCS (K27) | D |
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
but screened beyond IP by the triplet W^{scr} ladder plus f_xc^T (WP1-v3 IF-13; R̃_s ≡ 4R_{s^zs^z}; ×1.3–2 near the edge [E]). At the f_xc^T level
the LSWT magnon is the pole of R̃_s = R⁰ + R⁰f_xc^TR̃_s projected on 𝒫_L; the ladder adds the triplet W^{scr} kernel (AUDIT-2 m13).

**(1.3) Spectral budget [E].** The spin f-sum WP0-v2 (4.6)(e), 𝓜¹_{s^zs^z} = 𝓃_eq²/(4m_e), is shared between the magnon sector and the
electronic interband sector. The magnon share is the Hohenberg–Brinkman exchange moment ~ z_exJ^{ex}|𝐒|²(qa_lat)² per magnetic site, so
  ratio ≈ 4 z_ex J^{ex} |𝐒|² m_e a_lat² (𝓃_mag/𝓃_e) = 0.084 × z_ex|𝐒|²𝓃_mag/𝓃_e   (J^{ex} = 10 meV, a_lat = 4 Å; K14).
v1 quoted 2% for the prefactor (a factor 4 dropped). YIG (z_ex = 6, |𝐒| = 5/2, 𝓃_mag/𝓃_e = 5/343 all-electron): ≈ 5%. Magnons carry a small
share of the spin weight, so WP0-v2 §9.2 (v) (L17′) spin-channel bounds are loose for magnon targets unless restricted to 𝒫_L.

---
## 2. Magnetic targets

### 2.1 L13: magnon rate (1905.13744; 2009.13534)
**Source formulas** (source notation and units; quoted, not campaign symbols). Status: Eqs. (5), (6) [FT-R7] (B checked them against the HTML source);
Eq. (12) with n_s = |𝐒|/Ω [FT-R7] (B, via App. (A.10)–(A.13)); Eqs. (9)–(10) [UNRESOLVED]; 2009.13534 Eqs. (36), (38) [FT-R7] (A); Eq. (34) [UNRESOLVED].
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
"beyond 10 MeV" [UNRESOLVED]. (c) 1/(2|𝐒_j|) ≪ 1: 0.2 for YIG, 0.5 for |𝐒| = ½ (α-RuCl₃: LSWT qualitative only). (d) T ≪ ω_thr and T ≪ T_N (560 K YIG).
(e) Commensurate order (assumed by 2009.13534). (f) SOC small so that R̃_{s,c} ≈ 0; otherwise the spin coupling is Coulomb-screened by
WP0-v2 (5.3) at relative order (λ_SO/Δ_CF)² [E]. Si/Ge are non-magnetic: L13 has no Si/Ge numbers.

**Leading corrections [D for the form; E for size].** (i) Form factor: multiply [2.1] by F^{mag}_j(q). Fe³⁺: ⟨j₀⟩ ≈ 0.7 at q ≈ 2.5 Å⁻¹
≈ 0.5 keV, so |F^{mag}|² ≈ 0.5 [E]; the suppression grows fast for m_χ ≳ 0.3 MeV (q_max = 2m_χv_max ≳ 1.5 keV). Dominant correction.
(ii) Two-magnon, O(1/(2|𝐒|)): [2.4]. (iii) Magnon–phonon hybridisation near crossings: [2.5]. (iv) SOC ions: λ_{L,j} terms and non-dipole
orbital form factors (RG8).

**Source discrepancies [FT-R7, A-V18].** 2009.13534 Eq. (36) labels S′^x = (2S − a†a)^{1/2}a, S′^y = a†(2S − a†a)^{1/2}: these are S′^±, since S′^x is
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
The parametric suppression q²/(M_κω) of phonon excitation by spin couplings (2009.13534 §II.3 [UNRESOLVED]) is the off-resonant limit of [2.5].
*Specification.* ∂J^{ex}/∂u by finite displacements (phonopy displacements of a DFT+U supercell, re-extracting J^{ex}): 6N_atom supercell
runs; NiO (4-atom AFM cell) ~10³ CPU-h, YIG (80 atoms) ~10⁵ CPU-h [E]. Phonons from phonopy/DFPT; output ω_h, X^{m,p}_h → [2.5].
Convergence: mixing at crossings stable to 5% under supercell size.

---
## 3. Chiral and nonreciprocal responses (catalog §12.6 gap)

**(3.1) Reciprocity theorem [D].** Hypotheses: unpolarised DM, density coupling only (𝔇 = |Ṽ|²), Born, campaign sign of q (CONVENTIONS §3).
Relabel q → −q in WP0-v2 (3.3):
  Γ_χ(v) − Γ_χ(−v) = ∫d³q/(2π)³|Ṽ(q)|²[S(q,ω_q) − S(−q,ω_q)],   ω_q = q·v − q²/2m_χ.                                            [3.1]
Time reversal maps n_e(q) → n_e(−q) and leaves the Gibbs state invariant, so S(q,ω) = S(−q,ω); inversion gives the same (WP0-v2 (4.3)).
**A v-odd rate (odd under reversal of the DM wind) requires P and T both broken** (magnetoelectric, noncentrosymmetric magnets). This is a
necessary condition only (A-V15). By [3.1], Γ_χ(v) ≠ Γ_χ(−v) implies S(q,ω) ≠ S(−q,ω) somewhere on the kinematic surface. The converse fails:
a nonreciprocal S need not give a nonzero integral. Here the KKL sign (n_{−k}) would flip the odd part, so the campaign sign is binding
(CONVENTIONS §3).
*Order of the odd part (corrected, B-V14) [D].* Hypotheses: (i) continuity for the density row (WP0-v2 (4.8), CONVENTIONS §6), which gives
ω²S_nn(q,ω) = q_αq_βS_{j^αj^β}(q,ω) for ω ≠ 0; (ii) S_{j^αj^β}(q,ω) is analytic in q at fixed ω ≠ 0, i.e. a gapped target, or ω ≫ qv_F in a
metal. Write the odd part of the current response as S_{j^αj^β}(q,ω) − S_{j^αj^β}(−q,ω) = 2b^{NR}_{αβγ}(ω)q^γ + O(q³), where b^{NR} is the
magnetochiral (gyrotropic) tensor. Only its αβ-symmetric part enters below, and that part is nonzero only with P and T both broken. The
αβ-antisymmetric part contains natural optical activity, ε_{αβγ}γ_OA (P-odd, T-even, §3.2), which drops out of q_αq_βS_{j^αj^β}. Then
  S(q,ω) − S(−q,ω) = 2q^αq^βq^γ b^{NR}_{αβγ}(ω)/ω² + O(q⁵)   (density channel; K26).                                              [3.2′]
The even part is itself O(q²), since S_nn(0, ω ≠ 0) = 0. So the *relative* nonreciprocity is still first order in q; only the absolute order
of v2's [3.2] was wrong for the density coupling assumed in [3.1]. The q-linear form
  S_{XX}(q,ω) − S_{XX}(−q,ω) = 2q·𝐛_NR(ω) + O(q³)   (current and spin channels X = j, s, component-wise; 𝐛_NR → b^{NR}_{αβγ} for X = j)    [3.2]
holds for the current and spin rows. Angular content of [3.2′]: q̂^αq̂^βq̂^γ b^{NR}_{(αβγ)} contains at most ℓ = 1 and ℓ = 3, and which survive is
fixed by the effective point group G_eff (WP6-v3 (1.5), C28; AUDIT-2 m16). **ℓ = 1 occurs only for polar G_eff**. No cubic group has an ℓ = 1
invariant, and the lowest odd ℓ is 3 for T and T_d and 9 for O (WP6-v3 C28; then [3.2′] is not the leading odd term for O). v3's "ℓ = 1 remains
the leading odd harmonic" is withdrawn (flag I4). The same object appears in WP0-v3 (4.3) as 𝐁^{NR}_{αβγ} ≡ b^{NR}_{αβγ}/ω² (AUDIT-2 m17;
one NOTATION row). This agrees with REF-WP0-B's note on WP0-v2 (4.3).

**(3.2) Chiral, T-even targets [D].** S_nn is reciprocal, so only operator interference survives. Write 𝔇 = 𝔇^S + i𝔇^A, S = S^S + iS^A
(real symmetric / real antisymmetric parts); then Σ_ab𝔇_abS_ab ⊃ −Σ_ab𝔇^A_abS^A_ab (element-wise sum, = tr[𝔇ᵀS]; 𝔇_ab = ⟨𝒱_a*𝒱_b⟩ and S_ab = ⟨O_a†…O_b⟩ in WP0-v2 (3.1)/(3.3) order). Natural optical activity is the antisymmetric current
response S^A_{j^αj^β} = ε_{αβγ}q^γγ_OA(q,ω) + O(q³) (P-odd, T-even). From WP0-v2 (2.2): 𝒱^{(5)}_{j^δ} = −iε_{αγδ}𝐒_χ^αq^γc₅/(4m_χm_e²) and
𝒱^{(8)}_{j^δ} = −𝐒_χ^δc₈/(4m_χm_e), with (2j_χ+1)^{-1}tr(𝐒_χ^α𝐒_χ^β) = δ_{αβ}/4. The odd part of Σ_ab𝔇_abS_ab is +q²Re(c₅*c₈)γ_OA/(m_e(4m_χm_e)²)
(K12, exact contraction; REF-A re-derived it by hand), hence
  Γ^R_χ − Γ^L_χ = 2∫d³q/(2π)³ (q²/m_e) Re(c₅*c₈)/(4m_χm_e)² γ^R_OA(q,ω_q) × (1 + O(q²)),   γ^L_OA = −γ^R_OA.                      [3.3]
(v1 printed −∫(q²/m_e)…, i.e. a factor −½; the structure was right.) *Sign convention (A-V16):* γ_OA > 0 is **defined** by the decomposition
S = S^S + iS^A with S^A_{j^αj^β} = ε_{αβγ}q^γγ_OA in the S_ab ordering above. It is not an optical-rotation sign convention. If WP0 pairs 𝔇_ab with S_ba
instead, [3.3] changes sign (flag I9). 𝒪₈ is P-odd and 𝒪₅ P-even, so **an enantiomer difference measures
P-violating DM interactions** (e.g. anapole × magnetic dipole). Spin analogue: chiral phonons (2301.07617, 2511.20461 [UNRESOLVED; title only]) enter as an
antisymmetric spin–lattice response S^A_{s,κ}, contracted with 𝔇^A_{s,n} from 𝒪₁×𝒪₃ interference (∝ i(q × v_χ)); needs SOC [D].
*Specification.* (i) Nonreciprocal S: noncollinear-SOC DFT (QE), RPA+LFE response at ±q (Yambo, or an EXCEED-DM-type IP code); cost 2× the
anisotropic tables of G11; output the odd part [3.2′] per q-direction. (ii) γ_OA(ω) at linear q from DFPT natural optical activity (ABINIT,
Zabalo–Stengel) [E for availability]; finite-q γ_OA beyond linear order is RG4. Convergence: the odd part vanishes to noise in a
centrosymmetric control (Si). WP6 consequence: the odd-ℓ harmonics of S must be kept in the halo functional for such targets (flag I4).

---
## 4. Superconductors and thin films

### 4.1 L15: source formulas (source notation; Δ ≡ Δ_BCS, W ≡ L of the campaign)
- 2609.06423 Eq. (6): T-matrix element ∝ (u_{p₁}v_{p₂} + v_{p₁}u_{p₂})V^{χe}. [FT-R7]
- 2609.06423 Eq. (7): Π_QP(Q,ω) = (1/2V)Σ_p(1 − (ε_pε_{p+Q} − Δ²)/(E_pE_{p+Q}))[1/(ω − E_p − E_{p+Q} + i0⁺) − 1/(ω + E_p + E_{p+Q} − i0⁺)]. [FT-R7×2]
- 2609.06423 Eq. (8): ε_BCS = 1 − (4πα/Q²)Π_QP. Eq. (9): Γ = ∫dω∫_{Q⁻}^{Q⁺}Q³dQ/(2π)³|V^{χe}|²/(αv_χ)·Im ε_BCS/|ε_BCS|². Eq. (10): as (9)
  with |ε_BCS|² → |ε_Lin|², keeping Im ε_BCS. §IV, Fig. 3: phase-exchange polarisation Π_θ, suppressed by Δ²/(v_FQ)², relative error ≤ 1/25
  for ω > 5Δ. Fig. 2: |ε_BCS|²/|ε_Lin|². [FT-R7×2]
- 2101.08263 Eq. (1): Γ = ∫d³q/(2π)³|V|²[2(q²/e²)Im(−1/ε)] [UNRESOLVED]. Eq. (3): ε_RPA ≈ λ_TF²/2q² + i3πω_p²ω/(2q³v_F³) [FT-R7×2].
- 2101.08263 Eqs. (S.13)–(S.16): Lindhard with ω → ω + iΓ_p and the "causal" branch [FT-R7]. Eq. (S.30): S = (2q²/e²)Im ε [UNRESOLVED]. SM:
  "Causality also implies W(q,−ω) = −W(q,ω)"; the acausal choice suppresses the rate by up to 10⁷ [FT-R7×2].
- 1512.04533 Eq. (11): S(E_D,q) = 2∫d³p₂d³p₄(2π)⁴δ⁴(⋯)f₂(1 − f₄) [UNRESOLVED]. Eq. (12): S = (m_e²T/π|q|)[z/(1 − e^{−z})](1 + ξ/z);
  Eq. (14): S ≃ (m_e²E_D/π|q|)Θ(|q|v_F − |E_D|) [FT-R7] (arXiv PDF (3.2)–(3.4)).

### 4.2 Truncation chain and the conserving response [D]
1. WP0-v2 (3.3) with one density operator, then WP0-v2 (5.4)/(5.5) at clamped nuclei. This is exact for a dark photon (total charge), and
   for an electron-only coupling at ω ≫ ω_D up to O(κ_BO⁴). Ions enter only through pairing.
2. Reference: Nambu–Eliashberg with Δ_BCS(iν) from α²F and μ*. BCS limit: Δ_BCS constant, λ_ep T_c/ω_D → 0, ω ≪ ω_D.
3. **Conserving response (R3)**: Coulomb RPA plus the pairing-channel ladder (generalised RPA),
  R̃^{GRPA}(q,ω) = Π^N₃₃ + Π^N₃₂[Π^N₂₂(0,0) − Π^N₂₂(q,ω)]^{-1}Π^N₂₃ (+ amplitude channel Π^N₃₁…, zero under particle–hole symmetry),
  ε(q,ω) = ε_bg − v_C(q)R̃^{GRPA}(q,ω),   S_ee = (2q²/e²)(1 − e^{−βω})^{-1}Im[−1/ε],                                                [4.1]
  Π^N_ij = −TΣ_νV^{-1}Σ_k tr[τ^N_iG^N(k+q,iν+iΩ)τ^N_jG^N(k,iν)] continued iΩ → ω + i0 (retarded, CONVENTIONS §2); Π^N₂₂(0,0) = 2/g_pair by
  the gap equation (Goldstone).
   - **K2:** at q = 0 per k, Π^N₃₃ = 4Δ_BCS²/(E_k(4E_k² + Ω²)), Π^N₃₂ = −2Δ_BCSΩ/(E_k(⋯)), Π^N₂₂ − Π^N₂₂(0) = −Ω²/(E_k(⋯)). So R̃^{GRPA}(0,ω) ≡ 0 after
     the k-sum for every ω, while the bare Π^N₃₃(0,ω) ≠ 0. This is standard (Anderson; Nambu); both referees re-derived it.
   - **The bare bubble, 2609.06423 Eq. (7), is not conserving.** Its coherence factor → Δ_BCS²/E_k² ≠ 0 at Q → 0 (K3). This gives a spurious
     1/Q² term in ε_BCS and pair-breaking weight at ω > Qv_F (the region of their Fig. 2 where Im ε_BCS is finite above the red curve). The
     conserving theory suppresses that weight by (Qv_F/ω)² [E]. **This is not a source error, and v3 credits the source (A-V5, B-V20):**
     2609.06423 itself adds the phase-exchange polarisation Π_θ (§IV, Fig. 3), states that it is suppressed relative to Π_QP by
     Δ²/(v_FQ)² ~ (ξ_coh⁻¹/Q)², and bounds the relative error by 1/25 for ω > 5Δ [FT-R7×2].
   - The DM region (ω < qv_max < qv_F) never enters the artefact region, so their DM conclusion stands. There the vertex correction is
     O((Δ_BCS/v_Fq)²) ≤ (v_max/2v_F)² = 0.04 for Al (K16). **This bound is 2609.06423's** (above); v2 presented it as WP4's own. Neither work
     computes the vertex, so RG1 stays open.
4. Drop the pairing vertex: [4.1] → 2609.06423 Eq. (8).
5. Δ_BCS → 0: Lindhard (2101.08263 Eq. (S.13) with Γ_p → 0) on the retarded branch. T → 0 and the free gas give 2101.08263 Eq. (S.34)
   = 1512.04533 Eq. (14) via (S.30), which is WP0-v2 (4.1) at T = 0. At T > 0, the z/(1 − e^{−z}) of 1512.04533 Eq. (12) is exactly the
   (1 − e^{−βω})^{-1} of WP0-v2 (4.1) [D] (B checked the factorisation).
6. ω ≪ qv_F, q ≪ k_F: 2101.08263 Eq. (3) with Re ε = **k_TF²/q²** (K1: the Lindhard bracket → 1).

**(4.3) DM-region closed form [D].** Hypotheses: clean; T = 0; quasiclassical (Δ_BCS/E_F → 0, N(0) constant over ω); bare or GRPA bubble
(equal to O(Δ_BCS²/v_F²q²)); 2Δ_BCS < ω < qv_F − q²/2m_e (Lindhard Q₊ < 1). With ω ≤ qv_max, Q₊ < 1 is guaranteed for
q < 2k_F(1 − v_max/v_F) = 4.24 keV in Al (K28). That is all of the DM kinematics for m_χ ≲ 0.80 MeV (q_max = 2m_χv_max), and only part of it
above (A-V19; v2 wrote "where all DM kinematics lies", which is false for q ≳ 4.2 keV). Under these hypotheses ξ′ − ξ = v_Fq cosθ_k + q²/2m_e
can be satisfied for every pair (E₁, E₂) with E₁ + E₂ = ω, the ξξ′ term of the coherence factor averages out, and
  Im ε^{BCS}(q,ω) = 𝔤_I(ω/Δ_BCS) Im ε^{nor}(q,ω),
  𝔤_I(y_BCS) = (1/y_BCS)∫₁^{y_BCS−1}dy′_BCS[y′_BCS(y_BCS−y′_BCS) + 1]/√((y′_BCS² − 1)((y_BCS−y′_BCS)² − 1)) = (1 + 2/y_BCS)E(k) − 4K(k)/(y_BCS + 2),   k = (y_BCS − 2)/(y_BCS + 2),        [4.2]
with E, K complete elliptic integrals of modulus k. Derivation of the closed form: 𝔤_I = 𝔤_II + (2/y_BCS)∫dy′_BCS/√(⋯). The last integral is
4K(k)/(y_BCS + 2), and 𝔤_II (numerator y′_BCS(y_BCS−y′_BCS) − 1) is the Mattis–Bardeen form (1 + 2/y_BCS)E(k) − (4/y_BCS)K(k) (K4: both to
10⁻¹²; both referees re-derived it). **Not new:** the case-I elliptic form and its difference from Mattis–Bardeen are in P. B. Allen, PRB 3, 305 (1971), which 1604.06800 cites
(coordinator erratum, raised by the WP7-B1 referees). v3's derivation and K4 are a re-derivation; the claim of novelty is dropped.
Values: 𝔤_I(2⁺) = π/2 exactly (a step), 1.418 (2.5), 1.211 (4), 1.151 (5), 1.050 (10), 1.001 (100); 𝔤_I − 1 = (2ln(2y_BCS) − 1)/y_BCS² + …
for y_BCS ≫ 1 (K32).
**Reading of 𝔤_I (replaces the v2 sentence that FALLS, A-V7, B-V5).** 𝔤_I is the ratio Im ε^{BCS}/Im ε^{nor}, i.e. the production-rate ratio at
fixed screening. It is contained in 2609.06423's Eqs. (9)–(10), since both keep Im ε_BCS. It is distinct from their "agreement for ω ≳ 5Δ",
which compares |ε_BCS|²/|ε_Lin|² (screening). Rate_BCS/rate_Lindhard = 𝔤_I applies when the Lindhard rate uses Im ε^{nor}, e.g. 2101.08263,
and up to the screening correction [4.2′].
**(4.3′) Screening correction [D, sketch] (corrects v2's "Re ε^{BCS} = Re ε^{nor}[1 + O(Δ_BCS²/v_F²q²)]", which was asserted, A §2.3).**
Hypotheses as for [4.2], plus k_TF ≫ q and a conserving response (no weight at ω > qv_F). The two retarded ε differ only by
δIm ε = Im ε^{nor}[𝔤_I(y_BCS)Θ(y_BCS − 2) − 1], with Im ε^{nor} = (π/2)(k_TF²/q²)ω/(qv_F). Kramers–Kronig, (2/π)P∫dω′ω′δIm ε(ω′)/(ω′² − ω²), gives
  Re ε^{BCS} = Re ε^{nor}[1 + (Δ_BCS/(qv_F)) 𝔰_BCS(y_BCS) + O(Δ_BCS²/q²v_F²)],   𝔰_BCS(y) = P∫₀^∞dy′ y′²[𝔤_I(y′)Θ(y′ − 2) − 1]/(y′² − y²),
  L^{BCS} = 𝔤_I L^{nor}[1 − 2(Δ_BCS/(qv_F)) 𝔰_BCS(y_BCS) + …]   (Re ε ≫ Im ε).                                                        [4.2′]
Properties: 𝔰_BCS(0) = ∫₀^∞[𝔤_IΘ(y − 2) − 1]dy = 0, which K32 checks to 10⁻¹⁴: the static screening is unchanged at this order. 𝔰_BCS has a log
singularity at y = 2 from the case-I step. 𝔰_BCS(5) = 1.05, and 𝔰_BCS ≈ 5/y for y ≳ 10 [E, quadrature]. In the DM region Δ_BCS/(qv_F) ≤
(v_max/v_F)/y_BCS, so |δL/L| ≤ 2(v_max/v_F)𝔰_BCS(y)/y, reached only at the kinematic edge q = ω/v_max and falling as 1/q away from it. The
leading Re correction is therefore first order in Δ_BCS/(qv_F), not second, with a coefficient that vanishes at ω → 0. 2609.06423's full
Eq. (9) contains it; their Eq. (10) drops it.
*Sign (VER-A N3).* 𝔰_BCS > 0 for every y computed (0.5–50; K34 checks 2.2–10), so the superconductor screens more strongly and **the term lowers L**:
L^{BCS} < 𝔤_IL^{nor}. Near y = 2 the log singularity of 𝔰_BCS makes the term large and positive on both sides.
*Validity domain (R9; VER-B N1, VER-A N2) [E].* [4.2′] is a first-order expansion, valid only for 2(Δ_BCS/qv_F)𝔰_BCS(y) ≪ 1. At the Al edge
q = ω/v_max (K34):
| y_BCS | 2.2 | 2.5 | 3 | 5 | 10 |
|---|---|---|---|---|---|
| \|δL/L\|, KK to ∞ | 1.42 | 0.88 | 0.53 | 0.16 | 0.04 |
| \|δL/L\|, KK cut at ω′ = qv_F (Y = y_BCSv_F/v_max) | 1.04 | 0.57 | 0.30 | 0.07 | 0.01 |
So **the expansion fails for y_BCS ≲ 3.5 near the edge**: there L^{BCS} = 𝔤_IL^{nor} is uncontrolled. That is where the 𝔤_I step (π/2) matters
most, and where 2609.06423 reports that |ε_BCS|² and |ε_Lin|² deviate. Use there the full KK of Im ε^{BCS} including ω′ ≳ qv_F (RG9), or
quote the region as uncontrolled. The KK integrand has Im ε^{nor} ∝ ω′ only for ω′ ≪ qv_F, and the cut row shows the size of that
uncertainty. At y_BCS = 5 the effect is **8–16% [E]**: 16% with the KK to ∞, about 7% with a sharp cut at Y ≈ 13 (VER-A's tail estimate:
8%). Away from the edge (q ≫ ω/v_max) all entries scale down as ω/(qv_max).
The same ξ-decoupling in the dirty limit (ℓ_mfp ≪ ξ_coh) gives MB for the transverse/absorption channel. **One mechanism, momentum
relaxation on the scale of Δ_BCS (Doppler v_Fq or disorder), gives both 𝔤_I and MB [D].**
*Validity with numbers* (Al: Δ_BCS = 0.17 meV, E_F = 11.7 eV, v_F = 6.8×10⁻³; WSi: Δ_BCS = 0.26 meV, E_F = 7.0 eV, as 2609.06423).
v_max/v_F = 0.39, so ω < qv_F always. q ≥ 2Δ_BCS/v_max = **0.13 eV** ≪ k_F = 3.5 keV (A-V19, B-V6; v2 wrote "0.13 keV"). Δ_BCS/E_F ≈ 1.5×10⁻⁵.
qξ_coh ≥ 2v_F/(πv_max) = 1.6 (ξ_coh = v_F/πΔ_BCS = 12.7 eV⁻¹; K16), so the regime q ≲ 1/ξ_coh is **not reachable** for halo DM with
ω ≥ 2Δ_BCS in clean Al (this answers WP5 gap R5). T ≪ Δ_BCS: thermal QPs ∝ e^{−Δ_BCS/T} ~ e^{−200} at 10 mK. Clean limit qℓ_mfp ≫ 1 (§4.5).
Si/Ge are not superconductors.
*Leading corrections beyond L15 [D for the form; E for size].* (i) Non-thermal QPs, x_qp ~ 10⁻⁸–10⁻⁶ in Al films: replace p_i by a
generalised Gibbs state. This adds a sub-gap scattering channel ω < 2Δ_BCS with case-I factor ½(1 − Δ_BCS²/E₁E₂) and rate ∝ x_qp; WP0-v2
(4.1) holds with f_qp. (ii) Strong coupling (complex Δ_BCS(ω), Eliashberg): Holstein phonon-assisted absorption above 2Δ_BCS + ω_{Qν} (the WP3
X+ analogue; sector (2, ≥1) of §8). (iii) Plasmon tail and GSRF local fields (2101.08263 Eq. (S.19)): a Mermin-type relaxation (§4.5). A
damped complex G_LF violates positivity WP0-v2 (4.4) [D]; that 2101.08263 notes this is [UNRESOLVED]. (iv) The GRPA vertex [4.1] (RG1).
(v) The screening term [4.2′].
*Source discrepancies [D + FT].* (a) 2101.08263 Eq. (3): Re ε should read λ_TF²/q² (= k_TF²/q²), given their Eqs. (S.13)–(S.15) (λ_TF = √3ω_p/v_F)
(K1) [FT-R7×2]. The illustrative scaling W ~ ωq is off by a factor 4; their numerics use (S.13) and are unaffected. (b) 1512.04533 Eq. (13)
[(3.3) in the arXiv PDF]: e₋ = (E_D − q²/2m)²/(q²/2m) should be (E_D − E_q)²/(4E_q) (K7; agrees with 2101.08263 Eq. (S.34)) [FT-R7×2]. It
affects T > 0 and the edges, not Eq. (14). (c) 2101.08263 attributes W(q,−ω) = −W(q,ω) to causality [FT-R7×2]. The relation follows from the
**reality** of the time-domain density kernel, R(q,−ω) = R(−q,ω)* (ε(q,−ω*) = ε(−q,ω)*), together with inversion or T (q ↔ −q). Causality
gives only analyticity for Im ω > 0. (v2's own replacement, "causality alone gives ε(q,−ω) = ε(−q,ω)*", was also misattributed: A-V12, B-V10.)
The relation fails in P- and T-broken superconductors ([3.1]). (d) 2609.06423 Eq. (9) prefactor is consistent with WP0-v2 (3.3) (K8; B).
*Remark (no longer listed as a defect; A-V11, B-V9, §11A-2).* 2609.06423 Eqs. (4) and (7)–(8) are time-ordered: −i0⁺ on the negative-energy
pole [FT-R7×2]. Eq. (4) is the correct T = 0 Feynman propagator. For ω > 0 at T = 0 the time-ordered Π equals the retarded Π identically,
real and imaginary parts alike (K25), and the paper works only there ("for ω > 0"). Do not use these expressions for ω < 0, in KK
transforms, in sum rules or at T > 0. **Status: DERIVED** (the step to a conserving theory, and the correction sizes, are E; [4.2′] is D, sketch).

### 4.4 Branch cut / causality (2101.08263) [D]
WP0-v2 (4.1)–(4.2) fix the analytic structure without complex logarithms: Im ε = −v_C Im R̃ = (v_C/2)(1 − e^{−βω})S^{prop}, with
S^{prop} ≥ 0 a phase-space integral (their (S.31)/(S.34)); Re ε = ε_bg + KK[Im ε] (R^∞ = 0, WP0-v2 (4.2)). The "acausal branch" of
2101.08263 is a non-retarded continuation, and the source states that it **suppresses** the rate by up to 10⁷ [FT-R7×2]. v2's mechanism
("negative-frequency weight at ω > 0") was asserted, not derived, and is withdrawn (B-V11). The ω + iΓ_p prescription of (S.13) is **not
conserving**; the conserving relaxation form is Mermin's [4.3].

### 4.5 Film geometry and disorder (G9)
**[D, relaxation-time approximation; q ≪ k_F, q ≪ k_TF]** Mermin's conserving relaxation, γ_rel = 1/(relaxation time):
  ε_Mer(q,ω) = 1 + (ω+iγ_rel)[ε_Lin(q,ω+iγ_rel) − 1] / {ω + iγ_rel[ε_Lin(q,ω+iγ_rel) − 1]/[ε_Lin(q,0) − 1]}.                          [4.3]
Derivation of the limits (K11, rebuilt; B-V12 noted that the v2 check only tested the quoted asymptotes). For q ≪ k_F,
(ε_Lin(q,z_rel) − 1)/(ε_Lin(q,0) − 1) = 𝔣_Lin(z_rel) = 1 − (z_rel/qv_F)artanh(qv_F/z_rel), z_rel = ω + iγ_rel. *Diffusive* (qv_F ≪ |z_rel|): 𝔣_Lin = −q²v_F²/(3z_rel²)[1 + O((qℓ_mfp)²)],
and [4.3] at ω ~ D_diffq² ≪ γ_rel gives ε → 1 + k_TF²D_diff/(D_diffq² − iω), D_diff = v_Fℓ_mfp/3. For k_TF² ≫ q², ω/D_diff this gives
L = ω/(k_TF²D_diff), exactly the Drude ωγ_rel/ω_p² (k_TF²D_diff = ω_p²/γ_rel), for any ω/(D_diffq²). *Ballistic* (|z_rel| ≪ qv_F, retarded branch):
𝔣_Lin = 1 + iπz_rel/(2qv_F) − z_rel²/(qv_F)² + …, and L = πωq/(2k_TF²v_F)[1 + O(1/qℓ_mfp)]: the Lindhard Im ε survives inside Mermin at first order for
ω ≪ γ_rel (A-V13). Hence
  L_Mer/L_Drude → 1 (qℓ_mfp ≲ 1),   → πqℓ_mfp/6 (qℓ_mfp ≫ 1),   for q ≪ k_F, k_TF and ω ≪ γ_rel   (K11).                         [4.4]
These are asymptotes. At qℓ_mfp = 1.5 the ballistic formula gives 0.79 < 1 and does not apply.
- **QROCODILE (2412.16279; v2 claim withdrawn, A-V14, B-V12).** Per both referees' full-text reading [FT-R7×2], the bulk rate and limits use the
  Lindhard ε with ω + iΓ (Γ = 0.1E_F). Drude enters only the thin-layer Maxwell solution, for the directional anisotropy (their SM Fig. S1).
  So v2's "Drude underestimates L by πqℓ_mfp/6, conservative for their limit" is REFUTED and dropped. The relevant comment on their bulk ε is
  §4.4's: ω + iΓ Lindhard is not conserving, and Mermin [4.3] is the conserving fix. For amorphous WSi (E_F = 7 eV): k_F = 2.67 keV and
  k_TF = 3.56 keV, so q = 1–5 keV is not ≪ k_F or k_TF. ℓ_mfp ≈ 0.3–1 nm gives k_Fℓ_mfp ~ 1 (Ioffe–Regel); with ℓ = v_F/Γ ≈ 1.5 nm, qℓ ≈ 7–37
  (K31). The RTA–Mermin model [4.3]–[4.4] is therefore **outside its validity** for WSi at DM momenta, and no WSi correction factor is quoted.
  An ab initio disordered-film ε is RG2.
- Al films (ℓ_mfp ≳ 10 nm): qℓ_mfp ≳ 50 and q ≪ k_F over most of the DM range, so Lindhard holds. BCS: [4.2] with ε^{nor} → ε_Mer. In the
  dirty regime the ξ-decoupling holds independently of v_Fq (Anderson theorem).
**Film geometry [D for independent electrons in a slab; C with images].** DM states are plane waves, so the golden rule needs only the
diagonal S(q,q;ω). For a slab of thickness d_film:
  S_film(q_∥,q_z,ω) = ∫(dq′_z/2π) d_film sinc²[(q_z−q′_z)d_film/2] S_bulk(q_∥,q′_z,ω) + S_surf,                                       [4.5]
with S_surf the image/surface-mode term (specular model). Relative correction O(1/qd_film) [E]: 10% at q = 0.2 keV, d_film = 10 nm; ≲ 2% for
q ≳ 1 keV. Surface plasmons (ω_p/√2 ≈ 10 eV) lie outside DM kinematics.

### 4.6 Quasiparticle generation (G9; WP5 hand-over) [D for the seed; spec for the cascade]
Prompt final state Λ = (E₁, E₂), the (2,0) sector of §8 (WP0-v2 (7.1)). From [4.2] at fixed (q,ω):
  P(E₁|ω) = [E₁E₂ + Δ_BCS²]/[√(E₁² − Δ_BCS²)√(E₂² − Δ_BCS²)] / [ω 𝔤_I(ω/Δ_BCS)],   E₂ = ω − E₁,   E₁ ∈ [Δ_BCS, ω − Δ_BCS]  (normalised, K15).  [4.6]
For ω ≫ Δ_BCS this is flat: a normal-state hot e–h pair (agrees with WP5 §5). Cascade: Chang–Scalapino/Kaplan kinetic equations with
coherence factors, QP scattering (1 − Δ_BCS²/E₁E₂), recombination and pair-breaking (1 + Δ_BCS²/E₁E₂), and kernels α²F(ω′) from EPW (Al: fine
grids 60³/30³, ~10³ CPU-h). Phonon escape into the substrate is by acoustic mismatch with transmission t_esc (input). Outputs: the
pair-breaking efficiency **η_pb = Δ_BCS⟨N_qp⟩/ω**, with **N_qp the number of quasiparticles (not pairs; NOTATION v3)**; its variance (F_qp);
time constants. **N_qp = 2 exactly for ω < 4Δ_BCS** (A-V8, B-V16; v2 said 3Δ_BCS). Derivation: a QP of energy E relaxes by emitting phonons
of energy ≤ E − Δ_BCS, and pair breaking needs a phonon ≥ 2Δ_BCS, so E ≥ 3Δ_BCS is required. The larger prompt QP has E₁ ≤ ω − Δ_BCS, so a
third QP needs ω ≥ 4Δ_BCS (K27); recombination phonons (2Δ_BCS) re-break one pair and do not change N_qp. Hence η_pb = 2Δ_BCS/ω for
ω < 4Δ_BCS, → 1 at ω = 2Δ_BCS⁺ (WP5 (W13)). v1's 2Δ_BCSN_qp/ω double-counted (η_pb = 2 at threshold), and v2 dropped the factor 2.
Convergence: energy grid ≤ Δ_BCS/20; closed-system energy conservation to 10⁻⁴. t_esc is phenomenological (RG7).

---
## 5. Dirac and narrow-gap materials: L16

### 5.1 Source formulas (source notation: κ ≡ ε_bg, Λ ≡ Λ_D, g ≡ g_deg, W ≡ L, ε (mixing) ≡ κ_mix, g_D ≡ y_χ)
- 2101.08263 Eq. (4): W_Dirac = (e²/12πκ²v_F)Θ(ω − v_Fq)Θ(ω_max − ω). SM (S.21)–(S.22): Im ε_Dirac = (e²/12πv_F)√(1 − 4Δ²/s)(1 + 2Δ²/s)Θ(s − 4Δ²)
  **without** κ, s = ω² − v_F²q², and W = that/κ². [FT-R7×2]
- 1708.08929 Eq. (2.1): L ⊃ −(ε/2)F_μνF′^{μν} + eJ_EM·A (total charge). Eq. (2.6): (ε_r)_Dirac = 1 + (e²g/4π²κv_F)∫₀¹dx x(1−x)ln[(2v_FΛ)²/(Δ² − x(1−x)s)]
  + i(e²g/24πκv_F)√(⋯)(⋯)Θ(⋯). App. A Eq. (A.8): ε_r sums the Dirac bands only, with e²/κ. [FT-R7×2]
- 1708.08929 Eq. (3.7): ⟨|ℳ|²⟩ ≃ 16m_e²m_χ²g_D²e²ε²/((q² − m_{A′}²)²|ε_r|²). Eq. (3.11): F_med = 1/ε_r, σ̄_e = 16πμ²ε²α_EMα_D/q₀⁴ in vacuum.
  Eqs. (3.13)–(3.14): R_tot ∝ (288π⁴κ²v_F²/(e⁴g²))·I(v_F, Λ′, m_χ), with Λ′ = Λexp(12π²κv_F/(e²g)); Fig. 4 "in-medium effects included".
  Footnote 5: e₀² = e²/κ at the cutoff. Eqs. (4.4)–(4.5): absorption with ε²_eff = ε²m⁴/|m² − Π|², R ∝ ε²_eff Im ε_r, Π = ω²(1 − ε_r). [FT-R7×2]
- 1910.02091 Eqs. (2.3)–(2.7): vacuum σ̄_e; F_med = D⁰⁰/D₀⁰⁰ with D⁻¹ = D₀⁻¹ − iΠ, D₀ the vacuum propagator; F_med = q²/(q² − Π⁰⁰). Eq. (3.3): Π
  is the Dirac loop with (−ie)²g/κ. Eqs. (3.13)–(3.14): Π_ii/κ → Π_ii/κ_ii, F_med = [1 + (q_x²v_{F,z}²/κ_xx + q_y²v_{F,y}²/κ_yy + q_z²v_{F,z}²/κ_zz)π(q̃²)/q²]^{-1}
  (the typo q_x²v_{F,z}² is already in the 00 entry of (3.13)). Text after (3.8): effective charge e/√κ at the cutoff. Eqs. (2.25)–(2.27):
  absorption with |ε_med,x|² = ε²m⁴/|m² + Π₁₁|², Γ_x = |ε_med|²Im Π₁₁/m, Π₁₁ ∝ π/κ_xx. [FT-R7×2]

### 5.2 Truncation chain from WP0-v2 [D]
1. WP0-v2 (3.3) with a density coupling, then (5.3)/(5.4): S = (2q²/e²)Im[−ε^{-1}] with the **total** ε (dark photon). For an electron
   scalar at clamped nuclei the same holds by (5.5).
2. Clamped nuclei: for ω above the polar-phonon band this holds to O(κ_BO⁴); otherwise ε_bg → ε_bg(ω) with ionic poles.
3. Split R̃ = R̃_D + R̃_bg: the Dirac bands within Λ_D plus all remote bands. For ω ≪ E_bg (remote gap) and q ≪ 2π/a_lat,
   1 − v_CR̃_bg(q,ω) → ε_bg (static, local background; LFE neglected).
4. Two-band k·p to O(k): massive Dirac Hamiltonian with v_F and half-gap Δ_D. 5. R̃_D at IP (= RPA) level, T = 0, |E_F| < Δ_D. 6. Isotropy.
Result:
  ε = ε_bg − v_CR̃_D = ε_bg ε_r,   ε_r = 1 + δε_D/ε_bg,   L = Im δε_D/|ε_bg + δε_D|² → Im δε_D/ε_bg²  (|δε_D| ≪ ε_bg),            [5.1]
Im δε_D = (e²g_deg/24πv_F)√(1 − 4Δ_D²/𝓈)(1 + 2Δ_D²/𝓈)Θ(𝓈 − 4Δ_D²), 𝓈 = ω² − v_F²q². For g_deg = 2, Δ_D = 0 this is e²/12πv_F (K5: direct
two-band Lindhard integral). Hence 2101.08263 Eq. (4) and its gapped SM form follow **exactly** [D] (both referees verified this against
(S.21)–(S.22)).
**Anisotropy [D].** The background enters the longitudinal ε as q̂·ε_bg·q̂, not term by term inside Π⁰⁰:
  ε(q,ω) = q̂·ε_bg·q̂ − v_C R̃_D(q̃,ω),   R̃_D ∝ (Σ_i q_i²v_{F,i}²)π(q̃²)/(v_{F,x}v_{F,y}v_{F,z})  (no ε_bg inside).                     [5.2]
1910.02091 Eq. (3.14) equals ε_bg,eff/ε only for isotropic ε_bg. For anisotropic ε_bg it is not κ_eff·(1/ε) for any κ_eff (B). It carries the
typo q_x²v_{F,z}² for q_x²v_{F,x}², already present in the 00 entry of Eq. (3.13) (B-V3) [FT-R7×2]. ZrTe₅ clamped-ion
ε_bg = (187.5, 9.8, 90.9) (1708.08929 table) [FT-R7]. Since L ∝ 1/(q̂·ε_bg·q̂)², the background alone makes the **q ∥ y rate the larger one**,
by (ε_bg,xx/ε_bg,yy)² ≈ 366 over q ∥ x (221 with 1910.02091's DFT values 308.4, 20.75; K21), before the Dirac anisotropy (A-V3). That is a
large daily-modulation lever arm, misrepresented both by the harmonic mean (1708.08929) and by the per-component rule (1910.02091) [D for
the structure; E for the impact].

### 5.3 The ε_bg² finding: REFEREED (R×2 CONFIRMED against the full text)
**Claim [D + FT-R7×2].** Under the campaign convention (CONVENTIONS §9: σ̄_e defined in vacuum, all screening in S), 1708.08929 Eqs. (3.7),
(3.11), (3.13)–(3.14) and 1910.02091 Eqs. (2.7), (3.14) overstate the kinetically mixed dark-photon scattering rate by **ε_bg² exactly**. This
holds for any δε_D (not only |δε_D| ≪ ε_bg). It is ×1600 at the 1708.08929 benchmark ε_bg = 40 and ×640 for its ZrTe₅ curve in the source's isotropised (harmonic-mean, 25.3) model; the true ZrTe₅
ratio is direction-dependent, (q̂·ε_bg·q̂)² (VER-B N3). In 1910.02091 it is ε_bg,ii² for q along principal axis i. Off-axis, their per-component rule differs from [5.2] by a direction-dependent
factor. The plotted scattering reach is optimistic by the same factor in rate.
*The three facts, verified in both full texts by both referees.* (i) **Coupling:** kinetic mixing to eJ_EM, i.e. to all charges, remote bands
included (1708.08929 Eq. (2.1); 1910.02091 §2). (ii) **σ̄_e in vacuum**, from the free amplitude (1708.08929 Eqs. (3.8), (3.10), (3.11);
1910.02091 Eqs. (2.3)–(2.4)). (iii) **F_med = 1/ε_r is what the plotted limits use**, with ε_r = 1 + δε_D/ε_bg = ε/ε_bg: 1708.08929 Eq. (A.8)
(Dirac bands only, e²/κ), Eqs. (3.13)–(3.14) and Fig. 4; 1910.02091 Eq. (3.3) (1/κ in the loop), Eq. (2.6) (vacuum D₀) and Eqs. (2.7), (3.14).
*Derivation [D] (K22).* For a field that couples to J_EM, the remote-band polarisation is part of Π_L, so the physical longitudinal dielectric
function is ε = ε_bg + δε_D = ε_bg ε_r. The scattering amplitude is ∝ κ_mix e y_χ/(q²ε). With the bare (unit-charge) vertex of the source
(1708.08929 Eq. (3.6)), the golden-rule sum is Σ_f|f|²δ(ω − ω_f) = (q²/πe²)Im ε = (q²/πe²)Im δε_D, so
  Rate_URF ∝ Im δε_D/|ε_bg + δε_D|²,   Rate_src ∝ Im δε_D/|ε_r|² = Im δε_D·ε_bg²/|ε_bg + δε_D|²,   Rate_src/Rate_URF = ε_bg²  (exact).        [5.3]
For an anisotropic background, ε_bg → q̂·ε_bg·q̂ in [5.3] (K22). URF here means WP0-v2 (5.3)/(5.4), S = (2q²/e²)Im[−1/ε].
*Corrected explanation (replaces v2's sentence, which was wrong as an explanation; A §1.4; disagreement settled in §11A-1).* v2 said the
ε_bg² growth of 1708.08929 Eq. (3.14) "reflects absorbing the '1' of ε_r into Λ′". **That is not the cause.** Write Re ε_r = 1 + (α̃/6π)𝓁 with
𝓁 = ln((2v_FΛ_D)²/|𝓈|) and α̃ = αg_deg/(ε_bgv_F), so (e²g_deg/24π²ε_bgv_F) = α̃/6π. Absorbing the 1 gives Re ε_r = (α̃/6π)ln((2v_FΛ′_D)²/|𝓈|) with
Λ′_D = Λ_D exp(3π/α̃) = Λ_D exp(12π²ε_bgv_F/(e²g_deg)), the Λ′ of 1708.08929. Then
  1/|ε_r|² = (6π/α̃)²/|𝓛′_D|²,   1/|ε|² = 1/(ε_bg²|ε_r|²) = (6π/(α̃ε_bg))²/|𝓛′_D|²,   𝓛′_D ≡ ln((2v_FΛ′_D)²/|𝓈|) + i(6π/α̃)Im ε_r.
The source prefactor 288π⁴κ²v_F²/(e⁴g²) is exactly ½(6π/α̃)², which carries the explicit ε_bg². In the correct theory the prefactor is
(6π/(α̃ε_bg))², and α̃ε_bg = αg_deg/v_F does not depend on ε_bg (K23). **The Λ′_D rewrite is an identity, common to both theories, with the same
I(v_F, Λ′_D, m_χ). The explicit ε_bg² of Eq. (3.14) *is* the omitted 1/ε_bg².** At large ε_bg, 𝓛′_D ≈ 6π/α̃ ∝ ε_bg, so Rate_src tends to an
ε_bg-independent constant while Rate_URF ∝ 1/ε_bg² (B's asymptotics; compatible with this).
*Internal inconsistency of both sources [FT-R7×2].* 1708.08929 footnote 5 sets the cutoff charge to e₀² = e²/κ ("electrons behave as in an
ordinary insulator"), and 1910.02091 (after Eq. (3.8)) quotes e/√κ. At the cutoff their F_med → 1, so their external vertex is the vacuum e,
not e₀. 1708.08929's own sentence below (3.11), "the matrix element scales as e²(q) rather than e₀²", gives the URF result when
e²(q) = e₀²/ε_r = e²/(ε_bgε_r) is inserted.
*Interpretation.* The source rate is the exact rate for a DM coupled **only** to the Dirac-band charge: R_DD = R̃_D/(1 − v_CR̃_D/ε_bg) gives
Im(−R̃_D/ε_r) ∝ ε_bg²Im δε_D/|ε_bg + δε_D|² (both referees verified this). That model is not a kinetically mixed dark photon.
*Independent literature cross-check [FT-R7×2].* 2101.08263 (S.21)–(S.22)/Eq. (4), which shares authors with 1708.08929, has W = Im δε_D/κ², the
URF form. The two papers differ by κ² for the same model, and neither notes it.
*Suggested LIMITS L16 record (coordinator).* "1708.08929 Eqs. (3.7), (3.11), (3.14) and 1910.02091 Eqs. (2.7), (3.14) overstate the
dark-photon scattering rate by ε_bg² (exact) under the campaign σ̄_e convention; absorption by ε_bg (§5.5) [R7 FT, R×2]."

### 5.4 Validity and corrections
*Validity with numbers.* Benchmark Λ_D = 0.2 keV, v_F = 4×10⁻⁴, ε_bg = 40: q ≤ Λ_D; ω ≤ ω^D_max ≈ 2v_FΛ_D = 0.16 eV; α̃ = αg_deg/(ε_bgv_F) = 0.91
(K17), which is marginal for RPA; |E_F| < Δ_D, T ≪ Δ_D; ω ≪ E_bg; q ≪ 2π/a_lat for ε_bg(q) ≈ ε_bg(0). Si/Ge are not Dirac materials.
Narrow-gap generalisation: the Kane model, whose 2-band limit is Dirac with v_F = √(E_g/2m*); split-off bands correct it at O(E_g/Δ_SO) [D].
*Leading corrections [D for the form; E for size].* (i) **Charge renormalisation, both cutoff schemes (A-V4).** With 1708.08929 Eq. (2.6)
taken literally (scale 2v_FΛ_D in the log), the x-integral adds ∫₀¹x(1−x)ln[1/(x(1−x))]dx = 5/18, so
Re δε_D/ε_bg = (α̃/6π)[ln((2v_FΛ_D)²/𝓈) + 5/3] = 0.35 at √𝓈 = 10 meV, a rate factor (1.35)^{-2} = 0.55. With the e^{−5/6}-redefined cutoff (the
v2 value; REF-A attributes it to Eq. (2.7)), (α̃/6π)ln(4Λ_D²v_F²/𝓈) = 0.27, a rate factor 0.62 (K17). Since Λ_D = 0.2 keV is quoted without
fixing the scheme, **the rate factor is 0.55–0.62 (cutoff-scheme spread)**, and [5.1] must keep it. (ii) Excitonic (BSE rung): near 2Δ_D the
Sommerfeld factor 𝒮_F^D = πζ_S^D/(1 − e^{−πζ_S^D}), ζ_S^D = α/(ε_bgv_Fb_D), b_D = √(1 − 4Δ_D²/𝓈), is O(1) near threshold. (iii) Dynamic ionic
background ε_bg(ω) near the polar phonons. (iv) Doping (E_F in a band): an intraband Lindhard term with k_TF² = e²N(E_F)/ε_bg, which removes the
weak-screening advantage for ω ≲ v_Fk_F. (v) Band curvature beyond Λ_D. **Status: DERIVED** (§5.2, §5.3, §5.5).

### 5.5 Dark-photon absorption in the Dirac literature: a factor ε_bg (new in v3; referee finding A-V1′, B §A4) [D]
Hypotheses: kinetically mixed dark photon of mass m_φ absorbed at k_φ → 0 (ω = m_φ); coupling κ_mix to J_EM (total charge); in-medium photon
self-energy of all charges Π^{med}_γ = ω²(1 − ε), equal for both polarisations at k → 0 (diagonal per principal axis for an anisotropic ε); remote
bands transparent at ω (ω ≪ E_bg, ε_bg real). Then the effective in-medium mixing is κ_mix,eff² = κ_mix²m_φ⁴/|m_φ² − Π^{med}_γ|² = κ_mix²/|ε|², and
  Γ_abs = −κ_mix,eff² Im Π^{med}_γ/ω = κ_mix² m_φ Im ε/|ε|² = κ_mix² m_φ Im(−1/ε) = κ_mix² m_φ Im ε_r/(ε_bg|ε_r|²),                                  [5.4]
which is WP0-v2 L9b (Γ = κ_mix²m Im(−1/ε), total ε). The sources (1708.08929 Eqs. (4.4)–(4.5); 1910.02091 Eqs. (2.25)–(2.27)) [FT-R7×2] use
Π = ω²(1 − ε_r), i.e. a Dirac-only self-energy with e²/κ and a vacuum D₀. That gives Γ_src = κ_mix²m_φ Im ε_r/|ε_r|², so
  Γ_abs,src/Γ_abs,URF = ε_bg   (1708.08929);   = ε_bg,ii for polarisation along principal axis i (1910.02091)   (K24).               [5.5]
So **their absorption rates are too large by ε_bg, not ε_bg²**: ×40 at the 1708.08929 benchmark. The 1708.08929 Fig. 5 optimisation ("optimal
κ/g ~ O(10)") inherits the factor [FT-R7, A]. The factor is derived by both referees independently and here (K24). It is not propagated to
their plotted curves in this package. Owner of L9b: flag I10.

---
## 6. Dopants and colour centres as final states (G12, electronic part) [D]
Hypotheses: dilute uncorrelated centres, 𝓃_D a*³ ≪ 1 (Si:P a* ≈ 2–2.5 nm [E], 𝓃_D ≪ 10¹⁹ cm⁻³, below the metal–insulator transition); host
screening dominates; the centre is non-degenerate and gapped, so WP0-v2 Theorem D (H2) holds locally. Per centre, with WP0-v2 (7.2)
RPA+LFE external screening:
  S^D_ab(q,ω) = 𝓃_D Σ_f 2π⟨i|Õ_a(q)†|f⟩⟨f|Õ_b(q)|i⟩δ(ω − E_f + E_i),   ñ_e(q) = Σ_G (ε^{-1}_host)_{G0}(q,ω) n_e(q+G),                  [6.1]
with Õ = O for spin and transverse operators except as screened by WP0-v2 (5.3) (j_T via local fields; spins via the triplet W^{scr} ladder plus f_xc^T, WP1-v3 IF-13). The
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
  needed. *Worked example (corrected, A-V20; K29).* Validity needs v ≪ v*, v* = √(2|Δ_χ|/m_χ) for ω_ν ≪ |Δ_χ|. v2's example, m_χ = 1 MeV and
  |Δ_χ| = 1 eV, has v* = 1.41×10⁻³ < v_max = 2.65×10⁻³ (v_max/v* = 1.87). It lies outside the stated validity: the Doppler corrections are O(1),
  and [7.2] is there only an order-of-magnitude estimate. Inside validity: m_χ = 1 MeV, |Δ_χ| = 50 eV gives q* = 10 keV, v* = 1.0×10⁻² and
  v_max/v* = 0.27, so the corrections are ≲ 27% at the halo edge and ~8% at v ~ v₀. For Si, x_R = q*²/(2M⟨ω⟩) ≈ 0.05 (⟨ω⟩ ≈ 40 meV), so it is
  one-phonon dominated [E]. Magnons are cut by F^{mag}_j(q*).
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
*Added hypothesis (G5), restated on few-quasiparticle states in R9 (A-V17, B-V17; VER-A N1, VER-B N2).* Write H_d ≡ Σ_{n,m}𝒬^{D-g}_{n,m}H𝒬^{D-g}_{n,m}
(the sector-diagonal part) and H_off ≡ H − H_d. v3 assumed the operator norm ‖H_off‖ ≤ 𝔥_off. **That is vacuous for bulk targets:** for local
e–ph and e–e terms ‖H_off‖ is extensive (∝ volume; K33 (iii)). The restated hypothesis only involves the states actually probed:
  (G5′)  𝔥_off(ψ_b) ≡ sup_s ‖H_off e^{−iH_ds}ψ_b‖/‖ψ_b‖ < ∞,   ψ_b = O_b|i⟩ (a few-quasiparticle state, intensive 𝔥_off).
Exact number conservation, [H, U_qpN̂U_qp†] = 0, gives 𝔥_off = 0, which (G1)'s on-shell width Γ_qp > 0 excludes. *Size [E]:* if ψ_b decays by
the golden rule into a continuum of width W_c, then ‖H_offψ_b‖² = Σ_f|⟨f|H_off|ψ_b⟩|² = ΓW_c/2π. Hence 𝔥_off ~ √(Γ·W_c/2π) ≫ Γ, with
Γ = Γ_qp + Γ_ph (K33 (i), (ii)). It is **not** ~Γ, as v3 stated. v3's sentence "(G5) is the quantitative content of the bin condition (c)" is
**dropped**: (G5′) leads to the stricter sufficient condition Δω_bin ≫ √(ΓW_c), and (c) stays a separate [C].
*Theorem D-g.* (a) [D given U_qp **and (G5′)**] Take a bin function f_Δ(x) = g_bin(x/Δω_bin)/Δω_bin with g_bin ≥ 0, ∫g_bin = 1 and
∫|s||ĝ_bin(s)|ds < ∞, and the binned spectrum S^{bin}_ab(ω) = ⟨i|O_a†f_Δ(ω + E_i − H)O_b|i⟩. Then
  S^{bin}_ab = Σ_{n,m} S^{(n,m)}_ab + C^{cross}_ab,   S^{(n,m)}_ab ≡ ⟨i|O_a†𝒬^{D-g}_{n,m} f_Δ(ω + E_i − H_d) 𝒬^{D-g}_{n,m}O_b|i⟩,
  |C^{cross}_ab| ≤ c_g 𝔥_off(ψ_b) ‖O_a|i⟩‖ ‖O_b|i⟩‖/Δω_bin²,   c_g = (1/2π)∫|s||ĝ_bin(s)|ds  (= 1/π for a Gaussian bin; K30).                 [8.1′]
Each S^{(n,m)} is a restriction by orthogonal projectors, hence Hermitian PSD: f_Δ(·−H_d) commutes with every 𝒬^{D-g}_{n,m}, so it has no
cross-sector blocks. *Proof of the bound (state-restricted Duhamel):* f_Δ(ω − H) − f_Δ(ω − H_d) = (1/2π)∫dt ĝ_bin(Δω_bin t)e^{iωt}(e^{−iHt} − e^{−iH_dt}),
and (e^{−iHt} − e^{−iH_dt})ψ_b = −i∫₀^t ds e^{−iH(t−s)}H_off e^{−iH_ds}ψ_b, so ‖(e^{−iHt} − e^{−iH_dt})ψ_b‖ ≤ |t| 𝔥_off(ψ_b)‖ψ_b‖. Hence
‖(f_Δ(ω − H) − f_Δ(ω − H_d))ψ_b‖ ≤ c_g𝔥_off(ψ_b)‖ψ_b‖/Δω_bin², and Cauchy–Schwarz with O_a|i⟩ gives [8.1′] (checked on an exact star model,
K33 (ii)). Relative to a typical binned value ~‖O|i⟩‖²/Δω_bin, the cross terms are O(𝔥_off/Δω_bin) ~ O(√(ΓW_c)/Δω_bin) [E]. [8.1′] is
**sufficient but loose**: a resolvent/golden-rule estimate suggests cross terms O(Γ/Δω_bin), which is the bin condition (c), but that is not
what the Duhamel bound proves, so (c) remains [C]. Completeness without double counting is exact only in the conserved-number limit
𝔥_off → 0. For bilinear operators (density, spin, current) acting on a BCS reference, n ∈ {0, 2} at leading order: pair breaking changes n by
2, and only γ†γ† acts on |BCS⟩.
(b) [C] *Sector dictionary (SC).* (0, m): phonons with no broken pairs (electron-following, Bohm–Staver-screened ions; GS analogue); stable
only for ω_{Qν} < 2Δ_BCS, since higher phonons break pairs. (2, 0): conserving GRPA pair-breaking spectrum [4.1]–[4.2] with 𝔤_I (X0
analogue; prompt seed [4.6]). (2, ≥1): Holstein phonon-assisted absorption (X+ analogue, §4.3 (ii)). (0, 0) collective: the phase mode is
lifted to ω_p by Coulomb, the amplitude (Higgs) mode decouples from density at particle–hole symmetry, so no sub-gap n = 0 line at leading
order [D within GRPA]. Assigning the phase and Higgs modes, which are pair (n = 2) composites, to (0,0) is a convention, not a consequence
(A-V17). Normal metals: n counts e–h pairs; phonons Landau-damp into pairs at rate ~ λ_epω_{Qν}, so (0, m) and (2, m−1)
mix within that width.
(c) [C] *Bin condition (replaces (H5)).* The split is unique, and each S^{(n,m)} PSD as a measured spectrum, on energy bins wider than the
decay width of the sector label, Γ_qp(ω) + Γ_ph. This is **not** implied by [8.1′], whose sufficient condition is the stricter
Δω_bin ≫ 𝔥_off ~ √(ΓW_c) (R9; VER-A N1, VER-B N2). Fermi liquid Γ_qp ∝ ω²/E_F (fine for ω ≪ E_F); SC: (2,0) stable until recombination
(≫ 1/Δ_BCS); Dirac semimetal (marginal) Γ_qp ~ α̃²ω, so a unique split needs α̃² ≪ 1: **at the 1708.08929 benchmark α̃ = 0.91 the split is not
unique** and only totals are quotable [E]. Outside the bin condition a declared convention is needed, as DC in WP0-v2 (6.3).
(d) [D] Σ_{n,m}𝓜¹ = 𝓃_eq²/m_e under (G4) (WP0-v2 (4.6)); per-sector first moments are not separately fixed; the bare bubble violates the total
(K2), so a non-conserving (2,0) cannot be paired with any (0,m).
(e) [C] For gapped insulators (Δ_ad ≫ ω_ph) the sectors (0,m)/(2,0)/(2,≥1), with n counting e–h pairs, coincide with GS/X0/X+ of Theorem D
to O(κ_BO^{2(n+1)}) (the WP0-v3 G10 remainder; v3 wrote O(κ_BO^{n+1}), AUDIT-2 m8).
*Scope (AUDIT-2 m9).* (G1) covers fermionic quasiparticle references only. Magnetic insulators, which WP0-v3 G9 removed from Theorem D and
routed to F5, are **not** covered by D-g: open item OW4-4 (= WP0 OW0-17). No claim changes.
*Status:* (a) DERIVED given U_qp and (G5′), with the error term [8.1′]; (d) DERIVED given U_qp. The size 𝔥_off ~ √(ΓW_c/2π) is [E]. The existence of U_qp with a controlled error beyond perturbation theory (no gap, hence no space-adiabatic
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
- RG1. Magnitude of the GRPA vertex correction in the DM region (formula [4.1]). The bound O((Δ_BCS/v_Fq)²) ≤ 0.04 for Al is 2609.06423's
  (credited, §4.2). Neither work computes the vertex.
- RG2. Amorphous films (WSi): an ab initio ε(q,ω) of the disordered film beyond the relaxation time, and Δ_BCS inhomogeneity (candidate route:
  MD-quenched ≥ 500-atom supercells + Kubo–Greenwood/RPA, with Bogoliubov–de Gennes on top). In v3 the RTA–Mermin model is outside validity for
  WSi at DM momenta (K31), so RG2 is the only route to a WSi correction.
- RG3. Two-magnon final-state interactions at O(1/|𝐒|²), and bound states in anisotropic magnets.
- RG4. Finite-q optical activity γ_OA(q,ω) beyond linear order (DFPT gyrotropy is O(q)); finite-q b^{NR}_{αβγ} for [3.2′].
- RG5. Finite-q multiplet transition densities for colour centres in embedding codes.
- RG6. Dirac targets at α̃ ≳ 1 (beyond one-loop RPA); the BSE/Sommerfeld rung is not computed.
- RG7. Phonon interface transmission t_esc in the QP cascade (phenomenological).
- RG8. Non-dipole orbital magnetic form factors for SOC ions (λ_{L,j} ≠ 0).
- RG9 (new). [4.2′] beyond the quasiclassical sketch: the O(Δ_BCS²/q²v_F²) remainder, near-edge q ~ ω/v_max, and the log at ω = 2Δ_BCS. A
  rate-level table of 𝔰_BCS-corrected L^{BCS} for Al is a specification: one KK quadrature per (q, ω) on the [4.2] grid.
- RG10 (new). Re-plot the 1708.08929 / 1910.02091 scattering and absorption reaches with the ε_bg² and ε_bg factors (§5.3, §5.5) and the
  0.55–0.62 charge renormalisation. Owner: LIMITS / coordinator; not done in this package.
- OW4-1. Theorem D-g beyond conjecture (§8): the existence of U_qp with error bounds, (G5′) with 𝔥_off(ψ_b) computed (and a proof of the O(Γ/Δω_bin) bin condition (c)), and the Dirac bin condition at
  α̃ ~ 1.
- OW4-2. **CLOSED**: the R7 FT check confirmed §5.3 (R×2).
- OW4-3. **CLOSED:** the 𝔤_I closed form [4.2] is in Allen, PRB 3, 305 (1971) (not new).
- OW4-4 (R9; AUDIT-2 m9 = WP0 OW0-17). A gapless-target / doublet replacement of Theorem D for magnetic insulators (magnon targets). D-g's (G1)
  covers fermionic quasiparticles only.

---
## 11. Rebuttals (to be returned to the referee concerned)
v3 accepts every FALLS and every STANDS WITH CORRECTION verdict. The items below are points where a referee statement is, in our derivation,
incomplete or wrong. Each comes with a derivation.
- **R-1 → REF-A (§2.3, V19), partial.** REF-A says Q₊ < 1 fails "for q ≳ 2k_F(1 − v_max/v_F) ≈ 4.3 keV in Al (m_χ ≳ 3 MeV)". The momentum
  is right (4.24 keV, K28). The mass is not the threshold. Q₊ < 1 ⇔ ω < qv_F − q²/2m_e (K28 identity). With ω ≤ qv_max this is guaranteed iff
  q < 2k_F(1 − v_max/v_F), and q_max = 2m_χv_max reaches 4.24 keV at **m_χ = 0.80 MeV**. REF-A's 3 MeV corresponds to q ≈ 2m_χv at a typical
  v ≈ 7×10⁻⁴ (≈ 210 km/s). So the hypothesis fails *somewhere* in the kinematics for m_χ > 0.80 MeV, and for most of the halo above
  ~3 MeV. §4.3 states both.
- **R-2 → REF-A (§2.3) and REF-B (V5, B2).** REF-A asks that "Re ε^{BCS} = Re ε^{nor}[1 + O(Δ²/v_F²q²)]" be tagged [D, sketch] or cited to
  2609.06423. REF-B uses it as the content of 2609.06423's |ε|² agreement. A sketch derivation ([4.2′], K32) shows that **the statement is
  false as an order estimate.** KK of δIm ε = Im ε^{nor}(𝔤_IΘ − 1) gives a *first-order* term (Δ_BCS/qv_F)𝔰_BCS(ω/Δ_BCS). It vanishes only at
  ω → 0, by the sum rule ∫₀^∞(𝔤_IΘ(y−2) − 1)dy = 0 (K32, to 10⁻¹⁴). So v3 neither tags nor cites the v2 statement: it replaces it with [4.2′].
  2609.06423's numerical agreement for ω ≳ 5Δ is compatible with this, since 2(v_max/v_F)𝔰_BCS(5)/5 = 0.16 holds only at the kinematic edge (8–16% with the KK-cutoff spread, K34).
- **R-3 → REF-B (V9).** REF-B keeps a defect in 2609.06423 Eqs. (7)–(8): "the time-ordered Π is used as the retarded ε". For ω > 0 at T = 0
  the second-pole term 1/(ω + E + E′ ∓ i0⁺) has no pole, so Π^T(ω) ≡ Π^R(ω), real and imaginary parts alike, and ε_BCS built from it *is* the
  retarded ε there (K25). The two differ only by 2πiδ(ω + E + E′), at ω < 0. The paper uses ω > 0 and T = 0 only and says so. So there is no
  defect in the paper's use; the caveat is a usage remark (§4.3). Settled for REF-A in §11A-2.
- **R-4 → REF-B (§A1).** REF-B writes that "the package's reading of the 'κ² growth' of (3.14) is also right". As an *explanation of the
  discrepancy* it is not: the Λ′_D rewrite holds identically in the correct theory, and the explicit ε_bg² is the omitted 1/ε_bg² (K23).
  REF-B's large-ε_bg asymptotics are right and compatible with this. Settled in §11A-1.

## 11A. Referee disagreements, settled by derivation
1. **The explanation of the ε_bg² prefactor of 1708.08929 Eq. (3.14).** REF-A: v2's sentence ("absorbing the '1' into Λ′") is wrong as an
   explanation. REF-B: the reading is right. **REF-A is right.** Derivation (§5.3, K23): Re ε_r = 1 + (α̃/6π)𝓁 = (α̃/6π)ln((2v_FΛ′_D)²/|𝓈|) with
   Λ′_D = Λ_De^{3π/α̃}. This is an identity, so it holds in both theories. Then 1/|ε_r|² = (6π/α̃)²/|𝓛′_D|² ∝ ε_bg², while
   1/|ε|² = (6π/(α̃ε_bg))²/|𝓛′_D|² has no explicit ε_bg, since α̃ε_bg = αg_deg/v_F. The ratio is ε_bg² with the *same* Λ′_D, so the explicit
   prefactor is the omitted 1/ε_bg², not a by-product of the rewrite. REF-B's asymptotics (Rate_src → const, Rate_URF ∝ ε_bg⁻²) follow from
   𝓛′_D ≈ 6π/α̃ and agree.
2. **2609.06423 Eqs. (4), (7)–(8): defect or not.** REF-A: the time-ordered fact is CONFIRMED and the defect REFUTED (Eqs. (4) and (7)). REF-B:
   Eq. (4) is legitimate, but (7)–(8) are a defect because the time-ordered Π is used as the retarded ε. **REF-A is right** for the paper as
   written. Derivation: at T = 0 and ω > 0, Π^T − Π^R = Σ|M|²[1/(ω + Ω + i0) − 1/(ω + Ω − i0)] = −2πiΣ|M|²δ(ω + Ω) = 0, since Ω = E + E′ > 0 (K25).
   The full complex Π, and hence ε_BCS and Im ε/|ε|², coincide. REF-B's warning (ω < 0, KK, T > 0) is kept as a usage remark.
3. **Mermin [4.4]: STANDS (REF-A) or STANDS WITH CORRECTION (REF-B).** **REF-B is right on the validity domain; REF-A is right on the algebra.**
   Derivation (K11, rebuilt from [4.3]): the ballistic limit uses the small-q Lindhard bracket 𝔣_Lin = 1 + iπz_rel/(2qv_F) + …, valid for q ≪ k_F,
   and the L formula needs k_TF ≫ q. So [4.4] holds for q ≪ k_F, k_TF and is asymptotic: at qℓ_mfp = 1.5, πqℓ_mfp/6 = 0.79. REF-B's further
   point, that the v2 K11 ratio test was tautological, is right; K11 now derives both limits from [4.3].
4. **Re ε^{BCS} order (implicit).** REF-A: asserted; tag or cite. REF-B: uses it as stated. **Neither stands as is**: by [4.2′] the correction is
   first order with a vanishing static coefficient (R-2).
Not disagreements (same content, different verdict labels, all applied): η_pb 4Δ_BCS (A-V8 "with correction", B-V16 "minor sharpening"); the
anisotropy items (A-V3 "stands, state the direction"; B-V3 "typo also in (3.13)"); and 0.13 eV (A-V19, B-V6).

---
## 12. Interface flags
| # | Owner | Quantity | Recorded form | Change in v3 / action |
|---|---|---|---|---|
| I1 (F5) | WP4 → WP0 | gapless sectors | WP0-v2 §6.2 scope; "[C], owned by WP4" | **Changed (R9):** Theorem D-g (a) is [D given U_qp and (G5′)]: the state-restricted bound [8.1′], \|C^{cross}\| ≤ c_g𝔥_off(ψ_b)‖O_a\|i⟩‖‖O_b\|i⟩‖/Δω_bin², with 𝔥_off ~ √(ΓW_c/2π) [E] (not ~Γ). The bin condition (c) stays [C]. §8 (e) remainder O(κ_BO^{2(n+1)}). Magnetic insulators not covered (OW4-4 = OW0-17). WP0 must cite §8 with (G5′) |
| I2 | WP5 | QP efficiency | WP5 (W13) η_pb = Δ_BCS⟨N_qp⟩/ω | Formula unchanged. **Sharpened:** N_qp = 2, η_pb = 2Δ_BCS/ω for ω < 4Δ_BCS (was 3Δ_BCS) (K27) |
| I3 | WP2 | one-phonon amplitude phase | e^{iq·r_κ} | CLOSED (unchanged) |
| I4 | WP6 | halo functional for P,T-broken targets | odd ℓ kept (WP6-v2) | **Changed order:** for the density channel the odd part of S is O(q³) [3.2′] (relative O(q)). The lowest odd harmonic is set by G_eff: ℓ = 1 only for polar groups; cubic 3 (T, T_d), 9 (O) (WP6-v3 C28, IF6-12, adopted in R9). No change to the WP6 structure; any WP6 magnitude estimate built on a q-linear density odd part must use [3.2′] |
| I5 | WP1, WP0 | external weight for defects | WP0-v2 (7.2), CC-1 | unchanged |
| I6 | NOTATION | 𝓃_D | applied (v4) | unchanged |
| I7 | NOTATION | WP4 symbols | §15 | new v3 rows in §15 (flag I17) |
| I8 | LIMITS L16, coordinator, CONVENTIONS §9 "Why" line, SOTA | ε_bg² against 1708.08929 / 1910.02091 | v2: conditional | **Changed: firm (REFEREED R×2).** Rate_src/Rate_URF = ε_bg² exactly (any δε_D); ×1600 / ×640 (isotropised model); ε_bg,ii² along principal axes for 1910.02091. Suggested LIMITS wording in §5.3. The v2 explanation sentence is replaced |
| I9 | WP0 | rate contraction order | WP0-v2 (3.3); REF-WP0-A asks for tr[𝔇ᵀS] | [3.3] uses Σ_ab𝔇_abS_ab = tr[𝔇ᵀS] with 𝔇_ab = ⟨𝒱_a*𝒱_b⟩ and S_ab = ⟨O_a†…O_b⟩ (K12). This is consistent with REF-WP0-A's fix. If WP0-v3 instead pairs 𝔇_ab with S_ba, the sign of [3.3] (and of γ_OA as defined) flips |
| I10 | WP0 (L9b), WP3 (absorption), LIMITS | dark-photon absorption in Dirac targets | WP0-v2 L9b: Γ = κ_mix²m Im(−1/ε), total ε | **New:** 1708.08929 Eqs. (4.4)–(4.5) and 1910.02091 Eqs. (2.25)–(2.27) are ε_bg (ε_bg,ii) too large [5.5]. The WP0-v2 L9b formula is the correct one (K24); the LIMITS L9b row should record the source defect |
| I11 | WP0 (4.3), L19 | nonreciprocal S_ee | WP0-v2 (4.3) | Density-channel odd part O(q³) [3.2′], the same as REF-WP0-B's (4.3) correction; q-linear only for the j, s rows |
| I12 | WP5, WP6 | L^{BCS} (Al, WSi) | v2: L^{BCS} = 𝔤_I L^{nor}[1 + O(Δ²/v_F²q²)] | **Changed:** [4.2′] adds a first-order screening term −2(Δ_BCS/qv_F)𝔰_BCS(y)𝔤_IL^{nor}. It **lowers** L. At the Al kinematic edge it is 8–16% at y = 5 [E] and ≲ 4% at y = 10. The expansion **fails for y ≲ 3.5 near the edge** (\|δL/L\| ≈ 1.42/0.88/0.53 at y = 2.2/2.5/3), so the threshold region is uncontrolled there (RG9). Nuisances must be one-sided (downward) and must exclude or separately treat y ≲ 3.5 near the edge. The P(E₁\|ω) shape [4.6] is unchanged. The total SC rate and any WP6 SC nuisance must allow for it. WP0-v2 Table 6.1's parameter Δ_BCS/v_Fq ≤ 0.2 is now a first-order control parameter |
| I13 | catalog G9, LIMITS, WP6 | WSi film ε | v2: "QROCODILE Drude, ×1–10 conservative" | **Withdrawn.** WSi at q = 1–5 keV is outside the RTA–Mermin validity (K31); no WSi factor is quoted (RG2) |
| I14 | anyone quoting the L16 rate factor | charge renormalisation | v2: 0.62 | **Changed:** 0.55–0.62 (cutoff-scheme spread, K17) |
| I15 | WP5 (R5) | Al q_min | v2 text "0.13 keV" | 0.13 eV (typo; qξ_coh ≥ 1.6 unchanged) |
| I16 | WP0 Table 6.1 / WP4 [4.2] | DM-region hypothesis Q₊ < 1 | v2: "all DM kinematics" | **Changed:** guaranteed only for q < 4.24 keV, i.e. m_χ ≲ 0.80 MeV (K28) |
| I17 | NOTATION | new v3 symbols | — | rows requested in §15 (b^{NR}_{αβγ}, 𝔰_BCS, 𝔣_Lin, z_rel, 𝔥_off, H_d, H_off, f_Δ, g_bin, Δω_bin, c_g, C^{cross}_ab, S^{bin}_ab, Λ′_D, 𝓁, 𝓛′_D, Π^{med}_γ, κ_mix,eff, Γ_abs,src, Rate_src, Rate_URF; R9: W_c, ψ_b, 𝔥_off(ψ_b)). For the NOTATION v5 pass (AUDIT-2 m31); b^{NR} ≡ ω²𝐁^{NR} one row (m17) |
| F11 | all | static DFPT error | X2: O(ω_Q²/E_g²) | not used in WP4; no action |
Consistency notes (no mismatch): the L13/L15/L16/L19 pointers in WP0-v2 (9.7) match §2.1, §4.2, §5.2 and §3. The spin screening in §2.1(f)
and §1.2 matches WP0-v2 (5.3). [3.1] uses the campaign sign of q (CONVENTIONS §3). σ̄_e is in vacuum (CONVENTIONS §9), which is what makes I8
decisive. The WP0-v2 L9b absorption formula agrees with [5.4].

---
## 13. Closing table: one row per R7 referee item
Actions: **applied** (correction or upgrade made; for STANDS items, the verification is recorded and nothing changes); **rebutted** (a
derivation is returned to the referee, §11); **dropped** (claim removed). Where a row has two parts, both are listed.
| Item | Verdict | Action | Where |
|---|---|---|---|
| A-V1 | OW4-2 STANDS, now unconditional; one sentence wrong | applied | header, §0, §5.3 (firm claim, K22); sentence replaced (K23); OW4-2 closed; I8 |
| A-V1′ | referee finding: absorption off by ε_bg | applied | §5.5 [5.4]–[5.5], K24; I10 |
| A-V2 | L16 chain, K5 STANDS | applied (no change) | §5.2 (verification noted) |
| A-V3 | anisotropy STANDS; state which direction is larger | applied | §5.2: q ∥ y larger; 366 / 221 (K21) |
| A-V4 | charge renormalisation, scheme | applied | §5.4 (i): 0.35/0.55 vs 0.27/0.62 (K17); I14 |
| A-V5 | GRPA K2 STANDS; credit 2609.06423 Π_θ; drop novelty | applied | §4.2 step 3 (credit, "not a source error"); §14 novelty sentence removed; RG1 |
| A-V6 | 𝔤_I closed form STANDS; novelty unverified | applied (novelty dropped, Allen 1971 credited) | §4.3; OW4-3 closed |
| A-V7 | "𝔤_I = analytic form of 2609.06423's 5Δ agreement" FALLS | dropped | §4.3 sentence replaced ("Reading of 𝔤_I"); §0 |
| A-V8 | η_pb: N_qp = 2 to 4Δ_BCS | applied | §4.6, K27, K15 note; I2 |
| A-V9 | 2101.08263 Eq. (3) CONFIRMED | applied (kept, FT-R7×2) | §4.3 (a), §14 |
| A-V10 | 1512.04533 e₋ CONFIRMED | applied (kept, FT-R7×2) | §4.3 (b), §14 |
| A-V11 | 2609.06423 time-ordered: fact CONFIRMED, defect REFUTED | dropped (defect) / applied (remark) | §4.3 remark, §0; K25; §11A-2 |
| A-V12 | "causality" → reality (both the source's and WP4's) | applied | §4.3 (c) |
| A-V13 | Mermin [4.4] STANDS | applied | §4.5 (derivation added, K11 rebuilt); validity restricted per B (§11A-3) |
| A-V14 | QROCODILE "conservative" FALLS | dropped | §4.5 bullet replaced; §0; I13; K31 |
| A-V15 | reciprocity STANDS; "iff" only necessary | applied | §3.1, §0 |
| A-V16 | chiral rule STANDS; state the γ_OA sign convention | applied | §3.2 sign convention; I9 |
| A-V17 | D-g (a) needs (G5) / commutation | applied (restated in R9, §16) | §8 (G5′), [8.1′], K30, K33; I1 |
| A-V17 (sub) | phase/Higgs to (0,0) is a convention | applied | §8 (b) |
| A-V18 | 2009.13534 Eq. (36) CONFIRMED (notational) | applied (kept) | §2.1 |
| A-V19 | 0.13 keV → eV; Q₊ < 1 fails for q ≳ 4 keV | applied / rebutted (mass threshold, R-1) | §4.3 validity; K16, K28; I15, I16 |
| A-V20 | exothermic example outside validity | applied | §7 example (1 MeV, 50 eV), K29 |
| A-V21 | spectral budget STANDS | applied (no change) | §1.3 |
| A-V22 | kinematics STANDS | applied (no change) | §6 (K18) |
| A-V23 | contested corrections: none | n/a | — |
| A §2.3 (Re ε) | Re ε^{BCS} statement asserted | rebutted (R-2) and replaced by a derivation | §4.3 [4.2′], K32; I12 |
| B-V1 | OW4-2 CONFIRMED; upgrade; absorption factor ε_bg | applied | §5.3, §5.5, K22, K24; I8, I10 |
| B-V1 (sub, §A1) | "the κ²-growth reading is also right" | rebutted (R-4) | §11A-1, K23 |
| B-V2 | 2101.08263 Eq. (4) recovered STANDS | applied (no change) | §5.2 |
| B-V3 | typo also in Eq. (3.13) | applied | §5.1, §5.2 |
| B-V4 | L15 chain / K2 STANDS | applied (no change) | §4.2 |
| B-V5 | 𝔤_I math right; 2609.06423 reading wrong | dropped (reading) / applied | §4.3 "Reading of 𝔤_I"; the O(Δ²) part rebutted (R-2) |
| B-V6 | 0.13 keV → 0.13 eV | applied | §4.3, K16 |
| B-V7 | 2101.08263 Eq. (3) CONFIRMED | applied (kept) | §4.3 (a) |
| B-V8 | 1512.04533 e₋ CONFIRMED | applied (kept) | §4.3 (b) |
| B-V9 | Eq. (4) not a defect; (7)–(8) defect as retarded ε | applied (Eq. (4)) / rebutted ((7)–(8), R-3) | §4.3 remark; K25; §11A-2 |
| B-V10 | reality, not causality | applied | §4.3 (c) |
| B-V11 | acausal-branch mechanism asserted; it *suppresses* | applied (mechanism dropped) | §4.4 |
| B-V12 | Mermin algebra with correction; QROCODILE REFUTED; q ≪ k_F, k_TF; K11 tautological; redo WSi | applied / dropped (QROCODILE, WSi numbers) | §4.5, K11 rebuilt, K31; §11A-3; I13 |
| B-V13 | reciprocity STANDS | applied (no change) | §3.1 |
| B-V14 | density odd part O(q³) | applied | §3.1 [3.2′], K26; I4, I11 |
| B-V15 | chiral rule STANDS | applied (no change) | §3.2, K12 |
| B-V16 | N_qp = 2 to 4Δ_BCS | applied | §4.6, K27 |
| B-V17 | D-g (a) cross-term error | applied (restated in R9, §16) | §8 [8.1′], K30, K33 |
| B-V18 | L13 chain STANDS | applied (no change) | §2.1 |
| B-V19 | gap closures STAND | applied (no change) | §2.2–§2.3, §6, §7 |
| B-V20 | credit 2609.06423 for Δ²/(v_FQ)² ≤ 1/25 | applied | §4.2 step 3; RG1 |
**Counts** (47 rows; a two-part row is counted under each action it carries): **applied 43** (of which 14 are STANDS/CONFIRMED rows recorded
without change), **rebutted 5** (R-1 A-V19 mass; R-2 A §2.3 and B-V5 order; R-3 B-V9; R-4 B-V1 sub), **dropped 6** (A-V7, A-V11 defect, A-V14, B-V5
reading, B-V11 mechanism, B-V12 QROCODILE/WSi), n/a 1 (A-V23). Self-found in v3: [4.2′] (first-order screening term, prompted by A §2.3) and
the Q₊ mass threshold (R-1).
*v2 corrections retained.* The 44 rows of returns/R6/WP4-v2.md §13 (CORRECTIONS §10 items, the §0 and §17 renames, the F5/F11 flags, and
eight v1 errors) remain applied in this text. The v3 changes do not reopen any of them.

---
## 14. Literature (status after R7)
Kept only if CONFIRMED against the full text by an R7 referee; REFUTED claims are dropped; others are marked UNRESOLVED.
| Claim about a published paper | Status | Where |
|---|---|---|
| 1708.08929: ε_r = ε_tot/κ (Eq. (A.8)), F_med = 1/ε_r with vacuum σ̄_e (Eqs. (3.7), (3.11)), plotted limits (3.13)–(3.14), Fig. 4 → rate ×κ² | CONFIRMED (A, B) | §5.3 |
| 1910.02091: Π with 1/κ (Eq. (3.3)), vacuum D₀ (2.6), F_med (2.7), (3.14) → rate ×κ² | CONFIRMED (A, B) | §5.3 |
| 1708.08929 / 1910.02091: cutoff charge e/√κ against vacuum vertex e (internal inconsistency) | CONFIRMED (A, B) | §5.3 |
| 1708.08929 Eqs. (4.4)–(4.5), 1910.02091 Eqs. (2.25)–(2.27): absorption with Dirac-only Π (factor κ is derived) | equations CONFIRMED (A, B); factor D | §5.5 |
| 1708.08929 Fig. 5 "optimal κ/g ~ O(10)" inherits the absorption factor | CONFIRMED (A) | §5.5 |
| 1910.02091 typo q_x²v_{F,z}² in Eqs. (3.13) and (3.14) | CONFIRMED (A, B) | §5.1–§5.2 |
| ZrTe₅ clamped-ion κ = (187.5, 9.8, 90.9), harmonic mean 25.3 (1708.08929) | CONFIRMED (B) | §5.2 |
| 2101.08263 Eq. (4), (S.21)–(S.22): W = Im ε_Dirac/κ² (URF form) | CONFIRMED (A, B) | §5.2–§5.3 |
| 2101.08263 Eq. (3): λ_TF²/(2q²) should be λ_TF²/q² | CONFIRMED (A, B) | §4.3 (a) |
| 2101.08263 SM: "Causality also implies W(q,−ω) = −W(q,ω)" (attribution wrong) | CONFIRMED that they say it (A, B) | §4.3 (c) |
| 2101.08263 SM: acausal choice suppresses the rate by up to 10⁷ | CONFIRMED (B) | §4.4 |
| 1512.04533 Eq. (13) [(3.3)]: e₋ lacks a factor 4 | CONFIRMED (A, B) | §4.3 (b) |
| 1512.04533 (3.2): exact factorisation (1 − e^{−βω})^{-1} × proper part | CONFIRMED (B) | §4.2 step 5 |
| 2609.06423 Eqs. (6)–(9) as quoted; Eq. (9) prefactor = WP0-v2 (3.3) | CONFIRMED (A; B for (7)–(9)) | §4.1, §4.3 (d) |
| 2609.06423 bare bubble not conserving; Π_θ with Δ²/(v_FQ)² ≤ 1/25 already in the source | CONFIRMED (A, B) | §4.2 |
| 2609.06423 Eqs. (4), (7): time-ordered (fact) | CONFIRMED (A, B) | §4.3 remark |
| ~~2609.06423 Eqs. (4)/(7) are a source defect~~ | REFUTED (A; B for Eq. (4)); dropped (§11A-2) | — |
| ~~𝔤_I is the analytic form of 2609.06423's "agreement for ω ≳ 5Δ"~~ | REFUTED (A, B); dropped | — |
| ~~2412.16279 (QROCODILE) uses a Drude ε for its limit; Drude is conservative~~ | REFUTED (A, B); dropped | — |
| 2412.16279: bulk rate uses Lindhard with ω + iΓ, Γ = 0.1E_F; Drude only for thin-layer anisotropy | CONFIRMED (A, B) | §4.5 |
| 2009.13534 Eq. (36): S′^x, S′^y are S′^± (notational); Eq. (38) as quoted | CONFIRMED (A) | §2.1 |
| 1905.13744 Eqs. (5), (6); n_s via App. (A.10)–(A.13) (Eq. (12)) | CONFIRMED (B) | §2.1 |
| 1905.13744 Eqs. (9)–(10); breakdown "beyond 10 MeV" | UNRESOLVED | §2.1 |
| 2009.13534 Eq. (34); §II.3 suppression q²/(M_κω) | UNRESOLVED | §2.1, §2.3 |
| 2101.08263 Eq. (1), (S.30); the remark that a damped complex G_LF violates positivity | UNRESOLVED | §4.1, §4.3 |
| 1512.04533 Eq. (11) | UNRESOLVED | §4.1 |
| ~~Novelty of the 𝔤_I closed form [4.2]~~ | dropped: in P. B. Allen, PRB 3, 305 (1971) (cited by 1604.06800); coordinator erratum | §4.3 |
| Title-only [ABS] items: 2212.04504, 1901.07569, 2210.13516, 2301.07617, 2511.20461, 1004.0937, 1504.07237, 2005.10256, 2501.18120, 2308.06314, 1604.06800, 2210.06490 (no content claim beyond existence/topic) | UNRESOLVED | §3.2 (chiral phonons) |
The v2 sentence "No DM calculation of … a conserving BCS dielectric function was found" is **removed** (A-V5): 2609.06423 identifies the
conserving correction Π_θ and bounds it. The other "not found by v1's searches" statements (two-magnon continua, exothermic DM into
collective modes, NV final states) are search results, not literature claims, and are UNRESOLVED as novelty statements.

---
## 15. Symbols introduced/used
All symbols follow NOTATION v4 and CONVENTIONS; **no deviations**. Source formulas (§2.1, §4.1, §5.1) keep their own notation, as NOTATION
§K allows (κ, Λ, Λ′, g, g_D, ε (mixing), Δ, W, λ_TF, S_j, U, V, n_s, ε_r, Π_QP, Π_θ, Γ_p, f_j, s_f, s_i, ε_eff, ε_med, m_{A′}).
*Used as defined in NOTATION/CONVENTIONS:* all v2 symbols (returns/R6/WP4-v2.md §15, unchanged), plus κ_mix (dark-photon mixing),
y_χ (DM-side coupling, source g_D), m_φ and φ (absorbed boson), Γ_abs (WP0 (3.5)), α̃, 𝓈, δε_D, R̃_D, ε_r, ε_bg.
*Introduced in v3 (new objects; NOTATION v4 §M rows requested, flag I17):*
| Symbol | Meaning | Where |
|---|---|---|
| b^{NR}_{αβγ}(ω) | odd (q-linear) part of the current response, S_{j^αj^β}(q) − S_{j^αj^β}(−q) = 2b^{NR}_{αβγ}q^γ; enters the density odd part at O(q³). Same object as WP0-v3's 𝐁^{NR}_{αβγ} ≡ b^{NR}_{αβγ}/ω² (one NOTATION row, AUDIT-2 m17) | [3.2′] |
| 𝔰_BCS(y) | BCS screening function, P∫₀^∞dy′y′²[𝔤_IΘ(y′−2) − 1]/(y′² − y²); 𝔰_BCS(0) = 0 | [4.2′] |
| 𝔣_Lin(z_rel), z_rel | small-q Lindhard bracket (ε_Lin(q,z) − 1)/(ε_Lin(q,0) − 1); complex frequency ω + iγ_rel | §4.5 |
| H_d, H_off, 𝔥_off(ψ_b) | sector-diagonal part of H, off-diagonal remainder, state-restricted bound sup_s‖H_off e^{−iH_ds}ψ_b‖/‖ψ_b‖ (hypothesis (G5′)) | §8 |
| f_Δ, g_bin, ĝ_bin, Δω_bin, c_g | bin function g_bin(x/Δω_bin)/Δω_bin, its shape and Fourier transform, bin width, (1/2π)∫\|s\|\|ĝ_bin\| | [8.1′] |
| S^{bin}_ab, C^{cross}_ab | binned spectrum; cross-sector remainder | [8.1′] |
| W_c, ψ_b | final-state continuum width in the 𝔥_off estimate; probed state O_b\|i⟩ | §8 |
| Λ′_D, 𝓁, 𝓛′_D | Dirac cutoff with the "1" absorbed (Λ_De^{3π/α̃}); ln((2v_FΛ_D)²/\|𝓈\|); complex log with Λ′_D | §5.3 |
| Π^{med}_γ, κ_mix,eff | in-medium photon self-energy (all charges; renamed from Π_γ, which collided with Π^γ, AUDIT-2 m28; NOTATION row exists); in-medium effective mixing | [5.4] |
| Rate_src, Rate_URF, Γ_abs,src | source-convention and URF rates (ratios only) | [5.3], [5.5] |
In the text and checks, f_Δ is written with shape g_bin (not the bare g, which would collide with g_deg) and the leak bound is 𝔥_off (distinct
from the hybrid index h of §2.3). Labels: WP4v3-K1…K34 (checks); I1–I17 (flags); R-1…R-4 (rebuttals); OW4-1, OW4-4 (open items; OW4-3 closed); RG1–RG10;
WP4-D1…D6 keep their v1 meaning. Equation labels new in v3: [3.2′], [4.2′], [5.3]–[5.5], [8.1′] (R9; v3 [8.1] superseded).

---
## 16. R9 clean-up closing table (edited in place; VER-WP4-A/B new items and AUDIT-2 rows addressed to WP4)
VER-A and VER-B mark all R7 items RESOLVED and accept every rebuttal (R-1…R-4). The rows below are the new items only.
| Item | Content | Action | Where |
|---|---|---|---|
| VER-A N1 = VER-B N2 | (G5) as an operator norm is extensive (vacuous in bulk); 𝔥_off ~ Γ is wrong (√(ΓW_c)); "(G5) = bin condition" false | applied | §8: (G5′) state-restricted, [8.1′] with state-restricted Duhamel proof; 𝔥_off ~ √(ΓW_c/2π) [E]; sentence dropped; (c) stays [C]; [8.1′] "sufficient but loose"; K33; §0, I1, OW4-1 |
| VER-A N2 | [4.2′] y = 5 number has a KK-cutoff uncertainty (Y ≈ 13) | applied | §4.3 [4.2′] validity: 8–16% [E] at y = 5 (cut 7%, KK to ∞ 16%); K34; §0, I12, R-2 |
| VER-A N3 | state the sign of the screening term | applied | §4.3 "Sign": 𝔰_BCS > 0, L lowered; §0; I12 |
| VER-B N1 | [4.2′] is O(1) near threshold at the edge (1.42/0.88/0.53 at y = 2.2/2.5/3) | applied | §4.3 validity domain 2(Δ/qv_F)𝔰_BCS ≪ 1, table, "fails for y ≲ 3.5 at the edge", region uncontrolled → RG9; §0; I12 (one-sided nuisance, exclude y ≲ 3.5) |
| VER-B N3 | ×640 is the source's isotropised model | applied | §0, §5.3, I8 |
| AUDIT-2 m8 | §8 (e) remainder O(κ_BO^{n+1}) → O(κ_BO^{2(n+1)}) | applied | §8 (e); I1 |
| AUDIT-2 m9 | D-g does not cover magnetic insulators (WP0 G9) | applied (open item, no claim change) | §8 "Scope"; OW4-4 (= OW0-17); §0 |
| AUDIT-2 m13 | (1.2) spin-screening wording (WP1 IF-13: triplet W^{scr} ladder, R̃_s ≡ 4R_{s^zs^z}) | applied | §1.2; §6 [6.1] text |
| AUDIT-2 m16 | "ℓ = 1 still the leading odd harmonic" → set by G_eff: ℓ = 1 only for polar groups; cubic 3 (T, T_d), 9 (O) | applied (WP6-v3 C28 adopted) | §3.1 after [3.2′]; I4 |
| AUDIT-2 m17 | b^{NR} (WP4) vs 𝐁^{NR} (WP0): one object | applied | §3.1 note 𝐁^{NR} ≡ b^{NR}/ω²; §15; I17 |
| AUDIT-2 m28 | Π_γ collides with Π^γ | applied | renamed Π^{med}_γ (existing NOTATION row): §5.5 [5.4], §15, I17 |
| AUDIT-2 m31 | WP4 I17 symbols not yet in NOTATION | noted (coordinator, NOTATION v5) | I17 (list extended with W_c, ψ_b) |
| AUDIT-2 m7, m10, m22; L9b, L13, L15, L16 rows; I1–I17 cross-check | WP0 / LIMITS / NOTATION actions citing WP4 | no WP4 change; WP4 content consistent (I1, I8, I10, I12, I16 restated above) | §12 |
| Coordinator erratum (WP7-B1 referees) | 𝔤_I case-I closed form and its difference from Mattis–Bardeen are in Allen, PRB 3, 305 (1971) | applied (novelty claim dropped, credit added) | §0 L15 row, §4.3, OW4-3 (closed), §13 A-V6, §14 |
**Counts:** 13 applied (including 1 noted for NOTATION), 0 rebutted, 0 dropped. Checks: K33 (state-restricted bound, √(ΓW_c) size,
extensivity of the operator norm) and K34 ([4.2′] validity table, KK cutoff, sign) were added. **36/36 PASS** (< 30 s).

