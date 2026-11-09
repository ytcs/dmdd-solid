# R16 / CW4: closure of the spin, superconducting, Dirac, low-dimensional, molecular and quantum-dot loose ends (LE-97 … LE-117)

Closure agent CW4, brief briefs/R16/CW4.md, 2026-11-01. Ledger: state/LOOSE-ENDS.md §1 rows LE-97…LE-117 (§2 group CW4).
Sources read: returns/R8/WP4-v3.md (cited "WP4 [n]"), returns/R12/WP7-B1-v2.md ("B1 (n)"), returns/R12/WP7-B2-v2.md ("B2 (n)"), returns/R13/WP8-U.md and
WP8-U-table.csv, LIMITS.md, CONVENTIONS.md (with the R8/R13 amendments), NOTATION.md, CONTROLS.md, code/ENV.md. No referee report was needed.
Checks: `code/CW4/checks.py`, **18/18 PASS in ≈ 3 s** (sympy exact algebra; scipy quadrature; numpy Colpa), cited CW4-Kn. No heavy job was run.
Literature (lit.py, literature/papers-CW4/, every arXiv ID verified by the fetch; PDFs deleted at the end): 1910.02091, 1603.05351, 2208.05967, 2212.04504,
1604.06800, 1509.01598, cond-mat/0108424 (journal ref and DOI from the arXiv API), 1805.06359, 2305.06084, 0706.4150 [FT]. Closed-access, checked at metadata
level only: Allen, PRB 3, 305 (1971) (DOI 10.1103/PhysRevB.3.305, Unpaywall "closed"); Hechster and Sarusi, JAP 122, 024302 (2017) (DOI 10.1063/1.4993123, "closed").
Tags: CONVENTIONS §12 ([D], [D, sketch], [E], [C]; [FT], [ABS], [UNVERIFIED]; [CALC] = value computed here with code/CW4). Status of everything new: CLAIMED.
Deliverable rule (STATEMENT, user 2026-11-01; coordinator note R16): a compute row closes with a derivation of the quantity and a specification written for
a reader. Each specification below therefore states, in prose: **what** is computed, **which approximation** (τ level) it embodies, the **method** (named by
the book's ab initio appendix: DFT, DFPT, Wannier/EPW, RPA/TDDFT/BSE, SCHA/TDEP, MD/MLIP, transport MC), the **key convergence parameters**, the **pitfalls**,
and the cost. Every QE/EPW stage is written for the qe-rtsc fork layout (code/ENV.md): inputs with the `@PSEUDO@` placeholder, SG15 ONCV v1.2 via
`rtsc/pseudo.sh` (`_FR` only with SOC), stages scf → nscf → (ph | epw | external response code) as in `rtsc/bench/run-fork.sh`; scratch in /root/work/<ID>/.

## 0. Closure table
| Row | Item (short) | Kind | Status | Where |
|---|---|---|---|---|
| LE-97 | RG1 GRPA vertex magnitude; WP5 R5 seed at q ≲ 1/ξ_coh | compute-formulate | **CLOSED** (quantity and quadrature specified; magnitude = exact gap) | §1 |
| LE-98 | RG2 amorphous WSi ε(q,ω), Δ_BCS inhomogeneity | compute-formulate | **CLOSED** (formulated) | §2 |
| LE-99 | RG3 two-magnon final-state interaction, bound states | theory | **CLOSED-AS-EXACT-GAP** | §3 |
| LE-100 | RG4 finite-q γ_OA, finite-q b^{NR} | compute-formulate | **CLOSED** (formulated) | §4 |
| LE-101 | RG5 finite-q multiplet transition densities (embedding) | compute-formulate | **CLOSED** (formulated) | §5 |
| LE-102 | RG6 Dirac targets at α̃ ≳ 1 | theory | **CLOSED-AS-EXACT-GAP** | §6 |
| LE-103 | RG8 non-dipole orbital form factors, SOC ions | compute-formulate | **CLOSED** (formulated) | §7 |
| LE-104 | RG9 [4.2′] remainder, edge, log at 2Δ; L^{BCS} table for Al | compute-formulate | **CLOSED** (resummed [4.2″] + table [CALC]); remainder **EXACT GAP** | §8 |
| LE-105 | RG10 re-plot of 1708.08929 / 1910.02091 reaches | compute-formulate | **CLOSED** (isotropic re-plot exact; anisotropic formulated) | §9 |
| LE-106 | ZrTe₅ "Δ" of 1910.02091 Table 1 | literature-check | **CLOSED** (Δ = half-gap Δ_D; "Exp. [52]" provenance not supported) | §10 |
| LE-107 | measured bulk Δ_BCS (Al, Nb) | data | Nb **CLOSED** [FT, secondary]; Al **CLOSED-AS-EXACT-GAP** | §11 |
| LE-108 | G-A2 Nambu second order, Eliashberg; Allen equation numbers | theory | derivation **CLOSED** ([D]); Allen eq. numbers **CANNOT-CLOSE** (closed access) | §12 |
| LE-109 | G-A6 impurity band; valley–orbit; impact of the 3q̃ misprint | compute-formulate | **CLOSED** (impact [E, CALC]; impurity band = exact gap with spec) | §13 |
| LE-110 | G-E10b 2208.05967 normalisation; depolarisation; Ref. [139] | theory | **CLOSED** (discrepancy stated exactly; Ref. [139] identified); depolarisation size = exact gap | §14 |
| LE-111 | G-E10a Förster coupling, R_QD ~ a_x, ligands | theory | **CLOSED** (formula + size; crossover and ligands formulated) | §15 |
| LE-112 | G-E5 CT excitons; Hückel/PPP vs BSE | compute-formulate | **CLOSED** (formulated) | §16 |
| LE-113 | G-E12 semiconducting-CNT 1D massive-Dirac RPA; OPW and FSI sizes | theory | **CLOSED** (formula [D]; sizes [E, CALC]) | §17 |
| LE-114 | G-I5 transverse row, anisotropic flux, impact on 2401.11971 | compute-formulate | **CLOSED** (exact ratio + bound; recast formulated) | §18 |
| LE-115 | G-X6 non-rigid Wannier correction; sign/normalisation of the restricted boost | theory | **CLOSED-AS-EXACT-GAP** (sign/normalisation and (W.5)-under-(H_W) derived; DFPT size specified) | §19 |
| LE-116 | S2 beyond Larmor; Larmor citation | compute-formulate | **CLOSED** (AFM closed form [D], LSWT spec; citation [FT]) | §20 |
| LE-117 | S6 longitudinal spin response from unpolarised neutrons | theory | **CLOSED-AS-EXACT-GAP** (no-go theorem [D]; routes specified) | §21 |
Counts: CLOSED 15 (incl. 2 with an exact-gap remainder), CLOSED-AS-EXACT-GAP 5, CANNOT-CLOSE 1 (the Allen equation-number part of LE-108 only).
**Results that change refereed text** (owed corrections at the end): LB1-10 upgrades (A2.2) from [D, sketch] to [D] (§12); LB1-5 gets an exact prefactor verdict
(§14); B2-L6 citation becomes [FT] and gains the AFM weight (§20); L16 "re-plot = RG10" is replaced (§9); WP4 I12 / WP4 §4.3 validity table is superseded by the
resummed form (§8); WP8-U rows for ZrTe₅, Al, Nb (§10–§11).

---
## 1. LE-97 (RG1): GRPA vertex correction in the DM region; WP5 R5 seed at q ≲ 1/ξ_coh
**Item.** WP4 [4.1]: R̃^{GRPA} = Π^N₃₃ + Π^N₃₂[Π^N₂₂(0,0) − Π^N₂₂(q,ω)]^{-1}Π^N₂₃. Only a bound O((Δ_BCS/v_Fq)²) ≤ 0.04 (Al), which is 2609.06423's, exists.
**The quantity [D].** Define the vertex fraction 𝔳_GRPA(q,ω) ≡ Im[R̃^{GRPA} − Π^N₃₃]/Im Π^N₃₃; then L^{GRPA} = L^{bare}(1 + 𝔳_GRPA) up to the change of Re ε, which is
the KK transform of the same Im correction (as in §8). In the clean quasiclassical limit (N(0) constant, T = 0, Fermi sphere), with ξ′ = ξ + v_Fqμ + q²/2m_e,
E = √(ξ² + Δ_BCS²), the Nambu bubble of vertices τ^N_i, τ^N_j is a two-dimensional integral,
  Π^N_ij(q,ω) = (N(0)/2)∫_{−1}^{1}dμ∫dξ [M_i*M_j/(ω − E − E′ + i0) − M_iM_j*/(ω + E + E′ + i0)],   M_i ≡ ⟨+,ξ′|τ^N_i|−,ξ⟩,                    (1.1)
with the Bogoliubov spinors |+⟩ = (u, v), |−⟩ = (−v, u). CW4-K1c gives the pair-creation factors: |M₃|² = ½[1 − (ξξ′ − Δ²_BCS)/(EE′)] (case I, density; = the
factor of 2609.06423 Eq. (7)), |M₂|² = ½[1 + (ξξ′ + Δ²_BCS)/(EE′)] (phase), M₃*M₂ mixed; M₀ = u′v − v′u (current, case II). Im parts follow from
δ(ω − E − E′) with no broadening; Re parts by a principal value. Π^N₂₂ is UV log-divergent, but only the difference Π^N₂₂(0,0) − Π^N₂₂(q,ω) enters, which is finite.
*Strongest derived statements.* (i) At q = 0 the vertex term cancels Π^N₃₃ exactly for every ω (WP4-K2: R̃^{GRPA}(0,ω) ≡ 0). (ii) The vertex is a pairing-channel
(n = 2, phase-mode) dressing of the (2,0) sector of WP4 Theorem D-g; it does not change the sector assignment of the final pair. (iii) WP5 R5 (seed at q ≲ 1/ξ_coh)
is empty for halo DM in clean Al: qξ_coh ≥ 2v_F/(πv_max) = 1.6 for ω ≥ 2Δ_BCS (WP4-K16), so (1.1) is needed only for qξ_coh ≥ 1.6.
**Missing step (single):** evaluate (1.1) for i, j ∈ {2, 3} on the DM region and form 𝔳_GRPA. **Specification (book appendix: response functions, "BCS bubbles").**
*What:* 𝔳_GRPA(q,ω) for Al on the WP4 [4.2] grid, y_BCS = ω/Δ_BCS ∈ [2, 50], qv_F/Δ_BCS ∈ [y_BCS v_F/v_max, 10³]. *Approximation:* τ = RPA in the Coulomb channel +
pairing ladder (GRPA), ref = BCS, clean, quasiclassical; this is the conserving rung above the bare bubble of 2609.06423. *Method:* 2-D quadrature of (1.1)
(Gauss–Legendre in μ; adaptive ξ with the δ-function roots solved analytically for Im; Re by subtraction of the pole); no ab initio input beyond (N(0), v_F,
Δ_BCS). *Convergence:* 𝔳_GRPA stable to 10⁻³ under doubling of both grids; ξ cutoff ≥ 10³Δ_BCS with the log divergence cancelled analytically.
*Validation:* reproduce WP4-K2 (R̃^{GRPA}(q → 0) → 0) and the bare 2609.06423 Eq. (7) when the ladder is switched off. *Pitfalls:* the sign of i0 on the second pole
(the source's time-ordered form equals the retarded one only at ω > 0, T = 0; WP4 §11A-2); Π^N₂₂(0,0) must be taken from the same cutoff (gap equation 2/g_pair),
otherwise the Goldstone cancellation fails and 𝔳 acquires a spurious constant. *Cost:* minutes on one core per 10³ grid points (fits the box; optional run).

## 2. LE-98 (RG2): amorphous WSi, ε(q,ω) and Δ_BCS inhomogeneity
**Item.** WP4 §4.5 (K31): RTA–Mermin is outside validity for WSi at q = 1–5 keV (k_Fℓ_mfp ~ 1, q ~ k_F, k_TF); no WSi correction exists.
**The quantity [D].** For a disordered target the rate needs the configurational average of the *loss*, not the loss of the averaged ε:
  S̄^{WSi}(q,ω) = (2q²/e²)⟨Im[−(ε^{-1})_{00}(q,ω)]⟩_conf/(1 − e^{−βω}),   L^{WSi,BCS}(q,ω) = ⟨∫dΔ P_Δ(Δ; r) 𝔤_I(ω/Δ) L^{nor}_loc(q,ω)⟩_conf,            (2.1)
where the second form holds when the superconducting correlation length exceeds the scale of Δ(r) fluctuations only partially: P_Δ is the local-gap distribution
from BdG, and the case-I factor is applied locally (Anderson theorem: disorder does not change the case-I form for ℓ_mfp ≪ ξ_coh, WP4 §4.5). (2.1) differs from
|⟨ε⟩|^{-2} Im⟨ε⟩ by the variance of ε over configurations, O(var ε/|ε|²); for qL_box ≫ 1 the average self-averages within one large cell.
**Specification (book appendix: MD/MLIP → DFT → RPA → BdG).** *What:* ⟨L⟩(q,ω) for q = 0.5–5 keV, ω = 2Δ_BCS–50 eV, and P_Δ. *Approximation:* τ = `nB=0|X=RPA+LFE|K=-`,
ref = glass (configurational average) for the normal state; ref = BCS(BdG, attractive-U) for the gap; clamped nuclei.
*Method.* (1) MD/MLIP: train a machine-learned potential (MACE or DeePMD) on DFT-PBE AIMD of 216-atom W_xSi_{1−x} (x ≈ 0.2–0.25, the film composition, [E]);
melt-quench 512–1000-atom cells at ≤ 10¹³ K/s; ≥ 5 independent quenches. Validate density and the W–Si/W–W radial distribution against film data.
(2) DFT (QE, SG15 W with 5s5p semicore, Si): scf at Γ + 2³ k on each quench (stage scf, nscf with ≥ 3× occupied bands). (3) Kubo–Greenwood σ₁(ω) as the
optical validation (against film ellipsometry/sheet resistance); (4) RPA+LFE ε_GG′(q,ω) (Yambo or BerkeleyGW on the nscf output): the supercell reciprocal
lattice (2π/L ≈ 0.5 keV for L = 25 Å) provides the q points directly, so no q-folding is needed beyond q ≈ 0.5 keV. (5) BdG on a Wannier tight-binding
model of each cell (Wannier90 from the nscf), attractive U fitted to the measured film T_c; output Δ(r) and P_Δ. *Convergence:* G-cutoff for ε_GG′ to q + 3 keV,
bands to ω_max + 30 eV; ⟨L⟩ stable to 5% across quenches (this is the error bar) and under 512 → 1000 atoms; f-sum per q to 2%. *Pitfalls:* quench-rate
dependence of the amorphous network (report it as a nuisance); the RTA/Mermin form must not be used anywhere (K31); semicore W states contribute at
ω ≳ 35 eV; local-field effects are large in a disordered cell, keep ε^{-1}_{00} (not 1/ε_{00}). *Cost:* MLIP training 10³ CPU-h; DFT 10³–10⁴ CPU-h per
quench; RPA 10⁴–10⁵ CPU-h total; BdG 10² CPU-h. GPU fork for the DFT stages; formulated only (over the box limits).

## 3. LE-99 (RG3): two-magnon final-state interactions and bound states
**Item.** WP4 [2.3]–[2.4] are non-interacting (LSWT to O(S⁰)); the magnon–magnon interaction and bound states in anisotropic magnets are open.
**Formula [D, given the Holstein–Primakoff expansion to quartic order].** The quartic HP (or Dyson–Maleev) terms give a two-magnon vertex Γ^{(4m)}_{q}(k,k′) of
relative order 1/(2|𝐒|). The interacting two-magnon response is the ladder (Bethe–Salpeter) resummation in the pair channel of total momentum q:
  S^{(2m)}_{αβ}(q,ω) = −2 Im[𝒜^{2m†}_α 𝒢₂(q,ω)(1 − Γ^{(4m)}_q 𝒢₂(q,ω))^{-1} 𝒜^{2m}_β]/(1 − e^{−βω}),   𝒢₂(q,ω)_{kk′} = δ_{kk′}/(ω − ω_{kν} − ω_{q−k,ν′} + i0),     (3.1)
with 𝒜^{2m} the WP4 [2.3] amplitude (a vector over pair labels). Bound states are the poles of (1 − Γ^{(4m)}𝒢₂)^{-1} below the continuum,
det[1 − Γ^{(4m)}_q𝒢₂(q,ω_b)] = 0, ω_b < min_k(ω_k + ω_{q−k}); their weight is the residue projected on 𝒜^{2m}. *Orders:* the two-magnon weight is O(S⁰) against the
one-magnon O(S); (3.1) corrects it at relative O(1/(2|𝐒|)), i.e. O(1/|𝐒|²) relative to the one-magnon line (the LE row's order). For a Heisenberg FM the
two-magnon density response stays zero at T = 0 (S^z_tot conserved, V^B ≡ 0, WP4 (a)), so bound states (Wortis type) are invisible to the density/spin-z
row unless anisotropy breaks the conservation; with easy-plane or biaxial anisotropy V^B ≠ 0 and they enter at O(D_an/J^{ex}).
**Exact gap.** Strongest statement: (3.1) and the bound-state condition, with the order counting above. Missing step: Γ^{(4m)} for a concrete target (YIG, NiO,
α-RuCl₃) and the solution of (3.1). **Specification (LSWT appendix, "beyond linear spin waves").** *What:* S^{(2m)}(q,ω) with ladder, bound-state energies
and weights. *Approximation:* ref = LSWT plus the 1/S pair ladder (no three-magnon decay, which is O(1/S) only for noncollinear order: then add the cubic
vertex). *Method:* exchange and anisotropy from DFT+U (QE, four-state energy mapping or TB2J on Wannier functions); quartic vertex symbolically from the
spin Hamiltonian; (3.1) on an N_k = 30³–40³ grid as a linear solve per (q, ω), or exact diagonalisation of the two-magnon sector for small cells as check.
*Convergence:* ⟨𝐒²⟩ sum rule to 1%; bound-state energy stable to 1% under N_k doubling. *Pitfalls:* the HP versus Dyson–Maleev vertices differ off shell but
agree on shell (use one); for |𝐒| = ½ (α-RuCl₃) the expansion is not controlled; the continuum edge needs fine k near the minima. *Cost:* ≈ 10² CPU-h (YIG,
20 sublattices); DFT+U inputs 10³ CPU-h.

## 4. LE-100 (RG4): finite-q optical activity and finite-q b^{NR}
**Item.** WP4 [3.2′]–[3.3] use γ_OA and b^{NR} at linear order in q (DFPT gyrotropy).
**The quantity [D].** For any q, split the current response S_{j^αj^β}(q,ω) = S^S + iS^A. For a chiral, T-even target the exact antisymmetric part is
S^A_{j^αj^β}(q,ω) = ε_{αβγ}𝒢^γ_OA(q,ω) with 𝒢_OA odd in q; γ_OA ≡ ∂𝒢_OA/∂q at q = 0 (WP4 §3.2). For P- and T-broken targets the density odd part is
S(q,ω) − S(−q,ω) = q_αq_β[S_{j^αj^β}(q,ω) − S_{j^αj^β}(−q,ω)]/ω² exactly (continuity), so b^{NR} at finite q is the odd part of the full current tensor.
The rate formulas WP4 [3.1]–[3.3] hold with these full functions in place of the linear forms; "beyond linear order" means O(q³) in 𝒢_OA and O(q⁵) in the density.
**Specification (RPA/TDDFT appendix, "current response with SOC").** *What:* 𝒢_OA(q,ω) and S_{j^αj^β}(±q,ω) for one chiral (e.g. Te or α-SiO₂) and one
magnetoelectric target, q up to 10 keV, ω ≤ 50 eV. *Approximation:* τ = `X=RPA+LFE` for the longitudinal part; transverse current response IP+LFE (WP1 rule);
SOC included (fully relativistic SG15 `_FR`). *Method:* DFT (QE, noncollinear) → current-vertex matrix elements ⟨k+q|{p + i[V_NL, r], e^{iq·r}}/2|k⟩ on
Wannier-interpolated states (EXCEED-DM-type IP code extended to the current vertex) → Dyson with LFE (Yambo) for the longitudinal channel. Linear-order
check against DFPT gyrotropy (Zabalo–Stengel, ABINIT). *Convergence:* odd part vanishes to noise in a centrosymmetric control (Si), k-mesh 16³–24³ until
the odd part changes < 5%. *Pitfalls:* the nonlocal-pseudopotential commutator is mandatory in the current vertex; gauge consistency of the Wannier
interpolation at ±q (CONVENTIONS §4); the campaign sign of q (CONVENTIONS §3) fixes the sign of the odd part. *Cost:* 2× the anisotropic G11 tables,
≈ 10³–10⁴ CPU-h per target.

## 5. LE-101 (RG5): finite-q multiplet transition densities for colour centres
**Item.** WP4 [6.3] needs ⟨³E|ñ_e(q)|³A₂⟩ and singlet transitions for NV⁻; KS orbitals do not give multiplet states.
**The quantity [D].** In an embedding (active-space) description with orbitals {φ_i} and many-body states |I⟩, |F⟩ (CI vectors), the transition density is
  ⟨F|n_e(q)|I⟩ = Σ_{ij∈act} γ^{FI}_{ij}⟨φ_i|e^{iq·r}|φ_j⟩ + δ_{FI}⟨n_e(q)⟩_env,   γ^{FI}_{ij} = ⟨F|c†_ic_j|I⟩ (spin-summed),                        (5.1)
and the screened vertex is WP4 [6.1] with (ε^{-1}_host)_{G0}. The spin-flip (³A₂ → ¹E) amplitude uses the spin-density analogue with γ^{FI,σσ′}; it is ∝ q·r_tr
at small q (WP4 §6). Environment orbitals contribute only through screening at this order (the active-space projector is the hypothesis).
**Specification (embedding appendix: DFT → QDET/CRPA → CI).** *What:* |⟨F|ñ_e(q)|I⟩|² on |q| ∈ [0.5, 30] keV × 590 directions for the NV⁻ manifold (³A₂, ³E, ¹A₁,
¹E). *Approximation:* τ `X=BSE`-equivalent within the active space, ref = def(cr); Condon (vibronic dressing from WP4 [6.3] separately). *Method:* DFT (QE, PBE
then HSE) on a 512–1000-atom supercell; WEST QDET (or CRPA) effective Hamiltonian on 4–6 defect orbitals; full CI; new module: γ^{FI} × plane-wave form
factors of the KS orbitals (FFT on the real-space grid, Δr ≤ π/q_max). *Convergence:* multiplet energies to 0.05 eV against the ZPL and ¹E–¹A₁ data;
|⟨F|n(q)|I⟩|² stable to 5% under active-space enlargement and supercell 512 → 1000. *Pitfalls:* double counting of the screened interaction in QDET; the orbital
relaxation between ³A₂ and ³E (use common orbitals, or a biorthogonal correction); spin contamination of KS orbitals; the PAW augmentation term is not
needed with SG15 norm-conserving pseudopotentials but the q_max must stay below the pseudisation cutoff (≈ 25 keV for C). *Cost:* 10⁵ CPU-h (HSE + WEST).

## 6. LE-102 (RG6): Dirac targets at α̃ ≳ 1
**Item.** WP4 §5 is one-loop RPA; at the 1708.08929 benchmark α̃ = αg_deg/(ε_bgv_F) = 0.91.
**Strongest derived statements [D].** (i) The one-loop corrections beyond RPA are the self-energy (Fermi-velocity renormalisation, logarithmic in the cutoff)
and the vertex (excitonic) ladder; each is O(α̃) relative to RPA, and they partially cancel in conserved quantities (Ward identity for the density vertex), so the
f-sum is untouched at every order. (ii) Near threshold the ladder is the Elliott–Sommerfeld problem of a massive Dirac pair: for |𝓈 − 4Δ²_D| ≪ Δ²_D the pair is
non-relativistic with reduced mass Δ_D/(2v_F²) and Coulomb coupling α/ε_bg, so the bound series has Rydberg
  Ry_D = (Δ_D/(2v_F²))(α/ε_bg)²/2 = Δ_D(α̃/g_deg)²/4,                                                                                   (6.1)
and the continuum gains the Sommerfeld factor 𝒮_F^D of WP4 §5.4 (ii). CW4-K10: Ry_D = 0.052Δ_D at the benchmark; for ZrTe₅ (Δ_D = 11.75 meV, v_F = 1.3×10⁻³ along x,
isotropised ε_bg = 25.3, α̃ = 0.44) Ry_D ≈ 0.15 meV [E]. (iii) Hence the excitonic correction is confined to |√𝓈 − 2Δ_D| ≲ few Ry_D, while away from threshold
the correction is O(α̃) with an uncontrolled coefficient. (iv) At α̃ ≳ 1 WP4 Theorem D-g (c) already says the sector split is not unique (only totals are quotable).
**Missing step:** a non-perturbative (self-consistent GW + BSE, or functional-RG) evaluation of L at α̃ ~ 1. **Specification (GW/BSE appendix).** *What:* L(q,ω)
for the anisotropic massive Dirac model of ZrTe₅ (k·p within Λ_D, ε_bg tensor, v_F,i), then ab initio check. *Approximation:* 𝒳 = BSE on top of GW-renormalised
Dirac bands; static ε_bg plus the RPA Dirac polarisation in W. *Method:* model level: BSE on a k-grid inside Λ_D (≈ 60³ points, two bands), cost CPU-minutes;
ab initio: QE + Yambo G₀W₀ + BSE with SOC for the 12-atom cell, k ≥ 24³ near Γ (non-uniform grid). *Convergence:* Ry_D and the first BSE peak to 5%; k-grid
must resolve 1/a_D = Δ_D/(v_F) × α̃/g scale. *Pitfalls:* the cutoff scheme (WP4 §5.4 (i)); double counting of ε_bg if remote bands are also in the GW W;
the ionic ε_bg(ω) near polar phonons. *Cost:* model negligible; ab initio 10⁴–10⁵ CPU-h.

## 7. LE-103 (RG8): non-dipole orbital magnetic form factors for SOC ions
**Item.** WP4 §2.1 (iv), B2 (B2.6.1): λ_{L,j} ≠ 0 ions need orbital form factors beyond the dipole ⟨j₀⟩ + c₂⟨j₂⟩ approximation.
**The quantity [D].** With e^{iq·r} = 4πΣ_{K}i^Kj_K(qr)Σ_QY*_{KQ}(q̂)Y_{KQ}(r̂), the single-ion spin and orbital operators within a (J, M_J) multiplet reduce by
Wigner–Eckart to radial integrals ⟨j_K(q)⟩ = ∫r²dr R_{nℓ}(r)²j_K(qr) times reduced matrix elements:
  ⟨JM′|Σ_i e^{iq·r_i}(λ_S s_i + λ_L ℓ_i)|JM⟩ = Σ_{K even ≤ 2ℓ} Σ_{K′ = K±1} ⟨j_{K}(q)⟩ 𝒞^{(ℓ,J)}_{KK′}[Y_K(q̂) ⊗ 𝐉^{(K′)}]_{M′M},                (7.1)
where 𝒞 are 6j/9j coefficients (Balcar–Lovesey tensor form [UNVERIFIED]; the structure, not the citation, is what is derived: K ≤ 2ℓ = 6 for 4f, the orbital
current brings odd K′). The dipole approximation keeps K = 0, 2 with K′ = 1. Beyond it, q-direction-dependent terms appear at q ≳ 1/⟨r⟩_4f ≈ 3 keV.
**Specification (atomic/DFT appendix).** *What:* ⟨j_K(q)⟩, K = 0…6, and the multiplet-projected matrix elements (7.1) for the SOC ions of the WP8-U survivors.
*Approximation:* single-ion, ground J multiplet, crystal field as a perturbation within J; τ ref = LSWT downstream. *Method:* radial functions from Dirac–Fock
(GRASP) or from DFT+U Wannier projections (QE + Wannier90, fully relativistic `_FR`); Racah algebra symbolic (sympy.physics.wigner). *Convergence:* ⟨j₀(0)⟩ = 1,
sum rules of the orbital moment to 10⁻³; agreement with tabulated dipole form factors to 2% for q ≤ 1 keV. *Pitfalls:* the DM-side operator for λ_L couples to
the orbital current, not to ℓ times the density (keep the 𝒪-basis ordering of WP0 (2.2)); crystal-field mixing of J multiplets in light rare earths.
*Cost:* < 10 CPU-h per ion.

## 8. LE-104 (RG9): [4.2′] beyond the first-order sketch; L^{BCS} for Al
**Item.** WP4 [4.2′] is a first-order expansion that fails for y_BCS ≲ 3.5 at the kinematic edge; remainder, edge and the log at 2Δ_BCS are open.
**Derivation: resummed form [4.2″] [D, quasiclassical clean hypotheses of WP4 §4.3].** WP4's KK of δIm ε gives the exact (within the model) real part
Re ε^{BCS} = Re ε^{nor} + (k_TF²/q²)(Δ_BCS/qv_F)𝔰_BCS(y_BCS); nothing requires expanding |ε^{BCS}|^{-2}. With 𝔯 ≡ Im ε^{nor}/Re ε^{nor} and
δ_𝔰 ≡ (k_TF²/q²)(Δ_BCS/qv_F)𝔰_BCS/Re ε^{nor},
  L^{BCS} = 𝔤_I L^{nor} · (1 + 𝔯²)/[(1 + δ_𝔰)² + 𝔤_I²𝔯²],                                                                                   (8.1)
which reduces to WP4 [4.2′] at first order in δ_𝔰 and 𝔯 → 0. It is positive and bounded for all y_BCS > 2, so the "uncontrolled" region of WP4 I12 becomes a
controlled resummation. Two corrections the first-order table missed: (a) at the edge ω/(qv_F) = v_max/v_F = 0.39, 𝔯 = (π/2)(0.39)/Re 𝔣_Lin = 0.73 is not small;
(b) Re 𝔣_Lin = 1 − (x/2)ln[(1 + x)/(1 − x)] = 0.84 at x = 0.39 (WP4 §4.5 bracket), so Re ε^{nor} = 0.84k_TF²/q² there (WP4-K34 used 1). The 𝔤_I²𝔯² term
lowers L even at Δ_BCS/qv_F → 0, because the case-I step raises Im ε in the denominator.
**Table [CALC, code/CW4 K2]: L^{BCS}/(𝔤_I L^{nor}) at the Al edge q = ω/v_max** (v_max/v_F = 0.39); "KK ∞" integrates Im ε ∝ ω′ to infinity, "cut" stops at
ω′ = qv_F (the two bracket the unknown Im ε^{nor} above qv_F):
| y_BCS | 2.2 | 2.5 | 3 | 5 | 10 |
|---|---|---|---|---|---|
| 𝔰_BCS(y) | 4.01 | 2.82 | 2.03 | 1.05 | 0.50 |
| WP4 first order, \|δL/L\| | 1.42 | 0.88 | 0.53 | 0.16 | 0.04 |
| (8.1), KK ∞ | 0.33 | 0.45 | 0.58 | 0.80 | 0.94 |
| (8.1), cut | 0.40 | 0.54 | 0.66 | 0.86 | 0.96 |
Away from the edge every deviation scales down as ω/(qv_max). *The log at y = 2:* 𝔰_BCS diverges logarithmically from the π/2 step of 𝔤_I, so δ_𝔰 → ∞ and
L^{BCS} → 0 as 1/ln²|y − 2| at threshold: the threshold step of Im ε is screened away in L. This is a property of the clean quasiclassical model.
**Exact remaining gap.** Strongest statement: (8.1) with the table. Missing step: the O(Δ²_BCS/q²v_F²) corrections to Im ε^{BCS} itself (the ξξ′ averaging near
|μ| ≈ ω/qv_F) and the true Im ε^{nor} for ω′ ≳ qv_F in the KK. **Specification (response appendix).** *What:* full Im ε^{BCS}(q,ω) from (1.1) with i = j = 3 (and
the GRPA vertex of §1), its KK transform, and L^{BCS} on the WP4 [4.2] grid. *Approximation:* clean BCS, RPA(+GRPA), quasiclassical, Lindhard normal state
including ω′ > qv_F. *Method:* the §1 quadrature plus a KK on a log grid to ω′ = 10³ qv_F. *Convergence:* KK tail < 10⁻³ of Re ε; table entries to 1%.
*Pitfalls:* KK must use the conserving (no-weight-above-qv_F only in the clean limit) Im ε; mixing the bare and GRPA bubbles between Im and Re breaks
positivity. *Cost:* CPU-minutes (fits the box; optional run). Nuisance consequence: replace WP4 I12's "one-sided, exclude y ≲ 3.5" by "(8.1) with the KK-∞/cut
spread as a type-Δ nuisance".

## 9. LE-105 (RG10): re-plot of the 1708.08929 / 1910.02091 reaches
**Item.** LIMITS L16 "re-plot = RG10": apply ε_bg² (scattering), ε_bg (absorption) and the 0.55–0.62 charge renormalisation.
**Derivation [D].** WP4 [5.3]: Rate_src/Rate_URF = ε_bg² exactly, for any δε_D, *with the source's own |ε_r|²*; [5.5]: Γ_abs,src/Γ_abs,URF = ε_bg (CW4-K9). For a
background-free Poisson limit the excluded cross-section scales as 1/rate, so for the isotropic model of 1708.08929 the corrected curves are exact vertical shifts:
  σ̄_e,lim^{URF}(m_χ) = ε_bg² σ̄_e,lim^{src}(m_χ)  (×1600 at ε_bg = 40, ×640 for the isotropised ZrTe₅ curve, 3.2 and 2.8 decades);
  κ_mix,lim^{URF}(m_φ) = √ε_bg κ_mix,lim^{src}(m_φ)  (×6.3 at ε_bg = 40; ×5.0 for ε_bg = 25.3).                                                  (9.1)
**Where the 0.55–0.62 applies.** The sources keep Re δε_D (1708.08929 Eq. (2.6) has the log), so their |ε_r|² already contains the charge renormalisation, and
(9.1) must **not** be multiplied by 0.55–0.62. That factor (WP4 §5.4 (i)) belongs only to a recomputation that uses the campaign's leading form [5.1],
L → Im δε_D/ε_bg² (Re δε_D dropped): such a curve must be multiplied by 0.55–0.62 (cutoff-scheme spread) in rate. Using both would double count.
**Anisotropic 1910.02091 (formulated).** Their F_med is the per-component rule; URF is [5.2], ε = q̂·ε_bg·q̂ − v_CR̃_D. The ratio is not constant in q̂, so the
corrected limit is σ̄_lim^{URF} = σ̄_lim^{src}·N_src/N_URF with N the event integrals. *What:* N_URF and N_src (daily-modulation resolved) for ZrTe₅, BNQ-TTF,
Yb₃PbO with the source inputs (their Tables 1–2, exposure 1 kg·yr). *Approximation:* their model (k·p Dirac within Λ_i, RPA, static ε_bg tensor), only the
screening rule changed; campaign halo optional as a second curve. *Method:* direct re-implementation of their Eqs. (3.13)–(3.14) with the vertex 1/ε replaced by
[5.2]; 3-D q integral (Lebedev 590 directions × log |q|) and ω integral. *Convergence:* reproduce their published curve with their rule to 5% first (this
validates the integrator), then swap the rule. *Pitfalls:* their typo q_x²v_{F,z}² (use v_{F,x}); off-diagonal κ_ij of Table 2 (keep or state dropped);
the half-gap reading of §10. *Cost:* CPU-minutes (fits the box). On axis the factor is (ε_bg,ii)²: 9.5×10⁴, 431, 1.6×10⁴ for i = x, y, z (Table 2).

## 10. LE-106: ZrTe₅ "Δ" in 1910.02091 Table 1
**Reading [FT 1910.02091].** Eq. (1.1) (p.2): E_k± = ±√(v_F²k² + Δ²), "2Δ is the band gap". p.12, text below Table 1: "The calculated band gap with and without
structural optimization are given by 31.2 meV and 23.6 meV, which corresponds to Δ = 15.6 meV and Δ = 11.8 meV", and Table 1 lists exactly 15.6 (ISIF7) and 11.8
(NR) in its "∆ (meV)" column. Hence the column is the **half-gap Δ_D** (NOTATION ⚠ Δ_D), and the caption's "band gaps" is loose wording (CW4-K14). The
"Exp. [52]" entry 11.75 meV sits in the same column, so it is read as Δ_D = 11.75 meV (E_g = 23.5 meV).
**Provenance finding [FT 1603.05351 = their Ref. [52], Zheng et al., PRB 93, 115414].** [52] is a transport (SdH) paper: Table I gives F, k_F, m_eff, v_F, τ, ℓ,
μ per plane, and p.8 gives m* = 0.026m_e, v_F = 4.89×10⁵ m/s and "the estimated Fermi level E_F is about 35.4 meV" (page image read); no gap value appears
(no "gap" or "meV gap" in the text). So the 11.75 meV attributed to [52] is not supported by [52]. **Closure:** use Δ_D = 11.8 meV [FT, 1910.02091 p.12, DFT
experimental structure] as the documented value; record 11.75 meV as "attributed to [52], not found there [UNVERIFIED]". The two agree to 0.4%, so no Dirac
FOM changes; only the provenance tag does.

## 11. LE-107: measured bulk Δ_BCS for Al and Nb
**Nb [FT 1805.06359 p.3, secondary].** "a broad distribution of ∆ values peaked at the accepted bulk Nb ∆_Nb, between 1.5 and 1.61 meV depending on the
crystalline orientation" (their Ref. 20), with T_c = 9.25–9.3 K "typical of bulk niobium" (p.5). Value: **Δ_BCS(Nb) = 1.50–1.61 meV** (orientation), a review-level
[FT] quote, not a primary measurement in that paper. Consistency: 2Δ/k_BT_c = 3.75–4.0 (strong coupling, as expected for Nb).
**Al.** [FT 2305.06084 p.1–2]: bulk Al T_c = 1.2 K ("converges to the value for bulk Al (1.2 K) for thicker films"). With the weak-coupling BCS ratio Δ = 1.764k_BT_c
(Al is weak coupling, λ_ep ≈ 0.4 [E]) this gives **0.18 meV** (0.179 meV at T_c = 1.175 K) [D from FT T_c; CW4-K14]. Film gaps are larger: Δ_30 nm = 209 μeV
[FT 0706.4150 p.7], and thin films enhance T_c (2305.06084). **Finding:** the WP8-U table value 0.3 meV [FT 2109.04473 p.2] is ≈ 1.7× the bulk value; WP4 §4.3
already uses 0.17 meV (consistent with bulk). 2109.04473's thresholds (2Δ = 0.6 meV) are therefore not bulk-Al thresholds. **Exact gap (Al):** a primary [FT]
tunnelling or far-IR measurement of bulk Al Δ(0) was not located by the searches (arXiv: "aluminum superconducting gap tunnel", "bulk aluminium energy gap");
the strongest statement is the [FT] T_c plus the BCS ratio; the missing step is one primary citation (classic tunnelling values 2Δ/k_BT_c ≈ 3.4–3.5 [UNVERIFIED]).

## 12. LE-108 (G-A2): the superconducting Holstein process by explicit Nambu second order; strong coupling; Allen equation numbers
**Item.** B1 (A2.2) rests on an off-shell T-parity argument [D, sketch].
**Hypotheses.** (h1) Dark-photon (or photon) absorption at k_φ → 0 through the paramagnetic current j = Σ_kσ v_k c†_{kσ}c_{kσ} (the diamagnetic term is O(A²));
(h2) mean-field BCS reference, T = 0; (h3) one-phonon e–ph vertex g_{k+Q,k} real and T-even, g_{k+Q,k} = g_{−k,−k−Q} (density-type, CONVENTIONS §5);
(h4) Fermi-surface approximation: v_k and g depend on the Fermi-surface angles only over the ξ range ~ ω; (h5) bare vertices on the final pair (the GRPA
pair-channel dressing is O(Δ²_BCS/(v_FQ)²), §1).
**Derivation [D].** (a) In Nambu form the q = 0 current of the pair (k↑, −k↓) is v_kτ^N_0 because v_{−k} = −v_k, so [j, H_BCS] = 0 exactly (CW4-K1a): j is diagonal
in the Bogoliubov basis, each quasiparticle carries v_k(u_k² + v_k²) = v_k, and j has no pair-creation part (case II at q = 0 vanishes, K1b). (b) Hence the
second-order T-matrix has only the two time orderings with j acting on eigenstates: absorbing first gives J_i⟨f|H_ep|i⟩/ω, emitting the phonon first gives
⟨f|H_ep|i⟩J_f/(−ω), with J the current eigenvalues. The amplitude to |f⟩ = γ†_{k+Q↑}γ†_{−k↓}b†_{−Q}|BCS⟩ is therefore exactly
  T_fi = −(ê·(J_f − J_i)/ω)⟨f|H_ep|BCS⟩ = −(ê·(v_{k+Q} − v_k)/ω) g_{k+Q,k}(u_{k+Q}v_k + v_{k+Q}u_k),                                          (12.1)
with no requirement that intermediate states be off shell by ≫ Δ_BCS. (c) The e–ph vertex is density-type (h3), so its pair-creation factor is case I (K1c):
|u′v + v′u|² = ½[1 − (ξξ′ − Δ²_BCS)/(EE′)]. (d) Integrating ξ and ξ′ at fixed E + E′ = x = ω − ω_ph (the ξξ′ term is odd and drops) gives
∫dE (EE′ + Δ²_BCS)/√((E² − Δ²_BCS)(E′² − Δ²_BCS)) = x𝔤_I(x/Δ_BCS) = xE(√(1 − 4Δ²_BCS/x²)) (K1d, modulus form), while the Fermi-surface average of
|ê·(v_{k+Q} − v_k)|²|g|² gives the transport function α²F_tr, exactly as in the normal state. This is B1 (A2.2), now [D] under (h1)–(h5); Δ_BCS → 0 gives (A2.1).
The elastic (impurity) limit differs because the impurity vertex is not paired with a current eigenvalue difference: there j itself must create the pair at
q ≠ 0 (case II, Mattis–Bardeen), consistent with B1 §9.
**Strong coupling [D, sketch].** Replacing the BCS spinors by Eliashberg spectral functions, the pair weight becomes ∫dE[N_s(E)N_s(E′) + P_s(E)P_s(E′)] with
N_s = Re[E/√(E² − Δ(E)²)], P_s = Re[Δ(E)/√(E² − Δ(E)²)] (the case-I combination; case II has the minus sign), plus the mass renormalisation 1/(1 + λ_tr) in the
current eigenvalues. **Specification (Wannier/EPW appendix).** *What:* σ₁^{S,(2,1)}(ω) of Al and Nb with the Eliashberg form. *Approximation:* n_g = 2, sector (2,1),
isotropic Eliashberg (anisotropic for Nb optional). *Method:* QE scf/nscf → ph (q 8³) → EPW (k 60³ / q 30³ fine, Al; 40³/20³, Nb) for α²F and α²F_tr; real-axis
isotropic Eliashberg (EPW `eliashberg`, Padé or direct real-axis); then the (A2.2) integral with N_s, P_s. *Convergence:* T_c within 10% of experiment with one
μ*; σ₁ stable to 5% under fine-grid doubling. *Pitfalls:* Padé continuation artefacts near 2Δ; use the transport (1 − cos θ) weight, not α²F. *Cost:* 10³ CPU-h (GPU fork).
**Allen (1971) equation numbers: CANNOT-CLOSE.** Allen, PRB 3, 305 is closed access (Unpaywall "closed"; not on arXiv). 1604.06800 cites it as Ref. [29] without
equation numbers ("Following Ref. [29]", p.4) [FT]. The owed text cites Allen (1971) as a paper, with no equation numbers.

## 13. LE-109 (G-A6): impurity band, valley–orbit lines, impact of the 2212.04504 Eq. (12) misprint
**Misprint impact [E, CALC; CW4-K5].** Eq. (12) prints (3q̃ + k̃² + 1); the hydrogenic GOS has (3q̃² + k̃² + 1) (B1 C10, REFEREED). Hypotheses: their Si:P
parameters (E_I = 45 meV, m* = 0.3m_e, a* = 23 a.u.), |ε| held fixed (they use a Lindhard host ε(q,ω)), campaign SHM halo. Ratio of the scattering rate
evaluated with the printed bracket to the correct one:
| m_χ (MeV) | 0.02 | 0.1 | 1 | 10 |
|---|---|---|---|---|
| heavy mediator | 1.47 | 0.91 | 0.59 | 0.56 |
| light mediator | 1.46 | 1.24 | 1.07 | 1.06 |
So the printed formula overstates the reach near threshold (q̃ < 1) and understates it by up to ×1.8 for heavy mediators at m_χ ≳ 1 MeV (q̃ > 1). If their
numerics used the printed Eq. (12), their Fig. 2 scattering curves move by these factors (the absorption limit, q̃ → 0, is unaffected).
**Valley–orbit lines [D, EMT].** With ψ_s = Σ_ι α^s_ι F_ι(r)φ_{k_ι}(r) (six Δ valleys; A₁, E, T₂ combinations α^s),
  ⟨s′|e^{iq·r}|s⟩ = Σ_{ιι′} α^{s′*}_{ι′}α^s_ι Σ_G 𝒰_{ι′ι}(G) F̃_{ι′ι}(q + k_ι − k_{ι′} + G),                                                       (13.1)
with 𝒰_{ι′ι}(G) the Bloch-overlap coefficients at the valley minima and F̃ the envelope product transform; intravalley terms are at q ≲ 1/a*, intervalley
(g, f) terms at q ≈ |k_ι − k_ι′| ≈ 2–3 keV, reachable by MeV DM. The 1s(A₁) → 1s(E, T₂) lines are not optical (q → 0) transitions but are allowed at finite q.
**Impurity band (exact gap).** At n_D/n_c ≈ 0.5 the dilute (1.2) of B1 fails at O(1) near the edge. Strongest statement: (13.1) per centre plus B1 (A6.1);
missing step: the disorder-averaged S(q,ω) of a random donor ensemble. **Specification (tight-binding/DFT appendix).** *What:* ⟨S^D(q,ω)⟩ for Si:P at
n_D = 10¹⁸ and 1.8×10¹⁸ cm⁻³. *Approximation:* multivalley EMT orbitals on random sites (Poisson positions), Hubbard–Anderson Hamiltonian with
hopping from envelope overlaps, Hartree mean field; host screening as in (1.2). *Method:* exact diagonalisation of N = 10⁴–10⁵ sites (Lanczos/kernel polynomial)
per realisation, 100 realisations; cluster check by DFT supercells (QE, 1000–4000 Si atoms, 2–4 P) for the central-cell term. *Convergence:* S to 5% under N
and realisation count; TRK sum per donor. *Pitfalls:* valley interference makes hopping oscillate with distance (do not use a single-valley envelope); compensation
changes the occupation. *Cost:* 10³ CPU-h (TB); DFT clusters 10⁴ CPU-h. The impact number with their Lindhard ε: same K5 integral with their ε(q,ω) (minutes).

## 14. LE-110 (G-E10b): 2208.05967 normalisation, depolarisation, Ref. [139]
**Source equations [FT 2208.05967 p.5–6].** Eq. (6) dR_ex/dlnE_r = (N_tρ_χσ̄_e/(8m_χμ_eχ))∫qdq η|F_DM|²|f_QD|²; Eq. (10) |f_QD|² = Σδ(E_r − ΔE)|∫d³r e^{−iq·r}Ψ*_fΨ_i|²
(dimension E⁻¹); Eq. (12) |f_QD|² = (2π²/(E_rαm_e²V_cell))Σ∫V_cell²d³kd³k′/(2π)⁶E_rδ(…)Σ_{G′}qδ(q − |k′ − k + G′|)|f|², which is **identical** to 1509.01598
Eq. (3.17) |f_crystal|² (dimensionless) [FT 1509.01598 pp.13–14].
**Reconciliation [D] (CW4-K6).** From WP0 (9.2) per cell, with Eq. (10)'s normalisation (direction-averaged, spin as defined), the correct rate is
  dR/dlnE_r = N_t E_r ρ_χσ̄_e/(2m_χμ²_eχ) ∫ q dq η F²_DM ⟨|f_QD|²⟩_{q̂},                                                                       (14.1)
which is 1912.02822 Eq. (19) (B1 §2; spin counting as in Eq. (10), a factor-2 convention immaterial against the mismatch below), and with Eq. (12)'s normalisation it is 1509.01598 Eq. (3.13):
  dR/dlnE_r = N_t(ρ_χ/m_χ)σ̄_e α (m_e²/μ²_eχ) ∫ dq (E_r/q²) η F²_DM |f_QD|²_{Eq.(12)}.                                                          (14.2)
The printed Eq. (6) agrees with neither: with Eq. (10) it exceeds (14.1) by **μ_eχ/(4E_r)** (≈ 4×10⁴ at m_χ = 10 MeV, E_r = 3 eV); with Eq. (12) it has mass
dimension 2 instead of 1 (dimensionally inconsistent). Since the paper says its rates are "taken from more precise numerical codes" (QEdark, Ref. [5]) and Fig. 4
compares bulk Si/Ge/PbS rates, the plotted numbers are presumably from (14.2) [E]; Eq. (6) is then a typographical defect of the printed formula, not of the
numerics. *Check spec:* reproduce Fig. 4's bulk Si curve (m_χ = 10 MeV, σ̄_e = 10⁻³⁷ cm²) with QEdark tables in (14.2), seconds.
**Ref. [139] [metadata level].** E. Hechster and G. Sarusi, J. Appl. Phys. 122, 024302 (2017), DOI 10.1063/1.4993123, "Modeling the PbS quantum dots complex
dielectric function by adjusting the E-k diagram critical points of bulk PbS" (Crossref/Unpaywall; closed access). So the ε of their Eq. (16) is a **modelled
intrinsic** dot-material ε_in(ω) (a size-adjusted bulk model), not a measured film or composite ε. This confirms that the missing factor is the dot
depolarisation, B1 (E10.3): Γ_abs per dot = (κ_mix²σ_A/|ε_in|²)·9|ε_in|²/|ε_in + 2ε_out|².
**Depolarisation sign criterion [D] (K6).** With ε_in = ε₁ + iε₂ and real ε_out: the factor exceeds 1 iff |ε_in|² > (ε_out/2)(ε₁ + ε_out). **Exact gap:** its size over
2.5–10 eV needs ε_in(ω) of the actual dots (closed source). Spec: digitise or recompute ε_in(ω) (Hechster–Sarusi model, or DFT+GW-BSE for a 3–5 nm PbS cluster,
10⁴ CPU-h) and evaluate the factor; minutes once ε_in is in hand.

## 15. LE-111 (G-E10a): inter-dot Förster coupling, R_QD ~ a_x, ligand states
**Förster coupling [D, dipole–dipole, quasi-static].** For dots at separation R_dd ≫ R_QD in a matrix ε_out, the excitonic coupling (HL units, e² = 4πα) is
  J_F = α 𝔣^{loc 2}_1 [𝐝₁·𝐝₂ − 3(𝐝₁·R̂)(𝐝₂·R̂)]/(ε_out R³_dd),   𝔣^{loc}_1 = 3ε_out/(ε_in + 2ε_out),                                                 (15.1)
with 𝐝 the band-edge transition dipole (length). Effect on S: the coupled dots form a collective exciton band of width ~|J_F|; by the B1 (E5.2′) binning lemma,
transposed to dots, the ω-integrated S over a bin wider than |J_F| is unchanged up to O((J_F/ΔE_level)²). Size [E, K13]: d = 0.3 nm, R_dd = 6 nm, ε_out = 2.5,
ε_in = 17: J_F ≈ 6×10⁻⁵ eV, far below level spacings (~0.1 eV) and any bin. **Förster is negligible for S**; it matters for WP5 readout (energy transfer to the
largest dots, a red shift of emission), where the transfer rate ∝ J_F² is a WP5 input.
**R_QD ~ a_x crossover (formulated).** Strong confinement (R_QD ≪ a_x) is B1 (E10.1); weak confinement (R_QD ≫ a_x) quantises the exciton centre of mass,
E = E_g − E_x^b + π²/(2M_xR_QD²), with form factor ρ^{cell}_cv(q)·F̃_COM(q)·φ_x(0)-type factorisation. PbS (a_x ≈ 18 nm [UNVERIFIED], R_QD = 1.6–2.5 nm) is deep in the
strong regime (R/a_x ≈ 0.1–0.15), so (E10.1) applies to 2208.05967's dots. For R/a_x ~ 1 (e.g. CdSe 5 nm), *spec:* configuration-interaction (or BSE) in the
EFA basis of B1 §5 (ℓ ≤ 6, n ≤ 6 single-particle states, Coulomb with dielectric confinement (E10.2)), output E_f and ⟨f|ñ_e(q)|0⟩; convergence of E_x to 1 meV
in the basis; cost CPU-hours. **Ligand states (formulated):** treat ligand/surface states as additional centres in (1.2) with their own transition densities;
atomistic DFT of a passivated cluster (≤ 2000 atoms, QE/CP2K) gives their energies and q-form factors; pitfall: surface-state energies are functional-dependent
(use hybrid or GW corrections); cost 10⁴ CPU-h.

## 16. LE-112 (G-E5): charge-transfer excitons; Hückel/PPP versus BSE
**The quantity [D, two-state model].** With Frenkel state |F⟩ (energy E_F) and CT state |C⟩ (E_C) coupled by t_CT = t_e + t_h (electron- and hole-transfer
integrals, ∝ intermolecular overlap), the eigenstates are |±⟩ with mixing tan 2θ_CT = 2t_CT/(E_C − E_F), and
  f_±(q) = cos θ_CT f_F(q) ± sin θ_CT f_C(q),   f_C(q) = ⟨C|n_e(q)|0⟩ = O(S_HL)·(e^{iq·r_𝔬} − e^{iq·r_𝔬′})-weighted,                                (16.1)
where S_HL is the HOMO(𝔬)–LUMO(𝔬′) overlap. CT corrections to S are therefore O(θ²_CT) in line weight (intensity borrowing) plus new lines at E_C with
weight O(S²_HL + θ²_CT); at qd_𝔬𝔬′ ~ 1 the CT form factor carries the intermolecular phase, which no Frenkel model has.
**Specification (GW/BSE appendix).** *What:* ΔS(q,ω) = S^{BSE,periodic} − S^{Frenkel}, and |f|² from Hückel/PPP against TDDFT and GW-BSE, for anthracene and
t-stilbene. *Approximation:* periodic 𝒳 = BSE with intermolecular overlap (includes CT) versus the Frenkel truncation of B1 §2 (zero overlap); PPP is a
semi-empirical π-only model. *Method:* QE + Yambo (or BerkeleyGW) G₀W₀ + BSE on the molecular crystal (≈ 50–100 atoms, k 4³, 200 bands), finite-q BSE at
the q grid of B1 §2; molecule-level TDDFT/GW-BSE (PySCF/ORCA) for the Frenkel inputs; PPP with standard parameters. *Convergence:* exciton energies to 50 meV
under band and k doubling; partial f-sum per molecule to 2%. *Metric:* max over q ≤ 30 keV of |Δ|f|²|/|f|² per state; report CT weight θ²_CT. *Pitfalls:* van
der Waals geometry (use experimental crystal structures, CSD); finite-q BSE needs the exchange term with LFE consistent with WP1-v3 [E7]; PPP fails for
σ-electron contributions at q ≳ 10 keV. *Cost:* 10³–10⁴ CPU-h per crystal.

## 17. LE-113 (G-E12): semiconducting CNT, 1D massive-Dirac RPA; OPW and FSI sizes
**1D massive Dirac bubble [D] (CW4-K3).** Hypotheses: one subband pair of a semiconducting tube, h = v_Fkσ_x + Δ_nσ_z (half-gap Δ_n of subband n),
undoped, T = 0, degeneracy g_deg = 4 (spin × valley), density vertex within the subband (q along the axis; inter-subband terms enter through the
transverse form factor F_⊥). The interband bubble per unit length is
  −Im R̃_1D,n(q,ω) = 2g_deg v_F q² Δ_n²/[𝓈^{3/2}√(𝓈 − 4Δ_n²)] Θ(𝓈 − 4Δ_n²),   𝓈 = ω² − v_F²q²,                                                      (17.1)
verified against direct δ-function integration to 10⁻⁸. Properties: the inverse-square-root edge at 𝓈 = 4Δ_n² is the 1D van Hove singularity; the weight
∫d𝓈 of the bracket equals 1, so Δ_n → 0 gives −Im R̃ → g_deg v_Fq²δ(𝓈), the metallic (E8.1) limit. Re R̃_1D,n follows by KK (needed in the denominator).
RPA with the tube Coulomb kernel (uniform cylinder of radius R_tube, HL units): V_1D(q) = 2αI₀(qR_tube)K₀(qR_tube), ε_1D = 1 − V_1D Σ_n R̃_1D,n, and
S_1D(q,ω) = −2Im[Σ_nR̃_1D,n/ε_1D]/(1 − e^{−βω}); S(q,ω) follows from B1 (1.1) with |F_⊥|². Excitons (large in CNTs) are the BSE rung beyond this.
**OPW size [E, CALC, CW4-K4].** Model: C 2p_z Slater orbital (exponent β_2p = 1.568/a₀ = 5.85 keV). With M_PW = Ψ̃(k_f − q) and M_OPW = M_PW − Ψ̃(k_f)⟨ψ|e^{iq·r}|ψ⟩,
the direction-averaged |M_OPW|²/|M_PW|² is direction-dependent at low energy: 0.76 for q ∥ orbital axis (sheet normal) but 2.96 for q in-plane at
E_kin = 10 eV, q = 7.5 keV (in-plane the plane-wave amplitude is already small, q_z = 0, and the orthogonality term dominates); at 50 eV, 15 keV it is 0.65–0.70
and at 100 eV, 25 keV 0.74–0.77 for both directions. Far from the Bethe ridge (10 eV, q = 15 keV) the ratio is 7–67, where |M_PW|² is suppressed as p^{-10}.
So the OPW correction is −25 to −35% for E_kin ≳ 50 eV, and of either sign (−25% to ×3) at 10 eV; the halo- and direction-weighted sign at low energy is not
fixed without the σ orbitals (spec: same K4 integral with all occupied orbitals from a Wannier projection, CPU-minutes) [E].
**FSI size [E].** The ejected electron sees the hole: unscreened point charge gives the Sommerfeld factor 2πζ_S/(1 − e^{−2πζ_S}), ζ_S = αm_e/k_f, i.e. 7.3 (10 eV),
3.4 (50 eV), 2.6 (100 eV) as an upper bound; full in-plane screening gives 1. Graphene's semimetallic screening pushes it towards 1; semiconducting CNTs less so.
*Spec (closure of the size):* final states as scattering states of the slab/tube Hartree potential plus the screened hole (RPA W of the sheet), by direct
integration (1D in z for a sheet); cost CPU-hours.

## 18. LE-114 (G-I5): transverse row, anisotropic flux, impact on 2401.11971
**Exact ratio [D] (CW4-K11).** For the density row, (I5.1) and 2401.11971 Eq. (5) differ pointwise by
  𝔇_nn^{URF}/𝔇_nn^{src} = (1 − ω²/Q²)²   (heavy and light mediators; for m_V → 0 the URF form is Coulombic, (q₀²/Q²)², while the source's (Q² − ω²)^{-2} is not),   (18.1)
so R_URF/R_src = ⟨(1 − ω²/Q²)²⟩_src ∈ [(1 − v²_χ,max)², 1] with the source's integrand as weight, and the limit moves by the inverse. Since ω ≤ v_χQ, for
SRDM (v_χ ≲ 0.1) the change is ≤ 2%; for boosted DM with v_χ → 1 the bound is vacuous and the weight near ω/Q → v_χ decides.
**Transverse row and anisotropic flux [D, structure].** With 2608.20715 Eq. (2): S_tot = Im[−1/ε_L] + (v_χ² − ω²/Q²)Im[−Q²/(ω²ε_T − Q²)] per unit of the
density normalisation, and for a directional flux the contraction is Σ_ab𝔇_ab(q, p̂_χ)S_ab(q,ω) with full-vector S, i.e. q̂·S·q̂ and P_T(q̂)·S·P_T(q̂) weighted by
(p̂_χ·q̂)² terms. **Specification (recast).** *What:* R_URF/R_src for 2401.11971's targets and fluxes, and the transverse fraction. *Approximation:* their ε_L (RPA, Si/Ge),
ε_T = ε_L at q → 0 and Lindhard-transverse otherwise; relativistic 𝔇 of (I5.0). *Method:* re-implement their Eqs. (4)–(6) with (I5.1) and the transverse term,
CRDM flux tables as in the source; 3-D (Q, ω, flux angle) quadrature. *Convergence:* reproduce their Fig. 3 with their Eq. (5) to 5% first. *Pitfalls:* the
Cherenkov-type pole of the transverse term (ω²Re ε_T = Q², needs an iη scan); F_DM at Q² − ω² versus Q². *Cost:* CPU-hours (fits the box; optional run).

## 19. LE-115 (G-X6): sign and normalisation of the 𝒫^W_0-restricted boost; size of the non-rigid correction
**Normalisation and sign [D].** WP3 (W.5): A^{Mig}_a = (q/M_κ)·⟨a|∇_RΦ₀⟩/(E_a − E₀) = −(q/M_κ)·⟨a|∇_RV|0⟩/ω²_a. For one nucleus ∇_RV = −Σ_i∇_iV exactly, and
⟨a|Σ_i∇_iV|0⟩ = m_eω²_a⟨a|Σ_ir_i|0⟩ ([H,P] = iΣ∇V with P = im_e[H, Σr]), so A^{Mig}_a = +(m_eq/M_κ)·⟨a|Σ_ir_i|0⟩ = −i × (the first-order term iq_e·⟨a|Σr|0⟩ of the
sudden boost ⟨a|e^{iq_e·Σr}|0⟩, q_e = m_eq/M_κ). The overall phase −i is common to every Migdal amplitude, drops from |A|², but fixes the sign of the Migdal–PAER
interference of WP3 (W.6). B1's (H_W) replaces ∇_{R_0}V by −Σ_i(∇_iV)p^W_{0,i}, projector on the ket (ground-state) side; p^W_0 is the one-body projector on the
site-0 Wannier functions of the occupied manifold.
**(W.5) under (H_W) with its remainder [D, one-body local KS Hamiltonian h, so that Σ∇V = m_e[h,[h,r]]] (CW4-K7, K7b).** For a single excitation a = (c ← v)
and any projector, exactly,
  ⟨c|(∇V)p^W_0|v⟩ = m_e Σ_m (ε_c − ε_m)² r_cm (p^W_0)_mv,                                                                                      (19.1)
  A^{(H_W)}_a = (m_eq/M_κ)·Σ_{v′∈𝒲}[(ε_c − ε_v′)²/ω²_cv] r_cv′(p^W_0)_{v′v} = (m_eq/M_κ)·⟨c|r p^W_0|v⟩[1 + O(W_𝒲/ω_cv)],                              (19.2)
with v′ running over the Wannierised (occupied) manifold 𝒲 and W_𝒲 its bandwidth (relative error ≤ 2W_𝒲/ω_cv + (W_𝒲/ω_cv)²). Consequences: (i) the "rigid Wannier
boost" form of B1 §7(b) is exact iff the manifold is flat (cores, isolated atoms); (ii) **the acoustic sum rule fixes the ordering:** Σ_sites p^W_0 = P_𝒲 and
P_𝒲|v⟩ = |v⟩, so the site sum of (19.2) is exactly the full boost (m_eq/M_κ)⟨c|r|v⟩ with B1's ket-side ordering and valence-only Wannier functions. The
Hermitian-symmetrised alternative ½{∇V, p^W_0} gives only half the boost for interband final states (the bra-side term vanishes, c ∉ 𝒲; K7b) and is
**rejected**. This is the normalisation the v2 sketch left open; the sign is + relative to (m_eq/M_κ)⟨c|r|v⟩. For Si valence (W_𝒲 ≈ 12 eV) and ω_e ≈ 20–100 eV
the flat-band error bound is O(1) to 0.25, which quantifies "fails at O(1) for valence".
**Exact gap (non-rigid correction).** The true amplitude uses ∇_{R_0}V^{scf} (DFPT), not the projected translation. Missing step: the ratio
𝔯_W(q,ω_e) = |A^{DFPT}|²/|A^{(H_W)}|². **Specification (DFPT + Wannier appendix).** *What:* 𝔯_W per q for Si, Ge, diamond (the X6 type-M nuisance). *Approximation:*
leading non-adiabatic Migdal (T0), clamped-nuclei final states, RPA+LFE for the (p, ω_e) lines. *Method:* QE scf/nscf → ph.x (dvscf at the p grid) → Wannier90
valence MLWFs (k 16³) on the same U(k) gauge → matrix elements ⟨c|∂_{R_0}V^{scf}|v⟩ versus (19.1)–(19.2) side by side (EPW-style interpolation of the deformation
potential). *Convergence:* acoustic sum rule Σ_κ∂_{R_κ}V = −Σ∇V to 10⁻³; δM sum rule (WP3 J3). *Pitfalls:* nonlocal pseudopotentials add i[V_NL, r] to the
velocity (correct (19.1) by it); gauge consistency of g and ρ (CONVENTIONS §4). *Cost:* 10³ CPU-h (GPU fork).

## 20. LE-116 (S2): beyond the Larmor hypotheses; the Larmor citation
**Citation [FT cond-mat/0108424 = Oshikawa and Affleck, PRB 65, 134410 (2002), DOI 10.1103/PhysRevB.65.134410 (arXiv API)].** p.4, Eqs. (2.4)–(2.5): for
H = H₀ + H_Z with SU(2)-symmetric H₀, "dS⁺/dt = i[H, S⁺] = i[H_Z, S⁺] = −iHS⁺ because H₀ commutes with S⁺ … consequently χ^{+−}(0,ω) ∝ δ(ω − H) … completely sharp,
and located exactly at the Zeeman energy", with "the absorption intensity … generally affected by the exchange interaction". This is the B2 (B2.5.2) statement.
Kanamori and Tachiki (1962) is cited there (Ref. 47) for the linewidth theory, not for the Larmor statement; it should not be cited for it.
**Beyond Larmor: two-sublattice antiferromagnet [D, LSWT] (CW4-K8).** Easy-axis AFM, k = 0 bosonic Hamiltonian A^{sw}(a†a + b†b) + B^{sw}(ab + a†b†) with
A^{sw} = ω_E + ω_A, B^{sw} = ω_E (exchange and anisotropy frequencies). Colpa gives two degenerate modes ω_AFMR = √(A^{sw2} − B^{sw2}) = √(ω_A(2ω_E + ω_A))
(split by ±gμ_BB₀ in an axial field), and the uniform transverse spin S^x_tot = √(|𝐒|/2)(a + a† + b + b†) has total weight per antiparallel pair
  Σ_ν|⟨ν|S^x_tot|0⟩|²/N_pair = |𝐒|√((A^{sw} − B^{sw})/(A^{sw} + B^{sw})) = |𝐒| ω_AFMR/(2ω_E + ω_A),                                               (20.1)
against |𝐒| for a ferromagnetic pair (Larmor). Inserted in (B2.5.1): Γ_abs = (B2.5.2) with 𝔰_net → 2|𝐒|n_pair ω_AFMR/(2ω_E + ω_A) and δ(ω − ω_Lar) → Σ_±½δ(ω − ω_±) (T = 0): the AFM absorption
is suppressed by ω_AFMR/(2ω_E + ω_A) ≈ √(ω_A/2ω_E) (exchange suppression) but sits at THz frequencies. Demagnetisation is negligible (M_s = 0).
**Specification (LSWT appendix; general anisotropic, dipolar, noncollinear).** *What:* ω_ν(k → 0) and ℰ^α_ν(0) with shape (demag) and dipolar sums, then (B2.5.1).
*Approximation:* ref = LSWT, T-factor as (B2.5.2); dipolar interaction as an Ewald sum with the k → 0 shape-dependent limit (Polder–Kittel). *Method:* SpinW/Sunny
(Colpa) with J^{ex}, anisotropy, g tensors from INS/ESR fits or DFT+U (QE, four-state), magnetic unit cell. *Convergence:* (20.1) reproduced for the two-sublattice
test; FM limit reproduces (B2.5.2)–(B2.5.3). *Pitfalls:* the k → 0 and shape limits do not commute (uniform mode is shape-dependent); Colpa requires a positive-
definite boson matrix (a soft mode signals a wrong ground state). *Cost:* ≪ 1 CPU-h per target (fits the box; optional run, e.g. NiO or MnF₂).

## 21. LE-117 (S6): longitudinal spin response from neutron data
**No-go theorem [D] (CW4-K12).** Magnetic neutron scattering at wavevector q measures the transverse projection P_T(q̂):S(q,ω), P_T = 1 − q̂q̂ (B2 (B2.6.1)).
For any element g of the magnetic point group, S(gq) = gS(q)gᵀ and P_T(gq̂):(gSgᵀ) = P_T(q̂):S, so symmetry-equivalent q add no equation. Polarisation
analysis (P ∥ q, ⊥ q) separates the two transverse components and the chiral part, but the neutron magnetic interaction contains only M_⊥q, so q̂·S·q̂ at that q
is never measured, polarised or not. **No data-only neutron route to q̂·S·q̂ exists.**
**Routes (exact-gap closure).** (i) *Model route [D, under (H_iso)]:* for a collinear magnet with moment direction m̂ and S = S_∥(|q|,ω)m̂m̂ + S_⊥(|q|,ω)(1 − m̂m̂)
(no chiral part; S_∥, S_⊥ depending on q only through |q| in the fitted window), unpolarised data at two values of c = q̂·m̂ give P_T:S = S_∥(1 − c²) + S_⊥(1 + c²),
a 2×2 system for (S_∥, S_⊥) (K12), and q̂·S·q̂ = S_∥c² + S_⊥(1 − c²). Data with c varied by field-rotated single-domain samples satisfy the hypothesis better than
different |q| points. (ii) *Theory route:* fit an LSWT (or exact) model to the transverse data and compute q̂Sq̂ from it (the fit uncertainty is a type-M nuisance).
(iii) *Other probes:* at k → 0 the full tensor follows from FMR/THz permeability (B2 §6 (ii)); resonant x-ray magnetic scattering couples through photon
polarisation vectors and is not restricted to M_⊥q [E]. Spec for (i): polarised or unpolarised INS on a single-domain crystal in a rotating field, two field
angles per (|q|, ω) bin; for (ii): the §20 LSWT machinery.

---
## Symbols introduced/used
*Used as in NOTATION v4 + R9 + WP7 rows and CONVENTIONS:* Δ_BCS, Δ_D, 𝔤_I, 𝔤_II, 𝔰_BCS, 𝔣_Lin, v_F, k_F, k_TF, N(0), ξ_coh, ℓ_mfp, u^B_k/v^B_k (here written u, v), Π^N_ij,
τ^N_i, R̃^{GRPA}, ε_bg, α̃, 𝓈, g_deg, Λ_D, Λ′_D, δε_D, ε_r, κ_mix, Rate_src, Rate_URF, Γ_abs,src, 𝒮_F^D, ζ_S^D, U^B, V^B, ℰ^α_ν, F^{mag}_j, λ_{S,j}, λ_{L,j}, J^{ex}_{ij},
𝔰_net, ω_Lar, 𝒫^W_0, (H_W), A^{Mig}, δM_κ, ρ_cv, ε_in, ε_out, 𝔣^{loc}_ℓ, ϕ_QD, R_QD, a_x, 𝔍^F, f_{0𝔵}, a*, E_b^D (= E_I of 2212.04504), q̃, k̃, 𝓃_D, P_T, S_n, v_χ, 𝔇_nn, F_DM, q₀.
Source-only (NOTATION §K; quoted, not campaign symbols): Δ, κ, g, E_r, N_t, |f_QD|², |f_crystal|², E_I, E_eff/E_0, H (Oshikawa–Affleck field), m*, E_F of 1603.05351.
*Introduced (NOTATION rows requested; none collides with an existing row, checked by grep):*
| Symbol | Meaning | Where |
|---|---|---|
| 𝔳_GRPA(q,ω) | GRPA vertex fraction Im[R̃^{GRPA} − Π^N₃₃]/Im Π^N₃₃ | §1 (1.1) |
| M_i | Nambu pair-creation amplitude ⟨+,ξ′\|τ^N_i\|−,ξ⟩ | §1, §12 |
| P_Δ(Δ; r) | local-gap distribution from BdG | §2 (2.1) |
| Γ^{(4m)}_q, 𝒢₂ | two-magnon quartic vertex; free two-magnon propagator | §3 (3.1) |
| 𝒢^γ_OA(q,ω) | full-q antisymmetric current response (γ_OA its slope) | §4 |
| γ^{FI}_{ij} | one-body transition density matrix of embedded multiplets | §5 (5.1) |
| Ry_D | massive-Dirac exciton Rydberg Δ_D(α̃/g_deg)²/4 | §6 (6.1) |
| ⟨j_K(q)⟩, 𝒞^{(ℓ,J)}_{KK′} | radial form-factor integrals; multiplet reduction coefficients | §7 (7.1) |
| 𝔯, δ_𝔰 | Im ε^{nor}/Re ε^{nor}; KK screening shift relative to Re ε^{nor} | §8 (8.1) |
| J_F, R_dd, 𝐝 | Förster coupling, inter-dot distance, transition dipole | §15 (15.1) |
| θ_CT, t_CT, S_HL, f_C | Frenkel–CT mixing angle, transfer integral, HOMO–LUMO overlap, CT form factor | §16 (16.1) |
| R̃_1D,n, Δ_n, V_1D, R_tube, ε_1D | 1D subband bubble, subband half-gap, tube Coulomb kernel, radius, 1D dielectric function | §17 (17.1) |
| β_2p | Slater exponent of C 2p (not ζ_S) | §17 |
| p^W_0, W_𝒲, 𝔯_W | one-body site-0 Wannier projector; bandwidth of the Wannierised manifold; DFPT/(H_W) ratio | §19 |
| A^{sw}, B^{sw}, ω_E, ω_A, ω_AFMR, n_pair | k = 0 LSWT coefficients, exchange and anisotropy frequencies, AFMR frequency, AFM pairs per cell | §20 (20.1) |
| (H_iso), S_∥, S_⊥, c | uniaxial-tensor hypothesis, its components, q̂·m̂ | §21 |
Labels: CW4-K1…K14 and K7b (checks); equation labels (1.1)…(21.x) are local to this return (prefix "CW4").

## Interface flags
| # | To | Item | Action |
|---|---|---|---|
| IF-CW4-1 | WP4 / WP5 / WP6 | L^{BCS} at the edge | use (8.1) and the §8 table instead of [4.2′] + "exclude y ≲ 3.5"; type-Δ nuisance from the KK-∞/cut spread; WP4-K34's Re ε^{nor} = k_TF²/q² is 16% high at the edge |
| IF-CW4-2 | WP8-U, coordinator | Al Δ_BCS | table value 0.3 meV (2109.04473) is ≈ 1.7× bulk; use 0.18 meV [D from FT T_c] for bulk Al (WP4 already uses 0.17 meV); Nb 1.50–1.61 meV [FT 1805.06359 p.3, secondary] |
| IF-CW4-3 | WP8-U, WP8-F | ZrTe₅ Δ_D provenance | Δ_D = 11.8 meV [FT 1910.02091 p.12, DFT-NR]; "exp [52] 11.75" not in [52] |
| IF-CW4-4 | WP3 (W.6), WP7-B1 | Migdal phase | A^{Mig} = −i × boost amplitude: carry the −i in Migdal–PAER interference |
| IF-CW4-5 | WP5 | Holstein seeds in SC | (12.1) confirms B1 §9 WP4-consistency (i)–(ii): QP energy ω − ω_ph, case-I P(E₁) |
| IF-CW4-6 | LIMITS L16, WP6 | Dirac re-plot | multiply source curves by ε_bg² (σ̄) and √ε_bg (κ); never also by 0.55–0.62 |
| IF-CW4-7 | WP5 (readout) | QD films | Förster transfer ∝ J_F² is a WP5 readout input; S unaffected |
| IF-CW4-8 | CW8 / book | ab initio appendix | §1–§21 specifications are written in the appendix categories requested (coordinator note); reuse verbatim |

## Owed corrections (target → exact text; not applied here)
1. **LIMITS LB1-10, Status cell** → "DERIVED, REFEREED; (A2.2) **[D]** by explicit Nambu second order (R16 CW4 §12: [j(q=0), H_BCS] = 0, amplitude
   −ê·(v_{k+Q} − v_k)g(u′v + v′u)/ω, case I), result = Allen, PRB 3, 305 (1971) (cited without equation numbers; closed access)". Leading-correction cell: append
   "strong coupling: N_sN_s′ + P_sP_s′ (CW4 §12, [D, sketch])".
2. **WP7-B1-v2 §13 G-A2** (record through CORRECTIONS) → "CLOSED (R16 CW4 §12); Eliashberg form [D, sketch], computation specified".
3. **LIMITS LB1-5, Status cell** → "DERIVED (structure; bulk limit), REFEREED; prefactor: printed Eq. (6) exceeds the URF rate by μ_eχ/(4E_r) with Eq. (10) and is
   dimensionally inconsistent with Eq. (12) (= 1509.01598 Eq. (3.17)); correct forms CW4 (14.1)–(14.2); numerics presumably via (14.2) [E]; ✎ depolarisation factor
   CONFIRMED, > 1 iff |ε_in|² > (ε_out/2)(Re ε_in + ε_out), size UNRESOLVED". Caveat cell: replace "ε of the source's Ref. [139]: intrinsic or film, **not verified**" by
   "Ref. [139] = Hechster & Sarusi, JAP 122, 024302 (2017): modelled intrinsic dot ε (metadata level)".
4. **LIMITS LB1-11, Status cell** → replace "numerical impact **UNRESOLVED**" by "numerical impact [E]: printed/correct rate 1.47–0.56 (heavy), 1.46–1.06 (light)
   for m_χ = 0.02–10 MeV at fixed |ε| (CW4 §13)".
5. **LIMITS LB1-6, Leading-correction cell** → "OPW orthogonalisation (C 2p_z model, [E], CW4 §17): −25% (q ∥ orbital axis) to ×3 (in-plane) at 10 eV, −25 to −35% at 50–100 eV; FSI factor between 1 and the
   unscreened Sommerfeld 2.6–7.3 (100–10 eV) [E]; semiconducting CNT: 1D massive-Dirac RPA CW4 (17.1)".
6. **LIMITS LB1-8, Status cell** → "**[D]** under (H_W) with Hermitian ordering: A^{(H_W)} = (m_eq/M_κ)·⟨c|r p^W_0|v⟩[1 + O(W_𝒲/ω_cv)] (CW4 (19.2)), projector on the ket side (fixed by the acoustic sum rule;
   the symmetrised ordering gives half the boost and is rejected); phase −i relative to the boost; non-rigid (DFPT) ratio = exact gap G-X6, specified (CW4 §19)".
7. **LIMITS LB1-13, Status cell** → replace "**impact on its limits UNRESOLVED**" by "impact: R_URF/R_src = ⟨(1 − ω²/Q²)²⟩ ∈ [(1 − v²_χ,max)², 1] exactly (CW4 (18.1));
   ≤ 2% for v_χ ≲ 0.1; recast for v_χ → 1 specified".
8. **LIMITS B2-L6, Chain cell** → "(3.5), spin row, k → 0; Larmor statement [FT: Oshikawa & Affleck, PRB 65, 134410 (2002), Eqs. (2.4)–(2.5)], Polder (B2.5.3)";
   Caveat cell → "λ_S = g_J − 1 only for J multiplets; two-sublattice AFM: weight |𝐒|ω_AFMR/(2ω_E + ω_A) per pair at ω_AFMR (CW4 (20.1)); general anisotropic/dipolar
   targets: LSWT + demag (specified)".
9. **LIMITS B2-L7, Caveat cell** → "P_T only: no neutron route (polarised or not) to q̂·S·q̂ (CW4 §21 theorem); longitudinal part via (H_iso) two-angle
   inversion, model fit, or k → 0 permeability".
10. **LIMITS L16, Note cell** → replace "re-plot = RG10 (coordinator)" by "re-plot: σ̄_lim × ε_bg² (×1600; ×640 isotropised ZrTe₅), κ_lim × √ε_bg, exact for the isotropic
    models; not × 0.55–0.62 (already in the source |ε_r|²); anisotropic 1910.02091 recast specified (CW4 §9)".
11. **WP8-U-table.csv, ZrTe5 Delta_D row, note** → "half-gap per 1910.02091 p.12 (gap 23.6 meV ↔ Δ = 11.8 meV); 'exp [52]' = 1603.05351, which reports no gap
    [UNVERIFIED attribution]; use 11.8 (DFT, NR)". **Al Delta_BCS row** → value 0.18 meV, tag E (BCS from FT T_c 1.2 K, 2305.06084), note "2109.04473 uses 0.3 meV
    (film-like)". **Nb** → "Delta_BCS 1.50–1.61 meV, FT (secondary), 1805.06359 p.3, orientation-dependent".
12. **WP4-v3 I12 / LIMITS L15 nuisance wording** (through CORRECTIONS) → "L^{BCS} = 𝔤_IL^{nor}(1 + 𝔯²)/[(1 + δ_𝔰)² + 𝔤_I²𝔯²] (CW4 (8.1)); at the Al edge 0.33–0.40
    (y = 2.2) … 0.94–0.96 (y = 10)".

## Proposed LIMITS rows (numbering by the coordinator)
| # | Owner | Location | Source [FT] | Chain | Status | Leading correction; caveats |
|---|---|---|---|---|---|---|
| CW4-a | CW4 / WP4 | §8 (8.1) | WP4 [4.2′]; 2609.06423 Eq. (9) | clean quasiclassical BCS, KK of δIm ε, no expansion of \|ε\|⁻² | DERIVED (model); table [CALC] | O(Δ²/q²v_F²) in Im ε; Im ε^{nor} above qv_F (KK spread) |
| CW4-b | CW4 / WP7-B1 | §12 (12.1) | 1604.06800 Eqs. (16)–(17) | (3.5), sector (2,1), q_φ = 0, mean-field BCS, T-even g | DERIVED | Eliashberg N_sN_s′ + P_sP_s′ [D, sketch]; GRPA dressing O(Δ²/(v_FQ)²) |
| CW4-c | CW4 / WP7-B1 | §17 (17.1) | — | 1D massive Dirac, RPA with 2αI₀K₀ | DERIVED (K3) | excitons (BSE); inter-subband via F_⊥ |
| CW4-d | CW4 / WP7-B1 | §19 (19.1)–(19.2) | 1912.13484 Eqs. (2.7)–(2.8) | (W.5) T0, one-body local h, occupied-manifold MLWF projector on the ket side | DERIVED; DFPT ratio = gap | nonlocal V_NL commutator; W_𝒲/ω_cv |
| CW4-e | CW4 / WP7-B2 | §20 (20.1) | cond-mat/0108424 Eqs. (2.4)–(2.5) | (3.5), spin row, k → 0, two-sublattice LSWT | DERIVED (K8) | dipolar/shape; 1/(2\|𝐒\|) |
| CW4-f | CW4 / WP7-B2 | §21 | 2504.02927 Eq. (26) | neutron cross-section ∝ P_T:S | DERIVED (no-go) | (H_iso) needed for the longitudinal part |
| CW4-g | CW4 / WP7-B1 | §14 (14.1)–(14.2) | 2208.05967 Eqs. (6), (10), (12); 1509.01598 Eqs. (3.13), (3.17) | WP0 (9.2) per cell | DERIVED (K6) | Fig. 4 numerics not re-run |
