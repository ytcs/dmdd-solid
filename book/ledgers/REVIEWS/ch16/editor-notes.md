# Chapter 16 editor notes

## 16.1 drafted (2026-11-06; ~2,700 words prose; D.41 ~1,380; chapter opening + map; Limit Check 16.1a; 1 F row)
- The published Dirac reaches overstate scattering by ε_bg² and absorption by ε_bg. This matches the campaign's refereed correction (1708.08929/1910.02091, SOTA) and is derived in D.41. Geilhufe et al.'s ZrTe₅ absorption curve is reproduced to 0.5 % with their rule. The ZrTe₅ scattering correction is ×4800–6600 (inside the compute referee's range); the harmonic mean would give 2550.
- New: the lower bound (α/v_max)² = 7.6 on the overstatement wherever α̃ < 1, and the design rule reverses (the published absorption peaks at ε_bg = |ε_D|; the total-ε rate falls monotonically). Derivation review PRIORITY.
- ε_r (sources) clashes with the 16.7 glass permittivity → ε_pub (new symbol).
- E.20: 640/5.0 → 642/5.03 for ε_bg = 25.34.
- The recomputed published scattering curve sits at 0.63–0.72 of theirs (halo difference, per the caption). Verify.
- Sommerfeld near-threshold factor (> 1.5 over 85 % of the rate at 20 keV) is a nonrelativistic estimate: candidate 16.9 nuisance row.
- Rerun map16.py after 16.2–16.8.

## 16.2 drafted (2026-11-06; ~4,400 words; Limit Checks 16.2a–c; 3 F rows)
- Limit Check designs depart from the App. F plan: 16.2a compares linear vs parabolic channels (the subband/massive-Dirac response belongs to 16.3); 16.2b shows the 3D and 2D widths (the planned (π/2)v_a/v_F is 3D only; the 2D width is (v_a/v_F)/√(1−v_a²/v_F²)). Accept or rule at review.
- PRIORITY derivation: eq:16.2-inplane, the exact two-layer in-plane response, and the coefficient f²(1−f)²(ε_A−ε_B)²/12ε_∥ε_⊥² of eq:16.2-corr. The one-layer limit matches 2110.01587 Eq. (19) only up to a real constant: explain the constant. 2110.01587 Eq. (16) equals the effective-medium result at any filling.
- Nanotube rate of 2607.15338 is ×4 low at fixed g_c (×2.1 at fixed kernel); both readings printed. Verify.
- One graphene velocity v_D = 3.41e-3 (from the a_CC, γ₀ quoted by 2312.00866) vs the 0.8e6 m/s of 2607.15338: check consistency with 16.3.
- Pines 1956 credited unread. The last two prose edits are not rebuilt.

## 16.3 drafted (2026-11-06; ~3,490 words; Limit Checks 16.3a/b; 4 F rows)
- Results to verify (PRIORITY):
  - orthogonalized final states raise the graphene ejection rate ×1.44 (10 MeV) / ×1.84 (100 MeV);
  - hard-wall dots carry 0.70–1.03 of the gap-shifted bulk response, leading correction −9π/(8kR);
  - Blanco et al. Eq. (6) is too large by μ/(4ω) (4.05e4 at 10 MeV, 3 eV);
  - PbS-in-silica depolarization factor 6.00.
- Hochberg et al. Eq. (7) may double-count π states (N_C = 2/M_cell) unless the cluster wavefunction carries weight 1/2. The derivation reviewer decides.
- Blanco et al. Eq. (11) misprint (0.283d³ vs 0.283d). The text avoids it.
- Graphene/nanotube Dirac velocity: 16.3 uses 3.02e-3 (t = 2.8 eV), 16.2 uses 3.41e-3. Unify (subband edges move ~10 %). Ruling at review.
- E.21's orthogonalization ratio 0.4–4.3 (Slater; Clementi–Raimondi unread) vs Hochberg's orbital 0.46–25.
- App. C.8 lacks I₀, K₀, which SPINE and 16.2 point to. Add them at the App. C pass or repoint.
- Limit Check 16.3b x-axis is energy above the dot gap (kR controls), not R/a*.
- Add \cref{lim:16.3a,lim:16.3b} to the map caption.

## 16.6 drafted (2026-11-06; ~4,020 words; Limit Check 16.6a (2 panels); 2 F rows)
- 1608.02940 is cited in arXiv equation numbering ((3.3), (3.11), (3.12), (3.17), (4.3), (4.5)); SPINE uses journal numbering ((4), (12), (23), (25)). Pick one at the merge (arXiv numbering, consistent with the book's source practice) and fix SPINE.
- LiF E_d = 27 eV is a TRIM input (Cogswell et al.), not measured; the F-site phonon energy is bracketed (33.5–77.2 meV). Both are labelled as model values.
- WE 16.6 uses Lindhard/Kinchin–Pease below their validity (scale estimates); the Li/F sublattice split is not computed.
- Solid H₂ ⟨ω⟩_CM = 10 meV is assumed (negligible effect).
- E.21: m_1 → M_1 (NOTATION reserves m₁ for the first moment).
- "Cage effect" named without a citation: add one or describe it in words.
- Last prose edit not rebuilt.
- PRIORITY derivation: the bond-breaking convolution, the ω_vib/4 difference between impulse and improved Born (Essig et al.), and the threshold m_χ ≥ 4.0 MeV for the electronic exciton → F–H route.

## 16.5 drafted (2026-11-06; ~2,950 words; Limit Check 16.5a; 1 F row)
- PRIORITY (new claim about a published normalisation): Du et al. (2212.04504 v1) factor (E_eff/E₀)² = 4.84. In effective-mass theory the local-field ratio is close to 1. With the factor, their continuum alone carries oscillator strength 4.85 > the 3.85 the f-sum allows the whole donor. Derivation review must check.
- Du et al. Eq. (12) misprint: 3q̃ for 3q̃². Absorption is unaffected; the printed bracket gives scattering 1.47/0.91/0.59/0.56 of correct at 0.02/0.1/1/10 MeV. (Consistent with the campaign's earlier 2212.04504 misprint finding: check that it is the same one.)
- Du et al. absorption form = first order in donor density of the effective-medium loss function (host screening once). Holds within 10 % below 2.6e17 cm⁻³ in the continuum, but fails at 4.8e15 cm⁻³ at the 1s→2p₀ line centre (donor self-screening).
- Si:P line strengths are model values bracketed ×3.2–3.4 (EMA envelope vs Gaussian central cell); no measured oscillator strengths were fetched. Review: fetch measured Si:P oscillator strengths if open.
- The Limit Check design departs from the plan (Clausius–Mossotti vs donor density; line width assumed). Rule at review.
- Mott n_c ≈ 3e18 quoted via Du et al. (primaries unread). The CM divergence at 6.3e18 / 2.1e19 lies above n_c.
- New results to verify: 1s(A₁)→1s(E) via mass anisotropy at q ≈ 100–150 eV, vanishing along [111] (directional); 1s(A₁)→1s(T₂) needs 0.685–3.88 keV intervalley momenta.
- Local-field ratio (16.5-floc) uncomputed; E.21 should mention it. The unsized impurity-band correction is covered by DC-51.

## 16.4 drafted (2026-11-06; ~3,900 words, over the 3,500 budget; Limit Check 16.4a; 1 F row)
- Correction to the campaign return: intensity borrowing from other manifolds changes the binned sum at FIRST order in 𝔍/ΔE, not second (the model confirms it). The book states first order. Logged in CORRECTIONS.
- Model only: an anthracene π-electron model without σ electrons (𝔍 unscreened), so the corrections are "probably overstated". The measured Davydov splitting (~220 cm⁻¹) has no readable source; WE gives the model 31 meV only. Review: find an open source for the measured splitting, or keep the model value with the label.
- Limit Check against m_χ instead of q·a_mol (B_b band overlap). Rule at review.
- E.6 promised the reaction-field vs periodic difference; 16.4 gives the gas-to-crystal shifts and the periodic G₀W₀-BSE S1 (3.3 vs 3.1 eV) instead. Fix E.6 or accept.
- Mataga–Nishimoto form and U = 11.13 eV named without a citation (originals unread).
- Anisotropy: ×90 rate variation at 1 MeV; maximum daily modulation 0.98 at 1 MeV, 0.08–0.13 at 1 GeV. Verify at review.

## 16.7 drafted (2026-11-06; ~5,000 words; Limit Checks 16.7a–d; 4 F rows; 22 long-sentence warnings)
- DM–TLS scattering estimate 3.1e-2 /(kg·day·meV) at 1 MeV (public C = 2.6e-4, book halo) vs the campaign's 3.7e-2 (WP7-T). Both are inside the stated factor 3. Reconcile the inputs at review and update SOTA if 3.1e-2 is adopted.
- The host term is fixed by the acoustic tunnelling strength C_l alone (not tanδ₀). Add to the 16.9 glasses row.
- PRIORITY: Limit Check 16.7c. At the 4e-38 cm² reach Liu et al. quote, V_opt/E = 1.86, far outside Born validity (|V_opt|/E < 0.092). The published reach lies in the non-Born regime: verify, and state the consequence.
- ε_r = 3.9 (a-SiO₂) has no open source; γ_l = 1 eV is assumed. Review: find sources or keep the labels.
- Taraskin B units (printed cm⁻¹, read as unitless): verify.
- Prose review: 22 long sentences.

## 16.8 drafted (2026-11-06; ~3,800 words + D.42 ~1,570; Limit Checks 16.8a (2 panels)–d; 5 F rows)
- PRIORITY new derived result: the quasiparticle golden rule (D.42) adds a factor sinh(u)K₁(u), u = Δ_tl/2T, to Meißner et al. Eq. (9). Thermal TLS relax 14–29 % slower than the published factor says. Not checked against Black–Fulde (closed access). 16.9 and s16-summary should say "for Δ_tl ≪ T" when quoting the bare factor.
- Qureshi Eq. (10) small-coupling form off by Γ(1+α)/Γ(1−α) (0.71 at α = 0.28): verify.
- Exact single-channel coupling α_ohm = (4/π²)arctan²(πK_b^{1/2}) is a model result (0.70 of Born at K_b = 0.07).
- Unify τ₁⁻¹ (16.7) vs Γ₁ (16.8); V_b (16.7, 16.8) vs E_b (App. E.11).
- Meißner Eqs. (4)–(6) δε = 2γS: only Eq. (7) verified; the book states only Eq. (7).
- The three display splits after the last full build were checked only by a wrapper compile.
- WE 16.8: 1 g fused silica at 10 mK releases 46 pW after 1 h, 1.9 pW after a day, 0.27 pW after a week.
- Map caption: add the 16.7 and 16.8 Limit Checks; rerun map16.py.

## 16.9 + summary drafted (2026-11-06; s16-9 retitled "Material inputs of the novel targets"; Table 16.1 inputs (11 targets); nuisance longtable 32 rows; eq:16.9-power; WE ZrTe₅ band)
- SPINE title change 16.9: accept (fix SPINE at the merge).
- α_ohm 0.19 vs 0.28 (0.68, not 0.70): use the printed numbers.
- Inputs/truncation split into two tables (as in Ch15): accepted.
- Graphene v_D: unify at review (16.2 3.41e-3 vs 16.3 3.02e-3), then remove the Table 16.1 clause.

## Ch16 review rulings (2026-11-06; six reports: derivation-1/2/3, prose, reader-a/b — all MINOR GAPS / REVISE, no REWRITE)
- R1. ZrTe₅: the central Δ_D = 11.8 meV (half-gap, per state/CORRECTIONS l.458–459). The other Table 1 rows of 1910.02091 (incl. ISIF7 15.6 meV) form the computed range. Recompute thresholds and reaches. Label ×4800–6600 as "with the book's halo" (4200–6600 across halos; compute referee quotable (4–6)×10³). Explain the 0.63–0.72 recomputation gap as mostly the halo (0.8–1.1 with v₀ = 220, v_E = 232, v_esc = 600; the source states no halo). The 16.1 opener must not quote ≈2550.
- R2. DM–TLS scattering: the host term uses the longitudinal C_l (Golding 1.9e-4), giving 2.3e-2 /(kg·day·meV), or state explicitly that the polarization-averaged C is used and why. Make the text and the number consistent everywhere (16.7, Table 16.1, nuisance row, summary). Give the inputs behind the difference from the earlier 3.7e-2 (C and the halo escape cut).
- R3. s16-7 l.220: add the missing (δn/n₀)² (7e-4 for Ti–6Al–4V); use the quotable wording of REF-DC-49-54-36 §4 item 8.
- R4. Graphene Dirac velocity: 3.02e-3 (t = 2.8 eV) book-wide. Rerun the 16.2 scripts (g_c 0.17/0.21/0.34; subband pairs 1.9 → 1.7 eV; limit16_2a) and remove the two-velocity clause from Table 16.1.
- R5. 16.4 anthracene: fix the double counting of the crystal shift (the molecular level is set to the measured crystal 3.1 eV and then shifted by 𝔍). Use a gas-phase/molecular level or drop the second shift; rerun WE 16.4, the Limit Check and Fig. 16.4. Compare the model Davydov splitting (31 meV) with the measured ~25 meV (cite if an open source is found; otherwise "about 25 meV, as quoted by …"). "L_b has no dipole" holds only in the model. Limit Check 16.4a: show or state the 0.88–1.0 MeV window (ratio 1.38). Fix the Blanco 2020 vs 2021 attribution.
- R6. 16.6:
  - Budnik σ̄_n, not σ̄_e.
  - The Essig ~10 % comparison is false: restate it (10 % is below both 16 % and 25 %).
  - The electronic F–H threshold opens at the exciton energy, not the gap: source the LiF exciton energy (≈12.6 eV recalled) and recompute (≈3.6 MeV), in the text and the fig16_6 caption.
  - Swap the Araujo time constants (6.5 h F₃⁺, 9 h F₂⁰). Araujo estimates (does not count) one aggregate per 2–3 vacancies.
  - The Doppler width in the general (heteronuclear) form.
- R7. 16.3 dots: 0.76–1.03 at qR = 8 over the stated range; state that near the gap the ratio reaches 2.4–66. Hochberg Eq. (7): add the clause that, as printed, it counts states twice unless each carries weight ½. The "Slater" exponent is Clementi–Raimondi's (cite as quoted by E.21 or describe). Footnote the factor-1.8 offset in we:16-factor; define the 3.33 g/cm³ density and use one density in that worked example.
- R8. 16.5: Limit Check 16.5a L^D (not W). The 3.2–3.4 factor applies to the 2p lines only. State that the 1s(E) numbers assume one envelope shared by A₁ and E, and that "local-field ratio close to one" is an EMA expectation, not computed. Upgrade the misprint impact (1.47/0.91/0.59/0.56) to calculated.
- R9. 16.7:
  - The relaxation-plateau condition: the fastest systems relax fast (π/4 from the slow systems near u² ~ ωτ_min).
  - Host/core crossover: 1.2 keV orientation-averaged, 0.71 keV aligned.
  - Split the 16 real long sentences.
  - Symbol clashes (α, C, A, B, IR, S, R).
  - Al phonon rate 1.8e5 s⁻¹ only below ~50 mK.
- R10. 16.8: heat-release anomalous factor: 1.4 computed from Sahling 2014 Table I, while the paper's text says about 2. Print both with the reason. Unify τ₁⁻¹ and Γ₁; V_b vs E.11's E_b (keep V_b; fix E.11 at the App. E pass).
- R11. Summary/16.9: "at least 7.6" is for scattering; absorption 2.75. Remove the 16.9 recaps of the summary. Give "30 MeV" and "1.22 E_d" a home in a section or drop them.
- R12. Structure and prose:
  - Rewrite the chapter opening as motivation, not an outline. The map caption tags all 17 Limit Checks; rerun map16.py.
  - 16.1 points to D.41 instead of repeating it.
  - Cut process asides (misprint notes, "numerically checked").
  - US spelling; one phrasing of rate units.
  - Prose-review cuts (~1,500 words; 16.4 under budget).
  - App. C.8 lacks I₀, K₀: repoint 16.2 (to a standard reference or D.41) or add them to C.8 by a narrow edit.
  - 2110.01587 Eq. (19) constant: the one-clause explanation (−d_A; they never subtract the vacuum term).
- R13. Notation: the ~40 missing 16.4–16.6 rows, ε_pub, the Lindhard ε/k clash, t_j, B, s scope; the P̄ row (per λ, Δ_as ≥ 0); 𝓃₀ means nucleon.
- Ch7 worked example and E.20 table still print the ZrTe₅ half-gap 15.6 meV; R1 sets the central value at 11.8. Narrow fix at the next light pass.
