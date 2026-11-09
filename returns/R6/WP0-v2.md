# R6 / WP0-v2: architecture of the Unified Response Framework (URF), corrected standalone version

Revision agent, brief R6/REV-WP0. Supersedes returns/R4/WP0.md (v1), which stays as the historical record. Folds in O4 (Theorem D
(iv′)/(iv″)), X1 (soft acoustic limit, C7a–e) and X2 (pair-channel screening, M̃), and every owed correction in state/CORRECTIONS.md
§6 plus the WP0 defects reported in WP1–WP6, O4, X1, X2 (closing table, §13). Conventions: CONVENTIONS.md; symbols: NOTATION v4.
Checks: `code/WP0-v2/checks.py` (sympy only, exact arithmetic, 44 checks, all PASS, 13 s); cited as WP0v2-Cn.
Tags: **[D]** derived (hypotheses stated), **[D, sketch]**, **[E]** estimated, **[C]** conjectured; literature **[FT]** full text,
**[ABS]** abstract. "[FT via WPn]" = equation read in full text by return WPn. Labels from other returns carry their prefix (CONVENTIONS §14).
Status: CLAIMED (v1 content partly CROSS-CHECKED by X1, X2, WP1–WP6, O4; see SOTA), pending R×2.
Equation numbers: v2 keeps v1's number wherever the object survives; replaced objects keep the slot. Map in §0.

---
## 0. What changed, and the v1 → v2 equation map
| v1 | v2 | change |
|---|---|---|
| (1.2) hyperfine (2/3)σ·𝐈 | (1.2) | +(2/3)g_eμ_Bg_Iμ_N s·𝐈δ³ = +(1/3)…σ·𝐈δ³ (WP4-D1) |
| (1.2) δ_rel "from SOC", Ge sizes 0.27/0.05 | (1.2), (4.6′) | only mass-velocity: −(5/3)⟨T⟩/m_e; (Zα)² = 0.055 Ge 1s, ~10⁻³ Ge 3d (WP1-D2, D3) |
| (4.6), (5.3) [H,n] = q·j + (q²/2m)n | (4.6), (5.3) | [T_e, n_e(q)] = q·j_e(q) exactly (WP1-D1) |
| (4.9) soft limit [C], ℓ_Q with N inside | (4.9) | = X1 (X1), C7a–e; ℓ_Q N outside (WP3-1, CONVENTIONS §5) |
| (5.3) j_T, spins "unscreened" | (5.3) | j_T LFE-screened; spins (SOC = 0) f_xc^T-renormalised (WP1-D4, D5) |
| (5.5) three channels | (5.5) | four classes (X2 §3), topological proof |
| (5.6) D2-normalised projected form | (5.6) | X2 (2.3) with M̃, D1 normalisation |
| (5.7) M̃ (projected) | (5.7), (5.7′) | (5.7) = X2 (2.2); v1 form kept as truncation (5.7′) (WP3-2) |
| Table 6.1, τ | Table 6.1, §6.1 | x_coh retired, 2W_κ = q·B_κ·q, K labels, metadata, WP4-D4 rows |
| Theorem D (H2), (i), (ii), (iv), dictionary | §6.2 | scope; PSD only in window; m_A/δM_κ; O4 (iv′)/(iv″); S_eκ any c_ec_κ ≠ 0 |
| (7.1)–(7.2) | (7.1)–(7.2) | no plasmon label in RPA (WP5-3); out-state external weight derived (§7.2, §10) |
| (7.3) | (7.3) | WP5 (W6): q integral and 𝔇 trace inside the Λ sum (WP5-1, 2, 4) |
| (8.1)–(8.3) | (8.1)–(8.3) | WP6 M/A/E/Δ types; ∫_ℝωS = π𝓃_eq²/m_e; three reported objects (WP6-W1–W4) |
| (9.1) "isotropic f_χ" | (9.1) | hypothesis (I): angle-averaged S (WP6-W5) |
| (9.3) table | (9.7) table | L7d split, L12 deterministic, L15 GRPA, L16 ε_bg, L19 P,T-broken, L6 pointer; source quotes per entry |

---
## 1. Hamiltonian and degrees of freedom

**(1.1) [D]** Electrons i = 1..N_e (r_i, p_i, spin s_i = σ_i/2); nuclei I of species κ(I), charge Z_κ, mass M_κ, (R_I, P_I), nuclear spin
𝐈_I. Species s ∈ {e, κ}, density operators n_e(k) = Σ_i e^{ik·r_i}, n_κ(k) = Σ_{I∈κ} e^{ik·R_I}, charge numbers z_e = −1, z_κ = Z_κ, charge
density ρ_c(k) = e Σ_s z_s n_s(k), number densities 𝓃_s = N_s/V. With v_C(k) = e²/k²:

  H = Σ_i p_i²/2m_e + Σ_I P_I²/2M_κ(I) + (1/2V) Σ_{k≠0} v_C(k)[ρ_c(k)†ρ_c(k)/e² − Σ_s z_s²N_s] + H_rel + H_hf + H_ext ≡ H_C + H_rel + H_hf + H_ext.

H_C is the exact non-relativistic Coulomb Hamiltonian (point nuclei; finite size enters only through F^M_κ, F^Σ_κ of §2); k = 0 is removed
by neutrality. Every e–N and N–N interaction is Coulomb, so phonons, g and screening are derived objects (§5, §6).

**(1.2) Options** (switches; each later WP states which it uses).
- *Breit–Pauli [D].* H_rel = Σ_i[−p_i⁴/8m_e³ + (1/8m_e²)∇_i²V_pot + (1/4m_e²)σ_i·(∇_iV_pot × p_i)] + two-body SOO/SSO. Only the mass-velocity term
  changes the f-sum: Darwin is multiplicative and SOC is linear in p at fixed r, so both give an exactly zero double commutator (WP0v2-C4g,h;
  WP1 [E11]). The shift is (4.6′): δ_rel = −(5/3)⟨T⟩/m_e − q²/4m_e², i.e. −0.18% (Si), −0.58% (Ge) with all electrons [E, WP1].
- *Relativistic cores [D, WP1 §5].* With full Dirac bilinears ψ̄Γψ the factorisation of DM physics from target physics is exact (the
  operator set grows; WP1 O_Γ). The 16-row basis of §2 is the O(v_e¹) Foldy–Wouthuysen truncation; corrections are O(⟨v_e²⟩) ≈ (Zα)²:
  0.010 (Si 1s), **0.055 (Ge 1s), ~10⁻³ (Ge 3d)** [E] (WP0v2-C4i; v1's 0.27/0.05 were wrong). In 4-component codes without no-pair
  projection the double commutator vanishes; the NR f-sum is restored only by the negative-energy states, so Dirac cores must be projected.
  For halo DM the Ge 3d band dominates, and there the XC placement (4.5 eV) outweighs relativistic operator corrections (WP1 §5.4).
- *Hyperfine [D] (WP4-D1).* H_hf = Σ_{i,I} (+2/3) g_eμ_B g_Iμ_N s_i·𝐈_I δ³(r_i − R_I) = (+1/3) g_eμ_B g_Iμ_N σ_i·𝐈_I δ³(…) (Fermi contact,
  HL units, μ₀ = 1, from H = −𝛍_e·B_contact with 𝛍_e = −g_eμ_B s, B_contact = (2/3)g_Iμ_N𝐈δ³; g_I carries the sign of the nuclear moment;
  WP0v2-C8) + orbital, dipolar and quadrupole terms. It is the only coupling of 𝐈_I to the rest of the system.
- *External fields [D].* p_i → p_i + eA₀(r_i): paramagnetic current plus diamagnetic (e²/2m_e)A₀²; Zeeman g_eμ_B B₀·s_i. B₀ enters g_aγγ (2.9).
- *Broken-symmetry references [D].* Magnetic order and superconductivity do not change H; they change the reference state (WP4 (1.1)):
  (3.1)–(4.6) need only stationarity and hold unchanged, provided the response is computed in a **conserving** (Baym–Kadanoff)
  approximation; a bare bubble in a broken-symmetry basis violates (4.6) and (4.8) (WP4-K2). New small parameters (§6.1) are not finite
  orders of the e–ph expansion; the reference is metadata `ref` in τ (CONVENTIONS §11).

---
## 2. DM interaction basis

**(2.1) Kinematics [D].** The DM goes p → p − q, spin projection s → s′, optionally χ₁ → χ₂ with Δ_χ = m_{χ₂} − m_{χ₁} (exothermic if Δ_χ < 0):

  ω_q = q·v − q²/2m_χ − Δ_χ.                                                                                                    (2.1)

q is never folded; ω < 0 is allowed at T > 0. On shell v_min = (ω + Δ_χ)/q + q/2m_χ and v_∥ = (ω + Δ_χ)/q. Galilean relative velocity
(2009.13534 Eq. (13) [FT]): v^⊥ = v_χ − v_s, with v_χ ≡ v − q/2m_χ a DM-side c-number and v_s ≡ (k + k′)/2m_s a target-side operator.

**Target operator basis [D].** Every Fitzpatrick operator 𝒪_i is at most linear in 𝐒_s and in v_s (1203.3542; 2009.13534 Table III [FT]).
The complete basis per species is 16 operators O_a, a = (s, Γ), rows Γ ∈ {0, b, a, ab} (density, spin, current, spin-current); Cartesian
components are α, β:

| Γ | operator | electrons (Σ over i) | nuclei of species κ (Σ over I ∈ κ) |
|---|---|---|---|
| 0 | number density | n_e(q) = Σ e^{iq·r_i} | n_κ^F(q) = F^M_κ(q) Σ e^{iq·R_I} |
| b | spin density | s_e^β(q) = Σ e^{iq·r_i} s_i^β | I_κ^β(q) = F^Σ_κ(q) h^I_κ Σ e^{iq·R_I} 𝐈_I^β |
| a | paramagnetic current | j_e^α(q) = Σ ½{p_i^α/m_e, e^{iq·r_i}} | j_κ^α(q) = F^M_κ Σ ½{P_I^α/M_κ, e^{iq·R_I}} |
| ab | spin-current | J_e^{αβ}(q) = Σ ½{p_i^α/m_e, e^{iq·r_i}} s_i^β | J_κ^{αβ} = F^Σ_κ h^I_κ Σ ½{P_I^α/M_κ, e^{iq·R_I}} 𝐈_I^β |

h^I_κ is the nucleon-spin content per unit nuclear spin (WP2's spin coupling; 𝒥_κ is the nuclear spin quantum number). With x_α = R_I + y_α
and frozen internal nuclear states (ω ≪ keV), the internal factors collapse to F^M_κ(q) → f_pZ_κ + f_n(A_κ − Z_κ) at q → 0 (Helm) and F^Σ_κ;
composite internal responses (orbital 𝐋_s, 𝐋_s⊗𝐒_s, 2009.13534 Eq. (27)) are higher order in q·y and can be added as rows.

**Matching [D].** Write each 𝒪_i^{(s)} with v^⊥ = v_χ − v_s and map 1, 𝐒_s, v_s, 𝐒_s⊗v_s onto the rows. Examples: 𝒪₁ → n; 𝒪₄ = 𝐒_χ·𝐒_s →
𝐒_χ^β s^β; 𝒪₇ = 𝐒_s·v^⊥ → v_χ^β s^β − δ_{αβ}J^{αβ}; 𝒪₈ = 𝐒_χ·v^⊥ → 𝐒_χ·v_χ n − 𝐒_χ^α j^α; 𝒪₃ = i𝐒_s·(q/m_s × v^⊥) →
iε_{βγδ}(q^γ/m_s)(v_χ^δ s^β − J^{δβ}). The "a/b" split of 2009.13534 is this decomposition. Then

  ⟨p−q, s′|H_int|p, s⟩ = V^{-1} Σ_a 𝒱_a^{s′s}(q, v_χ) O_a(q),   𝒱_a = (4m_χm_s)^{-1} Σ_i c_i^{(s)} F_DM,i(q) A_i^a(q, v_χ, 𝐒_χ),          (2.2)

A_i^a read off from the expansion, F_DM,i the mediator factor. Anchor: 𝒱_{n_e} = c₁/(4m_χm_e), σ̄_e = μ_χe²|c₁|²/(16πm_χ²m_e²) (in vacuum,
at q₀ = αm_e), and **|𝒱_{n_e}|² = πσ̄_eF_DM²/μ_χe² = |Ṽ|²** (D1 N5, D2 §0). On shell, for local H and elastic DM, q·v^⊥ acts as zero, so only
the transverse projections P_Tv_χ and j_T, J_T survive in any rate (WP1 §2.2, [E4]; uses (4.6) continuity).

**DM tensor [D].** 𝔇_ab(q,v) ≡ (2j_χ+1)^{-1} Σ_{ss′} 𝒱_a^{s′s*}𝒱_b^{s′s}: Hermitian PSD (a sum of rank-one projectors). On shell
𝔇 = 𝔇^{(0)} + 𝔇^{(1)}·v_T + v_T·𝔇^{(2)}·v_T (WP6 (1.2)).                                                                        (2.3)

**Absorption couplings [D]** (DM boson φ, ω ≃ m_φ, |k_φ| ≃ m_φv ~ 10⁻³ω):
- *Dark photon:* κ_mix e A′_μJ^μ_em, J^μ_em = (ρ_c, J_c), J_c = eΣ_s z_s(j_s + diamagnetic).
- *ALP–electron:* 2106.12586 Eq. (18) [FT]. LO −(g_aee/2m_e)(∇φ)·σ → s_e(k), O(k)-suppressed; NLO ∝ (g_aee/4m_e²)(∂_tφ)ψ†σ·∇↔ψ → 2 tr J_e(k)
  = Σ½{σ_i·p_i/m_e, e^{ik·r_i}}: ALP absorption probes the trace of the spin-current row, equal to the current response only at SOC = 0 (L9b).
- *ALP–photon in B₀:* −g_aγγ φ E·B₀ is a source current ∥ B₀: a dark photon with κ_mix m_φ² → g_aγγB₀m_φ (2.9).
- *Scalar:* y_φ φψ̄ψ. LO operator n_e(k) (n_κ for nucleons), suppressed at k → 0 by charge conservation; NLO (1/8m_e²)ψ†∇↔²ψ (2106.12586
  Table I [FT]) = the kinetic-energy density 𝒯_e(k), an extra absorption row a = (e, 𝒯). WP3 adds a phonon-assisted 𝒯_e channel (L9b).

---
## 3. Master rate formulae

**(3.1) Response matrix [D].** With p_i = e^{−βE_i}/𝒵:

  S_ab(q,ω) = (2π/V) Σ_{i,f} p_i ⟨i|O_a(q)†|f⟩⟨f|O_b(q)|i⟩ δ(ω − E_f + E_i),     S ≡ S_ee.                                              (3.1)

  R_ab(q,ω) = −(i/V)∫₀^∞dt e^{iωt}⟨[O_a(q,t)†, O_b(q,0)]⟩ = (1/V)Σ_{if}(p_i − p_f)⟨i|O_a†|f⟩⟨f|O_b|i⟩/(ω − E_f + E_i + i0).                 (3.2)

**(3.2) Scattering [D].** Hypotheses: first Born in H_int; DM plane waves in V; Gibbs target; unpolarised DM. Per DM particle:

  Γ_χ(v) = ∫ d³q/(2π)³ Σ_ab 𝔇_ab(q,v) S_ab(q, ω_q),                                                                                (3.3)

  dℛ/dω = (ρ_χ/m_χρ_T) ∫d³v f_χ(v) ∫ d³q/(2π)³ tr[𝔇(q,v)S(q,ω)] δ(ω − ω_q)      (per unit target mass).                                (3.4)

Bookkeeping: 2πΣ_{p′}|V^{-1}Σ𝒱O|²δ = ∫d³q/(2π)³(2π/V)(…). For one density operator, (3.1) is D2's S, 𝔇 = |Ṽ|², and (3.3) is D1 eq. (3)
= D2 §0 = KKL 2101.08275 Eqs. (4), (6), (13) [FT via WP1] (KKL's n_{−k} has the opposite sign of q, immaterial unless P and T are both
broken, §4.3). At T > 0, (3.3) contains ω_q < 0 weighted by (4.3). 1509.01598 Eq. (17) is per target, 2311.04957 Eq. (3) per cell (WP6 (1.6)).

**(3.3) Absorption [D].** Quantise φ = Σ_k(2ωV)^{-1/2}(a^φ_k ε e^{ik·x} + h.c.), H_int = y_φ∫d³x φ(x)O(x):

  Γ_abs = (y_φ²/2ω) S_OO(k_φ, ω),   Γ_net = Γ_abs − Γ_emit = −(y_φ²/ω) Im R_OO(k_φ, ω),   ω = m_φ (+ k_φ²/2m_φ),                          (3.5)

  R_OO = R̃_OO + R̃_{Oμ} 𝒟^γ_{μν}(k_φ,ω) R̃_{νO}   (full = photon-proper part + photon-reducible part),                                  (3.6)

R̃ irreducible with respect to one photon line; 𝒟^γ the in-medium photon propagator (Coulomb part v_C/ε_L, transverse part
1/(ω² − k_φ² − Π^γ_T)). With y_φ²R̃_OO = Π_φφ, y_φR̃_{Oμ} = Π_φA this is 2106.12586 Eqs. (20)–(21) [FT]. ℛ = ρ_φΓ_net/(ρ_Tm_φ).

---
## 4. Exact relations at master level
Hypotheses: H of (1.1), Gibbs (or any stationary) state, operators of §2; extras stated per line.

**(4.1) FDT [D]** (WP0v2-C3a,b): (1 − e^{−βω})S_ab = i[R_ab − R_ba*]; diagonal S_aa = −2 Im R_aa/(1 − e^{−βω}).                             (4.1)
**(4.2) Spectral / KK [D]:** R_ab = R^∞_ab + ∫(dω′/2π)(1 − e^{−βω′})S_ab(q,ω′)/(ω − ω′ + i0). R^∞ = 0 for densities and spins; for
currents R^∞_{j^αj^β} = +δ_{αβ}𝓃_s/m_s (diamagnetic), needed for gauge invariance (R^L_{jj}(q,0) + 𝓃/m → 0).                             (4.2)
**(4.3) Detailed balance [D]:** S_ab[O](q,−ω) = e^{−βω}S_ba[O†](q,ω); for densities S_ab(−q,−ω) = e^{−βω}S_ba(q,ω). With inversion or time
reversal S(q,−ω) = e^{−βω}S(q,ω) and S(q,ω) = S(−q,ω). **Converse (WP4-D6):** with P and T both broken, S is nonreciprocal,
S(q,ω) − S(−q,ω) = 2q·𝐛_NR(ω) + O(q³), and the rate has a part odd in the DM wind (WP4 [3.1]–[3.2]); then the campaign sign of q (§2.1) is
binding. Chiral T-even targets show enantiomer differences only via 𝒪₅×𝒪₈ interference (WP4 [3.3]). Pointer: L19.                       (4.3)
**(4.4) Positivity [D]** (WP0v2-C3c): Σc_a*c_bS_ab = (2π/V)Σp_i|⟨f|Σc_bO_b|i⟩|²δ ≥ 0, so S is Hermitian PSD at each (q,ω) and Γ_χ ≥ 0;
|S_ab|² ≤ S_aaS_bb (e.g. |S_eκ| ≤ √(S_eeS_κκ)), Γ_χ ≤ ∫d³q/(2π)³ λ_max(𝔇) tr S.                                                      (4.4)
**(4.5) First-moment matrix [D]:** 𝓜¹_ab(q) ≡ ∫(dω/2π) ω[S_ab[O] + S_ab[O†]] = V^{-1}⟨[O_a†,[H,O_b]]⟩.                                    (4.5)

**(4.6) f-sum rules [D]** (WP0v2-C4a–c, e). Extra hypothesis (L): every term of H besides the kinetic energies is multiplicative in all
coordinates (true for H_C, H_hf contact, Zeeman; false for mass-velocity, non-local pseudopotentials). **[T_s, n_s(q)] = q·j_s(q) exactly**
(no (q²/2m)n term; WP1-D1, WP0v2-C4e), so [H, n_s(q)] = q·j_s(q) involves only species-s momenta and

  𝓜¹_{ss′} = δ_{ss′} q² 𝓃_s/m_s,   s, s′ ∈ {e, κ};   for densities with inversion  ∫_{−∞}^{∞}dω ω S_ss(q,ω) = π𝓃_sq²/m_s.              (4.6)

- (a) 𝓜¹_ee = 𝓃_eq²/m_e at every order in g and BO, any T, dynamic nuclei, all electrons (cores included); D2 §3 generalised. The integral
  runs over ω < 0 at T > 0. The normalisation is π, not 2π (WP6-W1, WP0v2-C9).
- (b) 𝓜¹_κκ = 𝓃_κq²/M_κ (× |F^M_κ|²).
- (c) **𝓜¹_eκ = 0**: Re S_eκ changes sign in ω; a one-signed Migdal or e–N interference spectrum is wrong. Its electronic/lattice split is
  not zero: 𝓜¹^{(L)}_eκ = −𝓜¹^{(e)}_eκ = 𝓃_κ(q²/M_κ)𝓕_κ(q) (WP3 J7).
- (d) Charge: 𝓜¹_cc = q²Σ_s z_s²e²𝓃_s/m_s ≡ q²ω_{p,c}², ω_{p,c}² = ω_{p,e}²(1 + Σ_κZ_κ²𝓃_κm_e/(𝓃_eM_κ)); the nuclear part is ~10⁻⁴.
- (e) Spin, SU(2) (SOC = 0, B₀ ∥ z): 𝓜¹_{s^zs^z} = 𝓃_eq²/(4m_e).
- (L) violated: 𝓜¹_ee = 𝓃_eq²/m_e + V^{-1}⟨[n_e†,[H_nl,n_e]]⟩. Mass-velocity (Breit–Pauli, closed shells; WP0v2-C4g; WP1 [E11]):

  𝓜¹_ee = (𝓃_eq²/m_e)[1 − (5/3)⟨T⟩/m_e − q²/4m_e² + O(m_e^{-4})],   ⟨T⟩ = mean kinetic energy per electron.                              (4.6′)

  Non-local pseudopotentials give the nonlocal f-sum owed in SOTA R2 (exact with the generalised current incl. [g^{NL}, q·r]).

**(4.7) Third-moment mixed sum rule [D]** (WP0v2-C4d, under (L)). With the electron–nucleus potential energy −U_κ(r) (U_κ(p) = Z_κ(p)e²/p², WP3):

  𝓜³_eκ(q) ≡ V^{-1}⟨[[n_e†,H],[H,[H,n_κ]]]⟩ = (1/(V m_eM_κ))⟨Σ_{i, I∈κ} e^{iq·(R_I−r_i)} (q·∇)² U_κ(r_i − R_I)⟩.                            (4.7)

For point nuclei, cubic sites and **q → 0 (qa ≪ 1)** ⟨(q·∇)²(−U_κ)⟩ → (q²/3)Z_κe²δ³ (at finite q the phase e^{iq·(R_I−r_i)} gives the traceless ℓ = 2 part of (q·∇)²U_κ a nonzero average), so 𝓜³_eκ = −q²Z_κe²𝓃_κ𝓃_e(R_κ)/(3m_eM_κ), with 𝓃_e(R_κ) the electron
contact density. The ω³ moment of Migdal-type mixed spectra is fixed by contact densities. Not found in the literature searched [E for
novelty]. Link to the 𝔨₃ (𝔨₃^{GS}/𝔨₃^X) split: closed at moment level by WP2-v2 (5.2′) and WP3-v2 J8 (q → 0) (F4 closed).

**(4.8) Translation Ward identities [D]** (WP0v2-C4f). P_tot = Σp_i + ΣP_I commutes with H_C, H_rel, H_hf. The mass density
ρ_M(q) = Σ_s m_sn_s(q) obeys [H, ρ_M(q)] = q·𝐠(q) exactly, 𝐠 the momentum density, 𝐠(0) = P_tot. For any B and ω ≠ 0:
Σ_s m_s S_{Bs}(q,ω) = (q/ω)·S_{B𝐠}(q,ω) = O(q²) as q → 0, whereas each term is O(q).                                                (4.8)
- (i) *Acoustic sum rule.* Rigid displacement u_κ = u ∀κ with adiabatic electrons: Σ_κ∂_{u_κ}V_pot^{scf} = −∇V_pot^{scf}; Σ_κΦ^{(2)}_{κα,κ′β}(0) = 0,
  Σ_κZ*_κ = 0; for the acoustic branch at Q = 0, g_mn(k,0) = (ε_nk − ε_mk)𝔄_mn with 𝔄 = −iℓ_Q ê·p, so g_nn(k,0) = 0 (X1 H3; holds with
  non-local PPs that move with the ions).
- (ii) The strictly Q = 0 acoustic mode is the centre-of-mass mode (H = P_tot²/2M_tot + internal part): its creation amplitude by any O(q)
  is iℓ_Q(ê·q)O, the contact term of (4.9). At small Q ≠ 0 the mode is a strain wave; the limit is (4.9).

**(4.9) Soft acoustic limit = X1 (X1) [D under X1 H1–H4]** (C7 = X1 §5 C7a–e; WP3 confirmed; WP0v2-C12). D1 normalisation of M^{(2)}
(no 1/√N), ℓ_Q = (2M_cellω_{Qν})^{-1/2} with N outside, upper sign = emission of −Q, index order Q̂·Ξ^n·ê, Ξ^n = D^n + v^g_n ⊗ p_nn:

  M^{(2)}_{cvν,±}(k,q,Q→0) = iℓ_Q ρ_cv(k,q) [ ê·q + (Q̂·D^c·ê ∓ c_ν ê·p_cc)/(Q̂·v^g_c ± c_ν) − (Q̂·D^v·ê ∓ c_ν ê·p_vv)/(Q̂·v^g_v ± c_ν) ] + O(|Q|^{1/2}),  (4.9)

with v^g_c, p_cc at k+q and v^g_v, p_vv at k; D^n the frozen-strain (comoving) deformation tensors, the only material constants
(|D|/c_ν ~ 10² keV ≫ q). Equivalent lab form: iℓ_Qρ_cv[ê·(q − p_cc + p_vv) + Q̂·Ξ^c·ê/(Q̂·v^g_c ± c_ν) − Q̂·Ξ^v·ê/(Q̂·v^g_v ± c_ν)].
v1's (4.9) differs by ê·(p_cc − p_vv) (lab reading) and carried N inside ℓ_Q (M_v1 = M_X1/√N); it agrees only at band extrema (WP3 [C1d]).
Consequences (X1 §6–§7) [D]: inside the window |Q| ≥ Q_min ≃ (E_min(q) − ω)/(v_max^g + c_ν) on shell, so no IR feature; no subtraction,
detuning-form denominators, zero weight at acoustic Γ, σ ≪ δ₀. Outside the window: Low-type soft bremsstrahlung, finite in 3D for
deformation coupling, BN-log only for piezo (GaAs) where the ZPL is open; Cherenkov-cone poles are the real cascade (not counted twice).

---
## 5. Screening from first principles

**(5.1) Definition [D].** Restrict v_C to the external channel {q+G}. R̃ is irreducible with respect to one Coulomb line of that channel,
in the super-space (a; G) (exact: the response to the total external + Hartree potential of the channel). Lines at all other momenta stay
inside R̃. H_C couples only through ρ_c, so

  R = R̃ + R̃ Zᵀ v_C Z R,   (Z)_{G; sG′} = z_s δ_{GG′},   v_C = diag v_C(q+G).                                                      (5.1)

**(5.2) Screened formula [D]** (WP0v2-C1, C2). With R̃_ac ≡ Σ_s R̃_as z_s and the total longitudinal dielectric matrix (electrons + nuclei, LFE)

  ε_{GG′}(q,ω) ≡ δ_{GG′} − v_C(q+G) R̃_{cc,GG′}(q,ω),                                                                              (5.2)

  R_ab = R̃_ab + R̃_ac ε^{-1} v_C R̃_cb   for arbitrary operators a, b (matrices in G; DM vertex at G = 0, unreduced-q convention §2 of CONVENTIONS). (5.3)

Rank one (no LFE): R_ab = R̃_ab + v_C R̃_acR̃_cb/ε (Sherman–Morrison in species space). TDDFT: v_C → f_Hxc in the proper part, ε → ε̃.

**Dependence on the coupling vector c_s [D]** (O_c = Σ_s c_sn_s):
- *Total charge (dark photon), |c⟩ ∝ |z⟩:* R_zz = v_C^{-1}[(ε^{-1})_00 − 1], so S_zz = (2q²/e²)Im[−(ε^{-1})_00]/(1 − e^{−βω}) with the **total**
  ε (WP0v2-C1b). This is the ELF form.                                                                                            (5.4)
- *Electron density only, |c⟩ = |e⟩ = −|z⟩ + Σ_κZ_κ|κ⟩:* R_ee = R_zz − Σ_κZ_κ(R_zκ + R_κz) + Σ_{κκ′}Z_κZ_κ′R_κκ′.                          (5.5)
  S_ee = (2q²/e²)L holds iff the nuclear terms vanish: (i) exactly at clamped nuclei (WP0v2-C1c), or (ii) at ω ≫ ω_max up to O(κ_BO⁴).
  In general ε_e^{-1} ≡ 1 + v_CR_ee gives S_ee = (2q²/e²)Im[−ε_e^{-1}]/(1 − e^{−βω}) exactly, with ε_e ≠ ε.
- *Nucleon number, |c⟩ = Σ_κA_κF^M_κ|κ⟩:* R_NN = R̃_NN + R̃_Ncε^{-1}v_CR̃_cN, the electronic plus ionic screening of the DM–nucleus vertex.
  The **external vertex stays A_κF^M_κ**; the Z*/ε_∞ structure appears only inside the Dyson series that turns TO into LO (WP2 (4.4)); an
  external Z*/ε_∞ vertex belongs to charge coupling (WP2-C1, WP2 (4.2)). Two-component limit: Bohm–Staver ω² = Ω²_{p,ion}/ε_e(q,0) [D].
- *Non-density operators [D].* (5.3) screens a only through R̃_ac. By (4.6), q·j_L = [H, n], so S_{n j_L} = (ω/q)S_nn and S_{j_Lj_L} = (ω/q)²S_nn,
  screened or not: **j_L is screened exactly like n**. **j_T is screened through local fields**: j_T(q) couples to n(q_r + G ≠ q), so
  R̃_{j_T, n(q_r+G)} ≠ 0, ≈ 10–30% [E] (WP1-D4); the transverse-photon part is O(ω_p²/q²) ≈ 2×10⁻⁵ at 4 keV. **Spins at SOC = 0** are not
  Coulomb-screened (singlet/triplet decoupling) but are xc-renormalised: R̃_s = R⁰ + R⁰f_xc^TR̃_s, S_{s^αs^β} = (δ_{αβ}/4)S^{IP}_nn at IP, with
  no 1/|ε|² (WP1-D5, [E6]); with SOC or magnetic order R̃_{s,c} ≠ 0 (Si ≲ 2%, Ge ≲ 10% in amplitude near the edge [E]). Rule: screen
  every operator with R̃_ac ≠ 0 (L3 correction).

**(5.5) Coulomb-line classes and no double counting [D at RPA/adiabatic TDDFT (ring) level; X2 §3–§4].** In a Coulomb-proper O(g²)
diagram with one external vertex (q,ω), one phonon line (Q,ω_Q) and a final pair, every Coulomb line is in exactly one class:
- *external* (q+G, ω): resums into ε̃^{-1}_{G0}(q,ω), local fields included (v1 kept only G = 0);
- *DFPT* (Q+G, ν ≈ ω_Q): the screened g; static DFPT errs by O(ω_Q²/E_g²) ≈ 3×10⁻³ (ε̃ even and analytic in ν below E_g; v1's O(ω_Q/E_g) is
  superseded); the non-adiabaticity of the amplitude, O(ω_Q/δ), is separate (D1 §4);
- *pair* (P+G, ω_f), P = q+Q, ω_f = ω ∓ ω_Q: W^{scr}(P,ω_f) = ε̃^{-1}(P,ω_f)f_Hxc(P) between two triangles;
- *ionic* (phonon line at q mod G, the "X" diagram): the ionic part of ε(q,ω); ≲ 10⁻⁴ in Si, ~10⁻³ absolute in polar targets (X2 §7).
Proof: removing the phonon line leaves a tree; the phonon line closes exactly one cycle; a line off the cycle is a bridge (only the improper
external chains, resummed once); on the cycle, the segments adjacent to the ion vertices are DFPT, the middle one is the pair channel. The
classification is topological, so it holds at q → 0 (P = Q) and Q → 0 (P → q). v1's statement "the pair channel is inside R̃ at (q,ω)" is
the same argument. Lines inside one loop (ladder, direct W) are excitonic and beyond this level [C].

**(5.6) PAER rate with full screening [D; X2 (2.3)]** (H5 window; RPA/ALDA, KS bands, O(g²), harmonic, static DFPT g):

  S^{X+}_ee(q,ω) = (4π/Ω) ⟨⟨Σ_{cvν±}(n_{Qν}+½±½) |M̃_{cvν,±}(k,q,Q)|² δ(ε_{c,k+P} − ε_{vk} ± ω_{Qν} − ω)⟩⟩ = (2q²/e²)L^{PA}(q,ω),            (5.6)

⟨⟨·⟩⟩ = N^{-2}Σ_{kQ}, spin 2 included, T ≪ E_g (otherwise divide L^{PA} by (1 − e^{−βω})). Inside the window ε̃^{-1}(q,ω) is
non-absorptive, so (5.6) is exact to O(g⁴) at this level (the ε₂²-term of |ε|² is O(g⁴); D1's H2 is redundant there).

**(5.7) Screened amplitude [D; X2 (2.2)]:**

  M̃_± = M^{(2)}_±[ρ̃] + Σ_{GG′} ρ_cv(k, P+G) W^{scr}_{GG′}(P, ω_f) 𝔗_{G′}(P),   ρ̃_mn(k,q) = Σ_G (ε̃^{-1})_{G0}(q,ω) ρ_mn(k, q+G),           (5.7)

M^{(2)} = D1 eq. (1) (unrestricted m sum, D1 normalisation; D2's is M^{(2)}/√N), 𝔗 = X2 (2.1) (all band pairs). Limits [D]: coherent
potential (M = Uρ for all pairs) gives M̃ = M/ε(P,ω_f) exactly (WP0v2-C7b); the rigid (convective, e^{iq·u}) component is screened by
ε(q,ω_f) to all orders in ω_Q/ω (REF-A's prescription, exact only there); no 1/|ε|⁴ arises.
**(5.7′) v1's projected form is a truncation** (WP3-2): G = G′ = 0, the triangle restricted to resonant pairs, M continued off shell:

  M̃^{(5.7′)}_{cvk} = M_{cvk} + ρ_cv(k,P)[v_C(P)/ε(P,ω_f)] R̃⁰_{ρ†M}(P,ω_f),   R̃⁰_{ρ†M}(P,ω_f) = (2/V)Σ_{k′c′v′} ρ*_{c′v′}(k′,P)M_{c′v′k′}/(ω_f − ε_{c′,k′+P} + ε_{v′k′} + i0),

with the optical-theorem identity Im[R̃⁰_MM + R̃⁰_{M†ρ}v_Cε^{-1}R̃⁰_{ρ†M}] = Σ|M̃|²Im(…) (WP0v2-C7a). v1's prediction (two factors: external
plus projected pair channel, reducing to |ε(P,ω_f)|^{-2} iff M ∝ ρ; REF-A's ε(q,ω∓ω_Q) as the Q → 0 case) is CONFIRMED by X2 and WP3.
**Sizes [E] (X2 §6):** δ_ω ≈ 1–2%, δ_LF ≈ 5–20%, δ_pair ≈ −(10–50)% (sign [C]); interim systematic on L^{PA}: factor [0.5, 1.2] until
X2-N2/N3. The dark photon adds no PAER amplitude at O(e·g) (ions only via ε_tot in the external and pair channels). Recommended code
route: ZG/frozen-phonon supercell with RPA local fields in the supercell basis (contains every class). Same structure at q → 0 (L9).

---
## 6. Expansion hierarchy and decomposition theorem

**Table 6.1. Small parameters** (Si values [E]):

| symbol | definition | Si | controls |
|---|---|---|---|
| κ_BO | (m_e/M)^{1/4}; u^{zp} ~ κ_BO × bond length, ω_ph ~ κ_BO² E_el, non-adiabatic mixing ~ κ_BO³ | 0.066 | BO order n_B |
| η_ep(q,ω) | ⟨\|g\|²⟩/δ², δ = off-shell distance (D1 §5; |d| ≥ min(E_min(q) − ω, E_g − ω_max)) | 10⁻³–10⁻¹ | e–ph order n_g |
| η_anh | ⟨u²⟩^{1/2}\|Φ^{(3)}\|/\|Φ^{(2)}\| | 0.01–0.03 (T = 0) | n_A |
| η_xc | ‖f_xcR̃‖/‖v_CR̃‖ (LFE); E_x^b/E_g | 0.2–0.5; 0.013 | ladder 𝒳: **not small**, error = computed next-rung difference |
| t_ph, t_g | T/ω_ph, T/E_g | 10⁻³ at 50 mK | thermal order n_T |
| x_R | q²/(2M⟨ω⟩) | 0.05 at 10 keV | 1-ph → multiphonon → impulse (K) |
| 2W_κ(q) | q·B_κ·q, B_κ = ⟨u_κu_κ⟩; = (q²/2M_κ)⟨coth(βω/2)/ω⟩ only for cubic sites | ≈ x_R (Einstein) | FC weight e^{−2W} (direction-dependent in general, enters L19) |
| n_ph; z_ΔR\|j₀(qΔR)\|c̄_ΔR^{n_ph} | phonon order; shell parameter (WP2 (2.3)–(2.4)) | — | coherent vs incoherent (replaces x_coh, retired) |
| σ_c | ΔE_e/(q v_rel) | — | sudden vs adiabatic Migdal (𝔐) |
| ξ_D | q_e r_n (q_e = q for ER, ≈ m_eq/M for Migdal) | — | multipole order n_D |
| broken symmetry | SC: Δ_BCS/E_F (~10⁻⁵), (T_c/ω_D)²ln, 1/k_Fℓ_mfp (O(1) in amorphous WSi), Δ_BCS/v_Fq (≤ 0.2); magnets: 1/(2\|𝐒_j\|), (hopping/Hubbard U)², q·r_3d (form factor) | — | reference metadata (WP4-D4) |

x_coh = q/G_min is neither sufficient (at n_ph = 1 the coherent S stays a δ on the dispersion at any q) nor necessary (n_ph ≥ 2 incoherent is
accurate in ω-integrated rates even below q_BZ) (WP2-D1). A one-phonon **incoherent** regime exists at q_BZ < q ≪ √(2Mω̄) (Si 5–20 keV)
(WP2-D3). Truncation N-phonon loses P[Pois(2W) ≥ N] of the f-sum (WP2).

**Truncation multi-index (CONVENTIONS §11).** τ = (n_B, n_g, n_A, 𝒳, n_T, K, 𝔐, n_D), 𝒳 ∈ {IP, RPA, RPA+LFE, TDDFT, BSE},
K ∈ {1ph-coh, 1ph-inc, multi-coh, multi-inc, imp}, 𝔐 ∈ {ad, sud}; n_T is an order, never a temperature. Mandatory metadata (not orders):
T; ref ∈ {normal, BCS, LSWT, …}; scr ⊆ {ext, LFE, DFPT, pair, ion}; conv ∈ {window, DC}. Library string
`nB=0|ng=0|nA=0|X=RPA+LFE|nT=0|K=-|Mg=-|nD=-` + `T=130K;ref=normal;scr=ext,LFE;conv=window`. Every LIMITS entry is a point τ (table (9.7));
the error model is the increment Δ^τ_k = S^{τ+e_k} − S^τ entered by type (§8).

**§6.2 Decomposition theorem.**
*Hypotheses.* (H1) H = H_C plus optional local terms obeying (L). (H2) The adiabatic electronic ground state Φ₀(r;R) is non-degenerate and
gapped, Δ_ad(R) ≥ E_g > 0, on the support of the vibrational state (insulator, no conical intersection there). (H3) Harmonic ground-surface
vibrations plus perturbative anharmonicity. (H4) T ≪ E_g. (H5), for the X0/X+ split only: every intermediate state in the excited block is
off shell by δ ≫ widths (D1 §5.4 window, ω ≤ E_min^{ren}(q,T) − δ₀).
**Scope of (H2) (WP4-D2) [D that it fails].** (H2) fails for every gapless target: metals, superconductors, semimetals (Δ_ad = 0 on the Fermi
surface; in superconductors Δ_BCS ≪ ω_D reverses the adiabatic hierarchy). For these the sectors must be quasiparticle-number sectors
(Bogoliubov quasiparticles and phonons via Migdal–Eliashberg, small parameter ω_D/E_F ~ κ_BO²), not adiabatic projectors [C]. Theorem D
applies to insulators, magnetic insulators, gapped Dirac materials with Δ_D ≫ ω_ph, and deep defects.
*Construction.* 𝒫₀ = ∫dR|Φ₀(R)⟩⟨Φ₀(R)| ⊗ |R⟩⟨R|, 𝒫_⊥ = 1 − 𝒫₀. Space-adiabatic perturbation theory (math-ph/0201055 [ABS]) gives, under
(H2), U_n with 𝒫_⊥U_n†HU_n𝒫₀ = O(κ_BO^{n+1}). Sectors: **GS** f ∈ U_n𝒫₀ℋ (electronic ground manifold); **X0** f ∈ U_n𝒫_⊥ℋ with zero net
change of reference phonon number; **X+** f ∈ U_n𝒫_⊥ℋ with ≥ 1 net phonon; X = X0 ∪ X+.
*Theorem D.* For all a, b:   S_ab = S_ab^{GS} + S_ab^{X0} + S_ab^{X+} + O(κ_BO^{n+1}).                                                        (6.1)
- **(i)** [D given U_n] GS and X = X0 ∪ X+ are restrictions of (3.1) by orthogonal projectors summing to 1: each is Hermitian PSD, no double
  counting, nothing omitted (PST rigorous for smooth potentials; Coulomb singularities assumed harmless [C]). The X0/X+ projectors exist only
  under (H5): **per-sector PSD of X0 and X+ holds inside the window, or for bins ≳ δ** (O4 §9). Outside, the split is the DC assignment
  (iv′) on H₀: S^{X+}_DC contains fp(1/δω²), negative against a narrow positive test function (WP0v2-C13a), and Z_Λ₀ may exceed 1.
- **(ii)** O′ = U_n†OU_n, leading order. (O′_e)_{GS,GS} = ρ̄_e(q;R) = ⟨Φ₀(R)|n_e(q)|Φ₀(R)⟩: electrons follow the nuclei (Z*, ε_∞, phonon peaks
  in the electron channel; 𝓜¹ weight O(κ_BO⁴)). (O′_e)_{X,GS} = ⟨Φ_n(R)|n_e|Φ₀(R)⟩: expanding in u gives the ZPL with FC e^{−2W} (X0) plus the
  Herzberg–Teller sideband (X+, O(κ_BO²)); non-adiabatic error O(κ_BO²ω_ph/δ) (D1 §4). (O′_κ)_{X,GS} ≈ (q/M_κ)·⟨Φ_n|∇_RΦ₀⟩/(E^ad_n − E^ad_0)e^{iq·R}:
  **Migdal is purely non-adiabatic** (agrees with 2505.08864 Eq. (21) [FT via WP3]), amplitude ~ (q × bond length)κ_BO⁴. For one nucleus
  ∇_RV_eN = −Σ_i∇_{r_i}V_eN and ⟨n|Σ∇_iV_eN|0⟩ = m_e(E^ad_n − E^ad_0)²⟨n|Σr_i|0⟩, so the amplitude is the boost (m_eq/M_κ)⟨n|Σr_i|0⟩ [D, sketch]. **Boost
  mass (WP3-5):** with electron drag the lattice sees M_κ + δM_κ, δM_κ ≡ 2Σ_{a≠0}Re⟨0|∇_{R_κ}V_eN|a⟩⟨a|∇_{R_κ}V_eN|0⟩/(E^ad_a − E^ad_0)³; for an atom
  δM = N_em_e, so the atomic L7a uses m_A (1707.07258 Eq. (73)), the crystal uses M_κ with the tensor δM_κ (δM/M ≤ 2.7×10⁻⁴ Si [E]).
- **(iii)** Partial sum rules [D]. 𝓜¹_ee: X0 + X+ = 𝓃_eq²/m_e − O(κ_BO⁴); the SOTA #3 compensation is a **first-moment** statement (X+ gains
  what X0 loses through the Fan + vertex non-phonon cuts, as a sum; not the AH tadpole). 𝓜¹_κκ: X carries 𝓜¹^{(e)}_κκ = 𝓃_κ q·δM_κ·q/M_κ²
  (Migdal energy moment E^{Mig}_1(q) = q·δM_κ·q/(2M_κ²) per nucleus; WP3 J3), GS the rest. 𝓜¹_eκ = 0 summed over sectors, with the
  nonzero split of (4.6c). **Zeroth moments:** there is no global rule for n_e (REF-B, WP3 J4). O4's identity Z_Λ₀ + (1/2π)fp∫Γ_Λ₀/δω² = 1
  holds per X0 pair **for the Fan (self-energy) part only**; the vertex term Re Υ_Λ₀ changes |ρ^{ren}|² (CORRECTIONS O4 §3 scope). For n_κ
  (incoherent) GS is depleted by P_Mig(q) (WP3 J4). The soft sector obeys the X1 coherent-state (BN) rule.
- **(iv)** X0/X+ split. *Inside the window:* unique to O(η_ep) [D]. *Outside:* fixed by the **Dyson convention DC** (O4 (iv′), CONVENTIONS §10):

  S^{X0}_DC = Σ_Λ₀ 2πZ_Λ₀|ρ^{ren}_Λ₀|²δ(ω − Ẽ_Λ₀);   S^{X+}_DC per Λ₊: 2πδ(ω − E_Λ₊)|g|²[|ρ|² fp(1/δω²) + 2Re(a^{off*}ρ)PV(1/δω) + |a^{off}|²],  (6.3)

  δ part → X0 (handed to the cascade), fp and PV parts → X+. Inside the window DC = D1 eq. (4) with no δ part. Results (O4):
  (iv″a) [D] totals are convention-independent to O(g², Γ²/δ²) against test functions smooth on δ; (iv″b) [D] the cascade-convolved
  P(N_eh|q,ω) is invariant if the cascade is Markov in Λ and its first-emission kernel uses the same g, ω_Q, energies and includes the Fano
  term 𝔉_{Λ₀,ν} (zero for PT-symmetric Si, Ge, diamond [D, sketch]; generically ≠ 0 in GaAs [C]); (iv″c) [D] within 𝒞_adm(ℓ_win) the split
  moves by |Δw₀|/w₀ ≲ (1.1 + b_λ)Γ/δ, and is FALSE universally (the t → ∞ convention moves O(1)); (iv″d) code pairs must satisfy O4 d1–d11
  (one kernel; same g, energies, width Γ(ω), Z and vertex, first emission once, 𝔉 export, smearing, T, non-phonon channels in the cascade
  only, edge shell). Mixed conventions double count: Lorentzian ZPL + fp sideband is O(g²), Lorentzian ZPL + resummed sideband is O(1)
  (O4 T3a,b). Within |ω − E_min(q)| ≲ few Γ (Si Γ/δ ≈ 0.02–0.6 [E]) only totals and P(N_eh) from the unexpanded Dyson form are quoted.
  A mathematically rigorous version needs a fibred limiting-absorption principle, a C*-dynamical thermodynamic limit, Coulomb stability
  with dynamical lattice, and an IR-safe X+ definition (O4 §8) [C].

*Sector dictionary* (the final state decides, not the coupling):

| | GS | X0 | X+ |
|---|---|---|---|
| S_ee | adiabatic electron-following | ZPL: clamped/ZPR-renormalised response, FC-reduced (L1–L3, L10–L11, L14) | PAER (L8), L9, exciton–phonon replicas |
| S_κκ | 1-phonon, multiphonon, NR (L4–L6, L18) | zero-phonon Migdal: n = 0 term of L7d, δ(ω_ph) part of WP3 (W.5) | Migdal with phonons/recoil (L7a–c), n ≥ 1 of L7d |
| S_eκ | Born-charge interference | ionic screening of the ZPL | Migdal–PAER interference for **any 𝔇 with c_ec_κ ≠ 0** |

The X sector of S_eκ carries a fixed negative ω_e-moment, −𝓃_κq²𝓕_κ/M_κ, equal and opposite to the lattice-energy weight of the GS
Born-charge interference (WP3 J7, WP3-4): a one-signed model of it is wrong.
*Double-counting rules [D]:* (a) multiphonon S_κκ normalised to 𝓃_κq²/M_κ plus Migdal overcounts 𝓜¹ by exactly 𝓃_κq·δM_κ·q/M_κ² and the
zeroth moment by P_Mig (≤ 3×10⁻⁴; WP3 N1); (b) never add the resonant sideband to the ZPL (D1 §5.2; O4 T3); (c) measured ELF/σ₁ contain
X0 + X+: never add a computed sideband to data, nor PAER to a ZG spectrum (WP3 N4, N5); (d) with c_ec_κ ≠ 0, Migdal and PAER amplitudes to
the same final state interfere (bounded by (4.4)); (e) neutron-calibrated yields contain Migdal: fit Y_tot, never Y_casc plus Migdal (WP3 N3).

---
## 7. From response to signal: the final-state-resolved response

**(7.1) Definition [D].** Orthogonal projectors {P_Λ} on prompt final states, Σ_ΛP_Λ = 1:

  S_ab(q,ω;Λ) = (2π/V)Σ_i p_i⟨i|O_a†P_Λ δ(ω − H + E_i) O_b|i⟩,   Σ_Λ S_ab(q,ω;Λ) = S_ab(q,ω).                                             (7.1)

Each S(·;Λ) is PSD (inside the window; outside, per §6.2(i)). Λ = prompt state after dressing (~1/E_g), before relaxation (~1/ω_ph):
e–h (n_e,k_e,E_e; n_h,k_h,E_h; spin, valley), E_e − E_h = ω_e (carrier energies E_e, E_h); phonon content n_ph, {Q_jν_j}, ω_ph = ω − ω_e
(WP3 joint response (W.1)); core hole (shell; seeds Auger); nuclear: E_R, direction, defect label. **Within RPA there is no separate
plasmon label:** the plasmon is a pole of ε^{-1}, its decay products are already the cvk pairs of (7.2) (WP5-3, Theorem C (a)); a collective
label is needed only beyond RPA or when the mode can escape or convert (films, WP4).

**(7.2) IP and screened pair-resolved forms [D].** IP: S(q,ω;cvk) = (4π/V)|ρ_cv(k,q)|²δ(ω − ε_{c,k+q} + ε_vk). RPA+LFE (TDDFT: ε → ε̃):

  S(q,ω;cvk) = (4π/V) |Σ_G (ε̃^{-1})_{G0}(q,ω) ρ_cv(k,q+G)|² δ(ω − ε_{c,k+q} + ε_vk),   (ε^{-1})_{G0} = δ_{G0} + v_C(q+G) R_{G0}(q,ω),        (7.2)

with **retarded** R_{G0} in the index order of (3.2) (a = n_e(q+G), b = n_e(q)). *Proof.* Two exact factorisations hold for any target
(WP0v2-C10a): R − R† = (1 + R†f)(R⁰ − R⁰†)(1 + fR) = (1 + Rf)(R⁰ − R⁰†)(1 + fR†), f = v_C (RPA) or f_Hxc. The first gives (7.2): the
external potential induces the total potential (ε̃^{-1})_{G0}φ_ext at q+G (causal, retarded), which creates bare outgoing pairs, i.e. the
**out-state** (prompt-final-state) labelling. The second is the in-state labelling, weight δ_{G0} + f(q+G)R^A_{G0} = [(1 + Rf)_{0G}]*. Both sum
to the same exact Im R_00 for every target, centrosymmetric or not (WP0v2-C10b,c); pair by pair they differ when pairs are open at (q,ω)
(WP0v2-C10d) and coincide when R(q,ω) is Hermitian, e.g. the external factor in the PAER window (WP0v2-C10e). Σ_cvk reproduces (5.4); the
pair-channel dressing (5.7) applies to X+. Relation to WP1 [E2] and CORRECTIONS WP1-D6: §10 (contested) and flag F1.

**(7.3) Interface to WP5 [D given (7.1); WP5 (W5)–(W6)].** Seeding keeps q, v and the operator structure inside the final-state sum:

  dℛ/d𝐍 = (ρ_χ/m_χρ_T) ∫d³v f_χ(v) ∫d³q/(2π)³ Σ_Λ tr[𝔇(q,v) S(q,ω_q;Λ)] P_casc(𝐍|Λ),   𝐍 = (N_eh, ℋ, E_st, N_FP, E_esc, …),            (7.3)

and at fixed (q, ω, v) the quanta distribution is P(N_eh|q,ω) = Σ_Λ tr[𝔇S(q,ω;Λ)]P_casc(N_eh|Λ)/tr[𝔇S(q,ω)] (the single-operator ratio of
v1 holds only for one operator; spin and current rows populate (E_e, E_h, k) differently; WP5-2). v1's ∫dω(dℛ/dω)P(N_eh|q,ω) integrated q
out before seeding and is ill defined (WP5-1). **Hand-over to WP5:** per operator, the joint density of (E_e, E_h, k_e, k_h | q, ω); for X+:
n_ph and ω_ph (WP3 (W.1)); for GS (NR): E_R and direction (multiphonon S^{GS}_κκ and final-state phonon spectrum ρ^{ph}_κ, WP2 (3.6)); core-hole
shell fractions; under DC the O4 d6 seeds (X0 at (Λ₀, Ẽ_Λ₀, n_ph = 0) with first emission in the cascade, X+ at (Λ₊, n_ph = 1) with none) and,
for non-PT targets, 𝔉_{Λ₀,ν} (O4 d7). Only the first generation keeps the q memory (WP5 (W7)). **R&K (L21)** is a photon-seed (q ≈ 0) fit,
not the Λ-marginal of the DM seed (WP5-4); using it is the WP5 θ_seed nuisance.

---
## 8. Uncertainty structure (interface to WP6)

**(8.1) Nuisance per truncation [D as a definition, WP6 (5.1); E as to sizes].** For each active truncation k in τ, with Δ^τ_k = S^{τ+e_k} − S^τ
(computed; for the ladder 𝒳 always the computed next-rung difference) and r^M_k = Δ^τ_k/S^τ:
- (M) multiplicative log-normal S(θ) = S^τΠ_k(1 + r^M_k)^{θ_k}, θ_k ~ 𝒩(0,1): PSD for all θ, equal to the additive form at first order
  (WP0v2-C14c);
- (A) additive for support-opening truncations (S^τ = 0 on part of (q,ω), e.g. the PAER window): S = S^τ + a^A_kΔ^τ_k, a^A_k > 0 log-normal,
  central value includes Δ^τ_k once computed (PAER: 68% range [0.5, 1.2], X2 interim);
- (E) energy shift S(q, ω − θ_Eσ_E) (edges, ZPR, E_g(T));
- (Δ) discrete model choices: discrete profiling or envelope.
v1's additive Gaussian S^τ + Σθ_kΔ_k violated (4.4) wherever |Δ_k| ≳ S^τ (WP6-W2) and is withdrawn. One θ_k per truncation, applied
coherently across (q,ω), targets and experiments sharing the physics.                                                             (8.1)

**(8.2) Exact constraints [D].** f-sum: ∫_{−∞}^{∞}dω ω S(q,ω;θ) = π𝓃_eq²/m_e (densities with inversion; ω < 0 included at T > 0;
WP6-W1). It is **vacuous** (∫ωΔ^τ_k = 0) for every conserving truncation, i.e. every rung of the 𝒳 ladder with local potentials (WP6-W3),
and informative only for non-conserving ones: q/band cutoffs (closed analytically by an f-sum-saturating impulse tail, WP6 (5.2)),
non-local pseudopotentials, a sideband without its Fan/vertex compensation. Positivity is automatic for M and A. L17 (9.6) restricts the
support of θ (it is not a prior). Anti-correlations follow from shared physics (PAER sideband vs ZPL loss, SOTA #3).                   (8.2)

**(8.3) Propagation and reporting [D, WP6 (6.1)–(6.3)].** ℒ(σ̄_e,θ,θ^det) = Π_{ex,i}Pois(n|σ̄_e s_{ex,i}(θ, θ^det_ex) + b) Π_kπ_k(θ_k) Π_{ex}π(θ^det_ex),
halo fixed (2105.00599). Report three objects: WP6-R1 nominal (θ = 0, central τ*), WP6-R2 theory-profiled (headline), WP6-R3 band (envelope
over |θ_k| ≤ 1, separate halo band, halo-independent bound). Profiling costs O(δ²) (1 + 2.71δ²/4), the envelope O(δ) (1/(1 − δ));
up to ×1.8 at δ = 0.5 (WP0v2-C14a,b; WP6-W4); the choice must be declared.                                                          (8.3)

---
## 9. L0 and L17 derived; pointers for every LIMITS entry

**§9.1 L0 [D].** Chain: (3.3) → single operator (𝔇 = |𝒱_{n_e}|²δ_{a,n_e}δ_{b,n_e}) → Δ_χ = 0 → Born → (2.2) anchor:

  Γ_χ = ∫d³q/(2π)³ |Ṽ(q)|² S_ee(q, ω_q),   |Ṽ|² = πσ̄_eF_DM²/μ_χe²,   ω_q = q·v − q²/2m_χ.                                             (9.1)

**Hypothesis (I): S angle-averaged (S → S̄), or an isotropic target** (not isotropic f_χ; the lab-frame SHM is anisotropic; WP6-W5). Then
⟨δ(q̂·v − v_min)⟩_q̂ = Θ(v − v_min)/(2v), so 𝒢(q,ω) = ∫d³v f_χδ(ω − ω_q) → η(v_min)/(2q) with η built from the full f_χ (WP0v2-C11a) and

  dℛ/dω = (ρ_χ/m_χρ_T)(πσ̄_e/μ_χe²)∫q²dq/(2π²) F_DM² [η(v_min)/2q] S̄_ee = (ρ_χσ̄_e/(4πm_χρ_Tμ_χe²)) ∫q dq F_DM² η(v_min) S̄_ee(q,ω).        (9.2)

(9.2) = D1 eq. (3) with 𝒢 = η/(2q) (D1's η/q owes a factor 2) = WP6 (1.4) = Hochberg 2101.08263 (S.9) = 1509.01598 Eq. (17) via
|f_crys|² = Ωq³S̄_ee/(4παm_e²) (WP1 [E12], 2101.08275 Eq. (16) [FT via WP1]) (WP0v2-C11b).
*Validity:* (a) Born, |Ṽ|μ_χq/4π ≪ 1; (b) only 𝒪₁^{(e)}, or the other 𝔇_ab suppressed by v and q/m_e powers of (2.2); (c) elastic DM;
(d) S_ee is the full electron-density response; the ELF form needs (5.5)(i) or (ii).
*Leading corrections:* (α) cross-operator terms 2Re𝔇_{n,j}S_{n,j} ~ (q/m_e)(v_χ, v_el): longitudinal velocity operators reduce to n exactly
(S_{nj_L} = (ω/q)S_nn, local H), and on shell only P_Tv_χ and j_T survive (WP1 [E4]); (β) second Born ~ μ_χ|Ṽ|q/4π; (γ) T > 0: the ω < 0 branch
∝ e^{−β|ω|} (4.3); (δ) anisotropy: first correction ℓ = 4 in cubic crystals, no ℓ = 2 (WP6 (1.5)); P,T-broken targets add a v-odd part (4.3).
**Status: DERIVED.**

**§9.2 L17 [D].** For a coupling channel ch ∈ {c (total charge), e (electrons only)}:

  L_ch(q,ω) ≡ (e²/2q²)(1 − e^{−βω})S_chch(q,ω) = −v_C Im R_chch = Im[−ε_ch^{-1}],   ε_c ≡ ε (5.2),  ε_e^{-1} ≡ 1 + v_CR_ee.             (9.3)

Exact relations: positivity gives L_ch ≥ 0 for ω > 0; with inversion or TR, L_ch is odd in ω; KK at ω = 0 (R^∞ = 0):

  ∫₀^∞(dω/ω) L_ch = (π/2)[1 − ε_ch^{-1}(q,0)] = (π/2)(−v_CR_chch(q,0)) ≥ 0     (2110.01587 Eq. (1); 2608.05282 Eq. (1) [FT]),               (9.4)

  ∫₀^∞dω ω L_ch = (π/2)ω_{p,ch}²,   ω_{p,e}² = e²𝓃_e/m_e (all electrons),   ω_{p,c}² = ω_{p,e}² + Σ_κZ_κ²e²𝓃_κ/M_κ,                          (9.5)

  K_n^{(ch)}(q) ≡ ∫₀^∞dω ω^n L_ch ≤ (π/2) ω_{p,ch}^{n+1}[1 − ε_ch^{-1}(q,0)]^{(1−n)/2},   −1 ≤ n ≤ 1   (Hölder; WP0v2-C5),                (9.6)

which is 2608.05282 Eq. (8) [FT]; inserted in (3.4) with η_n^max it gives their Eq. (9) and 2110.01587 Eq. (4) [FT].
*URF content.* (i) Holds at all orders in g, BO, anharmonicity and the 𝒳 ladder, at any T (with the factor (1 − e^{−βω_th})^{-1});
the X+ sideband cannot violate it; a truncated "static ZPL + sideband" can, by up to 𝓜₁^{SB} (D2 §3). With (4.6′), ω_{p,e}² carries the
relativistic factor. (ii) **Channel:** electron-only coupling needs ε_e(q,0) (fully relaxed, lattice included); dark photon needs the total
ε(q,0) and ω_{p,c}; equal at clamped nuclei, differing by the ionic static polarisation (ε₀ vs ε_∞ for polar q → 0). (iii) **Conservative
step 1 − ε^{-1}(q,0) ≤ 1:** needs ε_ch(q,0) ≥ 1. **PROVEN at RPA+LFE for any insulator** (WP1 [E3]: 0 < (ε^{-1})_00(q,0) ≤ 1, all q, LFE
included) [D]; beyond RPA it needs 1 − f_HxcR⁰ > 0, true for Si, Ge (r_s ≈ 2 < 5.25) [E]; for arbitrary materials negative static ε at q ≠ 0
is not excluded (Dolgov–Kirzhnits–Maksimov), so there it remains [C]. (iv) **Tightening [E]:** for ω_th above the phonon band subtract the
GS dω/ω weight: ∫_{ω_th}^∞(dω/ω)L ≤ (π/2)[1 − ε_∞^{-1}(q)] + O(κ_BO⁴), strictly tighter for polar targets. (v) **L17′ [D]:** any operator with
a kinetic-only first moment obeys (9.6) with ω_p² → e²𝓜¹/q² and 1 − ε^{-1}(q,0) → −v_CR(q,0); e.g. the spin channel (4.6e), giving bounds for
𝒪₄-type couplings [E for usefulness]; for magnon targets these are loose unless restricted to the projected manifold (WP4 (1.3)).
**Status: DERIVED** at RPA+LFE for insulators; (iii) as stated.

**(2.9) ALP–photon absorption [D, k → 0, uniform B₀]** (cited in §2). Map κ_mix m_φ² → g_aγγB₀m_φ in the dark-photon result
−Im[m²Π^γ/(m² − Π^γ)]/m = m Im(−1/ε) (WP0v2-C6): Γ_abs = g_aγγ²B₀² Im[−1/ε_∥(m_φ)]/m_φ, ε_∥ along B₀. Agrees with 2305.05681 [ABS];
prefactors against its full text: open (O6).                                                                                          (2.9)

**(9.7) Pointer table.** "τ / chain" names the truncation that produces each entry; ✔ chain confirmed, ✎ corrected. "Source" gives arXiv ID
and equation of the source formula, read in full text by the owner return named in brackets (CONVENTIONS §12; quoted forms in those returns).

| # | τ / chain (URF) | source formula [owner, FT] | ✔/✎ |
|---|---|---|---|
| L0 | (3.3) single n_e row, Born, (9.1) | Γ = ∫d³q/(2π)³\|V\|²[2(q²/e²)Im(−1/ε(q,ω_q))]: 2101.08263 Eq. (1); KKL 2101.08275 Eqs. (4), (6), (13) [WP1] | DERIVED |
| L1 | S^{X0}_ee, n_B = 0, 𝒳 = IP, unscreened, (I), spin 2 | 1509.01598 Eqs. (17), (21): dR/dlnE_e = (ρ_χ/m_χ)N_cellσ̄_eα(m_e²/μ²)∫dlnq(E_e/q)ηF²\|f_crystal\|²; \|f_crys\|² = Ωq³S̄/(4παm_e²) [WP1] | ✔ (D1's 2πα ✎) |
| L2 | (5.4)/(5.5): ELF needs clamped nuclei or ω ≫ ω_max (O(κ_BO⁴)); 𝒳 = RPA or exact | 2101.08275 Eq. (6): S = (k²/2πα)(1 − e^{−βω})^{-1}Im[−1/ε_L] [WP1] | ✎ (condition) |
| L3 | multi-operator (3.3), 𝒳 = IP + screening of every a with R̃_ac ≠ 0 (n, j_L; j_T via LFE; s via f_xc^T; s–n mixing with SOC); on-shell transverse projection | 2105.02233 Eqs. (11), (36)–(42); 2210.14917 Eqs. (18), (23), (70)–(71); 2510.25835 Eqs. (5)–(6) [WP1] | ✎ |
| L4 | S^{GS}_κκ, S^{GS}_cc; adiabatic (O′_e)_{GS,GS} → Z*, ε_∞; harmonic, K = 1ph-coh; dark photon = (5.4) ≡ Born-charge form (Sherman–Morrison) | 1910.08092 Eqs. (92), (104)–(106); 1807.10291 Eqs. (29)–(32) [WP2; Eq. (32) = isotropic one-branch \|ℳ\|², WP2-v2] | ✔ |
| L5 | S^{GS}_κκ harmonic all orders, K = multi-inc; control n_ph + shell parameter (not x_coh) | 2205.02250 Eqs. (15), (23)–(24), (36); 2011.09477 Eqs. (7)–(12) [WP2] | ✎ (control) |
| L6 | S^{GS}_κκ at x_R → ∞, K = imp: mean exact (𝔨₁ = q²/2M), Gaussian width with the true ⟨p²⟩, skewness 𝔨₃^{GS} from the BO curvature, remainder in X | Helm: hep-ph/0608035 Eqs. (5), (9)–(11) [WP2] | ✎ (WP2-D4) |
| L7a | S^X_κκ, isolated atom, K = imp, σ_c ≪ 1, n_D = 1; boost mass m_A | 1707.07258 Eqs. (55), (57), (73), (86), (91)–(92) [WP3] | ✔ (m_A ✎) |
| L7b | S^X_κκ, K = imp, soft limit, long-range ionic field → ELF | 2011.09496 Eq. (6): dP/dω = 4α∫d³k/(2π)³Z_ion²\|v_N·k\|²Im[−1/ε]/(ω⁴k²) [WP3] | ✔ |
| L7c | S^X_κκ with GS-sector phonon final states, leading non-adiabatic, harmonic | 2210.06490 Eq. (3.8); 2505.08864 Eq. (21) [WP3] | ✔ |
| L7d | DM–N × virtual phonon × e–ph, incoherent: **n = 0 term X0, n ≥ 1 terms X+** | 2205.03395 Eqs. (3.1)–(3.4) (Σ_n T_n incl. T₀ = δ(E)) [WP3] | ✎ (v1 "X0, not X+") |
| L8 | S^{X+}_ee at n_g = 2 with (5.6)–(5.7), DC outside the window | this campaign: D1 eq. (4) with M → M̃, X2 (2.3) | ✎ (pair channel, LFE) |
| L9 | q → 0 of L8, pair channel at (Q, ω∓ω_Q) | 2302.08085 Eqs. (60)–(63); 1202.3454 Eq. (1): prefactor 8π²α/(Ωω²) confirmed [WP3] | ✎ |
| L9b | (3.5)–(3.6) at k ≈ 0; A′: Γ = κ_mix²m Im(−1/ε); ALP–e: tr J_e (= current only at SOC = 0); aγγ: (2.9); X+ part and T-transfer of σ₁ (WP3) | 1608.01994 Eqs. (2), (3), (6), (7), (10); 2106.12586 Eqs. (20)–(22) [WP3] | ✔ + caveats |
| L10 | jellium limit of WP1 RPA (Lindhard, Mermin) | 2101.08275 Eqs. (17)–(24) [WP1] | ✔ |
| L11 | plasmon = zero of ε in (5.4); no separate final state in RPA (§7.1) | 2003.12077 Eqs. (5), (7); 2002.06937 Eqs. (13)–(14) [WP1] | ✔ |
| L12 | X0 ⊕ X+ at n_g = 2, adiabatic (ω_Q/δ → 0), phonon energy dropped from δ: **ZG = deterministic one-shot quadrature of the Williams–Lax average** | 1604.02394 Eqs. (1), (3)–(6), (24); 1603.06965 Eqs. (157)–(160) [WP3] | ✎ (v1 "stochastic") |
| L13 | spin row of (2.2), magnetic reference (LSWT, 1/(2\|𝐒_j\|)), magnetic form factor F^{mag}_j | 1905.13744 Eqs. (5)–(12); 2009.13534 Eq. (38) [WP4] | ✔ |
| L14 | 𝒳 = BSE in R̃ | 2507.14345 Eqs. (1)–(2) [WP1] | ✔ |
| L15 | BCS reference (not a finite n_g order) + **conserving GRPA** (bare bubble violates (4.6)) | 2609.06423 Eqs. (6)–(9); 2101.08263 Eqs. (1), (3), (S.13)–(S.16); 1512.04533 Eqs. (11)–(14) [WP4] | ✎ (WP4-D3) |
| L16 | low-energy Dirac H + RPA (5.4) with the **remote-band background ε_bg inside the total ε** | 2101.08263 Eq. (4); 1708.08929 Eqs. (2.6), (3.7), (3.11); 1910.02091 Eqs. (2.5)/(2.7), (3.13)–(3.14) [WP4; κ² claim pending referee FT check] | ✎ (WP4-D5) |
| L17 | §9.2 | 2110.01587 Eqs. (1), (4); 2608.05282 Eqs. (1), (8), (9) [WP0, FT] | DERIVED |
| L18 | n_A = 1 on S^{GS}_κκ (three exact linear constraints on θ_A) | 2309.10839 Eqs. (9)–(10), (23)–(26) [WP2] | ✔ |
| L19 | (3.3) with full q-vector S; cubic: ℓ = 4 first; 2W_κ direction-dependent; **P,T-broken targets: nonreciprocal S, v-odd rate (4.3)** | 2607.06005 Eqs. (6), (10); 2411.03433 Eqs. (18)–(24) [WP1, WP2] | ✎ (WP4-D6) |
| L20 | WP5 first moment of (W3), GS seed with K = imp | 2001.06503 Eqs. (3)–(7); 2209.04503 Eq. (2) [WP5] | ✔ |
| L21 | WP5 cascade with Λ-seeding (7.3); R&K = photon-seed fit | 2004.10709 Eqs. (5)–(9) [WP5] | ✎ |
| L22 | BO surface + WP5 NR partition (stored energy ≠ E_d) | 1805.09942 Eqs. (1), (4); 2301.06592 Eq. (8) [WP5] | ✔ |
| L23 | second moment of the WP5 cascade | 2004.10709 Eqs. (3), (16); 2004.11499 [WP5] | ✔ |
| L24 | (3.4) + (I) + WP6 halo functional and (8.3) | 1509.01598 Eq. (17); 2311.04957 Eqs. (9)–(11), (13), (19)–(20) [WP6] | ✔ |

---
## 10. Contested corrections

**CC-1. CORRECTIONS §6 row "§7.2 weight (ε^{-1})_{G0} → general weight (1+Rv)_{0G}" (WP1-D6). Applied in modified form.**
*Claim contested:* that (7.2)'s (ε^{-1})_{G0} is valid only with R_{GG′} = R_{G′G} and must be replaced by (1 + Rv)_{0G} in GaAs.
*Derivation [D, RPA/TDDFT, any target].* Let f = v_C (or f_Hxc), R = R⁰ + R⁰fR = R⁰ + RfR⁰. Then R = R⁰(1 + fR) and R† = (1 + R†f)R⁰†, so
(1 + R†f)(R⁰ − R⁰†)(1 + fR) = (1 + R†f)R − R†(1 + fR) = R − R†. Likewise R = (1 + Rf)R⁰, R† = R⁰†(1 + fR†) give
(1 + Rf)(R⁰ − R⁰†)(1 + fR†) = R − R†. With S⁰_{GG′} = Σ_pair ρ_G*ρ_{G′}δ(…) ∝ the anti-Hermitian part of R⁰ (IP pairs), the 00 element gives
S = Σ_pair|Σ_G w_Gρ_cv(k,q+G)|²δ with either w^{out}_G = (1 + fR)_{G0} = δ + f(q+G)R_{G0} (retarded; (7.2)) or
w^{in}_G = (1 + fR†)_{G0} = [(1 + Rf)_{0G}]* (advanced). Both are exact in total for every target (WP0v2-C10a–c). The prompt final state
of (7.1) is the outgoing state: in linear response the causal (retarded) induced potential screens the external one,
V_tot(q+G) = (ε̃^{-1})_{G0}φ_ext (CONVENTIONS §3 sign, (3.2) order), and the total potential creates bare pairs; equivalently the
golden-rule amplitude to |f^{(−)}⟩ carries retarded propagators. Hence **(7.2) with retarded (ε̃^{-1})_{G0} in (3.2) order is the general
out-state form, valid without inversion**; (1 + Rf)_{0G} is the in-state labelling and must enter conjugated. They coincide pair by pair
wherever R(q,ω) is Hermitian (no open pairs at (q,ω), e.g. the PAER window, so X2 (2.2)/(5.7) is unaffected) (WP0v2-C10e).
*Consequence for WP1 [E2] as printed*, |Σ_G(1 + Rv)_{0G}ρ(q_r+G)|²: with TR + inversion (real symmetric R⁰, S⁰) it equals (7.2) pair by
pair (WP0v2-C10g); without inversion its total misses Im R_00 unless ρ is read as ρ* (WP0v2-C10f). This is flagged to WP1/WP3 (F1);
CONVENTIONS §13 item 16's instruction "use the WP0 (3.2) index order" is satisfied by (7.2). Totals (rates) are never affected; the
pair-resolved seeding of WP5 in GaAs is.

No other correction is contested.

---
## 11. Interface flags
| # | Owner | Quantity | Recorded form | Mismatch / action |
|---|---|---|---|---|
| F1 | WP1, WP3 | external LFE weight, pair-resolved | WP1 [E2] (1+Rv)_{0G}ρ; X2 (2.2) (ε̃^{-1})_{G0} | WP0-v2 (7.2) = retarded out-state form = X2's; WP1 [E2] needs ρ → ρ* (or the conjugated weight) in non-centrosymmetric targets (§10). **CLOSED**: accepted by WP1-v2 §1.3 and WP3-v2 §M7; only the referee check remains (OW0-7) |
| F2 | WP5 | screening classes in Theorem C (c) | "WP0's three-channel argument (5.5)" | cite WP0-v2 (5.5), four classes (X2); the argument (every line at p resummed once) is unchanged |
| F3 | WP5, WP3 | final-state labels | WP0 v1 plasmon label; v1 (7.3) | WP0-v2 (7.1) has no plasmon label in RPA and (7.3) = WP5 (W6); consistent |
| F4 | WP2, WP3 | third cumulant / mixed third moment | WP2 (5.2) 𝔨₃^{GS}/𝔨₃^X; WP0 (4.7); WP3 Migdal spectra | **CLOSED** at moment level: WP2-v2 (5.2′), WP3-v2 J8 (q → 0, consistent with the qualified (4.7)) |
| F5 | WP4 | Theorem D for gapless targets | WP4-D2 quasiparticle-number sectors | WP0-v2 states the scope only; replacement theorem is [C], owned by WP4 |
| F6 | WP2 | multiphonon S^{GS}_κκ and ρ^{ph}_κ feeding WP5 | WP2 (2.2), (3.6) | used as recorded in (7.3); GS rename done in WP2-v2 (**CLOSED**) |
| F7 | WP3 | (W.4c) thermal factor | S^{X+} = (2q²/e²)L^{PA} | (5.6) divides by (1 − e^{−βω}) at T > 0; immaterial at T ≪ E_g (CORRECTIONS §9) |
| F8 | WP3, WP5 | Fano term 𝔉 in GaAs | O4 (O4.7) [C] | size unknown; needed by d7 for any GaAs pair-resolved prediction outside the window |
| F9 | WP6 | library τ string | WP6 §7.3 `nT=130K` | use the §6.1 string (temperature in metadata) |
| F10 | NOTATION | carrier energies E_e, E_h | CORRECTIONS §0 (WP0 §7) | NOTATION v3 has no row for them while §K maps 1509.01598's E_e → ω; add a row "E_e, E_h: prompt carrier energies" |
| F11 | WP1 | static DFPT error | X2: O(ω_Q²/E_g²); D2/v1: O(ω_Q/E_g) | WP0-v2 (5.5) uses X2's; returns quoting the old order should update |

---
## 12. Open items handed on
- Closed since v1: O1 (X2 confirms (5.6c–d)); O2 for (4.9) (X1, WP3) and the L9 pair channel (X2, P = Q); O3 (WP1 §2, §5); O4 at physics
  rigour (O4 (iv′)/(iv″)); O5 at RPA+LFE (WP1 [E3]).
- O6: (2.9) and the (3.5)–(3.6) absorption prefactors against the full text of 2305.05681.
- OW0-7: referee check (R7) of §10, the in/out-state labelling of the external weight (F1 itself is closed).
- OW0-8: CLOSED (F4; WP2-v2 (5.2′), WP3-v2 J8). OW0-9: a Theorem D for gapless targets (F5).
- OW0-10: size of 𝔉 in GaAs and the Γ_Λ₀/δ map over (q,ω) in Si for the d11 edge shell (O4). OW0-11: the rigorous version (O4 §8).
- OW0-12: X2-N1…N4 (pair channel, δ_LF) and the Umklapp re-check of the Si window (SOTA R2).

---
## 13. Corrections applied (closing table)
| # | Correction (ID / source) | Where applied | How |
|---|---|---|---|
| 1 | Hyperfine factor and sign (WP4-D1; audit A18) | (1.2) | +(2/3)g_eμ_Bg_Iμ_N s·𝐈δ³ = +(1/3)…σ·𝐈δ³; derivation from −𝛍_e·B; WP0v2-C8 |
| 2 | SOC/Darwin give zero to f-sum; mass-velocity only (WP1-D2) | (1.2), (4.6′) | [E11] form with derivation; WP0v2-C4g,h |
| 3 | Ge core sizes (WP1-D3) | (1.2) | 0.055 (1s), ~10⁻³ (3d); WP0v2-C4i; Dirac-bilinear factorisation and no-pair projection added |
| 4 | Commutator [T, n] = q·j exactly (WP1-D1; audit A13) | (4.6), (4.8), (5.3) | extra (q²/2m)n removed; WP0v2-C4e,e′,f |
| 5 | Soft limit (4.9) incomplete; ℓ_Q N inside (WP3-1; CONVENTIONS §5, §13 items 5–6) | (4.8)(i)–(ii), (4.9) | replaced by X1 (X1) in CONVENTIONS order and sign; lab form; v1 difference stated; WP0v2-C12 |
| 6 | j_T screened via LFE (WP1-D4) | (5.3), L3 | stated with size and the transverse-photon estimate |
| 7 | Spins xc-renormalised by f_xc^T (WP1-D5) | (5.3), L3 | [E6] form; SOC mixing sizes |
| 8 | Z*/ε_∞ belongs to charge coupling (WP2-C1) | (5.3) nucleon bullet | external vertex A_κF^M_κ; Z*/ε_∞ only inside the TO → LO Dyson series |
| 9 | (5.6)–(5.7) D2-normalised truncation (WP3-2; NOTATION-APPLY D7) | (5.5)–(5.7′) | X2 (2.2)/(2.3) adopted with D1 normalisation; v1 form kept as (5.7′) truncation; WP0v2-C7 |
| 10 | Table 6.1: x_coh, K label, 2W (WP2-D1, D2, D3) | Table 6.1 | x_coh retired → n_ph + shell parameter; 2W_κ = q·B_κ·q; 1ph-inc regime; K labels |
| 11 | Table row "1/S, Δ/E_F" (WP4-D4) | Table 6.1 | SC and magnet parameter rows |
| 12 | (H2) scope for gapless targets (WP4-D2) | §6.2 | scope paragraph; replacement [C] (F5) |
| 13 | Theorem D (i) per-sector PSD (O4 §9; CONVENTIONS §13 item 20) | §6.2 (i) | only in window or bins ≳ δ; Z may exceed 1; WP0v2-C13a |
| 14 | Theorem D (iv) [C] → O4 (iv′)/(iv″), DC, d1–d11 | §6.2 (iv), (6.3) | DC formulas, (a)–(d) results, T3a/b, edge shell, rigour gaps |
| 15 | Boost mass m_A vs M (WP3-5; CONVENTIONS §13 item 22) | §6.2 (ii), L7a | drag-mass tensor δM_κ; atom: M + δM = m_A |
| 16 | S_eκ X+ "dark photon only"; X-sector ω_e moment (WP3-4) | dictionary, (4.6c) | any 𝔇 with c_ec_κ ≠ 0; J7 split and sign |
| 17 | O4 zeroth-moment scope (CORRECTIONS §13; coordinator; CONVENTIONS §13 item 17) | §6.2 (iii) | Z + fp = 1 per pair for the Fan part only; no global n_e rule |
| 18 | Plasmon label double count (WP5-3; CONVENTIONS §13 item 21) | (7.1), L11 | Λ = cvk only within RPA |
| 19 | Multi-operator seeding weight (WP5-2) | (7.3) | tr[𝔇S(Λ)]/tr[𝔇S] |
| 20 | q integrated before seeding (WP5-1) | (7.3) | WP5 (W6) with q integral and 𝔇 trace inside the Λ sum |
| 21 | R&K is a photon-seed fit (WP5-4) | (7.3), L21 | stated; θ_seed nuisance |
| 22 | External weight (1+Rv)_{0G} (WP1-D6; CONVENTIONS §13 item 16) | (7.2), §10 | **contested in part**: retarded out-state form derived as general; WP0v2-C10 |
| 23 | Additive Gaussian violates positivity (WP6-W2) | (8.1) | M/A/E/Δ types; WP0v2-C14c |
| 24 | f-sum constraint 2π → π, over ℝ (WP6-W1; audit A12; CONVENTIONS §13 item 12) | (4.6), (8.2) | ∫_ℝωS = π𝓃_eq²/m_e; WP0v2-C9 |
| 25 | f-sum constraint vacuous for conserving truncations (WP6-W3) | (8.2) | stated; informative cases listed |
| 26 | Envelope vs profile (WP6-W4; CONVENTIONS §13 item 13) | (8.3) | three reported objects; orders O(δ²)/O(δ); WP0v2-C14a,b |
| 27 | (9.1) hypothesis: angle-averaged S (WP6-W5) | (9.1) | hypothesis (I) |
| 28 | L7d sector (WP3-3; CONVENTIONS §13 item 15) | dictionary, L7d | n = 0 → X0, n ≥ 1 → X+ |
| 29 | L12 ZG deterministic (WP3-6; CONVENTIONS §13 item 14) | L12 | deterministic one-shot quadrature of Williams–Lax |
| 30 | L15 GRPA, L16 ε_bg (WP4-D3, D5) | L15, L16 | conserving GRPA; ε_bg inside the total ε |
| 31 | P,T-broken nonreciprocity (WP4-D6) | (4.3), L19, (9.1)(δ) | converse flagged with WP4 [3.1]–[3.3] |
| 32 | L6 pointer incomplete (WP2-D4; not in CORRECTIONS) | L6 | mean exact, true ⟨p²⟩ width, BO skewness 𝔨₃^{GS} |
| 33 | Static DFPT error order (X2 §2 item 2) | (5.5) | O(ω_Q²/E_g²) replaces O(ω_Q/E_g) |
| 34 | Four Coulomb classes incl. ionic, external LFE (X2 §3; R1 "two channels" withdrawn, CONVENTIONS §7) | (5.5) | class list and topological proof |
| 35 | τ amendments: 𝒳, K labels, metadata T/ref/scr/conv (CONVENTIONS §11; NOTATION-APPLY D9) | §6.1, (1.2) | adopted with library string |
| 36 | §10 symbols superseded by NOTATION v3 (CORRECTIONS §6 last row and §0) | throughout | G → GS, X → 𝒳, ψ → s, a/b → α/β, v_k → v_C, τ_e → 𝒯_e, M¹ → 𝓜¹, ε_e/ε_h → E_e/E_h, c_s → c_ν, Ξ_n → Ξ^n, v_n → v^g_n, P_n → p_nn, O_i → 𝒪_i, F_i → F_DM,i, n_s → 𝓃_s, κ → κ_mix, Γ(v) → Γ_χ, R (rate) → ℛ, Z → 𝒵, J_κ → 𝒥_κ, τ_ph,g → t_ph,g, Δ_k → Δ^τ_k, ρ_m → ρ_M, g(q) → 𝐠(q), S_χ → 𝐒_χ |
| 37 | L17 (iii) status (WP1 [E3] answers O5) | (9.2)(iii) | DERIVED at RPA+LFE for insulators |
| 38 | Relativistic-core matching (WP1 §5 answers O3) | (1.2) | factorisation exact with Dirac bilinears; O(⟨v_e²⟩) truncation |
| 39 | AUDIT A2: 𝔨₃ naming, q → 0 qualifier, stale flags | (4.7), F1, F4, F6, OW0-7, OW0-8 | qualifier qa ≪ 1 added (ℓ = 2 average at finite q); cite WP2-v2 (5.2′), WP3-v2 J8; F1, F4, F6, OW0-8 closed; OW0-7 narrowed to the referee check |
| 40 | AUDIT A3: L4 source equations | (9.7) L4 | 1807.10291 Eqs. (29)–(32) |
| 41 | AUDIT A4: bare c and V for potential energy | (1.2), (4.8)(i), §6.2(ii), (8.3) | 2.71 written explicitly; V_pot, V_eN for potential energies (V = crystal volume) |
| 42 | AUDIT A5: O6 cross-reference | §12 | "(2.9) and the (3.5)–(3.6) absorption prefactors" |
| 43 | NOTATION v4 renames (CORRECTIONS §17) | (8.1), §6.2 (ii), §15 | a_k → a^A_k (A-type amplitude); adiabatic energies E_n, E_a, E₀ → E^ad_n, E^ad_a, E^ad_0; 2.71 and V_pot, V_eN already in place (#41); ℒ, π_k, s_{ex,i}, b_{ex,i} now have NOTATION rows; §15 updated to v4. Notational only |

**Count:** 42 corrections applied (38 owed at R6 + 4 AUDIT fixes A2–A5; #22 applied in modified form and argued in §10). Contested: 1 (partial, #22). Row 43 (NOTATION v4 renames) is notational and outside this count.

---
## 14. Literature (arXiv IDs as verified in v1 and in the owner returns)
Read in full text for WP0 (v1): 2009.13534 (Table III; Eqs. (13), (15)–(27), (38)), 2105.02233, 2106.12586 (Table I; Eqs. (18)–(22)),
2110.01587 (Eqs. (1)–(4), (C1)), 2608.05282 (Eqs. (1)–(9)). Abstract/title: 1203.3542, 2305.05681, math-ph/0201055, 2505.08864 (FT via WP3).
Source equations in §9.7 are those read in full text by the named owner return (WP1–WP6); not re-read here.

---
## 15. Symbols introduced/used
All symbols follow NOTATION v4 and CONVENTIONS; **no deviations** (v4 renames: CORRECTIONS §17, closing-table row 43). Used as defined there: q, ω, ω_q, Δ_χ, v, v_χ, v^⊥, v_s, v_T, v_∥, v_min,
𝒪_i, c_i^{(s)}, 𝒱_a^{s′s}, 𝔇, Ṽ, σ̄_e, F_DM, F_DM,i, 𝐒_χ, j_χ, κ_mix, g_aee, g_aγγ, B₀, φ, a^φ_k, k_φ, Γ_χ, Γ_abs, Γ_net, ℛ; s, z_s, n_s(q), N_s,
𝓃_s, ρ_c, ρ_M, 𝐠, O_a, Γ (rows {0,b,a,ab}), j_e^α, s_e^α, J_e^{αβ}, 𝒯_e, T_e, ⟨T⟩, 𝐈_I, 𝒥_κ, h^I_κ, F^M_κ, F^Σ_κ, I_κ^α, j_κ^α, J_κ^{αβ},
𝐋_s, g_e, g_I, μ_B, μ_N, 𝛍_e, H, H_C, H_rel, H_hf, H_ext, 𝒵, p_i, E_i, E_f; S, S_ab, S̄, R, R̃, R⁰, ε, ε̃, ε_e, ε_mac, ε_∞, ε₀, ε_L, ε_bg,
ε_∥ (component of ε), v_C, f_xc, f_xc^T, f_Hxc, Π^γ_T, L, L_ch, K_n^{(ch)}, 𝓜¹, 𝓜³, 𝓜₁^{SB}, ω_p, ω_{p,e}, ω_{p,c}, Ω_{p,ion}, Z*_κ, 𝓕_κ, ρ̄_e,
U_κ, δM_κ, E^{Mig}_1, P_Mig; ρ_mn, ρ̃_mn, ρ^{ren}, M^{(2)}, M̃, W^{scr}, 𝔗_G, P, ω_f, ℓ_Q, ê, Q̂, c_ν, D^n, Ξ^n, v^g_n, p_nn, 𝔄, Q_min,
g_mnν, b_{Qν}, n_{Qν}, ω_{Qν}, Φ^{(n)}, B_κ, 2W_κ, n_ph, z_ΔR, j₀, c̄_ΔR, x_R, κ_BO, η_ep, η_anh, η_xc, t_ph, t_g, σ_c, ξ_D, τ, 𝒳, K, 𝔐,
θ_k, Δ^τ_k, r^M_k, a^A_k, σ_E, θ^det_ex, ℒ, π_k, s_{ex,i}, b_{ex,i}, θ_E; GS, X0, X+, X, 𝒫₀, 𝒫_⊥, U_n, Δ_ad, Λ, P_Λ, Λ₀, Λ₊, Ẽ_Λ₀, Z_Λ₀, Γ_Λ₀, δω, fp, PV, DC, a^{off}, Υ_Λ₀,
𝔉_{Λ₀,ν}, 𝒞_adm(ℓ_win), w₀, b_λ, δ, δ₀, E_min, E_min^{ren}; N_eh, 𝐍, ℋ, E_st, N_FP, E_esc, P_casc, ρ^{ph}_κ, E_R, ω_e, ω_ph; ρ_χ, f_χ, η, 𝒢,
𝐛_NR, Δ_BCS, Δ_D, E_F, k_F, v_F, ℓ_mfp, 𝐒_j, F^{mag}_j, E_x^b, ρ_T, Ω, N, V, κ, M_κ, M_cell, Z_κ, A_κ, m_A.
Introduced here (new objects, no collision; proposed NOTATION rows): **y_φ** (absorbed-boson coupling to a target operator, (3.3));
**𝒟^γ_{μν}** (in-medium photon propagator, (3.6)); **Φ₀(r;R), Φ_n(R)** (adiabatic electronic states of Theorem D, energies E^ad_n(R), NOTATION v4 §M; force constants always carry
a superscript, Φ^{(n)}); **P_tot, M_tot** (total momentum, total mass, (4.8)); **𝓃_e(R_κ)** (electron contact density, (4.7));
**δ_rel** (relativistic f-sum shift, WP1's symbol, (1.2)); **V_pot, V_pot^{scf}, V_eN** (potential energies, as WP2-v2; NOTATION v4 §M row V_pot, V_ee, V_eN, V_NN); the χ²₁ 90% quantile is written as the number 2.71, never bare c (NOTATION v4 §M); **E_e, E_h** (carrier energies, per CORRECTIONS §0; NOTATION row missing, F10).
Labels: WP0v2-Cn (checks), CC-1 (contested), F1–F11 (flags), OW0-n (open items).
