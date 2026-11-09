# Ch22 part 1: derivation check (isolated). Files: ch22.tex, s22-1.tex, s22-summary.tex

Reviewer: derivation verifier (long-form-writing SKILL §5). Read against: accepted tex of Ch4, 8, 10–21, App. E.14/E.16/E.18; state/CORRECTIONS.md, SOTA.md (incl. R19 FBC, book-phase blocks), DC-RESULTS.md; returns/R18/REF-DC-49-54-36.md §4; figscripts/ch22 logs (we22_1, fig22_1, index22_1, gaps22_2, scope22_3). Sources fetched to sources/review-ch22/ (2512.08857, 2401.11971); PDFs deleted. Algebra/numbers: scratchpad chk22.py (sympy + mpmath).

Verdict: 5 WRONG, 7 GAP, everything else CHECKED. No superseded campaign value used. No DC quoting restriction violated.

## WRONG (fix before acceptance)

W1. s22-summary.tex ¶2, "The missing step is a specified calculation in 53 of them, a measurement in 11 and a proof or method in 8": WRONG. s22-2.tex l.19 and gaps22_2.log give **55 / 11 / 6** (sum 72). Correction: "in 55 of them, a measurement in 11 and a proof or method in 6".

W2. s22-summary.tex ¶3, "For $^{125}$Te at 1 MeV the Fermi function is 6.34, 4.3 % more than with the charge of the parent": WRONG direction. scope22_3.log: F(53) = 6.338, F(52) = 6.062, so the parent charge gives 4.35 % *less* (as s22-3 l.72 says), and the daughter gives 4.5 % *more*. Correction: "…is 6.34; with the charge of the parent it would be 4.3 % lower". (See also G7 on the convention behind 6.34.)

W3. tab:22-calc, row "Binding, trapping and capture rates…": "capture fraction (0.56 % closes the silicon Fano gap)": WRONG against the home. s18-5 l.39, s18-summary l.11 and tab:18-nuisances (l.34) give f_cap = **0.54 %** (0.32–0.77 %). The 0.56 % is (0.119 − 0.114)/0.886 with the rounded F; Ch18 uses the unrounded model F ≈ 0.1142, which reproduces 0.54 % and the 0.32–0.77 % bracket exactly. index22_1.log carries the stale 0.56. Correction: "0.54 %".

W4. tab:22-calc, row "Drag mass of crystalline silicon…": "drag mass now the atomic 14 m_e" and check "atomic limit δM_κ = N_e m_e of eq:4.3-TRK": superseded by sec:12.5. There the trace rule eq:12.5-trace makes 14 m_e (per atom, Q = 0) *exact* for the crystal, and the quantity a kick measures is the on-site element δM_II. Its valence part is 18.6 m_e, bounded to 12–24 m_e (tab:12-nuisances, row "Valence on-site drag mass", basis "bound"), and the total is 28.7 m_e, δM_II/M = 5.60e-4 (s12-5 l.90). Correction: Result → "on-site drag mass δM_II, valence 18.6 m_e (12 to 24 m_e, bound); the trace value 14 m_e is exact but is not the on-site element"; Check → "trace rule eq:12.5-trace (14 m_e per atom at Q = 0); acoustic sum rule; eq:8.6-fsum-k"; Home → add sec:12.5. The prose ("a few parts in 1e4", l.109) still holds (2.7e-4 to 5.6e-4). sec:8.6 l.118 ("the crystal value has not been computed … we take it as the estimate") is stale in the same way. That is a Ch8 light-pass item, outside these files.

W5. tab:22-calc, row "Finite-momentum Bethe–Salpeter…": "most of the one-standard-deviation factor 1.48 at 3 MeV": WRONG attribution. In we:10-band3 / we:21-rpaband the variance shares are attraction 39 %, tabulation spread 54 %, band energies 4 %, local fields 3 % (β = 0.247, 0.289, 0.078, 0.064; recomputed). The BSE calculation alone shrinks the band only from 1.482 to 1.358. The 93 % that s21-4 quotes needs the BSE *and* the converged IP table of the next row (band → 1.106). Correction: "with the converged independent-particle table of the next row, 93 % of the variance of the factor 1.48 at 3 MeV (the attraction alone 39 %)". The prose at l.105 ("dominated by the attraction … and by the disagreement between … tables") is correct.

## GAP

G1. tab:22-calc, cascade row "Cascade without a fitted constant…", and prose l.111. The result list omits the largest miss of the no-fit cascade: R19 FBC ε_eh = 4.15 eV [3.95, 4.73] plus a class systematic ≥ ±0.4 eV, against the measured 3.749 eV (SOTA R19; s18-4 l.16; s18-summary l.9, row l.28). That miss is set by the ionization rate below 4.5 eV, which is exactly what the "impact ionization from the GW self-energy" step computes. The row and l.111 present only F (0.114 against 0.119) as "the test", but the full band also gives 0.114, so F cannot separate the calibrated model from a first-principles one. Add to Result: "ε_eh 4.15 eV [3.95, 4.73] (class systematic ≥ ±0.4 eV) against the measured 3.749; 0.6 eV unexplained against Nielsen–Fischetti". At l.111: "…the pair energy (4.15 against 3.749 eV without a fitted constant) and the Fano factor (0.114 against 0.119) are the tests". The other R19 numbers quoted are CHECKED: 0.097 [0.030, 0.173], F 0.114, envelope 0.173/0.030 = 5.77 ("almost six"). The ~10× step-model overcount is not quoted in Ch22, which is fine.

G2. tab:22-calc header claim (l.31, "lists the open calculations of the book, each once"): not true as written. Open calculations specified in the homes but absent from the table and from Fig. 22.1:
- zero-T two-phonon absorption of Si in the one-phonon band (sec:11.6, 11.9-open; E.17);
- amorphous WSi disorder-averaged loss function and local-gap distribution (sec:15.3; E.20);
- the strong-coupling factor in the superconducting phonon-assisted form (sec:15.4; E.20 "computes the rate with and without it"), which Fig. 22.1 names as calc:O for Al but no row carries;
- the magnon ladder / bound pair of NiO and YIG (sec:14.2; E.20);
- G_OA(q,ω) at keV momenta for Te or α-quartz (sec:14.5; E.20);
- the Ch16 calculation-limited group of sec:16.9 l.40: ejected-electron final state, periodic finite-q BSE of a molecular crystal, excitons of a semiconducting tube, donor valley-orbit coefficients, layered stack beyond effective medium, α_ohm (E.10, E.11, E.21, E.22).
Either add rows (they can be grouped) or qualify the claim: "the open calculations that change a result for the running example or a contrast target; sec:22.2 lists the rest".

G3. Fig. 22.1 / fig22_1.py, row "Two-level systems in glass": marks data:F, theory:O. sec:16.9 tab (TLS at mK) reads "data (P̄); calculation (α_ohm); theory (interactions)". Add calc:O. The filled-marker counts are unchanged.

G4. Fig. 22.1, row "Nuclear recoil, Si lattice": data:F. The dominant item in tab:21-dominant is "computed phonon frequencies against measured, 0.24 %", basis "computed", so its basis is not data. The classification holds only if read as "measured dispersion would replace the computed one". Either state that reading in the caption or mark calc:F. If changed, the counts at l.130 become calc 12 / data 9, so the text must follow. Low priority, since the band is 0.25 %.

G5. l.134, "five deciding measurements of tab:21-guide and sec:19.5": the cold absorption edge of Si is not in tab:21-guide. Its home is sec:13.9-open (l.190). Add \cref{sec:13.9-open}. The other four (Ge pair energy at mK, TeO2 elastic constants, ²¹⁰Pb, two-bias) are CHECKED against tab:21-guide and s19-5.

G6. s22-summary.tex ¶1 (editor Q4: drafted before final 22.1). It matches the final 22.1 in content but omits 22.1's two results: the sorting outcome (22 channels: 11 calculation, 10 data, 2 theory, with the Si phonon-assisted window under both) and the short list (four calculations: PA loss function on common bins, coherent Si Migdal response below 2q_BZ, L(k,ω) of the survivors, close-collision kernel; five measurements). It also omits that the heavy-mediator CRDM recast is settled. Add one or two sentences. Everything the paragraph does say is CHECKED.

G7. s22-summary.tex ¶3 / eq:22.3-fermi convention (derivation-2 owns s22-3; flagged because the summary quotes the number). The 6.34 uses the prefactor 4, i.e. Behrens–Bühring F_0 without L_0. With the prefactor 2(1+γ_d) (F_0L_0, point nucleus), which s22-3 calls the "alternative convention", I get 6.09 (mpmath), and 5.84 for the parent (ratio 1.044). s22-3 calls its form "the point-charge solution of the Dirac equation evaluated at r_A", and the point-charge density at r_A is the 2(1+γ) form. Suggest the summary say "Fermi function F_0 = 6.34 (6.09 with L_0 = (1+γ)/2)", or that derivation-2 settle which one the text means. The 4.3–4.5 % daughter/parent statement survives either convention.

## CHECKED: ch22.tex opening

- "Between 0.333 and 0.405 MeV … only through the phonon-assisted rate … factor of ten (sec:13.9)": s13-9 l.3, 87; E.14 l.3. ✓
- "no calculation predicts how much charge a silicon recoil of 100 eV releases (sec:19.2)": s19-2 l.128. ✓

## CHECKED: 22.1 text

- l.13: 350–450 core-hours (E.14 l.15). ✓
- l.17–25, exact relations: every cited label exists (script check). The sector shares (8.6-fsum-e/k/ek), the transfer rule to order g⁴ (13.7), Hankel/positivity/KK, the Ward/soft/ASR/boost relations and M3 are cited correctly. One-pair condition: a second pair needs a carrier ≥ θ_ii E_g, so it holds for ω < (1+θ_ii)E_g. ✓ Cubic: no ℓ = 2 (s11-7 l.51). ✓ NiO spin sum rule (s14-1). ✓
- l.89: the factor 20 at 1.20 eV and the 25 meV window (s13-9 l.190); ×9 at 0.36 MeV and factor 3 (tab:21-dominant). ✓ Onset shift 2δω/v_max² = 8.54e-5 MeV for 0.3 meV (recomputed; E.14 l.56). ✓ "A few tens of core-hours": E.14 gives ~3 core-hours per direct-DFPT wavevector (tab:E14-params "10" for 3 Q); with new ground states at two lattice constants, "a few tens" is a fair estimate. ✓
- l.105: 1.48 at 3 MeV (s10-10 l.3, 118); ×3.2 at 1 MeV tabulation (tab:21-dominant; s21-4 l.57 gives band 3.4, 91 % tabulation). ✓
- l.107: Ge onset 0.2119–0.2141 MeV (s13-1 l.86). ✓ Hybrid without SOC: 2512.08857 p.3 and Fig. 1(a), "Γ-Γ and Γ-L band gaps of 0.775 and 0.823 eV" at α = 0.25, PAW non-relativistic pseudopotential (no SOC). Above α = 0.28 the order inverts, with errors of 34 % and 17 % at 0.34, so no α in the scanned 0.21–0.35 gives both. ✓ Optional precision: the gaps are at the HSE-optimized a = 5.71 Å, 1 % above experiment. "Fitted L below Γ can still miss curvatures": consistent with DC-2-alpha (masses +23 %, +39 %). ✓ Consistent with DC-2 (HSE06+SOC also inverts); the text does not claim hybrid+SOC will work. ✓
- l.109: 0.75 keV–2q_BZ (tab:12-nuisances); factor 1.2–1.4 (s12-3-validity); (16.6/1.17)⁵ = 5.75e5 → 5.7e5 (s17-5 l.195). ✓ Drag mass "few parts in 1e4" ✓ (see W4 for the table row).
- l.111: Born parameter Zα/v_F 15 / 35 (s19-2 l.66; 14.6 in s19-3). ✓ Envelope ×5.77. ✓ F 0.119 against 0.114. ✓ (but see G1)
- l.113: 1.128 against 0.81–1.02, final 𝔯_coll band (CORRECTIONS l.656/661; s19-5 l.151, 191–193). Not the withdrawn 0.87–0.98 or 1.05–1.13. ✓
- l.115: quarter percent above 100 meV at 30 MeV (s11-9 l.3, 94). ✓
- l.117 boosted recast: matches REF-DC-49-54-36 §4 items 1–3 in substance (10⁻⁴; ≤10⁻⁴; R^(−1/2); <1 % for m ≥ 10 keV; ~3 keV pole at 𝒬 = ω; 0.05–0.93 at 1 keV). Bib key liang2025plasmon = arXiv 2401.11971, the source REF-DC names; fetched and the Si/Ge setting confirmed. No withdrawn number (R = 0.14, ×2.7) is used. 𝒬 agrees with NOTATION l.780. ✓
- l.121–132, classification. Each Fig. 22.1 row was checked against its home and tab:21-dominant: Si ER 1–10 MeV calc; velocity/Ge 3d calc (bounds); PA window calc+data; Ge edge calc; GaAs polar data/calc:O; anharmonic theory/data:O (s11-9-open); Migdal <3 MeV calc/data:O; Migdal ranking calc; heavy-mediator ranking data (TeO2 C_ij, 21.7); NiO calc; Al data/calc:O (editor Q3: gap bulk vs film ×1.23 is data, so ✓); ZrTe5 data/calc:O (16.9); strong Dirac/dense donors theory (16.9 l.38); recoil charge calc/theory:O (editor Q3: s19-2 l.128, ✓); pair statistics calc/data:O; new pair energies data/calc:O; collection data/calc:O (two-bias decides, kernels E.25); delayed signals calc (s19-6 l.187); backgrounds data; published limits calc. Counts 2/11/10 over 22 rows (+1 double) = fig22_1.log. ✓ Exceptions: G3, G4. ZrTe5 ×2.8 (we:16-band). ✓
- l.134: four calculations, 352 eV. ✓ (G5 for the measurement list)

## CHECKED: tab:22-calc rows (other than W3–W5, G1)

- Si PA: 0.333–0.43; end of lead 0.42–0.43; two-channel 0.43–0.51 (s13-9 tab; CORRECTIONS l.570); 20 K edge, frozen phonon at X (E.14 l.42–44). ✓
- ω_TA(Q*): 0.3332/0.3374; scaled 0.3336/0.3378. 2(1.17+0.01479)/7.023e-6 = 0.33740 MeV, scaled shift +3.73e-4 MeV (recomputed); 0.3 meV bracket (E.14 l.56–58). ✓
- Pair channel: 0.3–2.6, pair residual unsized (s13-9 l.89; SOTA Ch13 block supersedes [0.4, 1.8]). ✓
- BSE: ×1.28 for 3.6–10 MeV (tab:21-dominant; s21-4 l.76); coupling block 10 % (s10-10 l.35); f-sum to a percent (s10-5 l.123). ✓ (W5)
- IP/all-electron: ×3.2, ×1.34, ×1.24, ≥16, 1.1–1.2 against 0.93 at 0.3–0.7 q₀ (s10-10 l.13, 38, 42; s10-4 l.72). ✓
- Ge 3d: 0.07/0.69 at 30 MeV; −0.76 % (s10-6 l.58, 125). ✓
- Ge window: 6³ grid; L gap within 0.1 eV of 0.744 eV; band masses (E.14 l.62–64). ✓ Known item: E.14 still specifies HSE06+SOC, which fails per DC-2. Editor Q2 has queued E.14. The row says "quasiparticle bands", which is correct.
- Coherent Migdal: "nearly all … up to 1 MeV, 33 % at 2, 7 % at 3 MeV"; 14.9 (tab:12-nuisances l.178; s17-summary l.27). Consistent with SOTA "≥ 99.8 % at 0.42–1 MeV"; Ch12 tex prints only "nearly all", so Ch22 matches its home. ✓
- Off-diagonal ε⁻¹: 1.2–1.4, lower end not bounded; ×1.35. ✓
- Wannier bound 1.6/0.54/0.25 at 20/50/100 eV (s12-3 l.189). ✓
- L(k,ω): P(first) 0.315 (NaF), 0.498 (NaCl) (s21-7 l.59, 83; s17-6). ✓
- Close-collision kernel: 352/399 eV (s19-2 l.24, 37: 51197 × 1.17²/(16 × 12.46) = 352 ✓); Si 0.10 at 100 eV (data 0.102); Ge (25 ± 3) % at 254 eV (s19-2 l.100). ✓
- Pair energies outside range: GaSb 0.83, width 0.21 (s21-7 l.15, 77). ✓ The 0.973 in 17.6 belongs to the floor row, a different row, so there is no conflict.
- Measured ε_eh 3.749 (Si), 2.96 eV (Ge, 77 K) (s18-4 l.3, 66). ✓
- Collection: 0.81–1.02 against 1.128. ✓ Traps/Luke (sec:20.1). ✓ Frenkel ~5 %, eq:19.6-sumrule (s19-6 l.29, 43). ✓
- Anharmonic: q_BZ–20 keV, ±0.2 % (s11-5 l.31, 145). ✓ All-electron density response / Ward. ✓ Cubic harmonics: ℓ = 2 zero; no first moment for ℓ ≥ 4 because the f-sum is isotropic (local potentials; with a nonlocal PP only to δ_NL accuracy, still a valid test). ✓
- GaAs: ≤3 %, −19 % parametric (s11-9 l.51, 53). ✓ NiO 7.8 % (s14-1 l.89). ✓ Al α²F_tr: 1.25e4, λ_tr 0.39 (s15-4 l.73, 134). ✓ ZrTe5: 1.33 × edge, Sommerfeld > 1.5 (s16-1 l.79). ✓
- Xe 1s 1/r, 1.7 at 56.5 keV (s10-9 l.176). ✓ Boosted light-mediator row ✓ (as above).
- Not in Ch22, no action: spin-current ALP g_aee 6.1e-13 (s15-4 l.126, SOTA) is not quoted in my files, so there is nothing to compare. It is also not in tab:22-calc; its open dressing (F₁ᵃ, λ_ep) is an s22-2 item.

## CHECKED: we:22-fsum (all numbers against we22_1.log; algebra in sympy)

- Kinematics: q²/2m_e = 1e6/(2 × 510999) = 0.97848 eV; 1 keV = 0.50677 Å⁻¹ = 0.43804 (2π/a) at a = 5.431 Å (log 0.43796 at 5.43). ✓
- Band-sum f-sum, eq:E.7-fsum. sympy: e^{−iqx}[H, e^{iqx}]f = (q²/2m)f − (iq/m)∂_x f. Its expectation in a Bloch state is q·v^g + q²/2m (Hellmann–Feynman), and a nonlocal V adds δ_NL. ✓ Dimensions: eV on both sides. ✓
- Local EPM, 531 PW, Γ: 0.1514/0.9265/0.9939/0.9992/0.9996 of 3.9139 eV; closure 8.6e-14 ("9e-14"). At k = (0.1, 0.2, 0.3): target 3.1135 eV, closure 4.5e-14 ("5e-14"). ✓ Γ target = 4q²/2m_e because Σ_v q·v = 0 at Γ by cubic symmetry. ✓
- "4e-4 left at 100 bands; shortfall 0.11": 1 − 0.89. ✓
- Cauchy–Schwarz: ρ*b = (√Δ ρ*)(b/√Δ) with Δ_m > 0. ✓ Dimensions: ρ is dimensionless, b = g/Δ is dimensionless, RHS [eV][eV⁻¹]. ✓
- θ_ep = 0.010–0.016 (s8-5 l.14, 46; s13-3 l.21); f-sum tolerance 2 % (E.16 l.36); 0.02/θ = 2.0–1.25. ✓ Z_v m_e/M_cell = 8 × 0.511/52330 = 7.81e-5. ✓ (θ² + share)/θ = 0.0178, 0.0209 → "1.8, 2.1 percent". ✓ Labeled as an estimate. ✓
- GAP (minor, no G number): the PBE 0.81/0.89 values hold for |q| = 0.1–0.5 Å⁻¹ (s13-9 l.188; E.14 l.80), while the WE applies them at 1 keV = 0.507 Å⁻¹, just outside. Write "at the upper end of the range where…" or quote |q| = 0.5 Å⁻¹.
- Wording (minor): "|q| = 1 keV … inside the off-shell window". The window is a condition on ω at given q (s13-3 l.7), not on |q|. Suggest "at |q| = 1 keV, where the off-shell window ω ≤ E_min(q) − δ_w is open".

## NOTATION / convention drift

- N1 (minor). we:22-fsum writes Z_v for valence electrons per cell (also s13-7 l.18). NOTATION l.1209 lists Z_val. Use Z_val or add Z_v as an alias.
- N2 (minor). we:22-fsum uses local Δ_m (energy difference) and b_m. Δ carries the gaps Δ_BCS, Δ_D, Δ_χ. Suggest ΔE_m or ε_m − ε_v inline, or declare it local.
- No factor-2, π or sign drift found in s22-1. θ_ep, δ_NL, q_BZ, M_cell (52.33 GeV), v^g and 𝒬 all agree with NOTATION.

## Campaign-number audit

- Checked against CORRECTIONS/SOTA: 𝔯_coll 0.81–1.02 (final) ✓; 1.128 ✓; screening 0.3–2.6 ✓; F 0.114 ✓; 0.097 [0.030, 0.173] ✓; Migdal coherent band ✓; 352/399 eV ✓; boosted CRDM (REF-DC §4 wording) ✓; Ge HSE (DC-2, DC-2-alpha) ✓. No superseded value found. Omission only: ε_eh 4.15 (G1).
- DC-RESULTS restrictions: DC-49/54/36 quoted only from REF §4 ✓; DC-67 P_casc library not quoted (the row asks for the tables as a future calculation) ✓; DC-2: no claim that hybrid+SOC gives the Ge edge ✓; DC-41/DC-93/DC-91 not used ✓.

## Editor-note items

- 22.3 Q1 (verify the Fermi strength A−2Z in the IAS and the overcount 73 vs 21): ✓. With T = T_z = (N−Z)/2 in the isospin limit, T₊ (p→n) annihilates the parent, so S₋ = N − Z = 21, all to the IAS (|⟨IAS|T₋|i⟩|² = 2T). One conversion per neutron gives N = 73, and 73/21 = 3.48 → "3.5". IAS: (6/5)Zαħc/R = 14.98 MeV, minus (m_n − m_H) gives 14.19 MeV. "About 14 MeV" ✓. Phason: 0.23 THz = 0.951 meV; 250/0.951 = 263, 300/0.951 = 315 ✓.
- 22.3 Q4: see G6. W1 and W2 are the numeric faults in the summary.
- 22.1 Q2: ✓ (see the l.107 entry above). Q3: ✓ (recoil charge, superconductor). Q4: ~2 % is labeled as an estimate ✓.
