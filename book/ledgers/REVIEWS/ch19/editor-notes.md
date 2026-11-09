# Chapter 19 editor notes

## 19.3 drafted (2026-11-06; ~3,900 words; Limit Checks 19.3a, 19.3b; 2 F rows)
- Main result: the Lindhard yield depends by ~13 % at 1 keV on how the softest collisions of the slowest secondaries are modelled (the cross-section below x = 2e-3: x^{1/3} vs local slope). This exceeds the error of the Lindhard formula itself (≤ 3–5 %). The Si data lie 8–38 % below the formula at 0.1–3.9 keV. The cross-section is the writer's construction (Thomas–Fermi small-angle); the Winterbon–Sigmund–Sanders form has no readable source. Derivation review PRIORITY: is the 13 % band an honest model uncertainty?
- Bethe stopping within 10 % only above 1.84 v_F; Si recoils are at 0.013–0.13 v_F (friction regime). WE: Si mean excitation 20.3 eV (valence only) vs 161–174 eV from the loss function vs adopted 173.0 eV; the L shell carries 2/3 of the logarithm.
- thomas1925zahl is the sum-rule paper, not Thomas–Fermi. Check other chapters that cite it for Thomas–Fermi.
- Lindhard 1963 credit only; Lindhard–Scharff 1961 via Sarkis 2023.
- g_L clash (Lindhard function vs Luke gain in 19.5).
- Limit Check numbering prints "19.1/19.2" with the chapter counter while the labels are lim:19.3a/b. Check that the box numbering scheme matches the other chapters.

## 19.1 drafted (2026-11-06; ~3,730 words; Ch19 opening + map; retitled "Nuclear recoil on the Born–Oppenheimer surface")
- Retitle accepted (gesturing-title rule); fix SPINE at the merge.
- Key results: classical propagation of the Wigner-shifted ensemble reproduces the impulse approximation eq:11.4-IA with exact mean and width (misses c₃); threshold as a smooth step (σ_ω 0.72 eV at 12.5 eV; 1.6° direction scatter); Si regime boundaries 0.41/0.54/12.5–36 eV/0.87–4.6 keV ↔ m_χ 28/32/154–262 MeV/1.3 GeV; partition keyresults eq:19.1-partition, eq:19.1-heat. PRIORITY derivation.
- E.23: "lattice heat" for E_heat → reword (E_heat = all phonon energy, as in 18.1; E_lat = the lattice share). The Massey length ℓ → ℓ_int (ℓ is the Lindhard log). NOTATION p_FP row cites "P_FP of E.23": fix.
- E.11: "zero-point motion does not matter above 10 eV" holds only for the mean threshold.
- ⟨ω⟩ = 40.9 meV (book) replaces the research 45 meV throughout.

## 19.2 drafted (2026-11-06; ~3,310 words; fig:19-yield; 2 F rows (no box))
- Key result: binary threshold E_R,th = (M/m_e)E_g²/(16E_F): 352 eV Si, 399 eV Ge (book gap/lattice; 336/387 with v_N²). SPINE LO(i) and E.23 l.3/27 say 395: update. Soft threshold: in the EPM model 0.56 % of valence electrons are promotable at 100 eV (model, an understatement). Landau–Zener kernel; Born parameter ~15, so non-perturbative. The Migdal part of Y_q is E_R-independent in the soft limit, 3.9–4.4e-4 (0.4 % of the measured yield at 100 eV). The double-counting rule is stated. PRIORITY derivation.
- Zener 1932 unread (form from Vutha 1001.3322).
- v_th clash → v_{N,th}. New symbols in the SEAM.

## 19.6 + summary drafted (2026-11-06; ~5,270 + 1,620 words; Limit Checks 19.6a/b; 2 F rows; tab:19-nuisances 22 rows)
- 19.6a: closed form D = (6T²/⟨q²⟩)[1 − I₀(A/T)⁻²] for tight-binding defecton diffusion, checked by finite difference. The T⁻⁹ law holds within 10 % for T ≥ 0.28 band widths. SPINE says "T below the band width": fix SPINE (Pushkarov Eq. (61) holds above; T⁻⁷ below). The low-T coefficient is 2× Pushkarov Eq. (64) (his estimate). PRIORITY derivation.
- 19.6b: Frenkel–Kontorova vs continuum kink within 10 % for width ≥ 1.74 a; leading energy correction −a²/72d²; barrier from App. C.20.
- Illustrative inputs, labelled: tunnelling exponents, Al interstitial barrier/width, V₀ ≈ 1 eV, pocket energies, phonon collection 0.25 (2208.02790).
- 19.5 collection ratio 1.154 (1.144 only as a variant) vs SPINE 1.144. Recheck the summary/nuisance rows after the 19.4/19.5 reviews.

## 19.5 drafted (2026-11-06; ~4,700 words; D.45 ~1,400; Limit Checks 19.5a/b; 4 F rows; NOTATION 19.5 block rewritten)
- Balance law eq:19.5-balance (configurational E_st; ΔZPE with phonons; W_bias = eV·N_ind by Ramo); NR/ER heat ratio 1.407 at 100 eV with no gap release; ≤ 3.5 % gap energy still held for 1 % of unity; calibration identity eq:19.5-calib; exact bound E_st/ω ≤ 1 − Y_ph on 𝔯_coll ≥ 1 (widens for 𝔯_coll < 1); two-bias inversion (0.9195 vs 0.952 at 40 V). PRIORITY derivation.
- 𝔯_coll = 1.154 with book inputs (ε_eh 3.75 eV; f_ion 0.346 Lindhard at 20 keV) vs SPINE 1.144 (y = 0.3, 3.82 eV): adopt 1.154 (the WE prints both). The Lindhard f_ion range 0.30–0.51 over 10–100 keV (research 0.22–0.35): a collection-only prediction gives 0.964 at 100 keV (just outside), 0.955 with the source's 75 % collection.
- E.25 ρ_g − 1 = 0.24 → "about 0.25" (0.254 at f = 0.346).
- g_L clash: rename the Luke gain visibly (g_Luke) at review; ϵ_Luke for the efficiency.
- The transport sign of 𝔯_coll − 1 is given as a reason only; 20.5 must carry the number with a script.
- 19.4 must cite eq:19.5-identity, eq:19.5-bound, app:D.45 rather than re-derive them (check at review).
- Fig. 19.4 inputs are illustrative (18.5 rates; E_st at the 19.4 bound; 59 µs single exponential from 2007.14289); ΔE_zp ~0.1 eV is an estimate.

## 19.4 drafted (2026-11-06; ~3,470 words; Limit Checks 19.4a/b; Table 19.1; 2 F rows)
- Displacement count from a first-collision equation with the K–P rules + the 19.3 screened cross-section: factor 0.70 vs the standard 0.8 (NRT, as quoted by Nordlund); the formula lies 11–14 % above for T_d ≥ 10 E_d; hard spheres give T_d/2E_d exactly; MC agrees. PRIORITY derivation.
- Bounds 0.055 (Si) / 0.064 (Ge) at 95 % C.L. under four conditions; 0.086 at 𝔯_coll = 0.9; no stored energy needed above 𝔯_coll = 1.154. Agree with the returns. p_surv·E_FP/E_d bounds 0.20/0.28 (Si 10/100 keV), 0.23 (Ge) vs the returns' 0.21/0.20 (Lindhard damage fractions; measured Pb 0.3). With book E_d = 36 eV, p_surv is only ≤ 0.73–1.04 at 10 keV (the returns' ≲ 0.47 used 9/20). Update SOTA after review.
- Ge E_d = 19.7 eV is model-conditional (four reasons; detectors of opposite polarity differ by 2.06σ).
- The four conditions are listed in both 19.4 and 19.5: keep them in one place (19.5, with the derivation) and point from the other.
- ξ_d new; Y_ph first use moves to 19.4; g_L double meaning still open.

## Ch19 review rulings (2026-11-06; five reports: derivation-1/2, prose, reader-a/b — MINOR GAPS / REVISE, no REWRITE)
- R1. ε_eh in the calibration (19.5 l.108 and everything downstream; also 19.4 Table 19.1, 19.6, the summary). CDMS sets its phonon scale and subtraction with 3.82 eV, while the Luke phonons follow the true ε. Model this correctly with the book's ε_eh = 3.75 eV (DC-67: 3.7468) and, per R2, the source's own yield fit. Recompute in bal19_5.py/def19_4.py the stored-only value, the edge (≈ 0.049), the collection-only 𝔯 (≈ 1.13–1.15), the two-bias numbers (≈ 0.9475 at 40 V) and the Si/Ge bounds. State the bound with a fifth condition (holds while the true ε ≤ 3.82 eV) and quote the book-ε value. Update every printed number from the logs. Remove the "does not depend on ε_eh" claim.
- R2. The worked example's "75 %" is relative to the Chavarria fit y_C, not Lindhard, and the source says Lindhard overestimates below 20 keV. Use y_C where the source does (f_ion 0.324 at 20 keV) and combine with R1 in one script (one 𝔯 value). Give Lindhard as the variant.
- R3. Lindhard soft-collision band (19.3): present it as a sensitivity, not an uncertainty. Give the exponent scan (0.30/0.363/0.40 → −11/+13/+39 % at 1 keV), state that the ε^{1/6} law follows from the assumed x^{1/3} continuation, and that the Thomas–Fermi x^{1/2} tail keeps the electronic share finite. Correct the nuisance row and the summary.
- R4. WE 19-lnI (19.3): remove the unit-dependent "normalized to the exact f-sum" variant (174 eV) and the "L shell 2/3, valence 1/6" split. Quote the data value 161 eV (and the adopted 173.0 with its source). Withdraw the editor-note claim.
- R5. Number fixes:
  - free-gas fraction vanishes at 336 eV (text and Fig. 19.2b);
  - shortest phonon period ≈ 65 fs (also E.11 by narrow edit);
  - the 1.6° scatter is per transverse component (2.3° polar);
  - "3 % at 500 eV" → 1.9 % with the exact bracket;
  - Migdal pairs model-free 2.3–4.4e-4;
  - 19.5 l.29: zero-point energy 61 meV per atom (31 is half); state the sign of ΔE_zp;
  - 2U = 298 eV; b = 0.52 → 1.158; 0.026; 58 µs;
  - Si M consistent (26.06 GeV, check against the book constants);
  - the Sarkis U_FP = 23.6 eV is not a Frenkel-pair formation energy (the book gives 7–10 eV): rename it per the source;
  - 19.6 l.166: electron recoils displace above the 19.4 onset (0.14 MeV): fix;
  - 19.6 R₀ = a(3V₀/Δ)^{1/4} from the stated criterion (crowdion 12–22 spacings), or change the criterion to match the formula with a reason;
  - 19.4 C_cal sign as in 19.5;
  - define "flashing" or replace it;
  - ω_p double meaning; bracket vs D/D_9 in 19.6.
- R6. Structure: move all calibration machinery, the bound, the widening and conditions (a)–(e) into 19.5. 19.4 states the result (Table 19.1) and points to 19.5. Merge Limit Checks 19.4b/19.5b into one (in 19.5) and re-letter if needed. 19.6's low-energy-excess discussion quotes the bounds with their conditions and adds the grown-in-defect term to its energy bound (or states it is excluded). The Ge damage fraction 0.7 rests on the surface yield 0.3: say the 0.23 bound is not conservative.
- R7. Prose:
  - remove the process leftovers (the 1.144 sentence; the "two-standard-deviation edge" sentence; the g_L parenthetical);
  - name what "three effects"/"four conditions" are at each announcement;
  - cut the four-verb outline sentences in the 19.2–19.5 openers;
  - cut the repeats (threshold ≠ stored energy, tunnelling-only recombination, "one table", the friction wording, the E.23 pointers) and the empty paragraphs (19.2 l.109, 19.6 l.186/190, part of 19.1 l.134);
  - "lattice heat" → precise wording (opening, 19.1 l.9, E.23);
  - split the two condition-list sentences;
  - register;
  - provenance chains phrased as "as quoted by";
  - shorten the D.45 title.
- R8. Notation: Luke gain → g_Luke (visible rename, book-wide where it occurs). Resolve the doubles (x, e, b, ε, ω_p, p, ⟨q²⟩, E_φ vs E_φ-variant, Z, s in D.45; bare ℓ as path length in 19.3). Add the ~30+ missing Ch19 rows.
