# R11 referee REF-WP7-D-A: hostile, isolated referee of returns/R10/WP7-D.md

Brief: briefs/R11/REF-WP7-D-A.md. I read the return, code/WP7-D/checks.py, WP0-v3 (§2, §3, §4, §9, G-table), CONVENTIONS, NOTATION,
CONTROLS, DONE and LIMITS. I did not read referees/, state/, other R10 returns or other briefs. I re-ran checks.py and got 34/34 PASS
in about 5 s. Full texts were fetched with lit.py into literature/papers-r11-WP7-D-A/ and deleted at the end: 1306.6089, 1711.10489,
2101.01241, 2501.05504, 1508.01798, 1905.12635, 2011.01940, 1509.01598, 1703.00910, 2507.14287, 2109.08168, 2006.13918 and 2102.10171
(PDF). I also checked the arXiv API abstracts of 1905.13650, 2308.00309, 2410.17308, 2609.07908 and 2405.05728 ([ABS] only).
I ran no simulations. My own algebra checks were done by hand or in sympy, each under 2 min.

## Verdict table

| # | Claim | Verdict | Reason |
|---|---|---|---|
| 1 | (D.1) Gaussian field spectrum, ∫𝒮_φ = ρ/m²; 1711.10489 Eq. (24) as a limit | STANDS | Eq. (24) is the exponential law with λ(ω) ≡ ⟨S_ΦΦ⟩ = Aπf/(m_av) in the same display. C2b reproduces it through their Eqs. (12)–(15). |
| 2 | (D.2) coherent signal = off-diagonal retarded R; finite-body replacement of k_φ | STANDS | Kubo at first order in the (3.2) index order. The finite-body sum over modes is correct. See C7 for the "slab" remark. |
| 3 | (D.3)(i) mean power and mean counts = the f_χ-averaged (3.5) "for any t_int and any t_coh" | STANDS WITH CORRECTION | This is false for short records. See C1. |
| 4 | (D.3)(ii) Bose bunching Var N = N̄ + N̄²/𝒩_c | STANDS | This is the chaotic-light (negative-binomial) result. It is correctly tagged [D, sketch]. |
| 5 | (D.4) Bloch transient and steady state; 1306.6089 Eq. (1); 2101.01241 Eq. (1) | STANDS | Both forms check out (C5a–d). The source quotes are verbatim. The envelope claim is CONFIRMED (see §c). |
| 6 | (D.5)–(D.6) SNR: t^{−1/2} versus (t·t_coh)^{−1/4}, crossover (3/2)t_coh | STANDS WITH CORRECTION | The scalings stand. The "3/2" depends on conventions. The FDT step needs a spin temperature. The Rayleigh penalty is not O(1). See C2–C4. |
| 7 | (D.7) BAR: Q_s → Q_DM^eff = (π/2)m F_φ(ω_n) ≤ 1.3×10⁶ (SHM) | STANDS WITH CORRECTION | The integral and the number are right (C6a–c; I checked the rest-frame value 2.41×10⁶ by hand). The normalisation in (D.7) has a typo. See C5–C7. |
| 8 | (D.8) h = −δα/α − δm_e/m_e from H_C scaling; drive ∝ ω²; corrections | STANDS WITH CORRECTION | The physics is right, but the citation is wrong and the (Zα)² size for Cu is overstated. See C8. |
| 9 | (D.9) multiferroic signal = R_{s^z,trJ_e} in a P,T-broken reference | STANDS | [D, sketch]. 2102.10171 Eq. (5) is quoted correctly. |
| 10 | (F.1)–(F.5) fermion-number-changing class, 𝔇^F, ω^F_q; m_χ²/q² exact by continuity | STANDS | I re-derived the contraction by hand: 2(k·J*)(p·J) − (k·p)J*·J = m(q+ω)²/q·\|n\|². One wording correction (C9). |
| 11 | (F.6) 1905.12635 Eq. (4) recovered, with the (1 − m_χ/M) recoil term and the impulse line width | STANDS | Eqs. (1), (3) and (4) and σ_NC = m_χ²/(4πΛ⁴) are verbatim. The width ≈ 4×10⁻³ (Si, 10 MeV) is a sound [E]. |
| 12a | 2011.01940 Eqs. (7) and (10) reproduced "exactly" | STANDS WITH CORRECTION | "Exact" holds only up to an unaddressed factor-2 spin convention in f_ion (C10). |
| 12b | 2011.01940 Eq. (9) differs at bound kinematics by 1 − ω²/m_χ² + … | STANDS WITH CORRECTION | The algebra is CONFIRMED. Calling the paper wrong is UNRESOLVED. The return misstates what the source flags (C11). |
| 13 | (T.1) contact pair absorption = two-point S at (≈0, 2m_χ); 2507.14287; ξ = 44.8 ↔ ρ/(2m) per species | STANDS WITH CORRECTION | ξ = 44.8 is CONFIRMED. The vector and axial operators are misstated (C12). |
| 14 | (T.2)–(T.3) dark Compton: seagull gives κ²σ_Th(1 − 3x/2), = 2109.08168 Eq. (2) through O(x) | STANDS | Eq. (2) is verbatim. I checked by hand that the resonant terms vanish for a free electron (ε′·k′ = 0, p_i = 0). |
| 15 | §3.5 scattering and mediator absorption are independent; the mediator is never on shell | STANDS | ω ≤ qv < q, so the mediator is spacelike. Tag misuse: see C14. |
| 16 | (S.1)–(S.2) Lindhard and Bethe stopping as limits of (3.3); tracks out of scope | STANDS | I re-derived the prefactor 2Z²α/(πv²) and the f-sum route to the Bethe formula by hand. The Born parameter ≈ 15 (Si) checks out. |
| 17 | §4.2 I2 split: radiative part carries only n_r; non-radiative part lies inside (3.3) | STANDS WITH CORRECTION | The in-medium scaling of an M1 decay is n_r³, not Re n_r (C13). |
| 18 | Checks 34/34 PASS | STANDS | Reproduced. Several checks are restatements rather than tests (C15). |

## Corrections (numbered C1–C15)

**C1 (claim 3, substantive).** §1.4(i) claims that the mean absorbed power equals the golden-rule rate "for any t_int and any t_coh".
- The mean energy absorbed in a record of length t is ∫dω 𝒮_φ(ω) convolved with the Fejér kernel (t/2π)sinc²((ω−ω′)t/2) and
  ω|Im R(ω′)|.
- It grows linearly in t only when t_int ≫ min(t_coh, 1/Γ_T), that is, when the record resolves the wider of the DM line and the target line.
- Counterexample, from the return's own (D.4) at δω_L = 0 and t ≪ T₂, t_coh: |M_⊥| = M₀Ω_a t, so the absorbed energy ∝ M_⊥² ∝ t². That is not a
  rate.
- The return's own (D.6) puts in the Fejér window for exactly this reason, so (i) contradicts (D.6).

Replace (i) with: "for t_int ≫ min(t_coh, 1/Γ_T) (steady state, as assumed in (D.2)); for shorter records the mean is (D.3) convolved with the
Fejér window." The statement that coherence never changes a mean linear in ⟨φφ⟩ is still true, but that mean is the windowed one.

**C2 (claim 6).** The crossover t_int = (3/2)t_coh comes from two choices:
- a box-shaped line of width 2π/t_coh;
- the offset-averaged single-bin TS, (2/3)(P_s t/𝒮_n)², which is the frequency-averaged value of a discrete DFT bin.

For the real SHM line F_φ the coefficient differs, and C4c tests only the box. State it as "t_int ≈ O(1)·t_coh (3/2 for a box line,
bin-offset averaged)". Leave "(3/2)" out of any LIMITS row.

**C3 (claim 6).** §1.6(a) calls the effect of the single Rayleigh draw for t_int ≲ t_coh "an O(1) weakening at 95% [E]".
1905.13650 [ABS, checked via the API] reports that earlier limits were overestimated by "factors ranging from 3 to 10". Cite it, and replace
"O(1)".

**C4 (claim 6, §1.5(c)).** The intrinsic spin noise is written with FDT at the lattice temperature, −coth(βω/2)Im R_{I⁺I⁻}, while
R ∝ ⟨I^z⟩.
- CASPEr samples are prepolarised and out of equilibrium, with T₁ of hours (1306.6089 §2).
- FDT applies there only at a spin temperature β_s defined by tanh(β_sω/2) = p. Then coth(β_sω/2)·⟨I^z⟩ is independent of p. That matches the
  source's statement in its §A.3 that the noise is "unaffected by the polarization".
- At the lattice β, the noise would scale with p/p_eq, which is wrong.

State the spin-temperature hypothesis in (D.5) and in the noise of §1.10.

**C5 (claim 7).** In (D.7), R_mode contains the factor 1/V, as R does in (D.3). The left-hand side should therefore be P_abs/V, or else
R_mode should carry V. As printed, the equation is dimensionally off by one power of V.

**C6 (claim 7).** The statement "their Q_DM ∼ 10⁶ holds at the line peak" is fine. Add that Q_DM^eff depends on the operating frequency
through F_φ(ω_n), and that it carries the annual modulation of v_E(t).

**C7 (claims 2 and 7).** "The 1/ε₀ in 2501.05504 Eq. (5) is the slab case." It is also the bulk value: κ_eff = κm²/(m² − Π_T) → κ/ε at k → 0.
The finite-body point is correct only as a statement about orientation:
- E′ normal to the plates gives 1/ε (the BAR geometry);
- E′ parallel to the plates gives 1;
- a sphere gives 3/(ε+2).

Reword the sentence so it does not imply that the slab value differs from the bulk value.

**C8 (claim 8).** Two corrections.
- (a) Citation. In 1508.01798, Eq. (7) is ℛ^eff_{i0j0} = δ_ij ḧ. The strain h ≡ −δα/α − δm_e/m_e is defined in the text right after
  Eq. (7). Fix the citation in §1.8 and in L-D5.
- (b) Size of the relativistic correction. "dln a/dln α = −1 + O((Zα)²), e.g. 0.045 for Cu": 0.045 is (Zα)² for the nuclear charge, a
  core-electron number. The lattice constant is set by valence and bonding electrons, whose relativistic sensitivity is much smaller. Present
  0.045 as an upper bound [E], not as "the dominant correction" with that size.

**C9 (claim 10, wording).** §2.4(a) says: "the full m_χ² (not E_ν̃m_χ) needs the nuclear longitudinal current." For a free nucleus,
ω/q ≈ m_χ/2M.
- Keeping the density row alone gives Γ ∝ q₀²/(1 + q₀/M) = m_χ²(1 − 2m_χ/M + …).
- With continuity, Γ ∝ m_χ²(1 − m_χ/M + …).
- The longitudinal current therefore matters only at O(m_χ/M), the same order as correction (i).

Say so. As written, a reader may conclude that the leading m_χ² needs J_L.

**C10 (claim 12a, spin factors; DONE rubric item).** The dictionary 𝒮̄_at = π|f_ion|²/(2E_R) is taken from 1509.01598 Eq. (52) with f_ion as in
its Eq. (51): 2k′³/(2π)³ summed over "occupied states". It is then applied to 2011.01940, whose Eq. (8) defines f_ion^{nl} with **4k′³**/(2π)³
and explicit (2l+1)(2l′+1)(2L+1)[3j]² sums. That is the 1703.00910 Eq. (5) convention, which I checked verbatim.

I summed Σ_{m,l′m′}|∫ψ̃*ψe^{iq·x}|² = Σ_L(2l+1)(2l′+1)(2L+1)[3j]²|I_L|². So the two definitions agree only if 1509.01598's "occupied states"
counts both spin states and the radial normalisations of R_{k′l′} agree. The return writes "spin-summed" without showing either point.
C10b and C10c test consistency inside the dictionary, not this convention. Rating: "exact" is UNRESOLVED up to a factor 2. Close it by
writing the per-shell 𝒮̄_at directly from (3.1) with explicit spin, and comparing it to 2011.01940 Eq. (8).

**C11 (claim 12b).** Eq. (9) is quoted verbatim, the bracket is transcribed correctly into C10e, and the expansion 1 − ω²/m_χ² + … is
right. The source, however, does not flag "the (Zα)² ≈ 0.16 relativistic correction". It says that relativistic wavefunction corrections
"increase the total cross-section", by "a factor of a few to several orders of magnitude for q ∼ O(MeV)", and it draws m_χ ≳ 100 keV dashed.
The −5% at Xe K-shell and m_χ = 100 keV therefore sits inside the region the source already marks unreliable.

The continuity argument is better motivated than the source, because the Z_eff states are eigenstates of one local potential. Still, both
treatments are non-relativistic approximations and the source writes "≃", so "Eq. (9) is wrong" is UNRESOLVED, not CONFIRMED. The return
correctly declines a REFUTED rating. Fix the sentence about what the source flags.

**C12 (claim 13, substantive).** §3.2 writes H_int = G_pair∫(S†S)O with "O = m_eψ̄ψ → m_e n, or ψ̄γ^μγ₅ψ → spin rows".
- In 2507.14287 Eq. (3), the vector and axial operators are i(S†∂↔_μS)(ψ̄γ^μ[G_V + G_Aγ⁵]ψ). (S†S)ψ̄γ^μγ₅ψ is not Lorentz invariant.
- The DM-side factor (p − p̄)^μ makes the A rate velocity-suppressed, as in their 𝒫[(u−v)_⊥²] (the line after their Eq. (10)).
- (T.1), with |G_pair|² alone, covers only the S and P structures. For V and A, add a pair tensor 𝔇^{pair}_ab(p, p̄).

Two smaller points:
- Γ_pair as written is a rate per unit target volume, not "per DM pair density".
- The source uses ρ_DM = 0.39 GeV/cm³; 1905.12635 and 2011.01940 use 0.4. LIMITS rows must rescale to CONVENTIONS §8 (0.3).

For §3.3 with a real φ, the n_φ² pair count needs the identical-particle factor 1/2.

**C13 (claim 17).** 2006.13918 Eq. (1) is a σ^{μν}F_{μν} transition dipole: magnetic, M1, at NR. In a non-magnetic transparent medium,
ignoring local fields:
- the photon density of states scales as n_r³ (not n_r);
- an E1 rate scales as n_r (the 1/ε field normalisation);
- an M1 rate scales as n_r³ (|B|² per photon is independent of n).

So "photon density of states ∝ Re n_r(δ)" is wrong on both counts. The fix does not matter numerically at δ ≫ ω_p, but the statement is
incorrect as written.

**C14 (tags).** 2501.09642 is tagged "[FT, Abstract and §3.4]" and 1509.01598 "[FT] (appendix A.3)". [FT] means read in full text
(CONVENTIONS §12). Use [ABS] plus the named section, or read the full text. The §3.5 closure itself rests on kinematics and stands.

**C15 (checks).** C1a takes Γ_net from WP0 (3.5) and P from (D.3) as inputs, so it tests one line of algebra. C2a, C4c and C10b are
restatements. C3 passes on an `or` fallback that compares integrands. None of these is wrong, but they are not independent tests. In
particular, nothing checks the (D.2) Kubo sign against (3.2) except C1b, on a classical oscillator.

## (c) Claims that a published paper is wrong

| Paper / item | Return's claim | My rating | Basis |
|---|---|---|---|
| 1306.6089 Eq. (1) | The off-resonance envelope printed as sin(δt)/δ; the exact small-tilt form is sin(δt/2)/(δ/2); the printed resonance is half as wide | **CONFIRMED** | Verbatim in the PDF and HTML: "M(t) ≈ npμE*ε_Sd_n sin[(2μB_ext − m_a)t/ħ]/(2μB_ext − m_a) · sin(2μB_ext t)". Resonant growth agrees once Ω_a = E*ε_Sd_n is read in the H = −dσ·E convention, consistent with their Larmor frequency 2μB. The carrier is also approximate: exact (ω_L+m_a)/2 versus their ω_L. The source writes "≈", so this is an approximation with a factor-2 width error, not a misprint of the resonant amplitude. |
| 2011.01940 Eq. (9) | Not current-conserving off the free shell; differs by 1 − ω²/m² + … | **UNRESOLVED** | The algebra is CONFIRMED (C10e reproduced). Whether the paper is wrong: both are NR approximations, and the difference is within the band the source already flags. See C11. |
| 2507.14287 Eq. (8) | ξ = 44.8 means each of S, S† has density ρ/(2m) | **CONFIRMED** | My hand integral, truncated at 2.5β_c: ξ⁻¹ = 0.0223 → ξ = 44.8. |
| 2501.05504 Eqs. (7)–(8) | Q_s = min(Q_p, Q_DM) misses the line shape when Q_p ≫ Q_DM | **CONFIRMED (as a refinement)** | Verbatim. Q_DM^eff = (π/2)m F_φ(ω_n) follows from the narrow Lorentzian. The source's "Q_DM ∼ 10⁶" is the peak value, not an error. |

## (b) The proposed LIMITS rows

- **L-D1:** ✔ with IF-D11.
- **L-D2:** ✔.
- **L-D3:** ✎. The scalings are right, but drop "(3/2)" (C2) and add the 1905.13650 penalty (C3).
- **L-D4:** ✎. Fix the P/V typo (C5). The prefactor 32 and M_n remain open, which the return states correctly.
- **L-D5:** ✎. Fix the Eq. (7) citation and the size of the (Zα)² correction (C8).
- **L-D6:** ✔ as [D, sketch].
- **L-D7:** ✔. Rescale ρ from 0.4 to 0.3.
- **L-D8:** ✎. Add the factor-2 caveat (C10) and correct what the source flags (C11).
- **L-D9:** ✎. Applies to S and P only; V and A need a DM pair tensor (C12).
- **L-D10:** ✔. Eq. (3), the ALP case, stays open as stated.
- **L-D11:** ✔. Born only; the Bethe usage stays [UNVERIFIED], as stated.
- **L-D12:** ✎. The scaling is n_r³ for M1 (C13).

For every row, the validity and leading-correction columns are otherwise correct.

## (d) Consistency with WP0-v3, CONVENTIONS and NOTATION
- (3.5) Γ_net = −(y²/ω)Im R and the R sign of (3.2) are used consistently.
- The (F.2) structure matches (3.3) with the tr[𝔇ᵀS] order.
- The O(κ_BO⁴) remainder agrees with G10 at n = 1.
- The (L) hypothesis for continuity agrees with (4.6) as corrected ([T_e, n_e] = q·j_e).
- 𝔘_C and 𝔇^F are correctly flagged as additions to the 16-row basis (IF-D2).
- geom ∈ {bulk, body} is a new mandatory-metadata entry for CONVENTIONS §11 (IF-D3). That is acceptable.
- I found no collisions with the new symbols. σ_Th rather than σ_T, and ν̃ rather than ν, are sensible choices.
- Halo: the return uses v₀ = 238 and |v_⊙| = 250.5 (CONVENTIONS §8), but quotes source rates at ρ = 0.39 or 0.4 without saying so (C12).

## (e) Gap-closure sufficiency
- **Items 1–3:** The computation specifications (§1.10, §2.6, §3.7) give inputs, grids, convergence criteria, cost and outputs. They are
  sufficient, apart from three things:
  - §1.10 must state the C1 regime condition and the spin-temperature noise (C4);
  - §2.6 must fix the f_ion spin convention (C10);
  - §3.7 must include the V/A pair tensor (C12).
- **Out-of-scope items (D3, D4, I2):** The exact remaining-gap statements are adequate. Charged-current fermionic absorption is a stated
  exact gap: it needs a nuclear transition row plus distorted lepton waves.

## (f) Novelty and new channels
- The return claims no novelty over the literature. The new items are framework rows and classes (𝔘_C, 𝔇^F, geom).
- 2308.00309 ("Absorption of Fermionic Dark Matter via the Scalar Portal", [ABS] via the API) was "verified but not read", yet it bears
  directly on (F.5). It should be read before L-D8's scalar entry is final.
- The Q_DM^eff refinement is a straightforward consequence of the integral. It should not be presented as a new result.

## DONE rung-4 rubric (items relevant here)
- **Time orderings:** both orderings are present in (T.2) and in 𝒯^{(2)}.
- **Spin factors:** see C10.
- **Bose factors:** the bunching in (D.3)(ii) is right; the §3.3 identical-boson factor 1/2 is missing (C12).
- **Resonant denominators:** (T.2) closure is restricted to m_V ≫ |E_B|. Near core edges the resonant terms are not small; this is correctly
  deferred.
- **Screening:** fermionic absorption at q ∼ m_χ ≫ q_TF is unscreened in effect. The finite-body depolarisation is not applied twice
  (but see C7).
- **DM kinematics:** see the ρ conventions in C12.
- **Sign of q:** k_ν̃ = p_χ − q matches (2.1).
- **Pauli blocking:** for ionisation into the continuum it is contained in S and is not an issue.

## Summary
There are no FALLS verdicts. Ten claims stand, and eight stand with correction: five substantive or quantitative fixes and three
citation, wording or tag fixes. The 1306.6089 envelope claim is CONFIRMED. The 2011.01940 Eq. (9) claim is UNRESOLVED; the return
already does not call it REFUTED.

The most important fixes are:
- C1: the golden-rule mean does not hold "for any t_int";
- C12: the pair-absorption operators for V and A;
- C10: the f_ion factor-2 convention behind the "exact" match;
- C13: the n_r³ scaling for M1 emission.
