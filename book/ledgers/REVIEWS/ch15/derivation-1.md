# Ch15 part 1: derivation check (s15-1, s15-2, D-39; ch15.tex)

Reviewer: derivation verifier, isolated, 2026-11-06. No tex edited, nothing committed, no QE run.
Method: sympy for the algebra; a new implementation of eq:15.1-Rcons (scipy and mpmath, with the substitution s = s* ∓ t²; it
imports nothing from bcs15.py) for every loss-function number; a new rate integral (own SHM η, own prefactor) for WE 15.1.
Scripts are in the session scratchpad under r15/ (core.py, sbcs.py, edge.py, scan.py, checks2.py, sumrule.py, pole.py,
offedge.py, rate.py, frac.py, mpcheck.py, sym1.py). Sources fetched to sources/review-ch15/ (arXiv 2609.06423, 2109.04473,
2101.08263, 1512.04533, cond-mat/9604124, 2305.06084); the PDFs are deleted. Not on arXiv, so not checked: Anderson 1958,
Mattis–Bardeen 1958, Allen 1971.
Base: v_max/v_F = 2.650e-3/6.67e-3 = 0.3973 unless stated.

## Summary
- WRONG (fix): 6 items. (1) The one-sided edge-remainder nuisance (15.2-nuisance). (2) Grid-artefact thresholds in the
  lim:15.1a caption and text (9.4/8.2/6.5/2.3/0.049). (3) The Lindhard-limit figure 3e-5 (15.1 l.76). (4) The bulk y<3
  fraction 18 % in WE 15.1. (5) Gan "Sect. IV" for the (Δ/v_Fq)² estimate and the 5Δ statement. (6) The AB pole given as the
  reason the ladder is large at y = 3 (15.2-cons).
- GAP (wording, precision, notation): about 14 items, listed below.
- CHECKED: everything else, including all PRIORITY items. Details follow.

## PRIORITY items (editor notes, ch15 and partII)

P1 eq:15.1-Rcons, derivation → CHECKED.
  sympy confirms each identity used: |M_η|², |M_s2|², the product (uv'+vu')(uu'+vv') = Δ/2E + Δ/2E';
  (EE'+ξξ'+Δ²)(EE'−ξξ'−Δ²) = Δ²(ξ'−ξ)²; eq:15.1-ident.
  sinh substitution: W = 2Δ cosh A cosh B, s = 2Δ cosh A sinh B, W² − s² = 4Δ² cosh²A, and dξ W/EE' = 2 dA at fixed s
  (numerically exactly 2).
  The partial fractions of l.58 hold. The normalization ∫dA/(2cosh²A) = 1 holds.
  F_μ closed form: checked numerically for p<0 and 0<p<1. Its p>1 continuation, with Im F_μ < 0, was checked against the
  t-integral at p + iε.
  Bubbles: re-derived R⁰_ηη, R⁰_s2η = 2iΔω⟨F⟩ and R⁰_s2s2|^{q,ω}_{0,0} = ⟨ω_μ²F_μ⟩ from eq:15.1-bubble.
  Ladder: from eq:7.2-Rc with K = diag(0, −V/2, −V/2), it is −4Δ²ω²⟨F⟩²/⟨ω_μ²F⟩. The sign does not depend on the ±i phase
  of M_s2.
  Neutral denominator ⟨ω²−v²q²μ²⟩ → c_AB = v_F/√3 ✓. Dimensions: R in eV², F_μ dimensionless ✓.
P2 Checks of eq:15.1-Rcons (15.1 l.76) → CHECKED, except for one number.
  q = 0 cancellation: P_cons = 3e-13 at Q = 1e-6 (y = 1, 2.5, 5).
  f-sum: P_cons/(Q²/3y²) = 1.000013 at Q = 0.01 ("one to 1e-5" ✓).
  Static limit: P_cons = −1.000000 (Q = 1, 5, 50).
  Lindhard limit → WRONG number. At x = 0.397, |P_cons − P_nor|/|P_nor| = 6.2e-5 at v_Fq = 1e3Δ and 8.2e-7 at 1e4Δ (mpmath,
  30 digits). REF-DC-41 has 8.6e-7 at x = 0.39. The printed "3e-5 at 1e4" is the quadrature floor of bcs15.P_resp(n=16):
  tab15_1.log l.31 gives 2.94e-5 at 1e4, which is below its own 6.6e-5 at 1e3 by only a factor 2.
  Fix: "to 6e-5 at v_Fq = 10³Δ_BCS and 1e-6 at 10⁴Δ_BCS".
P3 Bare absorptive part = 𝔤_I × Lindhard (eq:15.1-gI) → CHECKED.
  The Im R⁰_ηη display was re-derived (μ → ω_μ). Im P_bare/Im P_nor − 𝔤_I ≤ 3e-12 at all edge points.
  Elliptic form (modulus k, i.e. scipy parameter k²) = angle integral = the E-integral of eq:7.2-pairspec, to 1e-12.
  𝔤_I = 1.5002/1.3221/1.2111/1.1507/1.0505 at y = 2.2/3/4/5/10, and 𝔤_I(2⁺) = π/2 ✓.
  Large y: 𝔤_I − 1 = 0.0505 against (2ln2y−1)/y² = 0.0499 ✓.
  GAP (D.39, minor): the remainder is O(ln y′/y′⁴), not O(y′⁻⁴); (𝔤_I−1)y² − (2ln2y−1) grows from 7.9/y² at y = 20 to
  12.6/y² at 100. This has no effect on the tail term.
P4 First-order correction eq:15.1-sBCS (bare only) → CHECKED.
  The KK prefactor (2/π)·(π/2)(k_TF²/q²)/qv_F → (k_TF²/q²)(Δ/qv_F)𝔰 was re-derived. The first-order L was re-derived.
  𝔰_BCS from my own PV code: 6.013/4.014/2.823/2.034/1.053/0.501 at y = 2.05/2.2/2.5/3/5/10. Cut at y′ = y/x:
  4.853/2.907/1.808/1.138/0.431/0.132 ✓.
  𝔰(0) = 0: ∫₂^∞(𝔤_I−1) = 2.0000000000 ✓. 𝔰 > 0 on 0.1–50 ✓. 𝔰 − (π/2)ln[1/(y−2)] → 1.2136 ✓ (D.39, 15.2 log claim).
  WRONG/GAP (15.1 l.130): "approaches 5/y beyond (0.248 at y = 20)". y·𝔰 = 4.953, 4.938, 4.936, 4.935 at y = 20, 50, 100,
  200, which tends to π²/2 = 4.9348. Analytically the leading term is (2/y)PV∫₀^∞ ln t/(t²−1)dt = π²/(2y).
  Fix: "approaches π²/2y (0.248 at y = 20)".
  15.1 l.128, "four digits at v_Fq = 100Δ": bare shift×Q = 2.0338 against 2.0337 (y = 3), 1.0531 against 1.0529 (y = 5),
  0.5017 against 0.5011 (y = 10). → GAP: true at y ≤ 5 only; say "to 1e-3".
  Conserving shift×Q at y = 5: 0.954/1.048/1.053 at Q = 1e2/1e3/1e4 ✓.
  Maximum first-order term: 4.0 % (y = 10), 17 % (y = 5), 54 % (y = 3) ✓.
  Full bare at the y = 10 edge: 0.934 against 0.960. At 4× edge of y = 5: 0.953 against 0.958 ✓.
P5 Edge values 0.87/1.00/1.07/1.07/1.02 against DC-41 (REF-DC-41 §7 rules) → CHECKED.
  Mine at x = 0.397: 0.8683/1.0013/1.0721/1.0683/1.0230 (the book's 0.868/1.001/1.072/1.068/1.023).
  Mine at x = 0.39: 0.8660/0.9975/1.0679/1.0660/1.0224, which equals DC-41's 0.866/0.998/1.068/1.066/1.022 to the last digit.
  The DC-41 vs book difference (≤ 0.004) is the velocity ratio alone.
  Quoting rules: "screens less" is absent ✓. Pole not given L weight ✓. Films not given the clean table ✓. Threshold wording
  (L → 0 at 2Δ, 0.97 L^nor by y−2 = 0.03) follows REF §7 ✓.
  GAP (DC-RESULTS rule "ℓ_mfp scope in the same sentence"): 15.1 l.136 (the five clean edge values and "0.980–1.087") and the
  15.2-cons paragraph ("within 10 % for y ≥ 2.25 … peaks at 1.43") give clean values with no ℓ_mfp clause. Add "(clean;
  at y ≤ 2.5 valid for 𝔩_e ≳ 10 µm, \cref{sec:15.2-disorder})".
P6 y = 9.2 vs 9.4 (lim:15.1a caption) → WRONG in 15.1; 15.2 is right.
  Root-finder on the edge: L_bare/L_cons = 0.9 at y = 9.193. The other reading, L_cons/L_bare = 1.1, gives 9.73.
  The 9.37 of limit15_1a.log is a log-interpolation on a 14-point grid (8.152, 10.286). The same grid gives the companion
  numbers in that caption and in 15.1 l.153:
    Lindhard within 10 %: printed 8.2, i.e. Δ/qv_F ≤ 0.049 → 7.89 (Δ/qv_F ≤ 0.050) [L_nor/L_cons ≥ 0.9; 8.41 for
      L_cons/L_nor ≤ 1.1];
    at 4× edge: printed 6.5 → 6.26 [6.71];
    𝔤_IL^nor within 10 %: printed 2.3 → 2.247 [2.263]. 15.2 already prints 2.25.
  Fix: replace 9.4/8.2/0.049/6.5/2.3 by 9.2/7.9/0.050/6.3/2.25. Rerun limit15_1a with a root-finder, because its gray band is
  at y ≥ 8.2. State the one definition used (L_x/L_cons ≥ 0.9) in both sections.
  Related: 15.1 l.153 has "𝔤_IL^nor within 8 % for y ≥ 3" (= 1 − 1/1.087) and 15.2 has "at most 8.7 % at y = 3.6". Both are
  right but use opposite definitions; unify.
P7 D.39 resummation, and its overlap with 15.1 → CHECKED, with notes.
  eq:D.39-resum is an exact algebraic identity (sympy, 0). Its first-order expansion g[1 − 2δ − (g²−1)r²] holds (sympy) and
  reduces to eq:15.1-sBCS ✓.
  2δ_𝔰 = 0.647 and (𝔤_I²−1)r² = 0.420 at y = 3 ✓. The tail formula ∫_T^∞(2ln2y−1)/y² = (2ln2T+1)/T holds ✓. The step-J
  logarithm argument holds ✓.
  Sum rule: h = 2N_F/R^0 → 3ω²/(qv_F)² − 9/5 (from n_e = ⅔N_F m v_F² and the 3/5 moment) ✓.
  Mine: g(10³Δ) = −1.80003/−1.80005 and h(0) = −1.0000000 at qv_F = 5/12Δ. (2/π)∫_{2Δ}^∞ Im h/ω = 0.79997/0.79999 with no
  sub-gap term, against Lindhard 0.8000000 ✓.
  GAP (D.39): "against 1 + δ_𝔰 = 1.336 for the bare bubble computed in the same way". By eq:15.2-LBCS, δ_𝔰 is the KK quantity
  (1 + δ_𝔰 = 1.323). 1.336 is the direct bare 1 + δ (mine 1.3355). Write "1 + δ = 1.336 (bare; 1 + δ_𝔰 = 1.323 from 𝔰_BCS)".
  Overlap: 15.1 does not repeat the D.39 resummation. 15.2 states eq:15.2-LBCS and then restates eq:D.39-resum in prose
  (15.2-cons l.1): cite it and drop the restated fraction. The (π/2)ln[1/(y−2)] law and the "ratios depend on y and
  qv_F/Δ alone" statement appear in both 15.2 and D.39; keep them in one place.
  The F_μ reduction appears only in 15.1; D.39 only points to it ✓. No duplicate.
P8 WE 15.1 (bulk vs film gap, factor 1.23) → CHECKED, except one number. Independent rate code, own SHM η:
  R_cons light 3.3001 (bulk) and 2.6786 (film) /kg/yr; ratio 1.232 ✓. Lindhard cut ratio 1.298 ✓. Heavy 3.861e-13 ✓;
  heavy ratio 1.128 ✓.
  Ratios bulk 0.946/1.010/0.850/1.024 ✓; film 0.902/1.027/0.806/1.261 ✓.
  Max deposit 3.51 meV = 19.5Δ/11.7Δ; q_max = 5.30 eV; q/k_TF ≤ 1.3e-3; v_Fq ≤ 196Δ ✓.
  WRONG: "with the bulk gap [y<3] carries 18 %". Splitting the ω integral exactly at 3Δ gives 19.7 % (light) and 14.5 %
  (heavy) for the bulk gap, and 37.2 % (light) for the film gap. The 18 % of we15_1.log assigns Gauss nodes to y<3, which
  depends on the grid; with my 36-node grid the same binning gives 22 %. Fix: "20 %". The 37 % stands.
  Source check, 2109.04473 p. 2: "Δ is half of the superconducting gap energy", and Al Δ = 0.3 meV with E_F = 11.7 eV ✓.
  Film convention 2Δ = 0.6 meV, ×1.67 of bulk ✓. The editor's "factor 1.23" is the conserving light-mediator ratio ✓.
P9 One-sided upward nuisance, +0.8 to +9.1 % for y ≥ 3 (editor 15.2 note; 15.2-nuisance) → WRONG off the edge.
  On the edge the range holds: clean 1.072/1.068/1.023, dirty 1.008–1.091 (REF-DC-41 §4 table = book table).
  But rate cells cover q above the edge, and there the clean ratio L_cons/𝔤_IL^nor drops below one: 0.9797 at y = 3,
  q ≈ 4× edge. My scan over y ∈ [3, 30] and q from 1× to 200× edge finds a minimum of 0.980 and a maximum of 1.087. That
  matches 15.1 l.136's own "between 0.980 and 1.087".
  The remainder therefore runs from −2.0 % to +8.7 % (clean), and +9.1 % with disorder on the edge. Its sign is not fixed.
  Also, the lower bound of +0.8 % fails at large y even on the edge (1.0065 at y = 20, 1.0030 at y = 30).
  Fix: either make it two-sided (−2 % to +9 %), or restrict the one-sided statement to cells on the edge and state that
  off-edge cells have |remainder| ≤ 2 % (clean). The dirty off-edge ratio has not been computed. "Since the remainder can
  only raise the signal" must go.
  Same paragraph, "deviations from 𝔤_IL^nor fall with q at fixed ω": false at y = 2.2 (0.868 edge → 0.845 at 1.5× → 0.924
  at 8×) and at y = 3 (1.072 → 0.993 at 2× → 0.980 at 4× → 0.997 at Q = 10³; deviation 0.7 % → 2.0 %). → GAP: write "are
  largest on the edge".
P10 Bare first-order term reaching 0.3 → CHECKED: y = 3.833 (uncut), 3.004 (cut).
  GAP: the mask boundary 3.83 is defined by the bare bubble's first-order term, which 15.1 says describes the bare bubble
  only (editor: "no physical claim rests on it"). The conserving and dirty results give the physical reason, i.e. ℓ_mfp
  sensitivity at y ≲ 3. State the 3.8 boundary as a conservative margin over that, not as an expansion criterion.
P11 ω_AB (15.1 l.78, 15.2) clashes with NOTATION l.1310 (Alig–Bloom, E.13) → CONFIRMED. NOTATION has c_AB for the AB speed,
  so a rename such as ω_{AnB}, or moving E.13 to ω_{AlB}, is needed (ruling).
P12 v_F upright: 15.1 is italic throughout, 15.2/D.39 upright → CONFIRMED (known).
  𝔣_L(ν) clash with the phonon ν: known. NOTATION l.1100 (L^BCS) unused; l.1097 "𝔤_IL^nor" misparse still present.
P13 Al v_F (6.67e-3 vs 6.77e-3) → known; impact quantified here.
  a = 4.05 Å with 3 e/atom gives k_F = 1.7495 Å⁻¹, so v_F = k_F/m_e = 6.756e-3 and E_F = 11.66 eV. bcs15.py builds k_TF
  from this k_F, so its v_F and k_TF are mutually inconsistent at 1.3 %. k_TF cancels from every ratio.
  At v_F = 6.767e-3 (x = 0.3916): the L ratios move by ≤ 0.004 (0.867/0.998/1.069/1.067/1.023). 𝔳 moves by 10–40 %:
  0.45/0.35/0.22/0.053/0.004 against the printed 0.40/0.32/0.20/0.049/0.003 (y = 2.2/2.5/3/5/10), and 0.23 against 0.16 at
  y = 2.05. The 17 % (15.2) becomes 16.2 %.
  𝔳 is the one printed quantity that the v_F choice changes beyond its printed digits. Settle v_F before printing 𝔳.
P14 15.1 vs 7.2 jump (partII note "state the conserving and screening corrections to 7.2's jump") → CHECKED: covered by
  15.1 l.103 and l.132 (step a few µeV wide in L^cons, screened away in L^bare).

## s15-1 (other lines)
l.3 1 keV: 3.51 meV max (9.8× threshold), 5.30 eV, Δ/qv_F = 0.199 at threshold ✓.
l.7 βω = 417.8 ✓. c_LA = (106.8 GPa/2700)^{1/2} = 6.289 km/s ✓. (c/v_max)² = 6.3e-5 ✓. m < 2Δ/(2c_LA v_max) = 3.24 keV ✓.
  S = (2q²/e²)L/(1−e^{−βω}) agrees with S = −2Im χ and L = −(e²/q²)Im χ ✓.
l.18 n_e = 1.806e23 cm⁻³ ✓; k_TF = 4049 eV ✓; Δ/E_F = 1.54e-5 ✓.
  GAP: "k_TF²/q² ≥ 6e5" — the value at 5.3 eV is 5.84e5; write ≥ 5.8e5.
l.22 q²/2m_e ≤ 2.75e-5 eV ✓; v_Fq ≥ 2.52ω ✓.
l.27–56 phases, amplitudes, F_μ and its continuations ✓ (P1). Dimensions ✓.
l.84–88 Im F_μ, the change of variable, the condition v_Fq ≥ (ω²−4Δ²)^{1/2} ✓.
l.99 values ✓. "agree to all printed digits" ✓.
l.101 𝔳 = 0.397/0.202/0.0485/0.0032 at the edge, and 0.305/0.126/0.045/0.0116 at 4× edge ✓. (Δ/qv_F)² = 0.0063 at the y = 5
  edge ✓.
  WRONG locator: Gan's (Δ/v_FQ)² estimate of Π_θ is in Sect. V (Conclusion and discussion, Fig. 3), not Sect. IV. Same fix
  in 15.2-cons ("[Sect.~IV]{gan2026mean}" → Sect.~V).
  Note: Gan's estimate concerns the response, and 15.2's comparison of |R^cons−R^0|/|R^0| (coefficient 27) is the matching
  one. 𝔳 scales as 1/(Q ln Q) (DC-41), so comparing 0.049 with 0.006 is not like with like. Optional: say so.
l.103 Im ε^cons/Im ε_Lin at Q = 2.05/x: 0.136/0.606/1.228 at y−2 = 1e-6/1e-3/1e-2 ✓. Crosses π/2 at y−2 = 0.0245
  (4.4 µeV) ✓.
l.108 (fig:15-alloss) at q = 0.3 eV: L_cons/L_nor 1.274–1.340 and L_bare/L_nor 0.777–0.888 ✓. At 1 eV: spread 4.7 % ✓.
l.112 Q = 11.1 and 37.1; y_max = 4.42 ✓.
l.132 L_bare/L_nor = 0.030 (y−2 = 1e-9) and 0.299 (0.03); L_cons/L_nor = 0.972 at 0.03 ✓.
l.134 ✓ (P4). l.136: values ✓ (P5); bare direct 0.323/0.440/0.565/0.794/0.934 ✓; 0.980–1.087 and bare ≥ 0.527 ✓.
l.140 Gan Eq. (10) = Im ε_BCS/|ε_Lin|² ✓.
  GAP: "its own real part [Eq. (9)]" — Eq. (9) is the rate and Eq. (8) is ε_BCS; cite Eq. (8).
  Hochberg 2109.04473 "[Eq. (2)]": Eq. (2) is the general rate, and the 𝔤_IL^nor replacement is the sentence after it.
  Acceptable; "Eq. (2) and text" is more exact.
  GAP: hochberg2021determining "[Eq. (1)]" for "the Lindhard loss function". Its Eq. (1) is the general loss-function
  rate; the Lindhard form is its Eq. (S.13), written with a damping ω + iΓ_p. Cite "Eqs. (1), (S.13)" here and in the
  lim:15.1a box.
  1512.04533 Eq. (3.4), S = m_e²E_D/(π|q|) Θ(|q|v_F − E_D) ✓; same normalization as S_n = 2πN_Fω/v_Fq of 7.2 ✓.
l.150 limitbox: bare 0.527–0.372 of conserving at y ≤ 3 (>40 % below ✓); Lindhard 0.706 at y = 3 (~30 % ✓);
  v_F/Δ = 7.31 µm ✓.
l.153 Lindhard 19 % low at the y = 5 edge (0.813) ✓. |ε_bare|²/|ε_Lin|² = 1.259 against 1 + 2(Δ/qv_F)𝔰 = 1.167 ✓.
  Gan "ω ≳ 5Δ": the statement is in Sect. V (Conclusion), "for energy transfers above 5Δ …". Sect. IV/Fig. 2 has only "agree
  closely … except near 2Δ" → WRONG locator; cite Sect. V, or Sect. IV and V.
l.159 Savrasov Table III: Al T_c^exp 1.18 K and Δ₀^exp 0.18 meV ✓. 1.764 T_c = 0.1794 meV ✓. Gan 0.17 meV (Sect. IV) ✓.
  Hochberg p. 2 ✓. yeh2023doubling: 2.4 K for 3.5 nm, twice bulk ✓.
l.162–171 WE 15.1 ✓ except 18 % (P8).

## s15-2
Opening: first-order 1.45 at y = 2.2 ✓; m_min = 0.10 keV ✓.
  GAP: "gives it in closed form … for the conserving response". eq:15.2-cons is a parametrization, and 𝔳 and δ need the
  μ quadrature. Say "in resummed form".
15.2-resum: x = 0.3973, 𝔣_L = 0.8329, 𝔯_ε = 0.7493 ✓, 17 % ✓ (16 % at v_F 6.77e-3; P13). ε_Lin of eq:15.2-Lin = 1 − v_C R⁰
  with P_nor ✓.
  eq:15.2-LBCS = eq:D.39-resum with δ = δ_𝔰 ✓. It reduces to eq:15.1-sBCS ✓. Its two lowering effects ✓. Log law ✓.
  KK cut 4.01→2.91 and 2.03→1.14 ✓. Bare direct vs uncut: −1.43/−1.50/−1.40/−1.17/−0.61/−0.21 % (≤ 1.5 % ✓).
  Range text: 0.328–0.398, 0.571–0.657, 0.799–0.8545, 0.936–0.957 ✓.
  GAP (rounding): y = 5 cut = 0.8545, so the 2-digit "0.80–0.86" is a double rounding. Write 0.80–0.85.
  First-order 1.45/0.54/0.17/0.04 ✓; 3.83/3.00 ✓. "A third of 𝔤_IL^nor, half of L^nor" (0.328, 0.49) ✓.
tab:15-edge: every clean entry reproduced to the printed digits: 𝔤_I, 𝔰, first order, ∞/cut, 𝔳 0.158/0.397/0.324/0.202/
  0.0485/0.0032, and clean 0.681/0.868/1.001/1.072/1.068/1.023.
  Impurity columns = REF-DC-41 §4 (Γ = 3.7, 124) ✓. "Clean column changes by at most 0.004 at 0.39": max 0.0042 (y = 3) ✓.
  GAP: REF-DC-41 and limit15_2a.py label 𝔩_e with v_F = 6.8e-3 (Γ = 3.7 → 1.007 µm, Γ = 124 → 30.1 nm). With the book's
  6.67e-3 these are 0.988 µm and 29.5 nm. State in the caption that 𝔩_e uses v_F = 6.8e-3 (2 % shift), or relabel.
15.2-cons: eq:15.2-cons consistent with D.39 ✓. 1.322×1.202 = 1.590 ✓. 1+δ: 1.3355 (bare) → 0.5766 (cons) ✓. L_cons =
  1.072 𝔤_IL^nor = 1.417 L^nor ✓.
  Within 10 % for y ≥ 2.247 ✓. Above it from y = 2.495 ✓. Max 1.0870 at y = 3.6 ✓. Peak L_cons/L^nor 1.432 at y = 2.70 ✓.
  |ε_cons|/|ε_Lin| = 1.268/1.059/0.991 ✓.
  AB pole 1.9214/1.9634/1.9913 ✓. Scaling coefficient 26.9/17.6/11.4 at Q = 7.55/100/1000 ✓. Sum rule 4/5 ✓ (P7).
  WRONG: "The ladder is large on the edge because the AB pole sits just below the gap there … so the denominator of the
  ladder is small." KK split of Re(P_cons − P_nor) into the AB-pole term 2Z y_AB/(y² − y_AB²) and the rest:
  pole 1.131 of 1.013 at y = 2.2; 0.059 of 0.353 at y = 3; 0.000 of 0.129 at y = 5.
  The ladder denominator at y = 3 is |⟨(y²−s²)F⟩| = 2.48, not small. This is REF-DC-41 B2 ("FAILS for y ≥ 3", replacement
  text in §7).
  Fix: "Near the threshold (y ≲ 2.3) the ladder is large because the AB pole lies just below 2Δ …; at y ≥ 3 the shift
  comes from the continuum of the ladder."
lim:15.2a: caption 9.2 ✓ (P6); 0.37 = 0.323/0.868 ✓.
  Text after the box, "𝔤_IL^nor closer to conserving than bare at every y ≥ 2.25" ✓ (it holds at all y on the edge).
15.2-disorder: q = 0.149 eV and q𝔩_e = 0.0227 ✓. Mermin normal state at the same γ_rel = v_F/𝔩_e (REF validated) ✓.
  1.008–1.091 ✓. 0.87→0.60/0.38/0.19 ✓. 1.00→0.57 ✓. 4 % for 𝔩_e ≥ 10 µm (0.835 vs 0.863) ✓. Crossing below 0.40 between
  1 µm and 300 nm ✓.
WE 15.2: every step recomputed: q = 0.2038 eV, 1/q = 0.968 µm, qv_F = 7.55Δ, 0.1324, 0.833, 0.749, 0.3233, 1.561, 1.7512 +
  0.9812 = 2.732, 0.571, 0.755, 0.461 (19 % lower), 0.657, 1.590, 0.577, 1.059, 1.417, 1.072 ✓.
  "Less than 6 %": 1.072 → 1.008 is 5.97 % (dirty columns at x = 0.39) — borderline ✓.
15.2-nuisance: band curvature, "1", particle–hole asymmetry each < 1e-4 (REF: 8e-8, 8.5e-5, 2e-9) ✓. 2Δ/T_c = 3.540 and
  2πe^{−γ} = 3.528 ✓. Coefficient 11–27 ✓. Factor 4.6 (0.868/0.187 = 4.64) ✓. "Outside the KK spread at every y of the
  table" ✓.
  GAP: e^{−Δ/T} at 10 mK is e^{−208.9}; print e^{−209} (7.2 has the same rounding).
  GAP: "Within the model every correction of order (Δ/qv_F)² is in the ladder, since the bare absorptive part has none".
  The bare real part has second-order terms too (the KK-cut difference, 15.1 l.128, and the −1.5 % bare-vs-resummed gap).
  Write "every correction to the absorptive part …".
  WRONG: one-sided nuisance (P9). GAP: mask rationale (P10).

## D-39 (other lines)
Hypotheses, ε = −(k_TF²/q²)R/2N_F, N_F per spin (NOTATION l.232) ✓.
Notation clashes inside D.39 → GAP:
  - h(y′) (KK integrand) and h(ω) = 2N_F/R are two meanings in one section, and both clash with h_k (Nambu Bloch matrix,
    NOTATION l.636).
  - g = h − 3ω²/(qv_F)² stands next to 𝔤 and G.
  - G = 𝔤_IΘ − 1 clashes with the reciprocal vector and the Green's function.
  - The cutoff "T = 10⁴" clashes with the temperature T, which the same appendix sets to 0.
  Suggest 𝔥(y′), 𝔨(ω), the existing δ𝔤 (or G_I) and Y_tail.
Not in NOTATION (15.1/15.2/D.39): 𝔳, 𝔣_L, F_μ, 𝔭_μ, ω_μ, s_*, M^N_A, R^cons, ε^cons, ε^bare, L^bare, L^cons, the
  unsubscripted 𝔤 and δ, and ω_AB (clash). Rows needed at the merge.

## Campaign values (CORRECTIONS, SOTA, DC-RESULTS)
- CORRECTIONS l.343 and l.391 (CW4 (8.1) table 0.33–0.40 … as physical; type-Δ nuisance from the KK spread) are superseded
  by DC-41 (DC-RESULTS: VALIDATED WITH CORRECTIONS). The book follows DC-41: the resummed table is labelled bare, and the
  spread is rejected as a template ✓. No superseded value is printed as physical.
  The ledgers still need the update the editor notes list (SPINE, LIMITS, SOTA l.354/375/393: "8–16 %", "y ≲ 3.5").
- SOTA l.354 "≤ 16 % at 5Δ" against the book's 17 %: v_F 6.8e-3 vs 6.67e-3, consistent (P13).
- returns/R18: DC-41 and REF-DC-41 match my numbers at x = 0.39 to the last digit (P5). The REF §4 impurity table is the
  book's. REF B2 contradicts the book's AB-pole sentence (above). REF §7 quoting is respected except for the missing
  ℓ_mfp clauses (P5).
- DC-RESULTS: the Al anisotropy (σ_φ) is not quoted ✓. The 30 nm film 𝔩_e is used as typical, and REF flags it
  [UNVERIFIED]; it is sourced in 15.3 (outside these files).
