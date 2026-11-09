# R6 / AUDIT: cross-package consistency of the v2 packages (WP0-v2 … WP6-v2)

Brief: briefs/R6/AUDIT.md, plus the coordinator's mid-task addition (§8, catalog coverage; line cap 330). Read: returns/R6/WP0-v2 … WP6-v2,
CONVENTIONS, NOTATION v3, LIMITS, state/CORRECTIONS, state/SOTA, CONTROLS, README, literature/CATALOG-A, surveys/dm-solid-state-processes §4, §12.
Sympy and arithmetic checks: scratchpad `audit_checks.py` (exact identities and closed-form numbers, all as stated below). No other file edited.

**Verdict.** The seven v2 packages agree on every interface quantity of brief item (1), up to one formula-level mismatch at the
WP3 → WP6 interface (**A1, blocking**). The SOTA "R7 ITEM" 𝔨₃ normalisation mismatch is **not a mismatch** (§6, S1). The rest are
stale cross-references, notation slips and coordinator edits that are owed but not yet made. **1 blocking defect, 20 minor.**

---
## 1. Defect table
| ID | Packages | Location | Defect | Proposed resolution | Severity |
|---|---|---|---|---|---|
| A1 | WP3, WP6, WP1 | WP3 §M3, §3 (L8), IF-5; WP6 (3.3) PAER bullets, §5.2 n_g row | WP6 (3.3) needs the onset exponent of the **angle-averaged** S̄(q,ω) ∝ (ω − E_th)^{p_on}. WP3's p_on = 2 / 3 / ½ is the fixed-q exponent of S^{X+}, whose threshold E_g^{ren} + ω_{Q*ν}(q), Q* = k_c − k_v − q mod G, moves with q̂ through the phonon dispersion. WP1 [E10] shows that angle averaging raises a fixed-q exponent by +1 (+2 if the vertex vanishes on the minimum direction) when the threshold has an isolated quadratic minimum over q̂. The edge exponents 11/2, 13/2, 4 (+k_tail) are therefore not established. WP3 C5 also states that the infimum over q is E_g (acoustic Q* → 0), not E_g + ω_TA. | WP3 to give p_on for S̄ at fixed \|q\|: minimise E_g^{ren} + ω_{Q*ν}(q) over q̂ and apply the [E10] rule, separately for the acoustic Q* → 0 direction (where the window is empty) and the TA/TO pockets. WP6 to replace the three bullets with the resulting S̄ exponents and keep the type-Δ choice. R7 referee item. | **blocking** |
| A2 | WP0 | (4.7) last sentence; §11 F1, F4, F6; §12 OW0-7, OW0-8 | Stale: "κ₃", "link … OPEN (F4)", "WP2 still writes G", F1 "pending REV-WP1/WP3". F4 is closed at moment level (WP2-v2 (5.2′), WP3-v2 J8), F1 is accepted (WP1-v2 §1.3, WP3-v2 §M7), and F6 is done. Also, the closed form "point nuclei and cubic sites → −q²Z_κe²𝓃_κ𝓃_e(R_κ)/(3m_eM_κ)" needs **q → 0** (qa ≪ 1): the phase e^{iq·(R−r)} gives the traceless (ℓ = 2) part of (q·∇)²U a nonzero average at finite q. WP3 J8 states q → 0 correctly. | WP0 erratum at the next revision: 𝔨₃, cite WP2-v2 (5.2′) and WP3-v2 J8, add the "q → 0" qualifier, close F1, F4, F6 and OW0-8 and narrow OW0-7 to the referee check. | minor |
| A3 | WP0, WP2 | WP0 (9.7) L4 row | WP0 cites 1807.10291 Eqs. (29)–(31); WP2-v2 found that the isotropic one-branch \|ℳ\|² is Eq. (32) (its #34). | Cite Eqs. (29)–(32). | minor |
| A4 | WP0, WP3 | WP0 (8.3) "c = 2.71"; WP0 §6.2(ii), (4.8); WP3 J3, J8, (W.5) "∇_RV", "⟨∂²V⟩" | Bare c is reserved for the band subscript (WP6 IF6-2). V is the crystal volume in NOTATION, but here it is the potential energy (WP2 IF-5). | Write 2.71 explicitly; use V_pot (V_eN, V_NN) as WP2-v2 does. | minor |
| A5 | WP0 | §12 O6 | It cites "(2.5)/(2.9)", but v2 has no (2.5). | "(2.9) and the (3.5)–(3.6) absorption prefactors". | minor |
| A6 | WP3 | §M7 rigid-shift frame theorem; §M10 X2-N3 spec | The frame theorem uses χ, χ^{(2)}, χ⁰ for responses (the global rename χ → R was missed), bare c and D, and "ℓû·m_eΔv^g" (should be ℓ_Q ê). The spec writes "Λ(q) ≈ Λ(0)?" (X2's Λ_f → r^{pair}_f was missed; Λ is the final-state class). | Rename to R, R⁰, a named constant, ℓ_Q ê·…, r^{pair}(q). | minor |
| A7 | WP3, WP1 | WP3 §M9, IF-8 | The Si zero-phonon indirect exciton is quoted at 0.473 MeV. WP1-v2 gives 0.472 MeV at v_max = 794.5 km/s (recomputed here: 0.4721). | 0.472 MeV. | minor |
| A8 | WP3, WP2 | WP3 §2 L7b validity | It reads "impulse q ≳ √(2Mω̄) = 46 keV … i.e. m_χ ≳ 50–70 MeV". WP2-v2 uses x_R = 1 at 45.8 keV and the impulse onset q ≳ 2√(2Mω̄) = 91.5 keV, i.e. m_χ ≳ 17.3 MeV at the endpoint q = 2m_χv_max. 46 keV corresponds to 8.6 MeV at the endpoint (checked). | Adopt WP2's criterion and endpoint kinematics, or state that 50–70 MeV refers to typical (not endpoint) q. | minor |
| A9 | WP6, WP1, WP3 | WP6 (3.1), (3.5); WP3 §3 (L8); WP1 header | Si threshold conventions are mixed. WP6 m_min = 0.319 MeV uses E_th = 1.12 eV (a scissor-code or room-temperature gap). WP1 and WP3 use E_g(0) = 1.170 eV, which gives 0.333 MeV. The PAER window's lower edge 0.34 MeV is E_g + ω_TA = 1.188 eV, i.e. 0.338 MeV (checked). | Every quoted threshold mass names its E_th; the campaign default is the measured E_g(T_op), as WP6 §5.2 itself recommends. | minor |
| A10 | WP3, WP5 | WP3 §M4 "F8"; WP5 (W15) | Two estimates of the GaAs Fano-term effect on P(N_eh): WP3 gives "≲ 2×10⁻³ per bin edge"; WP5 gives \|ΔP\| ≲ 0.11 Γ/δ (2×10⁻³ off-edge, up to 7×10⁻² in the edge shell). The phase prefactors also differ by ~2 (WP3 2\|sin φ\| vs WP5 0.3). | Quote WP5 (W15) as the campaign bound (rigorous total-variation step × [E] phase); WP3 cites it. | minor |
| A11 | WP5 | §1.3, §5 text after (W13), flags I1, I3, I4, I5, I7 | Stale. I1: WP4-v2 dropped the factor 2 (η_pb = Δ_BCS⟨N_qp⟩/ω). I3: WP1-v2 adopted the out-state [E2]. I5: WP3-v2 §8 already writes the joint density of (E_e, E_h). I7 and §1.3: the NOTATION v3 addendum now has the E_e, E_h row. I4: WP6-v2 already writes ε_eh. (This is the SOTA item.) | Erratum lines at R7: mark I1, I3, I4, I5, I7 closed and delete the "WP4 [4.6] writes 2Δ…" sentence. No formula changes. | minor |
| A12 | WP6, WP5 | WP6 §5.2 yield row, IF6-1, IF6-5, IF6-6 | Stale flags: WP5 already renamed θ_k → θ_Rk; F1 is accepted; WP2 already renamed G → GS. The nuisance names θ_{R-k}, θ_W, θ_X do not match WP5-v2's θ_Rk, θ_GW, θ_exch, and WP5's θ_Eg and θ_𝔉 (type A on P, GaAs) have no row in WP6 §5.2, although §7.4 gates the 𝔉 export. | Adopt WP5's names; add θ_𝔉 (A on P_casc, \|ΔP\| ≤ 0.11Γ/δ, 0 for Si/Ge) and θ_Eg (E); close IF6-1, IF6-5, IF6-6. | minor |
| A13 | WP4, WP2 | WP4 I3; WP2 IF-8 | Stale: WP2-v2 states its eigenvector convention (e^{iq·r_κ}, IF-9), and WP3-v2 writes S^{GS}_κκ. | Close both. | minor |
| A14 | WP3, WP4, WP6 | new-symbol tables | Several new symbols are claimed collision-free but are not. 𝒜 has three meanings: WP6 𝒜_ij (NOTATION), WP4 𝒜^α (two-magnon amplitude), WP3 𝒜_ν(ω;T) (PA branch spectrum). y means ω/Δ_BCS in WP4 and ω − E_R in WP6. WP4 §5.4 reuses 𝒮_F, ζ_S with a different function (πζ/(1 − e^{−πζ})) and a different ζ_S. n_D is the WP4 defect density and also the τ multipole slot (WP4 I6). | NOTATION v4: 𝒜^{2m}_α, 𝒜^{PA}_ν, y_BCS / y_R, 𝒮_F^{D}, ζ_S^{D}, 𝓃_D. | minor |
| A15 | WP6, WP1 | WP6 §10 literature | WP6 lists 2607.06005 as [ABS], while WP1-v2 re-read it in full text. | Cite as [FT via WP1]. | minor |
| A16 | coordinator | LIMITS.md | The status column is OPEN everywhere, and the chain column is the R1 hypothesis (L7d, L12, L15, L16 and the L2 condition are not amended). These are CORRECTIONS §16 rows 3–4, not yet applied. | Apply §2 of this audit. | minor |
| A17 | coordinator | state/SOTA.md | CORRECTIONS §15 is entirely unapplied: "P(Q\|q,ω)" (lines 88, 121), "Convention C1" (119), theory row 11 not marked SUPERSEDED (18), amendments lines 22–25 and the WP6 convention flags (103) not marked resolved, no "read CORRECTIONS first" pointer. Line 220, "contact part of 𝔨₃ = −(m_e/M_κ)·(4.7)", misstates WP2-v2 (§6, S1). | Apply §15; fix line 220 to "𝓜³_κκ\|_{V_eN} = −(m_e/M_κ)𝓜³_eκ". | minor |
| A18 | coordinator | CONTROLS.md C4, C7; README.md | The C4 "compensated by Debye–Waller" wording is still there (CORRECTIONS §16). C7 text uses old notation (c, P_c, v_c, η). README lacks CONVENTIONS and CORRECTIONS. | Apply §16; restate C7 in v3 symbols (= WP0-v2 (4.9)). | minor |
| A19 | coordinator | literature/L1.md | CORRECTIONS §14 renames are owed (no revision of L1 exists). | Leave owed, or add an errata header. | minor |
| A20 | coordinator | NOTATION.md | Requested rows are pending: WP1 IF-9 (9 rows); WP2 IF-5/IF-6 (V_pot, V_eN, E^ad_n, q_BZ, G_min, …); WP3 (E^{Mig}_3, M^{exc}_{λ±}, 𝒜_ν); WP4 I6/I7 (~30); WP5 §14; WP6 IF6-2/IF6-3 (ℒ, π_k, a_k, index ex). | NOTATION v4 pass, applying A14 at the same time. | minor |

---
## 2. LIMITS status table (owner, status, chain with v2 equation numbers)
Statuses are campaign statuses (CONVENTIONS §12): every v2 entry is CLAIMED, pending R×2, unless noted. "Chain v2" means the chain cites WP0-v2
numbers and the owner's v2 equations; ✔ = checked consistent with WP0-v2 (9.7).
| # | Owner | v2 location | Chain (v2 eqs) | Proposed status | Note |
|---|---|---|---|---|---|
| L0 | WP0 | §9.1 | (3.3) → (9.1) → (9.2), 𝒢 = η/2q ✔ | DERIVED | — |
| L1 | WP1 | §7 L1 | WP0-v2 (3.3), (9.1), (9.2), (7.2) → [E1] IP → [E12] ✔ | DERIVED; SOTA #7 CROSS-CHECKED | D1's 2πα owes ×2 |
| L2 | WP1 | §7 L2 | (3.3) → (5.5)(i)/(ii) → (5.4) → (4.1) ✔ | DERIVED (✎ condition) | LIMITS chain must add the clamped / ω ≫ ω_max condition |
| L3 | WP1 | §7 L3 | (3.3) → (5.3) screening per row → [E4]–[E6] ✔ | DERIVED (✎) | 2510.25835 O₈ conservative ×O(10) [E] |
| L4 | WP2 | §9 L4 | (3.3) → (1.1) → (2.2) → (5.4) ≡ (4.2) → (4.3) ✔ | DERIVED | A3 (Eq. 32) |
| L5 | WP2 | §9 L5 | (2.1) → (2.3)/(2.4) → (3.2) → Poisson ✔ | DERIVED (✎ control) | x_coh retired |
| L6 | WP2 | §9 L6 | self part → (5.3) → WP0-v2 (3.4), (9.1) ✔ | DERIVED (✎) | skewness 𝔨₃^{GS}, X remainder (5.2) |
| L7a | WP3 | §2 | (W.5) T0 + T6, boost m_A ✔ | DERIVED | — |
| L7b | WP3 | §2 | (W.5) T0–T5 imp, soft → 4α ✔ | DERIVED | A8 (validity numbers) |
| L7c | WP3 | §2 | (W.5) T0–T4 ≡ 2210.06490 Eq. (3.8) ✔ | DERIVED | 2603.13052 Eq. (4.7) misprint |
| L7d | WP3 | §2 | (W.5) with off-shell phonon; n = 0 → X0, n ≥ 1 → X+ ✔ | DERIVED (✎ sector) | LIMITS chain must be amended |
| L8 | WP3 | Part I, §3 | (M.1)–(M.14), DC outside window ✔ | DERIVED (REFEREED R2 core; X1/X2/O4 parts CLAIMED) | A1 (onset); interim factor [0.5, 1.2] |
| L9 | WP3 | §4, (M.17) | L8 → q → 0 (C1) → ε^L = ε^T ✔ | CROSS-CHECKED (prefactor in FT) | LIMITS already says CROSS-CHECKED/REFEREED w/ corr. |
| L9b | WP3 (WP1 §2.5) | §4 | WP0-v2 (3.5)–(3.6), (2.9) ✔ | DERIVED + caveats | T-transfer of σ₁; ALP triplet refinement (WP1) |
| L10 | WP1 | §7 L10 | [E1] → jellium → RPA ✔ | DERIVED | Mermin = closure, not a rung |
| L11 | WP1 | §7 L11, [E9] | pole of ε^{-1}; no RPA plasmon label (WP0-v2 (7.1)) ✔ | DERIVED | no bulk plasmon for halo DM |
| L12 | WP3 | §5, (W.11)–(W.12) | X0 ⊕ X+ adiabatic, ω_ph dropped ✔ | DERIVED (✎ ZG deterministic) | never ZG + PAER |
| L13 | WP4 | §2.1, [2.1]–[2.2] | (3.3) spin row → 6 steps ✔ | DERIVED | magnetic form factor |
| L14 | WP1 | §7 L14, [E7] | [E1] with 𝒳 = BSE ✔ | DERIVED | — |
| L15 | WP4 | §4.2, [4.1]–[4.2] | (3.3) → (5.4)/(5.5) → GRPA → bare bubble → Lindhard ✔ | DERIVED (✎ GRPA); vertex size E | 𝔤_I closed form new |
| L16 | WP4 | §5.2, [5.1]–[5.2] | (3.3) → (5.3)/(5.4), ε_bg in the total ε ✔ | DERIVED; ε_bg² statement CONDITIONAL | R7 FT check (OW4-2) |
| L17 | WP0 (WP1) | WP0 §9.2; WP1 L17 | (9.3)–(9.6); ε(q,0) ≥ 1 by WP1 [E3] ✔ | DERIVED at RPA+LFE | beyond RPA [E] Si/Ge, [C] general |
| L18 | WP2 | §9 L18, (6.1)–(6.2) | n_A = 1 on S^{GS}_κκ ✔ | DERIVED | nuisance form WP6 (5.1′) |
| L19 | WP2 + WP1 | WP2 §8, §9; WP1 §6, L19 | (3.3) full q, (8.1); even ℓ, ℓ = 4 first ✔ | DERIVED (✎ P,T-broken) | consistent with WP4 [3.1], WP6 (1.5) |
| L20 | WP5 | §6.1 | (3.4) GS imp → (W9) → (W3) first moment ✔ | DERIVED (chain); ½εS_e not reproduced | Born invalid at keV, S_e ∝ v a fit |
| L21 | WP5 | §6.2 | (W6) → (W5) → (W3) + 7 truncations ✔ | DERIVED (✎ photon-seed fit) | A-units, \|M\|² discrepancies |
| L22 | WP5 | §6.3 | (W9) → (W3) → (W10) ✔ | DERIVED | E_st ≠ E_d; 2301.06592 ionization = E_d not a limit |
| L23 | WP5 | §6.4, (W14) | second moment of (W3) with (W4) ✔ | DERIVED (exact given (W4)); F ≈ 0.121 [E] | F_meas thinning corrects R&K App. A |
| L24 | WP6 | §2, (1.4), (1.6) | (3.4) → (9.1) → (I) → SHM → 1509.01598 Eq. (17) ✔ | DERIVED | — |
All 26 entries have an owner, a v2 location and a chain in v2 numbers; none is missing.

---
## 3. Interface quantities (brief item 1)
| Quantity | Defining eq. | Users (v2) | Result |
|---|---|---|---|
| Master formula | WP0-v2 (3.3)–(3.4) | WP1 L1–L3, WP2 (5.3)/L6, WP3 (M.5)–(M.6), WP4 [3.1], [7.2], WP5 (W6), WP6 (1.2)/(1.4) | consistent; (1.4)'s 1/(4π²) reproduces (9.2) |
| S, R, L, ε; S ↔ L; FDT | WP0-v2 (3.1)–(3.2), (4.1), (5.2), (9.3) | all | consistent (WP5 writes S_cc = WP0 S_zz, I8; no content change) |
| Screening | WP0-v2 (5.3)–(5.5) | WP1 [E1], §2; WP2 (4.2), (4.4); WP4 [4.1], [5.1]; WP5 (W1); WP6 §5.2 | consistent (j_T via LFE, spins via f_xc^T everywhere) |
| Theorem D sectors | WP0-v2 (6.1), §6.2 | WP1 1.1, WP2 (1.1), WP3 (W.1), WP4 §8 (gapless D-g), WP5 §3.1, WP6 (4.2) | consistent; PSD per sector only in the window, used by all |
| Final-state-resolved response → WP5 | WP0-v2 (7.1)–(7.3) | WP1 [E2], WP3 (W.1), WP4 [4.6], [6.1], WP5 (W5)–(W6), WP6 (1.7), §7.1 | consistent; retarded out-state weight adopted by all (F1 closed); WP5 text stale (A11) |
| Multiphonon S_NN → WP5 | WP2 (3.2), (3.5), (3.6), (5.3) | WP5 (W9), §3.1; WP6 §5.2 | consistent; ω′ < 0 = absorption and drag-mass subtraction applied |
| M̃ | WP0-v2 (5.7) | WP3 (M.13) (identical), (M.14) = WP0-v2 (5.6) ((2q²/e²)·8π²α/Ωq² = 4π/Ω) | consistent |
| Halo factor | 𝒢 → η/(2q) under (I) | WP0 (9.2), WP1 L1, WP2 (5.3), WP3 (M.6), WP6 (1.3)–(1.4) | consistent |
| Nuisances → WP6 | WP0-v2 (8.1)–(8.3) = WP6 (5.1)–(6.3) | WP1 §1.5 (BSE M+A), WP2 (6.1′), WP3 p_on, WP5 §8 | consistent except A1 (p_on) and A12 (names; θ_𝔉, θ_Eg rows) |

---
## 4. Owed corrections (brief item 4)
| CORRECTIONS § | Target | Status in v2 |
|---|---|---|
| §0 global renames | all | applied, except: χ in WP3 frame theorem (A6), κ₃ in WP0 (4.7) (A2), X2 Λ in WP3 §M10 (A6) |
| §1 D1, §2 D2, §3 REF-A/B, §4 X1 | carried by WP3 Part I | all applied (WP3 #1–#27) |
| §5 X2 | WP0, WP1, WP3 | external weight resolved by derivation (WP0 CC-1, WP1 §1.3, WP3 C17); δ_pair [C] kept; renames applied except A6 |
| §6 WP0 | WP0-v2 | 38 applied; #22 contested in part with an argument (CC-1), then **accepted** by WP1-v2 and confirmed by WP3-v2 → closed |
| §7–§12 | WP1–WP6 | applied (32, 36, 63, 42, 27, 29 rows); 0 contested |
| §13 O4 | via WP0 §6.2, WP3 §M4–§M5 | applied (DC, scope of Z + fp = 1, P(N_eh\|q,ω)) |
| §14 L1.md | — | missing (no revision exists) → A19 |
| §15 SOTA | coordinator | missing → A17 |
| §16 CONTROLS, LIMITS, README | coordinator | C7 sentence deleted (applied); C4, LIMITS, README missing → A16, A18 |
| WP0-v2 flags F1–F11 | REV agents | F1 accepted (WP1, WP3); F2 (WP5 §1.1(c)); F3 consistent; F4 closed at moment level; F5 WP4 §8; F6 done; F7 (WP3 W.4c); F8 bounded (WP5 W15, WP3 §M4; A10); F9 (WP6 §7.3); F10 (NOTATION row exists); F11 everywhere |

---
## 5. Duplicated or contradictory claims (brief item 5)
- **Anisotropy and modulation (WP1 §6, WP2 §8.2, WP3 L7b(v), WP6 (1.5), WP0 (4.3)/(9.1)(δ), WP4 [3.1]).** No contradiction. The ELF has no odd ℓ (TR) and no
  ℓ = 2 (cubic), so ℓ = 4 comes first. The harmonic incoherent multiphonon S of cubic-site crystals is exactly isotropic. The soft-limit (dipole) Migdal daily
  modulation vanishes in Si/Ge/GaAs. P,T-broken targets have odd ℓ, kept by WP6 (1.5) and the library. WP1 IF-7 and WP2 §8.2 cross-cite. Different objects; the claims are consistent.
- **Migdal (WP0 §6.2(ii)–(iii), dictionary, (4.6c), (4.7); WP2 (3.4), (5.2), (5.2′); WP3 J3, J4, J7, J8, L7a–d; WP5 §3.1).** The boost mass (m_A for an atom; M_κ + δM_κ in a crystal),
  E^{Mig}_1 = q·δM_κ·q/2M_κ², the L7d split, the J7 negative ω_e moment, the double-counting rules (a)–(e) and the drag-mass subtraction in the WP5 seed are
  stated identically in all packages. The third moment is consistent (§6 S1). Only the stale WP0 wording remains (A2).
- **PAER (WP0 (5.5)–(5.7′), WP3 Part I, WP6 §5.2).** Same M̃, four classes, O(ω_Q²/E_g²) DFPT error, window, interim [0.5, 1.2]. The open point is A1.
- **Numbers repeated across packages:** exciton thresholds (A7), impulse onset (A8), Si threshold mass (A9), Fano-term size (A10). All other repeated numbers agree:
  m_min 0.319/0.285 MeV, δM/M ≤ 2.7×10⁻⁴, E_R,th 375/465 eV, \|f_crys\|² dictionary, profile ×1.28 (linear) and envelope ×2.0 at δ = 0.5, ×1.8 = 2.0/1.112 (checked).

---
## 6. SOTA items marked "R7 ITEM" or "for the audit"
- **S1. 𝔨₃ normalisation, WP2-v2 vs WP3-v2: RESOLVED, no mismatch** (sympy, exact). WP0-v2 (4.7) at q → 0 gives 𝓜³_eκ = −q²Z_κe²𝓃_κ𝓃_e(R_κ)/(3m_eM_κ).
  WP2-v2 (5.2′) gives 𝔨₃ = (q²/2M_κ²)Z_κe²𝓃_e(R_κ)/3 per nucleus. For a density the moment matrix doubles, 𝓜³_κκ = 2𝓃_κ𝔨₃ (only 𝔨₃ carries V_eN).
  Then **𝓜³_κκ\|_{V_eN} = −(m_e/M_κ)𝓜³_eκ (WP2's statement) ⇔ 𝔨₃ = −(m_e/M_κ)𝓜³_eκ/(2𝓃_κ) (WP3's) ⇔ 𝓜³_eκ = −2𝓃_κ(M_κ/m_e)𝔨₃ (WP3 J8)**:
  all three hold identically. WP2-v2 speaks of the κκ *moment*; SOTA line 220 paraphrased it as "𝔨₃", which created the apparent mismatch. Action: fix SOTA
  line 220 (A17), drop "normalisation to check in R7" from WP3 IF-2, and close WP0 F4/OW0-8 (A2). What remains of F4 is numerical (𝔨₃^X from the all-electron
  (W.5); spec WP3 G6), not a consistency item.
- **S2. Stale WP5-v2 I1/I3 flag text: CONFIRMED stale,** together with I4, I5, I7 (A11). Route: WP5 erratum at R7, wording only.
- **S3. WP6-v2 REFEREE ITEM, hypothesis (P) in (4.2):** consistent with WP0-v2 §6.2(i) and O4 (the sufficiency argument in WP6 is sound: where per-sector PSD
  fails, P(i|Λ) is constant over the split). Route: R7 referees (OW6-6), with O4's Γ_Λ₀/δ map.
- **S4. F1 / GaAs external weight ("pending R7"):** the packages are consistent (WP0 C10, WP1 C4, WP3 C17 independently). Route: R7 referee confirmation only (OW0-7, O-WP3-7).
- **S5. L16 ε_bg² claim (OW4-2, HIGH PRIORITY):** correctly carried as conditional in WP4 and in WP0 (9.7). Route: R7 full-text referee.
- **S6. CORRECTIONS §7 2607.06005 "dipole" FT check:** done by WP1-v2 §6.2 (quote with section). Closed (A15 for WP6's tag).
- **S7. Si window Umklapp re-check (WP3 §M9, OW0-12) and X2-N1…N4:** numerics, not consistency. Route: deferred numerics.
- **S8. NOTATION flags (WP0 F10 done; WP1 IF-9; WP2 IF-5/6; WP4 I6/I7; WP6 IF6-2/3):** route to the NOTATION v4 pass (A14, A20).

---
## 7. Gap coverage (brief item 6)
| Gap | Owner(s) | Closed with formula + specification | Exact remaining gap recorded |
|---|---|---|---|
| G1 near-gap yield | WP5 | (W1)–(W8), (W15); spec §2 | R1 (BTE ii definition), R2 ((R-k) error), R7 (𝔉 export) |
| G2 phonon-assisted edge | WP3 | (M.1)–(M.14), (W.4), §5 hybrid; spec §M10, §8 G2 | X2-N1…N4 (pair channel); Umklapp re-check of the Si window; onset A1 |
| G3 NR partition | WP2 + WP5 | WP2 (3.5), (3.6), (5.3); WP5 (W9)–(W11); spec WP2 §10, WP5 §3.4 | WP5 R3 (TDDFT close-collision kernel) |
| G4 error bands, conventions | WP6 | (5.1)–(5.3), (5.1′), (6.1)–(6.5), library §7 | WP6 (7.5)(i)–(iv) |
| G5 many-body beyond RPA | WP1 (+WP3) | [E1], [E7], [E8]; spec WP1 G5; WP3 (W.14) | finite-q BSE beyond TDA never run (WP1 §10.1, WP3 O-WP3-2) |
| G6 Migdal consistency | WP3 | (W.1), (W.5), J1–J8, N1–N5; spec §8 G6 | numerical δM_κ, E^{Mig}_3 (O-WP3-3) |
| G7 core / relativistic | WP1 | §5, [E11]; spec G7 | no 4-component no-pair crystal code (WP1 §10.2) |
| G8 halo at the edge | WP6 | (3.1)–(3.4), (4.1)–(4.2) | G8′: directional halo-independent bound (OW6-1) |
| G9 SC / films | WP4 | [4.1]–[4.6]; specs §4 | RG1, RG2, RG7 |
| G10 non-density operators | WP1 | §2.6, [E4]–[E6]; spec G10 | LFE size on j_T (WP1 §10.4) |
| G11 anisotropy | WP1 + WP2 (+WP6) | WP1 §6.1, WP2 (8.1)–(8.2), WP6 (1.5); specs G11 | G8′ for directional bounds; P,T-broken targets: WP4 §3 spec |
| G12 unmodelled channels / defects | WP4 + WP5 (+WP3) | WP4 [2.3]–[2.5], [6.1]–[6.3], [7.2]; WP3 (W.13); WP5 (W12) | WP5 R4 (avalanche), WP4 RG3, RG5; ER defect creation in ionic targets (WP5 §4) |
| G13 anharmonicity | WP2 (+WP6) | (6.1), (6.1′), (6.2); WP6 (5.1′); spec G13 | WP2 gap 5 (non-perturbative, light atoms) |
| Cat. §12.1 PA scattering | WP3 | Part I | as G2 |
| Cat. §12.2 PA absorption | WP3 | (M.17), L9b T-transfer | data at mK |
| Cat. §12.3 excitons | WP1, WP3 | [E7], [E8], [E10], (W.14) | Frenkel / self-trapped (NaI) (WP1 §8) |
| Cat. §12.4 NR brems; exo into modes | WP3, WP4 | (W.13); [7.1]–[7.2] | — |
| Cat. §12.5 ER defects; NV / colour centres | WP5, WP4 | WP5 §4 (bound 0.78 meV); WP4 [6.3] | ionic-target bond breaking; RG5 |
| Cat. §12.6 two-magnon; CD | WP4 | [2.3]–[2.4], [3.3] | RG3, RG4 |
| Cat. §12.7 finite-T / ZPR | WP3 | (W.11)–(W.12), §M5 | non-adiabatic AHC (small, [E]) |
Every gap is either closed with formula + specification or recorded as an exact remaining gap; none is unassigned.

---
## 8. Catalog coverage (CATALOG-A; coordinator addition)
A = explicit formula derived in a v2 package, or the gap closed with a formula plus specification · B = master formula only (no dedicated sector treatment or target
model) · C = out of scope by design (readout, transduction, experiment design, macroscopic electrodynamics) · D = not covered.
| # | Process | Cl. | Where / why |
|---|---|---|---|
| E1 | valence e–h | A | WP1 [E1], [E2], [E12] |
| E2 | core ionization | A | WP1 §5, [E11], G7 |
| E3 | general DM–e operators | A | WP1 §2, [E4]–[E6], L3 |
| E4 | Wannier excitons (BSE) | A | WP1 [E7], [E8] |
| E5 | Frenkel excitons, organics | B | no molecular-crystal model; WP1 §8 lists Frenkel/NaI as remaining |
| E6 | dark/indirect excitons, exciton–phonon | A | WP1 §3.2–§3.4, [E10]; WP3 (W.14) |
| E7 | bulk plasmons | A | WP1 [E9], L11 |
| E8 | exotic/low-D plasmons | B | only HEG/RPA treated |
| E9 | heterostructures, layered | B | WP4 slab [4.5] only for film geometry |
| E10 | quantum dots | B | — |
| E11 | Dirac/Weyl | A | WP4 [5.1]–[5.2] |
| E12 | graphene/CNT | B | WP4 treats 3D Dirac only |
| E13 | Cooper-pair breaking | A | WP4 [4.1]–[4.2], [4.6] |
| E14 | shallow dopants | A | WP4 [6.1]–[6.2] |
| E15 | colour centres (DM–e) | A | WP4 [6.3] |
| L1 | single acoustic phonon | A | WP2 (2.2) |
| L2 | optical/LO phonon | A | WP2 (4.2)–(4.3) |
| L3 | multiphonon | A | WP2 (3.2), (3.5) |
| L4 | anharmonic | A | WP2 (6.1)–(6.2) |
| L5 | coherent → incoherent | A | WP2 (2.3)–(2.4), §3.3 |
| L6 | impulse NR | A | WP2 (5.1)–(5.3) |
| L7 | spin-dependent nucleon → phonons | A | WP2 (7.1) |
| L8 | phonon/NR daily modulation | A | WP2 (8.1)–(8.2) |
| L9 | chiral phonons | B | WP4 §3.2 names S^A_{s,κ} only |
| L10 | amorphous phonons | B | WP2 gap 6 (configurational average not done) |
| L11 | solid helium | B | — |
| S1 | magnon scattering | A | WP4 [2.1]–[2.2], [2.4] |
| S2 | boson absorption into magnons | B | WP0 (3.5) + WP4 [2.2]; Kittel/in-B modes not derived |
| S3 | axion quasiparticle | C | axion electrodynamics (macroscopic) |
| S4 | nuclear-spin precession | D | coherent classical-field (wave) regime, outside the golden-rule rate |
| S5 | axion–nuclear-spin phonons | B | WP2 (7.1) gives S_II; absorption form not written |
| S6 | spin response from neutron data | B | master formula with measured S |
| S7 | spin-dependent DM–e | A | WP1 [E6], §2.4 |
| S8 | chiral phonons, SMMs | B | — |
| S9 | magnetoelectric axion coupling | D | coherent classical field (Landau theory) |
| D1 | Frenkel pairs, E_d | A | WP5 (W10), §3.2 |
| D2 | colour-centre creation | B | WP5 §4: candidate-dependent, not computed |
| D3 | NV damage-track spectroscopy | D | non-perturbative track physics plus strain readout |
| D4 | paleo-detector tracks | D | non-perturbative track formation, multiple scattering |
| D5 | bond breaking, molecular solids | B | WP5 BO-MD logic only |
| X1 | atomic Migdal | A | WP3 L7a |
| X2 | crystal Migdal (ELF) | A | WP3 L7b |
| X3 | Migdal with phonon final states | A | WP3 L7c, (W.5) |
| X4 | non-adiabatic BO derivation | A | WP0 §6.2(ii); WP3 (W.1) |
| X5 | phonon-mediated Migdal | A | WP3 L7d |
| X6 | Wannier/bremsstrahlung Migdal | B | contained in (W.5), not discussed |
| X7 | anisotropic Migdal | A | WP1 §6.1(iii), WP2 §8.2, WP3 L7b(v) |
| X8 | Migdal excitation | B | (W.5) covers bound ω_e; no target treatment |
| X9 | NR bremsstrahlung | A | WP3 (W.13) |
| X10 | Migdal in absorption | B | WP3 §4(d) covers only the electronic 𝒯_e channel |
| X11 | Migdal measurement | C | calibration design (WP3 N3 gives the fitting rule) |
| A1 | dark photon/ALP/scalar on e | A | WP0 (3.5)–(3.6); WP3 L9b |
| A2 | absorption in SC/metals | B | WP4 §4.3(ii) mentions Holstein, no formula |
| A3 | PA absorption, indirect gap | A | WP3 (M.17), L9 |
| A4 | single-phonon absorption | B | WP0 (3.5) with WP2 (4.2); not written out |
| A5 | polaritons / g_aγγ in B₀ | A | WP0 (2.9) |
| A6 | dopant absorption | B | WP4 [6.1] at k ≈ 0, not written |
| A7 | amorphous phonon absorption | B | as L10 |
| A8 | qubit/device absorption | C | circuit-QED transduction |
| A9 | piezo BAR/hBAR | D | coherent classical strain field (wave regime) |
| A10 | fermionic absorption | D | missing operator class (DM → ν, relativistic final state) |
| A11 | pair absorption, dark Compton | D | two-insertion processes, beyond single-vertex Born |
| A12 | axion → photon in materials | C | macroscopic electrodynamics |
| R1 | scintillation | C | readout (WP5 only books E_esc) |
| R2 | organic/liquid scintillator rates | C | readout |
| R3 | Cherenkov/transition radiation | C | background/readout |
| R4 | athermal-phonon calorimetry | C | readout (WP5 ℋ, WP4 t_esc are inputs) |
| R5 | ionization yield / ε_eh | A | WP5 (W3)–(W8), (W14); L21, L23 |
| R6 | TES/KID/SNSPD/qubit | C | readout |
| R7 | phononic-crystal / vdW / JJ sensors | C | readout |
| R8 | halo-independent sensor analysis | A | WP6 (4.1)–(4.2) |
| I1 | exothermic DM | A | WP0 (2.1); WP4 [7.1] |
| I2 | inelastic DM, EM de-excitation | D | DM-side radiative process, no target response |
| I3 | inelastic DM–e | B | WP0 (2.1) with Δ_χ, any S |
| I4 | exo/inelastic into collective modes | A | WP4 [7.2] |
| I5 | boosted/solar-reflected DM | B | WP6 (1.2) for any f; no dedicated reach |
| §10(i) | scalar absorption with mixing | A | WP0 (3.5)–(3.6); WP3 L9b(d) (PA 𝒯_e) |
| §10(ii) | oscillating constants, resonators, clocks | D | coherent classical field |
| §10(iii) | quadratic coupling, random media | B | master formula at q → 0; amorphous not modelled |
| §10(iv) | scalar–nucleon Migdal absorption | B | as X10 |
| §11.1 | phonon-mediated Migdal | A | WP3 L7d |
| §11.2 | Migdal + phonon final states | A | WP3 (W.5), L7c |
| §11.3 | PA absorption | A | WP3 L9, L9b |
| §11.4 | PA electron scattering (PAER) | A | WP3 Part I (M.1)–(M.14) |
| §11.5 | plasmon-mediated ER | A | WP1 [E1], [E9] |
| §11.6 | exciton-mediated ER | A | WP1 [E7] |
| §11.7 | exciton → scintillation | C | readout (creation step is A, E4) |
| §11.8 | defect → stored energy → deficit | A | WP5 §3.2, (W11) |
| §11.9 | scattering + mediator absorption | D | two-step, beyond single Born |
| §11.10 | finite-T / ZPR on thresholds | A | WP3 (W.11)–(W.12), §M5 |
| §11.11 | PA exciton creation | A | WP3 (W.14) |
**Counts (91 rows):** A = 45, B = 25, C = 11, D = 10.
