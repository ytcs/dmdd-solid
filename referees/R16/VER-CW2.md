# R16 VER-CW2: hostile referee report on returns/R16/CW2.md (LE-48 … LE-72)

Read: returns/R16/CW2.md, code/CW2/ (checks.py rerun: **24/24 PASS**; ld1/*.in, *.out, results.json inspected), LIMITS.md, CONVENTIONS.md §1, §9,
returns/R12/WP7-B2-v2.md (definitions of C^{IR}, σ_w, ϑ_I, the 0.11 factor). Full text fetched: 2603.13052, 2308.06314 (literature/papers-r16-VER-CW2/, PDFs deleted).
PhonoDark-abs at commit 0cbb3d5 read from raw.githubusercontent.com (pda/couplings.py, material.py, selfenergy.py). Independent checks: sympy/numpy (scratchpad v.py, < 5 s).
Not read: referees/R16/, other R16 returns, briefs/, log/LAUNCHES.

## 1. Verdict table

### 1a. Owed corrections and status upgrades (scope 1)
| Item | Verdict | Reason |
|---|---|---|
| OC-1 LIMITS L7c (2603.13052 (4.8) 2×, CONFIRMED) | STANDS | Re-read from full text (§2a). The (3.11) sign and 1/m_N items are carried over from R8 (IF-15); not re-verified here |
| OC-2 LIMITS B2-L1 (2308.06314 Fig. 2 rigid ion, RESOLVED) | STANDS WITH CORRECTION | The structure is confirmed from text and code (§2b). "High by ≈ 9" depends on the Z* input: Z* = 2.1 gives 8.6, and the return's own LST value Z* = 2.16 gives 6.8. Write "≈ 7–9" |
| OC-3 CORRECTIONS WP2-v3 §5.2″ (L shell) | STANDS WITH CORRECTION | Numbers reproduced (results.json). Two things to add: the values are NR, and SR lowers 𝔯 − 1 by 7% (Si) and ≈ 30% (Ge/Ga/As); "< 1%" holds for 𝔯 (0.6% at 300 keV), not for 𝔯 − 1 (1.2%) |
| OC-4 LIMITS B2-L3 (A^{IR}, B^{IR}) | STANDS WITH CORRECTION | The polarisation weights are wrong (§3, LE-64): ŵ_ν ∝ c_ν⁻³, not 1/3 |
| OC-5 LIMITS B2-L4 (wall pressure) | STANDS | (CW2.25) and R_slab = 2R/(1+R) re-derived (phase-averaged Airy reflectance 1 − 1/√(1+F) = 2R/(1+R)) |
| OC-6 LIMITS B2-L5 (Markov–Krein remainder) | STANDS WITH CORRECTION | Add that the band is absolute in the CDF with width ϱ ~ 𝔨₂²/(ξ−𝔨₁)⁴, i.e. power law, so it is not a useful relative bound on threshold-tail rates (§3, LE-52/70) |
| OC-7 LIMITS isotope bullet (mK ratio ≥ 6.3×10³; +9%) | STANDS | Weights 1+n₁+n₂ and n₂−n₁ re-derived; Debye h_iso(50 meV) = −1.718 and κ^M_1 = −0.0536 reproduced; the [E, Debye] label is correct |
| OC-8 CORRECTIONS WP7-B2-v2 §2.2 (O(σ_M/M̄)) | STANDS | (CW2.22) re-derived (§3, LE-65); keep "[E for D(ω)]" |
| OC-9 SOTA (2603.13052 UNRESOLVED → CONFIRMED) | STANDS | As OC-1 |
| OC-10 CORRECTIONS WP2-v3 §12 / LIMITS L5 ("0.16 [E] superseded by ℛ₂") | STANDS WITH CORRECTION | ℛ₂ has not been computed for any real crystal; only the 1D illustration (−0.34) exists. Write "0.16 [E] stands until ℛ₂ (CW2.4) is computed" |
| OC-11 J3/N1 P_Mig ≤ E_R(δM/M)/E_g | STANDS | Re-derived: ℐ₄ ≤ ℐ₃/E_g on the support Δ ≥ E_g, and E^{Mig}_1 = q²ℐ₃/M² = E_R δM/M |
| Status LE-63 UNRESOLVED → CONFIRMED | STANDS | §2a |
| Status LE-68 UNRESOLVED → RESOLVED | STANDS WITH CORRECTION | §2b; factor as OC-2 |

### 1b. New derived results (scope 3)
| Row / eq. | Verdict | Reason |
|---|---|---|
| LE-48 (CW2.1)–(CW2.4) | STANDS | Order-n term e^{Φ}→Φⁿ/n! at t = 0 checked; at T = 0 B ~ ΔR⁻², so the sum converges for n ≥ 2 and diverges for n = 1; C1a reproduced |
| LE-49 (CW2.5)–(CW2.6) | STANDS | Cauchy–Schwarz holds pointwise in Q before integration. (CW2.6) is correctly labelled as only holding up to gradient terms |
| LE-50 (CW2.7)–(CW2.8) | STANDS | Coefficient re-derived: (2n+1)/2ω → T/ω², Σ_ν(q̂·ê_ν)² = 1, ∫d³Q/(Q²\|k−Q\|²) = π³/k ⇒ T²q⁴\|S_G\|²/(16M²c⁴k). Exact match |
| LE-51 (CW2.9) + spec | STANDS WITH CORRECTION | Spec cutoff is wrong by 4× (§4) |
| LE-52 (CW2.10)–(CW2.11) | STANDS WITH CORRECTION | Moments and the Hermite check ϱ = 2/3 are correct. The "narrow in the tails … sets low-mass reach" claim is an overclaim; the spec gives no convergence parameters (§4) |
| LE-53 (CW2.12) | STANDS WITH CORRECTION | The parenthetical claim that (CW2.12) is "exact … configurational average enforces uniaxiality" is **false** (§3) |
| LE-54 (CW2.13) [CALC] | STANDS WITH CORRECTION | Algebra and units (HL, e² = 4πα) reproduce 1498 eV² (Si). n_e is taken at r_min, not 0 (−0.18%, unstated). The SR caveat is mis-scoped (§0) |
| LE-55 (CW2.14)–(CW2.15) | STANDS | δM = 2ℐ₃, E₁ = q²ℐ₃/M², P = q²ℐ₄/M², E₃ = q²ℐ₁/M², and the ω² slope of Φ^{el}(ω) all re-derived; Sternheimer components −M/Δ, −M/Δ² give ℐ₂–ℐ₄; 4.3 eV and 3.1 eV reproduced |
| LE-56 (CW2.16) [CALC] | STANDS WITH CORRECTION | FT[(3μ²−1)/ρ³] = −4π(μ_k² − 1/3) verified (∫j₂/x = 1/3). The "single missing step" fails for Ge/Ga/As (§4) |
| LE-57, LE-58, LE-60, LE-61 (specs; C9, C19) | STANDS | Specs complete: what, level, method, convergence, pitfalls. C9 inputs remain [UNVERIFIED] as labelled |
| LE-59 (CW2.17)–(CW2.18) | STANDS | Euclidean vertex −4!ℓ⁸/(2ω) re-derived (= −0.75 at ω = 1). TR ⇒ S even in q, so terms linear in a degree-3 W₃ vanish. Contour placement in (CW2.17) not independently re-derived |
| LE-62 (CW2.19) | STANDS | Cauchy–Schwarz bound re-derived; Si 0.494 (ω/1 eV)² reproduced in a.u. (Ω = 270.3 a₀³, δM = 14 m_e) |
| LE-64 (CW2.20) | STANDS WITH CORRECTION | ŵ_ν (§3) |
| LE-65 (CW2.21)–(CW2.22) | STANDS | Dyson for M_I = M̄(1−δ): G_II = 𝒢/(1+δM̄ω²𝒢); O(δ) gives h = −1 − 2M̄ω²Re𝒢; weighting M_I(ϑ−ϑ̄)² matches σ_w of (B2.4.2); first-order cross terms vanish because ⟨δv_J⟩ = 0 |
| LE-66 (CW2.23) | STANDS WITH CORRECTION | Inequality correct under its stated hypotheses; spec lacks convergence (§4) |
| LE-67 (CW2.24) | STANDS WITH CORRECTION | LST in HL correct; |Z*| = 2.160 reproduced in SI. But C14 computes d with Z* = 2.1, not with the return's own 2.16: d = −1.18×10⁻³ vs −1.33×10⁻³ (rate +27%, beyond the return's own 20% target). Quote d for both, or for the LST value |
| LE-69 (CW2.25) | STANDS | Checked: sign, 2ρv_n²R and the scale 5×10⁻¹¹ Pa / 10⁻¹² m s⁻² |
| LE-70 | STANDS WITH CORRECTION | As LE-52 |
| LE-71 (CW2.26) | STANDS | O(k) counting checked: the G = 0 term is k²·Ze²/k² times a dipole O(k) matrix element; the Umklapp terms are k·G 𝒲_G times O(1). C17 is correct |
| LE-72 (CW2.27) | STANDS WITH CORRECTION | Definition of M and the nilpotency claim need fixing; the gap spec is insufficient (§4) |

## 0. [CALC] ld1.x atomic runs (scope 0)
- **Setup.** iswitch = 1 (AE), point nucleus, rel = 0/1, PBE/PZ, xmin = −7, dx 0.008/0.006, rmax 100/60. Configurations are correct (Ga 4p¹, As 4p³, spherical average). SCF converges to 6×10⁻¹⁵; N_el = Z to 3×10⁻⁵.
- **Convergence claim is overstated.** "𝓃_e(0)" is the density at the first grid point r_min = e^{xmin}/Z, not at r = 0. The NR cusp n(r) ≈ n(0)(1 − 2Zr) puts it low by 2Zr_min = 2e⁻⁷ = **1.8×10⁻³**, the same for all species.
  Check: n(r₀)/n(r₃) − 1 = 4.5×10⁻⁵ for Si, which equals 2Z(r₃−r₀). The dx test (3×10⁻⁸) does not vary xmin, so it cannot see this. Si n(0) = 1769.5, not 1766.3 a₀⁻³. Harmless at the stated precision, but "N_el to 10⁻⁵, grid 3×10⁻⁸" should not be read as the accuracy of 𝓃_e(0).
- **SR +50% caveat: wrongly scoped.**
  (i) The SR point-nucleus density diverges. The data give d ln n/d ln r = ln(33513/33557)/0.024 = −0.055 for Ge, matching 2(γ−1) = −0.0554. So +49% (Ge), +46% (Ga), +53% (As) are values at r_min ≈ 1.5 fm, inside the nucleus (R_N ≈ 4.7–5 fm). They are grid-dependent, not a property of the atom.
  At r ≈ R_N the SR excess is ≈ (R_N/r_min)^{−0.055} × 1.49 ≈ 1.40. Quote "≈ +40–50% [E], r_min-dependent". The Si +7.8% is robust: the exponent is −0.0105 and r_min = 3.4 fm ≈ R_N.
  (ii) "(5.2′) must be re-derived with a finite nucleus **and the Dirac current**" overstates the remaining work. 𝔨₃ comes from the double commutator with the NR nuclear kinetic energy, so it involves only ∇²_R of the e–N Coulomb potential. For Dirac–Coulomb electrons, the e⁻ kinetic term is R-independent and the identity is unchanged. With a finite nucleus, Ze²𝓃_e(R)/3 → Ze²∫𝓃_e ρ_N/3.
  What is owed is a relativistic finite-nucleus **density** averaged over ρ_N, not a new derivation. Breit/magnetic terms are a further, smaller correction.
  (iii) Scope omissions. The same factor (−30%) hits the §9 𝔯 table for Ge/Ga/As and therefore OC-3, LE-56 and IF-CW2-9. The §9 "missing step" ignores it (§4).
  IF-CW2-2 and CW2-L1 should state that the NR coefficients for Ge/Ga/As are **low by ≈ 40%** (they are not an upper or lower bound in any controlled sense beyond that).

## 2. Published-paper claims (scope 2)
**2a. 2603.13052 Eq. (4.8): CONFIRMED.** Full text, p. 13 below (4.5): "(c_i)² = πσ_n^{(i)}/μ²_χn", with c the coefficient of the NR four-field operator (Eq. (2.1), p. 3). This is the standard Born σ_n = μ²c²/π.
p. 15, (4.8): dσ/dq = q/(μ²_χn v²) Σσ_n F_{i,j}. App. A.6: F_{1,1} = F_M, which in Fitzpatrick normalisation is F_M(0) = N² for neutron coupling. The standard result is dσ/dq = qσ_nN²F²/(2μ_n²v²), so (4.8) is **2×**.
Rate: (4.6) carries 1/m_N and (4.7) carries 2αq²/(3ω⁴m_N), giving the product (4αq²/3m_N²ω⁴) × (q/2μ²v²) = KKL × standard. Reproduced (C10 sympy); the rate claim stands.
p. 18: (4.9) λ⁻¹ = n_E∫₀^{2m_χv}dq dσ/dq, and "σ(v) is obtain[ed] by integrating Eq. (4.8)". As printed, the mean free path is half the standard value, as the return says. Minor: the upper limit printed is 2m_χv (≈ 2μ_χN v for m_χ ≪ m_N), which does not affect the factor.
**2b. 2308.06314 Fig. 2: RESOLVED (rigid ion).** p. 20: Eqs. (40)–(41) use N_jψ and Q_jψ T with the mixing −ωq(1−ε∞)g_e/e. p. 21: "consider only coupling to the electron number … N_Ga,e = 28, N_As,e = 36". Footnote 2 (p. 19) gives the δZ fix only as an option.
Code at 0cbb3d5 confirms it:
- couplings.py ScalarE: `Nj = self.mat.get_Nj()`, `Fe = einsum(Nj, qmag, qhat)`, mixing `ce*(1 − tr ε/3)/E_EM·qω`.
- material.py get_Nj: Z − pymatgen oxidation state.
- selfenergy.py get_photon_se: `charge_list = Z_list − get_Nj()`.

No Born charges enter the vertex. Quoted line numbers are within ±2 of what I read. Caveat kept: later commits not examined (the GitHub API did not return history).
Factor: the effective rigid vertex is Z − Q/ε∞. The rate ratio (d_rigid/d)² is **8.6 at Z* = 2.1** and **6.8 at Z* = 2.16** (v.py). Replace "≈ 9 (g_e ≈ 3)" by "≈ 7–9 (g_e ≈ 2.6–2.9)".

## 3. Errors in derived results (detail)
- **LE-53 (CW2.12) exactness claim is false.** Counterexample: r̂ = ẑ, B = diag(B_T,B_T,B_L) + ε(x̂ẑ+ẑx̂). Then ⟨(q̂·B·q̂)²⟩_q̂ − [uniaxial formula] = **4ε²/15** ≠ 0 (sympy, at qr = 0). Averaging over orientations about r̂ does not remove ε².
  For n ≥ 2, (CW2.12) drops the variance of the non-uniaxial part of B_IJ. The averaged rank-2n tensor ⟨B^{⊗n}⟩_r has more invariants than ⟨(B_L−B_T)^k B_T^{n−k}⟩.
  Correction: "(CW2.12) holds if each B_IJ is uniaxial about r̂_IJ; otherwise use the direct pair sums of the spec (which are exact)". The spec is unaffected.
- **LE-64 (CW2.20) polarisation weights.** WP7-B2-v2 defines C^{IR}(ω) = ⟨|p_ν|²⟩_{ω_ν=ω}, a conditional average over modes at fixed ω. Branch ν has mode density ∝ ω²/c_ν³, so ŵ_ν = c_ν⁻³/Σ_ν′c_ν′⁻³: for 1L+2T, ŵ_L = c_L⁻³/(c_L⁻³+2c_T⁻³), not 1/3.
  The 1/3 from averaging over field polarisation belongs inside 𝒮^{(ν)}_Z. C11 is a single-branch 1D test and cannot see this. Fix (CW2.20), the A/B expressions and OC-4.
  Also unstated: the leading correction (non-plane-wave admixture below the Ioffe–Regel frequency, Rayleigh-type ∝ ω⁴ scattering).
- **LE-52/LE-70 tail claim.** The Markov–Krein band is absolute in F with width ϱ(ξ) ≈ 2𝔨₂²/(ξ−𝔨₁)⁴. A true threshold tail falls like a Gaussian or exponential, so near threshold the band bounds the rate only to O(1) relative accuracy or worse, by orders of magnitude.
  "Narrow in the tails, the threshold region that sets low-mass reach" must become "narrow in absolute CDF in the tails; not a relative bound on tail rates". §23 already says "bounds threshold-limited (tail) rates": same fix.
  The remainder inequality |F_exact − F_SCHA| ≤ |F_SCHA − F_canon| + ϱ is a triangle inequality and is correct.
- **LE-67.** Use one Z* throughout (§1b). With LST 2.16, d = −1.33×10⁻³ and +10% Z*/ε∞ → +41% (not 45%).
- **LE-54/56.** See §0 (r_min bias; SR scoping).
- **LE-72 (CW2.27).** As defined, M_{λλ′} = Σ(1+δ)Γ/Γ^{tot} gives full branching even for states with b_λ > 0. It must carry the decay probability (1 − p^{stable}_λ), and Σ_{λ″} must be over unordered pairs. Otherwise chiral-stable phonons are double-counted.
  "M nilpotent in energy order" fails once the Tamura (elastic isotope) channel in the spec is included. (𝟙 − M) is then invertible only through loss (boundary) terms; state this.

## 4. CLOSED-AS-EXACT-GAP rows (scope 4)
| Row | Single missing step? | Spec sufficient? | Verdict |
|---|---|---|---|
| LE-51 | Yes: Δ^{val} for 3–20 keV. Core negligibility rests on a hydrogenic [D] times a residual field ≈ 10⁻² a.u. [E], so the core part is [E], not [D], for real cores. The AE spec covers both | Mostly. Error: "ecutrho with \|G\|_max ≥ 1.5×20 keV (≈ 260 Ry)". 30 keV = 8.05 a₀⁻¹ ⇒ \|G\|² = 65 Ry; 260 Ry corresponds to 60 keV. This contradicts §7, where 250 keV ↔ 4700 Ry correctly uses ecutrho = \|G\|². Fix to ≈ 65 Ry (or justify 4× for the PAW AE reconstruction grid) | STANDS WITH CORRECTION |
| LE-52 | Yes: real-time anharmonic quantum dynamics | **No.** Gives what, level, methods and pitfalls, but no convergence parameters: beads, thermostat, Δt, trajectory length, cell size, the TRPMD vs CMD cross-check, the SSCHA dynamical ansatz order. It also names no system size or cost | STANDS WITH CORRECTION (add convergence block) |
| LE-56 | **No, for Ge/Ga/As.** The relativistic finite-nucleus density changes 𝔯 − 1 by ≈ 30% (§0). That is a second and much larger missing step than the valence anisotropy (≤ 1.3×10⁻³). For Si, yes (SR 7%: still to be flagged) | Spec level should read "AE, NR (Si) / scalar-relativistic finite-nucleus (Ge, GaAs)" | STANDS WITH CORRECTION |
| LE-66 | Yes (T = 0 two-phonon ε₂, or cold data) | Partly. Missing convergence: supercell size for the range of ∂Z*/∂u (2×2×2 only), ±u amplitude and linearity, q-mesh 32³ vs 48³, δ-smearing; no check against the 293 K curve (sum+difference) | STANDS WITH CORRECTION |
| LE-72 | The giant-moment amplitude is named as the gap | **No.** "CASSCF-SO on embedded clusters, ≈ 10³ CPU·h" with no level, embedding, active space, convergence or pitfalls; the return admits it is "not formulated beyond this pointer". The κ_URF half is spec'd | Giant-moment half: CANNOT-CLOSE unless a spec is supplied; κ_URF half STANDS WITH CORRECTION (§3) |

## 5. Proposed LIMITS rows (scope 5)
- **Format.** The table has only τ/chain, source, status. It lacks the validity and leading-correction columns that LIMITS v3 entries carry by reference. Add them (values below).
- **Sources.** None of CW2-L2–L5 was read in full text: Warren 1969, Lifshitz, LST/Born–Huang, Akhiezer 1965 are all [UNVERIFIED]. Under the brief's criterion they cannot be entered as "source quoted from full text". They are acceptable only as DERIVED (campaign) rows with source "classical, not verified". The derivations themselves I re-checked (§1b).
- **CW2-L1.** Validity: leading BO order, cubic site, NR Coulomb, point nucleus. Leading correction: relativistic finite-nucleus density, **+8% (Si), ≈ +40–50% (Ge/Ga/As)**; then O(⟨ω_ph⟩/ω_e) from J8. The row as written omits this.
- **CW2-L2.** Validity: T ≫ ω near G only and q → G, c_min bound. Leading correction: regular part, O((T/ω̄)²) relative. Fine.
- **CW2-L3.** Exact for one defect; leading correction is pair terms, O((δ^M)²x). Fine.
- **CW2-L4.** HL form correct. Validity: one TO/LO pair (cubic, two atoms). Leading correction: T-dependence of ε∞ (2–3% [E]).
- **CW2-L5.** Validity: needs 𝓂₀–𝓂₄ exactly. Leading caveat: absolute CDF bound, power-law tail (§3).

## 6. Minor
- §16: "(arXiv HTML numbers it Eq. (22))": not checked; irrelevant.
- §9: notation collision. 𝓃_e(G) (Fourier coefficient) and 𝓃_e(R_κ) (contact density) share a symbol; "2𝓃_e" at G = 0 means 2n̄. Add a NOTATION row or rename.
- §19: the quasi-harmonic shift is listed as "≲ 1%" in frequency, but α(ω) near structured two-phonon features can change by more than 1% at fixed ω. The inequality (CW2.23) should be stated as holding up to the shift ω → ω(1 ± 1%).

Counts (table rows, scope 1–3): STANDS 17, STANDS WITH CORRECTION 16, FALLS 0. One sub-item downgraded: LE-72 giant-moment half to CANNOT-CLOSE.
