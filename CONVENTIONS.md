# CONVENTIONS (authoritative; v1, 2026-10-31, NOTATION-APPLY pass after R5)

**Precedence.** CONVENTIONS.md > NOTATION.md (v4) > state/SOTA.md > state/CORRECTIONS.md > returns, briefs and sources.
- Returns are the historical record and are never edited. Where a return differs from this file, the return is read *through*
  state/CORRECTIONS.md, which lists every owed rename and every owed substantive correction, per return and per site.
- **Before quoting any return, open state/CORRECTIONS.md at that return's section.**
- Every convention below gives one sentence, "Why", on why it was chosen. §13 records the places where returns disagree and what
  was decided. The consistency audit of the key formulas is in returns/R5/NOTATION-APPLY.md (script: scratchpad copy cited there).

---
## 1. Units and charge
- ħ = c = k_B = 1. Heaviside–Lorentz charge: **e² = 4πα**, e > 0, electron charge −e, charge numbers z_e = −1, z_κ = Z_κ.
  Coulomb kernel **v_C(k) ≡ e²/k²** (matrix form v_C = diag v_C(q+G)).
  *Why:* every return from D1 on uses it, and it makes S = (2q²/e²)L read q²/(2πα), the KKL/Hochberg form, with no stray 4π.
- Sources in Gaussian units (Noffsinger, Adler–Wiser, Kouvaris–Pradler) are converted with e²_G = α; SI sources (EPW) with
  e²/ε₀^SI = 4πα. A quoted source formula keeps its own units and must say so.
  *Why:* the C1 and L9 prefactor checks (8π²α/(Ωω²)) close only with this map.
- Ω = unit-cell volume, N = number of cells (N_k = N_Q = N on uniform grids), V = NΩ. ρ_T = target mass density.
  *Why:* NOTATION v2 and all returns already use them; the per-cell/per-target/per-mass factors of the sources are fixed in §8.

## 2. Fourier conventions and normalisation
- Spatial: O(q) = ∫d³r e^{+iq·r} O(r), so n_e(q) = Σ_i e^{+iq·r_i}; Ṽ(q) = ∫d³x e^{+iq·x}V(x); ⟨p−q|V(r_χ−r_e)|p⟩ = V^{-1}Ṽ(q)e^{+iq·r_e}.
  *Why:* with q given by the DM (§3) this is the only choice in which the crystal vertex is e^{+iq·r} (D1 N0, D2 §0, WP0 (1.1)).
- Temporal: f(ω) = ∫dt e^{+iωt} f(t); retarded functions are analytic in Im ω > 0 (poles at ω − E_f + E_i + i0).
  *Why:* WP0 (3.2) and (4.2) use it; it fixes the sign of i0 that 2609.06423 gets wrong (WP4).
- Box normalisation: Σ_q ↔ V∫d³q/(2π)³, δ_{qq′} ↔ (2π)³δ³(q−q′)/V. Brillouin-zone average ⟨⟨·⟩⟩ ≡ N^{-2}Σ_{kQ} = Ω²∫_BZ d³k d³Q/(2π)⁶.
  *Why:* it makes every intensive quantity (S, ε₂, L) manifestly N-independent, as audited in D1 (2)/(4).
- Matrices in reciprocal space are indexed with the **unreduced** q at G = 0: (ε^{-1})_{00}(q,ω) ≡ (ε^{-1})_{G_qG_q}(q_r,ω), q = q_r + G_q,
  q_r ∈ 1BZ.
  *Why:* WP0 (5.2) and WP1 [E1] write the same object in the two forms; one statement removes the ambiguity.

## 3. Kinematics: sign of q, sign of ω, n_q
- **q is the momentum transferred FROM the DM TO the target** (3-vector, never folded to the 1BZ). The DM goes p → p − q.
- **ω is the energy given to the target**: ω_q = q·v − q²/2m_χ − Δ_χ (WP0 (2.1)). Δ_χ = m_{χ₂} − m_{χ₁}; Δ_χ < 0 is exothermic.
  ω < 0 is allowed at T > 0 (the target gives energy), weighted by detailed balance (§6).
- On-shell minimum speed v_min(q,ω) = (ω + Δ_χ)/q + q/2m_χ; longitudinal DM velocity v_∥ = (ω + Δ_χ)/q (WP6 (1.1)).
- Density operator **n_q ≡ n_e(q) = Σ_e e^{+iq·r_e}**; the response matrix uses ⟨i|O_a(q)†|f⟩⟨f|O_b(q)|i⟩ (WP0 (3.1)).
  *Why (all four):* fixed in D1 N0 / D2 §0 and used unchanged by WP0–WP6 and O4. KKL (n_{−k}) and Ibe (e^{−iq_e·x}) use the
  opposite sign; this is immaterial for T- or P-invariant targets (S(q) = S(−q)) but **not** for P- and T-broken targets (WP4 [3.1]),
  so the campaign sign is binding.

## 4. Bloch states and the density vertex
- ψ_{nk}(r) = e^{ik·r}u_{nk}(r)/√N, normalised over V; u_{nk} normalised to 1 over Ω. Periodic gauge ψ_{n,k+G} = ψ_{nk}.
- **ρ_{mn}(k,q) ≡ ⟨ψ_{m,k+q}|e^{iq·r}|ψ_{nk}⟩**, O(1), with k+q folded to the 1BZ and the Umklapp G kept inside the plane wave;
  ρ_{nn}(k,0) = 1. No factor N.
  *Why:* D1 N1 and D2 §0 showed independently that the old "·N" made S ∝ N (applied 2026-10-31).
- Band labels: n generic, m intermediate (any band), v occupied, c empty. **v and c appear only as band subscripts**, never bare.
  *Why:* v is the DM velocity and c_ν a sound speed (§13 item 9).
- g and ρ (and every Wannier tensor F^W_ij(R,q)) must share one gauge U(k); PAW/US inputs need the augmentation term at all q.
  *Why:* REF-A/REF-B §10: otherwise the m sum in M^{(2)} acquires random phases and ρ_nn(k,0) ≠ 1.

## 5. Phonons, EPW g, M^{(2)}
- Displacement: u_{Rκ} = Σ_{Qν}(2NM_κω_{Qν})^{-1/2} e_{κν}(Q) e^{iQ·R}(b_{Qν} + b†_{−Qν}); Σ_κ|e_{κν}(Q)|² = 1; e_{κν}(−Q) = e_{κν}(Q)*.
  Phonon operators are **b**, magnon (Holstein–Primakoff) operators are **a**.
  *Why:* the D1/D2 forms are equal; b removes the clash with HP magnons (WP4) and with the DM-boson mode operator (WP0 (3.3)).
- **EPW convention**: g_{mnν}(k,Q) = (2ω_{Qν})^{-1/2}Σ_κ e_{κν}(Q)M_κ^{-1/2}·⟨ψ_{m,k+Q}|∂_{κ,Q}V_KS|ψ_{nk}⟩, DFPT-screened, O(1);
  H_ep = N^{-1/2}Σ g_{mnν}(k,Q) c†_{m,k+Q}c_{nk}(b_{Qν} + b†_{−Qν}); hermiticity g_{mnν}(k,Q)* = g_{nmν}(k+Q,−Q).
  Long-range splits: g = g^S + g^L (EPW). The O(u²) Allen–Heine vertex is g^{AH}. Sources' "q" for the phonon wavevector is Q here.
  *Why:* it is what EPW outputs and what D1, D2, X1, X2, WP3 and WP5 (W2) use, so codes need no rescaling.
- Bose factor n_{Qν} = n_B(ω_{Qν}), n_B(x) = (e^{βx} − 1)^{-1}. Emission of phonon −Q carries n+1 (upper sign), absorption of +Q carries n (lower
  sign); both use g(·,Q). Combined weight n_{Qν} + ½ ± ½.
  *Why:* D1 N3 = D2 (2.1) = X1 = WP3; one sign convention for the whole M1 chain.
- **M^{(2)}_{cvν,±}(k,q,Q) is D1 eq. (1)**: unrestricted m sum, no 1/√N inside (the 1/√N sits in T_fi), final electron at k' = k+q+Q.
  D2's amplitude is M_D2 = M^{(2)}/√N. On shell the D2 denominator ω − ε_{m,k+q} + ε_{vk} equals D1's ε_{ck'} − ε_{m,k+q} ± ω_Q.
  *Why:* X1, X2, WP3 and the PAER rate (4π/Ω)⟨⟨Σ(n+½±½)|M|²δ⟩⟩ all use it; it keeps M intensive.
- Zero-point length **ℓ_Q ≡ (2M_cell ω_{Qν})^{-1/2}, N outside** (D1, X1, WP3); u^{zp} = ℓ_Q ê/√N (D2).
  *Why:* consistency with the M^{(2)} normalisation above; WP0 (4.9) put N inside; the rename is applied in WP0-v2/v3 (CORRECTIONS WP0).
- **C7 (soft acoustic limit) = X1 §5 C7a–e**, upper sign = emission of −Q, index order Q̂·Ξ^n·ê, Ξ^n = D^n + v^g_n ⊗ p_{nn}.
  *Why:* REF-A/REF-B refuted the D1 and D2 forms; WP3 confirmed X1 and showed WP0 (4.9) agrees only at band extrema.

## 6. Response objects, FDT and spin factor
- Response matrix S_ab(q,ω) = (2π/V)Σ_{if}p_i⟨i|O_a(q)†|f⟩⟨f|O_b(q)|i⟩δ(ω − E_f + E_i), p_i = e^{−βE_i}/𝒵 (WP0 (3.1)). S ≡ S_ee.
- Retarded response R_ab (WP0 (3.2)); **R, not χ** (χ is the DM). R⁰ = KS/QP independent-pair bubble. R̃ = Coulomb-proper response
  (irreducible with respect to one Coulomb line of the external channel {q+G}). D2's Π ≡ R̃_ee at clamped nuclei.
  Π^γ (photon self-energy, e²-normalised: Π^γ_T = e²(R_{j_Tj_T} + 𝓃_e/m_e)) is a different normalisation and always carries γ.
  *Why:* WP0 §10 decision; it removes the χ and Π collisions of D1, D2, X2 and 1608.01994.
- FDT: (1 − e^{−βω})S_ab = i[R_ab − R_ba*]; diagonal S_aa = −2 Im R_aa/(1 − e^{−βω}). Detailed balance S_ab(−q,−ω) = e^{−βω}S_ba(q,ω).
- Dielectric matrix (total charge, LFE included) ε_{GG′}(q,ω) = δ_{GG′} − v_C(q+G)R̃_{cc,GG′}; electron channel ε_e^{-1} ≡ 1 + v_C R_ee;
  macroscopic ε_mac ≡ 1/(ε^{-1})_{00}. ε = ε₁ + iε₂. Loss function **L ≡ Im[−(ε^{-1})_{00}(q,ω)]**; channel loss L_ch, ch ∈ {c, e}, with ε_c ≡ ε.
- **S ↔ L:** S_chch(q,ω) = (2q²/e²) L_ch(q,ω)/(1 − e^{−βω}) = q²L_ch/(2πα(1 − e^{−βω})). The ELF form of S_ee holds only at clamped
  nuclei or for ω ≫ ω_max (WP0 (5.5)); for a dark photon it holds exactly with the total ε.
- Proper part: ε₂ = −v_C Im R̃ = (e²/2q²)(1 − e^{−βω})S^{prop}. At T ≪ E_g and ω > 0 the thermal factor is dropped.
- **Spin factor:** S and ε₂ are summed over spin; for spin-independent vertices without SOC the IP forms carry an explicit 2,
  S(q,ω;cvk) = (4π/V)|ρ_cv(k,q)|²δ(…). With SOC drop the 2 and sum over spinor bands. Per-spin quantities (Catena's 𝒲̄_l) must say so.
  Spin channel (SOC = 0, unpolarised, IP): S_{s^αs^β} = (δ_{αβ}/4)S^{IP}_nn, unscreened (WP1 [E6]).
  *Why (whole section):* these are WP0 §3–§5, confirmed term by term by D1 ⟂ D2 (REFEREED) and by WP1–WP4; the spin factor was the
  most frequent source discrepancy (D2 script, 1509.01598 vs 2105.02233).
- Moments: 𝓜¹_ab = ∫(dω/2π)ω[S_ab[O] + S_ba[O†]] [amended R8 (WP0-v3 G3); the same pairing applies to 𝓜³]; for densities with inversion **∫_{−∞}^{∞}dω ω S_ee = π𝓃_e q²/m_e**, equivalently
  ∫₀^∞dω ω L = (π/2)ω_p² at T = 0.
  *Why:* this is WP0 (4.5)–(4.6) and (9.5); the 2π of WP0 (8.2) is the owed correction W1 (audit A12).
- Commutator: [T_e, n_e(q)] = q·j_e(q) **exactly**, with j_e = Σ½{p/m_e, e^{iq·r}}; the WP0 "+(q²/2m)n" term is wrong (WP1 D1; audit A13).

## 7. Screening and DM-side tensors
- **Proper / improper.** "Proper" means R̃ (or Π, ε₂^{prop}); "improper" or "screened" means the full R (or L). Screening is applied
  once: DFPT g (channel Q), external ε^{-1}(q,ω) with LFE, and the **pair channel** W^{scr}(P,ω_f) with P = q+Q, ω_f = ω ∓ ω_Q (X2).
  *Why:* X2's topological proof; WP0 (5.5) and WP3 confirm it; the R1 "two channels" statement is withdrawn.
- **Screened amplitude M̃ = X2 (2.2)**: M̃ = M^{(2)}[ρ̃] + Σ_{GG′}ρ_f(P+G)W^{scr}_{GG′}(P,ω_f)𝔗_{G′}(P), ρ̃(k,q) = Σ_G (ε̃^{-1})_{G0}(q,ω)ρ(k,q+G).
  WP0 (5.7) is its truncation. The retarded out-state weight (ε̃⁻¹)_{G0} in (3.2) order is general (WP0-v3 CC-1, R7 STANDS);
  W^{scr}(P,ω_f) retarded, final-pair index first (G8) (§13 item 16).
- **External-field type** is the species coupling vector c_s (WP0 (5.3); WP2's f_κ): total charge (dark photon) |c⟩ ∝ |z⟩ uses the total ε;
  electron-only |c⟩ = |e⟩ uses ε_e (equal to ε at clamped nuclei); nucleon uses R_NN = R̃_NN + R̃_{Nc}ε^{-1}v_C R̃_{cN}. Every operator with
  R̃_{ac} ≠ 0 is screened: n and j_L always; j_T through local fields (WP1 D4); spins at SOC = 0 are not Coulomb-screened but are
  dressed by the triplet W^{scr} ladder + f_xc^T, R̃_s ≡ 4R_{s^zs^z} (WP1-v3 IF-13).
  *Why:* WP0 (5.3) corrected by WP1; a single rule replaces the EXCEED-DM global f_scr.
- **DM-side tensor** 𝔇_ab(q,v) = (2j_χ+1)^{-1}Σ_{ss′}𝒱_a^{s′s*}𝒱_b^{s′s} (Hermitian PSD); vertex normalisation 𝒱_{n_e} = c₁/(4m_χm_e), so
  |𝒱_{n_e}|² = |Ṽ|² = πσ̄_eF_DM²/μ_χe². Velocity decomposition 𝔇 = 𝔇^{(0)} + 𝔇^{(1)}·v_T + v_T·𝔇^{(2)}·v_T with v_T the halo velocity
  transverse to q̂ (WP6 (1.2)). Target operators are O_a, a = (s, Γ) (WP0 (2.2)); Fitzpatrick operators are written 𝒪_i (i = 1…15);
  ~~𝒪₂ is outside the 16-row basis (needs a v_s⊗v_s row; WP0-v3 G2).~~ **R16:** 𝒪₂ → v_χ²n_s − 2v_χ·j_s + 𝔳²_s with the 17th row 𝔳²_s, ⟨k′|𝔳²_s|k⟩ = (k+k′)²/4m_s² (CW3 (CW3.2); = −2× the scalar-NLO 𝒯 row in its source normalisation) (CW3 OC-9; LIMITS L-O2).
  DM spin unpolarised unless stated.
  **R17 (LE-175, WP7-D-v2 IF-D2):** (i) **𝔘_C joins the operator basis** as one species-summed **two-body row** a = (C, 𝔘): 𝔘_C(k) is the Coulomb-energy density, with
  𝔘_C(0) = ∂H_C/∂ln α = (1/2V)Σ_{k′≠0}v_C(k′)[ρ_c(k′)†ρ_c(k′)/e² − Σ_s z_s²N_s] (WP0 (1.1)); it is the only row not of the per-species one-body form, so the basis
  is 17 one-body rows per species plus 𝔘_C. The single screening rule above applies if R̃_{𝔘c} ≠ 0 (not computed). Its only use is k → 0 (scalar moduli, WP7-D (D.8),
  LIMITS L-D5), and there the H_C scaling identity gives the vertex directly. (ii) **𝔇^F and 𝔇^{pair} are DM-side tensors, not basis rows**; they contract the existing S_ab:
  𝔇^F_ab = 𝔏_ab/(4E_χE_ν̃) on the curve ω = ω^F_q(v) (fermionic absorption, WP7-D (F.1)–(F.2)); for a massive ν̃, 𝔇^F = 𝔇^{NR}(m_χ/m_ν̃)(1 + O(v²)) in the vertex
  normalisation above (CW3-errata §2.2 item 20). 𝔇^{pair}_ab = 𝒢_a*𝒢_b/(4E_pE_p̄) at total momentum p + p̄ and energy E_p + E_p̄ (pair absorption, WP7-D (T.1)–(T.2)),
  against the rows n, j, 2 tr J, 2s. Neither is the single-χ spin average 𝔇_ab defined above, so neither inherits its velocity decomposition. The charged-current case
  (χ + n → p + e⁻) stays outside the basis as an exact gap (LE-86).
  *Why:* it is the WP0 anchor that reproduces D1/D2 and every LIMITS prefactor checked (audit A2–A5, A16).

## 8. Halo conventions (2105.00599) and rate normalisation
- SHM per 2105.00599: ρ_χ = 0.3 GeV/cm³, v₀ = 238 km/s, v_esc = 544 km/s, v_⊙ = v_lsr + v_pec = (0, 238, 0) + (11.1, 12.2, 7.3) km/s,
  |v_⊙| = 250.5 km/s, Earth orbital velocity v_⊕(t) of their eq. (11) (|v_⊕| = 29.8 km/s). Lab-frame f_χ(v) ∝ e^{−|v+v_E(t)|²/v₀²}
  Θ(v_esc − |v+v_E(t)|)/N_esc, with v_E(t) = v_⊙ + v_⊕(t).
- Halo integrals use v_E(t), averaged over the exposure. **Reference scalars** (edges, m_min, windows) use **v_E^ref ≡ |v_⊙| = 250.5 km/s**
  and **v_max ≡ v_esc + v_E^ref = 794.5 km/s** (quoted as 794); the annual range v_max ∈ [781, 810] km/s is a halo-band entry (WP6 R3).
  *Why:* it keeps every campaign threshold (floor 0.333, PAER edge 0.333–0.337, ZPL 0.42/0.54 MeV; 0.319 is the scissor comparison) valid, uses a time-independent frame quantity, and moves the
  annual-mean subtlety (252.1 km/s, WP6 C6) into the halo band, where it belongs.
- η(v_min) = ∫d³v f_χ Θ(|v| − v_min)/|v|; ξ(v_min) = 2∫_{v_min}^∞ v′η(v′)dv′ (WP6 (1.3)); η̃ = ρ_χσ̄_eη/m_χ (2311.04957).
  Velocity kernel 𝒢(q,ω) ≡ ∫d³v f_χ δ(ω − ω_q) = f̂^{(0)}(q̂,v_min)/q; **isotropic S gives 𝒢 → η(v_min)/(2q)**.
  *Why:* REF-A, WP0 (9.1), WP6 C10a and audit A1; D1's η/q is an owed correction. The hypothesis is the angle average of S, not
  isotropy of f_χ (WP6 W5).
- Rates are **per unit target mass** (WP0 (3.4)): dℛ/dω = (ρ_χ/m_χρ_T)∫d³v f_χ∫d³q/(2π)³ Σ_ab𝔇_abS_ab = tr[𝔇ᵀS] δ(ω − ω_q) [amended R8 (WP0-v3 G1): not tr[𝔇S], which differs when 𝔇 and S both have antisymmetric imaginary parts]; for O₁ and isotropic S,
  dℛ/dω = (ρ_χσ̄_e/(4πm_χρ_Tμ_χe²))∫q dq F_DM²η S̄. 1509.01598 eq. (17) is per target (×N_cell), 2311.04957 eq. (3) per cell.
  Library tables carry ΩS̄ (eV⁻¹).
  *Why:* WP0 (9.2) = WP6 (1.4) = Hochberg (S.9) = 1509.01598 eq. (17) with the |f_crys|² dictionary (audit A2–A5).
- Halo nuisances are not profiled in the headline: nominal and profiled limits use the fixed halo; the halo band is separate (WP6 (6.3)).

## 9. σ̄_e and F_DM
- σ̄_e ≡ μ_χe²|c₁|²/(16πm_χ²m_e²) = (μ_χe²/π)|Ṽ(q₀)|² at **q₀ = αm_e**, defined in vacuum; screening lives only in S.
- F_DM(q) = (m_V² + α²m_e²)/(m_V² + q²) (KKL eq. 12): heavy mediator 1, light mediator (αm_e/q)². F_DM multiplies the amplitude and
  enters the rate as F_DM². Operator-specific mediator factors are F_DM,i (WP0 (2.2)).
- dσ/dq = qσ/(2μ²v²) is the standard normalisation; 2603.13052's dσ/dq is 2× this (WP3).
  *Why:* WP0 (2.3) anchor = D1 N5 = D2 §0 = KKL eq. (11); "σ̄_e in vacuum" removes the κ² ambiguity found in the Dirac literature (WP4).

## 10. Terminology
- **"Debye–Waller" (DW) means only the Franck–Condon / Lamb–Mössbauer reduction e^{−2W} of zero-phonon weight**, with
  2W_κ(q) = q·B_κ·q, B_κ = ⟨u_κu_κ⟩ (direction-dependent unless the site is cubic). The O(u²) Allen–Heine vertex and its self-energy are
  the **AH tadpole** g^{AH}, Σ^{AH}, never "DW". Huang–Rhys factor S_HR = total FC exponent (= 2W in the lattice sector; from g_cc − g_vv
  for an electronic ZPL). Compensation statements are **first-moment** statements; there is no zeroth-moment rule for n_e.
  *Why:* REF-A/REF-B and SOTA R2: the two "DW" objects behave oppositely in the f-sum.
- **Final-state sectors (WP0 Theorem D):** GS (electronic ground surface; was "G"), X0 (electronic excitation, zero net reference
  phonons), X+ (electronic excitation, ≥ 1 net phonon); X ≡ X0 ∪ X+ (Migdal sector of S_κκ).
- **ZPL** = the X0 part of S_ee (zero-phonon line, renormalised). **Sideband** = the X+ part of S_ee (one or more net phonons). **PAER** =
  the X+ sideband at n_g = 2 with an e–h final state (L8). "First-order" and "zero-phonon" both mean the ordinary DM–electron transition.
- **Window** = D1 §5.4: ω ≤ E_min^{ren}(q,T) − δ₀, δ₀ ≫ max(ω_Q, Γ, T), with the bound |d| ≥ min(E_min(q) − ω, E_g − ω_max). Inside it the
  X0/X+ split is unique. **Outside it the split follows the Dyson convention (DC, O4's "C1")**: δ part → X0 (handed to the cascade),
  Hadamard finite part fp(1/δω²) and PV parts → X+; the code-pair conditions O4 d1–d11 are mandatory.
  *Why:* O4 (iv″a,b) proves that totals and the quanta distribution are convention-independent only with one declared kernel.
- Measured ELF/σ₁ data contain X0 + X+; never add a computed sideband to measured data, nor PAER to a ZG spectrum (WP3 N4).

## 11. Truncation multi-index τ (WP0 §6.1, amended)
**τ = (n_B, n_g, n_A, 𝒳, n_T, K, 𝔐, n_D)**:
- n_B: BO order (0 = clamped nuclei); n_g: e–ph order; n_A: anharmonic order; n_T: thermal **order** (not a temperature); n_D: multipole order;
- 𝒳 ∈ {IP, RPA, RPA+LFE, TDDFT, BSE}: kernel-ladder rung (was "X"; renamed because X is a sector);
- K ∈ {1ph-coh, 1ph-inc, multi-coh, multi-inc, imp}: kinematic regime, with "inc" = incoherent (shell terms dropped). This replaces the
  x_coh control and the "coherent 1-ph (x_R ≪ 1)" label (WP2 D1, D3);
- 𝔐 ∈ {ad, sud}: Migdal regime.
Mandatory metadata (not orders): T; reference state ref ∈ {normal, BCS, LSWT, …} (broken-symmetry references are not finite orders,
WP0 §1.2, WP4 D2/D4); screening set scr ⊆ {ext, LFE, DFPT, pair, ion}; resonance convention conv ∈ {window, DC}.
Library string: `nB=0|ng=0|nA=0|X=RPA+LFE|nT=0|K=-|Mg=-|nD=-` + `T=130K;ref=normal;scr=ext,LFE;conv=window`.
Nuisances are increments Δ^τ_k = S^{τ+e_k} − S^τ entered with the positivity-preserving types M (scalars or PSD geodesic), A (PSD increments), E, Δ, T (tilted; L its linearisation)
of WP6-v3 (5.1)–(5.1″), not WP0's additive
Gaussian (WP6 W2). *Why:* τ is the shared key between WP6's library and every LIMITS entry; the amendments remove three label
clashes and the temperature-in-an-order-slot ambiguity of WP6 §7.3.

## 12. Error-tag and status vocabulary
- Step tags: **[D]** DERIVED (hypotheses stated); **[D, sketch]** derived with a step outlined, not written out; **[E]** ESTIMATED
  (order-of-magnitude or model number); **[C]** CONJECTURED. "Standard" is not a tag.
- Literature tags: **[FT]** read in full text; **[ABS]** abstract or title only; **[UNVERIFIED]** quoted from memory.
- Claim status (SOTA): CLAIMED (one return) · CROSS-CHECKED (two independent routes agree) · REFEREED (R×2) · OPEN · AMENDED ·
  WITHDRAWN · SUPERSEDED (replaced by a named later result).
- Referee verdicts: STANDS · STANDS WITH CORRECTION · FALLS. Checks: PASS/FAIL. LIMITS pointers: ✔ confirmed, ✎ corrected.
- Owed-correction types (CORRECTIONS.md): **S** substantive, **N** notation rename, **W** wording/scope.
  *Why:* the returns already use these words; fixing their meaning lets SOTA and CORRECTIONS be read without the source return.

## 13. Disagreements between returns, and decisions
| # | Item | Positions | Decision |
|---|---|---|---|
| 1 | Isotropic halo factor | D1 η/q; REF-B "verified" η/q; REF-A, WP0, WP2–WP4, WP6 η/(2q) | **η/(2q)** (audit A1); D1 and REF-B §1 owe corrections |
| 2 | v_E | NOTATION v2 250 ("v_E"); WP6 252.1 annual mean; 2105.00599 |v_⊙| = 250.5 | v_E(t) in integrals; v_E^ref = 250.5, v_max = 794.5 (§8) |
| 3 | ρ_χ | NOTATION v1 0.4; WP2/WP6 flagged; coordinator 0.3 | **0.3 GeV/cm³** (already in NOTATION v2; flags resolved) |
| 4 | M^{(2)} normalisation | D1 (no 1/√N); D2 (1/√N); WP0 (5.6) uses D2's | **D1** (§5) |
| 5 | ℓ_Q | D1/X1/WP3 N outside; WP0 (4.9) N inside | **N outside** |
| 6 | Soft limit C7 | D1, D2, WP0 (4.9) vs X1 | **X1 C7a–e**; CONTROLS C7 last sentence is stale (defect) |
| 7 | "DW" | D1 e^{−2W} vs D2 AH tadpole reading | **FC e^{−2W} only** (§10) |
| 8 | Pair-channel screening | R1 two classes; REF-A ε(q,ω∓ω_Q); WP0 (5.7); X2 (2.2) | **X2 (2.2)**; REF-A exact for the convective part only |
| 9 | Letter c, v | X1/WP0 c, c_s = sound speed; c, v band labels; c_s coupling vector | sound speed **c_ν**; c, v band subscripts; c_s species coupling |
| 10 | [T_e, n] | WP0 (4.6)/(5.3) extra (q²/2m)n | **WP1 form** (audit A13) |
| 11 | Hyperfine contact | WP0 (2/3)σ·𝐈 | **WP4: +(1/3)g_eμ_Bg_Iμ_Nσ·𝐈δ³ = +(2/3)… s·𝐈δ³** (audit A18) |
| 12 | f-sum normalisation | WP0 (8.2) 2π𝓃q²/m | **π𝓃q²/m over ℝ** (WP6 W1, audit A12) |
| 13 | Nuisances, band | WP0 (8.1) additive Gaussian, (8.3) envelope | **M (scalars or PSD geodesic), A (PSD increments), E, Δ, T (tilted; L its linearisation) of WP6-v3 (5.1)–(5.1″), and three reported objects** |
| 14 | ZG | WP0 "stochastic evaluation" | **deterministic one-shot quadrature of Williams–Lax** (WP3) |
| 15 | L7d sector | WP0 "X0, not X+" | **n = 0 term X0, n ≥ 1 terms X+** (WP3) |
| 16 | External LFE weight | X2/WP0 (7.2) (ε^{-1})_{G0}; WP1 [E2] (1+Rv)_{0G} | **out-state retarded weight; WP1 [E2] with ρ* (CC-1 closed R7)** |
| 17 | Zeroth moment | REF-B, WP3 J4: no n_e rule; O4 (vi) "Z + fp = 1"; X1 BN soft-sector rule | consistent once scoped: O4's identity covers the Fan (Z) part per pair; the vertex term changes |ρ̃|², so no global rule |
| 18 | Sector letters | G (sector) vs G (reciprocal vector); X (sector) vs X (ladder) | **GS** and **𝒳** |
| 19 | Transverse-current screening | WP0 unscreened; WP1 LFE-screened | **WP1** |
| 20 | Theorem D (i) positivity | WP0 each sector PSD; O4: not outside the window | **O4**: per-sector PSD only in the window or for bins ≳ δ |
| 21 | Plasmon as a final state | WP0 (7.1) separate label; WP5 double count in RPA | **WP5**: Λ = cvk only within RPA, except an undamped RPA pole (metals, q < q_c): final state 𝔱 = pl (WP5-v3 IF-R8-3) |
| 22 | Boost mass in L7a | WP0 M; Ibe m_A; WP3 J3 dressed mass | atomic L7a uses m_A; crystal uses M_κ with the drag-mass correction δM_κ (WP3 J3) |
| 23 | Stored-energy convention (2026-11-01) | WP7-E v2 ΔZPE inside E_st; WP5 (W12), WP7-T T-1 configurational | **configurational** E^{conf}_i ≡ E^ad_0(R_i) everywhere; ΔZPE is an explicit correction inside ℋ_ph = ℋ_ph^{avail} + ΔZPE (only ℋ_ph^{avail} reaches a sensor). *Why:* T-1 is an identity only with one E^{conf} table (VER-WP7-E-A) |
| 24 | WP7 LIMITS labels (R13 merge) | B1 LB1-n, B2 B2-Ln, D L-Dn, T L25–L32, E L33–L38 | return-local labels kept, always prefixed; only T and E extend the global L-numbering (L25–L38). *Why:* renumbering would break every cross-reference in the refereed returns |
| 25 | geom metadata | D {bulk, body} (IF-D3); B1 {1D, 2D, stack} (IF-B1-9) | **one key, geom ∈ {bulk, body, 1D, 2D, stack}**; default bulk; 1D/2D/stack rates converted to per target mass (§11) |
| 26 | New τ values (WP7) | B2 K=el, ref=glass, nA=SCHA, src=data; T ref=def(·) | adopted (§11 amendment below) |
| 27 | Relativistic DM vertex (IF-B1-6) | §9 is NR only | adopted as a §9 amendment row (below); the NR F_DM(q) is its ω ≪ q limit |
| 28 | "observed" status (L-D10) | §12 has no word for a pattern verified to a finite order but not derived | **observed** added to §12 |
| 29 | r_mat and profile/envelope (2026-11-01) | WP6-v3 default r_mat = 0 (1 as a variant); OW6-4 | **method nuisances (𝒳 rung, XC PCs, pair-screening factor, yield model, 𝒜_ph) r_mat = 1 across materials computed with the same method and version; independently measured inputs r_mat = 0. The conservative choice depends on the sign of the two elasticities: for same-sign elasticities combined limits use r_mat = 1 and rankings report r_mat = 0 bands; for opposite signs combined limits use r_mat = 0 and rankings r_mat = 1; the sign is read per (nuisance, material pair) from the library. Headline = profile (WP6-R2), band = envelope (WP6-R3), declared in the library header.** *Why:* over r ∈ [0, 1] the variance of a sum is maximal at r = 1 and that of a ratio at r = 0 exactly when e_Ae_B > 0, and the reverse when e_Ae_B < 0 (CW7-errata §1.9, CW7-C16) |
| 30 | LIMITS labels R14–R16 (CW8-A merge, 2026-11-01) | WP8-R L39–L42 (R13, re-issued by v2); GAP-EF v1 L39–L43 (collision, GAP-EF-v2 IF-EF7); CW/CMPMC/COMP returns propose local labels; CMPMC-AUD "AUD-Ln" vs WP5-AUD "AUD-n"; two rows labelled L17 | **only WP8-R (L39–L42) and the coordinator-assigned cascade/defect rows L43–L46 extend the global L-numbering; all other packages keep return-local labels, always prefixed (L-EF, CW2-L, CW4-a…g, CW6-L, L-H, L-F, LU/LT, L8-N, L9-N, primed CW3 rows); GAP-EF v1 L39–L43 withdrawn (→ L-EF1…L-EF5); AUD-L/DEV-L → CMPMC-AUD-L/CMPMC-DEV-L; the R1-table L17 → R1-L17.** *Why:* WP8-R was the first to propose L39–L42 and LE-168 lists them so; row 24 practice keeps every refereed return's cross-references valid; prefixes remove the remaining duplicates (§14) |
| 31 | Status after a single verification (CW8-A merge, 2026-11-01) | R16 verifiers (VER-CWn, VER-GAP-EF-v2) read each return once; §12 has REFEREED (R×2) and CLAIMED only | **a claim verified once (R×1) after its return, with every verifier item answered in an errata, is REFEREED only if its package also had R×2 (e.g. GAP-EF: R14 R×2 + VER; WP8-R/U/F: R14 R×2 + VER-CW6/CW7; WP5-AUD: R14 R×2 settled in CW5); otherwise it is CLAIMED + VERIFIED (CW2…CW7).** The row's own status word (DERIVED, observed, …) is kept. *Why:* one verifier answers the verifier's questions, not a second independent reading; the brief of the R16 merge fixes this reading |
| 32 | ZrTe₅ Δ_D (CW8-A conflict C) | WP8-U-v3/table v4 11.75 meV; CW4-errata 11.8 meV and "not in the cited source" | **11.75 meV as printed in 1910.02091 (Eq. (1.1), half-gap), tagged [FT, primary provenance unverified]**: the number is the source's; only its "Exp. [52]" attribution fails (VER-CW4). 11.8 is the same value rounded |
| 33 | Al Δ_BCS (CW8-A conflict C) | table v4 0.3 meV (film-like, 2109.04473); bulk ≈ 0.18 meV from T_c | **bulk 0.18 meV [E, BCS 1.764 k_BT_c] for bulk Al; 0.3 meV only for thin films, labelled as such** (owed table row, CORRECTIONS §19) |
| 34 | LU3 vs CW6-L4 (CW8-A conflict C) | WP8-U-v3 withdraws LU3; CW6-errata upgrades it | **withdrawn as LU3; content carried as CW6-L4** (CW8-A ruling adopted) |
| 35 | ref=CDW metadata (CW3 proposal) | proposed only | **adopted** (§11 ref values) |
| 36 | ERR-CW7 new content (JARVIS shear-order fix, table v4, L-F4, c_NR1) | CLAIMED | stays CLAIMED until VER-ERR-CW7 (R17) |
| 37 | CW8-B judgement calls (R17) | 𝔘_C in the §7 basis; L30 prefactor spec authored in CW8-B; conditional 𝔘_C screening sentence | **accepted**: 𝔘_C = ∂H/∂ln α is a target operator (modulus-coupled DM, WP7-D (D.8)) and belongs in the basis as a two-body row; the L30 spec is tagged CLAIMED (coordinator-authored, no return); the screening sentence stays conditional until a return derives it |
| 38 | WP8-U screening S2 (synthesizable at ≥ 1 g) | single crystal ≥ 1 g | **≥ 1 g total target mass, reachable as an array/stack of individually instrumented crystals of ≥ ~0.1 g each with demonstrated mK readout** (user, 2026-11-01: "gram scale experiment is still feasible by running multiple / stack of 0.2 g substrate"). Array penalties carried as stated caveats, not as a FAIL: per-crystal readout channels and thresholds, larger surface-to-volume ratio (surface backgrounds), and per-crystal low-energy-excess and stress-release rates. Diamond (0.175 g CVD crystals at mK, W-TES at 16.8 eV, 2310.05815) passes S2 under this rule |
| 39 | WP8 status word (CW8-FINAL conflict) | VERIFIED vs REFEREED | **REFEREED**: WP8-U/R/F had R×2 at R14, R16 v2 revisions, then R16–R17 verification of every later change with 0 FALLS (§13 row 31 applies) |
| 40 | LE-171, LE-172 (book-side gates and Part II–III ledgers) | CANNOT-CLOSE in campaign files | **carried to the book**: closed by the Part II–III spine design (SPINE-II), which reads SOTA "R17 final state" |

## 14. Citation of labels
Equation, check and defect labels repeat across returns (C1 is a control, a WP1 check, a WP2 check and O4's convention; W1 is a WP5
equation and a WP6 defect; D1 is a return and a defect label in WP1, WP2, WP4; N1 is a return, a D1 convention, a WP3 rule, a WP6 flag).
**Always prefix a label with its return:** "WP6-W1", "WP5 (W1)", "WP3 (W.1)", "WP1-D4", "CONTROLS C1", "O4-DC". Unprefixed C1–C8 mean
CONTROLS.md.


## R8 amendments (2026-10-31, from the WP0-v3 interface flags)
- R^∞ ≡ 0 for every operator; the physical current kernel is R^{phys}_{j^αj^β} = R + δ_αβ𝓃_s/m_s (G11).
- The Born–Oppenheimer remainder is O(κ_BO^{2(n+1)}) (G10).
- The nonreciprocal part of a density S is O(q³) (G12).

## R13 amendments (2026-11-01, WP7 merge decisions; §13 rows 23–28)
- **§11 τ values.** K ∈ {1ph-coh, 1ph-inc, multi-coh, multi-inc, imp, **el**}: el = the elastic (n_ph = 0) term of a disordered or medium-scale target (WP7-B2 IF-B2-13). n_A ∈ {0, 1, …, **SCHA**}: SCHA = self-consistent harmonic resummation (Gaussian trial state, WP7-B2 §4), not a finite order. Metadata: ref ∈ {normal, BCS, LSWT, **glass**, **def(STM|band|cr)**} (glass = configurational average of a disordered reference, WP7-B2; def(·) = defect double-well/defecton/crowdion reference, WP7-T); **src ∈ {theory, data}** (data = measured S_{ss} used directly, WP7-B2 (B2.6.1)); **geom ∈ {bulk, body, 1D, 2D, stack}** (row 25); **basis ∈ {crystal, molecular}** (WP7-B1 E5). WP7-T's withdrawn v1 value K=def is not a τ value.
- **§9 relativistic DM (IF-B1-6).** For relativistic DM and a vector mediator the density-row mediator factor is F_DM^{rel}(q,ω) = (1 − ω²/q²)(q₀² + m_V²)/(q² − ω² + m_V²) (Coulomb 1/q² form for m_V → 0), plus a transverse row (Fermi 1940; 2608.20715 Eq. (2)); WP7-B1 §12. F_DM(q) of §9 is its ω ≪ q limit. Use only in WP7-B1 §12 channels; NR channels keep §9.
- **§12 status.** **observed**: a pattern verified to a stated finite order (or numerically) but not derived; weaker than DERIVED, never upgraded without a proof (WP7-D L-D10, VER-WP7-D-A E3).
- **§12 provenance tag [CALC]** (2026-11-01): a value computed in this campaign (QE/EPW etc.). Valid only with code/<ID>/ holding the inputs, pseudopotential names (code/ENV.md standard), the convergence record and the CONTROLS case passed. Ranks with [DB] below [FT] measured values for material properties.

## R16 amendments (2026-11-01, CW8-A merge of the verified R14–R16 returns; §13 rows 29–31)
- **§12 provenance tag [DB]** (owed by CW7, pointer as re-issued in CW7-errata §2.1; WP8-U-v3 IF-U11): [DB] database entry with ID and field (JARVIS-DFT `JVASP-n`, MP/Alexandria OPTIMADE, NIST, IAEA); ranks below [FT] and [CALC]; DB fields obey the vetting rules V1–V6 of returns/R16/WP8-U-v3.md §1.3 (JARVIS `elastic_tensor` shear order (xy, yz, zx), re-indexed to Voigt before use). *Why:* WP8 rows used DB values without a declared rank or vetting rule; the R14–R16 non-cubic elastic tensors were built with C₄₄ ↔ C₆₆ swapped because the JARVIS shear order was read as Voigt (WP8-U-v3 §0 row 10, CW7-C33).
- **§12 status words:** **CLAIMED + VERIFIED** (one return, verified once with every verifier item answered in an errata, package without R×2) is added; it ranks above CLAIMED and below REFEREED (§13 row 31). *Why:* it is the status of every R16 closure package (CW2–CW7).
- **§7 operator basis:** 17 rows (𝔳²_s added; §7 text above). *Why:* CW3 §3.1 derives the 𝒪₂ matching (LE-79, IF-CW3-5).
- **§11 metadata (proposed by CW3 IF-CW3-6, adopted):** ref ∈ {…, **CDW**} (charge-density-wave mean-field reference with the GRPA double-counting rule of CW3-errata §1.13 LE-81: the phonon-mediated interaction enters either Γ or D⁻¹, never both). *Why:* Theorem D-m and the CDW phason/amplitudon formula need a declared broken-symmetry reference (WP0 §1.2: broken-symmetry references are metadata, not orders).
- **WP8 data tables (reading rule):** for any (material, property) with several rows in returns/R16/WP8-U-table-v4.csv the last row whose note says "supersedes" wins; the screening keys `screen_S1–S3` and the `verdict` column are unique and final (WP8-U-v3 header). *Why:* v1–v3 carried contradictory keys (13 duplicates; VER-CW7 §A).

## R17 amendments (2026-11-01, CW8-B; LE-175)
- **§7 operator basis:** 17 one-body rows per species plus the two-body row 𝔘_C (§7 R17 text). *Why:* WP7-D-v2 (D.8) couples δα/α to ∂H/∂ln α, the Coulomb energy. That
  operator is exact for H_C (WP0 (1.1)) but is no combination of one-body bilinears, so a scalar-modulus rate cannot be written in the 17-row basis without it (IF-D2;
  WP7-D REFEREED R12).
- **§7 DM-side tensors:** 𝔇^F (fermionic absorption) and 𝔇^{pair} (pair absorption) are recorded as DM-side tensor classes beside 𝔇. They add no target row. *Why:*
  WP7-D-v2 §2.1 maps every target bilinear of (F.1) onto existing rows ("the new class is DM-side"), and (T.2) uses only n, j, tr J, s. What changes is the DM-side
  normalisation (1/(4E_χE_ν̃), 1/(4E_pE_p̄)) and the kinematic curve, and these do not fit the single-χ, NR definition of 𝔇.

## R17 final-merge notes (2026-11-01, CW8-FINAL; no new decision, status bookkeeping of §13 rows 30 and 36 only)
- **Row 30 (labels):** the R17 merge adds the return-local prefixes **CW1-L** (CW1-L1…L9), **L-S** (WP8-S, L-S1…L3) and **L-EW** (WP8-errata, L-EW1); no global L-number
  is assigned. LIMITS labels remain unique.
- **Row 36 (ERR-CW7 content):** its condition is met: referees/R17/VER-ERR-CW7.md and VER-ERR-WP8.md verified the ERR-CW7 and ERR-WP8 content (0 FALLS). The WP8 chain is
  recorded as **VERIFIED** (state/SOTA.md "R17 final state"); under row 31 the content of packages that had R14 R×2 would read REFEREED (coordinator to confirm the word).

