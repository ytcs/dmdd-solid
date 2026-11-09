# R11 referee report REF-WP7-B2-A (hostile, isolated)

Under review: returns/R10/WP7-B2.md and code/WP7-B2/checks.py. Read: WP0-v3, CONVENTIONS, NOTATION, CONTROLS, DONE, LIMITS.
Full texts fetched for this report (literature/papers-r11-WP7-B2-A/, deleted afterwards): 2308.06314, 2601.01043, 2512.16451,
1705.03016, 2411.10542, 2312.10566, 2301.07617. checks.py re-run: 31/31 PASS, 1.4 s. The check count of 31 is correct.
Sympy re-checks done for this report (all under 2 min): the LO residue of the full R in a one-mode model, the GaAs vertex numbers,
the B−L isotope variance, and the Debye form factor (2512.16451 Eq. (12)).

## Verdict table
| # | Claim | Verdict | Reason (details in the numbered sections) |
|---|---|---|---|
| 1a | (B2.1.1)–(B2.1.2) reproduce 2308.06314 Eqs. (2), (7), (16), (42) | STANDS | C1a/b re-run. Eq. (42) checked against the full text (q → k) |
| 1b | Coupling-to-mass rule "derived for any basis and any row" | STANDS WITH CORRECTION | Already general in the source (Eq. (44), "exact for g_Ψ ∝ m_Ψ"). The source's subtraction is a different projection (§1.2) |
| 1c | Electron-scalar vertex Z_κ − Z*_κ; "GaAs rate ×0.47" | **FALLS** (rate); vertex STANDS as the photon-proper vertex | The observable LO residue carries Z_κ − Z*_κ/ε_∞. The ratio is ≈ 0.1, with O(1) sensitivity. The source's footnote 2 already gives the δZ correction (§1.3) |
| 2a | Random-coupling broadband theorem (B2.2.1) | STANDS WITH CORRECTION | Algebra correct (C14). (R3) "δv independent of e_Iλ" is false for isotope disorder and for spin isotopes, at O(σ_M/M). v̄ needs the mass-weighted γ̄ (§2.1) |
| 2b | S5 = 2411.10542 Eq. (31) exactly | STANDS | Eq. (31), (27)–(29) verified in the full text; C5 re-run |
| 2c | Glass ε (B2.3.1); A7 = L9b with the glass ε | STANDS | Standard rank-1 form, HL units consistent |
| 2d | Low-ω law C^{IR} ∝ ω² from local neutrality; "(R3) fails at low ω" | **FALLS** | Prior art: Taraskin et al., cond-mat/0604205 (PRL 97, 055504), C(ω) = A + Bω². A, from globally neutral charge fluctuations, survives as ω → 0 (§2.2) |
| 2e | Isotope-disorder channel for B−L, "new"; σ_γ²/γ̄² = 1.8×10⁻⁴ | STANDS WITH CORRECTION | Physics correct. The number should be 1.88×10⁻⁴ (mass-weighted γ̄, real masses). Novelty UNRESOLVED (§2.3) |
| 3 | (B2.2.4) disordered Gaussian S; WP2-v3 gap 6 closed at formula level | STANDS WITH CORRECTION | Self term [D]. S_dist at n_ph ≥ 2 is [D, sketch]. "Closed" must read "closed for S_self, sketch for S_dist" |
| 4 | 2512.16451 Eq. (12) = n_ph = 0 term; Born fails at its claimed reach | STANDS | CONFIRMED against the full text: the paper invokes Born explicitly, n₀ = 2.69×10²⁴ cm⁻³ (Eq. (14)), reach 4×10⁻³⁸ cm² at m_χ ≃ 0.02 keV. V/E = 1.85 re-derived. Eq. (12) algebra verified (§3) |
| 5 | Solid He: SCHA S (B2.4.1); 2409.02439 Eqs. (4)–(5) = QH limit | STANDS | Bloch and the f-sum hold within the Gaussian. Beyond-Gaussian items are honestly marked [D, sketch]/[UNVERIFIED] |
| 6 | Magnon absorption (B2.5.1); Larmor theorem (B2.5.2); Polder factor (B2.5.3) | STANDS WITH CORRECTION | All three algebras verified. The Larmor theorem is textbook (cite it). It holds at any T. λ_S = g − 1 only for J multiplets (§4) |
| 7 | Neutron-data S (B2.6.1)–(B2.6.2); q̂q̂ part unmeasured | STANDS WITH CORRECTION | Formula and caveats correct. The Ni²⁺ example is wrong: quenched orbit gives λ_S ≈ 1, a bracket of ≈ 0.83, not 1.19 (§4.2) |
| 8a | Born-charge phonon magnetisation is two-phonon (B2.7.1); C20 | STANDS WITH CORRECTION | Operator algebra correct. "Magnetic-dipole DM ⇒ chiral phonons in pairs" is wrong in scope: the one-phonon j_T vertex exists at O(q) (§5.1) |
| 8b | No phonon angular-momentum conservation in decay (C10) | STANDS | [H,L] = 0 iff [D,J] = 0 re-derived. 2301.07617 does assert a selection rule (full text). Its κ is self-described as an estimate, so "κ is an estimate" is not a finding |
| 8c | SMM line (B2.7.2) | STANDS WITH CORRECTION | The S⁺ branch from m < 0 populations is missing. This is the bistable SMM case (§5.2) |
| 8d | 2601.01043 Eq. (12) printed linear; ratio n_r/\|ε\|² for its Eqs. (9)–(10) | STANDS | Both CONFIRMED in the full text (HTML alttext and PDF) |
| 9 | X10 identity (B2.8.1)–(B2.8.2); 2312.10566 Eq. (17) as the dilute limit | STANDS WITH CORRECTION | Identity and dilute limit verified. The screening-correction size (C15) is underestimated about 4× (§6) |
| 10 | D2 seeding formula (B2.9.1); 1705.03016 Eq. (6) Δp underestimated | STANDS | CONFIRMED: the source takes Δp ~ αm_e from a "Bohr-radius" position spread. Its conclusion is unaffected |
| 11 | D5 factorisation (B2.10.1) | STANDS | Exact under hypothesis (M), which must include orientation independence (free rotor) |
| 12 | 2308.06314 Eq. (48) misprint | STANDS WITH CORRECTION | CONFIRMED linear (HTML alttext). The squared form gives 3.1×10⁻¹⁰ against the printed "10⁻⁹": a residual factor ≈ 3 to state. "Rigid-ion source defect" must be softened (§1.3) |
| C | Consistency with WP0-v3 / NOTATION / CONVENTIONS | STANDS WITH CORRECTION | Notation collisions ω_L and m_s. Spin-ordered targets are placed in the Theorem D GS sector. τ strings lack the mandatory T (§7) |

---
## 1. A4 single-phonon absorption

**1.1 (B2.1.1)–(B2.1.2).** The prefactor identity C1b, (y²/2ω)(2π/Ω)|F·T|² = (1/ω)(y²/Ω)|F·T|²π, is correct. Eq. (42) of 2308.06314 reads
R ≈ (g²/e²)(q²/ω²)(ρ_φ/ρ_T)Im[−1/ε]. This matches the return. Minor point: "acoustic modes cannot absorb (… for c_ν ≪ v)" has the wrong
condition. Matching ω = c_νk = c_νm_φv to m_φ needs c_νv = 1, so the true statement is c_νv ≪ 1, which always holds. Fix the wording.

**1.2 Coupling-to-mass.** 2308.06314 states Eq. (44), Σ_j m_jT_jνq ≈ 0, and calls the cancellation "exact for couplings g_Ψ ∝ m_Ψ".
That is already basis- and row-general, so "derived here for any basis and any row" adds nothing. The return also writes "This is …
their subtraction F_j → F_j − m̂_jΣF·m̂". The source defines m̂_j = m_j/√(Σm_j²) (alttext checked). That is an orthogonal projection,
λ = Σv·m/Σm², whereas the return's δv uses λ = Σv/ΣM. Both leave the vertex unchanged, because Σ√M_κ e_κν = 0 for any λ. The
subtracted "form factors", however, are not unique: the source's "×10 smaller" refers to its projection only. Correction: say the
vertex is invariant under v_κ → v_κ − λM_κ for any λ, and drop "CONFIRMED, generalised" in favour of "CONFIRMED".

**1.3 Electron-scalar vertex and "GaAs ×0.47" (FALLS as stated).**
(i) The vertex c_e k·(Z_κ𝟙 − Z*_κ) is the photon-proper (R̃) vertex: Z* is defined at zero macroscopic field. For isotropic Z* a
scalar row couples only to the longitudinal polarisation, k̂·e. In the full R of WP0 (3.6) the TO pole cancels and only the LO
pole survives. Sympy, with a one-mode model (R̃_OO = a²P + χ, R̃_Oc = abP − χ, R̃_cc = b²P + χ, P = (ω² − ω_T²)⁻¹, ε_∞ = 1 − v_Cχ), gives:
 Res_{LO} R_OO = [a + b(1 − 1/ε_∞)]².
For an electron-number row this is the vertex **Z_κ − Z*_κ/ε_∞**: the electrons also screen the LO macroscopic field. The quantity
that enters Γ_net in (B2.1.2) is therefore not the "δv by 0.68" of C3.
(ii) GaAs numbers (Z* = 2.1, ε_∞ = 10.9; masses as in C3), as d = v_Ga/M_Ga − v_As/M_As:
- rigid proper: −0.0789;
- URF proper: −0.0540;
- URF physical, Z − Z*/ε_∞: **−0.00117**.
The source's own Eq. (41) carries the electronic mixing term −ωq(1 − ε_∞)g_e/e and rigid ionic charges Q_j = ±3. Its LO vertex
is then N_e + Q(1 − 1/ε_∞) = Z − Q/ε_∞, with d = −0.00346. Observable ratio URF/source ≈ (0.00117/0.00346)² ≈ **0.11**, not 0.47.
Because Z_Ga/M_Ga ≈ Z_As/M_As (0.4446 vs 0.4405), this residual is a near-cancellation. A 10% change in Z*/ε_∞ moves d by ≈ 40%.
The claim must be restated: physical LO vertex Z_κ − Z*_κ/ε_∞, rate strongly suppressed and sensitive to Z*, ε_∞ and isotopic
masses. C3 must compare residues, not proper vertices.
(iii) "Source defect: rigid-ion vertex" (§0 item 12, IF-B2-9, B2-L1 ✎) is overstated. 2308.06314 footnote 2 writes
⟨ψ†γ⁰ψ⟩ ≈ n_e + δn_e with δn_{ℓj,e} = iq^iδZ^{ik}_ju^k and δZ = Z* − Q_j. It states this for the photon coupling and refers to its
Ref. [72]. Rating: **UNRESOLVED/partly CONFIRMED.** The main-text illustration (N_Ga,e = 28, N_As,e = 36) is rigid-ion. The
mechanism is acknowledged in the source, and whether its GaAs projection in Fig. 2 includes δZ is not determinable from the text.

**1.4 Eq. (48) misprint.** CONFIRMED. The alttext reads R ≈ (1/4)(g_aee/e)(ω/m_e)(ρ_φ/ρ_T)Im[−1/ε], and Eq. (49) needs the square
(C13b). The squared form with e = √(4πα) gives g_aee = 3.1×10⁻¹⁰ at 100 meV and κ = 10⁻¹⁶, against the printed "10⁻⁹". That is a
factor ≈ 3, not "~". State the residual factor (an O(1) prefactor in the source or in the inferred square), or say "order of magnitude".

## 2. Random couplings and glasses

**2.1 (B2.2.1).** The configurational algebra is correct (C14, ∫D_I = 1 by completeness).
Hypothesis (R3) requires the δv_I to be independent of the eigenvectors. For isotope disorder (§2.4), δv_I ∝ M_I(γ_I − γ̄) is a
function of the masses that also shape e_Iλ. The same holds for ²⁹Si spin carriers (spin sites are mass-29 sites). The return
acknowledges this only as correction (i) in §2.2. Here (B2.2.1) is exact only to leading order in σ_M/M̄; label it [D] at
O((σ_M/M)⁰) and [E] for the correlation correction.
The mass subtraction also requires v̄ = Σv/ΣM. For B−L this is γ̄′ = Σx(A − Z)/ΣxM, the mass-weighted mean. C4a uses the
number-weighted mean and integer A. With γ̄′ and real masses, the rate weight Σx_IM_I(γ_I − γ̄′)²/(M̄γ̄′²) = **1.88×10⁻⁴**,
not 1.78×10⁻⁴. This is 5%; correct the number and C4a.

**2.2 C^{IR}(ω) low-ω law (FALLS).** The return claims local charge neutrality gives C^{IR} ∝ ω² below the boson peak, so (R3)
"fails at low ω". The established result (Taraskin, Simdyankin, Elliott, Neilson, Lo, cond-mat/0604205, abstract checked;
theory, THz data and simulations) is C(ω) = A + Bω²:
- A comes from fluctuating charges obeying global neutrality (the incoherent term);
- B comes from those obeying local neutrality.
As ω → 0 the constant A dominates, so the incoherent estimate is the low-ω limit, not its failure. The symbol C^{IR} ("introduced
here") and the IR-to-VDOS coupling function are prior art (Galeener–Sen; Taraskin–Elliott); cite them. Exact-gap item 1 must be
rewritten: "C^{IR} = A + Bω² (literature); A and B from glass models".

**2.3 Isotope channel novelty.** Not found in my arXiv searches (isotope + dark matter + phonon; coupling-to-mass + isotopes), and
2308.06314 has no "isotop" occurrence. Disorder-induced one-phonon IR absorption in homopolar crystals is old solid-state physics.
Rate: novelty UNRESOLVED. Replace "new" by "not found in the literature searched [E for novelty]".

**2.4 (B2.2.4) and gap 6.** Bloch's identity for a Gaussian state and the self/distinct split are fine. The n_ph ≥ 2 distinct term
is a sketch. Formula plus specification is sufficient for S_self and for S_dist at n_ph = 1 (Hessian, then direct sum). S_dist at
n_ph ≥ 2 needs the stated pair weighting to be derived, not sketched. "Closes gap 6 at formula level" is too strong: say
"closes it for S_self; S_dist at n_ph ≥ 2 [D, sketch]".

## 3. §10(iii) and 2512.16451 (CONFIRMED)
The full text states "Given the weakness of the DM interaction, the Born approximation can be employed" (§II). It uses
n₀ = 2.69×10²⁴ cm⁻³ (Eq. (14)) and claims MICROSCOPE sensitivity to σ_χN ≈ 4×10⁻³⁸ cm² at m_χ ≃ 0.02 keV (§IV). The words
refraction, reflection and optical potential are absent. My recomputation: V_opt = 2π𝔟n₀/m_χ = 1.85×10⁻⁵ eV, E_kin(v = 10⁻³) =
1.0×10⁻⁵ eV, and σ_crit = 1.16×10⁻³⁸ cm². Eq. (12) re-derived: the FT of δn²e^{−r/ξ} is 8πξ³/(1 + q²ξ²)², giving
(δn²/n₀²)6ξ³/(R³(1 + q²ξ²)²). The return's "not re-checked symbolically" can be upgraded.
Correction (wording): V_opt/E_kin ∝ v⁻². The acceleration (Eq. (13)) weights high lab speeds, and at v = 1.2×10⁻³ (typical) the
ratio is still ≈ 1.3. State the criterion over the f(v) actually used, not at v = 10⁻³ alone. Within one patch the fluctuation
term has phase kξV/2E ≈ 0.2V/E, so the DWBA modification there is mostly the refracted k′ and surface reflection. The return's
"[C for any limit]" is the right status. The paper's bound may be weaker or stronger; this report does not claim a direction.

## 4. Spin targets
**4.1 Larmor theorem (B2.5.2).** Re-derived: weight 2⟨S^z_tot⟩/(1 − e^{−βω_L}) at ω_L, and Γ_abs matches (B2.5.1). It is the standard
Larmor/ESR theorem (Kanamori–Tachiki 1962; Oshikawa–Affleck, PRB 65, 134410 (2002)) [UNVERIFIED citations from memory]: cite it
rather than present it as a result. It holds at any T, not only "below the ordering temperature": in a paramagnet m_s is the induced
moment. Hence "antiferromagnets (m_s = 0) have zero uniform weight" holds only at B₀ = 0, where ω_L = 0 too.
Polder/Kittel (B2.5.3): matrix elements and the factor (ω_x + ω_y)/(2ω_K) ≥ 1 are verified.
**4.2 λ_S = g − 1.** The Landé projection ⟨s⟩ = (g_J − 1)⟨J⟩ holds within a J multiplet (4f ions; 2005.10256 Table 1). For
orbitally quenched 3d ions the pseudo-spin is S itself, ⟨s⟩ = ⟨S⟩[1 − O((λ_SO/Δ)²)], and g = 2 + δg is orbital admixture. Hence
λ_S ≈ 1, not g − 1. In §6 the "Ni²⁺-like g ≈ 2.2: [(1.2)/(1.1)]² ≈ 1.19" should be [1/1.1]² ≈ **0.83**: the correction has the
opposite sign. The §5 leading correction "orbital moments (λ_S = g − 1 ≠ 1)" must be restricted to J-multiplet ions.

## 5. Chiral phonons and SMMs
**5.1 (B2.7.1).** C20 is correct: the M_κ dependence cancels in u × P, the overall prefactor is Z*/M_κ, and the N-normalisation is
correct. The operator 𝐌^{ph} = Σ(eZ*/2M)u × P is indeed bilinear. But a magnetic-dipole DM couples to the full ionic current:
𝐣(q) = Σ_I(eZ*_I/M_I)P_Ie^{iq·R_I} has a one-phonon transverse part, and q × 𝐣 gives one-phonon production at O(q). The return's own
chain lists j_T (WP2-v3 (7.2)). The u × P term is the O(q·u) piece of that expansion, i.e. subleading. Restate the claim: "the
Born-charge orbital moment is a two-phonon operator, so readout through it is quadratic; one-phonon production by magnetic-dipole
DM proceeds through j_T". The current wording ("produces chiral phonons in pairs at T = 0") is false as a statement about
magnetic-dipole DM.
**5.2 (B2.7.2).** The formula keeps only S⁻ terms, [S(S+1) − m(m−1)]δ(ω − D(2m−1) − ω_Z). For p_m > 0 at m < 0 — the metastable −S
well, which is the defining SMM situation at small ω_Z — absorption also proceeds through S⁺. Add
 (k_⊥²/4)Σ_m p_m[S(S+1) − m(m+1)]δ(ω + D(2m+1) + ω_Z).
For m = −S this is a line at D(2S−1) − ω_Z with weight 2S. The T → 0, single-well statement (C16) stands.
**5.3 2301.07617.** The full text says that phonon chirality "adds conservation of phonon angular momentum as a selection rule for
phonon decay processes" and that "due to angular momentum conservation" Γ states decay to chiral phonons. C10 and the pseudo-angular
momentum statement refute that as an exact rule: CONFIRMED. Its κ = 15% is explicitly an estimate ("we assume that each decay
pathway is equally likely"), so listing "κ is an estimate" among the validity issues found (§12, IF-B2-9) is not a finding. Keep
the selection-rule point and κ_URF.
**5.4 2601.01043.** Eq. (12), R ≃ (g_aγγB₀/m_a)(ρ_DM/ρ_T)Im[−1/κ], is linear: CONFIRMED in the HTML alttext. Eq. (13) needs the
square, consistent with WP0 (2.9). Eqs. (9)–(10) and (17)–(18) use σ_abs = α/n with ε → 1, so R_URF/R_src = n_r/|ε|²: CONFIRMED.
The value ≈ 0.25 needs ε at the IR band, where ε₂ is not small; label it [E].

## 6. X10 Migdal-type absorption
(B2.8.1) is verified (C11a, sign and the ω_fi² placement). In (B2.8.2) ⟨f|ρ_M(k)|i⟩ = O(k²) follows from (4.8) with P_tot
conserved. 2312.10566 Eqs. (13)–(17) are verified in the full text; Eq. (17) σ_φ ∝ k/ω and σ_φv ∝ v² agree with (B2.8.2).
Correction to C15: the screening factor n_r/|ε|² − 1 ≈ 3δ with δ = ω_p²/(2ω²) must use all electrons with binding below ω. In Si at
1 keV that is 12 e/atom (L shells included), ω_p ≈ 29 eV, giving ≈ 1.2×10⁻³, not 3×10⁻⁴. Still small; fix C15 and the text.
Scope: for multi-species targets, "c ∝ M" holds only to the mass defect (~10⁻³). The residual is handled by the per-species form.

## 7. Consistency (WP0-v3, NOTATION, CONVENTIONS)
- **NOTATION collisions, despite "collisions checked".**
  - ω_L is the LO frequency in NOTATION v4; the Larmor frequency is ω_Lar ("W2 ω_L" renamed). Rename ω_L → ω_Lar throughout §5.
  - m_s is the species mass of WP0 (4.8) (ρ_M = Σ_sm_sn_s), which the return itself uses in §8. Rename the net spin per cell (e.g. 𝔪_s).
  - λ as a mode label reintroduces the W2 "λ" that NOTATION mapped to ν, and it coexists with λ_κ and λ_{S,j} in (B2.2.2).
    Use ν or a decorated index.
- §1 chain: "Spin-ordered targets add v_κ ∝ ω²𝐒_κ" under "sector GS of Theorem D". WP0-v3 §6.2 puts magnetic insulators outside
  (H2) (FALLS in part, B-V12). Spin-ordered targets need the clamped-nucleus/LSWT route, not the GS sector.
- CONVENTIONS §11: the τ strings omit the mandatory T metadata (e.g. §1 `+ ref=normal;scr=ion`). Proposed values `nA=SCHA`, `X=data`
  and `ref=glass` are correctly flagged as IFs.
- WP0 (3.5)–(3.6), (2.9), (4.8), (5.5)(ii) are cited correctly. L9b dark-photon forms agree.

## 8. Proposed LIMITS rows (rubric b)
| Row | Source quote (FT, checked here) | Chain | Validity / leading correction |
|---|---|---|---|
| B2-L1 | Eqs. (2), (16), (42), (44) ✔; (48) linear ✔ | ✔ for photon-like and nucleon rows | ✎: electron-scalar correction must be Z − Z*/ε_∞ at the LO residue (§1.3). Credit footnote 2 for δZ. Remove "×0.47" |
| B2-L2 | 2411.10542 Eq. (31) ✔ | ✔ | ✔. Isotope-mass correlation (§2.1) is the leading correction, as stated |
| B2-L3 | 2603.22390 not re-fetched | ✔ (L9b) | ✎: replace the low-ω C ∝ ω² by A + Bω² (§2.2) |
| B2-L4 | 2512.16451 Eqs. (2), (12), (14) ✔ | ✔ | ✔ σ_crit. State its v-dependence (§3) |
| B2-L5 | not re-fetched | ✔ | ✔ |
| B2-L6 | 2005.10256 / 2001.10666 not re-fetched (C6 re-run) | ✔ | ✎: λ_S = g − 1 only for J multiplets; Larmor theorem is a known result |
| B2-L7 | not re-fetched (C9 re-run) | ✔ | ✎: g ≠ 2 bracket for quenched ions ≈ [1/(g/2)]² (§4.2) |
| B2-L8 | 2301.07617 ✔; 2601.01043 ✔ | ✔ | ✎ as proposed, plus the S⁺ branch (§5.2) and j_T one-phonon (§5.1). "κ estimate" is not a correction |
| B2-L9 | 2312.10566 Eqs. (13)–(17) ✔ | ✔ | ✔. Correction size ≈ 10⁻³ at 1 keV in Si (§6) |
| B2-L10 | 1705.03016 Eqs. (1), (5), (6) ✔ | ✔ | ✔ |

## 9. Gap-closure sufficiency (rubric e)
- A4 spec: sufficient, once the vertex in the PhonoDark-abs patch is the proper Z − Z* and the mixing term (3.6) is kept with the
  same Z*, so that the code produces the Z − Z*/ε_∞ residue. Patching N_e alone while keeping rigid Q_j in Π_φA would be inconsistent.
- Glass spec (§2): sufficient for D_I, C^{IR}(ω) and ε(ω). The MLIP Z*_I model must reproduce charge fluctuations (the A term), not
  only local neutrality.
- §10(iii) spec (transfer matrices): sufficient for a slab. MICROSCOPE cylinders need at least an axisymmetric DWBA; state it.
- S2, S6, X10, D2 and D5 specs: adequate as computation recipes. The yields in D2 and D5 remain exact gaps, as listed.

## 10. Literature claims rated (rubric c)
| Claim | Rating |
|---|---|
| 2308.06314 Eq. (48) linear in g_aee | CONFIRMED (residual ≈ 3× in Eq. (49) to note) |
| 2308.06314 electron vertex rigid-ion | UNRESOLVED / partly CONFIRMED (footnote 2 gives δZ = Z* − Q) |
| 2308.06314 Eq. (44) | CONFIRMED (subtraction forms differ; vertex identical) |
| 2601.01043 Eq. (12) linear in g_aγγB₀/m_a | CONFIRMED |
| 2601.01043 Eqs. (9)–(10): ε → 1, α vs Im(−1/ε) | CONFIRMED (n_r/\|ε\|²) |
| 2512.16451 Born invalid at 4×10⁻³⁸ cm², 20 eV | CONFIRMED |
| 2301.07617 angular-momentum selection rule in decay | CONFIRMED that the rule is not exact. "κ an estimate" is the source's own wording |
| 1705.03016 Eq. (6) Δp ~ αm_e underestimated | CONFIRMED (6.9 keV vs 3.7 keV; Δp/q_min = 0.05; conclusion holds) |
| Novelty: isotope channel | UNRESOLVED |
| Novelty/"introduced": C^{IR}, low-ω law | REFUTED (prior art; A + Bω²) |

## 11. Required corrections (summary)
1. §1/§0/C3/B2-L1: replace "GaAs rate ×0.47" by the LO-residue vertex Z − Z*/ε_∞ (ratio ≈ 0.1, highly sensitive). Credit 2308.06314 footnote 2.
2. §2.3 and gap 1: C^{IR} = A + Bω² (Taraskin et al.); the incoherent term survives at low ω.
3. §2.4/C4a: mass-weighted γ̄, giving 1.88×10⁻⁴. Novelty → "not found [E]". Note the (R3) violation at O(σ_M).
4. §6: Ni²⁺ bracket ≈ 0.83 (λ_S ≈ 1 for quenched orbit). §5: λ_S = g − 1 only for J multiplets.
5. §7(b): one-phonon production via j_T. Pairs only for the u × P readout operator.
6. (B2.7.2): add the S⁺ branch.
7. C15: ≈ 1.2×10⁻³ at 1 keV.
8. Notation: ω_L → ω_Lar; m_s renamed; λ mode label. Remove spin-ordered targets from the Theorem D GS chain. Add T to the τ strings.
9. Minor: "c_ν ≪ v" → "c_νv ≪ 1". Eq. (49) residual factor 3. Larmor theorem citation, valid at all T.
