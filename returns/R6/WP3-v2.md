# R6 / WP3-v2: the mixed electron–lattice sector of the URF, with the consolidated M1 (PAER) theory

Revision agent, brief R6/REV-WP3. Supersedes returns/R5/WP3.md (v1, historical record). Standalone: Part I is the complete M1 theory
(D1 ⟂ D2 as corrected by REF-A/REF-B and SOTA R2, X1, X2, O4), so the M1 paper can be written from it alone; Part II is the corrected v1.
Conventions: CONVENTIONS.md; symbols: NOTATION v4; architecture: returns/R6/WP0-v2.md, cited "WP0-v2 (s.n)". Checks: `code/WP3-v2/checks.py`
(sympy only, exact; 66 checks, all PASS, 10 s), cited WP3v2-Cn; C1–C10 keep their v1 meaning. Tags: **[D]** derived (hypotheses stated),
**[D, sketch]**, **[E]** estimated, **[C]** conjectured; literature **[FT]** full text (read for v1), **[ABS]**, **[UNVERIFIED]**. Labels of other
returns carry their prefix (CONVENTIONS §14). Equations: (M.n) Part I; (W.n) Part II (v1 numbers kept). Status: CLAIMED, pending R×2.

---
## 0. What changed, and results in brief
| v1 | v2 | change (source) |
|---|---|---|
| §3 "PAER, with X1, X2 integrated" (1 page) | Part I §M1–§M10 | full M1 theory with every R2/X1/X2/O4 correction (brief) |
| §1.1 "each sector PSD"; §1.6 outside (H5) [C] | §1.1, §1.6 | per-sector PSD only in the window or bins ≳ δ; DC convention + O4 (iv″) (WP0-v2 §6.2) |
| (W.4c) S^{X+} = (2q²/e²)L^{PA} | (W.4c) | ÷(1 − e^{−βω}) (CORRECTIONS §9, F7) |
| (W.5) external weight | (W.5), §M7 | out-state retarded (ε̃^{-1})_{G0}; rates unaffected (F1, WP3v2-C17) |
| J1–J7 | J1–J8 | new J8: Migdal third moment = WP2 κ₃^X, linked to WP0-v2 (4.7) (F4, WP3v2-C18) |
| — | §M4 | Fano term 𝔉 in GaAs bounded (F8) |
| — | §M3 | PAER onset exponent p_on for WP6 (WP6 O6-2) |
| symbols (G, S^G, n(ω), S exciton, W_e, χ_f, τ_e, Δ, M¹, n_e) | NOTATION v3 | GS, S^{GS}, n_r, λ, E^{Mig}_1, Ψ^{vib}_f, 𝒯_e, v_N·p / E_cv, 𝓜¹, 𝓃_e |
| WP0 v1 citations | WP0-v2 | (4.9), (5.5)–(5.7′), (6.1)–(6.3), (7.1)–(7.3), (9.7) |

**Results.** (1) **M1 [D]:** the PAER response S^{X+}_ee = (2q²/e²)L^{PA}/(1 − e^{−βω}) with the fully screened amplitude M̃ (M.13)–(M.14), the
unrestricted-band amplitude (M.1), the window (M.9) and, outside it, the Dyson convention with O4's invariance theorems (§M4); soft limit (M.15);
f-sum compensation as a first-moment aggregate (§M5); computable recipe (§M10). (2) **Joint response S_ab(q;ω_ph,ω_e) [D]** with exact marginal and
sum rules J1–J8; two new as far as found: the Migdal ω_e-moment equals the Born–Huang drag mass (J3), the electronic part of the e–N first moment is
−(q²/m_A)𝓕 (J7); J8 closes F4. (3) **Migdal family [D]:** L7a–d are truncations of (W.5); 2603.13052 Eq. (4.7) misprinted. (4) **L9 [D]** prefactor in FT;
L9b T-transfer; phonon-assisted 𝒯_e scalar channel. (5) **L12 [D]:** ZG = deterministic Williams–Lax quadrature with ω_ph dropped from δ.
(6) **Crystal NR bremsstrahlung [D]** (W.13). (7) **Exciton–phonon replicas [D]** (W.14). Corrections: 68 applied, 0 contested (§13); flags §12.

---
# Part I. M1: the phonon-assisted electronic response (PAER)

## M1. Set-up [D]
Hypotheses (P1) BO, harmonic phonons, linear e–ph coupling (the O(u²) AH vertex g^{AH} enters only the ZPL, §M5); (P2) KS/QP independent pairs
(screening at RPA/ALDA level, §M7; excitons beyond, §7 and [C]); (P3) T ≪ E_g; (P4) spin-independent vertex, no SOC (with SOC drop the spin 2, sum
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

  S^{PA}(q,ω) = (4π/Ω)⟨⟨Σ_{cvν±}(n_{Qν}+½±½)|M^{(2)}_±|² δ(ε_{c,k+q+Q} − ε_{vk} ± ω_{Qν} − ω)⟩⟩   (proper, unscreened; screened: M → M̃, §M7),     (M.3)

  ε₂^{PA}(q,ω) = (e²/2q²)(1 − e^{−βω})S^{PA} = (8π²α/Ωq²)⟨⟨Σ(n+½±½)|M^{(2)}_±|²δ(…)⟩⟩ ≡ D2 (2.2) (WP3v2-C22a).                                  (M.4)

The zero-phonon analogue (8π²α/Ωq²)N^{-1}Σ_k|ρ_cv|²δ is Adler–Wiser (e²_G = α). D2's script docstring πe²/(q²V) is per spin (WP3v2-C22b; script not edited).
Rate per DM particle Γ_χ = ∫d³q/(2π)³|Ṽ|²S(q,ω_q), |Ṽ|² = πσ̄_eF_DM²/μ_χe² (WP0-v2 (9.1)); per unit target mass (WP0-v2 (3.4)) with 𝒢 = ∫d³vf_χδ(ω − ω_q):

  dℛ/dω = (ρ_χ/m_χρ_T)(πσ̄_e/μ_χe²)∫d³q/(2π)³ F_DM² 𝒢(q,ω) S(q,ω),   (I) angle-averaged S: 𝒢 → η(v_min)/(2q),        (M.5)
  dℛ/dω = (ρ_χσ̄_e/(4πm_χρ_Tμ_χe²)) ∫q dq F_DM² η(v_min) S̄(q,ω)   (D1's η/q and 1/(2π) owe a factor 2; WP3v2-C12a,b).                              (M.6)

Zero-phonon limit: S^{(1)} = 4π∫_BZ d³k/(2π)³Σ_{cv}|ρ_cv(k,q)|²δ(ω − ε_{c,k+q} + ε_{vk}); with ∫d³q′ = Σ_{G′}∫_BZ d³k′ (6) becomes the Bloch rate

  dℛ^{(1)}/dω = (ρ_χσ̄_eαm_e²/(m_χρ_TΩμ_χe²))∫dq q^{-2}ηF_DM²|f_crys|²,  |f_crys|² = Ωq³S̄^{(1)}/(4παm_e²) = (2π²/(αm_e²Ω))Σ_{cv}∫∫(Ωd³k/(2π)³)(Ωd³k′/(2π)³)Σ_{G′}qδ(q − |k′−k+G′|)|ρ_cv|²δ(…),   (M.7)

= 1509.01598 Eqs. (17), (21) and 2101.08275 Eq. (16) (WP1 [E12]; WP3v2-C12c; D1's 4π²/2πα corrected). **Onset (WP6 O6-2) [D, parabolic pockets]:** at T = 0
the emission branch opens at E_g^{ren} + ω_{Q*ν}, Q* = k_c − k_v − q mod G (q-dependent); k and k′ are independent pockets, so S^{X+} ∝ (ω − E_g^{ren} − ω_{Q*ν})^{p_on},
p_on = 2 if M̃ ≠ 0 at the pockets, 3 if it vanishes linearly (symmetry-forbidden) (WP3v2-C19), ½ per exciton band with (W.14); at T > 0 the absorption
branch starts at E_g − ω_{Q*ν} with weight n_{Q*ν}. **Angle-averaged S̄^{X+}(|q|,ω) (WP6 (3.3); AUDIT A1) [D for an isolated quadratic minimum; vertex
zeros E].** At fixed |q| the threshold E_th(q̂) = E_g^{ren} + ω_{Q*ν}(q̂) moves with q̂; per pocket pair, Q* = K − q with K ≡ k_c − k_v + G, so |Q*|² = (|q| − |K|)² +
2|q||K|(1 − cos θ), θ = ∠(q̂, K̂): for acoustic branches the minimum over q̂ is at q̂ ∥ K̂, |Q*|_min = d(|q|) ≡ min_K||q| − |K||, and E_th = E_g^{ren} + c_ν d +
c_ν|q||K|θ²/(2d) + O(θ⁴) is an **isolated quadratic minimum** (one per valley and K; WP3v2-C23a). WP1 [E10] (2D angular measure): S̄ ∝ ∫θdθ(ω − E_th(θ))^{p}
∝ (ω − E_th,min)^{p+1}, and (ω − E_th,min)^{p+2} if |M̃|² ∝ θ² on the minimising direction (C23b,c). Results, with E_th(|q|) = E_g^{ren} + ω_TA(Q*_min):
(i) **acoustic Q* → 0 direction**, d → 0 (|q| → |K|): threshold → E_g (the infimum over q is E_g, reached only at |q| = |K|, q̂ ∥ K̂); there E_min(q) → E_g and the
window is **empty**: in the window E_min(q) − ω ≥ δ₀ requires d ≳ Q_w ≡ (2(m_c + m_h)δ₀)^{1/2} (Si: ≈ 0.2 Å⁻¹ for δ₀ = 0.1 eV [E]), so the in-window onset is
E_g^{ren} + c_TA d ≥ E_g^{ren} + c_TA Q_w; shells |q| within Q_w of |K| belong to the edge shell (DC, O4 d11; no PAER-only exponent). (ii) **TA pocket (lowest
branch, d ≥ Q_w):** p̄_on = 3 (fixed-q 2, +1) if M̃ ≠ 0 on q̂ ∥ K̂; **p̄_on = 4** if it vanishes there. For Si TA with Q* ∥ K ∥ valley axis the deformation
coupling Q̂·Ξ·ê = Ξ_u(Q̂·k̂)(k̂·ê) vanishes for ê ⊥ Q̂ [E], so the Si S̄ edge is p̄_on = 4 at E_g^{ren} + c_TA d, with a p̄_on = 3 kink at the LA threshold
E_g^{ren} + c_LA d. (iii) **TO/LO pockets:** each branch adds a kink at E_g^{ren} + min_{q̂}ω_{Q*ν} (a generic interior minimum on the |Q*| sphere, quadratic):
p̄ = 3, or 4 on a vertex zero. Symmetry-forbidden pockets (fixed-q 3): p̄ = 4 or 5. Excitons (fixed-q ½, (W.14)): p̄ = 3/2, or 5/2. At q → 0 (optics) the
TA threshold is the zone-boundary value E_g + 18 meV (Si); for DM it is E_g^{ren} + ω_TA(Q*_min(|q|)), q-dependent. Temperature: amplitudes T-independent (harmonic); electron factors f_v(1 − f_c) = 1 + O(e^{−E_g/T});
ω < 0 by detailed balance (WP0-v2 (4.3)); ZPR(T) moves E_g(T), E_dir(T) and the window edge.

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
cascade only; edge shell. Si: Γ/δ ≈ 0.02–0.6 [E]. Rigorous version needs a fibred limiting-absorption principle, a C*-dynamical limit, Coulomb stability
with dynamical lattice and an IR-safe X+ (O4 §8) [C].
**F8: size of 𝔉 in GaAs [E].** Relative to the incoherent branch weight, |𝔉_{Λ₀,ν}|/(2π|ρ|²Γ^{(ν)}/Γ_Λ₀) ≤ 2(Γ_Λ₀/δ)(|a^{off}|δ/|ρ|)|sin φ|, φ the phase of
ρ*a^{off} that PT symmetry would remove. In GaAs φ comes from the inversion-antisymmetric crystal potential (antisymmetric/symmetric pseudopotential
form factors ≈ 0.3 [UNVERIFIED, Cohen–Bergstresser]); with Γ/δ ≈ 0.01–0.5 (LO emission ~4 meV in Γ, intervalley ~50 meV above 0.3 eV [E]) and
|a^{off}|δ/|ρ| ~ 1 (b_λ), the ratio is ≲ 0.006–0.3. Since Σ_ν𝔉 = 0, 𝔉 only moves events between branches that differ in phonon energy (≤ 30 meV) and
valley. **Campaign bound: WP5-v2 (W15)** (rigorous total-variation step × [E] phase): |ΔP(N_eh|Λ₀)| ≤ 2π(Γ^{ph}/Γ^{tot})max_ν|c_ν^F|·max_{ν,ν′}|P_ν − P_ν′| ≲ 0.11Γ_Λ₀/δ,
i.e. ≲ 2×10⁻³ off the edge (Γ/δ ≈ 0.02) and up to 7×10⁻² in the O4-d11 edge shell; WP5's phase prefactor 0.3 replaces the 2|sin φ| above (AUDIT A10), and
my earlier "≲ 2×10⁻³ per bin edge" is its off-edge value. Inside the window there is no X0 seed and 𝔉 is irrelevant.

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

## M7. Screening [D at RPA/ALDA (ring) level, O(g²), harmonic, static DFPT g; X2]
**Coulomb-line classes (WP0-v2 (5.5)):** external (q+G, ω) → (ε̃^{-1})_{G0}(q,ω) with local fields; DFPT (Q+G, ν ≈ ω_Q) → screened g, static error
**O(ω_Q²/E_g²) ≈ 3×10⁻³** (ε̃(Q,ν) even and analytic below E_g; the D2 "O(ω_Q/E_g)" is superseded, F11); pair (P+G, ω_f) → W^{scr}(P,ω_f) = ε̃^{-1}(P,ω_f)f_Hxc(P)
between two triangles (new in R3); ionic (phonon line at q mod G, D2's "X") → ionic part of ε(q,ω). The R1 claim "every Coulomb line carries q or Q" is false
(REF-A/REF-B §5); "two channels" is withdrawn (CONVENTIONS §7). Screened amplitude (X2 (2.2) = WP0-v2 (5.7)):

  M̃_± = M^{(2)}_±[ρ̃] + Σ_{GG′}ρ_cv(k,P+G)W^{scr}_{GG′}(P,ω_f)𝔗_{G′}(P),   ρ̃_mn(k,q) = Σ_G(ε̃^{-1})_{G0}(q,ω)ρ_mn(k,q+G),                    (M.13)

𝔗_G(P) = (2/V)Σ_kΣ_{ab}⟨ψ_{bk}|e^{−i(P+G)·r}|ψ_{a,k+P}⟩N_ab(k)/(ω_f − ε_{a,k+P} + ε_{bk} + i0) the second-order KS density over **all** band pairs (X2 (2.1)),
N = [ρ̃, s^{(g)}] + [g, s^{(ρ̃)}] the TDH source whose on-shell residue is (M.1) (independent rederivation of the Pauli theorem). Rate (unitarity, X2 (2.3)):

  L^{PA}(q,ω) = (8π²α/Ωq²)⟨⟨Σ_{cvν±}(n_{Qν}+½±½)|M̃_±|²δ(ε_{c,k+P} − ε_{vk} ± ω_{Qν} − ω)⟩⟩ + O(g⁴),   S^{X+}_ee = (2q²/e²)L^{PA}/(1 − e^{−βω}).     (M.14)

In the window ε̃^{-1}(q,ω) is non-absorptive, so (M.14) is exact to O(g⁴) at this level and D1's H2 (ε₂ ≪ ε₁) is redundant; with G = 0 only, (M.14) is the
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
ε(P,ω_f) ≈ 3–4), δ_ion ≲ 10⁻⁴; **interim factor [0.5, 1.2] on L^{PA}** until X2-N2/N3 (WP0-v2 (8.1) A-type). **External weight (F1) [D]:** (ε̃^{-1})_{G0} is the
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
(Si: ≈ 0.015 Å⁻¹ [E]): **no IR feature** at any T. Edge: ε₂^{PA} ∝ (E_min − ω)^{-1/2}, integrable [E]. Outside (ZPL open): Low-type soft theorem
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
with ρ → v_mn incl. v^g_nn, same denominators); M^{(2)}(q = 0) = 0 (m = v in A + m = c in B; WP3v2-C11c); the q² cancels in (M.4):

  ε₂^{PA}(ω) = (8π²α/Ωω²)⟨⟨Σ_{cvν±}(n+½±½)|q̂·(A₁^v + A₂^v)|²δ(ε_{c,k+Q} − ε_{vk} ± ω_Q − ω)⟩⟩,  A₁^v = Σ_m g_cmv_mv/(ε_mk − ε_vk − ω),  A₂^v = Σ_m v_cmg_mv/(ε_{m,k+Q} − ε_vk ± ω_Q).   (M.17)

Cubic: q̂ → ê after the full k, Q, band sum (ε^L = ε^T, O_h); write q̂ before that step. D1's partial-fraction route divides by zero for m = v, c (the intraband
terms come from the k+q shift of ε, g, u; r_vv is gauge-dependent) and dropped its own i[g,q·r]_cv/ω term: restored. Non-local PPs: **exact** with the
generalised current, v = i[H,r] (incl. i[V_NL,r]) plus the phonon-vertex term i[g^{NL},q·r] (D2's "approximate" is wrong in kind); literature velocities
usually omit both. Prefactor confirmed in FT (§4, L9): EPW 2302.08085 Eq. (63), Noffsinger 1202.3454 Eq. (1) (SOTA amendment "from memory" closed).
**C2:** (M.1) is linear in g. **C3 [E]:** where the ZPL is open, sideband/ZPL ~ (50–100 meV/1–3 eV)² ~ 10⁻³–10⁻², larger only near the ZPL threshold.
**C4:** §M5 (with non-local PPs the C4 test needs the modified double commutator). **C5 [D]:** T = 0 threshold E_g + ω_{Q*ν}(q) (§M3). The infimum over q is **E_g**
(acoustic Q* → 0, q ≡ k_c − k_v mod G), not E_g + ω_TA; it lies where the window is empty, so the in-window onset is E_g^{ren} + c_TA Q*_min(|q|) ≥ E_g^{ren} + c_TA Q_w; T > 0 absorption from E_g − ω_{Q*ν} at the connecting Q* (D2's max_ν ω_Qν corrected). **C7:** §M8.
**C8, GaAs decoy (D2 flag, AMENDED):** at fixed q ≥ ω/v_max the Γ-valley ZPL opens at E_dir + q²/2(m_c* + m_h*), but q is not folded: at |q| ≈ |G₁₁₁| = 1.93 Å⁻¹
(3.8 keV) the vertical Umklapp ZPL is open at E_dir (reachable for m_χ ≳ 0.9 MeV at ω = 1.5 eV), with O(1) amplitude vs O(g) PAER; the L valley
(1.71 eV) needs |q| ≈ 0.97 Å⁻¹. A PAER-leading GaAs window can exist only at m_χ ≈ 0.4–0.9 MeV with the full q integral [E]. **Si window:** the ZPL at
q ≡ k_c − k_v (≈ 1 Å⁻¹) is open at E_g for m_χ ≳ 0.5 MeV; the G₁₁₁ vertical transition needs m_χ ≳ 1.1 MeV (coordinator estimate), so the PAER-only window
m_χ ≈ 0.34–0.47 MeV survives pending the Umklapp re-check; the zero-phonon indirect exciton opens at 0.472 MeV (v_max = 794.5 km/s) but is symmetry-forbidden (q ∥ [100],
(δk)²-suppressed), the allowed Umklapp exciton at 0.708 MeV (WP1 §3.2–§3.4). The window must be quoted in (m_χ, ω) after the q integration.

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
(every such process off shell). H′ = U†HU is block diagonal to O(κ_BO^{n+1}, g³). Write H′ = Ê_e + Ê_L, Ê_e = Σ_aε_a^{ren}|a⟩⟨a| the electronic-label energy
(constant on each block a = ground, e–h pair (c,k+P; v,k), exciton λ, core hole; ε^{ren} the AHC/ZPR-renormalised vertical label energy at T), Ê_L ≡ H′ − Ê_e
the lattice energy (phonons, nuclear recoil to all orders). Both commute with H′:

  S_ab(q;ω_ph,ω_e) ≡ (2π/V)Σ_{i,f}p_i⟨i|O′_a†|f⟩⟨f|O′_b|i⟩δ(ω_e − E^e_f + E^e_i)δ(ω_ph − E^L_f + E^L_i),   O′ = U†OU,                                (W.1)

  ∫dω_e S_ab(q; ω − ω_e, ω_e) = S_ab(q,ω) (WP0-v2 (3.1)) + O(κ_BO^{n+1}, g⁴).                                                                   (W.2)

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
S^{X+}_ee = (4π/Ω)⟨⟨Σ_{cvν±}(n_{Qν}+½±½)|M̃_±|²δ(ω_e − ε̃_{c,k+P} + ε̃_{vk})δ(ω_ph ∓ ω_{Qν})⟩⟩ = (2q²/e²)L^{PA}/(1 − e^{−βω}) (M.13)–(M.14) (renormalised energies:
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
- **(J1)** marginal (W.2). **(J2)** ∫∫(ω_e + ω_ph)(S_ab + S_ab[O†])dω_edω_ph/2π = 𝓜¹_ab (WP0-v2 (4.5)–(4.6)).
- **(J3) Split first moments.** 𝓜¹^{(e)}_ab ≡ V^{-1}⟨[O′_a†,[Ê_e,O′_b]]⟩, 𝓜¹^{(L)} = 𝓜¹ − 𝓜¹^{(e)}. For n_κ: 𝓜¹^{(e)}_κκ = 𝓃_κq·δM_κ·q/M_κ², δM_κ ≡ 2Σ_{a≠0}Re⟨0|∇_{R_κ}V|a⟩⟨a|∇_{R_κ}V|0⟩/(E_a − E₀)³
  (Born–Huang drag mass); per nucleus E^{Mig}_1(q) ≡ ∫ω_e dP_Mig/dω_e = q·δM_κ·q/(2M_κ²). Atom: δM = N_em_e exactly (TRK to all orders in q_e; WP3v2-C4a–c). The
  lattice sees M_κ + δM_κ: 𝓜¹^{(L)}_κκ = 𝓃_κq·[M_κ^{-1} − δM_κM_κ^{-2}]·q (WP0-v2 §6.2 (iii)). Si, Ge: δM/M ≤ 2.7×10⁻⁴, 2.4×10⁻⁴ (upper bounds) [WP3v2-C9].
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
  sum = (q²/2M²)⟨∂²V⟩ (WP2 (5.1)); (ii) link to WP0-v2 (4.7): its q → 0 limit is 𝓜³_eκ = −(𝓃_κq²/(m_eM_κ))⟨∂²V_eN⟩; for point nuclei on cubic sites ⟨∂²V_NN⟩ = 0
  (∇²(1/r) = 0 off site, ℓ = 2 cancels), so **𝓜³_eκ(q→0) = −2𝓃_κ(M_κ/m_e)(𝔨₃^X + 𝔨₃^{GS})**; (iii) 𝔨₃^{GS}/𝔨₃^X ≈ 3M_κω̄²/(Z_κe²𝓃_e(R_κ)) ≈ 10⁻⁶ in Si (1s contact
  density) [E], so the mixed third moment measures the Migdal third cumulant. The identity needs all-electron S^{ee} (or L7a per core shell): the ω_e³ moment is
  core-dominated, and a valence-only Z_κ(p) evaluation gives only its valence part.

### 1.5 No-double-counting rules (corollaries)
- **(N1) Multiphonon + Migdal:** S^{GS}_κκ normalised to the bare f-sum plus (W.5) overcounts 𝓜¹ by exactly 𝓃_κq·δM_κ·q/M_κ² (≤ 3×10⁻⁴) and the zeroth moment by P_Mig.
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
our −⟨∇V⟩/ω_e². Validity: ω_e ≫ ω_ph; T2; T ≪ E_g. Leading correction [D free recoil, E bound]: exact intermediate energies turn (q·p/M)/ω_e² into
[1/(ω′ − v_N·p) − 1/ω′], ω′ = ω_e + p²/2M (KKL's bracket); the relative correction 2v_N·p/ω_e is odd in p and vanishes after the angular average for an
inversion-symmetric ELF; the first surviving term is O(v_N²p²/ω_e², ω_ph²/ω_e²) ≈ 10⁻⁵ (Si, q = 100 keV, p = 5 keV, ω_e = 5 eV; v_N·p/ω_e = 3.8×10⁻³, C9). Their fn. 3
bound q ≲ √(2Mω_g) = 242 keV (Si), 301 keV (Ge) is therefore conservative: EFT and impulse formula are one function. Next: non-Condon ∂_u⟨a|∇V|0⟩ (interferes
with PAER, (W.6)) and T2 (O(η_ep)).
**L7c, NR-EFT (2603.13052 [FT]).** Eq. (3.4) same leading term; Eq. (3.11) is (3.8) with Σ_{n,n′}ccF_{i,j}. Discrepancies: (i) Eq. (3.11) prints S(q−k_e+K,…);
momentum conservation requires −K (as 2210.06490). (ii) Eq. (4.7) dP/dω = 2αq²/(3ω⁴m_N)∫… has the wrong dimension; with m_N → m_N² it is ½ of KKL's
4αq²/(3m_N²ω⁴) (C3a); their Eq. (4.8) dσ/dq = qσ̄/(μ²v²) is 2× the standard qσ/(2μ²v²) (CONVENTIONS §9), so the rate is consistent (C3b) [E: assumes σ̄ standard].
**L7b (2011.09496 [FT]).** Source: Eq. (3) (impulse; bracket [1/(ω − q_N·(k+K)/m_N) − 1/ω]²; F(p_i − p_f − q), Eq. (4)) and soft-limit Eq. (6)
dP/dω = 4α∫d³k/(2π)³Z_ion²(k)|v_N·k|²/(ω⁴k²)Im[−1/ε(k,ω)], v_N = q_N/m_N. Chain T0–T4, T5 = imp: S^{GS}_κκ(q−p, ω_ph) → δ(ω_ph − |q−p|²/2M) (or the Gaussian of
2210.06490 Eq. (4.9)); soft |p| ≪ q factorises dσ/dE_Ndω = (dσ/dE_N)(dP/dω) (their Eq. (1)). (W.5) → Eq. (6) with prefactor 4α exactly (C2a,b). Validity: impulse
x_R = 1 at √(2Mω̄) = 45.8 keV (Si, 40 meV), 58 keV (Ge, 25 meV) (C9); impulse onset (WP2-v2 criterion) q ≳ 2√(2Mω̄) = 91.5 keV (Si), 112 keV (Ge), i.e.
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
Theorem D, X+ → RS perturbation theory O(g²) (M.1), Pauli theorem → four-class screening (M.13). Validity (Si) [E]: window (M.9); m_χ ≈ 0.34–0.47 MeV (§M9);
onset: infimum E_g over q (window empty there); in the window E_g^{ren} + ω_TA(Q*_min(|q|)) (§M3; the optical q = 0 value is 1.170 + 0.018 eV); fixed-q p_on = 2,
angle-averaged p̄_on = 4 (TA vertex zero on the valley axis [E]; 3 otherwise), §M3. Leading corrections: (i) excitons (§7: onset −E_x^b ≈ 14.7 meV in Si, √ edges); (ii) O(g⁴) two-phonon
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
term, σ₁^{X+}(ω;T) = Σ_ν[(n_ν(T)+1)𝒜^{PA}_ν(ω − ω_ν;T) + n_ν(T)𝒜^{PA}_ν(ω + ω_ν;T)] (𝒜^{PA}_ν the T-independent branch spectra), with E_g(T) shifted by AHC; 1608.01994 uses 300 K
and 77 K data; at mK the absorption branch vanishes and E_g rises by ≈ 50 meV, so the data-driven Si rate is overestimated near the edge [E: O(1) within ~0.1 eV].
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

O(σ²) gives AHC in X0 (adiabatic Fan + AH; their Eq. (6) → (20)) plus adiabatic HBB in X+ (Eq. (24)). ZG is a **deterministic one-configuration quadrature** of (W.11),
exact to O(σ⁴) as N → ∞ by antithetic sign pairing (Eqs. (7)–(8)); not a stochastic evaluation (their Ref. 17 Monte Carlo WL is). Validity: harmonic, adiabatic,
any T, N → ∞; linear-coupling FC structure exact to the second moment (C6b,c), third fails (C6d). **Leading correction [D]:**

  S^{URF} − S^{WL} = Σ_{sb}|M|²[(n+1)δ(ω − E_cv − ω_Q) + nδ(ω − E_cv + ω_Q) − (2n+1)δ(ω − E_cv)] + O(ω_Q/δ)|M|²,   Δ𝓜₁ = +Σω_Q|M|² (T-independent, C6a).        (W.12)

At T = 0 the WL/ZG onset sits at E_g^{ren} instead of E_g^{ren} + ω_ν: ω_{Q*ν}(q): 18 (TA) to 58 (TO) meV in Si at q = 0, q-dependent for DM; in the 0.34–0.47 MeV window (ω_max ≈ 1.4 eV at 0.4 MeV) an O(1)
rate error at the lowest masses [E]. Further: non-adiabatic AHC (Fan at ε ± ω_Q; small in Si [E]; adiabatic AHC ill-defined for Fröhlich, 1603.06965 §VIII [ABS-level]);
O(σ⁴), supercell size; at q ≠ 0 unfold at unreduced q (Route S, which then also contains the pair channel). **Hybrid (closes the PAER/ZPR double count) [D]:**
S = S^{ZG}(q,ω;T) + [S^{X+,PAER} − S^{X+,ad}_{(2n+1)}], bracket from EPW on the same g; or AHC-renormalised X0 + PAER X+. **Never ZG + PAER.**

## 6. Crystal NR bremsstrahlung (catalog-processes §12 item 4)
**Atomic source [FT].** 1607.01789 Eq. (8) (Gaussian): d²σ/dωdE_R = (4ω³E_Rm_e²|α_pol(ω)|²/(3πm_Nα))dσ/dE_R = (4α/(3πω))(E_R/m_N)|f(ω)|²dσ/dE_R,
α_pol(ω) = −(α/(m_eω²))f(ω). 1905.00046 [ABS]: Migdal dominates bremsstrahlung in atoms.
**URF derivation [D].** Hypotheses: ω_γ ≫ ω_ph; photon wavelength ≫ a; ε_T(ω_γ) real. Setup: the transverse-photon-improper part of WP0-v2 (3.6) in S_κκ; the photon
couples to the lattice dipole H_γL = −Σ_IeZ*_κ(ω)u_I·E, Z*_κ(ω) the **dynamical Born charge** (macroscopic polarisation per displacement of one nucleus at ω, others
clamped, electrons non-adiabatic). The double-commutator expansion of 2210.06490 (3.3) gives amplitude ∝ eZ*·(q/M)·ê/ω_γ, independent of the lattice potential:

  d³Γ/(dω_γdω_phd³q) ∝ 𝔇_κκS^{GS}_κκ(q,ω_ph) × (2α/(3πω_γ))n_r(ω_γ)|Z*_κ(ω_γ)·q|²/M_κ²   (isotropic: |Z*·q|² → Z*²q²),                                        (W.13)

the photon-labelled extension of (W.1) (lattice ω_ph; photon ω_γ; ω_e = 0). Checks: vacuum atom (n_r = 1) Z*_atom = −m_eω²α_pol/e²_G = f, v_N² = 2E_R/M reproduce
Eq. (8) (C8a,c); Z*(∞) = Z (C8b). Small ω: Z*(ω) = Z*(0) + ω²C_κ, C_κ = 2ReΣ_nd_{0n}(∂_uV)_{n0}/E_n³ (DFPT). Above the gap n_r is complex and the photon is absorbed:
photon-pole residue = bremsstrahlung; continuum belongs to X (Migdal) at relative O(v²) (transverse vs Coulomb); no double count.
**Consequences [E].** Si/Ge: Z*(0) = 0 (ASR + equivalent sublattices), rate ∝ ω⁴C², comparable to the atomic estimate (|Z*| ≈ 0.05 at 1 eV); free-atom
Kouvaris–Pradler is not a crystal upper bound. GaAs (Z* ≈ 2.1, n_r ≈ 3.6): photons for ω < E_g where Migdal is closed; probability ≈ 2.6×10⁻¹³ over 0.1–1.4 eV at
m_χ = 100 MeV, ~10³× atomic, ~10⁻⁵ of above-gap Migdal; relevant only as a sub-gap optical channel in polar scintillators [C relevance].

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
| (M.1)–(M.4) amplitude, Pauli theorem, rate; (M.6)–(M.7) | D (P1–P5); REFEREED (R2) with the corrections applied |
| (M.8)–(M.9) window, no interference; (M.10), DC, O4 (iv″a–d) | D (REFEREED R2; O4 CLAIMED); rigorous version C |
| §M5 f-sum, aggregate compensation; per-diagram claim; δρ^V unrestricted sum | D; C; C |
| (M.12) adiabatic form, DFPT paths | D (REFEREED w/ corr.) |
| (M.13)–(M.14) screening, topology, frame theorem; F1 weight | D (RPA/ALDA); sizes E; δ_pair sign C |
| (M.15)–(M.16) soft limit, Ward identity, IR, C7a–e | D (X1 H1–H4); D^n symmetric C; magnitudes E |
| C1 (M.17) incl. FT prefactor; C5, C8 amended | D; C8 window E |
| (W.1)–(W.2), sectors; (W.4)–(W.6) | D (H1–H5; T1–T4) |
| J3, J7 (atom exact); J8 (F4) | D (leading BO); J8 ratio E |
| L7a–d; 2603.13052 discrepancy; EFT parameter | D (C2, C3); E (bound) |
| L9 prefactor FT; L9b T-transfer; 𝒯_e PA channel | D; sizes E |
| L12 (W.11)–(W.12), hybrid | D (C6); Si impact E |
| (W.13) bremsstrahlung | D; sizes E; relevance C |
| (W.14) exciton replicas | D (BSE-boson); completeness C |
| F8 bound on 𝔉 (WP5 (W15)); p_on fixed q and S̄ | E; D (parabolic, isolated quadratic minimum), vertex zeros E |

## 11. Contested corrections
None. One owed item is resolved rather than inherited: CORRECTIONS §9 "(W.5) inherits the X2/WP1 external-weight caveat (S open)". (W.5) uses the full matrix
S^{ee}_{GG′}, a total, which both weights reproduce exactly (WP3v2-C17a,b); the weight matters only for pair-resolved seeding, where the retarded out-state form
of WP0-v2 (7.2)/CC-1 is adopted. This agrees with WP0-v2 CC-1 and is an independent sympy confirmation of it (non-centrosymmetric complex ρ).

## 12. Interface flags
| # | Owner | Quantity | Recorded form | WP3-v2 use / mismatch |
|---|---|---|---|---|
| IF-1 (F1) | WP1 | external LFE weight, pair-resolved | WP1 [E2] (1+Rv)_{0G}ρ | WP3v2-C17c: as printed it misses the total without inversion. **WP1-v2 has accepted F1** (coordinator relay): out-state (ε^{-1})_{G0}ρ(q+G) = WP0-v2 (7.2) = X2 (2.2), used in (W.4b), (W.5) seeding, (M.13), (W.14). Closed, pending R7 |
| IF-2 (F4) | WP2, WP0 | κ₃ split, 𝓜³_eκ | WP2 (5.2); WP0-v2 (4.7) | closed by J8: 𝔨₃^X given from the all-electron, all-k form of (W.5) (static R^{ee}_{GG′}(p,0) over all p+G); WP2 (5.2) and WP2-v2 §5.2′ (first moment = J3) confirmed; contact part 𝔨₃^{(eN)} ≡ (q²/2M²)⟨∂²V_eN⟩ = −(m_e/M_κ)𝓜³_eκ(q→0)/(2𝓃_κ) with (4.7) per unit volume; WP2-v2's "−(m_e/M_κ)·(4.7)" is the same identity per nucleus in a ½-normalised moment (normalisation to check in R7); valence-only or soft-limit (W.5) cannot reproduce it |
| IF-3 (F6; WP2-v2 IF-8) | WP2 | GS lattice structure factor | WP2 "S^G" | S^{GS}_κκ throughout (W.4a), (W.5), (W.13); WP2-v2 adopts S^{GS}; consistent |
| IF-4 (F8) | WP3/WP5 numerics | 𝔉 in GaAs | O4 (O4.7) [C] | campaign bound WP5-v2 (W15): |ΔP| ≲ 0.11Γ/δ (2×10⁻³ off edge, 7×10⁻² edge shell); numbers still open |
| IF-5 | WP6 | onset exponent p (O6-2; AUDIT A1) | WP6 (3.3) | fixed q: 2 / 3 / ½; **angle-averaged S̄ at fixed |q|: 3 generic, 4 on a vertex zero (Si TA edge: 4 [E]), 4–5 forbidden, 3/2–5/2 excitons**; threshold E_g^{ren} + ω_TA(Q*_min(|q|)), window-empty below d < Q_w (§M3). WP6 to replace its 11/2, 13/2, 4 bullets |
| IF-6 | WP5 | X+, Migdal and DC seeds | WP0-v2 (7.3), WP5 (W6) | X+: (E_e, E_h, k_e, k_h, n_ph, ω_ph | q, ω) per operator; DC: O4 d6 seeds; Migdal: dP_Mig/dω_e + recoil; 2209.04503 "U" vs Migdal rule N3. Consistent |
| IF-7 (F7, F11) | WP3, all | thermal factor; static DFPT error | (W.4c); O(ω_Q/E_g) in D2 | applied: ÷(1 − e^{−βω}); O(ω_Q²/E_g²) |
| IF-8 | WP1 | Si exciton thresholds | WP1 §3.4 | used in §M9 (0.472 MeV forbidden, 0.708 MeV allowed) |
| IF-9 | CONTROLS, LIMITS | C4 wording, C7, L7d, L8, L9, L12 | CORRECTIONS §16 | §M5, §M8, §2, §3 give the texts; edits are the coordinator's |

## 13. Corrections applied (closing table)
| # | Correction (ID / source) | Where | How |
|---|---|---|---|
| 1 | D1 §2 eq. (3): 𝒢 = η/(2q), prefactor 1/(4π) (REF-A §1; audit A1) | (M.6) | derived; WP3v2-C12a,b |
| 2 | D1 §2 |f_cr|² prefactor 2π²/(αm_e²Ω), Ωq³S̄/(4παm_e²) (REF-A §1; WP1 [E12]) | (M.7) | WP3v2-C12c |
| 3 | REF-B §1 "η/q verified" wrong (CORRECTIONS §3) | (M.6) | η/(2q) used |
| 4 | D1 §5.1 bound → min(E_min − ω, E_g − ω_max) (REF-A §2, REF-B 2b) | (M.8) | per-path bounds |
| 5 | D1 §4 error scale δ; "only path B" holds for Sternheimer output only (REF-A §6, REF-B §6) | (M.12), §M6 | stated with finite P_v sum, non-SCF ∂ψ_c |
| 6 | D1 §5.2 Hadamard fp, not PV (REF-A §7, REF-B §7) | (M.10) | WP3v2-C13 |
| 7 | D1 §5.3, §6.2(b): first moment only; DW = e^{−2W}; AH shift not DW | §M5 | stated |
| 8 | D1 §6.1 C1: intraband division by zero; restore i[g,q·r] | §M9 C1 | D2 proof adopted; term restored |
| 9 | D1 §6.2 / D2 §6 C7 superseded by X1 (REF-A §4, REF-B §4) | §M8, (M.15) | X1 adopted; D1, D2 limits located (C1, C16) |
| 10 | D1 §3 / D2 §4b screening: pair channel; H2 redundant (REF-A §5, REF-B §5, X2) | §M7 | (M.13)–(M.14), four classes |
| 11 | D1 §7 recipe: Bethe ridge for ρ and g, cost redone, PAW at all q, Si quadrupoles, one gauge, nonlocal C4 (REF-A §10, REF-B §10) | §M10 | all included |
| 12 | D1 renames χ → R, Δ_{A,m} → d_{A,m}, a → b, D(λ) → ρ_cv(λ_fd) | (M.1), (M.12) | applied |
| 13 | D2 script docstring spin 2 (REF-A §1) | (M.4) | spin explicit; WP3v2-C22b (script untouched) |
| 14 | D2 §2b window misses hole path (REF-A §7, REF-B §7) | §M4 | D1's E_min(q) criterion |
| 15 | D2 §2c item 4 unrestricted sum in δρ^V unproven | §M5 | [C], Kubo form |
| 16 | D2 §3 per-diagram cutting pair unproven; "mainly g_cc − g_vv" [E] (REF-A §3, REF-B 3b) | §M5 | aggregate proof only |
| 17 | D2 §6 C8 restricted to m_χ ≈ 0.4–0.9 MeV, folded q (REF-A §8, REF-B §8; SOTA AMENDED) | §M9 | applied with Si analogue |
| 18 | D2 §6 C1 nonlocal "approximate" wrong in kind; q̂ before cubic step (REF-A §9, REF-B §9) | §M9 C1 | applied |
| 19 | D2 §6 C5 threshold E_g − max_ν ω_{Q*ν} at connecting Q* (REF-B §10) | §M3, §M9 | applied |
| 20 | D2 §0, §2: e(−Q) = e(Q)*; non-degeneracy unnecessary (REF-B §1, §7) | §M1, §M4 | stated |
| 21 | D2 §5 GaAs ε_ion ≈ 10⁻³ absolute, 10⁻⁴ relative (REF-B §5) | §M7 | applied |
| 22 | D2 renames χ → R, Π → R̃, A_Qν → B_Qν, M carries 1/√N, H_DW, Σ^{DW} → H_AH, Σ^{AH} | §M1, §M5 | applied |
| 23 | REF-A §5 ε(q,ω∓ω_Q) exact for the convective part only (X2 §5) | §M7 | frame theorem |
| 24 | REF sympy notation c_ν, 𝔄, v^g_n | §M8 | applied |
| 25 | X1 §9 screening aside resolved by X2 | §M7–§M8 | stated |
| 26 | X1 §5 C7 verbatim with ℓ_Q N outside, Q̂·Ξ·ê, upper sign emission (CONVENTIONS §5, §13 items 5–6) | (M.15), C7a–e | applied |
| 27 | X1 renames η → |Q|, c → c_ν, v_n → v^g_n, P_n → p_nn, S, s → 𝔖, s^W, K_± → K^{soft}_± | §M8 | applied |
| 28 | X2 (2.2) external weight in non-centrosymmetric targets (S open; CONVENTIONS §13 item 16; coordinator) | §M7, §11 | out-state weight; WP3v2-C17 |
| 29 | X2 §6 δ_pair sign, c_coh bound, q-independence stay [C]; interim [0.5, 1.2] | §M7 | applied |
| 30 | X2 renames χ_KS → R⁰, W → W^{scr}, Λ → r^{pair}, η → c_coh, T_G → 𝔗_G, D_f → δM^{intra}_f, K → f_Hxc | §M7 | applied |
| 31 | O4 §3 (vi) scope: Fan Z part per pair; no global n_e zeroth-moment rule (CONVENTIONS §13 item 17) | §M5, J4 | applied; WP3v2-C14 |
| 32 | O4 "P(Q)" → P(N_eh|q,ω) | §M4 | applied |
| 33 | O4 renames C1 → DC, m, f → Λ₀, Λ₊, λ_f → a^{off}, ρ̃ → ρ^{ren}, Δ → δω, φ → w_test, 𝒜(ℓ) → 𝒞_adm(ℓ_win), V → V_ep, P → PV | §M4 | applied |
| 34 | WP3 (W.4c) thermal factor (CORRECTIONS §9; F7) | (W.4c), (M.14) | ÷(1 − e^{−βω}); WP3v2-C21 |
| 35 | WP3 (W.5) external-weight caveat (CORRECTIONS §9; WP1-v2 IF-1 relay: out-state (ε^{-1})_{G0}ρ(q+G) accepted) | (W.5), §M7, §11, IF-1 | resolved: totals unaffected; pair-resolved seeding uses the out-state weight |
| 36 | WP3 renames S, Ω_S, A^S → λ, E_λ, A^λ; 𝒢_{SS′ν} → g^x | §7 | applied |
| 37 | WP3 renames χ_f → Ψ^{vib}_f; W_e → E^{Mig}_1; n(ω) → n_r; A_f → A^{Mig}_f, A^{PAER}_f; α(ω) → α_pol; k (W.5 loop) → p | §1–§6 | applied |
| 38 | WP3 renames τ_e → 𝒯_e; n_e, n_κ (densities) → 𝓃_e, 𝓃_κ; labels → WP3-… | §1, §4 | applied |
| 39 | Global: G → GS, S^G → S^{GS} (CORRECTIONS §0) | §1–§8 | applied |
| 40 | Global: "DW" for AH in W3 §5 source quotes | §5 | marked as source's Σ^DW = Σ^{AH} |
| 41 | Global: v_n, P_n → v^g_n, p_nn; M¹ → 𝓜¹ | §M8, §1.4 | applied |
| 42 | Global: κ → κ_mix (1608.01994 quote); X (ladder) → 𝒳; κ (BO) → κ_BO | §4, §1.3 | applied |
| 43 | Global: Δ collisions → v_N·p (L7c), E_cv (W.12), d_{A,m}, δω | §2, §5, §M | applied |
| 44 | SOTA amendment "C1 prefactor from memory" (CORRECTIONS §15) | §M9, §4 | closed in FT |
| 45 | SOTA #8 adiabatic REFEREED w/ corr. (δ, ∂V_SCF) | §M6 | = #5 scope stated in SOTA wording |
| 46 | Theorem D (i): per-sector PSD only in window / bins ≳ δ (O4 §9; CONVENTIONS §13 item 20) | §1.1, (J6) | applied |
| 47 | v1 §1.6 [C] → DC + O4 (iv″) (CONVENTIONS §10; WP0-v2 §6.2 (iv)) | §1.6 | applied |
| 48 | WP0-v2 equation numbers (brief) | throughout | v1 WP0 citations remapped |
| 49 | Static DFPT error O(ω_Q²/E_g²) (F11; X2 §2) | §M7, §2 L7d | applied |
| 50 | F4 / WP2 gap 7 / NOTATION-APPLY D10: compare κ₃ split, (4.7), Migdal spectra | (J8) | derived; WP3v2-C18 |
| 51 | F8: size of 𝔉 in GaAs | §M4 | bound [E]; WP3v2-C20 |
| 52 | WP6 O6-2: onset exponent for S^{X+} | §M3, §7 | p_on; WP3v2-C19 |
| 53 | F6: S^G from WP2 | (W.4a), (W.5) | S^{GS}; flag IF-3 |
| 54 | L9b(d) coupling g → y_φ (collision with g_mnν; WP0-v2 (3.5)) | §4 | applied (found in revision) |
| 55 | L9b(c) "unscreened spin current" → f_xc^T-renormalised (WP1-D5) | §4 | applied |
| 56 | ℓ_Q N outside; M^{(2)} D1 normalisation (CONVENTIONS §5, §13 items 4–5) | §M1–§M8 | applied |
| 57 | Boost mass m_A vs M_κ + δM_κ (CONVENTIONS §13 item 22) | §2 L7a | applied |
| 58 | ZG deterministic; L7d split (CONVENTIONS §13 items 14–15) | §5, §2 | kept |
| 59 | WP1 exciton thresholds as the Si window boundary (WP1 §3.4) | §M9 | applied |
| 60 | N3 extended to energy-loss terms that already contain Migdal (WP5, 2209.04503) | (N3) | applied |
| 61 | Carrier energies E_e, E_h (F10; NOTATION rows from WP0-v2) | §8 G2, IF-6 | applied |
| 62 | WP2-v2 relay (F4): 𝔨₃^X from the all-electron, all-k (W.5), or record a gap | (J8), IF-2 | given: E^{Mig}_3 = −(2M²)^{-1}Σ_{GG′}∫d³p…R^{ee}_{GG′}(p,0), all electrons, all p+G; contact identity with (4.7) agrees up to normalisation (IF-2) |
| 63 | WP2-v2 relay IF-8: S^G → S^{GS} | §1–§8 | applied (= #39, #53) |
| 64 | AUDIT A1 (blocking): p_on of angle-averaged S̄^{X+} at fixed |q|, minimised over q̂, WP1 [E10] rule; C5 infimum | §M3, §M9 C5, §3, IF-5 | derived: 3 / 4 (vertex zero) / 4–5 / 3/2–5/2; infimum E_g (window empty); WP3v2-C23 |
| 65 | AUDIT A6: χ → R, R⁰ in frame theorem; named c_𝔄, R^{(2)}_D; ℓ_Q ê; Λ(q) → r^{pair}(q) | §M7, §M10 | applied |
| 66 | AUDIT A7: Si zero-phonon exciton 0.472 MeV (v_max = 794.5 km/s) | §M9, IF-8 | applied |
| 67 | AUDIT A8: impulse criterion and endpoint kinematics (WP2-v2) | §2 L7b | 91.5/112 keV, 17.3/21.1 MeV; 50–70 MeV = typical q |
| 68 | AUDIT A10: WP5-v2 (W15) is the campaign Fano-term bound | §M4 F8, IF-4 | cited; prefactor 0.3 |
| 69 | NOTATION v4 renames (CORRECTIONS §17) | §4, §16 | 𝒜_ν(ω;T) → 𝒜^{PA}_ν(ω;T) (3 occurrences in §4, 1 in §16); §16 updated to v4. Notational only |

**Count:** 68 applied; 0 contested (#35 resolved with derivation, §11). Row 69 (NOTATION v4 renames) is notational and outside this count.

## 14. Open items handed on
O-WP3-1 X2-N2/N3 (pair channel, δ_LF) and the Umklapp re-check of the Si window; O-WP3-2 finite-P BSE for Si (G5); O-WP3-3 DFPT values of δM_κ, E^{Mig}_3, C_κ for Si, Ge,
GaAs; O-WP3-4 rigorous (H5)-free labels (O4 §8); O-WP3-5 WP1 to confirm the ALP/SOC statement of L9b(c); O-WP3-6 𝔉 in GaAs and the Γ_Λ₀/δ map in Si (F8, d11);
O-WP3-7 referee check of the F1 resolution with REV-WP1 (R7); O-WP3-8 δρ^V unrestricted sum (§M5) or its Kubo replacement.

## 15. Literature (IDs verified against the arXiv API for v1, 2026-10-31; FT = full text read for v1)
FT: 1707.07258 (Ibe et al.); 2011.09496 (KKL); 2210.06490 (Berghaus et al.); 2603.13052 (Berghaus–Essig–McDuffie); 2505.08864 (Esposito–Rocchi); 2205.03395 (Liang et al.);
1202.3454 (Noffsinger et al.); 2302.08085 (EPW 2023); 1608.01994 (Hochberg–Lin–Zurek); 1412.8378 (An et al.); 2106.12586 (Mitridate et al.); 1604.02394 (Zacharias–Giustino);
1603.06965 (Giustino RMP); 1607.01789 (Kouvaris–Pradler); 1705.04245 (Antonius–Louie). ABS/title: 1912.10929; 1905.00046; 2606.14845; 2104.01811; 2210.04917; 2310.05704;
2011.13352; 2105.00599. Via owner returns: 1509.01598 Eqs. (17), (21), 2101.08275 Eq. (16) (WP1); 2209.04503 (WP5). UNVERIFIED: Cohen–Bergstresser GaAs form factors (§M4).

## 16. Symbols introduced/used
All symbols follow NOTATION v4 and CONVENTIONS; **no deviations** (v4 renames: CORRECTIONS §17, closing-table row 69). Used as defined there: q, ω, ω_q, v, v_min, η, 𝒢, ρ_χ, f_χ, σ̄_e, Ṽ, F_DM, μ_χe, m_χ, ρ_T, Ω, N, V,
𝔇_ab, c_s, y_χ, y_N, y_φ, m_V, κ_mix, g_aee, φ, m_φ, k_φ, Γ_χ, Γ_abs, ℛ; k, k′, n, m, v, c (subscripts), ε_nk, ε̃_nk, E_g, E_dir, k_c, E_cv, E_min, E_min^{ren}, ρ_mn,
ρ_cv(k,q;λ_fd), ρ̃_mn, ρ^{ren}, M^{(1)}, M^{(2)}, M_v, A₁, A₂, A₁^v, A₂^v, M̃_±, d_{A,m}, d_{B,m}, δ, δ₀, p, p_mn, p_nn, v^g_n, v_mn, r_mn, j_e, 𝒯_e, T_e, O_a, H, H_ep, H_AH,
f_nk, E_i, E_f, p_i, 𝒵, T_fi; Q, ν, ω_{Qν}, e_{κν}, b_{Qν}, B_{Qν}, n_{Qν}, n_B, g_{mnν}, g^S, g^L, g^{AH}, g^x_{λλ′ν}, ℓ_Q, ê, Q̂, κ, κ_BO, M_κ, M_cell, Z_κ, m_A, R,
𝓃_e, 𝓃_κ, 𝓕_κ, Z*_κ, Z*_κ(ω), C_κ, ε_∞, ε₀, ω_LO, ω_TO, B_κ, 2W_κ, S_HR, 𝔨_m, 𝔨₃^{GS}, 𝔨₃^X, x_R, c_ν, D^n, Ξ^n, d^n, C_F, C_pz, v_N, Ω_{p,ion}; S, S_ab, S̄, S^{prop},
S^{(1)}, S^{PA}, S_ab(q;ω_ph,ω_e), R, R̃, R⁰, Π^γ, ε, ε̃, ε_e, ε₁, ε₂, ε₂^{PA}, ε_L, ε_T, L, L^{PA}, 𝓜¹, 𝓜³, 𝓜₁^{SB}, ω_p, f_xc, f_xc^T, f_Hxc, W^{scr}, P, ω_f, 𝔗_G,
r^{pair}_f, c_coh, δ_ω, δ_LF, δ_pair, δ_ion, δM^{intra}_f, A^λ_{cvk}, E_λ, λ, E_x, E_x^b, 𝒮_F, n_r, ω_γ, α_pol, σ₁; GS, X0, X+, X, 𝒫₀, U_n, U_ep, Λ, Λ₀, Λ₊, Ẽ_Λ₀, Z_Λ₀,
Γ_Λ₀, Γ^{ph}, Γ^{(f)}, Γ̂, Σ^{FM}, Σ^{AH}, δω, fp, PV, DC, 𝒞_adm(ℓ_win), w₀, b_λ, 𝔉_{Λ₀,ν}, c_ν^F, a^{off}_f, Υ_Λ₀, σ, τ, τ_J, 𝒳, K, 𝔐, η_ep, η_anh, σ_c, Δ^τ_k, p_on;
N_eh, P(N_eh|q,ω), P_casc, ε_eh, E_e, E_h, E_R, Y_tot, Y_casc; ω_e, ω_ph, Ê_e, Ê_L, A^{Mig}_f, A^{PAER}_f, U_κ(p), Z_κ(p), Ψ^{vib}_f, δM_κ, E^{Mig}_1, P_Mig; 𝔄, 𝔖, s^W,
K^{soft}_±, Q_min, Q_p; F^W_ij(R,q), U(k).
**Introduced here (new objects, no collision; NOTATION v4 §M rows):** **E^{Mig}_3(q)** (ω_e³ moment of the Migdal spectrum per nucleus, J8; analogue of
E^{Mig}_1); **M^{exc}_{λ±}** (exciton-replica amplitude, (W.14); v1's M^{exc}_{S±}); **𝒜^{PA}_ν(ω;T)** (T-independent PA branch spectrum in the σ₁ transfer rule, §4; v3 name 𝒜_ν).
Labels: (M.1)–(M.18) (Part I), (W.n) (v1 numbers), J1–J8, N1–N5, T0–T6, WP3v2-Cn, IF-n, O-WP3-n.
