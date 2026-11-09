# R5 / WP2: lattice sector of the URF

Isolated theory agent. Read scope as in the brief. Theory only: the identity checks are in `code/WP2/checks.py`
(C1–C9, all PASS, < 10 s). Literature: 14 arXiv IDs, all verified against the arXiv API (§13), all read in FULL TEXT [FT]
through `lit.py fetch` (folder `literature/papers-WP2/`, PDFs deleted at the end).
Tags: **[D]** DERIVED (hypotheses stated), **[E]** ESTIMATED, **[C]** CONJECTURED. Notation: NOTATION v2 = WP0 §10. WP0
equations are cited as "WP0 (x.y)". New equations are numbered (s.n) here. Units ħ = c = k_B = 1, e² = 4πα. Retarded response R.

---
## 0. Results in one page

1. **Reduction [D]:** the lattice sector is the G sector of WP0 Theorem D, with n_e → ρ̄_e(q;R) (§1).
2. **Exact harmonic S at all phonon orders, coherent and at finite T [D]** (2.2); an exact shell expansion (2.3), whose L = 0 term is
   the incoherent approximation; a BZ-average theorem (2.4) stating when "incoherent" is exact.
3. **2607.24933 Eq. (47) (3D) is incomplete:** the polarisation weights |q̂·e|² and the intra-cell phases also differ, not only momentum
   conservation (§3.3).
4. **Truncating at n ≤ N phonons loses P[Pois(2W) ≥ N] of the f-sum** (3.4). An exact Panjer equation (3.5) gives S at all n, with the
   final-state phonon spectrum for WP5 (3.6).
5. **L4 [D]:** WP0 (5.4) with the total ε ≡ the Born-charge one-phonon formula with Z*/ε∞ and LO eigenvectors (Sherman–Morrison, (4.2)).
   This reproduces 1910.08092 Eq. (106) and 1807.10291 Eq. (31). 1712.06598 Eq. (5) carries a spurious 1/V_cell.
6. **L6 [D]:** exact anharmonic cumulants (5.1); the mean recoil is exact. **New: κ₃ splits exactly into G (BO curvature) + X (Migdal)**
   (5.2). The free limit gives hep-ph/0608035 Eq. (5).
7. **L18 / G13 [D]:** three exact linear constraints on the anharmonic nuisance (6.1); structure at O(η²) (6.2); negligible in the IA
   regime, at O(λ²(ω̄/E_R)^{1/2}).
8. **Nuclear spin [D]:** unpolarised spins give an *exactly* incoherent channel (7.1). PhonoDark drops it; 2506.11191 has it. Polarisation
   turns on a coherent term ∝ P². Transverse currents excite TA/TO (7.2).
9. **L19 / G11 [D]:** a harmonic rate formula (8.1). **Cubic isotropy theorem:** the harmonic incoherent S has no anisotropy in
   Si/Ge/GaAs at any n or T (8.2), which explains 2411.03433.
10. **WP0 defects (§11):** x_coh is not the coherence control parameter; 2W of Table 6.1 holds only for cubic sites.

---
## 1. The lattice sector from the WP0 master formula

**(1.1) Operators [D].** The spin-independent DM couplings are O_f(q) = Σ_κ f_κ(q) n_κ(q) − c_e n_e(q). For a nucleon coupling,
f_κ = [c_pZ_κ + c_n(A_κ−Z_κ)]F^M_κ(q) and c_e = 0. For a dark photon, f_κ = Z_κ and c_e = 1, i.e. O_z of WP0 (5.4). For spin
couplings, the nuclear rows are I_κ^b and J_κ^{ab} of WP0 (2.2).

**(1.2) The G-sector reduction [D]** (hypotheses H1–H4 of WP0 §6.2). By Theorem D (ii), in the G sector
(O′_κ)_GG = F^M_κ e^{iq·R_I} acts on nuclear coordinates, and (O′_e)_GG = ⟨Φ₀(R)|n_e(q)|Φ₀(R)⟩ ≡ ρ̄_e(q;R), up to O(κ_BO⁴). Hence

  S^G_{ff}(q,ω) = (2π/V) Σ_{i,f∈G} p_i |⟨f| Σ_I f_κ e^{iq·R_I} − c_e ρ̄_e(q;R) |i⟩|² δ(ω − E_f + E_i),                    (1.1)

which is a purely nuclear (vibrational) problem on the BO surface E₀(R). Expanding ρ̄_e about the equilibrium positions R⁰ gives
the **charge vertex**

  ρ̄_e(q;R) = ρ̄_e(q;R⁰) + i Σ_I e^{iq·R⁰_I} Δ_κ(q)·u_I + O(u²),   charge vertex 𝒵_κ(q) ≡ Z_κ q − Δ_κ(q) → q·Z*_κ (q → 0),   (1.2)

so the linear charge coupling to u_I is i𝒵_κ(q)·u_I e^{iq·R⁰_I} (proper, i.e. without the macroscopic field).

The limits are as follows.
- The rigid-ion approximation is Δ_κ = q f^{at}_κ(q) (so 𝒵_κ = q[Z_κ − f^{at}_κ(q)]) with f^{at} the atomic form factor. At q ≫ q_BZ this gives the effective
  charges Z_κ − f^{at}_κ(q) used by 2205.02250 §IV.3 (Fig. 9).
- At q → 0, 𝒵_κ(q) → q·Z*_κ, the Born charge (1910.08092 Eqs. (98)–(104), which (1.2) reproduces).
- The leading correction to the rigid-ion form is the valence deformation Δ_κ − q f^{at}_κ. It is computable by DFPT (§10, G3/L4).

**(1.3) Conventions in the literature (per-source factor relative to WP0 (3.1)) [FT].**

| Source | Definition of S | Factor to WP0 S |
|---|---|---|
| 2205.02250 Eq. (4); 2411.03433 Eq. (1); 2309.10839 Eq. (2); 2607.24933 Eq. (4); 1910.08092 Eq. (90) | (2π/V)Σ\|⟨f\|Σf e^{iq·r}\|0⟩\|²δ | 1 (T = 0) |
| 1911.03482 Eq. (2) | (1/N)Σ\|…\|²δ | ×2π/Ω |
| 1712.06598 Eq. (10) | neutron convention, rate via (4π/V_cell) in Eq. (9) | ×2π/Ω |
| 2506.11191 Eq. (69) | (1/N)Σ λ²C, with C lacking 1/V (their footnote 6) | ×1/Ω (C has the 2π) |

All the sources are at T = 0. WP0 (3.1) is Gibbs-averaged, and the T > 0 forms below add the Bose factors.

---
## 2. Harmonic S_κκ′ at all phonon orders (coherent, finite T)

**(2.1) Exact form [D].** Hypotheses: H3 at n_A = 0 (harmonic BO surface), the Gibbs state, and the operator (1.1) with the linear
part of (1.2) absorbed into f_κ(q). With x⁰_{ℓκ} = ℓ + r_κ, u_{ℓκ} = Σ_{kν}(2NM_κω_{kν})^{-1/2}(e_κ(kν)a e^{ik·x⁰ − iωt} + h.c.), and
Bloch's identity (exact for Gaussian states),

  S(q,ω) = (1/V)∫dt e^{iωt} Σ_{ℓκ,ℓ′κ′} f_κ^* f_{κ′} e^{−iq·(x⁰_{ℓκ}−x⁰_{ℓ′κ′})} e^{−W_κ−W_{κ′}} exp Φ_{κκ′}(ℓ−ℓ′,t),                     (2.1)

  Φ_{κκ′}(L,t) = Σ_{kν} [(n_{kν}+1)(q·e_κ)(q·e*_{κ′}) e^{ik·(x⁰_{ℓκ}−x⁰_{ℓ′κ′})−iω_{kν}t} + n_{kν}(c.c. in e, k) e^{+iω_{kν}t}]/(2Nω_{kν}√(M_κM_{κ′})),

with 2W_κ(q) = q·B_κ·q and B_κ = ⟨u_κu_κ⟩ = Σ_{kν} e_κe_κ^†(2n+1)/(2NM_κω). Expanding exp Φ in powers gives the **n-phonon coherent term**:

  S^{(n)}(q,ω) = (2π/Ω)(1/n!) Σ_{{ν_i,s_i}} ∫Π_i[Ω d³k_i/(2π)³ · (n_i + (1+s_i)/2)/(2ω_i)] δ(ω − Σ_i s_iω_i) (2π)³/Ω Σ_G δ³(q − Σ_i s_ik_i − G)
               × |Σ_κ f_κ e^{−W_κ} e^{iG·r_κ} M_κ^{−n/2} Π_i (q·e^{s_i}_κ(k_iν_i))|²,     e^{+} ≡ e*, e^{−} ≡ e.                          (2.2)

Here s_i = +1 (−1) means emission (absorption). Checks:
- n = 1, T = 0 reproduces 1910.08092 Eq. (90) (π/Ω = (2π/Ω)/2) and 1911.03482 Eq. (8) (×2π/Ω, without DW).
- n = 2, T = 0, G = 0, in the long-wavelength isotropic limit, reproduces the "contact" term 1911.03482 Eqs. (12), (16).
- n = 0 is the Bragg term ∝ δ(ω)Σ_Gδ³(q−G), which has zero measure for DM.

**(2.2) Shell expansion [D].** Group (2.1) by lattice separation L and basis pair (κ,κ′):

  S = S_inc + ΔS_coh,   S_inc = (1/Ω)Σ_κ|f_κ|² e^{−2W_κ}∫dt e^{iωt}[e^{Φ_{κκ}(0,t)} − 1],   ΔS_coh = (1/Ω) Σ_{(L,κ,κ′)≠(0,κ,κ)} f_κ^*f_{κ′} e^{−iq·(L+r_κ−r_{κ′})} e^{−W_κ−W_{κ′}} ∫dt e^{iωt}[e^{Φ_{κκ′}(L,t)} − 1].   (2.3)

At order n each shell term is ∝ Φ_{κκ′}(L,t)^n. By Cauchy–Schwarz, |Φ_{κκ′}(L,t)| ≤ [Φ_{κκ}(0,0)Φ_{κ′κ′}(0,0)]^{1/2}.
- For n = 1 the sum over L must be done in full: it produces the dispersion δ-function, and no truncation in L is allowed.
- For n ≥ 2 at T = 0 the series converges absolutely, because the acoustic Φ(L) ~ L^{-2} makes Φ² ~ L^{-4}.
- At T > 0 the classical acoustic correlation Φ ~ T/L makes the n = 2 shell sum only *conditionally* convergent. This is the
  quasi-elastic "absorb a thermal phonon" process. At mK it is irrelevant (τ_ph = 10⁻³), but it is flagged (§12).

**(2.3) BZ-average theorem [D].** Let j_BZ(r) ≡ (Ω/(2π)³)∫_BZ d³p e^{ip·r}. Then, for every n,

  (Ω/(2π)³)∫_BZ d³p S^{(n)}(q+p,ω) = S^{(n)}_inc(q,ω) + Σ_{κ≠κ′} j_BZ(r_κ−r_{κ′}) S^{(n)}_{κκ′,L=0}(q,ω) + O(q_BZ ∂_q ln[W_κ, |q̂·e|²]).   (2.4)

Proof: insert (2.3) and hold the smooth factors at q. ∫_BZ e^{ip·L} = 0 for L ≠ 0 removes every shell term except the intra-cell
cross terms. **The incoherent approximation is therefore exactly the BZ average of the coherent S, up to intra-cell cross terms and
gradient corrections.** Check C9 tests this on a monatomic chain, where it holds exactly.

---
## 3. Multiphonon: incoherent approximation, Poisson tail, Debye–Waller / Franck–Condon

**(3.1) Incoherent harmonic S at finite T [D]** (2.3), with the projected DOS D_κ^{q̂}(ω) = N^{-1}Σ_{kν}|q̂·e_κ|²δ(ω−ω_{kν})
(2411.03433 Eq. (18)). Define the one-phonon measure

  μ_κ(q;ω′) = (q²/2M_κ) D_κ^{q̂}(|ω′|)/ω′ · [n(ω′)+1]   (ω′ < 0 gives absorption, with weight n(|ω′|) ≥ 0),   2W_κ = ∫dω′ μ_κ.   (3.1)

Then

  S_inc(q,ω) = (2π/Ω) Σ_κ |f_κ|² e^{−2W_κ(q)} Σ_{n≥1} μ_κ^{*n}(q;ω)/n!   (* = convolution in ω).                         (3.2)

At T = 0 with an isotropic D^{q̂} = D_κ this is 2205.02250 Eq. (36) and 2411.03433 Eq. (12). With the full D^{q̂} it is
2411.03433 Eq. (24). For an Einstein solid at T = 0, (3.2) becomes the Poisson law of 2011.09477 Eq. (10):
|f(n,q)|² = (q/q₀)^{2n}e^{−q²/q₀²}/n!, with q₀² = 2Mω₀.

**(3.2) Debye–Waller and Franck–Condon (SOTA terminology).** "DW" means the e^{−2W} weight of the zero-phonon (Bragg) term. In a
local picture it is the Franck–Condon overlap |⟨0|e^{iq·u}|0⟩|² = e^{−2W}, so the Huang–Rhys factor of the lattice sector is
S_HR = 2W. The same compound-Poisson structure gives the electronic ZPL line shape in WP3 when μ is replaced by the Huang–Rhys
spectral function of the electron–phonon coupling change. This is a pointer only.

**(3.3) The coherent–incoherent crossover and 2607.24933 [FT, D].** For a 1D monatomic chain, 2607.24933 Eq. (44) states that coherent
and incoherent S^{(n)} differ only by the momentum-conserving δ. Our (2.2) confirms this. Their 3D generalisation, Eq. (47), keeps
the isotropic weight D(ω,k) = (Ω/3(2π)³)Σ_α δ(ω−ω_{αk}) inside the coherent sum. That is not correct. The exact replacement is
(2.2), with the per-phonon weights |q̂·e(k_iν_i)|² and, for a polyatomic basis, the intra-cell phases e^{iG·r_κ}. For example, at n = 1 and
q ≪ q_BZ, Eq. (47) gives LA a weight 1/3 plus two spurious TA δ-functions; the exact result is LA with weight 1 and no TA.
The physical conclusion (incoherent is accurate for n ≥ 2 in ω-integrated rates) survives through (2.4). Pointwise, the
correction is O(1) at the edges of the n-phonon bands, where only near-Γ modes contribute and coherence forces q ≈ G (their
Figs. 8–10). Rate-level size, after angular averaging and ω-binning wider than ω_max: |ΔS_coh/S_inc|_n ≈ Σ_shells z_L|j₀(qL)| c̄_L^n,
where c̄_L = ⟨u₀·u_L⟩/⟨u²⟩. For Si, c̄₁ ≈ 0.2–0.4, and at q = 10 keV, L = 2.35 Å this gives ≲ 3% for n = 2 [E].

**(3.4) Sum rules (consistency with WP0) [D].**
- Zeroth moment: ∫(dω/2π)S_self = n_κ|f_κ|².
- First moment: ∫ω′μ dω′ = q²/2M_κ at any T, so the **f-sum WP0 (4.6b) holds exactly**. Its distribution over phonon number at
  T = 0 is ∫ω S^{(n)} / ∫ω S = e^{−2W}(2W)^{n−1}/(n−1)!. A truncation at n ≤ N therefore misses the fraction
  P[Pois(2W) ≥ N] of the f-sum (check C3). This is the quantitative truncation criterion for WP6 nuisance bookkeeping (WP0 (8.2)).
- The one-phonon term **without** DW saturates the f-sum exactly. With the coherent completeness relation Σ_ν e_{κν}e_{κ′ν}^† = δ_{κκ′}𝟙
  this holds for the coherent S too, including Umklapp. It is Placzek's rule. "One-phonon with e^{−2W}", as in 1910.08092 Eq. (94),
  carries only e^{−2W} of the f-sum, and the multiphonons supply the rest.
- Cross-species first moments vanish (WP0 (4.6c)), so intra-cell interference changes no f-sum.
- G holds 1 − O(κ_BO⁴) of the nuclear f-sum, and the remainder is Migdal (Theorem D (iii)).

**(3.5) Compound-Poisson integral equation [D]** (from ∂_t e^{Φ} = Φ̇e^{Φ}; check C4):

  ω S_κ(q,ω) = ∫dω′ ω′ μ_κ(q;ω′) S_κ(q, ω−ω′),   S_κ ≡ e^{−2W}Σ_{n≥0} μ^{*n}/n!.                                         (3.5)

This holds at any T. Solved on an ω grid, it gives the all-n S with no phonon-number truncation, at a cost of O(N_ω²) per q, or
O(N_ω log N_ω) with an FFT of e^{Φ(t)}. It supersedes the n ≤ 10–20 truncations of 2205.02250 and 2411.03433. Eq. (26) of 2411.03433
is the n-by-n version of the same recursion.

**(3.6) Final-state phonon spectrum (the WP5 hand-over, WP0 (7.1)) [D].** The mean number of created phonons per dω′, at given
(q,ω), is

  ρ_κ(ω′|q,ω) = μ_κ(q;ω′) S_κ(q,ω−ω′)/S_κ(q,ω),   ∫ω′ρ dω′ = ω  (by 3.5),   ∫ρ dω′ = ⟨n⟩.                                      (3.6)

Replacing μ by μ_{κν} (the branch-projected DOS) gives the branch content (LA/TA/LO/TO), which the down-conversion modelling of
WP5 needs. In the incoherent approximation the phonon momenta are uniform over the BZ, weighted by the DOS.

---
## 4. Polar couplings: dark photon, Born charges, ε∞, LO–TO (L4)

**(4.1) Start [D].** WP0 (5.4): S_zz(q,ω) = (2q²/e²) Im[−(ε^{-1})_{00}(q,ω)]/(1−e^{−βω}), with the **total** ε. This is exact for total-charge
coupling.

**(4.2) Adiabatic, harmonic, q → 0 [D]** (hypotheses: G sector; ω ≪ E_g, so the electronic ε is ε∞ = const; n_A = 0; q ≪ q_BZ).
The total longitudinal ε is

  ε(q̂,ω) = ε_q̂ + (e²/Ω) Σ_m [p(q̂)·e_m]²/(ω_m² − ω²),   ε_q̂ ≡ q̂·ε∞·q̂,   p(q̂)_{κα} ≡ (q̂·Z*_κ)_α/√M_κ,

where m runs over the analytic (TO) modes of D_A. Sherman–Morrison with D_NA = D_A + (e²/Ωε_q̂) p pᵀ, the non-analytic dynamical
matrix whose eigenmodes λ are the LO-split phonons, gives exactly (check C2)

  −1/ε = −1/ε_q̂ + (e²/Ωε_q̂²) pᵀ(D_NA − ω²)^{-1}p  ⇒  S_zz = (2π/Ω) Σ_λ (1/2ω_λ) |Σ_κ q·Z*_κ·e*_{κλ}/(ε_q̂√M_κ)|² δ(ω − ω_λ).    (4.2)

The ELF form with the total ε is therefore *identical* to the Born-charge one-phonon formula with vertex q·Z*/ε∞ and NA
eigenvectors. **This proves that the "screen by ε∞ only, put the ions in the source" prescription of 1910.08092 (text below Eq. 104)
equals WP0's total-ε prescription.** The two are bookkeepings of one Dyson series. With F_DM = (αm_e/q)², 𝒱 = Q_χe²/q², and WP0 (3.3),
this reproduces 1910.08092 Eq. (106) and 1807.10291 Eq. (29).

**(4.3) One polar branch [D]** (check C1). With ε = ε∞(ω_L²−ω²)/(ω_T²−ω²) and LST:

  Im[−1/ε] = (πω_L/2)(1/ε∞ − 1/ε₀) δ(ω−ω_L)  ⇒  Γ = ∫d³q/(2π)³ 2πδ(ω_q−ω_L) · Q_χ²e²ω_L(1/ε∞−1/ε₀)/(2q²),                  (4.3)

which is |M|² of 1807.10291 Eq. (31) with e′ = Q_χe, and σ̄_e of 1712.06598 Eq. (8).

**(4.4) Electron-only and nucleon couplings in polar crystals [D].**
- In the G sector the electron-only vertex is −ρ̄_e, whose linear part is q·(Z_κ𝟙 − Z*_κ). This is 1910.08092 Eq. (104), f_e term.
- The nucleon vertex is A_κ with *no* Z*/ε∞ factor. The LO–TO splitting enters only through the NA eigenvectors, i.e. through the
  R̃ε^{-1}vR̃ term of WP0 (5.3).

**(4.5) Si and Ge [D].** Z*_κ = 0 by symmetry: the two sites are related by inversion and Σ_κZ*_κ = 0. The leading dark-photon
one-phonon vertex is then quadrupolar, 𝒵_κα(q) = −(i/2)q_βq_γQ_{κ,βγα} + O(q³), so S_zz^{(1)} ∝ q⁴. A second contribution is the
two-phonon term from the second-order dipole ∂Z*/∂u. This agrees with SOTA #5 (zero ionic ε part in Si).

---
## 5. Impulse limit and free nuclear recoil (L6)

**(5.1) Exact cumulants of the self structure factor [D]** (check C5). Hypotheses: the self part of S_κκ; any H whose potential is
local in the struck coordinate (WP0 hypothesis (L)); any anharmonicity; any T; TR symmetry (so odd momentum moments vanish).
Write ∂ ≡ q̂·∇_{R_I} and p ≡ q̂·P_I. The ω-cumulants of S_self/∫S_self are

  κ₁ = q²/2M,   κ₂ = q²⟨p²⟩/M²,   κ₃ = (q²/2M²)⟨∂²V⟩,   κ₄ = (q²/M²)⟨(∂V)²⟩ + (q⁴/M⁴)(⟨p⁴⟩ − 3⟨p²⟩²).                        (5.1)

The derivation follows 2309.10839 Eqs. (56)–(60), with ⟨p[H,p]⟩ = ½⟨∂²V⟩ from stationarity. In the harmonic case (5.1) reproduces the
cumulants of (3.2), k_m = ∫ω′^m μ dω′: κ₂ = (q²/2M)∫Dω coth(βω/2) dω, κ₃ = (q²/2M)∫Dω² dω, and so on.
**κ₁ is exact, so the mean of the impulse peak is never shifted.** The "shift of the peak" in 2205.02250 Eq. (38) is a shift of the
mode by κ₃ (skewness), not of the mean.

**(5.2) The G/X split of κ₃ [D]** (leading BO order, H2; check C6). For the full Coulomb H, V contains V_eN, and ⟨∂²V_eN⟩ includes the
contact term Z_κe²ρ_e(R_κ)/3. The second-derivative identity ∂²E₀ = ⟨∂²V⟩ − 2Σ_n|⟨n|∂V|0⟩|²/(E_n−E₀), together with the Migdal amplitude
of WP0 §6.2 (ii), (q/M)⟨n|∂V|0⟩/(E_n−E₀)², gives

  κ₃^{total} = κ₃^G + κ₃^X,   κ₃^G = (q²/2M²)⟨∂²E₀⟩_vib,   κ₃^X = (q²/M²)Σ_n|⟨n|∂V|0⟩|²/(E_n−E₀) = ω³-moment of the Migdal sector.   (5.2)

Consequences.
- The lattice impulse approximation must use the **BO curvature**, not ⟨∇²V⟩ of the full Hamiltonian.
- The ω³ moment of S_κκ is dominated by the X sector, despite that sector's O(κ⁴) weight. This is the nuclear-diagonal companion of
  WP0 (4.7) and a consistency test for WP3's Migdal spectra.

**(5.3) Chain to the free recoil [D].**
1. The IA is the saddle at t ≈ 0 (2205.02250 Eqs. (37)–(39)). To leading order in 1/q it is equivalent to

     S_IA(q,ω) = (2π/Ω)Σ_κ|f_κ|² ∫d³p n_κ(p) δ(ω − q²/2M_κ − q·p/M_κ),                                            (5.3)

   with n_κ(p) the (anharmonic, T-dependent) nuclear momentum distribution. A Gaussian n_κ gives 2205.02250 Eq. (39),
   Δ² = κ₂ = 4E_R K_q̂, where K_q̂ = ⟨p²⟩/2M.
2. Taking Δ/E_R ≈ (ω̄/E_R)^{1/2} → 0 gives S^FR = (2π/Ω)Σ_κ|f_κ|²δ(ω − q²/2M_κ) (2205.02250 Eq. (42)).
3. In WP0 (3.4), with the isotropic halo (∫d³v f δ = η/2q, WP0 (9.1)) and |𝒱_p|² = πσ_p/μ_p², this gives
   dR/dE = ρ_χσ_N|F(q)|²η(v_min)/(2m_χμ_N²) with v_min = q/2μ_N, which is hep-ph/0608035 Eq. (5) (check C8).
4. The Helm |F|² of hep-ph/0608035 Eq. (9) is a parametrisation of |F^M_κ|² (WP0 (2.2)) under the assumption F_mass = F_charge
   (their Eqs. (7)–(8)), a 10–20% nuclear-structure systematic (their abstract).

---
## 6. Anharmonic expansion (L18, G13)

**(6.1) Exact constraints [D].** Let Δ_anh ≡ S_self^{(n_A≥1)} − S_self^{harm}, at fixed q and for the self part. Then (5.1) and the
normalisation give

  ∫dω Δ_anh = 0,   ∫dω ω Δ_anh = 0,   ∫dω (ω−q²/2M)² Δ_anh = q²δ⟨p²⟩/M²,                                                  (6.1)

where δ⟨p²⟩ is the anharmonic change of the kinetic energy. It is a static quantity, so PIMD gives it exactly. These are the linear
constraints that WP0 (8.2) asks for on the anharmonic nuisance θ_A.

**(6.2) Structure at O(η_anh²) [D in structure].** Use the cumulant expansion of ⟨e^{−iq·u(t)}e^{iq·u}⟩ beyond Gaussian, with K_m ∝ q^m
and K₃ ∝ Φ⁽³⁾, K₄ ∝ Φ⁽⁴⁾ + Φ⁽³⁾².
- (a) **One-phonon:** δ(ω−ω_ν) → A_ν(k,ω) = −2Im[2ω_ν/(ω²−ω_ν²−2ω_νΣ_ν(k,ω))]. Σ_ν is the bubble (Φ⁽³⁾²) plus the loop
  (Φ⁽⁴⁾) self-energy. The off-shell tail of A_LA is exactly the "anharmonic two-phonon" term of 1911.03482 Eqs. (13), (17),
  including their iΓ/2 propagators.
- (b) **Interference** of the one-phonon amplitude (via one cubic vertex) with the two-phonon contact term. It gives Fano-asymmetric
  line shapes and vanishes at leading order in the long-wavelength limit (real eigenvectors, 1911.03482 below Eq. (14)).
- (c) The anharmonic B_κ (that is, 2W) and ⟨p²⟩.
- (d) n-phonon terms with fewer DM vertices. With q ≫ q_BZ, the power counting is λ^{2k}x_R^{n−k} against x_R^n
  (2309.10839 Eq. (39)), so anharmonicity dominates the n-phonon term for x_R ≲ λ^{2k/k}. It matters only where S_harm is
  suppressed: high ω at small q.
- In the IA regime, anharmonicity enters only through κ₂, κ₃, κ₄. The Edgeworth parameters are γ₁ = κ₃/κ₂^{3/2} ~ (ω̄/E_R)^{1/2}, and
  the anharmonic parts are O(λ²), so the correction is O(λ²(ω̄/E_R)^{1/2}). This derives the conclusion of 2309.10839 ("negligible
  above ~10 MeV").

**(6.3) The 2309.10839 toy model, audited [D].**
- Matching: ω₀ = 1/⟨ω^{-1}⟩ plus the Gaussian smearing of their Eqs. (16)–(17) reproduces κ₁ and κ₂ exactly, since
  xω₀² + xσ² = q²ω̄/2M. It gives the harmonic κ₃ = (q²/2M)(3ω₀ω̄ − 2ω₀²) instead of (q²/2M)⟨ω²⟩: 6% low in Si [E], with
  ω̄ ≈ 40, ω₀ ≈ 28 and √⟨ω²⟩ ≈ 44 meV [E].
- Missing physics: (i) the 3D, angle-dependent single-site potential (their Eq. (23); taking the maximum-anharmonicity direction
  overestimates); (ii) intersite anharmonicity, i.e. the linewidths of (6.2a), which a single site cannot produce.
- **Normalisation discrepancy [FT]:** their Eq. (9) has e^{−W_d}, while their Eq. (10) defines W_d = (q²/4m_d)∫D/ω. This
  contradicts 2205.02250 Eq. (36) and their own Eq. (13), which have e^{−2W}. It is a typo at the level of the formula; we did not
  check whether it reached their numerics.

---
## 7. Nuclear-spin and nuclear-current couplings into phonons

**(7.1) Spin density [D].** Operator I_κ^b(q) of WP0 (2.2). Hypotheses:
- (S1) spin–lattice couplings (hyperfine, nuclear quadrupole) are ≪ ω_ph (≲ μeV against tens of meV);
- (S2) each spin-carrying isotope κ̃ occupies sites at random, with abundance c_κ (²⁹Si 4.7%, ⁷³Ge 7.8%);
- (S3) spin states are uncorrelated between sites, with polarisation P_κ along ẑ (paramagnet; ordering only at ≲ μK).

The lattice and spin traces then factorise. With g_κ ≡ F^Σ_κ⟨S_N⟩_κ/J_κ, f_{ℓκ} = g_κ I^b_{ℓκ}σ_{ℓκ} is a random coupling, and the
decomposition of 2205.02250 Eqs. (9)–(11) becomes exact:

  S^{bb}_{II}(q,ω) = S_coh[f̄_κ = c_κg_κ⟨I^b⟩] + (2π/Ω)Σ_κ c_κ g_κ²[⟨(I^b)²⟩ − c_κ⟨I^b⟩²] S̃_self,κ(q,ω),   ⟨I^z⟩ = P_κJ_κ, ⟨I^{x,y}⟩ = 0.   (7.1)

Here S̃_self is the normalised self term of (3.2), convolved with the Larmor spectrum (relative shift ω_L/ω_ph ~ 10⁻⁶).
- **Unpolarised (P = 0):** the channel is *exactly* incoherent, with ⟨(I^b)²⟩ = J(J+1)/3. The one-phonon part scales as
  q²D^{q̂}(ω)/ω. There is no coherent LA δ-function, so no q-linear enhancement at small q. This is 2506.11191 Eqs. (68)–(72), whose
  isotropic DOS is exact for cubic sites.
- 2009.13534 (text after its single-phonon rate) **drops** unordered-spin responses, and so omits this nonzero channel.
- **Polarised targets** (DNP, or B/T: P ≈ μ_IB/T, a few % at 1 T and 10 mK [E]) switch on a coherent term ∝ P², with the full
  one-phonon dispersion. They also switch on S_{nI} ∝ P interference with the SI channel through 𝔇_{n,I} (WP0 (2.3)).

**(7.2) Nuclear currents [D]** (rows j_κ, J_κ of WP0 (2.2)). The one-phonon matrix element is
⟨kν|j_κ^a(q)|0⟩ = −i(ω_{kν}/2NM_κ)^{1/2} e*^a_{κν} e^{−i(k−q)·x⁰} + O(q·u). Hence:
- **Longitudinal:** S_{n j_L} = (ω/q)S_nn exactly (WP0 (9.1 α)).
- **Transverse:** S^{(1)}_{j_Tj_T}(q,ω) = (2π/Ω)Σ_ν (ω_ν/2)|Σ_κ f_κ e^{iG·r_κ}(ê_⊥·e*_{κν})/√M_κ|² δ(ω−ω_ν). This excites TA/TO modes
  that density couplings cannot reach at q ≪ q_BZ. Relative to a density coupling it is suppressed by (ω/q v_χ)²-type DM-side
  factors, set by 𝔇.

---
## 8. Full q-vector anisotropy and daily modulation (L19 lattice part, G11)

**(8.1) Harmonic rate formula [D].** Hypotheses: 𝔇 depends on |q| only (true for O₁; the velocity-dependent operators need the
v-resolved form); the halo is isotropic in the Galactic frame and boosted by v_E(t), so g(q,ω) = ∫d³v f_χ δ(ω−ω_q) depends on q̂
only through x = q̂·v̂_E. Write S(q,ω) = Σ_{ℓm}S_{ℓm}(q,ω)Y_{ℓm}(q̂) in crystal axes. Funk–Hecke then gives

  dR/dω(t) = (ρ_χ/m_χρ_T) Σ_{ℓm} Y_{ℓm}(v̂_E^{cr}(t)) ∫ q²dq/(2π)³ 𝔇(q) S_{ℓm}(q,ω) · 2π∫_{−1}^{1}dx P_ℓ(x) g(q,ω;x).                (8.1)

Here v̂_E^{cr}(t) is the Earth-velocity direction in crystal axes, rotating with the sidereal day (2411.03433 Eq. (30)). The structure
matches the harmonic method of 2607.06005.

**(8.2) Selection rules [D]** (check C7).
- S(q,ω) = S(−q,ω) (TR or inversion) implies ℓ even.
- Cubic point groups have invariants only at ℓ = 0, 4, 6, 8, … .
- **Cubic isotropy theorem.** If every site κ has cubic site symmetry (T_d in Si, Ge, GaAs and diamond), every rank-2 site tensor is
  ∝ 𝟙: D_κ^{ij}(ω) = δ^{ij}D_κ(ω)/3 and B_κ ∝ 𝟙. Then (3.1)–(3.2) depend on q̂ only through q̂·D·q̂ = D/3. **The harmonic incoherent S
  is exactly isotropic at every n and T**, so its daily modulation vanishes identically. This explains why 2411.03433 (abstract)
  finds negligible modulation in Si and GaAs and 1–10% in Al₂O₃, where the site tensors are anisotropic and ℓ = 2 is allowed.
- **Residual anisotropy in cubic crystals:**
  - (i) the coherent one-phonon term (full anisotropy; it dominates for m_χ ≲ few MeV);
  - (ii) the coherent shell terms of (2.3) at n ≥ 2 (ℓ ≥ 4, size from §3.3);
  - (iii) in the IA regime, the rank-4 non-Gaussian part ⟨p_q̂⁴⟩ − 3⟨p_q̂²⟩² of κ₄ (5.1), which is O(λ⁴, λ₃²) and tiny;
  - (iv) for non-cubic crystals the IA width tensor ⟨p_ip_j⟩. 2411.03433 neglects it ("isotropic approximation" for the IA, with
    q̂ = ẑ), which is a small, systematically signed omission.
- **Pointer to WP3 [D, conditional on the form of their Eq. (33)].** 2607.06005 shows that the soft-limit Migdal rate depends only on
  the ℓ = 0, 2 moments of the ELF. In a cubic crystal the ℓ = 2 moment vanishes identically, so the Migdal daily modulation in Si and
  GaAs is zero at that order. Any nonzero value is a k-mesh or symmetry-breaking artefact or a higher-order (beyond-soft) effect.

---
## 9. LIMITS entries

**L4. Single phonon; dark photon via Born charges.**
- *Source* [FT]: 1910.08092 Eq. (92), with Y_j of Eqs. (104)–(105) and the dark-photon rate Eq. (106); 1807.10291 Eqs. (29)–(31);
  1712.06598 Eqs. (4)–(5), (10)–(11); 1911.03482 Eq. (8); 2009.13534 (single-phonon rate, general operators).
- *Chain:* WP0 (3.3) → (1.1) G sector at n_B = 0 → harmonic (2.2) at n = 1, T = 0 → vertex f_κ (nucleon A_κF^M_κ, 1910.08092 Eq. (94);
  charge 𝒵_κ → q·Z*_κ (1.2)) → dark photon: WP0 (5.4) ≡ (4.2) (Sherman–Morrison) → one branch → (4.3).
- *Validity (Si/Ge/GaAs):*
  - q ≪ q_BZ (2.3/2.2/2.2 keV) for the Z* vertex and the analytic eigenvector forms; the full (2.2) holds at all q with Umklapp;
  - ω_LO ≪ E_g, adiabatic error O((ω/E_g)²): GaAs (36 meV/1.5 eV)² ≈ 6×10⁻⁴;
  - T ≪ ω;
  - harmonic, with η_anh ≈ 0.01–0.03 (WP0 Table 6.1).
- *Leading corrections:*
  - finite-q charge vertex: valence deformation and dynamical quadrupoles (4.5), O(qa) relative in polar crystals and the leading
    term in Si/Ge;
  - DW e^{−2W}: 2W ≈ 6×10⁻⁴ at q = 1 keV in Si [E] (u_x² ≈ 0.0025 Å²);
  - anharmonic linewidth A_ν (6.2a), O(10⁻³) relative for Si optical phonons [E];
  - for dark photons in Si, the two-phonon term from ∂Z*/∂u.
- *Discrepancies:* (a) 1712.06598 Eq. (5) with Eq. (7): C_F² ∝ 1/V_cell makes |M|² dimensionally E² in the continuum golden rule of their Eq. (6). The
    consistent result (4.3) = 1807.10291 Eq. (31) has no cell volume, i.e. V_cell must be the normalisation volume, which cancels.
  (b) 1712.06598 Eq. (12) uses equal-mass eigenvectors, which leaves a spurious LO term ∝ (√A₁−√A₂)²q². The correct leading LO term is
    the q⁴a² term of 1911.03482 Eq. (44). For GaAs the spurious term is subdominant for q ≳ 0.1 keV [E].
  - Convention factors are in table (1.3).

**L5. Multiphonon incoherent approximation and Poisson tail.**
- *Source* [FT]: 2205.02250 Eqs. (15), (23)–(24), (36); 2011.09477 Eqs. (7)–(12); 2411.03433 Eqs. (12), (24); 2607.24933 Eqs. (44), (47).
- *Chain:* (1.1) → harmonic (2.1) → drop the shell terms (2.3) (equivalently the BZ average (2.4) minus intra-cell terms) → isotropic
  projected DOS (exact for cubic sites, §8.2) → T → 0 → (3.2) → Einstein → Poisson.
- *Validity:* n ≥ 2, or rates ω-integrated over ≳ ω_max (pointwise O(1) errors at n-phonon band edges, §3.3); n = 1 needs (2.2) at all q;
  - x_R = q²/2Mω̄ ≈ 1 at q ≈ 47 keV (Si) and ≈ 58 keV (Ge), with ω̄_Si ≈ 40, ω̄_Ge ≈ 23 meV [E]. The multiphonon window is roughly
    q ≈ 10–100 keV, m_χ ≈ 2–20 MeV at v_max ≈ 800 km/s.
- *Leading corrections:* coherent shell terms ~z|j₀(qL)|c̄^n (≲ 3% at n = 2 in Si, §3.3); anharmonic (6.2d); T via Bose factors (3.1),
  O(e^{−ω/T}); the Migdal transfer of O(κ⁴) of the f-sum. The truncation error is fixed exactly by (3.4), or removed by (3.5).
- *Discrepancies:* 2607.24933 Eq. (47) (§3.3); the 1911.03482 per-cell convention (1.3).

**L6. Free nuclear recoil, Helm.**
- *Source* [FT]: hep-ph/0608035 Eqs. (5), (9)–(11); 2205.02250 Eqs. (38)–(42); 2011.09477 Eq. (12).
- *Chain:* (1.1) → self part → IA (5.3) → narrow width → WP0 (3.4) → C8.
- *Validity:*
  - x_R ≫ 1 (q ≳ 2√(2Mω̄) ≈ 94 keV Si, 116 keV Ge, i.e. m_χ ≳ 20–40 MeV at the kinematic endpoint);
  - the threshold far from the kinematic endpoint, in units of Δ = (q²ω̄/2M)^{1/2};
  - no electronic excitation (the X weight is O(κ⁴)).
  - E_R above the displacement threshold changes the *partition*, not S (§10, G3).
- *Leading correction:* Gaussian smearing with Δ² = 4E_RK_q̂, which uses the true (zero-point plus anharmonic) kinetic energy; then the
  skewness κ₃^G (5.2), not ⟨∇²V⟩; the mean is exact. Near the threshold this gives the "Poisson tail" enhancement of 2011.09477.
- *Discrepancy:* 2205.02250's "true peak shifted" is the mode, not the mean (5.1). The WP0 L6 pointer is incomplete (§11).

**L18. Anharmonic NR corrections.**
- *Source* [FT]: 2309.10839 Eqs. (9)–(10), (23)–(26), (39), (52)–(62); also 2412.18330 [title and abstract].
- *Chain:* (1.1) with n_A ≥ 1 → self part (q ≫ q_BZ) → single site (neighbours frozen, so no intersite Φ⁽³⁾ and no linewidths) →
  1D along the maximum-anharmonicity direction → perturbation theory in λ₃, λ₄, or the IA with the cumulants (5.1).
- *Validity:* λ₃ ≈ 0.01, λ₄ ≈ 10⁻⁴ (Si, 2309.10839); q > q_BZ; the 1D reduction overestimates.
- *Leading corrections:* the exact constraints (6.1); the linewidth and Fano terms (6.2a–b), which the single site lacks; the 3D
  angular average of f_k(θ,φ)².
- *Discrepancy:* e^{−W} against e^{−2W} (§6.3).

**L19 (lattice part). Daily modulation.**
- *Source* [FT]: 2411.03433 Eqs. (18)–(24), (28)–(30); 2607.06005 (harmonic method, ℓ = 0, 2 Migdal).
- *Chain:* WP0 (3.3) with the full q-vector S → (8.1). Phonon S from (2.2) at n = 1 and (3.2) with D^{q̂} at n ≥ 2.
- *Validity:* (8.1) hypotheses; the incoherent approximation for n ≥ 2 as in L5.
- *Leading corrections:* cubic crystals, §8.2 (i)–(iii); non-cubic crystals, the IA width tensor (iv).
- *Discrepancy:* none in normalisation. The isotropic IA width of 2411.03433 is an omission, not an error.

---
## 10. Gaps assigned: closing formulas and computation specifications

**G3, lattice side: the multiphonon S_NN that WP5 needs.**
- *Formula:* (2.2) at n = 1 (coherent); (3.2) via (3.5) for n ≥ 2; (5.3) for the IA; the final-state spectra (3.6) and branch content.
  For NR the MD seed is the struck atom with momentum p + q, p ~ n_κ(p) of (5.3). That is exact to leading order in 1/q, and the
  energy partition (heat, defects, charge) is then WP5's transport problem.
- *Computation:* (i) QE pw.x/ph.x (LDA/PBEsol; Si/Ge ecut 50–60 Ry, k 8³, DFPT q 8³) → phonopy Fourier interpolation onto a 48³ mesh: D_κ^{ij}(ω),
    B_κ, branch-projected DOS, with tetrahedron ω-resolution 0.1 meV. (ii) i-PI PIMD (P ≈ 32 beads at 10 K; 216-atom cell; MLIP or DFTB) for n_κ(p), ⟨p²⟩, ⟨∂²E₀⟩ and κ₄, statistically converged to
    < 1%. (iii) New module (≈ 300 lines): solve (3.5) per (q, q̂) on an ω grid (N_ω ≈ 10⁴, FFT); output S_κ(q,ω), P(n|q,ω), ρ_κν(ω′|q,ω).
- *Cost:* DFPT ≈ 10² CPU·h; PIMD ≈ 10³ CPU·h with an MLIP; tables ≈ minutes.
- *Outputs:* HDF5 tables of S(q,q̂,ω) and ρ(ω′|q,ω) for q ∈ [0.1, 300] keV and ω ∈ [0, 50] eV, plus the IA-to-free switch at
  x_R > 16 with the Edgeworth κ₃^G, κ₄ terms.

**G11 (lattice): anisotropy and modulation.**
- *Formula:* (8.1) with the S_{ℓm} of (2.2) and (3.2).
- *Computation:* n = 1 from phonopy eigenvectors (48³ mesh, Umklapp to |q+G| = 30 keV), projected onto Y_{ℓm} (ℓ ≤ 12 cubic, ≤ 8 for
  Al₂O₃/SiC; Lebedev grid of 590 points); n ≥ 2 from the D^{ij}_κ tensors (2411.03433 Eq. (20)) inserted in (3.5) per q̂; shell corrections
  from Φ_{κκ′}(L,t) for L ≤ 4; the IA ⟨p_ip_j⟩ tensor from PIMD. Cost ∝ N_k·N_G·N_q̂ ≈ 10⁸ cheap operations (minutes).
  Output: S_{ℓm}(q,ω) tables and P̃_ℓ[g] for SHM and halo-independent inputs (WP6).
- *Prediction to test:* for Si, Ge and GaAs, S_{ℓ≥4} vanishes in the incoherent multiphonon part, up to the shell and κ₄ terms.

**G13: anharmonicity.**
- *Formula:* (6.2) for the coherent n = 1 and n = 2 terms, with the K₃ and K₄ cumulants for the incoherent n ≥ 2 terms, and (5.1)
  for the IA, all constrained by (6.1).
- *Computation:* phono3py (fc3 on 4×4×4 primitive cells (128 atoms), pair cutoff ≈ 5 Å, ≈ 300 supercell DFT runs for Si) →
  Σ_ν(k,ω), A_ν(k,ω) on a 24³ mesh; hiPhive or TDEP for fc4 and T-renormalisation; K₃(t), K₄(t) by contracting the phonon propagators
  (∝ N_k² per t-grid point, ≈ 10³ CPU·h); PIMD δ⟨p²⟩ (6.1) as the independent exact anchor.
- *Output:* the nuisance template Δ_anh(q,ω) satisfying (6.1), with an uncertainty from the fc3/fc4 fit and supercell convergence.

**L4 add-on (charge vertex at all q; serves G3 and dark-photon multiphonon at q < q_BZ).**
- Store the DFPT drho for each k in (i) and Fourier-transform: 𝒵_κα(k+G) = q_α(Z_κ − f^{core}_κ(q)) − Δn^{val}_{κα}(k+G),
  for |q| ≤ 20 keV (≈ 4000 G-vectors).
- This interpolates between Born, Z*, quadrupoles, and the Brown-type rigid charge. The cost is negligible on top of the DFPT run.

---
## 11. WP0 defects and clarifications

- **D1 (defect).** WP0 Table 6.1 and pointer L5 treat x_coh = q/G_min as the coherent/incoherent control parameter ("incoherent,
  x_coh ≫ 1"). By (2.3)–(2.4) it is not sufficient (at n = 1 the coherent S stays a δ on the dispersion at any q) and not necessary
  (n ≥ 2 is accurate in ω-integrated rates even at q < q_BZ). Replace it by the phonon order n plus the shell parameter z|j₀(qL)|c̄_L^n.
- **D2 (defect).** WP0 Table 6.1 writes "2W = q·⟨uu⟩·q = (q²/2M)⟨coth(βω/2)/ω⟩". The second equality holds only for an isotropic B_κ
  (cubic sites). In general 2W_κ = q·B_κ·q, which is direction-dependent (Al₂O₃), and it enters L19.
- **D3 (imprecision).** The K label "coherent 1-ph (x_R ≪ 1)" conflates two parameters. A one-phonon *incoherent* regime exists at
  q_BZ < q ≪ √(2Mω̄): Si q ≈ 5–20 keV.
- **D4 (incomplete pointer).** For L6, besides the Gaussian width: the mean is exact (κ₁); the width must use the true ⟨p²⟩; and the
  skewness must use the BO curvature, with the remainder in X (5.2).
- **C1 (clarification).** WP0 §5.3 says "In BO language [the second term of R_NN] produces the Z*/ε∞ (Fröhlich) vertex for LO
  phonons". For nucleon coupling the external vertex stays A_κ. Z*/ε∞ appears only inside the Dyson series that turns TO into LO (4.4).
  The external Z*/ε∞ vertex belongs to charge coupling (4.2).
- No error found in WP0 (3.1)–(3.4), (4.3)–(4.6) or (5.2)–(5.4) as used here. Our checks C1, C2 and C8 confirm (5.4) and (3.4) in the
  phonon regime.

---
## 12. Exact remaining gaps
1. Coherent n = 2 at q < q_BZ from first principles: the formula is (2.2) and the computation is specified (G13), but it has not been done.
   The §3.3 shell estimate is [E].
2. A rigorous pointwise (fixed q, ω) error bound on the incoherent approximation at n ≥ 2. Only the BZ average (2.4) is exact, and the
   band-edge O(1) failure is identified.
3. The T > 0 shell sum at n = 2 is conditionally convergent (acoustic Φ ~ T/L) and needs an Ewald-type resummation (irrelevant at mK).
4. The decay of the valence charge deformation at q ≫ q_BZ is [E]; the DFPT add-on of §10 decides it.
5. Non-perturbative anharmonicity (soft-mode or light-atom targets) lies outside (6.2). It is not needed for Si/Ge/GaAs (λ ≈ 0.01).
6. Amorphous targets: (2.1) needs configurational averaging, which is not covered here.
7. The G/X split (5.2) rests on the WP0 §6.2 Migdal amplitude ([D, sketch]). WP3 must confirm κ₃^X against its Migdal spectra.

---
## 13. Literature (IDs verified against the arXiv API, 2026-10-31; full text via lit.py; PDFs deleted)
[FT] 1712.06598 Eqs. (1)–(12); 1807.10291 Eqs. (29)–(31); 1910.08092 Eqs. (89)–(106); 2009.13534 (single-phonon rate and spin
responses); 1911.03482 Eqs. (1)–(44); 2205.02250 Eqs. (1)–(55); 2011.09477 Eqs. (7)–(12); 2309.10839 Eqs. (1)–(62); 2411.03433
Eqs. (1)–(30); 2607.24933 Eqs. (1)–(47); 2506.11191 Eqs. (63)–(73); 2607.06005 (ℓ = 0, 2 sections); hep-ph/0608035 Eqs. (1)–(11).
[ABS] 2412.18330. Classical results used without an arXiv source (flagged): Placzek moments; Sears expansion; Ambegaokar–Conway–Baym;
Gonze–Lee non-analytic dynamical matrix.

## 14. Symbols introduced/used (vs WP0 §10 NOTATION v2)

Conventions are followed as fixed: q is the momentum given to the crystal; n_q = Σe^{+iq·r}; S = (2π/V)Σ|⟨f|O_q|i⟩|²δ (WP0 (3.1));
HL units with e² = 4πα; the isotropic halo factor is η(v_min)/(2q). The halo numbers per 2105.00599 (ρ_χ = 0.3 GeV/cm³, v₀ = 238,
v_esc = 544 km/s) are not used numerically here. The only number used, v_max ≈ v_esc + v_E ≈ 800 km/s, is consistent with them.
**Flag:** NOTATION.md still lists ρ_χ = 0.4 GeV/cm³, which conflicts with the coordinator's 0.3.

| Symbol | Meaning | Status vs WP0 §10 |
|---|---|---|
| S_ab, S^G, R, R̃, ε, ε_e, 𝔇, 𝒱, O_a, n_κ^F, F^M_κ, F^Σ_κ, 𝐈_κ, j_κ, J_κ, Δ_χ | as in WP0 | used as defined |
| κ_BO, η_anh, x_R, W (2W = DW exponent), x_coh, τ_ph | small parameters | as WP0. **Deviation:** 2W_κ = q·B_κ·q in general (D2); x_coh is replaced as the control parameter by (n, c̄_L) (D1) |
| Q, ν, ω_{Qν}, e_{κν}(Q), n_{Qν} | phonon wavevector, branch, frequency, polarisation, Bose factor | NOTATION. In §2 the phonon wavevector is written k_i (several phonons) to keep Q free. **Minor deviation:** k is the electron crystal momentum in NOTATION; here k_i is a phonon wavevector, used only in §2–3 |
| s_i = ±1 | emission or absorption label | new |
| ℓ, L, r_κ, x⁰_{ℓκ}, u_{ℓκ} | lattice vector, separation, basis position, equilibrium site, displacement | new (standard) |
| f_κ(q) | per-species coupling strength (nucleon or charge) | new; maps to the c_s vector of WP0 (5.3) |
| ρ̄_e(q;R) | adiabatic electron density, (O′_e)_GG | new name for the WP0 Theorem D (ii) object |
| Δ_κ(q), 𝒵_κ(q) | valence/electron charge-response vector; total charge vertex (→ q·Z*_κ) | new |
| Z*_κ, Q_κ, ε∞, ε₀, ω_L, ω_T | Born charge, dynamical quadrupole, dielectric constants, LO/TO frequencies | new (standard) |
| p(q̂)_{κα}, D_A, D_NA | mode-charge vector, analytic and non-analytic dynamical matrices | new |
| B_κ | displacement tensor ⟨u_κu_κ⟩ | new |
| D_κ(ω), D_κ^{q̂}(ω), D^{ij}_κ(ω) | partial, projected and tensor phonon DOS (2411.03433 conventions) | new |
| μ_κ(q;ω′) | one-phonon measure (3.1) | new. **Collision risk:** μ_χe is the reduced mass; μ_κ always carries κ and (q;ω′) |
| ρ_κ(ω′\|q,ω) | final-state phonon spectrum (3.6) | new. **Collision risk** with ρ_χ, ρ_T, ρ_{mn}; always written with arguments |
| Φ_{κκ′}(L,t), Φ⁽³⁾, Φ⁽⁴⁾ | displacement correlator; anharmonic force constants | new. **Collision:** Φ₀ is the electronic ground state in WP0 §6.2. Proposal: force constants Φ⁽ⁿ⁾ always carry the superscript |
| c̄_L, j_BZ(r), z_L | shell displacement correlation, BZ form factor, shell coordination | new |
| κ₁…κ₄; κ₃^G, κ₃^X | ω-cumulants of S_self; G/X split | new. **Collision:** κ is also the species index and κ_BO. Proposal: rename the cumulants 𝔨_m in the reconciliation pass |
| n_κ(p), K_q̂, ⟨p²⟩ | nuclear momentum distribution; kinetic energy per direction | new. **Collision:** n_κ(q) is the density operator; n_κ(p) is always written with a momentum argument p. Proposal: rename it 𝔫_κ(p) |
| λ₃, λ₄, ω₀, ω̄, ⟨ω^{-1}⟩ | 2309.10839 anharmonic couplings, toy frequency, DOS moments | as in the source |
| A_ν(k,ω), Σ_ν | phonon spectral function and self-energy | new. **Collision:** Σ is also the summation sign and F^Σ. Proposal: Π^{ph}_ν |
| c_κ, P_κ, J_κ, g_κ, σ_{ℓκ} | isotope abundance, polarisation, nuclear spin, spin coupling, occupancy | new. **Collision:** J_κ^{ab} (spin-current) in WP0 (2.2) against the nuclear spin quantum number J_κ. Proposal: the quantum number becomes 𝒥_κ |
| S_HR | Huang–Rhys factor (= 2W in the lattice sector) | WP0 §10 |
| g(q,ω;x), P_ℓ, Y_ℓm, S_ℓm | halo Radon kernel (x = q̂·v̂_E), Legendre, harmonics, harmonic coefficients of S | new; g collides with the e–ph g of NOTATION, so the halo kernel always carries (q,ω;x). Proposal: 𝔤 |
