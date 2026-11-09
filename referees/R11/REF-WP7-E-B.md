# R11 hostile referee REF-WP7-E-B on returns/R10/WP7-E.md (+ code/WP7-E/checks.py)

Isolated referee. Read: WP7-E, checks.py (run: 35/35 PASS, ≈ 2 s), WP0-v3 §6–§8, WP5-v3 §1–§8 (the amended object), CONVENTIONS,
NOTATION, CONTROLS, DONE, LIMITS. Full texts fetched with lit.py into literature/papers-r11-WP7-E-B/ (deleted after use):
2004.10709, 1803.02903, 2405.10405, 2202.05097, 2208.02790, 2007.14289, 1805.09942, 2209.04503. No simulations; one arithmetic re-check.

## Verdict table (one row per main claim; numbering = WP7-E §0)
| # | Claim | Verdict | Reason (details in §§ below) |
|---|---|---|---|
| 1 | Balance law (E1) | STANDS WITH CORRECTION | reservoir list incomplete: zero-point energy of the occupied basin, exciton binding, electrostatic (space-charge/image) energy (B1–B3) |
| 2 | Exactness, Theorem E-0 | STANDS WITH CORRECTION | C2 checks are tautological; at t_pr the split N_eh E_g + E_trap^pr is reference-dependent; "exact" only given complete reservoirs (B1, B4) |
| 3 | Two-stage factorisation (E3) | STANDS WITH CORRECTION | needs a sufficiency hypothesis: 𝒫_det depends on the t_pr state only through 𝐍 (B5) |
| 4 | E_d counted once (Theorem E-1) | STANDS | E_d absent from (E1); enters only via P_FP (W10) (strictly as its median, not a "parameter"); forbidden combinations correct |
| 5 | Yield models act on E_el only (E-2), "E_st ⊂ E_nuc exactly" | STANDS WITH CORRECTION | "exactly" is an overclaim: WP5 §4 tags the premise [E]; recombination-enhanced / ionization-driven defect reactions move E_el into ΔE_st; E_esc^nuc dropped (B6) |
| 6 | Charge counted once (E-3); (W11) overstates | STANDS WITH CORRECTION | correct for doubly trapped pairs; a singly trapped carrier whose partner reaches a contact has deficit referenced to the contact Fermi level, not E_g − ΣE^tr (B4) |
| 7 | NTL identity (E11) | STANDS | Ramo–Shockley, two electrodes, no space charge; C5 correct |
| 8 | Measured charge (E12), Hecht, CCD thinning | STANDS WITH CORRECTION | (E12) is conditional on r_ev; the depth-averaged Hecht case adds ⟨N⟩Var_z⟨𝔵⟩/⟨𝔵⟩ to F_meas (B7) |
| 9 | Two-channel recoil scale E_R^rec (C7) | STANDS WITH CORRECTION | algebra right; but the source (1803.02903) reconstructs with a fitted η^φ_NR = 95.2%, which the return omits (C2, L38) |
| 10 | mK charge release frozen | STANDS WITH CORRECTION | conclusion holds, number wrong by ×100: F ≈ 1.2×10⁴ V/cm, not 1.2×10⁶ (code ħc error) (B8) |
| 11 | Delayed events: single releases and TLS sub-threshold; 10–100 eV need collective release | STANDS WITH CORRECTION | visibility threshold inconsistent (2.7 eV vs "≲ 1 eV"); amorphous-pocket recrystallisation omitted; EDELWEISS contrary sentence omitted (B9, C5) |
| 12 | Time laws, released fractions (C3) | STANDS WITH CORRECTION | erfc(d/√4Dw) → 1 only in 1D; in 3D the eventual-recombination probability is a/r₀ < 1 (B10) |
| 13 | Literature implicit assumptions | STANDS WITH CORRECTION | "QF data: Y_H = 1" FALSE for 1803.02903 (fits η^φ_NR = 0.952); 1805.09942 and 1803.02903 attribute the same ~5–6% NR phonon deficit to opposite causes (C2, C6) |
| 14 | WP5-v3 amendment A-1…A-11 | STANDS WITH CORRECTION | A-1 cites a non-existent (W3) state; A-4 inconsistent Δ and NTL normalisation; A-8 drops "secondary"; A-10 breaks the sentence and removes a needed hypothesis; four WP5 sites not amended (§G) |
| 15 | Nuisances §6 | STANDS WITH CORRECTION | "M with support restriction" is not a WP0 (8.1) type; θ_tr prior from a 77 K HPGe window bound does not constrain trapping (D2, D3) |
| L33–L38 | Proposed LIMITS rows | STANDS WITH CORRECTION (L35 STANDS) | no row gives validity or leading correction; Hecht uncited; L36–L38 need the η^φ_NR / ΔE_sl caveat (§E) |

---
## A. Checks (rung 3)
- All 35 checks pass, but C2a, C2c, C7a, C9b, C9c, C3a, C4c, C5b are identities that hold by construction: each process's reservoir changes
  are written so that they sum to zero, and C2c compares an expression with itself. They check the bookkeeping, not the physics. The physical
  content of Theorem E-0 is that the reservoir list is **complete**, and no check tests that (§B1–B3).
- **C10b is numerically wrong.** `hbarc_eVcm = Q(197327, 10**12)` = 1.97×10⁻⁷ eV·cm; the correct ħc = 1.97327×10⁻⁵ eV·cm. Recomputed:
  (4/3)√(2·0.3m_e)(45 meV)^{3/2}/(30ħc) = **1.19×10⁴ V/cm** (the script prints 1.19×10⁶). §0 row 10 ("F ≳ 10⁶ V/cm") and §2.1 ("F ≈ 1.2×10⁶
  V/cm") must read 1.2×10⁴ V/cm. The conclusion survives (still ≫ 1–100 V/cm). The check passed only because its threshold is > 10⁴.
- C3d, C3e, C4a, C5a, C6a–c, C12a,b: re-derived and correct (C12: 0.57 eV/s, 9.8×10⁵ eV with WP7-T's P̄ = 1.6×10¹⁹ eV⁻¹cm⁻³, i.e. 10⁴⁴ J⁻¹m⁻³).

## B. Derivation steps (rubric a)
**B1 Zero-point energy missing from (E1).** E_st ≡ E^ad_0(R̄) − E^ad_0(R_I(0)) is a classical-minimum difference, and ℋ_ph is phonon energy
"above the bath". The change of vibrational zero-point energy between the defect basin and the perfect crystal (ΔZPE, typically 10⁻¹ eV per
point defect, i.e. a few % of E_st,1) is in neither term. At mK it is the dominant correction to stored energy. Fix: define E_st as the
ground-vibrational-state energy of the basin minus that of 𝔅₀ (or add ΔZPE to E_st), and say so in A-3.
**B2 Excitons.** At mK and zero or low field, free pairs bind into free or bound excitons (E_x^b ≈ 15 meV Si; WP5 (W4) already has
E_g → E_g − E_x^b). E_pairs in §1.1 has no exciton term, and the process table has no exciton formation or capture. Add them.
**B3 Electrostatic energy.** With trapped charge (θ_SC, §2.1) the field energy, including image terms, is a reservoir. (E11) excludes space
charge, but (E1) is stated for "all t". Add E_es(t), or restrict (E1) to negligible space charge.
**B4 Reference level; the t_pr split.** Lemma 1 is right: only E_pairs + E_trap is μ-independent, and only for a neutral crystal. Then (i) at t_pr,
"ω = N_eh E_g + ℋ_pr + E_st + E_esc + E_trap^{pr}" is μ-dependent if one carrier of a pair is trapped and the other is free: E_pairs ≠ N_eh E_g
for an unpaired free population. Define E_trap^{pr} as the μ-independent quantity E_pairs + E_trap − N_eh^{free pairs}E_g. (ii) Once carriers
leave through the contacts, the crystal is not neutral and E_trap depends on μ. The physical reference is then the contacts' Fermi level E_F.
1803.02903 itself says carriers "relax to the Fermi level at the electrodes". A singly trapped electron whose hole was collected leaves the deficit
E_c − E^tr_e − E_F, not E_g − E^tr_e − E^tr_h. (E8) and A-4 use ⟨E_trap(t_win)⟩ without fixing μ. Set μ = E_F(contacts).
**B5 (E3) is not proved by "Markov at t_pr" alone.** The Markov state at t_pr is the full microstate: every carrier's position and momentum,
and the defect positions relative to the carriers. 𝐍 is a coarse summary of it. (E3) needs (H-E6): 𝒫_det depends on the t_pr state only
through 𝐍. This is approximate: for example, the trapping of carrier i on track defects depends on its distance from them, not only on r_ev
and a track density. Tag (E3) [D given H-E6].
**B6 Theorem E-2.** (i) uses only knock-on kinematics (4m_eE/M ≪ E_d). It ignores electronic-energy-driven defect reactions, which are known
in Si: recombination-enhanced defect reactions, and the ionization-driven athermal interstitial migration of the Bourgoin–Corbett type. These
change E_st (mostly by annealing close pairs) using E_el, in the same track and within or after t_pr. WP5 §4 itself tags the absence of
excitation-driven bond breaking in Si as [E], so "exactly in Si/Ge" upgrades an [E] premise to [D]. Restate: E_st ⊂ E_nuc to the extent that
carrier-driven defect reactions are negligible. Add that process to §1.3, and let 𝒦^{rel} depend on the local carrier history, not only on
(c, E_st, T) in (E5). Also, (E7)'s E_nuc = ℋ_nuc + E_st drops a nuclear-branch E_esc. State that it is 0 by t_pr, or keep the term.
**B7 (E12) with position averaging.** (E12) is conditional on (r_ev, track). The Hecht ⟨𝔵⟩ (E10) depends on depth z. For a population of
events (calibration lines, uniform DM), F_meas gains +⟨N_eh⟩Var_z(⟨𝔵⟩|z)/⟨𝔵⟩. This grows with energy and must be in L33/L35 and in A-10.
**B8 Field emission.** Besides the ×100 error (§A), Poole–Frenkel lowering for Coulombic centres is ≈ 2 meV at 100 V/cm in Si (recomputed).
This is negligible against 45 meV, so the claim stands, but the triangular-barrier model is the wrong model for charged centres; say so.
**B9 Delayed events §3.3.** (b) gives ϵ_coll E_st,1 ≈ 2.7 eV, so single-FP releases become visible for E_thr^det ≲ 2–3 eV, not "≲ 1 eV".
Present sub-eV-resolution devices (2007.14289: σ = 3.86 eV, threshold 16.3 eV) are within a factor of 6. Also, an event-seeded amorphous
pocket (WP5 §3.2 R_final; §6.3(c)) that recrystallises in one cooperative step can release ≫ E_st,1. "Particle-seeded single releases ≤ E_st,1"
is therefore not derived for keV recoils in Si or Ge. Either classify pocket recrystallisation as "collective but event-seeded" or drop the bound.
**B10 Correlated recombination.** The first-passage density d/√(4πDt³)e^{−d²/4Dt} with eventual probability 1 is the 1D law (crowdion). In 3D
the eventual recombination probability is a/r₀ < 1. P_rel(t_win) → (a/r₀)erfc((r₀ − a)/√(4Dt_win)), and the remainder becomes
uncorrelated (bimolecular). Fix §1.6 and C3e's label.
**B11 Minor.** E_hot(0⁺) = ω contradicts X+ seeds (ω_ph → ℋ at the vertex) and GS regime (i) (pure phonons). Write E_hot(0⁺) = ω − ω_ph(Λ).
WP5 (B3)'s NTL drift "inside P_casc" contradicts A-1 (§G).

## C. Claims about published papers and literature quotes (rubric c), verified in full text
| Claim | Rating | Evidence |
|---|---|---|
| C1. 2004.10709 App. A: F_meas = F/η + (1 − η) is wrong (exact ηF + 1 − η); its "lower bound" is in fact an upper bound | **CONFIRMED** | PDF (A1)–(A7): numerator "F·n + η·n(1 − η)" lacks η²; text "this approximation actually makes this estimate a lower bound". (F/η + 1 − η) − (ηF + 1 − η) = F(1/η − η) ≥ 0 |
| C2. 1803.02903 implies "E_stored(t_win) = 0 for NR relative to ER (Y_H = 1)" | **REFUTED** | The paper's main result is a fitted NR phonon scale "η^φ_NR = 95.2^{+0.9}_{−0.7}%" ("phonon collection efficiency of nuclear recoils relative to that of electron recoils"); E_R = (E_φ − E_QeV_b/ε)/η^φ_NR. In URF terms this is a measured 4.8% NR-minus-ER phonon deficit (E_stored + ΔE_sl + Δϵ_coll) at 10–100 keV in Si, i.e. Y_H ≈ 0.95 |
| C3. 1803.02903 Eq. (1) and the "flashing" quote | CONFIRMED | verbatim; 4 V/cm field |
| C4. 2405.10405 quotes; "window-dependent part ≲ 3%" | quotes CONFIRMED; use UNRESOLVED/misapplied | the HPGe was "cooled to 77 K", not mK; a window-independent result does not bound permanent trapping, so it cannot set the θ_tr prior (§D3) |
| C5. 2208.02790 / 2202.05097 quotes | CONFIRMED verbatim, but **selective** | 2202.05097 continues: holding strategies "with adjustable stress … none of these tests have shown a significant effect". 2208.02790: in the best-measured bin "a single exponential does not sufficiently describe" the rate (χ²/dof = 4192/68), and "a sum of exponentials or a power law … may be a more appropriate fit". WP7-E's "fits exponentials over 5 d, which does not separate the two" misreports this. 30.1 eV Det-A threshold CONFIRMED |
| C6. 1805.09942: Eq. (4), 6.08 ± 0.18%, the TRIM sentence | CONFIRMED | verbatim; Ge iZIP at ~50 mK, phonon energy scale. Note that it attributes to defects a deficit that 1803.02903 (Si) attributes to collection: the URF cannot separate the two without ΔE_sl (IF-E7) |
| C7. 2007.14289 heat-quenching quote | CONFIRMED | verbatim; continues "measurements … have not been made for Si", which is overtaken by C2 |
| C8. 2209.04503 U booked electronic by complement | CONFIRMED for **secondary** U only (as WP5 §6.1(5)) | ε_R = η̄ + ν̄, f_n = (ε + u − ν̄)/(ε + u): the primary's u is in ν̄. A-8 drops "secondary", which is a misstatement |

## D. Consistency with WP0-v3, CONVENTIONS, NOTATION (rubric d)
- D1. (E4) and (E1′) are consistent with WP0 (7.3) (tr[𝔇ᵀS], q inside the Λ sum). dℛ_bg is a new additive term. Fine as IF-E3.
- D2. **Types.** θ_frz and θ_coll are "M with support restriction". WP0 (8.1) M is log-normal, positive for all θ and unbounded. A support
  restriction is type L (only as the linearisation of T) or type T. Use T, or a logit-normal on E_st^{rel}/E_st and on ϵ_coll.
- D3. θ_tr prior "HPGe window bound ≲ 3% (2405.10405)" is a delayed-release bound at 77 K, not a trapping length at mK. Remove it.
- D4. Symbols. μ (local) collides with μ_χe, μ_N and μ*. F (field) collides with F_DM, F_eh and F_meas. D (diffusion) is close to 𝔇. c (class)
  collides with the channel c of WP5 (W3) and sound speeds c. Rename them, e.g. μ_ref, ℰ (field), D_diff, c_cls, and add NOTATION rows.

## E. Proposed LIMITS rows (rubric b)
LIMITS rows require the source formula, the chain, the **validity** and the **leading correction**. No row L33–L38 has the last two.
- **L33 Hecht.** The chain is valid (exponential trapping, uniform field, no detrapping, no diffusion, no space charge). No source is cited.
  Cite K. Hecht, Z. Phys. 77, 235 (1932), with the equation checked. Leading corrections: detrapping/emission, diffusion, the depth-averaging
  term of B7. STANDS WITH CORRECTION.
- **L34 NTL gain.** Valid, and the quote is correct. Validity: two electrodes, no space charge, terminal-velocity drift. Leading correction:
  mode-dependent phonon collection, which the source itself raises ("need not be identical"). STANDS WITH CORRECTION.
- **L35 thinning.** C1 CONFIRMED. The row is correct. Add the B7 depth term for induced-charge readout. STANDS.
- **L36 KP/NRT.** "f_DF fixes p_surv E_st,1/E_d" holds only with ΔE_sl = ΔE_trap = 0 and within NRT. The measured quantity is a Y_H deficit
  (C6 vs C2). Validity: Ge, 80–110 keV Pb recoils, t_win of an iZIP. STANDS WITH CORRECTION.
- **L37 unit heat quenching.** Quote correct. Add that the only Si measurement of the relevant ratio (C2) gives 0.952, not 1.
  STANDS WITH CORRECTION.
- **L38 two-channel scale.** Source Eq. (1) is right, but the source's reconstruction includes 1/η^φ_NR. The URF chain should give
  E_φ − eV_bN^meas = ω − E_stored − E_esc − ΔE_sl-type terms, identify η^φ_NR with 1 − (that deficit)/E_R, and list that as the leading
  correction. STANDS WITH CORRECTION.

## F. Gap-closure / computation specification (rubric e)
- Track traps: "capture cross sections from the nonradiative multiphonon form (Huang–Rhys)" is the wrong model for the shallow hydrogenic and
  Coulombic centres that dominate trapping in detector-grade Si/Ge at mK. Capture there is cascade (Lax-type) capture via sequential phonon
  emission. The specification must branch: deep (NMP) versus shallow (cascade).
- Drift–trap MC: G4CMP already implements anisotropic valley transport, NTL emission, trapping and impact ionisation with Ramo readout. Credit
  it and specify what is added (track traps, history-dependent n_j). Without athermal emission rates (G-E6) and ΔE_sl (G-E4), the E8 tables are
  not computable. The specification is sufficient only together with those two declared gaps. Add μ = E_F (B4) and ΔZPE (B1) to the table
  definitions.
- G-E1…G-E6 are honest. Add G-E7 (carrier-driven defect reactions, B6) and G-E8 (pocket recrystallisation size law, B9).

## Novelty (rubric f)
WP7-E makes no explicit novelty claim. The physics of §3.3(c) (stress-driven collective release, power-law time law, QP poisoning by
stress phonons) is in 2208.02790 itself, and the "time law as discriminant" point is anticipated there. Credit it. The balance-law framing
(E1) is a bookkeeping synthesis and should not be presented as a new result.

## G. WP5-v3 amendment A-1…A-11 (rubric g)
Checked against the WP5-v3 text:
- **A-1** refers to "the absorbing state 'trapped' of (W3)". WP5 (W3) has types {e, h, phonon, ion, core hole} and no trapped state or
  capture kernel. A-1 must also add the type, its kernel 𝒦_capture, and its δ𝐍 (N_trap^{pr}, E_trap^{pr}). Fix the t_pr formula per B4.
- **A-2** is correct (𝐍 extension). It also needs (H-E6) (B5).
- **A-3** is correct for E_d. It must define E_st including ΔZPE (B1).
- **A-4 (new W11).** (i) The Δ convention is inconsistent: E_esc and E_sl appear as NR − ER differences, but E_trap does not. ER pairs are trapped
  too, and ER has more pairs at equal ω, so the term must be ⟨ΔE_trap(t_win)⟩, which can be negative. (ii) If Y_H is the ratio of NR to ER heat
  signals (the 2007.14289 definition), it equals [ω − D_NR]/[ω − D_ER]. The linear form 1 − ΔD/E_R is first order in D_ER/ω; state that.
  (iii) NTL mode: the ER calibration contains ER's NTL gain, so the normalisation is E_R(1 + eV_b/ε_eh^γ), not E_R. As written, the
  "+eV_b⟨ΔN^meas⟩/E_R" is mis-normalised. (iv) Fix μ = E_F (B4).
- **A-5, A-6, A-7, A-9, A-11** are correct as text. A-6 should add B9's pocket caveat.
- **A-8**: insert "secondary" (C8).
- **A-10**: replacing "no trapping before counting" in §6.4 Validity produces a broken sentence. It also deletes a real hypothesis: (W14) is
  derived from (W4), which holds only for E_trap^{pr} = 0. Write instead: "…with no capture before t_pr (E_trap^{pr} = 0; otherwise (W14) uses
  ℋ + E_trap^{pr}), …; the measured Fano factor is F_meas = ⟨𝔵⟩F_eh + Var𝔵/⟨𝔵⟩ (+ the depth term)".
- **Incomplete.** These WP5 sites are not amended: §1.2 (B3) ("an NTL drift field adds a deterministic drift term", which contradicts A-1's
  "drift is post-prompt"); §6.4 "Leading URF corrections … then trapping (N_trap) … via (W4)"; §9 R6 ("shallow-dopant trapping enter (W4)
  and (W11)"); the §14 symbol rows (N_trap now restricted to t < t_pr).
- **Balance-law exactness proof:** valid as a flux argument once the reservoirs are complete. As written it is incomplete (B1–B3, B6) and the
  checks do not test completeness (§A). **E_d is counted once:** verified. E_d appears in no term of (E1), (E5)–(E8), (W11-new) or A-1…A-11
  except as the P_FP parameter and the f_DF ratio.

## Required corrections (summary)
1. C10b: ħc = 1.97327×10⁻⁵ eV·cm, so F ≈ 1.2×10⁴ V/cm (§0 row 10, §2.1).
2. §4(a), §0 row 13, L37, L38: 1803.02903 measures η^φ_NR = 0.952 (a ~5% NR phonon deficit); it does not assume Y_H = 1.
3. (E1)/A-3: add ΔZPE to E_st; add excitons; add space-charge energy, or restrict (E1).
4. μ = E_F(contacts); a μ-independent E_trap^{pr}; the singly-trapped deficit.
5. (E8)/A-4: ΔE_trap; ratio form; NTL normalisation.
6. (E3): add hypothesis (H-E6). Theorem E-2: drop "exactly"; add carrier-driven defect reactions.
7. (E12): depth-averaging term. §1.6: 3D correlated recombination factor a/r₀.
8. §3.3: threshold 2–3 eV; pocket recrystallisation; quote the EDELWEISS null-stress sentence and the 2208.02790 χ² result.
9. §6: θ_frz and θ_coll as type T; drop the 77 K HPGe bound from θ_tr.
10. LIMITS rows: add validity and leading correction; cite Hecht.
11. Amendment fixes A-1, A-4, A-8, A-10, plus the four unamended WP5 sites.
