# R6 / WP2-v2: lattice sector of the URF, corrected standalone version

Revision agent, brief R6/REV-WP2. Supersedes returns/R5/WP2.md (v1), which stays as the historical record. Applies every owed item of
state/CORRECTIONS.md §0 and §8, the WP0-v2 interface flags F4, F6, F11 (and the consistency notes F3, F7), and the WP2 items recorded in SOTA.
Conventions: CONVENTIONS.md; symbols: NOTATION v4. WP0 equations are cited from returns/R6/WP0-v2.md as "WP0-v2 (x.y)".
Checks: `code/WP2-v2/checks.py` (sympy only, exact arithmetic for every identity; 21 checks, all PASS, ≈ 40 s); cited as WP2v2-Cn.
Tags: **[D]** derived (hypotheses stated), **[D, sketch]**, **[E]** estimated, **[C]** conjectured; literature **[FT]** full text (arXiv HTML in
`literature/papers-WP2/`, re-read for the quotes of §9), **[ABS]** abstract. Labels from other returns carry their prefix (CONVENTIONS §14).
Status: CLAIMED (SOTA R5 WP2), pending R×2. **Equation numbers are v1's** (WP0-v2 and SOTA cite WP2 (2.2), (2.3)–(2.4), (3.6), (4.2), (4.4),
(5.2)); new objects are primed: (3.4′), (5.2′), (6.1′).

---
## 0. Results in one page, and what changed

1. **Reduction [D]:** the lattice sector is the GS sector of WP0-v2 Theorem D (6.1), with n_e → ρ̄_e(q;R) (§1).
2. **Exact harmonic S at all phonon orders, coherent, finite T [D]** (2.2), in the CONVENTIONS §5 phase convention; exact shell expansion
   (2.3) whose ΔR = 0 term is the incoherent approximation; BZ-average theorem (2.4): "incoherent" = BZ-averaged coherent S.
3. **2607.24933 Eq. (47) (3D) is incomplete:** polarisation weights |q̂·e|² and intra-cell phases differ, not only momentum conservation (§3).
4. **Truncating at n_ph ≤ N loses P[Pois(2W_κ) ≥ N] of the f-sum (3.4′), at any T and for the coherent S too** (v2: v1 stated T = 0). The
   exact Panjer equation (3.5) gives S at all orders, with the final-state phonon spectrum ρ^ph_κ for WP5 (3.6).
5. **L4 [D]:** WP0-v2 (5.4) with the total ε ≡ the Born-charge one-phonon formula with Z*/ε_∞ and LO eigenvectors (Sherman–Morrison (4.2));
   reproduces 1910.08092 Eq. (106) and 1807.10291 Eqs. (29)–(32). 1712.06598 Eq. (5) carries a spurious 1/V_cell.
6. **L6 [D]:** exact anharmonic cumulants (5.1); the mean recoil is exact. 𝔨₃ splits into GS (BO curvature) + X (Migdal) (5.2).
   **New (F4): (5.2′)** for point nuclei on cubic sites 𝔨₃ = (q²/2M_κ²)Z_κe²𝓃_e(R_κ)/3, so the Migdal ω³ moment is fixed by the contact
   density, and the κκ contact moment is exactly −(m_e/M_κ) × the WP0-v2 (4.7) mixed moment. The free limit gives hep-ph/0608035 Eq. (5).
7. **L18/G13 [D]:** three exact linear constraints on the anharmonic increment (6.1); with WP6's M-type nuisance they hold only at θ ∈ {0,1}
   (6.1′). Structure at O(η_anh²) (6.2); negligible in the impulse regime, O((λ^anh)²(ω̄/E_R)^{1/2}).
8. **Nuclear spin [D]:** unpolarised spins give an exactly incoherent channel (7.1) (dropped by PhonoDark 2009.13534, present in 2506.11191);
   polarisation adds a coherent term ∝ P_κ². Transverse nuclear currents excite TA/TO (7.2).
9. **L19/G11 [D]:** harmonic rate formula (8.1). **Cubic isotropy theorem:** the harmonic incoherent S has no anisotropy in Si/Ge/GaAs at any
   n_ph or T (8.2), which explains 2411.03433.
10. **WP0 defects** WP2-D1–D4, WP2-C1 (§11): all applied in WP0-v2 (its closing table #8, #10, #32); nothing further owed by WP0.

**v1 → v2 changes.** NOTATION v3 renames throughout (CORRECTIONS §0, §8; list in §16); GS sector names; coupling vector c_s with the WP0-v2
sign (O_c = Σ_s c_sn_s, no "−c_e"); phonon phases in the CONVENTIONS §5 form (intra-cell factor e^{iq·r_κ}, WP2v2-C13); f-sum fractions at
any T and for the coherent S (3.4′); drag-mass caveat on the GS f-sum (3.4); F4 comparison (5.2′); nuisance-type compatibility (6.1′);
K labels and τ points per LIMITS entry; source-formula quotes in §9; numbers recomputed (WP2v2-C10; v_max = 794.5 km/s): x_R = 1 at 45.8/55.8
keV (v1 47/58), impulse onset 91.5/112 keV (v1 94/116), endpoint masses 17.3/21.1 MeV (v1 "20–40"), toy 𝔨₃ 7% low (v1 6%); the ρ_χ flag is
withdrawn (resolved, CONVENTIONS §8); checks rewritten in sympy only.

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
- q → 0: 𝒵_κ → q·Z*_κ, the Born charge (1910.08092 Eqs. (98)–(104), which (1.2) reproduces);
- leading correction to the rigid ion: the valence deformation δρ_κ − q f^at_κ, computable by DFPT (§10).

**(1.3) Conventions in the literature (factor to WP0-v2 (3.1)) [FT].**

| Source | Definition of S | Factor to WP0-v2 S |
|---|---|---|
| 2205.02250 Eq. (4); 2411.03433 Eq. (1); 2309.10839 Eq. (2); 2607.24933 Eq. (4); 1910.08092 Eq. (90) | (2π/V)Σ\|⟨f\|Σc e^{iq·r}\|0⟩\|²δ | 1 (T = 0) |
| 1911.03482 Eq. (2) | (1/N)Σ\|…\|²δ | ×2π/Ω |
| 1712.06598 Eq. (10) | neutron convention; rate via (4π/V_cell) in Eq. (9) | ×2π/Ω |
| 2506.11191 Eq. (69) | (1/N)Σλ²C, C lacking 1/V (their footnote 6) | ×1/Ω (C has the 2π) |

All sources are at T = 0; WP0-v2 (3.1) is Gibbs-averaged and the T > 0 forms below carry Bose factors. Sources using the eigenvector phase
e^{iQ·x⁰} (1910.08092 Eq. (90): e^{iG·x⁰_j}) map to CONVENTIONS §5 by e_κν(Q) → e_κν(Q)e^{−iQ·r_κ} (WP2v2-C13).

---
## 2. Harmonic S_κκ′ at all phonon orders (coherent, finite T)

**Exact form [D].** Hypotheses: H3 at n_A = 0 (harmonic BO surface), Gibbs state, operator (1.1) with the vertex of (1.2) absorbed into c_κ
(exact for the rigid ion; for the full 𝒵_κ at one-phonon order). With u_{Rκ} = Σ_{Qν}(2NM_κω_{Qν})^{-1/2}e_{κν}(Q)e^{iQ·R}B_{Qν} (CONVENTIONS §5)
and Bloch's identity (exact for Gaussian states), S = V^{-1}∫dt e^{iωt}⟨O_c†(t)O_c(0)⟩ gives

  S(q,ω) = (1/V)∫dt e^{iωt} Σ_{Rκ,R′κ′} c_κ* c_κ′ e^{−iq·(x⁰_{Rκ}−x⁰_{R′κ′})} e^{−W_κ−W_κ′} exp Φ_{κκ′}(ΔR,t),   ΔR = R − R′,                     (2.1)

  Φ_{κκ′}(ΔR,t) = Σ_{Qν} [(n_{Qν}+1)(q·e_{κν}(Q))(q·e_{κ′ν}(Q))* e^{iQ·ΔR − iω_{Qν}t} + n_{Qν}(q·e_{κν}(Q))*(q·e_{κ′ν}(Q)) e^{−iQ·ΔR + iω_{Qν}t}]/(2Nω_{Qν}√(M_κM_κ′)),

with 2W_κ(q) = q·B_κ·q, B_κ = ⟨u_κu_κ⟩ = Σ_{Qν}e_{κν}e_{κν}†(2n_{Qν}+1)/(2NM_κω_{Qν}). Expanding exp Φ gives the **n_ph-phonon coherent term**

  S^{(n_ph)}(q,ω) = (2π/Ω)(1/n_ph!) Σ_{{ν_i,s^ph_i}} ∫Π_i[Ω d³Q_i/(2π)³ · (n_{Q_iν_i} + (1+s^ph_i)/2)/(2ω_{Q_iν_i})] δ(ω − Σ_i s^ph_iω_{Q_iν_i})
             × (2π)³/Ω Σ_G δ³(q − Σ_i s^ph_iQ_i − G) |Σ_κ c_κ e^{−W_κ} e^{iq·r_κ} M_κ^{−n_ph/2} Π_i (q·e^{s^ph_i}_{κν_i}(Q_i))|²,   e^{+} ≡ e*, e^{−} ≡ e.   (2.2)

s^ph_i = +1 (−1): emission (absorption) of phonon (Q_i, ν_i); emission carries e* and n + 1 (CONVENTIONS §5). **Phase convention (explicit):**
eigenvectors e_{κν}(Q) carry the cell phase e^{iQ·R} only (CONVENTIONS §5), so the one-phonon (and every n_ph) intra-cell factor is e^{iq·r_κ}
with q unreduced, as in WP4-v2 (v1's e^{iG·r_κ} belongs to the x⁰-phase eigenvectors; same |…|², WP2v2-C13). Checks: n_ph = 1, T = 0 reproduces 1910.08092
Eq. (90) (π/Ω = (2π/Ω)/2) and 1911.03482 Eq. (8) (×2π/Ω, without DW); n_ph = 2, T = 0, G = 0, long-wavelength isotropic limit gives the
"contact" term 1911.03482 Eqs. (12), (16); n_ph = 0 is the Bragg term ∝ δ(ω)Σ_Gδ³(q − G), of zero measure for DM.

**Shell expansion [D].** Group (2.1) by lattice separation ΔR and basis pair (κ,κ′):

  S = S_inc + ΔS_coh,   S_inc = (1/Ω)Σ_κ|c_κ|²e^{−2W_κ}∫dt e^{iωt}[e^{Φ_{κκ}(0,t)} − 1],
  ΔS_coh = (1/Ω)Σ_{(ΔR,κ,κ′)≠(0,κ,κ)} c_κ*c_κ′ e^{−iq·(ΔR+r_κ−r_κ′)} e^{−W_κ−W_κ′}∫dt e^{iωt}[e^{Φ_{κκ′}(ΔR,t)} − 1].                               (2.3)

At order n_ph each shell term is ∝ Φ_{κκ′}(ΔR,t)^{n_ph}; by Cauchy–Schwarz |Φ_{κκ′}(ΔR,t)| ≤ [Φ_{κκ}(0,0)Φ_{κ′κ′}(0,0)]^{1/2}.
- n_ph = 1: the ΔR sum must be done in full (it produces the dispersion δ); no truncation in ΔR is allowed.
- n_ph ≥ 2 at T = 0: absolutely convergent (acoustic Φ(ΔR) ~ ΔR^{-2}, Φ² ~ ΔR^{-4}).
- T > 0: the classical acoustic correlation Φ ~ T/ΔR makes the n_ph = 2 shell sum only conditionally convergent (quasi-elastic absorption of a
  thermal phonon); irrelevant at mK (t_ph ≈ 10⁻³), flagged (§12 gap 3).
The **shell parameter** z_ΔR|j₀(qΔR)|c̄_ΔR^{n_ph} (rate-level size, below) is the coherence control that replaces x_coh (WP0-v2 Table 6.1).

**BZ-average theorem [D].** With j_BZ(r) ≡ (Ω/(2π)³)∫_BZ d³p e^{ip·r}, for every n_ph

  (Ω/(2π)³)∫_BZ d³p S^{(n_ph)}(q+p,ω) = S^{(n_ph)}_inc(q,ω) + Σ_{κ≠κ′} j_BZ(r_κ−r_κ′) S^{(n_ph)}_{κκ′,ΔR=0}(q,ω) + O(q_BZ ∂_q ln[W_κ, |q̂·e|²]).      (2.4)

Proof: insert (2.3) and hold the smooth factors at q; ∫_BZ e^{ip·ΔR} = 0 for ΔR ≠ 0 removes every shell term except the intra-cell cross terms.
**The incoherent approximation is the BZ average of the coherent S, up to intra-cell cross terms and gradient corrections.** WP2v2-C9 verifies
the identity exactly (1D chain, symbolic weights).

---
## 3. Multiphonon: incoherent approximation, Poisson tail, Franck–Condon

**(3.1)–(3.2) Incoherent harmonic S at finite T [D].** From (2.3), with the projected DOS D_κ^{q̂}(ω) = N^{-1}Σ_{Qν}|q̂·e_{κν}(Q)|²δ(ω − ω_{Qν})
(2411.03433 Eq. (18)), define the one-phonon measure

  w_κ(q;ω′) = (q²/2M_κ) D_κ^{q̂}(|ω′|)/ω′ · [n_B(ω′) + 1]   (ω′ < 0: absorption, weight n_B(|ω′|)/|ω′| ≥ 0 since n_B(−x) + 1 = −n_B(x)),   ∫dω′ w_κ = 2W_κ.   (3.1)

  S_inc(q,ω) = (2π/Ω) Σ_κ |c_κ|² e^{−2W_κ(q)} Σ_{n_ph≥1} w_κ^{*n_ph}(q;ω)/n_ph!   (* = convolution in ω).                                (3.2)

At T = 0 with isotropic D^{q̂} = D_κ this is 2205.02250 Eq. (36) and 2411.03433 Eq. (12); with the full D^{q̂} it is 2411.03433 Eq. (24). For an
Einstein solid at T = 0, (3.2) is the Poisson law of 2011.09477 Eq. (10), |f(n,q)|² = (q/q₀)^{2n}e^{−q²/q₀²}/n!, q₀² = 2Mω₀ (source notation).

**Franck–Condon (CONVENTIONS §10).** "DW" means only the e^{−2W} weight of the zero-phonon (Bragg) term, locally the overlap
|⟨0|e^{iq·u}|0⟩|² = e^{−2W}; the lattice Huang–Rhys factor is S_HR = 2W_κ. Replacing w_κ by the Huang–Rhys spectral function of the e–ph coupling
change gives the same compound-Poisson ZPL line shape in WP3 (pointer only; the AH tadpole is not DW).

**(3.3) Coherent–incoherent crossover and 2607.24933 [FT, D].** For the 1D monatomic chain, 2607.24933 Eq. (44) states that coherent and
incoherent S^{(n)} differ only by the momentum δ; (2.2) confirms it. Their 3D generalisation, Eq. (47), keeps the isotropic weight
𝒟(ω,k) = (Ω_c/3(2π)³)Σ_αδ(ω−ω_{αk}) inside the coherent sum: not correct. The exact replacement is (2.2), with per-phonon weights
|q̂·e(Q_iν_i)|² and, for a polyatomic basis, the intra-cell phases. Example: n_ph = 1, q ≪ q_BZ: Eq. (47) gives LA weight 1/3 plus two spurious TA
δ's; the exact result is LA with weight 1 and no TA. The physical conclusion (incoherent is accurate for n_ph ≥ 2 in ω-integrated rates)
survives through (2.4). Pointwise the correction is O(1) at the edges of the n_ph-phonon bands, where only near-Γ modes contribute and coherence
forces q ≈ G (their Figs. 8–10). Rate-level size after angular averaging and ω-bins wider than ω_max: |ΔS_coh/S_inc|_{n_ph} ≈
Σ_shells z_ΔR|j₀(qΔR)|c̄_ΔR^{n_ph}, c̄_ΔR = ⟨u₀·u_ΔR⟩/⟨u²⟩. Si: c̄₁ ≈ 0.2–0.4; at q = 10 keV, |ΔR| = 2.35 Å, z = 4: ≈ 2% for n_ph = 2 [E] (WP2v2-C10).

**(3.4) Sum rules (consistency with WP0-v2 (4.6)) [D].**
- Zeroth moment: ∫(dω/2π)S_self = 𝓃_κ|c_κ|².
- First moment: ∫ω′w_κ dω′ = (q²/2M_κ)∫D_κ^{q̂}[(n_B+1) − n_B] = q²/2M_κ at any T, so the **f-sum WP0-v2 (4.6b) holds exactly** in the harmonic
  BO model. Since ∫ω w^{*n} = n(∫ωw)(∫w)^{n−1} (WP2v2-C3b, with absorption lines and detailed balance),

  ∫ω S^{(n_ph)}_inc / ∫ω S = e^{−2W_κ}(2W_κ)^{n_ph−1}/(n_ph−1)!,   so truncation at n_ph ≤ N misses P[Pois(2W_κ) ≥ N] of the f-sum,        (3.4′)

  **at any T** (2W_κ then includes coth(βω/2)). The coherent shell terms do not change it: ∂_tΦ_{κκ′}(ΔR,0) = −i(q²/2M_κ)δ_{κκ′}δ_{ΔR,0} by the
  completeness Σ_νe_{κν}e_{κ′ν}† = δ_{κκ′}𝟙, so every ΔR ≠ 0 or κ ≠ κ′ term has zero first moment at each n_ph (v1 stated (3.4′) at T = 0, incoherent).
- One-phonon **without** e^{−2W} saturates the f-sum exactly, coherent and with Umklapp (Placzek's rule, completeness). "One-phonon with e^{−2W}"
  (1910.08092 Eq. (94)) carries only e^{−2W} of it; the multiphonons supply the rest.
- Cross-species and inter-site first moments vanish (WP0-v2 (4.6c)): intra-cell interference changes no f-sum.
- **GS vs X (WP0-v2 §6.2 (iii); WP3 J3):** the true GS sector carries q²/2M_κ − E^{Mig}_1(q), E^{Mig}_1 = q·δM_κ·q/(2M_κ²), the rest is Migdal (X).
  A harmonic S^{GS} built with bare M_κ and normalised to the bare f-sum overcounts by E^{Mig}_1 (δM/M ≤ 2.7×10⁻⁴ Si [E, WP3]); never add Migdal
  on top without that subtraction (WP0-v2 double-counting rule (a)).
- **Nuisance type:** a phonon-order cut is a non-conserving, support-removing truncation, so the f-sum is informative for it (WP0-v2 (8.2)); since
  (3.5) removes the cut at negligible cost, no nuisance is needed. If a cut is kept, the WP6 type is A with Δ^τ fixed by (3.4′).

**(3.5) Compound-Poisson integral equation [D]** (from ∂_te^Φ = Φ̇e^Φ; WP2v2-C4):

  ω S_κ(q,ω) = ∫dω′ ω′ w_κ(q;ω′) S_κ(q, ω−ω′),   S_κ ≡ e^{−2W_κ}Σ_{n_ph≥0} w_κ^{*n_ph}/n_ph!,                                                  (3.5)

at any T. On an ω grid it gives the all-order S with no phonon-number truncation, cost O(N_ω²) per q or O(N_ω log N_ω) with an FFT of
e^{Φ(t)}; it supersedes the n ≤ 10–20 truncations of 2205.02250 and 2411.03433. 2411.03433 Eq. (26) is the order-by-order version.

**(3.6) Final-state phonon spectrum (WP5 hand-over, WP0-v2 (7.3)) [D].** Mean number of created phonons per dω′ at given (q,ω):

  ρ^ph_κ(ω′|q,ω) = w_κ(q;ω′) S_κ(q,ω−ω′)/S_κ(q,ω),   ∫ω′ρ^ph_κ dω′ = ω (by (3.5)),   ∫ρ^ph_κ dω′ = ⟨n_ph⟩,                                     (3.6)

ω′ < 0 entries are absorbed thermal phonons. Replacing w_κ by the branch-projected w_{κν} gives the branch content (LA/TA/LO/TO) needed for WP5
down-conversion. In the incoherent approximation the phonon momenta are uniform over the BZ, weighted by the DOS.

---
## 4. Polar couplings: dark photon, Born charges, ε_∞, LO–TO (L4)

**(4.1) Start [D].** WP0-v2 (5.4): S_zz(q,ω) = (2q²/e²)Im[−(ε^{-1})_{00}(q,ω)]/(1 − e^{−βω}) with the **total** ε; exact for total-charge coupling.

**(4.2) Adiabatic, harmonic, q → 0 [D]** (GS; ω ≪ E_g so the electronic ε is ε_∞; n_A = 0; q ≪ q_BZ). The total longitudinal ε is

  ε(q̂,ω) = ε_∞(q̂) + (e²/Ω) Σ_{ν′} [p(q̂)·e^A_{ν′}]²/(ω_{ν′}² − ω²),   ε_∞(q̂) ≡ q̂·ε_∞·q̂,   p(q̂)_{κα} ≡ (q̂·Z*_κ)_α/√M_κ,

ν′ running over the analytic (TO) eigenmodes e^A_{ν′} of D^dyn_A. Sherman–Morrison with D^dyn_NA = D^dyn_A + (e²/Ωε_∞(q̂))ppᵀ, whose eigenmodes ν
are the LO-split phonons, gives exactly (WP2v2-C2, exact rational 3-mode model)

  −1/ε = −1/ε_∞(q̂) + (e²/Ωε_∞(q̂)²) pᵀ(D^dyn_NA − ω²)^{-1}p  ⇒  S_zz = (2π/Ω) Σ_ν (1/2ω_{Qν}) |Σ_κ q·Z*_κ·e*_{κν}/(ε_∞(q̂)√M_κ)|² δ(ω − ω_{Qν}).  (4.2)

The ELF with the total ε is *identical* to the Born-charge one-phonon formula with vertex q·Z*/ε_∞ and NA eigenvectors: the "screen by ε_∞,
ions in the source" prescription of 1910.08092 (below Eq. (104)) equals WP0-v2's total-ε prescription; they are bookkeepings of one Dyson series.
With F_DM = (αm_e/q)², 𝒱 = e_χe²/q² and WP0-v2 (3.3) this reproduces 1910.08092 Eq. (106) and 1807.10291 Eq. (29).

**(4.3) One polar branch [D]** (WP2v2-C1). With ε = ε_∞(ω_L² − ω²)/(ω_T² − ω²) and LST:

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

**(5.1) Exact cumulants of the self structure factor [D]** (WP2v2-C5). Hypotheses: self part of S_κκ; any H whose potential V_pot (all Coulomb
potential energy, H_C minus kinetic terms) is local in the struck coordinate (WP0-v2 (L)); any anharmonicity; any T; TR (odd momentum moments
vanish). With ∂_q̂ ≡ q̂·∇_{R_I} and E^kin_q̂ ≡ ⟨(q̂·P_I)²⟩/2M_κ, the ω-cumulants of S_self/∫S_self are

  𝔨₁ = q²/2M_κ,  𝔨₂ = 2q²E^kin_q̂/M_κ,  𝔨₃ = (q²/2M_κ²)⟨∂_q̂²V_pot⟩,  𝔨₄ = (q²/M_κ²)⟨(∂_q̂V_pot)²⟩ + (q⁴/M_κ⁴)(⟨(q̂·P_I)⁴⟩ − 3⟨(q̂·P_I)²⟩²).   (5.1)

Derivation as 2309.10839 Eqs. (56)–(60), with ⟨p[H,p]⟩ = ½⟨∂²V⟩ from stationarity. WP2v2-C5 certifies k = 1–4 exactly for a cubic + quartic
oscillator with exact ground state e^{−W(x)} (the moment differences integrate to zero by an explicit polynomial Q, Q′ − 2W′Q = difference).
Harmonic case: (5.1) reproduces the cumulants of (3.2), ∫ω′^m w_κ dω′: 𝔨₂ = (q²/2M)∫D ω coth(βω/2)dω, 𝔨₃ = (q²/2M)∫Dω²dω, … **𝔨₁ is exact: the mean of
the impulse peak is never shifted.** The "shift of the peak" in 2205.02250 (below Eq. (38)) is a shift of the mode by 𝔨₃, not of the mean.

**(5.2) The GS/X split of 𝔨₃ [D at leading BO order, H2; Migdal amplitude of WP0-v2 §6.2 (ii)]** (WP2v2-C6). V_pot contains V_eN, and the
second-derivative identity ∂_q̂²E^ad_0 = ⟨Φ₀|∂_q̂²V_pot|Φ₀⟩ − 2Σ_n|⟨Φ_n|∂_q̂V_pot|Φ₀⟩|²/(E^ad_n − E^ad_0), with the Migdal amplitude
(q/M_κ)⟨Φ_n|∂_q̂V_pot|Φ₀⟩/(E^ad_n − E^ad_0)², gives

  𝔨₃ = 𝔨₃^{GS} + 𝔨₃^X,   𝔨₃^{GS} = (q²/2M_κ²)⟨∂_q̂²E^ad_0⟩_vib,   𝔨₃^X = (q²/M_κ²)Σ_n|⟨Φ_n|∂_q̂V_pot|Φ₀⟩|²/(E^ad_n − E^ad_0) = ω³-moment of S^X_κκ.      (5.2)

The same amplitudes give the X first moment (q²/M_κ²)Σ_n|…|²/(E^ad_n − E^ad_0)³ = q·δM_κ·q/(2M_κ²) = E^{Mig}_1, which is WP3 J3 (WP2v2-C6b).
Corrections: O(κ_BO⁴) and O(𝔨₁/ΔE₃) from measuring ω about 𝔨₁ instead of 0, ΔE₃ the ω³-weighted mean excitation energy. Consequences: the lattice
impulse approximation must use the **BO curvature**, not ⟨∇²V_pot⟩; the ω³ moment of S_κκ is dominated by X despite its O(κ_BO⁴) weight.

**(5.2′) Contact sum rule and the F4 comparison [D for point nuclei; cubic sites for the closed form] (new).** Write V_pot = V_ee + V_eN + V_NN,
V_eN = −Σ_{i,I}U_κ(r_i − R_I), U_κ(r) = Z_κe²/(4π|r|) for a point nucleus. (a) ∇²_R V_NN = 0 at a nuclear site (other nuclei are elsewhere) and
∇²_R(−U_κ) = +Z_κe²δ³(r_i − R_I) (WP2v2-C11b); (b) on a cubic site any rank-2 site tensor is ∝ 𝟙 (WP2v2-C11c), so ⟨∂_q̂²V_pot⟩ = ⟨∇²_RV_pot⟩/3
(the traceless part of ∂_α∂_β(1/r) averages to zero). Hence

  𝔨₃ = (q²/2M_κ²) Z_κe²𝓃_e(R_κ)/3,   𝔨₃^X = (q²/2M_κ²)[Z_κe²𝓃_e(R_κ)/3 − ⟨∂_q̂²E^ad_0⟩_vib],                                               (5.2′)

with 𝓃_e(R_κ) the electron contact density (WP0-v2 (4.7) notation). (c) **Link to WP0-v2 (4.7).** Newton's third law, (q·∇_R)²U_κ(r − R) =
(q·∇_r)²U_κ(r − R) (WP2v2-C11a), and the explicit double commutators (WP2v2-C11d: the e–N one is the multiplicative operator
e^{iq·(R−r)}(q·∇)²U_κ/(m_eM_κ), confirming (4.7); the κκ one has Hermitian potential part −(q·∇)²U_κ/M_κ²) give, at contact,

  𝓜³_κκ|_{V_eN} = −(m_e/M_κ) 𝓜³_eκ   (point nuclei),   i.e. 𝓜³_κκ|_{V_eN} = 𝓃_κq²Z_κe²𝓃_e(R_κ)/(3M_κ²) on cubic sites.

So WP2 (5.2) and WP0-v2 (4.7) are the κκ and eκ faces of one contact sum rule, and WP3 J3 is its first-moment companion; all three are mutually
consistent (F4 at the level of moments). Size [E] (WP2v2-C10): Si, hydrogenic 1s contact density only, 𝔨₃^X/𝔨₃^{GS} ≈ 8×10⁵; ΔE₃ is of the order
of the 1s binding (≈ 1.8 keV), so the O(𝔨₁/ΔE₃) correction is negligible for q ≪ √(2M_κΔE₃) ≈ 10 MeV. **Consequence for WP3:** the X ω³ moment is
UV (core, large-k) dominated; a valence-only or soft-limit (W.5) truncation (WP3 T3) cannot saturate (5.2′), so the test is meaningful only for
the all-electron, all-k (W.5) (Interface flag IF-1).

**(5.3) Chain to the free recoil [D].**
1. The IA is the saddle at t ≈ 0 (2205.02250 Eqs. (37)–(39)); to leading order in 1/q

     S_IA(q,ω) = (2π/Ω) Σ_κ |c_κ|² ∫d³p 𝔫_κ(p) δ(ω − q²/2M_κ − q·p/M_κ),                                                                  (5.3)

   with 𝔫_κ(p) the (anharmonic, T-dependent) nuclear momentum distribution. A Gaussian 𝔫_κ gives 2205.02250 Eq. (39) with width
   σ_ω² = 𝔨₂ = 4E_R E^kin_q̂ (source Δ_d → σ_ω), E_R = q²/2M_κ.
2. σ_ω/E_R ≈ (ω̄/E_R)^{1/2} → 0 gives S^FR = (2π/Ω)Σ_κ|c_κ|²δ(ω − q²/2M_κ) (2205.02250 Eq. (42)).
3. In WP0-v2 (3.4), with hypothesis (I) (S angle-averaged; 𝒢 → η(v_min)/(2q), WP0-v2 (9.1)) and |𝒱_p|² = πσ_p/μ_p², this gives
   dℛ/dE_R = ρ_χσ_N|F^M_κ(q)|²η(v_min)/(2m_χμ_N²), v_min = q/2μ_N: hep-ph/0608035 Eq. (5) (WP2v2-C8; per unit target mass, ρ_T = 𝓃_NM_N).
4. The Helm |F|² of hep-ph/0608035 Eq. (9) parametrises |F^M_κ|² (WP0-v2 (2.2)) under F_mass = F_charge (their Eqs. (7)–(8)), a 10–20%
   nuclear-structure systematic (their abstract).

---
## 6. Anharmonic expansion (L18, G13)

**(6.1) Exact constraints [D].** Let Δ^τ_A ≡ S_self^{(n_A=1)} − S_self^{harm} at fixed q (self part; the WP6 increment Δ^τ_k for k = n_A). From (5.1)
and the normalisation:

  ∫dω Δ^τ_A = 0,   ∫dω ω Δ^τ_A = 0,   ∫dω (ω − q²/2M_κ)² Δ^τ_A = 2q²δE^kin_q̂/M_κ,                                                        (6.1)

δE^kin_q̂ the anharmonic change of the kinetic energy, a static quantity that PIMD gives exactly. The middle identity is the WP6-W3 vacuity of the
f-sum for a conserving truncation (WP0-v2 (8.2)); the first and third are the informative constraints on θ_A.

**(6.1′) Compatibility with WP6 nuisance types [D] (new).** (6.1) is linear in Δ^τ_A. With the additive type A (S^τ + a^A_{n_A}Δ^τ_A) it holds for all
a^A_{n_A}. With the M type S^τ(1 + r^M_A)^{θ_A} it holds only at θ_A ∈ {0, 1}: a two-bin example with ∫Δ = 0 gives ∫S(θ) = (1 + a)^θ + (1 − a)^θ < 2 at
θ = ½ (WP2v2-C12). Recommendation: impose (6.1) on the computed Δ^τ_A (validation), and use M type with the constraint violation, O(θ(1−θ)(r^M)²),
recorded as a sub-percent systematic, or type A where S^τ is small (Interface flag IF-4).

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
  harmonic 𝔨₃ = (q²/2M)(3ω₀ω̄ − 2ω₀²) instead of (q²/2M)⟨ω²⟩: **7% low** in Si [E] (ω̄ ≈ 40, ω₀ ≈ 28, √⟨ω²⟩ ≈ 44 meV; WP2v2-C10; v1 said 6%).
- Missing physics: (i) the 3D angle-dependent single-site potential (their Eq. (23); the maximum-anharmonicity direction overestimates); (ii)
  intersite anharmonicity, i.e. the linewidths of (6.2a), which a single site cannot produce.
- **Normalisation discrepancy [FT]:** their Eq. (9) has e^{−W_d} with Eq. (10) W_d = (q²/4m_d)∫D/ω, i.e. W_d = W (half the FC exponent). This
  contradicts 2205.02250 Eq. (36) and their own Eq. (13), which have e^{−2W}: a typo at formula level; not checked whether it reached their numerics.

---
## 7. Nuclear-spin and nuclear-current couplings into phonons

**(7.1) Spin density [D].** Operator I_κ^β(q) = F^Σ_κh^I_κΣe^{iq·R_I}𝐈_I^β (WP0-v2 (2.2)). Hypotheses: (S1) spin–lattice couplings (hyperfine, nuclear
quadrupole) ≪ ω_ph (≲ μeV vs tens of meV); (S2) each spin-carrying isotope occupies sites at random with abundance x_κ (²⁹Si 4.7%, ⁷³Ge 7.8%),
occupancy o_{Rκ} ∈ {0,1}; (S3) spins uncorrelated between sites, polarisation P_κ along ẑ (paramagnet; order only at ≲ μK). Lattice and spin
traces factorise; the random coupling c_{Rκ} = F^Σ_κh^I_κ𝐈^β_{Rκ}o_{Rκ} makes the decomposition of 2205.02250 Eqs. (9)–(11) exact:

  S^{ββ}_{II}(q,ω) = S_coh[c̄_κ = x_κF^Σ_κh^I_κ⟨𝐈^β⟩] + (2π/Ω)Σ_κ x_κ(F^Σ_κh^I_κ)²[⟨(𝐈^β)²⟩ − x_κ⟨𝐈^β⟩²] S̃_self,κ(q,ω),   ⟨𝐈^z⟩ = P_κ𝒥_κ, ⟨𝐈^{x,y}⟩ = 0,   (7.1)

S̃_self the normalised self term of (3.2), convolved with the Larmor spectrum (ω_Lar/ω_ph ~ 10⁻⁶).
- **Unpolarised (P_κ = 0):** *exactly* incoherent, ⟨(𝐈^β)²⟩ = 𝒥_κ(𝒥_κ+1)/3; the one-phonon part scales as q²D^{q̂}(ω)/ω, no coherent LA δ, no
  q-linear enhancement at small q. This is 2506.11191 Eqs. (68)–(72), whose isotropic DOS is exact for cubic sites.
- 2009.13534 (text after its single-phonon rate) **drops** unordered-spin responses and so omits this nonzero channel.
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

**(8.2) Selection rules [D]** (WP2v2-C7).
- S(q,ω) = S(−q,ω) (TR or inversion) ⇒ ℓ even. (P- and T-broken targets: nonreciprocal S, odd ℓ allowed; WP0-v2 (4.3), L19 ✎ WP4-D6.)
- Cubic point groups have invariants only at ℓ = 0, 4, 6, 8, … (A₁ multiplicities of O: 1,0,0,0,1,0,1,0,1 for ℓ = 0…8).
- **Cubic isotropy theorem.** If every site has cubic site symmetry (T_d in Si, Ge, GaAs, diamond), every rank-2 site tensor is ∝ 𝟙:
  D_κ^{αβ}(ω) = δ_{αβ}D_κ(ω)/3, B_κ ∝ 𝟙. Then (3.1)–(3.2) depend on q̂ only through q̂·D_κ·q̂ = D_κ/3: **the harmonic incoherent S is exactly isotropic
  at every n_ph and T**, so its daily modulation vanishes identically. This explains why 2411.03433 (abstract) finds negligible modulation in Si and
  GaAs and 1–10% in Al₂O₃, where the site tensors are anisotropic and ℓ = 2 is allowed (and 2W_κ = q·B_κ·q is direction-dependent).
- **Residual anisotropy in cubic crystals:** (i) the coherent one-phonon term (full anisotropy; dominates for m_χ ≲ few MeV); (ii) coherent shell
  terms of (2.3) at n_ph ≥ 2 (ℓ ≥ 4, size from §3.3); (iii) in the IA, the rank-4 non-Gaussian ⟨(q̂·P)⁴⟩ − 3⟨(q̂·P)²⟩² of 𝔨₄ (5.1), O((λ^anh_4),
  (λ^anh_3)²), tiny; (iv) non-cubic crystals: the IA width tensor ⟨P_αP_β⟩, which 2411.03433 neglects ("isotropic approximation" with q̂ = ẑ): a
  small, systematically signed omission.
- **Pointer to WP3 [D, conditional on 2607.06005's soft-limit form].** 2607.06005 shows that the soft-limit Migdal rate depends only on the ℓ = 0, 2
  moments of the ELF; in a cubic crystal ℓ = 2 vanishes, so the soft-limit Migdal daily modulation in Si and GaAs is zero at that order (agrees with
  WP1's symmetry result). Any nonzero value is a k-mesh or symmetry-breaking artefact or a beyond-soft effect.

---
## 9. LIMITS entries (τ point per CONVENTIONS §11; source formulas quoted [FT] in source notation and units)

**L4. Single phonon; dark photon via Born charges.** τ: S^{GS}_κκ, S^{GS}_cc; `nB=0|ng=0|nA=0|X=-|nT=0|K=1ph-coh|Mg=-|nD=-` + `T=0;ref=normal;
scr=ext,DFPT,ion;conv=-` (𝒳 enters only through ε_∞, Z*, DFPT).
- *Source quotes* [FT]: 1910.08092 Eq. (92): "R = (1/m_cell)(ρ_χ/m_χ)(πσ̄/2μ²)∫d³q/(2π)³ ℱ_med²(q) Σ_ν (1/ω_{ν,k}) |Σ_j e^{−W_j(q)}m_j^{−1/2}
  e^{iG·x⁰_j}(Y_j·ε*_{ν,k,j})|² g(q,ω_{ν,k})"; Eq. (105): "Y_j = −q²(q·Z*_j)/(q·ε_∞·q)"; Eq. (106): the same with
  q⁴/(q·ε_∞·q)² and (q·Z*_j·ε*_{ν,k,j}). 1807.10291 Eq. (29): "ℳ_{q+G,ν} = iee′Σ_j (2Ωm_jω_{ν,q})^{−1/2}(q+G)·Z*_j·e*_{j,ν,q}/((q+G)·ε_∞·(q+G))";
  Eq. (32): "ℳ^iso_q = ie′[(ω_LO/2)(1/ε_∞ − 1/ε₀)]^{1/2}/|q|". 1712.06598 Eq. (5): "C_F = e[(ω_LO/2V_cell)(1/ε_∞ − 1/ε₀)]^{1/2}", Eq. (7):
  "|ℳ_q|² = (κ²g_X²/e²)C_F²/q²". Also 1911.03482 Eq. (8); 2009.13534 (single-phonon rate, general operators).
- *Chain:* WP0-v2 (3.3) → (1.1) GS at n_B = 0 → harmonic (2.2) at n_ph = 1, T = 0 → vertex c_κ (nucleon A_κF^M_κ, 1910.08092 Eq. (94); charge
  𝒵_κ → q·Z*_κ (1.2)) → dark photon: WP0-v2 (5.4) ≡ (4.2) → one branch (4.3). Map: ℱ_med ↔ F_DM, g(q,ω) ↔ 𝒢, m_j ↔ M_κ, ε* ↔ e* (x⁰ phase).
- *Validity (Si/Ge/GaAs):* q ≪ q_BZ (2.28/2.19/2.19 keV, q_BZ ≡ 2π/a) for the Z* vertex and analytic eigenvectors (the full (2.2) holds at all q
  with Umklapp); ω_LO ≪ E_g, adiabatic (static-DFPT) error O(ω_Q²/E_g²) (F11): GaAs (36 meV/1.5 eV)² ≈ 6×10⁻⁴; T ≪ ω; harmonic, η_anh ≈ 0.01–0.03.
- *Leading corrections:* finite-q charge vertex (valence deformation, dynamical quadrupoles (4.5)), O(qa) relative in polar crystals and leading
  in Si/Ge; FC e^{−2W}: 2W ≈ 6×10⁻⁴ at q = 1 keV in Si [E] (⟨u_x²⟩ ≈ 0.0025 Å²); anharmonic linewidth A^ph_ν (6.2a), O(10⁻³) for Si optical phonons
  [E]; dark photon in Si: two-phonon term from ∂Z*/∂u.
- *Discrepancies:* (a) 1712.06598 Eqs. (5), (7): C_F² ∝ 1/V_cell makes |ℳ|² dimensionally E² in the continuum golden rule of their Eq. (6); the
  consistent (4.3) = 1807.10291 Eq. (32) has no cell volume (V_cell must be the normalisation volume, which cancels). (b) 1712.06598 Eq. (12) uses
  equal-mass eigenvectors, leaving a spurious LO term ∝ (√A₁ − √A₂)²q²; the correct leading LO term is the q⁴a² term of 1911.03482 Eq. (44); for
  GaAs subdominant for q ≳ 0.1 keV [E]. Convention factors: table (1.3). **Status ✔** (WP0-v2 (9.7)).

**L5. Multiphonon incoherent approximation and Poisson tail.** τ: S^{GS}_κκ, `K=multi-inc`, n_A = 0, any n_T (Bose factors in (3.1)).
- *Source quotes* [FT]: 2205.02250 Eq. (36): "S(q,ω) ≈ (2π/Ω_c)Σ_d (f̄_d)² e^{−2W_d(q)} Σ_n (q²/2m_d)^n (1/n!) (Π_{i=1}^n ∫dω_i D_d(ω_i)/ω_i)
  δ(Σ_jω_j − ω)"; 2411.03433 Eq. (24): the same with D^{q̂}_d and f_d²-bar; 2011.09477 Eq. (10): "|f(n,q)|² = (1/n!)(q/q₀)^{2n}e^{−q²/q₀²}";
  2607.24933 Eqs. (44), (47) (quoted in §3.3).
- *Chain:* (1.1) → harmonic (2.1) → drop shell terms (2.3) (equivalently the BZ average (2.4) minus intra-cell terms) → isotropic projected DOS
  (exact for cubic sites, §8.2) → T → 0 → (3.2) → Einstein → Poisson. Map: d ↔ κ, f̄_d ↔ c_κ, m_d ↔ M_κ, Ω_c ↔ Ω.
- *Validity:* n_ph ≥ 2, or rates ω-integrated over ≳ ω_max (pointwise O(1) errors at band edges, §3.3); n_ph = 1 needs (2.2) at all q.
  x_R = q²/2M_κω̄ = 1 at q = 45.8 keV (Si) and 55.8 keV (Ge) (ω̄ ≈ 40, 23 meV [E]; WP2v2-C10). Multiphonon window q ≈ 10–100 keV, i.e. m_χ ≈ 1.9–19 MeV
  at the kinematic endpoint q = 2m_χv_max, v_max = 794.5 km/s.
- *Leading corrections:* coherent shell terms z_ΔR|j₀(qΔR)|c̄_ΔR^{n_ph} (≈ 2% at n_ph = 2 in Si, §3.3); anharmonic (6.2d); Bose factors (3.1),
  O(e^{−ω/T}); Migdal transfer E^{Mig}_1 of the f-sum (3.4). Truncation error fixed exactly by (3.4′), or removed by (3.5).
- *Discrepancies:* 2607.24933 Eq. (47) (§3.3); 1911.03482 per-cell convention (1.3). **Status ✎ (control):** x_coh replaced by n_ph and the shell
  parameter (WP2-D1, applied in WP0-v2 Table 6.1).

**L6. Free nuclear recoil, Helm.** τ: S^{GS}_κκ, `K=imp`, any n_A (cumulants exact), plus X remainder through (5.2).
- *Source quotes* [FT]: hep-ph/0608035 Eq. (5): "dR_i/dE = ρσ_i^{SI}|F(q)|²/(2mμ_i²) ∫_{v>q/2μ} f(v,t)/v d³v"; Eq. (9): "|F^{SI}(q)|² =
  (3j₁(qR₁)/(qR₁))² e^{−q²s²}"; 2205.02250 Eq. (39): "S^IA(q,ω) = Σ_d ((f̄_d)²/Ω_c)(2π/Δ_d²)^{1/2} exp(−(ω − q²/2m_d)²/(2Δ_d²))", Eq. (42):
  "S^FR(q,ω) = Σ_d (2π/Ω_c)(f̄_d)²δ(ω − q²/2m_d)". Map: dR_i/dE ↔ dℛ/dE_R, ∫f/v ↔ η(v_min), Δ_d ↔ σ_ω.
- *Chain:* (1.1) → self part → IA (5.3) → narrow width → WP0-v2 (3.4) with hypothesis (I) → WP2v2-C8.
- *Validity:* x_R ≫ 1 (q ≳ 2(2M_κω̄)^{1/2} = 91.5 keV Si, 112 keV Ge, i.e. m_χ ≳ 17.3 (Si), 21.1 (Ge) MeV at the kinematic endpoint
  q_max = 2m_χv_max; v1's "20–40 MeV" is withdrawn); threshold far from the endpoint in units of σ_ω = (q²ω̄/2M_κ)^{1/2}; no electronic excitation
  (X weight O(κ_BO⁴)); E_R above the displacement threshold changes the partition (WP5), not S.
- *Leading correction:* Gaussian smearing σ_ω² = 4E_RE^kin_q̂ with the true (zero-point plus anharmonic) kinetic energy; then the skewness 𝔨₃^{GS}
  (5.2), not ⟨∇²V_pot⟩ (whose value (5.2′) is X-dominated); the mean is exact. Near threshold this is the "Poisson tail" enhancement of 2011.09477.
- *Discrepancy:* 2205.02250's "true peak shifted" is the mode, not the mean (5.1). **Status ✎ (WP2-D4)**, applied in WP0-v2 (9.7).

**L18. Anharmonic NR corrections.** τ: S^{GS}_κκ, n_A = 1, K = multi-inc or imp.
- *Source quotes* [FT]: 2309.10839 Eq. (9): "S(q,ω) ≈ 2πΣ_d n_d|f_d|² e^{−W_d(q)} Σ_n (1/n!)(q²/2m_d)^n (Π_i∫dω_i D_d(ω_i)/ω_i) δ(Σ_jω_j − ω)";
  Eq. (10): "W_d(q) = (q²/4m_d)∫dω′ D_d(ω′)/ω′"; also Eqs. (23)–(26), (39), (52)–(62); 2412.18330 [ABS].
- *Chain:* (1.1) with n_A ≥ 1 → self part (q ≫ q_BZ) → single site (neighbours frozen: no intersite Φ^{(3)}, no linewidths) → 1D along the
  maximum-anharmonicity direction → perturbation theory in λ^anh_3, λ^anh_4, or the IA with the cumulants (5.1).
- *Validity:* λ^anh_3 ≈ 0.01, λ^anh_4 ≈ 10⁻⁴ (Si, 2309.10839); q > q_BZ; the 1D reduction overestimates.
- *Leading corrections:* exact constraints (6.1) (with (6.1′) for the nuisance type); linewidth and Fano terms (6.2a–b), absent from the single site;
  3D angular average of their f_k(θ,φ)².
- *Discrepancy:* e^{−W_d} vs e^{−2W_d} (§6.3). **Status ✔.**

**L19 (lattice part). Daily modulation.** τ: full q-vector S^{GS}_κκ; K = 1ph-coh at n_ph = 1, multi-inc with D^{q̂} at n_ph ≥ 2.
- *Source quotes* [FT]: 2411.03433 Eq. (24) (quoted under L5, with D^{q̂}_d(ω) of their Eq. (18)); 2607.06005 Eq. (10): "dR/dω ∼ ∫dq qF(q²)∫dω_q
  Σ_{ℓmm′} T_ℓm(q,ω_q,ω)ℛ^{(ℓ)}_{mm′}(t) f̂_{ℓm′}(s,v_lab)" (their T_ℓm ↔ S_ℓm, f̂ ↔ f̂^{(0)} of NOTATION F; "∼" is theirs).
- *Chain:* WP0-v2 (3.3) with the full q-vector S → (8.1); phonon S from (2.2) at n_ph = 1 and (3.2) with D^{q̂} at n_ph ≥ 2.
- *Validity:* (8.1) hypotheses; incoherent approximation for n_ph ≥ 2 as in L5. *Leading corrections:* cubic crystals §8.2 (i)–(iii); non-cubic (iv).
- *Discrepancy:* none in normalisation; the isotropic IA width of 2411.03433 is an omission. **Status ✎** (WP4-D6 converse, owned by WP0-v2/WP4).

---
## 10. Gaps assigned: closing formulas and computation specifications

**G3, lattice side: the multiphonon S_NN that WP5 needs.**
- *Formula:* (2.2) at n_ph = 1 (coherent); (3.2) via (3.5) for n_ph ≥ 2; (5.3) for the IA; final-state spectra (3.6) and branch content. For NR the
  MD seed is the struck atom with momentum p + q, p ~ 𝔫_κ(p) of (5.3), exact to leading order in 1/q; the energy partition (heat, defects, charge) is
  WP5's transport problem. GS normalisation: subtract E^{Mig}_1 if Migdal is seeded separately (3.4).
- *Computation:* (i) QE pw.x/ph.x (LDA/PBEsol; Si/Ge ecut 50–60 Ry, k 8³, DFPT q 8³) → phonopy Fourier interpolation onto 48³: D_κ^{αβ}(ω), B_κ,
  branch-projected DOS, tetrahedron resolution 0.1 meV. (ii) i-PI PIMD (P ≈ 32 beads at 10 K; 216-atom cell; MLIP or DFTB) for 𝔫_κ(p), E^kin_q̂,
  ⟨∂_q̂²E^ad_0⟩ and 𝔨₄, converged to < 1%. (iii) New module (≈ 300 lines): solve (3.5) per (q, q̂) on an ω grid (N_ω ≈ 10⁴, FFT); output S_κ(q,ω),
  P_ph(n_ph|q,ω), ρ^ph_κν(ω′|q,ω).
- *Cost:* DFPT ≈ 10² CPU·h; PIMD ≈ 10³ CPU·h with an MLIP; tables ≈ minutes.
- *Outputs:* HDF5 tables of S(q,q̂,ω) and ρ^ph(ω′|q,ω) for q ∈ [0.1, 300] keV, ω ∈ [0, 50] eV, with the IA-to-free switch at x_R > 16 and the
  Edgeworth 𝔨₃^{GS}, 𝔨₄ terms; library key τ per §9.

**G11 (lattice): anisotropy and modulation.**
- *Formula:* (8.1) with the S_ℓm of (2.2) and (3.2).
- *Computation:* n_ph = 1 from phonopy eigenvectors (48³ mesh, Umklapp to |q+G| = 30 keV), projected onto Y_ℓm (ℓ ≤ 12 cubic, ≤ 8 for Al₂O₃/SiC;
  Lebedev grid of 590 points); n_ph ≥ 2 from D^{αβ}_κ (2411.03433 Eq. (20)) inserted in (3.5) per q̂; shell corrections from Φ_{κκ′}(ΔR,t) for
  |ΔR| ≤ 4 shells; the IA ⟨P_αP_β⟩ tensor from PIMD. Cost ∝ N_k·N_G·N_q̂ ≈ 10⁸ cheap operations. Output: S_ℓm(q,ω) tables and P_ℓ-projected 𝒢 for
  SHM and halo-independent inputs (WP6).
- *Prediction to test:* for Si, Ge, GaAs, S_{ℓ≥4} vanishes in the incoherent multiphonon part, up to the shell and 𝔨₄ terms.

**G13: anharmonicity.**
- *Formula:* (6.2) for the coherent n_ph = 1, 2 terms, 𝒞₃, 𝒞₄ for the incoherent n_ph ≥ 2 terms, (5.1) for the IA, all constrained by (6.1).
- *Computation:* phono3py (fc3 on 4×4×4 primitive cells (128 atoms), pair cutoff ≈ 5 Å, ≈ 300 supercell DFT runs for Si) → Π^ph_ν(Q,ω),
  A^ph_ν(Q,ω) on 24³; hiPhive or TDEP for fc4 and T-renormalisation; 𝒞₃(t), 𝒞₄(t) by contracting phonon propagators (∝ N_k² per t point,
  ≈ 10³ CPU·h); PIMD δE^kin_q̂ (6.1) as the independent exact anchor.
- *Output:* nuisance template Δ^τ_A(q,ω) satisfying (6.1), typed per (6.1′), with an uncertainty from the fc3/fc4 fit and supercell convergence.

**L4 add-on (charge vertex at all q; serves G3 and dark-photon multiphonon at q < q_BZ).** Store the DFPT density response per Q in (i) and
Fourier-transform: 𝒵_{κα}(Q+G) = q_α(Z_κ − f^core_κ(q)) − δρ^val_{κα}(Q+G), q = Q + G, for |q| ≤ 20 keV (≈ 4000 G-vectors). This interpolates between
Born, Z*, quadrupoles and the rigid-ion (Brown-type) charge; negligible cost on top of DFPT.

---
## 11. WP0 defects reported by WP2 (status after WP0-v2)

| Label | Defect (v1 §11) | Status |
|---|---|---|
| WP2-D1 | x_coh = q/G_min is not the coherence control: not sufficient (n_ph = 1 coherent S stays a δ on the dispersion at any q), not necessary (n_ph ≥ 2 incoherent accurate in ω-integrated rates below q_BZ); use n_ph + shell parameter (2.3)–(2.4) | applied, WP0-v2 Table 6.1 (#10) |
| WP2-D2 | "2W = (q²/2M)⟨coth(βω/2)/ω⟩" holds only for isotropic B_κ (cubic sites); in general 2W_κ = q·B_κ·q, direction-dependent, enters L19 | applied (#10) |
| WP2-D3 | K label "coherent 1-ph (x_R ≪ 1)" conflates two parameters; a one-phonon incoherent regime exists at q_BZ < q ≪ (2Mω̄)^{1/2} (Si ≈ 5–20 keV) | applied (#10; K = 1ph-inc) |
| WP2-D4 | L6 pointer: mean exact (𝔨₁); width with the true E^kin_q̂; skewness from the BO curvature, remainder in X (5.2) | applied (#32) |
| WP2-C1 | WP0 §5.3 "Z*/ε_∞ (Fröhlich) vertex for LO phonons": for nucleon coupling the external vertex stays A_κF^M_κ; Z*/ε_∞ appears only inside the TO → LO Dyson series (4.4); external Z*/ε_∞ belongs to charge coupling (4.2) | applied (#8) |

No error found in WP0-v2 (3.1)–(3.4), (4.3)–(4.7) or (5.2)–(5.4) as used here; WP2v2-C1, C2, C8, C11d confirm (5.4), (3.4) and (4.7).
Notation remark (not a physics defect): WP0-v2 §6.2 (ii) writes the potential energy as V, which NOTATION reserves for the crystal volume; WP2-v2 uses
V_pot (flag IF-5).

---
## 12. Exact remaining gaps
1. Coherent n_ph = 2 at q < q_BZ from first principles: formula (2.2), computation specified (G13), not done; the §3.3 shell estimate is [E].
2. A rigorous pointwise (fixed q, ω) error bound on the incoherent approximation at n_ph ≥ 2; only the BZ average (2.4) is exact, and the band-edge
   O(1) failure is identified.
3. T > 0 shell sum at n_ph = 2 is conditionally convergent (acoustic Φ ~ T/ΔR); needs an Ewald-type resummation (irrelevant at mK).
4. Decay of the valence charge deformation at q ≫ q_BZ is [E]; the DFPT add-on of §10 decides it.
5. Non-perturbative anharmonicity (soft-mode, light-atom targets) lies outside (6.2); not needed for Si/Ge/GaAs (λ^anh ≈ 0.01).
6. Amorphous targets: (2.1) needs configurational averaging, not covered.
7. The GS/X split (5.2) rests on the WP0-v2 §6.2 (ii) Migdal amplitude ([D, sketch] for the boost reduction). Its first moment now agrees with WP3
   J3 and its contact face with WP0-v2 (4.7) (5.2′); WP3 must still evaluate 𝔨₃^X from the all-electron (W.5) against (5.2′) (OPEN, F4/OW0-8).

---
## 13. Literature (IDs verified against the arXiv API in v1, 2026-10-31; full-text HTML in literature/papers-WP2/)
[FT] 1712.06598 Eqs. (1)–(12); 1807.10291 Eqs. (29)–(32); 1910.08092 Eqs. (89)–(106); 2009.13534 (single-phonon rate, spin responses);
1911.03482 Eqs. (1)–(44); 2205.02250 Eqs. (1)–(55); 2011.09477 Eqs. (7)–(12); 2309.10839 Eqs. (1)–(62); 2411.03433 Eqs. (1)–(30); 2607.24933
Eqs. (1)–(47); 2506.11191 Eqs. (63)–(73); 2607.06005 (ℓ = 0, 2 sections; Eqs. (6), (10)); hep-ph/0608035 Eqs. (1)–(11). The §9 quotes were
re-extracted from the HTML for v2. [ABS] 2412.18330. Classical results without arXiv source (flagged): Placzek moments; Sears expansion;
Ambegaokar–Conway–Baym; Gonze–Lee non-analytic dynamical matrix; Born–Huang drag mass (via WP3).

---
## 14. Contested corrections
None. Every owed item (CORRECTIONS §0, §8; flags F4, F6, F11; consistency notes F3, F7) is applied as stated. One clarification, not a contest:
WP0-v2 Table 6.1 quotes "truncation N-phonon loses P[Pois(2W) ≥ N] of the f-sum (WP2)"; v2 shows it holds at any T and for the coherent S
(3.4′), so the quotation is correct and slightly stronger than v1's statement.

---
## 15. Interface flags
| # | Owner | Quantity | Recorded form | Mismatch / action |
|---|---|---|---|---|
| IF-1 (F4) | WP3 (WP0-v2) | X-sector moments of S_κκ | WP2 (5.2); WP0-v2 (4.7); WP3 J3, (W.5) | **consistent at the level of moments**: first moment = WP3 J3; contact face 𝓜³_κκ|_{V_eN} = −(m_e/M_κ)𝓜³_eκ with (4.7) (5.2′). Remaining: WP3 to compute 𝔨₃^X from the all-electron, all-k (W.5); valence/soft truncations (WP3 T3) cannot saturate (5.2′) |
| IF-2 (F6) | WP2 → WP5 | multiphonon S^{GS}_κκ, ρ^ph_κ | WP2 (2.2), (3.6) as used in WP0-v2 (7.3) | renamed GS/S^{GS}/ρ^ph_κ (rename done); WP5 must (i) treat ω′ < 0 entries of ρ^ph_κ as absorbed phonons, (ii) subtract E^{Mig}_1 from the GS f-sum when Migdal is seeded separately (3.4) |
| IF-3 | WP0-v2 | Table 6.1 truncation statement | "P[Pois(2W) ≥ N]" | consistent; valid at any T and for coherent S (3.4′) |
| IF-4 | WP6 | anharmonic nuisance type | WP6 (5.1) M/A/E/Δ; WP2 (6.1) | M type preserves (6.1) only at θ ∈ {0,1} (6.1′); WP6 to record the O(θ(1−θ)(r^M)²) violation or use A type for θ_A |
| IF-5 | NOTATION / WP0-v2 | potential energy symbol | WP0-v2 §6.2 (ii), (4.8): "V" | V is the crystal volume in NOTATION; propose row V_pot (and V_ee, V_eN, V_NN), E^ad_n for adiabatic energies |
| IF-6 | NOTATION | q_BZ, G_min | used by WP0-v2 Table 6.1 and WP2 | no NOTATION row; propose q_BZ ≡ 2π/a (Si 2.28 keV), G_min shortest nonzero G |
| IF-7 (F11) | X2 / WP1 | static-DFPT error | O(ω_Q²/E_g²) | WP2 L4 already used O((ω/E_g)²): consistent, no change |
| IF-9 | WP4 (relay) | one-phonon eigenvector phase | WP4-v2: e^{iq·r_κ} (CONVENTIONS §5) | WP2-v2 (2.2), (7.2) use the same e^{iq·r_κ}; consistent. Sources with e^{iG·x⁰} (1910.08092) map by e_κν → e_κνe^{−iQ·r_κ} |
| IF-8 (F3, F7) | WP3, WP5 | sector labels, thermal factor | WP0-v2 (7.1), (5.6) | no WP2 quantity affected. **CLOSED** (coordinator audit A13): WP3-v2 now writes S^{GS}_κκ |

---
## 16. Corrections applied (closing table)
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
All symbols follow NOTATION v4 and CONVENTIONS; **no deviations** (v4 renames: CORRECTIONS §17, closing-table row 38). Used as defined there: q, ω, ω_q, v, v_χ, v_min, v_max, v_E(t), v_E^ref,
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
stays the volume); **E^ad_n(R)** (adiabatic electronic energies; E^ad_0 = BO surface); **∂_q̂ ≡ q̂·∇_{R_I}**; **q_BZ ≡ 2π/a, G_min**; **ε_∞(q̂) ≡ q̂·ε_∞·q̂**;
**ν′, e^A_{ν′}** (analytic TO modes of D^dyn_A); **e^{s}_κν** (e^{+} ≡ e*, e^{−} ≡ e); **c̄_κ** (mean random coupling in (7.1)); **S̃_self,κ** (normalised self
term); **f^core_κ, δρ^val_κ** (core form factor, valence density response, §10); **P_ph(n_ph|q,ω)** (phonon-number distribution); **ΔE₃** (ω³-weighted
mean excitation energy, (5.2′)); **Δ^τ_A** (= Δ^τ_k at k = n_A); **a^A_{n_A}, θ_A** (type-A coefficient, anharmonic nuisance; v3 name a_A). Source-only notation appears
only inside quotes (§9: R, f̄_d, m_d, Ω_c, Δ_d, W_d, ℱ_med, g(q,ω), Y_j, ε*_{ν,k,j}, C_F, ℳ, e′, T_ℓm), per NOTATION §K.
