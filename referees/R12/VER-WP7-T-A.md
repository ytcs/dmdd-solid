# R12 verification VER-WP7-T-A (referee A, isolated) of returns/R12/WP7-T-v2.md against referees/R11/REF-WP7-T-A.md

Read: WP7-T-v2, code/WP7-T-v2/checks.py (re-run: **51/51 PASS**), my R11 report, and WP0-v3 §6.2 and §5 for the screening question.
I re-fetched cond-mat/0310283 (Eqs. (14)–(20)) to check the new localisation text, then deleted it. Arithmetic checks only.

## 1. Item-by-item (my R11 items)
| R11 item | v2 location | Verdict | Note |
|---|---|---|---|
| #1 `K=def`, 𝒳 = host ε, scr=- | §1.1, IF-T1 | RESOLVED | K = −, 𝒳 = −, ref=def(·); scr=DFPT is legal (CONVENTIONS §11) given §2 below |
| #2 pole rule (Hadamard fp) | (1.3), §2.7, C5d | RESOLVED | (1.3) re-derived: 1/(x²+η²) = (π/η)δ + fp(1/x²) + O(η) (test functions 1, x²: π/η − 2 vs fp −2; 2 − πη vs 2). Cross term 2Re(a*B)PV − 2πIm(a*B)δ is correct. The subtraction formula of §2.7 is correct |
| #2 c_l² cosmetic | (1.2) | RESOLVED | — |
| #3 quasi-elastic part, one-sign STM | §1.2, §2.2 | RESOLVED | — |
| #4 C4c settled, G-T5 | §2.3(a), G-T5, C4c | RESOLVED | Chain 2103.06977 Eqs. (4)+(12)+(13)+(15) is as I derived |
| #4 tanδ misquote | §2.3(d) | RESOLVED | AlOx 1.6×10⁻³ (no T); a-Si:H 2.5×10⁻⁵ at 4.2 K. Matches full text |
| §1.5 double tanh | (2.3) | RESOLVED | — |
| #5 window and core term | §1.4(i), §2.4, C14b | RESOLVED (one remark, N2) | The window q ≪ min(q_×, 1/r_core) is stated; the core is included. R_core ≈ 1.5 is reproduced from the C14b integrand (orientation average 2f²(1 − sin qd/qd), u·η weight). The (1 + m_χ/m_e)² = 8.74 restoration is correct; v1 had wrongly used m_χ ≪ m_e at 1 MeV, an error I missed in R11 |
| #5 P̄ inconsistency | §2.4, C14b′ | RESOLVED | 8.6×10⁴⁴ J⁻¹m⁻³ (C14c remains as an unused conversion: harmless, could be deleted) |
| #5 minor (ω/v², "§2.3(a)") | §2.4 | RESOLVED | — |
| #6 dispersion quoted, f-sum wording, Σw_i ≤ Δ_dfn | §3.1 | RESOLVED | — |
| #7 M_cr not new | §3.2, L31, C10c | RESOLVED | C10c (M_cr = E₀/c_s²) re-derived from 1806.11002 Eq. (3) with c_s² = βa²/m |
| #7 W numbers, band, normal-state W, prior literature | §3.2, C10d | RESOLVED | Band 0.024 meV (exact Mathieu; my asymptotic gave 0.03). Coherence downgraded to [C]. Cited works marked [UNVERIFIED]: correct |
| #8 α_ohm = 4K, coherence criterion | §4.1(b),(c), C6e | RESOLVED | Criterion now Δ̃₀(T) > αΘ (cond-mat/9409105 Eq. (10)) |
| #9 energy-gap law; λ convention | §4.1, §4.2, (4.3), C14d,e, C15 | RESOLVED (remark N5) | λ_P = (d/2)√(2MV) agrees with 1610.03974 Eq. (13) for intersecting parabolas (Mω²d²/8 barrier, λ₀ = Mωd²/4ħ = exact WKB integral). Quartic = (4/3)λ_P. Numbers 4.1 / 27.5 / 25.2 / 166 meV verified. Gap example: e⁻¹/17! = 1.0×10⁻¹⁵, Δλ ≈ 17. "Frozen" withdrawn to OPEN |
| #10 release laws | §4.3–§4.5 | RESOLVED | The 1D t^{−3/2} was withdrawn to [C] on referee B's point; acceptable |
| #11 (4.4) T = 0, transverse factor, C14f | §4.1(a), §4.4 | RESOLVED | — |
| #12 kinetics bath (J_loc), class split, α_ohm prerequisite | (4.1), §4.6, §5.2 | RESOLVED | The spec is now sufficient for the eV class, given G-T2 inputs |
| #13 §2.5 bound | §2.5 | RESOLVED | 2×10⁻²⁰ × 8.74 ≈ 2×10⁻¹⁹: correct |
| §1.3 screening | §1.5 | rebuttal ACCEPTED, with a scope condition (§2) | — |
| §2 Γ₂ location; §6 notation (ω₀ → ω_well, Γ_att); §4 priority UNRESOLVED; §5 IF-T8 wording | §2.1, §4.1, G-T7, IF-T8 | RESOLVED | — |

## 2. Screening rebuttal: ACCEPT (with a scope condition)
*Derivation.* Take the DM potential φ(r,t) coupled to electrons, Σ_e φ(r_e), with ω ≪ the electronic gap (GS sector, WP0 §6.2 (H2)).
- Its effect on the nuclear dynamics is the shift of the adiabatic surface, E₀(R;φ) = E₀(R) + ∫φ ρ̄_e(r;R) + O(φ²). This is exact at first order by
  Hellmann–Feynman: ∂E₀/∂φ(r) = ⟨Φ₀(R)|n_e(r)|Φ₀(R)⟩.
- The GS transition amplitude is therefore ⟨χ_f|∫φ ρ̄_e(R)|χ_i⟩ + O(κ_BO²). Expanding in u gives ∫φ ∂ρ̄_e/∂u_κ. Here ∂ρ̄_e/∂u_κ = δρ_κ is the
  self-consistent (Hartree + xc screened) density response to the nuclear displacement, i.e. the DFPT quantity.
- The alternative picture is: φ polarises the electrons by R^{scr}φ, and that induced density pushes the nuclei. The return's symmetry statement
  ∫(−∂_uV_eN)R^{scr}φ = ∫φ δρ_κ shows this is the same term counted from the other side, not an additional one.
- Multiplying again by ε_e⁻¹(q,ω) would screen twice. WP0's external ε⁻¹ applies when the vertex is the **proper** (Coulomb-irreducible)
  response R̃. A fully self-consistent adiabatic δρ_κ is the improper object, so CONVENTIONS §7 "screening applied once" is satisfied.

*Scope condition (must be added to §1.5, W).* The acceptance needs δρ_κ(q) to be the **full** finite-q DFPT response, including the G = 0
(macroscopic) Hartree component.
- WP2-v3 (1.2) and §1.3 state δρ_κ → q·(Z_κ𝟙 − Z*_κ). Born charges Z* are defined with the macroscopic field removed, which is the proper
  object.
- *Host term:* the difference is zero because Σ_κZ*_κ = 0, so neutral acoustic motion produces no macroscopic field.
- *Core term:* a displaced atom with Z*_κ ≠ 0 (O in SiO2) has a dipolar part, and at q ≲ q_BZ that part is reduced by the macroscopic
  screening (~1/ε_∞ = 0.5 at q → 0, tending to 1 at q ≫ q_BZ).
- *C14b's core* uses the free-atom f ≈ 8, i.e. rigid-ion with no screening. That is acceptable inside the stated ×3 [E] band, but §2.7's
  "δρ_κ from DFPT" must mean the finite-q improper response, not one reconstructed from Z*.

## 3. Theorem T-1 (release-path sum rule)
*Proof check.* d/dt Σ_iN_iE_i = Σ_{ij}(Γ_jiN_j − Γ_ijN_i)E_i. Relabelling the first sum gives Σ_{ij}Γ_ijN_i(E_j − E_i) = −∫dE E𝒦^{rel}. Integrating
from 0 to t with N_i(0) = δ_ic gives (5.3). The proof is correct, and C16 verifies it exactly on an absorbing chain (3849/899 both sides).

**Verdict: STANDS WITH CORRECTION.** It is a telescoping energy identity of any linear master equation, so the "theorem" label is generous but
the content is right. Two conditions are missing from (i)–(iii):
- **(iv) Probability conservation, Σ_iN_i = 1, i.e. a linear single-seed chain.** It is needed to rewrite E^{conf}_c − ΣN_iE_i as E_st − E_st^{frz}
  (subtracting E^{conf}_0). Bimolecular or uncorrelated recombination with other defects ((1 + t/t₀)⁻², §4.3(c)) is outside the per-seed (W12)
  kernel, so the identity needs the pair-state space there.
- **(v) E^{conf}_i must be the energies whose differences are the hop releases ε_ij**, i.e. the well **ground-state** (ZPE-inclusive) energies used
  in (4.2). WP5-v3 defines E_st from E^ad_0 at the minima (classical). At mK the release per hop differs from the classical drop by ΔZPE of the
  local modes (~10–100 meV for interstitials). That is a percent-level mismatch for eV E_st, and a sizeable one for meV TLS-like hops.
  Fix: use one E^{conf} table (condition (ii)) that is ZPE-corrected, or state the classical-energy truncation.

With (iv) and (v), the claim "closes WP7-E IF-E2" is accepted.

## 4. New errors / remarks in the changed sections
- **N1 (W).** The §2.4 incoherent-addition argument ("relative orientation of d and γ random") is the wrong reason, though the conclusion is
  right. With the origin at the defect centre x̄ (where D_R − D_L acts), the core amplitude is 2if·sin(q·d/2), purely imaginary, while the static
  host term is real. So Re(a*B) = 0 **for every orientation** in the static window: the PV cross term vanishes there, and only the Fano δ term
  (−2πIm(a*B)δ) survives at the pole. State this; it also makes the C14b sum exact rather than an average.
- **N2 (W).** C14b's R_core uses an unboosted Maxwellian (no v_E), while the host rate uses ⟨|v|⟩ = 330 km/s. Including v_E raises qd and
  R_core. This is covered by the stated ×3 band, but say which halo is used.
- **N3 (W).** The window (4.3) "reduces to λ_P ≲ 23.6 for ε ≲ ω_D" assumes ω_well·A_T ≈ 1. For one-phonon relaxation A_T = J_ph(ε)/(πε²) ∝ ε,
  so ω_well·A_T ≈ 1 holds near ε ~ meV but drops by ~10² at ε ~ 10 µeV (bound ~2 lower in λ_P). Add "(ε ~ meV)".
- **N4 (W).** §3.2 cites "~(V₀/Δ)^{1/3} ≈ 30 a_lat (cond-mat/0310283 Eq. (17))". The confinement condition is Eq. (17) |∇φ|a > Δ, but the radius
  formula R₀ = a(V₀/Δ)^{1/n} is Eq. (20). The V₀ ≈ 1 eV implicitly used (to get ≈ 30) is unstated; give it with [E]. The Eqs. (17)–(18)
  quotes are correct.
- **N5 (W).** The (π|B|²/η)δ and Fano δ terms exported to the cascade form a signed (non-PSD) seed weight. That is allowed by O4-d7 / CONVENTIONS
  §13 item 20, but IF-T9 should say so explicitly so that WP5 does not clip negative weights.
- No new S-level error found. New checks C5c, C5d, C6e, C10c, C10d, C14b, b′, d, e, C15a,b and C16 were inspected and all are non-vacuous.

## 5. Summary
Every R11 item is RESOLVED. Screening rebuttal: ACCEPT, with the condition that δρ_κ is the full finite-q improper DFPT response (it matters
only for the core term at q ≲ q_BZ). Theorem T-1 is correct; add conditions (iv) probability conservation and (v) ZPE-consistent E^{conf}.
There are five minor W items (N1–N5) and no new substantive error.
