# Ch15 post-revision check (isolated verifier, 2026-11-06)

Scope: tex/ch15/*.tex, D.39, D.40, the Ch15 F rows, the 7.2 and E.20 edits, figscripts/ch15 (+ logs, al_constants.py), the
eight ch15 review ledgers and rulings R0–R11. No tex or script was edited. Book tree is git-ignored, so there is no pre-revision
diff. "Content lost" is therefore checked against the review ledgers' line-level descriptions.
Independent tools: (a) hand/Python recomputation of the free-electron set, sound speeds, ξ₀, WE 15-film, the sheet factors,
kinematics and sum-rule integrals; (b) a new brute-force Nambu code (scratchpad indep.py). It does the 2-D ξ×μ sum of the one-loop
χ33, χ32, χ23, χ22 with eigenvector matrix elements and a broadening extrapolated to 0. The ladder is fixed only by the Goldstone
condition χ22(0,0), so it does not use F_μ or eq:15.1-Rcons. Conservation check: P_cons(Q=0.1, y=2.5) = 5.340e-4 vs Q²/3y² = 5.333e-4.

## Verdict: ACCEPT WITH FIXES (all minor; no physics or number in the rulings is wrong)

## 1. R1, aluminum constants: CONFIRMED (two minor concerns)
- a = 4.05 Å, 12 e/cube: n_e = 1.806e29 m⁻³, k_F = 1.7488 Å⁻¹, v_F = ħk_F/m_e = 2.0246e6 m/s = **6.753e-3**. CONFIRMED. (The ruling's
  "6.76e-3" is k_F rounded to 1.75; the lattice constant gives 6.753e-3.)
- ω_p = ħ(n e²/ε₀m)^{1/2} = 15.78 eV; k_TF² = 4k_F/πa₀ → k_TF = 2.051 Å⁻¹ = 4.048 keV; k_TF²v_F²/3 = ω_p² exactly. CONFIRMED.
- c_LA = (114.3 GPa/2700)^{1/2} = 6506 m/s, c_TA = (31.6/2700)^{1/2} = 3421 m/s. The Kamm–Alers 0 K set (114.3/61.9/31.6) is correct.
  CONCERN (minor): this combines 0 K elastic constants with the room-temperature density 2.70 g cm⁻³ (and a = 4.05 Å). At 4 K, a ≈ 4.032 Å
  and ρ ≈ 2.73 g cm⁻³, which give c_LA = 6.47 and c_TA = 3.40 km/s. Knock-ons are negligible: (c_LA/v_max)² 6.7e-5 → 6.6e-5, and 3.13 → 3.15 keV.
  Fix: either use ρ(0 K) for the sound speeds or add a clause in al_constants.py/15.1 that ρ_T is the room-temperature value (0.6 % on c).
- Knock-ons (script logs, plus my independent Nambu code where noted):
  - 𝔳 on the edge: 0.440 / 0.214 / 0.052 / 0.004 at y = 2.2/3/5/10 (tab15_1.log). Independent: 0.440, 0.214, 0.051 at y = 2.2, 3, 5. At y = 10
    my broadened brute force is not converged (Im P_bare off by 4 %), so the 0.004 rests on the scripts alone.
  - Also independent: L_cons/𝔤_I L^nor 0.866/1.069/1.067, L_bare(direct) 0.326/0.568/0.796, 1+δ = −0.183/0.596.
  - Bare within 10 % of conserving: root at y = 9.11. I rechecked it at 9.0/9.11/9.2 (0.898/0.900/0.902); at the old v_F it was 9.19.
    9.1 is CONFIRMED.
  - Edge table columns 𝔤_I, 𝔰_BCS, first order, both resummed columns, 𝔳 and the conserving clean, 1 µm and 30 nm columns all match
    tab15_1/limit15_2a logs. WE 15-edge arithmetic re-done: 0.575, 0.760, 1.065, 1.414, 1.069. CONFIRMED.
- One set everywhere: Ch15 (15.1, 15.2 WE, 15.3 WE/captions, 15.4, inputs table), 7.2 (v_F 6.75e-3; ξ = 2.4 µm; v_Fq = 10Δ; Δ/v_Fq = 0.10;
  ×3; 2.5 v_max), E.20 (2.0e6 m/s; 2v_F/πv_max = 1.6) and 6.4 (2.0e6 m/s, 1.75 Å⁻¹, 11.7 eV) are consistent. No 6.67/6.77/6.8e-3 and no
  15.7 eV is left in tex/. CONFIRMED.
- CONCERN (deferred, logged by reviser): room-T C11/C44 are still in a2ftr15.py (the empty-core λ_tr = 0.32/λ_ep = 0.44/1.25e4 of 15.4.4,
  shared with fig:6-a2F) and in tex/appC/C-18.tex l.106. These are outside this brief, and they are in "Changes the campaign ledgers need";
  the editor must carry them to CORRECTIONS.
- Stale docstrings (no effect on numbers, since the code imports al_constants): fig15_3.py l.15 and we15_4.py l.4 still say
  "v_F = 6.67e-3", and fig15_3.py says "γ_rel = 26.3 meV" (log: 26.65). Fix the docstrings.

## 2. R2, the cut: CONFIRMED
- Criterion: max/min of the edge L_cons/𝔤_I L^nor(same rate) over 𝔩_e = 30 nm–100 µm. y = 2.5: 0.996/0.569 = 1.751 (fails);
  y = 3: 1.067/1.008 = 1.058 (passes); including the clean value, 1.069/1.008 = 1.060. The boundary is bracketed by the grid only (2.5 < y* ≤ 3),
  and the text says exactly that ("boundary lies between the two"). Excluding y < 3 is the conservative reading.
- y < 3 appears in 15.2-nuisance, summary par. 2, the nuisance-table row and F row l.514. No "3.8" cut and no "masked/cells" is left anywhere
  in tex/. The remaining "3.81" is only the factual statement of where the first-order term reaches 0.3, which is fine. CONFIRMED.

## 3. R3, two-sided remainder: CONFIRMED
- Clean scan over halo momenta for y ≥ 3: [0.9797, 1.0845] (tab15_1.log). The minimum is at 4× the edge momentum of y = 3 (0.9797), so
  −2.0 % / +8.5 %. Impurity edge maximum 1.091 (y = 5, 30 nm) → +9.1 %. Printed −2 % to +9 %, two-sided, standard-normal, and dirty
  off-edge "not computed". The same values are in 15.1-first (0.980–1.085), 15.2, the summary, the nuisance row and the F rows. The clean edge
  values carry the 𝔩_e clause (15.2-cons, last sentence). CONFIRMED.

## 4. R0, spin current: CONFIRMED (two wording concerns in D.40, one minor gap in the summary prose)
- (i) "ξ_coh ≈ 1.6 µm to 2.4 µm" in 15.4.3, the F row (l.541), the nuisance row and the inputs table; 15.3.1 states both values with sources.
  ξ₀ check: BCS ħv_F/(πΔ) with v_F = 2.025e6 m/s and Δ = 0.18 meV is **2.36 µm**. The equivalent 0.18ħv_F/k_BT_c with T_c = 1.18 K
  gives 2.35 µm. The 1.6 µm is therefore the tabulated (Kittel) value and does NOT follow from the book's v_F and Δ. The book's range
  presentation is the correct handling; R0's "≈ 1.6 µm" alone would have been inconsistent with the book's own set. CONFIRMED.
- (ii) Film: g = 2.0e-12 (MB σ₁ = σ_n𝔤_II) against 1.5e-12 (σ_n𝔤_I) at 0.72 meV (fig15_3.log), in 15.4.3, summary par. 4 and the F row.
  "Phonon-only clean-Al projections only" is explicit in 15.4.3. CONFIRMED.
- (iii) F₁ᵃ, triplet p-wave vertex/mode, strong coupling (√1.43 = 1.196 → ×1.2 in g), integrated weight fixed: in 15.4.3, the nuisance row
  and the F row. CONCERN (minor): summary par. 4 prose does not state the line-shape caveat; it is only in tab:15-nuisances. Fix: add one
  clause, e.g. "the sum rule fixes the integrated weight; the line shape depends on F₁ᵃ, a triplet interaction and strong coupling".
- No novelty wording (grep: novel/first time/overlooked/no prior/neglected: none). The literature sentence is neutral. CONFIRMED.
- Formula checks: ∫σ^J dω = (π/2)ω_p² (substitution x = ω/2Δ: ∫₁^∞dx/x²√(x²−1) = 1); the fraction below 4Δ is √3/2 = 0.866 → 87 %, below
  20Δ √99/10 = 99.5 %; σ^J(1 meV) = 3.30e4 eV; dirty ∫₂^∞(𝔤_I−1)dy = 2 (log 1.9999965 + tail). CONFIRMED.
- New D.40 paragraph. Correct in substance: J^zz = i[H, D_s]; a contact singlet pairing term commutes with the local S^z density
  (so H_MF conserves spin locally); the s-wave ladder does not dress an odd vertex; paramagnetic weight ω_p² cancels the diamagnetic
  term → no spin supercurrent. Two wording CONCERNs:
  (a) "[[H, D_s], D_s] is the same one-body constant as for the charge dipole": with D_s = Σσ^z z/2 it is ¼ of the charge-dipole constant.
      The ¼ is compensated by the ½ in J^zz and the normalization of eq:15.4-sJdef. Fix: "a quarter of …, which eq:15.4-sJdef compensates",
      or "the same constant up to the factor of eq:15.4-sJdef".
  (b) "obeys the f-sum rule … with the weight (π/2)(ω_p^intra)² exactly, with interactions": for the full Hamiltonian the exact sum is the
      total weight (π/2)ω_p²(free, n_e e²/m_e, 15.78 eV), interband included. The intraband weight is exact for a one-band Hamiltonian with
      spin-independent interactions, which is the model used. Fix: insert "for the conduction band (a one-band Hamiltonian)". The same
      qualifier belongs in the 15.4.3 sentence "obeys an exact sum rule with the same (π/2)(ω_p^intra)²".

## 5. Restructure (old 15.2.3 → 15.3.3, algebra → D.39): CONFIRMED
- No dangling \cref anywhere in tex/ to sec:15.*, eq:15.*, tab:15-*, app:D.39/D.40 (scripted check against all \label; lim:* are limitbox
  keys, not \label). There is no textual "15.2.3" left. 15.3.3 = sec:15.3-sc (third subsection) holds the Born-impurity construction, the
  ℓ-scan numbers (0.87/0.60/0.38/0.19 at y = 2.2; 1.00 → 0.57 at 2.5; 1.008–1.091 at y ≥ 3; 10 µm/4 %; 300 nm vs the cut-bare value 0.40),
  the single normalization stated once, and the MB local limit 0.157/0.985/1.094/1.023 against the 30 nm column. I recomputed 𝔤_II(2.2) = 0.139
  and the ratio 0.157.
- Everything the prose review lists for the old 15.2.3 (l.82–84) and the s15-3 l.104 numbers is present, and the 1.26/1.30 mismatches are gone.
  15.2 points forward (sec:15.3-sc) in the nuisance paragraph and WE 15-edge without using undefined terms; 15.1-first and the lim:15.1a text point
  to 15.3-sc/15.3-dirty. D.39 holds the pair function, eq:D.39-Fcont, partial fractions, cutoff cancellation, the quadrature recipe, the resummation,
  𝔰_BCS and the sum rule; 15.1 points to it at each step. eq:15.1-F is restated only as the result. CONFIRMED.
- Logs: every log uses the new v_F (al_constants.log 08:08; bcs15-dependent logs written later). limit15_4a.log (07:22) predates the
  constants change, but its outputs (Holstein ratios, 11.4/7.4/8.1Δ) do not depend on v_F. Optional: rerun it for timestamp hygiene.

## 6. R4–R11 spot checks
- R4 CONFIRMED: 7.86 → 7.9 (Δ/qv_F 0.0499 → 0.050), 6.26 → 6.3, 2.250, 9.11 → 9.1, film root-finder 0.642/9.82 → 0.64/9.8, Lindhard limit
  6.2e-5/8.2e-7, "within 9 %". Note (optional): the film thresholds use ratio ≤ 1.1 (≥ 0.909) while lim:15.1a defines "within 10 %" as
  ≥ 0.9; harmless, but say which in the fig:15-film caption.
- R5 CONFIRMED: (2/qd)² with qd = 0.08606 → 540.1. 588 is reproduced by [2/(1 − e^{−qd})]² = 588.2 (film15.log 587.9); ratio 1.089 ≈ 1 + qd.
  QROCODILE paraphrase fixed.
- R8 WE 15-film CONFIRMED by hand: ℓ = 0.2534 eV⁻¹, γ = 26.65 meV, D = 337 cm²/s, 𝔴_γ = 0.392 + 11.62i; ε_Lin = (1.19 + 0.88i)e8,
  L = 4.0e-9; ε(ω+iγ) = (3.48 + 0.234i)e5, L = 1.93e-7, ratios 441 and 29.7; diffusion pole (0.755 + 10.33i)e6; Drude tail 9.63e-8;
  ratio 24. The R8 "0.241×10⁵" is correctly superseded by 0.234 with the R1 gas.
- R6 CONFIRMED: q_min/(ω/v_max) = 2.000, 1.172, 1.027 at m_min, 2m_min, 1 keV (quadratic root recomputed).
- R7/R11 notation CONFIRMED in Ch15/D.39/D.40/F: Ω_AB (\varOmega), 𝔣_L(𝔴), 𝔥/𝔨/δ𝔤/Y_tail, δ_𝔰 = 0.318 (1.318 vs direct 1.329), upright
  v_F, ε^bare. CONCERN (minor): tex/appE/E-20.tex l.7 and l.82 still print L^{BCS} and ε^{BCS}, which NOTATION entry 86 retires. Fix:
  → L^bare/L^cons (resummed form) and Im ε^cons (or ε^bare as meant). E.20 is in scope only narrowly, but the retired symbol now has no
  NOTATION row.
- R8 other items CONFIRMED: 20 % share (we15_1.log 0.197), ladder 4e-4, WSi 3.4e47, Gan 0.26 meV/Sect. V/Eq. (8), 0.53/0.38, ×1.13 heavy
  (logged 1.128), π²/2y (y𝔰 → 4.935), Re ε^cons < 0 (1 + δ = −0.18), M_s2 phase and |M_η|² written out. CONCERN (minor, outside Ch15):
  7.2 l.230 still has "a wavelength 1/q = 0.73 µm". Change it to "a length 1/q" in the same narrow edit.
- R9 CONFIRMED: strong-coupling wording (normal-metal 1/(1+λ_tr)² = 1/1.39² = 0.518 known, Allen 2015 Eq. (3); superconducting case open)
  in 15.4.4, the summary, the nuisance row and the F row. Allen 1971: "as quoted by" in 15.1 l.91, 15.4 l.71 and F l.525. CONCERN (minor):
  the lim:15.4a statement (s15-4 l.76) still says "following Allen~\cite{allen1971electron}" without "as quoted". Fix: "following Allen
  as quoted there". "??" and "masked" are gone.
- R10 CONFIRMED: 0.9995 for Drude, identical at 50/500 eV cutoff, flat σ_n 1.000000 → the residue is attributed to the Drude shape only;
  e–e absorption named and unsized, with no estimate printed.

## Fix list (for ACCEPT WITH FIXES)
1. D.40 (and the 15.4.3 sentence): qualify the exact spin sum rule as one-band/intraband; correct "same constant" to ¼ (compensated).
2. Summary par. 4: one clause on the spin-current line-shape caveat (F₁ᵃ, triplet, strong coupling), as R0(iii) requires.
3. E.20 l.7/l.82: L^BCS, ε^BCS → retired symbols replaced (L^bare/L^cons, ε^cons/ε^bare).
4. s15-4 l.76 (lim:15.4a): Allen 1971 "as quoted by" Hochberg–Lin–Zurek.
5. 7.2 l.230: "wavelength 1/q" → "length 1/q".
6. Docstrings: fig15_3.py, we15_4.py (v_F 6.67e-3, γ 26.3 meV) → al_constants values.
7. Optional: ρ(0 K) = 2.73 g cm⁻³ for the 0 K sound speeds (c_LA 6.47, c_TA 3.40 km/s), or state the mixed convention; the fig:15-film
   caption could state its 10 % definition; rerun limit15_4a for timestamp hygiene.
Deferred (logged, not blocking): room-T elastic constants in a2ftr15.py / 6.4 force-constant fit / C-18 l.106.
