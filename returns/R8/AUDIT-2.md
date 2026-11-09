# R8 / AUDIT-2: cross-package consistency of the v3 packages

Brief: briefs/R8/AUDIT-2.md. Read: returns/R8/WP0-v3 … WP6-v3 (every interface-flag section), CONVENTIONS.md, NOTATION.md (v4), LIMITS.md, CONTROLS.md,
state/CORRECTIONS.md, state/SOTA.md. referees/R8/ not read. No file other than this one edited. Sympy checks: scratchpad `a2.py` (𝔨₃/J8/(4.7′)/(5.2″)
identities exact; window and threshold numbers re-evaluated). Package equation numbers are the v2 numbers kept in v3 (every package says so).
**Result: 3 blocking defects, 33 minor.** All interface quantities agree in formula except the three blocking items; the M1 window is reconciled (§5).

---
## 1. Defect table
| ID | packages | location | defect | proposed resolution | severity |
|---|---|---|---|---|---|
| B1 | WP0 ↔ WP6, WP3 | WP0-v3 (8.1), (8.2), (5.7) "Sizes" | (8.1) states type M "PSD for all θ" and (8.2) "positivity automatic for M and A"; both false for the matrix S_ab (WP6-v3 C22 counterexample; A PSD only for PSD Δ, WP6 C23). (8.1) and (5.7) still give the PAER A-range [0.5, 1.2], which assumes the δ_LF, δ_pair signs that WP0 itself tags [C]; WP3-v3 IF-10 and WP6-v3 (5.2) use [0.4, 1.8] (median 0.85, σ_ln 0.75). WP6 IF6-4, IF6-14, IF6-15 unapplied. The nuisance structure feeding WP6 is contradictory | WP0 erratum: (8.1) = WP6-v3 (5.1) (M on scalars / PSD geodesic; A on PSD increments; L, T types); (8.2) positivity sentence as WP6 (5.3); [0.5, 1.2] → [0.4, 1.8] [E/C] in (5.7) and (8.1); CONVENTIONS §11 and §13 item 13 likewise (§6) | blocking |
| B2 | WP0 ↔ WP1 | WP0-v3 §9.2 (iii) bullet 1; L17 status | WP0 keeps "beyond RPA it needs 1 − f_HxcR⁰ > 0". WP1-v3 §1.4 / [E3] (IF-12) gives a counterexample to that condition and derives (−R⁰)^{-1} + f_xc > 0 (proper R̃ NSD; both R7 WP1 referees: f_xc, not f_Hxc). WP0 owns L17, so the LIMITS entry rests on a refuted hypothesis | WP0 erratum: replace the condition by WP1 (1.4′); keep "[E] true for Si, Ge"; LIMITS L17 row per §2 |
| B3 | WP0, WP3 ↔ WP2, WP5 | WP0-v3 §6.2 (iii) and double-counting rule (a); WP3-v3 J3 last sentence, N1 | Multiphonon/Migdal moment bookkeeping. WP0 "X carries 𝓜¹^{(e)}_κκ = 𝓃_κq·δM_κ·q/M_κ², GS the rest" and WP3 N1 "overcounts 𝓜¹ by exactly 𝓃_κq·δM_κ·q/M_κ²" omit the nuclear recoil carried by X events. WP5-v3 §3.1 (WP5v3-C20b; IF-R8-1) and WP2-v3 IF-2: 𝓜¹_X = E^{Mig}_1 + P_Mig q²/2M_κ, GS = (1 − P_Mig)S^{GS} with M_κ + δM_κ. Exact statements disagree (size ≲ 1% at keV) on the S_NN handed to WP5 | WP0 (iii), rule (a) and WP3 J3/N1: "the electronic-label moment 𝓜¹^{(e)} is not the X-sector moment; 𝓜¹_X = 𝓃_κ[E^{Mig}_1 + P_Mig q²/2M_κ]; overcount of 𝓜¹ = 𝓃_κ(E^{Mig}_1 + P_Mig q²/2M_κ)"; cite WP5-v3 §3.1 |
| m1 | WP1 ↔ WP3, WP6 | WP1-v3 §3.4 last bullet, §3.7, IF-6 table | Si M1 lower edge 0.338 MeV (zone-boundary TA, 18 meV) | 0.333 (exciton replica) – 0.337 (continuum) MeV [E] (WP6-v3 (3.1′), §5 below) | minor |
| m2 | WP6 ↔ CONTROLS, WP3 | WP6-v3 (3.1′) table row 1, consequence (i); CONTROLS C5 | "0.333 MeV floor unattained, S̄ vanishes at ω = E_g". The exciton replica E_x + ω_TA(Q*) = 1.1688 eV < E_g (ω_TA 13.5 < E_x^b 14.7 meV) gives 0.3328 MeV < 0.3332 (sympy); the true floor is 2E_x/v_max² = 0.329. C5 "no PAER below E_g + min ω" is false for replicas | WP6: floor at E_g is not a floor for excitonic replicas; CONTROLS C5 per §6 |
| m3 | WP6 ↔ WP3 | WP6-v3 (3.1′) consequence (ii), IF6-11 | says WP3's 0.333 "rested on the acoustic Q* → 0 infimum"; WP3-v3 §M9 bullet 1 actually gives 0.336–0.338 (free pairs) and 0.333 (replicas); the infimum is WP3's C5 fixed-q statement | WP6 wording; no number changes |
| m4 | WP0 ↔ WP3 | WP0-v3 (5.5) header, (5.6) "RPA/ALDA" | WP3-v3 §M7 (IF-12): (M.13) is [D] at RPA/TDH; ALDA adds a k_xc source term | WP0: "RPA/TDH; ALDA adds the k_xc term (WP3-v3 §M7)" |
| m5 | WP0 ↔ WP3 | WP0-v3 §6.2 (iv) "Si Γ/δ ≈ 0.02–0.6" | WP3-v3 §M4: 0.007–0.2 at δ₀ = 0.3 eV (0.02–0.6 was δ₀ = 0.1 eV, which violates δ₀ ≫ ω_max) | WP0 adopt WP3 values; WP5 IF-R8-10 (GaAs map) stays an open item |
| m6 | WP0 ↔ WP5 | WP0-v3 (7.1) plasmon sentence | WP5-v3 IF-R8-3: an undamped RPA pole (metals, q < q_c) is a final state 𝔱 = pl | WP0 (7.1) + CONVENTIONS §13 item 21 exception |
| m7 | WP0 ↔ WP4 | WP0-v3 §6.2 scope paragraph | still "[C], owned by WP4"; WP4-v3 I1: Theorem D-g (a) [D given U_qp and (G5)], bound [8.1] | WP0 cites WP4-v3 §8 with (G5) |
| m8 | WP4 ↔ WP0 | WP4-v3 §8 (e) | "coincide with GS/X0/X+ to O(κ_BO^{n+1})"; WP0-v3 G10: O(κ_BO^{2(n+1)}) | WP4 erratum |
| m9 | WP4 ↔ WP0 | WP4-v3 §8 hypotheses (G1) | G9 (magnetic insulators → gapless-target theorem) not taken up: D-g covers fermionic QPs only | record as WP4 open item (= WP0 OW0-17); no claim change |
| m10 | WP0 ↔ WP2, WP4 | WP0-v3 Table 6.1 and the paragraph after it | not updated for WP2 IF-3 (multi-site |c_κ|²/M_κ-weighted truncation loss), IF-10 ("incoherent accurate below q_BZ" is [E]; (2.4) Bravais only, q ≫ max(n_ph,2W)q_BZ), WP4 I12 (Δ_BCS/v_Fq first-order), I16 (Q₊ < 1 only for m_χ ≲ 0.80 MeV) | WP0 erratum, text only |
| m11 | WP6 ↔ WP2 | WP6-v3 (5.2) "Phonon order" row | single-site P[Pois(2W) ≥ N]; WP2-v3 (3.4″) weighted mean | cite (3.4″) |
| m12 | WP0 ↔ WP1 | WP0-v3 (5.3) spin bullet | WP1-v3 IF-13: leading beyond-IP spin term is the triplet W^{scr} ladder, R̃_s ≡ 4R_{s^zs^z}; WP0 keeps f_xc^T only (WP6 already applied IF-13) | WP0 (5.3); CONVENTIONS §7 (§6) |
| m13 | WP4 ↔ WP1 | WP4-v3 (1.2) | same spin-screening wording as m12 | WP4 wording |
| m14 | WP1 ↔ WP0 | WP1-v3 L17 (d) | −0.18%/−0.58% (mass-velocity only); WP0-v3 G4: −0.23%/−0.73% with orbit–orbit (WP1 §5.3 states the scope) | L17 (d) quote the total |
| m15 | WP3 ↔ WP5 | WP3-v3 §M4 (iv″b) and F8 paragraph | c_ν^F = Im(ρ*a^{off}) and bound 0.11Γ/δ; WP5-v3 (W17), IF-R8-4/5: dimensionless Kramers-summed c^F, worst case 0.3Γ/δ (WP6 IF6-8 adopted) | WP3 wording; NOTATION 𝔉 row (§6) |
| m16 | WP4 ↔ WP6 | WP4-v3 [3.2′] text, I4 | "ℓ = 1 still the leading odd harmonic"; WP6-v3 (1.5), C28: never for cubic G_eff (3 for T, T_d; 9 for O); ℓ = 1 only for polar groups (IF6-12) | WP4 adopt WP6 |
| m17 | WP0 ↔ WP4, WP6 | WP0-v3 (4.3) 𝐁^{NR}_{αβγ}; WP4 [3.2′], WP6 (1.5) b^{NR}_{αβγ}/ω² | one object, two names and normalisations | NOTATION: one row (𝐁^{NR} ≡ b^{NR}/ω²) |
| m18 | WP2 ↔ WP3 | WP3-v3 §2 L7b validity | Ge x_R = 1 at 58 keV (ω̄ = 25 meV) but impulse onset 112 keV; WP2-v3 L5: 55.8 keV (23 meV), 2× = 112 (sympy: 55.8/58.2) | WP3 → 55.8 keV (23 meV) |
| m19 | WP1 ↔ WP3 | WP3-v3 §M3 (c) | Si M_x = m_l + m_hh ≈ 1.41 m_e (Q_w = 0.33 Å⁻¹); WP1-v3 §3.4: 1.19 m_e (gives Q_w = 0.31) | one mass set [UNVERIFIED both]; quote Q_w ≈ 0.31–0.33 |
| m20 | WP5 ↔ WP0 | WP5-v3 §1.1 (c) | "four-class classification"; WP0-v3 G14: three classes + ionic phonon-bridge insertions (WP5 adds the caveat sentence) | wording only |
| m21 | WP5 ↔ WP0 | WP5-v3 (W6) note, §1.3 P(N_eh) | keeps "tr[𝔇S]" meaning Σ𝔇_abS_ab | write tr[𝔇ᵀS] (G1) |
| m22 | WP0 ↔ WP4, LIMITS | WP0-v3 (9.7) L16; LIMITS L16 | "κ² claim pending referee FT check" / "CONDITIONAL"; WP4-v3 §5.3: REFEREED R×2, plus absorption ×ε_bg (§5.5, I10) | WP0 (9.7); LIMITS row (§2) |
| m23 | WP0 | WP0-v3 §12 | OW0-7 listed twice (open and CLOSED) | delete the first |
| m24 | WP0 ↔ WP3 | WP0-v3 §6.2 (ii) "δM/M ≤ 2.7×10⁻⁴" | WP3-v3 IF-13: [E] estimate, not a bound (B-21) | drop "≤" |
| m25 | WP0 ↔ CONVENTIONS | CONVENTIONS §7 line 106 | "𝒪_i (i = 1…15)" while WP0-v3 G2 excludes 𝒪₂ from the 16-row basis | §6 |
| m26 | WP1 | WP1-v3 §3.7 | bare ε ≡ ω − E_min(q) (bare ε is the dielectric function, NOTATION §D) | rename ε_ex |
| m27 | WP3 | WP3-v3 (M.4) 𝒫_± | collides with 𝒫₀, 𝒫_⊥, 𝒫_GS (projectors) | rename (e.g. w^{EPW}_±) |
| m28 | WP4 | WP4-v3 I17 Π_γ | collides with Π^γ (photon self-energy) | rename |
| m29 | WP6 ↔ NOTATION | NOTATION §M row "k_δ, W_Lam" | WP6-v3 renamed W_Lam → w_δ, δ → δ_θ, K → 𝐊_pk (IF6-2) | §6 |
| m30 | WP2 ↔ NOTATION | NOTATION δρ_κ row | WP2 IF-11: "electronic charge-response vector (core + valence)" | §6 |
| m31 | WP0, WP3, WP4, WP6 ↔ NOTATION | new-symbol rows | R^{phys} (G11), K_pk, d_K, Q_w, p̄_on, γ_c, E^{PA}_th, m_χ^{ZP}, ϖ_II, WP4 I17 list, WP6 §15 list not in NOTATION | NOTATION v5 pass |
| m32 | LIMITS, SOTA, CONVENTIONS, CONTROLS, NOTATION | coordinator files | superseded values (listed in §6) | coordinator |
| m33 | WP1 ↔ WP0 | WP1-v3 §2.2 | G13 applied as SOC = 0 only; H_hf and B₀ off not stated | add the two conditions |

---
## 2. LIMITS status table (owner, v3 location, chain with current equation numbers; all chains still close)
Status key: REF = R×2 done in R7 on v2; v3 corrections CLAIMED pending R8 verification. "Note" = replacement for the LIMITS note column.
| # | Owner | v3 location | Chain (eq nos) | Status | Note / action |
|---|---|---|---|---|---|
| L0 | WP0 | §9.1 | (3.3) → (9.1) → (9.2), 𝒢 = η/2q ✔ | DERIVED, REF | — |
| L1 | WP1 | §7 L1 | WP0 (3.3), (9.1), (9.2) → [E1] IP → [E12] ✔ | DERIVED; SOTA #7 CROSS-CHECKED | add: pointwise 1/\|ε\|² 0.117/0.451 ≠ rate ratio ×1.4–2.5 (WP1 IF-16) |
| L2 | WP1 | §7 L2 | (3.3) → (5.5)(i)/(ii) → (5.4) → (4.1) ✔ | DERIVED (✎ condition), REF | — |
| L3 | WP1 | §7 L3 | (3.3) → (5.3) → §2.1–2.6, [E4]–[E6] ✔ | DERIVED (✎), REF | replace "O₈ conservative ×O(10)" by "≥ 12× (IP 20–30), factor UNRESOLVED; 𝒪₂, 𝒪₅ also; 2 independent Catena responses in Si/Ge" (IF-14) |
| L4 | WP2 | §9 L4 | (3.3) → (1.1) → (2.2) → (5.4) ≡ (4.2) → (4.3) ✔ | DERIVED, REF | — |
| L5 | WP2 | §9 L5 | (1.1) → (2.1) → (2.3) [(2.4) only for q ≫ max(n_ph,2W)q_BZ, plus κ ≠ κ′ pairs] → (3.2) → Poisson ✔ | DERIVED (✎ control), REF | add the (2.4) qualifiers (WP2 IF-10) |
| L6 | WP2 | §9 L6 | self part → (5.3) → WP0 (3.4), (9.1) ✔ | DERIVED (✎), REF | 𝔨₃^{GS} computed directly, never 𝔨₃ − 𝔨₃^X |
| L7a | WP3 | §2 | (W.5) T0 + T6, boost m_A ✔ | DERIVED, REF | — |
| L7b | WP3 | §2 | (W.5) T0–T5 imp, soft → 4α ✔ | DERIVED, REF | impulse onset 91.5/112 keV (m18) |
| L7c | WP3 | §2 | (W.5) T0–T4 ≡ 2210.06490 Eq. (3.8) ✔ | DERIVED, REF | replace "Eq. (4.7) misprint" by "Eq. (3.11) sign misprint; 1/m_N misplaced (4.6)→(4.7); (4.8) 2× UNRESOLVED; correction ≲ 10⁻³" (IF-15) |
| L7d | WP3 | §2 | (W.5) off-shell phonon; n = 0 → X0, n ≥ 1 → X+ ✔ | DERIVED (✎), REF | — |
| L8 | WP3 | Part I §M1–M10; Part II §3 | (M.1)–(M.14), DC outside (M.9) ✔ | DERIVED, REF (R2 core; R7) | interim factor **[0.4, 1.8]**; p̄_on Si 3 (LA kink 4), Ge 3; window per §5 (IF-5, IF-8, IF-10) |
| L9 | WP3 | §4, (M.17) | L8 → q → 0 (C1) → ε^L = ε^T ✔ | CROSS-CHECKED (FT prefactor) | — |
| L9b | WP3 (WP1 §2.5) | §4 | WP0 (3.5)–(3.6), (2.9) ✔ | DERIVED + caveats | 1608.01994 O(1) only within ≈ 20–25 meV (IF-14); Dirac absorption sources ×ε_bg too large (WP4 I10) |
| L10 | WP1 | §7 L10 | [E1] → jellium → RPA ✔ | DERIVED, REF | — |
| L11 | WP1 | §7 L11, [E9] | pole of ε⁻¹; (7.1) ✔ | DERIVED, REF | q_c ≈ 2.24 keV; "×(5/1.9)²" REFUTED → ≈ ×1.4 (IF-17) |
| L12 | WP3 | §5, (W.11)–(W.12) | X0 ⊕ X+ adiabatic, ω_ph dropped ✔ | DERIVED (✎), REF | ZG mechanism: alternating signs (7)–(10) |
| L13 | WP4 | §2.1, [2.1]–[2.2] | (3.3) spin row → 6 steps ✔ | DERIVED, REF | — |
| L14 | WP1 | §7 L14, [E7] | [E1] with 𝒳 = BSE ✔ | DERIVED, REF | — |
| L15 | WP4 | §4.2, [4.1]–[4.2], [4.2′] | (3.3) → (5.4)/(5.5) → GRPA → bare bubble → Lindhard ✔ | DERIVED (✎ GRPA), REF | drop "𝔤_I closed form new" (novelty UNRESOLVED, OW4-3; phase term credited to 2609.06423); add first-order [4.2′] (≤ 16% at 5Δ) |
| L16 | WP4 | §5.2–5.5, [5.1]–[5.2] | (3.3) → (5.3)/(5.4), ε_bg in total ε ✔ | DERIVED; **ε_bg² finding REFEREED (R×2, FT)** | replace "CONDITIONAL / R7 FT check" (I8); add absorption ×ε_bg (§5.5); re-plot = RG10 (coordinator) |
| L17 | WP0 (WP1) | WP0 §9.2; WP1 L17 | (9.3)–(9.6); ε(q,0) ≥ 1 by WP1 [E3] ✔ | DERIVED at RPA+LFE for ch = c and clamped ch = e | relaxed ch = e: step false in general (2.30; G6); beyond RPA (−R⁰)⁻¹ + f_xc > 0 (B2) |
| L18 | WP2 | §9 L18, (6.1)–(6.2) | n_A = 1 on S^{GS}_κκ ✔ | DERIVED, REF | nuisance form WP6-v3 (5.1″) type T (not (5.1′)) |
| L19 | WP2 + WP1 | WP2 §8, §9; WP1 §6, L19 | (3.3) full q, (8.1); even ℓ, ℓ = 4 first ✔ | DERIVED (✎), REF | P,T-broken: density odd part O(q³); lowest odd ℓ from G_eff (WP6 (1.5)) |
| L20 | WP5 | §6.1 | (3.4) GS imp → (W9) → (W3) first moment ✔ | DERIVED (chain), REF | replace "½εS_e not reproduced" by "derived in 2001.06503 App. B; objection = (D)-inconsistency; observable ℋ_nuc + E_st, BCA = truncation 0" (IF-R8-8) |
| L21 | WP5 | §6.2 | (W6) → (W5) → (W3) + truncations ✔ | DERIVED (✎), REF | — |
| L22 | WP5 | §6.3 | (W9) → (W3) → (W10) ✔ | DERIVED, REF | thresholds 352/395 eV, soft |
| L23 | WP5 | §6.4, (W14) | second moment of (W3) with (W4) ✔ | DERIVED, REF | "F ≈ 0.121 [E]" → "no evidential weight" (IF-R8-8) |
| L24 | WP6 | §2, (1.4), (1.6) | (3.4) → (9.1) → (I) → SHM → 1509.01598 Eq. (17) ✔ | DERIVED, REF | m_min = (3.1′); 0.333/0.212 are floors; recast exact only for min-over-bins (IF6-17) |
LIMITS header "CLAIMED pending R7" → "REFEREED (R7) on v2; v3 corrections pending R8 verification"; "returns/R6/AUDIT.md" → "returns/R8/AUDIT-2.md".

---
## 3. Interface quantities (brief item 1)
- **Master formula / contraction:** Σ_ab𝔇_abS_ab = tr[𝔇ᵀS] in WP0 (3.4), (7.3); WP4 [3.3] (I9 consistent); WP5 (W6) index-wise (m21); WP6 (1.2), (1.7), (4.1); CONVENTIONS §8 amended. Single-operator uses (WP1–WP3) unaffected. ✔
- **S, R, L, ε; S ↔ L; FDT:** identical in all packages (WP1 [E1], WP0 (5.4), WP3 (M.14) with 𝒫_±, thermal factor once in WP0 (5.6), WP3, WP6). ✔
- **Screening formula** WP0 (5.3): used verbatim by WP1, WP2 (4.2), WP3 §M7, WP4 [5.1], WP6 (5.2). Spin-row wording: m12, m13.
- **Theorem D sectors:** remainder O(κ_BO^{2(n+1)}) in WP0, WP2 (O(κ_BO⁴)), WP3, WP6; WP4 (e) stale (m8). Scope (magnetic insulators): m9.
- **Final-state-resolved response → WP5:** WP0 (7.1)–(7.3) = WP5 (W5)–(W6) (q, 𝔇 inside the Λ sum, retarded out-state weight, DC seeds). Plasmon exception: m6.
- **Multiphonon S_NN → WP5:** WP2 (2.2), (3.5), (3.6) = WP5 §3.1 (ω′ < 0 absorbed; (1 − P_Mig), M + δM). Moment bookkeeping: **B3**.
- **M̃ amplitude:** WP0 (5.7) ≡ WP3 (M.13); retarded W^{scr}(P,ω_f), final-pair index first, in both (G8 / IF-12). Level of rigour: m4. Envelope: **B1**.
- **Halo factor:** η/(2q) in WP0 (9.2), WP2 L6, WP3 (M.6), WP6 (1.4). ✔
- **Nuisance structure → WP6:** WP6 (5.1)–(5.2) ⇄ WP1 IF-3/IF-13, WP2 (6.1)/(6.1′) + IF-4, WP3 IF-10, WP4 I12, WP5 §8 — consistent, except WP0 (8.1)–(8.2) (**B1**) and WP2 (6.1′)'s M-or-A recommendation, superseded by type T (IF6-14; minor, inside B1's resolution).
- **𝔨₃ / 𝓜³ (F4):** WP0 (4.7′), WP2 (5.2″), WP3 J8(ii) and C26c are identically equal (sympy: all differences 0), including the 2𝓃_e term. F4 CLOSED.

---
## 4. Owed corrections in CORRECTIONS.md (brief item 4)
- §1–§16 (owed to v1 returns and coordinator files): applied in v2 (R6 AUDIT §4) and retained in every v3 closing table; none reopened. Contested: WP0 CC-1
  (§6 row WP1-D6) — **resolved** (R7 STANDS, A-V14; out-state retarded weight adopted campaign-wide; WP1 [E2] reads ρ*). CONVENTIONS §7 and §13 item 16 still
  carry the "must be checked / referees reconcile" wording (§6).
- §17 (NOTATION v4 renames owed inside the v2 returns): **all applied** in v3 (grep: no a_k for a^A_k, W_Lam only as a rename note, 𝒜^{2m}_α, 𝒜^{PA}_ν, y_R, 𝓃_D, 𝒬^{D-g},
  ξ_coh, M^{ii}, E^ad_0, E_car, θ_{R-k}, θ_GW/θ_exch, J^{(sh)}, Π_mom present; residual bare n_D are the τ multipole slot, correct).
- Coordinator-additions block (O4 scope, τ string nT, halo reference): applied (WP0 §6.2(iii); WP0/WP2/WP6 strings `nT=0` + `T=`; 250.5/794.5 everywhere).
- **Missing:** none against CORRECTIONS.md itself. New owed items are B1–B3, m1–m33 (to be indexed as CORRECTIONS §18 by the coordinator).

---
## 5. M1 window (WP1, WP3, WP6, SOTA)
Inputs: v_max = 794.5 km/s; E_g(0) = 1.170/0.744 eV; Si E_x^b = 14.7 meV; ω_TA(Q*₀ ≈ 0.53 Å⁻¹) ≈ 13.5 meV (Si), ≈ 7.5 meV (Ge) [E, OW6-7].
| quantity | WP1-v3 | WP3-v3 | WP6-v3 | SOTA | recomputed (sympy) | verdict |
|---|---|---|---|---|---|---|
| Si kinematic floor 2E_g/v_max² | — | 0.333 | 0.333 (labelled floor) | 0.333 | 0.3332 | ✔; not a floor for replicas (m2) |
| Si zero-phonon floor 2E_x/v_max² | 0.329 | — | 0.329 | 0.329 | 0.3290 | ✔ |
| Si PAER edge, exciton replica | — | ≈ 0.333 | ≈ 0.333 | — | 0.3328 | ✔ |
| Si PAER edge, continuum | 0.338 | 0.336–0.338 | ≈ 0.337 (0.333–0.339) | 0.338 | 0.3370 (0.3383 with ω_TA(K) = 18 meV) | adopt **0.333–0.337 [E]**; WP1, SOTA stale (m1) |
| Si forbidden-class ZPL (G = 0) | ≈ 0.42 (0.40–0.44) | ≈ 0.42 | ≈ 0.42 | ≈ 0.42 | 0.422 (M_x 1.19 m_e); 0.417 (1.41 m_e) | ✔ |
| Si PAER leads to / two-channel | 0.43 / 0.43–0.54 | 0.43 / 0.43–0.54 (coexist 0.42–0.54) | 0.43 / 0.43–0.54 | same | — ([E14]) | ✔ |
| Si allowed ZPL ((2̄00) at X) | ≈ 0.54 | ≈ 0.54 | ≈ 0.54 | ≈ 0.54 | — | ✔ |
| Ge PAER edge | ≈ 0.21 ("0.212 + phonon") | 0.212–0.214 | 0.213 (replica) / 0.214 | 0.212–0.213 | 0.2119 floor; 0.2140 with 7.5 meV | ✔ (quote **0.213**) |
| Ge allowed ZPL (L) | 0.32–0.36 | 0.32 (0.32–0.36) | 0.32–0.36 | 0.32 | 0.323 | ✔ |
| p̄_on table | [E10] rules | §M3 table | §3.3 table = WP3 | Si 3 / LA 4 / Ge 3 | — | ✔ identical; exciton replicas 3/2 (edge 5 + k_tail) |
**Statement to use:** Si PAER-only ≈ 0.333–0.42 MeV (edge 0.333 replica / 0.337 continuum); PAER-leading to ≈ 0.43; two-channel (forbidden-class ZPL
comparable, ratio 10⁻¹–10^{1.5}) 0.43–0.54; allowed ZPL above ≈ 0.54; Ge PAER-only ≈ 0.213–0.32 MeV. All [E], pending ab initio E_min(q), ω_ν(Q)
(O-WP3-1, OW6-7). Competing ZPL classes: Si second class (on-axis forbidden, G = 0, (k_rel)²/SOC-suppressed) and allowed ((2̄00) on-axis, (1̄11)
off-axis 0.62); Ge allowed L (Γ valley ≈ 3 MeV, WP1 rebuttal to REF-B pending R8). Consistent across WP1/WP3/WP6 except m1–m3, m19.

---
## 6. Coordinator-owned files: superseded statements (exact lines → replacement)
- **CONVENTIONS** l.3 "NOTATION.md (v3)" → "(v4)". l.66–67 "WP0 (4.9) puts N inside and is an owed rename" → "applied in WP0-v2/v3". l.97–98 "In non-centrosymmetric
  targets the external weight must be checked against WP1 [E2]" → "the retarded out-state weight (ε̃⁻¹)_{G0} in (3.2) order is general (WP0-v3 CC-1, R7 STANDS);
  W^{scr}(P,ω_f) retarded, final-pair index first (G8)". l.101–102 "spins at SOC = 0 … xc-renormalised by f_xc^T" → "… dressed by the triplet W^{scr} ladder
  + f_xc^T, R̃_s ≡ 4R_{s^zs^z} (WP1-v3 IF-13)". l.106 "𝒪_i (i = 1…15)" → add "𝒪₂ is outside the 16-row basis (needs a v_s⊗v_s row; WP0-v3 G2)". l.116
  "(0.34, 0.47, 0.319 MeV …)" → "(floor 0.333, PAER edge 0.333–0.337, ZPL 0.42/0.54 MeV; 0.319 is the scissor comparison)". l.161 and §13 item 13
  "M/A/E/Δ of WP6 (5.1)" → "M (scalars or PSD geodesic), A (PSD increments), E, Δ, T (tilted; L its linearisation) of WP6-v3 (5.1)–(5.1″)". §13 item 16
  decision → "out-state retarded weight; WP1 [E2] with ρ* (CC-1 closed R7)". §13 item 21 → add "except an undamped RPA pole (metals, q < q_c): final state
  𝔱 = pl (WP5-v3 IF-R8-3)". §13 item 17 unchanged.
- **LIMITS**: header and every row per §2 (L3, L5, L7c, L8, L9b, L11, L15, L16, L17, L18, L20, L23, L24 notes; status column REF). Hypothesis table row L12
  "ZG = stochastic evaluation" and row L7d are in the SUPERSEDED block: leave.
- **CONTROLS**: C5 "No PAER below ω = E_g + min ω_{Qν} at T = 0" → "At T = 0 the free-pair PAER threshold at fixed q is ≈ E_g + ω_{Q*ν}(q) − ½(m_c+m_h)\|∇ω\|²
  (infimum over q: E_g, outside the window); exciton replicas start at E_x + ω_ν(Q*), which can lie below E_g (WP3-v3 §M3, C5; WP6-v3 (3.1′))". C7 header
  "[authoritative form: WP0-v2 (4.9) … CLAIMED, pending R7]" → "[WP0-v3 (4.9) = WP3-v3 (M.15); REFEREED R7, STANDS]"; the C7 line is truncated after
  "gives no electronic" (delete the fragment). C8 bracket → "[window per WP3-v3 §M9 C8: PAER-leading GaAs only at m_χ ≈ 0.4–0.9 MeV, full q integral]".
- **NOTATION**: l.1 header fine (v4). Row δρ_κ (l.136) → "electronic charge-response vector (core + valence); δρ^val_κ = δρ_κ − q f^core_κ" (WP2 IF-11). Row
  𝔉, c_ν^F (l.226) → "c_ν^F = Γ_Λ₀ Im(Σ_Kramers ρ*a^{off}_ν)/\|ρ_Λ₀\|², dimensionless (WP5 (W17))". Row "k_δ, W_Lam" (l.454) → "k_δ, w_δ = √(1 + 2.71k_δ²) − 1".
  Row "Π_mom …, θ_δ, σ_δE" add δ_θ (nuisance size). New rows: R^{phys}_{j^αj^β}; 𝐁^{NR}_{αβγ} ≡ b^{NR}_{αβγ}/ω²; K_pk (= 𝐊_pk), d_K, ϑ, ϑ_Q, Q_w, p̄_on,
  γ_c, β_c, E^{PA}_th, m_χ^{PA}, m_χ^{ZP}, q^{ZP}, ϖ_II, η_PA, k_xc; WP0 §15 v3 list; WP4 I17 list (rename Π_γ); renames m26–m28.
- **SOTA**: l.3 "returns/R6/*-v2.md" → "returns/R8/*-v3.md". l.56 "Q_min ≈ … ~0.015 Å⁻¹" → "≈ 0.045 Å⁻¹ at δ₀ = 0.3 eV (0.015 at 0.1 eV)". l.65 and l.68
  "factor [0.5, 1.2]" → "[0.4, 1.8] (WP3-v3, R7)". l.100 "m_min(Si) = 0.319 MeV" → "0.333 floor (E_g = 1.170 eV); 0.319 is the scissor comparison".
  l.111 "375 eV (Si) and 465 eV (Ge)" → "≈ 352/395 eV, soft" (IF-R8-8). l.126 "Si: Γ/δ ≈ 0.02–0.6" → "0.007–0.2 at δ₀ = 0.3 eV". l.131 "O5 … PROVEN at
  RPA+LFE for any insulator" → add "(ch = c and clamped ch = e; relaxed electron channel false in general, WP0-v3 G6)". l.136 thresholds → "superseded by
  [E13] (§R8)". l.139 "q_c = 1.88 keV" → "≈ 2.24 keV". l.146, l.152–153 (𝔤_I novelty; QROCODILE conservative; κ² HIGH-PRIORITY) → "see R7/R8 entries"
  (credit 2609.06423; QROCODILE claim withdrawn; κ² REFEREED). l.163 "2603.13052 eq 4.7 … compensated by a doubled dσ/dq" → "1/m_N misplaced (4.6)→(4.7);
  (4.8) UNRESOLVED". l.173 BZ-average theorem → "exact only for Bravais lattices, q ≫ max(n_ph,2W)q_BZ (WP2-v3)". l.229–230 → "RESOLVED (AUDIT-2 §7)".
  l.237 "PAER window lower edge 0.338 MeV" → "0.333–0.337 MeV (WP6-v3 (3.1′))". l.240 "Q_w ≈ 0.2 Å⁻¹" → "0.33 Å⁻¹ at δ₀ = 0.3 eV". l.241 Ge re-base
  "coordinator-unreviewed, an R7 item" → "consistent across WP1/WP3/WP6 (AUDIT-2 §5)". l.75 Theorem D → add "magnetic insulators excluded; remainder
  O(κ_BO^{2(n+1)}); [C] for the crystal limit (WP0-v3 G9, G10)".

---
## 7. SOTA items marked "R7 ITEM" / "for the audit" / "→ AUDIT-2"
- **l.229 𝔨₃ normalisation (WP2/WP3): RESOLVED.** −2𝓃_κ(M_κ/m_e)𝔨₃[1 + 2𝓃_e/𝓃_e(R_κ)] = WP0-v3 (4.7′) = −(M_κ/m_e)·WP2 (5.2″)\|_{q→0⁺}; C26c contact identity
  exact (sympy, differences 0). No mismatch; F4 closed at the 10⁻⁴ level (WP0 G5, WP2 IF-1, WP3 IF-2). Route: SOTA wording only.
- **l.230 stale WP5-v2 I1/I3 text: RESOLVED** in WP5-v3 §10 (I1, I3, I4, I5, I7 CLOSED, audit A11).
- **l.241 Ge re-base (0.212 MeV): RESOLVED**, §5 (all three packages on E_g(0) = 0.744 eV).
- **l.353 G5 reopens F4 (WP2/WP3): CLOSED** (as l.229).
- **l.364 lower edge 0.333 vs 0.338: RESOLVED**, §5 (0.333 replica / 0.337 continuum; 0.338 used ω_TA at the pocket). Route WP1 erratum (m1), SOTA l.237.
- **l.210 (P) REFEREE ITEM:** WP6-v3 §4.2 hypothesis with sufficient conditions + library gate; consistent with WP0-v3 §6.2(i). Route: R8 verification (REF-WP6).
- **l.349–365 flags "→ AUDIT-2":** §8 below.
- **R8 rebuttals** (WP0 B-V6, WP1 B-13/B-9, WP3 B-12(a), WP4 R-1…R-4, WP5 ×3, WP6 R-A1/R-B1): internally consistent with the other packages; no
  cross-package contradiction found; route: R8 verification as planned.

---
## 8. Interface flags raised in v3: applied by the owner? (A = applied, M = missing, N = not needed; coord = coordinator file)
| Package | Flags and status |
|---|---|
| WP0 G1–G15 | G1 A (CONVENTIONS §8, WP6; WP5 in substance, m21); G2 M CONVENTIONS (m25), A WP1, N WP4; G3 A (CONVENTIONS, WP3 J2), N WP2; G4 A WP6, M WP1 (m14); G5 A (WP2 (5.2″), WP3 J8); G6 A WP6, M LIMITS L17 + SOTA O5 (coord); G7 A; G8 A WP3, N WP5; G9 M (WP4 m9; SOTA l.75); G10 A WP2, WP3, WP6, N WP5, M WP4 (m8); G11 A CONVENTIONS, M NOTATION; G12 A WP4, N WP1; G13 A in part WP1 (m33), N WP4/LIMITS; G14 A in substance WP5 (m20); G15 N |
| WP1 IF-3…IF-17 | IF-3, IF-4, IF-10, IF-15 A (WP6); IF-6, IF-6b A (WP3 §M9, WP6 (3.1′)), SOTA partly (l.237); IF-11 N (no WP0 magnetisation row); **IF-12 M (WP0; B2)**; IF-13 A WP6, M WP0 (m12), WP4 (m13), CONVENTIONS; IF-14, IF-17 M LIMITS L3, L11 (coord); IF-16 N; IF-17 N WP5 |
| WP2 IF-1…IF-14 | IF-1 A (WP3 J8, WP0 G5); IF-2 A (WP5 §3.1); IF-3, IF-10 M (WP0 m10, WP6 m11, SOTA l.173, LIMITS L5); IF-4 A (WP6); IF-5, IF-6, IF-8, IF-9 A (closed); IF-7 N; IF-11 M (NOTATION δρ_κ); IF-12, IF-13 N (WP2's own G3 spec); IF-14 A WP0 (9.7), N LIMITS |
| WP3 IF-2…IF-16 | IF-2, IF-16 A; IF-5 A (WP6 table identical); IF-8 A WP6, M SOTA l.237, LIMITS L8; **IF-10 A WP6, M WP0 (B1)**; IF-11 A; IF-12 A WP0 G8, N WP5 (m4 wording); IF-13 M WP0 (m24); IF-14, IF-15 M LIMITS L9b, L7c, SOTA l.163 (coord) |
| WP4 I1–I17 | I1 M (WP0 m7); I2 A (WP5 4Δ); I3, I5, I6, F11 N/closed; I4 A WP6 (stronger; m16 on WP4's side); I7, I17 M NOTATION (m31); I8 M LIMITS L16, WP0 (m22), A SOTA, N CONVENTIONS §9; I9 A; I10 N WP0/WP3 (formula correct), M LIMITS L9b; I11 A; I12 A WP6, N WP5; I13–I15 A WP6/WP5, N LIMITS; I16 M (WP0 m10) |
| WP5 IF-R8-1…10 | **IF-R8-1 A WP2, M WP0 + WP3 (B3)**; IF-R8-2 N; IF-R8-3 M WP0 (m6), CONVENTIONS item 21; IF-R8-4 M NOTATION, WP3 (m15), O4 → its erratum list; IF-R8-5 A WP6, M WP3 (m15); IF-R8-6, IF-R8-7, IF-R8-9 A; IF-R8-8 M SOTA l.111, LIMITS L20, L23 (coord); IF-R8-10 M, nobody supplies a GaAs Γ/δ map: record as exact remaining gap (OW0-10, O-WP3-6) |
| WP6 IF6-2…IF6-17 | IF6-2 M NOTATION (m29); IF6-3 A; **IF6-4, IF6-15 M WP0 (B1)**; IF6-7, IF6-16 A; IF6-8 A WP5, M WP3 (m15); IF6-9 A; IF6-10, IF6-11 M WP1 (m1), SOTA l.237, A WP3 (m3); IF6-12 M WP4 (m16); IF6-13 A; IF6-14 M (inside B1; WP2 (6.1′) superseded by type T); IF6-17 M LIMITS L24 |

---
## 9. Duplicated or contradictory claims (brief item 5)
- **Anisotropy/modulation (WP1 §6, WP2 §8, WP6 (1.5)):** consistent (odd ℓ ≡ 0 by TR, no cubic ℓ = 2, first ℓ = 4, soft-limit Migdal modulation zero in
  Si/GaAs; WP1's every-k statement supersedes WP2's conditional caveat). P,T-broken odd harmonics: WP4 vs WP6 (m16).
- **Migdal (WP0 §6.2 vs WP3):** amplitude, m_A/δM_κ, L7d split, J7 sign agree; first-moment bookkeeping B3; "≤" m24. **PAER screening:** formulas
  identical, rigour m4, envelope B1. **Thresholds:** m1–m3, m19. **Spin screening:** m12–m13. **δ_rel:** m14. **Fano:** m15. **Theorem D-g:** m7–m9.

---
## 10. Gap coverage (brief item 6)
| Gap | Owner(s) | Closed with formula + specification | Exact remaining gap recorded |
|---|---|---|---|
| G1 near-gap yield | WP5 | (W1′), (W3)–(W8), (W15)–(W17); spec §2 | R1, R2, R7, R8 (θ_dense) |
| G2 PA edge | WP3 | (M.1)–(M.14), §M3 onset table, (W.4c)/(W.14), §5 hybrid; §M10, §8 | X2-N1…N4 (envelope [0.4, 1.8]); ab initio E_min(q), ω_ν(Q*) (O-WP3-1, O-WP3-9) |
| G3 NR partition | WP2 + WP5 | WP2 (2.2), (3.5) (FFT at T > 0), (3.6), (5.3); WP5 (W9)–(W11), (1 − P_Mig) prescription | WP5 R3, R8; WP2 gaps 1–3 (small-q coherent n_ph = 2) |
| G4 error bands | WP6 | (5.1)–(5.1″) (types M/A/E/Δ/L/T), (5.2), (6.1)–(6.4), §7 | OW6-3, OW6-4; WP0 (8.1) alignment (B1) |
| G5 beyond RPA | WP1 (+WP3) | [E1], [E7], [E8] (corrected), [E13], [E14]; spec G5 (matrix-free); WP3 (W.14) | finite-q BSE beyond TDA never run; triplet channel (WP1 §10.2, 10.4) |
| G6 Migdal consistency | WP3 | (W.5), J1–J8 (2𝓃_e), N1–N5; §8 G6 | δM_κ, E^{Mig}_3 numerics (O-WP3-3); N1 wording (B3) |
| G7 core / relativistic | WP1 (+WP0) | §5, [E11], WP0 (4.6″); spec G7 | 4-component no-pair code; all-electron E′_ee (OW0-15) |
| G8 halo at the edge | WP6 | (3.1′), (3.2)–(3.4), (4.1)–(4.2), (P) as hypothesis | G8′ directional (OW6-1); (P) leakage size (OW6-6) |
| G9 SC / films | WP4 | [4.1]–[4.6], [4.2′], Mermin [4.3]–[4.4] (q ≪ k_F, k_TF) | RG1, RG2 (WSi now only via RG2: RTA–Mermin outside validity), RG7, RG9 |
| G10 non-density operators | WP1 | §2.1–2.6 (12/18 functions + R⁰_{GG′}), [E4]–[E6]; spec G10 | LFE on j_T; in-medium 𝒪₈ factor (WP1 §10.5) |
| G11 anisotropy | WP1 + WP2 (+WP6, WP4) | WP1 §6.1, WP2 (8.1)–(8.2), WP6 (1.5) with C28 odd-ℓ rule | G8′; WP4 RG4; m16 |
| G12 unmodelled channels / defects | WP4 + WP5 (+WP3) | WP4 [2.3]–[2.5], [6.1]–[6.3], [7.2]; WP3 (W.13) (equality); WP5 (W12) | WP5 R4; WP4 RG3, RG5 |
| G13 anharmonicity | WP2 (+WP6) | (6.1) (normalised), (6.1′), (6.2); WP6 type T (5.1″); spec G13 ([D, sketch] contraction) | WP2 gap 5 |
| Cat. §12.1–12.2 PA scattering / absorption | WP3 | Part I; (M.17), L9b T-transfer (77 K) | as G2; mK data |
| Cat. §12.3 excitons | WP1, WP3 | [E7], [E8], [E10], [E13], [E14], (W.14) | Frenkel / self-trapped (NaI) |
| Cat. §12.4 NR brems; exo into modes | WP3, WP4 | (W.13) equality + impulse hypothesis; [7.1]–[7.2] | — |
| Cat. §12.5 ER defects; NV | WP5, WP4 | WP5 §4; WP4 [6.3] | ionic-target bond breaking; RG5 |
| Cat. §12.6 two-magnon; CD | WP4 | [2.3]–[2.4], [3.1]–[3.3], [3.2′] | RG3, RG4 |
| Cat. §12.7 finite-T / ZPR | WP3 | (W.11)–(W.12), §M5 | non-adiabatic AHC [E] |
Every gap is assigned and either closed with formula + specification or recorded as an exact remaining gap. Catalog-coverage classification: unchanged
since R6 (A 45 · B 25 · C 11 · D 10); not re-classified.
