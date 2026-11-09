# Ch12 editor notes

## From the 12.3 writer (for the Ch12 batch review)
- Fig 12.2 (atomic, electron kinetic energy axis) vs Fig 12.3 (adds 8.15 eV ionization energy): unify the energy-axis convention.
- Valence drag mass from the computed first moment ≈ 18.6 m_e vs 14 m_e atomic estimate: 12.5 must address.
- Research-note value P_Mig ≈ 5e-3 at 1 keV (Si) is wrong; tables give 6.1e-2. Do not use the note value.
- Limit 12.3b: bound-lattice comparison shows <1e-5 effect; replaced by exact free-recoil amplitude (bound-lattice kept as second curve).

## From the 12.1 writer
- E.18 writes bare S(q;ω_l,ω_e); book form is S_ab — align in App E pass 2.
- Ruling needed at Ch12 review: E.18 says dropping off-diagonal (G≠G′) elements is wrong at O(1); Berghaus et al. call them small. 12.1 takes no side.
- Fig 12.1 P_Mig = 1.86e-6 is a labelled valence-only model value, not a full Si result.
- Commitment: Sect. 19.2 must separate the Migdal part of neutron-calibrated ionization yields.

## From the 12.2 writer
- Limit 12.2a plotted vs ξ_D (not suddenness ratio); F rows for 12.2a/b use n_D = 2 (rate order) — confirm at review.
- Cox et al. all-multipole tables: velocity-independent part (1.6e-4 Si, 1.3e-4 Ge) subtracted; stated in caption and F row.
- No Ge exciton binding energy in book; text says only "smaller than Si's 14.7 meV".
- App E pass 2: E.18 should send the core Migdal probability to sec:12.2, not sec:12.5.
- Cross-check for review: 12.3 reports P_Mig(Si, E_R=100 eV)=6.1e-3 = 29× atom; 12.2 gives atomic ionization at 1 keV 2.09e-3 (Si). Make the 12.2/12.3 energy-axis and P_Mig conventions consistent.

## EDITOR RULINGS (2026-11-02) — bind the Ch12 writers, reviewers and reviser
R1. **Off-diagonal (G≠G′) elements.** These are the local-field effects, and Limit 12.3a measures their size directly: the plain dielectric form is 1.35× too high overall and agrees within 10% only for p ≤ 1.3 q_BZ. So neither "order one" (E.18) nor "small" (Berghaus et al.) is right as stated. Book wording: "a ≈ 35 % effect on the total, concentrated at p ≳ q_BZ" with \cref{lim:12.3a}. 12.1 adds one sentence pointing there. E.18 is corrected in App E pass 2.
R2. **Energy axis.** The book convention is the total electronic energy transfer ω_e, ionization energy included, because that is what the detector records. Fig 12.2 is replotted on ω_e (shift by the binding energy). Captions name the axis "ω_e (electronic energy transfer)". Both figures use the same axis.
R3. **Valence drag mass.** Both numbers stand. 14 m_e is the free-atom estimate (12.2). 18.6 m_e is the first moment of the computed crystal valence spectrum (12.3). 12.5 reconciles them with the first-moment sum rule: the excess comes from the crystal's valence response beyond the atomic count. If 12.5 cannot close the gap, it states the residual as a nuisance.
R4. **12.2 choices accepted:**
  - Limit 12.2a is plotted against ξ_D.
  - Its F rows use n_D = 2, consistent with the 8.5 ruling that 𝔗 orders count powers in the rate.
  - The velocity-independent part of Cox et al. is subtracted, and the subtraction is stated.
R5. **Ge exciton.** Quote the indirect-exciton binding energy of Ge, 4.15 meV, with its literature citation (Macfarlane et al. absorption-edge data; verify the reference at revision), in place of "smaller than silicon's".
R6. **Limit 12.3b** with the exact free-recoil amplitude is accepted; the bound-lattice curve stays as the second curve, with the <1e-5 statement in the caption.
R7. **Fig 12.1** keeps the valence-only model value of P_Mig, labelled as such in the caption. The full-silicon number is the 12.3 result, and 12.1 cross-references it.
R8. **Research-note P_Mig(1 keV) ≈ 5e-3** is wrong and is not used anywhere. The table value is 6.1e-2.

## From the 12.4 writer
- CONFLICT (ruling needed): 12.3's exact free-recoil bracket (eq:12.3-bracket, limit12_3b.py) keeps y = (q−p)·p/M from KKL Eq. (3) but drops p²/2M in both denominators; with both kept the free amplitude is b/[(ω−b+a)(ω+a)], b = q·p/M, a = p²/2M, leading term b/ω² = the soft-limit numerator. The "3p²/q²" correction, "soft limit fails first / within 10 % for m_χ ≥ 16.5 MeV", lim:12.3b's 0.495 at 5 MeV and the matching F-row text are O(p/q) artefacts. Checked in figscripts/ch12/osc12_4.py (log). 12.4 states the correct physics (eq:12.4-corr) and does not cite 12.3's numbers.
- Brief misattribution: the Eq. (3.11) sign misprint and the factor-2 Eq. (4.8) are in 2603.13052, not 2210.06490 (v1 only on arXiv). Recorded in the lim:12.4a F row.
- 12.6 nuisance table: frame of the transition density (×2.4 on the phonon-emitting fraction at q = 5 keV), incoherent lattice factor at small |q−p| (zero-phonon Bragg sum within 8 %), G ≠ G′.

## From the 12.5 writer
- R3: reconciled structurally, not closed. 14 m_e = trace Σ_J δM_IJ (exact, derived D.34); a kick measures the on-site δM_II. Si on-site = 10.1 (cores, Cox) + 18.6 (valence, KKL LF, Z_ion) = 28.7 m_e; band 12–24 m_e for the valence; a 1D short-range model gives the opposite sign of the off-site sum. 12.6 nuisance table must carry the row (text points to sec:12.6).
- 8.6 l.120 / 12.1 "both corrections below 1e-3 of E_R": P_Mig (Si table) is 1e-3 at E_R = 16.5 eV and 3 % at 500 eV; restrict to the phonon regime.
- App E pass 2: E.18 l.3 ("valence follow only in part, so 14 m_e is an upper estimate") contradicts the tables; E.18 l.31 core P_Mig → sec:12.2; E.17's relativistic 37–45 % → derived 40–45 % (Ge/Ga/As), 8 % Si (D.34).
- Build: ch11/s11-7.tex l.79 contains a literal "\n\n" (undefined control sequence).

## EDITOR RULINGS (cont.)
R9. **PRIORITY: 12.3 free-recoil bracket.** The 12.4 writer finds that eq:12.3-bracket and limit12_3b.py keep (q−p)·p/M but drop p²/2M from both denominators. With both kept, the leading term is q·p/(Mω_e²), which is the soft-limit form. If so, the following are artefacts of order p/q:
  - the "3p²/q²" correction;
  - "soft limit holds only for m_χ ≥ 16.5 MeV";
  - lim:12.3b's 0.495 at 5 MeV;
  - the F-row text that matches them.
  The Ch12 derivation reviewer verifies this independently (sympy plus osc12_4.py). If confirmed, the reviser rebuilds Limit Check 12.3b with the corrected bracket and aligns 12.3 with eq:12.4-corr. Until then no other section quotes those 12.3 numbers.
R10. **Attribution fix.** The sign misprint and the factor-2 error are in arXiv:2603.13052 (Eqs. (3.8), (3.11), (4.1), (4.4), (4.8)), not 2210.06490. Correct every place in the book that says otherwise.
R11. **⟨p²⟩^{1/2}.** The 12.1 value (5.6 keV, Z = 4 model) and the 12.4 value (6.1 keV, Z_ion weight) both stay, each labelled by its model. 12.5 or 12.6 states which one the book's headline numbers use.
R12. **12.6 nuisance table.** It includes:
  - the transition-density frame (a factor 2.4 on the phonon-emitting fraction at 5 keV);
  - the incoherent lattice factor at small |q−p| (Bragg sum within 8 %);
  - the G≠G′ terms (≈35 %, R1);
  - the Ge Debye-scaled estimates.
R13. **PRIORITY (Ch12 derivation review): 12.6 new results.** Verify independently:
  (a) the finite-frequency Born-charge sum rule eq:12.6-sum. It gives Z*(1 eV) = −0.165 in Si, so the crystal radiates 33–38× its atoms. This overturns the research note's |Z*| ≈ 0.05 and its "comparable" verdict.
  (b) Bremsstrahlung needs only ω_γ ≫ ω_ph and q above the zone, not the impulse condition. GaAs is enhanced 4.94e3 at 1 eV and 1.87e4 over the band.
  (c) For mass-proportional scalar absorption, the loss-function form is exact at dipole order, and Dzuba et al. hold within 10 % only for m_φ ≥ 57 eV in Si.
  If (a) is confirmed, log it in state/NOVELTY.md.
R14. **Valence drag mass (12.5).** The band 12–24 m_e (Si) and 11.5–52 m_e (Ge) is accepted and goes into tab:12-nuisances (the 12.6 reviser adds the row if it is missing). 12.5 then points to \cref{tab:12-nuisances}, not to sec:12.6.
R15. **Accepted-chapter fix (Ch12 reviser may edit).** 8.6 l.120 and 12.1 say "both corrections below 10⁻³ of E_R". That fails above E_R ≈ 16.5 eV on the Si tables, where P_Mig = 3 % at 500 eV. Restrict the claim to its true range in both places.
R16. **App E pass 2:**
  - E.18 l.3 must not call 14 m_e an upper estimate (see 12.5);
  - E.18 l.31: core P_Mig belongs in 12.2;
  - E.17: the relativistic contact factor is 40–45 %, not 37–45 %.
R17. **12.3 bracket (R9) has a second independent confirmation.** Reader-a re-derived the exact amplitude b/[(ω−b+a)(ω+a)]; it has no p/q term, so y = (q−p)·p/M in 12.3 is the error. Unless derivation-1 refutes it, the reviser:
  - rewrites eq:12.3-bracket, Limit Check 12.3b, the 12.3 opening and the F row to the 12.4 result (the soft limit holds at every q, up to eq:12.4-corr);
  - aligns D.33-soft and tab:12-nuisances.
R18. **GaAs Ω = 44.80 Å³.** This is the measured zero-temperature cell, a = 5.638 Å (Table E.1, Ch11 ruling). Label it at each use; do not change it to 45.17.
R19. **Reader-b items:**
  - Ge nonrelativistic third moments are "about 30 % low", not 40 % (1/1.425).
  - ε̃ is "symmetric", not "Hermitian".
  - The count of nonrelativistic operators is the standard 14 (15 with O_2), or rephrase so no count is given.
  - Define GPAW at first use, and define "tagged recoil".
  - Every number in the displaced-oscillator WE must land in a script log (rerun or fix): 1.0463 eV, 65.5 meV, 0.188/0.192 eV, 0.056.
  - GaAs Ω: see R18; keep 44.80 Å³ and label it.
R1′. **AMENDS R1 (my R1 was wrong).** The ≈35 % in Limit Check 12.3a is the local-field effect on the DIAGONAL of ε⁻¹. Its caption says the off-diagonal G≠G′ elements are in neither curve.
  - The book attributes the 35 % to diagonal local fields only, as 12.4 l.77 does. Fix 12.5 l.67, the first row of tab:12-nuisances and anything else that credits the 35 % to G≠G′.
  - The size of the off-diagonal G≠G′ terms stays OPEN. State it as an unquantified nuisance, noting that E.18 and Berghaus et al. disagree. Take no side unless the derivation review supplies a number.
  - Use the wording the prose ledger proposes (prose.md E1).
R20. **12.2 vs 12.3 on valence.** 12.2 must not say the atom gives the valence probability "to an order of magnitude", because 12.3 finds the crystal valence at 47× the atomic value. Rephrase 12.2: the atom fixes the core channel, and the crystal changes the valence channel by more than an order of magnitude (\cref to 12.3).
R21. **Ge at 1 keV.** One value book-wide, taken from the we12_2/fig12_2 logs. Reconcile 1.63e-3 against 1.73e-3 (a possible all-shell vs ionization-only difference): label each if both are meaningful, otherwise fix the wrong one.
R22. **R9 is CONFIRMED by derivation-2.** The exact bracket is b/[(ω−b+a)(ω+a)]; the 12.3 form gives 1+3p²/q² (25.35 vs 0.99944 at q = 2 keV). The reviser rebuilds Limit Check 12.3b and removes 3p²/q², 16.5 MeV, 0.495 and F-rows l.335. 12.4 l.41 then states the result positively, with no dispute against 12.3. **R13(a)–(c) are confirmed.**
R23. **Derivation-2 numbers (12.5, D.34):**
  - with 28.7 m_e: δM/M = 5.61e-4, first moment 0.280 eV, off-site sum −14.7 m_e; fix the script's 10 m_e core;
  - R_rel radius sensitivity: 0.10 % (Si), 0.53 % (Ge);
  - the Ge rigid core without the 1s holds 26 electrons;
  - D.34: 2ZR/a₀ ≈ 2–6e-3, and dropping e^{−2λr} overstates R_rel by 0.4 % (Ge).
  - Name the uncontrolled Dirac remainder and the p₁/₂ contact density in tab:12-nuisances.
R24. **GaAs lattice constant (supersedes R18 and Ch11 R6 if the source check fails).** Derivation-2 says 5.638 Å is 0.8 % below the measured value; the measured value is about 5.648 Å at low T and 5.653 Å at 300 K. Check Table E.1's source.
  - If 5.638 is not a measured value at any temperature, relabel it truthfully ("the cell of the Chap. 5 calculation" or similar) everywhere it is called "measured" (Ch5, Ch11, Ch12), keeping the numbers that depend on it.
  - Log the check in this file.

## R24 check (Ch12 reviser, 2026-11-03)
Table E.1's GaAs 5.638 Å is from Csonka et al. 2009, Table II: measured lattice constants extrapolated to 0 K with the zero-point anharmonic expansion removed, a static-lattice value that is not measured at any temperature (low-T measured ≈ 5.648 Å, 300 K 5.653 Å). Relabelled "static-lattice" in E-1 (column header and caption), s5-5 (Fig. caption), s11-2 l.184 and s12-6 WE 12-gaas; 44.80 Å³ and all dependent numbers kept. Not touched (out of the reviser's scope): ch06/s6-2 l.114 ("measured constants of we:5-lst" with Ω = 44.80 Å³); Ge a = 5.658 Å in 12.6 against 5.640 (Table E.1) and 5.652 (Table 5.x), flag for the Chap. 5 owner.

### Off-diagonal G≠G′ estimate (tight-binding/EPM)
(2026-11-03, compute agent; script `figscripts/ch12/offdiag12.py`, every number in `offdiag12.log`. Answers the open size in R1′; a model bracket, not the deferred first-principles calculation.)
- **Method.** Cohen–Bergstresser empirical pseudopotential Si (`ch03/epm.py`, 113–169 plane waves, gap scissored 0.82→1.11 eV), RPA χ⁰_GG′(k,ω) (Adler–Wiser, resonant + antiresonant, η = 0.15 eV), Γ-centred NK³ mesh reduced by O_h, local-field set |G|² ≤ 11–35 (2π/a)², ε̃ = 1 − v^½χ⁰v^½ inverted at each ω. Soft-limit Migdal weight ∫dω ω⁻⁴ L_Mig, direction-averaged boost, Z_ion(p) of `mig12`, then the rate of eq:12.3-rate (heavy mediator, free recoil, q_min = 0). Three forms: (i) full matrix, weight Z(p)Z(p′) p̂·p̂′ e^{i(G−G′)·X} e^{−⟨u_x²⟩|G−G′|²/2} averaged over the two atoms X = ±τ (the structure phase of the struck nucleus plus the energy-integrated nuclear umklapp factor); (ii) diagonal of ε⁻¹ (book form, lim:12.3a); (iii) scalar 1/ε_GG.
- **Reviser action (eq:12.3-FL).** As printed, eq:12.3-FL needs either the phase e^{i(G−G′)·X} of the struck nucleus or the statement that the origin of ε sits on the struck atom. At the bond-centre origin the phase-free form gives 1.8–3.0 and diverges in G. This also bears on how Liang et al. Eqs. (12)–(13) are cited. The Debye–Waller damping of the umklapp channels changes (i) by < 1 %.
- **Validation.** (iii)/(ii): the model gives 1.19–1.27 against 1.35 in lim:12.3a. Its p-profile matches the table's shape (1.05 at q_BZ, 1.16–1.18 at 2 q_BZ, 1.21 at 3 q_BZ, rising to 1.9 at 4 q_BZ), so the model carries about 2/3 of the diagonal local-field effect. The p-distribution of the weight matches KKL within 0.03 per q_BZ window. P(ii) at E_R = 100 eV is 1.13–1.23× the KKL value at NK = 8–10 and |G|² ≤ 11–19, falling with NK. η = 0.3 eV pushes it to 1.67 through near-gap Lorentzian tails under ω⁻⁴: the absolute value is η-limited, the ratios are not (η = 0.3 changes (i)/(ii) by −0.03). Checks: positivity of the single-atom forms holds (min (i)/(ii) per q,ω ≥ 0.39); ±τ agree to 1e-15; an O_h rotation check agrees to 1e-3.
- **Result.** (i)/(ii), the full matrix over the book's diagonal form, is 1.378 at NK = 8, |G|² ≤ 19 (main run). Against m_χ it is 1.41 (10 MeV), 1.39 (30), 1.38 (100), 1.38 (300 and 1000), flat within 3 %. In ω_e it is 1.43–1.47 below 6 eV and 1.11–1.23 above. The off-diagonal elements **raise** the rate in every one of the 13 runs.
- **Convergence and uncertainty.**
  - k mesh: extrapolating in 1/NK² lowers the value to 1.31–1.33.
  - G set: the diagonal (ii) is converged at |G|² ≤ 19, but (i) is not. It falls by 0.06–0.08 for each added shell group up to |G|² = 35, from cross terms with p′ ≈ 4–6 (2π/a). A point-ion run (Z = 4) drifts the same way (1.57→1.49 for |G|² 19→35 at NK = 4), so the drift is the off-diagonal response at large G′, where smooth EPM pseudo-wavefunctions are least realistic, not the core-resolving vertex.
  - Extrapolated central value: ≈ 1.2–1.3.
  - Band: **(i)/(ii) ≈ 1.1 to 1.45**, i.e. +10 % to +45 % on the rate.
    - The upper edge covers every run with NK ≥ 6 (largest 1.43; 1.38 at NK = 8).
    - The lower edge is where the k and G extrapolation stops, **not a floor the model proves**. The G trend has not levelled off, and a first-principles value below 1.1 cannot be excluded.
    - What the model establishes is the sign: (i)/(ii) > 1 at every truncation run (13 runs).
  - Relative to the scalar form, in the model: (i)/(iii) = 1.378/1.231 ≈ 1.12 at NK = 8, |G|² ≤ 19. Applying the band to the table's real diagonal effect of 1.35 gives (i)/(iii) ≈ 0.8–1.07. Either way, the diagonal local-field reduction and the off-diagonal enhancement largely cancel.
- **Suggested tab:12-nuisances wording** (row "Off-diagonal elements G≠G′", type normalization, basis "model"): "Raises the rate in a model, by about ×1.25 (×1.38 at NK = 8, |G|² ≤ 19, still falling with |G|; the lower end is not bounded), flat in m_χ within 3 % for 10 MeV–1 GeV; empirical-pseudopotential RPA with the structure phase of the struck nucleus; first-principles size deferred (app:E.18)."
R25. **Post-acceptance check** (postaccept-check.md): offdiag12.py and the eq:12.3-FL phase are CHECKED. Two GAPs remain for the next light pass:
  (a) Reword "≈1.2–1.4" in all six places, using the ledger's suggested wording. The range is not a bracket: it runs from the extrapolated value up to the raw NK=8/GM=19 result, and the G drift is not slowing, so 1.2 is not a lower bound. Also say the model captures only about 2/3 of the diagonal local-field effect.
  (b) State the index order of R⁰ in eq:12.3-FL. It fixes the sign of the phase, which matters for GaAs.
