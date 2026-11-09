# App. C.10–C.14 acceptance review, part 1: derivation check (isolated)

Reviewer: derivation verifier (long-form-writing SKILL.md §5). Date 2026-11-07.
Scope: tex/appC/C-10.tex … C-14.tex; NOTATION.md; STYLE.md; SPINE App. C rows C.10–C.14.
Method: every non-definitional step redone by hand and with sympy/numpy (scripts kept in the session scratchpad, not in the book);
dimensions checked on every displayed result; every number recomputed; every chapter use of `app:C.1n` / `eq:C.1n-…` grepped in
tex/ch*/, tex/appD, tex/appE, tex/appF and compared in form and convention. Source: Cowan et al. 1007.1727 fetched with lit.py into
sources/review-appC2/ (PDF deleted after the check). The books (Krein–Nudel'man, Akhiezer, Harris, Feller) and Rogosinski, Shapiro,
Fishburn, Wilks are not open; checked against the standard statements only.

Summary: 1 WRONG (mathematical statement, C.10), 2 WRONG (notation drift against NOTATION, C.12 and C.14), 3 GAP (minor), all
else CHECKED. Every chapter citation of a C.10–C.14 result finds it here, in the form and convention used.

## C.10 Moment problems

| Location | Verdict | Note / correction |
|---|---|---|
| eq:C.10-moments, eq:C.10-hankel (positivity, Hankel matrix) | CHECKED | c^T H c = ∫p² dP; PD unless support ≤ 2 points. |
| ¶ after eq:C.10-hankel: H₁ (μ_{i+j+1}), sufficiency up to boundary cases, Carleman | CHECKED | Standard (Krein–Nudel'man). |
| eq:C.10-kernel, eq:C.10-reproduce | CHECKED | a^T H H⁻¹ v(ξ) = q(ξ). |
| eq:C.10-rho and the Lagrange minimization; point-mass bound w ≤ ϱ_MK | CHECKED | min c^T H c s.t. c^T v = 1 is 1/(v^T H⁻¹ v). |
| Three real distinct roots of r(x) = (x−ξ)K(x,ξ) | CHECKED | Orthogonality to linears ⇒ ≥ 2 sign changes; ξ simple since K(ξ,ξ) > 0. Leading coefficient e₂^T H⁻¹ v(ξ) is a nonzero quadratic in ξ, so "at most two roots" holds. |
| eq:C.10-quadrature, positive weights, w_ξ = ϱ_MK(ξ) | CHECKED | Division f = rs + t valid for deg f ≤ 4; f = K(·,ξ)² gives w_ξ K² = K. |
| eq:C.10-band (key result) and the majorant U for ξ = y₁, y₂, y₃ | CHECKED | ξ = y₂ quartic: five conditions, Rolle root c ∈ (y₁,y₂), U′ = A(x−y₁)(x−c)(x−y₃), A > 0, shape argument correct. Mirror argument for the lower bound correct. |
| Gaussian H⁻¹ = [[3/2,0,−1/2],[0,1,0],[−1/2,0,1/2]] | CHECKED | sympy. |
| eq:C.10-gauss ϱ_MK = 2/(3+ξ⁴) | CHECKED | sympy. Dimensionless (ξ in σ units). |
| Nodes 0, ±√3, weights 2/3, 1/6, 1/6; 1/6 ≤ F(0) ≤ 5/6 | CHECKED | sympy. |
| eq:C.10-tail: det H = μ̄₂μ̄₄ − μ̄₃² − μ̄₂³, (H⁻¹)₂₂ = μ̄₂/det H | CHECKED | sympy. Dimensions x⁴/x⁴. Shift invariance of K(ξ,ξ) is used implicitly (span{1,x,x²} is shift-invariant); fine. |
| Gaussian numerator 3 − 1 = 2 | CHECKED | |
| Gamma(3): exact ϱ_MK exceeds tail form by 4.1 % at 58σ, 1.3 % at 173σ | CHECKED | 4.08 % and 1.35 % on the upper side. On the lower side (−58σ) the exact value is 3.9 % *below* the tail form. Suggest "at 58 standard deviations above the mean". |
| Gaussian 3σ: 1−F = 1.35e-3; band [0, 2.38e-2]; ratio "eighteen"; 4σ ratio "240" | CHECKED | Canonical nodes through ξ = 3: −1.319, 0.569, 3 (ξ is the largest node, so the lower end 0 is right); ϱ = 2/84 = 0.02381; ratio 17.6; at 4σ 2/259 / 3.167e-5 = 244. |
| eq:C.10-stieltjes (half-line point-mass bound) | CHECKED | w ξ p₁(ξ)² ≤ ∫x p₁² dP, minimized: [ξ u^T H₁⁻¹ u]⁻¹. Dimensionless (checked under x → λx). |
| C-10.tex l. 101: "The second entry is small at small ξ, where the half-line constraint bites" | **WRONG** | As ξ → 0⁺, ξ u^T H₁⁻¹ u → 0, so the second entry diverges; at large ξ it falls only as ξ⁻³, slower than ϱ_MK ∝ ξ⁻⁴. Numerically (gamma(3): 12.2 vs 0.105 at ξ = 0.05; Si 100 keV: 1.52 vs 0.082 at 0.1 E_R) it is weaker than ϱ_MK near the origin and in the tail. It bites at intermediate ξ: for silicon at 100 keV it is below ϱ_MK by at most 6.8 % at ξ = 0.74 E_R, inside the window 0.65–0.85 E_R where a canonical node is negative, exactly as Sect. 11.5 states. Correction: "The second entry diverges as ξ → 0 and falls only as ξ⁻³ in the tail, so it is weaker than ϱ_MK near the origin and far out; it bites at intermediate ξ, where a node of the canonical representation through ξ lies below zero (Sect. 11.5)." |
| "For ξ < 0 the band collapses to F_P = 0" | CHECKED | |

Uses of C.10:
- 11.5 l. 7, 80, 82, 91, 94, 112; 11.9 l. 11; F-rows l. 272–275: band, ϱ_MK, Gaussian 2/(3+ξ⁴), tail coefficient μ̄₄ − μ̄₂² − μ̄₃²/μ̄₂,
  kernel, Stieltjes bound — all present in the same form. CHECKED. Spot-recomputed the 11.5 numbers that rest on C.10: Si 100 keV
  canonical nodes 59.8, 191.1, 371.3 meV, weights 0.191, 0.670, 0.139; tail numerator 3.333 − 1 − 0.553² = 2.03; half-line shrink
  6.8 %. All reproduce. 11.5 l. 91 ("there the half-line bound is smaller than ϱ_MK") is right and contradicts C.10 l. 101 (above).

## C.11 Generating functions, branching and renewal

| Location | Verdict | Note / correction |
|---|---|---|
| Opening: 100 eV → about 27 pairs | CHECKED | 100/3.75 = 26.7. |
| eq:C.11-pgf, eq:C.11-var | CHECKED | |
| Poisson PGF e^{N̄(s−1)}, Var = N̄; Si Fano 0.1–0.15 (Sect. 1.5) | CHECKED | 1.5 l. 21 states 0.1–0.15. |
| eq:C.11-thin, eq:C.11-thinfano F_k = fF + 1 − f | CHECKED | sympy: Var_k = f²VarN − f²⟨N⟩ + f⟨N⟩. |
| eq:C.11-gw both forms; ⟨N_n⟩ = m̄ⁿ | CHECKED | First form derived as stated; second by associativity of composition. |
| Extinction key result, minimal-root argument, convexity argument | CHECKED | |
| Toy law 1 − p + ps²: roots 1, (1−p)/p; p = 0.6 → 2/3, survival 1/3 | CHECKED | |
| eq:C.11-functional, eq:C.11-mean, eq:C.11-second | CHECKED | Expansion of (d + ΣY_j)² with independent subtrees reproduces all four terms. |
| eq:C.11-renewal | CHECKED | |
| eq:C.11-key (Feller XI.1) | CHECKED | Hypotheses (nonlattice, finite mean, z d.R.i.) as stated. |
| eq:C.11-undershoot: z(E) = Θ(E−y)[1−F(E)]; mean ⟨X²⟩/2⟨X⟩ | CHECKED | Integration by parts correct. |
| Overshoot via Wald and key theorem; eq:C.11-linear N̄ = E/⟨X⟩ + ⟨X²⟩/2⟨X⟩² − 1 | CHECKED | Dimensionless. |
| CLT step and eq:C.11-fano Var N ≈ σ_X²E/⟨X⟩³ | CHECKED | P(S_n > E) = Φ(u) with the stated n. Dimensionless. |
| Limits: deterministic loss → Fano 0; exponential → 1 | CHECKED | |
| Uniform [0,1]: ⟨E_res⟩ = 1/3, offset −1/3, Fano 1/3 | CHECKED | Renewal equation solved numerically at E = 20: offset −0.333333; simulation 2e5 chains at E = 50: 0.3326, −0.3307, 0.3365 (within 1 %). |
| Deterministic loss: −{E/d}, average −1/2 = d²/2d² − 1 | CHECKED | |
| Knock-on tail x⁻² up to E/2: ⟨X²⟩ ∝ E | CHECKED | |

Uses of C.11:
- 20.1 l. 92, 108; 18.3 l. 121; F-rows l. 846–848: binomial thinning fF + 1 − f. CHECKED.
- 18.1 l. 72; D.43 l. 24, 38, 49: functional (D.43 uses s = e^λ for the exponential form; consistent), mean and second-moment recursions,
  toy law with p > 1/2 converging to (1−p)/p. CHECKED.
- 18.2 l. 26, 65, 79, 109, 138, 156; F-rows l. 715, 722: second moment, Var N ≈ σ²ω/ε³ (C.11-fano with loss E_g + c), linear law,
  periodic remainder of a lattice chain. CHECKED.
- 18.3 l. 86–93: renewal limit; step-model mean (ω−E_g)/ε + 1/2 = ω/ε + 0.19 uses the −1/2 average of C.11. Recomputed: 0.5 − 1.16/3.75 = 0.19. CHECKED.
- D.44 l. 3, 48, 58: key theorem, undershoot law, lattice remainder. CHECKED.

## C.12 Linear programming and duality

| Location | Verdict | Note / correction |
|---|---|---|
| eq:C.12-weak; finite strong duality | CHECKED | |
| At most n nonzero components at an optimum | CHECKED | Argument correct (A d = 0, c^T d = 0 by optimality, slide to a zero). |
| eq:C.12-sip, g_λ | CHECKED | |
| eq:C.12-certificate | CHECKED | |
| eq:C.12-mass, κ_v, discarding mass off supp f, Slater | CHECKED | Σk_i ≥ max_i k_i ≥ κ_v on supp f uses k_i ≥ 0. |
| "Optimal halo is a sum of at most n streams [Rogosinski]" | GAP (minor) | Rogosinski's theorem applied to the n+1 functionals (k_1…k_n, f) gives a measure with at most n+1 atoms and the same counts and objective; n follows only after applying the finite argument above to that atomic measure. Add: "…with the same counts and objective on at most n + 1 points, and the finite argument above removes one more." |
| Complementary slackness | CHECKED | |
| eq:C.12-onebin | CHECKED | κ_v > 0 makes k₁ > 0 on supp f, so the sup is attained on the compact set. |
| eq:C.12-leak | CHECKED | g ≥ −L_h h by Lipschitz on the convex ball; then ∫f dΞ ≤ Σλ_h,i N_i + L_h h Ξ(supp f) ≤ … + L_h h N_tot/κ_v. Dimensions match the objective. |
| Negative-kernel paragraph | CHECKED | |
| C-12.tex l. 43 and l. 49: stream masses c_a, "c = N₁^up/k₁(w_*)" | **WRONG (notation)** | NOTATION entry 93(a) / row ξ_a: c_a → ξ_a (c is the speed of light); 21.2 and D.46 already write ξ_a. Rename c_a → ξ_a and c → ξ₁ (as D.46 l. 54). |

Uses of C.12:
- 21.2 l. 3, 20, 22, 44, 106; D.46 l. 3, 54, 56, 60, 69; F-rows l. 918: program, certificate, one-bin value (21.2 and D.46 use
  N_i^up/inf_{v≥u₀} A_i(v), which is C.12-onebin with f/k = 1/A — consistent), mass bound, bracket with δ_cert = L_h h. CHECKED.
- E.27 l. 7 writes the same program as 𝔎_i, F, 𝔥 with dual weights ξ_i and states the dictionary. Note (outside the scope of C.12):
  ξ_i = dual weights in E.27 clashes with ξ_a = stream masses in 21.2/D.46/NOTATION; flag for the E.27 owner.

## C.13 Interval orders

| Location | Verdict | Note / correction |
|---|---|---|
| Strict partial order, asymmetry | CHECKED | |
| eq:C.13-order: irreflexive, transitive | CHECKED | |
| Example [3,5], [2,4], [1,2.5] | CHECKED | |
| Interval-order (2+2-free) property and its proof; Fishburn representation; semiorder = equal lengths | CHECKED | |
| eq:C.13-height; tiers are antichains; tier k > 1 lies below a member of tier k−1 | CHECKED | |
| Sorting algorithm (decreasing u) | CHECKED | b ≻ a ⇒ u_b > u_a strictly, so ties are harmless. |
| Example A [8,10], B [5,9], C [6,7], D [1,9.5]: tiers {A,B,D}, {C}; midpoints 5.25, 6.5 | CHECKED | |

Uses of C.13: 17.6 l. 44, 66: order and height as defined; the two tier statements of 17.6 match C.13. CHECKED.

## C.14 Likelihoods, intervals and profiling

| Location | Verdict | Note / correction |
|---|---|---|
| N₉₀ = 2.303 (eq:1.5-N90) | CHECKED | ln 10. |
| eq:C.14-poisson; Cowan et al. Eq. (6) for the binned product | CHECKED | 1007.1727 Eq. (6) is the binned likelihood. |
| eq:C.14-gauss; Gaussian limit width N_obs^{1/2}; cubic term relative order N_obs^{-1/2} | CHECKED | sympy: −δ²/2n + δ³/3n²; at δ = √n the ratio is (2/3)n^{-1/2}. |
| eq:C.14-ratio; Cowan Eq. (8) | CHECKED | Cowan's t_μ (8) is the profiled form; without nuisances it is eq:C.14-ratio. Fine. |
| Coverage 2Φ(z) − 1; Wilks; Cowan Sect. 3.1 | CHECKED | Sect. 3.1 is "Approximate distribution of the profile likelihood ratio" (Wilks, Wald). |
| eq:C.14-thresholds 1.00, 2.71, 3.84; z = 1, 1.645, 1.960 | CHECKED | 1.6449² = 2.706, 1.9600² = 3.842. |
| One-sided: Cowan Eq. (14); z = 1.282, 1.645 → t = 1.64, 2.71 | CHECKED | Eq. (14) is q_μ, zero for μ̂ > μ. |
| N_obs = N_bkg = 0: t = 2N_sig, 0.82 vs 2.303 | CHECKED | |
| eq:C.14-profile; Cowan Eq. (7) | CHECKED | |
| Gaussian offset: θ̂̂ = rσ_ϑ²/(σ_N² + σ_ϑ²); eq:C.14-quadrature | CHECKED | sympy. Normalization nuisance to first order: relative widths in quadrature, correct. |
| Monte Carlo: 16th/84th percentiles, Φ(−1) = 0.159 | CHECKED | 0.1587. |
| eq:C.14-pairwise; example Φ(0.94) = 0.83 | CHECKED | 0.3/0.3202 = 0.937, Φ = 0.826. |
| Sampling error ≤ 0.0035 at N_MC = 2e4 | CHECKED | 0.003536. |
| σ_N throughout C.14 (width of N̂) | **WRONG (notation)** | NOTATION row "N̂, σ_N̂, σ_ϑ" and entry 74: σ_N is the nucleus cross-section of 1.4; rename σ_N → σ_N̂ "at the C.14 review". Not yet applied (eq:C.14-gauss, eq:C.14-quadrature, the profiling example). |
| Wording "Φ the standard normal distribution function" | CHECKED | Matches NOTATION Φ(z). |

Uses of C.14:
- 8.8 l. 106–108: profile (Cowan Eq. 7), normalization nuisance as Gaussian offset with σ_ϑ = ln(1+δ), quadrature, t* = 2N₉₀ = 4.61 from t = 2N_sig. CHECKED.
- 10.10 l. 77; 11.9 l. 79: quadrature of independent standard-normal ϑ_k. CHECKED.
- 14.6 l. 147: ratio and thresholds. CHECKED.
- 17.2 l. 92: t = 2.71 as the one-sided 95 % level. CHECKED.
- 17.6 l. 35, 47, 89: N_MC = 2e4, error ≤ 0.0035, pairwise formula; TeO₂/GaAs Φ(0.242/0.122) = 0.977 recomputed (0.242/0.1216 = 1.99, Φ = 0.977). CHECKED.
- 19.4 l. 85: one-sided f̂ + 1.645σ = 0.0638. CHECKED.
- 21.4 l. 36, 53; 21.5 l. 20, 24, 36; D.47 l. 11: profile statistic set to zero above the best fit (C.14 one-sided rule), Poisson product, asymptotics invalid at low counts. CHECKED.

## Cross-cutting

| Location | Verdict | Note / correction |
|---|---|---|
| SPINE App. C rows, "Used by" | GAP (SPINE, not tex) | Actual users exceed the lists: C.10 also 11.9; C.11 also 18.3, 20.1, D.43, D.44; C.12 also D.46, E.27; C.14 also 10.10, 11.9, 17.2, D.47. Update the SPINE rows. |
| NOTATION rows for C.10–C.14 locals (𝐇, 𝐇₁, 𝖪, ϱ_MK, 𝔊_N, 𝔤, P_ext, F_loss, E_res, Ξ, 𝓑, 𝗄_i, 𝖿, 𝗀_λ, λ_i, N_i^up, κ_v, ≻, h(a), 𝖫, 𝗍, 𝗍_p, ϑ̂, ϑ̂̂, Φ) | CHECKED | Used as listed, apart from the two renames above. |
| ϱ_MK row "first use 11.5" | GAP (minor, NOTATION) | Defined in C.10 (eq:C.10-rho); add "C.10 (also 11.5)" as for μ_k. |
| Dimensional analysis of all displayed results | CHECKED | All dimensionless or homogeneous as stated. |
