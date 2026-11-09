# R5 / WP3: the mixed electron–lattice sector (non-adiabatic) of the URF

Isolated theory agent, brief R5/WP3. Read scope as in the brief. Theory only. Checks are in `code/WP3/checks.py`:
27 sympy/numpy identities, all PASS, under 1 s. They are cited as [C1]…[C10].
Tags: **[D]** DERIVED (hypotheses stated), **[E]** ESTIMATED, **[C]** CONJECTURED.
Equations are numbered (W.n). WP0 equations are cited as WP0 (s.n) and are not re-derived.
Notation: NOTATION.md + WP0 §10, as listed in §12. Units: HL, e² = 4πα, unless a source formula is quoted in its own units.
**FT** means the formula was read in full text. All 23 arXiv IDs were checked against the arXiv API (§11). PDFs deleted.

## 0. Results in brief
1. **Joint response [D].** (W.1) defines S_ab(q;ω_ph,ω_e) in the decoupled frame of WP0 Theorem D. Its marginal over the split is
   exactly S_ab(q,ω) (W.2). (W.4)–(W.6) give it explicitly for the coupling matrix {n_e, n_κ} at the order τ_J stated in §1.3.
   Seven sum rules (J1–J7) hold. Two of them are new as far as we found:
   - the **ω_e-moment of the Migdal spectrum equals the Born–Huang electron-drag mass**, q·δM_κ·q/2M_κ² (J3);
   - **the electronic part of the e–N cross first moment is −(q²/m_A)F(q)** (J7).
   Together with the PSD sector projectors, they give **no double counting** between multiphonon and Migdal, and between PAER and ZPR,
   as quantitative identities (§1.5).
2. **Migdal family [D].** One formula, the nuclear X-sector entry (W.5), reduces by stated truncations to:
   - 2210.06490 Eq. (3.8) (L7c), with 2505.08864 Eq. (21) as its amplitude;
   - 2011.09496 Eqs. (3), (6) (L7b): impulse + soft limit, prefactor 4α reproduced [C2];
   - 2205.03395 Eqs. (3.1)–(3.4) (L7d);
   - 1707.07258 Eq. (57) (L7a): one nucleus, exact Galilean boost.
   Found in the sources:
   - 2603.13052 Eq. (4.7) is dimensionally wrong as printed (m_N must be m_N²) and is ½ of KKL. The ½ is compensated by its
     dσ/dq, which is 2× the standard [C3].
   - The "EFT breakdown" at q ≈ √(2Mω_g) (2210.06490 fn. 3) is conservative. The true expansion parameter is |q·p|/(M ω_e) ≈ 4×10⁻³ [C9].
3. **PAER (M1) [D].** S^{X+}_ee with X2's screened amplitude M̃ (W.4c). Checks of the two returns:
   - X1 is algebraically correct [C1a,e].
   - WP0 (4.9) is X1 only at band extrema. It misses the Galilean P_n terms [C1b–d] (WP0 defect 1).
   - WP0 (5.7) is X2 (2.2) truncated: scalar, resonant pairs only, effective one-body operator (WP0 defect 2).
4. **L9 [D].** The 8π²α/(Ωω²) prefactor is now confirmed in full text (EPW 2302.08085 Eq. (63); Noffsinger 1202.3454 Eq. (1)). This closes the SOTA item.
   **L9b [D]:** we derive the X+ part and give a temperature-transfer rule for data-driven σ₁. Scalar absorption: a new phonon-assisted τ_e channel.
5. **L12 [D].** Williams–Lax/ZG is the ω_ph-marginal of the adiabatic joint S, with the phonon energy dropped from the δ
   (1604.02394 Eq. (24) says so explicitly). The URF leading correction is a T-independent first-moment shift +Σω_Q|M|² [C6a].
   At T = 0 the onset is too low by ω_ph (18–58 meV in Si). This is material for the 0.34–0.47 MeV PAER window.
   Rule: never add a separately computed PAER sideband to a ZG spectrum.
6. **Crystal NR bremsstrahlung (gap) [D].** Rate ∝ n(ω)|Z*_κ(ω)·q/M|² × S^G_κκ(q,ω_ph) (W.13), where Z*_κ(ω) is the dynamical Born charge.
   It reduces to Kouvaris–Pradler 1607.01789 Eq. (8) in vacuum [C8].
   - **Non-polar Si/Ge:** Z*(0) = 0, so it is suppressed as ω⁴.
   - **Polar targets (GaAs):** Z*(0) ≈ 2 gives a sub-gap photon channel, ~10³× the atomic estimate [E].
7. **Exciton–phonon replicas (G5 part) [D].** Formula (W.14) and specification. Effective-mass limit: replicas at E_x(P) ± ω_ν with √ onsets.
8. **WP0 defects:** six items, in §9.

## 1. The joint response S(q; ω_ph, ω_e)

### 1.1 Definition [D]
Hypotheses: WP0 (H1)–(H4); (H5) where the X0/X+ label is used (otherwise §1.6); harmonic plus perturbative anharmonicity.

Let U = U_n ∘ U_ep be the decoupling unitary:
- U_n: WP0 §6.2 (space-adiabatic, BO order n);
- U_ep: a Schrieffer–Wolff transformation that removes O(g) intra-X scattering. It exists under (H5), where every such process is off shell.

In the decoupled frame H′ = U†HU is block diagonal to O(κ^{n+1}, g³). Write H′ = Ê_e + Ê_L:
- Ê_e = Σ_a ε_a^{ren}|a⟩⟨a| is the electronic-label energy. It is constant on each block a, where a = ground, e–h pair (c k+P; v k),
  exciton, or core hole. ε_a^{ren} is the AHC/ZPR-renormalised vertical label energy at T.
- Ê_L ≡ H′ − Ê_e is the lattice energy: phonons, plus nuclear recoil to all orders.

Both commute with H′. Hence:

  S_ab(q;ω_ph,ω_e) ≡ (2π/V) Σ_{i,f} p_i ⟨i|O_a′†|f⟩⟨f|O_b′|i⟩ δ(ω_e − E^e_f + E^e_i) δ(ω_ph − E^L_f + E^L_i),   O′ = U†OU.        (W.1)

  **Marginal theorem:** ∫dω_e S_ab(q; ω−ω_e, ω_e) = S_ab(q,ω) (WP0 3.1) + O(κ^{n+1}, g⁴).                                         (W.2)

The labels are energies of the *prompt* final state (WP0 7.1). Final-state sectors: Theorem D's G = {ω_e = 0}; X0 = {ω_e > 0, ω_ph = 0 at harmonic order, zero net phonon change}; X+ = the rest.

Hence S = S^G + S^{X0} + S^{X+}, each PSD (WP0 6.1). Rate: Γ = ∫d³q/(2π)³ ∫dω_e dω_ph Σ_ab 𝔇_ab S_ab(q;ω_ph,ω_e) δ(ω_q − ω_e − ω_ph) (WP0 3.3).
The split (ω_e, ω_ph) is the hand-over WP5 needs (WP0 7.3).

### 1.2 Why this split
For the electron operator, ω_e is the e–h (or exciton) energy and ω_ph is the phonon energy (PAER sidebands, ZPL at ω_ph = 0).
For the nuclear operator, ω_ph is the lattice recoil/multiphonon energy and ω_e is the Migdal electron energy.
2210.06490 states (p. 9) that a structure factor "that incorporates the Migdal effect directly" is "practically challenging".
(W.1) is that object. It is defined at every BO order.

### 1.3 Explicit entries at order τ_J
τ_J: n_B = leading non-adiabatic (κ⁴ amplitude at the nuclear vertex); n_g = 2 at the electron vertex (one-phonon sideband amplitude O(g));
harmonic lattice, all orders in q·u; X = RPA(+LFE) on every Coulomb line (WP0 5.5, X2 §3); T ≪ E_g; incoherent nuclear S unless stated.

**(W.4) Electron–electron.**
- (a) **G:** S^G_ee = δ(ω_e) Σ_{κκ′} 𝓕_κ(q)𝓕*_κ′(q) S^G_{κκ′}(q,ω_ph).
  𝓕_κ(q) is defined by iq·𝓕_κ … ≡ ∂⟨n_e(q)⟩^{ad}/∂u_κ (DFPT). In the rigid-ion approximation it is the atomic electron form factor.
  This is adiabatic electron-following (WP0 6.2 ii).
- (b) **X0:** S^{X0}_ee = δ(ω_ph) S^{ren}_ee(q,ω_e). This is the clamped response with AHC energies plus the O(g²) Fan-Z, mixing and
  vertex corrections of D2 §2c, and the FC/e^{−2W} weight reduction. It is screened (WP0 7.2). It vanishes in the PAER window.
- (c) **X+ (PAER):** S^{X+}_ee = (4π/Ω)⟨⟨Σ_{cvν±}(n_{Qν}+½±½)|M̃_±|² δ(ω_e − ε̃_{c,k+q+Q} + ε̃_{vk}) δ(ω_ph ∓ ω_{Qν})⟩⟩.
  M̃ is X2 (2.2) (with ρ̃ and the pair channel), and D1 (1) gives M. Equivalently S^{X+} = (2q²/e²)L^{PA} by X2 (2.3).

**(W.5) Nuclear–nuclear (species κ), X sector (Migdal).** The leading non-adiabatic amplitude is (WP0 6.2 ii; 2505.08864 Eq. (21))

  A_f = Σ_{I∈κ} ⟨χ_f| e^{iq·R_I} (q/M_κ)·⟨a|∇_{R_I}Φ₀⟩/(E_a−E_0) |χ_i⟩,   ⟨a|∇_RΦ₀⟩/(E_a−E_0) = −⟨a|∇_R V|0⟩/ω_e².

Write ∇_{R_I}V = (1/V)Σ_p (ip) U_κ(p) e^{−ip·R_I} n_e(p), with U_κ(p) = Z_κ(p)e²/p² the ion potential (cores frozen into Z_κ(p)).
Resum the (p, ω_e) Coulomb lines (WP0 5.3, second term of R_NN). Then take the Condon and ground-surface truncations T1, T2 of §2. This gives

  S^X_κκ(q;ω_ph,ω_e) = (1/2π) Σ_{GG′} ∫_BZ d³k/(2π)³ [q·(k+G)][q·(k+G′)] U_κ(k+G)U*_κ(k+G′)/(M_κ²ω_e⁴) · S^{ee}_{GG′}(k,ω_e) · S^G_κκ(q−k−G, ω_ph),     (W.5)

where:
- S^{ee}_{GG′} is the full (screened) electron density response matrix;
- S^G_κκ is the ground-surface lattice structure factor (WP2).

Its δ(ω_ph) part (the e^{−2W} elastic term of S^G) is X0. The rest is X+.
Scalar check: with S^ee = (2k²/e²)Im[−ε⁻¹], (W.5) = S^G × 4α∫d³k Z²(q·k)²Im[−ε⁻¹]/((2π)³M²ω_e⁴k²), which is KKL's dP/dω [C2b].

**(W.6) Mixed e–κ.**
- S^G_eκ = δ(ω_e) Σ_κ′ 𝓕_κ′ S^G_{κ′κ}: Born-charge / electron-cloud interference.
- S^{X+}_eκ = (2π/V) Σ_f A^{PAER*}_f A^{Mig}_f δδ: Migdal–PAER interference. It is nonzero because the Migdal one-phonon term
  (pair momentum P, phonon q−P) lands in the PAER final manifold. It is bounded by WP0 (4.4).

### 1.4 Sum rules of the joint response [D, under (L) of WP0 4.6 and τ_J]
- **(J1)** Marginal (W.2).
- **(J2)** ∫∫(ω_e+ω_ph)(S_ab+S_ab[O†])dω_e dω_ph/2π = M¹_ab (WP0 4.5–4.6).
- **(J3) Split first moments.** Define M¹^{(e)}_ab = V⁻¹⟨[O′_a†,[Ê_e,O′_b]]⟩ and M¹^{(L)} = M¹ − M¹^{(e)}.
  - For n_κ at leading order: M¹^{(e)}_κκ = n_κ q·δM_κ·q/M_κ², with
    δM_κ ≡ 2Σ_{a≠0} Re⟨0|∇_{R_κ}V|a⟩⟨a|∇_{R_κ}V|0⟩/(E_a−E_0)³,
    the Born–Huang non-adiabatic (electron-drag) mass tensor. Per nucleus, the Migdal energy moment is
    W_e(q) ≡ ∫ω_e dP/dω_e = q·δM_κ·q/(2M_κ²).
  - For an atom δM = N_e m_e exactly. This is the TRK sum: Σ_n E_n|⟨n|e^{−iq_e·Σr}|0⟩|² = N_e q_e²/2m_e to all orders in q_e [C4a–c].
  - Then M¹^{(L)}_κκ = n_κ q·[M_κ⁻¹ − δM_κM_κ⁻²]·q: the lattice sees the dressed mass M+δM. This makes WP0 6.2 (iii) quantitative.
  - Si, Ge: δM/M ≤ 2.7×10⁻⁴ and 2.4×10⁻⁴ (upper bounds, all electrons dragged) [C9].
- **(J4) Zeroth moment, n_κ, incoherent:** ∫∫(S^G+S^X)dω_e dω_ph/2π = n_κ, so S^G is depleted by P_Mig(q) (10⁻⁸–10⁻⁴).
  For n_e there is no zeroth-moment rule (REF verdict).
- **(J5) PAER/ZPR:** M¹ shift at O(g²): M₁^{SB} + ΔM₁^{X0} = 0 as a sum over SE-p, SE-h and V (REF-A aggregate; D2 3.1).
  In the joint form, the X0 loss sits at ω_ph = 0 and the X+ gain at ω_ph = ±ω_Q.
  The soft sector also obeys the X1 coherent-state (BN) zeroth-moment rule.
- **(J6)** Detailed balance per label: S_ab(−q;−ω_ph,−ω_e) = e^{−β(ω_e+ω_ph)}S_ba(q;ω_ph,ω_e) (both labels are differences of
  conserved block energies). PSD at each (ω_ph,ω_e) (WP0 4.4).
- **(J7) Mixed split.** M¹_eκ = 0 (WP0 4.6c), but M¹^{(L)}_eκ = −M¹^{(e)}_eκ = n_κ(q²/M_κ)𝓕_κ(q) ≠ 0, which is O(1/M) and not κ⁴-suppressed.
  - Hydrogenic/HO check: the electronic part is −(q²/m_A)F(q), verified by an explicit sum over states [C5].
  - Consequence: the X-sector of S_eκ (Migdal–ER interference, dark-photon-type couplings) carries ω_e-weight −n_κq²𝓕_κ/M_κ,
    equal and opposite to the lattice-energy weight of the G-sector Born-charge interference. A one-signed model of it is wrong.

### 1.5 No-double-counting rules (corollaries)
- **(N1) Multiphonon + Migdal.** A harmonic S^G_κκ normalised to the bare f-sum, plus (W.5), overcounts M¹ by exactly n_κq·δM·q/M²
  (≤ 3×10⁻⁴ relative) and the zeroth moment by P_Mig. Both negligible, but now identities, not "O(κ⁴)" statements.
- **(N2) Mixed approximations.** All four published Migdal formulas are truncations of (W.5) (§2). Combining, e.g., atomic Migdal for
  valence with a crystal multiphonon NR is a *different-truncation* error, not a double count.
- **(N3) Quenching data.** Neutron-calibrated NR ionization yields already contain Migdal (2104.01811 [ABS]).
  Use Y_tot(E_R) = Y_casc[S^G] + ∫dω_e P_casc(N|ω_e) dP/dω_e. Fit the calibration to the sum: never fit Y_casc and then add Migdal.
- **(N4) PAER vs ZPR.** Use S^{X0,ren} + S^{X+} with consistent renormalised energies (D1 §5.4). Do not add ZG (which contains an
  adiabatic X+) to PAER (§5).
- **(N5) Measured inputs.** Measured ELF/σ₁ contain X0+X+ (WP0 rule c).

### 1.6 Outside (H5)
Where a first-order transition is open, the X0/X+ label of the resonant part is fixed by the width prescription: Lorentzian → δ + Hadamard
finite part (SOTA R2). The joint S is then defined for the inclusive pair X0⊕X+ only [C] (WP0 O4).
For the soft-phonon sector, X1 §6.3–6.4 shows that the inclusive quantity is IR-safe.

## 2. Migdal: one formula, four truncations (L7a–d)
**Truncation chain from WP0 (3.1).**
- T0: Theorem D sector X of S_κκ; leading non-adiabatic order (WP0 6.2 ii). The adiabatic contribution vanishes for an infinite crystal
  (2505.08864 Eq. (12) [FT]).
- T1: Condon. ⟨a|∇_RV|0⟩ is taken at R₀.
- T2: ground-surface vibrational final states, χ_{a,ν′} → χ_{0,ν′}. This drops the e–ph displacement of the Migdal pair. Error O(2W_el)
  ≈ 0.02 (X1 §6.3 numbers).
- T3: RPA(+LFE) screening of the (k, ω_e) lines → (W.5).
- T4: diagonal G = G′.
- T5: lattice regime K ∈ {1ph/multi, imp}.
- T6: one nucleus.

**L7c (2210.06490 [FT]).**
- Source: Eq. (3.3) H_eff = ω⁻²[H_χL,[H_L,H_eL]], Eq. (3.6) H_eff = (m_Nω²)⁻¹Σ_I∇_I H_χL·∇_I H_eL, and Eq. (3.8)
  dΓ/dω = (8παN_T/V³)(g_χg_N/(m_Nω²))² Σ_{q,k_e,K,Q} q·(k_e+K) q·(k_e+Q)/(q²+m_φ²)² Z Z/(|k_e+K||k_e+Q|) Im[−ε⁻¹_KQ(k_e,ω)] S(q−k_e−K, E).
- Amplitude: 2505.08864 Eq. (21) M_non-ad = −i(g_χg_N/(V m_φ² M ω²)) Σ_I∫du e^{iq·X_I}χ*χ q·⟨φ_n′|∇_{X_I}V_eN|φ_n⟩ [FT].
- Chain: T0–T4, with K = harmonic or anharmonic S^G (the lattice potential drops out of the double commutator).
- **Equivalence [D]:** (W.5) at T0–T4 is Eq. (3.8) term by term. Their 1/ω² expansion of old-fashioned perturbation theory (Eq. (3.2)) is
  our non-adiabatic coupling −⟨∇V⟩/ω_e².
- Validity: ω_e ≫ ω_ph; T2 holds; T ≪ E_g.
- Leading correction [D for free recoil, E for bound]:
  - Keep the exact intermediate energies: (q·p/M)/ω_e² → [1/(ω′−Δ) − 1/ω′], with Δ = q·p/M and ω′ = ω_e + p²/2M.
    This is KKL's bracket.
  - The relative correction 2Δ/ω_e is odd in p. It vanishes after the angular average for an inversion-symmetric ELF.
  - The first surviving term is O(v_N²p²/ω_e², ω_ph²/ω_e²) ≈ 10⁻⁵ (Si, q = 100 keV, p = 5 keV, ω_e = 5 eV) [C9].
  - Their footnote-3 bound q ≲ √(2Mω_g) = 242 keV (Si), 301 keV (Ge) [C9] is therefore conservative. The EFT and the impulse formula
    are one function.
  - Next truncations: non-Condon ∂_u⟨a|∇V|0⟩, which interferes with PAER (W.6), and T2 (O(η_ep)).

**L7c, NR-EFT version (2603.13052 [FT]).**
- Eq. (3.4) has the same leading term. Eq. (3.11) is (3.8) with Σ_{n,n′} c c F_{i,j}.
- **Discrepancies:**
  - (i) Eq. (3.11) prints S(q−k_e+K, …) where 2210.06490 has q−k_e−K. Momentum conservation requires −K.
  - (ii) Eq. (4.7), dP/dω = 2αq²/(3ω⁴m_N)∫…, has wrong dimension. With m_N → m_N² it is ½ of KKL's 4αq²/(3m_N²ω⁴) [C3a].
    Their Eq. (4.8), dσ/dq = qσ̄/(μ²v²), is 2× the standard qσ/(2μ²v²). So the product, and hence the rate, is consistent [C3b] [E: the
    factor reading assumes σ̄ standard].

**L7b (2011.09496 [FT]).**
- Source: Eq. (3) (impulse; bracket [1/(ω − q_N·(k+K)/m_N) − 1/ω]²; F(p_i−p_f−q) Eq. (4)) and, in the soft limit,
  Eq. (6) dP/dω = 4α∫d³k/(2π)³ Z_ion²(k)|v_N·k|²/(ω⁴k²) Im[−1/ε(k,ω)], with v_N = q_N/m_N.
- Chain: T0–T4, T5 = impulse: S^G_κκ(q−k, ω_ph) → δ(ω_ph − |q−k|²/2M), or the Gaussian 2210.06490 Eq. (4.9). Then soft |k| ≪ q,
  which factorises dσ/dE_N dω = (dσ/dE_N)(dP/dω) (Eq. (1)).
- (W.5) → Eq. (6) with prefactor 4α exactly [C2a,b].
- Validity:
  - impulse needs q ≳ √(2Mω̄): 46 keV (Si, ω̄ = 40 meV) and 58 keV (Ge, 25 meV) [C9], i.e. m_χ ≳ 50–70 MeV (their text);
  - soft needs |k| ≪ q;
  - valence only (Z_ion).
- Leading corrections:
  - (i) the lattice binding of S^G (→ L7c);
  - (ii) off-diagonal ε⁻¹_{GG′}, O(1) per KKL;
  - (iii) as k → 0 the screened ion vertex must reproduce the Born-charge limit (Z*_κ(ω)/ε, WP0 5.3), which the diagonal Z_ion misses.
    This is small because the d³k measure suppresses it [E];
  - (iv) core shells add atomic-type Migdal (L7a) [D, T6 applied per core shell].
- Convention: their ELF uses the RPA "Lindhard formula" identity (2210.06490 fn. 4), i.e. electron-only coupling at ω_e ≫ ω_max, where
  WP0 (5.5)(ii) makes ε_e = ε to O(κ⁴).

**L7a (1707.07258 [FT]).**
- Source: Eq. (55) iT ≃ F_A M × Z_FI(q_e)×…, Eq. (57) Z_FI(q_e) = ∫Π d³x_i Φ*_F e^{−iΣq_e·x_i} Φ_I, Eq. (73) q_e = m_e v_F ≃ (m_e/m_A)q_A,
  rate Eqs. (91)–(92), dipole Eq. (86).
- Chain: T0 with one nucleus (T6) and free recoil.
  - For one nucleus, ∇_RV = −Σ_i∇_iV and ⟨n|Σ∇_iV|0⟩ = m_e(E_n−E_0)²⟨n|Σr_i|0⟩ (WP0 6.2 ii). The (W.5) amplitude becomes
    (m_eq/M)·⟨n|Σr|0⟩, the dipole term of Eq. (57).
  - To all orders: for one nucleus U_n is exactly the Galilean boost e^{im_e v·Σr}, which gives Eq. (57) [D].
- Validity: sudden (σ_c ≪ 1) and impulse;
  - isolated atom: false for valence electrons in a crystal (KKL), true for crystal **core** shells when r_core ≪ bond length and the
    binding ≫ valence bandwidth (Si 2p, Ge 3d) [E].
- Leading corrections: other nuclei (→ L7b); m_A vs M in q_e, O(Zm_e/M). By (J3) the physical choice is the dressed mass, which agrees with Ibe's m_A.
- Convention: Ibe's phase e^{−iq_e·x} is opposite to the boost e^{+im_ev·x}. |Z|² is unaffected.

**L7d (2205.03395 [FT]).**
- Source: Eq. (3.1) (virtual-phonon propagator i/((ε_i−ε_j)² − ω²_{k,α}) between the multiphonon blob and the bare vertex
  −iNZ_ion4πα/(V|k+G′|²)); Eq. (3.2) (reduced form q·(k+G′)/(m_N(ε_i−ε_j)²)); Eqs. (3.3)–(3.4) (incoherent harmonic sum Σ_n T_n,
  **including n = 0, T_0 = δ(E)**).
- Chain:
  - (W.5), with the nuclear inertial response written as off-shell phonon exchange: (2Mω_k)⁻¹·2ω_k/(ω_e²−ω_k²) = M⁻¹ω_e⁻²(1+ω_k²/ω_e²+…) [C7];
  - incoherent harmonic S^G;
  - screening imposed afterwards via the ELF (their HEG argument). This is T3 at RPA.
- The n = 0 term is X0. The n ≥ 1 terms are X+.
- Validity: as L7c.
- Leading correction: keeping the phonon pole is O(ω_ph²/E_g²) ≈ 10⁻³. That is the same order as the static-DFPT screening error (X2 §2.2)
  and the T1 non-Condon terms. **Keeping it alone is not a consistent improvement [D].**
- Convention: the bare Coulomb vertex with ε inserted afterwards equals (W.5) only at RPA. The (ε_i−ε_j)² of Eq. (3.2) is ω_e².

## 3. PAER, milestone M1 (L8), with X1 and X2 integrated
**State.** SOTA rows 1–10 are refereed or cross-checked. X1 and X2 have returned and are CLAIMED.
**L8 [D].** S^{X+}_ee at n_g = 2, (W.4c). Source: this campaign, D1 eq. (4) with M → M̃ (X2 (2.3)).
Chain: WP0 (3.1) → Theorem D, X+ → RS perturbation theory O(g²) (D1 (1), Pauli theorem) → three-channel screening (X2 (2.2)).

**X1 check (used here) [D].**
- (X1′) → (X1) holds identically for both signs [C1a].
- The synthetic C7e branch returns D2's form [C1e].
- The Ward identity (W) and (X2) Ξ = D + v⊗P are consistent with the ASR of WP0 (4.8 i, ii): the contact term ê·q is WP0's centre-of-mass amplitude.

**Reconciliation of WP0 (4.9) with C7a–e [D].** Algebra [C1]:
- WP0 (4.9) minus (X1) = ê·(P_c − P_v) if Ξ is read as the lab slope.
- If Ξ is read as the comoving D, the difference is the ∓cP numerator terms.
- They agree only at band extrema (v_n = P_n = 0) [C1d].

Adopted C7 = X1 §5 (C7a–e) verbatim, with three additions:
- (i) ℓ_Q is D1's (N^{−1/2} outside M). WP0's ℓ_Q contains N (D2 convention), so M_WP0 = M_X1/√N.
- (ii) The index order Q̂·Ξ·ê matters with non-local PPs (P ≠ m_ev makes v⊗P non-symmetric). Use X1's order.
- (iii) Upper sign = emission of −Q in both.

**X2 check [D].** X2 (2.2) contains WP0 (5.6)–(5.7) as the following truncation (WP0 defect 2):
- G = G′ = 0;
- the triangle T restricted to resonant c′v′ pairs;
- M continued off shell. D1's unrestricted-m form equals the true second-order source N_ab only on shell (D1 §1).

Both agree on the WP0 (5.6c) prediction: an external factor plus a projected pair-channel factor, reducing to |ε(P,ω_f)|⁻² iff M ∝ ρ.
This is X2's coherent-potential limit, M̃ = M/ε(P,ω_f), exactly. Both also give REF-A's ε(q,ω∓ω_Q) as the convective/Q → 0 limit.
**Use X2 (2.2).** The interim systematic factor [0.5, 1.2] on L^{PA} (X2 §6) stands until X2-N2/N3.

**Validity (Si) [E].**
- Window: ω ≤ E^{ren}_min(q,T) − δ₀, δ₀ ≫ max(ω_Q, γ, T).
- Mass window m_χ ≈ 0.34–0.47 MeV (SOTA; Umklapp check deferred).
- T = 0 onset E_g + ω_{TA} = 1.170 + 0.018 eV.

**Leading corrections:**
- (i) excitons (§7): onset −E_x^b (14.7 meV in Si [E]) and √ edges;
- (ii) O(g⁴) two-phonon sidebands, ~η_ep;
- (iii) anharmonic phonon widths, ~η_anh;
- (iv) the pair channel, if computed (X2-N2/N3);
- (v) the non-adiabatic amplitude is exact in D1 (1). The adiabatic HT form errs by ω_Q/δ (SOTA 8).

## 4. Phonon-assisted absorption (L9, L9b)
**L9 source [FT].**
- EPW 2302.08085 Eqs. (60)–(63): S1 = Σ_j g_mjν(k,q)v_jn(k)/(ε_jk−ε_nk−ħω+iη), S2 = Σ_j v_mj(k+q)g_jnν(k,q)/(ε_{j,k+q}−ε_nk+βħω_qν+iη).
  Im ε = 2(πe²/(ε₀Ωω²))Σ∫∫|e·(S1+S2)|² P δ. The "2" is spin. SI units.
- Noffsinger 1202.3454 Eq. (1): α(ω) = 2(4π²e²/(ωcn_r))(V_cell N_kN_q)⁻¹Σ|λ·(S1+S2)|²Pδ (Gaussian).

**Chain:** L8 → q → 0 (C1; D2's exact commutator proof) → transverse projection (cubic: ε^L = ε^T) → the proper ε₂ (no external factor).
Result: ε₂^{PA} = (8π²α/Ωω²)⟨⟨Σ(n+½±½)|ê·(S1+S2)|²δ⟩⟩.
- EPW: 2π·(e²/ε₀ → 4πα) = 8π²α.
- Noffsinger: ε₂ = αn_rc/ω = 8π²e²/(ω²V).
Both match D1 C1 **in full text**. This closes the SOTA amendment "C1 prefactor from memory".

**Discrepancies:**
- (i) Both sources sum j over the Wannier manifold only. Completeness, the [V_NL,r] term and the [g,r] term (D1 6.1, REF) are omitted.
  This is small at q = 0 and fatal at keV q.
- (ii) The iη (EPW) and iΓ (Noffsinger) in the denominators double count the first-order line outside the window (D1 §5.2).
  EPW says the needed theory "is under development". The URF answer is the window theorem + Hadamard finite part + the X1 soft-bremsstrahlung structure.
- (iii) Noffsinger writes the matrix elements bra–ket transposed. The sign is irrelevant in |·|².

**Leading correction:**
- the pair channel at (Q, ω∓ω_Q) (WP0 5.6f; X2 δ_pair ≈ −(10–50)% [E]);
- excitons (Elliott, positive).

EPW's Si result underestimates experiment by ≤50% (their text). This is consistent with a net exciton-dominated correction [C].

**L9b sources [FT].**
- 1608.01994: Eq. (2) ⟨n_eσv⟩ = −ImΠ/ω; Eq. (3) Π ≈ −iσ̂ω; Eq. (6) κ²_eff = κ²m⁴/[(m²−ReΠ)²+(ImΠ)²]; Eq. (7) R = ρ⁻¹(ρ_DM/m)κ²_effσ₁;
  Eq. (10) ALP R ≃ ρ⁻¹(ρ_DM/m)(3m_a²g²/(4m_e²e²))σ₁.
- 2106.12586: Eqs. (20)–(22) (mixing), (35) σ₁ = ωImε, (38)–(39).
- 1412.8378: Eq. (18) Γ_{T,L} = −κ²_{T,L}ImΠ_{T,L}/ω.

**Chain:** WP0 (3.5)–(3.6) at k ≈ m v → 0. Dark photon: Γ = κ²m Im(−1/ε) ≡ κ²_effσ₁ [C10]. Then σ₁ = σ₁^{X0} + σ₁^{X+} + σ₁^G.
**URF content [D]:**
- (a) For E_g^{ren} + ω_ν < m < E_dir^{ren}, σ₁ = σ₁^{X+} = mε₂^{PA}(m) of L9 entirely.
- (b) **Temperature transfer.** Data at T_d used at detector temperature T must be mapped term by term:
  σ₁^{X+}(ω;T) = Σ_ν[(n_ν(T)+1)A_ν(ω−ω_ν; T) + n_ν(T)A_ν(ω+ω_ν; T)], with E_g(T) shifted by AHC.
  1608.01994 uses 300 K and 77 K data. At mK the absorption branch vanishes and E_g rises by ≈ 50 meV. So the data-driven Si rate is
  overestimated near the edge [E: O(1) for m within ~0.1 eV of the edge].
- (c) **ALP.** The vertex is Tr J_e (WP0 2.5), an unscreened spin current. At SOC = 0 the spin sum of the PA amplitude equals the
  velocity form, so Eq. (10) holds for the X+ part with the proper σ₁^{PA}. With SOC it fails at O(SOC) [D].
- (d) **Scalar, new.** The LO n_e PA amplitude vanishes at k → 0 (charge conservation; D2 §2a q = 0 cancellation), so it is O(k).
  The NLO τ_e operator has no cancellation, since [τ_e,H] ≠ 0:
  Γ^{PA}_φ = (g²/2m_φ) S^{PA}_{ττ}(0,m_φ), where S^{PA}_ττ is D1 (2) with ρ_mn → (τ_e)_mn and no screening (2106.12586's finding for
  the zero-phonon part extends to X+) [D].

## 5. Finite-T and zero-point renormalisation (L12)
**Sources [FT].**
- AHC, 1603.06965: Eq. (157) Σ^FM_{nn′k}(ω) = (1/ħ)Σ_{mν}∫dq/Ω_BZ g*g[(1−f)/(ω−ε/ħ−ω_qν+iη) + f/(…+ω_qν−iη)];
  Eq. (158) the finite-T replacement with n_qν; Eq. (160) Σ^DW = Σ_ν∫g^DW_{nn′νν}(k,q,−q);
  Eqs. (195)–(198) the rigid-ion DW Σ^DW = −Σ′∫g^{2,DW}/(ε_nk−ε_mk)(2n+1).
- Williams–Lax/ZG, 1604.02394: Eq. (1) ε₂(ω;T) = Z⁻¹Σe^{−E_n/kT}⟨ε₂(ω;x)⟩_n; Eq. (3) the Gaussian integral with σ²_{ν,T} = (2n+1)l_ν²
  (Eq. (4)); Eq. (5) the ZG displacement Δτ = (M_p/M_κ)^{1/2}Σ(−1)^{ν−1}e σ; Eq. (6) the O(σ²) expansion; Eq. (24) the adiabatic HBB
  (2n+1)δ(ε_c−ε_v−ħω), "the Dirac delta function does not contain the phonon energy".
- EPW 2302.08085 Eqs. (67)–(68); ZG theory 1912.10929 [ABS].

**Chain [D]:** WP0 (3.1) → X0 ⊕ X+ at n_g = 2 → adiabatic amplitudes (ω_Q/δ → 0) → **phonon energy dropped from the δ**. In the joint form:

  S^{WL}(q,ω;T) = ∫dω_ph S^{ad}_{X0+X+}(q; ω_ph, ω)  (electronic label at the full ω),  = ⟨S^{clamped}(q,ω;x)⟩_{x∼𝒩(0,σ_T)}.           (W.11)

Expanding to O(σ²) gives AHC in X0 (adiabatic Fan + DW, which is Eq. (6) → (20)) plus adiabatic HBB in X+ (Eq. (24)).
ZG is a *deterministic* one-configuration quadrature of (W.11): exact to O(σ⁴) as N → ∞ by antithetic sign pairing (Eqs. (7)–(8)).
It is not a stochastic evaluation (WP0 defect 6). The Monte Carlo WL of their Ref. 17 is the stochastic one.

**Validity:** harmonic, adiabatic (ω_Q ≪ δ), T arbitrary, N → ∞ supercell. Linear-coupling Franck–Condon structure is exact to the
second moment [C6b–c]; the third moment fails [C6d].

**Leading correction [D]:**

  S^{URF} − S^{WL} = Σ_{sb} |M|² [(n+1)δ(ω−Δ−ω_Q) + nδ(ω−Δ+ω_Q) − (2n+1)δ(ω−Δ)] + O(ω_Q/δ)|M|²,   ΔM₁ = +Σω_Q|M|² (T-independent) [C6a].   (W.12)

- At T = 0 the WL/ZG sideband onset sits at E_g^{ren} instead of E_g^{ren} + ω_ν. That is 18 (TA) to 58 (TO) meV in Si.
- For the 0.34–0.47 MeV window (ω_max ≈ 1.4 eV at 0.4 MeV), the kinematic edge makes this an O(1) rate error at the lowest masses [E].
- Further corrections:
  - non-adiabatic (dynamical) AHC: Fan at ε ± ω_Q. Small in Si [E]; the adiabatic AHC is ill-defined for polar Fröhlich coupling (1603.06965 §VIII [ABS-level]);
  - O(σ⁴) and supercell size;
  - for DM at q ≠ 0, the supercell S must be unfolded at unreduced q (X2 Route S). RPA-LFE in the supercell basis then also contains the pair channel.

**Practical hybrid (closes the PAER/ZPR double count) [D]:**
S = S^{ZG}(q,ω;T) + [S^{X+,PAER} − S^{X+,ad}_{(2n+1)}], where the bracket is computed with EPW on the same g.
The other option is AHC-renormalised X0 + PAER X+. **Never ZG + PAER.**

## 6. Crystal NR bremsstrahlung (catalog-processes §12 item 4)
**Atomic source [FT].** 1607.01789 Eq. (8): d²σ/dωdE_R = (4ω³E_Rm_e²|α(ω)|²/(3πm_Nα))dσ/dE_R = (4α/(3πω))(E_R/m_N)|f(ω)|²dσ/dE_R,
with α(ω) = −(α/(m_eω²))f(ω) (Gaussian units). 1905.00046 [ABS]: Migdal dominates bremsstrahlung in atoms.

**URF derivation [D].**
- Hypotheses: ω_γ ≫ ω_ph; photon wavelength ≫ a; ε_T(ω_γ) real.
- Setup: the transverse-photon-improper part of WP0 (3.6) in S_κκ. The photon couples to the lattice dipole, H_γL = −Σ_I eZ*_κ(ω)u_I·E.
  Z*_κ(ω) is the **dynamical Born charge**: the macroscopic polarisation per displacement of one nucleus at frequency ω, with the other
  nuclei clamped and electrons non-adiabatic.
- The same double-commutator expansion as 2210.06490 (3.3) gives the amplitude ∝ eZ*·(q/M)·ê/ω_γ, independent of the lattice potential. Then

  d³Γ/(dω_γ dω_ph d³q) ∝ 𝔇_κκ S^G_κκ(q,ω_ph) × (2α/(3πω_γ)) n(ω_γ) |Z*_κ(ω_γ)·q|²/M_κ²   (isotropic: |Z*·q|² → Z*²q²).                  (W.13)

  This is the photon-labelled extension of the joint S: final state (lattice ω_ph; photon ω_γ; ω_e = 0).
- Checks:
  - vacuum (n = 1) atom: Z*_atom(ω) = −m_eω²α(ω)/e² ≡ f(ω), and v_N² = 2E_R/M, reproduce Eq. (8) [C8a,c];
  - Z*(∞) = Z [C8b].
- Small-ω expansion: Z*(ω) = Z*(0) + ω²C_κ + …, with C_κ = 2ReΣ_n d_{0n}(∂_uV)_{n0}/E_n³ (computable by DFPT).
- Above the gap n is complex. The photon is absorbed into e–h pairs. Assign by final state: photon-pole residue = bremsstrahlung; the
  continuum belongs to X (Migdal) at relative O(v²) (transverse vs Coulomb). No double count.

**Consequences [E].**
- **Si/Ge:** Z*(0) = 0 (ASR + equivalent sublattices), so the rate ∝ ω⁴C², comparable to the atomic estimate (|Z*| ≈ 0.05 at 1 eV).
  The free-atom Kouvaris–Pradler is not a crystal upper bound.
- **GaAs (Z* ≈ 2.1, n ≈ 3.6):** photons for ω < E_g, where Migdal is closed. P ≈ 2.6×10⁻¹³ over 0.1–1.4 eV at m_χ = 100 MeV.
  That is ~10³× the atomic estimate, and ~10⁻⁵ of the above-gap Migdal probability. It matters only as a sub-gap optical channel in polar scintillators [C relevance].

## 7. Exciton–phonon replicas (G5, exciton–phonon part)
**Formula [D].** Hypotheses: BSE excitons as bosons (low density), TDA, linear e–ph.
Final state: exciton S with centre-of-mass momentum P = q+Q, plus phonon ∓Q.

  M^{exc}_{S±}(q,Q) = Σ_{S′} 𝒢_{SS′ν}(q,Q) ρ_{S′0}(q)/(ω − Ω_{S′}(q)) + Σ_{S′} ρ_{SS′}(q) 𝒢_{S′0,ν}(Q)/(−Ω_{S′}(Q) ∓ ω_{Qν}),
  S^{X+,exc}_ee(q;ω_ph,ω_e) = (2π/V)Σ_{Sν±}(n+½±½)|M^{exc}_{S±}|² δ(ω_e − Ω_S(q+Q)) δ(ω_ph ∓ ω_{Qν}),                               (W.14)

where:
- ρ_{S′0}(q) = Σ_{vck}A^{S′*}_{vck}ρ̃_cv(k,q) is the exciton creation vertex, screened (WP0 7.2);
- 𝒢_{SS′ν} is Antonius–Louie 1705.04245 Eq. (49) [FT]: Σ A^{S*}A^{S′}g_cc′(k+Q,q) − Σ A^{S*}A^{S′}g_v′v(k,q);
- 𝒢_{S′0} = Σ A^{S′*}g_cv is creation of a pair by a phonon (path B / Z-graph partner);
- ρ_{SS′} is the exciton–exciton density vertex.

The second family is the excitonic image of D1 paths B–D. On shell, the unrestricted-sum theorem carries over when the S′ sums are
complete (it is the D1 algebra in the pair basis) [C: completeness of the BSE basis assumed].
Excitons replace free pairs, so (W.14) **replaces** (W.4c) near the edge and must not be added to it.

**Effective-mass (Wannier–Mott) limit [D].** |M_S|² = Ω|φ_S(0)|²|M_free(k_c,k_v)|² (Elliott). This gives:
- replicas at E_x(P_c) ± ω_ν;
- ∝ (ω − E_x ∓ ω_ν)^{1/2} per exciton band, instead of the free-pair (ω − E_g ∓ ω_ν)²;
- a Sommerfeld-enhanced continuum.

Si: E_x^b ≈ 14.7 meV; Ge ≈ 4 meV [E, memory]. The window onset moves down by E_x^b.

## 8. Gap closures and computation specifications
**G2 (frozen lattice / T = 0 / phonon-assisted edge).**
- Formula: S(q,ω;T) = S^{X0,ren}(q,ω;T) [AHC energies + D2 §2c] + S^{X+}(q,ω;T) [(W.4c) with M̃] in the window, or the hybrid of §5.
  Outside the window: X0⊕X+ inclusive with Hadamard finite part.
- Specification, Route P: QE (PBE + scissor/GW) + EPW; Wannier F_ij(R,q) tensor + plane-wave Sternheimer remainder (SOTA R2);
  ASR-enforced g with quadrupoles; coarse k 8³–12³, Q 6³, fine pocket grids ≡ 60³–120³; N_m converged to the Bethe ridge; σ ≪ δ₀;
  detuning-form denominators (X1 R1–R3); X2 Route S for δ_LF + δ_pair.
- Outputs: S(q,ω;T) and R(T)/R(0) per (N_eh, q) bin; joint F(ε_e,ε_h | q,ω) for WP5; nuisance Δ_k (WP0 8.1) for δ_pair, excitons, ZPR.
- Cost: as D1 §7, 10¹⁰–10¹¹ flop per material plus ZG supercells (4³–6³ cells, RPA-LFE) [E]. CPU.

**G6 (inconsistent Migdal; double counting).**
- Formula: (W.5) with sum rules J3/J4/J7 and rules N1–N3. A single code path covers all of L7a–d.
- Specification:
  - (i) S^ee_{GG′}(k,ω_e) all-electron RPA+LFE: GPAW, Yambo or BerkeleyGW, k up to 30 keV. Cores via Z_κ(k) or explicit core shells.
  - (ii) S^G_κκ(q,ω_ph) from phonopy DOS: incoherent recursion for q ≫ 1/a, coherent one-phonon below. Anharmonic optional (WP2).
  - (iii) The convolution (W.5), with the exact impulse bracket where |q·p|/Mω_e > 10⁻²; p-grid 50³ per q-shell.
  - (iv) Validate δM_κ (J3) by an independent DFPT sum, and P_Mig ≤ 10⁻³.
  - (v) Neutron-calibration prediction: the same (W.5) with neutron scattering lengths (for 2210.04917).
- Outputs: joint tables S^X(q;ω_ph,ω_e) for Si/Ge, the quenching-subtraction kernel, and a theory band from T2/LFE.
- Cost: dominated by (i), ≈ 10³ CPU-h [E].

**G5 (exciton–phonon part).**
- Formula: (W.14).
- Specification: BerkeleyGW/Yambo finite-momentum BSE at P ∈ pocket set (Si: P ≈ 0.85X); EPW g on the same gauge U(k); 𝒢 by
  1705.04245 Eq. (49); k-grid for exciton radius ~5 nm, ≈ (a_x/a)³ ~ 10³ points per pocket [E]; practical route: Wannier–Mott envelope × EPW M_free.
- Exact remaining gap: a converged finite-P BSE for Si/Ge on such grids has not been done. Cost ≈ 10⁴ CPU-h [E].

**Crystal NR bremsstrahlung.**
- Formula: (W.13).
- Specification: Z*_κ(ω) by frequency-dependent DFPT (Sternheimer at ±ω; QE/ABINIT); n(ω) from KK of ε₂; S^G from phonopy.
- Output: dR/dω_γ dω_ph.
- Cost: negligible beyond DFPT [E].

## 9. WP0 defects
1. **(4.9)** is incomplete. It equals X1 (X1) only at band extrema and omits the Galilean P_n terms [C1b–d]. Replace with X1 (X1).
   ℓ_Q convention: WP0 has N inside, D1/X1 outside.
2. **(5.7)** is X2 (2.2) restricted to G = G′ = 0, resonant pairs only, and an off-shell continuation of D1 (1). The truncation is not stated.
   (5.6c–d) is confirmed. Use X2 (2.2).
3. **§9.3 L7d "it is X0, not X+"** is partly wrong. 2205.03395 Eqs. (3.3)–(3.4) sum T_n with n ≥ 0: n = 0 is X0, n ≥ 1 is X+.
4. **Sector dictionary, S_eκ X+:** "dark photon only" should read "any 𝔇 with c_e c_κ ≠ 0".
   (J7) adds that the X-sector of S_eκ has a fixed negative ω_e-moment.
5. **6.2(ii)/L7a boost mass:** M vs Ibe's m_A (Eq. (73)). The O(Zm_e/M) difference is the drag mass of (J3).
6. **§9.3 L12 / LIMITS L12:** "ZG = stochastic evaluation" should read "deterministic one-shot quadrature of the Williams–Lax average"
   (1604.02394 Eqs. (5)–(8)).

## 10. Status
| Item | Tag |
|---|---|
| (W.1)–(W.2) joint S and marginal; sector decomposition | D (H1–H5; WP0 Theorem D) |
| (W.4)–(W.6) entries at τ_J | D (W.5 T1–T4 hypotheses) |
| J3 Migdal energy moment = drag mass; J7 mixed split | D (leading BO order); atom exact [C4, C5] |
| L7a–d as truncations of (W.5); KKL prefactor; 2603.13052 (4.7) discrepancy | D [C2, C3] |
| EFT expansion parameter |q·p|/Mω_e | D (free recoil), E (bound) |
| X1 algebra, C7 reconciliation; X2 ⊃ WP0 (5.7) | D [C1] |
| L9 prefactor in full text; L9b temperature transfer; τ_e PA scalar channel | D; size E |
| L12 (W.11)–(W.12); hybrid rule | D [C6]; Si impact E |
| Crystal bremsstrahlung (W.13) | D (hypotheses in §6); sizes E; relevance C |
| Exciton replicas (W.14) | D (BSE-boson); completeness C |
| G2, G6, G5-exc, bremsstrahlung specifications | E (costs) |

**Open, handed on:** O-WP3-1 X2-N2/N3 (pair channel) and the Umklapp re-check of the Si window; O-WP3-2 a finite-P BSE for Si (G5);
O-WP3-3 DFPT values of δM_κ and C_κ for Si, Ge, GaAs; O-WP3-4 proof of (H5)-free labels (WP0 O4); O-WP3-5 WP1 to confirm the ALP/SOC statement of L9b(c).

## 11. Literature (IDs verified against the arXiv API, 2026-10-31; FT = full text read)
FT: 1707.07258 (Ibe et al.); 2011.09496 (KKL); 2210.06490 (Berghaus et al.); 2603.13052 (Berghaus–Essig–McDuffie); 2505.08864 (Esposito–Rocchi);
2205.03395 (Liang et al.); 1202.3454 (Noffsinger et al.); 2302.08085 (EPW 2023); 1608.01994 (Hochberg–Lin–Zurek); 1412.8378 (An et al.);
2106.12586 (Mitridate et al.); 1604.02394 (Zacharias–Giustino); 1603.06965 (Giustino RMP); 1607.01789 (Kouvaris–Pradler); 1705.04245 (Antonius–Louie).
ABS / title: 1912.10929; 1905.00046; 2606.14845 (adiabatic Migdal); 2104.01811 (Migdal in quenching); 2210.04917 (Migdal measurement);
2310.05704; 2011.13352; 2105.00599 (halo conventions).

## 12. Symbols introduced/used (WP0 §10 governs; deviations flagged)
| Symbol | Meaning | Status |
|---|---|---|
| q, ω, n_e(q) = Σe^{+iq·r}, S_ab (WP0 3.1), R_ab, ρ_mn (O(1)), g (EPW), 𝔇_ab | as WP0 §10 / NOTATION | used as is |
| ω_e, ω_ph | electronic-label and lattice energy of the prompt final state (W.1) | **new** |
| S_ab(q;ω_ph,ω_e) | joint response (W.1); marginal = S_ab(q,ω) | **new** |
| Ê_e, Ê_L, U_ep | label-energy operators; e–ph Schrieffer–Wolff part of the decoupling | **new** (extends U_n) |
| G, X0, X+ | WP0 sectors; X0 ⇔ ω_ph = 0 at harmonic order | as WP0 |
| τ_J | truncation used for (W.4)–(W.6) | new instance of WP0 τ |
| M̃_± | screened PAER amplitude (X2 2.2) | as X2 |
| ℓ_Q | (2M_cellω_Q)^{−1/2}, **N outside** (D1/X1) | **deviation from WP0 (4.9)** (N inside) |
| D^n, Ξ^n = D^n + v_n⊗P_n, P_n | comoving and lab deformation tensors, band momentum (X1) | Ξ_n as WP0 §10, now defined as lab slope |
| 𝓕_κ(q) | adiabatic electron form factor riding with κ | **new** |
| U_κ(p) = Z_κ(p)e²/p², Z_κ(p) | ion potential, effective ion charge | new (KKL's Z_ion) |
| δM_κ | Born–Huang drag-mass tensor (J3) | **new** |
| W_e(q) | Migdal energy moment | **new**; not the Debye–Waller W |
| P_Mig(q) | total Migdal probability | new |
| W, e^{−2W} | Franck–Condon/Debye–Waller factor only | as directed |
| Z*_κ(ω), C_κ | dynamical Born charge; its ω² coefficient | new (Z* static as WP2) |
| n(ω) | refractive index | new; distinct from n_{Qν} (Bose) and n_e (density) — flagged |
| ω_γ | photon energy | new |
| S (exciton), Ω_S(P), A^S, 𝒢_{SS′ν} | BSE exciton, energy, envelope, exciton–phonon vertex (1705.04245) | new; **S as exciton label collides with S_ab** — use S only as a subscript |
| S1, S2 | HBB/EPW path amplitudes (sources) | source notation only |
| τ_e | kinetic-energy density (WP0 2.5) | as WP0 |
| v_N = q/M_κ | nuclear recoil velocity | new; v alone stays DM velocity |
| η(v_min)/(2q), halo per 2105.00599 | isotropic halo factor | as directed (not used beyond WP0) |
