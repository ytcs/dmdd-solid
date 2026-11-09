# R16 / CW6: closure of the phonon/charge-transport loose ends and the WP8-R revision (LE-20, LE-118 … LE-126)

Closure agent CW6, brief briefs/R16/CW6.md, 2026-11-01. Ledger rows: state/LOOSE-ENDS.md §1 group G and LE-20 (§2 group CW6).
**Read:** returns/R13/WP8-R.md ("v1"), referees/R14/REF-WP8-R-A.md and -B.md (cited by LE-20), returns/R14/WP5-AUD.md, returns/R15/CMPMC-AUD.md, returns/R16/CW5.md
§1 and §2.5 (coordinator input: LE-22 rulings, (CW5-3), (CW5-4)), returns/R12/WP7-E-v3.md §1.6–§3.2, §6–§8, returns/R8/WP4-v3.md (RG7), returns/R13/WP8-U.md (U7,
IF-U10, LU3) and its code/WP8-U/build_table.py, LIMITS L33–L38, CONVENTIONS (§12, R13 amendments), NOTATION (WP7-E rows, §G), CONTROLS, code/ENV.md.
**Deliverables:** this file and **returns/R16/WP8-R-v2.md** (LE-20; standalone, with its own closing table), both checked by `code/CW6/checks.py`:
**44/44 PASS in ≈ 17 s** (numpy, scipy, sympy; deterministic), cited **CW6-Kn**. No heavy job, no CMPMC run, no QE run.
**CMPMC citations** are to `/home/user/cmpmc` main = paer-sota = **cd56e1b** (CMPMC-AUD fixes merged; CMPMC-AUD itself cites the reference tree 921db93, whose line
numbers differ). Module verdicts are those of CMPMC-AUD §4.
**Literature [FT]** (lit.py into literature/papers-CW6/, IDs and titles verified against the arXiv API, PDFs deleted at the end): 1109.1193, 1109.4343, 1401.1937, 1805.02495,
1901.07569, 2012.12430, 2303.02196, 2408.04732. Crossref metadata only: Tamura, PRB 27, 858–866 (1983), "Isotope scattering of dispersive phonons in Ge"
(DOI 10.1103/PhysRevB.27.858). Not accessed: Kaplan (1979), Little (1959), Swartz–Pohl (1989), Jacoboni–Reggiani (1983). Tags: CONVENTIONS §12 and R13 ([CALC], [DB]).
**Deliverable rule (STATEMENT, user 2026-11-01).** A compute row closes with a derivation of the quantity and a specification a reader can follow: what is computed,
which approximation (τ level / model level) it embodies, the method (book appendix: transport Monte Carlo, DFT/DFPT, kinetic equations), key convergence parameters,
pitfalls and cost. CMPMC runs are "optional later runs", gated on the CMPMC-AUD module verdicts and on the CMPMC-AUD §6 upgrades named per row.

## 0. Closure table
| Row | Item (short) | Kind | Status | Where |
|---|---|---|---|---|
| LE-20 | apply R14 findings on WP8-R | correction-owed | **CLOSED** (WP8-R-v2 written; 46-row closing table; verdict revised) | §1, WP8-R-v2 |
| LE-118 | G-R1 ζ_O, σ_pos, r_coll for a concrete geometry | compute-formulate | **CLOSED** (functionals [D]; mean-field estimate [E]; CMPMC spec); geometry numbers = exact gap | §2 |
| LE-119 | G-R2 zero-field gap-energy release law; θ_gap | compute-formulate | **CLOSED-AS-EXACT-GAP** (law from (CW5-4); site/spectrum functional [D]; spec) | §3 |
| LE-120 | G-R3 created-phonon spectra propagated to sensors | compute-formulate | **CLOSED** (transfer-kernel bound [D]; spec seeded by WP5-AUD B-1) | §4 |
| LE-121 | δ_coll, r_coll; degeneracy | compute-formulate | **CLOSED** (decomposition exact; degeneracy broken by a bias scan [D]; spec) | §5 |
| LE-122 | G-E6 athermal emission, space-charge nonlinearity | compute-formulate | **CLOSED-AS-EXACT-GAP** (field law and locality bound [D]; spec) | §6 |
| LE-123 | RG7 t_esc in the QP cascade | compute-formulate | **CLOSED** (AMM/DMM t_esc [D, CALC-free]; film-escape law [D]; spec) | §7 |
| LE-124 | A_iso (Si) [E]; Tamura citation | literature-check | **CLOSED** ([FT] value 1.50–1.64×10⁻⁴⁵ s³; preset matched; WP8-U attribution corrected) | §8 |
| LE-125 | WP6 nuisances θ_ζ, θ_pos, F_NR | notation-bookkeeping | **CLOSED** (row text supplied) | §9 |
| LE-126 | SOTA statement on charge-mediated information | notation-bookkeeping | **CLOSED** (text supplied, cross-checked with LE-118) | §10 |
Counts: CLOSED 8, CLOSED-AS-EXACT-GAP 2, CANNOT-CLOSE 0. **Changes to refereed or audited text** (Owed corrections): WP8-R is superseded by v2; LIMITS L36
(B-b) support flag; WP7-E-v3 IF-E7/G-E4 text; WP8-U U7/IF-U10/LU3 attribution; WP6 §5.2 rows; SOTA IF-R6 sentence.

---
## 1. LE-20: R14 findings on WP8-R applied
**Item.** v1 stayed PROVISIONAL until the R14 referees and WP5-AUD. Both referee reports (A, B), the WP5-AUD rulings R-a…R-i/D-7…D-10, CW5's LE-22 resolution
(OC-7 on the HV verdict, OC-8 on the r_coll prior, (CW5-3)/(CW5-4) for the gap channel) and CMPMC-AUD IF-AUD-2…4 are applied in **returns/R16/WP8-R-v2.md**.
**Result.** Verdict: NO-GO for mode/frequency/angle selection of prompt populations in bulk Si/Ge; (c) HV becomes a CONDITIONAL NO-GO (firm at E_R ≲ 220 eV); (b)
the zero-field gap channel is UNRESOLVED (was NO-GO by ζ_O = 0); (d) stays CONDITIONAL, reclassified as the yield discriminant read out with phonons. Three referee
disagreements are ruled by evidence: device thickness 4 mm (2012.12430 p.4: "1 cm × 1 cm × 0.4 cm Si chip"; B right, A wrong); E_2σ 382 (A) vs 368 (B) are both
reproduced and come from different yield inputs (Lindhard(E) vs frozen 𝔶), v2 uses the measured Y (357 eV); Δ_Al is stated in all three readings (0.18 meV v1,
2Δ = 200 µeV 1109.4343 p.3, Δ = 173.715 µeV CMPMC presets.hpp:298), none of which changes a conclusion. New in v2 beyond the referees: the full isotropic P–SV AMM
with a reciprocity theorem (replaces the unread Kaplan source of L40), the gap-population term ζ_gapΔφ_gap with its ζ_O,min range, and the exact δ_coll^{gap}.
**Status: CLOSED.** v2 is CLAIMED; its yield sites carry WP5-AUD's status (REFEREED once CW5 OC-1…OC-8 apply). A further R×2 on v2 is the coordinator's choice.

---
## 2. LE-118 (G-R1): ζ_O, σ_pos and r_coll for a concrete geometry
**Item.** IF-R4: route (d) needs ζ_O ≥ 0.28 at σ_pos = 0.05 (v1; **0.24** in v2 with measured inputs), Si, 100 eV. ζ_O, σ_pos and r_coll have never been computed.
**The quantities [D].** Let u_pop(f, r, t) be the spectral energy density of population pop (primary, NTL, gap) born at event position r_ev, and let sensor
s ∈ {1, 2} absorb at its faces with a frequency-dependent probability per arrival P_s(f) = t̄_s(f)·𝟙[f ≥ 2Δ_s/h]·η_pb,s(f)/η_pb,s^∞ (transmission into the film, sub-gap
reflection, pair breaking). The energy delivered to sensor s is the flux integral E_s,pop(r_ev) = ∫dt∫df∮_{A_s}dA J_pop(f, r, t)·n̂ P_s(f), with J the energy current.
Then a_pop(r_ev) ≡ E_1,pop/(E_1,pop + E_2,pop) (two-film observable) or E_pop(t < t_f)/E_pop (fast/slow), and
  ζ_O ≡ ⟨a_NTL − a_prim⟩_r,   ζ_gap ≡ ⟨a_gap − a_prim⟩_r,   σ²_pos ≡ Var_r[a_prim(r) − â(r̂)],   r_coll ≡ ϵ_NTL/ϵ_prim^{ER},   ϵ_pop ≡ Σ_sE_s,pop/E_pop,        (CW6-1)
where â(r̂) is the position correction built from the estimated position r̂ (partition or delay), so σ_pos is the residual after correction. All four are linear
functionals of the birth spectra: given the transport Green's function 𝔊(f′, r′, t | f, r_ev) (a linear operator, since phonon–phonon interactions among
signal phonons are negligible at these densities), E_s,pop = ∫df 𝒦_s(f; r_ev) u_pop,0(f) with a **collection kernel** 𝒦_s. This is the book's statement: a
geometry is fully characterised for every population by two kernels 𝒦_1, 𝒦_2 on (f, r_ev).
**Mean-field limit [D given (i) diffusion time across the crystal ≪ absorption time, (ii) isotropic grey surfaces].** Then 𝒦 is position-independent and
∂_t u = 𝓜u − Γ_abs(f)u, Γ_abs(f) = (v̄/2d)[c₁t₁P₁(f) + c₂t₂P₂(f) + (1 − c₁ − c₂)ℓ_s], with 𝓜 the down-conversion generator of v1 §2, c_s the coverages, ℓ_s the bare-surface
loss per bounce (1109.1193 p.14: "∼0.1% for each phonon-surface interaction" [FT]); v̄/2d is the wall-hit rate of an isotropic gas in a slab (⟨v_z⟩ flux). The
time-integrated spectrum is n = (Γ_abs − 𝓜)⁻¹u₀ and E_s = Γ_s·n, an exact linear solve. **Estimate [E] (CW6-K7):** Si, d = 4 mm, c₁ = c₂ = 5%, t = 0.9, film 1
Nb-like (2Δ = 3 meV, cut 0.73 THz), film 2 Al (2Δ = 0.36 meV), ℓ_s = 10⁻³. Primaries (Debye birth): film 1/film 2/loss = 0.415/0.574/0.012. NTL births (flat to
2⟨E_Luke⟩, ⟨E_Luke⟩ = 0.75/2/4.7 meV, the paer-sota range of IF-AUD-5 [CALC pending]) give ζ_O = 0.42/0.28/0.11 and r_coll = 0.87/0.96/0.98. σ_pos = 0 in this limit by
construction; it is a purely geometric quantity.
**Strongest derived statements.** (i) ζ_O, ζ_gap and r_coll are fixed by 𝒦_s and the three birth spectra; NR and ER enter only through φ_pop (v2 §4.4), never through
𝒦_s. (ii) In the mean-field limit r_coll − 1 = Σ_s Γ_s·[(Γ_abs − 𝓜)⁻¹(u_NTL,0 − u_prim,0)] / ϵ_prim: its sign is the sign of the excess sub-gap and loss share of
the softer population, which is **negative** for NTL births below 2Δ_Al or exposed to surface loss (K7c). (iii) σ_pos needs the spatial kernel; the mean-field
value 0 is a lower bound.
**Missing step (single):** compute 𝒦_s(f; r_ev) for a stated geometry. **Specification (book appendix: transport Monte Carlo).**
*What:* 𝒦_1, 𝒦_2 on f ∈ [0.1, 15] THz (log grid, 40 points) × r_ev (8³ points in an octant, symmetry-reduced) for the 1×1×0.4 cm Si device of 2012.12430 with two TES
arrays (geometry and coverage from 2012.12430 App. A), and for a 1-cm CDMS-like Ge cylinder; then ζ_O, ζ_gap, σ_pos, r_coll by (CW6-1). *Approximation:* ballistic +
anisotropic phonon kinematics, isotropic-continuum isotope rate and L-only f⁵ decay (ICA, T = 0; LIMITS L39), film as lumped Kaplan absorber; no dispersion above ~1 THz.
*Method:* CMPMC main @ cd56e1b, `transport` (engine.hpp:424) with: CrystalLattice kinematics `KinematicsMode::Octahedral` (lattice.hpp:71; USE WITH PATCH P3; Exact
for caustic maps); bulk isotope + L decay with P1, P2 (USE WITH PATCH); surface three-way split (P8, USE WITH PATCH) with **campaign-supplied** p_spec, p_diff, p_anh
(`spec_prob_const`, geometry.hpp:62; IF-AUD-4: the G4CMP polynomials are demo values); KaplanFilm with subgap_absorption = 0 (USE; kaplan.hpp:51–70, film config
crystal_config.hpp:235–239) and film 1 gap set to Nb (presets.hpp:330, Δ = 1.50 meV); NTL phonons from `transport_charges` (engine.hpp:153; USE WITH PATCH P5, P6) at
V_b = 2/4/10 V. Presets: Si presets.hpp:22–68 (B_iso :36, A_anh :37, ν_D :42), Al :275–304. Seed each population as a monochromatic source per f-bin (that is what
makes 𝒦 a kernel), 10⁴ phonons per (f, r) cell. **Prerequisites before the run is meaningful:** CMPMC-AUD §6 item 2 (AMM/DMM interface t(θ, mode), so that t̄_s is not a
constant; until then supply the isotropic table of WP8-R-v2 §3.2) and item 1 (η_pb(ω, d_film) table; else η_pb^∞). **Do not use** jump-to-ballistic, NEE, the SoA/GPU
engines or fast-chord Luke. *Convergence:* f grid refinement (ζ_O changes < 0.01), 10⁴ → 4×10⁴ phonons per cell (statistical error < 1%), surface coefficients varied
over [AMM, DMM] (that spread is part of θ_ζ), Ge 𝒜_anh over its ×10 range. *Pitfalls:* (1) the toy's mean-field σ_pos = 0 is not a prediction; (2) the result depends on
p_spec, which no G4CMP default fixes; (3) NTL birth spectra are field-dependent and need P5 (the legacy 921db93 spectra are 5–45% too hard); (4) phonons trapped below
2Δ_Al are lost energy, not "absorbed". *Cost:* 40 × 512 cells × 10⁴ phonons × ~10⁴ steps ≈ 2×10¹² steps ≈ 35 h at 16 M steps/s on 4 threads (CMPMC-AUD T11): above the
3-h box limit, so FORMULATED; a 1-D (depth-only) reduction with 64 depth points runs in ≈ 1 h and is the recommended first pass.
**Verdict update for IF-R4 (CONDITIONAL kept).** The mean-field estimate shows ζ_O ≈ 0.1–0.4 is geometrically plausible at low field, so (d)'s requirement (0.24 at
σ_pos = 0.05) is not excluded; it is not established either. **Status: CLOSED** (quantities derived, estimate, spec); geometry numbers = exact gap.

---
## 3. LE-119 (G-R2): the release-time law of the gap energy at zero field, mK
**Item.** The (b) channel (Δf_g = 0.28, Si) and any timing discriminant need the time, place and spectrum of the gap-energy release; θ_gap if timing is used.
**Law [D, from CW5 §2.5].** With r_g(t) ≡ [E_pairs + E_X](t)/(N_ehE_g) and linear kinetics (H-g1)–(H-g3) of CW5, r_g(t) = 𝟙ᵀe^{Mt}p(0) = Σ_kw_ke^{−γ_kt} (CW5-4); a
bimolecular (dense-track) branch gives r_g = 1/(1 + t/t₀). The NR/ER heat ratio at window t_win is (CW5-3).
**Added here: the site–spectrum functional [D].** The phonon-borne part of the released gap energy splits by release channel ℓ ∈ {bulk exciton Auger/multiphonon,
surface recombination, electrode collection (E_c − μ_F, μ_F − E_v) and QP injection}: its spectral birth density is u_gap,0(f, r, t) = N_ehE_g Σ_ℓ π_ℓ(r, t) s_ℓ(f),
with π_ℓ the channel flux from (CW5-4) (outgoing fluxes of M, resolved by where the carrier or exciton is when it decays: bulk, or a face reached by diffusion) and s_ℓ the
emitted spectrum per channel. Then ζ_gap of (CW6-1) is Σ_ℓ π̄_ℓ(a_ℓ − a_prim), with π̄_ℓ the time-integrated channel fraction and a_ℓ the channel fraction of (CW6-1) for birth spectrum s_ℓ at the release site, evaluated with the kernels 𝒦_s of LE-118. **Three derived
consequences.** (i) Bulk hard release (s_ℓ above f_*(t_mem)) gives a_ℓ = a_prim, so ζ_gap = 0 only for that channel (the v1 statement, now one case). (ii) Surface and
electrode channels have π_ℓ set by the diffusion of excitons/carriers to faces: for diffusion constant D_X and lifetime 1/γ_X, the fraction reaching a face from depth z is
e^{−z/L_X}, L_X = (D_X/γ_X)^{1/2} (one-sided, absorbing face, 1-D) [D]; so the surface share is ≈ 2L_X/d for L_X ≪ d. (iii) In NTL mode all pairs are collected, so the
gap energy is released at the electrodes at the drift time, ≈ 1 µs (CW5 §1.2 estimate [E]), and the timing channel merges with (d) through ζ_gapΔφ_gap (v2 §4.4).
**Missing step (single):** the rates of (CW5-4) at 10–50 mK (k_FX, k_FT, k_XB,j, k_B↓, η_X, C_X; owned by CW5/LE-141) **and** D_X, the surface recombination
velocity S_surf and the per-channel spectra s_ℓ (owned here). **Specification.** *Kinetics part:* CW5 §2.5 spec (EPW cascade capture, BSE/DFT for bound excitons;
book appendix: kinetic equations, BSE). *Transport part (this row):* *What:* π_ℓ(r, t) and s_ℓ(f) for Si and Ge, then ζ_gap and its timing distribution.
*Approximation:* drift–diffusion of excitons (neutral, so field-free) with first-order surface loss S_surf; s_ℓ: for surface/electrode recombination a phonon cascade
starting at the recombination energy (multiphonon emission into the local modes, treated as a hard line at ω_op relaxing by §2, the conservative choice) or, for
QP injection, the Kaplan film cascade. *Method:* CMPMC does not model excitons (CMPMC-AUD §1.4: NOT USED; §6 item 3 "gap-energy / recombination phonon spectra" and item 5
"trap kinetics" are prerequisites). Until item 3 lands, run the exciton diffusion as a separate 1-D finite-difference solve (dz ≤ L_X/20, implicit time step, absorbing faces
with velocity S_surf), feed π_ℓ(z, t) as time-tagged sources into CMPMC `transport` with s_ℓ as birth spectra, and read ζ_gap with the LE-118 kernels. *Convergence:* grid
and time step (r_g to 10⁻³), S_surf ∈ [10, 10⁴] cm/s scan. *Pitfalls:* (1) at mK, D_X and k_XB depend on the impurity census of the actual crystal; (2) droplet formation
(Ge, Si at high density) is outside (CW5-4); (3) luminescence (η_X) leaves the detector and is in E_esc, not in ζ_gap. *Cost:* the diffusion solve is seconds; the transport
part is LE-118's kernel cost (no new run once 𝒦_s exists).
**Nuisance θ_gap.** If (b) or a timing observable is used: θ_X becomes type T on r_g^{NR}, r_g^{ER} separately (CW5 IF-CW5-2), plus **θ_ζg** (M on ζ_gap, prior uniform
[−0.5, 0.5] [E], i.e. sign open) and θ_Ssurf (M, σ_ln 2.3 [E]). Row text in §9. **Status: CLOSED-AS-EXACT-GAP.**

---
## 4. LE-120 (G-R3): created-phonon spectra propagated to the sensors
**Item.** f_s and the NR optical share are [E] until the created spectra (WP5-AUD B-1, LE-5; corrected by CW5 OC-3) are propagated.
**Transfer-kernel bound [D].** With the collection kernel 𝒦_s(f; r) of LE-118, ΔO_obs = Σ_s∫df w_s(f; r)[ũ_NR,0(f) − ũ_ER,0(f)] for normalised spectra ũ, where w_s is a
bounded weight |w_s| ≤ 1. Split the spectra at f_m ≡ f_*(t_mem): above f_m the cascade forgets the birth spectrum, so 𝒦_s(f; r) → 𝒦_s^∞(r) for f > f_m up to the
hard-part TV distance τ_h(t_mem) of v1 §2.3. Then
  |ΔO_obs| ≤ ‖ũ_NR,0 − ũ_ER,0‖_{TV, f < f_m} + τ_h(t_mem)·‖ũ_NR,0 − ũ_ER,0‖_{TV, f > f_m} ≤ Δ_soft + τ_h,                                                  (CW6-2)
with Δ_soft the NR/ER difference of the energy fraction born below f_m. With the v1 inputs Δ_soft ≈ (1 − 𝔶)f_s and τ_h ≤ 10⁻³, which is the v1 result; with the computed
spectra the bound is evaluated directly. (CW6-2) is the precise statement behind "only the soft fraction survives": it needs only linearity and the scaling result, and it
names the single number (Δ_soft) the WP5 tables must supply. **NR optical share.** The branch content of the NR birth is irrelevant for f > f_m by (CW6-2); it matters
only through the energy it puts below f_m (for x_R ≲ 1 given exactly by WP2 (3.6)).
**Specification (book appendix: transport Monte Carlo seeded by MD/e–ph tables).** *What:* ΔO_obs(t) and the arrival spectra for ER (5 seeds per energy) and NR
(MD partition tables) at E_R ∈ {50, 100, 300, 1000} eV. *Approximation:* as LE-118; birth spectra at the B-1 level (branch-resolved, 0.5 meV grid; NR end-state zero point
ω_s/2 subtracted, ΔZPE excluded, OC-3). *Method:* convolve the B-1 spectra with 𝒦_s (no new MC once LE-118's kernel exists); for a direct check, replace the mono-energetic
Debye spawn of partition.hpp:137–160 by sampling from the B-1 table (CMPMC-AUD §6 item 7; M effort) and run `transport`. *Convergence:* B-1 grid (0.5 → 0.25 meV), f_m
moved by ×2 (the bound must not change by more than τ_h). *Pitfalls:* (1) absorbed thermal phonons carry negative weight in B-1; the kernel is linear, so pass them as negative
sources, never clip (same rule as CW5 OC-9); (2) the boundary-thermostat share of the MD energy must be added with its own spectrum (B-1); (3) the toy f_s used a flat soft band;
the true residual-kinetic spectrum is part (ii) of B-1. *Cost:* convolution negligible; the direct CMPMC check ≈ 10⁸ steps per seed set (minutes). **Status: CLOSED.**

---
## 5. LE-121 (G-E4, IF-E7, IF-R3): δ_coll, r_coll and the degeneracy
**Item.** η^φ_NR = 0.952 (1803.02903) and f_DF = 6.08% (1805.09942) constrain δ_coll + r_coll-term + stored energy jointly (L38 degeneracy).
**Decomposition [D].** At first order in the population differences, δ_coll = δ_coll^{prim} + δ_coll^{gap} + δ_coll^{pos} + δ_coll^{esc}. The gap part is exact at fixed
populations: with ϵ_prim^{pop} = ϵ_hard(1 − 𝒢_gap x) + ϵ_gap𝒢_gap x, x = 1 (ER), y_ion (NR),
  δ_coll^{gap} = (1 − y_ion)𝒢_gap(ρ_g − 1)/[1 + 𝒢_gap(ρ_g − 1)],   ρ_g ≡ ϵ_gap/ϵ_hard   (CW6-K8a).                                                         (CW6-3)
ρ_g − 1 = 0.24 alone gives 0.048 for Si (K8b). δ_coll^{prim} ≤ 0.007–0.012 (v2 §6). δ_coll^{pos} = Cov_r(position distributions NR vs ER, 𝒦) vanishes for bulk calibration sources
with identical depth profiles; ²⁵²Cf neutrons and γ sources differ in depth profile, so it is not zero in 1803.02903 [E]. δ_coll^{esc}: surface ΔE_esc (WP7-E-v3).
**Degeneracy broken [D].** From (AUD-1), at r_coll = 1: ∂(1 − η)/∂r_coll = g_Luke(1 − y_ion)/(1 + g_Luke), ∂(1 − η)/∂X = 1 with X ≡ δ_coll + (D′_NR − κ_cal D′_ER)/ω. The
Jacobian at two biases has rank 2 (K8c, d). **Measurement proposal:** η^φ_NR at V_b = 4 V and 40 V (g_Luke = 1.05, 10.5) on one detector and source gives
r_coll − 1 = [Δ(1 − η)]/[Δ(g(1 − y)/(1 + g))] and X from either point. Within the bias range where r_coll itself is field-independent (NTL spectrum changes with field, IF-AUD-5),
the residual degeneracy is of order dr_coll/dV_b·ΔV_b, which the LE-118 run computes. Separating δ_coll from E_st needs one more handle: the two-window Y_H (CW5 §2.5) or
an ER/NR source pair with matched depth profiles (δ_coll^{pos} = 0).
**Specification.** *What:* ϵ_prim^{NR}, ϵ_prim^{ER}, ϵ_NTL, ϵ_gap for the 1803.02903 Si ZIP (7.6 cm × 1 cm, 4 V/cm, QET coverage from the CDMS II design) and the 1805.09942 Ge iZIP
(±2 V, ²⁰⁶Pb surface source), then δ_coll by (CW6-3) + spectral part and r_coll. *Approximation:* LE-118 + charge drift (HV valleys, Luke emission, Linear/Quadratic IV inside
their fitted ranges, constant-λ trapping). *Method:* CMPMC `transport_charges` (P5, P6; USE WITH PATCH) for NTL and electrode-collection phonons (collection energy
E_kin + E_g/2 at engine.hpp collection hit: PASS WITH CAVEAT μ_F mid-gap — supply μ_F per contact), `transport` for phonons, KaplanFilm for the QETs; position
distributions from the neutron/γ source Geant4 maps (external). **Prerequisites:** CMPMC-AUD §6 item 3 (gap-energy phonon spectra at electrodes: CMPMC records E_g/2 as a hit
with no phonons, which sets ρ_g by construction and must not be used for δ_coll^{gap}) and item 2. *Convergence:* 10⁵ events per population; ρ_g to ±0.02.
*Pitfalls:* (1) the IV Matrix model is DO NOT USE; (2) fast-chord Luke sets one NTL energy and would fix r_coll artificially; (3) the iZIP surface source puts δ_coll^{esc}
first. *Cost:* ≈ 10¹¹ steps ≈ 2 h (4 threads) per geometry once items 2–3 exist. **Status: CLOSED** (derivation, degeneracy statement, spec).

---
## 6. LE-122 (G-E6): athermal emission and the space-charge nonlinearity
**Item.** WP7-E-v3 (E9) at mK has frozen thermal emission; what remains is athermal emission and the field distortion by trapped charge (L33, L34 leading corrections).
**Space charge [D].** Planar detector of thickness d at fixed bias V_b. A trapped areal charge en_s at depth z₀ changes the field by ΔE = −en_s(d − z₀)/(dε_rε₀) below and
+en_sz₀/(dε_rε₀) above the sheet: a jump en_s/(ε_rε₀) with zero mean (fixed V_b) (K10b). For a volume density ρ_tr(z) the field correction is ΔE(z) = (1/ε_rε₀)[∫_0^zρ_tr −
(1/d)∫_0^d(d − z′)ρ_tr dz′]. The **nonlinearity parameter** ξ_SC ≡ max_z|ΔE|/ℰ_b; 1% of 1 V/cm in Si needs n_s = 6.5×10⁴ e/cm² (K10a). Accumulation: with event rate R per
area, pairs per event N_eh, trapped fraction p_tr (2303.02196 p.4: 12.7% in the HVeV device [FT]) and neutralisation (IR flashing) every t_flash,
n_s(t) ≈ RN_ehp_tr t up to t_flash. For a 1-cm² Si face at R = 1 Hz of 100-eV events (27 pairs), ξ_SC = 1% at 1 V/cm after t ≈ 6.5×10⁴/3.4 ≈ 5 h [E]; dense
calibration runs reach it in minutes. The effect on (E10) is a field-dependent ⟨𝔮|z⟩ through the drift velocity; with constant-λ trapping it changes ⟨𝔮⟩ only through the
v-dependence of σ_cap(u_car).
**Athermal emission: a locality bound [D].** Phonon-driven ionisation of a shallow centre needs hf ≥ E_b (45 meV for P in Si [UNVERIFIED], 10.9 THz). By §2 of WP8-R-v2, phonons above
that frequency survive t ≈ (x_L𝒜_anh f⁵)⁻¹ ≈ 0.95 ns and travel r_rms ≈ 1.2 µm (K10c). **Phonon-driven emission from neutral shallow donors is therefore confined to
≲ µm of the next event's track**, and its rate per trap is ≈ R·(track volume within ~µm)/V; NTL phonons (≤ ~6 meV) cannot ionise D⁰/A⁰ but can ionise the shallow
D⁻/A⁺ states (E_b ≈ 1–2 meV [UNVERIFIED]), which is the dominant athermal route for over-charged centres. Impact ionisation of neutral centres by drifting carriers needs
E_kin ≥ E_b; in Luke-limited drift ⟨E_Luke⟩ ≲ 6 meV (IF-AUD-5), so it proceeds from the hot tail only (2303.02196 measures 0.6% per carrier [FT]).
**Exact remaining gap.** Γ^{em}_j = ∫df Φ_ph(f)σ_ph-ion,j(f) + n_car u_car σ_ii,j(u) + (IR), with the cross-sections σ_ph-ion,j (phonon ionisation of D⁻/A⁺ and of D⁰ near
threshold) and σ_ii,j(u) unknown at mK. **Specification.** *What:* Γ^{em}_j(history) and ξ_SC(t) for Si and Ge detectors under a stated exposure. *Approximation:*
σ_ph-ion from the effective-mass hydrogenic model with deformation-potential coupling (Fermi golden rule, acoustic phonon of the Kaplan/Leman Ξ; τ: one-phonon
absorption); σ_ii from the Born impact cross-section on the same wavefunctions; trapped-charge field from 1-D Poisson (above) or the FEM fields of CMPMC (mesh_field.hpp:
NOT USED, not audited). *Method:* (1) closed-form effective-mass cross-sections (no DFT needed for the hydrogenic part; central-cell corrections from DFT supercells in the
rtsc layout if wanted: pw.x 216-atom Si:P, ecut 60 Ry, Γ-only, ≈ 10³ CPU-h; inputs with `@PSEUDO@`, SG15 ONCV v1.2 via `rtsc/pseudo.sh`, stages as `rtsc/bench/run-fork.sh`); (2) CMPMC trapping/impact ionisation (charge_physics.hpp:104–127; USE with caveat) extended
by CMPMC-AUD §6 item 5 (E9 kinetics with history n_j(t), speed-dependent σ and space charge) — **prerequisite**; (3) a run-sequence driver that carries n_j(t) across events.
*Convergence:* Poisson grid dz ≤ d/200; event-sequence length until ξ_SC saturates. *Pitfalls:* (1) constant mean-free-path trapping cannot produce history dependence;
(2) Ramo is exact with space charge (WP7-E-v3 C2c), but the dissipated heat differs by −ΔE_es; (3) flashing resets n_j but creates D⁻/A⁺ populations. *Cost:* minutes for
(1) and (3); (2) is item 5 (≈ 1 week implementation). **Status: CLOSED-AS-EXACT-GAP.**

---
## 7. LE-123 (RG7): phonon interface transmission t_esc in the QP cascade
**Item.** WP4-v3 [4.x] QP cascade treats phonon escape from the film into the substrate with a phenomenological t_esc; L40 rested on unread Kaplan (1979).
**Film-escape law [D].** A phonon in a film of thickness d (free top surface, substrate below) at angle θ travels 2d/cosθ between successive arrivals at the interface,
where it escapes with probability t_esc(θ); pair breaking acts with length λ_pb(ω). Summing the geometric series of round trips,
  P_abs(θ) = (1 − e^{−a})/(1 − (1 − t_esc)e^{−a}),   a = 2d/(λ_pb cosθ)   (CW6-K6a),                                                                       (CW6-4)
which reduces to CMPMC's 1 − e^{−4d/λ} (kaplan.hpp:51–58, path 4d; t_esc ≡ 1) after the flux average ⟨2d/cosθ⟩ = 4d (K6b), and to P_abs ≈ a/t_esc for a ≪ 1. Hence the
film phonon loss time is **τ_l = 4d/(v_film t̄_esc)**, the quantity τ_l of 1401.1937 that controls the thin-film fall of η_pb. CMPMC's film model is the t̄_esc = 1 limit;
the physical value enters exactly as `thickness_frac = 4/t̄_esc` at small a, and as (CW6-4) in general.
**t_esc from the interface [D numbers, CW6-K5].** The isotropic welded AMM (P–SV + SH, solved exactly, flux-conserving to 3×10⁻¹⁵) and DMM give, for Al → Si:
t̄_esc^{AMM} = 0.323 (P 0.603, SV 0.266, SH 0.315), t̄_esc^{DMM} = 0.257; with the CMPMC Al preset 0.328. **Reciprocity theorem [D]:** Σ_Al t̄_{Al→Si} = Σ_Si t̄_{Si→Al},
Σ = c_L⁻² + 2c_T⁻² (K5d), so the fitted effective Si → Al coefficient 0.3–0.55 (1805.02495 p.1 [FT]; 380 µm Si / 60 nm Al, specular MC fit) corresponds to **t̄_esc = 0.10–0.19**.
The three models differ by up to ×3 in τ_l (K6c). This is the RG7 closure: t_esc is no longer phenomenological; its model spread (AMM / DMM / fitted) is the nuisance.
**Specification (anisotropic and thin-film upgrade).** *What:* t_ν(θ, φ) for Al(111)/Si(001) and W/Si, both directions, and τ_l(ω) for d = 40–600 nm. *Approximation:*
anisotropic welded AMM (Christoffel-matched plane waves, 6×6 boundary problem) with film interference for λ ≳ d; clean interface. *Method:* elastic constants from DFPT/finite
strain in the rtsc layout (pw.x vc-relax → strain-stress, Al fcc ecut 60 Ry, 16³ k, smearing 0.02 Ry, ≈ 0.5 h in the box; `@PSEUDO@` inputs, SG15 ONCV v1.2 via `rtsc/pseudo.sh`, stages as `rtsc/bench/run-fork.sh`) or [FT]; boundary solve as CMPMC-AUD §6 item 2
(2 d isotropic, 1–2 wk anisotropic); then KaplanFilm with (CW6-4). *Convergence:* angular grid (t̄ to 10⁻³), reciprocity identity as a built-in test (as K5d).
*Pitfalls:* (1) oxide or aSi interlayers (Leman's "∼33%" tuned aSi–Al, 1109.1193 p.14) dominate real interfaces; (2) the measured 0.3–0.55 is model-conditional;
(3) the film's polycrystalline texture makes "Al(111)" an approximation. *Cost:* small (box-runnable). **Status: CLOSED.**

---
## 8. LE-124: A_iso (Si) and the Tamura citation
**Item.** WP8-U U7/IF-U10: "A_iso = 1.65×10⁻⁴⁵ s³ (1901.07569 pp.4–5)", [E]; Tamura PRB 27, 858 [UNVERIFIED] (LU3).
**Finding [FT].** 1901.07569 does **not** contain that number: its full text gives Table I (p.2) mean free paths and lifetimes and states, p.6, only that "for Ge, Ref. [54]
demonstrated that the phonon lifetime is limited by isotopic scattering", with the qualitative ordering. The 1.65×10⁻⁴⁵ is WP8-U's own closed form (code/WP8-U/build_table.py,
"Tamura coefficient … A_iso = V_a g₂^iso/(4π v_m³)" with JARVIS moduli). The [FT] source of the formula and value is **2408.04732 Eq. (4) and Table 4 (p.6)**:
"Γisotopic = Bν⁴ = (4π³Γ_mdΩ/⟨c³⟩)ν⁴", Si Γ_md = 2.02×10⁻⁴, ⟨c³⟩ = 2.13×10¹¹ m³/s³, B = 2.33 (calc), 2.42 (lit), 2.42–2.56 (measured, ref. [61] Tamura–Shields–Ramsbey–Wolfe)
×10⁻⁴² s³. **Value:** A_iso ≡ B/(2π)⁴ (ω-form) = **1.50 (calc), 1.55–1.64 (measured) ×10⁻⁴⁵ s³** (CW6-K9c). Re-derivation from IUPAC abundances [DB]: Γ_md = 2.007×10⁻⁴,
isotropic ⟨c³⟩ = 2.132×10¹¹, B = 2.338×10⁻⁴² (K9a, b). **CMPMC preset:** `c.B_iso = 2.43e-42` (include/cmpmc/materials/presets.hpp:36, cd56e1b) = Leman Table I = A_iso
1.559×10⁻⁴⁵, inside the measured band; CMPMC-AUD's anisotropic rebuild 2.442 (T3) agrees. WP8-U's 1.65 lies 0.4% above the measured upper edge and is acceptable as [E].
**Tamura citation:** bibliographic entry verified (Crossref: S.-i. Tamura, "Isotope scattering of dispersive phonons in Ge", PRB 27, 858–866, 15 Jan 1983); content not
accessed; the formula is carried by 2408.04732 (its refs. [38, 39] are Tamura). **Status: CLOSED.**

---
## 9. LE-125: WP6 nuisances for route (d) (and (b))
**Item.** IF-R5: rows θ_ζ (M), θ_pos (M), F_NR (A) once LE-118 fixes the ranges. Ranges now: ζ_O ∈ [0.1, 0.42] from the mean-field estimate (K7b), widened for the AMM/DMM
spread; σ_pos residual 1–10% (CDMS order-unity raw variation, corrected; v1 §4.2); F_NR measured (2303.02196). Row text (owed, §Owed corrections, OC-CW6-5):
| Level (τ slot) | Template Δ^τ_k | Type | Prior | Correlation | Source |
|---|---|---|---|---|---|
| θ_ζ | contrast ζ_O of the two-film / fast-slow observable | M | uniform [0, 0.5] [E] (central from 𝒦_s when computed) | geometry, V_b | WP8-R-v2 §4.4; CW6 LE-118 |
| θ_ζg | gap-population contrast ζ_gap | M | uniform [−0.5, 0.5] [E] (sign open) | geometry, release site | WP8-R-v2 §4.3; CW6 LE-119 |
| θ_pos | residual position spread σ_pos | M | log-uniform [0.01, 0.10] [E] | geometry, position estimator | WP8-R-v2 §4.2 |
| F_NR | NR pair-number Fano factor at E_R ≤ 0.5 keV | A (data band) | 2303.02196 Table II bands (1σ), shared with the WP5-AUD Fano row | material-wide | WP5-AUD §3.2; CW5 OC-7 |
**Status: CLOSED** (text supplied; WP6 not edited).

## 10. LE-126: SOTA statement (IF-R6)
**Cross-check with LE-118.** The statement must carry the bulk scope (near-face shell 0.5–3.9% of a 4-mm device), the Si/Ge restriction, the prompt-population restriction
and the open gap channel; LE-118 confirms that contrasts arise from collection geometry acting on charge-borne populations. **Text** (owed, OC-CW6-6): "Phonon NR/ER
information at the sensors is charge-mediated (NTL, carrier-relaxation and gap-energy phonons). In bulk Si/Ge, prompt phonon populations lose frequency and polarisation
memory within ≈ 10 ns (Si) / 30–100 ns (Ge) and ≲ 0.1 mm (WP8-R-v2 §2; [E], toy cascade with a derived f_*(t) scaling), except for events within that distance of an
instrumented face; this does not hold for Al₂O₃. The zero-field gap-energy channel ((1 − 𝔶)E_g/ε_eh ≈ 0.28 of E_R in Si) is UNRESOLVED pending its release law and site
(G-R2; CW5 (CW5-4)). Mode/frequency/angle-selective collection of primaries is NO-GO; HV phonon PSD at E_R ≤ 300 eV is a CONDITIONAL NO-GO (CW5 OC-7)." **Status: CLOSED.**

---
## Symbols introduced/used
| Symbol | Meaning | Where |
|---|---|---|
| 𝒦_s(f; r_ev) | collection kernel of sensor s (energy delivered per unit birth energy at f, r_ev) | (CW6-1), §2 |
| ζ_gap, θ_ζg, θ_Ssurf, S_surf, D_X, L_X | gap-population contrast and its nuisance; surface recombination velocity and its nuisance; exciton diffusion constant and length | §3, §9 |
| π_ℓ(r, t), s_ℓ(f) | gap-release flux per channel ℓ; its emitted spectrum | §3 |
| f_m ≡ f_*(t_mem), Δ_soft, τ_h | memory frequency; soft-born NR/ER difference; hard-part TV distance | (CW6-2) |
| δ_coll^{prim}, δ_coll^{gap}, δ_coll^{pos}, δ_coll^{esc}, ρ_g, ϵ_gap, ϵ_hard | parts of δ_coll; gap/hard collection ratio | (CW6-3) |
| ξ_SC, n_s, ρ_tr | space-charge nonlinearity; trapped areal and volume charge densities | §6 |
| σ_ph-ion,j, σ_ii,j | phonon-ionisation and impact-ionisation cross-sections of trap j | §6 |
| P_abs(θ), a, t̄_esc, τ_l, Σ ≡ c_L⁻² + 2c_T⁻², t̄_{12} | film absorption per entry; optical depth; flux+mode-averaged transmission; film loss time; reciprocity weight | (CW6-4), §7 |
| 𝒮_sep, 𝒮_int, 𝒮_b, O_obs, O_b, Δφ_gap | WP8-R-v2 renames/new (𝔖 → 𝒮_sep) | WP8-R-v2 |
| used | ζ_O, σ_pos, σ_Nph, f_s, f_*(t), 𝒜_anh ⚠, 𝒜_iso ⚠, A_iso (WP8-U), Γ_md (source, 2408.04732), r_g, P_g, 𝒢_gap (CW5), g_Luke, y_ion, 𝔶, r_coll, δ_coll, κ_cal(r_coll), ⟨𝔮⟩, η_pb, Δ_BCS, t_esc, d_film, ℓ^tr, σ_cap, Γ^{em}_j, n_j, E_b | NOTATION / v1 / WP5-AUD / CW5 |
Source-only: 2408.04732 B, Ω, ⟨c³⟩, Γ_md; 1901.07569 f_W, f_Al, τ_collection; CMPMC `B_iso`, `A_anh`, `thickness_frac`, `spec_prob_const`.

## Interface flags
| # | Owner | Item | Action |
|---|---|---|---|
| IF-CW6-1 | coordinator | WP8-R-v2 | supersedes returns/R13/WP8-R.md; SOTA/LIMITS pointers to v2; optional R×2 |
| IF-CW6-2 | WP7-E (IF-E7, G-E4), LIMITS L36 | (B-b) | WP8-R-v2 does not support r_coll ≥ 1 (toy 0.87–0.98); δ_coll^{gap} can carry 0.048; bias-scan proposal |
| IF-CW6-3 | CMPMC (follow-up agent) | prerequisites | §6 items 2, 3, 5, 7 of CMPMC-AUD are the gating upgrades for LE-118…122; add (CW6-4) to KaplanFilm (t̄_esc parameter); add a monochromatic-source kernel mode |
| IF-CW6-4 | CW5 / WP5 (LE-141) | rates | (CW5-4) rates plus D_X, S_surf, s_ℓ for LE-119 |
| IF-CW6-5 | WP8-U (CW7 / LE-19) | A_iso | U7/IF-U10/LU3 attribution corrected (OC-CW6-4) |
| IF-CW6-6 | WP6 | rows | §9 rows (θ_ζ, θ_ζg, θ_pos, F_NR band; θ_Ssurf) |
| IF-CW6-7 | NOTATION (CW8 / LE-164) | symbols | the "Symbols" rows above and WP8-R-v2's renames |
| IF-CW6-8 | WP4 | RG7 | t_esc replaced by t̄_esc^{AMM/DMM/fit} with (CW6-4); τ_l = 4d/(v t̄_esc) |

## Owed corrections (target → exact text; not applied here)
| # | Target | Type | Exact text |
|---|---|---|---|
| OC-CW6-1 | returns/R13/WP8-R.md (whole) | S | superseded by returns/R16/WP8-R-v2.md; header line: "SUPERSEDED (R16, CW6/LE-20) by WP8-R-v2" |
| OC-CW6-2 | LIMITS L36 Validity cell | S | append: "(B-b) r_coll ≥ 1 is not supported by WP8-R-v2 §6 (mean-field toy r_coll = 0.87–0.98 [E]); the bounds hold on the r_coll ≥ 1 branch only (CW5 OC-8)" |
| OC-CW6-3 | WP7-E-v3 §8 G-E4 and IF-E7 | W | G-E4 → "δ_coll = δ_coll^{prim} + δ_coll^{gap} + δ_coll^{pos} + δ_coll^{esc}; δ_coll^{prim} ≤ 0.012; δ_coll^{gap} = (1 − y_ion)𝒢_gap(ρ_g − 1)/[1 + 𝒢_gap(ρ_g − 1)] can carry 0.048 (ρ_g − 1 = 0.24); the r_coll/(δ_coll + E_st) degeneracy is broken by η^φ_NR at two biases (CW6 §5)" |
| OC-CW6-4 | WP8-U U7, IF-U10, LU3 | W | U7: "A_iso is ordered Ge > Si > C as 1901.07569 p.6 states qualitatively; the Si value 1.65×10⁻⁴⁵ s³ is this return's closed form [E], consistent with 2408.04732 Eq. (4)/Table 4 [FT]: 1.50 (calc), 1.55–1.64 (measured) ×10⁻⁴⁵ s³". LU3 source: "2408.04732 Eqs. (3)–(9) [FT]; Tamura PRB 27, 858 (1983) (bibliography verified, not accessed)"; status ESTIMATED → DERIVED (formula, [FT]) / E (value) |
| OC-CW6-5 | WP6-v3 §5.2 | S | append the four rows of §9 above, and θ_Ssurf "surface recombination velocity S_surf | M | σ_ln 2.3 [E] | crystal surface | CW6 LE-119" |
| OC-CW6-6 | state/SOTA.md, IF-R6 statement | W | the §10 text |
| OC-CW6-7 | WP4-v3 §6 RG7 and l.323, 329 | W | "t_esc is the flux- and mode-averaged film→substrate transmission t̄_esc: AMM 0.32, DMM 0.26, fitted-effective 0.10–0.19 (Al/Si; CW6 §7); it enters the film loss time τ_l = 4d/(v_film t̄_esc) and the per-entry absorption (CW6-4). RG7 closed as a nuisance θ_esc^{film} over the three models" |
| OC-CW6-8 | LIMITS L33, L34 leading-correction cells | W | add: "space-charge field ΔE(z) = (1/ε_rε₀)[∫_0^zρ_tr − (1/d)∫_0^d(d − z′)ρ_tr dz′] (CW6 §6); phonon-driven emission from neutral shallow centres confined to ≲ 1 µm of a track" |
| OC-CW6-9 | LOOSE-ENDS (coordinator) | N | LE-20, 118, 120, 121, 123, 124, 125, 126 CLOSED; 119, 122 CLOSED-AS-EXACT-GAP (pointers to this return) |

## Proposed LIMITS rows (numbering by the coordinator)
| # | Chain | Source | Validity | Leading correction | Status |
|---|---|---|---|---|---|
| CW6-L1 | transport Green's function → collection kernels 𝒦_s → ζ_O, ζ_gap, σ_pos, r_coll (CW6-1); mean-field linear solve | derived here; 1109.1193 p.14 (surface loss) [FT] | linear transport; mean-field: diffusion ≪ absorption time | position dependence (σ_pos); dispersion above 1 THz; AMM vs DMM surfaces | DERIVED (functionals) / E (toy) |
| CW6-L2 | transfer-kernel bound (CW6-2): \|ΔO_obs\| ≤ Δ_soft + τ_h | derived here | linearity; L39 scaling | non-ICA decay; surfaces before t_mem | DERIVED |
| CW6-L3 | film escape (CW6-4); τ_l = 4d/(v t̄_esc); reciprocity Σ₁t̄₁₂ = Σ₂t̄₂₁ | derived here; CMPMC kaplan.hpp:51–58 (t̄ = 1 limit) | specular film faces; lumped λ_pb | interference for λ ≳ d; anisotropy; interlayers | DERIVED |
| CW6-L4 | Tamura/Klemens isotope rate A_iso = Γ_mdΩ⟨c⁻³⟩/(4π) | 2408.04732 Eqs. (3)–(9), Table 4 [FT] | ICA, f ≪ f_D | dispersion (Tamura 1983/1985) | DERIVED (formula) / FT (value) |
| CW6-L5 | δ_coll^{gap} (CW6-3); bias-scan Jacobian | derived here; (AUD-1) | first order; fixed populations | δ_coll^{pos}, field dependence of r_coll | DERIVED |
| CW6-L6 | planar space-charge field; locality of phonon-driven emission | derived here | 1-D, fixed V_b; f⁵ decay law | 3-D trapped distributions; D⁻/A⁺ cross-sections | DERIVED (field) / E (locality numbers) |
