# R15 / CMPMC-AUD: audit of the CMPMC transport engine against the campaign theory and the literature

Agent CMPMC-AUD, brief briefs/R15/CMPMC-AUD.md, amended by the coordinator mid-task. The amendment, at the user's request: fixes are real commits on a writable
clone `/home/user/cmpmc`, branch `paer-sota`, which is not pushed. The tests ship as CTest targets, a "SOTA upgrade list" is added (§6), and `/home/user/ytcs/CMPMC` @ 921db93 stays the
untouched reference. **All file:line citations refer to the reference tree 921db93** unless they are marked `paer-sota`.
**Inputs:** the CMPMC source (every header in include/cmpmc/, PLAN.md, CONTRIBUTING_PHYSICS.md), the G4CMP source (read-only clone /home/user/ytcs/G4CMP-ref @ 09b04bc, V10-06-00),
WP5-v4 §1.2, §5, §6.4, WP7-E-v3 §1–§2, WP8-R §0–§3, CONVENTIONS, NOTATION and code/ENV.md. WP2-v3 and WP7-T-v2 were searched for phonon-transport formulas rather than read in full; none bears on CMPMC.
**Literature [FT]**, read in literature/papers-CMPMC-AUD/ with the PDFs deleted afterwards: 1109.1193 (Leman), 2302.05998 (G4CMP paper), 2408.04732 (phonon
parameters for new materials), 1401.1937 (Guruswamy et al., η of thin films). **ID correction:** the brief's "2302.04315" is a polymer-photonics paper and not G4CMP. The G4CMP paper is
2302.05998, which WP8-R also cites. Tamura PRB 31, 2574 (1985), Kaplan PRB 14, 4854 (1976), Herring–Vogt (1956) and Jacoboni–Reggiani (1983) are not on arXiv. **Not
accessed.** They enter only as quoted in the [FT] papers or as implemented in G4CMP.
**Code:** code/CMPMC-AUD/ holds tests/ (10 drivers, identical to the repo's tests/), run_tests.sh, out/ref/ (unpatched 921db93, report-only) and out/sota/ (patched),
and patches/ (9 `git format-patch` files). Builds are in /root/cmpmc-aud-build. Every test is single-core and takes ≤ 15 s. The 4-thread benchmark ran through run-heavy.sh (§2 T11).

---
## 0. Verdict at a glance
- **Before patching, CMPMC 921db93 was not usable for any campaign phonon spectrum or arrival-time number.** Its L-phonon decay kinematics (daughter energy split and L→TT
  angle) are not G4CMP's and do not conserve momentum. Its surface model drops G4CMP's surface down-conversion. Its default group-velocity table is coarse exactly along
  the crystal z axis. NTL phonons came out too hard at ≥ 10 V/cm.
- **9 commits on `paer-sota` fix these** (§3). The suite now passes 10/10 CTest targets. Against 921db93 the same sources fail 47 checks (out/ref/).
- **Ported correctly and confirmed independently:** Christoffel solver (closed forms to 1e-10; v_g = ∇_kω to 1e-9); isotope B rebuilt from isotope
  abundances to 0.5–2.7%; Luke rate and angles (Golden rule = Leman Eq. (22)); l₀ against Leman Table II (≤ 3%); the Fano sampler (Var/N = F to < 1%); the (W4) bookkeeping;
  the Kaplan samplers; and η_pb, which is exactly 2Δ/Ω below 4Δ and reaches 0.590 asymptotically, against 0.59 in 1401.1937.
- **Not usable in any form:** the Tier-4 shortcuts (jump-to-ballistic, fast-chord HV Luke, NEE), the SoA engine and the "GPU" wavefront pipeline (§4, §5).

---
## 1. Inventory and per-model rating
Ratings: PASS · PASS WITH CAVEAT (range stated) · FAIL (discrepancy, size) → patched (P#, §3) · NOT USED. Test labels are TN (§2).

### 1.1 Phonons
| Model (921db93 file:line) | Implemented | Campaign / literature | Rating, evidence |
|---|---|---|---|
| Christoffel + v_g, physics/phonon_physics.hpp:152–254 | Jacobi eigen-solve of D_il = C_ijlm k̂_jk̂_m/ρ; v_g,d = e_iC_ijld k̂_j e_l/(ρv_p); L = polarisation most ∥ k̂, FT/ST ordered by v_p | 2408.04732 Eq. (11) [FT]; Leman §III [FT] | **PASS.** [100]/[110]/[111] for Si/Ge/GaAs agree with the closed forms to 1e-10, and v_g agrees with a finite-difference ∇_kω to 7e-10 (T1). Caveat: at FT/ST degeneracies the mode label, and so v_g, is ill-defined (physics, not code) |
| v_g lookup, lattice.hpp:63–88 (181×361, uniform in cos θ, bilinear) | used by every engine call | — | **FAIL → P3.** The polar step near the crystal z axis is ≈ 8°. The q99 direction error is 14–16 mrad for L in Si/Ge (max 84 mrad) and 10–14 mrad for T (max 0.43 rad), with 1% of directions off by more than 1° (T1). The error is concentrated where an (001) wafer's sensors are |
| octahedral FP32 LUT, lattice.hpp:118–150 (256², float4) | Tier-2 table | — | **PASS WITH CAVEAT:** q99 is 0.2 mrad (L) and 2.5 mrad (T). Errors above 1° occur only on FT/ST degeneracy lines (0.12% of directions), and |v_g| q99 is < 8e-4. It is the default after P3 (52 ns per call; the exact solve takes 1.7 µs) |
| isotope, phonon_physics.hpp:31–35 | Γ = Bν⁴, the same for all modes, then DOS-weighted mode and isotropic k̂ | WP8-R §2.1 𝒜_iso f⁴; 2408.04732 Eqs. (3)–(9) [FT] | **PASS WITH CAVEAT** (ICA: one mode-averaged B; valid for f ≪ f_D, where dispersion is weak). Rebuilt B = 4π³Γ_mdΩ⟨v_p⁻³⟩ from IUPAC abundances and CMPMC's own solver: Si 2.442, Ge 37.5, GaAs 7.42 (×10⁻⁴²), against presets 2.43, 36.7, 7.22 (0.5–2.7%, T3) |
| anharmonic rate, phonon_physics.hpp:39–44 | Γ = Aν⁵ for L, 0 for T | WP8-R §2.1 (L only, 2302.05998 "negligible … not implemented" [FT]) | **PASS WITH CAVEAT** (ICA, f ≪ f_D, T = 0). The constant is uncertain: Si 0.741 (Tamura, as quoted in 2408.04732 T3) vs 1.15 calc. Ge 6.43 preset vs 6.8 calc, 16.5 (Tamura) and 1.61 (1109.4343): a ×10 spread, so f_* ∝ A^{−1/5} shifts by ≤ 1.6 (WP8-R). T-mode decay beyond the ICA is absent (§6) |
| L→L′T energy split, phonon_physics.hpp:94–113 | ad-hoc expression in (β, γ, λ, μ, θ_L, θ_T) labelled "G4CMP FV4" | Leman Eq. (9) [FT] = G4CMP GetLTDecayProb | **FAIL → P2.** Sampled ⟨x⟩ = 0.860 (Ge) and 0.989 (Si) against 0.659 and 0.664; Var(x) is wrong by ×3 and ×0.09 (T2). After P2 the moments agree to < 1e-3 |
| L→TT energy split, phonon_physics.hpp:117–145 | ad-hoc, asymmetric | Leman Eq. (12) [FT] = G4CMP GetTTDecayProb(d, d·x) | **FAIL → P2.** ⟨x⟩ = 0.386 and 0.390 against 0.5 exactly by the x↔1−x symmetry; Var(x) is wrong by 45–64% |
| decay angles, phonon_physics.hpp:72–90 | θ_L′ and θ_T correct; θ_TT = acos[(1 + x² − (1−x)² − 1/m²)m/(2x)] | Leman Eqs. (10), (11), (13), (14) [FT] | L′T: **PASS** (|Σk − k₀|/k₀ < 2e-13). TT: **FAIL → P1.** At x = ½ it gives cos θ = 1 instead of 1/m, and the momentum residual reaches 64% (Ge) and 67% (Si) of k_L (T2) |
| decay energy conservation, engine.hpp:847–897 | xE + (1−x)E | — | **PASS** (exact) |
| polycrystal, phonon_physics.hpp:48–51 | Γ = v_g/λ_poly | G4CMPPhononPolycrystalElasticScattering | PASS WITH CAVEAT (grey, v-independent λ); **NOT USED** (single crystals) |
| surface reflection, geometry.hpp:55–58, engine.hpp:526–543 | p_spec = P_spec(min(f, 350 GHz)), otherwise diffuse; anh_coeffs never used | G4CMPSurfaceProperty + PhononBoundaryProcess (3-way, normalised, plus surface down-conversion) | **FAIL → P8** against the port claim. Using G4CMP's example coefficients: p_anh = 0.04, 0.15 and 0.47 at 300, 400 and 500 GHz is missing, and above 520 GHz p_spec = 0.60 where G4CMP has specProb = 0 (T9). Those coefficients are G4CMP's own *demonstration values* ("not well-motivated"), so **no campaign number may use them**. AMM/DMM is absent (§6) |
| Lambertian re-emission, engine.hpp:836–845 | Lambertian in k̂, then 16 tries for v_g·n > 0 | G4CMP LambertianReflection | PASS WITH CAVEAT: the cosine law applies to k̂, not to v_g, which is G4CMP's convention too |
| prompt phonons, partition.hpp:137–160 | mono-energetic at hν_D with DOS mode mix | WP8-R §1: ER/NR prompt populations sit at the optical/Debye scale; ν_D(Ge) = 8.64 THz (1109.1193 T.I [FT]) | PASS WITH CAVEAT (no created-phonon spectrum; WP8-R IF-R1). Ge preset had **2 THz**, below the acoustic band edge → **P4**. Memory loss by ≲ 100 ns (WP8-R §2.3) limits the effect to the first ~100 ns of arrival times |

### 1.2 Charges
| Model (921db93 file:line) | Implemented | Campaign / literature | Rating, evidence |
|---|---|---|---|
| HV valleys, lattice.hpp:365–407 | m_c = 3/Σm_i⁻¹; T = diag(√(m_c/m_i)); E = √(p*² + m_c²) − m_c; v = M⁻¹p | Leman Eq. (23), Table II [FT] | PASS: E_kin(p ∥ [111]) = p²/2m_l to 6e-7 (T6). **FAIL → P6:** the valley axes ignored `orient`, giving a velocity error of up to 15|v| for a Miller-rotated crystal (T6). No non-parabolicity in the kinematics (α is used only in the Matrix IV rate) → caveat: E_kin ≲ 0.1 eV |
| l₀ = πħ⁴ρ/(2m³Ξ²), lattice.hpp:392–403 | — | Leman Table II [FT] | **PASS:** Si e 16.75 / h 7.46 µm (Leman 16.9 / 7.5), Ge e 264.8 / h 107.5 µm (257 / 108) (T5) |
| Luke rate, charge.hpp:81–105 | Γ = (v_L/3l₀)(M−1)³/M, M = k/k_s | Leman Eq. (22) [FT]; Golden rule [D] | **PASS.** It equals ∫ Eq. (22) dθ to 1e-11 at M = 1.5–20 (T5). **Finding [D]:** Leman Eq. (21) and 2302.05998 Eq. (8) print (M−1)³/M², which is inconsistent with their own Eq. (22)/(9) by a factor M. The Golden rule with \|M_q\|² = Ξ²ħq/(2ρVv_L) gives Γ = 2Ξ²m(k−k_s)³/(3πρv_Lħ²k) = (v_L/3l₀)(M−1)³/M. G4CMP's code comment calling for "mach·mach" (G4CMPProcessUtils.cc:629) is therefore wrong, and the code is right |
| Luke angle and energy, charge.hpp:108–165 | cos θ = 1/M + (1 − 1/M)u^{1/3}; q = 2(k cos θ − k_s); E = ħv_Lq_HV; recoil set by energy conservation in HV space | Leman (22) and §V.C ("maintain the phonon momentum magnitude") [FT] | **PASS:** ⟨cos θ⟩ and ⟨E_ph⟩ agree with (22) to ≤ 8e-4 (T5). The HV non-unitarity caveat (momentum not exactly conserved for e⁻) is inherited from G4CMP and Leman |
| drift stepping, engine.hpp:151–271 | rates taken at step start; fixed 100 ps cap | Leman §V.D [FT] (rate ≈ const per step); WP7-E-v3 (E11) | **FAIL → P5.** The per-carrier closure ΣE_Luke + ΔE_kin = eℰ·Δr fails by up to 1.2% at 10⁴ V/m, and the NTL spectrum is too hard: ⟨E_Luke⟩ 6.70 vs 4.62 meV (Si e⁻), 7.40 vs 5.28 (Si h⁺), 4.98 vs 4.68 (Ge e⁻) at 100 V/cm (T5). After P5: closure < 6e-5, converged to < 3% |
| collection energy, engine.hpp:210 | E_kin + E_g/2 recorded as a hit, no phonons emitted | WP7-E-v3 Thm E-3 (E_c − μ_F, μ_F − E_v) | PASS WITH CAVEAT (μ_F at mid-gap; no gap-phonon spectrum → §6 item 3) |
| IV Quadratic/Linear, charge_physics.hpp:83–100 | G4CMP fits | G4CMPIVRate{Quadratic,Linear} | **PASS** (identical to G4CMP, T6). These are empirical fits (Edelweiss Ge; Stanford Si), valid in their calibration field range |
| IV Matrix, charge_physics.hpp:39–80 | Z_f = 2N−1 for every phonon; Erginsoy impurity term added to the IV rate | Jacoboni–Reggiani (not accessed): Z_f = 1 (g) and 4 (f) in Si; 3 in Ge [UNVERIFIED] | **PASS** as a port. **CAVEAT/FAIL vs J&R:** the Si rate is ×3.96 the per-type Z_f value (T6), and neutral-impurity scattering is intra-valley and should not change the valley. Not a default; **DO NOT USE** until fixed (§6) |
| trapping, impact ionisation, charge_physics.hpp:104–127 | Γ = v/λ (constant mean free path), knock-on at 1 µeV | WP7-E-v3 (E9) with constant σ: λ = 1/(σ𝓃) | PASS WITH CAVEAT: no emission, no speed-dependent σ, no space charge (E_es), no filling of n_j(t). Adequate for Hecht-type ⟨𝔵|z⟩ (E10) at constant σ |
| charge cloud, charge_physics.hpp:132–152 | radius 0.25 a₀N^{1/3} | G4CMPChargeCloud | PASS WITH CAVEAT (geometric; irrelevant beyond µm) |

### 1.3 Partition, Fano, NIEL
| Model | Implemented | Campaign | Rating |
|---|---|---|---|
| (W4) bookkeeping, partition.hpp:75–164 | ω = N E_g + 2N·5 meV + hν_D·N_ph | WP5-v4 (W4) at zero field | **PASS** (closure 1e-15, T7). Each carrier's 5 meV is relaxed by Luke emission |
| Fano sampler, niel_models.hpp:200–260 | interpolated binomial / Gaussian | WP5-v4 §6.4 (Fano definition) | **PASS:** ⟨N⟩ to 3e-4 and Var/⟨N⟩ = F to < 1% for n̄ = 2–10⁴ and F = 0.119–0.30 (T7) |
| ε_eh, F (Si), presets.hpp:41–42 | 3.81 eV, 0.15 (G4CMP) | 3.749 eV, 0.119 (WP5-v4 §6.4, 2004.11499) | **FAIL → P4** (1.6% and 26%) |
| NIEL yields, niel_models.hpp:43–170 | Lindhard / Lewin–Smith / Sarkis / IMPACT / empirical | WP5-v4 L20 (Lindhard), Thm E-2 | PASS as a port (the formulas are G4CMP's; not re-derived). **CAVEAT:** the yield is applied to E_R, which Thm E-2 forbids for E_st-corrected quantities, and it is not derived below E_R,th (WP5 §3.3). Use only above ~0.4 keV and only as the "Lindhard" WP6 option |

### 1.4 Superconductors
| Model | Implemented | Campaign / literature | Rating |
|---|---|---|---|
| Kaplan film samplers, kaplan.hpp:140–181 | sin² / u² substitutions | Kaplan 1976 densities = WP5-v4 §5 seed P(E₁\|ω) | **PASS:** moments to ≤ 8e-4 at 2.5–20Δ (T8). The thermal (1 − f − f) factor is dropped (G4CMP keeps it; negligible for k_BT ≪ Δ) |
| η_pb of the film model, kaplan.hpp:61–137 | lumped cascade, low_qp_limit = 3Δ | WP5-v4 (W13): η = 2Δ/Ω for Ω < 4Δ; 0.57–0.6 asymptote (1401.1937 [FT]) | **PASS** in the no-loss limit: 2Δ/Ω to 1e-12 for Ω < 4Δ, then 0.569 (4.5Δ), 0.595 (6Δ) and 0.590 for 10–100Δ (T8). The rise above 4Δ is the 1401.1937 Fig. 4 structure. **"η_pb flat above 4Δ" is false** below 5Δ and holds only in the no-loss limit. With the 600 nm film escape law, η = 0.65 (3Δ), 0.53 (5Δ), 0.48 (10Δ) and 0.46 (40Δ): it falls with Ω, as in 1401.1937 |
| film escape law, kaplan.hpp:51–58 | λ = v_sτ₀/(1 + 0.29(Ω/Δ − 2)), path 4d / random | 2302.05998 Eq. (18) [FT]; exact Kaplan τ_pb | PASS WITH CAVEAT: within 6% of the exact Kaplan τ_pb on 2.5–40Δ (T8). Isotropic-film lumping; no AMM |
| subgapAbsorption, kaplan.hpp:184–193 | applied to **every** incident phonon ≥ 2Δ_abs | 2302.05998 text says sub-gap only [FT]; the G4CMP code does the same as CMPMC | CAVEAT: E_sig ≠ Δ_BCS N_qp unless subgap_absorption = 0. With it at 0, edep = Δ N_qp + 0 exactly, i.e. the (W13) [A-7] E_sig |
| KaplanSurrogateLUT, kaplan.hpp:224–298 | (abs, Σrefl) quantiles, 64 bins, nearest-lower bin, one merged re-emitted phonon | — | **FAIL → P7:** collected fraction +10% at 3Δ, and +5% to +13% in a p_ret = 0.9 cavity, because the merged phonon re-breaks pairs (T8). After P7 the error is < 1% |
| 3D Bogoliubov QP, physics/superconductor_3d.hpp | Kaplan τ_pb, τ_s and τ_r integrals with singularity-free quadrature; D = D_n√(1 − Δ²/E²) | Kaplan 1976 (not accessed; checked against G4CMP and against the closed form at Ω = 2Δ) | PASS WITH CAVEAT: 1/τ_pb(2Δ) = 1/τ₀^ph exactly. LUTs are clamped above 60Δ (Al: 10 meV). Recombination is with thermal QPs only (no QP–QP or Rothwarf–Taylor term), the gap is fixed, boundaries are diffuse only, and qp_velocity = 10⁶ m/s is a placeholder. **NOT USED** by any campaign computation in hand |
| excitons, magnons, custom_excitation_example.hpp | toy models | WP7-E-v3 §7 | **NOT USED** |

---
## 2. Independent tests (code/CMPMC-AUD/tests = repo tests/, CTest; out/ref = 921db93, out/sota = paer-sota)
| # | Test | What is compared | 921db93 | paer-sota |
|---|---|---|---|---|
| T1 | test_christoffel | closed-form v at 3 axes × 3 materials; v_g vs FD ∇ω; LUT error quantiles (Ge, Si, Al₂O₃) | 2 FAIL (bilinear q99) | PASS |
| T2 | test_anharmonic_decay | Σk = k₀ for every x; ⟨x⟩ and Var(x) against Leman (9), (12); E conservation | 12 FAIL | PASS (< 1e-3) |
| T3 | test_presets | Voigt C_ij, A, B, F_TT, DOS, v against G4CMP config.txt (read with CMPMC's own reader); B rebuilt; campaign ε_eh, F, ν_D | 11 FAIL | PASS |
| T4 | test_rates | Bν⁴, Aν⁵ (L), 0 (T) at 0.3–10 THz | PASS | PASS |
| T5 | test_luke_ntl | l₀ against Leman T.II; rate against ∫(22); angle and energy moments; (E11) closure at 1/10/100 V/cm for e⁻/h⁺ in Ge/Si; step convergence | 6 FAIL | PASS |
| T6 | test_charge_misc | v covariant under crystal rotation; HV E_kin and v; IV forms; Matrix vs J&R Z_f (reported) | 1 FAIL | PASS |
| T7 | test_fano_partition | Fano moments (18 cases); (W4) closure | PASS | PASS |
| T8 | test_kaplan | samplers; η_pb(Ω/Δ); escape law against exact τ_pb; surrogate against full cascade in a cavity | 5 FAIL | PASS |
| T9 | test_surface | p_spec and p_anh against G4CMP formulas at 6 frequencies; engine branching fraction | 10 FAIL | PASS (branching 0.281 vs 0.279) |
| T10 | test_headers_compile | all headers, including SoA/GPU, compile; phonon-run energy closure 1e-9 | PASS | PASS |
| T11 | examples/phonon_benchmark 5000 (4 threads, run-heavy.sh) | throughput and energy closure | 12.7 M steps/s; closure 5e-14 | 16.2 M steps/s; closure 6e-14 (the primaries carry 4.3× more energy because Ge ν_D is now 8.64 THz). The ±0.5 eV calorimeter scatter in demo [3] is Luke 5% sub-sampling noise (σ ≈ 0.55 eV) |

Hard checks: 47 fail on 921db93; **0 of the same checks fail on paer-sota**. `ctest`: 10/10 pass in 31 s. The legacy-path numbers stay in the sota output as
informational lines.

---
## 3. Fixes (branch `paer-sota` of /home/user/cmpmc, one logical fix per commit; diffs in code/CMPMC-AUD/patches/0001–0009)
| P | Commit | Corrected formula / change | Source | Rerun |
|---|---|---|---|---|
| P1 | 0ae1d90 | cos θ_T1 = (1 − m²(1−x)² + m²x²)/(2mx); second daughter x → 1−x | Leman (13)–(14) [FT]; G4CMP MakeTTDeviation | T2: residual 3e-15 |
| P2 | 9f57e30 | P_LT(x) ∝ x⁻²(1−x²)²[(1+x)² − m²(1−x)²][1 + x² − m²(1−x)²]²; P_TT(x) = Leman (12) at X = mx with A, B, C, D | Leman (9), (12) [FT]; G4CMP Get{LT,TT}DecayProb | T2 |
| P3 | 6f1043e | default kinematics = octahedral LUT; `KinematicsMode::{Octahedral, Exact, Bilinear}` | 2408.04732 Eq. (11) [FT] | T1: q99 16 → 0.2 mrad |
| P4 | 7d6d44d | GaAs A = 7.778e-55 s⁴, F_TT = 0.778, DOS 0.584:0.337:0.078, v = 5130/3020 m/s, ν_D = 8.58 THz; Si ε_eh = 3.749 eV, F = 0.119; Ge ν_D = 8.64 THz | G4CMP config.txt; 2408.04732 T3–T5 [FT]; WP5-v4 §6.4; 1109.1193 T.I [FT] | T3 |
| P5 | 69252ee | \|Δk\| per step ≤ f_dk·max(k_s, \|k\|) (HV frame for e⁻), f_dk = `charge_max_dk_frac` = 0.05 (0 = legacy) | Leman §V.D [FT]; WP7-E-v3 (E11) | T5 |
| P6 | 623ceeb | valley axes rotated by `orient` | Leman (23) [FT] | T6: 15 → 5e-15 |
| P7 | c5596c4 | surrogate stores complete outcomes (absorbed fraction plus the list of re-emitted phonons); stochastic 2-node interpolation; exact path outside [2Δ, 40Δ] | Kaplan cascade as KaplanFilm | T8: < 1% |
| P8 | c8267c9 | G4CMP three-way split (p_spec, p_diff, p_anh), normalised; surface down-conversion with Lambertian daughters; `spec_prob_const` | G4CMPSurfaceProperty / PhononBoundaryProcess | T9 |
| — | cd56e1b | tests/ plus `CMPMC_BUILD_TESTS` (enable_testing, add_subdirectory) | — | ctest 10/10 |

**Verified:** `git am --3way patches/*.patch` applies cleanly to a fresh 921db93 clone; the resulting include/ is byte-identical to paer-sota, and ctest passes 10/10.
After P7 the KaplanSurrogateLUT constructor runs 128×512 full cascades (≈ 1 s once at start-up, also in the SoA/GPU constructors); this is not a per-step cost.
Not patched (no default campaign path uses them; listed in §6): IV Matrix Z_f, the SoA engine's missing L→L′T branch and isotropic daughters, the GPU
pipeline's isotropic daughters, and the Tier-4 shortcuts. **Not pushed; main untouched.**

---
## 4. Usage verdict (gate of code/ENV.md: only PASS modules feed [CALC]; corrected models only from paer-sota)
| Module (paer-sota) | Verdict | Cleared observables (validity) |
|---|---|---|
| CrystalLattice kinematics (Octahedral/Exact), Christoffel | **USE WITH PATCH** (P3; Exact for caustic imaging) | arrival-time distribution, position dependence, focusing (any f in the non-dispersive regime f ≲ 1 THz Si/Ge; above that, dispersion is ignored) |
| bulk isotope + L decay (`transport`), with P1, P2 | **USE WITH PATCH** | arrival times, frequency spectrum at the sensor, quasidiffusion (ICA, T = 0). The ×10 spread in Ge A must be carried as a nuisance (WP8-R C1c) |
| surface reflection with P8 | **USE WITH PATCH, with campaign-supplied p_spec, p_diff, p_anh** | none with the G4CMP demo coefficients; AMM/DMM must be supplied externally (WP8-R §3.2 table) until §6 item 2 |
| Kaplan film (KaplanFilm) | **USE** with subgap_absorption = 0 for E_sig = Δ_BCS N_qp | collected-energy fraction, η_pb(Ω) per (W13) (lumped film, isotropic escape, Ω ≤ 100Δ) |
| KaplanSurrogateLUT | **USE WITH PATCH** (P7) | as KaplanFilm, to < 1% |
| charge drift + Luke (`transport_charges`) | **USE WITH PATCH** (P5, P6) | NTL heat and (E11) closure, NTL phonon spectrum, drift/Hecht ⟨𝔵\|z⟩ (E10) at constant σ; E ≤ 10⁴ V/m tested; E_kin ≲ 0.1 eV (parabolic HV) |
| IV Quadratic/Linear | **USE** inside the fitted field range | δ_coll, r_coll through the drift (fit-limited) |
| IV Matrix | **DO NOT USE** | — |
| trapping / impact ionisation | **USE** with caveat | ⟨𝔵\|z⟩ at constant λ_tr; not (E9) kinetics, emission or space charge |
| EnergyPartition + Fano | **USE WITH PATCH** (P4) | N_eh sampling, (W4) heat split; ER only; NR only above E_R,th through a WP6 yield option |
| Superconductor3D (bulk QP) | **NOT CLEARED** (caveats §1.4) | — |
| `transport_charges_fast_chord` | **DO NOT USE** | fixed M = 2.2 sets a single NTL energy per chord (wrong spectrum); collection drops E_kin |
| `jump_to_ballistic_cascade` | **DO NOT USE** | fixed-radius random jump (a shell, not a 3D Gaussian), rounded N_iso, cap of 48 daughters, isotropic k̂ |
| `evaluate_sparse_sensor_nee`, Russian roulette | NEE **DO NOT USE** (Lambertian in real space ignores focusing; not wired into the engine); roulette **USE** (unbiased w/p) | — |
| WavefrontSoAEngine, gpu WavefrontPipeline | **DO NOT USE** | SoA: L→TT only (no L′T branch), isotropic daughters, diffuse-only walls, only the first re-emitted phonon kept; GPU: isotropic daughters |
| mesh fields, electrode masks, polycrystal, excitons/magnons, NIEL beyond Lindhard | NOT USED (not audited numerically) | — |

---
## 5. PLAN.md "physics shortcuts": error on the campaign observables
| Shortcut | Measured or argued error | Observables at risk | Status |
|---|---|---|---|
| 181×361 bilinear v_g LUT (Tier 1) | q99 14–16 mrad (L), up to 0.43 rad (T) near the crystal z axis (T1) | position dependence, focusing pattern, early arrival time | replaced by octahedral (P3) |
| 256² FP32 octahedral LUT (Tier 2) | q99 0.2 / 2.5 mrad, \|v_g\| < 8e-4; > 1° on 0.12% of T directions (degeneracy lines) | negligible for timing (2.5 mrad × 1 cm = 25 µm) | default |
| 1024-bin inverse-CDF decay tables | moments to < 1e-3 after P2 (T2); 4096-point midpoint CDF | spectrum | PASS |
| KaplanSurrogateLUT (Tier 4.1) | +10% at 3Δ, +13% in a cavity (old); < 1% (P7) | collected-energy fraction | patched |
| jump-to-ballistic (Tier 4.2) | not quantified: the displacement is a fixed-radius shell, so the time spread is lost; the L fraction uses fLDOS rather than the steady mix | arrival time, position dependence | DO NOT USE |
| HV chord Luke (Tier 4.3) | NTL energies set by the assumed M = 2.2, not the field; collection drops E_kin | NTL spectrum, (E11) per carrier | DO NOT USE |
| NEE / roulette (Tier 4.4) | NEE ignores focusing and is not unbiased-wired; roulette unbiased | sparse-sensor yield | NEE no; roulette yes |
| QP LUTs 60Δ clamp; 64-node quadrature | exact at Ω = 2Δ; clamped above 60Δ | bulk-QP absorbers | not cleared |

---
## 6. SOTA upgrade list (prioritised; for the follow-up implementation agent)
| # | Physics CMPMC lacks | Formula / model | Source | Effort |
|---|---|---|---|---|
| 1 | Frequency- and thickness-dependent pair-breaking efficiency with film phonon loss | Chang–Scalapino kinetic equations, or event MC of (W3) with the Eliashberg α²F, coherence factors (1 ± Δ²/E₁E₂), the escape rate Γ_esc(d_film) and 2Δ-phonon trapping 1/(τ_l/τ_pb + 1); output η_pb(Ω, d_film, T) and F_qp | WP5-v4 §5 (W13) specification; 1401.1937 Eqs. (1)–(5) [FT] | L (2–3 wk); a table-driven η_pb(Ω, d) from an offline solve: M (3 d) |
| 2 | AMM/DMM interface transmission per mode and angle (substrate → film, and film re-emission) | AMM: Christoffel-matched plane-wave boundary conditions (6×6 Snell problem, anisotropic), t_ν(θ, φ); DMM: t₁₂ = Σc₂⁻²/(Σc₁⁻² + Σc₂⁻²); thin-film interference for λ ≳ d_film | WP8-R §3.2 (isotropic AMM/DMM table) [E]; 1805.02495 (cited [FT] in WP8-R) | M–L (1–2 wk anisotropic; 2 d isotropic) |
| 3 | Gap-energy / recombination phonon spectra at electrodes and traps | at collection or recombination emit E_c − μ_F (μ_F − E_v) as phonons with a recombination spectrum (multiphonon/Auger, high f), E_g − E^tr at traps; time-tagged release of E_X, E_trap | WP7-E-v3 (E1), Thm E-3, §2.1; WP8-R §1.2 item (b) | M (3–5 d) |
| 4 | Second-order Luke time stepping (Leman) to replace the Δk cap of P5 | t = (√(a₀² − 2a₁ ln u) − a₀)/a₁, a₁ = (τ₁⁻¹ − τ₀⁻¹)/(t₁ − t₀), plus velocity Verlet | Leman §V.E Eqs. (26)–(30) [FT] | S (1–2 d), with a 10–20× speed-up at high field |
| 5 | Trap kinetics (E9) instead of constant λ_tr | dn_j/dt = σ_j(u)u n_f(𝓃_j − n_j) − Γ^em n_j − σ^rec u n_h n_j, with history n_j(t), speed-dependent σ and space charge E_es | WP7-E-v3 (E9)–(E12) | M (1 wk) |
| 6 | IV Matrix model with per-type Z_f and intra-valley impurity scattering | W = Z_f m_d^{3/2}D_f²√(E ∓ ħω)(1 + 2αE)[n + ½ ∓ ½]/(√2πρħ²ω); Si g: Z = 1, f: Z = 4; Ge: Z = 3; Erginsoy as momentum relaxation | Jacoboni & Reggiani RMP 55, 645 (1983) [UNVERIFIED, to fetch] | S (1 d) |
| 7 | Created-phonon spectrum of the prompt cascade (ER, NR) instead of a Debye line | branch-projected ρ^ph_κ from WP2 (3.6) (NR, x_R ≲ 1); e–ph emission kernel of WP5 §2 (ER); MD tables (NR ≳ eV) | WP8-R IF-R1; WP2-v3 (3.6); WP5-v4 §2, §3.4 | M |
| 8 | Dispersive phonons and T-mode decay beyond the ICA (f ≳ 1 THz) | DFPT ω_ν(q), v_g from the dispersion (QE ph.x, available), Tamura 3-phonon rates with the full cubic tensor, T → T + L channels | 2408.04732 §2.1 (refs [30–32]) [FT]; WP2-v3 dispersion | L |
| 9 | QP–QP recombination and gap suppression (Rothwarf–Taylor) in Superconductor3D; un-clamped LUTs | dN/dt = −RN² + 2βN_2Δ …, R from Chang–Scalapino (A9) | 1401.1937 Eqs. (2)–(5) [FT] | M |
| 10 | Non-parabolic HV kinematics | ħ²k*²/2m_c = E(1 + αE), with v and the Luke threshold modified | Jacoboni–Reggiani [UNVERIFIED] | S |
| 11 | Faster exact Christoffel solve (closed-form cubic eigenvalues) so Exact can be the default | Cardano roots plus eigenvectors by cross products | standard algebra [D] | S (≤ 1 d) |
| 12 | SoA/GPU engines brought to parity with `transport` (LT branch, decay angles, P8 surfaces, all re-emitted phonons) | as in the engine | — | M |

---
## 7. Notes for the record
- G4CMP inconsistencies found, besides those in the port. (i) The comment at G4CMPProcessUtils.cc:629 is wrong: the code's (M−1)³/M is right, and Leman Eq. (21) and 2302.05998 Eq. (8)
  have a typo relative to their Eq. (22)/(9). (ii) G4CMPVKaplanQP::CalcQPEfficiency has an operator-precedence bug, so its efficiency is always 1. CMPMC implements the intended
  absorberEff + slope·E/Δ, which coincides at the default slope 0. (iii) G4CMP's Ge "Debye 2 THz" and GaAs "6.56 THz" mix the max-acoustic and max-optical conventions.
- CMPMC's config_reader puts stiffness into C_custom and leaves C11 and the other named fields at the Ge defaults. Only build_voigt_matrix() is authoritative (T3 compares the Voigt matrices).

---
## Symbols introduced/used
**Used (NOTATION):** ε_eh, F_eh, N_eh, η_pb, N_qp, F_qp, Δ_BCS, E_g, ω, ℋ, 𝒲_bias, V_b, g_Luke, ⟨𝔵|z⟩, ℓ^tr_e/h, δ_coll, r_coll, E_sig, t_esc, d_film; WP8-R's 𝒜_anh, 𝒜_iso, f, f_*.
**Source-only (quoted, never used as campaign symbols):** Leman/G4CMP A, B (= 𝒜_anh, 𝒜_iso), δ (= v_L/v_T), x, X, l0, k_L, C/Ξ; G4CMP specProb, subgapAbsorption, phononLifetimeSlope δτ.
**Introduced here:** 𝔐 ≡ k/k_s, the carrier Mach number (k_s ≡ m v_L/ħ, in the HV frame for e⁻); ℓ₀ ≡ πħ⁴ρ/(2m³Ξ²), the carrier–acoustic-phonon length; ϱ_LT ≡ v_L/v_T; Γ_Luke ≡ (v_L/3ℓ₀)(𝔐 − 1)³/𝔐;
p_spec, p_diff, p_anh, the surface branching probabilities (sum 1); f_dk, the per-step wavevector-change bound of P5; Γ_md, the mass-defect coefficient (2408.04732 Eq. (5)).

## Interface flags
| ID | To | Item | Action |
|---|---|---|---|
| IF-AUD-1 | coordinator / ENV.md | CMPMC gate | campaign [CALC] runs must use /home/user/cmpmc @ paer-sota ≥ cd56e1b (after push) with the §4 verdicts; 921db93 is not cleared for phonon or NTL observables |
| IF-AUD-2 | WP8-R, WP5 | η_pb "flat above 4Δ" | false below ≈ 5Δ (0.51 at 3.9Δ → 0.595 at 6Δ → 0.590); flat only without film loss; with loss it falls (0.53 → 0.46 for 5–40Δ, 600 nm Al). Amend WP8-R §0 row 3 and §3.3 |
| IF-AUD-3 | WP8-R | Luke rate typo | quote Γ_Luke = (v_L/3ℓ₀)(𝔐−1)³/𝔐 (derived §1.2), not 1109.1193 (21) / 2302.05998 (8) |
| IF-AUD-4 | WP8-R §3 | surface coefficients | G4CMP's polynomial surface coefficients are demonstration values; any campaign run must supply p_spec, p_diff, p_anh (AMM/DMM, §6 item 2) |
| IF-AUD-5 | WP7-E | NTL spectrum | NTL phonon energies at 1–100 V/cm (paer-sota, 1 mm, Ge/Si): ⟨E_Luke⟩ = 0.75–4.7 meV (e⁻), 1.1–6.4 meV (h⁺) ([CALC] pending IF-AUD-1); the legacy 921db93 values are 5–45% too hard |
| IF-AUD-6 | WP5 / WP6 | Si ε_eh, F | the presets now carry the campaign 3.749 eV / 0.119; T-dependence at mK is not modelled |
| IF-AUD-7 | brief author | literature ID | the G4CMP paper is 2302.05998, not 2302.04315 |

## Proposed LIMITS rows (coordinator assigns numbers)
| Label | Chain | Source | Conditions | Leading corrections | Status |
|---|---|---|---|---|---|
| AUD-L1 | Leman (9), (12)–(14) → CMPMC decay kinematics (P1, P2) | 1109.1193 [FT] = G4CMP | ICA, T = 0, f ≪ f_D | anisotropic/dispersive decay; T-mode decay | DERIVED + CHECKED (T2) |
| AUD-L2 | Golden rule → Γ_Luke = (v_L/3ℓ₀)(𝔐−1)³/𝔐 and the angle law | 1109.1193 (22) [FT]; §1.2 [D] | deformation potential, T = 0, parabolic, HV | non-parabolicity, T > 0 absorption, optical/IV emission | DERIVED (T5) |
| AUD-L3 | (E11) per-carrier closure in CMPMC with P5 | WP7-E-v3 (E11) | uniform field ≤ 10⁴ V/m, no traps | space charge ΔE_es; f_dk → 0 | CHECKED (closure < 6e-5) |
| AUD-L4 | Kaplan lumped film → η_pb(Ω/Δ) | WP5-v4 (W13); 1401.1937 [FT] | no loss: 2Δ/Ω (< 4Δ), 0.590 (≥ 10Δ); lumped escape | Chang–Scalapino film solution (§6 item 1) | CHECKED (T8) |
| AUD-L5 | B = 4π³Γ_mdΩ⟨v_p⁻³⟩ | 2408.04732 Eqs. (3)–(9) [FT] | ICA, natural abundance | dispersion | CHECKED (0.5–2.7%, T3) |
