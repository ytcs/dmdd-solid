# R4 / WP0: architecture of the Unified Response Framework (URF)

Isolated theory agent. Read scope as in the brief. Theory only: the identity checks are in
`code/WP0/checks.py` (14 checks, all PASS, < 5 s). Literature: arXiv IDs verified against the arXiv API
(§11). Full text was read for 2009.13534, 2105.02233, 2106.12586, 2110.01587 and 2608.05282.
Tags: **[D]** DERIVED (hypotheses stated), **[E]** ESTIMATED, **[C]** CONJECTURED. Later WPs cite these equation
numbers (s.n). Units follow NOTATION: ħ = c = k_B = 1, e² = 4πα, v_k ≡ e²/k². **The retarded response is written R, not χ**, because
χ is the DM (NOTATION v2, §10).

---
## 1. Hamiltonian and degrees of freedom

**(1.1) [D]** Electrons i = 1..N_e (r_i, p_i, spin s_i = σ_i/2). Nuclei I with species κ(I), charge Z_κ, mass M_κ, (R_I, P_I),
nuclear spin 𝐈_I. Densities per species s ∈ {e, κ}: n_e(k) = Σ_i e^{ik·r_i} and n_κ(k) = Σ_{I∈κ} e^{ik·R_I}. Charge numbers
z_e = −1, z_κ = Z_κ. Charge density ρ_c(k) = e Σ_s z_s n_s(k). Then

  H = Σ_i p_i²/2m_e + Σ_I P_I²/2M_I + (1/2V) Σ_{k≠0} v_k [ρ_c(k)†ρ_c(k)/e² − Σ_s z_s² N_s] + H_rel + H_hf + H_ext ≡ H_C + H_rel + H_hf + H_ext.

H_C is exact non-relativistic Coulomb (point nuclei; finite nuclear size enters at q·R_nuc only through F_κ, §2). k = 0 is
removed by neutrality. Every e–N and N–N interaction is Coulomb, so "phonons", "g" and "screening" are all *derived*
objects (§5, §6).

**(1.2) Options.** Each is a switch, and later WPs state which ones they use.
- *SOC / Breit–Pauli [D].* H_rel = Σ_i[−p_i⁴/8m_e³ + (1/8m_e²)∇_i²V + (1/4m_e²) σ_i·(∇_iV × p_i)] + two-body SOO/SSO.
  These terms are not multiplicative in r_i, so [H_rel, n_e(q)] ≠ 0. The f-sum (4.6) then picks up a correction
  δ_rel ~ ⟨T⟩/m_e (≈ (Zα)² for core shells) [E]. Pointer: WP1 (G7).
- *Relativistic cores (Dirac–Coulomb / ZORA / scalar-relativistic) [C].* The NR-EFT operators of §2 assume Pauli electrons. For
  4-component cores the density vertex becomes ψ†e^{iq·r}ψ, with large and small components, and the velocity operator
  becomes cα. The operator corrections are O((Zα)²) ≈ 0.27 for Ge 1s and ≈ 0.05 for 3d. WP1 must re-derive the matching (§2) for
  core shells and not just swap wavefunctions.
- *Hyperfine [D].* H_hf = Σ_{i,I} (2/3) g_eμ_B g_Iμ_N σ_i·𝐈_I δ³(r_i−R_I) (Fermi contact, HL units with μ₀ = 1; WP4 fixes the sign) + orbital and dipolar
  terms + nuclear quadrupole. This is the only coupling of 𝐈_I to the rest of the system.
- *External fields [D].* p_i → p_i + eA₀(r_i), giving a paramagnetic current coupling plus the diamagnetic term (e²/2m_e)A₀². Zeeman
  term g μ_B B₀·s_i. B₀ is needed for g_aγγ (2.9).
- *Magnetic order / superconductivity [D].* These do not change H. They change the **reference state**: a broken-symmetry
  mean-field state around which (3.1) is expanded. This brings in a new small parameter, 1/S for spin waves (L13) or the
  Ginzburg/Eliashberg parameter (L15). Neither is a finite order of the e–ph expansion (§9).

---
## 2. DM interaction basis

**(2.1) Kinematics [D].** The DM goes p → p − q with spin s → s′, and optionally changes state χ₁ → χ₂ with Δ_χ = m_{χ₂} − m_{χ₁}
(exothermic if Δ_χ < 0). Energy given to the target:

  ω_q = q·v − q²/2m_χ − Δ_χ.                                                                                         (2.1)

Galilean-invariant relative velocity, in the decomposition of 2009.13534 Eq. (13) [FT]:
v^⊥ = v_χ − v_ψ, with v_χ ≡ v − q/2m_χ a DM-side c-number and v_ψ ≡ (k+k′)/2m_ψ a target-side operator.

**(2.2) Target operator basis [D].** For each species ψ ∈ {e, κ}, every NR-EFT operator is at most linear in S_ψ and in v_ψ
(1203.3542; 2009.13534 Table III [FT]). The complete target basis per species is therefore 16 operators, labelled a = (ψ, Γ):

| Γ | operator O_{ψΓ}(q) | electrons (sum over i) | nuclei of species κ (sum over I∈κ) |
|---|---|---|---|
| 0 | number density | n_e(q) = Σ e^{iq·r_i} | n_κ^F(q) = F^M_κ(q) Σ e^{iq·R_I} |
| b | spin density | s_e^b(q) = Σ e^{iq·r_i} s_i^b | I_κ^b(q) = F^Σ_κ(q) Σ e^{iq·R_I} 𝐈_I^b ⟨S_N⟩_κ/J_κ |
| a | velocity (paramagnetic current) | j_e^a(q) = Σ ½{p_i^a/m_e, e^{iq·r_i}} | j_κ^a(q) = F^M_κ Σ ½{P_I^a/M_κ, e^{iq·R_I}} |
| ab | spin-current | J_e^{ab}(q) = Σ ½{p_i^a/m_e, e^{iq·r_i}} s_i^b | J_κ^{ab} = F^Σ_κ Σ ½{P_I^a/M_κ, e^{iq·R_I}} 𝐈_I^b⟨S_N⟩/J |

The nuclear rows use x_α = R_I + y_α, e^{iq·x_α} = e^{iq·R_I}e^{iq·y_α}, and the fact that the internal nuclear state cannot change at
ω ≪ keV. The internal factors therefore collapse to ground-state form factors: F^M_κ(q) → f_pZ_κ + f_n(A_κ−Z_κ) at q → 0 (Helm),
and F^Σ for spin. The composite internal responses (Δ, Φ″: the orbital L and L⊗S of 2009.13534 Eq. (27)) are higher order in
q·y and can be added as extra Γ.

**(2.3) Matching [D].** Write each Fitzpatrick operator O_i^{(ψ)} with v^⊥ = v_χ − v_ψ, and map 1, S_ψ, v_ψ, S_ψ⊗v_ψ to the four
rows of (2.2). For example:
O₁ → n; O₄ = S_χ·S_ψ → S_χ^b s^b; O₇ = S_ψ·v^⊥ → v_χ^b s^b − δ_ab J^{ab}; O₈ = S_χ·v^⊥ → S_χ·v_χ n − S_χ^a j^a;
O₃ = iS_ψ·(q/m_ψ × v^⊥) → i ε_{bcd}(q^c/m_ψ)(v_χ^d s^b − J^{db}). The "a/b" split of 2009.13534 is exactly this decomposition.
The interaction Hamiltonian is then

  ⟨p−q, s′| H_int |p, s⟩ = V^{-1} Σ_a 𝒱_a^{s′s}(q, v_χ) O_a(q),   𝒱_a = (4m_χm_ψ)^{-1} Σ_i c_i^{(ψ)} F_i(q) A_i^{a}(q, v_χ, S_χ),          (2.2)

where A_i^a is read off from the expansion and F_i(q) is the mediator form factor (F_DM for light mediators). Normalisation anchor:
𝒱_{n_e} = c₁/(4m_χm_e), so σ̄_e = μ_χe²|c₁|²/(16π m_χ²m_e²), and **|𝒱_{n_e}|² = πσ̄_e F_DM²/μ_χe² = |Ṽ|² of D1/D2** (D1 N5, D2 §0).

**(2.4) DM tensor [D].** 𝔇_ab(q,v) ≡ (2j_χ+1)^{-1} Σ_{ss′} 𝒱_a^{s′s*} 𝒱_b^{s′s}. This is Hermitian and positive semidefinite
(a sum of rank-one projectors).                                                                                              (2.3)

**(2.5) Absorption couplings [D], for a DM field φ with ω ≃ m_φ and |k| ≃ m_φ v ~ 10⁻³ω:**
- *Dark photon:* κ e A′_μ J^μ_em, with J^μ_em = (ρ_c, J_c) and J_c = e Σ_s z_s (j_s + diamagnetic) (2.6–2.7).
- *ALP–electron:* L_int from 2106.12586 Eq. (18) [FT]. The LO term is −(g_aee/2m_e)(∇a)·σ, so the target operator is s_e(k), which is
  O(k)-suppressed. The NLO term is ∝ (g_aee/4m_e²)(∂_t a) ψ†σ·∇↔ψ, so the target operator is 2 Tr J_e(k) ≡ Σ½{σ_i·p_i/m_e, e^{ik·r_i}}. Hence
  ALP absorption probes the **trace of the spin-current** row of (2.2). That equals the current response only when SOC = 0 (L9b).
- *ALP–photon in B₀:* −g_aγγ a E·B₀ acts as a source current J_a = −g_aγγ B₀ ∂_t a ∥ B₀, so it behaves as a dark photon with
  κ m² → g_aγγ B₀ m_a (2.9).
- *Scalar:* gφψ̄ψ. At LO the target operator is n_e(k) (and n_κ for a nucleon coupling). Charge conservation suppresses this at
  k → 0. At NLO it is (1/8m_e²)ψ†∇↔²ψ (2106.12586 Table I [FT]), which is a new target operator τ_e(k) (kinetic-energy density).
  It must be added to the basis for absorption: a = (e, τ).

---
## 3. Master rate formulae

**(3.1) Response matrix [D] (definition from the brief; fixed ordering).** With p_i = e^{−βE_i}/Z:

  S_ab(q,ω) = (2π/V) Σ_{i,f} p_i ⟨i|O_a(q)†|f⟩⟨f|O_b(q)|i⟩ δ(ω − E_f + E_i).                                                (3.1)

  R_ab(q,ω) = −(i/V)∫₀^∞dt e^{iωt}⟨[O_a(q,t)†, O_b(q,0)]⟩ = (1/V)Σ_{if}(p_i − p_f)⟨i|O_a†|f⟩⟨f|O_b|i⟩/(ω − E_f + E_i + i0).          (3.2)

**(3.2) Scattering [D].** Hypotheses: first Born approximation in H_int; DM plane waves normalised in V; target initially in the
Gibbs state; DM spin unpolarised. The golden rule gives, per DM particle,

  Γ(v) = ∫ d³q/(2π)³ Σ_{ab} 𝔇_ab(q,v) S_ab(q, ω_q),                                                                          (3.3)

  dR/dω = (ρ_χ/m_χρ_T) ∫d³v f_χ(v) ∫ d³q/(2π)³ Σ_ab 𝔇_ab S_ab(q,ω) δ(ω − ω_q).                                                (3.4)

Bookkeeping: 2πΣ_{p′}|V^{-1}Σ𝒱O|²δ = 2π V∫d³q/(2π)³ V^{-2}(…) = ∫d³q/(2π)³ (2π/V)(…). **Convention check against D1/D2:** for a
single density operator, (3.1) is D2's S, 𝔇 = |Ṽ|², and (3.3) is D1 eq. (3) / D2 §0. At T > 0, (3.3) automatically contains
ω_q < 0 (the target gives energy to the DM), weighted through (4.3).

**(3.3) Absorption [D].** Quantise φ = Σ_k (2ωV)^{-1/2}(a_k ε e^{ik·x} + h.c.), with H_int = g ∫d³x φ(x) O(x) (O carries any
polarisation index). Golden rule, net of stimulated emission:

  Γ_abs = (g²/2ω) S_OO(k, ω) ,   Γ_net = Γ_abs − Γ_emit = −(g²/ω) Im R_OO(k, ω),   ω = m_φ (+ k²/2m_φ),                            (3.5)

  R_OO = full (Coulomb- and photon-improper) response = R̃_OO + R̃_{Oμ} 𝒟^{μν}(k,ω) R̃_{νO},                                        (3.6)

where R̃ is irreducible with respect to one photon line and 𝒟 is the in-medium photon propagator (Coulomb part v_k/ε_L, transverse part
1/(ω² − k² − Π_T)). With g²R̃_OO = Π_φφ and gR̃_{Oμ} = Π_{φA}, (3.6) is exactly 2106.12586 Eqs. (20)–(21) [FT]. Rate per unit
mass: R = ρ_φ Γ_net/(ρ_T m_φ). The DM-to-target operator maps for each coupling class are in (2.5).

---
## 4. Exact relations at master level

Hypotheses for all of §4: H in (1.1), the Gibbs state, and operators as in (2.2). Extra hypotheses are noted line by line.

**(4.1) Fluctuation–dissipation [D]** (check C3):
  (1 − e^{−βω}) S_ab(q,ω) = i[R_ab(q,ω) − R_ba(q,ω)^*];   diagonal: S_aa = −2 Im R_aa/(1 − e^{−βω}).                     (4.1)
**(4.2) Kramers–Kronig / spectral representation [D]:**
  R_ab(q,ω) = R_ab^∞ + ∫(dω′/2π)(1 − e^{−βω′})S_ab(q,ω′)/(ω − ω′ + i0).                                                     (4.2)
R^∞ = 0 for densities and spins. For currents, R^∞_{j^aj^b} = +δ_ab n_ψ/m_ψ comes from the diamagnetic contact term, and it is needed for gauge
invariance (R_{jj}^L(q,0) + n/m → 0).
**(4.3) Detailed balance [D]:** S_ab[O](q,−ω) = e^{−βω} S_ba[O†](q,ω), where S[O†] is built from O_a → O_a†. For densities,
O(q)† = O(−q), so S_ab(−q,−ω) = e^{−βω}S_ba(q,ω). With inversion or time-reversal symmetry, S(q,−ω) = e^{−βω}S(q,ω).
**(4.4) Positivity [D]** (check C3b): for every complex vector c, Σ c_a^*c_b S_ab = (2π/V)Σp_i|⟨f|Σc_bO_b|i⟩|²δ ≥ 0. So S(q,ω) is
Hermitian PSD at each (q,ω), and Γ = ∫tr(𝔇S) ≥ 0. Corollaries:
  |S_ab|² ≤ S_aa S_bb (e.g. |S_eκ| ≤ √(S_ee S_κκ)),   Γ ≤ ∫d³q/(2π)³ λ_max(𝔇) tr S.                                           (4.4)
**(4.5) First-moment matrix [D].** Using stationarity of the Gibbs state:

  M¹_ab(q) ≡ ∫dω/2π ω[S_ab[O](q,ω) + S_ab[O†](q,ω)] = V^{-1}⟨[O_a†,[H,O_b]]⟩.                                                (4.5)

**(4.6) f-sum rules, per species and mixed [D]** (checks C4a–c). Extra hypothesis (L): every term of H other than the kinetic
energies is multiplicative in all coordinates. This holds for H_C, H_hf contact and H_ext Zeeman. It fails for H_SO, the mass-velocity
term and non-local pseudopotentials. Under (L), [H,n_s(q)] = q·j_s(q) + (q²/2m_s) n_s(q) involves only species-s momenta, so

  M¹_{ss′} = δ_{ss′} q² n_s/m_s   (n_s = N_s/V),   s,s′ ∈ {e, κ}.                                                             (4.6)

Consequences:
- (a) M¹_ee = n_e q²/m_e holds **at every order in g and BO, at any T, with the nuclei dynamic**. It is D2 §3 generalised. All
  electrons count, cores included.
- (b) M¹_κκ = n_κ q²/M_κ is the nuclear f-sum (×|F^M_κ|² with form factors).
- (c) **Mixed sum rule: M¹_{eκ} = 0.** The first moment of the e–N cross-response vanishes identically. Re S_eκ must change sign
  in ω, so a Migdal or e–N interference spectrum with a single sign is wrong.
- (d) Charge channel: M¹_cc = q² Σ_s z_s²e² n_s/m_s ≡ q² ω_{p,c}², where ω_{p,c}² = ω_{p,e}²(1 + Σ_κ Z_κ²n_κm_e/(n_eM_κ)). The nuclear
  term is a ~10⁻⁴ correction.
- (e) Spin, with SU(2) invariance (H_SO = 0 and B₀ ∥ z for the z component): M¹_{s^zs^z} = n_e q²/(4m_e).
With (L) violated: M¹_ee = n_eq²/m_e + V^{-1}⟨[n_e†,[H_nl,n_e]]⟩. For H_SO this is O(q²⟨∇V⟩/(m_e³)) [E]. Non-local PPs give the
"nonlocal f-sum" owed in SOTA (R2).

**(4.7) Third-moment mixed sum rule [D]** (check C4d, under (L)):

  M³_{eκ}(q) ≡ V^{-1}⟨[[n_e†,H],[H,[H,n_κ]]]⟩ = −(1/(V m_e M_κ)) ⟨Σ_{i, I∈κ} e^{iq·(R_I−r_i)} (q·∇)² v_{eN}(r_i − R_I)⟩.               (4.7)

For Coulomb v_eN and cubic site symmetry, ⟨(q·∇)²v⟩ → (q²/3)∇²v = (q²/3)Z_κe²δ³. This gives M³_eκ = −q²Z_κe²n_κρ_e(R_κ)/(3m_eM_κ), where
ρ_e(R_κ) is the electron contact density at the nucleus. **This is a sum rule for Migdal-type mixed spectra: their ω³ moment is fixed by
contact densities.** New, not found in the literature searched [E for novelty].

**(4.8) Ward identities for rigid translation [D].** P_tot = Σp_i + ΣP_I commutes with H_C (and with H_rel and H_hf). Mass density
ρ_m(q) = Σ_s m_s n_s(q) obeys [H, ρ_m(q)] = q·g(q), where g is the momentum density and g(0) = P_tot. For any B and ω ≠ 0:

  Σ_s m_s S_{sB}(q,ω) = (q/ω)·S_{gB}(q,ω) = O(q²)  as q → 0,                                                                  (4.8)

whereas each term is O(q). Two corollaries:
- *(i) Acoustic sum rule.* Rigid nuclear displacement u_κ = u ∀κ with adiabatic electrons gives Σ_κ ∂_{u_κ}V_scf = −∇V_scf. In
  DFPT form: Σ_κ Φ_{κα,κ′β}(0) = 0, Σ_κ Z*_κ = 0, and g^{ac}_{mn}(k,Q→0) ∝ ⟨m|−û·∇V|n⟩ (D1 §6.2, D2 C7).
- *(ii) The Q = 0 acoustic "phonon" is the centre-of-mass mode.* H = P_tot²/2M_tot + H_rel exactly, so its creation amplitude by
  any O(q) is i u·q O. **This fixes only the strictly Q = 0 component.** At small Q ≠ 0 the acoustic mode is a strain wave. Its
  intraband coupling g_nn^{ac} → i ℓ_Q Q(ê·Ξ_n(Q̂)·Q̂), where Ξ_n is the deformation-potential tensor, and with the intraband
  denominator ±(Q̂·v_n ∓ c_s)Q the limit is

  M^{ac}_{cv}(Q→0) = i ℓ_Q [ê·q + ê·Ξ_c·Q̂/(Q̂·v_c ± c_s) − ê·Ξ_v·Q̂/(Q̂·v_v ± c_s)] ρ_cv(k,q),   ℓ_Q = (2M_cellω_Q N)^{-1/2}   [C].   (4.9)

  This is direction-dependent and non-uniform (the Q → 0 and ω_Q → 0 limits do not commute). It agrees in structure with the R2 referees
  (SOTA C7 FALLS). The replacement for C7 is "(4.9), with Ξ from the same DFPT run". Sign conventions to be fixed by WP3.

---
## 5. Screening from first principles

**(5.1) Definition [D].** Restrict v to the external channel, {q+G}. R̃ is the response irreducible with respect to one Coulomb
line of that channel, in the super-space (a; G). This is exact: R̃ is the response to the total (external + Hartree) potential of the
channel. Coulomb lines at all other momenta (phonon Q, pair q+Q, …) stay inside R̃. Since H_C couples only through ρ_c,

  R = R̃ + R̃ Zᵀ v Z R,   (Z)_{G; sG′} = z_s δ_{GG′},   v = diag(v_{q+G}).                                                       (5.1)

**(5.2) General screened formula [D]** (checks C1a, C2). Let R̃_{ac} ≡ Σ_s R̃_{a s} z_s (the proper cross-response with charge) and

  ε_{GG′}(q,ω) ≡ δ_{GG′} − v_{q+G} R̃_{cc,GG′}(q,ω)   (the *total* longitudinal dielectric matrix: electrons + nuclei, LFE included).    (5.2)

Then, **for arbitrary operators a, b** (density, spin, current, nuclear):

  R_ab = R̃_ab + R̃_{a c} ε^{-1} v R̃_{c b}   (matrices in G; the DM vertex sits at G = 0).                                     (5.3)

Rank-one case (no LFE): R_ab = R̃_ab + v R̃_{ac}R̃_{cb}/ε. In species space this is Sherman–Morrison in the e/κ/charge basis.

**(5.3) Dependence on the coupling [D].** Let the DM couple to O_c ≡ Σ_s c_s n_s, i.e. a coupling vector |c⟩ in species space.
- *Total charge (dark photon), |c⟩ ∝ |z⟩:* R_zz = v^{-1}[(ε^{-1})_{00} − 1], so
  S_zz = (2q²/e²) Im[−(ε^{-1})_{00}]/(1−e^{−βω}) with the **total** ε. This is the ELF form (check C1b).                                         (5.4)
- *Electron density only, |c⟩ = |e⟩:* use the exact identity |e⟩ = −|z⟩ + Σ_κ Z_κ|κ⟩. Then

  R_ee = R_zz − Σ_κ Z_κ(R_{zκ} + R_{κz}) + Σ_{κκ′}Z_κZ_{κ′}R_{κκ′}.                                                              (5.5)

  The ELF form S_ee = (2q²/e²)L holds **iff the nuclear terms vanish**. That happens (i) exactly at clamped nuclei
  (R̃_{eκ} = R̃_{κκ} = 0; check C1c), or (ii) at electronic ω ≫ ω_max, up to O(κ_BO⁴) (nuclear spectral weight there is
  ∝ m_e/M). In general, define ε_e^{-1} ≡ 1 + v R_ee (D1 §3). Then S_ee = (2q²/e²)Im[−ε_e^{-1}] exactly, but ε_e ≠ ε.
- *Nucleon number, |c⟩ = Σ_κ A_κF^M_κ|κ⟩:* R_NN = R̃_NN + R̃_{Nc}ε^{-1}vR̃_{cN}. The second term is the electronic plus ionic
  screening of the DM–nucleus vertex. In BO language (§6) it produces the Z*/ε_∞ (Fröhlich) vertex for LO phonons, and the
  Bohm–Staver softening of the bare ion plasma pole into acoustic phonons (ω² = Ω_{p,ion}²/ε_e(q,0)) [D, two-component limit].
- *Non-density operators:* (5.3) screens a only through R̃_{ac}. Continuity, q·j_L = [H,n] − (q²/2m)n, means **the longitudinal current
  is screened exactly like the density**. Transverse currents, and spins with SOC = 0, are unscreened at O(v_rel⁰). With SOC or magnetic
  order, R̃_{s,c} ≠ 0 [D]. Correction to the L3 chain: "screening of the density channel" must read "of every operator with R̃_{ac} ≠ 0;
  at minimum n and j_L".

**(5.4) How the ELF form emerges [D].** (5.3) with a = b = c, together with (4.1). At clamped nuclei and without LFE, R̃_cc = Π (D2) and
ε = 1 − vΠ. This gives Im[−ε^{-1}] = ε₂/|ε|², which is L2/L10 at the RPA level when Π → Π_KS.

**(5.5) Three-channel theorem [D at RPA/adiabatic-TDDFT level; C beyond].** In a process with one external vertex (q,ω), one phonon line
(Q, ω_Q) and a final electronic pair, every Coulomb line carries one of three momenta, fixed by topology (mod G):
- *external* (q, ω): resums into ε^{-1}(q,ω);
- *phonon* (Q, ±ω_Q): resums into the screened g, statically screened ε^{-1}(Q,0) = DFPT, error O(ω_Q/E_g);
- *pair* (q+Q, ω_e = ω ∓ ω_Q): resums into final-state RPA screening.
For generic Q these channels are distinct, so screening each once neither omits nor double counts. Cutting a pair-channel line does not
disconnect the diagram, because the phonon line still joins the two halves. So the pair channel is inside R̃ at (q,ω). The result is

  S^{PA}_{ee}(q,ω) = |(ε^{-1})_{00}(q,ω)|² Σ_{Qν,±}(n_{Qν}+½±½) (−2) Im[R̃⁰_{M†M} + R̃⁰_{M†ρ} v ε^{-1} R̃⁰_{ρ†M}]_{(q+Q, ω_e)},                (5.6)

where R̃⁰_{XY} is the IP pair response of the pair operators M ≡ Σ M^{(2),±}_{cvν}(k,q,Q) c†c (D2 eq. 2.1, with DFPT g) and
ρ = n_e(q+Q+G). Pair-resolved form (check C7):

  M̃_{cvk} = M_{cvk} + ρ_{cv}(k, q+Q) [v_{q+Q}/ε(q+Q,ω_e)] Π_{ρM}(q+Q,ω_e),   S^{PA} ∝ Σ|M̃|²δ(…).                               (5.7)
Here Π_ρM(p,ω_e) ≡ R̃⁰_{ρ†M}(p,ω_e) = (2/V)Σ_{k′c′v′} ρ*_{c′v′}(k′,p) M_{c′v′k′}/(ω_e − ε_{c′,k′+p} + ε_{v′k′} + i0) (resonant part).

If M ∝ ρ (density-dominated), the bracket reduces to Im R̃⁰_MM/|ε(q+Q,ω_e)|² (check C7b).

**(5.6) Prediction for X2 and consistency with M1 [D/C].**
- (a) D1/D2 (SOTA #4: external 1/ε only) is (5.6) with the pair term dropped. That is exact only if Π_ρM(q+Q,ω_e) = 0 or
  ε(q+Q) → 1, i.e. |q+Q| ≫ the inverse bond length.
- (b) REF-A's ε(q, ω∓ω_Q) is the Q → 0 limit of the pair channel ε(q+Q, ω∓ω_Q). For Q → 0 the acoustic M ∝ ρ_cv(k,q) (4.9), so that
  limit is the density-dominated case.
- (c) **The architecture therefore predicts that X2 must find two factors: the external |ε(q,ω)|^{-2} AND a pair-channel
  correction at (q+Q, ω∓ω_Q) in projected form (5.6)–(5.7). It reduces to |ε(q+Q,ω∓ω_Q)|^{-2} only for M ∝ ρ.**
- (d) If X2 finds a single ε(q, ω∓ω_Q) for all Q, that contradicts (5.5) except at Q → 0.
- (e) Size [E]: in the Si window |q+Q| ≈ k_c ≈ 1.9 keV and ε₁(1.9 keV, 1.2 eV) ≈ 2–3. The pair factor is between 1 (Π_ρM ≈ 0,
  random phases over k) and ≈ 0.1–0.25 (M ∝ ρ), so it is not negligible a priori. Numerical check (deferred): a ZG/supercell
  RPA+LFE ELF contains all three channels in the adiabatic limit, because Q is a supercell reciprocal vector.
- (f) The same theorem applies to L9 (q → 0): the pair channel is then (Q, ω∓ω_Q). The HBB/Noffsinger IP formula omits it. This is
  a prediction for WP3.

---
## 6. Expansion hierarchy and decomposition theorem

**(6.1) Small parameters** (definition; Si value [E]):

| symbol | definition | Si value | controls |
|---|---|---|---|
| κ_BO | (m_e/M)^{1/4}; u_zp ~ κa, ω_ph ~ κ²E_el, non-adiabatic mixing ~ κ³ | 0.066 | BO order n_B |
| η_ep(q,ω) | ⟨\|g\|²⟩/δ², δ = off-shell distance (D1 §5) | 10⁻³–10⁻¹ | e–ph order n_g |
| η_anh | ⟨u²⟩^{1/2}\|Φ⁽³⁾\|/\|Φ⁽²⁾\| ≈ γ_G ⟨u²⟩^{1/2}/a | 0.01–0.03 (T=0) | anharmonic order n_A |
| η_xc | ‖f_xc R̃‖/‖vR̃‖ (LFE); E_b/E_g (excitons) | 0.2–0.5; 0.013 | **ladder, not small**: error = next-rung difference |
| τ_ph, τ_g | T/ω_ph, T/E_g | 10⁻³ at 50 mK | thermal order (Bose; e^{−E_g/T}) |
| x_R | q²/(2M⟨ω⟩) | 0.05 at q = 10 keV | coherent 1-ph (x_R ≪ 1) → multiphonon → impulse (x_R ≫ 1) |
| 2W | q·⟨uu⟩·q = (q²/2M)⟨coth(βω/2)/ω⟩ | ≈ x_R (Einstein) | Debye–Waller / FC weight e^{−2W} |
| x_coh | q/G_min | — | coherent (Bragg-sum) vs incoherent approximation |
| σ_c | ΔE_e/(q v_rel) ∈ (0,1] | — | sudden (σ_c ≪ 1) vs threshold-adiabatic Migdal |
| ξ_D | q_e r_n (q_e = q for ER, ≈ m_e q/M for Migdal; r_n = orbital radius) | — | multipole (dipole) order n_D |
| 1/S, Δ/E_F | spin-wave, BCS | — | broken-symmetry references (§1.2) |

A truncation is a multi-index **τ = (n_B, n_g, n_A, X, n_T, K, 𝔐, n_D)**, with X ∈ {IP, RPA, RPA+LFE, TDDFT, BSE}, K ∈ {1ph, multi, imp} and
𝔐 ∈ {ad, sud}. Every LIMITS entry is a point τ (table in §9). The error estimate (§8) is the τ → τ + 1 increment.

**(6.2) Decomposition theorem.**
*Hypotheses.*
- (H1) H = H_C, plus optional local terms satisfying (L).
- (H2) The adiabatic electronic ground state Φ₀(r;R) is non-degenerate and gapped, Δ_ad(R) ≥ E_g > 0, on the support of the
  vibrational state. This means an insulator with no conical intersection in the support.
- (H3) Ground-surface vibrations are harmonic plus perturbative anharmonicity.
- (H4) T ≪ E_g.
- (H5), for the X0/X+ split only: in the (q,ω) region considered, every intermediate state of the perturbative expansion inside the
  excited block is off shell by δ ≫ the widths (D1 §5 window).

*Construction.* Let 𝒫₀ = ∫dR |Φ₀(R)⟩⟨Φ₀(R)| ⊗ |R⟩⟨R| and 𝒫_⊥ = 1 − 𝒫₀. Space-adiabatic perturbation theory (Panati–Spohn–Teufel,
math-ph/0201055) gives, under (H2), a unitary U_n such that 𝒫_⊥ U_n†HU_n 𝒫₀ = O(κ_BO^{n+1}). Final-state sectors:
- **G**: f ∈ U_n𝒫₀ℋ (electronic ground manifold, any vibrational state);
- **X0**: f ∈ U_n𝒫_⊥ℋ with zero net change of the reference-phonon Fock number;
- **X+**: f ∈ U_n𝒫_⊥ℋ with ≥ 1 net phonon created or absorbed.

*Theorem D.* For all a, b:
  S_ab = S_ab^G + S_ab^{X0} + S_ab^{X+} + O(κ_BO^{n+1}).                                                                     (6.1)
- (i) Each sector is (3.1) restricted by an orthogonal projector, and the projectors sum to 1. So each sector is Hermitian PSD (4.4),
  there is no double counting and nothing is omitted. **[D]** given U_n. PST is rigorous for smooth potentials, and Coulomb
  singularities are assumed harmless [C].
- (ii) Operators transform as O′ = U_n†OU_n. To leading order:
  - (O′_e)_{GG} = ⟨Φ₀(R)|n_e(q)|Φ₀(R)⟩: electrons follow the nuclei. This gives Z*/ε_∞ and the electron-channel phonon peaks;
    S^G_ee carries M¹ weight O(κ⁴) relative to (4.6a).
  - (O′_e)_{XG} = ⟨Φ_n(R)|n_e|Φ₀(R)⟩: the clamped transition density at R. Expanding in u gives the ZPL with FC/e^{−2W} (X0) plus the
    Herzberg–Teller sideband (X+, O(κ²)). Non-adiabatic corrections are O(κ²·ω_ph/δ), which is D1's adiabatic error.
  - (O′_κ)_{XG} = [S₁, n_κ]_{XG} ≈ (q/M_κ)·⟨Φ_n|∇_{R}Φ₀⟩/(E_n−E₀) × e^{iq·R}. **Migdal is purely non-adiabatic** (agrees with
    2505.08864 [ABS]). Its amplitude is ~(qa)κ⁴, so P ~ (m_eqa/M)².
  - For a single nucleus, ∇_RV = −Σ_i∇_{r_i}V. Using ∇V = i[p,H] and ⟨n|P_e|0⟩ = i m_e(E_n−E₀)⟨n|Σr_i|0⟩, we get
    ⟨n|Σ∇_iV|0⟩ = m_e(E_n−E₀)²⟨n|Σr_i|0⟩, so ⟨Φ_n|∇_RΦ₀⟩/(E_n−E₀) = m_e⟨n|Σr_i|0⟩. The amplitude is then the boost
    (m_eq/M)·⟨n|Σr_i|0⟩ (L7a, up to a phase) **[D, sketch]**.
- (iii) Partial sum rules:
  - M¹_ee = M¹^G + M¹^{X0} + M¹^{X+}, and M¹^{X0} + M¹^{X+} = n_eq²/m_e − O(κ⁴). The SOTA #3 compensation is the statement that X+ gains
    exactly what X0 loses at O(κ²).
  - M¹_κκ: G holds 1 − O(κ⁴) of n_κq²/M_κ, and Migdal (X) holds the rest.
  - M¹_eκ = 0 summed over sectors (4.6c), not sector by sector.
- (iv) The X0/X+ split is unique to O(η_ep) under (H5). Without (H5), only S^{X0} + S^{X+} is defined. The resonant part is assigned by
  the width prescription (Lorentzian → δ + Hadamard finite part, SOTA R2) **[C]**.

*Sector dictionary* (final state decides the sector, not the coupling):

| | G | X0 | X+ |
|---|---|---|---|
| S_ee | adiabatic electron-following (phonon peaks in the electron channel) | clamped/ZPR-renormalised electronic response (L1–L3, L10–L12, L14) | PAER (L8), phonon-assisted absorption (L9) |
| S_κκ | single phonon, multiphonon, NR (L4–L6, L18) | phonon-mediated Migdal, zero-phonon (L7d) | Migdal with phonons (L7a–c) |
| S_eκ | Born-charge interference (dark photon on phonons) | ionic screening of the ZPL (D2 §5) | Migdal–PAER interference (dark photon only) |

*Double-counting rules that follow from (6.1):*
- (a) A multiphonon S_κκ normalised to the full n_κq²/M_κ, plus a Migdal rate, overcounts M¹ by O(κ⁴). This is numerically negligible.
- (b) Adding the resonant sideband to the ZPL double counts (D1 §5.2).
- (c) Adding a computed PAER to a *measured* ELF double counts, because data already contain X0 + X+.
- (d) For couplings to both e and N (dark photon), S^{X+}_{eκ} ≠ 0. Migdal and PAER amplitudes to the same e–h + phonon state interfere and
  cannot be added in quadrature. The interference is bounded by (4.4).

---
## 7. From response to signal: final-state-resolved response

**(7.1) Definition [D].** Let {P_Λ} be orthogonal projectors on the sector-resolved final states of Theorem D, with Σ_ΛP_Λ = 1. Then

  S_ab(q,ω;Λ) = (2π/V) Σ_i p_i ⟨i|O_a† P_Λ δ(ω − H + E_i) O_b|i⟩,   Σ_Λ S_ab(q,ω;Λ) = S_ab(q,ω).                                    (7.1)

Each S(·;Λ) is PSD. Λ labels the *prompt* final state, defined after dressing (~1/E_g) and before relaxation (~1/ω_ph … ps):
- e–h: (n_e, k_e, ε_e; n_h, k_h, ε_h; spin, valley), with ε_e − ε_h = ω_e;
- phonon content: N_ph, {Q_jν_j}, E_ph = ω − ω_e;
- core hole: shell, which seeds Auger;
- plasmon/collective: decays to e–h with branching B(Λ_eh|pl);
- nuclear: recoil energy E_R, direction, and Frenkel-pair/defect label.

**(7.2) IP and RPA forms [D].** IP: S(q,ω;cvk) = (4π/V)|ρ_cv(k,q)|²δ(ω − ε_{c,k+q} + ε_{vk}). The distribution in (ε_e, ε_h) follows by
δ(ε_e − ε_c)δ(ε_h − ε_v). In RPA+LFE the external potential is screened and then creates bare pairs:

  S^{RPA}(q,ω;cvk) = (4π/V)|Σ_G (ε^{-1})_{G0}(q,ω) ρ_cv(k,q+G)|² δ(ω − ε_{c,k+q} + ε_{vk}),   ε_{GG′} = δ_{GG′} − v_{q+G}R⁰_{GG′}.

This holds because the total potential on the electrons at q+G is (ε^{-1})_{G0}φ_ext, and the pairs are then created by the bare vertex. Σ over cvk reproduces (5.4). The pair-channel
dressing (5.7) applies to X+.

**(7.3) Interface to WP5 [D given (7.1)].** The measured-quanta distribution is

  P(N_eh | q, ω) = Σ_Λ S(q,ω;Λ) P_casc(N_eh | Λ) / S(q,ω),    dR/dN_eh = ∫dω (dR/dω)(ω, Λ-weighted) P(N_eh|q,ω).                    (7.2)

So the cascade is seeded by Λ, not by ω (G1). **Minimum hand-over to WP5:**
- the joint density F(ε_e, ε_h, k_e, k_h | q, ω);
- for X+: N_ph and E_ph;
- for G (NR): E_R and direction;
- core-hole shell fractions;
- the collective-mode fraction.
L21's R&K model is the special case P_casc(N_eh|Λ) = P_casc(N_eh|ω), i.e. Λ marginalised with a phenomenological kernel.

---
## 8. Uncertainty structure (interface to WP6)

**(8.1) Nuisance per truncation [D as a definition; E as to the sizes].** For every active truncation k in τ:

  S_model(q,ω;θ) = S^τ(q,ω) + Σ_k θ_k Δ_k(q,ω),   Δ_k ≡ S^{τ+e_k} − S^τ  (computed or estimated by η_k^{n_k+1}S^τ),   θ_k ~ 𝒩(0,1).       (8.1)

Here e_k raises truncation k by one. For the ladder X, Δ_X is the computed next-rung difference (RPA+LFE − RPA etc.), not a power
estimate.

**(8.2) Sum-rule constraints on θ [D].** The exact relations restrict the nuisance space:
- f-sum (4.6): Σ_kθ_k∫ωΔ_k dω = n_eq²/m_e·(2π) − ∫ωS^τ. This is a linear constraint, known per q;
- positivity: S_model ≥ 0 pointwise;
- L17 (9.6): an upper bound on ∫ω^nS_model.
Truncations whose Δ_k carries M¹ weight are therefore partly fixed. Example: the PAER sideband and the ZPL loss are anti-correlated by
SOTA #3. **Correlations follow from shared physics**: one θ per truncation, applied coherently across q, ω, targets and experiments.

**(8.3) Propagation [D].** μ(σ,θ) = exposure × ∫dR/dω(θ)·eff. The likelihood is ℒ(σ,θ) = Π_bins Pois(n|μ) · Π_k𝒩(θ_k). Exclusion uses the
profile ratio λ(σ) = ℒ(σ, θ̂̂)/ℒ(σ̂, θ̂). The theory band is the envelope over |θ_k| ≤ 1, reported separately. Pointer: WP6 (G4).

---
## 9. L0 and L17 derived; pointers for every other entry

**(9.1) L0 [D].** *Chain.* (3.3) → single operator (𝔇 = |𝒱_{n_e}|² δ_{a,n_e}δ_{b,n_e}) → Δ_χ = 0 → Born → (2.3) normalisation:

  Γ = ∫ d³q/(2π)³ |Ṽ(q)|² S_ee(q, ω_q),   |Ṽ|² = πσ̄_eF_DM²/μ_χe²,   ω_q = q·v − q²/2m_χ.                                    (9.1)

Isotropic f_χ gives ∫d³v f_χ δ(ω−ω_q) = η(v_min)/(2q), with v_min = ω/q + q/2m_χ (confirms the REF correction to D1's η/q). Then

  dR/dω = (ρ_χ/m_χρ_T)(πσ̄_e/μ_χe²) ∫ q²dq/(2π²) F_DM² [η(v_min)/2q] S̄_ee(q,ω) = (ρ_χσ̄_e/(4π m_χρ_Tμ_χe²)) ∫ q dq F_DM² η S̄_ee(q,ω).   (9.2)

S̄ is the angular average, and (9.2) is D1 eq. (3) with 𝒢 = η/2q.
*Validity.*
- (a) Born: |Ṽ|μ_χ q/(4π) ≪ 1 (no DM bound states or resonances in the crystal potential).
- (b) Only O₁^{(e)} is non-zero, or the other 𝔇_ab are suppressed by the velocity and q/m_e powers of (2.3).
- (c) Elastic DM.
- (d) S_ee is the full electron-density response. The ELF form needs (5.5)(i) or (ii).
*Leading corrections.*
- (α) Cross-operator terms 2Re 𝔇_{n,j}S_{n,j} ~ (q/m_e)(v_χ, v_el) relative. With continuity, S_{n j_L} = (ω/q)S_nn exactly (local H), so
  the longitudinal velocity operators reduce to n [D].
- (β) Second Born ~ μ_χ|Ṽ|q/4π.
- (γ) T > 0: ω < 0 branch e^{−β|ω|} (4.3).
- (δ) Thermal motion and finite size of the target at q ~ 1/R: none for electrons.
**Status: DERIVED.**

**(9.2) L17 [D].** Define, for a coupling channel X ∈ {c (total charge), e (electrons only)},

  L_X(q,ω) ≡ (e²/2q²)(1−e^{−βω}) S_XX(q,ω) = −v_q Im R_XX = Im[−ε_X^{-1}],   ε_c ≡ ε (5.2),  ε_e^{-1} ≡ 1 + v R_ee.          (9.3)

Exact relations:
- Positivity (4.4) and (1−e^{−βω}) > 0 for ω > 0 give L_X ≥ 0 for ω > 0.
- With inversion or TR, L_X is odd in ω.
- KK (4.2) at ω = 0 with R^∞ = 0 gives
  ∫₀^∞ (dω/ω) L_X = (π/2)[1 − ε_X^{-1}(q,0)] = (π/2)(−v R_XX(q,0)) ≥ 0.                                                      (9.4)
  This is (π/2)(1 − 1/ε(q,0)) of 2110.01587 Eq. (1) and 2608.05282 Eq. (1) [FT].
- f-sum (4.6):
  ∫₀^∞ dω ω L_X = (π/2) ω_{p,X}²,   ω_{p,e}² = e²n_e/m_e (all electrons),   ω_{p,c}² = ω_{p,e}² + Σ_κ Z_κ²e²n_κ/M_κ.                     (9.5)
- Hölder with r = 2/(1+n), s = 2/(1−n) gives, for −1 ≤ n ≤ 1 (check C5),

  K_n^X(q) ≡ ∫₀^∞ dω ω^n L_X ≤ (π/2) ω_{p,X}^{n+1} [1 − ε_X^{-1}(q,0)]^{(1−n)/2}.                                                  (9.6)

  This is 2608.05282 Eq. (8) [FT], via (1 − 1/ε) = (ε−1)/ε. Inserting (9.6) in (3.4) with η_n^max gives their Eq. (9) and 2110.01587 Eq. (4).

*URF content: conditions and corrections.*
- (i) Validity: positivity plus (4.2) plus (4.6). The bound holds **at all orders in g, BO, anharmonicity and the XC ladder, and at any T**
  (with T: S = 2q²L/(e²(1−e^{−βω})), a factor ≤ (1−e^{−βω_th})^{-1}). The X+ sideband (PAER) cannot violate it. The truncated
  "static ZPL + sideband" can, by up to M¹^{SB} (D2 §3) [D].
- (ii) **Channel correction.** 2608.05282 states "DM couples to electron density" and uses ε. In the URF:
  - electron-only coupling needs ε_e(q,0), the fully relaxed static electron response with lattice relaxation;
  - dark-photon coupling needs the total ε(q,0) and ω_{p,c}.
  These are equal at clamped nuclei and differ by the ionic static polarisation (ε₀ vs ε_∞ for polar q → 0).
- (iii) **Hypothesis flag.** The "conservative" step 1 − ε^{-1}(q,0) ≤ 1 needs ε_X(q,0) ≥ 1 (or > 0). Stability gives only
  ε^{-1}(q,0) ≤ 1 (equivalently −R(q,0) ≥ 0). Negative static ε at q ≠ 0 is not excluded in general (Dolgov–Kirzhnits–Maksimov), so
  the conservative bound is CONJECTURED for arbitrary materials and DERIVED wherever ε_X(q,0) ≥ 1 is computed.
- (iv) **Tightening (leading correction) [E].** For ω_th above the phonon band, subtract the G-sector dω/ω weight:
  ∫_{ω_th}^∞ (dω/ω)L ≤ (π/2)[1 − ε_∞^{-1}(q)] + O(κ⁴), where ε_∞(q) is the clamped-ion static response. This is strictly tighter for polar
  targets.
- (v) **Generalisation L17′ [D].** Any operator with a kinetic-only first moment obeys (9.6) with ω_p² → e²M¹/q² (so that (π/2)ω_p² = ∫₀^∞ωL) and
  1−ε^{-1}(q,0) → −v R(q,0). Example: the spin channel (4.6e) under SU(2), with M¹ = n_eq²/4m_e and −R_{szsz}(q,0) = the static spin
  susceptibility. This gives sum-rule bounds for O₄-type electron-spin couplings (new, [E] for usefulness).
**Status: DERIVED** (modulo (iii)).

**(9.3) Pointers.** "τ" is the truncation that should produce each entry. ✔ = LIMITS chain confirmed; ✎ = corrected.

| # | τ / chain (URF) | ✔/✎ |
|---|---|---|
| L1 | S^{X0}_ee; n_B = 0 (clamped), X = IP, no (5.3) dressing, isotropic, spin 2 | ✔ |
| L2 | (5.4)/(5.5): ELF form needs clamped nuclei or ω ≫ ω_max (O(κ⁴)); X = RPA or exact | ✎ (add the condition) |
| L3 | multi-operator (3.3), X = IP, **+ screening of every a with R̃_{ac} ≠ 0 (n, j_L; s with SOC)** | ✎ |
| L4 | S^G_{κκ}, S^G_{cc}; n_B = 0 adiabatic (O′_e)_{GG} → Z*, ε_∞; harmonic one-phonon, K = 1ph | ✔ |
| L5 | S^G_κκ harmonic all orders, incoherent (x_coh ≫ 1), K = multi | ✔ |
| L6 | S^G_κκ at x_R → ∞; leading correction = Gaussian Doppler width from the 1/x_R expansion | ✔ (the label "sudden" is unnecessary) |
| L7a | S^{X+}_κκ, isolated atom, K = imp, σ_c ≪ 1, dipole n_D = 1 (§6.2 ii) | ✔ |
| L7b | S^{X}_κκ, K = imp, non-adiabatic coupling dominated by the long-range ionic Coulomb field → ELF | ✔ |
| L7c | S^{X}_κκ with G-sector phonon final states, n_B = leading non-adiabatic, harmonic | ✔ |
| L7d | S^{X0}_κκ (zero-phonon final state) via virtual phonon × g | ✎ (it is X0, not X+) |
| L8 | S^{X+}_ee at n_g = 2 + three-channel screening (5.6) | ✎ (pair channel) |
| L9 | q → 0 of L8, transverse; pair channel at (Q, ω∓ω_Q) (5.6f) | ✎ |
| L9b | (3.5)–(3.6) at k ≈ 0; A′: Γ = κ²m Im(−1/ε); ALP–e: Tr J_e (= current only at SOC = 0); aγγ: (2.9) | ✔ + ALP caveat |
| L10–L11 | jellium limit of WP1 RPA; plasmon = zero of ε in (5.4) | ✔ |
| L12 | S^{X0}+S^{X+} at n_g = 2 in the adiabatic limit ω_Q/δ → 0 (ZG = stochastic evaluation of (O′_e)_{XG} averaged over the harmonic R distribution) | ✔ |
| L13 | spin row of (2.2), magnetic reference, linear spin wave (1/S) | ✔ |
| L14 | X = BSE in R̃ | ✔ |
| L15 | BCS broken-symmetry reference (not a finite n_g truncation; Cooper resummation) + RPA with coherence factors | ✎ |
| L16 | low-energy Dirac H + RPA (5.4) | ✔ |
| L17 | §9.2 | DERIVED |
| L18 | n_A = 1 on S^G_κκ | ✔ |
| L19 | (3.3) with full q-vector S, no angular average | ✔ |
| L20–L23 | WP5 cascade/partition with the (7.2) Λ-seeding; L21 = Λ-marginalised kernel | ✔ |
| L24 | (3.4) halo integral + WP6 (8.3) | ✔ |

**(2.9) (cited above) ALP–photon absorption [D, k → 0, uniform B₀].** Map κm² → g_aγγB₀m_a in the dark-photon result
−Im[m²Π/(m²−Π)]/m = m Im(−1/ε) (check C6):

  Γ_a = g_aγγ² B₀² Im[−1/ε_∥(m_a)]/m_a,   with ε_∥ the dielectric component along B₀.

This agrees with the abstract of 2305.05681 ("determined by the dielectric function") [ABS]. Prefactors to be confirmed by WP1/WP4.

---
## 10. NOTATION v2 (proposed additions; no collisions with NOTATION.md)

**Collisions found in the current files (to fix):**
- v = DM velocity *and* valence index. Proposal: keep v for velocity and write the valence index as v only as a subscript on band
  quantities; never write a bare v for the band.
- Q = phonon wavevector (NOTATION) *and* ionization yield (L21). Proposal: rename the yield N_eh.
- χ = DM (NOTATION) *and* response function (D2). Response is now R.
- S = structure factor *and* DM/nucleon spin S_χ, S_ψ *and* Huang–Rhys. Proposal: spins are bold **S**; Huang–Rhys is S_HR.
- L = ELF *and* orbital angular momentum (2009.13534). Proposal: orbital is 𝐋_ψ.
- Δ = DM mass splitting *and* energy denominators (D1/D2). Proposal: splitting is Δ_χ.
- W = Debye–Waller *and* the Catena W₁…W₅ responses. Proposal: the latter become 𝒲_i.

| Symbol | Meaning |
|---|---|
| s ∈ {e, κ}, z_s, n_s(q), N_s | species label, charge number (z_e = −1), number density operator, number |
| ρ_c(q) | charge density e Σ z_s n_s |
| O_a(q), a = (ψ,Γ) | target operator basis (2.2): Γ ∈ {0, b, a, ab} = density, spin, velocity, spin-current |
| s_e, j_e, J_e^{ab}, τ_e | electron spin density, paramagnetic current (velocity units), spin-current, kinetic-energy density |
| n_κ^F, 𝐈_κ, j_κ, F^M_κ, F^Σ_κ | nuclear density with form factor, nuclear-spin density, nuclear CM current, nuclear form factors |
| 𝒱_a^{s′s}(q,v_χ) | DM vertex (2.2); v_χ = v − q/2m_χ |
| 𝔇_ab | DM tensor (2.3) |
| S_ab(q,ω) | response matrix (3.1); S_ee ≡ the NOTATION S |
| R_ab, R̃_ab | full and Coulomb-proper retarded response (3.2), (5.1); D2's Π ≡ R̃_ee at clamped nuclei |
| ε_{GG′}, ε_e | total dielectric matrix (5.2); electron-channel ε_e^{-1} = 1 + vR_ee |
| L_X, K_n^X | channel loss function (9.3), moments (9.6) |
| ω_{p,e}, ω_{p,c} | all-electron plasma frequency, total-charge plasma frequency |
| M¹_ab, M³_ab | moment matrices (4.5), (4.7) |
| Δ_χ | DM mass splitting |
| κ_BO, η_ep, η_anh, η_xc, τ_ph, τ_g, x_R, W, x_coh, σ_c, ξ_D | small parameters (6.1) |
| τ = (n_B, n_g, n_A, X, n_T, K, 𝔐, n_D) | truncation multi-index |
| 𝒫₀, 𝒫_⊥, U_n; G, X0, X+ | adiabatic projectors, decoupling unitary, final-state sectors (6.2) |
| Λ, P_Λ, S(q,ω;Λ) | final-state class, projector, resolved response (7.1) |
| N_eh | ionization yield (replaces Q in L21) |
| θ_k, Δ_k | nuisance parameter and truncation increment (8.1) |
| Ξ_n | deformation-potential tensor (4.9) |

---
## 11. Literature used (all IDs verified against the arXiv API, 2026-10-31)
- 1203.3542 (Fitzpatrick et al., NR-EFT): operator basis, [ABS + via 2009.13534].
- 2009.13534 (Trickle–Zhang–Zurek–…): Table III and Eqs. (13), (15)–(27) [FT].
- 2105.02233 (Catena et al.) [FT, structure].
- 2106.12586 (Mitridate et al.): Table I, Eqs. (18)–(22) [FT].
- 2110.01587 (Lasenby–Prabhu): Eqs. (1)–(4), (C1) [FT].
- 2608.05282 (Barker et al.): Eqs. (1)–(9) [FT].
- 2501.18261, 2101.08275, 2101.08263, 2011.09496, 2505.08864, 2210.06490, 1608.01994, 2510.25835, 2402.06817, 1911.03482,
  1707.07258, 1509.01598, 2205.03395, 1905.13744, 2309.10839, 2205.02250, 1712.06598, 2603.13052, 2305.05681 [ABS / title check].
- math-ph/0201055 (Panati–Spohn–Teufel, space-adiabatic perturbation theory) [ABS].
PDFs deleted after reading (brief).

## 12. Open items handed on
- O1: the X2 test of (5.6c–d).
- O2: WP3: (4.9), with signs, and the pair channel in L9.
- O3: WP1: relativistic operator matching for cores (§1.2), and the L3 screening of j_L and s.
- O4: proof of Theorem D (iv) without (H5).
- O5: L17 (iii): whether ε(q,0) ≥ 1 for the target set.
- O6: the 2.5/2.9 prefactors against the full text of 2305.05681.
