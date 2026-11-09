# R7 / REF-WP2-A: hostile referee of returns/R6/WP2-v2.md

Referee A, isolated. Read: WP2-v2.md, code/WP2-v2/checks.py, CONVENTIONS, NOTATION v4, CONTROLS, DONE, LIMITS, WP0-v2.
I did not read referees/, state/, AUDIT.md, other returns or other briefs. checks.py re-run: 21/21 PASS (≈ 40 s). Full texts fetched
into literature/papers-r7-WP2-A/ and deleted after use: 2607.24933, 1712.06598, 2309.10839, 2205.02250, 2009.13534, 2411.03433.
Not fetched (claims not ruled on): 1910.08092, 1807.10291, 1911.03482, 2506.11191, 2011.09477, hep-ph/0608035, 2607.06005.

## Verdict table

| # | Claim (WP2-v2 location) | Verdict | One-line reason |
|---|---|---|---|
| 1 | GS reduction (1.1)–(1.2), charge vertex 𝒵_κ | STANDS | Follows from WP0-v2 Thm D (ii); limits (rigid ion, Born) correct |
| 2 | Exact coherent harmonic S (2.1)–(2.2), phases e^{iq·r_κ} | STANDS | Bloch identity, CONVENTIONS §5 normalisation and sign of q check; C13 correct |
| 3 | Shell expansion (2.3) and convergence statements | STANDS WITH CORRECTION | T > 0, n_ph = 2: Σ_ΔR Φ² diverges absolutely (Φ² ~ ΔR⁻²); finite only through the e^{−iq·ΔR} phase (distributional) |
| 4 | **BZ-average theorem (2.4)** | **STANDS WITH CORRECTION** | Exact for a Bravais lattice only. For a basis, *every* inter-sublattice shell survives with weight j_BZ(ΔR + r_κ − r_κ′), not only ΔR = 0. C9 (monatomic, q-independent weights) cannot test this |
| 5 | **2607.24933 Eq. (47) incomplete (§3.3)** | **STANDS WITH CORRECTION** | CONFIRMED for the polarisation weight: 1/3 replaces ∣q̂·e∣² even under the paper's stated "monoatomic, isotropic" assumption. The intra-cell-phase part is outside the paper's stated scope and is not an error of Eq. (47) |
| 6 | Incoherent S (3.1)–(3.2), FC terminology | STANDS | Absorption sign, ∫w = 2W, 2π/Ω prefactor verified |
| 7 | **Truncation loss (3.4′) at any T, coherent too** | STANDS | Order-n fraction and the Poisson tail re-derived; Φ̇_{κκ′}(ΔR,0) = −i(q²/2M)δδ re-derived. Polyatomic: the loss is a species-weighted mixture of P[Pois(2W_κ) ≥ N] |
| 8 | Panjer equation (3.5) and ρ^ph (3.6) | STANDS | Follows from ∂_t e^Φ = Φ̇e^Φ; C4 correct |
| 9 | **L4: Sherman–Morrison (4.2) ≡ total-ε ELF** | STANDS | Re-derived algebraically; the Im-part gives exactly (2π/Ω)Σ_ν(1/2ω)∣q·Z*·e*/(ε_∞√M)∣²δ |
| 10 | **1712.06598 Eq. (5) spurious 1/V_cell** | STANDS | CONFIRMED from the full text: with Eqs. (6)–(7), ∣ℳ∣² has dimension E², not E⁻¹ |
| 11 | 1712.06598 Eq. (12) equal-mass eigenvectors | STANDS WITH CORRECTION | CONFIRMED, but it is the paper's declared rough "≈" estimate; numerically negligible ((√A_Ga − √A_As)² ≈ 0.09 against 289) |
| 12 | One-branch (4.3), Si/Ge Z* = 0 (4.5), nucleon vertex (4.4) | STANDS | LST and residue re-derived; symmetry argument correct |
| 13 | Exact cumulants (5.1); mean exact | STANDS | Placzek/Sears moments; C5 certificate is a genuine exact check |
| 14 | 2205.02250 "true peak shifted" listed as a discrepancy (5.1, L6) | STANDS WITH CORRECTION | REFUTED as an error: the source says "peak" (the mode), which is correct. It is a clarification, not a discrepancy |
| 15 | GS/X split of 𝔨₃ (5.2) | STANDS (at stated order) | Second-derivative (Hellmann–Feynman) identity and Migdal ω¹, ω³ moments re-derived; C6 correct |
| 16 | **(5.2′) closed form 𝔨₃ = (q²/2M²)Z e²𝓃_e(R_κ)/3** | STANDS | Exact at any q for point nuclei on cubic sites (self term, no phase) |
| 17 | **(5.2′) 𝓜³_κκ∣_{V_eN} = −(m_e/M_κ)𝓜³_eκ, "one contact sum rule"** | **STANDS WITH CORRECTION** | True only for q·a_core ≪ 1 (a_core ≈ a₀/Z_κ, ≈ 50 keV⁻¹ scale for Si). 𝓜³_eκ carries e^{iq·(R−r)}, which gives the traceless ℓ = 2 part a finite-q average; 𝓜³_κκ does not. WP0-v2 (4.7) states q → 0; WP2-v2 omits it, and the restriction bites in the 10–300 keV window |
| 18 | Free recoil chain (5.3) → hep-ph/0608035 Eq. (5) | STANDS | C8 correct under hypothesis (I); σ_ω² = 4E_RE^kin correct |
| 19 | Exact constraints (6.1) and nuisance compatibility (6.1′) | STANDS WITH CORRECTION | The third identity omits the normalisation (2π/Ω)∣c_κ∣² (or else Δ must be the normalised S_self). (6.1′) is correct (concavity) |
| 20 | Toy-model audit (6.3), 𝔨₃ 7% low | STANDS | Compound-Poisson cumulants re-derived: x(ω₀³ + 3ω₀σ²) = (q²/2M)(3ω₀ω̄ − 2ω₀²) |
| 21 | **2309.10839 Eq. (9) e^{−W} vs e^{−2W}** | STANDS | CONFIRMED: Eq. (9) e^{−W_d}, Eq. (10) W_d = (q²/4m_d)∫D/ω, Eq. (13) e^{−2W_d} with W^toy = q²/4m_dω₀ |
| 22 | Spin channel (7.1); 2009.13534 omits it | STANDS | CONFIRMED: 2009.13534 drops unordered vector responses (text after its Eq. (31)). Its 1/N argument holds per final state, not after summing over phonon momenta |
| 23 | Currents (7.2) | STANDS | Matrix element (ω/2NM)^{1/2}e* and S_{j_Tj_T} weight ω/2 check |
| 24 | Rate expansion (8.1), selection rules | STANDS | Funk–Hecke with λ_ℓ = 2π∫P_ℓ; A₁ multiplicities correct (even ℓ: T_d ≅ O) |
| 25 | **Cubic isotropy theorem (8.2)** | STANDS | The self term depends on q̂ only through rank-2 site tensors (D^{αβ}_κ(ω), B_κ), which are ∝ 𝟙 on T_d sites. Exact. 2411.03433 excludes n = 1, so "explains" is fair (CONFIRMED) |
| 26 | 2411.03433 isotropic IA width "omission" | STANDS WITH CORRECTION | CONFIRMED that q̂ = ẑ is used, but the paper declares and sizes it (6–8% in ω̄). This is a declared approximation, not an omission |
| 27 | LIMITS L4, L5, L6, L18, L19 entries | STANDS WITH CORRECTION | Quotes I checked are correct (1712.06598, 2309.10839, 2205.02250 Eq. (39) form, 2607.24933). L5 chain cites (2.4), which needs the item 4 correction. L6's "discrepancy" should be reworded (item 14) |
| 28 | Gap closures G3, G11, G13, L4 add-on (§10) | STANDS | Each is a formula plus a code-level specification (inputs, grids, cost, outputs), not a restatement. G13's 𝒞₃, 𝒞₄ contraction is a sketch |
| 29 | Consistency with CONVENTIONS, NOTATION v4, WP0-v2 | STANDS WITH CORRECTION | Only defect is item 17 (missing q → 0 qualifier relative to WP0-v2 (4.7)). The agreement with WP3 J8 cannot be checked under isolation; I rely only on WP0-v2's statement that J8 holds at q → 0 |
| 30 | Contested corrections (§14: none) | STANDS | Nothing contested; the IF-3 clarification is correct (item 7) |

## Arguments

**A1. BZ-average theorem (item 4).** In (2.3) the explicit q-dependence of a shell term is e^{−iq·d}, with d ≡ ΔR + r_κ − r_κ′.
Holding Φ_{κκ′} and W_κ at q (the stated gradient approximation), the average over p ∈ BZ gives
e^{−iq·d}·(Ω/(2π)³)∫_BZ d³p e^{−ip·d} = e^{−iq·d} j_BZ(d). For κ = κ′, d = ΔR is a lattice vector, so j_BZ = δ_{ΔR,0}, as claimed.
For κ ≠ κ′, d is **never** a lattice vector, and j_BZ(d) ≠ 0 for every ΔR in general. Explicit case (sympy): a 1D diatomic chain with
r₂ − r₁ = a/2 gives j_BZ(d) = 2/π for both ΔR = 0 and ΔR = −a (the two nearest neighbours), then −2/(3π) for the next shell, and so on.
In diamond Si, the four nearest neighbours of a site are all on the other sublattice. They are related by T_d operations that leave the
fcc BZ invariant, so all four carry the same j_BZ (spherical-BZ estimate ≈ 0.44). (2.4) keeps one of the four.
**Correction:**
(Ω/(2π)³)∫_BZ S^{(n)}(q+p,ω) = S_inc^{(n)} + Σ_{κ≠κ′}Σ_{ΔR} j_BZ(ΔR + r_κ − r_κ′) S^{(n)}_{κκ′,ΔR}(q,ω) + gradient terms.
The headline "incoherent = BZ-averaged coherent" is exact only for Bravais lattices. For Si, Ge and GaAs the inter-sublattice shells are of
the same size as the §3.3 shell estimate, so they are not negligible a priori. The proof sentence "∫_BZ e^{ip·ΔR} = 0 removes every shell term
except the intra-cell cross terms" is false as written. WP2v2-C9 uses a monatomic chain and q-independent weights, so it tests only lattice
orthogonality, and "verifies the identity exactly" overstates it. The gradient terms are O(q_BZ/q) only for q ≫ q_BZ, and O(1) at q ≲ q_BZ.

**A2. 2607.24933 Eq. (47) (item 5).** HTML Eqs. (44)–(47) are PDF Eqs. (4.20)–(4.23). I confirmed this from the alttext sequence.
Eq. (47) is S_full^{(n)} = (2πf²e^{−2W}/Ω_c n!)(q²/2m)^n ∏_i∫d³k_i dω_i D(ω_i,k_i)/ω_i δ(ω − Σω_j)(2π)³/Ω_c Σ_G δ³(q − Σk_i − G),
with D(ω,k) = (Ω_c/(3(2π)³))Σ_α δ(ω − ω_{αk}) (Eq. (46)). Expanding (2.2) for one species gives the per-phonon factor
(Ω/(2π)³)Σ_α ∣q̂·e_α(k_i)∣²δ(ω_i − ω_{αk_i}). Eq. (47) has (1/3)Σ_α instead. At n = 1, G = 0, q ≪ q_BZ, momentum conservation sets
k = q, so ∣q̂·e_L∣² = 1 and ∣q̂·e_T∣² = 0. That holds also for an elastically isotropic medium, so the paper's caveat ("we have still
assumed a monoatomic, isotropic lattice for simplicity", directly below Eq. (4.23)) does not rescue the formula. **CONFIRMED** for the
polarisation weight. The package should quote that caveat. It should also drop "and, for a polyatomic basis, the intra-cell phases" as a
defect of Eq. (47), because the formula is explicitly monoatomic. That part extends the result; it does not correct it.

**A3. Truncation loss (item 7).** With ∫w = 2W (absorption lines included, weight n_B∣D∣/∣ω′∣ ≥ 0) and ∫ω′w = (q²/2M)∫D[(n+1) − n] = q²/2M,
we have ∫ω w^{*n} = n(∫ωw)(∫w)^{n−1}. So ∫ωS^{(n)}/∫ωS = e^{−2W}(2W)^{n−1}/(n−1)!, the sum over n ≥ 1 is 1, and the omitted
Σ_{n>N} equals Σ_{k≥N}e^{−x}x^k/k! = P[Pois(2W) ≥ N]. This holds at any T, with 2W ∝ ∫D coth(βω/2)/ω. For the coherent part, substitute
Q → −Q in the absorption term using e(−Q) = e(Q)*. This gives Φ̇_{κκ′}(ΔR,0) = −i(2N√(M_κM_κ′))⁻¹ Σ_Q e^{iQ·ΔR} q·(Σ_ν e_κν e_κ′ν†)·q
= −i(q²/2M_κ)δ_{κκ′}δ_{ΔR,0}. Then d_t(Φⁿ)∣₀ = nΦ^{n−1}Φ̇(0) = 0 for every shell term. Correct. With several species the lost fraction
is Σ_κ w_κP[Pois(2W_κ) ≥ N]/Σ_κ w_κ, where w_κ = 𝓃_κ∣c_κ∣²/M_κ. This should be written out, because 2W_κ differs between species in GaAs.

**A4. Sherman–Morrison (item 9).** Write s = pᵀ(D_A − z)⁻¹p and c = e²/Ω. Then ε = ε_∞ + cs. With D_NA = D_A + (c/ε_∞)ppᵀ,
pᵀ(D_NA − z)⁻¹p = s − (c/ε_∞)s²/(1 + cs/ε_∞) = ε_∞s/ε. Then −1/ε_∞ + (c/ε_∞²)(ε_∞s/ε) = (cs − ε)/(ε_∞ε) = −1/ε. ✓
D_NA is the Gonze–Lee non-analytic term in Heaviside–Lorentz units (4π → e²/… with e² = 4πα). For z = (ω + i0)², the imaginary part is
Σ_ν(p·e_ν)²πδ(ω − ω_ν)/(2ω_ν). Then S_zz = (2q²/e²)(c/ε_∞²)(…) = (2π/Ω)Σ_ν(1/2ω_ν)∣q·Z*·e_ν/(ε_∞√M)∣²δ. ✓ (CONVENTIONS §6 S ↔ L).
Hypotheses: macroscopic (rank-1) ε only, q ≪ q_BZ, ω ≪ E_g. These are the ones stated.

**A5. 1712.06598 Eqs. (5)–(7) (item 10).** Quoted correctly: C_F = e[(ω_LO/2V_cell)(1/ε_∞ − 1/ε₀)]^{1/2}, Eq. (6)
Γ = 2π∫d³p_f/(2π)³ δ(E_f − E_i − ω)∣ℳ_q∣², Eq. (7) ∣ℳ_q∣² = κ²g_X²C_F²/(e²q²). With e dimensionless, C_F²/q² ~ E·E³/E² = E².
Eq. (6) needs ∣ℳ∣² ~ E⁻¹ for Γ ~ E. Fröhlich's normalisation has 1/V with V the box volume, which cancels against Σ_{p_f} → V∫d³p/(2π)³.
Eq. (6) is already the cancelled form, so V_cell is spurious there. **CONFIRMED** at formula level. I did not check whether it reached
their curves, and the package does not claim that it did.

**A6. 2309.10839 (item 21).** Full text: Eq. (9) S ≈ 2πΣ_d n_d∣f_d∣²e^{−W_d(q)}Σ_n…, Eq. (10) W_d = (q²/4m_d)∫dω′D_d(ω′)/ω′ with
∫D_d = 1, Eq. (13) e^{−2W_d} with W_d^toy = q²/4m_dω₀. For D = δ(ω − ω₀), Eq. (10) equals W^toy, so (9) and (13) are mutually inconsistent.
The physical value is ∣⟨0∣e^{iqx}∣0⟩∣² = e^{−q²/2mω₀} = e^{−2W}. **CONFIRMED.** The package's "typo at formula level; numerics not checked"
is the right scope.

**A7. 𝔨₃ identities (items 16, 17).** (i) (5.1) gives 𝔨₃ = (q²/2M²)⟨∂_q̂²V_pot⟩ for the self term, with no phase, at any q.
∇²_{R_I}V_NN = 0 off coincidence. ∇²_R(−Z e²/4π∣r − R∣) = +Z e²δ³(r − R). On a T_d site ⟨∂_α∂_βV⟩ = δ_{αβ}tr/3; the traceless 1/r³ part
has a convergent angular average because the ℓ = 2 density component is ∝ r² at the nucleus. So 𝔨₃ = (q²/2M²)Z e²𝓃_e(R_κ)/3 at all q. ✓
Si size: Z e²𝓃_e/3 = 4π·14·(2·14³/π)/3 ≈ 1.0×10⁵ a.u. against Mω² ≈ 0.13 a.u. That gives a ratio of ≈ 7.7×10⁵ (C10). "≈ 8×10⁵" is fine.
(ii) The κκ potential term ⟨(q·∇)²(−U_κ)⟩/M² has no phase. The eκ term (WP0-v2 (4.7)) carries e^{iq·(R_I−r_i)}. Expand
e^{−iq·ρ} = Σ_ℓ(2ℓ+1)(−i)^ℓ j_ℓ(qρ)P_ℓ(q̂·ρ̂), with ρ = r − R. Then the traceless (ℓ = 2) part of ∂_α∂_β(1/ρ) couples to j₂(qρ) ≈ (qρ)²/15.
For a spherical core density this gives an eκ correction ∝ q²∫n(ρ)ρ⁻¹d³ρ relative to n(0). That is O((q a_core)²), with a_core ≈ a₀/Z_κ
(Si 1s: 1/a_core ≈ 52 keV). So 𝓜³_κκ∣_{V_eN} = −(m_e/M_κ)𝓜³_eκ is exact for the δ-function (trace) part at any q, and for the full
moments only as q a_core → 0. WP2v2-C11d sets the phase to 1 by hand ("contact: phase → 1"), which is exactly the missing hypothesis.
**Correction:** add "q ≪ Z_κ/a₀ (q → 0 of WP0-v2 (4.7))" to the relation and to IF-1. Say that in the multiphonon and impulse window
(q ≈ 10–300 keV) the κκ and eκ third moments are **not** related by −m_e/M_κ. The κκ closed form (i) still holds there.

**A8. Cubic isotropy (item 25).** Φ_κκ(0,t) = q·𝒯_κ(t)·q with 𝒯_κ(t) = Σ_{Qν}e_κνe_κν†[(n+1)e^{−iωt} + n e^{iωt}]/(2NM_κω). This is a rank-2
tensor invariant under the site group, so on T_d it is ∝ 𝟙 and S_inc depends only on ∣q∣, at all n_ph and T. ✓ 2411.03433 (full text) restricts
to n ≥ 2 and finds negligible Si and GaAs modulation. The theorem predicts exactly zero for that part, so the explanation stands.

**A9. Minor items.**
(a) Item 3: at T > 0, Φ_acoustic(ΔR) ~ T/ΔR, so Σ_{ΔR}∣Φ∣² ~ ∫R²dR/R² diverges linearly. Call it "absolutely divergent, finite as a lattice
Fourier sum away from q = G", not "conditionally convergent". The flag (§12 gap 3) is otherwise right.
(b) Item 19: the right side of the third line of (6.1) needs the factor (2π/Ω)∣c_κ∣²; otherwise Δ must be defined from the normalised S_self.
(c) Item 14: 2205.02250 says "the true peak is shifted slightly from the result (38)". A peak is a mode, so there is no error to report.
Reword L6 "Discrepancy" as "Clarification".
(d) (2.2): the "two-phonon contact term 1911.03482" and the 1910.08092 Eq. (90) factor π/Ω were not verified (paper not fetched). UNRESOLVED.
(e) Item 22: (7.1)'s incoherent part also contains an n_ph = 0 elastic spin-incoherent δ(ω) term (zero measure for DM). S̃_self should be
said to start at n_ph ≥ 1.

## Literature claims of error, rated
| Paper, location | Package claim | Rating |
|---|---|---|
| 2607.24933 Eq. (47) | isotropic 1/3 weight wrong in coherent sum | CONFIRMED (polarisation); intra-cell part outside paper's scope |
| 1712.06598 Eq. (5) (with (6), (7)) | spurious 1/V_cell | CONFIRMED |
| 1712.06598 Eq. (12) | equal-mass eigenvectors, spurious LO ∝ (√A₁ − √A₂)² | CONFIRMED (declared rough estimate; negligible) |
| 2309.10839 Eq. (9) | e^{−W_d} should be e^{−2W_d} | CONFIRMED |
| 2009.13534 after Eq. (31) | drops nonzero unordered-spin (incoherent) channel | CONFIRMED |
| 2205.02250 below Eq. (38) | "peak shift" is the mode, not the mean | REFUTED as a discrepancy (source is correct) |
| 2411.03433 §IA | isotropic IA width (q̂ = ẑ) is an omission | CONFIRMED as fact; it is a declared approximation |

## Required corrections (summary)
1. (2.4) and its proof, L5 chain, §0 item 2: add all inter-sublattice shells with weight j_BZ(ΔR + r_κ − r_κ′); restrict "incoherent = BZ
   average" to Bravais lattices; downgrade the WP2v2-C9 statement.
2. (5.2′)(c), §0 item 6, IF-1: qualify the −m_e/M_κ relation by q a_core ≪ 1 (WP0-v2 (4.7)'s q → 0). State that it fails in the keV window.
3. §3.3: quote 2607.24933's "monoatomic, isotropic" caveat and drop the intra-cell-phase charge against Eq. (47).
4. L6 and (5.1): 2205.02250 "peak" is not a discrepancy. L19: 2411.03433's q̂ = ẑ is a declared approximation.
5. (3.4′): give the species-weighted form for polyatomic targets. (6.1): give the normalisation. §2: T > 0 shell sum wording.
