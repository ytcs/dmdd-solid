# R16 / CMPMC-DEV: CMPMC brought toward state of the art (SOTA list of R15 CMPMC-AUD §6, plus the DO-NOT-USE modules)

Agent CMPMC-DEV, brief briefs/R16/CMPMC-DEV.md. **Repo:** /home/user/cmpmc, branch `paer-sota`. It started from main @ cd56e1b and now has 10 commits, cd56e1b..3d43a02.
Nothing was pushed, and main is untouched (`main cd56e1b`). Builds are in /root/cmpmc-dev-build and /root/cmpmc-dev-final. All tests are single-core. The 4-thread benchmark went through run-heavy.sh.
**Literature [FT]**, read in literature/papers-CMPMC-DEV/ with the PDFs deleted: 1109.1193 (Leman: §IV.G, §V.D–E Eqs. (24)–(30), p.17), 1401.1937 (Guruswamy et al.: Eqs. (1)–(5), Fig. 4 digitised
from the PDF at 200 dpi, Fig. 5, §V) and 2302.05998 (G4CMP paper, Eqs. (17)–(18)). The search for a Jacoboni–Reggiani Z_f source failed. RMP 55, 645 is closed access (Unpaywall). The three arXiv
candidates fetched (cond-mat/0506045, 0806.4347, 2605.18581) contain no Si g/f Z_f table. Campaign inputs: WP5-v4 §5 (W13); WP7-E-v3 (E1), §1.3 ledger, Thm E-3, (E9)–(E12);
WP8-R §1.2, §3.1–§3.3 and code/WP8-R/checks.py; REF-WP8-R-A F2, F4, F5 and REF-WP8-R-B A3, B1; R15 CMPMC-AUD.
**Rules followed:** one physics change per commit, each with the formula source in the message and a CTest test registered in tests/CMakeLists.txt. The existing T1–T10 still pass.

---
## 0. Verdict at a glance
- **Done (validated):** SOTA items 1 (reduced scope), 2 (isotropic), 3, 4 and 11 (accuracy). The fast-chord DO-NOT-USE engine now runs a validated path. Every other DO-NOT-USE module has a runtime guard.
  The G4CMP demo surface coefficients are no longer defaults. A real energy-loss bug was found and fixed (Kaplan buffer).
- **Designed only** (DESIGN_NOTES.md in the repo): items 1 (full Chang–Scalapino), 2 (anisotropic), 5, 6, 7, 8, 9, 10, 11 (as default), 12, jump-to-ballistic and NEE.
- **New numbers for the campaign:** η_pb(Ω, τ_l/τ₀^φ) now reproduces 1401.1937 Fig. 4. The oblique, flux-averaged Ge→Al AMM gives t_L = 0.63 against t_T = 0.84. Electrode recombination
  phonons are soft: for 600 nm Al on Ge their mean is 1.0 Δ_Al, 93% are below 2Δ_Al, and they carry 49–51% of E_rel.
- **Final ctest: 16/16 pass** (§4).

---
## 1. Per item (R15 §6 numbering)
| # | Item | Status | Commit | Test | Validation numbers |
|---|---|---|---|---|---|
| 1 | η_pb(Ω, d_film) with film loss (REF-WP8-R-A F4, -B A3) | **done, reduced scope** (lumped film, Kaplan/Debye α²F, T = 0); full scope designed (DESIGN_NOTES §1) | e070377 | test_pair_breaking | 1/τ_pb(2Δ) = 1/τ₀ to 5e-13; I(Ω) vs brute quadrature 3e-11; η = 2Δ/Ω exactly below 4Δ for every τ_l, F_qp = 0. Against 1401.1937 Fig. 4 at hν = 5, 6, 7, 8, 10Δ: \|Δη\| ≤ 0.011 for τ_l/τ₀^φ = 0.5, 1, 2, 4; 0.035–0.041 low at 8 (tolerance 0.045; documented model difference). No-loss limit 0.590 (10Δ, 20Δ); F_qp(no loss) = 0.21; η increases monotonically with τ_l |
| 2 | AMM/DMM interface transmission | **done, isotropic**; anisotropic and thin-film interference designed (§2) | 328afc6 | test_interface_amm | R+T = 1 to 1.2e-14 at all angles (P and SV incidence, both sides; not imposed by the solver); normal limit = 4Z₁Z₂/(Z₁+Z₂)² to 1e-12; identical media T = 1; SH and P-SV reciprocity 1e-10; WP8-R §3.2 table, 24 entries, to ≤ 4.9e-4 abs (its 3 printed digits); DMM t₁₂ + t₂₁ = 1 |
| 3 | Gap-energy / recombination phonons at electrodes (REF-WP8-R-A F2, -B B1) | **done** (collection; traps → item 5) | c43569b | test_charge_release | E_rel(e⁻) + E_rel(h⁺) = E_g to 3e-6 for μ_F mid-gap and at E_v + 0.2 eV; per-mode closure hit + phonons + lost = E_rel to 8e-14. BulkDebye: phonons at hν_D (10 per Ge carrier). ElectrodeFilm (600 nm Al on Ge): 49.4–50.7% of E_rel absorbed as QPs, the rest re-injected at mean 1.00–1.02 Δ_Al (90–93% < 2Δ_Al), ≈ 200× softer than hν_D(Ge); seed 80Δ vs 160Δ changes this by ≤ 1.2% |
| 4 | Leman second-order Luke stepping | **done (opt-in)** | 2444f54 | test_leman_stepping | Against first order with Δk ≤ 0.01k (Ge, Si; e⁻, h⁺; 1/10/100 V/cm; 60 carriers): ⟨E_Luke⟩ within 0.1–2.4% (P5 default: 0.1–2.4%), phonons per carrier ≤ 3%, (E11) closure ≤ 1e-3. Steps per carrier 1.3–4.5× fewer than P5 and 4–23× fewer than the reference. Not Leman's 15–20×: that factor is relative to his τ/2 rule |
| 5 | Trap kinetics (E9)–(E12) | **designed** (§5) | — | — | effort ≈ 1 week |
| 6 | IV Matrix Z_f, intra-valley impurity | **designed; module guarded** (§6) | d8ca9a0 (guard) | test_guards | no [FT] source for Z_f (search recorded); values [UNVERIFIED], so not coded |
| 7 | Created-phonon spectrum | **designed** (§7) | — | — | needs WP2/WP5 tables |
| 8 | Dispersive phonons, T-mode decay | **designed** (§8) | — | — | L |
| 9 | Rothwarf–Taylor bulk QP | **designed; module guarded** (§9) | d8ca9a0 | test_guards | — |
| 10 | Non-parabolic HV | **skipped (designed, §10)** | — | — | αE ≤ 0.005 at E_kin ≲ 10 meV: ≤ 1% effect, below the 2–3% stepping tolerance; α unsourced |
| 11 | Closed-form Christoffel | **done (accuracy); goal "Exact as default" not reached** (§11) | 2a634c8 | test_christoffel_cardano | Si, Ge, GaAs, sapphire, α-quartz, CaWO₄ over 2e5 directions: v_p vs Jacobi ≤ 4.7e-13, v_g ≤ 1.7e-11 (gap > 1e-3; Jacobi fallback below 1e-4); [100]/[110]/[111] closed forms 2e-16. Speed-up only 1.3× (−O2) / 1.65× (−O3), because the tensor contractions dominate. Octahedral stays the default |
| 12 | SoA/GPU parity | **designed; guarded** (§12) | d8ca9a0 | test_guards | — |

## 2. DO-NOT-USE modules (brief: reproduce the reference to a stated tolerance, or keep a runtime guard)
| Module | Outcome | Commit | Test |
|---|---|---|---|
| IV Matrix (×4 vs J&R in Si) | guard: `transport_charges` throws for `IVRateModel::Matrix` unless `allow_unvalidated` | d8ca9a0 | test_guards |
| bulk 3D-QP (`transport_superconductor_coupled`) | guard | d8ca9a0 | test_guards |
| jump-to-ballistic | guard (in `transport` when enabled) | d8ca9a0 | test_guards |
| fast-chord HV Luke | **fixed:** now runs `transport_charges` with LemanSecondOrder; identical output for one seed; accuracy as item 4 | 06764a9 | test_leman_stepping (d), test_guards |
| NEE | guard (explicit argument) | d8ca9a0 | test_guards |
| SoA / GPU engines | guard (constructors) | d8ca9a0 | test_guards |
`core/validation.hpp`: `require_validated()` throws `UnvalidatedModuleError` naming the module and the defect. `phonon_benchmark` opts in, with a comment on each use.

## 3. Other commits (brief requirements and findings)
| Commit | Change | Source | Test, numbers |
|---|---|---|---|
| db6fc2f | **Demo surface constants removed from defaults.** Default surfaces are now fully diffuse with p_anh = 0. The G4CMP polynomials move to `g4cmp_demo_*` with `demo_values = true`, which the engine refuses without opt-in | 1109.1193 §IV.G [FT]: "Generally diffusive scattering has been found to be a good model" | test_surface (c): p_diff = 1, p_anh = 0 on all faces at 0.1–2 THz; demo set throws; (a), (b) still validate the R15 P8 port (opt-in) |
| f61d710 | **Bug:** the Kaplan cascade buffer (`SmallVec<double,64>`) silently dropped entries. A film phonon above ~130Δ (≈ 22 meV in Al; Ge prompt phonons are 35.7 meV) lost energy (7% at 160Δ). Now `KaplanBuffer` = 256 | energy conservation of (W13) bookkeeping | test_pair_breaking (f): closure ≤ 3e-15 per event at 50–350Δ |
| 3d43a02 | VALIDATION.md (module → test → reference → tolerance, status), DESIGN_NOTES.md, README "Validation status", PLAN marks guarded tiers | — | — |

## 4. Final ctest (fresh build /root/cmpmc-dev-final, serial)
`100% tests passed, 0 tests failed out of 16`, total test time 70.35 s (paer-sota @ 3d43a02, fresh Release build, serial; no compiler errors).
New targets: test_pair_breaking, test_interface_amm, test_guards, test_charge_release, test_leman_stepping, test_christoffel_cardano. R15's T1–T10 are unchanged and pass. test_surface also gained (c).
Benchmark (`phonon_benchmark 200`, 4 threads, run-heavy.sh, run mid-session): rc = 0. Every guarded module ran with opt-in. Phonon-run energy closure is 2.9e-15. The wavefront demo deposits 9.70 of
14.29 eV, the known SoA/GPU defect (§12). The binary was built after d8ca9a0. It was not re-run at the end because the heavy lock was busy with COMP-PH.

## 5. Defaults vs opt-in
To keep the R15-validated paths reproducible, these defaults are unchanged: the G4CMP film-loss law, first-order Δk stepping, `ChargeRelease::RecordOnly` (= legacy E_kin + E_g/2) and Octahedral kinematics.
**For campaign [CALC] runs, use:** `loss_model = KaplanRateCompetition` with `phonon_loss_time = KaplanFilm::loss_time_from_geometry(d, v_s, t_AMM)`; `amm_interface` (substrate/film media
from sourced moduli); `subgap_absorption = 0` (so that E_sig = Δ N_qp, WP5-v4 [A-7]); `LemanSecondOrder`; `ElectrodeFilm` or `BulkDebye` with an explicit μ_F; and sourced reflection coefficients.
**Still G4CMP example values:** `AluminumFilm()`: film_absorption 0.20, subgap_absorption 0.10, gap 173.715 µeV, slope 0.29. Its τ₀ = 242 ps is Kaplan's value as used by G4CMP; 1401.1937 uses 0.26 ns.

## 6. Remaining items (in priority order)
1. Item 1 full scope: a Chang–Scalapino kinetic-equation table (α²F, T > 0) that also closes the 0.04 gap at τ_l/τ₀^φ = 8 (3 d).
2. Item 6: obtain J&R (or another [FT] Z_f source); then 1 d.
3. Item 5, trap kinetics (E9) with space charge (1 week). It reuses the item-3 release machinery for E^tr.
4. Item 2 anisotropic AMM and film interference (1–2 weeks); item 12 SoA/GPU parity; jump-to-ballistic Green's function; k-space NEE (each M).
5. Items 7, 8, 9; item 11 (Voigt/sparse contraction for Exact as default, S); item 10 once α is sourced.
6. Replace the `AluminumFilm()` example constants with sourced Al film values.

---
## Interface flags
| ID | To | Item | Action |
|---|---|---|---|
| IF-DEV-1 | WP8-R (L41, §3.3), WP5 | η_pb(Ω, τ_l/τ₀^φ) | Source for η_pb at 4Δ < Ω ≤ 10Δ: 1401.1937 Fig. 4 [FT], reproduced by CMPMC to ≤ 0.011 (τ_l/τ₀^φ ≤ 4). At hν = 10Δ, η = 0.35/0.42/0.48/0.52(0.53)/0.55(0.59) for τ_l/τ₀^φ = 0.5/1/2/4/8 (CMPMC (Fig. 4)). It falls with Ω in thin films. Closes IF-AUD-2 and REF-WP8-R-A F4 / -B A3: L41 → ESTIMATED with this source |
| IF-DEV-2 | WP8-R §3.2 | oblique AMM | Flux-averaged over the hemisphere with P-SV mode conversion, the isotropic AMM gives t_L/t_T = 0.98/0.93 (Si/Al), 0.63/0.84 (Ge/Al: P critical angle, v_L(Al) > v_L(Ge)), 0.53/0.51 (Si/W) and 0.84/0.83 (Al₂O₃/Al). The normal-incidence L/T contrast ≤ 10% does not hold for Ge/Al (REF-WP8-R-A F5) |
| IF-DEV-3 | WP8-R §1.2(b), §4.3; WP7-E | gap channel | Collected-carrier energy E_rel routed through a 600 nm Al electrode film (Kaplan cascade) re-enters Ge as soft phonons: 49–51% of E_rel, mean 1.0 Δ_Al, 90–93% below 2Δ_Al. This is a [CALC]-grade mechanism for the "soft, ballistic" surface-recombination population (1109.1193 p.17 [FT]). ζ_O for this population is not zero in the model |
| IF-DEV-4 | coordinator / ENV.md (IF-AUD-1, -4) | defaults | Default surfaces changed (diffuse, p_anh = 0). Any [CALC] that used the G4CMP demo polynomials must opt in (`allow_unvalidated`) and say so. Gate: paer-sota ≥ 3d43a02 |
| IF-DEV-5 | coordinator | buffer bug | Before f61d710, a Kaplan-film phonon above ~130Δ (≈ 22 meV in Al) lost energy silently, and `escaped_or_killed` absorbed the remainder, so the closure checks did not see it. Check any R15-era run in which Debye-scale phonons reached a film unconverted (likely only the benchmark) |
| IF-DEV-6 | brief author | Z_f | Jacoboni–Reggiani RMP 55, 645 is closed access. IV Matrix stays guarded until a full-text Z_f source exists |

## Proposed LIMITS rows (coordinator assigns numbers)
| Label | Chain | Source | Conditions | Leading corrections | Status |
|---|---|---|---|---|---|
| DEV-L1 | Kaplan cascade + rate-competition loss → η_pb(Ω, τ_l/τ₀^φ) | 1401.1937 Eqs. (1)–(5), Fig. 4 [FT]; Kaplan τ_pb | T = 0, Debye α²F, lumped film, 2Δ ≤ Ω ≤ 10Δ | α²F(Al), T > 0, the E = Δ convention (+4%); thick-film gap 0.04 | CHECKED (≤ 0.011, τ_l/τ₀^φ ≤ 4) |
| DEV-L2 | elastodynamic BCs → isotropic AMM t(θ, mode), DMM | WP8-R §3.2 [E]; 1109.1193 T.I, 2408.04732 T3 [FT] | isotropic half-spaces, ideal interface | anisotropy, film interference (λ ≳ d), interface disorder (measured 0.3–0.55) | CHECKED (R+T = 1 to 1e-14; table 4.9e-4) |
| DEV-L3 | 1109.1193 Eqs. (26)–(30) → NTL spectrum with 2nd-order stepping | 1109.1193 §V.E [FT]; WP7-E-v3 (E11) | uniform field 1–100 V/cm, parabolic HV | non-parabolicity (≤ 1%) | CHECKED (≤ 2.4% vs converged) |
| DEV-L4 | WP7-E-v3 ledger "collection" → E_rel and its film down-conversion | WP7-E-v3 §1.3, Thm E-3; 1109.1193 p.17 [FT] | μ_F an input; Kaplan film at T = 0; electronic seed quanta ≤ 80Δ | hot-electron e–e stage above ω_D(Al); real electrode geometry | CHECKED (closure 1e-13; seed ≤ 1.2%) |

## Symbols introduced/used
**Used (NOTATION):** η_pb, F_qp, N_qp, Δ_BCS (written Δ in code and tables), E_g, μ_F, E_c, E_v, ℋ_ph, E_sig, d_film, ε_eh, ω, 𝒲_bias; WP7-E-v3 E_trap, E^tr; R15 𝔐, ℓ₀, f_dk, p_spec, p_diff, p_anh.
**Source-only (quoted, never used as campaign symbols):** τ₀^φ (Kaplan characteristic phonon time; G4CMP/CMPMC `phonon_lifetime`), τ_l (1401.1937 film phonon-loss time), τ_pb(Ω), η_s (1401.1937 photon
efficiency), a₀, a₁ (1109.1193 Eqs. (26)–(30)), Z_f (J&R final-valley number), α (non-parabolicity), R, β (1401.1937 RT coefficients).
**Introduced here:** E_rel ≡ E_kin + (E_c − μ_F) (e⁻) or E_kin + (μ_F − E_v) (h⁺), the energy a collected carrier releases at the contact (WP7-E-v3 ledger row "collection"); t_AMM(ν, θ), t_DMM,
the substrate→film transmissions (energy-flux, isotropic); I(Ω) ≡ ∫_Δ^{Ω−Δ}[E(Ω−E)+Δ²]/√((E²−Δ²)((Ω−E)²−Δ²)) dE, so that 1/τ_pb = I/(πΔτ₀^φ).
