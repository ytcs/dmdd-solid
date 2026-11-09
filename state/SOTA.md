# SOTA: current status of campaign claims (overrides returns)

**Read state/CORRECTIONS.md before quoting any return.** Authoritative conventions: CONVENTIONS.md, NOTATION.md. Current refereeable packages: returns/R8/*-v3.md.

Status labels: CLAIMED (one return) · CROSS-CHECKED (two independent routes agree) · REFEREED (R×2) · OPEN · AMENDED.

## Theory (T1–T4)
| # | Claim | Source | Status |
|---|---|---|---|
| 1 | One-phonon cut of the O(g²) density response = Σ|A₁+A₂|² δ(…), two time orderings; band sum over intermediate m unrestricted (Pauli-blocked paths return as Z-graph partners) | D2 eq 2.1–2.2 | CROSS-CHECKED (D1 eq 1 ≡ D2 eq 2.1 on shell; D1 eq 4 ≡ D2 eq 2.2: 8π²α/(Ωq²)·N⁻²Σ|M|², spin 2, Bose n+1/n) |
| 2 | No sideband–zero-phonon-line interference at O(g²) (vertex odd in phonon operators) | D2 | CLAIMED |
| 3 | f-sum exact to all orders (local potentials). The sideband alone overshoots; the compensation comes from the non-phonon cuts of the Fan and vertex diagrams, NOT from the Allen–Heine DW tadpole | D2 | CLAIMED. The paper must fix the meaning of "Debye–Waller" |
| 4 | Screening: DFPT-screened g inside, one external 1/ε(q,ω); ELF = ε₂^{PA}/(ε₁⁰)² + O(g⁴) where ε₂⁰ = 0 | D2 | CLAIMED |
| 5 | Dark photon: no new eh+1ph amplitude at O(g); the ionic ε part is zero for Si | D2 | CLAIMED |
| 6 | Sideband separately computable iff every first-order transition at the same (q,ω) is off shell; D1 gives the pointwise window ω ≤ E_min^ren(q,T) − δ₀ | D1 §5, D2 §2b | CROSS-CHECKED |
| 7 | Rate normalisation: Γ = ∫d³q/(2π)³ |Ṽ|² S, |Ṽ|² = πσ̄_e F²/μ², S = (2q²/e²) L (FDT); the zero-phonon limit gives the Bloch crystal form-factor rate | D1 §2–3, D2 §0 | CROSS-CHECKED (the numerical prefactor against Essig et al. awaits L1) |
| 8 | Adiabatic (Herzberg–Teller) form = derivative of the frozen-phonon transition density, error ~ω_Q/δ; standard DFPT (P_c-projected ∂ψ_v) gives only path B and misses the occupied-band part of ∂ψ_v and all of ∂ψ_c | D1 §4 | CLAIMED |
| 9 | Optical limit C1: reduces to the velocity-form Noffsinger/HBB formula with q̂ in place of ê, full band sum | D1 §6, D2 §6 | CROSS-CHECKED in structure; prefactor awaits L1 |
| 10 | Computable recipe: EPW g + Wannier tensor F_ij(R,q) = ⟨w_iR|e^{iq·r}|w_j0⟩ in continuous q (Umklapp automatic) + Sternheimer remainder for high bands | D1 §7 | CLAIMED |
| 11 | [SUPERSEDED by X1 C7a–e, R3] C7 acoustic Q→0 limit ≠ 0 at finite q: D1 gives i ℓ_Q (û·q) ρ_cv (the Debye–Waller partner of the zero-phonon transition), D2 gives i u^{zp}·(q − m_eΔv) ρ_cv (lattice recoil) | D1, D2 | AGREE in the leading term; the m_eΔv term is a DISCREPANCY for the referees |

## Amendments owed
- NOTATION ρ_{mn}: drop the "·N" (it makes the vertex O(N)); use the O(1) single-particle matrix element. APPLIED in NOTATION.md (2026-10-31).
- NOTATION S(q,ω): adopt S = (2π/V) Σ_f |⟨f|n_q|i⟩|² δ(E_f−E_i−ω), n_q = Σ_e e^{+iq·r_e} (D2 proposal). CONFIRMED (WP0 (3.1), NOTATION v3).
- [SUPERSEDED: REF verdict FALLS, then X1 C7a–e] CONTROLS C7: at finite q the acoustic Q → 0 amplitude → i u^{zp}·(q − m_e Δv)ρ_cv (lattice recoil), not 0. It vanishes at q → 0 and has measure zero in the Q integral. AMENDED.
- CONTROLS C8 (decoy) may FAIL for DM kinematics: DM cannot reach q ≈ 0, so in GaAs there may be a window between E_dir + ω_ph and the L-valley energy where PAER leads. ~~OPEN, needs a band-structure check (deferred numerics; specification in D2 §9).~~ ✎R17 (CW1 OC-12): PAER-leading GaAs only at m_χ ≈ 0.43–0.51 MeV [E, parabolic; CW1 §24], full q integral; band-structure check formulated (CLOSED-AS-EXACT-GAP, LE-47; run = DEFERRED-COMPUTE DC-8). The CONTROLS.md C8 copy is owed (CORRECTIONS §20.1).
- [CLOSED in full text by WP3] C1 prefactor 8π²e²/(Ωω²) (velocity form) is from memory: L1 must confirm it.

## Literature (L1, 2026-10-31)
- Priority: NONE. No paper computes a phonon-assisted interband S(q,ω) / ELF / ε₂(q,ω) at q ≠ 0 for any probe (DM, EELS, IXS, ν). Closest:
  - Kahn & Lin 2108.03239 §VI name the "2→3 electron + phonon" response near the gap, with no formula;
  - 1608.01994 uses measured phonon-assisted Si absorption (q≈0, absorption only);
  - Liang et al. 2205.03395 reach the same final state through the DM–ion amplitude;
  - SPLENDOR 2507.17782 assumes phonon-assisted transitions are suppressed at mK. They are not: emission (n+1) survives at T=0.
- Rate normalisations KKL (Eqs 4, 6, 10–13) and Hochberg (Eqs 1, 2, S.7, S.9) agree with each other. Comparison with D1/D2's Γ = ∫|Ṽ|²S, S = (2q²/e²)L: KKL's S = k²/(2πα)·ELF ≡ 2q²/e²·L with e² = 4πα. CONSISTENT.
- The finite-q generalisation of EPW Eqs 61–62 (velocity vertex → density vertex) is not in the literature.
- Data-driven ELFs (Hochberg et al., DarkELF) carry zero weight between E_g and E_dir at small q. Si halo reach is shown only for m_χ ≥ 0.5 MeV (2e⁻ threshold). The EXCEED-DM energy-only bound is m_min = 0.28 MeV (their eq. 33).
- Si optical calibration (for the deferred numerics): Stanford et al. 2010.15844 Rajkanan refit; TA 18.27 meV, TO 57.73 meV, E_g(0) = 1.170 eV, n = 3.511 at 1.127 eV.

## R2 referee verdicts (REF-A, REF-B; isolated, they concur on every major item)
| Item | REF-A | REF-B | Status now |
|---|---|---|---|
| D1 ≡ D2 term by term (N, Ω, 2π, spin, α/e²) | STANDS w/ corr. | STANDS | **REFEREED**. Correction: D1's isotropic shortcut must read 𝒢 = η(v_min)/(2q), not η/q (factor 2; also affects D1's Essig comparison); D2's script docstring omits spin 2 |
| Pauli/exchange theorem (unrestricted band sum on shell) | STANDS w/ corr. | STANDS | **REFEREED** (D1's hole-denominator bound misstated; D2's third-order ZPL extension unproven) |
| f-sum / "Debye–Waller" | D2 right on the AH tadpole | same | **REFEREED**: the sideband's first-moment excess is compensated by the Fan + vertex non-phonon cuts *as a sum*. The diagram-by-diagram claim is unproven; there is no zeroth-moment rule. Terminology: "DW" in this campaign means the Franck–Condon / e^{−2W} reduction of zero-phonon weight, never the Allen–Heine tadpole |
| C7 acoustic Q→0 | FALLS (both) | FALLS (both) | **OPEN.** The intraband terms are a finite 0/0, g_nn/(Q̂·v_n ± c_s), so they are direction-dependent deformation-potential terms ~10² × the iq·u term. The amended C7 is WITHDRAWN and needs re-derivation |
| Screening | FALLS as proof | STANDS w/ corr. | **OPEN.** Both derivations omit the Coulomb lines at the pair momentum (q+Q, ω∓ω_Q). REF-A: the rigid-shift limit suggests ε(q, ω∓ω_Q). Needs derivation (a shared error of the two routes) |
| Adiabatic / DFPT | STANDS w/ corr. | STANDS | **REFEREED w/ corr.** True of the Sternheimer ∂ψ output only. The DFPT potential gives all g_mn, so the SOS has all four paths and P_v∂ψ_v is a cheap finite sum. Error scale δ = min(E_min(q) − ω, E_g − ω_Q) |
| Resonance window / no ZPL interference | STANDS w/ corr. | STANDS w/ corr. | **REFEREED**: window ω ≤ E_min(q) (D1 criterion; it includes the hole-path resonance); no i0 needed inside; the PV in D1 §5.2 → Hadamard finite part |
| GaAs decoy C8 fails (D2) | FALLS as stated | FALLS as stated | **AMENDED**: Umklapp vertical transitions (q ≈ G) reopen the ZPL at E_dir for m_χ ≳ 0.9 MeV (GaAs); a PAER-leading window can exist only at m_χ ≈ 0.4–0.9 MeV (✎R17, CW1 §24: ≈ 0.43–0.51 MeV [E, parabolic, full q integral]; band-structure check DC-8). The Si window must be re-checked with the full q integral including Umklapp (deferred numerics; coordinator estimate: the G₁₁₁ vertical transition in Si needs m_χ ≳ 1.1 MeV, so it does not close 0.34–0.47 MeV) |
| C1 optical limit | STANDS w/ corr. | STANDS w/ corr. | **REFEREED**. Use D2's exact commutator proof; D1's derivation divides by zero on intraband terms (right result). C1 is exact with nonlocal PP using the generalised current, including the phonon-vertex commutator term |
| Wannier recipe | STANDS w/ corr. | STANDS w/ corr. | **REFEREED w/ corr.** At keV q the intermediate-state weight is on bands tens of eV up (Bethe ridge), outside any Wannier manifold. A plane-wave / Sternheimer remainder is mandatory, and the cost must be redone. g and F must share one gauge U(k). Missing: PAW augmentation in ρ, quadrupole corrections to g, and the nonlocal f-sum for C4 |

## R3 X1 (soft-acoustic limit), 2026-10-31
- C7 replaced by C7a–e (X1 §5). The limit contains the frozen-strain deformation tensors D^n, which are material constants. D/c_s ~ 100 keV against q ~ 1–4 keV, so they dominate; the R1 forms are special cases (D1: D = 0, c ≪ v; D2: Ξ = 0). CLAIMED, with two independent checks (exact 1D model; on-shell Ward identity).
- Inside the PAER window there is no IR feature: on shell |Q| ≥ Q_min ≈ (E_min(q) − ω)/v_max (~0.015 Å⁻¹ in Si, est.) [superseded R8: ≈ 0.045 Å⁻¹ at δ₀ = 0.3 eV (0.015 at 0.1 eV)]. Outside the window there is Low-type soft-phonon bremsstrahlung, finite in 3D (the acoustic g ∝ Q via the ASR), and a Bloch–Nordsieck coherent-state sum rule exists. Piezo coupling (GaAs) gives a log divergence, but only where the ZPL is open. LO Fröhlich: the 1/Q cancels (the e–h pair is neutral).
- Implementation: no subtraction inside the window; write the denominators as zero-phonon detunings; zero weight at acoustic Γ; σ ≪ δ₀.
- Flag: the recoil term carries ρ_cv(k, q+Q), supporting REF-A's claim that its screening belongs to the pair channel (X2 to decide).

## R3 X2 (screening with pair-momentum lines), 2026-10-31
- Coulomb-line classes: (q+G, ω) external; (Q+G, ν) DFPT dressing of g; (P+G, ω∓ω_Q) pair channel, P = q+Q; ionic. R1 kept only the scalar external factor and the DFPT g, so the pair channel and the external local fields are NEW. CLAIMED.
- Screened amplitude: M̃ = M⁽²⁾[ρ̃] + Σ_GG' ρ_f(P+G) W_GG'(P,ω_f) T_G', with ρ̃ = Σ_G ε⁻¹_G0(q,ω) ρ(q+G). In the window L^PA = D1 eq. (4) with M → M̃ (RPA/ALDA, O(g²), static DFPT g; screening error O(ω_Q²/E_g²)). CLAIMED.
- No double counting: a topological proof (the phonon line closes exactly one cycle). CLAIMED.
- REF-A's ε(q, ω∓ω_Q) is exact for the rigid-translation part and wrong as a general prescription. There is no 1/|ε|⁴.
- In Si, R1's simple form is off by: frequency shift 1.5%, external LFE 5–20%, pair channel −(10–50)% (sign CONJECTURED). Interim systematic on L: factor [0.5, 1.2] [superseded R8: [0.4, 1.8] (WP3-v3, R7)] until the pair channel is computed (specification X2-N1..N4).
- Recommended code route: ZG/frozen-phonon supercell + RPA local fields in the supercell basis (includes the pair channel automatically).
- Dark photon: no new amplitude; ions ≲10⁻⁴ in Si.
- M1 theory is now COMPLETE pending R×2 on X1 + X2 (folded into the WP3 referee round).

## R4 WP0 (architecture), 2026-10-31: CLAIMED, pending R×2
- Operator basis: 16 target operators per species (density, spin, current, spin-current) + kinetic-energy density for scalar absorption. Master formula Γ = ∫tr(𝔇S) (eq 3.3); absorption Γ = −(g²/ω) Im R (eqs 3.5–3.6).
- Exact relations: FDT, KK, detailed balance, matrix positivity, a diagonal f-sum matrix (mixed e–N first moment = 0). NEW (as far as found): a third-moment mixed e–N sum rule (eq 4.7) and translation Ward identities.
- Screening: R_ab = R̃_ab + R̃_ac ε⁻¹ v R̃_cb (eq 5.3) with the total ε. The ELF form is exact for dark-photon coupling; for electron-only coupling it needs clamped nuclei or ω ≫ phonon band (up to m_e/M). The longitudinal current is screened like the density (corrects the L3 chain).
- INDEPENDENT AGREEMENT with X2: WP0 eqs 5.6–5.7 predict the pair-momentum screening factor and REF-A's limit as its Q→0 case.
- Theorem D (three final-state sectors: lattice / electronic / mixed; no double counting) DERIVED under its hypotheses. [added R8: magnetic insulators excluded; remainder O(κ_BO^{2(n+1)}); [C] for the crystal limit (WP0-v3 G9, G10)] The electronic/mixed split away from the off-shell window is CONJECTURED. Migdal is purely non-adiabatic; atomic L7a recovered.
- L0: η/(2q) confirmed. L17: holds at all orders and any T, with corrections (electron-channel ε_e(q,0), all-electron ω_p, phonon-band subtraction → ε_∞). One unproven hypothesis: ε(q,0) ≥ 1.
- C7: WP0 eq 4.9 (CONJECTURED) must be reconciled with X1's C7a–e in WP3.
- Open items O1–O6: WP0 end.

## Coordinator note on WP0 O4 (Theorem D (iv), the X0/X+ split without H5), 2026-10-31
- Diagnosis: without H5 the split is not well posed as a statement about S, so it cannot be proved.
  - X0 and X+ are degenerate continua inside the excited block, separated by ω_ph ≪ bandwidth with no
    spectral gap, so the space-adiabatic (PST) construction behind (i) does not apply.
  - On-shell intermediates make the zero-phonon e–h pair a decaying state (Im Σ_Fan ≠ 0), and "net phonons
    created in the event" versus "emitted later in the cascade" is a time-coarse-graining convention.
  - It is the condensed-matter analogue of exclusive versus inclusive soft emission in QED.
- Reformulation (proposed target for WP3/WP5):
  - (iv′) DEFINITION: a resonant-part assignment (Dyson-resummed Lorentzian → δ + Hadamard finite part)
    that hands the on-shell sideband to the WP5 cascade.
  - (iv″) THEOREM to prove: X0+X+ and the cascade-convolved quanta distribution P(N_eh|q,ω) are independent of
    the assignment to O(g²); the split itself is convention-dependent at relative order Γ/δ.
  - Tools: Dyson resummation + Ward identity at physics rigour. A mathematically rigorous version (resonance
    theory à la Jakšić–Pillet / Bach–Fröhlich–Sigal, van Hove–Davies weak coupling) exists only for
    embedded eigenvalues in finite-dimensional or atom–field models, not for continuum–continuum coupling
    in an infinite crystal with Coulomb interactions.

## R5 WP6 (rate assembly + UQ), 2026-10-31: CLAIMED, pending R×2
- L24 DERIVED: WP0 (3.4) → 1509.01598 eq 17 and 2311.04957 eqs 9–13, 19–20. The prefactor matches those and 2101.08275 eq 16.
- The halo enters only via the Radon transform of f and its first two transverse moments. For angle-averaged S the velocity-dependent operators need ξ = 2∫u′η du′, so no new halo function. The cubic anisotropy starts at ℓ = 4 (7 numbers per (q,ω)).
- Kinematic edge: a power law Δ₀^{7/2+k+p}, with the halo-tail index k degenerate with the response onset p. The edge depends on E_th/v_max², so halo and gap must be profiled jointly. m_min(Si) = 0.319 MeV (v_max = 794 km/s) [superseded R8: 0.333 floor (E_g = 1.170 eV); 0.319 is the scissor comparison], 0.285 MeV (840 km/s).
- G8 closed (halo-independent ER analysis with theory nuisances; conservative bound via WP0 positivity). Exact remaining gap: no conservative halo-independent bound for directional responses.
- G4 closed: positive-preserving nuisance types; the q_max error is removed analytically by an f-sum-saturating impulse tail; three published curves (nominal, profiled, band); a combination/recast recipe; a versioned HDF5 response-library spec with sum-rule release checks.
- Profiling costs O(δ²) (×1.27 at δ = 0.5) and the envelope O(δ) (×2.0). The choice must be declared.
- WP0 defects W1–W5. W1 ((8.2) f-sum constraint off by a factor 2: π not 2π) and W2 (an additive Gaussian can make S negative) are OWED corrections to WP0 §8.
- [RESOLVED, CONVENTIONS §8] Convention flags: NOTATION v_E = 250 is the Sun's speed (Earth's annual mean is 252.1 km/s); NOTATION ρ_χ = 0.4 versus the recommended 0.3 (2105.00599). The coordinator adopts 2105.00599 conventions for the paper (ρ_χ = 0.3, v₀ = 238, v_esc = 544, v_E per 2105.00599).

## R5 WP5 (energy partition), 2026-10-31: CLAIMED, pending R×2
- Theorem C (DERIVED): every hot-carrier rate is the WP0 master formula with the carrier as projectile coupling to the total charge, which is the GW lifetime (0812.2923 eqs 1–2). Impact ionization and plasmon emission/decay are one channel, so there is no separate plasmon species. In GaAs, LO emission comes from the total ε; add only the short-range e–ph.
- One branching generating-functional equation (W3), seeded by the WP0 final-state-resolved response. Its first moments give Lindhard (L20), the R&K mean yield (L21) and Kinchin–Pease (L22); its second moments give the Fano factors F and F_NR (L23).
- Exact energy bookkeeping (W4): F = (ε/E_g − 1)·Var(H)/(E_g⟨H⟩). Klein's 14/5 E_g is a truncation. A phonon shot-noise estimate gives F ≈ 0.121 (Si) against 0.119 measured, possibly coincidental. [superseded R8: F ≈ 0.121 has no evidential weight (IF-R8-8); R16: F_eh from GAP-EF-v2 (LIMITS L23)]
- NR: the multiphonon → MD handover is fixed (Doppler spread ~√(E_R⟨ω⟩) ~ 1 eV at E_d, so the threshold is smooth). Binary e–ion collisions cannot create e–h pairs below E_R ≈ 375 eV (Si) and 465 eV (Ge) (est.) [superseded R8: ≈ 352/399 eV [book; 395 was E_g = 0.74 eV], soft (IF-R8-8)]. Below that, Lindhard's S_e ∝ v is a fit, not a limit, and sub-keV ionization data test Landau–Zener close-collision excitation. Stored defect energy ≠ E_d. 2301.06592's ionization threshold = E_d is NOT a URF limit.
- Source discrepancies:
  - R&K: A has units eV³, not eV², and their eq 9 needs |M|².
  - R&K App A: the measured Fano factor is ηF + 1 − η, not F/η + 1 − η.
  - 2001.06503 and 2209.04503: reduced-energy conventions differ by 10%.
  - 2209.04503: the ½εS_e coefficient is not reproduced. [superseded R8: ½εS_e is derived in 2001.06503 App. B; the objection is the (D)-inconsistency; the L20 observable is ℋ_nuc + E_st, BCA = truncation 0 (IF-R8-8; LIMITS L20)]
- WP0 defects: (7.3) integrates out q before seeding; the seeding weights must keep tr(𝔇·) inside the final-state sum; listing plasmons as a final state alongside RPA e–h pairs double counts. All OWED corrections to WP0 §7.
- Not closed (exact remaining gaps): R1–R6 in WP5 §9.

## R5 O4 (X0/X+ convention independence), 2026-10-31: CLAIMED, pending R×2
- (iv′) DC (Dyson convention): X0 = 2πZ|ρ̃|²δ(ω−Ẽ); X+ = the finite-part + PV sideband. It reduces to D1/D2 inside the window.
- (iv″a) DERIVED: the total is convention-invariant at O(g²) for observables smooth on the δ scale (Ward identity −2ImΣ = Γ̂; Z + (1/2π)fp∫Γ/Δ² = 1); toy residual ∝ g^3.97. WARNING: the mixed pairs double count (Lorentzian ZPL + fp sideband: O(g²); Lorentzian ZPL + resummed sideband: O(1)).
- (iv″b) DERIVED with an amendment: P(N_eh|…) is invariant if the cascade is Markov and its first-emission kernel uses the same g, ω_Q and ε. The Fano production–decay interference term 𝔉 vanishes for PT-symmetric crystals (Si, sketch) and is generically ≠ 0 in GaAs (CONJECTURED). The response and cascade inputs must be consistent: a 10% error in ω_TO in the cascade gives an O(1) error in P(N_eh).
- (iv″c) DERIVED in an admissible class: |Δw₀|/w₀ ≲ (1.1 + b_λ)Γ/δ; FALSE universally (the t→∞ convention moves O(1) weight but still satisfies a and b).
- (iv″d) Eleven response/cascade code-pair consistency conditions (O4 §6), for CONVENTIONS and the WP6 library spec.
- Theorem D amendments: outside the window X+ is not separately positive and Z can exceed 1; the split is meaningless within ~Γ of E_min (Si: Γ/δ ≈ 0.02–0.6, rough) [superseded R8: 0.007–0.2 at δ₀ = 0.3 eV].
- Conclusion for the user's criterion: experimental predictions (total rate, quanta distribution) are convention-independent at O(g²) when the code-pair conditions hold.

## R5 WP1 (electronic sector), 2026-10-31: CLAIMED, pending R×2
- L1: the Essig f_crys ↔ S dictionary (E12) matches 2101.08275 eq 16, so SOTA #7 (Essig prefactor) → CROSS-CHECKED.
- O5: static ε(q,0) ≥ 1 PROVEN at RPA+LFE for any insulator [amended R8: ch = c and clamped ch = e; relaxed electron channel false in general, WP0-v3 G6] (beyond RPA, est. holds for Si/Ge). This upgrades L17's conservative bound to DERIVED at RPA+LFE.
- On shell, the longitudinal relative velocity cancels exactly, so only transverse currents survive. Only 3 of Catena et al.'s 5 crystal responses (2105.02233) are independent. 2510.25835's O₈ "fixed by ε" claim omits the transverse current (~40× underestimate in Si, est.), so their O₈ limits are conservative.
- Spin channel (no SOC, IP): S_ss = ¼ of the UNSCREENED density response, with an XC enhancement only. Minimal response table: 7 real functions per (q,ω).
- Finite-q excitons:
  - Selection rules: Si VBM→CBM with q∥[100] is symmetry-forbidden; Ge (q∥[111]) is allowed.
  - Thresholds: Si zero-phonon indirect exciton at 0.473 MeV (forbidden class), allowed Umklapp at 0.708 MeV; Ge at 0.420 MeV. [superseded by [E13] (§R8)]
  - The Sommerfeld near-edge enhancement is ×1.3–2 in Si (est.); the survey's "<10%" is CORRECTED.
  - IMPLICATION for M1: in Si the first-order (zero-phonon) edge near the PAER window is dipole-forbidden at leading order, which strengthens the PAER case.
- Plasmons: Landau-damping onset in Si at q_c = 1.88 keV [superseded R8: ≈ 2.24 keV], but reaching ω_p needs q ≥ 6.3 keV, so there is no bulk plasmon for halo DM. The literature uses three inconsistent cutoffs.
- Relativistic cores: factorisation is exact with full Dirac bilinears. The f-sum shift is −(5/3)⟨T⟩/m (−0.18% Si, −0.58% Ge). The Ge 3d error is dominated by the XC placement.
- Anisotropy: T-reversal kills odd ℓ and cubic symmetry kills ℓ = 2, so the ELF anisotropy cannot modulate the dipole Migdal rate in Si/Ge/GaAs. 2607.06005's "dipole" attribution is WRONG (needs a full-text double check at referee stage).
- WP0 defects (6, WP1 §9): owed corrections. Notation collisions κ (Sommerfeld) and W̄ → 𝒲̄ go to NOTATION-APPLY.

## R5 WP4 (spin / SC / special targets), 2026-10-31: CLAIMED, pending R×2
- L13 magnons: 1905.13744 eqs 5–12 and 2009.13534 eq 38 are recovered term by term (6-step chain). Missing correction: the magnetic form factor (~0.5 at q ≈ 0.5 keV for Fe³⁺, est.). 2009.13534 eq 36 has an S^± vs S^x,S^y label slip.
- L15 superconductors: the bare BCS bubble of 2609.06423 violates conservation (q→0), so the phase-mode vertex is needed. Closed form: the BCS rate = g_I(ω/Δ) × Lindhard (π/2 at 2Δ⁺, 1.15 at 5Δ, 1.05 at 10Δ). Mattis–Bardeen is recovered to 10⁻⁶. [superseded R7/R8: see R7/R8 entries; 𝔤_I novelty UNRESOLVED, phase term credited to 2609.06423]
- L15 source errors:
  - 2101.08263 eq 3: Re ε should be λ_TF²/q² (×4 in that illustrative formula; numerics unaffected).
  - 1512.04533 eq 13: missing a factor 4.
  - 2609.06423: time-ordered rather than retarded propagators.
  - The 2101.08263 branch-cut ambiguity is removed by building Im ε from positive S (WP0 4.1) and Re ε by KK.
- G9 films: Mermin-conserving relaxation. The Drude form (QROCODILE, WSi) is exact only for qℓ ≲ 1 and underestimates the ELF by πqℓ/6 for qℓ ≫ 1, so their limit is conservative. Thin film: O(1/qd). [superseded R7/R8: see R7/R8 entries; QROCODILE claim withdrawn]
- L16 Dirac: 2101.08263 eq 4 recovered exactly. HIGH-PRIORITY REFEREE CHECK: 1708.08929 and 1910.02091 appear to omit the 1/κ² background screening for dark-photon coupling, so their rates would be ~κ² ≈ 1600× too high at the benchmark. This contradicts published work and must be verified against full text before any claim. [superseded R7/R8: see R7/R8 entries; κ² REFEREED] 1910.02091 eq 3.14 typo.
- Chiral/CD: a density-coupling wind asymmetry requires broken P and T. A chiral T-even target shows an enantiomer difference only via O₅–O₈ interference, which probes parity-violating DM couplings.
- Gaps closed with formula + spec: two-magnon continua (0 for a Heisenberg FM, O(1/2S) otherwise); magnon–phonon hybrids; dopant and NV final states; exothermic DM into phonons/magnons (halo-independent line spectra to O(v/v*)).
- WP0 defects (6): hyperfine contact term ×2 too large and sign +; Theorem D gap hypothesis fails for metals/SC/semimetals (scope must be stated); L15 and L16 pointers; table 6.1 small parameters; P,T-broken wind-odd rates unflagged. Exact remaining gaps: RG1–RG8. Notation collisions κ, Λ, g, Δ, τ, v_k, V go to NOTATION-APPLY.

## R5 WP3 (mixed electron–lattice sector), 2026-10-31: CLAIMED, pending R×2
- Joint response S_ab(q; ω_ph, ω_e), defined in the Theorem D frame plus an e–ph Schrieffer–Wolff step; its marginal is exact. Seven sum rules. Two appear new:
  - the electron-energy moment of the Migdal spectrum equals the Born–Huang electron-drag mass;
  - the electronic part of the e–N cross first moment is −(q²/m_A)F(q).
  The multiphonon–Migdal and PAER–ZPR double-counting rules follow as identities.
- Migdal: atomic (1707.07258), crystal ELF (2011.09496), small-q EFT (2210.06490, 2505.08864) and phonon-mediated (2205.03395) are all truncations of one formula (L7a–d); the 4α prefactor is reproduced. 2603.13052 eq 4.7 is dimensionally wrong as printed (half of KKL), compensated by a doubled dσ/dq, so its rate is consistent. [superseded R8: 1/m_N misplaced (4.6)→(4.7); (4.8) UNRESOLVED] [superseded R16 (CW2 OC-9): (4.8) CONFIRMED (R16 CW2 §16): (4.8) is 2× the standard; rate unaffected] The EFT breakdown claim is conservative: the true parameter is |q·p|/(Mω_e) ~ 4×10⁻³.
- M1: X1 and X2 are confirmed by WP3. C7 uses X1's C7a–e (WP0 4.9 agrees only at band extrema). The screening uses X2's M̃ (WP0 5.6–5.7 is a truncation).
- L9: the 8π²α/(Ωω²) prefactor is confirmed in full text (EPW 2302.08085 eq 63; Noffsinger eq 1), so SOTA #9 → CROSS-CHECKED. Data-driven σ₁ at 77/300 K needs a T-transfer to mK; uncorrected, it overestimates the Si edge rate. NEW: a phonon-assisted kinetic-energy-density channel for scalar absorption.
- L12 ZG/Williams–Lax drops ω_ph from the energy δ (1604.02394 eq 24). At T = 0 its onset is 18–58 meV too low in Si, which matters in the PAER window. Never add a ZG spectrum to a separate PAER sideband; the hybrid formula is given.
- Crystal NR bremsstrahlung (GAP CLOSED): rate ∝ n(ω)|Z*(ω)·q/M|² × lattice structure factor; it reduces to Kouvaris–Pradler in vacuum. Si/Ge: Z*(0) = 0, so it is ∝ ω⁴ suppressed. GaAs: a sub-gap photon channel ~10³× the atomic estimate (est.).
- Exciton–phonon replicas: formula + spec (effective-mass √-onset limit).
- Exact remaining gap: a converged finite-q BSE for Si/Ge has never been done.
- WP0 defects (6) including: L7d spans X0 and X+; Migdal–PAER interference applies to any e+N coupling; the boost mass is m_A; ZG is a deterministic quadrature. Notation: ℓ_Q normalisation, exciton S vs S_ab, n(ω) vs n_Qν, n_e → NOTATION-APPLY.

## R5 WP2 (lattice sector), 2026-10-31: CLAIMED, pending R×2
- Exact harmonic coherent S_NN at finite T and all phonon orders, plus a shell expansion (zeroth term = incoherent approximation). BZ-average theorem: incoherent = the coherent S averaged over a BZ. [superseded R8: exact only for Bravais lattices, q ≫ max(n_ph,2W)q_BZ (WP2-v3)]
- 2607.24933 eq 47: in 3D the coherent and incoherent forms differ beyond the momentum δ (polarisation weights, intra-cell phases).
- Truncating at N phonons loses P[Pois(2W) ≥ N] of the f-sum. An exact recursion gives all orders plus the final-state phonon spectrum for WP5.
- L4: WP0 (5.4) with the total ε ≡ the Z*/ε∞ formula with LO eigenvectors (Sherman–Morrison); reproduces 1910.08092 eq 106 and 1807.10291 eq 31. 1712.06598 eq 5 has an inconsistent 1/V_cell.
- L6: the self-part cumulants are exact with anharmonicity; ⟨ω⟩ = q²/2M exactly. The third cumulant = lattice (BO curvature) + Migdal, tying to WP0 (4.7) and WP3. The Helm rate is recovered (hep-ph/0608035 eq 5).
- L18/G13: the anharmonic nuisance obeys three exact linear constraints; impulse effect O(λ²(ω̄/E_R)^{1/2}). 2309.10839 eq 9: e^{−W} should be e^{−2W}.
- Nuclear spin: unpolarised gives an exactly incoherent, nonzero channel (dropped by PhonoDark 2009.13534, included by 2506.11191); polarised adds a coherent term ∝ P².
- L19/G11: in cubic crystals the harmonic incoherent multiphonon S is exactly isotropic at every order and T, which explains the null modulation of 2411.03433. The soft-limit Migdal modulation in Si/GaAs vanishes (agrees with WP1's symmetry result).
- WP0 defects: x_coh = q/G_min is the wrong control parameter; the 2W formula holds only for cubic sites. 7 exact remaining gaps. Notation collisions → NOTATION-APPLY.

## NOTATION-APPLY (2026-10-31)
CONVENTIONS.md (22 decided disagreements, §13), NOTATION.md v3 (~300 rows, 162 collisions renamed) and state/CORRECTIONS.md were written. The cross-return audit (26/26) shows every return agrees on the master rate, S↔L, ε₂^PA, the optical prefactor, M^(2), M̃ and the halo factor, apart from the known owed corrections. Remaining coordinator-level defects are listed in CORRECTIONS.md (coordinator additions).

## R6 WP0-v2 (2026-10-31)
- Standalone architecture with O4, X1 and X2 folded in. 38 corrections applied, 1 contested in part (CC-1: out-state vs in-state local-field weight; both give the same total, the physical prompt state uses retarded (ε̃⁻¹)_{G0}). 44/44 sympy checks. Interface flags F1–F11 are routed to the REV agents via CORRECTIONS.md.

## R6 WP5-v2 (2026-10-31)
- 26 corrections applied, 0 contested; 34/34 sympy checks. F2 applied (the pair class enters only phonon-assisted impact ionization, as a truncation). F8: the GaAs Fano-term effect on P(Q) is bounded, |ΔP| ≲ 0.11 Γ/δ (~2×10⁻³ off-edge, up to ~7×10⁻² in the edge shell); it is zero in Si/Ge. New exact gap R7: needs the response-code export.
- Interface flags: I1 (WP4 η_pb factor 2, relayed to REV-WP4), I2 (adopts WP2 (5.3)'s anharmonic impulse width), I3 (uses WP0-v2 (7.2) not WP1 [E2] for GaAs pair splitting), I4–I8 bookkeeping.

## R6 WP4-v2 (2026-10-31)
- 32 owed corrections applied, 0 contested, plus 8 v1 errors fixed:
  - the chiral enantiomer-difference formula [3.3] was off by a factor −½;
  - the magnon spectral-budget prefactor is 8.4%, not 2%;
  - the one-phonon phase is e^{iq·r_κ};
  - the magnon absorption term in [2.2] is corrected;
  - four smaller fixes.
  23/23 sympy checks.
- η_pb resolved: η_pb = Δ_BCS⟨N_qp⟩/ω (=1 at 2Δ⁺); the factor 2 is dropped (WP5 I1 closed). [R8: N_qp = 2, η_pb = 2Δ_BCS/ω for ω < 4Δ_BCS, not 3Δ_BCS (WP4-v3 K27, I2; WP5-v4 §5; IF-R8-7)]
- New closed form: 𝔤_I(y) = (1+2/y)E(k) − 4K(k)/(y+2), with k = (y−2)/(y+2) (π/2 at threshold; matches the integral to 10⁻¹²).
- Theorem D-g for gapless targets: partly derived, the rest conjectured. At the Dirac benchmark coupling (0.91) the sector split is non-unique, so only totals can be quoted.
- The L16 ε_bg² claim is downgraded to a conditional pending the R7 full-text check (OW4-2).
- Flags relayed: odd-ℓ harmonics for P,T-broken targets → REV-WP6; the phonon phase convention → REV-WP2. NOTATION: n_D → 𝓃_D for the defect density.

## R6 WP6-v2 (2026-10-31)
- 26 corrections applied, 0 contested; 24/24 sympy checks; m_min and halo numbers recomputed at v_E^ref = 250.5 km/s and v_max = 794.5 km/s.
- Odd-ℓ harmonics for P,T-broken targets now included (WP4 relay done).
- Changes: seeding has tr(𝔇·) and the q integral inside the Λ sum; the halo-independent bound now needs a positivity hypothesis (P), since O4 showed per-sector non-positivity outside the window (REFEREE ITEM); the v1 regime A was empty, so regimes are now set by the crossover δ_v,× = 173 km/s; the edge exponent is proved for any power-vanishing tail; n_T is separated from T; the kernel-ladder error estimate is withdrawn for releases.
- Flags: NOTATION rows needed for θ_{R-k}, a_k, ℒ, π_k, and experiment index ex (IF6-1..3); WP2's "G sector" → GS (IF6-6).

## R6 WP1-v2 (2026-10-31)
- 32 corrections applied, 0 contested; 28/28 sympy checks. F1 ACCEPTED after an independent derivation: the out-state weight (ε⁻¹)_{G0}ρ(q+G) is now adopted campaign-wide (WP0-v2 7.2, X2 2.2, WP1-v2 E2), which closes the GaAs item pending R7. Exciton thresholds at v_max = 794.5: 0.472 / 0.708 / 0.420 MeV.
- 2607.06005 re-read in full text: the "dipole" attribution sentence is in their §III (Fig. 4 discussion), and the v1 verdict stands.
- IF-3 (a real mismatch, fixed by a relay to WP6): the BSE fallback nuisance is [+0.3, +1.0]×S (type M) near the edge plus type A for the exciton lines, replacing η_xc·S ≈ 1%. IF-1 relayed to REV-WP3. IF-9: 9 NOTATION rows to add.
- WP6-v2 IF-3 fix applied (row 27): BSE interim type M [+0.3, +1.0] for E_min ≤ ω ≲ E_min + 1 eV plus type A for the exciton lines; 24/24 checks.

## R6 WP2-v2 (2026-10-31)
- 36 corrections applied (5 self-found: the truncation-loss formula holds at any T and for the coherent S; endpoint masses 17.3/21.1 MeV; the anharmonic toy model 7% low; 1807.10291 eq (32)); 0 contested; 21/21 sympy checks.
- Phase convention fixed: eigenvectors carry only the cell phase, so the intra-cell factor is e^{iq·r_κ} at all orders (matches WP4-v2; same |·|² as v1).
- F4 resolved at moment level: the first moment of the Migdal sector = WP3 J3 drag mass; the 𝓜³_κκ|_{V_eN} = −(m_e/M_κ)𝓜³_eκ (audit: WP2-v2 (5.2′) and WP3-v2 J8 are the same identity; the earlier SOTA paraphrase was wrong). OWED by WP3: 𝔨₃^X from all-electron all-k (relayed).
- Relays: IF-2 → WP5 (subtract the Migdal drag energy if seeding separately; negative ω′ = absorbed phonons); IF-4 → WP6 (anharmonic nuisance must preserve the three constraints). NOTATION rows: V_pot (V collides with the volume), E^ad_n, q_BZ, G_min.

## R6 WP3-v2 (2026-10-31)
- Standalone. Part I is the consolidated M1 (PAER) theory: D1/D2 corrected per REF-A/B, plus X1, X2, O4 (M.1–M.16). Part II is the mixed sector in NOTATION v3. 63 corrections applied, 0 contested; 59/59 sympy checks.
- The (W.5) external local-field weight is resolved by derivation (out-state), consistent with WP0-v2/WP1-v2.
- New: J8 (the Migdal third moment, with 𝔨₃^X from all-electron all-k); the PAER onset exponent p_on = 2/3/½ (→ WP6); the GaAs Fano-term bound 𝔉 ≲ 0.3 of first-emission branching (ΔP ~ 2×10⁻³, est.).
- R7 ITEM (IF-2/F4): normalisation mismatch with WP2-v2. WP3 gets the contact 𝔨₃ = −(m_e/M_κ)·𝓜³/(2𝓃_κ), with (4.7) per unit volume, against WP2-v2's −(m_e/M_κ)·(4.7). For the audit to resolve. [RESOLVED (AUDIT-2 §7)]
## R6 WP5-v2 IF-2 follow-up: applied (Migdal drag energy E^Mig_1 = q·δM_κ·q/2M_κ² subtracted from the GS seed f-sum; ω′ < 0 = absorbed phonons); 37/37 checks. Its I1/I3 flag text is stale (resolved in WP4-v2 and WP1-v2); the audit should note this. [RESOLVED (AUDIT-2 §7)]
- WP6-v2 final: anharmonic nuisance (5.1′) preserves the 3 constraints for all θ (moment-projected type-A shape); PAER p_on = 2/3/½, giving edge exponents 11/2, 13/2, 4 (+k_tail) with a type-Δ case nuisance; 29 corrections, 26/26 checks.

## R6 AUDIT (2026-10-31)
- 1 blocking (A1: the PAER onset exponent must be for the angle-averaged S̄; WP3 then WP6), 20 minor. All interface quantities agree across packages. The 𝔨₃ "mismatch" was a SOTA paraphrase error; the two packages give the same identity. Gaps G1–G13 and the catalog §12 gaps are all closed with formula + specification or recorded as exact remaining gaps. Catalog coverage (91 rows): A 45 · B 25 · C 11 · D 10.
- Dispatched: A1, A6–A8, A10 → WP3; A2–A5 → WP0; A9, A12, A15 → WP6 (A1 follow-up later); A11 → WP5; A13 → WP2, WP4; A14, A20 → NOTATION v4.
- Coordinator items applied: A16 (LIMITS v2 status table), A17 (SOTA §15), A18 (CONTROLS C4/C7, README), A19 (L1-ERRATA.md).
- Campaign threshold convention (A9): E_th = measured E_g(T_op). Si at mK: 1.170 eV → m_min = 0.333 MeV; PAER window lower edge 0.338 MeV (E_g + ω_TA). [superseded R8: 0.333–0.337 MeV (WP6-v3 (3.1′))]

## R6 audit fixes applied (2026-10-31)
- WP3-v2 A1 (blocking) RESOLVED. The angle-averaged S̄^{X+} threshold has an isolated quadratic minimum at q̂ ∥ K, so p_on = 3 (generic), 4 (vertex zero on the minimising direction). Si TA edge 4 (deformation coupling vanishes for transverse ê on the valley axis [E]); LA/TO/LO kinks 3; forbidden pockets 4–5; exciton replicas 3/2–5/2. Shells with d < Q_w ≈ 0.2 Å⁻¹ (Si) [superseded R8: 0.33 Å⁻¹ at δ₀ = 0.3 eV] are edge shell (Dyson convention). C5 corrected (infimum E_g, window empty there). Also A6–A8 and A10. 68 corrections, 66/66 checks.
- WP0-v2 A2–A5 (42 corrections, 44/44); WP2-v2 IF-8 closed (37); WP4-v2 I3 closed (43); WP5-v2 A11 (28, 37/37); WP6-v2 A9/A12/A15 (32, 27/27; Ge re-based on E_g(0) = 0.744 eV → 0.212 MeV, coordinator-unreviewed, an R7 item [superseded R8: consistent across WP1/WP3/WP6 (AUDIT-2 §5)]). WP6 A1 follow-up in progress.
- NOTATION v4: A14 collisions renamed, ~75 rows added (§M), further collisions fixed. CORRECTIONS §17 lists the renames owed inside the v2 returns; these are to be applied before R7 (user directive: resolve all corrections before hostile review).

## R6 SECOND PASS COMPLETE (2026-10-31)
- All seven v2 packages are revised, audited (1 blocking + 20 minor, all resolved) and renamed to NOTATION v4. Checks, rerun by the coordinator: WP0 44/44, WP1 28/28, WP2 21/21, WP3 66/66, WP4 23/23, WP5 37/37, WP6 27/27.
- Ambiguous leftovers, not renamed: WP5 E₀ and dE/dt|_ph in (W8); old names kept in history rows.
- Next: R7 hostile review (2 isolated referees per package; briefs in briefs/R7/).

## R7 referee reports (arriving)
- REF-WP2-A: 0 FALLS, 19 STAND, 11 STAND w/ corr. BZ-average theorem exact only for Bravais lattices (with a basis, the inter-sublattice shells survive). 𝓜³_κκ = −(m_e/M_κ)𝓜³_eκ needs q·a_core ≪ 1. CONFIRMED vs FT: 2607.24933 eq 47 (polarisation weights; drop the intra-cell-phase charge), 1712.06598 eq 5, 2309.10839 eq 9. REFUTED: the 2205.02250 "peak shift".
- REF-WP5-B: 0 FALLS, 12 STAND w/ corr. Theorem C fixes: the out-rate only; the LFE Coulomb index ε⁻¹_{GG′}v(p+G′); an added Z*/ε_∞ consistency condition; "plasmon = e–h channel" fails for an undamped pole (Al). Binary-collision thresholds ~352/399 eV [book; 395 was E_g = 0.74 eV], not 375/465. The Lindhard chain misassigns U. CONFIRMED: R&K units and |M|², R&K App. A (but the correct inequality is F(1/η − η) ≥ 0), 2001.06503/2209.04503 10% and BC; REFUTED: R&K "Δ undefined", "½εS_e not derived".
- REF-WP4-B: OW4-2 CONFIRMED vs FT. 1708.08929 and 1910.02091 define ε_r = ε_tot/κ and use F_med = 1/ε_r with vacuum σ̄_e, so their dark-photon scattering rates are κ² (~1600 at κ = 40) × the correct rate. NEW: their absorption rates are too large by κ. Awaiting REF-WP4-A for independent confirmation before any firm claim. Also CONFIRMED: 2101.08263 eq 3, 1512.04533 eq 13, 2609.06423 eqs 7–8. REFUTED: 2609.06423 eq 4 is a legitimate T=0 Feynman propagator; the QROCODILE Drude claim (its limits use Lindhard with ω+iΓ). Corrections: 0.13 keV → 0.13 eV; credit 2609.06423's vertex estimate; [3.2] odd part O(q³); Theorem D-g (a) needs [H, UNU†] = 0 or a cross-term error.
- REF-WP4-A independently CONFIRMS OW4-2 (R×2 vs FT). 1708.08929 and 1910.02091 overstate dark-photon scattering rates by κ² (×1600 at κ = 40; ×640 for ZrTe₅) and absorption rates by κ; each paper is internally inconsistent (cutoff charge e/√κ against vacuum e at the vertex). The WP4 §5.3 statement becomes FIRM (REFEREED), with the explanation sentence replaced per REF-A. FALLS: the QROCODILE "conservative" claim (both referees); 𝔤_I is "the analytic form of 2609.06423's agreement" (both). CREDIT OWED: 2609.06423 already gives the phase-mode correction and its 1/25 bound, so drop the novelty claim. Both: the 2609.06423 propagator is not a defect; reality not causality; Theorem D-g (a) needs [H,N] = 0 (the bin condition); 0.13 eV; N_qp = 2 holds up to ω < 4Δ.
- REF-WP6-A: 9 STAND, 12 STAND w/ corr., 2 FALL.
  - FALLS: "the η̃ profile is unique" (only the fitted rates are unique; ker 𝒜 ≠ 0).
  - m_min values are correct, but are kinematic LOWER BOUNDS: the general edge is min_q[E_th(q)/q + q/2m_χ] = v_max (the PAER edge still ≈ 0.339 MeV).
  - The edge exponent stands (also with q-dependent thresholds); add bound-exciton lines p_on = −1.
  - Halo reduction: tensor orientation average; T-reversal kills all odd ℓ; no cubic ℓ = 1.
  - (P) needs 𝒜_i(v) non-decreasing (follows from PSD) plus a yield-uniformity condition, which fails near step-cascade jumps; an integrated-kernel library check is required.
  - (5.1′): positivity forces a sign on θ_δ, so the 𝒩(0,1) prior is unrealisable; fix by exponential tilting.
  - The profile-vs-envelope "×1.8" is not like-for-like (1.35 log-normal / 1.57 linear); the same error is in WP0-v2 (8.3).
  - Edge-sensitivity factors ×2.26/×0.10; notation reuse of K, δ, d.
  - CONFIRMED vs FT: 2311.04957 D1, D3/D5; D2 is an ambiguity; D4 is incomplete (1509.01598 eq 67 cutoff).
- REF-WP2-B (agrees with WP2-A on every shared item): 12 STAND, 11 w/ corr., 1 FALLS (the 2205.02250 "peak shift" claim is refuted). The BZ-average theorem with a basis needs all inter-site shells, and the gradient term needs q ≫ n_ph q_BZ. Shell-size estimate ~10% at 2 keV. 𝓜³ contact relation needs q·a_1s ≪ 1 (9% off at 51 keV, 29% at 102 keV). CONFIRMED: 1712.06598 eqs 5 and 12, 2309.10839 eq 9 (v1), 2009.13534 drops the spin channel, 2607.24933 eq 47 weights. Panjer recursion is forward only at T = 0; isotope disorder caveat on the spin channel. → WP2 R×2 COMPLETE.
- REF-WP3-B: 1 FALLS, 11 w/ corr.
  - FALLS: Si TA edge p̄_on = 4. With anisotropic TA velocity (Christoffel) q̂ ∥ K̂ is a threshold MAXIMUM; the true minima are off-axis (φ ≈ 0.41 rad) at ≈ E_g + 0.966 c_TA d with nonzero coupling, so p̄ = 3. Also no on-axis vertex zero (the valence shear deformation potential is symmetry-allowed). WP6 must not use "Si TA 4".
  - Corrections:
    - (M.13) is RPA-only: ALDA needs a second-order xc source, and W is retarded.
    - The [0.5, 1.2] systematic assumes the sign of δ_pair; with the sign open it is [0.5, 1.7].
    - The thermal factor is double-applied (O(e^{−E_g/T})): use EPW eq 64.
    - The δ₀ = 0.1 eV examples violate δ₀ ≫ ω_max.
    - L7c correction ≲10⁻³; the δM/M bound is not derived.
    - (W.13) "∝" means bremsstrahlung is not fully closed; GaAs ratio 10³–10⁴.
  - CONFIRMED: 2603.13052 eq 3.11 (+K); eq 4.7 dimension (but m_N is misplaced between 4.6 and 4.7; C3 ignores 4.6). 1604.02394 eq 24 is the declared adiabatic limit, so it is a characterisation, not an error. EPW band-sum statement; 2210.06490 fn 3.
- REF-WP6-B (agrees with WP6-A on every shared item):
  - 0 FALLS (claim level); the "η̃ unique" statement REFUTED.
  - (4.2) needs non-decreasing step columns (derived from (P) + positivity of 𝔇). The (P) sufficiency proof is circular, and (P) fails for ~1–2% of pairs under Dyson-convention seeding.
  - ×1.8 → ×1.35 (M) / ×1.57 (linear); WP0-v2 (8.3) inherits it.
  - Edge exponent 4 + k_tail + p_on at a threshold corner; the power law holds only within Δm/m ≲ 1–5%. At m_min the generic 13/2 + k_tail applies (the TA onset is out of reach below 0.366 MeV).
  - m_min values are lower bounds.
  - Element-wise M nuisances break 16×16 PSD; A is not automatically positive outside the window. Prior ranges contradict their types.
  - The ℓ = 1 projection survives the daily average for P,T-broken targets.
  - → WP6 R×2 COMPLETE.
- REF-WP0-A: 9 STAND, 9 w/ corr., 0 FALL.
  - Main corrections:
    - rate index order: Σ𝔇_abS_ab = tr[𝔇ᵀS], not tr[𝔇S] (it matters with antisymmetric imaginary parts); fix (3.4), (7.3), CONVENTIONS §8;
    - (4.7) q→0 limit is missing the uniform-density term: 𝓜³ = −q²Ze²𝓃_κ[𝓃_e(R) + 2𝓃̄_e]/(3mM) (~10⁻⁴ in Si), so recheck F4 against J8;
    - L17 (iii) fails for the electron-only channel when the lattice relaxes (two-fluid ε_e⁻¹ can be negative, ×2.3 in GaAs-like cases); the rate bound is 2110.01587 eqs 8–9;
    - the Breit orbit–orbit term is missing from H_rel (~27% of the mass-velocity f-sum shift).
  - Minor corrections:
    - 𝒪₂ is not in the 16-operator basis;
    - R^∞ in (4.2);
    - the ionic "Coulomb" class is a phonon line;
    - Theorem D: κ_BO² parameter; positivity only up to leakage; the true rigour gap is uniformity in the number of nuclei;
    - (6.3) missing 2/V;
    - O4 imports (b_λ, 𝒞_adm, d1–d11) undefined.
  - STANDS: CC-1 (confirmed physically), screening (5.1)–(5.7), C7 structure, L0. All checked source quotes CONFIRMED in full text.
- REF-WP5-A (agrees with WP5-B on every shared item; WP5 R×2 COMPLETE): 0 FALL, 3 clean, 17 w/ corr.
  - Theorem C:
    - (W1) is the out-rate; = 2|ImΣ| only without the f·n_B term; = the GW lifetime only at Z = 1 (0812.2923 has 2Z|ImΣ|, Z ≈ 0.8);
    - the code-pair conditions (shared Z*, ε_∞, multipole order, Ewald cutoff) must be stated.
  - Born parameter ≈ 15 (v_F); (W3) needs almost-sure termination and the minimal solution; (B2) pair density 3×10²⁰ cm⁻³; Lindhard limit needs BCA + Markov; renewal asymptotics [D, sketch]; thresholds ≈352/399 eV [book; 395 was E_g = 0.74 eV] (soft).
  - R&K: eq 23 is an upper bound because (23) − exact = F(1−ϵ²)/ϵ ≥ 0. 2209.04503 Z₁ claim UNRESOLVED.
  - W15: c^F dimension fix; the worst case is |ΔP| ≲ 0.3Γ/δ.
  - Migdal subtraction: the correct prescription is (1 − P_Mig)·S^GS with mass M + δM, and checks C20b/c must be fixed.
- REF-WP3-A (WP3 R×2 COMPLETE).
  - FALLS: Si TA onset 4. By group theory (C4v, no SOC) TA is ALLOWED on the valley axis and LA is FORBIDDEN, so the Si edge exponent is 3 and the LA kink is 4. The package's soft-limit argument can't distinguish branches, because ρ_cv = 0 on the axis for all of them. REF-B reaches p̄ = 3 by a different route (anisotropic c_TA gives off-axis minima), so both agree p̄_on = 3 for the Si edge. They disagree on the LA kink (REF-A: forbidden on-axis, exponent 4; REF-B: not addressed); the revision must settle this with a full-text-checked symmetry analysis.
  - Thermal factor double-counted ((W.4c) false at T > 0; F7's "fix" is itself the double count).
  - 2603.13052: the package's m_N² fix is REFUTED; the correct fix moves 1/m_N from eq 4.6 into eq 4.7 (both referees). The +K sign error is CONFIRMED.
  - ZG mechanism mis-cited (it is alternating signs in eqs 7–10, not antithetic pairing).
  - Interim factor: [0.4, 1.2] / [0.4, 1.8] without the sign assumptions (REF-B: [0.5, 1.7]). The revision must state the assumptions and adopt the wider envelope.
  - 1608.01994 overestimate is O(1) only within ~20–25 meV of the edge.
  - L7c correction ~4×10⁻⁴.
- REF-WP0-B (WP0 R×2 COMPLETE): 1 FALLS in part, 9 w/ corr., 6 STAND.
  - FALLS in part: Theorem D's scope. "Magnetic insulators" are excluded by (H2). The error order is in ε = κ_BO² (PST); PST is cited from its abstract only. Point nuclei fail the Spohn–Teufel smoothness condition, but finite nuclear size fixes it. The real gap is non-uniformity in system size. Agrees with REF-A.
  - Corrections:
    - (4.5) is false off-diagonal: pair S_ab[O] with S_ba[O†].
    - (4.2) R^∞ = 0 for every operator (agrees with A).
    - (4.3) the nonreciprocal part of S_ee is O(q³).
    - (2.2) spin-current rows need [H, s_i] = 0.
    - (5.5) the ionic class is a bridge (agrees with A).
    - (5.7) needs a retarded W; "R Hermitian" holds only for the external factor.
    - L17 (iii) fails for electron-only coupling with a relaxed lattice (2.30 GaAs-like; matches A); 2110.01587 §VII warns of this.
    - Bohm–Staver: use the clamped ε.
  - REFEREE DISAGREEMENT on (4.7). REF-A: the q→0 limit misses a uniform-density term 2𝓃̄_e (~10⁻⁴). REF-B: (4.7) holds, the contact term is exact at all q, and the cubic correction is O(q⁴). The revision must settle it with an explicit derivation (a conditionally convergent PV ℓ=2 term: A's point) and say which q-ordering of the limits is meant.
  - STANDS: C7 import, L0/L17 source quotes (eq 4 of 2110.01587 is an inequality: citation slip).
- REF-WP1-B: 1 FALLS, several w/ corr.
  - FALLS: the exciton thresholds 0.472/0.708/0.420 MeV pin q at Q_x+G. Because ∂E_min/∂q = 0 there and Q_x v_max > 2E_x, smaller |q| gives a lower m_χ. Si G=0 zero-phonon exciton: ~0.40–0.43 MeV [E], INSIDE the 0.338–0.47 MeV "PAER-only" window. Ge: zero-phonon via the direct Γ valley at 0.256 MeV.
  - IMPACT ON M1 (must be resolved in the correction round): the PAER-only window in Si narrows to ~0.338–0.40 MeV. Above that, the zero-phonon exciton channel is open but symmetry-forbidden at leading order (WP1 selection rules), so PAER may still lead; this needs the relative size. Ge window effectively closes (~0.20–0.256 MeV).
  - Corrections:
    - static ε ≥ 1 beyond RPA needs f_xc (not f_Hxc);
    - the 2510.25835 omission is CONFIRMED and also affects 𝒪₂, 𝒪₅ (×40 magnitude UNRESOLVED);
    - Im 𝒲̄₂ and 𝒲̄₅ vanish by PT in Si/Ge, so 2105.02233's explanation is REFUTED (numerical noise) and the package's "nonlocal-PP" reading is wrong;
    - the beyond-IP spin term is the triplet W-ladder (×1.3–2);
    - FW spin-curl coefficient 1/m_e;
    - q_c ≈ 2.2 keV;
    - the 2002.06937 factor is ~1.4, not (5/1.9)²;
    - G10: 14 real functions;
    - G5 kernel ~7 TB per q_r, so interpolation is mandatory.
  - CONFIRMED: the 2607.06005 dipole critique (and the Migdal ℓ=2 term also vanishes in Si/GaAs).
- REF-WP1-A (WP1 R×2 COMPLETE; ALL 14 R7 REPORTS IN): 1 FALLS, 13 w/ corr., 9 STAND.
  - FALLS: exciton thresholds as the WP3 boundary. Both referees: the true threshold minimises over Q; parabolic estimates Si ≈ 0.42 MeV, Ge ≈ 0.32 MeV (REF-B: Si 0.40–0.43, Ge 0.256 via Γ). The window must be recomputed from the ab initio E_min(q); for now it is a specification.
  - NEW: the allowed Umklapp G = (2̄00) in Si (non-symmorphic phases) at |q| = 2.63 keV, 0.594 MeV, not 0.708.
  - Catena responses: only 2 are independent with T + inversion (Im 𝒲̄₂ ≡ 0, 𝒲̄₅ ≡ 0), and both 2105.02233's and the package's explanations are refuted (agrees with B).
  - O₈ claim CONFIRMED; magnitude ~20–30 (⟨p_T²⟩), and the rate is still fixed by the full ε_ij tensor.
  - ε ≥ 1 beyond RPA needs f_xc (agrees with B); the Elliott weight in [E8] is 3× too large; 2101.08275 eq (24); EXCEED-DM axial vertex (B15)–(B18). The referee's scripts are in code/R7-REF-WP1-A/.

## R8 corrections (arriving)
- WP5-v3: 40 items, 27 applied (2 partly rebutted), 5 applied with a claim dropped, 7 stand, 1 n/a. 3 REBUTTALS to REF-A (§R8.2) go back to REF-A in the R8 verification. Refuted claims dropped; thresholds 352/399 eV [book; 395 was E_g = 0.74 eV] (soft); Born ≈ 15/35; (W1′), (W16) 2|ImΣ| = Γ_out + Γ_in; (W17) c^F; Migdal bookkeeping (1−P_Mig)S^GS with M+δM; GaAs worst case 0.3Γ/δ; code-pair conditions WP5-cp1–3. 55/55 checks. Interface flags IF-R8-1..10 (→ AUDIT-2).
- WP0-v3: 42 items, 32 applied, 8 STANDS, 1 REBUTTED (B-V6, back to REF-B in verification), 1 dropped (magnetic insulators out of Theorem D's scope).
  - (4.7) disagreement SETTLED for REF-A by two independent derivations. In the physical order (infinite sample first), 𝓜³ → −q²Z_κe²𝓃_κ[𝓃_e(R_κ) + 2𝓃_e]/(3m_eM_κ). The contact term is exact at all q (REF-B right on that); the remainder is O(q³) at T_d sites.
  - Breit term: δ_rel ≈ −0.23% Si, −0.73% Ge [E]. L17 fails for electron-only coupling with lattice relaxation. ×1.8 → ×1.35/×1.57.
  - 76/76 checks. CONVENTIONS amended (G1 rate contraction, G3 moments, G10–G12). Interface flags G1–G15 → AUDIT-2; G5 reopens F4 at the 10⁻⁴ level (WP2/WP3).
- WP4-v3: 47 rows, 43 applied, 5 REBUTTED (R-1..R-4, back to referees in verification), 6 dropped. The Dirac κ² finding is FIRM (exactly ε_bg² for any δε_D; corrected explanation: the missing 1/ε_bg² in 1708.08929 eq 3.14). Absorption is too large by ε_bg (§5.5). Disagreements settled (κ² explanation: REF-A; 2609.06423 propagator: REF-A; Mermin domain: REF-B). NEW [4.2′]: the BCS correction to Re ε is FIRST order, (Δ/qv_F)𝔰_BCS (≤16% in L at 5Δ, Al edge only). 34/34 checks. Flags I1–I17 → AUDIT-2.
- WP2-v3: 54 items, 26 applied, 26 STAND, 2 dropped (the 2205.02250 claim, refuted by both), 0 rebutted. (2.4) now has all inter-sublattice pairs; the BZ-average identity holds only for Bravais lattices and q ≫ max(n_ph, 2W)q_BZ. (5.2″): the κκ/eκ relation is qualified ((q a_1s)²/10) with the uniform 2𝓃_e term (1.2×10⁻⁴ Si), INDEPENDENTLY matching WP0-v3's settled (4.7), which closes the F4 reopening at the 10⁻⁴ level pending WP3. Eight A/B disagreements settled (B 4, A 1, both 1, wording 2). 31/31 checks. Flags IF-1..14 → AUDIT-2.
- WP1-v3: 51 items applied (7 rows involve dropped claims), 2 partly REBUTTED to REF-B (B-13: the Ge Γ 0.256 MeV is a flat-band floor, the parabolic Γ onset is ~3 MeV; B-9: 12/18 response functions, not 14). 49/49 checks.
  - [E13] threshold = min over q of q²/[2(q·v_max − E^ZP(q))]. Parabolic estimates (band masses UNVERIFIED, interim until ab initio E_min(q)): Si forbidden-class ZPL ≈ 0.42 MeV, Si allowed ≈ 0.54 MeV (via (2̄00) Umklapp), Ge L 0.32–0.36 MeV; floors 0.329 (Si) / 0.211 (Ge).
  - [E14] forbidden-ZPL/PAER ratio ~0.03–2 at the edge, 0.2–15 at +0.1 eV (order of magnitude).
  - **M1 window, revised:** Si: PAER leads for 0.338–~0.43 MeV, comparable 0.43–0.54, the allowed ZPL leads above. Ge: PAER-only ~0.21–0.32 MeV.
  - Nine disagreements settled (selection rules: REF-A; q_c = 2.24 keV: REF-B; ...). Flags IF-3,4,6,6b,10–17 → WP3, WP6, WP0, AUDIT-2.
- WP3-v3: 48 items, 26 applied, 21 STAND, 1 dropped (the 1608.01994 near-edge size), 1 partly REBUTTED (B-12(a), back to REF-B); the v2 "repair" of 2603.13052 is dropped. 105/105 checks.
  - LA/TA disagreement SETTLED with characters computed from the diamond geometry: on the Si [100] axis LA is forbidden and TA/TO/LO are allowed (REF-A on vertices). The TA minimum moves off-axis near |q| ≈ |K| (REF-B); on-axis iff γ_c > −|K_pk|/(2|q|).
  - Final p̄_on: Si edge (TA) 3, LA kink 4, TO/LO 3; (2̄00) class LO 4; Ge all 3. Envelope [0.4, 1.8]. δ₀ = 0.3 eV, Q_w = 0.33 Å⁻¹. J8 includes the uniform 2𝓃_e term (consistent with WP0-v3/WP2-v3, which closes F4).
  - M1 window [E]: Si strictly PAER-only 0.333–≈0.42 MeV (AUDIT-2 must reconcile the lower edge 0.333 vs 0.338: the acoustic Q*→0 infimum E_g is in the edge shell); Si with the forbidden ZPL open 0.42–0.54 (PAER leads to ≈0.43); above ≈0.54 the allowed ZPL leads; Ge PAER-only 0.212–≈0.32 MeV.
- WP6-v3: 49 rows, 29 applied, 17 STAND, 1 dropped ("η̃ unique"), 2 UNRESOLVED, 2 partial REBUTTALS (R-A1 → REF-A: the cubic bound-exciton edge exponent is 7/2+k_tail (9/2 for Si 1s); R-B1 → REF-B: supp Π_mom ⊆). 41/41 checks. General edge m_min = min_q q²/[2(q·v_max − E_th(q))]; 0.333/0.212 are floors. Si edge exponent 13/2+k_tail. M1 edge RECONCILED (IF6-11): the PAER edge is ≈0.333–0.337 MeV [E]. Window Si ≈0.333–0.42, Ge ≈0.213–0.32 MeV [E; ω_TA(Q*) from memory → OW6-7]. (P) is a hypothesis with sufficient conditions + an O(ω_Q/ε_eh) leakage + a library gate. Nuisance types fixed (M on contracted scalars/PSD geodesic; A on PSD increments; new tilted type T).
## R8 correction round COMPLETE (all 7 packages at v3). Next: R8 verification (the 14 original referees verify their items and adjudicate rebuttals) + AUDIT-2.

## R8 verification (arriving)
- VER-WP5-A: all 20 R7 items RESOLVED; all 3 rebuttals ACCEPTED (2209.04503 Z₁ → CONFIRMED). NEW: N1 (substantive) the forward-peaked-cross-section argument for L20 uses the wrong weight (keep the other half: separating collisions kills the cross term). Minor N2–N4: 7.2 eV onset circular (b_N); "u booked electronic" only for U in secondary collisions; P_Mig range (~5% at 10 keV). No [D]/LIMITS change; rung 4 met once N1 is fixed.
- VER-WP5-B: all 20 R7 items + 11 corrections RESOLVED; the vacuous checks are now real. NEW minor: N1 (§6.4(iii)/C19 wrong comparator: ω₀ × phonon heat), N2 (§1.5 re-applies the Si Γ/δ map to GaAs); cosmetic N3/N4. Accept for rung 4 after N1, N2.
- VER-WP2-A: all 30 RESOLVED, no new error (2 optional wording fixes). VER-WP2-B: all 24 RESOLVED, no new error (wording: the ≈0.16 estimate needs the farther-pair cancellation noted). → **WP2 PASSES verification (rung 4 met).** Open: WP3's evaluation of the Migdal part of 𝔨₃ against (5.2″) (WP3-v3 J8 includes the 2𝓃_e term; confirm in the WP3 verification).
- VER-WP3-B: all 24 RESOLVED; rebuttal B-12(a) ACCEPTED (γ_c > −|K_pk|/(2|q|) is general; 0.52–0.64|K_pk| is a harmless saddle band). REF-B concedes two of its own R7 points (0.14 meV shift; multiplicative [0.4, 1.8]). NEW minor: (1) the on/off-axis crossover assumes linear TA dispersion; dispersive criterion γ_ω > −(|K_pk|/2|q|)·v_g d_K/ω₀(d_K) moves it to ~0.85 keV, so "on-axis covers the low-mass end" is not established (exponents unchanged); (2) the ALDA cross term is k_xc δn_q δn_Q (no ½).
- VER-WP3-A: all 24 RESOLVED, no new error. LA/TA analysis confirmed (Si edge 3, LA kink 4; the (2̄00) class; Ge 3). The M1 boundary is reproduced (0.419–0.449 MeV), and the PAER edge 0.336–0.338 MeV (0.333 is the replica/bare-gap floor, not the free-pair edge). Minor flags: (2̄00) "LO 4" holds only if the LO minimum is on-axis; J8 and the ALDA source term are outside A's scope (REF-B covered the ALDA term). → **WP3 PASSES** once the B minor items (crossover dispersion, ALDA factor) are applied.
- VER-WP1-B: all 28 RESOLVED; all three rebuttals ACCEPTED (the Ge Γ onset ~3.1 MeV, so the Ge ZPL onset is L at 0.32–0.36 MeV; 12/18 response functions; 𝒲̄₅ vanishes only in achiral crystals). Concedes B-11 to REF-A ((2̄00) Umklapp allowed). NEW minor: N1 "allowed ZPL leads above 0.54 MeV" must be conditional on the unknown (2̄00) vertex (the reliably allowed class starts ~0.62 MeV); N2/N3 [E] tags; N4 cosmetic.
- VER-WP4-A: all items RESOLVED; the Dirac ε_bg²/ε_bg statements are correct and can go to LIMITS; R-1, R-2 ACCEPTED ([4.2′] verified by quadrature). NEW: N1 Theorem D-g (G5): the operator norm of H_off is extensive, so the bound as written is empty; restrict it to few-quasiparticle states, size ~√(Γ·W_c), not Γ. N2: [4.2′] at the Al edge has a KK cutoff ~13Δ, so quote 8–16% [E]. N3 wording.
- VER-WP4-B: all 20 RESOLVED; R-2, R-3, R-4 ACCEPTED. NEW: N1 [4.2′] expansion fails near threshold (|δL/L| ≈ 1.42/0.88/0.53 at y = 2.2/2.5/3), so state its validity (y ≳ 4–5) and fix I12; "≤16% at 5Δ" is correct. N2 = A's N1 (G5) (both referees agree). N3 label ×640 as the isotropised model.
- R8 verification so far: WP2 PASS; WP3, WP5 PASS after minor fixes; WP4 needs (G5) restated and the [4.2′] validity domain; WP1 needs minor N1–N3; WP0 and WP6 pending, AUDIT-2 pending.
- VER-WP0-B: all items RESOLVED except two residuals; rebuttal B-V6 ACCEPTED (three routes agree: the physical coefficient is [𝓃_e(R)+2𝓃_e]/3 with an O(q³) remainder at T_d sites). NEW N1 (minor, ~10⁻⁴): that coefficient needs q ≪ G_min ≈ 2.3 keV (Si), not q ≪ 1/a_core; only the contact term holds over the whole DM q range. N2 (not resolved): the (6.1) remainder order is semiclassical only; tag [C] for low-lying vibrational states.
- VER-WP0-A: all 22 RESOLVED; orbit–orbit rebuttal ACCEPTED (transverse kernel, so E′_ee; ≈0.27 δ_mv holds); (4.7) confirmed for A by two routes. NEW minor: N1 H1 smearing must use the nuclear CHARGE form factor, not F^M_κ; N2 the Si L17 counterexample figure is not derived (keep GaAs-like only); N3 §12 stale open/closed lines. → **WP0 PASSES** after minor fixes (A N1–N3; B N1 range q ≪ G_min, N2 [C] tag).
- VER-WP1-A: all 23 RESOLVED; [E13], the (2̄00) treatment and the M1 window reproduced. NEW wording N1 (= WP1-B N1): hedge "allowed ZPL leads above 0.54" (the (2̄00) vertex may be small; near 0.54 the region is a single point); N2 the Si second-class bright state is 2p (~0.001 MeV shift). → **WP1 PASSES** after minor fixes.
- VER-WP6-A: all 27 RESOLVED (2 citations UNRESOLVED, acceptable); R-A1 ACCEPTED (cubic bound-line edge 7/2+k_tail, 9/2 with an axis vertex zero). Edges 0.337 (continuum) / 0.333 MeV (replica) confirmed. NEW: N1 tilted type T must use ψ = ln(1 + Δ′_A/S_c) (otherwise the template is not reproduced and the tails blow up); N2 existence condition (endpoint variance, λ₂ tail integrability); N3–N5 minor/wording. Recommendation: L24, G8 REFEREED; G4 after N1, N2.
- VER-WP6-B: all 22 RESOLVED; R-B1 ACCEPTED. NEW-1 (minor-substantive): the Si exciton-replica edge (E_x + ω_TA ≈ 1.1688 eV → 0.3327 MeV) is at/below the 0.333 "floor", so the floor of the total S̄ is 0.329 MeV; CONTROLS C5 applies only to the continuum; Ge likewise. NEW-2 = A's N2 (tilted-type existence: upper variance bound); NEW-3 μ̂ unique only on bins with N_i > 0; NEW-4 cosmetic.
## R8 verification COMPLETE (14/14). Every package resolves all R7 items, and every rebuttal was ACCEPTED (13/13). Remaining: one consolidated clean-up (minor/new items listed per package above), pending AUDIT-2.
## R8 AUDIT-2 (2026-10-31): 3 BLOCKING + 33 minor.
- B1: WP0-v3 (8.1)–(8.2) "M PSD for all θ", "positivity automatic", and the old [0.5, 1.2]; WP6/WP3 flags not applied in WP0.
- B2: WP0-v3 §9.2(iii) beyond-RPA condition must be (−R⁰)⁻¹ + f_xc > 0 (WP1 IF-12).
- B3: Migdal/multiphonon bookkeeping in WP0 §6.2(iii) rule (a) and WP3 J3/N1 must use (1 − P_Mig)S^GS with M + δM (as WP2/WP5).
- CLOSED: 𝔨₃/F4 (sympy: WP0 (4.7′) ≡ WP2 (5.2″) ≡ WP3 J8). M1 window reconciled (stale numbers m1–m3). LIMITS table corrected in AUDIT-2 §2; coordinator-file lines in §6.
## R9 consolidated clean-up launched: each package's revision agent applies VER-A/B new items + AUDIT-2 items in place; the coordinator applies AUDIT-2 §2/§6.
- R9 coordinator files applied (LIMITS v3 status table, now REFEREED (R7); CONVENTIONS, CONTROLS C5/C7/C8, NOTATION rows added R9; SOTA annotations). Coordinator fix: NOTATION rows y_φ and 𝒟^γ corrected (𝒟^γ is the in-medium photon propagator; the DM-side tensor is 𝔇). WP1, WP2, WP5 R9 clean-ups done.
- WP3, WP6 R9 clean-ups done (WP3 114/114; WP6 42/42). CONTROLS C5 scope extended per IF6-18.
- WP0 R9 clean-up done (B1 positivity statements per WP6-v3 and [0.4, 1.8]; B2 (−R⁰)⁻¹ + f_xc > 0; B3 (1−P_Mig)S^GS with M+δM; H1 charge form factor; (4.7′) for q ≪ G_min plus exact (4.7″); (6.1) [C] tag). 82/82 checks. Flags m25 and m31 already applied in CONVENTIONS/NOTATION. ALL THREE AUDIT-2 BLOCKING DEFECTS RESOLVED.
- WP4 R9 clean-up done: (G5)/[8.1′] restated on few-quasiparticle states (𝔥_off ~ √(ΓW_c/2π) [E]; sufficient but loose; (c) [C]). [4.2′] valid only while 2(Δ/qv_F)𝔰_BCS ≪ 1; uncontrolled for y ≲ 3.5 at the Al edge (RG9); 8–16% [E] at y = 5; the term lowers L. Magnetic insulators are an open item (OW4-4 = OW0-17). 36/36 checks.

## FRAMEWORK REVIEW COMPLETE (2026-11-01)
- All seven packages (returns/R8/WP0-v3 … WP6-v3) have passed R7 hostile review (R×2), the R8 correction round, R8 verification (14/14, all 13 rebuttals accepted), AUDIT-2 (3 blocking defects resolved) and the R9 clean-up.
- Coordinator rerun of the checks: WP0 82/82, WP1 49/49, WP2 31/31, WP3 114/114, WP4 36/36, WP5 55/55, WP6 42/42 (409 total).
- LIMITS.md v3 status table: entries REFEREED (R7) with the R8/R9 corrections applied.
- Next (user-ordered queue): WP7 follow-up package (B-class channels, reachable D extensions, low-T defect kinetics, WP7-E energy-partition reconciliation) → WP8 figures of merit and material selection (incl. WP8-R go/no-go) → book writing when authorised.

## R10 WP7
- WP7-T returned (CLAIMED, pending R×2). Defects are a GS-sector configuration family (new K = def). DM vertex = core + elastic-dipole. TLS S flat in ω (a-SiO2 ~1e-3 /(kg·day·meV) at 1 MeV, σ̄_e = 1e-38, est.); sensor films matter as absorbers and delayed-release sources. Limits: dielectric loss, Jäckle, Korringa, ohmic, Vineyard/Wigner, STM heat release. NEW: dark-photon absorption on TLS = κ² tanδ/ε_r. Source factor-2 discrepancies in 1705.01108 eq 20 and 2103.06977 eq 2 (R×2 to verify against FT). Crowdion mass M_cr = 2μa·m/π² (W: coherent 1D quasiparticles at mK, est.). mK hops are T-independent or power-law, never Arrhenius. Release laws 1/t (broad ensembles) and t^{−3/2} (correlated Frenkel pairs). Hand-over p_st, 𝒦^{rel} → WP7-E. Main gap G-T1 (no ab initio α_ohm). Proposed LIMITS L25–L32 (provisional numbering).
- WP7-E launched.
- WP7-D returned (CLAIMED).
  - Coherent classical-field regime: no new response object (the off-diagonal retarded R at (mv, m); finite-body response below the coherence length). Mean power = the halo-averaged golden rule for any integration time; coherence changes only the statistics (Var N = N̄ + N̄²/𝒩_c); SNR scaling t^{−1/2} → (t t_coh)^{−1/4}. Recovers CASPEr, BAR/hBAR, resonator and magnetoelectric formulas; the CASPEr eq (1) off-resonance envelope is flagged (resonance printed half as wide).
  - Fermionic absorption: a DM-side tensor 𝔇^F plus the existing S on ω = m_χ − q (recovers 1905.12635, 2011.01940; a current-conservation correction for the vector operator).
  - Two-insertion processes classified by correlator order: pair/Thomson Compton use 2-point functions; resonant parts 4-point; interference 3-point.
  - Tracks hand off via the Lindhard/Bethe stopping power (the m → ∞ limit); tracks themselves are out of scope (non-perturbative). I2 has no target vertex.
  - New basis items 𝔘_C (Coulomb-energy row) and 𝔇^F; a geom metadata tag. 34/34 checks.
- WP7-B2 returned (CLAIMED).
  - A4 matches 2308.06314 term by term; the coupling-to-mass rule holds for any basis. Correction: their electron-scalar coupling should be Z − Z* (GaAs rate ×0.47).
  - One random-coupling result covers S5, A7 and L10: reproduces 2411.10542 eq 31, gives the glass dark-photon rate via ε(ω), and adds a NEW channel (isotope-disorder broadband B−L absorption in Si). Disordered S_NN closes WP2-v3 gap 6 at formula level.
  - §10(iii): 2512.16451 eq 12 recovered, but its Born approximation FAILS at the claimed MICROSCOPE reach (optical potential 1.9× the kinetic energy; needs σ ≪ 1.2×10⁻³⁸ cm²). R×2 must check.
  - L11 He: self-consistent harmonic S replaces quasi-harmonic.
  - S2: all small-k transverse weight in one Larmor line (exact, isotropic exchange); Kittel/Polder factor.
  - S6: unpolarised neutrons miss the longitudinal spin response needed for absorption and pseudoscalar couplings.
  - L9/S8: phonon magnetisation creates phonons only in pairs; 2301.07617's κ is an estimate.
  - X10: an exact identity recovers 2312.10566 eq 17.
  - D2/D5 seeding: sub-GeV recoils make vacancies, not the F₂⁰/F₃⁺ aggregates read out by 2503.20732.
  - Misprints claimed: 2308.06314 eq 48, 2601.01043 eq 12 (+ n_r/|ε|²).
  - 31/31 checks.
- WP7-B1 returned (CLAIMED): all 11 rows covered.
  - Frenkel: the incoherent molecular sum is exact in bins wider than the Davydov splitting.
  - Luttinger: the f-sum forces g·v = v_F (reproduces 2607.15338 exactly).
  - Demon modes carry only (q²/(q²+k_TF²))² of the f-sum.
  - Heterostructures: 2110.01587 eq 16 is exact at any filling.
  - Exothermic shell rate halo-independent to O(v²/v*²).
  - SC absorption: 1604.06800 eq 17 = x·𝔤_I (Landen), so phonon-assisted absorption carries case-I coherence and Mattis–Bardeen applies only to disorder-assisted absorption → IF-B1-1 to WP4 ([D, sketch]).
  - Source errors claimed: 2212.04504 eq 12 (3q̃ → 3q̃², missing Lyman lines); 2401.11971 eq 5 (missing (1 − ω²/Q²)²); 2208.05967 (dielectric confinement ×~6, so conservative); 2607.09352 (inconsistent screening levels); 1706.02487 typo.
  - 9 exact gaps. 28/28 checks.
- R10 R×2 referees launched for WP7-B1, B2, D, T (WP7-E after it returns).
- WP7-E returned (CLAIMED).
  - Balance law (E1), exact event by event at every t.
  - Two-stage split (the WP5 cascade before the prompt time, the detector stage after), so no double counting.
  - E_d never in the ledger (it sets only the displacement probability; needs a WP7-T release sum rule, IF-E2).
  - Yield models act only on the electronic share (stored energy is entirely nuclear in Si/Ge; Lindhard ν = nuclear share).
  - Trapped pairs: the heat deficit is E_g − trap depths, so WP5 (W11) overstates it.
  - Measured-charge compound law F_meas = ⟨𝔵⟩F_eh + Var𝔵/⟨𝔵⟩ (Hecht, CCD thinning as limits).
  - LEE: single-defect releases (~2.7 eV collected) and non-interacting TLS give heat deficit / sub-threshold power, not 10–100 eV events, which need collective stress release (consistent with 2208.02790, 2202.05097) [E].
  - Literature limits with their implicit defect assumptions (Lindhard U = 0; TRIM implies a fixed stored energy per defect, not E_d).
  - WP5-v3 amendment A-1..A-11; 10 nuisances; 8 flags; proposed L33–L38. 35/35 checks.

## R11 referee reports (WP7)
- REF-WP7-B2-B: 3 STAND, 9 w/ corr., 1 FALLS.
  - FALLS: C^IR ∝ ω² below the boson peak (prior art: C = A + Bω², Taraskin et al.).
  - CONFIRMED vs FT: 2308.06314 eq 48, 2601.01043 eq 12 (+ n_r/|ε|²), 2512.16451 Born failure at its claimed reach (V_opt/E_kin = 1.86), 1705.03016 eq 6.
  - Overstated "defects": the 2308.06314 rigid-ion vertex is in their own footnote; 2301.07617 already calls κ an estimate; the angular-momentum point is known (Zhang–Niu).
  - Corrections: SMM S⁺ branch / avalanche line D(2S−1) − ω_Z; the Ni²⁺ factor ~0.83; X10 screening 1 + (3/2)ω_p²/ω²; isotope-disorder B−L novelty UNRESOLVED (compare with the EM-like part; mass-weighted σ_γ² = 1.88×10⁻⁴); notation clashes ω_L/m_s/λ; B2-L4 validity wording.
- REF-WP7-T-B: core stands (two-state reduction, STM response, Jäckle/Black/NIBA, heat release; L26–L30 quotes OK). Both source claims CONFIRMED (1705.01108 eq 20 phonon ½; 2103.06977 eq 2 vs 7, a factor 4 in the rate). Corrections: the DM-on-TLS rate misses (1 + m_χ/m_e)² ≈ 8.7, so ~10⁻² /(kg·day·meV), outside its own static window, and screening is omitted. FALLS: pole rule §1.4(iii) (double pole, so the Hadamard finite part is needed). Novelty REFUTED: the crowdion mass = E₀/c_s², the textbook Frenkel–Kontorova kink mass. λ convention 2× Phillips/Jäckle, so the "frozen" verdicts for Si Frenkel pairs and Al interstitials are not robust (λ ≈ 25–37, energy-gap law). tanδ misquote (AlOx, not a-SiO2). W crowdion band 0.024 meV; coherence/ballistic → [C]. 5 vacuous checks.
- REF-WP7-D-A: 0 FALL, 10 STAND, 8 w/ corr.
  - Corrections:
    - mean power = golden rule only for t_int ≫ min(t_coh, 1/Γ_T), not for any t_int;
    - pair-absorption operator must be i(S†∂↔S) (velocity-dependent DM tensor) plus an identical-boson ½;
    - the 2011.01940 "exact" match has a factor-2 spin-convention issue;
    - DM radiative decay is magnetic dipole, so ∝ n_r³;
    - SNR crossover depends on a box line; random-amplitude penalty 3–10 (1905.13650); spin-noise FDT needs a spin temperature (prepolarised);
    - V in (D.7); citation/tag fixes.
  - CONFIRMED vs FT: the CASPEr eq 1 envelope half-width, 2507.14287 species density, 2501.05504 Q_DM peak-only (refinement). 2011.01940 eq 9 paper error UNRESOLVED.
  - LIMITS L-D3/4/5/8/9/12 need correction; read 2308.00309 before L-D8.
- REF-WP7-B2-A (WP7-B2 R×2 COMPLETE; agrees with B on all shared items): 10 STAND, 10 w/ corr., 2 FALL.
  - FALLS: (1) "GaAs ×0.47": with photon mixing only the LO resonance survives, with vertex Z − Z*/ε_∞; Ga and As nearly cancel, so ~0.1 and O(1)-sensitive. (2) C^IR ∝ ω² (= REF-B).
  - CONFIRMED vs FT: 2308.06314 eq 48 (a factor ~3 still remains vs the printed 10⁻⁹), 2601.01043 eq 12 + n_r/|ε|², 2512.16451 Born failure (1.85; R×2 CONFIRMED), 1705.03016 Δp, the 2301.07617 selection rule (κ point not a finding).
  - Isotope-disorder novelty UNRESOLVED (1.88×10⁻⁴).
  - Corrections: Ni²⁺ factor 0.83; magnetic-dipole DM does make single phonons via the transverse ionic current; SMM S⁺ branch; X10 screening ~1.2×10⁻³ at 1 keV; ω_Lar/m_s clashes; spin-ordered targets are not in the Theorem D GS sector (excluded); τ strings need T.
- REF-WP7-D-B (WP7-D R×2 COMPLETE): 0 FALL, 6 STAND, 12 w/ corr.
  - CONFIRMED: CASPEr eq 1 half-width; 2011.01940 eq 9 algebra (but the size statement is wrong: Xe K shell −11% typical, −34% to −41% at 56.5 keV); 2501.05504 Q_DM effective (max 1.3×10⁶ SHM); 2507.14287 ξ; 2109.08168 to O(m_V/m_e).
  - REFUTED: "1/ε₀ is the slab case" exclusivity. UNRESOLVED: CASPEr on-resonance agreement (2× under the source's definition); 2109.08168 O(x²) relativistic. [R16 (CW3-errata §2.2 item 21): 2109.08168 Eq. (3) (= HTML v2 Eq. (18) = PDF Eq. (17)): REFUTED by (m_a+2m_e)/(m_a+m_e) (CW3; VER-CW3 CONFIRMED); PDF Eq. (16) (dR/dcosθ) inconsistent with its (15) (4m_e²(ω−ω′)² vs 4m_e²ω²); 2109.08168 Eq. (2) is the exact tree-level Dirac result; 1306.6089 Eq. (1) amplitude: CONFIRMED with the per-level convention; source gloss misstated ×2; 2501.05504 Eq. (7): CONFIRMED (32 derived; m_V² numerator is the damped-oscillator form); 2011.01940 Eq. (9): not current-conserving (CONFIRMED); paper-error verdict = exact gap]
  - Mandatory corrections: k sign in (D.1); R_{I⁺I⁻} label/sign; the (3/2)t_coh crossover is an artefact (both referees); the near-T_CM multiferroic regime → exact remaining gap; I2 n_r³ (both referees); undefined cited equations; X/ε notation collisions.
- REF-WP7-B1-A: 8 STAND, 7 w/ corr., 0 FALL.
  - CONFIRMED vs FT: 2212.04504 eq 12 (3q̃²), 2401.11971 eq 5, 2208.05967 local-field factor, 1706.02487 typo, the 2607.09352 mixed response; 2110.01587 eq 16 exact at any filling. REFUTED: "2212.04504 omits Lyman lines" (their App. VII.6 includes them).
  - Corrections:
    - A6 screening applied twice;
    - I5: the transverse term is O(v²ω²/q²), up to ~8%, and already in 2608.20715 plus the classical Fermi formula, so it is NOT new;
    - A2: the case-I elliptic form and the Mattis–Bardeen difference are Allen PRB 3, 305 (1971);
    - E10: the bulk-input quote is wrong, and the 2208.05967 prefactor match is UNRESOLVED (source dimensionally inconsistent);
    - E8: overclaim; 2607.15338 is single-channel (CNT rate ×4);
    - E5 "exactly" qualifier; LB1-8 is a sketch, not DERIVED.
  - **CROSS-PACKAGE: the WP4-v3 𝔤_I "new closed form" novelty is REFUTED (Allen 1971); credit owed in WP4.**
- REF-WP7-T-A (WP7-T R×2 COMPLETE; agrees with B on every shared item): 0 FALL, 3 STAND, 10 w/ corr.; the crowdion-mass novelty REFUTED (Frenkel–Kontorova; Braun–Kivshar). Both source errors CONFIRMED (G-T5 is wrong: 2103.06977 eqs 4, 12, 15 settle it). Misquote confirmed (AlOx; 4.2 K a-Si:H 2.5×10⁻⁵). Hadamard finite part; the 1 MeV rate is outside validity (core term dominates); λ window and energy-gap law; insufficient eV Frenkel spec; W band ~0.03 meV and bulk W normal at mK. Minor: τ slot, double tanh, α_ohm = 4K, ω₀ clash. L25–L30 DERIVED, L31–L32 ✎; DM–TLS novelty UNRESOLVED.
- REF-WP7-B1-B (WP7-B1 R×2 COMPLETE; agrees with A): 8 STAND, 8 w/ corr. Novelty FALLS for g·v = v_F (textbook), the neutral demon (Pines 1956), the binned Frenkel sum (oscillator sum rule), the SC E-function form (Allen 1971). CONFIRMED source errors as A, plus 2401.11971 own eqs S.9–S.12. REFUTED Lyman-lines omission. 2208.05967 ×6 UNRESOLVED (evaluated outside the source's range; factor <1 in the far UV). NEW: 2607.15338 single-channel, so the CNT rate is 4× too low. Corrections: ε̃ clash, Landau damping, band-projected sum rule; C7/C12c not independent.
- REF-WP7-E-B: 0 FALL, 2 STAND, 13 w/ corr.
  - REFUTED reading: 1803.02903 does NOT assume equal NR/ER heat; it fits 95.2% (a ~5% NR phonon deficit), and 1805.09942 attributes ~6% to defects. Affects §4(a), result 13, L37/L38.
  - CONFIRMED: 2004.10709 App. A thinned Fano (upper bound); L35 stands.
  - Corrections:
    - C10b ħc ×100 (conclusion holds);
    - checks don't test completeness, and the balance law is missing zero-point, exciton and space-charge energy;
    - trapped-charge energy referenced to the contacts' Fermi level;
    - the two-stage split needs a summary-vector sufficiency assumption;
    - "defect energy only nuclear" ignores carrier-driven reactions;
    - F_meas depth averaging; erfc 1D only;
    - delayed-event threshold inconsistency, pocket recrystallisation, and selective quotes (EDELWEISS stress test; 2208.02790 single exponential fails);
    - WP5 amendment items A-1, A-4, A-8, A-10 flawed; four WP5 sites unamended; nuisance priors; LIMITS rows lack validity and leading correction.
- REF-WP7-E-A (WP7-E R×2 COMPLETE; agrees with B): 0 FALL, 3 STAND. μ must be the electrode Fermi level (the singly trapped carrier stores μ_F − E_v − E^tr); missing exciton/EHD/pair Coulomb reservoirs; tautological checks; ħc ×100; the TLS stored-energy total is per unit λ (×6.8 inconsistency); E_st ⊂ E_nuc only for creation; (E8) needs ΔE_trap and the ER-calibration ratio; F_meas position averaging; the two-stage summary needs the phonon spectrum, class c and r_ev; selective LEE quotes; NRT 0.8 mislabelled; WP5 amendment A-1/A-2/A-5/A-7/A-10/A-11 flawed, plus four missing.
## R11 COMPLETE (10/10). R12 WP7 correction round launched (authors produce *-v2 in returns/R12/), plus the WP4-v3 Allen-1971 credit fix.
- WP4-v3 erratum applied: the 𝔤_I closed form is credited to Allen PRB 3, 305 (1971); novelty dropped; OW4-3 closed. 36/36 checks.
- WP7-D-v2 (R12): every verdict applied; 1 claim dropped (the slab claim; replaced by orientation factors 1 / 3ε₀/(ε₀+2) / ε₀). Coherent mean holds for t_int ≫ min(t_coh, 1/Γ_T) (Fejér otherwise); k = −m_φv; R_{I⁺I⁺} with ⟨I^z⟩ < 0; spin temperature; SNR crossover O(1)·t_coh; penalty 3–10 not double-applied; 1306.6089 amplitude ×2 UNRESOLVED; near-T_CM → gap. 2011.01940 spin factor closed by derivation; sizes Xe K −11% / −34–41%, valence +0.7–2%; paper error UNRESOLVED; 2308.00309 read (light mediator F.7). Pair absorption i(S†∂↔S) + ½; I2 n_r³. Dark Compton now matches 2109.08168 through O(x²), first difference at O(x³) (cause UNRESOLVED). 49/49 checks.
- WP7-B1-v2 (R12): all items applied; novelty withdrawn with prior art credited (Davydov sum rule, v_J = v_F, Pines 1956, Allen 1971, Fermi 1940 + 2608.20715); A6 screening once; the Lyman claim withdrawn; I5 re-sized (impact on 2401.11971 limits UNRESOLVED); CNT ×4 added; E10 ×6 withdrawn (UNRESOLVED); LB1-8 SKETCH; a CONVENTIONS row for relativistic F_DM proposed. 30/30 checks.
- WP7-B2-v2 (R12): both FALLS dropped (GaAs: LO residue ≈0.11, near-cancellation, so order of magnitude only; C^IR = A + Bω²); defect claims retracted except the non-exact selection rule. Isotope B−L: novelty UNRESOLVED; ~10²–10³ above the EM-like part inside the phonon band, but resting on an UNVERIFIED two-phonon value (must be checked against FT in verification). Physics/notation fixes applied. 39/39 checks.
- WP7-T-v2 (R12): Hadamard finite-part pole rule (1/η and Fano δ → cascade; fp/PV → defect response). Screening REBUTTED (the vertex is already DFPT-screened, so ε_e⁻¹ again would double-screen) → back to the referees. Host-term sign fixed (+2w q̂·γ·q̂). DM–TLS a-SiO2 rate ≈2.4×10⁻² /(kg·day·meV) at 1 MeV (est. ×3), ω ≲ 0.1 meV. Literature fixes; crowdion mass credited (FK); W band 0.024 meV (Mathieu); coherence [C]; 1D t^{−3/2} withdrawn. λ in the Phillips/Jäckle convention (H in Nb 4.1, Si 27.5–37, Al 25); energy-gap/Marcus window; "frozen" verdicts withdrawn (open). NEW Theorem T-1: the release-path sum rule follows from the WP5 master equation, closing IF-E2. 51/51 checks.
- WP7-E-v2 (R12): all verdicts accepted; two claims withdrawn (1803.02903 unit-quenching reading; the "≲1 eV" threshold). E_st data constraints: Si 95.2% gives d_NR − 0.64 d_ER = 0.048; Ge 6.08%. If all of it is stored, p_surv E_st,1/E_d ≤ 0.18 (Si), ≤ 0.19 (Ge). μ_F reference; added reservoirs; completeness check (field energy = Green's pair sum; battery work = Δfield + heat). Field 1.2×10⁴ V/cm; TLS stored ≈1.4×10⁷ eV total. WP5 amendment A-1..A-16. 36/36 checks. Sum rule (E6) flagged to WP7-T-v2, which now proves it (Theorem T-1): verification must confirm consistency.
## R12 COMPLETE (5/5 v2). R12 verification launched (the original R11 referees verify their items).

## R12 verification (WP7)
- VER-WP7-D-B: all items RESOLVED; dark-Compton O(x²) agreement confirmed. NEW minor: (F.7) needs m_φ > m_χ (otherwise there is an on-shell pole and DM → ν̃φ decay); the N13 label is cosmetic. Does not block REFEREED.
- VER-WP7-B1-A: all RESOLVED, no new substantive error; rebuilt checks are independent; 3 optional wording fixes (n_D/n_c ≈ 0.3–0.6; ω/Q → v_χ; Landau full width).
- VER-WP7-B2-B: all RESOLVED (LO residue, GaAs ≈0.11 with 46% sensitivity, isotope formula, SMM S⁺, MD single-phonon current re-derived). Minor: τ label K=1ph-coh for the elastic term; unexplained nB=-; docstring count. Caveat: the isotope-vs-EM 10²–10³ remains an estimate on an unverified absorption value (open gap).
- VER-WP7-D-A (WP7-D verification COMPLETE): all RESOLVED; dark-Compton O(x²) CONFIRMED independently (diff at x³: −35/8 vs −15/4); L-D10 tag should be 'observed', not derived. Minor: E1 joined quotation; E2 the 2011.01940 ratios are single-point values (near threshold 0.981 at 100 keV, 0.923 at 200 keV), so label them.
- VER-WP7-B1-B (WP7-B1 verification COMPLETE): all 17+6 RESOLVED, no new errors; LB1-1..13 can go to LIMITS with the §17 statuses. Retracts its own R11 filling-mapping request. Caveat: the 2208.05967 Ref. [139] ε provenance is unverified (already UNRESOLVED).
- VER-WP7-T-B: all RESOLVED; the screening rebuttal ACCEPTED (C-8 withdrawn). Theorem T-1 STANDS w/ corr. (needs ΣN_i = 1; rename 'frozen' at finite t_obs). DM–TLS 2.4×10⁻² confirmed (host 9.6×10⁻³, R_core 1.59; the incoherent sum is exact in the static window, so the interference-sign error item does not apply). Minor: C5a/b labels; Δ̃₀ > γ₀/2; C14c leftover; §2.4 core caveats.
- VER-WP7-E-B: most items RESOLVED; 5 new errors.
  - N1 (substantive): the deficit includes the absolute sensor loss (70–90%), so the first-order (E8), (E13) and A-4 fail. Use a multiplicative collection efficiency; the bounds survive with Δϵ ≥ 0 stated.
  - N2: bounds at the limit values: 0.21 (Si) / 0.20 (Ge), p_surv ≲ 0.47 / 0.66.
  - N3: a bound exciton's E_g is in no reservoir.
  - N4: 1803.02903's collection efficiency is a field ratio, so it cannot set θ_tr.
  - N5: A-10 E_x sign plus missing terms.
- VER-WP7-E-A: (E6) ≡ T-1 in form (normalise by ⟨N_hop⟩; (E5) as a mean; T-1 for time-dependent stimulated rates). NEW inconsistency: ΔZPE in E_st vs configurational energies in T-1 / WP5 (W12). COORDINATOR DECISION: adopt the configurational convention in all three packages; ΔZPE enters the phonon reservoir ℋ_ph as an explicit correction. Also the A-1 exciton E_g and per-carrier deposits; A-10; the §3.2 (1−κ)D_ER term and 95% C.L. bounds; the θ_tr source; the θ_tr^pr tilt; A-12 bias work before t_pr; the exciton/EHD kinetics spec.
- → WP7-E needs a v3 fix round (substantive) plus re-verification by both referees.
- VER-WP7-T-A (WP7-T verification COMPLETE): all RESOLVED; screening rebuttal ACCEPTED (condition: δρ_κ is the full finite-q DFPT response incl. G = 0). T-1 STANDS w/ corr. (probability conservation; energy convention). Minor N1–N5. → WP7-T in-place clean-up sent (with the coordinator energy convention).
- VER-WP7-B2-A (WP7-B2 verification COMPLETE): all RESOLVED. Two-phonon value CONFIRMED from FT (Deinzer & Strauch PRB 69 045205, Fig. 3). NEW ERROR: the comparison paired the 76 meV absorption value with the 50 meV DOS; redone at 50 meV the ratio is ~6×10³ at 293 K (larger at mK), so the conclusion is stronger. → WP7-B2 in-place clean-up sent.
## R12 verification COMPLETE (10/10). Remaining: WP7-E v3 (+ re-verification), WP7-T and WP7-B2 clean-ups.
- WP7-B2 clean-up done: the isotope/EM ratio is ≈6.3×10³ at 293 K at 50 meV (Deinzer & Strauch 2004 Fig. 3), larger at mK; τ K=el (IF-B2-13); 39/39 checks. WP7-B2 COMPLETE.
- WP7-T clean-up done: T-1 conditions (iv) ΣN_i = 1 and (v) configurational energies with ΔZPE in ℋ_ph; time-dependent rates; ⟨N_hop⟩; E_st^{unrel}(t_obs); screening scope. With a consistent halo, the a-SiO2 DM–TLS rate is ≈3.7×10⁻² /(kg·day·meV) at 1 MeV (est. ×3). 51/51 checks. WP7-T COMPLETE.
- WP7-E-v3: multiplicative collection (absolute sensor loss cancels in NR/ER ratios); E_st bounds with Δϵ ≥ 0, r ≥ 1, X_NR ≥ κX_ER. NEW: r = 1.14 alone (no stored energy) reproduces the Si 0.952. 95% bounds 0.21/0.20 (p_surv ≲ 0.47/0.66). Exciton reservoir E_X; (W14) fixed; 1803.02903 used as a one-sided constraint; θ_tr^pr tilt; bias work before t_pr 4×10⁻⁴–0.25 eV/carrier; (E6) identity under T-1; configurational ZPE convention. 47/47 checks. → re-verification by both WP7-E referees.
- VER2-WP7-E-A: all RESOLVED; (E6) consistent with T-1. Minor open: cite T-1 condition (iv); rename E_st^{frz} → E_st^{unrel}; ΔZPE (~0.1 eV/defect, ~1% of E_st) missing from the pre-sensor deficit D′ in (E7), (E8), (E13), A-4, A-9; A-1 wording (a captured edge carrier counted twice). No bound shifts more than ~1%.
- VER2-WP7-E-B: N1–N5 RESOLVED; multiplicative collection correct. Minor: the bounds need the stated condition E_st/ω ≤ 1 − y; r = 1.144 confirmed; tag g = 4/3.82 as sourced (1803.02903); the y variation gives 0.947–0.955, so the data cannot distinguish r-only from stored energy (state this). NEW minor M1: ΔZPE missing from D′ in (E7), (E8), (E13), A-4 (ledger off by ~10⁻³ of ω). → WP7-E in-place clean-up (both referees' minors) sent.
- WP7-E clean-up done (in place, v3): T-1 (i)–(v) cited, incl. (iv) ΣN_i = 1 (single-seed chain; bimolecular/inter-seed reactions lie outside per-seed (E6)); E_st^{unrel} rename; ΔZPE in D′ (bounds ⟨E_st⟩/E_R 0.056 Si / 0.065 Ge; p_surv ≲ 0.48/0.67; ≤1% shift [E]); A-1 once-per-carrier deposit; (B-d) E_st/ω ≤ 1 − y stated (C7g exact relation); g = 4/3.82 [FT, 1803.02903]; r-only vs stored-energy degeneracy stated (η₀ = 0.947–0.955 for y = 0.22–0.35). 50/50 checks. WP7-E COMPLETE.
## WP7 COMPLETE (B1, B2, D, T, E all REFEREED).
## PAUSED 2026-11-01 (user: token limit). R13 briefs written (briefs/R13: WP5-ERR, WP8-F, WP8-U, WP8-R); the launched agents were stopped before producing returns (partial scratch removed). RESUME: (1) confirm the WP7 LIMITS/NOTATION/FRAMEWORK merge landed; (2) launch WP5-ERR, WP8-U, WP8-R, then WP8-F; (3) WP8-S synthesis queued.
- WP7 merge (WP7-B1, B2, D, T; WP7-E excluded): LIMITS "WP7 (R12, REFEREED)" (43 rows), NOTATION "Rows added WP7", FRAMEWORK status. Catalog coverage re-classified (table returns/R6/AUDIT.md §8, not edited; counts last stated above at R6 as A 45 · B 25 · C 11 · D 10): B → A for all 25 B rows (WP7-B1: E5, E8, E9, E10, E12, X6, X8, A2, A6, I3, I5; WP7-B2: A4, S5, A7, L10, §10(iii), L11, S2, S6, L9, S8, X10, §10(iv), D2, D5); D → A for S4, S9, A9, §10(ii) (WP7-D §1), A10 (§2), A11, §11.9 (§3); D → C for D3, D4, I2 (WP7-D §4: out of scope by design, with the stopping-power and radiative-decay interfaces). Counts (91 rows): A 77 · B 0 · C 14 · D 0. Caveats: X6(b) (LB1-8) and S9 (L-D6) are [D, sketch]; LB1-5 prefactor UNRESOLVED.
- WP7 merge (B1, B2, D, T) into LIMITS (43 rows, section "WP7 (R12, REFEREED)"), NOTATION ("Rows added WP7", 23 clashes resolved), FRAMEWORK. Open for RESUME: merge WP7-E rows (L33–L38) + its symbols (incl. 𝔠 rename); coordinator decisions pending (B1/D label numbering, merged geom set, new τ values K=el/ref=glass/nA=SCHA/src=data/ref=def(·), relativistic F_DM row IF-B1-6, add 'observed' to CONVENTIONS §12 status vocab); B1/D verifier minors applied in LIMITS rows only (not in the returns). Coverage now A 77 · B 0 · C 14 · D 0 (D3, D4, I2 counted C).
## RESUMED 2026-11-01 (user: "proceed"). WP8-U and WP8-R launched first (no dependency on the merge).
- WP7-E merge done: LIMITS "WP7-E" (L33–L38), NOTATION "Rows added WP7-E" (12 clashes resolved: κ_cal, X^{oth}, g_Luke, y_ion, δ_coll, r_coll, r_cap, σ_cap, 𝔮, m_ind, ΔE_X^b, ε → ε_eh), CORRECTIONS §18 (all WP7 owed renames, B1/B2/D/T included), FRAMEWORK status. Coordinator decisions in CONVENTIONS §13 rows 23–28 + "R13 amendments": configurational stored energy with ΔZPE in ℋ_ph; WP7 label numbering (only T, E extend L-numbers); geom ∈ {bulk, body, 1D, 2D, stack}; τ values K=el, nA=SCHA, ref=glass, ref=def(·), src, basis; F_DM^{rel} (IF-B1-6) as §9 amendment; status word "observed".
- IF-E8 (WP7-E): 1803.02903 measures η^φ_NR = 0.952 (95% C.L. band), **degenerate between E_st and collection (δ_coll, r_coll)**: r_coll = 1.144 alone reproduces it. Bounds (95%): ⟨E_st⟩/E_R ≤ 0.055 Si / 0.064 Ge (≤ 1% wider, 0.056 / 0.065, with ΔZPE in D′); p_surv·E_st,1/E_d ≤ 0.21 / 0.20. IF-E9 (shallow-level capture; exciton BSE parameters) owner unassigned.
- Next: WP5-ERR, WP8-F launched; then WP5-AUD (joint WP5-v4 + WP7-E audit, R×2) and WP8-S.
- **Provisional flag** [LIFTED R16: WP5-AUD §5 released the yield-dependent rows with F-a…F-i and R-a…R-i; WP8-F-v3 and WP8-R-v2 apply them; θ_X → θ_exc done in NOTATION (CW8-A)]: WP8-R and WP8-F were launched before the joint WP5 + WP7-E audit that FRAMEWORK requires before WP8 uses the yields. Their yield-dependent results (WP8-R NR/ER initial phonon populations and verdict; WP8-F stored-energy/LEE proxies) are PROVISIONAL until WP5-AUD, whose scope covers those sites. WP8-R's verdict does not enter SOTA as final before then. Pending NOTATION item: WP7-E θ_X (exciton nuisance) reuses WP6-v2's local name for θ_exch → rename θ_exc at the next NOTATION pass.
## R13 returns (2026-11-01; all CLAIMED, unrefereed; WP8-R/WP8-F yield-dependent items PROVISIONAL until WP5-AUD)
- WP5-v4 (WP5-ERR): A-1…A-16 applied; 17 conflicts listed (K1–K17, WP7-E-v3 wins; none contradicts a v3 derivation, only scope/definitions/tags); (W4) scope, (W6), (W11), (W12) change form; 75/75 checks. NOTATION row N_trap → IF-R13-1.
- WP8-U [superseded R16 by WP8-U-v3 + table v4, see the R14–R16 block]: 47 materials + 7 excluded families; 10 SURVIVOR (Si, Ge, GaAs, Al₂O₃, TeO₂, CaWO₄, Li₂MoO₄, γ-LiAlO₂, LiF, NaF), 30 SURVIVOR-COND, 3 REFERENCE, 4 EXCLUDED; table returns/R13/WP8-U-table.csv (1980 rows). ε_eh/F_eh GAP outside Si, Ge, diamond, SiC. Radiopurity: KTaO₃ 4.6×10³ Bq/kg (⁴⁰K), InSb 121 Bq/kg (¹¹⁵In). Source disagreements flagged (2008.08560 n_e; 1910.10716 c_LA). 23 PASS, 16 FLAG. Ran without WP8-F's property list → top-up owed (REF-WP8 row).
- WP8-F [superseded R16 by WP8-F-v3, see the R14–R16 block]: 9 FOM classes (ER-ρ, ER-light, ABS, NR-1ph, NR-mph/impulse, POL, MAG, PAER/Migdal, TLS/defects), rate FOM 𝓡 × kinematic factor, background-free 𝓩_0 and background-limited 𝓩_B scalars, systematics floor; property list for WP8-U (§5); 39/39 checks. LEE/stored-energy proxies provisional.
- WP8-R [superseded R16 by WP8-R-v2, see the R14–R16 block: (c) HV NO-GO → CONDITIONAL; δ_coll can carry the 0.048; (b) gap channel UNRESOLVED]: **NO-GO (provisional)** for mode/frequency/angle-selective NR/ER phonon discrimination: populations lose spectral and polarisation memory within ~10–100 ns, ≲ 0.1 mm; HV/NTL NO-GO at any contrast for E_R ≤ 300 eV (pair-number ceiling). Low-bias NTL-vs-primary phonon readout CONDITIONAL (measurement proposal IF-R4; ζ_O, σ_pos unmeasured). IF-E7: δ_prim ≤ 0.007, so collection memory cannot carry the 0.048 Si deficit; r_coll ≠ 1 expected, sign model-dependent. 48/48 checks.
- Next: WP5-AUD (joint WP5-v4 + WP7-E audit, R×2, incl. WP8-R/F yield sites); REF-WP8 (R×2 per WP8 package) + WP8-U top-up against WP8-F §5; NOTATION-APPLY for R13 symbols (incl. θ_X → θ_exc); then WP8-S.

## R14–R16 consolidated state (CW8-A merge, 2026-11-01; returns read through their errata; row texts in LIMITS "R14–R16", owed corrections in CORRECTIONS §19)
Status key (CONVENTIONS §12, §13 row 31): REFEREED = package had R×2 and its later verification is answered; CLAIMED + VERIFIED = R16 closure package verified once
(VER-CWn) and answered in its errata; CLAIMED = unrefereed. The WP8-S ranking (CW7 §12) is **not** merged (WP8-S not final; REF-WP8-S-A/B; rank.py must read table v4).
**Results (one line each).**
- **WP5-AUD (R14), REFEREED** (R×2 settled in CW5 §1 + CW5-errata): A-1…A-16 applied faithfully in WP5-v4; IF-R13-2 CONFIRMED with the general-r_coll form (AUD-1),
  κ_cal(r_coll); IF-R13-3 quench protocol CONFIRMED (Wigner R_I(0) carries 138 eV per 4096-atom cell); IF-R13-5 with the r_coll prior σ_ln 0.1 [E]; D′ must contain
  E_pairs + E_X at t_win (exact ratio, Si 100 eV r_g = 1: Y_H 1.407; the first-order 0.28 is invalid). **WP5-v4 REFEREED** when read through CORRECTIONS §19.5.
- **WP8-R HV verdict (IF-AUD-6 sentence as corrected by CW5 OC-7): "the HV (≥ 100 V) phonon-PSD NO-GO at E_R ≤ 300 eV is CONDITIONAL on (Y, F_NR, ⟨𝔮⟩, C.L.):
  firm at the central measured Y, F_NR (2303.02196) and at E_R ≲ 220 eV (1σ; maxima 1.26 at 100 eV, 1.72 at 220 eV); at the 1σ corner of the constructed 300-eV
  envelope the ceiling is 2.014 with ε = 3.8 eV (1.999 with 3.75)."** REFEREED.
- **L38 / η^φ_NR (WP7-E + WP5-AUD + CW5), REFEREED:** (AUD-1) is exact at first order for any r_coll; the E_st bound E_st/ω ≤ 1 − η^φ_NR is DERIVED for X^{oth}_ER ≥ 0 and
  r_coll ≥ 1, with the exact c_X correction for X^{oth}_ER < 0 (≤ 3×10⁻⁴ on 0.055/0.064). WP8-R-v2 does **not** support r_coll ≥ 1 (toy 0.87–0.98 [E]); on r_coll < 1
  the bound widens by g_Luke(1 − r_coll)(η − y_ion)/(1 + g_Luke); two biases invert (AUD-1) exactly (CW6-L5).
- **GAP-EF-v2, REFEREED** (R14 R×2 on v1 + VER-GAP-EF-v2): ε_eh and F_eh as moments of the energy-only cascade [D within (H-EF1)–(H-EF7)]; solver CROSS-CHECKED; with ω fixed
  F = Var(per-pair heat)/ε_eh²; F_eh = 𝒱_< + 𝒱_> + 2𝒞_<>, Si 0.091 + 0.288 − 0.265 = 0.114 (= R&K 0.115; 2.6σ below 0.119 ± 0.002; not independent support); F^{ren} is a
  lower bound in every computed case [C in general]; Rényi/RPP limit exact; 0911.1532 carries two misprints (ρ∞ 7th digit, F_unc dropped digit). **IF-EF6 SOTA row:
  "ε_eh ≈ 1.61E_g + k₂, k₂ = 1.2–2.5 eV (ω₀- and weakly E_g-dependent): an observed fit of the one-parameter cascade model, agreeing in form with 1.54E_g + 1.89" —
  status observed (v1's "derived" withdrawn).** 27-material predictions [E]; 4H-SiC: the 2005 limit F ≤ 0.04 lies below the model-class floor 0.051 (stated conflict).
  IF-E9 closed at the formula level (each captured electron raises ℋ_eff by exactly E_g); numbers open (GE-4).
- **EF-LIT (R16), CLAIMED:** no measured ε_eh or F_eh for Al₂O₃, CaWO₄, LiF, NaF; sapphire 27 eV is a vendor value, CaWO₄ ≈ 29.8 eV a Robbins–Lempicki estimate.
- **CW2 (LE-48…72), CLAIMED + VERIFIED:** 20 CLOSED, 5 CLOSED-AS-EXACT-GAP, 0 CANNOT-CLOSE. Exact coherent multiphonon weight and pointwise band; E^{Mig}_3 closed form with
  [CALC] NR coefficients (relativistic finite-nucleus contact density +8% Si, +37–45% Ge/Ga/As [E]); P_Mig ≤ E_R(δM/M)/E_g; Markov–Krein band for any anharmonicity;
  glass A^{IR}, B^{IR} from static configurations; isotope B−L Γ_iso/Γ_EM ≥ 6.3×10³ at mK, O(σ_M/M̄) +9% [E].
- **CW3 (LE-73…96), CLAIMED + VERIFIED:** Fano prefactor 1 in rate units; 𝔉 = 0 for PT-symmetric targets with N_e even under (P1)–(P5); Theorem D-m (i)–(ii) for magnetic
  insulators, (iii) conditional on the open (G5′-c); **(G5′) with U_qp = 1 WITHDRAWN (FALLS)**; 17th basis row 𝔳²_s (𝒪₂); relaxed electron-channel static step: L17 (iii) false
  for every solid as q → 0 [D]; WP7-D: 1306.6089 amplitude, 2501.05504 prefactor 32, 2305.05681, 1905.13650 CONFIRMED; dark Compton vector exact; ALP Eq. (3) REFUTED.
- **CW4 (LE-97…117), CLAIMED + VERIFIED:** CLOSED 16 (4 with exact-gap remainder), CLOSED-AS-EXACT-GAP 4, LE-107 split (Nb CLOSED, Al exact gap), CANNOT-CLOSE 1 part (Allen
  1971 equation numbers, closed access). (A2.2) [D] by Nambu second order; LB1-8 [D] under (H_W) with an absolute bound; resummed L^{BCS} at the Al edge; Dirac re-plot
  ×ε_bg² (σ̄), ×√ε_bg (κ); OPW sizes re-derived (FALLS → corrected); ZrTe₅ Δ_D = half-gap (value: see the conflict note below); Al bulk Δ_BCS ≈ 0.18 meV [E] (table 0.3 meV is film-like).
- **CW5 (LE-22, 23, 127…151, GAP-LEE), CLAIMED + VERIFIED** (its LE-22 part settles WP5-AUD, REFEREED): signed seed sampler with per-N_eh positivity; gap-release law
  r_g(t) (CW5-4) with bimolecular-loss forms (dense-track law FALLS → re-derived); renewal leading term DERIVED; L30 T⁻⁹ exponent DERIVED; α_ohm Born limit (factor 1);
  tanδ₀ of a-SiO₂ [FT]; LEE model: bound + structure derived, two missing steps (U_rel with (Γ_min, Γ_max); b_br).
- **CW6 (LE-20, 118…126) and WP8-R-v2, CLAIMED + VERIFIED / WP8-R-v2 REFEREED (R14 R×2 + VER-CW6):** WP8-R-v2 supersedes R13 WP8-R. Verdict: **NO-GO** for
  mode/frequency/angle selection of prompt populations in bulk Si/Ge; **(c) HV CONDITIONAL NO-GO** (above); **(b) zero-field gap-energy channel UNRESOLVED**; (d) low-bias
  phonon-read NTL CONDITIONAL (ζ_O,min 0.24 at σ_pos = 0.05). δ_coll^{gap} can carry the whole 0.048 Si deficit. **The "fitted Si→Al 0.3–0.55 ⇒ t̄_esc 0.10–0.19" FALLS:** the
  fitted coefficient is t̄_{Si→Al}·P_abs and constrains λ_pb/d; t̄_esc = AMM 0.32 / DMM 0.26 (RG7 closed as θ_esc^{film}). A_iso(Si) = 1.65×10⁻⁴⁵ s³ [E] within 0.4% of
  2408.04732 [FT].
- **IF-R6 statement (CW6 OC-CW6-6; supersedes the R13 sentence):** "Phonon NR/ER information at the sensors is charge-mediated (NTL, carrier-relaxation and gap-energy
  phonons). In bulk Si/Ge, prompt phonon populations lose frequency and polarisation memory within ≈ 10 ns (Si) / 30–100 ns (Ge) and ≲ 0.1 mm (WP8-R-v2 §2; [E], toy
  cascade with a derived f_*(t) scaling), except for events within that distance of an instrumented face; this does not hold for Al₂O₃. The zero-field gap-energy channel
  ((1 − 𝔶)E_g/ε_eh ≈ 0.28 of E_R in Si) is UNRESOLVED pending its release law and site (G-R2; CW5 (CW5-4)). Mode/frequency/angle-selective collection of primaries is
  NO-GO; HV phonon PSD at E_R ≤ 300 eV is a CONDITIONAL NO-GO (CW5 OC-7)." (near-face shell 0.24–1.9% of a 4-mm device with one instrumented face, 10–100 ns; CW6-errata B1)
- **CW7 (LE-19, 21, 152…157, 160, 176, 177), CLAIMED + VERIFIED:** halo-independent bound for directional responses (Theorem G8′, lab frame); continuous P_casc(N_eh|Λ)
  (solver fixed for θ_ii > 1); (P) leakage bound re-derived as (CW7-154′) (the R16 (CW7-154) FALLS); scalar-absorption closed form; magnon (r^M_mag = ΔS/S, derived) and
  one-sided SC rows; r_mat rule with signed elasticities (CONVENTIONS §13 row 29); low-T ε₀ of soft-mode crystals; cosmogenic rates [FT] for Si, Ge, NaI, Te.
- **WP8 SOTA block (CW7-errata §2.1):** "WP8-U/F revised (R16 CW7 + ERR-CW7): **WP8-U-v3, table v4, WP8-F-v3** supersede R13 and the R16 v2 files; yield rows released;
  WP8-S synthesis in CW7 §12 pending its revision (separate agent) and R×2." WP8-U-v3/F-v3 REFEREED at their R14-refereed content; the ERR-CW7 additions (shear-order fix,
  c_NR1, L-F4, polar bound, 𝓠_Mig plasmon pole, ²¹⁰Pb) CLAIMED (R×2 owed, IF-ERR7-6). Pool: 10 SURVIVOR, 32 SURVIVOR-COND, 2 EXCLUDED-RADIO, 3 REFERENCE (✎R17: ranked pool 11 SURVIVOR + 31 SURVIVOR-COND after diamond's promotion under
  CONVENTIONS §13 row 38). The light-mediator single-phonon rate is target-independent (1910.10716 Eq. (35)) ✎R17: only for m_χ ≫ (1 + κ_η)m_min^{ac}, κ_η = 3.14;
  ~~1/c ordering holds only for a heavy mediator at ≈ 0.1–0.43 MeV (Si)~~ ✎R17: heavy-mediator 1/c ordering holds pairwise on W_AB (per-material onset 4.7–5.7 m_min^{ac},
  ≈ 4.2 vs Si; first-order η(c + u) shift; LIMITS L-F1).
- **CMPMC-AUD (R15), CLAIMED:** CMPMC 921db93 was not usable for any campaign phonon spectrum or arrival-time number; 9 fixes on paer-sota; usage verdicts per module (§4);
  12-item SOTA list. **CMPMC-DEV (R16, paer-sota 3d43a02), CLAIMED:** items 1 (reduced), 2 (isotropic), 3, 4, 11 done; DO-NOT-USE modules guarded or fixed; 16/16 ctest;
  η_pb(Ω, τ_l/τ₀^φ) reproduces 1401.1937 Fig. 4 to ≤ 0.011; electrode recombination phonons soft (600 nm Al on Ge: mean 1.0 Δ_Al, 90–93% below 2Δ_Al).
- **COMP-PAER (R15), CLAIMED (unrefereed):** Si window [CALC] (PBE + scissor, C5 PASS): PAER-only 0.333 (replica) / 0.3374 (continuum) – 0.405–0.408 MeV; forbidden ZPL from
  0.405–0.408; allowed ZPL from 0.547 MeV (✎R17, CW1 OC-9: 0.405–0.408 kept, 0.407 with SOC; 0.547 is the nearest-pocket assignment, the allowed-size channel opens
  at ≈ 0.50 MeV on the X face). Rate/reach [E, ×/÷10]: σ̄_e^{95} ≈ 7×10⁻³² cm² (heavy) / 4×10⁻³⁴ cm² (light) at 0.40 MeV, 1 kg·yr; PAER is the only Si
  electron-recoil channel over ≈ 0.07 MeV below the ZPL threshold. Tier H and Ge FORMULATED.
**Cross-cutting findings.**
- **JARVIS elastic-tensor shear order.** JARVIS `elastic_tensor` lists the shear rows as (xy, yz, zx), not Voigt (yz, zx, xy). Every non-cubic C_ij, Christoffel speed and
  NR edge used in R14–R16 (WP8-U-top LT1, WP8-U-v2/table v3, WP8-F-v2, CW7 §12 ranking inputs) was built with **C₄₄ ↔ C₆₆ swapped and C₁₄ misplaced**. Found by REF-WP8-S-A §5c;
  fixed in returns/R16/WP8-U-table-v4.csv (rows `C_ij_Voigt_DFT_v4`, `c_LA_Christoffel_avg`, `c_dir_100_001`, `c_NR1_heavy`, `c_LA_max_dir`; [001] TA pair degenerate in all
  13 uniaxial entries; TeO₂ c̄_LA 4.05 → 4.10 km/s; CW7-C33, C34). Rule now in CONVENTIONS ([DB], V5′). Cubic entries are unaffected. Status of the fix: CLAIMED (IF-ERR7-6).
- **CMPMC Kaplan-buffer bug** (CMPMC-DEV commit f61d710): the Kaplan cascade buffer (`SmallVec<double,64>`) silently dropped entries, so a film phonon above ~130Δ (≈ 22 meV
  in Al; Ge prompt phonons are 35.7 meV) lost energy (7% at 160Δ), and `escaped_or_killed` absorbed the remainder so the closure checks did not see it. Fixed (`KaplanBuffer`
  = 256; closure ≤ 3e-15 per event at 50–350Δ). Any R15-era run in which Debye-scale phonons reached a film unconverted (likely only the benchmark) must be checked (IF-DEV-5).
  Campaign [CALC] gate: paer-sota ≥ 3d43a02 (IF-DEV-4; code/ENV.md update owed by the coordinator, not edited here).
- **Published-paper errors confirmed in R14–R16** (each by a verified return): 2603.13052 Eq. (4.8) is 2× the standard dσ/dq (rate unaffected; CW2); 2308.06314 Fig. 2 uses
  the rigid-ion vertex, so its GaAs electron-scalar rate is high by ≈ 7–9 (CW2); 2109.08168 Eq. (3) REFUTED and PDF Eq. (16) inconsistent with (15) (CW3); 1306.6089's verbal
  gloss misstates the shift ×2 (amplitude correct; CW3); 2011.01940 Eq. (9) not current-conserving at bound kinematics (CONFIRMED; paper-error size = exact gap; CW3);
  2208.05967 Eq. (6) wrong by μ_eχ/(4E_r) and dimensionally inconsistent with its Eq. (12) (CW4, CONFIRMED by VER-CW4); 2212.04504 Eq. (12) 3q̃ → 3q̃² misprint, impact
  1.47–0.56 (heavy) [E] (CW4); 1910.02091 Eq. (3.14) typo, and its Table 1 "Exp. [52]" Δ is not in [52] (CW4); 0911.1532 Eq. (23) ρ∞ and p.4 F_unc misprints (GAP-EF-v2-errata);
  2008.08560 Table I n_e column = 2 e/atom (CONFIRMED) and its "c_s" undefined for SiC (WP8-U-v3); 1109.1193 Eq. (21) and 2302.05998 Eq. (8) carry a Luke-rate typo against
  their Eqs. (22)/(9), and G4CMP's CalcQPEfficiency has an operator-precedence bug (CMPMC-AUD, CLAIMED). Checked and **not** errors: 2501.05504 Eq. (7), 2305.05681 Eq. (6),
  1905.13650 penalty, 2109.08168 Eq. (2), 2401.11971 Eq. (5) correction (impact on its CRDM limits still UNRESOLVED). ~~1910.10716 c_LA: "suspect, pending measured C_ij"
  (not a confirmed error).~~ ✎R17 (WP8-errata §12 + VER-ERR-WP8 C9, C2c): 1910.10716 Table I c_LA CONFIRMED inconsistent with measured elasticity for GaN, AlN, ZnO
  (above every Christoffel LA speed), CsI (20% below √(B/ρ)) and **CaWO₄ (8.4% below the measured sphere-averaged LA speed and below the slowest LA direction; measured tensor
  2508.08858 p.16, quoting its ref. [73], Farley & Saunders 1972)**; α-SiO₂, NaCl pending. 1805.02495's Si→Al "transmission" is an absorption probability t̄·P_abs (interpretation, CW6).
**Open conflicts for the coordinator** (returns/R16/CW8-A-merge-log.md §C): ZrTe₅ Δ_D 11.75 meV (WP8-U-v3 §5, table v4) vs 11.8 meV with "11.75 (exp [52])" unsupported
(CW4-errata OC-11); WP8-U LU3 withdrawn (WP8-U-v3) vs upgraded (CW6-errata OC-CW6-4) — settled by entering the content as CW6-L4.
**Next:** [✎R17: done; superseded by "R17 final state" below] WP8-S revision (rank.py → table v4) and its R×2; R17 R×2 of ERR-CW7 + WP8-U-v3 + WP8-F-v3 (IF-ERR7-6); CW1 (LE-24…47, 178, 179) after COMP-PH (LE-16, no return yet);
code/ENV.md CMPMC gate update; CONTROLS C4 note (COMP-PAER IF-CP-4).

## R17 final state (CW8-FINAL, 2026-11-01; record returns/R17/CW8-FINAL-log.md)
Merged in R17: CW1 (returns/R16/CW1.md read through referees/R16/VER-CW1.md and returns/R16/CW1-errata.md), COMP-PH (returns/R15/COMP-PH.md), WP8 (returns/R17/WP8-errata.md
read through referees/R17/VER-ERR-WP8.md, 0 FALLS; the verifier's corrections C1–C12 are applied as owed text, CORRECTIONS §20.2), GAP-EF-v3 (returns/R17/GAP-EF-v3-errata.md),
CW8-B and CW8-LIT bookkeeping. Row texts in LIMITS (✎R17-F), owed corrections in CORRECTIONS §20, symbols in NOTATION "Rows added R17 (CW8-FINAL)".
**Phase-2 work list:** every computation the campaign specified but did not run is a DC item of **state/DEFERRED-COMPUTE.md** (authoritative). Its header still says "CW1 never
returned" and lists DC-5 and DC-6 as open: that is stale. CW1 computed the DC-5 vertex (Σ_v|ρ|² = 0.150 [CALC]) and the DC-6 ratio at the [E] level (ϖ̄_II, vertex [CALC]); DC-6's
remaining part is the LE-26 exact gap (S^{PA} from the amplitude = DC-1; ZPL side on the same bins, CW1-errata E-15(2)), and DC-7's LE-27 part is closed by CW1 §4.

**Si PAER window as finally established** (tier B; every rate/reach number stays [E, ×/÷10] until tier H)
| Boundary | Value (MeV) | Tag and status | Tier-H deferral |
|---|---|---|---|
| PAER onset | **0.3332** (exciton replica) / **0.3374** (continuum) | [CALC] COMP-PH §0 (a_PBE phonons; Si controls PASS except ε_∞ +11% and L_LO −5.4%, FAILED-CONTROL, measured ε 11.7 used) = COMP-PAER §4 (C5 PASS); CLAIMED | DC-1 (L^{PA} from the full (M.1) amplitude; the 0.333–0.35 edge carries an exponentiated threshold error) |
| First zero-phonon edge | **0.405–0.408** (continuum; best 0.407, PBE+SOC, a_exp, DFT-re-minimised); 1s **0.402–0.405** | [CALC] CW1-L1 (CW1 §1 + CW1-errata E-1); off the valley axis in a {001} mirror plane, second class by the σ_z glide (CW1-L2); COMP-PAER's 0.405–0.408 kept; COMP-PH's 0.4154 is the on-axis local optimum; CLAIMED + VERIFIED | DC-1 stage-6 grid must contain the mirror-plane cones, the second heavy-hole cone and the X-face edge (IF-CW1-4) |
| PAER leads | to **≈ 0.43** (central 0.424–0.428), **≥ 0.42** (at least, 0.418–0.421) | [E] (ZPL vertices [CALC]; PAER side ×/÷10; second-hole term an upper estimate) CW1-L4 (CW1 §3 + errata E-7); CLAIMED + VERIFIED | DC-1 (S^{PA} from the amplitude) + the ZPL side on the same bins (LE-26 CEG) |
| Two-channel region | **0.43–0.51** | [E] as above; the second (mirror-even) heavy hole, open from 0.415–0.420 MeV, dominates the ZPL side above 0.43; CLAIMED + VERIFIED | DC-1 + LE-26 ZPL-side spec |
| Zero-phonon leads | above **≈ 0.51** (allowed-size (2̄00)-class ZPL opens at ≈ 0.50, ZPL/PAER 2.4–7.0; ≥ 10 pointwise from 0.51) | [E, vertex CALC] CW1-L3 (CW1 §2 + errata E-5, E-6); the 0.62 MeV fallback and 0.547 as the allowed onset are withdrawn (0.547 = nearest-pocket value); CLAIMED + VERIFIED | DC-1 (ZPL and PAER rates in one pipeline) |
Ge: the window is not established (COMP-PH Ge fails its band-order and TA controls): DC-2 (HSE06+SOC edge), DC-4 (6³ DFPT), DC-3 (tier H). GaAs decoy C8: PAER-leading only at
≈ 0.43–0.51 MeV [E, parabolic] (CW1 §24), DC-8.

**WP8 status:** WP8-U-v3, WP8-F-v3, WP8-U-table-v4 with WP8-errata, WP8-S-v2 with code/REV-WP8-S ranking_v3 are **REFEREED** (CONVENTIONS §13 row 39) (VER-ERR-CW7 and VER-ERR-WP8, 0 FALLS; no
SURVIVOR verdict, leader or tier changes under the verifier's corrections). (Reading under CONVENTIONS §13 row 31: these packages had R14 R×2, so the verified content would also
read REFEREED; the brief's word VERIFIED is recorded and the choice is left to the coordinator.)
**WP8 next-target guide, headline** (WP8-errata §16.2–§16.4 with VER-ERR-WP8 C6, C12; r_mat = 0; screens S1–S4 as a column):
- **Survivors (11):** Ge leads the ER floor (0.210 MeV) and ER quanta (3.37 eV, conditional on the 50 mK fit), the only survivor in the leading tier of two channels (excluding
  Migdal). **TeO₂ leads the survivors' heavy-mediator NR channel** (2.31 × Si; DB tensor, ρ proxy, S4-COND ¹²³Te). **Diamond leads the NR edge under the array rule**
  (3.15 keV; CONVENTIONS §13 row 38: ≥ 6 × 0.175 g crystals, per-crystal thresholds, surface-to-volume ×1.8, per-crystal LEE). LiF leads the polar rate, GaAs the polar reach.
  No Migdal reading at r_mat = 0 (max P₁ 0.32); no light-mediator ranking (×1.08 spread). Heavy-mediator readings hold on the pairwise window only: the η(c + u) shift
  makes C/Si 0.93 and C/TeO₂ 0.90 at 0.2–0.4 MeV, so no common window "vs Si" is 10% pairwise (C6; no leader moves).
- **Full 42-pool:** Pb salts lead the ER floor and quanta, all conditional (ε_eh [E] outside GAP-EF's validated range; ²¹⁰Pb; PbSe and PbS still need mK operation (S1) and phonon
  readout (S3), PbTe readout (S3)). CsI leads NR heavy and polar reach on an [E]-driven B-floor model (1910.10716's c_LA rejected; S1/S3 COND; measured or computed C_ij owed,
  DC-93). h-BN tops the 42-pool NR edge only at r_mat = 1 (S2 FAIL rests on an [UNVERIFIED] row). NaCl leads Migdal only at r_mat = 1 (L(k, ω) = DC-28).
- **Most rank-changing inputs:** literature reads (IF-EW-3: diamond, TeO₂ and CsI C_ij, LiF ε₀, GaSb low-T gap; not measurements); measurements (Pb-salt ε_eh at mK, ²¹⁰Pb
  activity of low-background lead, α-quartz mode data, CsI ω_LO at low T); computation (L(k, ω), DC-28).
**GAP-EF-v3:** the commensurate-grid rerun moves every ε_eh by ≤ 0.19% and F_eh by ≤ 0.13%; F_Si = 0.114 and its 2.6σ below 0.119 stand; 𝒜_ph 5.595 → 5.588 eV³; (EF11) is
0.3% low (not 4.6%); the WP8-errata "+1.3% in ε_eh" never applied to GAP-EF-v2 (closed: ≤ 0.19%).
**Ledger:** LOOSE-ENDS LE-1…179: CLOSED 134, CLOSED-AS-EXACT-GAP 42, CANNOT-CLOSE 2 (LE-171, LE-172: book-side SPINE and ledger passes), OPEN-pending 0, OPEN 0.
**Package checks (R17 CW8-FINAL rerun, one run each):** code/CW1 52/52 PASS; code/REV-WP8-S 31/31 PASS (checks.py only; rank.py not rerun); code/CW7 41/41 PASS (16.6 s);
code/GAP-EF-v3 41/41 PASS (185 s). COMP-PH and COMP-PAER have no checks.py.
## Book-phase corrections (Ch13 review, 2026-11-06) — authority over earlier lines
- Interim factor [0.4, 1.8] → screening correction 0.3–2.6 [E] relative to the optical calibration; pair-channel finite-q residual unsized (CORRECTIONS).
- GaAs PAER-leading band 0.43 → 0.52–0.56 MeV (E_L(0) = 1.815 eV); supersedes 0.43–0.51.
- Si rate-estimate reach on the Stanford 0.5 K cold edge: heavy 3e-30–3e-29 cm² at 0.36 MeV (×15), 4e-32 at 0.40 MeV; lead masses unchanged.
- Si nonadiabatic ZPR 8 meV (6.1 VBM + 1.9 CBM), Poncé 1504.05992 Table VI.
## Book-phase corrections (Ch14 review, 2026-11-06)
- Longitudinal spin response from neutron data: model-dependent (localized-moment q+G inversion), not "no route".
- Fixed-amplitude limit penalty: 1.99 (median) / 2.73 (at the detection threshold, reproduces Centers et al. 2.7).
- GaAs ⟨|L^ph|⟩: 0.124 (book PBE IFCs) vs 0.07 (Matas et al.) open; a single Cartesian component gives 0.062.
- Earlier line "F^mag ∼ 0.5 at q ≈ 0.5 keV for Fe³⁺" is refuted (⟨j₀⟩ ≈ 0.99 there); unused.
- ALP absorption in superconductors: clean singlet SC absorbs through the spin current (book 15.4, verified); published phonon-only clean-Al projections understate the reach by ~10⁴ in g_aee; dirty films comparable (Mattis–Bardeen).
## Book-phase corrections (Ch15 review, 2026-11-06)
- SC edge: first-order term 17 % at y = 5 (bare bubble only); the conserving edge values (above) replace "≤ 16 % at 5Δ", "8–16 %", "y ≲ 3.5"; exclusion y < 3.
- Spin-current ALP absorption: verified with caveats (ℓ ≫ ξ₀; gain only vs phonon-only clean-Al projections, films comparable: 1.5e-12 vs 2.0e-12; line shape model-dependent, ×1.2 in g). The integrated weight is protected by the exact spin f-sum and zero spin stiffness.
- Strong coupling: the normal-metal 1/(1+λ_tr)² = 0.52 is known (Allen 2015 Eq. (3)); only the superconducting extension is open.
- Sheet screening = kd ≪ 1 limit of Lasenby–Prabhu Eq. (19); exact slab 588 vs 540 at qd = 0.086.
## Book-phase corrections (Ch16 review, 2026-11-06)
- DM–TLS scattering (a-SiO₂): book 2.3e-2 /(kg·day·meV) at 1 MeV (C_l = 1.9e-4, escape-cut halo), est. ×3; supersedes 3.7e-2.
- Du et al. misprint impact (1.47/0.91/0.59/0.56, heavy) upgraded [E] → [CALC].
- WP7-B1 Frenkel binned sum superseded by 16.4: holds for whole manifolds with no outside coupling, flat η and ε_mac; intensity borrowing is first order.
- ZrTe₅ published/total factor: 5500–6600 (book halo, Δ 11.8 meV); 4300–6600 across halos and half-gaps; recomputation ratio 0.8–1.1 with (220, 232, 600) km/s.
- (supersedes the ZrTe₅ line above) ZrTe₅ total-ε with the whole measured-structure row of 1910.02091 (Δ_D 11.8 meV, Λ̃ 0.191 eV): threshold 8.0 keV isotropic (9.6/7.1/9.0 by axis); 108 ev/kg-yr at 100 keV and 1e-38 cm²; best reach 1.5e-40 near 38 keV; published/total factor 5200–6400 (book halo), 4300–6600 across halos and computed rows; absorption ζ 1.25e-15 at 100 meV (weaker ×6.3–6.4); one-loop parameter 1.02.
- Si Migdal rate at 0.42–1 MeV lies almost entirely (≥ 99.8 %) in the band 0.75 keV ≲ q ≲ 2 q_BZ, where the coherent response is unsized (LE-188): the light-mass Si Migdal rate carries an unsized model uncertainty; the diagonal/impulse form is reliable from ~3 MeV up.
## Book-phase corrections (Ch17 review, 2026-11-06)
- Counting vs linear readout: ratio e^{m/2T} for a counter whose band is the line; no coherent crossover below T (the advantage tends to one).
- Migdal figure of merit depends on the plasmon dispersion (LiF/Si 0.87 dispersionless vs 1.37–1.72 dispersing); the Migdal target order is open. The X_pole prior is a device (Si's own X ≈ 25).
- Heavy-mediator diamond/Si order reverses below 14 keV.
- Si Migdal rates below ~2 MeV carry the unsized coherent factor (LE-188).
## R19 FBC (full-band Si carrier cascade, stage 1; refereed ×2 + verified)
- No fitted constant: ε_eh 4.15 eV [3.95, 4.73] + model-class systematic ≥ ±0.4 eV (measured 3.749); ε is set by the ionization rate below 4.5 eV. F_eh 0.114 [0.101, 0.115] (agrees with the energy-only cascade; the 2.4σ deficit vs 0.119 is unexplained, not shown structural). P(N≥2, 5 eV) 0.097 [0.030, 0.173]; step-model overcount ~10× (≥ 6× robust). Heat 71.6 % at 100 eV. Momentum/valley memory ≤ 0.015 (DP model). Photon-vs-DM seed difference unresolved (photon seed not k-converged). ~0.6 eV gap to Nielsen–Fischetti's GW/BSE ε 3.50 unexplained. Stage 2 (excitons, GW rates, DFPT couplings, Ge/GaAs with SOC) → compute agent.
## Book-phase corrections (Ch19 review, 2026-11-06)
- Calibration chain: see CORRECTIONS (book Ch19 R1/R2). Stored-energy bound 0.055 (Si) with condition (e) ε_eh ≤ 3.82 eV; 0.049 with the book ε_eh = 3.75 eV. Collection-only explanation (needs 1.128) is not reached by the mean-field transport estimate of book 20.5, but not excluded until computed real-detector kernels exist; the two-bias measurement decides. The 𝔯_coll sign is open (book 20.5).
- Binary threshold for electronic excitation by recoils: 352 eV Si, 399 eV Ge.
- 𝔯_coll final band (book 20.5, Ch20 R1 rework): energy conserved (all film phonons returned, one or two films, 60 nm to thick, sub-gap lost or absorbed) 0.81–1.02 over ⟨E_L⟩ 0.75–4.7 meV, 0.82–1.01 at 0.84 meV; one Al film 0.96–1.02, two films 0.81–1.01; ε_prim 0.684; uniform signal-free sink (loss up to 0.3/hit) ≤ 1.023. Selective sink (lumped film) 1.05–1.53 is an upper envelope with no physical sink identified. 1.128 is not reached by the transport estimate; not excluded until computed real-detector kernels; the two-bias measurement decides. The earlier "1.05–1.13, reachable" note came from deleting escaped phonons and the second film's relaxation phonons (CORRECTIONS).
