# R12 verification VER-WP7-T-B (isolated) of returns/R12/WP7-T-v2.md against REF-WP7-T-B (R11)

Read: WP7-T-v2.md (all 449 lines) and code/WP7-T-v2/checks.py (re-run: 51/51 PASS). 2103.06977 was re-fetched to check Eqs. (4) and (12)–(16) in
full text, then deleted. Hand derivations were done for the screening rebuttal, the sign of the host term (C5c), the expansion (1.3), the Hadamard
subtraction in the §2.7 spec, Theorem T-1, and the core-term factor R_core in C14b. No simulations.

## 1. Item-by-item verdicts (R11 verdict-table rows #, corrections C-n)
| R11 item | v2 location | Verdict | Note |
|---|---|---|---|
| #1 K=def, scr=− | §1.1 | RESOLVED | K = −, ref=def(·), scr=DFPT, conv=DC. scr=DFPT is justified by the accepted rebuttal (§2) |
| #3 / C-9 host sign | §1.3, (1.2), C5c | RESOLVED | Re-derived with the CONVENTIONS e^{+iq·r} convention: f(q) = iD·q, δn = i n₀q·u = −n₀q̂Dq̂/(ρc_l²), ΔD = −2γ ⇒ +2n₀q̂γq̂/(ρc_l²). This agrees with my physical argument (R compressed ⇒ δn_e > 0). *Minor:* C5a and C5b still print "−2q̂γq̂" in the old force convention. Their content (the contraction) is right, but their labels now contradict (1.2); relabel them |
| #4 / C-4 pole rule | §1.4(iii), (1.3), C5d, §2.7 | RESOLVED | (1.3) re-derived: \|a + B/(x−iη)\|² = \|a\|² + (π\|B\|²/η)δ + \|B\|²fp(1/x²) + 2Re(a*B)PV(1/x) − 2πIm(a*B)δ + O(η). The §2.7 subtraction ∫[φ − φ(0) − xφ′(0)θ(1−\|x\|)]/x² equals the Hadamard fp exactly: the φ(0) piece cancels the 2φ(0)/ε counterterm and the φ′ piece is odd. This is consistent with C5d's symmetric form. η = ωΓ_ph is right for (ω + iΓ_ph/2)² |
| #2, #5 | §1.2, §2.1–2.2 | RESOLVED (unchanged, correct) | The one-sign STM convention is now stated |
| #6 / C-1(a) 1/𝔔_ph, source ½ | §2.3(a), C4c, L25 | RESOLVED | Verified in full text: 2103.06977 Eq. (4) χ″ = 4NM²tanh·(τ₂ Lorentzians), Eq. (12) P(E,Δ) = P₀E/(Δ√(E²−Δ²)), Eq. (13) ensemble average, Eq. (15) tanδ = ⟨χ⟩″/(ρv₀²). With τ₂ → ∞ and M = γΔ/2E this gives πP₀γ²tanh/(ρv²), confirmed independently by its Eq. (16) (δv/v = (P₀γ²/ρv²)ln T). The ½ in 1705.01108 Eq. (20) is settled as a source slip |
| C-1(b) 2103.06977 Eq. (2) | §2.3(c), L26 | RESOLVED | The tautological C3d is removed. The claim now rests on derivation, as it should |
| #7 / C-6 tanδ misquote | §2.3(d), L32 | RESOLVED | Matches the full text I read in R11 (AlOx 1.6×10⁻³; a-Si:H 2.5×10⁻⁵ at 4.2 K). The single tanh in (2.3) is correct |
| #8 / C-2 (m_χ/μ)² | (2.4), C14b | RESOLVED | The factor 8.744 is in the formula, in the per-TLS cross-section and in the number |
| #8 / C-3 static window | §1.4(i), §2.4 | RESOLVED | The window is ω/(c_l v) ≪ m_χ ≲ q_×/2v ≈ 0.3 MeV. The core term is added at 1 MeV (see §3) |
| #8 / C-8 screening | §1.5 | WITHDRAWN by me: rebuttal ACCEPTED (§2) | A caveat on the numerical core term is in §3 |
| #9 trigger ratio | §2.5 | RESOLVED | 9.9×10⁻²⁹·8.74·8.2/4/10⁻⁸ ≈ 1.8×10⁻¹⁹ ✓ |
| #10 / C-10 f-sum wording, Σw_i | §3.1 | RESOLVED | — |
| #11 / C-5 crowdion novelty | §3.2, L31, C10c | RESOLVED | M_cr = E₀/c_s² is credited as the textbook kink mass, and "not new" is stated |
| #12 / C-11 W band, coherence | §3.2, C10d, §5.1 | RESOLVED | 0.0246 meV matches my 0.024 meV. Coherence is downgraded to [C], with the bulk α-W T_c ≈ 15 mK point added (correct) |
| #13 / C-12 α_ohm = 4K | §4.1(b), C6e | RESOLVED | — |
| #15 / C-7 λ convention, energy gap | §4.1, §4.2, (4.3), C14d,e, C15 | RESOLVED | λ_P values 4.06/27.5/25.2 (quartic ×4/3 = 37) and V ≲ 166 meV(1 Å/d)² re-derived. C15a: e⁻¹/17! = 1.03×10⁻¹⁵ ⇒ Δλ = 17.2 ✓. The frozen verdicts are withdrawn and marked OPEN. (4.3) has the right structure (Γ = (π/2)ω_well²e^{−2λ}A_T, so Γ_att ≈ ω_well up to O(1)) |
| #16 / C-11 1D recombination | §4.3(b) | RESOLVED | — |
| #17 FC at T = 0 | §4.4(b) | RESOLVED | — |
| #19 / C-13 calibration | §5.2, §5.4 | RESOLVED | The class split is now by computed Γ, and the calibration claim is reworded |
| #20 / C-14 sampling, P̄ consistency, band | §2.2, §2.4, §2.7, C14b′ | RESOLVED | P̄ = 1.4×10²⁰ eV⁻¹cm⁻³ = 8.6×10⁴⁴ J⁻¹m⁻³ ✓ (C·ρc_l²/γ²). Sampling ≳ 10⁸ pairs and the 0.1 meV band are adopted. *Cosmetic:* C14c (the withdrawn 10⁴⁴ conversion) is still in the script and serves no purpose |
| #21 / C-15 vacuous checks | §7 | RESOLVED | The 5 vacuous checks are removed, and the conversion-only checks are labelled honestly |
| #14, #18, L27–L30 | — | unchanged; still STAND | — |

## 2. Screening rebuttal (§1.5): ACCEPT
**My R11 claim (C-8).** CONVENTIONS §7 says n_e is always screened, so I asked for an ε_e⁻¹(q,ω) factor on the DM–electron vertex.

**Derivation.**
1. Exact-state golden rule: S_ee = (2π/V)Σp_i|⟨f|n_e(q)|i⟩|²δ(·) (WP0 (3.1)), with exact eigenstates and the bare operator n_e. Screening is therefore never an extra
   multiplicative factor. It sits in the states.
2. In the GS sector under BO, ⟨χ_fΦ₀(R)|n_e(q)|χ_iΦ₀(R)⟩ = ⟨χ_f|ρ̄_e(q;R)|χ_i⟩ + O(κ_BO²). Here ρ̄_e(q;R) is the exact (self-consistent) ground-state
   density at frozen R.
3. To linear order in u: ∂ρ̄_e/∂u_κ = χ^{full}_ee(∂V_eN/∂u_κ) = δρ_κ, the DFPT (Hartree + xc self-consistent) response. That is the improper, ε⁻¹-dressed
   response, applied once.
4. Kubo cross-check: the phonon-reducible part of χ_ee is χ_{e,u}Dχ_{u,e}. Here χ_{u,e} is the force on κ from electrons polarised by an external φ,
   ∫(−∂_uV_eN)χ^{full}_eeφ. By the symmetry of the static χ^{full}_ee this equals ∫φ δρ_κ. So each end carries ε⁻¹ exactly once, through δρ_κ.
5. Multiplying by a further ε_e⁻¹(q,ω) would screen twice, contrary to CONVENTIONS §7 ("applied once: DFPT g").

**Conclusion.** My C-8 conflated the external-ε⁻¹ prescription for proper (R̃) responses with this vertex, which is already improper. The rebuttal is
correct.

**Residual conditions.** These are already stated in v2 as leading corrections:
- (a) non-adiabatic O(κ_BO²);
- (b) for q ≳ q_BZ, the acoustic-sum weight w_e must be replaced by Σ_κδρ_κ(q).
For the neutral acoustic host relaxation (w_c = 0) no macroscopic-field term arises, so no ε_∞ factor appears either.

## 3. Recomputed DM–TLS rate (§2.4, C14b)
- **Host term.** 1.10×10⁻³ × 8.744 = 9.6×10⁻³ /(kg day meV) ✓. It uses only C_TLS, so it is unaffected by the P̄ change.
- **Core term.**
  - ⟨|2·8·sin(q·d/2)|²⟩_orient = 128[1 − sin(qd)/(qd)] ✓ (matches the code's 2·64(1 − sin x/x)).
  - Weight q dq η(q/2m_χ) ∝ u η(u) du with q = 2m_χu ✓. Isotropic Maxwellian η = (2/√π v₀)e^{−u²/v₀²} ✓.
  - R_core = 1.59 and total = 9.6×10⁻³ × 2.59 = 2.5×10⁻² ✓ (quoted 2.4×10⁻²).
- **Incoherent addition: justified, and more strongly than v2 says.** In the static window the host amplitude B is real and even in q. The core
  amplitude 2ic sin(q·d/2) is imaginary relative to it about a common centre x̄. Re(a*B) therefore vanishes identically, not only on the orientation
  average. The "interference sign" item in v2's ×3 error budget is void inside the window. It survives only for an off-centre core, and at the pole as
  the Fano δ term.
- **Caveats (no change to the verdict; the number stands at [E, ×3]):**
  - (i) The halo is inconsistent: the host number uses ⟨v⟩ = 330 km/s, while R_core uses v₀ = 238 km/s with no v_E. A boost raises q and therefore
    R_core. This is within ×3.
  - (ii) The core vertex is a rigid ion (f = Z_O = 8), not the DFPT δρ_κ that §1.5 and §2.7 prescribe. Valence redistribution of 6 of the 8 electrons
    is an O(1) effect at q ≈ 1–2 keV. State this as a leading correction next to "no extra screening factor".
- **Verdict.** STANDS WITH CORRECTION (minor wording on (i) and (ii)).

## 4. Theorem T-1 (5.3)
- **Proof re-done.** Master equation Ṅ_i = Σ_j(Γ_jiN_j − Γ_ijN_i). Relabelling the gain term gives d/dt Σ_iN_iE_i = Σ_{ij}Γ_ijN_i(E_j − E_i) = −∫dE E𝒦^{rel}
  with 𝒦^{rel} as in (5.2). Integrating from N_i(0) = δ_ic gives E_c − Σ_iN_i(t)E_i.
- **Second equality.** With E_st = E_c − E₀ and E_st^{frz} = ΣN_iE_i − E₀, it needs ΣN_i(t) = 1: a closed, probability-conserving table with no
  loss to unlisted states. That is implicit in (W12) but should be stated as condition (iv).
- **Scope.** No detailed balance and no rate model are used. It is a bookkeeping identity for configuration energy. Uphill hops (ε < 0, bath heat)
  are correctly required in (i).
- **Naming.** "E_st^{frz}" at finite t_obs includes populations that are still relaxing. Call it "unreleased by t_obs", or define frozen as t_obs → ∞.
- **C16.** It checks the identity on an absorbing chain (exact rational arithmetic). That is adequate.
- **Verdict.** STANDS WITH CORRECTION (add condition (iv) ΣN_i = 1; wording on "frz").

## 5. New errors in changed sections
No substantive new error. Minor items:
- **N1.** C5a and C5b labels keep the v1 sign "−2q̂γq̂", contradicting (1.2). Relabel them, or state that they test only the contraction under the v1 force
  sign.
- **N2.** §4.1(c) coherence criterion "Δ̃₀ > γ₀". The damped-oscillator form of cond-mat/9409105 Eq. (10) gives an underdamped (coherent) response for
  Δ̃₀ > γ₀/2. The order of magnitude is unaffected.
- **N3.** C14c is vestigial (it converts a withdrawn input).
- **N4.** §2.4 should list the rigid-ion core and halo-mismatch caveats of §3.
