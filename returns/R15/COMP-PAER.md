# R15 / COMP-PAER: Si PAER kinematic window and order-of-magnitude rate/reach (M1 tier B, rescoped); tier H formulated

ID COMP-PAER. Brief: briefs/R15/COMP-PAER.md, **rescoped mid-run by the coordinator** (user deliverable directive, RULES.md: "the main deliverable is the
textbook … compute work can happen later unless the numerical value is important for physical reasons and/or critical to the framing"). Accordingly:
(i) the **window** (T5) is computed ab initio and is [CALC]; (ii) the **rate and reach** are an **order-of-magnitude, data-calibrated** estimate
[E] built on cheap first-principles inputs, not the §M10 sum-over-states; (iii) tier H (T6) and Ge are **FORMULATED** (inputs in the qe-rtsc
`rtsc/bench` layout), not run. No job was stopped mid-way; the amplitude pipeline (own g from dvscf + bare/non-local derivative, C6 frozen-phonon
check) was planned and dropped at the rescope before any code was written for it. Conventions: CONVENTIONS.md (§1 e² = 4πα, §3, §4, §5 EPW g, §6
S = q²L/2πα, §8 halo, §9 σ̄_e, F_DM); NOTATION v4. Tags: [CALC] (code/COMP-PAER/ holds inputs, pseudopotential, convergence record, control),
[E] estimated, [D] derived, [FT] full text, [DB]-like measured inputs marked "data". Status: CLAIMED, pending referee.

## 0. Results in brief
1. **Si window [CALC, PBE+scissor, controls C5 PASS].** PAER edge (free pairs, TA, emission, T = 0) **m_χ^{PA} = 0.3374 MeV**; exciton replica
   (E_x = E_g − 14.7 meV) **0.3333 MeV**; first zero-phonon final state (forbidden class G′ = 0, k_c − k_v pocket) reachable from **m_χ^{ZP} = 0.408 MeV**;
   allowed class (2̄00) from **0.547 MeV**; other Umklapp classes 0.562 MeV. These reproduce WP3-v3 §M9 / WP1-v3 [E13] (0.333/0.337, 0.42 (0.40–0.44),
   ≈ 0.54) and replace their parabolic [E] values: **Si strictly PAER-only band 0.333 (replica) / 0.337 (continuum) – 0.408 MeV [CALC]**; coexistence
   with the forbidden ZPL 0.408–0.547 MeV (PAER leading only near its lower end, WP3 §M9 (2), ratio ϖ_II not recomputed); allowed ZPL leads above 0.547 MeV.
2. **Rate/reach [E, ×/÷ 10].** Heavy mediator, 1 kg·yr, 3 events, ≥ 1 e⁻: σ̄_e^{95} ≈ 2.5×10⁻²⁵ cm² (0.337 MeV), 3×10⁻²⁹ (0.36), 7×10⁻³² (0.40),
   1.6×10⁻³² (0.42); light mediator 8×10⁻²⁸, 1.3×10⁻³¹, 4×10⁻³⁴, 1×10⁻³⁴ cm² at the same masses (§6 table). The steep fall is kinematic (η(v_min) at
   v_min → v_max); PAER can only set **interesting** (sub-10⁻³⁰ cm²) limits in the top ≈ 20–30 keV of its band, 0.38–0.41 MeV.
3. **Whether PAER matters (narrative answer).** In 0.333–0.408 MeV PAER is the *only* electronic channel (no zero-phonon state is reachable), so it alone
   sets the Si electron-recoil sensitivity there; at 1 kg·yr it reaches ≈ 7×10⁻³² cm² (heavy) / 4×10⁻³⁴ cm² (light) at 0.40 MeV (×/÷10), i.e. it extends the Si mass reach downward by ≈ 0.07 MeV below the zero-phonon threshold (0.408 MeV) at strongly reduced σ̄_e
   sensitivity. Above 0.547 MeV it is a 10⁻²–10⁻³ correction (C3).
4. **Tier H (T6) and Ge:** FORMULATED (§8, §9), gate verdict over limit (DFPT stage alone ≈ 24 h on the box).

## 1. Inputs, method, approximation level
**Electronic structure [CALC].** QE 7.6 (conda-forge, = qe-rtsc on CPU, code/ENV.md), PBE, SG15 ONCV **Si_ONCV_PBE-1.2.upf** (NC, l_max = 1, 4 projectors,
no NLCC), a = 5.431 Å (experimental, fixed; P = +23 kbar at PBE), ecut 40 Ry (§3), SCF k 8³. Bands: nscf on the Γ-centred **40³** grid (1661
irreducible points under O_h, unfolded in `scripts/ibz.py`), 8 bands. PBE indirect gap 0.557 eV → rigid **scissor +0.613 eV** on all conduction
bands so that E_g(0) = 1.170 eV (exp., includes ZPR). Direct gap at Γ (PBE+scissor) 3.17 eV.
**Phonons [CALC].** DFPT 4³ q grid, 8³ k, tr2_ph 10⁻¹⁶, q2r/matdyn with `asr='crystal'`. Check vs experiment at X: TA 17.0 (exp 18.6), LA=LO 50.7 (51.0),
TO 57.3 (57.5) meV; L: TA 13.1, LA 46.2, LO 51.4, TO 60.8 meV. The 4³ grid puts ω_TA(0.85X) = 17.1 meV ≥ ω_TA(X) (interpolation artefact, ≤ 1.5 meV).
**E_min(q) [CALC].** E_min(q) = min_k[ε_c(k+q) − ε_v(k)] on the 40³ grid (k restricted to valence states within 1.5 eV of the VBM), trilinear
periodic interpolation, 400 Fibonacci directions per |q|, |q| = 0.05–2.4 Å⁻¹ step 0.025 (`scripts/window.py`). Class of a final state: the nearest
pocket vector K_pk = k_c^{val} + G (k_c = 0.85X; WP3 §M3 notation): G = 0 (forbidden on axis), G = (2̄00) antiparallel to the valley (allowed), others.
**Reachability** (WP1-v3 [E13], WP3 §M9): channel open at m_χ iff min_q[E^{ch}(q)/|q| + |q|/2m_χ] ≤ v_max = 794.5 km/s (CONVENTIONS §8 reference frame).
PAER edge: E^{PA}(q) = E_g + min_{q̂, valleys} ω_TA(K_pk − q) (§M3 (b), C5), exciton replica E^{PA} − 14.7 meV (`scripts/paedge.py`, 16 500 matdyn Q).
**Rate model [E] (`scripts/rate.py`).** The §M10 amplitude was not computed (rescope). Instead, the ELF form (M.14)/(CONVENTIONS §6) with a measured
optical limit and a first-principles finite-q proxy:

  S̄^{PA}(q,ω) = q² L(q,ω)/(2πα),   L(q,ω) ≈ ε₂^{PA,opt}(ω) 𝔉_ρ(q) f_win(q,ω) / ε₁(q,ω)²,                                                  (P.1)

- ε₂^{PA,opt}(ω) = n(ω)α_abs(ω)ħc/ω from the **measured 20 K absorption** of Macfarlane et al. (data as plotted in 1202.3454 Fig. 2 [FT], digitised):
  (α_absħω)^{1/2} = 0.65 + 78(ω − 1.212 eV) (cm⁻¹eV)^{1/2} above the TO knee, linear ramp from 1.160 eV below it (TA/exciton replicas); n = 3.55 +
  0.37(ω − 1.17 eV). At 1.25 eV: α_abs ≈ 11 cm⁻¹, ε₂ = 5.9×10⁻⁴. Being measured, it contains excitons, local fields and the pair channel at q → 0 (so the
  [0.4, 1.8] interim factor of §M7 is *not* applied on top at q → 0); extrapolated linearly in (α_absħω)^{1/2} to ω ≤ 1.51 eV (α_abs(1.5) ≈ 330 cm⁻¹,
  consistent with the 78 K curve of 1202.3454 Fig. 3 within ×1.5).
- 𝔉_ρ(q) ≡ ⟨Σ_{v∈Γ₂₅′, c∈4 lowest}|ρ_cv(Γ,q)|²/q²⟩ / (same at q → 0) [CALC proxy, E as a model]: the dipole → saturation crossover of the DM vertex
  computed from the PBE wavefunctions (nscf at the unfolded k = q, coefficients matched by Miller index, `scripts/formfactor.py`; cubic average of
  [100], [110], [111] with weights 6:12:8). Values 1, 0.79, 0.50, 0.31, 0.18, 0.12, 0.077, 0.054, 0.040, 0.032, 0.024 at |q| = 0, 0.1, …, 1.0 Å⁻¹.
  Using the bare dipole extrapolation (𝔉 = 1) would overstate S̄ by ×10–40 in the relevant |q| = 0.3–0.9 Å⁻¹; whether the PAER amplitude M^{(2)} follows
  the zero-phonon vertex's fall-off is the main model assumption (M^{(2)} is linear in ρ, (M.1), but the m = v (A) and m = c (B) terms that cancel at
  q → 0 decorrelate at finite q, §M2); band [𝔉_ρ/3, min(1, 3𝔉_ρ)]. **Direction of the bias:** the uncancelled intraband (m = v, m = c) terms add amplitude that the
  interband proxy does not see, so 𝔉_ρ is more plausibly a *lower* estimate; the physical ceiling is the dipole extrapolation 𝔉 = 1, which at the q
  reached at 0.40 MeV (0.4–0.7 Å⁻¹) lies ×5–20 above 𝔉_ρ, i.e. at or just above the top of the quoted ×/÷10 band (σ̄_e lower by up to ×20). Supporting this: the triplet-averaged intraband vertex Tr\|ρ_vv(Γ,q)\|²/3 = 0.94 (0.1 Å⁻¹), 0.65
  (0.5 Å⁻¹) stays O(1) where Σ_c\|ρ_cv\|² is 0.05–0.23 [CALC, 100-band nscf].
- ε₁(q,ω): Cappellini model, ε₁(0,ω) = n(ω)² (≈ 12.6–13.5), k_TF = 1.104 a.u., ω_p = 16.6 eV (8 e/cell); ε₁ ≈ 6.7 at 0.5 Å⁻¹, 3.0 at 1.0 Å⁻¹ (ω = 1.3 eV) [E ±20 %].
- f_win(q,ω): fraction of q̂ with ω ≤ E_min(q) − δ₀ (window theorem (M.9)); δ₀ = 0.3 eV (strict) and δ₀ = 0 (includes the O4-d11 edge shell).
- Rate (M.6) with η(v_min) of the SHM (CONVENTIONS §8: v₀ = 238, v_esc = 544, |v_E| = 250.5 km/s, ρ_χ = 0.3 GeV cm⁻³), ρ_T = 2.329 g cm⁻³, F_DM per §9,
  T = 0 (emission only), ω from 1.161 eV. **Reach convention:** exposure 1 kg·yr, background-free, 3 events (≈ 95 % CL), threshold "any ω ≥ E_g ⇒ ≥ 1 e⁻"
  (single-electron readout, 100 % efficiency), fixed halo (WP6 R1 type); the annual v_max range 781–810 km/s is not propagated.
- Approximation level (τ, WP0 §6.1): `nB=0|ng=2|X=data(q→0)×model(q)|K=1ph-inc` + `T=0;scr=ε₁-model;conv=window`. Not included: phonon-energy shift of the
  threshold with q (TA(Q*) ≠ TA(K): ≤ 15 meV in ω), angular structure of S, SOC (Si split-off 44 meV), T > 0 absorption branch.

## 2. Gate decisions (limit ≤ 3 h wall, ≤ 12 GB per job; all multi-core jobs through code/run-heavy.sh)
| # | job (label) | estimate (basis) | decision | measured |
|---|---|---|---|---|
| 1 | ecut 30–60 × k 6³/8³ SCF scan (COMP-PAER-conv) | ≤ 1 min, < 0.1 GB (ENV benchmark ×(60/20)^{1.5}) | RUN | 8 SCFs, 1–4 s each, 8 MB |
| 2 | SCF 40 Ry + DFPT at one low-symmetry Q (0.137, 0.211, −0.083)2π/a (COMP-PAER-pilot) | ≈ 3–5 min (benchmark 3.5 min/8 q ×(40/20)^{1.5}×low symmetry) | RUN (pilot for the tier-H cost) | **8.0 min**, 0.25 GB (6 irreps, 1024 k+k+q) |
| 3 | DFPT 4³ (8 irr. q) + q2r + nscf 40³ (COMP-PAER-ph444-nscf40) | ≈ 20–40 min (pilot × 8 q × higher symmetry) | RUN | **12.7 min** (nscf 1.5 min), < 0.3 GB |
| 4 | nscf 40 k-points (Γ, q along 3 axes), 16 bands, wavefunctions (COMP-PAER-nscf-rho) | < 1 min | RUN | 11 s |
| 4b | nscf Γ + 2 q-points, 100 bands, f-sum convergence (COMP-PAER-fsum100) | < 1 min | RUN | 27 s |
| 5 | §M10 amplitude pipeline (own g from dvscf + bare/NL derivative; ≈ 100–400 Q, C6 8-atom frozen phonon) | ≈ 2–6 h total in ≤ 30-min jobs | **DROPPED at rescope** (not narrative-critical: replaced by (P.1) [E]) | — |
| 6 | Tier H Si (§8): DFPT 8³ at 60 Ry, 12³ k | ≈ 24 h (pilot × 29 q × (60/40)^{1.5} × (12/8)³) | **FORMULATED** (over limit; rescope) | — |
| 7 | Ge tier B/H (§9) | SOC + hybrid/GW gap: ≫ 3 h | **FORMULATED** | — |
matdyn (serial, 16 500 Q, 15 min) and all Python ran single-core outside the lock. Work dirs only in /root/work/COMP-PAER/.

## 3. Convergence [CALC] (code/COMP-PAER/out/conv_ecut_k.txt)
| ecut (Ry) | E_tot 8³ (Ry) | ΔE vs 60 (mRy/cell) | VBM 8³ (eV) | ΔVBM (meV) |
|---|---|---|---|---|
| 30 | −15.76462 | 1.21 | 6.2293 | 8.2 |
| 40 | −15.76548 | 0.35 | 6.2234 | 2.3 |
| 50 | −15.76574 | 0.08 | 6.2217 | 0.6 |
| 60 | −15.76582 | 0 | 6.2211 | 0 |
k: E_tot(6³) − E_tot(8³) = 1.5 mRy at 40 Ry; band energies at fixed k converge with k_SCF faster (charge density). **Chosen: 40 Ry, 8³** (eigenvalue
differences ≤ 2 meV, below the 15 meV directional-sampling resolution of E_min). Phonons at 40 Ry not re-checked at 60 Ry (≤ 1 % expected for SG15 Si;
tier H uses 60 Ry). Window numbers vs sampling: E_min grid 40³ (Δk ≈ 0.05 Å⁻¹) and 400 directions give E_min(|K_pk|) = 1.186 eV vs the exact 1.170 eV:
**m_χ^{ZP} biased high by ≈ 0.003 MeV → quote 0.405–0.408 MeV**. PAER edge: 300 directions, Δ|q| = 0.02 Å⁻¹, mass grid 10⁻⁵ MeV: ±0.0005 MeV.
Form factor: 16 bands; ρ uses only plane waves common to both k-sets (exact for NC pseudopotentials within one ecut).

## 4. Window (T5) [CALC; inputs §1; control C5]
| quantity | this return [CALC] | campaign value before | note |
|---|---|---|---|
| PBE indirect gap / scissor | 0.557 eV / +0.613 eV | — | E_g(0) = 1.170 eV |
| E_min(q) at \|q\| = 0.3, 0.5, 0.7, 0.9 Å⁻¹ (min over q̂ / median) | 2.18/2.25, 1.64/1.80, 1.33/1.71, 1.19/1.83 eV | parabolic | pointwise window ω ≤ E_min − δ₀ |
| ω_TA(Q*) minimised over q̂ at \|q\| = 0.4, 0.6, 0.8, 1.0 Å⁻¹ | 15.5, 11.5, 5.9, 2.8 meV | 13.5 meV at Q* ≈ 0.53 Å⁻¹ | 4³ DFPT |
| PAER edge, free pairs, m_χ^{PA} | **0.3374 MeV** | 0.337 [E] | WP3 §M9, WP6 IF6-10 |
| PAER edge, exciton replica | **0.3333 MeV** | 0.333 [E] | E_x^b = 14.7 meV [lit.] |
| first ZPL, forbidden class (G′ = 0), m_χ^{ZP} | **0.405–0.408 MeV** | 0.42 (0.40–0.44) [E13] | |
| allowed ZPL ((2̄00) class) | **0.547 MeV** | ≈ 0.54 [E13] | |
| other Umklapp classes | 0.562 MeV | — | |
**Restated Si window [CALC]:** (1) PAER-only: 0.333 (replica) / 0.337 (continuum) ≲ m_χ < 0.405–0.408 MeV; (2) PAER + forbidden-class ZPL:
0.408–0.547 MeV (PAER leads only near the lower end, WP3 §M9 (2); the ϖ_II ratio needs the §M10 amplitude, not recomputed); (3) allowed ZPL above
0.547 MeV. **Edge-shell share:** at m_χ = 0.40 (0.42, 0.46) MeV the reachable points with E_min − 0.3 eV < ω < E_min carry 15 % (25 %, 37 %) of the
PAER rate (δ₀ = 0 vs 0.3 eV in §6); below 0.38 MeV the whole reachable region is inside the strict window. Reached (q, ω): at 0.40 MeV
\|q\| ≈ 0.35–0.75 Å⁻¹ (0.7–1.5 keV, ≤ 0.4 αm_e: Bethe ridge irrelevant), median ω 1.29 eV, ω_max 1.40 eV; at 0.36 MeV median ω 1.225 eV.
Excitonic final states are included only through the measured ε₂ (rate) and the replica edge; the bound-exciton ZPL floor 0.329 MeV (WP6 (3.1′)) is
not a PAER threshold.

## 5. Rate (T5) [E]
dℛ/dω from (M.6)+(P.1). Total rate per σ̄_e (events kg⁻¹ yr⁻¹ cm⁻², heavy mediator, central 𝔉_ρ, strict window δ₀ = 0.3 eV): 1.2×10²⁵ (0.337 MeV),
9.7×10²⁸ (0.36), 4.3×10³¹ (0.40), 1.9×10³² (0.42), 5.6×10³³ (0.50) (`out/rate_out.txt`; ℛ ∝ σ̄_e). **Uncertainty (multiplicative, combined in log
quadrature, [E]):** 𝔉 proxy ×/÷3; finite-q screening beyond the measured q → 0 (local fields δ_LF, pair channel δ_pair, ε₁ model) ×/÷2 (the §M7 [0.4,
1.8] factor applied to the q-dependence only); data digitisation and T = 20 K → 0 ±25 %; TA/TO threshold shift with Q* and pocket k-dependence ×/÷1.5
at m_χ ≥ 0.36 MeV, up to ×/÷10 within 5 keV of the edge (the rate there scales as (m_χ − m_χ^{PA})^{p̄_on+k}, so any threshold error is exponentiated);
total **≈ ×/÷ 4 at 0.38–0.43 MeV, quoted as ×/÷10** (order of magnitude), **edge region 0.333–0.35 MeV: only the exponent is meaningful**.

## 6. Reach (T5) [E, ×/÷ 10]: σ̄_e^{95} (cm²), 1 kg·yr, 3 events, ≥ 1 e⁻, background-free
| m_χ (MeV) | heavy, strict window | heavy band (𝔉_ρ/3 … 3𝔉_ρ) | heavy, incl. edge shell | light, strict | light band |
|---|---|---|---|---|---|
| 0.334 | 6.6×10⁻²⁴ | 2.0×10⁻²³ … 2.2×10⁻²⁴ | same | 2.1×10⁻²⁶ | 6.3×10⁻²⁶ … 7.0×10⁻²⁷ |
| 0.337 | 2.5×10⁻²⁵ | 7.4×10⁻²⁵ … 8.2×10⁻²⁶ | same | 8.0×10⁻²⁸ | 2.4×10⁻²⁷ … 2.7×10⁻²⁸ |
| 0.340 | 3.2×10⁻²⁶ | 9.7×10⁻²⁶ … 1.1×10⁻²⁶ | same | 1.1×10⁻²⁸ | 3.3×10⁻²⁸ … 3.6×10⁻²⁹ |
| 0.350 | 6.4×10⁻²⁸ | 1.9×10⁻²⁷ … 2.1×10⁻²⁸ | same | 2.4×10⁻³⁰ | 7.1×10⁻³⁰ … 7.9×10⁻³¹ |
| 0.360 | 3.1×10⁻²⁹ | 9.2×10⁻²⁹ … 1.0×10⁻²⁹ | same | 1.3×10⁻³¹ | 3.8×10⁻³¹ … 4.2×10⁻³² |
| 0.380 | 6.2×10⁻³¹ | 1.8×10⁻³⁰ … 2.1×10⁻³¹ | 5.9×10⁻³¹ | 3.0×10⁻³³ | 9.1×10⁻³³ … 1.0×10⁻³³ |
| 0.400 | 7.0×10⁻³² | 2.1×10⁻³¹ … 2.3×10⁻³² | 6.0×10⁻³² | 3.9×10⁻³⁴ | 1.2×10⁻³³ … 1.3×10⁻³⁴ |
| 0.420* | 1.6×10⁻³² | 4.8×10⁻³² … 5.3×10⁻³³ | 1.2×10⁻³² | 1.0×10⁻³⁴ | 3.1×10⁻³⁴ … 3.4×10⁻³⁵ |
| 0.430* | 8.9×10⁻³³ | 2.7×10⁻³² … 3.0×10⁻³³ | 6.3×10⁻³³ | 6.2×10⁻³⁵ | 1.8×10⁻³⁴ … 2.1×10⁻³⁵ |
| 0.500* | 5.4×10⁻³⁴ | 1.6×10⁻³³ … 1.8×10⁻³⁴ | 3.2×10⁻³⁴ | 6.3×10⁻³⁶ | 1.9×10⁻³⁵ … 2.1×10⁻³⁶ |
| 0.600* | 5.9×10⁻³⁵ | 1.8×10⁻³⁴ … 2.0×10⁻³⁵ | 3.7×10⁻³⁵ | 1.4×10⁻³⁶ | 4.1×10⁻³⁶ … 4.6×10⁻³⁷ |
\* above m_χ^{ZP}: PAER-only reach of the sideband, not the experiment's reach (a zero-phonon channel is open; above 0.547 MeV it is allowed and
dominates by 10²–10³, C3). The ω integral is cut at 1.62 eV (ω_max = ½m_χv_max² = 1.76, 2.1 eV at 0.5, 0.6 MeV) and the α_abs extrapolation is checked only
to ≈ 1.5 eV, so the 0.46–0.60 MeV rows are rate lower bounds (σ̄_e upper bounds), and the 37 % edge-shell share at 0.46 MeV is computed with that cut. Light mediator: F_DM = (αm_e/q)², σ̄_e at q₀ = αm_e (CONVENTIONS §9), so F_DM² ≈ 50–800 at the reached q (0.7–1.4 keV); this is why light
< heavy here. (Full ω-spectra: `scripts/rate.py`, function `rate`.)

## 7. Controls (CONTROLS.md) for the numbers of this return
| control | status | evidence |
|---|---|---|
| C1 optical limit | **used as input, not tested**: (P.1) at q → 0 equals the measured ε₂ by construction | independent C1 test needs the §M10 amplitude (tier H stage 6) |
| C2 g → 0 | PASS by construction (ε₂^{PA,opt} → 0) | — |
| C3 first-order open | NOT TESTED numerically: the external anchor (1509.01598 Fig. 6, Si 1 e⁻, 1 kg·yr) is on disk only as text without the figure values; PAER/ZPL ≈ 10⁻²–10⁻³ above 0.547 MeV stays the WP3 [E] statement | WP3 §M9 (3) |
| C4 f-sum / completeness | **PARTIAL (cause of deficit not separated)**: Σ_{m≤N_m}(ε_m − ε_v)\|ρ_mv(Γ,q)\|² / (q²/2m_e) = 0.807/0.851/0.855/0.883 for N_m = 16/30/50/100 at 0.1 Å⁻¹ and 0.779/0.847/0.860/0.891 at 0.5 Å⁻¹ ([100]); with 16 bands 0.80–0.82 in all 3 directions to 0.6 Å⁻¹, 0.65–0.73 at 1.0 Å⁻¹. The sum still rises slowly at 100 bands: the deficit is band truncation plus, at most ≈ 0.1, the non-local-PP term (CONTROLS C4 note); 𝔉_ρ uses only the 4 lowest conduction bands and is unaffected | `out/ff.json`, `inputs/nscf_fs.in`; ELF bounds not tested |
| C5 kinematics | **PASS**: edge 0.3374 MeV from the threshold E_g + min ω_TA(Q*) (tilt correction ≤ 0.3 meV neglected); replica edge 0.3333 MeV from E_x + ω_TA; infimum E_g sits at \|q\| = \|K_pk\| where ω_TA(Q*) → 2.8 meV and the window is empty (E_min ≈ E_g) | `out/paedge.json`, `out/win.json` |
| C6 adiabatic equivalence | NOT RUN (dropped at rescope; spec §8) | — |
| C7 soft-acoustic | NOT RUN (spec §8) | — |
| C8 GaAs decoy | NOT RUN (spec §8) | — |
Window numbers pass C5; rate/reach numbers carry [E] (model-level, C1 used as calibration) and are **not** [CALC]; none is FAILED-CONTROL.
## 8. Tier H (T6): FORMULATED, not run (coordinator rescope 2026-11-01; RULES.md deliverable directive)
Layout: `code/COMP-PAER/tierH/{Si,Ge}/{scf,ph,nscf,epw}.in` in the qe-rtsc `rtsc/bench` layout (`@PSEUDO@`, outdir './', SG15 via
`rtsc/pseudo.sh`). Stages 1–4 (scf, ph incl. its collect step, nscf, epw) run unchanged with `rtsc/bench/run-fork.sh <dir> <bin> <work>`; stages 5
(`rho`) and 6 (`paer`) are new kernels, specified below (not yet written). Quantity computed: L^{PA}(q,ω) of (M.14) with M̃ of (M.13), then (M.6).
| stage | input | content | grid / parameter | convergence target |
|---|---|---|---|---|
| 1 scf | scf.in | PBE, SG15 Si 1.2 (Ge: `_FR-1.0`, SOC), a = 5.431 Å (Ge 5.658 Å) | ecut 60 Ry, k 12³ | ω(X) to 0.2 meV vs 80 Ry; E_tot 0.1 mRy |
| 2 ph | ph.in | DFPT, dvscf on the coarse grid; **dynamical quadrupoles** Q_κ,αβγ from a long-wave DFPT code (QE has none: ABINIT `lw_qdrpl` or literature) into `quadrupole.fmt` | q 8³ (29 irreducible) | g(Q*) at 3 off-grid Q vs direct ph.x ≤ 5 % |
| 3 nscf | nscf.in | full 12³ grid, no symmetry, 60 bands (Ge 120 spinors) | — | — |
| 4 epw | epw.in | Wannier (sp³ + d, 18 WFs; Ge 36), disentanglement window to +40 eV, `write_u_matrices`, Wannier-gauge g (`epmatwp`), IFCs; `asr_typ='crystal'` **keeping the O(Q) part of g** (ASR on the dynamical matrix only, never a zeroing of g at Q → 0) | k 12³ / q 8³ coarse | band interpolation ≤ 10 meV up to +10 eV; N_W test 18 → 26 |
| 5 rho | (new) | ρ_mn(k,q) on the coarse 12³ k grid for each target q (one nscf at k+q, unfolded), rotated with the **same U(k)** to F^W(R,q) (M.18) | q: \|q\| 0.25–1.25 Å⁻¹ step 0.05, 30 directions (C₄ᵥ wedge) | Wannier vs direct ρ at 5 off-grid k ≤ 2 % |
| 6 paer | (new) | (M.1) with all four paths and unrestricted m inside the Wannier manifold + **Sternheimer remainder** (rtsc/sth engine: (H − ε_{ck′})|∂ψ_c⟩ = −P_c^⊥∂V|ψ_c⟩ contracted with e^{iq·r}) for the Bethe-ridge part at \|q\| > 0.5 αm_e; ε̃^{-1}_{G0}(q,ω) RPA+LFE (yambo/BerkeleyGW or Route S supercell, X2 §8) and the pair term W^{scr}(P,ω_f)𝔗 at the pinned P ≈ 0.85X; pocket sums on fine grids; tetrahedra | fine k (Γ pocket) and k′ (6 Δ pockets) 60³→120³ equivalent, energy cut ω − E_g + 0.1 eV; σ → 0 | 5 % in L per (q,ω) bin; δ_pair, δ_LF reported separately |
Controls in stage 6 (CONTROLS): C1 run at |q| = 10⁻³ Å⁻¹ vs EPW `indabs` (same g) and vs Macfarlane 20 K α(ω); C2 by g → 0 flag; C4 completeness
Σ_m(ε_m − ε_v)|ρ_mv|² = q²/2m_e (+ non-local correction) as the N_W/Sternheimer test; C6 at Q = X (8-atom frozen cell, ±0.005 Å) vs (M.12);
C7a–e at |Q| = 10⁻²,10⁻³,10⁻⁴·2π/a in 3 directions; C8 GaAs with the same pipeline (lpolar, Fröhlich). Symmetry check: on-axis LA zero
(G′ = 0) and LO zero (2̄00) of §M3(d).
**Cost (from the measured pilot, this box: one low-symmetry Q, 40 Ry, 8³ k, 4 cores: 8.0 min wall, 0.25 GB).** Stage 2: 29 q ×
8 min × (60/40)^{1.5} × (12/8)³ ≈ 29 × 50 min ≈ 24 h on 4 CPU cores [E] (the GPU fork's batched Sternheimer is the intended speed-up);
stage 3: 1728 k × 60 bands, ≈ 1 h CPU; stage 4 (EPW coarse, 18 WFs): ≈ 2–4 h CPU; stage 5: one nscf per q (≈ 1800 q × 1728 k) ≈ 10⁵ k-point
diagonalisations ≈ 2–3 days CPU, the dominant cost (alternative: Wannier position-operator expansion valid only for q ≲ 0.5 αm_e);
stage 6: ~10¹⁰–10¹¹ flop per (q,ω) bin (WP3 §M10) × ~2×10³ bins ≈ 10¹⁴ flop + Sternheimer remainder (≈ 10³ solves per q) — hours on one
GPU. Memory: stage 2 < 2 GB; stage 5–6 ≤ 8 GB per q-batch. Disk ≈ 20 GB (dvscf 29 × 6 modes, epb). **Gate verdict: over the 3 h / 12 GB
box limit (stage 2 alone ≈ 24 h) → FORMULATED for the user's GPU pod.**

## 9. Ge: FORMULATED (not run)
Why not cheap: PBE closes the Ge gap (L₆ below Γ₇ at the PBE lattice), so a scissor on PBE bands is ill-defined; the L-valley masses and the
Γ₈⁺ hole need SOC (Δ_SO = 0.29 eV). Inputs: `code/COMP-PAER/tierH/Ge/{scf,ph,nscf,epw}.in` (Ge_ONCV_PBE_FR-1.0.upf, SOC, a = 5.658 Å, 60 Ry, k 12³,
q 8³, 120 spinor bands, 36 WFs). Quasiparticle energies: HSE06 nscf on the same grid or G₀W₀ corrections Wannier-interpolated (e–ph from PBE at the
HSE-corrected band order), target E_g(0) = 0.744 eV (L), E_dir = 0.89 eV. Window to compute exactly as §4 (classes: L valleys, C₃ᵥ, all branches
allowed, WP3 §M3 (d)); campaign [E] values to be replaced: PAER edge ≈ 0.213 MeV, allowed ZPL ≈ 0.32 MeV (0.32–0.36). Rate as §8 stage 6 (plus the
Γ-valley direct channel above ≈ 3 MeV only). Optical calibration for (P.1)-type estimates: Macfarlane et al. Ge indirect edge (not fetched). Cost:
SOC doubles the basis and ≈ ×4–8 the DFPT stage relative to Si: ≈ 4–8 days on 4 CPU cores [E]; one GPU node: hours. Gate: FORMULATED.

## Symbols introduced/used
| symbol | meaning | status |
|---|---|---|
| 𝔉_ρ(q) | finite-q form-factor proxy ⟨Σ_{v,c}\|ρ_cv(Γ,q)\|²/q²⟩ normalised to q → 0 (§1) | **new** |
| f_win(q,ω) | fraction of q̂ with ω ≤ E_min(q) − δ₀ | **new** |
| α_abs(ω), n(ω) | measured absorption coefficient, refractive index (α_abs to avoid the fine-structure α) | **new** |
| m_χ^{PA}, m_χ^{ZP} | PAER edge mass, first zero-phonon mass (WP3 §M9 usage) | used |
| E_min(q), δ₀, K_pk, Q*, ω_ν(Q), E_g, E_x, ρ_mn(k,q), g, M^{(2)}, L, S̄, ε₁, ε₂, η(v_min), v_max, σ̄_e, F_DM, ℓ_Q | as in NOTATION v4 / WP3-v3 / CONVENTIONS | used |

## Interface flags
- **IF-CP-1 (WP3 §M9, WP1 [E13], WP6 IF6-10, paper):** replace the Si window by the [CALC] values of §4: PAER-only 0.333 (replica) / 0.3374
  (continuum) – 0.405–0.408 MeV; forbidden ZPL from 0.405–0.408; allowed ZPL from 0.547 MeV. The 0.42 (0.40–0.44) and ≈ 0.54 MeV estimates are confirmed
  at their low end.
- **IF-CP-2 (paper narrative):** PAER is the only Si electron-recoil channel in a ≈ 0.07 MeV mass band; order-of-magnitude reach §6 (heavy
  ≈ 7×10⁻³² cm², light ≈ 4×10⁻³⁴ cm² at 0.40 MeV, 1 kg·yr, ×/÷10). Use as [E] only; never as [CALC].
- **IF-CP-3 (X2/§M7):** the dipole extrapolation of the optical ε₂ to q ≈ 0.3–0.9 Å⁻¹ overstates S̄ by ×10–40 (𝔉_ρ); any data-calibrated PAER
  estimate must carry a finite-q vertex form factor.
- **IF-CP-4 (CONTROLS C4):** with SG15 NC pseudopotentials the plane-wave f-sum Σ_m(ε_m − ε_v)|ρ_mv|² reaches only 0.81 (16 bands) → 0.89 (100
  bands) of q²/2m_e at 0.1–0.5 Å⁻¹, converging slowly; a C4 test of N_m must add the non-local commutator term and extrapolate in N_m.
- **IF-CP-5 (COMP-PH):** 4³ DFPT gives ω_TA(0.85X) ≥ ω_TA(X) by ≈ 1 meV (interpolation artefact); the TA edge masses need ≥ 6³ for 10⁻⁴ MeV accuracy.
- **IF-CP-6 (tier H owner):** specification §8 with inputs in code/COMP-PAER/tierH/ (rtsc/bench layout); stage 5–6 code (ρ in the Wannier gauge, PAER
  kernel, Sternheimer remainder) does not exist yet and is the critical path.

## Proposed LIMITS rows
| # | Owner | location | chain | status | note |
|---|---|---|---|---|---|
| L8-N1 | COMP-PAER | §4 | (M.9) window + WP1 [E13] reachability with ab initio E_min(q), ω_TA(Q) | CALC (C5 PASS) | Si 0.3333/0.3374–0.405(8) MeV PAER-only; 0.547 allowed ZPL |
| L8-N2 | COMP-PAER | §5–6, (P.1) | (M.14) ELF form, q → 0 data (L9) × 𝔉_ρ(q)/ε₁(q)² → (M.6) | ESTIMATED ×/÷10 | not [CALC]; replace by tier H stage 6 |
| L9-N1 | COMP-PAER | §7 C4 | plane-wave f-sum with NC PP | CALC (partial) | 0.81 (16 bands) → 0.89 (100 bands); NL vs truncation not separated |

Files: code/COMP-PAER/{inputs,scripts,out,tierH/{Si,Ge}}, env-additions.md; work dirs /root/work/COMP-PAER/ (not committed). Literature:
1202.3454 [FT] fetched into literature/papers-COMP-PAER/ (PDF deleted). Pseudopotential: Si_ONCV_PBE-1.2.upf (SG15, sha256 of tarball per ENV.md).
