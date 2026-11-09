# R11 referee report REF-WP7-T-A (hostile, isolated) on returns/R10/WP7-T.md

Referee A. Read: the return, code/WP7-T/checks.py (re-run: 46/46 PASS, ≈ 3 s), WP0-v3, WP2-v3 (1.2), WP5-v3 §4 (W12), CONVENTIONS,
NOTATION, CONTROLS, DONE, LIMITS. Full texts fetched with lit.py into literature/papers-r11-WP7-T-A/ and deleted after use:
1705.01108, 2103.06977, 1610.03974, cond-mat/9409105, 2409.02820, cond-mat/0310283, 1806.11002, 2009.03804. No simulations run;
arithmetic checks only (≤ 1 s).

## 0. Verdict table
| # | Main claim (return §) | Verdict | Reason (details in §1–§4) |
|---|---|---|---|
| 1 | Defect = reference-state choice, GS sector; τ string with `K=def`, `ref=def(·)` (§1.1, IF-T1) | STANDS WITH CORRECTION | Placement is right. But `K=def` misuses the kinematic slot (NOTATION: K is the kinematic regime only); `ref=def(·)` already carries the information. "𝒳 = host ε" is not a CONVENTIONS §11 rung. `scr=-` is declared with no leading correction (1/\|ε_e(q,ω)\|², CONVENTIONS §7) |
| 2 | Vertex 𝔣_s = core + dynamic elastic-dipole term (1.2); static window q-independent; pole rule §1.4(iii) | STANDS WITH CORRECTION | (1.2) re-derived: sign, units, transverse drop and static limit are correct (it is the DM→virtual phonon→TLS amplitude with both time orderings). The pole rule is wrong as stated: \|𝔣\|² has a double pole, so "the PV part stays in S^def" is undefined. It must be the Hadamard finite part fp(1/x²) (the CONVENTIONS §10 DC analogue), with the δ/Lorentzian part going to P_casc. The §2.7 spec ("PV prescription") inherits this |
| 3 | One-TLS S (2.1), rank one; STM S flat in ω (2.2) | STANDS | Re-derived, including C2 (∫P(Δ/E)² = P̄ with the one-sign-ε convention of 1705.01108 Eq. (8)), detailed balance and the FDT form of −Im R. The quasi-elastic ⟨g\|σ_z\|g⟩ (relaxation) part is omitted; harmless for DM (ω ≈ 0) but say so |
| 4 | TLS literature limits §2.3 (1/𝔔_ph, 1/𝔔_el, Jäckle, dark photon (2.3)) | STANDS WITH CORRECTION | The formulas are right. The C4c "source slip" is CONFIRMED and **can be settled**: 2103.06977 Eqs. (4), (12), (15), which the return itself cites, give the derived πP̄γ²tanh/(ρv²). G-T5's "cannot be checked" is wrong. A quote is misattributed: the "a-SiO2 tanδ ≈ 1.6×10⁻³ at 4.2 K" is not in 1705.01108 (see §2) |
| 5 | DM rate on TLS (2.4); 1.1×10⁻³ /(kg day meV) at m_χ = 1 MeV | STANDS WITH CORRECTION | The prefactor is right (re-derived; C13a,b). The number lies **outside the return's own static-window/host-dominance condition**: at m_χ = 1 MeV the q range is 1.5–5 keV > q_× ≈ 0.6 keV (d = 1 Å), so the core term dominates (amplitude ratio ≈ 2.7–6.8). The P̄ quoted next to the number is inconsistent with the inputs actually used |
| 6 | Defecton response (3.1) and its limits | STANDS WITH CORRECTION | The kernels are right (C11). Minor: the dispersion is quoted [FT], not derived. "Replaces the bare-mass share of WP0 (4.6b)" is an overclaim: (4.6) is exact and unchanged, and the band contributes \|𝔣^loc\|²q²/2m^dfn to it |
| 7 | Crowdion translation mass M_cr = 2μ_FKa₁₁₁m/π² "New [D]"; W coherent 1D defecton at mK | STANDS WITH CORRECTION (novelty REFUTED) | The formula is right (C10a), but it is the textbook sine-Gordon/FK kink mass (Braun–Kivshar; Kosevich; both are refs [3], [1] of 1806.11002). The W estimate combines the FK mass (μa = 0.5) with the atomistic 1 meV barrier, which FK itself does not give (Eq. (6) gives ~µeV). The band is ≈ 0.03 meV, not "(sub-)meV". Bulk α-W is normal at 10–100 mK (T_c ≈ 15 mK), so the electron bath is active. Prior quantum-crowdion literature is not cited |
| 8 | mK hop rate (4.1)–(4.3) and limits (a)–(e) | STANDS | Every limit re-checked against full text: Jäckle (Eq. (7)), Black (Eqs. (8), (9)), the cond-mat/9409105 Eqs. (8)–(9) NIBA identity, the Weiss T ≪ ε limit, and 2409.02820 Eqs. (1)–(4). Minor precisions in §3 |
| 9 | Tunnelling window λ ≲ 24; frozen Si close pairs (λ ≈ 55) and Al SIA (λ ≈ 50) (§4.2) | STANDS WITH CORRECTION | The criterion Γ ~ ω₀e^{−2λ} holds only for ε ≲ ω_D (one phonon). For eV releases (Frenkel pairs) the energy-gap (FC) suppression of (4.2) is missing. The λ estimates use λ = d√(2MV) (1705.01108 Eq. (7)); 2103.06977 uses (d/2)√(2mV), and a quartic barrier gives (2/3)d√(2MV). That factor ≤ 2 in the exponent moves Si FP to 28–37 and Al to 25–33, so "frozen" is not robust and stays [E] |
| 10 | Release laws 1/t (4.5) and t^{−3/2} (§4.3) | STANDS | (4.5) re-derived = 1610.03974 Eq. (6). The 1D first-passage and 3D Smoluchowski tails are correct, and so is the bimolecular (1 + t/t₀)⁻² |
| 11 | Energy per event (§4.4): one phonon, FC conditional occupation (4.4), photon branch 5×10⁻¹⁴ | STANDS WITH CORRECTION | (4.4) is exact only at T = 0 (Poisson weights; C12 tests only that case). Transverse dominance is 2(γ_t/γ_l)²(c_l/c_t)⁵ ≈ 64(γ_t/γ_l)², not "~2⁵". The photon ratio is verified for one transverse branch (C14h). C14f proves nothing and should be deleted |
| 12 | WP5/WP7-E interface (5.1)–(5.2) and specs §4.6, §5.4 | STANDS WITH CORRECTION | The definitions are fine. The λ ≤ 24 class split inherits #9. The kinetics spec puts only J_ph (Debye ω³) + J_el into J^{sb}; eV releases need local/optical modes (S_HR,k) in the bath, so the spec is insufficient for the Frenkel-pair class, the DM-relevant one |
| 13 | §2.5 DM-triggered relaxation ≪ 10⁻²⁰ of spontaneous | STANDS WITH CORRECTION | At σ̄_e = 10⁻³⁸ cm², m_χ = 1 MeV, Γ_↓ = 10⁻⁸ s⁻¹: n_χ⟨v⟩σ̄_e\|𝔣\|²/4Γ_↓ ≈ 2×10⁻²⁰, not "≪ 10⁻²⁰". State the σ̄_e used. The conclusion is unchanged |

## 1. DERIVED steps (rubric a, d)
**1.1 (1.1)–(1.2).** I re-derived P_def O P_def with the 1705.01108 Eq. (1) basis (σ_z^{(p)} = \|R⟩⟨R\| − \|L⟩⟨L\|): correct. For (1.2), with the
CONVENTIONS §2 Fourier sign, f_i = (elastic-dipole force) → F(q) = 2iγ^{def}·q and ũ = G F, so δO = w i q·ũ = −2w q·G·γ·q. Units close
(F(q) energy/length, G length⁵/energy, q·ũ dimensionless). The c_l² in the numerator and denominator of (1.2) cancel and should be removed
cosmetically. The transverse drop is exact for any γ because q·P_T = 0. The host term is the DM–phonon vertex × retarded propagator ×
TLS–phonon vertex, summed over both time orderings (1/(ω − cq + i0) − 1/(ω + cq) → 1/(c²q² − ω²)). Hypotheses (H-def) are adequate.
WP2-v3 (1.2) gives 𝒵_κ = Z_κq − δρ_κ → q·Z*_κ, hence δρ_κ → q·(Z_κ𝟙 − Z*_κ) and w_e = Ω⁻¹ΣZ_κ, as the return says.

**1.2 Pole rule (§1.4(iii)) — correction S.** S^def ∝ \|𝔣(q,ω)\|² contains \|1/(c_l²q² − ω² − i0)\|², a double pole. Its "principal-value
part" is not integrable, so the stated split is undefined. Replace it with the rule CONVENTIONS §10 already fixes for the analogous electronic
case: the regularised Lorentzian (width = phonon damping, including TLS absorption) is split into its δ part, which goes to S^{GS} ⊗ P_casc
(real phonon then TLS absorption), plus the **Hadamard finite part** fp(1/x²) and PV cross terms with the core amplitude, which stay in S^def.
§2.7 "PV prescription at the pole with analytic subtraction" must read "fp prescription". The light-mediator statement in §2.4 is [D, sketch]
and depends on this.

**1.3 Screening (rubric item).** The electron-coupled host and core vertices are external density vertices. By CONVENTIONS §7 they carry ε_e⁻¹(q,ω),
which is O(10%) at q ~ keV in SiO2 and larger at q ≲ 0.5 keV. The τ string declares scr=-. That is legal, but the leading correction must be
stated (#1).

**1.4 (2.1)–(2.2).** Correct, with the population factor p_g = 1/(1 + e^{−E/T}) and the 2π/V normalisation of WP0 (3.1). The STM convention
(ε ≥ 0 only, as in 1705.01108 Eq. (8) and 2103.06977 Eq. (12)) is what makes ∫P(Δ/E)² = P̄. Say so explicitly: the two-sign convention doubles
every TLS rate.

**1.5 §2.3(a),(b).** Re-derived: absorbed power ω·2π\|γS₀/2\|²(Δ/E)²·tanh against the travelling-wave energy ½ρc²S₀² gives πP̄γ²tanh/(ρc²). The
electric analogue with ⟨cos²⟩ = 1/3 and the stored energy ε_rE₀²/2 (HL) gives πP̄p²tanh/(3ε_r). Both are right. In (2.3) tanδ_TLS(m_φ,T) ≡ 1/𝔔_el
**already contains** tanh(m_φ/2T), so listing "the tanh(m_φ/2T) factor" as a correction double-counts it. Use tanδ₀·tanh if tanδ₀ means the
T → 0 value.

**1.6 (2.4).** Re-derived: ∫q dq η(q/2m_χ) = 2m_χ²⟨\|v\|⟩, then (2.4) with prefactor 1/4. The arithmetic of C14b is right (1.1×10⁻³). But:
- *Window.* The return's own crossover q_× ≈ 2w\|γ\|/(ρc_l²c_κd) ≈ 0.6 keV (d = 1 Å) lies below the m_χ = 1 MeV range q ≈ 2m_χv ≈ 1.5–5.2 keV.
  There the one-atom core amplitude 2c_κ sin(q·d/2) exceeds the host amplitude 2.9 by ≈ 2.7–6.8 (Z̄ = 10; less with the atomic form factor).
  Required correction: add q ≪ q_× to the static-window hypotheses. That means 50 keV ≪ m_χ ≲ q_×/(2v) ≈ 0.3 MeV (d = 1 Å). Otherwise include
  𝔣^core and its interference (sign unknown), and label the 1 MeV number "host term only; core term not included" [E]. The q-independence claim
  for m_χ = 1 MeV is not supported.
- *Inputs.* The number uses C_TLS = 3×10⁻⁴ and γ = 1 eV, which imply P̄ = 1.4×10²⁰ eV⁻¹cm⁻³ = 8.6×10⁴⁴ J⁻¹m⁻³, not the quoted
  "P̄ = 1.6×10¹⁹ eV⁻¹cm⁻³ = 10⁴⁴ J⁻¹m⁻³" (C14c, used nowhere in C14b). Delete that parenthetical or make the inputs consistent.
- "m_χ ≫ ω/v² (≈ 0.1 keV)" uses v_max; with ⟨v⟩ it is ≈ 1 keV. This is immaterial at 1 MeV.
- "ℓ_TLS from (2.3a)" should read "from §2.3(a)"; (2.3) is the dark-photon equation.

**1.7 §3.1.** (ii) The arcsine half-widths are correct. The bound "≤ 2Δ_dfn" is loose: Σw_i ≤ 6J = Δ_dfn (simple cubic). (iii) The free-gas
moments are correct. The f-sum wording needs fixing (#6).

**1.8 §3.2 (W numbers).** The arithmetic is verified (E_rec = 0.147 meV, ħω₀/2 = 0.38 meV). It is model-inconsistent: FK with μa = 0.5 gives, by
1806.11002 Eq. (6), E_mig ≈ 8V₀π²/(μa)²·cosech(2π²) ~ µeV, while the 1 meV is the atomistic barrier of the double-sine model (1806.11002 §2,
period a/2 and different curvature). Treat V = 1 meV, M = 0.1m_W as a Mathieu problem: depth s = V/E_rec ≈ 6.8, giving J ≈ (4/√π)E_rec s^{3/4}e^{−2√s}
≈ 7.6 µeV and a band ≈ 4J ≈ 0.03 meV ≈ 0.35 K [E, referee]. That is "coherent at mK if the scattering rate is < 0.03 meV", not a sub-meV band.
Bulk α-W has T_c ≈ 15 mK, so in bulk W absorbers at 10–100 mK the α_ohm bath (§4.1(c)) is on, and coherence is not established without G-T1.

**1.9 §4.1.** (a) C3a re-derived by hand: Γ_↓ = γ²(Δ/E)²E³/(2πρc⁵) per branch for H_int = γSσ_z, i.e. δε = 2γS. J_ph from λB = 2γS gives
γ²ω³/(πρc⁵) per branch, as in (4.1). (b) 2103.06977 Eq. (8) ↔ W_el² = 4α_ohm is correct. For 2009.03804 Eq. (4) (τ_el⁻¹ = 4πKΔ₀²coth/(ħE))
the exact map is **α_ohm = 4K**; write that instead of "up to its coupling normalisation". (c) The NIBA closed form, the T ≪ ε limit and C6a
match the Weiss/Leggett results; C6a is an exact identity by the Γ reflection formula. The coherence criterion is loose: Δ̃(Θ) is
T-dependent, and coherence needs Δ̃ ≳ γ₀ = KΘ, i.e. T ≲ Δ_r/α_ohm with Δ_r = Δ(Δ/ω_co)^{α/(1−α)}. "Below the scale Δ̃" should be restated.
(d) Correct. (e) The quote is correct; the T⁹ sketch is acceptable as [D, sketch].

**1.10 §4.2 — correction S.** (i) ω₀e^{−2λ} ≈ Δ²/ω₀ equals the one-phonon rate only for ε ~ meV (A ≈ 10⁸ s⁻¹K⁻³ gives ≈ 7×10¹²e^{−2λ} s⁻¹
at ε = 1 meV). For ε ≫ ω_D, (4.2) with a linear bath gives Δ² × (multiphonon FC factor), which is exponentially small in ε/ω_D for weak
coupling (energy-gap law). The window criterion and the (5.1) "relaxing (λ ≤ 24)" class therefore apply only to ε ≲ ω_D, or require the
FC factor. (ii) Convention clash: 1705.01108 Eq. (7) λ = d√(2mV)/ħ, 2103.06977 λ = (d/2ħ)√(2mV); the WKB integral over a quartic barrier
gives (2/3)d√(2MV)/ħ. Carry a θ_λ ∈ [½, 1] factor in every λ estimate (C14d,e). The conclusions "Si close FP frozen", "Al SIA frozen" and
"V ≲ 41 meV(1 Å/d)²" are [E] with factor ≤ 2 uncertainty in the exponent (V-window up to ×4).

**1.11 §4.3–§4.5.** All correct (C8, C9 re-derived). (4.4): add "T = 0 (or ε ≫ T)". At T > 0 the generating function contains absorption
terms and ⟨n_k⟩_ε is not S_HR,k A(ε−ω_k)/A(ε).

## 2. Quotes and proposed LIMITS rows (rubric b)
Quotes checked in full text. Correct: 1705.01108 Eqs. (1), (5), (6)–(7), (8), (9), (15), (16), (20), (22), |γ| ≈ 1 eV. The Γ₂ = Γ₁/2 + Γ_φ
relation is in the text just above (15), not in Eq. (15). Also correct: 2103.06977 Eqs. (2), (4)–(9), (12), "dominated by transverse", T⁵
fit; 1610.03974 Eqs. (1), (4)–(11); cond-mat/9409105 Eqs. (1), (7)–(10), Δ̃₀ after (10), Δ₁ dominance; 2409.02820 Eqs. (1)–(4), T_c = ħω/2πk_B;
cond-mat/0310283 Eqs. (1)–(4), (7), (11), (12), Δ ≈ 10⁻⁴ K (³He), "several degrees" (vacancions), m* = ħ²/Aa²; 1806.11002 Eqs. (2), (3), (6),
µeV (FK) vs meV (atomistic), rare direction changes; 2009.03804 Eqs. (3), (4).
**Misquote (correction S/W):** §2.3(d) "a-SiO2 tanδ ≈ 1.6×10⁻³ at 4.2 K per 1705.01108 §VI". Full text §VI.D: 1.6×10⁻³ is for **thin
plasma-oxidised AlOx** (Deng et al.), with no temperature stated; the 4.2 K value is **a-Si:H, tanδ = 2.5×10⁻⁵** (Bruno et al.). Fix the material
and temperature.

| Row | Source quote | Chain | Validity / leading correction | Verdict |
|---|---|---|---|---|
| L25 | correct | valid | Correct (T → 0, D₀ → P̄; corrections: saturation Eq. (22), relaxation part 2103.06977 Eq. (6), interactions). Replace "(phonon factor ✎, G-T5)" with "1705.01108 Eq. (20) phonon form is ½ of 2103.06977 Eqs. (4)+(12)+(15) and of the derived value" | DERIVED ✔ (with this edit) |
| L26 | correct | valid | Add α_ohm = 4K for 2009.03804; superconducting form E ≪ Δ_BCS (stated) | DERIVED ✔ |
| L27 | correct | valid | Scaling limit ω_co ≫ T, ε; NIBA; the Δ₁ correction is stated | DERIVED ✔ |
| L28 | correct | valid | κ = 1, harmonic classical Z; the κ_PB pole at T_× is stated | DERIVED ✔ |
| L29 | correct | valid | Γ_max⁻¹ ≪ t ≪ Γ_min⁻¹, Δ_tun ≪ E; T* from Eqs. (7)–(8) | DERIVED ✔ |
| L30 | correct | dispersion quoted, kernel derived, T⁻⁹ sketch | ok | DERIVED (kernel) / [D, sketch] ✔ |
| L31 | correct | valid in FK | **drop "(new)"**: standard FK kink mass; numbers [E] with the §1.8 caveats | DERIVED ✎ |
| L32 | correct for Eq. (20) | valid | Remove the double tanh; fix the tanδ material quote | DERIVED ✎ |

## 3. Claims that a published paper is wrong (rubric c)
| Claim | Verified against | Rating |
|---|---|---|
| 1705.01108 Eq. (20): 1/Q_ph = π\|γ\|²D₀/(2ρv²) is ½ of the value consistent with its own Eq. (16) (δε = 2γ·S) | Full text Eqs. (16), (20); 2103.06977 Eqs. (4), (12), (15): tanδ = ⟨χ″⟩/ρv² with χ″_res = 4NM²tanh·πδ and 4M² = γ²(Δ/E)², giving πP₀γ²tanh/(ρv²); also the standard resonant/relaxation ratio 2:1 (2009.03804 plateau πωC/2 is the relaxation plateau, consistent) | **CONFIRMED**. The return should state it as settled, not [C], and withdraw the G-T5 clause about it |
| 2103.06977 Eq. (2) region: H_int = ½(γ·S)σ_z (δε = γS) would give Eq. (7)/4 | Full text: text above Eq. (2) "δε = γ·S", "H_int = 1/2(γ·S)σ_z"; Eq. (7) equals my re-derivation with δε = 2γS. Eqs. (4), (15) are also consistent only with δε = 2γS (the 4M² prefactor) | **CONFIRMED** (a notation slip in the text; Eqs. (4)–(7) are mutually consistent) |
| 1705.01108 Eq. (20) "D₀ = (constant) TLS DOS", which by its Eq. (9) is log-enhanced; the resonant loss needs P₀ | Eqs. (8), (9), (20) | **CONFIRMED** as an ambiguity (not an algebra error); D₀ → P₀ is the correct reading |

## 4. Novelty / new-channel claims (rubric f)
- **M_cr = 2μa m/π² "New [D]": REFUTED.** It is m∫(∂u/∂z₀)²dz/a for the sine-Gordon kink, the standard FK kink mass m_k = 2/(π²d) in
  Braun–Kivshar units (d = 1/μa). Both textbooks, Kosevich 2006 and Braun–Kivshar 2004, are refs [1], [3] of the cited 1806.11002. Credit them.
- **Quantum crowdion motion in W at low T:** not claimed as new, but the return should cite the prior experimental and theory literature,
  e.g. Arakawa et al., "Quantum de-trapping and transport of heavy defects in tungsten", Nat. Mater. (2020) (title and venue found via OpenAlex;
  [ABS], not read), and Derlet–Nguyen-Manh–Dudarev PRB 76, 054107 (2007), Dudarev Phil. Mag. 83, 3577 (2003) (refs of 1806.11002).
- **DM scattering on TLS (2.4) and dark-photon absorption via tanδ_TLS (2.3):** not claimed new. My lit.py priority searches (arXiv, OpenAlex)
  were inconclusive. **UNRESOLVED**: no novelty may be asserted downstream without a proper priority check (the TLS–DM literature since
  2210.04128 is active).

## 5. Gap-closure sufficiency (rubric e)
The return closes none of G1–G13 outright. IF-T8 cites "CATALOG-B G12", but G12 (triggered avalanches, WP5-v3) stays [C] (G-T4). That is
honest, but IF-T8 should not suggest otherwise. Specs:
- §2.7 is sufficient after the fp correction (§1.2) and with the ε_e⁻¹ screening factor added.
- §3.4 is sufficient.
- §4.6/§5.4 are **insufficient** for the eV-release (Frenkel-pair) class. J^{sb} must include the local/optical-mode Huang–Rhys couplings
  S_HR,k (the same inputs as (4.4)). The λ ≤ 24 class split must be replaced by the computed Γ(ε, λ, S_HR) with the θ_λ factor, and α_ohm (G-T1)
  is a prerequisite for every metal host, not just a nuisance.

## 6. Notation / consistency (rubric d)
- K = kinematic regime only (NOTATION); `K=def` must go; keep `ref=def(STM|band|cr)`.
- ω₀ is already a NOTATION row (Einstein/toy frequency), and an attempt rate Γ_att exists (WP5 rows). Rename the attempt frequency (e.g. ω_att)
  or reuse Γ_att. The crowdion well frequency ω₀ (§3.2) is a third use.
- 𝒳 entries must be rungs; "host ε" belongs in scr.
- Rung-4 rubric items checked with no error found: Bose and thermal factors (coth, tanh, detailed balance), phonon normalisation
  (2ρVω)^{-1/2}, sign of q (e^{+iq·x} core term), DM kinematics (η/2q, ξ(0) = ⟨\|v\|⟩, σ̄_e at q₀), WP0 (3.1) normalisation. The double-pole
  resonant denominator (§1.2) and screening (§1.3) are covered above.

## 7. Required corrections (summary)
S: pole rule → Hadamard fp (§1.2); (2.4) window q ≪ q_×, or include 𝔣^core (§1.6); §4.2 window only for ε ≲ ω_D, plus the λ-convention
factor θ_λ (§1.10); kinetics spec bath for eV releases (§5).
W: K=def; scr leading correction; C4c settled via 2103.06977 and G-T5 edited; tanδ misquote; double tanh in (2.3); P̄ parenthetical;
M_cr not new; W band ≈ 0.03 meV and bulk-W normal state; (4.4) T = 0; α_ohm = 4K; transverse factor; f-sum wording; §2.5 bound ≈ 2×10⁻²⁰;
delete C14f; notation ω₀.
