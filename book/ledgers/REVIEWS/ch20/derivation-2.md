# Ch20 derivation check, part 2 (ch20.tex, s20-4, s20-5, s20-summary)
Reviewer: derivation verifier (isolated), 2026-11-06. Sources fetched and read in full text: 1401.1937 (Guruswamy), 1109.1193 (Leman), 2109.13551 (Malica–Dal Corso), 1803.02903 (Agnese), 2303.02196 (Albakry), 2012.12430 (Ren), 1109.4343 (Hertel). Kaplan 1976 and Chang–Scalapino were not available (paywalled), so they are checked only as Leman and Guruswamy quote them.
Recomputation: every number taken from the cached logs qp20_4.log, kern20_5.log and disc20_5.log, with an independent re-derivation in sympy/scipy. One light new run (25 s, no QE): /tmp/claude-0/-home-user-breakthrough-maths/30a63adb-c597-5cb8-b46c-4c5645c8b7d4/scratchpad/rcoll_cascade.py. It imports qp20_4.Cascade and reimplements the kern20_5 solver; with the ramp yield it reproduces the logged 0.892/1.094/1.040/ε_prim 0.6066 exactly.

## A. PRIORITY items

A1. Kinematic proof Y = 2Δ/E below 4Δ (s20-4 l.24–45). **CHECKED.** Threshold for pair-breaking emission is E ≥ 3Δ. The hotter quasiparticle has at most E_ath − Δ, so a third quasiparticle needs E_ath ≥ 4Δ. E_leak = 0 because only the first phonon can break a pair. Guruswamy p.5 quote verbatim ✓. qp20_4.log max |Y − 2/W| < 1e-12 for all r and both seeds ✓. The 87–174 GHz band ✓. WE 20-al3: 𝔤_I(3) = 1.32212 (quadrature), t_pb = 0.7921 t0 = 0.206 ns, Y = 2/3, E_sub = Δ, emitted phonons ≤ Δ = 43.5 GHz, all ✓. Caveat (no change needed): the exact count ignores recombination and absorption of sub-gap phonons by other quasiparticles, which is consistent with "dilute".
   Cross-check against DC-83 (VALIDATED, quotable): the CMPMC 600 nm film gives 0.654 at 3Δ, not 2/3. That is a per-arriving-phonon yield that includes first-phonon escape (0.654/0.667 = 0.981). It agrees with the book's conditional definition, but a sentence should say that the unconditional value is lower by the absorption probability.
A2. Split, normalization and rates (eq:20.4-split, -tpb, -emit). **CHECKED.** ∫ numerator/denominator = W𝔤_I; I(2⁺) = π, so 𝔤_I(2) = π/2 and t_pb(2Δ) = t0. t_pb(10Δ) = 0.2991 t0 ✓. The Allen-formula argument (α²F ∝ F ∝ E² ⇒ γ ∝ E) ✓. Leman Sect. IV items 3–4 match eq:20.4-split (case I) and eq:20.4-emit ✓. Guruswamy Eq. (1) has −Δ² for the photon ✓. t0 = 0.26 ns and τ0 = 438 ns are both on p.3 ✓; 0.1–10 ns on p.1 ✓. Δ/(v_F q) ≤ 1.61e-3 ✓.
   - WRONG locator: eq:20.4-tpb "as quoted by Leman [Sect. IV]". Leman gives only P_φ and P_QP, not the pair-breaking rate. Cite Kaplan directly (unread) or Guruswamy p.5 ("τ_pb scales approximately as 1/Ω"). Also "Kaplan et al. use α²F = bE²" cites Kaplan directly; the editor ruling is "as quoted by Leman" (item 3, the Ω² factor).
   - Minor: Al c_LA. The Ch15 R1 0 K ruling uses ρ = 2.73 → 6.47 km/s and v_F/v_L = 313, not 311 (qp20_4 uses 2.70). The bound becomes 1.60e-3. The C11 = 114.3 GPa from Malica–Dal Corso Table 2 (1143 kbar) ✓.
A3. Kaplan cascade and its MC (eq:20.4-cascade, s20-4 l.84–96). **CHECKED.** The first-step equations are correct: the script's Z, A, B decomposition is exactly eq:20.4-cascade with N̄_qp = 1 below 3Δ, and eq:20.4-ppb is the competition of independent decays ✓. Self-similar mean 3E/4 ✓. Phonon vs photon seed 0.0071 / 0.0006 ✓.
   - Wording: the MC differs by up to 1.2σ (0.0014 vs a standard error of 0.0011–0.0012), so "within its statistical error of 0.001" should read "within 1.2 standard errors (≈0.001)". Energy closure 7e-15–2.1e-14 ✓ ("2e-14").
A4. 0.590 / 0.600. **CHECKED.** Logged no-loss maximum 0.5997 at 5.456Δ; asymptote 0.5901–0.5905 over 10–60Δ. Independent confirmation from DC-83/CMPMC (VALIDATED): 0.5687 (4.5Δ), 0.5948 (6Δ), 0.5901 (10Δ), 0.5907 (100Δ), against the book's 0.5681, 0.5946, 0.5902, so they agree to ≤ 6e-4. Guruswamy p.2 "0.57–0.6" ✓ and Sect. V "≃ 0.59 at τ_l/τ0φ = 8" ✓.
A5. Guruswamy comparison (l.109, lim:20.4a). **CHECKED.** Offsets −0.0013…−0.0110 for r ≤ 4 and −0.0362…−0.0405 at r = 8 are as logged. Fig. 4 inputs (P_s 0.2, P_p 20 aW/µm³, T/Tc 0.1) ✓. Probe +2 % and excess energy +4 % in Sect. V ✓. τ_l/τ0φ ≈ 0.5 on p.3 ✓. The digitization (±0.005) cannot be re-checked without the figure; it is accepted as logged.
A6. Thin-film numbers (s20-4 l.100, l.122). CHECKED: p_pb 0.835/0.930; local maximum 0.5598 at 5.203Δ; Y(10Δ) = 0.3486/0.4150/0.4771/0.5240/0.5540; 0.238 at 60Δ; band change −20.5/−6.5/−1.7 %; 0.7 THz = 16.08Δ, 9.50 and 4.81 quasiparticles, range 0.299–0.590.
   - **WRONG** l.122: "where the film costs up to 40 percent of the infinite-volume yield". 40 % is Guruswamy's ≤10Δ figure (cascade 41 % at 10Δ). Across the arrival band that sentence is about, the cascade at t_l/t0 = 0.5 costs 49 % (16Δ) to 60 % (60Δ). Fix: "40 % at 10Δ (Guruswamy, cascade 41 %), 49–60 % across 16–60Δ in the cascade".
   - **GAP** l.122 and fig:20-yield caption: "Down-converted phonons arrive at 0.7 to 2.7 THz (sec:20.2)". 20.2 states no such band (grep: no 0.7/2.7 THz). Either derive it, or cite 20.5's mean-field arrival spectrum (energy-weighted mean 4.35 meV = 1.05 THz, 26 % below 3 meV). Also, the band runs to 62Δ but the cascade grid stops at 60Δ.
A7. Electrode phonons (s20-4 l.126–130). CHECKED: 85/96 % (r = 4), 92/98 % (r = 8), 20Δ changes ≤ 0.019, 200Δ escape 0.39 %. Leman p.17 (Sect. V A) "13% … low frequency, ballistic" ✓, which arithmetically is 0.75/(2.96+3) = 0.126. Agnese Sect. 2 "recombination phonons" ✓. Ge ν_D 0.864e13 /s (Leman Table I) → 35.7 meV, factor 99 ✓. Isotope 140 and 2.11e3 /s, mean free paths 38.7 m and 1.54 m ✓.
   - Convention drift: "three-phonon decay … 0.3 s in germanium" uses Leman's A_anh 6.43e-55. 20.2 uses 1.61e-55 for Ge (→ 1.2 s), and the Hernandez value 1.65e-54 gives 0.12 s. Quote "0.1–1 s"; the ballistic conclusion stands either way.
A8. **RULING: replace 20.5's linear near-gap ramp by 20.4's logged cascade.** WRONG as drafted; recomputed below.
   (a) Physics text in s20-5 l.61 and l.74. "Luke energy between 2Δ and about 6Δ … one pair is broken … Y = 2Δ/E" is true only below 4Δ. The cascade gives 0.5 at 4Δ, 0.568 at 4.5Δ, 0.594 at 5Δ, 0.600 at 5.46Δ and 0.595 at 6Δ, so it is *above* 0.59 from ≈4.7Δ to 8Δ. Hence "−0.048 at 0.75 meV for the one-speed spectrum, whose energy sits between 4Δ and 6Δ where Y < 0.59" is **WRONG**.
   (b) s_ng (one Al film, primaries at Ȳ_prim):

   | s_ng at 0.75 meV | one-speed | spread |
   |---|---|---|
   | ramp (text) | −0.048 | +0.002 |
   | cascade, no escape | **+0.002** | **+0.018** |
   | cascade, t_l/t0 = 8 | +0.065 | +0.067 |
   | cascade, t_l/t0 = 4 | +0.126 | +0.114 |
   | cascade, t_l/t0 = 2 | +0.24 | +0.20 |

   "With Y∞ = 0.50 the gain is +0.06 for both shapes" corresponds to the cascade at t_l/t0 = 4 (Ȳ_prim 0.504) and is **+0.13/+0.11**. The sign statement "of either sign" now holds only marginally: with the cascade the gain is ≥ 0 at every computed point.
   (c) Two-film band, sub-gap lost. The flat-yield values 0.935–0.998 and 0.975–1.000 are unchanged (no near-gap model enters), and so are 0.992 (absorbed) and the ×10 bare loss 0.88/0.91.

   | near-gap value | spread @2 meV | one-speed @2.9 meV | spread @0.75 | one-speed @0.75 |
   |---|---|---|---|---|
   | ramp (text/log) | 1.040 | 1.094 | 0.900 | 0.892 |
   | cascade, no escape | **1.036** (max 1.039 at 2.2) | **1.088** | **0.910** | **0.934** |

   So the "1.04–1.09" band moves to **1.04–1.09 (1.036–1.088), i.e. by ≤ 0.006: unchanged at the quoted precision**. Its lower side, which the text never states, moves from 0.89–0.90 to 0.91–0.93. Report: the near-gap model also *lowers* 𝔯_coll at 0.75 meV, because primaries absorbed in the Nb-like film just above 3 meV get yield up to 1 (ε_prim 0.583 → 0.611). The text and the summary state only the lift. **GAP**.
   (d) With the escape-dependent cascade (the "escape-dependent values" of the ruling; same t_l/t0 for both films):
       - Two films, sub-gap lost: maximum 1.093 / 1.098 / 1.107 / 1.121 / 1.172 for t_l/t0 = 8 / 4 / 2 / 1 / 0.5; minimum down to 0.93 / 0.91 / 0.88 / 0.83 / 0.76.
       - One Al film, sub-gap lost, 𝔯_coll at ⟨E_L⟩ = 0.75 / 1 / 2 meV:
         - t_l/t0 = 4: one-speed 1.110 / 1.088 / 1.033, spread 1.057 / 1.050 / 1.022;
         - t_l/t0 = 2: 1.23 / 1.17 / 1.06 and 1.15 / 1.12 / 1.05;
         - t_l/t0 = 1: 1.45 / 1.33 / 1.12 and 1.31 / 1.24 / 1.09.
         - With sub-gap absorbed (κ = 1), t_l/t0 = 4, 0.75 meV: 1.129 / 1.124.

       Cause: the primaries arrive at about 24Δ_Al, where Y(t_l/t0 = 4) ≈ 0.50, while soft Luke energy is read at 2Δ/E (0.5–1) or 0.50–0.56. This is 20.4's own arrival-band statement (l.122), carried into the kernels.
   (e) Consequences: **WRONG** as stated, both are robust only for thick films:
       - s20-5 l.78: "the collection ratio that would explain [CDMS II] … more than 0.1 above one, outside every value of this estimate";
       - summary l.166: "none of this reaches …".

       20.3 puts a 60 nm film at t_l/t0 = 0.86–1.08 (0.72 with the 0 K set), and CDMS-type Al fins a few hundred nm thick at roughly 3–5. At those values the one-film estimate reaches or exceeds 1.128 for ⟨E_L⟩ ≲ 1 meV, and the two-film estimate reaches 1.10–1.12. Suggested rewrite: "outside the thick-film (t_l/t0 ≥ 8) estimate, 0.91–1.09; with film escape (t_l/t0 ≲ 4) the near-gap gain alone gives 1.05–1.1 at ⟨E_L⟩ ≤ 1 meV and more in thinner films". Update 19.5 l.151 and l.193 ("largest transport value 1.09 … collection alone is disfavored"), CORRECTIONS row 656 and SOTA l.695 ("transport ≤ ~1.09") accordingly. The 1.128 target [1.099, 1.152] is no longer outside the transport range once escape is included.
   (f) fig:20-rcoll caption: "rising linearly to 0.59 at 6Δs" → the 20.4 cascade. The green curve moves by ≤ 0.01 above 1.5 meV and by +0.01 at 0.75 meV. kern20_5.py yqp() docstring cites "1401.1937 p.8" for 0.59; the paper has 6 pages (the statement is in Sect. V, p.6).
A9. Mean-field kernels (s20-5 l.30–57). **CHECKED.**
   - Formulas: hit rate v/2d (⟨|v_z|⟩ = v/2) ✓; eq:20.5-meanfield daughter term 2p(E/E′)/E′ conserves energy (symmetric p, mean ½) and is dimensionally consistent ✓.
   - Inputs: v̄ = Σc⁻²/Σc⁻³ = 5.751 km/s, x_L = 0.0975, E_prim 62.0 meV ✓.
   - Outputs: 15.3 µs, 4.35 meV, 40.4/58.4/1.2 %, 0.262 below 3 meV, a_prim 0.591, ε_prim 0.583, closure 1e-6 ✓; s_sub analytic (A: (0.36/(4⟨E⟩/3))⁴; B: (0.36/2⟨E⟩)²) 0.085/0.017/0.005 and 0.13/0.058/0.032/0.008 ✓; ϖ_O 0.41/0.20/0.08/0.03 ✓; 30 vs 15 µs, 2.0 vs 1.0 % ✓.
   - eq:20.5-sign derivation: ratio = (1 − s_sub) + s_ng + κ s_sub ✓; solve-vs-identity agree to 3e-4 ✓.
   - Sources: Ren Sect. IV 1×1×0.4 cm and 2.65(2) eV ✓; Hertel Sect. 1 300/700 GHz ✓ (1.24/2.90 meV).
   - **WRONG locator:** ℓ_bare = 1e-3 "[Sect. IV G]{leman}" → Sect. III G (p.14). 20.3 cites III G correctly.
   - Convention drift: x_L = 0.0975 (isotropic 9.00/5.40) against NOTATION and 20.2's x_L(Si) = 0.093. State that 0.0975 is the isotropic-continuum value, or use 0.093. γ changes by 5 %, so the effect on the logged numbers is small.
A10. Three discrimination routes.
   - Primary route: f_soft = 64.1/3750 = 0.0171, Δ_soft = 0.0153, σ_pos cap 0.0077 ✓; the S ≤ ϖΔ/σ_pos logic ✓.
     - **WRONG/GAP (memory-time dependence)**: l.89 "lose … memory within about 10 ns and 30 to 100 ns". Revised 20.2 (l.129) says these times hold only for band-top births: births over the upper factor two take 0.15 µs (Si) and 1.0 µs (Ge), and the 22 meV TA daughters of an ER are forgotten only near 1 µs in Si.
     - The 20.2 bound at 1 µs is 0.15 against an actual 0.012 (20.2 l.156). So eq:20.5-primary is a model estimate (actual ≈ 0.012 ≈ Δ_soft), not a bound. Write "≃", not "≤", or state the condition E_mem below every hard birth.
     - **WRONG** l.94: "a position class, a few percent of the volume of a 4 mm crystal". 20.2 gives a near-face shell of 0.21 / 1.7 / 13.5 % at 10 ns / 100 ns / 1 µs, and 36 % at 3 µs. At the ER memory time of about 1 µs it is 13.5 %. The verdict paragraph (l.153) inherits this; add "and ≈1 µs for the transverse daughters of electron recoils".
   - Gap route: E_g/ε = 0.312, (1 − Y)·0.312 = 0.280 ✓, eq:20.5-gap ✓ (sign NR − ER), t1 = 3.865 t0 at Y = 0.102 ✓ (state the Y dependence). Leman Sect. V A 13 % ✓.
     - Notation drift: b(t), b_ER, b_NR are the retired names; NOTATION row (clash 91) and 19.5 use f_ret(t), f^NR_ret, f^ER_ret. The release scale t0 here collides with the Kaplan t₀ of 20.3/20.4 (NOTATION row 1293); 19.5 eq:19.5-bimol carries the same clash.
   - Low-bias route: eq:20.5-lowbias re-derived in sympy (diff 0) ✓; maximum (1 − √Y)/(1 + √Y) at g = Y^(−1/2) ✓, 0.516 ✓; ϖ_O,min 0.129/0.240/0.451 ✓; f_det = 0.873 (Albakry 12.7 %) ✓, F_NR 0.9 ✓.
     - **WRONG** l.108: "Its ceiling … 10.3 at 100 eV". This is an artifact of disc20_5's bias grid starting at 0.3 V; S_low rises monotonically as V → 0 to **10.80**, equal to the zero-bias ideal charge-and-heat value (disc20_5.log "zero bias 10.802"), as the sentence itself claims ("that of the charge yield itself").
     - Minor: g = 3.1 with g = f_det g_Luke is **13.4 V** at f_det = 0.873 (11.7 V at full collection), not "near 12 V".
     - Minor: the route uses Y_q while the script uses Y′_q (3.75/3.8); state it.
   - Hertel Sect. 3: "better than 1:10³, 7 < E < 20 keV, limited by statistics" ✓.
A11. HV ceiling. **CHECKED.**
   - eq:20.5-hv re-derived in sympy from ΔN and the two variances (diff 0) ✓; 1/g fall ✓.
   - WE: 26.67, 23.28, 0.1066, 58.67, 765.9, 31.54, 5.459/7.343/1.885, 0.5635/0.2309, 3.076/1.695, S = 1.2205 ✓. Mean-charge 1.503, f = 1 1.324 ✓; F_NR threshold 0.213 (mean charge), unreachable (binomial) ✓; bias series 16.8/10.7/3.4/1.22/0.43 ✓.
   - Envelopes: 1σ maximum 1.724 at 220 eV, 2σ > 2 on 100–224 eV, maximum 2.457 at 100 eV ✓. The 2σ value at 220 eV is only 2.015, and the 224 eV edge depends on the log-linear interpolation between the 220 and 460 eV rows; say so.
   - Albakry Eq. (1) ε = 3.8 eV and Table II rows ✓.
   - **GAP** (WE l.139, table l.194): "The most favorable corner … Y 0.098, F_NR 0.4, gives 1.72" holds in the *mean-charge* limit only. In the binomial limit the same corner gives 1.36. Add "(mean-charge limit)".
   - Editor convention item: F_eh = 0.119 (measured, ER) against 20.1's cascade 0.114. State it; it moves S_HV(220) by +0.004 (1.224).
   - Campaign comparison: SOTA's WP8-R verdict (1σ maxima 1.26 at 100 eV and 1.72 at 220 eV) matches the book's 1.268/1.724. Its "2.014 at the 1σ corner of the constructed 300 eV envelope" is a different construction (the book: 1.451 at 300 eV, 1σ). This is not a superseded value; it is already in the editor notes.
A12. Consistency of 𝔯_coll with 19.5. 1.128 (19.5 l.191) is "more than 0.1 above one" ✓ as arithmetic. **WRONG** as a robust exclusion once film escape is included (A8 e).
A13. Summary and nuisance table against the final sections.
   - Summary 20.2 paragraph (l.160, drafted from SPINE): **WRONG**. "lose the memory … within about 10 ns and 30 to 100 ns" → "for births near the band top; 0.15 µs (Si) / 1.0 µs (Ge) for births in the upper factor two, ≈1 µs for the transverse daughters of an electron recoil in Si". The table row "Memory loss of prompt phonons" needs the same fix.
   - Summary 20.4 paragraph (l.164): **GAP**. "near 0.57 to 0.6 in thick films" → "0.590 without escape (infinite volume; literature 0.57–0.6); in the cascade 0.54–0.55 at t_l/t0 = 8 and 0.24–0.35 at 0.5 over 10–60Δ". The table row "Quasiparticle yield above 4Δ": basis "est." → "model (computed)". "Up to 40 %" holds only at ≤ 10Δ (see A6).
   - Summary 20.3 paragraph and the "Interface transmission" row: consistent with the *current* 20.3 (0.934/0.327, 0.22/0.28 ns, 6–26, factor 1.26), but against the 20.3 ruling (0 K Al primary: t̄_esc 0.368, t_l 0.187 ns, t_l/t0 ≈ 0.72). Update after 20.3 is revised, and add the 0 K set to the row.
   - Summary 20.5 paragraph and "Collection ratio" row: add the escape-dependent values (A8 d/e) and the near-gap lower side 0.91–0.93; "none of this reaches …" is WRONG (A8 e). ϖ_O values ✓; the 0.13–0.45 contrast ✓; 0.28(1 − b) → 0.28(1 − f_ret); 3.87 t0 ✓; HV row ✓, plus "(mean-charge)" on 1.72.
   - Summary 20.1 paragraph and its rows: 0.632/0.736/0.787 ✓, 0.125–0.158 ✓ (charge20_1.log), 6.3–12.6e4 cm⁻² ✓ (ε0 is the static dielectric constant in the book's units), 5–10 h ✓ (0.127 trapped per pair: 5.2–10.3 h), position term 1.2e-4 N̄ ✓.
A14. ch20.tex l.4: **WRONG** (editor note). "Luke phonons collected 15 percent better" → about 13 % (𝔯_coll = 1.128 in revised 19.5). The rest of the opening checks: 26.7 pairs, 31 eV, 69 eV; 34 pairs at Y = 0.127, 0.9 keV, 55 eV ✓.

## B. Other checks (all CHECKED unless marked)
B1. s20-5 l.3: 0.102 × 100/3.8 = 2.68 pairs, 100/3.75 = 26.7 ✓. l.7: 1 keV/3.3 meV ≈ 3e5 phonons, about 7e5 per cm³ in a 1 g crystal (0.43 cm³), 5.0e22 atoms/cm³ ✓.
B2. eq:20.5-functionals and 𝔯_coll = ϵ_Luke/ϵ^ER_prim match the NOTATION row 1267 gloss (the Part II note on Luke over primary is resolved) ✓. ℭ_s is "the fraction ending as quasiparticles", as E.25 requests ✓.
B3. Notation and convention drift against NOTATION.md:
   - (i) f_soft and ω_op in s20-5 l.89 and the table → f_s, ω_opt (rows 509, 1288; 20.2 uses f_s, ω_opt).
   - (ii) b(t) → f_ret(t) (A10).
   - (iii) t0 overloaded: Kaplan t₀ (row 1293) vs the release scale of eq:20.5-gap and eq:19.5-bimol. Suggest t_rel there.
   - (iv) c_s for the coverage fraction: rule 4 reserves the warning for sound speed, but c_ν is the sound-speed family; use 𝔠_s or f_cov,s to avoid confusion.
   - (v) Γ_em is already the boson-emission rate of WE 4.8 (row 450). 20.4 reuses it for the quasiparticle emission rate; add a local gloss or rename it Γ_qp-em.
   - (vi) x_L 0.0975 vs 0.093 (A9).
   - (vii) New symbols without NOTATION rows: s_sub, s_ng, κ_sub, ℭ_s, a_X, φ_X, O_obs, 𝒮_sep, 𝒮_HV, σ_pos, ℓ_bare, Γ_abs, Y′_q, ε_src, F_eff, E_sub, E_leak, t_pb, p_pb, N̄_qp, N̄_ph, Δ_soft (20.5 sense). The Δ_soft of 20.2 row 1290 has the same meaning ✓.
   - No factor-2 or π drift found: Y_qp = ΔN/E with no factor 2, consistent with the SOTA η_pb resolution; t_pb normalized at 2Δ.
B4. Campaign returns, CORRECTIONS, SOTA and DC-RESULTS:
   - No superseded value is used in my sections. The toy 0.87–0.98 is correctly marked superseded (CORRECTIONS 656). The Luke mean energies 0.75–4.7 meV match DC-83 (Si within 1.1 %, quoted range unchanged).
   - DC-83 (VALIDATED) supports A4.
   - DC-41 (conserving 𝔤_I) does not bear on phonon pair breaking, where v_F q ≫ ω (20.4's statement stands). It would bear on a statement about DM/photon *rates*, and 20.4 makes none.
   - DC-67 F 0.11398 = 20.1's 0.114; 20.5 uses the measured 0.119 (A11).
   - Rows to update if the editor accepts A8 e: CORRECTIONS 656 and SOTA 695 (19.5 pointer).
B5. Dimensional analysis. All displayed results are consistent:
   - eq:20.4-Y, -split, -tpb, -ppb and -emit, with the overall scale absorbed;
   - eq:20.5-kernel, -Gabs [1/s], -meanfield [1/energy on both sides], -sign, -sep, -primary, -gap, -lowbias and -hv (all dimensionless).
   - Limits checked: Y → 1 as E → 2Δ ✓; S_HV(g → 0) is the charge-and-heat value ✓; S_HV ∝ 1/g ✓; 𝔯_coll → 1 at κ = 1 with flat yield ✓; ϖ_O = 1 − a_prim while Luke < 3 meV ✓.

## C. Corrections list (for the reviser)
1. s20-5 l.61 and l.74 (A8 a, b): rewrite the near-gap paragraph with the cascade. s_ng = +0.002 (one-speed), +0.018 (spread) at 0.75 meV with no escape; +0.13/+0.11 at t_l/t0 = 4 in place of "+0.06".
2. s20-5 l.76 and the caption: the band stays 1.04–1.09 (cascade 1.036/1.088). Add the lower side 0.91–0.93 and the escape-dependent values; replace the ramp by the cascade in kern20_5.py.
3. s20-5 l.78, summary l.166, the table row, 19.5 l.151/l.193, CORRECTIONS 656, SOTA 695: "outside every value" → thick-film only; with escape (t_l/t0 ≲ 4) 𝔯_coll reaches 1.05–1.13 at ⟨E_L⟩ ≤ 1 meV in one film.
4. s20-5 l.89, l.94, l.153, summary l.160 and the table: memory times and near-face volume per 20.2 (0.15–1 µs; 13.5 % at 1 µs).
5. s20-5 l.108: 10.3 → 10.8; "near 12 V" → 13 V (f_det = 0.873).
6. s20-5 l.139 and the table: 1.72 "(mean-charge limit; binomial 1.36)".
7. s20-5 l.44: Leman Sect. IV G → III G. s20-4 l.47: the eq:20.4-tpb locator (Leman has no t_pb).
8. s20-4 l.122: "up to 40 percent" → 41 % at 10Δ, 49–60 % over the arrival band. Source the 0.7–2.7 THz band.
9. ch20.tex l.4: 15 % → 13 %.
10. Notation: f_s, ω_opt, f_ret, t_rel, x_L; add the NOTATION rows of B3 (vii).
11. Minor: Al ρ 2.73 (6.47 km/s, 313); MC "1.2σ"; Ge decay "0.1–1 s"; state F_eh = 0.119 as measured vs 0.114 cascade.
