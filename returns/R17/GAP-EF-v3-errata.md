# R17 / FIX-GAP-EF-GRID: GAP-EF-v3 errata — GAP-EF-v2 rerun on the grid-commensurate cascade solver

Agent FIX-GAP-EF-GRID, brief briefs/R17/FIX-GAP-EF-GRID.md. This is an **addendum**. Read it with returns/R16/GAP-EF-v2.md and
returns/R16/GAP-EF-v2-errata.md; neither is edited. It answers returns/R17/WP8-errata.md §5 (RC3, interface IF-EW-1: "rerun GAP-EF-v2 on
commensurate grids"). **For the merger:** where §5 or §6 below gives replacement text, use it in place of the GAP-EF-v2 / GAP-EF-v2-errata
original. Every passage not listed is unchanged.

Inputs read: briefs/R17/FIX-GAP-EF-GRID.md; returns/R17/WP8-errata.md §0, §5; code/CW7/cascade_gf.py (the reference guard); code/GAP-EF-v2/
(all files, data/results.json, data/scan.json); code/GAP-EF/cascade.py (diff against v2); returns/R16/GAP-EF-v2.md and GAP-EF-v2-errata.md
(every passage that prints a model number); RULES.md; CONVENTIONS.md; symbols as in GAP-EF-v2 (NOTATION.md not re-read). **No literature was fetched.**

**Deliverables.** This file and **code/GAP-EF-v3/** (a copy of code/GAP-EF-v2/, fixed): `cascade.py` (strict commensurability guard),
`model.py` (commensurate grids, interpolation in w_ph to the true ω₀), `predict.py` → `data/results.json`, `scan.py` → `data/scan.json`,
`mc.py` → `data/mc.json` (new: independent Monte Carlo), `compare.py` → `data/delta_v2_v3.json` (new: every v2 → v3 change), and `checks.py`:
**41/41 PASS in ≈ 3 min** (the 32 GAP-EF-v2 checks, with C3/C4a/C4b, C13, C15, C20 and C25 edited, plus GAP-EF-v3-C1…C7, C2b and C4b). code/GAP-EF/ and code/GAP-EF-v2/ are untouched.
Nothing committed.
**Numerics** (all light, deterministic except mc.py): predict.py 314 s on 4 workers; scan.py 24 s; mc.py 152 s (10⁶ histories per point,
11 points); checks.py ≈ 3 min; compare.py < 1 s. No first-principles numerics.
**Status.** Solver CROSS-CHECKED against an independent Monte Carlo at the true ω₀ (GAP-EF-v3-C4, C4b). Material numbers [E], as in v2.

---
## 0. Verdict

| # | Item | Result | § |
|---|---|---|---|
| 1 | What v2 actually did | v2 never ran at h = 0.02. model.grid already chose N ≥ 60 with \|w_eff/w_ph − 1\| < 1%, so the WP8-errata §5 figure "+1.3% in ε_eh (Si, h = 0.02)" **never applied** to GAP-EF-v2. The real v2 offsets: ω₀ by −0.83% … +0.73% (Si −0.13%); and, a second defect not in the brief, θ_ii = 3/2 (variant V1) ran at θ_eff = 3/2 − 1/(2N) on odd N (Ge, C, 4H-, 6H-SiC, GaN: θ_eff 1.4925–1.5065; and 13 prediction rows) | §1 |
| 2 | Fix | cascade.py refuses any (h, w_ph, θ_ii) with h ∤ E_g, θ_iiE_g or ω₀ (ValueError, CW7 rule); model.run solves only on commensurate nodes w_k = k/N and Lagrange-interpolates every output to the true w_ph (same h, error ≤ 3 × 10⁻⁵); θ_ii = 3/2 runs on even N | §1 |
| 3 | Size of the change | **Every ε_eh changes by ≤ 0.06% (V0), ≤ 0.19% (V1, the θ fix), every F_eh by ≤ 0.13%; predictions ≤ 0.13% (PbTe) in ε, ≤ 0.04% in F; residuals ≤ 0.07 points.** Not ≈ 1%: the elasticity ∂ln ε/∂ln w_ph ≈ 0.11 (Si) times offsets < 1% | §3 |
| 4 | Si F = 0.114 and 2.6σ | **Unchanged**: F_Si 0.11384 → 0.11384 (+0.002%), 2.580σ → 2.579σ. 𝒜_ph 5.595 → **5.588 eV³** (−0.12%) | §4 |
| 5 | Validation rms | **Unchanged** at 12.3% (12.335% → 12.334%); mean +8.2%; range −6.5% … **+24.7%** (GaN 24.63% → 24.66% crosses the rounding edge) | §4 |
| 6 | Closed form | (EF9) 1.613 + **2.329**(λ_ph w_ph^{**0.965**})^{0.2395}, max 0.52%; (EF10) last digit of every coefficient moves; residual budgets unchanged | §4 |
| 7 | Predictions table | 18 of 27 rows change in a printed digit (≤ 0.01 eV in ε_eh, ≤ 0.02 eV in a band edge, one F digit: ZnS 0.088 → 0.087); no ranking or band reading changes | §4, R3-7 |
| 8 | Statement that **does** change | (EF11) check: v2's "solver FD dε/dE_g = 1.777, (EF11) 4.6% low" was itself an ω₀-grid artefact (E_g ± 0.01 eV moved w_eff by +0.37% / +0.73%). At the true ω₀ the FD is **1.699** and (EF11) (1.694) is **0.3% low** | §4 |
| 9 | Verification | Independent MC (continuous energies, true ω₀, 10⁶ histories per point) = solver continuum limit for Si, Ge, C, max \|z\| = 1.5 (moments) and 0.7 (ε_eh, F_eh on the fit window) | §2 |
| 10 | Found in verification | With phonons the quadrature is **O(h^{3/2})**, not O(h) (λ_ph = 0 rows: O(h), table1 stands): the error at the production grid is 1.55× the N-vs-2N difference that v2 quotes — Si ε +0.064%, F −0.071%; C ε +0.19%. Larger than the commensurability effect; inside every quoted band | §2, R3-1 |

---
## 1. The defect and the fix

**Mechanism (as in CW7, WP8-errata §5).** The recursion (EF3)–(EF4) reads m_t, ρ_t and p_t at x − E_g and x − ω₀ and starts ii at x = θ_iiE_g.
On a grid h = 1/N (units E_g) with w_phN or θ_iiN not an integer, cascade.py set n_w = round(w_phN), n_th = round(θ_iiN), i.e. it solved the
problem at w_eff = n_w h and θ_eff = n_th h and reported it as the value at (w_ph, θ_ii).

**What v2 did, row by row** (code/GAP-EF-v2/data/results.json):
- ω₀: model.grid took the smallest N ≥ 60 with |n_w/N − w_ph|/w_ph < 1%. Offsets: Si −0.13%, Ge −0.10%, C +0.17%, 4H-SiC +0.62%, 6H-SiC
  +0.67%, 3C-SiC −0.83%, GaN +0.22%, SiO₂ −0.41%, β-Ga₂O₃ +0.68%, Al₂O₃ +0.73%, CaWO₄ +0.12%; the predictions likewise, all < 1%.
- θ_ii = 3/2 (V1): Python's round is half-to-even, so on odd N, θ_eff = (3N ∓ 1)/(2N): Ge (N = 79) 1.4937, C (67) 1.4925, 4H-SiC (81) 1.5062,
  6H-SiC (75) 1.4933, GaN (77) 1.5065. v2's grid() did not know θ_ii. Predictions on odd N in V1: GaAs, LiF, NaF, GaN, AlN, InSb, GaSb, CaF₂,
  MgF₂, PbS, C, 4H-SiC, Ge (13 rows).
- The exact-commensurate alternative is not affordable: w_ph = ω₀/E_g from decimal inputs has denominators 290 … 124 000 (Si 21/388, C 163/5470,
  MgF₂ 737/124 000).

**Fix (code/GAP-EF-v3/).**
- `cascade.check_grid(h, w, θ)` is called by `Cascade.__init__`: h must divide 1, every θ_t and w_ph (to 10⁻⁹), w_ph ≥ h, θ_t ≥ 1; otherwise
  ValueError. w_ph is not checked when phonon=False (ω₀ never enters; the λ_ph → 0 rows of §1.6).
- `model.grid(w, θ)` is v2's search restricted to N with Nθ_ii integral. For θ_ii = 1 it returns v2's N exactly, so the discretisation level of
  every V0/V3 row is v2's; V1 moves to the first even N inside the 1% window (Ge 79 → 98, C 67 → 100, 4H-SiC 81 → 82, 6H-SiC 75 → 76,
  GaN 77 → 116).
- `model.run` solves on that one grid at the commensurate nodes k/N, k ∈ {n_w − 1, n_w, n_w + 1} ({1, 2, 3} when n_w = 1; one solve if w_phN is
  an integer), and Lagrange-interpolates ε, F, b and every decomposition column to the true w_ph. The offset δ = w_phN − n_w is ≤ 0.01n_w, and
  the nodes share h, so no discretisation is mixed in. Interpolation error: 3 vs 5 nodes ≤ 2.6 × 10⁻⁵, 3 vs 2 nodes ≤ 9.6 × 10⁻⁵
  (GAP-EF-v3-C3: Si, Ge V1, C, 3C-SiC (largest δ), CsI (n_w = 1)).
- predict.py: same inputs, variants, statistics and band rules; parallel over rows. table1 (λ_ph = 0 rows) is copied from v2: ω₀ does not enter
  and h = 0.01, 0.005 divide 1 and 3/2 (GAP-EF-v3-C1). scan.py rerun (v2's scan.json was still the v1 output; w_ph = 0.035, 0.075 sat 0.84%, 0.50%
  off-grid).
- Not changed: the W_v support edge (ρ_h = 0 above W_v/E_g, quantised to h). It is a support cutoff, not a shifted read, and is one O(h) quadrature
  term like any other; the MC (which uses the exact W_v) agrees (C4, C4b).
- code/GAP-EF/cascade.py (v1) has the same defect; it is superseded and not touched.

## 2. Verification

**Independent Monte Carlo (mc.py, GAP-EF-v3-C4, C4b).** Event-by-event cascade in continuous energy at the true ω₀ and the v3 𝒜_ph (V0): ii with
p_t = 1/(1 + λ_ph ρ_t(x − w_ph)/𝔓_t(x − 1)), 𝔓 in closed form (with the hole cutoff for Si), products Dirichlet(3/2, 3/2, 3/2) with rejection of
holes above W_v; no grid and no code shared with cascade.py. 10⁶ histories per point, one electron seed.

| | x₀ = 20E_g: ⟨N⟩ MC | solver, h → 0 | ε_eh MC (eV) [window] | v3 reported ε_eh | F_eh MC | v3 reported F_eh |
|---|---|---|---|---|---|---|
| Si (B_h 12 eV) | 5.8698 ± 0.0009 | 5.8690 | 3.7467 ± 0.0009 [20, 40] | 3.7490 | 0.1139 ± 0.0004 | 0.1138 |
| Ge | 4.8591 ± 0.0008 | 4.8591 | 2.7924 ± 0.0006 [30, 60] | 2.7938 | 0.1245 ± 0.0004 | 0.1247 |
| C | 9.3769 ± 0.0009 | 9.3781 | 11.353 ± 0.002 [12.5, 25] | 11.372 | 0.0878 ± 0.0003 | 0.0875 |

- Means and variances at x₀ = 10, 20 and the [10, 20] secants: all |z| < 1.5 against the solver's h → 0 value at the true ω₀ (C4).
- ε_eh, F_eh from the secant over the production fit window [X/2, X]: |z| ≤ 0.7 against the solver continuum on the same window; the reported
  (production-grid) values differ from MC by their discretisation error only (C4b).
- The MC precision (≈ 1.5 × 10⁻⁴ in ⟨N⟩) is of the size of the ω₀ shift itself (1.5 × 10⁻⁴ in ε, Si), so the MC confirms the v3 solver at the
  true ω₀; it does not by itself resolve v2 from v3. The shift is resolved deterministically (same grid, §3).

**Order of the scheme (GAP-EF-v3-C2).** On commensurate grids the h-sequence is monotone (as CW7 found), and the observed order is
**p = 1.49–1.50** for ε, F and the pointwise moments (asymptotic ε, F: Si N = 74/148/296, C 67/134/268; pointwise moments also Ge 79/158/316). The error at the production grid is
therefore (f_N − f_2N)·2^{3/2}/(2^{3/2} − 1) = 1.55 × the doubling difference: Si ε +0.064%, F −0.071%; C ε +0.19%, F −0.087% (v2 quotes the
doubling differences 0.04–0.05% and 0.12% as the discretisation). For Si the bias is absorbed into 𝒜_ph by the calibration (the continuum value at
𝒜_ph = 5.588 eV³ is ε = 3.7466 eV, MC 3.7467 ± 0.0009). Linear Richardson (assuming O(h)) is not the right extrapolation for these rows.
Without phonons (λ_ph = 0, the table1 rows of §1.6) the observed order is 1 (p = 0.97–1.01 on h = 0.01/0.005/0.0025), so v2's linear Richardson
there stands and c₀ = 1.5853, 2.0562 agree with the three-level extrapolation to < 10⁻⁴ (GAP-EF-v3-C2b): the h^{3/2} term enters with the
phonon step. This is why table1 is copied unchanged.

## 3. Changes of every ε_eh, F_eh and validation residual (compare.py, data/delta_v2_v3.json)

**Calibration (Si, 3.749 eV).** 𝒜_ph: V0 5.5947 → 5.5878 eV³ (−0.124%), V1 5.5249 → 5.5179, V3 0.6877 → 0.6868 eV³. F_Si: V0 0.113840 → 0.113843,
V1 0.113041 → 0.113043, V3 0.102273 → 0.102274 (all +0.002%). Decomposition (𝒱_<, 𝒱_>, 2𝒞_<>, F^{ren}, r̄_c) unchanged at 10⁻⁴ (one printed digit:
Si V1 𝒱_> 0.1776 → 0.1777).

**Validation rows** (ε_eh v2 → v3 in eV; Δε/ε; ΔF/F; residual meas/model − 1):

| Row | V0 | V1 (θ_ii = 3/2) | V3 (a_DOS = 1) | ΔF/F (V0 / V1 / V3) | residual |
|---|---|---|---|---|---|
| Ge | 2.7939 → 2.7938 (−0.003%) | 2.7904 → 2.7901 (−0.013%) | 2.6874 → 2.6873 (−0.003%) | −0.000 / −0.003 / +0.000% | +5.95% → +5.95% |
| C | 11.3740 → 11.3722 (−0.016%) | 11.8093 → 11.8318 (**+0.190%**) | 12.2355 → 12.2337 (−0.015%) | −0.009 / −0.063 / −0.006% | +13.86% → +13.87% |
| 4H-SiC | 7.5655 → 7.5615 (−0.052%) | 7.6830 → 7.6744 (−0.112%) | 8.0480 → 8.0444 (−0.045%) | −0.036 / +0.039 / −0.023% | +3.50% → +3.55% |
| 6H-SiC | 7.1684 → 7.1642 (−0.058%) | 7.2504 → 7.2511 (+0.010%) | 7.6006 → 7.5969 (−0.049%) | −0.041 / −0.128 / −0.026% | −6.53% → −6.48% |
| 3C-SiC | 6.1150 → 6.1187 (+0.059%) | 6.1516 → 6.1550 (+0.056%) | 6.4044 → 6.4074 (+0.048%) | +0.048 / +0.052 / +0.031% | +12.84% → +12.77% |
| GaN | 7.6950 → 7.6932 (−0.023%) | 7.8427 → 7.8480 (+0.068%) | 8.2223 → 8.2207 (−0.020%) | −0.014 / −0.110 / −0.009% | +24.63% → +24.66% |
| SiO₂ | 17.4072 → 17.4085 (+0.008%) | 19.0510 → 19.0515 (+0.002%) | 18.7610 → 18.7624 (+0.008%) | +0.004 / +0.001 / +0.003% | +3.41% → +3.40% |
| β-Ga₂O₃ (ext.) | 9.9913 → 9.9869 (−0.044%) | 10.3960 → 10.3932 (−0.027%) | 10.7560 → 10.7517 (−0.041%) | −0.024 / −0.020 / −0.015% | +56.14% → +56.20% |
| Al₂O₃ (EF-LIT) | 16.5424 → 16.5382 (−0.025%) | 18.2108 → 18.2097 (−0.006%) | 17.8405 → 17.8359 (−0.026%) | −0.011 / −0.003 / −0.007% | +63.22% → +63.26% |
| CaWO₄ (EF-LIT) | 10.6875 → 10.6861 (−0.012%) | 11.1742 → 11.1734 (−0.007%) | 11.5148 → 11.5135 (−0.012%) | −0.006 / −0.005 / −0.004% | +178.83% → +178.87% |
| GaAs (UNVER.) | 3.9464 → 3.9440 (−0.060%) | — | — | −0.040% | (+6.4% → +6.5%, excluded) |

The largest change, C V1 +0.19%, is the θ fix (+0.165%: θ_eff 1.4925 → 3/2, at v2's grid level) plus the finer even grid (+0.025%, N 67 → 100)
(GAP-EF-v3-C5). V0 changes are the ω₀
correction alone; their sign follows the sign of the v2 offset (ε rises with w_ph at fixed 𝒜_ph) combined with the −0.12% in 𝒜_ph.

**Statistics.** Primary: range [−6.534%, +24.627%] → [−6.480%, +24.655%], mean +8.233% → +8.245%, rms 12.335% → 12.334%. No-GaN: mean +5.501% →
+5.510%, rms 8.743% → 8.728%, max +13.86% → +13.87%. Extended: mean +14.22% → +14.24%, rms 22.96% → 22.98%, max +56.14% → +56.20%. All: rms 63.40% →
63.42%, max +178.83% → +178.87%. GaN at 8.9 eV: +15.66% → +15.69%. F_Si residual +4.53% (unchanged); ∂F/∂𝒜_ph 0.001377 → 0.001378 eV⁻³.

**Predictions** (V0 central value; bands from the v3 variants and the v3 validation range): ε_eh changes −0.127% (PbTe) … +0.092% (PbSe), median
−0.02%; F_eh −0.040% (GaAs) … +0.026% (PbS); band edges ≤ 0.12%. Per row (Δε/ε, ΔF/F): GaAs −0.060, −0.040; Al₂O₃ −0.025, −0.011; TeO₂ −0.027, −0.015;
CaWO₄ −0.012, −0.006; LiF −0.013, −0.003; NaF −0.016, −0.004; GaN −0.023, −0.014; AlN −0.037, −0.018; InSb −0.017, −0.004; GaSb −0.037, −0.021;
SiO₂-q +0.008, +0.004; ZnO −0.015, −0.008; MgO −0.030, −0.013; NaCl −0.020, −0.006; NaI −0.025, −0.009; CsI −0.029, −0.009; CaF₂ −0.017, −0.005;
MgF₂ −0.019, −0.005; ZnS −0.041, −0.023; PbTe −0.127, −0.035; PbS +0.065, +0.026; PbSe +0.092, +0.025; SrTiO₃ −0.032, −0.021; KTaO₃ −0.010, −0.005;
C −0.016, −0.009; 4H-SiC −0.052, −0.036; Ge −0.003, −0.000 (all in %). The replacement table is R3-7.

**Other model numbers.** R&K points (§1.7(c)): ε 3.4249/3.6513/3.7868 → 3.4230/3.6491/3.7844 eV; F 0.11033/0.11445/0.11679 → 0.11029/0.11441/0.11674;
(A, E_g) = (5.2, 1.0) and (5.2, 1.2): ε 3.4412 → 3.4379, 3.7793 → 3.7783; F 0.11832 → 0.11824, 0.11236 → 0.11233. Secants: ∂ε/∂A 0.0905 → 0.0904,
∂F/∂A 0.00161 (=), ∂ε/∂E_g 1.691 → **1.702**, ∂F/∂E_g −0.0298 → −0.0296. Deviations from R&K Eqs. (12)–(13): points ε ≤ 1.15% (v2 1.10%), F ≤ 2.42%
(2.38%), both at A = 3; slopes ≤ 7.6% (7.7%), ∂F/∂E_g +5.6% (+6.5%). Ge decomposition (§1.6): 𝒱_> 0.44395 → 0.44393, F^{ren} 0.015349 → 0.015352
(printed 0.4440 → 0.4439, 0.0153 → 0.0154; the rest equal at 4 digits). Scan (60 rows): every row within 0.14% (ε) / 0.07% (F) of v2; F range
[0.083, 0.142] unchanged. β-Ga₂O₃ with Γ-point ω₀ (C27): 9.974 against 9.987 eV (−0.13%), residual +56.4% against +56.2%.

## 4. Do the GAP-EF-v2 statements change?

| Statement | v2 | v3 | Verdict |
|---|---|---|---|
| F_Si (V0, untuned) | 0.1138 | 0.1138 (0.113843) | STANDS |
| 2.6σ below 0.119 ± 0.002 | 2.58σ | 2.58σ (2.579) | STANDS |
| 𝒜_ph | 5.595 eV³ | **5.588 eV³** | number changes (−0.12%) |
| ±10% in 𝒜_ph → ±0.7% in F; ∂F/∂𝒜_ph 0.0014 eV⁻³ | 0.68% | 0.68% | STANDS |
| Si decomposition 0.091 + 0.288 − 0.265 = 0.114; 92% cancellation | — | identical | STANDS |
| Primary residuals −6.5% … +24.6%, mean +8.2%, rms 12.3% | | −6.5% … **+24.7%**, +8.2%, 12.3% | upper end changes in the last digit |
| No-GaN rms 8.7%; extended rms 23.0%, max +56.1%; all rms 63.4%, max +178.8% | | 8.7%; 23.0%, **+56.2%**; 63.4%, **+178.9%** | maxima change in the last digit |
| (EF9) 1.613 + 2.327(λ_ph w_ph^{0.964})^{0.2395}, max 0.52%, rms 0.19% | | 1.613 + **2.329**(λ_ph w_ph^{**0.965**})^{0.2395}, 0.52%, **0.18%** | coefficients change in the last digit |
| (EF10) 0.02347 + 0.03643e − 0.002711e² + 0.01653w_ph, max 2.3%, rms 0.8% | | **0.02346 + 0.03644e − 0.002712e² + 0.01658w_ph**, 2.3%, 0.8% | coefficients change in the last digit |
| k₂ ∈ [1.2, 2.5] eV, in-domain 1.5–2.5, k₂(Si) 1.87 eV | 1.196–2.534, 1.871 | 1.196–2.532, 1.870 | STANDS at the printed digits; ω₀ exponent 0.96 → 0.97 |
| (EF11) vs solver FD: "1.69; solver FD 1.78" (v2), "FD 1.777, (EF11) 4.6% low" (errata C15) | | **FD 1.699; (EF11) 1.694, 0.3% low** | **CHANGES** (v2's FD was a grid artefact) |
| R&K: F_∞ 0.1145 vs 0.115; points ≤ 1.1% / 2.4%; slopes ≤ 7.7% | | **0.1144**; ≤ **1.2%** / 2.4%; ≤ **7.6%** | numbers change in the last digit; CROSS-CHECKED stands |
| Predictions table, 27 rows | | 18 rows change in a printed digit (R3-7) | no reading, band verdict or ordering changes |
| 4H-SiC F 0.093/0.091/0.091; floor 0.0510 | | identical | STANDS |
| Discretisation "≤ 0.05% (Si), 0.12% (C)" | doubling differences | errors at the production grid: Si 0.064% (ε), 0.071% (F); C 0.19% | **wording changes** (order 3/2, §2) |

## 5. Replacement texts for GAP-EF-v2.md

**R3-1. §0, row 1** (cell "Result"): "Exact first and second moment recursions (EF3)–(EF4) of the energy-only cascade, solved by quadrature on
grids commensurate with E_g, θ_iiE_g and ω₀ (values at the true ω₀ by interpolation in w_ph; GAP-EF-v3). The scheme is O(h^{3/2}) with phonons (O(h) at λ_ph = 0); discretisation
error at the production grid ε +0.064%, F −0.071% (Si), ε +0.19% (C) (GAP-EF-v3-C2); asymptote stable to 10⁻⁴ (GAP-EF-v2-C6)". (Tag as in
GAP-EF-v2-errata R-1.)

**R3-2. §0, row 5**, the R&K clause: "R&K: F_∞ **0.1144** vs 0.115, **agreement at their ≈ 2% MC scatter**, plus five points and four slopes of
their fitted planes, Eqs. (12)–(13) (GAP-EF-v2-C8)". Same in §1.7(c) first sentence ("give F_∞ = 0.1144") and in L-EF4 ("F_∞ = 0.1144").

**R3-3. §0, row 6**, first sentence: "𝒜_ph = **5.588 eV³**, fixed by Si ε_eh = 3.749 eV alone (ABS fit 5.2)." The rest of the row stands. Same
number in §2 (l. 294: "𝒜_ph = 5.588 eV³ (V0)").

**R3-4. §0, row 7**, first sentence: "ε_eh/E_g = 1.613 + 2.329(λ_ph w_ph^{0.965})^{0.2395} (0.52% max) is an **observed fit** of the model. In eV it
reads ε_eh ≈ 1.61E_g + k₂ with k₂ = 2.33(𝒜_phω₀^{0.97})^{0.24}E_g^{0.05}". The rest stands. Same k₂ formula in L-EF5.

**R3-5. §0, rows 8 and 10**: in row 8 "residuals −6.5% … **+24.7%**, mean +8.2%, rms **12.3%**"; in row 10 "Bands now carry the **+24.7%** GaN
residual". Everything else in both rows stands.

**R3-6. §1.3, Step 4**, the grid sentence: "The grid is **commensurate**: h = 1/N must divide E_g, θ_iiE_g and ω₀, because the sweep reads m_t, ρ_t and
p_t at x − E_g and x − ω₀ and starts ii at θ_iiE_g; cascade.py raises otherwise (GAP-EF-v3-C1). N is the smallest N ≥ 60 with Nθ_ii integral and
|n_w/N − w_ph| < 1% w_ph; the solver runs at the commensurate nodes k/N, k = n_w − 1, n_w, n_w + 1, and every output is interpolated to the true
w_ph (error ≤ 3 × 10⁻⁵, GAP-EF-v3-C3). (v1 silently ran CsI with 2.04 w_ph, REF-B 2.7; v2 ran every row at w_eff = n_w/N, within 1% of w_ph, and
θ_ii = 3/2 at θ_eff = 3/2 − 1/(2N) on odd N; GAP-EF-v3 errata.)"

**R3-7. §1.6 table, three cells:** Si V1 𝒱_> **0.1777**; Ge 𝒱_> **0.4439**; Ge F^{ren} **0.0154**. (Ratio column unchanged.)

**R3-8. §1.7(c) table** (complete; also replaces GAP-EF-v2-errata R-9's table):

| quantity | solver | R&K Eqs. (12)–(13) |
|---|---|---|
| ε at (A, E_g) = (3, 1.124) / (5.2, 1.124) / (7, 1.124) | 3.423 / 3.649 / 3.784 eV | 3.463 / 3.648 / 3.799 eV |
| F at the same points | 0.1103 / 0.1144 / 0.1167 | 0.1130 / 0.1163 / 0.1190 |
| ∂ε/∂A (secant over A ∈ [3, 7]) | 0.090 | 0.084 |
| ∂F/∂A (secant) | 0.0016 | 0.0015 |
| ∂ε/∂E_g (secant over E_g ∈ [1.0, 1.2]) | 1.70 | 1.7 |
| ∂F/∂E_g (secant over E_g ∈ [1.0, 1.2]) | −0.030 | −0.028 |

and the sentence after it: "All five points agree to ≤ 1.2% in ε and ≤ 2.4% in F; the largest deviations of both are at A = 3. All four slopes
agree to ≤ 7.6%." (GAP-EF-v2-C8.)

**R3-9. §1.8, (EF9)–(EF10)** (complete displays):

  ε_eh/E_g = 1.613 + 2.329 (λ_ph w_ph^{0.965})^{0.2395}   (max 0.52%, rms 0.18%),                                                                (EF9)
  F_eh = 0.02346 + 0.03644 e − 0.002712 e² + 0.01658 w_ph,   e ≡ ε_eh/E_g   (max 2.3%, rms 0.8%).                                              (EF10)

(scan.py rerun on the commensurate solver; v2's scan.json was the v1 output.) The k₂ line: "k₂ = 2.33(𝒜_phω₀^{0.97})^{0.24}E_g^{0.05}"; the
exponent 1 − (3 + γ)β is 0.0503 with the stored coefficients (0.0504 with the rounded (0.965, 0.2395)). k₂(Si) = 1.870 eV ("1.87" stands);
range 1.196–2.532 eV ("1.2–2.5" stands).

**R3-10. §1.8, (EF11)** (complete display):

  dε_eh/dE_g = c₀′ + c₁u(1 − 3β − γβ),   u = (λ_ph w_ph^γ)^β,   (c₀′, c₁, γ, β) = (1.613, 2.329, 0.965, 0.2395)   [Si: 1.69; solver FD 1.70, GAP-EF-v2-C15].   (EF11)

"R&K's Eq. (12) slope 1.7 agrees." stands.

**R3-11. §1.9 table, three rows** (complete):

| Item | Size | Status |
|---|---|---|
| discretisation (commensurate grid; N, 2N, 4N) | order h^{3/2}; error at the production grid: ε +0.064%, F −0.071% (Si; absorbed in 𝒜_ph); ε +0.19%, F −0.087% (C); others ≈ 1.55 × the N-vs-2N difference (SiO₂ ≈ 0.28%) | quantified (GAP-EF-v2-C5, GAP-EF-v3-C2) |
| ω₀ and θ_ii off the grid | none: commensurate nodes + interpolation to the true ω₀ (≤ 3 × 10⁻⁵); θ_ii = 3/2 on even N. v2's < 1% ω₀ offsets and θ_eff = 3/2 − 1/(2N) moved ε by ≤ 0.06% (V0), ≤ 0.19% (V1) | removed (GAP-EF-v3-C1, C3, C5) |
| calibration at E_g(110 K) for a 123 K datum | ≲ 0.1% in ε [E] (dε/dE_g ≈ 1.7) | estimated |

and in the (H-EF5) row: "ε residual −6.5% … +24.7% (§2)".

**R3-12. §2 table, model columns** (the other columns stand):

| Material | model V0 (V1, V3) | resid. | F model V0 |
|---|---|---|---|
| Ge | 2.79 (2.79, 2.69) | +5.9% | 0.125 |
| C | 11.37 (**11.83, 12.23**) | +13.9% | 0.088 |
| 4H-SiC | **7.56 (7.67, 8.04)** | **+3.6%** | 0.093 |
| 6H-SiC | **7.16** (7.25, 7.60) | −6.5% | 0.094 |
| 3C-SiC | 6.12 (6.15, **6.41**) | +12.8% | 0.099 |
| GaN | 7.69 (**7.85**, 8.22) | **+24.7%** | 0.091 |
| SiO₂ | 17.41 (19.05, 18.76) | +3.4% | 0.084 |
| β-Ga₂O₃ (extended) | 9.99 (**10.39, 10.75**) | **+56.2%** | 0.087 |
| Al₂O₃ (EF-LIT) | 16.54 (18.21, 17.84) | **+63.3%** | 0.084 |
| CaWO₄ (EF-LIT) | 10.69 (11.17, 11.51) | **+178.9%** | 0.087 |
| GaAs | **3.94** | (**+6.5%**, excluded) | 0.104 |

**R3-13. §2, residual statistics and reading** (substitutions; the sentences otherwise stand): "range −6.5% … **+24.7%**, mean +8.2%, rms 12.3%";
"**Extended** … −6.5% … **+56.2%**, mean +14.2%, rms 23.0%"; "All [FT] rows … −6.5% … **+178.9%**, rms 63.4%"; "GaN (**+24.7%** at EBIC)"; "GaN (8.9 eV
against EBIC 9.59: +7.8% against **+24.7%**)"; "4H-SiC (7.3 eV, +7.3% against the model's **+3.6%**)". "GaN at 8.9 eV would give +15.7%" stands.

**R3-14. §3 Recipe:** "(−6.5% / **+24.7%** on ε; Si's +4.5% on F). The **+24.7%** is GaN at EBIC; with GaN excluded it would be +13.9%." Add after the
"v2 rerun" bullet: "- **v3 rerun (R17).** Every row recomputed on the commensurate solver at the true ω₀ (and θ_ii = 3/2 exactly in V1): ε_eh
moved by −0.13% … +0.09%, F_eh by ≤ 0.04%, band edges by ≤ 0.12% (GAP-EF-v3 errata §3)."

**R3-15. §3 table** (complete; columns as in v2):

| Material (WP8-U verdict) | E_g | λ_ph | w_ph | ε_eh [eV] (band) | ε_eh/E_g | F_eh (band) |
|---|---|---|---|---|---|---|
| GaAs (S) | 1.42 | 1.95 | 0.0246 | 3.94 (3.69–4.93) | 2.78 | 0.104 (0.096–0.108) |
| Al₂O₃ (S)ⁿ | 8.8 | 0.0082 | 0.0118 | 16.54 (15.47–20.95) | 1.88 | 0.084 (0.067–0.088) |
| TeO₂ (S)ⁿ [DB gap] | 4.645 | 0.056 | 0.0192 | 9.69 (9.06–12.19) | 2.09 | 0.088 (0.068–0.092) |
| CaWO₄ (S)ⁿ | 5.2 | 0.04 | 0.0204 | 10.69 (9.99–13.45) | 2.06 | 0.087 (0.068–0.091) |
| LiF (S)ⁿ | 14.2 | 0.002 | 0.0054 | 25.05 (23.43–32.49) | 1.76 | 0.082 (0.068–0.086) |
| NaF (S)ⁿ | 11.5 | 0.0037 | 0.0043 | 20.48 (19.16–26.45) | 1.78 | 0.082 (0.068–0.086) |
| Ge (S), F only | 0.73 | 14.4 | 0.0507 | 2.79 (2.58–3.48) | 3.83 | 0.125 (0.108–0.130) |
| C (C), F only | 5.47 | 0.034 | 0.0298 | 11.37 (10.64–14.31) | 2.08 | 0.088 (0.083–0.092) |
| 4H-SiC (C), F only, F conditional (§2) | 3.26 | 0.16 | 0.0368 | 7.56 (7.07–9.49) | 2.32 | 0.093 (0.088–0.097) |
| GaN (C), F only | 3.43 | 0.14 | 0.0259 | 7.69 (7.19–9.66) | 2.24 | 0.091 (0.086–0.095) |
| AlN (C) | 6.2 | 0.023 | 0.0176 | 12.33 (11.53–15.52) | 1.99 | 0.086 (0.081–0.090) |
| SiO₂-q (C)ⁿ | 9.2 | 0.0072 | 0.0162 | 17.41 (16.28–22.00) | 1.89 | 0.084 (0.067–0.088) |
| ZnO (C)ⁿ | 3.3 | 0.16 | 0.0192 | 7.32 (6.83–9.19) | 2.22 | 0.090 (0.069–0.095) |
| MgO (C)ⁿ | 7.83 | 0.012 | 0.0105 | 14.84 (13.88–18.76) | 1.90 | 0.084 (0.067–0.088) |
| ZnS (C) | 3.8 | 0.1 | 0.0108 | 7.95 (7.43–10.00) | 2.09 | 0.087 (0.083–0.091) |
| NaCl (C)ⁿ | 8.75 | 0.0083 | 0.0035 | 15.83 (14.81–20.31) | 1.81 | 0.083 (0.067–0.087) |
| NaI (C)ⁿ | 5.8 | 0.029 | 0.0034 | 10.90 (10.20–13.82) | 1.88 | 0.084 (0.067–0.088) |
| CsI (C)ⁿ | 6.14 | 0.024 | 0.0016 | 11.21 (10.48–14.33) | 1.82 | 0.083 (0.067–0.087) |
| CaF₂ (C)ⁿ | 11.81 | 0.0034 | 0.0047 | 21.04 (19.67–27.16) | 1.78 | 0.082 (0.068–0.086) |
| MgF₂ (C)ⁿ | 12.4 | 0.0029 | 0.0059 | 22.14 (20.70–28.55) | 1.79 | 0.082 (0.068–0.087) |
| SrTiO₃ (C)ⁿ [DB gap] | 2.302 | 0.46 | 0.0285 | 5.68 (5.24–7.12) | 2.47 | 0.096 (0.071–0.101) |
| KTaO₃ (C)ⁿ [DB gap] | 3.326 | 0.15 | 0.0196 | 7.37 (6.89–9.26) | 2.22 | 0.090 (0.069–0.094) |
| GaSb (C) | 0.72 | 15 | 0.0379 | 2.67 (2.48–3.32) | 3.70 | 0.122 (0.106–0.128) |
| InSb (C) | 0.24 | 404 | 0.0896 | 1.75 (1.40–2.19) | 7.31 | 0.159 (0.127–0.166) |
| PbS (C) | 0.29 | 229 | 0.0928 | 1.92 (1.57–2.39) | 6.61 | 0.155 (0.124–0.162) |
| PbTe (C) | 0.19 | 815 | 0.0711 | 1.52 (1.18–1.90) | 8.01 | 0.162 (0.129–0.170) |
| PbSe (C) | 0.17 | 1140 | 0.1006 | 1.56 (1.17–1.94) | 9.16 | 0.168 (0.133–0.175) |

**R3-16. §4.2(iii)**: "(EF11) giving ≈ 1.7 (Si) to ≈ 1.6 (wide gap)" stands.

**R3-17. §7**, header "(code/GAP-EF-v3/checks.py, 41/41 PASS, ≈ 3 min)"; row GAP-EF-v2-C20 → "every validation and prediction row at the true ω₀:
commensurate interpolation nodes, |δ|/n_w < 1%, θ_ii = 3/2 rows on even N; CsI N ≥ 600; grid() fails loudly"; new rows as in §7 below.

**R3-18. Closing table, row B-7**: append "; v3 (R17): strict commensurate grid, values at the true ω₀ (GAP-EF-v3 errata)".

## 6. Replacement texts for GAP-EF-v2-errata.md

**E3-1. Header, Numerics paragraph**, last sentence: "The solver (cascade.py, model.py) and data/*.json are unchanged, so data/results.json remains
the record of the return" → "… so code/GAP-EF-v2/data/results.json was the record of the return until R17; **code/GAP-EF-v3/data/results.json
supersedes it** (commensurate grid, GAP-EF-v3 errata)."

**E3-2. §1, VER #8 / V-12**, bullets 2–3: "The fourth slope, from data/results.json rk_slopes, is ∂F/∂E_g = (0.112333 − 0.118245)/0.2 = **−0.0296**
against Eq. (13)'s −0.028 (+5.6%). So there are **four** slopes, not three." / "Maximum point deviations: −1.15% in ε and −2.42% in F, both at
A = 3." Bullet 4: "(observed ≤ 7.6%)".

**E3-3. §1, VER #11 / V-13**, bullets 1–3: "k₂(Si) = 2.3291(5.5878 × 0.063^{0.96541})^{0.23949} × 1.164^{0.05033} = **1.870 eV**, so "1.86" becomes
"1.87"." / "The exponent 1 − (3 + γ)β is 0.0503 with the stored fit coefficients, 0.0504 with the rounded (0.965, 0.2395); both round to 0.05." /
"C25 pins min 1.196, max 2.532, in-domain min 1.505 (GaSb), and Si 1.870 (±0.002)."

**E3-4. §1, VER #14 / V-7**, bullet 3: "With that Γ-point convention the model gives ε = 9.974 eV against 9.987 (−0.13%). The residual becomes
+56.4% against +56.2% (C27)."

**E3-5. §2, R-1 row 1**: replaced by R3-1 above. **R-1 row 5**: "F_∞ 0.1144 vs 0.115".

**E3-6. §2, R-9**: the table and the sentence after it are replaced by R3-8 above.

**E3-7. §2, R-10**: "In the line before (EF11), the exponent reads "E_g^{1−(3+γ)β} = E_g^{0.050}". With the stored coefficients this is 0.0503; with
the rounded (0.965, 0.2395) it is 0.0504."

**E3-8. §2, R-11** (β-Ga₂O₃ row): "gives model 9.974 eV and residual +56.4% (GAP-EF-v2-C27)"; model column "9.99 (10.39, 10.75)"; resid. "+56.2%".

**E3-9. §2, R-13 acceptance tests**: (a2) "ε = 3.649 eV and F = 0.1144 at (A, E_g, ω₀, B_h) = (5.2 eV³, 1.124 eV, 63 meV, 12 eV)"; (a4) "ε = 3.749 eV
at 𝒜_ph = 5.588 eV³". Pitfall (p1): replace "Each phonon step must be an integer number of bins to < 1%, the rule that model.grid enforces" by "Each
phonon step, E_g and E_th must be an integer number of bins **exactly** (the solver raises otherwise, GAP-EF-v3-C1); the value at the true ω₀ comes from
commensurate solves interpolated in ω₀ (GAP-EF-v3-C3), never from rounding ω₀ onto the grid". Expected accuracy: "**worse for 4H-SiC (+7.3% against
+3.6%) and SiO₂ (+7.8% against +3.4%)**". Add a pitfall: "(p8) *Order.* With √-DOS edges the scheme is O(h^{3/2}); extrapolate with the observed order,
not linear Richardson, for rows with phonons; the λ_ph = 0 rows are O(h) (GAP-EF-v3-C2, C2b)."

**E3-10. §2, R-14 check rows**: GAP-EF-v2-C13 targets "−6.5/24.7/8.2/12.3, 5.5/8.7/13.9, 14.2/23.0/56.2, 63.4/178.9%"; GAP-EF-v2-C15 "(EF11) 1.694 and
FD 1.699 at the true ω₀, ±0.005 (v2-errata's FD 1.777 was the w_eff jump between E_g ± 0.01 eV)"; GAP-EF-v2-C25 "k₂ ∈ [1.196, 2.532] eV, in-domain
minimum 1.505, k₂(Si) = 1.870".

**E3-11. §3, L-EF4** (re-issued row): "F_∞ = 0.1144"; "agree with R&K Eqs. (12)–(13) to ≤ 1.2% (ε), ≤ 2.4% (F) at five points, four slopes ≤ 7.6%".

**E3-12. §4 Rebuttal (item 11)** and **§6 row #11**: "exponent 0.0507" → "exponent 0.0503 (v3 fit; v2 fit 0.0507)".

## 7. Owed outside this write set
- **WP8-errata §5, IF-EW-1** (owner ERR-WP8 / coordinator): replace "every GAP-EF(-v2) ε_eh, F prediction at h = 0.02 is for ω₀,eff … For the Si case
  the bias is +1.3% in ε_eh" by "GAP-EF-v2 did not use h = 0.02: model.grid held |w_eff/w_ph − 1| < 1% (and θ_ii = 3/2 was rounded on odd N).
  Rerun on the commensurate solver (code/GAP-EF-v3, returns/R17/GAP-EF-v3-errata.md): ε_eh moves by ≤ 0.06% (V0), ≤ 0.19% (V1), F_eh by ≤ 0.13%;
  Si F = 0.114 and its 2.6σ stand." Its rows at l. 454 and l. 518 ("Si +1.3% in ε_eh") → "**closed**: ≤ 0.19% (GAP-EF-v3)".
- state/CORRECTIONS.md: a GAP-EF-v2 section pointing to this file (coordinator).
- code/GAP-EF/cascade.py (v1) carries the same rounding; v1 is superseded, no rerun owed.

## 8. Checks (code/GAP-EF-v3/checks.py, 41/41 PASS, ≈ 3 min; output in data/checks_stdout.txt)
The 32 GAP-EF-v2 checks run on the v3 solver and data with these edits: C3/C4a/C4b at w_ph = 4/74 (identities; the v2 call is refused by the
guard); C13 targets 24.7/56.2/178.9; C15 targets FD 1.699, (EF11) 1.694; C25 targets max 2.532, k₂(Si) 1.870; C20 rewritten (rows at the true ω₀). New:

| Check | Content |
|---|---|
| GAP-EF-v3-C1 | the guard raises on v2's Si grid (w = 0.054124, h = 1/74), on CW7's h = 0.02, on θ_ii = 3/2 with N = 79, on w < h; accepts commensurate grids and the λ_ph = 0 grids of table1; v2's odd-N V1 rows = {4H-SiC, 6H-SiC, C, GaN, Ge} |
| GAP-EF-v3-C2 | commensurate h-sequences (Si 74/148/296, C 67/134/268) monotone, order 3/2 ± 0.02; production-grid error Si ε +0.064%, F −0.071%; C ε +0.19%, F −0.087% |
| GAP-EF-v3-C2b | λ_ph = 0 rows: order 1 (± 0.05), table1's linear Richardson stands; c₀ within 10⁻⁴ of the three-level extrapolation |
| GAP-EF-v3-C3 | interpolation in w_ph: 3 vs 5 nodes ≤ 3 × 10⁻⁵ (Si, Ge V1, C, 3C-SiC, CsI), 3 vs 2 nodes ≤ 10⁻⁴ |
| GAP-EF-v3-C4 | independent MC (mc.py) vs solver h → 0 at the true ω₀: ⟨N⟩, Var N at x₀ = 10, 20 and the secants, Si/Ge/C, all \|z\| < 3 (max 1.5) |
| GAP-EF-v3-C4b | MC ε_eh, F_eh on the fit window [X/2, X] vs solver continuum (\|z\| < 3, max 0.7) and vs the reported v3 values (within MC + 1.6 × doubling difference) |
| GAP-EF-v3-C5 | v2 → v3 bounds: validation ε ≤ 0.19% (V0 ≤ 0.06%), F ≤ 0.13%; predictions ε ≤ 0.13%, F ≤ 0.041%; Δ𝒜_ph = −0.124%; C V1 split θ +0.165%, grid +0.025% |
| GAP-EF-v3-C6 | headline digits: F_Si 0.1138, 2.58σ, 𝒜_ph 5.588, rms 12.3%, (EF9)/(EF10) coefficients and residuals as in R3-9 |
| GAP-EF-v3-C7 | scan rerun: rows within 0.14% (ε), 0.07% (F) of v2; fit residuals 0.52%/0.18%, 2.3%/0.8% |

## Symbols introduced/used
| Symbol | Meaning | Status |
|---|---|---|
| h = 1/N | energy-grid bin in units of E_g; N points per E_g | as GAP-EF-v2 (code) |
| n_w, w_eff = n_w/N | phonon step in bins; v2's quantised w_ph | local (this errata) |
| θ_eff | v2's quantised θ_ii, h·round(θ_ii/h) | local |
| δ = w_phN − n_w | offset of the true w_ph from the nearest node | local |
| w_ph = ω₀/E_g, λ_ph = 𝒜_ph/E_g³, θ_ii, a_DOS, B_h | as GAP-EF-v2 / NOTATION | used |
| 𝒱_<, 𝒱_>, 2𝒞_<>, F^{ren}, r̄_c, 𝔓_t, ρ_t, k₂ | as GAP-EF-v2 | used |
| p | observed order of the quadrature error, f_N − f_∞ ∝ h^p (here 3/2) | local |
| x₀ | seed electron kinetic energy (units E_g) | as GAP-EF-v2-errata R-2 |
