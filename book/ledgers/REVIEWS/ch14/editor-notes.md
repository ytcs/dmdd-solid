# Chapter 14 editor notes

## 14.3 drafted (2026-11-06; ~3,610 words detex; Limit Check 14.3a two panels; 2 F rows)
- Bound to 14.4: SPINE writes g_J for Ni²⁺, but Ni²⁺ is quenched (g_J is reserved for J multiplets). 0.83 corresponds to g = 2.2 with λ_S = 1. Fix the 14.4 wording, and fix the NOTATION λ_S row ("spin–lattice factor" is wrong).
- The zero-point correction to the AFMR weight for |S| = 5/2 at MnF₂'s ω_A/ω_E = 0.017 is not computed (the 8-site ED cannot reach it): added to DEFERRED-COMPUTE.
- Γ_M/ω = 1e-5 for YIG is the value Mitridate et al. assume, not a measurement. The text must say so (review check).
- MnF₂ AFMR: 1.021 meV from fitted fields vs 1.1 meV from neutron data at 4 K. Both are printed; reconcile at review.
- SPINE's 2001.10666 Eq. (35) is the cavity–magnon Hamiltonian in v3. The text cites Eqs. (25)–(27), (38), (55), (59); fix SPINE at the merge.

## 14.1 drafted (2026-11-06; ~3,000 words detex + D.38 ~1,400; Limit Check 14.1a; 2 F rows; chapter opening + map)
- Unify notation with 14.2: 14.1's w^M_q = 14.2's w_⊥/|S|. 14.2 also repeats ΔS = 0.078 and the four-interleaved-sc-lattices remark; cut the repeats at review (14.1 owns them).
- Check: 4.54 meV NiO gap from dos Santos et al. Sect. III ("magnon energy at the M point … infrared"); 14.1 calls it a zone-centre magnon from far-IR. Verify against the original IR papers.
- Ni²⁺ form-factor coefficients were taken from the periodictable package (cites the International Tables). Verify against the table itself.
- Rerun map14.py after 14.4–14.6 (hard-coded Limit Check numbers).
- The 14.1a Limit Check compares weights, not rates. Optionally add a rate panel once the 14.2 two-magnon rate exists.
- The 14.1 rewrite after the box has not been rebuilt (the next build covers it).

## 14.2 drafted (2026-11-06; ~3,830 words; no box/F row per SPINE; lint clean)
- ΔS = 0.078 and W∥/W⊥ = 0.073 agree with 14.1 (0.0784, 0.0731). Unify symbols at review.
- WP4 §2.3 is wrong: the exchange-striction (strain derivative of J) term has no part linear in the bosons about a collinear state, so it couples a phonon only to magnon pairs. One-magnon–one-phonon mixing is magnetoelastic (spin–orbit), as in Kittel and Rückriegel et al.; the text follows them. Logged in CORRECTIONS. App. E.20 has no specification for magnetoelastic constants: add one at the App. E pass.
- The NiO magnon–phonon nuisance is unsized (no measured magnetoelastic constants among the inputs).
- Rückriegel Eq. (3.1) has a stray factor 2 against its own Eq. (3.23). The book cites only (3.23)/(3.25).
- The final-state interaction ~0.04 is an order-counting estimate. Tag it as an estimate.

## 14.4 drafted (2026-11-06; ~2,750 words detex, short because App. C.19 carries the cross-section; Limit Check 14.4a; 1 F row)
- Unread sources: g ≈ 2.2 for octahedral Ni²⁺ (Abragam & Bleaney 1970, not opened); L/S = 0.34 (Fernandez et al., closed access, taken as quoted by Kwon & Min); Lovesey Vol. 2 (no chapter, not read). The citation audit must verify these or soften the attributions.
- SPINE 14.4 LO(iv) g_J → spectroscopic g (merge). NOTATION λ_S row wording (merge).
- Check the printed Limit Check numbering: map14.py labels this box "Limit Check 14.3" while the label is lim:14.4a. Confirm the numbering scheme at review and rerun map14.py.

## 14.5 drafted (2026-11-06; ~4,300 words; Limit Checks 14.5a (2 panels) + 14.5b; 3 F rows)
- GaAs lowest-band ⟨|L^ph|⟩ = 0.124 (book PBE IFCs) vs 0.07 (Matas et al., different dynamical matrix). Both printed; resolve at review (check whether the compute agent's DC results bear on it).
- Rename 14.5's ω_M in eq:14.5-GL (clash with 14.3's ω_M).
- E.20: 𝒢_OA has units of S and gives an enantiomer difference, not a dimensionless "directional signal". Align E.20.
- The Limit Check 14.5a/b design departs from the App. F plan (x-axis m_χ; validity = rate-weighted average within 10 % of the band average; 14.5b compares models at |S| = 5/2 with gap 0.02 T_CM). Review whether this is acceptable.
- Check against Alves et al. Sect. III: the claim that the absorption trigger depends on m_φ alone (so their boosted fraction is irrelevant).
- New derived statement: a magnet conserving S^z_tot has R_{s^z𝒥}(0, ω≠0) = 0, so the resonant multiferroic response needs SOC. Derivation review PRIORITY.
- Open items match DC-37, DC-46, DC-84 (the compute agent may be handling them).

## 14.6 drafted (2026-11-06; ~6,100 words detex incl. 960 summary and 1,300 of tables, over the 4,500 budget; Limit Checks 14.6a–c; 3 F rows; nuisance table 23 rows; inputs table)
- E.26 defines t_coh with an extra 2π (6.6 ms at 1 µeV). The book uses 1/(m v₀²) = 1.04 ms (Ch11 R7). Fix E.26.
- 8.2's golden-rule condition (record ≫ both t_coh and 1/Γ) vs 14.6's sharper statement (the ensemble mean needs only the shorter; a single record matches only beyond t_coh). Do a light pass on 8.2.
- Recheck the 14.6 summary and the 14.4/14.5 nuisance rows against the final s14-4/s14-5.
- Fixed-amplitude limit too strong ×1.99 (book model) vs Centers et al. 2.7–10 (at the detection threshold): both printed with the reason.
- The nuisance-table basis column adds a new label "data". Check it against the PARTII status vocabulary.
- Rerun map14.py now that every box is final.
- 14.6 is over budget: the prose review should check for cuts.

## Ch14 review rulings (2026-11-06; five reports: derivation-1/2, prose, reader-a/b — all MINOR GAPS / REVISE, no REWRITE)
- R1. "At least ΔS/|S|" (14.1, Table 14.3/nuisance table) → an estimate of the one-magnon weight defect at leading order, with D.38's caveat (the ground-state change at the same order is excluded). No "bound" wording anywhere. Fix the D.38 convergence statement (inverse square; ΔS → 0.0785).
- R2. Neutron no-go (14.4): restate it. Model-independently (exact response), no neutron measurement reaches q̂·S·q̂. Within the localized-moment model that 14.4 itself uses, transverse data at several q+G determine the full tensor. Qualify the O₆/O₁₀/ALP claim: those elements are not measurable model-independently but follow within the localized-moment model under its stated assumptions. The key-result box changes accordingly.
- R3. GaAs ⟨|L^ph|⟩: keep 0.124. State that grid, masses, weighting and force-constant variation (±40 %) cannot produce a factor 2, and that a single Cartesian component gives 0.062, close to the 0.07 of Matas et al. Give it as a possible origin, not an assertion.
- R4. Coherence time: the book convention is 1/(m v₀²) everywhere. Fix E.26 and s11-8, and resolve the "both vs shorter" contradiction in 14.3 l.80 and the 14.6 opener (²⁰⁷Pb with T₂ = 16.7 ms) to 14.6's rule. Light pass on 8.2 to match.
- R5. Number fixes:
  - MnF₂ ω_M/ω_E: check the 4π (reader-b; 1.3e-3 vs ~1.6e-2 in book units).
  - MnF₂: lead with the measured 1.1 meV / ~9.4 T; give the fitted values second.
  - Aybas: 1.9 nT measured (2.9 nT computed).
  - 14.5: 0.2 MeV, not 0.23.
  - YIG: q_1BZ with the current lattice constant, named as the zone corner; "every q inside the zone" below 134 keV.
  - c_M: J₁+J₂ model (edge 7.3 keV, ratio 5.1), or label the J₂-only value.
  - The ×29 near the edge is an upper value (the in-plane branch is near 0.6 meV).
  - Mention the accidental zero at X.
  - Summary: 4.77 vs 5.0, and 0.073 vs 0.078.
  - M = 3.5 vs 3.25 MeV.
  - The de Broglie 2π.
- R6. Labels and sources:
  - Γ_M/ω = 1e-5 is an assumed value.
  - The 4.54 meV citation goes to the original far-IR papers, or is softened to "quoted by dos Santos et al.".
  - "hexaferrite" → the correct term for h-LuScFeO₃.
  - Sm³⁺ is J-mixing sensitive.
  - Unread sources (Abragam & Bleaney g ≈ 2.2; Fernandez L/S; Lovesey) are attributed as "quoted by" where not read.
  - Alves: correct for halo DM; say that their boosted fraction does not apply to absorption.
- R7. Reproducibility: make the Neyman-construction factors (1.99, 1.76, 3.46, the 23 t_coh crossover; and 2.73 reproducing Centers et al.'s 2.7) and the 8-site cluster numbers reproducible from the text (state the construction in enough detail) and from complete logs. limit14_6c.log is truncated: regenerate it.
- R8. Structure and prose:
  - Move the Summary (\section*{Summary}, as in Ch11–13), the inputs table and the nuisance table out of s14-6 into a new file tex/ch14/s14-summary.tex, input last in ch14.tex (no new numbered section). Make the listed 14.6 cuts so that 14.6 proper is about 4,400 words or less.
  - Remove the 14.2 repeats of 14.1 (ΔS, four lattices, most of 14.2.5). Credit the 7 % to 14.1.
  - Cut the restating endings (14.4.2, 14.4.3, 14.5 open problems, the recap after the nuisance table).
  - Register: reduce "so/only/gives"; use natural connectives.
  - Define "Kittel mode" at first use; also Schiff moment, δk′/ϑ_k, ν and z, and the eq:14.5-GL symbols.
  - "at 1 keV" → "at q = 1 keV".
  - Fix the four "??" references.
  - Add the computed 14.5 rows to the nuisance table and recheck the 14.4/14.5 rows and the summary against the final sections.
- R9. Notation: resolve Ω, ω_M (14.3 vs 14.5), bare g (point-group element in 14.4), Δ (gap vs detuning), Γ_T, and λ_S (spin fraction of the ionic angular momentum). Add the missing Ch14 symbols to NOTATION.
- R10. Rerun map14.py and every Ch14 figscript affected.
- X_αβ in 14.2 conflicts with the u_αβ strain-tensor ruling: rename in the tex at the next light pass (from the Ch14 merge).
