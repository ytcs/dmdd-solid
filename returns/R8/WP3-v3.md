# R8 / WP3-v3: the mixed electron–lattice sector of the URF, with the consolidated M1 (PAER) theory

Revision agent, brief R8/REV3-WP3. Supersedes returns/R6/WP3-v2.md (historical record) after the R7 hostile review (referees/R7/REF-WP3-A.md,
REF-WP3-B.md). Standalone: Part I is the complete M1 theory, Part II the joint response, Migdal, absorption, ZG, bremsstrahlung and excitons.
Conventions: CONVENTIONS.md; symbols: NOTATION v4; architecture: returns/R6/WP0-v2.md as amended by returns/R8/WP0-v3.md (cited "WP0-v3 (s.n)"
where v3 changed the item, "WP0-v2 (s.n)" otherwise). Window inputs: returns/R8/WP1-v3.md [E13], [E14], IF-6, IF-6b; moments: returns/R8/WP2-v3.md
(5.2″), IF-1. Checks: `code/WP3-v3/checks.py` (sympy/mpmath only, no simulation; **114 checks, all PASS, ≈ 12 s** (R9)); labels WP3v2-Cn (unchanged from v2)
and WP3v3-Cn (new or corrected). Tags: **[D]** derived (hypotheses stated), **[D, sketch]**, **[E]** estimated, **[C]** conjectured; literature
**[FT]** full text, **[ABS]**, **[UNVERIFIED]**, and the R7 literature ratings **CONFIRMED / REFUTED / UNRESOLVED**. Labels of other returns carry
their prefix (CONVENTIONS §14). Equations: (M.n) Part I; (W.n) Part II (v1 numbers kept). Status: CLAIMED, pending audit.

---
## 0. What changed in v3, and results in brief
| v2 | v3 | change (referee item) |
|---|---|---|
| §M3 (ii): Si TA S̄ edge p̄_on = 4 (vertex zero on the valley axis), LA kink 3 | §M3 (b)–(e), table | **FALLS → replaced** by a C4v/C3v character analysis computed from the diamond geometry: Si TA edge p̄_on = 3, **LA kink 4** (LA forbidden on axis), TO, LO 3; Ge 3 for all branches (A-V11, B-12; C24) |
| C23a: minimum at q̂ ∥ K̂ (isotropic c_ν) | §M3 (b), (e) | anisotropic c_ν: on-axis minimum iff γ_c > −\|K_pk\|/(2\|q\|); with dispersion γ_ω > −(\|K_pk\|/2\|q\|)·v_gd_K/ω₀(d_K) (R9); Si TA crossover ≈ 0.8–1.0 keV [E]; Ge conical axis (A-V10, B-11; C23d–l) |
| fixed-q threshold E_g + ω_{Q*} | §M3 (a) | min over pockets, shift −½(m_c+m_h)\|∇ω\|² ≈ 0.14–0.29 meV (A-V9, B-10; C25) |
| Q_w removes the shell; δ₀ = 0.1 eV; c_TA·d | §M3 (c), §M4, §M8 | polar cap only; δ₀ = 0.3 eV (Q_w ≈ 0.31–0.33 Å⁻¹); ω_TA(Q*) (A-V12, B-4, B-13; C30) |
| M1 window 0.34–0.47 MeV "PAER-only" | §M9 | **restated**: Si PAER-only 0.333 (replica) / 0.337 (continuum)–≈0.42 MeV; coexistence with the forbidden zero-phonon channel 0.42–0.54 (PAER leads only to ≈ 0.43); Ge ≈ 0.213–0.32 MeV (WP1-v3 [E13], [E14]) |
| (M.4), (M.14), (W.4c): ÷(1 − e^{−βω}) on top of (n+½±½) | (M.3), (M.4), (M.14), (W.4c) | thermal factor once, EPW w^{EPW}_± weights (A-V2, B-2; C21a–c) |
| [0.5, 1.2] pair-screening factor | §M7 | **[0.4, 1.8] [E/C]**, composition and sign hypotheses stated (A-V7, B-8; C28) |
| (M.13) [D at RPA/ALDA] | §M7 | [D at RPA/TDH]; ALDA k_xc source; W^{scr}(P,ω_f) retarded (B-7; C27) |
| 2603.13052: "m_N → m_N² in (4.7), rate consistent" | §2 L7c | REFUTED repair withdrawn: m_N misplaced between (4.6) and (4.7); (4.8) UNRESOLVED (A-V15/16, B-15/16; C3a–d) |
| L7c correction ≈ 10⁻⁵; fn. 3 "therefore conservative" | §2 L7c | ≲ 10⁻³ (2p²/Mω_e, ω_ph²/ω_e²); agreement with fn. 3 (A-V14, B-17; C9b) |
| ZG "antithetic sign pairing (7)–(8)" | §5 | alternating signs (7)–(10); antithetic pair (12); characterisation, not an error of the paper (A-V17, B-18) |
| L9b(b): E_g rises 50 meV, O(1) within 0.1 eV | §4 | 77 K data: 4 meV, n_TA ≈ 0.07, O(1) within ≈ 20–25 meV (A-V22 REFUTED in size; C9c) |
| (W.13) "∝"; GaAs ~10³× atomic | §6 | equality with measure, impulse hypothesis; 10³–10⁴× (B-20, A-V18; C9d) |
| J3 "upper bounds" | J3 | [E] (B-21) |
| J8 (ii) contact form | J8 | × [1 + 2𝓃_e/𝓃_e(R_κ)] at q → 0⁺; finite-q via WP2-v3 (5.2″) (WP0-v3 G5; C26) |
| Theorem D remainder O(κ_BO^{n+1}); J2 S_ab[O†] | §1.1, J2 | O(κ_BO^{2(n+1)}); S_ba[O†] (WP0-v3 G10, G3) |
| K, E_th (collisions); Q_w, d, p̄_on, θ undeclared | §16 | K_pk, E^{PA}_th(q̂), ϑ; declared (A-V23) |

**Results.** (1) **M1 [D]:** S^{X+}_ee = (2q²/e²)L^{PA}/(1 − e^{−βω}) with L^{PA} built from the fully screened M̃ (M.13)–(M.14) and the EPW weights w^{EPW}_±; the
unrestricted-band amplitude (M.1); the window (M.9) and, outside it, the Dyson convention with O4's invariance theorems (§M4); soft limit (M.15);
f-sum compensation as a first-moment aggregate (§M5); computable recipe (§M10). (2) **Onset exponents for WP6 [D, symmetry; E, location]:** Si S̄ edge
p̄_on = 3, LA kink 4, Ge 3 (§M3 table). (3) **M1 window [E]:** §M9. (4) **Joint response S_ab(q;ω_ph,ω_e) [D]** with J1–J8. (5) **Migdal family [D]:**
L7a–d are truncations of (W.5). (6) L9, L9b, L12, crystal NR bremsstrahlung (W.13), exciton replicas (W.14). R7: 48 referee items, closing table §13.

---
# Part I. M1: the phonon-assisted electronic response (PAER)

## M1. Set-up [D]
Hypotheses (P1) BO, harmonic phonons, linear e–ph coupling (the O(u²) AH vertex g^{AH} enters only the ZPL, §M5); (P2) KS/QP independent pairs
(screening at RPA/TDH level, ALDA term §M7; excitons beyond, §7 and [C]); (P3) T ≪ E_g; (P4) spin-independent vertex, no SOC (with SOC drop the spin 2, sum
spinor bands); (P5) insulator (WP0-v2 (H2)). u_{Rκ} = Σ_{Qν}(2NM_κω_{Qν})^{-1/2}e_{κν}(Q)e^{iQ·R}B_{Qν}, B_{Qν} = b_{Qν} + b†_{−Qν}, e_{κν}(−Q) = e_{κν}(Q)*;
H_ep = N^{-1/2}Σ g_{mnν}(k,Q)c†_{m,k+Q}c_{nk}B_{Qν} (EPW, DFPT-screened, O(1)); hermiticity g_{mnν}(k,Q)* = g_{nmν}(k+Q,−Q) (needs e(−Q) = e(Q)*).
DM vertex V^{-1}Ṽ(q)n_e(q), n_e(q) = Σ_kρ_{mn}(k,q)c†_{m,k+q}c_{nk}, ρ O(1) with Umklapp inside (CONVENTIONS §4). Final state: electron (c, k′ = k+q+Q),
hole (v, k), and phonon −Q emitted (upper sign, weight n_{Qν}+1) or +Q absorbed (lower sign, n_{Qν}); both with g(·,Q); pair momentum P = q+Q, pair
energy ω_f = ω ∓ ω_{Qν}; on shell ω = ε_{ck′} − ε_{vk} ± ω_{Qν}.

## M2. Amplitude: four paths and the Pauli/exchange theorem [D under P1–P5]
Two one-body vertices take Φ₀ to one pair by exactly four routes (a diagonal first vertex needs q ∈ G, measure zero; REF-A §2):
| path | 1st vertex | 2nd vertex | m | E_i − E_I | sign |
|---|---|---|---|---|---|
| A | DM (v,k)→(m,k+q) | ph (m,k+q)→(c,k′) | empty | ω − ε_{m,k+q} + ε_{vk} | + |
| B | ph (v,k)→(m,k+Q) | DM (m,k+Q)→(c,k′) | empty | ε_{vk} − ε_{m,k+Q} ∓ ω_Q | + |
| C | DM (m,k+Q)→(c,k′) | ph hole (m,k+Q)→(v,k) | occupied | ω − ε_{ck′} + ε_{m,k+Q} | − |
| D | ph (m,k+q)→(c,k′) | DM hole (m,k+q)→(v,k) | occupied | ε_{m,k+q} − ε_{ck′} ∓ ω_Q | − |
Sign: c†_mc_vc†_cc_m|Φ₀⟩ = −c†_cc_v|Φ₀⟩ (m occupied) vs + (m empty). **Theorem:** on shell D equals the A-form with m occupied and C the B-form
(WP3v2-C11a,b), so Pauli blocking is undone by the exchange (Z-graph) partners and the many-body amplitude is the one-electron one with an
**unrestricted** band sum (D1 eq. (1) ≡ D2 eq. (2.1)·√N on shell):

  M^{(2)}_{cvν,±}(k,q,Q) = Σ_m^{all} [ g_{cmν}(k+q,Q)ρ_{mv}(k,q)/d_{A,m} + ρ_{cm}(k+Q,q)g_{mvν}(k,Q)/d_{B,m} ],
  d_{A,m} = ε_{ck′} − ε_{m,k+q} ± ω_{Qν},   d_{B,m} = ε_{vk} − ε_{m,k+Q} ∓ ω_{Qν},                                                      (M.1)

  T_fi = (Ṽ(q)/V) N^{-1/2} (n_{Qν} + ½ ± ½)^{1/2} M^{(2)}_±   (D1 normalisation, CONVENTIONS §5; D2's amplitude is M^{(2)}/√N).                (M.2)

A₁ (first term: density first, electron then scatters) and A₂ (hole scatters / phonon first). Consequences: restricting m to empty bands is wrong
(breaks the completeness that C1 and C7 need); the identity is on shell only (WP3v2-C11d), so off-shell objects (ε₁^{PA}, the O(g²) ZPL vertex) need
the four-path or Kubo form; disconnected terms (I = Φ₀ with ⟨Φ₀|n_e(G)|Φ₀⟩ ≠ 0) cancel against the I = f piece (linked clusters), leaving the m = v (A),
m = c (B) terms already in (M.1); Umklapp is automatic with unfolded q and the periodic gauge. Spec D1 N-a (Fock-space brute force, M = 6–8 orbitals).

## M3. Rate, ε₂^{PA}, zero-phonon limit, onset [D]
With Σ_{p′} = V∫d³q/(2π)³, spin 2, Bose factors, ⟨⟨·⟩⟩ = N^{-2}Σ_{kQ} = Ω²∫_BZ d³kd³Q/(2π)⁶:

  S^{PA}(q,ω) = (4π/Ω)⟨⟨Σ_{cvν±}(n_{Qν}+½±½)f_v(1 − f_c)|M^{(2)}_±|² δ(ε_{c,k+q+Q} − ε_{vk} ± ω_{Qν} − ω)⟩⟩   (proper, unscreened; screened: M → M̃, §M7),     (M.3)

  ε₂^{PA}(q,ω) = (e²/2q²)(1 − e^{−βω})S^{PA} = (8π²α/Ωq²)⟨⟨Σ w^{EPW}_±|M^{(2)}_±|²δ(…)⟩⟩ ≡ D2 (2.2) (WP3v2-C22a),
  w^{EPW}_± ≡ (1 − e^{−βω})(n_{Qν}+½±½)f_v(1 − f_c) = EPW 2302.08085 Eq. (64) on shell, at every T (WP3v3-C21a).                                  (M.4)

**Thermal factor, once (v3; A-V2, B-2):** (M.3) is the golden-rule structure factor (emission n+1, absorption n, electron factors f_v(1 − f_c) = 1 + O(e^{−E_g/T}));
the proper ε₂ and L^{PA} carry w^{EPW}_± (absorption minus stimulated emission), so S = (2q²/e²)L/(1 − e^{−βω}) holds exactly at finite β (C21b). v2 wrote
(n+½±½) in both (M.4) and (M.14) and also divided by (1 − e^{−βω}) in (W.4c): a double count at O(e^{−βω}) (C21c); v2's C21 tested only β → ∞. Numerically nil
for T ≪ E_g; consistent with WP0-v3 (5.6) and F7. The zero-phonon analogue (8π²α/Ωq²)N^{-1}Σ_k|ρ_cv|²δ is Adler–Wiser (e²_G = α). D2's script docstring πe²/(q²V) is per spin (WP3v2-C22b; script not edited).
Rate per DM particle Γ_χ = ∫d³q/(2π)³|Ṽ|²S(q,ω_q), |Ṽ|² = πσ̄_eF_DM²/μ_χe² (WP0-v2 (9.1)); per unit target mass (WP0-v2 (3.4)) with 𝒢 = ∫d³vf_χδ(ω − ω_q):

  dℛ/dω = (ρ_χ/m_χρ_T)(πσ̄_e/μ_χe²)∫d³q/(2π)³ F_DM² 𝒢(q,ω) S(q,ω),   (I) angle-averaged S: 𝒢 → η(v_min)/(2q),        (M.5)
  dℛ/dω = (ρ_χσ̄_e/(4πm_χρ_Tμ_χe²)) ∫q dq F_DM² η(v_min) S̄(q,ω)   (D1's η/q and 1/(2π) owe a factor 2; WP3v2-C12a,b).                              (M.6)

Zero-phonon limit: S^{(1)} = 4π∫_BZ d³k/(2π)³Σ_{cv}|ρ_cv(k,q)|²δ(ω − ε_{c,k+q} + ε_{vk}); with ∫d³q′ = Σ_{G′}∫_BZ d³k′ (6) becomes the Bloch rate

  dℛ^{(1)}/dω = (ρ_χσ̄_eαm_e²/(m_χρ_TΩμ_χe²))∫dq q^{-2}ηF_DM²|f_crys|²,  |f_crys|² = Ωq³S̄^{(1)}/(4παm_e²) = (2π²/(αm_e²Ω))Σ_{cv}∫∫(Ωd³k/(2π)³)(Ωd³k′/(2π)³)Σ_{G′}qδ(q − |k′−k+G′|)|ρ_cv|²δ(…),   (M.7)

= 1509.01598 Eqs. (17), (21) and 2101.08275 Eq. (16) (WP1 [E12]; WP3v2-C12c; D1's 4π²/2πα corrected). **Onset (WP6 O6-2) [v3; A-V9–V12, B-10–B-13].** Notation: K_pk ≡ k_c − k_v + G (pocket-pair vector, one per valley and G), Q* = K_pk − q,
d_K(|q|) ≡ ||q| − |K_pk||, ϑ = ∠(q̂, K̂_pk), ϑ_Q = ∠(Q̂*, K̂_pk), E^{PA}_th(q̂) the angle-dependent PAER threshold at fixed |q|.

**(a) Fixed q [D, parabolic pockets].** At T = 0 the emission branch opens at E^{PA}_th(q) = min_{k,k′}F, F = ε_c(k′) − ε_v(k) + ω_ν(k′ − k − q), not at
E_g^{ren} + ω_ν(Q*): the tilt ∇_Qω_ν moves the 6-dimensional quadratic minimum of F down by ½(m_c + m_h)|∇_Qω_ν|² (masses along ∇ω; WP3v3-C25a), Si
≈ 0.14 meV (TA), 0.29 meV (LA) (C25b; REF-A's order, REF-B's "μeV" too small). k and k′ are independent pockets, so S^{X+} ∝ (ω − E^{PA}_th)^{p_on},
p_on = 2 if M̃ ≠ 0 at the minimum, 3 if it vanishes linearly (C19), ½ per exciton band with (W.14). At T > 0 the absorption branch starts ≈ E_g − ω_{Q*ν}.

**(b) Angle average at fixed |q| [D for an isolated minimum; WP1 [E10] rule].** E^{PA}_th(q̂) = E_g^{ren} + ω_ν(Q*(q̂)). With |Q*|² = d_K² + |q||K_pk|ϑ² + O(ϑ⁴)
and the tilt ϑ_Q ≃ |q|ϑ/d_K, and c_ν(Q̂) = c₀(1 + γ_cϑ_Q²) near a symmetry axis K̂_pk (stationary there by symmetry),

  E^{PA}_th(ϑ) = E_g^{ren} + c₀d_K + c₀(|q|/d_K)(γ_c|q| + |K_pk|/2)ϑ² + O(ϑ⁴)   for |q| > |K_pk| and |q| < |K_pk| alike (WP3v3-C23d),      (M.7a)

so q̂ ∥ K̂_pk is a minimum iff **γ_c > −|K_pk|/(2|q|)** (C23e). **Dispersive form (R9; VER-WP3-B N1) [D]:** with ω_ν(Q,ϑ_Q) = ω₀(Q)(1 + γ_ω(Q)ϑ_Q²),
E^{PA}_th − E_g^{ren} = ω₀(d_K) + [ω₀′(d_K)|q||K_pk|/(2d_K) + ω₀(d_K)γ_ω|q|²/d_K²]ϑ² (WP3v3-C23l), so the axis is a minimum iff
**γ_ω(d_K) > −(|K_pk|/(2|q|))·r(d_K)**, r ≡ v_gd_K/ω₀(d_K) ≤ 1 for sub-linear branches ((M.7a) is the r = 1, linear case). Stationarity of c_ν on the axis (REF-A) is necessary, not sufficient; REF-B's criterion γ_c > −½ is
the case |q| = |K_pk|. If it fails the minima move off axis; if the axis is a conical point of the branch (degenerate TA on a 3-fold axis) the axis is never
a minimum. Any isolated quadratic minimum gives p̄ = p_on + 1, and p_on + 2 if |M̃|² ∝ (distance)² there (C23b,c); a minimum on a C_nv axis where the vertex is
symmetry-forbidden gives p_on + 2.

**(c) Window and Q_w [D, parabolic pockets].** E_min(q) − E_g^{ren} = |Q*|²/2M_x (M_x = m_c + m_h along Q̂*), so ω ≤ E_min − δ₀ at the onset ⇔ |Q*| ≥ Q_w,
Q_w = M_xc + (M_x²c² + 2M_xδ₀)^{1/2} ≈ (2M_xδ₀)^{1/2} (C30a). Si (M_x = m_l + m_hh ≈ 1.41 m_e; WP1-v3 uses 1.19 m_e, both [UNVERIFIED]): **Q_w ≈ 0.31–0.33 Å⁻¹ at δ₀ = 0.3 eV**, the value consistent with
(M.9) (δ₀ ≫ ω_max ≈ 60 meV); 0.19 Å⁻¹ at δ₀ = 0.1 eV, which then carries an adiabatic/convention error ω_Q/δ₀ ≈ 0.6 (C30b; B-4, B-13). At fixed |q| the failing set
is the **polar cap** |Q*| < Q_w, cos ϑ_w = 1 − (Q_w² − d_K²)/(2|q||K_pk|) (C30c), not the whole shell (A-V12): for d_K < Q_w, S̄ is a mixed object (in-window outside
the cap, DC inside, O4 d11) and its apparent onset at the cap rim is set by the convention, so no PAER-only exponent is assigned there; for d_K ≥ Q_w the cap is
empty. Thresholds use ω_ν(Q*) (Si TA is already sub-linear at |Q*| ≳ 0.2 Å⁻¹), never c_ν·d_K. For free pairs the infimum over q is E_g (acoustic Q* → 0 at |q| = |K_pk|),
where the window is empty; exciton replicas start at E_x + ω_ν(Q*), which can lie below E_g (Si: 1.1688 eV), so E_g is not a floor for them (AUDIT-2 m2).

**(d) Symmetry of the on-axis amplitude [D, SOC = 0; C24, computed from the geometry].** Si: hole at Γ (Γ₂₅′), electron Δ₁ at k_c ∥ [100]; on the axis q, Q*,
k_c are invariant under C₄ᵥ(x) and momentum conservation cancels all nonsymmorphic phases except the operator's e^{−iG′·t} (WP1-v3 §3.2(c)); t_d elements
are C₄^±, σ_y, σ_z (C24a). Characters: Γ₂₅′ ↓ C₄ᵥ = Δ₂′ ⊕ Δ₅, no Δ₁ (C24b); Γ₁₅ ↓ C₄ᵥ = Δ₁ ⊕ Δ₅ (C24c); the mechanical representation along Δ, built from
the two-atom basis with its translations, is Δ₁ ⊕ Δ₂′ ⊕ 2Δ₅ at every ξ (C24d), with **LA = Δ₁** (the branch continuous to the in-phase translation has reduced
C₄ character +1, C24e), LO = Δ₂′, TA = TO = Δ₅ (agrees with the standard compatibility tables, which REF-A quoted from memory; the derivation here does not rely
on them). The amplitude is nonzero iff A₁ ⊂ Δ₁ ⊗ Γ_op ⊗ Γ_ph ⊗ (Δ₂′ ⊕ Δ₅):
- G′ = 0 class (Γ_op = Δ₁; the nearest K_pk for |q| < 2.28 keV): **LA forbidden; TA, TO, LO allowed** (C24f; REF-A).
- G′ = (2̄00) class (Γ_op = Δ₂′, glide phase −1; |q| > 2.28 keV): **LO forbidden; LA, TA, TO allowed** (C24g; new).
- Ge: electron L₁ (Λ₁ on the axis), C₃ᵥ has no t_d elements (C24h), Γ₂₅′ ↓ C₃ᵥ = Λ₁ ⊕ Λ₃, phonons 2Λ₁ ⊕ 2Λ₃: **all branches allowed** (C24i,j). With SOC
  (Γ₈⁺ → E₁/₂ ⊕ E₃/₂, L₆ → E₁/₂ of the C₃ᵥ double group) E₁/₂ ⊗ (E₁/₂ ⊕ E₃/₂) contains A₁ and E, so still allowed [D, sketch].
The v2 argument (conduction intravalley Ξ_u(Q̂·k̂)(k̂·ê) multiplying ρ_cv) is withdrawn: ρ_cv(Γ, q ∥ x) vanishes on the axis for every branch (WP1-v3 §3.2), so it
could not single out TA; the surviving on-axis TA amplitude comes from interband paths (A via Δ₅ intermediates; B with the valence shear deformation potential
d, B-12(iii)), and (M.15) is an off-shell control that cannot decide on-shell vertex zeros (B-9 caveat, B-12(iv)). SOC lifts the Si LA zero at
O(Δ_SO/ΔE) ≈ 4% in amplitude [E] (WP1-v3 §3.2).

**(e) Location of the minima [E, continuum elasticity; C^{el} (GPa) Si 165.7/63.9/79.6, Ge 128.5/48.3/66.8; dispersion at d_K ≈ 0.3–1 Å⁻¹ beyond its range].**
Si lowest TA about [100]: γ_c = −(B² − A²)/(2AC^{el}_{44}) = −0.96 (A = C^{el}_{11} − C^{el}_{44}, B = C^{el}_{12} + C^{el}_{44}; (001) tilt plane, C23f), −0.88, −0.78 at
azimuth π/8, π/4 (C23g). In linear elasticity the TA axis would be a minimum for |q| < |K_pk|/(2|γ_c|) ≈ 0.52|K_pk| ≈ 1.0 keV (G′ = 0); with a sine-like TA dispersion
(r ≈ 0.83 at d_K ≈ 0.45 X) the crossover moves to |q| ≈ 0.41|K_pk| ≈ **0.79 keV** with r(d_K) evaluated self-consistently, ≈ 0.85 keV with r frozen at 0.83 (VER-WP3-B) (C23l,m), so the crossover is ≈ 0.8–1.0 keV [E, needs ab initio ω_TA(Q),
γ_ω(Q); O-WP3-9]; above it the axis is a local maximum (REF-B's case),
with off-axis minima in the {001} planes; as |q| → |K_pk| they sit at ϑ_Q ≈ 0.42 rad with E^{PA}_th − E_g^{ren} ≈ 0.966 c_TA d_K (C23h, REF-B reproduced); exact
geometry (linear dispersion): on axis at |q| = 0.5|K_pk|, off axis (0.94 of the on-axis value) at |q| = 1.3|K_pk| (C23i). LA: γ_LA > 0, on-axis minimum at every |q| (C23j). Ge:
[111] is a conical acoustic axis of the TA pair (lower sheet drops linearly, β_c ≈ 0.25, C23k): TA minima are off axis at every |q|.

**Final p̄_on for WP6 (replaces v2 IF-5; v2's "Si TA 4" withdrawn and must not be used):**
| target, branch (class) | fixed-q p_on | S̄ p̄_on | threshold of S̄ (d_K ≥ Q_w) | tag |
|---|---|---|---|---|
| Si TA (G′ = 0) — **the edge** | 2 | **3** | E_g^{ren} + min_{q̂}ω_TA(Q*): on axis below the crossover \|q\| ≈ 0.8–1.0 keV [E], off axis (≳ 0.966 of the on-axis value) above | D (symmetry: allowed on and off axis); location E |
| Si LA kink (G′ = 0) | 3 on axis | **4** | E_g^{ren} + ω_LA(d_K), on axis | D (SOC = 0); SOC admixes a p̄ = 3 piece of relative weight ~2×10⁻³ [E] |
| Si TO, LO kinks (G′ = 0) | 2 | 3 | E_g^{ren} + min_{q̂}ω_ν(Q*) | D symmetry; location E |
| Si, (2̄00) class (\|q\| > 2.28 keV) | 2 (LO: 3 on axis) | 3 (TA, TO, LA); LO: 4 **if its minimum is on the axis, otherwise 3** | as above with K_pk = k_c + (2̄00) | D symmetry; location E |
| Ge, all branches | 2 | **3** | E_g^{ren} + min_{q̂}ω_ν(Q*) (TA off axis) | D (SOC = 0; SOC: D, sketch); location E |
| exciton replicas (W.14) | ½ | 3/2 (Si LA: 5/2) | lowered by E_x^b | D (Wannier–Mott) |
| shells with d_K < Q_w | — | none (mixed window + DC) | — | D |

Temperature: amplitudes T-independent (harmonic); electron factors f_v(1 − f_c) = 1 + O(e^{−E_g/T}); ω < 0 by detailed balance (WP0-v2 (4.3)); ZPR(T) moves
E_g(T), E_dir(T) and the window edge.

## M4. Resonances, window, and outside the window [D]
*E_min(q) ≡ min_{k, n occ, m emp}(ε_{m,k+q} − ε_{nk}) ≥ E_g.* d_{A,m} vanishes iff the first-order transition v → m at (q,ω) is on shell; d_{B,m} (m occupied,
path C) iff m → c at q is on shell: a generic first-order transition, not a band-crossing effect (D2 §2b's A₁-only criterion is incomplete). For ω < E_min(q):

  |d_{A,m}| (m empty), |d_{B,m}| (m occ) ≥ E_min(q) − ω;   |d_{A,m}| (m occ), |d_{B,m}| (m emp) ≥ E_g − ω_Q;   all |d| ≥ min(E_min(q) − ω, E_g − ω_max) > 0.   (M.8)

(D1 §5.1's "≥ E_min(q) − ω for all" corrected; REF-A/REF-B §2.) In Si at q folding near 0 or G, E_min ≈ 3.4 eV ≫ ω, and the E_g − ω_Q branch is the binding one.
**Window theorem [D]:** the sideband is separately computable from (M.1)–(M.4), with no i0, subtraction or counterterm, iff

  ω ≤ E_min^{ren}(q,T) − δ₀,   δ₀ ≫ max(ω_{Qν}, Γ_Λ₀, T),   applied pointwise in q,                                                         (M.9)

with renormalised energies used consistently in δ and denominators (difference O(g⁴) except at the edge). The window is a region of the (q,ω) plane, not
ω < E_dir. **No sideband–ZPL interference at O(g²) [D]:** zero- and one-phonon final states are orthogonal (different phonon occupations), at any T; D2's
non-degeneracy hypothesis is not needed for orthogonality (only for perturbation theory at resonance). The edge shell |ω − E_min| ≲ few Γ_Λ₀ is a separate
systematic (O4 d11). **Outside the window (CONVENTIONS §10):** the resonant |A₁|² is resummed by the Fan width; the split uses O4 (O4.4) (WP3v2-C13):

  Γ_Λ₀/(δω² + Γ_Λ₀²/4) = 2πδ(δω) + Γ_Λ₀ fp(1/δω²) + O(Γ²/δ²),   δω = ω − Ẽ_Λ₀,                                                            (M.10)

a Hadamard finite part (1/δω² has no principal value; D1 §5.2's "P" corrected); fp is negative against a narrow test function (WP3v2-C13a). The δ part,
summed over branches, is Γ^{(1)} × phonon branching of the hot pair, already in the ZPL (counting it again is double counting). **DC [D, O4]:**
S^{X0}_DC = Σ_Λ₀2πZ_Λ₀|ρ^{ren}_Λ₀|²δ(ω − Ẽ_Λ₀); S^{X+}_DC per Λ₊ = 2πδ(ω − E_Λ₊)|g|²[|ρ|²fp(1/δω²) + 2Re(a^{off*}ρ)PV(1/δω) + |a^{off}|²] (WP0-v2 (6.3));
inside the window DC = (M.3). (iv″a) totals invariant to O(g², Γ²/δ²) against test functions smooth on δ (Ward identity −2ImΣ = Γ̂; toy residual ∝ g^{3.97});
(iv″b) the cascade-convolved P(N_eh|q,ω) is invariant if the cascade is Markov in Λ and its first-emission kernel uses the same g, ω_Q, energies and the
Fano term 𝔉_{Λ₀,ν} = 2πΓ^{(ν)}_Λ₀[c̄ − c_ν^F], c_ν^F = Im(ρ*a^{off}_ν), Σ_ν𝔉 = 0 (WP3v2-C20); 𝔉 = 0 for PT-symmetric Si, Ge, diamond [D, sketch: PT-real gauge];
(iv″c) within 𝒞_adm(ℓ_win) the split moves by |Δw₀|/w₀ ≲ (1.1 + b_λ)Γ/δ, and FALSE universally (t → ∞ convention moves O(1)); (iv″d) code pairs obey
O4 d1–d11: one kernel (forbidden: Lorentzian ZPL + fp sideband, O(g²), T3a; Lorentzian ZPL + |δω + iΓ/2|^{-2} sideband, O(1), T3b); same g, gauge, ω_Q,
energies, Γ(ω), Z and vertex, smearing, T; first emission once (X0 seeds at (Λ₀, Ẽ_Λ₀, n_ph = 0), X+ at (Λ₊, n_ph = 1)); 𝔉 export; non-phonon widths in the
cascade only; edge shell. Si: Γ/δ₀ ≈ 0.007–0.2 at δ₀ = 0.3 eV, the value that satisfies (M.9) (δ₀ ≫ ω_max ≈ 60 meV); v2's 0.02–0.6 was at δ₀ = 0.1 eV,
where ω_Q/δ₀ ≈ 0.6 (B-4) [E]. Rigorous version needs a fibred limiting-absorption principle, a C*-dynamical limit, Coulomb stability
with dynamical lattice and an IR-safe X+ (O4 §8) [C].
**F8: size of 𝔉 in GaAs [E].** Relative to the incoherent branch weight, |𝔉_{Λ₀,ν}|/(2π|ρ|²Γ^{(ν)}/Γ_Λ₀) ≤ 2(Γ_Λ₀/δ)(|a^{off}|δ/|ρ|)|sin φ|, φ the phase of
ρ*a^{off} that PT symmetry would remove. In GaAs φ comes from the inversion-antisymmetric crystal potential (antisymmetric/symmetric pseudopotential
form factors ≈ 0.3 [UNVERIFIED, Cohen–Bergstresser]); with Γ/δ ≈ 0.01–0.5 (LO emission ~4 meV in Γ, intervalley ~50 meV above 0.3 eV [E]) and
|a^{off}|δ/|ρ| ~ 1 (b_λ), the ratio is ≲ 0.006–0.3. Since Σ_ν𝔉 = 0, 𝔉 only moves events between branches that differ in phonon energy (≤ 30 meV) and
valley. **Campaign bound: WP5-v2 (W15)** (rigorous total-variation step × [E] phase): |ΔP(N_eh|Λ₀)| ≤ 2π(Γ^{ph}/Γ^{tot})max_ν|c_ν^F|·max_{ν,ν′}|P_ν − P_ν′| ≲ 0.11Γ_Λ₀/δ,
i.e. ≲ 2×10⁻³ off the edge (Γ/δ ≈ 0.02) and up to 7×10⁻² in the O4-d11 edge shell; WP5's phase prefactor 0.3 replaces the 2|sin φ| above (AUDIT A10), and
my earlier "≲ 2×10⁻³ per bin edge" is its off-edge value. **R9 (AUDIT-2 m15; WP5-v3 (W17), IF-R8-4/5):** the campaign form uses the dimensionless,
Kramers-summed c^F (not Im(ρ*a^{off}) per branch) and the worst-case bound |ΔP| ≲ 0.3Γ_Λ₀/δ (adopted by WP6, IF6-8); the 0.11Γ/δ above is WP5-v2's value,
superseded. Inside the window there is no X0 seed and 𝔉 is irrelevant.

## M5. ZPL renormalisation and the f-sum [D]
Non-phonon cuts (D2 §2c), all interference terms inside the zero-phonon sector (not sideband–ZPL): (1) energy shift ε̃_n = ε_n + ReΣ^{FM}_nn + Σ^{AH}_nn
(δ′ term, zeroth moment unchanged); (2) Fan Z-factors (1 + ∂_zReΣ_cc + ∂_zReΣ_vv)|ρ|², ∂_zReΣ < 0; (3) band mixing 2Re(ρ*δρ^{mix}) with band-off-diagonal
Σ_{mm′}; (4) virtual-phonon vertex 2Re(ρ*δρ^V) — its unrestricted band sum is **unproven** [C] (three time orderings, phonon absorbed by another sea
electron; REF-A §2c, REF-B 2c), so state it in Kubo form; (5) norm parts = (2). SE-p, SE-h give |A₁|², |A₂|²; V gives 2ReA₁A₂*; the Hartree tadpole (T)
vanishes at equilibrium; (X) is the ionic channel (§M7). **f-sum [D]** (local H, hypothesis (L) of WP0-v2 (4.6); all-electron at every order in u):
[H_ep, n_e] = [H_AH, n_e] = 0, so

  ∫_{−∞}^{∞}dω ω S(q,ω) = π𝓃_eq²/m_e at every order in g;   𝓜₁^{SB} + Δ𝓜₁^{X0} = 0,   𝓜₁^{SB} ≡ ∫₀^∞dω ω ε₂^{PA} > 0.                       (M.11)

*Who compensates [D, aggregate]:* the AH tadpole ½⟨uu⟩:∂²V is a static local one-body potential; [[T_e,n_e],n_e†] is a c-number, so it is first-moment
neutral (its two-phonon states are O(g⁴)). At O(g²) the first-moment shift is the ω^{-2} coefficient of the proper response: (X) ~ ω^{-6} → 0, (T) = 0,
(AH) = 0, hence 𝓜₁(SE-p + SE-h + V) = 0 and the non-phonon cuts of these three give −𝓜₁^{SB} (REF-A §3). The per-diagram "cutting pair" is **withdrawn
to [C]** (SE and V are not separately conserving, Ward identity; REF-B 3b); "mainly g_cc − g_vv" is [E]. "DW" means only FC/Lamb–Mössbauer e^{−2W}, whose
linear-coupling (Fan + vertex) part carries the compensation; Σ^{AH} is never "DW" (CONVENTIONS §10). **Only first moments are compensated:** there is
no zeroth-moment rule for n_e (REF-B 3c); O4's Z_Λ₀ + (1/2π)fp∫Γ_Λ₀/δω² = 1 + O(g⁴) (WP3v2-C14) holds per pair for the **Fan part only**, the vertex term
ReΥ_Λ₀ changes |ρ^{ren}|² (CONVENTIONS §13 item 17); the soft sector has the X1 coherent-state rule (§M8). The sideband alone overshoots by 𝓜₁^{SB} =
O(⟨|g|²⟩/ΔE²) relative; L17 bounds (WP0-v2 (9.4)–(9.6)) hold for the exact L, a truncated "static ZPL + sideband" can violate first-moment bounds by
≤ 𝓜₁^{SB}, and in the window (ZPL closed) partial ≤ total holds strictly. Specs: D2-N1 (1D ring ED, λ² scaling, A₂ dropped must fail, Δ𝓜₁^{X0} = −𝓜₁^{SB}
+ O(λ⁴), AH tadpole O(μ²)), D2-N4 (bounds).

## M6. Adiabatic (Herzberg–Teller) form and DFPT [D]
Frozen-phonon transition density ρ_cv(k,q;λ_fd) = ⟨ψ_{ck′}(λ_fd)|e^{iq·r}|ψ_{vk}(λ_fd)⟩ with first-order states from g:

  ∂_λρ_cv = Σ_m[g_cmρ_mv/(ε_{ck′} − ε_{m,k+q}) + ρ_cm g_mv/(ε_{vk} − ε_{m,k+Q})] = M^{(2)}|_{ω_Q→0},  M^{(2)}_± − ∂_λρ_cv = ∓ω_QΣ_m[gρ/d²_{A,m} − ρg/d²_{B,m}] + O(ω_Q²/d³).   (M.12)

Relative error ω_Q/δ, **δ = min(E_min(q) − ω, E_g − ω_Q)** (from (M.8); D1's "distance to nearest threshold" corrected); Si ω_Q/E_g ≲ 6%; emission and absorption
coincide adiabatically, differ at O(ω_Q/δ); the form fails near the window edge. *DFPT [D]:* the Sternheimer output P_c|∂ψ_v⟩ is path B (m empty) only;
P_v|∂ψ_v⟩ = Σ_{v′}|v′⟩g_{v′v}/(ε_v − ε_{v′}) (path C) is a finite sum; |∂ψ_c⟩ (paths A, D) needs one non-SCF Sternheimer (H₀ − ε_{ck′})|∂ψ_c⟩ = −(1 − |ψ_c⟩⟨ψ_c|)∂V_SCF†|ψ_c⟩,
well conditioned in the window (ω − ω_Q < E_min(q)); degenerate valence multiplets (Si Γ₂₅′) need a gauge-covariant ρ_cv(λ_fd). But ∂V_SCF gives every g_mn,
so the SOS form (M.1) has all four paths at no extra DFPT cost (REF-A §6). Path B alone violates completeness (C1, C7). Spec D1 N-b (1D, FD vs (M.12) vs (M.1)).

## M7. Screening [D at RPA/TDH (ring) level, O(g²), harmonic, static DFPT g; X2. ALDA: one extra source, below (B-7)]
**Coulomb-line classes (WP0-v2 (5.5)):** external (q+G, ω) → (ε̃^{-1})_{G0}(q,ω) with local fields; DFPT (Q+G, ν ≈ ω_Q) → screened g, static error
**O(ω_Q²/E_g²) ≈ 3×10⁻³** (ε̃(Q,ν) even and analytic below E_g; the D2 "O(ω_Q/E_g)" is superseded, F11); pair (P+G, ω_f) → W^{scr}(P,ω_f) = ε̃^{-1}(P,ω_f)f_Hxc(P)
between two triangles (new in R3); ionic (phonon line at q mod G, D2's "X") → ionic part of ε(q,ω). The R1 claim "every Coulomb line carries q or Q" is false
(REF-A/REF-B §5); "two channels" is withdrawn (CONVENTIONS §7). Screened amplitude (X2 (2.2) = WP0-v2 (5.7)):

  M̃_± = M^{(2)}_±[ρ̃] + Σ_{GG′}ρ_cv(k,P+G)W^{scr}_{GG′}(P,ω_f)𝔗_{G′}(P),   ρ̃_mn(k,q) = Σ_G(ε̃^{-1})_{G0}(q,ω)ρ_mn(k,q+G),                    (M.13)

𝔗_G(P) = (2/V)Σ_kΣ_{ab}⟨ψ_{bk}|e^{−i(P+G)·r}|ψ_{a,k+P}⟩N_ab(k)/(ω_f − ε_{a,k+P} + ε_{bk} + i0) the second-order KS density over **all** band pairs (X2 (2.1)),
N = [ρ̃, s^{(g)}] + [g, s^{(ρ̃)}] the TDH source whose on-shell residue is (M.1) (independent rederivation of the Pauli theorem). Rate (unitarity, X2 (2.3)):

  L^{PA}(q,ω) = (8π²α/Ωq²)⟨⟨Σ_{cvν±}w^{EPW}_±|M̃_±|²δ(ε_{c,k+P} − ε_{vk} ± ω_{Qν} − ω)⟩⟩ + O(g⁴),   S^{X+}_ee = (2q²/e²)L^{PA}/(1 − e^{−βω}).     (M.14)

**TDH vs ALDA (B-7) [D].** N is the time-dependent-Hartree source: it contains f_Hxc only linearly. At ALDA the second-order effective potential is
v^{(2)}_eff(P) = f_Hxc δn^{(2)}(P) + k_xc[δn^{(1)}(q,ω)δn^{(1)}_ph(Q,ω_Q)] (the cross term of ½k_xc(δn_q + δn_Q)², coefficient 1; R9, VER-WP3-B N2), k_xc ≡ δ³E_xc/δn³ ≠ 0 (LDA: ∝ n^{-5/3}, WP3v3-C27), which adds
Σ_Gρ_cv(k,P+G)(ε̃^{-1}k_xc[δn_qδn_Q])_G to (M.13); size [E] ≲ δ_LF of the pair term. So (M.13) is [D] at RPA/TDH; "ALDA" requires that term.
**W^{scr}(P,ω_f) is retarded** (WP0-v3 G8: (3.2) order, final-pair index first): (P,ω_f) is the final pair's own energy-momentum, so ε̃(P,ω_f) is
always absorptive; the golden-rule form with |M̃|² is exact with the retarded W by the C17a identity. In the window ε̃^{-1}(q,ω) (the external line)
is non-absorptive to O(g²), so (M.14) is exact to O(g⁴) at this level and D1's H2 (ε₂ ≪ ε₁) is redundant; with G = 0 only, (M.14) is the
R1 form ε₂^{PA}/ε₁⁽⁰⁾² (SOTA #4) with ε₂^{PA} built from M̃. H1 (ω ≫ ω_LO) is needed only to drop the ionic part of ε₁ (O((m_e/M)ω_p²/ω²)). The S_ee ELF
form holds at ω ≫ ω_max to O(κ_BO⁴) (WP0-v2 (5.5)(ii)). **No double counting [D]:** removing the phonon line leaves a tree; it closes one cycle; a line
off it is a bridge (improper external chain, resummed once); on it the segments next to the ion vertices are DFPT, the middle one is the pair channel;
the classification is topological, so it holds at q → 0 (P = Q) and Q → 0 (P → q); lines inside one loop (ladder, direct W) are excitonic [C].
**Rigid-shift frame theorem [D]:** for g = u[𝔄,H], [n_e(q),𝔄] = c_𝔄 n_e(q) (c_𝔄 = iℓ_Q ê·q), 𝔄 commuting with V_ee: R^{(2)} = c_𝔄φu[R(q,ω_f) − R(q,ω)] + R^{(2)}_D (R^{(2)}_D the
response to (φn_e(q) at ω, −ω₂u𝔄 at ω₂)), so the convective part
is screened by ε(q,ω_f) to all orders in ω_Q/ω (REF-A's ε(q, ω∓ω_Q) is exact **only** for it), the −R⁰(q,ω) piece of the triangle (displaced induced
charge) cancels the pair enhancement, the intraband part δM^{intra}_f (ℓ_Q ê·m_eΔv^g) is screened at (q,ω) with its own feedback, and no 1/|ε|⁴ arises.
Coherent-potential limit: M = Uρ for all pairs ⇒ M̃ = M/ε(P,ω_f) exactly (WP3v2-C15). **Sizes [E] (X2 §6):** δ_ω ≈ 1–2% (|ε(q,ω)/ε(q,ω_f) − 1| ≤ 0.8% amplitude),
δ_LF ≈ 5–20%, δ_pair = 2Re⟨r^{pair}_f⟩ + ⟨|r^{pair}_f|²⟩ ≈ −(10–50)% (sign, c_coh ≤ 1, q-independence [C]; P ≡ k_c − k_v ≈ 0.85X pinned, |P| ≈ 1 Å⁻¹,
ε(P,ω_f) ≈ 3–4), δ_ion ≲ 10⁻⁴; **interim factor [0.4, 1.8] on L^{PA} [E/C]** until X2-N2/N3 (WP0-v2 (8.1) A-type): composition (1+δ_ω)(1+δ_LF)(1+δ_pair), δ_ω = ±2%,
δ_LF ∈ [−0.2, 0.2] (sign not derived), δ_pair ∈ [−0.5, 0.5] (sign [C], not adopted) → [0.39, 1.84] (WP3v3-C28). v2's [0.5, 1.2] assumed δ_LF ≥ 0 and
δ_pair ≤ 0 (A-V7, B-8); it is recovered as the conditional range if both signs are derived. **External weight (F1) [D]:** (ε̃^{-1})_{G0} is the
retarded out-state weight in WP0-v2 (3.2) order; with the in-state weight [(1+Rf)_{0G}]* it gives the same total Im R_00 for any target (WP3v2-C17a,b);
WP1 [E2] as printed misses the total without inversion (C17c); pair-resolved weights differ only where pairs are open at (q,ω) (C17d), never in the
PAER window, so (M.13)–(M.14) are exact for GaAs too and only out-of-window seeding is affected. **Dark photon [D]:** no new pair+phonon amplitude at O(e·g)
(an ion vertex with one u creates the phonon; one g then annihilates it or adds a second); the quadratic path is O(g⁴) in rate; ions enter only via
ε_tot in the external and pair channels: Si ≲ 10⁻⁴ (Z*(0) = 0); GaAs ε_ion ≈ −(ε₀ − ε_∞)ω_TO²/ω² ≈ 10⁻³ absolute, ≈ 10⁻⁴ relative (D2's 10⁻³–10⁻² corrected).
Bare g would overestimate the long-range |g| by ~ε_∞; 1/ε(q,ω) on g screens at the wrong momentum.

## M8. Soft acoustic limit (C7) [D under X1 H1–H4; X1 = WP0-v2 (4.9)]
Long-wave acoustic polarisation e_κν = ê(M_κ/M_cell)^{1/2}, ω_{Qν} = c_ν(Q̂)|Q|, ℓ_Q = (2M_cellω_{Qν})^{-1/2} with N outside; ASR: g_mn(k,0) = (ε_nk − ε_mk)𝔄_mn,
𝔄 = −iℓ_Qê·p, g_nn(k,0) = 0 (holds with non-local PPs moving with the ions); intraband slope g_nn(k,|Q|Q̂) = iℓ_Q|Q|Q̂·Ξ^n·ê + O(|Q|²ℓ). For c ≠ v non-degenerate:

  M^{(2)}_{cvν,±}(k,q,Q→0) = iℓ_Qρ_cv(k,q)[ê·q + (Q̂·D^c·ê ∓ c_νê·p_cc)/(Q̂·v^g_c ± c_ν) − (Q̂·D^v·ê ∓ c_νê·p_vv)/(Q̂·v^g_v ± c_ν)] + O(|Q|^{1/2}),        (M.15)

v^g_c, p_cc at k+q; v^g_v, p_vv at k; upper sign emission of −Q; index order Q̂·Ξ^n·ê (matters with non-local PPs, p ≠ m_ev^g). Lab form: interband terms give
[ρ,𝔄]_cv + (𝔄_cc − 𝔄_vv)ρ_cv = iℓ_Qê·(q − p_cc + p_vv)ρ_cv; the intraband 0/0 terms give ±iℓ_QQ̂·Ξ^n·ê/(Q̂·v^g_n ± c_ν) (WP3v2-C16); with **Ξ^n = D^n + v^g_n⊗p_nn**
(Galilean + comoving strain) the p terms cancel, giving (M.15) (WP3v2-C1a). D^n = frozen-strain deformation tensors at fixed reduced k (+ quadrupolar
non-analytic part): the only material constants; |D|/c_ν ~ 10² keV ≫ q, so they dominate the limit by ~10². **Ward identity [D]:** for any one-body s^W(Q),
𝔖 = s^W B_{Qν} + h.c.,

  M[g] = M[g′] + i⟨c,k+q+Q|[s^W, e^{iq·r}]|v,k⟩,   g′_mn(κ,Q) = g_mn + i s^W_mn(ε_nκ − ε_{m,κ+Q} ∓ ω_Q)   (on shell, unrestricted m; exact at all Q),          (M.16)

since (E_I − E_f)/(E_i − E_I) = −1 on shell even for the 0/0 terms. Comoving s^W = ℓ_Qê·½{e^{iQ·r},p}: recoil term iℓ_Q(ê·q)ρ_cv(k,q+Q) (one-phonon term of
e^{iq·u(r)}), g′ = strain + velocity coupling, giving (M.15) independently; X1's 1D model verifies (M.15) to 10⁻¹⁸, Ξ = D + v⊗p to 10⁻²⁶, (M.16) to 10⁻⁶⁰.
D1's iℓ_Q(ê·q)ρ_cv needs D = 0 and c_ν ≪ |v^g| (its "+O(ω_Q/δ)" is wrong for m = c, v, whose denominators are Q·v^g ± ω_Q); D2's iu^{zp}·(q − m_eΔv^g)ρ_cv
holds only at Q ≡ 0 (= C7e); WP0 v1 (4.9) differs by ê·(p_cc − p_vv) and agrees only at band extrema (WP3v2-C1b–d). At extrema (M.15) → iℓ_Qρ_cv ê·[q ±
(D^c − D^v)Q̂/c_ν]. Degenerate multiplet: diagonalise the O(Q) k·p splitting along Q̂; the result is a matrix in the multiplet. **C7 (code check):** evaluate
(M.1) as a function (denominators, no δ) at |Q| = 10⁻²,10⁻³,10⁻⁴ ·2π/a, ≥ 3 directions, both signs: C7a ASR + completeness at Q = 0 (tests N_m to the Bethe
ridge); C7b intraband slope Ξ^n = D^n + v^g⊗p; C7c full limit (M.15), deviation O(|Q|); C7d ∝ ρ_cv(k,q) → 0 as q → 0; C7e synthetic g = [𝔄,H], ω_Q → 0
gives D2's form (with physical g, D1's or D2's form is a bug). Off shell because the window forbids |Q| < Q_min.
**IR [D]:** on shell the intraband denominators are ZPL detunings (ω − E_cv(k,q), E_cv(k+Q,q) − ω), so in the window |Q| ≥ Q_min ≃ (E_min(q) − ω)/(v^g_max + c_ν)
(Si: ≈ 0.045 Å⁻¹ at δ₀ = 0.3 eV; 0.015 Å⁻¹ at 0.1 eV [E]): **no IR feature** at any T. Edge: ε₂^{PA} ∝ (E_min − ω)^{-1/2}, integrable [E]. Outside (ZPL open): Low-type soft theorem
M → iℓ_Q(ê·K^{soft}_±)M^{(1)}, K^{soft}_± = q + (D^cQ̂ ∓ c_νp_cc)/(Q̂·v^g_c ± c_ν) − (c → v); Adler zero ⇒ |M|²(n+1)d^dQ ∝ Q^{d−2}dQ (T = 0), Q^{d−3}dQ (T > 0):
finite in 3D, soft sideband ∝ E (T = 0) or T; 2W_soft = (Ω/(2π)³)∫dΩ_Q|ê·K^{soft}|²Q_p²/(4M_cellc_ν), UV-dominated. Cherenkov-cone poles (Q̂·v^g = ∓c_ν) are
the real cascade (Γ^{(1)} × branching), regulated by the width, finite part kept. Eikonal BN: coherent-state emission, Σ_n|⟨n|coh⟩|² = 1, soft zeroth
moment conserved within the soft sector; essential only for piezo (3D log, GaAs, where the ZPL is open), 2D at T > 0, 1D. The DW e^{−2W} contains recoil
and the deformation/Galilean parts of K^{soft}, larger by (D/c_νq)² ~ 10³–10⁴ at extrema [E]. Optical non-polar: g_nn(0) = ℓ₀d^n, no 0/0, analytic.
Fröhlich LO: the 1/Q cancels (neutral pair), finite direction-dependent limit (pair dipole + Doppler + interband polarisation). Piezo: |M|² ∝ Q^{-3},
genuine BN log, only outside the window. Si quadrupoles enter only via D^n(Q̂). **Numerics [D]:** in the window, R1 detuning-form denominators (A, m empty:
ω − E_cv-type; B, m occ: (ε_{ck′} − ε_{m,k+Q}) − ω; others energy form, bounded by E_g ∓ ω_Q), R2 zero weight at acoustic Γ and σ ≪ δ₀, R3 optional
cancellation-free (M.16) with comoving s^W (Wannier-interpolable). At the edge/outside: eikonal patch
ΔS^{PA}_patch = (4π/Ω)Ω²∫d³k/(2π)³Σ|ρ_cv|²∫dΩ_Q̂(2π)^{-3}|ê·K^{soft}_+|²E/(2M_cellc_νx_+²)Θ(0 < E/x_+ < Q_p), x_+ = Q̂·v^g_c + c_ν, E = ω − E_cv(k,q),
paired with (1 − 2W_soft); halve Q_p for stability.

## M9. Controls C1–C8
**C1, optical limit [D].** D2's exact proof: for local V and ΔV, [H, n_e(q)] = q·j_e(q), so on shell ω⟨f|n_e|i⟩ = q·⟨f|j_e|i⟩ and M^{(2)} → (q/ω)q̂·M_v (M_v = (M.1)
with ρ → v_mn incl. v^g_nn, same denominators); M^{(2)}(q = 0) = 0 (m = v in A + m = c in B; WP3v2-C11c; identically, not only on shell, since ρ(k,0) = δ: B-1); the q² cancels in (M.4):

  ε₂^{PA}(ω) = (8π²α/Ωω²)⟨⟨Σ_{cvν±}(n+½±½)|q̂·(A₁^v + A₂^v)|²δ(ε_{c,k+Q} − ε_{vk} ± ω_Q − ω)⟩⟩,  A₁^v = Σ_m g_cmv_mv/(ε_mk − ε_vk − ω),  A₂^v = Σ_m v_cmg_mv/(ε_{m,k+Q} − ε_vk ± ω_Q).   (M.17)

Cubic: q̂ → ê after the full k, Q, band sum (ε^L = ε^T, O_h); write q̂ before that step. D1's partial-fraction route divides by zero for m = v, c (the intraband
terms come from the k+q shift of ε, g, u; r_vv is gauge-dependent) and dropped its own i[g,q·r]_cv/ω term: restored. Non-local PPs: **exact** with the
generalised current, v = i[H,r] (incl. i[V_NL,r]) plus the phonon-vertex term i[g^{NL},q·r] (D2's "approximate" is wrong in kind); literature velocities
usually omit both. Prefactor confirmed in FT (§4, L9): EPW 2302.08085 Eq. (63), Noffsinger 1202.3454 Eq. (1) (SOTA amendment "from memory" closed).
**C2:** (M.1) is linear in g. **C3 [E]:** where the ZPL is open, sideband/ZPL ~ (50–100 meV/1–3 eV)² ~ 10⁻³–10⁻², larger only near the ZPL threshold.
**C4:** §M5 (with non-local PPs the C4 test needs the modified double commutator). **C5 [D]:** T = 0 threshold min_{k,k′}F ≈ E_g + ω_{Q*ν}(q) − ½(m_c+m_h)|∇ω|² (§M3 (a)). For free pairs the infimum over q is **E_g**
(acoustic Q* → 0, q ≡ k_c − k_v mod G), not E_g + ω_TA (exciton replicas start at E_x + ω_ν(Q*), possibly below E_g: AUDIT-2 m2); it lies where the window is empty, so the in-window onset is E_g^{ren} + min_{q̂}ω_TA(Q*) with |Q*| ≥ Q_w (§M3 (c)); T > 0 absorption from E_g − ω_{Q*ν} at the connecting Q* (D2's max_ν ω_Qν corrected). **C7:** §M8.
**C8, GaAs decoy (D2 flag, AMENDED):** at fixed q ≥ ω/v_max the Γ-valley ZPL opens at E_dir + q²/2(m_c* + m_h*), but q is not folded: at |q| ≈ |G₁₁₁| = 1.93 Å⁻¹
(3.8 keV) the vertical Umklapp ZPL is open at E_dir (reachable for m_χ ≳ 0.9 MeV at ω = 1.5 eV), with O(1) amplitude vs O(g) PAER; the L valley
(1.71 eV) needs |q| ≈ 0.97 Å⁻¹. A PAER-leading GaAs window can exist only at m_χ ≈ 0.4–0.9 MeV with the full q integral [E]. The window must be quoted in (m_χ, ω) after the q integration; it is restated below.

**M1 window, restated (v3) [D for the conditions; E for every number; inputs WP1-v3 [E13], [E14], IF-6, IF-6b].** A channel whose lowest final energy at
total momentum q is E^{ch}(q) is reachable at m_χ iff min_q[E^{ch}(q)/|q| + |q|/2m_χ] ≤ v_max (WP1-v3 [E13]; the minimum runs over |q|, q̂ and every G). The
pinned values of v2 (0.47, 0.708 MeV at q = Q_x + G) are upper bounds and are dropped (WP1-v3 A-12, B-13). v_max = 794.5 km/s.
- **PAER edge.** E^{PA}(q) = E_g^{ren} + min_{q̂}ω_TA(Q*) in the window: Si free pairs (continuum) m_χ^{PA} ≈ **0.337 MeV** with ω_TA(Q*₀ ≈ 0.53 Å⁻¹) ≈ 13.5 meV (0.338 with the zone-boundary TA 18 meV; the bare-gap value
  2E_g/v_max² = 0.333 MeV, E_g(0) = 1.170 eV, is not attained by free pairs); the exciton replicas (W.14) start at **≈ 0.333 MeV** (E_x + ω_TA = 1.1688 eV < E_g, since ω_TA ≈ 13.5 meV < E_x^b = 14.7 meV; the true kinematic floor of
  any channel ending in a bound exciton is 2E_x/v_max² = 0.329 MeV) (AUDIT-2 m1, m2); Ge **≈ 0.213 MeV** (floor 0.212, E_g(0) = 0.744 eV; 0.214 with 7.5 meV) (WP3v3-C29).
- **(1) Si, strictly PAER-only:** m_χ^{PA} (0.333 replica / 0.337 continuum) ≲ m_χ < m_χ^{ZP} ≈ **0.42 MeV (0.40–0.44)**, where the second-class (G = 0, on-axis forbidden) zero-phonon line first becomes
  reachable [E13]. No zero-phonon final state of any class is reachable, so every electronic event is X+ (PAER) or GS. Inside this band the reachable points
  with ω > E_min(q) − δ₀ form the edge shell (O4 d11), where the X0/X+ split moves by O(Γ/δ₀) (Si ≈ 0.007–0.2 at δ₀ = 0.3 eV [E]); elsewhere PAER is
  convention-free.
- **(2) Si, PAER coexisting with the forbidden-class zero-phonon channel:** ≈ **0.42–0.54 MeV**. Pointwise in (q,ω): below E_min(q) − δ₀ PAER is alone (window);
  above E_min(q) the zero-phonon continuum and bound lines are open but second class (|ρ_cv|² ∝ k_rel², or SOC-suppressed). There X+ lies outside (M.9) and
  is defined by the DC convention (M.10); its resonant fp/PV part carries the same forbidden vertex as the zero-phonon line, so the convention dependence there is
  O(Γ/δ) × the second-class weight [D, sketch]. Ratio ϖ_II = S^{X0}_{II}/S^{PA} ≈ 0.03–2 at the edge, 0.2–15 at ε = 0.1 eV [E14]: in m_χ, **PAER leads only up to
  ≈ 0.43 MeV; 0.43–0.54 MeV is a two-channel region with comparable rates** (ratio 10^{−1}–10^{1.5}). For IF-6b the S^{PA} at the same (q,ω) is (M.14) in the
  DC convention, computed by the §M10 recipe on the WP1 grid; interim η_PA = 10⁻³–10⁻² [E] (C3).
- **(3) Si above ≈ 0.54 MeV:** the allowed zero-phonon line (G′ = (2̄00) branch at X, WP1-v3 §3.2(c), [E13]; the referees' 0.594 MeV is the q-pinned upper bound)
  leads; PAER/ZPL ≈ 10⁻³–10⁻² (C3). The G₁₁₁ vertical transition (≳ 1.1 MeV) is irrelevant for the boundary.
- **(4) Ge:** the zero-phonon channel is **allowed** (L valley, C₃ᵥ, WP1-v3 §3.2), reachable from **≈ 0.32 MeV (0.32–0.36)** [E13]; the direct Γ valley needs ≈ 3 MeV in
  parabolic bands (WP1-v3 §R1). **Ge PAER-only window ≈ 0.213–0.32 MeV**; above, the allowed zero-phonon line leads; there is no forbidden-class coexistence band.
All numbers sit at Δq ≈ 0.15–0.37 q_BZ, beyond strict parabolicity: the boundaries are recomputed from [E13] with ab initio E_min(q) (Si along Γ–X on both sides
of X; Ge Γ–L and Γ) and the exciton dispersion (O-WP3-1). Quote the window as these four statements, never as a single "0.34–0.47 MeV".

## M10. Computable recipe and specifications [D for formulas, E for costs]
Inputs: DFT bands (PBE + scissor/GW); Wannier functions; DFPT on coarse Q → EPW g^W, ω_{Qν}, e_{κν}; **ASR enforced on g keeping its O(Q) deformation part**;
Fröhlich (polar) and **dynamical quadrupoles (also Si)** in the long-range g. Density vertex with Umklapp:

  ρ_mn(k,q) = [U†(k+q)F̃(k+q,q)U(k)]_mn,   F̃(κ,q) = Σ_R e^{−iκ·R}F^W(R,q),   F^W_ij(R,q) = ⟨w_iR|e^{iq·r}|w_j0⟩ (smooth in continuous q, decays in R),   (M.18)

F̃(κ+G) = F̃(κ), so unfolding is immaterial and Umklapp automatic. **g and F must share one gauge U(k)** (else the m sum gets random phases). **Bethe ridge:**
at |q| ≳ αm_e, Σ_m(ε_m − ε_v)|ρ_mv|² = q²/2m_e puts the weight of ρ_mv on bands q²/2m_e above (13.6 eV at 1 a.u., 54 eV at 2 a.u.), outside any 8–16-band
manifold; path A then needs ρ **and** g_cm to high bands: either (a) a plane-wave Sternheimer remainder per (k′,Q), (H − ε_{ck′})|∂ψ_c⟩ = …, contracted with
e^{iq·r}, computed on the coarse grid and interpolated as a smooth tensor (cost O(N_PW log N_PW·N_iter) per (k,q,Q)), or (b) a large disentangled manifold
reaching above q²/2m_e with an N_W convergence test; the N_W-only route is valid for q ≲ 0.5αm_e [E]. **PAW/US augmentation at all q** (else ρ_nn(k,0) ≠ 1);
all-electron reconstruction grows in importance with q. Non-local PPs enter the C1 and C4 checks, not ρ. Sampling: fixed q, (k,k′) pockets (Si: Γ valence,
six Δ valleys), Q = k′ − k − q folded; tetrahedron or σ ≪ δ₀ with σ → 0; detuning denominators (X1 R1). Convergence: coarse k 8³–12³, Q 4³–8³, pocket grids
≡ 60³–120³, N_W, N_m/Sternheimer tolerance, |q| step and angles (3D q for anisotropy), σ, ε̃ with LFE, δ₀. Cost per (q,ω):
O(N_v^{pk}N_c^{pk}[N_W³ + N_mN_νN_cN_v]) plus the remainder; total ~10¹⁰–10¹¹ flop × remainder factor, CPU [E]. **Routes (X2 §8):** P (primitive cell:
ε̃^{-1}_{G0}(q,ω), M^{(2)}[ρ̃], 𝔗 by second-order Sternheimer at (ω, ∓ω_Q), W^{scr}(P,ω_f) at the few pinned P); S (recommended: ZG/frozen-phonon supercell,
RPA local fields in the supercell basis, unfolded to unreduced q; contains every class; IP + scalar-ε run gives δ_LF + δ_pair by difference). DFPT/adiabatic
variant: (M.12) with the ω_Q/δ error bar. **Specs:** D1 N-a (Pauli, Fock space), N-b (C6/(M.12)), N-c (C1), N-d (C7 via C7a–e: C7e for the Q ≡ 0 branch, C7c
physical), N-e (ε̃ in the window); D2-N1 (ED ring, §M5), N2 (Si/GaAs window and C8 with folded q, L/X valleys), N3 (closed by L9 FT), N4 (L17 bounds with
𝓜₁^{SB}); X2-N1 (1D pair channel vs real-time TDH), N2 (Si q = 0 Route S ± local fields vs optics), N3 (Si q = 0.5, 1, 2 keV: δ_LF, δ_pair, r^{pair}(q) ≈ r^{pair}(0)?), N4
(ε̃^{-1}_{G0}); O4: Γ_Λ₀/δ map in Si (d11 shell), 𝔉 in GaAs (F8).

---
# Part II. The joint response, Migdal, absorption, ZG, bremsstrahlung, excitons

## 1. The joint response S(q; ω_ph, ω_e)
### 1.1 Definition [D]
Hypotheses: WP0-v2 (H1)–(H4); (H5) where the X0/X+ label is used (otherwise §1.6); harmonic plus perturbative anharmonicity. U = U_n ∘ U_ep: U_n the
space-adiabatic unitary of WP0-v2 §6.2 (BO order n); U_ep a Schrieffer–Wolff transformation removing O(g) intra-X scattering, which exists under (H5)
(every such process off shell). H′ = U†HU is block diagonal to O(κ_BO^{2(n+1)}, g³) (WP0-v3 G10, (6.1); [C] for the crystal limit). Write H′ = Ê_e + Ê_L, Ê_e = Σ_aε_a^{ren}|a⟩⟨a| the electronic-label energy
(constant on each block a = ground, e–h pair (c,k+P; v,k), exciton λ, core hole; ε^{ren} the AHC/ZPR-renormalised vertical label energy at T), Ê_L ≡ H′ − Ê_e
the lattice energy (phonons, nuclear recoil to all orders). Both commute with H′:

  S_ab(q;ω_ph,ω_e) ≡ (2π/V)Σ_{i,f}p_i⟨i|O′_a†|f⟩⟨f|O′_b|i⟩δ(ω_e − E^e_f + E^e_i)δ(ω_ph − E^L_f + E^L_i),   O′ = U†OU,                                (W.1)

  ∫dω_e S_ab(q; ω − ω_e, ω_e) = S_ab(q,ω) (WP0-v2 (3.1)) + O(κ_BO^{2(n+1)}, g⁴).                                                                   (W.2)

Labels are energies of the prompt final state (WP0-v2 (7.1)). Sectors: GS = {ω_e = 0}; X0 = {ω_e > 0, zero net phonon change (ω_ph = 0 at harmonic order)};
X+ = the rest. S = S^{GS} + S^{X0} + S^{X+}; GS and X = X0 ∪ X+ are restrictions by orthogonal projectors and each is Hermitian PSD; **X0 and X+ separately are
PSD only inside the window or for bins ≳ δ** (WP0-v2 §6.2 (i), O4 §9; outside, X+ contains fp and Z_Λ₀ may exceed 1). Rate:
Γ_χ = ∫d³q/(2π)³∫dω_edω_phΣ_ab𝔇_abS_ab(q;ω_ph,ω_e)δ(ω_q − ω_e − ω_ph) (WP0-v2 (3.3)); the split (ω_e, ω_ph) is the WP5 hand-over (WP0-v2 (7.3)).
**Why.** For n_e, ω_e is the e–h/exciton energy and ω_ph the phonon energy (PAER sidebands; ZPL at ω_ph = 0). For n_κ, ω_ph is the lattice recoil/multiphonon
energy and ω_e the Migdal electron energy. 2210.06490 (p. 9) calls a structure factor "that incorporates the Migdal effect directly" "practically
challenging"; (W.1) is that object, at every BO order.

### 1.3 Explicit entries at order τ_J
τ_J: n_B = leading non-adiabatic (κ_BO⁴ amplitude at the nuclear vertex); n_g = 2 at the electron vertex (one-phonon amplitude O(g)); harmonic lattice, all
orders in q·u; 𝒳 = RPA(+LFE) on every Coulomb line (WP0-v2 (5.5)); T ≪ E_g; incoherent nuclear S unless stated. Metadata scr = ext,LFE,DFPT,pair; conv = window/DC.
**(W.4) e–e.** (a) **GS:** S^{GS}_ee = δ(ω_e)Σ_{κκ′}𝓕_κ(q)𝓕*_κ′(q)S^{GS}_{κκ′}(q,ω_ph), iq·𝓕_κ ≡ ∂⟨n_e(q)⟩^{ad}/∂u_κ (DFPT; rigid-ion: atomic form factor): adiabatic
electron-following (WP0-v2 §6.2 (ii)). (b) **X0:** S^{X0}_ee = δ(ω_ph)S^{ren}_ee(q,ω_e): clamped response with AHC energies plus the O(g²) Fan-Z, mixing and vertex
terms (§M5) and the FC e^{−2W} reduction; screened with the out-state weight (WP0-v2 (7.2)); zero in the window. (c) **X+ (PAER):**
S^{X+}_ee = (4π/Ω)⟨⟨Σ_{cvν±}(n_{Qν}+½±½)f_v(1 − f_c)|M̃_±|²δ(ω_e − ε̃_{c,k+P} + ε̃_{vk})δ(ω_ph ∓ ω_{Qν})⟩⟩ = (2q²/e²)L^{PA}/(1 − e^{−βω}) (M.13)–(M.14) (renormalised energies:
the difference from WP0-v2 (5.6) is O(g⁴) in the window).
**(W.5) n_κ–n_κ, X sector (Migdal).** Leading non-adiabatic amplitude (WP0-v2 §6.2 (ii); 2505.08864 Eq. (21) [FT]):
A^{Mig}_f = Σ_{I∈κ}⟨Ψ^{vib}_f|e^{iq·R_I}(q/M_κ)·⟨a|∇_{R_I}Φ₀⟩/(E_a − E₀)|Ψ^{vib}_i⟩, ⟨a|∇_RΦ₀⟩/(E_a − E₀) = −⟨a|∇_RV|0⟩/ω_e². With ∇_{R_I}V = V^{-1}Σ_p(ip)U_κ(p)e^{−ip·R_I}n_e(p),
U_κ(p) = Z_κ(p)e²/p² (cores frozen into Z_κ(p)), resumming the (p, ω_e) Coulomb lines (WP0-v2 (5.3), R_NN) and taking T1, T2 of §2:

  S^X_κκ(q;ω_ph,ω_e) = (1/2π)Σ_{GG′}∫_BZ d³p/(2π)³ [q·(p+G)][q·(p+G′)]U_κ(p+G)U*_κ(p+G′)/(M_κ²ω_e⁴) · S^{ee}_{GG′}(p,ω_e) · S^{GS}_κκ(q−p−G, ω_ph),     (W.5)

S^{ee}_{GG′} the full screened density-response matrix (a total, not pair-resolved, so the F1 weight question does not arise for rates; pair-resolved
Migdal seeding uses the out-state weight); S^{GS}_κκ the GS lattice structure factor (WP2's "S^G", F6). δ(ω_ph) part (e^{−2W} elastic) → X0; rest → X+. Scalar
check: S^{ee} = (2p²/e²)Im[−ε^{-1}] gives S^{GS} × 4α∫d³pZ²(q·p)²Im[−ε^{-1}]/((2π)³M²ω_e⁴p²) = KKL dP/dω (WP3v2-C2b).
**(W.6) e–κ.** S^{GS}_eκ = δ(ω_e)Σ_κ′𝓕_κ′S^{GS}_{κ′κ} (Born-charge/electron-cloud interference); S^{X+}_eκ = (2π/V)Σ_fA^{PAER*}_fA^{Mig}_fδδ (Migdal–PAER interference,
nonzero for any 𝔇 with c_ec_κ ≠ 0: the Migdal one-phonon term with pair momentum P and phonon q−P lands in the PAER manifold); bounded by WP0-v2 (4.4).

### 1.4 Sum rules [D, under (L) of WP0-v2 (4.6) and τ_J]
- **(J1)** marginal (W.2). **(J2)** ∫∫(ω_e + ω_ph)(S_ab[O] + S_ba[O†])dω_edω_ph/2π = 𝓜¹_ab (WP0-v3 (4.5)–(4.6); off-diagonal pairing S_ba[O†], WP0-v3 G3).
- **(J3) Split first moments.** 𝓜¹^{(e)}_ab ≡ V^{-1}⟨[O′_a†,[Ê_e,O′_b]]⟩, 𝓜¹^{(L)} = 𝓜¹ − 𝓜¹^{(e)}. For n_κ: 𝓜¹^{(e)}_κκ = 𝓃_κq·δM_κ·q/M_κ², δM_κ ≡ 2Σ_{a≠0}Re⟨0|∇_{R_κ}V|a⟩⟨a|∇_{R_κ}V|0⟩/(E_a − E₀)³
  (Born–Huang drag mass); per nucleus E^{Mig}_1(q) ≡ ∫ω_e dP_Mig/dω_e = q·δM_κ·q/(2M_κ²). Atom: δM = N_em_e exactly (TRK to all orders in q_e; WP3v2-C4a–c). The
  lattice sees M_κ + δM_κ. **The electronic-label moment 𝓜¹^{(e)} is not the X-sector moment (R9, AUDIT-2 B3):** in the impulse regime an X (Migdal)
  event carries ω_e **and** the nuclear recoil ≈ q²/2M_κ, so per nucleus 𝓜¹_X = E^{Mig}_1 + P_Mig q²/2M_κ, while the nuclear f-sum is exact with the bare mass,
  ∫dω ωS_κκ = 𝓃_κq²/2M_κ. Hence 𝓜⁰_GS = 𝓃_κ(1 − P_Mig), 𝓜¹_GS = 𝓃_κ[(1 − P_Mig)q²/2M_κ − E^{Mig}_1] = 𝓃_κ(1 − P_Mig)q²/2(M_κ + δM_κ) + O(P_Mig δM/M,
  (δM/M)²) (WP3v3-C31; = WP5-v3 §3.1, WP5v3-C20b; WP2-v3 IF-2): **S^{GS} = (1 − P_Mig(q))·S^{GS}[M_κ → M_κ + δM_κ]**. (v2/v3's 𝓜¹^{(L)} = 𝓃_κq·[M_κ^{-1} −
  δM_κM_κ^{-2}]·q is the lattice-label moment of 𝓜¹^{(e)}'s complement, not the GS-sector moment.) Si, Ge: δM/M ≈ 2.7×10⁻⁴, 2.4×10⁻⁴ **[E]** (all electrons dragged; a PSD δM_{κκ′} bounds only its trace, Σ_{κκ′}δM = N_em_e per cell, not a
  diagonal element: B-21) [WP3v2-C9].
- **(J4) Zeroth moment, n_κ incoherent:** ∫∫(S^{GS} + S^X)dω_edω_ph/2π = 𝓃_κ: GS depleted by P_Mig(q) (10⁻⁸–10⁻⁴). For n_e no zeroth-moment rule; O4's Z + fp = 1 is per
  pair, Fan part only (§M5).
- **(J5) PAER/ZPR:** 𝓜₁^{SB} + Δ𝓜₁^{X0} = 0 as the SE-p + SE-h + V aggregate (§M5); in the joint form the X0 loss sits at ω_ph = 0, the X+ gain at ω_ph = ±ω_Q; the soft
  sector obeys the X1 coherent-state rule.
- **(J6)** S_ab(−q;−ω_ph,−ω_e) = e^{−β(ω_e+ω_ph)}S_ba(q;ω_ph,ω_e) (both labels are differences of conserved block energies); PSD at each (ω_ph, ω_e) where the labels exist.
- **(J7) Mixed split.** 𝓜¹_eκ = 0 (WP0-v2 (4.6c)) but 𝓜¹^{(L)}_eκ = −𝓜¹^{(e)}_eκ = 𝓃_κ(q²/M_κ)𝓕_κ(q) ≠ 0 (O(1/M), not κ_BO⁴-suppressed). HO/hydrogenic check: the
  electronic part is −(q²/m_A)𝓕 exactly (WP3v2-C5). The X sector of S_eκ carries ω_e-weight −𝓃_κq²𝓕_κ/M_κ, opposite to the GS Born-charge lattice weight:
  a one-signed model is wrong.
- **(J8) Third moment of the Migdal sector (F4) [D, leading BO order, T1–T2, T ≪ E_g].** Per nucleus, with ∂ ≡ q̂·∇_{R_κ},
  E^{Mig}_3(q) ≡ ∫ω_e³dP_Mig/dω_e = M_κ^{-2}Σ_{a≠0}|q·⟨a|∇V|0⟩|²/(E_a − E₀) = (q²/2M_κ²)[⟨∂²V⟩ − ∂²E₀] (second-order perturbation theory; WP3v2-C18a,b), and in
  the screened form (W.5), by KK (∫₀^∞(dω/2π)S/ω = −R(0)/2, C18c): E^{Mig}_3 = −(2M_κ²)^{-1}Σ_{GG′}∫_BZ d³p/(2π)³[q·(p+G)][q·(p+G′)]U_κU*_κ R^{ee}_{GG′}(p,0) > 0, the
  electronic-screening part of the on-site force constant; this all-electron, all-k form is the required 𝔨₃^X (WP2-v2 relay). Hence (i) WP2 (5.2) is confirmed: 𝔨₃^X = E^{Mig}_3[1 + O(𝔨₁/ω_e, ⟨ω_ph⟩/ω_e)], 𝔨₃^{GS} = (q²/2M²)⟨∂²E₀⟩,
  sum = (q²/2M²)⟨∂²V⟩ (WP2 (5.1)); (ii) link to WP0-v3 (4.7), (4.7′) (v3; WP0-v3 G5, WP2-v3 (5.2″) and IF-1): for point nuclei on cubic sites, q → 0⁺ after L → ∞,
  **𝓜³_eκ(q→0⁺) = −2𝓃_κ(M_κ/m_e)(𝔨₃^X + 𝔨₃^{GS})·[1 + 2𝓃_e/𝓃_e(R_κ)]** (WP3v3-C26a,b): the contact (trace) part ⟨∂²V⟩ = Z_κe²𝓃_e(R_κ)/3 is common
  to the κκ and eκ faces, and the eκ face alone has the uniform-density ℓ = 2 term 2𝓃_e (6∫₀^∞j₂(y)dy/y = 2), relative 1.2×10⁻⁴ in Si; at finite q the
  factor is [𝓃_e(R_κ) + Δ𝓃_κ(q)]/𝓃_e(R_κ) (WP2-v3 (5.2″); hydrogenic 1s core 1 + (q a_{1s,κ})²/10: 9% at 51 keV in Si). Contact identity:
  𝔨₃^{(eN)} ≡ (q²/2M²)⟨∂²V_eN⟩ = −(m_e/M_κ)𝓜³_eκ(q→0⁺)/(2𝓃_κ) × 𝓃_e(R_κ)/(𝓃_e(R_κ) + 2𝓃_e) (C26c; normalisation of WP0-v3 (4.5), closing IF-2).
  So J8 compares with the κκ closed form WP2 (5.2′) at every q, and with the eκ moment only at q → 0⁺ or through (5.2″); (iii) 𝔨₃^{GS}/𝔨₃^X ≈ 3M_κω̄²/(Z_κe²𝓃_e(R_κ)) ≈ 10⁻⁶ in Si (1s contact
  density) [E], so the mixed third moment measures the Migdal third cumulant. The identity needs all-electron S^{ee} (or L7a per core shell): the ω_e³ moment is
  core-dominated, and a valence-only Z_κ(p) evaluation gives only its valence part.

### 1.5 No-double-counting rules (corollaries)
- **(N1) Multiphonon + Migdal (R9, AUDIT-2 B3):** S^{GS}_κκ normalised to the bare f-sum (unit weight, mass M_κ) plus (W.5) overcounts the zeroth moment by
  𝓃_κP_Mig and 𝓜¹ by 𝓃_κ(E^{Mig}_1 + P_Mig q²/2M_κ) (the X events' electronic energy and their recoil); the consistent GS input is (1 − P_Mig)S^{GS} with mass
  M_κ + δM_κ (J3; WP5-v3 §3.1, WP2-v3 IF-2). Size [E]: δM/M ≈ 2.7×10⁻⁴ (Si); P_Mig ≈ 5×10⁻³ at E_R = 1 keV, ∝ E_R, dominant above ≈ 50 eV: ≲ 1% at keV.
- **(N2) Mixed approximations:** all four published Migdal formulas are truncations of (W.5) (§2); combining atomic valence Migdal with crystal multiphonon NR is a
  different-truncation error, not a double count.
- **(N3) Quenching data:** neutron-calibrated NR yields contain Migdal (2104.01811 [ABS]): Y_tot(E_R) = Y_casc[S^{GS}] + ∫dω_eP_casc(N_eh|ω_e)dP_Mig/dω_e; fit the sum.
  Same rule for an energy-loss term "that effectively incorporates the Migdal effect" (2209.04503, WP5): never add a WP3 Migdal rate to it.
- **(N4) PAER vs ZPR:** S^{X0,ren} + S^{X+} with consistent renormalised energies (M.9); never ZG + PAER (§5). **(N5)** measured ELF/σ₁ contain X0 + X+ (WP0-v2 §6.2 (c)).

### 1.6 Outside (H5)
Where a first-order transition is open, U_ep does not exist; the sectors are defined on H₀ (O4) and the resonant part follows the Dyson convention
(M.10), WP0-v2 (6.3): the joint S is defined with the δ part in X0 at (ω_e = Ẽ_Λ₀, ω_ph = 0) and fp/PV parts in X+ at (ω_e = ε_{ck′} − ε_vk, ω_ph = ±ω_Q); totals and
P(N_eh) are convention-independent (iv″a,b), the split moves by O(Γ/δ) (iv″c), and per-label PSD fails against narrow bins. The soft sector is IR-safe
inclusively (X1 §6.3–§6.4; §M8).

## 2. Migdal: one formula, four truncations (L7a–d)
**Chain from WP0-v2 (3.1).** T0: sector X of S_κκ, leading non-adiabatic (adiabatic part vanishes for an infinite crystal, 2505.08864 Eq. (12) [FT]).
T1: Condon (⟨a|∇_RV|0⟩ at R₀). T2: GS vibrational final states Ψ^{vib}_{a,ν′} → Ψ^{vib}_{0,ν′} (drops the e–ph displacement of the Migdal pair; error O(2W_el) ≈ 0.02, X1 §6.3).
T3: RPA(+LFE) on the (p, ω_e) lines → (W.5). T4: diagonal G = G′. T5: lattice regime K ∈ {1ph-coh, multi-inc, imp}. T6: one nucleus.
**L7c (2210.06490 [FT]).** Source: Eq. (3.3) H_eff = ω^{-2}[H_χL,[H_L,H_eL]]; Eq. (3.6) H_eff = (m_Nω²)^{-1}Σ_I∇_IH_χL·∇_IH_eL; Eq. (3.8)
dΓ/dω = (8παN_T/V³)(g_χg_N/(m_Nω²))²Σ_{q,k_e,K,Q}q·(k_e+K)q·(k_e+Q)/(q²+m_φ²)² ZZ/(|k_e+K||k_e+Q|)Im[−ε^{-1}_{KQ}(k_e,ω)]S(q−k_e−K,E) (source symbols; g_χg_N = y_χy_N, m_φ = m_V).
Amplitude: 2505.08864 Eq. (21) M_non-ad = −i(g_χg_N/(Vm_φ²Mω²))Σ_I∫du e^{iq·X_I}Ψ*Ψ q·⟨φ_n′|∇_{X_I}V_eN|φ_n⟩ [FT]. Chain T0–T4, K harmonic or anharmonic S^{GS}
(the lattice potential drops out of the double commutator). **Equivalence [D]:** (W.5) at T0–T4 is Eq. (3.8) term by term; their 1/ω² expansion (Eq. (3.2)) is
our −⟨∇V⟩/ω_e². Validity: ω_e ≫ ω_ph; T2; T ≪ E_g. Leading correction (v3; A-V14, B-17) [D free recoil; E bound]: exact intermediate energies turn (q·p/M)/ω_e² into [1/(ω′ − v_N·p) − 1/ω′],
ω′ = ω_e + p²/2M (KKL's bracket). The odd term 2v_N·p/ω_e vanishes after the p average for any time-reversal-even ELF (S(−p) = S(p); inversion not
needed). The first surviving terms are even: 2p²/(Mω_e) ≈ 3.8×10⁻⁴ under free recoil (Si, p = 5 keV, ω_e = 5 eV) and O(ω_ph²/ω_e²) ≈ 1.4×10⁻⁴ for bound
nuclei (C9b): **≲ 10⁻³**, not v2's 10⁻⁵. 2210.06490 fn. 3 states q ~ √(2m_Nω_g) with ω_g ≃ 1.2 / 0.7 eV, i.e. m_χ ≳ 250 / 320 MeV, and itself calls this
"the most conservative value" (CONFIRMED by A and B); √(2M·1.2 eV) = 251 keV (Si), √(2M·0.7 eV) = 308 keV (Ge) (C9). We **agree** with the footnote:
the EFT and the impulse formula are one function to ≲ 10⁻³ in the overlap. Next: non-Condon ∂_u⟨a|∇V|0⟩ (interferes
with PAER, (W.6)) and T2 (O(η_ep)).
**L7c, NR-EFT (2603.13052 [FT]).** Eq. (3.4) same leading term; Eq. (3.11) is (3.8) with Σ_{n,n′}ccF_{i,j}. Discrepancies: (i) Eq. (3.11) (and (4.1), the appendix and the text) prints S(q−k_e+K,…); the vertex q·(k_e+K)Z(|k_e+K|) fixes the
Coulomb-line momentum at k_e+K, so momentum conservation requires q−k_e−K (as 2210.06490 Eq. (3.8)); S is not G-periodic (Debye–Waller), so this is a
real misprint, numerically immaterial in their free-ion soft-limit evaluation (**CONFIRMED**, A-V16, B-15). (ii) **m_N misplaced between (4.6) and (4.7)
(CONFIRMED; v2's repair REFUTED, A-V15, B-16):** (4.7) dP/dω = 2αq²/(3ω⁴m_N)∫… is dimensionless as printed (WP3v3-C3a), but their (4.6)
dR/dω = (n_χN_T/(m_NM_T))∫dq∫d³v v f (dσ/dq)(dP/dω) carries one extra 1/m_N, so the printed product (4.6)×(4.7)×(4.8) equals KKL × the standard
dσ/dq = qσ̄/(2μ²v²) (C3b). The repair is to move 1/m_N from (4.6) into (4.7): then (4.7) = ½ KKL and the 2× of (4.8) dσ/dq = qσ̄/(μ²v²) compensates
(C3d). v2's "m_N → m_N² in (4.7), rate consistent" leaves a spurious 1/m_N in the rate (C3c) and is withdrawn. Whether (4.8)'s 2× is itself an error
depends on their σ̄ and F_ij normalisation (App. A, not traced): **UNRESOLVED** [E].
**L7b (2011.09496 [FT]).** Source: Eq. (3) (impulse; bracket [1/(ω − q_N·(k+K)/m_N) − 1/ω]²; F(p_i − p_f − q), Eq. (4)) and soft-limit Eq. (6)
dP/dω = 4α∫d³k/(2π)³Z_ion²(k)|v_N·k|²/(ω⁴k²)Im[−1/ε(k,ω)], v_N = q_N/m_N. Chain T0–T4, T5 = imp: S^{GS}_κκ(q−p, ω_ph) → δ(ω_ph − |q−p|²/2M) (or the Gaussian of
2210.06490 Eq. (4.9)); soft |p| ≪ q factorises dσ/dE_Ndω = (dσ/dE_N)(dP/dω) (their Eq. (1)). (W.5) → Eq. (6) with prefactor 4α exactly (C2a,b). Validity: impulse
x_R = 1 at √(2Mω̄) = 45.8 keV (Si, 40 meV), 55.8 keV (Ge, 23 meV; WP2-v3 L5) (C9); impulse onset (WP2-v2 criterion) q ≳ 2√(2Mω̄) = 91.5 keV (Si), 112 keV (Ge), i.e.
m_χ ≳ 17.3 (Si), 21.1 (Ge) MeV at the kinematic endpoint q = 2m_χv_max (v1's "50–70 MeV" referred to typical, not endpoint, q); soft |p| ≪ q; valence only (Z_ion). Leading corrections: (i) lattice binding
of S^{GS} (→ L7c); (ii) off-diagonal ε^{-1}_{GG′}, O(1) per KKL; (iii) as p → 0 the screened ion vertex must reproduce Z*_κ(ω)/ε (WP0-v2 (5.3)), missed by diagonal
Z_ion, small by the d³p measure [E]; (iv) core shells add atomic-type Migdal (L7a per shell) [D]; (v) anisotropy: cubic crystals have no ℓ = 2 ELF moment, so
the soft-limit Migdal daily modulation vanishes in Si, GaAs at that order (WP1, WP2 §8). Convention: their ELF uses the RPA "Lindhard" identity (2210.06490
fn. 4), electron-only coupling at ω_e ≫ ω_max, where ε_e = ε to O(κ_BO⁴) (WP0-v2 (5.5)(ii)).
**L7a (1707.07258 [FT]).** Source: Eq. (55) iT ≃ F_AM × Z_FI(q_e) × …; Eq. (57) Z_FI(q_e) = ∫Πd³x_iΦ*_Fe^{−iΣq_e·x_i}Φ_I; Eq. (73) q_e = m_ev_F ≃ (m_e/m_A)q_A;
rate Eqs. (91)–(92); dipole Eq. (86). Chain T0 + T6, free recoil: for one nucleus ∇_RV = −Σ_i∇_iV and ⟨n|Σ∇_iV|0⟩ = m_e(E_n − E₀)²⟨n|Σr_i|0⟩, so the (W.5)
amplitude is (m_eq/M)·⟨n|Σr|0⟩, the dipole term of Eq. (57); to all orders U_n is the Galilean boost e^{im_ev·Σr}, giving Eq. (57) [D]. Validity: sudden (σ_c ≪ 1),
impulse; isolated atom false for crystal valence (KKL), true for crystal cores with r_core ≪ bond length and binding ≫ valence bandwidth (Si 2p, Ge 3d) [E].
Corrections: other nuclei (→ L7b); boost mass O(Zm_e/M): by J3 the physical mass is M + δM = m_A for an atom (Ibe's choice), M_κ with tensor δM_κ in a crystal
(CONVENTIONS §13 item 22). Convention: Ibe's e^{−iq_e·x} is opposite to the boost e^{+im_ev·x}; |Z_FI|² unaffected.
**L7d (2205.03395 [FT]).** Source: Eq. (3.1) (virtual-phonon propagator i/((ε_i − ε_j)² − ω²_{k,α}) between the multiphonon blob and the bare vertex
−iNZ_ion4πα/(V|k+G′|²)); Eq. (3.2) (reduced q·(k+G′)/(m_N(ε_i − ε_j)²)); Eqs. (3.3)–(3.4) (incoherent harmonic Σ_nT_n, **including n = 0, T₀ = δ(E)**). Chain: (W.5) with
the nuclear inertial response as off-shell phonon exchange, (2Mω_k)^{-1}·2ω_k/(ω_e² − ω_k²) = M^{-1}ω_e^{-2}(1 + ω_k²/ω_e² + …) (C7); incoherent harmonic S^{GS};
screening imposed afterwards via the ELF (their HEG argument) = T3 at RPA. **n = 0 term X0, n ≥ 1 terms X+.** Validity: as L7c. Leading correction: keeping
the phonon pole is O(ω_ph²/E_g²) ≈ 10⁻³, the same order as the static-DFPT screening error (§M7) and the T1 non-Condon terms: **keeping it alone is not a
consistent improvement [D].** Convention: bare Coulomb vertex + ε afterwards equals (W.5) only at RPA; their (ε_i − ε_j)² is ω_e².

## 3. L8 (PAER) entry
**L8 [D].** S^{X+}_ee at n_g = 2: (W.4c) = (M.13)–(M.14); DC outside the window (§M4). Source: this campaign: D1 eq. (4) with M → M̃ (X2 (2.3)). Chain: WP0-v2 (3.1) →
Theorem D, X+ → RS perturbation theory O(g²) (M.1), Pauli theorem → four-class screening (M.13). Validity [E]: window (M.9) pointwise in q; M1 window §M9 (Si PAER-only ≈ 0.333 (replica) / 0.337 (continuum)–0.42 MeV, PAER-leading to ≈ 0.43, coexisting with the
forbidden zero-phonon channel 0.42–0.54; Ge PAER-only ≈ 0.213–0.32 MeV); onset: fixed-q p_on = 2 (3 forbidden), angle-averaged **Si p̄_on = 3** (TA edge;
LA kink 4; TO, LO 3), **Ge p̄_on = 3** (all branches), §M3 table; threshold E_g^{ren} + min_{q̂}ω_TA(Q*) with |Q*| ≥ Q_w (the optical q = 0 value is
1.170 + 0.018 eV). Leading corrections: (i) excitons (§7: onset −E_x^b ≈ 14.7 meV in Si, √ edges); (ii) O(g⁴) two-phonon
sidebands ~η_ep; (iii) anharmonic widths ~η_anh; (iv) pair channel if computed (X2-N2/N3); (v) the adiabatic HT form errs by ω_Q/δ (§M6; (M.1) is exact).

## 4. Phonon-assisted absorption (L9, L9b)
**L9 source [FT].** EPW 2302.08085 Eqs. (60)–(63) (SI): S1 = Σ_jg_{mjν}(k,q)v_{jn}(k)/(ε_{jk} − ε_{nk} − ħω + iη), S2 = Σ_jv_{mj}(k+q)g_{jnν}(k,q)/(ε_{j,k+q} − ε_{nk} + βħω_{qν} + iη),
Im ε = 2(πe²/(ε₀Ωω²))Σ∫∫|e·(S1+S2)|²Pδ (the 2 is spin; source "q" = campaign Q, S1, S2 = A₁^v, A₂^v, ε₀ = ε₀^SI). Noffsinger 1202.3454 Eq. (1) (Gaussian):
α(ω) = 2(4π²e²/(ωcn_r))(V_cellN_kN_q)^{-1}Σ|λ·(S1+S2)|²Pδ. **Chain:** L8 → q → 0 (C1, D2's commutator proof) → transverse projection (cubic ε^L = ε^T) → proper ε₂ (no
external factor): (M.17), ε₂^{PA} = (8π²α/Ωω²)⟨⟨Σ(n+½±½)|ê·(A₁^v + A₂^v)|²δ⟩⟩. EPW: 2π(e²/ε₀^SI → 4πα) = 8π²α; Noffsinger: ε₂ = αn_rc/ω gives 8π²e_G²/(ω²V). Both
match **in full text**. Discrepancies: (i) both sum j over the Wannier manifold only; completeness, [V_NL,r] and [g,r] omitted: small at q = 0, fatal at keV q.
(ii) iη, iΓ double count the first-order line outside the window; EPW says the theory "is under development"; URF answer: window + fp/DC + X1 soft structure.
(iii) Noffsinger writes matrix elements bra–ket transposed; irrelevant in |·|². Leading corrections: pair channel at (Q, ω∓ω_Q) (P = Q at q = 0; δ_pair ≈ −(10–50)%
[E]); excitons (Elliott, positive). EPW's Si result underestimates experiment by ≤ 50% (their text), consistent with a net exciton-dominated correction [C].
**L9b sources [FT].** 1608.01994 Eq. (2) ⟨n_eσv⟩ = −ImΠ/ω, Eq. (3) Π ≈ −iσ̂ω, Eq. (6) κ²_eff = κ²m⁴/[(m² − ReΠ)² + (ImΠ)²], Eq. (7) R = ρ^{-1}(ρ_DM/m)κ²_effσ₁,
Eq. (10) ALP R ≃ ρ^{-1}(ρ_DM/m)(3m_a²g²/(4m_e²e²))σ₁ (source Π = Π^γ, κ = κ_mix); 2106.12586 Eqs. (20)–(22), (35) σ₁ = ω Im ε, (38)–(39); 1412.8378 Eq. (18)
Γ_{T,L} = −κ²_{T,L}ImΠ_{T,L}/ω. **Chain:** WP0-v2 (3.5)–(3.6) at k_φ → 0. Dark photon Γ = κ_mix²m Im(−1/ε) ≡ κ²_effσ₁ (C10); σ₁ = σ₁^{X0} + σ₁^{X+} + σ₁^{GS}.
**URF content [D].** (a) For E_g^{ren} + ω_ν < m < E_dir^{ren}: σ₁ = σ₁^{X+} = mε₂^{PA}(m) of L9. (b) **Temperature transfer:** data at T_d used at T must be mapped term by
term, σ₁^{X+}(ω;T) = Σ_ν[(n_ν(T)+1)𝒜^{PA}_ν(ω − ω_ν;T) + n_ν(T)𝒜^{PA}_ν(ω + ω_ν;T)] (𝒜^{PA}_ν the T-independent branch spectra), with E_g(T) shifted by AHC; 1608.01994 uses the 77 K data
where available near the edge ("the difference between absorption at temperatures of 77 K and 4.2 K is even smaller"; CONFIRMED in FT by A). From 77 K
to mK, E_g rises by ≈ 4 meV (Varshni) and n_TA(77 K) ≈ 0.07 (C9c), so the data-driven Si rate is overestimated by O(1) only within ≈ ω_TA + few meV ≈
20–25 meV of the edge [E]. v2's "E_g rises by ≈ 50 meV, O(1) within ~0.1 eV" applies to 300 K data only and is withdrawn (A-V22, REFUTED in size).
(c) **ALP:** the vertex is tr J_e (WP0-v2 §2), not Coulomb-screened at SOC = 0 (f_xc^T-renormalised, WP0-v2 (5.3)); at SOC = 0 the spin sum of the PA amplitude
equals the velocity form, so Eq. (10) holds for X+ with the proper σ₁^{PA}; with SOC it fails at O(SOC) [D]. (d) **Scalar, new:** the LO n_e PA amplitude vanishes at
k_φ → 0 (charge conservation; (M.1) at q = 0), so it is O(k_φ); the NLO 𝒯_e row has no cancellation ([𝒯_e, H] ≠ 0): Γ^{PA}_φ = (y_φ²/2m_φ)S^{PA}_{𝒯𝒯}(0,m_φ), S^{PA}_{𝒯𝒯} =
(M.3) with ρ_mn → (𝒯_e)_mn and no Coulomb screening (2106.12586's zero-phonon finding extended to X+) [D].

## 5. Finite-T and zero-point renormalisation (L12)
**Sources [FT].** AHC 1603.06965: Eq. (157) Σ^{FM}_{nn′k}(ω) = ħ^{-1}Σ_{mν}∫dq/Ω_BZ g*g[(1−f)/(ω − ε/ħ − ω_qν + iη) + f/(… + ω_qν − iη)]; Eq. (158) finite T with n_qν;
Eq. (160) "Σ^DW" = Σ_ν∫g^{DW}_{nn′νν}(k,q,−q); Eqs. (195)–(198) rigid-ion "DW" −Σ′∫g^{2,DW}/(ε_nk − ε_mk)(2n+1) (source's "DW" = campaign Σ^{AH}, g^{AH}, the AH tadpole;
not the FC e^{−2W}). Williams–Lax/ZG 1604.02394: Eq. (1) ε₂(ω;T) = 𝒵^{-1}Σe^{−E_n/kT}⟨ε₂(ω;x)⟩_n; Eq. (3) Gaussian integral, σ²_{ν,T} = (2n+1)l_ν² (Eq. (4)); Eq. (5)
ZG displacement Δτ = (M_p/M_κ)^{1/2}Σ(−1)^{ν−1}eσ; Eq. (6) O(σ²) expansion; Eq. (24) adiabatic HBB (2n+1)δ(ε_c − ε_v − ħω), "the Dirac delta function does not contain
the phonon energy". EPW 2302.08085 Eqs. (67)–(68); ZG theory 1912.10929 [ABS].
**Chain [D]:** WP0-v2 (3.1) → X0 ⊕ X+ at n_g = 2 → adiabatic amplitudes (ω_Q/δ → 0) → **phonon energy dropped from δ**. Jointly:

  S^{WL}(q,ω;T) = ∫dω_ph S^{ad}_{X0+X+}(q;ω_ph,ω) (electronic label at the full ω) = ⟨S^{clamped}(q,ω;x)⟩_{x∼𝒩(0,σ_T)}.                                         (W.11)

O(σ²) gives AHC in X0 (adiabatic Fan + AH; their Eq. (6) → (20)) plus adiabatic HBB in X+ (Eq. (24)). ZG is a **deterministic one-configuration quadrature** of (W.11)
(not a stochastic evaluation; their Ref. 17 Monte Carlo WL is): the O(σ⁴) agreement as N → ∞ comes from the alternating signs (−1)^{ν−1} over
frequency-ordered, effectively degenerate modes (Eqs. (7)–(9)), extended to all orders by a heuristic argument (Eq. (10)); the "antithetic pair" S, −S
(Eq. (12)) removes odd orders at finite N (A-V17, B-18; v2's "antithetic sign pairing, Eqs. (7)–(8)" misattributed). The δ without ω_ph is the paper's own
declared adiabatic limit (Eq. (24) text, CONFIRMED by A and B), not an error of the paper; the URF content is its consequence at T → 0 below. Validity: harmonic, adiabatic,
any T, N → ∞; linear-coupling FC structure exact to the second moment (C6b,c), third fails (C6d). **Leading correction [D]:**

  S^{URF} − S^{WL} = Σ_{sb}|M|²[(n+1)δ(ω − E_cv − ω_Q) + nδ(ω − E_cv + ω_Q) − (2n+1)δ(ω − E_cv)] + O(ω_Q/δ)|M|²,   Δ𝓜₁ = +Σω_Q|M|² (T-independent, C6a).        (W.12)

At T = 0 the WL/ZG onset sits at E_g^{ren} instead of E_g^{ren} + ω_ν: ω_{Q*ν}(q): 18 (TA) to 58 (TO) meV in Si at q = 0, q-dependent for DM; in the Si PAER window (0.333–≈0.43 MeV, §M9; ω_max ≈ 1.4 eV at 0.4 MeV) an O(1)
rate error at the lowest masses [E]. Further: non-adiabatic AHC (Fan at ε ± ω_Q; small in Si [E]; adiabatic AHC ill-defined for Fröhlich, 1603.06965 §VIII [ABS-level]);
O(σ⁴), supercell size; at q ≠ 0 unfold at unreduced q (Route S, which then also contains the pair channel). **Hybrid (closes the PAER/ZPR double count) [D]:**
S = S^{ZG}(q,ω;T) + [S^{X+,PAER} − S^{X+,ad}_{(2n+1)}], bracket from EPW on the same g; or AHC-renormalised X0 + PAER X+. **Never ZG + PAER.**

## 6. Crystal NR bremsstrahlung (catalog-processes §12 item 4)
**Atomic source [FT].** 1607.01789 Eq. (8) (Gaussian): d²σ/dωdE_R = (4ω³E_Rm_e²|α_pol(ω)|²/(3πm_Nα))dσ/dE_R = (4α/(3πω))(E_R/m_N)|f(ω)|²dσ/dE_R,
α_pol(ω) = −(α/(m_eω²))f(ω). 1905.00046 [ABS]: Migdal dominates bremsstrahlung in atoms.
**URF derivation [D].** Hypotheses: ω_γ ≫ ω_ph; photon wavelength ≫ a; ε_T(ω_γ) real. Setup: the transverse-photon-improper part of WP0-v2 (3.6) in S_κκ; the photon
couples to the lattice dipole H_γL = −Σ_IeZ*_κ(ω)u_I·E, Z*_κ(ω) the **dynamical Born charge** (macroscopic polarisation per displacement of one nucleus at ω, others
clamped, electrons non-adiabatic). The double-commutator expansion of 2210.06490 (3.3) gives amplitude ∝ eZ*·(q/M)·ê/ω_γ, independent of the lattice potential:

  dΓ/dω_γ = ∫d³q/(2π)³∫dω_ph Σ_κ𝔇_κκ S^{GS}_κκ(q,ω_ph) (2αn_r(ω_γ)/(3πω_γ)) |Z*_κ(ω_γ)·q|²/M_κ² δ(ω_q − ω_ph − ω_γ)   (isotropic: |Z*·q|² → Z*²q²),                                        (W.13)

an equality in the measure of WP0-v2 (3.3) (B-20; v2 wrote "∝"), with hypotheses ω_γ ≫ ω_ph **and E_R ≫ ω_ph (impulse;
GaAs q ≳ 125 keV)**; the photon-labelled extension of (W.1) (lattice ω_ph; photon ω_γ; ω_e = 0). Checks: vacuum atom (n_r = 1) Z*_atom = −m_eω²α_pol/e²_G = f, v_N² = 2E_R/M reproduce
Eq. (8) (C8a,c); Z*(∞) = Z (C8b). Small ω: Z*(ω) = Z*(0) + ω²C_κ, C_κ = 2ReΣ_nd_{0n}(∂_uV)_{n0}/E_n³ (DFPT). Above the gap n_r is complex and the photon is absorbed:
photon-pole residue = bremsstrahlung; continuum belongs to X (Migdal) at relative O(v²) (transverse vs Coulomb); no double count.
**Consequences [E].** Si/Ge: Z*(0) = 0 (ASR + equivalent sublattices), rate ∝ ω⁴C², comparable to the atomic estimate (|Z*| ≈ 0.05 at 1 eV); free-atom
Kouvaris–Pradler is not a crystal upper bound. GaAs (Z* ≈ 2.1, n_r ≈ 3.6): photons for ω < E_g where Migdal is closed; probability ≈ 2.6×10⁻¹³ over 0.1–1.4 eV at
m_χ = 100 MeV, crystal/atom per photon n_rZ*²/|f(ω)|² ≈ 3×10³ at 1 eV, ∝ ω⁻⁴, band-integrated (0.1–1.4 eV) ~10⁴, i.e. **10³–10⁴×** atomic (A-V18, B-20; C9d),
~10⁻⁵ of above-gap Migdal; relevant only as a sub-gap optical channel in polar scintillators [C relevance].

## 7. Exciton–phonon replicas (G5, exciton–phonon part)
**Formula [D].** Hypotheses: BSE excitons as bosons (low density), TDA, linear e–ph. Final state: exciton λ with centre-of-mass momentum P = q+Q plus phonon ∓Q:

  M^{exc}_{λ±}(q,Q) = Σ_{λ′}g^x_{λλ′ν}(q,Q)ρ_{λ′0}(q)/(ω − E_{λ′}(q)) + Σ_{λ′}ρ_{λλ′}(q)g^x_{λ′0,ν}(Q)/(−E_{λ′}(Q) ∓ ω_{Qν}),
  S^{X+,exc}_ee(q;ω_ph,ω_e) = (2π/V)Σ_{λν±}(n_{Qν}+½±½)|M^{exc}_{λ±}|²δ(ω_e − E_λ(q+Q))δ(ω_ph ∓ ω_{Qν}),                                                           (W.14)

ρ_{λ′0}(q) = Σ_{vck}A^{λ′*}_{vck}ρ̃_cv(k,q) the screened creation vertex (out-state weight); g^x_{λλ′ν} = Antonius–Louie 1705.04245 Eq. (49) [FT]
(ΣA^{λ*}A^{λ′}g_{cc′}(k+Q,q) − ΣA^{λ*}A^{λ′}g_{v′v}(k,q)); g^x_{λ′0} = ΣA^{λ′*}g_cv (pair creation by a phonon, path B/Z-graph); ρ_{λλ′} the exciton–exciton density vertex.
The second family is the excitonic image of paths B–D; the unrestricted-sum theorem carries over if the λ′ sums are complete [C]. (W.14) **replaces** (W.4c) near the edge.
**Wannier–Mott limit [D].** |M_λ|² = Ω|φ_λ(0)|²|M_free(k_c,k_v)|² (Elliott): replicas at E_x(P_c) ± ω_ν; (ω − E_x ∓ ω_ν)^{1/2} per exciton band (p_on = ½) instead of
the free-pair power 2; Sommerfeld-enhanced continuum (×1.3–2 near the Si edge, WP1). Si E_x^b ≈ 14.7 meV, Ge ≈ 4 meV [E, memory]; the window onset moves down by E_x^b.

## 8. Gap closures and specifications [E for costs]
**G2 (phonon-assisted edge).** S = S^{X0,ren} (AHC + §M5) + S^{X+} ((W.4c) with M̃) in the window, or the §5 hybrid; outside, DC (§M4). Route P/S and parameters: §M10.
Outputs: S(q,ω;T), ℛ(T)/ℛ(0) per (N_eh, q) bin; joint density of (E_e, E_h | q, ω) and (n_ph, ω_ph) for WP5; DC seeds and 𝔉 (non-PT targets); nuisance increments
Δ^τ_k for δ_pair (A-type), excitons, ZPR (E-type) per WP0-v2 (8.1); p_on. Cost 10¹⁰–10¹¹ flop plus remainder and ZG supercells (4³–6³, RPA-LFE); CPU.
**G6 (Migdal consistency).** (W.5) with J3/J4/J7/J8 and N1–N3, one code path for L7a–d: (i) all-electron RPA+LFE S^{ee}_{GG′}(p,ω_e) (GPAW, Yambo, BerkeleyGW),
p up to 30 keV, cores via Z_κ(p) or explicit shells; (ii) S^{GS}_κκ from phonopy (incoherent recursion for q ≫ 1/a, coherent one-phonon below; anharmonic optional,
WP2); (iii) the convolution, exact impulse bracket where |q·p|/Mω_e > 10⁻², p-grid 50³ per shell; (iv) validate δM_κ (J3) and E^{Mig}_3 (J8) against independent DFPT
sums, P_Mig ≤ 10⁻³; (v) neutron calibration with neutron scattering lengths (2210.04917). Outputs: S^X(q;ω_ph,ω_e) for Si/Ge, quenching-subtraction kernel,
T2/LFE band. ≈ 10³ CPU-h.
**G5 (exciton–phonon).** (W.14): finite-momentum BSE at P in the pocket set (Si P ≈ 0.85X), EPW g on the same U(k), g^x by 1705.04245 Eq. (49), ~10³ k per pocket
(a_x ≈ 5 nm); practical route Wannier–Mott × EPW M_free. Remaining gap: converged finite-P BSE for Si/Ge never done; ≈ 10⁴ CPU-h.
**Bremsstrahlung.** (W.13): Z*_κ(ω) by frequency-dependent DFPT (Sternheimer at ±ω; QE/ABINIT), n_r from KK of ε₂, S^{GS} from phonopy; output dℛ/dω_γdω_ph; negligible cost.

## 9. WP0 defects reported in v1: status
All six are applied in WP0-v2 (closing table there): v1-1 (4.9) → X1 (#5); v1-2 (5.7) truncation → (5.7)/(5.7′) (#9); v1-3 L7d split (#28); v1-4 S_eκ X+ any c_ec_κ ≠ 0 and
J7 sign (#16); v1-5 boost mass (#15); v1-6 ZG deterministic (#29). No new WP0-v2 defect found; consistency notes in §12.

## 10. Status
| Item | Tag |
|---|---|
| (M.1)–(M.4) amplitude, Pauli theorem, rate (thermal factor once, w^{EPW}_±); (M.6)–(M.7) | D (P1–P5); REFEREED R2, R7 (STANDS / applied) |
| (M.8)–(M.9) window, no interference; (M.10), DC, O4 (iv″a–d) | D (REFEREED R7: STANDS); rigorous version C |
| §M3 onset: fixed q (min F), angle average with anisotropy (M.7a), polar cap, symmetry table | D (parabolic pockets; C4v/C3v characters, SOC = 0); locations E |
| §M5 f-sum, aggregate compensation; per-diagram claim; δρ^V unrestricted sum | D; C; C |
| (M.12) adiabatic form, DFPT paths | D |
| (M.13)–(M.14) screening, topology, frame theorem; F1 weight; retarded W^{scr}(P,ω_f) | D (RPA/TDH); ALDA k_xc term D, size E; sizes E; δ_pair, δ_LF signs C; envelope [0.4, 1.8] E/C |
| (M.15)–(M.16) soft limit, Ward identity, IR, C7a–e | D (X1 H1–H4); off-shell control only |
| C1 (M.17) incl. FT prefactor; C5, C8 | D; C8 window E |
| M1 window (§M9) | conditions D; numbers E (WP1-v3 [E13], [E14]) |
| (W.1)–(W.2), sectors; (W.4)–(W.6) | D (H1–H5; T1–T4); remainder O(κ_BO^{2(n+1)}), crystal limit C |
| J3 (atom exact; Si/Ge numbers E), J7, J8 (with the 2𝓃_e term) | D (leading BO); ratios E |
| L7a–d; 2603.13052 (3.11), (4.6)/(4.7) CONFIRMED, (4.8) UNRESOLVED; L7c correction ≲ 10⁻³ | D (C2, C3); E (bound) |
| L9 prefactor (CONFIRMED); L9b T-transfer (77 K); 𝒯_e PA channel | D; sizes E |
| L12 (W.11)–(W.12), hybrid | D (C6); Si impact E |
| (W.13) bremsstrahlung (equality) | D; sizes E (10³–10⁴× atomic); relevance C |
| (W.14) exciton replicas | D (BSE-boson); completeness C |
| F8 bound on 𝔉 (WP5 (W15)) | E |

## 11. Contested corrections
None against CORRECTIONS.md. One referee statement is rebutted in part (§R1); referee disagreements are settled in §R2.

## R1. Rebuttals (go back to the named referee)
**To REF-B (§3, item B-12(a)): "q̂ ∥ K̂ is a local maximum of the Si TA threshold along every azimuth."** True for |q| > |K_pk| (REF-B's parametrisation
d = |q| − |K|), false in general. Derivation (WP3v3-C23d): with |Q*|² = d_K² + |q||K_pk|ϑ² + O(ϑ⁴), ϑ_Q ≃ |q|ϑ/d_K and c = c₀(1 + γ_cϑ_Q²),
E^{PA}_th = c₀d_K + c₀(|q|/d_K)(γ_c|q| + |K_pk|/2)ϑ² for both |q| > |K_pk| and |q| < |K_pk|. The axis is a minimum iff γ_c > −|K_pk|/(2|q|). REF-B's −½ is the
|q| = |K_pk| value. With the Si γ_c ∈ [−0.96, −0.78] (C23f,g) the axis is a **minimum for |q| ≲ 0.52|K_pk| ≈ 1.0 keV** in linear elasticity, and below ≈ 0.8 keV with the TA dispersion (dispersive criterion of §M3 (b),
C23l; crossover ≈ 0.8–1.0 keV [E]); whether this covers the low-mass end of the M1 window (|q| ≈ 0.9 keV at 0.34 MeV) is **not established** (R9: VER-WP3-B N1).
The exact-geometry scan (linear dispersion) confirms an on-axis minimum at |q| = 0.5|K_pk| and an off-axis one at 1.3|K_pk| (C23i).
REF-B's conclusion p̄_on = 3 is unaffected: on the axis TA is symmetry-allowed (C24f), off it the vertex is generic.

## R2. Referee disagreements, settled
1. **Si TA edge and LA kink (main item).** REF-A: TA allowed and LA forbidden on the axis (C4v), so edge 3 and LA kink 4, with the minimum on axis because
   c_ν is stationary on a C4v axis. REF-B: anisotropy moves the TA minimum off axis (p̄ = 3), the valence shear coupling allows TA on axis, LA minimum on axis,
   LA vertex not addressed. **Settled [D, C24; E, C23]:** the selection rules are derived from characters computed from the diamond geometry (C24a–g), not
   from memorised tables: on the axis, G′ = 0, LA (Δ₁) is forbidden and TA, TO, LO allowed — **REF-A is right on the vertices**. Stationarity is not
   sufficient for a minimum (criterion (M.7a)); the TA axis is a maximum above a crossover |q| ≈ 0.8–1.0 keV [E] — **REF-B is right on the TA location for |q| near |K_pk|**, and
   neither is complete (§R1). The LA minimum is on the axis at every |q| (γ_LA > 0, C23j; REF-B), where the LA vertex vanishes (REF-A) and grows ∝ ϑ off it, so
   the **LA kink is p̄ = 4** (C23c). Final values for WP6: §M3 table (Si edge 3, LA kink 4, TO/LO 3; (2̄00) class LO 4 if its minimum is on axis, else 3; Ge 3).
2. **Size of the fixed-q threshold shift.** REF-A ~ m*c² ≈ 0.1–1 meV; REF-B "O(mc²) ~ μeV". Settled by C25a: −½(m_c + m_h)c² = 0.14 meV (TA), 0.29 meV (LA)
   in Si: REF-A's order. The exponent is unaffected (both agree).
3. **Pair-screening envelope.** REF-A: multiplicative, [0.4, 1.2] or [0.4, 1.8]; REF-B: additive, [0.5, 1.7]. Settled: the factors compose multiplicatively
   ((1 + δ_LF)(1 + δ_pair) at the |M̃|² level is not the sum when |δ_pair| ~ 0.5); with neither sign derived the envelope is [0.39, 1.84] → **[0.4, 1.8]** (C28):
   REF-A's composition; the brief's "wider envelope" is adopted.
4. **Status of (M.13) at ALDA.** REF-A: STANDS at RPA/ALDA; REF-B: [D] only at RPA. Settled for **REF-B**: the source N is TDH; ALDA adds a k_xc term
   (§M7, C27). REF-A accepted the topology without re-deriving the source.
5. **δ₀ in the numerical examples.** Raised by REF-B only; REF-A checked Q_w at δ₀ = 0.1 eV. (M.9) requires δ₀ ≫ ω_max, so **REF-B is right**: numbers are
   quoted at δ₀ = 0.3 eV with the δ₀ = 0.1 eV values kept beside the ω_Q/δ₀ ≈ 0.6 caveat.
6. **Bremsstrahlung (W.13).** REF-A: STANDS [E]; REF-B: not closed while written "∝". Settled for **REF-B**: the equality with the measure of WP0-v2 (3.3) and the
   impulse hypothesis are now stated; REF-A's ω⁻⁴ scaling is adopted for the ratio.
7. **L7c correction size.** REF-A 2p²/(Mω_e) ≈ 4×10⁻⁴; REF-B ω_ph²/ω_e² ≈ 1.4×10⁻⁴ and ≲ 10⁻³. Not in conflict: the first is the free-recoil term, the second
   the bound-lattice one; quoted together as ≲ 10⁻³ (C9b).

## 12. Interface flags
| # | Owner / user | Quantity | v2 | v3 | Action |
|---|---|---|---|---|---|
| IF-5 **CHANGED** | WP6 (3.3), O6-2; AUDIT A1 | angle-averaged onset exponent p̄_on | Si TA edge 4, LA kink 3; "3 generic, 4 on a vertex zero" | **Si edge 3 (TA), LA kink 4, TO/LO 3; (2̄00) class LO 4 if on-axis minimum, else 3; Ge 3 all branches**; fixed q 2 (3 forbidden); threshold min_{q̂}ω_TA(Q*) with \|Q*\| ≥ Q_w; no exponent on shells d_K < Q_w | WP6 must not adopt "Si TA 4"; replace its bullets by the §M3 table |
| IF-8 **CHANGED** (= WP1-v3 IF-6, IF-6b) | WP6, M1/SOTA, LIMITS L8 | M1 window | Si PAER-only 0.34–0.47 MeV; exciton 0.472/0.708 MeV | Si PAER-only 0.333 (replica) / 0.337 (continuum)–≈0.42; PAER-leading to ≈ 0.43; two-channel 0.43–0.54; allowed ZPL above ≈ 0.54; Ge PAER-only ≈ 0.213–0.32 MeV [E] | WP6 edges and m_min tables; SOTA M1 statement; S^{PA} on WP1's grid specified (§M9 (2)) |
| IF-10 **NEW** | WP0 (8.1), WP6 nuisances | interim pair-screening factor on L^{PA} (A-type) | [0.5, 1.2] | **[0.4, 1.8] [E/C]**, multiplicative composition | WP6 prior range |
| IF-11 **NEW** | WP0-v3 (5.6), F7; WP6 | thermal factor | ÷(1 − e^{−βω}) with (n+½±½) weights in L^{PA} | L^{PA} with w^{EPW}_± (EPW (64)); S = (2q²/e²)L/(1 − e^{−βω}) exact | none numerically (O(e^{−E_g/T})); agrees with WP0-v3 F7 |
| IF-12 **NEW** | WP0-v3 G8, X2, WP5 seeding | W^{scr}(P,ω_f); (M.13) level | [D at RPA/ALDA] | RPA/TDH; ALDA k_xc source; W retarded | WP5 pair-resolved seeding uses the retarded W |
| IF-2 **CHANGED** (WP0-v3 G5; WP2-v3 IF-1) | WP2, WP0 | 𝓜³_eκ(q→0) vs 𝔨₃ | J8(ii) contact form | × [1 + 2𝓃_e/𝓃_e(R_κ)] (q → 0⁺), finite q via WP2 (5.2″); normalisation of WP0-v3 (4.5); F4 closed at the 10⁻⁴ level on WP3's side | none further; J8 test only all-electron, all-k (W.5) |
| IF-13 **NEW** | WP2-v2 (J3 users), WP0 (N1) | δM_κ/M_κ Si, Ge | "upper bounds" 2.7, 2.4×10⁻⁴ | [E] estimates | wording |
| IF-14 **NEW** | LIMITS L9b, WP6 (dark photon / ALP near the edge) | 1608.01994 near-edge overestimate | O(1) within 0.1 eV | O(1) within ≈ 20–25 meV (77 K data) | LIMITS L9b text |
| IF-15 **NEW** | LIMITS L7c, SOTA | 2603.13052 (4.6)/(4.7) | "m_N → m_N² in (4.7)" | m_N misplaced between (4.6) and (4.7); (4.8) UNRESOLVED | LIMITS text |
| IF-16 | WP0-v3 G10, G3 | Theorem D remainder; off-diagonal moment pairing | O(κ_BO^{n+1}); S_ab[O†] | O(κ_BO^{2(n+1)}); S_ba[O†] | applied here (§1.1, J2) |
| IF-1, IF-3, IF-4, IF-6, IF-7, IF-9 | as v2 | external weight; S^{GS}; 𝔉 bound; WP5 seeds; F11; controls texts | — | unchanged | none |

## 13. Closing table (R7 referee items)
| Item | Verdict | Action | Where |
|---|---|---|---|
| A-V1 | STANDS | kept | §M2 |
| A-V2 | SWC (thermal factor twice) | applied | (M.3), (M.4), (M.14), (W.4c); C21a–c |
| A-V3 | STANDS | kept | §M4 |
| A-V4 | STANDS | kept | (M.10) |
| A-V5 | STANDS | kept | §M5 |
| A-V6 | STANDS (RPA/ALDA) | kept; tag narrowed to RPA/TDH per B-7 (§R2.4) | §M7 |
| A-V7 | SWC ([0.5, 1.2] not an envelope) | applied: [0.4, 1.8], composition and signs stated | §M7; C28; IF-10 |
| A-V8 | STANDS | kept | §M8 |
| A-V9 | SWC (threshold = min F) | applied | §M3 (a); C25 |
| A-V10 | SWC (c_ν stationarity) | applied, strengthened to the curvature criterion (M.7a) | §M3 (b), (e); C23d–k |
| A-V11 | FALLS (Si TA 4, LA 3) | applied: replaced by the derived C4v table (TA 3, LA 4) | §M3 (d), table; §3; IF-5; C24 |
| A-V12 | SWC (polar cap; ω_TA(Q)) | applied | §M3 (c); C30c |
| A-V13 | STANDS | kept | §2 |
| A-V14 | SWC (≈ 4×10⁻⁴; fn. 3 wording, inputs) | applied | §2 L7c; C9 |
| A-V15 | misprint CONFIRMED; repair REFUTED | applied (repair replaced; v2 repair dropped) | §2 L7c; C3a–d |
| A-V16 | (3.11) CONFIRMED; (4.8) UNRESOLVED | applied (kept; (4.8) marked UNRESOLVED) | §2 L7c |
| A-V17 | SWC (ZG mechanism) | applied | §5 |
| A-V18 | STANDS [E] | kept; ω⁻⁴ scaling added | §6; C9d |
| A-V19 | STANDS | kept; updated for WP0-v3 G5 | J8; C26 |
| A-V20 | STANDS | kept | §M7, §11 of v2 (F1) |
| A-V21 | CONFIRMED | kept | §4, §M9 C1 |
| A-V22 | REFUTED in size | dropped; replaced by the 77 K statement | §4 L9b(b); C9c; IF-14 |
| A-V23 | SWC (notation) | applied | §16 |
| A-V24 | STANDS | kept | §8 |
| B-1 | STANDS (C11c stronger than claimed) | kept; noted: the q = 0 cancellation is identical, not only on shell | §M2 |
| B-2 | SWC (thermal factor) | applied | as A-V2 |
| B-3 | STANDS | kept | (M.5)–(M.7) |
| B-4 | SWC (δ₀ inconsistent with (M.9)) | applied: δ₀ = 0.3 eV | §M3 (c), §M4, §M8; C30b |
| B-5 | STANDS | kept | (M.10) |
| B-6 | STANDS | kept | §M5 |
| B-7 | SWC (TDH, not ALDA; retarded W) | applied | §M7; C27; IF-12 |
| B-8 | SWC ([0.5, 1.2] conditional) | applied (wider envelope, §R2.3) | §M7; C28 |
| B-9 | STANDS (caveat: off-shell control) | kept; caveat applied | §M3 (d) |
| B-10 | STANDS | kept | §M3 (a) |
| B-11 | SWC (anisotropic c_ν in C23) | applied | §M3 (b), (e); C23d–k |
| B-12 | FALLS (Si TA 4) | applied (p̄ = 3); (a) rebutted in part for \|q\| < 0.52\|K_pk\| | §M3; §R1; C23i, C24 |
| B-13 | SWC (Q_w with consistent δ₀, longitudinal masses) | applied | §M3 (c); C30 |
| B-14 | STANDS | kept | §2 |
| B-15 | CONFIRMED | kept | §2 L7c |
| B-16 | CONFIRMED, package diagnosis corrected | applied | §2 L7c; C3 |
| B-17 | CONFIRMED / SWC (≲ 10⁻³) | applied | §2 L7c; C9b |
| B-18 | CONFIRMED (characterisation; "antithetic" misnomer) | applied | §5 |
| B-19 | CONFIRMED | kept | §4 |
| B-20 | SWC ((W.13) equality, impulse hypothesis, 10³–10⁴) | applied | §6 |
| B-21 | SWC (J3 bounds not derived) | applied ([E]) | J3; C9; IF-13 |
| B-22 | STANDS | kept; G5 term added | J8 |
| B-23 | STANDS | kept | F1 |
| B-24 | STANDS | kept | throughout |
| B §9 (checks) | C3 incomplete; C19/C23 blind to c_ν(Q̂); C14b near-tautological; C9 labels; no thermal or TDH check | applied: C3a–d, C23d–k, C21a–c, C27 added; C9 relabelled; C14b kept but marked as bookkeeping (C14a carries the content) | code/WP3-v3/checks.py |

**Counts (48 items):** applied 26 (A: V2, V7, V9, V10, V11, V12, V14, V15, V16, V17, V23 and the updates to V18, V19; B: 2, 4, 7, 8, 11, 12, 13, 16, 17,
18, 20, 21 and the update to B-22); kept (STANDS/CONFIRMED) 21; dropped 1 (A-V22; within A-V15 the v2 repair is also dropped); rebutted 1, in part (B-12(a), §R1),
without changing B-12's conclusion. The v2 closing table (69 rows, returns/R6/WP3-v2.md §13) remains applied in full.

## 13b. R9 clean-up (VER-WP3-A/B, AUDIT-2 rows addressed to WP3)
| Item | Content | Action | Where |
|---|---|---|---|
| VER-B N1 | (M.7a) linear-dispersion only; dispersive criterion γ_ω > −(\|K_pk\|/2\|q\|)·v_gd_K/ω₀(d_K) | applied; crossover ≈ 0.79 keV self-consistent (0.85 with r frozen), quoted ≈ 0.8–1.0 keV [E]; "covers the low-mass end" dropped (not established) | §M3 (b), (e), table; §R1; §R2.1; §0; C23l,m |
| VER-B N2 | ALDA cross term coefficient 1, not ½ | applied | §M7 |
| VER-A F1 / AUDIT m1 | 0.333 MeV is the replica / bare-gap value, not the free-pair edge | applied: 0.333 (replica) / 0.337 (continuum, ω_TA ≈ 13.5 meV); Ge 0.213 | §0, §M9, §3, IF-8; C29b |
| VER-A F2 | (2̄00)-class LO 4 needs an on-axis LO minimum | applied: "4 if on axis, otherwise 3" | §M3 table, §R2.1, IF-5 |
| VER-A F3 | J8 2𝓃_e factor and ALDA k_xc not verified by A | noted (AUDIT-2 l.161 confirms J8 = WP0 (4.7′) = WP2 (5.2″) exactly) | J8 |
| AUDIT B3 (blocking) | Migdal/GS bookkeeping: 𝓜¹_X = E^{Mig}_1 + P_Mig q²/2M_κ; GS = (1 − P_Mig)S^{GS} with M_κ + δM_κ | applied (matches WP5-v3 §3.1, WP2-v3 IF-2) | J3, N1; C31a–c |
| AUDIT m2 | E_g is not a floor for exciton replicas (E_x + ω_TA < E_g) | applied | §M3 (c), §M9 C5, §M9 window; C29b |
| AUDIT m3 | WP6 wording on WP3's 0.333 | no WP3 change (WP3 already separates replica/continuum) | — |
| AUDIT m15 | Fano term: Kramers-summed c^F, worst case 0.3Γ/δ (WP5-v3 (W17)) | applied | §M4 F8 |
| AUDIT m18 | Ge x_R = 1 at 55.8 keV (23 meV) | applied | §2 L7b; C9e |
| AUDIT m19 | Si M_x 1.41 vs 1.19 m_e | applied: Q_w ≈ 0.31–0.33 Å⁻¹, both [UNVERIFIED] | §M3 (c), §0; C30d |
| AUDIT m27 | 𝒫_± collides with projectors | renamed **w^{EPW}_±** throughout | (M.4), (M.14), §16 |
| AUDIT L7c, L8, L9b, L12 rows; IF-2/5/8/10–16 | wording and values already as in v3 | no change needed (verified) | §2, §3, §4, §5, §12 |
| AUDIT m31 | NOTATION rows for K_pk, d_K, Q_w, p̄_on, γ_c, E^{PA}_th | requested (+ γ_ω, r, w^{EPW}_±) | §16 |
Checks after R9: 114, all PASS (C23l,m, C29b, C30d, C9e, C31a–c added).

## 14. Open items handed on
O-WP3-1 ab initio E_min(q) and exciton dispersion for the window boundaries (Si Γ–X both sides of X; Ge Γ–L, Γ), with S^{PA} on WP1's (q,ω) grid for [E14];
O-WP3-2 finite-P BSE for Si (G5); O-WP3-3 DFPT values of δM_κ, E^{Mig}_3, C_κ for Si, Ge, GaAs; O-WP3-4 rigorous (H5)-free labels (O4 §8); O-WP3-5 WP1 to
confirm the ALP/SOC statement of L9b(c); O-WP3-6 𝔉 in GaAs and Ge and the Γ_Λ₀/δ₀ map in Si (F8, d11); O-WP3-7 X2-N2/N3 (δ_LF, δ_pair signs) to narrow
[0.4, 1.8]; O-WP3-8 δρ^V unrestricted sum (§M5) or its Kubo replacement; O-WP3-9 ab initio phonon dispersion for the location of the TA/optical minima
(§M3 (e)) and the SOC admixture of the Si LA kink; O-WP3-10 the ALDA k_xc pair term (§M7).

## 15. Literature
R7 ratings (full text read by the referees): **CONFIRMED** — 2603.13052 Eq. (3.11) sign misprint and the (4.6)/(4.7) m_N misplacement; 2210.06490 Eq. (3.8),
fn. 3 (inputs 1.2/0.7 eV, "most conservative") and the p. 9 quote; 1604.02394 Eq. (24) and its adiabatic-limit text, Eqs. (5)–(12) as re-described in §5;
EPW 2302.08085 Eqs. (60)–(64) and the two verbatim quotes; 1607.01789 Eq. (8); 1608.01994 use of 77 K data near the edge. **REFUTED** (dropped) — v2's
reading of 1608.01994 as a 300 K-based overestimate within 0.1 eV; v2's repair of 2603.13052 (4.7). **UNRESOLVED** — whether 2603.13052 Eq. (4.8)'s 2× is an
error (σ̄ normalisation). Not re-rated in R7 (FT for v1, algebra re-derived by both referees under V13/B-14): 1707.07258, 2011.09496, 2505.08864,
2205.03395, 1202.3454, 1412.8378, 2106.12586, 1603.06965, 1705.04245. ABS/title only: 1912.10929, 1905.00046, 2104.01811, 2210.04917, 2209.04503 (via WP5).
Via owner returns: 1509.01598, 2101.08275 (WP1). UNVERIFIED: Cohen–Bergstresser GaAs form factors (§M4); Si/Ge elastic constants (standard values,
used only for [E] locations); the Δ/Λ compatibility tables are not used as input (derived, C24).

## 16. Symbols introduced/used
NOTATION v4 and CONVENTIONS throughout; all symbols of v2 §16 are used as defined there. **v3 deviations fixed (A-V23):** v2's K (pocket-pair vector) collided
with NOTATION's regime label K → **K_pk**; v2's E_th(q̂) collided with NOTATION's detection threshold → **E^{PA}_th(q̂)**; v2's θ (near θ_k, nuisances) → **ϑ**.
**Introduced here (new, no collision; NOTATION rows requested):** **K_pk** ≡ k_c − k_v + G; **d_K(|q|)** ≡ ||q| − |K_pk||; **ϑ, ϑ_Q** (polar angles of q̂ and Q̂*
from K̂_pk); **E^{PA}_th(q̂)**; **p̄_on** (onset exponent of the angle-averaged S̄; p_on is NOTATION's fixed-q exponent); **Q_w** (window radius in |Q*|); **γ_c**
(quadratic anisotropy coefficient of c_ν about an axis); **β_c** (linear (conical) coefficient); **C^{el}_{11}, C^{el}_{12}, C^{el}_{44}** (elastic constants; C_κ is
taken); **w^{EPW}_±** (EPW thermal weight; R9 rename of v3's 𝒫_±, AUDIT-2 m27); **γ_ω(Q)**, **r(d_K)** ≡ v_gd_K/ω₀(d_K) (dispersive anisotropy, R9); **k_xc** ≡ δ³E_xc/δn³ (second-order xc kernel); **m_χ^{PA}** (PAER kinematic edge mass). From WP1-v3: m_χ^{ZP}, q^{ZP}, ϖ_II,
η_PA, ε̄_PA. Kept from v2: E^{Mig}_3(q), M^{exc}_{λ±}, 𝒜^{PA}_ν(ω;T). Irrep labels Δ₁, Δ₂′, Δ₅, Λ₁, Λ₃, Γ₁₅, Γ₂₅′ are BSW labels (as WP1-v3).
Labels: (M.1)–(M.18), (M.7a) (Part I), (W.n), J1–J8, N1–N5, T0–T6, WP3v2-Cn, WP3v3-Cn, IF-n, O-WP3-n, R1, R2.
