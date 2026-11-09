# R18 / REF-DC-67: hostile referee report on returns/R18/DC-67.md and code/DC-67/

Read: DC-67.md; CW7 §4; CW7-errata §1.4; WP8-errata §5, §14, §16–17, IF-EW-1; GAP-EF-v3-errata; CORRECTIONS rows l.605, l.612–616; CONVENTIONS; NOTATION; code/DC-67 and its data; code/GAP-EF, -v2, -v3 result files; WP8-U-table-v4.csv. No other R18 return or referee report was read.
Own code: code/REF-DC-67/. `ref_casc.py` is a new solver with exact cell masses for ρ (hole edge cut exactly), closed-form Φ_t, block FFT convolutions, and its own MC. It shares no code or quadrature with cascade.py or casc2.py and converges as h² where theirs converges as h^{3/2}. DC-67's casc2.py and P_casc_lib.py were run only as objects under test (claims 4, 5, reader). Python as specified, ≤ 2 cores.

## 0. Verdicts

| # | Claim | Verdict | Key numbers |
|---|---|---|---|
| R | **Not in the brief: the library reader** | **FAILS**: violates property (b) on all 30 V1 tables; jump exceeds 10⁻² on 21 of 30 (list in §5) | Reader gives P(N = 1) = 0.450 for LiF at x_e = 1.49, x_h = 0.2, below the θ_ii = 3/2 threshold; the exact value is 1 (CW7 property (b)). Error up to 0.68. No check covers it |
| 1a | D4: "criterion unreachable", error falls as x^{−1/2}, 10⁻⁶ at x ~ 10⁹–10¹⁰ | **FAILS** as derived | Correct law max\|ΔP\| ≃ C/x, Si C = 0.242 predicted, 0.243 measured. Gaussian reaches 10⁻⁶ at x ≈ 2.4×10⁵. Second-order Edgeworth falls as x⁻²: ≈ 6×10² (extrapolated) |
| 1b | X1 criterion 10⁻⁶ on a Gaussian | Criterion **wrong**, and `gaussian_match` has a **real defect** | Binned Gaussian carries variance σ² + 1/12 (same 1/x leading law, extra x^{−3/2} term). Point form halves the error at the table end (wide gap 1.0×10⁻² → 4.6×10⁻³) |
| 2 | +1.3% is CW7-C7 only; GAP-EF shift ≤ 0.19% | **STANDS WITH CORRECTION** | ε 0.1898% (C V1), F 0.1283% (6H-SiC V1), V0 0.0592%. "Independent code" is false |
| 3 | Si: 3.7466 eV; 5.618 eV³; F 0.11396; 2.52σ | **STANDS WITH CORRECTION** | Reproduced to 7 digits on the GAP-EF window [20, 40]. As x → ∞: ε 3.74678 eV; recalibrated 𝒜_ph 5.6156 eV³, F 0.11398, **2.51σ** |
| 4 | Convex read | **STANDS WITH CORRECTION** | Biased at O(a(1−a)h²); ≲ 10⁻⁵ in ε, F at production (2 rows measured), 10⁻⁴-level at a ≈ ½. P < 0 in the rejected run was an artefact of unphysical rows; the mixture-variance argument stands |
| 5a | Order h^{3/2} | **STANDS** | Error ratio 2.83 per doubling, all x, SiO₂-q and Si |
| 5b | Median 4×10⁻³; Si 1.3×10⁻³ | **STANDS** | 3.9×10⁻³; 1.35×10⁻³ |
| 5c | Worst 1.5×10⁻² | **FAILS** | 2.19×10⁻² (SiO₂-q, x = 1.306); own MC 2.05×10⁻² at x = 1.355. With the reader 3.2×10⁻² (m1). Near-onset relative error −19% |
| 6 | Coverage; "closed except X1 and the 14" | **FAILS** as a closure statement | 42/14/28 counts correct, but 2 of the 14 are SURVIVORs, the exclusion reason is contradicted by 3 library rows, and the Λ map is not delivered |

Overall: the solver and the Si physics stand. **The library must not be released through `P_casc_lib.py` as it stands.** §7 of the return (closure, "WP6 can drop the profiling") should be withdrawn pending R, 5c, 6.

## 1. X1: the Gaussian match

**Derivation.** N is integer valued with cumulants κ_r(x) = K_r N̄ + c_r + (exponentially small), since ln 𝔊 is asymptotically linear in x (CW7 §4(c)). Here σ² = F N̄ and κ₃ = K₃N̄. The lattice local limit expansion with z = (n − N̄)/σ is

 P(n) = (φ(z)/σ)[1 + (γ₁/6)He₃(z) + (γ₂/24)He₄(z) + (γ₁²/72)He₆(z) + …] + O(e^{−2π²σ²}),  γ₁ = κ₃/σ³, γ₂ = κ₄/σ⁴.

CW7's O(x^{−1/2}) is the **relative** size of the skewness term. The **absolute** pointwise error carries the further 1/σ of the peak height:

 max_n|P − Gauss| ≃ max_z|φHe₃|/6 · |κ₃|/σ⁴ = 0.0917 |K₃| / (F² N̄) ≡ C/x,  C = 0.0917 |K₃| ε_eh/(F²E_g).

So the scale is **x⁻¹, not x^{−1/2}**. The return's own data say so: 1.98×10⁻², 1.32×10⁻², 9.8×10⁻³ at x = 20, 30, 40 is exactly 1/x.

**Measured** (Si V0, own P(n|x), x to 240, rows every E_g/8, K₃ = 0.0106, F = 0.1139 → C = 0.242). Envelope max|ΔP| on [a, 1.5a) (data/x1_gauss.json):

| a (E_g) | binned, asymptotic (DC-67) | binned, exact moments | point Gaussian | + skewness term | + 2nd order |
|---|---|---|---|---|---|
| 20 | 2.6×10⁻² | 2.2×10⁻² | 1.3×10⁻² | 6.3×10⁻³ | 1.1×10⁻³ |
| 40 | 1.1×10⁻² | 9.9×10⁻³ | 6.3×10⁻³ | 2.3×10⁻³ | 2.6×10⁻⁴ |
| 80 | 4.9×10⁻³ | 4.4×10⁻³ | 3.1×10⁻³ | 7.7×10⁻⁴ | 6.0×10⁻⁵ |
| 160 | 2.2×10⁻³ | 2.0×10⁻³ | 1.5×10⁻³ | 2.7×10⁻⁴ | 1.4×10⁻⁵ |
| exponent, x ≥ 40 | −1.19 | −1.15 | **−1.03** | **−1.50** | **−2.10** |

C measured 0.243 against 0.242 predicted. At the author's sample points I reproduce 1.99×10⁻², 1.33×10⁻², 9.87×10⁻³. The "second order, asymptotic cumulants" column equals the exact-cumulant one for x ≥ 30, so the formula needs only linear cumulant laws. These are Si numbers; Edgeworth was not tested on other materials.

**Answer to the question: both.**
- *The criterion is wrong for its purpose.* No plain Gaussian meets 10⁻⁶ below x ≈ 2.4×10⁵ E_g, so it cannot be the stopping rule for X doubling.
- *D4 is wrong too.* Rate wrong; 10⁹–10¹⁰ is high by four orders; "unreachable" is false as a statement about the match, since second-order Edgeworth extrapolates to 10⁻⁶ at x ≈ 6×10² (0.35/x²; measured only to x = 240). Direct tables at cost ∝ X² also reach far past any need.
- *There is a real, second-order defect.* The binned form still converges to P with the same leading 1/x law, but it is measurably worse at finite x. `gaussian_match` integrates the density over unit bins, which convolves with a unit box and adds 1/12 to the variance (relative order 1/(12σ²)), which is 4–9% of σ² at the table end. The return's "even with the exact mean and variance" column therefore does not have the exact variance. The excess decays as x^{−3/2} but is up to half the error in the table's range: at the end of the 30 m1 tables, median max|ΔP| 1.4×10⁻² (DC-67 form) against about 5×10⁻³ (point form, exact moments), data/lib_end.json. The return also blames skewness alone; at x = 15 the binning is more than half the error (3.4×10⁻² against 1.6×10⁻²).

The return's "1–2%" at the table end is correct as a number (0.8–2.0×10⁻² on all 30 rows).

**Limits to state to users.** Leading law ΔP ≈ C/x with C (data/K3.json): wide gaps 0.07–0.10, GaAs 0.17, Si 0.24, Ge 0.33, InSb and Pb salts 0.7–1.0.
- Absolute, not relative: the error in small tail bins is relatively much larger.
- Needs σ² ≳ 0.7 (Si x ≳ 20). Below that Edgeworth is unreliable: on [5, 7.5) second-order is worse than the plain form (2.7×10⁻¹ with exact cumulants, against 7×10⁻² for the point Gaussian).
- b_N is for the one-sided electron seed; a two-carrier seed needs its own mean (b differs by 0.26–0.35, return §4).
- Holes in Si exist only for x_h ≤ W_v/E_g = 10.31. **Rows of Ph above that are unphysical**; the reader serves them silently.

## 2. Premise

Checked against the files directly (code/GAP-EF-v2 and -v3 data/results.json, 65 matched rows; model.py).
- **Stands:** v2 passes h = 1/N from grid() with Nmin = 60; recorded N are 60–98, none 50. Cascade's default h = 0.02 is never reached by the production path. Max change: V0 ε 0.0592% (3C-SiC), V1 ε 0.1898% (C), V3 0.0493%; F 0.1283% (6H-SiC V1); predictions 0.127% (PbTe). 𝒜_ph 5.5947 → 5.5878. CORRECTIONS l.605 is accurate. +1.319% reproduces from their stored run. §14 is indeed unrelated; IF-EW-1 is in §5.
- **Correction 1:** the "+1.3%" is not all ω₀ quantisation, which is how IF-EW-1 and DC-67 label it. With my solver: continuum ε/E_g 3.21839 (ω₀ 0.054), 3.25734 (0.06), so **+1.21% is quantisation, +0.11% is quadrature at h = 0.02** (3.26097/3.25734). F: 0.11391 → 0.11487.
- **Correction 2:** "≤ 0.19%" is the v2 → v3 change, not the error of the GAP-EF numbers. Production grids retain the O(h^{3/2}) error (Si ε +0.064%, C +0.19%, GAP-EF-v3 R3-1). The two are distinct and the return's item 1 runs them together.
- **Correction 3:** "90 rows re-verified by independent code" is false. casc2 uses, in the return's own words, the "same discrete arithmetic as cascade.py", at the same N. Agreement to 6×10⁻⁵ tests the coding of the two-table form and the read; it cannot see the shared quadrature error, which is larger than the agreement. Independent here means Si (claim 3) and §5 below.

## 3. Si recalibration

Own solver, ω₀ = 21/388 E_g exact, W_v cut exact, N = 388…3104 (order 2), LSQ fit as in `asym`:

| Quantity (window [20, 40]) | DC-67 | Referee |
|---|---|---|
| ε at 𝒜_ph 5.5878 | 3.74662 | 3.746619 |
| F | 0.113924 | 0.113924 |
| 𝒜_ph for ε = 3.749 | 5.6176 | 5.6176 (5.61759) |
| F | 0.113965 | 0.113964 |
| σ below 0.119 ± 0.002 | 2.518 | 2.518 |

So the arithmetic **stands to 7 digits**. But "continuum" here is h → 0 at fixed X = 40, not x → ∞, and the return never tests X for ε, F. Which is right is partly a convention: GAP-EF defines every ε_eh, F on [X/2, X]. If that convention is kept, the [20, 40] numbers stand as stated. If ε_eh, F mean the asymptotic slopes, the window transient is a **campaign-wide caveat on all rows**, sized here for Si only. The fit window is still in a damped transient (data/si_claim3.json, 𝒜_ph 5.5878):

| Window | [10,20] | [15,30] | [20,40] | [40,80] | [80,160] | [160,320] |
|---|---|---|---|---|---|---|
| ε (eV) | 3.74642 | 3.74792 | 3.74662 | 3.74678 | 3.74678 | 3.74678 |
| F | 0.11380 | 0.11416 | 0.11392 | 0.11394 | 0.11394 | 0.11394 |

Asymptote, direct solve on [80, 160]: at 5.5878, ε **3.74678 eV**, F **0.11394**; calibrated to 3.749: **𝒜_ph 5.6156 eV³, F 0.11398, 2.51σ**. The X-shift (ΔF 1.5×10⁻⁵, 𝒜_ph −0.0021) is about a fifth of the h-shift in F that the return reports, and the [15, 30] excursion (ΔF 2.4×10⁻⁴ = 0.12σ) is twice the 2.58 → 2.52 move. So 2.52σ has a digit it has not earned. It is immaterial next to ±0.002, but rounded to two figures the continuum statement is **2.5σ**, not the "2.6σ" that CORRECTIONS l.605, l.612 say stands. That sentence stands only as a production-grid figure.

## 4. Convex read

**Mean and variance are biased; the claim "mean exactly ω₀" concerns the energy step, not N.** The read replaces 𝔊(x − w) by linear interpolation, error ½a(1−a)h²𝔊″ per step. Isolated by comparing linear and cubic reads at the same N and quadrature (data/convex.json, c4b.json):

| Case | a | Δε/ε | ΔF/F | ΔN̄/N̄ (x = 20, vs truth) | Δvar/var | max\|ΔP\| from read |
|---|---|---|---|---|---|---|
| Si production N = 74 | 0.005 | −1.4×10⁻⁶ | +3.5×10⁻⁶ | | | |
| PbSe production N = 60 | 0.035 | −3.3×10⁻⁶ | +7.8×10⁻⁶ | | | |
| Si N = 83 | 0.49 | −5.3×10⁻⁵ | +1.4×10⁻⁴ | +6.0×10⁻⁵ | +2.0×10⁻⁴ | 1.7×10⁻⁴ |
| Si N = 46 | 0.49 | −1.7×10⁻⁴ | +4.5×10⁻⁴ | +2.0×10⁻⁴ | +6.7×10⁻⁴ | |
| SiO₂-q N = 154 | 0.49 | −7.4×10⁻⁵ | +7.3×10⁻⁵ | +8.0×10⁻⁵ | +1.6×10⁻⁴ | 9.4×10⁻⁴ |
| C N = 84 | 0.50 | | | | | 1.0×10⁻³ |

Sign: N̄ up, ε down, variance and F up. Scaling: Si 46 vs 83 gives 3.26 = (83/46)² as expected. Rough size δln N̄ ≈ 0.1 a(1−a)h²/w_ph (within ×1.4 on three cases; a fit, not a theorem).

**Production is safe, for a reason the return does not give.** grid() puts wN within 1% of an integer, so a(1−a) ≤ 0.047 on all 225 rows (26 of 30 m1 rows have a ≥ 0.98 or a < 0.01). The a ≈ ½ regime was never tested: W2 ran at a = 0.03 and the N → 2N → 4N series keeps a small. The bias is well below the quadrature error at every N, so it is a caveat, not a defect. The n_f = 0 branch, used by 10 m1 rows at a ≈ 0.99, I did not isolate; CsI at a = ½ and a = 0.99 gave total max|ΔP| 2.0×10⁻³ and 1.05×10⁻³ including quadrature.

**The reasons given for rejecting Lagrange need correcting; the mixture-variance argument stands.**
- "Not moment preserving" is imprecise: Lagrange in ω₀ is linear in P, so raw moments are interpolated exactly. The author's "mixture variance" is the correct term, Σ L_im_i² − (ΣL_im_i)², which vanishes for three nodes if m is linear in k. It is a third-difference effect that grows as m². It is real where nodes 1, 2, 3 span ×3 in ω₀: I reproduce GaAs V1 at −2.67×10⁻³ in F against the return's 2.65×10⁻³. At n_w ≥ 4 it is small (Si: 1×10⁻⁴).
- "P as low as −3.6×10⁻³": that value sits in **unphysical hole rows**, TeO₂ Wv, x = 1.03 > W = 1. Physical rows: min Pe −4×10⁻⁹. L2's failure was an artefact.

Rejecting the method was still right, on the F error alone.

## 5. Accuracy

**Spot check.** SiO₂-q m1 (their worst row), 2×10⁶ histories per x, own MC. The MC agrees with my solver (N = 1984) at every row (max |z| 1.3; the row x = 1.74, where all histories gave N_sub = 1, is omitted as degenerate), so the reference is anchored.

| x | lib − MC | MC standard error | mean MC | mean lib |
|---|---|---|---|---|
| 1.145 | 4.4×10⁻³ | 1.1×10⁻⁴ | 0.0229 | 0.0185 (**−19%**) |
| 1.258 | 1.8×10⁻² | 3.0×10⁻⁴ | 0.2323 | 0.2144 (−7.7%) |
| 1.355 | **2.05×10⁻²** | 3.4×10⁻⁴ | 0.6320 | 0.6114 |
| 1.500 | 2.7×10⁻³ | 1.0×10⁻⁴ | 0.9809 | 0.9781 |
| 3.5 | 7.6×10⁻³ | 3.5×10⁻⁴ | 1.5559 | 1.5482 |
| 6.0 | 5.0×10⁻³ | 3.2×10⁻⁴ | 2.9560 | 2.9462 |

Si m1 at x = 2.24, 3.24, 5, 8: lib − ref 0.85–1.1×10⁻³, consistent with 1.3×10⁻³.

**All 30 materials, m1, every table row against my solver at N ≥ 1500, x ≤ 25** (data/acc_m1.csv): median of per-material worst 3.9×10⁻³ (**stands**); worst **2.19×10⁻²** SiO₂-q x = 1.306, then Al₂O₃ 1.49×10⁻², MgO 1.13×10⁻², C 9.3×10⁻³. Si 1.35×10⁻³. V1 max 1.37×10⁻² (4H-SiC), V3 3.0×10⁻³, Wv 2.19×10⁻² (data/acc_var.csv). Holes checked only for Si: 1.35×10⁻³.

**Order:** max over all x of |P_N − truth|, N, 2N, 4N, 8N: SiO₂-q 2.21×10⁻², 7.83×10⁻³, 2.77×10⁻³, 9.78×10⁻⁴; Si 1.35×10⁻³, 4.76×10⁻⁴, 1.68×10⁻⁴, 5.93×10⁻⁵. Ratio 2.83 = 2^{3/2}. **Stands**, including through the threshold, and the 1.55 factor is right.

**Why 5c fails.** conv.py samples only multiples of 0.25 E_g, and the worst error is at x ≈ 1.3. Its range was also limited to X = 12, electrons, m1. The peak falls between samples.

**MC1 does not test what §5 implies.** It compares the MC with the **Richardson-extrapolated** solver at x = 5, 10, 20, never the tables and never near threshold. Against the table, the same kind of test gives |z| = 8–60 for SiO₂-q.

**Reader (R, the worst finding).** Total error including `carrier`'s linear interpolation, m1: median 6.5×10⁻³, worst **3.2×10⁻²** (LiF x = 1.23), ≥ 2×10⁻² on 7 of 30 rows; above x = 5 up to 9.8×10⁻³. The return's 2.4×10⁻² came from 6 materials, m1 only. **V1:** for θ_ii > 1, Φ(θ_ii − 1) > 0, so P has a true jump at x = θ_ii, and table rows sit at about 1.45 and 1.5. Linear interpolation smears the jump below threshold: P(N_sub = 0 | x) from the reader, should be exactly 1 for x < 1.5:

| x | 1.47 | 1.49 | 1.499 |
|---|---|---|---|
| LiF | 0.733 | 0.450 | 0.323 |
| C | 0.955 | 0.909 | 0.889 |

Max error 0.68 (LiF), V1 median over materials 3.5×10⁻². The size of the jump is p(θ_ii), the value 1 − P(0 | x = 1.5): above 10⁻² on 21 of 30 (LiF, MgF2, CaF2, NaF, SiO2-q, Al2O3, NaCl, MgO, AlN, CsI, NaI, C, CaWO4, TeO2, ZnS, GaN, KTaO3, ZnO, 4H-SiC, 6H-SiC, 3C-SiC); at or below 10⁻² on SrTiO3, GaAs, Si, Ge, GaSb, PbTe, PbSe, PbS, InSb, where the V1 tables are usable today at that error. This violates CW7 §4 property (b) and acceptance C8, which was only tested on raw grids. x_interp.py never touched V1. Fix: reader must return δ_{n,0} for x < θ_ii and interpolate only from the x = θ_ii row upward; add a row at each jump; refine rows on [1, 1.6] for wide gaps. I did not test such a fix.

## 6. Coverage

Verified from WP8-U-table-v4.csv: pool 42 = 10 SURVIVOR + 32 SURVIVOR-COND; the 14 named are the 14 missing; InSb, KTaO₃ are EXCLUDED-RADIO extras; 225 tables; max N̄ + 8σ = 27.6. Disclosed fairly: θ set is the author's choice, joint corner absent, Λ map absent, D5.

Misrepresented or omitted:
1. **Two of the 14 are SURVIVORs:** Li₂MoO₄ and γ-LiAlO₂ (WP8-errata §16.2). DC-67's row says "every … survivor". 9 of 11 are covered. The return never says so, and it lists them in the middle of a list of proxies.
2. **The exclusion reason is false as a criterion.** "No measured E_g and ω₀ pair" also describes TeO₂, SrTiO₃ and KTaO₃, which **are** in the library on JARVIS mBJ gaps. h-BN (6.115), c-BN (5.813), PE (8.914) have the same class of mBJ gap plus Γ-max modes. The real criterion is "inherited from GAP-EF PRED". h-BN leads the 42-pool NR-edge row of §16.4, with PE and c-BN behind it. Li₂MoO₄ has only a PBE gap and no mode row among those searched, so it does need an input decision.
3. **"Closed except X1 and the 14" omits the Λ half.** CW7 §4's *What* includes "the library maps Λ ↦ (x_e, x_h) for every Λ-sector". §1 admits that is not delivered; §7 drops it. Add also D5 (N ≤ 20 unreachable in wide gaps: table reach N̄ ≈ 14).
4. **θ_𝔉 is silently absent.** CW7 §4(d) names it (A-type, GaAs); it is neither tabulated nor listed. θ_{R-k} is covered only as part of the M factor. The WP5-v4 §8 ranges were not checked by me.
5. **Library m1 is calibrated to the production-grid 𝒜_ph.** If the coordinator adopts 5.616 eV³, the Si tables are off that basis by 0.5% in 𝒜_ph (inside the θ grid).
6. **"WP6 can now drop the discrete {step, R&K, URF} profiling"** does not follow: 12 non-metals have no table, and V1 is broken in the reader.
7. Accuracy statements rest on m1 electrons; the return gives no V1, V3, Wv, or hole convergence. L1, L2 hold by construction, and they include unphysical rows.

## 7. Exact replacement text

- **§0 item 3:** "GAP-EF Si, exact ω₀ = 21/388 E_g, no interpolation [CALC]. At 𝒜_ph 5.5878 eV³, h → 0: on the production window [20, 40], ε_eh 3.7466 eV, F 0.11392 (order 1.500); as x → ∞, ε_eh 3.7468 eV, F 0.11394. Recalibrating the asymptote to 3.749 eV: 𝒜_ph 5.616 eV³, F 0.1140, 2.5σ below 0.119 ± 0.002 (2.51σ; 2.52σ on the production window; production grid 2.58σ). Window choices at x ≥ 15 move F by up to 2.4×10⁻⁴ (0.12σ). Reproduced by independent solver (REF-DC-67 §3)."
- **§0 item 1, last sentence:** "The v2 → v3 change is ≤ 0.19% in ε_eh, ≤ 0.13% in F; this is not the residual grid error (Si +0.064%, C +0.19%). Of the +1.3%, +1.21% is ω₀ quantisation and +0.11% quadrature at h = 0.02. Not rerun here. The 90-row agreement is with the same discrete arithmetic and does not test quadrature."
- **§0 item 4:** delete "by independent code" wherever applied to the 90 rows.
- **§0 item 6 and D4:** "FAIL: Gaussian match beyond the table. CW7-errata §1.4's 10⁻⁶ is not a usable criterion for a Gaussian: the local limit expansion gives max|ΔP| ≃ 0.0917|K₃|/(F²N̄) = C/x (Si C = 0.24, measured 0.243), i.e. 10⁻⁶ at x ≈ 2×10⁵. The relative skewness is O(x^{−1/2}); the absolute error is O(x⁻¹). `gaussian_match` was also defective: unit-bin integration adds 1/12 to the variance. Use point values φ(z)/σ with the Edgeworth terms: errors x^{−3/2} (first order), x⁻² (second; Si 2.6×10⁻⁴ at x = 40, 1.4×10⁻⁵ at x = 160)."
- **CW7-errata §1.4 criterion:** "X doubling until the matched-Gaussian tail changes P by < 10⁻⁶" → "**X set by the largest N needed; beyond X use the second-order lattice Edgeworth form, whose error is stated (Si ≲ 3×10⁻⁴ for x ≥ 40); needs σ_N² ≳ 0.7.**" Also "C6: O(h)" → "O(h) at λ_ph = 0, O(h^{3/2}) with phonons".
- **§2 True ω₀:** "It failed for n_w ≤ 2: nodes 1, 2, 3 span ×3 in ω₀ and the interpolated P picks up a mixture term Σ L_im_i² − (Σ L_im_i)² in the variance, F off by up to 2.65×10⁻³ (raw moments are interpolated exactly; the term cancels for m linear in the node index). The P = −3.6×10⁻³ of the rejected run lay in unphysical hole rows x > W; physical rows reach −4×10⁻⁹." And after "mean exactly ω₀": "This does not make N̄ or Var N unbiased: the read is a linear interpolation of 𝔊 with error O(a(1−a)h²), raising N̄ and F. At a ≈ ½, Si N = 83: ε −5×10⁻⁵, F +1.4×10⁻⁴; at production a(1−a) ≤ 0.047 and the shifts are ≲ 10⁻⁵ (Si, PbSe measured: ≤ 8×10⁻⁶)."
- **E3-9 (p1) addition:** "for distributions use the convex phonon read on a grid with wN within 1% of an integer; do not interpolate P in ω₀ with nodes spanning more than ±25% of ω₀."
- **§3 h row:** "Production error at table rows, all x (REF-DC-67): median 3.9×10⁻³, worst 2.2×10⁻² (SiO₂-q, x = 1.31); Si 1.35×10⁻³. Worst errors are at x ≈ 1.2–1.5 in wide gaps, where the relative error in the first-ii probability reaches −19%. Reader interpolation adds to this: total 3.2×10⁻² for m1."
- **§4 MC1 row:** add "(tests the h → 0 extrapolation, not the tables; x ≥ 5 only)".
- **§1 Coverage, reason:** "Not covered: Al, Nb (metals); Li₂MoO₄, γ-LiAlO₂ (**SURVIVORs; 9 of 11 survivors are covered**); Bi₂Se₃, Cr₂O₃, MnO, NiO, NiPS₃, YIG, ZrTe₅ and h-BN, c-BN, PE. Selection is the GAP-EF PRED list, not data quality: TeO₂, SrTiO₃, KTaO₃ are in on the same DFT-gap footing as h-BN, c-BN, PE, which could be added at seconds per row."
- **§7, DC-67 row:** "Not closed. Open: reader across θ_ii jumps (V1 tables not usable until fixed); X1 as re-specified; 12 non-metals including 2 SURVIVORs; Λ map (needs S_Λ); θ_𝔉; N ≤ 20 reach in wide gaps. Rerun half closed in R17." Delete "WP6 can now drop …" until then.
- **`P_casc_lib.py` docstring:** "Ph rows above W_v/E_g are unphysical. x < θ_ii must return δ_{n,0}."

## 8. May be quoted in a textbook

1. "In the energy-only cascade model the number of pairs from a carrier of energy x has mean x/ε_eh + b and variance F x/ε_eh, and its distribution approaches a lattice Gaussian. The absolute pointwise error falls as 1/x; the relative skewness falls as x^{−1/2}." [D, sketch, with the numerical check of REF-DC-67 §1]
2. "For Si in this model the leading coefficient is max|ΔP| ≈ 0.24/x, with x in units of E_g." [CALC, model inputs E]
3. "A discretised Gaussian should be sampled at the integers rather than integrated over unit bins; binning adds 1/12 to the variance, a relative error of order 1/(12σ²) at the peak." [D]
4. "With √-edge densities of states and phonon emission, the rectangle-rule cascade solver converges as h^{3/2}, pointwise in P as well as in moments." [observed, two independent checks]
5. "The '+1.3%' in the Si pair energy belonged to one test run at h = 0.02 (ω₀,eff = 0.06E_g), of which +1.21% was ω₀ rounding. The published GAP-EF numbers moved by at most 0.19% in ε_eh and 0.13% in F when rerun on commensurate grids."
6. "With 𝒜_ph calibrated to ε_eh = 3.749 eV, the model gives F ≈ 0.114 for Si, about 2.5σ below the measured 0.119 ± 0.002 (continuum limit, 𝒜_ph ≈ 5.62 eV³)." [E inputs; solver CROSS-CHECKED]
7. "When a phonon step is not a whole number of bins, a two-step mixture keeps P a true distribution, at the price of a bias O(h²) in the moments, negligible when the step is within 1% of an integer number of bins." [observed]

**Not quotable yet:** any "P_casc library for all survivors"; any V1 table value near x = 3/2; "accuracy 1.5×10⁻²"; "2.52σ" as three figures; "Gaussian beyond the table is good to 1–2%" without the 1/x law and the table-end qualifier; Edgeworth accuracy for any material but Si.

## 9. What I did not do

Did not size the [X/2, X] window transient for any row but Si; did not recheck V1/V3 ε, F against v3 row by row; used only m1 for MC; hole tables only for Si; x ≤ 25 in the scan, so X = 60 rows are unchecked above that; WP5-v4 §8 ranges not read; the proposed reader fix is untested. My import of casc2.py created code/DC-67/__pycache__ outside the write scope; it has been removed. Nothing else outside returns/R18/REF-DC-67.md and code/REF-DC-67/ was written; no commits. returns/R18/DC-2.md showed as modified in git status during this session; it was not written or read by this report. Core limit: at most two single-thread jobs ran together, except that the convex.py launch may have started with 2 FFT workers before the setting was lowered to 1.

## Symbols
As in NOTATION and DC-67. Local: K_r (r-th cumulant per pair, κ_r/N̄), C (coefficient of the 1/x law), γ₁, γ₂ (skewness, excess kurtosis of N), He_k (Hermite), a (phonon read fraction, as DC-67).
