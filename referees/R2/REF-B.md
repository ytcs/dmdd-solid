# R2 / REF-B: hostile referee report on R1/D1 (golden rule) and R1/D2 (Kubo)

Scope: read only D1.md, D2.md, their scripts, STATEMENT, NOTATION, CONTROLS and DONE. Both scripts were re-run
(`python3 -I`): every check prints 0 or the expected power. The scripts are correct, but they test only the
identities they encode. They do not test the limits contested below (C7 in particular). All other checks are by hand.

## Verdict table

| # | Claim | Verdict | One-line reason |
|---|---|---|---|
| 1 | D1 (1)–(4) agree term by term with D2 (2.1)–(2.2) | STANDS | Denominators agree on shell. The N, Ω, 2π and spin factors give 8π²α/(Ωq²)⟨⟨…⟩⟩ in both. The HL e² = 4πα is used consistently. |
| 2a | Pauli/exchange theorem: on shell, unrestricted m sum, signs | STANDS | Re-derived all four paths and both fermion signs (§2). |
| 2b | D1 §5.1: in the window every denominator has \|Δ\| ≥ E_min(q) − ω | STANDS WITH CORRECTION | False for B with m empty and for A with m occupied. The correct bound is min(E_min(q) − ω, E_g − ω_max). The no-i0 conclusion survives. |
| 2c | D2: the "same Pauli argument" also gives unrestricted sums in the 3-vertex ZPL vertex δρ^V | STANDS WITH CORRECTION | Not derived. The two-time-ordering algebra does not carry over, because a phonon exchanged with the Fermi sea is a two-body process. It does not affect the sideband. |
| 3a | f-sum exact for local H at all orders in g; the A² DW tadpole is first-moment neutral (D2) | STANDS | The double commutator contains only T_e (§3). |
| 3b | D2: each diagram's phonon cut plus its non-phonon cut is first-moment neutral ("cutting pair") | FALLS (as stated) | No proof is given. SE and V are not separately conserving (Ward identity), and only their sum is neutral. |
| 3c | D1: "sideband weight compensated by reduction of zero-phonon weight / e^{−2W}" | STANDS WITH CORRECTION | Only the **first moment** is compensated. No zeroth-moment rule exists, so "weight" is wrong. With "DW" read as the Franck–Condon/Lamb–Mössbauer factor, D1 and D2 say the same thing. |
| 4 | C7 limit: D1 iℓ_Q(û·q)ρ_cv versus D2 iu^{zp}·(q − m_eΔv)ρ_cv | BOTH FALL as the physical Q→0 limit | Intraband terms (m=c in A, m=v in B) are 0/0. Their limit is direction-dependent and involves the deformation potential and c_s/v (§4). D2's form is right only at Q ≡ 0 exactly. D1's "+O(ω_Q/δ)" is wrong. The amended C7 in CONTROLS must be replaced. |
| 5 | DFPT g inside, plus one external 1/ε(q,ω) with static-lattice ε₁, gives no double screening | STANDS WITH CORRECTION | There is no double counting. However, D2's premise "every Coulomb line carries q or Q" is false: lines at the pair momentum q+Q (exchange/local-field e-h kernel) exist at O(g²) and are omitted by both returns. This must be declared or estimated. H2 is redundant inside the window. |
| 6 | D1 §4: standard DFPT gives only path B (empty m) | STANDS | This is true of the Sternheimer output (P_c∂ψ_v). DFPT also gives ΔV_SCF, from which the rest follows non-self-consistently, as D1 says. |
| 7 | Resonance prescription; no sideband–ZPL interference at O(g²) | STANDS WITH CORRECTION | Orthogonality of the final states is enough, and D2's non-degeneracy hypothesis is not needed. D1's "P" must be the Hadamard finite part of 1/Δ². See 2b for the bound. |
| 8 | D2: C8 decoy may fail for GaAs under DM kinematics | FALLS (as stated) | The argument uses the unfolded \|q\|. For q near a reciprocal vector G, Umklapp reopens the ZPL at E_dir. Any surviving window is confined to m_χ ≲ 1 MeV (§8). |
| 9 | C1: reduction to the velocity-form phonon-assisted ε₂ | STANDS WITH CORRECTION | D2's commutator proof is exact for local potentials. D1's partial-fraction derivation mishandles the intraband (m=v, m=c) terms, and D1 drops its own i[g, q·r] term in step 3. With nonlocal PPs, D2's "holds only approximately" is wrong: it is exact with the generalised current plus an i[ΔV_NL, r] vertex. |
| 10 | D1 §7 Wannier F_ij(R,q) recipe with Umklapp | STANDS WITH CORRECTION | The F̃ algebra and Umklapp handling are right. However, the keV-q intermediate sum is dominated by bands far outside any Wannier manifold. That remainder is not Wannier-interpolable at fine grids, so the cost estimate is incomplete. g and F also need the same gauge U(k) (§10). |

Rung-4 rubric items not listed above: Bose factors, spin, √(1/2Mω), Umklapp in g, sign of q and DM kinematics
(η/q, F_DM, σ̄_e via |Ṽ|² = πσ̄F²/μ²) were all checked and are correct in both returns. Neither return touches
the ionization threshold or yield (deferred, Tier B).

---

## 1. Term-by-term agreement (both stand)
**Amplitudes.** On shell, ω = ε_{ck'} − ε_{vk} ± ω_Q. Then D2's first denominator becomes
ω − ε_{m,k+q} + ε_{vk} = ε_{ck'} − ε_{m,k+q} ± ω_Q, which is D1's. The second denominators are identical.
D2's M carries N^{-1/2}, while D1 puts the 1/√N in T_fi. The two are equal: M_D2 = M_D1/√N.

**Rate.** Write |T_fi|² = |Ṽ|²V^{-2}N^{-1}(n+½±½)|M_D1|². Then Γ = 2π·V∫d³q/(2π)³·2_spin·Σ_{kQ}|T|²δ
= ∫d³q/(2π)³|Ṽ|²·(4π/(VN))·N²⟨⟨·⟩⟩, which gives S^PA = (4π/Ω)⟨⟨·⟩⟩, D1 (2) ✓.
Then ε₂ = (e²/2q²)S = (4πα/2q²)(4π/Ω)⟨⟨·⟩⟩ = 8π²α/(Ωq²)⟨⟨·⟩⟩, D1 (4) ✓.
For D2 (2.2): (2πe²/q²V)Σ_{kQ}|M_D1|²/N = 2π·4πα·N²/(q²NΩN)⟨⟨·⟩⟩, the same ✓. The spin 2 sits inside "2π" in D2
(e²/2q² × 2π/V × 2). The docstring of D2's script writes πe²/(q²V), which is per spin. This is cosmetic.

**Remaining checks.** D2's Lehmann sign is verified: with A = n_q†(t) and B = n_q, the first pole carries |⟨f|n_q|i⟩|²δ(ω − E_f + E_i), so
S = −2Imχ/(1 − e^{−βω}) ✓. D2's hermiticity g*_mn(k,Q) = g_nm(k+Q,−Q) needs e_κν(−Q) = e*_κν(Q). This should be stated.
The phonon label (emit −Q or absorb +Q, both with g(·,Q)) is consistent ✓.
D1's η/q angular average and the 1/(2π) prefactor in the isotropic dR/dω are verified ✓.

## 2. Pauli/exchange theorem
**Signs.** For path C, c†_m c_v c†_c c_m = −c†_c c†_m c_m c_v. Acting on Φ₀ with m and v occupied, this gives −c†_c c_v Φ₀.
For path A (m empty), c†_c c_m c†_m c_v Φ₀ = +c†_c c_v Φ₀. D2's commutator [c†_{v'}c_v, c†_c c_{v'}] = −c†_c c_v is
the same fact. ✓

**Denominators.** E_i − E_I is ω − ε_m + ε_v for A, ε_v − ε_m ∓ ω_Q for B, ω − ε_c + ε_m for C, and ε_m − ε_c ∓ ω_Q for D ✓.
On shell, −1·ρg/(ε_m − ε_c ∓ ω_Q) = gρ/(ε_c − ε_m ± ω_Q) = gρ/(ω + ε_v − ε_m), so D → A-form ✓.
Likewise −ρg/(ω − ε_c + ε_m) = ρg/(ε_v − ε_m ∓ ω_Q), so C → B-form ✓. The same holds with s = ±1 (absorption).
D1's linked-cluster treatment of q = G is also right. ⟨f|ρ_G|f⟩ − ⟨Φ₀|ρ_G|Φ₀⟩ = ρ_cc − ρ_vv supplies the m=c (B) and m=v (A)
terms with the correct signs.

**Off shell.** The four-path form differs from (1) off shell. This affects only ε₁^{PA} and the O(g²) ZPL vertex. Both enter L in the window at
O(g⁴) (§5), so nothing claimed for the sideband is affected.
D2 §2c item 4 nevertheless asserts unrestricted sums for the three-vertex virtual-phonon vertex "by the same argument".
That argument is a two-ordering identity. At third order with a virtual phonon, the phonon can be absorbed by a
*different* sea electron, which is a phonon-mediated two-body interaction (Fock-like, partly inside Σ^FM through its f factors).
The claim must be derived or downgraded to [C].

**2b, the bound in D1 §5.1 is wrong as stated.** Use the on-shell identity Δ_B = ε_{ck'} − ε_{m,k+Q} − ω for every m.
- For m occupied this is a first-order transition at momentum q, so |Δ_B| ≥ E_min(q) − ω ✓.
- For m empty, the direct form gives |Δ_B| = ε_{m,k+Q} − ε_{vk} ± ω_Q ≥ E_g − ω_Q. This is *not* ≥ E_min(q) − ω when E_min(q) > 2ω − E_g.
  That happens in Si for q folding near 0 or G, where E_min ≈ 3.4 eV and ω ≈ 1.2 eV.
- The same applies to A with m occupied: |Δ_A| = ε_{ck'} − ε_{m,k+q} ± ω_Q ≥ E_g − ω_Q.

Corrected statement: |Δ| ≥ min(E_min(q) − ω, E_g − ω_max) > 0. The δ in the adiabatic error estimate (§4 of D1) must use
this minimum. The numbers barely change, since E_g − ω_max ≈ 1 eV.

## 3. f-sum rule and "Debye–Waller"
**3a (D2 correct).** Take H = T_e + V_e(r; {R}) + T_ion + …, with V local in r_e. Then [[H, n_q], n_q†] = [[T_e, n_q], n_q†] = N_e q²/m_e, for any
phonon state and at every order of the u-expansion, truncated or not, as long as every term is local in r_e. Any static local one-body
potential, including the phonon-averaged A² tadpole ½⟨uu⟩:∂²V, therefore leaves M₁ unchanged. Its 2-phonon (b†b†) matrix elements
enter |·|² only at O(g⁴). Hence ΔM₁^{DW-tadpole} = 0 exactly, and M₁^{SB} must be cancelled by the non-phonon cuts of the
linear-coupling diagrams (SE-p + SE-h + V). This is D2's statement. It fails for nonlocal pseudopotentials, as D2 notes and D1 does not.

**3b (D2 overreaches).** The "cutting pair" claim, that *each* diagram's phonon cut and non-phonon cut add to zero first moment, is asserted, not
derived. Number conservation is enforced by the Ward identity, which ties the self-energy insertions to the vertex correction.
Individual diagrams are not conserving. For example, a static local U inserted on the particle line alone shifts M₁ by
Σ_n f_n⟨n|n_q†Un_q|n⟩ − (Pauli terms) ≠ 0 in general, and only SE-p + SE-h together give ⟨[n_q†,[U,n_q]]⟩ = 0.
Only the sum SE-p + SE-h + V is neutral. The claim is also unnecessary. Delete it or prove it.

**3c (D1 imprecise; D1 and D2 do not actually disagree).** D1 says the "sideband weight is compensated by the reduction of the zero-phonon weight".
The exact constraint concerns the **first moment** only. The zeroth moment ∫S dω = S(q) (static structure factor) has no O(g²)
conservation law. D1's §6.2 "e^{−2W}" is the one-phonon/two-phonon expansion of e^{iq·u}. In a perturbative electron basis its
first-moment part comes from linear-coupling non-phonon cuts: Fan Z, mixing and the vertex.
D2's split (A² tadpole neutral; Franck–Condon e^{−S} from the g_cc − g_vv parts of Z and V) is therefore the precise form of D1's statement, provided
"DW" means the Franck–Condon/Lamb–Mössbauer factor and not the Allen–Heine tadpole. The paper must fix one meaning, and must say "first moment" throughout.
D2's ELF-bound discussion is honest ([C/E], unread papers) and is not refereed here.

## 4. C7: the acoustic Q→0 limit (neither form is correct)
Take a rigid shift with ΔV = [A, H₀], A = −iℓ ê·p, ℓ = (2M_cell ω_Q)^{-1/2} (with N^{-1/2} in D2's normalisation). This gives G_ab = (E_b − E_a)A_ab, and G_nn = 0.
Split the unrestricted sum (1) at Q→0 into interband and intraband terms.

*Interband (m≠c in A, m≠v in B).* The denominators tend to E_c − E_m and E_v − E_m, which are nonzero, so G/Δ → −A_cm and +A_mv:
Σ_{m≠c}(−A_cm ρ_mv) + Σ_{m≠v} ρ_cm A_mv = [ρ, A]_cv + A_cc ρ_cv − ρ_cv A_vv.
Using [e^{iq·r}, p] = −q e^{iq·r}, this is iℓ ê·(q − m_e(v_c − v_v)) ρ_cv. This is exactly D2's expression, and D2's sympy check (2).

*Intraband (m=c in A, m=v in B).* The terms are
  g_cc(k+q,Q) ρ_cv / (ε_{c,k+q+Q} − ε_{c,k+q} ± ω_Q)  −  g_vv(k,Q) ρ_cv / (ε_{v,k+Q} − ε_{vk} ± ω_Q).
Both numerator and denominator are O(Q). For a physical acoustic branch, g_nn(k,Q) = ℓ·Q·[i Q̂·Ξ^n(k)·ê] + O(Q²), where Ξ^n
is the full long-wave intraband coupling tensor (deformation potential, with any rigid-frame m_e v v piece included), and the denominators are
Q(Q̂·v_n ± c_s). Hence
$$M^{(2)}_{ac}\xrightarrow{Q\to0}\Big\{i\ell\,\hat e\cdot[q-m_e(v_c-v_v)]+\frac{i\ell\,\hat Q\cdot\Xi^c\cdot\hat e}{\hat Q\cdot v_c\pm c_s}-\frac{i\ell\,\hat Q\cdot\Xi^v\cdot\hat e}{\hat Q\cdot v_v\pm c_s}\Big\}\rho_{cv}(k,q)+O(Q^{1/2}).$$
This is a soft-boson (Low-type) factorisation, and it is non-analytic in the direction Q̂.

Consequences:
- **D2's form** is obtained only if the intraband ratios are dropped. That is legitimate at Q ≡ 0 with ω_Q → 0 taken afterwards: the denominator is then ±ω_Q and the numerator is exactly 0.
  It is not the limit along a physical dispersion. D2's statement "g_nn = 0" confuses g_nn(Q=0) with lim g_nn/Δ.
- **D1's form** follows only if Ξ contains nothing but the rigid-frame part, g_nn = −(ε_{n,k+Q} − ε_{nk})A_nn, *and* c_s ≪ |Q̂·v_n|.
  The ratio is then −A_cc, which restores [ρ, A]. D1's "+ω_Q(…)= O(ω_Q/δ)" is wrong for the m=c and m=v terms, whose denominators are Q·v ± ω_Q, not δ.
  S3c is consistent: for m = f both sides are 0, so the "correction" is O(1). D1's own test N-d (Q = 0, ω_Q → 0) would return D2's form, not D1's.
- **Magnitude.** At band extrema (v_n = 0) the first term reduces to iℓ ê·q and the soft terms become ±iℓ(Ξ^c − Ξ^v)/c_s.
  With Ξ ~ 5–10 eV and c_s ~ 3×10⁻⁵, Ξ/c_s ~ 10⁵ eV, compared with q ~ 1–4 keV. The soft term dominates by about 10².
- **What survives.** Integrability survives, because |M|² ∝ ℓ² ∝ Q^{-1} at T=0 and (n+1)|M|² ∝ Q^{-2} at T>0 against Q²dQ, as both claim.
  It also survives that the Q→0 region lies outside the window: the soft denominators vanish only on the Cherenkov cone, where the ZPL is on shell.
- **What must change.** The amended C7 in CONTROLS ("an implementation must reproduce iu·(q − m_eΔv)ρ") would flag a *correct* code as buggy.
  Replace it with the displayed formula. As a test, use the synthetic rigid-shift g with Ξ ≡ 0 at Q = 0 exactly (which gives D2's form), and separately check the soft factor.

## 5. Screening
- **No double counting.** This holds, by D2's argument: chains at (q, ω) are reducible and give 1/ε. Chains at (Q, ≈ω_Q) dress g, and static DFPT is adequate at O(ω_Q/E_g).
- **Missing class of Coulomb lines.** D2's premise "every Coulomb line carries q or Q" is false. Split the PA box into two triangles (ρ_q, g_Q, v_{q+Q+G}) joined by an RPA chain
  at (q+Q, ω ∓ ω_Q), the momentum of the final e-h pair. This is Coulomb-proper with respect to q, because the phonon line still connects the two halves, and it is O(g²).
  It is the exchange (local-field) part of the e-h kernel at the pair momentum, the same class as RPA local fields in optics (~10–20% in Si ε₂ [E]).
  It is neither in D1's KS-pair golden rule nor in D2's diagram list. It is not a double count; it is an omission. It must be estimated, or declared beside the excitonic (direct-kernel) approximation that D1 marks [C].
- **Conditions.** In the window ε₂^{(1)} = 0, so L = ε₂^{PA}/(ε₁² + ε₂^{PA2}) = ε₂^{PA}/ε₁⁰² + O(g⁴) identically. H2 (ε₂ ≪ ε₁) is automatically satisfied there and is needed only outside the window.
  H1 (ω ≫ ω_LO) is needed only to drop the phonon-reducible (X) part of ε₁, which at DM q in Si is O((m_e/M)ω_p²/ω²). H3 is used correctly.
- **Minor.** D2's GaAs ε^{ion} "10⁻³–10⁻²" is an overestimate. (ε₀ − ε_∞)(ω_TO/ω)² ≈ 2·(0.033/1.5)² ≈ 10⁻³ absolute, which is ~10⁻⁴ relative to ε_∞ ≈ 11.

## 6. Adiabatic claim (D1 §4): stands
DFPT's Sternheimer equation returns P_c|∂ψ_v⟩, i.e. components on all empty m at k+Q. That is path B with m empty. In the parallel-transport gauge, P_v∂ψ_v is set to zero.
Paths A and D (|∂ψ_c⟩) and C (P_v∂ψ_v) are missing, as D1 says. All of them follow from the DFPT ΔV_SCF without another self-consistent cycle:
P_v∂ψ_v is a finite valence sum, and ∂ψ_c needs one non-SCF Sternheimer solve at energy ε_{ck'}.
The derivative (5), using ⟨∂ψ_c| from the −Q half of the real pattern by hermiticity, is correct. The error estimate is ω_Q/δ with δ from §2b.

## 7. Resonances and interference
The sideband–ZPL cross term vanishes because the final states are orthogonal (different phonon occupations). This holds at every T. D2's parity argument is equivalent.
D2's extra hypothesis "non-degenerate between sectors" is not needed for orthogonality; it is needed only for perturbation theory to be valid at resonance.
D1 writes |Δ+iγ/2|^{-2} → (2π/γ)δ(Δ) + P. The remainder is the Hadamard finite part 𝔣𝔭(1/Δ²), not a principal value. 1/Δ² has no PV, so this is a correction to the prescription's wording.
D2's iff condition ("every reachable first-order transition off shell") is equivalent to D1's ω ≤ E_min(q) − δ₀.
One D2 remark is wrong. The hole-relaxation resonance of A₂ (m valence) is generic for any hole below the VBM, not "only near band crossings". On shell, however, it is identical to an open m→c first-order transition (Δ_B = ε_{ck'} − ε_m − ω), so it is excluded inside the window.

## 8. D2's C8 flag: unsound as stated
D2 works at fixed |q| ≥ q_min = ω/v_max. Check: 1.5 eV / 2.65×10⁻³ = 566 eV = 0.29 Å⁻¹ ✓. D2's parabolic Γ threshold E_dir + q²/2(m_c+m_h) ≈ E_dir + 0.55 eV is also correct.
But **q is not reduced to the 1BZ**. For |q| near |G₁₁₁| = 2π√3/a = 1.93 Å⁻¹, the folded q' = q − G is small, and the ZPL Γ→Γ transition reopens at E_dir + q'²/2M,
through the Umklapp form factor ρ_cv(k, q'+G), which is generically O(10⁻¹–1).
At fixed ω, the DM rate integrates over every accessible |q| up to q_max ≈ m_χ v(1 + √(1 − 2ω/m_χv²)). The ZPL stays closed only if q_max < |G| − √(2M(ω − E_dir)) ≈ 1.93 − 0.2 Å⁻¹.
At ω = 1.5 eV this means m_χ ≲ 0.7–1 MeV. For heavier DM the shell near G opens the ZPL at E_dir, with O(1) amplitude against the O(g) PAER, and C8 holds as written.
D1 §5.1 already noted that the window must exclude q folding near k_c − k_v. D2 did not apply this. The flag reduces to "possible only for m_χ ≲ 1 MeV, and only if the f_χ weight survives near q_max". That needs the N2 band check, which must use folded q.

## 9. Optical limit C1
- **D2 is correct.** [H, n_q] = [T, n_q] = q·j_q for local V and local ΔV. Taking matrix elements between exact eigenstates on shell gives ω⟨f|n_q|i⟩ = q·⟨f|j_q|i⟩, and expanding both sides to O(g) gives
  M^{(2)} = (q/ω)·M_j with the same denominators. As q → 0, j → p/m_e, including the intraband v_nn ✓.
  The prefactor 8π²e_G²/(Ωω²)(1/N_kN_Q) with spin is ✓. Using the transverse ê in place of q̂ needs D1's cubic ε^L = ε^T(q→0) remark, which D2 omits.
- **D1's derivation has a gap.** It writes ρ_mn(k,q) = δ_mn + iq·r_mn and uses S3a/S3b, which are singular for m = v (A) and m = c (B), and r_vv is a gauge-dependent Berry connection.
  The intraband velocity terms in S₁ and S₂ actually come from expanding ε_{v,k+q} (giving q·v_v/ω²) and from the covariant k+q dependence of g and u, not from r_vv.
  The final S₁ and S₂, with unrestricted m, are right (they agree with D2), but the step as written does not derive them.
  D1 then states that i[g, q·r]_cv "must be kept for consistency" and drops it from the step-3 formula. Restore it.
- **Gauge and nonlocality.** In D1's length-to-velocity route, the r_mn → v_mn/(i(E_m − E_n)) step automatically uses the full v = i[H, r], including i[V_NL, r]. With nonlocal ∂V, the extra vertex i[ΔV_NL, q·r] appears.
  D2's "the equivalence holds only approximately" is wrong: it is exact with the generalised current q·j_q + [V_NL + ΔV_NL, n_q]. What is approximate is using p/m_e alone.
  Whether the literature formula omits [V_NL, r] is [E] in both returns and is not checked here.

## 10. Recipe (D1 §7)
- **Correct.** ρ_mn(k,q) = [U†(k+q) F̃(k+q,q) U(k)]_mn with F̃(κ,q) = Σ_R e^{−iκ·R}F(R,q). Re-derived: ⟨w_{iR'}|e^{iq·r}|w_{jR}⟩ = e^{iq·R}F_ij(R'−R, q).
  Because e^{−i(k+q)·R} = e^{−i[k+q]·R}, the "unfolded k+q" is immaterial. All Umklapp information sits in the unreduced q argument of F ✓.
  The ASR enforcement and the PAW/all-electron reconstruction above 3–4 keV are both appropriate. The PAW density vertex adds Σ⟨ψ̃|p̃_i⟩(⟨φ_i|e^{iq·r}|φ_j⟩ − ⟨φ̃_i|e^{iq·r}|φ̃_j⟩)⟨p̃_j|ψ̃⟩. e^{iq·r} is local, so no NL-PP commutator enters ρ itself; that issue arises only in C1 and in the [ΔV_NL, n_q] vertex.
- **Missing 1, the remainder.** At q ~ keV, e^{iq·r}|v⟩ has most of its weight on bands ~q²/2m_e ≈ 2–16 eV and higher, which lie outside any N_W = 8–16 manifold. Path A is then dominated by the out-of-manifold remainder.
  D1's Sternheimer remainder is correct in principle: an adiabatic solve at ε_{ck'} with error ω_Q/Δ_m. But it is a plane-wave object per (k', Q), not Wannier-interpolable, so the fine pocket grids (60³–120³) cannot use it directly.
  The recipe must specify one of two routes: (a) the remainder computed on the coarse grid and interpolated as a smooth tensor, or (b) a large disentangled manifold reaching above q²/2m_e with a convergence test in N_W. The cost formula must include either.
- **Missing 2, gauge consistency.** g_cm(k+q,Q) and ρ_mv(k,q) share the band index m at k+q. g^W and F must come from the same Wannierisation and the same U(k), or the m-sum acquires random relative phases.
- **Minor.** C5: D2's "E_g − max ω_Qν" overstates the absorption threshold. It is E_g − max_ν ω_{Q*ν} at the connecting Q*(q), as D1 has it.

## Required corrections (summary)
1. Replace C7 (and both returns' versions) with the soft-factor formula of §4, and fix D1's O(ω_Q/δ) claim.
2. Make the f-sum and compensation statements first-moment only. Fix "DW" to mean the Franck–Condon factor. Delete or prove D2's cutting-pair claim.
3. Declare or estimate the pair-momentum (q+Q) exchange/local-field kernel. Do not cite D2's "two classes" proof as complete.
4. Restrict D2's C8 flag to m_χ ≲ 1 MeV, with folded q.
5. Correct D1's §5.1 bound to min(E_min − ω, E_g − ω_max), and use the Hadamard finite part in §5.2.
6. In D1's C1, restore i[g, q·r] and re-derive the intraband terms. In D2, call the NL case "exact with the generalised current".
7. In the recipe, give an interpolable treatment and cost for the out-of-manifold remainder, and require one gauge for g and F.
