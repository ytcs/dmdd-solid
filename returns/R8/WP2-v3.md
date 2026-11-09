# R8 / WP2-v3: lattice sector of the URF, corrected standalone version (R7 hostile review applied)

Revision agent, brief R8/REV3-WP2. Supersedes returns/R6/WP2-v2.md (v2) and returns/R5/WP2.md (v1), which stay as the historical record.
Applies every verdict of referees/R7/REF-WP2-A.md (items A-1…A-30) and REF-WP2-B.md (items B-1…B-24), and the cross-package notes of
state/SOTA.md "R7 referee reports" that touch WP2 quantities (REF-WP0-A on WP0-v2 (4.7); REF-WP5-A on the Migdal subtraction).
Conventions: CONVENTIONS.md; symbols: NOTATION v4. WP0 equations are cited from returns/R6/WP0-v2.md as "WP0-v2 (x.y)".
Checks: `code/WP2-v3/checks.py` (sympy only, exact arithmetic for every identity, no numerical simulation; 31 checks, all PASS, ≈ 35 s);
cited as WP2v3-Cn (C1–C13 are v2's, C9/C11d re-described; new: C3d, C4b, C6c, C9b, C9c, C11e–g, C12b, C14).
Tags: **[D]** derived (hypotheses stated), **[D, sketch]**, **[E]** estimated, **[C]** conjectured. Literature: **[FT]** full text,
**[ABS]** abstract; every literature claim now carries its R7 status, **CONFIRMED** (by at least one referee against the full text),
**UNRESOLVED** (no referee read the source), and REFUTED claims are dropped (§13). Labels from other returns carry their prefix (CONVENTIONS §14).
Status: R×2 COMPLETE (SOTA R7); this is the corrected version. **Equation numbers are v1's/v2's** (WP0-v2 and SOTA cite WP2 (2.2), (2.3)–(2.4),
(3.6), (4.2), (4.4), (5.2)); (2.4) keeps its number but its content is corrected; new objects are double-primed: (3.4″), (5.2″).
**R9 clean-up (in place):** optional wording items of referees/R8/VER-WP2-A.md and VER-WP2-B.md (both: all items RESOLVED, no new error) and the
returns/R8/AUDIT-2.md rows addressed to WP2 are applied; record in §16c. Checks re-run: 31/31 PASS.

---
## 0. Results in one page, and what changed

1. **Reduction [D]:** the lattice sector is the GS sector of WP0-v2 Theorem D (6.1), with n_e → ρ̄_e(q;R) (§1).
2. **Exact harmonic S at all phonon orders, coherent, finite T [D]** (2.2), in the CONVENTIONS §5 phase convention; exact shell expansion
   (2.3) whose (ΔR, κ, κ′) = (0, κ, κ) terms are the incoherent approximation. **BZ-average theorem (2.4), corrected (v3):** for a Bravais
   lattice the BZ-averaged coherent S is the incoherent S; with a basis every inter-sublattice pair (ΔR, κ ≠ κ′) survives with weight
   j_BZ(ΔR + r_κ − r_κ′), and the statement is asymptotic in q ≫ max(n_ph, 2W_κ)q_BZ. "Incoherent = BZ-averaged coherent" is therefore
   **false for Si, Ge, GaAs** as an identity (nearest-neighbour pairs are inter-sublattice, j_BZ ≈ 0.44 each [E]).
3. **2607.24933 Eq. (47) (3D) [FT, CONFIRMED]:** the isotropic weight 1/3 per branch is incorrect for the coherent term at fixed phonon momentum
   (the exact weight is |q̂·e|²), even under the paper's stated "monoatomic, isotropic" assumption; Eq. (47) is not used in their numerics [FT, per REF-A and REF-B: their numerics use the 1D model] (§3.3).
4. **Truncating at n_ph ≤ N loses P[Pois(2W_κ) ≥ N] of the (signed) f-sum (3.4′), at any T and for the coherent S** (multiplicative vertices);
   with several sites the loss is the |c_κ|²/M_κ-weighted mean (3.4″). The exact compound-Poisson equation (3.5) gives S at all orders (a forward
   march at T = 0, the FFT of e^{Φ(t)} at T > 0), with the final-state phonon spectrum ρ^ph_κ for WP5 (3.6).
5. **L4 [D]:** WP0-v2 (5.4) with the total ε ≡ the Born-charge one-phonon formula with Z*/ε_∞ and LO eigenvectors (Sherman–Morrison (4.2));
   reproduces 1910.08092 Eq. (106) and 1807.10291 Eqs. (29)–(32). 1712.06598 Eq. (5) carries a spurious 1/V_cell.
6. **L6 [D]:** exact anharmonic cumulants (5.1); the mean recoil is exact. 𝔨₃ splits into GS (BO curvature) + X (Migdal) (5.2); 𝔨₃^{GS}
   must be computed directly as a GS cumulant, never as 𝔨₃ − 𝔨₃^X. **(5.2′)** for point nuclei on cubic sites 𝔨₃ = (q²/2M_κ²)Z_κe²𝓃_e(R_κ)/3
   **at all q** (exact). **(5.2″) (v3):** the κκ ↔ eκ relation −(m_e/M_κ)𝓜³_eκ = (self κκ potential moment) is **not** exact: −(m_e/M_κ)𝓜³_eκ(q)
   ∝ 𝓃_e(R_κ) + Δ𝓃_κ(q), with Δ𝓃_κ → 2𝓃_e as q → 0⁺ (relative 1.2×10⁻⁴ in Si) and Δ𝓃_κ/𝓃_e(R_κ) ≈ (q a_{1s,κ})²/10 from the core
   (Si: 9% at 51 keV, 29% at 102 keV). It holds for the contact (trace) term at every q. The free limit gives hep-ph/0608035 Eq. (5).
7. **L18/G13 [D]:** three exact linear constraints on the anharmonic increment (6.1); with WP6's M-type nuisance they hold only at θ ∈ {0,1}
   (6.1′). Structure at O(η_anh²) (6.2); negligible in the impulse regime, O((λ^anh)²(ω̄/E_R)^{1/2}).
8. **Nuclear spin [D]:** unpolarised spins give an exactly incoherent channel (7.1) (dropped by PhonoDark 2009.13534 [FT, CONFIRMED]);
   identifying its lattice factor with the average-lattice self term neglects isotope mass disorder, O(ΔM/M) ≈ 3.5% for ²⁹Si [E].
   Polarisation adds a coherent term ∝ P_κ². Transverse nuclear currents excite TA/TO (7.2).
9. **L19/G11 [D]:** harmonic rate formula (8.1). **Cubic isotropy theorem:** the harmonic incoherent S has no anisotropy in Si/Ge/GaAs at any
   n_ph or T (8.2), which explains the negligible Si/GaAs modulation of 2411.03433 [FT, CONFIRMED].
10. **WP0 defects** WP2-D1–D4, WP2-C1 (§11): all applied in WP0-v2 (its closing table #8, #10, #32). v3: the "incoherent accurate below q_BZ"
    half of WP2-D1 is downgraded to [E] (IF-10); WP0-v2 (4.7) at q → 0⁺ acquires the 2𝓃_e term (IF-1).

**v2 → v3 changes (R7).** (2.4) corrected for a basis and given its hypothesis q ≫ max(n_ph, 2W_κ)q_BZ, with C9 re-described and C9b, C9c
added; the shell-size estimate becomes a range ≈ 2–10% (q = 10–2 keV) with shells indexed by (ΔR, κ, κ′); the T > 0 shell sum is "absolutely
divergent, defined as a lattice Fourier sum"; 2607.24933 Eq. (47) charge limited to the polarisation weights; the 2205.02250 "discrepancy" is
dropped (REFUTED); 2411.03433's q̂ = ẑ IA width is a declared approximation; 1712.06598 Eq. (12) is a declared rough estimate; the κκ/eκ
contact relation is qualified and quantified (5.2″), including the 2𝓃_e term; the e^{−W_κ} bookkeeping of the non-rigid vertex is stated (O(2W));
species-weighted truncation loss (3.4″) and signed-moment qualifier; (3.5) route at T > 0; (6.1) normalisation; (7.1) isotope and n_ph ≥ 1
qualifiers; GS f-sum with the Migdal prescription of WP5 (R7); literature statuses (§13). Closing table §16. v1 → v2 changes: returns/R6/WP2-v2.md §0.

---
## 1. The lattice sector from the master formula

**(1.1) Operators [D].** Spin-independent couplings are O_c(q) = Σ_s c_s n_s(q) = Σ_κ c_κ n_κ(q) + c_e n_e(q) (WP0-v2 (5.3), coupling vector c_s).
Nucleon: c_κ = [c₁^{(p)}Z_κ + c₁^{(n)}(A_κ − Z_κ)]F^M_κ(q), c_e = 0. Dark photon (total charge): c_κ = Z_κ, c_e = z_e = −1, i.e. O_z of
WP0-v2 (5.4). Electron-only: c_κ = 0, c_e = 1. Spin couplings use the nuclear rows I_κ^β, J_κ^{αβ} of WP0-v2 (2.2).

**(1.2) GS-sector reduction [D]** (hypotheses H1–H4 of WP0-v2 §6.2). By Theorem D (ii), in GS (O′_κ)_{GS,GS} = F^M_κ e^{iq·R_I} acts on nuclear
coordinates and (O′_e)_{GS,GS} = ⟨Φ₀(R)|n_e(q)|Φ₀(R)⟩ ≡ ρ̄_e(q;R) (R in the argument = the configuration {R_I}), up to O(κ_BO⁴). Hence

  S^{GS}_{cc}(q,ω) = (2π/V) Σ_{i,f∈GS} p_i |⟨f| Σ_I c_κ e^{iq·R_I} + c_e ρ̄_e(q;R) |i⟩|² δ(ω − E_f + E_i),                              (1.1)

a purely vibrational problem on the BO surface E^ad_0(R). Expanding ρ̄_e about equilibrium sites x⁰_{Rκ} = R + r_κ gives the **charge vertex**

  ρ̄_e(q;R) = ρ̄_e(q;R⁰) + i Σ_I e^{iq·x⁰_I} δρ_κ(q)·u_I + O(u²),   𝒵_κ(q) ≡ Z_κq − δρ_κ(q) → q·Z*_κ (q → 0),                              (1.2)

so the linear total-charge coupling to u_I is i𝒵_κ(q)·u_I e^{iq·x⁰_I} (proper, without the macroscopic field); the electron density alone has
linear vertex iδρ_κ·u_I → i q·(Z_κ𝟙 − Z*_κ)·u_I. Limits:
- rigid ion: δρ_κ = q f^at_κ(q), exact to all orders in u (ρ̄_e = Σ_I f^at_κ e^{iq·R_I}), 𝒵_κ = q[Z_κ − f^at_κ]; at q ≫ q_BZ these are the
  effective charges of 2205.02250 §IV.3 (Fig. 9);
- q → 0: 𝒵_κ → q·Z*_κ, the Born charge; (1.2) reproduces 1910.08092 Eqs. (98)–(104) **at O(u) and q → 0 only** (B-1) [those equations
  UNRESOLVED as quotes, §13];
- leading correction to the rigid ion: the valence deformation δρ_κ − q f^at_κ, computable by DFPT (§10).

**Meaning of δρ_κ (v3, B-1).** In (1.2) δρ_κ is the response of the **whole** electron density (core + valence): it equals q f^at_κ in the rigid-ion
limit. Its valence part is δρ^val_κ ≡ δρ_κ − q f^core_κ (§10). This follows NOTATION v4 row "f^core_κ, δρ^val_κ … valence part of δρ_κ"; the
row "δρ_κ(q) … valence charge-response vector" contradicts it and should read "electronic charge-response vector (core + valence)" (IF-11).

**Debye–Waller bookkeeping of the vertex [D] (v3, B-1; WP2v3-C14).** (1.2) is additive and anchored at x⁰_I. For a harmonic Gaussian state the
one-phonon matrix element of the nuclear (and of any rigidly moving) part is ⟨1|e^{iq·u}|0⟩ = i q·⟨1|u|0⟩ e^{−W_κ}, whereas the linear
deformation term gives ⟨1|δρ_κ·u|0⟩ with **no** e^{−W_κ}. Attaching e^{−W_κ} to the whole 𝒵_κ in (2.2) (the convention of this return, and of
1910.08092's multiplicative Y_j) is therefore exact for the rigid ion and for the nucleon vertex, and differs from the additive (1.2) by a
relative O(2W_κ) in S for the valence-deformation part; the multiplicative form also generates an extra contraction term (1910.08092 Eq. (91),
third term of Y_j), O(q³). At q ≪ q_BZ, 2W ≈ 6×10⁻⁴ (Si, 1 keV), so L4 is unaffected.

**(1.3) Conventions in the literature (factor to WP0-v2 (3.1)) [FT].**

| Source | Definition of S | Factor to WP0-v2 S |
|---|---|---|
| 2205.02250 Eq. (4); 2411.03433 Eq. (1); 2309.10839 Eq. (2); 2607.24933 Eq. (4); 1910.08092 Eq. (90) | (2π/V)Σ\|⟨f\|Σc e^{iq·r}\|0⟩\|²δ | 1 (T = 0) |
| 1911.03482 Eq. (2) | (1/N)Σ\|…\|²δ | ×2π/Ω |
| 1712.06598 Eq. (10) | neutron convention; rate via (4π/V_cell) in Eq. (9) | ×2π/Ω |
| 2506.11191 Eq. (69) | (1/N)Σλ²C, C lacking 1/V (their footnote 6) | ×1/Ω (C has the 2π) |

All sources are at T = 0; WP0-v2 (3.1) is Gibbs-averaged and the T > 0 forms below carry Bose factors. Sources using the eigenvector phase
e^{iQ·x⁰} (1910.08092 Eq. (90): e^{iG·x⁰_j}) map to CONVENTIONS §5 by e_κν(Q) → e_κν(Q)e^{−iQ·r_κ} (WP2v3-C13).

---
## 2. Harmonic S_κκ′ at all phonon orders (coherent, finite T)

**Exact form [D].** Hypotheses: H3 at n_A = 0 (harmonic BO surface), Gibbs state, operator (1.1) with the vertex of (1.2) absorbed into c_κ
(exact for the rigid ion and the nucleon vertex; for the full 𝒵_κ at one-phonon order up to the relative O(2W_κ) of the DW bookkeeping, §1.2). With u_{Rκ} = Σ_{Qν}(2NM_κω_{Qν})^{-1/2}e_{κν}(Q)e^{iQ·R}B_{Qν} (CONVENTIONS §5)
and Bloch's identity (exact for Gaussian states), S = V^{-1}∫dt e^{iωt}⟨O_c†(t)O_c(0)⟩ gives

  S(q,ω) = (1/V)∫dt e^{iωt} Σ_{Rκ,R′κ′} c_κ* c_κ′ e^{−iq·(x⁰_{Rκ}−x⁰_{R′κ′})} e^{−W_κ−W_κ′} exp Φ_{κκ′}(ΔR,t),   ΔR = R − R′,                     (2.1)

  Φ_{κκ′}(ΔR,t) = Σ_{Qν} [(n_{Qν}+1)(q·e_{κν}(Q))(q·e_{κ′ν}(Q))* e^{iQ·ΔR − iω_{Qν}t} + n_{Qν}(q·e_{κν}(Q))*(q·e_{κ′ν}(Q)) e^{−iQ·ΔR + iω_{Qν}t}]/(2Nω_{Qν}√(M_κM_κ′)),

with 2W_κ(q) = q·B_κ·q, B_κ = ⟨u_κu_κ⟩ = Σ_{Qν}e_{κν}e_{κν}†(2n_{Qν}+1)/(2NM_κω_{Qν}). Expanding exp Φ gives the **n_ph-phonon coherent term**

  S^{(n_ph)}(q,ω) = (2π/Ω)(1/n_ph!) Σ_{{ν_i,s^ph_i}} ∫Π_i[Ω d³Q_i/(2π)³ · (n_{Q_iν_i} + (1+s^ph_i)/2)/(2ω_{Q_iν_i})] δ(ω − Σ_i s^ph_iω_{Q_iν_i})
             × (2π)³/Ω Σ_G δ³(q − Σ_i s^ph_iQ_i − G) |Σ_κ c_κ e^{−W_κ} e^{iq·r_κ} M_κ^{−n_ph/2} Π_i (q·e^{s^ph_i}_{κν_i}(Q_i))|²,   e^{+} ≡ e*, e^{−} ≡ e.   (2.2)

s^ph_i = +1 (−1): emission (absorption) of phonon (Q_i, ν_i); emission carries e* and n + 1 (CONVENTIONS §5). **Phase convention (explicit):**
eigenvectors e_{κν}(Q) carry the cell phase e^{iQ·R} only (CONVENTIONS §5), so the one-phonon (and every n_ph) intra-cell factor is e^{iq·r_κ}
with q unreduced, as in WP4-v2 (v1's e^{iG·r_κ} belongs to the x⁰-phase eigenvectors; same |…|², WP2v3-C13). Checks: n_ph = 1, T = 0 reproduces the
one-phonon form with π/Ω = (2π/Ω)/2 on the line tagged (91) in the 1910.08092 HTML, together with Y_j (v2 cited "(90)", which is the definition
of S; citation corrected per REF-B §H, [FT, CONFIRMED]); and 1911.03482 Eq. (8) (×2π/Ω, without DW); n_ph = 2, T = 0, G = 0, long-wavelength
isotropic limit gives the "contact" term 1911.03482 Eqs. (12), (16) (both 1911.03482 agreements **UNRESOLVED**: no referee read the source);
n_ph = 0 is the Bragg term ∝ δ(ω)Σ_Gδ³(q − G), of zero measure for DM.

**Shell expansion [D].** Group (2.1) by lattice separation ΔR and basis pair (κ,κ′):

  S = S_inc + ΔS_coh,   S_inc = (1/Ω)Σ_κ|c_κ|²e^{−2W_κ}∫dt e^{iωt}[e^{Φ_{κκ}(0,t)} − 1],
  ΔS_coh = (1/Ω)Σ_{(ΔR,κ,κ′)≠(0,κ,κ)} c_κ*c_κ′ e^{−iq·(ΔR+r_κ−r_κ′)} e^{−W_κ−W_κ′}∫dt e^{iωt}[e^{Φ_{κκ′}(ΔR,t)} − 1].                               (2.3)

At order n_ph each shell term is ∝ Φ_{κκ′}(ΔR,t)^{n_ph}; by Cauchy–Schwarz |Φ_{κκ′}(ΔR,t)| ≤ [Φ_{κκ}(0,0)Φ_{κ′κ′}(0,0)]^{1/2}.
- n_ph = 1: the ΔR sum must be done in full (it produces the dispersion δ); no truncation in ΔR is allowed.
- n_ph ≥ 2 at T = 0: absolutely convergent (acoustic Φ(ΔR) ~ ΔR^{-2}, Φ² ~ ΔR^{-4}).
- T > 0 (v3, A-3): the classical acoustic correlation Φ ~ T/ΔR gives Σ_ΔR|Φ|² ~ ∫R²dR/R², **absolutely (linearly) divergent**; the n_ph = 2
  shell sum exists only as a lattice Fourier sum, i.e. as a distribution in q through the phase e^{−iq·ΔR_{κκ′}}, finite away from q = G
  (quasi-elastic absorption of a thermal phonon); irrelevant at mK (t_ph ≈ 10⁻³), flagged (§12 gap 3).
Shells are labelled by the pair (ΔR, κ, κ′), with pair separation **ΔR_{κκ′} ≡ ΔR + r_κ − r_κ′** (v3, B-3): in diamond the nearest pair
(|ΔR_{κκ′}| = 2.35 Å, z = 4) has κ ≠ κ′ and is not indexed by a lattice vector. The **shell parameter** z_{ΔR_{κκ′}}|j₀(q|ΔR_{κκ′}|)|c̄^{n_ph}_{ΔR_{κκ′}}
(rate-level size, §3.3) is the coherence control that replaces x_coh (WP0-v2 Table 6.1).

**BZ-average theorem [D] (corrected in v3: A-4, B-4; WP2v3-C9, C9b, C9c).** With j_BZ(r) ≡ (Ω/(2π)³)∫_BZ d³p e^{−ip·r} (real and even,
the BZ being inversion-symmetric), hold the smooth factors of (2.3) (Φ_{κκ′} ∝ q_αq_β and W_κ) at q. The only remaining p-dependence of a shell
term under q → q + p is e^{−ip·ΔR_{κκ′}}, whose BZ average is j_BZ(ΔR_{κκ′}). Hence, for every n_ph,

  (Ω/(2π)³)∫_BZ d³p S^{(n_ph)}(q+p,ω) = S^{(n_ph)}_inc(q,ω) + Σ_{ΔR} Σ_{κ≠κ′} j_BZ(ΔR + r_κ − r_κ′) S^{(n_ph)}_{κκ′,ΔR}(q,ω) + (gradient terms).   (2.4)

- κ = κ′: ΔR_{κκ} = ΔR is a lattice vector and j_BZ(ΔR) = δ_{ΔR,0}: only the self term survives. This is the whole content for a **Bravais
  lattice**, where "incoherent = BZ-averaged coherent S" is exact up to gradient terms.
- κ ≠ κ′: ΔR + r_κ − r_κ′ is never a lattice vector, so **every** ΔR contributes, and Σ_ΔR j_BZ(ΔR + r_κ − r_κ′) = 1 (Poisson summation;
  only G = 0 lies inside the BZ). 1D diatomic chain, r₂ − r₁ = a/2: j_BZ(na + a/2) = (−1)ⁿ/(π(n + ½)), i.e. 2/π for both nearest neighbours,
  −2/(3π) for the next pair, … (C9b, exact; C9b also shows that v2's "ΔR = 0 only" form fails). Diamond: the four nearest neighbours of a site
  are on the other sublattice and related by T_d operations that leave the fcc BZ invariant, so all four carry the same j_BZ ≈ 0.44
  (equal-volume spherical BZ, [E], C10). v2's (2.4) kept one of the four.
- **Gradient terms.** The held factors vary across the BZ by relative 2n_ph p/q (from Φ^{n_ph} ∝ q^{2n_ph}) and 4W_κ p/q (from e^{−2W_κ}).
  For the self term the linear order averages to zero (inversion-symmetric BZ), leaving O((n_ph q_BZ/q)²) (1D: n(2n−1)q_BZ²/(12q²) for |q+p|^{2n},
  C9c); the cross terms keep a linear piece ∝ ∫_BZ p e^{−ip·ΔR_{κκ′}} ≠ 0 (C9c), O(max(n_ph, 2W_κ)q_BZ/q). (2.4) is therefore an **asymptotic
  statement for q ≫ max(n_ph, 2W_κ) q_BZ**; at q ≲ n_ph q_BZ the gradient terms are O(1).

**Consequences.** (i) The incoherent approximation is the BZ average of the coherent S only for Bravais lattices and q ≫ n_ph q_BZ. (ii) For Si,
Ge, GaAs the inter-sublattice pairs give a BZ-averaged correction of size up to ≈ Σ_pairs j_BZ(ΔR_{κκ′}) c̄^{n_ph}_{ΔR_{κκ′}}, ≈ 4 × 0.44 × 0.3² ≈ 0.16
at n_ph = 2 with c̄ ≈ 0.3 [E], falling as c̄^{n_ph}. This counts the **nearest pairs only**: since Σ_ΔR j_BZ = 1 while the four nearest pairs already
sum to 4 × 0.444 = 1.77, the farther pairs carry net weight ≈ −0.77 (opposite sign) with smaller but nonzero c̄^{n_ph}, so they partly cancel; 0.16
is an upper-type indicator, and the e^{−iq·ΔR_{κκ′}} phases can only reduce it further (R9, VER-B R1, VER-A; WP2v3-C10); it is of the same order as the §3.3 shell estimate and not negligible a priori. (iii) The
v2 claim "incoherent is accurate in ω-integrated rates below q_BZ" (WP2-D1, as quoted in WP0-v2 Table 6.1) has no derivation behind it: it is
**[E]** (IF-10). WP2v2-C9 = WP2v3-C9 (monatomic chain, q-independent weights) tests only j_BZ(ΔR) = δ_{ΔR,0}; v2's "verifies the identity exactly"
overstated it.

---
## 3. Multiphonon: incoherent approximation, Poisson tail, Franck–Condon

**(3.1)–(3.2) Incoherent harmonic S at finite T [D].** From (2.3), with the projected DOS D_κ^{q̂}(ω) = N^{-1}Σ_{Qν}|q̂·e_{κν}(Q)|²δ(ω − ω_{Qν})
(2411.03433 Eq. (18)), define the one-phonon measure

  w_κ(q;ω′) = (q²/2M_κ) D_κ^{q̂}(|ω′|)/ω′ · [n_B(ω′) + 1]   (ω′ < 0: absorption, weight n_B(|ω′|)/|ω′| ≥ 0 since n_B(−x) + 1 = −n_B(x)),   ∫dω′ w_κ = 2W_κ.   (3.1)

  S_inc(q,ω) = (2π/Ω) Σ_κ |c_κ|² e^{−2W_κ(q)} Σ_{n_ph≥1} w_κ^{*n_ph}(q;ω)/n_ph!   (* = convolution in ω).                                (3.2)

At T = 0 with isotropic D^{q̂} = D_κ this is 2205.02250 Eq. (36) and 2411.03433 Eq. (12); with the full D^{q̂} it is 2411.03433 Eq. (24)
[FT, CONFIRMED quotes, REF-B]. For an Einstein solid at T = 0, (3.2) is the Poisson law of 2011.09477 Eq. (10), |f(n,q)|² = (q/q₀)^{2n}e^{−q²/q₀²}/n!,
q₀² = 2Mω₀ (source notation) [UNRESOLVED as a quote: not re-read by a referee].

**Franck–Condon (CONVENTIONS §10).** "DW" means only the e^{−2W} weight of the zero-phonon (Bragg) term, locally the overlap
|⟨0|e^{iq·u}|0⟩|² = e^{−2W}; the lattice Huang–Rhys factor is S_HR = 2W_κ. Replacing w_κ by the Huang–Rhys spectral function of the e–ph coupling
change gives the same compound-Poisson ZPL line shape in WP3 (pointer only; the AH tadpole is not DW).

**(3.3) Coherent–incoherent crossover and 2607.24933 [FT, D] (v3: A-5, B-5, B-3).** For the 1D monatomic chain, 2607.24933 Eq. (44) states that
coherent and incoherent S^{(n)} differ only by the momentum δ; (2.2) confirms it. Their 3D generalisation, Eq. (47) (PDF Eq. (4.23)), inserts the
isotropic weight 𝒟(ω,k) = (Ω_c/3(2π)³)Σ_αδ(ω−ω_{αk}) (their Eq. (46)) into the coherent sum together with momentum conservation. **This is
incorrect for the coherent term at fixed phonon momentum** [FT, CONFIRMED by both referees]: expanding (2.2) for one species gives the per-phonon
weight (Ω/(2π)³)Σ_α|q̂·e_α(Q_i)|²δ(ω_i − ω_{αQ_i}), not (1/3)Σ_α. Example: n_ph = 1, G = 0, q ≪ q_BZ: momentum conservation sets Q = q, so the
exact result is LA with weight |q̂·e_L|² = 1 and no TA, whereas Eq. (47) gives weight 1/3 on each of LA, TA, TA. A plane wave at fixed Q is
purely L or T **even in an elastically isotropic medium**, so the paper's caveat directly below Eq. (4.23), "we have still assumed a monoatomic,
isotropic lattice for simplicity", does not rescue the formula. The same paper's 1D Eq. (48) (LA weight 1) agrees with (2.2). Scope: the intra-cell
phases of a polyatomic basis lie outside Eq. (47)'s stated monoatomic scope; (2.2) **extends** the result to a basis and is **not** a correction of
Eq. (47) on that point (v2's charge withdrawn). [FT, per REF-A and REF-B] Their §5 uses only 1D results (the 1D N-site model) as proxies, so Eq. (47) does not enter their rates.
The physical conclusion "incoherent is accurate for n_ph ≥ 2 in ω-integrated rates" is, after the correction of (2.4), **[E]** for crystals with a
basis and for q ≲ n_ph q_BZ. Pointwise the correction is O(1) at the edges of the n_ph-phonon bands, where only near-Γ modes contribute and
coherence forces q ≈ G (their Figs. 8–10).

**Shell size [E] (v3, B-3; WP2v3-C10).** Rate-level size after angular averaging and ω-bins wider than ω_max:
|ΔS_coh/S_inc|_{n_ph} ≈ Σ_pairs z_{ΔR_{κκ′}}|j₀(q|ΔR_{κκ′}|)|c̄^{n_ph}_{ΔR_{κκ′}}, c̄_{ΔR_{κκ′}} = ⟨u_{0κ}·u_{ΔRκ′}⟩/⟨u²⟩. Si, nearest pair (κ ≠ κ′,
|ΔR_{κκ′}| = 2.35 Å, z = 4), c̄ ≈ 0.2–0.4; at n_ph = 2, c̄ = 0.3: **1.8% at q = 10 keV** (q|ΔR_{κκ′}| = 11.9, close to a node of j₀) and
**10% at q = 2 keV** (q|ΔR_{κκ′}| = 2.38, j₀ = 0.29). Quote the envelope 4c̄²/(q|ΔR_{κκ′}|) (3.0% at 10 keV, 15% at 2 keV) or the range ≈ 2–10% for q = 10–2 keV, not a single "≈ 2%".
At q = 2 keV < q_BZ the incoherent baseline itself is outside the validity of (2.4), so this is a size indicator only.

**(3.4) Sum rules (consistency with WP0-v2 (4.6)) [D].**
- Zeroth moment: ∫(dω/2π)S_self = 𝓃_κ|c_κ|².
- First moment: ∫ω′w_κ dω′ = (q²/2M_κ)∫D_κ^{q̂}[(n_B+1) − n_B] = q²/2M_κ at any T, so the **f-sum WP0-v2 (4.6b) holds exactly** in the harmonic
  BO model. Since ∫ω w^{*n} = n(∫ωw)(∫w)^{n−1} (WP2v3-C3b, with absorption lines and detailed balance),

  ∫ω S^{(n_ph)}_inc / ∫ω S = e^{−2W_κ}(2W_κ)^{n_ph−1}/(n_ph−1)!,   so truncation at n_ph ≤ N misses P[Pois(2W_κ) ≥ N] of the f-sum,        (3.4′)

  **at any T** (2W_κ then includes coth(βω/2)). The coherent shell terms do not change it: ∂_tΦ_{κκ′}(ΔR,0) = −i(q²/2M_κ)δ_{κκ′}δ_{ΔR,0} by the
  completeness Σ_νe_{κν}e_{κ′ν}† = δ_{κκ′}𝟙 (after e(−Q) = e(Q)*, n_{−Q} = n_Q), so every ΔR ≠ 0 or κ ≠ κ′ term has zero first moment at each
  n_ph. Qualifiers (v3, A-7, B-7): (i) at T > 0 the fractions refer to the **signed** first moment over ω ∈ ℝ (absorption lines enter with ω < 0;
  each order's share e^{−2W}(2W)^{n−1}/(n−1)! is nevertheless ≥ 0); (ii) the coherent statement holds for exactly multiplicative vertices (rigid
  ion, nucleon); for the full charge vertex 𝒵_κ only at n_ph = 1 (§1.2); (iii) with several sites (WP2v3-C3d):

  lost f-sum fraction = Σ_κ (|c_κ|²/M_κ) P[Pois(2W_κ) ≥ N] / Σ_κ (|c_κ|²/M_κ)   (sum over basis sites; per species weight 𝓃_κ|c_κ|²/M_κ),        (3.4″)

  which matters in GaAs, where 2W_Ga ≠ 2W_As.
- One-phonon **without** e^{−2W} saturates the f-sum exactly, coherent and with Umklapp (Placzek's rule, completeness). "One-phonon with e^{−2W}"
  (1910.08092 Eq. (94)) carries only e^{−2W} of it; the multiphonons supply the rest.
- Cross-species and inter-site first moments vanish (WP0-v2 (4.6c)): intra-cell interference changes no f-sum.
- **GS vs X (WP0-v2 §6.2 (iii); WP3 J3):** the X states carry the electronic excitation plus the nuclear recoil, so at leading BO order the X
  first moment is Σ_n|a^{Mig}_n|²(ΔE_n + q²/2M_κ) = E^{Mig}_1 + P_Mig q²/2M_κ (E^{Mig}_1 = q·δM_κ·q/(2M_κ²), P_Mig = Σ_n|a^{Mig}_n|², a^{Mig}_n the
  Migdal amplitudes of (5.2), ΔE_n = E^ad_n − E^ad_0).
  The exact f-sum q²/2M_κ then leaves the GS sector with (1 − P_Mig)q²/2M_κ − E^{Mig}_1 = (1 − P_Mig)q²/2(M_κ + δM_κ) to first order (WP2v3-C6c;
  isotropic δM shown). This is the prescription of REF-WP5-A (R7, SOTA): **GS = (1 − P_Mig)·S^{GS} built with mass M_κ + δM_κ** (v2 kept only the
  E^{Mig}_1 term). A harmonic S^{GS} with bare M_κ and unit weight overcounts (δM/M ≤ 2.7×10⁻⁴ Si [E, WP3]); never add Migdal on top without
  that correction (WP0-v2 double-counting rule (a); IF-2).
- **Nuisance type:** a phonon-order cut is a non-conserving, support-removing truncation, so the f-sum is informative for it (WP0-v2 (8.2)); since
  (3.5) removes the cut at negligible cost, no nuisance is needed. If a cut is kept, the WP6 type is A with Δ^τ fixed by (3.4′).

**(3.5) Compound-Poisson integral equation [D]** (from ∂_te^Φ = Φ̇e^Φ; WP2v3-C4, C4b):

  ω S_κ(q,ω) = ∫dω′ ω′ w_κ(q;ω′) S_κ(q, ω−ω′),   S_κ ≡ e^{−2W_κ}Σ_{n_ph≥0} w_κ^{*n_ph}/n_ph!,                                                  (3.5)

at any T (C4b: the two-sided identity holds term by term with absorption lines). **Numerical route (v3, B-8, B-23).** At T = 0, w_κ is supported on
ω′ ∈ (0, ω_max], so (3.5) is a forward march from the seed e^{−2W_κ}δ(ω): cost O(N_ω²) per (q, q̂). At T > 0, w_κ has ω′ < 0 support, the bin
equation at ω involves S at ω − ω′ > ω, and the equation is degenerate at ω = 0 (where it does not fix the δ(ω) weight): it is **not** a forward
recursion. In the time domain it is ∂_tŜ = Φ̇Ŝ, whose solution is unique up to normalisation, Ŝ = e^{−2W_κ}e^{Φ_κκ(0,t)}; the T > 0 route is the
**FFT of e^{−2W_κ}[e^{Φ_κκ(0,t)} − 1]** (the Bragg δ removed analytically, a small Gaussian or Lorentzian regulator for the quasi-elastic region),
cost O(N_ω log N_ω) (IF-12). Either route supersedes the n ≤ 10–20 truncations of 2205.02250 and 2411.03433; 2411.03433 Eq. (26) is the order-by-order version.

**(3.6) Final-state phonon spectrum (WP5 hand-over, WP0-v2 (7.3)) [D].** Mean number of created phonons per dω′ at given (q,ω):

  ρ^ph_κ(ω′|q,ω) = w_κ(q;ω′) S_κ(q,ω−ω′)/S_κ(q,ω),   ∫ω′ρ^ph_κ dω′ = ω (by (3.5)),   ∫ρ^ph_κ dω′ = ⟨n_ph⟩,                                     (3.6)

ω′ < 0 entries are absorbed thermal phonons; ⟨n_ph⟩ counts emitted **and** absorbed phonons (B-8); the created number is ∫_{ω′>0}ρ^ph_κ. Replacing w_κ by the branch-projected w_{κν} gives the branch content (LA/TA/LO/TO) needed for WP5
down-conversion. In the incoherent approximation the phonon momenta are uniform over the BZ, weighted by the DOS.

---
## 4. Polar couplings: dark photon, Born charges, ε_∞, LO–TO (L4)

**(4.1) Start [D].** WP0-v2 (5.4): S_zz(q,ω) = (2q²/e²)Im[−(ε^{-1})_{00}(q,ω)]/(1 − e^{−βω}) with the **total** ε; exact for total-charge coupling.

**(4.2) Adiabatic, harmonic, q → 0 [D]** (GS; ω ≪ E_g so the electronic ε is ε_∞; n_A = 0; q ≪ q_BZ). The total longitudinal ε is

  ε(q̂,ω) = ε_∞(q̂) + (e²/Ω) Σ_{ν′} [p(q̂)·e^A_{ν′}]²/(ω_{ν′}² − ω²),   ε_∞(q̂) ≡ q̂·ε_∞·q̂,   p(q̂)_{κα} ≡ (q̂·Z*_κ)_α/√M_κ,

ν′ running over the analytic (TO) eigenmodes e^A_{ν′} of D^dyn_A. Sherman–Morrison with D^dyn_NA = D^dyn_A + (e²/Ωε_∞(q̂))ppᵀ, whose eigenmodes ν
are the LO-split phonons, gives exactly (WP2v3-C2, exact rational 3-mode model)

  −1/ε = −1/ε_∞(q̂) + (e²/Ωε_∞(q̂)²) pᵀ(D^dyn_NA − ω²)^{-1}p  ⇒  S_zz = (2π/Ω) Σ_ν (1/2ω_{Qν}) |Σ_κ q·Z*_κ·e*_{κν}/(ε_∞(q̂)√M_κ)|² δ(ω − ω_{Qν}).  (4.2)

The ELF with the total ε is *identical* to the Born-charge one-phonon formula with vertex q·Z*/ε_∞ and NA eigenvectors: the "screen by ε_∞,
ions in the source" prescription of 1910.08092 (below Eq. (104)) equals WP0-v2's total-ε prescription; they are bookkeepings of one Dyson series.
With F_DM = (αm_e/q)², 𝒱 = e_χe²/q² and WP0-v2 (3.3) this reproduces 1910.08092 Eq. (106) and 1807.10291 Eq. (29) [FT, quotes CONFIRMED by
REF-B]. Hypotheses (both referees): macroscopic (rank-1) ε only, real Γ-point eigenvectors, q ≪ q_BZ, ω ≪ E_g.

**(4.3) One polar branch [D]** (WP2v3-C1). With ε = ε_∞(ω_L² − ω²)/(ω_T² − ω²) and LST:

  Im[−1/ε] = (πω_L/2)(1/ε_∞ − 1/ε₀)δ(ω − ω_L)  ⇒  Γ_χ = ∫d³q/(2π)³ 2πδ(ω_q − ω_L) · e_χ²e²ω_L(1/ε_∞ − 1/ε₀)/(2q²),                    (4.3)

i.e. |ℳ|² of 1807.10291 Eq. (32) with e′ = e_χe, and σ̄_e of 1712.06598 Eq. (8).

**(4.4) Electron-only and nucleon couplings in polar crystals [D].** In GS the electron-only vertex is ρ̄_e, linear part i q·(Z_κ𝟙 − Z*_κ)·u_I:
the f_e term of 1910.08092 Eq. (104). The nucleon vertex is c_κ = A_κF^M_κ with **no** Z*/ε_∞ factor; LO–TO splitting enters only through the NA
eigenvectors, i.e. through R̃_{Nc}ε^{-1}v_CR̃_{cN} of WP0-v2 (5.3) (WP2-C1, applied in WP0-v2 (5.3) nucleon bullet).

**(4.5) Si and Ge [D].** Z*_κ = 0 by symmetry (the two sites are related by inversion and Σ_κZ*_κ = 0). The leading dark-photon one-phonon
vertex is quadrupolar, 𝒵_{κα}(q) = −(i/2)q_βq_γ𝒬_{κ,βγα} + O(q³), so S_zz^{(1)} ∝ q⁴. A second contribution is the two-phonon term of the
second-order dipole ∂Z*/∂u. Agrees with SOTA #5 (zero ionic ε part in Si).

---
## 5. Impulse limit and free nuclear recoil (L6)

**(5.1) Exact cumulants of the self structure factor [D]** (WP2v3-C5). Hypotheses: self part of S_κκ; any H whose potential V_pot (all Coulomb
potential energy, H_C minus kinetic terms) is local in the struck coordinate (WP0-v2 (L)); any anharmonicity; any T; TR (odd momentum moments
vanish). With ∂_q̂ ≡ q̂·∇_{R_I} and E^kin_q̂ ≡ ⟨(q̂·P_I)²⟩/2M_κ, the ω-cumulants of S_self/∫S_self are

  𝔨₁ = q²/2M_κ,  𝔨₂ = 2q²E^kin_q̂/M_κ,  𝔨₃ = (q²/2M_κ²)⟨∂_q̂²V_pot⟩,  𝔨₄ = (q²/M_κ²)⟨(∂_q̂V_pot)²⟩ + (q⁴/M_κ⁴)(⟨(q̂·P_I)⁴⟩ − 3⟨(q̂·P_I)²⟩²).   (5.1)

Derivation as 2309.10839 Eqs. (56)–(60), with ⟨p[H,p]⟩ = ½⟨∂²V⟩ from stationarity. WP2v3-C5 certifies k = 1–4 exactly for a cubic + quartic
oscillator with exact ground state e^{−W(x)} (the moment differences integrate to zero by an explicit polynomial Q, Q′ − 2W′Q = difference).
Harmonic case: (5.1) reproduces the cumulants of (3.2), ∫ω′^m w_κ dω′: 𝔨₂ = (q²/2M)∫D ω coth(βω/2)dω, 𝔨₃ = (q²/2M)∫Dω²dω, … **𝔨₁ is exact: the mean of
the impulse peak is never shifted.** Clarification (v3, A-14, B-20): 2205.02250 (below Eq. (38)) writes "the true peak is shifted slightly from
the result (38)"; a peak is the mode, which does shift (by ≈ −𝔨₃/2𝔨₂ at leading Edgeworth order). The source is correct; v2's listing of this as a
discrepancy is **withdrawn** (REFUTED by both referees).

**(5.2) The GS/X split of 𝔨₃ [D at leading BO order, H2; Migdal amplitude of WP0-v2 §6.2 (ii)]** (WP2v3-C6). V_pot contains V_eN, and the
second-derivative identity ∂_q̂²E^ad_0 = ⟨Φ₀|∂_q̂²V_pot|Φ₀⟩ − 2Σ_n|⟨Φ_n|∂_q̂V_pot|Φ₀⟩|²/(E^ad_n − E^ad_0), with the Migdal amplitude
(q/M_κ)⟨Φ_n|∂_q̂V_pot|Φ₀⟩/(E^ad_n − E^ad_0)², gives

  𝔨₃ = 𝔨₃^{GS} + 𝔨₃^X,   𝔨₃^{GS} = (q²/2M_κ²)⟨∂_q̂²E^ad_0⟩_vib,   𝔨₃^X = (q²/M_κ²)Σ_n|⟨Φ_n|∂_q̂V_pot|Φ₀⟩|²/(E^ad_n − E^ad_0) = ω³-moment of S^X_κκ.      (5.2)

The same amplitudes give the X first moment (q²/M_κ²)Σ_n|…|²/(E^ad_n − E^ad_0)³ = q·δM_κ·q/(2M_κ²) = E^{Mig}_1, which is WP3 J3 (WP2v3-C6b).
Corrections: O(κ_BO⁴) and O(𝔨₁/ΔE₃) from measuring ω about 𝔨₁ instead of 0, ΔE₃ the ω³-weighted mean excitation energy. Consequences: the lattice
impulse approximation must use the **BO curvature**, not ⟨∇²V_pot⟩; the ω³ moment of S_κκ is dominated by X despite its O(κ_BO⁴) weight.
**Computing 𝔨₃^{GS} (v3, B-12 remark):** since 𝔨₃^X/𝔨₃^{GS} ≈ 8×10⁵ [E], the listed O(κ_BO⁴) and O(𝔨₁/ΔE₃) corrections, relative to 𝔨₃, exceed
𝔨₃^{GS} itself (e.g. 3E_R/ΔE₃ × 8×10⁵ ≈ 10³ at E_R = 1 eV). 𝔨₃^{GS} is usable only when defined and computed **directly** as a GS-sector cumulant
(BO curvature ⟨∂_q̂²E^ad_0⟩_vib, e.g. from PIMD), **never** as 𝔨₃ − 𝔨₃^X. Status: [D] at leading BO order, OPEN on WP3's side (B-12).

**(5.2′) Contact sum rule and the F4 comparison [D for point nuclei; cubic sites for the closed form] (new).** Write V_pot = V_ee + V_eN + V_NN,
V_eN = −Σ_{i,I}U_κ(r_i − R_I), U_κ(r) = Z_κe²/(4π|r|) for a point nucleus. (a) ∇²_R V_NN = 0 at a nuclear site (other nuclei are elsewhere) and
∇²_R(−U_κ) = +Z_κe²δ³(r_i − R_I) (WP2v3-C11b); (b) on a cubic site any rank-2 site tensor is ∝ 𝟙 (WP2v3-C11c), so ⟨∂_q̂²V_pot⟩ = ⟨∇²_RV_pot⟩/3
(the traceless part of ∂_α∂_β(1/r) averages to zero). Hence

  𝔨₃ = (q²/2M_κ²) Z_κe²𝓃_e(R_κ)/3,   𝔨₃^X = (q²/2M_κ²)[Z_κe²𝓃_e(R_κ)/3 − ⟨∂_q̂²E^ad_0⟩_vib],                                               (5.2′)

with 𝓃_e(R_κ) the electron contact density (WP0-v2 (4.7) notation). The first relation holds **at all q** (the self phases e^{∓iq·R_I} cancel in
the double commutator; both referees). Precision on (b) (v3): the rank-2 tensor ⟨∂_α∂_β V_pot⟩ at a site is absolutely defined only for the
neutral combination V_eN + V_NN (the electron-only field gradient of an infinite crystal is conditionally convergent, shape-dependent); for that
combination the traceless part vanishes on a cubic site and ∇²_R V_NN = 0, so (5.2′) holds. Its potential moment is the **self** part of 𝓜³_κκ:
𝓜³_κκ|^{self}_pot = 2𝓃_κ𝔨₃ = 𝓃_κq²Z_κe²𝓃_e(R_κ)/(3M_κ²) (normalisation with inversion, REF-B §F). The inter-site (I ≠ J) V_NN terms of 𝓜³_κκ
are distinct-part quantities and do not enter 𝔨₃.

**(5.2″) Link to WP0-v2 (4.7): the κκ/eκ relation at finite q [D] (v3, A-17, B-14, A-29; WP2v3-C11e–g, C10).** Newton's third law,
(q·∇_R)²U_κ(r − R) = (q·∇_r)²U_κ(r − R) (C11a), and the explicit double commutators (C11d: the e–N one is the multiplicative operator
e^{iq·(R−r)}(q·∇)²U_κ/(m_eM_κ), confirming (4.7); the κκ one has Hermitian potential part −(q·∇)²U_κ/M_κ²) show that the eκ moment is the κκ
self moment **with the phase e^{−iq·ρ}, ρ = r − R, inserted** and with electrons only. Split (q̂·∇)²(1/4πρ) = −(1/3)δ³(ρ) + PV 2P₂(q̂·ρ̂)/(4πρ³). The
trace (contact) part sits at ρ = 0, where the phase is 1: it is identical in both moments **at every q**. The traceless part averages to zero in
the κκ moment (cubic site, neutral combination) but, in the eκ moment, couples to the ℓ = 2 component of the phase, −5j₂(qρ)P₂ (Rayleigh, C11e).
Hence, for point nuclei on cubic sites,

  −(m_e/M_κ)𝓜³_eκ(q) = 𝓃_κq²Z_κe²[𝓃_e(R_κ) + Δ𝓃_κ(q)]/(3M_κ²),   Δ𝓃_κ(q) ≡ −(3/4π) PV∫d³ρ 𝓃_e(R_κ+ρ) e^{−iq·ρ} [3(q̂·ρ̂)² − 1]/ρ³,      (5.2″)

whereas 𝓜³_κκ|^{self}_pot = 𝓃_κq²Z_κe²𝓃_e(R_κ)/(3M_κ²) (5.2′). Evaluation:
- **Uniform part (q → 0⁺).** For the G = 0 component 𝓃_e of the density, Δ𝓃 = 6𝓃_e∫₀^∞j₂(y)dy/y = 2𝓃_e (C11e), independent of q: a
  non-analytic q → 0⁺ limit (at q = 0 exactly the electron-only integral is shape-dependent). The G ≠ 0 components give, at q → 0, a traceless
  rank-2 tensor summed over each T_d star, which vanishes; at finite q they leave anisotropic terms O(q/G_min) allowed by T_d (∝ q̂_xq̂_yq̂_z),
  weighted by valence Fourier components, ≲ 10⁻⁴ relative [D, sketch / E]. So −(m_e/M_κ)𝓜³_eκ(0⁺) ∝ 𝓃_e(R_κ) + 2𝓃_e, which is the form found by
  REF-WP0-A for (4.7) (SOTA R7); relative size 2𝓃_e/𝓃_e(R_κ) = 1.2×10⁻⁴ in Si (hydrogenic 1s² contact density, C10) (IF-1).
- **Core part (finite q).** For a spherical shell density, Δ𝓃 = 6∫₀^∞𝓃(ρ)j₂(qρ)dρ/ρ. With ∫₀^∞e^{−y/ξ}(cos μy − 1)dy/y = −½ln(1 + ξ²μ²) (C11f) and
  j₂ = −½∫P₂(μ)cos(yμ)dμ, a hydrogenic 1s² core, 𝓃 ∝ e^{−2ρ/a_{1s,κ}}, gives the closed form (C11g)

    𝔯_κ(q) ≡ [𝓃_e(R_κ) + Δ𝓃^{1s}_κ(q)]/𝓃_e(R_κ) = 3 + 3/ξ_κ² − 3(1 + ξ_κ²)arctan(ξ_κ)/ξ_κ³,   ξ_κ ≡ q a_{1s,κ}/2,   𝔯_κ = 1 + (q a_{1s,κ})²/10 + O(q⁴),

  which reproduces REF-B's quadrature table exactly (𝔯 = 1.035, 1.091, 1.288, 1.674 at ξ = 0.3, 0.5, 1, 2). Si (Z_eff ≈ 13.7,
  1/a_{1s} = 51.1 keV): **𝔯 − 1 = 0.4% at 10 keV, 3.3% at 30 keV, 9.0% at 51 keV, 28.7% at 102 keV** (C10). The L shell roughly doubles the O(q²)
  coefficient [E] (its 8 electrons at ≈ 4× the radius), so the hydrogenic numbers are a lower bound on the deviation.

**Corrected statement.** 𝓜³_κκ|^{self}_pot = −(m_e/M_κ)𝓜³_eκ holds **for the contact (trace) term at every q**, and for the full moments only up to
relative O(𝓃_e/𝓃_e(R_κ)) ≈ 10⁻⁴ plus O((q a_{1s,κ})²) (Si: q ≪ 50 keV). In the multiphonon and impulse window (q ≈ 10–300 keV) the κκ and eκ
third moments are **not** related by −m_e/M_κ; the κκ closed form (5.2′) still holds there. v2's "exactly" and "at contact" are withdrawn. With
this qualifier WP2 agrees with WP0-v2 (4.7) (q → 0, qa ≪ 1) and, per WP0-v2's record, with WP3-v2 J8 (q → 0); without it, it would not. WP2v3-C11d
sets the phase to 1 by hand and so tests only the trace part; the finite-q content is C11e–g. So WP2 (5.2), WP0-v2 (4.7) and WP3 J3 are mutually
consistent at q → 0 (F4 at the level of moments). Size [E] (C10): Si, hydrogenic 1s contact density only, 𝔨₃^X/𝔨₃^{GS} ≈ 8×10⁵; ΔE₃ is of the order
of the 1s binding (≈ 1.8 keV), so the O(𝔨₁/ΔE₃) correction to the GS/X split is negligible for q ≪ √(2M_κΔE₃) ≈ 10 MeV. **Consequence for WP3:**
the X ω³ moment is UV (core, large-k) dominated; a valence-only or soft-limit (W.5) truncation (WP3 T3) cannot saturate (5.2′), so the test is
meaningful only for the all-electron, all-k (W.5), and only against (5.2″) at the q where it is done (Interface flag IF-1).

**(5.3) Chain to the free recoil [D].**
1. The IA is the saddle at t ≈ 0 (2205.02250 Eqs. (37)–(39)); to leading order in 1/q

     S_IA(q,ω) = (2π/Ω) Σ_κ |c_κ|² ∫d³p 𝔫_κ(p) δ(ω − q²/2M_κ − q·p/M_κ),                                                                  (5.3)

   with 𝔫_κ(p) the (anharmonic, T-dependent) nuclear momentum distribution. A Gaussian 𝔫_κ gives 2205.02250 Eq. (39) with width
   σ_ω² = 𝔨₂ = 4E_R E^kin_q̂ (source Δ_d → σ_ω), E_R = q²/2M_κ.
2. σ_ω/E_R ≈ (ω̄/E_R)^{1/2} → 0 gives S^FR = (2π/Ω)Σ_κ|c_κ|²δ(ω − q²/2M_κ) (2205.02250 Eq. (42)).
3. In WP0-v2 (3.4), with hypothesis (I) (S angle-averaged; 𝒢 → η(v_min)/(2q), WP0-v2 (9.1)) and |𝒱_p|² = πσ_p/μ_p², this gives
   dℛ/dE_R = ρ_χσ_N|F^M_κ(q)|²η(v_min)/(2m_χμ_N²), v_min = q/2μ_N: hep-ph/0608035 Eq. (5) (WP2v3-C8; per unit target mass, ρ_T = 𝓃_NM_N)
   [quote UNRESOLVED: not re-read by a referee; the derivation itself was checked, A-18].
4. The Helm |F|² of hep-ph/0608035 Eq. (9) parametrises |F^M_κ|² (WP0-v2 (2.2)) under F_mass = F_charge (their Eqs. (7)–(8)), a 10–20%
   nuclear-structure systematic (their abstract) [UNRESOLVED].

---
## 6. Anharmonic expansion (L18, G13)

**(6.1) Exact constraints [D].** Let Δ^τ_A ≡ S_self^{(n_A=1)} − S_self^{harm} at fixed q (self part; the WP6 increment Δ^τ_k for k = n_A). From (5.1)
and the normalisation:

  ∫dω Δ^τ_A = 0,   ∫dω ω Δ^τ_A = 0,   ∫dω (ω − q²/2M_κ)² Δ^τ_A = (2π/Ω)|c_κ|² · 2q²δE^kin_q̂/M_κ,                                         (6.1)

δE^kin_q̂ the anharmonic change of the kinetic energy, a static quantity that PIMD gives exactly. The factor (2π/Ω)|c_κ|² = 2π𝓃_κ|c_κ|² is the
normalisation ∫dω S_self (per κ site; with n_κ^{cell} equivalent κ sites per cell, 𝓃_κ = n_κ^{cell}/Ω, i.e. sum (6.1) over the sites; R9, VER-A) (v3, A-19; v2 omitted it; WP2v3-C12b); equivalently, drop it if Δ^τ_A is defined from the normalised S_self/∫S_self. The middle identity is the WP6-W3 vacuity of the
f-sum for a conserving truncation (WP0-v2 (8.2)); the first and third are the informative constraints on θ_A.

**(6.1′) Compatibility with WP6 nuisance types [D] (new).** (6.1) is linear in Δ^τ_A. With the additive type A (S^τ + a^A_{n_A}Δ^τ_A) it holds for all
a^A_{n_A}. With the M type S^τ(1 + r^M_A)^{θ_A} it holds only at θ_A ∈ {0, 1}: a two-bin example with ∫Δ = 0 gives ∫S(θ) = (1 + a)^θ + (1 − a)^θ < 2 at
θ = ½ (WP2v3-C12). Recommendation (R9, superseding v2/v3's "M type with recorded violation, or type A"; AUDIT-2 L18, IF6-14): impose (6.1) on the computed Δ^τ_A
(validation) and use WP6-v3's **exponentially tilted type T (5.1″)**, which is PSD by construction and keeps the linear moment constraints (6.1)
exact for all θ, with WP6's n_κ ≡ (2π/Ω)|c_κ|² = the (6.1) normalisation; the affine form (type L in WP6-v3) is only its linearisation. The M-type
result above (C12) stays as the reason M is not used here (Interface flag IF-4).

**(6.2) Structure at O(η_anh²) [D in structure].** Cumulant expansion of ⟨e^{−iq·u(t)}e^{iq·u}⟩ beyond Gaussian, with 𝒞_m ∝ q^m, 𝒞₃ ∝ Φ^{(3)},
𝒞₄ ∝ Φ^{(4)} + (Φ^{(3)})².
- (a) **One-phonon:** δ(ω − ω_{Qν}) → A^ph_ν(Q,ω) = −2Im[2ω_{Qν}/(ω² − ω_{Qν}² − 2ω_{Qν}Π^ph_ν(Q,ω))], Π^ph_ν the bubble ((Φ^{(3)})²) plus loop
  (Φ^{(4)}) self-energy. The off-shell tail of A^ph_LA is exactly the "anharmonic two-phonon" term of 1911.03482 Eqs. (13), (17), including their
  iΓ/2 propagators.
- (b) **Interference** of the one-phonon amplitude (via one cubic vertex) with the two-phonon contact term: Fano-asymmetric line shapes,
  vanishing at leading order in the long-wavelength limit (real eigenvectors; 1911.03482 below Eq. (14)).
- (c) The anharmonic B_κ (i.e. 2W_κ) and E^kin_q̂.
- (d) n_ph-phonon terms with fewer DM vertices: for q ≫ q_BZ the power counting is (λ^anh)^{2k}x_R^{n−k} against x_R^n (2309.10839 Eq. (39)), so
  anharmonicity dominates the n_ph-phonon term for x_R ≲ (λ^anh)², i.e. only where S_harm is suppressed (high ω at small q).
- Impulse regime: anharmonicity enters only through 𝔨₂, 𝔨₃, 𝔨₄. Edgeworth parameter γ₁ = 𝔨₃/𝔨₂^{3/2} ~ (ω̄/E_R)^{1/2}, anharmonic parts
  O((λ^anh)²), so the correction is O((λ^anh)²(ω̄/E_R)^{1/2}): this derives 2309.10839's "negligible above ~10 MeV".

**(6.3) The 2309.10839 toy model, audited [D].**
- Matching: ω₀ = 1/⟨ω^{-1}⟩ plus the Gaussian smearing of their Eqs. (16)–(17) reproduces 𝔨₁, 𝔨₂ exactly (xω₀² + xσ² = q²ω̄/2M). It gives the
  harmonic 𝔨₃ = (q²/2M)(ω₀² + 3σ²) = (q²/2M)(3ω₀ω̄ − 2ω₀²) (σ² = ω₀ω̄ − ω₀², their Eq. (17)) instead of (q²/2M)⟨ω²⟩: **7% low** in Si [E]
  (ω̄ ≈ 40, ω₀ ≈ 28, √⟨ω²⟩ ≈ 44 meV; WP2v3-C10). The estimate ignores their Θ(ω_max) cutoff of the smearing (B-17).
- Missing physics: (i) the 3D angle-dependent single-site potential (their Eq. (23); the maximum-anharmonicity direction overestimates); (ii)
  intersite anharmonicity, i.e. the linewidths of (6.2a), which a single site cannot produce.
- **Normalisation discrepancy [FT, CONFIRMED by both referees; v1 of the paper]:** their Eq. (9) has e^{−W_d} with Eq. (10) W_d = (q²/4m_d)∫D/ω,
  i.e. W_d = W (half the FC exponent). This contradicts 2205.02250 Eq. (36) and their own Eq. (13), which have e^{−2W} with W^toy = q²/4m_dω₀ = W_d
  for D = δ(ω − ω₀); the physical value is |⟨0|e^{iqx}|0⟩|² = e^{−2W}. A typo at formula level; not checked whether it reached their numerics.

---
## 7. Nuclear-spin and nuclear-current couplings into phonons

**(7.1) Spin density [D].** Operator I_κ^β(q) = F^Σ_κh^I_κΣe^{iq·R_I}𝐈_I^β (WP0-v2 (2.2)). Hypotheses: (S1) spin–lattice couplings (hyperfine, nuclear
quadrupole) ≪ ω_ph (≲ μeV vs tens of meV); (S2) each spin-carrying isotope occupies sites at random with abundance x_κ (²⁹Si 4.7%, ⁷³Ge 7.8%),
occupancy o_{Rκ} ∈ {0,1}; (S3) spins uncorrelated between sites, polarisation P_κ along ẑ (paramagnet; order only at ≲ μK). Lattice and spin
traces factorise; the random coupling c_{Rκ} = F^Σ_κh^I_κ𝐈^β_{Rκ}o_{Rκ} makes the decomposition of 2205.02250 Eqs. (9)–(11) exact:

  S^{ββ}_{II}(q,ω) = S_coh[c̄_κ = x_κF^Σ_κh^I_κ⟨𝐈^β⟩] + (2π/Ω)Σ_κ x_κ(F^Σ_κh^I_κ)²[⟨(𝐈^β)²⟩ − x_κ⟨𝐈^β⟩²] S̃_self,κ(q,ω),   ⟨𝐈^z⟩ = P_κ𝒥_κ, ⟨𝐈^{x,y}⟩ = 0,   (7.1)

S̃_self the normalised self term of (3.2), convolved with the Larmor spectrum (ω_Lar/ω_ph ~ 10⁻⁶), **starting at n_ph ≥ 1** (v3, A-9e): the
n_ph = 0 part of the incoherent term is an elastic spin-incoherent δ(ω), of zero measure for DM.
- **Unpolarised (P_κ = 0):** incoherent, ⟨(𝐈^β)²⟩ = 𝒥_κ(𝒥_κ+1)/3; the one-phonon part scales as q²D^{q̂}(ω)/ω, no coherent LA δ, no q-linear
  enhancement at small q. The **incoherence** is exact under (S1)–(S3): ⟨𝐈^β⟩ = 0 kills every inter-site term whatever the lattice. **Isotope
  caveat (v3, B-18):** identifying the lattice factor with the average-lattice S̃_self of (3.2) neglects mass disorder: the spin-carrying isotope
  (²⁹Si, ⁷³Ge) is heavier than the host average, so its local DOS, B_κ and E^kin_q̂ differ by O(ΔM/M) (≈ 1/28 ≈ 3.5% for ²⁹Si) [E], and
  occupancy and phonons are not strictly independent; "exact" applies to the channel structure, not to this identification. The form agrees
  with 2506.11191 Eqs. (68)–(72), whose isotropic DOS is exact for cubic sites [UNRESOLVED as a quote: no referee read 2506.11191].
- 2009.13534 (text after its Eq. (31)) **drops** unordered-spin responses ("in the absence of ordering, the corresponding terms should be dropped")
  and so omits this nonzero channel [FT, CONFIRMED by both referees]: its 1/N argument holds per final state; the sum over the N phonon momenta
  restores a finite incoherent rate.
- **Polarised targets** (DNP, or B/T: P_κ ≈ μ_IB/T, ≈ 2% for ²⁹Si at 1 T and 10 mK [E]) switch on a coherent term ∝ P_κ² with the full one-phonon
  dispersion, and S_{nI} ∝ P_κ interference with the SI channel through 𝔇_{n,I} (WP0-v2 (2.3)).

**(7.2) Nuclear currents [D]** (rows j_κ, J_κ of WP0-v2 (2.2)). One-phonon matrix element ⟨Qν|j_κ^α(q)|0⟩ = −i(ω_{Qν}/2NM_κ)^{1/2}e*^α_{κν}(Q)
e^{−i(Q−q)·R}e^{iq·r_κ} + O(q·u). Hence: **longitudinal** S_{nj_L} = (ω/q)S_nn exactly (WP0-v2 (5.3), non-density bullet); **transverse**
S^{(1)}_{j_Tj_T}(q,ω) = (2π/Ω)Σ_ν(ω_{Qν}/2)|Σ_κ c_κe^{iq·r_κ}(ê_⊥·e*_{κν})/√M_κ|²δ(ω − ω_{Qν}), exciting TA/TO modes that density couplings
cannot reach at q ≪ q_BZ; relative to a density coupling suppressed by (ω/qv_χ)²-type DM-side factors, set by 𝔇 (on shell only P_Tv_χ and j_T
survive, WP0-v2 (2.2)).

---
## 8. Full q-vector anisotropy and daily modulation (L19 lattice part, G11)

**(8.1) Harmonic rate formula [D].** Hypotheses: 𝔇 depends on |q| only (true for 𝒪₁; velocity-dependent operators need the v-resolved form);
halo isotropic in the Galactic frame, boosted by v_E(t) (CONVENTIONS §8), so 𝒢(q,ω) = ∫d³v f_χδ(ω − ω_q) depends on q̂ only through
x = q̂·v̂_E. With S(q,ω) = Σ_{ℓm}S_ℓm(q,ω)Y_ℓm(q̂) in crystal axes, Funk–Hecke gives

  dℛ/dω(t) = (ρ_χ/m_χρ_T) Σ_{ℓm} Y_ℓm(v̂_E^{cr}(t)) ∫q²dq/(2π)³ 𝔇(q) S_ℓm(q,ω) · 2π∫_{−1}^{1}dx P_ℓ(x) 𝒢(q,ω;x),                                (8.1)

v̂_E^{cr}(t) the Earth-velocity direction in crystal axes (sidereal rotation; 2411.03433 Eq. (30)). Same structure as the harmonic method of
2607.06005 Eq. (10).

**(8.2) Selection rules [D]** (WP2v3-C7).
- S(q,ω) = S(−q,ω) (TR or inversion) ⇒ ℓ even. (P- and T-broken targets: nonreciprocal S; for density couplings the odd part is O(q³) (WP0-v3 (4.3)); odd ℓ allowed only as G_eff permits, the
  lowest being ℓ = 3 for G_eff ⊇ T or T_d, ℓ = 9 for O, and ℓ = 1 only for a polar G_eff (WP6-v3 (1.5)); R9, AUDIT-2 L19; L19 ✎ WP4-D6.)
- Cubic point groups have invariants only at ℓ = 0, 4, 6, 8, … (A₁ multiplicities of O: 1,0,0,0,1,0,1,0,1 for ℓ = 0…8).
- **Cubic isotropy theorem.** If every site has cubic site symmetry (T_d in Si, Ge, GaAs, diamond), every rank-2 site tensor is ∝ 𝟙:
  D_κ^{αβ}(ω) = δ_{αβ}D_κ(ω)/3, B_κ ∝ 𝟙. Then (3.1)–(3.2) depend on q̂ only through q̂·D_κ·q̂ = D_κ/3: **the harmonic incoherent S is exactly isotropic
  at every n_ph and T**, so its daily modulation vanishes identically. This explains why 2411.03433 finds negligible modulation in Si and GaAs (their n ≥ 2 framework, Eq. (24); the
  theorem predicts exactly zero there) and 1–10% in Al₂O₃, where the site tensors are anisotropic and ℓ = 2 is allowed (and 2W_κ = q·B_κ·q is direction-dependent).
- **Residual anisotropy in cubic crystals:** (i) the coherent one-phonon term (full anisotropy; dominates for m_χ ≲ few MeV); (ii) coherent shell
  terms of (2.3) at n_ph ≥ 2, including the κ ≠ κ′ pairs (ℓ ≥ 4, size from §3.3); (iii) in the IA, the rank-4 non-Gaussian ⟨(q̂·P)⁴⟩ − 3⟨(q̂·P)²⟩² of 𝔨₄ (5.1), O((λ^anh_4),
  (λ^anh_3)²), tiny; (iv) non-cubic crystals: the IA width tensor ⟨P_αP_β⟩. 2411.03433 §II.B uses the isotropic approximation for the IA width (q̂ = ẑ)
  **as a declared and quantified approximation** (ω̄_d differs by 6–8% along xy for Al₂O₃) [FT, CONFIRMED; v3 rewording, A-26, B-21], not an
  omission.
- **Pointer to WP3/WP1 [D].** WP1-v3 §6.1 shows that the projection of an O_h- or T_d-invariant finite-k ELF on ℓ = 2 vanishes **at every k**, so the
  Migdal ELF daily modulation in Si, Ge and GaAs is zero beyond the soft limit too; this supersedes v2/v3's caveat "conditional on 2607.06005's
  soft-limit form" (R9, AUDIT-2 §8 anisotropy note). Any nonzero value is a k-mesh or symmetry-breaking artefact.

---
## 9. LIMITS entries (τ point per CONVENTIONS §11; source formulas quoted [FT] in source notation and units)

**L4. Single phonon; dark photon via Born charges.** τ: S^{GS}_κκ, S^{GS}_cc; `nB=0|ng=0|nA=0|X=-|nT=0|K=1ph-coh|Mg=-|nD=-` + `T=0;ref=normal;
scr=ext,DFPT,ion;conv=-` (𝒳 enters only through ε_∞, Z*, DFPT).
- *Source quotes* [FT]: 1910.08092 Eq. (92): "R = (1/m_cell)(ρ_χ/m_χ)(πσ̄/2μ²)∫d³q/(2π)³ ℱ_med²(q) Σ_ν (1/ω_{ν,k}) |Σ_j e^{−W_j(q)}m_j^{−1/2}
  e^{iG·x⁰_j}(Y_j·ε*_{ν,k,j})|² g(q,ω_{ν,k})"; Eq. (105): "Y_j = −q²(q·Z*_j)/(q·ε_∞·q)"; Eq. (106): the same with
  q⁴/(q·ε_∞·q)² and (q·Z*_j·ε*_{ν,k,j}). 1807.10291 Eq. (29): "ℳ_{q+G,ν} = iee′Σ_j (2Ωm_jω_{ν,q})^{−1/2}(q+G)·Z*_j·e*_{j,ν,q}/((q+G)·ε_∞·(q+G))";
  Eq. (32): "ℳ^iso_q = ie′[(ω_LO/2)(1/ε_∞ − 1/ε₀)]^{1/2}/|q|". 1712.06598 Eq. (5): "C_F = e[(ω_LO/2V_cell)(1/ε_∞ − 1/ε₀)]^{1/2}", Eq. (7):
  "|ℳ_q|² = (κ²g_X²/e²)C_F²/q²". Also 1911.03482 Eq. (8) [UNRESOLVED]; 2009.13534 (single-phonon rate, general operators). All quotes above
  except 1911.03482 CONFIRMED against the full text by REF-B (and 1712.06598 by REF-A).
- *Chain:* WP0-v2 (3.3) → (1.1) GS at n_B = 0 → harmonic (2.2) at n_ph = 1, T = 0 → vertex c_κ (nucleon A_κF^M_κ, 1910.08092 Eq. (94); charge
  𝒵_κ → q·Z*_κ (1.2)) → dark photon: WP0-v2 (5.4) ≡ (4.2) → one branch (4.3). Map: ℱ_med ↔ F_DM, g(q,ω) ↔ 𝒢, m_j ↔ M_κ, ε* ↔ e* (x⁰ phase).
- *Validity (Si/Ge/GaAs):* q ≪ q_BZ (2.28/2.19/2.19 keV, q_BZ ≡ 2π/a) for the Z* vertex and analytic eigenvectors (the full (2.2) holds at all q
  with Umklapp); ω_LO ≪ E_g, adiabatic (static-DFPT) error O(ω_Q²/E_g²) (F11): GaAs (36 meV/1.5 eV)² ≈ 6×10⁻⁴; T ≪ ω; harmonic, η_anh ≈ 0.01–0.03.
- *Leading corrections:* finite-q charge vertex (valence deformation, dynamical quadrupoles (4.5)), O(qa) relative in polar crystals and leading
  in Si/Ge; FC e^{−2W}: 2W ≈ 6×10⁻⁴ at q = 1 keV in Si [E] (⟨u_x²⟩ ≈ 0.0025 Å²), which is also the size of the vertex DW-bookkeeping ambiguity
  (additive (1.2) vs multiplicative, §1.2; v3, B-1); anharmonic linewidth A^ph_ν (6.2a), O(10⁻³) for Si optical phonons
  [E]; dark photon in Si: two-phonon term from ∂Z*/∂u.
- *Discrepancies:* (a) 1712.06598 Eqs. (5), (7): C_F² ∝ 1/V_cell makes |ℳ|² dimensionally E² in the continuum golden rule of their Eq. (6); the
  consistent (4.3) = 1807.10291 Eq. (32) has no cell volume (V_cell must be the normalisation volume, which cancels). (b) 1712.06598 Eq. (12) uses
  equal-mass eigenvectors, leaving a spurious LO term ∝ (√A₁ − √A₂)²q² [FT, CONFIRMED by both referees]; it is the paper's **declared rough
  ("≈") estimate** and numerically small ((√A_Ga − √A_As)² ≈ 0.09 against (√A_Ga + √A_As)² ≈ 289; v3, A-11). The exact long-wavelength
  eigenvectors give F_LO = 0 at O(q); the true leading LO term ∝ q²A₁A₂(q·Δr)²/A_tot (the q⁴a² term of 1911.03482 Eq. (44), UNRESOLVED as a quote)
  exceeds the spurious one for q ≳ 0.05–0.1 keV in GaAs [E] (REF-B: 0.05 keV angle-averaged). Convention factors: table (1.3). **Status ✔** (WP0-v2 (9.7)).

**L5. Multiphonon incoherent approximation and Poisson tail.** τ: S^{GS}_κκ, `K=multi-inc`, n_A = 0, any n_T (Bose factors in (3.1)).
- *Source quotes* [FT]: 2205.02250 Eq. (36): "S(q,ω) ≈ (2π/Ω_c)Σ_d (f̄_d)² e^{−2W_d(q)} Σ_n (q²/2m_d)^n (1/n!) (Π_{i=1}^n ∫dω_i D_d(ω_i)/ω_i)
  δ(Σ_jω_j − ω)"; 2411.03433 Eq. (24): the same with D^{q̂}_d and f_d²-bar; 2011.09477 Eq. (10): "|f(n,q)|² = (1/n!)(q/q₀)^{2n}e^{−q²/q₀²}"
  [UNRESOLVED]; 2607.24933 Eqs. (44), (47) (quoted in §3.3). Other quotes CONFIRMED by REF-B.
- *Chain:* (1.1) → harmonic (2.1) → drop shell terms (2.3) (equivalently, for q ≫ max(n_ph, 2W_κ)q_BZ, the BZ average (2.4) minus the κ ≠ κ′
  terms from **all** ΔR; v3, A-27, B-L5) → isotropic projected DOS (exact for cubic sites, §8.2) → T → 0 → (3.2) → Einstein → Poisson. Map: d ↔ κ, f̄_d ↔ c_κ, m_d ↔ M_κ, Ω_c ↔ Ω.
- *Validity:* n_ph ≥ 2 and q ≫ n_ph q_BZ, rates ω-integrated over ≳ ω_max (pointwise O(1) errors at band edges, §3.3); below n_ph q_BZ, and for
  crystals with a basis, the accuracy of the incoherent approximation is **[E]** (§2, (2.4) consequences); n_ph = 1 needs (2.2) at all q.
  x_R = q²/2M_κω̄ = 1 at q = 45.8 keV (Si) and 55.8 keV (Ge) (ω̄ ≈ 40, 23 meV [E]; WP2v3-C10). Multiphonon window q ≈ 10–100 keV, i.e. m_χ ≈ 1.9–19 MeV
  at the kinematic endpoint q = 2m_χv_max, v_max = 794.5 km/s.
- *Leading corrections:* coherent shell terms z|j₀(q|ΔR_{κκ′}|)|c̄^{n_ph} over pairs (ΔR, κ, κ′) (≈ 2–10% at n_ph = 2 in Si for q = 10–2 keV, §3.3); anharmonic (6.2d); Bose factors (3.1),
  O(e^{−ω/T}); Migdal transfer of the f-sum ((1 − P_Mig), M_κ + δM_κ; (3.4)). Truncation error fixed exactly by (3.4′)/(3.4″), or removed by (3.5).
- *Discrepancies:* 2607.24933 Eq. (47): the isotropic 1/3 polarisation weight in the coherent term (§3.3; CONFIRMED; not used in their numerics [FT]);
  1911.03482 per-cell convention (1.3) (UNRESOLVED). **Status ✎ (control):** x_coh replaced by n_ph and the shell
  parameter (WP2-D1, applied in WP0-v2 Table 6.1).

**L6. Free nuclear recoil, Helm.** τ: S^{GS}_κκ, `K=imp`, any n_A (cumulants exact), plus X remainder through (5.2).
- *Source quotes* [FT]: hep-ph/0608035 Eq. (5): "dR_i/dE = ρσ_i^{SI}|F(q)|²/(2mμ_i²) ∫_{v>q/2μ} f(v,t)/v d³v"; Eq. (9): "|F^{SI}(q)|² =
  (3j₁(qR₁)/(qR₁))² e^{−q²s²}" [both hep-ph/0608035 quotes UNRESOLVED]; 2205.02250 Eq. (39): "S^IA(q,ω) = Σ_d ((f̄_d)²/Ω_c)(2π/Δ_d²)^{1/2} exp(−(ω − q²/2m_d)²/(2Δ_d²))", Eq. (42):
  "S^FR(q,ω) = Σ_d (2π/Ω_c)(f̄_d)²δ(ω − q²/2m_d)". Map: dR_i/dE ↔ dℛ/dE_R, ∫f/v ↔ η(v_min), Δ_d ↔ σ_ω.
- *Chain:* (1.1) → self part → IA (5.3) → narrow width → WP0-v2 (3.4) with hypothesis (I) → WP2v3-C8.
- *Validity:* x_R ≫ 1 (q ≳ 2(2M_κω̄)^{1/2} = 91.5 keV Si, 112 keV Ge, i.e. m_χ ≳ 17.3 (Si), 21.1 (Ge) MeV at the kinematic endpoint
  q_max = 2m_χv_max; v1's "20–40 MeV" is withdrawn); threshold far from the endpoint in units of σ_ω = (q²ω̄/2M_κ)^{1/2}; no electronic excitation
  (X weight O(κ_BO⁴)); E_R above the displacement threshold changes the partition (WP5), not S.
- *Leading correction:* Gaussian smearing σ_ω² = 4E_RE^kin_q̂ with the true (zero-point plus anharmonic) kinetic energy; then the skewness 𝔨₃^{GS}
  (5.2), not ⟨∇²V_pot⟩ (whose value (5.2′) is X-dominated), **computed directly as a GS cumulant, never as 𝔨₃ − 𝔨₃^X** (§5.2; v3, B-L6); the mean is
  exact. Near threshold this is the "Poisson tail" enhancement of 2011.09477.
- *Discrepancy:* none. *Clarification:* 2205.02250's "true peak shifted" refers to the mode, which does shift; the mean (𝔨₁) is exact (5.1). (v2's
  "discrepancy" REFUTED and withdrawn, A-14, B-20.) **Status ✎ (WP2-D4)**, applied in WP0-v2 (9.7).

**L18. Anharmonic NR corrections.** τ: S^{GS}_κκ, n_A = 1, K = multi-inc or imp.
- *Source quotes* [FT]: 2309.10839 Eq. (9): "S(q,ω) ≈ 2πΣ_d n_d|f_d|² e^{−W_d(q)} Σ_n (1/n!)(q²/2m_d)^n (Π_i∫dω_i D_d(ω_i)/ω_i) δ(Σ_jω_j − ω)";
  Eq. (10): "W_d(q) = (q²/4m_d)∫dω′ D_d(ω′)/ω′"; also Eqs. (23)–(26), (39), (52)–(62); 2412.18330 [ABS].
- *Chain:* (1.1) with n_A ≥ 1 → self part (q ≫ q_BZ) → single site (neighbours frozen: no intersite Φ^{(3)}, no linewidths) → 1D along the
  maximum-anharmonicity direction → perturbation theory in λ^anh_3, λ^anh_4, or the IA with the cumulants (5.1).
- *Validity:* λ^anh_3 ≈ 0.01, λ^anh_4 ≈ 10⁻⁴ (Si, 2309.10839); q > q_BZ; the 1D reduction overestimates.
- *Leading corrections:* exact constraints (6.1) (nuisance: WP6-v3 type T (5.1″), (6.1′); R9, AUDIT-2 L18); linewidth and Fano terms (6.2a–b), absent from the single site;
  3D angular average of their f_k(θ,φ)².
- *Discrepancy:* e^{−W_d} vs e^{−2W_d} (§6.3) [FT, CONFIRMED by both referees]. **Status ✔.**

**L19 (lattice part). Daily modulation.** τ: full q-vector S^{GS}_κκ; K = 1ph-coh at n_ph = 1, multi-inc with D^{q̂} at n_ph ≥ 2.
- *Source quotes* [FT]: 2411.03433 Eq. (24) (quoted under L5, with D^{q̂}_d(ω) of their Eq. (18)); 2607.06005 Eq. (10): "dR/dω ∼ ∫dq qF(q²)∫dω_q
  Σ_{ℓmm′} T_ℓm(q,ω_q,ω)ℛ^{(ℓ)}_{mm′}(t) f̂_{ℓm′}(s,v_lab)" (their T_ℓm ↔ S_ℓm, f̂ ↔ f̂^{(0)} of NOTATION F; "∼" is theirs) [UNRESOLVED].
- *Chain:* WP0-v2 (3.3) with the full q-vector S → (8.1); phonon S from (2.2) at n_ph = 1 and (3.2) with D^{q̂} at n_ph ≥ 2.
- *Validity:* (8.1) hypotheses; incoherent approximation for n_ph ≥ 2 as in L5. *Leading corrections:* cubic crystals §8.2 (i)–(iii); non-cubic (iv).
- *Discrepancy:* none in normalisation. 2411.03433's isotropic IA width (q̂ = ẑ) is a declared and quantified approximation (6–8% in ω̄_d for
  Al₂O₃), not an omission (v3, A-26, B-21). **Status ✎** (WP4-D6 converse, owned by WP0-v2/WP4).

---
## 10. Gaps assigned: closing formulas and computation specifications

**G3, lattice side: the multiphonon S_NN that WP5 needs.**
- *Formula:* (2.2) at n_ph = 1 (coherent); (3.2) via (3.5) for n_ph ≥ 2; (5.3) for the IA; final-state spectra (3.6) and branch content. For NR the
  MD seed is the struck atom with momentum p + q, p ~ 𝔫_κ(p) of (5.3), exact to leading order in 1/q; the energy partition (heat, defects, charge) is
  WP5's transport problem. GS normalisation: subtract E^{Mig}_1 if Migdal is seeded separately (3.4).
- *Computation:* (i) QE pw.x/ph.x (LDA/PBEsol; Si/Ge ecut 50–60 Ry, k 8³, DFPT q 8³) → phonopy Fourier interpolation onto 48³: D_κ^{αβ}(ω), B_κ,
  branch-projected DOS, tetrahedron resolution 0.1 meV. (ii) i-PI PIMD (P ≈ 32 beads at 10 K; 216-atom cell; MLIP or DFTB) for 𝔫_κ(p), E^kin_q̂,
  ⟨∂_q̂²E^ad_0⟩ and 𝔨₄, converged to < 1%. (iii) New module (≈ 300 lines): solve (3.5) per (q, q̂) on an ω grid (N_ω ≈ 10⁴): forward march at T = 0, FFT
  of e^{−2W_κ}[e^{Φ_κκ(0,t)} − 1] with a regulator at T > 0 (v3, B-23); output S_κ(q,ω), P_ph(n_ph|q,ω), ρ^ph_κν(ω′|q,ω).
- *Cost:* DFPT ≈ 10² CPU·h; PIMD ≈ 10³ CPU·h with an MLIP; tables ≈ minutes.
- *Outputs:* HDF5 tables of S(q,q̂,ω) and ρ^ph(ω′|q,ω) for q ∈ [0.1, 300] keV, ω ∈ [0, 50] eV, with the IA-to-free switch at x_R > 16 and the
  Edgeworth 𝔨₃^{GS}, 𝔨₄ terms (𝔨₃^{GS} from PIMD directly, §5.2); library key τ per §9. **Validity flag (v3, B-23):** cells with n_ph ≥ 2 and
  q ≲ n_ph q_BZ (q ≲ 2–10 keV) lie outside (2.4); they must be flagged in the tables or routed to the coherent (2.2) (specified under G13), and the
  inter-sublattice pairs (ΔR, κ ≠ κ′) must be added there (IF-13).

**G11 (lattice): anisotropy and modulation.**
- *Formula:* (8.1) with the S_ℓm of (2.2) and (3.2).
- *Computation:* n_ph = 1 from phonopy eigenvectors (48³ mesh, Umklapp to |q+G| = 30 keV), projected onto Y_ℓm (ℓ ≤ 12 cubic, ≤ 8 for Al₂O₃/SiC;
  Lebedev grid of 590 points); n_ph ≥ 2 from D^{αβ}_κ (2411.03433 Eq. (20)) inserted in (3.5) per q̂; shell corrections from Φ_{κκ′}(ΔR,t) for
  the first 4 pair shells, indexed by (ΔR, κ, κ′) (|ΔR_{κκ′}| ordered; v3, B-23); the IA ⟨P_αP_β⟩ tensor from PIMD. Cost ∝ N_k·N_G·N_q̂ ≈ 10⁸ cheap operations. Output: S_ℓm(q,ω) tables and P_ℓ-projected 𝒢 for
  SHM and halo-independent inputs (WP6).
- *Prediction to test:* for Si, Ge, GaAs, S_{ℓ≥4} vanishes in the incoherent multiphonon part, up to the shell and 𝔨₄ terms.

**G13: anharmonicity.**
- *Formula:* (6.2) for the coherent n_ph = 1, 2 terms, 𝒞₃, 𝒞₄ for the incoherent n_ph ≥ 2 terms, (5.1) for the IA, all constrained by (6.1).
- *Computation:* phono3py (fc3 on 4×4×4 primitive cells (128 atoms), pair cutoff ≈ 5 Å, ≈ 300 supercell DFT runs for Si) → Π^ph_ν(Q,ω),
  A^ph_ν(Q,ω) on 24³; hiPhive or TDEP for fc4 and T-renormalisation; 𝒞₃(t), 𝒞₄(t) by contracting phonon propagators (∝ N_k² per t point,
  ≈ 10³ CPU·h) [D, sketch: the contraction is specified only in structure, A-28]; PIMD δE^kin_q̂ (6.1) as the independent exact anchor.
- *Output:* nuisance template Δ^τ_A(q,ω) satisfying (6.1), typed per (6.1′), with an uncertainty from the fc3/fc4 fit and supercell convergence.

**L4 add-on (charge vertex at all q; serves G3 and dark-photon multiphonon at q < q_BZ).** Store the DFPT density response per Q in (i) and
Fourier-transform: 𝒵_{κα}(Q+G) = q_α(Z_κ − f^core_κ(q)) − δρ^val_{κα}(Q+G), q = Q + G, for |q| ≤ 20 keV (≈ 4000 G-vectors). This interpolates between
Born, Z*, quadrupoles and the rigid-ion (Brown-type) charge; negligible cost on top of DFPT.

---
## 11. WP0 defects reported by WP2 (status after WP0-v2)

| Label | Defect (v1 §11) | Status |
|---|---|---|
| WP2-D1 | x_coh = q/G_min is not the coherence control: not sufficient (n_ph = 1 coherent S stays a δ on the dispersion at any q), not necessary (n_ph ≥ 2 incoherent accurate in ω-integrated rates below q_BZ); use n_ph + shell parameter (2.3)–(2.4) | applied, WP0-v2 Table 6.1 (#10). **v3:** the "not sufficient" half stands [D]; the "not necessary … below q_BZ" half is **[E]** only (corrected (2.4) holds for q ≫ n_ph q_BZ; IF-10) |
| WP2-D2 | "2W = (q²/2M)⟨coth(βω/2)/ω⟩" holds only for isotropic B_κ (cubic sites); in general 2W_κ = q·B_κ·q, direction-dependent, enters L19 | applied (#10) |
| WP2-D3 | K label "coherent 1-ph (x_R ≪ 1)" conflates two parameters; a one-phonon incoherent regime exists at q_BZ < q ≪ (2Mω̄)^{1/2} (Si ≈ 5–20 keV) | applied (#10; K = 1ph-inc) |
| WP2-D4 | L6 pointer: mean exact (𝔨₁); width with the true E^kin_q̂; skewness from the BO curvature, remainder in X (5.2) | applied (#32) |
| WP2-C1 | WP0 §5.3 "Z*/ε_∞ (Fröhlich) vertex for LO phonons": for nucleon coupling the external vertex stays A_κF^M_κ; Z*/ε_∞ appears only inside the TO → LO Dyson series (4.4); external Z*/ε_∞ belongs to charge coupling (4.2) | applied (#8) |

No error found in WP0-v2 (3.1)–(3.4), (4.3)–(4.6) or (5.2)–(5.4) as used here; WP2v3-C1, C2, C8, C11d confirm (5.4), (3.4) and the operator form of
(4.7). On the q → 0 evaluation of (4.7), (5.2″) derives the extra uniform-density term 2𝓃_e found by REF-WP0-A (IF-1).
Notation remark (not a physics defect): WP0-v2 §6.2 (ii) writes the potential energy as V, which NOTATION reserves for the crystal volume; WP2-v2 uses
V_pot (flag IF-5, closed by NOTATION v4).

---
## 12. Exact remaining gaps
1. Coherent n_ph = 2 at q < q_BZ from first principles: formula (2.2), computation specified (G13), not done; the §3.3 shell estimate is [E].
2. A rigorous pointwise (fixed q, ω) error bound on the incoherent approximation at n_ph ≥ 2. Only the BZ average (2.4) is derived, asymptotically
   for q ≫ max(n_ph, 2W_κ)q_BZ, and for a basis it includes the inter-sublattice pairs; the band-edge O(1) failure is identified. The regime
   q ≲ n_ph q_BZ, and the size of the κ ≠ κ′ terms in Si/Ge/GaAs (up to ≈ 0.16 at n_ph = 2 from the nearest pairs, partly cancelled by farther pairs of opposite-sign weight [E]), need the coherent (2.2) (G13).
3. T > 0 shell sum at n_ph = 2 is absolutely divergent (acoustic Φ ~ T/ΔR, Σ|Φ|² ~ linear) and defined only as a lattice Fourier sum (a distribution
   in q, finite away from q = G); needs an Ewald-type resummation (irrelevant at mK).
4. Decay of the valence charge deformation at q ≫ q_BZ is [E]; the DFPT add-on of §10 decides it.
5. Non-perturbative anharmonicity (soft-mode, light-atom targets) lies outside (6.2); not needed for Si/Ge/GaAs (λ^anh ≈ 0.01).
6. Amorphous targets: (2.1) needs configurational averaging, not covered.
7. The GS/X split (5.2) rests on the WP0-v2 §6.2 (ii) Migdal amplitude ([D, sketch] for the boost reduction). Its first moment agrees with WP3
   J3 and its contact face with WP0-v2 (4.7) at q → 0 (5.2″, with the 2𝓃_e term); WP3 must still evaluate 𝔨₃^X from the all-electron (W.5) against
   (5.2′)/(5.2″) at the q used. The moment identity (F4) is CLOSED (AUDIT-2: WP0-v3 (4.7′) = WP2 (5.2″) = WP3-v3 J8(ii)); the numerical
   all-electron evaluation remains OPEN (OW0-8).
8. Finite-q eκ factor Δ𝓃_κ(q) of (5.2″) beyond the hydrogenic 1s² model (L shell, valence anisotropy ∝ q̂_xq̂_yq̂_z): all-electron density needed [E].

---
## 13. Literature, with R7 status (IDs verified against the arXiv API in v1, 2026-10-31)
Full texts read by the author in v1/v2 ([FT] list of v2 §13 unchanged). Status after R7: **CONFIRMED** = checked against the full text by at least
one referee (REF-A and/or REF-B, literature/papers-r7-WP2-A/, -B/); **UNRESOLVED** = no referee read the source; **REFUTED** = dropped.

| Paper, location | Claim in this return | R7 status | Where |
|---|---|---|---|
| 2607.24933 Eq. (47) (PDF 4.23), Eqs. (44), (46), (48) | isotropic 1/3 polarisation weight incorrect in the coherent term at fixed Q; declared "monoatomic, isotropic" scope; not used numerically [FT, A and B] | **CONFIRMED** (A, B); the intra-cell-phase charge **withdrawn** (outside the paper's scope) | §3.3, L5 |
| 1712.06598 Eqs. (5)–(7) | spurious 1/V_cell in C_F² (|ℳ|² ~ E² in the golden rule of Eq. (6)) | **CONFIRMED** (A, B) at formula level; propagation to their curves not checked | L4 (a) |
| 1712.06598 Eq. (12) | equal-mass eigenvectors, spurious LO ∝ (√A₁ − √A₂)²q² | **CONFIRMED** (A, B); declared rough estimate, numerically small | L4 (b) |
| 2309.10839 Eqs. (9), (10), (13) | e^{−W_d} should be e^{−2W_d} | **CONFIRMED** (A, B; paper v1) | §6.3, L18 |
| 2009.13534 text after Eq. (31) | drops the nonzero unordered-spin (incoherent) channel | **CONFIRMED** (A, B) | (7.1) |
| 2205.02250 below Eq. (38) | "peak shift" listed as a discrepancy | **REFUTED** (A, B): dropped; the mode does shift, the mean is exact | (5.1), L6 |
| 2411.03433 §II.B, Eqs. (12), (18), (24) | IA width with q̂ = ẑ; cubic isotropy explains negligible Si/GaAs modulation | **CONFIRMED** (A, B); "omission" reworded to "declared, quantified approximation" | (8.2), L19 |
| 1910.08092 Eqs. (92), (105), (106); line (91) | quotes; one-phonon π/Ω form on the line tagged (91) (v2 cited (90)) | **CONFIRMED** (B) | (2.2), L4 |
| 1910.08092 Eqs. (94), (98)–(104), (104) f_e term | Born-charge reduction, nucleon vertex, f_e term | **UNRESOLVED** (not re-read; the derivation (1.2) is independent) | (1.2), (4.4) |
| 1807.10291 Eqs. (29), (32) | dark-photon one-phonon and one-branch |ℳ|² | **CONFIRMED** (B) | (4.2), (4.3), L4 |
| 2205.02250 Eqs. (36), (39), (42) | multiphonon incoherent, IA, free-recoil forms | **CONFIRMED** (B) | (3.2), (5.3), L5, L6 |
| 1911.03482 Eqs. (2), (8), (12), (13), (16), (17), (44) | convention factor; one-, two-phonon and anharmonic agreements; q⁴a² LO term | **UNRESOLVED** (no referee fetched it) | (1.3), (2.2), (6.2), L4 |
| 2506.11191 Eqs. (68)–(72), (69) footnote 6 | unpolarised spin channel; convention factor | **UNRESOLVED** | (1.3), (7.1) |
| 2011.09477 Eq. (10) | Einstein-solid Poisson law | **UNRESOLVED** | (3.2), L5 |
| hep-ph/0608035 Eqs. (5), (7)–(9) | free-recoil rate, Helm form factor | **UNRESOLVED** (the chain to Eq. (5) is checked by C8) | (5.3), L6 |
| 2607.06005 Eqs. (6), (10) | harmonic rate structure; soft-limit Migdal ℓ = 0, 2 | **UNRESOLVED** | (8.1), (8.2), L19 |
| 2412.18330 | anharmonic NR corrections | [ABS] only, UNRESOLVED | L18 |

Classical results without arXiv source (flagged): Placzek moments; Sears expansion; Ambegaokar–Conway–Baym; Gonze–Lee non-analytic dynamical matrix;
Born–Huang drag mass (via WP3); Rayleigh expansion and the spherical-Bessel integrals used in (5.2″) (checked in C11e–g).

---
## 14. Referee disagreements settled, and rebuttals

**Disagreements between REF-A and REF-B (each settled by derivation).**
1. **Vertex Debye–Waller bookkeeping (A-1 STANDS vs B-1 STANDS WITH CORRECTION). B is right.** For a harmonic Gaussian state
   ⟨1|e^{iq·u}|0⟩ = i q·⟨1|u|0⟩e^{−W} (WP2v3-C14, exact), while the additive deformation term δρ_κ·u of (1.2) has the matrix element ⟨1|δρ_κ·u|0⟩
   with no e^{−W}. So attaching e^{−W_κ} to the whole 𝒵_κ differs from (1.2) by a relative O(2W_κ) in S for the non-rigid part. A's verdict covers
   the reduction (1.1)–(1.2) and its limits, which do hold; it did not examine the bookkeeping in (2.2). Applied in §1.2, §2, L4.
2. **Scale of the gradient terms in (2.4) (A-4: O(q_BZ/q), q ≫ q_BZ; B-4: q ≫ n_ph q_BZ). B's scale is right, with one refinement.** The held
   factors are Φ^{n_ph} ∝ q^{2n_ph} and e^{−2W_κ(q)}, whose relative variation over the BZ is 2n_ph p/q and 4W_κ p/q. For the self term the
   linear order vanishes because the BZ is inversion-symmetric, leaving O((n_ph q_BZ/q)²) (C9c: n(2n−1)q_BZ²/(12q²) in 1D). The cross terms keep a
   linear piece (∫_BZ p e^{−ip·ΔR_{κκ′}} ≠ 0, C9c). The controlling hypothesis is q ≫ max(n_ph, 2W_κ)q_BZ. A's statement is the n_ph = O(1) case.
3. **Compound-Poisson equation (A-8 STANDS vs B-8 STANDS WITH CORRECTION). Both are right about the identity (C4, C4b); B is right about the
   numerical route.** At T > 0, w_κ has ω′ < 0 support, so the bin at ω couples to S at ω − ω′ > ω and (3.5) is not triangular; the solution
   is the time-domain e^{Φ(t)}, computed by FFT. Applied in (3.5), G3.
4. **Normalisation of (6.1) (A-19 STANDS WITH CORRECTION vs B-15 STANDS). A is right.** S_self = 2π𝓃_κ|c_κ|²·P(ω) with ∫P dω = 1 (from
   ∫(dω/2π)S_self = 𝓃_κ|c_κ|², (3.4)), so the variance identity carries (2π/Ω)|c_κ|² (C12b). B's check (linearity, concavity) is about (6.1′),
   which is unaffected.
5. **"Exactly incoherent" spin channel (A-22 STANDS vs B-18 STANDS WITH CORRECTION). Both are right about different statements.** The incoherence
   is exact: ⟨𝐈^β⟩ = 0 under (S1)–(S3) removes every inter-site term whatever the lattice. Identifying the lattice factor with the average-lattice
   S̃_self is not exact: the spin-carrying isotope's mass differs (O(ΔM/M) ≈ 3.5% for ²⁹Si). B's caveat is applied to the identification only.
6. **2205.02250 (A-14 STANDS WITH CORRECTION vs B-20 FALLS).** The substance is the same: the source is correct and the "discrepancy" is withdrawn.
   It is recorded as **dropped** (B's label is the precise one for the literature claim; A's "stands" refers to the physics that 𝔨₁ is exact, which
   is kept).
7. **1712.06598 Eq. (12) (A-11 STANDS WITH CORRECTION vs B-10 STANDS).** Both CONFIRM it. A's framing (a declared "≈" estimate, numerically
   negligible next to the acoustic weight) is applied. B's crossover (≈ 0.05 keV) is kept next to v2's 0.1 keV as a range. The two do not conflict:
   they compare the spurious term against different references (the LA weight vs the true LO term).
8. **Gap closures (A-28 STANDS vs B-23 STANDS WITH CORRECTION). B is right.** This follows from disagreement 2: the G3 cells with n_ph ≥ 2 at
   q ≲ n_ph q_BZ rely on (2.4) outside its validity, and the T > 0 route is the FFT (disagreement 3). A's "real specification" verdict is kept.

**Rebuttals: none.** Every referee correction is applied. Two statements go beyond the referees; both are derived and checked, and neither
contradicts them. (i) On (5.2′) (A-16, B-13, both STANDS): ⟨∂_α∂_βV⟩ is absolutely defined only for the neutral V_eN + V_NN, so the κκ moment
should be called the self potential moment and not "|_{V_eN}". (ii) On (5.2″) (A-17, B-14): besides the O((q a_{1s})²) core term the referees
found, the eκ moment has a q-independent uniform-density term 2𝓃_e as q → 0⁺ (C11e). This agrees with REF-WP0-A's finding on WP0-v2 (4.7)
(SOTA R7).

---
## 15. Interface flags
Changes that alter a quantity another package uses are marked **CHANGED**.

| # | Owner | Quantity | Recorded form | Mismatch / action |
|---|---|---|---|---|
| IF-1 (F4) **CHANGED** | WP3, WP0-v2 (REV-WP0) | κκ/eκ third moments; X-sector ω³ moment | WP2 (5.2), (5.2′), (5.2″); WP0-v2 (4.7); WP3 J3, J8, (W.5) | v2's "𝓜³_κκ\|_{V_eN} = −(m_e/M_κ)𝓜³_eκ exactly" is withdrawn. The relation holds for the contact (trace) term at every q. For the full moments it holds only up to relative 2𝓃_e/𝓃_e(R_κ) ≈ 1.2×10⁻⁴ (q → 0⁺) plus (q a_{1s,κ})²/10 (Si: 9% at 51 keV, 29% at 102 keV). (5.2″) derives REF-WP0-A's 𝓃_e(R_κ) + 2𝓃_e at q → 0⁺ (REV-WP0 settles the (4.7) dispute; WP2's derivation supports A, read as the q → 0⁺ limit). WP3 J8 must compare at q → 0 or against (5.2″) at its q; valence/soft truncations (WP3 T3) cannot saturate (5.2′). **R9: F4 CLOSED at moment level** (AUDIT-2): WP0-v3 (4.7′), WP2 (5.2″)\|_{q→0⁺} and WP3-v3 J8(ii) are identical including the 2𝓃_e term; WP0-v3's O(q³) at T_d sites matches the ∝ q̂_xq̂_yq̂_z remainder of (5.2″) |
| IF-2 (F6) **CHANGED** | WP2 → WP5 | multiphonon S^{GS}_κκ, ρ^ph_κ, GS f-sum | WP2 (2.2), (3.4), (3.6) as used in WP0-v2 (7.3) | WP5 must (i) treat ω′ < 0 entries of ρ^ph_κ as absorbed phonons (⟨n_ph⟩ counts both); (ii) when Migdal is seeded separately, use GS = (1 − P_Mig)·S^{GS} with mass M_κ + δM_κ (v2: subtract E^{Mig}_1 only), consistent with REF-WP5-A (R7) and WP5-v3 §3.1. R9 (AUDIT-2 B3): WP0-v3 rule (a) and WP3-v3 J3/N1 must adopt 𝓜¹_X = 𝓃_κ[E^{Mig}_1 + P_Mig q²/2M_κ]; WP2 unchanged |
| IF-3 **CHANGED (extended)** | WP0-v2 | Table 6.1 truncation statement | "P[Pois(2W) ≥ N]" | Consistent for one site. With several sites the loss is the \|c_κ\|²/M_κ-weighted mean (3.4″); at T > 0 it refers to the signed first moment |
| IF-4 **CHANGED** | WP6 | anharmonic constraints and nuisance type | WP6 (5.1) M/A/E/Δ; WP2 (6.1), (6.1′) | The third identity of (6.1) now carries (2π/Ω)\|c_κ\|² (or else use normalised S_self). M type preserves (6.1) only at θ ∈ {0,1}. **R9:** nuisance = WP6-v3 type T (5.1″) (exact constraints, PSD); WP6 adopted the normalisation (n_κ) |
| IF-5 | NOTATION / WP0-v2 | V_pot, E^ad_n | NOTATION v4 rows exist | **CLOSED** (v4 §M rows) |
| IF-6 | NOTATION | q_BZ ≡ 2π/a_lat, G_min | NOTATION v4 row exists | **CLOSED**; v3 uses a_lat |
| IF-7 (F11) | X2 / WP1 | static-DFPT error | O(ω_Q²/E_g²) | consistent, no change |
| IF-8 (F3, F7) | WP3, WP5 | sector labels, thermal factor | WP0-v2 (7.1), (5.6) | **CLOSED** |
| IF-9 | WP4 (relay) | one-phonon eigenvector phase | e^{iq·r_κ} (CONVENTIONS §5) | consistent, no change |
| IF-10 **CHANGED** | WP0-v2 (Table 6.1, WP2-D1), SOTA, LIMITS L5 | BZ-average theorem (2.4); coherence control | "incoherent = BZ-averaged coherent S"; "n_ph ≥ 2 incoherent accurate below q_BZ" | (2.4) is exact only for Bravais lattices, and only asymptotically for q ≫ max(n_ph, 2W_κ)q_BZ. With a basis, every inter-sublattice pair adds j_BZ(ΔR_{κκ′})S_{κκ′,ΔR} (Si nearest neighbours j_BZ ≈ 0.44 each). The "below q_BZ" half of WP2-D1 is **[E]**. The shell estimate is ≈ 2–10% (q = 10–2 keV), not "≈ 2%"; shells are indexed by (ΔR, κ, κ′). Owners citing WP2 (2.4) must add both qualifiers |
| IF-11 | NOTATION | δρ_κ(q) row text | "valence charge-response vector" | contradicts the v4 row "δρ^val_κ … valence part of δρ_κ" and (1.2). Proposed text: "electronic charge-response vector (core + valence); δρ^val_κ = δρ_κ − q f^core_κ". Text only, no symbol change |
| IF-12 | WP5 | (3.5) numerical route | "O(N_ω²) march" | T = 0 only; at T > 0 use the FFT of e^{−2W}[e^{Φ(t)} − 1] with a regulator (§3.5, G3) |
| IF-13 **CHANGED** | WP5 (G3 tables), WP4/WP0-v2 (L19) | multiphonon tables at small q | G3 grid from q = 0.1 keV, (3.2) for n_ph ≥ 2 | Cells with n_ph ≥ 2 and q ≲ n_ph q_BZ must be flagged or computed from the coherent (2.2), with the (ΔR, κ ≠ κ′) pairs |
| IF-14 | LIMITS (L5, L6, L19 text), WP0-v2 (9.7) | discrepancy entries | v2 wording | L6: the 2205.02250 discrepancy is deleted (now a clarification). L5: the 2607.24933 charge is limited to the polarisation weights. L19: 2411.03433's IA width is a declared approximation. L4 (b): 1712.06598 Eq. (12) is a declared estimate |

---
## 16. Closing table: R7 referee items
Disposition: **applied** (text changed as the referee asked, or with a derivation where the referees disagreed), **kept** (verdict STANDS; no
change needed), **dropped** (claim removed), **rebutted** (none).

| Item | Verdict | Disposition | Where (v3) |
|---|---|---|---|
| A-1 | STANDS | kept (reduction holds); B-1's bookkeeping point added (§14 #1) | §1.2 |
| A-2 | STANDS | applied (A9d): 1911.03482 contact term and 1910.08092 π/Ω marked UNRESOLVED/CONFIRMED; (90) → (91) | §2 checks, §13 |
| A-3 | STANDS W/ CORR | applied: T > 0 shell sum "absolutely divergent, a lattice Fourier sum" | §2 shell bullets, §12 gap 3 |
| A-4 | STANDS W/ CORR | applied: (2.4) with all inter-sublattice pairs, Bravais-only identity, C9 re-described, C9b added | (2.4), §0 item 2, L5, §11, §12, IF-10 |
| A-5 | STANDS W/ CORR | applied: caveat quoted, intra-cell charge withdrawn | §3.3, §0 item 3, L5, §13 |
| A-6 | STANDS | kept | (3.1)–(3.2) |
| A-7 | STANDS | applied: species-weighted form (3.4″), C3d | (3.4′), (3.4″) |
| A-8 | STANDS | kept (identity); route refined per B-8 (§14 #3) | (3.5) |
| A-9 | STANDS | kept; hypotheses stated explicitly | (4.2) |
| A-10 | STANDS | kept (CONFIRMED) | L4 (a), §13 |
| A-11 | STANDS W/ CORR | applied: declared rough estimate, numerically negligible | L4 (b), §13 |
| A-12 | STANDS | kept | (4.3)–(4.5) |
| A-13 | STANDS | kept | (5.1) |
| A-14 | STANDS W/ CORR (REFUTED claim) | **dropped**: 2205.02250 "discrepancy" withdrawn; clarification kept | (5.1), L6, §13 |
| A-15 | STANDS | kept | (5.2) |
| A-16 | STANDS | kept; v3 precision (neutral V_eN + V_NN, self part) | (5.2′) |
| A-17 | STANDS W/ CORR | applied: q a_core qualifier, quantified (5.2″), C11e–g | (5.2″), §0 item 6, IF-1 |
| A-18 | STANDS | kept; hep-ph/0608035 quote UNRESOLVED | (5.3) |
| A-19 | STANDS W/ CORR | applied: (2π/Ω)\|c_κ\|² in (6.1), C12b (§14 #4) | (6.1), IF-4 |
| A-20 | STANDS | kept | (6.3) |
| A-21 | STANDS | kept (CONFIRMED) | (6.3), L18 |
| A-22 | STANDS | applied (A9e): S̃_self starts at n_ph ≥ 1; isotope caveat per B-18 (§14 #5) | (7.1) |
| A-23 | STANDS | kept | (7.2) |
| A-24 | STANDS | kept | (8.1), (8.2) |
| A-25 | STANDS | kept (CONFIRMED) | (8.2) |
| A-26 | STANDS W/ CORR | applied: declared approximation | (8.2)(iv), L19, §13 |
| A-27 | STANDS W/ CORR | applied: L5 chain (κ ≠ κ′ from all ΔR), L6 clarification | §9 L5, L6 |
| A-28 | STANDS | applied: G13 contraction tagged [D, sketch]; B-23 defects fixed | §10 |
| A-29 | STANDS W/ CORR | applied: q → 0 qualifier relative to WP0-v2 (4.7) | (5.2″), IF-1 |
| A-30 | STANDS | kept | §14 |
| B-1 | STANDS W/ CORR | applied: DW bookkeeping (O(2W)), "(98)–(104) at O(u), q → 0", δρ_κ meaning, C14 (§14 #1) | §1.2, §2, L4, IF-11 |
| B-2 | STANDS | applied (citation slip): π/Ω form on line (91), not (90) | §2 checks |
| B-3 | STANDS W/ CORR | applied: pairs (ΔR, κ, κ′); 2–10% range and envelope; C10 | §2, §3.3, L5, IF-10 |
| B-4 | STANDS W/ CORR | applied: all-ΔR cross terms, Σj_BZ = 1, hypothesis q ≫ max(n_ph, 2W)q_BZ, C9b, C9c (§14 #2) | (2.4), §0, §11, IF-10 |
| B-5 | STANDS W/ CORR | applied: "incorrect for the coherent term at fixed k (polarisation weights), not used numerically" | §3.3, L5 |
| B-6 | STANDS | kept | (3.1)–(3.2) |
| B-7 | STANDS | applied: signed-moment, per-species, multiplicative-vertex qualifiers | (3.4′), (3.4″) |
| B-8 | STANDS W/ CORR | applied: forward march T = 0 only, FFT at T > 0; ⟨n_ph⟩ counts absorptions; C4b (§14 #3) | (3.5), (3.6), G3, IF-12 |
| B-9 | STANDS | kept | (4.2), (4.3) |
| B-10 | STANDS | kept; crossover range 0.05–0.1 keV (§14 #7) | L4 (b) |
| B-11 | STANDS | kept | (5.1) |
| B-12 | STANDS (OPEN on WP3's side) | applied: 𝔨₃^{GS} computed directly, never 𝔨₃ − 𝔨₃^X | (5.2), L6, G3 |
| B-13 | STANDS | kept; v3 precision as A-16 | (5.2′) |
| B-14 | STANDS W/ CORR | applied: q·a_1s ≪ 1, closed form reproduces 9%/29%, C11g | (5.2″), IF-1 |
| B-15 | STANDS | kept; normalisation fixed per A-19 (§14 #4) | (6.1), (6.1′) |
| B-16 | STANDS | kept (CONFIRMED) | (6.3) |
| B-17 | STANDS [E] | applied: Θ(ω_max) cutoff ignored, noted | (6.3) |
| B-18 | STANDS W/ CORR | applied: isotope mass disorder O(ΔM/M) on the identification (§14 #5) | (7.1), §0 item 8 |
| B-19 | STANDS | kept | (8.2) |
| B-20 | FALLS (as a discrepancy) | **dropped** | (5.1), L6, §13 |
| B-21 | STANDS W/ CORR | applied: declared approximation | (8.2)(iv), L19 |
| B-22 | STANDS | kept | (4.5) |
| B-23 | STANDS W/ CORR | applied: G3 cells q ≲ n_ph q_BZ flagged, FFT route, G11 pairs (§14 #8) | §10, IF-13 |
| B-24 | n/a | kept (nothing contested) | §14 |

**Count (54 items):** applied 26 (A 13, B 13); kept 26 (A 16, B 10 incl. B-24 n/a); dropped 2 (A-14 = B-20, the same 2205.02250 claim); rebutted 0.
Disagreements settled: 8 (§14). Cross-package (SOTA R7, not referee items): REF-WP0-A's (4.7) uniform term derived in (5.2″) (IF-1); REF-WP5-A's
Migdal prescription adopted in (3.4) (IF-2).

### 16c. R9 clean-up (coordinator, in place): VER-WP2-A/B optional items and AUDIT-2 rows addressed to WP2
| # | Source | Item | Disposition | Where |
|---|---|---|---|---|
| R9-1 | VER-WP2-A §3.1 | [FT] tag on "Eq. (47) not used in their numerics" | applied | §0 item 3, §3.3, L5, §13 |
| R9-2 | VER-WP2-A §3.2 | (2π/Ω)\|c_κ\|² = 2π𝓃_κ\|c_κ\|² assumes one κ site per cell | applied: 𝓃_κ = n_κ^{cell}/Ω, sum over sites | (6.1) |
| R9-3 | VER-WP2-B R1 (and VER-A §2a) | ≈ 0.16 counts nearest pairs only; farther pairs carry net weight 1 − 4·0.444 = −0.77 and partly cancel; phases reduce it | applied; C10 extended (farther-pair weight −0.775) | §2 consequences (ii), §12 gap 2 |
| R9-4 | VER-WP2-B R2 | keep [D] (uniform 2𝓃_e) and [D, sketch/E] (G ≠ 0 remainder) tags | kept (no change requested) | (5.2″) |
| R9-5 | AUDIT-2 B3 | X-sector first moment 𝓜¹_X = E^{Mig}_1 + P_Mig q²/2M_κ; GS = (1 − P_Mig)S^{GS} with M_κ + δM_κ | no WP2 change (WP2 is the reference form); action on WP0/WP3 noted | IF-2 |
| R9-6 | AUDIT-2 m10 | WP0 Table 6.1 not updated for WP2 IF-3, IF-10 | no WP2 change (WP0 erratum) | IF-3, IF-10 |
| R9-7 | AUDIT-2 m11 | WP6 phonon-order row to cite (3.4″) | no WP2 change (WP6) | (3.4″) |
| R9-8 | AUDIT-2 m18 | Ge x_R = 1 at 55.8 keV (23 meV), impulse onset 112 keV | no WP2 change: WP2 L5/L6 values are the reference (C10: 55.79, 111.6 keV); WP3 to adopt | §9 L5, L6 |
| R9-9 | AUDIT-2 m30 | NOTATION δρ_κ row text | no WP2 change (NOTATION owner) | IF-11 |
| R9-10 | AUDIT-2 §2 L4 | chain ✔ | no action | §9 L4 |
| R9-11 | AUDIT-2 §2 L5 | add the (2.4) qualifiers | already in WP2 L5 (chain and validity); LIMITS owner via IF-10 | §9 L5 |
| R9-12 | AUDIT-2 §2 L6 | 𝔨₃^{GS} computed directly | already in WP2 L6 and (5.2) | §9 L6 |
| R9-13 | AUDIT-2 §2 L18; §8 IF6-14; §4 nuisance note | WP2 (6.1′) M-or-A recommendation superseded by WP6-v3 type T (5.1″) | applied | (6.1′), §9 L18, IF-4 |
| R9-14 | AUDIT-2 §2 L19 | P,T-broken: density odd part O(q³); lowest odd ℓ from G_eff (WP6-v3 (1.5)) | applied | (8.2) selection rules |
| R9-15 | AUDIT-2 §4 (F4), §7 l.229, l.353 | WP0-v3 (4.7′) = WP2 (5.2″)\|_{q→0⁺} = WP3-v3 J8(ii), including 2𝓃_e; F4 CLOSED | applied: status recorded; numerical all-electron evaluation stays OPEN | IF-1, §12 gap 7 |
| R9-16 | AUDIT-2 §8 anisotropy note | WP1-v3's every-k statement supersedes WP2's "conditional on the soft-limit form" caveat | applied | (8.2) pointer |
| R9-17 | AUDIT-2 §8 flag table (WP2 IF-1…IF-14) | statuses A/M/N; IF-12, IF-13 N (WP2's own G3 spec) | no change; M items belong to WP0, WP6, NOTATION, LIMITS | §15 |
| R9-18 | AUDIT-2 §5 τ strings | `nT=0` + `T=` | already present (L4 τ string) | §9 |
| R9-19 | AUDIT-2 §9 gap table (G3, G11, G13) | status only | no action | §10 |

**R9 count (19 rows):** 7 applied (R9-1, 2, 3, 13, 14, 15, 16; C10 extended for R9-3); 12 need no WP2 change (already present, or another owner's action). No result changed.
Checks re-run: 31/31 PASS.

### 16b. R6 corrections (v1 → v2), kept for the record (unchanged; locations refer to v2's text, which v3 retains unless amended above)
| # | Correction (ID / source) | Where applied | How |
|---|---|---|---|
| 1 | ρ_χ = 0.4 flag (CORRECTIONS §8 r1; §15; CONVENTIONS §8, §13 item 3) | header, §0 | flag withdrawn; no halo number used except v_max = 794.5 km/s |
| 2 | §5.2 GS/X split needs WP3 confirmation, OPEN (CORRECTIONS §8 r2) | (5.2), §12 gap 7 | kept OPEN; scope of what remains stated |
| 3 | F4: compare 𝔨₃ split with WP0-v2 (4.7) and WP3 Migdal spectra (CORRECTIONS F4; WP0-v2 F4) | (5.2), (5.2′), IF-1 | explicit comparison: J3 first moment, contact identity, −m_e/M_κ relation; WP2v2-C6b, C11 |
| 4 | Sector rename G → GS, S^G → S^{GS} (CORRECTIONS §0, §8; F6; CONVENTIONS §13 item 18) | throughout | done |
| 5 | k_i (phonon) → Q_i (§8) | §2, §3 | done |
| 6 | ℓ (cell) → R; L → ΔR (§8) | §2, §3, §10 | x⁰_{Rκ}, u_{Rκ}, Φ_{κκ′}(ΔR,t), c̄_ΔR, z_ΔR |
| 7 | κ_m → 𝔨_m; κ₃^G, κ₃^X → 𝔨₃^{GS}, 𝔨₃^X (§0, §8) | §5, §6, §8 | done |
| 8 | n_κ(p) → 𝔫_κ(p); K_q̂ → E^kin_q̂ (§8) | (5.1), (5.3), §6 | done; 𝔨₂ = 2q²E^kin_q̂/M_κ |
| 9 | μ_κ → w_κ; ρ_κ(ω′\|…) → ρ^ph_κ (§8) | (3.1)–(3.6) | done |
| 10 | Σ_ν → Π^ph_ν; A_ν → A^ph_ν (§8, NOTATION C) | (6.2) | done |
| 11 | J_κ (spin q.n.) → 𝒥_κ; c_κ (abundance) → x_κ; g_κ → h^I_κ; σ_ℓκ → o_{Rκ} (§8) | (7.1) | done; F^Σ_κ kept separate as in WP0-v2 (2.2) |
| 12 | s_i → s^ph_i (§8) | (2.2) | done |
| 13 | Q_κ → 𝒬_κ; Δ_κ → δρ_κ (§0, §8) | (1.2), (4.5), §10 | done; δρ^val_κ, f^core_κ introduced for the add-on |
| 14 | D_A, D_NA → D^dyn_A, D^dyn_NA; λ (NA modes) → ν (§8, NOTATION C) | (4.2) | done; analytic modes ν′, e^A_{ν′} |
| 15 | ω_L (Larmor) → ω_Lar (§8) | (7.1) | done; ω_L stays the LO frequency |
| 16 | g(q,ω;x) → 𝒢 (§8) | (8.1) | 𝒢(q,ω;x) |
| 17 | Q_χ → e_χ (§8) | (4.2), (4.3) | done |
| 18 | f_κ(q) ≡ c_κ (§8; NOTATION c_s) | (1.1)–(7.2) | coupling vector with WP0-v2 sign, O_c = Σ_sc_sn_s (v1 "−c_e n_e" removed) |
| 19 | Δ (Doppler) → σ_ω (§0, §8) | (5.3), L6 | done |
| 20 | K₃, K₄ → 𝒞₃, 𝒞₄ (§8) | (6.2), G13 | done |
| 21 | a_{Qν} → b_{Qν}, B_{Qν} (§0) | (2.1) | done |
| 22 | λ₃, λ₄ → λ^anh_3, λ^anh_4; τ_ph → t_ph; Φ⁽ⁿ⁾ → Φ^{(n)} (NOTATION C, E) | §2, §6, L18 | done |
| 23 | Labels C1–C9, D1–D4 → WP2-… (§8; CONVENTIONS §14) | throughout | WP2-D1…D4, WP2-C1 (defects); checks WP2v2-C1…C13 |
| 24 | WP0 citations → WP0-v2 equation numbers (brief) | throughout | (3.3), (3.4), (4.6), (4.7), (5.3), (5.4), (6.1), (7.3), (8.2), (9.1), (9.7) |
| 25 | Phase convention u_{Rκ} ∝ e^{iQ·R} (CONVENTIONS §5); coordinator relay of the WP4-v2 interface flag (one-phonon phase e^{iq·r_κ}, not e^{iG·r_κ}) | (2.1), (2.2), (7.2), (1.3), IF-9 | stated explicitly; intra-cell factor e^{iq·r_κ} at every n_ph; v1's e^{iG·r_κ} = x⁰-phase eigenvectors, same \|…\|²; WP2v2-C13 |
| 26 | v_max = 794.5 km/s, rates per unit mass, 𝒢 → η/(2q) under hypothesis (I) (CONVENTIONS §8; WP0-v2 (9.1), WP6-W5) | §9 L5, L6; (5.3) | numbers recomputed (WP2v2-C10); hypothesis (I) stated |
| 27 | K labels, τ points (CONVENTIONS §11; WP0-v2 §6.1, (9.7)) | §9 | τ per LIMITS entry; x_coh retired |
| 28 | Nuisances by WP6 types, f-sum vacuous for conserving truncations (WP0-v2 (8.1)–(8.2); WP6-W2, W3) | (3.4), (6.1), (6.1′) | phonon cut → A or removed; (6.1b) = W3 vacuity; M-type compatibility derived |
| 29 | Static-DFPT error O(ω_Q²/E_g²) (F11) | L4 validity | stated; v1 value unchanged |
| 30 | GS f-sum vs Migdal drag mass (WP0-v2 §6.2 (iii), double-counting rule (a); WP3 J3) | (3.4), G3, IF-2 | E^{Mig}_1 subtraction stated |
| 31 | "DW" only = FC e^{−2W}; AH tadpole not DW (CONVENTIONS §10) | §3 | stated |
| 32 | Self-found: f-sum fraction at T = 0 only → any T, coherent included | (3.4′) | derived; WP2v2-C3b,c |
| 33 | Self-found: numbers (x_R = 1 momenta, IA onset, endpoint masses, toy 𝔨₃ 7%) | §0, (6.3), L5, L6 | recomputed, WP2v2-C10 |
| 34 | Self-found: 1807.10291 equation for the isotropic one-branch |ℳ|² is Eq. (32) (v1 "Eq. (31)") | (4.3), L4 | corrected from the full text |
| 35 | Checks script sympy-only (brief) | code/WP2-v2/checks.py | numpy diagonalisations (v1 C2, C5, C6, C9) replaced by exact certificates |
| 36 | Source-formula quotes per LIMITS entry (brief) | §9 | quoted from the full-text HTML |
| 37 | IF-8 closed: WP3-v2 writes S^{GS}_κκ (coordinator audit A13) | §15 IF-8 | flag marked CLOSED |
| 38 | NOTATION v4 renames (CORRECTIONS §17) | (6.1′), §17 | a_A → a^A_{n_A}; y → y_R owed at "(5.1′)" but no y (= ω − E_R) occurs in this return (no (5.1′) here; that label is WP6-v2's); §17 updated to v4. Notational only |

**Count:** 37 corrections applied (32 owed or brief-mandated, 5 self-found/format); **0 contested**; interface flags IF-1…IF-9. Row 38 (NOTATION v4 renames) is notational and outside this count.

---
## 17. Symbols introduced/used
All symbols follow NOTATION v4 and CONVENTIONS; **no deviations** (v4 renames: CORRECTIONS §17, §16b row 38). One NOTATION row-text conflict
is flagged, not deviated from: δρ_κ is used as in (1.2) and the v4 row "δρ^val_κ … valence part of δρ_κ" (IF-11).
**New in v3 (flagged):** **ΔR_{κκ′} ≡ ΔR + r_κ − r_κ′** (pair separation; shells indexed by (ΔR, κ, κ′); z, c̄ carry it as subscript);
**a_{1s,κ}** (1s orbital radius a₀/Z_eff of species κ; Si 1/a_{1s} = 51.1 keV); **Δ𝓃_κ(q)** (finite-q traceless density factor of the eκ third
moment, (5.2″)); **𝔯_κ(q), ξ_κ ≡ q a_{1s,κ}/2** (hydrogenic ratio and its argument, (5.2″)); **𝓜³_κκ|^{self}_pot** (self potential part of 𝓜³_κκ,
replacing v2's "𝓜³_κκ|_{V_eN}"); **a^{Mig}_n, ΔE_n** (Migdal amplitude of (5.2) and E^ad_n − E^ad_0, in (3.4)); j₂, P₂ (spherical Bessel, Legendre;
standard); **n_κ^{cell}** (number of equivalent κ sites per cell, (6.1), R9); WP6-v3's n_κ ≡ (2π/Ω)|c_κ|² is cited only in (6.1′). Used as defined in NOTATION v4: a_lat, a₀, P_Mig, j_BZ, q_BZ, G_min, 𝓃_e (mean electron density), 𝓃_e(R_κ). Used as defined there: q, ω, ω_q, v, v_χ, v_min, v_max, v_E(t), v_E^ref,
P_T, 𝒪₁, c₁^{(p)}, c₁^{(n)} (c_i^{(s)} with s = p, n), 𝒱, 𝔇, σ̄_e, σ_N, σ_p, μ_N, μ_p, μ_χe, F_DM, e_χ, ρ_χ, ρ_T, f_χ, η, 𝒢, f̂^{(0)}, m_χ, ℛ, Γ_χ;
s ∈ {e, κ}, c_s (c_κ, c_e), z_s, n_s(q), 𝓃_s, 𝓃_e, O_a, O_c, O_z, I_κ^β, j_κ^α, J_κ^{αβ}, 𝐈_I, 𝒥_κ, h^I_κ, F^M_κ, F^Σ_κ, j_T, j_L, ê_⊥ (unit vector ⊥ q);
S, S_ab, S^{GS}, S^X, S_inc, S_coh, S_self, S_IA, S^FR, S^{(n_ph)}, S_ℓm, S̄, R, R̃, ε, ε_∞, ε₀, ε_mac, v_C, L, 𝓜¹, 𝓜³; GS, X, X0, X+, Φ₀, Φ_n,
κ_BO, H_C, p_i, E_i, E_f, 𝒵 (partition function only where written), 𝓃_e(R_κ), U_κ, δM_κ, E^{Mig}_1, P_Mig, WP3 (W.5);
Q, ν, ω_{Qν}, e_{κν}(Q), b_{Qν}, B_{Qν}, n_{Qν}, n_B, N, Ω, V, R (lattice translation; inside ρ̄_e(q;R), Φ₀(r;R) the configuration, as in NOTATION),
ΔR, r_κ, x⁰_{Rκ}, u_{Rκ}, u_I, R_I, P_I, κ, M_κ, M_cell, A_κ, Z_κ, Z*_κ, 𝒬_κ, δρ_κ, 𝒵_κ, ρ̄_e, f^at_κ, ε_∞, ω_L, ω_T, ω_Lar, D^dyn_A, D^dyn_NA,
p(q̂)_{κα}, B_κ, W, 2W_κ, S_HR, D_κ, D_κ^{q̂}, D_κ^{αβ}, w_κ, ρ^ph_κ, Φ_{κκ′}(ΔR,t), Φ^{(n)}, c̄_ΔR, z_ΔR, j_BZ, n_ph, s^ph_i, 𝔨_m, 𝔨₃^{GS}, 𝔨₃^X, 𝒞_m,
𝔫_κ(p), E^kin_q̂, x_R, x_coh (retired), λ^anh_3, λ^anh_4, η_anh, A^ph_ν, Π^ph_ν, ω₀, ω̄, ⟨ω^{-1}⟩, x_κ, P_κ, o_{Rκ}, E_R, σ_ω, t_ph, j₀, Y_ℓm, P_ℓ, ℓ,
x = q̂·v̂_E; τ, 𝒳, K, n_B, n_g, n_A, n_T, Δ^τ_k, r^M_k, θ_k; E_g, ω_Q in (ω_Q/E_g)²; labels per CONVENTIONS §14.
Introduced here (new objects, no collision; NOTATION v4 §M rows, requested as IF-5/IF-6): **V_pot, V_ee, V_eN, V_NN** (potential energy and its parts; V alone
stays the volume); **E^ad_n(R)** (adiabatic electronic energies; E^ad_0 = BO surface); **∂_q̂ ≡ q̂·∇_{R_I}**; **q_BZ ≡ 2π/a_lat, G_min**; **ε_∞(q̂) ≡ q̂·ε_∞·q̂**;
**ν′, e^A_{ν′}** (analytic TO modes of D^dyn_A); **e^{s}_κν** (e^{+} ≡ e*, e^{−} ≡ e); **c̄_κ** (mean random coupling in (7.1)); **S̃_self,κ** (normalised self
term); **f^core_κ, δρ^val_κ** (core form factor, valence density response, §10); **P_ph(n_ph|q,ω)** (phonon-number distribution); **ΔE₃** (ω³-weighted
mean excitation energy, (5.2′)); **Δ^τ_A** (= Δ^τ_k at k = n_A); **a^A_{n_A}, θ_A** (type-A coefficient, anharmonic nuisance; v3 name a_A). Source-only notation appears
only inside quotes (§9: R, f̄_d, m_d, Ω_c, Δ_d, W_d, ℱ_med, g(q,ω), Y_j, ε*_{ν,k,j}, C_F, ℳ, e′, T_ℓm), per NOTATION §K.
