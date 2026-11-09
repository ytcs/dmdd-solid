# REF-FBC-B: referee report on R19/FBC (full-band cascade, Si): numerical reproduction and code audit

Referee: isolated numerical/code referee (Claude). Scope: returns/R19/FBC.md, code/FBC/, caches in /root/work/FBC.
Nothing was edited except this file. New caches (n = 14 grid, NB = 8/12 tables) went to a scratch directory only.
CPU used: about 30 CPU-min (4 cores, single-threaded BLAS per process).

## 1. checks.py: 13/13. What each check actually tests

`python3 checks.py`: **REPRODUCED, 13/13 PASS** (14 s). How much each check tests:

| check | verdict | comment |
|---|---|---|
| C1 gap | meaningful (calibration) | gap 1.1600 eV for both calibrations |
| C1 symmetry | half trivial | E(Rk) = E(k) holds by construction, since grid energies are copied from the wedge. The part that tests something is \|Hc − ec\| = 9e-15 on rotated vectors, which checks the non-symmorphic phases |
| C2 completeness | **trivial** | sums \|ρ\|² over *all* 113 eigenvectors, which is unitarity of `eigh`. It cannot detect the 20-band truncation or a bad vertex. Tolerance 1e-10 |
| C3 f-sum / ε | **meaningful** | Im ε = (2πv/Ω)S_GG with spin 2. f-sum = 0.965–0.977, so the normalisation of S (1/(N·DBIN), cell volume, δ binning) is validated independently. This is the key check of the golden-rule prefactor |
| C4 S rotation | meaningful | rotated vs direct S, with non-symmorphic phases: 0.4 % |
| C5 brute force | meaningful | factorised Γ_D (ii.py) vs sampled golden rule (exch.py, separate vertex code): 0.99/1.02 |
| C6 exchange relabel | weak | Σ\|M_E\|² = Σ\|M_D\|² holds only in expectation (600 samples). The 25 % tolerance catches only gross momentum or Umklapp errors |
| C7 k-grid | meaningful, loose | shell-rate ratios 12³/10³ with a 1.6× tolerance. It understates the threshold sensitivity of P(N) (see §4) |
| C8 DOS | meaningful (basic) | 4.000 valence states/spin/cell; parabolic edge 1.00 |
| C9 MC vs book GF | **mislabelled** | it tests a *separate toy MC written inside checks.py* (`c9.mc`), not the production engine `mc.Model.run`. FBC.md §5 ("In book mode the MC reproduces casc18_3 …") claims more than the check shows. The production engine is protected only by the per-event energy identity (asserted in run_mc.py) and by the full/eo agreement |
| C10 seeds | meaningful | energy sum rule 1e-6 eV; q → 0 DM vertex = k·p optical vertex to 0.3 % |
| C11 MC | normalisation trivial | the "independent runs" (seed = 1 vs 2) **reuse the same 2×10⁴ seed draws**, so TV ≤ 0.013 measures cascade noise only, not seed-sampling noise. That is the right floor for the paired comparisons (full vs eo) but not for an absolute error |

## 2. Code audit

Every item below was read line by line, and the prefactors were re-derived by hand.

- **Band indexing**: valence 0..3, conduction `ce = 4..19`, consistently in ii.py, exch.py, mc.py and seeds.py.
  Kinetic energies: Ek_e = E − E_g and Ek_h = −E (VBM = 0). Electron step (n1,k) → (n1′, k−p) and hole step
  k → k+p (`sgn`) match `kX = k1 − p` and `kY = k1 + p` in ii.py. The pair (v,k2) → (c,k2+p) conserves crystal
  momentum, and wedge rotations use `perm[op_from_irr]` consistently for the carrier and the pair tables.
  **REPRODUCED (no bug).**
- **Spin and DOS factors**: Γ_D = (4π/ħΩ²)N⁻¹Σ_p A S A†, where 4π = 2π × 2 (pair spin). I re-derived it from
  \|M\|² = \|Σ_G w ρρ\|²/(NΩ)² with N² (k2, p) terms; units w² [eV²Å⁶]/Ω² × δ/ħ → s⁻¹. The phonon rates
  W_j = (Z_j/6)πD²g_t/(ρω), with g_t per spin over all 6 valleys, equal JR's Z_f πD²N_1valley/(ρω) (JR's N has no
  spin factor). Units check, and ħ cancels. Acoustic W_ac = Ξ²q_c³/(12πρuħv) and mean loss ¾ħuq_c both re-derived.
  **REPRODUCED (no bug).**
- **Golden-rule normalisation**: correct. It is anchored by C3 (f-sum on the same S) and C5. e² = 14.40 eV Å,
  Ω = a³/4. **REPRODUCED.**
- **Exchange sign and factor**: I re-derived the spin sum, with ½ for identical final electrons in the same-spin
  channel: Σ_ord[1.5\|D\|² + 0.5\|E\|² − Re DE*]. This equals the coded Σ_ord[\|D\|² + \|E\|² − Re DE*] because
  Σ\|E\|² = Σ\|D\|² for each initial state. The sign of the interference is correct (fermions). The contact limit
  gives R_x = ½. The exchange momenta are p_x = k1 − k2 − p (electrons) and k2 − k1 (holes), each with the
  correct ±G pairing. **REPRODUCED.**
  Two minor points: R_x is noisy below 2.6 eV and is extrapolated flat at 1.12 for electrons, which is allowed
  (R_x ≤ 1.5); this is covered by the rxthr variant. R_x is not recomputed for the screening variants.
- **Energy and momentum in the II and phonon steps**: momentum is conserved on the grid (Umklapp is explicit).
  Energy is exact by construction: the three product energies are rescaled to E − E_g, and the phonon loss is
  subtracted exactly. The residual mismatch between grid energies and the rescaled ones is O(DW + DWP + σ) ≈ 0.1–0.2 eV,
  which is a model approximation, not a bug. I confirmed ω = N E_g + E_ph + E_res to < 1e-9 eV in every one of my
  runs. **REPRODUCED.**
- **Termination**: every carrier is followed until E < E_g; then no further pair is possible, and E is booked as
  residual kinetic energy, which thermalises later. Electrons are tabulated up to 19.5 eV; above that, the
  high-energy rule ionises with probability 1. A run that hit `maxsteps` would violate the asserted energy
  identity, so it cannot pass silently. **Correct.** Caveat: ε_eh and F_eh (50 → 100 eV) are obtained largely in
  the high-energy-rule regime (no matrix elements and no phonons above 19.5 eV). Only the DOS choice is varied
  (hefree: −0.03 eV).
- **Seed sampling**: the q weights `DQ/n_b · q · η(v_min)` are a correct Monte Carlo estimate of ∫d³q η/q F² S
  for isotropic S; light mediator F² = (q₀/q)⁴; photon |p|²/ΔE²; energies rescaled to ω − E_g. Three minor
  inaccuracies, each negligible (< 0.01 in TV at a 0.1 eV smearing):
  - (a) `sample_records` draws within a q sample with |ρ|²·gauss and leaves out the variation of η(v_min) across
    the ±0.1 eV window;
  - (b) the per-q multinomial uses floor-binned spectra read at `round(ω/DBIN)`, a +0.025 eV offset;
  - (c) the analysis histograms carry the same offset.
- **Variant consistency (minor)**: for scr = 1–3 only the total rate changes. The final-state CDF (`tab_e`/`tab_h`)
  and the pair-choice weights (`pw`) are always the "cap" ones. This should be stated as part of the variant
  definition.

**No bug found that changes a headline number.**

## 3. Independent reproduction

I re-ran from the caches, with new RNG seeds (my driver uses mc.Model), and recomputed from the data files.

| quantity | return | referee | verdict |
|---|---|---|---|
| ε_eh (50 → 100 eV, one-sided) | 4.130 ± 0.003 | 4.1205 ± 0.0034 (n12 full, seed 77, 4×10⁴/ω); eo n12 4.115 ± 0.005; repo reruns 4.124, 4.126, 4.126 | REPRODUCED (Δ = −0.010 = 2.0σ; the primary run is the high member of 5) |
| F_eh | 0.114 ± 0.002 | 0.1123 ± 0.0018 (bootstrap); eo 0.1114 ± 0.0024 | REPRODUCED |
| P(N ≥ 2), 5 eV, DM heavy | 0.111 ± 0.002 | 0.1080 ± 0.0010 (10⁵ cascades; same 2×10⁴ seeds); file values 0.1106 / 0.1093 | REPRODUCED (1.1σ) |
| TV(full heavy, book casc18_3 DM), 5 / 6 / 10 eV | 0.059 / 0.059 / 0.200 | 0.0587 / 0.0586 / 0.1996 (recomputed with casc18_3.Casc) | REPRODUCED |
| book P(≥2) at 5 eV | 0.169 | 0.1693 | REPRODUCED |
| photon (28³) vs DM, 10 eV | 0.078 | 0.0799 (fresh MC, 4×10⁴ each) | REPRODUCED numerically; **error bar understated**, see below |

**MC error bars.** The binomial σ for P(≥2) is 0.0022 at 2×10⁴, as quoted. For ε and F, a bootstrap (400
resamples) gives 0.0034 and 0.0018; the Gaussian formulas in run_mc.py give 0.0034 and 0.0018. **Correct.** The
spread of five nominally equivalent ε runs (4.115–4.130) is about 0.005, so it is consistent.

**Photon vs DM at 10 eV: DISCREPANT in the error bar.**
- In the same full-band cascade, TV(photon 28³, DM heavy) = 0.080, but TV(photon 12³, DM heavy) = 0.018.
  TV(photon 28³, photon 12³) = 0.062. In the energy-only cascade with the same splits these are 0.053, 0.021
  and 0.070.
- So the 12³ → 28³ change of the photon seed alone is ≈ 0.06. The DM seed exists only on 12³: its k2 sums are on
  12³, smoothed by the q average, but never tested at a finer grid.
- The quoted "0.078 ± 0.013 (+ ≤ 0.02 seed grid)" therefore understates the seed-grid uncertainty. The defensible
  statement is that the photon/DM difference at 10 eV is ≲ 0.08 and that its seed-grid uncertainty is of the same
  order (≈ 0.06).
- IF-FBC-5 ("the book's ≤ 0.062 is exceeded") is **not established**. The P(≥2) ratio of 0.99 at 5 eV is
  reproduced (0.109/0.111).

## 4. Convergence (referee runs)

For n = 8 and 10 I used the cached n = 8 and n = 10 ii tables. For n = 14 I ran ii.py 14 myself (14 CPU-min).
Cascades use energy-only (eo) mode with the n12 seed energies. eo differs from full by ≤ 0.003 at 5 eV in my
runs, so the eo mode isolates the kernels. Each entry is 4×10⁴ events.

| grid | P(≥2) 4.5 eV | P(≥2) 5 eV | ε_eh (eV) | F_eh |
|---|---|---|---|---|
| 8³ | 0.0547 ± 0.0011 | 0.1286 ± 0.0017 | 4.024 ± 0.005 | 0.116 ± 0.003 |
| 10³ | 0.0472 ± 0.0011 | 0.1167 ± 0.0016 | 4.107 ± 0.005 | 0.115 ± 0.003 |
| 12³ (return's grid) | 0.0413 ± 0.0010 | 0.1053 ± 0.0015 | 4.115 ± 0.005 | 0.111 ± 0.002 |
| 14³ (new) | 0.0448 ± 0.0010 | 0.1094 ± 0.0016 | 4.118 ± 0.005 | 0.113 ± 0.002 |

- **ε_eh and F_eh are converged in k** at 12³ (12 → 14: +0.003 eV, ΔF = 0.002, both within MC error).
  **REPRODUCED.**
- **P(≥2) near threshold is grid-sensitive.**
  - It falls by about 10 % per step from 8³ to 12³, then rises 4 % at 5 eV and 8 % at 4.5 eV from 12³ to 14³
    (about 2σ).
  - The rates of C7 (DOS-weighted mean 0.027) hide this: the threshold region depends on a few states near the
    band edges.
  - A grid uncertainty of ≈ ±0.005 at 5 eV and ≈ ±0.004 (±9 %) at 4.5 eV should enter the §7 budget. It exceeds
    the quoted MC ±0.002, but it is well inside the stated physics band [0.056, 0.155].
  - The step overcount at 14³ is 1/0.109 = 9.1, against 9.0. **DISCREPANT (minor): an error budget item is
    missing.** The headline value stands.
- **Number of bands** (8³ grid, eo, 5 eV). NB = 8: 0.1282 ± 0.0017. NB = 12: 0.1287 ± 0.0017. NB = 20:
  0.1286 ± 0.0017. Likewise at 4.5 eV (0.0571, 0.0565, 0.0547). The near-threshold result does not depend on
  bands above the 4th conduction band. **Converged.** The completeness of 20 bands up to 19.5 eV (the band-20
  minimum is 21.8 eV) matters only for ε; it is plausible but untested by C2.
- **MC sample size.** 2×10⁴ → 10⁵ events moves P(≥2, 5 eV) from 0.1106 to 0.1080, within 1.1σ. ε moves within
  2σ. **Adequate.**
- **G shells** (C7, 8 vs 11 at n = 8, ≤ 4 %): I accept it and did not repeat it.

## 5. IF-FBC-8: casc18_3.py above about 60 eV

**REPRODUCED.** The mechanism is more specific than the flag states. One-sided seeds; slopes are (Δω/Δ⟨N⟩, ΔVar/Δ⟨N⟩).

| setting | ⟨N⟩, Var at 100 eV | ε, F over 50 → 100 eV | ε, F over 20 → 40 E_g |
|---|---|---|---|
| NZ = 32, X = 90 (grid to 104 eV) | 26.854, 6.531 | **3.7958, 0.3816** (as the flag says) | 3.7495, 0.1142 |
| NZ = 64 or 96, X = 90 | 27.017, 3.028 | 3.7494, 0.1142 | 3.7495, 0.1142 |
| NZ = 32, X = 46 (casc18_3's large grid, 53.4 eV) | 27.017, **−144** | nonsense | 3.7495, 0.1142 |

There are two separate failures:
1. **Domain overrun.** `Casc.Gat` clips the cell index at K−2 but does not clip the interpolation weight f. Above
   X·E_g (25.5 eV for the default X = 22, 53.4 eV for X = 46) it therefore *extrapolates linearly* and gives no
   warning. With X = 46 and NZ = 64, the variance is 1.641 instead of 1.658 at 55 eV and −0.33 instead of 1.81 at
   60 eV. This is the "wrong above ~60 eV" seen with the script's own X = 46 grid.
2. **Root-of-unity aliasing.** With NZ = 32, the mass at N ≥ 32 folds onto N mod 32. This is negligible to 80 eV
   (ΔVar 8e-8), 0.005 at 90 eV, and +3.5 at 100 eV: P(N ≤ 2) = 5.1e-3 is the aliased tail at ⟨N⟩ = 27.

The book's uses (pair seeds ≤ 21 eV; one-sided slopes 20–40 E_g ≤ 46.4 eV with X = 46) are safe, as are FBC's
matched.py calibration (20–40 E_g with X = 46) and C9. **Fix**:
- in `Gat`, assert or clip `xx ≤ (K−1)h`, not only the index;
- choose NZ ≥ ⟨N⟩ + 10σ_N, or check that the reconstructed P(N) puts negligible mass in its last and first bins;
- rewrite IF-FBC-8 as: "domain X·E_g (silent extrapolation) and, separately, NZ = 32 aliasing above about
  85 eV".

## 6. Corrections requested

1. **C9 relabel.** Either test `mc.Model.run` itself, for example with tables replaced by the book's p_ii and a
   DOS split, or change FBC.md §5 to "a reference MC in checks.py reproduces …". The production engine has no
   benchmark against the generating function.
2. **C2** should be described as a unitarity sanity check. It does not test the band truncation.
3. **Add a k-grid term to §7** for P(N ≥ 2) at 4.5–5 eV (≈ ±5–9 %, from the 12³ vs 14³ runs above). Change
   "MC ±0.002" to "MC ±0.002, grid ±0.005".
4. **Photon vs DM (IF-FBC-5, Result 6).** The 0.078 compares a 28³ photon split with a 12³ DM split. The 12³ → 28³
   change of the photon split alone is 0.062 in TV. Either compute the DM seed on a finer k2 grid, or quote
   "≤ 0.08, not resolved from seed-grid error (≈ 0.06)". Withdraw the claim that the book's ≤ 0.062 is exceeded.
5. **C11 / §7 "MC" column.** State that the repetitions share the seed sample, so the 0.013 is the cascade-noise
   floor for paired comparisons (adequate for the memory bound IF-FBC-2), not an absolute error.
6. **IF-FBC-8**: correct the mechanism as in §5.
7. **Minor.**
   - Screening variants reuse the cap final-state and pair-choice weights.
   - Seed sampling leaves out η(v_min) inside the ±0.1 eV window and has a 0.025 eV binning offset.
   - R_x below 2.6 eV is a flat extrapolation of one noisy bin.
   - The high-energy rule controls most of the 50 → 100 eV ε slope.

   These should be stated; none changes a number beyond its band.

## Overall verdict

**ACCEPT WITH CORRECTIONS.**
- The normalisation, spin, exchange, momentum and energy bookkeeping of the code are correct as far as I can
  check.
- The headline numbers are reproduced within MC error: ε_eh = 4.12–4.13 eV, F_eh = 0.112–0.114,
  P(N ≥ 2, 5 eV) = 0.108–0.111, the book-cascade distances, and the casc18_3 numerical flag.
- The return's convergence claims are adequate for ε and F, under-budgeted for near-threshold P(N), and not
  established for the photon-vs-DM excess.
