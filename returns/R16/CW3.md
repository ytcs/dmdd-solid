# R16 / CW3: closure of LE-73…LE-96 (architecture rigour, Fano and edge-shell maps, basis extensions, WP7-D extensions)

Closure agent CW3, brief briefs/R16/CW3.md. Sources: state/LOOSE-ENDS.md §1, §1b, §2, §3; returns/R8/WP0-v3.md ("WP0 (n)"), R5/O4.md (read through CORRECTIONS §13:
m, f → Λ₀, Λ₊; λ → a^{off}; C1 → DC), R8/WP3-v3.md, R8/WP4-v3.md, R13/WP5-v4.md, R12/WP7-D-v2.md ("D (n)"), R12/WP7-B1-v2.md, R12/WP7-B2-v2.md, LIMITS.md,
CONVENTIONS.md (incl. R8, R13 amendments), NOTATION.md, CONTROLS.md, code/ENV.md. No referee report was read. No file outside this return and code/CW3/ was edited.
Checks: `python3 -I code/CW3/checks.py`: **28/28 PASS, ≈ 15 s** (cited CW3-Cn). Fork inputs: code/CW3/fork/{GaAs-LE76, Si-LE76}/{scf,ph,nscf,epw}.in (rtsc/bench layout,
`@PSEUDO@`), code/CW3/fork/mk_shell_k.py. Literature: fetched with lit.py into literature/papers-CW3/ (every arXiv ID resolved by the arXiv fetch), PDFs deleted at the end;
INSPIRE citation walk of 2011.01940 (59 citing records). Tags per CONVENTIONS §12; every new result here is **CLAIMED** (one return). Units HL, e² = 4πα.

## 0. Closure table
| Row | Item (short) | Status | Where |
|---|---|---|---|
| LE-73 | rigorous (H5)-free X0/X+ labels | CLOSED-AS-EXACT-GAP (single missing step: fibred LAP, shared with LE-82) | §1.1 |
| LE-74 | N_nuc-uniform PST; (6.1) remainder for low-lying states | low-lying order CLOSED [D given PST, FT]; N-uniformity CLOSED-AS-EXACT-GAP | §1.2 |
| LE-75 | 𝔉 = 0 in Ge with SOC (and Si) | CLOSED [D] (pair-space PT reality, N_e even) | §2.2 |
| LE-76 | 𝔉 size, Γ/δ map GaAs; K_ν ≥ 0 GaAs; Si d11 map | CLOSED (quantity derived + full spec; K_ν ≥ 0 [E]) | §2.3 |
| LE-77 | O(1) prefactor of the Fano coefficient | CLOSED [D] (prefactor 1, not 2π; non-phonon branch term) | §2.1 |
| LE-78 | all-electron E′_ee (orbit–orbit) | CLOSED (exact formula + spec; complete O(α²) list) | §3.2 |
| LE-79 | 𝒪₂ row | CLOSED (row 𝔳²_s added; matching derived) | §3.1 |
| LE-80 | Theorem D for magnetic insulators | CLOSED as theorem (charge-gap PST + quasi-boson sectors) with stated hypotheses; bin condition [C] | §1.3 |
| LE-81 | CDW phason/amplitudon | CLOSED-AS-EXACT-GAP (formula + spec, joint with LE-80) | §1.4 |
| LE-82 | D-g beyond conjecture | (G5′) 𝔥_off CLOSED [D, upper bound + spec]; U_qp, bin (c), Dirac α̃ ~ 1 CLOSED-AS-EXACT-GAP | §1.5 |
| LE-83 | relaxed electron channel ε_e | CLOSED [D] (exact Lehmann formula; Si counterexample derived) + spec | §3.3 |
| LE-84 | CC-1 many-body level | CLOSED (accepted at stated level) | §1.6 |
| LE-85 | 2305.05681 prefactors (O6) | CLOSED: CONFIRMED [FT] with one wording correction | §3.4 |
| LE-86 | charged current χ + n → p + e⁻ | CLOSED-AS-EXACT-GAP (row + distorted-wave spec) | §4.1 |
| LE-87 | massive ν̃ reduction | CLOSED [D] (exact NR identity) | §4.2 |
| LE-88 | two-insertion reductions | (b), (d) CLOSED [D]; (c) CLOSED-AS-EXACT-GAP | §4.3 |
| LE-89 | 1306.6089 factor 2; 2101.01241 u | CLOSED: amplitude CONFIRMED (convention fixed) [FT]; u derived, WP7-D wording corrected | §4.4 |
| LE-90 | 2501.05504 prefactor 32, M_n | CLOSED [D] (both derived; m_V² ≡ m_Vω_n) | §4.5 |
| LE-91 | drive ∝ ω²; δ_rel^a | CLOSED: drive [D]; 2δ_rel^a = −1.97×10⁻² (Cu) [FT] | §4.6 |
| LE-92 | near-T_CM multiferroic | CLOSED-AS-EXACT-GAP (scaling form + LLG spec) | §4.7 |
| LE-93 | 2011.01940 Eq. (9); R_{k′l′}; priority | CLOSED: statuses set (Eq. (9) defect stated; R normalisation CONFIRMED via citation chain [FT]; no prior continuity remark found) | §4.8 |
| LE-94 | dark Compton O(x²); x³; ALP Eq. (3) | CLOSED: vector DERIVED (source Eq. (2) = exact Dirac result); x³ split derived; **ALP Eq. (3) REFUTED** by (m_a+2m_e)/(m_a+m_e) | §4.9 |
| LE-95 | Bethe log constant; L-D12 | CLOSED: derived [D] + PDG [FT]; L-D12 tag kept with scope note | §4.10 |
| LE-96 | 1905.13650 penalty | CLOSED: CONFIRMED [FT] with framework breakdown | §4.11 |

---
## 1. Architecture rigour (WP0, O4, WP4)

### 1.1 LE-73: rigorous X0/X+ labels without (H5)
*Item.* O4 (iv″a–c) and the DC convention are proved at physics rigour (formal O(g²), distributions, Markov cascade); O4 §8 lists four obstructions to a theorem.
*Strongest derived statement.* (a) O4 (O4.6) [D, physics rigour]. (b) For the **single-fibre Friedrichs–Fano model** (one zero-phonon level coupled to finitely many
continua with C² form factors; the O4 toy) everything is exact: the spectral measure of the source is S_b(ω) = Γ_b|a_b + G(ρ + Υ)|², and CW3-C1 verifies (O4.6) and the
per-branch kernel to O(Γ²) (residual ratio 4.00 on halving Γ). (c) Two of the four O4 §8 obstructions are definitional, not missing proofs: the IR problem is removed by
*defining* X+ as "≥ 1 phonon with ω_Q > ε_res" (Bloch–Nordsieck; (a), (b) unaffected, (c) acquires ln(δ/ε_res) [C]); the Coulomb problem is a statement about deriving H₀
(screened bands, screened g) from H_C, which the URF takes as the reference input (WP0 §5) and is outside the X0/X+ question. Two genuine analytic steps remain: the
thermodynamic limit and continuum–continuum coupling. Both reduce to one estimate.
*Single missing step.* A **fibred limiting-absorption principle (LAP)**: for the fibre Hamiltonians H_K = H₀(K) + gV(K) at fixed total crystal momentum K, on the
window complement and away from JDOS singularities, a Mourre estimate uniform in g ∈ [0, g₀], in K, and in the cell number N, giving Hölder-continuous boundary values
⟨φ|(H_K − ω ∓ i0)^{-1}|ψ⟩ ∈ C^{0,θ} with N-independent constants. Given it, O4 (O4.6) and Theorem (b) hold as theorems for test functions in C^{1,θ}, with the remainder
C(g⁴ + Γ²/δ²)‖φ‖_{C^{1,θ}}; the degenerate-X0 case follows from the matrix form already used in §2.2.
*Why not now.* Mourre theory is available for one fibre with a discrete embedded level; X0 here is itself a band continuum, so the conjugate operator must be built per
fibre from the pair dispersion (dilation in the relative e–h momentum), and the uniformity in N is the same quasi-locality issue as §1.2. This is a mathematics project,
not a computation; no specification beyond the statement is needed for the book. Tag of (iv″) unchanged: [D] physics rigour, theorem [C] pending the LAP.

### 1.2 LE-74: (6.1) remainder for low-lying vibrational states; N_nuc-uniformity
*Low-lying states [D given PST, FT].* math-ph/0201055 (Panati–Spohn–Teufel, ATMP 7, 145) [FT], section "Energy cutoff" (journal pp. 175–176): for Born–Oppenheimer
Hamiltonians, whose gap does not grow with momentum, decoupling is proved "uniformly for energies below any λ ∈ ℝ, i.e. on Ran 1_{(−∞,λ]}(Ĥ₀)", by an auxiliary symbol
equal to H₀ on the cutoff region. Low-lying vibrational states (scaled nuclear momenta εp ~ κ_BO ≪ 1) lie in this range for any λ above the zero-point energy.
Hence (6.1) holds on them with the **same order O(κ_BO^{2(n+1)})** as in the semiclassical regime (absolute, operator-norm bound on the cutoff subspace). The v2
re-indexing worry is void: the theorem needs bounded momenta, not O(1) momenta. Not claimed: a *relative* bound against observables that are themselves small at low
energy (e.g. sideband weights ∝ κ_BO²): there the effective order is κ_BO^{2(n+1)−2m} for an observable of order κ_BO^{2m}.
*Correction of the obstruction list.* PST's gap hypotheses (G1)–(G3) (paper §2) concern the fast (electronic) spectrum σ_r(z) only. The **gapless acoustic branch is
not an obstruction** to (6.1); it is the IR issue of the X+ definition (§1.1). WP0 §6.2 "and the crystal has a gapless acoustic branch" is an owed W correction.
*N_nuc-uniformity: exact gap.* The PST constants involve the symbol bounds of H_e(R) in 3N_nuc slow variables; for local H_e the derivatives are sums of local terms, so
‖·‖ grows ∝ N_nuc and the bound is extensive. *Strongest statement:* for finite N_nuc with smeared nuclei and an energy cutoff, ‖(1 − Π_n)ĤΠ_nχ_λ‖ ≤ C_n(N_nuc, λ)κ_BO^{2(n+1)}.
*Single missing step:* a **quasi-local superadiabatic generator**: U_n = e^{iS_n} with S_n = Σ_x s_x a sum of exponentially localised terms (Lieb–Robinson-type bounds), so that
the error acting on a local observable (n_e(q) per volume) is intensive, C_n(N)/N bounded. This is the space-adiabatic analogue of the extended-system adiabatic
theorem for gapped lattice systems (Bachmann–De Roeck–Fraas, time-adiabatic case [UNVERIFIED for the precise statement]); the electronic gap Δ_ad ≥ E_g of (H2) is the
needed uniform gap. Tag of (6.1): [D] finite systems, [C] crystal limit, unchanged; the low-lying-state [C] is lifted.

### 1.3 LE-80: Theorem D-m, sectors for magnetic insulators
*Hypotheses.* (M1) clamped-nucleus charge gap: H_e(R) has a group of levels σ_r(R) (the low-energy spin manifold 𝒫_L(R): spin multiplets of a Mott or
charge-transfer insulator) separated from the rest by Δ_ch(R) ≥ Δ_ch > 0 uniformly on the essential support (as (H2), with "ground state" → "ground manifold");
(M2) a symmetry-broken reference selected by an infinitesimal field (WP4 (R1)) with a quasi-boson description: LSWT magnons a_{kν} plus harmonic phonons b, coupled
linearly by g_mp (WP4 §2.3); (M3) residual H_off = cubic and quartic magnon terms (relative 1/√(2|𝐒|), 1/(2|𝐒|)), anharmonic and magnon–phonon nonlinear terms;
(M4) conserving response (WP4 (R3)).
*Statement.* (i) [D given PST, finite systems; C crystal as §1.2] PST with σ_r = 𝒫_L (PST allows a band *group*, paper (G1)–(G3)) gives a superadiabatic projector Π
with (1 − Π)ĤΠ = O(κ_BO^{2(n+1)}) on energy-cutoff states. Sectors: **GS-m** = Ran Π (spin–lattice manifold: phonons, magnons, hybrids), **X-m** = charge excitations
across Δ_ch (X0-m/X+-m by reference phonon number as in Theorem D). Magnons are *not* adiabatically separated from phonons; both live in GS-m, so magnon–phonon
crossings and Goldstone modes are no obstruction. (ii) [D at quadratic order] The quadratic spin–lattice boson Hamiltonian (LSWT + harmonic + linear g_mp) is
diagonalised exactly by a symplectic (Bogoliubov) transformation U_b; the hybrid-quanta number N̂_hyb gives an orthogonal resolution of GS-m into sectors
𝒬^{D-m}_n with exact completeness. (iii) [D given U_b and (G5′)] With H_d ≡ Σ_n𝒬_nH𝒬_n and H_off from (M3), the D-g bound WP4 [8.1′] holds verbatim: its proof
(state-restricted Duhamel + Cauchy–Schwarz) uses only H = H_d + H_off and 𝔥_off(ψ_b), not Fermi statistics. So
|C^{cross}_ab| ≤ c_g𝔥_off(ψ_b)‖O_a|i⟩‖‖O_b|i⟩‖/Δω_bin², with 𝔥_off(ψ_b)² ≤ sup over few-hybrid states of ⟨H_off²⟩ (computable as §1.5). (iv) [C] Bin condition:
unique split on bins wider than the hybrid decay width Γ_mag + Γ_ph (as D-g (c)). (v) [D] Σ_n𝓜¹ is the spin f-sum WP0 (4.6e) under (M4); per-sector moments are not
fixed (WP4 (1.3): magnon share ≈ 0.084 z_ex|𝐒|²𝓃_mag/𝓃_e).
*Scope and limits.* Fails when Δ_ch is not ≫ ω_ph, J (itinerant magnets: use D-g with collective sectors as convention), and for fractionalised references (spin liquids:
spinon/parton sectors are fermionic, D-g (G1) with a gauge constraint, [C]). Leading correction: O(κ_BO^{2(n+1)}) leakage into X-m, plus O(J/Δ_ch)² charge admixture inside
𝒫_L (Schrieffer–Wolff, WP4 [1.1]). This replaces OW0-17/OW4-4 by Theorem D-m (i)–(iii) [D at the stated levels] and (iv) [C]; WP7-B2 IF-B2-11 spin-ordered targets
are covered by (i)–(ii).

### 1.4 LE-81: CDW phason and amplitudon (joint with LE-80)
*Formula [D, structure].* On a CDW mean-field reference (order parameter Δ_CDW at ±Q_CDW, coupled lattice distortion), the conserving response is the GRPA in the
2×2 space (k, k + Q_CDW): R = R⁰_CDW + R⁰_CDW Γ_{HF+ph} R, with Γ the functional derivative of the same self-energy that produced Δ_CDW (Hartree–Fock + phonon-mediated),
and the coupled phonon D^{-1}(q,ω) = D₀^{-1} − |g_{Q}|²Π_CDW(q,ω). The Ward identity of the broken translation makes the **phason** the Goldstone pole of R at Q_CDW + q
(ω_φ → v_φ|q| for incommensurate CDW, pinned by commensurability or impurities), the **amplitudon** the pole at ≈ 2Δ_CDW-softened ω_A. The DM vertex is n_e(q) at
q ≈ ±Q_CDW + G; S_ee then follows from WP0 (5.3) with R̃ → this conserving R̃ and ε including the CDW-reconstructed bands. Sector assignment: as D-g (b), the
collective modes are pair composites and their sector is a convention (D-m (ii) gives the bosonic number sector once U_b is the GRPA normal-mode transformation).
*Single missing step.* The conserving GRPA vertex on a **DFT** CDW mean field (supercell bands with the self-consistent distortion) is not implemented in any code;
model (tight-binding) versions exist (Lee–Rice–Anderson phason theory [UNVERIFIED as a citation]). *Spec.* TiSe₂ 2×2×2 CDW supercell (DFT-relaxed, PBE+U or hybrid to get
the CDW), Wannier90 bands; EPW on the normal primitive cell for g at Q_CDW; GRPA kernel with the static screened interaction (W from RPA) plus the phonon-mediated
term; q grid 32×32×8 around Q_CDW, ω to 50 meV with 2000 points; check the Goldstone theorem (ω_φ → 0 for an artificially incommensurate Q) and the f-sum (4.6) to
10⁻³. Cost ≈ 10³–10⁴ core-h (DFT supercell + kernel). Output S_ee(q,ω) near Q_CDW with τ `ref=CDW` (new metadata value, flagged).

### 1.5 LE-82: Theorem D-g beyond conjecture
*(G5′) with 𝔥_off computed [D, upper bound].* Take U_qp = 1 (bare Kohn–Sham/QP number of H₀ = bands + harmonic phonons) and H_off = all number-changing parts of
H_ep and of H_ee. For a one-quasiparticle source ψ_b, H_d conserves the QP number, so φ_s = e^{−iH_ds}ψ_b stays in the one-QP sector and
𝔥_off(ψ_b)² ≤ max_{nk} ⟨nk|H_off²|nk⟩ = max_{nk}[(1/N)Σ_{mνQ}|g_{mnν}(k,Q)|²(2n_{Qν} + 1) + Σ_{ee}^{(2)}(nk)],   Σ_{ee}^{(2)} = Σ over 2p1h final states of |W|²,
the **zeroth moment of the Fan–Migdal spectral function** (no energy conservation; −(1/π)∫dε Im Σ^{FM}_nk(ε) = (1/N)Σ|g|²(2n+1)), plus its e–e analogue. For a bilinear source
(pair) the electron and hole terms add. Size [E]: Al, λ ≈ 0.4, ω_D ≈ 36 meV, conduction width ≈ 10 eV: 𝔥_off ~ √(λω_DW/π) ≈ 0.2 eV, so the Duhamel bound needs
Δω_bin ≫ 0.2 eV; consistent with WP4's √(ΓW_c/2π). *Spec:* EPW, `g2sum(n,k)` = Σ_{mνQ}|g|²(2n+1)/N over the Wannier manifold and a 40³ (Al) fine Q grid at the
k-points of interest; the e–e part from the RPA screened W (BerkeleyGW/Yambo, 2p1h sum) [E for its size: ≲ the e–ph part below E_F + 1 eV]. Cost ≈ 10² core-h.
*Exact gaps.* (1) U_qp with error bounds beyond perturbation theory: not needed for (a) once U_qp = 1 is admitted (the price is a larger 𝔥_off); a dressed U_qp would
reduce 𝔥_off, and its existence is open (no gap, no PST). (2) **Bin condition (c)**: strongest statement is [8.1′]; the missing step is a second-order (golden-rule)
estimate |C^{cross}| ≲ Γ(ψ_b)/Δω_bin, which requires a limiting-absorption principle for H_d on the sectors: **the same fibred LAP as §1.1**. (3) **Dirac α̃ ~ 1:**
strongest derived statement: totals are convention-free (conserving RPA) and the split is non-unique at the benchmark (Γ_qp/ω ~ α̃² ≈ 0.8). New [D, sketch, one-loop]:
the Coulomb coupling of a 3D Dirac/Weyl semimetal is marginally irrelevant, α̃(ω) = α̃₀/[1 + (2N_Dα̃₀/3π)ln(Λ_D/ω)] (velocity renormalisation, QED-like β function), so
the bin condition is met asymptotically at low ω; at α̃₀ = 0.91, N_D = 1, Λ_D/ω = 10³: α̃ ≈ 0.39, α̃² ≈ 0.15, marginal [E]. Missing computation: Γ_qp(ω) from a
self-consistent GW (or RG-improved RPA) self-energy of the actual material (RG6 of WP4), spec as WP4 §5.4 with the running α̃(ω) as the check.

### 1.6 LE-84: CC-1 as a many-body statement
*Accepted at the stated level (closure).* Exact statements: totals (rates) are identical for in- and out-state weights (WP0 CC-1) [D, any target]. Within any theory
whose final-state interaction is a one-body mean-field potential short-ranged in the pair channel (TDH, ALDA), the bare outgoing pair is the asymptotic state and the
retarded weight (ε̃^{-1})_{G0} labels it [D]. As a statement about exact many-body eigenstates it needs Møller operators Ω₋ for the e–h pair relative to H₀; the
electron–hole Coulomb tail requires Dollard-modified wave operators, and the pair decays into multi-pair states (impact ionisation), so asymptotic completeness is not
available: [D, sketch]. This level is what the book states; no upgrade is needed for any rate or for the WP5 seeding (which uses the mean-field level).

---
## 2. Fano term and edge-shell maps (O4, WP3, WP5)

### 2.1 LE-77: the O(1) prefactor of the Fano coefficient [D]
*Hypotheses.* O4 (A1)–(A4); one non-degenerate X0 seed Λ₀ (degenerate case §2.2); first-emission branches b = phonon branches ν (final states Λ₊ ∈ ν) and non-phonon
channels x (impact ionisation, Auger, radiative) with widths Γ^{(b)}, Γ^{tot} = Σ_bΓ^{(b)}; off-shell production amplitudes a^{off}_f per unit g (O4 λ_f). Hypothesis
(F-x): **a^{off}_x = 0** for the non-phonon branches at the order kept (O(g²); their off-shell production is O(e²) and outside the truncation).
*Derivation.* The exact amplitude is A_f = g_f[a^{off}_f + G(ρ + Υ)], G = (ω − Ẽ + iΓ^{tot}/2)^{-1} (Z → 1 at this order), Im Υ = −½Σ_fΓ^{(f)}a^{off}_f. Expanding as in
O4 §3, the δ(ω − Ẽ) coefficient of Σ_{f∈b}2πδ(ω − E_f)|A_f|² is (i) from |G|²|ρ + Υ|²: (2π/Γ^{tot})Γ^{(b)}[|ρ|² + Σ_{b′}Γ^{(b′)}c_{b′}]; (ii) from 2Re(a^{off*}Gρ),
G → PV − iπδ: −2πΓ^{(b)}c_b, with c_b ≡ Σ_{f∈b}Γ^{(f)}Im(ρ*a^{off}_f)/Γ^{(b)}. Dividing by the total X0 weight 2π|ρ|²:

  K_b = (Γ^{(b)}/Γ^{tot})[1 + c̄^F − c_b^F],   c_b^F ≡ Γ^{tot}c_b/|ρ|²,   c̄^F ≡ Σ_bΓ^{(b)}c_b^F/Γ^{tot},   Σ_bK_b = 1,                                     (CW3.1)

i.e. the rate-unit Fano term is **𝔉_b = Γ^{(b)}(c̄^F − c_b^F)**, in K_b = (Γ^{(b)} + 𝔉_b)/Γ^{tot}. **The prefactor is 1.** O4 (O4.7), 𝔉 = 2πΓ^{(ν)}(c̄ − c_ν) with the
raw c = Im(ρ*a^{off}), is correct as a coefficient of δ in the spectral weight (units of 2π|ρ|²); the 2π entered only when WP5-v4 inserted the dimensionless c^F of
(W17) into the rate kernel. Two consequences: (a) c^F must be normalised with **Γ^{tot}** (NOTATION writes Γ_Λ₀; it must mean Γ^{tot}_Λ₀); (b) with Γ^x > 0 the
phonon-branch terms do not sum to zero: Σ_ν𝔉_ν = −Γ^x c̄^F and **K_x = (Γ^x/Γ^{tot})(1 + c̄^F)**, the interference also moves events between phonon and non-phonon first
steps (rests on (F-x)). CW3-C1a: exact Fano model vs (CW3.1) |ΔK| = 9×10⁻⁶, vs the WP5 2π form 1.2×10⁻²; C1b: K_x shift reproduced; C1c: residual O(Γ²).
*Bound and positivity [D].* With Σ_b𝔉_b = 0 and P̄ the midpoint of {P_b}, |ΔP(N|Λ₀)| ≤ (Γ^{ph}/Γ^{tot})max_ν|c_ν^F|·max_{b,b′}|P_b − P_b′| ≤ max_ν|c_ν^F|; K_b ≥ 0 iff
1 + c̄^F − c_b^F ≥ 0, sufficient 2max|c^F| ≤ 1. The [E] sizes are unchanged: |c_ν^F| = (Γ^{tot}/δ)(|a^{off}|δ/|ρ|)|sin φ_ν| ≲ 0.3Γ/δ (GaAs worst case), so |ΔP| ≲ 0.3Γ/δ
and K_ν ≥ 0 wherever Γ/δ ≲ 1.7 (the same two numbers WP5-v4 quotes, now with the correct formulas). θ_𝔉 prior unchanged in value.

### 2.2 LE-75: 𝔉 = 0 for PT-symmetric targets, with or without SOC [D]
*Hypotheses.* (P1) H (Coulomb, SOC, e–ph, anharmonic) and the reference (Gibbs) state are invariant under the antiunitary Θ = PT (inversion × time reversal); non-magnetic,
no B₀. (P2) **N_e even**, so Θ² = (−1)^{N_e} = +1 on the N-electron Fock sector (Si, Ge, diamond: every atom has even Z). (P3) The source O_b has definite Θ-parity:
Θn_e(q)Θ^{-1} = n_e(q) (P: q → −q, T: e^{−iq·r} → e^{+iq·r}); j(q) even; s(q), J(q) odd. (P4) Θ maps each phonon branch set ν (all Q; PT: Q → Q) onto itself (sum
degenerate branches into one Θ-closed set).
*Derivation.* An antiunitary with Θ² = +1 admits a Θ-real basis (Θ|α⟩ = |α⟩) of every Θ-invariant subspace (Gram–Schmidt with ⟨x|y⟩ real for Θ-even x, y). Choose it for
the degenerate X0 manifold D(Λ₀), for every final-state shell and for the initial eigenstates. Then for Θ-even Hermitian operators ⟨α|O|β⟩ = ⟨Θα|ΘOΘ^{-1}|Θβ⟩* = ⟨α|O|β⟩*:
ρ, g, a^{off} and Γ̂ (matrix on D) are real (for a Θ-odd O_b all source amplitudes are purely imaginary, a common phase). The only complex objects are resolvents. With
G = (ω − Ẽ + iΓ̂/2)^{-1}, Γ̂ real symmetric, ∫G dω over a symmetric window is −iπ·𝟙 (all eigen-channels) and ∫G†AG dω is real symmetric for real symmetric A
(in the eigenbasis γ_i of Γ̂ it is 4πA_ij/(γ_i + γ_j)). Hence both δ-type cross terms of §2.1, 2Re[(a^{off})ᵀg(−iπ)ρ] and 2Re[ρᵀM(−iπ g ᵀa^{off})], vanish: 𝔉_b = 0 for every
Θ-closed branch, per eigen-channel of Γ̂ and in trace. ∎ This upgrades Si, diamond from [D, sketch] and **Ge (SOC) from [C] to [D]**.
*Why the one-particle argument failed.* With SOC the single-particle Θ² = −1: ρ_cv and a^{off} are quaternion-real Kramers blocks and element-wise Im(ρ*a^{off}) ≠ 0
(WP5-v4). The pair (electron + hole) space carries Θ_pair = Θ_c ⊗ Θ_h with Θ_pair² = +1, where a real basis exists. CW3-C2a: Fano (t-odd) branch weight 1.5×10⁻¹³ for
Θ-symmetric random 4-dim manifolds vs 0.24 generic; C2b: element-wise Im ≠ 0 in the Kramers product basis; C2c: real basis constructed.
*Limits.* Odd N_e (charged defects) or magnetic order or B₀: Θ² ≠ +1 or no Θ; then only a doublet-trace statement survives [D, sketch]. GaAs (T only): T maps q → −q,
so O_b is not mapped to itself and 𝔉 ≠ 0 generically [C] (O4 conclusion unchanged). Off-diagonal 𝔇_ab between rows of opposite Θ-parity can carry Fano terms even in Si.

### 2.3 LE-76: the GaAs (and Si) Γ_Λ₀/δ map, the size of 𝔉 in GaAs, K_ν ≥ 0 [compute-formulate]
*Quantities (definitions, [D]).* For an X0 seed Λ₀ = (c, v, k; q) at Ẽ_Λ₀ outside the window: Γ^{ph}_Λ₀ = Γ_c(k+q) + Γ_v(k), Γ_n(k) = −2 Im Σ^{FM}_nk(ε_nk) (on-shell Fan–Migdal,
emission + absorption, n_Q at T); δ_Λ₀ = min{|Ẽ_Λ₀ − E^{ren}_min(q)|, distance of ε_ck to the nearest intervalley threshold (L, X for GaAs; X–X′ f/g for Si),
the local JDOS feature scale (|∇_kE_Λ|/|∇²_kE_Λ| at Λ₀)}. The d11 edge shell is {|ω − E_min(q)| < 3Γ}. The Fano coefficient is c_ν^F of (CW3.1), with
a^{off}_f = [M^{(2)}_f − g_{fΛ₀}ρ_{Λ₀}(ω − Ẽ_Λ₀ + i0)^{-1}]/g_{fΛ₀} evaluated on the final shell E_f = Ẽ_Λ₀ (the non-resonant remainder of D1 eq. (1), hole path and all
m ≠ c). K_ν ≥ 0 iff 1 + c̄^F − c_ν^F ≥ 0.
*[E] values now.* GaAs: Fröhlich LO emission for electrons above ω_LO, Γ_LO ≈ α_Fω_LO·√(ω_LO/E)·ln[(√E + √(E−ω_LO))/(√E − √(E−ω_LO))] ≈ 3 meV at E = 0.3 eV (α_F = 0.068,
ω_LO = 36 meV); Γ–L intervalley above ≈ 0.3 eV: 20–60 meV (WP3-v3 F8). With δ₀ = 0.3 eV: Γ/δ ≈ 0.01–0.2 off the shell. Hence **K_ν ≥ 0 holds for GaAs outside the
d11 shell by the sufficient condition Γ/δ ≲ 1.7 [E]**; |ΔP| ≲ 0.3Γ/δ ≲ 0.06 [E]. Inside the shell only totals and P(N_eh) from the unexpanded Dyson form are quoted.
*What is computed, and at which level.* Γ_n(k): n_g = 2 on-shell Fan–Migdal width, harmonic, DFPT-screened g (scr = DFPT; static, error O(ω_Q²/E_g²)), KS bands with a
scissor/valley correction (𝒳 = IP for the width); c^F: the same n_g = 2 amplitude as PAER (WP3 (M.1)) restricted to the X0 shell. Method: DFT (PBE) → DFPT phonons and
dvscf on a 6³ q grid → Wannier interpolation (EPW) → `elecselfen` on a fine grid; c^F from the WP3 response code (it already builds M^{(2)}) with the same gauge U(k) (O4-d2).
*Inputs (code/CW3/fork/).* GaAs-LE76: fully relativistic SG15 Ga_ONCV_PBE_FR-1.0.upf, As_ONCV_PBE_FR-1.1.upf (`noncolin`, `lspinorb`: the 0.34 eV split-off band sets
the hole widths), ecutwfc 90 Ry (energy converged to ≈ 1 mRy at 80–90 Ry with the SR set, code/COMP-PH/conv/conv_ecut_*.json; re-check with the FR files), a = 5.653 Å, 8³ k; ph.x 6³ q with `epsil = .true.`
(Z*, ε_∞ for `lpolar = .true.`); nscf 6³ full list, 48 spinor bands; EPW 16 spinor Wannier functions (Ga, As sp³; Ga 3d excluded, bands 1–10), `elecselfen`, T = 10 K,
`degaussw` 5 meV, fine q 100³, filkf from `mk_shell_k.py 24` (13824 k; generate in the workdir before the epw stage: run-fork.sh copies only *.in). Si-LE76: SR
Si_ONCV_PBE-1.2.upf, 70 Ry, 8 Wannier sp³ with disentanglement, `lpolar = .false.`, fine q 60³. Stages as rtsc/bench/run-fork.sh.
*Convergence.* Γ_n(k) to 5% under fine q 80³ → 100³ (GaAs; Fröhlich needs the dense q near Γ) and 40³ → 60³ (Si); `degaussw` 10 → 5 → 2.5 meV (the result must be stable
once σ ≪ Γ, else O4-d8 is violated); Wannier spread and band interpolation error < 10 meV within 3 eV of the gap. c^F: to 10% under the m-sum truncation (all
Wannier bands vs. +20 bands from the plane-wave basis).
*Cost.* GaAs FR DFPT ≈ 3–6×10² core-h CPU (≈ 5–10 GPU-h on the fork), EPW self-energy 13824 k × 10⁶ q ≈ 10⁴ core-h CPU (≈ 30–60 GPU-h); Si ≈ 1/10 of this. Above the box
limits: FORMULATED. *Outputs.* Γ_n(k) tables, the Γ/δ map on the (q, ω) grid of WP3-v3 §M10, c_ν^F(Λ₀), K_ν(Λ₀), the d11 shell mask; θ_𝔉 updated with the [CALC] value.
*Pitfalls.* (1) PBE puts the GaAs L and X valleys too low and the gap at ≈ 0.5 eV: intervalley thresholds set both Γ and δ, so apply a scissor plus valley offsets fitted
to experiment (or Wannier-interpolate HSE/GW bands) consistently in Γ, δ and the response code (O4-d3). (2) Polar divergence: without `lpolar` (g^L) the Fröhlich width is
wrong by O(1). (3) Gauge: ρ, g and a^{off} must share U(k) (CONVENTIONS §4) or c^F acquires random phases. (4) Kramers/degenerate manifolds: evaluate c^F in the
matrix form of §2.2 and report Θ-closed sums; for Si the code must return c^F = 0 to numerical precision (the check of O4-d7). (5) Smearing σ of δ(ω − E_f) identical in
Γ and in S^{X+} (O4-d8).

---
## 3. Basis extensions and relativistic f-sum (WP0)

### 3.1 LE-79: the 𝒪₂ row [D]
Galilean variables (WP0 (2.1)): v^⊥ = v_χ − v_s, v_s = (k + k′)/2m_s. Define per species the **velocity-square density row** a = (s, 𝔳²):

  ⟨k′|𝔳²_s(q)|k⟩ = (k + k′)²/(4m_s²) δ_{k′,k+q},   𝔳²_s(q) = Σ_{i∈s}(1/4m_s²){p_i,{p_i, e^{iq·r_i}}}_{sym} = Σ_i p_i·e^{iq·r_i}p_i/m_s² + (q²/4m_s²)n_s(q).     (CW3.2)

Then **𝒪₂^{(s)} = (v^⊥)² → v_χ² n_s − 2v_χ·j_s + 𝔳²_s** (CW3-C8). Only the trace of v_s⊗v_s is needed (𝒪₂ is the only quadratic 𝒪_i and it is a scalar), so one row per
species suffices: the basis becomes 17 rows per species. Relation to existing rows: 𝔳²_s is (up to normalisation) the scalar-NLO kinetic row 𝒯_e of WP0 §2
((1/8m²)ψ†∇↔²ψ has matrix element −(k + k′)²/8m², i.e. 𝔳²_e = −2·[(1/8m_e²)ψ†∇↔²ψ]); one row serves both uses. Screening: R̃_{𝔳²,c} ≠ 0 (spin-independent orbital
operator), so it is screened by WP0 (5.3). Size: relative to 𝒪₁ the halo term is v_χ² ~ 10⁻⁶ and the target term ⟨p²⟩/m² ~ (Z_effα)² (cores) or α² (valence).
Nuclei: same with m_s → M_κ and F^M_κ. CONVENTIONS §7 exclusion is replaced (owed correction).

### 3.2 LE-78: all-electron orbit–orbit f-sum shift [compute-formulate]
*Derived quantity [D].* Under (L) violated only by Breit–Pauli O(α²) terms, only terms at least quadratic in momenta change 𝓜¹_ee: mass-velocity (WP0 (4.6′)) and
orbit–orbit; spin–orbit, spin–other-orbit (linear in p) and Darwin, contact spin–spin (multiplicative) give [n†,[H, n]] = 0. From WP0 (4.6″) with FT[(𝟙 + r̂r̂)/r](k) =
(8π/k²)(𝟙 − k̂k̂), the exact orbit–orbit term in terms of the all-electron static structure factor 𝒮_st(k) ≡ ⟨n_e(k)n_e(−k)⟩/N_e (Bragg part included):

  𝓜¹_ee ⊃ −(𝓃_e/m_e²)∫d³k/(2π)³ v_C(k)[q² − (q·k̂)²]·½[𝒮_st(k+q) + 𝒮_st(k−q) − 2],                                                  (CW3.3)

finite: the uniform (G = 0) Bragg term sits at k = ∓q, where the transverse projector annihilates q (WP0 C18c). For pairs with q r_ij ≪ 1 (cores) it reduces to
δ_oo = −(4/3)E′_ee/(N_em_e); the Thomas–Fermi estimate δ_rel ≈ −0.23% (Si), −0.73% (Ge) [E] stands until computed.
*What is computed, level.* A ground-state two-body property (static pair density) at all-electron, scalar-relativistic level; correlation enters only through the xc hole
(≈ 1–2% of E_ee) and HF is adequate for 10% accuracy. *Method.* (i) Atoms (dominant, cores): X2C-Hartree–Fock (pyscf, `sfx2c1e`) for Si and Ge with uncontracted large
basis (ANO-RCC or cc-pwCV5Z uncontracted, plus tight s, p exponents to 10⁷), E_ee = E_J − E_K from the density matrix; the q-dependent version by evaluating (CW3.3) with
the HF 𝒮_st(k) = 1 + (1/N_e)[|n(k)|² − Σ_σ‖ρ_σ(k)‖²_F] (Hartree and exchange parts from the one-particle density matrix in momentum space). (ii) Crystal valence correction:
𝒮_st(k) from a PAW all-electron density (GPAW/Quantum ESPRESSO PAW reconstruction) plus the HEG xc hole for the valence; cores from (i). *Convergence.* E_ee to 10⁻⁴
relative under basis cardinal number 4 → 5; k integral of (CW3.3) to 10⁻³ (radial grid to k = 50/a_0 for Ge 1s). *Cost.* Minutes per atom (fits the box; not run,
compute-formulate); crystal correction ≈ 10 core-h. *Outputs.* δ_oo(q) for q ∈ [1, 100] keV, the total δ_rel = δ_mv + δ_oo per material, replacing the [E] in WP1 [E11],
WP6 and L17 (9.5). *Pitfalls.* (1) The uniform-Hartree subtraction must not be done by hand: (CW3.3) does it exactly; subtracting E_H of the crystal double counts. (2) Core
cusp: contracted valence basis sets underestimate ⟨1/r_ij⟩ for 1s² by several %. (3) Consistency of order: δ_mv and δ_oo are both O(α²⟨p²⟩/m²); including only one
mis-states the shift by ≈ 27%. (4) For q r_ij ≳ 1 (valence) the cos factor matters: use (CW3.3), not the angle average 4/3.

### 3.3 LE-83: the relaxed electron-channel static step [D] and its computation
*Derivation (exact Lehmann form).* For the electron-only channel, −v_CR_ee(q,0) = (2/π)∫₀^∞dω/ω L_e (WP0 (9.4)), and the Lehmann sum splits by Theorem D sectors.
The X-sector (above-phonon) part is the clamped electronic step 1 − ε^{-1}_{cl}(q) + O(κ_BO⁴). The GS sector at harmonic, adiabatic order (one phonon, 2W ≪ 1) contributes
through the electron density that follows the nuclei: n_e(q) ⊃ Σ_{Rκ}e^{iq·(R+τ_κ)}(−iq·Z^{(e)}_κ(q)·u_{Rκ}), with **Z^{(e)}_κ(q) the electron-following charge** (at
q → 0 in an insulator Z^{(e)}_κ = Z_κ𝟙 − Z*_κ, all electrons; Si: Z^{(e)} = 14, GaAs: Z_κ − Z*_κ). With CONVENTIONS §5 phonons:

  1 − ε_e^{-1}(q,0) = [1 − ε^{-1}_{cl}(q)] + 𝒢_GS(q) + O(κ_BO⁴, 2W),   𝒢_GS(q) ≡ (e²/(q²Ω))Σ_ν|Σ_κ q·Z^{(e)}_κ(q)·e_{κν}(q_r)e^{iq·τ_κ}/√M_κ|²/ω_ν(q_r)² ≥ 0.      (CW3.4)

*Limits [D].* (a) q → 0, LA branch, acoustic sum rule (Σ_κZ*_κ = 0 so Σ_κZ^{(e)}_κ = N_e per cell, e_κ ∝ √(M_κ/M_cell)ê): **𝒢_GS → Ω²_{P,e}/(c_L(q̂)q)²,
Ω²_{P,e} ≡ e²𝓃_e²/ρ_T** (𝓃_e all electrons): the electron-only probe compresses neutral matter, and the static step diverges as 1/q² for every solid. (b) LO term in a
polar crystal: the two-fluid model of WP0 (9.4′) is the R̃_eκ = 0 toy of (CW3.4) with optical modes only: step(0) − step(above phonons) = 𝔞_e²(1/ε_∞ − 1/ε₀) (CW3-C9a,c,
Lehmann residue), which reproduces the GaAs-like 2.30 (C9b). Sizes: Si Ω_{P,e} = 0.51 eV, GaAs 0.69 eV (CW3-C9d); the q → 0 form gives Ω²/(c_Lq)² = 1 at q* = 18 keV
(Si), 44 keV (GaAs), both > q_BZ, so the acoustic term alone gives **1 − ε_e^{-1}(q,0) ≫ 1 for q ≲ q_BZ** [D] (**Si counterexample derived**, no polarity needed).
At q = 1 keV (0.44 of Γ–X) neither linear dispersion nor Z^{(e)} ≈ Z holds for the valence part: **[E] ≳ 10²** (the q → 0 formula gives 3×10²). For q > q_BZ the
derived statement is (CW3.4) itself; its size needs Z^{(e)}(q) and the full branch sum: [E] ≳ 1 pending the computation below.
*Consequence (L17).* For ch = e with the lattice relaxed, step (iii) is not a usable bound: the GS lattice term dominates for q ≲ q_BZ [D] and is [E] ≳ 1 beyond; the usable electron-only bound is
WP0 §9.2 (iv) (ω_th above the phonon band, subtract the GS dω/ω weight), or (9.4) with (CW3.4) evaluated. ch = c and clamped ch = e are unaffected.
*What is computed, level.* (CW3.4) at n_B = 0 (adiabatic), harmonic, one phonon, DFPT-screened (ref = normal); the clamped term at 𝒳 = RPA+LFE. Inputs: ε_cl(q)
(RPA+LFE, WP1 route), phonons ω_ν(q_r), e_κν (DFPT, COMP-PH outputs reusable), Z*_κ, and Z^{(e)}_κ(q) at finite q. *Method for Z^{(e)}(q).* Frozen-phonon supercells
commensurate with q (Si 1×1×N along [100], N = 2…8): displace sublattice κ by u e^{iq·R}, SCF, Fourier transform Δn_e at q (pw.x + pp.x), linear in u (two amplitudes);
equivalently the DFPT induced density. *Convergence.* Z^{(e)}(q) to 1% (ecut, k); 𝒢_GS to 2% under q-grid refinement; check q → 0 against Ω²_{P,e}/(c_Lq)² with c_L from
DFPT elastic constants. *Cost.* ≈ 10² core-h (fits the box in parts; formulated). *Pitfalls.* (1) Pseudopotential DFPT gives the valence following charge Z_val − Z*:
add the frozen cores (Z_core, rigid) back, valid for q ≪ 1/a_core (Si 1s: q ≲ 30 keV). (2) Acoustic-sum-rule violation gives ω_ν → 0 with finite numerator: a spurious
divergence; enforce the ASR (matdyn `asr = 'crystal'`). (3) Use the unreduced q with q_r = q − G_q (CONVENTIONS §2). (4) For 2W ≳ 0.1 add multiphonon GS terms (the
static sum is over all GS states). (5) Direction dependence of c_L(q̂) and of the LO non-analytic term at q → 0.

### 3.4 LE-85: 2305.05681 against WP0 (2.9) and (3.5)–(3.6) [FT]
2305.05681 (Berlin–Trickle) [FT, arXiv v1]: Eq. (5) Γ ≃ −(1/m_a)Im[Π_aa + Σ_λΠ^λ_{aA}Π^λ_{Aa}/(m_a² − Π^λ_{AA})] is WP0 (3.5)–(3.6) (photon-proper + photon-reducible, Γ_net =
−Im Π/ω); with Π^i_{aA} = ig_aγγm_aB₀^i and Π^{ij}_{AA} = −ω²(1 − ε^{ij}) it gives Eq. (6) **Γ ≃ (g²_aγγ/m_a)Σ_λ(e_λ·B₀)²Im[−1/ε_λ(m_a)]** and, isotropic, Eq. (7)
Γ ≃ (g_aγγB₀)²Im[−1/ε(m_a)]/m_a; Eq. (3) R ≃ κ²(ρ_DM/ρ_T)Im[−1/ε(m_A′)] and the map g_aγγB₀ ↔ κm_a (Eq. (4)). **CONFIRMED** (prefactors, units, mapping; source
ρ_DM ≃ 0.4 → 0.3). One wording correction: WP0 (2.9) "ε_∥ along B₀" must read **B̂₀·Im[−ε^{-1}(m_φ)]·B̂₀ = Σ_λ(e_λ·B̂₀)²Im(−1/ε_λ)** (inverse tensor projected; equals
Im(−1/ε_∥) only for B₀ along a principal axis). Validity condition from the source footnote: target size ≫ skin depth (m_a Im√ε)^{-1}, otherwise boundary conditions
(D IF-D9 orientation factors) enter. O6 closed.

---
## 4. WP7-D extensions

### 4.1 LE-86: charged current χ + n → p + e⁻ (exact-gap closure)
*Row.* Species-changing nuclear rows O^{CC}_{F}(q) = Σ_I e^{iq·R_I}τ⁺_I (Fermi) and O^{CC}_{GT,β}(q) = Σ_I e^{iq·R_I}σ^β_Iτ⁺_I (Gamow–Teller), acting between nucleus (A, Z)
and daughter (A, Z+1); responses S^{CC}_ab(q,ω) = (2π/V)Σ_f p_i⟨i|O_a^{CC†}|f⟩⟨f|O_b^{CC}|i⟩δ(ω − E_f + E_i) with the nuclear transition strengths (B(F), B(GT) at q → 0).
*Strongest derived statement [D, allowed approximation].* The final e⁻ is not free: with χ at rest, q = −k_e, energy m_χ + M(A,Z) = M(A,Z+1)* + E_e + recoil, and in the
allowed approximation (k_eR_N ≪ 1, distorted wave evaluated at the nucleus) the rate factorises as Γ^{CC} = Σ_f ∫d³k_e/(2π)³ 2πδ(m_χ − Q_f − E_e) F(Z+1, E_e)
𝔏^{CC}_{ab}(k_e)⟨i|O_a^{CC†}|f⟩⟨f|O_b^{CC}|i⟩/(4m_χE_e), F(Z,E) = 2(1+γ)(2pR_N)^{2γ−2}e^{πη}|Γ(γ+iη)|²/Γ(2γ+1)², γ = √(1−(Zα)²), η = ZαE/p (1905.12635 Eqs. (6)–(13)
[FT via D]). *Single missing step.* The general case is outside the 𝔇 ⊗ S factorisation: the lepton is distorted by the target's own field, so the DM-side tensor
becomes an operator in target space. The URF form is the golden rule with the lepton out-state |e^{(−)}_{k}⟩ of the full (nuclear + atomic) Coulomb field,
Γ = Σ_f|⟨f; e^{(−)}|H_int|i; χ⟩|²; factorisation with F(Z,E) is its allowed limit. *Spec.* Nuclear: shell-model (KSHELL/NuShellX) B(F), B(GT) and q-dependent transition
densities for the target isotopes; lepton: Dirac–Coulomb continuum with finite nuclear size and atomic screening (Behrens–Bühring), plus bound-state capture e⁻ into
atomic orbitals (bound β-decay analogue); grids E_e to Q_max, 200 points; cost ≲ 10 core-h per isotope.

### 4.2 LE-87: massive ν̃ reduction [D]
With m_ν̃ = m_χ + Δ_χ, E_ν̃ = m_ν̃ + k²/2m_ν̃ + O(k⁴/m³), k = m_χv − q, (F.1) gives exactly at NR order (CW3-C7)
  ω^F_q(v) = ω_q^{(2.1)} + k²/(2m_χ) − k²/(2m_ν̃) = ω_q^{(2.1)} + (Δ_χ/m_ν̃)·k²/(2m_χ),
i.e. WP0 (2.1) with the outgoing kinetic energy evaluated with m_χ instead of m_ν̃; and 𝔇^F = 𝔇^{NR}·(m_χ/m_ν̃)(1 + O(v²)) from the relativistic normalisation 1/(4E_χE_ν̃).
Relative corrections O(Δ_χ/m_χ) in both places, now explicit. Tag [D, sketch] → [D].

### 4.3 LE-88: two-insertion reductions
*(b) [D].* Exact identity: S_{𝒯𝒯}(k,ω) is the two-point function of the effective operator 𝒯_eff(ω₁) = O_b(k₂)G(E_i + ω₁)O_a(k₁) + (1 ↔ 2). Local reduction: for ω₁, ω₂
below the lowest excitation Δ reachable by O_a, O_b, 𝒯_eff = −α_ab(0) + O(ω₁/Δ), α_ab the static mixed polarisability operator; for gauge couplings (photon, dark photon)
the ω → 0 limit is fixed by the seagull (Low's theorem), which (T.3)–(T.4) instantiate. *(d) [D].* For a quasi-free (Gaussian) target the four-point function of bilinears
equals the disconnected product S(q₁)S(q₂) plus connected loop terms of relative size O(1/N_eff), N_eff the number of electrons in the DM coherence volume.
*(c) exact gap.* Interference terms need R^{(2)}_{abc}(ω₁, ω₂); no reduction exists. Missing step: crystal quadratic response; spec: quadratic TDDFT (2n+1 DFPT for the
static part, Gonze–Vigneron) on the WP1 grids; HEG Lindhard quadratic response as the check; ≈ 10³ core-h.

### 4.4 LE-89: 1306.6089 amplitude and 2101.01241 u [FT]
*1306.6089 [FT, arXiv HTML].* Eq. (1) M(t) ≈ npμE*ε_Sd_n sin[(2μB_ext − m_a)t]/(2μB_ext − m_a)·sin(2μB_ext t); text: d_nε_SE* "is the energy shift produced between spin-up and spin-down
states". *2101.01241 Supplement [FT, in the arXiv PDF]* (S41): "each of the two nuclear spin states shifts by this amount, in opposite directions … Ω_a = (1/2)(2Δε/ħ)", the 1/2 from
the rotating-wave approximation; (S45) E* = Δε/d_n. *Resolution [D, CW3-C10].* For H = (ω_L/2)σ_z − dE σ_x cos(ω_Lt) the Rabi frequency is Ω_a = dE (numerical evolution:
M_⊥/sin(dE t) = 1.0001), so M_⊥ = M₀Ω_at at resonance. Eq. (1) at δω_L → 0 gives npμ(d_nε_SE*)t = M₀(d_nε_SE*)t. The two agree iff **d_nε_SE* is the per-level shift
(half the splitting)**, which is the convention of the CASPEr supplement and of 1306.6089's own Larmor term (ω_L = 2μB_ext with μ the moment, i.e. per-level shift μB).
Status: amplitude **CONFIRMED** with that convention (no factor 2); the envelope correction (half as wide) stands.
*u.* (S22)–(S23): M₁ = uM₀Ω_eT₂cos(ω₁t), u = ∫L(ω₀ + Δ − ω₁)h(ω₀ + Δ)dΔ, L = 1/(1 + (ω₀ − ω₁)²T₂²), h the normalised inhomogeneous line; (S24) u ≈ π/(ΓT₂); (S25) u =
(3.8 ± 0.3)×10⁻⁴. Derived [D] from (D.2) with the site sum of R_{I⁺I⁺}: the in-phase steady state averaged over h is uM₀Ω_aT₂, the quadrature vanishes for h symmetric about
ω₁ (CW3-C10b: u = 3.84×10⁻⁴ for their T₂, Γ). Correction to D §1.5: u is the overlap of the **absorptive Lorentzian with the inhomogeneous line only**; the DM line is
treated separately (Supplement §VII, (S54)–(S56): coherent drive, then the SHM power spectrum). Tag [D, sketch] → [D].

### 4.5 LE-90: 2501.05504 prefactor 32 and M_n [D]
Source [FT]: Eq. (2) U_n = (M_nω_n)^{-1/2}cos(nπz/L)exp(−(x²+y²)/2r_n²), ∫U_n² = (2ρω_n)^{-1}, M_n = ρπr_n²L₀; Eq. (6) δH ≈ −κ√(2ρ_V)(e_pt/ε₀)cosθ_Vcos(m_Vt)∫∇_zu;
P_s = 2πm_V|⟨n|δH₀|0⟩|²δ(m_V − ω_n) smeared. Derivation (CW3-C3): the normalisation fixes **M_n = ρπr_n²L₀** (a); ∫∂_zU_n d³x = [cos nπ − 1]·2πr_n²/√(M_nω_n) =
−4πr_n²/√(M_nω_n) for odd n, 0 for even n (c); |⟨n|δH₀|0⟩|² = 4κ²ρ_Ve²cos²θM_n/(ε₀²ρ²L₀²ω_n); with δ(m − ω) → (2γω²/π)/((m² − ω²)² + ω²γ²):
P_s = 32κ²(ρ_V/ρ²)(e_pt²/ε₀²)(M_n/L₀²)·**m_Vω_n**γcos²θ/((m_V² − ω_n²)² + (ω_nγ)²), i.e. Eq. (7) with m_V² ≡ m_Vω_n, identical on resonance (b). The 32 = 2π × 4 × 2 × 2/π.
r_n is a geometric input (their Eq. (3)–(4), paraxial plano-convex mode) entering only through M_n; FEM in the D §1.10 spec. Only odd n couple. LIMITS L-D4 "prefactor open"
→ derived.

### 4.6 LE-91: drive ∝ ω² and δ_rel^a
*Drive [D].* Hypotheses: modulus h(t) = δa/a uniform over the body (L_s ≪ ℓ_coh), adiabatic electrons (ω ≪ E_g), linear elasticity, isotropic dilation (cubic). Write the
lab displacement u_lab = u + h(t)ξ (ξ the material coordinate, u measured from the instantaneous equilibrium). The stress depends on strain relative to the new
equilibrium, σ = C:(∇u_lab − h𝟙) = C:∇u, so ρ(ü + ḧξ) = ∇·C:∇u: **the drive is the body force −ρḧξ**, ∝ ω²h; a static h is a relabelling of coordinates and
excites nothing. Mode force F_n = −ḧ∫ρξ·U_n = −ḧM°RJ_n (1508.01798 Eq. (8)). Corrections: non-cubic crystals → tensor h_ij; modulation of C (parametric, O(h u)); electronic
lag O(ω/E_g). Tag [D, sketch] → [D].
*δ_rel^a [FT].* 1809.02863 (Pašteka et al., PRL 122, 160801) Table II, fully relativistic DFT: (da_e/a_e)/(dα/α) at fixed a_B = **−1.97×10⁻² (Cu)**, −2.35×10⁻³ (Nb),
+3.65×10⁻⁴ (Al), −2.17×10⁻⁴ (Si), −1.61×10⁻¹ (Au); (da/a)/(dμ/μ) = −1.12×10⁻³ (Cu). In D (1.8) notation 2δ_rel^a ≡ dln(a/a_B)/dlnα, so dln a/dlnα = −1 + 2δ_rel^a with
**2δ_rel^a(Cu) = −0.0197**: WP7-D's [E] "0.01–0.02, negative" is CONFIRMED; the μ column confirms correction (a) ~10⁻³.

### 4.7 LE-92: multiferroic response near T_CM (exact-gap closure)
*Strongest derived statement.* (D.9) structure, P,T-breaking selection rule, FDT and causality [D]; near the transition, dynamic scaling gives
R_{s^z,trJ_e}(0,ω;T) = χ_×(T)Φ(ωτ(T)), χ_× ∝ |t|^{−γ_×}, τ ∝ ξ^z ∝ |t|^{−νz} [D given scaling]; 2102.10171 Eq. (10) is the single-relaxator (Ginzburg–Landau, damping by hand)
form Φ = 1/(1 − (ωτ)² − iη_Mωτ²) [D, sketch]. *Single missing step.* Φ and χ_× for the real material: finite-T spin dynamics with the tr J_e vertex. *Spec.* What: the
dynamic cross-correlation ⟨M^z(t)X(0)⟩, X = Σ_i tr J_e (the magnetoelectric source), at T ∈ [0.8, 1.2]T_CM. Level: classical spin dynamics on a DFT-derived Hamiltonian
(n_T = classical, ref = ordered/paramagnetic), beyond LSWT. Method: atomistic stochastic LLG (Langevin, α_G from data) with J_ij, DMI, single-ion anisotropy from DFT+U+SOC
(TB2J-type mapping) and the vertex coupling from Berry-phase polarisation derivatives ∂P/∂(S_i·S_j); FDT gives R. Convergence: L ≥ 4ξ (finite-size scaling), time step
< 1/(10ω_max), 10³ trajectories. Cost ≈ 10³–10⁴ core-h. Pitfalls: classical statistics below the Debye-like spin temperature (quantum thermostat), critical slowing down
(run time ≫ τ), and the sign convention of q (CONVENTIONS §3, binding for P,T-broken targets).

### 4.8 LE-93: 2011.01940 statuses [FT]
*R_{k′l′} normalisation.* 2011.01940 (v3, 2022) Eq. (8) cites [3] 1206.2644 and [12] 1703.00910; both print the same 4k′³ form (1206.2644 Eq. (3), 1703.00910 App. Eq. (5))
without the normalisation; 1206.2644 builds on its ref. [2] = 1108.5383, whose Eq. (6) [FT] prints |f_ion|² = (2k′³/(2π)³)Σ_{degen. occupied}Σ_{l′m′}|∫ψ̃*ψ_ie^{iq·x}|² with
"⟨ψ̃_{k′l′m′}|ψ̃_{klm}⟩ = (2π)³δ_{l′l}δ_{m′m}k^{-2}δ(k′ − k)". Status: **CONFIRMED** (convention inherited through the citation chain, not restated in 2011.01940; 4k′³ = 2 spins × 2k′³ as D §2.4(b)).
*Eq. (9).* Status set: **"not current-conserving at bound kinematics"** (algebra CONFIRMED: Eq. (9)/(F.4) = 1 − ω²/m_χ² + …); "paper wrong" is replaced by: Eq. (9) is a
free-vertex factorisation ansatz whose O(ω²/m_χ²) defect is of the same order as the omitted S_{J_TJ_T} and Dirac terms at K-shell kinematics; the quantitative verdict is
an **exact gap**: a Dirac–Hartree–Fock evaluation of (F.4) with S_{J_TJ_T} for Xe at m_χ = 56.5–100 keV (D §2.6 inputs). Independent support for the factorisation
critique [FT]: 2509.14534 (Ge–Sheng–Xing) shows the free-electron factorisation |M|² = |M_free|²|f|² is inconsistent for bound electrons (negative cross sections; 30–50%
relativistic changes) for scattering.
*Priority.* INSPIRE walk of 2011.01940 (59 citing records, titles screened), FT read: 2201.11905 (uses the same factorised |M|²|f_ion|², Eq. (14)), 2201.11497 (Eq. (6):
the same leading free |M|² for S, V, A, T), 2509.14534 (general factorisation critique, not continuity). **No prior statement of the continuity defect found** [E for
novelty]; 2201.11905 is downgraded from "priority candidate" to "not relevant".

### 4.9 LE-94: dark Compton (L-D10) and the ALP Eq. (3)
*Vector [D].* Exact tree-level QED for V (at rest) + e (at rest) → γ + e, by explicit Dirac traces with three V polarisations (CW3-C4a, gauge invariance checked), equals
2109.08168 Eq. (2) **at all x = m_V/m_e** (ratio 1 to 10⁻¹²); the source's App. Eqs. (7)–(12) are the full Dirac result. Series (normalised to n_eκ²σ_Th):
exact 1 − 3x/2 + 5x²/2 − (15/4)x³; (T.4) with NR recoil (ω′ + ω′²/2m_e = m_V) 1 − 3x/2 + 5x²/2 − (35/8)x³; (T.4) with exact two-body ω′ = m_V(m_V + 2m_e)/2(m_V + m_e):
… − (17/4)x³ (C4b, C4c). Hence: **agreement through O(x²) is DERIVED** (the omitted NR terms, Pauli spin and Klein–Nishina structure, sum to O(x³) because the comparison
is with the exact amplitude); the x³ difference 5/8 splits into **1/8 kinematic** (NR vs relativistic recoil) and **1/2 from the Dirac amplitude** beyond the NR seagull.
L-D10 status "observed" → DERIVED. *ALP (CLAIMED, three routes).* Exact tree-level QED with L = g_aee ia ψ̄γ⁵ψ gives
  σv = e²g²_aee m_a²(m_a + 2m_e)/[16πm_e²(m_a + m_e)³]                                                                                    (CW3.5)
(C5a). 2109.08168 Eq. (3) (= its Eq. (18)) is larger by **(m_a + 2m_e)/(m_a + m_e)** (2 at m_a ≪ m_e, → 1 at m_a ≫ m_e) (C5b). Route 2 (C5d): the source's own Eq. (16) |M|²,
integrated with the normalisation that takes its Eq. (9) to its (correct) Eq. (12), reproduces (CW3.5), not Eq. (18). Route 3: NR seagull from the derivative form
(on shell equivalent at tree level), **H_sg = −(e g_aee/2m_e²)(∂_ta)σ·A**, gives σv = e²g²m_a²/(8πm_e⁴), the m_a → 0 limit of (CW3.5) (C5c). Status of Eq. (3): REFUTED
(factor (m_a+2m_e)/(m_a+m_e); its small-mass limit "4m_a²/m_e²" should read 2m_a²/m_e²). D §3.4(iii)'s seagull "(e g_aee/2m_e)aσ·A" is corrected to H_sg above.

### 4.10 LE-95: Bethe log constant (L-D11) and L-D12
*Derivation [D].* From (S.1) at T = 0, split the k integral at k₀ with ω_max/v ≪ k₀ ≪ 1/a (dipole region below, f-sum saturated above). Below k₀, L(k,ω) ≈ L(0,ω) and
∫_{ω/v}^{k₀}dk/k = ln(k₀v/ω); above k₀ up to the Bethe ridge (ω = k²/2m_e meets ω = kv at k = 2m_ev) the inner integral is (π/2)ω_p² and gives ln(2m_ev/k₀). k₀ cancels
(CW3-C6b): −dE/dx = (4πZ²α²𝓃_e/m_ev²)ln(2m_ev²/Ī), **ln Ī = (2/πω_p²)∫₀^∞dω ωL(0,ω)ln ω** (C6a). Hypotheses: Born (Z_κα/v ≪ 1), v ≫ all shell velocities that
contribute (else shell corrections C/Z), NR; leading corrections: shell, Barkas (Z³, R^{(2)}, §4.3(c)), Bloch, density effect (relativistic). *Source [FT].* PDG RPP 2024
(Navas et al., PRD 110, 030001), ch. 34, Eq. (34.5) (Bethe equation) and §34.2.1: I is "a geometric average of the excitation energies of the medium weighed by the
corresponding oscillator strength" (quoting ICRU 49); in the NR limit (γ → 1, W_max = 2m_ev²) the bracket is ln(2m_ev²/I) − v² (C6c). Agreement; for condensed media the
oscillator-strength weight is the loss function, as in ln Ī above. L-D11: [D, sketch]/[UNVERIFIED] → **DERIVED + [FT]**. *L-D12:* tag [D, sketch] kept, scope note: out of
scope (DM-side decay, no target operator); its non-radiative part is inside URF via WP0 (3.3) with Δ_χ = −δ.

### 4.11 LE-96: 1905.13650 fixed-amplitude penalty [FT]
1905.13650 (Centers et al.) [FT, arXiv HTML]: abstract "overestimated by factors ranging from 3 to 10 depending on experimental details, model assumptions, and choice of
inference framework"; main Eq. (7) γ^{stoch}_{95%} ≈ 3.0γ^{det}_{95%} (Bayesian, Berger–Bernardo prior, data at the detection threshold A = A^{dt}; "increases for higher
CL and decreases for smaller A"); ≈ 10 with a uniform prior (not invariant under reparametrisation); ≈ 2.7 frequentist (marginal likelihood); ≈ 8.4 for pseudoscalar
"wind" couplings with velocity and phase also stochastic; 4.4 from the Neyman-construction MC (Supp. Eq. (32)); regime T ≪ τ_c; conclusion "≈ 2.7–10". **CONFIRMED.**
L-D3 text: "fixed-amplitude penalty 2.7–10 (1905.13650 [FT]: 3.0 Bayesian, 2.7 frequentist, ≈ 8.4 with velocity and phase for gradient couplings; framework-dependent)".

---
## Symbols introduced/used
**Used as defined (NOTATION v4 + R9):** q, ω, Δ_χ, κ_BO, Γ_Λ₀, Γ^{ph}, Γ^x, Γ^{tot}, a^{off}, ρ_Λ₀, Ẽ_Λ₀, Z_Λ₀, 𝔉_{Λ₀,ν}, c_ν^F, 𝒦_{Λ₀→Λ₊}, δω, DC, 𝒞_adm, GS, X0, X+, 𝒫₀, Π (PST
projector), U_qp, 𝒬^{D-g}, 𝔥_off, H_d, H_off, Δω_bin, R, R̃, S, L, ε, ε_∞, ε₀, v_C, Z*_κ, e_κν, ω_ν, ℓ_Q, M_κ, M_cell, Ω, ρ_T, 𝓃_e, ω_p, 𝓜¹, 𝒦^{oo}, H_oo, E′_ee, δ_oo,
δ_mv, n_e, j, s, J, 𝒯_e, 𝔇, 𝔇^F, 𝔏, ν̃, m_ν̃, ω^F_q, 𝔘_C, h_mod, δ_rel^a, Ω_a, ω_L, δω_L, T₂, M₀, β_s, u (source), M_n, r_n, γ_n, Q_DM^eff, Ī, 𝒯^{(2)}, 𝒯^C, R^{(2)}, x = m_V/m_e,
σ_Th, ω′, e_λ, e′_λ′, t_coh, ℓ_coh.
**Introduced (proposed NOTATION rows; collisions checked against NOTATION v4):**
| Symbol | Meaning | Where |
|---|---|---|
| c_b^F, c̄^F, K_b, 𝔉_b (b ∈ {ν, x}) | dimensionless Fano coefficient normalised with Γ^{tot}; first-emission branching incl. non-phonon branch x; rate-unit Fano term | (CW3.1) |
| Θ | antiunitary PT; Θ² = (−1)^{N_e} on the N-electron sector | §2.2 |
| δ_Λ₀ | off-shell scale of seed Λ₀ (min of edge distance, valley threshold, JDOS scale) | §2.3 |
| 𝔳²_s(q) | velocity-square density row, ⟨k′|𝔳²|k⟩ = (k+k′)²/4m_s² (𝒦 avoided: kernels) | (CW3.2) |
| 𝒮_st(k) | all-electron static structure factor ⟨n_e(k)n_e(−k)⟩/N_e (S is dynamic) | (CW3.3) |
| Z^{(e)}_κ(q) | electron-following charge (tensor); q → 0: Z_κ𝟙 − Z*_κ | (CW3.4) |
| 𝒢_GS(q), Ω_{P,e} | GS lattice part of the electron-only static step; Ω²_{P,e} = e²𝓃_e²/ρ_T | (CW3.4) |
| GS-m, X-m, 𝒬^{D-m}_n, U_b, N̂_hyb | Theorem D-m sectors; symplectic magnon–phonon normal-mode map; hybrid-quanta number | §1.3 |
| α̃(ω), N_D, Λ_D | running Dirac fine-structure constant; number of four-component nodes; band cutoff | §1.5 |
| O^{CC}_F, O^{CC}_{GT}, F(Z,E) | charged-current nuclear rows; Fermi function | §4.1 |
| H_sg | NR ALP–photon seagull −(eg_aee/2m_e²)(∂_ta)σ·A | §4.9 |

## Interface flags
| # | Owner | Quantity | This return |
|---|---|---|---|
| IF-CW3-1 | WP5 (W15)/(W17), K_ν; WP6 θ_𝔉; WP3 §M4 F8; O4-d7 export | Fano kernel | 𝔉_b = Γ^{(b)}(c̄^F − c_b^F), prefactor 1, c^F with Γ^{tot}; non-phonon branch K_x = (Γ^x/Γ^{tot})(1 + c̄^F); bound |ΔP| ≤ (Γ^{ph}/Γ^{tot})max|c^F|·spread; [E] numbers unchanged |
| IF-CW3-2 | WP0 §6.2 (iv″b), WP3, WP5, O4 | 𝔉 = 0 | [D] for PT-symmetric, N_e even, with or without SOC (Si, Ge, diamond); no "Kramers-summed" qualifier needed (Θ-real pair basis) |
| IF-CW3-3 | WP3 (R-code), WP5 (C-code); COMP queue | GaAs/Si Γ/δ map, c^F | fork inputs code/CW3/fork/; [E] K_ν ≥ 0 for GaAs off the d11 shell |
| IF-CW3-4 | LIMITS L17, WP6 (θ support), WP0 §9.2 (iii), G6 | electron-only static step | (CW3.4): GS lattice term → Ω²_{P,e}/(c_Lq)² ≫ 1 for q ≲ q_BZ in every solid [D]; [E] ≳ 1 beyond pending Z^{(e)}(q); step (iii) not a usable bound for relaxed ch = e |
| IF-CW3-5 | CONVENTIONS §7, WP0 §2, WP1, WP4 | basis | 17th row 𝔳²_s; 𝒪₂ mapped |
| IF-CW3-6 | WP0 §6.2, OW0-17, WP4 OW4-4, WP7-B2 IF-B2-11, WP7-B1 G-E8 | magnetic/CDW sectors | Theorem D-m (i)–(iii); CDW GRPA formula; metadata `ref=CDW` proposed (CONVENTIONS §11) |
| IF-CW3-7 | WP4 OW4-1 | 𝔥_off | zeroth-moment formula + EPW `g2sum` spec; bin condition and §1.1 share one missing step (fibred LAP) |
| IF-CW3-8 | WP1 [E11], WP6, LIMITS L17 (9.5) | δ_rel | complete O(α²) list (mass-velocity + orbit–orbit only); (CW3.3) spec |
| IF-CW3-9 | LIMITS L-D1, L-D3, L-D4, L-D5, L-D8, L-D10, L-D11 | statuses | §4 (all CLAIMED here) |
| IF-CW3-10 | LIMITS (new), SOTA ratings | 2109.08168 Eq. (3) | REFUTED by (m_a+2m_e)/(m_a+m_e) (three routes) |
| IF-CW3-11 | WP0 (2.9), L9b | aγγ absorption | tensor form B̂₀·Im[−ε^{-1}]·B̂₀; skin-depth condition |

## Owed corrections (target → exact replacement text; none applied here)
1. **WP5-v4 §1.5, (W17) and the K_ν line** (S) → "K_b = (Γ^{(b)} + 𝔉_b)/Γ^{tot}, 𝔉_b ≡ Γ^{(b)}(c̄^F − c_b^F), c_b^F ≡ Γ^{tot}Im(Σ_{f∈b}Γ^{(f)}ρ*_Λ₀a^{off}_f/Γ^{(b)})/|ρ_Λ₀|², c̄^F = Σ_bΓ^{(b)}c_b^F/Γ^{tot}, b ∈ {ν, x}, a^{off}_x = 0 at O(g²); Σ_b𝔉_b = 0 (Σ_ν𝔉_ν = −Γ^xc̄^F)."
2. **WP5-v4 (W15)** (S) → "|ΔP(N|Λ₀)| ≤ (Γ^{ph}/Γ^{tot})max_ν|c_ν^F|·max_{b,b′}|P_b(N) − P_b′(N)| ≤ max_ν|c_ν^F|"; positivity line → "K_b ≥ 0 iff 1 + c̄^F − c_b^F ≥ 0, sufficient 2max|c^F| ≤ 1"; GaAs [E] "2π max|c^F| ≲ 0.3Γ/δ" → "max|c^F| ≲ 0.3Γ/δ".
3. **WP5-v4 §8 θ_𝔉 row; WP6 θ_𝔉 prior** (S) → bound "|ΔP| ≤ max|c^F|" (not 2π max|c^F|); value [E] ≲ 0.3Γ/δ unchanged.
4. **NOTATION row 𝔉_{Λ₀,ν}, c_ν^F** (N) → "𝔉_b = Γ^{(b)}(c̄^F − c_b^F) (rate units; O4 (O4.7) is the spectral-weight form 2π|ρ|²𝔉_b/Γ^{tot}); c_b^F = Γ^{tot}_Λ₀ Im(ρ*a^{off}_b)/|ρ_Λ₀|², dimensionless; b includes non-phonon branches; vanishes for PT-symmetric targets with N_e even (CW3 §2.2)".
5. **WP0-v3 §6.2 (iv″b)** (S) → "… includes the Fano term 𝔉_{Λ₀,b} (CW3 (CW3.1)); 𝔉 = 0 for PT-symmetric targets with an even electron number, with or without SOC (Si, Ge, diamond) [D] (Θ-real pair basis, CW3 §2.2); generically ≠ 0 in GaAs [C]".
6. **WP3-v3 §M4 (iv″b) sentence** (S) → "Fano term 𝔉_{Λ₀,b} = Γ^{(b)}(c̄^F − c_b^F) with c^F of CW3 (CW3.1); 𝔉 = 0 for PT-symmetric Si, Ge, diamond [D]".
7. **WP0-v3 §6.2 rigour paragraph** (W) → delete "and the crystal has a gapless acoustic branch"; add "the PST gap condition concerns the electronic spectrum only; acoustic softness is the IR issue of the X+ definition (O4 §8.4)". "For low-lying vibrational states … the order of the remainder is not derived [C]" → "holds with the same order on energy-cutoff states (math-ph/0201055, 'Energy cutoff') [D given PST]".
8. **WP0-v3 §6.2 Scope of (H2)** (S) → "Magnetic insulators with a charge gap Δ_ch ≫ ω_ph, J are covered by Theorem D-m (CW3 §1.3): GS-m = spin–lattice manifold, quasi-boson sectors; itinerant magnets and fractionalised references remain open".
9. **CONVENTIONS §7** (S) → replace "𝒪₂ is outside the 16-row basis (needs a v_s⊗v_s row; WP0-v3 G2)" by "𝒪₂ → v_χ²n_s − 2v_χ·j_s + 𝔳²_s with the 17th row 𝔳²_s, ⟨k′|𝔳²_s|k⟩ = (k+k′)²/4m_s² (CW3 (CW3.2); = −2× the scalar-NLO 𝒯 row in its source normalisation)".
10. **LIMITS L17 (and WP0-v3 §9.2 (iii) relaxed ch = e, G6)** (S) → "ch = e, lattice relaxed: 1 − ε_e^{-1}(q,0) = [1 − ε_cl^{-1}(q)] + 𝒢_GS(q), 𝒢_GS = (e²/q²Ω)Σ_ν|Σ_κq·Z^{(e)}_κ·e_κν e^{iq·τ_κ}/√M_κ|²/ω_ν(q_r)² (CW3 (CW3.4)), → Ω²_{P,e}/(c_Lq)² ≫ 1 for q ≲ q_BZ in every solid, Si included [D] (Si q* = 18 keV), [E] ≳ 1 for q > q_BZ pending Z^{(e)}(q); step (iii) is not a usable bound; use (iv) or (9.4) with (CW3.4). The two-fluid 2.30 is the optical-only toy."
11. **WP0-v3 (2.9) and L9b note** (W) → "Γ_abs = g²_aγγB₀² B̂₀·Im[−ε^{-1}(m_φ)]·B̂₀/m_φ (= 2305.05681 Eq. (6), CONFIRMED [FT]); valid for samples ≫ skin depth"; §12 O6 → "closed (CW3 §3.4)".
12. **LIMITS L-D1** (S) → status "DERIVED, envelope ✎; amplitude CONFIRMED with d_nε_SE* = per-level shift (half-splitting), 2101.01241 Supp. (S41), (S45) [FT]"; note "u = 2101.01241 (S23), absorptive overlap with the inhomogeneous line only [D]".
13. **WP7-D-v2 §1.5** (W) → "u … is the overlap of the inhomogeneous spin line with the absorptive Lorentzian (2101.01241 (S23)); the DM line is treated separately (Supp. §VII)"; amplitude sentence → "CONFIRMED with the per-level-shift convention".
14. **LIMITS L-D3** (W) → "fixed-amplitude penalty 2.7–10 (1905.13650 [FT]: 3.0 Bayesian objective prior, 2.7 frequentist, ≈ 8.4 gradient couplings with velocity and phase; framework-dependent)".
15. **LIMITS L-D4; WP7-D §1.7, IF-D12** (S) → "prefactor 32 and M_n = ρπr_n²L₀ derived (CW3 §4.5); Eq. (7)'s m_V² is m_Vω_n (equal on resonance); odd n only".
16. **LIMITS L-D5; WP7-D §1.8** (S) → "drive ∝ ω² [D] (body force −ρḧξ); 2δ_rel^a = −1.97×10⁻² (Cu), 1809.02863 Table II [FT]".
17. **LIMITS L-D8; WP7-D IF-D10** (S) → "R_{k′l′} normalisation CONFIRMED, inherited (1108.5383 Eq. (6) via 1206.2644 [FT]); Eq. (9): not current-conserving at bound kinematics (CONFIRMED); quantitative verdict = exact gap (S_{J_TJ_T} + Dirac, Xe DHF); priority: no prior continuity remark found (INSPIRE walk; 2201.11905, 2201.11497 [FT] use the factorised form)".
18. **LIMITS L-D10; WP7-D §3.4, IF-D12** (S) → status "DERIVED: 2109.08168 Eq. (2) is the exact tree-level Dirac result (CW3-C4a); (T.4) agrees through O(x²); x³: exact −15/4, (T.4) −35/8; 1/8 kinematic, 1/2 Dirac amplitude"; §3.4(iii) seagull → "H_sg = −(eg_aee/2m_e²)(∂_ta)σ·A"; "Eq. (3) open" → "Eq. (3) REFUTED by (m_a+2m_e)/(m_a+m_e) (CW3 (CW3.5))".
19. **LIMITS L-D11; WP7-D §4.1** (S) → "(S.2) DERIVED with ln Ī = (2/πω_p²)∫ωL(0,ω)ln ω dω; PDG RPP 2024 Eq. (34.5) [FT]".
20. **WP7-D §2.5 massive ν̃** (W) → "ω^F = ω^{(2.1)} + (Δ_χ/m_ν̃)k²/2m_χ, 𝔇^F = 𝔇^{NR}(m_χ/m_ν̃)(1 + O(v²)) [D]".
21. **SOTA ratings (WP7-D)** (W) → add "2109.08168 Eq. (3): REFUTED (CW3)"; "1306.6089 Eq. (1) amplitude: CONFIRMED (CW3)"; "2011.01940 Eq. (9): not current-conserving (CONFIRMED); paper-error verdict = exact gap".

## Proposed LIMITS rows (provisional; labels for the coordinator)
| # | τ / chain (URF) | Source formula | Status |
|---|---|---|---|
| L-D10′ | (T.3)–(T.4) vs exact Born QED, free e at rest, V at rest | 2109.08168 Eq. (2), App. (7)–(12) | DERIVED (CLAIMED): Eq. (2) exact at all x; (T.4) through O(x²); x³ split 1/8 kinematic + 1/2 Dirac |
| L-D13 | ALP dark Compton, exact Born QED (CW3.5); NR seagull H_sg | 2109.08168 Eq. (3)/(18) | ✎ REFUTED by (m_a+2m_e)/(m_a+m_e) (CLAIMED, three routes) |
| L-D11′ | (S.1) → (S.2) Bethe with ln Ī from L(0,ω); Born, v ≫ shell velocities | PDG RPP 2024 Eq. (34.5) | DERIVED; shell/Barkas/Bloch corrections named |
| L17′ | ch = e relaxed: (CW3.4), GS lattice term | 2110.01587 §VII warning [per WP0, FT] | DERIVED (CLAIMED); step ≤ 1 false for every solid at q ≲ q_BZ, [E] beyond |
| L-O2 | 𝒪₂ → n, j, 𝔳²_s (CW3.2) | 2009.13534 Table III (operator list) [FT via WP0] | DERIVED |
| L-Fano | DC first-emission kernel (CW3.1) incl. non-phonon branch | O4 (O4.7) | ✎ prefactor 1 in rate units; 𝔉 = 0 for PT, N_e even [D] |
| L9b′ | aγγ in B₀: tensor form B̂₀·Im[−ε^{-1}]·B̂₀ | 2305.05681 Eqs. (2)–(7) | CONFIRMED [FT] ✎ (tensor wording) |
