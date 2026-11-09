# R11 referee report REF-WP7-B2-B (hostile, isolated) on returns/R10/WP7-B2.md

Scope: returns/R10/WP7-B2.md and code/WP7-B2/checks.py (re-run: 31/31 PASS, ≈ 5 s). Read: WP0-v3, CONVENTIONS, NOTATION, CONTROLS, DONE, LIMITS.
Full texts fetched to literature/papers-r11-WP7-B2-B/ and deleted after use: 2308.06314, 2601.01043, 2512.16451, 1705.03016, 2301.07617, 2312.10566.
Prior-art search (lit.py arxiv): cond-mat/0604205 (Taraskin et al., abstract read [ABS]). No simulations; my sympy checks took < 10 s.

## Verdict table
| # | Main claim | Verdict | Reason (details in §§ below) |
|---|---|---|---|
| 1 | A4 one-phonon absorption (B2.1.1)–(B2.1.3); coupling-to-mass rule; electron-scalar vertex Z − Z*, GaAs ×0.47 | STANDS WITH CORRECTION | Formula and limits verified against 2308.06314 Eqs. (2), (7), (14), (16), (42), (44) [FT]. But the "rigid-ion source defect" is overstated: 2308.06314 footnote 2 states the rigid-ion assumption itself and gives the Born-charge fix δZ = Z* − Q_j. ×0.47 just applies that footnote to the electron row. Acoustic-mode kinematic condition misstated (R1) |
| 2 | Random-coupling broadband theorem (B2.2.1); S5 = 2411.10542 Eq. (31) | STANDS WITH CORRECTION | Algebra correct (C5, C14). (R3) "independent of the eigenvectors" fails at O(ΔM/M) wherever the random vertex sits on an isotope (²⁹Si, isotope channel). The return lists this as an [E] correction, but the theorem is stated as exact (R2) |
| 2a | Isotope-disorder channel for B−L in monatomic crystals is "new" | STANDS WITH CORRECTION (novelty UNRESOLVED) | No prior art found in a limited search. The claim is incomplete: the EM-current part of B−L (Z·[nuclei − electrons]) absorbs through Si's two-phonon ε(ω) at O(k⁰), and the return never compares it with the isotope term. σ_γ² should be mass-weighted: 1.88×10⁻⁴, not 1.78×10⁻⁴ (R3) |
| 2b | A7: local neutrality ⇒ C^{IR} ∝ ω² below the boson peak [D, sketch] | FALLS (as stated) | Prior art cond-mat/0604205 gives C(ω) = A + Bω². A ≠ 0 comes from charge fluctuations that obey only global neutrality; local neutrality gives the Bω² term. The return's own incoherent estimate is the A term, so a pure ω² law is not implied (R4) |
| 3 | L10: exact Gaussian S for a disordered harmonic solid (B2.2.4); closes WP2 gap 6 at formula level | STANDS | Bloch's identity holds for any Gaussian state. The configurational split and the g₂ correction are properly labelled [D, sketch]. The spec (§2.5) is sufficient for a formula-level closure |
| 4 | §10(iii): 2512.16451 Eq. (12) = n_ph = 0 term; Born fails at the MICROSCOPE reach | STANDS WITH CORRECTION | Eqs. (2), (7)–(12), (14) quoted correctly. I re-derived Eq. (12) (the return did not: "standard algebra" breaks DONE rung 1). V_opt/E_kin = 1.86 at 4×10⁻³⁸ cm², 20 eV: CONFIRMED. The validity statement in row B2-L4 needs to be made precise, and 2W ~ 10⁻¹⁷ is wrong (R5) |
| 5 | L11 solid He: SCHA replacement (B2.4.1); 2409.02439 = QH limit | STANDS | The f-sum holds for any Gaussian (it holds for any local H). The Lindemann numbers are [E]. The interference term is correctly [UNVERIFIED]. Not checked against 2409.02439 full text (no defect is claimed there) |
| 6 | S2: (B2.5.1) = 2005.10256 Eq. (27), 2001.10666; Larmor theorem (B2.5.2); Polder factor (B2.5.3) | STANDS WITH CORRECTION | Algebra verified, including detailed balance 2⟨S^z⟩/(1 − e^{−βω_L}). The Larmor statement is textbook (the uniform resonance is unshifted by isotropic exchange), so it is not a result of this return: cite it. Notation clash ω_L and m_s (R6) |
| 7 | S6: neutron-data spin S (B2.6.1)–(B2.6.2); q̂q̂ part not measured | STANDS WITH CORRECTION | Dictionary C9 is right. The numerical example for g ≠ 2 is wrong: for a quenched 3d ion (Ni²⁺) λ_S = 1, not g − 1. The bracket is (2/g)² ≈ 0.83, not 1.19 (R7) |
| 8 | L9/S8: magnetisation is two-phonon (B2.7.1); L^{ph} not conserved; SMM line (B2.7.2); 2601.01043 defects | STANDS WITH CORRECTION | (B2.7.1) verified (C20). The L^{ph} non-conservation is right but known: Zhang–Niu pseudo-angular momentum, to be cited. 2301.07617 itself calls κ an estimate. (B2.7.2) omits the S⁺ branch, which carries the metastable-well line that SMM avalanche detectors actually use (R8) |
| 9 | X10: exact crystal identity (B2.8.1)–(B2.8.2); reduces to 2312.10566 Eq. (17) | STANDS WITH CORRECTION | Identity verified via WP0 (4.8). Dilute limit = Eq. (17) (C11b) [FT]. The medium correction has the wrong sign and size: n_r/\|ε\|² = 1 + (3/2)ω_p²/ω² (≈ +4×10⁻⁴ at 1 keV), not 1 − O(ω_p²/ω²) (R9) |
| 10 | D2 colour centres (B2.9.1); 1705.03016 Eq. (1) as limit; Eq. (6) Δp underestimated | STANDS WITH CORRECTION | Limit and quotes are correct [FT]. Δp claim CONFIRMED. The source's footnote 2 (quantum effects shift the threshold by ≲ 15%) and its statement that Eq. (1) counts dislocations, not specific defects, should be credited (R10) |
| 11 | D5 bond breaking (B2.10.1) | STANDS | Factorisation exact under (M). The caveat that (M) fails for dissociative final states is covered by p_esc |
| 12 | Source defects list (§0 row 12, §12, IF-B2-9) | STANDS WITH CORRECTION | Two misprints CONFIRMED; 2512.16451 CONFIRMED; 2601.01043 n_r/\|ε\|² CONFIRMED. The 2308.06314 "rigid-ion vertex" and the 2301.07617 "κ estimate" are the sources' own stated approximations, not defects (§C) |

## A. Rubric (c): claims that published papers are wrong (all checked against full text)
| Claim | Rating | Evidence |
|---|---|---|
| 2308.06314 Eq. (48) printed linear in g_aee | CONFIRMED | HTML LaTeX: `R\approx\frac{1}{4}\frac{g_{aee}}{e}\frac{\omega}{m_e}…`. Eq. (49) g_aee ~ 10⁻⁹(100 meV/ω)(κ/10⁻¹⁶) follows from the square: g = 2eκm_e/ω = 3.1×10⁻¹⁰ (≈ the "∼10⁻⁹"); the linear form gives ~10⁻²⁵ |
| 2601.01043 Eq. (12) printed linear in g_aγγB₀/m_a | CONFIRMED | HTML LaTeX: `R\simeq\left(\frac{g_{a\gamma\gamma}B_0}{m_a}\right)\frac{\rho_{DM}}{\rho_T}…`. Eq. (13) g ~ εm_a/B₀ needs the square; the square also matches WP0 (2.9) |
| 2601.01043 dark-photon rate uses ε → 1; URF factor n_r/\|ε\|² | CONFIRMED | Text: absorption "rescaled by the relative permittivity of the SMM, which can be approximated as unity [23]". Ratio n_r/\|ε\|² is exact algebra (C13c). Quote fix: R is Eqs. (17)–(18) with (9)–(10) inserted; Eqs. (9)–(10) alone are ⟨nσv⟩ ≈ ε²⟨nσ^γ⟩, σ^γ = α/n |
| 2512.16451 Born outside validity at its reach | CONFIRMED | Reach "4×10⁻³⁸ cm² around m_χ ≃ 0.02 keV" (text). n₀ = 2.69×10²⁴ cm⁻³ is the nucleon density (Eq. (14), App. A Eq. (25)), consistent with σ_χN per nucleon. My check gives V_opt/E_kin = 1.86 and σ_crit = 1.16×10⁻³⁸ cm². The full text has no refraction, reflection or optical-potential discussion (searched) |
| 2308.06314 electron-scalar vertex is rigid-ion | CONFIRMED (fact); REFUTED as "defect" | Main text: "N_{Ga,e} = 28, N_{As,e} = 36" (after Eq. (44)). Footnote 2: "Eq. (38) is derived assuming that the electronic wave functions do not distort … δn_{ℓj,e} ≡ iq^iδZ^{ik}_ju^k_{ℓj}, δZ ≡ Z* − Q_j". The fix is the source's own. Reword as "rigid-ion approximation stated in its footnote 2; applying its own Born-charge prescription to the electron row changes the GaAs rate by ×0.47" |
| 1705.03016 Eq. (6): Δp ~ αm_e underestimates the spread | CONFIRMED | Text: "uncertainty in the position of the nucleus is of order the Bohr radius, it follows that Δp ∼ αm_e". The zero-point value is (Mω/2)^{1/2} ≈ 6.9 keV per component, √3 larger for the magnitude; Δp/q_min ≈ 0.05–0.09, so the conclusion holds. The source's footnote 2 already estimates "≲ 15%" on the threshold |
| 2301.07617: angular-momentum conservation is not a decay selection rule; κ is an estimate | CONFIRMED (substance); not a defect for κ | The source invokes "conservation of phonon angular momentum as a selection rule for phonon decay processes [61]". C10 is correct: only C_n pseudo-angular momentum survives. But the source itself says κ = 15% "is an estimate", with "each decay pathway … equally likely", because three-phonon couplings are "computationally prohibitive". Credit that; the novel content is only the selection-rule point, which is known (Zhang–Niu PRL 115, 115502 (2015) [UNVERIFIED citation]) |

## B. Rubric (b): proposed LIMITS rows
- B2-L1 ✔ with ✎: the quotes of Eqs. (2), (7), (14), (16), (40)–(44) are correct. Replace "✎ electron scalar Z − Z*" with "applies 2308.06314 fn. 2 to the electron row". The Eq. (48) square is correct.
- B2-L2 ✔ (C5 algebra). Add the O(ΔM/M) eigenvector–vertex correlation as the leading correction (spin isotope = mass isotope).
- B2-L3 ✔ for (B2.3.1). Remove "C^{IR} ∝ ω²"; the low-ω form is A + Bω² (cond-mat/0604205 [ABS]), with A estimated by (B2.2.1).
- B2-L4 ✎ must read: "Born plane-wave on the medium valid for V_opt/E_kin ≪ 1, i.e. σ_χN ≪ σ_crit = m_χ⁴v⁴/(4πn₀²) (μ_χN ≈ m_χ). The bulk phase
  kRV_opt/2E_kin ≫ 1 is a uniform shift that drops out of the fluctuation cross-section in DWBA (k → k′), leaving O(V_opt/E_kin) corrections
  plus surface refraction. Above σ_crit the force is reflection-dominated." As written, §3 says DWBA is needed even below σ_crit while the row says
  "valid only for σ ≪ σ_crit": the two statements must be reconciled.
- B2-L5 ✔ (QH limit structure). B2-L6 ✔. B2-L7 ✔ plus the λ_S correction (R7). B2-L8 ✎ plus the S⁺ branch (R8). B2-L9 ✔ with the sign/size fix (R9).
  B2-L10 ✎ with source credits (R10).

## C. Required corrections (R-numbered)
- **R1 (§1).** "Acoustic modes cannot absorb (ω = c_νk ≪ m_φ for c_ν ≪ v)": the condition is c_νv ≪ 1, from ω_ac(k_φ) = c_νm_φv. Rewrite the source-defect
  sentence per §A. The electron-scalar vertex is fine for TO modes; for LO modes the macroscopic-field electron response sits in 𝒟^γ. State that
  R̃ means zero macroscopic field, so Z* (not Z_κ − Z*_κ plus a χ_∞ term) is the right input.
- **R2 (§2.1).** Restate (R3) as exact only when the random vertex is independent of the masses (nuclear-spin orientation at fixed isotope). For vertices
  tied to isotopes (S5 spin isotopes, §2.4), (B2.2.1) is the leading term, with O(ΔM/M) corrections from vertex–eigenvector correlation. Use
  isotope-class-resolved D_κ(ω) from the disordered Hessian.
- **R3 (§2.4).** (a) "New" stays UNRESOLVED: no prior art found, but the search was limited. (b) Decompose the B−L current as N_I·(nuclear) + [Z_I·(nuclear) − electrons].
  The second part is EM-like (dark-photon-like, κe ↔ g) and absorbs via Si's measured ε(ω) in the two-phonon band (∂Z*/∂u, §1 item (iv)) at O(k⁰).
  The isotope channel is additive to it and must be compared before any claim of leading broadband absorption. (c) v̄ = Σv/ΣM gives a mass-weighted
  mean, γ̄ = Σ(A−Z)/ΣM. The relevant weight is Σx_IM_I(γ_I − γ̄)²/(M̄γ̄²) = 1.88×10⁻⁴; C4a uses number weights and A for M (1.78×10⁻⁴).
- **R4 (§2.3, gap 1).** Replace "C^{IR} ∝ ω² below the boson peak" with C^{IR}(ω) ≈ A + Bω². A comes from fluctuating charges constrained only by global
  neutrality; it is estimated by the incoherent form (B2.2.1). Bω² comes from locally neutral units. Cite cond-mat/0604205. Mark the A/B split [E] until
  computed from the glass models of §2.5.
- **R5 (§3).** (a) Replace "standard algebra, not re-checked" with the derivation: ∫d³r e^{iq·r}e^{−r/ξ} = 8πξ³/(1+q²ξ²)², over N_tot² = n₀²(4πR³/3)²,
  times V, gives Eq. (12) exactly (bulk limit, boundary terms dropped). (b) 2W(q) at q = 0.1 eV is q²⟨u²⟩ ≈ (5×10⁻⁵ Å⁻¹)²×5×10⁻³ Å² ≈ 10⁻¹¹,
  not 10⁻¹⁷ (still negligible). (c) Reconcile with B2-L4 (§B).
- **R6 (§5, notation).** NOTATION reserves ω_L for the LO frequency and ω_Lar ⚠ for Larmor (row 141). m_s is the species mass in WP0 (4.8)
  (ρ_M = Σ_sm_sn_s) and in R^{phys} (row 462), and §8 of this return uses ρ_M. Rename to ω_Lar and, e.g., 𝔰_net. "Collisions checked" is false
  for these two. Cite the Larmor statement as standard ESR theory: isotropic exchange commutes with S_tot.
- **R7 (§6).** λ_S = g_J − 1 holds only inside an LS J-multiplet (unquenched 4f). For quenched 3d ions (Ni²⁺, g ≈ 2.2 from SOC admixture) ⟨s⟩ = S, so
  λ_S ≈ 1 and the bracket is [1/(g/2)]² ≈ 0.83, not 1.19. The same fix applies to §5 "orbital moments (λ_S = g − 1 ≠ 1)".
- **R8 (§7(d)).** (B2.7.2) must include the S⁺ branch: + 𝓃_mol2πλ_S²(k_⊥²/4)Σ_mp_m[S(S+1) − m(m+1)]δ(ω + D_ZFS(2m+1) + ω_Z). An SMM avalanche detector
  (2601.01043 Eqs. (4)–(6): barrier U − ½ΔE_Zee) is prepared in the metastable well m = −S. Its absorption line is D_ZFS(2S−1) − ω_Z with weight 2S
  (my sympy check), not D_ZFS(2S−1) + ω_Z. As written, "at T → 0 one line at D_ZFS(2S−1) + ω_Z" describes the wrong population for the detector.
- **R9 (§8).** n_r/\|ε\|² with ε = 1 − ω_p²/ω² is 1 + (3/2)ω_p²/ω² + …: +4.1×10⁻⁴ at 1 keV in Si (C15 computes (ω_p/ω)² only and the text gives
  the sign as "1 − O"). Conclusion unchanged.
- **R10 (§9).** Credit 1705.03016's footnote 2 (≲ 15% quantum shift of the threshold), consistent with the return's ≈ 10% Doppler smearing. Also credit
  its sentence that Eq. (1) "is that for creating a dislocated nucleus … not … a specific defect type". The f_opt and p_q corrections are then
  refinements the source anticipated, not omissions.
- **R11 (notation, §2).** λ as a disordered-mode label clashes with NOTATION (λ ⚠ = exciton label, row 202; W2 "λ" modes were renamed ν, row 105). It
  also sits in the same formula as λ_I (spin coupling, §2.2). γ_I (B−L charge per mass) and γ_λ (linewidth, (B2.3.1)) share §2. Use ν (or 𝔪) for
  modes and a distinct symbol for the B−L ratio.
- **R12 (τ strings).** `X=data` puts a non-kernel value in the 𝒳 slot (CONVENTIONS §11 lists kernel rungs only). `ref=exact(Larmor)` is an unflagged
  new metadata value. `K=1ph-inc;ref=glass` mixes an order slot into metadata. Add these to the IF table (IF-B2-2, -3, -10 cover only part).

## D. Rubric (a), (d): derivation status and consistency
- Verified as derived with stated hypotheses: (B2.1.2) = 2308.06314 Eq. (2)+(16) (C1); (B2.1.3) (orthogonality to √M ê, WP0 (4.8)(i)); (B2.2.1)
  (C14); (B2.5.2) (C7 plus my detailed-balance check); (B2.5.3) (C8); (B2.6.1) inversion of 2504.02927 Eq. (26) (C9c); (B2.7.1) (C20); (B2.8.1) (C11a:
  [H,[H,X]] = ∂V/M) and (B2.8.2) (WP0 (4.8): ⟨f|ρ_M(k)|i⟩ = O(k²)); (B2.10.1) under (M).
- Consistent with WP0-v3 (3.5)–(3.6), (2.9), (4.1), (4.8) and with CONVENTIONS §5 (u normalisation, √N𝒱 bookkeeping).
- [D, sketch] labels are honest for the distinct terms of (B2.2.4), the DWBA, the beyond-SCHA terms and the orbit–lattice one-phonon moment. The C^{IR}
  low-ω law is the only [D, sketch] item contradicted by prior art (R4).
- DONE rung-4 items: Bose factors correct in (B2.2.1), (B2.5.2), (B2.6.2), (B2.7.2) (apart from R8). Umklapp present in (B2.7.1). Screening counted once
  (X10 via ε_e at ω ≫ ω_max; A4 photon-reducible part via 𝒟^γ). The sign of q is immaterial here (P,T-even targets; noted in §6).

## E. Rubric (e): gap-closure sufficiency
- WP2 gap 6 (amorphous S): formula plus spec (MLIP quench, ≥ 5 configurations, finite-size gap criterion, n_ph ≤ 2 module) is sufficient at formula level.
  The C^{IR} low-ω extrapolation must use A + Bω² (R4).
- §10(iii): DWBA/transfer-matrix spec sufficient for a(σ, m_χ) with regime marks. The reflection regime is correctly left as an exact gap.
- S6 data route: sufficient for P_T-projected couplings. The longitudinal part is correctly declared an exact gap.
- SMM spec: insufficient until the S⁺/metastable branch is added (R8).
- Isotope channel: the spec lacks the competing EM-like two-phonon term (R3b), so it does not yet close "B−L in Si".

## F. Rubric (f): novelty
- Isotope-disorder B−L channel: UNRESOLVED. Limited arXiv search, no prior hit; keep "new" only as "not found in the literature searched [E for novelty]".
- Larmor theorem, Kittel/Polder ellipticity, L^{ph} non-conservation: known physics. The return should cite, not present them as results.
- X10 crystal identity: a direct corollary of WP0 (4.8); not claimed new; fine.
- C^{IR} ∝ ω²: superseded by prior art (cond-mat/0604205).

## G. Checks script
- 31/31 PASS reproduced. Weak points: C4a uses number weights (R3c). C15 checks the magnitude but not the sign of the correction (R9). C16 covers only the
  S⁻ branch from m = S (R8). C10 is a 6×6 toy that illustrates rather than proves; the general statement follows from u^TDJu = ½u^T[D,J]u, which
  should be written in the text. C12 is fine.
