# R11 referee REF-WP7-E-A (hostile, isolated): returns/R10/WP7-E.md + code/WP7-E/checks.py

Read: WP7-E, checks.py (run: 35/35 PASS, ≈2 s), WP0-v3 §7, WP5-v3 §1.2, §3–§6, §8, WP7-T (4.5) only (caller-permitted), CONVENTIONS,
NOTATION, CONTROLS, DONE, LIMITS. Full texts fetched into literature/papers-r11-WP7-E-A/ (2004.10709, 1803.02903, 1805.09942, 2007.14289,
2405.10405, 2208.02790, 2202.05097, 2001.06503) and deleted after use. No referees/, state/ or other briefs read.

## Verdict table
| # | Claim | Verdict | Reason (details §1–§6) |
|---|---|---|---|
| 1 | (E1) balance law, Theorem E-0 "exact" | STANDS WITH CORRECTION | first-law bookkeeping is right, but E_pairs+E_trap uses "μ any reference", which Lemma 1 itself shows is false once one carrier is collected (crystal not neutral); μ must be the electrode Fermi level. (H-E1) misses exciton/EHD binding and pair Coulomb energy. C2a/C2c do not test anything (§1) |
| 2 | (E3) two-stage factorisation, "coupling only through 𝐍" | STANDS WITH CORRECTION | Markov at t_pr is exact only for the full reservoir microstate. The listed 𝐍 lacks the t_pr phonon spectrum and positions and the carrier-cloud geometry, which 𝒫_det needs (the return's own IF-E7). c and r_ev are not additive, so they cannot sit in WP5's e^{ϑ·𝐍} (§2) |
| 3 | Theorem E-1, E_d counted once; (E5)–(E6) | STANDS (minor corrections) | correct: E_d is the parameter of P_FP, not a ledger entry. E_st^{frz} is defined "on the observation time" but (E6) integrates to ∞. 𝒦^{rel} has no carrier- or phonon-stimulated channel (§2) |
| 4 | Theorem E-2: E_st ⊂ E_nuc "exactly" in Si/Ge | STANDS WITH CORRECTION | electrons cannot *create* Frenkel pairs, but they can *change* E_st: recombination-enhanced defect reactions and athermal (ionization-driven) interstitial migration. "Exactly" holds for creation only (§2) |
| 5 | Theorem E-3: deficit of a trapped pair is E_g − E^tr_e − E^tr_h | STANDS WITH CORRECTION | right for a doubly trapped pair. The generic biased-detector case (one carrier collected, one trapped) stores μ_F − E_v − E^tr_h (or E_c − E^tr_e − μ_F), which depends on the contact. Table 3.4 and A-4 omit it (§1) |
| 6 | (E11) 𝒲_bias = eV_b N^meas (Ramo–Shockley) | STANDS | C5 correct; conditions (two electrodes, no space charge) stated. For CDMS-II ZIP and iZIP the multi-electrode form is required, so N^meas ≠ the single readout channel (L34) |
| 7 | (E12) compound law, F_meas = ⟨𝔵⟩F_eh + Var𝔵/⟨𝔵⟩ | STANDS WITH CORRECTION | correct conditional on r_ev. A reported F_meas averages over position: add ⟨N_eh⟩Var_r⟨𝔵\|r⟩/⟨𝔵⟩. A-10 imports the conditional form as "the measured Fano factor" (§3) |
| 8 | (C7) E_R^rec = ω − E_stored − E_esc; y^meas | STANDS WITH CORRECTION | the algebra is a tautology (C7b checks x = x). The physics omits that ε and the phonon scale are calibrated on ERs, which have their own ⟨𝔵⟩_ER and E_trap^ER (1803.02903 [FT]). So y^meas carries ⟨𝔵⟩_NR/⟨𝔵⟩_ER (§3) |
| 9 | (E8) windowed Y_H; "Y_H rises with t_win" | STANDS WITH CORRECTION | E_trap must enter as ΔE_trap (NR − ER), as E_esc and E_sl already do. The monotonicity holds only for the E_st^{rel} term. The NTL normalisation is ambiguous (§3) |
| 10 | mK emission frozen; "F ≈ 1.2×10⁶ V/cm" | STANDS WITH CORRECTION | **numerical error ×100**: checks.py uses ħc = 1.97327×10⁻⁷ eV·cm (true value 1.97327×10⁻⁵). The correct field is F ≈ 1.2×10⁴ V/cm. The conclusion (≫ 1–100 V/cm) survives with a margin of 10²–10⁴, not 10⁴–10⁶ (§4) |
| 11 | Event criterion; (a) TLS give power; (b) single-defect releases sub-threshold; (c) LEE needs collective release | STANDS WITH CORRECTION | (a) the stored-energy number is per unit λ (WP7-T (4.5)), so C12a and C12b contradict each other. (b) ignores amorphous-pocket recrystallisation (multi-atom, can exceed E_st,1). (c) quotes its sources selectively: 2202.05097 reports a stress null and 2208.02790 rejects a single exponential (§4) |
| 12 | Time laws (1/t, t^{−3/2}, exp, (1+t/t₀)⁻²); P_rel formulas | STANDS (minor) | C3 correct. erfc(d/√4Dt) is the 1D law; in 3D, P_rel = (r_c/d)erfc((d−r_c)/√4Dt), asymptote r_c/d < 1 (§4) |
| 13 | §4 literature limits L20–L22 + QF data | STANDS WITH CORRECTION | quotes CONFIRMED (§5). The NRT 0.8 factor is mislabelled "Kinchin–Pease". 1805.09942's f_DF is a two-channel E_R^rec deficit, so it contains E_trap. The 2007.14289 next sentence (Ge heat QF ≈ 1) is omitted. QFs are NR/ER ratios of 𝔵 |
| 14 | WP5-v3 amendment A-1…A-11 | STANDS WITH CORRECTION | A-1, A-2, A-4, A-5, A-7, A-10 and A-11 need changes; four required amendments are missing (§6) |
| 15 | §6 nuisances | STANDS WITH CORRECTION | after A-11 no θ covers prompt trapping (N_trap^{pr}, E_trap^{pr}); θ_coll has no ER/NR ⟨𝔵⟩ ratio |
| 16 | §7 computation specification | STANDS WITH CORRECTION | not sufficient for capture on shallow Coulombic centres at mK: NMP (WP4-v3 §6) is the wrong mechanism (cascade capture needed). Exciton/EHD formation in zero-field calorimeters is absent (§2) |
| L33 | Hecht → (E10) | STANDS WITH CORRECTION | derivation correct (C4). "Source [FT]" is not met (Hecht 1932, no FT quote): mark the source UNVERIFIED/classic |
| L34 | NTL gain eV_bN^meas from (E11); 1803.02903 Eq. (1) | STANDS WITH CORRECTION | Eq. (1) quoted correctly. Validity must name the multi-electrode Ramo sum (ZIP: two charge electrodes vs grounded phonon side) and space charge (θ_SC) |
| L35 | F_meas = ϵ_detF_eh + 1 − ϵ_det; corrects 2004.10709 App. A | STANDS | misprint CONFIRMED in FT (§5) |
| L36 | KP/NRT limit; f_DF fixes p_surv E_st,1/E_d | STANDS WITH CORRECTION | the measured f_DF (iZIP phonon − Luke, 103 keV ²⁰⁶Pb surface recoils) is the full (E8)-type deficit, including E_trap and surface ΔE_esc. The paper notes polarity-dependent charge collection. NRT/p_surv is ill-defined in a dense 103 keV cascade |
| L37 | unit heat quenching = truncation | STANDS WITH CORRECTION | the truncation must also set ΔE_trap = 0. "Wrong by up to ~13% at 1 keV" assumes p_surv = 1, excluded by MD, and is tempered by the source's own sentence that Ge measurements give ≈ 1 |
| L38 | two-channel recoil scale | STANDS WITH CORRECTION | add the ER-calibration factors (#8) |

Rubric (c), paper-is-wrong claims: **2004.10709 App. A (A6)–(A7) CONFIRMED** (variance term F·n must be η²F·n; their "lower bound"
is an upper bound). **1805.09942 E_d depends on TRIM's stored energy per displacement: UNRESOLVED.** The FT says "systematic error
does not include modeling imperfections in Geant4 and TRIM" but does not state TRIM's per-displacement energy, so C8 is an inference
about TRIM internals, not a verified error. **WP5 (W11) overstates the trap deficit** (internal): CONFIRMED (arithmetic, C9c).
Rubric (f): the return makes no explicit novelty or new-channel claim. The "collective stress release" reading of the LEE is the authors'
own hypothesis in 2208.02790 ("relaxation of thermally induced stress … is the source") and is not new. Nothing to credit.

## 1. Balance law and its exactness proof (rubric a, g)
1. **Reference μ.** Lemma 1 (C1a, correct) gives d(E_pairs+E_trap)/dμ = N_h,tot − N_e,tot. A carrier that reaches an electrode leaves the
   crystal charged, so the sum is μ-dependent exactly when trapping matters in a biased detector. (H-E2) then fixes μ physically: the
   collected partner "relax[es] to the Fermi level at the electrodes" (1803.02903 [FT], §2). Redoing the one-pair balance with a hole
   trapped at z′ and the electron collected, with the bias energy kept in 𝒲_bias and the NTL heat: the remaining stored energy is
   μ_F − E_v − E^tr_h with μ_F the electrode Fermi level in the band-aligned gauge, independent of z′. **Correction:** in §1.1 replace "μ any
   reference" by "μ = the contact Fermi level (H-E2); 'any μ' only for a neutral crystal". Add the singly trapped case to Theorem E-3(i),
   the Table 3.4 E_trap column and A-4: E_trap(single e) = E_c − E^tr_e − μ_F, E_trap(single h) = μ_F − E_v − E^tr_h. These depend on the contact
   (Schottky barrier, a-Si layers) and are O(E_g/2), not O(E^tr).
2. **Reservoir completeness (H-E1).** Missing: free and bound exciton binding (WP5 already writes E_g → E_g − E_x^b), electron–hole-droplet
   condensation energy in Ge/Si, and the Coulomb and image energy of separated, uncollected charge. In zero-field mK calorimeters, pairs at
   the edges form excitons before they recombine, so E_pairs = N_eh E_g is not the t_pr value there. These are meV per pair, but "exact" needs
   them listed, or a stated O(E_x^b/E_g) truncation.
3. **N_eh with unpaired carriers.** "ω = N_eh E_g + ℋ_pr + E_st + E_esc + E_trap^{pr}" (C2c, A-1) is wrong when one member of a pair is trapped
   before t_pr. E_pairs then contains the free partner's (μ − E_v), which is in neither N_eh E_g nor E_trap^{pr}. Write the t_pr balance with
   E_pairs + E_trap (μ = μ_F), and define N_eh as the number of fully free pairs.
4. **Checks.** C2a sums hand-built dictionaries that conserve energy by construction, so it tests notation, not physics. C2c is vacuous:
   it defines omega = N E_g + H + E_st + E_esc and checks that it equals itself. C7b, C9c and C5b are identities of the same kind. Rung 3
   (DONE.md) is therefore not met for (E1). A real check would be a stochastic toy (capture, emission, drift, collection) with the reservoir
   sum monitored.
5. **Verdict on exactness.** Granted complete reservoirs and the μ_F reference, (E1) is the first law with the bias as the only external
   work. Theorem E-0 stands with these corrections. Its [D] tag rests on (H-E1), which must carry the omissions of item 2.

## 2. Factorisation, E_d, yield and kinetics (rubric a, d, e)
1. **(E3) sufficiency.** "Condition on the reservoir state at t_pr" is exact only for the microstate. The return's 𝐍 omits the spectrum and
   positions of ℋ_pr (athermal phonons at 10–100 ps are far from thermal; ϵ_coll and E_sl depend on them, which is IF-E7) and the spatial
   e–h cloud (it sets 𝔵 and track recombination). Either add dℋ_pr/dω_ph(r) and the cloud geometry to 𝐍, or downgrade "coupling only through
   𝐍" to [D given a sufficient-statistic assumption]. **Additivity:** WP5 (W3) needs additive deposits δ𝐍_c in e^{ϑ·𝐍}. A class label c and a
   position r_ev are not additive, so treat them as marks: P_casc(𝐍, c, r_ev | Λ) as a marked law, not components of ϑ·𝐍.
2. **Theorem E-1** is correct, and the forbidden combinations (a)–(c) are right. Minor points: (i) E_st^{frz} is "reached … on the
   observation time" while (E6) integrates t to ∞. Define E_st^{frz} as the energy of states with Γ = 0 at T, or cut (E6) at t_obs.
   (ii) (E5) uses 𝒦^{rel}(E,t|c,E_st,T) only, but the §1.3 ledger has athermal triggers (later-event phonons, NTL phonons) and TLS absorption,
   and §2 adds carrier recombination at track defects. 𝒦^{rel} must depend on the local phonon flux and on carrier density, or (E5) does not
   cover processes listed in its own ledger.
3. **Theorem E-2 "exactly".** The 0.78 meV kinematic bound (C11, correct; it holds up to ~10² keV electrons, not just "at 10 eV") forbids
   electron-driven *creation*. Recombination-enhanced defect reactions (Kimerling) and the athermal migration of Si self-interstitials under
   ionization (Watkins; Bourgoin–Corbett) [UNVERIFIED, from memory] let electronic energy (E_g − E^tr per recombination at a defect) move or
   anneal existing defects. That changes E_st inside the recoil's own track (the "track self-trapping" of §2.3). **Correction:**
   "E_st ⊂ E_nuc for defect creation; electronically stimulated migration and annihilation is a cross-channel E_el → ΔE_st (sign either
   way), post-prompt, in 𝒦^{rel}". (E7) at t_pr stands only if no such reaction occurs before t_pr.
4. **(E9).** "v_th" is not meaningful at mK. Use the carrier's actual speed in the hot-carrier distribution. Capture on shallow Coulombic
   centres at mK is cascade capture (σ strongly speed-dependent), not the NMP form WP4-v3 §6 that §7 specifies, so §7 cannot deliver σ_j for
   shallow levels. Add a cascade-capture (Lax/Abakumov-type) computation or state it as a gap.

## 3. Measured charge, two-channel and Y_H (rubric a, b)
1. **(E12) position mixture.** The i.i.d. step is valid given r_ev. A detector's reported F_meas averages over r_ev:
   F_meas^{obs} = ⟨𝔵⟩F_eh + ⟨Var𝔵|r⟩/⟨𝔵⟩ + ⟨N_eh⟩Var_r(⟨𝔵|r⟩)/⟨𝔵⟩. The last term grows with N_eh (non-Fano scaling). It must be in A-10 and IF-E5.
2. **Calibration ratio.** Every quoted QF or yield is NR relative to ER. 1803.02903 [FT]: the phonon scale is set using "bulk electron
   recoils, which should have unity ionization yield", and ε converts charge to E_Q on ERs. In URF terms:
   y^meas = [⟨𝔵⟩_NR⟨N_eh⟩_NR/⟨𝔵⟩_ER⟨N_eh⟩_ER^{per ω}]·[(ω − E_stored − E_esc)_ER/(ω − E_stored − E_esc)_NR] (per unit ω). §3.1, §4(a),
   L38 and C7b use absolute ⟨𝔵⟩ and omit E_stored^ER. The same applies to §4(b) (2405.10405 calibrates on ²⁴¹Am and Pb X-ray peaks [FT]),
   so "measured QF = ⟨𝔵⟩·QF_created" should read ⟨𝔵⟩_NR/⟨𝔵⟩_ER·QF_created.
3. **(E8)/A-4.** ER events also trap charge. With "Δ = NR minus ER at equal ω", the term must be ⟨ΔE_trap(t_win)⟩. As written, (E8)
   subtracts the full NR E_trap while the ER calibration has already absorbed E_trap^ER. NTL mode: the ER reference signal is
   E_R(1 + eV_b/ε_eh), so the "+eV_b⟨ΔN^meas⟩/E_R" term is correct only for a ratio normalised to E_R, which is not the measured
   NR/ER phonon ratio. State the normalisation. "Y_H rises with t_win" (C9a) holds at fixed E_trap, E_esc and E_sl, but E_trap(t_win) and
   the cumulative E_esc and E_sl also depend on t_win. Restrict the claim to the E_st^{rel} term.
4. **2405.10405 bound.** Quotes CONFIRMED ("three trapezoidal shaping times, 2, 8, and 16 µs, and four Gaussian … 2, 6, 12, and 18 µs";
   "differed by less than 2 eV with one exception, the 12 µs Gaussian filter"). The 2 eV concerns the γ+NR combined energy and is
   calibrated per data set on γ/X-ray lines, so it bounds the NR-minus-ER window dependence. It does not bound the absolute ⟨𝔵⟩ window
   dependence, and it holds for 6 of 7 filters. Keep [E] and state both.

## 4. mK emission, delayed events, numbers (rubric a, e)
1. **C10b bug.** `hbarc_eVcm = Q(197327, 10**12)` = 1.97×10⁻⁷ eV·cm. The true value is 1.97327×10⁻⁵ eV·cm. Recomputed:
   F(S = 30) = (4/3)√(2·0.3m_e)(45 meV)^{3/2}/(30ħc) = **1.19×10⁴ V/cm**. Replace "1.2×10⁶" (§2.1, §0 row 10) and fix the constant. The
   check asserts only "> 10⁴", so it passed with the wrong value and would pass, barely, with the right one. Poole–Frenkel lowering for
   Coulombic traps and phonon-assisted tunnelling reduce the margin further. "Absent at detector fields" survives; "far above" should be
   "≳ 10² above".
2. **C12 internal inconsistency.** WP7-T (4.5) gives the stored excess per unit λ (∫dλ in its derivation). C12b calls π²P̄V T₁²/12 ≈ 10⁶ eV
   the "total stored excess". But C12a's Q̇ = (that)/(2t) integrated over 1 s–10 d releases ln(8.6×10⁵)/2 ≈ 6.8 times the "total". Total
   = per-λ value × Δλ (Δλ ~ ½ln(Γ_max/Γ_min) ~ 10–20). The conclusion (power, not events) is unaffected, and the quantum ≲ few T₁ still holds.
3. **(b) single-defect bound.** "ε_path ≤ E_st,1" ignores amorphous-pocket recrystallisation. The return's own §1.1 lists pockets in E_st,
   and WP5 L22(c) and 2408.07518 are cited there. A pocket of N_a atoms releases ~N_a × (0.1–0.2 eV) [E] in one transition, which can be
   ≥ 10 eV. The rate bound (≤ NR rate × releases) still makes it negligible underground. The "only for E_thr ≲ 1 eV" sentence must be
   qualified. Also, C11b compares a Si/Ge Frenkel pair with the CaWO₄ (CRESST Det-A) threshold. 2007.14289's Si CPD (σ = 3.86 eV, 4.2σ
   trigger) is the matching comparator; the conclusion is unchanged.
4. **(c) selective quotation.** Two passages in the cited full texts work against the "agreement". (i) 2202.05097 [FT], the same EDELWEISS/
   Ricochet paragraph as the quoted "Sudden increases": holder tests "with adjustable stress on the crystal … none of these tests have shown
   a significant effect on the magnitude and shape of this low-energy excess"; the leading hypothesis there is NTD epoxy cracking. (ii)
   2208.02790 [FT]: "In the lowest-energy bin in the HS calorimeter, a single exponential does not sufficiently describe the time-dependent
   rate (χ²/(dof) = 4192/68)… A sum of exponentials or a power law … may be a more appropriate fit". The return's "[E] does not separate the
   two" misstates the source, which already rejects the single exponential in its best-measured bin. Report both. (c) stays a
   [C]-level reading (G-E2).
5. **3D correlated recombination.** As in the verdict table: the erfc law is 1D, and the 3D version has the (r_c/d) prefactor. The rest
   escape into the bimolecular or sink channel.

## 5. Full-text verification of quotes (rubric b, c)
All quotes CONFIRMED verbatim unless noted. 1803.02903: flashing sentence; Eq. (1) E_φ = E_R + E_Q eV_b/ε = E_R(1 + y eV_b/ε); "should have
unity ionization yield". 2004.10709 App. A: (A6) (F·n + η·n(1−η))/(η·n), (A7) F/η + (1−η), "this approximation actually makes this estimate a
lower bound": **error CONFIRMED**. 1805.09942: Eq. (4) f_DF = 1 − (1−f)/(1−f_sur), (6.08 ± 0.18)%, 19.7 eV, the TRIM sentence; also (not cited
by the return) "systematic error does not include modeling imperfections in Geant4 and TRIM" and the polarity / charge-collection paragraph,
both relevant to L36. 2007.14289: heat-QF sentence CONFIRMED; the next sentence ("similar work has been undertaken for Ge, where the heat
quenching factor was shown to be very close to unity") is omitted and bears on L37. 2405.10405: as §3.4. 2208.02790: "observe excess
low-energy (10–100 eV scale) events of an unknown origin", "non-ionizing", the two-orders sentence, "6–10 d" (the source's sentence reads
"3–38 and 30–85 eV rates"), CRESST "∼15 days"/"∼year"; but see §4.4. 2202.05097: Det-A "30.1 eV for nuclear recoils", "Sudden increases …
above 10 K", RED30 "not associated with the creation of electron-hole pairs"; but see §4.4. 2001.06503: "safely neglected", "cut-off at an
energy equal to twice the assumed binding energy", Table I "Dislocation 36 / 23". Attribution error: "N_FP^{NRT} = 0.8E_dam/2E_d
(Kinchin–Pease)". The 0.8 is Norgett–Robinson–Torrens; Kinchin–Pease is E/2E_d. 1805.09942 cites both. All arXiv IDs resolve to the
papers named.

## 6. WP5-v3 amendment A-1…A-11 (rubric g)
- **A-1** refers to "the absorbing state 'trapped' of (W3)". WP5-v3 (W3) has no such state (its absorbing carriers are those below E_th^{ii};
  trapping appears only in (W11) and §8). Add to (W3): a capture channel (kernel from (E9) for t < t_pr), an absorbing type "trapped on
  level j" with 𝐍_term contributing E_trap. Also fix the N_eh/E_pairs statement (§1.3).
- **A-2**: c and r_ev as marks, not components of the additive 𝐍 (§2.1); otherwise (W3)/(W5) are ill-defined.
- **A-3**: fine, after the E_st^{frz} definition fix (§2.2(i)).
- **A-4**: ⟨ΔE_trap⟩, not ⟨E_trap⟩. Add the singly trapped deficit (μ_F). State the NTL normalisation (§3.3).
- **A-5**: "trapping … is a detector-stage effect" contradicts A-2's N_trap^{pr} ∈ P_casc. Say "trapping after t_pr". The QF comparison must
  use ⟨𝔵⟩_NR/⟨𝔵⟩_ER.
- **A-6**: correct (the target string exists verbatim in WP5 (W12)).
- **A-7 is wrong as written.** (W13) is the bookkeeping of a superconducting **absorber** (WP5 §5: ω is the deposit in the superconductor).
  There E_sub and E_excess are absorber phonon energy (ℋ_ph) and E_esc is E_esc of (E1), not E_sl. Only when (W13) is applied to a sensor
  film, with ω replaced by the phonon energy entering the film, do E_sig = N_qpΔ_BCS and E_sl = E_sub + E_excess + E_esc(film). Rewrite with
  both cases.
- **A-8, A-9**: A-8 fine. A-9 must say that 1805.09942's f_DF is a phonon-minus-Luke deficit containing E_trap and ΔE_esc (L36).
- **A-10 is incomplete.** WP5 (W14) is "[D, exact given (W4)]". A-1 adds E_trap^{pr} to (W4), so (W14) now needs E_trap^{pr} = 0. A-10 deletes
  "no trapping before counting" without replacing it. Replace it by "no capture before t_pr (E_trap^{pr} = 0)", and add the position-mixture
  term to F_meas (§3.1).
- **A-11**: moving trapping out of θ_esc into θ_tr (post-prompt trapping lengths) leaves no nuisance for N_trap^{pr}, E_trap^{pr}. Add
  θ_tr^{pr} (type M, support E_trap^{pr} ≥ 0).
- **Missing amendments:** (i) WP5 §6.4 "Leading URF corrections … then trapping (N_trap) and exciton or luminescence escape via (W4)" must
  point to (E12) and post-prompt trapping; (ii) WP5 (W6) must read (E4) (IF-E3 covers WP0 (7.3) but not WP5's copy); (iii) WP5 §9 R6
  "shallow-dopant trapping … enter (W4) and (W11)" must be redirected to (E1)/(E8); (iv) NOTATION row "N_trap" (§G line 264) must be
  restricted to t < t_pr (only noted in the Symbols table).
- **E_d counted once** across the amended WP5 + WP7-E: verified. E_d appears only in (W10)/P_FP. A-3 removes any ledger use, and L36/A-9
  keep E_st,1 ≠ E_d. STANDS.

## 7. Consistency with WP0-v3, CONVENTIONS, NOTATION (rubric d)
(E4) and (E1′) match WP0-v3 (7.3), with tr[𝔇ᵀS] in the right index order. ω follows CONVENTIONS §3. Clashes: c (configuration class) vs
NOTATION's c (band subscript) and 𝒦_c (cascade kernel of channel c): (E13)'s Σ_c and 𝒦^{rel}(…|c) collide with 𝒦_c. Rename the class
(e.g. 𝔠). Bare μ (chemical reference) next to the μ_χe, μ_N family: acceptable as declared "local", but write μ_F per §1.1. T₁ (freeze-in
temperature) vs Γ₁ (TLS relaxation): fine. F (field) vs F_eh, F_meas, F_DM: use ℰ or F_b for the field. CONVENTIONS §12: Theorem E-2(i)
is tagged [D] but rests on an [UNVERIFIED] scope (no electronically stimulated defect reactions); E_st,1 ≈ 7–9 eV is correctly [UNVERIFIED].

## 8. Required corrections (summary for the author)
1. μ = electrode Fermi level; singly trapped deficit added (Thm E-3, Table 3.4, A-4). 2. Add exciton/EHD/Coulomb terms to (H-E1) or
truncate them explicitly. 3. 𝐍 sufficiency for (E3); c and r_ev as marks. 4. Theorem E-2 "exactly" → creation only; stimulated E_st change in
𝒦^{rel}. 5. ΔE_trap in (E8)/A-4; ER-calibration ratios in (C7), y^meas, §4(a)(b), L38. 6. Position-mixture term in F_meas (E12, A-10).
7. Fix ħc in checks.py: F ≈ 1.2×10⁴ V/cm. 8. C12 per-λ normalisation. 9. Pockets in (b); the stress null (2202.05097) and the
single-exponential rejection (2208.02790) in (c). 10. 3D r_c/d in C3e. 11. NRT attribution; L33 source not FT; L36/L37 as above.
12. A-1, A-2, A-5, A-7, A-10, A-11 rewritten; four missing amendments added. 13. Replace the tautological checks (C2a, C2c, C7b, C9c)
with checks that can fail.
