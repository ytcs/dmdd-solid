# R16 / CW2: closure of LE-48 … LE-72 (lattice, Migdal, anharmonicity, disorder, polar single phonons)

Brief: campaign/paer/briefs/R16/CW2.md. Ledger: state/LOOSE-ENDS.md §1 rows LE-48–LE-72 (§2 group CW2). Sources read: returns/R8/WP2-v3.md, WP3-v3.md (Part II, §8, §10, §12–§15),
returns/R12/WP7-B2-v2.md, LIMITS.md, CONVENTIONS.md (incl. R8/R13 amendments), NOTATION.md (rows checked for collisions), CONTROLS.md, code/ENV.md. No referee report was read.
Checks: code/CW2/checks.py, **24/24 PASS** (≈ 60 s, one core). [CALC] runs: code/CW2/atomic_contact.py (QE 7.6 ld1.x, all-electron atoms, < 10 s single thread).
Formulated-job inputs: code/CW2/inputs/{Si,Ge,GaAs}/ (rtsc/bench layout). Literature: literature/papers-CW2/ (HTML kept, PDFs deleted); arXiv IDs cited here verified against the arXiv API: 2603.13052, 2308.06314, 2210.04917. Nothing committed; no other file edited.
Deliverable rule (STATEMENT, user 2026-11-01) and coordinator clarification: a compute row is closed by a derivation of the quantity plus a specification that a reader can follow
(what is computed, its expansion level τ, method and convergence parameters, pitfalls). Every compute row below carries that block, marked **Spec**.

## 0. Closure table

| Row | Item (short) | Status | Where | One-line result |
|---|---|---|---|---|
| LE-48 | coherent n_ph = 2 at q < q_BZ | CLOSED | §1 | BZ form (CW2.1); exact ω-integrated weight as a lattice sum of squared displacement correlations (CW2.3); spec |
| LE-49 | pointwise bound, incoherent approx. | CLOSED | §2 | 0 ≤ S^{(n)}_coh ≤ n_b𝔓^{(n)} (CW2.5), ⟨𝔓⟩_BZ = S_inc (CW2.6); exact rate-level ℛ_n; table flag rule |
| LE-50 | T > 0 shell sum, n_ph = 2 | CLOSED | §3 | resummed (momentum-space) form (CW2.7), finite for q ≠ G; integrable 1/\|q − G\| (second-order TDS) bound (CW2.8) |
| LE-51 | valence deformation at q ≫ q_BZ; L4 add-on | CLOSED-AS-EXACT-GAP | §4 | decomposition + translational sum rule (CW2.9); core tail O((qa)^{-2}) relative [D, hydrogenic]; valence tail needs AE δρ (spec) |
| LE-52 | non-perturbative anharmonicity | CLOSED-AS-EXACT-GAP | §5 | moments are static (CW2.10); Markov–Krein CDF band from 𝔨₁–𝔨₄ (CW2.11), any anharmonicity; real-time dynamics = gap |
| LE-53 | amorphous S_dist at n_ph ≥ 2 | CLOSED | §6 | isotropic-glass formula (CW2.12) with conditional correlation moments; spec |
| LE-54 | 𝔨₃^X all-electron; E^{Mig}_3 | CLOSED | §7 | E^{Mig}_3 = (q²/2M²)[Ze²𝓃_e(R)/3 − ∂²E^ad] (CW2.13); [CALC] Si 1498, Ge 16836, Ga 15416, As 18493 eV² × E_R |
| LE-55 | δM_κ, C_κ, P_Mig ≤ 10⁻³ | CLOSED | §8 | inverse spectral moments (CW2.14); P_Mig ≤ E_R(δM/M)/E_g; Sternheimer recipe (CW2.15); spec |
| LE-56 | Δ𝓃_κ(q) beyond 1s² | CLOSED-AS-EXACT-GAP | §9 | [CALC] AE atomic 𝔯_κ(q) for Si, Ge, Ga, As; reciprocal-space formula (CW2.16); "L shell doubles" withdrawn; crystal valence = gap |
| LE-57 | G3 multiphonon tables | CLOSED | §10 | (3.2)/(3.5)/(3.6) + validated T > 0 FFT route (C19); per-atom PDOS suffices on cubic sites; spec |
| LE-58 | G3 PIMD inputs | CLOSED | §11 | spec with estimators, bead/T convergence, pitfalls |
| LE-59 | G13/G-F2 anharmonic template | CLOSED | §12 | linked-cluster exponent (CW2.17); first-order Φ³ vanishes in S_κκ by TR (CW2.18); contraction rule; spec |
| LE-60 | G11 S_ℓm tables | CLOSED | §13 | selection rules; Si continuum S₄₀/S₀₀ = +2.2% [E]; incoherent S_{ℓ>0} = 0 test; spec |
| LE-61 | G6 Migdal one code path | CLOSED | §14 | spec with three closure tests ((CW2.13), J3/TRK, (CW2.14) bound) |
| LE-62 | crystal NR bremsstrahlung Z*_κ(ω) | CLOSED | §15 | Z*_κ(ω) at zero macroscopic field (CW2.19); \|Z*(ω) − Z*(0)\| ≤ ω²√(α₂δM) [D]; spec |
| LE-63 | 2603.13052 Eq. (4.8) factor 2 | CLOSED (CONFIRMED) | §16 | (4.8) is 2× the standard dσ/dq given their c_i² = πσ_n/μ²; rate (4.6) unaffected; mean free path (4.9) inherits it |
| LE-64 | glass A^{IR}, B^{IR}; S_dist n_ph ≥ 2 | CLOSED | §17 | C^{IR}(ω) = 𝒮_Z(ω/c)/M̄ (CW2.20): A^{IR} = 𝒮_Z(0⁺)/M̄, B^{IR} from 𝒮_Z″; from static configurations |
| LE-65 | isotope-resolved Hessians, O(σ_M/M̄) | CLOSED | §18 | exact O(σ_M/M̄) via single-site Lifshitz (CW2.21)–(CW2.22): relative correction κ^M_1h_iso(ω) ≈ +9% at 50 meV [E] |
| LE-66 | low-T in-band ε(ω) of Si | CLOSED-AS-EXACT-GAP | §19 | α(ω, T→0) ≤ α(ω, 293 K) (CW2.23) ⇒ Γ_iso/Γ_EM ≥ 6.3×10³ at mK; no low-T datum found (GAP); spec |
| LE-67 | GaAs electron-scalar near-cancellation | CLOSED | §20 | requirement δ(Z*/ε_∞) ≤ 2% for 20% in rate; LST data route (CW2.24) meets it, PBE-DFPT ε_∞ does not |
| LE-68 | 2308.06314 Fig. 2 projection | CLOSED (RESOLVED) | §21 | rigid-ion vertex, no δZ (text Eqs. (40)–(41) + PhonoDark-abs code) ⇒ GaAs curve ≈ 9× high in rate |
| LE-69 | reflection/refraction force above σ_crit | CLOSED | §22 | planar wall pressure (CW2.25) with thick-slab average 2R/(1+R) (C15); cylinder geometry spec; any bound stays [C] until run |
| LE-70 | solid He remainder beyond Gaussian | CLOSED | §23 | Markov–Krein band (CW2.11) with exact static moments bounds the remainder at any δ_Lind; PIMD spec |
| LE-71 | X10 valence, c_κ not ∝ M_κ | CLOSED | §24 | exact k → 0 amplitude through S^{ee}_{GG′}(0,ω) (CW2.26); diamond (200) channel vanishes (C17); spec |
| LE-72 | κ_URF in MOF cells; giant moments | CLOSED-AS-EXACT-GAP | §25 | branching-process expectation (CW2.27) (C16); fc3 spec; giant-moment (4f) mechanism = gap |

Counts: CLOSED 20 (two of them literature verdicts), CLOSED-AS-EXACT-GAP 5, CANNOT-CLOSE 0.

## 0b. Shared computation stack (referenced by the Spec blocks)
- **A. Harmonic lattice (DFPT → IFC → interpolation).** Computed: force constants Φ_{κκ′}(ΔR), eigenpairs (ω_{Qν}, e_{κν}(Q)), per-atom PDOS, B_κ, B_{κκ′}(ΔR), Z*, ε_∞.
  Level: GS sector, n_B = 0, n_A = 0 (harmonic BO surface), static (adiabatic) DFPT, 𝒳 = KS-PBE linear response. Method: pw.x scf → ph.x on an 8³ q grid → q2r.x → matdyn.x
  (code/CW2/inputs/{Si,Ge,GaAs}: SG15 ONCV PBE v1.2, ecutwfc 80 Ry (COMP-PH conv/ scan: Si stress converged to 0.1 kbar at 80 Ry; Ge, GaAs carry 3d semicore), 12³ k,
  tr2_ph 10⁻¹⁶, epsil for GaAs, fildrho/fildvscf kept). Convergence: IFC range (6³ vs 8³ q grid, ω to 0.1 meV), ecut, k; acoustic sum rule `asr='crystal'`.
  Pitfalls: PBE lattice constants are ≈ 0.7–1% large and soften phonons by 2–4%, so the inputs use experimental low-T a and a vc-relax partner run gives the systematic;
  polar GaAs needs the non-analytic (Z*, ε_∞) term in q2r/matdyn, else LO is wrong at small Q; the eigenvector phase must be the cell phase e^{iQ·R} (CONVENTIONS §5) with
  intra-cell factor e^{iq·r_κ} at unreduced q (WP2-v3 §2). Cost (ENV benchmark scaling (ecut/20)^{1.5}·N_el/8·N_irr/8): Si ≈ 25 CPU·h, Ge and GaAs ≈ 60 CPU·h each → formulated (> 3 h).
  On the user's pod the same inputs run through rtsc/bench/run-fork.sh (RTSC_STH=1 batched Sternheimer). COMP-PH (LE-16) outputs, when returned, replace stage A for Si/Ge.
- **B. All-electron densities.** Atoms: ld1.x (done here, §7, §9). Crystals: PAW with AE reconstruction (QE pp.x plot_num = 21 with pslibrary PAW sets, not SG15) or LAPW (Elk/WIEN2k).
  Pitfall: a norm-conserving pseudo-density (SG15) is unphysical inside r_c, i.e. above q_c ≈ 2π/r_c ≈ 10 keV (r_c ≈ 2 a₀ for Si); it cannot give core or orthogonality-wiggle tails.
- **C. Frequency-dependent DFPT (shifted Sternheimer).** Computed: dynamical on-site force constant Φ^{el}_{κκ}(ω), Z*_κ(ω), ε(ω), the inverse moments ℐ_k of §8.
  Method: solve (H − ε_v ∓ ω − iη)Δψ^±_v = −P_c ΔV ψ_v self-consistently (TDDFPT at RPA, optionally ALDA); imaginary frequencies iω avoid resonances and give Taylor coefficients
  by fits in ω²; real ω with η = 10–20 meV near the gap. This is the use case of the fork's batched Sternheimer engine (rtsc/sth); a ≈ 50-line patch of ph.x zstar_eu
  (mixed E(ω)–u response) is needed. Pitfalls: KS gaps (PBE GaAs ≈ 0.5 eV vs 1.52 eV) put spurious resonances below the true gap → scissor or hybrid functional, or use measured ε(ω);
  pseudopotential frozen cores miss the core part of δM (add N_core m_e exactly, J3 atomic TRK) and of P_Mig (add atomic L7a per shell).
- **D. PIMD.** i-PI + MLIP (MACE or NequIP trained on PBE, validated on displaced configurations to 3σ of the PIMD distribution), 216-atom cells; estimators in §11.
- **E. Glass models.** Melt-quench MD with an MLIP as specified in WP7-B2-v2 §2.5 (648–5184 atoms, ≥ 5 quenches), full Hessian diagonalisation (15552 dof dense: ≈ 4×10¹² flop),
  Z*_I from a charge model that reproduces site-charge fluctuations (not only local neutrality) or DFPT on subcells.

---
## 1. LE-48: coherent n_ph = 2 at q < q_BZ from first principles
**Item.** WP2-v3 §12.1: the coherent two-phonon S at q ≲ q_BZ was specified but not derived in a computable closed form; the §3.3 shell size is [E].
**Derivation [D]** (hypotheses: harmonic Gaussian state, multiplicative vertex c_κ (nucleon or rigid ion; for the full charge vertex use 𝒵_κ of §4 at one-phonon order, WP2-v3 §1.2)).
Integrating the n_ph = 2 term of WP2-v3 (2.2) over Q₂ with the momentum δ:

  S^{(2)}_coh(q,ω) = (π/Ω) Σ_{ν₁ν₂,s₁s₂} ⟨ Π_{i=1,2}[n_{Q_iν_i} + (1+s_i)/2] δ(ω − s₁ω₁ − s₂ω₂) |F^{s₁s₂}_{ν₁ν₂}(q,Q₁)|²/(4ω₁ω₂) ⟩_BZ,
  F^{s₁s₂}_{ν₁ν₂} = Σ_κ c_κ e^{−W_κ} e^{iq·r_κ} (q·e^{s₁}_{κν₁}(Q₁))(q·e^{s₂}_{κν₂}(Q₂))/M_κ,   s₁Q₁ + s₂Q₂ = q − G,   ⟨·⟩_BZ ≡ Ω∫_BZ d³Q₁/(2π)³.        (CW2.1)

This is what a code evaluates pointwise. Its ω integral has an exact real-space form. From WP2-v3 (2.1) at t = 0, Φ_{κκ′}(ΔR,0) = q·B_{κκ′}(ΔR)·q with the static correlation tensor

  B_{κκ′}(ΔR) ≡ N⁻¹ Σ_{Qν} (2n_{Qν} + 1) e_{κν}(Q) e_{κ′ν}(Q)† e^{iQ·ΔR}/(2ω_{Qν}√(M_κM_κ′)),   B_{κκ}(0) = B_κ,                                       (CW2.2)

(using e(−Q) = e(Q)*, n_{−Q} = n_Q), so that for every n

  𝔚^{(n)}(q) ≡ ∫(dω/2π) S^{(n)}(q,ω) = (1/(n!Ω)) Σ_{ΔR,κ,κ′} c_κ*c_κ′ e^{−iq·ΔR_{κκ′}} e^{−W_κ−W_κ′} [q·B_{κκ′}(ΔR)·q]^n,   ΔR_{κκ′} = ΔR + r_κ − r_κ′.               (CW2.3)

The (0,κ,κ) terms are the incoherent weight 𝔚^{(n)}_inc = (n!Ω)⁻¹Σ_κ|c_κ|²e^{−2W_κ}(q·B_κ·q)^n, and the **exact rate-level coherence correction** for ω bins that cover the n-phonon band is

  ℛ_n(q) ≡ 𝔚^{(n)}(q)/𝔚^{(n)}_inc(q) − 1.                                                                                                                         (CW2.4)

At T = 0 in 3D, B_{κκ′}(ΔR) ~ ΔR⁻² (acoustic), so (CW2.3) converges absolutely for n ≥ 2; it replaces the [E] estimate z|j₀|c̄^{n} of WP2-v3 §3.3 (whose c̄ is B normalised by B_κ).
C1a: in a 1D diatomic chain the shell sum equals the BZ form to 10⁻⁶ (Poisson identity). Illustration (1D, not Si): ℛ₂ = −0.34 at q = 0.37 q_BZ, i.e. O(1), as WP2-v3 anticipated.
Limits: q ≫ max(n, 2W)q_BZ recovers (2.4); n = 1 must not be truncated in ΔR (WP2-v3 §2). Leading correction: the non-multiplicative valence vertex (§4), relative O(2W_κ).
**Spec.** Computed: S^{(2)}_coh(q,q̂,ω) for Si (then Ge, GaAs) on |q| ∈ [0.2, 10] keV (40 log points) × the irreducible set (≈ 20) of directions of a 590-point Lebedev grid, ω bins 0.5 meV;
and ℛ₂(q), ℛ₃(q) from (CW2.3). Level: τ = `nB=0|ng=0|nA=0|X=-|nT=0|K=multi-coh|Mg=-|nD=-` + `T=10mK;ref=normal;scr=-`. Method: stack A, then (i) B_{κκ′}(ΔR) for |ΔR_{κκ′}| ≤ 40 Å
from the 48³ eigenpairs (FFT), (ii) the Q₁ sum of (CW2.1) on 48³ with Gaussian δ (σ = 0.25 meV), Q₂ obtained by folding q − G − s₁Q₁. Convergence: 32³ → 48³ → 64³ until each
bin changes < 2%; σ ≤ bin/2; real-space radius until ℛ_n changes < 10⁻³. Cost ≈ 4×10⁶ mode pairs per (q, q̂) → ≈ 2×10⁹ evaluations, a few CPU·h after stage A.
Pitfalls: the Q = 0 acoustic point has weight (n+1)/ω → ∞ on a mesh but integrable measure: exclude it and add the analytic small-sphere term; the phase e^{iq·r_κ} uses unreduced q
(a reduced-q phase silently changes the κ ≠ κ′ interference); at T > 0 never use the real-space form (§3). Optional later run: on COMP-PH phonons, as the ledger states.

## 2. LE-49: pointwise error bound for the incoherent approximation at n_ph ≥ 2
**Item.** WP2-v3 §12.2, IF-10, IF-13: only a BZ-averaged, asymptotic statement existed; the κ ≠ κ′ size (≈ 0.16 at n_ph = 2) is [E].
**Derivation [D].** Cauchy–Schwarz on the basis sum in (CW2.1) (and its n-phonon analogue), |Σ_κ a_κ|² ≤ n_b Σ_κ|a_κ|², gives for every (q, ω) and n

  0 ≤ S^{(n)}_coh(q,ω) ≤ n_b 𝔓^{(n)}(q,ω),   𝔓^{(n)} ≡ (2π/Ω)(1/n!) Σ_κ |c_κ|²e^{−2W_κ} Σ∫ Π_i[Ωd³Q_i/(2π)³ (n_i + (1+s_i)/2)/(2ω_i)] |Π_i q·e^{s_i}_{κν_i}(Q_i)|²/M_κ^n
          × δ(ω − Σs_iω_i) (2π)³Ω⁻¹Σ_G δ³(q − Σs_iQ_i − G),                                                                                                  (CW2.5)

the **momentum-resolved self density** (each site's n-phonon density with total crystal momentum held at q). Averaging q over a BZ cell makes the last momentum uniform, so

  (Ω/(2π)³)∫_BZ d³p 𝔓^{(n)}(q + p, ω) = S^{(n)}_inc(q,ω) + (gradient terms, WP2-v3 (2.4)),                                                                 (CW2.6)

checked in 1D on the full mesh (C1c, agreement to 10⁻⁵). Hence the certified pointwise band: ΔS^{(n)}_coh/S^{(n)}_inc ∈ [−1, n_b𝔓^{(n)}/S^{(n)}_inc − 1]. For a Bravais lattice (n_b = 1) S_coh = 𝔓 exactly,
so the whole error is the momentum-conservation effect 𝔓/S_inc − 1, O(1) at band edges and → 0 in the q average. The lower end −1 is attained where momentum conservation
forbids the pair (kinematic gaps). The ω-integrated error is ℛ_n (CW2.4), exact. Both ends are computable from stack A; the [E] 0.16 is superseded by ℛ₂ (§1).
**Table flag rule (for G3/IF-13).** Define f_coh ≡ 𝔓^{(n)}/S^{(n)}_inc: for a Bravais lattice S_coh = f_coh S_inc exactly; for a basis (CW2.5) only certifies S_coh ∈ [0, n_b f_coh S_inc],
which is no 10% certificate, so pointwise accuracy needs S_coh itself. Rule: cells with n_ph ≥ 2 and (q ≲ n_ph q_BZ or |f_coh − 1| > 0.1) store the computed S_coh/S_inc from (CW2.1);
all cells store ℛ_n(q) (exact, rate level). 𝔓 and S_coh are accumulated in the same Q pass (spec as §1).

## 3. LE-50: T > 0 shell sum at n_ph = 2 (Ewald-type resummation)
**Item.** WP2-v3 §12.3: Σ_ΔR|Φ|² diverges linearly at T > 0 (classical B ~ T/ΔR); the shell sum exists only as a lattice Fourier sum.
**Derivation [D].** Poisson resummation of (CW2.3) at n = 2 turns the lattice sum of the product B·B into a BZ convolution of the two Fourier factors B̂(Q) = Σ_ν(2n+1)e e†/(2ω√(MM′)):

  𝔚^{(2)}(q) = (1/2Ω) ⟨ Σ_{ν₁ν₂} (2n₁+1)(2n₂+1) |F_{ν₁ν₂}(q,Q₁)|²/(4ω₁ω₂) ⟩_BZ,   Q₂ = q − Q₁ − G,                                                         (CW2.7)

i.e. (CW2.1) summed over s₁, s₂ and integrated over ω. This is the resummed form: each factor (2n+1)/2ω → T/ω² ∝ T/(c²Q²) is integrable in 3D, so 𝔚^{(2)} is finite for q ≠ G.
The only singularity is when both phonons are soft, Q₁, Q₂ → 0, i.e. q → G. There B̂ → Tê ê/(M_cell ω²) for every (κ,κ′) (acoustic e_κ = ê√(M_κ/M_cell)), Σ_ν(q̂·ê_ν)² = 1, and
∫d³Q/(Q²|k − Q|²) = π³/k (C2), so with k = q − G and c_min the slowest sound speed

  𝔚^{(2),th}(q) ≤ |Σ_κ c_κ e^{−W_κ} e^{−iG·r_κ}|² T² |q|⁴ / (16 M_cell² c_min⁴ |q − G|) + (regular),                                                         (CW2.8)

an integrable 1/|q − G| singularity weighted by the Bragg structure factor: the classical **second-order thermal diffuse scattering** law (first order ∝ 1/k², second ∝ 1/k; Warren,
X-ray Diffraction (1969) [UNVERIFIED]). The thermal piece is O((T/ω̄)²) relative near G and negligible at 10 mK (T/ω̄ ≈ 2×10⁻⁵). **Rule:** at T > 0 a code must use (CW2.1)/(CW2.7)
(mode space), never the real-space shell sum. No extra computation is needed beyond §1. Status: CLOSED.

## 4. LE-51: decay of the valence charge deformation at q ≫ q_BZ; L4 add-on 𝒵_κα(Q+G)
**Item.** WP2-v3 §12.4 and §10 "L4 add-on": the q ≫ q_BZ decay of δρ^val is [E]; DFPT δρ per Q to be Fourier transformed to |q| ≤ 20 keV.
**Derivation.** Split the linear charge vertex (WP2-v3 (1.2)) into rigid neutral atom plus deformation, with f^at_κ the all-electron atomic form factor:

  𝒵_κα(q) = q_α[Z_κ − f^at_κ(q)] − Δ_κα(q),   Δ_κ ≡ δρ_κ − q f^at_κ;   Σ_κ δρ_κα(G)|_{Q=0} = G_α ρ̄_e(G)  (uniform translation of all electrons).        (CW2.9)

The sum rule is exact and is the convergence test of a DFPT δρ table at Q = 0. (a) **Core tail [D for a hydrogenic core]:** a core follows its nucleus except for its polarisation by
the residual field at the nucleus; for H(1s) the Dalgarno–Lewis function ψ₁ = −(r + r²/2)cosθ ψ₀ (C3a) gives a deformation density with a non-analytic |x|x_z piece whose
transform falls as q⁻⁵ (coefficient −96 per unit field, C3b), against q·f ~ 16q⁻³ for the rigid shift: relative O((qa)⁻²) times the residual field, which per unit displacement is
≈ Φ_onsite/(Z e) ≈ 10⁻² a.u. in Si [E]. So the core part of Δ is negligible at every q. (b) **Valence tail:** what remains is the valence deformation, smooth on the bond scale
except for its orthogonality wiggles inside the core region (valence share of the contact density 0.5% in Si, §9). Strongest derived statement: 𝒵 → q(Z − f^at) up to a valence term
that decays faster than q f^at at large q. **Missing step:** the magnitude of Δ^val for 3 ≲ |q| ≲ 20 keV.
**Spec.** Computed: Δ_κα(Q+G) for |Q+G| ≤ 20 keV (≈ 4000 G), Si/Ge/GaAs. Level: GS, n_B = 0, linear in u, static DFPT, PBE; core frozen. Method: (i) |q| ≲ q_c ≈ 10 keV: ph.x fildrho
(stack A, the `drho` files of inputs/*/ph.in), FFT per Q, subtract q f^at_κ from ld1.x (§9 tables); (ii) all q: finite-displacement AE densities, ±0.01 Å in a 3×3×3 conventional cell
(216 atoms), PAW with AE reconstruction (stack B) or LAPW; Δ = [n_AE(+u) − n_AE(−u)]/2u − q f^at. Convergence: ecutrho such that |G|_max ≥ 1.5×20 keV (≈ 260 Ry), (CW2.9) sum
rule to 10⁻³, ±u linearity. Cost: DFPT add-on negligible; AE supercells ≈ 2 × 50 CPU·h. Pitfalls: pseudo δρ above q_c is an artefact of the pseudisation, not physics; at Q → 0
in GaAs ph.x returns the response at zero macroscopic field (the proper 𝒵, as (1.2) requires), do not add the LO field twice; e^{−W} bookkeeping of Δ is additive (WP2-v3 §1.2).

## 5. LE-52: non-perturbative anharmonicity (soft-mode, light-atom targets)
**Item.** WP2-v3 §12.5: outside the O(η²_anh) structure (6.2); scope statement exists.
**Derivation [D].** (i) Every integer ω-moment of S_self (and of the full S) is an equal-time correlator: with P(ω) ≡ S_self/∫S_self,

  𝓂_k ≡ ∫ω^kP dω,  𝓂₁ = 𝔨₁,  𝓂₂ = 𝔨₂ + 𝔨₁²,  𝓂₃ = 𝔨₃ + 3𝔨₂𝔨₁ + 𝔨₁³,  𝓂₄ = 𝔨₄ + 4𝔨₃𝔨₁ + 3𝔨₂² + 6𝔨₂𝔨₁² + 𝔨₁⁴  (𝔨_k of WP2-v3 (5.1)),                         (CW2.10)

exact for any local H, any anharmonicity (double wells, soft modes, quantum crystals) and any T; they need only static (PIMD) averages. (ii) **Markov–Krein bound** (Akhiezer, The Classical
Moment Problem (1965); Krein–Nudel'man [UNVERIFIED citations]): with the Hankel matrix H_{ij} = 𝓂_{i+j} (i, j = 0, 1, 2), v(x) = (1, x, x²), ϱ(ξ) = [v(ξ)ᵀH⁻¹v(ξ)]⁻¹, and the canonical
representation through ξ (nodes ξ and the two roots of v(x)ᵀH⁻¹v(ξ) = 0, weights ϱ(x_i)),

  Σ_{x_i<ξ} ϱ(x_i) ≤ F(ξ − 0) ≤ F(ξ + 0) ≤ Σ_{x_i≤ξ} ϱ(x_i),   F(ξ) = ∫_{−∞}^{ξ} P dω,                                                                     (CW2.11)

for every distribution with these moments (C4: brackets a skewed test S at 28 points). Every bin-integrated rate at fixed q is then bounded from four static numbers, without perturbation
theory. The band is wide at the peak (ϱ = 2/3 at the mean of a Gaussian) and narrow in the tails (ϱ ~ 𝔨₂²/(ξ − 𝔨₁)⁴), the threshold region that sets low-mass reach. At T = 0, S is
supported on ω ≥ 0 and the Stieltjes version (adding the shifted Hankel matrix 𝓂_{i+j+1}) tightens it. **Missing step:** the pointwise S(q,ω) needs real-time quantum dynamics of the
anharmonic lattice. **Spec.** Computed: F_s(q,t) or S_self(q,ω) for soft-mode or light-atom targets (KTaO₃, SrTiO₃, LiH, solid He). Level: n_A = all orders, approximate quantum
dynamics. Method: thermostatted ring-polymer MD (TRPMD) or centroid MD for the Kubo-transformed F_s(q,t), stochastic self-consistent harmonic approximation with its dynamical
extension, or TDEP with the bubble self-energy; each validated against (CW2.10) (exact moments from PIMD). Pitfalls: RPMD/CMD are exact only for the first moments and at short time;
every approximate S must be tested against the moment band (CW2.11), and violations flagged; double-well tunnelling splittings are missed by classical-like centroid methods.

## 6. LE-53: amorphous S_NN at n_ph ≥ 2 (distinct part)
**Item.** WP2-v3 §12.6, WP7-B2-v2 IF-B2-4 and gap 1: closed for S_self and S_dist at n_ph = 1 only.
**Derivation [D].** WP7-B2-v2 (B2.2.4) at order n, ω-integrated, for a statistically isotropic glass (one species; with several species replace g₂ by partial g_ab and c² by c_ac_b).
Write the static pair tensor B_IJ = B_L r̂r̂ + B_T(𝟙 − r̂r̂) + (traceless fluctuation), and average e^{−iq·r}(q·B·q)^n over q̂ at fixed r with μ = q̂·r̂ (C18: ⟨μ^{2k}e^{−ixμ}⟩ = (−1)^k j₀^{(2k)}(x)):

  𝔚^{(n)}_dist(q) = (𝓃_at c² e^{−2W} q^{2n}/n!) ∫4πr²dr g₂(r) Σ_{k=0}^{n} C(n,k)(−1)^k ⟨(B_L − B_T)^k B_T^{n−k}⟩_r j₀^{(2k)}(qr),                              (CW2.12)

with ⟨·⟩_r the configurational average over pairs at distance r ((CW2.12) is exact when B_IJ is uniaxial about r̂_IJ, which the configurational average at fixed r enforces for the averaged moments; no factorisation of ⟨B_L^aB_T^b⟩_r is assumed;
the spec's direct pair sums need no such assumption). Pointwise S_dist(q,ω) follows from Φ_IJ(t) in mode space (B2.2.4). Limits: q ≫ 1/d_nn → j₀^{(2k)}(qr) ~ (qr)⁻¹
decorrelation; n = 1 reproduces the Brillouin-peak result. Leading correction: boson-peak modes are not plane waves (affects small q only). At T > 0 use mode space (§3 rule).
**Spec.** Computed: 𝔚^{(n)}_dist(q), S^{(n)}_dist(q,ω) for n = 2, 3 for a-SiO₂, a-Si, SiN_x. Level: GS, n_A = 0, `K=multi-inc` for the self part, coherent distinct part; `ref=glass`.
Method: stack E; B_IJ for all pairs with r ≤ 15 Å from the eigenpairs; binned conditional moments (Δr = 0.02 Å); Φ_IJ(t) on 2¹⁴ time points. Convergence: g₂ and moments between
N = 1728 and 5184 atoms to 5%; ≥ 5 quenches. Cost ≈ 10² CPU·h per model after the MD (10⁴ CPU·h, WP7-B2). Pitfalls: finite-size gap 2πc/L (≈ 3–4 meV at L = 4 nm) removes the
lowest modes, so small-q, low-ω cells must be flagged; quench-rate dependence of g₂ and of the boson peak is a systematic (type M).

## 7. LE-54: 𝔨₃^X all-electron vs (5.2″); E^{Mig}_3 (J8) numerical
**Item.** WP2-v3 §12.7, WP0-v3 OW0-8, WP3-v3 O-WP3-3: the all-electron (W.5) evaluation of 𝔨₃^X = E^{Mig}_3 was never done.
**Derivation [D]** (hypotheses: leading BO order, point nucleus, cubic site, non-relativistic Coulomb, vibrationally averaged state). WP2-v3 (5.2′) gives the total third cumulant from the
contact density at every q, and (5.2)/J8 split it as 𝔨₃ = 𝔨₃^{GS} + E^{Mig}_3 with 𝔨₃^{GS} = (q²/2M²)⟨∂²_q̂E^ad_0⟩. Hence, up to the O(𝔨₁/ΔE₃, ⟨ω_ph⟩/ω_e) terms of J8 (i), the Migdal third moment needs no excited states:

  E^{Mig}_3(q) = (q²/2M_κ²)[Z_κe²⟨𝓃_e(R_κ)⟩_vib/3 − ⟨∂²_q̂E^ad_0⟩_vib] = E_R · [4πZ_κα𝓃_e(R_κ)/3 − Φ^{on}_κ]/M_κ,                                            (CW2.13)

Φ^{on}_κ the on-site force constant (q2r output, ∝ 𝟙 on a cubic site). **[CALC]** (ld1.x, all-electron atom, no pseudopotential, NR, PBE; code/CW2/ld1/): 𝓃_e(0) = 1766.3 (Si), 22458 (Ge),
20378 (Ga), 24676 (As) a₀⁻³, so **E^{Mig}_3/E_R = 1498 (Si), 16836 (Ge), 15416 (Ga), 18493 (As) eV²** (C5). Controls (no CONTROLS C1–C8 case applies to an atomic ground state):
N_el normalisation to 10⁻⁵, grid dx 0.008 → 0.006 changes 𝓃_e(0) by 3×10⁻⁸, LDA (PZ) −0.9% (Si), −0.4% (Ge); hydrogenic limit (C7). Crystal effects: valence share of 𝓃_e(0)
0.52% (Si), 0.10% (Ge), bounding the bonding change; Φ^{on}/(4πZα𝓃_e/3) ≈ 10⁻⁶ (Si). Thus 𝔨₃^X/𝔨₃^{GS} = 7.7×10⁵ in Si at √⟨ω²⟩ = 44 meV [E], confirming the WP2/WP3 [E].
**Relativistic flag.** Scalar-relativistic ld1.x raises the density at r_min = 6.5×10⁻⁵ a₀ by +7.8% (Si), +49% (Ge), +46% (Ga), +53% (As); the point-nucleus Dirac density diverges as
r^{2(γ−1)}. (CW2.13) is the value within the campaign's NR theory; a physical Ge/GaAs number needs (5.2′) re-derived with a finite nucleus and the Dirac current (IF-CW2-2).
**Remaining (validation only).** The (W.5) all-k evaluation must reproduce (CW2.13); a plane-wave RPA cannot (the integrand is converged only for p ≳ 5/a_{1s}, Si ≈ 250 keV,
ecutrho ≈ 4700 Ry), so the test is per shell: Σ_shells E^{Mig}_3[L7a, atomic] + E^{Mig,val}_3[(W.5), RPA+LFE, p ≤ 30 keV] = (CW2.13). Spec in §14.

## 8. LE-55: δM_κ, C_κ, P_Mig for Si, Ge, GaAs; P_Mig ≤ 10⁻³ validation
**Item.** WP3-v3 O-WP3-3, IF-13, §8 G6 (iv): δM/M ≈ 2.7, 2.4×10⁻⁴ are [E] (they are N_e m_e/M_atom, the free-atom TRK value).
**Derivation [D]** (leading BO order, Condon). Define the spectral measure of the nuclear force operator, dσ_κ(Δ) = Σ_a|q̂·⟨a|∇_{R_κ}V|0⟩|²δ(Δ − E_a + E₀), and ℐ_k ≡ ∫Δ^{−k}dσ_κ. Then

  δM^{q̂q̂}_κ = 2ℐ₃,  E^{Mig}_1 = q²ℐ₃/M_κ²,  P_Mig = q²ℐ₄/M_κ²,  E^{Mig}_3 = q²ℐ₁/M_κ²,  Φ^{el}_{κκ}(ω) = Φ^{el}_{κκ}(0) − ω²δM_κ + O(ω⁴),                     (CW2.14)

the last from Φ^{el}(ω) = ⟨∂²V⟩ − Σ_a2Δ_a|⟨a|∂V|0⟩|²/(Δ_a² − ω²): the drag mass is the ω² coefficient of the dynamical on-site force constant, so (Φ(ω) − ω²M)u = 0 moves with M + δM.
Since Δ ≥ E_g on the support, ℐ₄ ≤ ℐ₃/E_g, hence **P_Mig ≤ E^{Mig}_1/E_g = E_R(δM_κ/M_κ)/E_g** (C6), and by Cauchy–Schwarz P_Mig ≥ q²ℐ₃²/(M²ℐ₂). The G6 (iv) condition P_Mig ≤ 10⁻³ is
therefore guaranteed for E_R ≤ 10⁻³E_gM/δM: 4.3 eV (Si), 3.1 eV (Ge) with the [E] δM; above that it must be checked with the computed ℐ₄. With two static Sternheimer solves
(stack C at ω = 0; KS level with the SCF ΔV),

  |ψ⁽¹⁾_v⟩ = −(H − ε_v)⁻¹P_c ∂_q̂V|ψ_v⟩,  |ψ⁽²⁾_v⟩ = (H − ε_v)⁻¹P_c|ψ⁽¹⁾_v⟩:  ℐ₂ = 2Σ_v⟨ψ⁽¹⁾|ψ⁽¹⁾⟩, ℐ₃ = 2Σ_v⟨ψ⁽¹⁾|ψ⁽²⁾⟩, ℐ₄ = 2Σ_v⟨ψ⁽²⁾|ψ⁽²⁾⟩,        (CW2.15)

(factor 2 = spin), uncoupled in the second solve; the coupled (TDDFT) δM is the ω² slope of Φ^{el}(iω) from stack C. C_κ = 2ReΣ_a d_{0a}(∂V)_{a0}/Δ_a³ is the mixed analogue (E-field
first-order wavefunction in place of one ψ⁽¹⁾), bounded in §15. **Spec.** Computed: δM_κ (Q = 0 sublattice and on-site), ℐ₂–ℐ₄, P_Mig(E_R), C_κ for Si, Ge, GaAs. Level: τ n_B = leading
non-adiabatic (κ_BO⁴ amplitude), 𝒳 = RPA (SCF ΔV), harmonic. Method: stack C; on-site quantities = BZ average of the Q-resolved ones (8³ Q); valence from DFPT plus N_core m_e (exact
for rigid cores) for δM and atomic L7a per shell for P_Mig. Convergence: δM to 1% in k (12³ → 16³), iω fit points 0.1–0.5 eV. Cost ≈ 3× a DFPT (≈ 75 CPU·h Si). Pitfalls:
(CW2.15) is a sum over KS pairs, the many-body ℐ_k agree only at independent-pair level; the macroscopic field at Q = 0 in GaAs must be excluded (zero-field response); trace
check Σ_{κκ′}δM_{κκ′}(Q = 0) = N_e m_e per cell (J3) needs the core term.

## 9. LE-56: finite-q eκ factor Δ𝓃_κ(q) beyond hydrogenic 1s²
**Item.** WP2-v3 §12.8: L shell and valence anisotropy (∝ q̂_xq̂_yq̂_z) need an all-electron density.
**Derivation [D].** Inserting n(R_κ + ρ) = Σ_G 𝓃_e(G)e^{iG·(R_κ+ρ)} into the PV form (5.2″) and using PV∫d³ρ e^{−ik·ρ}[3(q̂·ρ̂)² − 1]/ρ³ = −4π[(q̂·k̂)² − 1/3],

  Δ𝓃_κ(q) = 3 Σ_G 𝓃_e(G) e^{iG·R_κ} [(q̂·(q − G)^)² − 1/3],                                                                                               (CW2.16)

which reproduces the uniform term 2𝓃_e at G = 0 and, for an isolated spherical density, the radial form 6∫𝓃 j₂(qρ)dρ/ρ (C20). **[CALC] spherical (atomic) part**, 𝔯_κ = 1 + Δ𝓃_κ/𝓃_e(0)
from ld1.x AE densities (NR PBE; C7):

| q (keV) | 10 | 30 | 51.1 | 102 | 300 |
|---|---|---|---|---|---|
| Si 𝔯 − 1 (AE) / hydrogenic 1s² (Z_eff 13.7) | 0.59% / 0.38% | 4.21% / 3.33% | 9.98% / 9.06% | 28.71% / 28.68% | 92.0% / 93.1% |
| Ge / Ga / As 𝔯 − 1 (AE) | 0.15 / 0.16 / 0.14% | 1.14 / 1.20 / 1.08% | 2.86 / 3.01 / 2.73% | 8.70 / 9.11 / 8.32% | 40.6 / 42.2 / 39.1% |

The L shell raises the O(q²) coefficient by ≈ 1.6× (not 2×) and matters only below ≈ 50 keV; above ≈ 100 keV the hydrogenic 1s² form is accurate to < 1% and is **not** a lower bound
(300 keV). The valence shells change 𝔯 by ≤ 1.3×10⁻³ (Si, 102 keV; core-only vs total), which bounds the crystal-valence correction [E]; the uniform term adds 2𝓃_e/𝓃_e(0) = 1.2×10⁻⁴ (Si).
SR densities lower 𝔯 − 1 by 7% (Si) to 30% (Ge) at fixed q (relativistic contraction; see §7 flag). **Missing step:** the crystal valence anisotropy (T_d, ℓ = 3).
**Spec.** Computed: Δ𝓃_κ(q,q̂) by (CW2.16) for Si, Ge, GaAs at the q of the impulse window. Level: GS density, PBE, AE. Method: core part from the atomic radial form (done);
valence AE density n^val(G) from stack B (PAW pp.x plot_num = 21 minus atomic core, or LAPW) to |G| ≤ 40 a₀⁻¹; angular dependence on a Lebedev grid. Convergence: |G| cutoff and PAW
augmentation radius until Δ𝓃^val changes < 10⁻⁵𝓃_e(0). Cost ≈ 10 CPU·h. Pitfalls: (CW2.16) converges for the core only through angular cancellation (use the radial form for the core);
NC pseudo-densities are unusable here (stack B).

## 10. LE-57: G3 multiphonon tables S(q,q̂,ω), P_ph(n_ph|q,ω), ρ^ph_κν
**Item.** WP2-v3 §10 G3 (i), (iii): tables S(q,q̂,ω), P_ph(n_ph|q,ω), ρ^ph_κν from DFPT → 48³ → (3.5) module, FFT at T > 0; never produced.
**Derivation [D]** (WP2-v3 (3.1)–(3.6), (8.2)). On cubic sites (Si, Ge, GaAs) D^{q̂}_κ = D_κ/3 exactly, so the per-atom PDOS (matdyn `dos=.true.`) is the complete input for the incoherent
part; branch content needs the 48³ eigenvectors. T = 0: forward march of (3.5); T > 0: FFT of e^{−2W}[e^{Φ_κκ(0,t)} − 1] with a Gaussian time regulator. C19 validates the T > 0 route
against the exact Einstein-site weights e^{−2W}I_n(2y√(n(n+1)))e^{nβω₀/2} to 10⁻⁵. P_ph(n|q,ω) = (2π/Ω)|c_κ|²e^{−2W_κ}(w_κ^{*n}/n!)/S_κ per order, ρ^ph by (3.6).
**Spec.** Computed: HDF5 tables of S(q,q̂,ω), P_ph, ρ^ph_κν, f_coh and ℛ_n (§2). Level: `K=multi-inc` (+ coherent n = 1 from (2.2), flagged cells from (CW2.1)); n_A = 0; T ∈ {10 mK, 1 K, 77 K}.
Method: stack A (or COMP-PH), PDOS on 48³ tetrahedra at 0.1 meV, a new ≈ 300-line module. Grids: q ∈ [0.1, 300] keV (400 log points), ω ∈ [0, 1 eV] at 0.1 meV and above that the IA
Gaussian with Edgeworth 𝔨₃^{GS}, 𝔨₄ (switch at x_R > 16). Convergence: f-sum (3.4′) to 10⁻⁴ per q; FFT window t_max ≥ 20π/δω. Cost: tables minutes after stage A.
Pitfalls: 2W_κ uses B_κ with (2n + 1); remove the Bragg δ(ω) analytically; with separately seeded Migdal use (1 − P_Mig)S^{GS}[M + δM] (WP2-v3 IF-2); GaAs needs species-resolved
2W (3.4″); n_ph ≥ 2, q ≲ n q_BZ cells carry the §2 flags.

## 11. LE-58: G3 PIMD inputs 𝔫_κ(p), E^kin_q̂, ⟨∂²E^ad_0⟩, 𝔨₄
**Item.** WP2-v3 §10 G3 (ii): PIMD inputs (≈ 10³ CPU·h); the ledger asks for the specification only.
**Spec (complete).** Computed: the nuclear momentum distribution 𝔫_κ(p), E^kin_q̂, the on-site BO curvature ⟨∂²_q̂E^ad_0⟩_vib (= 𝔨₃^{GS}, never 𝔨₃ − 𝔨₃^X, WP2-v3 §5.2), and the 𝔨₄ pieces
⟨(∂_q̂E^ad)²⟩ and ⟨(q̂·P)⁴⟩ − 3⟨(q̂·P)²⟩², i.e. the exact moments (CW2.10) of the GS sector. Level: BO surface from an MLIP fitted to PBE (or SCAN), quantum nuclei exact (PIMD),
anharmonicity to all orders, static. Method: stack D; 216-atom cells; centroid-virial estimator for E^kin; open-path (end-to-end) estimator for 𝔫(p) and ⟨P⁴⟩; analytic MLIP Hessian
averaged over beads for the curvature. Convergence: Trotter number P with βω_max/P ≲ 0.3 (at 10 K, Si ω_max ≈ 64 meV, P ≈ 250) or PIGLET/GLE acceleration (P ≈ 16–32); run at
T = 50–100 K and correct to T → 0 with the harmonic difference from stack A; < 1% statistical error. Cost ≈ 10³ CPU·h. Pitfalls: the open-path estimator is noisy for ⟨P⁴⟩ (≥ 10⁶
steps or displaced-path estimators); MLIP extrapolation beyond the training distribution biases 𝔨₄; use per-isotope masses where the isotope matters (§18).

## 12. LE-59: G13 / G-F2 anharmonic nuisance template
**Derivation [D].** (i) Linked-cluster form (exact for any H): with u(t) the struck-site displacement and W_n the contour-ordered connected n-point functions of q·u,

  F_κ(q,t) ≡ ⟨e^{−iq·u(t)}e^{iq·u(0)}⟩ = exp[Σ_{n≥2} (1/n!) Σ_{a+b=n} C(n,a)(−i)^a i^b W_n(t^a, 0^b)],                                                (CW2.17)

the a points at contour time t (e^{−iq·u(t)}, backward branch), the b points at 0 (e^{iq·u(0)}, forward branch), contour order fixed by the product; n = 2 gives −2W_κ + Φ_κκ(0,t). Perturbatively each W_n is a tree or loop diagram: W₂ is dressed by the Φ⁴ loop and the (Φ³)² bubble
(the A^ph_ν of WP2-v3 (6.2a)); W₃ at first order is −i∮_C dτ Φ^{(3)}_{abc}G_C(·,τ)³; W₄ has the Φ⁴ tree −i∮Φ^{(4)}G_C⁴ and the (Φ³)² tree with one internal line. The vertex rule is
checked in its Euclidean static form, d⟨x⁴⟩_c/dλ₄ = −4!ℓ⁸/(2ω) = −12ℓ⁸ (ω = 1), exactly (C8). (ii) **Time-reversal theorem:** S_κκ(q,ω) = S_κκ(−q,ω) for every T-invariant target and
site (Θn_κ(q)Θ⁻¹ = n_κ(−q)). W₃ at O(Φ³) is homogeneous of degree 3 in q, so

  first-order Φ³ terms cancel identically in S_κκ;  the leading anharmonic increment is O((Φ³)², Φ⁴): dressed W₂, W₄, and ½W₃²,                              (CW2.18)

confirmed numerically for a cubic oscillator (|ΔS| ∝ λ₃^{2.02}, C8). This fixes the structure of the template: Δ^τ_A = S[W₂^{dressed}, W₄, ½W₃²] − S^{harm}, constrained by WP2-v3
(6.1) and entered as WP6-v3 type T. **Spec.** Computed: Δ^τ_A(q,ω) for Si (then Ge, GaAs). Level: n_A = 1 in the η²_anh sense, T-renormalised. Method: phono3py fc3 (4×4×4 primitive,
128 atoms, pair cutoff 5 Å, ≈ 300 supercell DFT runs) → bubble spectral function on 24³ (`--spf`); hiPhive or TDEP fc4 → loop shift; W₃, W₄ as mode sums over (λ₁…λ₄) with
contour kernels built from G^>(t) = Σ[(n+1)e^{−iωt} + ne^{iωt}]/(2ω) (∝ N_k² per t, ≈ 10³ CPU·h); PIMD δE^kin_q̂ (§11) as the exact anchor of (6.1). Convergence: supercell 3×3×3 → 4×4×4,
cutoff 4 → 5 Å, 24³ → 32³; nuisance width from the spread. Pitfalls: the first-order Φ³ term must vanish numerically (a test of the contour placement); M-type nuisances break (6.1)
(WP2-v3 (6.1′)); phono3py linewidths are on-shell, the template needs the full spectral function. Optional Si fc3 run not attempted (phono3py absent; > 3 h).

## 13. LE-60: G11 lattice anisotropy S_ℓm tables
**Item.** WP2-v3 §10 G11: n_ph = 1 Lebedev projection and the prediction S_{ℓ≥4} = 0 in the incoherent part, untested.
**Derivation [D].** S_ℓm(q,ω) = ∫dq̂ Y*_ℓm(q̂)S(q,ω). For O_h Laue symmetry only A₁g harmonics survive (ℓ = 0, 4, 6, 8, …); the cubic isotropy theorem (WP2-v3 (8.2)) gives S_ℓm = 0 for all
ℓ > 0 in the harmonic incoherent part at every n_ph and T. The coherent one-phonon part carries ℓ ≥ 4: in continuum elasticity the ω-integrated one-phonon weight per direction is
∝ Σ_ν|q̂·e_ν|²/c_ν(q̂); for Si (C₁₁, C₁₂, C₄₄ = 165.7, 63.9, 79.6 GPa [UNVERIFIED]) S₂₀/S₀₀ = 10⁻¹⁴ (symmetry), **S₄₀/S₀₀ = +2.2%, S₆₀/S₀₀ = +0.02%** [E for inputs] (C9).
**Spec.** Computed: S_ℓm(q,ω) tables, ℓ ≤ 12 (cubic), ≤ 8 (Al₂O₃, SiC), and P_ℓ-projected 𝒢 (WP2-v3 G11). Level: `K=1ph-coh` at n = 1 with Umklapp to 30 keV; `K=multi-inc` with D^{αβ}_κ plus the
flagged coherent cells of §1–§2 at n ≥ 2. Method: §10 module per q̂ on a 590-point Lebedev grid (exact for degree ≤ 41), ω bins ≥ the dispersion change across neighbouring q̂.
Prediction test: |S_{ℓ≥4}|/S₀₀ < 10⁻⁶ in the incoherent part (numerical noise); a larger value is a mesh or symmetry-breaking artefact. Pitfalls: projecting a δ(ω − ω_q̂) line
without ω bins gives meaningless Y_ℓm coefficients; residual ℓ ≥ 4 in cubic crystals comes only from the coherent terms and 𝔨₄ (WP2-v3 §8.2).

## 14. LE-61: G6 Migdal one code path
**Item.** WP3-v3 §8 G6: one code path for L7a–d (all-electron RPA+LFE S^{ee}, convolution, neutron calibration); specification only.
**Spec (complete).** Computed: S^X_κκ(q;ω_ph,ω_e) of WP3-v3 (W.5) for Si and Ge, the quenching-subtraction kernel, the T2/LFE band. Level: τ n_B = leading non-adiabatic, T1–T3 (Condon,
GS vibrational final states, RPA+LFE), lattice K from G3. Method: (i) all-electron RPA+LFE S^{ee}_{GG′}(p,ω_e) (GPAW with AE reconstruction, or Yambo/BerkeleyGW with semicore) for
p ≤ 30 keV, ω_e ≤ 100 eV; cores as explicit shells via L7a; (ii) S^{GS}_κκ from the §10 tables; (iii) the convolution with the exact impulse bracket where |q·p|/Mω_e > 10⁻², p grid 50³
per shell. Closure tests: (a) E^{Mig}_3 per shell + valence = (CW2.13); (b) δM from the ω_e⁻³ moment = (CW2.14)/(CW2.15) and Σ = N_e m_e per cell; (c) P_Mig obeys P_Mig ≤ E_R(δM/M)/E_g;
(d) neutron calibration with 2210.04917 [ABS; ID verified] scattering lengths. Convergence: LFE matrix size (|G| ≤ 4 a₀⁻¹ → 6), k mesh 8³ → 12³, ω_e grid 0.05 eV. Cost ≈ 10³ CPU·h.
Pitfalls: never add (W.5) to a bare-mass, unit-weight S^{GS} (N1: (1 − P_Mig), M + δM); diagonal-only ε⁻¹ is an O(1) error (KKL); valence-only Z_κ(p) misses the core-dominated ω³ moment.

## 15. LE-62: crystal NR bremsstrahlung (W.13): Z*_κ(ω)
**Item.** WP3-v3 §6, §8: (W.13) needs Z*_κ(ω) by frequency-dependent DFPT; GaAs 10³–10⁴× atomic [E]; relevance [C].
**Derivation [D].** At zero macroscopic field (photon-proper, as (W.13) requires), with d the cell dipole operator and ∂V ≡ ∂V/∂u_κ(Q = 0),

  eZ*_{κ,αβ}(ω) = eZ_κδ_αβ − Σ_a 2Δ_a Re[⟨0|d_α|a⟩⟨a|∂_βV|0⟩]/(Δ_a² − ω²) = eZ*_κ(0) − ω²C_κ + O(ω⁴),   Z*_κ(ω → ∞) = Z_κ;
  |C_κ| ≤ [α₂ δM_κ(Q=0)]^{1/2},   α₂ = 2Σ_a|d_{0a}|²/Δ_a³ = Ω ∂ε_∞/∂(ω²)|₀ /(4π) (Gaussian),                                                                (CW2.19)

the bound by Cauchy–Schwarz on the same spectral sums (C6), δM_κ(Q = 0) the sublattice drag mass (intensive). [E] inputs (dε/dω² ≈ 0.6, 0.8 eV⁻² from n(ω) [UNVERIFIED]; δM ≈ N_e m_e):
|Z*_Si(ω)| ≤ 0.49(ω/1 eV)², consistent with WP3's [E] 0.05 at 1 eV; GaAs |Z*(ω) − Z*(0)| ≤ 0.90(ω/1 eV)² against Z*(0) = 2.1, so at ω_γ ≈ 1 eV the dispersion of Z* is not negligible a priori
and must be computed. Relevance of the channel stays [C] (WP3-v3 §6). **Spec.** Computed: Z*_κ(ω) for ω ∈ [0.05, E_g] and n_r(ω), then dℛ/dω_γdω_ph by (W.13) with S^{GS} from §10. Level: GS
lattice, electronic response TDDFPT (RPA, then ALDA), zero macroscopic field, harmonic. Method: stack C, mixed E(ω)–u response (zstar_eu generalised to complex frequency; fork batched
shifted solves); imaginary-axis fit for C_κ, real ω with η = 10–20 meV near E_g; scissor to the measured gap. Convergence: Z*(0) and ε_∞ against static DFPT to 1%; η → 0 extrapolation.
Cost ≈ 2× a DFPT per frequency batch (≈ 50 CPU·h GaAs). Pitfalls: PBE gap places the Z*(ω) resonance far below the true edge; using the full (macroscopic-field) response double counts
the photon line; Σ_κZ*_κ(ω) → 0 as ω → 0 (acoustic sum rule) and → Σ_κZ_κ as ω → ∞; at finite ω the sum is the electronic lag response to a rigid ion-lattice oscillation and is checked against that independent run.

## 16. LE-63: 2603.13052 Eq. (4.8) factor 2 (σ̄ normalisation): CONFIRMED
**[FT]** (literature/papers-CW2/2603.13052.html; PDF page numbers of v1). p. 12, below Eq. (4.5): "we have defined the reference cross section for each operator (σ_n^{(i)}) with
(c_i^{(n)})² = πσ_n^{(i)}/μ²_χn"; p. 4, Eq. (2.1) L = Σ c_i^{(n)} O_i Φ_χΦ_χΦ_nΦ_n (NR fields), so c is the NR Fourier potential and σ_n = μ²c²/π is the standard Born cross section. p. 15,
Eq. (4.8): "dσ/dq (q,v) = q/(μ²_χn v²) Σ_{i,j} σ_n^{(i)} F^{(n,n)}_{i,j}(q,v)" (arXiv HTML numbers it Eq. (22)); App. A.6: F_{1,1} = F_M. For 𝒪₁ with F = 1,
∫₀^{2μv}dq (4.8) = 2σ_n, whereas the standard qσ/(2μ²v²) integrates to σ_n (C10). **Verdict: (4.8) is 2× the standard dσ/dq**, as CONVENTIONS §9 already records. Consequences:
(i) the Migdal rate is unaffected, because (4.7) dP/dω = 2αq²/(3ω⁴m_N)∫… (p. 15) with the 1/m_N of (4.6) is ½ KKL and the product (4.6)(4.7)(4.8) equals KKL × standard dσ/dq
(C10; WP3-v3 C3b–d), and (4.5) follows from (4.1) with c² = πσ/μ² (re-derived here); (ii) p. 19: "The total DM-nucleus scattering cross section, σ(v), is obtain[ed] by integrating
Eq. (4.8) over the DM momentum", and the mean free path (4.9) λ⁻¹ = n_E∫dq dσ/dq uses it, so, if evaluated as printed (their code was not examined), their attenuation (overburden ceiling) for 𝒪₁ and 𝒪₄ carries a factor 2 (λ_mfp half the
standard value). Status: UNRESOLVED → **CONFIRMED** (owed text below).

## 17. LE-64: glass A^{IR}, B^{IR} and S_dist at n_ph ≥ 2
**Item.** WP7-B2-v2 §11.1, LIMITS B2-L3: C^{IR} = A^{IR} + B^{IR}ω² known only in form.
**Derivation [D]** (hypothesis: low-ω modes below the Ioffe–Regel frequency are plane-wave-like, e_Iν = ê_ν e^{ik·x_I}√(M_I/(N M̄)), ω = c_νk). Then p_ν = (NM̄)^{−1/2}Σ_I ε̂·Z*_I·ê_ν e^{ik·x_I}
(the masses cancel), so

  C^{IR}(ω) = Σ_ν ŵ^{pol}_ν 𝒮^{(ν)}_Z(ω/c_ν)/M̄,  𝒮^{(ν)}_Z(k) ≡ N⁻¹⟨|Σ_I ε̂·Z*_I·ê_ν e^{ik·x_I}|²⟩:   A^{IR} = Σ_ν ŵ^{pol}_ν𝒮^{(ν)}_Z(0⁺)/M̄,  B^{IR} = Σ_ν ŵ^{pol}_ν𝒮^{(ν)″}_Z(0)/(2M̄c_ν²),     (CW2.20)

ŵ^{pol}_ν the polarisation weights (1/3 each for an isotropic glass). A^{IR} vanishes iff the Born-charge field is hyperuniform (local neutrality); fluctuating charges with only global
neutrality give A^{IR} = ⟨|δZ*|²⟩/(3M̄)-type, the incoherent estimate of WP7-B2. C11 (disordered 1D chain): random charges C^{IR} = 0.988 vs 𝒮_Z/M = 0.989; neutral dimers 0.0024 vs 0.0024.
A^{IR}, B^{IR} therefore follow from **static** configurations and a charge model, without the Hessian; the Hessian is needed only above the Ioffe–Regel limit. S_dist at n_ph ≥ 2: (CW2.12), §6.
**Spec.** Computed: 𝒮^{(ν)}_Z(k) for k ≤ 0.3 Å⁻¹, A^{IR}, B^{IR}, c_ν; full C^{IR}(ω) from the Hessian as a cross-check up to ω_BP. Level: `ref=glass`, harmonic, rank-1 macroscopic ε.
Method: stack E configurations; Z*_I by DFPT on 192–648-atom subcells or a charge-equilibration MLIP fitted to them; 𝒮_Z on the k grid of the periodic cell. Convergence: L ≥ 4 nm so that
k_min = 2π/L is below the correlation length of Z*; 5 quenches. Cost ≈ 10³ CPU·h (DFPT Z*). Pitfalls: a locally neutral charge model forces A^{IR} = 0 by construction; enforce Σ_IZ*_I = 0 per
configuration; TLS and anharmonic absorption at mK are separate channels (WP7-T).

## 18. LE-65: isotope B−L channel: isotope-resolved Hessians and O(σ_M/M̄) correlations
**Item.** WP7-B2-v2 §11.2: isotope-resolved Hessians and the O(σ_M/M̄) vertex–eigenvector correlation were not computed.
**Derivation [D].** Same force constants, masses M_I = M̄(1 − δ^M_I) with δ^M_I ≡ (M̄ − M_I)/M̄. The mass-subtracted vertex δv_I = −iωgM_I(ϑ_I − ϑ̄) has zero mean and is independent between sites,
so at first order in δ^M all cross terms vanish and each site contributes through its own local DOS. For one site the Lifshitz Green function is exact: G_II = 𝒢^{lat}_{00}/(1 + δ^M_IM̄ω²𝒢^{lat}_{00}),
𝒢^{lat}_{00}(ω) = (1/3)N⁻¹Σ_{Qν}1/(M̄(ω²_{Qν} − ω² − i0)), and D_I = (2ωM_I/π)Im G_II, so

  D_I(ω)/D(ω) = (1 − δ^M_I) Im[𝒢^{lat}_{00}/(1 + δ^M_IM̄ω²𝒢^{lat}_{00})]/Im 𝒢^{lat}_{00}                                                           (exact, one isotope),   (CW2.21)
  Γ_iso = (πg²σ_wD(ω)/2Ω_at)[1 + κ^M_1h_iso(ω) + O((δ^M)²)],   κ^M_1 ≡ Σ_Ix_IM_I(ϑ_I − ϑ̄)²δ^M_I/σ_w,   h_iso(ω) ≡ −1 − 2M̄ω²Re 𝒢^{lat}_{00}(ω).                    (CW2.22)

C12: a 1D chain with one defect reproduces (CW2.21) at δ^M = 0.04 and 0.3 (in-band Re𝒢 = 0 in 1D, so there it tests the exact form). Natural Si (real masses): σ_w/(M̄ϑ̄²) = 1.879×10⁻⁴
(= C4a), **κ^M_1 = −0.054** (dominated by ³⁰Si, ²⁹Si); Debye model (ω_D = 64.5 meV) h_iso(50 meV) = −1.72, so the O(σ_M/M̄) correction is **≈ +9% at 50 meV [E for D(ω)]**, replacing the [E]
"≈ 3.5%". Pair terms are O((δ^M)²x). **Spec.** Computed: Γ_iso(ω) exactly for natural Si and the Lifshitz check. Level: harmonic, isotope disorder exact, `K=1ph-inc`. Method: Si IFC from stack A;
4096-atom supercells (8×8×8 conventional cells, 12288 dof, dense diagonalisation ≈ 10 min) with 10 random isotope realisations, the direct sum (B2.2.1) with real δv_I; Re𝒢 by Hilbert
transform of the 48³ PDOS for (CW2.22). Convergence: 10 → 20 realisations, 4096 → 13824 atoms (kernel polynomial method) to 2%. Cost ≈ 10 CPU·h. Pitfalls: the M_Iϑ̄ part must be
subtracted with the mass-weighted ϑ̄ (else a spurious acoustic term); δ^M_I referenced to the same M̄ as ϑ̄.

## 19. LE-66: isotope B−L: low-T in-band ε(ω) of Si
**Item.** The Γ_iso/Γ_EM ≈ 6.3×10³ uses the 293 K two-phonon α(50 meV) ≈ 0.55 cm⁻¹ (Deinzer & Strauch, PRB 69, 045205 (2004) [FT via VER-WP7-B2-A]).
**Derivation [D]** (harmonic two-phonon absorption with T-independent second-order dipole moments and frequencies). Net absorption weights: sum processes (1 + n₁)(1 + n₂) − n₁n₂ = 1 + n₁ + n₂ ≥ 1,
→ 1 at T = 0; difference processes n₂ − n₁ ≥ 0 (ω₂ < ω₁), → 0. Hence for every ω

  α(ω; T → 0) ≤ α(ω; 293 K)   ⇒   Γ_iso/Γ_EM (mK) ≥ 6.3×10³ at 50 meV,                                                                                (CW2.23)

since Γ_iso of (B2.4.2) is the net (T-independent) one-phonon rate. For pairs near 25 + 25 meV the sum factor is 2.18 at 293 K (C13), so the true mK ratio is likely ≳ 10⁴. The inequality
inherits the [E] on D(50 meV); anharmonic broadening and the quasi-harmonic shift (≲ 1%) are its leading corrections. **Data:** no measured mK/low-T in-band Si α(50 meV) was found
(arXiv and OpenAlex searches, this return): **GAP**. **Spec.** Computed: the T = 0 two-phonon ε₂(ω) of Si. Level: second-order dipole ∂Z*/∂u (WP2-v3 (4.5)), harmonic, ω < 2ω_max.
Method: finite differences of Z* (DFPT, epsil) in ±u displaced 2×2×2 supercells → ∂Z*/∂u; two-phonon joint density with sum weights only on 32³ (Deinzer–Strauch route). Cost ≈ 10² CPU·h.
Pitfall: the Si Raman/IR selection rules suppress many pair combinations; the measured 293 K curve mixes sum and difference processes, so only the T = 0 computation (or cold data) splits them.

## 20. LE-67: A4 GaAs electron-scalar rate as a near-cancellation
**Item.** WP7-B2-v2 §11.11, LIMITS B2-L1: the GaAs electron-scalar rate is a near-cancellation; Z*, ε_∞ and masses are needed to ≲ 1%.
**Derivation [D].** The observable vertex (B2.1.4) enters through d ≡ v_Ga/M_Ga − v_As/M_As, v_κ = Z_κ − Z*_κ/ε_∞. With Z_Ga/M_Ga = 0.4446 ≈ Z_As/M_As = 0.4405, ∂d/∂(Z*/ε_∞) = −(1/M_Ga + 1/M_As)
and ∂d/∂M_Ga = −v_Ga/M_Ga², so (C14): d = −1.18×10⁻³; +10% in Z*/ε_∞ → +45% in d; +0.01 u in M_Ga → +5.4%. For a rate (∝ d²) to 20%: **δ(Z*/ε_∞) ≤ 4.3×10⁻³ (2.2%)** and
δM_Ga ≤ 0.02 u (natural Ga 69.723 u is known far better). The combination needed follows from measurable quantities via Lyddane–Sachs–Teller:

  Z*/ε_∞ = [Ω μ(ω_L² − ω_T²)/(e²ε_∞)]^{1/2},   δ(Z*/ε_∞)/(Z*/ε_∞) = ½δε_∞/ε_∞ ⊕ (ω_Lδω_L − ω_Tδω_T)/(ω_L² − ω_T²),                                     (CW2.24)

so ε_∞ to 1% and Raman frequencies to 0.1% meet the requirement; [UNVERIFIED] values (a = 5.6533 Å, ω_T = 8.06, ω_L = 8.75 THz, ε_∞ = 10.9) give |Z*| = 2.16. PBE-DFPT ε_∞ for GaAs is
too large by tens of percent (gap problem) and cannot meet 2%; DFPT is used for the sign of Z*_Ga and as a consistency check. ε_∞ must be the low-T value (it changes by ≈ 2–3% between
293 K and 4 K [E]). **Spec.** Computed: d and the rate with its sensitivity band. Inputs: [FT] low-T ω_L, ω_T, ε_∞, a (Landolt–Börnstein, Raman and ellipsometry papers) to be collected;
DFPT Z*, ε_∞ from inputs/GaAs (stack A, epsil). Level: τ of B2-L1. Pitfalls: Ga isotope disorder (⁶⁹Ga/⁷¹Ga) adds a broadband channel of §18 type; using rigid-ion Q_j (§21) changes d by 3×.

## 21. LE-68: 2308.06314 Fig. 2 projection: RESOLVED (rigid ion, no δZ)
**[FT, text + code].** literature/papers-CW2/2308.06314.html (v1, 11 Aug 2023). p. 19, Eqs. (40)–(41): Π_ϕϕ and Π^i_ϕA are built from g_ΨN_jψ q·T and Q_jψ T with the electronic mixing term
−ωq^i(1 − ε_∞)g_e/e; p. 20: "consider only coupling to the electron number on each site in GaAs, N_Ga,e = 28, N_As,e = 36". Footnote 2 (p. 18) gives the Born-charge fix "δZ_j ≡ Z_j − Q_j …
replacing Q_jT → Z_jT in Eq. (38)" for the photon coupling but does not say it was used. The released code (github.com/kpardo/PhonoDark-abs, commit 0cbb3d5, 15 Aug 2023) settles it:
pda/couplings.py l.32 `Nj = self.mat.get_Nj()`, l.37 `Fe = einsum(Nj, qmag, qhat)`, l.42–43 mixing `ce*(1 − tr ε/3)/e·ωq`; pda/material.py l.85, l.97 N_j = Z_j − (pymatgen oxidation state);
pda/selfenergy.py l.183 `charge_list = Z − Nj` (Q = ±3) in Π_AA and the φA mixing. Born charges enter only through phonopy's non-analytic correction of the eigenmodes
(pda/phonopy_funcs.py l.107–111). **Status: RESOLVED: the Fig. 2 GaAs curve uses the rigid-ion structure**, so by WP7-B2 (C3) its electron-scalar rate is high by ≈ 1/0.11 ≈ 9 and its
g_e reach optimistic by ≈ 3, an order-of-magnitude statement (near-cancellation, §20). Caveat: the repository post-dates v1 by four days; no later change of these lines was examined.

## 22. LE-69: reflection/refraction force above σ_crit
**Item.** WP7-B2-v2 §11.3, LIMITS B2-L4: above σ_crit the force on heterogeneous test masses is reflection/refraction-dominated and not computed.
**Derivation [D for a planar face; E for numbers].** Above σ_crit the medium is an optical potential V_opt = 2π𝔟̄n₀/μ_χN (WP7-B2-v2 §3). A plane wave with normal velocity v_n meets a step with
k′² = k_n² − 2μV_opt: R(v_n) = |(k_n − k′)/(k_n + k′)|² (total reflection for k_n² < 2μV_opt, V_opt > 0). For a slab many de Broglie wavelengths thick (λ_dB ≈ 60 μm at m_χ = 20 eV, v = 10⁻³)
the thickness-averaged reflectance is R_slab = 2R/(1 + R) (C15, exact average over a period). The momentum transfer on a face with outward normal n̂ is the reflected flux:

  P_wall(n̂) = 2ρ_χ ∫d³v f_χ(v) (v·n̂)² R_slab(v·n̂) Θ(−v·n̂),   a_test = −Σ_faces A_f P_wall(n̂_f)n̂_f / m_test,                                         (CW2.25)

transmitted particles exit with their initial velocity and transfer no net momentum (absorption neglected). The equivalence-principle signal is Δa between two test masses through the
composition dependence of 𝔟̄n₀ in R; the isotropic part cancels and the DM wind v_E leaves a net term. Scale [E]: ρ_χv² ≈ 5×10⁻¹¹ Pa, so a 1-cm, 4.4 g/cm³ plate feels ≲ 10⁻¹² m s⁻²·R_slab
× (wind asymmetry). The source's claim is neither confirmed nor refuted here: the sign and size of Δa need (CW2.25) evaluated. **Spec.** Computed: Δa(σ_χN, m_χ) for the MICROSCOPE
cylinders over the SHM f(v). Level: optical potential (first order in 𝔟n₀, exact in V_opt/E_kin), specular faces, no absorption. Method: (CW2.25) per face of the axisymmetric geometry
with 1D transfer matrices along the local normal (curvature radius ≫ λ_dB), 4D (v, face) Monte-Carlo integration, ≈ 300 lines, CPU minutes. Pitfalls: roughness on the λ_dB scale makes
reflection diffuse; Born regime (σ < σ_crit) must reproduce WP7-B2 (B2.3.2) as R → V_opt²-small; multiple reflections between nested cylinders. Any bound from this channel stays [C] until run.

## 23. LE-70: L11 solid He near melting: remainder beyond the Gaussian
**Item.** WP7-B2-v2 §11.4, LIMITS B2-L5: no remainder bound beyond the Gaussian (SCHA) state at δ_Lind ≈ 0.3.
**Derivation [D].** The SCHA S (WP7-B2 (B2.4.1)) shares 𝓂₀ and 𝓂₁ with the exact S but not 𝓂₂–𝓂₄. Any S compatible with the exact moments (CW2.10), which are static and therefore exact from PIMD
at any Lindemann ratio, lies inside the Markov–Krein band (CW2.11). This is the remainder bound: |F_exact(ξ) − F_SCHA(ξ)| ≤ |F_SCHA(ξ) − F_canon(ξ)| + ϱ(ξ) pointwise in the CDF, valid at
δ_Lind ≈ 0.3 because no expansion is made. The same holds for the coherent S at q ≲ q_BZ, whose moments are S(q) (static structure factor), the f-sum q²/2M, ⟨|q·ĵ|²⟩ and the
Puff third-moment correlator (all equal-time). **Spec.** Computed: 𝓂₀–𝓂₄ of S_self and of the coherent S at |q| = 0.5–20 keV; the band (CW2.11) per q. Level: exact quantum statics, Aziz-type
He–He pair potential (no MLIP needed), n_A = all orders. Method: PIMD (i-PI) at V_m = 21 cm³/mol, T = 1 K, 180–432 atoms, P = 128 beads (ω_D ≈ 2 meV ≈ 25 K, βω_D ≈ 25); open-path estimator
for 𝔫(p). Convergence: P 64 → 128, N 180 → 432. Cost ≈ 10³ CPU·h. Pitfalls: Bose exchange is negligible for ⁴He solid statics at this T [E] but must be checked by permutation sampling once;
the band is wide at the peak, so it bounds threshold-limited (tail) rates, not line shapes.

## 24. LE-71: X10 valence for c_κ not ∝ M_κ
**Item.** WP7-B2-v2 §11.10, LIMITS B2-L9: for c_κ not ∝ M_κ the valence part needs non-adiabatic ⟨f|∇_{R_I}V|i⟩ in the crystal.
**Derivation [D]** (exact at k → 0, any BO order; WP7-B2 (B2.8.1) with ∇_{R_I}V = V⁻¹Σ_p ipU_κ(p)e^{−ip·R_I}n_e(p), U_κ = Z_κe²/p² for point nuclei with all electrons in n_e). The site sum of
c_I e^{ik·R_I} forces p = k + G. Writing c_κ/M_κ = c̃ + δc̃_κ, the c̃ part gives (B2.8.2); the remainder has the amplitude

  A_fi = −(1/(Ωω²)) Σ_G [k·(k + G)] 𝒲_G(k) ⟨f|n_e(k + G)|i⟩,   𝒲_G(k) ≡ Σ_κ δc̃_κ U_κ(k + G) e^{−iG·r_κ},
  Γ ∝ Σ_{GG′} [k·(k+G)][k·(k+G′)] 𝒲_G𝒲*_{G′} S^{ee}_{GG′}(k → 0, ω)/(Ω²ω⁴).                                                                                 (CW2.26)

Both the G = 0 term (k·k U(k) → e²Σ_κδc̃_κZ_κ) and the Umklapp terms (k·G 𝒲_G ⟨n_e(G)⟩) are O(k): the off-diagonal (local-field) S^{ee}_{0G}, S^{ee}_{GG′} are the whole Umklapp effect.
For equal δc̃ on both diamond sites 𝒲_G ∝ the basis structure factor, zero for (200), |·|² = 2, 4 for (111), (220) (C17). **Spec.** Computed: S^{ee}_{GG′}(k → 0, ω) for |G| ≤ 6(2π/a), ω from E_g to
100 eV plus core edges, per model δc̃_κ. Level: RPA+LFE (then ALDA), clamped nuclei (ω ≫ ω_max), all-electron or valence + per-shell cores. Method: Yambo / BerkeleyGW χ_{GG′}(q→0,ω) or
QE turbo_eels at q = G; contract with (CW2.26). Convergence: LFE size until Γ changes < 2%; k mesh 12³. Cost ≈ 10² CPU·h. Pitfalls: a diagonal-only ε misses the Umklapp terms entirely; the
G = 0 term must use the improper S^{ee} (it already contains 1/|ε|²); for c_κ ∝ M_κ up to the mass defect, 𝒲 is ∝ 10⁻³ and the result must reduce to (B2.8.2).

## 25. LE-72: L9/S8 κ_URF in MOF cells; giant-moment mechanisms
**Item.** WP7-B2-v2 §11.7, LIMITS B2-L8: κ_URF needs mode-resolved three-phonon decay in MOF cells; giant-moment mechanisms open.
**Derivation [D].** κ_URF (WP7-B2-v2 §7(c)) is the mean number (or energy fraction) of phonons that end in the long-lived chiral band with |L^{ph}| > L_th per created phonon. For a branching
cascade λ → λ′λ″ the expectations obey a linear system even though the process branches: with M_{λλ′} = Σ_{λ″}(1 + δ_{λ′λ″})Γ_{λ→λ′λ″}/Γ^{tot}_λ (mean number of daughters in λ′) and b_λ the
probability of being stable and chiral,

  𝒩_χ = (𝟙 − M)⁻¹ b,   κ_URF = Σ_λ w_λ 𝒩_{χ,λ}/Σ_λ w_λ,                                                                                                         (CW2.27)

finite because energy strictly decreases along the cascade (M nilpotent in energy order). C16 checks the algebra against Monte Carlo (single-daughter case); probabilities of "≥ 1 chiral
phonon" are not linear and use the branching generating functional 𝔊_x (WP5). **Spec.** Computed: Γ_{λ→λ′λ″} with daughter L^{ph}, isotope (Tamura) and boundary rates, κ_URF. Level: n_A = 1
(three-phonon, Fermi golden rule), harmonic L^{ph}. Method: phono3py fc3 for the MOF cell (≈ 10⁵ CPU·h at DFT; ≈ 10³ CPU·h with an MLIP fc3 validated on 50 DFT supercells), 10×10×20 grid,
(CW2.27) by sparse solve. Convergence: grid, fc3 cutoff, smearing of energy conservation. Pitfalls: L^{ph} is gauge-dependent within degenerate subspaces (diagonalise L there); L^{ph} is not
conserved in decay (WP7-B2 C23), so labels must be recomputed per daughter. **Missing step (gap):** giant-moment (4f orbit–lattice) one-phonon amplitudes ∂⟨s_e, L⟩/∂u need ab initio
crystal-field derivatives (CASSCF-SO on embedded clusters, ≈ 10³ CPU·h per molecule): not formulated beyond this pointer.

---
## Symbols introduced/used
Used as in NOTATION v4 and CONVENTIONS: q, Q, G, ω, ν, κ, e_{κν}, ω_{Qν}, n_{Qν}, M_κ, M_cell, c_κ, W_κ, B_κ, Φ_{κκ′}, ΔR_{κκ′}, j_BZ, q_BZ, S_inc, ΔS_coh, w_κ, D_κ, D^{q̂}_κ, 𝔨_k, E^kin_q̂, E^ad_0,
𝒵_κ, δρ_κ, f^at_κ, f^core_κ, Z*_κ, ε_∞, 𝓃_e(R_κ), Δ𝓃_κ, 𝔯_κ, a_{1s,κ}, E^{Mig}_1, E^{Mig}_3, P_Mig, δM_κ, C_κ, E_R, x_R, A^{IR}, B^{IR}, C^{IR}, p_ν, σ_w, ϑ_I, ϑ̄, Ω_at, V_opt, 𝔟_χN, σ_crit, δ_Lind,
L^{ph}, κ_URF, 𝔊_x, U_κ, S^{ee}_{GG′}, n_B, τ keys, WP6 types.
Introduced (NOTATION rows requested; collisions checked: none):
| Symbol | Meaning | Where |
|---|---|---|
| B_{κκ′}(ΔR) | static displacement correlation tensor (extends B_κ = B_{κκ}(0)) | (CW2.2) |
| 𝔚^{(n)}(q), 𝔚^{(n)}_inc, 𝔚^{(n)}_dist | ω-integrated n-phonon weight; its self and (glass) distinct parts | (CW2.3), (CW2.12) |
| ℛ_n(q) | exact rate-level coherence correction 𝔚/𝔚_inc − 1 | (CW2.4) |
| 𝔓^{(n)}(q,ω), f_coh | momentum-resolved self n-phonon density; table coherence flag | (CW2.5), §2 |
| 𝓂_k, ϱ(ξ) | normalised ω-moments of S; Christoffel (Markov–Krein) mass at ξ | (CW2.10), (CW2.11) |
| B_L(r), B_T(r) | longitudinal/transverse pair correlations in a glass | (CW2.12) |
| Φ^{on}_κ, Φ^{el}_{κκ}(ω) | on-site force constant; dynamical electronic on-site force constant | (CW2.13), (CW2.14) |
| σ_κ(Δ), ℐ_k, ψ⁽¹⁾, ψ⁽²⁾ | force-operator spectral measure; its inverse moments; first/second Sternheimer functions | (CW2.14), (CW2.15) |
| α₂ | ω² coefficient of the proper cell polarisability | (CW2.19) |
| 𝒮^{(ν)}_Z(k), ŵ^{pol}_ν | Born-charge structure factor; polarisation weights | (CW2.20) |
| δ^M_I, 𝒢^{lat}_{00}(ω), κ^M_1, h_iso(ω) | isotope mass defect; host on-site lattice Green function; isotope correlation coefficient; its spectral function | (CW2.21), (CW2.22) |
| R_slab, P_wall | thickness-averaged reflectance; reflected-flux pressure | (CW2.25) |
| 𝒲_G(k), δc̃_κ | Umklapp vertex of the non-mass-proportional coupling; its per-mass remainder | (CW2.26) |
| M_{λλ′}, b_λ, 𝒩_χ | cascade daughter matrix; chiral-stable probability; expected chiral count | (CW2.27) |

## Interface flags
| # | Owner / user | Quantity | This return | Action |
|---|---|---|---|---|
| IF-CW2-1 | WP5, WP6 (G3 tables; WP2-v3 IF-13) | coherence validity of multiphonon cells | f_coh = 𝔓/S_inc (exact for Bravais), computed S_coh/S_inc in flagged cells, exact ℛ_n (CW2.4) | adopt as the G3 validity columns |
| IF-CW2-2 **CHANGED** | WP3, WP0 (J8, (4.7′)), CW1 | E^{Mig}_3, 𝔨₃^X | closed form (CW2.13), [CALC] coefficients; NR vs SR: +8% Si, ≈ +50% Ge/Ga/As | WP3 quotes (CW2.13); a relativistic finite-nucleus (5.2′) is owed for Ge/GaAs numbers |
| IF-CW2-3 | COMP-PH (LE-16) | 8³ IFC, 48³ per-atom PDOS, eigenvectors, drho | consumed by §1, §2, §10, §13, §18 | COMP-PH outputs replace stack A; per-atom PDOS suffices on cubic sites |
| IF-CW2-4 | WP6 (type T), WP8-F G-F2 | anharmonic template | first-order Φ³ absent in S_κκ (CW2.18); increment O((Φ³)², Φ⁴) | template structure fixed; no M type |
| IF-CW2-5 | CW1 / WP1, WP8-U | GaAs low-T ε_∞, ω_L, ω_T [FT] | needed to 1% (§20) | collect measured values |
| IF-CW2-6 | WP3 (O-WP3-3), WP0 (N1) | P_Mig validity range | P_Mig ≤ E_R(δM/M)/E_g (CW2.14) | add to J3/N1 |
| IF-CW2-7 | WP7-B2, LIMITS | isotope channel | O(σ_M/M̄) = κ^M_1h_iso ≈ +9% [E]; mK ratio ≥ 6.3×10³ | numbers carried |
| IF-CW2-8 | CW8 (SOTA, NOTATION) | literature statuses; new symbols | 2603.13052 (4.8) CONFIRMED; 2308.06314 Fig. 2 RESOLVED; Symbols table | SOTA and NOTATION rows |
| IF-CW2-9 | WP2 (L4 add-on), CW1 | pseudo vs AE densities | NC pseudo-densities invalid above q_c ≈ 10 keV (stack B) | every finite-q charge vertex or Δ𝓃 above q_c uses AE |

## Owed corrections (target → exact text; not applied)
1. **LIMITS L7c, "Note / action"** → "Eq. (3.11) sign misprint; 1/m_N misplaced (4.6)→(4.7); (4.8) dσ/dq = qσ_nF/(μ²v²) is 2× the standard qσ_n/(2μ²v²) (CONFIRMED, R16 CW2 §16: their (c_i)² = πσ_n/μ²
   fixes σ_n as the Born cross section); the Migdal rate (4.6) is unaffected, the mean free path (4.9) inherits the 2×; correction ≲ 10⁻³".
2. **LIMITS B2-L1, last column**, replace "2308.06314 Fig. 2 projection **UNRESOLVED**" → "2308.06314 Fig. 2 uses the rigid-ion vertex (N_Ga,e = 28, N_As,e = 36; Q_j = ±3 in Π_ϕA), no δZ
   (RESOLVED, R16 CW2 §21: Eqs. (40)–(41); PhonoDark-abs 0cbb3d5 pda/couplings.py l.32–43, pda/selfenergy.py l.183): its GaAs electron-scalar rate is high by ≈ 9 (g_e reach ≈ 3), order of magnitude".
3. **state/CORRECTIONS.md, WP2-v3 §5.2″ (Core part)**, replace "The L shell roughly doubles the O(q²) coefficient [E] (its 8 electrons at ≈ 4× the radius), so the hydrogenic numbers are
   a lower bound on the deviation." → "All-electron atomic densities (R16 CW2 §9, [CALC]): 𝔯 − 1 = 0.59, 4.21, 9.98, 28.7, 92% (Si) at 10, 30, 51.1, 102, 300 keV; the L shell raises the O(q²)
   coefficient by ≈ 1.6× and is negligible above ≈ 100 keV, where hydrogenic 1s² is accurate to < 1% (not a bound)." Same section, §12 item 8 → "spherical part [CALC]; crystal valence anisotropy open".
4. **LIMITS B2-L3, last column**, replace "A^{IR}, B^{IR} not computed (gap 1)" → "A^{IR} = Σ_νŵ^{pol}_ν𝒮_Z(0⁺)/M̄, B^{IR} = Σ_νŵ^{pol}_ν𝒮_Z″(0)/(2M̄c_ν²) from static configurations (R16 CW2 (CW2.20)); values need the glass
   Z* charge model (spec CW2 §17); S_dist at n_ph ≥ 2: (CW2.12)".
5. **LIMITS B2-L4, last column**, replace "force above σ_crit not computed [C] (gap 3)" → "above σ_crit: reflected-flux pressure (CW2.25) with R_slab = 2R/(1+R) (R16 CW2 §22); MICROSCOPE geometry
   specified, not evaluated; any bound [C]".
6. **LIMITS B2-L5, last column**, replace "no remainder bound beyond the Gaussian near melting (δ_Lind ≈ 0.3)" → "remainder bounded pointwise in the CDF by the Markov–Krein band of the exact static
   moments (R16 CW2 (CW2.10)–(CW2.11)); PIMD moments specified".
7. **LIMITS "Numbers carried", isotope bullet**, append: "At mK Γ_iso/Γ_EM ≥ 6.3×10³ (derived: α(ω, T→0) ≤ α(ω, 293 K), R16 CW2 (CW2.23)); O(σ_M/M̄) correction κ^M_1h_iso ≈ +9% at 50 meV [E, Debye]
   (CW2.22); low-T measured α: GAP."
8. **state/CORRECTIONS.md, WP7-B2-v2 §2.2 (i) and §2.1 scope** "O(ΔM/M) (²⁹Si ≈ 3.5%) [E]" → "O(σ_M/M̄): exact first-order form (R16 CW2 (CW2.22)), +9% at 50 meV [E for D(ω)]".
9. **state/SOTA.md, WP3 literature line** "UNRESOLVED — whether 2603.13052 Eq. (4.8)'s 2× is an error (σ̄ normalisation)" → "CONFIRMED (R16 CW2 §16): (4.8) is 2× the standard; rate unaffected".
10. **state/CORRECTIONS.md, WP2-v3 §12 gaps 1–3, IF-10, IF-13; LIMITS L5 "Leading corrections"**, append: "exact ω-integrated coherent weight (R16 CW2 (CW2.3)–(CW2.4)), certified pointwise band
    (CW2.5)–(CW2.6), T > 0 resummed form (CW2.7) (second-order TDS 1/|q − G|)"; the "≈ 0.16 [E]" is superseded by ℛ₂.
11. **state/CORRECTIONS.md, WP3-v3 IF-13 / J3** append: "P_Mig ≤ E_R(δM_κ/M_κ)/E_g (R16 CW2 (CW2.14)); δM_κ = ω² slope of the dynamical on-site force constant".

## Proposed LIMITS rows
| # | τ / chain | Source formula | Status |
|---|---|---|---|
| CW2-L1 | J8 with WP2 (5.2′): E^{Mig}_3 = (q²/2M²)[Ze²𝓃_e(R)/3 − ∂²E^ad] (CW2.13) | WP3-v3 J8, WP2-v3 (5.2′) (campaign) | DERIVED (leading BO, point nucleus, cubic, NR); [CALC] coefficients |
| CW2-L2 | T > 0 coherent n_ph = 2 near G, (CW2.8) | second-order thermal diffuse scattering ∝ 1/\|q − G\| (Warren 1969 [UNVERIFIED]) | DERIVED as bound; source not read |
| CW2-L3 | single-isotope LDOS (CW2.21) | Lifshitz mass-defect Green function (classical [UNVERIFIED]) | DERIVED, C12 |
| CW2-L4 | GaAs Z*/ε_∞ from LO–TO (CW2.24) | Lyddane–Sachs–Teller / Born–Huang (classical [UNVERIFIED]) | DERIVED; inputs to collect [FT] |
| CW2-L5 | moment band (CW2.11) for any S | Markov–Krein (Akhiezer 1965 [UNVERIFIED]) | DERIVED as applied, C4 |
