# Chapter 17 editor notes

## 17.3 drafted (2026-11-06; ~2,950 words; no box/F row; new tab:17-endo)
- Key result: shell formula for the exothermic rate into a collective mode, halo-independent to O(v²/v_ν²), valid if the mode weight is smooth over m·v_max. Si phonons: 0.78–1.10 of the full calculation (weight varies on the zone scale). PRIORITY derivation check.
- WE 17.3 GaAs LO, m = 30 keV, Δ = −1 eV: 1,810/kg-yr vs 842 elastic; 2.6e4 at 10 keV.
- Fig. 17.3 uses two couplings at separate reference cross-sections (no common coupling in Si for a dark photon; Born charge zero). Accept.
- The 14.3 promise about exothermic DM at the Larmor frequency is closed in words only (no sourced YIG spin stiffness).
- Plasmon/electronic 0.09–0.16 compares the electron-gas model with crystal tables (labelled).
- Table numbering may shift (Table 17.1 planned for 17.5). Fix SPINE at the merge.
- s17-1 l.28 has a placeholder \SI{MIGEQ}{MeV} that broke the full build: 17.1 writer to fix (sent).

## 17.2 drafted (2026-11-06; ~2,970 words; Fig. 17.2 coverage map (3 panels); mass-decade table; WE 17.2)
- PRIORITY derivation: the key result that counting beats a quantum-limited linear readout by e^{m_φ/2T} in signal (14.6 bunched variance + Lamoreaux Eq. (9) linear noise, which assumes Poisson counts). Crossover m_φ ≈ T (0.86 µeV at 10 mK); background-free above ~20 µeV for a one-day record. Screening ceiling L ≤ 1/(2|ε₁|).
- ZrTe₅: the figure draws both 11.8 and 15.6 meV; rerun abs17_2.py once Ch16 R1 lands (the reach at 100 meV is barely affected).
- YIG dark-photon point (ζ = 7.6e-17 at 10 µeV) is derived here from 14.3's substitution; Ch14 prints no such number. Ruling: keep it only if 14.3's text supports it with a stated derivation line; otherwise drop it.
- GaAs density 5.361 g/cm³ kept to match 11.8, though Ch11 R6 says it implies the wrong lattice constant. Flag for a book-wide consistency pass.

## 17.1 drafted (2026-11-06; ~3,230 words + opening/map ~400; fig:17-sectors, WE 17-crossover, tab:17-boundaries)
- Migdal vs multiphonon/free-recoil crossover thresholds in Si (heavy mediator): 0.178 … 5.33 eV for 1 … 100 MeV; zero-phonon = phonon-dressed Migdal at 13.2 MeV; the electron-only acoustic peak equals ER at 12.3 MeV (model property, stated as such).
- The "one phonon" region up to ~20 MeV at a 1 meV threshold rests on the incoherent one-phonon term, valid within 10 % only above 18 keV (11.3). Review must check the consistency of the region boundary.
- Symbol clashes: ω_× (14.2), σ_n (per-nucleon vs 15.4 conductivity), ω_top vs ω_max (11.3).
- Ge crossover and GaAs acoustic edge "not evaluated" (no Ge phonon DOS / GaAs elastic tensor in the scripts). Candidates for DEFERRED or a literature value.
- The 17.3 file used \Volc (undefined); it is gone now. Watch the build.

## 17.4 drafted (2026-11-06; ~3,000 words; Fig. 17.4 kinematics; WE GaAs interference)
- Born-charge cross cell: exact cancellation of the dark-photon phonon rate in Si; GaAs removes 99.75/99.81 % (rate 216×/245× below bare nuclear charges). Zero-phonon cell: +5.47e-4 (Si), +4.83–4.88e-4 (GaAs).
- Key results eq:17.4-Sek (Migdal–phonon-assisted cross response), eq:17.4-bound (positivity; single-sector bound only inside the window), eq:17.4-lock/-rate (saturated at small q; |Ṽ_e − (m_e/M)Ṽ_nuc|²; vanishes for mass-proportional couplings). PRIORITY derivation.
- POSSIBLE TENSION WITH ACCEPTED CH12 (PRIORITY): the Ch8 boost identity (eq:8.3-boostward) forces the coherent small-q Migdal response to be (m_e/M)² × the electron response. 12.4 applies the diagonal soft-limit probability down to q ≈ 2 keV; at 2 keV it is ~16× above the identity, with a different shape. 12.4 may need a "q ≳ q_BZ" qualifier. The Ch17 derivation review must settle this; if 12.4 is wrong below q_BZ, raise a Ch12 erratum.
- "Ionic correction of the zero-phonon line" replaces "ionic screening" (the cell changes Im ε). Fix SPINE at the merge.

## 17.6 + summary drafted (2026-11-06; ~4,130 + 1,830 words; tab:17-widths, tab:17-rank, Fig. 17.5, nuisance table 16 rows)
- Leaders (P(first), independent errors): ER floor Ge 0.212 MeV (1.000); heavy-mediator single phonon TeO₂ 2.39× Si (0.968); nuclear edge diamond 3.11 keV (1.000); polar rate LiF (0.987); polar reach GaAs 10.35 keV (1.000). Migdal unreadable (0.315). Light mediator not ranked. Consistent with SPINE 21.7.
- Tier change vs the research ranking: Ge (measured tensor, FOM 1.69) falls below GaAs (database tensor, 1.87). The database speeds run 4.8 % low on Si/Ge/C, and correcting for that lowers P(GaAs > Ge) from 0.884 to 0.741. Stated in the text; a measured GaAs elastic tensor is needed (DEFERRED/data).
- New convention X_pole (log-uniform [1, 3]), stated as far narrower than the 5.7e5 range of 17.5. Review: is this defensible?
- The 11-crystal pool points to 21.7 for its selection rule; Fig. 17.5 uses Griffin's 24 (lead salts lead: PbSe 0.0484 MeV). Ge ahead of GaSb only through the estimated GaSb gap shift (0.973; reversed with no shift).
- Recheck the summary paragraphs and nuisance rows for 17.4/17.5 against their final text.
- CsI 3.7–3.8 uses the illustrative denser cold bound; Vallin read in abstract only.

## 17.5 drafted (2026-11-06; ~4,330 words; Limit Check 17.5a; tab:17-fom; WE diamond vs Si; fig:17-window)
- Valence partial f-sum (π/2)(ω_p^val)²/ε_core(0)² (Si core factor 0.970). Heavy-mediator ranking bias 1 − c_NR1/(135 km/s): crystals rank to 10 % only if speeds differ by < ~13.5 km/s. Pairwise windows (diamond/Si 24.8 keV–0.424 MeV, settles at 0.933; diamond/CsI only 87–227 keV): a common window against Si does not rank materials among themselves. PRIORITY derivation.
- Griffin et al. tabulated sound speeds for GaN, AlN, ZnO, CsI, CaWO₄ are inconsistent with measured elastic constants (CsI 3.73×Si, CaWO₄ 1.96 with measured tensors). Consistent with WP8 errata/CORRECTIONS §20.2.
- Polar FOM as a pair (band integral + mean optical frequency). Migdal pole factor: LiF 0.87, Ge 0.47 of Si; the gap bound reverses LiF/Si, so the order stays open (→ 21.7). Consistent with 17.6's "Migdal unreadable".
- The campaign window numbers came from the campaign halo; book halo onsets 3.7–4.1 edges, diamond/Si −6.7 %. 17.6 must use the book values (check at review).
- Worked example 4.7 normalisation (3.93 vs 4.13 valence electrons; 1.4 % overshoot): optional note in 4.4/4.7.
- LiF ω_p^val = 26.1 eV is free-electron (not measured).
- The last cross-reference edit is not rebuilt; tab:17-fom has 1.4/2.9 pt overfull lines.

## Ch17 review rulings (2026-11-06; five reports: derivation-1/2, prose, reader-a/b — MINOR GAPS / REVISE; 17.6.1 and 17.6.5 borderline REWRITE)
- R0. Migdal at q < q_BZ: Ch12 erratum under independent verification (ledgers/REVIEWS/ch12/erratum-migdal.md). The Ch17 reviser must NOT change Migdal numbers that depend on 12.3-soft/12.4-harm below q_BZ in this pass. Mark them in revision.md as "pending Ch12 erratum" (17.1 crossovers, 17.4, 17.5 pole factor, 17.6 Migdal rows). A follow-up pass applies the erratum.
- R1. Number errors:
  - WE 17.4 GaAs: without the cross cell the rate would be 403× (Ga)/521× (As) larger; 216/245 are bare nucleus vs Z*².
  - 17.3: one elastic rate (12.0 vs 17 → reconcile from the log), and the phonon factor 37× (not 31×; also in the summary).
  - WE 17.2: 122 meV at 10 cm⁻¹ (not 40) and 4.26 cm⁻¹ (not 4.6), or fix the formula if the numbers are right.
  - NiO ratio 3.1: show the missing weight factor (~1.2) or correct it to 2.54.
  - The NiO row of tab:17-endo uses c_M = 1.36e-4: 7.31/8.20/316 keV.
  - CsI 25 % (not 20 %); the η-shift nuisance 7 % (not 6 %); GaAs polar edge 10.35 keV everywhere.
  - "about 500 MeV" → ≈410 MeV; "escape speed" → v_max; Ge Θ_D 373 K; 1 + 2ΔS = 1.157; "against 32" holds for GaAs only (NiO 46).
- R2. 17.2 ZrTe₅: rerun abs17_2.py against the final Ch16 (whole 11.8 meV row: ζ 1.25e-15, ×6.3–6.4, cone end 0.38 eV).
- R3. 17.2 coherent vs counting: remove "a coherent detector overtakes below ~T" (it contradicts eq:17.2-ratio, which is > 1 at every mass). State the bandwidth assumption: the counter bandwidth equals the line width; Lamoreaux carries an extra (Q_c/2πQ_a)^{1/2}.
- R4. YIG dark-photon point in 17.2: add the one-line derivation (vacuum ζ from 14.3's substitution, random polarisation; 7.62e-17 reproduced) or drop the point.
- R5. 17.5:
  - WE 17.5: diamond outranks Si until ~14 keV, so replace "ranks correctly at every mass above the edges" with the true statement.
  - eq:17.5-pole: include the plasmon dispersion (LiF/Si 1.4–1.7 instead of 0.87), or state that it is ignored and give the size.
  - Ge pole factor: state the 3d-screening caveat.
  - Polar log formula: say which v (v ≈ v₀).
  - Remove 17.5.7 (pure recap); the polar subsection points to Ch11 instead of restating it.
- R6. 17.6:
  - The X_pole prior [1, 3] contradicts the book's Si spectrum (X ≈ 25 from 12.3). Rebuild the prior from the book's own numbers, or say that the Migdal medians are prior artifacts and that the caption medians include √3. Keep "no Migdal reading".
  - Add the GaAs 𝓘_pol width (0.04) to tab:17-widths, and make the caption match the text.
  - Rewrite 17.6.1 and 17.6.5 (borderline REWRITE in the prose review); remove the process sentences of l.31.
  - Don't repeat the CaWO₄ tensor from 17.5.
- R7. Figures and tables:
  - fig:17-sectors(a): cap the one-phonon region at the band top (63.7 meV); fix the linear acoustic branch up to q_BZ.
  - tab:17-boundaries: the GaAs 0.433 is the kinematic floor, not a zero-phonon edge.
  - The plasmon window uses the cutoff of the dispersion actually used (2.30 keV, 7.3 eV).
  - The Fig. 17.1 graphic says "Limit Check 17.5" while the caption says 17.1: fix.
  - Rerun map17.py.
- R8. Prose:
  - Apply the prose review (117 items): looped paragraphs; the measurement disclaimer once; values given only by citation get numbers; register (only/about overuse, add natural connectives).
  - US spelling; "cross-section" hyphenation per STYLE; punctuate eq:17.3-endolin.
  - 17.4.2: add the steps to derive Eq. 17.10.
  - Define Laue class and Brillouin scattering, or replace them.
  - The 21.7 references ("??"): plain prose until 21.7 exists.
- R9. Notation:
  - one per-nucleon cross-section symbol (σ_n vs σ_p; NOTATION's σ_n is the conductivity, so pick a non-clashing symbol);
  - n_B (Bose) vs the BO order: rename the BO order;
  - ω_top vs ω_max; ω_×; F_κ; σ_j;
  - add the missing 17.3/17.5 NOTATION rows.
